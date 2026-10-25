"""Walk-forward edge hunt: no lookahead, folds, cooldown, FDR, luck, reversals. No network, no orders."""

from datetime import date, datetime, timedelta

import numpy as np
import pandas as pd
import pytest

import edge_hunt as eh
import scalp_real as sc


def test_confirmed_pivot_waits_for_the_right_wing():
    n = 40
    high = np.full(n, 10.0)
    low = np.full(n, 9.0)
    low[10] = 5.0
    high[10] = 14.0
    lo, hi = eh.confirmed_pivots(high, low, left=5, right=5)
    assert not lo[10] and not hi[10]
    assert lo[15] and hi[15]
    assert not lo[:15].any() and not hi[:15].any()
    # A bar after the confirmation is not read.
    low2 = low.copy()
    high2 = high.copy()
    low2[20] = 1.0
    high2[20] = 1.0
    lo2, hi2 = eh.confirmed_pivots(high2, low2, 5, 5)
    assert np.array_equal(lo[:16], lo2[:16])
    assert np.array_equal(hi[:16], hi2[:16])
    # A bar inside the right wing kills the pivot. Equal neighbors are not strict.
    low3 = low.copy()
    low3[12] = 4.0
    lo3, _ = eh.confirmed_pivots(high, low3, 5, 5)
    assert not lo3[15]
    low4 = low.copy()
    low4[8] = 5.0
    lo4, _ = eh.confirmed_pivots(high, low4, 5, 5)
    assert not lo4[15]
    direction = eh.pivot_direction(high, low, 5, 5)
    # Both a high and a low confirm on the same bar -> no direction.
    assert direction[15] == 0
    low_only = low.copy()
    lo_only, hi_only = eh.confirmed_pivots(np.full(n, 10.0), low_only, 5, 5)
    assert lo_only[15] and not hi_only[15]
    assert eh.pivot_direction(np.full(n, 10.0), low_only, 5, 5)[15] == 1


def test_divergence_is_flagged_on_the_second_confirmation_only():
    n = 40
    high = np.full(n, 20.0)
    low = np.full(n, 10.0)
    left = right = 3
    low[8] = 6.0
    low[16] = 5.0
    hist = np.zeros(n)
    hist[8] = -3.0
    hist[16] = -1.0
    bull, bear = eh.regular_divergence(high, low, hist, left, right)
    conf = 16 + right
    assert bull[conf]
    assert not bull[:conf].any()
    assert not bear.any()
    # Histogram is read at the pivot bars, not at the confirmation bar.
    hist2 = hist.copy()
    hist2[conf] = -100.0
    bull2, _ = eh.regular_divergence(high, low, hist2, left, right)
    assert bull2[conf]
    # A future bar after confirmation does not remove it.
    low_future = low.copy()
    low_future[conf + 2] = 1.0
    bull3, _ = eh.regular_divergence(high, low_future, hist, left, right)
    assert np.array_equal(bull[: conf + 1], bull3[: conf + 1])
    # An equal low inside the right wing removes the second pivot, so the divergence never prints.
    low_kill = low.copy()
    low_kill[16 + 1] = 5.0
    bull4, _ = eh.regular_divergence(high, low_kill, hist, left, right)
    assert not bull4.any()
    # Bearish: higher high in price, lower high in the histogram.
    high_b = np.full(n, 20.0)
    low_b = np.full(n, 10.0)
    high_b[8] = 30.0
    high_b[16] = 32.0
    hist_b = np.zeros(n)
    hist_b[8] = 2.0
    hist_b[16] = 1.0
    bull_b, bear_b = eh.regular_divergence(high_b, low_b, hist_b, left, right)
    assert bear_b[conf] and not bull_b[conf]
    assert eh.divergence_direction(high_b, low_b, hist_b, left, right)[conf] == -1
    assert eh.divergence_direction(high, low, hist, left, right)[conf] == 1


def test_macd_events_are_causal_and_named():
    close = np.linspace(100.0, 110.0, 50)
    hist = eh.macd_histogram(close)
    bumped = close.copy()
    bumped[-1] = 1000.0
    hist2 = eh.macd_histogram(bumped)
    assert np.allclose(hist[:-1], hist2[:-1])
    zero, shrink, flip = eh.macd_event_directions(hist)
    z2, s2, f2 = eh.macd_event_directions(hist2)
    assert np.array_equal(zero[:-1], z2[:-1])
    assert np.array_equal(shrink[:-1], s2[:-1])
    assert np.array_equal(flip[:-1], f2[:-1])

    hand = np.array([-0.2, -0.1, 0.1, 0.05, 0.2])
    zero, shrink, flip = eh.macd_event_directions(hand)
    assert zero.tolist() == [0, 0, 1, 0, 0]
    assert shrink.tolist() == [0, -1, 0, 1, 0]
    assert flip[3] == -1 and flip[4] == 1
    # Editing the last bar does not move the earlier cross, shrink, or flip.
    edited = hand.copy()
    edited[-1] = -5.0
    zero_e, shrink_e, flip_e = eh.macd_event_directions(edited)
    assert np.array_equal(zero[:-1], zero_e[:-1])
    assert np.array_equal(shrink[:-1], shrink_e[:-1])
    assert flip_e[3] == -1
    down = np.array([0.2, 0.1, -0.3])
    assert eh.macd_event_directions(down)[0].tolist() == [0, 0, -1]


def test_wvf_rollover_is_the_bar_after_the_spike():
    w = np.array([10.0, 50.0, 80.0, 70.0, 70.0, 90.0])
    fire = eh.wvf_rollover_mask(w, 60)
    assert fire.tolist() == [False, False, False, True, False, False]
    future = w.copy()
    future[-1] = 1.0
    assert np.array_equal(eh.wvf_rollover_mask(future, 60)[:4], fire[:4])
    # Flattening the bar after the spike removes the rollover. The spike bar itself never fires.
    killed = w.copy()
    killed[3] = 85.0
    assert not eh.wvf_rollover_mask(killed, 60)[3]
    assert not fire[2]


def test_squeeze_release_needs_a_color_flip():
    on = np.array([True, True, False, False, False])
    mom = np.array([1.0, 2.0, 1.0, 0.5, 0.4])
    out = eh.squeeze_release_direction(on, mom)
    assert out.tolist() == [0, 0, 1, 0, 0]
    # Same-sign slope is not a color flip, so the release is ignored.
    straight = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    assert eh.squeeze_release_direction(on, straight).tolist() == [0, 0, 0, 0, 0]
    # No release while the squeeze stays on.
    still = np.array([True, True, True, False, False])
    assert eh.squeeze_release_direction(still, mom)[2] == 0
    # The slope into that later release does not change sign, so it is not a signal.
    assert eh.squeeze_release_direction(still, mom)[3] == 0
    flip_later = np.array([1.0, 2.0, 3.0, 1.0, 0.5])
    assert eh.squeeze_release_direction(still, flip_later)[3] == 1
    bear = np.array([1.0, 2.0, -0.4, -0.2, 0.0])
    released = eh.squeeze_release_direction(on, bear)
    assert released[2] == -1


def test_vwap_stretch_requires_the_volume_spike():
    dist = np.array([2.0, -2.0, 2.0, 0.5, -1.5])
    rvol = np.array([1.5, 2.0, 1.49, 3.0, 1.5])
    out = eh.vwap_rvol_direction(dist, rvol, stretch=1.0, rvol_min=1.5)
    assert out.tolist() == [1, -1, 0, 0, -1]
    assert eh.vwap_rvol_direction(dist, rvol, stretch=1.6, rvol_min=1.5).tolist() == [1, -1, 0, 0, 0]


def test_asof_known_does_not_use_a_future_value():
    known = np.array([100, 200, 200], dtype=np.int64)
    values = np.array([1.0, 5.0, 9.0])
    bars = np.array([99, 100, 150, 200, 250], dtype=np.int64)
    got = eh.asof_known(bars, known, values)
    # Two values share time 200; the later one in file order is kept by a stable sort.
    assert np.isnan(got[0])
    assert got[1] == 1.0
    assert got[2] == 1.0
    assert got[3] == 9.0
    assert got[4] == 9.0


def test_htf_event_stamps_the_confirmation_minute_only():
    dest = np.zeros((1, 8), dtype=np.int8)
    t0 = 1_700_000_000_000_000_000
    step = 60_000_000_000
    lookup = {t0 + i * step: (0, i) for i in range(8)}
    known = np.array([t0 + 3 * step], dtype=np.int64)
    eh._stamp_direction(dest, lookup, known, np.array([1]))
    assert dest[0].tolist() == [0, 0, 1, 0, 0, 0, 0, 0]
    # A later bar does not inherit the event.
    eh._stamp_direction(dest, lookup, np.array([t0 + 6 * step]), np.array([-1]))
    assert dest[0, 5] == -1
    assert dest[0, 2] == 1
    assert dest[0, 3] == 0 and dest[0, 4] == 0


def test_prior_vix_ignores_the_session_and_the_future():
    days = [date(2024, 1, d) for d in (8, 9, 10, 11, 12)]
    closes = {
        date(2024, 1, 2): 10.0,
        date(2024, 1, 3): 11.0,
        date(2024, 1, 4): 12.0,
        date(2024, 1, 5): 13.0,
        date(2024, 1, 8): 14.0,
        date(2024, 1, 9): 99.0,
        date(2024, 1, 12): 50.0,
    }
    prior, chg = eh.prior_vix_features(days, closes)
    # Jan 8 sees Jan 5 only: fewer than 5 closes, so the change is blank.
    assert prior[0] == 13.0
    assert np.isnan(chg[0])
    # Jan 9 sees Jan 8, not the 99 printed on Jan 9.
    assert prior[1] == 14.0
    window = np.array([10.0, 11.0, 12.0, 13.0, 14.0])
    assert chg[1] == pytest.approx(14.0 - window.mean())
    # Jan 10 still does not see Jan 9's 99, because that close is not before Jan 10? 
    # Jan 9 is before Jan 10, so Jan 10 DOES see 99. Jan 12 sees 50 only as its own close, which is ignored,
    # and the prior close is Jan 9's 99 (Jan 10 and 11 have no print).
    assert prior[2] == 99.0
    assert prior[4] == 99.0
    poisoned = dict(closes)
    poisoned[date(2024, 1, 10)] = 7.0
    prior2, _ = eh.prior_vix_features(days, poisoned)
    assert prior2[2] == 99.0
    assert prior2[3] == 7.0


def test_synthetic_vix_loader_does_not_leak_the_same_day():
    days = list(pd.bdate_range("2024-03-01", periods=8).date)
    vix, source = eh.load_vix_closes(days)
    assert source == "synthetic"
    prior, _chg = eh.prior_vix_features(days, vix)
    poisoned = dict(vix)
    poisoned[days[4]] = 1234.0
    prior2, _ = eh.prior_vix_features(days, poisoned)
    assert prior2[4] == pytest.approx(prior[4])
    assert prior2[5] == 1234.0


def test_fred_vix_parser_skips_missing_dots():
    text = "DATE,VIXCLS\n2024-01-02,12.5\n2024-01-03,.\n2024-01-04,13\n"
    parsed = eh._parse_fred_vix(text)
    assert parsed[date(2024, 1, 2)] == 12.5
    assert date(2024, 1, 3) not in parsed
    assert parsed[date(2024, 1, 4)] == 13.0
    yahoo = "Date,Open,High,Low,Close,Adj Close,Volume\n2024-01-02,1,2,0.5,11.5,11.5,0\n"
    assert eh._parse_yahoo_csv(yahoo)[date(2024, 1, 2)] == 11.5


def test_relative_volume_uses_only_prior_days():
    vol = np.array([
        [10.0, 10.0],
        [100.0, 40.0],
        [1000.0, 80.0],
    ])
    got = eh.relative_volume(vol, window=20)
    assert np.isnan(got[0]).all()
    assert got[1, 0] == pytest.approx(10.0)
    assert got[2, 0] == pytest.approx(1000.0 / np.median([10.0, 100.0]))
    future = vol.copy()
    future[2, 0] = 1.0
    again = eh.relative_volume(future, window=20)
    assert again[1, 0] == pytest.approx(got[1, 0])
    # Today's own volume is the numerator, not part of the median.
    today = vol.copy()
    today[1, 0] = 200.0
    shifted = eh.relative_volume(today, window=20)
    assert shifted[1, 0] == pytest.approx(20.0)
    assert shifted[2, 0] == pytest.approx(1000.0 / np.median([10.0, 200.0]))


def test_daily_context_and_opening_range_ignore_later_bars():
    opens = np.full((2, 30), 100.0)
    highs = np.full((2, 30), 110.0)
    lows = np.full((2, 30), 90.0)
    closes = np.full((2, 30), 100.0)
    closes[0, -1] = 100.0
    opens[1, 0] = 102.0
    highs[1, 16] = 900.0
    closes[1, 20] = 400.0
    ctx = eh.daily_price_context(opens, highs, lows, closes)
    assert ctx["gap_pct"][1] == pytest.approx(0.02)
    assert ctx["gap_vs_range"][1] == pytest.approx(2.0 / 20.0)
    assert ctx["prior_range_pct"][1] == pytest.approx(0.20)
    assert ctx["prior_close_pos"][1] == pytest.approx(0.5)
    assert ctx["or_size"][1] == pytest.approx((110.0 - 90.0) / 102.0)
    # Minute 16 is outside the opening range.
    highs2 = highs.copy()
    highs2[1, 3] = 130.0
    ctx2 = eh.daily_price_context(opens, highs2, lows, closes)
    assert ctx2["or_size"][1] == pytest.approx((130.0 - 90.0) / 102.0)
    assert ctx2["gap_pct"][1] == pytest.approx(ctx["gap_pct"][1])

    high = np.full(30, 10.0)
    low = np.full(30, 8.0)
    close = np.full(30, 9.0)
    close[15] = 11.0
    close[16] = 7.0
    high[20] = 50.0
    brk = eh.opening_range_break(high, low, close)
    assert np.isnan(brk[:14]).all()
    assert brk[14] == 0.0
    assert brk[15] == 1.0
    assert brk[16] == -1.0
    # The range is frozen at bar 14. A later extreme does not move the break.
    high_b = high.copy()
    high_b[18] = 100.0
    low_b = low.copy()
    low_b[18] = 1.0
    assert np.array_equal(eh.opening_range_break(high_b, low_b, close), brk, equal_nan=True)


def _rth_frame(days, seed=0):
    parts = []
    for d in days:
        parts.append(pd.date_range(
            pd.Timestamp(datetime(d.year, d.month, d.day), tz="America/New_York") + pd.Timedelta(hours=9, minutes=30),
            periods=eh.N_MIN,
            freq="1min",
        ))
    index = pd.concat([pd.Series(np.arange(len(p)), index=p) for p in parts]).index
    rng = np.random.default_rng(seed)
    steps = rng.normal(0.0, 0.03, len(index))
    close = 500.0 + np.cumsum(steps)
    open_ = np.r_[500.0, close[:-1]]
    high = np.maximum(open_, close) + 0.05
    low = np.minimum(open_, close) - 0.05
    vol = rng.integers(1000, 5000, len(index)).astype(float)
    return pd.DataFrame(
        {"open": open_, "high": high, "low": low, "close": close, "volume": vol},
        index=index,
    )


def test_compute_features_does_not_look_ahead():
    days = [date(2024, 1, 2) + timedelta(days=i) for i in range(4)]
    score = days[2:]
    df = _rth_frame(days, seed=3)
    vix = {d: 15.0 + i for i, d in enumerate(pd.bdate_range(days[0] - timedelta(days=20), days[-1]).date)}
    panel = eh.compute_features({"SPY": df}, vix, score, ["SPY"])
    cut = 100
    mutated = df.copy()
    session_minute = mutated.index.hour * 60 + mutated.index.minute - (9 * 60 + 30)
    mask = np.asarray(mutated.index.date == days[-1]) & np.asarray(session_minute >= cut)
    assert mask.any()
    mutated.loc[mask, ["open", "high", "low", "close"]] += 80.0
    mutated.loc[mask, "volume"] *= 10.0
    later = eh.compute_features({"SPY": mutated}, vix, score, ["SPY"])
    for name, arr in panel.f.items():
        assert np.array_equal(arr[:-1], later.f[name][:-1], equal_nan=True), name
        assert np.array_equal(arr[-1, :, :cut], later.f[name][-1, :, :cut], equal_nan=True), name
    for name, arr in panel.ev.items():
        assert np.array_equal(arr[:-1], later.ev[name][:-1]), name
        assert np.array_equal(arr[-1, :, :cut], later.ev[name][-1, :, :cut]), name
    for name, arr in panel.daily.items():
        assert np.array_equal(arr, later.daily[name], equal_nan=True), name
    # The shock is visible after the cut, so the comparison above is not vacuous.
    assert not np.allclose(
        panel.f["ret_5"][-1, 0, cut + 10],
        later.f["ret_5"][-1, 0, cut + 10],
        equal_nan=True,
    )


def test_fade_and_follow_take_opposite_sides_at_the_next_bar():
    day = date(2024, 1, 2)
    panel = eh.Panel([day], ["SPY"])
    for name in ("vwap_atr", "rvol", "wvf_1m", "wvi_1m"):
        panel.add_f(name)
    for name in eh.FIXED_EVENTS + eh.GRID_EVENTS:
        if name in ("vwap_rvol",) or "roll" in name:
            continue
        panel.add_ev(name)
    panel.ev["swing_1m"][0, 0, 20] = 1
    panel.ev["div_5m"][0, 0, 30] = -1
    panel.ev["macd_zero_1m"][0, 0, 40] = 1
    panel.ev["macd_shrink_1m"][0, 0, 42] = -1
    panel.ev["macd_flip_3m"][0, 0, 44] = 1
    panel.ev["sq_release_1m"][0, 0, 46] = -1
    follow = eh._cond("event", "swing_1m", "event", "follow", -1, "event")
    fade = eh._cond("event", "swing_1m", "event", "fade", -1, "event")
    call_f, put_f = eh.entry_masks(panel, follow, None)
    call_a, put_a = eh.entry_masks(panel, fade, None)
    assert call_f[0, 0, 21] and not put_f[0, 0, 21]
    assert put_a[0, 0, 21] and not call_a[0, 0, 21]
    assert not call_f[0, 0, 20] and not put_a[0, 0, 20]
    # Bearish divergence: follow buys the put, fade buys the call.
    call_f, put_f = eh.entry_masks(panel, eh._cond("event", "div_5m", "event", "follow", -1, "event"), None)
    call_a, put_a = eh.entry_masks(panel, eh._cond("event", "div_5m", "event", "fade", -1, "event"), None)
    assert put_f[0, 0, 31] and not call_f[0, 0, 31]
    assert call_a[0, 0, 31] and not put_a[0, 0, 31]
    for feat, minute, follow_call in (
        ("macd_zero_1m", 40, True),
        ("macd_shrink_1m", 42, False),
        ("macd_flip_3m", 44, True),
        ("sq_release_1m", 46, False),
    ):
        call_f, put_f = eh.entry_masks(panel, eh._cond("event", feat, "event", "follow", -1, "event"), None)
        call_a, put_a = eh.entry_masks(panel, eh._cond("event", feat, "event", "fade", -1, "event"), None)
        entry = minute + 1
        if follow_call:
            assert call_f[0, 0, entry] and put_a[0, 0, entry]
        else:
            assert put_f[0, 0, entry] and call_a[0, 0, entry]
        assert not (call_f[0, 0, entry] and put_f[0, 0, entry])
    panel.f["vwap_atr"][0, 0, 50] = 2.0
    panel.f["rvol"][0, 0, 50] = 1.5
    call_f, put_f = eh.entry_masks(panel, eh._cond("event", "vwap_rvol", "event", "follow", -1, "event"), 1.0)
    call_a, put_a = eh.entry_masks(panel, eh._cond("event", "vwap_rvol", "event", "fade", -1, "event"), 1.0)
    assert call_f[0, 0, 51] and put_a[0, 0, 51]
    panel.f["vwap_atr"][0, 0, 50] = 2.0
    panel.f["rvol"][0, 0, 50] = 1.2
    call_f, _put_f = eh.entry_masks(panel, eh._cond("event", "vwap_rvol", "event", "follow", -1, "event"), 1.0)
    assert not call_f[0, 0, 51]
    wvf = np.full(eh.N_MIN, np.nan)
    wvf[60] = 40.0
    wvf[61] = 80.0
    wvf[62] = 70.0
    wvf[63] = 70.0
    panel.f["wvf_1m"][0, 0, :] = wvf
    call_f, put_f = eh.entry_masks(panel, eh._cond("event", "wvf_roll_1m", "event", "follow", -1, "event"), 60.0)
    call_a, put_a = eh.entry_masks(panel, eh._cond("event", "wvf_roll_1m", "event", "fade", -1, "event"), 60.0)
    assert call_f[0, 0, 63] and not put_f[0, 0, 63]
    assert put_a[0, 0, 63] and not call_a[0, 0, 63]
    assert not call_f[0, 0, 62]
    panel.f["wvi_1m"][0, 0, :] = wvf
    call_f, put_f = eh.entry_masks(panel, eh._cond("event", "wvi_roll_1m", "event", "follow", -1, "event"), 60.0)
    call_a, _put_a = eh.entry_masks(panel, eh._cond("event", "wvi_roll_1m", "event", "fade", -1, "event"), 60.0)
    assert put_f[0, 0, 63] and call_a[0, 0, 63]


def test_shift_signal_stays_inside_the_entry_window():
    sig = np.zeros((1, 1, eh.N_MIN), dtype=bool)
    sig[0, 0, 10] = True
    sig[0, 0, 14] = True
    sig[0, 0, eh.LAST_ENTRY] = True
    out = eh.shift_signal(sig)
    assert out[0, 0, 15]
    assert not out[0, 0, 10]
    assert not out[0, 0, 14]
    assert not out[0, 0, eh.LAST_ENTRY]
    if eh.LAST_ENTRY + 1 < eh.N_MIN:
        assert not out[0, 0, eh.LAST_ENTRY + 1]


def test_walk_forward_folds_are_expanding_prefixes():
    with pytest.raises(ValueError):
        eh.walk_forward_folds(eh.K_FOLDS, eh.K_FOLDS)
    for n, first in ((18, 3), (30, 5), (170, 29)):
        folds = eh.walk_forward_folds(n, 5)
        assert len(folds) == 5
        covered = []
        prev = -1
        for train, test in folds:
            assert train.tolist() == list(range(int(test[0])))
            assert int(train.max()) < int(test.min())
            assert int(test.min()) == prev + 1 or prev < 0
            prev = int(test.max())
            covered.extend(test.tolist())
            assert len(set(test.tolist())) == len(test)
        assert covered == list(range(first, n))
        assert folds[0][0].tolist() == list(range(first))
    folds = eh.walk_forward_folds(170, 5)
    assert folds[0][1].tolist() == list(range(29, 58))
    assert len(folds[-1][1]) == 28


def test_cooldown_is_per_day_and_call_wins_the_tie():
    call = np.zeros((2, 1, 30), dtype=bool)
    put = np.zeros((2, 1, 30), dtype=bool)
    put[0, 0, 0] = True
    call[0, 0, 5] = True
    put[0, 0, 5] = True
    call[0, 0, 10] = True
    put[0, 0, 19] = True
    call[1, 0, 0] = True
    day, sym, minute, side = eh.cooldown_indices(call, put, gap=10)
    kept = {(int(d), int(m), int(s)) for d, m, s in zip(day, minute, side)}
    assert kept == {(0, 0, 1), (0, 10, 0), (1, 0, 0)}
    assert (0, 5, 0) not in kept and (0, 19, 1) not in kept
    assert (sym == 0).all()


def test_fdr_matches_bh_and_grows_with_the_family():
    p = np.array([0.01, 0.04, 0.5])
    q = eh.fdr_qvalues(p, family_n=3)
    assert q.tolist() == pytest.approx([0.03, 0.06, 0.5])
    wider = eh.fdr_qvalues(p, family_n=10)
    assert wider.tolist() == pytest.approx([0.1, 0.2, 1.0])
    assert np.all(wider >= q)
    raw = eh.fdr_qvalues(p)
    assert np.allclose(raw, sc.benjamini_hochberg(p), equal_nan=True)
    mixed = np.array([np.nan, 0.01])
    assert np.isnan(eh.fdr_qvalues(mixed)[0])
    slotted = eh.fdr_qvalues(mixed, family_n=2)
    assert slotted[1] == pytest.approx(0.02)
    assert slotted[0] == pytest.approx(1.0)


def test_luck_benchmark_and_day_label_shuffle():
    summary = eh.luck_shuffle_benchmark([1.0, 3.0, 2.0], [4, 0, 2])
    assert summary["n_shuf"] == 3
    assert summary["best_oos_net"] == 3.0
    assert summary["median_best_oos_net"] == 2.0
    assert summary["expected_rules_as_good"] == pytest.approx(2.0)
    empty = eh.luck_shuffle_benchmark([], [])
    assert empty["n_shuf"] == 0 and np.isnan(empty["best_oos_net"])
    perm = eh.day_label_permutations(8, 5, 123)
    again = eh.day_label_permutations(8, 5, 123)
    assert np.array_equal(perm, again)
    for row in perm:
        assert sorted(row.tolist()) == list(range(8))
    panel = eh.Panel([date(2024, 1, d) for d in range(1, 4)], ["SPY"])
    panel.add_daily("gap_pct")
    panel.daily["gap_pct"][:, 0] = [1.0, 2.0, 3.0]
    panel.add_f("ret_5")
    panel.f["ret_5"][0, 0, 0] = 7.0
    panel.add_ev("swing_1m")
    panel.ev["swing_1m"][1, 0, 4] = -1
    shuffled = panel.shuffled(np.array([2, 0, 1]))
    assert shuffled.daily["gap_pct"][:, 0].tolist() == [3.0, 1.0, 2.0]
    assert shuffled.f is panel.f and shuffled.ev is panel.ev
    assert shuffled.f["ret_5"][0, 0, 0] == 7.0
    assert shuffled.ev["swing_1m"][1, 0, 4] == -1


def test_clustered_t_matches_scalp_real():
    rng = np.random.default_rng(0)
    values = rng.normal(size=30)
    day_ids = np.repeat(np.arange(10), 3)
    sums = np.bincount(day_ids, weights=values, minlength=10)
    cnts = np.bincount(day_ids, minlength=10).astype(float)
    t1, p1 = eh.clustered_t_from_days(sums, cnts)
    t2, p2 = sc.clustered_t(values, day_ids, 10)
    assert t1 == pytest.approx(t2)
    assert p1 == pytest.approx(p2)


def test_accumulate_pack_order_is_sum_count_hit():
    net = np.full((1, 1, 5, 2, 1, 1), np.nan)
    hit = np.zeros_like(net)
    net[0, 0, 2, 0, 0, 0] = 4.0
    day = np.array([0])
    sym = np.array([0])
    minute = np.array([2])
    side = np.array([0])
    sums, cnts, hits = eh.accumulate_entries(day, sym, minute, side, net, hit)
    assert sums[0, 0, 0, 0] == 4.0
    assert cnts[0, 0, 0, 0] == 1.0
    assert hits[0, 0, 0, 0] == 0.0


def test_primary_exit_picks_the_threshold_not_the_other_exit():
    def pack(sum0, sum1, cnt=2.0):
        sm = np.zeros((2, 1, 1, 2))
        ct = np.full((2, 1, 1, 2), cnt)
        ht = np.zeros((2, 1, 1, 2))
        sm[:, :, 0, 0] = sum0
        sm[:, :, 0, 1] = sum1
        return sm, ct, ht

    gates = [np.ones((2, 1), dtype=bool)]
    legs = [pack(50.0, 1.0), pack(0.0, 20.0)]
    train = np.array([0, 1])
    code, n_p = eh._select_codes(gates, legs, train, min_train=1, primary_i=1)
    assert n_p == 2 and int(code[0]) == 1
    code0, _ = eh._select_codes(gates, legs, train, min_train=1, primary_i=0)
    assert int(code0[0]) == 0
    missing, _ = eh._select_codes(gates, legs, train, min_train=100, primary_i=1)
    assert int(missing[0]) == -1


def _opt_book(prices):
    rec = sc._empty_opt()
    for minute, px in prices.items():
        rec["open"][minute] = px
        rec["high"][minute] = px * 1.30
        rec["low"][minute] = px * 0.95
        rec["close"][minute] = px
        rec["real"][minute] = True
    rec["lab"] = pd.Series(rec["close"]).ffill(limit=sc.STALE_AFTER).to_numpy()
    return rec


def test_slip_matches_simulate_trade_and_does_not_slide_a_premium_skip():
    day = date(2024, 6, 3)
    sess = {k: np.full(eh.N_MIN, 500.0) for k in ("open", "high", "low", "close")}
    sess["open"][21] = 501.0
    sess["real"] = np.ones(eh.N_MIN, dtype=bool)
    und = {"SPY": {day: sess}}
    book_500 = _opt_book({30: 2.00, 31: 0.60, 40: 0.60, 41: 0.70})
    book_501 = _opt_book({21: 0.60})
    bt = sc._bt()
    opt = {
        (day, bt.lab_occ("SPY", day, "C", 500)): book_500,
        (day, bt.lab_occ("SPY", day, "P", 500)): book_500,
        (day, bt.lab_occ("SPY", day, "C", 501)): book_501,
        (day, bt.lab_occ("SPY", day, "P", 501)): book_501,
    }
    exits = (eh.PRIMARY_EXIT,)
    costs = (0.01, 0.005, 0.65)
    premium = (0.45, 0.80)
    net, _hit = eh.build_outcome_cube([day], ["SPY"], und, opt, ("atm",), exits, costs, premium, progress=False)

    def filled(book, minute):
        trial = sc.simulate_trade(book, minute, exits[0], costs, allow_slip=False, premium=premium)
        assert trial["status"] == "fill"
        return trial["net_pct"]

    # No print at minute 20 on the 500 strike. The next minute is a different strike and is used.
    assert net[0, 0, 20, 0, 0, 0] == pytest.approx(filled(book_501, 21))
    assert net[0, 0, 21, 0, 0, 0] == pytest.approx(filled(book_501, 21))
    # Premium skip at minute 30 does not slide into the in-band print at 31.
    assert np.isnan(net[0, 0, 30, 0, 0, 0])
    assert net[0, 0, 31, 0, 0, 0] == pytest.approx(filled(book_500, 31))
    # A real print does not slide, even though the next minute would fill at a different price.
    assert net[0, 0, 40, 0, 0, 0] == pytest.approx(filled(book_500, 40))
    assert filled(book_500, 40) != pytest.approx(filled(book_500, 41))
    direct = eh._price_minute(book_500, 30, exits, costs, premium)
    assert direct[0] == "premium"
    nxt = eh._price_minute(book_500, 31, exits, costs, premium)
    slid, _hits = eh._apply_slip(direct, nxt)
    assert np.isnan(slid).all()
    missed = eh._price_minute(book_500, 20, exits, costs, premium)
    assert missed[0] == "miss"
    used, _h = eh._apply_slip(missed, eh._price_minute(book_501, 21, exits, costs, premium))
    assert used[0] == pytest.approx(filled(book_501, 21))


def test_family_has_both_directions_and_disjoint_pairs():
    specs = eh.build_family()
    again = eh.build_family()
    names = [s.name for s in specs]
    assert names == [s.name for s in again]
    assert len(names) == len(set(names))
    for feat in eh.FIXED_EVENTS + eh.GRID_EVENTS:
        assert f"single {feat} follow" in names
        assert f"single {feat} fade" in names
    for spec in specs:
        gate = spec.day_gate if spec.day_gate is not None else spec.minute_gate
        if gate is None:
            assert spec.kind == "single"
            continue
        assert not (eh._sources(gate) & eh._sources(spec.leg))
        if spec.kind == "pair":
            assert spec.leg.kind != "always"
    # Reversal events are in the family on the timeframes the search promised.
    for feat in (
        "macd_zero_1m", "macd_shrink_1m", "macd_flip_1m",
        "macd_zero_3m", "macd_shrink_3m", "macd_flip_3m",
        "div_1m", "div_3m", "div_5m",
        "swing_1m", "swing_3m",
        "vwap_rvol",
        "wvf_roll_1m", "wvf_roll_3m", "wvi_roll_1m", "wvi_roll_3m",
        "sq_release_1m", "sq_release_3m",
    ):
        assert any(s.leg.feature == feat and s.leg.mode == "fade" for s in specs)
        assert any(s.leg.feature == feat and s.leg.mode == "follow" for s in specs)
    assert "Follow trades" in eh.reversal_blurb() and "Fade trades" in eh.reversal_blurb()
    assert eh._parse_strikes("1otm,atm") == ("1otm", "atm")
    assert eh._parse_strikes("atm,1otm") == ("atm", "1otm")
    with pytest.raises(SystemExit):
        eh._parse_strikes("nope")


def test_planted_event_beats_random_inside_the_walk_forward():
    n_days = 18
    days = [date(2024, 2, 1) + timedelta(days=i) for i in range(n_days)]
    panel = eh.Panel(days, ["SPY"])
    panel.add_ev("macd_zero_1m")
    panel.ev["macd_zero_1m"][:, 0, 20] = 1
    panel.add_daily("vix_chg_5d")
    panel.daily["vix_chg_5d"][:, 0] = np.linspace(-1.0, 1.0, n_days)
    event = eh._cond("event", "macd_zero_1m", "event", "follow", -1, "event")
    daily = eh._cond("signed", "vix_chg_5d", "mag", "follow", -1, "daily")
    family = [
        eh.Spec("single macd_zero_1m follow", "single", None, None, event),
        eh.Spec("single vix_chg_5d follow", "single", None, None, daily),
    ]
    exits = ((0.10, 0.10, 10), eh.PRIMARY_EXIT)
    net = np.full((n_days, 1, eh.N_MIN, 2, 1, len(exits)), -5.0, dtype=np.float32)
    net[:, 0, 21, 0, 0, 1] = 10.0
    hit = np.zeros_like(net)
    result = eh.run_search(
        panel, net, hit, ("atm",), exits,
        n_shuf=4, seed=7, min_train=1, min_quantile_n=1, boot=20,
        family=family, progress=False,
    )
    assert result["family_size"] == 4
    planted = [r for r in result["rows"] if r["name"].startswith("single macd_zero") and r["exit_index"] == 1]
    assert len(planted) == 1
    row = planted[0]
    assert row["n"] == 15
    assert row["mean_net_pct"] == pytest.approx(10.0)
    assert row["hit_rate"] == pytest.approx(0.0)
    assert row["mean_net_pct"] > 0
    assert row["beats_random"] == 1
    assert row["random_mean_net_pct"] < 0
    assert row["folds_positive"] == 5
    assert row["candidate"] == 1
    assert row["sensitive"] == 0
    daily_rows = [r for r in result["rows"] if r["sensitive"] == 1]
    assert daily_rows
    luck = result["luck"]
    assert luck["n_shuf"] == 4
    assert math_isfinite(luck["best_oos_net"])
    assert math_isfinite(luck["median_best_oos_net"])
    assert math_isfinite(luck["expected_rules_as_good"])
    assert luck["best_oos_net"] + 1e-6 >= row["mean_net_pct"]
    text = eh.render_report({
        "stamp": "2026-10-25 09:00 ET",
        "span": f"SPY, {n_days} sessions, {days[0].isoformat()} through {days[-1].isoformat()}.",
        "family_size": result["family_size"],
        "n_specs": result["n_specs"],
        "n_strikes": 1,
        "n_exits": len(exits),
        "luck": luck,
        "method": "method",
        "limits": eh._limits_text(),
    }, result["rows"])
    assert "Verdict:" in text
    assert "1 candidate rule." in text
    assert "Luck benchmark" in text
    assert days[0].isoformat() in text
    assert "not a trade list" in text
    assert "Fade trades" in text and "Follow trades" in text
    assert "Data only" in text


def math_isfinite(value):
    return isinstance(value, (int, float)) and np.isfinite(value)


def test_workflow_is_manual_data_only_and_cannot_push_main():
    text = open(".github/workflows/edge_hunt.yml").read()
    assert text.startswith("name: Edge hunt (walk-forward, real option prices)\n")
    assert "workflow_dispatch:" in text
    assert "schedule:" not in text
    assert "ALPACA_KEY: ${{ secrets.ALPACA_KEY }}" in text
    assert "ALPACA_SECRET: ${{ secrets.ALPACA_SECRET }}" in text
    assert 'git push origin "HEAD:${BRANCH}"' in text
    assert "Refusing to push results" in text
    assert "main|master" in text
    assert '[[ "$BRANCH" =~ ^[A-Za-z0-9._/-]+$ ]]' in text
    assert 'HEADBR="$(git rev-parse --abbrev-ref HEAD)"' in text
    assert 'mkdir -p /tmp/edge-out' in text
    assert "rm -f results/EDGE_HUNT.md" in text
    assert 'git checkout -B "$BRANCH"' in text
    assert 'default: "edge-hunt-results"' in text
    assert 'default: "170"' in text
    assert 'default: "1otm,atm"' in text
    assert 'default: "0.45"' in text and 'default: "0.80"' in text
    assert 'default: "false"' in text
    assert "EDGE_QUICK:" in text
    assert "python -m pytest -q tests/test_edge_hunt.py" in text
    assert "results/EDGE_HUNT.md" in text
    assert "results/edge_hunt_rules.csv" in text
    assert "results/edge_hunt_trades.csv" in text
    for banned in ("submit_order", "TradingClient", "MarketOrderRequest"):
        assert banned not in text
    readme = open("README.md").read()
    assert "Edge hunt (walk-forward, real option prices)" in readme
    assert "Run workflow" in readme
    assert "Do not tap Re-run" in readme
    assert "edge-hunt-results" in readme
    src = open("edge_hunt.py").read()
    for banned in ("submit_order", "TradingClient", "MarketOrderRequest"):
        assert banned not in src
