"""Vix Fix whipsaw check on real 0DTE option prices. Data only. No orders.

The signal is read off 1-minute SPY and QQQ bars. Fear and greed are
``backtest.vfx_pane`` on the 0-100 scale. A fill uses the same ask/bid cost
model as the greed/fear fade: half-spread max(1 cent, 0.5% of premium) per
side, $0.65 commission per side, 1-strike OTM, 0DTE, premium 0.30-1.00.
The last 25% of sessions is held out with ``fgfade.holdout_split``.
"""

from __future__ import annotations

import csv
import os
import sys
import time
import traceback
from datetime import datetime, timedelta, timezone

import numpy as np
import pandas as pd

import edge_hunt as eh
import fgfade as fg
import scalp_real as sc

NY = fg.NY
COSTS = fg.COSTS
LOOKBACK = 22
MAX_LEVELS = (95, 91)
OTHERS = ("ge60", "ge30", "asleep")
FILTERS = ("none", "mom_with", "range_lt_3atr", "vwap_with")
WINDOWS = ("all", "noon")
EXITS = ("hold20", "tp15_sl25", "be_a15")
NOON_LO, NOON_HI = 150, 210  # 12:00 inclusive through 12:59
STRIKE = "1otm"

SUMMARY_HEADERS = [
    "variant", "filter", "window", "exit", "n", "sessions",
    "mean_net", "win", "median", "worst", "ci_lo", "ci_hi",
    "train_n", "train_mean", "hold_n", "hold_mean", "random_n", "random_mean",
]
TRADE_FIELDS = [
    "day", "symbol", "clock", "side", "max_level", "other_value",
    "fear", "greed", "signal_minute", "entry_minute", "in_noon",
    "mom_with", "range_lt_3atr", "vwap_with", "split",
    "contract", "raw",
    "net_hold20", "why_hold20", "net_tp15_sl25", "why_tp15_sl25", "net_be_a15", "why_be_a15",
    "rnd_minute", "rnd_net_hold20", "rnd_net_tp15_sl25", "rnd_net_be_a15",
    "und_atr_20", "und_atr_30", "rnd_und_atr_20", "rnd_und_atr_30",
]


def _log(message):
    sc._print_scrubbed(message, flush=True)


def _stage(name, fn, failures):
    _log(f"STAGE {name} start")
    try:
        return fn()
    except (Exception, SystemExit) as exc:
        traceback.print_exc()
        sys.stderr.flush()
        _log(f"STAGE {name} failed: {exc}")
        failures.append((name, str(exc)))
        return None


def is_break(level, i, day, max_level):
    """Previous bar was at the max and this bar is the first print back below it."""
    if i < 1 or day[i] != day[i - 1]:
        return False
    prev = float(level[i - 1])
    cur = float(level[i])
    if prev != prev or cur != cur:
        return False
    return prev >= float(max_level) and cur < float(max_level)


def first_break(level, i, day, max_level, lookback=LOOKBACK):
    """True when `i` is a max break and no other break sits in the prior `lookback` bars.

    The lookback does not cross a session. A later bar that is still below the
    max is not a break, because the previous bar was not maxed.
    """
    if not is_break(level, i, day, max_level):
        return False
    start = max(1, i - int(lookback))
    for j in range(start, i):
        if day[j] != day[i]:
            continue
        if is_break(level, j, day, max_level):
            return False
    return True


def other_ok(value, mode):
    if value != value:
        return False
    if mode == "ge60":
        return float(value) >= 60.0
    if mode == "ge30":
        return float(value) >= 30.0
    if mode == "asleep":
        return float(value) < 10.0
    raise ValueError(mode)


def _finite(value):
    return isinstance(value, (int, float)) and value == value


def atr_move(sess, entry_min, side, atr, ahead):
    """Directional underlying move in ATR from the entry open to the later close."""
    if sess is None or not _finite(atr) or atr <= 0:
        return float("nan")
    m1 = int(entry_min) + int(ahead)
    m0 = int(entry_min)
    if m0 < 0 or m1 >= sc.N_MIN or m1 < 0:
        return float("nan")
    if not (sess["real"][m0] and sess["real"][m1]):
        return float("nan")
    px0 = float(sess["open"][m0])
    px1 = float(sess["close"][m1])
    if not (_finite(px0) and _finite(px1)):
        return float("nan")
    return float(side) * (px1 - px0) / float(atr)


def _flag(value):
    return "true" if value else "false"


def collect_signals(fear, greed, high, low, close, minutes, day_i, atr, mom, vwap, sym_i, und_day, score_days):
    """One record per first break that passes at least one other-side test.

    `day_i` is -1 off the scored sessions. Entry is the next bar's open, so the
    signal bar's own close is not the fill.
    """
    fear = np.asarray(fear, dtype=float)
    greed = np.asarray(greed, dtype=float)
    n = len(fear)
    day = np.asarray(day_i)
    out = []
    for i in range(1, n):
        if int(day[i]) < 0:
            continue
        minute = int(minutes[i])
        entry = minute + 1
        if entry < fg.ENTRY_LO or entry > fg.ENTRY_HI or entry >= sc.FLAT_MIN:
            continue
        for max_level in MAX_LEVELS:
            for side, level, other in ((1, fear, greed), (-1, greed, fear)):
                if not first_break(level, i, day, max_level):
                    continue
                other_v = float(other[i])
                if not any(other_ok(other_v, mode) for mode in OTHERS):
                    continue
                prev = i - 1
                same = day[prev] == day[i]
                mom_i = float(mom[i]) if i < len(mom) else float("nan")
                mom_p = float(mom[prev]) if same and prev < len(mom) else float("nan")
                if side == 1:
                    mom_with = _finite(mom_i) and _finite(mom_p) and not (mom_i < mom_p)
                else:
                    mom_with = _finite(mom_i) and _finite(mom_p) and not (mom_i > mom_p)
                bar_range = float(high[i] - low[i])
                atr_i = float(atr[i]) if i < len(atr) else float("nan")
                range_ok = _finite(atr_i) and atr_i > 0 and _finite(bar_range) and bar_range < 3.0 * atr_i
                vw = float(vwap[i]) if i < len(vwap) else float("nan")
                cl = float(close[i])
                if side == 1:
                    vwap_ok = _finite(vw) and _finite(cl) and cl >= vw
                else:
                    vwap_ok = _finite(vw) and _finite(cl) and cl <= vw
                if _finite(vw) and _finite(cl) and _finite(atr_i) and atr_i > 0:
                    signed = (cl - vw) / atr_i
                    vwap_dist = signed if side == 1 else -signed
                else:
                    vwap_dist = float("nan")
                sess = und_day.get(score_days[int(day[i])])
                out.append({
                    "day_i": int(day[i]),
                    "sym_i": int(sym_i),
                    "side": int(side),
                    "max_level": int(max_level),
                    "other_value": other_v,
                    "fear": float(fear[i]),
                    "greed": float(greed[i]),
                    "signal_minute": minute,
                    "entry_minute": entry,
                    "mom_with": bool(mom_with),
                    "range_lt_3atr": bool(range_ok),
                    "vwap_with": bool(vwap_ok),
                    "vwap_dist": float(vwap_dist),
                    "in_noon": bool(NOON_LO <= entry < NOON_HI),
                    "und_atr_20": atr_move(sess, entry, side, atr_i, 20),
                    "und_atr_30": atr_move(sess, entry, side, atr_i, 30),
                    "_atr": atr_i,
                })
    return out


def signals_from_frames(frames, symbols, score_days, und):
    """Fear/greed from ``vfx_pane`` on 1-minute RTH bars. Warmup days stay in the pane."""
    score_index = {day: i for i, day in enumerate(score_days)}
    found = []
    for sym_i, sym in enumerate(symbols):
        df = frames.get(sym)
        if df is None or not len(df):
            continue
        bars = fg.to_tf(df, 1)
        if not len(bars):
            continue
        fear, greed = fg.fear_greed(bars)
        _sq, mom, _up, _dn = fg.ttm_squeeze(bars["high"], bars["low"], bars["close"])
        high = bars["high"].to_numpy(dtype=float)
        low = bars["low"].to_numpy(dtype=float)
        close = bars["close"].to_numpy(dtype=float)
        minutes = (bars.index.hour * 60 + bars.index.minute - (9 * 60 + 30)).to_numpy(dtype=int)
        day_ord = np.array([ts.date().toordinal() for ts in bars.index], dtype=np.int32)
        day_i = np.array([score_index.get(ts.date(), -1) for ts in bars.index], dtype=np.int32)
        atr = fg.atr14(high, low, close)
        vwap = fg.session_vwap(high, low, close, bars["volume"].to_numpy(dtype=float), day_ord)
        und_day = und.get(sym, {})
        found.extend(collect_signals(
            fear, greed, high, low, close, minutes, day_i, atr, mom, vwap,
            sym_i, und_day, score_days,
        ))
    for sig in found:
        day = score_days[sig["day_i"]]
        sig["rnd_minute"] = fg.random_minute(
            sig["entry_minute"],
            np.random.default_rng(sc.stream_seed(
                "whipsaw", day.isoformat(), symbols[sig["sym_i"]],
                sig["entry_minute"], sig["side"], sig["max_level"],
            )),
        )
    return found


def _passes(sig, other, filt, window):
    if not other_ok(sig["other_value"], other):
        return False
    if window == "noon" and not sig["in_noon"]:
        return False
    if filt == "none":
        return True
    return bool(sig[filt])


def variant_id(max_level, other, side):
    side_name = "long" if int(side) == 1 else "short"
    return f"max{int(max_level)}_{other}_{side_name}"


def needed_contracts(signals, und, symbols, score_days):
    bt = sc._bt()
    needed = {}
    seen = set()
    for sig in signals:
        minutes = [sig["entry_minute"]]
        if sig.get("rnd_minute") is not None:
            minutes.append(int(sig["rnd_minute"]))
        for minute in minutes:
            key = (sig["day_i"], sig["sym_i"], int(minute), sig["side"])
            if key in seen:
                continue
            seen.add(key)
            day = score_days[sig["day_i"]]
            sess = und[symbols[sig["sym_i"]]].get(day)
            if sess is None:
                continue
            for m in (int(minute), int(minute) + 1):
                if m < fg.ENTRY_LO or m > fg.ENTRY_HI or m >= sc.FLAT_MIN:
                    continue
                spot = sc.spot_at(sess, m)
                strike = sc.strike_price(spot, sig["side"], STRIKE)
                if strike is None:
                    continue
                cp = "C" if int(sig["side"]) == 1 else "P"
                needed.setdefault(day, set()).add(bt.lab_occ(symbols[sig["sym_i"]], day, cp, strike))
    return needed


def locate_fill(sess, opt, day, sym, minute, side):
    """Same strike walk as the fade study. No print may slip one minute. A print outside the band does not."""
    bt = sc._bt()
    minute = int(minute)
    for m in (minute, minute + 1):
        if m < fg.ENTRY_LO or m > fg.ENTRY_HI or m >= sc.FLAT_MIN:
            continue
        spot = sc.spot_at(sess, m)
        strike = sc.strike_price(spot, side, STRIKE)
        if strike is None:
            continue
        contract = bt.lab_occ(sym, day, "C" if int(side) == 1 else "P", strike)
        rec = opt.get((day, contract))
        if rec is None:
            continue
        if not (rec["real"][m] and np.isfinite(rec["open"][m]) and float(rec["open"][m]) >= sc.MIN_PREMIUM):
            continue
        raw = float(rec["open"][m])
        if not sc.premium_in_band(raw, fg.PREMIUM_BAND):
            return None
        return rec, m, contract, raw
    return None


def breakeven_trade(opt, entry_min, arm=0.15, costs=COSTS):
    """be_a15 on the option print. No stop until the high is +arm over the entry print.

    The stop is then the entry print. The sale is haircut by the same half-spread
    ``simulate_trade`` uses. A 15:55 flat is the harness flat, not a 20-bar hold.
    """
    cent, pct, comm = costs
    entry_min = int(entry_min)
    if entry_min < 0 or entry_min >= sc.FLAT_MIN:
        return {"status": "skip_entry"}
    if not (opt["real"][entry_min] and np.isfinite(opt["open"][entry_min]) and opt["open"][entry_min] >= sc.MIN_PREMIUM):
        return {"status": "skip_entry"}
    raw = float(opt["open"][entry_min])
    if not sc.premium_in_band(raw, fg.PREMIUM_BAND):
        return {"status": "skip_premium", "entry_min": entry_min, "raw_entry": raw}
    debit = raw + sc.half_spread(raw, cent, pct)
    peak = raw
    armed = False
    last = entry_min
    fill = reason = exit_min = None
    for m in range(entry_min, sc.FLAT_MIN + 1):
        if opt["real"][m] and np.isfinite(opt["close"][m]):
            o = float(opt["open"][m]) if np.isfinite(opt["open"][m]) else float(opt["close"][m])
            h = float(opt["high"][m]) if np.isfinite(opt["high"][m]) else float(opt["close"][m])
            l = float(opt["low"][m]) if np.isfinite(opt["low"][m]) else float(opt["close"][m])
            c = float(opt["close"][m])
            last = m
        else:
            age = m - last
            carried = opt["lab"][m] if 0 <= m < sc.N_MIN else np.nan
            if age > sc.STALE_AFTER or not np.isfinite(carried):
                if m >= sc.FLAT_MIN:
                    return {"status": "skip_stale", "entry_min": entry_min}
                continue
            o = h = l = c = float(carried)
        if armed and l <= raw:
            fill = min(o, raw)
            reason = "be"
            exit_min = m
            break
        if h == h:
            peak = max(peak, h)
        if peak >= raw * (1.0 + float(arm)):
            armed = True
        if m >= sc.FLAT_MIN:
            fill = c
            reason = "flat"
            exit_min = m
            break
    if fill is None:
        return {"status": "skip_stale", "entry_min": entry_min}
    credit = max(0.0, fill - sc.half_spread(fill, cent, pct))
    dollar = (credit - debit) * 100.0 - 2.0 * comm
    net = dollar / (debit * 100.0) * 100.0
    return {
        "status": "fill", "entry_min": entry_min, "exit_min": exit_min,
        "raw_entry": raw, "reason": reason, "net_pct": float(net),
    }


def _result_net(res):
    if not res or res.get("status") != "fill" or not _finite(res.get("net_pct")):
        return float("nan"), res.get("status", "") if res else ""
    return float(res["net_pct"]), str(res.get("reason", ""))


def exit_pack(opt, entry_min):
    hold = sc.simulate_trade(opt, int(entry_min), (100.0, None, 20), COSTS, allow_slip=False, premium=fg.PREMIUM_BAND)
    fixed = sc.simulate_trade(opt, int(entry_min), (0.15, 0.25, 10_000), COSTS, allow_slip=False, premium=fg.PREMIUM_BAND)
    be = breakeven_trade(opt, int(entry_min))
    out = {}
    for name, res in (("hold20", hold), ("tp15_sl25", fixed), ("be_a15", be)):
        net, why = _result_net(res)
        out[name] = {"net": net, "why": why}
    return out


def attach_fills(signals, und, opt, symbols, score_days):
    cache = {}

    def one(day_i, sym_i, minute, side):
        key = (day_i, sym_i, int(minute) if minute is not None else None, int(side))
        if key in cache:
            return cache[key]
        if minute is None:
            cache[key] = None
            return None
        day = score_days[day_i]
        sess = und[symbols[sym_i]].get(day)
        if sess is None:
            cache[key] = None
            return None
        located = locate_fill(sess, opt, day, symbols[sym_i], int(minute), int(side))
        if located is None:
            cache[key] = None
            return None
        rec, m, contract, raw = located
        packed = exit_pack(rec, m)
        packed["contract"] = contract
        packed["raw"] = raw
        packed["fill_minute"] = m
        cache[key] = packed
        return packed

    for sig in signals:
        sig["fill"] = one(sig["day_i"], sig["sym_i"], sig["entry_minute"], sig["side"])
        rnd = sig.get("rnd_minute")
        sig["rnd_fill"] = one(sig["day_i"], sig["sym_i"], rnd, sig["side"]) if rnd is not None else None
        sess = und[symbols[sig["sym_i"]]].get(score_days[sig["day_i"]])
        sig["rnd_und_atr_20"] = float("nan")
        sig["rnd_und_atr_30"] = float("nan")
        if rnd is not None and sess is not None and _finite(sig.get("_atr")):
            sig["rnd_und_atr_20"] = atr_move(sess, int(rnd), sig["side"], sig["_atr"], 20)
            sig["rnd_und_atr_30"] = atr_move(sess, int(rnd), sig["side"], sig["_atr"], 30)


def _fmt(value, digits=2):
    if not _finite(value):
        return ""
    return f"{float(value):.{digits}f}"


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


def _pack_stats(nets, day_ids, n_days, n_boot, seed):
    nets = np.asarray(list(nets), dtype=float)
    day_ids = np.asarray(list(day_ids), dtype=int)
    ok = np.isfinite(nets)
    nets = nets[ok]
    day_ids = day_ids[ok]
    n = int(len(nets))
    if n == 0:
        return {
            "n": 0, "sessions": 0, "mean": float("nan"), "win": float("nan"),
            "median": float("nan"), "worst": float("nan"),
            "ci_lo": float("nan"), "ci_hi": float("nan"),
        }
    sums = np.zeros(n_days, dtype=float)
    cnts = np.zeros(n_days, dtype=float)
    for value, day_i in zip(nets, day_ids):
        if 0 <= int(day_i) < n_days:
            sums[int(day_i)] += float(value)
            cnts[int(day_i)] += 1.0
    lo, hi = sc.bootstrap_mean(sums, cnts, int(n_boot), int(seed))
    return {
        "n": n,
        "sessions": int(len(set(int(d) for d in day_ids))),
        "mean": float(nets.mean()),
        "win": float(100.0 * np.mean(nets > 0)),
        "median": float(np.median(nets)),
        "worst": float(nets.min()),
        "ci_lo": lo,
        "ci_hi": hi,
    }


def _slice_nets(signals, other, filt, window, exit_name, which):
    nets = []
    days = []
    for sig in signals:
        if not _passes(sig, other, filt, window):
            continue
        packed = sig.get("fill") if which == "signal" else sig.get("rnd_fill")
        if not packed:
            continue
        value = packed[exit_name]["net"]
        if not _finite(value):
            continue
        nets.append(value)
        days.append(sig["day_i"])
    return nets, days


def summary_rows(signals, n_days, train_idx, test_idx, n_boot):
    train = set(int(i) for i in train_idx)
    test = set(int(i) for i in test_idx)
    rows = []
    for max_level in MAX_LEVELS:
        for other in OTHERS:
            for side in (1, -1):
                group = [s for s in signals if s["max_level"] == max_level and s["side"] == side]
                name = variant_id(max_level, other, side)
                for filt in FILTERS:
                    for window in WINDOWS:
                        for exit_name in EXITS:
                            nets, days = _slice_nets(group, other, filt, window, exit_name, "signal")
                            stats = _pack_stats(nets, days, n_days, n_boot, sc.stream_seed("whipsaw-boot", name, filt, window, exit_name))
                            train_nets = [v for v, d in zip(nets, days) if d in train]
                            hold_nets = [v for v, d in zip(nets, days) if d in test]
                            rnd_nets, _rnd_days = _slice_nets(group, other, filt, window, exit_name, "random")
                            rows.append({
                                "variant": name,
                                "filter": filt,
                                "window": window,
                                "exit": exit_name,
                                "n": stats["n"],
                                "sessions": stats["sessions"],
                                "mean_net": stats["mean"],
                                "win": stats["win"],
                                "median": stats["median"],
                                "worst": stats["worst"],
                                "ci_lo": stats["ci_lo"],
                                "ci_hi": stats["ci_hi"],
                                "train_n": len(train_nets),
                                "train_mean": _mean(train_nets),
                                "hold_n": len(hold_nets),
                                "hold_mean": _mean(hold_nets),
                                "random_n": len(rnd_nets),
                                "random_mean": _mean(rnd_nets),
                            })
    return rows


def underlying_rows(signals):
    """Mean directional ATR move on every signal, filled or not."""
    rows = []
    for max_level in MAX_LEVELS:
        for other in OTHERS:
            for side in (1, -1):
                name = variant_id(max_level, other, side)
                group = [
                    s for s in signals
                    if s["max_level"] == max_level and s["side"] == side and other_ok(s["other_value"], other)
                ]
                rows.append({
                    "variant": name,
                    "n": len(group),
                    "atr20": _mean(s["und_atr_20"] for s in group),
                    "atr30": _mean(s["und_atr_30"] for s in group),
                    "random_atr20": _mean(s.get("rnd_und_atr_20", float("nan")) for s in group),
                    "random_atr30": _mean(s.get("rnd_und_atr_30", float("nan")) for s in group),
                })
    return rows


def _md(headers, body):
    head = "| " + " | ".join(headers) + " |"
    rule = "| " + " | ".join("---" for _ in headers) + " |"
    lines = ["| " + " | ".join(str(c) for c in row) + " |" for row in body]
    return "\n".join([head, rule, *lines])


def _summary_body(rows):
    body = []
    for row in rows:
        body.append([
            row["variant"], row["filter"], row["window"], row["exit"],
            row["n"], row["sessions"],
            _fmt(row["mean_net"]), _fmt(row["win"]), _fmt(row["median"]), _fmt(row["worst"]),
            _fmt(row["ci_lo"]), _fmt(row["ci_hi"]),
            row["train_n"], _fmt(row["train_mean"]),
            row["hold_n"], _fmt(row["hold_mean"]),
            row["random_n"], _fmt(row["random_mean"]),
        ])
    return body


def _find(rows, **want):
    for row in rows:
        if all(row.get(key) == value for key, value in want.items()):
            return row
    return None


def verdict_paragraph(rows, und_rows, meta):
    bits = []
    for side in ("long", "short"):
        row = _find(rows, variant=f"max95_ge60_{side}", filter="none", window="all", exit="hold20")
        und = next((r for r in und_rows if r["variant"] == f"max95_ge60_{side}"), None)
        if row is None:
            continue
        bits.append(
            f"{side} hold20 all-day n {row['n']} mean {_fmt(row['mean_net'])}% "
            f"win {_fmt(row['win'])}% random {_fmt(row['random_mean'])}% "
            f"held-out n {row['hold_n']} mean {_fmt(row['hold_mean'])}%"
        )
        if und is not None:
            bits.append(
                f"{side} underlying ATR +20 {_fmt(und['atr20'])} +30 {_fmt(und['atr30'])} "
                f"(random +20 {_fmt(und['random_atr20'])})"
            )
    if not bits:
        text = "No primary max95 other-side-at-least-60 row was scored."
    else:
        text = " ".join(bits) + "."
    if meta.get("synthetic"):
        text += " Prices in this file are synthetic, not a market."
    text += " Held-out is the last 25% of sessions and was not used to choose the rule. This is not a reason to trade."
    return text


def render_report(rows, und_rows, meta, failures):
    parts = [
        "# Vix Fix whipsaw check",
        "",
        "Raw numbers are first. Definitions are under the table. The last paragraph is the only prose.",
        "",
        _md(SUMMARY_HEADERS, _summary_body(rows)),
        "",
        "## Underlying move in ATR",
        "",
        "Directional: long is (later close - entry open) / ATR(14), short is the opposite. "
        "The chart study's claim was long +0.31 / +0.36 and short +0.22 / +0.36 at +20 / +30 bars, random about 0. "
        "This table uses every signal, including ones with no option fill.",
        "",
        _md(
            ["variant", "n", "atr20", "atr30", "random_atr20", "random_atr30"],
            [[r["variant"], r["n"], _fmt(r["atr20"]), _fmt(r["atr30"]), _fmt(r["random_atr20"]), _fmt(r["random_atr30"])] for r in und_rows],
        ),
        "",
        "## What a row is",
        "",
        "Fear and greed are vfx_pane on 1-minute bars, 0-100. A max is the level at or above 95, or 91 in the variant. "
        "A break is the first bar back below that max after a maxed bar. A break is dropped when another break of the same max "
        f"sits in the prior {LOOKBACK} bars of the same session. Longs need greed at the break bar at least 60 (or 30, or under 10 for asleep). "
        "Shorts mirror that. ge30 includes every ge60 signal. Do not add those rows. "
        "The fill is the next bar's open, 1-strike OTM, 0DTE, premium 0.30 to 1.00. "
        "Entry debit is the print plus half-spread max(1 cent, 0.5%). The sale is the exit print minus that haircut. Commission is $0.65 a side. "
        "hold20 sells the close 20 minutes later. tp15_sl25 is target +15% and stop -25%, stop first, else the 15:55 flat. "
        "be_a15 has no stop until the option high is +15% over the entry print, then the stop is that print. "
        "mom_with drops a long whose squeeze momentum is lower than the prior bar, and a short whose momentum is higher. "
        "range_lt_3atr keeps a break bar whose high-low is under 3 ATR(14). "
        "vwap_with keeps a long closing at or above the session VWAP and a short closing at or below it. "
        "Filters are separate rows, not stacked. Noon is an entry minute from 12:00 through 12:59. "
        "Train is the first 75% of sessions. Held-out is the last 25%. The bootstrap CI is the day-clustered 95% interval of the mean.",
        "",
    ]
    if meta.get("synthetic"):
        parts.append("Synthetic prices are not a market. This file is a pipeline check.")
        parts.append("")
    if failures:
        parts.append("A stage failed. Rows above are whatever finished.")
        parts.append("")
        parts.extend(f"STAGE {name} failed: {err}" for name, err in failures)
        parts.append("")
    parts.append(
        f"Sessions {meta.get('first_day', '')} through {meta.get('last_day', '')} "
        f"({meta.get('n_sessions', 0)} sessions). Signals {meta.get('n_signals', 0)}. "
        f"Runtime {_fmt(meta.get('runtime_min'), 1)} minutes."
    )
    parts.append("")
    parts.append(verdict_paragraph(rows, und_rows, meta))
    parts.append("")
    return "\n".join(parts)


def trade_rows(signals, symbols, score_days, train_idx):
    train = set(int(i) for i in train_idx)
    rows = []
    for sig in signals:
        fill = sig.get("fill")
        if not fill:
            continue
        rnd = sig.get("rnd_fill") or {}
        day = score_days[sig["day_i"]]
        row = {
            "day": day.isoformat(),
            "symbol": symbols[sig["sym_i"]],
            "clock": fg.clock_hhmm(sig["entry_minute"]),
            "side": "long" if sig["side"] == 1 else "short",
            "max_level": sig["max_level"],
            "other_value": _fmt(sig["other_value"]),
            "fear": _fmt(sig["fear"]),
            "greed": _fmt(sig["greed"]),
            "signal_minute": sig["signal_minute"],
            "entry_minute": sig["entry_minute"],
            "in_noon": _flag(sig["in_noon"]),
            "mom_with": _flag(sig["mom_with"]),
            "range_lt_3atr": _flag(sig["range_lt_3atr"]),
            "vwap_with": _flag(sig["vwap_with"]),
            "split": "train" if sig["day_i"] in train else "hold",
            "contract": fill.get("contract", ""),
            "raw": _fmt(fill.get("raw"), 4),
            "und_atr_20": _fmt(sig["und_atr_20"]),
            "und_atr_30": _fmt(sig["und_atr_30"]),
            "rnd_minute": "" if sig.get("rnd_minute") is None else int(sig["rnd_minute"]),
            "rnd_und_atr_20": _fmt(sig.get("rnd_und_atr_20")),
            "rnd_und_atr_30": _fmt(sig.get("rnd_und_atr_30")),
        }
        for name in EXITS:
            leg = fill.get(name) or {}
            row[f"net_{name}"] = _fmt(leg.get("net"), 4)
            row[f"why_{name}"] = leg.get("why", "")
            rleg = rnd.get(name) or {}
            row[f"rnd_net_{name}"] = _fmt(rleg.get("net"), 4)
        rows.append(row)
    return rows


def write_outputs(out_dir, report, trades):
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "WHIPSAW.md")
    with open(path, "w") as handle:
        handle.write(report)
    csv_path = os.path.join(out_dir, "whipsaw_trades.csv")
    with open(csv_path, "w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=TRADE_FIELDS, extrasaction="ignore")
        writer.writeheader()
        for row in trades:
            writer.writerow(row)
    return path


def _empty_report(meta, message, failures):
    meta = dict(meta)
    meta.setdefault("n_signals", 0)
    meta.setdefault("n_sessions", 0)
    text = render_report([], [], meta, failures)
    return text.replace(
        "Raw numbers are first.",
        "Raw numbers are first.\n\n" + message,
        1,
    )


def run_study(frames, symbols, score_days, und, opt=None, synthetic=False, cache_dir=None,
              workers=4, n_boot=1000):
    t0 = time.time()
    failures = []
    train_idx, test_idx = fg.holdout_split(len(score_days))
    meta = {
        "symbols": list(symbols),
        "n_sessions": len(score_days),
        "first_day": score_days[0].isoformat() if score_days else "",
        "last_day": score_days[-1].isoformat() if score_days else "",
        "n_signals": 0,
        "synthetic": bool(synthetic),
        "runtime_min": 0.0,
        "score_days": list(score_days),
    }
    signals = _stage(
        "signals",
        lambda: signals_from_frames(frames, symbols, score_days, und),
        failures,
    )
    if signals is None:
        signals = []
    meta["n_signals"] = len(signals)
    _log(f"  signals {len(signals)}")

    def _download():
        nonlocal opt
        if opt is not None:
            return opt
        needed = needed_contracts(signals, und, symbols, score_days)
        _log(f"  option days {len(needed)} contract-days {sum(len(v) for v in needed.values())}")
        return eh.fetch_option_days(
            needed, und, symbols, synthetic,
            cache_dir or "/tmp/whipsaw-cache",
            workers=max(1, int(workers)),
        )

    if signals:
        opt = _stage("download", _download, failures)
        if opt is None:
            opt = {}
        _stage("fills", lambda: attach_fills(signals, und, opt, symbols, score_days), failures)

    und_rows = underlying_rows(signals) if signals else []
    rows = []
    if signals and any(s.get("fill") for s in signals):
        packed = _stage(
            "summarize",
            lambda: summary_rows(signals, len(score_days), train_idx, test_idx, n_boot),
            failures,
        )
        rows = packed or []
    elif not failures:
        rows = summary_rows(signals, len(score_days), train_idx, test_idx, n_boot) if signals else []

    meta["runtime_min"] = (time.time() - t0) / 60.0
    report = render_report(rows, und_rows, meta, failures)
    trades = trade_rows(signals, symbols, score_days, train_idx) if signals else []
    return {
        "report": report,
        "rows": rows,
        "underlying": und_rows,
        "trades": trades,
        "meta": meta,
        "failures": failures,
        "signals": signals,
    }


def _env_flag(name):
    return os.getenv(name, "").strip().lower() in {"1", "true", "yes", "y"}


def _env_int(name, default):
    raw = os.getenv(name, "").strip()
    return int(raw) if raw else default


def keys_ready():
    return bool(os.getenv("ALPACA_KEY", "").strip() and os.getenv("ALPACA_SECRET", "").strip())


def main():
    t0 = time.time()
    out_dir = os.getenv("WHIP_OUT", "results").strip() or "results"
    os.makedirs(out_dir, exist_ok=True)
    synthetic = _env_flag("WHIP_SYNTH")
    if not synthetic and not keys_ready():
        meta = {"n_sessions": 0, "n_signals": 0, "synthetic": False, "runtime_min": 0.0, "first_day": "", "last_day": ""}
        write_outputs(out_dir, _empty_report(meta, fg.MISSING_KEYS, [("keys", fg.MISSING_KEYS)]), [])
        _log(f"STAGE keys failed: {fg.MISSING_KEYS}")
        return 1
    days_n = _env_int("WHIP_DAYS", 120)
    if days_n < 6:
        meta = {"n_sessions": 0, "n_signals": 0, "synthetic": synthetic, "runtime_min": 0.0, "first_day": "", "last_day": ""}
        message = f"Need at least 6 sessions. Got {days_n}."
        write_outputs(out_dir, _empty_report(meta, message, [("days", message)]), [])
        _log(f"STAGE days failed: {message}")
        return 1
    symbols = [s.strip().upper() for s in os.getenv("WHIP_SYMBOLS", "SPY,QQQ").split(",") if s.strip()]
    if not symbols:
        _log("STAGE symbols failed: symbols is empty")
        return 1
    n_boot = _env_int("WHIP_BOOT", 1000)
    workers = _env_int("WHIP_WORKERS", 4)
    cache_dir = os.getenv("WHIP_CACHE", "/tmp/whipsaw-cache").strip() or "/tmp/whipsaw-cache"
    now = datetime.now(NY)
    end = datetime.now(timezone.utc) - timedelta(minutes=20)
    start = (pd.Timestamp(now.date(), tz=NY) - pd.Timedelta(days=int(days_n * 3 + 30))).tz_convert("UTC").to_pydatetime()
    _log(f"whipsaw symbols {', '.join(symbols)} days {days_n} synthetic {int(synthetic)}")
    try:
        frames = sc._load_underlying(symbols, start, end, synthetic)
        und = {sym: sc.rth_session(df) for sym, df in frames.items()}
        all_days = sc.complete_days(und, symbols, now)
    except (Exception, SystemExit) as exc:
        traceback.print_exc()
        meta = {"n_sessions": 0, "n_signals": 0, "synthetic": synthetic, "runtime_min": 0.0, "first_day": "", "last_day": ""}
        write_outputs(out_dir, _empty_report(meta, str(exc), [("load", str(exc))]), [])
        _log(f"STAGE load failed: {exc}")
        return 1
    if len(all_days) < 6:
        meta = {"n_sessions": len(all_days), "n_signals": 0, "synthetic": synthetic, "runtime_min": 0.0, "first_day": "", "last_day": ""}
        message = "Not enough completed sessions to score."
        write_outputs(out_dir, _empty_report(meta, message, [("sessions", message)]), [])
        _log(f"STAGE sessions failed: {message}")
        return 1
    score_days = all_days[-days_n:]
    _log(f"  sessions {score_days[0]} .. {score_days[-1]} n {len(score_days)}")
    result = run_study(
        frames, symbols, score_days, und,
        synthetic=synthetic, cache_dir=cache_dir, workers=workers, n_boot=n_boot,
    )
    result["meta"]["runtime_min"] = (time.time() - t0) / 60.0
    result["report"] = result["report"].replace(
        f"Runtime {_fmt(result['meta'].get('runtime_min'), 1)} minutes.",
        f"Runtime {result['meta']['runtime_min']:.1f} minutes.",
    )
    # The report was rendered inside run_study with its own clock. Rewrite the sentence from the meta we just set.
    result["report"] = render_report(
        result["rows"], result["underlying"], result["meta"], result["failures"],
    )
    try:
        _log("STAGE write outputs start")
        path = write_outputs(out_dir, result["report"], result["trades"])
        _log(f"  wrote {path}")
    except Exception as exc:
        traceback.print_exc()
        _log(f"STAGE write outputs failed: {exc}")
        result["failures"].append(("write outputs", str(exc)))
    if result["failures"]:
        name, err = result["failures"][-1]
        _log(f"STAGE {name} failed: {err}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
