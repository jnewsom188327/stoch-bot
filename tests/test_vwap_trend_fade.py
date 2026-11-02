"""Vix Fix + VWAP trend fade rules and the manual workflow. No orders, no network."""

from datetime import datetime

import numpy as np

import fgfade as fg
import scalp_real as sc
import vwap_trend_fade as vtf


def _book(n=25):
    fear = np.full(n, 40.0)
    greed = np.full(n, 40.0)
    close = np.full(n, 100.0)
    vwap = np.full(n, 100.0)
    mom = np.zeros(n)
    minutes = np.arange(n) + 20  # 9:50 onward, inside 9:40–15:00
    day = np.zeros(n, dtype=int)
    return fear, greed, close, vwap, mom, minutes, day


def test_short_needs_greed_maxed_fear_quiet_red_vwap_and_a_close_above():
    fear, greed, close, vwap, mom, minutes, day = _book()
    greed[18], greed[19], greed[20] = 90.0, 96.0, 90.0
    fear[19], fear[20] = 20.0, 10.0
    vwap[:] = 101.0
    vwap[20] = 100.0
    close[20] = 105.0
    mom[18], mom[19], mom[20] = 0.0, 1.0, 0.4
    rows = vtf.collect_signals(fear, greed, close, vwap, mom, minutes, day, 1, 0)
    shorts = [r for r in rows if r["side"] == -1 and r["max_level"] == 95 and r["opp"] == 30]
    assert len(shorts) == 1
    assert shorts[0]["signal_minute"] == int(minutes[20])
    assert shorts[0]["entry_minute"] == int(minutes[20]) + 1
    assert shorts[0]["first_drop"] is True
    assert shorts[0]["mom_turn"] is True
    # Already falling into the maxed bar, so this is not the first drop.
    greed[18] = 98.0
    again = vtf.collect_signals(fear, greed, close, vwap, mom, minutes, day, 1, 0)
    short2 = [r for r in again if r["side"] == -1 and r["max_level"] == 95 and r["opp"] == 30][0]
    assert short2["first_drop"] is False
    # Opposite side too strong for the 30 cap, still valid for 45.
    fear[19] = 40.0
    wide = vtf.collect_signals(fear, greed, close, vwap, mom, minutes, day, 1, 0)
    assert not any(r["side"] == -1 and r["opp"] == 30 and r["max_level"] == 95 for r in wide)
    assert any(r["side"] == -1 and r["opp"] == 45 and r["max_level"] == 95 for r in wide)


def test_long_is_the_mirror_and_the_clock_is_9_40_through_15_00():
    fear, greed, close, vwap, mom, minutes, day = _book()
    fear[18], fear[19], fear[20] = 80.0, 97.0, 90.0
    greed[19], greed[20] = 20.0, 10.0
    vwap[:] = 99.0
    vwap[20] = 100.0
    close[20] = 98.0
    rows = vtf.collect_signals(fear, greed, close, vwap, mom, minutes, day, 1, 0)
    longs = [r for r in rows if r["side"] == 1 and r["max_level"] == 95 and r["opp"] == 30]
    assert len(longs) == 1
    assert longs[0]["entry_minute"] == int(minutes[20]) + 1
    # Close back above VWAP, or a flat slope, kills it.
    close[20] = 101.0
    assert not any(r["side"] == 1 for r in vtf.collect_signals(fear, greed, close, vwap, mom, minutes, day, 1, 0))
    close[20] = 98.0
    vwap[:] = 99.0
    vwap[15] = 100.0  # slope zero at index 20 versus index 15
    vwap[20] = 100.0
    assert not any(r["side"] == 1 for r in vtf.collect_signals(fear, greed, close, vwap, mom, minutes, day, 1, 0))
    vwap[:] = 99.0
    vwap[20] = 100.0
    assert vtf.in_signal_window(10) and vtf.in_signal_window(330)
    assert not vtf.in_signal_window(9) and not vtf.in_signal_window(331)
    early = minutes.copy()
    early[20] = 5  # 9:35
    assert vtf.collect_signals(fear, greed, close, vwap, mom, early, day, 1, 0) == []
    # 2-minute chart: entry is two minutes after the signal bar starts.
    two = [r for r in vtf.collect_signals(fear, greed, close, vwap, mom, minutes, day, 2, 0) if r["side"] == 1]
    assert two[0]["entry_minute"] == int(minutes[20]) + 2


def test_contract_is_the_ask_closest_to_65_inside_45_to_100():
    spot = 100.0
    # 0.40 is under the window. 0.50 is closer to 0.65 than 0.80.
    assert vtf.pick_ask([(100, 0.40), (101, 0.50), (102, 0.80)], spot) == (101, 0.50)
    assert vtf.pick_ask([(110, 0.60), (101, 0.70)], spot)[0] == 101
    assert vtf.pick_ask([(100, 0.20), (101, 1.20)], spot) is None
    assert vtf.entry_ask(0.64) == 0.65
    calls = vtf.candidate_strikes(100, 1)
    puts = vtf.candidate_strikes(100, -1)
    assert 100 in calls and 125 in calls and 70 not in calls
    assert 100 in puts and 75 in puts and 130 not in puts

    day = datetime(2026, 1, 15).date()
    minute = 20
    sess = {k: np.full(sc.N_MIN, np.nan) for k in ("open", "high", "low", "close")}
    sess["real"] = np.zeros(sc.N_MIN, dtype=bool)
    sess["real"][minute] = True
    sess["open"][minute] = 100.0
    opt = {}
    cheap = sc._bt().lab_occ("SPY", day, "C", 101)
    target = sc._bt().lab_occ("SPY", day, "C", 103)
    for contract, raw in ((cheap, 0.20), (target, 0.64)):
        rec = sc._empty_opt()
        rec["real"][minute] = True
        rec["open"][minute] = raw
        rec["high"][minute] = raw
        rec["low"][minute] = raw
        rec["close"][minute] = raw
        opt[(day, contract)] = rec
    chosen = vtf.choose_fill(sess, opt, day, "SPY", minute, 1)
    assert chosen["status"] == "fill"
    assert chosen["strike"] == 103
    assert chosen["ask"] == 0.65
    # A chain of prints all outside the window does not slip forward.
    opt[(day, target)]["open"][minute] = 0.20
    skipped = vtf.choose_fill(sess, opt, day, "SPY", minute, 1)
    assert skipped["status"] == "premium"


def test_skipped_premium_is_counted_on_the_row():
    sig = {
        "day_i": 0, "sym_i": 0, "tf": 1, "side": -1, "max_level": 95, "opp": 30,
        "signal_minute": 20, "entry_minute": 21, "mom_turn": False, "first_drop": True,
        "chosen": {"status": "premium"},
        "rnd_chosen": {"status": "no_print"},
        "rnd_minute": 40,
    }
    rows = vtf.summary_rows([sig], 8, np.arange(0, 6), np.arange(6, 8), 20)
    base = [r for r in rows if r["variant"] == "tf1_max95_opp30_short" and r["confluence"] == "base" and r["exit"] == "hold20"][0]
    assert base["n"] == 0
    assert base["skipped_premium"] == 1
    first = [r for r in rows if r["confluence"] == "first_drop" and r["exit"] == "hold20" and r["variant"] == "tf1_max95_opp30_short"][0]
    assert first["skipped_premium"] == 1
    mom = [r for r in rows if r["confluence"] == "mom_turn" and r["exit"] == "hold20" and r["variant"] == "tf1_max95_opp30_short"][0]
    assert mom["skipped_premium"] == 0


def test_main_builds_the_download_window_before_loading_bars(tmp_path, monkeypatch):
    monkeypatch.setenv("VTF_SYNTH", "1")
    monkeypatch.setenv("VTF_DAYS", "8")
    monkeypatch.setenv("VTF_OUT", str(tmp_path))
    monkeypatch.setenv("VTF_SYMBOLS", "SPY")

    def loader(symbols, start, end, synthetic):
        assert start < end
        raise RuntimeError("loader-reached")

    monkeypatch.setattr(vtf.sc, "_load_underlying", loader)
    assert vtf.main() == 1
    report = (tmp_path / "VWAP_TREND_FADE.md").read_text()
    assert "loader-reached" in report
    assert "STAGE load failed" in report


def test_workflow_is_manual_and_places_no_orders():
    text = open(".github/workflows/vwap_trend_fade.yml").read()
    src = open("vwap_trend_fade.py").read()
    assert text.startswith("name: Vix Fix + VWAP trend fade check (real option prices)\n")
    assert "workflow_dispatch:" in text
    assert "schedule:" not in text
    assert 'default: "120"' in text
    assert 'default: "vwap-trend-fade-results"' in text
    assert "if: always()" in text
    assert "Refusing to push results" in text
    assert "main|master" in text
    assert "results/VWAP_TREND_FADE.md" in text
    assert "python vwap_trend_fade.py" in text
    readme = open("README.md").read()
    assert "Vix Fix + VWAP trend fade check (real option prices)" in readme
    assert "vwap-trend-fade-results" in readme
    assert "Run workflow" in readme
    assert "Do not tap Re-run" in readme
    for banned in ("submit_order", "TradingClient", "MarketOrderRequest", "paper=True"):
        assert banned not in text
        assert banned not in src
