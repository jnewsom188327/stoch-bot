"""
TREND FLIP BOT - paper trades Trend Flip v3.0 on SPY and QQQ, 2-minute AND 3-minute charts, through Alpaca PAPER.
PAPER ONLY - the paper=True switch in main() is hard-coded. Keys come from GitHub Secrets ALPACA_KEY / ALPACA_SECRET.

SIGNAL (same math as the TradingView indicator Trend Flip v3.0, and the 6-year backtest):
  LINE  : EMA 13 > EMA 34 and close > VWAP = GREEN | the opposite = RED | anything else = GRAY
  FIRES : the line turns GREEN (calls) / RED (puts) on a candle close, 9:35 - 15:30 ET, with a Vix Fix
          FEAR spike (calls) / GREED spike (puts) in the last 10 candles (or one arrives within 5 candles
          while the line keeps its color). Each chart (SPY 2m, SPY 3m, QQQ 2m, QQQ 3m) trades on its own.
YOUR PLAN (settings below):
  BUY   : 5 contracts, first strike OUT of the money (call above price on green, put below price on red), 0DTE.
  +30%  : sell 4, keep 1 as the runner.
  RUNNER: sells at the close of candle 15, or when it falls 20% from its best price after the partial.
  STOP  : option down 30% from the fill -> sell everything still open (checked every 5 seconds).
  BREAKEVEN: once the option has traded +10% over the fill, the stop moves up to the fill price (sell everything
          still open if it falls back to it). Replay of the first 6 days: Trend Flip +$126 -> +$530.
  ALSO  : opposite color flip on that chart -> sell everything (v3.0 rule) | flat 5 min before the close.
  No new trades after 15:30. Max 4 trades open (one per chart).
Option prices for the % rules = middle of bid/ask. Orders are market orders (paper fills).
Data = Alpaca's free IEX feed, so a signal can very occasionally differ from TradingView's chart.
Logs: flip_trades.csv (one row per sale) and flip_state.json (open trades, so the next run can take over).
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

# ===== SETTINGS (edit here) =====
SYMBOLS = ["SPY", "QQQ"]
TFS = [2, 3]                 # chart minutes
QTY = 5                      # contracts per trade
PARTIAL_QTY = 4              # sold at the first target
TP_PCT = 30                  # first target: option up this % -> sell PARTIAL_QTY
SL_PCT = 30                  # stop: option down this % -> sell everything still open
BE_ARM_PCT = 10              # breakeven: once the option has been this % over the fill, the stop moves to the fill (0 = off)
TRAIL_PCT = 20               # runner: sell if it falls this % from its best price (0 = off)
HOLD = 15                    # time exit: close of candle N (entry candle = 1)
FLIP_EXIT = True             # sell everything on the opposite color flip (v3.0 rule)
OTM_STEPS = 1                # 1 = first strike out of the money
DTE = 0                      # 0 = expires today, 1 = next trading day
FIRST_FIRE = 935             # HHMM ET
LAST_FIRE = 1530             # HHMM ET - no new trades after this (earlier on half days)
FLAT_MIN = 5                 # sell everything this many minutes before the close
CHECK_SECS = 5               # how often the % rules are checked
MAX_OPEN = 4                 # max trades open at once
DIRECTION = 0                # 0 = calls + puts, 1 = calls only, -1 = puts only

# Trend Flip v3.0 settings (match the TradingView indicator)
FAST, SLOW, USE_VWAP = 13, 34, True
VF_ON, VF_LOOK, WAIT = True, 10, 5

RUN_MINUTES = 340            # GitHub allows 6 h per run; the next scheduled run takes over from flip_state.json
LOG = "flip_trades.csv"
STATE = "flip_state.json"

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


def to_tf(d1, mins, now):
    g = d1.groupby(d1.index.floor(f"{mins}min"))
    out = pd.DataFrame({"open": g["open"].first(), "high": g["high"].max(), "low": g["low"].min(),
                        "close": g["close"].last(), "volume": g["volume"].sum()}).dropna()
    return out[out.index + pd.Timedelta(minutes=mins) <= now]       # closed candles only


# ===== Trend Flip v3.0 (same math as backtest.py / TradingView) =====
def bars_since(flag):
    out = np.full(len(flag), 999, dtype=np.int64)
    last = None
    for i, f in enumerate(flag):
        if f:
            last = i
        if last is not None:
            out[i] = i - last
    return out


def trend_flip(df):
    """Returns (line color now, raw flip on the last candle, fire on the last candle)."""
    h, l, c, v = df["high"], df["low"], df["close"], df["volume"]
    ef = c.ewm(span=FAST, adjust=False).mean()
    es = c.ewm(span=SLOW, adjust=False).mean()
    day = df.index.date
    hlc3 = (h + l + c) / 3
    vwap = ((hlc3 * v).groupby(day).cumsum() / v.groupby(day).cumsum().replace(0, np.nan)).ffill()
    up = (ef > es) & (c > vwap) if USE_VWAP else (ef > es)
    dn = (ef < es) & (c < vwap) if USE_VWAP else (ef < es)
    st = np.where(up, 1, np.where(dn, -1, 0))
    hc22, lc22 = c.rolling(22).max(), c.rolling(22).min()
    wvf = (hc22 - l) / hc22 * 100
    wvi = (h - lc22) / lc22 * 100

    def spike(w):
        mid, sd = w.rolling(20).mean(), w.rolling(20).std(ddof=0)
        return ((w >= mid + 2 * sd) | (w >= w.rolling(50).max() * 0.85)).fillna(False).to_numpy()

    hm = df.index.hour * 100 + df.index.minute
    inT = (hm >= FIRST_FIRE) & (hm < LAST_FIRE)
    prev = np.r_[0, st[:-1]]
    sig = np.where(inT & (st != 0) & (st != prev), st, 0)
    if VF_ON:
        okL = bars_since(spike(wvf)) <= VF_LOOK
        okS = bars_since(spike(wvi)) <= VF_LOOK
    else:
        okL = okS = np.ones(len(st), dtype=bool)
    ent = np.zeros(len(st), dtype=np.int64)
    arm = armB = 0
    for i in range(len(st)):
        if sig[i] != 0:
            arm, armB = sig[i], 0
        elif arm != 0:
            armB += 1
        if arm != 0 and (st[i] != arm or armB > WAIT or not inT[i]):
            arm = 0
        if arm != 0 and (okL[i] if arm == 1 else okS[i]):
            ent[i] = arm
            arm = 0
    return int(st[-1]), int(sig[-1]), int(ent[-1])


# ===== Options + orders =====
def expiry(tc, today):
    if DTE <= 0:
        return today
    from alpaca.trading.requests import GetCalendarRequest
    cal = tc.get_calendar(GetCalendarRequest(start=today + timedelta(days=1), end=today + timedelta(days=10)))
    d = cal[DTE - 1].date if len(cal) >= DTE else today
    return d if isinstance(d, date) else pd.Timestamp(d).date()


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
        sleep(0.5)
    log(f"order not filled after 30 s: {contract}")
    return None


# ===== Trade management =====
def enter(tc, oc, chart, sym, side, spot, bar_start, exp):
    try:
        c = pick_otm(tc, sym, side, spot, exp)
    except Exception as e:
        log(f"{chart}: option lookup failed: {e}")
        return None
    if not c:
        log(f"{chart}: no {'call' if side == 1 else 'put'} found for {exp}")
        return None
    fill = market(tc, c.symbol, QTY, True)
    if fill is None:
        return None
    log(f"{chart} BUY {QTY} {c.symbol} ({'CALL' if side == 1 else 'PUT'}, strike {c.strike_price}) @ {fill:.2f} | "
        f"{sym} {spot:.2f} | target +{TP_PCT}% = {fill * (1 + TP_PCT / 100):.2f}, stop -{SL_PCT}% = {fill * (1 - SL_PCT / 100):.2f}")
    return dict(chart=chart, sym=sym, side=side, contract=c.symbol, strike=float(c.strike_price), qty=QTY,
                fill=fill, spot=spot, entry_start=bar_start.isoformat(), t=now_et().isoformat(),
                partial=False, peak=fill, best=0.0, worst=0.0)


def sell(tc, tr, qty, reason, spot=None):
    px = market(tc, tr["contract"], qty, False)
    if px is None:
        return False
    pnl = (px - tr["fill"]) * 100 * qty
    pct = (px / tr["fill"] - 1) * 100 if tr["fill"] else 0.0
    leg = f"{qty} of {QTY}" + (" (runner)" if tr["partial"] and qty == tr["qty"] else "")
    t0 = datetime.fromisoformat(tr["t"])
    write_row(dict(date=now_et().strftime("%Y-%m-%d"), chart=tr["chart"], side="CALL" if tr["side"] == 1 else "PUT",
                   contract=tr["contract"], leg=leg, reason=reason, entry_time=t0.strftime("%H:%M"),
                   exit_time=now_et().strftime("%H:%M"), minutes=round((now_et() - t0).total_seconds() / 60, 1),
                   entry_fill=tr["fill"], exit_fill=px, pnl_usd=round(pnl, 2), pnl_pct=round(pct, 1),
                   best_pct=round(tr["best"], 1), worst_pct=round(tr["worst"], 1),
                   spot_entry=round(tr["spot"], 2), spot_exit=round(spot, 2) if spot else ""))
    log(f"{tr['chart']} SELL {qty} {tr['contract']} @ {px:.2f} | {reason} | ${pnl:+.2f} ({pct:+.0f}%)")
    tr["qty"] -= qty
    return True


def fast_checks(tc, oc, trades):
    """Every few seconds: +30% partial, -30% stop, runner trailing stop."""
    q = mids(oc, {t["contract"] for t in trades.values()})
    changed = False
    for chart, tr in list(trades.items()):
        m = q.get(tr["contract"])
        if not m:
            continue
        pct = (m / tr["fill"] - 1) * 100
        armed = BE_ARM_PCT > 0 and tr["best"] >= BE_ARM_PCT          # armed on an EARLIER check, like the replay
        tr["best"], tr["worst"] = max(tr["best"], pct), min(tr["worst"], pct)
        if armed and pct <= 0:
            if sell(tc, tr, tr["qty"], f"BREAKEVEN (was +{BE_ARM_PCT}%)"):
                changed = True
        elif pct <= -SL_PCT:
            if sell(tc, tr, tr["qty"], f"STOP -{SL_PCT}%"):
                changed = True
        elif not tr["partial"] and pct >= TP_PCT and tr["qty"] > PARTIAL_QTY:
            if sell(tc, tr, PARTIAL_QTY, f"TARGET +{TP_PCT}%"):
                tr["partial"], tr["peak"] = True, m
                changed = True
        elif tr["partial"] and TRAIL_PCT > 0:
            tr["peak"] = max(tr["peak"], m)
            if m <= tr["peak"] * (1 - TRAIL_PCT / 100):
                if sell(tc, tr, tr["qty"], f"RUNNER gave back {TRAIL_PCT}% from best"):
                    changed = True
        if tr["qty"] <= 0:
            del trades[chart]
    return changed


def recover_check(tc, trades):
    """Drop saved trades whose contracts are no longer held (sold by hand, expired...)."""
    try:
        held = {p.symbol: abs(int(float(p.qty))) for p in tc.get_all_positions()}
    except Exception as e:
        log(f"positions check failed: {e}")
        return trades
    for chart, tr in list(trades.items()):
        if held.get(tr["contract"], 0) <= 0:
            log(f"{chart}: saved trade {tr['contract']} is no longer held - forgetting it")
            del trades[chart]
        else:
            log(f"{chart}: taking over open trade {tr['contract']} x{tr['qty']} (fill {tr['fill']:.2f})")
    return trades


# ===== Check mode =====
def check(tc, dc, oc):
    log("CHECK MODE - no trades")
    a = tc.get_account()
    log(f"account {a.status} | cash ${a.cash} | buying power ${a.buying_power} | "
        f"options level {getattr(a, 'options_trading_level', '?')}")
    now = now_et()
    data = get_1m(dc)
    for sym in SYMBOLS:
        d1 = data.get(sym)
        if d1 is None or d1.empty:
            log(f"{sym}: no bars")
            continue
        for tf in TFS:
            df = to_tf(d1, tf, now)
            st, sg, en = trend_flip(df)
            log(f"{sym} {tf}m: {len(df)} candles, last {df.index[-1]:%m-%d %H:%M} | line "
                f"{'GREEN' if st == 1 else 'RED' if st == -1 else 'GRAY'} | fire on last candle: {en}")
        spot = float(d1["close"].iloc[-1])
        try:
            exp = expiry(tc, now.date())
            for side in (1, -1):
                c = pick_otm(tc, sym, side, spot, exp)
                if c:
                    log(f"{sym} {spot:.2f}: 1st OTM {'call' if side == 1 else 'put'} {c.symbol} | mid {mids(oc, [c.symbol]).get(c.symbol, 0):.2f}")
                else:
                    log(f"{sym}: no {'call' if side == 1 else 'put'} for {exp} (market closed / no expiry today)")
        except Exception as e:
            log(f"{sym}: option lookup failed: {e}")
    log("CHECK OK - keys work")


# ===== Main loop =====
def main():
    from alpaca.data.historical import OptionHistoricalDataClient, StockHistoricalDataClient
    from alpaca.trading.client import TradingClient
    from alpaca.trading.requests import GetCalendarRequest
    if not KEY or not SECRET:
        log("Missing ALPACA_KEY / ALPACA_SECRET secrets in the repo settings.")
        sys.exit(1)
    tc = TradingClient(KEY, SECRET, paper=True)   # PAPER ONLY - never change this
    dc = StockHistoricalDataClient(KEY, SECRET)
    oc = OptionHistoricalDataClient(KEY, SECRET)
    if os.getenv("MODE", "run") == "check":
        return check(tc, dc, oc)
    run_loop(tc, dc, oc, GetCalendarRequest)


def run_loop(tc, dc, oc, GetCalendarRequest):
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
    last_fire = min(LAST_FIRE, hhmm(close_dt - timedelta(minutes=30)))
    exp = expiry(tc, today)
    log(f"Trend Flip bot | {', '.join(SYMBOLS)} on {', '.join(f'{t}m' for t in TFS)} | buy {QTY} 1st OTM, expiry {exp} | "
        f"+{TP_PCT}% sell {PARTIAL_QTY} | breakeven after +{BE_ARM_PCT}% | runner: candle {HOLD} or -{TRAIL_PCT}% from best | stop -{SL_PCT}% | "
        f"no new trades after {last_fire} | flat {flat_dt:%H:%M}")

    trades = recover_check(tc, load_state(today))
    save_state(trades, today)
    last_seen = {}
    ran_once = False
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
            sleep(20)
            continue

        # wait for the next minute (+3 s); check the % rules every few seconds while trades are open
        target = now.replace(second=0, microsecond=0) + timedelta(minutes=1, seconds=3)
        while True:
            rem = (target - now_et()).total_seconds()
            if rem <= 0:
                break
            if trades and fast_checks(tc, oc, trades):
                save_state(trades, today)
            sleep(min(rem, CHECK_SECS) if trades else rem)

        now = now_et()
        try:
            data = get_1m(dc)
        except Exception as e:
            log(f"bars failed: {e}")
            continue
        changed = False
        for sym in SYMBOLS:
            d1 = data.get(sym)
            if d1 is None or d1.empty:
                continue
            for tf in TFS:
                chart = f"{sym} {tf}m"
                df = to_tf(d1, tf, now)
                if len(df) < 120:
                    continue
                bar = df.index[-1]
                if last_seen.get(chart) == bar:
                    continue
                first_look = chart not in last_seen
                last_seen[chart] = bar
                if first_look and (now - (bar + pd.Timedelta(minutes=tf))).total_seconds() > 75:
                    continue                                        # old candle at start-up: don't act on it
                st, sg, en = trend_flip(df)
                bar_close = bar + pd.Timedelta(minutes=tf)
                spot = float(df["close"].iloc[-1])
                tr = trades.get(chart)
                if tr:
                    held = int((bar - pd.Timestamp(tr["entry_start"])) / pd.Timedelta(minutes=tf)) + 1
                    reason = None
                    if bar_close >= flat_dt:
                        reason = "FLAT before the close"
                    elif FLIP_EXIT and sg == -tr["side"]:
                        reason = "OPPOSITE FLIP"
                    elif held >= HOLD:
                        reason = f"TIME (candle {HOLD})"
                    if reason and sell(tc, tr, tr["qty"], reason, spot):
                        del trades[chart]
                        changed = True
                if (en != 0 and chart not in trades and len(trades) < MAX_OPEN
                        and (DIRECTION == 0 or en == DIRECTION)
                        and hhmm(bar_close) <= last_fire and bar_close < flat_dt and now < flat_dt):
                    log(f"{chart}: TREND FLIP {'GREEN - CALLS' if en == 1 else 'RED - PUTS'} at {bar_close:%H:%M} close {spot:.2f}")
                    new = enter(tc, oc, chart, sym, en, spot, bar_close, exp)
                    if new:
                        trades[chart] = new
                        changed = True
        if changed:
            save_state(trades, today)
        if not ran_once:
            log(f"watching {len(last_seen)} charts")
            ran_once = True
        if now >= flat_dt and trades:
            for chart, tr in list(trades.items()):
                if sell(tc, tr, tr["qty"], "FLAT before the close"):
                    del trades[chart]
            save_state(trades, today)

    save_state(trades, today)
    summary(today)


def summary(today):
    if not os.path.exists(LOG):
        log("No trades logged yet.")
        return
    rows = list(csv.DictReader(open(LOG)))
    td = [r for r in rows if r["date"] == today.isoformat()]
    tot = sum(float(r["pnl_usd"]) for r in td if r["pnl_usd"] not in ("", "nan"))
    alltot = sum(float(r["pnl_usd"]) for r in rows if r["pnl_usd"] not in ("", "nan"))
    lines = [f"## Trend Flip bot - {today}", f"Today: {len(td)} sales, **${tot:+,.2f}** | all time: ${alltot:+,.2f}", "",
             "| Chart | Side | Contract | Sold | Reason | In | Out | Entry | Exit | $ | % |", "|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in td:
        lines.append(f"| {r['chart']} | {r['side']} | {r['contract']} | {r['leg']} | {r['reason']} | {r['entry_time']} | "
                     f"{r['exit_time']} | {r['entry_fill']} | {r['exit_fill']} | {float(r['pnl_usd']):+.2f} | {r['pnl_pct']}% |")
    text = "\n".join(lines)
    log("\n" + text)
    s = os.getenv("GITHUB_STEP_SUMMARY")
    if s:
        with open(s, "a") as f:
            f.write(text + "\n")


if __name__ == "__main__":
    main()
