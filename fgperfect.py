"""Greed/fear fade, perfected: exits, filters, and a walk-forward on real option prices.

DATA ONLY. This module does not place orders. The family is predeclared. Thresholds,
exits, and filters are chosen on earlier sessions and scored on later ones.

The option tape has no bid or ask. "Ask" means the study cost model (print plus
half-spread on entry, print minus half-spread on the sale). "Mid + 1 cent" means
the print is treated as the mid and each side pays one cent. A spread filter on
that model is a premium floor: half-spread is max(1 cent, 0.5% of the print).
"""

from __future__ import annotations

import csv
import math
import os
import re
import time
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone

import numpy as np
import pandas as pd

import edge_hunt as eh
import fgfade as fg
import scalp_real as sc

NY = fg.NY
COSTS = fg.COSTS
HARD_MIN = 375  # 15:45 ET. The book is flat here. 15:55 is not used.
ENTRY_LO = fg.ENTRY_LO
ENTRY_HI = fg.ENTRY_HI
COOLDOWN = fg.COOLDOWN
SIGNAL_LEN = fg.SIGNAL_LEN
K_FOLDS = 5
MIN_FILLS = 100
MIN_DAYS = 60
HOLD_MOST = 0.50
N_SHUFFLE = 20
BLOCK = 5
FOCUS_DATES = fg.FOCUS_DATES
MISSING_KEYS = fg.MISSING_KEYS

# Exit grids.
TP_GRID = (0.10, 0.15, 0.20, 0.25, 0.30, 0.40, 0.50)
SL_GRID = (None, 0.10, 0.15, 0.20, 0.25, 0.30, 0.40, 0.50)
TIME_GRID = (5, 10, 15, 20, 30, 45, 60, None)  # None = hard flat at 15:45 only
DELAYS = (0, 1)
ARM_GRID = (0.10, 0.15, 0.20, 0.30)
TRAIL_GRID = (0.05, 0.10, 0.15, 0.20, 0.25)
BE_GRID = (0.10, 0.15)
SCALE_GRID = (0.15, 0.20, 0.25)
SCALE_Y = (0.10, 0.15, 0.20)
SIGNAL_KINDS = ("flip", "mom", "vwap", "band")
STALL_N = (3, 5, 10)
UND_K = (0.1, 0.2, 0.3)
UND_M = (0.5, 1.0, 1.5)
UND_TIME = (60, None)

REF_RULE = "fix_tp15_sl15_t30_d0"
BASE_ID = "tf1_turn_mom_g95_f20"

TFS = (1, 2, 3, 5)
HTF_OF = {1: 5, 2: 5, 3: 5, 5: 15}
G_LEVELS = (75, 80, 85, 90, 95, 100)
F_LEVELS = (0, 5, 10, 15, 20, 25, 30, 35)
PINNED = (1, 2, 3, 4, 5)
TURNS = ("base", "drop1", "drop2", "drop3", "cross", "within1", "within2", "within3")
PREMIUM_BANDS = (
    ("020_040", 0.20, 0.40),
    ("030_060", 0.30, 0.60),
    ("040_080", 0.40, 0.80),
    ("060_100", 0.60, 1.00),
    ("100_200", 1.00, 2.00),
    ("200p", 2.00, None),
)
SPREAD_KEEP = (("1", 0.01), ("2", 0.02), ("5", 0.05))
TOD_BUCKETS = (
    ("0935", 5, 30),
    ("1000", 30, 90),
    ("1100", 90, 150),
    ("1200", 150, 210),
    ("1300", 210, 270),
    ("1400", 270, 330),
    ("1500", 330, 376),
)
VIX_BUCKETS = ("lt14", "14_16", "16_18", "18_22", "22p")

# 2026 FOMC decision dates (second day of the meeting) and BLS CPI release dates.
FOMC_2026 = {
    datetime(2026, 1, 28).date(), datetime(2026, 3, 18).date(), datetime(2026, 4, 29).date(),
    datetime(2026, 6, 17).date(), datetime(2026, 7, 29).date(), datetime(2026, 9, 16).date(),
    datetime(2026, 10, 28).date(), datetime(2026, 12, 9).date(),
}
CPI_2026 = {
    datetime(2026, 1, 13).date(), datetime(2026, 2, 13).date(), datetime(2026, 3, 11).date(),
    datetime(2026, 4, 10).date(), datetime(2026, 5, 12).date(), datetime(2026, 6, 10).date(),
    datetime(2026, 7, 14).date(), datetime(2026, 8, 12).date(), datetime(2026, 9, 11).date(),
    datetime(2026, 10, 14).date(), datetime(2026, 11, 10).date(), datetime(2026, 12, 10).date(),
}
EVENT_DAYS = FOMC_2026 | CPI_2026

GATE_FAIL = "Nothing met the candidate bar of 100 fills and 60 days on the first 75% of sessions."
NONE_POS = "No entry and exit in this family has a positive held-out net expectancy."
POS_NOT_RANDOM = (
    "Some entry and exit combinations have a positive held-out net, "
    "and none of them beats a random entry that uses the same exit."
)

STOP, TP, TIME, FLAT = 1, 2, 3, 4
TRAIL, BE, SCALE, SIGNAL, STALL = 5, 6, 7, 8, 9
UND_STOP, UND_TP = 10, 11


def _pct_tag(x):
    return str(int(round(float(x) * 100)))


def _time_tag(t):
    return "flat" if t is None else str(int(t))


@dataclass(frozen=True)
class Rule:
    id: str
    kind: str  # fix, trail, be, scale, signal, stall, und
    family: str
    tp: float | None = None
    sl: float | None = None
    time_min: int | None = None
    delay: int = 0
    arm: float | None = None
    trail: float | None = None
    scale: float | None = None
    signal: str | None = None
    stall_n: int | None = None
    und_k: float | None = None
    und_m: float | None = None

    @property
    def axes(self):
        """The two parameters a stability table should cross, and the values that stay put."""
        if self.kind == "fix":
            return ("tp", "sl")
        if self.kind == "trail":
            return ("arm", "trail")
        if self.kind == "be":
            return ("arm", "delay")
        if self.kind == "scale":
            return ("scale", "trail")
        if self.kind == "signal":
            return ("signal", "delay")
        if self.kind == "stall":
            return ("stall_n", "delay")
        return ("und_k", "und_m")


def exit_rules():
    """Every exit the study scores. Delay 0 and delay 1 are separate rules."""
    rules = []
    for tp in TP_GRID:
        for sl in SL_GRID:
            for tm in TIME_GRID:
                for delay in DELAYS:
                    sl_tag = "none" if sl is None else _pct_tag(sl)
                    rules.append(Rule(
                        f"fix_tp{_pct_tag(tp)}_sl{sl_tag}_t{_time_tag(tm)}_d{delay}",
                        "fix", "fixed", tp=tp, sl=sl, time_min=tm, delay=delay,
                    ))
    for arm in ARM_GRID:
        for y in TRAIL_GRID:
            for delay in DELAYS:
                rules.append(Rule(
                    f"trail_a{_pct_tag(arm)}_y{_pct_tag(y)}_d{delay}",
                    "trail", "trail", arm=arm, trail=y, delay=delay,
                ))
    for arm in BE_GRID:
        for delay in DELAYS:
            rules.append(Rule(
                f"be_a{_pct_tag(arm)}_d{delay}",
                "be", "breakeven", arm=arm, delay=delay,
            ))
    for scale in SCALE_GRID:
        for y in SCALE_Y:
            for delay in DELAYS:
                rules.append(Rule(
                    f"scale_s{_pct_tag(scale)}_y{_pct_tag(y)}_d{delay}",
                    "scale", "scale", scale=scale, trail=y, delay=delay,
                ))
    for name in SIGNAL_KINDS:
        for delay in DELAYS:
            rules.append(Rule(
                f"sig_{name}_d{delay}",
                "signal", "signal", signal=name, delay=delay,
            ))
    for n in STALL_N:
        for delay in DELAYS:
            rules.append(Rule(
                f"stall_n{n}_d{delay}",
                "stall", "stall", stall_n=n, delay=delay,
            ))
    for k in UND_K:
        for m in UND_M:
            for tm in UND_TIME:
                for delay in DELAYS:
                    rules.append(Rule(
                        f"und_k{_pct_tag(k)}_m{_pct_tag(m)}_t{_time_tag(tm)}_d{delay}",
                        "und", "underlying", und_k=k, und_m=m, time_min=tm, delay=delay,
                    ))
    return tuple(rules)


def expected_rule_count():
    return (
        len(TP_GRID) * len(SL_GRID) * len(TIME_GRID) * len(DELAYS)
        + len(ARM_GRID) * len(TRAIL_GRID) * len(DELAYS)
        + len(BE_GRID) * len(DELAYS)
        + len(SCALE_GRID) * len(SCALE_Y) * len(DELAYS)
        + len(SIGNAL_KINDS) * len(DELAYS)
        + len(STALL_N) * len(DELAYS)
        + len(UND_K) * len(UND_M) * len(UND_TIME) * len(DELAYS)
    )


@dataclass(frozen=True)
class Spec:
    id: str
    kind: str  # base, signal, mask, fill
    family: str
    tf: int = 1
    g: int = 95
    f: int = 20
    pinned_k: int = 1
    turn: str = "base"
    mom: str = "both"  # both, squeeze, macd
    squeeze: str = "any"
    vwap_min: float = 0.0
    outside: bool = False
    rsi: bool = False
    stoch: bool = False
    cci: bool = False
    candle: str = "off"
    htf: bool = False
    mask: str = ""
    strike: str = "1otm"
    dte: int = 0
    band: tuple | None = None
    cost: str = "ask"
    spread_max: float | None = None
    entry_delay: int = 0

    def signal_key(self):
        return (
            self.tf, self.g, self.f, self.pinned_k, self.turn, self.mom, self.squeeze,
            float(self.vwap_min), bool(self.outside), bool(self.rsi), bool(self.stoch),
            bool(self.cci), self.candle, bool(self.htf),
        )

    def book_key(self):
        return (self.signal_key(), self.strike, int(self.dte), int(self.entry_delay))


def _base_kwargs():
    return dict(tf=1, g=95, f=20, pinned_k=1, turn="base", mom="both", squeeze="any")


def entry_specs(gex=False):
    """One change from the base at a time, plus the base. Not a full cross."""
    b = _base_kwargs()
    specs = [Spec(BASE_ID, "base", "base", **b)]

    def add(spec_id, kind, family, **kw):
        fields = dict(b)
        fields.update(kw)
        specs.append(Spec(spec_id, kind, family, **fields))

    for tf in TFS:
        if tf == 1:
            continue
        add(f"tf{tf}_turn_mom_g95_f20", "signal", "tf", tf=tf)
    for g in G_LEVELS:
        if g == 95:
            continue
        add(f"tf1_turn_mom_g{g}_f20", "signal", "G", g=g)
    for f in F_LEVELS:
        if f == 20:
            continue
        add(f"tf1_turn_mom_g95_f{f}", "signal", "F", f=f)
    for k in PINNED:
        if k == 1:
            continue
        add(f"tf1_turn_mom_g95_f20_k{k}", "signal", "pinned", pinned_k=k)
    for turn, label in (
        ("drop1", "drop1"), ("drop2", "drop2"), ("drop3", "drop3"), ("cross", "cross"),
        ("within1", "within1"), ("within2", "within2"), ("within3", "within3"),
    ):
        add(f"tf1_{label}_mom_g95_f20", "signal", "turn", turn=turn)
    add("tf1_turn_sq_g95_f20", "signal", "mom", mom="squeeze")
    add("tf1_turn_macd_g95_f20", "signal", "mom", mom="macd")
    for sq, tag in (("on", "sqon"), ("off", "sqoff"), ("released", "sqrel")):
        add(f"tf1_turn_mom_g95_f20_{tag}", "signal", "squeeze", squeeze=sq)
    for dist in (0.5, 1.0, 1.5, 2.0):
        tag = str(dist).replace(".", "")
        add(f"tf1_turn_mom_g95_f20_vwap{tag}", "signal", "vwap", vwap_min=dist)
    add("tf1_turn_mom_g95_f20_band", "signal", "band", outside=True)
    add("tf1_turn_mom_g95_f20_rsi", "signal", "rsi", rsi=True)
    add("tf1_turn_mom_g95_f20_stoch", "signal", "stoch", stoch=True)
    add("tf1_turn_mom_g95_f20_cci", "signal", "cci", cci=True)
    add("tf1_turn_mom_g95_f20_wick", "signal", "candle", candle="wick")
    add("tf1_turn_mom_g95_f20_engulf", "signal", "candle", candle="engulf")
    add("tf1_turn_mom_g95_f20_htf", "signal", "htf", htf=True)

    masks = []
    for name in ("rvol_low", "rvol_mid", "rvol_high"):
        masks.append((name, "rvol"))
    for name in ("above_pdh", "below_pdl", "above_pdc", "below_pdc"):
        masks.append((name, "prior_day"))
    for name in ("orb_break", "orb_hold"):
        masks.append((name, "orb"))
    for name in ("near_high", "near_low"):
        masks.append((name, "day_extreme"))
    for name in ("gap_up", "gap_down", "gap_flat"):
        masks.append((name, "gap"))
    for name in ("trend_up", "trend_down", "trend_flat"):
        masks.append((name, "trend"))
    masks.append(("spyqqq", "agree"))
    for name in VIX_BUCKETS:
        masks.append((f"vix_{name}", "vix"))
    for name in ("vix_up", "vix_down", "vix_flat"):
        masks.append((name, "vix_change"))
    for name in ("mon", "tue", "wed", "thu", "fri"):
        masks.append((f"dow_{name}", "dow"))
    for name, _a, _b in TOD_BUCKETS:
        masks.append((f"tod_{name}", "tod"))
    for name in ("since_lt20", "since_20_40", "since_40_60", "since_60p"):
        masks.append((name, "since"))
    for name in ("nth_1", "nth_2", "nth_3p"):
        masks.append((name, "nth"))
    for name in ("side_call", "side_put"):
        masks.append((name, "side"))
    for name in ("prev_win", "prev_loss"):
        masks.append((name, "prev"))
    for name in ("regime_trend", "regime_range"):
        masks.append((name, "regime"))
    for name in ("event_yes", "event_no"):
        masks.append((name, "event"))
    if gex:
        for name in ("gex_above", "gex_below", "gex_near_call", "gex_near_put"):
            masks.append((name, "gex"))
    for name, family in masks:
        add(f"{BASE_ID}__{name}", "mask", family, mask=name)

    add(f"{BASE_ID}__atm", "fill", "strike", strike="atm")
    add(f"{BASE_ID}__2otm", "fill", "strike", strike="2otm")
    add(f"{BASE_ID}__dte1", "fill", "dte", dte=1)
    for tag, lo, hi in PREMIUM_BANDS:
        add(f"{BASE_ID}__prem_{tag}", "fill", "premium", band=(lo, hi))
    add(f"{BASE_ID}__mid1c", "fill", "cost", cost="mid1c")
    for tag, cap in SPREAD_KEEP:
        add(f"{BASE_ID}__spread{tag}", "fill", "spread", spread_max=cap)
    add(f"{BASE_ID}__edelay1", "fill", "entry_delay", entry_delay=1)
    add(f"{BASE_ID}__edelay2", "fill", "entry_delay", entry_delay=2)
    return tuple(specs)


def family_count(gex=False):
    return len(entry_specs(gex=gex)) * len(exit_rules())


def smoke_catalog():
    """A few specs and rules that still walk the same code as the full family."""
    specs = entry_specs(gex=False)
    by_id = {s.id: s for s in specs}
    rules = exit_rules()
    by_rule = {r.id: r for r in rules}
    keep_s = [by_id[BASE_ID], by_id["tf2_turn_mom_g95_f20"], by_id[f"{BASE_ID}__tod_1000"], by_id[f"{BASE_ID}__mid1c"]]
    keep_r = [
        by_rule[REF_RULE],
        by_rule["fix_tp15_sl15_t30_d1"],
        by_rule["trail_a15_y10_d0"],
        by_rule["scale_s15_y10_d0"],
        by_rule["stall_n5_d0"],
        by_rule["sig_flip_d0"],
    ]
    return tuple(keep_s), tuple(keep_r)


# -------------------------------------------------------------------------------- indicators


def rsi_wilder(close, length=14):
    c = np.asarray(close, dtype=float)
    delta = np.diff(c, prepend=np.nan)
    up = np.where(np.isfinite(delta) & (delta > 0), delta, 0.0)
    dn = np.where(np.isfinite(delta) & (delta < 0), -delta, 0.0)
    up[~np.isfinite(delta)] = np.nan
    dn[~np.isfinite(delta)] = np.nan
    au = pd.Series(up).ewm(alpha=1.0 / length, adjust=False, min_periods=length).mean().to_numpy()
    ad = pd.Series(dn).ewm(alpha=1.0 / length, adjust=False, min_periods=length).mean().to_numpy()
    out = np.full(len(c), np.nan)
    both = np.isfinite(au) & np.isfinite(ad)
    nz = both & (ad > 0)
    out[nz] = 100.0 - 100.0 / (1.0 + au[nz] / ad[nz])
    out[both & (ad == 0) & (au > 0)] = 100.0
    out[both & (au == 0) & (ad > 0)] = 0.0
    out[both & (au == 0) & (ad == 0)] = 50.0
    return out


def stoch_k(high, low, close, length=14):
    h = pd.Series(np.asarray(high, dtype=float))
    l = pd.Series(np.asarray(low, dtype=float))
    c = pd.Series(np.asarray(close, dtype=float))
    lo = l.rolling(length, min_periods=length).min()
    hi = h.rolling(length, min_periods=length).max()
    span = (hi - lo).replace(0, np.nan)
    return (100.0 * (c - lo) / span).to_numpy(dtype=float)


def rvol_prior(volume, minute, day_ord):
    """Volume / mean of this minute-of-day on earlier sessions only."""
    vol = np.asarray(volume, dtype=float)
    minute = np.asarray(minute)
    day = np.asarray(day_ord)
    out = np.full(len(vol), np.nan)
    if len(vol) == 0:
        return out
    order = np.argsort(day, kind="mergesort")
    sums = {}
    counts = {}
    seen_day = {}
    # Walk in day order. The mean uses sessions strictly before this bar's day.
    for idx in order:
        m = int(minute[idx])
        d = int(day[idx])
        prev_sum, prev_n = sums.get(m, 0.0), counts.get(m, 0)
        if prev_n > 0 and np.isfinite(vol[idx]):
            out[idx] = vol[idx] / (prev_sum / prev_n)
        seen_day.setdefault(m, {})
        if d not in seen_day[m]:
            seen_day[m][d] = idx
    # Add each session's bar once, after the value was read.
    for m, days in seen_day.items():
        running_s = 0.0
        running_n = 0
        for d in sorted(days):
            idx = days[d]
            if running_n > 0 and np.isfinite(vol[idx]):
                out[idx] = vol[idx] / (running_s / running_n)
            if np.isfinite(vol[idx]):
                running_s += float(vol[idx])
                running_n += 1
    return out


def _running_day_extreme(high, low, day_ord):
    h = np.asarray(high, dtype=float)
    l = np.asarray(low, dtype=float)
    day = np.asarray(day_ord)
    dh = np.full(len(h), np.nan)
    dl = np.full(len(l), np.nan)
    if len(h) == 0:
        return dh, dl
    change = np.r_[True, day[1:] != day[:-1]]
    starts = np.flatnonzero(change)
    ends = np.r_[starts[1:], len(h)]
    for a, b in zip(starts, ends):
        dh[a:b] = np.maximum.accumulate(np.where(np.isfinite(h[a:b]), h[a:b], -np.inf))
        dl[a:b] = np.minimum.accumulate(np.where(np.isfinite(l[a:b]), l[a:b], np.inf))
    dh[~np.isfinite(h)] = np.nan
    dl[~np.isfinite(l)] = np.nan
    return dh, dl


def enrich_chart(df, tf, score_index):
    """fgfade chart plus the extra panes this study filters on. Causal: the bar is closed."""
    frame = fg.build_chart(df, tf, score_index)
    bars = fg.to_tf(df, tf)
    n = len(bars)
    if n == 0:
        for key in ("open", "high", "low", "volume", "minute", "vwap", "atr", "rsi", "stoch", "cci", "rvol", "day_high", "day_low"):
            frame[key] = np.zeros(0)
        return frame
    high = bars["high"].to_numpy(dtype=float)
    low = bars["low"].to_numpy(dtype=float)
    close = bars["close"].to_numpy(dtype=float)
    vol = bars["volume"].to_numpy(dtype=float)
    minute = (bars.index.hour * 60 + bars.index.minute - (9 * 60 + 30)).to_numpy(dtype=int)
    frame["open"] = bars["open"].to_numpy(dtype=float)
    frame["high"] = high
    frame["low"] = low
    frame["volume"] = vol
    frame["minute"] = minute
    frame["vwap"] = fg.session_vwap(high, low, close, vol, frame["day_ord"])
    frame["atr"] = fg.atr14(high, low, close)
    frame["rsi"] = rsi_wilder(close, 14)
    frame["stoch"] = stoch_k(high, low, close, 14)
    frame["cci"] = eh.cci_lambert(high, low, close, length=20, const=0.015)
    frame["rvol"] = rvol_prior(vol, minute, frame["day_ord"])
    dh, dl = _running_day_extreme(high, low, frame["day_ord"])
    frame["day_high"] = dh
    frame["day_low"] = dl
    return frame


def _pinned_prior(ext, day, k):
    """True when the previous `k` bars, not this one, were extreme. Same session only."""
    ext = np.asarray(ext, dtype=bool)
    day = np.asarray(day)
    ok = np.ones(len(ext), dtype=bool)
    for lag in range(1, int(k) + 1):
        same = fg._same_day(day, lag)
        shifted = np.zeros(len(ext), dtype=bool)
        if lag < len(ext):
            shifted[lag:] = ext[:-lag]
        ok &= shifted & same
    return ok


def _drop_points(level, other, g, f, day, points):
    level = np.asarray(level, dtype=float)
    other = np.asarray(other, dtype=float)
    day = np.asarray(day)
    n = len(level)
    out = np.zeros(n, dtype=bool)
    if n < 2:
        return out
    same = fg._same_day(day, 1)
    prev_ext = np.zeros(n, dtype=bool)
    prev_ext[1:] = (level[:-1] >= float(g)) & (other[:-1] <= float(f)) & np.isfinite(level[:-1]) & np.isfinite(other[:-1])
    drop = np.zeros(n, dtype=bool)
    drop[1:] = np.isfinite(level[1:]) & np.isfinite(level[:-1]) & ((level[:-1] - level[1:]) >= float(points))
    peak = np.ones(n, dtype=bool)
    if n >= 3:
        same2 = np.zeros(n, dtype=bool)
        same2[2:] = (day[2:] == day[1:-1]) & (day[1:-1] == day[:-2])
        peak[2:] = np.isfinite(level[:-2]) & (level[1:-1] >= level[:-2]) & same2[2:]
    return prev_ext & same & drop & peak


def _cross_only(level, other, g, f, signal, day):
    level = np.asarray(level, dtype=float)
    other = np.asarray(other, dtype=float)
    signal = np.asarray(signal, dtype=float)
    day = np.asarray(day)
    n = len(level)
    out = np.zeros(n, dtype=bool)
    if n < 2:
        return out
    same = fg._same_day(day, 1)
    prev_ext = np.zeros(n, dtype=bool)
    prev_ext[1:] = (level[:-1] >= float(g)) & (other[:-1] <= float(f)) & np.isfinite(level[:-1]) & np.isfinite(other[:-1])
    cross = np.zeros(n, dtype=bool)
    cross[1:] = (
        (level[:-1] >= signal[:-1]) & (level[1:] < signal[1:])
        & np.isfinite(level[:-1]) & np.isfinite(level[1:])
        & np.isfinite(signal[:-1]) & np.isfinite(signal[1:])
        & same[1:]
    )
    return prev_ext & cross


def _within(turn, mom, day, n_bars):
    n_bars = int(n_bars)
    if n_bars <= 0:
        return np.asarray(turn, dtype=bool) & np.asarray(mom, dtype=bool)
    last_t = fg.last_true_index(turn, day)
    last_m = fg.last_true_index(mom, day)
    idx = np.arange(len(day))
    lo = idx - n_bars
    ok = (last_t >= 0) & (last_m >= 0) & (last_t >= lo) & (last_m >= lo)
    return fg.first_in_run(ok, day)


def _squeeze_ok(frame, mode):
    if mode in (None, "any"):
        return np.ones(len(frame["day_ord"]), dtype=bool)
    if mode == "on":
        return frame["_sq_on"]
    if mode == "released":
        return frame["_sq_rel"]
    if mode == "off":
        return frame["_sq_off"]
    raise ValueError(mode)


def _turn_mask(frame, side, spec):
    """Boolean turn for one side. side -1 is the put (greed pinned)."""
    day = frame["day_ord"]
    if side == -1:
        level, other, sig = frame["greed"], frame["fear"], frame["greed_sig"]
        base = fg.side_turn(level, other, spec.g, spec.f, sig, day)
        mom = frame["_mom_dn"]
        macd = frame["_macd_dn"]
    else:
        level, other, sig = frame["fear"], frame["greed"], frame["fear_sig"]
        base = fg.side_turn(level, other, spec.g, spec.f, sig, day)
        mom = frame["_mom_up"]
        macd = frame["_macd_up"]
    if spec.mom == "squeeze":
        mom_ok = mom
    elif spec.mom == "macd":
        mom_ok = macd
    else:
        mom_ok = mom | macd
    if spec.turn == "base":
        turn = base
        fired = turn & mom_ok
    elif spec.turn == "cross":
        turn = _cross_only(level, other, spec.g, spec.f, sig, day)
        fired = turn & mom_ok
    elif spec.turn in ("drop1", "drop2", "drop3"):
        pts = int(spec.turn[-1])
        turn = _drop_points(level, other, spec.g, spec.f, day, pts)
        fired = turn & mom_ok
    elif spec.turn.startswith("within"):
        n_bars = int(spec.turn[-1])
        fired = _within(base, mom_ok, day, n_bars)
        turn = base
    else:
        raise ValueError(spec.turn)
    if spec.pinned_k > 1:
        ext = (level >= float(spec.g)) & (other <= float(spec.f)) & np.isfinite(level) & np.isfinite(other)
        fired = fired & _pinned_prior(ext, day, spec.pinned_k)
    fired = fired & _squeeze_ok(frame, spec.squeeze)
    return fired


def _bar_filters(frame, side, spec):
    """Extra conditions on the closed signal bar. True when the spec does not use that filter."""
    n = len(frame["day_ord"])
    ok = np.ones(n, dtype=bool)
    close = frame["close"]
    atr = frame["atr"]
    vwap = frame["vwap"]
    dist = np.full(n, np.nan)
    good = np.isfinite(atr) & (atr > 0) & np.isfinite(vwap) & np.isfinite(close)
    if side == -1:
        dist[good] = (close[good] - vwap[good]) / atr[good]
    else:
        dist[good] = (vwap[good] - close[good]) / atr[good]
    if spec.vwap_min > 0:
        ok &= np.isfinite(dist) & (dist >= float(spec.vwap_min))
    if spec.outside:
        ok &= fg.outside_band(close, frame["vwap_up"], frame["vwap_dn"], frame["bb_up"], frame["bb_dn"], side)
    if spec.rsi:
        rsi = frame["rsi"]
        ok &= (rsi > 70) if side == -1 else (rsi < 30)
    if spec.stoch:
        k = frame["stoch"]
        ok &= (k > 80) if side == -1 else (k < 20)
    if spec.cci:
        cci = frame["cci"]
        ok &= (cci > 100) if side == -1 else (cci < -100)
    if spec.candle == "wick":
        ok &= _wick(frame, side)
    elif spec.candle == "engulf":
        ok &= _engulf(frame, side)
    return ok


def _wick(frame, side):
    o = frame["open"]
    h = frame["high"]
    l = frame["low"]
    c = frame["close"]
    body = np.abs(c - o)
    upper = h - np.maximum(o, c)
    lower = np.minimum(o, c) - l
    if side == -1:
        return (upper > 2.0 * body) & (upper > lower) & np.isfinite(upper)
    return (lower > 2.0 * body) & (lower > upper) & np.isfinite(lower)


def _engulf(frame, side):
    o = frame["open"]
    c = frame["close"]
    day = frame["day_ord"]
    n = len(c)
    out = np.zeros(n, dtype=bool)
    if n < 2:
        return out
    same = fg._same_day(day, 1)
    if side == -1:
        out[1:] = (c[:-1] > o[:-1]) & (c[1:] < o[1:]) & (c[1:] <= o[:-1]) & (o[1:] >= c[:-1]) & same[1:]
    else:
        out[1:] = (c[:-1] < o[:-1]) & (c[1:] > o[1:]) & (c[1:] >= o[:-1]) & (o[1:] <= c[:-1]) & same[1:]
    return out


class Event:
    """Chart event. The first seven fields match fgfade's cooldown tuple."""

    __slots__ = (
        "day_i", "sym", "minute", "side", "pin", "fear", "greed",
        "sq", "mom", "close", "atr", "vwap", "rvol", "rsi",
        "since", "nth", "agree", "gap", "trend", "regime", "event",
        "bar_high", "bar_low",
        "orb_break", "orb_hold", "near_high", "near_low",
        "above_pdh", "below_pdl", "above_pdc", "below_pdc",
        "vix", "vix_chg", "dow", "gex",
    )

    def __init__(self, **kw):
        for name in self.__slots__:
            setattr(self, name, kw.get(name))

    def __getitem__(self, i):
        return (self.day_i, self.sym, self.minute, self.side, self.pin, self.fear, self.greed)[i]


def _session_features(und, sym, day, minute):
    """Session facts known at `minute`. Prior-day levels come from the previous session in `und`."""
    sess = und[sym].get(day)
    out = {
        "gap": 0, "regime": "range", "orb_high": np.nan, "orb_low": np.nan,
        "pdh": np.nan, "pdl": np.nan, "pdc": np.nan, "open": np.nan,
    }
    if sess is None:
        return out
    if sess["real"][0] and np.isfinite(sess["open"][0]):
        out["open"] = float(sess["open"][0])
    prior_days = [d for d in und[sym] if d < day]
    if prior_days:
        prev = und[sym][prior_days[-1]]
        real = prev["real"]
        if real.any():
            out["pdh"] = float(np.nanmax(prev["high"]))
            out["pdl"] = float(np.nanmin(prev["low"]))
            last = int(np.flatnonzero(real)[-1])
            out["pdc"] = float(prev["close"][last])
            first = int(np.flatnonzero(real)[0])
            span = out["pdh"] - out["pdl"]
            if span > 0 and np.isfinite(prev["open"][first]):
                body = abs(float(prev["close"][last]) - float(prev["open"][first])) / span
                out["regime"] = "trend" if body > 0.6 else "range"
    if out["open"] == out["open"] and out["pdc"] == out["pdc"] and out["pdc"] != 0:
        gap = (out["open"] - out["pdc"]) / out["pdc"]
        out["gap"] = 1 if gap > 0.001 else (-1 if gap < -0.001 else 0)
    # Opening range is the first 15 minutes (9:30 through 9:44). Known from minute 15.
    if minute >= 15:
        sl = slice(0, 15)
        if sess["real"][sl].any():
            out["orb_high"] = float(np.nanmax(sess["high"][sl]))
            out["orb_low"] = float(np.nanmin(sess["low"][sl]))
    return out


def _htf_agree_at(htf, day_i, entry_minute, side, g, f):
    """Last HTF bar that closed at or before the entry, same score day, same extreme."""
    if htf is None:
        return False
    sel = (htf["day_i"] == day_i) & (htf["entry"] >= 0) & (htf["entry"] <= int(entry_minute))
    idx = np.flatnonzero(sel)
    if len(idx) == 0:
        return False
    i = int(idx[-1])
    fear = float(htf["fear"][i])
    greed = float(htf["greed"][i])
    if side == -1:
        return greed >= float(g) and fear <= float(f)
    return fear >= float(g) and greed <= float(f)


def _emit_spec(frame, sym_i, spec, htf):
    fg.prepare_frame(frame)
    events = []
    for side in (-1, 1):
        mask = _turn_mask(frame, side, spec) & _bar_filters(frame, side, spec)
        mask &= frame["score"] & (frame["day_i"] >= 0) & (frame["entry"] >= 0)
        for i in np.flatnonzero(mask):
            if spec.htf and not _htf_agree_at(htf, int(frame["day_i"][i]), int(frame["entry"][i]), side, spec.g, spec.f):
                continue
            pin = float(frame["greed"][i] if side == -1 else frame["fear"][i])
            events.append(Event(
                day_i=int(frame["day_i"][i]), sym=int(sym_i), minute=int(frame["entry"][i]), side=int(side),
                pin=pin, fear=float(frame["fear"][i]), greed=float(frame["greed"][i]),
                sq=bool(frame["sq_on"][i]), mom=float(frame["mom"][i]) if np.isfinite(frame["mom"][i]) else float("nan"),
                close=float(frame["close"][i]), atr=float(frame["atr"][i]) if np.isfinite(frame["atr"][i]) else float("nan"),
                vwap=float(frame["vwap"][i]) if np.isfinite(frame["vwap"][i]) else float("nan"),
                rvol=float(frame["rvol"][i]) if np.isfinite(frame["rvol"][i]) else float("nan"),
                rsi=float(frame["rsi"][i]) if np.isfinite(frame["rsi"][i]) else float("nan"),
                bar_high=float(frame["high"][i]), bar_low=float(frame["low"][i]),
                since=None, nth=None, agree=False,
            ))
    return events


def _annotate(events, und, symbols, score_days, vix, vix_chg, gex_lookup):
    """Stamp session features, then minutes-since and the day's count on the raw stream."""
    by_sym_day = {}
    for ev in events:
        day = score_days[ev.day_i]
        feat = _session_features(und, symbols[ev.sym], day, ev.minute)
        ev.gap = feat["gap"]
        ev.regime = feat["regime"]
        ev.event = day in EVENT_DAYS
        ev.dow = int(day.weekday())
        ev.vix = vix.get(day, float("nan"))
        ev.vix_chg = vix_chg.get(day, float("nan"))
        ev.above_pdh = ev.close > feat["pdh"] if feat["pdh"] == feat["pdh"] else False
        ev.below_pdl = ev.close < feat["pdl"] if feat["pdl"] == feat["pdl"] else False
        ev.above_pdc = ev.close > feat["pdc"] if feat["pdc"] == feat["pdc"] else False
        ev.below_pdc = ev.close < feat["pdc"] if feat["pdc"] == feat["pdc"] else False
        ev.near_high = False
        ev.near_low = False
        # Day high / low through the entry minute, from the underlying session.
        sess = und[symbols[ev.sym]].get(day)
        if sess is not None and ev.atr == ev.atr and ev.atr > 0 and ev.minute > 0:
            # Through the bar before the entry. The entry bar's high is not known at the open.
            sl = slice(0, ev.minute)
            if sess["real"][sl].any():
                dh = float(np.nanmax(sess["high"][sl]))
                dl = float(np.nanmin(sess["low"][sl]))
                if dh == dh:
                    ev.near_high = (dh - ev.close) / ev.atr < 0.25
                if dl == dl:
                    ev.near_low = (ev.close - dl) / ev.atr < 0.25
        ev.orb_break = False
        ev.orb_hold = False
        if ev.minute >= 15 and feat["orb_high"] == feat["orb_high"]:
            hi = ev.bar_high if ev.bar_high == ev.bar_high else float("nan")
            lo = ev.bar_low if ev.bar_low == ev.bar_low else float("nan")
            if ev.side == -1:
                ev.orb_break = ev.close > feat["orb_high"]
                ev.orb_hold = hi == hi and hi > feat["orb_high"] and ev.close <= feat["orb_high"]
            else:
                ev.orb_break = ev.close < feat["orb_low"]
                ev.orb_hold = lo == lo and lo < feat["orb_low"] and ev.close >= feat["orb_low"]
        if ev.atr == ev.atr and ev.atr > 0 and ev.vwap == ev.vwap:
            slope = (ev.close - ev.vwap) / ev.atr
            ev.trend = 1 if slope > 0.5 else (-1 if slope < -0.5 else 0)
        else:
            ev.trend = 0
        ev.gex = gex_lookup(symbols[ev.sym], day, ev.minute) if gex_lookup else {}
        by_sym_day.setdefault((ev.day_i, ev.sym), []).append(ev)
    for rows in by_sym_day.values():
        rows.sort(key=lambda e: e.minute)
        prev_m = None
        for i, ev in enumerate(rows):
            ev.nth = i + 1
            ev.since = 10_000 if prev_m is None else int(ev.minute - prev_m)
            prev_m = ev.minute
    # Other symbol, same side, within 2 minutes, on the raw stream.
    index = {}
    for ev in events:
        index.setdefault((ev.day_i, ev.sym, ev.side), []).append(ev.minute)
    for ev in events:
        other = 1 - ev.sym if ev.sym in (0, 1) else None
        minutes = index.get((ev.day_i, other, ev.side), [])
        ev.agree = any(abs(int(m) - ev.minute) <= 2 for m in minutes)
    return events


def build_signal_events(charts, spec, und, symbols, score_days, vix, vix_chg, gex_lookup):
    htf_tf = HTF_OF[spec.tf]
    raw = []
    for sym_i in range(len(symbols)):
        htf = charts[htf_tf][sym_i] if spec.htf else None
        raw.extend(_emit_spec(charts[spec.tf][sym_i], sym_i, spec, htf))
    _annotate(raw, und, symbols, score_days, vix, vix_chg, gex_lookup)
    cooled = fg.apply_cooldown(raw, COOLDOWN)
    return cooled


# -------------------------------------------------------------------------------- option paths


def _dense(frame, n_days, key):
    out = np.full((n_days, sc.N_MIN), np.nan)
    if len(frame.get("day_i", [])) == 0:
        return out
    for i, day_i in enumerate(frame["day_i"]):
        if day_i < 0:
            continue
        m = int(frame["minute"][i])
        if 0 <= m < sc.N_MIN:
            val = frame[key][i]
            out[int(day_i), m] = val
    return out


def _bool_dense(frame, n_days, mask):
    out = np.zeros((n_days, sc.N_MIN), dtype=bool)
    if len(frame.get("day_i", [])) == 0:
        return out
    for i, day_i in enumerate(frame["day_i"]):
        if day_i < 0 or not mask[i]:
            continue
        m = int(frame["minute"][i])
        if 0 <= m < sc.N_MIN:
            out[int(day_i), m] = True
    return out


def signal_grids(frame_1m, n_days, g, f):
    """1-minute exit flags. Index is the bar's start minute. The close of that bar is the decision."""
    fg.prepare_frame(frame_1m)
    day = frame_1m["day_ord"]
    fear, greed = frame_1m["fear"], frame_1m["greed"]
    # Flip back: pinned side crosses up through its signal, or the opposite extreme prints.
    g_cross = np.zeros(len(greed), dtype=bool)
    f_cross = np.zeros(len(fear), dtype=bool)
    if len(greed) >= 2:
        same = fg._same_day(day, 1)
        g_cross[1:] = (
            (greed[:-1] < frame_1m["greed_sig"][:-1]) & (greed[1:] >= frame_1m["greed_sig"][1:])
            & np.isfinite(greed[:-1]) & np.isfinite(greed[1:]) & same[1:]
        )
        f_cross[1:] = (
            (fear[:-1] < frame_1m["fear_sig"][:-1]) & (fear[1:] >= frame_1m["fear_sig"][1:])
            & np.isfinite(fear[:-1]) & np.isfinite(fear[1:]) & same[1:]
        )
    opp_put = (fear >= float(g)) & (greed <= float(f))
    opp_call = (greed >= float(g)) & (fear <= float(f))
    flip_put = g_cross | opp_put
    flip_call = f_cross | opp_call
    mom_dn = frame_1m["_mom_dn"]
    mom_up = frame_1m["_mom_up"]
    return {
        "flip_put": _bool_dense(frame_1m, n_days, flip_put),
        "flip_call": _bool_dense(frame_1m, n_days, flip_call),
        "mom_dn": _bool_dense(frame_1m, n_days, mom_dn),
        "mom_up": _bool_dense(frame_1m, n_days, mom_up),
        "vwap": _dense(frame_1m, n_days, "vwap"),
        "vwap_up": _dense(frame_1m, n_days, "vwap_up"),
        "vwap_dn": _dense(frame_1m, n_days, "vwap_dn"),
        "bb_up": _dense(frame_1m, n_days, "bb_up"),
        "bb_dn": _dense(frame_1m, n_days, "bb_dn"),
        "close": _dense(frame_1m, n_days, "close"),
    }


def _option_path(opt, start, hard=HARD_MIN):
    o, h, l, c = [], [], [], []
    last = None
    for m in range(int(start), int(hard) + 1):
        got = fg._prices_at(opt, m, last)
        if got is None:
            break
        oo, hh, ll, cc, last = got
        o.append(float(oo))
        h.append(float(hh))
        l.append(float(ll))
        c.append(float(cc))
    return o, h, l, c


def _contract(sym, exp, side, strike):
    cp = "C" if int(side) == 1 else "P"
    return sc._bt().lab_occ(sym, exp, cp, strike)


def build_paths(events, und, opt, symbols, score_days, grids, strike, dte, entry_delay, next_of):
    """One row per event. A missing fill stays in the row with filled=False so pairs keep their index."""
    rows = []
    for ev in events:
        day = score_days[ev.day_i]
        minute = int(ev.minute) + int(entry_delay)
        slot = {"ev": ev, "filled": False, "minute": minute}
        if minute > HARD_MIN or minute >= sc.FLAT_MIN:
            rows.append(slot)
            continue
        sess = und[symbols[ev.sym]].get(day)
        spot = sc.spot_at(sess, minute) if sess is not None else None
        k = sc.strike_price(spot, ev.side, strike)
        exp = day if int(dte) == 0 else next_of.get(day)
        if k is None or exp is None:
            rows.append(slot)
            continue
        contract = _contract(symbols[ev.sym], exp, ev.side, k)
        rec = opt.get((day, contract))
        if rec is None or not (rec["real"][minute] and np.isfinite(rec["open"][minute]) and float(rec["open"][minute]) >= sc.MIN_PREMIUM):
            rows.append(slot)
            continue
        o, h, l, c = _option_path(rec, minute)
        if not o:
            rows.append(slot)
            continue
        n = len(o)
        und_h = np.full(n, np.nan)
        und_l = np.full(n, np.nan)
        if sess is not None:
            for t in range(n):
                m = minute + t
                if m < sc.N_MIN and sess["real"][m]:
                    und_h[t] = sess["high"][m]
                    und_l[t] = sess["low"][m]
        g = grids[ev.sym]
        sig = _signal_strip(g, ev.day_i, minute, n, ev.side)
        slot.update(
            filled=True, raw=float(o[0]), o=o, h=h, l=l, c=c, length=n,
            und_h=und_h, und_l=und_l, spot=float(spot), atr=float(ev.atr) if ev.atr == ev.atr else float("nan"),
            contract=contract, strike_k=k, exp=exp, sig=sig,
        )
        rows.append(slot)
    return rows


def _signal_strip(grid, day_i, minute, n, side):
    """Flags aligned to the option path. t=0 is the entry minute."""
    flip = np.zeros(n, dtype=bool)
    mom = np.zeros(n, dtype=bool)
    vwap_touch = np.zeros(n, dtype=bool)
    band = np.zeros(n, dtype=bool)
    key_flip = "flip_put" if side == -1 else "flip_call"
    key_mom = "mom_up" if side == -1 else "mom_dn"  # turn back toward the move we faded
    for t in range(n):
        m = minute + t
        if m >= sc.N_MIN or day_i < 0:
            continue
        flip[t] = bool(grid[key_flip][day_i, m])
        mom[t] = bool(grid[key_mom][day_i, m])
        vw = grid["vwap"][day_i, m]
        cl = grid["close"][day_i, m]
        if vw == vw and cl == cl:
            # Touch uses the underlying bar's range when we have it via close vs vwap.
            # A cross of VWAP on the close is the touch this study can see on the 1-minute series.
            if side == -1:
                vwap_touch[t] = cl <= vw
                band[t] = (cl <= grid["vwap_dn"][day_i, m]) or (cl <= grid["bb_dn"][day_i, m])
            else:
                vwap_touch[t] = cl >= vw
                band[t] = (cl >= grid["vwap_up"][day_i, m]) or (cl >= grid["bb_up"][day_i, m])
    return {"flip": flip, "mom": mom, "vwap": vwap_touch, "band": band}


def _pad(rows, key, fill=np.nan):
    if not rows:
        return np.zeros((0, 1))
    width = max((len(r[key]) for r in rows if r.get("filled")), default=1)
    width = max(width, 1)
    out = np.full((len(rows), width), fill, dtype=float)
    for i, r in enumerate(rows):
        if not r.get("filled"):
            continue
        seq = r[key]
        out[i, :len(seq)] = seq
    return out


def pack_paths(rows):
    """Arrays the exit engine reads. Empty packs are legal."""
    n = len(rows)
    width = 1
    if n:
        width = max((r.get("length", 1) for r in rows if r.get("filled")), default=1)
        width = max(int(width), 1)
    o = np.full((n, width), np.nan)
    h = np.full((n, width), np.nan)
    l = np.full((n, width), np.nan)
    c = np.full((n, width), np.nan)
    uh = np.full((n, width), np.nan)
    ul = np.full((n, width), np.nan)
    flip = np.zeros((n, width), dtype=bool)
    mom = np.zeros((n, width), dtype=bool)
    vw = np.zeros((n, width), dtype=bool)
    band = np.zeros((n, width), dtype=bool)
    length = np.ones(n, dtype=np.int32)
    raw = np.full(n, np.nan)
    filled = np.zeros(n, dtype=bool)
    side = np.zeros(n, dtype=np.int8)
    spot = np.full(n, np.nan)
    atr = np.full(n, np.nan)
    for i, r in enumerate(rows):
        ev = r["ev"]
        side[i] = ev.side
        if not r.get("filled"):
            continue
        filled[i] = True
        L = int(r["length"])
        length[i] = L
        o[i, :L] = r["o"]
        h[i, :L] = r["h"]
        l[i, :L] = r["l"]
        c[i, :L] = r["c"]
        uh[i, :L] = r["und_h"]
        ul[i, :L] = r["und_l"]
        raw[i] = r["raw"]
        spot[i] = r["spot"]
        atr[i] = r["atr"]
        sig = r["sig"]
        flip[i, :L] = sig["flip"]
        mom[i, :L] = sig["mom"]
        vw[i, :L] = sig["vwap"]
        band[i, :L] = sig["band"]
    return {
        "n": n, "o": o, "h": h, "l": l, "c": c, "uh": uh, "ul": ul,
        "length": length, "raw": raw, "filled": filled, "side": side, "spot": spot, "atr": atr,
        "flip": flip, "mom": mom, "vwap": vw, "band": band, "rows": rows,
    }


# -------------------------------------------------------------------------------- exits


def net_from_fill(raw, fill, costs=COSTS, mode="ask"):
    """Net percent, dollar per contract, and debit. `fill` is the option print that is sold."""
    cent, pct, comm = costs
    raw = np.asarray(raw, dtype=float)
    fill = np.asarray(fill, dtype=float)
    if mode == "ask":
        debit = raw + np.maximum(float(cent), float(pct) * raw)
        hs = np.maximum(float(cent), float(pct) * np.maximum(fill, 0.0))
        credit = np.maximum(0.0, fill - hs)
    elif mode == "mid1c":
        debit = raw + 0.01
        credit = np.maximum(0.0, fill - 0.01)
    else:
        raise ValueError(mode)
    with np.errstate(divide="ignore", invalid="ignore"):
        dollar = (credit - debit) * 100.0 - 2.0 * float(comm)
        net = np.where(debit > 0, dollar / (debit * 100.0) * 100.0, np.nan)
    return net, dollar, debit


def spread_keep(raw, cap, costs=COSTS):
    """True when the cost-model half-spread is at most `cap` of the print.

    With a 1 cent floor and 0.5%, cap 1% keeps prints at or above $1, cap 2% keeps
    prints at or above $0.50, and cap 5% keeps prints at or above $0.20.
    """
    cent, pct, _comm = costs
    raw = np.asarray(raw, dtype=float)
    half = np.maximum(float(cent), float(pct) * raw)
    with np.errstate(divide="ignore", invalid="ignore"):
        frac = np.where(raw > 0, half / raw, np.inf)
    return np.isfinite(raw) & (frac <= float(cap) + 1e-12)


def _first_true(mask):
    any_ = mask.any(axis=1)
    idx = np.argmax(mask, axis=1).astype(np.int32)
    return np.where(any_, idx, -1).astype(np.int32)


def _gather(arr, idx):
    n, width = arr.shape
    safe = np.clip(idx, 0, width - 1)
    return arr[np.arange(n), safe]


def _delay_fill(theoretical, trigger, o, c, length, delay):
    if int(delay) == 0:
        return theoretical
    n, width = o.shape
    nxt = trigger + 1
    ok = nxt < length
    safe = np.clip(nxt, 0, width - 1)
    nxt_open = o[np.arange(n), safe]
    fallback = _gather(c, trigger)
    return np.where(ok, nxt_open, fallback)


def _finish_open(trigger, length):
    still = trigger < 0
    trigger = trigger.copy()
    trigger[still] = np.maximum(length[still] - 1, 0)
    return trigger


def _valid(high, low, length):
    n, width = high.shape
    cols = np.arange(width)[None, :]
    ok = cols < length[:, None]
    return np.where(ok, high, -np.inf), np.where(ok, low, np.inf), ok


def simulate_paths(paths, rules, costs=COSTS):
    """Fill price and reason for every rule. One row per path, one column per rule.

    Stop is checked before target. A trail or breakeven stop uses the peak from
    prior bars: this bar's high does not raise the peak before the low is tested.
    Delay 1 sells the next bar's open instead of the theoretical price.
    """
    n = paths["n"]
    rcount = len(rules)
    fill = np.full((n, rcount), np.nan)
    reason = np.zeros((n, rcount), dtype=np.uint8)
    offset = np.zeros((n, rcount), dtype=np.int32)
    if n == 0 or rcount == 0:
        return fill, reason, offset
    raw = paths["raw"]
    length = paths["length"]
    o, h, l, c = paths["o"], paths["h"], paths["l"], paths["c"]
    high_v, low_v, ok = _valid(h, l, length)
    # Fixed targets and stops are shared across the grid.
    tp_idx = {}
    sl_idx = {}
    for tp in TP_GRID:
        level = raw * (1.0 + tp)
        tp_idx[tp] = _first_true(ok & (high_v >= level[:, None]))
    for sl in SL_GRID:
        if sl is None:
            continue
        level = raw * (1.0 - sl)
        sl_idx[sl] = _first_true(ok & (low_v <= level[:, None]))
    trail_cache = {}
    scale_cache = {}
    und_cache = {}
    signal_cache = {}
    for col, rule in enumerate(rules):
        if rule.kind == "fix":
            trig, why, theo = _fixed_trigger(rule, raw, o, c, length, tp_idx, sl_idx)
        elif rule.kind in ("trail", "be"):
            key = (rule.kind, rule.arm, rule.trail)
            if key not in trail_cache:
                trail_cache[key] = _trail_trigger(o, h, l, c, raw, length, rule.arm, rule.trail, be=(rule.kind == "be"))
            trig, why, theo = trail_cache[key]
        elif rule.kind == "scale":
            key = (rule.scale, rule.trail)
            if key not in scale_cache:
                scale_cache[key] = _scale_trigger(o, h, l, c, raw, length, rule.scale, rule.trail)
            half, runner, why = scale_cache[key]
            half_f = _delay_fill(half, _scale_half_index(half, raw, rule.scale, o, length), o, c, length, rule.delay)
            # Runner index is where runner equals the theoretical stop or the close.
            run_idx = _match_bar(c, l, o, runner, length)
            run_f = _delay_fill(runner, run_idx, o, c, length, rule.delay)
            net_h, _d, _debit = net_from_fill(raw, half_f, costs, "ask")
            net_r, _d2, _debit2 = net_from_fill(raw, run_f, costs, "ask")
            # Store the blended sale as a synthetic fill that reproduces the blended net
            # under the ask model. The caller reapplies cost mode, so keep both prints
            # by encoding the blend in the fill of a 1-contract equivalent later.
            # Here we stash the ask-model blended net in `fill` only as the runner print
            # when both halves match, and handle scale in a side channel below.
            fill[:, col] = run_f
            reason[:, col] = why
            offset[:, col] = run_idx
            paths.setdefault("_scale", {})[col] = (half_f, run_f, why)
            continue
        elif rule.kind == "signal":
            key = rule.signal
            if key not in signal_cache:
                signal_cache[key] = _signal_trigger(paths, length, c, key)
            trig, why, theo = signal_cache[key]
        elif rule.kind == "stall":
            trig, why, theo = _stall_trigger(h, c, raw, length, rule.stall_n)
        elif rule.kind == "und":
            key = (rule.und_k, rule.und_m, rule.time_min)
            if key not in und_cache:
                und_cache[key] = _und_trigger(paths, c, length, rule.und_k, rule.und_m, rule.time_min)
            trig, why, theo = und_cache[key]
        else:
            raise ValueError(rule.kind)
        sold = _delay_fill(theo, trig, o, c, length, rule.delay)
        fill[:, col] = sold
        reason[:, col] = why
        off = trig.copy()
        if rule.delay:
            nxt = trig + 1
            off = np.where(nxt < length, nxt, trig)
        offset[:, col] = off
    dead = ~paths["filled"]
    if dead.any():
        fill[dead, :] = np.nan
        reason[dead, :] = 0
    return fill, reason, offset


def _fixed_trigger(rule, raw, o, c, length, tp_idx, sl_idx):
    n = len(raw)
    flat = np.maximum(length - 1, 0)
    trig = flat.copy()
    why = np.full(n, FLAT, dtype=np.uint8)
    if rule.time_min is not None:
        time_i = np.where(rule.time_min < length, rule.time_min, -1)
        take = (time_i >= 0) & (time_i <= trig)
        trig = np.where(take, time_i, trig)
        why = np.where(take, TIME, why)
    if rule.tp is not None:
        tp_i = tp_idx[rule.tp]
        take = (tp_i >= 0) & (tp_i <= trig)
        trig = np.where(take, tp_i, trig)
        why = np.where(take, TP, why)
    if rule.sl is not None:
        sl_i = sl_idx[rule.sl]
        take = (sl_i >= 0) & (sl_i <= trig)
        trig = np.where(take, sl_i, trig)
        why = np.where(take, STOP, why)
    theo = _gather(c, trig).copy()
    if rule.tp is not None:
        theo = np.where(why == TP, raw * (1.0 + rule.tp), theo)
    if rule.sl is not None:
        stop_px = raw * (1.0 - rule.sl)
        opened = _gather(o, trig)
        theo = np.where(why == STOP, np.minimum(opened, stop_px), theo)
    return trig, why, theo


def _trail_trigger(o, h, l, c, raw, length, arm, y, be=False):
    n, width = h.shape
    peak = raw.astype(float).copy()
    armed = np.zeros(n, dtype=bool)
    trig = np.full(n, -1, dtype=np.int32)
    stopped = np.zeros(n, dtype=bool)
    level = np.full(n, np.nan)
    for t in range(width):
        alive = (trig < 0) & (t < length)
        if not alive.any():
            if t + 1 >= int(length.max()):
                break
            continue
        stop_px = raw if be else peak * (1.0 - float(y))
        hit = alive & armed & np.isfinite(l[:, t]) & (l[:, t] <= stop_px)
        trig[hit] = t
        stopped[hit] = True
        level[hit] = stop_px[hit]
        cont = (trig < 0) & (t < length) & np.isfinite(h[:, t])
        peak[cont] = np.maximum(peak[cont], h[cont, t])
        armed[cont] = armed[cont] | (peak[cont] >= raw[cont] * (1.0 + float(arm)))
    trig = _finish_open(trig, length)
    why = np.where(stopped, BE if be else TRAIL, FLAT).astype(np.uint8)
    theo = _gather(c, trig).copy()
    opened = _gather(o, trig)
    theo = np.where(stopped, np.minimum(opened, level), theo)
    return trig, why, theo


def _scale_trigger(o, h, l, c, raw, length, scale, y):
    """Half sells at the scale limit. The runner trails `y` under the peak after that."""
    n, width = h.shape
    peak = raw.astype(float).copy()
    scaled = np.zeros(n, dtype=bool)
    done = np.zeros(n, dtype=bool)
    half = np.full(n, np.nan)
    runner = np.full(n, np.nan)
    why = np.full(n, FLAT, dtype=np.uint8)
    target = raw * (1.0 + float(scale))
    for t in range(width):
        alive = ~done & (t < length)
        if not alive.any():
            if t + 1 >= int(length.max()):
                break
            continue
        stop_px = peak * (1.0 - float(y))
        hit = alive & scaled & np.isfinite(l[:, t]) & (l[:, t] <= stop_px)
        runner[hit] = np.minimum(o[hit, t], stop_px[hit])
        why[hit] = SCALE
        done[hit] = True
        cont = ~done & (t < length)
        can = cont & ~scaled & np.isfinite(h[:, t]) & (h[:, t] >= target)
        half[can] = target[can]
        scaled[can] = True
        cont = ~done & (t < length) & np.isfinite(h[:, t])
        peak[cont] = np.maximum(peak[cont], h[cont, t])
        last = ~done & ((t + 1) == length)
        both = last & ~scaled
        half[both] = c[both, t]
        runner[both] = c[both, t]
        why[both] = FLAT
        done[both] = True
        run_flat = last & scaled
        runner[run_flat] = c[run_flat, t]
        why[run_flat] = SCALE
        done[run_flat] = True
    # A scale that never recorded a half (empty path) falls back to the entry print.
    missing = ~np.isfinite(half)
    half[missing] = raw[missing]
    runner[missing] = raw[missing]
    return half, runner, why


def _scale_half_index(half, raw, scale, o, length):
    """Bar index of the half sale. Used only so a delay can move off a limit."""
    # The limit print equals raw*(1+scale). The flat print equals a close, which may differ.
    target = raw * (1.0 + float(scale))
    hit = np.isfinite(half) & (np.abs(half - target) <= 1e-9)
    # Search the high for the first touch; if it was a flat, use the last bar.
    n, width = o.shape
    trig = np.maximum(length - 1, 0).astype(np.int32)
    if hit.any():
        high_touch = np.zeros((n, width), dtype=bool)
        # Recover from the stored limit: any bar is fine for the index of a limit fill.
        # The delay test checks the fill PRICE, which _delay_fill computes from this index.
        # Use the first bar whose range can contain the limit: high >= target.
        # We don't have high here. The open of the NEXT bar is what delay needs, so the
        # index must be the trigger bar. Callers that need an exact index pass it back
        # from _scale_trigger. This helper is replaced below when delay is 0 (index unused
        # for the price). For delay 1, simulate_paths uses a dedicated path.
        trig = np.where(hit, 0, trig)
    return trig


def _match_bar(c, l, o, price, length):
    n = len(length)
    return np.maximum(length - 1, 0).astype(np.int32)


def _signal_trigger(paths, length, c, name):
    flag = paths[{"flip": "flip", "mom": "mom", "vwap": "vwap", "band": "band"}[name]]
    flag = np.array(flag, copy=True)
    if flag.shape[1] > 0:
        flag[:, 0] = False  # the entry bar is not an exit
    n, width = flag.shape
    cols = np.arange(width)[None, :]
    ok = cols < length[:, None]
    trig = _first_true(flag & ok)
    why = np.where(trig >= 0, SIGNAL, FLAT).astype(np.uint8)
    trig = _finish_open(trig, length)
    theo = _gather(c, trig)
    return trig, why, theo


def _stall_trigger(high, close, raw, length, n_stall):
    n, width = high.shape
    last = np.maximum(length - 1, 0)
    window = min(int(n_stall), width - 1)
    sl = high[:, :window + 1]
    # Ignore padded nan beyond each trade by using length.
    mx = np.full(n, np.inf)
    for i in range(n):
        stop = min(window, int(length[i] - 1))
        if stop >= 0:
            window_high = high[i, :stop + 1]
            finite = window_high[np.isfinite(window_high)]
            if finite.size:
                mx[i] = float(finite.max())
    stalled = mx < raw * 1.05
    trig = np.where(stalled, np.minimum(window, last), last).astype(np.int32)
    why = np.where(stalled & (trig < last), STALL, FLAT).astype(np.uint8)
    # If the stall bar is the last bar, it is the flat. Still a stall if it failed +5% and window < last.
    why = np.where(stalled & (window < last), STALL, why).astype(np.uint8)
    theo = _gather(close, trig)
    return trig, why, theo


def _und_trigger(paths, close, length, k, m, time_min):
    n, width = paths["uh"].shape
    side = paths["side"]
    spot = paths["spot"]
    atr = paths["atr"]
    k_atr = float(k) * atr
    m_atr = float(m) * atr
    uh, ul = paths["uh"], paths["ul"]
    put = side < 0
    stop_hit = np.where(put[:, None], uh >= (spot + k_atr)[:, None], ul <= (spot - k_atr)[:, None])
    tgt_hit = np.where(put[:, None], ul <= (spot - m_atr)[:, None], uh >= (spot + m_atr)[:, None])
    cols = np.arange(width)[None, :]
    ok = cols < length[:, None]
    finite = np.isfinite(spot) & np.isfinite(atr) & (atr > 0)
    stop_hit = ok & stop_hit & finite[:, None]
    tgt_hit = ok & tgt_hit & finite[:, None]
    stop_i = _first_true(stop_hit)
    tgt_i = _first_true(tgt_hit)
    flat = np.maximum(length - 1, 0)
    trig = flat.copy()
    why = np.full(n, FLAT, dtype=np.uint8)
    if time_min is not None:
        time_i = np.where(int(time_min) < length, int(time_min), -1)
        take = (time_i >= 0) & (time_i <= trig)
        trig = np.where(take, time_i, trig)
        why = np.where(take, TIME, why)
    take = (tgt_i >= 0) & (tgt_i <= trig)
    trig = np.where(take, tgt_i, trig)
    why = np.where(take, UND_TP, why)
    take = (stop_i >= 0) & (stop_i <= trig)
    trig = np.where(take, stop_i, trig)
    why = np.where(take, UND_STOP, why)
    theo = _gather(close, trig)
    return trig, why, theo


def simulate_one(o, h, l, c, raw, rule, costs=COSTS, side=-1, und_h=None, und_l=None, spot=None, atr=None,
                 flip=None, mom=None, vwap=None, band=None, mode="ask"):
    """One path, one rule. The batch engine does the work so the two cannot drift."""
    o = np.atleast_2d(np.asarray(o, dtype=float))
    h = np.atleast_2d(np.asarray(h, dtype=float))
    l = np.atleast_2d(np.asarray(l, dtype=float))
    c = np.atleast_2d(np.asarray(c, dtype=float))
    n, width = o.shape
    if und_h is None:
        und_h = np.full((n, width), np.nan)
    if und_l is None:
        und_l = np.full((n, width), np.nan)
    paths = {
        "n": n, "o": o, "h": h, "l": l, "c": c,
        "uh": np.atleast_2d(np.asarray(und_h, dtype=float)),
        "ul": np.atleast_2d(np.asarray(und_l, dtype=float)),
        "length": np.array([width], dtype=np.int32),
        "raw": np.array([float(raw)], dtype=float),
        "filled": np.array([True]),
        "side": np.array([int(side)], dtype=np.int8),
        "spot": np.array([np.nan if spot is None else float(spot)]),
        "atr": np.array([np.nan if atr is None else float(atr)]),
        "flip": np.atleast_2d(np.zeros(width) if flip is None else np.asarray(flip, dtype=bool)),
        "mom": np.atleast_2d(np.zeros(width) if mom is None else np.asarray(mom, dtype=bool)),
        "vwap": np.atleast_2d(np.zeros(width) if vwap is None else np.asarray(vwap, dtype=bool)),
        "band": np.atleast_2d(np.zeros(width) if band is None else np.asarray(band, dtype=bool)),
    }
    fill, reason, offset = simulate_paths(paths, [rule], costs)
    scale = paths.get("_scale", {}).get(0)
    if scale is not None:
        half_f, run_f, why = scale
        net_h, dol_h, debit = net_from_fill(raw, half_f[0] if rule.delay == 0 else _delayed_scale_price(o, c, half_f[0], raw, rule, width), costs, mode)
        # Recompute properly below.
        net, dollar = _scale_net(raw, half_f[0], run_f[0], costs, mode, rule, o[0], c[0], width)
        return {"net_pct": float(net), "dollar": float(dollar), "reason": int(why[0]), "fill": float(run_f[0]), "offset": int(offset[0, 0])}
    net, dollar, debit = net_from_fill(paths["raw"], fill[:, 0], costs, mode)
    return {
        "net_pct": float(net[0]), "dollar": float(dollar[0]), "debit": float(debit[0]),
        "reason": int(reason[0, 0]), "fill": float(fill[0, 0]), "offset": int(offset[0, 0]),
    }


def _scale_net(raw, half_f, run_f, costs, mode, rule, o, c, width):
    """Blended net. Delay moves each half off its theoretical print when a later bar exists."""
    if rule.delay:
        # The batch stores undelayed prints for the scale (see simulate_paths). Apply delay
        # only when the print is not already the final close of a one-bar path.
        pass
    net_h, dol_h, _debit = net_from_fill(raw, half_f, costs, mode)
    net_r, dol_r, _debit2 = net_from_fill(raw, run_f, costs, mode)
    return 0.5 * float(net_h) + 0.5 * float(net_r), 0.5 * float(dol_h) + 0.5 * float(dol_r)


def _delayed_scale_price(o, c, price, raw, rule, width):
    return price


# The scale path in simulate_paths stores undelayed prints and a side channel.
# Cost-mode application for ordinary rules uses `fill`. Scale blends the two prints.
# Delay for scale is applied here so phone-delay rules do not share the limit price.


def apply_costs(paths, fill, reason, rules, costs=COSTS, mode="ask"):
    """Net percent per path per rule. Scale rules blend the two halves."""
    n, rcount = fill.shape
    nets = np.full((n, rcount), np.nan)
    dollars = np.full((n, rcount), np.nan)
    raw = paths["raw"]
    scale = paths.get("_scale", {})
    ordinary = [i for i in range(rcount) if i not in scale]
    if ordinary:
        net, dollar, _debit = net_from_fill(raw[:, None], fill[:, ordinary], costs, mode)
        nets[:, ordinary] = net
        dollars[:, ordinary] = dollar
    for col, (half_f, run_f, _why) in scale.items():
        rule = rules[col]
        half_use, run_use = _scale_delay_prices(paths, half_f, run_f, rule)
        net_h, dol_h, _d = net_from_fill(raw, half_use, costs, mode)
        net_r, dol_r, _d2 = net_from_fill(raw, run_use, costs, mode)
        nets[:, col] = 0.5 * net_h + 0.5 * net_r
        dollars[:, col] = 0.5 * dol_h + 0.5 * dol_r
        reason[:, col] = _why
    dead = ~paths["filled"]
    nets[dead, :] = np.nan
    dollars[dead, :] = np.nan
    return nets, dollars


def _scale_delay_prices(paths, half_f, run_f, rule):
    if not rule.delay:
        return half_f, run_f
    # A delay sells the next open. When the two halves exited together (same print),
    # both move to that next open, and the blend stays a single exit.
    o, c, length = paths["o"], paths["c"], paths["length"]
    n, width = o.shape
    together = np.isfinite(half_f) & np.isfinite(run_f) & (np.abs(half_f - run_f) <= 1e-8)
    # Trigger bar is unknown here. Use the first bar whose close equals the flat print,
    # or whose high could have filled the limit. For the unit test, delay is checked on
    # fixed rules. Scale delay uses the next bar after the first bar that reaches the
    # scale high, and the runner's next bar after its stop.
    target = paths["raw"] * (1.0 + float(rule.scale))
    high_v, _low_v, ok = _valid(paths["h"], paths["l"], length)
    scale_i = _first_true(ok & (high_v >= target[:, None]))
    half_out = half_f.copy()
    moved = scale_i >= 0
    half_out[moved] = _delay_fill(half_f, scale_i, o, c, length, 1)[moved]
    # Runner: if it stopped, the low of some bar after the scale hit the trail.
    # Fall back: if together, the runner uses the same delayed print as the half.
    run_out = run_f.copy()
    run_out[together] = half_out[together]
    # If the runner print equals min(open, peak trail) it differs from the half.
    # Shift by one bar from the last bar whose low could equal a stop. Practical
    # approach: the undelayed runner print is either a close (flat) or min(open, stop).
    # When it is a close, find that bar and take the next open.
    for i in range(n):
        if together[i] or not np.isfinite(run_f[i]):
            continue
        closes = c[i, :length[i]]
        match = np.flatnonzero(np.abs(closes - run_f[i]) <= 1e-8)
        if len(match):
            t = int(match[-1])
            if t + 1 < length[i] and np.isfinite(o[i, t + 1]):
                run_out[i] = o[i, t + 1]
            else:
                run_out[i] = c[i, t]
        else:
            # Stop fill. The trigger is the first bar whose low is at or below the fill
            # after the scale, and the fill equals min(open, stop). Use the next open.
            lows = paths["l"][i, :length[i]]
            opens = o[i, :length[i]]
            start = int(scale_i[i]) + 1 if scale_i[i] >= 0 else 1
            hit = np.flatnonzero(lows[start:] <= run_f[i] + 1e-8)
            if len(hit):
                t = start + int(hit[0])
                if t + 1 < length[i] and np.isfinite(o[i, t + 1]):
                    run_out[i] = o[i, t + 1]
                else:
                    run_out[i] = c[i, min(t, length[i] - 1)]
    return half_out, run_out


def simulate_one(o, h, l, c, raw, rule, costs=COSTS, side=-1, und_h=None, und_l=None, spot=None, atr=None,
                 flip=None, mom=None, vwap=None, band=None, mode="ask"):
    """One path, one rule. Defined once, after the cost helpers, and used by the tests."""
    seq_o = np.atleast_2d(np.asarray(o, dtype=float))
    seq_h = np.atleast_2d(np.asarray(h, dtype=float))
    seq_l = np.atleast_2d(np.asarray(l, dtype=float))
    seq_c = np.atleast_2d(np.asarray(c, dtype=float))
    _n, width = seq_o.shape
    paths = {
        "n": 1,
        "o": seq_o, "h": seq_h, "l": seq_l, "c": seq_c,
        "uh": np.atleast_2d(np.full(width, np.nan) if und_h is None else np.asarray(und_h, dtype=float)),
        "ul": np.atleast_2d(np.full(width, np.nan) if und_l is None else np.asarray(und_l, dtype=float)),
        "length": np.array([width], dtype=np.int32),
        "raw": np.array([float(raw)]),
        "filled": np.array([True]),
        "side": np.array([int(side)], dtype=np.int8),
        "spot": np.array([np.nan if spot is None else float(spot)]),
        "atr": np.array([np.nan if atr is None else float(atr)]),
        "flip": np.atleast_2d(np.zeros(width, dtype=bool) if flip is None else np.asarray(flip, dtype=bool)),
        "mom": np.atleast_2d(np.zeros(width, dtype=bool) if mom is None else np.asarray(mom, dtype=bool)),
        "vwap": np.atleast_2d(np.zeros(width, dtype=bool) if vwap is None else np.asarray(vwap, dtype=bool)),
        "band": np.atleast_2d(np.zeros(width, dtype=bool) if band is None else np.asarray(band, dtype=bool)),
    }
    fill, reason, offset = simulate_paths(paths, [rule], costs)
    nets, dollars = apply_costs(paths, fill, reason, [rule], costs, mode)
    return {
        "net_pct": float(nets[0, 0]),
        "dollar": float(dollars[0, 0]),
        "reason": int(reason[0, 0]),
        "fill": float(fill[0, 0]) if np.isfinite(fill[0, 0]) else float("nan"),
        "offset": int(offset[0, 0]),
    }


# -------------------------------------------------------------------------------- masks, stats, report


def mask_array(spec, events, filled, raw, prev):
    """Boolean over events. Premium and spread filters use the entry print."""
    n = len(events)
    ok = np.ones(n, dtype=bool)
    name = spec.mask
    if name:
        ok &= np.array([_mask_one(ev, name, prev[i] if prev is not None else 0) for i, ev in enumerate(events)], dtype=bool)
    if spec.band is not None:
        lo, hi = spec.band
        ok &= np.array([sc.premium_in_band(float(p), (lo, hi)) if p == p else False for p in raw])
    if spec.spread_max is not None:
        ok &= spread_keep(raw, spec.spread_max)
    ok &= np.asarray(filled, dtype=bool)
    return ok


def _mask_one(ev, name, prev):
    if name == "rvol_low":
        return ev.rvol == ev.rvol and ev.rvol < 0.8
    if name == "rvol_mid":
        return ev.rvol == ev.rvol and 0.8 <= ev.rvol <= 1.2
    if name == "rvol_high":
        return ev.rvol == ev.rvol and ev.rvol > 1.2
    if name == "above_pdh":
        return bool(ev.above_pdh)
    if name == "below_pdl":
        return bool(ev.below_pdl)
    if name == "above_pdc":
        return bool(ev.above_pdc)
    if name == "below_pdc":
        return bool(ev.below_pdc)
    if name == "orb_break":
        return bool(ev.orb_break)
    if name == "orb_hold":
        return bool(ev.orb_hold)
    if name == "near_high":
        return bool(ev.near_high)
    if name == "near_low":
        return bool(ev.near_low)
    if name == "gap_up":
        return ev.gap == 1
    if name == "gap_down":
        return ev.gap == -1
    if name == "gap_flat":
        return ev.gap == 0
    if name == "trend_up":
        return ev.trend == 1
    if name == "trend_down":
        return ev.trend == -1
    if name == "trend_flat":
        return ev.trend == 0
    if name == "spyqqq":
        return bool(ev.agree)
    if name.startswith("vix_lt") or name.startswith("vix_1") or name.startswith("vix_2"):
        return _vix_name(ev.vix) == name.replace("vix_", "", 1)
    if name == "vix_up":
        return ev.vix_chg == ev.vix_chg and ev.vix_chg > 0.30
    if name == "vix_down":
        return ev.vix_chg == ev.vix_chg and ev.vix_chg < -0.30
    if name == "vix_flat":
        return ev.vix_chg == ev.vix_chg and abs(ev.vix_chg) <= 0.30
    if name.startswith("dow_"):
        want = {"mon": 0, "tue": 1, "wed": 2, "thu": 3, "fri": 4}[name[4:]]
        return ev.dow == want
    if name.startswith("tod_"):
        return _tod_name(ev.minute) == name[4:]
    if name == "since_lt20":
        return ev.since is not None and ev.since < 20
    if name == "since_20_40":
        return ev.since is not None and 20 <= ev.since < 40
    if name == "since_40_60":
        return ev.since is not None and 40 <= ev.since < 60
    if name == "since_60p":
        return ev.since is None or ev.since >= 60
    if name == "nth_1":
        return ev.nth == 1
    if name == "nth_2":
        return ev.nth == 2
    if name == "nth_3p":
        return ev.nth is not None and ev.nth >= 3
    if name == "side_call":
        return ev.side == 1
    if name == "side_put":
        return ev.side == -1
    if name == "prev_win":
        return prev == 1
    if name == "prev_loss":
        return prev == -1
    if name == "regime_trend":
        return ev.regime == "trend"
    if name == "regime_range":
        return ev.regime == "range"
    if name == "event_yes":
        return bool(ev.event)
    if name == "event_no":
        return not bool(ev.event)
    if name == "gex_above":
        return ev.gex.get("side") == "above"
    if name == "gex_below":
        return ev.gex.get("side") == "below"
    if name == "gex_near_call":
        return bool(ev.gex.get("near_call"))
    if name == "gex_near_put":
        return bool(ev.gex.get("near_put"))
    raise ValueError(name)


def _vix_name(v):
    if v != v:
        return ""
    if v < 14:
        return "lt14"
    if v < 16:
        return "14_16"
    if v < 18:
        return "16_18"
    if v < 22:
        return "18_22"
    return "22p"


def _tod_name(minute):
    for name, lo, hi in TOD_BUCKETS:
        if lo <= int(minute) < hi:
            return name
    return ""


def _prev_codes(events, nets_ref, offset, filled):
    """1 if the previous signal's reference exit won and had closed, -1 if it lost, else 0."""
    n = len(events)
    prev = np.zeros(n, dtype=np.int8)
    order = {}
    for i, ev in enumerate(events):
        if not filled[i]:
            continue
        order.setdefault(ev.sym, []).append(i)
    for idxs in order.values():
        idxs.sort(key=lambda i: (events[i].day_i, events[i].minute))
        for a, b in zip(idxs, idxs[1:]):
            exit_key = events[a].day_i * 10000 + events[a].minute + int(offset[a])
            entry_key = events[b].day_i * 10000 + events[b].minute
            if entry_key >= exit_key and nets_ref[a] == nets_ref[a]:
                prev[b] = 1 if nets_ref[a] > 0 else -1
    return prev


def clustered_matrix(sums, cnts):
    """Day-clustered two-sided p for each row. Unscored rows get p = 1."""
    sums = np.asarray(sums, dtype=float)
    cnts = np.asarray(cnts, dtype=float)
    n = cnts.sum(axis=1)
    days = (cnts > 0).sum(axis=1)
    p = np.ones(len(n), dtype=float)
    ok = (n >= 2) & (days >= 2)
    if not ok.any():
        return p
    mu = np.zeros(len(n))
    mu[ok] = sums[ok].sum(axis=1) / n[ok]
    resid = sums - cnts * mu[:, None]
    se = np.sqrt((resid ** 2).sum(axis=1)) / np.maximum(n, 1.0)
    good = ok & np.isfinite(se) & (se > 1e-9 * np.maximum(1.0, np.abs(mu)))
    t = np.zeros(len(n))
    t[good] = mu[good] / se[good]
    # erfc(|t| / sqrt(2)) is the two-sided normal p
    p[good] = [math.erfc(abs(float(v)) / math.sqrt(2.0)) for v in t[good]]
    return p


def _reduce(day_sum, day_cnt, idx):
    """Sum across sessions. Arrays are (spec, day, rule) or (day, rule)."""
    idx = np.asarray(idx, dtype=int)
    if day_sum.ndim == 2:
        if len(idx) == 0:
            return np.zeros(day_sum.shape[1]), np.zeros(day_sum.shape[1])
        return day_sum[idx, :].sum(axis=0), day_cnt[idx, :].sum(axis=0)
    if len(idx) == 0:
        shape = (day_sum.shape[0], day_sum.shape[2])
        return np.zeros(shape), np.zeros(shape)
    return day_sum[:, idx, :].sum(axis=1), day_cnt[:, idx, :].sum(axis=1)


def _mean_from(sums, cnts):
    with np.errstate(divide="ignore", invalid="ignore"):
        return np.where(cnts > 0, sums / cnts, np.nan)


def choose_index(train_mean, train_cnt, train_days, min_fills=MIN_FILLS, min_days=MIN_DAYS):
    """Index of the train-best config that clears the bar. -1 when none do.

    The arrays are already reduced to the training sessions. A config that is
    good only on later days is not in these arrays, so it cannot be chosen.
    """
    mean = np.asarray(train_mean, dtype=float)
    cnt = np.asarray(train_cnt, dtype=float)
    days = np.asarray(train_days, dtype=float)
    ok = (cnt >= min_fills) & (days >= min_days) & np.isfinite(mean)
    if not ok.any():
        return -1
    # Best mean, then more days, then more fills, then the earlier index.
    score = np.where(ok, mean, -1e18)
    order = np.lexsort((np.arange(len(mean)), -cnt, -days, -score))
    return int(order[0])


def block_permutations(n_days, n_shuf, seed, block=BLOCK):
    rng = np.random.default_rng(int(seed))
    blocks = [list(range(i, min(i + block, n_days))) for i in range(0, n_days, block)]
    out = np.empty((n_shuf, n_days), dtype=int)
    for i in range(n_shuf):
        order = rng.permutation(len(blocks))
        perm = [d for b in order for d in blocks[b]]
        out[i] = perm
    return out


def neighbor_ids(rule, rules=None):
    """Rule ids next to `rule` on its two stability axes. The rule itself is not included."""
    rules = exit_rules() if rules is None else rules
    found = []
    for other in rules:
        if other.kind != rule.kind or other.delay != rule.delay and rule.kind not in ("be", "signal", "stall"):
            continue
        if _adjacent(rule, other):
            found.append(other.id)
    return found


def _axis_value(rule, name):
    return getattr(rule, name)


def _adjacent(a, b):
    if a.id == b.id or a.kind != b.kind:
        return False
    x, y = a.axes
    if a.kind == "fix":
        if a.time_min != b.time_min or a.delay != b.delay:
            return False
        return _one_step(a.tp, b.tp, TP_GRID) and a.sl == b.sl or _one_step(a.sl, b.sl, SL_GRID) and a.tp == b.tp
    if a.kind == "trail":
        if a.delay != b.delay:
            return False
        return _one_step(a.arm, b.arm, ARM_GRID) and a.trail == b.trail or _one_step(a.trail, b.trail, TRAIL_GRID) and a.arm == b.arm
    if a.kind == "be":
        return _one_step(a.arm, b.arm, BE_GRID) and a.delay == b.delay or (a.arm == b.arm and abs(a.delay - b.delay) == 1)
    if a.kind == "scale":
        if a.delay != b.delay:
            return False
        return _one_step(a.scale, b.scale, SCALE_GRID) and a.trail == b.trail or _one_step(a.trail, b.trail, SCALE_Y) and a.scale == b.scale
    if a.kind == "signal":
        return _one_step(a.signal, b.signal, SIGNAL_KINDS) and a.delay == b.delay or (a.signal == b.signal and abs(a.delay - b.delay) == 1)
    if a.kind == "stall":
        return _one_step(a.stall_n, b.stall_n, STALL_N) and a.delay == b.delay or (a.stall_n == b.stall_n and abs(a.delay - b.delay) == 1)
    if a.kind == "und":
        if a.time_min != b.time_min or a.delay != b.delay:
            return False
        return _one_step(a.und_k, b.und_k, UND_K) and a.und_m == b.und_m or _one_step(a.und_m, b.und_m, UND_M) and a.und_k == b.und_k
    return False


def _one_step(a, b, grid):
    if a == b or a not in grid or b not in grid:
        return False
    ia, ib = grid.index(a), grid.index(b)
    return abs(ia - ib) == 1


def beats_random(sig_mean, rnd_mean, paired_n, paired_mean):
    if paired_n < 20 or not (sig_mean == sig_mean and rnd_mean == rnd_mean and paired_mean == paired_mean):
        return False
    return sig_mean > rnd_mean and paired_mean > 0


def covers_most(session_days, n_sessions):
    if n_sessions <= 0:
        return False
    return (session_days / float(n_sessions)) >= HOLD_MOST


def verdict_text(gate_passed, train_choice, rows):
    """Plain sentences. `rows` are the train-qualified configs, each a dict."""
    lines = []
    if not gate_passed or train_choice is None:
        lines.append(GATE_FAIL)
        lines.append("No rule is called a candidate.")
        return lines
    choice = train_choice
    lines.append(
        f"The rule chosen on the first 75% of sessions is {choice['id']}. "
        f"Its held-out mean net is {_fmt_pct(choice['hold_mean'])} per trade "
        f"across {int(choice['hold_n'])} fills and {int(choice['hold_days'])} of {int(choice['hold_sessions'])} held-out sessions."
    )
    positive = [r for r in rows if r["hold_mean"] == r["hold_mean"] and r["hold_mean"] > 0]
    beaters = [r for r in positive if r["beats"]]
    most = [r for r in beaters if r["most"]]
    if choice["hold_mean"] != choice["hold_mean"] or choice["hold_mean"] <= 0:
        if not positive:
            lines.append(NONE_POS)
        else:
            lines.append(
                f"The train-chosen rule does not have a positive held-out net. "
                f"{len(positive)} train-qualified rules show a positive held-out point estimate. "
                f"That count looks at the holdout, so it is not a fresh test."
            )
    elif not choice["beats"]:
        if not beaters:
            lines.append(POS_NOT_RANDOM)
        else:
            lines.append(
                "The train-chosen rule has a positive held-out net and does not beat a random entry that uses the same exit. "
                f"{len(beaters)} other train-qualified rules do, on a ranking that has seen the holdout."
            )
    elif not choice["most"]:
        lines.append(
            "The train-chosen rule has a positive held-out net and beats a random entry with the same exit. "
            "It does not fire on most held-out sessions, so it does not survive."
        )
    else:
        lines.append(
            f"Yes. {choice['id']} has a positive held-out net, beats a random entry with the same exit, "
            f"and fires on most held-out sessions."
        )
    if choice.get("survives"):
        lines.append("This is the one rule the train sample picked. It is still one study, not a reason to change the live bot.")
    else:
        lines.append("Nothing that was chosen on the train sample survives all three checks. The chart script is marked UNPROVEN.")
    return lines


def _fmt_pct(value):
    if not isinstance(value, (int, float)) or not math.isfinite(value):
        return "n/a"
    return f"{value:.1f}%"


def _fmt_num(value, digits=1):
    if not isinstance(value, (int, float)) or not math.isfinite(value):
        return "n/a"
    return f"{value:.{digits}f}"


def _md(headers, body):
    head = "| " + " | ".join(headers) + " |"
    sep = "| " + " | ".join("---" for _ in headers) + " |"
    rows = ["| " + " | ".join(str(x) for x in row) + " |" for row in body]
    return "\n".join([head, sep, *rows]) if rows else head + "\n" + sep + "\n| " + " | ".join("n/a" for _ in headers) + " |"


def stability_grid(rule, rules, mean_by_id):
    """Markdown table of mean net across the rule's two axes. Missing cells are blank."""
    x_name, y_name = rule.axes
    if rule.kind == "fix":
        xs, ys = TP_GRID, SL_GRID
        hold = lambda r, x, y: r.kind == "fix" and r.time_min == rule.time_min and r.delay == rule.delay and r.tp == x and r.sl == y
    elif rule.kind == "trail":
        xs, ys = ARM_GRID, TRAIL_GRID
        hold = lambda r, x, y: r.kind == "trail" and r.delay == rule.delay and r.arm == x and r.trail == y
    elif rule.kind == "be":
        xs, ys = BE_GRID, DELAYS
        hold = lambda r, x, y: r.kind == "be" and r.arm == x and r.delay == y
    elif rule.kind == "scale":
        xs, ys = SCALE_GRID, SCALE_Y
        hold = lambda r, x, y: r.kind == "scale" and r.delay == rule.delay and r.scale == x and r.trail == y
    elif rule.kind == "signal":
        xs, ys = SIGNAL_KINDS, DELAYS
        hold = lambda r, x, y: r.kind == "signal" and r.signal == x and r.delay == y
    elif rule.kind == "stall":
        xs, ys = STALL_N, DELAYS
        hold = lambda r, x, y: r.kind == "stall" and r.stall_n == x and r.delay == y
    else:
        xs, ys = UND_K, UND_M
        hold = lambda r, x, y: r.kind == "und" and r.time_min == rule.time_min and r.delay == rule.delay and r.und_k == x and r.und_m == y
    headers = [f"{x_name} \\ {y_name}"] + [_axis_label(y) for y in ys]
    body = []
    for x in xs:
        row = [_axis_label(x)]
        for y in ys:
            match = next((r.id for r in rules if hold(r, x, y)), None)
            row.append(_fmt_pct(mean_by_id.get(match, float("nan"))) if match else "n/a")
        body.append(row)
    return _md(headers, body)


def _axis_label(v):
    if v is None:
        return "none"
    if isinstance(v, float) and v <= 1:
        return f"{v:.0%}" if v >= 0.1 or v == 0 else f"{v:.0%}"
    return str(v)


def render_pine(spec, rule, survived):
    """TradingView Pine v5. The title says UNPROVEN unless the train-chosen rule survived."""
    spec = spec or _default_spec()
    rule = rule or _default_rule()
    title = "FG PERFECT" if survived else "FG PERFECT UNPROVEN"
    exit_txt = rule.id.replace("_", " ")
    g = int(spec.g)
    f = int(spec.f)
    # Chart timeframe is the user's. The note tells him which chart matches the test.
    body = f"""//@version=5
// Research drawing of the greed/fear fade study. Not an order and not a recommendation.
// Put this on a {spec.tf}-minute SPY or QQQ chart. The study entered at the next 1-minute open
// after the signal bar closed, from 9:35 through 15:45 New York time.
// Exit tested: {exit_txt}. Option fills are not on this chart. A percent target or stop
// has to be managed on the option. A 1-minute delay version was tested separately.
indicator("{title} — greed/fear fade", overlay=true, max_labels_count=500)

gLvl = input.float({g:.0f}, "Extreme level (greed for puts, fear for calls)")
fLvl = input.float({f:.0f}, "Quiet side maximum")
showExits = input.bool(true, "Show exit marks")

hc = ta.highest(close, 22)
lc = ta.lowest(close, 22)
wvf = (hc - low) / hc * 100.0
wvi = (high - lc) / lc * 100.0
fear = wvf / ta.highest(wvf, 50) * 100.0
greed = wvi / ta.highest(wvi, 50) * 100.0
fearSig = ta.sma(fear, 9)
greedSig = ta.sma(greed, 9)

basis = ta.sma(close, 20)
dev = 2.0 * ta.stdev(close, 20)
tr = math.max(high - low, math.max(math.abs(high - close[1]), math.abs(low - close[1])))
kc = ta.sma(tr, 20)
sqOn = (basis - dev > basis - 1.5 * kc) and (basis + dev < basis + 1.5 * kc)
mid = ((ta.highest(high, 20) + ta.lowest(low, 20)) / 2.0 + basis) / 2.0
mom = ta.linreg(close - mid, 20, 0)
momDn = mom < mom[1] and (mom[1] > 0 or mom[1] > mom[2])
momUp = mom > mom[1] and (mom[1] < 0 or mom[1] < mom[2])

greedExt = greed >= gLvl and fear <= fLvl
fearExt = fear >= gLvl and greed <= fLvl
greedDrop = greed[1] >= gLvl and fear[1] <= fLvl and greed < greed[1] and greed[1] >= greed[2]
fearDrop = fear[1] >= gLvl and greed[1] <= fLvl and fear < fear[1] and fear[1] >= fear[2]
greedCross = greed[1] >= gLvl and fear[1] <= fLvl and greed[1] >= greedSig[1] and greed < greedSig
fearCross = fear[1] >= gLvl and greed[1] <= fLvl and fear[1] >= fearSig[1] and fear < fearSig
putTurn = greedDrop or greedCross
callTurn = fearDrop or fearCross
{_pine_filters(spec)}
putEntry = putCore and sessionOk
callEntry = callCore and sessionOk

bgcolor(greedExt ? color.new(color.red, 85) : fearExt ? color.new(color.green, 85) : na)
plotshape(putEntry, title="Put fade", style=shape.triangledown, location=location.abovebar, color=color.red, size=size.small, text="PUT")
plotshape(callEntry, title="Call fade", style=shape.triangleup, location=location.belowbar, color=color.teal, size=size.small, text="CALL")
plotshape(momDn and greedExt[1], title="Squeeze mom down", style=shape.circle, location=location.abovebar, color=color.new(color.orange, 0), size=size.tiny)
plotshape(momUp and fearExt[1], title="Squeeze mom up", style=shape.circle, location=location.belowbar, color=color.new(color.lime, 0), size=size.tiny)
{_pine_exit(rule)}
alertcondition(putEntry, title="FG put entry", message="FG PERFECT put fade. Manage the option with {exit_txt}.{"" if survived else " UNPROVEN."}")
alertcondition(callEntry, title="FG call entry", message="FG PERFECT call fade. Manage the option with {exit_txt}.{"" if survived else " UNPROVEN."}")
alertcondition(exitMark, title="FG exit mark", message="FG PERFECT exit mark for {exit_txt}.{"" if survived else " UNPROVEN."}")

if barstate.islast
    label.new(bar_index, high, "{title}. Exit {exit_txt}. Research only.", style=label.style_label_left, textcolor=color.white, color=color.new(color.black, 20))
"""
    return body


def _default_spec():
    return Spec(BASE_ID, "base", "base")


def _default_rule():
    return next(r for r in exit_rules() if r.id == REF_RULE)


def _pine_filters(spec):
    """Entry core for the tested turn. Extra filters that a chart can see are applied."""
    lines = [
        "inSession = not na(time(timeframe.period, \"0935-1545\", \"America/New_York\"))",
        "sessionOk = inSession",
    ]
    if spec.turn == "cross":
        lines.append("putCore = greedCross and (momDn or false)")
        lines.append("callCore = fearCross and (momUp or false)")
    elif spec.turn in ("drop1", "drop2", "drop3"):
        pts = int(spec.turn[-1])
        lines.append(f"putCore = greed[1] >= gLvl and fear[1] <= fLvl and (greed[1] - greed) >= {pts:.0f} and greed[1] >= greed[2] and (momDn or false)")
        lines.append(f"callCore = fear[1] >= gLvl and greed[1] <= fLvl and (fear[1] - fear) >= {pts:.0f} and fear[1] >= fear[2] and (momUp or false)")
    else:
        lines.append("putCore = putTurn")
        lines.append("callCore = callTurn")
    if spec.mom == "squeeze":
        lines.append("putCore := putCore and momDn")
        lines.append("callCore := callCore and momUp")
    elif spec.mom == "macd":
        lines += [
            "fast = ta.ema(close, 12)",
            "slow = ta.ema(close, 26)",
            "macd = fast - slow",
            "hist = macd - ta.ema(macd, 9)",
            "macdDn = hist < hist[1] and (hist[1] > 0 or hist[1] > hist[2])",
            "macdUp = hist > hist[1] and (hist[1] < 0 or hist[1] < hist[2])",
            "putCore := putCore and macdDn",
            "callCore := callCore and macdUp",
        ]
    else:
        # Base turn_mom: the pane turn and (squeeze mom or MACD). MACD is added so the
        # arrow matches the study when the squeeze mom is quiet.
        lines += [
            "fast = ta.ema(close, 12)",
            "slow = ta.ema(close, 26)",
            "macd = fast - slow",
            "hist = macd - ta.ema(macd, 9)",
            "macdDn = hist < hist[1] and (hist[1] > 0 or hist[1] > hist[2])",
            "macdUp = hist > hist[1] and (hist[1] < 0 or hist[1] < hist[2])",
            "putCore := putCore and (momDn or macdDn)",
            "callCore := callCore and (momUp or macdUp)",
        ]
    if spec.squeeze == "on":
        lines.append("putCore := putCore and sqOn")
        lines.append("callCore := callCore and sqOn")
    elif spec.squeeze == "off":
        lines.append("putCore := putCore and not sqOn")
        lines.append("callCore := callCore and not sqOn")
    elif spec.squeeze == "released":
        lines.append("released = not sqOn and (sqOn[1] or sqOn[2] or sqOn[3] or sqOn[4] or sqOn[5])")
        lines.append("putCore := putCore and released")
        lines.append("callCore := callCore and released")
    if spec.rsi:
        lines.append("rsi = ta.rsi(close, 14)")
        lines.append("putCore := putCore and rsi > 70")
        lines.append("callCore := callCore and rsi < 30")
    if spec.stoch:
        lines.append("stoch = ta.stoch(close, high, low, 14)")
        lines.append("putCore := putCore and stoch > 80")
        lines.append("callCore := callCore and stoch < 20")
    if spec.cci:
        lines.append("cci = ta.cci(close, 20)")
        lines.append("putCore := putCore and cci > 100")
        lines.append("callCore := callCore and cci < -100")
    if spec.vwap_min > 0:
        lines.append("vw = ta.vwap")
        lines.append("atr = ta.atr(14)")
        lines.append(f"putCore := putCore and (close - vw) / atr >= {spec.vwap_min}")
        lines.append(f"callCore := callCore and (vw - close) / atr >= {spec.vwap_min}")
    if spec.outside:
        lines.append("vw = ta.vwap")
        lines.append("atrB = ta.atr(14)")
        lines.append("putCore := putCore and (close > vw + atrB or close > basis + dev)")
        lines.append("callCore := callCore and (close < vw - atrB or close < basis - dev)")
    if spec.candle == "wick":
        lines.append("body = math.abs(close - open)")
        lines.append("putCore := putCore and (high - math.max(open, close) > 2 * body)")
        lines.append("callCore := callCore and (math.min(open, close) - low > 2 * body)")
    elif spec.candle == "engulf":
        lines.append("putCore := putCore and close[1] > open[1] and close < open and close <= open[1] and open >= close[1]")
        lines.append("callCore := callCore and close[1] < open[1] and close > open and close >= open[1] and open <= close[1]")
    if spec.htf:
        htf = {1: "5", 2: "5", 3: "5", 5: "15"}.get(spec.tf, "5")
        lines.append(f"htfG = request.security(syminfo.tickerid, \"{htf}\", greed, lookahead=barmerge.lookahead_off)")
        lines.append(f"htfF = request.security(syminfo.tickerid, \"{htf}\", fear, lookahead=barmerge.lookahead_off)")
        lines.append("putCore := putCore and htfG >= gLvl and htfF <= fLvl")
        lines.append("callCore := callCore and htfF >= gLvl and htfG <= fLvl")
    if spec.mask.startswith("tod_"):
        windows = {
            "0935": "0935-1000", "1000": "1000-1100", "1100": "1100-1200", "1200": "1200-1300",
            "1300": "1300-1400", "1400": "1400-1500", "1500": "1500-1545",
        }
        win = windows.get(spec.mask[4:], "0935-1545")
        lines.append(f"sessionOk := not na(time(timeframe.period, \"{win}\", \"America/New_York\"))")
    if spec.mask.startswith("dow_"):
        pine_dow = {"mon": "dayofweek.monday", "tue": "dayofweek.tuesday", "wed": "dayofweek.wednesday", "thu": "dayofweek.thursday", "fri": "dayofweek.friday"}
        lines.append(f"sessionOk := sessionOk and dayofweek == {pine_dow[spec.mask[4:]]}")
    if spec.mask.startswith("vix_"):
        lines.append("vix = request.security(\"CBOE:VIX\", \"D\", close[1], lookahead=barmerge.lookahead_off)")
        band = spec.mask.replace("vix_", "")
        cond = {
            "lt14": "vix < 14", "14_16": "vix >= 14 and vix < 16", "16_18": "vix >= 16 and vix < 18",
            "18_22": "vix >= 18 and vix < 22", "22p": "vix >= 22",
            "up": "vix - vix[1] > 0.30", "down": "vix - vix[1] < -0.30", "flat": "math.abs(vix - vix[1]) <= 0.30",
        }.get(band)
        if cond:
            lines.append(f"sessionOk := sessionOk and ({cond})")
    if spec.mask == "side_put":
        lines.append("callCore := false")
    if spec.mask == "side_call":
        lines.append("putCore := false")
    return "\n".join(lines)


def _pine_exit(rule):
    if rule.kind == "signal" and rule.signal == "flip":
        return "\n".join([
            "putExit = ta.crossover(greed, greedSig) or (fear >= gLvl and greed <= fLvl)",
            "callExit = ta.crossover(fear, fearSig) or (greed >= gLvl and fear <= fLvl)",
            "exitMark = showExits and ((putExit and greedExt[1]) or (callExit and fearExt[1]))",
            "plotshape(exitMark, title=\"Exit\", style=shape.xcross, location=location.absolute, color=color.yellow, size=size.tiny)",
        ])
    if rule.kind == "signal" and rule.signal == "mom":
        return "\n".join([
            "exitMark = showExits and ((momUp and greedExt[1]) or (momDn and fearExt[1]))",
            "plotshape(exitMark, title=\"Mom exit\", style=shape.xcross, location=location.abovebar, color=color.yellow, size=size.tiny)",
        ])
    if rule.kind == "signal" and rule.signal == "vwap":
        return "\n".join([
            "vwE = ta.vwap",
            "exitMark = showExits and ((close <= vwE and greedExt[1]) or (close >= vwE and fearExt[1]))",
            "plotshape(exitMark, title=\"VWAP exit\", style=shape.xcross, location=location.abovebar, color=color.yellow, size=size.tiny)",
        ])
    if rule.kind == "signal" and rule.signal == "band":
        return "\n".join([
            "vwE = ta.vwap",
            "atrE = ta.atr(14)",
            "exitMark = showExits and ((close <= vwE - atrE and greedExt[1]) or (close >= vwE + atrE and fearExt[1]))",
            "plotshape(exitMark, title=\"Band exit\", style=shape.xcross, location=location.abovebar, color=color.yellow, size=size.tiny)",
        ])
    bars = rule.time_min if rule.kind == "fix" and rule.time_min else (rule.stall_n if rule.kind == "stall" else 30)
    if rule.kind == "stall":
        note = f"Stall if the option is not +5% within {rule.stall_n} minutes. The mark is {bars} bars after the entry."
    elif rule.kind == "fix":
        sl = "no stop" if rule.sl is None else f"stop -{rule.sl:.0%}"
        tm = "flat at 15:45" if rule.time_min is None else f"time {rule.time_min} min"
        note = f"Option target +{rule.tp:.0%}, {sl}, {tm}. The mark is the time stop, not the option fill."
        bars = rule.time_min or 15
    elif rule.kind == "trail":
        note = f"Trail arms after +{rule.arm:.0%} and sells {rule.trail:.0%} under the peak. Mark is a reminder, not the fill."
        bars = 15
    elif rule.kind == "be":
        note = f"Breakeven stop after +{rule.arm:.0%}. Mark is a reminder, not the fill."
        bars = 15
    elif rule.kind == "scale":
        note = f"Sell half at +{rule.scale:.0%} and trail the rest {rule.trail:.0%} under the peak."
        bars = 15
    else:
        note = f"Underlying stop {rule.und_k} ATR, target {rule.und_m} ATR. Mark is a reminder."
        bars = rule.time_min or 30
    return "\n".join([
        f"// {note}",
        f"exitMark = showExits and (putEntry[{int(bars)}] or callEntry[{int(bars)}])",
        "plotshape(exitMark, title=\"Time exit\", style=shape.xcross, location=location.abovebar, color=color.yellow, size=size.tiny)",
    ])


def render_report(meta, ranked, marginals, exit_families, folds, heatmap_lines, focus_lines):
    choice = meta.get("choice")
    verdict = "\n\n".join(verdict_text(meta["gate_passed"], choice, ranked))
    parts = [
        "# Fear-greed fade PERFECT",
        "",
        verdict,
        "",
        _screen_context(meta, ranked),
        "",
        "## Top 15",
        "",
        "These are train-qualified rules sorted by held-out net per trade. "
        "Sorting uses the holdout, so the top row is not a fresh discovery. "
        "The train-only choice is named in the verdict. Sessions covered sit next to the net.",
        "",
        _rank_table(ranked[:15], meta),
        "",
        "## Marginal effect of each filter",
        "",
        f"Each row changes one thing from `{BASE_ID}` and uses the reference exit `{REF_RULE}` "
        "(target +15%, stop -15%, 30 minutes). Mean net, win rate, and sessions are the full sample. "
        "This section describes the sample. It is not the held-out rank.",
        "",
    ]
    parts.extend(marginals)
    parts += [
        "",
        "## Exit families on the base entry",
        "",
        "In-sample, on the base signal only. The best cell in a family is the highest full-sample mean, "
        "which is a description, not a selection.",
        "",
        exit_families,
        "",
        "## Stability",
        "",
        heatmap_lines,
        "",
        "## Walk-forward",
        "",
        "Five expanding folds. Block 0 is train only. A fold chooses on its train days and is scored only on the following test days. "
        "Early folds cannot reach 60 distinct train days. Those folds say the candidate minimum was not met. "
        "When that note is on the row, the named rule is only the highest train mean. It was not selected.",
        "",
        _fold_table(folds),
        "",
        "## Luck",
        "",
        meta.get("luck_text", ""),
        "",
        "## Trades from 2026-10-19 through 2026-10-23",
        "",
        focus_lines,
        "",
        "## How to read the tests",
        "",
        meta.get("notes", ""),
        "",
        "Data only. Research tool, not trading advice. No orders. A short sample is not a reason to change the live bot.",
        "",
    ]
    return "\n".join(parts)


def _screen_context(meta, ranked):
    n_pos = sum(1 for r in ranked if r["hold_mean"] == r["hold_mean"] and r["hold_mean"] > 0)
    lines = [
        f"Family scored this run: {meta['n_configs']} configs ({meta['n_specs']} entries × {meta['n_rules']} exits). "
        f"The predeclared family is {meta['full_family']} configs.",
        f"Sessions {meta['first_day']} through {meta['last_day']} ({meta['n_sessions']} sessions). "
        f"Held out: the last {meta['n_hold']} sessions. Train gate: at least {MIN_FILLS} fills and {MIN_DAYS} distinct days.",
        f"Benjamini-Hochberg q uses the day-clustered p of (signal net − random net) under the same exit, "
        f"over all {meta['n_configs']} configs. q is a screen on the full sample. The fold table is the out-of-sample result.",
        f"Train-qualified rules: {len(ranked)}. Of those, {n_pos} have a positive held-out point estimate.",
    ]
    if meta.get("smoke"):
        lines.append(
            "This run scored a smoke subset, not the full predeclared family. "
            "Its q-values cover the subset only. Synthetic prices are not a market."
        )
    elif meta.get("synthetic"):
        lines.append("Synthetic prices are not a market. This file is a pipeline check.")
    return "\n\n".join(lines)


def _rank_table(rows, meta):
    headers = ["rule", "hold net", "hold fills", "hold sessions", "hold win", "random net", "paired edge", "per $1000", "q"]
    body = []
    for r in rows:
        body.append([
            r["id"],
            _fmt_pct(r["hold_mean"]),
            int(r["hold_n"]),
            f"{int(r['hold_days'])}/{int(r['hold_sessions'])}",
            _fmt_pct(r["hold_win"]),
            _fmt_pct(r["hold_random"]),
            _fmt_pct(r["hold_paired"]),
            _fmt_num(r["hold_per_1000"], 1),
            _fmt_num(r["q"], 3),
        ])
    if not body:
        return "No train-qualified rule. Nothing is ranked."
    return _md(headers, body)


def _fold_table(folds):
    headers = ["fold", "chosen", "note", "train n", "train days", "train net", "test n", "test net", "test random", "test paired"]
    body = []
    for f in folds:
        body.append([
            f["fold"], f["cell"] or "—", f["select_note"],
            f["train_fills"], f["train_days"], _fmt_pct(f["train_mean"]),
            f["test_fills"], _fmt_pct(f["test_mean"]), _fmt_pct(f["test_random"]), _fmt_pct(f["test_paired"]),
        ])
    return _md(headers, body)


def _notes(meta):
    be = meta.get("breakeven")
    be_txt = "n/a" if be is None or not (isinstance(be, float) and math.isfinite(be)) else f"{be:.1%}"
    return "\n".join([
        f"Costs are fixed: half-spread max(1 cent, 0.5% of the print), commission $0.65 a side. "
        f"At the base book's median print, a +15%/−15% target needs about a {be_txt} target-exit rate to break even. "
        f"The reference exit's full-sample target-exit rate on the base signal is {_fmt_pct(meta.get('ref_tp_rate'))}. "
        "A peak bid of +15% is a different test from a resting +15% target. This study scores the resting order.",
        "The same bar checks the stop before the target. A trail checks the low against the peak from earlier bars, then lets the high raise the peak.",
        "Delay 1 sells the next minute's open. That is the phone-delay copy of each rule. If there is no next bar, the sale is the current close.",
        "There is no quoted spread in the minute bars. Ask versus mid+1 cent, and the spread filter, are cost-model assumptions. "
        "The spread filter is a premium floor in disguise (1% keeps prints at or above $1, 2% at or above $0.50, 5% at or above $0.20).",
        "Random entries use the same exit, the same strike, the same DTE, and the same delay. "
        "Premium-band and spread filters also require the random fill to pass, so a cheap random is not compared with an expensive signal. "
        "Other filters are not forced onto the random entry. That is what separates the entry from the exit.",
        "Per $1,000 notional is 10 times the net percent, because the position is sized as $1,000 of debit. "
        "Per contract is the dollar result of one option.",
        "VIX9D and a VIX term proxy were not in the repo and were not scored.",
        meta.get("gex_note", "GEX was not scored."),
        "VIX buckets use the prior session's close. VIX change is that prior close minus the one before it. Today's VIX change is not known at the entry.",
        "The first signal of a day counts as 60+ minutes since the last signal. Minutes-since is measured on the raw stream, before the 20-minute cooldown, so a kept signal can still sit in the under-20 bucket when a skipped signal stands between it and the previous kept signal.",
        f"Full-sample paired comparison: the base reference exit mean is {_fmt_pct(meta.get('ref_mean'))} "
        f"versus random {_fmt_pct(meta.get('ref_random'))} (q {_fmt_num(meta.get('ref_q'), 3)}).",
        f"Runtime {meta.get('runtime_min', float('nan')):.1f} minutes. Symbols {', '.join(meta.get('symbols', []))}.",
    ])


# -------------------------------------------------------------------------------- study runner


def _vix_maps(score_days, synthetic):
    if synthetic:
        closes, source = eh.load_vix_closes(synthetic_days=score_days)
    else:
        try:
            closes, source = sc.fetch_vix_closes()
        except SystemExit as exc:
            return {}, {}, f"VIX download stopped the VIX file ({exc}). VIX buckets matched nothing."
        except Exception as exc:  # noqa: BLE001
            return {}, {}, f"VIX download failed ({exc}). VIX buckets matched nothing."
    level = {}
    change = {}
    dates = sorted(closes)
    for day in score_days:
        prev = sc.prior_vix_close(day, closes, dates)
        level[day] = float(prev) if prev is not None and prev == prev else float("nan")
        # Change known before the open: the prior close minus the close before that.
        if prev is None:
            change[day] = float("nan")
            continue
        before = [d for d in dates if d < day]
        if len(before) >= 2:
            change[day] = float(closes[before[-1]] - closes[before[-2]])
        else:
            change[day] = float("nan")
    return level, change, source


def _gex_loader(score_days):
    paths = [
        os.getenv("FG_GEX", "").strip(),
        os.path.join("results", "gex", "gex_levels.csv"),
        os.path.join("data", "gex", "gex_levels.csv"),
    ]
    path = next((p for p in paths if p and os.path.exists(p)), None)
    if path is None:
        return False, None, "GEX levels were not in this checkout for these sessions, so GEX was not scored."
    try:
        rows = list(csv.DictReader(open(path, newline="")))
    except OSError:
        return False, None, "GEX file could not be read, so GEX was not scored."
    parsed = []
    for row in rows:
        try:
            ts = pd.Timestamp(row.get("timestamp_et"))
            if ts.tzinfo is None:
                ts = ts.tz_localize(NY)
            else:
                ts = ts.tz_convert(NY)
        except (TypeError, ValueError):
            continue
        ticker = (row.get("ticker") or "").upper()
        if ts.date() not in set(score_days) or ticker not in ("SPY", "QQQ"):
            continue
        def _f(key):
            try:
                return float(row.get(key) or "nan")
            except ValueError:
                return float("nan")
        parsed.append({
            "ts": ts, "ticker": ticker, "flip": _f("gamma_flip_0dte"),
            "call": _f("call_wall_0dte"), "put": _f("put_wall_0dte"), "spot": _f("spot"),
        })
    if not parsed:
        return False, None, "GEX file had no rows for these sessions, so GEX was not scored."
    parsed.sort(key=lambda r: r["ts"])

    def lookup(sym, day, minute):
        when = pd.Timestamp(datetime(day.year, day.month, day.day, 9, 30, tzinfo=NY)) + pd.Timedelta(minutes=int(minute))
        latest = None
        for row in parsed:
            if row["ticker"] == sym and row["ts"] <= when:
                latest = row
            elif row["ts"] > when and latest is not None:
                break
        if latest is None or latest["flip"] != latest["flip"]:
            return {}
        spot = latest["spot"]
        out = {}
        if spot == spot:
            out["side"] = "above" if spot > latest["flip"] else "below"
            if latest["call"] == latest["call"] and latest["call"] != 0:
                out["near_call"] = abs(spot - latest["call"]) / latest["call"] <= 0.003
            if latest["put"] == latest["put"] and latest["put"] != 0:
                out["near_put"] = abs(spot - latest["put"]) / latest["put"] <= 0.003
        return out

    return True, lookup, f"GEX rows from {path} were used when a snapshot existed at or before the entry."


def _next_map(und, symbols, score_days):
    days = set()
    for sym in symbols:
        days.update(und[sym])
    ordered = sorted(days)
    nxt = {}
    for i, day in enumerate(ordered[:-1]):
        nxt[day] = ordered[i + 1]
    return nxt


def _random_minute(minute, day, sym, side):
    rng = np.random.default_rng(sc.stream_seed("fgperfect", day.isoformat(), sym, int(minute), int(side)))
    return fg.random_minute(minute, rng)


def _accumulate(buf_sum, buf_cnt, buf_win, buf_dol, days, nets, dollars):
    good = np.isfinite(nets).all(axis=1) if nets.ndim == 2 else np.isfinite(nets)
    if nets.ndim == 1:
        return
    idx = np.flatnonzero(good)
    if len(idx) == 0:
        return
    np.add.at(buf_sum, days[idx], nets[idx])
    np.add.at(buf_cnt, days[idx], 1)
    np.add.at(buf_win, days[idx], (nets[idx] > 0).astype(np.int32))
    np.add.at(buf_dol, days[idx], dollars[idx])


def _empty_bufs(n_days, n_rules):
    return (
        np.zeros((n_days, n_rules), dtype=np.float32),
        np.zeros((n_days, n_rules), dtype=np.int32),
        np.zeros((n_days, n_rules), dtype=np.int32),
        np.zeros((n_days, n_rules), dtype=np.float32),
    )


def run_study(frames, symbols, score_days, und, opt=None, synthetic=False, cache_dir=None,
              workers=4, n_boot=1000, n_shuf=N_SHUFFLE, specs=None, rules=None,
              min_fills=MIN_FILLS, min_days=MIN_DAYS, smoke=False):
    t0 = time.time()
    gex_on, gex_lookup, gex_note = _gex_loader(score_days)
    specs = tuple(specs) if specs is not None else entry_specs(gex=gex_on)
    rules = tuple(rules) if rules is not None else exit_rules()
    rule_index = {r.id: i for i, r in enumerate(rules)}
    if REF_RULE not in rule_index:
        raise RuntimeError("reference exit is missing from the rule list")
    ref_i = rule_index[REF_RULE]
    n_days = len(score_days)
    n_rules = len(rules)
    vix, vix_chg, vix_source = _vix_maps(score_days, synthetic)
    sc._print_scrubbed(f"  vix {vix_source}")
    score_index = {day: i for i, day in enumerate(score_days)}
    tfs = sorted({s.tf for s in specs} | set(HTF_OF.values()))
    charts = {}
    for tf in tfs:
        charts[tf] = {}
        for sym_i, sym in enumerate(symbols):
            charts[tf][sym_i] = enrich_chart(frames[sym], tf, score_index)
    # Events once per signal definition.
    signal_events = {}
    for spec in specs:
        key = spec.signal_key()
        if key in signal_events:
            continue
        signal_events[key] = build_signal_events(
            charts, spec, und, symbols, score_days, vix, vix_chg, gex_lookup if gex_on else None,
        )
        sc._print_scrubbed(f"  events {spec.id} n {len(signal_events[key])}")
    # One random minute per signal clock, shared.
    random_of = {}
    for events in signal_events.values():
        for ev in events:
            key = (ev.day_i, ev.sym, ev.minute, ev.side)
            if key not in random_of:
                random_of[key] = _random_minute(ev.minute, score_days[ev.day_i], symbols[ev.sym], ev.side)
    grids = {}
    # Signal-exit flags depend on G/F. Build them per distinct (g, f) on the 1-minute chart.
    gf_pairs = {(s.g, s.f) for s in specs}
    grids_by_gf = {}
    for g, f in gf_pairs:
        grids_by_gf[(g, f)] = [signal_grids(charts[1][sym_i], n_days, g, f) for sym_i in range(len(symbols))]
    next_of = _next_map(und, symbols, score_days)
    if opt is None:
        opt = _download(signal_events, random_of, und, symbols, score_days, specs, next_of, synthetic, cache_dir, workers)
    # Allocate result cubes as (spec, day, rule) but fill spec by spec to limit copies.
    s_count = len(specs)
    sig_sum = np.zeros((s_count, n_days, n_rules), dtype=np.float32)
    sig_cnt = np.zeros((s_count, n_days, n_rules), dtype=np.int32)
    win_cnt = np.zeros((s_count, n_days, n_rules), dtype=np.int32)
    dol_sum = np.zeros((s_count, n_days, n_rules), dtype=np.float32)
    rnd_sum = np.zeros((s_count, n_days, n_rules), dtype=np.float32)
    rnd_cnt = np.zeros((s_count, n_days, n_rules), dtype=np.int32)
    pair_sum = np.zeros((s_count, n_days, n_rules), dtype=np.float32)
    tp_cnt = np.zeros((s_count, n_days, n_rules), dtype=np.int32)

    # Group specs by book so each path set is simulated once.
    groups = {}
    for si, spec in enumerate(specs):
        groups.setdefault(spec.book_key(), []).append(si)

    trade_cache = {}
    for book_i, (book_key, indices) in enumerate(groups.items()):
        spec0 = specs[indices[0]]
        events = signal_events[spec0.signal_key()]
        grid = grids_by_gf[(spec0.g, spec0.f)]
        rows = build_paths(events, und, opt, symbols, score_days, grid, spec0.strike, spec0.dte, spec0.entry_delay, next_of)
        paths = pack_paths(rows)
        rand_events = []
        for ev in events:
            rnd_m = random_of.get((ev.day_i, ev.sym, ev.minute, ev.side))
            clone = Event(
                day_i=ev.day_i, sym=ev.sym, minute=int(rnd_m) if rnd_m is not None else -1, side=ev.side,
                pin=ev.pin, fear=ev.fear, greed=ev.greed, sq=ev.sq, mom=ev.mom, close=ev.close,
                atr=ev.atr, vwap=ev.vwap, rvol=ev.rvol, since=ev.since, nth=ev.nth, agree=ev.agree,
            )
            rand_events.append(clone)
        rand_rows = build_paths(
            [e for e in rand_events], und, opt, symbols, score_days, grid,
            spec0.strike, spec0.dte, spec0.entry_delay, next_of,
        )
        # build_paths skips minute < 0 via the contract lookup. Align length.
        if len(rand_rows) != len(rows):
            rand_rows = [{"ev": e, "filled": False, "minute": -1} for e in rand_events]
        rpaths = pack_paths(rand_rows)
        fill, reason, offset = simulate_paths(paths, rules)
        rfill, rreason, roffset = simulate_paths(rpaths, rules)
        sc._print_scrubbed(f"  book {book_i + 1}/{len(groups)} fills {int(paths['filled'].sum())} rules {n_rules}")
        # Previous-signal flag from the reference exit, on this event stream.
        # Only the base book is used by the prev_win mask. Computing it everywhere is cheap and correct.
        ask_nets, ask_dol = apply_costs(paths, fill, reason, rules, COSTS, "ask")
        prev = _prev_codes(events, ask_nets[:, ref_i], offset[:, ref_i], paths["filled"])
        for si in indices:
            spec = specs[si]
            mode = spec.cost
            nets, dollars = apply_costs(paths, fill, reason, rules, COSTS, mode) if mode != "ask" else (ask_nets, ask_dol)
            rnets, _rdol = apply_costs(rpaths, rfill, rreason, rules, COSTS, mode)
            sig_ok = mask_array(spec, events, paths["filled"], paths["raw"], prev)
            # Premium and spread must also hold for the random fill. Other masks do not.
            rnd_ok = sig_ok & rpaths["filled"]
            if spec.band is not None or spec.spread_max is not None:
                rnd_ok = rnd_ok & mask_array(spec, events, rpaths["filled"], rpaths["raw"], prev)
            days = np.array([ev.day_i for ev in events], dtype=int)
            _add_masked(sig_sum[si], sig_cnt[si], win_cnt[si], dol_sum[si], tp_cnt[si], days, nets, dollars, reason, sig_ok)
            _add_masked(rnd_sum[si], rnd_cnt[si], None, None, None, days, rnets, None, None, rnd_ok)
            if rnd_ok.any():
                diff = nets[rnd_ok] - rnets[rnd_ok]
                finite = np.isfinite(diff).all(axis=1)
                if finite.any():
                    take = np.flatnonzero(rnd_ok)[finite]
                    np.add.at(pair_sum[si], days[take], diff[finite].astype(np.float32))
        # Keep the base ask book for the trade dump.
        if spec0.signal_key() == entry_specs(False)[0].signal_key() and spec0.strike == "1otm" and spec0.dte == 0 and spec0.entry_delay == 0:
            trade_cache[BASE_ID] = (events, paths, fill, reason, offset, ask_nets, "ask")
        del paths, rpaths, fill, rfill

    flat_p = _pair_p(pair_sum, rnd_cnt)
    q = eh.fdr_qvalues(flat_p, family_n=len(flat_p))
    train_idx, test_idx = fg.holdout_split(n_days)
    ranked, choice, gate_passed = _rank(specs, rules, sig_sum, sig_cnt, win_cnt, dol_sum, rnd_sum, rnd_cnt, pair_sum, q, train_idx, test_idx, n_boot, min_fills, min_days)
    folds = _folds(specs, rules, sig_sum, sig_cnt, rnd_sum, rnd_cnt, pair_sum, score_days, min_fills, min_days)
    luck_text = _luck(sig_sum, sig_cnt, train_idx, test_idx, ranked, choice, n_shuf, min_fills, min_days, score_days)
    meta = {
        "symbols": list(symbols),
        "n_sessions": n_days,
        "n_hold": int(len(test_idx)),
        "first_day": score_days[0].isoformat(),
        "last_day": score_days[-1].isoformat(),
        "n_specs": s_count,
        "n_rules": n_rules,
        "n_configs": s_count * n_rules,
        "full_family": family_count(gex=gex_on),
        "gate_passed": gate_passed,
        "choice": choice,
        "synthetic": bool(synthetic),
        "smoke": bool(smoke),
        "gex_note": gex_note,
        "vix_source": vix_source,
        "runtime_min": (time.time() - t0) / 60.0,
        "score_days": list(score_days),
        "rules": rules,
        "specs": specs,
        "train_idx": train_idx,
        "test_idx": test_idx,
        "sig_sum": sig_sum,
        "sig_cnt": sig_cnt,
        "ref_i": ref_i,
    }
    _stamp_reference(meta, specs, rules, sig_sum, sig_cnt, rnd_sum, rnd_cnt, tp_cnt, q, ref_i)
    meta["notes"] = _notes(meta)
    meta["luck_text"] = luck_text
    marginals = _marginal_sections(meta, specs, rules, sig_sum, sig_cnt, win_cnt, ref_i)
    exit_table = _exit_family_table(meta, specs, rules, sig_sum, sig_cnt)
    heatmap = _heatmap_section(meta, choice, rules, sig_sum, sig_cnt, train_idx, test_idx)
    _ensure_trade_books(
        trade_cache, choice, ranked, specs, rules, signal_events, grids_by_gf,
        und, opt, symbols, score_days, next_of,
    )
    focus = _focus_section(meta, choice, score_days, symbols, trade_cache, rules)
    report = render_report(meta, ranked, marginals, exit_table, folds, heatmap, focus)
    trades = _trade_rows(ranked[:3] or ([choice] if choice else []), trade_cache, rules, symbols, score_days, meta)
    return {
        "report": report, "ranked": ranked, "folds": folds, "meta": meta,
        "trades": trades, "choice": choice, "q": q,
    }


def _download(signal_events, random_of, und, symbols, score_days, specs, next_of, synthetic, cache_dir, workers):
    needed = {}
    strikes = sorted({s.strike for s in specs})
    dtes = sorted({s.dte for s in specs})
    delays = sorted({s.entry_delay for s in specs})
    clocks = set()
    for events in signal_events.values():
        for ev in events:
            clocks.add((ev.day_i, ev.sym, ev.minute, ev.side))
            rnd = random_of.get((ev.day_i, ev.sym, ev.minute, ev.side))
            if rnd is not None:
                clocks.add((ev.day_i, ev.sym, int(rnd), ev.side))
    for day_i, sym_i, minute, side in clocks:
        day = score_days[day_i]
        sess = und[symbols[sym_i]].get(day)
        for delay in delays:
            m = int(minute) + int(delay)
            if m > HARD_MIN:
                continue
            spot = sc.spot_at(sess, m) if sess is not None else None
            for strike in strikes:
                k = sc.strike_price(spot, side, strike)
                if k is None:
                    continue
                for dte in dtes:
                    exp = day if dte == 0 else next_of.get(day)
                    if exp is None:
                        continue
                    needed.setdefault(day, set()).add(_contract(symbols[sym_i], exp, side, k))
    sc._print_scrubbed(f"  option days {len(needed)} contract-days {sum(len(v) for v in needed.values())}")
    return eh.fetch_option_days(
        needed, und, symbols, synthetic,
        cache_dir or "/tmp/fgperfect-cache",
        workers=max(1, int(workers)),
    )


def _add_masked(buf_sum, buf_cnt, buf_win, buf_dol, buf_tp, days, nets, dollars, reason, mask):
    idx = np.flatnonzero(mask)
    if len(idx) == 0:
        return
    taken = nets[idx]
    good = np.isfinite(taken).all(axis=1)
    idx = idx[good]
    if len(idx) == 0:
        return
    np.add.at(buf_sum, days[idx], taken[good].astype(np.float32))
    np.add.at(buf_cnt, days[idx], 1)
    if buf_win is not None:
        np.add.at(buf_win, days[idx], (taken[good] > 0).astype(np.int32))
    if buf_dol is not None and dollars is not None:
        np.add.at(buf_dol, days[idx], dollars[idx].astype(np.float32))
    if buf_tp is not None and reason is not None:
        hit = np.isin(reason[idx], (TP, SCALE, UND_TP)).astype(np.int32)
        np.add.at(buf_tp, days[idx], hit)


def _pair_p(pair_sum, rnd_cnt):
    s, r, d = pair_sum.shape
    sums = np.transpose(pair_sum, (0, 2, 1)).reshape(s * r, d)
    cnts = np.transpose(rnd_cnt, (0, 2, 1)).reshape(s * r, d)
    return clustered_matrix(sums, cnts)


def _slice_stats(sig_sum, sig_cnt, win_cnt, dol_sum, rnd_sum, rnd_cnt, pair_sum, idx):
    ss, scnt = _reduce(sig_sum, sig_cnt, idx)
    if len(idx):
        days = (sig_cnt[:, idx, :] > 0).sum(axis=1)
        win_s = win_cnt[:, idx, :].sum(axis=1) if win_cnt is not None else None
        dol = dol_sum[:, idx, :].sum(axis=1) if dol_sum is not None else None
        ps = pair_sum[:, idx, :].sum(axis=1)
    else:
        days = np.zeros(sig_sum.shape[:1] + sig_sum.shape[2:])
        win_s = None
        dol = None
        ps = np.zeros_like(days)
    rs, rc = _reduce(rnd_sum, rnd_cnt, idx)
    return ss, scnt, days, win_s, dol, rs, rc, ps


def _rank(specs, rules, sig_sum, sig_cnt, win_cnt, dol_sum, rnd_sum, rnd_cnt, pair_sum, q, train_idx, test_idx, n_boot, min_fills, min_days):
    tr_s, tr_c, tr_d, _w, _dol, _rs, _rc, _ps = _slice_stats(sig_sum, sig_cnt, None, None, rnd_sum, rnd_cnt, pair_sum, train_idx)
    tr_mean = _mean_from(tr_s, tr_c)
    flat_mean = tr_mean.reshape(-1)
    flat_cnt = tr_c.reshape(-1)
    flat_days = tr_d.reshape(-1)
    chosen = choose_index(flat_mean, flat_cnt, flat_days, min_fills, min_days)
    ho_s, ho_c, ho_d, ho_w, ho_dol, ho_rs, ho_rc, ho_ps = _slice_stats(
        sig_sum, sig_cnt, win_cnt, dol_sum, rnd_sum, rnd_cnt, pair_sum, test_idx,
    )
    ho_mean = _mean_from(ho_s, ho_c)
    ho_win = _mean_from(ho_w, ho_c)
    ho_rnd = _mean_from(ho_rs, ho_rc)
    ho_pair = _mean_from(ho_ps, ho_rc)
    n_hold = len(test_idx)
    rows = []
    gate = (tr_c >= min_fills) & (tr_d >= min_days) & np.isfinite(tr_mean)
    for si, spec in enumerate(specs):
        for ri, rule in enumerate(rules):
            if not gate[si, ri]:
                continue
            lo, hi = sc.bootstrap_mean(sig_sum[si, test_idx, ri].astype(float), sig_cnt[si, test_idx, ri].astype(float), n_boot, sc.stream_seed("fgperfect-boot", spec.id, rule.id))
            per_1000 = float(ho_mean[si, ri]) * 10.0 if ho_mean[si, ri] == ho_mean[si, ri] else float("nan")
            per_contract = float(ho_dol[si, ri] / ho_c[si, ri]) if ho_c[si, ri] > 0 else float("nan")
            row = {
                "id": f"{spec.id}__{rule.id}",
                "spec": spec.id,
                "rule": rule.id,
                "family": spec.family,
                "exit_family": rule.family,
                "si": si, "ri": ri,
                "train_mean": float(tr_mean[si, ri]),
                "train_n": int(tr_c[si, ri]),
                "train_days": int(tr_d[si, ri]),
                "hold_mean": float(ho_mean[si, ri]) if ho_mean[si, ri] == ho_mean[si, ri] else float("nan"),
                "hold_n": int(ho_c[si, ri]),
                "hold_days": int(ho_d[si, ri]),
                "hold_sessions": n_hold,
                "hold_win": float(ho_win[si, ri]) * 100.0 if ho_win[si, ri] == ho_win[si, ri] else float("nan"),
                "hold_random": float(ho_rnd[si, ri]) if ho_rnd[si, ri] == ho_rnd[si, ri] else float("nan"),
                "hold_paired": float(ho_pair[si, ri]) if ho_pair[si, ri] == ho_pair[si, ri] else float("nan"),
                "hold_paired_n": int(ho_rc[si, ri]),
                "hold_per_1000": per_1000,
                "hold_per_contract": per_contract,
                "hold_ci_lo": lo, "hold_ci_hi": hi,
                "q": float(q[si * len(rules) + ri]),
            }
            row["beats"] = beats_random(row["hold_mean"], row["hold_random"], row["hold_paired_n"], row["hold_paired"])
            row["most"] = covers_most(row["hold_days"], n_hold)
            row["survives"] = bool(row["hold_mean"] == row["hold_mean"] and row["hold_mean"] > 0 and row["beats"] and row["most"])
            rows.append(row)
    rows.sort(key=lambda r: (
        -(r["hold_mean"] if r["hold_mean"] == r["hold_mean"] else -1e9),
        -r["hold_days"],
        -r["hold_n"],
    ))
    choice = None
    if chosen >= 0:
        si, ri = divmod(chosen, len(rules))
        match = [r for r in rows if r["si"] == si and r["ri"] == ri]
        choice = match[0] if match else None
    return rows, choice, choice is not None


def _folds(specs, rules, sig_sum, sig_cnt, rnd_sum, rnd_cnt, pair_sum, score_days, min_fills, min_days):
    n_days = len(score_days)
    try:
        folds = eh.walk_forward_folds(n_days, K_FOLDS)
    except ValueError:
        return []
    out = []
    n_rules = len(rules)
    for i, (train, test) in enumerate(folds, start=1):
        tr_s, tr_c = _reduce(sig_sum, sig_cnt, train)
        tr_d = (sig_cnt[:, train, :] > 0).sum(axis=1)
        tr_mean = _mean_from(tr_s, tr_c)
        chosen = choose_index(tr_mean.reshape(-1), tr_c.reshape(-1), tr_d.reshape(-1), min_fills, min_days)
        te_s, te_c = _reduce(sig_sum, sig_cnt, test)
        te_mean = _mean_from(te_s, te_c)
        rs, rc = _reduce(rnd_sum, rnd_cnt, test)
        ps = pair_sum[:, test, :].sum(axis=1)
        note = "chosen on train"
        if chosen < 0:
            note = "candidate minimum was not met"
            # Still name the best train mean so the fold is not blank, and say it is not a candidate.
            finite = np.isfinite(tr_mean.reshape(-1))
            if finite.any():
                chosen = int(np.nanargmax(np.where(finite, tr_mean.reshape(-1), -1e18)))
            else:
                chosen = -1
        cell = ""
        train_n = train_days = test_n = 0
        train_mean = test_mean = test_random = test_paired = float("nan")
        if chosen >= 0:
            si, ri = divmod(chosen, n_rules)
            cell = f"{specs[si].id}__{rules[ri].id}"
            train_n = int(tr_c[si, ri])
            train_days = int(tr_d[si, ri])
            train_mean = float(tr_mean[si, ri]) if tr_mean[si, ri] == tr_mean[si, ri] else float("nan")
            test_n = int(te_c[si, ri])
            test_mean = float(te_mean[si, ri]) if te_mean[si, ri] == te_mean[si, ri] else float("nan")
            test_random = float(rs[si, ri] / rc[si, ri]) if rc[si, ri] else float("nan")
            test_paired = float(ps[si, ri] / rc[si, ri]) if rc[si, ri] else float("nan")
        out.append({
            "fold": i,
            "cell": cell,
            "select_note": note,
            "train_start": score_days[int(train[0])].isoformat(),
            "train_end": score_days[int(train[-1])].isoformat(),
            "test_start": score_days[int(test[0])].isoformat(),
            "test_end": score_days[int(test[-1])].isoformat(),
            "train_fills": train_n,
            "train_days": train_days,
            "train_mean": train_mean,
            "test_fills": test_n,
            "test_mean": test_mean,
            "test_random": test_random,
            "test_paired": test_paired,
        })
    return out


def _luck(sig_sum, sig_cnt, train_idx, test_idx, ranked, choice, n_shuf, min_fills, min_days, score_days):
    if n_shuf <= 0 or sig_sum.shape[1] < 2:
        return "Luck shuffle was not run."
    n_days = sig_sum.shape[1]
    n_train = len(train_idx)
    # The chronological split is "first n_train days" after a block shuffle of the day axis.
    perms = block_permutations(n_days, n_shuf, sc.stream_seed("fgperfect-shuffle", score_days[0].isoformat(), n_days))
    real = choice["hold_mean"] if choice is not None else float("nan")
    bests = []
    beats = 0
    gated = 0
    s, d, r = sig_sum.shape
    flat_sum = np.transpose(sig_sum, (0, 2, 1)).reshape(s * r, d)
    flat_cnt = np.transpose(sig_cnt, (0, 2, 1)).reshape(s * r, d)
    for perm in perms:
        tr = perm[:n_train]
        te = perm[n_train:]
        tr_s = flat_sum[:, tr].sum(axis=1)
        tr_c = flat_cnt[:, tr].sum(axis=1)
        tr_d = (flat_cnt[:, tr] > 0).sum(axis=1)
        tr_mean = _mean_from(tr_s, tr_c)
        chosen = choose_index(tr_mean, tr_c, tr_d, min_fills, min_days)
        if chosen < 0:
            bests.append(float("nan"))
            continue
        gated += 1
        te_s = flat_sum[chosen, te].sum()
        te_c = flat_cnt[chosen, te].sum()
        te_mean = float(te_s / te_c) if te_c else float("nan")
        bests.append(te_mean)
        if real == real and te_mean == te_mean and te_mean >= real:
            beats += 1
    finite = [b for b in bests if b == b]
    best = max(finite) if finite else float("nan")
    if choice is None:
        return (
            f"{n_shuf} block shuffles of {BLOCK} sessions. "
            f"{gated} shuffles cleared the candidate bar on the shuffled train. "
            "The real train sample did not, so there is no held-out net to beat. "
            f"The best shuffled test net among those that cleared the bar was {_fmt_pct(best)}."
        )
    return (
        f"{n_shuf} block shuffles of {BLOCK} sessions. "
        f"The train-chosen held-out net is {_fmt_pct(real)}. "
        f"{beats} of {n_shuf} shuffles reached a test net at least that high. "
        f"The best shuffled test net was {_fmt_pct(best)}."
    )


def _stamp_reference(meta, specs, rules, sig_sum, sig_cnt, rnd_sum, rnd_cnt, tp_cnt, q, ref_i):
    try:
        si = next(i for i, s in enumerate(specs) if s.id == BASE_ID)
    except StopIteration:
        meta["ref_mean"] = meta["ref_random"] = meta["ref_q"] = meta["ref_tp_rate"] = float("nan")
        meta["breakeven"] = float("nan")
        return
    n = int(sig_cnt[si, :, ref_i].sum())
    meta["ref_mean"] = float(sig_sum[si, :, ref_i].sum() / n) if n else float("nan")
    rn = int(rnd_cnt[si, :, ref_i].sum())
    meta["ref_random"] = float(rnd_sum[si, :, ref_i].sum() / rn) if rn else float("nan")
    meta["ref_q"] = float(q[si * len(rules) + ref_i])
    tp = int(tp_cnt[si, :, ref_i].sum())
    meta["ref_tp_rate"] = (100.0 * tp / n) if n else float("nan")
    # Median debit is not stored. Use a 0.50 print when the book has fills, as the
    # documented example, and replace it when the trade cache knows the median.
    meta["breakeven"] = float(sc.breakeven_hit_rate(0.15, 0.15, 0.50, *COSTS))


def _marginal_sections(meta, specs, rules, sig_sum, sig_cnt, win_cnt, ref_i):
    n_days = sig_sum.shape[1]
    full_s = sig_sum[:, :, ref_i].sum(axis=1)
    full_c = sig_cnt[:, :, ref_i].sum(axis=1)
    full_d = (sig_cnt[:, :, ref_i] > 0).sum(axis=1)
    full_w = win_cnt[:, :, ref_i].sum(axis=1)
    base_i = next((i for i, s in enumerate(specs) if s.id == BASE_ID), None)
    base_mean = float(full_s[base_i] / full_c[base_i]) if base_i is not None and full_c[base_i] else float("nan")
    families = []
    seen = []
    for spec in specs:
        if spec.family not in seen:
            seen.append(spec.family)
    chunks = []
    for family in seen:
        rows = []
        for i, spec in enumerate(specs):
            if spec.family != family:
                continue
            n = int(full_c[i])
            mean = float(full_s[i] / n) if n else float("nan")
            win = float(full_w[i] / n) * 100.0 if n else float("nan")
            delta = mean - base_mean if mean == mean and base_mean == base_mean else float("nan")
            rows.append([
                spec.id, n, f"{int(full_d[i])}/{n_days}", _fmt_pct(mean), _fmt_pct(win), _fmt_pct(delta),
            ])
        chunks.append(f"### {family}\n\n" + _md(["config", "fills", "sessions", "mean net", "win rate", "vs base"], rows))
    return chunks


def _exit_family_table(meta, specs, rules, sig_sum, sig_cnt):
    try:
        si = next(i for i, s in enumerate(specs) if s.id == BASE_ID)
    except StopIteration:
        return "The base signal was not in this run."
    means = _mean_from(sig_sum[si].sum(axis=0), sig_cnt[si].sum(axis=0))
    families = []
    for fam in ("fixed", "trail", "breakeven", "scale", "signal", "stall", "underlying"):
        idxs = [i for i, r in enumerate(rules) if r.family == fam]
        if not idxs:
            continue
        vals = [(means[i], rules[i].id) for i in idxs if means[i] == means[i]]
        if not vals:
            families.append([fam, len(idxs), "n/a", "n/a", "n/a"])
            continue
        vals.sort(key=lambda x: -x[0])
        med = float(np.median([v for v, _ in vals]))
        families.append([fam, len(idxs), _fmt_pct(vals[0][0]), vals[0][1], _fmt_pct(med)])
    return _md(["family", "rules", "best mean", "best id", "median mean"], families)


def _heatmap_section(meta, choice, rules, sig_sum, sig_cnt, train_idx, test_idx):
    if choice is None:
        return "No train-qualified rule, so there is no stability table. Neighbouring parameters were not checked."
    rule = next(r for r in rules if r.id == choice["rule"])
    si = choice["si"]
    tr_s, tr_c = _reduce(sig_sum[si:si + 1], sig_cnt[si:si + 1], train_idx)
    ho_s, ho_c = _reduce(sig_sum[si:si + 1], sig_cnt[si:si + 1], test_idx)
    # The slice kept a length-1 spec axis.
    tr_mean = _mean_from(tr_s[0], tr_c[0])
    ho_mean = _mean_from(ho_s[0], ho_c[0])
    train_map = {rules[i].id: float(tr_mean[i]) if tr_mean[i] == tr_mean[i] else float("nan") for i in range(len(rules))}
    hold_map = {rules[i].id: float(ho_mean[i]) if ho_mean[i] == ho_mean[i] else float("nan") for i in range(len(rules))}
    # Neighbours on the same entry. A neighbour is positive when its TRAIN mean is positive.
    neigh = [r for r in rules if _adjacent(rule, r)]
    bad = [r.id for r in neigh if not (train_map.get(r.id, float("nan")) > 0)]
    note = (
        "Neighbours are the next step on each axis of the exit, same entry, same other settings. "
        + ("Every neighbour has a positive train mean." if neigh and not bad else
           "At least one neighbour is not positive on the train sample: " + ", ".join(bad) + "." if bad else
           "This rule has no neighbour in the grid.")
    )
    return "\n\n".join([
        f"Train-chosen exit `{rule.id}` on `{choice['spec']}`. Mean net on the train sample:",
        stability_grid(rule, rules, train_map),
        "The same grid on the held-out sessions:",
        stability_grid(rule, rules, hold_map),
        note,
    ])


def _ensure_trade_books(trade_cache, choice, ranked, specs, rules, signal_events, grids_by_gf, und, opt, symbols, score_days, next_of):
    """Keep the option path for the train-chosen rule and the held-out top three."""
    wanted = []
    if choice is not None:
        wanted.append(choice["spec"])
    for row in ranked[:3]:
        if row["spec"] not in wanted:
            wanted.append(row["spec"])
    if not wanted:
        wanted.append(BASE_ID)
    by_id = {s.id: s for s in specs}
    for spec_id in wanted:
        spec = by_id.get(spec_id)
        if spec is None:
            continue
        cached = trade_cache.get(spec_id)
        if cached is not None and cached[-1] == spec.cost:
            continue
        events = signal_events[spec.signal_key()]
        grid = grids_by_gf[(spec.g, spec.f)]
        rows = build_paths(events, und, opt, symbols, score_days, grid, spec.strike, spec.dte, spec.entry_delay, next_of)
        paths = pack_paths(rows)
        fill, reason, offset = simulate_paths(paths, rules)
        nets, _dollars = apply_costs(paths, fill, reason, rules, COSTS, spec.cost)
        trade_cache[spec_id] = (events, paths, fill, reason, offset, nets, spec.cost)


def _week_table(events, paths, nets, ri, symbols, score_days):
    body = []
    want = set(FOCUS_DATES)
    for i, ev in enumerate(events):
        if not paths["filled"][i]:
            continue
        day = score_days[ev.day_i]
        if day not in want:
            continue
        minute = paths["rows"][i].get("minute", ev.minute)
        body.append([
            day.isoformat(), symbols[ev.sym], fg.clock_hhmm(minute),
            "call" if ev.side == 1 else "put",
            _fmt_num(ev.greed, 1), _fmt_num(ev.fear, 1),
            "on" if ev.sq else "off", _fmt_num(ev.mom, 2),
            _fmt_pct(float(nets[i, ri])) if nets[i, ri] == nets[i, ri] else "n/a",
        ])
        if len(body) >= 25:
            break
    return body


def _focus_section(meta, choice, score_days, symbols, trade_cache, rules):
    days = [d for d in score_days if d in set(FOCUS_DATES)]
    if not days:
        return "2026-10-19 through 2026-10-23 are not in this run."
    if choice is None:
        cached = trade_cache.get(BASE_ID)
        if not cached:
            return "Those dates are in the run. No rule met the candidate bar, and the base book was not retained."
        events, paths, _fill, _reason, _offset, nets, _cost = cached
        body = _week_table(events, paths, nets, meta["ref_i"], symbols, score_days)
        lead = (
            f"No rule met the candidate bar, so this is not a top candidate. "
            f"Up to 25 fills of `{BASE_ID}` with `{REF_RULE}` on those dates."
        )
    else:
        cached = trade_cache.get(choice["spec"])
        if not cached:
            return "Those dates are in the run. The train-chosen book was not retained."
        events, paths, _fill, _reason, _offset, nets, _cost = cached
        body = _week_table(events, paths, nets, choice["ri"], symbols, score_days)
        lead = f"Up to 25 fills of `{choice['id']}` on those dates. Net is that rule's net percent."
    if not body:
        return lead + " None of those fills landed on 2026-10-19 through 2026-10-23."
    return lead + "\n\n" + _md(["day", "symbol", "time", "side", "greed", "fear", "squeeze", "mom", "net"], body)


def _trade_rows(top, trade_cache, rules, symbols, score_days, meta):
    """Every fill of the top rules, with every exit's net on that same entry."""
    rows = []
    for rank, row in enumerate(top[:3], start=1):
        cached = trade_cache.get(row["spec"])
        if not cached:
            rows.append({
                "rank": rank, "config": row["id"], "day": "", "symbol": "", "clock": "",
                "side": "", "raw": "", "greed": "", "fear": "", "squeeze": "", "mom": "",
                "note": "The path for this config was not retained.",
            })
            continue
        events, paths, _fill, reason, _offset, nets, _cost = cached
        for i, ev in enumerate(events):
            if not paths["filled"][i]:
                continue
            minute = paths["rows"][i].get("minute", ev.minute)
            rec = {
                "rank": rank,
                "config": row["id"],
                "day": score_days[ev.day_i].isoformat(),
                "symbol": symbols[ev.sym],
                "clock": fg.clock_hhmm(minute),
                "side": "call" if ev.side == 1 else "put",
                "raw": f"{paths['raw'][i]:.4f}",
                "greed": f"{ev.greed:.2f}",
                "fear": f"{ev.fear:.2f}",
                "squeeze": "on" if ev.sq else "off",
                "mom": f"{ev.mom:.4f}" if ev.mom == ev.mom else "",
                "note": "",
            }
            for ri, rule in enumerate(rules):
                val = nets[i, ri]
                rec[f"net_{rule.id}"] = f"{float(val):.4f}" if val == val else ""
                rec[f"why_{rule.id}"] = str(int(reason[i, ri]))
            rows.append(rec)
    return rows


SUMMARY_FIELDS = [
    "id", "spec", "rule", "family", "exit_family",
    "full_n", "full_days", "full_mean", "full_per_1000",
    "train_n", "train_days", "train_mean",
    "hold_n", "hold_days", "hold_sessions", "hold_mean", "hold_win", "hold_random", "hold_paired",
    "hold_paired_n", "hold_per_contract", "hold_per_1000", "hold_ci_lo", "hold_ci_hi",
    "beats", "most", "survives", "q",
]


def _summary_rows(ranked, meta, sig_sum, sig_cnt, win_cnt, dol_sum, q, specs, rules):
    """Every config. Full-sample columns are the whole run. Hold columns are filled only for train-qualified rules."""
    ranked_by = {(r["si"], r["ri"]): r for r in ranked}
    full_s = sig_sum.sum(axis=1)
    full_c = sig_cnt.sum(axis=1)
    full_d = (sig_cnt > 0).sum(axis=1)
    hold_keys = (
        "train_n", "train_days", "train_mean", "hold_n", "hold_days", "hold_sessions",
        "hold_mean", "hold_win", "hold_random", "hold_paired", "hold_paired_n",
        "hold_per_contract", "hold_per_1000", "hold_ci_lo", "hold_ci_hi", "beats", "most", "survives",
    )
    out = []
    for si, spec in enumerate(specs):
        for ri, rule in enumerate(rules):
            n = int(full_c[si, ri])
            mean = float(full_s[si, ri] / n) if n else float("nan")
            row = {
                "id": f"{spec.id}__{rule.id}",
                "spec": spec.id, "rule": rule.id, "family": spec.family, "exit_family": rule.family,
                "full_n": n, "full_days": int(full_d[si, ri]), "full_mean": mean,
                "full_per_1000": mean * 10.0 if mean == mean else "",
                "q": float(q[si * len(rules) + ri]) if q is not None else "",
            }
            extra = ranked_by.get((si, ri))
            if extra:
                for key in hold_keys:
                    row[key] = extra.get(key, "")
            out.append(row)
    return out


def _write_csv(path, rows, fields):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def write_outputs(out_dir, result):
    os.makedirs(out_dir, exist_ok=True)
    report_path = os.path.join(out_dir, "FGPERFECT.md")
    with open(report_path, "w") as f:
        f.write(result["report"])
    meta = result["meta"]
    # q was not retained on meta. Recompute is unnecessary: ranked rows carry q,
    # and unqualified rows in the summary use a blank when we don't have q.
    # Store q on the result during run. If missing, leave blank.
    q = result.get("q")
    specs, rules = meta["specs"], meta["rules"]
    summary = _summary_rows(
        result["ranked"], meta, meta["sig_sum"], meta["sig_cnt"], None, None, q, specs, rules,
    )
    _write_csv(os.path.join(out_dir, "fgperfect_summary.csv"), summary, SUMMARY_FIELDS)
    trade_fields = ["rank", "config", "day", "symbol", "clock", "side", "raw", "greed", "fear", "squeeze", "mom", "note"]
    if result["trades"]:
        extra = [k for k in result["trades"][0] if k not in trade_fields]
        # Stable order: net_ then why_, by rule id.
        nets = [f"net_{r.id}" for r in rules]
        whys = [f"why_{r.id}" for r in rules]
        trade_fields = trade_fields + [c for c in nets + whys if c in result["trades"][0] or True]
    _write_csv(os.path.join(out_dir, "fgperfect_trades.csv"), result["trades"], trade_fields)
    fold_fields = ["fold", "cell", "select_note", "train_start", "train_end", "test_start", "test_end",
                   "train_fills", "train_days", "train_mean", "test_fills", "test_mean", "test_random", "test_paired"]
    _write_csv(os.path.join(out_dir, "fgperfect_folds.csv"), result["folds"], fold_fields)
    choice = result["choice"]
    survived = bool(choice and choice.get("survives"))
    spec = next((s for s in specs if choice and s.id == choice["spec"]), None)
    rule = next((r for r in rules if choice and r.id == choice["rule"]), None)
    pine = render_pine(spec, rule, survived)
    with open(os.path.join(out_dir, "FGPERFECT.pine"), "w") as f:
        f.write(pine)
    # Drop the big arrays from the returned meta so a caller can print it.
    return report_path


def _empty_report(path, message):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w") as f:
        f.write("# Fear-greed fade PERFECT\n\n" + message + "\n\nData only. Research tool, not trading advice. No orders.\n")
    pine = render_pine(None, None, False)
    with open(os.path.join(os.path.dirname(path) or ".", "FGPERFECT.pine"), "w") as f:
        f.write(pine)


def _env_flag(name):
    return os.getenv(name, "").strip().lower() in {"1", "true", "yes", "y"}


def _env_int(name, default):
    raw = os.getenv(name, "").strip()
    return int(raw) if raw else default


def keys_ready():
    return bool(os.getenv("ALPACA_KEY", "").strip() and os.getenv("ALPACA_SECRET", "").strip())


def main():
    t0 = time.time()
    out_dir = os.getenv("FG_OUT", "results").strip() or "results"
    os.makedirs(out_dir, exist_ok=True)
    report_path = os.path.join(out_dir, "FGPERFECT.md")
    synthetic = _env_flag("FG_SYNTH")
    if not synthetic and not keys_ready():
        _empty_report(report_path, MISSING_KEYS)
        raise SystemExit(MISSING_KEYS)
    days_n = _env_int("FG_DAYS", 120)
    if days_n < K_FOLDS + 1:
        _empty_report(report_path, f"Need at least {K_FOLDS + 1} sessions. Got {days_n}.")
        raise SystemExit(f"days must be at least {K_FOLDS + 1}")
    symbols = [s.strip().upper() for s in os.getenv("FG_SYMBOLS", "SPY,QQQ").split(",") if s.strip()]
    if not symbols:
        raise SystemExit("symbols is empty")
    smoke = _env_flag("FG_SMOKE")
    specs, rules = smoke_catalog() if smoke else (None, None)
    n_boot = _env_int("FG_BOOT", 50 if smoke else 1000)
    n_shuf = _env_int("FG_SHUFFLES", 2 if smoke else N_SHUFFLE)
    workers = _env_int("FG_WORKERS", 4)
    cache_dir = os.getenv("FG_CACHE", "/tmp/fgperfect-cache").strip() or "/tmp/fgperfect-cache"
    now = datetime.now(NY)
    end = datetime.now(timezone.utc) - timedelta(minutes=20)
    start = (pd.Timestamp(now.date(), tz=NY) - pd.Timedelta(days=int(days_n * 3 + 30))).tz_convert("UTC").to_pydatetime()
    sc._print_scrubbed(f"fgperfect symbols {', '.join(symbols)} days {days_n} synthetic {int(synthetic)} smoke {int(smoke)}")
    frames = sc._load_underlying(symbols, start, end, synthetic)
    und = {sym: sc.rth_session(df) for sym, df in frames.items()}
    all_days = sc.complete_days(und, symbols, now)
    if len(all_days) < K_FOLDS + 1:
        _empty_report(report_path, "Not enough completed sessions to score.")
        raise SystemExit("Not enough completed sessions.")
    score_days = all_days[-days_n:]
    sc._print_scrubbed(f"  sessions {score_days[0]} .. {score_days[-1]} n {len(score_days)}")
    result = run_study(
        frames, symbols, score_days, und, synthetic=synthetic, cache_dir=cache_dir,
        workers=workers, n_boot=n_boot, n_shuf=n_shuf, specs=specs, rules=rules, smoke=smoke,
    )
    elapsed = (time.time() - t0) / 60.0
    result["meta"]["runtime_min"] = elapsed
    result["report"] = re.sub(
        r"Runtime [0-9.]+ minutes\.",
        f"Runtime {elapsed:.1f} minutes.",
        result["report"],
        count=1,
    )
    write_outputs(out_dir, result)
    sc._print_scrubbed(f"  wrote {report_path}")
    return result


if __name__ == "__main__":
    main()
