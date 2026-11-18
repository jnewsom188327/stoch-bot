"""
FIRE BOT - paper trades the FIRE GRADE fires on SPY + QQQ (1-minute chart) through Alpaca PAPER.
PAPER ONLY - the paper=True switch in main() is hard-coded. Keys come from GitHub Secrets ALPACA_KEY / ALPACA_SECRET.

FIRES (same math as the backtest and the "Flow Fire + Pin Box" TradingView script, regular hours only):
  Clean VF turn  : ATR Vix Fix line (EMA 5) turns down from above its 85th percentile (390-bar window)
  PUT 5  = greed turn + red candle (close in lower half) + Stoch 9-3-3 hook down (>70) + TTM lower high
  PUT 4  = greed turn + red candle + Stoch 9-3-3 hook down + greed pinned (old 22/50 lines: greed >=80 with fear <=15)
  CALL 5 = fear turn + TTM higher low + 2x volume + old fear line turning down from >=80 (last 3 bars)
  Fires are checked 9:50 - 15:00 ET on the closed 1-minute candle.
SKIPS (each one helped in both halves of the backtest year):
  - lunch 11:00 - 12:59
  - quiet stretch: the last 10 days' average range is in the bottom third of the last 60 days
  - after a LOSING trade, that ticker is done for the day
  - one trade per ticker at a time (a fire while that ticker is already in a trade is logged, not traded)
TRADE : 1DTE (next expiration after today), 2 strikes in the money, market orders.
EXITS : PUT 5 after 15 min | PUT 4 after 45 min | CALL 5 after 90 min
        STOP: the stock trades $0.05*ATR past the last 6 candles' high (puts) / low (calls)  - checked every 5 seconds
        Everything is flat by 15:55.
SIZE  : KELLY x the bot's own bankroll per trade (KELLY = 1.0 = full Kelly = the whole free bankroll).
        The bankroll starts at START_BANKROLL and is tracked in fire_book.json, so it does not matter what else
        runs on the paper account. Run the workflow with reset = yes to put it back to the start.
FULL RECORD:
  fire_signals.csv - every fire, its grade and readings, and what the bot did with it (traded / skipped + why)
  fire_trades.csv  - one row per trade: stock + option prices, $ and %, bankroll before / after
  fire_fills.csv   - every order sent, with the bid / ask at that moment (to see the real fills)
  fire_state.json  - open trades (so the next scheduled run takes over)
  fire_book.json   - the bankroll
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

SYMBOLS = ["SPY", "QQQ"]
START_BANKROLL = 2500.0
KELLY = 1.0                  # fraction of the free bankroll per trade (1.0 = full Kelly)
MAX_QTY = 200                # safety cap on contracts per trade
ITM = 2                      # strikes in the money
HOLD = {"PUT 5": 15, "PUT 4": 45, "CALL 5": 90}
FIRE_FROM_K, FIRE_TO_K = 20, 330          # minutes after 9:30 (9:50 - 15:00), same as the backtest
LUNCH = (90, 210)                          # 11:00 - 12:59 skipped
FLAT_AT = 1555
CHECK_SECS = 5
RUN_MINUTES = 340
SIGNALS_LOG = "fire_signals.csv"
TRADES_LOG = "fire_trades.csv"
FILLS_LOG = "fire_fills.csv"
STATE = "fire_state.json"
BOOK = "fire_book.json"

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


def load_json(path, default):
    try:
        with open(path) as f:
            return json.load(f)
    except Exception:
        return default


def save_json(path, obj):
    with open(path, "w") as f:
        json.dump(obj, f, indent=1, default=str)


# ===== indicator math (identical to the backtest) =====
def ema(x, n):
    a = 2 / (n + 1)
    o = np.empty_like(x)
    o[0] = x[0]
    for i in range(1, len(x)):
        o[i] = o[i - 1] + a * (x[i] - o[i - 1])
    return o


def rmax(x, w):
    return pd.Series(x).rolling(w, min_periods=1).max().values


def rmin(x, w):
    return pd.Series(x).rolling(w, min_periods=1).min().values


def atrs(h, l, c):
    tr = np.maximum(h - l, np.r_[0, np.maximum(abs(h[1:] - c[:-1]), abs(l[1:] - c[:-1]))])
    tr[0] = h[0] - l[0]
    return pd.Series(tr).ewm(alpha=1 / 14, adjust=False).mean().values


def ttm(h, l, c):
    n = len(c)
    a = np.maximum(atrs(h, l, c), 0.01)
    hh = rmax(h, 20)
    ll = rmin(l, 20)
    sm = pd.Series(c).rolling(20, min_periods=1).mean().values
    d = c - ((hh + ll) / 2 + sm) / 2
    m = np.zeros(n)
    for i in range(4, n):
        w = min(20, i + 1)
        y = d[i - w + 1:i + 1]
        x = np.arange(w)
        b, a0 = np.polyfit(x, y, 1)
        m[i] = np.clip((a0 + b * (w - 1)) / a[i], -10, 10)
    return m


def fire_at(g, k):
    """g = today's 1m regular-hours bars indexed 0..k (k = the candle that just closed).
    Returns a list of fires on candle k: dict(name, side, stop, atr, readings)"""
    h, l, c, o, v = [g[x].values.astype(float) for x in ["high", "low", "close", "open", "volume"]]
    if k < FIRE_FROM_K or k > FIRE_TO_K or len(c) != k + 1:
        return []
    a = np.maximum(atrs(h, l, c), 1e-6)
    rng = np.maximum(h - l, 0.01)
    m = ttm(h, l, c)
    hc = rmax(c, 22)
    lc = rmin(c, 22)
    wf = (hc - l) / hc * 100
    wg = (h - lc) / lc * 100
    fA = ema(100 * wf / np.maximum(rmax(wf, 50), 1e-9), 10)
    gA = ema(100 * wg / np.maximum(rmax(wg, 50), 1e-9), 10)
    va = pd.Series(v).rolling(20, min_periods=5).mean().shift(1).values
    raw = 100 * (c - rmin(l, 9)) / np.maximum(rmax(h, 9) - rmin(l, 9), 1e-9)
    K = pd.Series(raw).rolling(3, min_periods=1).mean().values
    D = pd.Series(K).rolling(3, min_periods=1).mean().values
    out = []
    for side in (1, -1):
        x = ema(((rmax(c, 22) - l) if side == 1 else (h - rmin(c, 22))) / a, 5)
        thr = pd.Series(x).rolling(390, min_periods=30).quantile(.85).values
        if not (x[k - 1] >= thr[k - 1] and x[k] < x[k - 1] and x[k - 1] >= x[k - 2]):
            continue
        S_, O_ = (fA, gA) if side == 1 else (gA, fA)
        cur = np.zeros(k + 1, bool)
        cur[2:] = (S_[1:-1] >= 80) & (S_[2:] < S_[1:-1]) & (S_[1:-1] >= S_[:-2])
        if side == 1:
            hk = np.r_[False, (K[1:] > D[1:]) & (K[:-1] <= D[:-1])] & (pd.Series(K).rolling(3, min_periods=1).min().values < 30) & (K < 50)
        else:
            hk = np.r_[False, (K[1:] < D[1:]) & (K[:-1] >= D[:-1])] & (pd.Series(K).rolling(3, min_periods=1).max().values > 70) & (K > 50)
        hook = bool(hk[max(0, k - 2):k + 1].any())
        w0 = max(0, k - 30)
        j = w0 + int(np.argmin(l[w0:k - 5] if side == 1 else -h[w0:k - 5]))
        newx = (l[k - 3:k + 1].min() < l[j]) if side == 1 else (h[k - 3:k + 1].max() > h[j])
        ms = m * side
        div = bool(newx and ms[k - 3:k + 1].min() > ms[j])
        if side == 1:
            candle = bool(c[k] > o[k] and (c[k] - l[k]) / rng[k] >= .5)
        else:
            candle = bool(c[k] < o[k] and (h[k] - c[k]) / rng[k] >= .5)
        vol2x = bool(np.nanmax(v[k - 5:k + 1]) >= 2 * va[k]) if va[k] == va[k] else False
        both = bool(cur[max(0, k - 2):k + 1].any())
        pinned = bool(S_[max(0, k - 5):k + 1].max() >= 80 and O_[max(0, k - 5):k + 1].min() <= 15)
        name = None
        if side == -1 and candle and hook and div:
            name = "PUT 5"
        elif side == -1 and candle and hook and pinned:
            name = "PUT 4"
        elif side == 1 and div and vol2x and both:
            name = "CALL 5"
        ext = l[k - 5:k + 1].min() if side == 1 else h[k - 5:k + 1].max()
        out.append(dict(name=name, side=side, stop=float(ext - side * 0.05 * a[k]), atr=float(a[k]), close=float(c[k]),
                        candle=candle, stoch=hook, ttmdiv=div, vol2x=vol2x, oldline=both, pinned=pinned))
    return out


# ===== data =====
def today_1m(dc, sym, today):
    from alpaca.data.enums import DataFeed
    from alpaca.data.requests import StockBarsRequest
    from alpaca.data.timeframe import TimeFrame
    start = datetime.combine(today, datetime.min.time(), ET).replace(hour=9, minute=30).astimezone(timezone.utc)
    req = StockBarsRequest(symbol_or_symbols=[sym], timeframe=TimeFrame.Minute, start=start,
                           end=now_et().astimezone(timezone.utc), feed=DataFeed.IEX)
    df = dc.get_stock_bars(req).df
    if df is None or df.empty:
        return None
    d = df.xs(sym, level=0) if isinstance(df.index, pd.MultiIndex) else df
    d = d.sort_index()
    d.index = d.index.tz_convert(ET)
    d["k"] = (d.index.hour * 60 + d.index.minute) - 570
    d = d[(d.k >= 0) & (d.k < 390)]
    return d.groupby("k")[["open", "high", "low", "close", "volume"]].last()


def bars_upto(d, k):
    """0..k, gaps filled forward like the backtest"""
    return d.reindex(range(k + 1)).ffill().bfill()


def quiet_today(dc, sym, today):
    from alpaca.data.enums import DataFeed
    from alpaca.data.requests import StockBarsRequest
    from alpaca.data.timeframe import TimeFrame
    try:
        start = datetime.combine(today - timedelta(days=120), datetime.min.time(), timezone.utc)
        req = StockBarsRequest(symbol_or_symbols=[sym], timeframe=TimeFrame.Day, start=start,
                               end=datetime.combine(today, datetime.min.time(), timezone.utc), feed=DataFeed.IEX)
        df = dc.get_stock_bars(req).df
        d = df.xs(sym, level=0) if isinstance(df.index, pd.MultiIndex) else df
        d = d.sort_index()
        d = d[d.index.tz_convert(ET).date < today]
        r = ((d["high"] - d["low"]) / d["close"]).values
        prev, allr = r[-10:], r[-60:]
        if len(allr) <= 20:
            return False, None
        return bool(np.mean(prev) <= np.percentile(allr, 33)), round(float(np.mean(prev)) * 100, 2)
    except Exception as e:
        log(f"{sym} quiet check failed ({e}) - not skipping")
        return False, None


def spot_now(dc, sym):
    from alpaca.data.enums import DataFeed
    from alpaca.data.requests import StockLatestTradeRequest
    try:
        r = dc.get_stock_latest_trade(StockLatestTradeRequest(symbol_or_symbols=[sym], feed=DataFeed.IEX))
        return float(r[sym].price)
    except Exception as e:
        log(f"{sym} price failed: {e}")
        return None


# ===== options + orders =====
def pick_contract(tc, sym, side, spot, today):
    """1DTE (first expiration after today), 2 strikes in the money"""
    from alpaca.trading.enums import ContractType
    from alpaca.trading.requests import GetOptionContractsRequest
    want = round(spot) - ITM * side
    req = GetOptionContractsRequest(
        underlying_symbols=[sym], expiration_date_gte=today + timedelta(days=1), expiration_date_lte=today + timedelta(days=7),
        type=ContractType.CALL if side == 1 else ContractType.PUT,
        strike_price_gte=str(want - 3), strike_price_lte=str(want + 3), limit=1000)
    cs = tc.get_option_contracts(req).option_contracts or []
    if not cs:
        return None
    exp = min(pd.Timestamp(x.expiration_date).date() for x in cs)
    cs = [x for x in cs if pd.Timestamp(x.expiration_date).date() == exp]
    return min(cs, key=lambda x: abs(float(x.strike_price) - want))


def quote(oc, contract):
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
            time.sleep(0.5)
    except Exception as e:
        log(f"order failed ({'BUY' if buy else 'SELL'} {qty} {contract}): {e}")
    t = now_et()
    append_csv(FILLS_LOG, dict(date=t.strftime("%Y-%m-%d"), time=t.strftime("%H:%M:%S"), contract=contract,
                               action="BUY" if buy else "SELL", qty=qty, fill=fill if fill is not None else "",
                               bid=bid or "", ask=ask or "",
                               slip_vs_mid=round(fill - (bid + ask) / 2, 3) if fill and bid and ask else "", reason=why))
    return fill, bid, ask


# ===== bankroll =====
def load_book():
    b = load_json(BOOK, None)
    if not b or os.getenv("RESET", "no").lower() in ("yes", "y", "true", "1"):
        b = dict(start=START_BANKROLL, bankroll=START_BANKROLL, peak=START_BANKROLL, resets=(b or {}).get("resets", -1) + 1,
                 since=now_et().strftime("%Y-%m-%d"))
        save_json(BOOK, b)
        log(f"bankroll set to ${START_BANKROLL:,.0f}")
    return b


# ===== trades =====
def open_trade(tc, oc, dc, book, trades, sym, f, today, cand_time):
    spot = spot_now(dc, sym) or f["close"]
    risk = f["side"] * (spot - f["stop"])
    if not (0.2 * f["atr"] < risk <= 3 * f["atr"]):
        return "skip: stop too close/far from price (backtest rule)"
    c = pick_contract(tc, sym, f["side"], spot, today)
    if c is None:
        return "skip: no contract found"
    bid, ask, mid = quote(oc, c.symbol)
    px = ask or mid
    if not px or px < 0.29:
        return "skip: no usable quote"
    free = book["bankroll"] - sum(t["cost"] for t in trades.values())
    try:
        bp = float(tc.get_account().options_buying_power or tc.get_account().buying_power)
    except Exception:
        bp = free
    dollars = min(KELLY * free, bp * 0.98)
    qty = min(MAX_QTY, int(dollars // (px * 100)))
    if qty < 1:
        return f"skip: bankroll ${free:,.0f} can't buy 1 at ${px:.2f}"
    fill, b0, a0 = market(tc, oc, c.symbol, qty, True, f"{f['name']} entry")
    if fill is None:
        return "skip: entry order did not fill"
    t = now_et()
    trades[sym] = dict(sym=sym, name=f["name"], side=f["side"], contract=c.symbol, qty=qty, entry=fill,
                       cost=round(fill * 100 * qty, 2), entry_time=t.isoformat(), fire_time=cand_time,
                       exit_by=(t + timedelta(minutes=HOLD[f["name"]])).isoformat(), stop=round(f["stop"], 3),
                       entry_spot=spot, bank_before=round(book["bankroll"], 2), bid=b0, ask=a0)
    log(f"BUY {qty} {c.symbol} @ {fill} ({f['name']} {sym}) | ${fill * 100 * qty:,.0f} of ${book['bankroll']:,.0f} bankroll | "
        f"stop {sym} {f['stop']:.2f} | out by {(t + timedelta(minutes=HOLD[f['name']])):%H:%M}")
    return f"TRADED {qty}x {c.symbol} @ {fill}"


def close_trade(tc, oc, book, trades, done, sym, reason, spot):
    tr = trades[sym]
    fill, bid, ask = market(tc, oc, tr["contract"], tr["qty"], False, reason)
    if fill is None:
        _, _, mid = quote(oc, tr["contract"])
        if mid is None:
            log(f"could not close {tr['contract']} - will retry")
            return False
        fill = mid
        reason += " (no fill - logged at mid, CHECK POSITION)"
    pnl = (fill - tr["entry"]) * 100 * tr["qty"]
    book["bankroll"] = round(book["bankroll"] + pnl, 2)
    book["peak"] = max(book.get("peak", book["bankroll"]), book["bankroll"])
    save_json(BOOK, book)
    t = now_et()
    append_csv(TRADES_LOG, dict(date=t.strftime("%Y-%m-%d"), ticker=sym, fire=tr["name"], contract=tr["contract"], qty=tr["qty"],
                                fire_time=tr["fire_time"], entry_time=tr["entry_time"][11:19], exit_time=t.strftime("%H:%M:%S"),
                                entry_spot=tr["entry_spot"], exit_spot=spot or "", stop=tr["stop"], entry=tr["entry"], exit=fill,
                                pnl_pct=round(100 * (fill / tr["entry"] - 1), 2), pnl_usd=round(pnl, 2),
                                bank_before=tr["bank_before"], bank_after=book["bankroll"], why=reason))
    done[sym] = pnl
    log(f"SELL {tr['qty']} {tr['contract']} @ {fill} ({reason}) | {100 * (fill / tr['entry'] - 1):+.1f}% ${pnl:+,.0f} | bankroll ${book['bankroll']:,.0f}")
    del trades[sym]
    return True


def manage(tc, oc, dc, book, trades, done, force=None):
    changed = False
    for sym in list(trades):
        tr = trades[sym]
        spot = spot_now(dc, sym)
        reason = force
        if reason is None:
            if spot is not None and ((spot <= tr["stop"]) if tr["side"] == 1 else (spot >= tr["stop"])):
                reason = "stop"
            elif now_et() >= datetime.fromisoformat(tr["exit_by"]):
                reason = f"time {HOLD[tr['name']]}m"
        if reason and close_trade(tc, oc, book, trades, done, sym, reason, spot):
            changed = True
    return changed


def recover(tc, trades):
    """drop saved trades whose position is gone (e.g. closed by hand)"""
    try:
        held = {p.symbol for p in tc.get_all_positions()}
    except Exception:
        return trades
    for sym in list(trades):
        if trades[sym]["contract"] not in held:
            log(f"saved trade {trades[sym]['contract']} has no position - dropping it")
            del trades[sym]
    return trades


def check(tc, dc, oc):
    log("CHECK MODE - no trades")
    a = tc.get_account()
    log(f"account {a.status} | buying power ${a.buying_power} | options level {getattr(a, 'options_trading_level', '?')}")
    book = load_book()
    log(f"bankroll ${book['bankroll']:,.2f} (start ${book['start']:,.0f}, peak ${book.get('peak', 0):,.0f}, resets {book.get('resets', 0)})")
    today = now_et().date()
    for sym in SYMBOLS:
        q, rr = quiet_today(dc, sym, today)
        d = today_1m(dc, sym, today)
        n = 0 if d is None else len(d)
        found = []
        if d is not None and n:
            last = int(d.index.max())
            for k in range(FIRE_FROM_K, min(last, FIRE_TO_K) + 1):
                for f in fire_at(bars_upto(d, k), k):
                    if f["name"]:
                        found.append(f"{9 + (k + 31) // 60}:{(k + 31) % 60:02d} {f['name']}")
        log(f"{sym}: quiet={q} (10-day avg range {rr}%) | {n} bars today | fires: {', '.join(found) or 'none'}")
        spot = spot_now(dc, sym)
        if spot:
            for side in (1, -1):
                c = pick_contract(tc, sym, side, spot, today)
                if c:
                    b, a_, m = quote(oc, c.symbol)
                    log(f"  {c.symbol} bid {b} ask {a_}")
    log("CHECK OK - keys work")


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
    t0 = time.time()
    today = now_et().date()
    cal = tc.get_calendar(GetCalendarRequest(start=today, end=today))
    if not cal:
        log("Market closed today.")
        return
    close_dt = cal[0].close
    if not isinstance(close_dt, datetime):
        close_dt = datetime.combine(today, close_dt)
    close_dt = close_dt.replace(tzinfo=ET) if close_dt.tzinfo is None else close_dt.astimezone(ET)
    end_dt = min(now_et().replace(hour=FLAT_AT // 100, minute=FLAT_AT % 100, second=0, microsecond=0), close_dt - timedelta(minutes=5))
    book = load_book()
    st = load_json(STATE, {})
    if st.get("day") != today.isoformat():
        st = dict(day=today.isoformat(), trades={}, done={}, seen=[])
    trades, done, seen = recover(tc, st["trades"]), st["done"], set(st["seen"])

    def save():
        save_json(STATE, dict(day=today.isoformat(), trades=trades, done=done, seen=sorted(seen)))

    quiet = {s: quiet_today(dc, s, today) for s in SYMBOLS}
    lastturn = {}
    log(f"FIRE bot | {SYMBOLS} 1m | PUT 4-5 + CALL 5 | 1DTE {ITM} ITM | KELLY {KELLY} of bankroll ${book['bankroll']:,.2f} | "
        f"quiet: {', '.join(f'{s}={q[0]}' for s, q in quiet.items())} | flat {end_dt:%H:%M}")
    save()
    while True:
        now = now_et()
        if time.time() - t0 > RUN_MINUTES * 60:
            log("Run time limit - the next scheduled run takes over (open trades are saved).")
            break
        if now >= end_dt:
            manage(tc, oc, dc, book, trades, done, force="flat 15:55")
            save()
            log("Done for today.")
            break
        if hhmm(now) < 930:
            if hhmm(now) < 820:
                log("Too early, exiting.")
                break
            time.sleep(20)
            continue
        nxt = now.replace(second=0, microsecond=0) + timedelta(minutes=1, seconds=4)
        while (rem := (nxt - now_et()).total_seconds()) > 0:
            if trades and manage(tc, oc, dc, book, trades, done):
                save()
            time.sleep(min(rem, CHECK_SECS) if trades else rem)
        now = now_et()
        k = (now.hour * 60 + now.minute) - 570 - 1          # the candle that just closed
        if k < FIRE_FROM_K or k > FIRE_TO_K:
            continue
        for sym in SYMBOLS:
            try:
                d = None
                for _ in range(5):
                    d = today_1m(dc, sym, today)
                    if d is not None and len(d) and int(d.index.max()) >= k:
                        break
                    time.sleep(3)
                if d is None or not len(d) or int(d.index.max()) < k:
                    log(f"{sym}: no bar for minute {k} yet - skipping")
                    continue
                for f in fire_at(bars_upto(d.loc[:k], k), k):
                    lt = lastturn.get(f"{sym}{f['side']}", -99)
                    lastturn[f"{sym}{f['side']}"] = k
                    if not f["name"] or k - lt < 4:          # backtest: turns within 4 candles of the last one are ignored
                        continue
                    tag = f"{sym}-{k}-{f['side']}"
                    if tag in seen:
                        continue
                    seen.add(tag)
                    ct = f"{9 + (k + 31) // 60}:{(k + 31) % 60:02d}"
                    if LUNCH[0] <= k < LUNCH[1]:
                        what = "skip: lunch"
                    elif quiet[sym][0]:
                        what = "skip: quiet stretch"
                    elif sym in done and done[sym] < 0:
                        what = "skip: already lost on this ticker today"
                    elif sym in trades:
                        what = "skip: already in a trade on this ticker"
                    else:
                        what = open_trade(tc, oc, dc, book, trades, sym, f, today, ct)
                    log(f"{sym} {ct} {f['name']} -> {what}")
                    append_csv(SIGNALS_LOG, dict(date=today.isoformat(), time=ct, ticker=sym, fire=f["name"], price=f["close"],
                                                 stop=round(f["stop"], 3), candle=f["candle"], stoch=f["stoch"], ttmdiv=f["ttmdiv"],
                                                 vol2x=f["vol2x"], oldline=f["oldline"], pinned=f["pinned"], action=what))
                    save()
            except Exception as e:
                log(f"{sym}: fire check failed: {e}")
    save()
    summary(today, book)


def summary(today, book):
    lines = [f"## Fire bot - {today}", f"Bankroll **${book['bankroll']:,.2f}** (start ${book['start']:,.0f} on {book.get('since')}, "
             f"peak ${book.get('peak', 0):,.0f}, resets {book.get('resets', 0)})"]
    if os.path.exists(TRADES_LOG):
        df = pd.read_csv(TRADES_LOG)
        td = df[df["date"] == today.isoformat()]
        lines.append(f"Today: {len(td)} trades, ${td['pnl_usd'].sum():+,.2f} | all time: {len(df)} trades, "
                     f"win {100 * (df['pnl_usd'] > 0).mean():.0f}%, avg {df['pnl_pct'].mean():+.1f}%")
        lines += ["", "| Ticker | Fire | In | Out | Why | % | $ |", "|---|---|---|---|---|---|---|"]
        for _, r in td.iterrows():
            lines.append(f"| {r.ticker} | {r.fire} | {r.entry_time} | {r.exit_time} | {r.why} | {r.pnl_pct:+.1f}% | {r.pnl_usd:+,.0f} |")
    if os.path.exists(FILLS_LOG):
        fl = pd.read_csv(FILLS_LOG)
        s = pd.to_numeric(fl["slip_vs_mid"], errors="coerce")
        if s.notna().any():
            lines.append(f"\nFills: avg ${s.abs().mean():.3f} from the mid per contract ({s.notna().sum()} orders)")
    text = "\n".join(lines)
    log("\n" + text)
    p = os.getenv("GITHUB_STEP_SUMMARY")
    if p:
        with open(p, "a") as f:
            f.write(text + "\n")


if __name__ == "__main__":
    main()
