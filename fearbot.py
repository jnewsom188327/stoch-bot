"""
FEAR SNAP BOT - paper trades Fear Snap v4.3 fires on SPY and QQQ (1-minute chart) through Alpaca PAPER.
PAPER ONLY - the paper=True switch in main() is hard-coded. Keys come from GitHub Secrets ALPACA_KEY / ALPACA_SECRET.

SIGNAL: Fear Snap v4.3 (SNAP + STRETCH + RETEST, longs need fear divergence), fires 9:40 - 14:30 ET on a 1m close.
        Long fire = CALLS, short fire = PUTS. One trade per ticker at a time.
YOUR PLAN (settings below):
  BUY    : 10 contracts, first strike OUT of the money, 0DTE.
  AVERAGE DOWN: if SPY/QQQ moves 1.5 ATR against the entry before the +25% sale -> buy 10 more.
  NOT AVERAGED: option +25% -> sell 7. The last 3 run until the option falls 15% from its best,
                or makes no new high for 3 minutes, or 30 minutes after entry - whichever comes first.
  AVERAGED   : sell all 20 at +10% over the new average price, or all at -30% from the average,
               or at 30 minutes after entry.
  ALSO   : nothing sold yet at 30 minutes -> sell all | flat 5 min before the close.
SHADOW : every trade also logs what would have happened with NO averaging down
         (all 10 sold at the moment the 1.5 ATR trigger hit), so you can compare the two plans.
Option prices for the % rules = middle of bid/ask. Orders are market orders (paper fills).
Data = Alpaca's free IEX feed, so a fire can occasionally differ from the TradingView chart.
Logs: fear_trades.csv (one row per finished trade), fear_fills.csv (every buy/sell), fear_state.json (open trades).
"""
import csv
import json
import os
import sys
import time
from datetime import date, datetime, timedelta, timezone
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd
from numpy.lib.stride_tricks import sliding_window_view as swv

# ===== SETTINGS (edit here) =====
SYMBOLS = ["SPY", "QQQ"]
QTY = 10                     # contracts on entry
ADD_QTY = 10                 # contracts added when averaging down
ADD_ATR = 1.5                # average down when the stock moves this many ATR against the entry
TP_PCT = 25                  # not averaged: option up this % -> sell PARTIAL_QTY
PARTIAL_QTY = 7
TRAIL_PCT = 15               # runners: sell if the option falls this % from its best
STALL_MIN = 3                # runners: sell if no new high for this many minutes
AVG_TP_PCT = 10              # averaged: sell all at +this % over the average
AVG_SL_PCT = 30              # averaged: sell all at -this % from the average
MAX_HOLD_MIN = 30            # everything out by this many minutes after entry
OTM_STEPS = 1                # 1 = first strike out of the money
FLAT_MIN = 5                 # sell everything this many minutes before the close
CHECK_SECS = 5               # how often prices are checked while a trade is open
DIRECTION = 0                # 0 = calls + puts, 1 = calls only, -1 = puts only

RUN_MINUTES = 340            # GitHub allows 6 h per run; the next scheduled run takes over from fear_state.json
TRADES_LOG = "fear_trades.csv"
FILLS_LOG = "fear_fills.csv"
STATE = "fear_state.json"

# Fear Snap v4.3 settings (match the TradingView indicator)
P = dict(pd=22, rng=50, maxLvl=95, zeroLvl=5, holdLvl=91, resetLvl=60, recentBars=3,
         spdLen=200, spdMult=2.0, spdFloor=8, longDiv=True, shortDiv=False, divBars=90, divTol=0.5,
         strMin=2.0, strLook=10, strAge=3,
         retLook=60, retSkip=5, retTol=0.4, retRatio=0.8, retMinSt=1.0,
         hotLen=300, hotPct=90, maxChase=1.5, coolBars=3,
         stLen=20, zLen=300, st=(1.0, 1.5, 2.0, 2.5), atrLen=14)
TYPES = {1: "SNAP", 2: "STRETCH", 3: "RETEST"}

ET = ZoneInfo("America/New_York")
KEY = os.getenv("ALPACA_KEY", "").strip()
SECRET = os.getenv("ALPACA_SECRET", "").strip()


def now_et():
    return datetime.now(ET)


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


# ===== Fear Snap v4.3 math (same as the backtest / TradingView) =====
def norm(x, n):
    hi, lo = x.rolling(n).max(), x.rolling(n).min()
    return np.where(hi == lo, 50.0, (x - lo) / (hi - lo) * 100)


def pct_rank(a, n):
    out = np.full(len(a), np.nan)
    if len(a) <= n:
        return out
    w = swv(a[:-1], n)
    cur = a[n:]
    for s in range(0, len(cur), 20000):
        e = s + 20000
        out[n + s:n + e] = (w[s:e] <= cur[s:e, None]).sum(1) / n * 100
    return out


def bars_ago_of_ext(a, n, highest=True):
    out = np.full(len(a), np.nan)
    if len(a) < n:
        return out
    w = swv(np.nan_to_num(a, nan=-np.inf if highest else np.inf), n)[:, ::-1]
    out[n - 1:] = (w.argmax(1) if highest else w.argmin(1))
    return out


def indicators(df):
    c, h, l = df.close, df.high, df.low
    hc, lc = c.rolling(P["pd"]).max(), c.rolling(P["pd"]).min()
    d = pd.DataFrame(index=df.index)
    d["fr"] = (hc - l) / hc * 100
    d["gr"] = (h - lc) / lc * 100
    d["fear"] = norm(d.fr, P["rng"])
    d["greed"] = norm(d.gr, P["rng"])
    fC = pd.Series(norm((hc - c) / hc * 100, P["rng"]), index=df.index)
    gC = pd.Series(norm((c - lc) / lc * 100, P["rng"]), index=df.index)
    d["dF"], d["dG"] = fC.shift(1) - fC, gC.shift(1) - gC
    d["nF"] = (fC - fC.shift(1)).abs().rolling(P["spdLen"]).mean()
    d["nG"] = (gC - gC.shift(1)).abs().rolling(P["spdLen"]).mean()
    tr = pd.concat([h - l, (h - c.shift(1)).abs(), (l - c.shift(1)).abs()], axis=1).max(1)
    d["atr"] = tr.ewm(alpha=1 / P["atrLen"], adjust=False).mean()
    d["ema"] = c.ewm(span=P["stLen"], adjust=False).mean()
    hlc3 = (h + l + c) / 3
    day = df.t.dt.date
    pv = (hlc3 * df.volume).groupby(day).cumsum()
    vv = df.volume.groupby(day).cumsum()
    d["vwap"] = (pv / vv.replace(0, np.nan)).ffill().fillna(c)
    d["sdE"] = (c - d.ema).rolling(P["zLen"]).std(ddof=0)
    d["sdV"] = (c - d.vwap).rolling(P["zLen"]).std(ddof=0)
    d["fPct"] = pct_rank(d.fr.to_numpy(float), P["hotLen"])
    d["gPct"] = pct_rank(d.gr.to_numpy(float), P["hotLen"])
    d["fHot"] = pd.Series(d.fPct).rolling(P["strLook"]).max()
    d["gHot"] = pd.Series(d.gPct).rolling(P["strLook"]).max()
    L, S = P["strLook"], P["retSkip"]
    d["loN"], d["hiN"] = l.rolling(L).min(), h.rolling(L).max()
    d["agoLo"] = bars_ago_of_ext(l.to_numpy(float), L, False)
    d["agoHi"] = bars_ago_of_ext(h.to_numpy(float), L, True)
    hS, lS = h.shift(S), l.shift(S)
    d["pHi"], d["pLo"] = hS.rolling(P["retLook"]).max(), lS.rolling(P["retLook"]).min()
    d["hiOff"] = S + bars_ago_of_ext(hS.to_numpy(float), P["retLook"], True)
    d["loOff"] = S + bars_ago_of_ext(lS.to_numpy(float), P["retLook"], False)
    d["hiR"], d["loR"] = h.rolling(S).max(), l.rolling(S).min()
    d["gNow"], d["fNow"] = d.gr.rolling(S).max(), d.fr.rolling(S).max()
    m = df.t.dt.hour * 60 + df.t.dt.minute
    d["mktOk"] = (m >= 580) & (m < 870)          # fires 9:40 - 14:30
    return d


def signals(df, d):
    """Bar-by-bar Fear Snap state machine. Returns [(bar index, +1 long / -1 short, type, stretch score)]."""
    n = len(df)
    A = {k: d[k].to_numpy(float) for k in d.columns if d[k].dtype != bool}
    ok = d["mktOk"].to_numpy(bool)
    c, h, l = df.close.to_numpy(float), df.high.to_numpy(float), df.low.to_numpy(float)
    st = P["st"]

    def dist(ext, dr, i):
        dE = ((A["ema"][i] - ext) if dr == 1 else (ext - A["ema"][i])) / A["sdE"][i]
        dV = ((A["vwap"][i] - ext) if dr == 1 else (ext - A["vwap"][i])) / A["sdV"][i]
        return max(dE, dV)

    def score(x):
        if np.isnan(x):
            return 0
        return 5 if x >= st[3] else 4 if x >= st[2] else 3 if x >= st[1] else 2 if x >= st[0] else 1

    state, lastMax, ext, pk, lastFire = 0, None, np.nan, np.nan, -10**9
    pPkL = pExL = pPkS = pExS = np.nan
    pEndL = pEndS = None
    fires = []
    warm = max(P["zLen"], P["hotLen"], P["spdLen"], P["retLook"] + P["retSkip"]) + 2
    for i in range(warm, n):
        atr = A["atr"][i]
        if np.isnan(atr) or np.isnan(A["fear"][i]) or np.isnan(A["sdE"][i]) or atr <= 0:
            continue
        fr, gr, fear, greed = A["fr"][i], A["gr"][i], A["fear"][i], A["greed"][i]
        old = state
        peakNow = max(pk, fr) if state == 1 else max(pk, gr) if state == -1 else np.nan
        extNow = min(ext, l[i]) if state == 1 else max(ext, h[i]) if state == -1 else np.nan
        divL = pEndL is not None and i - pEndL <= P["divBars"] and extNow <= pExL + P["divTol"] * atr and peakNow < pPkL
        divS = pEndS is not None and i - pEndS <= P["divBars"] and extNow >= pExS - P["divTol"] * atr and peakNow < pPkS
        recent = lastMax is not None and i - lastMax <= P["recentBars"]
        aL = (state == 1 and recent and A["dF"][i] >= max(P["spdMult"] * A["nF"][i], P["spdFloor"])
              and c[i] - extNow <= P["maxChase"] * atr and (not P["longDiv"] or divL))
        aS = (state == -1 and recent and A["dG"][i] >= max(P["spdMult"] * A["nG"][i], P["spdFloor"])
              and extNow - c[i] <= P["maxChase"] * atr and (not P["shortDiv"] or divS))
        stLo, stHi = dist(A["loN"][i], 1, i), dist(A["hiN"][i], -1, i)
        bL = (A["fHot"][i] >= P["hotPct"] and stLo >= P["strMin"] and A["agoLo"][i] <= P["strAge"]
              and c[i] > h[i - 1] and c[i] - A["loN"][i] <= P["maxChase"] * atr)
        bS = (A["gHot"][i] >= P["hotPct"] and stHi >= P["strMin"] and A["agoHi"][i] <= P["strAge"]
              and c[i] < l[i - 1] and A["hiN"][i] - c[i] <= P["maxChase"] * atr)
        cL = cS = False
        if not np.isnan(A["hiOff"][i]):
            j = i - int(A["hiOff"][i])
            cS = (A["gPct"][j] >= P["hotPct"] and A["hiR"][i] >= A["pHi"][i] - P["retTol"] * atr
                  and A["gNow"][i] < A["gr"][j] * P["retRatio"] and dist(A["hiR"][i], -1, i) >= P["retMinSt"]
                  and c[i] < l[i - 1] and A["hiR"][i] - c[i] <= P["maxChase"] * atr)
        if not np.isnan(A["loOff"][i]):
            j = i - int(A["loOff"][i])
            cL = (A["fPct"][j] >= P["hotPct"] and A["loR"][i] <= A["pLo"][i] + P["retTol"] * atr
                  and A["fNow"][i] < A["fr"][j] * P["retRatio"] and dist(A["loR"][i], 1, i) >= P["retMinSt"]
                  and c[i] > h[i - 1] and c[i] - A["loR"][i] <= P["maxChase"] * atr)
        canFire = i - lastFire > P["coolBars"]
        fired = False
        if (aL or bL or cL) and canFire and ok[i]:
            ty = 1 if aL else 3 if cL else 2
            sc = score(dist(extNow, 1, i)) if aL else score(dist(A["loR"][i], 1, i)) if cL else score(stLo)
            fires.append((i, 1, ty, sc))
            fired = True
        if (aS or bS or cS) and canFire and ok[i]:
            ty = 1 if aS else 3 if cS else 2
            sc = score(dist(extNow, -1, i)) if aS else score(dist(A["hiR"][i], -1, i)) if cS else score(stHi)
            fires.append((i, -1, ty, sc))
            fired = True
        if fired:
            state, lastFire = 0, i
        if state == 1:
            lastMax = i if fear >= P["holdLvl"] else lastMax
            ext, pk = min(ext, l[i]), max(pk, fr)
            state = 0 if fear < P["resetLvl"] else state
        elif state == -1:
            lastMax = i if greed >= P["holdLvl"] else lastMax
            ext, pk = max(ext, h[i]), max(pk, gr)
            state = 0 if greed < P["resetLvl"] else state
        if i - lastFire > P["coolBars"]:
            if fear >= P["maxLvl"] and greed <= P["zeroLvl"] and state != 1:
                state, lastMax, ext, pk = 1, i, l[i], fr
            elif greed >= P["maxLvl"] and fear <= P["zeroLvl"] and state != -1:
                state, lastMax, ext, pk = -1, i, h[i], gr
        if old == 1 and state != 1:
            pPkL, pExL, pEndL = peakNow, extNow, i
        if old == -1 and state != -1:
            pPkS, pExS, pEndS = peakNow, extNow, i
    return fires


def last_fire(d1):
    """Fear Snap on the 1m bars. Returns (side, type, score, atr, spot) if the LAST closed candle fired, else None."""
    df = d1.copy()
    df["t"] = df.index
    df = df.reset_index(drop=True)
    if len(df) < 700:
        return None
    d = indicators(df)
    last = [f for f in signals(df, d) if f[0] == len(df) - 1]
    if not last:
        return None
    i, side, ty, sc = last[0]
    return side, ty, sc, float(d["atr"].iloc[i]), float(df["close"].iloc[i])


# ===== Data =====
def get_1m(dc):
    """Closed 1-minute bars (pre/post market included, like the TradingView chart) for all SYMBOLS."""
    from alpaca.data.enums import DataFeed
    from alpaca.data.requests import StockBarsRequest
    from alpaca.data.timeframe import TimeFrame
    now = datetime.now(timezone.utc)
    req = StockBarsRequest(symbol_or_symbols=SYMBOLS, timeframe=TimeFrame.Minute,
                           start=now - timedelta(days=6), end=now, feed=DataFeed.IEX)
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
        d = d[d.index + pd.Timedelta(minutes=1) <= pd.Timestamp(now).tz_convert(ET)]
        hm = d.index.hour * 100 + d.index.minute
        out[sym] = d[(hm >= 400) & (hm < 2000)][["open", "high", "low", "close", "volume"]].astype(float)
    return out


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
def pick_otm(tc, sym, side, spot, exp):
    from alpaca.trading.enums import ContractType
    from alpaca.trading.requests import GetOptionContractsRequest
    req = GetOptionContractsRequest(
        underlying_symbols=[sym], expiration_date=exp,
        type=ContractType.CALL if side == 1 else ContractType.PUT,
        strike_price_gte=str(int(spot - 15)), strike_price_lte=str(int(spot + 15)), limit=200)
    cs = tc.get_option_contracts(req).option_contracts or []
    if side == 1:
        c = sorted([x for x in cs if float(x.strike_price) > spot], key=lambda x: float(x.strike_price))
    else:
        c = sorted([x for x in cs if float(x.strike_price) < spot], key=lambda x: -float(x.strike_price))
    return c[OTM_STEPS - 1] if len(c) >= OTM_STEPS else None


def mids(oc, syms):
    from alpaca.data.requests import OptionLatestQuoteRequest
    out = {}
    if not syms:
        return out
    try:
        qs = oc.get_option_latest_quote(OptionLatestQuoteRequest(symbol_or_symbols=list(syms)))
        for s in syms:
            q = qs.get(s) if hasattr(qs, "get") else None
            if q is None:
                continue
            bid, ask = float(q.bid_price or 0), float(q.ask_price or 0)
            m = (bid + ask) / 2 if bid > 0 and ask > 0 else (ask or bid or None)
            if m:
                out[s] = m
    except Exception as e:
        log(f"quote failed: {e}")
    return out


def status_of(o):
    return str(getattr(o.status, "value", o.status)).lower()


def market(tc, contract, qty, buy):
    """Market order; returns the average fill price or None."""
    from alpaca.trading.enums import OrderSide, TimeInForce
    from alpaca.trading.requests import MarketOrderRequest
    try:
        o = tc.submit_order(MarketOrderRequest(symbol=contract, qty=qty, side=OrderSide.BUY if buy else OrderSide.SELL,
                                               time_in_force=TimeInForce.DAY))
    except Exception as e:
        log(f"order failed ({'BUY' if buy else 'SELL'} {qty} {contract}): {e}")
        return None
    for _ in range(60):
        o = tc.get_order_by_id(o.id)
        if status_of(o) == "filled" and o.filled_avg_price is not None:
            return float(o.filled_avg_price)
        if status_of(o) in ("canceled", "rejected", "expired"):
            log(f"order {status_of(o)}: {'BUY' if buy else 'SELL'} {qty} {contract}")
            return None
        time.sleep(0.5)
    log(f"order not filled after 30 s: {contract}")
    return None


def fill_row(tr, action, qty, px, reason):
    append_csv(FILLS_LOG, dict(date=now_et().strftime("%Y-%m-%d"), time=now_et().strftime("%H:%M:%S"),
                               ticker=tr["sym"], contract=tr["contract"], action=action, qty=qty,
                               price=round(px, 2), reason=reason))


# ===== Trade management =====
def enter(tc, sym, side, ty, sc, atr, spot, exp):
    try:
        c = pick_otm(tc, sym, side, spot, exp)
    except Exception as e:
        log(f"{sym}: option lookup failed: {e}")
        return None
    if not c:
        log(f"{sym}: no {'call' if side == 1 else 'put'} found for {exp}")
        return None
    fill = market(tc, c.symbol, QTY, True)
    if fill is None:
        return None
    t = now_et()
    tr = dict(sym=sym, side=side, trigger=TYPES[ty], score=sc, contract=c.symbol, strike=float(c.strike_price),
              qty=QTY, max_qty=QTY, fill=fill, avg=fill, atr=atr, spot=spot, t=t.isoformat(),
              averaged=False, partial=False, peak=fill, peak_t=t.isoformat(),
              realized=0.0, shadow=None, best=0.0, worst=0.0, last_reason="")
    fill_row(tr, "BUY", QTY, fill, f"FEAR SNAP {TYPES[ty]} {'LONG' if side == 1 else 'SHORT'}")
    trig = spot - ADD_ATR * atr if side == 1 else spot + ADD_ATR * atr
    log(f"{sym} {TYPES[ty]} {'LONG - CALLS' if side == 1 else 'SHORT - PUTS'}: BUY {QTY} {c.symbol} @ {fill:.2f} | "
        f"{sym} {spot:.2f}, ATR {atr:.2f} | +{TP_PCT}% = {fill * (1 + TP_PCT / 100):.2f} | "
        f"average down if {sym} hits {trig:.2f}")
    return tr


def sell(tc, tr, qty, reason):
    px = market(tc, tr["contract"], qty, False)
    if px is None:
        return False
    pnl = (px - tr["avg"]) * 100 * qty
    tr["realized"] += pnl
    tr["qty"] -= qty
    tr["last_reason"] = reason
    fill_row(tr, "SELL", qty, px, reason)
    log(f"{tr['sym']} SELL {qty} {tr['contract']} @ {px:.2f} | {reason} | ${pnl:+.2f}")
    return True


def finish(tr):
    t0 = datetime.fromisoformat(tr["t"])
    shadow = tr["shadow"] if tr["averaged"] else tr["realized"]
    append_csv(TRADES_LOG, dict(
        date=now_et().strftime("%Y-%m-%d"), ticker=tr["sym"], side="CALL" if tr["side"] == 1 else "PUT",
        trigger=tr["trigger"], stretch=tr["score"], contract=tr["contract"],
        entry_time=t0.strftime("%H:%M"), exit_time=now_et().strftime("%H:%M"),
        minutes=round((now_et() - t0).total_seconds() / 60, 1), entry_fill=tr["fill"], avg_cost=round(tr["avg"], 3),
        contracts=tr["max_qty"], averaged_down="YES" if tr["averaged"] else "no", exit_reason=tr["last_reason"],
        pnl_usd=round(tr["realized"], 2), no_avg_down_pnl_usd=round(shadow, 2),
        best_pct=round(tr["best"], 1), worst_pct=round(tr["worst"], 1),
        spot_entry=round(tr["spot"], 2), atr=round(tr["atr"], 3)))
    log(f"{tr['sym']} TRADE DONE: ${tr['realized']:+.2f} (without averaging down: ${shadow:+.2f})")


def manage(tc, oc, dc, trades, flat_dt):
    """Every few seconds: average-down trigger, +25% sale, runners, averaged exits, 30-minute cap."""
    if not trades:
        return False
    q = mids(oc, {t["contract"] for t in trades.values()})
    spots = stock_prices(dc, {t["sym"] for t in trades.values()})
    now = now_et()
    changed = False
    for sym, tr in list(trades.items()):
        m = q.get(tr["contract"])
        if not m:
            continue
        pct = (m / tr["avg"] - 1) * 100
        tr["best"], tr["worst"] = max(tr["best"], pct), min(tr["worst"], pct)
        age = (now - datetime.fromisoformat(tr["t"])).total_seconds() / 60
        s = spots.get(sym)
        if now >= flat_dt:
            changed |= sell(tc, tr, tr["qty"], "FLAT before the close")
        elif tr["averaged"]:
            if m >= tr["avg"] * (1 + AVG_TP_PCT / 100):
                changed |= sell(tc, tr, tr["qty"], f"AVERAGED: +{AVG_TP_PCT}% over average")
            elif m <= tr["avg"] * (1 - AVG_SL_PCT / 100):
                changed |= sell(tc, tr, tr["qty"], f"AVERAGED: STOP -{AVG_SL_PCT}%")
            elif age >= MAX_HOLD_MIN:
                changed |= sell(tc, tr, tr["qty"], f"TIME {MAX_HOLD_MIN} min")
        elif tr["partial"]:
            if m > tr["peak"]:
                tr["peak"], tr["peak_t"] = m, now.isoformat()
                changed = True
            stall = (now - datetime.fromisoformat(tr["peak_t"])).total_seconds() / 60
            if m <= tr["peak"] * (1 - TRAIL_PCT / 100):
                changed |= sell(tc, tr, tr["qty"], f"RUNNERS: -{TRAIL_PCT}% from best")
            elif stall >= STALL_MIN:
                changed |= sell(tc, tr, tr["qty"], f"RUNNERS: no new high for {STALL_MIN} min")
            elif age >= MAX_HOLD_MIN:
                changed |= sell(tc, tr, tr["qty"], f"TIME {MAX_HOLD_MIN} min")
        else:
            against = None if s is None else ((tr["spot"] - s) if tr["side"] == 1 else (s - tr["spot"]))
            if against is not None and against >= ADD_ATR * tr["atr"]:
                tr["shadow"] = (m - tr["fill"]) * 100 * tr["qty"]          # the no-average-down plan exits here
                px = market(tc, tr["contract"], ADD_QTY, True)
                if px is not None:
                    tr["avg"] = (tr["avg"] * tr["qty"] + px * ADD_QTY) / (tr["qty"] + ADD_QTY)
                    tr["qty"] += ADD_QTY
                    tr["max_qty"] = tr["qty"]
                    tr["averaged"] = True
                    fill_row(tr, "BUY", ADD_QTY, px, f"AVERAGE DOWN ({sym} {s:.2f}, {ADD_ATR} ATR against)")
                    log(f"{sym} AVERAGE DOWN: BUY {ADD_QTY} @ {px:.2f} | new average {tr['avg']:.2f} | "
                        f"exit +{AVG_TP_PCT}% = {tr['avg'] * (1 + AVG_TP_PCT / 100):.2f}, "
                        f"stop -{AVG_SL_PCT}% = {tr['avg'] * (1 - AVG_SL_PCT / 100):.2f}")
                    changed = True
                else:
                    tr["shadow"] = None
            elif m >= tr["fill"] * (1 + TP_PCT / 100) and tr["qty"] > PARTIAL_QTY:
                if sell(tc, tr, PARTIAL_QTY, f"TARGET +{TP_PCT}%"):
                    tr["partial"], tr["peak"], tr["peak_t"] = True, m, now.isoformat()
                    changed = True
            elif age >= MAX_HOLD_MIN:
                changed |= sell(tc, tr, tr["qty"], f"TIME {MAX_HOLD_MIN} min")
        if tr["qty"] <= 0:
            finish(tr)
            del trades[sym]
            changed = True
    return changed


def recover_check(tc, trades):
    """Drop saved trades whose contracts are no longer held (sold by hand, expired...)."""
    try:
        held = {p.symbol: abs(int(float(p.qty))) for p in tc.get_all_positions()}
    except Exception as e:
        log(f"positions check failed: {e}")
        return trades
    for sym, tr in list(trades.items()):
        if held.get(tr["contract"], 0) <= 0:
            log(f"{sym}: saved trade {tr['contract']} is no longer held - forgetting it")
            del trades[sym]
        else:
            log(f"{sym}: taking over open trade {tr['contract']} x{tr['qty']} (avg {tr['avg']:.2f})")
    return trades


# ===== Check mode =====
def check(tc, dc, oc):
    log("CHECK MODE - no trades")
    a = tc.get_account()
    log(f"account {a.status} | cash ${a.cash} | buying power ${a.buying_power} | "
        f"options level {getattr(a, 'options_trading_level', '?')}")
    data = get_1m(dc)
    today = now_et().date()
    for sym in SYMBOLS:
        d1 = data.get(sym)
        if d1 is None or d1.empty:
            log(f"{sym}: no bars")
            continue
        df = d1.copy()
        df["t"] = df.index
        df = df.reset_index(drop=True)
        d = indicators(df)
        fires = signals(df, d)
        log(f"{sym}: {len(df)} 1m candles, last {d1.index[-1]:%m-%d %H:%M} | Fear Snap fires in the last 6 days: {len(fires)}")
        for i, side, ty, sc in fires[-5:]:
            log(f"   {df.t.iloc[i]:%m-%d %H:%M} {TYPES[ty]} {'LONG' if side == 1 else 'SHORT'} S{sc} @ {df.close.iloc[i]:.2f}")
        spot = float(d1["close"].iloc[-1])
        try:
            for side in (1, -1):
                c = pick_otm(tc, sym, side, spot, today)
                if c:
                    log(f"{sym} {spot:.2f}: 1st OTM {'call' if side == 1 else 'put'} {c.symbol} | "
                        f"mid {mids(oc, [c.symbol]).get(c.symbol, 0):.2f}")
                else:
                    log(f"{sym}: no {'call' if side == 1 else 'put'} for today (market closed / no expiry today)")
        except Exception as e:
            log(f"{sym}: option lookup failed: {e}")
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
    flat_dt = close_dt - timedelta(minutes=FLAT_MIN)
    log(f"Fear Snap bot | {', '.join(SYMBOLS)} 1m | buy {QTY} 1st OTM 0DTE | +{TP_PCT}% sell {PARTIAL_QTY}, runners "
        f"-{TRAIL_PCT}% / {STALL_MIN} min stall | average down {ADD_QTY} at {ADD_ATR} ATR against, then "
        f"+{AVG_TP_PCT}% / -{AVG_SL_PCT}% | max {MAX_HOLD_MIN} min | flat {flat_dt:%H:%M}")

    trades = recover_check(tc, load_state(today))
    save_state(trades, today)
    last_bar = {}
    while True:
        now = now_et()
        if time.time() - t_start > RUN_MINUTES * 60:
            log("Run time limit - the next scheduled run takes over (open trades are saved).")
            break
        if now >= close_dt + timedelta(minutes=1):
            log("Market closed - done for today.")
            break
        if hhmm(now) < 930:
            if hhmm(now) < 820:
                log("Too early, exiting.")
                break
            time.sleep(20)
            continue

        # wait for the next minute (+3 s), checking open trades every few seconds
        target = now.replace(second=0, microsecond=0) + timedelta(minutes=1, seconds=3)
        while True:
            rem = (target - now_et()).total_seconds()
            if rem <= 0:
                break
            if trades and manage(tc, oc, dc, trades, flat_dt):
                save_state(trades, today)
            time.sleep(min(rem, CHECK_SECS) if trades else rem)

        now = now_et()
        if now >= flat_dt:
            if trades and manage(tc, oc, dc, trades, flat_dt):
                save_state(trades, today)
            continue
        try:
            data = get_1m(dc)
        except Exception as e:
            log(f"bars failed: {e}")
            continue
        for sym in SYMBOLS:
            d1 = data.get(sym)
            if d1 is None or d1.empty or sym in trades:
                continue
            bar = d1.index[-1]
            if last_bar.get(sym) == bar:
                continue
            first_look = sym not in last_bar
            last_bar[sym] = bar
            if first_look and (now - (bar + pd.Timedelta(minutes=1))).total_seconds() > 75:
                continue                                        # old candle at start-up: don't act on it
            try:
                f = last_fire(d1)
            except Exception as e:
                log(f"{sym}: signal failed: {e}")
                continue
            if not f:
                continue
            side, ty, sc, atr, spot = f
            if DIRECTION != 0 and side != DIRECTION:
                continue
            log(f"{sym}: FEAR SNAP {TYPES[ty]} {'LONG' if side == 1 else 'SHORT'} (S{sc}) at {bar + pd.Timedelta(minutes=1):%H:%M} close {spot:.2f}")
            tr = enter(tc, sym, side, ty, sc, atr, spot, today)
            if tr:
                trades[sym] = tr
                save_state(trades, today)

    save_state(trades, today)
    summary(today)


def summary(today):
    if not os.path.exists(TRADES_LOG):
        log("No finished trades logged yet.")
        return
    rows = list(csv.DictReader(open(TRADES_LOG)))
    td = [r for r in rows if r["date"] == today.isoformat()]

    def tot(rs, k):
        return sum(float(r[k]) for r in rs if r[k] not in ("", "nan"))

    lines = [f"## Fear Snap bot - {today}",
             f"Today: {len(td)} trades, **${tot(td, 'pnl_usd'):+,.2f}** (without averaging down: ${tot(td, 'no_avg_down_pnl_usd'):+,.2f})",
             f"All time: {len(rows)} trades, **${tot(rows, 'pnl_usd'):+,.2f}** (without averaging down: ${tot(rows, 'no_avg_down_pnl_usd'):+,.2f})",
             "", "| Ticker | Side | Trigger | In | Out | Contracts | Avg down | Exit | $ | $ no avg down |",
             "|---|---|---|---|---|---|---|---|---|---|"]
    for r in td:
        lines.append(f"| {r['ticker']} | {r['side']} | {r['trigger']} | {r['entry_time']} | {r['exit_time']} | "
                     f"{r['contracts']} | {r['averaged_down']} | {r['exit_reason']} | {float(r['pnl_usd']):+.2f} | "
                     f"{float(r['no_avg_down_pnl_usd']):+.2f} |")
    text = "\n".join(lines)
    log("\n" + text)
    s = os.getenv("GITHUB_STEP_SUMMARY")
    if s:
        with open(s, "a") as f:
            f.write(text + "\n")


if __name__ == "__main__":
    main()
