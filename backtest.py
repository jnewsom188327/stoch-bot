"""
TREND LINE STUDY (MODE=study, the default) - line anatomy, 4 entry events (+ faded) on 1/2/3/5m, ~30 conditions
  (TTM squeeze, Vix Fix levels, every timeframe's agreement, price action), confluence picked on 2020-23 and checked on
  2024-now, and exits (time, color, warning, TTM peak/zero, bracket, trailing, hold).
TREND FLIP STOPS & TARGETS (MODE=brackets) - every target/stop combination (+1/-1 ... +3/-1, wide stops,
  no stop) for v3.0 and the leads (higher-timeframe agreement, gap and go, yesterday's breakout), vs a coin flip.
TREND FLIP EXPLORE (MODE=explore) - timeframes 1/2/3/5/15m x line settings, faded flips, which
  timeframes should agree, and other setups (ORB, VWAP reclaim, yesterday's high/low, gap fade), graded entry-only
  against a coin-flip luck line built from real data.
TREND FLIP ENTRY QUALITY (MODE=quality) - grades only the entry, for trading the exit by hand:
  every combination of quiet days / entry window / Vix Fix / 15m filter / VWAP rule, TRAIN 2020-23 vs TEST 2024-now.
TREND FLIP OPTIMIZER + MONTE CARLO (MODE=optimize) - see the OPTIMIZER section at the bottom.
  Every entry and exit idea, on top of the quiet-day filter, picked on 2020-2023 only and checked on 2024-now,
  then a Monte Carlo of the final setup in option dollars (Black-Scholes estimate, 1DTE and 0DTE).
TREND FLIP QUIET-DAY FILTER + MARKET-CONDITIONS STUDY (+ v3.0 / v4.0 backtest) - years of 2/3-minute bars from Alpaca.
DATA ONLY: it never places an order.
MODE=regime: for every v3.0 trade, measure the market conditions at the signal candle, split each
  condition into thirds using 2020-2023 ONLY (TRAIN), pick rules on TRAIN, then check them on 2024-2026 (TEST),
  data the rules never saw. A rule is only real if it also helps on TEST.
MODE=compare: the earlier v3.0 vs v4.0 comparison.
MODE=quiet: v3.0 + "quiet day" filter = only trade when YESTERDAY's regular-hours range was below
  X times the daily ATR(14). Same rule on every chart, several X values, TRAIN / TEST / year by year.
Runs in GitHub Actions. Keys come from GitHub Secrets ALPACA_KEY / ALPACA_SECRET (never in this file).

Same rules as the TradingView indicator Trend Flip v3.0:
  LINE  : EMA 13 > EMA 34 and close > VWAP = GREEN | the opposite = RED | anything else = GRAY
  ENTRY : the line turns GREEN (long) / RED (short) on a candle close between 9:35 and 15:30 ET,
          and a Vix Fix FEAR spike (longs) / GREED spike (shorts) happened in the last 10 candles.
          No spike yet? Wait up to 5 candles for one while the line keeps its color.
          Filled at the NEXT candle's open.
  EXIT  : 2 ATR stop (checked first, worst case) | opposite color flip | close of candle 15 | flat at 15:55
          (also flat at the end of a short day).
v4.0 ideas tested against v3.0 (same code as the TradingView LAB box):
  ENTRY + 15m agrees / + 15m and 60m agree (trend of the last CLOSED higher-timeframe candle)
  EXIT  ride strong trend (keep holding after candle 15 until the warning color) / ride if 15m agrees /
        cut losers on warning (from candle 3, losing + warning color) / ride + cut
  Warning color = price closed back through the fast line while it is rolling over, 2 candles in a row.
Results: printed in the run log, shown on the run's Summary page, and saved in the results/ folder.
"""
import os
import sys
import time
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd

NY = ZoneInfo("America/New_York")
SYMBOLS = [s.strip().upper() for s in os.getenv("SYMBOLS", "SPY,QQQ").split(",") if s.strip()]
START = os.getenv("START", "2020-01-01").strip() or "2020-01-01"
DELTA = 0.6          # option delta for the rough $ estimate
TFS = [int(x) for x in os.getenv("TFS", "2,3").split(",") if x.strip()]
MODE = os.getenv("MODE", "study").strip().lower() or "study"
SPLIT = os.getenv("SPLIT", "2024-01-01")   # TRAIN = before this date, TEST = from this date
OUT = "results"

# v3.0 settings
V30 = dict(fast=13, slow=34, use_vwap=True, vf_on=True, vf_look=10, wait=5,
           hold=15, stop=2.0, t_start=935, t_end=1530, flat_at=1555, direction=0,
           htf=0, xm=0, weak_n=2, max_hold=60, cut_after=3, htf1=15, htf2=60)


# ---------------------------------------------------------------- data
def fetch_1m(symbol, start, end):
    """1-minute bars 4:00-20:00 ET from Alpaca (SIP first, IEX if the plan does not allow SIP)."""
    from alpaca.data.enums import Adjustment, DataFeed
    from alpaca.data.historical import StockHistoricalDataClient
    from alpaca.data.requests import StockBarsRequest
    from alpaca.data.timeframe import TimeFrame

    key, sec = os.getenv("ALPACA_KEY", "").strip(), os.getenv("ALPACA_SECRET", "").strip()
    if not key or not sec:
        sys.exit("ALPACA_KEY / ALPACA_SECRET are missing. Add them in Settings > Secrets and variables > Actions.")
    client = StockHistoricalDataClient(key, sec)
    last_err = None
    for feed in (DataFeed.SIP, DataFeed.IEX):
        try:
            parts = []
            cur = start
            while cur < end:
                nxt = min(cur + timedelta(days=120), end)
                req = StockBarsRequest(symbol_or_symbols=symbol, timeframe=TimeFrame.Minute,
                                       start=cur, end=nxt, feed=feed, adjustment=Adjustment.SPLIT)
                df = client.get_stock_bars(req).df
                if len(df):
                    parts.append(df)
                print(f"  {symbol} {feed.value}: {cur:%Y-%m-%d} -> {nxt:%Y-%m-%d}  {len(df):,} bars", flush=True)
                cur = nxt
            if not parts:
                raise RuntimeError("no bars returned")
            df = pd.concat(parts)
            if isinstance(df.index, pd.MultiIndex):
                df = df.reset_index(level=0, drop=True)
            df = df[~df.index.duplicated()].sort_index()
            df.index = df.index.tz_convert(NY)
            return df[["open", "high", "low", "close", "volume"]].astype(float), feed.value
        except Exception as e:  # noqa: BLE001
            last_err = e
            msg = str(e)
            print(f"  {symbol}: feed {feed.value} failed: {msg[:300]}", flush=True)
            if "401" in msg or "unauthorized" in msg.lower():
                break  # bad keys - the other feed will fail the same way
    sys.exit(f"Could not download {symbol}: {last_err}\n"
             "If it says 401 / unauthorized / forbidden: the API keys in GitHub Secrets are wrong or expired. "
             "Make new PAPER keys in Alpaca and paste them into ALPACA_KEY and ALPACA_SECRET again.")


def fake_1m(symbol, start, end):
    """Random-walk data so the program can be tested without keys (TEST=1)."""
    rng = np.random.default_rng(7 if symbol == "SPY" else 11)
    days = pd.bdate_range(start.date(), end.date()).tz_localize(NY)
    idx = []
    for d in days:
        idx.append(pd.date_range(d + pd.Timedelta(hours=4), d + pd.Timedelta(hours=19, minutes=59), freq="1min"))
    idx = idx[0].append(idx[1:]) if len(idx) > 1 else idx[0]
    ret = rng.normal(0, 0.0004, len(idx))
    close = 400 * np.exp(np.cumsum(ret))
    open_ = np.r_[close[0], close[:-1]]
    hi = np.maximum(open_, close) * (1 + np.abs(rng.normal(0, 0.0002, len(idx))))
    lo = np.minimum(open_, close) * (1 - np.abs(rng.normal(0, 0.0002, len(idx))))
    vol = rng.integers(100, 5000, len(idx)).astype(float)
    return pd.DataFrame({"open": open_, "high": hi, "low": lo, "close": close, "volume": vol}, index=idx), "fake"


def to_tf(df1, rth_only, mins=3):
    hm = df1.index.hour * 100 + df1.index.minute
    df1 = df1[(hm >= 930) & (hm < 1600)] if rth_only else df1[(hm >= 400) & (hm < 2000)]
    g = df1.groupby(df1.index.floor(f"{mins}min"))
    out = pd.DataFrame({"open": g["open"].first(), "high": g["high"].max(), "low": g["low"].min(),
                        "close": g["close"].last(), "volume": g["volume"].sum()})
    return out.dropna()


# ---------------------------------------------------------------- indicators (TradingView math)
def htf_state(df, fast, slow, mins):
    """Trend (+1 / -1) of the last CLOSED higher-timeframe candle, known at each chart bar's start
    (matches TradingView request.security(..., f()[1], lookahead_on))."""
    c = df["close"].groupby(df.index.floor(f"{mins}min")).last()
    s = np.where(c.ewm(span=fast, adjust=False).mean() > c.ewm(span=slow, adjust=False).mean(), 1, -1)
    hs = pd.DataFrame({"end": c.index + pd.Timedelta(minutes=mins), "s": s})
    bars = pd.DataFrame({"t": df.index})
    m = pd.merge_asof(bars, hs, left_on="t", right_on="end", direction="backward")
    return m["s"].fillna(0).astype(int).to_numpy()


def indicators(df, fast, slow, use_vwap, weak_n=2, htf1=15, htf2=60):
    o, h, l, c, v = (df[k] for k in ("open", "high", "low", "close", "volume"))
    pc = c.shift(1)
    tr = pd.concat([h - l, (h - pc).abs(), (l - pc).abs()], axis=1).max(axis=1)
    tr.iloc[0] = h.iloc[0] - l.iloc[0]
    atr = tr.ewm(alpha=1 / 14, adjust=False).mean()                 # ta.atr = RMA of true range
    ef = c.ewm(span=fast, adjust=False).mean()
    es = c.ewm(span=slow, adjust=False).mean()
    day = df.index.date
    hlc3 = (h + l + c) / 3
    pv = (hlc3 * v).groupby(day).cumsum()
    vv = v.groupby(day).cumsum()
    vwap = (pv / vv.replace(0, np.nan)).ffill()                      # ta.vwap, resets every day
    up = (ef > es) & (c > vwap) if use_vwap else (ef > es)
    dn = (ef < es) & (c < vwap) if use_vwap else (ef < es)
    st = np.where(up, 1, np.where(dn, -1, 0))
    # CM Williams Vix Fix (fear) + mirror (greed): 22 lookback, BB 20 / 2, range 50 at 0.85
    hc22, lc22 = c.rolling(22).max(), c.rolling(22).min()
    wvf = (hc22 - l) / hc22 * 100
    wvi = (h - lc22) / lc22 * 100

    def spike(w):
        mid, sd = w.rolling(20).mean(), w.rolling(20).std(ddof=0)
        return ((w >= mid + 2 * sd) | (w >= w.rolling(50).max() * 0.85)).fillna(False).to_numpy()

    hm = (df.index.hour * 100 + df.index.minute).to_numpy()
    # warning color: close back through the fast line while it rolls over, weak_n candles in a row
    fl_raw = ((c < ef) & (ef < ef.shift(1))).astype(int)
    fs_raw = ((c > ef) & (ef > ef.shift(1))).astype(int)
    fadeL = (fl_raw.rolling(weak_n).sum() == weak_n).to_numpy()
    fadeS = (fs_raw.rolling(weak_n).sum() == weak_n).to_numpy()
    strongL = (st == 1) & ~fadeL
    strongS = (st == -1) & ~fadeS
    return dict(o=o.to_numpy(), h=h.to_numpy(), l=l.to_numpy(), c=c.to_numpy(), atr=atr.to_numpy(),
                st=st, fear=spike(wvf), greed=spike(wvi), hm=hm, day=np.array(day),
                strongL=strongL, strongS=strongS, vwap=vwap.to_numpy(),
                h1=htf_state(df, fast, slow, htf1), h2=htf_state(df, fast, slow, htf2))


def bars_since(flag):
    flag = np.asarray(flag, dtype=bool)
    idx = np.where(flag, np.arange(len(flag)), -1)
    last = np.maximum.accumulate(idx) if len(idx) else idx
    return np.where(last >= 0, np.arange(len(flag)) - last, 999).astype(np.int64)


def signals(ind, p):
    st, hm = ind["st"], ind["hm"]
    inT = (hm >= p["t_start"]) & (hm < p["t_end"])
    prev = np.r_[0, st[:-1]]
    sig = np.where(inT & (st != 0) & (st != prev), st, 0)
    if p["vf_on"]:
        okL = bars_since(ind["fear"]) <= p["vf_look"]
        okS = bars_since(ind["greed"]) <= p["vf_look"]
    else:
        okL = okS = np.ones(len(st), dtype=bool)
    if p.get("allowL") is not None:
        okL = okL & p["allowL"]
        okS = okS & p["allowS"]
    if p["htf"] >= 1:
        okL = okL & (ind["h1"] == 1)
        okS = okS & (ind["h1"] == -1)
    if p["htf"] >= 2:
        okL = okL & (ind["h2"] == 1)
        okS = okS & (ind["h2"] == -1)
    ent = np.zeros(len(st), dtype=np.int64)
    arm, armB = 0, 0
    for i in range(len(st)):
        if sig[i] != 0:
            arm, armB = sig[i], 0
        elif arm != 0:
            armB += 1
        if arm != 0 and (st[i] != arm or armB > p["wait"] or not inT[i]):
            arm = 0
        if arm != 0 and (okL[i] if arm == 1 else okS[i]):
            ent[i] = arm
            arm = 0
    return sig, ent


# ---------------------------------------------------------------- trade simulator (same order as Pine)
def simulate(ind, sig, ent, p, times):
    o, h, l, c, atr, hm, day = ind["o"], ind["h"], ind["l"], ind["c"], ind["atr"], ind["hm"], ind["day"]
    sL, sS, h1 = ind["strongL"], ind["strongS"], ind["h1"]
    xm = p["xm"]
    n = len(o)
    trades = []
    side = pend = 0
    en = ea = stp = 0.0
    eb = 0
    best = worst = 0.0
    ft = 0
    for i in range(n):
        if pend != 0 and side == 0:
            side, en = pend, o[i]
            ea = atr[i - 1] if i > 0 and not np.isnan(atr[i - 1]) else atr[i]
            stp = en - side * p["stop"] * ea
            eb, best, worst, ft = i, 0.0, 0.0, 0
        pend = 0
        if side != 0:
            sd = side
            held = i - eb + 1
            fav = (h[i] - en) if sd == 1 else (en - l[i])
            adv = (en - l[i]) if sd == 1 else (h[i] - en)
            if ft == 0:
                ft = -1 if adv >= ea else (1 if fav >= ea else 0)
            best, worst = max(best, fav), max(worst, adv)
            code, px = 0, 0.0
            last_of_day = i + 1 >= n or day[i + 1] != day[i]
            weak = (not sL[i]) if sd == 1 else (not sS[i])
            agr = h1[i] == sd
            if (l[i] <= stp) if sd == 1 else (h[i] >= stp):
                code, px = 1, (min(o[i], stp) if sd == 1 else max(o[i], stp))
            elif sig[i] == -sd:
                code, px = 5, c[i]
            elif hm[i] >= p["flat_at"] or last_of_day:
                code, px = 6, c[i]
            elif xm in (3, 4) and p["cut_after"] <= held < p["hold"] and weak and sd * (c[i] - en) < 0:
                code, px = 9, c[i]
            elif held >= p["hold"]:
                ride = (not weak) if xm in (1, 4) else ((not weak) and agr) if xm == 2 else False
                if not ride:
                    code, px = (7 if held > p["hold"] else 2), c[i]
                elif held >= p["max_hold"]:
                    code, px = 2, c[i]
            if code:
                pts = sd * (px - en)
                trades.append((times[eb], sd, en, px, code, pts, pts / ea, held, best / ea, worst / ea, ft, eb, i))
                side = 0
        if ent[i] != 0 and side == 0 and (p["direction"] == 0 or ent[i] == p["direction"]):
            pend = ent[i]
    cols = ["entry_time", "side", "entry", "exit", "code", "pts", "r", "held", "best_r", "worst_r", "first", "ib", "ix"]
    return pd.DataFrame(trades, columns=cols)


_IND = {}


def run(df3, **over):
    p = dict(V30, **over)
    key = (id(df3), p["fast"], p["slow"], p["use_vwap"], p["weak_n"], p["htf1"], p["htf2"])
    p.setdefault("allowL", None)
    if key not in _IND:
        _IND[key] = indicators(df3, p["fast"], p["slow"], p["use_vwap"], p["weak_n"], p["htf1"], p["htf2"])
    ind = _IND[key]
    sig, ent = signals(ind, p)
    return simulate(ind, sig, ent, p, df3.index)


# ---------------------------------------------------------------- stats
def stats(t):
    if len(t) == 0:
        return dict(n=0)
    r = t["r"].to_numpy()
    gw, gl = r[r > 0].sum(), -r[r < 0].sum()
    cum = np.cumsum(r)
    dd = (np.maximum.accumulate(np.r_[0, cum])[1:] - cum).max()
    streak = best_streak = 0
    for x in r:
        streak = streak + 1 if x <= 0 else 0
        best_streak = max(best_streak, streak)
    half = len(r) // 2
    first = t["first"].to_numpy()
    dec = (first != 0).sum()
    days = t["entry_time"].dt.date.nunique()
    return dict(n=len(t), win=100 * (r > 0).mean(), avg=r.mean(), pf=gw / gl if gl > 0 else float("inf"),
                total=r.sum(), usd=t["pts"].mean() * DELTA * 100, dd=dd, streak=best_streak,
                h1=r[:half].mean() if half else float("nan"), h2=r[half:].mean() if half else float("nan"),
                plus1=100 * (first == 1).sum() / dec if dec else float("nan"),
                best=t["best_r"].mean(), worst=t["worst_r"].mean(), per_day=len(t) / max(days, 1))


def fmt_row(name, s):
    if s.get("n", 0) == 0:
        return f"| {name} | 0 | - | - | - | - | - | - |"
    return (f"| {name} | {s['n']} | {s['win']:.0f}% | **{s['avg']:+.2f}** | {s['pf']:.2f} | {s['total']:+.0f} | "
            f"{s['dd']:.1f} | {s['streak']} |")


HEAD = ("| Test | Trades | Win | ATR / trade | PF | Total ATR | Worst drawdown (ATR) | Longest losing run |\n"
        "|---|---|---|---|---|---|---|---|")


# ---------------------------------------------------------------- main
def main():
    if MODE == "regime":
        return regime_main()
    if MODE == "quiet":
        return quiet_main()
    if MODE == "optimize":
        return optimize_main()
    if MODE == "quality":
        return quality_main()
    if MODE == "explore":
        return explore_main()
    if MODE == "brackets":
        return brackets_main()
    if MODE == "study":
        return study_main()
    test = os.getenv("TEST", "") == "1"
    end = datetime.now(timezone.utc) - timedelta(days=1)
    start = datetime.fromisoformat(START).replace(tzinfo=timezone.utc)
    os.makedirs(OUT, exist_ok=True)
    md = [f"# Trend Flip v3.0 / v4.0 backtest - {datetime.now(NY):%Y-%m-%d %H:%M} ET",
          f"Data: {START} to {end:%Y-%m-%d}, {'/'.join(str(t) for t in TFS)}-minute candles. ATR / trade = average result per trade in ATR "
          f"(the same number as the TradingView box). Healthy = above +0.30 with PF above 1.3.", ""]
    for sym in SYMBOLS:
        print(f"\n=== {sym} ===", flush=True)
        df1, feed = fake_1m(sym, start, end) if test else fetch_1m(sym, start, end)
        for tf in TFS:
            ext = to_tf(df1, rth_only=False, mins=tf)
            print(f"  {tf}m: {len(ext):,} bars (with pre/post market), feed {feed}", flush=True)
            main_t = run(ext)
            main_t.assign(entry_time=main_t["entry_time"].dt.strftime("%Y-%m-%d %H:%M")).to_csv(
                f"{OUT}/trades_{sym}_{tf}m_v30.csv", index=False)
            s = stats(main_t)
            md += [f"## {sym} {tf}-minute  ({feed} data, {ext.index[0]:%Y-%m-%d} to {ext.index[-1]:%Y-%m-%d})", "",
                   "### v4.0 ideas vs v3.0 (one change at a time)", HEAD,
                   fmt_row("**v3.0 (your settings)**", s)]
            tests = [("ENTRY + 15m agrees", dict(htf=1)),
                     ("ENTRY + 15m and 60m agree", dict(htf=2)),
                     ("EXIT ride strong trend", dict(xm=1)),
                     ("EXIT ride if 15m agrees", dict(xm=2)),
                     ("EXIT cut losers on warning", dict(xm=3)),
                     ("EXIT ride + cut losers", dict(xm=4)),
                     ("15m agrees + ride + cut", dict(htf=1, xm=4)),
                     ("no Vix Fix filter", dict(vf_on=False)),
                     ("Vix Fix spike within 5", dict(vf_look=5)),
                     ("Vix Fix spike within 20", dict(vf_look=20)),
                     ("hold 10 candles", dict(hold=10)),
                     ("hold 25 candles", dict(hold=25)),
                     ("stop 1.5 ATR", dict(stop=1.5)),
                     ("stop 3 ATR", dict(stop=3.0))]
            for name, over in tests:
                print(f"    running: {name}", flush=True)
                md.append(fmt_row(name, stats(run(ext, **over))))
            md.append("")
            L, S = main_t[main_t["side"] == 1], main_t[main_t["side"] == -1]
            sl, ss = stats(L), stats(S)
            md += ["### v3.0 details",
                   f"- Longs: {sl.get('n', 0)} trades, {sl.get('avg', float('nan')):+.2f} ATR | "
                   f"Shorts: {ss.get('n', 0)} trades, {ss.get('avg', float('nan')):+.2f} ATR",
                   f"- 1st half {s.get('h1', float('nan')):+.2f} | 2nd half {s.get('h2', float('nan')):+.2f} ATR per trade",
                   f"- Went +1 ATR your way before -1 ATR against: {s.get('plus1', float('nan')):.0f}% "
                   f"| avg best +{s.get('best', 0):.1f} / avg worst -{s.get('worst', 0):.1f} ATR",
                   f"- {s.get('per_day', 0):.1f} trades per trading day | rough $ per option per trade "
                   f"(0.6 delta, before theta + spread): ${s.get('usd', 0):+.0f}", "",
                   "### v3.0 by year", "| Year | Trades | Win | ATR / trade | PF | Total ATR |", "|---|---|---|---|---|---|"]
            for yr, g in main_t.groupby(main_t["entry_time"].dt.year):
                y = stats(g)
                md.append(f"| {yr} | {y['n']} | {y['win']:.0f}% | **{y['avg']:+.2f}** | {y['pf']:.2f} | {y['total']:+.0f} |")
            md.append("")
            _IND.clear()

    text = "\n".join(md)
    print("\n" + text)
    stamp = datetime.now(NY).strftime("%Y-%m-%d")
    for path in (f"{OUT}/backtest_{stamp}.md", f"{OUT}/latest.md"):
        with open(path, "w") as f:
            f.write(text + "\n")
    summ = os.getenv("GITHUB_STEP_SUMMARY")
    if summ:
        with open(summ, "a") as f:
            f.write(text + "\n")


# ================================================================ MARKET-CONDITIONS STUDY
# Each condition is measured on the SIGNAL candle (the candle before the entry) using only data known then.
# "aligned" conditions are multiplied by the trade side, so + means "in the direction of my trade".
FEATS = [
    # key, label, aligned?
    ("trend", "Daily trend: yesterday's close vs its 20-day average (ATR, + = with my trade)", True),
    ("gap", "Today's opening gap (daily ATR, + = gap in my trade's direction)", True),
    ("daymove", "Move since today's 9:30 open (daily ATR, + = day already moving my way)", True),
    ("vwap", "Distance from VWAP at the signal (3m ATR, + = stretched my way)", True),
    ("vol", "Volatility level: daily ATR as % of price", False),
    ("yrange", "Yesterday's range vs normal (1 = normal day)", False),
    ("dayrange", "Today's range so far vs normal", False),
    ("ivol", "3-minute ATR now vs its 20-day normal", False),
    ("tod", "Time of day", False),
]
TOD_EDGES = [1030, 1200, 1400]
TOD_NAMES = ["9:35-10:30", "10:30-12:00", "12:00-14:00", "14:00-15:30"]


def regime_features(df1, df, ind):
    """Raw (side-free) feature arrays aligned to the chart bars of df."""
    hm1 = df1.index.hour * 100 + df1.index.minute
    rth = df1[(hm1 >= 930) & (hm1 < 1600)]
    g = rth.groupby(rth.index.date)
    d = pd.DataFrame({"o": g["open"].first(), "h": g["high"].max(), "l": g["low"].min(), "c": g["close"].last()})
    pc = d["c"].shift(1)
    tr = pd.concat([d["h"] - d["l"], (d["h"] - pc).abs(), (d["l"] - pc).abs()], axis=1).max(axis=1)
    atrd = tr.ewm(alpha=1 / 14, adjust=False).mean()
    sma20 = d["c"].rolling(20).mean()
    known = pd.DataFrame({                       # everything here is known before today's open
        "pc": pc, "atr": atrd.shift(1), "sma": sma20.shift(1), "prange": (d["h"] - d["l"]).shift(1),
        "dopen": d["o"]})
    day = pd.Index(df.index.date)
    k = known.reindex(day)
    c, h, l = ind["c"], ind["h"], ind["l"]
    hm = ind["hm"]
    inrth = (hm >= 930) & (hm < 1600)
    # today's range so far (RTH only)
    hh = pd.Series(np.where(inrth, h, np.nan), index=df.index).groupby(day).cummax().to_numpy()
    ll = pd.Series(np.where(inrth, l, np.nan), index=df.index).groupby(day).cummin().to_numpy()
    atr_d = k["atr"].to_numpy()
    a3 = ind["atr"]
    a3norm = pd.Series(a3).ewm(span=20 * 130, adjust=False).mean().shift(1).to_numpy()
    vw = ind["vwap"]
    tod = np.digitize(hm, TOD_EDGES).astype(float)
    return {
        "trend": (k["pc"].to_numpy() - k["sma"].to_numpy()) / atr_d,
        "gap": (k["dopen"].to_numpy() - k["pc"].to_numpy()) / atr_d,
        "daymove": np.where(inrth, (c - k["dopen"].to_numpy()) / atr_d, np.nan),
        "vwap": (c - vw) / a3,
        "vol": atr_d / k["pc"].to_numpy() * 100,
        "yrange": k["prange"].to_numpy() / atr_d,
        "dayrange": (hh - ll) / atr_d,
        "ivol": a3 / a3norm,
        "tod": tod,
    }


def trade_feats(t, F):
    sb = (t["ib"].to_numpy() - 1).clip(0)
    side = t["side"].to_numpy()
    out = {}
    for key, _, aligned in FEATS:
        v = F[key][sb]
        out[key] = v * side if aligned else v
    return pd.DataFrame(out, index=t.index)


def bucket(v, cuts, key):
    if key == "tod":
        return v.astype(int)
    b = np.digitize(v, cuts)
    return np.where(np.isnan(v), -1, b)


def avg(r):
    return r.mean() if len(r) else float("nan")


def regime_one(sym, tf, df1, df):
    md = []
    base = run(df)
    ind = _IND[next(iter(_IND))]
    F = regime_features(df1, df, ind)
    tf_ = trade_feats(base, F)
    t = pd.concat([base, tf_], axis=1)
    test_mask = t["entry_time"] >= pd.Timestamp(SPLIT, tz=NY)
    tr, te = t[~test_mask], t[test_mask]
    md += [f"## {sym} {tf}-minute",
           f"TRAIN 2020-{int(SPLIT[:4]) - 1}: {len(tr)} trades, **{avg(tr['r']):+.3f}** ATR/trade | "
           f"TEST {SPLIT[:4]}-now: {len(te)} trades, **{avg(te['r']):+.3f}** ATR/trade "
           f"(thirds hold ~{len(tr) // 3} trades each: differences under about 0.10 are noise)", ""]
    md += ["### Each condition split into thirds (cut points from TRAIN only)",
           "| Condition | Third | TRAIN n | TRAIN ATR | TEST n | TEST ATR |", "|---|---|---|---|---|---|"]
    rules = []
    for key, label, aligned in FEATS:
        if key == "tod":
            cuts, names = None, TOD_NAMES
        else:
            cuts = np.nanquantile(tr[key], [1 / 3, 2 / 3])
            names = [f"low (< {cuts[0]:.2f})", f"mid", f"high (> {cuts[1]:.2f})"]
        btr, bte = bucket(tr[key].to_numpy(), cuts, key), bucket(te[key].to_numpy(), cuts, key)
        avgs = []
        for i, nm in enumerate(names):
            a_tr, a_te = tr["r"][btr == i], te["r"][bte == i]
            avgs.append(avg(a_tr))
            md.append(f"| {label if i == 0 else ''} | {nm} | {len(a_tr)} | {avg(a_tr):+.2f} | {len(a_te)} | {avg(a_te):+.2f} |")
        worst = int(np.nanargmin(avgs))
        best = int(np.nanargmax(avgs))
        keep = [i for i in range(len(names)) if i != worst]
        k_tr, k_te = tr["r"][np.isin(btr, keep)], te["r"][np.isin(bte, keep)]
        o_tr, o_te = tr["r"][btr == best], te["r"][bte == best]
        rules.append(dict(key=key, label=label, cuts=cuts, aligned=aligned, worst=worst, best=best, names=names,
                          skip_tr=avg(k_tr), skip_te=avg(k_te), n_skip_te=len(k_te),
                          only_tr=avg(o_tr), only_te=avg(o_te), n_only_te=len(o_te)))
    md.append("")
    md += ["### Rules picked on TRAIN, checked on TEST",
           f"Baseline v3.0: TRAIN {avg(tr['r']):+.3f} | TEST {avg(te['r']):+.3f}. ✅ = helps on BOTH TRAIN and TEST.",
           "| Rule | TRAIN ATR | TEST ATR | TEST trades | |", "|---|---|---|---|---|"]
    btr0, bte0 = avg(tr["r"]), avg(te["r"])
    for r in sorted(rules, key=lambda x: -x["skip_tr"]):
        ok = r["skip_tr"] > btr0 and r["skip_te"] > bte0
        md.append(f"| skip {r['names'][r['worst']]} - {r['key']} | {r['skip_tr']:+.3f} | {r['skip_te']:+.3f} | {r['n_skip_te']} | {'✅' if ok else ''} |")
    for r in sorted(rules, key=lambda x: -x["only_tr"]):
        ok = r["only_tr"] > btr0 and r["only_te"] > bte0
        md.append(f"| ONLY {r['names'][r['best']]} - {r['key']} | {r['only_tr']:+.3f} | {r['only_te']:+.3f} | {r['n_only_te']} | {'✅' if ok else ''} |")
    md.append("")

    # combined rule: the 2 best "skip worst third" rules on TRAIN, re-simulated candle by candle
    top = sorted(rules, key=lambda x: -x["skip_tr"])[:2]

    def allow(side):
        ok = np.ones(len(df), dtype=bool)
        for r in top:
            v = F[r["key"]] * side if r["aligned"] else F[r["key"]]
            b = bucket(v, r["cuts"], r["key"])
            ok &= (b != r["worst"]) & (b >= 0)
        return ok
    comb = run(df, allowL=allow(1), allowS=allow(-1))
    cm = comb["entry_time"] >= pd.Timestamp(SPLIT, tz=NY)
    desc = " AND ".join(f"skip {r['names'][r['worst']]} {r['key']}" for r in top)
    s_tr, s_te, s_all = stats(comb[~cm]), stats(comb[cm]), stats(comb)
    b_tr, b_te = stats(base[~test_mask]), stats(base[test_mask])
    md += [f"### Best 2 rules combined (picked on TRAIN, full candle-by-candle re-run): {desc}", HEAD,
           fmt_row("v3.0 TRAIN", b_tr), fmt_row("**combined TRAIN**", s_tr),
           fmt_row("v3.0 TEST (never seen)", b_te), fmt_row("**combined TEST (never seen)**", s_te), "",
           "| Year | Trades | ATR / trade (combined) | ATR / trade (v3.0) |", "|---|---|---|---|"]
    for yr in sorted(set(base["entry_time"].dt.year)):
        c_ = comb[comb["entry_time"].dt.year == yr]
        b_ = base[base["entry_time"].dt.year == yr]
        md.append(f"| {yr} | {len(c_)} | **{avg(c_['r']):+.2f}** | {avg(b_['r']):+.2f} |")
    md.append("")
    t.assign(entry_time=t["entry_time"].dt.strftime("%Y-%m-%d %H:%M")).to_csv(
        f"{OUT}/regime_trades_{sym}_{tf}m.csv", index=False)
    return md


def regime_main():
    end = datetime.now(timezone.utc) - timedelta(days=1)
    start = datetime.fromisoformat(START).replace(tzinfo=timezone.utc)
    test = os.getenv("TEST", "") == "1"
    os.makedirs(OUT, exist_ok=True)
    md = [f"# Trend Flip market-conditions study - {datetime.now(NY):%Y-%m-%d %H:%M} ET",
          f"v3.0 rules. TRAIN = {START[:4]} to {int(SPLIT[:4]) - 1} (rules are picked here). "
          f"TEST = {SPLIT[:4]} to now (never used to pick anything). ATR / trade like the TradingView box.", ""]
    for sym in SYMBOLS:
        print(f"\n=== {sym} ===", flush=True)
        df1, feed = fake_1m(sym, start, end) if test else fetch_1m(sym, start, end)
        for tf in TFS:
            print(f"  {tf}m ...", flush=True)
            df = to_tf(df1, rth_only=False, mins=tf)
            _IND.clear()
            md += regime_one(sym, tf, df1, df)
            _IND.clear()
    text = "\n".join(md)
    print("\n" + text)
    stamp = datetime.now(NY).strftime("%Y-%m-%d")
    for path in (f"{OUT}/regime_{stamp}.md", f"{OUT}/regime_latest.md"):
        with open(path, "w") as f:
            f.write(text + "\n")
    summ = os.getenv("GITHUB_STEP_SUMMARY")
    if summ:
        with open(summ, "a") as f:
            f.write(text + "\n")



# ================================================================ QUIET-DAY FILTER (fixed rule, all charts)
QX = [0.6, 0.7, 0.8, 1.0]


def quiet_one(sym, tf, df1, df):
    base = run(df)
    ind = _IND[next(iter(_IND))]
    yr = regime_features(df1, df, ind)["yrange"]
    sm = pd.Timestamp(SPLIT, tz=NY)
    rows, runs = [], {}
    for x in QX:
        ok = np.nan_to_num(yr, nan=99.0) < x
        runs[x] = run(df, allowL=ok, allowS=ok)
    big = np.nan_to_num(yr, nan=0.0) <= 1.0
    runs["skipbig"] = run(df, allowL=big, allowS=big)

    def line(name, t):
        tr, te = t[t["entry_time"] < sm], t[t["entry_time"] >= sm]
        s_all, s_tr, s_te = stats(t), stats(tr), stats(te)
        if s_all.get("n", 0) == 0:
            return f"| {name} | 0 | | | | | |"
        days = t["entry_time"].dt.date.nunique()
        return (f"| {name} | {s_all['n']} | {s_all['win']:.0f}% | **{s_all['avg']:+.3f}** | {s_all['pf']:.2f} | "
                f"{s_tr.get('avg', float('nan')):+.3f} | **{s_te.get('avg', float('nan')):+.3f}** | {s_all['dd']:.0f} | {days} |")
    md = [f"## {sym} {tf}-minute", "",
          "| Rule | Trades | Win | ATR / trade (all) | PF | TRAIN 2020-23 | TEST 2024-now | Worst DD (ATR) | Days traded |",
          "|---|---|---|---|---|---|---|---|---|", line("v3.0 (no filter)", base)]
    for x in QX:
        md.append(line(f"only after quiet days: yesterday < {x:.1f} ATR", runs[x]))
    md.append(line("skip days after a big day (yesterday > 1.0 ATR)", runs["skipbig"]))
    md += ["", "| Year | v3.0 | quiet < 0.7 | trades (quiet) |", "|---|---|---|---|"]
    q = runs[0.7]
    for y in sorted(set(base["entry_time"].dt.year)):
        b_, q_ = base[base["entry_time"].dt.year == y], q[q["entry_time"].dt.year == y]
        md.append(f"| {y} | {avg(b_['r']):+.2f} | **{avg(q_['r']):+.2f}** | {len(q_)} |")
    md.append("")
    return md


def quiet_main():
    end = datetime.now(timezone.utc) - timedelta(days=1)
    start = datetime.fromisoformat(START).replace(tzinfo=timezone.utc)
    test = os.getenv("TEST", "") == "1"
    os.makedirs(OUT, exist_ok=True)
    md = [f"# Trend Flip quiet-day filter - {datetime.now(NY):%Y-%m-%d %H:%M} ET",
          "Rule: only take v3.0 trades when YESTERDAY's 9:30-16:00 range (high - low) was below X times the daily "
          "ATR(14). Found in the market-conditions study; same rule on every chart. ATR / trade like the TradingView box.", ""]
    for sym in SYMBOLS:
        print(f"\n=== {sym} ===", flush=True)
        df1, feed = fake_1m(sym, start, end) if test else fetch_1m(sym, start, end)
        for tf in TFS:
            print(f"  {tf}m ...", flush=True)
            df = to_tf(df1, rth_only=False, mins=tf)
            _IND.clear()
            md += quiet_one(sym, tf, df1, df)
            _IND.clear()
    text = "\n".join(md)
    print("\n" + text)
    stamp = datetime.now(NY).strftime("%Y-%m-%d")
    for path in (f"{OUT}/quiet_{stamp}.md", f"{OUT}/quiet_latest.md"):
        with open(path, "w") as f:
            f.write(text + "\n")
    summ = os.getenv("GITHUB_STEP_SUMMARY")
    if summ:
        with open(summ, "a") as f:
            f.write(text + "\n")


# ================================================================ OPTIMIZER + MONTE CARLO (MODE=optimize)
# 1. Every entry idea and every exit idea is tested ON TOP of the quiet-day filter (yesterday < 0.7 daily ATR).
# 2. Winners are picked on TRAIN (2020-2023) only: an idea is picked if it earns more option $ per year than the
#    plain quiet-day setup on at least 3 of the 4 charts. TEST (2024-now) is only used to check, never to pick.
# 3. Monte Carlo: the final setup's trading DAYS are re-shuffled into 10,000 possible years, so you see the range
#    of years it could give you (typical, bad case, chance of a losing year, worst drop from a high).
# Option $ = Black-Scholes estimate for an at-the-money call (longs) or put (shorts), 1 contract, in today's prices:
#   volatility from the daily ATR (ATR / 1.6 = daily move, +15% implied-vol premium), time decay from the real clock
#   (0DTE expires at today's close, 1DTE at tomorrow's close), minus COST $ per round trip (spread + commission).
#   This includes theta and gamma, which the simple "delta x ATR" number does not. Still an estimate, not fills.
from math import erf as _m_erf

COST = float(os.getenv("COST", "2"))             # $ per contract per round trip
PICK = os.getenv("OPT", "1dte").strip().lower()   # option type used to pick winners: 1dte or 0dte
QUIET_X = float(os.getenv("QUIET_X", "0.7"))
PATHS = int(os.getenv("PATHS", "10000"))

ENTRY_TESTS = [
    ("+ 15m agrees", dict(htf=1)),
    ("+ 15m and 60m agree", dict(htf=2)),
    ("Vix Fix spike within 5", dict(vf_look=5)),
    ("Vix Fix spike within 20", dict(vf_look=20)),
    ("no Vix Fix filter", dict(vf_on=False)),
    ("no waiting for a late spike (wait 0)", dict(wait=0)),
    ("wait up to 10 for a spike", dict(wait=10)),
    ("entries from 10:00", dict(t_start=1000)),
    ("no entries after 14:00", dict(t_end=1400)),
    ("no VWAP rule on the line", dict(use_vwap=False)),
]
EXIT_TESTS = [
    ("EXIT ride strong trend", dict(xm=1)),
    ("EXIT ride if 15m agrees", dict(xm=2)),
    ("EXIT cut losers on warning", dict(xm=3)),
    ("EXIT ride + cut losers", dict(xm=4)),
    ("EXIT ride + cut, warning after 3 candles", dict(xm=4, weak_n=3)),
    ("EXIT hold 10 candles", dict(hold=10)),
    ("EXIT hold 20 candles", dict(hold=20)),
    ("EXIT hold 25 candles", dict(hold=25)),
    ("EXIT stop 1.5 ATR", dict(stop=1.5)),
    ("EXIT stop 3 ATR", dict(stop=3.0)),
    ("EXIT no stop (flip / time / 15:55 only)", dict(stop=50.0)),
]
TV_NAME = {  # how to set each idea in Trend Flip v4.1
    "+ 15m agrees": "Higher timeframes > Entry filter = HTF 1 agrees",
    "+ 15m and 60m agree": "Higher timeframes > Entry filter = Both agree",
    "Vix Fix spike within 5": "Setup > Vix Fix: spike within the last N candles = 5",
    "Vix Fix spike within 20": "Setup > Vix Fix: spike within the last N candles = 20",
    "no Vix Fix filter": "Setup > Vix Fix filter = OFF",
    "no waiting for a late spike (wait 0)": "Setup > No spike at the flip? Wait up to N candles = 0",
    "wait up to 10 for a spike": "Setup > No spike at the flip? Wait up to N candles = 10",
    "entries from 10:00": "Exit > New entries from = 1000",
    "no entries after 14:00": "Exit > New entries until = 1400",
    "no VWAP rule on the line": "Setup > Price must be on the right side of VWAP = OFF",
    "EXIT ride strong trend": "Exit > Exit = Ride strong trend",
    "EXIT ride if 15m agrees": "Exit > Exit = Ride if HTF agrees",
    "EXIT cut losers on warning": "Exit > Exit = Cut losers on warning",
    "EXIT ride + cut losers": "Exit > Exit = Ride + cut losers",
    "EXIT ride + cut, warning after 3 candles": "Exit > Exit = Ride + cut losers, and Warning colors > N = 3",
    "EXIT hold 10 candles": "Exit > Time: sell at the close of candle N = 10",
    "EXIT hold 20 candles": "Exit > Time: sell at the close of candle N = 20",
    "EXIT hold 25 candles": "Exit > Time: sell at the close of candle N = 25",
    "EXIT stop 1.5 ATR": "Exit > Stop (x ATR) = 1.5",
    "EXIT stop 3 ATR": "Exit > Stop (x ATR) = 3",
    "EXIT no stop (flip / time / 15:55 only)": "Exit > Stop (x ATR) = 50",
}

_verf = np.vectorize(_m_erf)


def _ncdf(x):
    return 0.5 * (1.0 + _verf(np.asarray(x, dtype=float) / np.sqrt(2.0)))


def bs_price(S, K, T, sig, call):
    """Black-Scholes, no rates/dividends. T in years, sig annual."""
    T = np.maximum(T, 1e-9)
    v = np.maximum(sig * np.sqrt(T), 1e-9)
    d1 = (np.log(S / K) + 0.5 * v * v) / v
    c = S * _ncdf(d1) - K * _ncdf(d1 - v)
    return np.where(call, c, c - S + K)


def fm(x):
    if x is None or (isinstance(x, float) and np.isnan(x)):
        return "-"
    return f"{'+' if x >= 0 else '-'}${abs(x):,.0f}"


class Ctx:
    """Everything about one chart that does not depend on the setup being tested."""

    def __init__(self, sym, tf, df1, df):
        self.sym, self.tf, self.df = sym, tf, df
        self.name = f"{sym} {tf}m"
        base = run(df)
        ind = _IND[next(iter(_IND))]
        F = regime_features(df1, df, ind)
        self.yr = F["yrange"]
        self.quiet_ok = np.nan_to_num(self.yr, nan=99.0) < QUIET_X
        vol = pd.Series(F["vol"]).ffill().bfill().to_numpy()            # daily ATR as % of price
        self.sig = vol / 100.0 / 1.6 * np.sqrt(252.0) * 1.15             # annual implied-vol estimate
        self.times = df.index
        self.mod = (df.index.hour * 60 + df.index.minute).to_numpy()
        hm = ind["hm"]
        rth = (hm >= 930) & (hm < 1600)
        dates = pd.Index(df.index.date)
        last_bar = pd.Series(self.mod[rth], index=dates[rth]).groupby(level=0).max() + tf
        self.close_min = last_bar                                         # minute of day the session closes
        self.sessions = np.array(sorted(set(dates[rth])))
        self.split = pd.Timestamp(SPLIT, tz=NY).date()
        self.n_tr = int((self.sessions < self.split).sum())
        self.n_te = int((self.sessions >= self.split).sum())
        last_days = self.sessions[-20:]
        mask = rth & np.isin(np.array(df.index.date), last_days)
        self.atr_now = float(np.nanmean(ind["atr"][mask]))
        self.p_now = float(ind["c"][rth][-1])
        self.base = base

    def money(self, t):
        """Adds option $ columns (today's prices, after costs) to a trades table."""
        t = t.copy()
        if len(t) == 0:
            for k in ("usd_delta", "usd_1dte", "usd_0dte"):
                t[k] = []
            t["date"] = []
            return t
        ib, ix = t["ib"].to_numpy(), t["ix"].to_numpy()
        S0, S1 = t["entry"].to_numpy(), t["exit"].to_numpy()
        call = t["side"].to_numpy() == 1
        dates = pd.Index(self.times[ib].date)
        cm = self.close_min.reindex(dates).to_numpy(dtype=float)
        cm = np.where(np.isnan(cm), 960.0, cm)
        rem0 = np.maximum(cm - self.mod[ib], 1.0)
        rem1 = np.maximum(cm - (self.mod[ix] + self.tf), 0.5)
        sig = self.sig[np.maximum(ib - 1, 0)]
        K = np.round(S0)
        scale = self.p_now / S0 * 100.0
        yr_min = 252.0 * 390.0
        for k, extra in (("usd_0dte", 0.0), ("usd_1dte", 390.0)):
            v0 = bs_price(S0, K, (rem0 + extra) / yr_min, sig, call)
            v1 = bs_price(S1, K, (rem1 + extra) / yr_min, sig, call)
            t[k] = (v1 - v0) * scale - COST
        t["usd_delta"] = t["r"] * self.atr_now * DELTA * 100.0 - COST
        t["date"] = dates
        return t

    def ev(self, t):
        t = self.money(t)
        d = t["date"].to_numpy() if len(t) else np.array([])
        tr, te = t[d < self.split] if len(t) else t, t[d >= self.split] if len(t) else t
        yt, ye = max(self.n_tr / 252.0, 1e-9), max(self.n_te / 252.0, 1e-9)
        ya = yt + ye

        def part(x, yrs):
            n = len(x)
            return dict(n=n, per_yr=n / yrs, avg=x["r"].mean() if n else float("nan"),
                        win=100 * (x["r"] > 0).mean() if n else float("nan"),
                        d1=x["usd_1dte"].sum() / yrs if n else 0.0, d0=x["usd_0dte"].sum() / yrs if n else 0.0,
                        dd=x["usd_delta"].sum() / yrs if n else 0.0,
                        t1=x["usd_1dte"].mean() if n else float("nan"), t0=x["usd_0dte"].mean() if n else float("nan"))
        return dict(all=part(t, ya), tr=part(tr, yt), te=part(te, ye), trades=t)

    def daily(self, t, col, which="all"):
        s = t.groupby("date")[col].sum() if len(t) else pd.Series(dtype=float)
        sess = self.sessions if which == "all" else (
            self.sessions[self.sessions < self.split] if which == "tr" else self.sessions[self.sessions >= self.split])
        return s.reindex(sess, fill_value=0.0).to_numpy(dtype=float)


def monte_carlo(daily, seed, paths=PATHS, days=252):
    """Re-shuffle trading days (with replacement) into many possible years."""
    if len(daily) == 0:
        return None
    rng = np.random.default_rng(seed)
    out_tot, out_dd, out_q = [], [], []
    for chunk in range(0, paths, 2000):
        k = min(2000, paths - chunk)
        sim = daily[rng.integers(0, len(daily), size=(k, days))]
        cum = np.cumsum(sim, axis=1)
        peak = np.maximum.accumulate(np.concatenate([np.zeros((k, 1)), cum], axis=1), axis=1)[:, 1:]
        out_dd.append((peak - cum).max(axis=1))
        out_tot.append(cum[:, -1])
        out_q.append(cum[:, days // 4 - 1])
    tot, dd, q = np.concatenate(out_tot), np.concatenate(out_dd), np.concatenate(out_q)
    # how sure is the edge? re-shuffle the whole history (same length) many times
    L = len(daily)
    hist = np.array([daily[rng.integers(0, L, L)].sum() for _ in range(2000)])
    return dict(med=np.median(tot), p5=np.percentile(tot, 5), p95=np.percentile(tot, 95),
                lose=100 * (tot < 0).mean(), lose_q=100 * (q < 0).mean(),
                dd_med=np.median(dd), dd95=np.percentile(dd, 95), real=100 * (hist > 0).mean())


def mc_row(label, opt, sample, m, per_yr):
    if m is None:
        return f"| {label} | {opt} | {sample} | 0 | | | | | | | | |"
    return (f"| {label} | {opt} | {sample} | {per_yr:.0f} | **{fm(m['med'])}** | {fm(m['p5'])} | {fm(m['p95'])} | "
            f"**{m['lose']:.0f}%** | {m['lose_q']:.0f}% | {fm(-m['dd_med'])} | {fm(-m['dd95'])} | {m['real']:.0f}% |")


MC_HEAD = ("| Setup | Option | Days sampled from | Trades / yr | Typical year | Bad year (1 in 20) | Good year (1 in 20) | "
           "Chance of a losing year | Chance of a losing 3 months | Typical worst drop | Bad-case worst drop | "
           "Chance the edge is real |\n|---|---|---|---|---|---|---|---|---|---|---|---|")


def optimize_main():
    end = datetime.now(timezone.utc) - timedelta(days=1)
    start = datetime.fromisoformat(START).replace(tzinfo=timezone.utc)
    test = os.getenv("TEST", "") == "1"
    os.makedirs(OUT, exist_ok=True)
    pk = "d1" if PICK != "0dte" else "d0"
    pk_name = "1DTE" if pk == "d1" else "0DTE"
    charts = []
    for sym in SYMBOLS:
        print(f"\n=== {sym} ===", flush=True)
        df1, feed = fake_1m(sym, start, end) if test else fetch_1m(sym, start, end)
        for tf in TFS:
            df = to_tf(df1, rth_only=False, mins=tf)
            _IND.clear()
            print(f"  {sym} {tf}m: {len(df):,} bars ({feed})", flush=True)
            cx = Ctx(sym, tf, df1, df)
            ok = cx.quiet_ok
            res = {"v3.0 (every day)": cx.ev(cx.base)}
            res["QUIET (v3.0 + quiet-day filter)"] = cx.ev(run(df, allowL=ok, allowS=ok))
            for name, over in ENTRY_TESTS + EXIT_TESTS:
                print(f"    {cx.name}: {name}", flush=True)
                res[name] = cx.ev(run(df, allowL=ok, allowS=ok, **over))
                for k in list(_IND.keys())[1:]:
                    if len(_IND) > 2:
                        del _IND[k]
            cx.res = res
            charts.append(cx)
            _IND.clear()
        del df1
    QK = "QUIET (v3.0 + quiet-day filter)"
    nC = len(charts)
    need = max(1, int(np.ceil(0.75 * nC)))

    # ---------- scoreboard (picked on TRAIN only)
    board = []
    for name, over in ENTRY_TESTS + EXIT_TESTS:
        dtr = [c.res[name]["tr"][pk] - c.res[QK]["tr"][pk] for c in charts]
        dte = [c.res[name]["te"][pk] - c.res[QK]["te"][pk] for c in charts]
        btr, bte = sum(x > 0 for x in dtr), sum(x > 0 for x in dte)
        board.append(dict(name=name, over=over, kind="exit" if name.startswith("EXIT") else "entry",
                          btr=btr, bte=bte, mtr=float(np.mean(dtr)), mte=float(np.mean(dte)),
                          cand=btr >= need and np.mean(dtr) > 0))
    best_e = max([b for b in board if b["cand"] and b["kind"] == "entry"], key=lambda b: b["mtr"], default=None)
    best_x = max([b for b in board if b["cand"] and b["kind"] == "exit"], key=lambda b: b["mtr"], default=None)

    # ---------- final setup: best of {quiet, +entry pick, +exit pick, +both}, judged on TRAIN only
    options = [("QUIET only", {}, [])]
    if best_e:
        options.append((f"QUIET + {best_e['name']}", dict(best_e["over"]), [best_e["name"]]))
    if best_x:
        options.append((f"QUIET + {best_x['name']}", dict(best_x["over"]), [best_x["name"]]))
    if best_e and best_x:
        options.append((f"QUIET + {best_e['name']} + {best_x['name']}", dict(best_e["over"], **best_x["over"]),
                        [best_e["name"], best_x["name"]]))
    for c in charts:
        c.opt_res = {}
        for lbl, over, names in options:
            if not names:
                c.opt_res[lbl] = c.res[QK]
            elif len(names) == 1:
                c.opt_res[lbl] = c.res[names[0]]
            else:
                print(f"    {c.name}: combined {lbl}", flush=True)
                c.opt_res[lbl] = c.ev(run(c.df, allowL=c.quiet_ok, allowS=c.quiet_ok, **over))
                _IND.clear()
    final_lbl, final_over, final_names = max(
        options, key=lambda o: np.mean([c.opt_res[o[0]]["tr"][pk] for c in charts]))

    # ---------- write up
    yrs_tr = f"{START[:4]}-{int(SPLIT[:4]) - 1}"
    yrs_te = f"{SPLIT[:4]}-now"
    det = []
    for c in charts:
        det += [f"## {c.name}: every idea on top of the quiet-day filter",
                f"Today's prices: {c.sym} ≈ {c.p_now:.2f}, 1 ATR ({c.tf}m) ≈ {c.atr_now:.2f} pts. "
                f"TRAIN {yrs_tr} = {c.n_tr} sessions, TEST {yrs_te} = {c.n_te} sessions. $ = 1 contract per trade, after ${COST:.0f} costs.", "",
                f"| Setup | Trades / yr | Win | ATR / trade TRAIN | ATR / trade TEST | 1DTE $/yr TRAIN | 1DTE $/yr TEST | "
                f"0DTE $/yr TRAIN | 0DTE $/yr TEST | beats QUIET ({pk_name}) |",
                "|---|---|---|---|---|---|---|---|---|---|"]
        q = c.res[QK]
        for name, r in c.res.items():
            if name in ("v3.0 (every day)", QK):
                mark = ""
                nm = f"**{name}**"
            else:
                a, b = r["tr"][pk] > q["tr"][pk], r["te"][pk] > q["te"][pk]
                mark = "✅ both" if a and b else ("TRAIN only" if a else ("TEST only" if b else ""))
                nm = name
            det.append(f"| {nm} | {r['all']['per_yr']:.0f} | {r['all']['win']:.0f}% | {r['tr']['avg']:+.3f} | "
                       f"**{r['te']['avg']:+.3f}** | {fm(r['tr']['d1'])} | **{fm(r['te']['d1'])}** | "
                       f"{fm(r['tr']['d0'])} | {fm(r['te']['d0'])} | {mark} |")
        det.append("")

    sb = [f"## Scoreboard: does the idea beat the quiet-day setup? ({nC} charts, {pk_name} $ per year)",
          f"Picked = beats QUIET on TRAIN ({yrs_tr}) on at least {need} of {nC} charts. TEST ({yrs_te}) was never used to pick.", "",
          f"| Idea | TRAIN: charts better | TEST: charts better | TRAIN $/yr vs QUIET (avg) | TEST $/yr vs QUIET (avg) | Picked on TRAIN? | Held up on TEST? |",
          "|---|---|---|---|---|---|---|"]
    for b in sorted(board, key=lambda b: -b["mtr"]):
        held = "" if not b["cand"] else ("✅ yes" if b["bte"] >= need and b["mte"] > 0 else "❌ no")
        sb.append(f"| {b['name']} | {b['btr']}/{nC} | {b['bte']}/{nC} | {fm(b['mtr'])} | {fm(b['mte'])} | "
                  f"{'✅' if b['cand'] else ''} | {held} |")
    sb.append("")

    fin = [f"## Final setup (picked on TRAIN): **{final_lbl}**",
           "Choices tried (best average TRAIN wins): " + "; ".join(o[0] for o in options) + "."]
    if final_names:
        fin.append("TradingView v4.1 settings: " + " | ".join(TV_NAME.get(n, n) for n in final_names) + " (quiet-day filter stays ON).")
    fin += ["", "| Chart | Setup | TRAIN ATR / trade | TEST ATR / trade | TRAIN 1DTE $/yr | TEST 1DTE $/yr | TEST 0DTE $/yr |",
            "|---|---|---|---|---|---|---|"]
    fin_test_better = 0
    for c in charts:
        f_ = c.opt_res[final_lbl]
        if f_["te"][pk] > c.res[QK]["te"][pk] or not final_names:
            fin_test_better += 1
        for lbl, r in (("v3.0 every day", c.res["v3.0 (every day)"]), ("QUIET", c.res[QK]), ("**FINAL**", f_)):
            fin.append(f"| {c.name} | {lbl} | {r['tr']['avg']:+.3f} | **{r['te']['avg']:+.3f}** | {fm(r['tr']['d1'])} | "
                       f"**{fm(r['te']['d1'])}** | {fm(r['te']['d0'])} |")
    fin.append("")

    mc = ["## Monte Carlo: 10,000 possible years (1 contract per trade, today's prices, after costs)",
          "How it works: the real trading days (including days with no trade) are drawn at random, with replacement, "
          "252 at a time = one possible year. Repeated 10,000 times. "
          "*Chance the edge is real* = how often a re-shuffled copy of the whole history still ended in profit "
          "(95%+ = strong, 80-95% = maybe, under 80% = could easily be luck). "
          "*Worst drop* = biggest fall from a high point during the year.", ""]
    head_lines = []
    seed = 1
    for c in charts:
        f_ = c.opt_res[final_lbl]
        mc += [f"### {c.name}", MC_HEAD]
        rows = [("v3.0 every day", c.res["v3.0 (every day)"]), ("QUIET", c.res[QK]), ("FINAL", f_)]
        for col, opt in (("usd_1dte", "1DTE"), ("usd_0dte", "0DTE")):
            for lbl, r in rows:
                seed += 1
                m = monte_carlo(c.daily(r["trades"], col), seed)
                mc.append(mc_row(lbl, opt, "all years", m, r["all"]["per_yr"]))
                if lbl == "FINAL" and opt == pk_name:
                    head_lines.append(
                        f"- **{c.name}** ({opt}): typical year {fm(m['med']) if m else '-'}, "
                        f"bad year {fm(m['p5']) if m else '-'}, chance of a losing year {m['lose']:.0f}%, "
                        f"bad-case worst drop {fm(-m['dd95'])}, chance the edge is real {m['real']:.0f}%"
                        if m else f"- **{c.name}**: no trades")
            if opt == pk_name:
                for which, nm in (("tr", f"only {yrs_tr} (if that market comes back)"), ("te", f"only {yrs_te}")):
                    seed += 1
                    m = monte_carlo(c.daily(f_["trades"], col, which), seed)
                    mc.append(mc_row("FINAL", opt, nm, m, f_[which]["per_yr"]))
        mc.append("")
        ft = f_["trades"]
        if len(ft):
            ft.assign(entry_time=ft["entry_time"].dt.strftime("%Y-%m-%d %H:%M")).drop(columns=["date"]).round(3).to_csv(
                f"{OUT}/final_trades_{c.sym}_{c.tf}m.csv", index=False)

    yr = ["## Year by year (1DTE $ per year, 1 contract)", "| Chart | Year | v3.0 every day | QUIET | FINAL | FINAL trades |",
          "|---|---|---|---|---|---|"]
    for c in charts:
        f_ = c.opt_res[final_lbl]["trades"]
        b_, q_ = c.res["v3.0 (every day)"]["trades"], c.res[QK]["trades"]
        for y in sorted(set(b_["entry_time"].dt.year)):
            def ys(t):
                return t[t["entry_time"].dt.year == y]["usd_1dte"].sum() if len(t) else 0.0
            nf = int((f_["entry_time"].dt.year == y).sum()) if len(f_) else 0
            yr.append(f"| {c.name} | {y} | {fm(ys(b_))} | {fm(ys(q_))} | **{fm(ys(f_))}** | {nf} |")
    yr.append("")

    top = [f"# Trend Flip optimizer + Monte Carlo - {datetime.now(NY):%Y-%m-%d %H:%M} ET",
           f"Data {START} to {end:%Y-%m-%d}, {', '.join(c.name for c in charts)}. DATA ONLY - no orders.", "",
           "## The answer in 30 seconds",
           f"- Entry idea picked on {yrs_tr}: **{best_e['name'] if best_e else 'none beat the quiet-day setup'}**",
           f"- Exit idea picked on {yrs_tr}: **{best_x['name'] if best_x else 'none beat the quiet-day setup'}**",
           f"- Final setup: **{final_lbl}**" + (f" - beat QUIET on {yrs_te} (never seen) on {fin_test_better}/{nC} charts"
                                                 if final_names else ""),
           f"- Monte Carlo of the final setup, 1 contract per trade, after ${COST:.0f} costs per trade:"] + head_lines + [
           "",
           f"Assumptions: option $ = Black-Scholes estimate for an at-the-money option (theta and gamma included), "
           f"implied vol from the daily ATR, in today's {', '.join(sorted(set(c.sym for c in charts)))} prices, "
           f"${COST:.0f} per round trip. Real fills, IV changes and slippage will differ. Quiet day = yesterday's "
           f"range < {QUIET_X:.1f} daily ATR.", ""]
    text = "\n".join(top + sb + fin + mc + yr + det)
    print("\n" + text)
    stamp = datetime.now(NY).strftime("%Y-%m-%d")
    for path in (f"{OUT}/optimize_{stamp}.md", f"{OUT}/optimize_latest.md"):
        with open(path, "w") as f:
            f.write(text + "\n")
    summ = os.getenv("GITHUB_STEP_SUMMARY")
    if summ:
        with open(summ, "a") as f:
            f.write(text + "\n")


# ================================================================ ENTRY QUALITY (MODE=quality, the default)
# For traders who manage the exit by hand: grades ONLY the entry, so no exit rule is involved.
# For every entry (filled at the next open) it watches the next 30 candles (or until 15:55):
#   +1 before -1 = price reached +1 ATR your way before it went 1 ATR against you (same candle = counted as a loss)
#   +2 before -1 = reached +2 ATR before -1 ATR against ("great trade")
#   1:1 result   = what a simple bracket (+1 ATR target / -1 ATR stop) made, in ATR; unresolved = closed after 30 candles
#   1:2 result   = same with a +2 ATR target / -1 ATR stop
# One trade at a time: a new signal is ignored while the previous one is still open (bracket not hit yet).
# Every combination of the settings below is tested on all charts; TRAIN = 2020-2023, TEST = 2024-now.
# A combination only counts if it is good in BOTH periods (score = the worse of the two).
QWIN = int(os.getenv("QWIN", "30"))
LUCK = "55% (2020-23) / 52% (2024-now), with 4/4 charts \"positive\" - measured on random-walk data, same 4 charts and dates"
GRID = dict(
    quiet=[None, 0.7],
    window=[(935, 1530), (1000, 1530), (935, 1400), (1000, 1400)],
    vf=[5, 10, 20, None],
    htf=[0, 1],
    vwap=[True, False],
)
WIN_NAME = {(935, 1530): "9:35-15:30", (1000, 1530): "10:00-15:30", (935, 1400): "9:35-14:00", (1000, 1400): "10:00-14:00"}


def grade_entries(ind, ent, times, win=QWIN):
    o, h, l, c, atr, hm, day = ind["o"], ind["h"], ind["l"], ind["c"], ind["atr"], ind["hm"], ind["day"]
    n = len(o)
    rows = []
    busy_until = -1
    for i in np.nonzero(ent)[0]:
        e_i = i + 1
        if e_i >= n or day[e_i] != day[i] or e_i <= busy_until:
            continue
        sd, en, a = int(ent[i]), o[e_i], atr[i]
        if not a or np.isnan(a):
            continue
        r1 = r2 = None
        h1 = h2 = 0
        mfe = mae = 0.0
        j = e_i
        last = e_i
        res1 = None
        while j < n and day[j] == day[e_i] and j < e_i + win and hm[j] < 1555:
            fav = ((h[j] - en) if sd == 1 else (en - l[j])) / a
            adv = ((en - l[j]) if sd == 1 else (h[j] - en)) / a
            mae = max(mae, adv) if h1 == 0 and r1 is None else mae
            mfe = max(mfe, fav)
            if r1 is None:
                if adv >= 1:
                    r1, res1 = -1.0, j
                elif fav >= 1:
                    r1, h1, res1 = 1.0, 1, j
            if r2 is None:
                if adv >= 1:
                    r2 = -1.0
                elif fav >= 2:
                    r2, h2 = 2.0, 1
            last = j
            if r1 is not None and r2 is not None:
                break
            j += 1
        close_r = sd * (c[last] - en) / a
        if r1 is None:
            r1, res1 = close_r, last
        if r2 is None:
            r2 = close_r
        busy_until = res1
        rows.append((times[e_i], sd, h1, h2, r1, r2, mfe, res1 - e_i + 1))
    return pd.DataFrame(rows, columns=["t", "side", "hit1", "hit2", "r1", "r2", "mfe", "bars"])


def q_stats(g, years):
    if len(g) == 0:
        return dict(n=0, per_yr=0.0, hit1=np.nan, hit2=np.nan, r1=np.nan, r2=np.nan, mfe=np.nan, bars=np.nan)
    return dict(n=len(g), per_yr=len(g) / years, hit1=100 * g["hit1"].mean(), hit2=100 * g["hit2"].mean(),
                r1=g["r1"].mean(), r2=g["r2"].mean(), mfe=g["mfe"].mean(), bars=g["bars"].mean())


def combo_name(k):
    q, w, vf, htf, vw = k
    parts = ["quiet days only" if q else "every day", WIN_NAME[w], f"Vix Fix {vf}" if vf else "no Vix Fix"]
    if htf:
        parts.append("15m agrees")
    if not vw:
        parts.append("no VWAP rule")
    return " · ".join(parts)


def combo_tv(k):
    q, w, vf, htf, vw = k
    return (f"Trade days = {'Only after quiet days' if q else 'Every day'}; "
            f"New entries from = {w[0]}, until = {w[1]}; "
            + (f"Vix Fix filter ON, spike within = {vf}" if vf else "Vix Fix filter OFF")
            + f"; HTF entry filter = {'HTF 1 agrees' if htf else 'Off'}; "
            f"VWAP rule = {'ON' if vw else 'OFF'}")


def quality_main():
    import itertools
    end = datetime.now(timezone.utc) - timedelta(days=1)
    start = datetime.fromisoformat(START).replace(tzinfo=timezone.utc)
    test = os.getenv("TEST", "") == "1"
    os.makedirs(OUT, exist_ok=True)
    split = pd.Timestamp(SPLIT, tz=NY)
    combos = list(itertools.product(GRID["quiet"], GRID["window"], GRID["vf"], GRID["htf"], GRID["vwap"]))
    BASE = (None, (935, 1530), 10, 0, True)        # v3.0
    res = {k: {} for k in combos}
    chart_info = []
    for sym in SYMBOLS:
        print(f"\n=== {sym} ===", flush=True)
        df1, feed = fake_1m(sym, start, end) if test else fetch_1m(sym, start, end)
        for tf in TFS:
            df = to_tf(df1, rth_only=False, mins=tf)
            _IND.clear()
            name = f"{sym} {tf}m"
            run(df)                                                     # builds indicators (VWAP on)
            ind_on = _IND[next(iter(_IND))]
            yr = regime_features(df1, df, ind_on)["yrange"]
            hm = ind_on["hm"]
            rth = (hm >= 930) & (hm < 1600)
            dates = np.array(sorted(set(pd.Index(df.index.date)[rth])))
            y_tr = max((dates < split.date()).sum() / 252.0, 1e-9)
            y_te = max((dates >= split.date()).sum() / 252.0, 1e-9)
            last_days = dates[-20:]
            atr_now = float(np.nanmean(ind_on["atr"][rth & np.isin(np.array(df.index.date), last_days)]))
            chart_info.append((name, atr_now, float(ind_on["c"][rth][-1])))
            inds = {True: ind_on, False: indicators(df, 13, 34, False)}
            for k in combos:
                q, w, vf, htf, vw = k
                p = dict(V30, t_start=w[0], t_end=w[1], vf_on=vf is not None, vf_look=vf or 10, htf=htf)
                if q:
                    ok = np.nan_to_num(yr, nan=99.0) < q
                    p["allowL"], p["allowS"] = ok, ok
                _, ent = signals(inds[vw], p)
                g = grade_entries(inds[vw], ent, df.index)
                tr, te = g[g["t"] < split], g[g["t"] >= split]
                res[k][name] = dict(tr=q_stats(tr, y_tr), te=q_stats(te, y_te), all=q_stats(g, y_tr + y_te))
            print(f"  {name}: {len(combos)} combinations graded", flush=True)
            _IND.clear()
            del inds
        del df1
    charts = [c[0] for c in chart_info]
    nC = len(charts)
    y_te_all = y_te

    def moe(p, n):
        return 196 * np.sqrt(max(p / 100 * (1 - p / 100), 1e-9) / max(n, 1)) if not np.isnan(p) else float("nan")

    rows = []
    for k in combos:
        r = res[k]
        b = res[BASE]
        tr1 = np.mean([r[c]["tr"]["r1"] for c in charts])
        te1 = np.mean([r[c]["te"]["r1"] for c in charts])
        tr2 = np.mean([r[c]["tr"]["r2"] for c in charts])
        te2 = np.mean([r[c]["te"]["r2"] for c in charts])
        both = sum(r[c]["tr"]["r1"] > b[c]["tr"]["r1"] and r[c]["te"]["r1"] > b[c]["te"]["r1"] for c in charts)
        pos = sum(r[c]["tr"]["r1"] > 0 and r[c]["te"]["r1"] > 0 for c in charts)
        rows.append(dict(k=k, name=combo_name(k), per_yr=np.mean([r[c]["all"]["per_yr"] for c in charts]),
                         h1_tr=np.mean([r[c]["tr"]["hit1"] for c in charts]), h1_te=np.mean([r[c]["te"]["hit1"] for c in charts]),
                         h2_tr=np.mean([r[c]["tr"]["hit2"] for c in charts]), h2_te=np.mean([r[c]["te"]["hit2"] for c in charts]),
                         tr1=tr1, te1=te1, tr2=tr2, te2=te2, score1=min(tr1, te1), score2=min(tr2, te2),
                         both=both, pos=pos, mfe=np.mean([r[c]["all"]["mfe"] for c in charts]),
                         bars=np.mean([r[c]["all"]["bars"] for c in charts])))
    enough = [x for x in rows if x["per_yr"] >= 25]
    rank = sorted(enough, key=lambda x: -max(x["score1"], x["score2"]))
    base = next(x for x in rows if x["k"] == BASE)
    best = rank[0]
    use2 = best["score2"] > best["score1"]

    def line(x, mark=""):
        return (f"| {mark}{x['name']} | {x['per_yr']:.0f} | {x['h1_tr']:.0f}% / **{x['h1_te']:.0f}%** | "
                f"{x['tr1']:+.3f} / **{x['te1']:+.3f}** | {x['h2_tr']:.0f}% / **{x['h2_te']:.0f}%** | "
                f"{x['tr2']:+.3f} / **{x['te2']:+.3f}** | {x['pos']}/{nC} | {x['both']}/{nC} | {x['bars']:.0f} |")
    HQ = ("| Settings | Trades / yr per chart | +1 before -1 (TRAIN / TEST) | 1:1 bracket ATR / trade | "
          "+2 before -1 | 1:2 bracket ATR / trade | Charts positive in BOTH periods (1:1) | Charts better than v3.0 in BOTH | "
          "Avg candles to +1 or -1 |\n|---|---|---|---|---|---|---|---|---|")
    md = [f"# Trend Flip ENTRY QUALITY - {datetime.now(NY):%Y-%m-%d %H:%M} ET",
          f"Data {START} to {end:%Y-%m-%d}, {', '.join(charts)}. {len(combos)} setting combinations. DATA ONLY - no orders.",
          "Grades only the entry (you manage the exit). 50% '+1 before -1' = coin flip; 55%+ in BOTH periods is a real edge. "
          "1:1 / 1:2 bracket = what a fixed target/stop would have made per trade (ATR). TRAIN 2020-2023 / TEST 2024-now.", "",
          "## The answer in 30 seconds",
          f"- **Best settings (good in BOTH periods):** {best['name']}",
          f"- In TradingView v4.1: {combo_tv(best['k'])}",
          f"- Hits +1 ATR before -1 ATR: **{best['h1_tr']:.0f}%** (2020-23) / **{best['h1_te']:.0f}%** (2024-now) "
          f"vs v3.0 {base['h1_tr']:.0f}% / {base['h1_te']:.0f}% "
          f"(luck margin about ±{moe(best['h1_te'], best['per_yr'] * nC * y_te_all):.0f} points on 2024-now)",
          f"- Luck check: when this same search was run on RANDOM price data, the best of {len(combos)} combinations "
          f"still showed about {LUCK} '+1 before -1'. Only trust a winner that clearly beats that in BOTH periods.",
          f"- Best simple bracket for it: **{'+2 ATR target / -1 ATR stop' if use2 else '+1 ATR target / -1 ATR stop'}** "
          f"= {(best['tr2'] if use2 else best['tr1']):+.3f} / {(best['te2'] if use2 else best['te1']):+.3f} ATR per trade (TRAIN / TEST)",
          f"- About {best['per_yr']:.0f} trades a year per chart (≈ {best['per_yr'] / 52:.1f} a week)",
          "- Option reality check (1 ATR now, 0.6 delta): " + "; ".join(
              f"{n} 1 ATR ≈ ${a * DELTA * 100:.0f}" for n, a, _ in chart_info) +
          ". Costs (~$2 spread + commission) and time decay come out of that.", "",
          "## Top 15 (needs 25+ trades a year; ranked by the WORSE of TRAIN and TEST)", HQ]
    md += [line(x, "**→** " if i == 0 else "") for i, x in enumerate(rank[:15])]
    md += ["", "## Reference rows", HQ, line(base, "v3.0: ")]
    for k in combos:
        if k == (0.7, (935, 1530), 10, 0, True):
            md.append(line(next(x for x in rows if x["k"] == k), "v4.1 default: "))
    md += ["", f"## Best settings chart by chart: {best['name']}",
           "| Chart | Period | Trades | Trades / yr | +1 before -1 | +2 before -1 | 1:1 ATR / trade | 1:2 ATR / trade | Avg best move (ATR) |",
           "|---|---|---|---|---|---|---|---|---|"]
    for c in charts:
        for per, lbl in (("tr", "2020-23"), ("te", "2024-now")):
            s_ = res[best["k"]][c][per]
            b_ = res[BASE][c][per]
            md.append(f"| {c} | {lbl} | {s_['n']} | {s_['per_yr']:.0f} | **{s_['hit1']:.0f}%** (v3.0 {b_['hit1']:.0f}%) | "
                      f"{s_['hit2']:.0f}% | {s_['r1']:+.3f} | {s_['r2']:+.3f} | {s_['mfe']:.2f} |")
    md += ["", "## Every combination (sorted)", HQ]
    md += [line(x) for x in sorted(rows, key=lambda x: -max(x["score1"], x["score2"]))]
    text = "\n".join(md)
    print("\n" + text)
    stamp = datetime.now(NY).strftime("%Y-%m-%d")
    for path in (f"{OUT}/quality_{stamp}.md", f"{OUT}/quality_latest.md"):
        with open(path, "w") as f:
            f.write(text + "\n")
    summ = os.getenv("GITHUB_STEP_SUMMARY")
    if summ:
        with open(summ, "a") as f:
            f.write(text + "\n")


# ================================================================ EXPLORE (MODE=explore, the default)
# Entry-quality grade (same as MODE=quality) for:
#   A. every chart timeframe (1/2/3/5/15m) x every line setting (EMA 5/13, 8/21, 13/34, 20/50, 34/89), and FADED
#   B. timeframe agreement: for 1/2/3/5m charts, every other timeframe alone and the common pairs must agree
#   C. other setups: opening-range breakout 15/30, VWAP reclaim, yesterday's high/low breakout and rejection,
#      gap fade - each also FADED
# LUCK LINE (real data): the v3.0 entry times on that chart with a COIN-FLIP direction, 12 times over.
#   edge = '+1 before -1' minus the coin-flip rate. A result only counts if the edge is above zero on SPY and QQQ,
#   in 2020-23 and in 2024-now (4 of 4 cells) - ranked by its WORST cell.
EX_TFS = [int(x) for x in os.getenv("EX_TFS", "1,2,3,5,15").split(",")]
EX_EMAS = [(5, 13), (8, 21), (13, 34), (20, 50), (34, 89)]
EX_AGREE_CHARTS = [1, 2, 3, 5]
EX_HTFS = [1, 2, 3, 5, 15, 30, 60]
EX_PAIRS = [(1, 15), (1, 5), (5, 15), (5, 30), (15, 60), (5, 60), (1, 60), (3, 15)]
EX_SETUP_TFS = [2, 3, 5]
SEEDS = int(os.getenv("SEEDS", "12"))


def ext_1m(df1):
    hm = df1.index.hour * 100 + df1.index.minute
    return df1[(hm >= 400) & (hm < 2000)]


def tf_state_at_close(df1x, chart_index, chart_tf, mins, fast=13, slow=34):
    """Trend (+1/-1) of the last `mins` candle CLOSED by the time the chart candle closes (no lookahead)."""
    c = df1x["close"].groupby(df1x.index.floor(f"{mins}min")).last()
    s = np.where(c.ewm(span=fast, adjust=False).mean() > c.ewm(span=slow, adjust=False).mean(), 1, -1)
    hs = pd.DataFrame({"end": c.index + pd.Timedelta(minutes=mins), "s": s})
    bars = pd.DataFrame({"t": chart_index + pd.Timedelta(minutes=chart_tf)})
    m = pd.merge_asof(bars, hs, left_on="t", right_on="end", direction="backward")
    return m["s"].fillna(0).astype(int).to_numpy()


def daily_levels(df1, chart_df):
    """Yesterday's RTH high / low / close, today's RTH open, daily ATR - mapped onto every chart candle."""
    hm1 = df1.index.hour * 100 + df1.index.minute
    rth = df1[(hm1 >= 930) & (hm1 < 1600)]
    g = rth.groupby(rth.index.date)
    d = pd.DataFrame({"o": g["open"].first(), "h": g["high"].max(), "l": g["low"].min(), "c": g["close"].last()})
    pc = d["c"].shift(1)
    tr = pd.concat([d["h"] - d["l"], (d["h"] - pc).abs(), (d["l"] - pc).abs()], axis=1).max(axis=1)
    k = pd.DataFrame({"pdh": d["h"].shift(1), "pdl": d["l"].shift(1), "pdc": pc, "dopen": d["o"],
                      "datr": tr.ewm(alpha=1 / 14, adjust=False).mean().shift(1)})
    return k.reindex(pd.Index(chart_df.index.date))


def first_per_day(cond, day):
    cond = pd.Series(np.asarray(cond, dtype=bool))
    n = cond.astype(int).groupby(np.asarray(day)).cumsum()
    return (cond & (n == 1)).to_numpy()


def setup_signals(name, df, ind, lv, tf):
    c, h, l, hm, day = ind["c"], ind["h"], ind["l"], ind["hm"], ind["day"]
    vw = ind["vwap"]
    close_hm = hm + tf  # rough HHMM of the candle close (minutes < 60 assumed only for window tests below)
    rth = (hm >= 930) & (hm < 1600)
    win = (hm >= 935) & (hm < 1530)
    ent = np.zeros(len(c), dtype=np.int64)
    if name.startswith("ORB"):
        mins = 15 if name == "ORB15" else 30
        end_hm = 945 if mins == 15 else 1000
        in_or = (hm >= 930) & (hm < end_hm)
        s = pd.DataFrame({"h": np.where(in_or, h, np.nan), "l": np.where(in_or, l, np.nan), "d": day})
        orh = s.groupby("d")["h"].transform("max").to_numpy()
        orl = s.groupby("d")["l"].transform("min").to_numpy()
        ok = (hm >= end_hm) & (hm < 1200)
        up = first_per_day(ok & (c > orh), day)
        dn = first_per_day(ok & (c < orl), day)
        ent[up] = 1
        ent[dn & ~up] = -1
    elif name == "VWAP reclaim":
        below = c < vw
        same = np.r_[False, day[1:] == day[:-1]]
        run = pd.Series(below).groupby((pd.Series(below) != pd.Series(below).shift()).cumsum()).cumcount().to_numpy() + 1
        prev_run = np.r_[0, run[:-1]]
        prev_below = np.r_[False, below[:-1]]
        ok = win & same & (hm >= 945)
        ent[ok & ~below & prev_below & (prev_run >= 5)] = 1
        ent[ok & below & ~prev_below & (prev_run >= 5)] = -1
    elif name == "Yesterday high/low BREAKOUT":
        pdh, pdl = lv["pdh"].to_numpy(), lv["pdl"].to_numpy()
        up = first_per_day(win & (c > pdh), day)
        dn = first_per_day(win & (c < pdl), day)
        ent[up] = 1
        ent[dn & ~up] = -1
    elif name == "Yesterday high/low REJECTION":
        pdh, pdl = lv["pdh"].to_numpy(), lv["pdl"].to_numpy()
        sh = first_per_day(win & (h > pdh) & (c < pdh), day)
        lg = first_per_day(win & (l < pdl) & (c > pdl), day)
        ent[lg] = 1
        ent[sh & ~lg] = -1
    elif name == "Gap fade":
        gap = (lv["dopen"].to_numpy() - lv["pdc"].to_numpy()) / lv["datr"].to_numpy()
        first = first_per_day((hm >= 935) & rth, day)
        ent[first & (gap > 0.3)] = -1
        ent[first & (gap < -0.3)] = 1
    return ent


SETUPS = ["ORB15", "ORB30", "VWAP reclaim", "Yesterday high/low BREAKOUT", "Yesterday high/low REJECTION", "Gap fade"]


def explore_main():
    end = datetime.now(timezone.utc) - timedelta(days=1)
    start = datetime.fromisoformat(START).replace(tzinfo=timezone.utc)
    test = os.getenv("TEST", "") == "1"
    os.makedirs(OUT, exist_ok=True)
    split = pd.Timestamp(SPLIT, tz=NY)
    R = {}        # (block, config, chart_tf) -> {(sym, per): stats}
    BASE = {}     # (sym, tf, per) -> coin-flip hit1 mean
    t0 = time.time()

    def grade(key, sym, ind, ent, times, yrs):
        g = grade_entries(ind, ent, times)
        tr, te = g[g["t"] < split], g[g["t"] >= split]
        R.setdefault(key, {})[(sym, "tr")] = q_stats(tr, yrs[0])
        R[key][(sym, "te")] = q_stats(te, yrs[1])

    for sym in SYMBOLS:
        print(f"\n=== {sym} ===", flush=True)
        df1, feed = fake_1m(sym, start, end) if test else fetch_1m(sym, start, end)
        df1x = ext_1m(df1)
        for tf in sorted(set(EX_TFS) | set(EX_AGREE_CHARTS) | set(EX_SETUP_TFS)):
            df = to_tf(df1, rth_only=False, mins=tf)
            hm = (df.index.hour * 100 + df.index.minute).to_numpy()
            rth = (hm >= 930) & (hm < 1600)
            dates = np.array(sorted(set(pd.Index(df.index.date)[rth])))
            yrs = (max((dates < split.date()).sum() / 252.0, 1e-9), max((dates >= split.date()).sum() / 252.0, 1e-9))
            p0 = dict(V30, allowL=None)
            base_ind = indicators(df, 13, 34, True)
            _, ent_v3 = signals(base_ind, p0)
            # coin-flip luck line: same entry times, random direction
            rng = np.random.default_rng(100 + tf)
            hits = {"tr": [], "te": []}
            nz = ent_v3 != 0
            for _ in range(SEEDS):
                e = np.zeros_like(ent_v3)
                e[nz] = rng.choice([-1, 1], size=int(nz.sum()))
                g = grade_entries(base_ind, e, df.index)
                hits["tr"].append(100 * g[g["t"] < split]["hit1"].mean())
                hits["te"].append(100 * g[g["t"] >= split]["hit1"].mean())
            for per in ("tr", "te"):
                BASE[(sym, tf, per)] = float(np.mean(hits[per]))
            print(f"  {sym} {tf}m: {len(df):,} candles | coin-flip +1 before -1: "
                  f"{BASE[(sym, tf, 'tr')]:.1f}% / {BASE[(sym, tf, 'te')]:.1f}%  ({time.time() - t0:.0f}s)", flush=True)
            # A. timeframe x line setting, normal and faded
            if tf in EX_TFS:
                for fs in EX_EMAS:
                    ind = base_ind if fs == (13, 34) else indicators(df, fs[0], fs[1], True)
                    _, ent = (None, ent_v3) if fs == (13, 34) else signals(ind, p0)
                    grade(("A", f"EMA {fs[0]}/{fs[1]}", tf), sym, ind, ent, df.index, yrs)
                    grade(("A", f"EMA {fs[0]}/{fs[1]} FADED", tf), sym, ind, -ent, df.index, yrs)
            # B. timeframe agreement (EMA 13/34 line + Vix Fix as v3.0)
            if tf in EX_AGREE_CHARTS:
                grade(("B", "no agreement filter", tf), sym, base_ind, ent_v3, df.index, yrs)
                states = {m: tf_state_at_close(df1x, df.index, tf, m) for m in EX_HTFS if m != tf}
                sets = [(m,) for m in states] + [pr for pr in EX_PAIRS if tf not in pr]
                for st_ in sets:
                    aL = np.ones(len(df), dtype=bool)
                    aS = np.ones(len(df), dtype=bool)
                    for m in st_:
                        aL &= states[m] == 1
                        aS &= states[m] == -1
                    _, ent = signals(base_ind, dict(V30, allowL=aL, allowS=aS))
                    nm = " + ".join(("1h" if m == 60 else f"{m}m") for m in st_) + " agree"
                    grade(("B", nm, tf), sym, base_ind, ent, df.index, yrs)
            # C. other setups
            if tf in EX_SETUP_TFS:
                lv = daily_levels(df1, df)
                for su in SETUPS:
                    ent = setup_signals(su, df, base_ind, lv, tf)
                    grade(("C", su, tf), sym, base_ind, ent, df.index, yrs)
                    grade(("C", su + " FADED", tf), sym, base_ind, -ent, df.index, yrs)
            del df, base_ind
        del df1, df1x

    syms = SYMBOLS
    cells = [(s_, p_) for s_ in syms for p_ in ("tr", "te")]

    def row(key):
        blk, nm, tf = key
        r = R[key]
        edges, zs = [], []
        for (s_, p_) in cells:
            st = r.get((s_, p_), {})
            n, h1 = st.get("n", 0), st.get("hit1", np.nan)
            b = BASE[(s_, tf, p_)]
            if n == 0 or np.isnan(h1):
                edges.append(np.nan)
                zs.append(np.nan)
                continue
            edges.append(h1 - b)
            zs.append((h1 - b) / (100 * np.sqrt(0.25 / n)))
        per_yr = np.mean([r[(s_, "tr")]["per_yr"] + 0 for s_ in syms if (s_, "tr") in r])
        per_yr_te = np.mean([r[(s_, "te")]["per_yr"] for s_ in syms if (s_, "te") in r])
        r2 = [r[c_]["r2"] for c_ in cells if c_ in r and r[c_]["n"]]
        r1 = [r[c_]["r1"] for c_ in cells if c_ in r and r[c_]["n"]]
        e = np.array(edges, dtype=float)
        z = np.array(zs, dtype=float)
        return dict(key=key, name=nm, tf=tf, blk=blk, per_yr=(per_yr + per_yr_te) / 2, edges=e, worst=np.nanmin(e) if np.isfinite(e).any() else -99,
                    mean=np.nanmean(e) if np.isfinite(e).any() else -99, pos=int(np.nansum(e > 0)), zmin=np.nanmin(z) if np.isfinite(z).any() else -99,
                    r1=np.mean(r1) if r1 else np.nan, r2=np.mean(r2) if r2 else np.nan,
                    h=[r.get(c_, {}).get("hit1", np.nan) for c_ in cells])

    rows = [row(k) for k in R]
    for x in rows:
        x["real"] = x["pos"] == len(cells) and x["zmin"] >= 1.0 and x["per_yr"] >= 20

    def tab(rs, title, note=""):
        out = [f"### {title}"]
        if note:
            out.append(note)
        hdr = " | ".join(f"{s_} {'20-23' if p_ == 'tr' else '24-now'}" for s_, p_ in cells)
        out += [f"| Setup | Chart | Trades/yr per symbol | +1 before -1: {hdr} | Edge vs coin flip (worst / avg) | Cells above coin flip | 1:1 ATR/trade | 1:2 ATR/trade | Real? |",
                "|---|---|---|" + "---|" * len(cells) + "---|---|---|---|---|"]
        for x in rs:
            hs = " | ".join("-" if np.isnan(v) else f"{v:.1f}%" for v in x["h"])
            out.append(f"| {x['name']} | {x['tf']}m | {x['per_yr']:.0f} | {hs} | **{x['worst']:+.1f}** / {x['mean']:+.1f} | "
                       f"{x['pos']}/{len(cells)} | {x['r1']:+.3f} | {x['r2']:+.3f} | {'✅' if x['real'] else ''} |")
        return out + [""]

    A = sorted([x for x in rows if x["blk"] == "A"], key=lambda x: -x["worst"])
    B = [x for x in rows if x["blk"] == "B"]
    C = sorted([x for x in rows if x["blk"] == "C"], key=lambda x: -x["worst"])
    reals = sorted([x for x in rows if x["real"]], key=lambda x: -x["worst"])
    best_tf = {}
    for tf in EX_TFS:
        cand = [x for x in A if x["tf"] == tf and "FADED" not in x["name"]]
        if cand:
            best_tf[tf] = max(cand, key=lambda x: x["worst"])
    agree_best = {}
    for tf in EX_AGREE_CHARTS:
        cand = sorted([x for x in B if x["tf"] == tf], key=lambda x: -x["worst"])
        if cand:
            agree_best[tf] = cand
    base_lines = [f"{s_} {tf}m: {BASE[(s_, tf, 'tr')]:.1f}% / {BASE[(s_, tf, 'te')]:.1f}%" for s_ in syms for tf in EX_TFS if (s_, tf, 'tr') in BASE]

    md = [f"# Trend Flip EXPLORE - {datetime.now(NY):%Y-%m-%d %H:%M} ET",
          f"Data {START} to {end:%Y-%m-%d}, {', '.join(syms)}. Entry-quality grade: does price go +1 ATR your way before 1 ATR against "
          "(next 30 candles, same candle = loss)? DATA ONLY - no orders. Runtime "
          f"{(time.time() - t0) / 60:.0f} min.", "",
          "**Luck line (real data):** the v3.0 entry times with a COIN-FLIP direction. Edge = result minus that. "
          "✅ Real = above the coin flip on SPY and QQQ in BOTH 2020-23 and 2024-now, by at least 1 standard error in every cell, "
          "20+ trades a year. Coin-flip rates (2020-23 / 2024-now): " + "; ".join(base_lines), "",
          "## The answer in 30 seconds",
          f"- **Ideas that beat the coin flip everywhere: {len(reals)} of {len(rows)}**" + (
              ": " + "; ".join(f"{x['name']} on {x['tf']}m (worst {x['worst']:+.1f} pts)" for x in reals[:8]) if reals else
              " - none. Nothing tested here has a reliable direction edge."),
          "- Best line setting per chart (worst-cell edge): " + "; ".join(
              f"{tf}m = {x['name']} ({x['worst']:+.1f})" for tf, x in best_tf.items()),
          "- Best timeframe agreement per chart: " + "; ".join(
              f"{tf}m = {c[0]['name']} ({c[0]['worst']:+.1f}, vs none {next((y['worst'] for y in c if y['name'] == 'no agreement filter'), float('nan')):+.1f})"
              for tf, c in agree_best.items()),
          f"- Best other setup: {C[0]['name']} on {C[0]['tf']}m ({C[0]['worst']:+.1f})" if C else "", ""]
    if reals:
        md += tab(reals, "Everything that beat the coin flip in all 4 cells")
    md += tab(A, "A. Chart timeframe x line setting (v3.0 rules), and faded (sorted by worst cell)")
    md += ["## B. Which timeframes should agree? (per chart, sorted by worst cell)"]
    for tf, c in agree_best.items():
        md += tab(c, f"{tf}-minute chart")
    md += tab(C, "C. Other setups, and faded (sorted by worst cell)",
              "ORB = first close beyond the 9:30-9:45 (15) or 9:30-10:00 (30) high/low, until 12:00. VWAP reclaim = close back "
              "across VWAP after 5+ closes on the other side. Breakout = first close beyond yesterday's high/low. Rejection = "
              "wick beyond yesterday's high/low but close back inside -> trade back in. Gap fade = gap over 0.3 daily ATR, trade "
              "toward yesterday's close at 9:35+.")
    text = "\n".join(md)
    print("\n" + text)
    stamp = datetime.now(NY).strftime("%Y-%m-%d")
    for path in (f"{OUT}/explore_{stamp}.md", f"{OUT}/explore_latest.md"):
        with open(path, "w") as f:
            f.write(text + "\n")
    summ = os.getenv("GITHUB_STEP_SUMMARY")
    if summ:
        with open(summ, "a") as f:
            f.write(text + "\n")


# ================================================================ STOPS & TARGETS GRID (MODE=brackets, the default)
# For v3.0 and the three leads from the explore run, every target / stop combination (in ATR of the chart):
#   +1/-1, +1/-2, +1/-3, +2/-2, +3/-3, +2/-1, +3/-1, 3 ATR stop + hold to 15:55, and NO stop + hold to 15:55.
# Each trade may run until 15:55 the same day (unresolved = closed then). Target and stop on the same candle = loss.
# One trade at a time. Win rate is shown next to the BREAKEVEN win rate (stop / (target + stop)).
# Coin flip = the same entry times with a random direction (6x). Edge = ATR per trade minus the coin flip's.
# Real = edge above zero on SPY and QQQ, 2020-23 and 2024-now (4/4), by at least 1 standard error in every cell.
BRACKETS = [(1, 1), (1, 2), (1, 3), (2, 2), (3, 3), (2, 1), (3, 1), (None, 3), (None, None)]
BR_SEEDS = int(os.getenv("BR_SEEDS", "6"))


def br_name(b):
    t, s_ = b
    if t is None and s_ is None:
        return "NO stop, hold to 15:55"
    if t is None:
        return f"-{s_} stop, hold to 15:55"
    return f"+{t} target / -{s_} stop"


def grade_brackets(ind, ent, times, flat=1555):
    """Returns {bracket: DataFrame(t, win, r)} - each bracket keeps its own one-trade-at-a-time state."""
    o, h, l, c, atr, hm, day = ind["o"], ind["h"], ind["l"], ind["c"], ind["atr"], ind["hm"], ind["day"]
    n = len(o)
    busy = {b: -1 for b in BRACKETS}
    rows = {b: [] for b in BRACKETS}
    # last bar index of each day before the flat time
    for i in np.nonzero(ent)[0]:
        e = i + 1
        if e >= n or day[e] != day[i] or hm[e] >= flat:
            continue
        a = atr[i]
        if not a or np.isnan(a):
            continue
        j = e
        while j + 1 < n and day[j + 1] == day[e] and hm[j + 1] < flat:
            j += 1
        sd, en = int(ent[i]), o[e]
        fav = ((h[e:j + 1] - en) if sd == 1 else (en - l[e:j + 1])) / a
        adv = ((en - l[e:j + 1]) if sd == 1 else (h[e:j + 1] - en)) / a
        fin = sd * (c[j] - en) / a
        for b in BRACKETS:
            if e <= busy[b]:
                continue
            t, st = b
            hs = np.nonzero(adv >= st)[0] if st is not None else np.array([], dtype=int)
            ht = np.nonzero(fav >= t)[0] if t is not None else np.array([], dtype=int)
            ks = hs[0] if len(hs) else 10**9
            kt = ht[0] if len(ht) else 10**9
            if ks == 10**9 and kt == 10**9:
                r, win, k = fin, int(fin > 0), len(fav) - 1
            elif ks <= kt:
                r, win, k = -float(st), 0, ks
            else:
                r, win, k = float(t), 1, kt
            busy[b] = e + k
            rows[b].append((times[e], win, r))
    return {b: pd.DataFrame(v, columns=["t", "win", "r"]) for b, v in rows.items()}


def brackets_main():
    end = datetime.now(timezone.utc) - timedelta(days=1)
    start = datetime.fromisoformat(START).replace(tzinfo=timezone.utc)
    test = os.getenv("TEST", "") == "1"
    os.makedirs(OUT, exist_ok=True)
    split = pd.Timestamp(SPLIT, tz=NY)
    t0 = time.time()
    SETS = [("v3.0", 2), ("v3.0", 3), ("v3.0 + 30m agrees", 2), ("v3.0 + 15m & 1h agree", 3),
            ("Gap and go", 2), ("Gap and go", 5), ("Yesterday high/low breakout", 2), ("Yesterday high/low breakout", 5)]
    RES = {}   # (setup, tf, bracket) -> {(sym, per): dict(n, per_yr, win, r, se, coin)}
    for sym in SYMBOLS:
        print(f"\n=== {sym} ===", flush=True)
        df1, feed = fake_1m(sym, start, end) if test else fetch_1m(sym, start, end)
        df1x = ext_1m(df1)
        for tf in sorted(set(t for _, t in SETS)):
            df = to_tf(df1, rth_only=False, mins=tf)
            hm = (df.index.hour * 100 + df.index.minute).to_numpy()
            rth = (hm >= 930) & (hm < 1600)
            dates = np.array(sorted(set(pd.Index(df.index.date)[rth])))
            yrs = {"tr": max((dates < split.date()).sum() / 252.0, 1e-9), "te": max((dates >= split.date()).sum() / 252.0, 1e-9)}
            ind = indicators(df, 13, 34, True)
            lv = daily_levels(df1, df)
            for name, stf in SETS:
                if stf != tf:
                    continue
                if name == "v3.0":
                    _, ent = signals(ind, dict(V30, allowL=None))
                elif name == "v3.0 + 30m agrees":
                    s30 = tf_state_at_close(df1x, df.index, tf, 30)
                    _, ent = signals(ind, dict(V30, allowL=s30 == 1, allowS=s30 == -1))
                elif name == "v3.0 + 15m & 1h agree":
                    a15, a60 = tf_state_at_close(df1x, df.index, tf, 15), tf_state_at_close(df1x, df.index, tf, 60)
                    _, ent = signals(ind, dict(V30, allowL=(a15 == 1) & (a60 == 1), allowS=(a15 == -1) & (a60 == -1)))
                elif name == "Gap and go":
                    ent = -setup_signals("Gap fade", df, ind, lv, tf)
                else:
                    ent = setup_signals("Yesterday high/low BREAKOUT", df, ind, lv, tf)
                real = grade_brackets(ind, ent, df.index)
                rng = np.random.default_rng(7 + tf)
                nz = ent != 0
                coins = []
                for _ in range(BR_SEEDS):
                    e2 = np.zeros_like(ent)
                    e2[nz] = rng.choice([-1, 1], size=int(nz.sum()))
                    coins.append(grade_brackets(ind, e2, df.index))
                for b in BRACKETS:
                    g = real[b]
                    for per in ("tr", "te"):
                        gp = g[g["t"] < split] if per == "tr" else g[g["t"] >= split]
                        cp = []
                        for cg in coins:
                            x = cg[b]
                            x = x[x["t"] < split] if per == "tr" else x[x["t"] >= split]
                            if len(x):
                                cp.append(x["r"].mean())
                        RES.setdefault((name, tf, b), {})[(sym, per)] = dict(
                            n=len(gp), per_yr=len(gp) / yrs[per], win=100 * gp["win"].mean() if len(gp) else np.nan,
                            r=gp["r"].mean() if len(gp) else np.nan,
                            se=gp["r"].std(ddof=1) / np.sqrt(len(gp)) if len(gp) > 1 else np.nan,
                            coin=float(np.mean(cp)) if cp else np.nan)
                print(f"  {sym} {tf}m {name}: {int(nz.sum())} signals ({time.time() - t0:.0f}s)", flush=True)
        del df1, df1x

    cells = [(s_, p_) for s_ in SYMBOLS for p_ in ("tr", "te")]
    rows = []
    for (name, tf, b), r in RES.items():
        edges = [r[c_]["r"] - r[c_]["coin"] for c_ in cells]
        zs = [(r[c_]["r"] - r[c_]["coin"]) / r[c_]["se"] if r[c_]["se"] and not np.isnan(r[c_]["se"]) and r[c_]["se"] > 0 else np.nan for c_ in cells]
        e = np.array(edges, dtype=float)
        z = np.array(zs, dtype=float)
        t_, s_ = b
        be = 100 * s_ / (t_ + s_) if t_ is not None and s_ is not None else np.nan
        rows.append(dict(name=name, tf=tf, b=b, r=r, e=e, worst=np.nanmin(e), avg=np.nanmean(e), pos=int(np.nansum(e > 0)),
                         zmin=np.nanmin(z), be=be, win=np.nanmean([r[c_]["win"] for c_ in cells]),
                         exp=[r[c_]["r"] for c_ in cells], per_yr=np.nanmean([r[c_]["per_yr"] for c_ in cells]),
                         real=bool(np.all(e > 0) and np.nanmin(z) >= 1.0)))
    reals = sorted([x for x in rows if x["real"]], key=lambda x: -x["worst"])
    hdr = " | ".join(f"{s_} {'20-23' if p_ == 'tr' else '24-now'}" for s_, p_ in cells)

    def tab(rs):
        out = [f"| Target / stop | Trades/yr per symbol | Win rate (avg) | Breakeven win rate | ATR per trade: {hdr} | Edge vs coin flip (worst / avg) | Real? |",
               "|---|---|---|---|" + "---|" * len(cells) + "---|---|"]
        for x in rs:
            ex = " | ".join(f"{v:+.3f}" for v in x["exp"])
            out.append(f"| {br_name(x['b'])} | {x['per_yr']:.0f} | {x['win']:.1f}% | {'-' if np.isnan(x['be']) else f'{x[chr(98) + chr(101)]:.1f}%'} | {ex} | "
                       f"**{x['worst']:+.3f}** / {x['avg']:+.3f} | {'✅' if x['real'] else ''} |")
        return out + [""]

    by_setup = {}
    for x in rows:
        by_setup.setdefault((x["name"], x["tf"]), []).append(x)
    best_each = {k: max(v, key=lambda x: x["worst"]) for k, v in by_setup.items()}
    md = [f"# Trend Flip STOPS & TARGETS - {datetime.now(NY):%Y-%m-%d %H:%M} ET",
          f"Data {START} to {end:%Y-%m-%d}, {', '.join(SYMBOLS)}. Runtime {(time.time() - t0) / 60:.0f} min. DATA ONLY - no orders.",
          "Targets and stops are in ATR of the chart. A trade may run until 15:55 the same day. ATR per trade = average result. "
          "Coin flip = same entry times, random direction. Edge = ATR per trade minus the coin flip. "
          "✅ Real = edge above zero in all 4 cells (SPY/QQQ x 2020-23/2024-now) by at least 1 standard error.", "",
          "## The answer in 30 seconds",
          f"- **Target/stop combinations that beat the coin flip everywhere: {len(reals)} of {len(rows)}**" + (
              ": " + "; ".join(f"{x['name']} {x['tf']}m with {br_name(x['b'])} (worst edge {x['worst']:+.3f} ATR)" for x in reals[:8])
              if reals else " - none. No stop or target turns these entries into an edge."),
          "- Best target/stop for each setup (by worst cell): " + "; ".join(
              f"{k[0]} {k[1]}m = {br_name(v['b'])} ({v['worst']:+.3f} / avg {v['avg']:+.3f})" for k, v in best_each.items()),
          "- Read the win rate next to the breakeven win rate: a wide stop wins more often, but only matters if the win rate beats breakeven.", ""]
    if reals:
        md += ["## Everything that beat the coin flip in all 4 cells"] + tab(reals)
    for k, v in by_setup.items():
        md += [f"## {k[0]} - {k[1]}-minute chart"] + tab(v)
    text = "\n".join(md)
    print("\n" + text)
    stamp = datetime.now(NY).strftime("%Y-%m-%d")
    for path in (f"{OUT}/brackets_{stamp}.md", f"{OUT}/brackets_latest.md"):
        with open(path, "w") as f:
            f.write(text + "\n")
    summ = os.getenv("GITHUB_STEP_SUMMARY")
    if summ:
        with open(summ, "a") as f:
            f.write(text + "\n")


# ================================================================ TREND LINE STUDY (MODE=study, the default)
# Everything about the Trend Flip line on 1/2/3/5m charts, SPY + QQQ, 2020-now.
#  1. Line anatomy: how long green / red runs last, how many are chop, how far price moves during them.
#  2. Entry events (each also FADED): line turns green/red | red(pink) ends -> long, green(blue) ends -> short |
#     pink appears -> long, blue appears -> short | strong color returns after a warning.
#  3. ~30 conditions at every event: TTM squeeze state, TTM momentum size/slope/color/zero-cross, Vix Fix fear/greed
#     level, agreement of every other timeframe (1/2/3/5/15/30/60m), candle body/range, VWAP distance, slow-EMA slope,
#     previous run length, time of day, quiet day, gap and day direction, volatility.
#  4. Every event is graded BOTH ways (long and short) over the next 30 candles, so the coin flip is exact:
#     edge = (+1-before-1 rate your way - the same for the other way) / 2, in percentage points.
#  5. Confluence: up to 3 conditions picked on 2020-23 ONLY (best edge, enough trades), checked on 2024-now.
#  6. Exits for the winners: time, line color ends, opposite color, warning color, TTM momentum peak / zero cross,
#     +2/-1 bracket, 1 ATR trailing stop, hold to 15:55 (all with a 3 ATR safety stop).
ST_TFS = [int(x) for x in os.getenv("ST_TFS", "1,2,3,5").split(",")]
ST_HTFS = [1, 2, 3, 5, 15, 30, 60]
WIN = 30
EVENTS = ["Line turns GREEN (long) / RED (short)", "RED or PINK ends -> long / GREEN or BLUE ends -> short",
          "PINK appears -> long / BLUE appears -> short", "Strong color returns after a warning"]
EV_SHORT = ["Turns green/red", "Red/pink ends", "Pink/blue appears", "Strong again"]


def linreg_last(y, n=20):
    """Pine ta.linreg(y, n, 0): value of the least-squares line at the newest point of each window."""
    y = np.asarray(y, dtype=float)
    out = np.full(len(y), np.nan)
    if len(y) < n:
        return out
    x = np.arange(n, dtype=float)
    xm = x.mean()
    sxx = ((x - xm) ** 2).sum()
    yy = np.nan_to_num(y)
    sy = np.convolve(yy, np.ones(n), "valid")
    sxy = np.convolve(yy, x[::-1], "valid")        # sum_k x_k * y_(t-n+1+k)
    slope = (sxy - xm * sy) / sxx
    inter = sy / n - slope * xm
    vals = inter + slope * (n - 1)
    bad = pd.Series(np.isnan(y)).rolling(n).max().to_numpy()[n - 1:] > 0
    vals[bad] = np.nan
    out[n - 1:] = vals
    return out


def ttm_waves(m, keep=500):
    """Like the TTM Stretch Bands pane: typical (median) wave max per side from FINISHED waves only, wave age,
    and fresh turns (cyan->blue top / red->yellow bottom) on the last 2 bars."""
    from collections import deque
    n = len(m)
    typ = np.full(n, np.nan)
    age = np.zeros(n, dtype=np.int64)
    up, dn = deque(maxlen=keep), deque(maxlen=keep)
    med_up = med_dn = np.nan
    side, start, wmax = 0, 0, 0.0
    for i in range(n):
        v = m[i]
        if np.isnan(v):
            continue
        ns = 1 if v > 0 else -1
        if ns != side:
            if side == 1 and i - start >= 2:
                up.append(wmax)
                med_up = float(np.median(up))
            elif side == -1 and i - start >= 2:
                dn.append(wmax)
                med_dn = float(np.median(dn))
            side, start, wmax = ns, i, 0.0
        wmax = max(wmax, abs(v))
        typ[i] = med_up if ns == 1 else med_dn
        age[i] = i - start
    m1, m2 = np.r_[np.nan, m[:-1]], np.r_[np.nan, np.nan, m[:-2]]
    top = (m1 > 0) & (m1 > m2) & (m <= m1)
    bot = (m1 < 0) & (m1 < m2) & (m >= m1)
    top2, bot2 = top | np.r_[False, top[:-1]], bot | np.r_[False, bot[:-1]]
    turn = np.where(bot2, 1, np.where(top2, -1, 0))   # +1 = bottom turn (good for longs), -1 = top turn
    return typ, age, turn


def run_lengths(st):
    """Current run length (bars, incl. this one) and the previous run's length + value, for every bar."""
    st = np.asarray(st)
    n = len(st)
    cur = np.ones(n, dtype=np.int64)
    prev_len = np.zeros(n, dtype=np.int64)
    prev_val = np.zeros(n, dtype=np.int64)
    pl, pv = 0, 0
    for i in range(1, n):
        if st[i] == st[i - 1]:
            cur[i] = cur[i - 1] + 1
        else:
            pl, pv = cur[i - 1], st[i - 1]
        prev_len[i], prev_val[i] = pl, pv
    return cur, prev_len, prev_val


def study_arrays(df, df1, df1x, tf):
    ind = indicators(df, 13, 34, True)
    o, h, l, c, a, st, hm = ind["o"], ind["h"], ind["l"], ind["c"], ind["atr"], ind["st"], ind["hm"]
    fadeL = (st == 1) & ~ind["strongL"]
    fadeS = (st == -1) & ~ind["strongS"]
    color = np.where(st == 1, np.where(fadeL, 1, 2), np.where(st == -1, np.where(fadeS, -1, -2), 0))
    cs, hs, ls = df["close"], df["high"], df["low"]
    # TTM squeeze (LazyBear): BB 20/2 inside KC 20/1.5 ; momentum = linreg(close - avg(avg(HH20, LL20), SMA20), 20)
    basis = cs.rolling(20).mean()
    dev = 2.0 * cs.rolling(20).std(ddof=0)
    pc = cs.shift(1)
    tr = pd.concat([hs - ls, (hs - pc).abs(), (ls - pc).abs()], axis=1).max(axis=1)
    rma = tr.rolling(20).mean()
    sq_on = ((basis - dev) > (basis - 1.5 * rma)) & ((basis + dev) < (basis + 1.5 * rma))
    sq_on = sq_on.fillna(False).to_numpy()
    mid = ((hs.rolling(20).max() + ls.rolling(20).min()) / 2 + basis) / 2
    mom = linreg_last((cs - mid).to_numpy(), 20)
    mom_prev = np.r_[np.nan, mom[:-1]]
    since_sq = bars_since(sq_on)
    sq_state = np.where(sq_on, "in squeeze", np.where(since_sq <= 3, "fired 0-3 bars ago",
                                                       np.where(since_sq <= 10, "fired 4-10 bars ago", "no squeeze in 10+ bars")))
    sgn = np.sign(np.nan_to_num(mom))
    cross_dir = np.zeros(len(c), dtype=np.int64)
    for k in (1, 2, 3):
        prev = np.r_[[0] * k, sgn[:-k]]
        cross_dir = np.where((cross_dir == 0) & (sgn != 0) & (prev != 0) & (prev != sgn), sgn, cross_dir)
    # Vix Fix fear (wvf) / greed (wvi) and their level vs the spike line
    hc22, lc22 = cs.rolling(22).max(), cs.rolling(22).min()
    wvf = (hc22 - ls) / hc22 * 100
    wvi = (hs - lc22) / lc22 * 100

    def ratio(w):
        line = np.minimum(w.rolling(20).mean() + 2 * w.rolling(20).std(ddof=0), w.rolling(50).max() * 0.85)
        return (w / line.replace(0, np.nan)).to_numpy()
    cur_len, prev_len, prev_val = run_lengths(st)
    typ, wage, wturn = ttm_waves(mom / a)
    lv = daily_levels(df1, df)
    datr = lv["datr"].to_numpy()
    yr = ((lv["pdh"] - lv["pdl"]) / lv["datr"]).to_numpy()
    es = cs.ewm(span=34, adjust=False).mean().to_numpy()
    ef = cs.ewm(span=13, adjust=False).mean().to_numpy()
    a_norm = pd.Series(a).ewm(span=20 * int(390 / tf), adjust=False).mean().shift(1).to_numpy()
    F = dict(
        mom=mom / a, mslope=(mom - mom_prev) / a, cross_dir=cross_dir, sq_state=sq_state,
        fear_ratio=ratio(wvf), greed_ratio=ratio(wvi), fear_raw=wvf.to_numpy(), greed_raw=wvi.to_numpy(),
        fear_ago=bars_since(ind["fear"]), greed_ago=bars_since(ind["greed"] & ~ind["fear"]),
        fear_n=(wvf / wvf.rolling(50).max() * 100).to_numpy(), greed_n=(wvi / wvi.rolling(50).max() * 100).to_numpy(),
        stretch=np.abs(mom / a) / typ, wave_age=wage, turn=wturn,
        vwap=(c - ind["vwap"]) / a, gap=(lv["dopen"].to_numpy() - lv["pdc"].to_numpy()) / datr,
        daymove=(c - lv["dopen"].to_numpy()) / datr, es_slope=(es - np.r_[[np.nan] * 5, es[:-5]]) / a,
        body=(c - o) / a, crange=(h - l) / a, spread=(ef - es) / a, yrange=yr, atr_ratio=a / a_norm,
        cur_len=cur_len, prev_len=prev_len,
        tod=np.where(hm < 1030, "9:35-10:30", np.where(hm < 1200, "10:30-12:00", np.where(hm < 1400, "12:00-14:00", "14:00-15:30"))))
    for m in ST_HTFS:
        if m != tf:
            F[f"agree_{m}"] = tf_state_at_close(df1x, df.index, tf, m)
    return ind, color, F, mom


def find_events(st, color, hm):
    prev_st = np.r_[0, st[:-1]]
    prev_c = np.r_[0, color[:-1]]
    win = (hm >= 935) & (hm < 1530)
    ev = []
    e0 = np.where((st != 0) & (st != prev_st), st, 0)
    e1 = np.where((prev_st == -1) & (st != -1), 1, np.where((prev_st == 1) & (st != 1), -1, 0))
    e2 = np.where((color == -1) & (prev_c == -2), 1, np.where((color == 1) & (prev_c == 2), -1, 0))
    e3 = np.where((color == 2) & (prev_c == 1), 1, np.where((color == -2) & (prev_c == -1), -1, 0))
    for k, e in enumerate((e0, e1, e2, e3)):
        idx = np.nonzero(win & (e != 0))[0]
        ev.append((k, idx, e[idx]))
    return ev


def grade_two_sided(ind, idx, flat=1555):
    o, h, l, c, a, hm, day = ind["o"], ind["h"], ind["l"], ind["c"], ind["atr"], ind["hm"], ind["day"]
    n = len(o)
    out = np.full((len(idx), 7), np.nan)   # hitL, hitS, r2L, r2S, mfeL, mfeS, valid
    for q, i in enumerate(idx):
        e = i + 1
        if e >= n or day[e] != day[i] or hm[e] >= flat or not a[i] or np.isnan(a[i]):
            continue
        j = e
        last = min(n - 1, e + WIN - 1)
        while j < last and day[j + 1] == day[e] and hm[j + 1] < flat:
            j += 1
        en, at = o[e], a[i]
        up = (h[e:j + 1] - en) / at
        dn = (en - l[e:j + 1]) / at
        fin = (c[j] - en) / at

        def first(x, v):
            k = np.nonzero(x >= v)[0]
            return k[0] if len(k) else 10**9
        u1, d1, u2, d2 = first(up, 1), first(dn, 1), first(up, 2), first(dn, 2)
        hitL = 1.0 if u1 < d1 else 0.0
        hitS = 1.0 if d1 < u1 else 0.0
        r2L = 2.0 if u2 < d1 else (-1.0 if d1 <= u2 and d1 < 10**9 else fin)
        r2S = 2.0 if d2 < u1 else (-1.0 if u1 <= d2 and u1 < 10**9 else -fin)
        out[q] = (hitL, hitS, r2L, r2S, up.max(), dn.max(), 1)
    return out


def align(E, side):
    """Features as seen from the trade's side (+ = in your favor)."""
    s = side.astype(float)
    A = pd.DataFrame(index=E.index)
    A["TTM momentum size (ATR, + = your way)"] = E["mom"] * s
    A["TTM momentum slope (ATR, + = turning your way)"] = E["mslope"] * s
    mw, ms = A.iloc[:, 0], A.iloc[:, 1]
    A["TTM momentum color (vs your trade)"] = np.where(mw > 0, np.where(ms > 0, "with you + rising (cyan for longs)", "with you + fading (blue for longs)"),
                                                       np.where(ms < 0, "against you + falling (red for longs)", "against you + turning (yellow for longs)"))
    A["TTM squeeze"] = E["sq_state"]
    A["TTM momentum crossed zero your way in last 3 bars"] = np.where(E["cross_dir"].to_numpy() * s > 0, "yes", "no")
    A["Vix Fix spike level YOUR way (fear before long / greed before short; 1 = spike line)"] = np.where(s > 0, E["fear_ratio"], E["greed_ratio"])
    A["Vix Fix spike level AGAINST you (1 = spike line)"] = np.where(s > 0, E["greed_ratio"], E["fear_ratio"])
    A["Vix Fix raw number YOUR way"] = np.where(s > 0, E["fear_raw"], E["greed_raw"])
    A["VIX FIX pane bar YOUR way (0-100 as on your pane; red fear for longs, blue greed for shorts)"] = np.where(s > 0, E["fear_n"], E["greed_n"])
    A["VIX FIX pane bar AGAINST you (0-100)"] = np.where(s > 0, E["greed_n"], E["fear_n"])
    A["TTM stretch vs typical wave (1 = median full stretch; + = momentum your way, - = against)"] = np.sign(E["mom"].to_numpy() * s) * E["stretch"].to_numpy()
    A["TTM wave age (bars since momentum crossed zero)"] = E["wave_age"].astype(float)
    tv = E["turn"].to_numpy() * s
    A["TTM turn in the last 2 bars"] = np.where(tv > 0, "turned YOUR way (red>yellow before a long)", np.where(tv < 0, "turned AGAINST you (cyan>blue before a long)", "no fresh turn"))
    A["Candles since a Vix Fix spike YOUR way"] = np.where(s > 0, E["fear_ago"], E["greed_ago"]).astype(float)
    A["Distance from VWAP (ATR, + = your side)"] = E["vwap"] * s
    A["Opening gap (daily ATR, + = your way)"] = E["gap"] * s
    A["Day's move so far (daily ATR, + = your way)"] = E["daymove"] * s
    A["Slow EMA 34 slope (ATR per 5 bars, + = your way)"] = E["es_slope"] * s
    A["Signal candle body (ATR, + = your way)"] = E["body"] * s
    A["Signal candle range (ATR)"] = E["crange"]
    A["Fast-slow EMA gap (ATR, + = your way)"] = E["spread"] * s
    A["Yesterday's range (daily ATR; low = quiet day)"] = E["yrange"]
    A["Volatility now vs normal (ATR ratio)"] = E["atr_ratio"]
    A["Length of the current color run (bars)"] = E["cur_len"].astype(float)
    A["Length of the previous color run (bars)"] = E["prev_len"].astype(float)
    A["Time of day"] = E["tod"]
    for m in ST_HTFS:
        col = f"agree_{m}"
        if col in E:
            v = E[col].to_numpy(dtype=float) * s
            A[f"{'1h' if m == 60 else str(m) + 'm'} trend"] = np.where(np.isnan(E[col].to_numpy(dtype=float)), None,
                                                                      np.where(v > 0, "agrees", "disagrees"))
    A["edge"] = 50.0 * (np.where(s > 0, E["hitL"], E["hitS"]) - np.where(s > 0, E["hitS"], E["hitL"]))
    A["edge_r2"] = 0.5 * (np.where(s > 0, E["r2L"], E["r2S"]) - np.where(s > 0, E["r2S"], E["r2L"]))
    A["hit"] = 100 * np.where(s > 0, E["hitL"], E["hitS"])
    A["mfe"] = np.where(s > 0, E["mfeL"], E["mfeS"])
    for k in ("sym", "tf", "per", "t", "ev"):
        A[k] = E[k].to_numpy()
    return A


def rules_for(A, tr_mask):
    """Candidate conditions: category == value, or numeric >= / <= TRAIN quintile cuts."""
    out = []
    skip = {"edge", "edge_r2", "hit", "mfe", "sym", "tf", "per", "t", "ev"}
    for col in A.columns:
        if col in skip:
            continue
        v = A[col]
        if not pd.api.types.is_numeric_dtype(v):
            for val in sorted(set(v[tr_mask].dropna())):
                out.append((f"{col} = {val}", (v == val).to_numpy()))
        else:
            x = v.to_numpy(dtype=float)
            qs = np.unique(np.round(np.nanquantile(x[tr_mask], [0.2, 0.4, 0.6, 0.8]), 3))
            for q in qs:
                out.append((f"{col} >= {q:g}", np.nan_to_num(x, nan=-1e18) >= q))
                out.append((f"{col} <= {q:g}", np.nan_to_num(x, nan=1e18) <= q))
    return out


def cell_edges(A, mask, by=("sym", "per")):
    g = A[mask].groupby(list(by))["edge"]
    return g.mean(), g.count(), g.std(ddof=1)


def study_exits(ind, color, mom, idx, side, flat=1555):
    """ATR result of each exit rule for given entries (entry = next open, 3 ATR safety stop, flat 15:55)."""
    o, h, l, c, a, hm, day, st = ind["o"], ind["h"], ind["l"], ind["c"], ind["atr"], ind["hm"], ind["day"], ind["st"]
    n = len(o)
    names = ["Time 5 candles", "Time 10 candles", "Time 15 candles", "Time 30 candles", "Line leaves your color",
             "Opposite color starts", "Warning color (blue/pink) or color ends", "TTM momentum peaks (turns against you)",
             "TTM momentum crosses zero against you", "+2 / -1 ATR bracket", "1 ATR trailing stop (on closes)", "Hold to 15:55"]
    res = np.full((len(idx), len(names)), np.nan)
    momp = np.r_[np.nan, mom[:-1]]
    for q, (i, sd) in enumerate(zip(idx, side)):
        e = i + 1
        if e >= n or day[e] != day[i] or hm[e] >= flat or not a[i] or np.isnan(a[i]):
            continue
        en, at = o[e], a[i]
        stop = en - sd * 3 * at
        best = en
        done = [False] * len(names)
        j = e
        while True:
            last = (j + 1 >= n) or day[j + 1] != day[e] or hm[j + 1] >= flat
            held = j - e + 1
            hit_stop = (l[j] <= stop) if sd == 1 else (h[j] >= stop)
            stop_px = min(o[j], stop) if sd == 1 else max(o[j], stop)
            best = max(best, c[j]) if sd == 1 else min(best, c[j])
            r_close = sd * (c[j] - en) / at
            for k in range(len(names)):
                if done[k]:
                    continue
                if k == 9:   # bracket +2/-1 (intrabar, stop first)
                    up = sd * ((h[j] if sd == 1 else l[j]) - en) / at
                    dn = sd * (en - (l[j] if sd == 1 else h[j])) / at
                    if dn >= 1:
                        res[q, k], done[k] = -1.0, True
                    elif up >= 2:
                        res[q, k], done[k] = 2.0, True
                    elif last:
                        res[q, k], done[k] = r_close, True
                    continue
                if hit_stop:
                    res[q, k], done[k] = sd * (stop_px - en) / at, True
                    continue
                cond = False
                if k <= 3:
                    cond = held >= (5, 10, 15, 30)[k]
                elif k == 4:
                    cond = st[j] != sd
                elif k == 5:
                    cond = st[j] == -sd
                elif k == 6:
                    cond = color[j] != 2 * sd
                elif k == 7:
                    cond = held >= 2 and sd * (mom[j] - momp[j]) < 0
                elif k == 8:
                    cond = sd * mom[j] < 0 and held >= 2
                elif k == 10:
                    cond = sd * (best - c[j]) >= at
                if cond or last:
                    res[q, k], done[k] = r_close, True
            if all(done) or last:
                break
            j += 1
    return names, res


def study_main():
    end = datetime.now(timezone.utc) - timedelta(days=1)
    start = datetime.fromisoformat(START).replace(tzinfo=timezone.utc)
    test = os.getenv("TEST", "") == "1"
    os.makedirs(OUT, exist_ok=True)
    split = pd.Timestamp(SPLIT, tz=NY)
    t0 = time.time()
    rows, anat, keep = [], [], {}
    years = {}
    for sym in SYMBOLS:
        print(f"\n=== {sym} ===", flush=True)
        df1, feed = fake_1m(sym, start, end) if test else fetch_1m(sym, start, end)
        df1x = ext_1m(df1)
        for tf in ST_TFS:
            df = to_tf(df1, rth_only=False, mins=tf)
            ind, color, F, mom = study_arrays(df, df1, df1x, tf)
            st, hm, c, a = ind["st"], ind["hm"], ind["c"], ind["atr"]
            rth = (hm >= 930) & (hm < 1600)
            dates = np.array(sorted(set(pd.Index(df.index.date)[rth])))
            years[(sym, tf, "tr")] = max((dates < split.date()).sum() / 252.0, 1e-9)
            years[(sym, tf, "te")] = max((dates >= split.date()).sum() / 252.0, 1e-9)
            # ---- line anatomy (runs of green / red that start in RTH)
            cur, _, _ = run_lengths(st)
            ends = np.nonzero(np.r_[st[1:] != st[:-1], True])[0]
            for e_ in ends:
                ln = int(cur[e_])
                s0 = e_ - ln + 1
                if st[e_] == 0 or not rth[s0] or s0 == 0:
                    continue
                move = st[e_] * (c[e_] - c[s0]) / a[s0] if a[s0] else np.nan
                best = ((ind["h"][s0:e_ + 1].max() - c[s0]) if st[e_] == 1 else (c[s0] - ind["l"][s0:e_ + 1].min())) / a[s0]
                anat.append((sym, tf, "GREEN" if st[e_] == 1 else "RED", ln, ln * tf, move, best))
            # ---- events
            for k, idx, side in find_events(st, color, hm):
                g = grade_two_sided(ind, idx)
                ok = ~np.isnan(g[:, 6])
                idx, side, g = idx[ok], side[ok], g[ok]
                E = pd.DataFrame({key: (val[idx] if isinstance(val, np.ndarray) else np.asarray(val)[idx]) for key, val in F.items()})
                E["hitL"], E["hitS"], E["r2L"], E["r2S"], E["mfeL"], E["mfeS"] = g[:, 0], g[:, 1], g[:, 2], g[:, 3], g[:, 4], g[:, 5]
                E["side"] = side
                E["sym"], E["tf"], E["ev"] = sym, tf, k
                E["t"] = df.index[idx]
                E["per"] = np.where(E["t"] < split, "tr", "te")
                E["i"] = idx
                rows.append(E)
            keep[(sym, tf)] = (ind, color, mom)
            print(f"  {sym} {tf}m: {len(df):,} candles ({time.time() - t0:.0f}s)", flush=True)
        del df1, df1x
    E = pd.concat(rows, ignore_index=True)
    cells = [(s_, p_) for s_ in SYMBOLS for p_ in ("tr", "te")]
    pname = {"tr": f"{START[:4]}-{int(SPLIT[:4]) - 1}", "te": f"{SPLIT[:4]}-now"}

    def fmt_cells(m, cnt=None):
        return " | ".join((f"{m.get(c_, np.nan):+.1f}" if c_ in m.index else "-") for c_ in cells)

    md = [f"# TREND LINE STUDY - {datetime.now(NY):%Y-%m-%d %H:%M} ET",
          f"Data {START} to {end:%Y-%m-%d}, {', '.join(SYMBOLS)}, {', '.join(f'{t}m' for t in ST_TFS)}. DATA ONLY - no orders. Runtime {{RT}} min.",
          "**Edge** = how much more often price went +1 ATR YOUR way before 1 ATR against, than the other way, at the same moment "
          "(percentage points, over the next 30 candles; 0 = coin flip). Half of the difference, so +5 means e.g. 55% vs 45%. "
          "**R** = the same idea for a +2 / -1 ATR bracket, in ATR per trade. "
          f"TRAIN = {pname['tr']} (everything is picked here). TEST = {pname['te']} (never used to pick).", ""]

    # ---- 1. anatomy
    AN = pd.DataFrame(anat, columns=["sym", "tf", "col", "bars", "mins", "move", "best"])
    md += ["## 1. Line anatomy - how long green and red runs last (runs starting 9:30-16:00)",
           "| Chart | Color | Runs | Median length | 80% are shorter than | Chop (2 bars or less) | 10+ bars | Avg move start->end (ATR) | Avg best move (ATR) |",
           "|---|---|---|---|---|---|---|---|---|"]
    for tf in ST_TFS:
        for col in ("GREEN", "RED"):
            x = AN[(AN["tf"] == tf) & (AN["col"] == col)]
            if len(x) == 0:
                continue
            md.append(f"| {tf}m | {col} | {len(x):,} | {x['bars'].median():.0f} bars ({x['mins'].median():.0f} min) | "
                      f"{x['bars'].quantile(0.8):.0f} bars ({x['mins'].quantile(0.8):.0f} min) | {100 * (x['bars'] <= 2).mean():.0f}% | "
                      f"{100 * (x['bars'] >= 10).mean():.0f}% | {x['move'].mean():+.2f} | {x['best'].mean():.2f} |")
    md.append("")

    # ---- 2. events baseline
    md += ["## 2. The entry events by themselves (edge per cell: " + " | ".join(f"{s_} {pname[p_]}" for s_, p_ in cells) + "). FADED = the same numbers with the sign flipped.",
           "| Event | Direction | Chart | Events/yr per symbol | Edge per cell | R (+2/-1) per cell |", "|---|---|---|---|---|---|"]
    variants = []
    for k in range(4):
        for faded in (False, True):
            variants.append((k, faded))
    for k, faded in [v for v in variants if not v[1]]:
        sub = E[E["ev"] == k]
        A = align(sub, -sub["side"].to_numpy() if faded else sub["side"].to_numpy())
        for tf in ST_TFS:
            m = A["tf"] == tf
            e_ = A[m].groupby(["sym", "per"])["edge"].mean()
            r_ = A[m].groupby(["sym", "per"])["edge_r2"].mean()
            n_yr = np.mean([((A["tf"] == tf) & (A["sym"] == s_)).sum() / (years[(s_, tf, "tr")] + years[(s_, tf, "te")]) for s_ in SYMBOLS])
            md.append(f"| {EV_SHORT[k]} | {'FADED' if faded else 'as is'} | {tf}m | {n_yr:.0f} | {fmt_cells(e_)} | "
                      + " | ".join(f"{r_.get(c_, np.nan):+.3f}" for c_ in cells) + " |")
    md.append("")

    # ---- 3. single conditions + 4. confluence, per event variant
    summary, conf_rules = [], {}
    for k, faded in variants:
        sub = E[E["ev"] == k]
        A = align(sub, -sub["side"].to_numpy() if faded else sub["side"].to_numpy()).reset_index(drop=True)
        tr = (A["per"] == "tr").to_numpy()
        te = ~tr
        base_tr, base_te = A.loc[tr, "edge"].mean(), A.loc[te, "edge"].mean()
        cand = rules_for(A, tr)
        N0 = tr.sum()
        singles = []
        for nm, mk in cand:
            ntr = (mk & tr).sum()
            if ntr < max(0.10 * N0, 200):
                continue
            etr, ete = A.loc[mk & tr, "edge"].mean(), A.loc[mk & te, "edge"].mean()
            ce = A[mk].groupby(["sym", "per"])["edge"].mean()
            ctf = A[mk].groupby(["tf", "per"])["edge"].mean()
            tf_ok = sum(1 for t_ in ST_TFS if ctf.get((t_, "tr"), -1) > 0 and ctf.get((t_, "te"), -1) > 0)
            singles.append(dict(nm=nm, mk=mk, etr=etr, ete=ete, share=100 * ntr / N0, ce=ce,
                                pos=int(sum(ce.get(c_, -1) > 0 for c_ in cells)), tf_ok=tf_ok))
        # greedy confluence on TRAIN
        cur = np.ones(len(A), dtype=bool)
        steps = []
        for step in range(3):
            best = None
            for nm, mk in cand:
                m2 = cur & mk
                ntr = (m2 & tr).sum()
                if ntr < max(0.08 * N0, 300):
                    continue
                g = A.loc[m2 & tr]
                cc = g.groupby(["sym", "tf"])["edge"].mean()
                if (cc <= 0).any():
                    continue                                  # must help on every chart in TRAIN
                sc = g["edge"].mean()
                if best is None or sc > best[0]:
                    best = (sc, nm, m2)
            if best is None or (steps and best[0] < steps[-1]["etr"] + 0.3):
                break
            cur = best[2]
            steps.append(dict(nm=best[1], etr=best[0], ete=A.loc[cur & te, "edge"].mean(), mask=cur.copy(),
                              ntr=(cur & tr).sum(), nte=(cur & te).sum()))
        title = f"{EVENTS[k]}{' - FADED' if faded else ''}"
        conf_rules[(k, faded)] = (title, steps, A)
        if steps:
            fm_ = steps[-1]["mask"]
            ce = A[fm_].groupby(["sym", "per"])["edge"].mean()
            ctf = A[fm_ & te].groupby(["sym", "tf"])["edge"].mean()
            se = A.loc[fm_ & te, "edge"].std(ddof=1) / np.sqrt(max((fm_ & te).sum(), 1))
            summary.append(dict(title=title, k=k, faded=faded, steps=steps, base_tr=base_tr, base_te=base_te, ce=ce,
                                te_charts=int((ctf > 0).sum()), te_n=len(ctf), z=steps[-1]["ete"] / se if se > 0 else 0,
                                r2=A.loc[fm_ & te, "edge_r2"].mean()))
        singles.sort(key=lambda x: -x["etr"])
        keep[("singles", k, faded)] = (singles, base_tr, base_te)

    # ---- answer block
    summary.sort(key=lambda x: -x["steps"][-1]["ete"])
    for x in summary:
        x["real"] = bool(x["steps"][-1]["ete"] > 0 and x["te_charts"] >= x["te_n"] - 1 and x["z"] >= 2)
    real = [x for x in summary if x["real"]]
    top = ["## The answer in 30 seconds",
           f"- **Recipes that held up on {pname['te']} (never seen): {len(real)} of {len(summary)}**" +
           ("" if real else " - none of the trend-line recipes held up on new data."),
           "- Luck reference: the same search on RANDOM price data found recipes with TRAIN edge about +2 to +2.5 that "
           "fell to about 0 (or below) on TEST. A real recipe needs a clearly positive TEST edge on nearly every chart."]
    for x in summary[:8]:
        st_ = x["steps"]
        top.append(f"- **{x['title']}**: " + " AND ".join(s_["nm"] for s_ in st_) +
                   f" -> TRAIN edge {st_[-1]['etr']:+.1f} (event alone {x['base_tr']:+.1f}) | **TEST edge {st_[-1]['ete']:+.1f}** "
                   f"(event alone {x['base_te']:+.1f}), helped on {x['te_charts']}/{x['te_n']} charts in TEST, R(+2/-1) {x['r2']:+.3f} ATR"
                   f"{' ✅' if x['real'] else ''}")
    top.append("")

    # ---- 3. tables of single conditions for each event variant (top 15 by TRAIN + the TTM / Vix / timeframe rows)
    sec3 = ["## 3. Single conditions (picked by TRAIN edge, checked on TEST)",
            "Cells = edge for " + " | ".join(f"{s_} {pname[p_]}" for s_, p_ in cells) +
            ". Charts OK = 1/2/3/5m charts where it helped in BOTH periods. Share = % of events kept."]
    for k, faded in variants:
        singles, btr, bte = keep[("singles", k, faded)]
        sec3 += [f"### {EVENTS[k]}{' - FADED' if faded else ''} (event alone: TRAIN {btr:+.1f}, TEST {bte:+.1f})",
                 "| Condition | Share kept | TRAIN edge | TEST edge | Edge per cell | Cells > 0 | Charts OK |", "|---|---|---|---|---|---|---|"]
        shown = singles[:15]
        if not faded and k == 0:
            extra = [s_ for s_ in singles if s_ not in shown and any(w in s_["nm"] for w in ("TTM", "Vix", "trend ="))]
            shown = shown + extra
        for s_ in shown:
            sec3.append(f"| {s_['nm']} | {s_['share']:.0f}% | {s_['etr']:+.1f} | **{s_['ete']:+.1f}** | {fmt_cells(s_['ce'])} | {s_['pos']}/4 | {s_['tf_ok']}/{len(ST_TFS)} |")
        sec3.append("")

    # ---- 4. confluence detail
    sec4 = ["## 4. Confluence recipes step by step (each step picked on TRAIN; must help every chart in TRAIN)"]
    for (k, faded), (title, steps, A) in conf_rules.items():
        if not steps:
            sec4 += [f"### {title}", "No condition helped every chart in TRAIN.", ""]
            continue
        tr = (A["per"] == "tr").to_numpy()
        sec4 += [f"### {title}", "| Step | Add condition | Events kept TRAIN / TEST | TRAIN edge | TEST edge |", "|---|---|---|---|---|",
                 f"| 0 | (event alone) | {tr.sum():,} / {(~tr).sum():,} | {A.loc[tr, 'edge'].mean():+.1f} | {A.loc[~tr, 'edge'].mean():+.1f} |"]
        for n_, s_ in enumerate(steps, 1):
            sec4.append(f"| {n_} | {s_['nm']} | {s_['ntr']:,} / {s_['nte']:,} | {s_['etr']:+.1f} | **{s_['ete']:+.1f}** |")
        fm_ = steps[-1]["mask"]
        pt = A[fm_].groupby(["sym", "tf", "per"])["edge"].agg(["mean", "count"])
        sec4 += ["", "| Chart | TRAIN edge (n) | TEST edge (n) |", "|---|---|---|"]
        for s0 in SYMBOLS:
            for t_ in ST_TFS:
                a_ = pt.loc[(s0, t_, "tr")] if (s0, t_, "tr") in pt.index else None
                b_ = pt.loc[(s0, t_, "te")] if (s0, t_, "te") in pt.index else None
                sec4.append(f"| {s0} {t_}m | {a_['mean']:+.1f} ({int(a_['count'])}) | **{b_['mean']:+.1f}** ({int(b_['count'])}) |"
                            if a_ is not None and b_ is not None else f"| {s0} {t_}m | - | - |")
        sec4.append("")

    # ---- 5. exits for the event alone and the top recipes
    sec5 = ["## 5. Exits (ATR per trade; entry at the next open; 3 ATR safety stop; flat 15:55)",
            "Columns = " + " | ".join(f"{s_} {pname[p_]}" for s_, p_ in cells) + ". Compare rows within a table."]
    pick = [(0, False, "Line turns green/red (no filter)", None)] + [(x["k"], x["faded"], x["title"] + " - best recipe", x["steps"][-1]["mask"]) for x in summary[:3]]
    for k, faded, title, mask in pick:
        sub = E[E["ev"] == k].reset_index(drop=True)
        side = (-sub["side"] if faded else sub["side"]).to_numpy()
        if mask is not None:
            sub, side = sub[mask].reset_index(drop=True), side[mask]
        allr, names = [], None
        for (s0, t_), grp in sub.groupby(["sym", "tf"]):
            ind, color, mom = keep[(s0, t_)]
            names, r = study_exits(ind, color, mom, grp["i"].to_numpy(), side[grp.index.to_numpy()])
            d = pd.DataFrame(r, columns=names)
            d["sym"], d["per"] = s0, grp["per"].to_numpy()
            allr.append(d)
        if not allr:
            continue
        R = pd.concat(allr)
        sec5 += [f"### {title} ({len(R):,} trades)", "| Exit | " + " | ".join(f"{s_} {pname[p_]}" for s_, p_ in cells) + " | Avg |",
                 "|---|" + "---|" * (len(cells) + 1)]
        mean_rows = []
        for nm in names:
            g = R.groupby(["sym", "per"])[nm].mean()
            mean_rows.append((nm, g, g.mean()))
        for nm, g, av in sorted(mean_rows, key=lambda x: -x[2]):
            sec5.append(f"| {nm} | " + " | ".join(f"{g.get(c_, np.nan):+.3f}" for c_ in cells) + f" | **{av:+.3f}** |")
        sec5.append("")

    text = "\n".join(md[:3]).replace("{RT}", f"{(time.time() - t0) / 60:.0f}") + "\n" + "\n".join(md[3:4] + top + md[4:] + sec4 + sec3 + sec5)
    print("\n" + text[:20000])
    stamp = datetime.now(NY).strftime("%Y-%m-%d")
    for path in (f"{OUT}/study_{stamp}.md", f"{OUT}/study_latest.md"):
        with open(path, "w") as f:
            f.write(text + "\n")
    summ = os.getenv("GITHUB_STEP_SUMMARY")
    if summ:
        with open(summ, "a") as f:
            f.write(text[:900000] + "\n")


if __name__ == "__main__":
    main()
