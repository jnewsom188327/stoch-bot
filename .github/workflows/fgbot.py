"""
FG FLOW BOT - paper trades the Fear Greed Flow indicator on SPY and QQQ (5-minute chart) through Alpaca PAPER.
PAPER ONLY - the paper=True switch in main() is hard-coded. Keys come from GitHub Secrets ALPACA_KEY / ALPACA_SECRET.

SIGNAL (same math as the TradingView "FG Flow" indicator, setting A = no fixed targets):
  LONG  : fear flushed to 85+ in the last 12 bars, fear line crosses back under its signal line (release),
          fear falling AND greed rising together (flow), green candle, greed NOT yet above its signal line (early).
  SHORT : mirror image (greed flush + release, bear flow, red candle, fear not yet above its signal line).
  Entries 9:35 - 15:00 ET on a closed 5m candle. One trade per ticker. One trade per flush.
EXITS (decided on the stock price, like the indicator):
  STOP  : just past the flush low/high (0.2 ATR), capped at 2.5 ATR. Checked live every 5 seconds.
  RELEASE : the other side flushed and released (e.g. greed pinned, then crosses under its line).
  FLOW FLIPPED : both lines moved against the trade for 2 candles.
  TIME  : 30 candles. CLOSE: everything out by 15:55.
ORDERS: 2 contracts, 1st strike OUT of the money, nearest expiration (0DTE on SPY/QQQ). Market orders (paper).
Logs: fg_trades.csv (one row per trade, stock points AND option $) and fg_state.json (open trades).
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
SYMBOLS = ["SPY", "QQQ"]
QTY = 2                      # contracts per trade
OTM_STEPS = 1                # 1 = first strike out of the money
MAX_DTE = 7
CHECK_SECS = 5

# FG Flow settings (match the TradingView indicator)
TF = 5
PD, NLEN, SLEN, FLEN = 22, 50, 9, 3
HOT, LOOK, RELWIN = 85.0, 12, 3
STOP_BUF, MAX_RISK, HOLD_MAX = 0.2, 2.5, 30
EARLY_ONLY = True
ENTRY_FROM, ENTRY_TO, END_AT = 935, 1500, 1555

RUN_MINUTES = 340
LOG = "fg_trades.csv"
STATE = "fg_state.json"

ET = ZoneInfo("America/New_York")
KEY = os.getenv("ALPACA_KEY", "").strip()
SECRET = os.getenv("ALPACA_SECRET", "").strip()
WHY = {1: "stop", 2: "release", 3: "flow flipped", 4: "time", 5: "close"}


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


# ===== FG Flow math (same as TradingView) =====
def rma(x, n):
    return x.ewm(alpha=1 / n, adjust=False).mean()


def ema(x, n):
    return x.ewm(span=n, adjust=False).mean()


def sim(df):
    """Runs the FG Flow indicator bar by bar (exactly like the chart).
    Returns (events on the LAST bar, every event as (bar index, event))."""
    c, h, l, o = df["close"], df["high"], df["low"], df["open"]
    hc, lc = c.rolling(PD).max(), c.rolling(PD).min()
    fRaw = (hc - l) / hc * 100
    gRaw = (h - lc) / lc * 100
    fMax, gMax = fRaw.rolling(NLEN).max(), gRaw.rolling(NLEN).max()
    F = (fRaw / fMax * 100).where(fMax > 0, 0.0)
    G = (gRaw / gMax * 100).where(gMax > 0, 0.0)
    sigF, sigG = ema(F, SLEN), ema(G, SLEN)
    fS, gS = ema(F, FLEN), ema(G, FLEN)
    tr = pd.concat([h - l, (h - c.shift(1)).abs(), (l - c.shift(1)).abs()], axis=1).max(axis=1)
    atr = rma(tr, 14)
    bull = (gS > gS.shift(1)) & (fS < fS.shift(1))
    bear = (gS < gS.shift(1)) & (fS > fS.shift(1))
    gX = (G < sigG) & (G.shift(1) >= sigG.shift(1))
    fX = (F < sigF) & (F.shift(1) >= sigF.shift(1))

    def bars_since(x):
        idx = pd.Series(np.where(x.to_numpy(), np.arange(len(x)), np.nan), index=x.index).ffill()
        return pd.Series(np.arange(len(x)), index=x.index) - idx

    fFlush = F.rolling(LOOK).max() >= HOT
    gFlush = G.rolling(LOOK).max() >= HOT
    fRel = (bars_since(fX) <= RELWIN) & (F < sigF)
    gRel = (bars_since(gX) <= RELWIN) & (G < sigG)
    fUp = (F > HOT) & (F.shift(1) <= HOT)
    gUp = (G > HOT) & (G.shift(1) <= HOT)
    rawL = fFlush & fRel & bull & (c > o)
    rawS = gFlush & gRel & bear & (c < o)
    lowF, highF = l.rolling(LOOK).min(), h.rolling(LOOK).max()
    bear2, bull2 = bear & bear.shift(1, fill_value=False), bull & bull.shift(1, fill_value=False)
    hm = df.index.hour * 100 + df.index.minute
    inE = (hm >= ENTRY_FROM) & (hm < ENTRY_TO)
    inEnd = (hm >= 930) & (hm < END_AT)

    A = {k: v.to_numpy() for k, v in dict(c=c, h=h, l=l, G=G, F=F, sigG=sigG, sigF=sigF, atr=atr,
                                         gX=gX, fX=fX, gFlush=gFlush, fFlush=fFlush, rawL=rawL, rawS=rawS,
                                         fUp=fUp, gUp=gUp, lowF=lowF, highF=highF, bear2=bear2, bull2=bull2).items()}
    pos, ePx, sPx, eBar, usedL, usedS = 0, np.nan, np.nan, 0, False, False
    allev = []
    n = len(df)
    for i in range(NLEN + PD, n):
        ev = []
        if A["fUp"][i]:
            usedL = False
        if A["gUp"][i]:
            usedS = False
        if pos != 0:
            hit = A["l"][i] <= sPx if pos == 1 else A["h"][i] >= sPx
            held = i - eBar
            if pos == 1:
                ex = 1 if hit else 2 if (A["gFlush"][i] and A["gX"][i]) else 3 if (A["bear2"][i] and A["G"][i] < A["sigG"][i]) else 0
            else:
                ex = 1 if hit else 2 if (A["fFlush"][i] and A["fX"][i]) else 3 if (A["bull2"][i] and A["F"][i] < A["sigF"][i]) else 0
            if ex == 0:
                ex = 4 if held >= HOLD_MAX else 5 if not inEnd[i] else 0
            if ex:
                xPx = sPx if ex == 1 else A["c"][i]
                ev.append(("exit", pos, ex, xPx, (xPx - ePx) * pos))
                pos = 0
        if pos == 0 and inE[i]:
            earlyL = A["G"][i] <= A["sigG"][i]
            earlyS = A["F"][i] <= A["sigF"][i]
            goL = A["rawL"][i] and not usedL and (not EARLY_ONLY or earlyL)
            goS = A["rawS"][i] and not usedS and (not EARLY_ONLY or earlyS)
            if goL or goS:
                pos = 1 if goL else -1
                ePx, eBar, a = A["c"][i], i, A["atr"][i]
                raw = A["lowF"][i] - STOP_BUF * a if goL else A["highF"][i] + STOP_BUF * a
                cap = ePx - MAX_RISK * a if goL else ePx + MAX_RISK * a
                sPx = max(raw, cap) if goL else min(raw, cap)
                usedL = usedL or goL
                usedS = usedS or goS
                ev.append(("entry", pos, 0, ePx, sPx))
        allev += [(i, e) for e in ev]
    last = [e for i, e in allev if i == n - 1]
    return last, allev


# ===== Data =====
def get_5m(dc):
    from alpaca.data.enums import DataFeed
    from alpaca.data.requests import StockBarsRequest
    from alpaca.data.timeframe import TimeFrame, TimeFrameUnit
    now = datetime.now(timezone.utc)
    req = StockBarsRequest(symbol_or_symbols=SYMBOLS, timeframe=TimeFrame(TF, TimeFrameUnit.Minute),
                           start=now - timedelta(days=6), end=now, feed=DataFeed.IEX)
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
        d = d[d.index + pd.Timedelta(minutes=TF) <= cut]
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
def pick_otm(tc, sym, side, spot, today):
    from alpaca.trading.enums import ContractType
    from alpaca.trading.requests import GetOptionContractsRequest
    req = GetOptionContractsRequest(
        underlying_symbols=[sym], expiration_date_gte=today, expiration_date_lte=today + timedelta(days=MAX_DTE),
        type=ContractType.CALL if side == 1 else ContractType.PUT,
        strike_price_gte=str(round(spot - 15, 2)), strike_price_lte=str(round(spot + 15, 2)), limit=1000)
    cs = tc.get_option_contracts(req).option_contracts or []
    if not cs:
        return None
    exp = min(pd.Timestamp(x.expiration_date).date() for x in cs)
    cs = [x for x in cs if pd.Timestamp(x.expiration_date).date() == exp]
    if side == 1:
        c = sorted([x for x in cs if float(x.strike_price) > spot], key=lambda x: float(x.strike_price))
    else:
        c = sorted([x for x in cs if float(x.strike_price) < spot], key=lambda x: -float(x.strike_price))
    return c[OTM_STEPS - 1] if len(c) >= OTM_STEPS else None


def status_of(o):
    return str(getattr(o.status, "value", o.status)).lower()


def market(tc, contract, qty, buy):
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
def enter(tc, sym, side, spot, stop, today):
    try:
        c = pick_otm(tc, sym, side, spot, today)
    except Exception as e:
        log(f"{sym}: option lookup failed: {e}")
        return None
    if not c:
        log(f"{sym}: no {'call' if side == 1 else 'put'} found")
        return None
    fill = market(tc, c.symbol, QTY, True)
    if fill is None:
        return None
    log(f"{sym} FG {'LONG - CALLS' if side == 1 else 'SHORT - PUTS'}: BUY {QTY} {c.symbol} @ {fill:.2f} | "
        f"{sym} {spot:.2f}, stop {stop:.2f}")
    return dict(sym=sym, side=side, contract=c.symbol, qty=QTY, fill=fill, spot=spot, stop=stop,
                t=now_et().isoformat())


def close_trade(tc, tr, reason, spot):
    px = market(tc, tr["contract"], tr["qty"], False)
    if px is None:
        return False
    pnl = (px - tr["fill"]) * 100 * tr["qty"]
    pts = (spot - tr["spot"]) * tr["side"] if spot else ""
    t0 = datetime.fromisoformat(tr["t"])
    write_row(dict(date=now_et().strftime("%Y-%m-%d"), ticker=tr["sym"], side="LONG" if tr["side"] == 1 else "SHORT",
                   contract=tr["contract"], reason=reason, entry_time=t0.strftime("%H:%M"),
                   exit_time=now_et().strftime("%H:%M"), minutes=round((now_et() - t0).total_seconds() / 60, 1),
                   stock_entry=round(tr["spot"], 2), stock_exit=round(spot, 2) if spot else "",
                   stock_pts=round(pts, 2) if pts != "" else "", stop=round(tr["stop"], 2),
                   opt_entry=tr["fill"], opt_exit=px, contracts=tr["qty"], pnl_usd=round(pnl, 2),
                   pnl_pct=round((px / tr["fill"] - 1) * 100, 1)))
    log(f"{tr['sym']} EXIT {'LONG' if tr['side'] == 1 else 'SHORT'} ({reason}): SELL {tr['qty']} {tr['contract']} "
        f"@ {px:.2f} | ${pnl:+.2f} | stock {pts if pts == '' else round(pts, 2)} pts")
    return True


def stop_checks(tc, dc, trades):
    """Every few seconds: sell if the stock trades through the stop."""
    spots = stock_prices(dc, set(trades))
    changed = False
    for sym, tr in list(trades.items()):
        s = spots.get(sym)
        if s is None:
            continue
        if (tr["side"] == 1 and s <= tr["stop"]) or (tr["side"] == -1 and s >= tr["stop"]):
            if close_trade(tc, tr, "stop", s):
                del trades[sym]
                changed = True
    return changed


def recover_check(tc, trades):
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
            log(f"{sym}: taking over open trade {tr['contract']} x{tr['qty']} (stop {tr['stop']:.2f})")
    return trades


# ===== Check mode =====
def check(tc, dc):
    log("CHECK MODE - no trades")
    a = tc.get_account()
    log(f"account {a.status} | buying power ${a.buying_power} | options level {getattr(a, 'options_trading_level', '?')}")
    data = get_5m(dc)
    for sym in SYMBOLS:
        d = data.get(sym)
        if d is None or len(d) < 200:
            log(f"{sym}: not enough 5m candles ({0 if d is None else len(d)})")
            continue
        _, allev = sim(d)
        lines, pts = [], []
        for i, e in allev:
            if e[0] == "entry":
                lines.append(f"{d.index[i]:%m-%d %H:%M} {'LONG' if e[1] == 1 else 'SHORT'} @ {e[3]:.2f} stop {e[4]:.2f}")
            else:
                pts.append(e[4])
                lines.append(f"{d.index[i]:%m-%d %H:%M}    exit {WHY[e[2]]} {e[4]:+.2f} pts")
        n_ent = sum(1 for _, e in allev if e[0] == "entry")
        avg = f"{np.mean(pts):+.2f}" if pts else "-"
        log(f"{sym}: {len(d)} candles | FG trades in the data: {n_ent} | avg {avg} stock pts per trade")
        for ln in lines[-8:]:
            log(f"   {ln}")
    log("CHECK OK - keys work")


# ===== Main loop =====
def main():
    from alpaca.data.historical import StockHistoricalDataClient
    from alpaca.trading.client import TradingClient
    if not KEY or not SECRET:
        log("Missing ALPACA_KEY / ALPACA_SECRET secrets in the repo settings.")
        sys.exit(1)
    tc = TradingClient(KEY, SECRET, paper=True)   # PAPER ONLY - never change this
    dc = StockHistoricalDataClient(KEY, SECRET)
    if os.getenv("MODE", "run") == "check":
        return check(tc, dc)
    run_loop(tc, dc)


def run_loop(tc, dc):
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
    end_dt = min(now_et().replace(hour=END_AT // 100, minute=END_AT % 100, second=0, microsecond=0),
                 close_dt - timedelta(minutes=5))
    log(f"FG Flow bot | {', '.join(SYMBOLS)} on {TF}m | {QTY}x 1st OTM | exits: stop / release / flow flip / "
        f"{HOLD_MAX} bars / {end_dt:%H:%M}")
    trades = recover_check(tc, load_state(today))
    save_state(trades, today)
    last_bar = None
    while True:
        now = now_et()
        if time.time() - t_start > RUN_MINUTES * 60:
            log("Run time limit - the next scheduled run takes over (open trades are saved).")
            break
        if now >= end_dt:
            spots = stock_prices(dc, set(trades)) if trades else {}
            for sym, tr in list(trades.items()):
                if close_trade(tc, tr, "close", spots.get(sym)):
                    del trades[sym]
            save_state(trades, today)
            log("Done for today.")
            break
        if hhmm(now) < 930:
            if hhmm(now) < 820:
                log("Too early, exiting.")
                break
            time.sleep(20)
            continue
        nxt = now.replace(second=0, microsecond=0) + timedelta(minutes=TF - now.minute % TF, seconds=5)
        while True:
            rem = (nxt - now_et()).total_seconds()
            if rem <= 0:
                break
            if trades and stop_checks(tc, dc, trades):
                save_state(trades, today)
            time.sleep(min(rem, CHECK_SECS) if trades else rem)
        try:
            data = get_5m(dc)
        except Exception as e:
            log(f"bars failed: {e}")
            continue
        spy = data.get(SYMBOLS[0])
        bar = spy.index[-1] if spy is not None and len(spy) else None
        if bar is None or bar == last_bar:
            continue
        first = last_bar is None
        last_bar = bar
        changed = False
        for sym in SYMBOLS:
            d = data.get(sym)
            if d is None or len(d) < 200 or d.index[-1] != bar:
                continue
            try:
                events, _ = sim(d)
            except Exception as e:
                log(f"{sym}: signal failed: {e}")
                continue
            spot = float(d["close"].iloc[-1])
            for kind, side, why, px, extra in events:
                tr = trades.get(sym)
                if kind == "exit" and tr:
                    if close_trade(tc, tr, WHY[why], spot):
                        del trades[sym]
                        changed = True
                elif kind == "entry" and not tr and not first:
                    log(f"{sym}: FG FLOW {'LONG' if side == 1 else 'SHORT'} at {bar + pd.Timedelta(minutes=TF):%H:%M} "
                        f"close {px:.2f}, stop {extra:.2f}")
                    new = enter(tc, sym, side, px, extra, today)
                    if new:
                        trades[sym] = new
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
    lines = [f"## FG Flow bot - {today}", f"Today: {len(td)} trades, **${tot:+,.2f}** | all time: ${alltot:+,.2f}", "",
             "| Ticker | Side | In | Out | Reason | Stock pts | Option in | Option out | $ |",
             "|---|---|---|---|---|---|---|---|---|"]
    for r in td:
        lines.append(f"| {r['ticker']} | {r['side']} | {r['entry_time']} | {r['exit_time']} | {r['reason']} | "
                     f"{r['stock_pts']} | {r['opt_entry']} | {r['opt_exit']} | {float(r['pnl_usd']):+.2f} |")
    text = "\n".join(lines)
    log("\n" + text)
    s = os.getenv("GITHUB_STEP_SUMMARY")
    if s:
        with open(s, "a") as f:
            f.write(text + "\n")


if __name__ == "__main__":
    main()
