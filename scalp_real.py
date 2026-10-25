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

import bisect
import builtins
import hashlib
import json
import math
import os
import sys
import time
import urllib.request
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
ENTRY_HOURS = (9, 10, 11, 12, 13, 14, 15)
# Reference and paired random minutes. Session minute 0 is 9:30.
# [5, 356) is 9:35 through 15:25 inclusive, matching the frozen baseline window.
RANDOM_MINUTE_LO = 5
RANDOM_MINUTE_HI = 356
# Prior-day VIX close. FRED, then Yahoo, then Cboe, then data/vix_daily.csv.
FRED_VIX_URL = "https://fred.stlouisfed.org/graph/fredgraph.csv?id=VIXCLS"
YAHOO_VIX_URL = "https://query1.finance.yahoo.com/v8/finance/chart/%5EVIX?interval=1d&range=10y"
CBOE_VIX_URL = "https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv"
VIX_SNAPSHOT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "vix_daily.csv")
VIX_TIMEOUT = 60
VIX_ATTEMPTS = 3
VIX_STALE_DAYS = 5
VIX_MIN_DOWNLOAD = 100
BROWSER_UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
)
# Descriptive buckets on the prior trading day's close. 20 belongs to >=20.
REGIME_BUCKETS = ("<16", "16-20", ">=20")
REGIME_TP = 0.15
REGIME_TIME_STOPS = (10, 30)

# Snapshot of diamondbot.BOOKS["TUNED"] and its entry window. The signal
# function reads the live constants; tests fail if the bot drifts.
TUNED_DIAMOND = (30, 14, 3, 1.0, 30, 50, 5, 70, 1)
DIAMOND_ENTRY_FROM = 945
DIAMOND_ENTRY_TO = 1430

TPS = (0.10, 0.15, 0.20, 0.30)
SLS = (0.10, 0.15, 0.20, 0.30, None)
TIME_STOPS = (5, 10, 20, 30)
# atm and 2itm are the original family. 1otm and 2otm are optional strike modes.
# A run that does not ask for them keeps the original family and N = 2240.
ORIGINAL_STRIKES = ("atm", "2itm")
STRIKE_MODES = ("atm", "2itm", "1otm", "2otm")

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
    "selected_top3", "skips_premium",
    "hour_9_n", "hour_9_net_pct", "hour_10_n", "hour_10_net_pct",
    "hour_11_n", "hour_11_net_pct", "hour_12_n", "hour_12_net_pct",
    "hour_13_n", "hour_13_net_pct", "hour_14_n", "hour_14_net_pct",
    "hour_15_n", "hour_15_net_pct",
]

TRADE_FIELDS = [
    "date", "time", "symbol", "side", "entry", "exit", "reason", "net_pct",
    "signal", "strike", "tp", "sl", "time_stop", "split", "book",
    "contract", "dollar",
]


def family_strike_modes(strikes=None):
    """Strike modes that enter the Bonferroni family for a run.

    The default family is atm and 2itm, so N stays 2240, including a run that
    asks for only one of those two. A run that includes 1otm or 2otm uses the
    strike modes that run actually includes (the full grid of those modes).
    """
    if strikes is None:
        return ORIGINAL_STRIKES
    chosen = {s for s in strikes}
    if not chosen or chosen <= set(ORIGINAL_STRIKES):
        return ORIGINAL_STRIKES
    return tuple(s for s in STRIKE_MODES if s in chosen)


def search_config_count(strikes=None):
    """Bonferroni family: every search signal x strike x exit. Random is the control."""
    modes = family_strike_modes(strikes)
    return len(SEARCH_IDS) * len(modes) * len(TPS) * len(SLS) * len(TIME_STOPS)


def family_note(strikes=None):
    modes = family_strike_modes(strikes)
    noun = "strike mode" if len(modes) == 1 else "strike modes"
    note = (
        f"{len(SEARCH_IDS)} search signals x {len(modes)} {noun} "
        f"({', '.join(modes)}) x {len(TPS)} targets x {len(SLS)} stops x {len(TIME_STOPS)} time stops"
    )
    if set(modes) <= set(ORIGINAL_STRIKES):
        note += "; atm/2itm runs keep N = 2240 even when the run asks for only one of those two"
    else:
        note += "; this run includes 1otm or 2otm, so N is the full grid of the strike modes in the run"
    return note


def iter_configs(strikes=None):
    modes = ORIGINAL_STRIKES if strikes is None else strikes
    for sig in SIGNAL_IDS:
        for strike in modes:
            for tp in TPS:
                for sl in SLS:
                    for ts in TIME_STOPS:
                        yield sig, strike, tp, sl, ts


def _fmt_sl(sl):
    return "none" if sl is None else f"{sl:.2f}"


def render_predeclared():
    """Frozen text. Written before any OPRA run. main() refuses to compute if the file differs."""
    n_search = search_config_count()
    n_all = n_search + len(ORIGINAL_STRIKES) * len(TPS) * len(SLS) * len(TIME_STOPS)
    lines = [
        "SCALP_REAL PREDECLARED 2026-10-24",
        "Written before any OPRA computation. Do not add a config after seeing results.",
        "DATA ONLY. No order is sent by scalp_real.py or by .github/workflows/scalp_real.yml.",
        "This file is a research plan, not trading advice.",
        "",
        "DATA",
        "- SPY and QQQ, 0DTE. Strike modes are atm, 2itm, 1otm, and 2otm. The workflow default is 2itm,atm.",
        "  The config list below is that default grid. A run may choose a subset. Bonferroni N follows the rule in SPLIT AND TESTS.",
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
        "- Premium band (SCALP_PREMIUM_MIN and SCALP_PREMIUM_MAX, dollars per share). Empty means no bound on that side.",
        "  The entry print is the real option open used as the entry. An entry is taken only when that open is inside [min, max].",
        "  A print outside the band is not a trade: it is skipped and counted as skips_premium.",
        "  The same band applies to paired random controls and to the reference random book.",
        "  A control whose entry print falls outside the band is skipped and counted the same way.",
        "  On a search result row, skips_premium is the signal book's premium skips plus the paired controls skipped for the band.",
        "  On a random baseline row, skips_premium is that book's own premium skips.",
        "- Exits walk 1-minute bars. A minute with no print may use the lab_fetch_opt close only when that close is at most 5 minutes old.",
        "- A price older than 5 minutes is never an exit. If the time stop or the 15:55 flat falls on a stale minute, the trade is unfilled and counted.",
        "- Same bar: a stop is applied before a target. A stop that gaps fills at the bar open when that open is worse than the stop.",
        "- A target fills at the target price (not at a higher wick).",
        "- One open position per symbol inside each (signal, strike) book. A new signal while the book is in a trade is ignored.",
        "- Calls at the same minute are considered before puts. Flat at the 15:55 bar (session minute 385). No new entry at or after 15:55.",
        "- Entry clock (SCALP_FIRST_ENTRY and SCALP_LAST_ENTRY, HH:MM ET). Empty means no extra cutoff.",
        "  Empty SCALP_LAST_ENTRY keeps the existing rule: no new entry at or after 15:55.",
        "  When SCALP_FIRST_ENTRY is set, no signal entry and no control entry before that time.",
        "  When SCALP_LAST_ENTRY is set, no signal entry and no control entry at or after that time.",
        "  The same window applies to paired random controls and to the reference random book.",
        "",
        "SPLIT AND TESTS",
        "- VIX day filter (SCALP_VIX_MIN, SCALP_VIX_MAX). Empty means that side is open. Both empty turns the filter off.",
        "  The level is the prior trading day's VIX close: FRED series VIXCLS",
        "  (https://fred.stlouisfed.org/graph/fredgraph.csv?id=VIXCLS), then the Yahoo chart",
        "  API for ^VIX, then the Cboe VIX history file. Each download is retried.",
        "  data/vix_daily.csv fills any gap and is the last fallback. The session's own close is not used.",
        "  The report states the VIX data span. A missing prior close older than 5 days stops the run.",
        "  The most recent close, if it is the only one missing and it is within 5 days, uses the latest",
        "  available prior close and the report says so.",
        "  A day is kept only when min <= prior close < max, on the sides that are set.",
        "  The same kept days are used for signal trades, paired random controls, and the reference random book.",
        "  The report prints how many days were kept and how many were dropped.",
        "  If the VIX history cannot be fetched, the run stops. It does not score an unfiltered book.",
        "- After dead OPRA days are dropped, and after the VIX day filter, the last round(25%) of remaining days, at least 1, are held out.",
        "  The report states the in-sample and held-out day counts for that split.",
        "- Held-out days are scored once, and only for the top 3 in-sample configs of each search signal.",
        "- The report section 'By VIX regime' does not use the VIX day filter. Buckets are post-hoc and descriptive.",
        "  They are not a selected result and they are not part of N.",
        "- Rank key (in-sample only): day-clustered t of (signal net % - paired-random net %) on trades where both filled,",
        "  then mean net %, then trade count. A config needs at least 5 signal fills and 5 paired fills to be ranked.",
        "- Primary t-stat is day-clustered on the per-trade net percent (sum of within-day deviations, divided by n).",
        "- Bootstrap 95% CI resamples days with replacement (default 2000) and recomputes the per-trade mean. Seed 20261024 plus a fixed per-config salt.",
        f"- Search family N = {n_search} when the run uses only atm and 2itm "
        f"(every search signal x those two strikes x 4 targets x 5 stops x 4 time stops), "
        "including a run that asks for only one of those two.",
        "- A run that includes 1otm or 2otm recomputes N from the strike modes in that run "
        "(the full grid of those modes x the same signals and exits) and prints that N and the Bonferroni bar.",
        "- The random rows are the baseline. They are not in N and they are not ranked for the holdout.",
        "- Bonferroni: two-sided normal p * N < 0.05. FDR: Benjamini-Hochberg on the in-sample paired-difference p-values.",
        "- Break-even hit rate assumes the trade exits at the target or the stop and never by time: p = -net_loss / (net_win - net_loss),",
        "  with the same half-spread and commission, at that config's in-sample median entry open. No stop -> not defined.",
        "",
        "RANDOM",
        "- Paired control (the comparison column): one control per one-position entry attempt, same symbol, day, and direction,",
        "  minute drawn uniformly from the same 30-minute clock bucket inside the allowed entry window, excluding the signal minute.",
        "  The allowed window is 9:35-15:25, intersected with SCALP_FIRST_ENTRY / SCALP_LAST_ENTRY when those are set.",
        "  If that bucket has no other allowed minute, the draw uses the whole allowed window. A minute outside the clock is not drawn.",
        "  Controls are not put through a second one-position rule, so the attempt count stays matched.",
        "  The control is priced with the same simulate_trade fill and exit as the signal.",
        "  Seed = SHA256('paired', signal, strike, day, symbol, entry minute, side).",
        "- Reference book (signal id random): per day and symbol, N = round-half-up median of the other signals' raw fire counts that day.",
        "  N distinct minutes drawn uniformly from the real minutes in 9:35-15:25 that also fall inside the entry clock",
        "  (empty clock means the whole 9:35-15:25 list). Fair coin direction, then the same one-position rule and the same",
        "  run_book fills and exits as a signal trade.",
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
        "- atm = round(spot). 2itm call = round(spot) - 2. 2itm put = round(spot) + 2.",
        "- 1otm call = round(spot) + 1. 1otm put = round(spot) - 1. 2otm call = round(spot) + 2. 2otm put = round(spot) - 2.",
        "- Expiration is the session date. Symbol from backtest.lab_occ.",
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


def simulate_trade(opt, entry_min, cfg, costs, allow_slip=True, premium=None):
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
    if not premium_in_band(raw, premium):
        return {"status": "skip_premium", "entry_min": ent, "raw_entry": raw}
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
        hs_in = half_spread(raw, cent_floor, pct)
        hs_out = half_spread(fill, cent_floor, pct)
        spread_cost_pct = (hs_in + hs_out) / raw * 100.0 if raw > 0 else float("nan")
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
            "spread_cost_pct": spread_cost_pct,
        }
    return {"status": "skip_stale", "entry_min": ent}


def strike_price(spot, side, mode):
    if spot is None or not math.isfinite(spot) or spot <= 0:
        return None
    k = int(np.round(float(spot)))
    if mode == "2itm":
        k = k - 2 * int(side)
    elif mode == "1otm":
        k = k + int(side)
    elif mode == "2otm":
        k = k + 2 * int(side)
    elif mode != "atm":
        raise ValueError(mode)
    return k if k > 0 else None


def premium_in_band(raw, band):
    """True when `raw` (the entry print, dollars per share) is inside [min, max].

    `band` is None, or (min, max) with either side None meaning that side is open.
    The comparison is inclusive.
    """
    if band is None:
        return True
    lo, hi = band
    if lo is not None and raw < lo:
        return False
    if hi is not None and raw > hi:
        return False
    return True


def parse_clock_et(text, name):
    """Return (HH:MM label or None, session minute or None). Empty keeps the existing rule."""
    raw = (text or "").strip()
    if not raw:
        return None, None
    if len(raw) != 5 or raw[2] != ":" or not (raw[:2].isdigit() and raw[3:].isdigit()):
        sys.exit(f"{name} must be HH:MM ET, or empty")
    hh, mm = int(raw[:2]), int(raw[3:])
    if hh > 23 or mm > 59:
        sys.exit(f"{name} must be HH:MM ET, or empty")
    return raw, hh * 60 + mm - (9 * 60 + 30)


def minute_allowed(minute, window):
    """True when a new entry may be taken at this session minute.

    `window` is None or (first_session_minute or None, last_session_minute or None).
    The 15:55 bar is never an entry. A set last minute rejects that minute and later ones.
    A set first minute rejects anything earlier.
    """
    if minute is None or minute < 0 or minute >= FLAT_MIN or minute >= N_MIN:
        return False
    if not window:
        return True
    first, last = window
    if first is not None and minute < first:
        return False
    if last is not None and minute >= last:
        return False
    return True


def describe_premium(band):
    if band is None or (band[0] is None and band[1] is None):
        return (
            "Premium band: none. Any real entry print at or above $0.05 can be taken. "
            "skips_premium stays 0."
        )
    lo = "no minimum" if band[0] is None else f"${band[0]:.2f}"
    hi = "no maximum" if band[1] is None else f"${band[1]:.2f}"
    return (
        f"Premium band: the entry print (the real option open) must be within [{lo}, {hi}] dollars per share. "
        "An entry outside that band is skipped and counted as skips_premium. "
        "The same band is applied to paired random controls and to the reference random book."
    )


def describe_window(first_label, last_label):
    if first_label is None and last_label is None:
        return "Entry cutoff: none beyond the existing rule. No new entry at or after 15:55 ET."
    parts = []
    if first_label:
        parts.append(f"no signal or control entry before {first_label} ET")
    else:
        parts.append("no extra first-entry cutoff")
    if last_label:
        parts.append(f"no signal or control entry at or after {last_label} ET")
    else:
        parts.append("no new entry at or after 15:55 ET")
    return (
        "Entry cutoff: " + "; ".join(parts) + ". "
        "The same clock applies to paired random controls and to the reference random book. Flat at 15:55."
    )


def entry_hour_breakdown(trades):
    """Mean net % and fill count by the entry print's clock hour. Descriptive only."""
    buckets = {h: [] for h in ENTRY_HOURS}
    for t in trades:
        hh = int(str(t["time"])[:2])
        if hh in buckets:
            buckets[hh].append(float(t["net_pct"]))
    out = {}
    for h in ENTRY_HOURS:
        vals = buckets[h]
        out[h] = {
            "n": len(vals),
            "net_pct": float(np.mean(vals)) if vals else float("nan"),
        }
    return out


def minute_hour(entry_min):
    """Clock hour in America/New_York for a session minute (9:30 = 0)."""
    return ((9 * 60 + 30) + int(entry_min)) // 60


def random_eligible_minutes(sess, entry_window=None):
    """Real underlying minutes inside 9:35-15:25 and inside the entry clock.

    The baseline is session minutes [5, 356): 9:35 through 15:25 inclusive.
    `entry_window` None keeps that list. A set clock intersects it.
    The 15:55 bar is never included.
    """
    if sess is None:
        return []
    real = sess["real"]
    out = []
    last = min(RANDOM_MINUTE_HI, FLAT_MIN, len(real))
    for m in range(RANDOM_MINUTE_LO, last):
        if not real[m]:
            continue
        if not minute_allowed(m, entry_window):
            continue
        out.append(m)
    return out


def draw_random_minutes(eligible, n, rng):
    """Uniform distinct draws. `n` is capped at the size of `eligible`."""
    n = min(int(n), len(eligible))
    if n <= 0:
        return np.asarray([], dtype=int)
    pick = rng.choice(np.asarray(eligible, dtype=int), size=n, replace=False)
    return np.asarray(pick, dtype=int)


def flat_round_trip_pct(raw, costs):
    """Net % of a round trip that sells at the same raw price. Spread plus commission only."""
    if raw is None or not math.isfinite(raw) or raw <= 0:
        return float("nan")
    cent_floor, pct, commission = costs
    debit = raw + half_spread(raw, cent_floor, pct)
    credit = max(0.0, raw - half_spread(raw, cent_floor, pct))
    dollar = (credit - debit) * 100.0 - 2.0 * commission
    if debit <= 0:
        return float("nan")
    return dollar / (debit * 100.0) * 100.0


def assign_vix_bucket(prior):
    """Bucket a prior-day VIX close. None when the close is missing.

    <16, then 16 up to but not including 20, then >=20.
    """
    if prior is None or not isinstance(prior, (int, float)) or not math.isfinite(prior):
        return None
    if prior < 16.0:
        return "<16"
    if prior < 20.0:
        return "16-20"
    return ">=20"


def _prior_in_band(prior, vix_min, vix_max):
    """True when a prior close passes the day filter. Both bounds None keeps every day."""
    if vix_min is None and vix_max is None:
        return True
    if prior is None or not isinstance(prior, (int, float)) or not math.isfinite(prior):
        return False
    if vix_min is not None and prior < vix_min:
        return False
    if vix_max is not None and prior >= vix_max:
        return False
    return True


def parse_vix_band(vix_min, vix_max):
    """Validate SCALP_VIX_MIN / SCALP_VIX_MAX. Empty bounds arrive as None."""
    if vix_min is not None and vix_min < 0:
        sys.exit("SCALP_VIX_MIN cannot be negative")
    if vix_max is not None and vix_max < 0:
        sys.exit("SCALP_VIX_MAX cannot be negative")
    if vix_min is not None and vix_max is not None and not vix_min < vix_max:
        sys.exit("SCALP_VIX_MIN must be below SCALP_VIX_MAX; a day is kept when min <= prior close < max")
    return vix_min, vix_max


def parse_fred_vix_csv(text):
    """Map session date -> VIX close from a FRED VIXCLS graph CSV. '.' is a missing day."""
    out = {}
    for line in str(text).splitlines():
        line = line.strip().lstrip("\ufeff")
        if not line or line.lower().startswith("observation") or line.lower().startswith("date"):
            continue
        parts = line.split(",")
        if len(parts) < 2:
            continue
        raw_date, raw_val = parts[0].strip(), parts[1].strip()
        if raw_val in ("", "."):
            continue
        try:
            day = datetime.strptime(raw_date, "%Y-%m-%d").date()
            val = float(raw_val)
        except ValueError:
            continue
        if math.isfinite(val) and val > 0:
            out[day] = val
    return out


def parse_yahoo_vix_chart(text):
    """Map session date -> close from a Yahoo v8 chart payload for ^VIX.

    Daily stamps are converted to the America/New_York calendar date.
    A null close is skipped.
    """
    data = json.loads(text)
    chart = data.get("chart") or {}
    if chart.get("error"):
        raise RuntimeError(str(chart.get("error"))[:200])
    result = (chart.get("result") or [None])[0]
    if not result:
        raise RuntimeError("Yahoo chart payload had no result")
    stamps = result.get("timestamp") or []
    quote = ((result.get("indicators") or {}).get("quote") or [{}])[0]
    closes = quote.get("close") or []
    out = {}
    for stamp, close in zip(stamps, closes):
        if stamp is None or close is None:
            continue
        try:
            val = float(close)
        except (TypeError, ValueError):
            continue
        if not math.isfinite(val) or val <= 0:
            continue
        day = datetime.fromtimestamp(int(stamp), timezone.utc).astimezone(NY).date()
        out[day] = val
    return out


def _parse_vix_day(raw):
    raw = str(raw).strip()
    for fmt in ("%Y-%m-%d", "%m/%d/%Y"):
        try:
            return datetime.strptime(raw, fmt).date()
        except ValueError:
            continue
    return None


def _keep_vix_close(raw):
    raw = str(raw).strip()
    if raw in ("", "."):
        return None
    try:
        val = float(raw)
    except ValueError:
        return None
    if not math.isfinite(val) or val <= 0:
        return None
    return val


def parse_cboe_vix_csv(text):
    """Map session date -> close from Cboe VIX_History.csv.

    The file is DATE,OPEN,HIGH,LOW,CLOSE. Dates are MM/DD/YYYY or YYYY-MM-DD.
    A leading title row and an empty close are skipped.
    """
    rows = []
    for line in str(text).splitlines():
        line = line.strip().lstrip("\ufeff")
        if not line:
            continue
        rows.append([part.strip().strip('"') for part in line.split(",")])
    date_i = 0
    close_i = None
    start = 0
    for i, parts in enumerate(rows[:8]):
        upper = [part.upper() for part in parts]
        if "DATE" in upper and "CLOSE" in upper:
            date_i = upper.index("DATE")
            close_i = upper.index("CLOSE")
            start = i + 1
            break
    out = {}
    for parts in rows[start:]:
        ci = close_i
        if ci is None:
            if len(parts) < 2:
                continue
            ci = 4 if len(parts) > 4 else len(parts) - 1
        if date_i >= len(parts) or ci >= len(parts):
            continue
        day = _parse_vix_day(parts[date_i])
        val = _keep_vix_close(parts[ci])
        if day is None or val is None:
            continue
        out[day] = val
    return out


def parse_vix_snapshot_csv(text):
    """Map session date -> close from data/vix_daily.csv. Header date,vix_close. Empty values are skipped."""
    out = {}
    for line in str(text).splitlines():
        line = line.strip().lstrip("\ufeff")
        if not line or line.lower().startswith("date"):
            continue
        parts = [part.strip().strip('"') for part in line.split(",")]
        if len(parts) < 2:
            continue
        day = _parse_vix_day(parts[0])
        val = _keep_vix_close(parts[1])
        if day is None or val is None:
            continue
        out[day] = val
    return out


def load_vix_snapshot(path=None):
    path = path or VIX_SNAPSHOT_PATH
    with open(path, encoding="utf-8") as f:
        return parse_vix_snapshot_csv(f.read())


def _default_vix_transport(url, headers, timeout=VIX_TIMEOUT, attempts=VIX_ATTEMPTS):
    last = None
    for i in range(attempts):
        try:
            req = urllib.request.Request(url, headers=headers, method="GET")
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read().decode("utf-8", errors="replace")
        except Exception as e:  # noqa: BLE001
            last = e
            if i + 1 < attempts:
                time.sleep(1.0 * (i + 1))
    raise last


def _vix_span_source(owner, closes):
    order = ("FRED VIXCLS", "Yahoo ^VIX", "Cboe VIX", "data/vix_daily.csv")
    used = [name for name in order if name in set(owner.values())]
    dates = sorted(closes)
    first = dates[0].isoformat()
    last = dates[-1].isoformat()
    label = " + ".join(used)
    return (
        f"{label}. VIX data span {first} through {last} ({len(dates)} closes). "
        f"Last date {last}."
    )


def fetch_vix_closes(transport=None):
    """Return (date -> close, source). FRED, then Yahoo chart, then Cboe, then the snapshot.

    Each download is tried through the transport. The default transport retries
    three times with a 60s timeout. Sources are merged: an earlier source wins
    a date that appears twice, and data/vix_daily.csv fills any gap. The
    snapshot is also the last fallback when every download fails.

    Raises SystemExit when every source fails. A caller must not continue
    with an empty series: that would silently drop the day filter.
    """
    transport = transport or _default_vix_transport
    errors = []
    downloaded = {}
    sources = (
        ("FRED VIXCLS", FRED_VIX_URL, parse_fred_vix_csv, {"User-Agent": BROWSER_UA, "Accept": "text/csv,*/*"}),
        ("Yahoo ^VIX", YAHOO_VIX_URL, parse_yahoo_vix_chart, {"User-Agent": BROWSER_UA, "Accept": "application/json"}),
        ("Cboe VIX", CBOE_VIX_URL, parse_cboe_vix_csv, {"User-Agent": BROWSER_UA, "Accept": "text/csv,*/*"}),
    )
    for name, url, parse, headers in sources:
        try:
            body = transport(url, headers)
            parsed = parse(body)
            if len(parsed) < VIX_MIN_DOWNLOAD:
                raise RuntimeError(f"only {len(parsed)} closes")
            downloaded[name] = parsed
        except Exception as e:  # noqa: BLE001
            errors.append(f"{name}: {type(e).__name__}")
            _print_scrubbed(f"  VIX {name} failed: {type(e).__name__}")

    snapshot = {}
    try:
        snapshot = load_vix_snapshot()
        if not snapshot:
            raise RuntimeError("empty snapshot")
    except Exception as e:  # noqa: BLE001
        errors.append(f"data/vix_daily.csv: {type(e).__name__}")
        _print_scrubbed(f"  VIX data/vix_daily.csv failed: {type(e).__name__}")

    if not downloaded and not snapshot:
        sys.exit(
            "Could not download VIX closes from FRED, Yahoo, or Cboe, and data/vix_daily.csv "
            "could not be read. Refusing to run. "
            + "; ".join(errors)
        )

    merged = {}
    owner = {}
    for name, layer in (
        ("data/vix_daily.csv", snapshot),
        ("Cboe VIX", downloaded.get("Cboe VIX") or {}),
        ("Yahoo ^VIX", downloaded.get("Yahoo ^VIX") or {}),
        ("FRED VIXCLS", downloaded.get("FRED VIXCLS") or {}),
    ):
        for day, val in layer.items():
            merged[day] = float(val)
            owner[day] = name
    source = _vix_span_source(owner, merged)
    last = max(merged)
    _print_scrubbed(f"VIX source {source}")
    _print_scrubbed(f"VIX last date available {last.isoformat()}")
    return merged, source


def previous_weekday(day):
    d = day - timedelta(days=1)
    while d.weekday() >= 5:
        d -= timedelta(days=1)
    return d


def latest_weekday(day):
    d = day
    while d.weekday() >= 5:
        d -= timedelta(days=1)
    return d


def apply_vix_coverage(closes, sessions, source, today=None):
    """Stop if a session's prior trading day is missing and the hole is not the one recent tail.

    The first session's previous weekday may be a holiday. When that gap is
    older than 5 days and a close exists within 5 calendar days before the
    session, it is covered. A recent hole is not covered that way. Later
    sessions require the previous session date itself. The latest weekday as
    of `today` is also required, because that is the most recent close.

    One missing date is tolerated only when it is that most recent close, it
    is within 5 days, and nothing later is already in the series. The close is
    not invented: prior_vix_close already walks back. The substitution is
    logged and appended to the source string. Any other hole raises SystemExit
    and names the missing dates.
    """
    if not sessions:
        return closes, source
    today = today or datetime.now(NY).date()
    if isinstance(today, datetime):
        today = today.date()
    ordered = []
    for day in sessions:
        if isinstance(day, datetime):
            day = day.date()
        ordered.append(day)
    ordered = sorted(set(ordered))
    needed = []
    first = ordered[0]
    prev0 = previous_weekday(first)
    if prev0 not in closes:
        near = any(0 < (first - d).days <= VIX_STALE_DAYS for d in closes)
        # A holiday at the start of a long sample is fine. A hole in the last
        # 5 days is still a missing prior and is listed with the others.
        stale_gap = (today - prev0).days > VIX_STALE_DAYS
        if not (near and stale_gap):
            needed.append(prev0)
    for prev in ordered[:-1]:
        if prev not in closes:
            needed.append(prev)
    tail = latest_weekday(today)
    if tail not in closes:
        needed.append(tail)
    missing = sorted(set(d for d in needed if d not in closes))
    if not missing:
        return closes, source
    hole = missing[-1]
    only_recent_tail = (
        len(missing) == 1
        and 0 <= (today - hole).days <= VIX_STALE_DAYS
        and not any(d > hole for d in closes)
    )
    if only_recent_tail:
        dates = sorted(closes)
        i = bisect.bisect_left(dates, hole)
        if i <= 0:
            sys.exit(
                f"VIX history is missing {hole.isoformat()} and has no earlier close. Refusing to run."
            )
        carry_day = dates[i - 1]
        carry = float(closes[carry_day])
        _print_scrubbed(
            f"  VIX close {hole.isoformat()} is missing; "
            f"using latest available prior close {carry_day.isoformat()} {carry:.2f}."
        )
        note = (
            f" Missing {hole.isoformat()} (most recent close only); "
            f"using latest available prior close {carry_day.isoformat()} {carry:.2f}."
        )
        return closes, source + note
    listed = ", ".join(d.isoformat() for d in missing)
    sys.exit(
        "VIX history does not cover every session's prior trading day. "
        f"Missing dates: {listed}. "
        "A gap older than 5 days, or more than the single most recent close, stops the run. "
        "Refusing to run."
    )


def prior_vix_close(day, closes, dates=None):
    """Last VIX close strictly before `day`. The session day's own close is ignored."""
    if not closes:
        return None
    dates = dates if dates is not None else sorted(closes)
    i = bisect.bisect_left(dates, day)
    if i <= 0:
        return None
    return float(closes[dates[i - 1]])


def prior_vix_by_day(days, closes):
    dates = sorted(closes)
    return {day: prior_vix_close(day, closes, dates) for day in days}


def filter_days_by_vix(days, closes, vix_min, vix_max):
    """Return (kept, dropped) in the original order.

    Both bounds None: every day is kept and dropped is empty.
    An active filter drops a day whose prior close is missing or outside the band.
    `dropped` items are (day, prior or None).
    """
    if vix_min is None and vix_max is None:
        return list(days), []
    dates = sorted(closes)
    kept, dropped = [], []
    for day in days:
        prior = prior_vix_close(day, closes, dates)
        if _prior_in_band(prior, vix_min, vix_max):
            kept.append(day)
        else:
            dropped.append((day, prior))
    return kept, dropped


def describe_vix_filter(vix_min, vix_max, kept, dropped, source, n_is, n_oos):
    """One report paragraph: the band, the source, and the day counts after the filter."""
    n_kept = len(kept)
    if vix_min is None and vix_max is None:
        return (
            f"VIX day filter: off (SCALP_VIX_MIN and SCALP_VIX_MAX empty). "
            f"Prior-day VIX closes were still loaded from {source} for the regime table. "
            f"Days kept: {n_kept}. Days dropped: 0. "
            f"The 25% holdout is computed on these days: {n_is} in-sample, {n_oos} held-out."
        )
    if vix_min is not None and vix_max is not None:
        band = f"{vix_min:g} <= close < {vix_max:g}"
    elif vix_min is not None:
        band = f"close >= {vix_min:g}"
    else:
        band = f"close < {vix_max:g}"
    missing = sum(1 for _day, prior in dropped if prior is None)
    out_of_band = len(dropped) - missing
    listed = []
    for day, prior in dropped:
        if prior is None:
            listed.append(f"{day.isoformat()} (no prior close)")
        else:
            listed.append(f"{day.isoformat()} ({prior:.2f})")
    detail = ", ".join(listed) if listed else "none"
    return (
        f"VIX day filter: prior trading day's VIX close from {source} must satisfy {band}. "
        "No lookahead: the session day's own close is not used. "
        f"Days kept: {n_kept}. Days dropped: {len(dropped)} "
        f"({out_of_band} outside the band, {missing} with no prior close). "
        f"Dropped: {detail}. "
        "The same kept days are used for signal trades, paired random controls, and the reference random book. "
        f"The 25% holdout is computed after this filter: {n_is} in-sample, {n_oos} held-out."
    )


def regime_rows(books, split_days, prior_of, signals, strikes):
    """Descriptive 15% target rows by prior-day VIX bucket.

    `books` is keyed by (signal, strike, tp, sl, time_stop). This does not
    apply SCALP_VIX_MIN / SCALP_VIX_MAX. `split_days` is [(name, [days]), ...].
    """
    rows = []
    for sid in signals:
        for strike in strikes:
            for sl in SLS:
                for ts in REGIME_TIME_STOPS:
                    trades = books.get((sid, strike, REGIME_TP, sl, ts)) or []
                    for split_name, days in split_days:
                        for bucket in REGIME_BUCKETS:
                            bucket_days = [d for d in days if assign_vix_bucket(prior_of.get(d)) == bucket]
                            want = set(bucket_days)
                            subset = [t for t in trades if t["day"] in want]
                            stats = summarize(subset, bucket_days, 0, 0)
                            rows.append({
                                "signal": sid,
                                "strike": strike,
                                "tp": REGIME_TP,
                                "sl": sl,
                                "time_stop": ts,
                                "split": split_name,
                                "bucket": bucket,
                                "n": stats["n"],
                                "hit_rate": stats["hit_rate"],
                                "mean_net_pct": stats["mean_net_pct"],
                                "t": stats["t"],
                            })
    return rows


def regime_intro(n_live, reg_is, reg_oos, n_missing, n_kept, n_dropped, n_is, n_oos, n_family, filter_on):
    """State both splits. The regime split is before the VIX day filter."""
    def _span(days):
        if not days:
            return "none"
        return f"{days[0].isoformat()} to {days[-1].isoformat()}"

    def _days(n):
        return f"{n} day" if n == 1 else f"{n} days"

    if not filter_on:
        same = " The selection split is the same days, because the VIX day filter is off."
    elif n_dropped == 0:
        same = " The VIX day filter dropped no days, so the selection split is these same days."
    else:
        same = (
            " The selection holdout is a different split: it is computed after the VIX day filter, "
            f"{n_is} in-sample and {n_oos} held-out, on the {n_kept} kept days ({n_dropped} dropped)."
        )
    return (
        "Descriptive only. These are post-hoc buckets, not selected, and they were not used to rank configs. "
        f"They are not part of the search family. Search family N = {n_family}. "
        f"Fixed target 15%. Each stop in the grid. Time stop 10m and 30m. "
        "Search signals and the reference random book, at each strike in this run "
        "(atm and 2itm on a default run; 1otm and 2otm when the strike input includes them). "
        "Net % is the per-trade mean. t is the day-clustered t on the trades in that bucket and split. "
        f"This section does not use the VIX day filter. It uses all {n_live} OPRA days. "
        f"In-sample: {_days(len(reg_is))} ({_span(reg_is)}). "
        f"Held-out: {_days(len(reg_oos))} ({_span(reg_oos)}). "
        "That 25% holdout is computed on the OPRA days before the VIX day filter. "
        f"Days with no prior VIX close are left out of the buckets: {n_missing}."
        + same
    )


def audit_fill_stats(trades, costs):
    """Premium, spread, flat-cost, and exit-reason shares for one random book."""
    premiums = [float(t["raw_entry"]) for t in trades if math.isfinite(float(t.get("raw_entry", float("nan"))))]
    empty = {
        "p10": float("nan"), "p50": float("nan"), "p90": float("nan"),
        "spread_pct": float("nan"), "flat_pct": float("nan"),
        "stop_share": float("nan"), "tp_share": float("nan"),
        "time_share": float("nan"), "flat_share": float("nan"),
    }
    if not premiums:
        return empty
    p10, p50, p90 = (float(x) for x in np.quantile(np.asarray(premiums, dtype=float), [0.10, 0.50, 0.90]))
    spreads = [float(t["spread_cost_pct"]) for t in trades if math.isfinite(float(t.get("spread_cost_pct", float("nan"))))]
    flats = [flat_round_trip_pct(float(t["raw_entry"]), costs) for t in trades]
    flats = [x for x in flats if math.isfinite(x)]
    n = len(trades)
    counts = {"stop": 0, "tp": 0, "time": 0, "flat": 0}
    for t in trades:
        reason = t.get("reason")
        if reason in counts:
            counts[reason] += 1

    def _share(key):
        return counts[key] / n if n else float("nan")

    return {
        "p10": p10, "p50": p50, "p90": p90,
        "spread_pct": float(np.median(spreads)) if spreads else float("nan"),
        "flat_pct": float(np.median(flats)) if flats else float("nan"),
        "stop_share": _share("stop"), "tp_share": _share("tp"),
        "time_share": _share("time"), "flat_share": _share("flat"),
    }


def hour_draw_table(events, und, symbols, days, entry_window):
    """Drawn random minutes by hour, and the eligible-minute pool those draws came from."""
    drawn = {h: 0 for h in ENTRY_HOURS}
    pool = {h: 0 for h in ENTRY_HOURS}
    dayset = set(days)
    for day in days:
        for sym in symbols:
            sess = und.get(sym, {}).get(day)
            for m in random_eligible_minutes(sess, entry_window):
                hh = minute_hour(m)
                if hh in pool:
                    pool[hh] += 1
    for ev in events:
        if ev["day"] not in dayset:
            continue
        hh = minute_hour(ev["entry_min"])
        if hh in drawn:
            drawn[hh] += 1
    return drawn, pool


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


def reference_random_events(signal_events, und, symbols, days, entry_window=None):
    """Standalone baseline book. N per day/symbol = median raw fire count of the search signals.

    Minutes are drawn uniformly from the real 9:35-15:25 minutes that also pass
    `entry_window`. The fill path is run_book, the same path as a signal.
    """
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
            eligible = random_eligible_minutes(sess, entry_window)
            if not eligible:
                continue
            n = min(n, len(eligible))
            rng = np.random.default_rng(stream_seed("ref", day.isoformat(), sym))
            pick = draw_random_minutes(eligible, n, rng)
            dirs = rng.choice(np.asarray([-1, 1]), size=len(pick))
            for minute, side in zip(pick, dirs):
                events.append({
                    "day": day, "symbol": sym, "side": int(side), "entry_min": int(minute),
                    "signal_i": -1, "signal_time": None, "signal": "random",
                })
    events.sort(key=lambda e: (e["day"], e["symbol"], e["entry_min"], -e["side"]))
    return events


def paired_entry(attempt, und, entry_window=None):
    """One matched control minute for an entry attempt. Returns an event dict or None.

    The pool is the same 30-minute bucket inside the allowed entry window
    (9:35-15:25 intersected with the entry clock). If that bucket is empty,
    the draw uses the whole allowed window. Minutes outside the clock are not drawn.
    """
    day, sym, minute, side = attempt["day"], attempt["symbol"], attempt["entry_min"], attempt["side"]
    sess = und[sym].get(day)
    if sess is None:
        return None
    eligible = [m for m in random_eligible_minutes(sess, entry_window) if m != minute]
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


def run_book(events, opt, und, strike, cfg, costs, signal, premium=None, entry_window=None):
    """One position per symbol. Returns fills, attempts (including skips), and skip counts.

    premium is (min, max) dollars per share, either side None. entry_window is
    (first session minute or None, last session minute or None). Defaults keep
    the historical book: no premium band, no entry before 15:55 only.
    """
    busy = {}
    trades = []
    attempts = []
    skips = {"skip_entry": 0, "skip_stale": 0, "skip_spot": 0, "skip_premium": 0}
    seq = 0
    bt = _bt()
    ordered = sorted(events, key=lambda e: (e["day"], e["symbol"], e["entry_min"], -e["side"]))
    for ev in ordered:
        key = (ev["day"], ev["symbol"])
        if not minute_allowed(ev["entry_min"], entry_window):
            continue
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
            if not minute_allowed(m, entry_window):
                continue
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
            trial = simulate_trade(book, m, cfg, costs, allow_slip=False, premium=premium)
            if trial["status"] == "fill":
                filled = trial
                filled["contract"] = contract
                filled["spot"] = spot
                break
            if trial["status"] in ("skip_stale", "skip_premium"):
                # A real entry print existed. A stale exit cannot be priced.
                # A premium skip is the entry print outside the band; do not slide to a later minute.
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
            "spread_cost_pct": filled.get("spread_cost_pct", float("nan")),
            "signal": signal,
            "strike": strike,
        })
    return trades, attempts, skips


def simulate_controls(controls, opt, und, cfg, costs, strike, premium=None, entry_window=None):
    """Price paired controls independently (no second one-position rule).

    Returns (trades, premium_skips). premium_skips records controls whose entry
    print fell outside the band. A control minute outside the entry window is
    not entered and is not a premium skip. Defaults match the historical book.
    """
    bt = _bt()
    trades = []
    premium_skips = []
    for ev in controls:
        if ev is None:
            continue
        if not minute_allowed(ev["entry_min"], entry_window):
            continue
        spot = None
        contract = None
        book = None
        for m in range(ev["entry_min"], min(ev["entry_min"] + ENTRY_LOOK, FLAT_MIN)):
            if not minute_allowed(m, entry_window):
                continue
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
            trial = simulate_trade(book, m, cfg, costs, allow_slip=False, premium=premium)
            if trial["status"] == "skip_premium":
                premium_skips.append({"day": ev["day"], "attempt_id": ev.get("attempt_id")})
                break
            if trial["status"] == "skip_stale":
                break
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
    return trades, premium_skips


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


def _pct_cell(share):
    if share is None or not isinstance(share, float) or not math.isfinite(share):
        return ""
    return f"{share * 100:.1f}%"


def _append_random_audit(lines, audit):
    """Diagnostics for the reference random book. Not a rank key."""
    if not audit:
        return
    lines.append("## Random baseline audit")
    lines.append("")
    lines.append(audit.get("note") or "")
    lines.append("")
    lines.append(
        "Drawn entry minutes by hour, in sample, before the one-position rule. "
        "Eligible is the count of real minutes in the allowed window (9:35-15:25, and the entry clock when set) "
        "across the same days and symbols. A uniform draw tracks that pool. "
        "Fills are not uniform: the one-position rule keeps the earlier entry and drops a later overlap, "
        "and a missing print or a premium-band skip drops a draw. Those filters are the same ones a signal book uses."
    )
    lines.append("")
    drawn = audit.get("drawn") or {}
    pool = audit.get("pool") or {}
    head = " | ".join(f"{h} ET" for h in ENTRY_HOURS)
    lines.append(f"| | {head} |")
    lines.append("|" + "|".join(["---"] * (1 + len(ENTRY_HOURS))) + "|")
    lines.append("| Drawn | " + " | ".join(str(int(drawn.get(h, 0))) for h in ENTRY_HOURS) + " |")
    lines.append("| Eligible minutes | " + " | ".join(str(int(pool.get(h, 0))) for h in ENTRY_HOURS) + " |")
    lines.append("")
    lines.append(
        "Filled reference book, in sample, 15% target, each stop, time stop 10m and 30m. "
        "Premium is the raw option open at entry. "
        "Spread % is the median round-trip half-spread (entry side plus exit side) as a percent of that premium. "
        "Flat cost % is the median net % of a round trip that sells at the same raw price, after the half-spread and the commission. "
        "Compare Net % with Flat cost %. A random mean near the flat cost is the cost model, not a second exit engine. "
        "Signal net % is the median of the in-sample search-signal means at the same strike and exit. "
        "Signal premium is the median raw entry across those signal fills. "
        "Exit shares are the fraction of random fills that left by stop, target, time, or the 15:55 flat. "
        "Fills by hour are counts from 9 ET through 15 ET."
    )
    lines.append("")
    rows = audit.get("rows") or []
    if not rows:
        lines.append("The reference book had no in-sample configs to audit.")
        lines.append("")
        return
    lines.append(
        "| Strike | SL | Time | Trades | Net % | Hit | Signal net % | Prem p10 | Prem med | Prem p90 | Signal prem | Spread % | Flat cost % | Stop | Target | Time | Flat | Fills by hour 9-15 |"
    )
    lines.append("|" + "|".join(["---"] * 18) + "|")
    for rec in rows:
        hours = rec.get("fill_hours") or {}
        hour_cell = "/".join(str(int((hours.get(h) or {}).get("n", 0))) for h in ENTRY_HOURS)
        lines.append(
            f"| {rec['strike']} | {_fmt_sl(rec['sl'])} | {rec['time_stop']}m | {rec['n']} | "
            f"{_fmt(rec['mean_net_pct'])} | {_hit(rec['hit_rate'])} | {_fmt(rec.get('signal_net'))} | "
            f"{_fmt(rec.get('p10'))} | {_fmt(rec.get('p50'))} | {_fmt(rec.get('p90'))} | {_fmt(rec.get('signal_prem'))} | "
            f"{_fmt(rec.get('spread_pct'))} | {_fmt(rec.get('flat_pct'))} | "
            f"{_pct_cell(rec.get('stop_share'))} | {_pct_cell(rec.get('tp_share'))} | "
            f"{_pct_cell(rec.get('time_share'))} | {_pct_cell(rec.get('flat_share'))} | {hour_cell} |"
        )
    lines.append("")


def _append_vix_regime(lines, regime):
    """Post-hoc prior-day VIX buckets. Not used for selection and not part of N."""
    if not regime:
        return
    lines.append("## By VIX regime")
    lines.append("")
    lines.append(regime.get("intro") or "")
    lines.append("")
    lines.append("| Signal | Strike | SL | Time | Split | Prior VIX | Trades | Hit | Net % | t |")
    lines.append("|---|---|---|---|---|---|---|---|---|---|")
    rows = regime.get("rows") or []
    if not rows:
        lines.append("| — | | | | | | | | | |")
    for rec in rows:
        split = "in-sample" if rec["split"] == "in_sample" else "held-out"
        lines.append(
            f"| {rec['signal']} | {rec['strike']} | {_fmt_sl(rec['sl'])} | {rec['time_stop']}m | {split} | "
            f"{rec['bucket']} | {rec['n']} | {_hit(rec['hit_rate'])} | {_fmt(rec['mean_net_pct'])} | {_fmt(rec['t'])} |"
        )
    lines.append("")


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
    lines.append(meta["premium_line"])
    lines.append("")
    lines.append(meta["window_line"])
    lines.append("")
    if meta.get("vix_line"):
        lines.append(meta["vix_line"])
        lines.append("")
    lines.append(
        f"Split: {meta['n_is']} in-sample day{'s' if meta['n_is'] != 1 else ''} ({meta['is_first']} to {meta['is_last']}), "
        f"{meta['n_oos']} held-out day{'s' if meta['n_oos'] != 1 else ''} ({meta['oos_first']} to {meta['oos_last']}). "
        "This 25% holdout is computed after the VIX day filter (after dead OPRA days are dropped). "
        f"The holdout section is the only place those days are scored for selection, and only for the top {TOP_K} in-sample configs of each signal."
    )
    lines.append("")
    lines.append(
        f"Search family N = {meta['n_family']} ({meta['family_note']}). "
        f"Two-sided Bonferroni bar is p < {0.05 / meta['n_family']:.6g} "
        f"(|t| > {meta['t_crit']:.2f} under a normal reference). "
        f"FDR is Benjamini-Hochberg on the finite in-sample paired-difference p-values from this run. "
        f"The random book is the control and is not part of N. "
        "The VIX regime buckets are descriptive and are not part of N."
    )
    lines.append("")
    lines.append("## Break-even hit rate")
    lines.append("")
    lines.append(
        "If a trade could only exit at the target or the stop, the hit rate that zeros expectancy is "
        "p = -net_loss / (net_win - net_loss), after the half-spread and the commission. "
        "The table uses a $2.00 premium and a $0.60 premium so the grid is comparable. "
        "Each results-csv row also has the rate at that config's own median entry open. "
        "A time stop makes the true break-even higher than this, because many trades exit before the target."
    )
    lines.append("")
    lines.append("| Target | Stop | Break-even hit rate at $2.00 | Break-even hit rate at $0.60 |")
    lines.append("|---|---|---|---|")
    for tp in TPS:
        for sl in SLS:
            p2 = breakeven_hit_rate(tp, sl, 2.0, meta["cent_floor"], meta["pct"], meta["commission"])
            p60 = breakeven_hit_rate(tp, sl, 0.60, meta["cent_floor"], meta["pct"], meta["commission"])
            sl_txt = "none" if sl is None else f"{sl * 100:.0f}%"

            def _be(p):
                return "not defined" if not math.isfinite(p) else f"{p * 100:.1f}%"

            lines.append(f"| {tp * 100:.0f}% | {sl_txt} | {_be(p2)} | {_be(p60)} |")
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
        lines.append("| Strike | TP | SL | Time | Trades | /day | Hit | Net % | $/day | Max DD $ | t | vs random net % | t diff | 95% CI | skips entry/stale/premium |")
        lines.append("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
        for r in show:
            ci = f"[{_fmt(r['boot_lo'])}, {_fmt(r['boot_hi'])}]" if math.isfinite(r["boot_lo"]) else ""
            lines.append(
                f"| {r['strike']} | {r['tp'] * 100:.0f}% | {_fmt_sl(r['sl'])} | {r['time_stop']}m | {r['n']} | "
                f"{_fmt(r['trades_per_day'])} | {_hit(r['hit_rate'])} | "
                f"{_fmt(r['mean_net_pct'])} | {_fmt(r['usd_per_day'])} | {_fmt(r['max_drawdown_usd'])} | {_fmt(r['t'])} | "
                f"{_fmt(r['random_mean_net_pct'])} | {_fmt(r['t_diff'])} | {ci} | "
                f"{r['n_skip_entry']}/{r['n_skip_stale']}/{r.get('skips_premium', 0)} |"
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
    _append_random_audit(lines, meta.get("random_audit"))
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
    lines.append("## Entry hour")
    lines.append("")
    lines.append(
        "Descriptive only, not used for selection. "
        "Mean net % and fill count by the clock hour of the entry print (ET), for the top in-sample config of each signal "
        "and for the reference random book at that same strike and exit. "
        "This split was not used to rank configs and was not used to choose the holdout. "
        "The same columns (`hour_9_n`, `hour_9_net_pct`, through hour 15) are on those rows in `results/scalp_real_results.csv`, "
        "and on every in-sample random baseline row. Other rows leave them blank. A cell is `trades / mean net %`."
    )
    lines.append("")
    hour_table = meta.get("hour_table") or []
    if not hour_table:
        lines.append("No ranked in-sample config, so there is no per-signal hour split.")
    else:
        head = " | ".join(f"{h} ET" for h in ENTRY_HOURS)
        lines.append(f"| Book | Signal | Strike | TP | SL | Time | {head} |")
        lines.append("|" + "|".join(["---"] * (6 + len(ENTRY_HOURS))) + "|")
        for rec in hour_table:
            cells = []
            for h in ENTRY_HOURS:
                slot = rec["hours"].get(h) or {"n": 0, "net_pct": float("nan")}
                if slot["n"]:
                    cells.append(f"{slot['n']} / {_fmt(slot['net_pct'])}")
                else:
                    cells.append("0")
            lines.append(
                f"| {rec['book']} | {rec['signal']} | {rec['strike']} | {rec['tp'] * 100:.0f}% | "
                f"{_fmt_sl(rec['sl'])} | {rec['time_stop']}m | " + " | ".join(cells) + " |"
            )
    lines.append("")
    _append_vix_regime(lines, meta.get("vix_regime"))
    lines.append("## How to read a pass")
    lines.append("")
    lines.append(
        "A config is interesting only if the in-sample paired difference beats the Bonferroni or FDR bar **and** the holdout "
        "mean is still positive against its own random book. Anything short of that is a description of this sample, not an edge. "
        "The By VIX regime table is one of those descriptions: post-hoc buckets, not a selected result. "
        "0DTE spreads are often wider than the half-spread assumed here; when they are, the break-even hit rate moves up."
    )
    lines.append("")
    lines.append(
        "Skipped entries with no print within 2 minutes, exits skipped as stale, and entry prints outside the premium band "
        f"(skips_premium) are columns in the csv. {meta['skip_note']}"
    )
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


def _env_optional_float(name):
    raw = os.getenv(name, "").strip()
    if not raw:
        return None
    try:
        return float(raw)
    except ValueError:
        sys.exit(f"{name} must be a number, or empty")


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
        "skip_premium": sum(1 for a in att if a["status"] == "skip_premium"),
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
        "skips_premium": skips.get("skip_premium", 0),
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
    premium_min = _env_optional_float("SCALP_PREMIUM_MIN")
    premium_max = _env_optional_float("SCALP_PREMIUM_MAX")
    if premium_min is not None and premium_min < 0:
        sys.exit("SCALP_PREMIUM_MIN cannot be negative")
    if premium_max is not None and premium_max < 0:
        sys.exit("SCALP_PREMIUM_MAX cannot be negative")
    if premium_min is not None and premium_max is not None and premium_min > premium_max:
        sys.exit("SCALP_PREMIUM_MIN cannot be above SCALP_PREMIUM_MAX")
    premium = None if premium_min is None and premium_max is None else (premium_min, premium_max)
    first_label, first_min = parse_clock_et(os.getenv("SCALP_FIRST_ENTRY", ""), "SCALP_FIRST_ENTRY")
    last_label, last_min = parse_clock_et(os.getenv("SCALP_LAST_ENTRY", ""), "SCALP_LAST_ENTRY")
    entry_window = None if first_min is None and last_min is None else (first_min, last_min)
    vix_min, vix_max = parse_vix_band(
        _env_optional_float("SCALP_VIX_MIN"),
        _env_optional_float("SCALP_VIX_MAX"),
    )
    _print_scrubbed("fetching prior-day VIX closes (FRED VIXCLS, Yahoo ^VIX, Cboe, data/vix_daily.csv)")
    vix_closes, vix_source = fetch_vix_closes()
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
    vix_closes, vix_source = apply_vix_coverage(vix_closes, candidate, vix_source)
    _print_scrubbed(f"VIX source {vix_source} closes {len(vix_closes)}")

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
    ref_events = reference_random_events(signal_events, und, symbols, candidate, entry_window)

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
    signal_live = {sid: _filter_days(evs, live_set) for sid, evs in signal_events.items()}
    # Unfiltered by VIX. The regime table and the contract set use this book.
    ref_live = reference_random_events(signal_live, und, symbols, live, entry_window)
    kept, vix_dropped = filter_days_by_vix(live, vix_closes, vix_min, vix_max)
    _print_scrubbed(f"VIX day filter kept {len(kept)} dropped {len(vix_dropped)} of {len(live)} OPRA days")
    if not kept:
        text = (
            "# 0DTE scalp on real option prints\n\n"
            f"VIX day filter kept 0 of {len(live)} OPRA days ({vix_source}). Nothing was scored.\n"
            "Data only. Research tool, not trading advice.\n"
        )
        _write_text(os.path.join(out_dir, "SCALP_REAL.md"), text)
        sys.exit("VIX day filter left no sessions.")
    kept_set = set(kept)
    # Same days for signals, paired controls (they follow the attempts), and the reference book.
    signal_events = {sid: _filter_days(evs, kept_set) for sid, evs in signal_live.items()}
    ref_events = _filter_days(ref_live, kept_set)
    # 25% holdout AFTER the day filter. The regime section splits the unfiltered OPRA days on its own.
    is_days, oos_days = _split(kept)
    reg_is, reg_oos = _split(live)
    is_set, oos_set = set(is_days), set(oos_days)
    priors = prior_vix_by_day(live, vix_closes)

    # Pass 1 already fetched signal + reference contracts on the original candidate set.
    # Reference events on live days use the same per-day seed, so those contracts are present.
    books = {}
    attempts_by = {}
    for sid in list(SEARCH_IDS) + ["random"]:
        evs = ref_events if sid == "random" else signal_events[sid]
        for strike in strikes:
            for tp, sl, ts in ((tp, sl, ts) for tp in TPS for sl in SLS for ts in TIME_STOPS):
                trades, attempts, _skips = run_book(
                    evs, opt, und, strike, (tp, sl, ts), costs, sid,
                    premium=premium, entry_window=entry_window,
                )
                key = (sid, strike, tp, sl, ts)
                books[key] = trades
                attempts_by[key] = attempts

    # Regime rows do not use the VIX day filter. When the filter is off, the study
    # books are already the full OPRA set. When it is on, reprice the 15% slice
    # on the unfiltered days. Premium band and entry clock still apply.
    regime_signals = list(SEARCH_IDS) + ["random"]
    if vix_min is None and vix_max is None:
        regime_books = books
    else:
        regime_books = {}
        for sid in regime_signals:
            evs = ref_live if sid == "random" else signal_live[sid]
            for strike in strikes:
                for sl in SLS:
                    for ts in REGIME_TIME_STOPS:
                        trades, _attempts, _skips = run_book(
                            evs, opt, und, strike, (REGIME_TP, sl, ts), costs, sid,
                            premium=premium, entry_window=entry_window,
                        )
                        regime_books[(sid, strike, REGIME_TP, sl, ts)] = trades

    # Paired controls, then a second fetch for any contract the first pass did not load.
    controls = {}
    extra = {}
    for key, attempts in attempts_by.items():
        sid, strike, tp, sl, ts = key
        if sid == "random":
            continue
        drawn = []
        for att in attempts:
            ev = paired_entry(att, und, entry_window)
            drawn.append(ev)
        controls[key] = drawn
        for ev in drawn:
            if ev is None:
                continue
            if not minute_allowed(ev["entry_min"], entry_window):
                continue
            for m in range(ev["entry_min"], min(ev["entry_min"] + ENTRY_LOOK, FLAT_MIN)):
                if not minute_allowed(m, entry_window):
                    continue
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
    control_premium_skips = {}
    for key, drawn in controls.items():
        sid, strike, tp, sl, ts = key
        filled, prem_skips = simulate_controls(
            [e for e in drawn if e is not None], opt, und, (tp, sl, ts), costs, strike,
            premium=premium, entry_window=entry_window,
        )
        control_trades[key] = filled
        control_premium_skips[key] = prem_skips

    def skips_with_controls(key, days):
        skips = _skips_for(attempts_by[key], days)
        want = set(days)
        extra = sum(1 for s in control_premium_skips.get(key, []) if s["day"] in want)
        skips["skip_premium"] = skips.get("skip_premium", 0) + extra
        return skips

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
            skips = skips_with_controls(key, days)
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
    n_family = search_config_count(strikes)
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
                                    stats, skips_with_controls(key, oos_days), len(oos_days), costs, True)
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

    # Entry-hour columns are descriptive. They are filled for the top in-sample config of each
    # signal and for every in-sample random baseline row. They are not a rank key.
    hour_lookup = {}
    for key, trades in books.items():
        sid, strike, tp, sl, ts = key
        if sid != "random":
            continue
        hour_lookup[(sid, strike, tp, sl, ts, "in_sample")] = entry_hour_breakdown(split_trades(trades, is_days))
    hour_table = []
    for sid in SEARCH_IDS:
        # The selected top when one qualifies; otherwise the leading in-sample row.
        # The hour split is not an input to either choice.
        best = next((rec["is"] for rec in tops if rec["is"]["signal"] == sid), None)
        if best is None:
            mine = [r for r in is_search_rows if r["signal"] == sid and math.isfinite(r["t_diff"])]
            mine.sort(key=lambda r: (r["t_diff"], r["mean_net_pct"] if math.isfinite(r["mean_net_pct"]) else -1e9, r["n"]),
                      reverse=True)
            best = mine[0] if mine else None
        if best is None:
            continue
        key = (best["signal"], best["strike"], best["tp"], best["sl"], best["time_stop"])
        sig_hours = entry_hour_breakdown(split_trades(books[key], is_days))
        hour_lookup[(*key, "in_sample")] = sig_hours
        hour_table.append({
            "book": "signal", "signal": best["signal"], "strike": best["strike"],
            "tp": best["tp"], "sl": best["sl"], "time_stop": best["time_stop"], "hours": sig_hours,
        })
        ref_key = ("random", key[1], key[2], key[3], key[4])
        ref_hours = hour_lookup.get((*ref_key, "in_sample"))
        if ref_hours is not None:
            hour_table.append({
                "book": "random", "signal": "random", "strike": ref_key[1],
                "tp": ref_key[2], "sl": ref_key[3], "time_stop": ref_key[4], "hours": ref_hours,
            })

    # FDR / bonferroni stay blank on holdout rows (they were not part of the family correction).
    csv_rows = []
    for r in rows:
        hour_kwargs = {}
        breakdown = hour_lookup.get((r["signal"], r["strike"], r["tp"], r["sl"], r["time_stop"], r["split"]))
        if breakdown:
            for h, slot in breakdown.items():
                hour_kwargs[f"hour_{h}_n"] = slot["n"]
                hour_kwargs[f"hour_{h}_net_pct"] = slot["net_pct"] if slot["n"] else ""
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
            skips_premium=r["skips_premium"], **hour_kwargs,
        ))

    entry_skips = sum(r["n_skip_entry"] for r in is_search_rows)
    stale_skips = sum(r["n_skip_stale"] for r in is_search_rows)
    prem_skips = sum(r["skips_premium"] for r in is_search_rows)
    attempts = sum(r["n_attempts"] for r in is_search_rows)
    skip_note = (
        f"Across the in-sample search grid (each exit is its own book, so the same signal is counted once per exit): "
        f"{entry_skips} entry skips, {stale_skips} stale-exit skips, and {prem_skips} skips_premium "
        f"out of {attempts} one-position attempts. "
        "On a search row, skips_premium counts that signal's premium skips plus paired controls outside the band."
    )
    t_crit = norm_ppf(1 - (0.05 / n_family) / 2)
    vix_line = describe_vix_filter(vix_min, vix_max, kept, vix_dropped, vix_source, len(is_days), len(oos_days))
    n_missing_prior = sum(1 for day in live if priors.get(day) is None)
    regime_payload = {
        "intro": regime_intro(
            len(live), reg_is, reg_oos, n_missing_prior, len(kept), len(vix_dropped),
            len(is_days), len(oos_days), n_family, vix_min is not None or vix_max is not None,
        ),
        "rows": regime_rows(
            regime_books,
            [("in_sample", reg_is), ("holdout", reg_oos)],
            priors,
            regime_signals,
            strikes,
        ),
    }
    audit_rows = []
    for strike in strikes:
        for sl in SLS:
            for ts in REGIME_TIME_STOPS:
                rnd_trades = split_trades(books.get(("random", strike, REGIME_TP, sl, ts), []), is_days)
                stats = summarize(rnd_trades, is_days, 0, 0)
                fill = audit_fill_stats(rnd_trades, costs)
                sig_nets = []
                sig_prems = []
                for sid in SEARCH_IDS:
                    sig_trades = split_trades(books.get((sid, strike, REGIME_TP, sl, ts), []), is_days)
                    if not sig_trades:
                        continue
                    sig_nets.append(float(np.mean([t["net_pct"] for t in sig_trades])))
                    sig_prems.extend(float(t["raw_entry"]) for t in sig_trades if math.isfinite(float(t["raw_entry"])))
                audit_rows.append({
                    "strike": strike,
                    "sl": sl,
                    "time_stop": ts,
                    "n": stats["n"],
                    "mean_net_pct": stats["mean_net_pct"],
                    "hit_rate": stats["hit_rate"],
                    "signal_net": float(np.median(sig_nets)) if sig_nets else float("nan"),
                    "signal_prem": float(np.median(sig_prems)) if sig_prems else float("nan"),
                    "fill_hours": entry_hour_breakdown(rnd_trades),
                    **fill,
                })
    drawn_hours, pool_hours = hour_draw_table(ref_events, und, symbols, is_days, entry_window)
    random_audit = {
        "note": (
            "The reference random book is the baseline, not a search signal. "
            "Bug fixed in this version: minutes used to be drawn from all of 9:35-15:25, and a minute outside "
            "SCALP_FIRST_ENTRY / SCALP_LAST_ENTRY was dropped afterward. With a late window that threw away most draws, "
            "the book was a thinned leftover rather than N uniform entries inside the window the signals may trade. "
            "Draws are now uniform on the intersection of 9:35-15:25 and that clock. "
            "Fills and exits go through run_book and simulate_trade, the same functions a signal trade uses. "
            "No separate fill bug was found. "
            "This audit is descriptive. It is not used to rank configs and it is not part of N."
        ),
        "drawn": drawn_hours,
        "pool": pool_hours,
        "rows": audit_rows,
    }
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
        "family_note": family_note(strikes),
        "premium_line": describe_premium(premium),
        "window_line": describe_window(first_label, last_label),
        "vix_line": vix_line,
        "vix_regime": regime_payload,
        "random_audit": random_audit,
        "hour_table": hour_table,
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
