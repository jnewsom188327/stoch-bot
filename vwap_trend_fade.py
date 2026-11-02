"""Vix Fix plus VWAP trend fade on real 0DTE option prices. Data only. No orders.

SPY, 1-minute bars and the same bars aggregated to 2 minutes. Fear and greed
are ``vfx_pane``. The fill, the half-spread, and the commission are the
whipsaw cost model. The contract is the call or put whose ask is inside
$0.45–$1.00 and closest to $0.65. The last 25% of sessions is held out.
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
import whipsaw_check as wc
import whipsaw_vwap as wv

NY = wc.NY
TFS = (1, 2)
MAX_LEVELS = (95, 91)
OPP_LEVELS = (30, 45)
CONFLUENCE = ("base", "mom_turn", "first_drop")
EXITS = ("hold20", "tp15_sl25", "be_a15", "vwap_touch")
SIG_LO = 10    # 9:40
SIG_HI = 330   # 15:00 inclusive, signal-bar start
PREMIUM_LO = 0.45
PREMIUM_HI = 1.00
PREMIUM_TARGET = 0.65
HOLD_BARS = 20

STAT_HEADERS = [
    "variant", "confluence", "exit", "n", "sessions", "mean_net", "win", "median", "worst",
    "ci_lo", "ci_hi", "train_n", "train_mean", "hold_n", "hold_mean",
    "random_n", "random_mean", "skipped_premium",
]
TRADE_FIELDS = [
    "day", "symbol", "tf", "clock", "side", "max_level", "opp", "confluence_mom", "confluence_first",
    "split", "contract", "strike", "ask", "raw", "skip",
    "net_hold20", "net_tp15_sl25", "net_be_a15", "net_vwap_touch", "touch",
    "rnd_minute", "rnd_net_hold20", "rnd_net_tp15_sl25", "rnd_net_be_a15", "rnd_net_vwap_touch",
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


def in_signal_window(minute):
    """Signal-bar start from 9:40 through 15:00 ET. 9:30 is session minute 0."""
    return SIG_LO <= int(minute) <= SIG_HI


def entry_ask(raw, costs=wc.COSTS):
    """Ask-side price of a print: the print plus the study half-spread."""
    cent, pct, _comm = costs
    raw = float(raw)
    return raw + sc.half_spread(raw, cent, pct)


def candidate_strikes(spot, side):
    """Calls for a long, puts for a short. A few strikes ITM through the cheap OTM wing.

    $0.65 0DTE premium on SPY sits near the money, not twenty strikes away.
    """
    atm = int(round(float(spot)))
    if int(side) == 1:
        lo, hi = atm - 3, atm + 25
    else:
        lo, hi = atm - 25, atm + 3
    return [k for k in range(lo, hi + 1) if k > 0]


def pick_ask(quotes, spot):
    """quotes are (strike, ask). Keep $0.45–$1.00. Closest to $0.65, then closer to the spot."""
    ok = [(int(k), float(a)) for k, a in quotes if PREMIUM_LO <= float(a) <= PREMIUM_HI]
    if not ok:
        return None
    return min(ok, key=lambda ka: (abs(ka[1] - PREMIUM_TARGET), abs(ka[0] - float(spot)), ka[0]))


def _same(day, i, j):
    return 0 <= j < len(day) and day[i] == day[j]


def mom_turned(mom, day, i, side):
    """True when momentum was against the fade and turns toward it on a bar 0–3 back.

    A short wants a turn down (rising, then falling). A long wants a turn up.
    """
    mom = np.asarray(mom, dtype=float)
    for k in range(max(2, i - 3), i + 1):
        if not (_same(day, i, k) and _same(day, k, k - 1) and _same(day, k - 1, k - 2)):
            continue
        a, b, c = float(mom[k - 2]), float(mom[k - 1]), float(mom[k])
        if not (a == a and b == b and c == c):
            continue
        if int(side) == -1 and b > a and c < b:
            return True
        if int(side) == 1 and b < a and c > b:
            return True
    return False


def collect_signals(fear, greed, close, vwap, mom, minutes, day_i, tf, sym_i):
    """One record per (max, opposite-cap) pair that passes the base fade rule."""
    fear = np.asarray(fear, dtype=float)
    greed = np.asarray(greed, dtype=float)
    close = np.asarray(close, dtype=float)
    vwap = np.asarray(vwap, dtype=float)
    minutes = np.asarray(minutes, dtype=int)
    day = np.asarray(day_i)
    n = len(fear)
    out = []
    for i in range(1, n):
        if int(day[i]) < 0 or not _same(day, i, i - 1):
            continue
        minute = int(minutes[i])
        if not in_signal_window(minute):
            continue
        entry = fg.entry_minute_of(minute, tf)
        if entry is None:
            continue
        if i < 5 or not _same(day, i, i - 5):
            continue
        slope = float(vwap[i] - vwap[i - 5])
        if not (slope == slope and vwap[i] == vwap[i] and close[i] == close[i]):
            continue
        if not (fear[i] == fear[i] and greed[i] == greed[i] and fear[i - 1] == fear[i - 1] and greed[i - 1] == greed[i - 1]):
            continue
        if not (fear[i] < fear[i - 1] and greed[i] < greed[i - 1]):
            continue
        for max_level in MAX_LEVELS:
            for opp in OPP_LEVELS:
                for side, extreme, quiet in ((-1, greed, fear), (1, fear, greed)):
                    if float(extreme[i - 1]) < float(max_level) or float(quiet[i - 1]) > float(opp):
                        continue
                    if side == -1:
                        if not (slope < 0.0 and close[i] > vwap[i]):
                            continue
                    else:
                        if not (slope > 0.0 and close[i] < vwap[i]):
                            continue
                    first = False
                    if i >= 2 and _same(day, i - 1, i - 2) and extreme[i - 2] == extreme[i - 2]:
                        first = float(extreme[i]) < float(extreme[i - 1]) and float(extreme[i - 1]) >= float(extreme[i - 2])
                    out.append({
                        "day_i": int(day[i]),
                        "sym_i": int(sym_i),
                        "tf": int(tf),
                        "side": int(side),
                        "max_level": int(max_level),
                        "opp": int(opp),
                        "signal_minute": minute,
                        "entry_minute": int(entry),
                        "mom_turn": mom_turned(mom, day, i, side),
                        "first_drop": bool(first),
                        "fear": float(fear[i]),
                        "greed": float(greed[i]),
                    })
    return out


def signals_from_frames(frames, symbols, score_days, tfs=TFS):
    """1-minute RTH bars, and those bars aggregated to 2 minutes. Warmup days stay in the pane."""
    score_index = {day: i for i, day in enumerate(score_days)}
    found = []
    for sym_i, sym in enumerate(symbols):
        df = frames.get(sym)
        if df is None or not len(df):
            continue
        for tf in tfs:
            bars = fg.to_tf(df, tf)
            if not len(bars):
                continue
            fear, greed = fg.fear_greed(bars)
            _sq, mom, _up, _dn = fg.ttm_squeeze(bars["high"], bars["low"], bars["close"])
            close = bars["close"].to_numpy(dtype=float)
            high = bars["high"].to_numpy(dtype=float)
            low = bars["low"].to_numpy(dtype=float)
            day_ord = np.array([ts.date().toordinal() for ts in bars.index], dtype=np.int32)
            vwap = fg.session_vwap(high, low, close, bars["volume"].to_numpy(dtype=float), day_ord)
            minutes = (bars.index.hour * 60 + bars.index.minute - (9 * 60 + 30)).to_numpy(dtype=int)
            day_i = np.array([score_index.get(ts.date(), -1) for ts in bars.index], dtype=np.int32)
            found.extend(collect_signals(fear, greed, close, vwap, mom, minutes, day_i, tf, sym_i))
    for sig in found:
        day = score_days[sig["day_i"]]
        rnd = fg.random_minute(
            sig["entry_minute"],
            np.random.default_rng(sc.stream_seed(
                "vwap-trend-fade", day.isoformat(), symbols[sig["sym_i"]],
                sig["tf"], sig["entry_minute"], sig["side"], sig["max_level"], sig["opp"],
            )),
        )
        if rnd is not None:
            rnd = int(rnd) - (int(rnd) % int(sig["tf"]))
            if rnd < fg.ENTRY_LO:
                rnd += int(sig["tf"])
        sig["rnd_minute"] = rnd
    return found


def session_paths(frames, symbols, score_days, tf):
    keep = set(score_days)
    out = {}
    for sym in symbols:
        df = frames.get(sym)
        if df is None or not len(df):
            continue
        bars = fg.to_tf(df, tf)
        if not len(bars):
            continue
        high = bars["high"].to_numpy(dtype=float)
        low = bars["low"].to_numpy(dtype=float)
        close = bars["close"].to_numpy(dtype=float)
        day_ord = np.array([ts.date().toordinal() for ts in bars.index], dtype=np.int32)
        vwap = fg.session_vwap(high, low, close, bars["volume"].to_numpy(dtype=float), day_ord)
        minutes = (bars.index.hour * 60 + bars.index.minute - (9 * 60 + 30)).to_numpy(dtype=int)
        for i, ts in enumerate(bars.index):
            day = ts.date()
            if day not in keep:
                continue
            m = int(minutes[i])
            if m < 0 or m >= sc.N_MIN:
                continue
            slot = out.get((sym, day))
            if slot is None:
                slot = {
                    "high": np.full(sc.N_MIN, np.nan),
                    "low": np.full(sc.N_MIN, np.nan),
                    "vwap": np.full(sc.N_MIN, np.nan),
                }
                out[(sym, day)] = slot
            slot["high"][m] = high[i]
            slot["low"][m] = low[i]
            slot["vwap"][m] = vwap[i]
    return out


def touch_minute(path, start, tf):
    """First chart bar in the next 20 whose range crosses that bar's VWAP. Else bar 20."""
    start = int(start)
    step = int(tf)
    cap = min(start + HOLD_BARS * step, sc.FLAT_MIN)
    if path is None:
        return cap, False
    m = start
    while m <= cap:
        if 0 <= m < sc.N_MIN:
            vw = float(path["vwap"][m])
            hi = float(path["high"][m])
            lo = float(path["low"][m])
            if hi == hi and lo == lo and vw == vw and lo <= vw <= hi:
                return m, True
        m += step
    return cap, False


def variant_id(tf, max_level, opp, side):
    side_name = "long" if int(side) == 1 else "short"
    return f"tf{int(tf)}_max{int(max_level)}_opp{int(opp)}_{side_name}"


def needed_contracts(signals, und, symbols, score_days):
    bt = sc._bt()
    needed = {}
    seen = set()
    for sig in signals:
        minutes = [sig["entry_minute"]]
        if sig.get("rnd_minute") is not None:
            minutes.append(int(sig["rnd_minute"]))
        day = score_days[sig["day_i"]]
        sess = und[symbols[sig["sym_i"]]].get(day)
        if sess is None:
            continue
        cp = "C" if int(sig["side"]) == 1 else "P"
        for minute in minutes:
            for m in (int(minute), int(minute) + 1):
                if m < fg.ENTRY_LO or m > fg.ENTRY_HI or m >= sc.FLAT_MIN:
                    continue
                spot = sc.spot_at(sess, m)
                if spot is None:
                    continue
                for strike in candidate_strikes(spot, sig["side"]):
                    contract = bt.lab_occ(symbols[sig["sym_i"]], day, cp, strike)
                    if (day, contract) in seen:
                        continue
                    seen.add((day, contract))
                    needed.setdefault(day, set()).add(contract)
    return needed


def _quotes_at(sess, opt, day, sym, minute, side):
    bt = sc._bt()
    spot = sc.spot_at(sess, minute)
    if spot is None:
        return None, [], False
    cp = "C" if int(side) == 1 else "P"
    quotes = []
    saw = False
    for strike in candidate_strikes(spot, side):
        contract = bt.lab_occ(sym, day, cp, strike)
        rec = opt.get((day, contract))
        if rec is None:
            continue
        if not (rec["real"][minute] and np.isfinite(rec["open"][minute]) and float(rec["open"][minute]) >= sc.MIN_PREMIUM):
            continue
        saw = True
        raw = float(rec["open"][minute])
        quotes.append((strike, entry_ask(raw), contract, rec, raw))
    return float(spot), quotes, saw


def choose_fill(sess, opt, day, sym, minute, side):
    """Lock the entry minute. Slip one minute only when no strike has a print.

    A print whose ask is outside $0.45–$1.00 does not move the clock.
    """
    minute = int(minute)
    for m in (minute, minute + 1):
        if m < fg.ENTRY_LO or m > fg.ENTRY_HI or m >= sc.FLAT_MIN:
            continue
        spot, quotes, saw = _quotes_at(sess, opt, day, sym, m, side)
        if not saw:
            continue
        picked = pick_ask([(k, a) for k, a, _c, _r, _raw in quotes], spot)
        if picked is None:
            return {"status": "premium", "fill_minute": m}
        strike, ask = picked
        match = next(q for q in quotes if q[0] == strike and q[1] == ask)
        _k, _a, contract, rec, raw = match
        return {
            "status": "fill",
            "fill_minute": m,
            "strike": strike,
            "ask": ask,
            "contract": contract,
            "rec": rec,
            "raw": raw,
        }
    return {"status": "no_print"}


def _exit_pack(rec, fill_min, tf, path):
    step = HOLD_BARS * int(tf)
    hold = sc.simulate_trade(rec, int(fill_min), (100.0, None, step), wc.COSTS, allow_slip=False, premium=None)
    fixed = sc.simulate_trade(rec, int(fill_min), (0.15, 0.25, 10_000), wc.COSTS, allow_slip=False, premium=None)
    be = wc.breakeven_trade(rec, int(fill_min))
    minute, touched = touch_minute(path, int(fill_min), tf)
    touch_net = wv.sale_net(rec, int(fill_min), minute)
    pack = {}
    for name, res in (("hold20", hold), ("tp15_sl25", fixed), ("be_a15", be)):
        net, why = wc._result_net(res)
        pack[name] = {"net": net, "why": why}
    pack["vwap_touch"] = {"net": touch_net, "why": "vwap" if touched else "time", "minute": minute, "touched": touched}
    return pack


def score_signals(signals, und, opt, symbols, score_days, paths):
    cache = {}

    def one(day_i, sym_i, minute, side, tf):
        key = (day_i, sym_i, None if minute is None else int(minute), int(side), int(tf))
        if key in cache:
            return cache[key]
        if minute is None:
            cache[key] = {"status": "no_print"}
            return cache[key]
        day = score_days[day_i]
        sess = und[symbols[sym_i]].get(day)
        if sess is None:
            cache[key] = {"status": "no_print"}
            return cache[key]
        chosen = choose_fill(sess, opt, day, symbols[sym_i], int(minute), int(side))
        if chosen.get("status") == "fill":
            chosen["exits"] = _exit_pack(chosen["rec"], chosen["fill_minute"], tf, paths.get(int(tf), {}).get((symbols[sym_i], day)))
        cache[key] = chosen
        return chosen

    for sig in signals:
        got = one(sig["day_i"], sig["sym_i"], sig["entry_minute"], sig["side"], sig["tf"])
        sig["chosen"] = got
        rnd = sig.get("rnd_minute")
        sig["rnd_chosen"] = one(sig["day_i"], sig["sym_i"], rnd, sig["side"], sig["tf"]) if rnd is not None else {"status": "no_print"}


def _conf_ok(sig, name):
    if name == "base":
        return True
    if name == "mom_turn":
        return bool(sig["mom_turn"])
    if name == "first_drop":
        return bool(sig["first_drop"])
    raise ValueError(name)


def _net(chosen, exit_name):
    if not chosen or chosen.get("status") != "fill":
        return float("nan")
    return (chosen.get("exits") or {}).get(exit_name, {}).get("net", float("nan"))


def _row_stats(sigs, exit_name, n_days, train, test, n_boot, seed):
    nets, days, rnd = [], [], []
    skipped = 0
    for sig in sigs:
        if sig.get("chosen", {}).get("status") == "premium":
            skipped += 1
        value = _net(sig.get("chosen"), exit_name)
        if wc._finite(value):
            nets.append(float(value))
            days.append(sig["day_i"])
        random_value = _net(sig.get("rnd_chosen"), exit_name)
        if wc._finite(random_value):
            rnd.append(float(random_value))
    packed = wc._pack_stats(nets, days, n_days, n_boot, seed)
    train_nets = [v for v, d in zip(nets, days) if d in train]
    hold_nets = [v for v, d in zip(nets, days) if d in test]
    return {
        "n": packed["n"],
        "sessions": packed["sessions"],
        "mean_net": packed["mean"],
        "win": packed["win"],
        "median": packed["median"],
        "worst": packed["worst"],
        "ci_lo": packed["ci_lo"],
        "ci_hi": packed["ci_hi"],
        "train_n": len(train_nets),
        "train_mean": wc._mean(train_nets),
        "hold_n": len(hold_nets),
        "hold_mean": wc._mean(hold_nets),
        "random_n": len(rnd),
        "random_mean": wc._mean(rnd),
        "skipped_premium": skipped,
    }


def summary_rows(signals, n_days, train_idx, test_idx, n_boot):
    train = set(int(i) for i in train_idx)
    test = set(int(i) for i in test_idx)
    rows = []
    for tf in TFS:
        for max_level in MAX_LEVELS:
            for opp in OPP_LEVELS:
                for side in (1, -1):
                    name = variant_id(tf, max_level, opp, side)
                    pool = [
                        s for s in signals
                        if s["tf"] == tf and s["max_level"] == max_level and s["opp"] == opp and s["side"] == side
                    ]
                    for conf in CONFLUENCE:
                        group = [s for s in pool if _conf_ok(s, conf)]
                        for exit_name in EXITS:
                            stats = _row_stats(
                                group, exit_name, n_days, train, test, n_boot,
                                sc.stream_seed("vwap-trend-fade", name, conf, exit_name),
                            )
                            rows.append({"variant": name, "confluence": conf, "exit": exit_name, **stats})
    return rows


def _md(headers, body):
    head = "| " + " | ".join(headers) + " |"
    rule = "| " + " | ".join("---" for _ in headers) + " |"
    lines = ["| " + " | ".join(str(c) for c in row) + " |" for row in body]
    return "\n".join([head, rule, *lines])


def _body(rows):
    out = []
    for row in rows:
        out.append([
            row["variant"], row["confluence"], row["exit"],
            row["n"], row["sessions"],
            wc._fmt(row["mean_net"]), wc._fmt(row["win"]), wc._fmt(row["median"]), wc._fmt(row["worst"]),
            wc._fmt(row["ci_lo"]), wc._fmt(row["ci_hi"]),
            row["train_n"], wc._fmt(row["train_mean"]),
            row["hold_n"], wc._fmt(row["hold_mean"]),
            row["random_n"], wc._fmt(row["random_mean"]),
            row["skipped_premium"],
        ])
    return out


def _cell(rows, variant, conf, exit_name):
    for row in rows:
        if row["variant"] == variant and row["confluence"] == conf and row["exit"] == exit_name:
            return row
    return None


def verdict_paragraph(rows, meta):
    bits = []
    for side in ("long", "short"):
        name = f"tf1_max95_opp30_{side}"
        hold = _cell(rows, name, "base", "hold20")
        touch = _cell(rows, name, "base", "vwap_touch")
        if hold is None:
            continue
        bits.append(
            f"{side} tf1 max95 opp30 base hold20 n {hold['n']} mean {wc._fmt(hold['mean_net'])}% "
            f"win {wc._fmt(hold['win'])}% random {wc._fmt(hold['random_mean'])}% "
            f"held-out n {hold['hold_n']} mean {wc._fmt(hold['hold_mean'])}% "
            f"skipped for premium {hold['skipped_premium']}"
        )
        if touch is not None:
            bits.append(f"{side} VWAP touch mean {wc._fmt(touch['mean_net'])}%")
    text = " ".join(bits) + "." if bits else "No tf1 max95 opposite-at-most-30 base row was scored."
    if meta.get("synthetic"):
        text += " Prices in this file are synthetic, not a market."
    text += " Held-out is the last 25% of sessions and was not used to choose the rule. This is not a reason to trade."
    return text


def render_report(rows, meta, failures):
    parts = [
        "# Vix Fix + VWAP trend fade",
        "",
        "Raw numbers are first. The last paragraph is the only prose.",
        "",
        _md(STAT_HEADERS, _body(rows)),
        "",
        "Short: the prior bar has greed at or above the max and fear at or below the opposite cap, "
        "this bar both fear and greed print lower than the prior bar, the 5-bar session-VWAP slope is down, and the close is above VWAP. "
        "Long is the mirror: fear maxed, greed quiet, VWAP slope up, close below VWAP. "
        "Signal bars are 9:40 through 15:00 ET. The fill is the next bar's open. "
        "1-minute and 2-minute bars are both scored. The 2-minute bars are the 1-minute bars aggregated. A 20-bar hold on the 2-minute chart is 40 minutes. "
        "mom_turn keeps a signal whose squeeze momentum was moving against the fade and turns toward it on this bar or one of the prior 3. "
        "first_drop keeps a signal where the maxed side's prior bar was not already falling. "
        "Those two are separate rows. base is every signal. "
        "The contract is the call (long) or put (short), a few strikes in the money through 25 points out, "
        "whose ask (print plus half-spread) is inside $0.45–$1.00 and closest to $0.65. "
        "skipped_premium is how many signals in that row had prints and none of them landed in that window. "
        "Train is the first 75% of sessions. The bootstrap CI is the day-clustered 95% interval of the mean.",
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
        f"Runtime {wc._fmt(meta.get('runtime_min'), 1)} minutes."
    )
    parts.append("")
    parts.append(verdict_paragraph(rows, meta))
    parts.append("")
    return "\n".join(parts)


def trade_rows(signals, symbols, score_days, train_idx):
    train = set(int(i) for i in train_idx)
    rows = []
    for sig in signals:
        chosen = sig.get("chosen") or {}
        if chosen.get("status") not in ("fill", "premium"):
            continue
        exits = chosen.get("exits") or {}
        rnd = sig.get("rnd_chosen") or {}
        rnd_ex = rnd.get("exits") or {}
        touch = exits.get("vwap_touch") or {}
        rows.append({
            "day": score_days[sig["day_i"]].isoformat(),
            "symbol": symbols[sig["sym_i"]],
            "tf": sig["tf"],
            "clock": fg.clock_hhmm(sig["signal_minute"]),
            "side": "long" if sig["side"] == 1 else "short",
            "max_level": sig["max_level"],
            "opp": sig["opp"],
            "confluence_mom": wc._flag(sig["mom_turn"]),
            "confluence_first": wc._flag(sig["first_drop"]),
            "split": "train" if sig["day_i"] in train else "hold",
            "contract": chosen.get("contract", ""),
            "strike": chosen.get("strike", ""),
            "ask": wc._fmt(chosen.get("ask"), 4),
            "raw": wc._fmt(chosen.get("raw"), 4),
            "skip": "" if chosen.get("status") == "fill" else chosen.get("status", ""),
            "net_hold20": wc._fmt((exits.get("hold20") or {}).get("net"), 4),
            "net_tp15_sl25": wc._fmt((exits.get("tp15_sl25") or {}).get("net"), 4),
            "net_be_a15": wc._fmt((exits.get("be_a15") or {}).get("net"), 4),
            "net_vwap_touch": wc._fmt(touch.get("net"), 4),
            "touch": wc._flag(touch.get("touched")),
            "rnd_minute": "" if sig.get("rnd_minute") is None else int(sig["rnd_minute"]),
            "rnd_net_hold20": wc._fmt((rnd_ex.get("hold20") or {}).get("net"), 4),
            "rnd_net_tp15_sl25": wc._fmt((rnd_ex.get("tp15_sl25") or {}).get("net"), 4),
            "rnd_net_be_a15": wc._fmt((rnd_ex.get("be_a15") or {}).get("net"), 4),
            "rnd_net_vwap_touch": wc._fmt((rnd_ex.get("vwap_touch") or {}).get("net"), 4),
        })
    return rows


def write_outputs(out_dir, report, trades):
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "VWAP_TREND_FADE.md")
    with open(path, "w") as handle:
        handle.write(report)
    csv_path = os.path.join(out_dir, "vwap_trend_fade_trades.csv")
    with open(csv_path, "w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=TRADE_FIELDS, extrasaction="ignore")
        writer.writeheader()
        for row in trades:
            writer.writerow(row)
    return path


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
    }
    signals = _stage("signals", lambda: signals_from_frames(frames, symbols, score_days), failures)
    if signals is None:
        signals = []
    meta["n_signals"] = len(signals)
    _log(f"  signals {len(signals)}")
    paths = {}
    for tf in TFS:
        built = _stage(f"vwap paths tf{tf}", lambda tf=tf: session_paths(frames, symbols, score_days, tf), failures)
        paths[tf] = built or {}

    def _download():
        if opt is not None:
            return opt
        needed = needed_contracts(signals, und, symbols, score_days)
        _log(f"  option days {len(needed)} contract-days {sum(len(v) for v in needed.values())}")
        return eh.fetch_option_days(
            needed, und, symbols, synthetic,
            cache_dir or "/tmp/vwap-trend-fade-cache",
            workers=max(1, int(workers)),
        )

    if signals:
        got = _stage("download", _download, failures)
        if got is None:
            got = {}
        _stage("fills", lambda: score_signals(signals, und, got, symbols, score_days, paths), failures)

    rows = _stage(
        "summarize",
        lambda: summary_rows(signals, len(score_days), train_idx, test_idx, n_boot),
        failures,
    )
    if rows is None:
        rows = []
    meta["runtime_min"] = (time.time() - t0) / 60.0
    report = render_report(rows, meta, failures)
    trades = trade_rows(signals, symbols, score_days, train_idx)
    return {
        "report": report, "rows": rows, "trades": trades, "meta": meta, "failures": failures,
    }


def _empty(meta, message, failures):
    text = render_report([], meta, failures)
    return text.replace("Raw numbers are first.", "Raw numbers are first.\n\n" + message, 1)


def _env_flag(name):
    return os.getenv(name, "").strip().lower() in {"1", "true", "yes", "y"}


def _env_int(name, default):
    raw = os.getenv(name, "").strip()
    return int(raw) if raw else default


def main():
    t0 = time.time()
    out_dir = os.getenv("VTF_OUT", "results").strip() or "results"
    os.makedirs(out_dir, exist_ok=True)
    synthetic = _env_flag("VTF_SYNTH")
    blank = {"n_sessions": 0, "n_signals": 0, "synthetic": synthetic, "runtime_min": 0.0, "first_day": "", "last_day": ""}
    if not synthetic and not wc.keys_ready():
        write_outputs(out_dir, _empty(blank, fg.MISSING_KEYS, [("keys", fg.MISSING_KEYS)]), [])
        _log(f"STAGE keys failed: {fg.MISSING_KEYS}")
        return 1
    days_n = _env_int("VTF_DAYS", 120)
    if days_n < 6:
        message = f"Need at least 6 sessions. Got {days_n}."
        write_outputs(out_dir, _empty(blank, message, [("days", message)]), [])
        _log(f"STAGE days failed: {message}")
        return 1
    symbols = [s.strip().upper() for s in os.getenv("VTF_SYMBOLS", "SPY").split(",") if s.strip()]
    if not symbols:
        _log("STAGE symbols failed: symbols is empty")
        return 1
    now = datetime.now(NY)
    end = datetime.now(timezone.utc) - timedelta(minutes=20)
    start = (pd.Timestamp(now.date(), tz=NY) - pd.Timedelta(days=int(days_n * 3 + 30))).tz_convert("UTC").to_pydatetime()
    _log(f"vwap-trend-fade symbols {', '.join(symbols)} days {days_n} synthetic {int(synthetic)}")
    try:
        frames = sc._load_underlying(symbols, start, end, synthetic)
        und = {sym: sc.rth_session(df) for sym, df in frames.items()}
        all_days = sc.complete_days(und, symbols, now)
    except (Exception, SystemExit) as exc:
        traceback.print_exc()
        write_outputs(out_dir, _empty(blank, str(exc), [("load", str(exc))]), [])
        _log(f"STAGE load failed: {exc}")
        return 1
    if len(all_days) < 6:
        message = "Not enough completed sessions to score."
        write_outputs(out_dir, _empty(blank, message, [("sessions", message)]), [])
        _log(f"STAGE sessions failed: {message}")
        return 1
    score_days = all_days[-days_n:]
    _log(f"  sessions {score_days[0]} .. {score_days[-1]} n {len(score_days)}")
    result = run_study(
        frames, symbols, score_days, und,
        synthetic=synthetic,
        cache_dir=os.getenv("VTF_CACHE", "/tmp/vwap-trend-fade-cache").strip() or "/tmp/vwap-trend-fade-cache",
        workers=_env_int("VTF_WORKERS", 4),
        n_boot=_env_int("VTF_BOOT", 1000),
    )
    result["meta"]["runtime_min"] = (time.time() - t0) / 60.0
    result["report"] = render_report(result["rows"], result["meta"], result["failures"])
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
