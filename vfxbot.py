"""
VIX FIX FORWARD TEST BOT - "FEAR / GREED MAXED" on SPY and QQQ (3-minute chart) through Alpaca PAPER.
PAPER ONLY - the paper=True switch in main() is hard-coded. Keys come from GitHub Secrets ALPACA_KEY / ALPACA_SECRET.
Pre-registered rules (frozen 2026-10-24): see results/VFX_FORWARD_TEST.md. DO NOT change the rules during the test.

SIGNAL : on a CLOSED 3m bar (extended hours included), Vix Fix FEAR F = wvf / highest(wvf, 50) * 100 (lookback 22)
         crosses up through 95 -> LONG (calls). GREED G does the same -> SHORT (puts). Entries 9:35 - 14:45 ET (bar close).
         The math is imported from backtest.py (vfx_pane, indicators, tlt_colors, ang_series, agr_series, to_tf) so it is
         the SAME code edge_main used - nothing is re-typed here.
SKIP   : the 6 readings that hurt in BOTH halves (edge_main bins): 1 trend line AGAINST you strong, 2 price 3+ ATR wrong
         side of VWAP, 3 against the day's move, 4 trend-line angle -15 or less, 5 TTM against you turning your way,
         6 your side's Vix Fix up 15-30 in the last 2 candles.
TRADE  : 1 contract, 2 strikes IN the money, 0DTE. Marketable limit BUY at the ask after the bar closes.
EXIT   : LINE COLOR - the trend line turns the other color on a closed 3m bar. Hard flat 15:55. Marketable limit SELL at the bid.
         One open trade per symbol; fires while open are logged and ignored. No averaging, no stops, no targets.
P&L    : booked from the LOGGED quotes (ask in, bid out) + $0.65 / contract / side, NOT from the paper fill.
CONTROL: for every real trade, one random 3m bar from the same 30-minute bucket, same symbol + direction, on the NEXT
         trading day(s), priced live the same way and exited the same way. LOGGED ONLY - never traded.
LOG    : results/vfx_forward_log.csv (one row per REAL / CONTROL trade, plus SKIPPED / IGNORED / NOFILL fires).
STATE  : results/vfx_state.json (open trades, open + pending control trades).
"""
import csv
import json
import os
import random
import sys
import time
from datetime import date, datetime, timedelta, timezone
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd

import backtest as B   # same indicator math as backtest.py edge_main

# ===== SETTINGS (frozen for the forward test) =====
SYMBOLS = ["SPY", "QQQ"]
TF = 3                       # chart minutes
LEVEL = 95                   # Vix Fix fear / greed level
ITM_STEPS = 2                # 2 strikes in the money
QTY = 1                      # contracts per trade
COMMISSION = 0.65            # $ per contract per side (booked in the log)
ENTRY_FROM, ENTRY_TO = 935, 1445   # signal bar CLOSE time window (ET)
FLAT_HHMM = 1555             # hard flat
BUCKET_MIN = 30              # control arm time-of-day bucket
ORDER_WAIT_S = 20            # wait for a marketable limit to fill before re-pricing
CHECK_SECS = 5
RUN_MINUTES = 340            # GitHub allows 6 h per run; the next scheduled run takes over from the state file
LOG = "results/vfx_forward_log.csv"
STATE = "results/vfx_state.json"
FLAGS = ["f1_line_against_strong", "f2_vwap_3atr_wrong", "f3_against_day", "f4_angle_le_-15",
         "f5_ttm_against_turning", "f6_own_vix_up_15_30"]
COLS = ["arm", "fire_id", "date", "symbol", "side", "signal_bar", "fg_value", *FLAGS, "skip", "contract", "strike",
        "spot_entry", "entry_time", "bid_in", "ask_in", "mid_in", "fill_in", "exit_time", "bid_out", "ask_out", "mid_out",
        "fill_out", "exit_reason", "gross_pct", "net_pct", "slip_in_pct", "slip_out_pct", "note"]

ET = ZoneInfo("America/New_York")
KEY = os.getenv("ALPACA_KEY", "").strip()
SECRET = os.getenv("ALPACA_SECRET", "").strip()


def now_et():
    return datetime.now(ET)


def log(msg):
    print(now_et().strftime("%H:%M:%S"), msg, flush=True)


def hhmm(dt):
    return dt.hour * 100 + dt.minute


def append_log(row):
    os.makedirs(os.path.dirname(LOG), exist_ok=True)
    new = not os.path.exists(LOG)
    with open(LOG, "a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLS, extrasaction="ignore")
        if new:
            w.writeheader()
        w.writerow({k: row.get(k, "") for k in COLS})


def load_state():
    try:
        with open(STATE) as f:
            return json.load(f)
    except Exception:
        return {}


def save_state(st):
    os.makedirs(os.path.dirname(STATE), exist_ok=True)
    with open(STATE, "w") as f:
        json.dump(st, f, indent=1, default=str)


# ===== Signal math (all from backtest.py) =====
def bars_3m(d1, now=None):
    """CLOSED 3m bars (4:00-20:00 ET) from 1m bars. The still-forming 3m bar is dropped."""
    df = B.to_tf(d1, rth_only=False, mins=TF)
    if now is not None:
        df = df[df.index + pd.Timedelta(minutes=TF) <= pd.Timestamp(now)]
    return df


def readings(df):
    """Per-bar arrays exactly as edge_main builds them (3m, extended hours, Vix 22/50, EMA 13 line)."""
    ind = B.indicators(df, 13, 34, True)
    col, ef = B.tlt_colors(df, ind)
    ang = np.nan_to_num(B.ang_series(df, ind, 5))
    m = B.agr_series(df, ind)["m"]
    F, G = B.vfx_pane(df)
    F, G = np.nan_to_num(F), np.nan_to_num(G)
    hm, day, c, o, a = ind["hm"], ind["day"], ind["c"], ind["o"], ind["atr"]
    rth = (hm >= 930) & (hm < 1600)
    dord = np.array([d_.toordinal() for d_ in day])
    o930 = pd.Series(np.where(rth, o, np.nan)).groupby(pd.Series(dord)).transform("first").to_numpy()
    return dict(F=F, G=G, col=np.asarray(col), ang=ang, m=np.asarray(m), vw=np.asarray(ind["vwap"]), a=np.asarray(a),
                c=np.asarray(c), hm=np.asarray(hm), dord=dord, move=c - o930)


def flags_at(R, i, sd):
    """the 6 'hurt' readings for side sd at bar i (same bins as edge_main FEAT: TLC, VWAP, WITH, ANG, TCOL, CHW)"""
    a = R["a"][i]
    W = R["G"] if sd == 1 else R["F"]           # edge_main 'your side' Vix Fix: greed for longs, fear for shorts
    mm, mmp = R["m"][i] * sd, (R["m"][i - 1] * sd if i >= 1 else np.nan)
    wchg = W[i] - W[i - 2] if i >= 2 else 0.0
    return {
        FLAGS[0]: int(2 + R["col"][i] * sd == 0),
        FLAGS[1]: int(np.nan_to_num((R["c"][i] - R["vw"][i]) / a * sd) < -3),
        FLAGS[2]: int(not (R["move"][i] * sd > 0)),
        FLAGS[3]: int(R["ang"][i] * sd < -15),
        FLAGS[4]: int(mm < 0 and mm > mmp),
        FLAGS[5]: int(15 <= np.nan_to_num(wchg) < 30),
    }


def fires_at(df, R, i):
    """[(side, F/G value)] for a fire on the CLOSED bar i (empty if none). Mirrors edge_main trigger 6 + its window."""
    if i < 1 or R["dord"][i] != R["dord"][i - 1] or not (np.isfinite(R["a"][i]) and R["a"][i] > 0):
        return []
    end = df.index[i] + pd.Timedelta(minutes=TF)
    if R["hm"][i] < 930 or not (ENTRY_FROM <= hhmm(end) <= ENTRY_TO):
        return []
    out = []
    if R["F"][i] >= LEVEL and R["F"][i - 1] < LEVEL:
        out.append((1, float(R["F"][i])))
    if R["G"][i] >= LEVEL and R["G"][i - 1] < LEVEL:
        out.append((-1, float(R["G"][i])))
    return out


def line_exit(R, i, sd):
    """LINE COLOR exit: the line turned the other color (long: red / pink, short: green / blue) on bar i"""
    return R["col"][i] <= -1 if sd == 1 else R["col"][i] >= 1


def all_fires(df):
    """every fire on a frame (for check mode / tests): [(i, side, value, flags, skip)]"""
    R = readings(df)
    out = []
    for i in range(len(df)):
        for sd, v in fires_at(df, R, i):
            fl = flags_at(R, i, sd)
            out.append((i, sd, v, fl, any(fl.values())))
    return out


# ===== Data =====
def get_1m(dc):
    """Closed 1-minute bars (pre/post market included) for all SYMBOLS, IEX feed like the other bots."""
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


def quote(oc, contract):
    """(bid, ask, mid) or None"""
    from alpaca.data.requests import OptionLatestQuoteRequest
    try:
        qs = oc.get_option_latest_quote(OptionLatestQuoteRequest(symbol_or_symbols=[contract]))
        q = qs.get(contract) if hasattr(qs, "get") else None
        if q is None:
            return None
        bid, ask = float(q.bid_price or 0), float(q.ask_price or 0)
        if bid <= 0 or ask <= 0 or ask < bid:
            return None
        return bid, ask, (bid + ask) / 2
    except Exception as e:
        log(f"quote failed {contract}: {e}")
        return None


def pick_itm(tc, sym, side, spot, exp):
    """2 strikes in the money from round(spot), like edge_main (k0 = round(spot), strike = k0 - 2 for calls, + 2 for puts)"""
    from alpaca.trading.enums import ContractType
    from alpaca.trading.requests import GetOptionContractsRequest
    req = GetOptionContractsRequest(
        underlying_symbols=[sym], expiration_date=exp,
        type=ContractType.CALL if side == 1 else ContractType.PUT,
        strike_price_gte=str(int(spot - 15)), strike_price_lte=str(int(spot + 15)), limit=200)
    cs = tc.get_option_contracts(req).option_contracts or []
    if not cs:
        return None
    want = round(spot) - ITM_STEPS * side
    return min(cs, key=lambda x: (abs(float(x.strike_price) - want), -side * float(x.strike_price)))


def status_of(o):
    return str(getattr(o.status, "value", o.status)).lower()


def limit_order(tc, oc, contract, buy, final=False):
    """Marketable limit at the ask (buy) / bid (sell). Re-priced up to 3 times; a sell on the final flat falls back to
    a market order. Returns (avg fill, quote used) or (None, last quote)."""
    from alpaca.trading.enums import OrderSide, TimeInForce
    from alpaca.trading.requests import LimitOrderRequest, MarketOrderRequest
    q = None
    for attempt in range(3):
        q = quote(oc, contract)
        if q is None:
            time.sleep(2)
            continue
        px = round(q[1] if buy else q[0], 2)
        try:
            o = tc.submit_order(LimitOrderRequest(symbol=contract, qty=QTY, limit_price=px,
                                                  side=OrderSide.BUY if buy else OrderSide.SELL,
                                                  time_in_force=TimeInForce.DAY))
        except Exception as e:
            log(f"order failed ({'BUY' if buy else 'SELL'} {contract} @ {px}): {e}")
            return None, q
        for _ in range(ORDER_WAIT_S * 2):
            o = tc.get_order_by_id(o.id)
            if status_of(o) == "filled" and o.filled_avg_price is not None:
                return float(o.filled_avg_price), q
            if status_of(o) in ("canceled", "rejected", "expired"):
                break
            time.sleep(0.5)
        try:
            tc.cancel_order_by_id(o.id)
            time.sleep(1)
            o = tc.get_order_by_id(o.id)
            if status_of(o) == "filled" and o.filled_avg_price is not None:
                return float(o.filled_avg_price), q
        except Exception:
            pass
    if not buy and final:
        try:
            o = tc.submit_order(MarketOrderRequest(symbol=contract, qty=QTY, side=OrderSide.SELL, time_in_force=TimeInForce.DAY))
            for _ in range(60):
                o = tc.get_order_by_id(o.id)
                if status_of(o) == "filled" and o.filled_avg_price is not None:
                    return float(o.filled_avg_price), quote(oc, contract) or q
                time.sleep(0.5)
        except Exception as e:
            log(f"market sell failed {contract}: {e}")
    return None, q


def book(tr, q_out, exit_time, reason, fill_out=""):
    """finish a trade row: P&L from the LOGGED quotes (ask in, bid out) + commission per side"""
    bid_in, ask_in, mid_in = tr["bid_in"], tr["ask_in"], tr["mid_in"]
    row = dict(tr)
    row.update(exit_time=exit_time, exit_reason=reason, fill_out=fill_out)
    if q_out:
        b, a, m = q_out
        cps = COMMISSION / 100                     # per share of premium
        row.update(bid_out=b, ask_out=a, mid_out=round(m, 4),
                   gross_pct=round((m / mid_in - 1) * 100, 3),
                   net_pct=round(((b - cps) - (ask_in + cps)) / (ask_in + cps) * 100, 3),
                   slip_in_pct=round((ask_in / mid_in - 1) * 100, 3),
                   slip_out_pct=round((1 - b / m) * 100, 3) if m > 0 else "")
    else:
        row["note"] = (row.get("note", "") + " no exit quote").strip()
    append_log(row)
    return row


# ===== the bot =====
class Bot:
    def __init__(self, tc, oc, today):
        self.tc, self.oc, self.today = tc, oc, today
        s = load_state()
        self.open = s.get("open", {}) if s.get("day") == today.isoformat() else {}
        self.ctrl_open = [c for c in s.get("ctrl_open", []) if c.get("date") == today.isoformat()]
        self.pending = s.get("pending", [])
        for c in s.get("ctrl_open", []):          # a control left open on an earlier day was never closed: redraw it
            if c.get("date") != today.isoformat():
                self.pending.append(dict(fire_id=c["fire_id"], symbol=c["symbol"], side=c["side"], bucket=c["bucket"],
                                         made=c.get("made", c["date"])))
        self.n = s.get("n", 0)
        self.rng = random.Random(f"{today.isoformat()}-{self.n}")
        self.draw_controls()

    def save(self):
        save_state(dict(day=self.today.isoformat(), open=self.open, ctrl_open=self.ctrl_open, pending=self.pending, n=self.n))

    def draw_controls(self):
        """give every pending control made on an EARLIER day a random closed-bar time inside its 30-minute bucket today"""
        for p in self.pending:
            if p.get("made", "") >= self.today.isoformat() or p.get("draw_day") == self.today.isoformat():
                continue
            b0 = p["bucket"]
            cands = []
            for mins in range(b0, b0 + BUCKET_MIN):
                hm_ = (mins // 60) * 100 + mins % 60
                if mins % TF == 0 and ENTRY_FROM <= hm_ <= ENTRY_TO and mins - TF >= 9 * 60 + 30:
                    cands.append(hm_)
            if cands:
                p["draw_day"], p["at"] = self.today.isoformat(), self.rng.choice(cands)

    def recover(self):
        try:
            held = {p.symbol: abs(int(float(p.qty))) for p in self.tc.get_all_positions()}
        except Exception as e:
            log(f"positions check failed: {e}")
            return
        for sym, tr in list(self.open.items()):
            if held.get(tr["contract"], 0) <= 0:
                log(f"{sym}: saved trade {tr['contract']} no longer held - logging it as LOST")
                book(tr, None, now_et().isoformat(timespec="seconds"), "LOST (not held at restart)")
                del self.open[sym]
            else:
                log(f"{sym}: taking over open trade {tr['contract']}")

    def on_bar(self, sym, df, R, i, now):
        """called once per newly CLOSED 3m bar i of sym"""
        bar_end = df.index[i] + pd.Timedelta(minutes=TF)
        end_hm = hhmm(bar_end)
        spot = float(R["c"][i])
        # 1) exits (real + control) on LINE COLOR
        tr = self.open.get(sym)
        if tr and bar_end > pd.Timestamp(tr["entry_time"]) and line_exit(R, i, _side(tr)):
            self.exit_real(sym, "LINE COLOR")
        for c in list(self.ctrl_open):
            if c["symbol"] == sym and bar_end > pd.Timestamp(c["entry_time"]) and line_exit(R, i, _side(c)):
                self.exit_ctrl(c, "LINE COLOR")
        # 2) controls due at this bar
        for p in list(self.pending):
            if p["symbol"] == sym and p.get("draw_day") == self.today.isoformat() and p.get("at") == end_hm:
                self.pending.remove(p)
                self.enter_ctrl(p, sym, spot, bar_end)
        # 3) fires
        for sd, v in fires_at(df, R, i):
            fl = flags_at(R, i, sd)
            skip = any(fl.values())
            self.n += 1
            fid = f"{self.today:%Y%m%d}-{sym}-{end_hm:04d}-{'L' if sd == 1 else 'S'}"
            base = dict(fire_id=fid, date=self.today.isoformat(), symbol=sym, side="LONG" if sd == 1 else "SHORT",
                        signal_bar=bar_end.isoformat(), fg_value=round(v, 2), **fl, skip=int(skip), spot_entry=spot)
            log(f"{sym}: {'FEAR' if sd == 1 else 'GREED'} MAXED {v:.1f} at {bar_end:%H:%M} | flags {list(fl.values())}"
                f"{' -> SKIP' if skip else ''}")
            if skip:
                append_log(dict(base, arm="SKIPPED"))
            elif sym in self.open:
                append_log(dict(base, arm="IGNORED", note="position open"))
            else:
                self.enter_real(base, sym, sd, spot, bar_end)
        self.save()

    def enter_real(self, base, sym, sd, spot, bar_end):
        try:
            c = pick_itm(self.tc, sym, sd, spot, self.today)
        except Exception as e:
            c = None
            log(f"{sym}: option lookup failed: {e}")
        if not c:
            append_log(dict(base, arm="NOFILL", note="no 0DTE contract"))
            return
        fill, q = limit_order(self.tc, self.oc, c.symbol, True)
        if fill is None or q is None:
            append_log(dict(base, arm="NOFILL", contract=c.symbol, strike=float(c.strike_price),
                            bid_in=q[0] if q else "", ask_in=q[1] if q else "", note="entry not filled"))
            return
        tr = dict(base, arm="REAL", contract=c.symbol, strike=float(c.strike_price), entry_time=now_et().isoformat(timespec="seconds"),
                  bid_in=q[0], ask_in=q[1], mid_in=round(q[2], 4), fill_in=fill, side_n=sd)
        self.open[sym] = tr
        log(f"{sym}: BUY {QTY} {c.symbol} @ {fill:.2f} (bid {q[0]:.2f} / ask {q[1]:.2f})")
        # control for this real trade: same symbol, side, 30-minute bucket, drawn on a later trading day
        mins = bar_end.hour * 60 + bar_end.minute
        self.pending.append(dict(fire_id=base["fire_id"], symbol=sym, side=sd, bucket=(mins // BUCKET_MIN) * BUCKET_MIN,
                                 made=self.today.isoformat()))
        self.save()

    def exit_real(self, sym, reason, final=False):
        tr = self.open[sym]
        fill, q = limit_order(self.tc, self.oc, tr["contract"], False, final=final)
        if fill is None and not final:
            log(f"{sym}: exit not filled - will retry")
            return
        row = book(tr, q, now_et().isoformat(timespec="seconds"), reason, fill_out=fill if fill is not None else "")
        log(f"{sym}: SELL {tr['contract']} ({reason}) net {row.get('net_pct', '?')}%")
        del self.open[sym]
        self.save()

    def enter_ctrl(self, p, sym, spot, bar_end):
        sd = p["side"]
        base = dict(arm="CONTROL", fire_id=p["fire_id"], date=self.today.isoformat(), symbol=sym,
                    side="LONG" if sd == 1 else "SHORT", signal_bar=bar_end.isoformat(), spot_entry=spot)
        try:
            c = pick_itm(self.tc, sym, sd, spot, self.today)
        except Exception as e:
            c = None
            log(f"{sym}: control option lookup failed: {e}")
        q = quote(self.oc, c.symbol) if c else None
        if not c or not q:
            p.pop("draw_day", None)               # redraw next trading day
            self.pending.append(p)
            return
        self.ctrl_open.append(dict(base, contract=c.symbol, strike=float(c.strike_price), entry_time=now_et().isoformat(timespec="seconds"),
                                   bid_in=q[0], ask_in=q[1], mid_in=round(q[2], 4), fill_in="", bucket=p["bucket"],
                                   made=p.get("made", ""), side_n=sd))
        log(f"{sym}: CONTROL (not traded) {base['side']} {c.symbol} ask {q[1]:.2f} for fire {p['fire_id']}")

    def exit_ctrl(self, c, reason):
        q = quote(self.oc, c["contract"])
        book(c, q, now_et().isoformat(timespec="seconds"), reason)
        self.ctrl_open.remove(c)

    def flat_all(self):
        for sym in list(self.open):
            self.exit_real(sym, "FLAT 15:55", final=True)
        for c in list(self.ctrl_open):
            self.exit_ctrl(c, "FLAT 15:55")
        self.save()


def _side(d):
    return 1 if d.get("side") == "LONG" else -1


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
    flat_dt = min(datetime.combine(today, datetime.min.time(), ET).replace(hour=15, minute=55), close_dt - timedelta(minutes=5))
    log(f"VFX forward test | {', '.join(SYMBOLS)} {TF}m | Vix Fix {LEVEL} | {QTY}x {ITM_STEPS} ITM 0DTE | "
        f"LINE COLOR exit | flat {flat_dt:%H:%M} | PAPER")
    bot = Bot(tc, oc, today)
    bot.recover()
    bot.save()
    last = {}
    while True:
        now = now_et()
        if time.time() - t_start > RUN_MINUTES * 60:
            log("Run time limit - the next scheduled run takes over (state saved).")
            break
        if now >= flat_dt:
            bot.flat_all()
            log("Flat - done for today.")
            break
        if hhmm(now) < 930:
            if hhmm(now) < 820:
                log("Too early, exiting.")
                break
            time.sleep(20)
            continue
        # wake 4 s after the next 3m boundary
        nxt = now.replace(second=0, microsecond=0) + timedelta(minutes=TF - now.minute % TF, seconds=4)
        time.sleep(max(0, (nxt - now_et()).total_seconds()))
        now = now_et()
        if now >= flat_dt:
            continue
        try:
            data = get_1m(dc)
        except Exception as e:
            log(f"bars failed: {e}")
            continue
        for sym in SYMBOLS:
            d1 = data.get(sym)
            if d1 is None or d1.empty:
                continue
            df = bars_3m(d1, now)
            if len(df) < 200:
                continue
            i = len(df) - 1
            bar = df.index[i]
            if last.get(sym) == bar:
                continue
            first = sym not in last
            last[sym] = bar
            if first and (now - (bar + pd.Timedelta(minutes=TF))).total_seconds() > 90:
                continue                       # stale bar at start-up: never act on it
            try:
                R = readings(df)
                bot.on_bar(sym, df, R, i, now)
            except Exception as e:
                log(f"{sym}: bar handling failed: {e}")
    bot.save()
    summary(today)


def summary(today):
    if not os.path.exists(LOG):
        log("No rows logged yet.")
        return
    rows = list(csv.DictReader(open(LOG)))
    real = [r for r in rows if r["arm"] == "REAL" and r["net_pct"] not in ("", None)]
    ctrl = [r for r in rows if r["arm"] == "CONTROL" and r["net_pct"] not in ("", None)]
    td = [r for r in rows if r["date"] == today.isoformat()]
    mean = lambda rs: (sum(float(r["net_pct"]) for r in rs) / len(rs)) if rs else float("nan")
    lines = [f"## VFX forward test - {today}",
             f"Today: {sum(r['arm'] == 'REAL' for r in td)} real trades, {sum(r['arm'] == 'SKIPPED' for r in td)} skipped fires",
             f"All time: {len(real)} real trades, mean net {mean(real):+.2f}% | {len(ctrl)} control, mean net {mean(ctrl):+.2f}%",
             "Checkpoints: 150 / 300 / 500 real trades - run `python vfx_report.py`. Do not peek-and-tweak in between."]
    text = "\n".join(lines)
    log("\n" + text)
    s = os.getenv("GITHUB_STEP_SUMMARY")
    if s:
        with open(s, "a") as f:
            f.write(text + "\n")


def check(tc, dc, oc):
    log("CHECK MODE - no trades")
    a = tc.get_account()
    log(f"account {a.status} | options level {getattr(a, 'options_trading_level', '?')}")
    data = get_1m(dc)
    today = now_et().date()
    for sym in SYMBOLS:
        d1 = data.get(sym)
        if d1 is None or d1.empty:
            log(f"{sym}: no bars")
            continue
        df = bars_3m(d1, now_et())
        fs = all_fires(df)
        log(f"{sym}: {len(df)} 3m bars | fires in the last 6 days: {len(fs)} ({sum(not f[4] for f in fs)} pass the filter)")
        for i, sd, v, fl, sk in fs[-8:]:
            log(f"   {df.index[i] + pd.Timedelta(minutes=TF):%m-%d %H:%M} {'LONG' if sd == 1 else 'SHORT'} {v:.1f} "
                f"flags {list(fl.values())} {'SKIP' if sk else 'TRADE'}")
        try:
            spot = float(d1["close"].iloc[-1])
            for sd in (1, -1):
                c = pick_itm(tc, sym, sd, spot, today)
                log(f"{sym} {spot:.2f}: 2 ITM {'call' if sd == 1 else 'put'} {c.symbol if c else 'none today'}"
                    + (f" quote {quote(oc, c.symbol)}" if c else ""))
        except Exception as e:
            log(f"{sym}: option lookup failed: {e}")
    log("CHECK OK")


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


if __name__ == "__main__":
    main()
