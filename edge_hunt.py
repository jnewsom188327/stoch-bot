"""
Walk-forward search for 0DTE SPY/QQQ long-premium edges on real option prices.

DATA ONLY. This script reads historical bars. It does not import an order
client, submit orders, or send a trade. It is a research tool, not trading advice.

The supported run is .github/workflows/edge_hunt.yml (Actions tab,
"Edge hunt (walk-forward, real option prices)", Run workflow). A fresh run,
not Re-run. Keys come from the ALPACA_KEY and ALPACA_SECRET secrets and are
never printed.

Outputs:
    results/EDGE_HUNT.md
    results/edge_hunt_rules.csv
    results/edge_hunt_trades.csv

Fills, costs, strike math, and option downloads are reused from scalp_real.py.
This file does not modify that module.
"""

from __future__ import annotations

import bisect
import csv
import math
import os
import pickle
import threading
import time
import urllib.error
import urllib.request
import warnings
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd

import scalp_real as sc

NY = sc.NY
N_MIN = sc.N_MIN
FLAT_MIN = sc.FLAT_MIN
FIRST_ENTRY = 15          # 9:45 ET. Opening range (9:30-9:44) is known.
LAST_ENTRY = FLAT_MIN - 1  # 15:54. No new entry at or after 15:55.
COOLDOWN = 10
K_FOLDS = 5
SEED = 20261025
MIN_TRAIN = 20
MIN_QUANTILE_N = 40
N_SHUFFLE = 200
BOOT_N = 1000
RVOL_MIN = 1.5
PIVOT_LEFT = 5
PIVOT_RIGHT = 5

# Threshold grids. Ordered loose to tight so a tie keeps the looser cut.
HIGH_QS = (0.60, 0.75, 0.90)
LOW_QS = (0.40, 0.25, 0.10)
MAG_QS = (0.60, 0.75, 0.90)
STRETCHES = (1.0, 1.5, 2.0)
WVF_LEVELS = (60.0, 75.0, 90.0)

EXITS = tuple(
    (tp, sl, ts)
    for tp in (0.10, 0.15, 0.20)
    for sl in (0.10, 0.20, None)
    for ts in (10, 30)
)
# Thresholds are chosen on this exit. Every exit is still scored and is in the FDR family.
PRIMARY_EXIT = (0.15, 0.20, 10)
PRIMARY_I = EXITS.index(PRIMARY_EXIT)

DAILY_FEATURES = (
    "vix_prior", "vix_chg_5d", "gap_pct", "gap_vs_range",
    "prior_range_pct", "prior_close_pos", "or_size", "dow",
)
LEVEL_DAILY = (
    "vix_prior", "vix_chg_5d", "gap_pct", "gap_vs_range",
    "prior_range_pct", "prior_close_pos", "or_size",
)
LEVEL_INTRA = (
    "vwap_atr", "ret_5", "ret_15", "ret_30", "rvol",
    "wvf_1m", "wvf_3m", "squeeze_bars", "ema_slope",
)
SIGNED_DAILY = ("gap_pct", "gap_vs_range", "vix_chg_5d")
SIGNED_INTRA = ("vwap_atr", "ret_5", "ret_15", "ret_30", "ema_slope", "or_break")

# Events whose direction is known at the signal bar (no extra threshold).
FIXED_EVENTS = (
    "macd_zero_1m", "macd_shrink_1m", "macd_flip_1m",
    "macd_zero_3m", "macd_shrink_3m", "macd_flip_3m",
    "div_1m", "div_3m", "div_5m",
    "swing_1m", "swing_3m",
    "sq_release_1m", "sq_release_3m",
)
# Threshold is chosen on the training window from a fixed grid.
GRID_EVENTS = (
    "vwap_rvol",
    "wvf_roll_1m", "wvf_roll_3m",
    "wvi_roll_1m", "wvi_roll_3m",
)
TOD_BUCKETS = tuple(range(0, 13))  # 9:30-9:59 ... 15:30-15:59

# Intraday gates paired with reversal events. Not a full cross of every feature.
INTRA_GATES = (
    ("rvol", "high", "intra_level"),
    ("wvf_1m", "high", "intra_level"),
    ("wvf_3m", "high", "intra_level"),
    ("squeeze_bars", "high", "intra_level"),
    ("vwap_atr", "mag", "mag"),
    ("ema_slope", "mag", "mag"),
    ("ret_5", "mag", "mag"),
    ("squeeze_on", "on", "flag"),
)

EVENT_SOURCES = {
    "macd_zero_1m": frozenset({"macd_1m"}),
    "macd_shrink_1m": frozenset({"macd_1m"}),
    "macd_flip_1m": frozenset({"macd_1m"}),
    "macd_zero_3m": frozenset({"macd_3m"}),
    "macd_shrink_3m": frozenset({"macd_3m"}),
    "macd_flip_3m": frozenset({"macd_3m"}),
    "div_1m": frozenset({"div_1m"}),
    "div_3m": frozenset({"div_3m"}),
    "div_5m": frozenset({"div_5m"}),
    "swing_1m": frozenset({"swing_1m"}),
    "swing_3m": frozenset({"swing_3m"}),
    "sq_release_1m": frozenset({"squeeze_on", "squeeze_bars"}),
    "sq_release_3m": frozenset({"squeeze_on", "squeeze_bars"}),
    "vwap_rvol": frozenset({"vwap_atr", "rvol"}),
    "wvf_roll_1m": frozenset({"wvf_1m"}),
    "wvf_roll_3m": frozenset({"wvf_3m"}),
    "wvi_roll_1m": frozenset({"wvi_1m"}),
    "wvi_roll_3m": frozenset({"wvi_3m"}),
}

RULE_FIELDS = [
    "rule_id", "name", "kind", "strike", "tp", "sl", "time_stop",
    "n", "hit_rate", "mean_net_pct", "t", "p", "q_fdr",
    "boot_lo", "boot_hi", "folds_positive", "fold_means",
    "random_n", "random_mean_net_pct", "random_hit_rate",
    "beats_random", "candidate", "sensitive", "train_params",
]
TRADE_FIELDS = [
    "date", "time", "symbol", "side", "entry", "exit", "reason", "net_pct",
    "rule_id", "rule", "strike", "tp", "sl", "time_stop", "book", "contract", "fold",
]

FRED_VIX_URL = "https://fred.stlouisfed.org/graph/fredgraph.csv?id=VIXCLS"


# -------------------------------------------------------------------------------- pure stats


def walk_forward_folds(n_days, k=K_FOLDS):
    """K out-of-sample folds on a chronological split, expanding train.

    Days are cut into k+1 blocks. Block 0 is train only. Fold i tests block i+1
    and trains on every block before it. Every training day is strictly before
    that fold's first test day. Returns a list of (train_idx, test_idx) int arrays.
    """
    if k < 1:
        raise ValueError("k must be positive")
    if n_days < k + 1:
        raise ValueError(f"need at least {k + 1} sessions for {k} out-of-sample folds, got {n_days}")
    n_blocks = k + 1
    base, rem = divmod(int(n_days), n_blocks)
    sizes = [base + (1 if i < rem else 0) for i in range(n_blocks)]
    if any(s < 1 for s in sizes):
        raise ValueError("fold blocks would be empty")
    edges = np.cumsum([0] + sizes)
    folds = []
    for t in range(1, n_blocks):
        train = np.arange(0, int(edges[t]))
        test = np.arange(int(edges[t]), int(edges[t + 1]))
        folds.append((train, test))
    return folds


def fdr_qvalues(pvals, family_n=None):
    """Benjamini-Hochberg q-values.

    With family_n omitted, this matches scalp_real.benjamini_hochberg (N = number
    of finite p-values). With family_n set, N is at least that family size.
    Non-finite p-values are treated as 1 so an unscored rule still uses a slot.
    """
    p = np.asarray(pvals, dtype=float)
    if family_n is None:
        return sc.benjamini_hochberg(p)
    if len(p) == 0:
        return p.copy()
    vals = np.where(np.isfinite(p), p, 1.0)
    n = max(int(family_n), len(vals))
    order = np.argsort(vals, kind="mergesort")
    ranked = vals[order]
    q = ranked * (n / np.arange(1, len(ranked) + 1))
    q = np.minimum.accumulate(q[::-1])[::-1]
    np.clip(q, 0.0, 1.0, out=q)
    placed = np.empty(len(ranked), dtype=float)
    placed[order] = q
    return placed


def luck_shuffle_benchmark(per_shuffle_best, per_shuffle_n_as_good):
    """Summarize the day-label shuffle null.

    per_shuffle_best: best out-of-sample mean net in that shuffle.
    per_shuffle_n_as_good: how many rules in that shuffle reached the real best.
    The luck benchmark reported to the phone is the best (maximum) of the
    per-shuffle bests. The expected count is the mean of the per-shuffle counts.
    """
    best = np.asarray(per_shuffle_best, dtype=float)
    counts = np.asarray(per_shuffle_n_as_good, dtype=float)
    if len(best) == 0:
        return {
            "n_shuf": 0,
            "best_oos_net": float("nan"),
            "median_best_oos_net": float("nan"),
            "expected_rules_as_good": float("nan"),
        }
    return {
        "n_shuf": int(len(best)),
        "best_oos_net": float(np.nanmax(best)),
        "median_best_oos_net": float(np.nanmedian(best)),
        "expected_rules_as_good": float(np.nanmean(counts)) if len(counts) else float("nan"),
    }


def day_label_permutations(n_days, n_shuf, seed):
    """Each row is a permutation of 0..n_days-1. Row i reassigns daily features."""
    rng = np.random.default_rng(int(seed) + 17)
    out = np.empty((int(n_shuf), int(n_days)), dtype=int)
    for i in range(int(n_shuf)):
        out[i] = rng.permutation(int(n_days))
    return out


def clustered_t_from_days(sums, cnts):
    """Day-clustered t of the per-trade mean, from per-day sums and counts.

    Same estimator as scalp_real.clustered_t. Empty days add nothing.
    """
    sums = np.asarray(sums, dtype=float)
    cnts = np.asarray(cnts, dtype=float)
    n = float(cnts.sum())
    if n < 2 or int((cnts > 0).sum()) < 2:
        return float("nan"), float("nan")
    mu = float(sums.sum() / n)
    resid = sums - cnts * mu
    se = math.sqrt(float((resid ** 2).sum())) / n
    if not math.isfinite(se) or se <= 1e-9 * max(1.0, abs(mu)):
        return float("nan"), float("nan")
    t = mu / se
    return t, sc.norm_sf(t)


def cooldown_indices(call, put, gap=COOLDOWN):
    """Keep entries at least `gap` minutes apart, per day and symbol.

    call/put are boolean (days, symbols, minutes) on the ENTRY clock.
    A minute where both are true takes the call and starts the cooldown.
    Returns day, sym, minute, side (0 call, 1 put) int arrays.
    """
    call = np.asarray(call, dtype=bool)
    put = np.asarray(put, dtype=bool)
    d_n, s_n, m_n = call.shape
    n = d_n * s_n
    c = call.reshape(n, m_n)
    p = put.reshape(n, m_n)
    want = c | p
    last = np.full(n, -10_000, dtype=np.int32)
    kept = np.full((n, m_n), -1, dtype=np.int8)
    for m in range(m_n):
        can = want[:, m] & ((m - last) >= gap)
        is_c = can & c[:, m]
        is_p = can & ~c[:, m] & p[:, m]
        took = is_c | is_p
        kept[is_c, m] = 0
        kept[is_p, m] = 1
        last = np.where(took, m, last)
    series, minutes = np.nonzero(kept >= 0)
    day = (series // s_n).astype(np.int32)
    sym = (series % s_n).astype(np.int32)
    side = kept[series, minutes].astype(np.int8)
    return day, sym, minutes.astype(np.int32), side


def shift_signal(sig):
    """Move a signal-bar mask onto the next minute and clip to the entry window.

    sig True at bar m means the bar's close is known and the entry is m+1.
    """
    sig = np.asarray(sig, dtype=bool)
    out = np.zeros_like(sig)
    out[:, :, 1:] = sig[:, :, :-1]
    out[:, :, :FIRST_ENTRY] = False
    if LAST_ENTRY + 1 < out.shape[-1]:
        out[:, :, LAST_ENTRY + 1:] = False
    return out


# -------------------------------------------------------------------------------- pivots and reversal events


def confirmed_pivots(high, low, left=PIVOT_LEFT, right=PIVOT_RIGHT):
    """Swing pivots confirmed only after `right` bars exist on the right.

    A low at index p is confirmed at index p+right, and only if low[p] is
    strictly below every other bar in [p-left, p+right]. The flag is False at p.
    Bars after the confirmation index are not read.
    Returns (low_confirmed, high_confirmed) boolean arrays.
    """
    high = np.asarray(high, dtype=float)
    low = np.asarray(low, dtype=float)
    n = len(low)
    lo = np.zeros(n, dtype=bool)
    hi = np.zeros(n, dtype=bool)
    if left < 1 or right < 1:
        raise ValueError("pivot wings must be positive")
    for p in range(left, n - right):
        i = p + right
        lw = low[p - left:p + right + 1]
        hw = high[p - left:p + right + 1]
        if np.all(np.isfinite(lw)) and low[p] < lw[:left].min() and low[p] < lw[left + 1:].min():
            lo[i] = True
        if np.all(np.isfinite(hw)) and high[p] > hw[:left].max() and high[p] > hw[left + 1:].max():
            hi[i] = True
    return lo, hi


def pivot_direction(high, low, left=PIVOT_LEFT, right=PIVOT_RIGHT):
    """+1 confirmed swing low (bullish pivot), -1 confirmed swing high, else 0.

    The value sits on the confirmation bar, not the pivot bar. Both on one bar -> 0.
    """
    lo, hi = confirmed_pivots(high, low, left, right)
    out = np.zeros(len(low), dtype=np.int8)
    out[lo & ~hi] = 1
    out[hi & ~lo] = -1
    return out


def regular_divergence(high, low, hist, left=PIVOT_LEFT, right=PIVOT_RIGHT):
    """Regular divergence, flagged on the confirmation bar of the second pivot.

    Bullish: price lower low, MACD histogram higher low. Bearish: price higher
    high, histogram lower high. Histogram values are taken at the pivot bars,
    which are `right` bars before each confirmation, so both are already known.
    Returns (bull, bear) boolean arrays.
    """
    high = np.asarray(high, dtype=float)
    low = np.asarray(low, dtype=float)
    hist = np.asarray(hist, dtype=float)
    lo, hi = confirmed_pivots(high, low, left, right)
    n = len(low)
    bull = np.zeros(n, dtype=bool)
    bear = np.zeros(n, dtype=bool)
    last_lo = None
    last_hi = None
    for i in range(n):
        if lo[i]:
            p = i - right
            price = float(low[p])
            hv = float(hist[p]) if p < len(hist) else float("nan")
            if last_lo is not None and math.isfinite(hv) and math.isfinite(last_lo[1]):
                if price < last_lo[0] and hv > last_lo[1]:
                    bull[i] = True
            if math.isfinite(price) and math.isfinite(hv):
                last_lo = (price, hv)
        if hi[i]:
            p = i - right
            price = float(high[p])
            hv = float(hist[p]) if p < len(hist) else float("nan")
            if last_hi is not None and math.isfinite(hv) and math.isfinite(last_hi[1]):
                if price > last_hi[0] and hv < last_hi[1]:
                    bear[i] = True
            if math.isfinite(price) and math.isfinite(hv):
                last_hi = (price, hv)
    return bull, bear


def divergence_direction(high, low, hist, left=PIVOT_LEFT, right=PIVOT_RIGHT):
    bull, bear = regular_divergence(high, low, hist, left, right)
    out = np.zeros(len(low), dtype=np.int8)
    out[bull & ~bear] = 1
    out[bear & ~bull] = -1
    return out


def macd_histogram(close):
    """MACD(12, 26, 9) histogram. Causal: bar i uses closes through i."""
    s = pd.Series(np.asarray(close, dtype=float))
    ema12 = s.ewm(span=12, adjust=False).mean()
    ema26 = s.ewm(span=26, adjust=False).mean()
    macd = ema12 - ema26
    signal = macd.ewm(span=9, adjust=False).mean()
    return (macd - signal).to_numpy(dtype=float)


def macd_event_directions(hist):
    """Zero-cross, shrink, and color-flip directions at the bar they become known.

    zero: +1 when the histogram crosses from <=0 to >0, -1 the other way.
    shrink: histogram keeps its sign and |hist| falls. Direction is that sign
    (the side that is fading).
    flip: the one-bar slope of the histogram changes sign. Direction is the new slope.
    Returns three int8 arrays.
    """
    h = np.asarray(hist, dtype=float)
    n = len(h)
    zero = np.zeros(n, dtype=np.int8)
    shrink = np.zeros(n, dtype=np.int8)
    flip = np.zeros(n, dtype=np.int8)
    for i in range(1, n):
        a, b = h[i - 1], h[i]
        if not (math.isfinite(a) and math.isfinite(b)):
            continue
        if a <= 0.0 and b > 0.0:
            zero[i] = 1
        elif a >= 0.0 and b < 0.0:
            zero[i] = -1
        if a * b > 0.0 and abs(b) < abs(a):
            shrink[i] = 1 if b > 0.0 else -1
    for i in range(2, n):
        d0 = h[i - 1] - h[i - 2]
        d1 = h[i] - h[i - 1]
        if not (math.isfinite(d0) and math.isfinite(d1)):
            continue
        if d0 * d1 < 0.0 and d1 != 0.0:
            flip[i] = 1 if d1 > 0.0 else -1
    return zero, shrink, flip


def wvf_rollover_mask(wvf, level):
    """True at i when bar i-1 was a local VIX-fix spike at or above `level` and bar i fell.

    Uses wvf[i], wvf[i-1], wvf[i-2] only. The spike bar itself is not a signal.
    """
    w = np.asarray(wvf, dtype=float)
    prev = np.full(w.shape, np.nan)
    prev2 = np.full(w.shape, np.nan)
    prev[..., 1:] = w[..., :-1]
    prev2[..., 2:] = w[..., :-2]
    return (prev >= float(level)) & (w < prev) & (prev >= prev2) & np.isfinite(w)


def squeeze_release_direction(on, mom):
    """Squeeze release plus a momentum color flip, at the release bar.

    on[i] True means the squeeze is on at i. A release is on[i-1] and not on[i].
    Color flip: (mom[i] - mom[i-1]) has the opposite sign of (mom[i-1] - mom[i-2]).
    Direction is the sign of mom[i] when that is nonzero, else the new slope.
    """
    flag = np.asarray(on, dtype=bool)
    m = np.asarray(mom, dtype=float)
    out = np.zeros(len(m), dtype=np.int8)
    for i in range(2, len(m)):
        if not (flag[i - 1] and not flag[i]):
            continue
        d0 = m[i - 1] - m[i - 2]
        d1 = m[i] - m[i - 1]
        if not (math.isfinite(d0) and math.isfinite(d1)) or d0 * d1 >= 0.0:
            continue
        if math.isfinite(m[i]) and m[i] != 0.0:
            out[i] = 1 if m[i] > 0.0 else -1
        elif d1 != 0.0:
            out[i] = 1 if d1 > 0.0 else -1
    return out


def vwap_rvol_direction(vwap_atr, rvol, stretch, rvol_min=RVOL_MIN):
    """Direction of a VWAP stretch that also has a volume spike.

    +1 when price is at least `stretch` ATRs above VWAP and relative volume
    is at least rvol_min. -1 when the stretch is below VWAP. 0 otherwise.
    The 1.5x volume floor is fixed. `stretch` is the trained parameter.
    """
    dist = np.asarray(vwap_atr, dtype=float)
    rv = np.asarray(rvol, dtype=float)
    ok = (np.abs(dist) >= float(stretch)) & (rv >= float(rvol_min)) & np.isfinite(dist)
    out = np.zeros(dist.shape, dtype=np.int8)
    out[ok & (dist > 0)] = 1
    out[ok & (dist < 0)] = -1
    return out


def asof_known(bar_end_ns, known_ns, values):
    """Last value whose known time is <= each bar end. No value from the future.

    bar_end_ns, known_ns: int64 nanoseconds. values aligns with known_ns.
    A bar whose end is strictly before the value's known time gets NaN.
    """
    known = np.asarray(known_ns, dtype=np.int64)
    vals = np.asarray(values, dtype=float)
    order = np.argsort(known, kind="mergesort")
    known = known[order]
    vals = vals[order]
    idx = np.searchsorted(known, np.asarray(bar_end_ns, dtype=np.int64), side="right") - 1
    out = np.full(len(bar_end_ns), np.nan, dtype=float)
    ok = idx >= 0
    out[ok] = vals[idx[ok]]
    return out


def _run_length(flag):
    flag = np.asarray(flag, dtype=bool)
    out = np.zeros(len(flag), dtype=np.int32)
    n = 0
    for i, v in enumerate(flag):
        n = n + 1 if v else 0
        out[i] = n
    return out


def _last_finite(row):
    finite = np.isfinite(row)
    if not finite.any():
        return float("nan")
    return float(row[np.nonzero(finite)[0][-1]])


def relative_volume(volume, window=20):
    """volume[day, minute] / median of that minute on the previous `window` days.

    Today's volume is the numerator only. Later days are not in the median.
    """
    vol = np.asarray(volume, dtype=float)
    d_n, m_n = vol.shape
    out = np.full((d_n, m_n), np.nan)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=RuntimeWarning)
        for i in range(1, d_n):
            sl = vol[max(0, i - window):i]
            med = np.nanmedian(sl, axis=0)
            good = np.isfinite(med) & (med > 0) & np.isfinite(vol[i])
            out[i, good] = vol[i, good] / med[good]
    return out


def prior_vix_features(days, vix_closes):
    """Prior-day VIX close and (that close minus the mean of the 5 closes before the session).

    vix_closes maps the calendar date of the VIX close to its value. Session D
    sees only dates strictly before D. Fewer than 5 prior closes -> change is NaN.
    """
    items = []
    for key, val in dict(vix_closes).items():
        if isinstance(key, datetime):
            key = key.date()
        elif isinstance(key, pd.Timestamp):
            key = key.date()
        try:
            fv = float(val)
        except (TypeError, ValueError):
            continue
        if math.isfinite(fv):
            items.append((key, fv))
    items.sort()
    dates = [d for d, _ in items]
    vals = np.array([v for _, v in items], dtype=float)
    prior = np.full(len(days), np.nan)
    chg = np.full(len(days), np.nan)
    for i, day in enumerate(days):
        j = bisect.bisect_left(dates, day) - 1
        if j < 0:
            continue
        prior[i] = vals[j]
        if j >= 4:
            chg[i] = vals[j] - float(vals[j - 4:j + 1].mean())
    return prior, chg


def daily_price_context(opens, highs, lows, closes):
    """Session context from prior-day OHLC and today's open. No later bar of today.

    opens/highs/lows/closes: (days, minutes) regular-session arrays.
    or_size uses today's first 15 minutes only (9:30-9:44). It does not use minute 15+.
    gap uses today's 9:30 open and the prior session's last finite close.
    """
    opens = np.asarray(opens, dtype=float)
    highs = np.asarray(highs, dtype=float)
    lows = np.asarray(lows, dtype=float)
    closes = np.asarray(closes, dtype=float)
    d_n = closes.shape[0]
    gap = np.full(d_n, np.nan)
    gap_vs = np.full(d_n, np.nan)
    prange = np.full(d_n, np.nan)
    cpos = np.full(d_n, np.nan)
    or_size = np.full(d_n, np.nan)
    for i in range(d_n):
        h15 = highs[i, :15]
        l15 = lows[i, :15]
        if h15.size >= 15 and np.isfinite(h15).all() and np.isfinite(l15).all():
            op = opens[i, 0]
            if math.isfinite(op) and op != 0:
                or_size[i] = (float(h15.max()) - float(l15.min())) / op
        if i == 0:
            continue
        prev_c = _last_finite(closes[i - 1])
        if not (np.isfinite(highs[i - 1]).any() and np.isfinite(lows[i - 1]).any()):
            continue
        prev_h = float(np.nanmax(highs[i - 1]))
        prev_l = float(np.nanmin(lows[i - 1]))
        op = opens[i, 0]
        if not (math.isfinite(prev_c) and prev_c != 0 and math.isfinite(op)):
            continue
        gap[i] = (op - prev_c) / prev_c
        rng = prev_h - prev_l
        if math.isfinite(rng):
            prange[i] = rng / prev_c
        if math.isfinite(rng) and rng > 0:
            gap_vs[i] = (op - prev_c) / rng
            cpos[i] = (prev_c - prev_l) / rng
    return {
        "gap_pct": gap,
        "gap_vs_range": gap_vs,
        "prior_range_pct": prange,
        "prior_close_pos": cpos,
        "or_size": or_size,
    }


def opening_range_break(high, low, close):
    """+1 / -1 / 0 once the 9:30-9:44 range is closed. NaN before that bar.

    high/low/close are one session. Index 14 is the 9:44 bar. Its close, and
    the high/low of indices 0..14, are known then. Later highs do not move the range.
    """
    high = np.asarray(high, dtype=float)
    low = np.asarray(low, dtype=float)
    close = np.asarray(close, dtype=float)
    out = np.full(len(close), np.nan)
    if len(close) < 15 or not (np.isfinite(high[:15]).all() and np.isfinite(low[:15]).all()):
        return out
    hi = float(high[:15].max())
    lo = float(low[:15].min())
    for m in range(14, len(close)):
        c = close[m]
        if not math.isfinite(c):
            continue
        if c > hi:
            out[m] = 1.0
        elif c < lo:
            out[m] = -1.0
        else:
            out[m] = 0.0
    return out


# -------------------------------------------------------------------------------- panel and features


class Panel:
    """Feature cube. Intraday arrays are indexed by the signal bar, not the entry bar.

    f[name]: (days, symbols, minutes) float, NaN when unknown.
    daily[name]: (days, symbols) float.
    ev[name]: (days, symbols, minutes) int8 direction at the signal bar.
    """

    def __init__(self, days, symbols):
        self.days = list(days)
        self.symbols = list(symbols)
        self.shape = (len(self.days), len(self.symbols), N_MIN)
        self.f = {}
        self.daily = {}
        self.ev = {}

    def add_f(self, name):
        self.f[name] = np.full(self.shape, np.nan, dtype=np.float64)
        return self.f[name]

    def add_daily(self, name):
        self.daily[name] = np.full(self.shape[:2], np.nan, dtype=np.float64)
        return self.daily[name]

    def add_ev(self, name):
        self.ev[name] = np.zeros(self.shape, dtype=np.int8)
        return self.ev[name]

    def shuffled(self, perm):
        """New panel: daily rows follow perm, intraday arrays are shared and not reordered.

        perm[i] is the source day whose daily features are pasted onto calendar day i.
        Intraday prices, events, and the outcome cube stay on the calendar day.
        """
        out = object.__new__(Panel)
        out.days = self.days
        out.symbols = self.symbols
        out.shape = self.shape
        out.f = self.f
        out.ev = self.ev
        out.daily = {k: np.ascontiguousarray(v[perm]) for k, v in self.daily.items()}
        return out


def _prep_frame(df):
    if df.index.tz is None:
        raise ValueError("bars must be timezone-aware")
    out = df.copy()
    out.index = out.index.tz_convert(NY)
    out = out[~out.index.duplicated(keep="last")].sort_index()
    for col in ("open", "high", "low", "close", "volume"):
        if col not in out.columns:
            raise ValueError(f"missing {col}")
        out[col] = out[col].astype(float)
    return out


def _indicator_frame(df):
    """Causal 1-minute columns. Bar i uses rows 0..i only."""
    o, h, l, c, v = (df[k] for k in ("open", "high", "low", "close", "volume"))
    prev_c = c.shift(1)
    tr = pd.concat([h - l, (h - prev_c).abs(), (l - prev_c).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1 / 14, adjust=False).mean()
    ema13 = c.ewm(span=13, adjust=False).mean()
    ema34 = c.ewm(span=34, adjust=False).mean()
    hm = df.index.hour * 100 + df.index.minute
    rth = (hm >= 930) & (hm < 1600)
    day = pd.Series(df.index.date, index=df.index)
    hlc3 = (h + l + c) / 3.0
    pv = (hlc3 * v).where(rth, 0.0).groupby(day).cumsum()
    vv = v.where(rth, 0.0).groupby(day).cumsum()
    vwap = pv / vv.replace(0, np.nan)
    bt = sc._bt()
    fear, greed = bt.vfx_pane(df)
    basis = c.rolling(20).mean()
    dev = 2.0 * c.rolling(20).std(ddof=0)
    tr_kc = pd.concat([h - l, (h - prev_c).abs(), (l - prev_c).abs()], axis=1).max(axis=1)
    kc = tr_kc.rolling(20).mean()
    inside = ((basis - dev) > (basis - 1.5 * kc)) & ((basis + dev) < (basis + 1.5 * kc))
    inside = inside.fillna(False).to_numpy()
    mid = ((h.rolling(20).max() + l.rolling(20).min()) / 2.0 + basis) / 2.0
    mom = bt.linreg_last((c - mid).to_numpy(dtype=float), 20)
    hist = macd_histogram(c.to_numpy(dtype=float))
    spread = (ema13 - ema34) / atr.replace(0, np.nan)
    slope = spread - spread.shift(5)
    return {
        "open": o.to_numpy(dtype=float),
        "high": h.to_numpy(dtype=float),
        "low": l.to_numpy(dtype=float),
        "close": c.to_numpy(dtype=float),
        "volume": v.to_numpy(dtype=float),
        "atr": atr.to_numpy(dtype=float),
        "vwap": vwap.to_numpy(dtype=float),
        "vwap_atr": ((c - vwap) / atr.replace(0, np.nan)).to_numpy(dtype=float),
        "ema_slope": slope.to_numpy(dtype=float),
        "ret_5": (c / c.shift(5) - 1.0).to_numpy(dtype=float),
        "ret_15": (c / c.shift(15) - 1.0).to_numpy(dtype=float),
        "ret_30": (c / c.shift(30) - 1.0).to_numpy(dtype=float),
        "wvf": np.asarray(fear, dtype=float),
        "wvi": np.asarray(greed, dtype=float),
        "squeeze_on": inside,
        "squeeze_bars": _run_length(inside).astype(float),
        "mom": np.asarray(mom, dtype=float),
        "hist": hist,
        "index": df.index,
    }


def _htf_frame(df, minutes):
    """OHLC bars labeled by start time. A bar is known `minutes` after its label. No peek."""
    g = df.groupby(df.index.floor(f"{minutes}min"), sort=True)
    out = pd.DataFrame({
        "open": g["open"].first(),
        "high": g["high"].max(),
        "low": g["low"].min(),
        "close": g["close"].last(),
        "volume": g["volume"].sum(),
    }).dropna(subset=["close"])
    return out


def _session_matrix(frame_high, frame_low, frame_open, frame_close, frame_volume, index):
    """RTH sessions in chronological order as (dates, (D, N_MIN) arrays)."""
    hm = index.hour * 100 + index.minute
    rth = (hm >= 930) & (hm < 1600)
    buckets = {}
    for i in np.nonzero(np.asarray(rth))[0]:
        ts = index[i]
        minute = int(ts.hour * 60 + ts.minute - 570)
        if minute < 0 or minute >= N_MIN:
            continue
        buckets.setdefault(ts.date(), []).append((minute, i))
    dates = sorted(buckets)
    shape = (len(dates), N_MIN)
    arrays = {k: np.full(shape, np.nan) for k in ("open", "high", "low", "close", "volume")}
    for di, day in enumerate(dates):
        for minute, i in buckets[day]:
            arrays["open"][di, minute] = frame_open[i]
            arrays["high"][di, minute] = frame_high[i]
            arrays["low"][di, minute] = frame_low[i]
            arrays["close"][di, minute] = frame_close[i]
            arrays["volume"][di, minute] = frame_volume[i]
    return dates, arrays


def _stamp_direction(dest, lookup, known_ns, direction):
    """Write a higher-timeframe event onto the 1-minute bar that closes at known_ns.

    The event is not copied onto later minutes. known_ns is the close time.
    """
    direction = np.asarray(direction)
    known_ns = np.asarray(known_ns, dtype=np.int64)
    step = 60_000_000_000
    for t, d in zip(known_ns, direction):
        if d == 0:
            continue
        key = int(t) - step
        pos = lookup.get(key)
        if pos is None:
            continue
        di, minute = pos
        cur = int(dest[di, minute])
        new = int(d)
        if cur == 0:
            dest[di, minute] = new
        elif cur != new:
            dest[di, minute] = 0


def _lookup_rth(index, score_pos):
    lookup = {}
    for ts in index:
        di = score_pos.get(ts.date())
        if di is None:
            continue
        minute = int(ts.hour * 60 + ts.minute - 570)
        if 0 <= minute < N_MIN:
            lookup[int(ts.value)] = (di, minute)
    return lookup


def _fill_symbol(panel, si, df, score_pos):
    ind = _indicator_frame(df)
    index = ind["index"]
    lookup = _lookup_rth(index, score_pos)
    names = {
        "ret_5": "ret_5", "ret_15": "ret_15", "ret_30": "ret_30",
        "vwap_atr": "vwap_atr", "ema_slope": "ema_slope",
        "wvf_1m": "wvf", "wvi_1m": "wvi",
    }
    # Direct loop over RTH rows that land on score days.
    hm = index.hour * 100 + index.minute
    rth = (hm >= 930) & (hm < 1600)
    for i in np.nonzero(np.asarray(rth))[0]:
        ts = index[i]
        di = score_pos.get(ts.date())
        if di is None:
            continue
        minute = int(ts.hour * 60 + ts.minute - 570)
        if minute < 0 or minute >= N_MIN:
            continue
        for dst, src in names.items():
            panel.f[dst][di, si, minute] = ind[src][i]
        on = ind["squeeze_on"][i]
        # NaN until the squeeze window exists: rolling leaves False after fillna only when
        # the comparison was False. Early bars with NaN basis were fillna(False), so they
        # read as off. Mark the first 20 bars of the whole frame as unknown instead.
        if i < 20:
            panel.f["squeeze_on"][di, si, minute] = np.nan
            panel.f["squeeze_bars"][di, si, minute] = np.nan
        else:
            panel.f["squeeze_on"][di, si, minute] = 1.0 if on else 0.0
            panel.f["squeeze_bars"][di, si, minute] = ind["squeeze_bars"][i]
    # 1-minute events on the continuous series, then copied onto RTH score minutes.
    pos_of = {int(ts.value): i for i, ts in enumerate(index)}
    zero, shrink, flip = macd_event_directions(ind["hist"])
    swing = pivot_direction(ind["high"], ind["low"])
    div = divergence_direction(ind["high"], ind["low"], ind["hist"])
    rel = squeeze_release_direction(ind["squeeze_on"], ind["mom"])
    event_cols = {
        "macd_zero_1m": zero,
        "macd_shrink_1m": shrink,
        "macd_flip_1m": flip,
        "swing_1m": swing,
        "div_1m": div,
        "sq_release_1m": rel,
    }
    for name, arr in event_cols.items():
        dest = panel.ev[name][:, si, :]
        for key, (di, minute) in lookup.items():
            i = pos_of.get(key)
            if i is None:
                continue
            dest[di, minute] = arr[i]
    # Higher timeframes. Levels are carried forward with asof. Events stamp once.
    bar_end = np.array([int(ts.value) + 60_000_000_000 for ts in index], dtype=np.int64)
    for minutes, tag in ((3, "3m"), (5, "5m")):
        htf = _htf_frame(df, minutes)
        if not len(htf):
            continue
        known = np.array(
            [int((ts + pd.Timedelta(minutes=minutes)).value) for ts in htf.index],
            dtype=np.int64,
        )
        htf_hist = macd_histogram(htf["close"].to_numpy(dtype=float))
        if tag == "3m":
            bt = sc._bt()
            fear, greed = bt.vfx_pane(htf)
            wvf_aligned = asof_known(bar_end, known, np.asarray(fear, dtype=float))
            wvi_aligned = asof_known(bar_end, known, np.asarray(greed, dtype=float))
            for key, (di, minute) in lookup.items():
                i = pos_of.get(key)
                if i is None:
                    continue
                panel.f["wvf_3m"][di, si, minute] = wvf_aligned[i]
                panel.f["wvi_3m"][di, si, minute] = wvi_aligned[i]
            z, sh, fl = macd_event_directions(htf_hist)
            sw = pivot_direction(htf["high"].to_numpy(dtype=float), htf["low"].to_numpy(dtype=float))
            # 3m squeeze release
            hh, ll, cc = htf["high"], htf["low"], htf["close"]
            basis = cc.rolling(20).mean()
            dev = 2.0 * cc.rolling(20).std(ddof=0)
            pc = cc.shift(1)
            tr = pd.concat([hh - ll, (hh - pc).abs(), (ll - pc).abs()], axis=1).max(axis=1)
            kc = tr.rolling(20).mean()
            inside = ((basis - dev) > (basis - 1.5 * kc)) & ((basis + dev) < (basis + 1.5 * kc))
            inside = inside.fillna(False).to_numpy()
            mid = ((hh.rolling(20).max() + ll.rolling(20).min()) / 2.0 + basis) / 2.0
            mom = sc._bt().linreg_last((cc - mid).to_numpy(dtype=float), 20)
            rel3 = squeeze_release_direction(inside, mom)
            for name, arr in (
                ("macd_zero_3m", z), ("macd_shrink_3m", sh), ("macd_flip_3m", fl),
                ("swing_3m", sw), ("sq_release_3m", rel3),
            ):
                _stamp_direction(panel.ev[name][:, si, :], lookup, known, arr)
        dv = divergence_direction(
            htf["high"].to_numpy(dtype=float),
            htf["low"].to_numpy(dtype=float),
            htf_hist,
        )
        _stamp_direction(panel.ev[f"div_{tag}"][:, si, :], lookup, known, dv)
    # Session context, including warmup days that are not in the score window.
    dates, mats = _session_matrix(
        ind["high"], ind["low"], ind["open"], ind["close"], ind["volume"], index,
    )
    ctx = daily_price_context(mats["open"], mats["high"], mats["low"], mats["close"])
    rvol_all = relative_volume(mats["volume"], 20)
    date_pos = {d: i for i, d in enumerate(dates)}
    for day, di in score_pos.items():
        si_src = date_pos.get(day)
        if si_src is None:
            continue
        for name in ("gap_pct", "gap_vs_range", "prior_range_pct", "prior_close_pos", "or_size"):
            panel.daily[name][di, si] = ctx[name][si_src]
        panel.f["rvol"][di, si, :] = rvol_all[si_src]
        panel.f["or_break"][di, si, :] = opening_range_break(
            mats["high"][si_src], mats["low"][si_src], mats["close"][si_src],
        )


def compute_features(frames, vix_closes, score_days, symbols):
    """Build a panel for score_days. Earlier rows in `frames` are warmup only.

    frames: symbol -> 1-minute OHLC+V DataFrame, timezone-aware.
    vix_closes: date -> VIX close. A session does not see its own date or later.
    Intraday values at minute m use bars whose close is at or before that minute's close.
    Higher-timeframe values are withheld until that bar's close.
    """
    score_days = list(score_days)
    symbols = list(symbols)
    panel = Panel(score_days, symbols)
    for name in (
        "ret_5", "ret_15", "ret_30", "vwap_atr", "ema_slope", "rvol",
        "wvf_1m", "wvi_1m", "wvf_3m", "wvi_3m", "squeeze_on", "squeeze_bars", "or_break",
    ):
        panel.add_f(name)
    for name in DAILY_FEATURES:
        panel.add_daily(name)
    for name in FIXED_EVENTS:
        panel.add_ev(name)
    score_pos = {d: i for i, d in enumerate(score_days)}
    prior, chg = prior_vix_features(score_days, vix_closes)
    for si in range(len(symbols)):
        panel.daily["vix_prior"][:, si] = prior
        panel.daily["vix_chg_5d"][:, si] = chg
        panel.daily["dow"][:, si] = [float(d.weekday()) for d in score_days]
    for si, sym in enumerate(symbols):
        df = _prep_frame(frames[sym])
        _fill_symbol(panel, si, df, score_pos)
    return panel


# -------------------------------------------------------------------------------- rules


class Cond(tuple):
    """A condition. mode '' is a gate. call/put/follow/fade is a side."""

    __slots__ = ()

    def __new__(cls, id, kind, feature, bucket, mode, level, group):
        return tuple.__new__(cls, (id, kind, feature, bucket, mode, float(level), group))

    @property
    def id(self):
        return self[0]

    @property
    def kind(self):
        return self[1]

    @property
    def feature(self):
        return self[2]

    @property
    def bucket(self):
        return self[3]

    @property
    def mode(self):
        return self[4]

    @property
    def level(self):
        return self[5]

    @property
    def group(self):
        return self[6]


class Spec(tuple):
    __slots__ = ()

    def __new__(cls, name, kind, day_gate, minute_gate, leg):
        return tuple.__new__(cls, (name, kind, day_gate, minute_gate, leg))

    @property
    def name(self):
        return self[0]

    @property
    def kind(self):
        return self[1]

    @property
    def day_gate(self):
        return self[2]

    @property
    def minute_gate(self):
        return self[3]

    @property
    def leg(self):
        return self[4]


def _cond(kind, feature, bucket, mode, level, group):
    ident = f"{feature}|{bucket}|{mode}" if mode else f"{feature}|{bucket}"
    if kind == "tod":
        ident = f"tod|{int(level)}|{mode}"
    elif kind == "dow":
        ident = f"dow|{int(level)}|{mode or 'gate'}"
    elif kind == "always":
        ident = f"always|{mode}"
    elif kind == "flag":
        ident = f"{feature}|{bucket}|{mode}" if mode else f"{feature}|{bucket}"
    return Cond(ident, kind, feature, bucket, mode, level, group)


def is_daily_signed(cond):
    return cond is not None and cond.kind == "signed" and cond.feature in SIGNED_DAILY


def is_shuffle_sensitive(spec):
    """True when a day-label shuffle can change the rule. Intraday-only rules are not."""
    if spec.day_gate is not None:
        return True
    return is_daily_signed(spec.leg)


def param_grid(cond):
    if cond is None:
        return (None,)
    if cond.kind in ("daily_level", "intra_level"):
        return HIGH_QS if cond.bucket == "high" else LOW_QS
    if cond.kind == "mag":
        return MAG_QS
    if cond.kind == "signed" and cond.feature != "or_break":
        return MAG_QS
    if cond.kind == "event" and cond.feature == "vwap_rvol":
        return STRETCHES
    if cond.kind == "event" and "roll" in cond.feature:
        return WVF_LEVELS
    return (None,)


def _fixed_threshold(cond):
    return cond.kind == "event" and (cond.feature == "vwap_rvol" or "roll" in cond.feature)


def _values_for(panel, cond, train):
    if cond.kind == "daily_level" or (cond.kind == "signed" and cond.feature in panel.daily):
        return np.asarray(panel.daily[cond.feature][train], dtype=float)
    if cond.feature in panel.f:
        return np.asarray(panel.f[cond.feature][train], dtype=float)
    raise KeyError(cond.feature)


def resolve_threshold(panel, cond, train, param, min_n):
    """Return ('ok', threshold) or ('bad', None).

    Quantiles use `train` rows only. A fixed grid value does not read the test days.
    ('ok', None) means the condition has no threshold.
    """
    if _fixed_threshold(cond):
        return ("ok", float(param))
    if param is None:
        return ("ok", None)
    values = _values_for(panel, cond, train)
    if cond.kind in ("signed", "mag"):
        values = np.abs(values)
    flat = values[np.isfinite(values)]
    if flat.size < int(min_n):
        return ("bad", None)
    return ("ok", float(np.quantile(flat, float(param))))


def entry_masks(panel, cond, thr):
    """Boolean call/put masks on the ENTRY clock. thr is the resolved threshold or None."""
    d_n, s_n, m_n = panel.shape
    call = np.zeros((d_n, s_n, m_n), dtype=bool)
    put = np.zeros((d_n, s_n, m_n), dtype=bool)
    window = slice(FIRST_ENTRY, LAST_ENTRY + 1)
    if cond.kind == "always":
        if cond.mode == "call":
            call[:, :, window] = True
        else:
            put[:, :, window] = True
        return call, put
    if cond.kind == "tod":
        mins = np.arange(m_n)
        on = (mins // 30) == int(cond.level)
        on[:FIRST_ENTRY] = False
        on[LAST_ENTRY + 1:] = False
        if cond.mode == "call":
            call[:, :, on] = True
        else:
            put[:, :, on] = True
        return call, put
    if cond.kind == "dow":
        ok = panel.daily["dow"] == float(cond.level)
        if cond.mode == "call":
            call[:, :, window] = ok[:, :, None]
        else:
            put[:, :, window] = ok[:, :, None]
        return call, put
    if cond.kind == "daily_level":
        x = panel.daily[cond.feature]
        good = x >= thr if cond.bucket == "high" else x <= thr
        good = good & np.isfinite(x)
        if cond.mode == "call":
            call[:, :, window] = good[:, :, None]
        elif cond.mode == "put":
            put[:, :, window] = good[:, :, None]
        return call, put
    if cond.kind == "flag":
        sig = panel.f[cond.feature]
        if cond.bucket == "on":
            good = sig >= 0.5
        else:
            good = sig == 0.0
        good = shift_signal(good)
        if cond.mode == "call":
            call = good
        elif cond.mode == "put":
            put = good
        else:
            # gate: both masks true so a caller can AND either side
            call = good
            put = good
        return call, put
    if cond.kind == "intra_level":
        x = panel.f[cond.feature]
        good = (x >= thr) if cond.bucket == "high" else (x <= thr)
        good = shift_signal(good & np.isfinite(x))
        if cond.mode == "call":
            return good, put
        if cond.mode == "put":
            return call, good
        return good, good
    if cond.kind == "mag":
        x = panel.f[cond.feature]
        good = shift_signal((np.abs(x) >= thr) & np.isfinite(x))
        return good, good
    if cond.kind == "signed":
        if cond.feature in panel.daily:
            x = panel.daily[cond.feature]
            ok = (np.abs(x) >= thr) & np.isfinite(x) if thr is not None else np.isfinite(x)
            sign = np.sign(x)
            pos = ok & (sign > 0)
            neg = ok & (sign < 0)
            if cond.mode == "fade":
                pos, neg = neg, pos
            call[:, :, window] = pos[:, :, None]
            put[:, :, window] = neg[:, :, None]
            return call, put
        x = panel.f[cond.feature]
        if cond.feature == "or_break":
            pos = x > 0
            neg = x < 0
        else:
            mag = (np.abs(x) >= thr) & np.isfinite(x)
            pos = mag & (x > 0)
            neg = mag & (x < 0)
        if cond.mode == "fade":
            pos, neg = neg, pos
        return shift_signal(pos), shift_signal(neg)
    if cond.kind == "event":
        direction = _event_direction(panel, cond, thr)
        pos = direction > 0
        neg = direction < 0
        if cond.mode == "fade":
            pos, neg = neg, pos
        return shift_signal(pos), shift_signal(neg)
    raise ValueError(cond.kind)


def _event_direction(panel, cond, thr):
    name = cond.feature
    if name == "vwap_rvol":
        return vwap_rvol_direction(panel.f["vwap_atr"], panel.f["rvol"], thr, RVOL_MIN)
    if name.startswith("wvf_roll"):
        src = "wvf_1m" if name.endswith("1m") else "wvf_3m"
        return wvf_rollover_mask(panel.f[src], thr).astype(np.int8)
    if name.startswith("wvi_roll"):
        src = "wvi_1m" if name.endswith("1m") else "wvi_3m"
        fire = wvf_rollover_mask(panel.f[src], thr)
        out = np.zeros(fire.shape, dtype=np.int8)
        out[fire] = -1
        return out
    return panel.ev[name]


def day_gate_mask(panel, cond, thr):
    """(days, symbols) boolean. The gate is constant for the whole session."""
    if cond.kind == "dow":
        return panel.daily["dow"] == float(cond.level)
    x = panel.daily[cond.feature]
    if cond.bucket == "high":
        good = x >= thr
    else:
        good = x <= thr
    return good & np.isfinite(x)


def _sources(cond):
    if cond is None:
        return frozenset()
    if cond.kind == "event":
        return EVENT_SOURCES.get(cond.feature, frozenset({cond.feature}))
    if cond.kind in ("always", "tod"):
        return frozenset({cond.id})
    if cond.kind == "dow":
        return frozenset({"dow"})
    return frozenset({cond.feature}) if cond.feature else frozenset()


def build_family():
    """Predeclared singles and pairs. Built from the lists above, not from results."""
    specs = []
    always_call = _cond("always", "", "all", "call", -1, "base")
    always_put = _cond("always", "", "all", "put", -1, "base")

    def add(name, kind, day_gate, minute_gate, leg):
        specs.append(Spec(name, kind, day_gate, minute_gate, leg))

    day_gates = []
    for feat in LEVEL_DAILY:
        for bucket in ("high", "low"):
            gate = _cond("daily_level", feat, bucket, "", -1, "daily")
            day_gates.append(gate)
            for mode, leg in (("call", always_call), ("put", always_put)):
                add(f"single {feat} {bucket} {mode}", "single", gate, None, leg)
    for dow in range(5):
        gate = _cond("dow", "dow", "eq", "", dow, "daily")
        day_gates.append(gate)
        for mode, leg in (("call", always_call), ("put", always_put)):
            add(f"single dow {dow} {mode}", "single", gate, None, leg)

    side_legs = []
    for feat in LEVEL_INTRA:
        for bucket in ("high", "low"):
            for mode in ("call", "put"):
                leg = _cond("intra_level", feat, bucket, mode, -1, "intra")
                side_legs.append(leg)
                add(f"single {feat} {bucket} {mode}", "single", None, None, leg)
    for feat in SIGNED_DAILY:
        for mode in ("follow", "fade"):
            leg = _cond("signed", feat, "mag", mode, -1, "daily")
            side_legs.append(leg)
            add(f"single {feat} {mode}", "single", None, None, leg)
    for feat in SIGNED_INTRA:
        for mode in ("follow", "fade"):
            leg = _cond("signed", feat, "mag", mode, -1, "intra")
            side_legs.append(leg)
            add(f"single {feat} {mode}", "single", None, None, leg)
    for bucket in TOD_BUCKETS:
        for mode in ("call", "put"):
            leg = _cond("tod", "tod", "eq", mode, bucket, "time")
            side_legs.append(leg)
            hh, mm = divmod(9 * 60 + 30 + bucket * 30, 60)
            add(f"single tod {hh:02d}:{mm:02d} {mode}", "single", None, None, leg)
    for bucket in ("on", "off"):
        for mode in ("call", "put"):
            leg = _cond("flag", "squeeze_on", bucket, mode, -1, "intra")
            side_legs.append(leg)
            add(f"single squeeze {bucket} {mode}", "single", None, None, leg)
    for feat in FIXED_EVENTS + GRID_EVENTS:
        for mode in ("follow", "fade"):
            leg = _cond("event", feat, "event", mode, -1, "event")
            side_legs.append(leg)
            add(f"single {feat} {mode}", "single", None, None, leg)

    for gate in day_gates:
        for leg in side_legs:
            if _sources(gate) & _sources(leg):
                continue
            # A daily level single is already gate x always. Do not pair a gate with always.
            if leg.kind == "always":
                continue
            add(f"pair {gate.id} + {leg.id}", "pair", gate, None, leg)

    minute_gates = []
    for feat, bucket, kind in INTRA_GATES:
        minute_gates.append(_cond(kind, feat, bucket, "", -1, "gate"))
    event_legs = [leg for leg in side_legs if leg.kind == "event"]
    for gate in minute_gates:
        for leg in event_legs:
            if _sources(gate) & _sources(leg):
                continue
            add(f"pair {gate.id} + {leg.id}", "pair", None, gate, leg)
    return specs


def family_blurb():
    return (
        "Singles cover each daily and intraday feature as a high bucket and a low bucket, "
        "both call and put; each signed feature as follow and as fade; day of week; "
        "each 30-minute clock bucket; squeeze on and off; and every reversal event as follow and fade. "
        "Pairs are every daily-context gate with every setup that uses a different feature, "
        "plus each reversal event with a predeclared intraday gate "
        "(relative volume, Williams VIX Fix level, squeeze length or on, VWAP stretch, "
        "EMA slope, 5-minute return) when that gate is not the same measurement as the event. "
        "This is not the cross of every feature with every other feature."
    )


def reversal_blurb():
    return (
        "Reversal events, all causal: MACD(12,26,9) histogram zero-cross, shrink, and color flip "
        "on 1-minute and 3-minute bars; regular bullish/bearish divergence of price vs MACD histogram "
        "on 1-minute, 3-minute, and 5-minute bars; 5-bar-left/5-bar-right swing pivots on 1-minute and "
        "3-minute bars, flagged at the confirmation bar; VWAP stretch in ATR units with relative volume "
        "at least 1.5x the same-minute 20-day median; Williams VIX Fix (and the greed mirror) spike "
        "then rollover on 1-minute and 3-minute bars; TTM squeeze release with a momentum color flip "
        "on 1-minute and 3-minute bars. Follow trades the event's direction. Fade trades against it. "
        "A pivot or a divergence is not tradable until the right-side bars have closed."
    )


# -------------------------------------------------------------------------------- option outcomes


def _price_minute(book, minute, exits, costs, premium):
    """One intended minute on one contract. Entry existence does not depend on the exit."""
    n_e = len(exits)
    nets = np.full(n_e, np.nan, dtype=np.float64)
    hits = np.zeros(n_e, dtype=np.uint8)
    if book is None or minute < 0 or minute >= FLAT_MIN:
        return "miss", nets, hits
    probe = sc.simulate_trade(book, int(minute), exits[0], costs, allow_slip=False, premium=premium)
    if probe["status"] == "skip_entry":
        return "miss", nets, hits
    if probe["status"] == "skip_premium":
        return "premium", nets, hits
    for ei, cfg in enumerate(exits):
        trial = probe if ei == 0 else sc.simulate_trade(
            book, int(minute), cfg, costs, allow_slip=False, premium=premium,
        )
        if trial["status"] == "fill":
            nets[ei] = float(trial["net_pct"])
            hits[ei] = 1 if trial["hit"] else 0
    return "entry", nets, hits


def _apply_slip(primary, nxt):
    """primary/nxt are (status, nets, hits). Do not slide through a real print or a premium skip."""
    status, nets, hits = primary
    if status in ("entry", "premium"):
        return nets, hits
    if nxt is None:
        return nets, hits
    st2, nets2, hits2 = nxt
    if st2 == "entry":
        return nets2, hits2
    return nets, hits


def build_outcome_cube(days, symbols, und, opt, strikes, exits, costs, premium, progress=True):
    """Net % and hit flag for an intended entry minute, after the 2-minute print search.

    Shape (days, symbols, minutes, side, strike, exit). side 0 is call, 1 is put.
    A missing print at the intended minute may use the next minute, on that minute's
    own strike, matching scalp_real.run_book. A premium skip does not slide.
    """
    bt = sc._bt()
    n_d, n_s = len(days), len(symbols)
    n_k, n_e = len(strikes), len(exits)
    net = np.full((n_d, n_s, N_MIN, 2, n_k, n_e), np.nan, dtype=np.float32)
    hit = np.zeros((n_d, n_s, N_MIN, 2, n_k, n_e), dtype=np.uint8)
    day_pos = {d: i for i, d in enumerate(days)}
    for di, day in enumerate(days):
        for si, sym in enumerate(symbols):
            sess = und[sym].get(day)
            if sess is None:
                continue
            for side_i, side in ((0, 1), (1, -1)):
                cp = "C" if side == 1 else "P"
                for ki, mode in enumerate(strikes):
                    books = [None] * N_MIN
                    for m in range(FIRST_ENTRY, LAST_ENTRY + 2):
                        if m >= N_MIN:
                            break
                        spot = sc.spot_at(sess, m)
                        if spot is None:
                            continue
                        k = sc.strike_price(spot, side, mode)
                        if k is None:
                            continue
                        books[m] = opt.get((day, bt.lab_occ(sym, day, cp, k)))
                    for m in range(FIRST_ENTRY, LAST_ENTRY + 1):
                        primary = _price_minute(books[m], m, exits, costs, premium)
                        nxt = None
                        if primary[0] == "miss" and m + 1 <= LAST_ENTRY:
                            nxt = _price_minute(books[m + 1], m + 1, exits, costs, premium)
                        nets, hits = _apply_slip(primary, nxt)
                        net[di, si, m, side_i, ki, :] = nets
                        hit[di, si, m, side_i, ki, :] = hits
        if progress and (di + 1) % 10 == 0:
            sc._print_scrubbed(f"  priced {di + 1}/{n_d} sessions")
    return net, hit


def accumulate_entries(day, sym, minute, side, net, hit):
    """Sum finite outcomes into (days, symbols, strikes, exits).

    Returns (sum, count, hit). Count is filled trades. Hit is how many of those
    reached the target. Selection and out-of-sample stats read them in that order.
    """
    d_n, s_n, _, _, n_k, n_e = net.shape
    sum_ = np.zeros((d_n, s_n, n_k, n_e), dtype=np.float64)
    hit_ = np.zeros((d_n, s_n, n_k, n_e), dtype=np.float64)
    cnt_ = np.zeros((d_n, s_n, n_k, n_e), dtype=np.float64)
    if len(day) == 0:
        return sum_, hit_, cnt_
    vals = np.asarray(net[day, sym, minute, side], dtype=float)
    hits = np.asarray(hit[day, sym, minute, side], dtype=float)
    good = np.isfinite(vals)
    for k in range(n_k):
        for e in range(n_e):
            g = good[:, k, e]
            if not np.any(g):
                continue
            np.add.at(sum_[:, :, k, e], (day[g], sym[g]), vals[g, k, e])
            np.add.at(hit_[:, :, k, e], (day[g], sym[g]), hits[g, k, e])
            np.add.at(cnt_[:, :, k, e], (day[g], sym[g]), 1.0)
    return sum_, cnt_, hit_


# -------------------------------------------------------------------------------- search


def _zero_pack(shape_dse):
    z = np.zeros(shape_dse, dtype=np.float64)
    return z, z.copy(), z.copy()


def _masks_resolved(panel, cond, train, param, min_n, role):
    """role 'leg' builds call/put. role 'day' builds a day mask. role 'minute' builds a minute gate."""
    status, thr = resolve_threshold(panel, cond, train, param, min_n)
    if status != "ok":
        return None
    if role == "day":
        return day_gate_mask(panel, cond, thr)
    call, put = entry_masks(panel, cond, thr)
    if role == "minute":
        return call | put
    return call, put


def _leg_pack(panel, cond, train, param, min_n, net, hit):
    resolved = _masks_resolved(panel, cond, train, param, min_n, "leg")
    if resolved is None:
        return _zero_pack((panel.shape[0], panel.shape[1], net.shape[4], net.shape[5]))
    call, put = resolved
    return accumulate_entries(*cooldown_indices(call, put), net, hit)


def build_leg_catalog(panel, legs, folds, net, hit, min_n, progress=True):
    """For each intraday (or always) leg, per fold, per threshold: day sums after cooldown."""
    catalog = {}
    for i, leg in enumerate(legs):
        per_fold = []
        grid = param_grid(leg)
        for train, _test in folds:
            packs = []
            for param in grid:
                packs.append(_leg_pack(panel, leg, train, param, min_n, net, hit))
            per_fold.append(packs)
        catalog[leg.id] = per_fold
        if progress and (i + 1) % 25 == 0:
            sc._print_scrubbed(f"  catalog {i + 1}/{len(legs)} legs")
    return catalog


def _daily_signed_pack(panel, cond, train, param, min_n, always_call, always_put):
    status, thr = resolve_threshold(panel, cond, train, param, min_n)
    if status != "ok" or thr is None:
        return _zero_pack(always_call[0].shape)
    x = panel.daily[cond.feature]
    ok = (np.abs(x) >= thr) & np.isfinite(x)
    sign = np.sign(x)
    pos = ok & (sign > 0)
    neg = ok & (sign < 0)
    if cond.mode == "fade":
        pos, neg = neg, pos
    sm = always_call[0] * pos[:, :, None, None] + always_put[0] * neg[:, :, None, None]
    ct = always_call[1] * pos[:, :, None, None] + always_put[1] * neg[:, :, None, None]
    ht = always_call[2] * pos[:, :, None, None] + always_put[2] * neg[:, :, None, None]
    return sm, ct, ht


def _select_codes(gate_rows, leg_rows, train, min_train, primary_i=PRIMARY_I):
    """gate_rows: list of (D,S) masks. leg_rows: list of (sum, cnt, hit) packs.

    Picks a (gate, leg) pair per strike by training mean on the primary exit.
    Returns best_code (n_strikes,) with code = gate_index * n_leg + leg_index, or -1.
    """
    n_p = len(leg_rows)
    n_k = leg_rows[0][0].shape[2]
    gstack = np.stack([np.asarray(m[train], dtype=float) for m in gate_rows], axis=0)
    sm = np.stack([pk[0][train, :, :, primary_i] for pk in leg_rows], axis=0)
    ct = np.stack([pk[1][train, :, :, primary_i] for pk in leg_rows], axis=0)
    summed = np.tensordot(gstack, sm, axes=([1, 2], [1, 2]))
    counted = np.tensordot(gstack, ct, axes=([1, 2], [1, 2]))
    mu = np.where(counted >= min_train, summed / np.maximum(counted, 1.0), -np.inf)
    flat = mu.reshape(-1, n_k)
    code = np.argmax(flat, axis=0)
    best = flat[code, np.arange(n_k)]
    code = np.where(np.isfinite(best) & (best > -1e300), code, -1).astype(int)
    return code, n_p


def _mix_packs(gate_rows, leg_rows, code, n_p):
    sm0 = leg_rows[0][0]
    mixed_s = np.zeros_like(sm0)
    mixed_c = np.zeros_like(sm0)
    mixed_h = np.zeros_like(sm0)
    for k, raw in enumerate(code):
        if raw < 0:
            continue
        gi, pi = divmod(int(raw), n_p)
        gate = gate_rows[gi]
        sm, ct, ht = leg_rows[pi]
        mixed_s[:, :, k, :] = sm[:, :, k, :] * gate[:, :, None]
        mixed_c[:, :, k, :] = ct[:, :, k, :] * gate[:, :, None]
        mixed_h[:, :, k, :] = ht[:, :, k, :] * gate[:, :, None]
    return mixed_s, mixed_c, mixed_h


def _gate_rows_for(panel, spec, train, min_n):
    if spec.day_gate is None:
        return [np.ones(panel.shape[:2], dtype=bool)]
    rows = []
    for param in param_grid(spec.day_gate):
        resolved = _masks_resolved(panel, spec.day_gate, train, param, min_n, "day")
        if resolved is None:
            rows.append(np.zeros(panel.shape[:2], dtype=bool))
        else:
            rows.append(resolved)
    return rows


def _leg_rows_for(panel, spec, train, fold_i, catalog, always, min_n, net, hit):
    """Packs aligned with param_grid(spec.leg), except minute-gate pairs which expand the grid."""
    if spec.minute_gate is not None:
        packs = []
        codes = []
        for gi, gparam in enumerate(param_grid(spec.minute_gate)):
            gmask = _masks_resolved(panel, spec.minute_gate, train, gparam, min_n, "minute")
            for pi, lparam in enumerate(param_grid(spec.leg)):
                resolved = _masks_resolved(panel, spec.leg, train, lparam, min_n, "leg")
                if gmask is None or resolved is None:
                    packs.append(_zero_pack((panel.shape[0], panel.shape[1], net.shape[4], net.shape[5])))
                else:
                    call, put = resolved
                    call = call & gmask
                    put = put & gmask
                    packs.append(accumulate_entries(*cooldown_indices(call, put), net, hit))
                codes.append((gi, pi))
        return packs, codes
    if is_daily_signed(spec.leg):
        packs = []
        for param in param_grid(spec.leg):
            packs.append(_daily_signed_pack(panel, spec.leg, train, param, min_n, *always))
        return packs, None
    return catalog[spec.leg.id][fold_i], None


def _oos_index(folds, n_days):
    idx = np.full(n_days, -1, dtype=int)
    cursor = 0
    for _train, test in folds:
        for d in test:
            idx[int(d)] = cursor
            cursor += 1
    return idx


def _fmt_sl(sl):
    return "none" if sl is None else f"{sl:.2f}"


def _row_stats(sums, cnts, hits, folds, oos_index, boot, seed):
    """Per-exit stats are computed by the caller on a 1-d day axis. This is one exit."""
    n = float(cnts.sum())
    mean = float(sums.sum() / n) if n else float("nan")
    hit_rate = float(hits.sum() / n) if n else float("nan")
    tstat, p = clustered_t_from_days(sums, cnts)
    lo, hi = sc.bootstrap_mean(sums, cnts, int(boot), int(seed) % (2 ** 32))
    fold_means = []
    positive = 0
    for _train, test in folds:
        block = oos_index[test]
        c = float(cnts[block].sum())
        if c <= 0:
            fold_means.append(float("nan"))
            continue
        mu = float(sums[block].sum() / c)
        fold_means.append(mu)
        if mu > 0:
            positive += 1
    return {
        "n": int(round(n)),
        "hit_rate": hit_rate,
        "mean_net_pct": mean,
        "t": tstat,
        "p": p if math.isfinite(p) else 1.0,
        "boot_lo": lo,
        "boot_hi": hi,
        "folds_positive": positive,
        "fold_means": fold_means,
    }


def draw_matched_minutes(minutes, seed):
    """Draw a minute from the same empirical clock, off the original minute when it collides.

    A one-minute spike falls back to the rest of that 30-minute bucket, then to the
    entry window. This is the matched random clock.
    """
    minutes = np.asarray(minutes, dtype=int)
    n = len(minutes)
    if n == 0:
        return minutes.copy()
    rng = np.random.default_rng(int(seed) % (2 ** 32))
    hist = np.bincount(np.clip(minutes, 0, N_MIN - 1), minlength=N_MIN).astype(float)
    elig = np.arange(FIRST_ENTRY, LAST_ENTRY + 1)
    p = hist[elig]
    if p.sum() <= 0:
        p = np.ones(len(elig), dtype=float)
    p = p / p.sum()
    draw = rng.choice(elig, size=n, p=p)
    same = np.nonzero(draw == minutes)[0]
    for i in same:
        m = int(minutes[i])
        b0 = (m // 30) * 30
        bucket = np.arange(b0, b0 + 30)
        bucket = bucket[(bucket >= FIRST_ENTRY) & (bucket <= LAST_ENTRY) & (bucket != m)]
        if len(bucket) == 0:
            bucket = elig[elig != m]
        draw[i] = int(rng.choice(bucket)) if len(bucket) else m
    return draw


def matched_random_lookup(day, sym, minute, side, draw, net, hit, strike_i, n_redraw=8, seed=1):
    """Mean net and hit rate per exit for the matched minutes. Redraw if that exit did not fill."""
    n_e = net.shape[5]
    means = np.full(n_e, np.nan)
    ns = np.zeros(n_e, dtype=int)
    hits = np.full(n_e, np.nan)
    if len(day) == 0:
        return means, ns, hits
    rng = np.random.default_rng(int(seed) % (2 ** 32))
    elig = np.arange(FIRST_ENTRY, LAST_ENTRY + 1)
    cur = np.array(draw, dtype=int, copy=True)
    for _ in range(n_redraw):
        vals = np.asarray(net[day, sym, cur, side, strike_i, :], dtype=float)
        if np.isfinite(vals).all():
            break
        bad = ~np.isfinite(vals).any(axis=1) if vals.ndim == 2 else ~np.isfinite(vals)
        # Redraw rows that missed on every exit (no print). Keep partial exit fills.
        miss = ~np.isfinite(vals).all(axis=1)
        if not miss.any():
            break
        cur[miss] = rng.choice(elig, size=int(miss.sum()))
    vals = np.asarray(net[day, sym, cur, side, strike_i, :], dtype=float)
    hv = np.asarray(hit[day, sym, cur, side, strike_i, :], dtype=float)
    for e in range(n_e):
        g = np.isfinite(vals[:, e])
        ns[e] = int(g.sum())
        if ns[e]:
            means[e] = float(vals[g, e].mean())
            hits[e] = float(hv[g, e].mean())
    return means, ns, hits, cur


def materialize_entries(panel, spec, folds, codes, strike_i, min_n, net, hit):
    """OOS entries for one strike, using the stored winning parameter code per fold.

    `net` and `hit` are unused except to keep the call signature stable for tests that
    only check the minutes. Passing them lets a caller reuse the same arguments as scoring.
    """
    del net, hit
    chunks = []
    for fi, (train, test) in enumerate(folds):
        code = int(codes[fi, strike_i])
        if code < 0:
            continue
        call, put = _masks_from_code(panel, spec, train, code, min_n)
        if call is None:
            continue
        day, sym, minute, side = cooldown_indices(call, put)
        if len(day) == 0:
            continue
        in_test = np.zeros(panel.shape[0], dtype=bool)
        in_test[test] = True
        keep = in_test[day]
        if not keep.any():
            continue
        chunks.append((day[keep], sym[keep], minute[keep], side[keep], np.full(int(keep.sum()), fi, dtype=int)))
    if not chunks:
        empty = np.zeros(0, dtype=int)
        return empty, empty, empty, empty, empty
    return tuple(np.concatenate([c[i] for c in chunks]) for i in range(5))


def _masks_from_code(panel, spec, train, code, min_n):
    """Rebuild the pre-cooldown masks for a winning code. None if the code is empty."""
    if spec.minute_gate is not None:
        n_p = len(param_grid(spec.leg))
        gi, pi = divmod(int(code), n_p)
        gparams = param_grid(spec.minute_gate)
        lparams = param_grid(spec.leg)
        if gi >= len(gparams) or pi >= len(lparams):
            return None
        gmask = _masks_resolved(panel, spec.minute_gate, train, gparams[gi], min_n, "minute")
        resolved = _masks_resolved(panel, spec.leg, train, lparams[pi], min_n, "leg")
        if gmask is None or resolved is None:
            return None
        call, put = resolved
        return call & gmask, put & gmask
    n_p = len(param_grid(spec.leg))
    if spec.day_gate is None:
        gi, pi = 0, int(code)
        gate = None
    else:
        gi, pi = divmod(int(code), n_p)
        gparams = param_grid(spec.day_gate)
        if gi >= len(gparams):
            return None
        gate = _masks_resolved(panel, spec.day_gate, train, gparams[gi], min_n, "day")
        if gate is None:
            return None
    lparams = param_grid(spec.leg)
    if pi >= len(lparams):
        return None
    resolved = _masks_resolved(panel, spec.leg, train, lparams[pi], min_n, "leg")
    if resolved is None:
        return None
    call, put = resolved
    if gate is not None:
        call = call & gate[:, :, None]
        put = put & gate[:, :, None]
    return call, put


def _param_text(spec, codes):
    parts = []
    for fi, row in enumerate(codes):
        parts.append(f"f{fi}:" + ",".join(str(int(c)) for c in row))
    return spec.name + " " + " ".join(parts)


def run_search(
    panel, net, hit, strike_names, exits=EXITS, *,
    n_shuf=N_SHUFFLE, seed=SEED, min_train=MIN_TRAIN, min_quantile_n=MIN_QUANTILE_N,
    boot=BOOT_N, family=None, progress=True,
):
    """Walk-forward the family. `net`/`hit` are the outcome cubes from build_outcome_cube.

    Returns rows (one per rule x strike x exit), the luck summary, and enough
    winning-parameter codes to rebuild the top entries.
    """
    specs = list(family) if family is not None else build_family()
    primary_i = exits.index(PRIMARY_EXIT) if PRIMARY_EXIT in exits else 0
    folds = walk_forward_folds(panel.shape[0], K_FOLDS)
    for train, test in folds:
        if len(train) and len(test) and int(train.max()) >= int(test.min()):
            raise RuntimeError("walk-forward train overlaps test")
    oos_index = _oos_index(folds, panel.shape[0])
    n_oos = int((oos_index >= 0).sum())
    # Legs that are cooldown catalogs: everything except daily-signed, which is a mix of the always grids.
    always_call = _cond("always", "", "all", "call", -1, "base")
    always_put = _cond("always", "", "all", "put", -1, "base")
    legs = []
    seen = set()
    for spec in specs:
        if spec.minute_gate is not None or is_daily_signed(spec.leg):
            continue
        if spec.leg.id not in seen:
            seen.add(spec.leg.id)
            legs.append(spec.leg)
    for leg in (always_call, always_put):
        if leg.id not in seen:
            seen.add(leg.id)
            legs.append(leg)
    if progress:
        sc._print_scrubbed(f"  rules {len(specs)}  catalog legs {len(legs)}  oos days {n_oos}")
    catalog = build_leg_catalog(panel, legs, folds, net, hit, min_quantile_n, progress=progress)
    # always packs are fold-independent in the masks (all minutes) but the function refits per fold.
    # They are in the catalog under always|call and always|put. Daily signed reads fold 0's pack
    # only if the mask is identical every fold, which it is. Use each fold's own pack anyway.
    rows = []
    stored = []
    n_k = net.shape[4]
    n_e = len(exits)
    for si, spec in enumerate(specs):
        always = None
        if is_daily_signed(spec.leg) or spec.day_gate is not None:
            always = (
                catalog[always_call.id],
                catalog[always_put.id],
            )
        # _stitch_spec expects `always` as a pair of packs for the CURRENT fold.
        # Pass the catalog slices via a small adapter inside the stitch by fold.
        oos_s, oos_c, oos_h, codes = _stitch_spec_adapt(
            panel, spec, folds, catalog, always_call, always_put, net, hit,
            min_quantile_n, min_train, oos_index, primary_i,
        )
        sensitive = is_shuffle_sensitive(spec)
        for k, strike in enumerate(strike_names):
            for e, (tp, sl, ts) in enumerate(exits):
                stats = _row_stats(
                    oos_s[:, k, e], oos_c[:, k, e], oos_h[:, k, e],
                    folds, oos_index, boot, sc.stream_seed("edge-boot", spec.name, strike, e, seed),
                )
                rid = f"{spec.name}|{strike}|tp{tp:.2f}|sl{_fmt_sl(sl)}|t{ts}"
                row = {
                    "rule_id": rid,
                    "name": spec.name,
                    "kind": spec.kind,
                    "strike": strike,
                    "tp": tp,
                    "sl": sl,
                    "time_stop": ts,
                    "q_fdr": float("nan"),
                    "random_n": 0,
                    "random_mean_net_pct": float("nan"),
                    "random_hit_rate": float("nan"),
                    "beats_random": 0,
                    "candidate": 0,
                    "sensitive": int(sensitive),
                    "train_params": _param_text(spec, codes[:, k:k + 1]),
                    "spec_index": si,
                    "strike_index": k,
                    "exit_index": e,
                    **stats,
                }
                rows.append(row)
        stored.append({"spec": spec, "codes": codes, "sensitive": sensitive})
        if progress and (si + 1) % 200 == 0:
            sc._print_scrubbed(f"  scored {si + 1}/{len(specs)} setups")
    real_best = _best_mean(rows)
    luck = _luck(
        panel, stored, rows, folds, catalog, always_call, always_put, net, hit,
        min_quantile_n, min_train, oos_index, n_shuf, seed, real_best, progress, primary_i,
    )
    _attach_random(panel, rows, stored, folds, net, hit, min_quantile_n, seed, progress)
    pvals = []
    for row in rows:
        if row["n"] >= 2 and math.isfinite(row["t"]):
            pvals.append(row["p"])
        else:
            pvals.append(1.0)
    qvals = fdr_qvalues(pvals, family_n=len(rows))
    for row, qv in zip(rows, qvals):
        row["q_fdr"] = float(qv)
        rm = row["random_mean_net_pct"]
        row["beats_random"] = int(
            math.isfinite(row["mean_net_pct"]) and math.isfinite(rm) and row["mean_net_pct"] > rm
        )
        row["candidate"] = int(
            math.isfinite(row["mean_net_pct"]) and row["mean_net_pct"] > 0
            and row["beats_random"] == 1
            and row["folds_positive"] >= 3
        )
    return {
        "rows": rows,
        "stored": stored,
        "luck": luck,
        "folds": folds,
        "family_size": len(rows),
        "n_specs": len(specs),
        "real_best": real_best,
        "oos_index": oos_index,
    }


def _stitch_spec_adapt(panel, spec, folds, catalog, always_call, always_put, net, hit, min_n, min_train, oos_index, primary_i=PRIMARY_I):
    """Like _stitch_spec, but daily-signed packs are built from that fold's always catalog."""
    n_oos = int((oos_index >= 0).sum())
    n_k = net.shape[4]
    n_e = net.shape[5]
    oos_s = np.zeros((n_oos, n_k, n_e), dtype=np.float64)
    oos_c = np.zeros((n_oos, n_k, n_e), dtype=np.float64)
    oos_h = np.zeros((n_oos, n_k, n_e), dtype=np.float64)
    codes = np.full((len(folds), n_k), -1, dtype=int)
    for fi, (train, test) in enumerate(folds):
        if is_daily_signed(spec.leg):
            legs = []
            for param in param_grid(spec.leg):
                legs.append(_daily_signed_pack(
                    panel, spec.leg, train, param, min_n,
                    catalog[always_call.id][fi][0],
                    catalog[always_put.id][fi][0],
                ))
            gates = _gate_rows_for(panel, spec, train, min_n) if spec.day_gate is not None else [
                np.ones(panel.shape[:2], dtype=bool)
            ]
            # Daily signed specs in this family have day_gate None. A pair would pass a gate.
            if spec.day_gate is None:
                gates = [np.ones(panel.shape[:2], dtype=bool)]
        elif spec.minute_gate is not None:
            legs, _ = _leg_rows_for(
                panel, spec, train, fi, catalog, None, min_n, net, hit,
            )
            gates = [np.ones(panel.shape[:2], dtype=bool)]
        else:
            legs = catalog[spec.leg.id][fi]
            gates = _gate_rows_for(panel, spec, train, min_n)
        code, n_p = _select_codes(gates, legs, train, min_train, primary_i)
        codes[fi] = code
        mixed_s, mixed_c, mixed_h = _mix_packs(gates, legs, code, n_p)
        block = oos_index[test]
        oos_s[block] += mixed_s[test].sum(axis=1)
        oos_c[block] += mixed_c[test].sum(axis=1)
        oos_h[block] += mixed_h[test].sum(axis=1)
    return oos_s, oos_c, oos_h, codes


def _best_mean(rows):
    vals = [r["mean_net_pct"] for r in rows if math.isfinite(r["mean_net_pct"])]
    if not vals:
        return float("nan")
    return float(max(vals))


def _luck(
    panel, stored, rows, folds, catalog, always_call, always_put, net, hit,
    min_n, min_train, oos_index, n_shuf, seed, real_best, progress, primary_i,
):
    if n_shuf <= 0:
        return luck_shuffle_benchmark([], [])
    insensitive = []
    for row in rows:
        if not row["sensitive"] and math.isfinite(row["mean_net_pct"]):
            insensitive.append(row["mean_net_pct"])
    ins_best = max(insensitive) if insensitive else float("nan")
    eps = 1e-9
    bar = real_best
    ins_count = 0
    if math.isfinite(bar):
        ins_count = sum(1 for v in insensitive if v >= bar - eps)
    perms = day_label_permutations(panel.shape[0], n_shuf, seed)
    per_best = np.empty(n_shuf, dtype=float)
    per_count = np.empty(n_shuf, dtype=float)
    sensitive_idx = [i for i, st in enumerate(stored) if st["sensitive"]]
    for s_i, perm in enumerate(perms):
        shuf = panel.shuffled(perm)
        best = ins_best
        count = ins_count
        for si in sensitive_idx:
            spec = stored[si]["spec"]
            oos_s, oos_c, _h, _c = _stitch_spec_adapt(
                shuf, spec, folds, catalog, always_call, always_put, net, hit,
                min_n, min_train, oos_index, primary_i,
            )
            totals_c = oos_c.sum(axis=0)
            totals_s = oos_s.sum(axis=0)
            with np.errstate(invalid="ignore", divide="ignore"):
                means = np.where(totals_c > 0, totals_s / totals_c, np.nan)
            finite = means[np.isfinite(means)]
            if len(finite):
                local = float(finite.max())
                if not math.isfinite(best) or local > best:
                    best = local
                if math.isfinite(bar):
                    count += int(np.sum(finite >= bar - eps))
        per_best[s_i] = best
        per_count[s_i] = count
        if progress and (s_i + 1) % 20 == 0:
            sc._print_scrubbed(f"  luck shuffle {s_i + 1}/{n_shuf}")
    return luck_shuffle_benchmark(per_best, per_count)


def _attach_random(panel, rows, stored, folds, net, hit, min_n, seed, progress):
    """Matched random for every setup that actually traded, once per strike (entries are shared across exits)."""
    by_key = {}
    for row in rows:
        if row["n"] <= 0:
            continue
        by_key.setdefault((row["spec_index"], row["strike_index"]), []).append(row)
    done = 0
    for (si, k), group in by_key.items():
        spec = stored[si]["spec"]
        codes = stored[si]["codes"]
        day, sym, minute, side, _fold = materialize_entries(
            panel, spec, folds, codes, k, min_n, net, hit,
        )
        if len(day) == 0:
            continue
        rnd_seed = sc.stream_seed("edge-rnd", spec.name, group[0]["strike"], seed)
        draw = draw_matched_minutes(minute, rnd_seed)
        means, ns, hits, _cur = matched_random_lookup(
            day, sym, minute, side, draw, net, hit, k, seed=rnd_seed + 3,
        )
        for row in group:
            e = row["exit_index"]
            row["random_mean_net_pct"] = float(means[e]) if e < len(means) else float("nan")
            row["random_n"] = int(ns[e]) if e < len(ns) else 0
            row["random_hit_rate"] = float(hits[e]) if e < len(hits) else float("nan")
            row["_entries"] = (day, sym, minute, side)
            row["_draw"] = draw
        done += 1
        if progress and done % 200 == 0:
            sc._print_scrubbed(f"  random books {done}/{len(by_key)}")


# -------------------------------------------------------------------------------- report


def _fmt_num(x, nd=2):
    if x is None or not isinstance(x, (int, float)) or not math.isfinite(float(x)):
        return ""
    return f"{float(x):.{nd}f}"


def _fmt_pct(x):
    if x is None or not isinstance(x, (int, float)) or not math.isfinite(float(x)):
        return ""
    return f"{float(x):+.1f}%"


def _exit_label(row):
    sl = "no stop" if row["sl"] is None else f"stop {float(row['sl']) * 100:.0f}%"
    return f"target {float(row['tp']) * 100:.0f}% / {sl} / {int(row['time_stop'])}m"


def _table(rows, limit=None):
    show = rows if limit is None else rows[:limit]
    lines = [
        "| Rule | Strike | Exit | OOS net | Trades | Hit | t | Folds + | 95% CI | Random | Candidate |",
        "|---|---|---|---:|---:|---:|---:|---:|---|---:|---|",
    ]
    for r in show:
        hit = "" if not math.isfinite(r["hit_rate"]) else f"{r['hit_rate'] * 100:.0f}%"
        ci = ""
        if math.isfinite(r["boot_lo"]) and math.isfinite(r["boot_hi"]):
            ci = f"{r['boot_lo']:+.1f}% to {r['boot_hi']:+.1f}%"
        lines.append(
            "| {name} | {strike} | {exit} | {net} | {n} | {hit} | {t} | {fp}/5 | {ci} | {rnd} | {cand} |".format(
                name=r["name"],
                strike=r["strike"],
                exit=_exit_label(r),
                net=_fmt_pct(r["mean_net_pct"]),
                n=r["n"],
                hit=hit,
                t=_fmt_num(r["t"], 2),
                fp=r["folds_positive"],
                ci=ci,
                rnd=_fmt_pct(r["random_mean_net_pct"]),
                cand="yes" if r["candidate"] else "no",
            )
        )
    if not show:
        lines.append("|  |  |  |  |  |  |  |  |  |  |  |")
    return "\n".join(lines)


def render_report(meta, rows):
    ranked = sorted(
        [r for r in rows if math.isfinite(r["mean_net_pct"])],
        key=lambda r: r["mean_net_pct"],
        reverse=True,
    )
    candidates = [r for r in ranked if r["candidate"]]
    best = ranked[0] if ranked else None
    luck = meta["luck"]
    n_cand = len(candidates)
    best_txt = "no scored trades"
    if best is not None:
        best_txt = f"{_fmt_pct(best['mean_net_pct'])} on {best['name']} ({best['strike']}, {_exit_label(best)})"
    luck_best = luck.get("best_oos_net", float("nan"))
    luck_med = luck.get("median_best_oos_net", float("nan"))
    luck_n = luck.get("expected_rules_as_good", float("nan"))
    lines = []
    lines.append(f"# Edge hunt ({meta['stamp']})")
    lines.append("")
    lines.append(
        f"**Verdict:** {n_cand} candidate rule{'s' if n_cand != 1 else ''}. "
        f"Best real out-of-sample net is {best_txt}. "
        f"Luck benchmark (best out-of-sample net across {luck.get('n_shuf', 0)} shuffles of the daily labels): "
        f"{_fmt_pct(luck_best) or 'n/a'}. "
        f"Median of those per-shuffle bests: {_fmt_pct(luck_med) or 'n/a'}. "
        f"Rules expected to look at least this good by luck: {_fmt_num(luck_n, 2) or 'n/a'}."
    )
    lines.append("")
    lines.append(
        "A candidate must do all three: out-of-sample mean net above 0 after costs, "
        "mean net above its matched random book, and a positive fold mean in at least 3 of 5 folds. "
        "The top 30 below are ranked by out-of-sample net even when they are not candidates."
    )
    lines.append("")
    lines.append(f"**Data span:** {meta['span']}")
    lines.append("")
    lines.append(
        f"Family size: {meta['family_size']} "
        f"({meta['n_specs']} setups x {meta['n_strikes']} strikes x {meta['n_exits']} exits). "
        f"Benjamini-Hochberg uses that full family as N. "
        f"Primary selection exit: target 15%, stop 20%, 10-minute time stop. "
        f"The same chosen thresholds are then scored at 10% and 20% targets, stops 10%, 20%, and none, "
        f"and time stops of 10 and 30 minutes."
    )
    lines.append("")
    lines.append("## Candidates")
    lines.append("")
    if candidates:
        lines.append(_table(candidates, limit=40))
        if len(candidates) > 40:
            lines.append("")
            lines.append(f"{len(candidates) - 40} more candidates are in the CSV.")
    else:
        lines.append("No rule cleared the candidate bar on the out-of-sample folds.")
    lines.append("")
    lines.append("## Top 30 by out-of-sample net")
    lines.append("")
    lines.append("These are the highest out-of-sample means. A 'no' in the candidate column failed the bar above. They are not a trade list.")
    lines.append("")
    lines.append(_table(ranked, limit=30))
    lines.append("")
    lines.append("## What was searched")
    lines.append("")
    lines.append(family_blurb())
    lines.append("")
    lines.append(reversal_blurb())
    lines.append("")
    lines.append(meta["method"])
    lines.append("")
    lines.append("## Limits")
    lines.append("")
    lines.append(meta["limits"])
    lines.append("")
    lines.append("Data only. Research tool, not trading advice. No order is sent.")
    lines.append("")
    return "\n".join(lines)


def _write_csv(path, fields, rows):
    tmp = path + ".tmp"
    with open(tmp, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        for row in rows:
            out = {}
            for k in fields:
                v = row.get(k, "")
                if isinstance(v, float):
                    out[k] = "" if not math.isfinite(v) else f"{v:.6f}"
                elif isinstance(v, (list, tuple)):
                    out[k] = ";".join("" if (isinstance(x, float) and not math.isfinite(x)) else f"{x:.4f}" for x in v)
                elif v is None:
                    out[k] = ""
                else:
                    out[k] = v
            w.writerow(out)
    os.replace(tmp, path)


def _method_text(costs, premium, strikes):
    cent, pct, comm = costs
    lo, hi = premium
    return (
        f"Costs match scalp_real: half-spread per side is max({cent * 100:.0f} cents, {pct * 100:.1f}% of premium), "
        f"commission ${comm:.2f} per contract per side, one contract. "
        f"Entry is the next real option open after the signal bar (that minute, or the next minute if it has no print), "
        f"plus the half-spread. Exit is the bid-side proxy from scalp_real.simulate_trade. "
        f"Premium band ${lo:.2f} to ${hi:.2f}. Strikes: {', '.join(strikes)}. "
        f"Cooldown {COOLDOWN} minutes per rule per day. Calls win if call and put both fire on the same minute. "
        f"Walk-forward: sessions split into {K_FOLDS + 1} chronological blocks; the first block is train only; "
        f"each of the {K_FOLDS} later blocks is an out-of-sample fold trained on every earlier block. "
        f"Quantile cuts and fixed grids ({', '.join(str(x) for x in STRETCHES)} ATR, "
        f"VIX-fix levels {', '.join(str(int(x)) for x in WVF_LEVELS)}) are chosen only on that training prefix, "
        f"by mean net on the 15%/20%/10-minute exit, with at least the minimum train trade count. "
        f"Matched random uses the same days, the same strike and premium band, the same exit, "
        f"and the rule's own entry-clock distribution (a one-minute spike falls back to its 30-minute bucket). "
        f"Day-clustered t and a day-resampled 95% bootstrap describe the pooled out-of-sample trades. "
        f"The luck benchmark permutes daily-feature labels across sessions ({N_SHUFFLE} times unless quick or overridden), "
        f"refits every daily-context rule, and leaves intraday rules as they were."
    )


def _limits_text():
    return (
        "Long premium only, one contract, no spreads. "
        "A 30-minute time stop can still be open when the next entry fires 10 minutes later, so trades can overlap; "
        "the number above is per trade, not a one-position account path. "
        "The half-spread is a proxy, not the quote. "
        "Thresholds are fit on one primary exit per strike, then reused for the other exits, and those other exits still count in the family. "
        "Pairs are daily context with a setup, and reversal events with a short gate list, not every pair of indicators. "
        "A rule that trades almost every eligible minute on a 'good' day will look like its matched random, "
        "because the random book is drawn on those same days at the same clock. Its expectancy is still in the top 30 and the CSV. "
        "The candidate flag is the stricter test: better minutes than that random book. "
        "Shuffling daily labels does not break an intraday event, so the luck benchmark is a floor under the best intraday result "
        "and a null for the daily-context rules. "
        "VIX is the prior daily close (FRED VIXCLS, Yahoo ^VIX if FRED fails), not an intraday VIX. "
        "Relative volume needs 20 prior sessions; early days stay blank. "
        "This is a search of a predeclared family. It is not a promise that a candidate will keep working."
    )


# -------------------------------------------------------------------------------- data plumbing


def _http_text(url, timeout=45):
    req = urllib.request.Request(url, headers={"User-Agent": "edge-hunt-research"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read().decode("utf-8", errors="replace")


def _parse_fred_vix(text):
    out = {}
    for line in text.splitlines()[1:]:
        parts = line.strip().split(",")
        if len(parts) < 2:
            continue
        raw = parts[1].strip()
        if not raw or raw == ".":
            continue
        try:
            out[datetime.strptime(parts[0][:10], "%Y-%m-%d").date()] = float(raw)
        except ValueError:
            continue
    return out


def _parse_yahoo_csv(text):
    out = {}
    for line in text.splitlines()[1:]:
        parts = line.strip().split(",")
        if len(parts) < 5:
            continue
        try:
            out[datetime.strptime(parts[0][:10], "%Y-%m-%d").date()] = float(parts[4])
        except ValueError:
            continue
    return out


def _yahoo_vix_url():
    end = datetime.now(timezone.utc)
    start = end - timedelta(days=365 * 6)
    p1 = int(start.timestamp())
    p2 = int(end.timestamp())
    return (
        "https://query1.finance.yahoo.com/v7/finance/download/%5EVIX"
        f"?period1={p1}&period2={p2}&interval=1d&events=history"
    )


def load_vix_closes(synthetic_days=None):
    """Prior-day VIX closes. FRED first, Yahoo CSV if FRED fails. Synthetic mode skips the network."""
    if synthetic_days is not None:
        start = synthetic_days[0] - timedelta(days=40)
        out = {}
        for i, ts in enumerate(pd.bdate_range(start, synthetic_days[-1])):
            out[ts.date()] = 14.0 + (i % 9) * 0.7
        return out, "synthetic"
    try:
        parsed = _parse_fred_vix(_http_text(FRED_VIX_URL))
        if len(parsed) >= 10:
            return parsed, "FRED VIXCLS"
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        sc._print_scrubbed(f"  VIX FRED failed: {type(exc).__name__}")
    try:
        parsed = _parse_yahoo_csv(_http_text(_yahoo_vix_url()))
        if len(parsed) >= 10:
            return parsed, "Yahoo ^VIX"
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        sc._print_scrubbed(f"  VIX Yahoo failed: {type(exc).__name__}")
    raise SystemExit("Could not download VIX closes from FRED or Yahoo. Nothing was scored.")


class _Limiter:
    def __init__(self, interval):
        self.interval = float(interval)
        self.lock = threading.Lock()
        self.next_t = 0.0

    def wait(self):
        with self.lock:
            now = time.monotonic()
            delay = max(0.0, self.next_t - now)
            self.next_t = max(now, self.next_t) + self.interval
        if delay:
            time.sleep(delay)


def _cache_file(cache_dir, day):
    return os.path.join(cache_dir, f"{day.isoformat()}.pkl")


def load_cached_day(cache_dir, day):
    path = _cache_file(cache_dir, day)
    if not os.path.exists(path):
        return {}
    try:
        with open(path, "rb") as f:
            got = pickle.load(f)
    except (OSError, pickle.UnpicklingError, EOFError):
        return {}
    return got if isinstance(got, dict) else {}


def store_cached_day(cache_dir, day, mapping):
    os.makedirs(cache_dir, exist_ok=True)
    path = _cache_file(cache_dir, day)
    tmp = path + ".tmp"
    with open(tmp, "wb") as f:
        pickle.dump(mapping, f, protocol=pickle.HIGHEST_PROTOCOL)
    os.replace(tmp, path)


def fetch_option_days(needed, und, symbols, synthetic, cache_dir, workers=2, interval=0.35):
    """Download each day's contracts once, with a disk cache, a small pool, and retries inside scalp_real."""
    opt = {}
    missing = {}
    for day, contracts in needed.items():
        cached = {} if synthetic else load_cached_day(cache_dir, day)
        have = {}
        need = []
        for contract in contracts:
            if contract in cached:
                have[contract] = cached[contract]
            else:
                need.append(contract)
        for contract, rec in have.items():
            opt[(day, contract)] = rec
        if need:
            missing[day] = need
    if not missing:
        return opt
    if synthetic:
        got = sc._fetch_all(None, missing, und, True, symbols)
        opt.update(got)
        return opt
    key = os.getenv("ALPACA_KEY", "").strip()
    sec = os.getenv("ALPACA_SECRET", "").strip()
    if not key or not sec:
        raise SystemExit("ALPACA_KEY / ALPACA_SECRET are missing. Add them in Settings > Secrets and variables > Actions.")
    from alpaca.data.historical import OptionHistoricalDataClient

    limiter = _Limiter(interval)
    lock = threading.Lock()
    local = threading.local()

    def client():
        oc = getattr(local, "oc", None)
        if oc is None:
            oc = sc._CacheClient(OptionHistoricalDataClient(key, sec))
            local.oc = oc
        return oc

    def one(day):
        limiter.wait()
        contracts = missing[day]
        try:
            recs = sc.fetch_option_day(client(), contracts, day)
        except Exception as exc:  # noqa: BLE001
            sc._print_scrubbed(f"  option day {day} failed: {sc._scrub(exc)[:180]}")
            return day, {}
        return day, recs

    days = sorted(missing)
    with_workers = max(1, int(workers))
    if with_workers == 1:
        results = [one(day) for day in days]
    else:
        from concurrent.futures import ThreadPoolExecutor
        with ThreadPoolExecutor(max_workers=with_workers) as pool:
            results = list(pool.map(one, days))
    for day, recs in results:
        if not recs:
            continue
        merged = load_cached_day(cache_dir, day)
        merged.update(recs)
        store_cached_day(cache_dir, day, merged)
        with lock:
            for contract, rec in recs.items():
                opt[(day, contract)] = rec
        sc._print_scrubbed(f"  options {day} contracts {len(recs)}")
    return opt


def contracts_for_minutes(days, symbols, und, strikes):
    """Every contract the entry search can touch, including the one-minute slip."""
    bt = sc._bt()
    needed = {}
    for day in days:
        bag = set()
        for sym in symbols:
            sess = und[sym].get(day)
            if sess is None:
                continue
            for m in range(FIRST_ENTRY, min(LAST_ENTRY + 2, N_MIN)):
                spot = sc.spot_at(sess, m)
                if spot is None:
                    continue
                for side in (1, -1):
                    cp = "C" if side == 1 else "P"
                    for mode in strikes:
                        k = sc.strike_price(spot, side, mode)
                        if k is None:
                            continue
                        bag.add(bt.lab_occ(sym, day, cp, k))
        if bag:
            needed[day] = bag
    return needed


def _env_flag(name):
    return os.getenv(name, "").strip().lower() in {"1", "true", "yes", "y"}


def _env_int(name, default):
    raw = os.getenv(name, "").strip()
    return int(raw) if raw else default


def _env_float(name, default):
    raw = os.getenv(name, "").strip()
    return float(raw) if raw else default


def _parse_strikes(raw):
    parts = [p.strip().lower() for p in (raw or "").split(",") if p.strip()]
    bad = [p for p in parts if p not in sc.STRIKE_MODES]
    if bad or not parts:
        raise SystemExit(f"strikes must be a subset of {', '.join(sc.STRIKE_MODES)}")
    return tuple(parts)


def _parse_premium(lo_raw, hi_raw):
    lo = float(lo_raw) if str(lo_raw).strip() else 0.45
    hi = float(hi_raw) if str(hi_raw).strip() else 0.80
    if lo < 0 or hi < 0 or lo > hi:
        raise SystemExit("premium band is invalid")
    return (lo, hi)


def _top_rules(rows, n=30):
    ranked = sorted(
        [r for r in rows if math.isfinite(r["mean_net_pct"])],
        key=lambda r: r["mean_net_pct"],
        reverse=True,
    )
    return ranked[:n]


def trades_from_entries(entries, und, opt, symbols, days, strikes, exits, costs, premium, meta_rows):
    """Re-simulate the top rules and their matched random minutes for the trade CSV."""
    bt = sc._bt()
    out = []
    day_list = list(days)
    for row in meta_rows:
        packed = row.get("_entries")
        draw = row.get("_draw")
        if not packed:
            continue
        day_i, sym_i, minute, side, = packed
        books = (("rule", minute), ("random", draw if draw is not None else minute))
        strike = row["strike"]
        cfg = (row["tp"], row["sl"], row["time_stop"])
        strike_i = strikes.index(strike)
        for book, mins in books:
            # One exit per row, so filter to this row's exit by re-simulating that exit only.
            for i in range(len(day_i)):
                di = int(day_i[i])
                si = int(sym_i[i])
                m = int(mins[i])
                sd = 1 if int(side[i]) == 0 else -1
                day = day_list[di]
                sym = symbols[si]
                sess = und[sym].get(day)
                if sess is None:
                    continue
                # Slip the same way the cube did: try m, then m+1 if no print.
                trial = None
                contract = ""
                for step in (0, 1):
                    mm = m + step
                    if mm > LAST_ENTRY or mm >= N_MIN:
                        break
                    spot = sc.spot_at(sess, mm)
                    if spot is None:
                        continue
                    k = sc.strike_price(spot, sd, strike)
                    if k is None:
                        continue
                    contract = bt.lab_occ(sym, day, "C" if sd == 1 else "P", k)
                    book_opt = opt.get((day, contract))
                    if book_opt is None:
                        continue
                    got = sc.simulate_trade(book_opt, mm, cfg, costs, allow_slip=False, premium=premium)
                    if got["status"] == "skip_entry":
                        continue
                    trial = got
                    break
                if trial is None or trial["status"] != "fill":
                    continue
                hh, mm = divmod((9 * 60 + 30) + int(trial["entry_min"]), 60)
                out.append({
                    "date": day.isoformat(),
                    "time": f"{hh:02d}:{mm:02d}",
                    "symbol": sym,
                    "side": "CALL" if sd == 1 else "PUT",
                    "entry": f"{trial['entry']:.4f}",
                    "exit": f"{trial['exit']:.4f}",
                    "reason": trial["reason"],
                    "net_pct": f"{trial['net_pct']:.4f}",
                    "rule_id": row["rule_id"],
                    "rule": row["name"],
                    "strike": strike,
                    "tp": f"{row['tp']:.2f}",
                    "sl": _fmt_sl(row["sl"]),
                    "time_stop": row["time_stop"],
                    "book": book,
                    "contract": contract,
                    "fold": "",
                })
    return out


def _empty_report(path, message):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w") as f:
        f.write("# Edge hunt\n\n" + message + "\n\nData only. Research tool, not trading advice.\n")


def main():
    t0 = time.time()
    out_dir = os.getenv("EDGE_OUT", "results").strip() or "results"
    os.makedirs(out_dir, exist_ok=True)
    quick = _env_flag("EDGE_QUICK")
    days_n = 30 if quick else _env_int("EDGE_DAYS", 170)
    if days_n < K_FOLDS + 1:
        raise SystemExit(f"days must be at least {K_FOLDS + 1}")
    symbols = [s.strip().upper() for s in os.getenv("EDGE_SYMBOLS", "SPY,QQQ").split(",") if s.strip()]
    strikes = _parse_strikes(os.getenv("EDGE_STRIKES", "1otm,atm"))
    premium = _parse_premium(os.getenv("EDGE_PREMIUM_MIN", "0.45"), os.getenv("EDGE_PREMIUM_MAX", "0.80"))
    cent = _env_float("EDGE_HALF_SPREAD_CENTS", 1.0) / 100.0
    pct = _env_float("EDGE_HALF_SPREAD_PCT", 0.5) / 100.0
    commission = _env_float("EDGE_COMMISSION", 0.65)
    costs = (cent, pct, commission)
    n_shuf = _env_int("EDGE_SHUFFLES", 20 if quick else N_SHUFFLE)
    boot = _env_int("EDGE_BOOT", 200 if quick else BOOT_N)
    synthetic = _env_flag("EDGE_SYNTH")
    cache_dir = os.getenv("EDGE_CACHE", "/tmp/edge-hunt-cache").strip() or "/tmp/edge-hunt-cache"
    workers = _env_int("EDGE_WORKERS", 2)
    min_train = _env_int("EDGE_MIN_TRAIN", 8 if quick else MIN_TRAIN)
    min_q = _env_int("EDGE_MIN_QUANTILE", 15 if quick else MIN_QUANTILE_N)

    now = datetime.now(NY)
    end = datetime.now(timezone.utc) - timedelta(minutes=20)
    start = (pd.Timestamp(now.date(), tz=NY) - pd.Timedelta(days=int(days_n * 3 + 90))).tz_convert("UTC").to_pydatetime()
    sc._print_scrubbed(
        f"edge hunt symbols {', '.join(symbols)} days {days_n} quick {int(quick)} synthetic {int(synthetic)}"
    )
    frames = sc._load_underlying(symbols, start, end, synthetic)
    und = {sym: sc.rth_session(df) for sym, df in frames.items()}
    all_days = sc.complete_days(und, symbols, now)
    if len(all_days) < K_FOLDS + 1:
        _empty_report(os.path.join(out_dir, "EDGE_HUNT.md"), "Not enough completed sessions to score.")
        raise SystemExit("Not enough completed sessions.")
    score_days = all_days[-days_n:]
    vix, vix_source = load_vix_closes(score_days if synthetic else None)
    sc._print_scrubbed(f"  VIX source {vix_source} points {len(vix)}")
    panel = compute_features(frames, vix, score_days, symbols)
    needed = contracts_for_minutes(score_days, symbols, und, strikes)
    opt = fetch_option_days(needed, und, symbols, synthetic, cache_dir, workers=workers)
    live = []
    for day in score_days:
        if any(opt.get((day, c), {}).get("real", np.zeros(1)).any() for c in needed.get(day, ())):
            live.append(day)
    if len(live) < K_FOLDS + 1:
        _empty_report(
            os.path.join(out_dir, "EDGE_HUNT.md"),
            "Not enough sessions with OPRA 1-minute prints to score. Nothing was ranked.",
        )
        raise SystemExit("Not enough OPRA sessions.")
    # Keep the panel aligned with the days that actually have option prints.
    dropped = [d for d in score_days if d not in set(live)]
    if live != score_days:
        keep = [score_days.index(d) for d in live]
        panel = _subset_panel(panel, keep)
        score_days = live
    sc._print_scrubbed(f"  sessions {score_days[0]} .. {score_days[-1]} n {len(score_days)}")
    net, hit = build_outcome_cube(score_days, symbols, und, opt, strikes, EXITS, costs, premium)
    result = run_search(
        panel, net, hit, strikes, EXITS,
        n_shuf=n_shuf, boot=boot, min_train=min_train, min_quantile_n=min_q,
    )
    span = (
        f"{', '.join(symbols)}, {len(score_days)} completed sessions with option prints, "
        f"{score_days[0].isoformat()} through {score_days[-1].isoformat()}. "
        f"Warmup bars before {score_days[0].isoformat()} seed indicators, relative volume, and prior-day stats, and are not scored. "
        f"VIX: {vix_source}. Premium ${premium[0]:.2f} to ${premium[1]:.2f}. "
        f"Quick mode: {'yes, 30 sessions' if quick else 'no'}."
    )
    if dropped:
        span += f" Dropped {len(dropped)} sessions with no prints."
    meta = {
        "stamp": now.strftime("%Y-%m-%d %H:%M ET"),
        "span": span,
        "family_size": result["family_size"],
        "n_specs": result["n_specs"],
        "n_strikes": len(strikes),
        "n_exits": len(EXITS),
        "luck": result["luck"],
        "method": _method_text(costs, premium, strikes),
        "limits": _limits_text(),
    }
    text = render_report(meta, result["rows"])
    md_path = os.path.join(out_dir, "EDGE_HUNT.md")
    csv_path = os.path.join(out_dir, "edge_hunt_rules.csv")
    tr_path = os.path.join(out_dir, "edge_hunt_trades.csv")
    with open(md_path, "w") as f:
        f.write(text)
    _write_csv(csv_path, RULE_FIELDS, result["rows"])
    top = _top_rules(result["rows"], 30)
    # Attach entries for the top 30 if random pass already stored them; else materialize.
    for row in top:
        if "_entries" not in row:
            spec = result["stored"][row["spec_index"]]["spec"]
            codes = result["stored"][row["spec_index"]]["codes"]
            day, sym, minute, side, _fold = materialize_entries(
                panel, spec, result["folds"], codes, row["strike_index"], min_q, net, hit,
            )
            rnd_seed = sc.stream_seed("edge-rnd", spec.name, row["strike"], SEED)
            row["_entries"] = (day, sym, minute, side)
            row["_draw"] = draw_matched_minutes(minute, rnd_seed) if len(minute) else minute
    trade_rows = trades_from_entries(
        None, und, opt, symbols, score_days, list(strikes), EXITS, costs, premium, top,
    )
    _write_csv(tr_path, TRADE_FIELDS, trade_rows)
    summary = os.getenv("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a") as f:
            f.write(text + "\n")
    sc._print_scrubbed(f"wrote {md_path} {csv_path} {tr_path} in {(time.time() - t0) / 60:.1f} min")
    sc._print_scrubbed(text.split("\n\n")[1] if "\n\n" in text else text[:500])


def _subset_panel(panel, keep):
    """Drop sessions that had no option prints. keep is a list of row indices, chronological."""
    out = Panel([panel.days[i] for i in keep], panel.symbols)
    for name, arr in panel.f.items():
        out.f[name] = np.ascontiguousarray(arr[keep])
    for name, arr in panel.daily.items():
        out.daily[name] = np.ascontiguousarray(arr[keep])
    for name, arr in panel.ev.items():
        out.ev[name] = np.ascontiguousarray(arr[keep])
    out.shape = (len(keep), len(panel.symbols), N_MIN)
    return out


if __name__ == "__main__":
    main()
