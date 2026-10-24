"""Offline tests for scalp exit fills and entry timing. No network and no orders."""

import math
from datetime import date

import numpy as np
import pandas as pd
import pytest

import scalp_real as sc

NY = sc.NY
COSTS = (0.01, 0.005, 0.65)


def _opt(price=1.0, real=None):
    rec = sc._empty_opt()
    rec["open"][:] = price
    rec["high"][:] = price
    rec["low"][:] = price
    rec["close"][:] = price
    rec["lab"][:] = price
    rec["real"][:] = True if real is None else real
    return rec


def _und(day, spot=500.0):
    rec = {k: np.full(sc.N_MIN, spot) for k in ("open", "high", "low", "close")}
    rec["real"] = np.ones(sc.N_MIN, dtype=bool)
    return {day: rec}


def test_entry_minute_is_the_bar_after_the_signal_closes():
    # 1-minute bar starting 10:00 (session minute 30) closes at 10:01.
    assert sc.entry_session_minute(30, 1) == 31
    # 3-minute bar starting 10:00 covers session minutes 30, 31, 32 and closes at 33.
    entry = sc.entry_session_minute(30, 3)
    assert entry == 33
    assert entry > 32

    start = pd.Timestamp("2026-10-01 10:00", tz=NY)
    found = sc.entry_minute_from_timestamp(start, 3)
    assert found == (33, date(2026, 10, 1))
    # A bar that would enter at or after 15:55 is not an entry.
    late = pd.Timestamp("2026-10-01 15:54", tz=NY)
    assert sc.entry_minute_from_timestamp(late, 1) is None


def test_fill_uses_the_entry_bar_not_the_signal_bar():
    opt = _opt(1.0)
    opt["high"][19] = 50.0  # a target sitting on the signal minute must be ignored
    opt["open"][20:] = 2.0
    opt["high"][20:] = 2.02
    opt["low"][20:] = 1.98
    opt["close"][20:] = 2.0
    opt["lab"] = opt["close"].copy()
    got = sc.simulate_trade(opt, 20, (0.50, 0.20, 3), COSTS)
    assert got["status"] == "fill"
    assert got["entry_min"] == 20
    assert got["reason"] == "time"
    assert got["raw_entry"] == pytest.approx(2.0)


def test_second_minute_is_used_when_the_first_has_no_print():
    opt = _opt(1.0)
    opt["real"][20] = False
    opt["open"][20] = np.nan
    got = sc.simulate_trade(opt, 20, (0.50, 0.20, 2), COSTS, allow_slip=True)
    assert got["status"] == "fill"
    assert got["entry_min"] == 21


def test_no_print_within_two_minutes_is_skipped():
    opt = _opt(1.0)
    opt["real"][20] = False
    opt["real"][21] = False
    got = sc.simulate_trade(opt, 20, (0.10, 0.10, 5), COSTS)
    assert got["status"] == "skip_entry"


def test_take_profit_fills_at_the_target_not_the_high():
    opt = _opt(1.0)
    opt["open"][10] = 1.0
    opt["high"][10] = 5.0
    got = sc.simulate_trade(opt, 10, (0.20, 0.20, 10), COSTS, allow_slip=False)
    assert got["reason"] == "tp"
    # Target is 1.20. Half-spread is max(0.01, 0.5% of 1.20) = 0.01. Credit = 1.19.
    assert got["exit"] == pytest.approx(1.19)


def test_stop_wins_when_the_same_bar_hits_both_and_a_gap_fills_at_the_open():
    opt = _opt(1.0)
    opt["open"][10] = 1.0
    opt["high"][10] = 2.0
    opt["low"][10] = 0.5
    both = sc.simulate_trade(opt, 10, (0.10, 0.10, 10), COSTS, allow_slip=False)
    assert both["reason"] == "stop"
    # Stop level 0.90, bar opened at 1.00, so the stop fills at 0.90 before the half-spread.
    assert both["exit"] == pytest.approx(0.90 - 0.01)

    opt["open"][10] = 1.0
    opt["high"][10] = 1.0
    opt["low"][10] = 1.0
    opt["close"][10] = 1.0
    opt["open"][11] = 0.40
    opt["high"][11] = 0.45
    opt["low"][11] = 0.30
    opt["close"][11] = 0.42
    gap = sc.simulate_trade(opt, 10, (0.50, 0.10, 10), COSTS, allow_slip=False)
    assert gap["reason"] == "stop"
    assert gap["exit_min"] == 11
    assert gap["exit"] == pytest.approx(0.40 - 0.01)


def test_time_stop_flat_and_no_stop():
    opt = _opt(1.0)
    timed = sc.simulate_trade(opt, 10, (0.50, None, 5), COSTS, allow_slip=False)
    assert timed["reason"] == "time"
    assert timed["exit_min"] == 15

    late = sc.simulate_trade(opt, 380, (0.50, None, 30), COSTS, allow_slip=False)
    assert late["reason"] == "flat"
    assert late["exit_min"] == sc.FLAT_MIN


def test_stale_exit_is_skipped_and_a_five_minute_carry_is_allowed():
    opt = _opt(1.0, real=np.zeros(sc.N_MIN, dtype=bool))
    opt["real"][10] = True
    opt["open"][10] = 1.0
    opt["high"][10] = 1.0
    opt["low"][10] = 1.0
    opt["close"][10] = 1.0
    opt["lab"][:] = np.nan
    opt["lab"][10:16] = 1.0  # this minute plus five carried minutes, matching ffill(limit=5)

    carried = sc.simulate_trade(opt, 10, (0.50, 0.50, 5), COSTS, allow_slip=False)
    assert carried["status"] == "fill"
    assert carried["exit_min"] == 15
    assert carried["reason"] == "time"

    stale = sc.simulate_trade(opt, 10, (0.50, 0.50, 6), COSTS, allow_slip=False)
    assert stale["status"] == "skip_stale"


def test_costs_and_commission_on_a_time_exit():
    opt = _opt(1.0)
    opt["close"][:] = 1.10
    opt["open"][:] = 1.10
    opt["high"][:] = 1.10
    opt["low"][:] = 1.10
    opt["lab"][:] = 1.10
    opt["open"][10] = 1.00
    got = sc.simulate_trade(opt, 10, (0.50, 0.50, 1), COSTS, allow_slip=False)
    debit = 1.00 + 0.01
    credit = 1.10 - 0.01
    dollar = (credit - debit) * 100 - 1.30
    assert got["entry"] == pytest.approx(debit)
    assert got["exit"] == pytest.approx(credit)
    assert got["dollar"] == pytest.approx(dollar)
    assert got["net_pct"] == pytest.approx(dollar / (debit * 100) * 100)


def test_one_position_blocks_overlap_and_calls_go_first():
    day = date(2026, 10, 1)
    opt = _opt(1.0)
    import backtest as bt
    contract = bt.lab_occ("SPY", day, "C", 500)
    put = bt.lab_occ("SPY", day, "P", 500)
    und = {"SPY": _und(day)}
    book = {(day, contract): opt, (day, put): opt}
    events = [
        {"day": day, "symbol": "SPY", "side": -1, "entry_min": 30},
        {"day": day, "symbol": "SPY", "side": 1, "entry_min": 30},
        {"day": day, "symbol": "SPY", "side": 1, "entry_min": 35},
        {"day": day, "symbol": "SPY", "side": 1, "entry_min": 41},
    ]
    trades, attempts, _skips = sc.run_book(events, book, und, "atm", (0.30, 0.30, 10), COSTS, "orb_1m")
    # Call at minute 30 is taken (the put at that minute is sorted behind it). It exits at 40.
    # Minute 35 is still inside that trade, so it is not an attempt. Minute 41 is a new trade.
    assert [t["entry_min"] for t in trades] == [30, 41]
    assert trades[0]["side"] == "CALL"
    assert len(attempts) == 2


def test_breakeven_hit_rate_matches_the_two_outcome_equation():
    p = sc.breakeven_hit_rate(0.20, 0.20, 2.0, 0.01, 0.005, 0.65)
    debit = 2.0 + max(0.01, 0.005 * 2.0)
    win = 2.4 - max(0.01, 0.005 * 2.4)
    loss = 1.6 - max(0.01, 0.005 * 1.6)
    net_w = (win - debit) * 100 - 1.30
    net_l = (loss - debit) * 100 - 1.30
    assert p == pytest.approx(-net_l / (net_w - net_l))
    assert math.isnan(sc.breakeven_hit_rate(0.20, None, 2.0, 0.01, 0.005, 0.65))


def test_clustered_t_needs_at_least_two_days():
    t, p = sc.clustered_t([1.0, 2.0, 3.0], [0, 0, 0], 1)
    assert math.isnan(t) and math.isnan(p)
    t2, p2 = sc.clustered_t([1.0, 1.0, 3.0, 5.0], [0, 0, 1, 1], 2)
    assert math.isfinite(t2) and math.isfinite(p2)
    assert sc.norm_ppf(0.975) == pytest.approx(1.95996398454, abs=1e-6)
    assert sc.norm_sf(1.95996398454) == pytest.approx(0.05, abs=1e-4)
    q = sc.benjamini_hochberg([0.04, 0.01, float("nan"), 0.03])
    finite = np.sort(q[np.isfinite(q)])
    assert np.all(np.diff(finite) >= -1e-12)
    assert q[1] <= q[2] or not np.isfinite(q[2])
    assert abs(q[np.isfinite(q)].max() - 0.04) < 1e-9


def test_select_top_uses_only_the_rows_it_is_given_and_ranks_by_difference_t():
    rows = [
        {"n": 4, "n_paired": 10, "t_diff": 9, "mean_net_pct": 5, "signal": "too_small"},
        {"n": 10, "n_paired": 10, "t_diff": 1.0, "mean_net_pct": 9, "signal": "richer"},
        {"n": 10, "n_paired": 10, "t_diff": 2.0, "mean_net_pct": 0.1, "signal": "stronger"},
        {"n": 10, "n_paired": 3, "t_diff": 8, "mean_net_pct": 1, "signal": "unpaired"},
    ]
    picked = sc.select_top(rows, k=1)
    assert [r["signal"] for r in picked] == ["stronger"]


def test_vix_skip_flags_match_the_frozen_rules():
    quiet = dict(side=1, color=2, close=100, vwap=100, atr=1, day_open=100, angle=0,
                 ttm_m=0.2, ttm_m_prev=0.1, vix_now=96, vix_prev2=90)
    assert sc.vix_skip_flags(**quiet) == []
    assert 1 in sc.vix_skip_flags(**{**quiet, "color": -2})
    assert 2 in sc.vix_skip_flags(**{**quiet, "close": 96, "vwap": 100, "atr": 1})
    assert 3 in sc.vix_skip_flags(**{**quiet, "close": 99, "day_open": 100})
    assert 4 in sc.vix_skip_flags(**{**quiet, "angle": -15})
    assert 5 in sc.vix_skip_flags(**{**quiet, "ttm_m": -0.2, "ttm_m_prev": -0.4})
    assert 6 in sc.vix_skip_flags(**{**quiet, "vix_now": 80, "vix_prev2": 60})
    assert 6 not in sc.vix_skip_flags(**{**quiet, "vix_now": 95, "vix_prev2": 60})  # 35 points is the 30+ bin


def test_opening_range_fires_once_per_side_after_the_range():
    day = date(2026, 10, 1)
    sess = _und(day, 100)[day]
    sess["high"][:15] = 101
    sess["low"][:15] = 99
    sess["close"][:] = 100
    sess["close"][20] = 102
    sess["close"][21] = 103
    sess["close"][30] = 98
    sess["close"][31] = 97
    ev = sc.orb_events(sess, day, {day})
    assert [(e["side"], e["entry_min"]) for e in ev] == [(1, 21), (-1, 31)]


def test_unison_direction_and_flip_use_only_the_three_bar_window():
    n = 12
    day = np.array([date(2026, 10, 1)] * n)
    fear = np.zeros(n)
    greed = np.zeros(n)
    fear[5] = 85
    greed[6] = 85
    close = np.full(n, 100.0)
    ema = np.full(n, 101.0)  # close is below the EMA -> call as written
    bundle = {"fear": fear, "greed": greed, "ema13": ema, "ind": {"day": day, "c": close, "hm": np.full(n, 1000)}}
    long_m, short_m = sc.unison_masks(bundle, False)
    assert long_m[6] and not short_m[6]
    assert not long_m[:6].any()
    flipped_l, flipped_s = sc.unison_masks(bundle, True)
    assert flipped_s[6] and not flipped_l[6]
    # A Greed print on the previous day must not complete today's Fear bar.
    day2 = np.array([date(2026, 9, 30)] * 3 + [date(2026, 10, 1)] * (n - 3))
    fear2 = np.zeros(n)
    greed2 = np.zeros(n)
    greed2[2] = 90
    fear2[3] = 90
    bundle["fear"], bundle["greed"] = fear2, greed2
    bundle["ind"] = {"day": day2, "c": close, "hm": np.full(n, 1000)}
    long2, short2 = sc.unison_masks(bundle, False)
    assert not long2[3] and not short2[3]


def test_filtered_vix_cross_is_a_subset_and_signals_do_not_look_ahead():
    rng = np.random.default_rng(0)
    idx = pd.date_range("2026-10-01 04:00", periods=1200, freq="1min", tz=NY)
    steps = rng.normal(0, 0.0004, len(idx))
    close = 500 * np.exp(np.cumsum(steps))
    df = pd.DataFrame({
        "open": np.r_[close[0], close[:-1]],
        "high": close * 1.001,
        "low": close * 0.999,
        "close": close,
        "volume": np.full(len(idx), 1000.0),
    }, index=idx)
    bundle = sc.chart_bundle(df)
    raw_l, raw_s = sc.vix95_masks(bundle, False)
    fil_l, fil_s = sc.vix95_masks(bundle, True)
    assert not np.any(fil_l & ~raw_l)
    assert not np.any(fil_s & ~raw_s)

    prefix = df.iloc[:-40]
    b2 = sc.chart_bundle(prefix)
    for builder in (
        lambda b, frame: sc.vix95_masks(b, False),
        lambda b, frame: sc.vix95_masks(b, True),
        lambda b, frame: sc.squeeze_masks(frame, b),
        lambda b, frame: sc.ema_flip_masks(b),
        lambda b, frame: sc.unison_masks(b, False),
        lambda b, frame: sc.angle_flat_masks(frame, b),
    ):
        a_l, a_s = builder(bundle, df)
        b_l, b_s = builder(b2, prefix)
        cut = len(prefix) - 1
        assert np.array_equal(a_l[:cut], b_l[:cut])
        assert np.array_equal(a_s[:cut], b_s[:cut])


def test_paired_random_stays_in_the_bucket_and_is_stable():
    day = date(2026, 10, 1)
    und = {"SPY": _und(day)}
    attempt = {
        "day": day, "symbol": "SPY", "entry_min": 40, "side": 1,
        "signal": "orb_1m", "strike": "atm", "attempt_id": "a1",
    }
    first = sc.paired_entry(attempt, und)
    second = sc.paired_entry(attempt, und)
    assert first["entry_min"] == second["entry_min"]
    assert first["entry_min"] != 40
    assert first["entry_min"] // 30 == 40 // 30
    assert first["side"] == 1


def test_lab_fetch_opt_carry_matches_the_five_minute_rule():
    day = date(2026, 10, 1)
    start = pd.Timestamp(day, tz=NY) + pd.Timedelta(hours=9, minutes=30)
    times = [start, start + pd.Timedelta(minutes=1)]
    symbol = "SPY251001C00500000"
    frame = pd.DataFrame(
        {"open": [1.0, 1.1], "high": [1.05, 1.15], "low": [0.95, 1.05], "close": [1.0, 1.2], "volume": [10, 10]},
        index=pd.MultiIndex.from_arrays([[symbol, symbol], times], names=["symbol", "timestamp"]),
    )

    class _Bag:
        def __init__(self, df):
            self.df = df

    class _Client:
        def get_option_bars(self, req):
            return _Bag(frame)

    got = sc.fetch_option_day(_Client(), [symbol], day)
    rec = got[symbol]
    assert rec["real"][0] and rec["real"][1]
    assert not rec["real"][2]
    assert rec["open"][1] == pytest.approx(1.1)
    # lab_fetch_opt forward-fills at most 5 minutes: minute 6 is the last carry, minute 7 is empty.
    assert np.isfinite(rec["lab"][6])
    assert rec["lab"][6] == pytest.approx(1.2)
    assert not np.isfinite(rec["lab"][7])


def test_predeclared_grid_matches_the_code_and_names_every_signal():
    text = sc.render_predeclared()
    body = text.split("CONFIGS\n", 1)[1].strip().splitlines()
    expected = [
        f"{sig},{strike},{tp:.2f},{sc._fmt_sl(sl)},{ts},{'baseline' if sig == 'random' else 'search'}"
        for sig, strike, tp, sl, ts in sc.iter_configs()
    ]
    assert body == expected
    assert "Written before any OPRA computation" in text
    for sid in sc.SIGNAL_IDS:
        assert sid in text
    assert sc.search_config_count() == 14 * 2 * 4 * 5 * 4
    on_disk = open("results/SCALP_REAL_PREDECLARED.txt").read()
    assert on_disk == text


def test_tuned_diamond_constants_match_the_bot_and_this_file_places_no_orders():
    import diamondbot
    assert diamondbot.BOOKS["TUNED"] == sc.TUNED_DIAMOND
    assert (diamondbot.ENTRY_FROM, diamondbot.ENTRY_TO) == (sc.DIAMOND_ENTRY_FROM, sc.DIAMOND_ENTRY_TO)
    src = open("scalp_real.py").read()
    for banned in ("submit_order", "TradingClient", "MarketOrderRequest", "LimitOrderRequest", "place_order"):
        assert banned not in src
    # The diamond is read from the bot. The order path in that module is not referenced.
    assert "diamondbot.diamonds" in src
    assert "open_trade" not in src


def test_workflow_is_manual_data_only_and_cannot_push_main():
    text = open(".github/workflows/scalp_real.yml").read()
    assert "workflow_dispatch:" in text
    assert "schedule:" not in text
    assert "ALPACA_KEY: ${{ secrets.ALPACA_KEY }}" in text
    assert "ALPACA_SECRET: ${{ secrets.ALPACA_SECRET }}" in text
    assert 'git push origin "HEAD:${BRANCH}"' in text
    assert "Refusing to push results" in text
    assert "main|master" in text
    for banned in ("submit_order", "TradingClient", "MarketOrderRequest"):
        assert banned not in text
