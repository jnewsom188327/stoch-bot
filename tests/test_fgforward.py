"""Forward-test guard, signal parity, and the quote exit simulator. No network, no orders."""

from datetime import datetime, timezone
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd
import pytest

import fgfade as fg
import fgforward as ff
import fgperfect as fp
import scalp_real as sc

NY = ZoneInfo("America/New_York")


def _at(year, month, day, hour, minute, tz=NY):
    return datetime(year, month, day, hour, minute, tzinfo=tz)


def test_window_follows_new_york_not_the_utc_clock():
    assert ff.inside_forward_window(_at(2026, 7, 15, 11, 54)) is False
    assert ff.inside_forward_window(_at(2026, 7, 15, 11, 55)) is True
    assert ff.inside_forward_window(_at(2026, 7, 15, 15, 49)) is True
    assert ff.inside_forward_window(_at(2026, 7, 15, 15, 50)) is False
    assert ff.inside_forward_window(_at(2026, 7, 18, 12, 0)) is False  # Saturday
    # 15:55 UTC is 11:55 EDT and 10:55 EST. 16:55 UTC is 11:55 EST.
    july = datetime(2026, 7, 15, 15, 55, tzinfo=timezone.utc).astimezone(NY)
    january = datetime(2026, 1, 15, 15, 55, tzinfo=timezone.utc).astimezone(NY)
    january_late = datetime(2026, 1, 15, 16, 55, tzinfo=timezone.utc).astimezone(NY)
    assert ff.inside_forward_window(july) is True
    assert ff.inside_forward_window(january) is False
    assert ff.inside_forward_window(january_late) is True
    assert ff.startup_guard(_at(2026, 7, 15, 9, 0), "/tmp/does-not-exist-fgforward") == "outside the forward window"


def test_lock_quiet_when_another_live_process_holds_it(tmp_path):
    path = tmp_path / "lock"
    path.write_text("1")  # pid 1 is alive
    now = _at(2026, 7, 15, 12, 0)
    assert ff.startup_guard(now, str(path)) == "already running"
    assert ff.startup_guard(now, str(tmp_path / "missing")) == ""
    stale = tmp_path / "stale"
    stale.write_text("999999")
    assert ff.lock_held(str(stale)) is False


def test_noon_bucket_is_12_00_through_12_59():
    assert ff.tod_bucket(150) == "1200"
    assert ff.tod_bucket(209) == "1200"
    assert ff.in_noon_window(150) and ff.in_noon_window(209)
    assert ff.tod_bucket(149) == "1100"
    assert ff.tod_bucket(210) == "1300"
    assert not ff.in_noon_window(149)
    assert any(spec.id == ff.RULE_ID for spec in fp.entry_specs(False))
    ids = {rule.id for rule in fp.exit_rules()}
    assert "be_a15_d0" in ids and "be_a10_d0" in ids


def test_random_plan_is_two_per_ticker_per_hour_and_spaced():
    day = datetime(2026, 7, 15).date()
    plan = ff.random_plan(day, ("SPY", "QQQ"))
    assert len(plan) == 7 * 2 * 2
    noon = [row for row in plan if row["hour"] == "12"]
    assert len(noon) == 4
    for row in noon:
        assert 150 <= row["minute"] < 210
        assert ff.in_noon_window(row["minute"])
    for sym in ("SPY", "QQQ"):
        for hour, _lo, _hi in ff.hour_ranges():
            mins = sorted(row["minute"] for row in plan if row["symbol"] == sym and row["hour"] == hour)
            assert len(mins) == 2
            assert mins[1] - mins[0] >= 20


def _fixture_frames():
    day = datetime(2026, 1, 15, 9, 30, tzinfo=NY)
    idx = pd.date_range(day, periods=390, freq="min")
    close = np.full(390, 100.0)
    for i in range(30, 80):
        close[i] = 100 - (i - 30) * 0.15
    high = close + 0.05
    low = close - 0.05
    for i in range(80, 88):
        high[i] = close[i] + 8.0
        low[i] = close[i] - 0.02
    for i in range(88, 100):
        close[i] = close[87] - (i - 87) * 0.3
        high[i] = close[i] + 0.05
        low[i] = close[i] - 0.05
    frame = pd.DataFrame(
        {"open": close, "high": high, "low": low, "close": close, "volume": np.full(390, 1000.0)},
        index=idx,
    )
    return {"SPY": frame}


def test_signals_match_fgperfect_on_a_fixture_day():
    frames = _fixture_frames()
    day = datetime(2026, 1, 15).date()
    got = ff.events_for_frames(frames, ["SPY"], day)
    spec = next(spec for spec in fp.entry_specs(False) if spec.id == fp.BASE_ID)
    chart = fp.enrich_chart(frames["SPY"], 1, {day: 0})
    direct = fp.build_signal_events(
        {1: {0: chart}}, spec, {"SPY": sc.rth_session(frames["SPY"])}, ["SPY"], [day], {}, {}, None,
    )
    assert len(direct) >= 1
    assert [(ev.minute, ev.side, round(ev.greed, 4), round(ev.fear, 4)) for ev in got] == [
        (ev.minute, ev.side, round(ev.greed, 4), round(ev.fear, 4)) for ev in direct
    ]
    assert got[0].side == -1
    assert fg.clock_hhmm(got[0].minute) == "10:59"


def test_breakeven_does_not_stop_before_the_arm_and_stop_beats_the_target():
    ask = 0.50
    fill = ff.entry_fill_of(ask)
    assert fill == pytest.approx(0.51)
    # Falls apart before any +10% or +15% bid. Breakeven is still a hold to the flat.
    crashed = ff.simulate_bid_path([0.50, 0.30, 0.05], ask)
    assert crashed["why_be_a15"] == "flat"
    assert crashed["why_be_a10"] == "flat"
    assert crashed["net_be_a15"] < -50
    assert crashed["why_tp15_sl15"] == "stop"
    assert crashed["why_tp15_sl25"] == "stop"
    # Arms at +15%, then the next bid back at the entry fill is the breakeven stop.
    # The fixed +15/-15 stop is checked first, so the opening gap down is a stop
    # even though a later bid would have been a target.
    path = [0.40, 0.55, 0.62, 0.51, 0.20]
    armed = ff.simulate_bid_path(path, ask)
    assert armed["why_be_a15"] == "be"
    assert armed["why_be_a10"] == "be"
    assert armed["why_tp15_sl15"] == "stop"
    assert armed["why_hold"] == "flat"
    assert armed["why_scale_15_15"] == "scale"
    assert armed["mfe_pct"] == pytest.approx((0.62 / fill - 1.0) * 100.0)
    assert armed["mae_pct"] == pytest.approx((0.20 / fill - 1.0) * 100.0)
    # Scale net is the average of the two halves under the same cost model.
    half_net, _dollar = ff._sale_net(ask, 0.62)
    # Runner stops when the bid is 15% under the 0.62 peak: 0.527. 0.51 is through that stop.
    run_net, _dollar2 = ff._sale_net(ask, 0.51)
    assert armed["net_scale_15_15"] == pytest.approx(0.5 * (half_net + run_net))


def test_scoreboard_warns_until_30_sessions_and_names_the_tail(tmp_path):
    signals = [{
        "kind": "signal", "in_window": "true", "status": "filled",
    }, {
        "kind": "signal", "in_window": "true", "status": "skipped",
    }]
    trades = [{
        "kind": "signal", "in_window": "true",
        "net_be_a15": "-80", "net_be_a10": "-70", "net_tp15_sl15": "-15",
        "net_tp15_sl25": "-25", "net_scale_15_15": "-40", "net_hold": "-80",
    }, {
        "kind": "random", "in_window": "true",
        "net_be_a15": "5", "net_be_a10": "1", "net_tp15_sl15": "0",
        "net_tp15_sl25": "0", "net_scale_15_15": "0", "net_hold": "2",
    }]
    text = ff.render_scoreboard(signals, trades, ["2026-10-01"])
    assert "need >=30 sessions" in text
    assert "Noon-hour signals: 2" in text
    assert "biggest single loss -80.0%" in text
    assert "1 of 1" in text
    assert "No orders" in text
    reached = ff.render_scoreboard(signals, trades, [str(i) for i in range(30)])
    assert "need >=30 sessions" not in reached
    assert "30-session line has been reached" in reached
    ff._append_rows(str(tmp_path / "fgforward_signals.csv"), ff.SIGNAL_FIELDS, [])
    assert (tmp_path / "fgforward_signals.csv").read_text().startswith("day,")


def test_workflow_is_weekday_log_only_and_cannot_push_main():
    text = open(".github/workflows/fgforward.yml").read()
    src = open("fgforward.py").read()
    assert text.startswith("name: Greed/fear forward test (log only)\n")
    assert 'cron: "55 15 * * 1-5"' in text
    assert 'cron: "55 16 * * 1-5"' in text
    assert "workflow_dispatch:" in text
    assert "group: fgforward" in text
    assert "cancel-in-progress: false" in text
    assert "fgforward-results" in text
    assert "Refusing to commit results on" in text
    assert "ALPACA_KEY: ${{ secrets.ALPACA_KEY }}" in text
    assert "ALPACA_SECRET: ${{ secrets.ALPACA_SECRET }}" in text
    assert "python -m pytest -q tests/test_fgforward.py" in text
    assert "timeout-minutes: 360" in text
    for banned in ("submit_order", "TradingClient", "MarketOrderRequest", "paper=True"):
        assert banned not in text
        assert banned not in src
    readme = open("README.md").read()
    assert "Greed/fear forward test (log only)" in readme
    assert "Run workflow" in readme
    assert "Do not tap Re-run" in readme
    assert "fgforward-results" in readme
