"""
STOCH BOT v2 - paper trades the Stoch Scalp / Confluence Pro setup on SPY 1m through Alpaca PAPER.
Entry (same as the TradingView indicator):
  LONG : Stoch 14-3-3 %K was under 20 in the last 3 bars and crosses up through %D while under 50
  SHORT: mirror (over 80, crosses down, still over 50)
  + TREND: EMA 21 above EMA 50 (longs) / below (shorts)
  + PRICE: signal candle closes your way, in the good half of its range
  Fires 9:35 - 15:30 ET, right after the 1m candle closes.
PLAN A (real paper orders): 0DTE option ~$1 in the money.
  Exits: SPY 3 ATR stop | option down OPT_STOP_PCT % | option up OPT_TP_PCT % (0 = off)
         | 48 bars | flat 5 min before the close. Stops are checked every 10 seconds.
  trades.csv also records the option's best % gain and worst % loss during every trade,
  so we can find the best % stop / % target later.
PLAN B (shadow, no orders): same signals, 4 ATR stop + exit when the Stoch flips.
  Priced off the option's mid quote and written to shadow_b.csv to compare with Plan A.
PAPER ONLY - the paper=True switch below is hard-coded.
"""
import csv
import os
import random
import string
import sys
import time
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

import pandas as pd
from alpaca.data.enums import DataFeed
from alpaca.data.historical import OptionHistoricalDataClient, StockHistoricalDataClient
from alpaca.data.requests import OptionLatestQuoteRequest, StockBarsRequest, StockLatestTradeRequest
from alpaca.data.timeframe import TimeFrame
from alpaca.trading.client import TradingClient
from alpaca.trading.enums import ContractType, OrderSide, QueryOrderStatus, TimeInForce
from alpaca.trading.requests import (
    GetCalendarRequest,
    GetOptionContractsRequest,
    GetOrdersRequest,
    MarketOrderRequest,
)

# ===== SETTINGS (edit here) =====
SYMBOL = "SPY"
K_LEN, K_SM, D_SM = 14, 3, 3
OVERSOLD, OVERBOUGHT, LOOK = 20, 80, 3
USE_TREND = True
USE_PRICE = True
FIRST_FIRE = 935         # HHMM ET
LAST_FIRE = 1530         # HHMM ET (moved earlier automatically on half days)
TRADE = "long+short"     # "long+short", "long", "short"

# Plan A (real paper orders)
STOP_ATR = 3.0           # stop on SPY price, in ATR
MAX_HOLD = 48            # bars
OPT_STOP_PCT = 40        # sell if the option is down this % from your fill (0 = off)
OPT_TP_PCT = 0           # sell if the option is up this % from your fill (0 = off)
STOCH_FLIP_EXIT = False  # True = also exit when the Stoch hooks the other way
COOLDOWN = 3             # bars after an exit
USE_OPTIONS = True
ITM_DOLLARS = 1.0        # strike this far in the money
QTY = 1                  # option contracts
FALLBACK_SHARES = 10     # used only if no option can be bought

# Plan B (shadow only, no orders)
SHADOW_B = True
B_STOP_ATR = 4.0
B_MAX_HOLD = 48
B_COOLDOWN = 3

RUN_MINUTES = 340        # GitHub allows 6 h per run; the next scheduled run picks up
LOG = "trades.csv"
LOG_B = "shadow_b.csv"

ET = ZoneInfo("America/New_York")
KEY = os.getenv("ALPACA_KEY", "").strip()
SECRET = os.getenv("ALPACA_SECRET", "").strip()


def log(msg):
    print(datetime.now(ET).strftime("%H:%M:%S"), msg, flush=True)


def hhmm(dt):
    return dt.hour * 100 + dt.minute


def write_row(path, row):
    new = not os.path.exists(path)
    with open(path, "a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(row.keys()))
        if new:
            w.writeheader()
        w.writerow(row)


# ===== Data + indicators =====
def get_bars(dc):
    now = datetime.now(timezone.utc)
    req = StockBarsRequest(symbol_or_symbols=SYMBOL, timeframe=TimeFrame.Minute,
                           start=now - timedelta(days=4), end=now, feed=DataFeed.IEX)
    df = dc.get_stock_bars(req).df
    if df is None or df.empty:
        return pd.DataFrame()
    if isinstance(df.index, pd.MultiIndex):
        df = df.xs(SYMBOL, level=0)
    df = df.sort_index()
    df = df[df.index + pd.Timedelta(minutes=1) <= pd.Timestamp(now)]  # closed bars only
    return df[["open", "high", "low", "close"]].astype(float)


def add_indicators(df):
    h, l, c = df["high"], df["low"], df["close"]
    pc = c.shift(1)
    tr = pd.concat([h - l, (h - pc).abs(), (l - pc).abs()], axis=1).max(axis=1)
    df["atr"] = tr.ewm(alpha=1 / 14, adjust=False).mean()
    df["ema21"] = c.ewm(span=21, adjust=False).mean()
    df["ema50"] = c.ewm(span=50, adjust=False).mean()
    ll, hh = l.rolling(K_LEN).min(), h.rolling(K_LEN).max()
    raw = 100 * (c - ll) / (hh - ll).replace(0, float("nan"))
    df["k"] = raw.rolling(K_SM).mean()
    df["d"] = df["k"].rolling(D_SM).mean()
    return df


def hook(df):
    """+1 long hook, -1 short hook, 0 none, on the last closed bar."""
    k, d = df["k"], df["d"]
    if len(df) < 60 or pd.isna(k.iloc[-1]) or pd.isna(d.iloc[-2]):
        return 0
    up = k.iloc[-1] > d.iloc[-1] and k.iloc[-2] <= d.iloc[-2] and k.iloc[-LOOK:].min() < OVERSOLD and k.iloc[-1] < 50
    dn = k.iloc[-1] < d.iloc[-1] and k.iloc[-2] >= d.iloc[-2] and k.iloc[-LOOK:].max() > OVERBOUGHT and k.iloc[-1] > 50
    return 1 if up else -1 if dn else 0


def signal(df, last_fire):
    r = df.iloc[-1]
    t = df.index[-1].tz_convert(ET)
    if not (FIRST_FIRE <= hhmm(t) < last_fire):
        return 0
    h = hook(df)
    if h == 0:
        return 0
    rng = r["high"] - r["low"]
    clv = (r["close"] - r["low"]) / rng if rng > 0 else 0.5
    if h == 1:
        ok = TRADE != "short"
        ok = ok and (not USE_TREND or r["ema21"] > r["ema50"])
        ok = ok and (not USE_PRICE or (r["close"] > r["open"] and clv >= 0.5))
    else:
        ok = TRADE != "long"
        ok = ok and (not USE_TREND or r["ema21"] < r["ema50"])
        ok = ok and (not USE_PRICE or (r["close"] < r["open"] and clv <= 0.5))
    return h if ok else 0


def latest_price(dc):
    try:
        r = dc.get_stock_latest_trade(StockLatestTradeRequest(symbol_or_symbols=SYMBOL, feed=DataFeed.IEX))
        return float(r[SYMBOL].price)
    except Exception:
        return None


def option_mid(oc, sym):
    try:
        q = oc.get_option_latest_quote(OptionLatestQuoteRequest(symbol_or_symbols=sym))[sym]
        bid, ask = float(q.bid_price or 0), float(q.ask_price or 0)
        if bid > 0 and ask > 0:
            return (bid + ask) / 2
        return ask or bid or None
    except Exception:
        return None


# ===== Orders =====
def status_of(o):
    return str(getattr(o.status, "value", o.status)).lower()


def wait_fill(tc, oid, secs=30):
    for _ in range(secs * 2):
        o = tc.get_order_by_id(oid)
        if o.filled_avg_price is not None and status_of(o) == "filled":
            return float(o.filled_avg_price)
        if status_of(o) in ("canceled", "rejected", "expired"):
            log(f"order {status_of(o)}")
            return None
        time.sleep(0.5)
    return None


def pick_option(tc, side, spot):
    today = datetime.now(ET).date()
    req = GetOptionContractsRequest(
        underlying_symbols=[SYMBOL], expiration_date=today,
        type=ContractType.CALL if side == 1 else ContractType.PUT,
        strike_price_gte=str(int(spot - 15)), strike_price_lte=str(int(spot + 15)), limit=200)
    cs = tc.get_option_contracts(req).option_contracts or []
    if side == 1:
        c = [x for x in cs if float(x.strike_price) <= spot - ITM_DOLLARS]
        return max(c, key=lambda x: float(x.strike_price)) if c else None
    c = [x for x in cs if float(x.strike_price) >= spot + ITM_DOLLARS]
    return min(c, key=lambda x: float(x.strike_price)) if c else None


def make_cid(side, spot, stop, bar_ts, atr):
    tag = "".join(random.choices(string.ascii_lowercase, k=4))
    return f"sb_{side}_{spot:.2f}_{stop:.2f}_{int(bar_ts.timestamp())}_{atr:.4f}_{tag}"


def enter(tc, side, spot, atr, bar_ts):
    stop = spot - side * STOP_ATR * atr
    cid = make_cid(side, spot, stop, bar_ts, atr)
    sym, is_opt, qty, oside = SYMBOL, False, FALLBACK_SHARES, OrderSide.BUY if side == 1 else OrderSide.SELL
    if USE_OPTIONS:
        try:
            c = pick_option(tc, side, spot)
            if c:
                sym, is_opt, qty, oside = c.symbol, True, QTY, OrderSide.BUY
        except Exception as e:
            log(f"option lookup failed, using shares: {e}")
    try:
        o = tc.submit_order(MarketOrderRequest(symbol=sym, qty=qty, side=oside,
                                               time_in_force=TimeInForce.DAY, client_order_id=cid))
    except Exception as e:
        log(f"entry order failed: {e}")
        return None
    fill = wait_fill(tc, o.id)
    if fill is None:
        return None
    log(f"A ENTER {'LONG' if side == 1 else 'SHORT'} {sym} x{qty} @ {fill} | SPY {spot:.2f} stop {stop:.2f}")
    return dict(side=side, sym=sym, is_opt=is_opt, qty=qty, spot=spot, stop=stop, atr=atr,
                bar_ts=bar_ts, fill=fill, t=datetime.now(ET), best=0.0, worst=0.0)


def recover(tc):
    """Pick up an open position left by an earlier run (details are stored in the order id)."""
    try:
        for p in tc.get_all_positions():
            if not p.symbol.startswith(SYMBOL):
                continue
            orders = tc.get_orders(GetOrdersRequest(status=QueryOrderStatus.CLOSED, symbols=[p.symbol], limit=20))
            for o in orders:
                cid = o.client_order_id or ""
                if cid.startswith("sb_") and status_of(o) == "filled":
                    _, side, spot, stop, ts, atr, _ = cid.split("_")
                    pos = dict(side=int(side), sym=p.symbol, is_opt=p.symbol != SYMBOL, qty=abs(int(float(p.qty))),
                               spot=float(spot), stop=float(stop), atr=float(atr),
                               bar_ts=pd.Timestamp(int(ts), unit="s", tz="UTC"),
                               fill=float(o.filled_avg_price), t=o.filled_at.astimezone(ET), best=0.0, worst=0.0)
                    log(f"recovered open position {p.symbol}")
                    return pos
    except Exception as e:
        log(f"recover failed: {e}")
    return None


def exit_pos(tc, pos, reason, spot):
    try:
        o = tc.close_position(pos["sym"])
        fill = wait_fill(tc, o.id)
    except Exception as e:
        log(f"exit failed: {e}")
        return False
    fill = fill if fill is not None else float("nan")
    if pos["is_opt"]:
        pnl = (fill - pos["fill"]) * 100 * pos["qty"]
        pct = (fill / pos["fill"] - 1) * 100 if pos["fill"] else 0
    else:
        pnl = pos["side"] * (fill - pos["fill"]) * pos["qty"]
        pct = pos["side"] * (fill / pos["fill"] - 1) * 100 if pos["fill"] else 0
    move = pos["side"] * (spot - pos["spot"]) / pos["atr"] if pos["atr"] else 0
    mins = (datetime.now(ET) - pos["t"]).total_seconds() / 60
    write_row(LOG, dict(
        date=datetime.now(ET).strftime("%Y-%m-%d"), side="LONG" if pos["side"] == 1 else "SHORT",
        entry_time=pos["t"].strftime("%H:%M"), exit_time=datetime.now(ET).strftime("%H:%M"),
        minutes=round(mins, 1), reason=reason, spy_entry=round(pos["spot"], 2), spy_exit=round(spot, 2),
        move_atr=round(move, 2), symbol=pos["sym"], qty=pos["qty"], entry_fill=pos["fill"], exit_fill=fill,
        pnl_usd=round(pnl, 2), pnl_pct=round(pct, 1),
        best_pct=round(pos["best"], 1), worst_pct=round(pos["worst"], 1)))
    log(f"A EXIT {reason} {pos['sym']} @ {fill} | ${pnl:.2f} ({pct:+.0f}%) | best {pos['best']:+.0f}% worst {pos['worst']:+.0f}% | {mins:.0f} min")
    return True


# ===== Plan B shadow =====
def b_enter(tc, oc, side, spot, atr, bar_ts):
    try:
        c = pick_option(tc, side, spot)
    except Exception:
        c = None
    if not c:
        return None
    m = option_mid(oc, c.symbol)
    if not m:
        return None
    log(f"B (shadow) ENTER {'LONG' if side == 1 else 'SHORT'} {c.symbol} mid {m:.2f}")
    return dict(side=side, sym=c.symbol, spot=spot, stop=spot - side * B_STOP_ATR * atr, atr=atr,
                bar_ts=bar_ts, entry=m, t=datetime.now(ET), best=0.0, worst=0.0)


def b_exit(oc, sh, reason, spot):
    m = option_mid(oc, sh["sym"])
    m = m if m is not None else float("nan")
    pnl = (m - sh["entry"]) * 100
    pct = (m / sh["entry"] - 1) * 100
    move = sh["side"] * (spot - sh["spot"]) / sh["atr"] if sh["atr"] else 0
    mins = (datetime.now(ET) - sh["t"]).total_seconds() / 60
    write_row(LOG_B, dict(
        date=datetime.now(ET).strftime("%Y-%m-%d"), side="LONG" if sh["side"] == 1 else "SHORT",
        entry_time=sh["t"].strftime("%H:%M"), exit_time=datetime.now(ET).strftime("%H:%M"),
        minutes=round(mins, 1), reason=reason, spy_entry=round(sh["spot"], 2), spy_exit=round(spot, 2),
        move_atr=round(move, 2), symbol=sh["sym"], entry_mid=round(sh["entry"], 2), exit_mid=round(m, 2),
        pnl_usd=round(pnl, 2), pnl_pct=round(pct, 1),
        best_pct=round(sh["best"], 1), worst_pct=round(sh["worst"], 1)))
    log(f"B (shadow) EXIT {reason} {sh['sym']} | ${pnl:.2f} ({pct:+.0f}%) | {mins:.0f} min")


def track_pct(d, now_px, base):
    if now_px and base:
        pct = (now_px / base - 1) * 100
        d["best"] = max(d["best"], pct)
        d["worst"] = min(d["worst"], pct)
        return pct
    return None


# ===== Check mode =====
def check(tc, dc, oc):
    log("CHECK MODE - no trades")
    a = tc.get_account()
    log(f"account {a.status} | cash ${a.cash} | options level {getattr(a, 'options_trading_level', '?')}")
    df = add_indicators(get_bars(dc))
    log(f"{len(df)} bars loaded, last {df.index[-1].tz_convert(ET) if len(df) else 'none'}")
    if len(df):
        r = df.iloc[-1]
        log(f"SPY {r['close']:.2f} | K {r['k']:.0f} D {r['d']:.0f} | ATR {r['atr']:.3f} | trend {'up' if r['ema21'] > r['ema50'] else 'down'}")
        try:
            c = pick_option(tc, 1, r["close"])
            if c:
                log(f"today's ITM call: {c.symbol} | mid quote {option_mid(oc, c.symbol)}")
            else:
                log("no 0DTE contract found (market closed or no expiry today)")
        except Exception as e:
            log(f"option lookup failed: {e}")
    log("CHECK OK - keys work")


# ===== Main loop =====
def main():
    if not KEY or not SECRET:
        log("Missing ALPACA_KEY / ALPACA_SECRET secrets in the repo settings.")
        sys.exit(1)
    tc = TradingClient(KEY, SECRET, paper=True)   # PAPER ONLY
    dc = StockHistoricalDataClient(KEY, SECRET)
    oc = OptionHistoricalDataClient(KEY, SECRET)
    if os.getenv("MODE", "run") == "check":
        check(tc, dc, oc)
        return

    start = time.time()
    today = datetime.now(ET).date()
    cal = tc.get_calendar(GetCalendarRequest(start=today, end=today))
    if not cal:
        log("Market closed today.")
        return
    close_dt = cal[0].close
    if not isinstance(close_dt, datetime):
        close_dt = datetime.combine(today, close_dt)
    close_dt = close_dt.replace(tzinfo=ET) if close_dt.tzinfo is None else close_dt.astimezone(ET)
    flat_dt = close_dt - timedelta(minutes=5)
    last_fire = min(LAST_FIRE, hhmm(close_dt - timedelta(minutes=30)))
    log(f"Market closes {close_dt:%H:%M} ET | last fire {last_fire} | flat {flat_dt:%H:%M} | "
        f"A: {STOP_ATR} ATR stop, option stop {OPT_STOP_PCT}%, TP {OPT_TP_PCT}% | B shadow: {SHADOW_B}")

    pos = recover(tc)
    sh = None
    last_bar = None
    last_exit_a = last_exit_b = -999
    bar_count = 0

    while True:
        now = datetime.now(ET)
        if time.time() - start > RUN_MINUTES * 60:
            log("Run time limit - next scheduled run takes over.")
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

        # wait for the next candle to close (+3 s); while in a trade, check stops every 10 seconds
        target = now.replace(second=0, microsecond=0) + timedelta(minutes=1, seconds=3)
        while True:
            rem = (target - datetime.now(ET)).total_seconds()
            if rem <= 0:
                break
            if pos or sh:
                px = latest_price(dc)
                if pos:
                    hit = px and ((pos["side"] == 1 and px <= pos["stop"]) or (pos["side"] == -1 and px >= pos["stop"]))
                    reason = "STOP" if hit else None
                    if pos["is_opt"] and not reason:
                        pct = track_pct(pos, option_mid(oc, pos["sym"]), pos["fill"])
                        if pct is not None and OPT_STOP_PCT > 0 and pct <= -OPT_STOP_PCT:
                            reason = "OPT_STOP"
                        elif pct is not None and OPT_TP_PCT > 0 and pct >= OPT_TP_PCT:
                            reason = "OPT_TP"
                    if reason and exit_pos(tc, pos, reason, px or pos["spot"]):
                        pos = None
                        last_exit_a = bar_count
                if sh:
                    track_pct(sh, option_mid(oc, sh["sym"]), sh["entry"])
                    if px and ((sh["side"] == 1 and px <= sh["stop"]) or (sh["side"] == -1 and px >= sh["stop"])):
                        b_exit(oc, sh, "STOP", px)
                        sh = None
                        last_exit_b = bar_count
            time.sleep(min(rem, 10) if (pos or sh) else rem)

        try:
            df = get_bars(dc)
        except Exception as e:
            log(f"bars failed: {e}")
            continue
        if df.empty or df.index[-1] == last_bar:
            continue
        last_bar = df.index[-1]
        bar_count += 1
        df = add_indicators(df)
        r = df.iloc[-1]
        bar_close = last_bar.tz_convert(ET) + timedelta(minutes=1)
        hk = hook(df)
        s = signal(df, last_fire) if bar_close < flat_dt else 0

        # ----- Plan A -----
        if pos:
            held = int((df.index >= pos["bar_ts"]).sum())
            reason = None
            if (pos["side"] == 1 and r["low"] <= pos["stop"]) or (pos["side"] == -1 and r["high"] >= pos["stop"]):
                reason = "STOP"
            elif held >= MAX_HOLD:
                reason = "TIME"
            elif bar_close >= flat_dt:
                reason = "FLAT"
            elif STOCH_FLIP_EXIT and hk == -pos["side"]:
                reason = "FLIP"
            if reason and exit_pos(tc, pos, reason, r["close"]):
                pos = None
                last_exit_a = bar_count
        elif s != 0 and bar_count - last_exit_a >= COOLDOWN:
            pos = enter(tc, s, r["close"], r["atr"], last_bar + pd.Timedelta(minutes=1))

        # ----- Plan B (shadow) -----
        if SHADOW_B:
            if sh:
                held = int((df.index >= sh["bar_ts"]).sum())
                reason = None
                if (sh["side"] == 1 and r["low"] <= sh["stop"]) or (sh["side"] == -1 and r["high"] >= sh["stop"]):
                    reason = "STOP"
                elif hk == -sh["side"]:
                    reason = "FLIP"
                elif held >= B_MAX_HOLD:
                    reason = "TIME"
                elif bar_close >= flat_dt:
                    reason = "FLAT"
                if reason:
                    b_exit(oc, sh, reason, r["close"])
                    sh = None
                    last_exit_b = bar_count
            elif s != 0 and bar_count - last_exit_b >= B_COOLDOWN:
                sh = b_enter(tc, oc, s, r["close"], r["atr"], last_bar + pd.Timedelta(minutes=1))

    if sh:
        b_exit(oc, sh, "RUN_END", sh["spot"])
    for path, name in ((LOG, "A"), (LOG_B, "B shadow")):
        if os.path.exists(path):
            rows = list(csv.DictReader(open(path)))
            td = [x for x in rows if x["date"] == today.isoformat()]
            tot = sum(float(x["pnl_usd"]) for x in td if x["pnl_usd"] not in ("", "nan"))
            log(f"{name} today: {len(td)} trades, ${tot:.2f} | all time: {len(rows)} trades")


if __name__ == "__main__":
    main()
