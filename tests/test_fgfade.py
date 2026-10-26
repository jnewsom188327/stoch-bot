"""Greed/fear fade math, causality, and the manual results workflow. No orders, no network."""

import math
from datetime import datetime

import numpy as np
import pandas as pd
import pytest

import fgfade as fg
import scalp_real as sc

NY = fg.NY
EXACT_NO_BETTER = (
    "The +15% peak hit-rate within 30 minutes is no better than the matched random entry."
)


def test_grid_is_the_predeclared_family():
    cells = fg.grid_cells((1, 3, 5))
    assert len(cells) == 960
    assert fg.family_row_count((1, 3, 5)) == 3840
    ids = [c.id for c in fg.grid_cells((1,))]
    assert len(ids) == 320 == len(set(ids))
    assert "tf1_first_g95_f10" in ids
    assert "tf1_turn_g85_f20" in ids
    assert "tf1_turn_band_g85_f5" in ids
    assert "tf1_turn_mom_g90_f20" in ids
    assert "tf1_all3_n0_any_g95_f10" in ids
    assert "tf1_all3_n3_off_g80_f30" in ids
    first = next(c for c in cells if c.variant == "first")
    assert first.N is None and first.squeeze is None
    with pytest.raises(SystemExit):
        fg.parse_tfs("15")
    assert fg.parse_tfs("5,1,5") == (5, 1)


def test_first_in_run_resets_each_session():
    flag = np.array([1, 1, 0, 1, 1], dtype=bool)
    day = np.array([0, 0, 1, 1, 1])
    got = fg.first_in_run(flag, day)
    assert list(np.flatnonzero(got)) == [0, 3]


def test_side_turn_drop_cross_and_session_boundary():
    other = np.zeros(4)
    day = np.zeros(4, dtype=int)
    drop = fg.side_turn(np.array([10.0, 50.0, 40.0, 40.0]), other, 40, 10, np.zeros(4), day)
    assert list(np.flatnonzero(drop)) == [2]
    cross = fg.side_turn(
        np.array([30.0, 50.0, 50.0]), np.zeros(3), 40, 10, np.array([0.0, 40.0, 60.0]), np.zeros(3, dtype=int),
    )
    assert list(np.flatnonzero(cross)) == [2]
    broken = fg.side_turn(
        np.array([10.0, 50.0, 40.0]), np.zeros(3), 40, 10, np.zeros(3), np.array([0, 0, 1]),
    )
    assert not broken.any()


def test_quiet_lift_and_momentum_turns():
    got = fg.quiet_lift(
        np.array([5.0, 1.0, 2.0]), np.array([10.0, 50.0, 50.0]), 40, 10, np.zeros(3), np.zeros(3, dtype=int),
    )
    assert list(np.flatnonzero(got)) == [2]
    day = np.zeros(4, dtype=int)
    assert fg.mom_turn_down(np.array([0.0, 1.0, 2.0, 1.0]), day)[3]
    assert not fg.mom_turn_down(np.array([0.0, -1.0, -2.0, -3.0]), day)[3]
    assert fg.mom_turn_down(np.array([0.0, 0.5, 0.4]), np.zeros(3, dtype=int))[2]
    assert fg.mom_turn_up(np.array([0.0, -1.0, -0.2]), np.zeros(3, dtype=int))[2]
    assert not fg.mom_turn_down(np.array([0.0, 1.0, 0.0]), np.array([0, 0, 1]))[2]


def test_cluster_window_does_not_refire_or_cross_a_session():
    day = np.zeros(12, dtype=int)
    pinned = np.zeros(12, dtype=bool)
    quiet = np.zeros(12, dtype=bool)
    mom = np.zeros(12, dtype=bool)
    extreme = np.zeros(12, dtype=bool)
    pinned[5] = quiet[6] = mom[7] = extreme[5] = True
    assert fg.cluster_fires(pinned, quiet, mom, extreme, 0, day).sum() == 0
    assert fg.cluster_fires(pinned, quiet, mom, extreme, 1, day).sum() == 0
    assert list(np.flatnonzero(fg.cluster_fires(pinned, quiet, mom, extreme, 2, day))) == [7]
    assert list(np.flatnonzero(fg.cluster_fires(pinned, quiet, mom, extreme, 3, day))) == [7]
    held = np.ones(5, dtype=bool)
    assert list(np.flatnonzero(fg.cluster_fires(held, held, held, held, 0, np.zeros(5, dtype=int)))) == [0]
    day2 = np.array([0, 0, 0, 1, 1])
    pinned = np.array([0, 0, 1, 0, 0], dtype=bool)
    quiet = np.array([0, 0, 0, 1, 0], dtype=bool)
    mom = np.array([0, 0, 0, 1, 0], dtype=bool)
    extreme = np.array([0, 0, 1, 0, 0], dtype=bool)
    assert fg.cluster_fires(pinned, quiet, mom, extreme, 3, day2).sum() == 0


def test_squeeze_states_partition_and_the_five_bar_release():
    on = np.array([1, 1, 0, 0, 0, 0, 0], dtype=bool)
    day = np.zeros(len(on), dtype=int)
    released = fg.released_recent(on, day, 5)
    # Index 6 still sees the on-bar at index 1 (five bars back). Index 7 would not.
    assert released[2] and released[5] and released[6]
    only = np.zeros(8, dtype=bool)
    only[0] = True
    rel = fg.released_recent(only, np.zeros(8, dtype=int), 5)
    assert rel[5] and not rel[6]
    on_s, rel_s, off = fg.squeeze_states(on, day, 5)
    assert np.all(on_s | rel_s | off)
    assert not np.any(on_s & rel_s)
    assert not np.any(rel_s & off)
    assert not np.any(on_s & off)


def test_outside_band_is_the_fade_side():
    close = np.array([10.0])
    assert fg.outside_band(close, [9.0], [1.0], [11.0], [1.0], -1)[0]
    assert fg.outside_band(close, [11.0], [11.0], [12.0], [8.0], 1)[0]
    assert not fg.outside_band(close, [11.0], [9.0], [12.0], [8.0], -1)[0]


def test_cooldown_keeps_the_more_extreme_side_and_a_twenty_minute_gap():
    tie = fg.apply_cooldown([
        (0, 0, 5, -1, 90.0, 1.0, 90.0),
        (0, 0, 5, 1, 90.0, 90.0, 1.0),
    ])
    assert len(tie) == 1 and tie[0][fg.SIDE] == -1
    stronger = fg.apply_cooldown([
        (0, 0, 5, -1, 90.0, 1.0, 90.0),
        (0, 0, 5, 1, 95.0, 95.0, 1.0),
    ])
    assert len(stronger) == 1 and stronger[0][fg.SIDE] == 1
    spaced = fg.apply_cooldown([
        (0, 0, 0, -1, 90.0, 1.0, 90.0),
        (0, 0, 19, -1, 90.0, 1.0, 90.0),
        (0, 0, 20, -1, 90.0, 1.0, 90.0),
        (1, 0, 0, -1, 90.0, 1.0, 90.0),
    ])
    assert [(e[fg.DI], e[fg.MIN]) for e in spaced] == [(0, 0), (0, 20), (1, 0)]


class _First:
    def choice(self, cands):
        self.last = [int(x) for x in np.asarray(cands)]
        return self.last[0]


def test_random_minute_stays_in_the_bucket_or_falls_back():
    near_open = _First()
    assert fg.random_minute(5, near_open) == 25
    assert near_open.last[0] == 25
    assert all(abs(m - 5) >= 20 for m in near_open.last)
    assert max(near_open.last) <= 34
    middle = _First()
    assert fg.random_minute(20, middle) == 40
    assert 20 not in middle.last
    assert all(abs(m - 20) >= 20 for m in middle.last)


def _stamp(opt, minute, open_, high, low, close):
    opt["real"][minute] = True
    opt["open"][minute] = open_
    opt["high"][minute] = high
    opt["low"][minute] = low
    opt["close"][minute] = close
    opt["lab"][minute] = close


def test_mfe_windows_ignore_bars_outside_the_path():
    opt = sc._empty_opt()
    _stamp(opt, 9, 0.50, 5.00, 0.50, 0.50)
    for minute in range(10, 41):
        _stamp(opt, minute, 0.50, 0.55, 0.50, 0.50)
    _stamp(opt, 16, 0.50, 0.90, 0.50, 0.50)
    _stamp(opt, 40, 0.50, 2.00, 0.50, 0.50)
    got = fg.measure_path(opt, 10)
    assert got["peak_by_window"][5] < got["peak_by_window"][15] < got["peak_by_window"][30]
    assert got["peak_by_window"][30] == got["peak_by_window"][60]
    assert got["peak_bid"] < 3.0
    assert got["hits"][fg.HIT_15_30]


def test_drawdown_stops_at_the_peak_bar():
    opt = sc._empty_opt()
    _stamp(opt, 10, 0.50, 0.60, 0.50, 0.55)
    _stamp(opt, 11, 0.55, 0.70, 0.30, 0.60)
    _stamp(opt, 12, 0.60, 0.65, 0.10, 0.40)
    got = fg.measure_path(opt, 10)
    assert got["t_peak"] == 1
    assert got["worst_bid"] == pytest.approx(0.29)
    assert got["peak_bid"] == pytest.approx(0.69)


def test_stop_is_taken_before_the_target_on_the_same_bar():
    opt = sc._empty_opt()
    _stamp(opt, 20, 0.50, 0.70, 0.40, 0.50)
    exits = fg.fixed_exits(opt, 20)
    assert exits["tp15_sl15"]["reason"] == "stop"


def _session(spots):
    rec = {k: np.full(sc.N_MIN, np.nan) for k in ("open", "high", "low", "close")}
    rec["real"] = np.zeros(sc.N_MIN, dtype=bool)
    for minute, spot in spots.items():
        rec["open"][minute] = spot
        rec["close"][minute] = spot
        rec["high"][minute] = spot
        rec["low"][minute] = spot
        rec["real"][minute] = True
    return rec


def _print(minute, price):
    opt = sc._empty_opt()
    _stamp(opt, minute, price, price, price * 0.99, price)
    return opt


def test_premium_outside_the_band_does_not_slide():
    day = datetime(2026, 1, 5).date()
    sess = _session({30: 400.0, 31: 400.0})
    contract = sc._bt().lab_occ("SPY", day, "P", 399)
    book = {(day, contract): _print(30, 1.50)}
    book[(day, contract)]["real"][31] = True
    book[(day, contract)]["open"][31] = 0.50
    book[(day, contract)]["high"][31] = 0.50
    book[(day, contract)]["low"][31] = 0.49
    book[(day, contract)]["close"][31] = 0.50
    got = fg.resolve_fill(sess, book, day, "SPY", 30, -1, "1otm")
    assert got["raw"] == pytest.approx(1.50)
    assert got["slipped"] is False
    assert got["in_band"] is False


def test_missing_print_slips_one_minute_and_recomputes_the_strike():
    day = datetime(2026, 1, 5).date()
    sess = _session({30: 400.0, 31: 410.0})
    contract = sc._bt().lab_occ("SPY", day, "P", 409)
    book = {(day, contract): _print(31, 0.50)}
    got = fg.resolve_fill(sess, book, day, "SPY", 30, -1, "1otm")
    assert got["slipped"] is True
    assert got["raw"] == pytest.approx(0.50)
    assert got["in_band"] is True
    assert got["contract"] == contract
    late = _session({375: 400.0, 376: 400.0})
    late_contract = sc._bt().lab_occ("SPY", day, "P", 399)
    late_book = {(day, late_contract): _print(376, 0.50)}
    assert fg.resolve_fill(late, late_book, day, "SPY", 375, -1, "1otm") is None


def _fill(hit, net=1.0, in_band=True, raw=0.50):
    hits = [False] * (len(fg.WINDOWS) * len(fg.HIT_LEVELS))
    hits[fg.HIT_15_30] = bool(hit)
    exits = {name: {"reason": "tp" if hit else "stop", "net": net} for name, _cfg in fg.EXITS}
    return {
        "in_band": in_band,
        "raw": raw,
        "debit": raw + 0.01,
        "peak_bid": 0.70,
        "t_peak": 4,
        "worst_bid": 0.40,
        "mfe": 12.0,
        "drawdown": -8.0,
        "hits": tuple(hits),
        "entry_min": 30,
        "path_minutes": 60,
        "contract": "C",
        "exits": exits,
    }


def test_selection_uses_only_the_train_day_mask():
    common = fg.Cell(1, "first", 80, 5)
    leaked = fg.Cell(1, "first", 95, 5)
    events = {
        common.id: [(d, 0, 30, -1, 90.0, 1.0, 90.0) for d in (0, 1)],
        leaked.id: [(d, 0, 40, -1, 99.0, 1.0, 99.0) for d in (2, 3, 4, 5)],
    }
    fills = {}
    for cid, rows in events.items():
        for ev in rows:
            fills[(ev[0], ev[1], ev[2], ev[3], "1otm")] = _fill(cid == leaked.id)
    days = [datetime(2026, 1, d).date() for d in range(5, 11)]
    scored = fg._select_and_score(
        [common, leaked], events, fills, {}, 6, np.array([0, 1]), np.array([2, 3, 4, 5]),
        days, 1, 0, 1, 1,
    )
    assert scored["cell"] == common.id
    assert scored["train_signal_days"] == 2
    assert scored["test_signal_days"] == 0


def test_choose_cell_prefers_sessions_and_records_a_missed_minimum():
    chosen = fg.choose_cell([
        {"cell": "rare", "signal_days": 4, "hit_15_30": 90.0, "fills": 20, "signals": 20},
        {"cell": "common", "signal_days": 40, "hit_15_30": 30.0, "fills": 50, "signals": 50},
    ], 15)
    assert chosen["cell"] == "common"
    assert chosen["select_note"] == "minimum met"
    floored = fg.choose_cell([
        {"cell": "tiny", "signal_days": 30, "hit_15_30": 99.0, "fills": 3, "signals": 30},
        {"cell": "ok", "signal_days": 5, "hit_15_30": 10.0, "fills": 15, "signals": 15},
    ], 15)
    assert floored["cell"] == "ok"
    missed = fg.choose_cell([
        {"cell": "a", "signal_days": 2, "hit_15_30": 10.0, "fills": 2, "signals": 2},
        {"cell": "b", "signal_days": 8, "hit_15_30": 10.0, "fills": 4, "signals": 4},
    ], 15)
    assert missed["cell"] == "b"
    assert missed["select_note"] == "minimum was not met"


def test_coverage_verdict_and_breakeven_wording():
    change = fg.coverage_change(100, 40)
    assert change["fraction"] == pytest.approx(0.4)
    assert change["dropped"] == 60
    text = fg.coverage_sentence(100, 40, 120)
    assert "100 of 120" in text and "40 sessions" in text and "40%" in text
    assert fg.verdict_sentence(40, 40) == EXACT_NO_BETTER
    assert fg.verdict_sentence(10, 40) == EXACT_NO_BETTER
    higher = fg.verdict_sentence(55, 40, q=0.2)
    assert "higher than the matched random entry" in higher
    assert "55.0%" in higher and "40.0%" in higher and "0.200" in higher
    rate = sc.breakeven_hit_rate(0.15, 0.15, 0.50, 0.01, 0.005, 0.65)
    assert math.isfinite(rate) and rate > 0.5
    sentence = fg.breakeven_sentence(rate, 0.50, 40.0)
    assert "$0.50" in sentence and "TP +15%" in sentence and "stop" in sentence
    assert "40.0%" in sentence


def _hand_frame():
    n = 7
    frame = {
        "day_ord": np.zeros(n, dtype=np.int32),
        "day_i": np.zeros(n, dtype=np.int32),
        "entry": np.array([30, 31, 32, 100, 130, 131, 132], dtype=np.int32),
        "score": np.ones(n, dtype=bool),
        "fear": np.array([5.0, 1.0, 2.0, 5.0, 5.0, 1.0, 2.0]),
        "greed": np.array([10.0, 96.0, 95.5, 10.0, 10.0, 96.0, 95.5]),
        "fear_sig": np.zeros(n),
        "greed_sig": np.zeros(n),
        "mom": np.array([0.0, 1.0, 0.5, 0.0, 0.0, 0.0, 0.0]),
        "hist": np.array([0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.5]),
        "sq_on": np.zeros(n, dtype=bool),
        "close": np.ones(n),
        "vwap_up": np.full(n, 0.5),
        "vwap_dn": np.zeros(n),
        "bb_up": np.full(n, 0.5),
        "bb_dn": np.zeros(n),
    }
    return frame


def _minutes(frame, cell):
    return sorted(ev[fg.MIN] for ev in fg.events_for_frame(frame, cell, 0))


def test_variants_fire_on_the_turn_cluster_and_the_squeeze_filter():
    frame = _hand_frame()
    assert _minutes(frame, fg.Cell(1, "first", 95, 10)) == [31, 131]
    assert _minutes(frame, fg.Cell(1, "turn", 95, 10)) == [32, 132]
    assert _minutes(frame, fg.Cell(1, "turn_band", 95, 10)) == [32, 132]
    assert _minutes(frame, fg.Cell(1, "turn_mom", 95, 10)) == [32, 132]
    assert _minutes(frame, fg.Cell(1, "all3", 95, 10, 0, "any")) == [32]
    assert _minutes(frame, fg.Cell(1, "all3", 95, 10, 0, "off")) == [32]
    assert _minutes(frame, fg.Cell(1, "all3", 95, 10, 0, "on")) == []
    assert _minutes(frame, fg.Cell(1, "all3", 95, 10, 0, "released5")) == []
    frame["sq_on"] = np.array([1, 0, 0, 0, 0, 0, 0], dtype=bool)
    frame.pop("_ready", None)
    assert _minutes(frame, fg.Cell(1, "all3", 95, 10, 0, "released5")) == [32]
    assert _minutes(frame, fg.Cell(1, "all3", 95, 10, 0, "off")) == []
    call = {
        "day_ord": np.zeros(3, dtype=np.int32),
        "day_i": np.zeros(3, dtype=np.int32),
        "entry": np.array([30, 31, 32], dtype=np.int32),
        "score": np.ones(3, dtype=bool),
        "fear": np.array([10.0, 96.0, 95.5]),
        "greed": np.array([5.0, 1.0, 2.0]),
        "fear_sig": np.zeros(3),
        "greed_sig": np.zeros(3),
        "mom": np.array([0.0, -1.0, -0.4]),
        "hist": np.zeros(3),
        "sq_on": np.zeros(3, dtype=bool),
        "close": np.ones(3),
        "vwap_up": np.ones(3),
        "vwap_dn": np.ones(3),
        "bb_up": np.ones(3),
        "bb_dn": np.ones(3),
    }
    calls = fg.events_for_frame(call, fg.Cell(1, "all3", 95, 10, 0, "any"), 0)
    assert len(calls) == 1 and calls[0][fg.SIDE] == 1 and calls[0][fg.MIN] == 32


def test_squeeze_matches_the_repo_definition():
    rng = np.random.default_rng(1)
    n = 80
    close = 100 + np.cumsum(rng.normal(0, 0.2, n))
    high = close + 0.15
    low = close - 0.15
    sq, mom, up, dn = fg.ttm_squeeze(high, low, close)
    cs = pd.Series(close)
    hs = pd.Series(high)
    ls = pd.Series(low)
    basis = cs.rolling(20).mean()
    dev = 2.0 * cs.rolling(20).std(ddof=0)
    prev = cs.shift(1)
    tr = pd.concat([hs - ls, (hs - prev).abs(), (ls - prev).abs()], axis=1).max(axis=1)
    kc = tr.rolling(20).mean()
    inside = ((basis - dev) > (basis - 1.5 * kc)) & ((basis + dev) < (basis + 1.5 * kc))
    expect_sq = inside.fillna(False).to_numpy(dtype=bool)
    mid = ((hs.rolling(20).max() + ls.rolling(20).min()) / 2.0 + basis) / 2.0
    expect_mom = sc._bt().linreg_last((cs - mid).to_numpy(dtype=float), 20)
    np.testing.assert_array_equal(sq, expect_sq)
    np.testing.assert_allclose(mom, expect_mom, equal_nan=True)
    np.testing.assert_allclose(up, (basis + dev).to_numpy(), equal_nan=True)
    np.testing.assert_allclose(dn, (basis - dev).to_numpy(), equal_nan=True)


def test_fear_greed_does_not_use_a_future_bar():
    idx = pd.date_range("2026-01-05 09:30", periods=120, freq="1min", tz=NY)
    rng = np.random.default_rng(0)
    close = 100 + np.cumsum(rng.normal(0, 0.05, len(idx)))
    df = pd.DataFrame({
        "open": close, "high": close + 0.1, "low": close - 0.1, "close": close, "volume": np.full(len(idx), 1000.0),
    }, index=idx)
    fear, greed = fg.fear_greed(df)
    bumped = df.copy()
    bumped.iloc[-1, bumped.columns.get_loc("low")] = 50.0
    fear2, greed2 = fg.fear_greed(bumped)
    np.testing.assert_allclose(fear[:-1], fear2[:-1], equal_nan=True)
    np.testing.assert_allclose(greed[:-1], greed2[:-1], equal_nan=True)


def test_higher_timeframe_bar_is_known_at_its_close():
    idx = pd.date_range("2026-01-05 09:30", periods=390, freq="1min", tz=NY)
    rng = np.random.default_rng(2)
    close = 100 + np.cumsum(rng.normal(0, 0.04, len(idx)))
    df = pd.DataFrame({
        "open": close, "high": close + 0.2, "low": close - 0.2, "close": close, "volume": np.full(len(idx), 1000.0),
    }, index=idx)
    assert fg.entry_minute_of(4, 1) == 5
    assert fg.entry_minute_of(3, 1) is None
    assert fg.entry_minute_of(374, 1) == 375
    assert fg.entry_minute_of(375, 1) is None
    assert fg.entry_minute_of(30, 3) == 33
    ts = idx[30]
    bars = fg.to_tf(df, 3)
    assert bars.loc[ts, "close"] == pytest.approx(df.iloc[32]["close"])
    later = df.copy()
    later.iloc[33, later.columns.get_loc("close")] = 999.0
    assert fg.to_tf(later, 3).loc[ts, "close"] == pytest.approx(bars.loc[ts, "close"])
    inside = df.copy()
    inside.iloc[32, inside.columns.get_loc("close")] = 999.0
    assert fg.to_tf(inside, 3).loc[ts, "close"] == pytest.approx(999.0)
    fear, _greed = fg.fear_greed(bars)
    tail = df.copy()
    tail.iloc[-1, tail.columns.get_loc("low")] = 1.0
    fear_tail, _g = fg.fear_greed(fg.to_tf(tail, 3))
    np.testing.assert_allclose(fear[:-1], fear_tail[:-1], equal_nan=True)


def _frames(n_days=8):
    days = pd.bdate_range("2026-09-01", periods=n_days)
    frames = {}
    for sym, base in (("SPY", 500.0), ("QQQ", 450.0)):
        parts = []
        for day in days:
            start = pd.Timestamp(day).tz_localize(NY) + pd.Timedelta(hours=9, minutes=30)
            idx = pd.date_range(start, periods=390, freq="1min")
            close = np.full(390, base)
            close[60:90] = base * 1.01
            parts.append(pd.DataFrame({
                "open": close,
                "high": close + 0.4,
                "low": close - 0.4,
                "close": close,
                "volume": np.full(390, 1000.0),
            }, index=idx))
        frames[sym] = pd.concat(parts)
    return frames


def test_synth_run_writes_the_report_without_keys(tmp_path, monkeypatch):
    monkeypatch.setenv("FG_SYNTH", "1")
    monkeypatch.setenv("FG_DAYS", "6")
    monkeypatch.setenv("FG_TFS", "1")
    monkeypatch.setenv("FG_BOOT", "20")
    monkeypatch.setenv("FG_OUT", str(tmp_path))
    monkeypatch.setenv("FG_SYMBOLS", "SPY,QQQ")
    monkeypatch.delenv("ALPACA_KEY", raising=False)
    monkeypatch.delenv("ALPACA_SECRET", raising=False)
    monkeypatch.setattr(fg.sc, "_load_underlying", lambda *_a, **_k: _frames(8))
    fg.main()
    report = (tmp_path / "FGFADE.md").read_text()
    assert report.startswith("# Fear-greed fade\n")
    assert "all three" in report
    assert "9-bar" in report
    assert "1.5" in report
    assert "2026-10-19 through 2026-10-23 are not in this run." in report
    summary = (tmp_path / "fgfade_summary.csv").read_text().strip().splitlines()
    assert len(summary) == 1 + 320 * 2 * 2
    folds = (tmp_path / "fgfade_folds.csv").read_text().strip().splitlines()
    assert len(folds) == 1 + 5 + 1
    assert (tmp_path / "fgfade_trades.csv").exists()


def test_missing_keys_write_a_report_and_stop(tmp_path, monkeypatch):
    monkeypatch.delenv("ALPACA_KEY", raising=False)
    monkeypatch.delenv("ALPACA_SECRET", raising=False)
    monkeypatch.delenv("FG_SYNTH", raising=False)
    monkeypatch.setenv("FG_OUT", str(tmp_path))
    with pytest.raises(SystemExit, match="ALPACA_KEY"):
        fg.main()
    text = (tmp_path / "FGFADE.md").read_text()
    assert "ALPACA_KEY" in text
    assert "No orders" in text


def test_workflow_is_manual_and_cannot_push_main():
    text = open(".github/workflows/fgfade.yml").read()
    assert text.startswith("name: Fear-greed fade (real option prices)\n")
    assert "workflow_dispatch:" in text
    assert "schedule:" not in text
    assert "ALPACA_KEY: ${{ secrets.ALPACA_KEY }}" in text
    assert "ALPACA_SECRET: ${{ secrets.ALPACA_SECRET }}" in text
    assert 'git push origin "HEAD:${BRANCH}"' in text
    assert "Refusing to push results" in text
    assert "main|master" in text
    assert '[[ "$BRANCH" =~ ^[A-Za-z0-9._/-]+$ ]]' in text
    assert 'HEADBR="$(git rev-parse --abbrev-ref HEAD)"' in text
    assert "mkdir -p /tmp/fgfade-out" in text
    assert "rm -f results/FGFADE.md" in text
    assert 'git checkout -B "$BRANCH"' in text
    assert 'default: "fgfade-results"' in text
    assert 'default: "120"' in text
    assert 'default: "1,3,5"' in text
    assert "python -m pytest -q tests/test_fgfade.py" in text
    assert "results/FGFADE.md" in text
    assert "results/fgfade_summary.csv" in text
    assert "results/fgfade_trades.csv" in text
    assert "results/fgfade_folds.csv" in text
    readme = open("README.md").read()
    assert "Fear-greed fade (real option prices)" in readme
    assert "Run workflow" in readme
    assert "Do not tap Re-run" in readme
    assert "fgfade-results" in readme
    for banned in ("submit_order", "TradingClient", "MarketOrderRequest"):
        assert banned not in text
        assert banned not in open("fgfade.py").read()
