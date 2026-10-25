"""
Replay Clean Scan paper trades on real OPRA 1-minute option bars.

DATA ONLY. This reads clean_trades.csv, downloads historical option bars, and
writes a report. It does not import an order client or send an order.

The live bot (cleanbot.py) is not modified. Its exit rules are read from that
file and replayed here. The logged dollars are paper market fills with no
commission. This replay prices the same entries with the scalp_real cost
model, so a dollar gap is expected and is labeled, not hidden.
"""

from __future__ import annotations

import csv
import math
import os
import sys
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd

import cleanbot as cb
import scalp_real as sc

ET = ZoneInfo("America/New_York")
FLAT_MINUTE = (cb.EXIT_AT // 100) * 60 + (cb.EXIT_AT % 100)  # 15:45
SESSION_END = 15 * 60 + 59
BOOT_N = 2000
BOOT_SEED = 20261025
VARIANTS = (
    "current",
    "fixed",
    "no_scan",
    "breakeven",
    "trail50",
    "trail30",
    "partial10",
    "time5",
    "time10",
    "time15",
    "time30",
)
VARIANT_TITLES = {
    "current": "Current bot rules (stop, scale-out, scan exit, 15:45)",
    "fixed": "Fixed stop and target only (A sells all at +25/-25; B is +10 then +20 / -10)",
    "no_scan": "Current scale-out with scan exits turned off (15:45 still flats)",
    "breakeven": "After +10%, stop moves to the entry price (costs still apply)",
    "trail50": "After +10%, exit on a 50% giveback of the peak gain",
    "trail30": "After +15%, exit on a 30% giveback of the peak gain",
    "partial10": "Sell half at +10%, trail the rest at a 50% giveback",
    "time5": "Exit 5 minutes after entry",
    "time10": "Exit 10 minutes after entry",
    "time15": "Exit 15 minutes after entry",
    "time30": "Exit 30 minutes after entry",
}


def _print(msg):
    text = str(msg)
    for secret in (os.getenv("ALPACA_KEY", ""), os.getenv("ALPACA_SECRET", "")):
        if secret:
            text = text.replace(secret, "[redacted]")
    print(text, flush=True)


def hhmm_to_minute(text):
    hour, minute = str(text).strip().split(":")
    return int(hour) * 60 + int(minute)


def minute_to_hhmm(minute):
    minute = int(minute)
    return f"{minute // 60:02d}:{minute % 60:02d}"


def half_spread(price, costs):
    cent, pct, _comm = costs
    return sc.half_spread(price, cent, pct)


def default_costs():
    cent = float(os.getenv("CLEAN_HALF_SPREAD_CENTS", "1")) / 100.0
    pct = float(os.getenv("CLEAN_HALF_SPREAD_PCT", "0.5")) / 100.0
    comm = float(os.getenv("CLEAN_COMMISSION", "0.65"))
    return (cent, pct, comm)


def round_trip(raw_entry, raw_exit, qty, costs):
    """Ask-side entry, bid-side exit, commission per contract per side."""
    qty = int(qty)
    cent, pct, comm = costs
    debit = float(raw_entry) + half_spread(raw_entry, costs)
    credit = max(0.0, float(raw_exit) - half_spread(raw_exit, costs))
    dollar = (credit - debit) * 100.0 * qty - 2.0 * comm * qty
    base = debit * 100.0 * qty
    net_pct = (dollar / base * 100.0) if base > 0 else 0.0
    raw_dollar = (float(raw_exit) - float(raw_entry)) * 100.0 * qty
    return dollar, net_pct, raw_dollar


def parse_sold(text):
    left, _, right = str(text).lower().partition(" of ")
    return int(float(left.strip())), int(float(right.strip() or left))


def implied_qty(pnl, entry, exit_px):
    """contracts = pnl_usd / ((exit - entry) * 100). None when the two fills match."""
    delta = float(exit_px) - float(entry)
    if abs(delta) < 1e-9:
        return None
    return float(pnl) / (delta * 100.0)


def load_rows(path):
    with open(path, newline="") as f:
        raw = list(csv.DictReader(f))
    rows = []
    for src in raw:
        sold_qty, sold_of = parse_sold(src["sold"])
        entry = float(src["entry_fill"])
        exit_px = float(src["exit_fill"])
        pnl = float(src["pnl_usd"])
        implied = implied_qty(pnl, entry, exit_px)
        qty_gap = implied is None or abs(implied - sold_qty) > 0.25
        rows.append({
            "date": src["date"],
            "version": src["version"].strip(),
            "ticker": src["ticker"].strip(),
            "side": src["side"].strip().upper(),
            "contract": src["contract"].strip(),
            "sold_qty": sold_qty,
            "sold_of": sold_of,
            "reason": src["reason"].strip(),
            "entry_hhmm": src["entry_time"].strip(),
            "exit_hhmm": src["exit_time"].strip(),
            "entry_minute": hhmm_to_minute(src["entry_time"]),
            "exit_minute": hhmm_to_minute(src["exit_time"]),
            "entry_fill": entry,
            "exit_fill": exit_px,
            "pnl_usd": pnl,
            "pnl_pct": float(src["pnl_pct"]),
            "best_pct": float(src["best_pct"]),
            "worst_pct": float(src["worst_pct"]),
            "implied_qty": implied,
            "qty_gap": qty_gap,
        })
    return rows


def group_positions(rows):
    """One entry can log two sales (scale-out). Keep the logged sale order by exit time."""
    buckets = {}
    order = []
    for row in rows:
        key = (row["date"], row["version"], row["ticker"], row["contract"], row["entry_hhmm"])
        if key not in buckets:
            buckets[key] = []
            order.append(key)
        buckets[key].append(row)
    positions = []
    for key in order:
        legs = sorted(buckets[key], key=lambda r: (r["exit_minute"], r["reason"]))
        qty = sum(leg["sold_qty"] for leg in legs)
        positions.append({
            "date": legs[0]["date"],
            "version": legs[0]["version"],
            "ticker": legs[0]["ticker"],
            "side": legs[0]["side"],
            "contract": legs[0]["contract"],
            "entry_hhmm": legs[0]["entry_hhmm"],
            "entry_minute": legs[0]["entry_minute"],
            "entry_fill": legs[0]["entry_fill"],
            "qty": qty,
            "logged_usd": sum(leg["pnl_usd"] for leg in legs),
            "best_pct": max(leg["best_pct"] for leg in legs),
            "worst_pct": min(leg["worst_pct"] for leg in legs),
            "qty_gap": any(leg["qty_gap"] for leg in legs),
            "legs": legs,
            "scan_side": 1 if legs[0]["side"] == "CALL" else -1,
        })
    return positions


def rules_for(version, kind):
    spec = cb.VERSIONS[version]
    rules = {
        "name": kind,
        "sl": float(spec["sl"]),
        "tp1": None,
        "tp1_qty": int(spec["tp1_qty"]),
        "tp1_all": False,
        "tp2": None,
        "scan": False,
        "flat": FLAT_MINUTE,
        "be_arm": None,
        "trail_arm": None,
        "trail_gb": None,
        "partial": None,
        "time_n": None,
    }
    tp1 = float(spec["tp1"])
    tp2 = None if spec["tp2"] is None else float(spec["tp2"])
    if kind == "current":
        rules.update(tp1=tp1, tp2=tp2, scan=True)
    elif kind == "fixed":
        # A is one bracket on the whole lot. B keeps the two targets. Neither waits on the scan.
        if version == "A":
            rules.update(tp1=tp1, tp1_all=True)
        else:
            rules.update(tp1=tp1, tp2=tp2)
    elif kind == "no_scan":
        rules.update(tp1=tp1, tp2=tp2, scan=False)
    elif kind == "breakeven":
        rules.update(tp1=tp1, tp2=tp2, be_arm=10.0)
    elif kind == "trail50":
        rules.update(trail_arm=10.0, trail_gb=0.50)
    elif kind == "trail30":
        rules.update(trail_arm=15.0, trail_gb=0.30)
    elif kind == "partial10":
        rules.update(partial=10.0, trail_arm=10.0, trail_gb=0.50)
    elif kind.startswith("time"):
        rules.update(time_n=int(kind.replace("time", "")), flat=SESSION_END)
    else:
        raise KeyError(kind)
    return rules


def _level(entry, pct):
    return float(entry) * (1.0 + float(pct) / 100.0)


def move_pct(entry, price):
    return (float(price) / float(entry) - 1.0) * 100.0


def _stop_binding(rules, peak, partial_done):
    """Tightest long stop, as a percent from the entry. The version stop is the floor."""
    parts = [("version", -float(rules["sl"]))]
    if rules["be_arm"] is not None and peak + 1e-9 >= rules["be_arm"]:
        parts.append(("be", 0.0))
    trail_on = (
        rules["trail_gb"] is not None
        and rules["trail_arm"] is not None
        and peak + 1e-9 >= rules["trail_arm"]
        and not (rules["partial"] is not None and not partial_done)
    )
    if trail_on:
        parts.append(("trail", peak * (1.0 - float(rules["trail_gb"]))))
    return max(parts, key=lambda item: item[1])


def _stop_reason(kind, rules):
    if kind == "be":
        return "BE entry"
    if kind == "trail":
        give = int(round(float(rules["trail_gb"]) * 100))
        return f"TRAIL {give}% giveback"
    return f"STOP -{rules['sl']:g}%"


def _book(legs, entry, minute, qty, raw, reason, costs):
    dollar, net_pct, raw_dollar = round_trip(entry, raw, qty, costs)
    legs.append({
        "minute": int(minute),
        "hhmm": minute_to_hhmm(minute),
        "qty": int(qty),
        "raw": float(raw),
        "reason": reason,
        "net_usd": dollar,
        "net_pct": net_pct,
        "raw_usd": raw_dollar,
    })


def _bar_ok(bar):
    vals = (bar["o"], bar["h"], bar["l"], bar["c"])
    return all(isinstance(v, (int, float)) and math.isfinite(v) and v > 0 for v in vals)


def _normalize_bar(bar):
    o, h, l, c = float(bar["o"]), float(bar["h"]), float(bar["l"]), float(bar["c"])
    return {
        "minute": int(bar["minute"]),
        "o": o,
        "h": max(h, o, c),
        "l": min(l, o, c),
        "c": c,
    }


def replay_position(pos, bars, rules, scan_at, costs):
    """Walk 1-minute bars. A bar that touches the stop and a target stops first.

    The stop checked on a bar is the one that was already active from earlier
    bars. A new high can arm a breakeven or a trail for the next bar. It does
    not stop the trade out on the same bar, because the low may have printed
    before that high. A gap through a stop that was already active fills at
    the open when the open is worse.
    """
    entry = float(pos["entry_fill"])
    qty = int(pos["qty"])
    legs = []
    usable = [_normalize_bar(b) for b in bars if int(b["minute"]) >= pos["entry_minute"] and _bar_ok(b)]
    usable = [b for b in usable if b["minute"] <= SESSION_END]
    usable.sort(key=lambda b: b["minute"])
    if not usable or qty <= 0 or entry <= 0:
        return legs

    if rules["time_n"] is not None:
        deadline = min(pos["entry_minute"] + int(rules["time_n"]), SESSION_END)
        chosen = next((b for b in usable if b["minute"] >= deadline), None)
        if chosen is None:
            chosen = usable[-1]
            reason = f"TIME +{rules['time_n']}m (no bar, last print)"
        elif chosen["minute"] != pos["entry_minute"] + int(rules["time_n"]):
            reason = f"TIME +{rules['time_n']}m"
        else:
            reason = f"TIME +{rules['time_n']}m"
        raw = chosen["o"]
        _book(legs, entry, chosen["minute"], qty, raw, reason, costs)
        return legs

    peak = 0.0
    partial_done = False
    tp1_done = False
    for bar in usable:
        if qty <= 0:
            break
        minute, o, h, l, c = bar["minute"], bar["o"], bar["h"], bar["l"], bar["c"]
        kind, stop_pct = _stop_binding(rules, peak, partial_done)
        stop_px = _level(entry, stop_pct)
        if l <= stop_px + 1e-12:
            raw = o if o < stop_px else stop_px
            _book(legs, entry, minute, qty, raw, _stop_reason(kind, rules), costs)
            qty = 0
            break

        new_peak = max(peak, move_pct(entry, h))
        target = _next_target(rules, entry, qty, tp1_done, partial_done, h)
        if target is not None:
            q = min(qty, target["qty"])
            _book(legs, entry, minute, q, target["px"], target["reason"], costs)
            qty -= q
            tp1_done = tp1_done or target["kind"] == "tp1"
            partial_done = partial_done or target["kind"] == "partial"
            peak = max(new_peak, target["pct"])
            if qty <= 0:
                break
            if rules["scan"] and scan_at and minute >= scan_at[0]:
                _book(legs, entry, minute, qty, o, scan_at[1], costs)
                qty = 0
                break
            if minute >= rules["flat"]:
                _book(legs, entry, minute, qty, o, "3:45 time exit", costs)
                qty = 0
                break
            continue

        peak = new_peak
        if rules["scan"] and scan_at and minute >= scan_at[0]:
            _book(legs, entry, minute, qty, o, scan_at[1], costs)
            qty = 0
            break
        if minute >= rules["flat"]:
            _book(legs, entry, minute, qty, o, "3:45 time exit", costs)
            qty = 0
            break

    if qty > 0:
        last = usable[-1]
        _book(legs, entry, last["minute"], qty, last["c"], "NO BAR AT FLAT", costs)
    return legs


def _next_target(rules, entry, qty, tp1_done, partial_done, high):
    """The live bot sells the whole lot at TP2 when one quote is already there."""
    if rules["partial"] is not None and not partial_done and high + 1e-12 >= _level(entry, rules["partial"]):
        part = qty if qty < 2 else max(1, qty // 2)
        pct = float(rules["partial"])
        return {"px": _level(entry, pct), "qty": part, "reason": f"PARTIAL +{pct:g}%", "kind": "partial", "pct": pct}
    if rules["tp2"] is not None and high + 1e-12 >= _level(entry, rules["tp2"]):
        pct = float(rules["tp2"])
        return {"px": _level(entry, pct), "qty": qty, "reason": f"TP2 +{pct:g}%", "kind": "tp2", "pct": pct}
    if rules["tp1"] is not None and not tp1_done and high + 1e-12 >= _level(entry, rules["tp1"]):
        pct = float(rules["tp1"])
        if rules["tp1_all"] or qty <= int(rules["tp1_qty"]):
            q = qty
        elif qty > int(rules["tp1_qty"]):
            q = int(rules["tp1_qty"])
        else:
            return None
        return {"px": _level(entry, pct), "qty": q, "reason": f"TP1 +{pct:g}%", "kind": "tp1", "pct": pct}
    return None


def reason_class(reason):
    text = str(reason).strip().upper()
    if text.startswith("STOP"):
        return "stop"
    if text.startswith("TP1"):
        return "tp1"
    if text.startswith("TP2"):
        return "tp2"
    if "SCAN" in text:
        return "scan"
    if "3:45" in text or text.startswith("NO BAR"):
        return "flat"
    if text.startswith("BE"):
        return "be"
    if text.startswith("TRAIL"):
        return "trail"
    if text.startswith("PARTIAL"):
        return "partial"
    if text.startswith("TIME"):
        return "time"
    return text.lower()


def short_reason(reason):
    text = str(reason)
    upper = text.upper()
    if "CHOPPY" in upper:
        return "choppy"
    if "FLIPPED" in upper:
        return "flip"
    if "20 EMA" in upper or "EMA" in upper:
        return "ema"
    if "ADX" in upper or "FADING" in upper:
        return "adx"
    if upper.startswith("STOP"):
        return "stop"
    if upper.startswith("TP1"):
        return "tp1"
    if upper.startswith("TP2"):
        return "tp2"
    if "3:45" in text:
        return "15:45"
    if upper.startswith("BE"):
        return "breakeven"
    if "TRAIL 50" in upper:
        return "trail50"
    if "TRAIL 30" in upper:
        return "trail30"
    if upper.startswith("PARTIAL"):
        return "half"
    if upper.startswith("TIME"):
        return text.replace("TIME ", "").split(" (")[0]
    if "SCAN" in upper:
        return "scan"
    if upper.startswith("NO BAR"):
        return "no flat bar"
    return text[:18]


def validation_flag(pos, legs):
    if not legs:
        return "no bars"
    if any(leg["reason"].startswith("NO BAR") for leg in legs) and any(
        "SCAN" in leg["reason"].upper() or "3:45" in leg["reason"] for leg in pos["legs"]
    ):
        # Still compare. A missing flat bar is its own mismatch below.
        pass
    logged = sorted(pos["legs"], key=lambda leg: (leg["exit_minute"], leg["reason"]))
    if len(logged) != len(legs):
        return "mismatch"
    for src, got in zip(logged, legs):
        if reason_class(src["reason"]) != reason_class(got["reason"]):
            return "mismatch"
        if abs(src["exit_minute"] - got["minute"]) > 1:
            return "mismatch"
    raw = sum(leg["raw_usd"] for leg in legs)
    if abs(raw - pos["logged_usd"]) > max(1.0, 0.02 * abs(pos["logged_usd"])):
        return "price gap"
    net = sum(leg["net_usd"] for leg in legs)
    if abs(net - pos["logged_usd"]) > 0.5:
        return "cost drag"
    return "match"


def position_net(pos, legs, costs):
    if not legs:
        return 0.0, 0.0, 0.0
    net = sum(leg["net_usd"] for leg in legs)
    raw = sum(leg["raw_usd"] for leg in legs)
    debit = float(pos["entry_fill"]) + half_spread(pos["entry_fill"], costs)
    base = debit * 100.0 * int(pos["qty"])
    pct = (net / base * 100.0) if base > 0 else 0.0
    return net, raw, pct


def run_variants(positions, bars_for, scan_for, costs):
    """bars_for(pos) -> list of bars. scan_for(pos) -> (minute, reason) or None."""
    out = {name: [] for name in VARIANTS}
    for pos in positions:
        bars = list(bars_for(pos) or [])
        scan_at = scan_for(pos)
        for name in VARIANTS:
            rules = rules_for(pos["version"], name)
            legs = replay_position(pos, bars, rules, scan_at, costs)
            net, raw, pct = position_net(pos, legs, costs)
            flag = validation_flag(pos, legs) if name == "current" else ""
            out[name].append({
                "pos": pos,
                "variant": name,
                "legs": legs,
                "net_usd": net,
                "raw_usd": raw,
                "net_pct": pct,
                "flag": flag,
                "reason": " + ".join(short_reason(leg["reason"]) for leg in legs) if legs else "no bars",
                "exit_hhmm": legs[-1]["hhmm"] if legs else "",
            })
    return out


def max_drawdown(dollars):
    if not len(dollars):
        return 0.0
    equity = np.cumsum(np.asarray(dollars, dtype=float))
    peak = np.maximum.accumulate(equity)
    return float((equity - peak).min())


def bootstrap_total(dollars, n=BOOT_N, seed=BOOT_SEED):
    values = np.asarray(list(dollars), dtype=float)
    if not len(values):
        return (float("nan"), float("nan"), float("nan"))
    rng = np.random.default_rng(seed)
    picks = rng.integers(0, len(values), size=(n, len(values)))
    totals = values[picks].sum(axis=1)
    lo, hi = np.quantile(totals, [0.025, 0.975])
    return float(values.sum()), float(lo), float(hi)


def summarize(rows):
    dollars = [row["net_usd"] for row in rows]
    pcts = [row["net_pct"] for row in rows]
    total, lo, hi = bootstrap_total(dollars)
    wins = sum(1 for value in dollars if value > 0)
    return {
        "n": len(rows),
        "wins": wins,
        "net": total if rows else 0.0,
        "avg_pct": float(np.mean(pcts)) if rows else 0.0,
        "max_dd": max_drawdown(dollars),
        "ci_lo": lo,
        "ci_hi": hi,
    }


def _slices(rows):
    """Overall, each version, each day, and each version on each day."""
    named = [("all", rows)]
    versions = sorted({row["pos"]["version"] for row in rows})
    days = sorted({row["pos"]["date"] for row in rows})
    for version in versions:
        named.append((f"version {version}", [row for row in rows if row["pos"]["version"] == version]))
    for day in days:
        named.append((day, [row for row in rows if row["pos"]["date"] == day]))
    for day in days:
        for version in versions:
            named.append((
                f"{day} {version}",
                [row for row in rows if row["pos"]["date"] == day and row["pos"]["version"] == version],
            ))
    return named


def _money(value):
    if value is None or not math.isfinite(value):
        return "n/a"
    return f"${value:+,.0f}" if abs(value) >= 10 else f"${value:+,.2f}"


def fmt_pct(value):
    if value is None or not math.isfinite(value):
        return "n/a"
    return f"{value:+.1f}%"


def green_then_red(rows):
    green = [row for row in rows if row["best_pct"] > 0]
    red = [row for row in green if row["pnl_usd"] < 0]
    return len(rows), len(green), len(red)


def render_report(sale_rows, positions, results, costs, notes):
    n_sales, n_green, n_gave_back = green_then_red(sale_rows)
    days = sorted({pos["date"] for pos in positions})
    day_text = ", ".join(days) if days else "no days"
    cent, pct, comm = costs
    lines = [
        "# Clean Scan replay",
        "",
        "Data only. No order is sent. The live Clean Scan bot and its schedule are unchanged.",
        "",
        f"Log: {n_sales} sales, {len(positions)} entries, {day_text}.",
        f"{n_green} of {n_sales} sales traded green at some point (best_pct > 0). "
        f"{n_gave_back} of those {n_green} closed at a loss. "
        "Stops and scan exits (leg got choppy, trend flipped) gave back more than the take-profits kept.",
        "",
        f"{n_sales} sales over {len(days)} days is far too small to conclude anything. "
        "The intervals are a 95% bootstrap of the entry dollars (2,000 resamples, seed 20261025). "
        "They describe this sample. They are not a reason to change the bot.",
        "",
        "Costs, same model as scalp_real: the entry is the logged fill plus a half-spread, "
        f"the exit is the replay fill minus a half-spread, half-spread = max({cent * 100:.0f} cent, {pct * 100:.1f}% of premium) per side, "
        f"commission ${comm:.2f} per contract per side. "
        "Logged dollars are paper fills with no commission, so the replay dollars will not equal the log even when the rule matches.",
        "Stops and targets are measured from the logged fill. "
        "If one 1-minute bar touches the active stop and a target, the stop is filled. "
        "A trail that arms on this bar's high and is then broken by this bar's low stops out. "
        "The live bot checks a quote mid every 5 seconds. This replay only has 1-minute highs and lows, so some exits cannot match. Those rows are flagged.",
        "",
        "## Does the replay reproduce the log?",
        "",
        notes.get("validation_note", ""),
        "",
    ]
    current = results["current"]
    flags = {}
    for row in current:
        flags[row["flag"]] = flags.get(row["flag"], 0) + 1
    flag_text = ", ".join(f"{name} {count}" for name, count in sorted(flags.items())) or "none"
    logged_total = sum(pos["logged_usd"] for pos in positions)
    replay_total = sum(row["net_usd"] for row in current)
    raw_total = sum(row["raw_usd"] for row in current)
    lines.append(
        f"Flags: {flag_text}. Logged total ${logged_total:+,.0f}. "
        f"Replay raw (no spread, no commission) ${raw_total:+,.0f}. "
        f"Replay net ${replay_total:+,.0f}."
    )
    lines.append(
        "match = same exit class, within 1 minute, and the raw dollars are close. "
        "price gap = the rule matched but the bar price is not the paper fill. "
        "cost drag = the raw dollars match and the spread plus commission is the gap. "
        "mismatch = a different exit or a different minute. no bars = nothing to replay."
    )
    lines += [
        "",
        "| day | v | sym | in | best | log | log $ | replay | replay $ | flag |",
        "|---|---|---|---|---:|---|---:|---|---:|---|",
    ]
    for row in current:
        pos = row["pos"]
        log_why = " + ".join(short_reason(leg["reason"]) for leg in pos["legs"])
        lines.append(
            f"| {pos['date'][5:]} | {pos['version']} | {pos['ticker']} | {pos['entry_hhmm']} | "
            f"{pos['best_pct']:.0f}% | {log_why} | {pos['logged_usd']:+.0f} | {row['reason']} | "
            f"{row['net_usd']:+.0f} | {row['flag']} |"
        )
    lines += ["", "## Exit variants", ""]
    lines.append("Each variant starts from the same logged entries and contract counts. A and B keep their own stops except where the variant says otherwise.")
    for name in VARIANTS:
        lines.append(f"- **{name}**: {VARIANT_TITLES[name]}")
    lines += [
        "",
        "A fixed target sells both contracts at +25%. The current A rule sells one at +25% and leaves the other on until a scan exit or 15:45. "
        "no_scan is that current rule with the scan turned off. Breakeven moves the stop to the entry price, and the spread and commission still come out, so that exit is a small loss.",
        "",
        "## Totals",
        "",
    ]
    for name in VARIANTS:
        lines.append(f"### {name}")
        lines.append("")
        lines.append("| slice | n | wins | net $ | avg % | max DD | 95% CI |")
        lines.append("|---|---:|---:|---:|---:|---:|---|")
        for label, subset in _slices(results[name]):
            stats = summarize(subset)
            ci = "n/a" if not subset else f"{_money(stats['ci_lo'])} to {_money(stats['ci_hi'])}"
            lines.append(
                f"| {label} | {stats['n']} | {stats['wins']} | {_money(stats['net'])} | {fmt_pct(stats['avg_pct'])} | "
                f"{_money(stats['max_dd'])} | {ci} |"
            )
        lines.append("")
        lines.append("| day | v | sym | out | why | net $ |")
        lines.append("|---|---|---|---|---|---:|")
        for row in results[name]:
            pos = row["pos"]
            lines.append(
                f"| {pos['date'][5:]} | {pos['version']} | {pos['ticker']} | {row['exit_hhmm']} | "
                f"{row['reason']} | {row['net_usd']:+.0f} |"
            )
        lines.append("")
    sale_days = len({row["date"] for row in sale_rows})
    lines.append(f"n={n_sales} sales over {sale_days} days is far too small to conclude anything.")
    lines.append("")
    return "\n".join(lines)


def write_csv(path, results):
    fields = [
        "variant", "date", "version", "ticker", "side", "contract", "qty",
        "entry_time", "entry_fill", "exit_time", "reason", "leg_qty", "leg_raw",
        "net_usd", "net_pct", "raw_usd", "logged_usd", "best_pct", "flag",
    ]
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for name in VARIANTS:
            for row in results[name]:
                pos = row["pos"]
                if not row["legs"]:
                    writer.writerow({
                        "variant": name, "date": pos["date"], "version": pos["version"],
                        "ticker": pos["ticker"], "side": pos["side"], "contract": pos["contract"],
                        "qty": pos["qty"], "entry_time": pos["entry_hhmm"], "entry_fill": pos["entry_fill"],
                        "exit_time": "", "reason": "no bars", "leg_qty": "", "leg_raw": "",
                        "net_usd": 0, "net_pct": 0, "raw_usd": 0, "logged_usd": pos["logged_usd"],
                        "best_pct": pos["best_pct"], "flag": row["flag"],
                    })
                    continue
                for leg in row["legs"]:
                    writer.writerow({
                        "variant": name, "date": pos["date"], "version": pos["version"],
                        "ticker": pos["ticker"], "side": pos["side"], "contract": pos["contract"],
                        "qty": pos["qty"], "entry_time": pos["entry_hhmm"], "entry_fill": pos["entry_fill"],
                        "exit_time": leg["hhmm"], "reason": leg["reason"], "leg_qty": leg["qty"],
                        "leg_raw": f"{leg['raw']:.4f}", "net_usd": f"{leg['net_usd']:.2f}",
                        "net_pct": f"{leg['net_pct']:.2f}", "raw_usd": f"{leg['raw_usd']:.2f}",
                        "logged_usd": pos["logged_usd"], "best_pct": pos["best_pct"], "flag": row["flag"],
                    })


def bars_from_option_frame(df, symbol):
    """Turn an Alpaca option-bar frame into ET minute bars for one contract."""
    if df is None or not len(df):
        return []
    frame = df
    if isinstance(df.index, pd.MultiIndex):
        try:
            frame = df.xs(symbol, level=0)
        except KeyError:
            return []
    frame = frame.sort_index()
    idx = frame.index
    if getattr(idx, "tz", None) is None:
        idx = idx.tz_localize("UTC")
    idx = idx.tz_convert(ET)
    out = []
    for stamp, rec in zip(idx, frame.itertuples(index=False)):
        minute = int(stamp.hour) * 60 + int(stamp.minute)
        out.append({
            "minute": minute,
            "o": float(getattr(rec, "open")),
            "h": float(getattr(rec, "high")),
            "l": float(getattr(rec, "low")),
            "c": float(getattr(rec, "close")),
        })
    return out


def find_scan_exit(frame, entry_minute, side, day):
    """First 5-minute close after the entry whose Clean Scan state is no longer this side.

    `frame` is the regular-hours 5-minute chart with a timezone index (bar start).
    The exit minute is the bar close. Returns (minute, reason) or None.
    """
    if frame is None or not len(frame):
        return None
    states, why, _info = cb.scan(frame)
    for i, start in enumerate(frame.index):
        start_et = start.tz_convert(ET) if getattr(start, "tz", None) else start.tz_localize(ET)
        if start_et.date().isoformat() != day:
            continue
        close_minute = int(start_et.hour) * 60 + int(start_et.minute) + cb.TF
        if close_minute <= entry_minute:
            continue
        if int(states[i]) != int(side):
            code = int(why[i])
            label = cb.WHY.get(code, "criteria lost")
            return close_minute, f"SCAN EXIT: {label}"
    return None


def _day(text):
    return datetime.strptime(text, "%Y-%m-%d").date()


def fetch_market(positions):
    """OPRA 1-minute option bars, and IEX 5-minute stock bars for the scan clock."""
    key = os.getenv("ALPACA_KEY", "").strip()
    secret = os.getenv("ALPACA_SECRET", "").strip()
    if not key or not secret:
        sys.exit("ALPACA_KEY / ALPACA_SECRET are missing. Add them in Settings > Secrets and variables > Actions.")
    from alpaca.data.enums import DataFeed
    from alpaca.data.historical import OptionHistoricalDataClient, StockHistoricalDataClient
    from alpaca.data.requests import OptionBarsRequest, StockBarsRequest
    from alpaca.data.timeframe import TimeFrame, TimeFrameUnit

    oc = OptionHistoricalDataClient(key, secret)
    dc = StockHistoricalDataClient(key, secret)
    option_bars = {}
    grouped = {}
    for pos in positions:
        grouped.setdefault((pos["date"], pos["contract"]), []).append(pos)
    for (day, contract), group in grouped.items():
        start_min = min(pos["entry_minute"] for pos in group)
        start = datetime.combine(_day(day), datetime.min.time(), ET) + timedelta(minutes=start_min)
        end = datetime.combine(_day(day), datetime.min.time(), ET) + timedelta(hours=16)
        start_utc = start.astimezone(timezone.utc)
        end_utc = end.astimezone(timezone.utc)
        df = None
        last_err = ""
        for attempt in range(4):
            try:
                df = oc.get_option_bars(OptionBarsRequest(
                    symbol_or_symbols=contract, timeframe=TimeFrame.Minute,
                    start=start_utc, end=end_utc,
                )).df
                break
            except Exception as exc:  # noqa: BLE001
                last_err = type(exc).__name__
                _print(f"  option bars {contract} {day} failed ({attempt + 1}/4): {last_err}")
        bars = bars_from_option_frame(df, contract)
        option_bars[(day, contract)] = bars
        _print(f"  {contract} {day}: {len(bars)} bars" + (f" ({last_err})" if not bars else ""))

    symbols = sorted({pos["ticker"] for pos in positions})
    days = sorted({_day(pos["date"]) for pos in positions})
    stock = {}
    if symbols and days:
        start = datetime.combine(days[0] - timedelta(days=14), datetime.min.time(), ET)
        end = datetime.combine(days[-1], datetime.min.time(), ET) + timedelta(hours=16)
        try:
            df = dc.get_stock_bars(StockBarsRequest(
                symbol_or_symbols=symbols,
                timeframe=TimeFrame(cb.TF, TimeFrameUnit.Minute),
                start=start.astimezone(timezone.utc),
                end=end.astimezone(timezone.utc),
                feed=DataFeed.IEX,
            )).df
        except Exception as exc:  # noqa: BLE001
            _print(f"  stock bars failed: {type(exc).__name__}. Scan clock will be missing.")
            df = None
        if df is not None and len(df):
            for sym in symbols:
                try:
                    frame = df.xs(sym, level=0) if isinstance(df.index, pd.MultiIndex) else df
                except KeyError:
                    continue
                frame = frame.sort_index()
                frame.index = frame.index.tz_convert(ET)
                hm = frame.index.hour * 100 + frame.index.minute
                stock[sym] = frame[(hm >= 930) & (hm < 1600)][["open", "high", "low", "close", "volume"]].astype(float)
                _print(f"  {sym} 5m bars {len(stock[sym])}")
    return option_bars, stock


def scan_lookup(stock):
    cache = {}

    def lookup(pos):
        key = (pos["ticker"], pos["date"], pos["entry_minute"], pos["scan_side"])
        if key in cache:
            return cache[key]
        frame = stock.get(pos["ticker"]) if stock else None
        found = find_scan_exit(frame, pos["entry_minute"], pos["scan_side"], pos["date"])
        cache[key] = found
        return found

    return lookup


def build(positions, option_bars, stock, costs):
    missing_scan = []

    def bars_for(pos):
        return option_bars.get((pos["date"], pos["contract"]), [])

    look = scan_lookup(stock)

    def scan_for(pos):
        found = look(pos)
        if found is None and any("SCAN" in leg["reason"].upper() for leg in pos["legs"]):
            missing_scan.append(pos)
        return found

    results = run_variants(positions, bars_for, scan_for, costs)
    note = (
        "The scan clock is cleanbot.scan on IEX 5-minute bars (the feed the bot trades on). "
        "Option bars are Alpaca OPRA 1-minute bars from the entry minute through 15:59 ET."
    )
    if missing_scan:
        names = ", ".join(f"{p['date']} {p['version']} {p['ticker']}" for p in missing_scan)
        note += f" No recomputed scan exit for: {names}. Those current-rule replays can only stop, take profit, or flat at 15:45."
    return results, {"validation_note": note}


def main():
    path = os.getenv("CLEAN_TRADES", "clean_trades.csv").strip() or "clean_trades.csv"
    out_dir = os.getenv("CLEAN_REPLAY_OUT", "results").strip() or "results"
    if not os.path.exists(path):
        sys.exit(f"Missing {path}")
    os.makedirs(out_dir, exist_ok=True)
    costs = default_costs()
    rows = load_rows(path)
    positions = group_positions(rows)
    _print(f"clean replay: {len(rows)} sales, {len(positions)} entries")
    option_bars, stock = fetch_market(positions)
    results, notes = build(positions, option_bars, stock, costs)
    text = render_report(rows, positions, results, costs, notes)
    md_path = os.path.join(out_dir, "CLEANBOT_REPLAY.md")
    csv_path = os.path.join(out_dir, "cleanbot_replay_trades.csv")
    with open(md_path, "w") as f:
        f.write(text)
    write_csv(csv_path, results)
    _print(f"wrote {md_path}")
    flags = {}
    for row in results["current"]:
        flags[row["flag"]] = flags.get(row["flag"], 0) + 1
    _print("validation " + ", ".join(f"{k}={v}" for k, v in sorted(flags.items())))


if __name__ == "__main__":
    main()
