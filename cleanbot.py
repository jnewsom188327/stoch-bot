"""
CLEAN SCAN BOT - paper trades the Clean Mover Scan signals on 16 tickers (5-minute chart) through Alpaca PAPER.
PAPER ONLY - the paper=True switch in main() is hard-coded. Keys come from GitHub Secrets ALPACA_KEY / ALPACA_SECRET.

SIGNAL (same math as the TradingView "Clean Scan" indicator, on closed 5-minute candles, regular hours):
  LONG  : Clean >= 33, ADX >= 25, current leg clean >= 0.45, RVol >= 1.0, +DI > -DI and close > 20 EMA
  SHORT : same, but -DI > +DI and close < 20 EMA
  New entries 9:30 - 15:15 ET. One trade per ticker at a time. 3-bar cooldown after an exit.
TWO VERSIONS trade every signal side by side (2 contracts each), so you can compare them:
  A (runner) : 1st strike OTM | stop -25% | TP1 +25% sell 1 | last one rides until the scan exit
  B (quick)  : 2nd strike OTM | stop -10% | TP1 +10% sell 1 | TP2 +20% sell the last one
  BOTH       : calls on LONG, puts on SHORT, nearest expiration (0DTE on SPY/QQQ/IWM, nearest weekly on stocks)
               sell everything when the scan exit fires (trend flipped, lost the 20 EMA, ADX under 20,
               leg got choppy) | everything sold by 15:45 | % rules checked every 5 seconds
Option prices for the % rules = middle of bid/ask. Orders are market orders (paper fills).
Data = Alpaca's free IEX feed, so a signal can occasionally differ from the TradingView table.
Logs: clean_trades.csv (one row per sale) and clean_state.json (open trades, so the next run can take over).
"""
import csv
import json
import os
import sys
import time
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd

# ===== SETTINGS (edit here) =====
SYMBOLS = ["SPY", "QQQ", "IWM", "NVDA", "TSLA", "AAPL", "MSFT", "AMZN",
           "META", "GOOGL", "AMD", "AVGO", "PLTR", "COIN", "MSTR", "SMH"]
# otm = which strike out of the money | qty = contracts | sl/tp1/tp2 = option % (tp2 None = ride to the scan exit)
VERSIONS = {
    "A": dict(otm=1, qty=2, sl=25, tp1=25, tp1_qty=1, tp2=None),
    "B": dict(otm=2, qty=2, sl=10, tp1=10, tp1_qty=1, tp2=20),
}
MAX_DTE = 7                  # nearest expiration within this many days
DIRECTION = 0                # 0 = calls + puts, 1 = calls only, -1 = puts only
MAX_OPEN = 32                # max trades open at once (both versions count)
CHECK_SECS = 5               # how often the % rules are checked

# Clean Scan settings (match the TradingView indicator)
TF = 5                       # minutes per candle
W = 12                       # leg window (bars)
N = 390                      # "lately" average (bars)
CLEAN_MIN, ADX_IN, ER_IN, RV_MIN = 33.0, 25.0, 0.45, 1.0
ADX_OUT, ER_OUT, COOL_BARS = 20.0, 0.15, 3
ENTRY_FROM, ENTRY_TO = 930, 1515   # new entries (HHMM ET)
EXIT_AT = 1545                     # everything sold by this time

RUN_MINUTES = 340            # GitHub allows 6 h per run; the next scheduled run takes over from clean_state.json
LOG = "clean_trades.csv"
STATE = "clean_state.json"

ET = ZoneInfo("America/New_York")
KEY = os.getenv("ALPACA_KEY", "").strip()
SECRET = os.getenv("ALPACA_SECRET", "").strip()
WHY = {1: "trend flipped", 2: "lost the 20 EMA", 3: "trend fading (ADX)", 4: "leg got choppy", 5: "3:45 time exit"}


def now_et():
    return datetime.now(ET)


def log(msg):
    print(now_et().strftime("%H:%M:%S"), msg, flush=True)


def hhmm(dt):
    return dt.hour * 100 + dt.minute


def write_row(row):
    new = not os.path.exists(LOG)
    with open(LOG, "a", newline="") as f:
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


# ===== Clean Scan math (same as TradingView) =====
def rma(x, n):
    return x.ewm(alpha=1 / n, adjust=False).mean()


def scan(df):
    """Runs the Clean Scan state machine over the 5m candles.
    Returns (state series: 1 long / -1 short / 0 out, exit-reason series, latest numbers)."""
    c, h, l, v = df["close"], df["high"], df["low"], df["volume"]
    ema = c.ewm(span=20, adjust=False).mean()
    ch = (c - c.shift(W)).abs()
    path = (c - c.shift(1)).abs().rolling(W).sum()
    er = (ch / path.replace(0, np.nan)).fillna(0.0)
    clean = er.rolling(N).mean() * 100
    up, dn = h.diff(), -l.diff()
    pdm = pd.Series(np.where((up > dn) & (up > 0), up, 0.0), index=df.index)
    mdm = pd.Series(np.where((dn > up) & (dn > 0), dn, 0.0), index=df.index)
    tr = pd.concat([h - l, (h - c.shift(1)).abs(), (l - c.shift(1)).abs()], axis=1).max(axis=1)
    atr = rma(tr, 14)
    dp = 100 * rma(pdm, 14) / atr
    dm = 100 * rma(mdm, 14) / atr
    dx = 100 * (dp - dm).abs() / (dp + dm).replace(0, np.nan)
    adx = rma(dx.fillna(0), 14)
    rv = v.rolling(6).mean() / v.rolling(N).mean()
    hm = df.index.hour * 100 + df.index.minute
    inS = (hm >= 930) & (hm < EXIT_AT)
    inE = (hm >= ENTRY_FROM) & (hm < ENTRY_TO)

    st, why = np.zeros(len(df), dtype=int), np.zeros(len(df), dtype=int)
    s, cool = 0, 0
    C, E, A, R, ER_, DP, DM, CL = (x.to_numpy() for x in (c, ema, adx, rv, er, dp, dm, clean))
    for i in range(len(df)):
        cool = max(0, cool - 1)
        w_ = 0
        if s != 0:
            r = (5 if not inS[i] else 1 if (DM[i] > DP[i] if s == 1 else DP[i] > DM[i])
                 else 2 if (C[i] < E[i] if s == 1 else C[i] > E[i])
                 else 3 if A[i] < ADX_OUT else 4 if ER_[i] < ER_OUT else 0)
            if r:
                s, cool, w_ = 0, COOL_BARS, r
        elif (inE[i] and cool == 0 and CL[i] >= CLEAN_MIN and A[i] >= ADX_IN
              and ER_[i] >= ER_IN and R[i] >= RV_MIN):
            if DP[i] > DM[i] and C[i] > E[i]:
                s = 1
            elif DM[i] > DP[i] and C[i] < E[i]:
                s = -1
        st[i], why[i] = s, w_
    info = dict(clean=CL[-1], adx=A[-1], rv=R[-1], close=C[-1])
    return st, why, info


# ===== Data =====
def get_5m(dc):
    """Closed 5-minute candles, regular hours only (like the TradingView table), for all SYMBOLS."""
    from alpaca.data.enums import DataFeed
    from alpaca.data.requests import StockBarsRequest
    from alpaca.data.timeframe import TimeFrame, TimeFrameUnit
    now = datetime.now(timezone.utc)
    req = StockBarsRequest(symbol_or_symbols=SYMBOLS, timeframe=TimeFrame(TF, TimeFrameUnit.Minute),
                           start=now - timedelta(days=14), end=now, feed=DataFeed.IEX)
    df = dc.get_stock_bars(req).df
    out = {}
    if df is None or df.empty:
        return out
    cut = pd.Timestamp(now).tz_convert(ET)
    for sym in SYMBOLS:
        try:
            d = df.xs(sym, level=0) if isinstance(df.index, pd.MultiIndex) else df
        except KeyError:
            continue
        d = d.sort_index()
        d.index = d.index.tz_convert(ET)
        d = d[d.index + pd.Timedelta(minutes=TF) <= cut]                 # closed candles only
        hm = d.index.hour * 100 + d.index.minute
        out[sym] = d[(hm >= 930) & (hm < 1600)][["open", "high", "low", "close", "volume"]].astype(float)
    return out


# ===== Options + orders =====
def pick_otm(tc, sym, side, spot, today, steps):
    from alpaca.trading.enums import ContractType
    from alpaca.trading.requests import GetOptionContractsRequest
    width = max(5.0, spot * 0.08)
    req = GetOptionContractsRequest(
        underlying_symbols=[sym], expiration_date_gte=today, expiration_date_lte=today + timedelta(days=MAX_DTE),
        type=ContractType.CALL if side == 1 else ContractType.PUT,
        strike_price_gte=str(round(spot - width, 2)), strike_price_lte=str(round(spot + width, 2)), limit=1000)
    cs = tc.get_option_contracts(req).option_contracts or []
    if not cs:
        return None
    exp = min(pd.Timestamp(x.expiration_date).date() for x in cs)
    cs = [x for x in cs if pd.Timestamp(x.expiration_date).date() == exp]
    if side == 1:
        c = sorted([x for x in cs if float(x.strike_price) > spot], key=lambda x: float(x.strike_price))
    else:
        c = sorted([x for x in cs if float(x.strike_price) < spot], key=lambda x: -float(x.strike_price))
    return c[steps - 1] if len(c) >= steps else None


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


# ===== Trade management =====
def enter(tc, sym, side, info, today, ver):
    v = VERSIONS[ver]
    spot = info["close"]
    try:
        c = pick_otm(tc, sym, side, spot, today, v["otm"])
    except Exception as e:
        log(f"{sym} [{ver}]: option lookup failed: {e}")
        return None
    if not c:
        log(f"{sym} [{ver}]: no {'call' if side == 1 else 'put'} found")
        return None
    fill = market(tc, c.symbol, v["qty"], True)
    if fill is None:
        return None
    tp2 = f"TP2 {fill * (1 + v['tp2'] / 100):.2f}" if v["tp2"] else "runner rides to the scan exit"
    log(f"{sym} [{ver}] {'LONG - CALLS' if side == 1 else 'SHORT - PUTS'}: BUY {v['qty']} {c.symbol} (strike {c.strike_price}, "
        f"exp {c.expiration_date}) @ {fill:.2f} | {sym} {spot:.2f} | Clean {info['clean']:.0f}, ADX {info['adx']:.0f}, "
        f"RVol {info['rv']:.1f} | TP1 {fill * (1 + v['tp1'] / 100):.2f}, {tp2}, stop {fill * (1 - v['sl'] / 100):.2f}")
    return dict(sym=sym, ver=ver, side=side, contract=c.symbol, strike=float(c.strike_price), qty=v["qty"],
                qty0=v["qty"], fill=fill, spot=spot, clean=round(info["clean"], 1), adx=round(info["adx"], 1),
                t=now_et().isoformat(), tp1=False, best=0.0, worst=0.0)


def sell(tc, tr, qty, reason, spot=None):
    px = market(tc, tr["contract"], qty, False)
    if px is None:
        return False
    pnl = (px - tr["fill"]) * 100 * qty
    pct = (px / tr["fill"] - 1) * 100 if tr["fill"] else 0.0
    t0 = datetime.fromisoformat(tr["t"])
    write_row(dict(date=now_et().strftime("%Y-%m-%d"), version=tr["ver"], ticker=tr["sym"], side="CALL" if tr["side"] == 1 else "PUT",
                   contract=tr["contract"], sold=f"{qty} of {tr['qty0']}", reason=reason, entry_time=t0.strftime("%H:%M"),
                   exit_time=now_et().strftime("%H:%M"), minutes=round((now_et() - t0).total_seconds() / 60, 1),
                   entry_fill=tr["fill"], exit_fill=px, pnl_usd=round(pnl, 2), pnl_pct=round(pct, 1),
                   best_pct=round(tr["best"], 1), worst_pct=round(tr["worst"], 1), clean=tr["clean"], adx=tr["adx"],
                   spot_entry=round(tr["spot"], 2), spot_exit=round(spot, 2) if spot else ""))
    log(f"{tr['sym']} [{tr['ver']}] SELL {qty} {tr['contract']} @ {px:.2f} | {reason} | ${pnl:+.2f} ({pct:+.0f}%)")
    tr["qty"] -= qty
    return True


def fast_checks(tc, oc, trades):
    """Every few seconds: each version's stop, TP1 and TP2."""
    q = mids(oc, {t["contract"] for t in trades.values()})
    changed = False
    for key, tr in list(trades.items()):
        m = q.get(tr["contract"])
        if not m:
            continue
        v = VERSIONS[tr["ver"]]
        pct = (m / tr["fill"] - 1) * 100
        tr["best"], tr["worst"] = max(tr["best"], pct), min(tr["worst"], pct)
        if pct <= -v["sl"]:
            changed |= sell(tc, tr, tr["qty"], f"STOP -{v['sl']}%")
        elif v["tp2"] and pct >= v["tp2"]:
            changed |= sell(tc, tr, tr["qty"], f"TP2 +{v['tp2']}%")
        elif not tr["tp1"] and pct >= v["tp1"] and tr["qty"] > v["tp1_qty"]:
            if sell(tc, tr, v["tp1_qty"], f"TP1 +{v['tp1']}%"):
                tr["tp1"] = True
                changed = True
        if tr["qty"] <= 0:
            del trades[key]
    return changed


def recover_check(tc, trades):
    try:
        held = {p.symbol: abs(int(float(p.qty))) for p in tc.get_all_positions()}
    except Exception as e:
        log(f"positions check failed: {e}")
        return trades
    for key, tr in list(trades.items()):
        if held.get(tr["contract"], 0) <= 0:
            log(f"{key}: saved trade {tr['contract']} is no longer held - forgetting it")
            del trades[key]
        else:
            log(f"{key}: taking over open trade {tr['contract']} x{tr['qty']} (fill {tr['fill']:.2f})")
    return trades


# ===== Check mode =====
def check(tc, dc, oc):
    log("CHECK MODE - no trades")
    a = tc.get_account()
    log(f"account {a.status} | cash ${a.cash} | buying power ${a.buying_power} | "
        f"options level {getattr(a, 'options_trading_level', '?')}")
    data = get_5m(dc)
    today = now_et().date()
    for sym in SYMBOLS:
        d = data.get(sym)
        if d is None or len(d) < N + 20:
            log(f"{sym}: not enough 5m candles ({0 if d is None else len(d)})")
            continue
        st, why, info = scan(d)
        sig = {1: "LONG", -1: "SHORT", 0: "-"}[int(st[-1])]
        entries = int(((st != 0) & (np.r_[0, st[:-1]] == 0)).sum())
        log(f"{sym:5s} Clean {info['clean']:4.0f} | ADX {info['adx']:4.0f} | RVol {info['rv']:4.1f} | now {sig:5s} | "
            f"signals in the last {len(d) // 78} days: {entries}")
    d = data.get("SPY")
    if d is not None and len(d):
        spot = float(d["close"].iloc[-1])
        for side in (1, -1):
            try:
                c = pick_otm(tc, "SPY", side, spot, today, 2)
                if c:
                    log(f"SPY {spot:.2f}: 2nd OTM {'call' if side == 1 else 'put'} {c.symbol} | "
                        f"mid {mids(oc, [c.symbol]).get(c.symbol, 0):.2f}")
            except Exception as e:
                log(f"SPY option lookup failed: {e}")
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
    exit_dt = min(now_et().replace(hour=EXIT_AT // 100, minute=EXIT_AT % 100, second=0, microsecond=0),
                  close_dt - timedelta(minutes=15))
    log(f"Clean Scan bot | {len(SYMBOLS)} tickers on {TF}m | versions: "
        + " / ".join(f"{k}: {v['qty']}x OTM{v['otm']} stop -{v['sl']}% TP1 +{v['tp1']}%"
                     + (f" TP2 +{v['tp2']}%" if v["tp2"] else " runner") for k, v in VERSIONS.items())
        + f" | scan exits on | all out by {exit_dt:%H:%M}")

    trades = recover_check(tc, load_state(today))
    save_state(trades, today)
    last_bar = None
    while True:
        now = now_et()
        if time.time() - t_start > RUN_MINUTES * 60:
            log("Run time limit - the next scheduled run takes over (open trades are saved).")
            break
        if now >= exit_dt:
            for key, tr in list(trades.items()):
                if sell(tc, tr, tr["qty"], WHY[5]):
                    del trades[key]
            save_state(trades, today)
            log("3:45 - all out, done for today.")
            break
        if hhmm(now) < 930:
            if hhmm(now) < 820:
                log("Too early, exiting.")
                break
            time.sleep(20)
            continue

        # wait for the next 5-minute candle close (+5 s), checking % rules every few seconds
        nxt = now.replace(second=0, microsecond=0) + timedelta(minutes=TF - now.minute % TF, seconds=5)
        while True:
            rem = (nxt - now_et()).total_seconds()
            if rem <= 0:
                break
            if trades and fast_checks(tc, oc, trades):
                save_state(trades, today)
            time.sleep(min(rem, CHECK_SECS) if trades else rem)

        try:
            data = get_5m(dc)
        except Exception as e:
            log(f"bars failed: {e}")
            continue
        spy = data.get("SPY")
        bar = spy.index[-1] if spy is not None and len(spy) else None
        if bar is None or bar == last_bar:
            continue
        first = last_bar is None
        last_bar = bar
        changed = False
        for sym in SYMBOLS:
            d = data.get(sym)
            if d is None or len(d) < N + 20 or d.index[-1] != bar:
                continue
            try:
                st, why, info = scan(d)
            except Exception as e:
                log(f"{sym}: scan failed: {e}")
                continue
            now_s, prev_s = int(st[-1]), int(st[-2])
            mine = {k: t for k, t in trades.items() if t["sym"] == sym}
            for key, tr in mine.items():
                if now_s != tr["side"]:
                    reason = WHY.get(int(why[-1]), "criteria lost")
                    if sell(tc, tr, tr["qty"], f"SCAN EXIT: {reason}", info["close"]):
                        del trades[key]
                        changed = True
            if (not mine and now_s != 0 and prev_s == 0 and not first
                    and (DIRECTION == 0 or now_s == DIRECTION)):
                log(f"{sym}: CLEAN SCAN {'LONG' if now_s == 1 else 'SHORT'} at {bar + pd.Timedelta(minutes=TF):%H:%M}")
                for ver in VERSIONS:
                    if len(trades) >= MAX_OPEN:
                        break
                    new = enter(tc, sym, now_s, info, today, ver)
                    if new:
                        trades[f"{sym}|{ver}"] = new
                        changed = True
        if first:
            log(f"watching {len(SYMBOLS)} tickers")
        if changed:
            save_state(trades, today)

    save_state(trades, today)
    summary(today)


def summary(today):
    if not os.path.exists(LOG):
        log("No trades logged yet.")
        return
    rows = list(csv.DictReader(open(LOG)))
    td = [r for r in rows if r["date"] == today.isoformat()]
    tot = sum(float(r["pnl_usd"]) for r in td)
    alltot = sum(float(r["pnl_usd"]) for r in rows)
    lines = [f"## Clean Scan bot - {today}", f"Today: {len(td)} sales, **${tot:+,.2f}** | all time: ${alltot:+,.2f}"]
    for ver in VERSIONS:
        t_ = sum(float(r["pnl_usd"]) for r in td if r.get("version") == ver)
        a_ = sum(float(r["pnl_usd"]) for r in rows if r.get("version") == ver)
        lines.append(f"Version {ver}: today **${t_:+,.2f}** | all time ${a_:+,.2f}")
    lines += ["",
             "| Ver | Ticker | Side | Contract | Sold | Reason | In | Out | Entry | Exit | $ | % |",
             "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in td:
        lines.append(f"| {r.get('version', '')} | {r['ticker']} | {r['side']} | {r['contract']} | {r['sold']} | {r['reason']} | {r['entry_time']} | "
                     f"{r['exit_time']} | {r['entry_fill']} | {r['exit_fill']} | {float(r['pnl_usd']):+.2f} | {r['pnl_pct']}% |")
    text = "\n".join(lines)
    log("\n" + text)
    s = os.getenv("GITHUB_STEP_SUMMARY")
    if s:
        with open(s, "a") as f:
            f.write(text + "\n")


if __name__ == "__main__":
    main()
