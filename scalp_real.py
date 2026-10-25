"""
0DTE SPY/QQQ scalp exits on real Alpaca OPRA 1-minute option bars.

DATA ONLY. This script reads historical stock and option bars. It does not
import an order client, submit orders, or send a trade. It is a research
tool, not trading advice.

Run locally only with keys you are allowed to use:

    ALPACA_KEY=... ALPACA_SECRET=... python scalp_real.py

The supported run is the manually triggered workflow
.github/workflows/scalp_real.yml (Actions tab, scalp_real, Run workflow).
Keys come from the ALPACA_KEY and ALPACA_SECRET secrets. They are never
printed.

Outputs (written at the end of a run):
    results/SCALP_REAL.md
    results/scalp_real_results.csv
    results/scalp_real_trades.csv

The config list in results/SCALP_REAL_PREDECLARED.txt is checked against
this file before any bar is downloaded. A mismatch stops the run.
"""

from __future__ import annotations

import builtins
import hashlib
import math
import os
import sys
import time
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd

NY = ZoneInfo("America/New_York")
FLAT_MIN = (15 * 60 + 55) - (9 * 60 + 30)  # 385, the 15:55 bar
N_MIN = 390
STALE_AFTER = 5          # a carried print older than this is not an exit
ENTRY_LOOK = 2           # intended minute and the next one
MIN_PREMIUM = 0.05
SEED = 20261024
BOOT_DEFAULT = 2000
HOLD_FRAC = 0.25
TOP_K = 3
MIN_TRADES = 5

# Snapshot of diamondbot.BOOKS["TUNED"] and its entry window. The signal
# function reads the live constants; tests fail if the bot drifts.
TUNED_DIAMOND = (30, 14, 3, 1.0, 30, 50, 5, 70, 1)
DIAMOND_ENTRY_FROM = 945
DIAMOND_ENTRY_TO = 1430

TPS = (0.10, 0.15, 0.20, 0.30)
SLS = (0.10, 0.15, 0.20, 0.30, None)
TIME_STOPS = (5, 10, 20, 30)
STRIKE_MODES = ("atm", "2itm")

# id, role, chart minutes, entry window on the signal bar (hhmm, half-open), blurb
SIGNALS = (
    ("random", "baseline", 1, (935, 1525),
     "(a) reference random book: each day and symbol draws N minutes, N = the median raw fire count of the other signals that day"),
    ("vix95_filt_3m", "search", 3, (935, 1445),
     "(b) Vix Fix fear/greed crosses up through 95 on 3-minute bars, then the 6-flag skip filter"),
    ("vix95_raw_3m", "search", 3, (935, 1445),
     "(c) Vix Fix 95 cross, 3-minute, no skip filter. This is also the 3-minute half of (l); it is listed once"),
    ("ttm_squeeze_3m", "search", 3, (935, 1530),
     "(d) TTM squeeze fire on 3-minute bars, trade the sign of TTM momentum"),
    ("ema_vwap_flip_3m", "search", 3, (935, 1530),
     "(e) EMA13/34 + VWAP line turns green (call) or red (put) on a 3-minute close"),
    ("angle_flat_23_1m", "search", 1, (935, 1530),
     "(f) 1-minute trend-line angle flattens through +23 deg (call) or -23 deg (put)"),
    ("orb_1m", "search", 1, (945, 1530),
     "(g) opening-range break: first 1-minute close beyond the 9:30-9:45 high or low, once per side"),
    ("vwap_reclaim_1m", "search", 1, (945, 1530),
     "(h) 1-minute close crosses VWAP, 9:45-15:30"),
    ("mom5_1m", "search", 1, (935, 1530),
     "(i) 1-minute 5-bar return beyond 0.10 percent, same direction, 10-minute cooldown"),
    ("diamond_tuned_1m", "search", 1, (945, 1430),
     "(j) diamondbot TUNED diamond on 1-minute bars, both directions (green call, red put)"),
    ("vix_unison_1m", "search", 1, (935, 1445),
     "(k) 1-minute Fear and Greed both >= 80 inside 3 bars; call when close < EMA13, put when close > EMA13"),
    ("vix_unison_1m_flip", "search", 1, (935, 1445),
     "(k) the same 1-minute unison, direction flipped"),
    ("vix_unison_3m", "search", 3, (935, 1445),
     "(k) 3-minute unison, call below EMA13 / put above"),
    ("vix_unison_3m_flip", "search", 3, (935, 1445),
     "(k) 3-minute unison, direction flipped"),
    ("vix95_raw_1m", "search", 1, (935, 1445),
     "(l) Vix Fix 95 cross on 1-minute bars, no skip filter"),
)

SIGNAL_IDS = tuple(s[0] for s in SIGNALS)
SEARCH_IDS = tuple(s[0] for s in SIGNALS if s[1] == "search")
SIGNAL_BLURB = {s[0]: s[4] for s in SIGNALS}
SIGNAL_TF = {s[0]: s[2] for s in SIGNALS}

RESULT_FIELDS = [
    "signal", "strike", "tp", "sl", "time_stop", "split", "role",
    "n", "n_attempts", "trades_per_day", "hit_rate", "mean_net_pct",
    "usd_per_day", "max_drawdown_usd", "t", "p", "t_diff", "p_diff",
    "boot_lo", "boot_hi", "boot_diff_lo", "boot_diff_hi",
    "random_n", "random_hit_rate", "random_mean_net_pct", "random_t",
    "n_skip_entry", "n_skip_stale", "n_skip_spot", "n_days",
    "breakeven_hit_rate", "q_fdr", "bonferroni_05", "beats_random",
    "selected_top3",
]

TRADE_FIELDS = [
    "date", "time", "symbol", "side", "entry", "exit", "reason", "net_pct",
    "signal", "strike", "tp", "sl", "time_stop", "split", "book",
    "contract", "dollar",
]


def search_config_count():
    """Bonferroni family: every search signal x strike x exit. Random is the control."""
    return len(SEARCH_IDS) * len(STRIKE_MODES) * len(TPS) * len(SLS) * len(TIME_STOPS)


def iter_configs():
    for sig in SIGNAL_IDS:
        for strike in STRIKE_MODES:
            for tp in TPS:
                for sl in SLS:
                    for ts in TIME_STOPS:
                        yield sig, strike, tp, sl, ts


def _fmt_sl(sl):
    return "none" if sl is None else f"{sl:.2f}"


def render_predeclared():
    """Frozen text. Written before any OPRA run. main() refuses to compute if the file differs."""
    n_search = search_config_count()
    n_all = n_search + len(STRIKE_MODES) * len(TPS) * len(SLS) * len(TIME_STOPS)
    lines = [
        "SCALP_REAL PREDECLARED 2026-10-24",
        "Written before any OPRA computation. Do not add a config after seeing results.",
        "DATA ONLY. No order is sent by scalp_real.py or by .github/workflows/scalp_real.yml.",
        "This file is a research plan, not trading advice.",
        "",
        "DATA",
        "- SPY and QQQ, 0DTE, strikes atm and 2itm (workflow input may run a subset; the family below is the full grid).",
        "- As many recent completed sessions as the workflow days input asks for (default 60).",
        "- A session needs at least 180 regular-hours 1-minute bars on every symbol. Today is excluded until 16:00 ET.",
        "- Days on which Alpaca returns no OPRA 1-minute bar for any requested contract are dropped before the split.",
        "- If fewer than the requested number remain, the run uses what remains and says so.",
        "- Underlying bars: backtest.fetch_1m. Option bars: backtest.lab_fetch_opt (closes, forward-filled at most 5 minutes)",
        "  plus the open/high/low of the same response for the entry print and for stop/target wicks.",
        "- Indicators that need a warmup use the extended-hours feed inside backtest.to_tf / indicators, same as edge_main.",
        "",
        "COSTS (per side)",
        "- Ask-side entry proxy = open of the entry bar + max(1 cent, 0.5% of that open). Both numbers are workflow inputs.",
        "- Bid-side exit proxy = exit print - max(1 cent, 0.5% of that print), floored at 0.",
        "- Commission 0.65 dollars per contract per side (workflow input). One contract. Multiplier 100.",
        "- Net % = (exit credit - entry debit) * 100 - 2 * commission, divided by (entry debit * 100).",
        "- Take-profit and stop are measured from the raw entry open, before the extra half-spread.",
        "",
        "FILLS",
        "- A signal is known at its bar close. The entry minute is the next 1-minute bar after that close. No earlier bar is used.",
        "- The entry print is the open of the first REAL option bar at that minute or the following minute (within 2 minutes).",
        "- No real print in those two minutes: skip the entry and count it. A forward-filled price is not an entry.",
        "- An option open under 0.05 is skipped.",
        "- Exits walk 1-minute bars. A minute with no print may use the lab_fetch_opt close only when that close is at most 5 minutes old.",
        "- A price older than 5 minutes is never an exit. If the time stop or the 15:55 flat falls on a stale minute, the trade is unfilled and counted.",
        "- Same bar: a stop is applied before a target. A stop that gaps fills at the bar open when that open is worse than the stop.",
        "- A target fills at the target price (not at a higher wick).",
        "- One open position per symbol inside each (signal, strike) book. A new signal while the book is in a trade is ignored.",
        "- Calls at the same minute are considered before puts. Flat at the 15:55 bar (session minute 385). No new entry at or after 15:55.",
        "",
        "SPLIT AND TESTS",
        "- After dead OPRA days are dropped, the last round(25%) of remaining days, at least 1, are held out.",
        "- Held-out days are scored once, and only for the top 3 in-sample configs of each search signal.",
        "- Rank key (in-sample only): day-clustered t of (signal net % - paired-random net %) on trades where both filled,",
        "  then mean net %, then trade count. A config needs at least 5 signal fills and 5 paired fills to be ranked.",
        "- Primary t-stat is day-clustered on the per-trade net percent (sum of within-day deviations, divided by n).",
        "- Bootstrap 95% CI resamples days with replacement (default 2000) and recomputes the per-trade mean. Seed 20261024 plus a fixed per-config salt.",
        f"- Search family N = {n_search} (every search signal x atm/2itm x 4 targets x 5 stops x 4 time stops).",
        "- The random rows are the baseline. They are not in N and they are not ranked for the holdout.",
        "- Bonferroni: two-sided normal p * N < 0.05. FDR: Benjamini-Hochberg on the in-sample paired-difference p-values.",
        "- Break-even hit rate assumes the trade exits at the target or the stop and never by time: p = -net_loss / (net_win - net_loss),",
        "  with the same half-spread and commission, at that config's in-sample median entry open. No stop -> not defined.",
        "",
        "RANDOM",
        "- Paired control (the comparison column): one control per one-position entry attempt, same symbol, day, and direction,",
        "  minute drawn from the same 30-minute clock bucket inside 9:35-15:25, excluding the signal minute.",
        "  If that bucket is empty, the draw uses the whole 9:35-15:25 window. Controls are not put through a second one-position rule,",
        "  so the attempt count stays matched. Seed = SHA256('paired', signal, strike, day, symbol, entry minute, side).",
        "- Reference book (signal id random): per day and symbol, N = round-half-up median of the other signals' raw fire counts that day.",
        "  N distinct minutes from 9:35-15:25, fair coin direction, then the same one-position rule and the same exits.",
        "  Seed = SHA256('ref', day, symbol). This book is a portfolio baseline, so its trade count can fall below N after the one-position rule.",
        "",
        "SIGNALS (chart, window, rule). Extended hours feed the indicators. The window is when a closed bar may fire.",
        "- Vix Fix pane = wvf / highest(wvf, 50) * 100 and the greed mirror, lookback 22, from backtest.vfx_pane.",
        "- A 95-cross is the first bar where that pane is >= 95 and the previous bar was < 95. Fear cross -> call. Greed cross -> put.",
        "  Both on the same bar -> skip. Window 9:35-14:45 ET.",
        "- (b) skip the cross if ANY of these is true on the signal bar (frozen from the Vix Fix forward test):",
        "  1. Trend-line color (backtest.tlt_colors) is strongly against the trade: color * side == -2.",
        "  2. Close is 3 or more ATR on the wrong side of VWAP: side * (close - vwap) / atr <= -3.",
        "  3. The trade is against the day's move: side * (close - 9:30 open) < 0.",
        "  4. Trend-line angle (EMA13 slope over 5 bars, in degrees) is -15 or worse against the trade: side * angle <= -15.",
        "  5. TTM momentum is against the trade and turning back: (m * side) < 0 and (m * side) rose versus the prior bar.",
        "     m is backtest.agr_series momentum / ATR.",
        "  6. The trade's own Vix Fix pane rose by 15 up to but not including 30 points over the prior 2 bars.",
        "     That is the learned 'up 15-30' bin (edges 5/15/30), not the 30+ bin.",
        "- (d) Squeeze: Bollinger 20/2 inside Keltner 20/1.5 on the 3-minute chart. Fire = previous bar inside, this bar outside.",
        "  Direction = sign of TTM momentum. 9:35-15:30.",
        "- (e) Line color from backtest.indicators (EMA13 vs EMA34 and close vs VWAP). Fire when the color newly becomes green or red. 3-minute, 9:35-15:30.",
        "- (f) backtest.ang_events mode 'dn' at 23 degrees on 1-minute bars. The degree scale was defined on the 1-minute angle study. 9:35-15:30.",
        "- (g) Opening range = high and low of the first 15 regular-hours minutes (9:30-9:44). First later close strictly beyond it, once per side.",
        "- (h) Previous close on one side of VWAP and this close on the other. VWAP is backtest.indicators (resets each day, extended hours included). 9:45-15:30.",
        "- (i) Close / close[5] - 1 has absolute value > 0.001, direction of the sign, at least 10 1-minute bars since the last fire. 9:35-15:30.",
        f"- (j) diamondbot.diamonds with BOOKS['TUNED'] = {TUNED_DIAMOND}. 1-minute bars. Green -> call, red -> put.",
        "  The bot's entry window is the close time: 9:45 <= close < 14:30. Both directions. Scalp exits replace the bot's exits.",
        "  Same-bar green and red -> skip. This script never calls the bot's order functions.",
        "- (k) Unison: some bar in the last 3 bars (same day) has Fear >= 80 and some bar in that window has Greed >= 80.",
        "  Fire on the bar the condition turns true. As written: close < EMA13 -> call, close > EMA13 -> put. Flip is the opposite.",
        "  Equal to the EMA -> no trade. Tested on 1-minute and on 3-minute bars. Window 9:35-14:45.",
        "- (l) The unfiltered 95-cross on 1-minute bars, and on 3-minute bars. The 3-minute case is signal vix95_raw_3m (also item c), not a second copy.",
        "",
        "EXITS",
        "- Target 10, 15, 20, 30 percent.",
        "- Stop 10, 15, 20, 30 percent, or none.",
        "- Time stop 5, 10, 20, 30 minutes, measured from the fill minute to the bar start.",
        "- Anything still open exits on the 15:55 bar, or is counted stale if that bar has no usable print.",
        "",
        "STRIKE",
        "- Spot is the underlying open at the fill minute (a missing minute may use a close at most 5 minutes old).",
        "- atm = round(spot). 2itm call = round(spot) - 2. 2itm put = round(spot) + 2. Expiration is the session date. Symbol from backtest.lab_occ.",
        "",
        f"CONFIG COUNT {n_all} rows follow ({n_search} search + {n_all - n_search} random baseline). Columns: signal,strike,tp,sl,time_stop,role",
        "CONFIGS",
    ]
    for sig, strike, tp, sl, ts in iter_configs():
        role = "baseline" if sig == "random" else "search"
        lines.append(f"{sig},{strike},{tp:.2f},{_fmt_sl(sl)},{ts},{role}")
    lines.append("")
    return "\n".join(lines)


def assert_predeclared(path):
    expected = render_predeclared()
    if not os.path.exists(path):
        sys.exit(f"Missing {path}. Refusing to compute without the predeclared config list.")
    with open(path) as f:
        got = f.read()
    if got != expected:
        sys.exit(f"{path} does not match the grid in scalp_real.py. Refusing to compute.")


def _scrub(msg):
    text = str(msg)
    for name in ("ALPACA_KEY", "ALPACA_SECRET", "APCA_API_KEY_ID", "APCA_API_SECRET_KEY"):
        secret = os.getenv(name, "")
        if secret:
            text = text.replace(secret, "***")
    return text


_REAL_PRINT = builtins.print


def _print_scrubbed(*args, **kwargs):
    _REAL_PRINT(*(_scrub(a) for a in args), **kwargs)


def _call_scrubbed(fn):
    """Route print through the scrubber while Alpaca helpers run. They sometimes echo exception text."""
    real = builtins.print
    builtins.print = _print_scrubbed
    try:
        return fn()
    finally:
        builtins.print = real


def half_spread(price, cent_floor, pct):
    return max(float(cent_floor), float(pct) * float(price))


def stream_seed(*parts):
    raw = "|".join(str(p) for p in parts).encode()
    return int.from_bytes(hashlib.sha256(raw).digest()[:8], "little")


def norm_sf(z):
    """Two-sided standard-normal p-value."""
    if z is None or not math.isfinite(z):
        return float("nan")
    return math.erfc(abs(float(z)) / math.sqrt(2.0))


def norm_ppf(p):
    """Inverse CDF of the standard normal (Acklam)."""
    if not 0.0 < p < 1.0:
        raise ValueError("p must be in (0, 1)")
    a = (-3.969683028665376e+01, 2.209460984245205e+02, -2.759285104469687e+02,
         1.383577518672690e+02, -3.066479806614716e+01, 2.506628277459239e+00)
    b = (-5.447609879822406e+01, 1.615858368580409e+02, -1.556989798598866e+02,
         6.680131188771972e+01, -1.328068155288572e+01)
    c = (-7.784894002430293e-03, -3.223964580411365e-01, -2.400758277161838e+00,
         -2.549732539343734e+00, 4.374664141464968e+00, 2.938163982698783e+00)
    d = (7.784695709041462e-03, 3.224671290700398e-01, 2.445134137142996e+00, 3.754408661907416e+00)
    plow, phigh = 0.02425, 1 - 0.02425
    if p < plow:
        q = math.sqrt(-2 * math.log(p))
        return (((((c[0] * q + c[1]) * q + c[2]) * q + c[3]) * q + c[4]) * q + c[5]) / (
            (((d[0] * q + d[1]) * q + d[2]) * q + d[3]) * q + 1)
    if p > phigh:
        q = math.sqrt(-2 * math.log(1 - p))
        return -(((((c[0] * q + c[1]) * q + c[2]) * q + c[3]) * q + c[4]) * q + c[5]) / (
            (((d[0] * q + d[1]) * q + d[2]) * q + d[3]) * q + 1)
    q = p - 0.5
    r = q * q
    return (((((a[0] * r + a[1]) * r + a[2]) * r + a[3]) * r + a[4]) * r + a[5]) * q / (
        (((((b[0] * r + b[1]) * r + b[2]) * r + b[3]) * r + b[4]) * r + 1))


def benjamini_hochberg(pvals):
    """Return BH q-values aligned with pvals. Non-finite inputs stay NaN and are left out of N."""
    p = np.asarray(pvals, dtype=float)
    out = np.full(len(p), np.nan)
    ok = np.isfinite(p)
    if not ok.any():
        return out
    vals = p[ok]
    order = np.argsort(vals)
    ranked = vals[order]
    n = len(ranked)
    q = ranked * n / np.arange(1, n + 1)
    q = np.minimum.accumulate(q[::-1])[::-1]
    q = np.clip(q, 0, 1)
    placed = np.empty(n)
    placed[order] = q
    out[np.nonzero(ok)[0]] = placed
    return out


def breakeven_hit_rate(tp, sl, premium, cent_floor, pct, commission):
    """Hit rate that zeros the expectancy when every trade exits at the target or the stop."""
    if sl is None or premium is None or not math.isfinite(premium) or premium <= 0:
        return float("nan")
    debit = premium + half_spread(premium, cent_floor, pct)
    win_px = premium * (1.0 + tp)
    loss_px = premium * (1.0 - sl)
    credit_w = max(0.0, win_px - half_spread(win_px, cent_floor, pct))
    credit_l = max(0.0, loss_px - half_spread(loss_px, cent_floor, pct))
    net_w = (credit_w - debit) * 100.0 - 2.0 * commission
    net_l = (credit_l - debit) * 100.0 - 2.0 * commission
    denom = net_w - net_l
    if denom <= 0:
        return float("nan")
    return float(-net_l / denom)


def entry_session_minute(bar_start_minute, bar_minutes):
    """Session minute (9:30 = 0) of the first 1-minute bar after a chart bar closes.

    `bar_start_minute` is the chart bar's start. The bar covers
    [start, start + bar_minutes). Its close is the start of the next 1-minute bar.
    """
    if bar_minutes < 1:
        raise ValueError("bar_minutes must be positive")
    return int(bar_start_minute) + int(bar_minutes)


def entry_minute_from_timestamp(bar_start, bar_minutes):
    """Return (session minute, date) of the entry bar, or None if it is not a same-day RTH entry before 15:55."""
    close_ts = bar_start + pd.Timedelta(minutes=int(bar_minutes))
    if close_ts.date() != bar_start.date():
        return None
    minute = int(close_ts.hour * 60 + close_ts.minute - (9 * 60 + 30))
    if minute < 0 or minute >= FLAT_MIN:
        return None
    return minute, close_ts.date()


def _empty_opt():
    return {
        "open": np.full(N_MIN, np.nan),
        "high": np.full(N_MIN, np.nan),
        "low": np.full(N_MIN, np.nan),
        "close": np.full(N_MIN, np.nan),
        "real": np.zeros(N_MIN, dtype=bool),
        "lab": np.full(N_MIN, np.nan),
    }


def simulate_trade(opt, entry_min, cfg, costs, allow_slip=True):
    """Fill one option trade or return a skip status.

    cfg is (tp, sl or None, time_stop minutes).
    costs is (cent_floor, pct, commission) with pct as a fraction (0.005 = 0.5%).
    The walk never reads a minute before the fill.
    allow_slip=True accepts the intended minute or the next one (the 2-minute entry window)
    on this same contract. The book runner passes False and walks the two minutes itself,
    because each minute can be a different strike.
    """
    tp, sl, time_stop = cfg
    cent_floor, pct, commission = costs
    if entry_min is None or entry_min < 0 or entry_min >= FLAT_MIN:
        return {"status": "skip_entry"}
    real = opt["real"]
    span = ENTRY_LOOK if allow_slip else 1
    ent = None
    for m in range(int(entry_min), min(int(entry_min) + span, FLAT_MIN, N_MIN)):
        if real[m] and np.isfinite(opt["open"][m]) and opt["open"][m] >= MIN_PREMIUM:
            ent = m
            break
    if ent is None:
        return {"status": "skip_entry"}
    raw = float(opt["open"][ent])
    debit = raw + half_spread(raw, cent_floor, pct)
    tp_px = raw * (1.0 + tp)
    sl_px = None if sl is None else raw * (1.0 - sl)
    last = ent
    for m in range(ent, FLAT_MIN + 1):
        if real[m] and np.isfinite(opt["close"][m]):
            o = float(opt["open"][m]) if np.isfinite(opt["open"][m]) else float(opt["close"][m])
            h = float(opt["high"][m]) if np.isfinite(opt["high"][m]) else float(opt["close"][m])
            l = float(opt["low"][m]) if np.isfinite(opt["low"][m]) else float(opt["close"][m])
            c = float(opt["close"][m])
            last = m
        else:
            age = m - last
            carried = opt["lab"][m] if 0 <= m < N_MIN else np.nan
            if age > STALE_AFTER or not np.isfinite(carried):
                if (m - ent) >= time_stop or m >= FLAT_MIN:
                    return {"status": "skip_stale", "entry_min": ent}
                continue
            o = h = l = c = float(carried)
        hit_sl = sl_px is not None and l <= sl_px
        hit_tp = h >= tp_px
        if hit_sl:
            fill = min(o, sl_px)
            reason = "stop"
        elif hit_tp:
            fill = tp_px
            reason = "tp"
        elif (m - ent) >= time_stop:
            fill = c
            reason = "time"
        elif m >= FLAT_MIN:
            fill = c
            reason = "flat"
        else:
            continue
        credit = max(0.0, fill - half_spread(fill, cent_floor, pct))
        dollar = (credit - debit) * 100.0 - 2.0 * commission
        net_pct = dollar / (debit * 100.0) * 100.0
        return {
            "status": "fill",
            "entry_min": ent,
            "exit_min": m,
            "raw_entry": raw,
            "entry": debit,
            "exit": credit,
            "reason": reason,
            "net_pct": net_pct,
            "dollar": dollar,
            "hit": reason == "tp",
        }
    return {"status": "skip_stale", "entry_min": ent}


def strike_price(spot, side, mode):
    if spot is None or not math.isfinite(spot) or spot <= 0:
        return None
    k = int(np.round(float(spot)))
    if mode == "2itm":
        k = k - 2 * int(side)
    elif mode != "atm":
        raise ValueError(mode)
    return k if k > 0 else None


def spot_at(und, minute):
    """Underlying open at `minute`, else the last real close at most 5 minutes old."""
    if und is None or minute < 0 or minute >= N_MIN:
        return None
    if und["real"][minute] and np.isfinite(und["open"][minute]):
        return float(und["open"][minute])
    for back in range(1, STALE_AFTER + 1):
        j = minute - back
        if j >= 0 and und["real"][j] and np.isfinite(und["close"][j]):
            return float(und["close"][j])
    return None


def vix_skip_flags(side, color, close, vwap, atr, day_open, angle, ttm_m, ttm_m_prev, vix_now, vix_prev2):
    """The six frozen skip flags. Any one of them drops the trade. Values are the signal bar only."""
    flags = []
    if color * side == -2:
        flags.append(1)
    if atr is not None and math.isfinite(atr) and atr > 0 and math.isfinite(close) and math.isfinite(vwap):
        if side * (close - vwap) / atr <= -3:
            flags.append(2)
    if day_open is not None and math.isfinite(day_open) and math.isfinite(close):
        if side * (close - day_open) < 0:
            flags.append(3)
    if angle is not None and math.isfinite(angle) and side * angle <= -15:
        flags.append(4)
    if ttm_m is not None and ttm_m_prev is not None and math.isfinite(ttm_m) and math.isfinite(ttm_m_prev):
        mm, prev = ttm_m * side, ttm_m_prev * side
        if mm < 0 and mm > prev:
            flags.append(5)
    if vix_now is not None and vix_prev2 is not None and math.isfinite(vix_now) and math.isfinite(vix_prev2):
        chg = vix_now - vix_prev2
        if 15 <= chg < 30:
            flags.append(6)
    return flags


def _hm_window(hm, t_from, t_to):
    return (hm >= t_from) & (hm < t_to)


def _collect(index, long_m, short_m, tf, dayset):
    events = []
    hit = np.nonzero(np.asarray(long_m) | np.asarray(short_m))[0]
    for i in hit:
        if long_m[i] and short_m[i]:
            continue
        side = 1 if long_m[i] else -1
        found = entry_minute_from_timestamp(index[i], tf)
        if found is None:
            continue
        minute, day = found
        if dayset is not None and day not in dayset:
            continue
        events.append({
            "day": day,
            "side": side,
            "entry_min": minute,
            "signal_i": int(i),
            "signal_time": index[i],
        })
    return events


def _bt():
    import backtest as bt
    return bt


def chart_bundle(df):
    """Indicators used by the Vix / squeeze / line / angle signals. One pass per chart."""
    bt = _bt()
    ind = bt.indicators(df, 13, 34, True)
    color, _ef = bt.tlt_colors(df, ind)
    ang = bt.ang_series(df, ind, 5)
    fear, greed = bt.vfx_pane(df)
    ag = bt.agr_series(df, ind)
    return {
        "ind": ind,
        "color": np.asarray(color),
        "ang": np.asarray(ang, dtype=float),
        "fear": np.nan_to_num(np.asarray(fear, dtype=float)),
        "greed": np.nan_to_num(np.asarray(greed, dtype=float)),
        "m": np.asarray(ag["m"], dtype=float),
        "ema13": df["close"].ewm(span=13, adjust=False).mean().to_numpy(),
    }


def vix95_masks(bundle, filtered):
    fear, greed = bundle["fear"], bundle["greed"]
    prev_f = np.r_[np.nan, fear[:-1]]
    prev_g = np.r_[np.nan, greed[:-1]]
    long_m = (fear >= 95) & (prev_f < 95)
    short_m = (greed >= 95) & (prev_g < 95)
    if not filtered:
        return long_m, short_m
    ind = bundle["ind"]
    color, ang, m = bundle["color"], bundle["ang"], bundle["m"]
    c, vw, atr = ind["c"], ind["vwap"], ind["atr"]
    hm, day = ind["hm"], ind["day"]
    rth = (hm >= 930) & (hm < 1600)
    o930 = pd.Series(np.where(rth, ind["o"], np.nan)).groupby(pd.Series(day)).transform("first").to_numpy()
    keep_l = np.zeros(len(c), dtype=bool)
    keep_s = np.zeros(len(c), dtype=bool)
    for i in np.nonzero(long_m | short_m)[0]:
        if long_m[i] and short_m[i]:
            continue
        side = 1 if long_m[i] else -1
        prev_m = m[i - 1] if i else float("nan")
        mine = fear if side == 1 else greed
        prev2 = mine[i - 2] if i >= 2 else float("nan")
        flags = vix_skip_flags(
            side, int(color[i]), float(c[i]), float(vw[i]), float(atr[i]),
            float(o930[i]) if np.isfinite(o930[i]) else None,
            float(ang[i]), float(m[i]), float(prev_m), float(mine[i]), float(prev2),
        )
        if flags:
            continue
        if side == 1:
            keep_l[i] = True
        else:
            keep_s[i] = True
    return keep_l, keep_s


def squeeze_masks(df, bundle):
    cs, hs, ls = df["close"], df["high"], df["low"]
    basis = cs.rolling(20).mean()
    dev = 2.0 * cs.rolling(20).std(ddof=0)
    pc = cs.shift(1)
    trr = pd.concat([hs - ls, (hs - pc).abs(), (ls - pc).abs()], axis=1).max(axis=1).rolling(20).mean()
    inside = ((basis - dev) > (basis - 1.5 * trr)) & ((basis + dev) < (basis + 1.5 * trr))
    inside = inside.fillna(False).to_numpy()
    fire = np.r_[False, inside[:-1]] & ~inside
    m = bundle["m"]
    return fire & (m > 0), fire & (m < 0)


def ema_flip_masks(bundle):
    st = np.asarray(bundle["ind"]["st"])
    prev = np.r_[0, st[:-1]]
    return (st == 1) & (prev != 1), (st == -1) & (prev != -1)


def angle_flat_masks(df, bundle):
    bt = _bt()
    ind = bundle["ind"]
    idx, sd = bt.ang_events(bundle["ang"], ind["hm"], ind["day"], 23, "dn")
    n = len(df)
    long_m = np.zeros(n, dtype=bool)
    short_m = np.zeros(n, dtype=bool)
    if len(idx):
        long_m[idx[sd == 1]] = True
        short_m[idx[sd == -1]] = True
    return long_m, short_m


def unison_masks(bundle, flipped):
    fear, greed = bundle["fear"], bundle["greed"]
    day = bundle["ind"]["day"]
    f_roll = pd.Series(fear >= 80).rolling(3, min_periods=3).max().fillna(0).to_numpy() > 0
    g_roll = pd.Series(greed >= 80).rolling(3, min_periods=3).max().fillna(0).to_numpy() > 0
    d1 = np.r_[None, day[:-1]]
    d2 = np.r_[None, None, day[:-2]]
    same = (day == d1) & (day == d2)
    both = f_roll & g_roll & same
    prev = np.r_[False, both[:-1]]
    fire = both & ~prev
    close = bundle["ind"]["c"]
    ema = bundle["ema13"]
    below = close < ema
    above = close > ema
    if flipped:
        below, above = above, below
    return fire & below, fire & above


def apply_window(long_m, short_m, hm, t_from, t_to):
    win = _hm_window(hm, t_from, t_to)
    return long_m & win, short_m & win


def events_from_chart(df, bundle, kind, dayset):
    meta = {s[0]: s for s in SIGNALS}[kind]
    _id, _role, tf, window, _blurb = meta
    hm = bundle["ind"]["hm"]
    if kind == "vix95_filt_3m":
        long_m, short_m = vix95_masks(bundle, True)
    elif kind in ("vix95_raw_3m", "vix95_raw_1m"):
        long_m, short_m = vix95_masks(bundle, False)
    elif kind == "ttm_squeeze_3m":
        long_m, short_m = squeeze_masks(df, bundle)
    elif kind == "ema_vwap_flip_3m":
        long_m, short_m = ema_flip_masks(bundle)
    elif kind == "angle_flat_23_1m":
        long_m, short_m = angle_flat_masks(df, bundle)
    elif kind == "vwap_reclaim_1m":
        c, vw = bundle["ind"]["c"], bundle["ind"]["vwap"]
        day = bundle["ind"]["day"]
        same = np.r_[False, day[1:] == day[:-1]]
        prev_c = np.r_[np.nan, c[:-1]]
        prev_v = np.r_[np.nan, vw[:-1]]
        long_m = same & (prev_c < prev_v) & (c > vw)
        short_m = same & (prev_c > prev_v) & (c < vw)
    elif kind in ("vix_unison_1m", "vix_unison_3m"):
        long_m, short_m = unison_masks(bundle, False)
    elif kind in ("vix_unison_1m_flip", "vix_unison_3m_flip"):
        long_m, short_m = unison_masks(bundle, True)
    else:
        raise ValueError(kind)
    long_m, short_m = apply_window(np.asarray(long_m, bool), np.asarray(short_m, bool), hm, window[0], window[1])
    return _collect(df.index, long_m, short_m, tf, dayset)


def orb_events(und_day, day, dayset):
    """First close beyond the 9:30-9:44 high/low. `und_day` is one session of 390 minutes."""
    if dayset is not None and day not in dayset:
        return []
    high, low, close, real = und_day["high"], und_day["low"], und_day["close"], und_day["real"]
    if real[:15].sum() < 10:
        return []
    hi = np.nanmax(np.where(real[:15], high[:15], np.nan))
    lo = np.nanmin(np.where(real[:15], low[:15], np.nan))
    if not math.isfinite(hi) or not math.isfinite(lo):
        return []
    events = []
    saw_l = saw_s = False
    for i in range(15, N_MIN - 1):
        if saw_l and saw_s:
            break
        if not real[i] or not np.isfinite(close[i]):
            continue
        if not saw_l and close[i] > hi:
            events.append({"day": day, "side": 1, "entry_min": i + 1, "signal_i": i, "signal_time": None})
            saw_l = True
        if not saw_s and close[i] < lo:
            events.append({"day": day, "side": -1, "entry_min": i + 1, "signal_i": i, "signal_time": None})
            saw_s = True
    return [e for e in events if e["entry_min"] < FLAT_MIN]


def mom5_events(und_day, day, dayset):
    if dayset is not None and day not in dayset:
        return []
    close, real = und_day["close"], und_day["real"]
    events = []
    last = -10 ** 9
    for i in range(5, N_MIN - 1):
        hm = (9 * 60 + 30 + i)
        hh = (hm // 60) * 100 + (hm % 60)
        if hh < 935 or hh >= 1530:
            continue
        if not real[i] or not real[i - 5]:
            continue
        if not np.isfinite(close[i]) or not np.isfinite(close[i - 5]) or close[i - 5] <= 0:
            continue
        if i - last < 10:
            continue
        ret = close[i] / close[i - 5] - 1.0
        if abs(ret) <= 0.001:
            continue
        events.append({
            "day": day,
            "side": 1 if ret > 0 else -1,
            "entry_min": i + 1,
            "signal_i": i,
            "signal_time": None,
        })
        last = i
    return [e for e in events if e["entry_min"] < FLAT_MIN]


def diamond_events(df, dayset):
    """TUNED diamonds from diamondbot.diamonds. Entry math only — no order function is called."""
    import diamondbot
    bull, bear, _R = diamondbot.diamonds(df, diamondbot.BOOKS["TUNED"])
    close_ts = df.index + pd.Timedelta(minutes=1)
    close_hm = close_ts.hour * 100 + close_ts.minute
    win = (close_hm >= diamondbot.ENTRY_FROM) & (close_hm < diamondbot.ENTRY_TO)
    long_m = np.asarray(bull, bool) & np.asarray(win, bool)
    short_m = np.asarray(bear, bool) & np.asarray(win, bool)
    return _collect(df.index, long_m, short_m, 1, dayset)


def build_signal_events(charts, und, dayset):
    """charts[(symbol, tf)] = (df, bundle). und[symbol][day] = rth arrays. Returns signal -> list of events with symbol."""
    out = {sid: [] for sid in SEARCH_IDS}
    for sym in sorted({s for s, _tf in charts}):
        df1, b1 = charts[(sym, 1)]
        df3, b3 = charts[(sym, 3)]
        for kind, frame in (
            ("vix95_filt_3m", (df3, b3)),
            ("vix95_raw_3m", (df3, b3)),
            ("ttm_squeeze_3m", (df3, b3)),
            ("ema_vwap_flip_3m", (df3, b3)),
            ("angle_flat_23_1m", (df1, b1)),
            ("vwap_reclaim_1m", (df1, b1)),
            ("vix_unison_1m", (df1, b1)),
            ("vix_unison_1m_flip", (df1, b1)),
            ("vix_unison_3m", (df3, b3)),
            ("vix_unison_3m_flip", (df3, b3)),
            ("vix95_raw_1m", (df1, b1)),
        ):
            for ev in events_from_chart(frame[0], frame[1], kind, dayset):
                ev = dict(ev)
                ev["symbol"] = sym
                ev["signal"] = kind
                out[kind].append(ev)
        for ev in diamond_events(df1, dayset):
            ev = dict(ev)
            ev["symbol"] = sym
            ev["signal"] = "diamond_tuned_1m"
            out["diamond_tuned_1m"].append(ev)
        for day, sess in sorted(und[sym].items()):
            if dayset is not None and day not in dayset:
                continue
            for ev in orb_events(sess, day, dayset):
                ev = dict(ev)
                ev["symbol"] = sym
                ev["signal"] = "orb_1m"
                out["orb_1m"].append(ev)
            for ev in mom5_events(sess, day, dayset):
                ev = dict(ev)
                ev["symbol"] = sym
                ev["signal"] = "mom5_1m"
                out["mom5_1m"].append(ev)
    for sid in out:
        out[sid].sort(key=lambda e: (e["day"], e["symbol"], e["entry_min"], -e["side"]))
    return out


def reference_random_events(signal_events, und, symbols, days):
    """Standalone baseline book. N per day/symbol = median raw fire count of the search signals."""
    counts = {}
    for sid, evs in signal_events.items():
        per = {}
        for e in evs:
            per[(e["day"], e["symbol"])] = per.get((e["day"], e["symbol"]), 0) + 1
        for key, n in per.items():
            counts.setdefault(key, []).append(n)
    events = []
    for day in days:
        for sym in symbols:
            raw = counts.get((day, sym), [])
            # signals with zero fires that day still count in the median
            padded = list(raw) + [0] * (len(SEARCH_IDS) - len(raw))
            if not padded:
                continue
            n = int(math.floor(float(np.median(padded)) + 0.5))
            sess = und[sym].get(day)
            if sess is None or n <= 0:
                continue
            eligible = [m for m in range(5, 356) if sess["real"][m]]
            if not eligible:
                continue
            n = min(n, len(eligible))
            rng = np.random.default_rng(stream_seed("ref", day.isoformat(), sym))
            pick = rng.choice(np.asarray(eligible), size=n, replace=False)
            dirs = rng.choice(np.asarray([-1, 1]), size=n)
            for minute, side in zip(pick, dirs):
                events.append({
                    "day": day, "symbol": sym, "side": int(side), "entry_min": int(minute),
                    "signal_i": -1, "signal_time": None, "signal": "random",
                })
    events.sort(key=lambda e: (e["day"], e["symbol"], e["entry_min"], -e["side"]))
    return events


def paired_entry(attempt, und):
    """One matched control minute for an entry attempt. Returns an event dict or None."""
    day, sym, minute, side = attempt["day"], attempt["symbol"], attempt["entry_min"], attempt["side"]
    sess = und[sym].get(day)
    if sess is None:
        return None
    eligible = [m for m in range(5, 356) if sess["real"][m] and m != minute]
    bucket = [m for m in eligible if m // 30 == minute // 30]
    pool = bucket or eligible
    if not pool:
        return None
    rng = np.random.default_rng(stream_seed(
        "paired", attempt["signal"], attempt["strike"], day.isoformat(), sym, int(minute), int(side),
    ))
    chosen = int(rng.choice(np.asarray(pool)))
    return {
        "day": day, "symbol": sym, "side": int(side), "entry_min": chosen,
        "signal": attempt["signal"], "strike": attempt["strike"],
        "attempt_id": attempt["attempt_id"],
    }


class _CacheClient:
    """Repeat identical option-bar requests without a second download. lab_fetch_opt and the OHLC pass share this."""

    def __init__(self, inner):
        self.inner = inner
        self.cache = {}
        self.calls = 0

    def get_option_bars(self, req):
        syms = req.symbol_or_symbols
        syms = (syms,) if isinstance(syms, str) else tuple(syms)
        key = (syms, repr(req.start), repr(req.end), repr(getattr(req, "timeframe", "")))
        if key not in self.cache:
            self.calls += 1
            self.cache[key] = self.inner.get_option_bars(req)
        return self.cache[key]


def _rows_from_frame(df):
    """Yield (symbol, tz-aware NY index, frame) groups from an Alpaca option-bar frame."""
    if df is None or not len(df) or not isinstance(df.index, pd.MultiIndex):
        return
    for sym, g in df.groupby(level=0):
        g = g.droplevel(0)
        ix = g.index
        if getattr(ix, "tz", None) is None:
            continue
        yield sym, ix.tz_convert(NY), g


def _stamp_minutes(ix):
    mm = (ix.hour * 60 + ix.minute - (9 * 60 + 30)).to_numpy()
    ok = (mm >= 0) & (mm < N_MIN)
    return mm, ok


def fetch_option_day(oc, contracts, day):
    """OHLC, real-print mask, and lab_fetch_opt closes for one session.

    The close series used for a carried exit is the array lab_fetch_opt returns
    (forward-filled at most 5 minutes). Opens come from the same bars.
    """
    bt = _bt()
    from alpaca.data.requests import OptionBarsRequest
    from alpaca.data.timeframe import TimeFrame

    contracts = sorted(set(contracts))
    start = pd.Timestamp(day, tz=NY) + pd.Timedelta(hours=9, minutes=30)
    end = start + pd.Timedelta(minutes=N_MIN)
    start_utc = start.tz_convert("UTC").to_pydatetime()
    end_utc = end.tz_convert("UTC").to_pydatetime()
    raw = {}

    def pull():
        for k0 in range(0, len(contracts), 60):
            chunk = contracts[k0:k0 + 60]
            df = None
            for attempt in range(4):
                try:
                    df = oc.get_option_bars(OptionBarsRequest(
                        symbol_or_symbols=chunk, timeframe=TimeFrame.Minute,
                        start=start_utc, end=end_utc,
                    )).df
                    break
                except Exception as e:  # noqa: BLE001
                    _print_scrubbed(f"  option bars {day} failed ({attempt + 1}/4): {_scrub(e)[:200]}")
                    time.sleep(5 * (attempt + 1))
            if df is None or not len(df):
                continue
            for sym, ix, g in _rows_from_frame(df):
                mm, ok = _stamp_minutes(ix)
                rec = raw.get(sym) or _empty_opt()
                for col in ("open", "high", "low", "close"):
                    if col not in g.columns:
                        continue
                    rec[col][mm[ok]] = g[col].to_numpy()[ok]
                rec["real"][mm[ok]] = np.isfinite(rec["open"][mm[ok]]) & (rec["open"][mm[ok]] > 0)
                raw[sym] = rec
        lab = bt.lab_fetch_opt(oc, contracts, day)
        for sym, closes in lab.items():
            rec = raw.get(sym) or _empty_opt()
            rec["lab"] = np.asarray(closes, dtype=float)
            raw[sym] = rec
        for rec in raw.values():
            if rec["lab"] is None or len(rec["lab"]) != N_MIN:
                rec["lab"] = np.full(N_MIN, np.nan)
        return raw

    return _call_scrubbed(pull)


def rth_session(df1):
    hm = df1.index.hour * 100 + df1.index.minute
    rth = df1[(hm >= 930) & (hm < 1600)]
    out = {}
    for day, g in rth.groupby(rth.index.date):
        rec = {k: np.full(N_MIN, np.nan) for k in ("open", "high", "low", "close")}
        mm = (g.index.hour * 60 + g.index.minute - (9 * 60 + 30)).to_numpy()
        ok = (mm >= 0) & (mm < N_MIN)
        for col in rec:
            rec[col][mm[ok]] = g[col].to_numpy()[ok]
        rec["real"] = np.isfinite(rec["open"])
        out[day] = rec
    return out


def complete_days(und, symbols, now=None):
    now = now or datetime.now(NY)
    sets = []
    for sym in symbols:
        good = set()
        for day, sess in und[sym].items():
            if int(sess["real"].sum()) >= 180:
                good.add(day)
        sets.append(good)
    if not sets:
        return []
    days = sorted(set.intersection(*sets)) if len(sets) > 1 else sorted(sets[0])
    if now.hour < 16:
        days = [d for d in days if d < now.date()]
    else:
        days = [d for d in days if d <= now.date()]
    return days


def run_book(events, opt, und, strike, cfg, costs, signal):
    """One position per symbol. Returns fills, attempts (including skips), and skip counts."""
    busy = {}
    trades = []
    attempts = []
    skips = {"skip_entry": 0, "skip_stale": 0, "skip_spot": 0}
    seq = 0
    bt = _bt()
    ordered = sorted(events, key=lambda e: (e["day"], e["symbol"], e["entry_min"], -e["side"]))
    for ev in ordered:
        key = (ev["day"], ev["symbol"])
        if ev["entry_min"] <= busy.get(key, -1):
            continue
        seq += 1
        attempt_id = f"{signal}|{strike}|{ev['day']}|{ev['symbol']}|{ev['entry_min']}|{ev['side']}|{seq}"
        attempt = {
            "attempt_id": attempt_id,
            "day": ev["day"],
            "symbol": ev["symbol"],
            "side": ev["side"],
            "entry_min": ev["entry_min"],
            "signal": signal,
            "strike": strike,
            "status": None,
        }
        # Spot and contract are fixed once the fill minute is known. Try the intended minute
        # and the next one, matching the entry search, and keep the first real option open.
        filled = None
        saw_contract = False
        spot_ok = False
        for m in range(ev["entry_min"], min(ev["entry_min"] + ENTRY_LOOK, FLAT_MIN)):
            spot = spot_at(und[ev["symbol"]].get(ev["day"]), m)
            if spot is None:
                continue
            spot_ok = True
            k = strike_price(spot, ev["side"], strike)
            if k is None:
                continue
            contract = bt.lab_occ(ev["symbol"], ev["day"], "C" if ev["side"] == 1 else "P", k)
            book = opt.get((ev["day"], contract))
            if book is None:
                continue
            saw_contract = True
            trial = simulate_trade(book, m, cfg, costs, allow_slip=False)
            if trial["status"] == "fill":
                filled = trial
                filled["contract"] = contract
                filled["spot"] = spot
                break
            if trial["status"] == "skip_stale":
                # A real entry print existed but the exit could not be priced.
                filled = trial
                filled["contract"] = contract
                break
        if not spot_ok:
            attempt["status"] = "skip_spot"
            skips["skip_spot"] += 1
            attempts.append(attempt)
            continue
        if filled is None:
            attempt["status"] = "skip_entry" if not saw_contract else "skip_entry"
            skips["skip_entry"] += 1
            attempts.append(attempt)
            continue
        if filled["status"] != "fill":
            attempt["status"] = filled["status"]
            skips[filled["status"]] = skips.get(filled["status"], 0) + 1
            attempts.append(attempt)
            continue
        attempt["status"] = "fill"
        attempts.append(attempt)
        busy[key] = filled["exit_min"]
        hh, mm = divmod((9 * 60 + 30) + filled["entry_min"], 60)
        trades.append({
            "attempt_id": attempt_id,
            "day": ev["day"],
            "time": f"{hh:02d}:{mm:02d}",
            "symbol": ev["symbol"],
            "side": "CALL" if ev["side"] == 1 else "PUT",
            "side_n": ev["side"],
            "entry": filled["entry"],
            "exit": filled["exit"],
            "reason": filled["reason"],
            "net_pct": filled["net_pct"],
            "dollar": filled["dollar"],
            "hit": filled["hit"],
            "contract": filled["contract"],
            "entry_min": filled["entry_min"],
            "exit_min": filled["exit_min"],
            "raw_entry": filled["raw_entry"],
            "signal": signal,
            "strike": strike,
        })
    return trades, attempts, skips


def simulate_controls(controls, opt, und, cfg, costs, strike):
    """Price paired controls independently (no second one-position rule)."""
    bt = _bt()
    trades = []
    for ev in controls:
        if ev is None:
            continue
        spot = None
        contract = None
        book = None
        for m in range(ev["entry_min"], min(ev["entry_min"] + ENTRY_LOOK, FLAT_MIN)):
            spot = spot_at(und[ev["symbol"]].get(ev["day"]), m)
            if spot is None:
                continue
            k = strike_price(spot, ev["side"], strike)
            if k is None:
                continue
            contract = bt.lab_occ(ev["symbol"], ev["day"], "C" if ev["side"] == 1 else "P", k)
            book = opt.get((ev["day"], contract))
            if book is None:
                continue
            trial = simulate_trade(book, m, cfg, costs, allow_slip=False)
            if trial["status"] == "fill":
                hh, mm = divmod((9 * 60 + 30) + trial["entry_min"], 60)
                trades.append({
                    "attempt_id": ev["attempt_id"],
                    "day": ev["day"],
                    "time": f"{hh:02d}:{mm:02d}",
                    "symbol": ev["symbol"],
                    "side": "CALL" if ev["side"] == 1 else "PUT",
                    "entry": trial["entry"],
                    "exit": trial["exit"],
                    "reason": trial["reason"],
                    "net_pct": trial["net_pct"],
                    "dollar": trial["dollar"],
                    "hit": trial["hit"],
                    "contract": contract,
                    "raw_entry": trial["raw_entry"],
                })
                break
    return trades


def contracts_for_events(events, und, strikes):
    """Contracts the entry search might touch: intended minute and the next minute, each requested strike."""
    bt = _bt()
    needed = {}
    for ev in events:
        sess = und[ev["symbol"]].get(ev["day"])
        if sess is None:
            continue
        for m in range(ev["entry_min"], min(ev["entry_min"] + ENTRY_LOOK, FLAT_MIN)):
            spot = spot_at(sess, m)
            if spot is None:
                continue
            for mode in strikes:
                k = strike_price(spot, ev["side"], mode)
                if k is None:
                    continue
                cp = "C" if ev["side"] == 1 else "P"
                needed.setdefault(ev["day"], set()).add(bt.lab_occ(ev["symbol"], ev["day"], cp, k))
    return needed


def _day_sums(values, day_ids, n_days):
    sums = np.zeros(n_days)
    cnts = np.zeros(n_days)
    if len(values):
        sums = np.bincount(day_ids, weights=np.asarray(values, float), minlength=n_days).astype(float)
        cnts = np.bincount(day_ids, minlength=n_days).astype(float)
    return sums, cnts


def clustered_t(values, day_ids, n_days):
    values = np.asarray(values, dtype=float)
    if len(values) < 2:
        return float("nan"), float("nan")
    mu = float(values.mean())
    sums, cnts = _day_sums(values, day_ids, n_days)
    # One day cannot support a day-clustered error. Identical values make the error exactly 0.
    if int((cnts > 0).sum()) < 2:
        return float("nan"), float("nan")
    resid = sums - cnts * mu
    se = math.sqrt(float((resid ** 2).sum())) / len(values)
    if not math.isfinite(se) or se <= 1e-9 * max(1.0, abs(mu)):
        return float("nan"), float("nan")
    t = mu / se
    return t, norm_sf(t)


def bootstrap_mean(sums, cnts, n_boot, seed):
    n_days = len(sums)
    if n_days == 0 or cnts.sum() < 1 or n_boot <= 0:
        return float("nan"), float("nan")
    rng = np.random.default_rng(seed)
    pick = rng.integers(0, n_days, size=(n_boot, n_days))
    s = sums[pick].sum(1)
    c = cnts[pick].sum(1)
    with np.errstate(divide="ignore", invalid="ignore"):
        means = np.where(c > 0, s / c, np.nan)
    if not np.isfinite(means).any():
        return float("nan"), float("nan")
    lo, hi = np.nanquantile(means, [0.025, 0.975])
    return float(lo), float(hi)


def summarize(trades, days, n_boot, seed):
    idx = {d: i for i, d in enumerate(days)}
    kept = [t for t in trades if t["day"] in idx]
    n_days = len(days)
    daily = np.zeros(n_days)
    for t in kept:
        daily[idx[t["day"]]] += t["dollar"]
    cum = np.cumsum(daily)
    peak = np.maximum.accumulate(cum) if n_days else cum
    max_dd = float((peak - cum).max()) if n_days else 0.0
    vals = np.array([t["net_pct"] for t in kept], dtype=float)
    dids = np.array([idx[t["day"]] for t in kept], dtype=int) if kept else np.zeros(0, dtype=int)
    tstat, p = clustered_t(vals, dids, n_days)
    sums, cnts = _day_sums(vals, dids, n_days)
    # dollar drawdown uses every day; the bootstrap of the mean uses the same day axis
    # (empty days add nothing to the per-trade mean).
    lo, hi = bootstrap_mean(sums, cnts, n_boot, seed)
    hits = np.array([1.0 if t["hit"] else 0.0 for t in kept], dtype=float)
    return {
        "n": len(kept),
        "trades_per_day": len(kept) / n_days if n_days else float("nan"),
        "hit_rate": float(hits.mean()) if len(hits) else float("nan"),
        "mean_net_pct": float(vals.mean()) if len(vals) else float("nan"),
        "usd_per_day": float(daily.mean()) if n_days else float("nan"),
        "max_drawdown_usd": max_dd,
        "t": tstat,
        "p": p,
        "boot_lo": lo,
        "boot_hi": hi,
        "median_raw": float(np.median([t["raw_entry"] for t in kept])) if kept else float("nan"),
        "sums": sums,
        "cnts": cnts,
    }


def paired_summary(sig_trades, rnd_trades, days, n_boot, seed):
    idx = {d: i for i, d in enumerate(days)}
    rnd = {t["attempt_id"]: t for t in rnd_trades if t["day"] in idx}
    diffs = []
    dids = []
    both = 0
    for t in sig_trades:
        if t["day"] not in idx:
            continue
        other = rnd.get(t["attempt_id"])
        if other is None:
            continue
        both += 1
        diffs.append(t["net_pct"] - other["net_pct"])
        dids.append(idx[t["day"]])
    vals = np.asarray(diffs, dtype=float)
    dids = np.asarray(dids, dtype=int) if dids else np.zeros(0, dtype=int)
    tstat, p = clustered_t(vals, dids, len(days))
    sums, cnts = _day_sums(vals, dids, len(days))
    lo, hi = bootstrap_mean(sums, cnts, n_boot, seed + 17)
    return {"n_paired": both, "t_diff": tstat, "p_diff": p, "boot_diff_lo": lo, "boot_diff_hi": hi,
            "mean_diff": float(vals.mean()) if len(vals) else float("nan")}


def select_top(rows, k=TOP_K):
    """In-sample rows only. Highest paired-difference t, then mean net %, then n."""
    eligible = []
    for r in rows:
        if r["n"] < MIN_TRADES or r["n_paired"] < MIN_TRADES:
            continue
        if not math.isfinite(r["t_diff"]):
            continue
        eligible.append(r)
    eligible.sort(key=lambda r: (r["t_diff"], r["mean_net_pct"] if math.isfinite(r["mean_net_pct"]) else -1e9, r["n"]),
                  reverse=True)
    return eligible[:k]


def _fmt(x, nd=2):
    if x is None or not isinstance(x, (int, float)) or not math.isfinite(x):
        return ""
    return f"{x:.{nd}f}"


def _hit(rate):
    if rate is None or not isinstance(rate, float) or not math.isfinite(rate):
        return ""
    return f"{rate * 100:.1f}%"


def _row_out(**kwargs):
    row = {k: "" for k in RESULT_FIELDS}
    for k, v in kwargs.items():
        if k not in row:
            continue
        if isinstance(v, float):
            row[k] = "" if not math.isfinite(v) else f"{v:.6f}"
        elif v is None:
            row[k] = ""
        else:
            row[k] = v
    return row


def render_report(meta, rows, tops):
    lines = []
    lines.append(f"# 0DTE scalp on real option prints ({meta['stamp']})")
    lines.append("")
    lines.append("**Research tool, not trading advice.** Data only: historical Alpaca bars, no orders.")
    if meta.get("synthetic"):
        lines.append("")
        lines.append("**SYNTHETIC RUN.** Prices are a stand-in path, not OPRA. Do not read these numbers as a backtest.")
    lines.append("")
    lines.append("## What was measured")
    lines.append("")
    lines.append(meta["coverage"])
    lines.append("")
    lines.append(
        f"Costs: extra half-spread max({meta['cent_floor'] * 100:.1f} cents, {meta['pct'] * 100:.2f}% of premium) per side, "
        f"commission ${meta['commission']:.2f} per contract per side, 1 contract. "
        f"Entry is the next real option open after the signal bar closes (or the minute after, if that one is the first print). "
        f"Exits do not use a print more than 5 minutes old. Flat at 15:55."
    )
    lines.append("")
    lines.append(
        f"Split: {meta['n_is']} in-sample day{'s' if meta['n_is'] != 1 else ''} ({meta['is_first']} to {meta['is_last']}), "
        f"{meta['n_oos']} held-out day{'s' if meta['n_oos'] != 1 else ''} ({meta['oos_first']} to {meta['oos_last']}). "
        f"The holdout section is the only place those days are scored, and only for the top {TOP_K} in-sample configs of each signal."
    )
    lines.append("")
    lines.append(
        f"Search family N = {meta['n_family']} (the full predeclared grid; a run that asks for one strike still uses this N). "
        f"Two-sided Bonferroni bar is p < {0.05 / meta['n_family']:.6g} "
        f"(|t| > {meta['t_crit']:.2f} under a normal reference). "
        f"FDR is Benjamini-Hochberg on the finite in-sample paired-difference p-values from this run. "
        f"The random book is the control and is not part of N."
    )
    lines.append("")
    lines.append("## Break-even hit rate")
    lines.append("")
    lines.append(
        "If a trade could only exit at the target or the stop, the hit rate that zeros expectancy is "
        "p = -net_loss / (net_win - net_loss), after the half-spread and the commission. "
        "The table uses a $2.00 premium so the grid is comparable. Each results-csv row also has the rate at that config's own median entry open. "
        "A time stop makes the true break-even higher than this, because many trades exit before the target."
    )
    lines.append("")
    lines.append("| Target | Stop | Break-even hit rate at $2 |")
    lines.append("|---|---|---|")
    for tp in TPS:
        for sl in SLS:
            p = breakeven_hit_rate(tp, sl, 2.0, meta["cent_floor"], meta["pct"], meta["commission"])
            sl_txt = "none" if sl is None else f"{sl * 100:.0f}%"
            p_txt = "not defined" if not math.isfinite(p) else f"{p * 100:.1f}%"
            lines.append(f"| {tp * 100:.0f}% | {sl_txt} | {p_txt} |")
    lines.append("")
    lines.append("## In-sample, best configs by the paired-difference t")
    lines.append("")
    lines.append(
        "Full grid: `results/scalp_real_results.csv` (hit_rate and breakeven_hit_rate are fractions, net_pct is in percent). "
        "Trades for the top configs and the random baseline: `results/scalp_real_trades.csv`."
    )
    lines.append("")
    for sid in SEARCH_IDS:
        mine = [r for r in rows if r["signal"] == sid and r["split"] == "in_sample"]
        lines.append(f"### {sid}")
        lines.append("")
        lines.append(SIGNAL_BLURB[sid])
        lines.append("")
        if not mine:
            lines.append("No configs were run.")
            lines.append("")
            continue
        finite = [r for r in mine if math.isfinite(r["t_diff"])]
        finite.sort(key=lambda r: r["t_diff"], reverse=True)
        show = finite[:8]
        if not show:
            lines.append("No in-sample config produced a paired-difference t. That needs trades on at least two days.")
            lines.append("")
            continue
        lines.append("| Strike | TP | SL | Time | Trades | /day | Hit | Net % | $/day | Max DD $ | t | vs random net % | t diff | 95% CI | skips entry/stale |")
        lines.append("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
        for r in show:
            ci = f"[{_fmt(r['boot_lo'])}, {_fmt(r['boot_hi'])}]" if math.isfinite(r["boot_lo"]) else ""
            lines.append(
                f"| {r['strike']} | {r['tp'] * 100:.0f}% | {_fmt_sl(r['sl'])} | {r['time_stop']}m | {r['n']} | "
                f"{_fmt(r['trades_per_day'])} | {_hit(r['hit_rate'])} | "
                f"{_fmt(r['mean_net_pct'])} | {_fmt(r['usd_per_day'])} | {_fmt(r['max_drawdown_usd'])} | {_fmt(r['t'])} | "
                f"{_fmt(r['random_mean_net_pct'])} | {_fmt(r['t_diff'])} | {ci} | {r['n_skip_entry']}/{r['n_skip_stale']} |"
            )
        lines.append("")
    lines.append("## Reference random book, in sample")
    lines.append("")
    lines.append(SIGNAL_BLURB["random"])
    lines.append("")
    refs = [r for r in rows if r["signal"] == "random" and r["split"] == "in_sample" and math.isfinite(r["mean_net_pct"])]
    refs.sort(key=lambda r: r["mean_net_pct"], reverse=True)
    if not refs:
        lines.append("The reference book produced no fills.")
    else:
        lines.append("| Strike | TP | SL | Time | Trades | /day | Hit | Net % | $/day | Max DD $ | t | 95% CI |")
        lines.append("|---|---|---|---|---|---|---|---|---|---|---|---|")
        for r in refs[:8]:
            ci = f"[{_fmt(r['boot_lo'])}, {_fmt(r['boot_hi'])}]"
            lines.append(
                f"| {r['strike']} | {r['tp'] * 100:.0f}% | {_fmt_sl(r['sl'])} | {r['time_stop']}m | {r['n']} | "
                f"{_fmt(r['trades_per_day'])} | {_hit(r['hit_rate'])} | "
                f"{_fmt(r['mean_net_pct'])} | {_fmt(r['usd_per_day'])} | {_fmt(r['max_drawdown_usd'])} | {_fmt(r['t'])} | {ci} |"
            )
    lines.append("")
    lines.append("## Holdout, one look")
    lines.append("")
    lines.append(
        f"Chosen on the in-sample paired-difference t (at least {MIN_TRADES} fills on each side). "
        "These rows were not used to pick the configs."
    )
    lines.append("")
    lines.append("| Signal | Strike | TP | SL | Time | IS t diff | OOS trades | OOS hit | OOS net % | OOS $/day | OOS max DD $ | OOS t | OOS vs random | OOS t diff | OOS 95% CI |")
    lines.append("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    if not tops:
        lines.append("| — | | | | | | | | | | | | | | |")
    for rec in tops:
        ins, oos = rec["is"], rec["oos"]
        ci = f"[{_fmt(oos['boot_lo'])}, {_fmt(oos['boot_hi'])}]" if oos and math.isfinite(oos["boot_lo"]) else ""
        lines.append(
            f"| {ins['signal']} | {ins['strike']} | {ins['tp'] * 100:.0f}% | {_fmt_sl(ins['sl'])} | {ins['time_stop']}m | "
            f"{_fmt(ins['t_diff'])} | {oos['n'] if oos else 0} | "
            f"{_hit(oos['hit_rate']) if oos else ''} | "
            f"{_fmt(oos['mean_net_pct']) if oos else ''} | {_fmt(oos['usd_per_day']) if oos else ''} | "
            f"{_fmt(oos['max_drawdown_usd']) if oos else ''} | {_fmt(oos['t']) if oos else ''} | "
            f"{_fmt(oos['random_mean_net_pct']) if oos else ''} | {_fmt(oos['t_diff']) if oos else ''} | {ci} |"
        )
    lines.append("")
    lines.append("## How to read a pass")
    lines.append("")
    lines.append(
        "A config is interesting only if the in-sample paired difference beats the Bonferroni or FDR bar **and** the holdout "
        "mean is still positive against its own random book. Anything short of that is a description of this sample, not an edge. "
        "0DTE spreads are often wider than the half-spread assumed here; when they are, the break-even hit rate moves up."
    )
    lines.append("")
    lines.append(f"Skipped entries with no print within 2 minutes, and exits skipped as stale, are columns in the csv. {meta['skip_note']}")
    lines.append("")
    return "\n".join(lines)


def _filter_days(events, live):
    return [e for e in events if e["day"] in live]


def _write_csv(path, fields, rows):
    tmp = path + ".tmp"
    with open(tmp, "w", newline="") as f:
        w = __import__("csv").DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        for row in rows:
            w.writerow(row)
    os.replace(tmp, path)


def _write_text(path, text):
    tmp = path + ".tmp"
    with open(tmp, "w") as f:
        f.write(text)
    os.replace(tmp, path)


def _env_float(name, default):
    raw = os.getenv(name, "").strip()
    return float(raw) if raw else default


def _env_int(name, default):
    raw = os.getenv(name, "").strip()
    return int(raw) if raw else default


def _parse_strikes(raw):
    parts = [p.strip().lower() for p in raw.split(",") if p.strip()]
    bad = [p for p in parts if p not in STRIKE_MODES]
    if bad or not parts:
        sys.exit(f"SCALP_STRIKES must be a subset of {', '.join(STRIKE_MODES)}")
    # keep the predeclared order
    return tuple(s for s in STRIKE_MODES if s in parts)


def _load_underlying(symbols, start, end, synthetic):
    bt = _bt()
    frames = {}
    if synthetic:
        for sym in symbols:
            df, feed = bt.fake_1m(sym, start, end)
            frames[sym] = df
            _print_scrubbed(f"  {sym}: synthetic {feed} {len(df):,} bars")
        return frames
    for sym in symbols:
        df, feed = bt.fetch_1m(sym, start, end)
        frames[sym] = df
        _print_scrubbed(f"  {sym}: {feed} {len(df):,} bars")
    return frames


def _synth_option(contract, day, und, sym):
    """Deterministic stand-in so the pipeline can be exercised without keys. Not a market."""
    sess = und[sym][day]
    spot = pd.Series(sess["close"]).ffill().bfill().to_numpy()
    # contract is SYM yymmdd C/P strike*1000
    cp = contract[len(sym) + 6]
    k = int(contract[len(sym) + 7:]) / 1000.0
    mins = np.arange(N_MIN)
    left = np.maximum(N_MIN - mins, 1) / N_MIN
    intrinsic = np.maximum(spot - k, 0) if cp == "C" else np.maximum(k - spot, 0)
    prem = intrinsic + 0.35 * np.sqrt(left)
    rec = _empty_opt()
    rec["open"] = prem
    rec["high"] = prem * 1.02
    rec["low"] = prem * 0.98
    rec["close"] = prem
    rec["real"] = np.isfinite(prem)
    # punch a hole so stale-exit handling has something to do on minute 100-110
    rec["real"][100:112] = False
    for col in ("open", "high", "low", "close"):
        rec[col][100:112] = np.nan
    rec["lab"] = pd.Series(rec["close"]).ffill(limit=STALE_AFTER).to_numpy()
    return rec


def _fetch_all(oc, needed, und, synthetic, symbols):
    opt = {}
    for i, day in enumerate(sorted(needed)):
        contracts = sorted(needed[day])
        if synthetic:
            got = {}
            for c in contracts:
                sym = next(s for s in symbols if c.startswith(s))
                got[c] = _synth_option(c, day, und, sym)
        else:
            got = fetch_option_day(oc, contracts, day)
        n_real = 0
        for c, rec in got.items():
            opt[(day, c)] = rec
            if rec["real"].any():
                n_real += 1
        _print_scrubbed(f"  options {day} {i + 1}/{len(needed)} contracts {len(contracts)} with a print {n_real}")
    return opt


def _live_days(days, opt):
    live = []
    for day in days:
        ok = False
        for (d, _c), rec in opt.items():
            if d == day and rec["real"].any():
                ok = True
                break
        if ok:
            live.append(day)
    return live


def _split(days):
    if not days:
        return [], []
    n_oos = max(1, int(round(len(days) * HOLD_FRAC)))
    if n_oos >= len(days):
        n_oos = len(days) - 1 if len(days) > 1 else 1
    if len(days) == 1:
        return days, []
    return days[:-n_oos], days[-n_oos:]


def _config_seed(signal, strike, tp, sl, ts, part):
    return stream_seed("boot", part, signal, strike, f"{tp:.2f}", _fmt_sl(sl), ts) % (2 ** 32)


def _skips_for(attempts, days):
    want = set(days)
    att = [a for a in attempts if a["day"] in want]
    return {
        "attempts": len(att),
        "skip_entry": sum(1 for a in att if a["status"] == "skip_entry"),
        "skip_stale": sum(1 for a in att if a["status"] == "skip_stale"),
        "skip_spot": sum(1 for a in att if a["status"] == "skip_spot"),
    }


def _merge_stats(base, extra):
    out = dict(base)
    out.update(extra)
    return out


def _make_row(signal, strike, tp, sl, ts, split, role, stats, skips, n_days, costs, selected):
    be = breakeven_hit_rate(tp, sl, stats.get("median_raw"), costs[0], costs[1], costs[2])
    return {
        "signal": signal, "strike": strike, "tp": tp, "sl": sl, "time_stop": ts, "split": split, "role": role,
        "n": stats["n"], "n_attempts": skips.get("attempts", 0),
        "trades_per_day": stats["trades_per_day"], "hit_rate": stats["hit_rate"],
        "mean_net_pct": stats["mean_net_pct"], "usd_per_day": stats["usd_per_day"],
        "max_drawdown_usd": stats["max_drawdown_usd"], "t": stats["t"], "p": stats["p"],
        "t_diff": stats.get("t_diff", float("nan")), "p_diff": stats.get("p_diff", float("nan")),
        "boot_lo": stats["boot_lo"], "boot_hi": stats["boot_hi"],
        "boot_diff_lo": stats.get("boot_diff_lo", float("nan")),
        "boot_diff_hi": stats.get("boot_diff_hi", float("nan")),
        "random_n": stats.get("random_n", 0),
        "random_hit_rate": stats.get("random_hit_rate", float("nan")),
        "random_mean_net_pct": stats.get("random_mean_net_pct", float("nan")),
        "random_t": stats.get("random_t", float("nan")),
        "n_skip_entry": skips.get("skip_entry", 0),
        "n_skip_stale": skips.get("skip_stale", 0),
        "n_skip_spot": skips.get("skip_spot", 0),
        "n_days": n_days,
        "breakeven_hit_rate": be,
        "q_fdr": float("nan"),
        "bonferroni_05": 0,
        "beats_random": "",
        "selected_top3": 1 if selected else 0,
        "n_paired": stats.get("n_paired", 0),
    }


def _trade_rows(trades, signal, strike, tp, sl, ts, split_of, book):
    rows = []
    for t in trades:
        rows.append({
            "date": t["day"].isoformat(),
            "time": t["time"],
            "symbol": t["symbol"],
            "side": t["side"],
            "entry": f"{t['entry']:.4f}",
            "exit": f"{t['exit']:.4f}",
            "reason": t["reason"],
            "net_pct": f"{t['net_pct']:.4f}",
            "signal": signal,
            "strike": strike,
            "tp": f"{tp:.2f}",
            "sl": _fmt_sl(sl),
            "time_stop": ts,
            "split": split_of(t["day"]),
            "book": book,
            "contract": t.get("contract", ""),
            "dollar": f"{t['dollar']:.4f}",
        })
    return rows


def main():
    out_dir = os.getenv("SCALP_OUT", "results").strip() or "results"
    os.makedirs(out_dir, exist_ok=True)
    pre_path = os.path.join("results", "SCALP_REAL_PREDECLARED.txt")
    assert_predeclared(pre_path)

    days_n = _env_int("SCALP_DAYS", 60)
    if days_n < 1:
        sys.exit("SCALP_DAYS must be >= 1")
    symbols = [s.strip().upper() for s in os.getenv("SCALP_SYMBOLS", "SPY,QQQ").split(",") if s.strip()]
    strikes = _parse_strikes(os.getenv("SCALP_STRIKES", "2itm,atm"))
    cent_floor = _env_float("SCALP_HALF_SPREAD_CENTS", 1.0) / 100.0
    pct = _env_float("SCALP_HALF_SPREAD_PCT", 0.5) / 100.0
    commission = _env_float("SCALP_COMMISSION", 0.65)
    n_boot = _env_int("SCALP_BOOT", BOOT_DEFAULT)
    synthetic = os.getenv("SCALP_SYNTH", "") == "1"
    costs = (cent_floor, pct, commission)
    t0 = time.time()

    now = datetime.now(NY)
    end = datetime.now(timezone.utc) - timedelta(minutes=20)
    start = (pd.Timestamp(now.date(), tz=NY) - pd.Timedelta(days=int(days_n * 3 + 70))).tz_convert("UTC").to_pydatetime()
    _print_scrubbed(f"underlying {', '.join(symbols)} from {start:%Y-%m-%d}  synthetic={synthetic}")
    frames = _load_underlying(symbols, start, end, synthetic)
    und = {sym: rth_session(df) for sym, df in frames.items()}
    all_days = complete_days(und, symbols, now)
    if not all_days:
        sys.exit("No completed sessions in the underlying data.")
    candidate = all_days[-days_n:]
    _print_scrubbed(f"completed sessions {len(all_days)}, using {len(candidate)} ({candidate[0]} .. {candidate[-1]})")

    bt = _bt()
    charts = {}
    dayset = set(candidate)
    for sym, df1 in frames.items():
        df_rth_ext = bt.to_tf(df1, rth_only=False, mins=1)
        df3 = bt.to_tf(df1, rth_only=False, mins=3)
        charts[(sym, 1)] = (df_rth_ext, chart_bundle(df_rth_ext))
        charts[(sym, 3)] = (df3, chart_bundle(df3))
        _print_scrubbed(f"  {sym} charts 1m {len(df_rth_ext):,}  3m {len(df3):,}")

    signal_events = build_signal_events(charts, und, dayset)
    for sid in SEARCH_IDS:
        _print_scrubbed(f"  fires {sid} {len(signal_events[sid])}")
    ref_events = reference_random_events(signal_events, und, symbols, candidate)

    needed = contracts_for_events([e for evs in signal_events.values() for e in evs] + ref_events, und, strikes)
    oc = None
    if not synthetic:
        key, sec = os.getenv("ALPACA_KEY", "").strip(), os.getenv("ALPACA_SECRET", "").strip()
        if not key or not sec:
            sys.exit("ALPACA_KEY / ALPACA_SECRET are missing. Add them in Settings > Secrets and variables > Actions.")
        from alpaca.data.historical import OptionHistoricalDataClient
        oc = _CacheClient(OptionHistoricalDataClient(key, sec))
    opt = _fetch_all(oc, needed, und, synthetic, symbols)
    live = _live_days(candidate, opt)
    dropped = [d for d in candidate if d not in set(live)]
    _print_scrubbed(f"OPRA days {len(live)} of {len(candidate)} requested; dropped {len(dropped)} with no prints")
    if not live:
        text = (
            "# 0DTE scalp on real option prints\n\n"
            "No OPRA 1-minute bars came back for the requested contracts. Nothing was scored.\n"
            "Data only. Research tool, not trading advice.\n"
        )
        _write_text(os.path.join(out_dir, "SCALP_REAL.md"), text)
        sys.exit("No OPRA 1-minute bars for the requested days.")

    live_set = set(live)
    signal_events = {sid: _filter_days(evs, live_set) for sid, evs in signal_events.items()}
    ref_events = reference_random_events(signal_events, und, symbols, live)
    is_days, oos_days = _split(live)
    is_set, oos_set = set(is_days), set(oos_days)

    # Pass 1 already fetched signal + reference contracts on the original candidate set.
    # Reference events on live days use the same per-day seed, so those contracts are present.
    books = {}
    attempts_by = {}
    for sid in list(SEARCH_IDS) + ["random"]:
        evs = ref_events if sid == "random" else signal_events[sid]
        for strike in strikes:
            for tp, sl, ts in ((tp, sl, ts) for tp in TPS for sl in SLS for ts in TIME_STOPS):
                trades, attempts, _skips = run_book(evs, opt, und, strike, (tp, sl, ts), costs, sid)
                key = (sid, strike, tp, sl, ts)
                books[key] = trades
                attempts_by[key] = attempts

    # Paired controls, then a second fetch for any contract the first pass did not load.
    controls = {}
    extra = {}
    for key, attempts in attempts_by.items():
        sid, strike, tp, sl, ts = key
        if sid == "random":
            continue
        drawn = []
        for att in attempts:
            ev = paired_entry(att, und)
            drawn.append(ev)
        controls[key] = drawn
        for ev in drawn:
            if ev is None:
                continue
            for m in range(ev["entry_min"], min(ev["entry_min"] + ENTRY_LOOK, FLAT_MIN)):
                spot = spot_at(und[ev["symbol"]].get(ev["day"]), m)
                if spot is None:
                    continue
                k = strike_price(spot, ev["side"], strike)
                if k is None:
                    continue
                contract = bt.lab_occ(ev["symbol"], ev["day"], "C" if ev["side"] == 1 else "P", k)
                if (ev["day"], contract) not in opt:
                    extra.setdefault(ev["day"], set()).add(contract)
    if extra:
        _print_scrubbed(f"second option pass for paired controls, {sum(len(v) for v in extra.values())} contracts")
        more = _fetch_all(oc, extra, und, synthetic, symbols)
        opt.update(more)

    control_trades = {}
    for key, drawn in controls.items():
        sid, strike, tp, sl, ts = key
        control_trades[key] = simulate_controls([e for e in drawn if e is not None], opt, und, (tp, sl, ts), costs, strike)

    def split_trades(trades, days):
        want = set(days)
        return [t for t in trades if t["day"] in want]

    rows = []
    is_search_rows = []
    for key, trades in books.items():
        sid, strike, tp, sl, ts = key
        role = "baseline" if sid == "random" else "search"
        for split_name, days in (("in_sample", is_days), ("holdout", oos_days)):
            # Held-out days are scored later, and only for the top 3 search configs.
            if split_name == "holdout":
                continue
            if not days and split_name == "holdout":
                continue
            skips = _skips_for(attempts_by[key], days)
            st = summarize(split_trades(trades, days), days, n_boot, _config_seed(sid, strike, tp, sl, ts, split_name))
            rnd_st = {
                "random_n": 0, "random_hit_rate": float("nan"),
                "random_mean_net_pct": float("nan"), "random_t": float("nan"),
            }
            paired = {"n_paired": 0, "t_diff": float("nan"), "p_diff": float("nan"),
                      "boot_diff_lo": float("nan"), "boot_diff_hi": float("nan")}
            if role == "search":
                ct = split_trades(control_trades.get(key, []), days)
                rnd_full = summarize(ct, days, n_boot, _config_seed(sid, strike, tp, sl, ts, split_name + "-rnd"))
                paired = paired_summary(split_trades(trades, days), ct, days, n_boot,
                                        _config_seed(sid, strike, tp, sl, ts, split_name + "-diff"))
                rnd_st = {
                    "random_n": rnd_full["n"], "random_hit_rate": rnd_full["hit_rate"],
                    "random_mean_net_pct": rnd_full["mean_net_pct"], "random_t": rnd_full["t"],
                }
            stats = _merge_stats(st, paired)
            stats.update(rnd_st)
            row = _make_row(sid, strike, tp, sl, ts, split_name, role, stats, skips, len(days), costs, False)
            rows.append(row)
            if role == "search" and split_name == "in_sample":
                is_search_rows.append(row)

    q = benjamini_hochberg([r["p_diff"] for r in is_search_rows])
    n_family = search_config_count()
    for r, qv in zip(is_search_rows, q):
        r["q_fdr"] = float(qv) if math.isfinite(qv) else float("nan")
        p = r["p_diff"]
        r["bonferroni_05"] = int(math.isfinite(p) and p * n_family < 0.05)
        rm = r["random_mean_net_pct"]
        r["beats_random"] = int(math.isfinite(r["mean_net_pct"]) and math.isfinite(rm) and r["mean_net_pct"] > rm)

    tops = []
    trade_dump = []

    def split_of(day):
        if day in is_set:
            return "in_sample"
        if day in oos_set:
            return "holdout"
        return ""

    for sid in SEARCH_IDS:
        group = [r for r in is_search_rows if r["signal"] == sid]
        chosen = select_top(group, TOP_K)
        for r in chosen:
            r["selected_top3"] = 1
            key = (r["signal"], r["strike"], r["tp"], r["sl"], r["time_stop"])
            if oos_days:
                trades = books[key]
                ct = control_trades.get(key, [])
                st = summarize(split_trades(trades, oos_days), oos_days, n_boot, _config_seed(*key, "holdout"))
                rnd_full = summarize(split_trades(ct, oos_days), oos_days, n_boot, _config_seed(*key, "holdout-rnd"))
                paired = paired_summary(split_trades(trades, oos_days), split_trades(ct, oos_days), oos_days, n_boot,
                                        _config_seed(*key, "holdout-diff"))
                stats = _merge_stats(st, paired)
                stats.update({
                    "random_n": rnd_full["n"], "random_hit_rate": rnd_full["hit_rate"],
                    "random_mean_net_pct": rnd_full["mean_net_pct"], "random_t": rnd_full["t"],
                })
                oos_row = _make_row(r["signal"], r["strike"], r["tp"], r["sl"], r["time_stop"], "holdout", "search",
                                    stats, _skips_for(attempts_by[key], oos_days), len(oos_days), costs, True)
                rows.append(oos_row)
            else:
                oos_row = None
            tops.append({"is": r, "oos": oos_row})
            trade_dump += _trade_rows(books[key], *key, split_of, "signal")
            trade_dump += _trade_rows(control_trades.get(key, []), *key, split_of, "random_paired")
            ref_key = ("random", key[1], key[2], key[3], key[4])
            if ref_key in books:
                trade_dump += _trade_rows(books[ref_key], ref_key[0], ref_key[1], ref_key[2], ref_key[3], ref_key[4],
                                          split_of, "random_ref")

    # FDR / bonferroni stay blank on holdout rows (they were not part of the family correction).
    csv_rows = []
    for r in rows:
        csv_rows.append(_row_out(
            signal=r["signal"], strike=r["strike"], tp=f"{r['tp']:.2f}", sl=_fmt_sl(r["sl"]),
            time_stop=r["time_stop"], split=r["split"], role=r["role"],
            n=r["n"], n_attempts=r["n_attempts"], trades_per_day=r["trades_per_day"],
            hit_rate=r["hit_rate"], mean_net_pct=r["mean_net_pct"], usd_per_day=r["usd_per_day"],
            max_drawdown_usd=r["max_drawdown_usd"], t=r["t"], p=r["p"], t_diff=r["t_diff"], p_diff=r["p_diff"],
            boot_lo=r["boot_lo"], boot_hi=r["boot_hi"], boot_diff_lo=r["boot_diff_lo"], boot_diff_hi=r["boot_diff_hi"],
            random_n=r["random_n"], random_hit_rate=r["random_hit_rate"],
            random_mean_net_pct=r["random_mean_net_pct"], random_t=r["random_t"],
            n_skip_entry=r["n_skip_entry"], n_skip_stale=r["n_skip_stale"], n_skip_spot=r["n_skip_spot"],
            n_days=r["n_days"], breakeven_hit_rate=r["breakeven_hit_rate"], q_fdr=r["q_fdr"],
            bonferroni_05=r["bonferroni_05"], beats_random=r["beats_random"], selected_top3=r["selected_top3"],
        ))

    entry_skips = sum(r["n_skip_entry"] for r in is_search_rows)
    stale_skips = sum(r["n_skip_stale"] for r in is_search_rows)
    attempts = sum(r["n_attempts"] for r in is_search_rows)
    skip_note = (
        f"Across the in-sample search grid (each exit is its own book, so the same signal is counted once per exit): "
        f"{entry_skips} entry skips and {stale_skips} stale-exit skips out of {attempts} one-position attempts."
    )
    t_crit = norm_ppf(1 - (0.05 / n_family) / 2)
    coverage = (
        f"Symbols {', '.join(symbols)}. Requested {days_n} sessions, underlying had {len(all_days)} completed, "
        f"this run kept {len(live)} with at least one OPRA print ({live[0]} to {live[-1]})."
        + (f" Dropped with no prints: {', '.join(d.isoformat() for d in dropped)}." if dropped else "")
        + f" Strikes: {', '.join(strikes)}. Bootstrap draws: {n_boot}."
    )
    meta = {
        "stamp": now.strftime("%Y-%m-%d %H:%M ET"),
        "synthetic": synthetic,
        "coverage": coverage,
        "cent_floor": cent_floor,
        "pct": pct,
        "commission": commission,
        "n_is": len(is_days),
        "n_oos": len(oos_days),
        "is_first": is_days[0].isoformat() if is_days else "—",
        "is_last": is_days[-1].isoformat() if is_days else "—",
        "oos_first": oos_days[0].isoformat() if oos_days else "—",
        "oos_last": oos_days[-1].isoformat() if oos_days else "—",
        "n_family": n_family,
        "t_crit": t_crit,
        "skip_note": skip_note,
    }
    report = render_report(meta, rows, tops)
    md_path = os.path.join(out_dir, "SCALP_REAL.md")
    csv_path = os.path.join(out_dir, "scalp_real_results.csv")
    tr_path = os.path.join(out_dir, "scalp_real_trades.csv")
    _write_text(md_path, report)
    _write_csv(csv_path, RESULT_FIELDS, csv_rows)
    _write_csv(tr_path, TRADE_FIELDS, trade_dump)
    summary = os.getenv("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a") as f:
            f.write(report + "\n")
    _print_scrubbed(f"wrote {md_path} {csv_path} {tr_path} in {(time.time() - t0) / 60:.1f} min")
    _print_scrubbed(report)


if __name__ == "__main__":
    main()
