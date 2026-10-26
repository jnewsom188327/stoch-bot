"""Log-only forward test of the noon greed/fear fade. No orders, not even paper orders.

The signal is the perfect-study base ``tf1_turn_mom_g95_f20``. Noon rows
(``tod_1200``, 12:00–12:59 ET) are the forward test of
``tf1_turn_mom_g95_f20__tod_1200`` with breakeven exits ``be_a15_d0`` and
``be_a10_d0``. Other hours are logged as context. A random entry with the same
premium band and the same exits is logged too.

Reads SIP stock bars and option quotes. Does not import a trading client and
does not submit orders.
"""

from __future__ import annotations

import csv
import json
import os
import subprocess
import time
import traceback
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd

import fgfade as fg
import fgperfect as fp
import scalp_real as sc

NY = fg.NY
SYMBOLS = ("SPY", "QQQ")
SPEC_ID = fp.BASE_ID
RULE_ID = f"{SPEC_ID}__tod_1200"
PREMIUM = fg.PREMIUM_BAND  # 0.30–1.00, the fade study's band
COSTS = fp.COSTS
FLAT_MINUTE = 375  # 15:45 ET. Same hard flat as the study.
WINDOW_OPEN = 11 * 60 + 55
WINDOW_CLOSE = 15 * 60 + 50  # exclusive
POLL_SECONDS = 15
BAR_EVERY = 2
SESSIONS_NEEDED = 30
TAIL_LOSS = -50.0  # net percent

EXITS = ("be_a15", "be_a10", "tp15_sl15", "tp15_sl25", "scale_15_15", "hold")

SIGNAL_FIELDS = [
    "day", "symbol", "clock", "minute", "side", "kind", "tod_bucket", "in_window",
    "greed", "fear", "mom", "squeeze", "status", "skip_reason",
    "contract", "spot", "strike", "bid", "ask", "entry_fill",
]
TRADE_FIELDS = [
    "day", "symbol", "clock", "minute", "side", "kind", "tod_bucket", "in_window",
    "contract", "bid", "ask", "entry_fill", "mfe_pct", "mae_pct", "minutes_to_peak",
] + [f"net_{name}" for name in EXITS] + [f"why_{name}" for name in EXITS]


def _log(message):
    sc._print_scrubbed(message, flush=True)


def inside_forward_window(now):
    """True from 11:55 ET inclusive until 15:50 ET exclusive, weekdays only."""
    if now.tzinfo is None:
        now = now.replace(tzinfo=NY)
    else:
        now = now.astimezone(NY)
    if now.weekday() >= 5:
        return False
    minute = now.hour * 60 + now.minute
    return WINDOW_OPEN <= minute < WINDOW_CLOSE


def _pid_alive(pid):
    if pid <= 0:
        return False
    try:
        os.kill(pid, 0)
    except PermissionError:
        return True
    except OSError:
        return False
    return True


def lock_held(path):
    """True when a different live process owns the lock. A dead pid is stale."""
    if not path or not os.path.exists(path):
        return False
    try:
        pid = int(open(path).read().strip() or "0")
    except (OSError, ValueError):
        return False
    if pid == os.getpid():
        return False
    return _pid_alive(pid)


def startup_guard(now, lock_path):
    """Quiet reasons to stop before any market call. Empty string means go."""
    if not inside_forward_window(now):
        return "outside the forward window"
    if lock_held(lock_path):
        return "already running"
    return ""


def acquire_lock(path):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    if lock_held(path):
        return False
    with open(path, "w") as handle:
        handle.write(str(os.getpid()))
    return True


def release_lock(path):
    try:
        if os.path.exists(path) and not lock_held(path):
            os.remove(path)
    except OSError:
        pass


def session_minute(now):
    now = now.astimezone(NY)
    return now.hour * 60 + now.minute - (9 * 60 + 30)


def clock_of(minute):
    return fg.clock_hhmm(minute)


def tod_bucket(minute):
    return fp._tod_name(minute)


def in_noon_window(minute):
    """Study bucket tod_1200: minutes 150–209, which is 12:00–12:59 ET."""
    return tod_bucket(minute) == "1200"


def entry_fill_of(ask):
    """Ask plus the study half-spread, max(1 cent, 0.5% of the ask)."""
    ask = float(ask)
    return ask + sc.half_spread(ask, COSTS[0], COSTS[1])


def _sale_net(ask, sale):
    net, dollar, _debit = fp.net_from_fill(np.array([float(ask)]), np.array([float(sale)]))
    return float(np.ravel(net)[0]), float(np.ravel(dollar)[0])


def simulate_bid_path(bids, ask):
    """Exits from a path of option bids. Levels are versus the entry fill.

    Breakeven has no stop and no target until the peak bid is +arm over the
    entry fill, then the stop is the entry fill. Otherwise the position is
    sold at the last bid (the 15:45 flat). A fixed stop is checked before the
    target. Scale sells half at +15% and trails the rest 15% under the later
    peak. The two scale halves are averaged, same as the study.
    """
    bids = [float(b) for b in bids if b == b and float(b) > 0]
    if not bids:
        raise ValueError("bid path is empty")
    fill = entry_fill_of(ask)
    out = {"entry_fill": fill}
    mfe_i = max(range(len(bids)), key=lambda i: bids[i])
    out["mfe_pct"] = (max(bids) / fill - 1.0) * 100.0
    out["mae_pct"] = (min(bids) / fill - 1.0) * 100.0
    out["minutes_to_peak"] = ""  # caller stamps the clock when it has times
    out["peak_index"] = int(mfe_i)

    def walk_be(arm):
        armed = False
        peak = fill
        for bid in bids:
            if not armed:
                peak = max(peak, bid)
                if peak >= fill * (1.0 + arm):
                    armed = True
                continue
            if bid <= fill:
                return bid, "be"
        return bids[-1], "flat"

    def walk_fixed(tp, sl):
        tp_px = fill * (1.0 + tp)
        sl_px = fill * (1.0 - sl)
        for bid in bids:
            if bid <= sl_px:
                return bid, "stop"
            if bid >= tp_px:
                return bid, "tp"
        return bids[-1], "flat"

    def walk_scale():
        target = fill * (1.0 + 0.15)
        half = None
        peak = fill
        for bid in bids:
            if half is None:
                if bid >= target:
                    half = bid
                    peak = bid
                continue
            stop_px = peak * (1.0 - 0.15)
            if bid <= stop_px:
                return half, bid, "scale"
            peak = max(peak, bid)
        last = bids[-1]
        if half is None:
            return last, last, "flat"
        return half, last, "scale"

    for name, arm in (("be_a15", 0.15), ("be_a10", 0.10)):
        sale, why = walk_be(arm)
        net, _dollar = _sale_net(ask, sale)
        out[f"net_{name}"] = net
        out[f"why_{name}"] = why
    for name, tp, sl in (("tp15_sl15", 0.15, 0.15), ("tp15_sl25", 0.15, 0.25)):
        sale, why = walk_fixed(tp, sl)
        net, _dollar = _sale_net(ask, sale)
        out[f"net_{name}"] = net
        out[f"why_{name}"] = why
    half, runner, why = walk_scale()
    net_h, _d1 = _sale_net(ask, half)
    net_r, _d2 = _sale_net(ask, runner)
    out["net_scale_15_15"] = 0.5 * (net_h + net_r)
    out["why_scale_15_15"] = why
    net_hold, _dh = _sale_net(ask, bids[-1])
    out["net_hold"] = net_hold
    out["why_hold"] = "flat"
    return out


def hour_ranges():
    """Clock hours that overlap 9:35–15:45, as session-minute [lo, hi)."""
    spans = ((9, 35, 60), (10, 0, 60), (11, 0, 60), (12, 0, 60), (13, 0, 60), (14, 0, 60), (15, 0, 45))
    out = []
    for hour, m0, m1 in spans:
        lo = hour * 60 + m0 - (9 * 60 + 30)
        hi = hour * 60 + m1 - (9 * 60 + 30)
        out.append((f"{hour:02d}", lo, hi))
    return out


def pick_two(lo, hi, seed):
    minutes = list(range(int(lo), int(hi)))
    if len(minutes) <= 2:
        chosen = minutes
    else:
        rng = np.random.default_rng(sc.stream_seed("fgforward-random", seed))
        chosen = None
        for _ in range(40):
            draw = sorted(int(x) for x in rng.choice(minutes, size=2, replace=False))
            if draw[1] - draw[0] >= 20:
                chosen = draw
                break
        if chosen is None:
            chosen = [minutes[0], minutes[-1]]
    return chosen


def random_plan(day, symbols):
    """Two minutes per ticker per clock hour, at least 20 minutes apart."""
    rows = []
    for sym in symbols:
        for name, lo, hi in hour_ranges():
            for minute in pick_two(lo, hi, f"{day.isoformat()}|{sym}|{name}"):
                rows.append({"symbol": sym, "minute": int(minute), "hour": name, "kind": "random"})
    return rows


def base_spec():
    return next(spec for spec in fp.entry_specs(False) if spec.id == SPEC_ID)


def events_for_frames(frames, symbols, day):
    """Closed-bar turn_mom events for one session. Same function the study uses."""
    score = {day: 0}
    charts = {1: {}}
    und = {}
    kept_symbols = []
    for sym in symbols:
        df = frames.get(sym)
        if df is None or not len(df):
            continue
        sym_i = len(kept_symbols)
        charts[1][sym_i] = fp.enrich_chart(df, 1, score)
        und[sym] = sc.rth_session(df)
        kept_symbols.append(sym)
    if not kept_symbols:
        return []
    return fp.build_signal_events(
        charts, base_spec(), und, kept_symbols, [day], {}, {}, None,
    )


def _reading_at(frame, minute):
    entry = frame["entry"]
    hits = np.flatnonzero(entry == int(minute))
    if len(hits) == 0:
        prior = np.flatnonzero((entry >= 0) & (entry <= int(minute)))
        if len(prior) == 0:
            return None
        i = int(prior[-1])
    else:
        i = int(hits[-1])
    greed = float(frame["greed"][i])
    fear = float(frame["fear"][i])
    mom = float(frame["mom"][i]) if np.isfinite(frame["mom"][i]) else float("nan")
    sq = bool(frame["sq_on"][i])
    if greed >= 95 and fear <= 20 and not (fear >= 95 and greed <= 20):
        side = -1
    elif fear >= 95 and greed <= 20:
        side = 1
    else:
        side = -1 if greed >= fear else 1
    return side, greed, fear, mom, sq


def frames_closed(frames, now):
    """Drop the minute that has not closed yet. The study signals on a closed bar."""
    cut = pd.Timestamp(now).tz_convert(NY)
    out = {}
    for sym, df in frames.items():
        if df is None or not len(df):
            out[sym] = df
            continue
        out[sym] = df[df.index + pd.Timedelta(minutes=1) <= cut]
    return out


def _num(text):
    try:
        value = float(text)
    except (TypeError, ValueError):
        return float("nan")
    return value


def _fmt(value, digits=1):
    if not isinstance(value, (int, float)) or not (value == value):
        return "n/a"
    return f"{value:.{digits}f}"


def _stats(rows, col):
    vals = []
    for row in rows:
        value = _num(row.get(col))
        if value == value:
            vals.append(value)
    if not vals:
        return {"n": 0, "mean": float("nan"), "win": float("nan"), "worst": float("nan"),
                "sum1000": float("nan"), "tail": 0}
    n = len(vals)
    return {
        "n": n,
        "mean": sum(vals) / n,
        "win": 100.0 * sum(v > 0 for v in vals) / n,
        "worst": min(vals),
        "sum1000": sum(v * 10.0 for v in vals),
        "tail": sum(v < TAIL_LOSS for v in vals),
    }


def _is_true(value):
    return str(value).strip().lower() in {"1", "true", "yes", "y"}


def render_scoreboard(signals, trades, sessions):
    """One-screen daily board. Noon rows are the forward test. Random rows share the exits."""
    noon_signals = [r for r in signals if r.get("kind") == "signal" and _is_true(r.get("in_window"))]
    noon_filled = [r for r in noon_signals if r.get("status") == "filled"]
    noon_trades = [r for r in trades if r.get("kind") == "signal" and _is_true(r.get("in_window"))]
    noon_random = [r for r in trades if r.get("kind") == "random" and _is_true(r.get("in_window"))]
    n_sess = len(sessions)
    lines = [
        "# Greed/fear forward test",
        "",
        "Log only. No orders of any kind, including Alpaca paper orders. "
        "Bars and quotes are read-only. This file is not a signal to trade.",
        "",
        f"Rule under test: `{RULE_ID}`. Exits `{ 'be_a15_d0' }` and `{ 'be_a10_d0' }`. "
        "The noon bucket is 12:00–12:59 ET (session minutes 150–209). "
        "Other hours are context and are marked `in_window` false.",
        "",
        f"Sessions so far: {n_sess}. " + (
            f"need >=30 sessions"
            if n_sess < SESSIONS_NEEDED
            else f"The {SESSIONS_NEEDED}-session line has been reached."
        ),
        f"Noon-hour signals: {len(noon_signals)}. Noon-hour trades (a quote inside 0.30–1.00): {len(noon_filled)}. "
        f"Trade rows on disk: {len(noon_trades)}.",
        "",
        "Nets are percent of the debit after the study cost model: entry is the ask plus "
        "max(1 cent, 0.5% of the ask), the sale is the bid minus that same haircut, and "
        "commission is $0.65 a side. Per $1,000 is 10 times the net percent.",
        "",
        "The breakeven rule has no stop until the peak bid is +15% (or +10%) over the entry fill. "
        "Before that, a loser is held to 15:45 and can be worse than -50%.",
        "",
    ]
    headers = ["exit", "noon trades", "mean net %", "win rate %", "worst %", "sum per $1000", "noon random mean %"]
    body = []
    for name in EXITS:
        sig = _stats(noon_trades, f"net_{name}")
        rnd = _stats(noon_random, f"net_{name}")
        body.append([
            name,
            sig["n"],
            _fmt(sig["mean"]),
            _fmt(sig["win"]),
            _fmt(sig["worst"]),
            _fmt(sig["sum1000"]),
            _fmt(rnd["mean"]),
        ])
    lines.append(_md(headers, body))
    lines.append("")
    be = _stats(noon_trades, "net_be_a15")
    tail_pct = (100.0 * be["tail"] / be["n"]) if be["n"] else float("nan")
    lines.append(
        f"Tail risk, noon `be_a15`: biggest single loss {_fmt(be['worst'])}%. "
        f"Trades that lost more than 50%: {be['tail']} of {be['n']} ({_fmt(tail_pct)}%)."
    )
    lines.append("")
    lines.append(
        "The random control is 2 entries per ticker per clock hour, same 0.30–1.00 band, "
        "same exits. The random column above is the noon hour only, so the clock matches."
    )
    lines.append("")
    return "\n".join(lines) + "\n"


def _md(headers, rows):
    head = "| " + " | ".join(str(h) for h in headers) + " |"
    rule = "| " + " | ".join("---" for _ in headers) + " |"
    body = ["| " + " | ".join(str(c) for c in row) + " |" for row in rows]
    return "\n".join([head, rule, *body])


def _append_rows(path, fields, rows):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    new = not os.path.exists(path)
    with open(path, "a", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        if new:
            writer.writeheader()
        for row in rows:
            writer.writerow(row)


def _read_csv(path):
    if not os.path.exists(path):
        return []
    with open(path, newline="") as handle:
        return list(csv.DictReader(handle))


def _state_path(out_dir):
    return os.path.join(out_dir, "fgforward_state.json")


def load_state(out_dir, day):
    path = _state_path(out_dir)
    blank = {
        "day": day.isoformat(),
        "job_start_minute": None,
        "sessions": [],
        "seen": [],
        "random_plan": [],
        "open": [],
    }
    if not os.path.exists(path):
        return blank
    try:
        saved = json.load(open(path))
    except (OSError, json.JSONDecodeError):
        return blank
    if saved.get("day") != day.isoformat():
        blank["sessions"] = list(saved.get("sessions") or [])
        return blank
    for key in blank:
        saved.setdefault(key, blank[key])
    return saved


def save_state(out_dir, state):
    path = _state_path(out_dir)
    os.makedirs(out_dir, exist_ok=True)
    tmp = path + ".tmp"
    with open(tmp, "w") as handle:
        json.dump(state, handle, indent=1, sort_keys=True)
    os.replace(tmp, path)


def write_board(out_dir, sessions):
    signals = _read_csv(os.path.join(out_dir, "fgforward_signals.csv"))
    trades = _read_csv(os.path.join(out_dir, "fgforward_trades.csv"))
    text = render_scoreboard(signals, trades, sessions)
    with open(os.path.join(out_dir, "FGFORWARD.md"), "w") as handle:
        handle.write(text)


def _seen_key(row):
    return f"{row['day']}|{row['symbol']}|{row['minute']}|{row['side']}|{row['kind']}"


def publish(out_dir):
    """Commit the result files onto the results branch. Refuses main and master."""
    if os.getenv("FG_PUBLISH", "").strip() != "1":
        return
    branch = os.getenv("FG_RESULTS_BRANCH", "fgforward-results").strip() or "fgforward-results"
    if branch in {"main", "master", "origin/main", "origin/master"}:
        raise SystemExit(f"Refusing to push results to {branch}")
    git_dir = os.getenv("FG_GIT", "").strip() or os.getcwd()
    head = subprocess.run(
        ["git", "rev-parse", "--abbrev-ref", "HEAD"], cwd=git_dir, capture_output=True, text=True,
    )
    name = (head.stdout or "").strip()
    if name in {"main", "master"}:
        _log(f"Refusing to commit results on {name}")
        return
    rels = [
        "results/fgforward_signals.csv",
        "results/fgforward_trades.csv",
        "results/FGFORWARD.md",
        "results/fgforward_state.json",
    ]
    # The worktree root holds results/. When FG_OUT is that results dir, paths match.
    subprocess.run(["git", "config", "user.name", "fgforward"], cwd=git_dir, check=False)
    subprocess.run(["git", "config", "user.email", "fgforward@users.noreply.github.com"], cwd=git_dir, check=False)
    present = [rel for rel in rels if os.path.exists(os.path.join(git_dir, rel))]
    if not present:
        return
    subprocess.run(["git", "add", "--"] + present, cwd=git_dir, check=False)
    diff = subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=git_dir)
    if diff.returncode == 0:
        return
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M")
    subprocess.run(["git", "commit", "-m", f"fgforward log {stamp}"], cwd=git_dir, check=False)
    for attempt in range(4):
        pull = subprocess.run(["git", "pull", "--rebase", "origin", branch], cwd=git_dir)
        if pull.returncode != 0:
            subprocess.run(["git", "rebase", "--abort"], cwd=git_dir, check=False)
            time.sleep(2 ** attempt)
            continue
        push = subprocess.run(["git", "push", "origin", f"HEAD:{branch}"], cwd=git_dir)
        if push.returncode == 0:
            _log(f"pushed {branch}")
            return
        time.sleep(2 ** attempt)
    _log("publish failed: push rejected")


def _keys():
    return os.getenv("ALPACA_KEY", "").strip(), os.getenv("ALPACA_SECRET", "").strip()


def fetch_frames(symbols, now):
    """SIP minute bars, IEX only if SIP is refused. Same helper the studies use."""
    bt = sc._bt()
    end = now.astimezone(timezone.utc)
    start = (pd.Timestamp(now) - pd.Timedelta(days=4)).to_pydatetime()
    frames = {}
    for sym in symbols:
        try:
            df, feed = bt.fetch_1m(sym, start, end)
        except SystemExit as exc:
            _log(f"bars {sym} failed: {exc}")
            continue
        frames[sym] = df
        _log(f"  {sym} {feed} bars {len(df)}")
    return frames


def _option_client():
    from alpaca.data.historical import OptionHistoricalDataClient
    key, secret = _keys()
    return OptionHistoricalDataClient(key, secret)


def _quote_pair(quote):
    if quote is None:
        return None
    try:
        bid = float(quote.bid_price or 0)
        ask = float(quote.ask_price or 0)
    except (TypeError, ValueError, AttributeError):
        return None
    if ask <= 0:
        return None
    return bid, ask


def _quote_map(client, contracts):
    from alpaca.data.requests import OptionLatestQuoteRequest
    contracts = list(dict.fromkeys(c for c in contracts if c))
    if not contracts:
        return {}
    try:
        got = client.get_option_latest_quote(OptionLatestQuoteRequest(symbol_or_symbols=contracts))
    except Exception as exc:
        _log(f"quote failed: {exc}")
        return {}
    out = {}
    for contract in contracts:
        quote = got.get(contract) if hasattr(got, "get") else None
        pair = _quote_pair(quote)
        if pair is not None:
            out[contract] = pair
    return out


def _quote_one(client, contract):
    return _quote_map(client, [contract]).get(contract)


def _signal_row(day, symbol, minute, side, kind, greed, fear, mom, squeeze, status, reason, **extra):
    row = {
        "day": day.isoformat(),
        "symbol": symbol,
        "clock": clock_of(minute),
        "minute": int(minute),
        "side": "call" if int(side) == 1 else "put",
        "kind": kind,
        "tod_bucket": tod_bucket(minute),
        "in_window": "true" if in_noon_window(minute) else "false",
        "greed": f"{float(greed):.2f}" if greed == greed else "",
        "fear": f"{float(fear):.2f}" if fear == fear else "",
        "mom": f"{float(mom):.4f}" if mom == mom else "",
        "squeeze": "on" if squeeze else "off",
        "status": status,
        "skip_reason": reason,
        "contract": "",
        "spot": "",
        "strike": "",
        "bid": "",
        "ask": "",
        "entry_fill": "",
    }
    row.update(extra)
    return row


def decide_entry(day, symbol, minute, side, kind, greed, fear, mom, squeeze, und, client):
    """First 1-strike OTM 0DTE. Skip, with a reason, when the ask is outside 0.30–1.00."""
    base = dict(day=day, symbol=symbol, minute=minute, side=side, kind=kind,
                greed=greed, fear=fear, mom=mom, squeeze=squeeze)
    if int(minute) > fg.ENTRY_HI or int(minute) >= sc.FLAT_MIN:
        return _signal_row(**base, status="skipped", reason="after 15:45"), None
    sess = und.get(symbol, {}).get(day) if und else None
    spot = sc.spot_at(sess, int(minute)) if sess is not None else None
    if spot is None:
        return _signal_row(**base, status="skipped", reason="no spot"), None
    strike = sc.strike_price(spot, int(side), "1otm")
    if strike is None:
        return _signal_row(**base, status="skipped", reason="no strike", spot=f"{spot:.2f}"), None
    cp = "C" if int(side) == 1 else "P"
    contract = sc._bt().lab_occ(symbol, day, cp, strike)
    quoted = _quote_one(client, contract)
    if quoted is None:
        return _signal_row(
            **base, status="skipped", reason="no quote",
            contract=contract, spot=f"{spot:.2f}", strike=str(strike),
        ), None
    bid, ask = quoted
    if not sc.premium_in_band(ask, PREMIUM):
        return _signal_row(
            **base, status="skipped", reason="premium outside 0.30-1.00",
            contract=contract, spot=f"{spot:.2f}", strike=str(strike),
            bid=f"{bid:.4f}", ask=f"{ask:.4f}",
        ), None
    fill = entry_fill_of(ask)
    row = _signal_row(
        **base, status="filled", reason="",
        contract=contract, spot=f"{spot:.2f}", strike=str(strike),
        bid=f"{bid:.4f}", ask=f"{ask:.4f}", entry_fill=f"{fill:.4f}",
    )
    opened = {
        "row": row,
        "ask": ask,
        "bids": [[datetime.now(NY).isoformat(timespec="seconds"), bid]],
    }
    return row, opened


def finalize_trade(opened, now):
    row = opened["row"]
    path = opened.get("bids") or []
    bids = [float(pair[1]) for pair in path]
    ask = float(opened["ask"])
    try:
        result = simulate_bid_path(bids, ask)
    except ValueError:
        return None
    times = []
    for pair in path:
        try:
            times.append(datetime.fromisoformat(pair[0]))
        except ValueError:
            times.append(now)
    peak_i = result["peak_index"]
    if times:
        start = times[0]
        peak_at = times[min(peak_i, len(times) - 1)]
        minutes = (peak_at - start).total_seconds() / 60.0
    else:
        minutes = float("nan")
    trade = {
        "day": row["day"],
        "symbol": row["symbol"],
        "clock": row["clock"],
        "minute": row["minute"],
        "side": row["side"],
        "kind": row["kind"],
        "tod_bucket": row["tod_bucket"],
        "in_window": row["in_window"],
        "contract": row["contract"],
        "bid": row["bid"],
        "ask": row["ask"],
        "entry_fill": f"{result['entry_fill']:.4f}",
        "mfe_pct": f"{result['mfe_pct']:.2f}",
        "mae_pct": f"{result['mae_pct']:.2f}",
        "minutes_to_peak": f"{minutes:.2f}",
    }
    for name in EXITS:
        trade[f"net_{name}"] = f"{result[f'net_{name}']:.4f}"
        trade[f"why_{name}"] = result[f"why_{name}"]
    return trade


def _charts_for_random(frames, day):
    score = {day: 0}
    out = {}
    for sym, df in frames.items():
        if df is None or not len(df):
            continue
        out[sym] = fp.enrich_chart(df, 1, score)
    return out


def run_session(now_fn, sleep_fn, out_dir, symbols=SYMBOLS):
    """One session inside the window. `now_fn` and `sleep_fn` are injectable for tests."""
    now = now_fn()
    day = now.astimezone(NY).date()
    state = load_state(out_dir, day)
    if day.isoformat() not in state["sessions"]:
        state["sessions"].append(day.isoformat())
    if state["job_start_minute"] is None:
        state["job_start_minute"] = int(session_minute(now))
    if not state["random_plan"]:
        state["random_plan"] = random_plan(day, symbols)
    seen = set(state["seen"])
    for row in _read_csv(os.path.join(out_dir, "fgforward_signals.csv")):
        if row.get("day") == day.isoformat():
            seen.add(_seen_key(row))
    state["seen"] = sorted(seen)
    client = _option_client()
    tick = 0
    frames = {}
    _log(f"fgforward {day} start minute {state['job_start_minute']} log only")
    while True:
        now = now_fn()
        local = now.astimezone(NY)
        minute_now = session_minute(local)
        if minute_now >= FLAT_MINUTE or not inside_forward_window(local):
            _poll(state, client, local)
            _flatten(state, out_dir, local)
            return state
        if tick % BAR_EVERY == 0:
            fresh = fetch_frames(symbols, local)
            if fresh:
                frames = frames_closed(fresh, local)
            und = {sym: sc.rth_session(df) for sym, df in frames.items() if df is not None and len(df)}
            _take_signals(state, out_dir, frames, und, symbols, day, minute_now, client, seen)
            _take_randoms(state, out_dir, frames, und, day, minute_now, client, seen)
        _poll(state, client, local)
        tick += 1
        if tick % 40 == 0:
            save_state(out_dir, state)
            write_board(out_dir, state["sessions"])
            publish(out_dir)
        sleep_fn(POLL_SECONDS)


def _take_signals(state, out_dir, frames, und, symbols, day, minute_now, client, seen):
    if not frames:
        return
    # build_signal_events indexes symbols in the order we pass. Keep that order.
    ordered = [sym for sym in symbols if sym in frames]
    events = events_for_frames({sym: frames[sym] for sym in ordered}, ordered, day)
    sym_of = {i: sym for i, sym in enumerate(ordered)}
    new_rows = []
    for ev in events:
        if int(ev.minute) < int(state["job_start_minute"]):
            continue
        if int(ev.minute) > int(minute_now):
            continue
        symbol = sym_of[ev.sym]
        row_key = f"{day.isoformat()}|{symbol}|{int(ev.minute)}|{('call' if ev.side == 1 else 'put')}|signal"
        if row_key in seen:
            continue
        if int(minute_now) > int(ev.minute) + 1:
            row = _signal_row(
                day, symbol, int(ev.minute), ev.side, "signal",
                ev.greed, ev.fear, ev.mom if ev.mom == ev.mom else float("nan"), bool(ev.sq),
                "skipped", "missed the entry minute",
            )
            new_rows.append(row)
            seen.add(row_key)
            continue
        row, opened = decide_entry(
            day, symbol, int(ev.minute), ev.side, "signal",
            ev.greed, ev.fear, ev.mom if ev.mom == ev.mom else float("nan"), bool(ev.sq),
            und, client,
        )
        new_rows.append(row)
        seen.add(_seen_key(row))
        if opened is not None:
            state["open"].append(opened)
            _log(f"  signal {row['symbol']} {row['clock']} {row['side']} {row['contract']} ask {row['ask']}")
        else:
            _log(f"  skip {row['symbol']} {row['clock']} {row['skip_reason']}")
    _persist_signals(state, out_dir, new_rows, seen)


def _take_randoms(state, out_dir, frames, und, day, minute_now, client, seen):
    if not frames:
        return
    charts = _charts_for_random(frames, day)
    new_rows = []
    for plan in state["random_plan"]:
        minute = int(plan["minute"])
        if minute < int(state["job_start_minute"]) or minute > int(minute_now):
            continue
        symbol = plan["symbol"]
        frame = charts.get(symbol)
        if frame is None:
            continue
        reading = _reading_at(frame, minute)
        if reading is None:
            side, greed, fear, mom, squeeze = -1, float("nan"), float("nan"), float("nan"), False
        else:
            side, greed, fear, mom, squeeze = reading
        # The side is chosen at the minute. Match the minute exactly so 15 does not catch 150.
        prefix = f"{day.isoformat()}|{symbol}|{minute}|"
        if any(key.startswith(prefix) and key.endswith("|random") for key in seen):
            continue
        if int(minute_now) > minute + 1:
            row = _signal_row(
                day, symbol, minute, side, "random", greed, fear, mom, squeeze,
                "skipped", "missed the entry minute",
            )
            new_rows.append(row)
            seen.add(_seen_key(row))
            continue
        row, opened = decide_entry(
            day, symbol, minute, side, "random", greed, fear, mom, squeeze, und, client,
        )
        new_rows.append(row)
        seen.add(_seen_key(row))
        if opened is not None:
            state["open"].append(opened)
            _log(f"  random {row['symbol']} {row['clock']} {row['side']} ask {row['ask']}")
        else:
            _log(f"  random skip {row['symbol']} {row['clock']} {row['skip_reason']}")
    _persist_signals(state, out_dir, new_rows, seen)


def _persist_signals(state, out_dir, rows, seen):
    if not rows:
        return
    _append_rows(os.path.join(out_dir, "fgforward_signals.csv"), SIGNAL_FIELDS, rows)
    state["seen"] = sorted(seen)
    save_state(out_dir, state)
    write_board(out_dir, state["sessions"])
    publish(out_dir)


def _poll(state, client, now):
    contracts = [t["row"]["contract"] for t in state["open"] if t["row"].get("contract")]
    if not contracts:
        return
    quotes = _quote_map(client, contracts)
    stamp = now.astimezone(NY).isoformat(timespec="seconds")
    for trade in state["open"]:
        contract = trade["row"].get("contract")
        got = quotes.get(contract)
        if got is None:
            continue
        bid, _ask = got
        if bid > 0:
            trade["bids"].append([stamp, bid])


def _flatten(state, out_dir, now):
    done = []
    for opened in list(state["open"]):
        trade = finalize_trade(opened, now)
        if trade is None:
            _log(f"  no bid path {opened['row'].get('symbol')} {opened['row'].get('clock')}")
            continue
        _append_rows(os.path.join(out_dir, "fgforward_trades.csv"), TRADE_FIELDS, [trade])
        done.append(opened)
        _log(
            f"  flat {trade['symbol']} {trade['clock']} {trade['kind']} "
            f"be15 {trade['net_be_a15']} be10 {trade['net_be_a10']}"
        )
        state["open"] = [t for t in state["open"] if t is not opened]
        save_state(out_dir, state)
        write_board(out_dir, state["sessions"])
        publish(out_dir)
    if not done:
        save_state(out_dir, state)
        write_board(out_dir, state["sessions"])
        publish(out_dir)
    _log("fgforward session closed")


def main():
    now = datetime.now(NY)
    out_dir = os.getenv("FG_OUT", "results").strip() or "results"
    lock_path = os.getenv("FG_LOCK", "/tmp/fgforward.lock").strip() or "/tmp/fgforward.lock"
    reason = startup_guard(now, lock_path)
    if reason:
        _log(reason)
        return 0
    key, secret = _keys()
    if not key or not secret:
        _log("ALPACA_KEY / ALPACA_SECRET are missing. No orders were sent.")
        return 1
    if not acquire_lock(lock_path):
        _log("already running")
        return 0
    try:
        run_session(lambda: datetime.now(NY), time.sleep, out_dir)
    except Exception as exc:
        traceback.print_exc()
        _log(f"STAGE forward failed: {exc}")
        return 1
    finally:
        release_lock(lock_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
