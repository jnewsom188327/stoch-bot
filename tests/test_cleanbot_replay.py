"""Clean Scan replay: mocked option bars, no network, no orders."""

import numpy as np
import pandas as pd
import pytest

import cleanbot_replay as cr
import scalp_real as sc


COSTS = (0.01, 0.005, 0.65)


def _pos(version="A", qty=2, entry=1.0, minute=10 * 60, legs=None, logged=0.0):
    return {
        "date": "2026-10-22",
        "version": version,
        "ticker": "SPY",
        "side": "PUT",
        "contract": "SPY261022P00767000",
        "entry_hhmm": cr.minute_to_hhmm(minute),
        "entry_minute": minute,
        "entry_fill": entry,
        "qty": qty,
        "logged_usd": logged,
        "best_pct": 0.0,
        "worst_pct": 0.0,
        "qty_gap": False,
        "legs": legs or [],
        "scan_side": -1,
    }


def _bar(minute, o, h, l, c):
    return {"minute": minute, "o": o, "h": h, "l": l, "c": c}


def _flat(start, n, price):
    return [_bar(start + i, price, price, price, price) for i in range(n)]


def test_logged_qty_matches_the_pnl_formula_and_the_green_then_red_count():
    rows = cr.load_rows("clean_trades.csv")
    assert len(rows) == 34
    assert not any(row["qty_gap"] for row in rows)
    sales, green, gave_back = cr.green_then_red(rows)
    assert sales == 34 and green == 30 and gave_back == 18
    positions = cr.group_positions(rows)
    assert len(positions) == 26
    assert positions[0]["ticker"] == "TSLA" and positions[0]["version"] == "A"
    assert positions[0]["qty"] == 2
    paired = [pos for pos in positions if len(pos["legs"]) == 2]
    assert paired
    # 34 is the sale count. Scaled exits are 1 contract, full exits are 2.
    assert sum(pos["qty"] for pos in positions) == sum(row["sold_qty"] for row in rows) == 52


def test_half_spread_matches_scalp_real():
    assert cr.half_spread(1.0, COSTS) == pytest.approx(sc.half_spread(1.0, 0.01, 0.005))
    assert cr.half_spread(10.0, COSTS) == pytest.approx(0.05)
    dollar, _pct, raw = cr.round_trip(1.0, 0.75, 2, COSTS)
    # debit 1.01, credit 0.74, (0.74-1.01)*200 - 2*0.65*2
    assert raw == pytest.approx(-50.0)
    assert dollar == pytest.approx(-54.0 - 2.60)


def test_same_bar_stop_and_target_stops_first():
    pos = _pos()
    rules = cr.rules_for("A", "fixed")
    legs = cr.replay_position(pos, [_bar(600, 1.0, 1.40, 0.70, 1.10)], rules, None, COSTS)
    assert len(legs) == 1
    assert legs[0]["reason"] == "STOP -25%"
    assert legs[0]["qty"] == 2
    assert legs[0]["raw"] == pytest.approx(0.75)


def test_a_gap_through_the_stop_fills_at_the_open():
    pos = _pos()
    rules = cr.rules_for("A", "fixed")
    legs = cr.replay_position(pos, [_bar(600, 0.50, 0.55, 0.40, 0.45)], rules, None, COSTS)
    assert legs[0]["raw"] == pytest.approx(0.50)
    assert legs[0]["reason"] == "STOP -25%"


def test_target_fills_at_the_target_not_the_wick():
    pos = _pos()
    rules = cr.rules_for("A", "fixed")
    legs = cr.replay_position(pos, [_bar(600, 1.40, 1.40, 1.30, 1.35)], rules, None, COSTS)
    assert legs[0]["reason"] == "TP1 +25%"
    assert legs[0]["qty"] == 2
    assert legs[0]["raw"] == pytest.approx(1.25)


def test_current_a_scales_one_and_the_fixed_rule_sells_both():
    pos = _pos()
    bars = [_bar(600, 1.0, 1.30, 0.95, 1.20), _bar(15 * 60 + 45, 1.50, 1.50, 1.50, 1.50)]
    current = cr.replay_position(pos, bars, cr.rules_for("A", "current"), None, COSTS)
    fixed = cr.replay_position(pos, bars, cr.rules_for("A", "fixed"), None, COSTS)
    assert [(leg["reason"], leg["qty"]) for leg in current] == [("TP1 +25%", 1), ("3:45 time exit", 1)]
    assert [(leg["reason"], leg["qty"]) for leg in fixed] == [("TP1 +25%", 2)]


def test_b_jump_through_both_targets_is_one_tp2_sale():
    pos = _pos(version="B")
    rules = cr.rules_for("B", "fixed")
    legs = cr.replay_position(pos, [_bar(600, 1.0, 1.25, 0.95, 1.22)], rules, None, COSTS)
    assert [(leg["reason"], leg["qty"], round(leg["raw"], 2)) for leg in legs] == [("TP2 +20%", 2, 1.20)]


def test_b_scales_at_10_then_20():
    pos = _pos(version="B")
    bars = [_bar(600, 1.0, 1.12, 0.98, 1.11), _bar(603, 1.11, 1.25, 1.08, 1.22)]
    legs = cr.replay_position(pos, bars, cr.rules_for("B", "fixed"), None, COSTS)
    assert [(leg["reason"], leg["qty"], leg["minute"]) for leg in legs] == [
        ("TP1 +10%", 1, 600),
        ("TP2 +20%", 1, 603),
    ]


def test_scan_exit_closes_the_runner_and_no_scan_waits_for_1545():
    pos = _pos()
    bars = [_bar(600, 1.0, 1.05, 0.99, 1.02), _bar(610, 1.40, 1.42, 1.38, 1.41), _bar(15 * 60 + 45, 1.10, 1.10, 1.10, 1.10)]
    scan = (610, "SCAN EXIT: leg got choppy")
    current = cr.replay_position(pos, bars, cr.rules_for("A", "current"), scan, COSTS)
    quiet = cr.replay_position(pos, bars, cr.rules_for("A", "no_scan"), scan, COSTS)
    assert current[-1]["reason"] == "SCAN EXIT: leg got choppy"
    assert current[-1]["minute"] == 610
    assert current[-1]["raw"] == pytest.approx(1.40)
    assert quiet[-1]["reason"] == "3:45 time exit"
    assert quiet[-1]["minute"] == 15 * 60 + 45


def test_breakeven_lock_exits_at_entry_and_costs_make_it_a_loss():
    pos = _pos()
    bars = [_bar(600, 1.05, 1.12, 1.05, 1.10), _bar(601, 1.08, 1.08, 0.99, 1.00)]
    legs = cr.replay_position(pos, bars, cr.rules_for("A", "breakeven"), None, COSTS)
    assert len(legs) == 1
    assert legs[0]["reason"] == "BE entry"
    assert legs[0]["minute"] == 601
    assert legs[0]["raw"] == pytest.approx(1.0)
    assert legs[0]["qty"] == 2
    assert legs[0]["net_usd"] < 0
    assert legs[0]["raw_usd"] == pytest.approx(0.0)


def test_trail_gives_back_half_the_peak_after_10_percent():
    pos = _pos()
    bars = [_bar(600, 1.16, 1.20, 1.15, 1.18), _bar(601, 1.16, 1.16, 1.08, 1.10)]
    legs = cr.replay_position(pos, bars, cr.rules_for("A", "trail50"), None, COSTS)
    assert legs[0]["reason"] == "TRAIL 50% giveback"
    assert legs[0]["raw"] == pytest.approx(1.10)
    assert legs[0]["minute"] == 601


def test_trail_30_waits_for_a_15_percent_peak():
    pos = _pos()
    bars = [_bar(600, 1.18, 1.20, 1.18, 1.19), _bar(602, 1.16, 1.16, 1.13, 1.14)]
    legs = cr.replay_position(pos, bars, cr.rules_for("A", "trail30"), None, COSTS)
    assert legs[0]["reason"] == "TRAIL 30% giveback"
    assert legs[0]["minute"] == 602
    assert legs[0]["raw"] == pytest.approx(1.14)


def test_partial_sells_half_then_trails_the_rest():
    pos = _pos()
    bars = [_bar(600, 1.08, 1.12, 1.08, 1.11), _bar(604, 1.07, 1.07, 1.04, 1.05)]
    legs = cr.replay_position(pos, bars, cr.rules_for("A", "partial10"), None, COSTS)
    assert [(leg["reason"], leg["qty"], leg["minute"], round(leg["raw"], 2)) for leg in legs] == [
        ("PARTIAL +10%", 1, 600, 1.10),
        ("TRAIL 50% giveback", 1, 604, 1.06),
    ]


def test_time_exit_uses_the_open_n_minutes_later():
    pos = _pos(minute=600)
    bars = [_bar(600 + i, 1.0 + i * 0.01, 1.5, 0.9, 1.4) for i in range(12)]
    legs = cr.replay_position(pos, bars, cr.rules_for("A", "time5"), None, COSTS)
    assert len(legs) == 1
    assert legs[0]["minute"] == 605
    assert legs[0]["raw"] == pytest.approx(1.05)
    assert legs[0]["reason"] == "TIME +5m"
    assert legs[0]["raw"] < 1.5


def test_validation_flags_a_rule_that_does_not_match_the_log():
    logged = [{
        "reason": "STOP -25%", "exit_minute": 601, "exit_hhmm": "10:01",
        "sold_qty": 2, "pnl_usd": -50.0,
    }]
    pos = _pos(legs=logged, logged=-50.0)
    bars = [_bar(600, 1.0, 1.40, 0.95, 1.30)]
    legs = cr.replay_position(pos, bars, cr.rules_for("A", "current"), None, COSTS)
    assert cr.reason_class(legs[0]["reason"]) == "tp1"
    assert cr.validation_flag(pos, legs) == "mismatch"
    assert cr.validation_flag(pos, []) == "no bars"


def test_drawdown_and_bootstrap():
    assert cr.max_drawdown([10.0, -30.0, 5.0]) == pytest.approx(-30.0)
    assert cr.max_drawdown([]) == 0.0
    total, lo, hi = cr.bootstrap_total([5.0, 5.0, 5.0], n=50, seed=1)
    assert total == pytest.approx(15.0)
    assert lo == pytest.approx(15.0) and hi == pytest.approx(15.0)
    again = cr.bootstrap_total([10.0, -4.0, 1.0])
    same = cr.bootstrap_total([10.0, -4.0, 1.0])
    assert again == same
    assert again[1] <= again[2]


def test_report_states_the_sample_is_too_small_and_shows_each_variant():
    rows = cr.load_rows("clean_trades.csv")
    positions = cr.group_positions(rows)[:2]
    def bars_for(pos):
        return [_bar(pos["entry_minute"], pos["entry_fill"], pos["entry_fill"] * 1.3, pos["entry_fill"] * 0.7, pos["entry_fill"])]
    def scan_for(_pos):
        return None
    results = cr.run_variants(positions, bars_for, scan_for, COSTS)
    text = cr.render_report(rows, positions, results, COSTS, {"validation_note": "Scan clock from the test."})
    assert "far too small to conclude anything" in text
    assert "n=34 sales over 3 days is far too small to conclude anything." in text
    assert "95% bootstrap" in text
    assert "mismatch" in text or "price gap" in text or "cost drag" in text or "no bars" in text
    for name in cr.VARIANTS:
        assert f"### {name}" in text
        assert name in text
    assert "version A" in text and "version B" in text
    assert "2026-10-21" in text


def test_every_logged_entry_replays_on_mocked_bars():
    rows = cr.load_rows("clean_trades.csv")
    positions = cr.group_positions(rows)

    def bars_for(pos):
        entry = pos["entry_fill"]
        minute = pos["entry_minute"]
        return [
            _bar(minute, entry, entry * 1.30, entry * 0.70, entry),
            _bar(min(minute + 10, cr.SESSION_END), entry * 1.05, entry * 1.08, entry * 0.80, entry),
            _bar(cr.FLAT_MINUTE, entry, entry, entry * 0.5, entry),
        ]

    def scan_for(pos):
        return (min(pos["entry_minute"] + 20, cr.SESSION_END), "SCAN EXIT: leg got choppy")

    results = cr.run_variants(positions, bars_for, scan_for, COSTS)
    assert all(len(results[name]) == 26 for name in cr.VARIANTS)
    assert any(row["flag"] == "mismatch" for row in results["current"])
    text = cr.render_report(rows, positions, results, COSTS, {"validation_note": "mocked scan clock"})
    assert "2026-10-22" in text
    assert "version A" in text and "version B" in text


def test_option_frame_is_read_in_new_york_time():
    stamp = pd.Timestamp("2026-10-22 14:00", tz="UTC")  # 10:00 ET
    idx = pd.MultiIndex.from_arrays([["SPY261022P00767000"], [stamp]])
    df = pd.DataFrame({"open": [1.5], "high": [1.6], "low": [1.4], "close": [1.55]}, index=idx)
    bars = cr.bars_from_option_frame(df, "SPY261022P00767000")
    assert bars[0]["minute"] == 10 * 60
    assert bars[0]["c"] == pytest.approx(1.55)
    assert cr.bars_from_option_frame(df, "OTHER") == []


def test_scan_exit_uses_the_five_minute_close(monkeypatch):
    idx = pd.date_range("2026-10-22 12:40", periods=3, freq="5min", tz="America/New_York")
    frame = pd.DataFrame({"open": 1, "high": 1, "low": 1, "close": 1, "volume": 1}, index=idx)

    def fake_scan(_df):
        return np.array([1, 1, 0]), np.array([0, 0, 4]), {}

    monkeypatch.setattr(cr.cb, "scan", fake_scan)
    found = cr.find_scan_exit(frame, cr.hhmm_to_minute("12:45"), 1, "2026-10-22")
    assert found[0] == 12 * 60 + 55
    assert found[1] == "SCAN EXIT: leg got choppy"
    assert cr.find_scan_exit(frame, cr.hhmm_to_minute("12:45"), 1, "2026-10-23") is None


def test_workflow_is_manual_data_only_and_cannot_push_main():
    text = open(".github/workflows/cleanbot_replay.yml").read()
    live = open(".github/workflows/cleanbot.yml").read()
    assert text.startswith("name: Clean Scan replay (real option prices)\n")
    assert "workflow_dispatch:" in text
    assert "schedule:" not in text
    assert "schedule:" in live
    assert "ALPACA_KEY: ${{ secrets.ALPACA_KEY }}" in text
    assert "ALPACA_SECRET: ${{ secrets.ALPACA_SECRET }}" in text
    assert 'git push origin "HEAD:${BRANCH}"' in text
    assert "Refusing to push results" in text
    assert "main|master" in text
    assert '[[ "$BRANCH" =~ ^[A-Za-z0-9._/-]+$ ]]' in text
    assert 'HEADBR="$(git rev-parse --abbrev-ref HEAD)"' in text
    assert "mkdir -p /tmp/cleanbot-replay-out" in text
    assert "rm -f results/CLEANBOT_REPLAY.md" in text
    assert 'git checkout -B "$BRANCH"' in text
    assert 'default: "cleanbot-replay-results"' in text
    assert "python -m pytest -q tests/test_cleanbot_replay.py" in text
    assert "results/CLEANBOT_REPLAY.md" in text
    assert "results/cleanbot_replay_trades.csv" in text
    for banned in ("submit_order", "TradingClient", "MarketOrderRequest"):
        assert banned not in text
    assert "python cleanbot_replay.py" in text
