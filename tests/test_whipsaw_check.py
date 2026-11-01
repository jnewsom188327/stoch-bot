"""Whipsaw rule, exits, and the manual workflow. No orders, no network."""

from datetime import datetime

import numpy as np
import pandas as pd
import pytest

import fgfade as fg
import scalp_real as sc
import whipsaw_check as wc

NY = fg.NY


def test_first_break_skips_a_rebreak_inside_22_bars_and_keeps_a_later_one():
    day = np.zeros(40, dtype=int)
    level = np.full(40, 50.0)
    level[4] = 96
    level[5] = 80  # break
    level[8] = 97
    level[9] = 70  # re-break four bars later
    level[33] = 98
    level[34] = 60  # 25 bars after the previous break
    assert wc.first_break(level, 5, day, 95)
    assert not wc.first_break(level, 9, day, 95)
    assert wc.first_break(level, 34, day, 95)
    # Still below the max is not another break.
    level[6] = 75
    assert not wc.is_break(level, 6, day, 95)
    # A max on the previous session does not break today.
    day[10] = 1
    level[9] = 100
    level[10] = 40
    assert not wc.is_break(level, 10, day, 95)


def test_other_side_thresholds_and_entry_is_the_next_bar():
    n = 12
    fear = np.full(n, 20.0)
    greed = np.full(n, 70.0)
    fear[4] = 96
    fear[5] = 40
    high = np.full(n, 101.0)
    low = np.full(n, 100.0)
    close = np.full(n, 100.5)
    minutes = np.arange(n) + 10  # 9:40 onward, entry of bar 5 is minute 16
    day_i = np.zeros(n, dtype=int)
    atr = np.full(n, 1.0)
    mom = np.linspace(1, 2, n)
    vwap = np.full(n, 100.0)
    day = datetime(2026, 1, 15).date()
    sess = {k: np.full(sc.N_MIN, np.nan) for k in ("open", "high", "low", "close")}
    sess["real"] = np.zeros(sc.N_MIN, dtype=bool)
    sess["real"][:] = True
    sess["open"][:] = 100.0
    sess["close"][:] = 100.0
    rows = wc.collect_signals(
        fear, greed, high, low, close, minutes, day_i, atr, mom, vwap,
        0, {day: sess}, [day],
    )
    longs = [r for r in rows if r["side"] == 1 and r["max_level"] == 95]
    assert len(longs) == 1
    assert longs[0]["signal_minute"] == 15
    assert longs[0]["entry_minute"] == 16
    assert wc.other_ok(longs[0]["other_value"], "ge60")
    assert wc.other_ok(longs[0]["other_value"], "ge30")
    assert not wc.other_ok(longs[0]["other_value"], "asleep")
    greed2 = greed.copy()
    greed2[5] = 5
    asleep = wc.collect_signals(
        fear, greed2, high, low, close, minutes, day_i, atr, mom, vwap,
        0, {day: sess}, [day],
    )
    long_asleep = [r for r in asleep if r["side"] == 1 and r["max_level"] == 95]
    assert len(long_asleep) == 1
    assert wc.other_ok(long_asleep[0]["other_value"], "asleep")
    assert not wc.other_ok(long_asleep[0]["other_value"], "ge60")


def test_short_is_the_mirror_and_filters_are_not_stacked():
    n = 8
    greed = np.full(n, 20.0)
    fear = np.full(n, 70.0)
    greed[3] = 99
    greed[4] = 50
    high = np.full(n, 110.0)
    low = np.full(n, 100.0)  # range 10, ATR 1 -> fails the 3 ATR filter
    close = np.full(n, 99.0)  # under VWAP, so a short passes vwap_with and a long would not
    minutes = np.arange(n) + 20
    day_i = np.zeros(n, dtype=int)
    atr = np.ones(n)
    mom = np.array([0, 1, 2, 3, 2.5, 2, 1, 0], dtype=float)  # falling at the break, against a short? short is against when mom rises
    # mom[4]=2.5 < mom[3]=3, so short momentum is not higher: mom_with True for short
    vwap = np.full(n, 105.0)
    day = datetime(2026, 1, 15).date()
    rows = wc.collect_signals(
        fear, greed, high, low, close, minutes, day_i, atr, mom, vwap,
        0, {}, [day],
    )
    shorts = [r for r in rows if r["side"] == -1 and r["max_level"] == 95]
    assert len(shorts) == 1
    assert shorts[0]["entry_minute"] == int(minutes[4]) + 1
    assert shorts[0]["mom_with"] is True
    assert shorts[0]["range_lt_3atr"] is False
    assert shorts[0]["vwap_with"] is True
    assert wc._passes(shorts[0], "ge60", "none", "all")
    assert not wc._passes(shorts[0], "ge60", "range_lt_3atr", "all")
    assert wc._passes(shorts[0], "ge60", "vwap_with", "all")


def _flat_opt(price, n=40, entry=5):
    opt = sc._empty_opt()
    opt["open"][:] = price
    opt["high"][:] = price
    opt["low"][:] = price
    opt["close"][:] = price
    opt["real"][: n] = True
    opt["lab"][:] = price
    return opt, entry


def test_hold20_matches_the_fade_cost_model_and_breakeven_waits_for_the_arm():
    opt, entry = _flat_opt(1.0)
    hold = sc.simulate_trade(opt, entry, (100.0, None, 20), wc.COSTS, allow_slip=False, premium=fg.PREMIUM_BAND)
    assert hold["status"] == "fill"
    assert hold["reason"] == "time"
    assert hold["exit_min"] == entry + 20
    # debit 1.01, credit 0.99, dollar -3.30. Net percent is dollar / debit.
    assert hold["net_pct"] == pytest.approx(-3.30 / 1.01, abs=1e-6)

    crashed = sc._empty_opt()
    crashed["real"][:] = True
    crashed["open"][:] = 0.40
    crashed["high"][:] = 0.40
    crashed["low"][:] = 0.40
    crashed["close"][:] = 0.40
    crashed["lab"][:] = 0.40
    crashed["open"][entry] = 1.0
    crashed["high"][entry] = 1.0
    crashed["low"][entry] = 1.0
    crashed["close"][entry] = 1.0
    be = wc.breakeven_trade(crashed, entry)
    assert be["status"] == "fill"
    assert be["reason"] == "flat"
    assert be["net_pct"] < -50

    armed = sc._empty_opt()
    armed["real"][:40] = True
    price = np.full(sc.N_MIN, 1.0)
    price[entry + 1] = 1.20
    price[entry + 2] = 1.00
    armed["open"][:] = price
    armed["high"][:] = price
    armed["low"][:] = price
    armed["close"][:] = price
    armed["lab"][:] = price
    be_hit = wc.breakeven_trade(armed, entry)
    assert be_hit["reason"] == "be"
    assert be_hit["exit_min"] == entry + 2


def test_underlying_move_is_directional_and_noon_is_12_00_through_12_59():
    sess = {k: np.full(sc.N_MIN, np.nan) for k in ("open", "high", "low", "close")}
    sess["real"] = np.ones(sc.N_MIN, dtype=bool)
    sess["open"][:] = 100.0
    sess["close"][:] = 100.0
    sess["close"][30] = 100.31
    sess["close"][40] = 99.78
    assert wc.atr_move(sess, 10, 1, 1.0, 20) == pytest.approx(0.31)
    assert wc.atr_move(sess, 10, -1, 1.0, 30) == pytest.approx(0.22)
    assert wc.NOON_LO == 150 and wc.NOON_HI == 210
    assert fg.clock_hhmm(150) == "12:00"
    assert fg.clock_hhmm(209) == "12:59"


def test_empty_signal_study_writes_the_raw_table(tmp_path):
    day = datetime(2026, 1, 15, 9, 30, tzinfo=NY)
    idx = pd.date_range(day, periods=200, freq="min")
    close = np.full(200, 100.0)
    frame = pd.DataFrame(
        {"open": close, "high": close + 0.1, "low": close - 0.1, "close": close, "volume": np.full(200, 1000.0)},
        index=idx,
    )
    # One short day will not be a "complete" session. Call the study directly.
    und = {"SPY": sc.rth_session(frame)}
    score_day = datetime(2026, 1, 15).date()
    # Pad the session so the direct study still runs on this one day.
    result = wc.run_study({"SPY": frame}, ["SPY"], [score_day], und, synthetic=True, n_boot=20)
    assert result["failures"] == []
    text = result["report"]
    assert text.startswith("# Vix Fix whipsaw check\n")
    assert "mean_net" in text.splitlines()[4] or "| variant |" in text
    assert "not a reason to trade" in text
    wc.write_outputs(str(tmp_path), result["report"], result["trades"])
    assert (tmp_path / "WHIPSAW.md").exists()
    assert (tmp_path / "whipsaw_trades.csv").read_text().startswith("day,")


def test_workflow_is_manual_and_places_no_orders():
    text = open(".github/workflows/whipsaw.yml").read()
    src = open("whipsaw_check.py").read()
    assert text.startswith("name: Vix Fix whipsaw check (real option prices)\n")
    assert "workflow_dispatch:" in text
    assert "schedule:" not in text
    assert 'default: "120"' in text
    assert 'default: "whipsaw-results"' in text
    assert "ALPACA_KEY: ${{ secrets.ALPACA_KEY }}" in text
    assert "ALPACA_SECRET: ${{ secrets.ALPACA_SECRET }}" in text
    assert "python -m pytest -q tests/test_whipsaw_check.py" in text
    assert "results/WHIPSAW.md" in text
    assert "results/whipsaw_trades.csv" in text
    assert "if: always()" in text
    assert "Refusing to push results" in text
    assert "main|master" in text
    readme = open("README.md").read()
    assert "Vix Fix whipsaw check (real option prices)" in readme
    assert "whipsaw-results" in readme
    assert "Run workflow" in readme
    assert "Do not tap Re-run" in readme
    for banned in ("submit_order", "TradingClient", "MarketOrderRequest", "paper=True"):
        assert banned not in text
        assert banned not in src
