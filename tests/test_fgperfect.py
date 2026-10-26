"""Greed/fear fade perfect-study math, the candidate gate, and the manual workflow. No orders, no network."""

import math
from datetime import datetime

import numpy as np
import pandas as pd
import pytest

import fgperfect as fp
import scalp_real as sc

NY = fp.NY


def test_exit_and_entry_families_are_predeclared():
    rules = fp.exit_rules()
    assert len(rules) == fp.expected_rule_count()
    assert len(rules) == len({r.id for r in rules})
    assert fp.REF_RULE in {r.id for r in rules}
    specs = fp.entry_specs()
    ids = {s.id for s in specs}
    assert len(specs) == len(ids)
    assert fp.BASE_ID in ids
    base = next(s for s in specs if s.id == fp.BASE_ID)
    assert base.kind == "base" and base.tf == 1 and base.g == 95 and base.f == 20
    for tf in (2, 3, 5):
        assert f"tf{tf}_turn_mom_g95_f20" in ids
    for g in (75, 80, 85, 90, 100):
        assert f"tf1_turn_mom_g{g}_f20" in ids
    for f in (0, 5, 10, 15, 25, 30, 35):
        assert f"tf1_turn_mom_g95_f{f}" in ids
    for k in (2, 3, 4, 5):
        assert f"tf1_turn_mom_g95_f20_k{k}" in ids
    for turn in ("drop1", "drop2", "drop3", "cross", "within1", "within2", "within3"):
        assert f"tf1_{turn}_mom_g95_f20" in ids
    for tag in ("atm", "2otm", "dte1", "mid1c", "edelay1", "edelay2", "spread1", "spread2", "spread5"):
        assert f"{fp.BASE_ID}__{tag}" in ids
    for tag, _lo, _hi in fp.PREMIUM_BANDS:
        assert f"{fp.BASE_ID}__prem_{tag}" in ids
    for bucket in fp.VIX_BUCKETS:
        assert f"{fp.BASE_ID}__vix_{bucket}" in ids
    for name, _a, _b in fp.TOD_BUCKETS:
        assert f"{fp.BASE_ID}__tod_{name}" in ids
    # GEX is not counted unless a file for these sessions is actually present.
    assert not any("gex_" in i for i in ids)
    assert fp.family_count() == len(specs) * len(rules)
    # One change at a time: the base book is shared by the masks and the cost rescores.
    masks = [s for s in specs if s.kind == "mask"]
    assert masks and all(s.book_key() == base.book_key() for s in masks)


def test_fixed_exit_matches_simulate_trade_and_the_stop_wins_a_tie():
    opt = sc._empty_opt()
    opt["real"][:] = True
    opt["open"][:] = 1.0
    opt["high"][:] = 1.0
    opt["low"][:] = 1.0
    opt["close"][:] = 1.0
    opt["low"][12] = 0.80
    opt["high"][12] = 1.30
    opt["open"][12] = 0.90
    got = sc.simulate_trade(opt, 10, (0.15, 0.15, 30), fp.COSTS, allow_slip=False)
    assert got["reason"] == "stop"
    rule = next(r for r in fp.exit_rules() if r.id == "fix_tp15_sl15_t30_d0")
    sl = slice(10, 13)
    one = fp.simulate_one(opt["open"][sl], opt["high"][sl], opt["low"][sl], opt["close"][sl], 1.0, rule)
    assert one["reason"] == fp.STOP
    assert one["net_pct"] == pytest.approx(got["net_pct"])
    assert one["dollar"] == pytest.approx(got["dollar"])


def test_phone_delay_sells_the_next_open():
    o = np.array([1.0, 1.0, 0.90, 0.70])
    h = np.array([1.0, 1.0, 1.30, 0.70])
    l = np.array([1.0, 1.0, 0.80, 0.70])
    c = np.array([1.0, 1.0, 1.00, 0.70])
    rule = next(r for r in fp.exit_rules() if r.id == "fix_tp15_sl15_t30_d1")
    one = fp.simulate_one(o, h, l, c, 1.0, rule)
    assert one["fill"] == pytest.approx(0.70)
    assert one["reason"] == fp.STOP


def test_trail_does_not_use_the_high_that_prints_after_the_stop():
    rule = next(r for r in fp.exit_rules() if r.id == "trail_a10_y5_d0")
    o = [1.00, 1.18]
    h = [1.20, 1.50]
    l = [1.00, 1.14]
    c = [1.10, 1.40]
    one = fp.simulate_one(o, h, l, c, 1.0, rule)
    assert one["reason"] == fp.TRAIL
    assert one["fill"] == pytest.approx(1.14)


def test_scale_out_is_the_average_of_the_two_halves():
    rule = next(r for r in fp.exit_rules() if r.id == "scale_s15_y10_d0")
    o = [1.00, 1.00, 1.10]
    h = [1.00, 1.20, 1.20]
    l = [1.00, 1.00, 1.00]
    c = [1.00, 1.10, 1.05]
    one = fp.simulate_one(o, h, l, c, 1.0, rule)
    half, _d1, _ = fp.net_from_fill(1.0, 1.15)
    runner, _d2, _ = fp.net_from_fill(1.0, 1.08)
    assert one["net_pct"] == pytest.approx(0.5 * float(half) + 0.5 * float(runner))


def test_spread_filter_is_the_cost_model_premium_floor():
    raw = np.array([0.19, 0.20, 0.49, 0.50, 0.99, 1.00])
    assert list(fp.spread_keep(raw, 0.05)) == [False, True, True, True, True, True]
    assert list(fp.spread_keep(raw, 0.02)) == [False, False, False, True, True, True]
    assert list(fp.spread_keep(raw, 0.01)) == [False, False, False, False, False, True]


def test_breakeven_rate_is_above_one_half():
    rate = sc.breakeven_hit_rate(0.15, 0.15, 0.50, *fp.COSTS)
    assert math.isfinite(rate) and rate > 0.5


def test_candidate_gate_uses_the_train_sample_only():
    train_mean = np.array([-5.0, 2.0, 1.0, 0.5])
    train_cnt = np.array([200, 150, 120, 110])
    train_days = np.array([80, 70, 65, 60])
    # The first config would win a test sample. It is not chosen, because the train mean is the worst.
    assert fp.choose_index(train_mean, train_cnt, train_days) == 1
    assert fp.choose_index(train_mean, np.array([10, 10, 10, 10]), train_days) == -1
    assert fp.choose_index(train_mean, train_cnt, np.array([10, 10, 10, 40])) == -1


def test_bh_family_size_is_the_number_of_configs():
    p = np.array([0.01, 0.20, 1.0])
    q = fp.eh.fdr_qvalues(p, family_n=len(p))
    wider = fp.eh.fdr_qvalues(p, family_n=len(p) + 50)
    assert len(q) == len(p)
    assert wider[0] > q[0]
    # An unscored row still occupies a slot.
    sums = np.array([[1.0, 1.0], [0.0, 0.0]])
    cnts = np.array([[1.0, 1.0], [0.0, 0.0]])
    got = fp.clustered_matrix(sums, cnts)
    assert got[1] == 1.0
    assert 0 < got[0] <= 1.0


def test_neighbours_of_the_reference_exit():
    rule = next(r for r in fp.exit_rules() if r.id == fp.REF_RULE)
    ids = set(fp.neighbor_ids(rule))
    assert "fix_tp10_sl15_t30_d0" in ids
    assert "fix_tp20_sl15_t30_d0" in ids
    assert "fix_tp15_sl10_t30_d0" in ids
    assert "fix_tp15_sl20_t30_d0" in ids
    assert "fix_tp50_sl15_t30_d0" not in ids
    assert "fix_tp15_sl15_t15_d0" not in ids
    assert fp.REF_RULE not in ids


def test_verdict_sentences():
    blank = "\n".join(fp.verdict_text(False, None, []))
    assert fp.GATE_FAIL in blank
    choice = {
        "id": "base__fix", "hold_mean": -1.0, "hold_n": 40, "hold_days": 20,
        "hold_sessions": 30, "beats": False, "most": False, "survives": False,
    }
    assert fp.NONE_POS in "\n".join(fp.verdict_text(True, choice, [choice]))
    positive = dict(choice, hold_mean=1.5)
    text = "\n".join(fp.verdict_text(True, positive, [positive]))
    assert fp.POS_NOT_RANDOM in text
    assert "UNPROVEN" in "\n".join(fp.verdict_text(True, positive, [positive]))


def test_pine_is_v5_and_marked_unproven_until_a_rule_survives():
    raw = fp.render_pine(None, None, False)
    assert raw.startswith("//@version=5\n")
    assert 'indicator("FG PERFECT UNPROVEN' in raw
    assert "plotshape" in raw
    assert "alertcondition" in raw
    survived = fp.render_pine(None, None, True)
    title = survived.split("indicator(", 1)[1].split(")", 1)[0]
    assert "UNPROVEN" not in title
    assert "alertcondition" in survived


def test_two_minute_bar_does_not_see_the_entry_minute():
    idx = pd.date_range("2026-01-05 09:30", periods=30, freq="1min", tz=NY)
    close = np.full(30, 100.0)
    df = pd.DataFrame({
        "open": close, "high": close + 0.2, "low": close - 0.2, "close": close, "volume": np.full(30, 1000.0),
    }, index=idx)
    # A 2-minute bar starting at 9:34 closes at 9:36. The entry minute is 6.
    # Minute 6 is the entry, so it is not inside the closed bar.
    assert fp.fg.entry_minute_of(4, 2) == 6
    bars = fp.fg.to_tf(df, 2)
    ts = idx[4]
    later = df.copy()
    later.iloc[6, later.columns.get_loc("close")] = 999.0
    assert fp.fg.to_tf(later, 2).loc[ts, "close"] == pytest.approx(bars.loc[ts, "close"])
    fear, _greed = fp.fg.fear_greed(fp.fg.to_tf(df, 2))
    tail = df.copy()
    tail.iloc[-1, tail.columns.get_loc("low")] = 1.0
    fear2, _g = fp.fg.fear_greed(fp.fg.to_tf(tail, 2))
    np.testing.assert_allclose(fear[:-1], fear2[:-1], equal_nan=True)


def _frames(n_days=8):
    days = pd.bdate_range("2026-09-01", periods=n_days)
    frames = {}
    for sym, base in (("SPY", 500.0), ("QQQ", 450.0)):
        parts = []
        for i, day in enumerate(days):
            start = pd.Timestamp(day).tz_localize(NY) + pd.Timedelta(hours=9, minutes=30)
            idx = pd.date_range(start, periods=390, freq="1min")
            close = np.full(390, base)
            close[60:90] = base * (1.01 if i % 2 == 0 else 0.99)
            parts.append(pd.DataFrame({
                "open": close, "high": close + 0.4, "low": close - 0.4,
                "close": close, "volume": np.full(390, 1000.0 + (i * 10)),
            }, index=idx))
        frames[sym] = pd.concat(parts)
    return frames


def test_synth_smoke_writes_the_report_and_says_the_bar_was_not_met(tmp_path, monkeypatch):
    monkeypatch.setenv("FG_SYNTH", "1")
    monkeypatch.setenv("FG_SMOKE", "1")
    monkeypatch.setenv("FG_DAYS", "8")
    monkeypatch.setenv("FG_BOOT", "5")
    monkeypatch.setenv("FG_SHUFFLES", "2")
    monkeypatch.setenv("FG_OUT", str(tmp_path))
    monkeypatch.setenv("FG_SYMBOLS", "SPY,QQQ")
    monkeypatch.delenv("ALPACA_KEY", raising=False)
    monkeypatch.delenv("ALPACA_SECRET", raising=False)
    monkeypatch.setattr(fp.sc, "_load_underlying", lambda *_a, **_k: _frames(8))
    fp.main()
    report = (tmp_path / "FGPERFECT.md").read_text()
    assert report.startswith("# Fear-greed fade PERFECT\n")
    assert "not a market" in report
    assert fp.GATE_FAIL in report
    assert "candidate minimum was not met" in report
    assert "2026-10-19 through 2026-10-23 are not in this run." in report
    assert (tmp_path / "fgperfect_summary.csv").exists()
    assert (tmp_path / "fgperfect_trades.csv").exists()
    assert (tmp_path / "fgperfect_folds.csv").exists()
    pine = (tmp_path / "FGPERFECT.pine").read_text()
    assert pine.startswith("//@version=5\n")
    assert "UNPROVEN" in pine
    summary = (tmp_path / "fgperfect_summary.csv").read_text().strip().splitlines()
    specs, rules = fp.smoke_catalog()
    assert len(summary) == 1 + len(specs) * len(rules)


def test_missing_keys_write_a_report_and_stop(tmp_path, monkeypatch):
    monkeypatch.delenv("ALPACA_KEY", raising=False)
    monkeypatch.delenv("ALPACA_SECRET", raising=False)
    monkeypatch.delenv("FG_SYNTH", raising=False)
    monkeypatch.setenv("FG_OUT", str(tmp_path))
    with pytest.raises(SystemExit, match="ALPACA_KEY"):
        fp.main()
    text = (tmp_path / "FGPERFECT.md").read_text()
    assert "ALPACA_KEY" in text
    assert "No orders" in text


def test_workflow_is_manual_and_cannot_push_main():
    text = open(".github/workflows/fgperfect.yml").read()
    assert text.startswith("name: Fear-greed fade PERFECT (real option prices)\n")
    assert "workflow_dispatch:" in text
    assert "schedule:" not in text
    assert "ALPACA_KEY: ${{ secrets.ALPACA_KEY }}" in text
    assert "ALPACA_SECRET: ${{ secrets.ALPACA_SECRET }}" in text
    assert 'git push origin "HEAD:${BRANCH}"' in text
    assert "Refusing to push results" in text
    assert "main|master" in text
    assert '[[ "$BRANCH" =~ ^[A-Za-z0-9._/-]+$ ]]' in text
    assert 'HEADBR="$(git rev-parse --abbrev-ref HEAD)"' in text
    assert "mkdir -p /tmp/fgperfect-out" in text
    assert "rm -f results/FGPERFECT.md" in text
    assert 'git checkout -B "$BRANCH"' in text
    assert 'default: "fgperfect-results"' in text
    assert 'default: "120"' in text
    assert "python -m pytest -q tests/test_fgperfect.py" in text
    assert "results/FGPERFECT.md" in text
    assert "results/fgperfect_summary.csv" in text
    assert "results/fgperfect_trades.csv" in text
    assert "results/fgperfect_folds.csv" in text
    assert "results/FGPERFECT.pine" in text
    assert "timeout-minutes: 90" in text
    assert "actions/cache/restore@v4" in text
    assert "actions/cache/save@v4" in text
    assert "FG_BOOK_CACHE: .fgperfect-books" in text
    commit_at = text.index("Commit results onto the results branch (never main)")
    assert "if: always()" in text[commit_at:commit_at + 180]
    readme = open("README.md").read()
    assert "Fear-greed fade PERFECT (real option prices)" in readme
    assert "Run workflow" in readme
    assert "Do not tap Re-run" in readme
    assert "fgperfect-results" in readme
    for banned in ("submit_order", "TradingClient", "MarketOrderRequest"):
        assert banned not in text
        assert banned not in open("fgperfect.py").read()


def _zero_cubes(n_specs, n_days, n_rules):
    shape = (n_specs, n_days, n_rules)
    return {
        "sig_sum": np.zeros(shape, np.float32),
        "sig_cnt": np.zeros(shape, np.int32),
        "win_cnt": np.zeros(shape, np.int32),
        "dol_sum": np.zeros(shape, np.float32),
        "rnd_sum": np.zeros(shape, np.float32),
        "rnd_cnt": np.zeros(shape, np.int32),
        "pair_sum": np.zeros(shape, np.float32),
        "tp_cnt": np.zeros(shape, np.int32),
    }


def test_pair_p_lines_up_with_spec_and_rule_not_with_the_day_axis():
    """The failed Actions run indexed q as spec * n_rules + rule.

    Cubes are (spec, day, rule). Unpacking the day axis as if it were the rule
    axis builds a q shorter than that index. Two specs, three days, four rules
    is enough: the last slot is 7, and the old length was specs * days = 6.
    """
    pair = np.zeros((2, 3, 4), dtype=np.float32)
    cnt = np.zeros((2, 3, 4), dtype=np.float32)
    pair[1, 0, 3] = 2.0
    pair[1, 1, 3] = 0.0
    cnt[1, 0, 3] = 1.0
    cnt[1, 1, 3] = 1.0
    p = fp._pair_p(pair, cnt)
    assert p.shape == (2 * 4,)
    assert 1 * 4 + 3 >= 2 * 3
    assert p[1 * 4 + 3] < 1.0
    assert p[0] == 1.0


def test_book_cache_reloads_the_same_slices_and_a_bad_file_is_recomputed(tmp_path):
    cubes = _zero_cubes(4, 3, 5)
    cubes["sig_sum"][0, 1, 2] = np.float32(1.5)
    cubes["sig_cnt"][2, 0, 4] = 7
    indices = [0, 2]
    path = tmp_path / "book.npz"
    fp._save_book(str(path), indices, cubes)
    fresh = _zero_cubes(4, 3, 5)
    assert fp._load_book(str(path), indices, fresh)
    assert fresh["sig_sum"][0, 1, 2] == np.float32(1.5)
    assert int(fresh["sig_cnt"][2, 0, 4]) == 7
    assert fresh["sig_sum"][1, 0, 0] == 0
    path.write_bytes(b"not a numpy archive")
    again = _zero_cubes(4, 3, 5)
    assert fp._load_book(str(path), indices, again) is False
    assert again["sig_sum"][0, 1, 2] == 0
    days_a = ["2024-01-02", "2024-01-03"]
    days_b = ["2024-01-02", "2024-01-04"]
    spec = fp.entry_specs(False)[0]
    token_a = fp._book_token(spec.book_key(), (spec.id,), ("r",), days_a, ("SPY",))
    token_b = fp._book_token(spec.book_key(), (spec.id,), ("r",), days_b, ("SPY",))
    assert token_a != token_b
    assert token_a == fp._book_token(spec.book_key(), (spec.id,), ("r",), days_a, ("SPY",))


def test_full_grid_post_loop_with_nothing_surviving_writes_every_file(tmp_path):
    """Same shape as the Actions run: 48 books, 1008 exits, some books with no fills.

    Twelve sessions cannot clear a 60-day train gate, so every fold has no eligible
    cell and nothing survives. That must still exit 0 and write the report.
    """
    specs = fp.entry_specs(gex=False)
    rules = fp.exit_rules()
    assert len({s.book_key() for s in specs}) == 48
    assert len(rules) == 1008
    n_days = 12
    cubes = _zero_cubes(len(specs), n_days, len(rules))
    ref_i = next(i for i, rule in enumerate(rules) if rule.id == fp.REF_RULE)
    # One book has a few fills, not enough days or fills to be a candidate.
    # The other 47 books stay at zero, including books whose paths never filled.
    cubes["sig_cnt"][0, :3, :] = 1
    cubes["sig_sum"][0, :3, :] = np.float32(0.01)
    cubes["sig_sum"][0, 0, ref_i] = np.float32(0.20)
    cubes["sig_sum"][0, 1, ref_i] = np.float32(-0.05)
    cubes["win_cnt"][0, :3, :] = 1
    cubes["dol_sum"][0, :3, :] = np.float32(0.4)
    cubes["rnd_cnt"][0, :3, :] = 1
    cubes["rnd_sum"][0, :3, :] = np.float32(0.0)
    cubes["pair_sum"][0, :3, :] = np.float32(0.01)
    cubes["pair_sum"][0, 0, ref_i] = np.float32(0.20)
    cubes["pair_sum"][0, 1, ref_i] = np.float32(-0.05)
    cubes["tp_cnt"][0, :3, ref_i] = 1
    score_days = [ts.date() for ts in pd.bdate_range("2024-01-02", periods=n_days)]
    result = fp.score_cubes(
        specs, rules, score_days, ["SPY", "QQQ"],
        n_boot=4, n_shuf=2, synthetic=True, smoke=False,
        ref_i=ref_i, full_family=fp.family_count(False),
        gex_note="GEX was not scored.", vix_source="synthetic",
        **cubes,
    )
    assert result["failures"] == []
    assert fp.study_exit_code(result) == 0
    assert result["choice"] is None
    assert result["meta"]["gate_passed"] is False
    assert len(result["q"]) == len(specs) * len(rules)
    assert len(result["folds"]) == 5
    assert all(row["select_note"] == "candidate minimum was not met" for row in result["folds"])
    assert any(row["cell"] for row in result["folds"])
    fp._finalize_outputs(str(tmp_path), result)
    report = (tmp_path / "FGPERFECT.md").read_text()
    assert report.startswith("# Fear-greed fade PERFECT\n")
    assert fp.GATE_FAIL in report
    assert "not a market" in report
    assert "candidate minimum was not met" in report
    assert "No rule is called a candidate." in report
    pine = (tmp_path / "FGPERFECT.pine").read_text()
    assert pine.startswith("//@version=5\n")
    assert "UNPROVEN" in pine
    summary = (tmp_path / "fgperfect_summary.csv").read_text().strip().splitlines()
    assert len(summary) == 1 + len(specs) * len(rules)
    edelay = [
        line for line in summary
        if line.startswith(f"{fp.BASE_ID}__edelay2__{fp.REF_RULE},")
    ]
    assert len(edelay) == 1
    # id, spec, rule, family, exit_family, full_n
    assert edelay[0].split(",")[5] == "0"
    assert (tmp_path / "fgperfect_trades.csv").exists()
    assert (tmp_path / "fgperfect_folds.csv").exists()


def test_a_failed_stage_keeps_partial_files_and_names_the_stage(tmp_path, monkeypatch, capsys):
    def boom(*_args, **_kwargs):
        raise RuntimeError("marginal boom")

    monkeypatch.setattr(fp, "_marginal_sections", boom)
    specs, rules = fp.smoke_catalog()
    cubes = _zero_cubes(len(specs), 8, len(rules))
    ref_i = next(i for i, rule in enumerate(rules) if rule.id == fp.REF_RULE)
    score_days = [ts.date() for ts in pd.bdate_range("2024-01-02", periods=8)]
    result = fp.score_cubes(
        specs, rules, score_days, ["SPY", "QQQ"],
        n_boot=2, n_shuf=1, synthetic=True, smoke=True, ref_i=ref_i,
        **cubes,
    )
    assert result["failures"]
    assert result["failures"][0][0] == "marginals"
    assert "marginal boom" in result["failures"][0][1]
    assert fp.study_exit_code(result) == 1
    with pytest.raises(SystemExit) as caught:
        fp._finalize_outputs(str(tmp_path), result)
    assert caught.value.code == 1
    captured = capsys.readouterr()
    blob = captured.out + "\n" + captured.err
    assert "STAGE marginals failed: marginal boom" in blob
    assert "Traceback (most recent call last)" in blob
    assert "RuntimeError: marginal boom" in blob
    stage_lines = [line for line in captured.out.splitlines() if line.startswith("STAGE ")]
    assert stage_lines[-1] == "STAGE marginals failed: marginal boom"
    report = (tmp_path / "FGPERFECT.md").read_text()
    assert "STAGE marginals failed: marginal boom" in report
    assert fp.GATE_FAIL in report
    pine = (tmp_path / "FGPERFECT.pine").read_text()
    assert "UNPROVEN" in pine
    assert (tmp_path / "fgperfect_summary.csv").exists()
    assert (tmp_path / "fgperfect_folds.csv").exists()
    assert (tmp_path / "fgperfect_trades.csv").exists()
