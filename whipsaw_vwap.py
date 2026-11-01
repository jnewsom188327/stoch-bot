"""VWAP distance and VWAP-touch exit on the whipsaw signals. Data only. No orders.

Signals, the 1-strike OTM contract, and the ask/bid cost model come from
whipsaw_check.py. This file only adds the VWAP buckets and the touch exit.
"""

from __future__ import annotations

import csv
import os
import sys
import time
import traceback
from datetime import datetime, timedelta, timezone

import numpy as np

import edge_hunt as eh
import fgfade as fg
import scalp_real as sc
import whipsaw_check as wc

NY = wc.NY
BUCKETS = (
    ("below -4", lambda d: d < -4.0),
    ("-4 to -2", lambda d: -4.0 <= d < -2.0),
    ("-2 to 0", lambda d: -2.0 <= d < 0.0),
    ("0 to 2", lambda d: 0.0 <= d < 2.0),
    ("2 to 4", lambda d: 2.0 <= d < 4.0),
    ("4+", lambda d: d >= 4.0),
)
OTHERS = ("ge60", "ge30")
HOLD_BARS = 20

TRADE_FIELDS = [
    "day", "symbol", "clock", "side", "max_level", "other_value", "vwap_dist", "bucket",
    "far_side", "stretched_2", "split", "contract", "raw",
    "net_hold20", "net_vwap_touch", "touch", "touch_minute",
    "rnd_net_hold20", "rnd_net_vwap_touch", "und_atr_20",
]
STAT_HEADERS = [
    "variant", "slice", "exit", "n", "sessions", "mean_net", "win", "median", "worst",
    "ci_lo", "ci_hi", "train_n", "train_mean", "hold_n", "hold_mean", "random_n", "random_mean", "atr20",
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


def bucket_name(dist):
    """Signed ATR distance. Negative is against the trade (a fade). Positive is chasing."""
    if not wc._finite(dist):
        return ""
    for name, pred in BUCKETS:
        if pred(float(dist)):
            return name
    return ""


def far_side(dist):
    """Price starts against the trade, so VWAP is still in front of it."""
    return wc._finite(dist) and float(dist) < 0.0


def stretched_against(dist):
    """Two or more ATR against the trade. That is the below -4 and -4 to -2 buckets."""
    return wc._finite(dist) and float(dist) <= -2.0


def session_paths(frames, symbols, score_days):
    """High, low, and session VWAP on the session-minute grid, for the touch test."""
    keep = set(score_days)
    out = {}
    for sym in symbols:
        df = frames.get(sym)
        if df is None or not len(df):
            continue
        bars = fg.to_tf(df, 1)
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


def first_touch(path, start, cap):
    """First session minute in [start, cap] whose bar range touches that bar's VWAP.

    No touch returns `cap`. A missing path also returns `cap`.
    """
    start = int(start)
    cap = int(cap)
    if path is None or cap < start:
        return cap, False
    for m in range(start, cap + 1):
        if m < 0 or m >= sc.N_MIN:
            break
        vw = float(path["vwap"][m])
        hi = float(path["high"][m])
        lo = float(path["low"][m])
        if vw == vw and hi == hi and lo == lo and lo <= vw <= hi:
            return m, True
    return cap, False


def _bar_close(opt, minute, last):
    if 0 <= minute < sc.N_MIN and opt["real"][minute] and np.isfinite(opt["close"][minute]):
        close = float(opt["close"][minute])
        return close, minute
    if last is None:
        return None
    age = minute - last
    carried = opt["lab"][minute] if 0 <= minute < sc.N_MIN else np.nan
    if age > sc.STALE_AFTER or not np.isfinite(carried):
        return None
    return float(carried), last


def sale_net(opt, entry_min, exit_min, costs=wc.COSTS):
    """Net percent of selling the option close at `exit_min`. Same bill as simulate_trade."""
    cent, pct, comm = costs
    entry_min = int(entry_min)
    exit_min = int(exit_min)
    if entry_min < 0 or not (opt["real"][entry_min] and np.isfinite(opt["open"][entry_min])):
        return float("nan")
    raw = float(opt["open"][entry_min])
    debit = raw + sc.half_spread(raw, cent, pct)
    if debit <= 0:
        return float("nan")
    last = None
    fill = None
    for m in range(entry_min, exit_min + 1):
        got = _bar_close(opt, m, last)
        if got is None:
            continue
        close, last = got
        if m == exit_min:
            fill = close
    if fill is None:
        return float("nan")
    credit = max(0.0, fill - sc.half_spread(fill, cent, pct))
    dollar = (credit - debit) * 100.0 - 2.0 * comm
    return float(dollar / debit)


def touch_exit(opt, entry_min, path):
    """Sell on the first underlying VWAP touch, or at bar 20 if it never touches."""
    entry_min = int(entry_min)
    cap = min(entry_min + HOLD_BARS, sc.FLAT_MIN)
    minute, touched = first_touch(path, entry_min, cap)
    net = sale_net(opt, entry_min, minute)
    return {"net": net, "minute": minute, "touched": touched}


def _group(signals, max_level, other, side, pred):
    out = []
    for sig in signals:
        if sig["max_level"] != int(max_level) or sig["side"] != int(side):
            continue
        if not wc.other_ok(sig["other_value"], other):
            continue
        if sig.get("fill") is None or not pred(sig):
            continue
        out.append(sig)
    return out


def _stats(sigs, kind, n_days, train, test, n_boot, seed):
    nets = []
    days = []
    rnd = []
    atrs = []
    for sig in sigs:
        if kind == "hold20":
            value = (sig.get("fill") or {}).get("hold20", {}).get("net")
            random_value = (sig.get("rnd_fill") or {}).get("hold20", {}).get("net")
        else:
            value = (sig.get("vwap_touch") or {}).get("net")
            random_value = (sig.get("rnd_vwap_touch") or {}).get("net")
        if wc._finite(value):
            nets.append(float(value))
            days.append(sig["day_i"])
            if wc._finite(sig.get("und_atr_20")):
                atrs.append(float(sig["und_atr_20"]))
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
        "atr20": wc._mean(atrs),
    }


def _variants():
    rows = []
    for max_level in wc.MAX_LEVELS:
        for other in OTHERS:
            for side in (1, -1):
                rows.append((max_level, other, side, wc.variant_id(max_level, other, side)))
    return rows


def build_rows(signals, n_days, train_idx, test_idx, n_boot):
    train = set(int(i) for i in train_idx)
    test = set(int(i) for i in test_idx)
    bucket_rows = []
    touch_rows = []
    combo_rows = []
    for max_level, other, side, name in _variants():
        for label, pred in BUCKETS:
            group = _group(signals, max_level, other, side, lambda s, p=pred: p(s.get("vwap_dist", float("nan"))))
            stats = _stats(group, "hold20", n_days, train, test, n_boot, sc.stream_seed("whipsaw-vwap", name, label))
            bucket_rows.append({"variant": name, "slice": label, "exit": "hold20", **stats})
        far = _group(signals, max_level, other, side, lambda s: far_side(s.get("vwap_dist")))
        stretch = _group(signals, max_level, other, side, lambda s: stretched_against(s.get("vwap_dist")))
        for kind, sample, sink in (
            ("hold20", far, touch_rows),
            ("vwap_touch", far, touch_rows),
            ("hold20", stretch, combo_rows),
            ("vwap_touch", stretch, combo_rows),
        ):
            stats = _stats(sample, kind, n_days, train, test, n_boot, sc.stream_seed("whipsaw-vwap", name, kind, len(sink)))
            sink.append({"variant": name, "slice": "far side" if sink is touch_rows else "stretched 2+", "exit": kind, **stats})
    return bucket_rows, touch_rows, combo_rows


def _md(headers, body):
    head = "| " + " | ".join(headers) + " |"
    rule = "| " + " | ".join("---" for _ in headers) + " |"
    lines = ["| " + " | ".join(str(c) for c in row) + " |" for row in body]
    return "\n".join([head, rule, *lines])


def _body(rows):
    out = []
    for row in rows:
        out.append([
            row["variant"], row["slice"], row["exit"],
            row["n"], row["sessions"],
            wc._fmt(row["mean_net"]), wc._fmt(row["win"]), wc._fmt(row["median"]), wc._fmt(row["worst"]),
            wc._fmt(row["ci_lo"]), wc._fmt(row["ci_hi"]),
            row["train_n"], wc._fmt(row["train_mean"]),
            row["hold_n"], wc._fmt(row["hold_mean"]),
            row["random_n"], wc._fmt(row["random_mean"]),
            wc._fmt(row["atr20"]),
        ])
    return out


def _cell(rows, variant, slice_name, exit_name):
    for row in rows:
        if row["variant"] == variant and row["slice"] == slice_name and row["exit"] == exit_name:
            return row
    return None


def verdict_paragraph(bucket_rows, touch_rows, combo_rows, meta):
    bits = []
    for side in ("long", "short"):
        name = f"max95_ge60_{side}"
        fade = _cell(bucket_rows, name, "below -4", "hold20")
        chase = _cell(bucket_rows, name, "4+", "hold20")
        hold = _cell(touch_rows, name, "far side", "hold20")
        touch = _cell(touch_rows, name, "far side", "vwap_touch")
        combo_h = _cell(combo_rows, name, "stretched 2+", "hold20")
        combo_t = _cell(combo_rows, name, "stretched 2+", "vwap_touch")
        if fade is not None:
            bits.append(
                f"{side} below -4 ATR hold20 n {fade['n']} mean {wc._fmt(fade['mean_net'])}% "
                f"random {wc._fmt(fade['random_mean'])}% held-out {wc._fmt(fade['hold_mean'])}%"
            )
        if chase is not None:
            bits.append(f"{side} 4+ chase hold20 n {chase['n']} mean {wc._fmt(chase['mean_net'])}%")
        if hold is not None and touch is not None:
            bits.append(
                f"{side} far-side hold20 {wc._fmt(hold['mean_net'])}% vs VWAP touch {wc._fmt(touch['mean_net'])}%"
            )
        if combo_h is not None and combo_t is not None:
            bits.append(
                f"{side} stretched 2+ hold20 {wc._fmt(combo_h['mean_net'])}% vs VWAP touch {wc._fmt(combo_t['mean_net'])}%"
            )
    text = " ".join(bits) + "." if bits else "No max95 other-side-at-least-60 row was scored."
    if meta.get("synthetic"):
        text += " Prices in this file are synthetic, not a market."
    text += " Held-out is the last 25% of sessions. This is not a reason to trade."
    return text


def render_report(bucket_rows, touch_rows, combo_rows, meta, failures):
    parts = [
        "# Vix Fix whipsaw VWAP check",
        "",
        "Raw numbers are first. The last paragraph is the only prose.",
        "",
        "## Distance from session VWAP, 20-bar hold",
        "",
        "Distance is the signal-bar close versus session VWAP, in ATR(14), signed with the trade. "
        "Long is (close - VWAP) / ATR. Short is (VWAP - close) / ATR. "
        "Negative is against the trade (stretched, a fade). Positive is chasing.",
        "",
        _md(STAT_HEADERS, _body(bucket_rows)),
        "",
        "## VWAP-touch exit versus the 20-bar hold",
        "",
        "Only trades whose signal bar is on the against side of VWAP (distance < 0). "
        "The touch exit sells the option close on the first bar, within 20 minutes, whose high-low "
        "crosses that bar's session VWAP. No touch sells at bar 20, the same clock as the plain hold.",
        "",
        _md(STAT_HEADERS, _body(touch_rows)),
        "",
        "## Stretched 2+ ATR against, hold versus VWAP touch",
        "",
        "Distance at or below -2 ATR. That is the below -4 bucket and the -4 to -2 bucket together.",
        "",
        _md(STAT_HEADERS, _body(combo_rows)),
        "",
        "ge30 includes every ge60 signal. Do not add those rows. "
        "Costs are the whipsaw check: ask-side entry, bid-side exit, half-spread max(1 cent, 0.5%), $0.65 a side, 1-strike OTM, 0DTE, premium 0.30 to 1.00. "
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
    parts.append(verdict_paragraph(bucket_rows, touch_rows, combo_rows, meta))
    parts.append("")
    return "\n".join(parts)


def score_signals(signals, und, opt, symbols, score_days, paths):
    cache = {}

    def one(day_i, sym_i, minute, side):
        key = (day_i, sym_i, None if minute is None else int(minute), int(side))
        if key in cache:
            return cache[key]
        if minute is None:
            cache[key] = None
            return None
        day = score_days[day_i]
        sess = und[symbols[sym_i]].get(day)
        located = wc.locate_fill(sess, opt, day, symbols[sym_i], int(minute), int(side)) if sess is not None else None
        if located is None:
            cache[key] = None
            return None
        rec, fill_min, contract, raw = located
        packed = wc.exit_pack(rec, fill_min)
        packed["contract"] = contract
        packed["raw"] = raw
        packed["fill_minute"] = fill_min
        packed["touch"] = touch_exit(rec, fill_min, paths.get((symbols[sym_i], day)))
        cache[key] = packed
        return packed

    for sig in signals:
        packed = one(sig["day_i"], sig["sym_i"], sig["entry_minute"], sig["side"])
        sig["fill"] = packed
        sig["vwap_touch"] = None if packed is None else packed["touch"]
        rnd = sig.get("rnd_minute")
        rnd_packed = one(sig["day_i"], sig["sym_i"], rnd, sig["side"]) if rnd is not None else None
        sig["rnd_fill"] = rnd_packed
        sig["rnd_vwap_touch"] = None if rnd_packed is None else rnd_packed["touch"]


def trade_rows(signals, symbols, score_days, train_idx):
    train = set(int(i) for i in train_idx)
    rows = []
    for sig in signals:
        fill = sig.get("fill")
        if not fill:
            continue
        if sig["max_level"] not in wc.MAX_LEVELS:
            continue
        if not (wc.other_ok(sig["other_value"], "ge60") or wc.other_ok(sig["other_value"], "ge30")):
            continue
        touch = fill.get("touch") or {}
        rnd = sig.get("rnd_fill") or {}
        rnd_touch = rnd.get("touch") or {}
        rows.append({
            "day": score_days[sig["day_i"]].isoformat(),
            "symbol": symbols[sig["sym_i"]],
            "clock": fg.clock_hhmm(sig["entry_minute"]),
            "side": "long" if sig["side"] == 1 else "short",
            "max_level": sig["max_level"],
            "other_value": wc._fmt(sig["other_value"]),
            "vwap_dist": wc._fmt(sig.get("vwap_dist")),
            "bucket": bucket_name(sig.get("vwap_dist")),
            "far_side": wc._flag(far_side(sig.get("vwap_dist"))),
            "stretched_2": wc._flag(stretched_against(sig.get("vwap_dist"))),
            "split": "train" if sig["day_i"] in train else "hold",
            "contract": fill.get("contract", ""),
            "raw": wc._fmt(fill.get("raw"), 4),
            "net_hold20": wc._fmt((fill.get("hold20") or {}).get("net"), 4),
            "net_vwap_touch": wc._fmt(touch.get("net"), 4),
            "touch": wc._flag(touch.get("touched")),
            "touch_minute": touch.get("minute", ""),
            "rnd_net_hold20": wc._fmt((rnd.get("hold20") or {}).get("net"), 4),
            "rnd_net_vwap_touch": wc._fmt(rnd_touch.get("net"), 4),
            "und_atr_20": wc._fmt(sig.get("und_atr_20")),
        })
    return rows


def write_outputs(out_dir, report, trades):
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "WHIPSAW_VWAP.md")
    with open(path, "w") as handle:
        handle.write(report)
    csv_path = os.path.join(out_dir, "whipsaw_vwap_trades.csv")
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
    signals = _stage("signals", lambda: wc.signals_from_frames(frames, symbols, score_days, und), failures)
    if signals is None:
        signals = []
    meta["n_signals"] = len(signals)
    _log(f"  signals {len(signals)}")
    paths = _stage("vwap paths", lambda: session_paths(frames, symbols, score_days), failures) or {}

    def _download():
        nonlocal opt
        if opt is not None:
            return opt
        needed = wc.needed_contracts(signals, und, symbols, score_days)
        _log(f"  option days {len(needed)} contract-days {sum(len(v) for v in needed.values())}")
        return eh.fetch_option_days(
            needed, und, symbols, synthetic,
            cache_dir or "/tmp/whipsaw-vwap-cache",
            workers=max(1, int(workers)),
        )

    if signals:
        opt = _stage("download", _download, failures)
        if opt is None:
            opt = {}
        _stage(
            "fills",
            lambda: score_signals(signals, und, opt, symbols, score_days, paths),
            failures,
        )

    built = _stage(
        "summarize",
        lambda: build_rows(signals, len(score_days), train_idx, test_idx, n_boot),
        failures,
    )
    if built is None:
        bucket_rows, touch_rows, combo_rows = [], [], []
    else:
        bucket_rows, touch_rows, combo_rows = built
    meta["runtime_min"] = (time.time() - t0) / 60.0
    report = render_report(bucket_rows, touch_rows, combo_rows, meta, failures)
    trades = trade_rows(signals, symbols, score_days, train_idx)
    return {
        "report": report,
        "bucket_rows": bucket_rows,
        "touch_rows": touch_rows,
        "combo_rows": combo_rows,
        "trades": trades,
        "meta": meta,
        "failures": failures,
    }


def _empty(meta, message, failures):
    text = render_report([], [], [], meta, failures)
    return text.replace("Raw numbers are first.", "Raw numbers are first.\n\n" + message, 1)


def _env_flag(name):
    return os.getenv(name, "").strip().lower() in {"1", "true", "yes", "y"}


def _env_int(name, default):
    raw = os.getenv(name, "").strip()
    return int(raw) if raw else default


def main():
    t0 = time.time()
    out_dir = os.getenv("WHIP_OUT", "results").strip() or "results"
    os.makedirs(out_dir, exist_ok=True)
    synthetic = _env_flag("WHIP_SYNTH")
    blank = {"n_sessions": 0, "n_signals": 0, "synthetic": synthetic, "runtime_min": 0.0, "first_day": "", "last_day": ""}
    if not synthetic and not wc.keys_ready():
        write_outputs(out_dir, _empty(blank, fg.MISSING_KEYS, [("keys", fg.MISSING_KEYS)]), [])
        _log(f"STAGE keys failed: {fg.MISSING_KEYS}")
        return 1
    days_n = _env_int("WHIP_DAYS", 120)
    if days_n < 6:
        message = f"Need at least 6 sessions. Got {days_n}."
        write_outputs(out_dir, _empty(blank, message, [("days", message)]), [])
        _log(f"STAGE days failed: {message}")
        return 1
    symbols = [s.strip().upper() for s in os.getenv("WHIP_SYMBOLS", "SPY,QQQ").split(",") if s.strip()]
    if not symbols:
        _log("STAGE symbols failed: symbols is empty")
        return 1
    now = datetime.now(NY)
    end = datetime.now(timezone.utc) - timedelta(minutes=20)
    start = (pd.Timestamp(now.date(), tz=NY) - pd.Timedelta(days=int(days_n * 3 + 30))).tz_convert("UTC").to_pydatetime()
    _log(f"whipsaw-vwap symbols {', '.join(symbols)} days {days_n} synthetic {int(synthetic)}")
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
        cache_dir=os.getenv("WHIP_CACHE", "/tmp/whipsaw-vwap-cache").strip() or "/tmp/whipsaw-vwap-cache",
        workers=_env_int("WHIP_WORKERS", 4),
        n_boot=_env_int("WHIP_BOOT", 1000),
    )
    result["meta"]["runtime_min"] = (time.time() - t0) / 60.0
    result["report"] = render_report(
        result["bucket_rows"], result["touch_rows"], result["combo_rows"], result["meta"], result["failures"],
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
