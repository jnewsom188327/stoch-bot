"""
TREND FLIP OPTIMIZER + MONTE CARLO (MODE=optimize, the default) - see the OPTIMIZER section at the bottom.
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
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd

NY = ZoneInfo("America/New_York")
SYMBOLS = [s.strip().upper() for s in os.getenv("SYMBOLS", "SPY,QQQ").split(",") if s.strip()]
START = os.getenv("START", "2020-01-01").strip() or "2020-01-01"
DELTA = 0.6          # option delta for the rough $ estimate
TFS = [int(x) for x in os.getenv("TFS", "2,3").split(",") if x.strip()]
MODE = os.getenv("MODE", "optimize").strip().lower() or "optimize"
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
    out = np.full(len(flag), 999, dtype=np.int64)
    last = -10**9
    for i, f in enumerate(flag):
        if f:
            last = i
        out[i] = i - last if last > -10**9 else 999
    return out


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


if __name__ == "__main__":
    main()
