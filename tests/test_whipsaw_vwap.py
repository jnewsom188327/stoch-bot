"""VWAP buckets and the VWAP-touch exit. No orders, no network."""

import numpy as np

import fgfade as fg
import scalp_real as sc
import whipsaw_check as wc
import whipsaw_vwap as wv


def test_distance_is_signed_with_the_trade_and_the_buckets_cover_the_line():
    # Long: close below VWAP is against. Short of the same prices is with the trade.
    assert (98.0 - 100.0) / 1.0 == -2.0
    long_dist = (98.0 - 100.0) / 1.0
    short_dist = -long_dist
    assert wv.bucket_name(long_dist) == "-2 to 0"
    assert wv.bucket_name(short_dist) == "2 to 4"
    assert wv.bucket_name(-4.1) == "below -4"
    assert wv.bucket_name(-4.0) == "-4 to -2"
    assert wv.bucket_name(-2.0) == "-2 to 0"
    assert wv.bucket_name(0.0) == "0 to 2"
    assert wv.bucket_name(2.0) == "2 to 4"
    assert wv.bucket_name(4.0) == "4+"
    assert wv.far_side(-0.1) and not wv.far_side(0.0)
    assert wv.stretched_against(-2.0) and wv.stretched_against(-5.0)
    assert not wv.stretched_against(-1.9)


def test_touch_sells_the_first_cross_and_caps_at_20_bars():
    path = {
        "high": np.full(sc.N_MIN, 99.0),
        "low": np.full(sc.N_MIN, 98.0),
        "vwap": np.full(sc.N_MIN, 100.0),
    }
    start = 10
    # No bar reaches VWAP.
    minute, touched = wv.first_touch(path, start, start + 20)
    assert minute == start + 20 and touched is False
    path["high"][start + 3] = 100.5
    path["low"][start + 3] = 99.5
    minute, touched = wv.first_touch(path, start, start + 20)
    assert minute == start + 3 and touched is True
    # A later cross does not win.
    path["high"][start + 1] = 101.0
    path["low"][start + 1] = 99.0
    minute, touched = wv.first_touch(path, start, start + 20)
    assert minute == start + 1 and touched is True


def test_vwap_touch_net_matches_the_hold_when_vwap_is_never_touched():
    opt = sc._empty_opt()
    opt["real"][:40] = True
    opt["open"][:] = 1.0
    opt["high"][:] = 1.0
    opt["low"][:] = 1.0
    opt["close"][:] = 1.0
    opt["lab"][:] = 1.0
    entry = 5
    hold = sc.simulate_trade(opt, entry, (100.0, None, 20), wc.COSTS, allow_slip=False, premium=fg.PREMIUM_BAND)
    path = {
        "high": np.full(sc.N_MIN, 90.0),
        "low": np.full(sc.N_MIN, 89.0),
        "vwap": np.full(sc.N_MIN, 100.0),
    }
    touch = wv.touch_exit(opt, entry, path)
    assert touch["touched"] is False
    assert touch["minute"] == entry + 20
    assert touch["net"] == hold["net_pct"]


def test_far_side_touch_table_uses_only_against_trades(tmp_path):
    def sig(dist, net, rnd):
        return {
            "day_i": 0,
            "sym_i": 0,
            "side": 1,
            "max_level": 95,
            "other_value": 70.0,
            "entry_minute": 20,
            "vwap_dist": dist,
            "und_atr_20": 0.3,
            "fill": {"hold20": {"net": net}, "contract": "C", "raw": 1.0, "touch": {"net": net - 1, "touched": True, "minute": 22}},
            "rnd_fill": {"hold20": {"net": rnd}, "touch": {"net": rnd, "touched": False, "minute": 40}},
            "vwap_touch": {"net": net - 1},
            "rnd_vwap_touch": {"net": rnd},
            "rnd_minute": 40,
        }
    signals = [sig(-3.0, 5.0, 1.0), sig(3.0, 9.0, 1.0)]
    bucket, touch, combo = wv.build_rows(signals, 8, np.arange(0, 6), np.arange(6, 8), 50)
    fade = [r for r in bucket if r["variant"] == "max95_ge60_long" and r["slice"] == "-4 to -2"][0]
    chase = [r for r in bucket if r["variant"] == "max95_ge60_long" and r["slice"] == "2 to 4"][0]
    assert fade["n"] == 1 and fade["mean_net"] == 5.0
    assert chase["n"] == 1 and chase["mean_net"] == 9.0
    far_hold = [r for r in touch if r["exit"] == "hold20" and r["variant"] == "max95_ge60_long"][0]
    far_touch = [r for r in touch if r["exit"] == "vwap_touch" and r["variant"] == "max95_ge60_long"][0]
    assert far_hold["n"] == 1 and far_hold["mean_net"] == 5.0
    assert far_touch["n"] == 1 and far_touch["mean_net"] == 4.0
    combo_touch = [r for r in combo if r["exit"] == "vwap_touch" and r["variant"] == "max95_ge60_long"][0]
    assert combo_touch["n"] == 1 and combo_touch["slice"] == "stretched 2+"
    text = wv.render_report(bucket, touch, combo, {"n_sessions": 8, "n_signals": 2, "synthetic": True, "runtime_min": 0.1, "first_day": "d", "last_day": "d"}, [])
    assert text.startswith("# Vix Fix whipsaw VWAP check\n")
    assert "not a reason to trade" in text
    assert text.index("## Distance") < text.index("## VWAP-touch")
    wv.write_outputs(str(tmp_path), text, [])
    assert (tmp_path / "WHIPSAW_VWAP.md").exists()
    assert (tmp_path / "whipsaw_vwap_trades.csv").read_text().startswith("day,")


def test_main_builds_the_download_window_before_loading_bars(tmp_path, monkeypatch):
    """The Actions crash was NameError: pd is not defined on the start timestamp."""
    monkeypatch.setenv("WHIP_SYNTH", "1")
    monkeypatch.setenv("WHIP_DAYS", "8")
    monkeypatch.setenv("WHIP_OUT", str(tmp_path))
    monkeypatch.setenv("WHIP_SYMBOLS", "SPY")

    def loader(symbols, start, end, synthetic):
        assert start < end
        raise RuntimeError("loader-reached")

    monkeypatch.setattr(wv.sc, "_load_underlying", loader)
    assert wv.main() == 1
    report = (tmp_path / "WHIPSAW_VWAP.md").read_text()
    assert "loader-reached" in report
    assert "STAGE load failed" in report


def test_workflow_is_manual_and_places_no_orders():
    text = open(".github/workflows/whipsaw_vwap.yml").read()
    src = open("whipsaw_vwap.py").read()
    assert text.startswith("name: Vix Fix whipsaw VWAP check (real option prices)\n")
    assert "workflow_dispatch:" in text
    assert "schedule:" not in text
    assert 'default: "120"' in text
    assert 'default: "whipsaw-vwap-results"' in text
    assert "if: always()" in text
    assert "Refusing to push results" in text
    assert "main|master" in text
    assert "results/WHIPSAW_VWAP.md" in text
    assert "results/whipsaw_vwap_trades.csv" in text
    assert "python whipsaw_vwap.py" in text
    readme = open("README.md").read()
    assert "Vix Fix whipsaw VWAP check (real option prices)" in readme
    assert "whipsaw-vwap-results" in readme
    assert "Run workflow" in readme
    assert "Do not tap Re-run" in readme
    for banned in ("submit_order", "TradingClient", "MarketOrderRequest", "paper=True"):
        assert banned not in text
        assert banned not in src
