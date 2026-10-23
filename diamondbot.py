"""
DIAMOND BOT - paper trades EVERY AGREE DOTS diamond on SPY + QQQ, 1/2/3/5-minute charts, through Alpaca PAPER.
PAPER ONLY - the paper=True switch in main() is hard-coded. Keys come from GitHub Secrets ALPACA_KEY / ALPACA_SECRET.

TWO BOOKS (logged separately so they can be compared head to head):
  YOURS : TTM 20 / ATR 14 / avg 5 / depth 1 - Vix Fix 22 / 50 / avg 10 / turn 50 - both turns within 2 candles
  TUNED : TTM 30 / ATR 14 / avg 3 / depth 1 - Vix Fix 30 / 50 / avg 5 / turn 70 - both turns on the same candle
DIAMOND = exact AGREE DOTS math on the closed candle (extended hours feed the indicators, like the chart).
  green diamond -> LONG (calls), red diamond -> SHORT (puts).
ENTRY : 9:45 - 14:30 ET, 0DTE AT THE MONEY, about $1,000 per trade (the contract count closest to $1,000 at the ask).
        One trade per book per chart. Same-direction diamond while in = ignored. OPPOSITE diamond = close + flip.
EXITS : every trade runs ALL 6 exit plans at once, decided on the stock price (checked every 5 seconds):
        P1 +$0.50 / -$0.50 | P2 +$1.00 / stop past the swing | P3 ride to the opposite diamond / stop past the swing
        P4 +$1.00 / -$0.50 | P5 +$0.30 / -$0.30           | P6 +$0.50 / stop past the swing
        Swing = $0.05 past the last 10 candles' low (longs) / high (shorts) on that chart. 30-minute time stop on every plan.
        Contracts are dealt to the plans in that order (P1, P2, ... P6, then P1 again). A plan with NO contract is still run:
        its exit is logged at the option's live mid price (shadow) - so every plan gets a real option result on every trade.
        Everything is flat by 15:55.
FULL RECORD:
  diamond_signals.csv - every diamond on every chart and book, its readings, and what the bot did with it
  diamond_trades.csv  - one row per exit plan per trade (real or shadow), stock + option prices, $ and %
  diamond_fills.csv   - every order sent, with the bid / ask at that moment
  diamond_state.json  - open trades (so the next scheduled run takes over)
"""
import csv
import json
import math
import os
import sys
import time
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd

# ===== SETTINGS (edit here) =====
SYMBOLS = ["SPY", "QQQ"]
TFS = [1, 2, 3, 5]
BOOKS = {"YOURS": (20, 14, 5, 1.0, 22, 50, 10, 50, 2),
         "TUNED": (30, 14, 3, 1.0, 30, 50, 5, 70, 1)}
DOLLARS = 1000.0             # per trade (the contract count closest to this at the ask)
MAX_QTY = 40                 # safety cap on contracts per trade
PLANS = [("P1 +0.50/-0.50", 0.50, 0.50, False),
         ("P2 +1.00/swing", 1.00, "swing", False),
         ("P3 ride/swing", None, "swing", True),
         ("P4 +1.00/-0.50", 1.00, 0.50, False),
         ("P5 +0.30/-0.30", 0.30, 0.30, False),
         ("P6 +0.50/swing", 0.50, "swing", False)]
HOLD_MIN = 30
SWING_N, SWING_BUF = 10, 0.05
ENTRY_FROM, ENTRY_TO, END_AT = 945, 1430, 1555
CHECK_SECS = 5
HIST_DAYS = 6
RUN_MINUTES = 340
TRADES_LOG = "diamond_trades.csv"
SIGNALS_LOG = "diamond_signals.csv"
FILLS_LOG = "diamond_fills.csv"
STATE = "diamond_state.json"

ET = ZoneInfo("America/New_York")
KEY = os.getenv("ALPACA_KEY", "").strip()
SECRET = os.getenv("ALPACA_SECRET", "").strip()


def now_et():
    return datetime.now(ET)


def sleep(s):
    time.sleep(s)


def log(msg):
    print(now_et().strftime("%H:%M:%S"), msg, flush=True)


def hhmm(dt):
    return dt.hour * 100 + dt.minute


def append_csv(path, row):
    new = not os.path.exists(path)
    with open(path, "a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(row.keys()))
        if new:
            w.writeheader()
        w.writerow(row)


def save_state(trades, day):
    with open(STATE, "w") as f:
        json.dump(dict(day=day.isoformat(), trades=trades), f, indent=1, default=str)


def load_state(day):
    try:
        with open(STATE) as f:
            s = json.load(f)
        if s.get("day") == day.isoformat():
            return s.get("trades", {})
    except Exception:
        pass
    return {}


# ===== AGREE DOTS diamond math (same as TradingView + the backtest) =====
def linreg_last(y, n):
    y = np.asarray(y, dtype=float)
    out = np.full(len(y), np.nan)
    if len(y) < n:
        return out
    x = np.arange(n, dtype=float)
    xm = x.mean()
    sxx = ((x - xm) ** 2).sum()
    yy = np.nan_to_num(y)
    sy = np.convolve(yy, np.ones(n), "valid")
    sxy = np.convolve(yy, x[::-1], "valid")
    slope = (sxy - xm * sy) / sxx
    out[n - 1:] = sy / n - slope * xm + slope * (n - 1)
    bad = pd.Series(np.isnan(y)).rolling(n).max().to_numpy()[n - 1:] > 0
    out[n - 1:][bad] = np.nan
    return out


def diamonds(df, st):
    """bull / bear diamond flags per candle + the readings arrays, for one book's settings"""
    L_, AL, aL, td, lb_, hl_, mL, vd, w = st
    hS, lS, cS = df["high"], df["low"], df["close"]
    sh = lambda x, k: np.r_[np.full(k, np.nan), x[:-k]]
    tr = pd.concat([hS - lS, (hS - cS.shift(1)).abs(), (lS - cS.shift(1)).abs()], axis=1).max(axis=1)
    tr.iloc[0] = hS.iloc[0] - lS.iloc[0]
    mid = ((hS.rolling(L_).max() + lS.rolling(L_).min()) / 2 + cS.rolling(L_).mean()) / 2
    mom = linreg_last((cS - mid).to_numpy(), L_)
    atr = tr.ewm(alpha=1 / AL, adjust=False).mean().to_numpy()
    m = np.nan_to_num(np.where(atr > 0, mom / atr, 0.0))
    av = pd.Series(m).ewm(span=aL, adjust=False).mean().to_numpy()
    av1, av2 = sh(av, 1), sh(av, 2)
    tu = (av > av1) & (av1 <= av2) & (av1 <= -td)
    tdn = (av < av1) & (av1 >= av2) & (av1 >= td)
    hc, lc = cS.rolling(lb_).max(), cS.rolling(lb_).min()
    wvf, wvs = (hc - lS) / hc * 100, (hS - lc) / lc * 100
    F = np.nan_to_num((wvf / wvf.rolling(hl_).max() * 100).to_numpy())
    G = np.nan_to_num((wvs / wvs.rolling(hl_).max() * 100).to_numpy())
    gA = pd.Series(G).ewm(span=mL, adjust=False).mean().to_numpy()
    fA = pd.Series(F).ewm(span=mL, adjust=False).mean().to_numpy()
    gA1, fA1, gA2, fA2 = sh(gA, 1), sh(fA, 1), sh(gA, 2), sh(fA, 2)
    fT = (fA1 >= vd) & (fA < fA1) & (fA1 >= fA2)
    gT = (gA1 >= vd) & (gA < gA1) & (gA1 >= gA2)
    n = len(df)
    ar = np.arange(n)

    def since(x):
        return ar - np.maximum.accumulate(np.where(x, ar, -10 ** 6))
    s_tu, s_td, s_fT, s_gT = since(tu), since(tdn), since(fT), since(gT)
    bull = (tu & (s_fT < w)) | (fT & (s_tu < w))
    bear = (tdn & (s_gT < w)) | (gT & (s_td < w))
    p1 = lambda x: np.r_[False, x[:-1]]
    p2 = lambda x: np.r_[False, False, x[:-2]]
    bullM = bull & ~p1(bull) & ~p2(bull)
    bearM = bear & ~p1(bear) & ~p2(bear)
    R = dict(av1=av1, m=m, fA1=fA1, gA1=gA1, F=F, G=G, s_tu=s_tu, s_td=s_td, s_fT=s_fT, s_gT=s_gT)
    return bullM, bearM, R


def readings(df, R, i, side):
    """what the diamond showed when it fired (side: 1 long / -1 short)"""
    h, l = df["high"].to_numpy(), df["low"].to_numpy()
    st_, ot_ = (R["F"], R["G"]) if side == 1 else (R["G"], R["F"])
    vpk = R["fA1"][i] if side == 1 else R["gA1"][i]
    s_t = R["s_tu"][i] if side == 1 else R["s_td"][i]
    s_v = R["s_fT"][i] if side == 1 else R["s_gT"][i]
    first = "same candle" if s_t == s_v else ("TTM first" if s_t > s_v else "VIX FIX first")
    lo = max(0, i - 19)
    return dict(ttm_peak=round(abs(float(R["av1"][i])), 2), ttm_now=round(float(R["m"][i]) * -side, 2),
                vix_avg_peak=round(float(vpk), 1), stretched_now=round(float(st_[i]), 1), other_now=round(float(ot_[i]), 1),
                first=first, run20=round(float(h[lo:i + 1].max() - l[lo:i + 1].min()), 2))


# ===== Data =====
def to_tf(df1, tf):
    g = df1.groupby(df1.index.floor(f"{tf}min"))
    out = pd.DataFrame({"open": g["open"].first(), "high": g["high"].max(), "low": g["low"].min(),
                        "close": g["close"].last(), "volume": g["volume"].sum()})
    return out.dropna()


def fetch_1m(dc, start, end):
    from alpaca.data.enums import DataFeed
    from alpaca.data.requests import StockBarsRequest
    from alpaca.data.timeframe import TimeFrame
    req = StockBarsRequest(symbol_or_symbols=SYMBOLS, timeframe=TimeFrame.Minute, start=start, end=end, feed=DataFeed.IEX)
    df = dc.get_stock_bars(req).df
    out = {}
    if df is None or df.empty:
        return out
    for sym in SYMBOLS:
        try:
            d = df.xs(sym, level=0) if isinstance(df.index, pd.MultiIndex) else df
        except KeyError:
            continue
        d = d.sort_index()
        d.index = d.index.tz_convert(ET)
        hm = d.index.hour * 100 + d.index.minute
        out[sym] = d[(hm >= 400) & (hm < 2000)][["open", "high", "low", "close", "volume"]].astype(float)
    return out


class Bars:
    """1-minute history per symbol: loaded once, then topped up every minute"""

    def __init__(self, dc):
        self.dc = dc
        now = now_et().astimezone(timezone.utc)
        self.d = fetch_1m(dc, now - timedelta(days=HIST_DAYS), now)

    def refresh(self):
        now = now_et().astimezone(timezone.utc)
        new = fetch_1m(self.dc, now - timedelta(minutes=30), now)
        for sym, d in new.items():
            old = self.d.get(sym)
            self.d[sym] = d if old is None else pd.concat([old[~old.index.isin(d.index)], d]).sort_index()

    def closed(self, sym, tf, now):
        """the tf candles that have fully closed by `now`"""
        d = self.d.get(sym)
        if d is None or not len(d):
            return None
        d = d[d.index + pd.Timedelta(minutes=1) <= now]
        c = to_tf(d, tf)
        return c[c.index + pd.Timedelta(minutes=tf) <= now]


def stock_prices(dc, syms):
    from alpaca.data.enums import DataFeed
    from alpaca.data.requests import StockLatestTradeRequest
    out = {}
    try:
        r = dc.get_stock_latest_trade(StockLatestTradeRequest(symbol_or_symbols=list(syms), feed=DataFeed.IEX))
        for s in syms:
            if s in r:
                out[s] = float(r[s].price)
    except Exception as e:
        log(f"stock price failed: {e}")
    return out


# ===== Options + orders =====
def pick_atm(tc, sym, side, spot, today):
    from alpaca.trading.enums import ContractType
    from alpaca.trading.requests import GetOptionContractsRequest
    req = GetOptionContractsRequest(
        underlying_symbols=[sym], expiration_date_gte=today, expiration_date_lte=today + timedelta(days=7),
        type=ContractType.CALL if side == 1 else ContractType.PUT,
        strike_price_gte=str(round(spot - 6, 2)), strike_price_lte=str(round(spot + 6, 2)), limit=1000)
    cs = tc.get_option_contracts(req).option_contracts or []
    if not cs:
        return None
    exp = min(pd.Timestamp(x.expiration_date).date() for x in cs)
    cs = [x for x in cs if pd.Timestamp(x.expiration_date).date() == exp]
    return min(cs, key=lambda x: (abs(float(x.strike_price) - spot), float(x.strike_price)))


def quote(oc, contract):
    """(bid, ask, mid) or (None, None, None)"""
    from alpaca.data.requests import OptionLatestQuoteRequest
    try:
        qs = oc.get_option_latest_quote(OptionLatestQuoteRequest(symbol_or_symbols=[contract]))
        q = qs.get(contract) if hasattr(qs, "get") else qs[contract]
        bid, ask = float(q.bid_price or 0), float(q.ask_price or 0)
        mid = (bid + ask) / 2 if bid > 0 and ask > 0 else (ask or bid or None)
        return (bid or None), (ask or None), mid
    except Exception as e:
        log(f"quote failed {contract}: {e}")
        return None, None, None


def contracts_for(ask):
    if not ask or ask <= 0:
        return 1
    x = DOLLARS / (ask * 100)
    lo, hi = max(1, math.floor(x)), max(1, math.ceil(x))
    q = lo if abs(lo * ask * 100 - DOLLARS) <= abs(hi * ask * 100 - DOLLARS) else hi
    return min(q, MAX_QTY)


def status_of(o):
    return str(getattr(o.status, "value", o.status)).lower()


def market(tc, oc, contract, qty, buy, why):
    from alpaca.trading.enums import OrderSide, TimeInForce
    from alpaca.trading.requests import MarketOrderRequest
    bid, ask, _ = quote(oc, contract)
    fill = None
    try:
        o = tc.submit_order(MarketOrderRequest(symbol=contract, qty=qty, side=OrderSide.BUY if buy else OrderSide.SELL,
                                               time_in_force=TimeInForce.DAY))
        for _ in range(60):
            o = tc.get_order_by_id(o.id)
            if status_of(o) == "filled" and o.filled_avg_price is not None:
                fill = float(o.filled_avg_price)
                break
            if status_of(o) in ("canceled", "rejected", "expired"):
                log(f"order {status_of(o)}: {'BUY' if buy else 'SELL'} {qty} {contract}")
                break
            sleep(0.5)
    except Exception as e:
        log(f"order failed ({'BUY' if buy else 'SELL'} {qty} {contract}): {e}")
    t = now_et()
    append_csv(FILLS_LOG, dict(date=t.strftime("%Y-%m-%d"), time=t.strftime("%H:%M:%S"), contract=contract,
                               action="BUY" if buy else "SELL", qty=qty, fill=fill if fill is not None else "",
                               bid=bid or "", ask=ask or "", reason=why))
    return fill, bid, ask


# ===== Trades =====
def deal(qty):
    k = len(PLANS)
    return [qty // k + (1 if i < qty % k else 0) for i in range(k)]


def open_trade(tc, oc, key, book, sym, tf, side, spot, swing_px, sig, today):
    try:
        c = pick_atm(tc, sym, side, spot, today)
    except Exception as e:
        log(f"{key}: option lookup failed: {e}")
        return None, "option lookup failed"
    if not c:
        return None, "no contract found"
    bid, ask, mid = quote(oc, c.symbol)
    qty = contracts_for(ask or mid)
    fill, fb, fa = market(tc, oc, c.symbol, qty, True, f"{book} {sym} {tf}m {'GREEN' if side == 1 else 'RED'} diamond")
    if fill is None:
        return None, "buy order failed"
    plans = []
    for (nm, tgt, stp, ride), q in zip(PLANS, deal(qty)):
        stop_px = swing_px if stp == "swing" else spot - side * stp
        plans.append(dict(name=nm, qty=q, target=None if tgt is None else round(spot + side * tgt, 2),
                          stop=round(stop_px, 2), ride=ride, open=True))
    tr = dict(key=key, book=book, sym=sym, tf=tf, side=side, contract=c.symbol, strike=float(c.strike_price), qty=qty,
              fill=fill, bid=fb, ask=fa, spot=spot, swing=round(swing_px, 2), t=now_et().isoformat(), plans=plans, sig=sig)
    log(f"ENTER {key} {'LONG - CALLS' if side == 1 else 'SHORT - PUTS'}: BUY {qty} {c.symbol} @ {fill:.2f} "
        f"(${fill * 100 * qty:,.0f}) | {sym} {spot:.2f}, swing stop {swing_px:.2f} | plans {deal(qty)}")
    return tr, "ENTER"


def close_plan(tc, oc, tr, p, reason, spot):
    """exit one plan: sell its contracts (real) or log the live mid (shadow)"""
    if p["qty"] > 0:
        px, bid, ask = market(tc, oc, tr["contract"], p["qty"], False, f"{tr['key']} {p['name']} {reason}")
        if px is None:
            return False
        real = 1
    else:
        bid, ask, px = quote(oc, tr["contract"])
        if px is None:
            px = ""
        real = 0
    p["open"] = False
    t0 = datetime.fromisoformat(tr["t"])
    t = now_et()
    pts = round((spot - tr["spot"]) * tr["side"], 2) if spot else ""
    per = round((px - tr["fill"]) * 100, 2) if px != "" else ""
    s = tr.get("sig", {})
    append_csv(TRADES_LOG, dict(
        date=t.strftime("%Y-%m-%d"), book=tr["book"], ticker=tr["sym"], tf=tr["tf"], side="LONG" if tr["side"] == 1 else "SHORT",
        contract=tr["contract"], strike=tr["strike"], plan=p["name"], real=real, contracts=p["qty"],
        entry_time=t0.strftime("%H:%M:%S"), exit_time=t.strftime("%H:%M:%S"), minutes=round((t - t0).total_seconds() / 60, 1),
        reason=reason, stock_entry=round(tr["spot"], 2), target=p["target"] if p["target"] is not None else "", stop=p["stop"],
        stock_exit=round(spot, 2) if spot else "", stock_pts=pts, opt_entry=tr["fill"], opt_exit=px if px == "" else round(px, 2),
        opt_bid_exit=bid or "", opt_ask_exit=ask or "", pnl_per_contract=per,
        pnl_usd=round(per * p["qty"], 2) if per != "" else "", pnl_pct=round((px / tr["fill"] - 1) * 100, 1) if px != "" else "",
        trade_contracts=tr["qty"], trade_cost=round(tr["fill"] * 100 * tr["qty"], 2),
        **{k: s.get(k, "") for k in ("ttm_peak", "ttm_now", "vix_avg_peak", "stretched_now", "other_now", "first", "run20")}))
    log(f"  {tr['key']} {p['name']} {reason} | {'SELL ' + str(p['qty']) if real else 'shadow'} @ {px if px == '' else round(px, 2)} | "
        f"stock {pts} | ${per if per == '' else round(per * max(1, p['qty']), 2)}{'' if real else ' (1 contract, shadow)'}")
    return True


def manage(tc, oc, trades, spots, now):
    """every few seconds: targets, stops, time stops"""
    changed = False
    for key, tr in list(trades.items()):
        s = spots.get(tr["sym"])
        age = (now - datetime.fromisoformat(tr["t"])).total_seconds() / 60
        for p in tr["plans"]:
            if not p["open"]:
                continue
            why = None
            if s is not None:
                if p["target"] is not None and (s - p["target"]) * tr["side"] >= 0:
                    why = "target"
                elif (s - p["stop"]) * tr["side"] <= 0:
                    why = "stop"
            if why is None and age >= HOLD_MIN:
                why = "time"
            if why and close_plan(tc, oc, tr, p, why, s):
                changed = True
        if not any(p["open"] for p in tr["plans"]):
            del trades[key]
            changed = True
    return changed


def close_all(tc, oc, tr, reason, spot):
    for p in tr["plans"]:
        if p["open"]:
            close_plan(tc, oc, tr, p, reason, spot)
    return not any(p["open"] for p in tr["plans"])


def recover_check(tc, trades):
    try:
        held = {p.symbol: abs(int(float(p.qty))) for p in tc.get_all_positions()}
    except Exception as e:
        log(f"positions check failed: {e}")
        return trades
    for key, tr in list(trades.items()):
        if held.get(tr["contract"], 0) <= 0 and any(p["open"] and p["qty"] > 0 for p in tr["plans"]):
            log(f"{key}: saved trade {tr['contract']} is no longer held - forgetting it")
            del trades[key]
        else:
            log(f"{key}: taking over open trade {tr['contract']} x{tr['qty']}")
    return trades


# ===== Signals on a closed candle =====
def on_candle(tc, oc, trades, bars, sym, tf, now, today, spots):
    c = bars.closed(sym, tf, now)
    if c is None or len(c) < 200:
        return False
    i = len(c) - 1
    t_close = c.index[i] + pd.Timedelta(minutes=tf)
    if (now - t_close).total_seconds() > 90:          # stale candle (data gap) - do not trade it
        return False
    changed = False
    for book, st in BOOKS.items():
        try:
            bull, bear, R = diamonds(c, st)
        except Exception as e:
            log(f"{book} {sym} {tf}m: diamond math failed: {e}")
            continue
        side = 1 if bull[i] else -1 if bear[i] else 0
        if side == 0:
            continue
        key = f"{book} {sym} {tf}m"
        sig = readings(c, R, i, side)
        spot = spots.get(sym) or float(c["close"].iloc[-1])
        lo = max(0, i - SWING_N + 1)
        swing = (float(c["low"].iloc[lo:i + 1].min()) - SWING_BUF) if side == 1 else (float(c["high"].iloc[lo:i + 1].max()) + SWING_BUF)
        cur = trades.get(key)
        action = ""
        if cur and cur["side"] == side:
            action = "ignored - already in this direction"
        else:
            if cur:
                changed = True
                if not close_all(tc, oc, cur, "opposite diamond", spot):
                    action = "opposite diamond - could not close the open trade (kept, no flip)"
                    log(f"DIAMOND {key} -> {action}")
                    append_csv(SIGNALS_LOG, dict(date=today.isoformat(), candle=c.index[i].strftime("%H:%M"), closed=t_close.strftime("%H:%M"),
                                                 seen=now.strftime("%H:%M:%S"), book=book, ticker=sym, tf=tf,
                                                 diamond="GREEN" if side == 1 else "RED", candle_close=round(float(c["close"].iloc[-1]), 2),
                                                 spot=round(spot, 2), swing_stop=round(swing, 2), action=action, **sig))
                    continue
                del trades[key]
                action = "closed the open trade (opposite diamond)"
            in_win = ENTRY_FROM <= hhmm(t_close) < ENTRY_TO and hhmm(now) < ENTRY_TO + 1
            if not in_win:
                action = (action + " | " if action else "") + "outside the entry window (9:45-14:30)"
            else:
                tr, res = open_trade(tc, oc, key, book, sym, tf, side, spot, swing, sig, today)
                if tr:
                    trades[key] = tr
                    changed = True
                action = (action + " | " if action else "") + (("FLIP - " if cur else "") + res)
        log(f"DIAMOND {key} {'GREEN' if side == 1 else 'RED'} candle {c.index[i]:%H:%M} close {c['close'].iloc[-1]:.2f} -> {action}")
        append_csv(SIGNALS_LOG, dict(date=today.isoformat(), candle=c.index[i].strftime("%H:%M"), closed=t_close.strftime("%H:%M"),
                                     seen=now.strftime("%H:%M:%S"), book=book, ticker=sym, tf=tf,
                                     diamond="GREEN" if side == 1 else "RED", candle_close=round(float(c["close"].iloc[-1]), 2),
                                     spot=round(spot, 2), swing_stop=round(swing, 2), action=action, **sig))
    return changed


# ===== Check mode: recent diamonds per chart / book (compare with the chart) =====
def check(tc, dc, oc):
    log("CHECK MODE - no trades")
    a = tc.get_account()
    log(f"account {a.status} | buying power ${a.buying_power} | options level {getattr(a, 'options_trading_level', '?')}")
    bars = Bars(dc)
    now = now_et()
    for sym in SYMBOLS:
        for tf in TFS:
            c = bars.closed(sym, tf, now)
            if c is None or len(c) < 200:
                log(f"{sym} {tf}m: not enough candles ({0 if c is None else len(c)})")
                continue
            for book, st in BOOKS.items():
                bull, bear, _ = diamonds(c, st)
                hm = c.index.hour * 100 + c.index.minute
                idx = np.nonzero((bull | bear) & (hm >= 930) & (hm < 1600))[0]
                last_day = c.index[-1].date()
                td = [i for i in idx if c.index[i].date() == last_day]
                txt = ", ".join(f"{c.index[i] + pd.Timedelta(minutes=tf):%H:%M} {'G' if bull[i] else 'R'}" for i in td)
                log(f"{book} {sym} {tf}m - {len(td)} diamonds on {last_day} (time = candle close): {txt}")
    try:
        cs = pick_atm(tc, "SPY", 1, stock_prices(dc, ["SPY"]).get("SPY", 0) or float(bars.d["SPY"]["close"].iloc[-1]), now.date())
        if cs:
            b, a_, m = quote(oc, cs.symbol)
            log(f"option check: {cs.symbol} bid {b} ask {a_} -> {contracts_for(a_ or m)} contracts for ${DOLLARS:,.0f}")
    except Exception as e:
        log(f"option check failed: {e}")
    log("CHECK OK - keys work")


# ===== Main loop =====
def main():
    from alpaca.data.historical import OptionHistoricalDataClient, StockHistoricalDataClient
    from alpaca.trading.client import TradingClient
    if not KEY or not SECRET:
        log("Missing ALPACA_KEY / ALPACA_SECRET secrets in the repo settings.")
        sys.exit(1)
    tc = TradingClient(KEY, SECRET, paper=True)   # PAPER ONLY - never change this
    dc = StockHistoricalDataClient(KEY, SECRET)
    oc = OptionHistoricalDataClient(KEY, SECRET)
    if os.getenv("MODE", "run") == "check":
        return check(tc, dc, oc)
    run_loop(tc, dc, oc)


def run_loop(tc, dc, oc):
    from alpaca.trading.requests import GetCalendarRequest
    t_start = time.time()
    today = now_et().date()
    cal = tc.get_calendar(GetCalendarRequest(start=today, end=today))
    if not cal:
        log("Market closed today.")
        return
    close_dt = cal[0].close
    if not isinstance(close_dt, datetime):
        close_dt = datetime.combine(today, close_dt)
    close_dt = close_dt.replace(tzinfo=ET) if close_dt.tzinfo is None else close_dt.astimezone(ET)
    end_dt = min(now_et().replace(hour=END_AT // 100, minute=END_AT % 100, second=0, microsecond=0), close_dt - timedelta(minutes=5))
    log(f"DIAMOND bot | {', '.join(SYMBOLS)} on {TFS} m | books {list(BOOKS)} | ~${DOLLARS:,.0f}/trade ATM 0DTE | "
        f"6 exit plans | entries {ENTRY_FROM}-{ENTRY_TO} | flat {end_dt:%H:%M}")
    trades = recover_check(tc, load_state(today))
    save_state(trades, today)
    bars = None
    while True:
        now = now_et()
        if time.time() - t_start > RUN_MINUTES * 60:
            log("Run time limit - the next scheduled run takes over (open trades are saved).")
            break
        if now >= end_dt:
            spots = stock_prices(dc, {tr["sym"] for tr in trades.values()}) if trades else {}
            for key, tr in list(trades.items()):
                if close_all(tc, oc, tr, "close", spots.get(tr["sym"])):
                    del trades[key]
            save_state(trades, today)
            log("Done for today.")
            break
        if hhmm(now) < 930:
            if hhmm(now) < 820:
                log("Too early, exiting.")
                break
            sleep(20)
            continue
        if bars is None:
            try:
                bars = Bars(dc)
                log(f"history loaded: " + ", ".join(f"{s} {len(d)} 1m bars" for s, d in bars.d.items()))
            except Exception as e:
                log(f"history failed: {e}")
                sleep(10)
                continue
        nxt = now.replace(second=0, microsecond=0) + timedelta(minutes=1, seconds=6)
        while True:
            rem = (nxt - now_et()).total_seconds()
            if rem <= 0:
                break
            if trades:
                spots = stock_prices(dc, {tr["sym"] for tr in trades.values()})
                if manage(tc, oc, trades, spots, now_et()):
                    save_state(trades, today)
            sleep(min(rem, CHECK_SECS) if trades else rem)
        now = now_et()
        want = now.replace(second=0, microsecond=0) - timedelta(minutes=1)     # the 1m bar that just closed
        ok = False
        for _ in range(6):
            try:
                bars.refresh()
            except Exception as e:
                log(f"bars refresh failed: {e}")
            d0 = bars.d.get(SYMBOLS[0])
            if d0 is not None and len(d0) and d0.index[-1] >= want:
                ok = True
                break
            sleep(3)
        if not ok:
            log(f"no {want:%H:%M} bar yet - skipping this minute")
            continue
        closing = [tf for tf in TFS if now.minute % tf == 0]
        spots = stock_prices(dc, SYMBOLS)
        changed = False
        for sym in SYMBOLS:
            for tf in closing:
                try:
                    changed |= on_candle(tc, oc, trades, bars, sym, tf, now, today, spots)
                except Exception as e:
                    log(f"{sym} {tf}m: candle check failed: {e}")
        if changed:
            save_state(trades, today)
    save_state(trades, today)
    summary(today)


def summary(today):
    if not os.path.exists(TRADES_LOG):
        log("No trades logged yet.")
        return
    df = pd.read_csv(TRADES_LOG)
    td = df[df["date"] == today.isoformat()]
    lines = [f"## Diamond bot - {today}"]
    real = td[td["real"] == 1]
    lines.append(f"Today: {td.groupby(['book', 'ticker', 'tf', 'entry_time']).ngroups} trades | real P&L **${real['pnl_usd'].sum():+,.2f}** "
                 f"| all time real: ${df[df['real'] == 1]['pnl_usd'].sum():+,.2f}")
    lines += ["", "### Every exit plan today (option % per contract, real + shadow)", "| Book | Plan | Exits | Win % | Avg option % | Real $ |",
              "|---|---|---|---|---|---|"]
    for (b, p), g in td.groupby(["book", "plan"]):
        pp = pd.to_numeric(g["pnl_pct"], errors="coerce")
        lines.append(f"| {b} | {p} | {len(g)} | {100 * (pp > 0).mean():.0f}% | {pp.mean():+.1f}% | "
                     f"{pd.to_numeric(g['pnl_usd'], errors='coerce')[g['real'] == 1].sum():+,.2f} |")
    text = "\n".join(lines)
    log("\n" + text)
    s = os.getenv("GITHUB_STEP_SUMMARY")
    if s:
        with open(s, "a") as f:
            f.write(text + "\n")


if __name__ == "__main__":
    main()

