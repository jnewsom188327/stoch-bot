"""Offline tests for vfxbot.py (no keys, no network). Run: python -m pytest tests/ -q  (or python tests/test_vfxbot.py)"""
import os
import sys
import tempfile
from datetime import datetime, timezone
from types import SimpleNamespace

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import backtest as B  # noqa: E402
import vfxbot as V    # noqa: E402


def fake3m(sym="SPY"):
    d1, _ = B.fake_1m(sym, datetime(2026, 9, 1, tzinfo=timezone.utc), datetime(2026, 10, 20, tzinfo=timezone.utc))
    return V.bars_3m(d1)


def test_fires_match_edge_main_trigger():
    """trigger 6 of edge_main: (F >= 95) & (pF < 95) [long], same for G [short], window + same-day previous bar"""
    df = fake3m()
    R = V.readings(df)
    F, G = R["F"], R["G"]
    pF, pG = np.r_[np.nan, F[:-1]], np.r_[np.nan, G[:-1]]
    ends = df.index + pd.Timedelta(minutes=3)
    ehm = ends.hour * 100 + ends.minute
    same = np.r_[False, R["dord"][1:] == R["dord"][:-1]]
    ok = same & (R["hm"] >= 930) & (ehm >= 935) & (ehm <= 1445) & np.isfinite(R["a"]) & (R["a"] > 0)
    L = set(np.nonzero((F >= 95) & (pF < 95) & ok)[0])
    S = set(np.nonzero((G >= 95) & (pG < 95) & ok)[0])
    got = V.all_fires(df)
    assert {i for i, sd, *_ in got if sd == 1} == L
    assert {i for i, sd, *_ in got if sd == -1} == S
    assert len(L) + len(S) > 20


def test_no_lookahead():
    """a fire seen on the full history must be seen identically when the data ends at that bar"""
    df = fake3m()
    full = V.all_fires(df)
    rng = np.random.default_rng(0)
    for k in rng.choice(len(full), min(15, len(full)), replace=False):
        i, sd, v, fl, sk = full[k]
        cut = df.iloc[: i + 1]
        R = V.readings(cut)
        f = dict(V.fires_at(cut, R, i))
        assert sd in f and abs(f[sd] - v) < 1e-9
        assert V.flags_at(R, i, sd) == fl


def test_flags_match_edge_bins():
    """flags vs edge_main FEAT bins: TLC==0, VWAP bin 0, WITH==1, ANG bin 0, TCOL==2, CHW bin 2"""
    df = fake3m("QQQ")
    R = V.readings(df)
    sh = lambda x, k: np.r_[np.full(k, np.nan), x[:-k]]
    for sd in (1, -1):
        W = R["G"] if sd == 1 else R["F"]
        mm = R["m"] * sd
        rise = mm > sh(mm, 1)
        ref = np.stack([
            (2 + R["col"] * sd).astype(int) == 0,
            np.digitize(np.nan_to_num((R["c"] - R["vw"]) / R["a"] * sd), [-3, -1, 1, 3]) == 0,
            np.where(R["move"] * sd > 0, 0, 1) == 1,
            np.digitize(R["ang"] * sd, [-15, -5, 5, 15, 23]) == 0,
            np.where(mm >= 0, np.where(rise, 0, 1), np.where(rise, 2, 3)) == 2,
            np.digitize(np.nan_to_num(W - sh(W, 2)), [5, 15, 30]) == 2,
        ], axis=1).astype(int)
        for i in range(300, len(df), 97):
            assert list(V.flags_at(R, i, sd).values()) == list(ref[i]), (sd, i)


class FakeClients:
    """mock Alpaca: every contract quoted bid 2.00 / ask 2.10 at entry, moves with the underlying afterwards"""
    def __init__(self):
        self.spot = 400.0
        self.orders = []

    def get_option_contracts(self, req):
        k0 = round(self.spot)
        typ = str(getattr(req.type, "value", req.type))
        cs = [SimpleNamespace(symbol=f"SPY261020{'C' if 'call' in typ else 'P'}{k:05d}000", strike_price=str(k)) for k in range(k0 - 10, k0 + 11)]
        return SimpleNamespace(option_contracts=cs)

    def get_option_latest_quote(self, req):
        s = req.symbol_or_symbols[0]
        k = int(s[-8:-3])
        intr = max(0.0, (self.spot - k) if "C" in s[9] else (k - self.spot))
        m = max(0.05, intr + 0.5)
        return {s: SimpleNamespace(bid_price=round(m - 0.05, 2), ask_price=round(m + 0.05, 2))}

    def submit_order(self, o):
        self.orders.append(o)
        return SimpleNamespace(id=len(self.orders), status="filled", filled_avg_price=o.limit_price if hasattr(o, "limit_price") else 1.0)

    def get_order_by_id(self, i):
        o = self.orders[i - 1]
        return SimpleNamespace(id=i, status="filled", filled_avg_price=getattr(o, "limit_price", 1.0))

    def cancel_order_by_id(self, i):
        pass

    def get_all_positions(self):
        return []


def test_replay_day_with_mock_broker():
    try:
        import alpaca  # noqa: F401
    except ImportError:
        print("alpaca-py not installed - skipping mock replay")
        return
    df_all = fake3m()
    days = sorted(set(df_all.index.date))
    tmp = tempfile.mkdtemp()
    V.LOG, V.STATE = os.path.join(tmp, "log.csv"), os.path.join(tmp, "state.json")
    fc = FakeClients()
    total_real = 0
    for d in days[-12:]:
        bot = V.Bot(fc, fc, d)
        upto = df_all[df_all.index.date <= d]
        start = np.nonzero(upto.index.date == d)[0]
        for i in start:
            end = upto.index[i] + pd.Timedelta(minutes=3)
            if V.hhmm(end) < 930:
                continue
            if V.hhmm(end) >= 1555:
                break
            cut = upto.iloc[: i + 1]
            fc.spot = float(cut["close"].iloc[-1])
            V.now_et = lambda e=end: e.to_pydatetime()
            bot.on_bar("SPY", cut, V.readings(cut), i, end)
        bot.flat_all()
        assert not bot.open
    log = pd.read_csv(V.LOG)
    real = log[log.arm == "REAL"]
    total_real = len(real)
    assert total_real > 0
    assert (real.exit_reason.isin(["LINE COLOR", "FLAT 15:55"])).all()
    # P&L booked from quotes: net = (bid_out - c) / (ask_in + c) - 1, c = 0.0065
    c = 0.0065
    exp = ((real.bid_out - c) - (real.ask_in + c)) / (real.ask_in + c) * 100
    assert np.allclose(real.net_pct, exp, atol=1e-2)
    assert (real.skip == 0).all()
    assert set(log.arm) <= {"REAL", "CONTROL", "SKIPPED", "IGNORED", "NOFILL"}
    ctrl = log[log.arm == "CONTROL"]
    assert len(ctrl) > 0 and set(ctrl.fire_id) <= set(real.fire_id)
    # control drawn from the same 30-min bucket and side as its fire
    for r in ctrl.itertuples():
        f = real[real.fire_id == r.fire_id].iloc[0]
        tf_, tc_ = pd.Timestamp(f.signal_bar), pd.Timestamp(r.signal_bar)
        assert (tf_.hour * 60 + tf_.minute) // 30 == (tc_.hour * 60 + tc_.minute) // 30
        assert f.side == r.side and tc_.date() > tf_.date()
    print(f"replay ok: {total_real} real, {len(ctrl)} control, rows {log.arm.value_counts().to_dict()}")
    import vfx_report
    print(vfx_report.report(log))


if __name__ == "__main__":
    for nm, fn in list(globals().items()):
        if nm.startswith("test_"):
            fn()
            print("PASS", nm)
