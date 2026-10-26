"""
Greed/fear extreme fade on real 0DTE option prices, regular hours only.

DATA ONLY. This script reads historical bars. It does not import an order
client, submit orders, or send a trade. It is a research tool, not trading advice.

The supported run is .github/workflows/fgfade.yml (Actions tab,
"Fear-greed fade (real option prices)", Run workflow). A fresh run, not Re-run.
Keys come from the ALPACA_KEY and ALPACA_SECRET secrets and are never printed.

Outputs on the results branch (default fgfade-results, never main):
    results/FGFADE.md
    results/fgfade_summary.csv
    results/fgfade_trades.csv
    results/fgfade_folds.csv

Fills, costs, strike math, and the option-bar cache are reused from scalp_real.py
and edge_hunt.py. This file does not modify those modules or cleanbot.py.
"""

from __future__ import annotations

import csv
import math
import os
import time
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd

import edge_hunt as eh
import scalp_real as sc

NY = ZoneInfo("America/New_York")

# Pinned side (greed on a put, fear on a call) and the quiet side.
GREED_LEVELS = (80, 85, 90, 95)
FEAR_LEVELS = (5, 10, 20, 30)
TFS = (1, 3, 5)
BASE_VARIANTS = ("first", "turn", "turn_band", "turn_mom")
SQUEEZE_FILTERS = ("any", "released5", "on", "off")
CLUSTER_NS = (0, 1, 2, 3)
SIGNAL_LEN = 9
COOLDOWN = 20
HORIZON = 60
ENTRY_LO = 5       # 9:35
ENTRY_HI = 375     # 15:45
RELEASE_LOOK = 5
SQUEEZE_LEN = 20
BB_MULT = 2.0
KC_MULT = 1.5
K_FOLDS = 5
MIN_SELECT = 15
PREMIUM_BAND = (0.30, 1.00)
STRIKES = ("1otm", "atm")
BANDS = ("band", "any")
WINDOWS = (5, 15, 30, 60)
HIT_LEVELS = (0.10, 0.15, 0.20, 0.30)
HIT_15_30 = WINDOWS.index(30) * len(HIT_LEVELS) + HIT_LEVELS.index(0.15)
EXITS = (
    ("tp15_sl15", (0.15, 0.15, 60)),
    ("tp15_sl25", (0.15, 0.25, 60)),
    ("tp15_nostop_30", (0.15, None, 30)),
)
# Same bill as the edge hunt: 1 cent or 0.5% half-spread, $0.65 a side.
COSTS = (0.01, 0.005, 0.65)
FOCUS_DATES = tuple(datetime(2026, 10, 19).date() + timedelta(days=i) for i in range(5))
MISSING_KEYS = (
    "ALPACA_KEY / ALPACA_SECRET are missing. "
    "Add them in Settings > Secrets and variables > Actions."
)

# Event tuple: day index, symbol index, entry minute, side, pinned, fear, greed.
DI, SYM, MIN, SIDE, PIN, FEAR, GREED = range(7)


@dataclass(frozen=True)
class Cell:
    tf: int
    variant: str
    G: int
    F: int
    N: int | None = None
    squeeze: str | None = None

    @property
    def id(self):
        if self.variant == "all3":
            return f"tf{self.tf}_all3_n{self.N}_{self.squeeze}_g{self.G}_f{self.F}"
        return f"tf{self.tf}_{self.variant}_g{self.G}_f{self.F}"


def grid_cells(tfs=TFS):
    """Every predeclared setup. Both mirrors live inside one cell."""
    cells = []
    for tf in tfs:
        for g in GREED_LEVELS:
            for f in FEAR_LEVELS:
                for variant in BASE_VARIANTS:
                    cells.append(Cell(int(tf), variant, int(g), int(f)))
                for n in CLUSTER_NS:
                    for sq in SQUEEZE_FILTERS:
                        cells.append(Cell(int(tf), "all3", int(g), int(f), int(n), sq))
    return cells


def family_row_count(tfs=TFS):
    """Cells times strike (1otm, atm) times premium book (band, any)."""
    return len(grid_cells(tfs)) * len(STRIKES) * len(BANDS)


def first_in_run(flag, day_code):
    """True on the first bar of a same-day run. A new session starts a new run."""
    flag = np.asarray(flag, dtype=bool)
    day = np.asarray(day_code)
    if len(flag) == 0:
        return flag.copy()
    prev = np.zeros(len(flag), dtype=bool)
    prev[1:] = flag[:-1] & (day[1:] == day[:-1])
    return flag & ~prev


def _same_day(day, lag):
    out = np.zeros(len(day), dtype=bool)
    if lag <= 0 or lag >= len(day):
        return out
    out[lag:] = day[lag:] == day[:-lag]
    return out


def side_turn(level, other, level_thr, other_max, signal, day_code):
    """Pinned side leaves its extreme.

    The prior bar was pinned (level >= level_thr and the other side <= other_max).
    This bar either drops off that peak (lower than the prior bar, and the prior
    bar was not already falling) or crosses under its signal line. The signal
    line is the SMA of `level`. Nothing crosses a session boundary.
    """
    level = np.asarray(level, dtype=float)
    other = np.asarray(other, dtype=float)
    signal = np.asarray(signal, dtype=float)
    day = np.asarray(day_code)
    n = len(level)
    out = np.zeros(n, dtype=bool)
    if n < 2:
        return out
    same = _same_day(day, 1)
    prev_ext = np.zeros(n, dtype=bool)
    prev_ext[1:] = (
        (level[:-1] >= float(level_thr))
        & (other[:-1] <= float(other_max))
        & np.isfinite(level[:-1])
        & np.isfinite(other[:-1])
    )
    drop = np.zeros(n, dtype=bool)
    if n >= 3:
        same2 = _same_day(day, 1).copy()
        same2[2:] = (day[2:] == day[1:-1]) & (day[1:-1] == day[:-2])
        drop[2:] = (
            (level[2:] < level[1:-1])
            & (level[1:-1] >= level[:-2])
            & np.isfinite(level[2:])
            & np.isfinite(level[1:-1])
            & np.isfinite(level[:-2])
            & same2[2:]
        )
    cross = np.zeros(n, dtype=bool)
    cross[1:] = (
        (level[:-1] >= signal[:-1])
        & (level[1:] < signal[1:])
        & np.isfinite(level[:-1])
        & np.isfinite(level[1:])
        & np.isfinite(signal[:-1])
        & np.isfinite(signal[1:])
        & same[1:]
    )
    return prev_ext & same & (drop | cross)


def quiet_lift(quiet, pinned, pinned_thr, quiet_max, signal, day_code):
    """Quiet side lifts off its low while the prior bar was the extreme.

    Lift: this bar is higher than the prior bar, and the prior bar was not
    already rising. Or the series crosses up through its signal line.
    """
    quiet = np.asarray(quiet, dtype=float)
    pinned = np.asarray(pinned, dtype=float)
    signal = np.asarray(signal, dtype=float)
    day = np.asarray(day_code)
    n = len(quiet)
    if n < 2:
        return np.zeros(n, dtype=bool)
    same = _same_day(day, 1)
    prev_ext = np.zeros(n, dtype=bool)
    prev_ext[1:] = (
        (pinned[:-1] >= float(pinned_thr))
        & (quiet[:-1] <= float(quiet_max))
        & np.isfinite(pinned[:-1])
        & np.isfinite(quiet[:-1])
    )
    lift = np.zeros(n, dtype=bool)
    if n >= 3:
        same2 = np.zeros(n, dtype=bool)
        same2[2:] = (day[2:] == day[1:-1]) & (day[1:-1] == day[:-2])
        lift[2:] = (
            (quiet[2:] > quiet[1:-1])
            & (quiet[1:-1] <= quiet[:-2])
            & np.isfinite(quiet[2:])
            & np.isfinite(quiet[1:-1])
            & np.isfinite(quiet[:-2])
            & same2[2:]
        )
    cross = np.zeros(n, dtype=bool)
    cross[1:] = (
        (quiet[:-1] <= signal[:-1])
        & (quiet[1:] > signal[1:])
        & np.isfinite(quiet[:-1])
        & np.isfinite(quiet[1:])
        & np.isfinite(signal[:-1])
        & np.isfinite(signal[1:])
        & same[1:]
    )
    return prev_ext & same & (lift | cross)


def _mom_turn(mom, day_code, down):
    """Histogram ticks against the move after it was positive/rising (down) or negative/falling (up)."""
    m = np.asarray(mom, dtype=float)
    day = np.asarray(day_code)
    n = len(m)
    out = np.zeros(n, dtype=bool)
    if n < 2:
        return out
    same = _same_day(day, 1)
    if down:
        tick = np.zeros(n, dtype=bool)
        tick[1:] = (m[1:] < m[:-1]) & np.isfinite(m[1:]) & np.isfinite(m[:-1])
        armed = np.zeros(n, dtype=bool)
        armed[1:] = m[:-1] > 0
    else:
        tick = np.zeros(n, dtype=bool)
        tick[1:] = (m[1:] > m[:-1]) & np.isfinite(m[1:]) & np.isfinite(m[:-1])
        armed = np.zeros(n, dtype=bool)
        armed[1:] = m[:-1] < 0
    if n >= 3:
        same2 = np.zeros(n, dtype=bool)
        same2[2:] = (day[2:] == day[1:-1]) & (day[1:-1] == day[:-2])
        slope = np.zeros(n, dtype=bool)
        if down:
            slope[2:] = (m[1:-1] > m[:-2]) & np.isfinite(m[:-2]) & same2[2:]
        else:
            slope[2:] = (m[1:-1] < m[:-2]) & np.isfinite(m[:-2]) & same2[2:]
        armed = armed | slope
    return tick & armed & same


def mom_turn_down(mom, day_code):
    """Was positive or rising, then this bar is lower than the prior bar."""
    return _mom_turn(mom, day_code, True)


def mom_turn_up(mom, day_code):
    """Was negative or falling, then this bar is higher than the prior bar."""
    return _mom_turn(mom, day_code, False)


def last_true_index(flag, day_code):
    """Index of the latest True so far today, or -1. Yesterday does not carry."""
    flag = np.asarray(flag, dtype=bool)
    day = np.asarray(day_code)
    n = len(flag)
    out = np.full(n, -1, dtype=np.int32)
    if n == 0:
        return out
    starts = np.flatnonzero(np.r_[True, day[1:] != day[:-1]])
    ends = np.r_[starts[1:], n]
    for a, b in zip(starts, ends):
        idx = np.flatnonzero(flag[a:b])
        if len(idx) == 0:
            continue
        pos = np.arange(b - a)
        place = np.searchsorted(idx, pos, side="right") - 1
        good = place >= 0
        vals = np.full(b - a, -1, dtype=np.int32)
        vals[good] = (idx[place[good]] + a).astype(np.int32)
        out[a:b] = vals
    return out


def cluster_fires(pinned_turn, quiet_turn, mom_turn, extreme, n_bars, day_code):
    """First bar where the three turns and an extreme all sit in the last N bars.

    N is bars of this timeframe, looking backward only, and only inside the
    session. The flag does not fire again while that window stays complete.
    """
    n_bars = int(n_bars)
    if n_bars < 0:
        raise ValueError("n_bars must be >= 0")
    day = np.asarray(day_code)
    n = len(day)
    if n == 0:
        return np.zeros(0, dtype=bool)
    idx = np.arange(n)
    lo = idx - n_bars
    last_p = last_true_index(pinned_turn, day)
    last_q = last_true_index(quiet_turn, day)
    last_m = last_true_index(mom_turn, day)
    last_e = last_true_index(extreme, day)
    # -1 means "not yet today". A negative lookback must not treat that as a hit.
    ok = (
        (last_p >= 0) & (last_q >= 0) & (last_m >= 0) & (last_e >= 0)
        & (last_p >= lo) & (last_q >= lo) & (last_m >= lo) & (last_e >= lo)
    )
    return first_in_run(ok, day)


def released_recent(sq_on, day_code, lookback=RELEASE_LOOK):
    """Squeeze is off now, and it was on at least once in the prior `lookback` bars today."""
    on = np.asarray(sq_on, dtype=bool)
    day = np.asarray(day_code)
    n = len(on)
    recent = np.zeros(n, dtype=bool)
    for k in range(1, int(lookback) + 1):
        if k >= n:
            break
        recent[k:] |= on[:-k] & (day[k:] == day[:-k])
    return (~on) & recent


def squeeze_states(sq_on, day_code, lookback=RELEASE_LOOK):
    """on, released in the last `lookback` bars, and off. The three cover every bar once."""
    on = np.asarray(sq_on, dtype=bool)
    released = released_recent(on, day_code, lookback)
    off = ~on & ~released
    return on, released, off


def outside_band(close, vwap_up, vwap_dn, bb_up, bb_dn, side):
    """Put: close above the upper VWAP band or the upper Bollinger. Call: the mirror, below."""
    close = np.asarray(close, dtype=float)
    if int(side) == -1:
        return (close > np.asarray(vwap_up, dtype=float)) | (close > np.asarray(bb_up, dtype=float))
    if int(side) == 1:
        return (close < np.asarray(vwap_dn, dtype=float)) | (close < np.asarray(bb_dn, dtype=float))
    raise ValueError(side)


def apply_cooldown(events, gap=COOLDOWN):
    """One event per symbol per `gap` minutes.

    Same minute: the more extreme pinned reading wins. A tie keeps the put.
    """
    groups = {}
    for ev in events:
        groups.setdefault((ev[DI], ev[SYM]), []).append(ev)
    kept = []
    for rows in groups.values():
        rows.sort(key=lambda e: (e[MIN], -(e[PIN] if e[PIN] == e[PIN] else -1e9), e[SIDE]))
        chosen = []
        for ev in rows:
            if chosen and chosen[-1][MIN] == ev[MIN]:
                continue
            chosen.append(ev)
        last = -10_000
        for ev in chosen:
            if ev[MIN] - last >= int(gap):
                kept.append(ev)
                last = ev[MIN]
    kept.sort(key=lambda e: (e[DI], e[SYM], e[MIN], e[SIDE]))
    return kept


def random_minute(minute, rng, lo=ENTRY_LO, hi=ENTRY_HI, gap=COOLDOWN):
    """A minute in the same 30-minute bucket, at least `gap` minutes away.

    If that bucket has no such minute, use the whole entry window. The draw is
    the caller's rng, so one seed gives one clock for every cell.
    """
    minute = int(minute)
    bucket = lo + ((min(max(minute, lo), hi) - lo) // 30) * 30
    bucket_end = min(bucket + 30, hi + 1)
    cands = [m for m in range(max(bucket, lo), bucket_end) if abs(m - minute) >= gap]
    if not cands:
        cands = [m for m in range(lo, hi + 1) if abs(m - minute) >= gap]
    if not cands:
        return None
    return int(rng.choice(np.asarray(cands, dtype=int)))


def entry_minute_of(bar_start, tf, lo=ENTRY_LO, hi=ENTRY_HI):
    """Session minute of the 1-minute bar that opens as this chart bar closes.

    9:30 is 0. The bar is known at start + tf. Entries outside 9:35–15:45,
    and anything at or after the 15:55 flat, are dropped.
    """
    ent = int(bar_start) + int(tf)
    if ent < int(lo) or ent > int(hi) or ent >= sc.FLAT_MIN:
        return None
    return ent


def clock_hhmm(minute):
    total = 9 * 60 + 30 + int(minute)
    return f"{total // 60:02d}:{total % 60:02d}"


def ttm_squeeze(high, low, close):
    """TTM squeeze as in backtest.study_arrays: BB 20/2.0 inside KC 20/1.5.

    Keltner width is 1.5 times the 20-bar mean of true range, not an EMA ATR.
    Momentum is the 20-bar linear regression of close minus the LazyBear mid.
    """
    cs = pd.Series(np.asarray(close, dtype=float))
    hs = pd.Series(np.asarray(high, dtype=float))
    ls = pd.Series(np.asarray(low, dtype=float))
    basis = cs.rolling(SQUEEZE_LEN).mean()
    dev = BB_MULT * cs.rolling(SQUEEZE_LEN).std(ddof=0)
    prev = cs.shift(1)
    tr = pd.concat([hs - ls, (hs - prev).abs(), (ls - prev).abs()], axis=1).max(axis=1)
    kc = tr.rolling(SQUEEZE_LEN).mean()
    inside = ((basis - dev) > (basis - KC_MULT * kc)) & ((basis + dev) < (basis + KC_MULT * kc))
    sq = inside.fillna(False).to_numpy(dtype=bool)
    mid = ((hs.rolling(SQUEEZE_LEN).max() + ls.rolling(SQUEEZE_LEN).min()) / 2.0 + basis) / 2.0
    mom = sc._bt().linreg_last((cs - mid).to_numpy(dtype=float), SQUEEZE_LEN)
    return sq, np.asarray(mom, dtype=float), (basis + dev).to_numpy(dtype=float), (basis - dev).to_numpy(dtype=float)


def fear_greed(df):
    """Williams VIX Fix pane. 100 means the series is at its own 50-bar high."""
    fear, greed = sc._bt().vfx_pane(df)
    return np.asarray(fear, dtype=float), np.asarray(greed, dtype=float)


def _sma(values, length):
    return pd.Series(np.asarray(values, dtype=float)).rolling(int(length), min_periods=int(length)).mean().to_numpy(dtype=float)


def session_vwap(high, low, close, volume, day_code):
    """Session VWAP of typical price. Each day starts over."""
    tp = (np.asarray(high, float) + np.asarray(low, float) + np.asarray(close, float)) / 3.0
    vol = np.asarray(volume, float)
    vol = np.where(np.isfinite(vol) & (vol > 0), vol, 0.0)
    tp = np.where(np.isfinite(tp), tp, 0.0)
    day = np.asarray(day_code)
    n = len(day)
    if n == 0:
        return np.zeros(0, dtype=float)
    change = np.r_[True, day[1:] != day[:-1]]
    starts = np.flatnonzero(change)
    c_pv = np.cumsum(tp * vol)
    c_v = np.cumsum(vol)
    base_pv = np.zeros(len(starts))
    base_v = np.zeros(len(starts))
    if len(starts) > 1:
        base_pv[1:] = c_pv[starts[1:] - 1]
        base_v[1:] = c_v[starts[1:] - 1]
    gid = np.cumsum(change).astype(int) - 1
    denom = c_v - base_v[gid]
    numer = c_pv - base_pv[gid]
    out = np.full(n, np.nan)
    ok = denom > 0
    out[ok] = numer[ok] / denom[ok]
    return out


def atr14(high, low, close):
    """ATR(14) as an EMA of true range with alpha 1/14, matching edge_hunt."""
    h = np.asarray(high, float)
    l = np.asarray(low, float)
    c = np.asarray(close, float)
    prev = np.r_[np.nan, c[:-1]]
    parts = np.vstack([h - l, np.abs(h - prev), np.abs(l - prev)])
    tr = np.nanmax(parts, axis=0)
    return pd.Series(tr).ewm(alpha=1.0 / 14.0, adjust=False).mean().to_numpy(dtype=float)


def rth_bars(df):
    hm = df.index.hour * 100 + df.index.minute
    return df[(hm >= 930) & (hm < 1600)]


def to_tf(df, minutes):
    """RTH bars of `minutes`. A higher-timeframe bar does not mix two sessions.

    The label is the bar's start. Its close is known `minutes` later, so the
    builder never reads a 1-minute bar past that close.
    """
    rth = rth_bars(df)
    if int(minutes) == 1 or not len(rth):
        return rth
    parts = []
    for _, g in rth.groupby(rth.index.date, sort=True):
        grouped = g.groupby(g.index.floor(f"{int(minutes)}min"), sort=True)
        out = pd.DataFrame({
            "open": grouped["open"].first(),
            "high": grouped["high"].max(),
            "low": grouped["low"].min(),
            "close": grouped["close"].last(),
            "volume": grouped["volume"].sum(),
        }).dropna(subset=["open", "high", "low", "close"])
        parts.append(out)
    if not parts:
        return rth.iloc[0:0]
    return pd.concat(parts)


def build_chart(df, tf, score_index):
    """Indicators on one timeframe. `score_index` maps a session date to its row in the study."""
    bars = to_tf(df, tf)
    n = len(bars)
    empty = {
        "day_ord": np.zeros(0, dtype=np.int32),
        "day_i": np.zeros(0, dtype=np.int32),
        "entry": np.zeros(0, dtype=np.int32),
        "score": np.zeros(0, dtype=bool),
        "fear": np.zeros(0), "greed": np.zeros(0),
        "fear_sig": np.zeros(0), "greed_sig": np.zeros(0),
        "mom": np.zeros(0), "hist": np.zeros(0), "sq_on": np.zeros(0, dtype=bool),
        "close": np.zeros(0), "vwap_up": np.zeros(0), "vwap_dn": np.zeros(0),
        "bb_up": np.zeros(0), "bb_dn": np.zeros(0),
    }
    if n == 0:
        return empty
    fear, greed = fear_greed(bars)
    sq, mom, bb_up, bb_dn = ttm_squeeze(bars["high"], bars["low"], bars["close"])
    hist = eh.macd_histogram(bars["close"].to_numpy(dtype=float))
    minutes = (bars.index.hour * 60 + bars.index.minute - (9 * 60 + 30)).to_numpy(dtype=int)
    entry = np.full(n, -1, dtype=np.int32)
    for i, minute in enumerate(minutes):
        if minute < 0 or minute >= sc.N_MIN:
            continue
        ent = entry_minute_of(int(minute), tf)
        if ent is not None:
            entry[i] = int(ent)
    day_ord = np.array([ts.date().toordinal() for ts in bars.index], dtype=np.int32)
    day_i = np.array([score_index.get(ts.date(), -1) for ts in bars.index], dtype=np.int32)
    vwap = session_vwap(bars["high"], bars["low"], bars["close"], bars["volume"], day_ord)
    atr = atr14(bars["high"], bars["low"], bars["close"])
    return {
        "day_ord": day_ord,
        "day_i": day_i,
        "entry": entry,
        "score": (day_i >= 0) & (entry >= 0),
        "fear": fear,
        "greed": greed,
        "fear_sig": _sma(fear, SIGNAL_LEN),
        "greed_sig": _sma(greed, SIGNAL_LEN),
        "mom": mom,
        "hist": np.asarray(hist, dtype=float),
        "sq_on": np.asarray(sq, dtype=bool),
        "close": bars["close"].to_numpy(dtype=float),
        "vwap_up": vwap + atr,
        "vwap_dn": vwap - atr,
        "bb_up": bb_up,
        "bb_dn": bb_dn,
    }


def build_charts(frames, score_days, tfs):
    score_index = {day: i for i, day in enumerate(score_days)}
    charts = {}
    for tf in tfs:
        charts[tf] = {}
        for sym_i, _sym in enumerate(frames):
            charts[tf][sym_i] = build_chart(frames[_sym], tf, score_index)
    return charts


def prepare_frame(frame):
    """Pieces that do not depend on the greed/fear thresholds."""
    if frame.get("_ready"):
        return frame
    day = frame["day_ord"]
    frame["_mom_dn"] = mom_turn_down(frame["mom"], day)
    frame["_mom_up"] = mom_turn_up(frame["mom"], day)
    frame["_macd_dn"] = mom_turn_down(frame["hist"], day)
    frame["_macd_up"] = mom_turn_up(frame["hist"], day)
    on, released, off = squeeze_states(frame["sq_on"], day, RELEASE_LOOK)
    frame["_sq_on"] = on
    frame["_sq_rel"] = released
    frame["_sq_off"] = off
    frame["_band_put"] = outside_band(frame["close"], frame["vwap_up"], frame["vwap_dn"], frame["bb_up"], frame["bb_dn"], -1)
    frame["_band_call"] = outside_band(frame["close"], frame["vwap_up"], frame["vwap_dn"], frame["bb_up"], frame["bb_dn"], 1)
    frame["_ready"] = True
    return frame


def threshold_shared(frame, g, f):
    day = frame["day_ord"]
    fear, greed = frame["fear"], frame["greed"]
    ext_put = (greed >= float(g)) & (fear <= float(f)) & np.isfinite(greed) & np.isfinite(fear)
    ext_call = (fear >= float(g)) & (greed <= float(f)) & np.isfinite(fear) & np.isfinite(greed)
    return {
        "ext_put": ext_put,
        "ext_call": ext_call,
        "turn_put": side_turn(greed, fear, g, f, frame["greed_sig"], day),
        "turn_call": side_turn(fear, greed, g, f, frame["fear_sig"], day),
        "lift_put": quiet_lift(fear, greed, g, f, frame["fear_sig"], day),
        "lift_call": quiet_lift(greed, fear, g, f, frame["greed_sig"], day),
        "first_put": first_in_run(ext_put, day),
        "first_call": first_in_run(ext_call, day),
        "clusters": {},
    }


def _squeeze_mask(frame, mode):
    if mode is None or mode == "any":
        return np.ones(len(frame["day_ord"]), dtype=bool)
    if mode == "on":
        return frame["_sq_on"]
    if mode == "released5":
        return frame["_sq_rel"]
    if mode == "off":
        return frame["_sq_off"]
    raise ValueError(mode)


def _emit(mask, side, frame, sym):
    sel = np.asarray(mask, dtype=bool) & np.asarray(frame["score"], dtype=bool) & (frame["day_i"] >= 0)
    fear = frame["fear"]
    greed = frame["greed"]
    pin = greed if side == -1 else fear
    out = []
    for i in np.flatnonzero(sel):
        out.append((
            int(frame["day_i"][i]), int(sym), int(frame["entry"][i]), int(side),
            float(pin[i]), float(fear[i]), float(greed[i]),
        ))
    return out


def events_from_shared(frame, cell, sym, shared):
    """Chart events for one cell. Cooldown is applied by the caller across symbols."""
    if cell.variant == "first":
        put, call = shared["first_put"], shared["first_call"]
    elif cell.variant == "turn":
        put, call = shared["turn_put"], shared["turn_call"]
    elif cell.variant == "turn_band":
        put = shared["turn_put"] & frame["_band_put"]
        call = shared["turn_call"] & frame["_band_call"]
    elif cell.variant == "turn_mom":
        put = shared["turn_put"] & (frame["_mom_dn"] | frame["_macd_dn"])
        call = shared["turn_call"] & (frame["_mom_up"] | frame["_macd_up"])
    elif cell.variant == "all3":
        cached = shared["clusters"].get(cell.N)
        if cached is None:
            day = frame["day_ord"]
            cached = (
                cluster_fires(shared["turn_put"], shared["lift_put"], frame["_mom_dn"], shared["ext_put"], cell.N, day),
                cluster_fires(shared["turn_call"], shared["lift_call"], frame["_mom_up"], shared["ext_call"], cell.N, day),
            )
            shared["clusters"][cell.N] = cached
        sq = _squeeze_mask(frame, cell.squeeze)
        put, call = cached[0] & sq, cached[1] & sq
    else:
        raise ValueError(cell.variant)
    return _emit(put, -1, frame, sym) + _emit(call, 1, frame, sym)


def events_for_frame(frame, cell, sym):
    """Events for one chart, with the 20-minute cooldown applied."""
    prep = prepare_frame(frame)
    shared = threshold_shared(prep, cell.G, cell.F)
    return apply_cooldown(events_from_shared(prep, cell, sym, shared), COOLDOWN)


def build_events(charts, cells):
    out = {c.id: [] for c in cells}
    by_tf = {}
    for cell in cells:
        by_tf.setdefault(cell.tf, []).append(cell)
    for tf, group in by_tf.items():
        for sym_i, frame in charts[tf].items():
            prep = prepare_frame(frame)
            buckets = {}
            for cell in group:
                buckets.setdefault((cell.G, cell.F), []).append(cell)
            for (g, f), bucket in buckets.items():
                shared = threshold_shared(prep, g, f)
                for cell in bucket:
                    out[cell.id].extend(events_from_shared(prep, cell, sym_i, shared))
    for cid in out:
        out[cid] = apply_cooldown(out[cid], COOLDOWN)
    return out


def _prices_at(opt, minute, last_real):
    """OHLC of a real print, else a lab carry no older than STALE_AFTER. None ends the path."""
    if 0 <= minute < sc.N_MIN and opt["real"][minute] and np.isfinite(opt["close"][minute]):
        close = float(opt["close"][minute])
        open_ = float(opt["open"][minute]) if np.isfinite(opt["open"][minute]) else close
        high = float(opt["high"][minute]) if np.isfinite(opt["high"][minute]) else close
        low = float(opt["low"][minute]) if np.isfinite(opt["low"][minute]) else close
        return open_, high, low, close, minute
    if last_real is None:
        return None
    age = minute - last_real
    carried = opt["lab"][minute] if 0 <= minute < sc.N_MIN else np.nan
    if age > sc.STALE_AFTER or not np.isfinite(carried):
        return None
    close = float(carried)
    return close, close, close, close, last_real


def _net_pct(bid, debit, commission):
    if debit <= 0 or not math.isfinite(bid):
        return float("nan")
    dollar = (float(bid) - float(debit)) * 100.0 - 2.0 * float(commission)
    return dollar / (float(debit) * 100.0) * 100.0


def measure_path(opt, entry_min, costs=COSTS, horizon=HORIZON):
    """Peak bid over the next `horizon` minutes, and whether each window cleared each target.

    The bid is the print minus the half-spread, floored at zero. The peak is the
    best high-bid. Drawdown is the worst low-bid from the entry through the
    peak bar (that bar's low may print before its high). Bars before the entry
    are not read. A carried print older than five minutes ends the path.
    Net percent matches simulate_trade: both commissions and the entry ask.
    """
    cent, pct, comm = costs
    entry_min = int(entry_min)
    raw = float(opt["open"][entry_min])
    debit = raw + sc.half_spread(raw, cent, pct)
    last_m = min(entry_min + int(horizon), sc.FLAT_MIN)
    peak_by_w = [-1.0] * len(WINDOWS)
    peak_bid = -1.0
    peak_at = entry_min
    running_worst = float("inf")
    worst_at_peak = float("nan")
    last_real = None
    saw = False
    for minute in range(entry_min, last_m + 1):
        px = _prices_at(opt, minute, last_real)
        if px is None:
            break
        _o, high, low, _c, last_real = px
        saw = True
        high_bid = max(0.0, high - sc.half_spread(high, cent, pct))
        low_bid = max(0.0, low - sc.half_spread(low, cent, pct))
        if low_bid < running_worst:
            running_worst = low_bid
        if high_bid > peak_bid:
            peak_bid = high_bid
            peak_at = minute
            worst_at_peak = running_worst
        age = minute - entry_min
        for i, window in enumerate(WINDOWS):
            if age <= window and high_bid > peak_by_w[i]:
                peak_by_w[i] = high_bid
    if not saw or peak_bid < 0:
        return None
    hits = []
    for high_bid in peak_by_w:
        net = _net_pct(high_bid, debit, comm) if high_bid >= 0 else float("nan")
        for level in HIT_LEVELS:
            hits.append(bool(math.isfinite(net) and net >= level * 100.0))
    return {
        "ok": True,
        "raw": raw,
        "debit": debit,
        "peak_bid": float(peak_bid),
        "peak_by_window": {w: (float(p) if p >= 0 else float("nan")) for w, p in zip(WINDOWS, peak_by_w)},
        "t_peak": int(peak_at - entry_min),
        "worst_bid": float(worst_at_peak) if math.isfinite(worst_at_peak) else float("nan"),
        "mfe": _net_pct(peak_bid, debit, comm),
        "drawdown": _net_pct(worst_at_peak, debit, comm),
        "hits": tuple(hits),
        "entry_min": entry_min,
        "path_minutes": int(last_m - entry_min),
    }


def fixed_exits(opt, entry_min, costs=COSTS):
    """Three fixed rules. simulate_trade checks the stop before the target on the same bar."""
    out = {}
    for name, cfg in EXITS:
        res = sc.simulate_trade(opt, int(entry_min), cfg, costs, allow_slip=False, premium=None)
        if res.get("status") != "fill":
            out[name] = {"reason": res.get("status", "skip"), "net": float("nan")}
        else:
            out[name] = {"reason": res["reason"], "net": float(res["net_pct"])}
    return out


def resolve_fill(und_sess, opt, day, sym, minute, side, strike, costs=COSTS):
    """Fill the intended minute, or the next one if it has no usable print.

    A real open at or above the minimum premium locks the minute. Missing the
    0.30–1.00 band does not slide the clock. The slip minute, when there is
    no print, recomputes the strike from that minute's spot. The slip stays
    inside 9:35–15:45.
    """
    bt = sc._bt()
    minute = int(minute)
    for step, m in enumerate((minute, minute + 1)):
        if m < ENTRY_LO or m > ENTRY_HI or m >= sc.FLAT_MIN:
            continue
        spot = sc.spot_at(und_sess, m)
        k = sc.strike_price(spot, side, strike)
        if k is None:
            continue
        contract = bt.lab_occ(sym, day, "C" if int(side) == 1 else "P", k)
        rec = opt.get((day, contract))
        if rec is None:
            continue
        if not (rec["real"][m] and np.isfinite(rec["open"][m]) and float(rec["open"][m]) >= sc.MIN_PREMIUM):
            continue
        measured = measure_path(rec, m, costs)
        if measured is None:
            continue
        measured["in_band"] = bool(sc.premium_in_band(measured["raw"], PREMIUM_BAND))
        measured["slipped"] = step == 1
        measured["contract"] = contract
        measured["exits"] = fixed_exits(rec, m, costs)
        return measured
    return None


def draw_randoms(events_by_cell, score_days, symbols):
    """One random minute per (day, symbol, minute, side), shared by every cell."""
    keys = set()
    for events in events_by_cell.values():
        for ev in events:
            keys.add((ev[DI], ev[SYM], ev[MIN], ev[SIDE]))
    out = {}
    for day_i, sym_i, minute, side in keys:
        day = score_days[day_i]
        rng = np.random.default_rng(sc.stream_seed(
            "fgfade", day.isoformat(), symbols[sym_i], int(minute), int(side),
        ))
        out[(day_i, sym_i, minute, side)] = random_minute(minute, rng)
    return out


def contract_keys(events_by_cell, random_of):
    keys = set()
    for events in events_by_cell.values():
        for ev in events:
            keys.add((ev[DI], ev[SYM], ev[MIN], ev[SIDE]))
    for key, minute in random_of.items():
        if minute is not None:
            keys.add((key[0], key[1], int(minute), key[3]))
    return keys


def needed_contracts(keys, und, symbols, score_days):
    bt = sc._bt()
    needed = {}
    for day_i, sym_i, minute, side in keys:
        day = score_days[day_i]
        sess = und[symbols[sym_i]].get(day)
        if sess is None:
            continue
        for m in (int(minute), int(minute) + 1):
            if m < ENTRY_LO or m > ENTRY_HI or m >= sc.FLAT_MIN:
                continue
            spot = sc.spot_at(sess, m)
            for mode in STRIKES:
                k = sc.strike_price(spot, side, mode)
                if k is None:
                    continue
                cp = "C" if int(side) == 1 else "P"
                needed.setdefault(day, set()).add(bt.lab_occ(symbols[sym_i], day, cp, k))
    return needed


def build_fills(keys, und, opt, symbols, score_days, costs=COSTS):
    fills = {}
    for day_i, sym_i, minute, side in keys:
        day = score_days[day_i]
        sess = und[symbols[sym_i]].get(day)
        if sess is None:
            continue
        for strike in STRIKES:
            fills[(day_i, sym_i, int(minute), int(side), strike)] = resolve_fill(
                sess, opt, day, symbols[sym_i], int(minute), int(side), strike, costs,
            )
    return fills


def _day_ok_array(n_days, mask):
    if mask is None:
        return np.ones(n_days, dtype=bool)
    out = np.zeros(n_days, dtype=bool)
    out[np.asarray(mask, dtype=int)] = True
    return out


def _mean(values):
    arr = np.asarray(list(values), dtype=float)
    arr = arr[np.isfinite(arr)]
    if len(arr) == 0:
        return float("nan")
    return float(arr.mean())


def _median(values):
    arr = np.asarray(list(values), dtype=float)
    arr = arr[np.isfinite(arr)]
    if len(arr) == 0:
        return float("nan")
    return float(np.median(arr))


def summarize_cell(cell, events, fills, random_of, n_days, day_mask, strike, band, n_boot, seed):
    """One grid row. Signal days count chart events. Hit rates count filled trades in this book."""
    day_ok = _day_ok_array(n_days, day_mask)
    kept = [ev for ev in events if 0 <= ev[DI] < n_days and day_ok[ev[DI]]]
    signal_days = {ev[DI] for ev in kept}
    filled = []
    for ev in kept:
        got = fills.get((ev[DI], ev[SYM], ev[MIN], ev[SIDE], strike))
        if not got:
            continue
        if band == "band" and not got["in_band"]:
            continue
        rnd = None
        alt = random_of.get((ev[DI], ev[SYM], ev[MIN], ev[SIDE]))
        if alt is not None:
            rnd = fills.get((ev[DI], ev[SYM], int(alt), ev[SIDE], strike))
            if rnd is not None and band == "band" and not rnd["in_band"]:
                rnd = None
        filled.append((ev, got, rnd))
    n_sess = int(day_ok.sum())
    hit_sums = np.zeros(len(WINDOWS) * len(HIT_LEVELS), dtype=float)
    for _ev, got, _rnd in filled:
        hit_sums += np.asarray(got["hits"], dtype=float)
    n = len(filled)
    hits = {f"hit_{int(level * 100)}_{window}": (float(hit_sums[i] / n * 100.0) if n else float("nan"))
            for i, (window, level) in enumerate((w, lv) for w in WINDOWS for lv in HIT_LEVELS)}
    paired = [(ev, got, rnd) for ev, got, rnd in filled if rnd]
    diffs = [float(got["hits"][HIT_15_30]) - float(rnd["hits"][HIT_15_30]) for _ev, got, rnd in paired]
    day_ids = [ev[DI] for ev, _got, _rnd in paired]
    paired_hit = (
        float(np.mean([got["hits"][HIT_15_30] for _ev, got, _rnd in paired]) * 100.0) if paired else float("nan")
    )
    if diffs:
        sums = np.bincount(day_ids, weights=np.asarray(diffs, float), minlength=n_days).astype(float)
        cnts = np.bincount(day_ids, minlength=n_days).astype(float)
        _t, p = eh.clustered_t_from_days(sums, cnts)
        if not math.isfinite(p):
            p = 1.0
    else:
        p = 1.0
    rnd_hits = [float(rnd["hits"][HIT_15_30]) for _ev, _got, rnd in paired]
    exit_stats = {}
    for name, _cfg in EXITS:
        nets = [got["exits"][name]["net"] for _ev, got, _rnd in filled]
        wins = [1.0 if got["exits"][name]["reason"] == "tp" else 0.0 for _ev, got, _rnd in filled]
        exit_stats[f"mean_{name}"] = _mean(nets)
        exit_stats[f"median_{name}"] = _median(nets)
        exit_stats[f"win_{name}"] = (float(np.mean(wins) * 100.0) if wins else float("nan"))
    hit_day = np.zeros(n_days)
    cnt_day = np.zeros(n_days)
    net_day = np.zeros(n_days)
    net_cnt = np.zeros(n_days)
    if n:
        ids = [ev[DI] for ev, _got, _rnd in filled]
        hit_day = np.bincount(
            ids,
            weights=np.array([float(got["hits"][HIT_15_30]) for _ev, got, _rnd in filled], dtype=float),
            minlength=n_days,
        ).astype(float)
        cnt_day = np.bincount(ids, minlength=n_days).astype(float)
        finite_net = []
        finite_id = []
        for ev, got, _rnd in filled:
            net = got["exits"]["tp15_sl15"]["net"]
            if isinstance(net, (int, float)) and math.isfinite(net):
                finite_net.append(float(net))
                finite_id.append(ev[DI])
        if finite_id:
            net_day = np.bincount(finite_id, weights=np.asarray(finite_net, float), minlength=n_days).astype(float)
            net_cnt = np.bincount(finite_id, minlength=n_days).astype(float)
    boot_seed = int(seed) if seed is not None else 0
    if n_boot and n:
        hit_lo, hit_hi = sc.bootstrap_mean(hit_day, cnt_day, int(n_boot), boot_seed)
        net_lo, net_hi = sc.bootstrap_mean(net_day, net_cnt, int(n_boot), boot_seed + 1)
        if math.isfinite(hit_lo):
            hit_lo, hit_hi = hit_lo * 100.0, hit_hi * 100.0
    else:
        hit_lo = hit_hi = net_lo = net_hi = float("nan")
    row = {
        "cell": cell.id,
        "variant": cell.variant,
        "tf": cell.tf,
        "G": cell.G,
        "F": cell.F,
        "N": "" if cell.N is None else int(cell.N),
        "squeeze": cell.squeeze or "",
        "strike": strike,
        "band": band,
        "signals": len(kept),
        "signal_days": len(signal_days),
        "pct_sessions": (100.0 * len(signal_days) / n_sess) if n_sess else float("nan"),
        "signals_per_session": (len(kept) / n_sess) if n_sess else float("nan"),
        "fills": n,
        "fill_days": len({ev[DI] for ev, _g, _r in filled}),
        "random_n": len(paired),
        "paired_hit_15_30": paired_hit,
        "random_hit_15_30": (float(np.mean(rnd_hits) * 100.0) if rnd_hits else float("nan")),
        "hit_diff": (float(np.mean(diffs) * 100.0) if diffs else float("nan")),
        "p": float(p),
        "q": float("nan"),
        "mean_mfe": _mean(got["mfe"] for _ev, got, _rnd in filled),
        "median_mfe": _median(got["mfe"] for _ev, got, _rnd in filled),
        "median_t_peak": _median(got["t_peak"] for _ev, got, _rnd in filled),
        "mean_dd": _mean(got["drawdown"] for _ev, got, _rnd in filled),
        "median_dd": _median(got["drawdown"] for _ev, got, _rnd in filled),
        "median_raw": _median(got["raw"] for _ev, got, _rnd in filled),
        "boot_hit_lo": hit_lo,
        "boot_hit_hi": hit_hi,
        "boot_net_lo": net_lo,
        "boot_net_hi": net_hi,
    }
    row.update(hits)
    row.update(exit_stats)
    return row


def choose_cell(rows, min_select=MIN_SELECT):
    """Most sessions, then the higher +15% peak within 30 minutes, then more fills.

    Rows with fewer than `min_select` fills are skipped when any row meets it.
    Otherwise the same ranking is used and the note says the minimum was not met.
    The caller passes train rows only.
    """
    usable = [r for r in rows if r.get("signals", r.get("signal_days", 0)) >= 0]
    if not usable:
        return None
    pool = [r for r in usable if int(r["fills"]) >= int(min_select)]
    note = "minimum met"
    if not pool:
        pool = list(usable)
        note = "minimum was not met"

    def key(row):
        hit = row.get("hit_15_30", float("nan"))
        hit = float(hit) if hit is not None and math.isfinite(hit) else -1.0
        return (int(row["signal_days"]), hit, int(row["fills"]))

    best = dict(max(pool, key=key))
    best["select_note"] = note
    return best


def coverage_change(alone_days, conf_days):
    alone = int(alone_days)
    conf = int(conf_days)
    frac = float(conf / alone) if alone else float("nan")
    return {"alone": alone, "confluence": conf, "fraction": frac, "dropped": alone - conf}


def coverage_sentence(alone_days, conf_days, n_sessions):
    change = coverage_change(alone_days, conf_days)
    if not change["alone"]:
        return (
            "Greed/fear alone (`first`) did not fire on a session in this run, "
            "so there is no base to compare with the squeeze cluster."
        )
    pct = change["fraction"] * 100.0
    return (
        f"Greed/fear alone (`first`, the threshold that fires on the most days) "
        f"is on {change['alone']} of {int(n_sessions)} sessions. "
        f"The all-three cluster (squeeze filter off, the window that fires on the most days) "
        f"is on {change['confluence']} sessions, which is {pct:.0f}% as many."
    )


def verdict_sentence(signal_hit, random_hit, q=None):
    """`signal_hit` and `random_hit` are percents. Equal counts as no better."""
    if not (isinstance(signal_hit, (int, float)) and isinstance(random_hit, (int, float))):
        return "The +15% peak hit-rate within 30 minutes could not be compared with the matched random entry."
    if not (math.isfinite(signal_hit) and math.isfinite(random_hit)):
        return "The +15% peak hit-rate within 30 minutes could not be compared with the matched random entry."
    if float(signal_hit) <= float(random_hit):
        return "The +15% peak hit-rate within 30 minutes is no better than the matched random entry."
    qbit = ""
    if q is not None and isinstance(q, (int, float)) and math.isfinite(q):
        qbit = f" Full-sample q is {float(q):.3f}."
    return (
        "The +15% peak hit-rate within 30 minutes is higher than the matched random entry "
        f"on this sample ({float(signal_hit):.1f}% signal, {float(random_hit):.1f}% random).{qbit}"
    )


def breakeven_sentence(rate, premium, win_rate):
    """`rate` is the fraction from scalp_real.breakeven_hit_rate. `win_rate` is a percent."""
    if not (isinstance(rate, (int, float)) and math.isfinite(rate) and isinstance(premium, (int, float)) and math.isfinite(premium)):
        return "The break-even win rate for TP +15% / stop −15% could not be computed (no filled premium)."
    text = (
        f"At a ${float(premium):.2f} premium, the fixed exit TP +15% / stop −15% needs a "
        f"{float(rate) * 100.0:.1f}% win rate to break even after the half-spread and both commissions. "
        "That win rate is the share of trades that exit at the target, not the share whose peak bid tags +15%."
    )
    if isinstance(win_rate, (int, float)) and math.isfinite(win_rate):
        text += f" This book's target-exit rate is {float(win_rate):.1f}%."
    return text


def holdout_split(n_days):
    """Train is the first 75% of sessions. The last 25% is held out, at least one day."""
    hold = max(1, int(round(int(n_days) * 0.25)))
    if hold >= int(n_days):
        hold = int(n_days) - 1
    train = np.arange(0, int(n_days) - hold)
    test = np.arange(int(n_days) - hold, int(n_days))
    return train, test


def _rank_key(row):
    hit = row.get("hit_15_30", float("nan"))
    hit = float(hit) if isinstance(hit, (int, float)) and math.isfinite(hit) else -1.0
    return (int(row["signal_days"]), hit, int(row["fills"]))


def _blank_eval(fold_id, train_idx, test_idx, score_days):
    return {
        "fold": fold_id,
        "cell": "",
        "select_note": "no cell",
        "train_start": score_days[int(train_idx[0])].isoformat() if len(train_idx) else "",
        "train_end": score_days[int(train_idx[-1])].isoformat() if len(train_idx) else "",
        "test_start": score_days[int(test_idx[0])].isoformat() if len(test_idx) else "",
        "test_end": score_days[int(test_idx[-1])].isoformat() if len(test_idx) else "",
        "train_signal_days": 0,
        "train_fills": 0,
        "train_hit": float("nan"),
        "test_signal_days": 0,
        "test_fills": 0,
        "test_hit": float("nan"),
        "test_paired_hit": float("nan"),
        "test_random_hit": float("nan"),
        "test_mean_net": float("nan"),
        "test_win": float("nan"),
        "boot_hit_lo": float("nan"),
        "boot_hit_hi": float("nan"),
    }


def _select_and_score(cells, events_by_cell, fills, random_of, n_days, train_idx, test_idx, score_days, fold_id, n_boot, min_select, seed):
    train_rows = []
    by_id = {}
    for cell in cells:
        row = summarize_cell(
            cell, events_by_cell[cell.id], fills, random_of, n_days, train_idx,
            "1otm", "band", 0, seed,
        )
        train_rows.append(row)
        by_id[cell.id] = cell
    chosen = choose_cell(train_rows, min_select)
    if chosen is None:
        return _blank_eval(fold_id, train_idx, test_idx, score_days)
    cell = by_id[chosen["cell"]]
    tested = summarize_cell(
        cell, events_by_cell[cell.id], fills, random_of, n_days, test_idx,
        "1otm", "band", n_boot, seed + 17,
    )
    return {
        "fold": fold_id,
        "cell": chosen["cell"],
        "select_note": chosen["select_note"],
        "train_start": score_days[int(train_idx[0])].isoformat(),
        "train_end": score_days[int(train_idx[-1])].isoformat(),
        "test_start": score_days[int(test_idx[0])].isoformat(),
        "test_end": score_days[int(test_idx[-1])].isoformat(),
        "train_signal_days": int(chosen["signal_days"]),
        "train_fills": int(chosen["fills"]),
        "train_hit": chosen["hit_15_30"],
        "test_signal_days": int(tested["signal_days"]),
        "test_fills": int(tested["fills"]),
        "test_hit": tested["hit_15_30"],
        "test_paired_hit": tested["paired_hit_15_30"],
        "test_random_hit": tested["random_hit_15_30"],
        "test_mean_net": tested["mean_tp15_sl15"],
        "test_win": tested["win_tp15_sl15"],
        "boot_hit_lo": tested["boot_hit_lo"],
        "boot_hit_hi": tested["boot_hit_hi"],
    }


def walk_forward(cells, events_by_cell, fills, random_of, score_days, n_boot, min_select):
    n_days = len(score_days)
    folds = eh.walk_forward_folds(n_days, K_FOLDS)
    out = []
    for i, (train, test) in enumerate(folds, start=1):
        out.append(_select_and_score(
            cells, events_by_cell, fills, random_of, n_days, train, test, score_days,
            i, n_boot, min_select, sc.stream_seed("fgfade-fold", i),
        ))
    return out


def held_out(cells, events_by_cell, fills, random_of, score_days, n_boot, min_select):
    train, test = holdout_split(len(score_days))
    return _select_and_score(
        cells, events_by_cell, fills, random_of, len(score_days), train, test, score_days,
        "heldout", n_boot, min_select, sc.stream_seed("fgfade-heldout"),
    )


def _fmt_pct(value):
    if not isinstance(value, (int, float)) or not math.isfinite(value):
        return "n/a"
    return f"{float(value):.1f}%"


def _fmt_num(value, digits=1):
    if not isinstance(value, (int, float)) or not math.isfinite(value):
        return "n/a"
    return f"{float(value):.{digits}f}"


def _fmt_points(value):
    """A net that is already in percent. Missing stays n/a, without a stray percent sign."""
    if not isinstance(value, (int, float)) or not math.isfinite(value):
        return "n/a"
    return f"{float(value):.1f}%"


def _n_sessions(n):
    n = int(n)
    return f"{n} session" if n == 1 else f"{n} sessions"


def _fmt_ci(lo, hi):
    if not (isinstance(lo, (int, float)) and isinstance(hi, (int, float)) and math.isfinite(lo) and math.isfinite(hi)):
        return "n/a"
    return f"{lo:.1f}% to {hi:.1f}%"


def _cell_label(row):
    n = row.get("N", "")
    sq = row.get("squeeze", "")
    extra = ""
    if row["variant"] == "all3":
        extra = f" N={n} {sq}"
    return f"{row['variant']} {row['tf']}m G{row['G']} F{row['F']}{extra}"


def _phone_table(rows, limit):
    headers = ["setup", "days", "% sess", "fills", "+15% 30m", "random", "mean MFE", "mean 15/15", "q"]
    body = []
    for row in rows[:limit]:
        body.append([
            _cell_label(row),
            int(row["signal_days"]),
            _fmt_pct(row["pct_sessions"]),
            int(row["fills"]),
            _fmt_pct(row["hit_15_30"]),
            _fmt_pct(row["random_hit_15_30"]),
            _fmt_num(row["mean_mfe"]),
            _fmt_num(row["mean_tp15_sl15"]),
            _fmt_num(row["q"], 3),
        ])
    return _md_table(headers, body)


def _md_table(headers, body):
    if not body:
        return "_none_"
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for row in body:
        lines.append("| " + " | ".join(str(c) for c in row) + " |")
    return "\n".join(lines)


def _hit_grid(row):
    headers = ["window"] + [f"+{int(level * 100)}%" for level in HIT_LEVELS]
    body = []
    for window in WINDOWS:
        body.append([f"{window} min"] + [_fmt_pct(row.get(f"hit_{int(level * 100)}_{window}")) for level in HIT_LEVELS])
    return _md_table(headers, body)


def _find_row(rows, **want):
    for row in rows:
        if all(row.get(k) == v for k, v in want.items()):
            return row
    return None


def render_report(rows, folds, held, meta, focus_trades):
    """Phone report. The full grid is the summary CSV. Days covered sort first."""
    n_sess = int(meta["n_sessions"])
    band = [r for r in rows if r["strike"] == "1otm" and r["band"] == "band"]
    ordered = sorted(band, key=_rank_key, reverse=True)
    top = ordered[0] if ordered else None
    headline_pool = [r for r in band if r["variant"] == "all3" and r["squeeze"] == "any"]
    headline = max(headline_pool, key=_rank_key) if headline_pool else None
    first_pool = [r for r in band if r["variant"] == "first"]
    best_first = max(first_pool, key=_rank_key) if first_pool else None
    lines = ["# Fear-greed fade", ""]
    lines.append(
        "Data only. Research tool, not trading advice. No orders. "
        f"Symbols {', '.join(meta['symbols'])}. "
        f"Sessions {meta['first_day']} through {meta['last_day']} ({n_sess}). "
        f"Timeframes {', '.join(str(t) + 'm' for t in meta['tfs'])}. "
        "Regular hours, entry from 9:35 through 15:45 ET. "
        "Costs match the edge hunt: buy the ask (option open plus the half-spread), "
        "sell the bid (fill minus the half-spread), half-spread the larger of 1 cent and 0.5% of premium, "
        "$0.65 a side."
    )
    lines.append("")
    lines.append("## Verdict")
    lines.append("")
    if top is None:
        lines.append("No setups were scored.")
    else:
        lines.append(
            f"The setup on the most sessions is `{top['cell']}` "
            f"({int(top['signal_days'])} of {n_sess} sessions, {int(top['fills'])} filled trades)."
        )
        lines.append("")
        if int(top["fills"]) and not int(top["random_n"]):
            lines.append("This book has fills, and none of the matched random entries landed in the same premium band.")
            lines.append("")
        lines.append(
            f"Matched pairs {int(top['random_n'])}. "
            f"On those pairs the signal +15% within 30 min is {_fmt_pct(top['paired_hit_15_30'])} "
            f"and the random entry is {_fmt_pct(top['random_hit_15_30'])}."
        )
        lines.append("")
        lines.append(verdict_sentence(top["paired_hit_15_30"], top["random_hit_15_30"], top.get("q")))
        lines.append("")
        rate = sc.breakeven_hit_rate(0.15, 0.15, top["median_raw"], COSTS[0], COSTS[1], COSTS[2])
        lines.append(breakeven_sentence(rate, top["median_raw"], top["win_tp15_sl15"]))
        lines.append("")
        lines.append(
            f"Mean peak net {_fmt_points(top['mean_mfe'])}, median peak net {_fmt_points(top['median_mfe'])}, "
            f"median minutes to the peak {_fmt_num(top['median_t_peak'])}, "
            f"median drawdown to that peak {_fmt_points(top['median_dd'])}. "
            f"95% bootstrap for the +15% within 30 min hit rate: {_fmt_ci(top['boot_hit_lo'], top['boot_hit_hi'])}. "
            f"95% bootstrap for the mean TP +15% / stop −15% net: "
            f"{_fmt_points(top['boot_net_lo'])} to {_fmt_points(top['boot_net_hi'])}."
        )
    if headline is not None and (top is None or headline["cell"] != top["cell"]):
        lines.append("")
        lines.append(
            f"The all-three cluster on the most sessions is `{headline['cell']}` "
            f"({int(headline['signal_days'])} of {n_sess} sessions, {int(headline['fills'])} fills)."
        )
        lines.append("")
        lines.append(
            f"Matched pairs {int(headline['random_n'])}. "
            f"On those pairs the signal +15% within 30 min is {_fmt_pct(headline['paired_hit_15_30'])} "
            f"and the random entry is {_fmt_pct(headline['random_hit_15_30'])}."
        )
        lines.append("")
        lines.append(verdict_sentence(headline["paired_hit_15_30"], headline["random_hit_15_30"], headline.get("q")))
        rate_h = sc.breakeven_hit_rate(0.15, 0.15, headline["median_raw"], COSTS[0], COSTS[1], COSTS[2])
        lines.append("")
        lines.append(breakeven_sentence(rate_h, headline["median_raw"], headline["win_tp15_sl15"]))
    lines.append("")
    lines.append("## Coverage")
    lines.append("")
    alone = int(best_first["signal_days"]) if best_first else 0
    conf = int(headline["signal_days"]) if headline else 0
    lines.append(coverage_sentence(alone, conf, n_sess))
    lines.append("")
    if best_first is not None:
        lines.append(
            f"Same threshold as that `first` cell (tf {best_first['tf']}m, G{best_first['G']}, F{best_first['F']}), "
            "all three with the squeeze filter off:"
        )
        lines.append("")
        body = [[f"first", int(best_first["signal_days"]), _fmt_pct(best_first["pct_sessions"]), int(best_first["fills"])]]
        for n in CLUSTER_NS:
            row = _find_row(
                band, variant="all3", squeeze="any", tf=best_first["tf"],
                G=best_first["G"], F=best_first["F"], N=n,
            )
            if row is not None:
                body.append([f"all3 N={n}", int(row["signal_days"]), _fmt_pct(row["pct_sessions"]), int(row["fills"])])
        lines.append(_md_table(["setup", "days", "% sess", "fills"], body))
        lines.append("")
    if headline is not None:
        lines.append(
            f"Squeeze state at `{headline['cell']}` (same timeframe, thresholds, and N). "
            "`any` is the cluster with no squeeze-state filter."
        )
        lines.append("")
        body = []
        for sq in SQUEEZE_FILTERS:
            row = _find_row(
                band, variant="all3", squeeze=sq, tf=headline["tf"],
                G=headline["G"], F=headline["F"], N=headline["N"],
            )
            if row is not None:
                change = coverage_change(int(headline["signal_days"]), int(row["signal_days"]))
                if change["alone"]:
                    share = _fmt_pct(change["fraction"] * 100.0)
                elif change["confluence"]:
                    share = "n/a"
                else:
                    share = "0%"
                body.append([sq, int(row["signal_days"]), share, int(row["fills"]), _fmt_pct(row["hit_15_30"])])
        lines.append(_md_table(["squeeze", "days", "vs filter off", "fills", "+15% 30m"], body))
    lines.append("")
    lines.append("## Headline: all three turn")
    lines.append("")
    lines.append(
        "A put fires when greed is the pinned side and fear is the quiet side. A call is the mirror. "
        f"The signal line is a {SIGNAL_LEN}-bar average of that pane. The pane does not publish its own signal line. "
        f"Squeeze is Bollinger {SQUEEZE_LEN} / {BB_MULT:.1f} inside Keltner {SQUEEZE_LEN} / {KC_MULT:.1f}, "
        "momentum a 20-bar linear regression of close minus the mid. That is the definition in backtest.py. "
        "All three means, within N bars on that timeframe: the pinned side turns down off its peak or under its signal line, "
        "the quiet side lifts off its low or through its signal line, and the squeeze momentum ticks against the move. "
        "The extreme (pinned at or above G, quiet at or below F) has to sit in that same window. "
        "The row fires once, on the first bar the set is complete. "
        "Squeeze `released5` means the squeeze fired within the last 5 bars. `on` means it is on now. "
        "`off` means it is not on and it did not fire in those 5 bars. `any` leaves that filter off."
    )
    lines.append("")
    if headline is not None:
        lines.append(f"Peak-bid hit rates for `{headline['cell']}` (first OTM, premium 0.30–1.00):")
        lines.append("")
        lines.append(_hit_grid(headline))
        lines.append("")
        lines.append(
            f"Fixed exits on that book: TP +15% / stop −15% mean {_fmt_points(headline['mean_tp15_sl15'])} "
            f"(target exits {_fmt_pct(headline['win_tp15_sl15'])}), "
            f"TP +15% / stop −25% mean {_fmt_points(headline['mean_tp15_sl25'])}, "
            f"TP +15% / no stop / 30 min mean {_fmt_points(headline['mean_tp15_nostop_30'])}."
        )
        lines.append("")
    head_rows = [r for r in ordered if r["variant"] == "all3"]
    lines.append("All-three rows with the most sessions (first OTM, premium 0.30–1.00):")
    lines.append("")
    lines.append(_phone_table(head_rows, 12))
    lines.append("")
    lines.append("## Walk-forward")
    lines.append("")
    lines.append(
        "Five expanding folds. Block 0 is train only. Each fold picks one cell on its train days "
        "(first OTM, premium 0.30–1.00, most sessions, then the higher +15% peak within 30 minutes) "
        f"and scores that cell only on the later test days. A cell needs {MIN_SELECT} train fills to be eligible "
        "when any cell has that many."
    )
    lines.append("")
    for fold in folds:
        lines.append(_fold_sentence(fold))
        lines.append("")
    lines.append("## Held-out last 25%")
    lines.append("")
    lines.append(
        "The last 25% of sessions were not used to pick the cell. "
        "The pick uses the first 75% and the same rule as the folds."
    )
    lines.append("")
    lines.append(_fold_sentence(held))
    lines.append("")
    lines.append("## Other variants")
    lines.append("")
    lines.append(
        "Sorted by sessions covered, then the +15% peak within 30 minutes, then fills. "
        "`first` is the first bar of the extreme. `turn` is the pinned side leaving that extreme. "
        "`turn_band` also wants price outside the fade-side VWAP band (VWAP plus or minus ATR 14) or the Bollinger band. "
        "`turn_mom` also wants squeeze momentum or the MACD histogram ticking against the move. "
        "The cooldown is one event per ticker per 20 minutes inside each cell, so the variants can be compared. "
        "The full grid, both strikes, and both premium books are in `fgfade_summary.csv`. "
        "Hit columns there are percents. q is Benjamini-Hochberg over every row in that file. It is a screen. "
        "The fold section is the out-of-sample result."
    )
    lines.append("")
    lines.append(_phone_table(ordered, 15))
    lines.append("")
    lines.append("## 2026-10-19 through 2026-10-23")
    lines.append("")
    have = [d for d in FOCUS_DATES if d in set(meta["score_days"])]
    if not have:
        lines.append("2026-10-19 through 2026-10-23 are not in this run.")
    elif not focus_trades:
        lines.append("Those days are in this run. The reported variants have no filled trade on them.")
    else:
        lines.append(_md_table(
            ["date", "time", "ticker", "side", "variant", "entry ask", "peak bid", "min to peak", "15/15 net"],
            [[
                t["date"], t["time"], t["ticker"], t["side"], t["variant"],
                _fmt_num(t["entry_ask"], 2), _fmt_num(t["peak_bid"], 2),
                t["time_to_peak"], _fmt_num(t["tp15_sl15_net"]),
            ] for t in focus_trades],
        ))
    lines.append("")
    lines.append("## Notes")
    lines.append("")
    lines.append(
        "The +15% peak test uses the best bid in the window. Net is that bid against the entry ask, minus both commissions. "
        "The fixed +15% target is different: the option high has to touch the raw premium times 1.15, and the sale is on the bid. "
        "On a bar that touches both the stop and the target, the stop is taken first."
    )
    lines.append("")
    lines.append(
        "The book flats at 15:55. An entry at 15:45 has ten minutes of path, so the 30-minute and 60-minute windows are that shorter path. "
        "A chart event whose entry would fall before 9:35 is not taken, and a run that started then is not re-armed at 9:35."
    )
    lines.append("")
    lines.append(
        f"This file scores {meta['n_cells']} setups and {meta['n_rows']} rows after strike and premium band. "
        f"Bootstrap draws: {meta['n_boot']}. Runtime {meta['runtime_min']:.1f} minutes. "
        + ("Prices in this run are synthetic. They are not a market. " if meta.get("synthetic") else "")
        + "A short sample is not a reason to change the live bot."
    )
    lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def _fold_sentence(fold):
    if not fold.get("cell"):
        return f"Fold {fold['fold']}: no cell to test ({fold.get('train_start', '')} to {fold.get('test_end', '')})."
    boot = ""
    if math.isfinite(fold.get("boot_hit_lo", float("nan"))):
        boot = f" Bootstrap for the test hit rate: {_fmt_ci(fold['boot_hit_lo'], fold['boot_hit_hi'])}."
    return (
        f"Fold {fold['fold']}: train {fold['train_start']} to {fold['train_end']} "
        f"({_n_sessions(fold['train_signal_days'])}, {fold['train_fills']} fills, {fold['select_note']}), "
        f"chose `{fold['cell']}`. "
        f"Test {fold['test_start']} to {fold['test_end']}: "
        f"{_n_sessions(fold['test_signal_days'])}, {fold['test_fills']} fills, "
        f"+15% within 30 min {_fmt_pct(fold['test_hit'])} "
        f"(matched {_fmt_pct(fold.get('test_paired_hit'))} versus random {_fmt_pct(fold['test_random_hit'])}), "
        f"mean net at TP +15% / stop −15% {_fmt_points(fold['test_mean_net'])}, "
        f"target exits {_fmt_pct(fold['test_win'])}.{boot}"
    )


def assign_q(rows):
    qs = eh.fdr_qvalues([r["p"] for r in rows], family_n=len(rows))
    for row, q in zip(rows, qs):
        row["q"] = float(q)
    return rows


def reported_cells(rows):
    """Top 3 by sessions on the first-OTM premium book, plus the busiest all-three cell if it is not already there."""
    band = [r for r in rows if r["strike"] == "1otm" and r["band"] == "band"]
    ordered = sorted(band, key=_rank_key, reverse=True)
    chosen = [(row, f"top{i}") for i, row in enumerate(ordered[:3], start=1)]
    have = {row["cell"] for row, _role in chosen}
    pool = [r for r in band if r["variant"] == "all3" and r["squeeze"] == "any"]
    if pool:
        headline = max(pool, key=_rank_key)
        if headline["cell"] not in have:
            chosen.append((headline, "headline"))
    return chosen


def trade_records(chosen, cells_by_id, events_by_cell, fills, score_days, symbols):
    """Filled first-OTM premium-band trades for the reported cells."""
    records = []
    for row, role in chosen:
        cell = cells_by_id[row["cell"]]
        for ev in events_by_cell[cell.id]:
            got = fills.get((ev[DI], ev[SYM], ev[MIN], ev[SIDE], "1otm"))
            if not got or not got["in_band"]:
                continue
            exits = got["exits"]
            records.append({
                "date": score_days[ev[DI]].isoformat(),
                "time": clock_hhmm(got["entry_min"]),
                "ticker": symbols[ev[SYM]],
                "side": "put" if ev[SIDE] == -1 else "call",
                "contract": got["contract"],
                "entry_ask": got["debit"],
                "raw_entry": got["raw"],
                "peak_bid": got["peak_bid"],
                "peak_net": got["mfe"],
                "time_to_peak": got["t_peak"],
                "drawdown_net": got["drawdown"],
                "tp15_sl15_reason": exits["tp15_sl15"]["reason"],
                "tp15_sl15_net": exits["tp15_sl15"]["net"],
                "tp15_sl25_reason": exits["tp15_sl25"]["reason"],
                "tp15_sl25_net": exits["tp15_sl25"]["net"],
                "tp15_nostop_30_reason": exits["tp15_nostop_30"]["reason"],
                "tp15_nostop_30_net": exits["tp15_nostop_30"]["net"],
                "greed": ev[GREED],
                "fear": ev[FEAR],
                "variant": cell.variant,
                "tf": cell.tf,
                "G": cell.G,
                "F": cell.F,
                "N": "" if cell.N is None else cell.N,
                "squeeze": cell.squeeze or "",
                "role": role,
                "cell": cell.id,
            })
    records.sort(key=lambda r: (r["date"], r["time"], r["ticker"], r["cell"]))
    return records


def focus_trades(records, score_days):
    have = set(score_days)
    if not any(day in have for day in FOCUS_DATES):
        return []
    want = {d.isoformat() for d in FOCUS_DATES}
    return [r for r in records if r["date"] in want]


SUMMARY_FIELDS = [
    "cell", "variant", "tf", "G", "F", "N", "squeeze", "strike", "band",
    "signals", "signal_days", "pct_sessions", "signals_per_session", "fills", "fill_days",
] + [f"hit_{int(level * 100)}_{window}" for window in WINDOWS for level in HIT_LEVELS] + [
    "random_n", "paired_hit_15_30", "random_hit_15_30", "hit_diff", "p", "q",
    "mean_mfe", "median_mfe", "median_t_peak", "mean_dd", "median_dd", "median_raw",
    "mean_tp15_sl15", "median_tp15_sl15", "win_tp15_sl15",
    "mean_tp15_sl25", "median_tp15_sl25", "win_tp15_sl25",
    "mean_tp15_nostop_30", "median_tp15_nostop_30", "win_tp15_nostop_30",
    "boot_hit_lo", "boot_hit_hi", "boot_net_lo", "boot_net_hi",
]

TRADE_FIELDS = [
    "date", "time", "ticker", "side", "contract", "entry_ask", "raw_entry", "peak_bid", "peak_net",
    "time_to_peak", "drawdown_net",
    "tp15_sl15_reason", "tp15_sl15_net", "tp15_sl25_reason", "tp15_sl25_net",
    "tp15_nostop_30_reason", "tp15_nostop_30_net",
    "greed", "fear", "variant", "tf", "G", "F", "N", "squeeze", "role", "cell",
]

FOLD_FIELDS = [
    "fold", "cell", "select_note", "train_start", "train_end", "test_start", "test_end",
    "train_signal_days", "train_fills", "train_hit", "test_signal_days", "test_fills",
    "test_hit", "test_paired_hit", "test_random_hit", "test_mean_net", "test_win",
    "boot_hit_lo", "boot_hit_hi",
]


def _write_csv(path, fields, rows):
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow({k: row.get(k, "") for k in fields})


def write_outputs(out_dir, report, rows, trades, folds, held):
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "FGFADE.md"), "w") as f:
        f.write(report)
    _write_csv(os.path.join(out_dir, "fgfade_summary.csv"), SUMMARY_FIELDS, rows)
    _write_csv(os.path.join(out_dir, "fgfade_trades.csv"), TRADE_FIELDS, trades)
    _write_csv(os.path.join(out_dir, "fgfade_folds.csv"), FOLD_FIELDS, list(folds) + [held])


def _env_flag(name):
    return os.getenv(name, "").strip().lower() in {"1", "true", "yes", "y"}


def _env_int(name, default):
    raw = os.getenv(name, "").strip()
    return int(raw) if raw else int(default)


def parse_tfs(raw):
    out = []
    for part in str(raw).split(","):
        part = part.strip()
        if not part:
            continue
        value = int(part)
        if value not in TFS:
            raise SystemExit("tfs must be a subset of 1,3,5")
        if value not in out:
            out.append(value)
    if not out:
        raise SystemExit("tfs must be a subset of 1,3,5")
    return tuple(out)


def keys_ready():
    return bool(os.getenv("ALPACA_KEY", "").strip() and os.getenv("ALPACA_SECRET", "").strip())


def _empty_report(path, message):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w") as f:
        f.write("# Fear-greed fade\n\n" + message + "\n\nData only. Research tool, not trading advice. No orders.\n")


def run_study(frames, symbols, score_days, tfs, und, opt=None, synthetic=False, cache_dir=None,
              workers=4, n_boot=1000, min_select=MIN_SELECT, costs=COSTS):
    """Score the grid. `opt` may be supplied by a test; otherwise contracts are downloaded for event minutes only."""
    t0 = time.time()
    cells = grid_cells(tfs)
    charts = build_charts(frames, score_days, tfs)
    events_by_cell = build_events(charts, cells)
    n_signals = sum(len(v) for v in events_by_cell.values())
    sc._print_scrubbed(f"  chart events {n_signals} cells {len(cells)}")
    random_of = draw_randoms(events_by_cell, score_days, symbols)
    keys = contract_keys(events_by_cell, random_of)
    if opt is None:
        needed = needed_contracts(keys, und, symbols, score_days)
        sc._print_scrubbed(f"  option days {len(needed)} contract-days {sum(len(v) for v in needed.values())}")
        opt = eh.fetch_option_days(
            needed, und, symbols, synthetic,
            cache_dir or "/tmp/fgfade-cache",
            workers=max(1, int(workers)),
        )
    fills = build_fills(keys, und, opt, symbols, score_days, costs)
    n_days = len(score_days)
    rows = []
    for cell in cells:
        for strike in STRIKES:
            for band in BANDS:
                rows.append(summarize_cell(
                    cell, events_by_cell[cell.id], fills, random_of, n_days, None,
                    strike, band, n_boot, sc.stream_seed("fgfade", cell.id, strike, band),
                ))
    assign_q(rows)
    folds = walk_forward(cells, events_by_cell, fills, random_of, score_days, n_boot, min_select)
    held = held_out(cells, events_by_cell, fills, random_of, score_days, n_boot, min_select)
    cells_by_id = {c.id: c for c in cells}
    chosen = reported_cells(rows)
    trades = trade_records(chosen, cells_by_id, events_by_cell, fills, score_days, symbols)
    meta = {
        "symbols": list(symbols),
        "tfs": list(tfs),
        "n_sessions": n_days,
        "first_day": score_days[0].isoformat(),
        "last_day": score_days[-1].isoformat(),
        "score_days": list(score_days),
        "n_cells": len(cells),
        "n_rows": len(rows),
        "n_boot": int(n_boot),
        "runtime_min": (time.time() - t0) / 60.0,
        "synthetic": bool(synthetic),
    }
    report = render_report(rows, folds, held, meta, focus_trades(trades, score_days))
    return {
        "rows": rows,
        "folds": folds,
        "held": held,
        "trades": trades,
        "report": report,
        "events": events_by_cell,
        "fills": fills,
        "meta": meta,
    }


def main():
    t0 = time.time()
    out_dir = os.getenv("FG_OUT", "results").strip() or "results"
    os.makedirs(out_dir, exist_ok=True)
    report_path = os.path.join(out_dir, "FGFADE.md")
    synthetic = _env_flag("FG_SYNTH")
    if not synthetic and not keys_ready():
        _empty_report(report_path, MISSING_KEYS)
        raise SystemExit(MISSING_KEYS)
    days_n = _env_int("FG_DAYS", 120)
    if days_n < K_FOLDS + 1:
        _empty_report(report_path, f"Need at least {K_FOLDS + 1} sessions. Got {days_n}.")
        raise SystemExit(f"days must be at least {K_FOLDS + 1}")
    tfs = parse_tfs(os.getenv("FG_TFS", "1,3,5"))
    symbols = [s.strip().upper() for s in os.getenv("FG_SYMBOLS", "SPY,QQQ").split(",") if s.strip()]
    if not symbols:
        raise SystemExit("symbols is empty")
    n_boot = _env_int("FG_BOOT", 1000)
    workers = _env_int("FG_WORKERS", 4)
    min_select = _env_int("FG_MIN_SELECT", MIN_SELECT)
    cache_dir = os.getenv("FG_CACHE", "/tmp/fgfade-cache").strip() or "/tmp/fgfade-cache"
    now = datetime.now(NY)
    end = datetime.now(timezone.utc) - timedelta(minutes=20)
    start = (pd.Timestamp(now.date(), tz=NY) - pd.Timedelta(days=int(days_n * 3 + 30))).tz_convert("UTC").to_pydatetime()
    sc._print_scrubbed(
        f"fgfade symbols {', '.join(symbols)} days {days_n} tfs {','.join(str(t) for t in tfs)} "
        f"synthetic {int(synthetic)}"
    )
    frames = sc._load_underlying(symbols, start, end, synthetic)
    und = {sym: sc.rth_session(df) for sym, df in frames.items()}
    all_days = sc.complete_days(und, symbols, now)
    if len(all_days) < K_FOLDS + 1:
        _empty_report(report_path, "Not enough completed sessions to score.")
        raise SystemExit("Not enough completed sessions.")
    score_days = all_days[-days_n:]
    sc._print_scrubbed(f"  sessions {score_days[0]} .. {score_days[-1]} n {len(score_days)}")
    result = run_study(
        frames, symbols, score_days, tfs, und,
        synthetic=synthetic, cache_dir=cache_dir, workers=workers,
        n_boot=n_boot, min_select=min_select,
    )
    result["meta"]["runtime_min"] = (time.time() - t0) / 60.0
    result["report"] = render_report(
        result["rows"], result["folds"], result["held"], result["meta"],
        focus_trades(result["trades"], score_days),
    )
    write_outputs(out_dir, result["report"], result["rows"], result["trades"], result["folds"], result["held"])
    sc._print_scrubbed(f"  wrote {report_path} runtime {result['meta']['runtime_min']:.1f} min")
    return result


if __name__ == "__main__":
    main()
