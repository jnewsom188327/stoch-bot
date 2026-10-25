"""Offline tests for scalp exit fills and entry timing. No network and no orders."""

import json
import math
from datetime import date, timedelta

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


def test_otm_strike_price_for_calls_and_puts():
    # 500.2 rounds to 500. OTM is the mirror of the 2itm offset.
    assert sc.strike_price(500.2, 1, "1otm") == 501
    assert sc.strike_price(500.2, -1, "1otm") == 499
    assert sc.strike_price(500.2, 1, "2otm") == 502
    assert sc.strike_price(500.2, -1, "2otm") == 498
    assert sc.strike_price(501.6, 1, "1otm") == 503  # round(501.6) + 1
    assert sc.strike_price(501.6, -1, "2otm") == 500  # round(501.6) - 2
    assert "1otm" in sc.STRIKE_MODES and "2otm" in sc.STRIKE_MODES


def test_default_strike_modes_and_family_n_stay_2240():
    # No new inputs: the default strike string is still 2itm,atm, in the original order.
    assert sc._parse_strikes("2itm,atm") == ("atm", "2itm")
    assert sc.family_strike_modes(None) == ("atm", "2itm")
    assert sc.family_strike_modes(("atm", "2itm")) == ("atm", "2itm")
    assert sc.family_strike_modes(("atm",)) == ("atm", "2itm")
    assert sc.family_strike_modes(("2itm",)) == ("atm", "2itm")
    assert sc.search_config_count() == 2240
    assert sc.search_config_count(("2itm", "atm")) == 2240
    assert sc.search_config_count(("atm",)) == 14 * 2 * 4 * 5 * 4
    # A run that includes the new strikes counts the modes it actually runs.
    assert sc.search_config_count(("1otm",)) == 14 * 1 * 4 * 5 * 4
    assert sc.search_config_count(("1otm", "2otm")) == 14 * 2 * 4 * 5 * 4
    assert sc.search_config_count(("atm", "2itm", "1otm", "2otm")) == 14 * 4 * 4 * 5 * 4
    assert "full grid" in sc.family_note(("1otm",))
    # atm and 2itm prices are the original formulas.
    assert sc.strike_price(500.2, 1, "atm") == 500
    assert sc.strike_price(500.2, -1, "atm") == 500
    assert sc.strike_price(500.2, 1, "2itm") == 498
    assert sc.strike_price(500.2, -1, "2itm") == 502
    assert sc.strike_price(501.6, 1, "2itm") == 500
    assert sc.strike_price(501.6, -1, "2itm") == 504
    grid_strikes = {strike for _sig, strike, _tp, _sl, _ts in sc.iter_configs()}
    assert grid_strikes == {"atm", "2itm"}
    with pytest.raises(SystemExit) as ei:
        sc._parse_strikes("3otm")
    msg = str(ei.value)
    assert "1otm" in msg and "2otm" in msg and "atm" in msg
    assert sc._parse_strikes("2otm,1otm,atm") == ("atm", "1otm", "2otm")


def test_premium_band_skip_is_counted_and_applied_to_controls():
    import backtest as bt
    day = date(2026, 10, 1)
    und = {"SPY": _und(day, 500)}
    contract = bt.lab_occ("SPY", day, "C", 500)
    opt = _opt(0.60)
    opt["open"][40] = 0.30
    opt["high"][40] = 0.30
    opt["low"][40] = 0.30
    opt["close"][40] = 0.30
    opt["open"][80] = 0.81
    opt["high"][80] = 0.81
    opt["low"][80] = 0.81
    opt["close"][80] = 0.81
    book = {(day, contract): opt}
    band = (0.45, 0.80)
    events = [
        {"day": day, "symbol": "SPY", "side": 1, "entry_min": 40},
        {"day": day, "symbol": "SPY", "side": 1, "entry_min": 50},
        {"day": day, "symbol": "SPY", "side": 1, "entry_min": 80},
    ]
    trades, attempts, skips = sc.run_book(
        events, book, und, "atm", (0.30, 0.30, 5), COSTS, "orb_1m", premium=band,
    )
    assert [t["entry_min"] for t in trades] == [50]
    assert trades[0]["raw_entry"] == pytest.approx(0.60)
    assert skips["skip_premium"] == 2
    assert sum(1 for a in attempts if a["status"] == "skip_premium") == 2
    # Inclusive edges are entries. Just outside is a premium skip.
    for price, taken in ((0.45, True), (0.80, True), (0.44, False), (0.81, False)):
        edged = _opt(price)
        got, _att, sk = sc.run_book(
            [{"day": day, "symbol": "SPY", "side": 1, "entry_min": 40}],
            {(day, contract): edged}, und, "atm", (0.30, None, 2), COSTS, "orb_1m", premium=band,
        )
        assert (len(got) == 1) is taken
        assert sk["skip_premium"] == (0 if taken else 1)
    # No band: the cheap print is still a trade. Default behavior does not count premium skips.
    open_book, _att, open_skips = sc.run_book(
        [{"day": day, "symbol": "SPY", "side": 1, "entry_min": 40}],
        book, und, "atm", (0.30, None, 2), COSTS, "random",
    )
    assert len(open_book) == 1 and open_skips["skip_premium"] == 0
    # Paired controls use the same band. 0.30 is skipped and counted; 0.60 is taken.
    controls = [
        {"day": day, "symbol": "SPY", "side": 1, "entry_min": 40, "attempt_id": "cheap"},
        {"day": day, "symbol": "SPY", "side": 1, "entry_min": 50, "attempt_id": "mid"},
    ]
    filled, prem = sc.simulate_controls(controls, book, und, (0.30, None, 2), COSTS, "atm", premium=band)
    assert [t["attempt_id"] for t in filled] == ["mid"]
    assert [s["attempt_id"] for s in prem] == ["cheap"]
    # The reference random book is run_book, so the same skip applies there too.
    ref, _att, ref_skips = sc.run_book(
        [{"day": day, "symbol": "SPY", "side": 1, "entry_min": 40}],
        book, und, "1otm", (0.30, None, 2), COSTS, "random", premium=band,
    )
    # 1otm call at spot 500 is strike 501, which this book does not contain, so this is an entry skip.
    # Use the atm contract for the reference path above; repeat on atm to show the count.
    assert ref == []
    ref2, _att, ref_skips2 = sc.run_book(
        [{"day": day, "symbol": "SPY", "side": 1, "entry_min": 40}],
        book, und, "atm", (0.30, None, 2), COSTS, "random", premium=band,
    )
    assert ref2 == [] and ref_skips2["skip_premium"] == 1


def test_last_entry_cutoff_blocks_signal_and_control():
    import backtest as bt
    day = date(2026, 10, 1)
    und = {"SPY": _und(day)}
    contract = bt.lab_occ("SPY", day, "C", 500)
    book = {(day, contract): _opt(1.0)}
    # 14:00 ET is session minute 270. Entries at or after it are out.
    window = (None, sc.parse_clock_et("14:00", "SCALP_LAST_ENTRY")[1])
    assert window == (None, 270)
    events = [
        {"day": day, "symbol": "SPY", "side": 1, "entry_min": 269},
        {"day": day, "symbol": "SPY", "side": 1, "entry_min": 270},
    ]
    trades, attempts, _skips = sc.run_book(
        events, book, und, "atm", (0.30, None, 2), COSTS, "orb_1m", entry_window=window,
    )
    assert [t["entry_min"] for t in trades] == [269]
    assert [a["entry_min"] for a in attempts] == [269]
    # A missing print at 13:59 must not slip into 14:00.
    slipped = _opt(1.0)
    slipped["real"][269] = False
    slipped["open"][269] = np.nan
    late_only, _att, late_skips = sc.run_book(
        [{"day": day, "symbol": "SPY", "side": 1, "entry_min": 269}],
        {(day, contract): slipped}, und, "atm", (0.30, None, 2), COSTS, "orb_1m", entry_window=window,
    )
    assert late_only == []
    assert late_skips["skip_premium"] == 0
    controls = [
        {"day": day, "symbol": "SPY", "side": 1, "entry_min": 270, "attempt_id": "late"},
        {"day": day, "symbol": "SPY", "side": 1, "entry_min": 260, "attempt_id": "ok"},
    ]
    filled, prem = sc.simulate_controls(
        controls, book, und, (0.30, None, 2), COSTS, "atm", entry_window=window,
    )
    assert [t["attempt_id"] for t in filled] == ["ok"]
    assert prem == []
    # Default window still allows 14:00 and still blocks the 15:55 bar.
    open_window, _att, _sk = sc.run_book(
        [{"day": day, "symbol": "SPY", "side": 1, "entry_min": 270},
         {"day": day, "symbol": "SPY", "side": 1, "entry_min": 384},
         {"day": day, "symbol": "SPY", "side": 1, "entry_min": 385}],
        book, und, "atm", (0.50, None, 2), COSTS, "random",
    )
    assert [t["entry_min"] for t in open_window] == [270, 384]


def test_first_entry_cutoff_blocks_signal_and_control():
    import backtest as bt
    day = date(2026, 10, 1)
    und = {"SPY": _und(day)}
    contract = bt.lab_occ("SPY", day, "C", 500)
    book = {(day, contract): _opt(1.0)}
    # 13:00 ET is session minute 210. Nothing before it is an entry.
    window = (sc.parse_clock_et("13:00", "SCALP_FIRST_ENTRY")[1], None)
    assert window == (210, None)
    events = [
        {"day": day, "symbol": "SPY", "side": 1, "entry_min": 209},
        {"day": day, "symbol": "SPY", "side": 1, "entry_min": 210},
    ]
    trades, attempts, _skips = sc.run_book(
        events, book, und, "atm", (0.30, None, 2), COSTS, "orb_1m", entry_window=window,
    )
    assert [t["entry_min"] for t in trades] == [210]
    assert [a["entry_min"] for a in attempts] == [210]
    # A 12:59 signal must not become an entry by slipping onto 13:00.
    slipped = _opt(1.0)
    slipped["real"][209] = False
    slipped["open"][209] = np.nan
    early, _att, _sk = sc.run_book(
        [{"day": day, "symbol": "SPY", "side": 1, "entry_min": 209}],
        {(day, contract): slipped}, und, "atm", (0.30, None, 2), COSTS, "random", entry_window=window,
    )
    assert early == []
    controls = [
        {"day": day, "symbol": "SPY", "side": 1, "entry_min": 209, "attempt_id": "early"},
        {"day": day, "symbol": "SPY", "side": 1, "entry_min": 210, "attempt_id": "ok"},
    ]
    filled, prem = sc.simulate_controls(
        controls, book, und, (0.30, None, 2), COSTS, "atm", entry_window=window,
    )
    assert [t["attempt_id"] for t in filled] == ["ok"]
    assert prem == []
    # Empty inputs: no extra cutoff. 12:59 is still an entry.
    assert sc.parse_clock_et("", "SCALP_FIRST_ENTRY") == (None, None)
    assert sc.parse_clock_et("  ", "SCALP_LAST_ENTRY") == (None, None)
    before, _att, _sk = sc.run_book(
        [{"day": day, "symbol": "SPY", "side": 1, "entry_min": 209}],
        book, und, "atm", (0.30, None, 2), COSTS, "orb_1m",
    )
    assert [t["entry_min"] for t in before] == [209]


def test_entry_hour_breakdown_and_report_state_the_new_rules():
    trades = [
        {"time": "09:40", "net_pct": 10.0},
        {"time": "09:50", "net_pct": -2.0},
        {"time": "13:05", "net_pct": 4.0},
        {"time": "15:10", "net_pct": -1.0},
    ]
    got = sc.entry_hour_breakdown(trades)
    assert list(got) == [9, 10, 11, 12, 13, 14, 15]
    assert got[9]["n"] == 2 and got[9]["net_pct"] == pytest.approx(4.0)
    assert got[10]["n"] == 0 and math.isnan(got[10]["net_pct"])
    assert got[13]["n"] == 1 and got[13]["net_pct"] == pytest.approx(4.0)
    assert got[15]["net_pct"] == pytest.approx(-1.0)
    meta = {
        "stamp": "2026-10-24 16:00 ET",
        "synthetic": False,
        "coverage": "Symbols SPY, QQQ. Strikes: 1otm.",
        "cent_floor": 0.01,
        "pct": 0.005,
        "commission": 0.65,
        "n_is": 10,
        "n_oos": 3,
        "is_first": "2026-08-01",
        "is_last": "2026-10-01",
        "oos_first": "2026-10-02",
        "oos_last": "2026-10-06",
        "n_family": 1120,
        "t_crit": sc.norm_ppf(1 - (0.05 / 1120) / 2),
        "skip_note": "premium skips included.",
        "family_note": sc.family_note(("1otm",)),
        "premium_line": sc.describe_premium((0.45, 0.80)),
        "window_line": sc.describe_window("13:00", "15:00"),
        "hour_table": [{
            "book": "signal", "signal": "orb_1m", "strike": "1otm",
            "tp": 0.20, "sl": 0.20, "time_stop": 10,
            "hours": got,
        }],
    }
    text = sc.render_report(meta, [], [])
    assert "Descriptive only, not used for selection" in text
    assert "Break-even hit rate at $0.60" in text
    assert "Break-even hit rate at $2.00" in text
    assert "$0.45" in text and "$0.80" in text
    assert "before 13:00 ET" in text and "at or after 15:00 ET" in text
    assert "Search family N = 1120" in text
    assert "not used to rank" in text
    p60 = sc.breakeven_hit_rate(0.20, 0.20, 0.60, 0.01, 0.005, 0.65)
    assert f"{p60 * 100:.1f}%" in text
    pre = sc.render_predeclared()
    assert "1otm call = round(spot) + 1" in pre
    assert "2otm put = round(spot) - 2" in pre
    assert "SCALP_PREMIUM_MIN" in pre and "skips_premium" in pre
    assert "SCALP_FIRST_ENTRY" in pre and "SCALP_LAST_ENTRY" in pre
    assert "SCALP_VIX_MIN" in pre and "prior trading day" in pre
    assert "N = 2240" in pre


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
    assert "python -m pytest -q tests/test_scalp_real.py" in text
    assert "SCALP_PREMIUM_MIN:" in text
    assert "SCALP_PREMIUM_MAX:" in text
    assert "SCALP_FIRST_ENTRY:" in text
    assert "SCALP_LAST_ENTRY:" in text
    assert "SCALP_VIX_MIN:" in text
    assert "SCALP_VIX_MAX:" in text
    assert "vix_min:" in text
    assert "vix_max:" in text
    assert "14:00" in text
    assert 'default: "2itm,atm"' in text


def test_prior_vix_uses_the_previous_close_and_not_the_same_day():
    # Friday 2026-10-02, Monday 2026-10-05. Monday must use Friday, not Monday's own close.
    closes = {
        date(2026, 10, 2): 18.0,
        date(2026, 10, 5): 30.0,
        date(2026, 10, 6): 40.0,
    }
    assert sc.prior_vix_close(date(2026, 10, 5), closes) == 18.0
    assert sc.prior_vix_close(date(2026, 10, 6), closes) == 30.0
    past = {k: v for k, v in closes.items() if k < date(2026, 10, 5)}
    assert sc.prior_vix_close(date(2026, 10, 5), past) == sc.prior_vix_close(date(2026, 10, 5), closes)
    assert sc.prior_vix_close(date(2026, 10, 2), closes) is None
    # A future print must not leak backward.
    assert sc.prior_vix_close(date(2026, 10, 5), {date(2026, 10, 6): 99.0, date(2026, 10, 2): 18.0}) == 18.0


def test_vix_band_is_half_open_and_the_holdout_split_is_after_the_filter():
    days = [date(2026, 10, d) for d in (1, 2, 5, 6, 7, 8)]
    closes = {
        date(2026, 9, 30): 18.0,  # prior for Oct 1
        date(2026, 10, 1): 12.0,  # prior for Oct 2; Oct 1's own close must not drop Oct 1
        date(2026, 10, 2): 17.0,
        date(2026, 10, 5): 19.0,
        date(2026, 10, 6): 15.5,  # prior for Oct 7, below 16
        date(2026, 10, 7): 20.0,  # prior for Oct 8; 20 is not < 20
        date(2026, 10, 8): 21.0,
    }
    assert sc.assign_vix_bucket(15.99) == "<16"
    assert sc.assign_vix_bucket(16.0) == "16-20"
    assert sc.assign_vix_bucket(19.99) == "16-20"
    assert sc.assign_vix_bucket(20.0) == ">=20"
    assert sc.assign_vix_bucket(None) is None
    assert sc._prior_in_band(16.0, 16.0, None)
    assert not sc._prior_in_band(15.99, 16.0, None)
    assert not sc._prior_in_band(20.0, 16.0, 20.0)
    assert sc._prior_in_band(19.99, 16.0, 20.0)
    assert sc._prior_in_band(12.0, None, None)
    kept, dropped = sc.filter_days_by_vix(days, closes, 16.0, 20.0)
    # Oct 1 prior 18 keep. Oct 2 prior 12 drop. Oct 5 prior 17 keep.
    # Oct 6 prior 19 keep. Oct 7 prior 15.5 drop. Oct 8 prior 20 drop (max is exclusive).
    assert kept == [date(2026, 10, 1), date(2026, 10, 5), date(2026, 10, 6)]
    assert [d for d, _p in dropped] == [date(2026, 10, 2), date(2026, 10, 7), date(2026, 10, 8)]
    # Same-day close of Oct 1 is 12. Looking ahead would have dropped it.
    assert date(2026, 10, 1) in kept
    is_days, oos_days = sc._split(kept)
    assert is_days + oos_days == kept
    assert not (set(is_days) | set(oos_days)) & {d for d, _p in dropped}
    n_oos = max(1, int(round(len(kept) * sc.HOLD_FRAC)))
    assert oos_days == kept[-n_oos:]
    assert len(is_days) == len(kept) - len(oos_days)
    # Filter off keeps every day and drops none, including a day with no prior close.
    all_kept, none_dropped = sc.filter_days_by_vix(days, closes, None, None)
    assert all_kept == days and none_dropped == []
    with pytest.raises(SystemExit):
        sc.parse_vix_band(16.0, 16.0)
    line = sc.describe_vix_filter(16.0, None, kept, dropped, "FRED VIXCLS", len(is_days), len(oos_days))
    assert "Days kept: 3" in line and "Days dropped: 3" in line
    assert f"{len(is_days)} in-sample" in line and f"{len(oos_days)} held-out" in line
    assert "No lookahead" in line


def test_vix_parsers_and_a_failed_fetch_stops():
    text = "observation_date,VIXCLS\n2026-10-01,15.50\n2026-10-02,.\n2026-10-05,18\n"
    parsed = sc.parse_fred_vix_csv(text)
    assert parsed[date(2026, 10, 1)] == pytest.approx(15.50)
    assert date(2026, 10, 2) not in parsed
    assert sc.prior_vix_close(date(2026, 10, 5), parsed) == pytest.approx(15.50)
    # 07:00 UTC is still that calendar date in New York. A null close is skipped.
    stamp = 1790319600  # 2026-09-25 07:00 UTC
    payload = (
        '{"chart":{"result":[{"timestamp":[1790319600,1790406000],'
        '"indicators":{"quote":[{"close":[14.87,null]}]}}],"error":null}}'
    )
    yahoo = sc.parse_yahoo_vix_chart(payload)
    assert date(2026, 9, 25) in yahoo
    assert yahoo[date(2026, 9, 25)] == pytest.approx(14.87)
    assert stamp == 1790319600
    assert len(yahoo) == 1

    # More than 100 closes, so a short error page cannot pass the source check.
    extra = []
    for month in range(1, 6):
        for d in range(1, 29):
            extra.append(f"2021-{month:02d}-{d:02d},{16 + d / 100:.2f}")
    fred_body = "observation_date,VIXCLS\n" + "\n".join(extra)
    seen = []

    def transport(url, headers):
        seen.append((url, headers.get("User-Agent", "")))
        if "fredgraph" in url:
            return fred_body
        raise AssertionError("Yahoo should not be called when FRED parses")

    closes, source = sc.fetch_vix_closes(transport=transport)
    assert source == "FRED VIXCLS"
    assert len(closes) >= 100
    assert len(seen) == 1

    def fallback(url, headers):
        seen.append((url, headers.get("User-Agent", "")))
        if "fredgraph" in url:
            raise OSError("fred down")
        body = {
            "chart": {
                "result": [{
                    "timestamp": [1_600_000_000 + i * 86400 for i in range(120)],
                    "indicators": {"quote": [{"close": [16.5] * 120}]},
                }],
                "error": None,
            }
        }
        return json.dumps(body)

    seen.clear()
    closes, source = sc.fetch_vix_closes(transport=fallback)
    assert source == "Yahoo ^VIX"
    assert "Mozilla" in seen[1][1]
    assert "chart" in seen[1][0]

    def boom(url, headers):
        raise OSError("no network")

    with pytest.raises(SystemExit) as ei:
        sc.fetch_vix_closes(transport=boom)
    assert "VIX" in str(ei.value)
    assert "Refusing" in str(ei.value)


def test_vix_filter_keeps_the_same_days_for_the_random_book():
    day_drop = date(2026, 10, 2)
    day_keep = date(2026, 10, 5)
    closes = {date(2026, 10, 1): 12.0, date(2026, 10, 2): 18.0}
    # Oct 2 prior is 12 (drop if min is 16). Oct 5 prior is 18 (keep).
    kept, dropped = sc.filter_days_by_vix([day_drop, day_keep], closes, 16.0, None)
    assert kept == [day_keep]
    assert [d for d, _p in dropped] == [day_drop]
    sess = _und(day_keep)[day_keep]
    und = {"SPY": {day_drop: _und(day_drop)[day_drop], day_keep: sess}}
    events = {}
    for sid in sc.SEARCH_IDS:
        events[sid] = [
            {"day": day_drop, "symbol": "SPY"},
            {"day": day_keep, "symbol": "SPY"},
            {"day": day_keep, "symbol": "SPY"},
        ]
    window = (210, 300)
    full = sc.reference_random_events(events, und, ["SPY"], [day_drop, day_keep], window)
    part = sc.reference_random_events(events, und, ["SPY"], kept, window)
    assert all(e["day"] == day_keep for e in part)
    assert [(e["day"], e["entry_min"], e["side"]) for e in part] == [
        (e["day"], e["entry_min"], e["side"]) for e in full if e["day"] in set(kept)
    ]
    signal = [{"day": day_drop, "symbol": "SPY"}, {"day": day_keep, "symbol": "SPY"}]
    assert [e["day"] for e in sc._filter_days(signal, set(kept))] == [day_keep]


def test_regime_buckets_keep_days_the_filter_would_drop():
    d1, d2, d3, d4 = [date(2026, 10, d) for d in (1, 2, 5, 6)]
    # Priors: 10 and 15 are <16, 18 is 16-20, 25 is >=20.
    # A vix_min of 16 would drop d1. The regime table still scores it.
    prior = {d1: 10.0, d2: 15.0, d3: 18.0, d4: 25.0}
    trades = [
        {"day": d1, "net_pct": 10.0, "dollar": 1.0, "hit": True, "raw_entry": 0.6},
        {"day": d2, "net_pct": -4.0, "dollar": -1.0, "hit": False, "raw_entry": 0.6},
        {"day": d3, "net_pct": 1.0, "dollar": 1.0, "hit": True, "raw_entry": 0.6},
        {"day": d4, "net_pct": -2.0, "dollar": -1.0, "hit": False, "raw_entry": 0.6},
    ]
    books = {("orb_1m", "atm", 0.15, 0.20, 10): trades}
    rows = sc.regime_rows(
        books,
        [("in_sample", [d1, d2, d3]), ("holdout", [d4])],
        prior,
        ["orb_1m"],
        ["atm"],
    )
    low = [r for r in rows if r["bucket"] == "<16" and r["split"] == "in_sample" and r["sl"] == 0.20 and r["time_stop"] == 10]
    assert len(low) == 1 and low[0]["n"] == 2
    assert low[0]["mean_net_pct"] == pytest.approx(3.0)
    assert math.isfinite(low[0]["t"])
    mid = [r for r in rows if r["bucket"] == "16-20" and r["split"] == "in_sample" and r["sl"] == 0.20 and r["time_stop"] == 10]
    assert mid[0]["n"] == 1
    high = [r for r in rows if r["bucket"] == ">=20" and r["split"] == "holdout" and r["sl"] == 0.20 and r["time_stop"] == 10]
    assert high[0]["n"] == 1 and high[0]["mean_net_pct"] == pytest.approx(-2.0)
    empty = [r for r in rows if r["bucket"] == ">=20" and r["split"] == "in_sample" and r["sl"] == 0.20 and r["time_stop"] == 10]
    assert empty[0]["n"] == 0
    intro = sc.regime_intro(4, [d1, d2, d3], [d4], 0, 2, 2, 1, 1, 1120, True)
    assert "post-hoc" in intro and "not selected" in intro
    assert "Search family N = 1120" in intro
    assert "does not use the VIX day filter" in intro
    assert "In-sample: 3 days" in intro and "Held-out: 1 day (" in intro


def test_random_entries_are_uniform_on_the_allowed_window_and_share_fills():
    window = (210, 300)  # 13:00 inclusive, 14:30 exclusive
    day0 = date(2026, 1, 5)
    sess = _und(day0)[day0]
    eligible = sc.random_eligible_minutes(sess, window)
    assert eligible == list(range(210, 300))
    assert sc.random_eligible_minutes(sess, None)[0] == 5
    assert sc.random_eligible_minutes(sess, None)[-1] == 355
    # Hour pool on a full session: 9:35-9:59, five full hours, 15:00-15:25.
    pool = {h: 0 for h in sc.ENTRY_HOURS}
    for m in sc.random_eligible_minutes(sess, None):
        pool[sc.minute_hour(m)] += 1
    assert pool[9] == 25 and pool[10] == 60 and pool[14] == 60 and pool[15] == 26

    n_days = 40
    days = [day0 + timedelta(days=i) for i in range(n_days)]
    und = {"SPY": {d: sess for d in days}}
    events = {sid: [] for sid in sc.SEARCH_IDS}
    for d in days:
        for sid in sc.SEARCH_IDS:
            events[sid].extend({"day": d, "symbol": "SPY"} for _ in range(50))
    ref = sc.reference_random_events(events, und, ["SPY"], days, window)
    assert len(ref) == 50 * n_days
    counts = np.zeros(len(eligible), dtype=float)
    index = {m: i for i, m in enumerate(eligible)}
    for ev in ref:
        assert ev["entry_min"] in index
        counts[index[ev["entry_min"]]] += 1
    assert len({ev["entry_min"] for ev in ref if ev["day"] == days[0]}) == 50
    again = sc.reference_random_events(events, und, ["SPY"], days, window)
    assert [(e["day"], e["entry_min"], e["side"]) for e in again] == [
        (e["day"], e["entry_min"], e["side"]) for e in ref
    ]
    drawn, eligible_n = sc.hour_draw_table(ref, und, ["SPY"], days, window)
    drawn_v = np.array([drawn[h] for h in sc.ENTRY_HOURS], dtype=float)
    pool_v = np.array([eligible_n[h] for h in sc.ENTRY_HOURS], dtype=float)
    expected = pool_v / pool_v.sum() * drawn_v.sum()
    chi = float(((drawn_v - expected) ** 2 / np.maximum(expected, 1e-9)).sum())
    assert chi < 40
    # 13:00-13:59 is 60 minutes, 14:00-14:29 is 30. The draw share follows that.
    assert drawn[13] / sum(drawn.values()) == pytest.approx(60 / 90, abs=0.04)
    assert drawn[9] == 0 and drawn[15] == 0

    # A paired control for an afternoon signal stays inside the clock and the bucket.
    attempt = {
        "day": day0, "symbol": "SPY", "entry_min": 220, "side": 1,
        "signal": "orb_1m", "strike": "atm", "attempt_id": "a1",
    }
    paired = sc.paired_entry(attempt, und, window)
    assert window[0] <= paired["entry_min"] < window[1]
    assert paired["entry_min"] // 30 == 220 // 30
    assert paired["entry_min"] != 220

    import backtest as bt
    contract = bt.lab_occ("SPY", day0, "C", 500)
    opt = _opt(1.0)
    opt["high"][40] = 1.0
    opt["low"][40] = 1.0
    opt["high"][41] = 1.40
    book = {(day0, contract): opt}
    ev = [{"day": day0, "symbol": "SPY", "side": 1, "entry_min": 40}]
    und_one = {"SPY": {day0: sess}}
    sig, _, _ = sc.run_book(ev, book, und_one, "atm", (0.15, 0.20, 10), COSTS, "orb_1m")
    rnd, _, _ = sc.run_book(ev, book, und_one, "atm", (0.15, 0.20, 10), COSTS, "random")
    assert len(sig) == 1 and len(rnd) == 1
    for key in ("reason", "net_pct", "entry", "exit", "entry_min", "exit_min", "raw_entry", "spread_cost_pct"):
        assert sig[0][key] == pytest.approx(rnd[0][key]) if isinstance(sig[0][key], float) else sig[0][key] == rnd[0][key]
    assert sig[0]["reason"] == "tp"

    stopped = _opt(1.0)
    stopped["low"][50] = 0.70
    stopped["high"][50] = 1.0
    book2 = {(day0, contract): stopped}
    ev2 = [{"day": day0, "symbol": "SPY", "side": 1, "entry_min": 50}]
    sig2, _, _ = sc.run_book(ev2, book2, und_one, "atm", (0.15, 0.20, 30), COSTS, "mom5_1m")
    rnd2, _, _ = sc.run_book(ev2, book2, und_one, "atm", (0.15, 0.20, 30), COSTS, "random")
    assert sig2[0]["reason"] == "stop" and rnd2[0]["reason"] == "stop"
    assert sig2[0]["net_pct"] == pytest.approx(rnd2[0]["net_pct"])
    assert sig2[0]["exit"] == pytest.approx(rnd2[0]["exit"])


def test_random_audit_reports_premium_spread_and_exit_shares():
    trades = []
    for i, reason in enumerate(["stop", "tp", "time", "time", "flat"] * 2):
        trades.append({
            "raw_entry": 0.50,
            "spread_cost_pct": 4.0,
            "reason": reason,
            "net_pct": -6.0,
            "entry_min": 30,
            "time": "10:00",
            "dollar": -1.0,
            "hit": reason == "tp",
        })
    stats = sc.audit_fill_stats(trades, COSTS)
    assert stats["p10"] == pytest.approx(0.50)
    assert stats["p50"] == pytest.approx(0.50)
    assert stats["p90"] == pytest.approx(0.50)
    assert stats["spread_pct"] == pytest.approx(4.0)
    assert stats["stop_share"] == pytest.approx(0.2)
    assert stats["tp_share"] == pytest.approx(0.2)
    assert stats["time_share"] == pytest.approx(0.4)
    assert stats["flat_share"] == pytest.approx(0.2)
    # $0.50 open, 1 cent half-spread each side, $0.65 commission each side.
    # debit 0.51, credit 0.49, dollar -3.30, net % -3.30/51*100.
    assert sc.flat_round_trip_pct(0.50, COSTS) == pytest.approx(-3.30 / 51.0 * 100.0)
    assert stats["flat_pct"] == pytest.approx(sc.flat_round_trip_pct(0.50, COSTS))
    drawn, pool = sc.hour_draw_table(
        [{"day": date(2026, 10, 1), "entry_min": 5}, {"day": date(2026, 10, 1), "entry_min": 355}],
        {"SPY": _und(date(2026, 10, 1))},
        ["SPY"],
        [date(2026, 10, 1)],
        None,
    )
    assert drawn[9] == 1 and drawn[15] == 1 and drawn[12] == 0
    assert pool[9] == 25 and pool[15] == 26


def test_report_states_vix_days_and_marks_the_regime_table_descriptive():
    meta = {
        "stamp": "2026-10-24 16:00 ET",
        "synthetic": False,
        "coverage": "Symbols SPY. Strikes: atm.",
        "cent_floor": 0.01,
        "pct": 0.005,
        "commission": 0.65,
        "n_is": 9,
        "n_oos": 3,
        "is_first": "2026-08-01",
        "is_last": "2026-10-01",
        "oos_first": "2026-10-02",
        "oos_last": "2026-10-06",
        "n_family": 2240,
        "t_crit": sc.norm_ppf(1 - (0.05 / 2240) / 2),
        "skip_note": "premium skips included.",
        "family_note": sc.family_note(("atm", "2itm")),
        "premium_line": sc.describe_premium(None),
        "window_line": sc.describe_window(None, None),
        "hour_table": [],
        "vix_line": sc.describe_vix_filter(16, None, [date(2026, 10, 1)] * 12, [], "FRED VIXCLS", 9, 3),
        "vix_regime": {
            "intro": sc.regime_intro(
                16, [date(2026, 10, 1)] * 12, [date(2026, 10, 2)] * 4, 0, 12, 4, 9, 3, 2240, True,
            ),
            "rows": [{
                "signal": "orb_1m", "strike": "atm", "sl": 0.20, "time_stop": 10,
                "split": "in_sample", "bucket": ">=20", "n": 4,
                "hit_rate": 0.5, "mean_net_pct": 1.5, "t": 0.4,
            }, {
                "signal": "random", "strike": "atm", "sl": 0.20, "time_stop": 30,
                "split": "holdout", "bucket": "<16", "n": 2,
                "hit_rate": 0.0, "mean_net_pct": -9.0, "t": -1.2,
            }],
        },
        "random_audit": {
            "note": (
                "Draws are now uniform on the intersection of 9:35-15:25 and that clock. "
                "Fills and exits go through run_book and simulate_trade, the same functions a signal trade uses."
            ),
            "drawn": {h: (1 if h == 13 else 0) for h in sc.ENTRY_HOURS},
            "pool": {h: (60 if h == 13 else 0) for h in sc.ENTRY_HOURS},
            "rows": [{
                "strike": "atm", "sl": 0.20, "time_stop": 10, "n": 8,
                "mean_net_pct": -9.0, "hit_rate": 0.1, "signal_net": -1.0,
                "p10": 0.40, "p50": 0.55, "p90": 0.90, "signal_prem": 1.20,
                "spread_pct": 4.0, "flat_pct": -8.5,
                "stop_share": 0.5, "tp_share": 0.1, "time_share": 0.3, "flat_share": 0.1,
                "fill_hours": {h: {"n": 0, "net_pct": float("nan")} for h in sc.ENTRY_HOURS},
            }],
        },
    }
    text = sc.render_report(meta, [], [])
    assert "Days kept: 12" in text and "Days dropped: 0" in text
    assert "9 in-sample" in text and "3 held-out" in text
    assert "after the VIX day filter" in text
    assert "Search family N = 2240" in text
    assert "not part of N" in text
    assert "## By VIX regime" in text
    assert "post-hoc" in text and "not selected" in text
    assert "in-sample" in text and "held-out" in text
    assert "## Random baseline audit" in text
    assert "run_book and simulate_trade" in text
    assert "Flat cost %" in text
    assert "-9.00" in text

