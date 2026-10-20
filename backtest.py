"""
VIX FIX WHIPLASH (MODE=wsw, the default) - one side of the Vix Fix pane maxed, then the other side maxes within N candles.
  Measures what a whiplash looks like (gap, how often) and tests FOLLOW / FADE, every T x N, hold 1-10 candles,
  SPY + QQQ 1/2/3/5m, 2020-now, vs random entries. DATA ONLY.
VF SCALPER +$0.50 IN 20 MINUTES (MODE=vfs) - every fire of the VF Scalper indicator (12 Vix Fix fires) with the
  trend-line filter off / with / against, target +$0.50 per share, 20-minute time limit, no stop vs $0.25 / $0.50 / $1.00 stops,
  SPY + QQQ 1/2/3/5m, 2020-now, vs random entries the same way, every year and chart. DATA ONLY.
VF CROSS v2 FIRES AFTER 10 MINUTES (MODE=vfc) - every fire of your VF CROSS v2 indicator (HARD, TURN, MAX,
  CROSS, long + short, and each one FLIPPED) on SPY + QQQ 1/2/3/5m, 2020-now, scored 5 / 10 / 20 minutes later vs a random
  entry in the same direction, every year, every chart. DATA ONLY.
VIX FIX RETEST + THE LEADERBOARD (MODE=vfx) - 2020-now, SPY + QQQ 1/2/3/5m. DATA ONLY, ATR only.
  Your 10/20 chart idea: a FEAR spike (red bars) marks a low, price BOUNCES at least 1 ATR, then PULLS BACK at least
  half of the bounce, but fear has dried up (the fear bar is under half the spike's tallest bar) -> long.
    VF1 = that retest | VF2 = + greed bar taller than fear (the mirror flipped) | VF3 = VF2 + a mirror phase first
    VF4 = VF2, then wait for the first green candle (confirmation) | VF5 = old version: lower low on a GRAY bar only
    | VF0 = reference: the streak ends (tested before).
  NUMBERS ONLY (no red / blue, your 10/20 12:15 note) - fear number F (0-100) and greed number G (0-100) of your pane:
    N1 divergence: price makes a new low below the last F peak's low (30 candles, peak 70+) but F is 10+ below that peak
    (shorts: new high, G 10+ below its peak) | N2 = 20+ below | N3 = N1 + the next candle turns your way
    N4 = after a peak, a mirror (F and G both 25+, within 15) for 3+ candles, then the other side takes over by 15+
    while the peak side is under half its peak | N5 = N4 + price holds above the peak's low (below its high for shorts).
  Shorts = the mirror image (GREED spike, bounce down, pull back up, greed dried up, fear taller than greed).
  On the same ruler: SUPER, SUPER+ and GAP & GO. Edge vs a coin flip, ATR after 5 / 10 / 15 / 30 / 60 candles and to
  15:55, minus a random entry in the same direction, best hold picked on 2020-23 only, every year, chart, side.
STOCH SCALP PRO - LAST 2 YEARS (MODE=stoch) - your Stoch Pro v1.2 box on SPY + QQQ 1/2/3/5m:
  Stoch 14-3-3 hook (was under 20 / over 80 in the last 3 bars, crosses %D, still under / over 50), filters
  trend (EMA 21/50) / VWAP / 5m trend / price candle, fast 5-3-3 and slow 21-5-5, entry at the next open,
  3-bar cooldown, 0.02 ATR slippage a side, flat 15:55. Every stop x target x hold time, the hold curve,
  the edge vs a coin flip, and option money (0DTE ATM like the box, 0DTE 1 strike out, 1DTE) with drawdowns.
TREND FLIP v2.7 - LAST 2 YEARS (MODE=v27) - the exact v2.7 setup from the TradingView boxes
  (13/34 + VWAP line flip, Vix Fix "After spike" within 10 candles, wait up to 5, entry at the next open,
  2 ATR stop, opposite flip exits, flat 15:55) on SPY + QQQ 1/2/3/5m over the last 2 years.
  Tests every hold time (5-60 candles) + the box's Trail / Hybrid / Color exits, the FILTER LAB filters,
  the edge vs a coin flip, and option money: 0DTE and 1DTE 1-strike-out-of-the-money contracts (Black-Scholes
  estimate at today's prices, $2 costs), with the worst drawdown and a Monte Carlo of bad years.
LONGS vs SHORTS (MODE=sides) - SUPER, SUPER+ (Stoch %K 20-40 your way) and GAP & GO (confirmed), split
  into LONGS and SHORTS. Each side is also compared with RANDOM entries in the same direction (because the market
  went up over 2020-2026, a random long already wins a bit more than half the time - the real question is
  whether a SUPER LONG beats a random long, and a SUPER SHORT beats a random short).
FILTER TEST (MODE=plus; PLUS_BASE=v40 (default) or super) - each filter on top of the v4.0 signal
  (or SUPER): Stoch, volume, MACD, VWAP distance, Vix Fix pane height / spike age, TTM momentum / slope / color / squeeze.
  Filters on top of SUPER (dip version): Stoch level and
  cross, relative volume (vs last 20, vs time of day, dip volume), MACD histogram size / turn / side of zero.
TTM + VIX FIX ON THEIR OWN (MODE=solo) - every TTM and Vix Fix signal by itself: turns, turn size,
  squeeze fire, zero cross, first spike bar, streak ends, streak length, bar height on every candle, TTM stretch stats,
  and the average price move 1 / 5 / 10 candles later.
TTM SQUEEZE + VIX FIX TEST (MODE=ttmvix) - TTM bottom/peak + first blue/red Vix Fix bar, streak ends,
  or Vix Fix first then TTM turn (your way round and the classic way round), with/without the trend line agreeing.
SUPER + GAP & GO TEST (MODE=super) - does SUPER LONG/SHORT keep its edge if it fires 1 candle sooner
  (warning after 1 close) or at the sharp dip itself (no color)? + 8 GAP & GO versions (gap size, entry time,
  confirmed). Same grading as the study, exits, rough $ per option.
TREND LINE STUDY (MODE=study) - line anatomy, 4 entry events (+ faded) on 1/2/3/5m, ~30 conditions
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
MODE = os.getenv("MODE", "wsw").strip().lower() or "wsw"
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
    if MODE == "super":
        return super_main()
    if MODE == "ttmvix":
        return ttmvix_main()
    if MODE == "solo":
        return solo_main()
    if MODE == "wsw":
        return wsw_main()
    if MODE == "vfs":
        return vfs_main()
    if MODE == "vfc":
        return vfc_main()
    if MODE == "vfx":
        return vfx_main()
    if MODE == "stoch":
        return stoch_main()
    if MODE == "v27":
        return v27_main()
    if MODE == "sides":
        return sides_main()
    if MODE == "plus":
        return plus_main()
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


# ================================================================ SUPER TIMING TEST (MODE=super, the default)
# Does SUPER LONG / SHORT keep its edge if it fires EARLIER?
#   A. SUPER as in the indicator: warning color after 2 closes (weakN=2), stretch >= 1.15 ATR, TTM dip >= 0.42 ATR
#   B. SUPER after 1 close (weakN=1) - one candle sooner
#   C. Sharp dip only: stretched trend + TTM dip on ANY candle, no color needed (earliest; first one per 10 candles)
# Graded both ways (exact coin flip) like the study + the "hold until the opposite color" exit.
SUP_GAP = float(os.getenv("SUP_GAP", "1.15"))
SUP_DROP = float(os.getenv("SUP_DROP", "0.42"))


def super_events(df, wn, variant):
    ind = indicators(df, 13, 34, True, weak_n=wn)
    c, a, st, hm = ind["c"], ind["atr"], ind["st"], ind["hm"]
    fadeL = (st == 1) & ~ind["strongL"]
    fadeS = (st == -1) & ~ind["strongS"]
    color = np.where(st == 1, np.where(fadeL, 1, 2), np.where(st == -1, np.where(fadeS, -1, -2), 0))
    cs, hs, ls = df["close"], df["high"], df["low"]
    basis = cs.rolling(20).mean()
    mid = ((hs.rolling(20).max() + ls.rolling(20).min()) / 2 + basis) / 2
    mom = linreg_last((cs - mid).to_numpy(), 20)
    mslope = (mom - np.r_[np.nan, mom[:-1]]) / a
    ef = cs.ewm(span=13, adjust=False).mean().to_numpy()
    es = cs.ewm(span=34, adjust=False).mean().to_numpy()
    spread = (ef - es) / a
    prev = np.r_[0, color[:-1]]
    win = (hm >= 935) & (hm < 1530)
    if variant == "dip":
        L = win & (color == 2) & (spread >= SUP_GAP) & (mslope <= -SUP_DROP)
        S = win & (color == -2) & (spread <= -SUP_GAP) & (mslope >= SUP_DROP)
        ent = np.where(L, 1, np.where(S, -1, 0))
        last = -10**9
        for i in np.nonzero(ent)[0]:
            if i - last < 10:
                ent[i] = 0
            else:
                last = i
    else:
        L = win & (color == 1) & (prev == 2) & (spread >= SUP_GAP) & (mslope <= -SUP_DROP)
        S = win & (color == -1) & (prev == -2) & (spread <= -SUP_GAP) & (mslope >= SUP_DROP)
        ent = np.where(L, 1, np.where(S, -1, 0))
    return ind, color, mom, ent


GAP_VARS = [("G1. Gap 0.3+ at 9:35 (as in the indicator)", 0.3, 935, False),
            ("G2. Gap 0.2+ at 9:35", 0.2, 935, False),
            ("G3. Gap 0.5+ at 9:35", 0.5, 935, False),
            ("G4. Gap 0.75+ at 9:35", 0.75, 935, False),
            ("G5. Gap 0.3+ at the 9:30 open candle", 0.3, 930, False),
            ("G6. Gap 0.3+ at 9:45", 0.3, 945, False),
            ("G7. Gap 0.3+ at 10:00", 0.3, 1000, False),
            ("G8. Gap 0.3+ at 9:35, CONFIRMED (gap not filled + right side of VWAP)", 0.3, 935, True)]


def gap_events(df, df1, ind, thr, t_from, confirm):
    lv = daily_levels(df1, df)
    gap = ((lv["dopen"] - lv["pdc"]) / lv["datr"]).to_numpy()
    hm, day, c = ind["hm"], ind["day"], ind["c"]
    first = first_per_day((hm >= t_from) & (hm < 1600), day)
    sd = np.sign(np.nan_to_num(gap))
    ok = first & (np.abs(np.nan_to_num(gap)) >= thr)
    if confirm:
        ok &= (sd * (c - lv["pdc"].to_numpy()) > 0) & (sd * (c - ind["vwap"]) > 0)
    return np.where(ok, sd, 0).astype(np.int64)


def super_main():
    end = datetime.now(timezone.utc) - timedelta(days=1)
    start = datetime.fromisoformat(START).replace(tzinfo=timezone.utc)
    test = os.getenv("TEST", "") == "1"
    os.makedirs(OUT, exist_ok=True)
    split = pd.Timestamp(SPLIT, tz=NY)
    t0 = time.time()
    VARS = [("A. SUPER now (warning after 2 closes)", 2, "warn"), ("B. SUPER after 1 close (1 candle sooner)", 1, "warn"),
            ("C. Sharp dip only, no color (earliest)", 2, "dip")]
    EXN = ["Opposite color starts", "Hold to 15:55", "+2 / -1 ATR bracket"]
    R = {}
    ATRNOW = {}

    def record(name, sym, tf, ind, color, mom, ent, yrs):
        idx = np.nonzero(ent)[0]
        side = ent[idx]
        g = grade_two_sided(ind, idx)
        ok = ~np.isnan(g[:, 6])
        idx, side, g = idx[ok], side[ok], g[ok]
        hit_s = np.where(side > 0, g[:, 0], g[:, 1])
        hit_o = np.where(side > 0, g[:, 1], g[:, 0])
        edge = 50.0 * (hit_s - hit_o)
        names, ex = study_exits(ind, color, mom, idx, side)
        t = ind["times"][idx]
        for per in ("tr", "te"):
            m = (t < split) if per == "tr" else (t >= split)
            d = dict(n=int(m.sum()), per_yr=m.sum() / yrs[per], edge=float(np.mean(edge[m])) if m.any() else np.nan,
                     hit=float(100 * np.mean(hit_s[m])) if m.any() else np.nan)
            for nm in EXN:
                d[nm] = float(np.nanmean(ex[m, names.index(nm)])) if m.any() else np.nan
            R[(name, sym, tf, per)] = d

    for sym in SYMBOLS:
        print(f"\n=== {sym} ===", flush=True)
        df1, feed = fake_1m(sym, start, end) if test else fetch_1m(sym, start, end)
        for tf in ST_TFS:
            df = to_tf(df1, rth_only=False, mins=tf)
            hm = (df.index.hour * 100 + df.index.minute).to_numpy()
            rth = (hm >= 930) & (hm < 1600)
            dates = np.array(sorted(set(pd.Index(df.index.date)[rth])))
            yrs = {"tr": max((dates < split.date()).sum() / 252.0, 1e-9), "te": max((dates >= split.date()).sum() / 252.0, 1e-9)}
            for name, wn, var in VARS:
                ind, color, mom, ent = super_events(df, wn, var)
                ind["times"] = df.index
                record(name, sym, tf, ind, color, mom, ent, yrs)
            ind, color, mom, _ = super_events(df, 2, "warn")
            ind["times"] = df.index
            mask = rth & np.isin(np.array(df.index.date), dates[-20:])
            ATRNOW[(sym, tf)] = float(np.nanmean(ind["atr"][mask]))
            for name, thr, tfrom, conf in GAP_VARS:
                record(name, sym, tf, ind, color, mom, gap_events(df, df1, ind, thr, tfrom, conf), yrs)
            print(f"  {sym} {tf}m done ({time.time() - t0:.0f}s)", flush=True)
        del df1
    pn = {"tr": f"{START[:4]}-{int(SPLIT[:4]) - 1}", "te": f"{SPLIT[:4]}-now"}

    def usd(r, sym, tf):
        return r * ATRNOW[(sym, tf)] * DELTA * 100 - 2.0 if not np.isnan(r) else np.nan

    def block(title, names_):
        out = [f"## {title} - the answer in 30 seconds"]
        for name in names_:
            row = []
            for per in ("tr", "te"):
                cells = [R[(name, s_, tf, per)] for s_ in SYMBOLS for tf in ST_TFS]
                n = sum(c["n"] for c in cells)
                e = np.nansum([c["edge"] * c["n"] for c in cells]) / max(n, 1)
                row.append(e)
            e2m = [R[(name, s_, 2, "te")]["edge"] for s_ in SYMBOLS]
            best = max(EXN, key=lambda nm: np.nanmean([R[(name, s_, tf, "te")][nm] for s_ in SYMBOLS for tf in ST_TFS]))
            bv = np.nanmean([R[(name, s_, tf, "te")][best] for s_ in SYMBOLS for tf in ST_TFS])
            out.append(f"- **{name}**: TRAIN edge {row[0]:+.1f} | **TEST edge {row[1]:+.1f}** | 2m TEST " +
                       " / ".join(f"{s_} {v:+.1f}" for s_, v in zip(SYMBOLS, e2m)) +
                       f" | best exit on TEST: {best} ({bv:+.2f} ATR per trade)")
        out += ["", f"### {title} - every chart",
                "| Version | Chart | Signals/yr | Edge " + pn["tr"] + " | Edge " + pn["te"] + " | " +
                " | ".join(f"{nm} {pn['te']} (ATR / ~$ per option)" for nm in EXN) + " |",
                "|---|---|---|---|---|" + "---|" * len(EXN)]
        for name in names_:
            for s_ in SYMBOLS:
                for tf in ST_TFS:
                    a_, b_ = R[(name, s_, tf, "tr")], R[(name, s_, tf, "te")]
                    ex = " | ".join(f"{b_[nm]:+.2f} / ${usd(b_[nm], s_, tf):+.0f}" for nm in EXN)
                    out.append(f"| {name} | {s_} {tf}m | {(a_['per_yr'] + b_['per_yr']) / 2:.0f} | {a_['edge']:+.1f} | **{b_['edge']:+.1f}** | {ex} |")
        return out + [""]

    md = [f"# SUPER + GAP & GO TEST - {datetime.now(NY):%Y-%m-%d %H:%M} ET",
          f"Data {START} to {end:%Y-%m-%d}. SUPER: stretch >= {SUP_GAP} ATR, TTM dip >= {SUP_DROP} ATR. DATA ONLY. Runtime {(time.time() - t0) / 60:.0f} min.",
          "**Edge** = +1-ATR-your-way-first rate minus the other way, halved (0 = coin flip, +6 = ~56% vs 44%). TRAIN = "
          f"{pn['tr']}, TEST = {pn['te']}. Exits: opposite color starts / hold to 15:55 / +2-1 bracket, 3 ATR safety stop, in ATR per "
          "trade. **~$ per option** = rough: ATR result x today's chart ATR x 0.6 delta x 100 - $2 costs (no time decay).", ""]
    md += block("SUPER LONG / SHORT timing", [v[0] for v in VARS])
    md += block("GAP & GO versions", [v[0] for v in GAP_VARS])
    text = "\n".join(md)
    print("\n" + text)
    stamp = datetime.now(NY).strftime("%Y-%m-%d")
    for path in (f"{OUT}/super_{stamp}.md", f"{OUT}/super_latest.md"):
        with open(path, "w") as f:
            f.write(text + "\n")
    sm = os.getenv("GITHUB_STEP_SUMMARY")
    if sm:
        with open(sm, "a") as f:
            f.write(text + "\n")


# ================================================================ TTM + VIX FIX COMBO TEST (MODE=ttmvix, the default)
# VIX FIX pane: RED bar = fear spike, BLUE bar = greed spike (greed only when not fear). TTM: bottom turn = red->yellow,
# peak = cyan->blue (same as the TTM Stretch pane). A TTM turn "counts" for 10 candles (until the opposite turn).
#  U1 LONG = TTM bottomed, then the FIRST BLUE bar | SHORT = TTM peaked, then the FIRST RED bar   (your idea)
#  U2 LONG = TTM bottomed, then a BLUE streak ENDS  | SHORT = TTM peaked, then a RED streak ENDS
#  U3 LONG = BLUE bar in the last 10 candles, THEN the TTM bottoms | SHORT = RED bar, then the TTM peaks
#  C1-C3 = the classic way round (RED fear at a bottom -> long, BLUE greed at a top -> short), same 3 timings
#  B1 = TTM turn alone | B2 = first Vix Fix bar alone (blue -> long, red -> short)
#  Each also "+ line agrees" (Trend Flip line green for longs / red for shorts).
# Graded both ways (exact coin flip): a NEGATIVE edge means the OPPOSITE direction works.
TV_K = int(os.getenv("TV_K", "10"))


def first_in_phase(evt, turn):
    n = len(evt)
    cum = np.cumsum(evt.astype(np.int64))
    idx = np.maximum.accumulate(np.where(turn, np.arange(n), -1))
    before = np.where(idx >= 0, cum[np.maximum(idx, 0)] - evt[np.maximum(idx, 0)], 0)
    return evt & (idx >= 0) & (cum - before == 1)


def ttmvix_signals(ind, mom, wv_fear, wv_greed):
    a, hm, st = ind["atr"], ind["hm"], ind["st"]
    m = mom / a
    m1, m2 = np.r_[np.nan, m[:-1]], np.r_[np.nan, np.nan, m[:-2]]
    bot = np.nan_to_num((m1 < 0) & (m1 < m2) & (m >= m1)).astype(bool)
    top = np.nan_to_num((m1 > 0) & (m1 > m2) & (m <= m1)).astype(bool)
    sb, stp = bars_since(bot), bars_since(top)
    up = (sb <= TV_K) & (sb < stp)
    dn = (stp <= TV_K) & (stp < sb)
    fear = wv_fear
    greed = wv_greed & ~wv_fear
    pf, pg = np.r_[False, fear[:-1]], np.r_[False, greed[:-1]]
    fFirst, gFirst = fear & ~pf, greed & ~pg
    fEnd, gEnd = ~fear & pf, ~greed & pg
    win = (hm >= 935) & (hm < 1530)
    S = {}
    S["U1. TTM bottom/peak, then FIRST BLUE (long) / RED (short) bar"] = (up & first_in_phase(gFirst, bot), dn & first_in_phase(fFirst, top))
    S["U2. TTM bottom/peak, then BLUE / RED streak ENDS"] = (up & first_in_phase(gEnd, bot), dn & first_in_phase(fEnd, top))
    S["U3. BLUE / RED bar first, THEN the TTM bottoms / peaks"] = (bot & (bars_since(greed) <= TV_K), top & (bars_since(fear) <= TV_K))
    S["C1. TTM bottom/peak, then FIRST RED (long) / BLUE (short) bar - classic"] = (up & first_in_phase(fFirst, bot), dn & first_in_phase(gFirst, top))
    S["C2. TTM bottom/peak, then RED / BLUE streak ENDS - classic"] = (up & first_in_phase(fEnd, bot), dn & first_in_phase(gEnd, top))
    S["C3. RED / BLUE bar first, THEN the TTM bottoms / peaks - classic"] = (bot & (bars_since(fear) <= TV_K), top & (bars_since(greed) <= TV_K))
    S["B1. TTM bottom (long) / peak (short) alone"] = (bot, top)
    S["B2. First BLUE bar (long) / first RED bar (short) alone"] = (gFirst, fFirst)
    out = {}
    for k, (L, Sh) in S.items():
        for agree in (False, True):
            l2, s2 = L & win, Sh & win
            if agree:
                l2, s2 = l2 & (st == 1), s2 & (st == -1)
            ent = np.where(l2 & ~s2, 1, np.where(s2 & ~l2, -1, 0)).astype(np.int64)
            out[k + (" + line agrees" if agree else "")] = ent
    return out


def ttmvix_main():
    end = datetime.now(timezone.utc) - timedelta(days=1)
    start = datetime.fromisoformat(START).replace(tzinfo=timezone.utc)
    test = os.getenv("TEST", "") == "1"
    os.makedirs(OUT, exist_ok=True)
    split = pd.Timestamp(SPLIT, tz=NY)
    t0 = time.time()
    EXN = ["Opposite color starts", "Hold to 15:55", "+2 / -1 ATR bracket", "TTM momentum peaks (turns against you)", "Time 10 candles"]
    R, ATRNOW, NAMES = {}, {}, []
    for sym in SYMBOLS:
        print(f"\n=== {sym} ===", flush=True)
        df1, feed = fake_1m(sym, start, end) if test else fetch_1m(sym, start, end)
        for tf in ST_TFS:
            df = to_tf(df1, rth_only=False, mins=tf)
            hm = (df.index.hour * 100 + df.index.minute).to_numpy()
            rth = (hm >= 930) & (hm < 1600)
            dates = np.array(sorted(set(pd.Index(df.index.date)[rth])))
            yrs = {"tr": max((dates < split.date()).sum() / 252.0, 1e-9), "te": max((dates >= split.date()).sum() / 252.0, 1e-9)}
            ind, color, mom, _ = super_events(df, 2, "warn")
            ATRNOW[(sym, tf)] = float(np.nanmean(ind["atr"][rth & np.isin(np.array(df.index.date), dates[-20:])]))
            sigs = ttmvix_signals(ind, mom, ind["fear"], ind["greed"])
            for name, ent in sigs.items():
                if name not in NAMES:
                    NAMES.append(name)
                idx = np.nonzero(ent)[0]
                side = ent[idx]
                g = grade_two_sided(ind, idx)
                ok = ~np.isnan(g[:, 6])
                idx, side, g = idx[ok], side[ok], g[ok]
                hs_ = np.where(side > 0, g[:, 0], g[:, 1])
                ho_ = np.where(side > 0, g[:, 1], g[:, 0])
                edge = 50.0 * (hs_ - ho_)
                names, ex = study_exits(ind, color, mom, idx, side)
                t = df.index[idx]
                for per in ("tr", "te"):
                    mk = (t < split) if per == "tr" else (t >= split)
                    d = dict(n=int(mk.sum()), per_yr=mk.sum() / yrs[per], edge=float(np.mean(edge[mk])) if mk.any() else np.nan)
                    for nm in EXN:
                        d[nm] = float(np.nanmean(ex[mk, names.index(nm)])) if mk.any() else np.nan
                    R[(name, sym, tf, per)] = d
            print(f"  {sym} {tf}m done ({time.time() - t0:.0f}s)", flush=True)
        del df1
    pn = {"tr": f"{START[:4]}-{int(SPLIT[:4]) - 1}", "te": f"{SPLIT[:4]}-now"}

    def pooled(name, per, key="edge"):
        cells = [R[(name, s_, tf, per)] for s_ in SYMBOLS for tf in ST_TFS]
        n = sum(c["n"] for c in cells)
        return np.nansum([c[key] * c["n"] for c in cells if not np.isnan(c[key])]) / max(n, 1), n

    rows = []
    for name in NAMES:
        etr, ntr = pooled(name, "tr")
        ete, nte = pooled(name, "te")
        d = 1 if etr >= 0 else -1                       # direction is decided on TRAIN only
        pos = sum(1 for s_ in SYMBOLS for tf in ST_TFS if d * R[(name, s_, tf, "te")]["edge"] > 0)
        rows.append(dict(name=name, etr=etr, ete=ete, d=d, pos=pos, n=ntr + nte,
                         per_yr=np.mean([R[(name, s_, tf, "tr")]["per_yr"] + R[(name, s_, tf, "te")]["per_yr"] for s_ in SYMBOLS for tf in ST_TFS]) / 2))
    rows.sort(key=lambda x: -min(x["d"] * x["etr"], x["d"] * x["ete"]))
    nC = len(SYMBOLS) * len(ST_TFS)
    md = [f"# TTM SQUEEZE + VIX FIX TEST - {datetime.now(NY):%Y-%m-%d %H:%M} ET",
          f"Data {START} to {end:%Y-%m-%d}, {', '.join(SYMBOLS)}, {', '.join(f'{t}m' for t in ST_TFS)}. DATA ONLY. Runtime {(time.time() - t0) / 60:.0f} min.",
          "**Edge** = +1-ATR-your-way-first rate minus the other way, halved (0 = coin flip, +5 = ~55% vs 45%). "
          f"Direction is picked on TRAIN ({pn['tr']}): if the edge is negative, the OPPOSITE trade works -> shown as 'FADE IT'. "
          f"TEST = {pn['te']}, never used to pick. A TTM turn counts for {TV_K} candles. Exits in ATR per trade (3 ATR safety stop).", "",
          "## The answer in 30 seconds (ranked by the worse of TRAIN and TEST, in the better direction)",
          "| Setup | Trade it | Signals/yr per chart | TRAIN edge | TEST edge | Charts positive in TEST |", "|---|---|---|---|---|---|"]
    for x in rows:
        md.append(f"| {x['name']} | {'as described' if x['d'] > 0 else '**FADE IT** (opposite)'} | {x['per_yr']:.0f} | "
                  f"{x['d'] * x['etr']:+.1f} | **{x['d'] * x['ete']:+.1f}** | {x['pos']}/{nC} |")
    md += ["", "Luck check: anything under about +1.5 or positive on fewer than 6 of 8 charts in TEST is noise. "
           "For reference, SUPER (dip version) scored TRAIN +5.2 / TEST +3.4 on 8/8 charts.", ""]
    md += [f"## Every chart (edge as described; TEST exits in ATR / ~$ per option)",
           "| Setup | Chart | Signals/yr | Edge " + pn["tr"] + " | Edge " + pn["te"] + " | " + " | ".join(f"{nm} (TEST)" for nm in EXN) + " |",
           "|---|---|---|---|---|" + "---|" * len(EXN)]
    for x in rows:
        for s_ in SYMBOLS:
            for tf in ST_TFS:
                a_, b_ = R[(x["name"], s_, tf, "tr")], R[(x["name"], s_, tf, "te")]
                exs = " | ".join(("-" if np.isnan(b_[nm]) else f"{b_[nm]:+.2f} / ${b_[nm] * ATRNOW[(s_, tf)] * DELTA * 100 - 2:+.0f}") for nm in EXN)
                md.append(f"| {x['name']} | {s_} {tf}m | {(a_['per_yr'] + b_['per_yr']) / 2:.0f} | {a_['edge']:+.1f} | **{b_['edge']:+.1f}** | {exs} |")
    text = "\n".join(md)
    print("\n" + text[:15000])
    stamp = datetime.now(NY).strftime("%Y-%m-%d")
    for path in (f"{OUT}/ttmvix_{stamp}.md", f"{OUT}/ttmvix_latest.md"):
        with open(path, "w") as f:
            f.write(text + "\n")
    sm = os.getenv("GITHUB_STEP_SUMMARY")
    if sm:
        with open(sm, "a") as f:
            f.write(text[:900000] + "\n")


# ================================================================ TTM + VIX FIX ON THEIR OWN (MODE=solo, the default)
# Every signal by itself (no trend line, no combos), SPY + QQQ, 1/2/3/5m. Entry = next open.
# Edge = graded both ways (exact coin flip; negative = the opposite direction works).
# Moves = average price change 1 / 5 / 10 candles after entry, in YOUR direction, in ATR (+ points at today's ATR).
SOLO_HB = [(0, 20), (20, 40), (40, 60), (60, 80), (80, 95), (95, 101)]
SOLO_TB = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 999)]
SOLO_SB = [(1, 1), (2, 2), (3, 3), (4, 5), (6, 999)]


def fwd_moves(ind, idx, side, ks=(1, 5, 10)):
    o, c, a, hm, day = ind["o"], ind["c"], ind["atr"], ind["hm"], ind["day"]
    n = len(o)
    out = {}
    e = idx + 1
    okE = e < n
    for k in ks:
        j = idx + k
        ok = okE & (j < n)
        v = np.full(len(idx), np.nan)
        ii, ee, jj = idx[ok], e[ok], j[ok]
        good = (day[np.minimum(jj, n - 1)] == day[ii]) & (day[ee] == day[ii]) & (hm[jj] < 1600)
        val = (c[jj] - o[ee]) / a[ii] * side[ok]
        v[np.nonzero(ok)[0][good]] = val[good]
        out[k] = v
    return out


def solo_main():
    end = datetime.now(timezone.utc) - timedelta(days=1)
    start = datetime.fromisoformat(START).replace(tzinfo=timezone.utc)
    test = os.getenv("TEST", "") == "1"
    os.makedirs(OUT, exist_ok=True)
    split = pd.Timestamp(SPLIT, tz=NY)
    t0 = time.time()
    EV, BARS, DESC, ATRNOW = [], [], [], {}
    for sym in SYMBOLS:
        print(f"\n=== {sym} ===", flush=True)
        df1, feed = fake_1m(sym, start, end) if test else fetch_1m(sym, start, end)
        for tf in ST_TFS:
            df = to_tf(df1, rth_only=False, mins=tf)
            ind, color, mom, _ = super_events(df, 2, "warn")
            o, c, a, hm = ind["o"], ind["c"], ind["atr"], ind["hm"]
            n = len(c)
            rth = (hm >= 930) & (hm < 1600)
            dates = np.array(sorted(set(pd.Index(df.index.date)[rth])))
            ATRNOW[(sym, tf)] = float(np.nanmean(a[rth & np.isin(np.array(df.index.date), dates[-20:])]))
            per = np.where(df.index < split, "tr", "te")
            win = (hm >= 935) & (hm < 1530)
            m = mom / a
            m1, m2 = np.r_[np.nan, m[:-1]], np.r_[np.nan, np.nan, m[:-2]]
            bot = np.nan_to_num((m1 < 0) & (m1 < m2) & (m >= m1)).astype(bool)
            top = np.nan_to_num((m1 > 0) & (m1 > m2) & (m <= m1)).astype(bool)
            # squeeze on/off (BB 20/2 inside KC 20/1.5)
            cs, hs, ls = df["close"], df["high"], df["low"]
            basis, dev = cs.rolling(20).mean(), 2.0 * cs.rolling(20).std(ddof=0)
            pc = cs.shift(1)
            trr = pd.concat([hs - ls, (hs - pc).abs(), (ls - pc).abs()], axis=1).max(axis=1).rolling(20).mean()
            sq = (((basis - dev) > (basis - 1.5 * trr)) & ((basis + dev) < (basis + 1.5 * trr))).fillna(False).to_numpy()
            fire = np.r_[False, sq[:-1]] & ~sq
            sg = np.sign(np.nan_to_num(m))
            sgp = np.r_[0, sg[:-1]]
            zc = (sg != 0) & (sgp != 0) & (sg != sgp)
            # Vix Fix (as the pane): fear = red, greed = blue (greed only when not fear); bar height 0-100
            hc22, lc22 = cs.rolling(22).max(), cs.rolling(22).min()
            wvf = ((hc22 - ls) / hc22 * 100)
            wvi = ((hs - lc22) / lc22 * 100)
            fN = (wvf / wvf.rolling(50).max() * 100).to_numpy()
            gN = (wvi / wvi.rolling(50).max() * 100).to_numpy()
            fear = ind["fear"]
            greed = ind["greed"] & ~fear
            pf, pg = np.r_[False, fear[:-1]], np.r_[False, greed[:-1]]

            def runlen(x):
                r = np.zeros(len(x), dtype=np.int64)
                for i in range(len(x)):
                    r[i] = r[i - 1] + 1 if x[i] and i > 0 else (1 if x[i] else 0)
                return r
            rf, rg = runlen(fear), runlen(greed)
            fmax = pd.Series(np.where(fear, fN, np.nan)).groupby((~pd.Series(fear)).cumsum()).cummax().to_numpy()
            gmax = pd.Series(np.where(greed, gN, np.nan)).groupby((~pd.Series(greed)).cumsum()).cummax().to_numpy()

            def add(fam, L, S, bucket=None):
                idx = np.nonzero(win & (L | S) & ~(L & S))[0]
                if len(idx) == 0:
                    return
                side = np.where(L[idx], 1, -1)
                g = grade_two_sided(ind, idx)
                ok = ~np.isnan(g[:, 6])
                idx, side, g = idx[ok], side[ok], g[ok]
                edge = 50.0 * (np.where(side > 0, g[:, 0], g[:, 1]) - np.where(side > 0, g[:, 1], g[:, 0]))
                fm = fwd_moves(ind, idx, side)
                d = pd.DataFrame({"fam": fam, "bucket": bucket[idx] if bucket is not None else "", "sym": sym, "tf": tf,
                                  "per": per[idx], "edge": edge, "f1": fm[1], "f5": fm[5], "f10": fm[10]})
                EV.append(d)

            add("TTM bottom turn = long / peak turn = short", bot, top)
            tsize = np.where(bot, -m1, np.where(top, m1, np.nan))
            tb = np.array([next(((f"{lo}-{hi} ATR" if hi < 999 else f"{lo}+ ATR") for lo, hi in SOLO_TB if lo <= v < hi), "") if not np.isnan(v) else "" for v in tsize])
            add("TTM turn by size (how stretched momentum was at the turn)", bot, top, tb)
            add("TTM squeeze FIRES -> trade momentum's direction", fire & (m > 0), fire & (m < 0))
            add("TTM momentum crosses zero (up = long, down = short)", zc & (sg > 0), zc & (sg < 0))
            add("Vix Fix FIRST red bar = long / FIRST blue bar = short", fear & ~pf, greed & ~pg)
            fe, ge = ~fear & pf, ~greed & pg
            add("Vix Fix streak ENDS: after red bars = long / after blue bars = short", fe, ge)
            sl = np.where(fe, np.r_[0, rf[:-1]], np.where(ge, np.r_[0, rg[:-1]], 0))
            sb = np.array([next((f"{lo}" if lo == hi else (f"{lo}-{hi}" if hi < 999 else f"{lo}+") for lo, hi in SOLO_SB if lo <= v <= hi), "") + " bars" if v > 0 else "" for v in sl])
            add("Vix Fix streak ENDS, by how many spike bars in a row", fe, ge, sb)
            hmax = np.where(fe, np.r_[np.nan, fmax[:-1]], np.where(ge, np.r_[np.nan, gmax[:-1]], np.nan))
            hb = np.array([next((f"{lo}-{min(hi, 100)}" for lo, hi in SOLO_HB if lo <= v < hi), "") if not np.isnan(v) else "" for v in hmax])
            add("Vix Fix streak ENDS, by the tallest bar in the streak (0-100)", fe, ge, hb)
            # every candle: Vix Fix bar height -> next moves (fear height = long, greed height = short) + baseline
            idx = np.nonzero(win)[0]
            fmL = fwd_moves(ind, idx, np.ones(len(idx), dtype=np.int64))
            for nm, h, sd in (("FEAR (red side) bar height -> LONG", fN, 1), ("GREED (blue side) bar height -> SHORT", gN, -1)):
                hv = h[idx]
                hbk = np.array([next((f"{lo}-{min(hi, 100)}" for lo, hi in SOLO_HB if lo <= v < hi), "") if not np.isnan(v) else "" for v in hv])
                BARS.append(pd.DataFrame({"kind": nm, "bucket": hbk, "sym": sym, "tf": tf, "per": per[idx],
                                          "f1": fmL[1] * sd, "f5": fmL[5] * sd, "f10": fmL[10] * sd}))
            BARS.append(pd.DataFrame({"kind": "ALL candles (long) = market drift baseline", "bucket": "all", "sym": sym, "tf": tf,
                                      "per": per[idx], "f1": fmL[1], "f5": fmL[5], "f10": fmL[10]}))
            # TTM pane stats (like your Stretch Bands table) on this chart
            tops, bots = m1[top & rth], -m1[bot & rth]
            wid = np.cumsum(np.r_[1, (sg[1:] != sg[:-1]).astype(int)])
            wv = pd.DataFrame({"w": wid, "s": sg, "v": np.abs(np.nan_to_num(m))})
            wmax = wv.groupby("w").agg(s=("s", "first"), v=("v", "max"), L=("v", "size"))
            wmax = wmax[wmax["L"] >= 2]
            for lab, arr in (("Top turns (cyan>blue)", tops), ("Bottom turns (red>yellow)", bots),
                             ("Wave max UP", wmax.loc[wmax["s"] > 0, "v"].to_numpy()), ("Wave max DOWN", wmax.loc[wmax["s"] < 0, "v"].to_numpy())):
                arr = arr[~np.isnan(arr)]
                if len(arr):
                    DESC.append((sym, tf, lab, len(arr), arr.mean(), np.median(arr), np.percentile(arr, 80), arr.max()))
            print(f"  {sym} {tf}m done ({time.time() - t0:.0f}s)", flush=True)
        del df1
    E = pd.concat(EV, ignore_index=True)
    B = pd.concat(BARS, ignore_index=True)
    pn = {"tr": f"{START[:4]}-{int(SPLIT[:4]) - 1}", "te": f"{SPLIT[:4]}-now"}
    nC = len(SYMBOLS) * len(ST_TFS)
    atr_txt = ", ".join(f"{s_} {tf}m 1 ATR = {ATRNOW[(s_, tf)]:.2f}" for s_ in SYMBOLS for tf in ST_TFS)

    def summarize(g):
        tr, te = g[g["per"] == "tr"], g[g["per"] == "te"]
        ctf = te.groupby(["sym", "tf"])["edge"].mean()
        return dict(n_yr=len(g) / (2 * 6.8) / max(g[["sym", "tf"]].drop_duplicates().shape[0] / 1, 1) * 2,
                    etr=tr["edge"].mean(), ete=te["edge"].mean(), pos=int((ctf > 0).sum()), npos=len(ctf),
                    f1=te["f1"].mean(), f5=te["f5"].mean(), f10=te["f10"].mean(), n=len(g))

    md = [f"# TTM SQUEEZE + VIX FIX, EACH ON ITS OWN - {datetime.now(NY):%Y-%m-%d %H:%M} ET",
          f"Data {START} to {end:%Y-%m-%d}, {', '.join(SYMBOLS)}, {', '.join(f'{t}m' for t in ST_TFS)}. DATA ONLY. Runtime {(time.time() - t0) / 60:.0f} min.",
          "**Edge** = +1-ATR-your-way-first rate minus the other way, halved (0 = coin flip; +5 = ~55% vs 45%; negative = the opposite "
          f"direction works). **Next 1 / 5 / 10** = average price move that many candles after entry, in your direction, in ATR "
          f"({pn['te']}). Real = edge +1.5 or better in BOTH periods and positive on 6+ of {nC} charts. "
          f"Today's ATRs: {atr_txt}.", "",
          "## The answer in 30 seconds - every signal on its own",
          "| Signal | Events | Edge " + pn["tr"] + " | Edge " + pn["te"] + f" | Charts positive (TEST) | Next 1 | Next 5 | Next 10 | Real? |",
          "|---|---|---|---|---|---|---|---|---|"]
    bfams = set(E.loc[E["bucket"] != "", "fam"])
    for fam, g in E[(E["bucket"] == "") & ~E["fam"].isin(bfams)].groupby("fam", sort=False):
        x = summarize(g)
        real = x["etr"] >= 1.5 and x["ete"] >= 1.5 and x["pos"] >= 6
        md.append(f"| {fam} | {x['n']:,} | {x['etr']:+.1f} | **{x['ete']:+.1f}** | {x['pos']}/{x['npos']} | {x['f1']:+.3f} | {x['f5']:+.3f} | {x['f10']:+.3f} | {'✅' if real else ''} |")
    md += ["", "## Broken down (by size / streak / height)",
           "| Signal | Bucket | Events | Edge " + pn["tr"] + " | Edge " + pn["te"] + " | Charts positive (TEST) | Next 1 | Next 5 | Next 10 |",
           "|---|---|---|---|---|---|---|---|---|"]
    for fam, g in E[E["bucket"] != ""].groupby("fam", sort=False):
        for bk, gb in sorted(g.groupby("bucket"), key=lambda kv: kv[0]):
            x = summarize(gb)
            md.append(f"| {fam} | {bk} | {x['n']:,} | {x['etr']:+.1f} | **{x['ete']:+.1f}** | {x['pos']}/{x['npos']} | {x['f1']:+.3f} | {x['f5']:+.3f} | {x['f10']:+.3f} |")
    md += ["", "## Vix Fix bar height on EVERY candle -> what price did next (raw moves; compare with the ALL candles row = drift)",
           "| Bar | Height (0-100) | Share of candles | Next 1 " + pn["tr"] + " | Next 1 " + pn["te"] + " | Next 5 TEST | Next 10 TEST | Next 10 minus drift (TEST) |",
           "|---|---|---|---|---|---|---|---|"]
    drift = B[(B["kind"].str.startswith("ALL")) & (B["per"] == "te")]["f10"].mean()
    B = B[B["bucket"] != ""]
    for kind, g in B.groupby("kind", sort=False):
        tot = len(g)
        for bk, gb in sorted(g.groupby("bucket"), key=lambda kv: (kv[0] == "all", float(kv[0].split("-")[0]) if kv[0][0].isdigit() else 0)):
            tr, te = gb[gb["per"] == "tr"], gb[gb["per"] == "te"]
            adj = te["f10"].mean() - (drift if "LONG" in kind else -drift) if not kind.startswith("ALL") else 0.0
            md.append(f"| {kind} | {bk} | {100 * len(gb) / tot:.0f}% | {tr['f1'].mean():+.3f} | {te['f1'].mean():+.3f} | {te['f5'].mean():+.3f} | "
                      f"{te['f10'].mean():+.3f} | **{adj:+.3f}** |")
    md += ["", "## TTM momentum stretch on each chart (like your TTM Stretch Bands table, in ATR, regular hours)",
           "| Chart | | N | Avg | Median | 80% | Max |", "|---|---|---|---|---|---|---|"]
    for row in DESC:
        md.append(f"| {row[0]} {row[1]}m | {row[2]} | {row[3]:,} | {row[4]:.2f} | {row[5]:.2f} | {row[6]:.2f} | {row[7]:.2f} |")
    md += ["", f"Points: multiply ATR moves by the chart's ATR above (e.g. +0.10 ATR on SPY 2m = about {0.1 * ATRNOW.get(('SPY', 2), 0):.2f} pts "
           f"≈ ${0.1 * ATRNOW.get(('SPY', 2), 0) * DELTA * 100:.0f} per 0.6-delta option, before costs)."]
    text = "\n".join(md)
    print("\n" + text[:15000])
    stamp = datetime.now(NY).strftime("%Y-%m-%d")
    for path in (f"{OUT}/solo_{stamp}.md", f"{OUT}/solo_latest.md"):
        with open(path, "w") as f:
            f.write(text + "\n")
    sm = os.getenv("GITHUB_STEP_SUMMARY")
    if sm:
        with open(sm, "a") as f:
            f.write(text[:900000] + "\n")


# ================================================================ SUPER + STOCH / VOLUME / MACD (MODE=plus, the default)
# Base = SUPER (dip version, as in the indicator): stretched trend (EMA gap >= 1.15 ATR) + sharp TTM dip >= 0.42 ATR.
# Each filter is tested ON TOP of SUPER, one at a time. Kept only if it improves SUPER in BOTH periods on most charts.
#  STOCH 14,3,3 : %K level "your way" (longs: K; shorts: 100-K -> low = oversold in your favor), %K crossing %D your way
#  VOLUME       : signal candle volume vs last 20 candles, vs the same time of day (20-day avg), last 3 candles vs 20
#  MACD 12,26,9 : histogram size your way (ATR), histogram turning your way, MACD line on your side of zero
PLUS_BUCKETS = {
    "Stoch %K your way (0 = fully oversold for longs / overbought for shorts)": [(0, 20), (20, 40), (40, 60), (60, 80), (80, 101)],
    "Volume vs last 20 candles (1 = normal)": [(0, 0.7), (0.7, 1.0), (1.0, 1.5), (1.5, 2.5), (2.5, 999)],
    "Volume vs same time of day (20-day avg)": [(0, 0.7), (0.7, 1.0), (1.0, 1.5), (1.5, 2.5), (2.5, 999)],
    "Last 3 candles' volume vs last 20 (the dip's volume)": [(0, 0.7), (0.7, 1.0), (1.0, 1.5), (1.5, 2.5), (2.5, 999)],
    "MACD histogram your way (ATR)": [(-999, -0.3), (-0.3, -0.1), (-0.1, 0.1), (0.1, 0.3), (0.3, 999)],
    "Distance from VWAP your side (ATR)": [(-999, -1), (-1, 0), (0, 0.5), (0.5, 1), (1, 2), (2, 999)],
    "VIX FIX pane bar YOUR way (0-100; red before longs, blue before shorts)": [(0, 20), (20, 40), (40, 60), (60, 80), (80, 95), (95, 101)],
    "VIX FIX pane bar AGAINST you (0-100)": [(0, 20), (20, 40), (40, 60), (60, 80), (80, 95), (95, 101)],
    "Candles since a Vix Fix spike your way": [(0, 1), (1, 3), (3, 6), (6, 11), (11, 999)],
    "TTM momentum your way (ATR)": [(-999, -1), (-1, -0.3), (-0.3, 0.3), (0.3, 1), (1, 2), (2, 999)],
    "TTM momentum slope your way (ATR per candle)": [(-999, -0.3), (-0.3, -0.1), (-0.1, 0.1), (0.1, 0.3), (0.3, 999)],
}


def plus_features(df, ind, idx, side):
    c, h, l, v = df["close"], df["high"], df["low"], df["volume"]
    a = ind["atr"]
    ll, hh = l.rolling(14).min(), h.rolling(14).max()
    k = (100 * (c - ll) / (hh - ll).replace(0, np.nan)).rolling(3).mean()
    d = k.rolling(3).mean()
    K, D = k.to_numpy(), d.to_numpy()
    vol = v.to_numpy(dtype=float)
    rv20 = vol / pd.Series(vol).rolling(20).mean().shift(1).to_numpy()
    hm = ind["hm"]
    tod = pd.Series(vol).groupby(hm).transform(lambda x: x.rolling(20, min_periods=5).mean().shift(1)).to_numpy()
    rvtod = vol / tod
    rv3 = pd.Series(vol).rolling(3).mean().to_numpy() / pd.Series(vol).rolling(20).mean().shift(3).to_numpy()
    e12, e26 = c.ewm(span=12, adjust=False).mean(), c.ewm(span=26, adjust=False).mean()
    macd = (e12 - e26).to_numpy()
    sigl = pd.Series(macd).ewm(span=9, adjust=False).mean().to_numpy()
    hist = macd - sigl
    histp = np.r_[np.nan, hist[:-1]]
    Kp, Dp = np.r_[np.nan, K[:-1]], np.r_[np.nan, D[:-1]]
    sd = side.astype(float)
    kw = np.where(sd > 0, K[idx], 100 - K[idx])
    crossL = (K > D) & (Kp <= Dp)
    crossS = (K < D) & (Kp >= Dp)
    recentL = crossL | np.r_[False, crossL[:-1]]
    recentS = crossS | np.r_[False, crossS[:-1]]
    F = {
        "Stoch %K your way (0 = fully oversold for longs / overbought for shorts)": kw,
        "Stoch %K crossed %D your way (last 2 candles)": np.where(np.where(sd > 0, recentL[idx], recentS[idx]), "yes", "no"),
        "Volume vs last 20 candles (1 = normal)": rv20[idx],
        "Volume vs same time of day (20-day avg)": rvtod[idx],
        "Last 3 candles' volume vs last 20 (the dip's volume)": rv3[idx],
        "MACD histogram your way (ATR)": hist[idx] / a[idx] * sd,
        "MACD histogram turning your way": np.where((hist[idx] - histp[idx]) * sd > 0, "yes", "no"),
        "MACD line on your side of zero": np.where(macd[idx] * sd > 0, "yes", "no"),
    }
    if os.getenv("PLUS_BASE", "v40").lower() == "v40":
        vw = ind["vwap"]
        F["Distance from VWAP your side (ATR)"] = (c.to_numpy()[idx] - vw[idx]) / a[idx] * sd
        hc22, lc22 = c.rolling(22).max(), c.rolling(22).min()
        wvf, wvi = (hc22 - l) / hc22 * 100, (h - lc22) / lc22 * 100
        fN, gN = (wvf / wvf.rolling(50).max() * 100).to_numpy(), (wvi / wvi.rolling(50).max() * 100).to_numpy()
        F["VIX FIX pane bar YOUR way (0-100; red before longs, blue before shorts)"] = np.where(sd > 0, fN[idx], gN[idx])
        F["VIX FIX pane bar AGAINST you (0-100)"] = np.where(sd > 0, gN[idx], fN[idx])
        fa, ga = bars_since(ind["fear"]), bars_since(ind["greed"] & ~ind["fear"])
        F["Candles since a Vix Fix spike your way"] = np.where(sd > 0, fa[idx], ga[idx]).astype(float)
        basis = c.rolling(20).mean()
        mid = ((h.rolling(20).max() + l.rolling(20).min()) / 2 + basis) / 2
        mom = linreg_last((c - mid).to_numpy(), 20)
        mm = mom / a
        mmp = np.r_[np.nan, mm[:-1]]
        F["TTM momentum your way (ATR)"] = mm[idx] * sd
        F["TTM momentum slope your way (ATR per candle)"] = (mm[idx] - mmp[idx]) * sd
        mw, ms = mm[idx] * sd, (mm[idx] - mmp[idx]) * sd
        F["TTM color (vs your trade)"] = np.where(mw > 0, np.where(ms > 0, "cyan-type: with you, rising", "blue-type: with you, fading"),
                                                  np.where(ms > 0, "yellow-type: against you, turning", "red-type: against you, falling"))
        dev = 2.0 * c.rolling(20).std(ddof=0)
        pc = c.shift(1)
        trr = pd.concat([h - l, (h - pc).abs(), (l - pc).abs()], axis=1).max(axis=1).rolling(20).mean()
        sq = (((basis - dev) > (basis - 1.5 * trr)) & ((basis + dev) < (basis + 1.5 * trr))).fillna(False).to_numpy()
        ss = bars_since(sq)
        F["TTM squeeze"] = np.where(sq[idx], "in squeeze", np.where(ss[idx] <= 3, "fired 0-3 candles ago", np.where(ss[idx] <= 10, "fired 4-10 ago", "none in 10+")))
    return F


def plus_main():
    end = datetime.now(timezone.utc) - timedelta(days=1)
    start = datetime.fromisoformat(START).replace(tzinfo=timezone.utc)
    test = os.getenv("TEST", "") == "1"
    os.makedirs(OUT, exist_ok=True)
    split = pd.Timestamp(SPLIT, tz=NY)
    t0 = time.time()
    rows = []
    for sym in SYMBOLS:
        print(f"\n=== {sym} ===", flush=True)
        df1, feed = fake_1m(sym, start, end) if test else fetch_1m(sym, start, end)
        for tf in ST_TFS:
            df = to_tf(df1, rth_only=False, mins=tf)
            ind, color, mom, ent = super_events(df, 2, "dip")
            if os.getenv("PLUS_BASE", "v40").lower() == "v40":
                _, ent = signals(ind, dict(V30, allowL=None))
            idx = np.nonzero(ent)[0]
            side = ent[idx]
            g = grade_two_sided(ind, idx)
            ok = ~np.isnan(g[:, 6])
            idx, side, g = idx[ok], side[ok], g[ok]
            edge = 50.0 * (np.where(side > 0, g[:, 0], g[:, 1]) - np.where(side > 0, g[:, 1], g[:, 0]))
            names, ex = study_exits(ind, color, mom, idx, side)
            F = plus_features(df, ind, idx, side)
            d = pd.DataFrame(F)
            d["edge"] = edge
            d["hold"] = ex[:, names.index("Hold to 15:55")]
            d["sym"], d["tf"] = sym, tf
            d["per"] = np.where(df.index[idx] < split, "tr", "te")
            rows.append(d)
            print(f"  {sym} {tf}m: {len(idx)} signals ({time.time() - t0:.0f}s)", flush=True)
        del df1
    E = pd.concat(rows, ignore_index=True)
    pn = {"tr": f"{START[:4]}-{int(SPLIT[:4]) - 1}", "te": f"{SPLIT[:4]}-now"}
    nC = len(SYMBOLS) * len(ST_TFS)
    base = {p_: E.loc[E["per"] == p_, "edge"].mean() for p_ in ("tr", "te")}
    baseh = E.loc[E["per"] == "te", "hold"].mean()

    def line(nm, mk):
        g = E[mk]
        etr, ete = g.loc[g["per"] == "tr", "edge"].mean(), g.loc[g["per"] == "te", "edge"].mean()
        ctf = g[g["per"] == "te"].groupby(["sym", "tf"])["edge"].mean()
        bt = E[E["per"] == "te"].groupby(["sym", "tf"])["edge"].mean()
        better = int(sum(1 for k_ in ctf.index if ctf[k_] > bt.get(k_, 0)))
        helps = etr > base["tr"] + 1.0 and ete > base["te"] + 1.0 and better >= 6
        return (f"| {nm} | {100 * mk.mean():.0f}% | {etr:+.1f} | **{ete:+.1f}** | {better}/{len(ctf)} | "
                f"{g.loc[g['per'] == 'te', 'hold'].mean():+.2f} | {'✅ helps' if helps else ''} |"), (helps, ete - base["te"], nm)

    bname = "v4.0 signal (line flip + Vix Fix spike, as v3.0)" if os.getenv("PLUS_BASE", "v40").lower() == "v40" else "SUPER (dip version)"
    md = [f"# {bname.split(' (')[0]} + FILTERS - {datetime.now(NY):%Y-%m-%d %H:%M} ET",
          f"Data {START} to {end:%Y-%m-%d}, {', '.join(SYMBOLS)}, {', '.join(f'{t}m' for t in ST_TFS)}. Base = {bname}. "
          f"DATA ONLY. Runtime {(time.time() - t0) / 60:.0f} min.",
          "**Edge** = +1-ATR-your-way-first rate minus the other way, halved (0 = coin flip). **Charts better** = charts where the "
          f"filtered signal beat the plain signal in TEST ({pn['te']}). **Hold** = ATR per trade held to 15:55 (TEST). "
          "✅ = beats the plain signal by 1.0+ in BOTH periods and on 6+ of 8 charts. Luck check: on RANDOM price data, 1 of ~25 "
          "filters passed a looser (0.5) version of this test, so treat a single ✅ with care.", "",
          f"**Plain {bname}: {len(E):,} signals | TRAIN edge {base['tr']:+.1f} | TEST edge {base['te']:+.1f} | hold to 15:55 {baseh:+.2f} ATR**", ""]
    body, res = [], []
    hdr = ["| Filter | Kept | Edge " + pn["tr"] + " | Edge " + pn["te"] + " | Charts better (TEST) | Hold (TEST) | |", "|---|---|---|---|---|---|---|"]
    for col in [c_ for c_ in E.columns if c_ not in ("edge", "hold", "sym", "tf", "per")]:
        body += [f"### {col}"] + hdr
        v = E[col]
        if not pd.api.types.is_numeric_dtype(v):
            for val in sorted(v.dropna().unique()):
                l_, r_ = line(f"= {val}", (v == val).to_numpy())
                body.append(l_)
                res.append((r_[0], r_[1], f"{col} = {val}"))
        else:
            x = v.to_numpy(dtype=float)
            for lo, hi in PLUS_BUCKETS[col]:
                mk = (x >= lo) & (x < hi)
                if mk.sum() < 30:
                    continue
                lab = f"{lo:g} to {hi:g}" if lo > -999 and hi < 999 else (f"under {hi:g}" if lo <= -999 else f"{lo:g}+")
                l_, r_ = line(lab, mk)
                body.append(l_)
                res.append((r_[0], r_[1], f"{col}: {lab}"))
        body.append("")
    good = sorted([r_ for r_ in res if r_[0]], key=lambda z: -z[1])
    md += ["## The answer in 30 seconds",
           f"- **Filters that make it better in both periods on most charts: {len(good)}**" +
           (": " + "; ".join(f"{z[2]} (TEST +{z[1]:.1f} over the plain signal)" for z in good[:8]) if good else
            " - none of the filters improve it."),
           "- Note: a filter that keeps only a small share of signals can look good by luck - check 'Kept' and 'Charts better'.", ""]
    text = "\n".join(md + body)
    print("\n" + text)
    stamp = datetime.now(NY).strftime("%Y-%m-%d")
    for path in (f"{OUT}/plus_{stamp}.md", f"{OUT}/plus_latest.md"):
        with open(path, "w") as f:
            f.write(text + "\n")
    sm = os.getenv("GITHUB_STEP_SUMMARY")
    if sm:
        with open(sm, "a") as f:
            f.write(text + "\n")


# ================================================================ LONGS vs SHORTS (MODE=sides)
def sides_main():
    end = datetime.now(timezone.utc) - timedelta(days=1)
    start = datetime.fromisoformat(START).replace(tzinfo=timezone.utc)
    test = os.getenv("TEST", "") == "1"
    os.makedirs(OUT, exist_ok=True)
    split = pd.Timestamp(SPLIT, tz=NY)
    t0 = time.time()
    rng = np.random.default_rng(7)
    rows, base_rows, atrnow = [], [], {}
    for sym in SYMBOLS:
        print(f"\n=== {sym} ===", flush=True)
        df1, feed = fake_1m(sym, start, end) if test else fetch_1m(sym, start, end)
        for tf in ST_TFS:
            df = to_tf(df1, rth_only=False, mins=tf)
            ind, color, mom, sup = super_events(df, 2, "dip")
            ind["times"] = df.index
            hm = ind["hm"]
            c, h, l = df["close"], df["high"], df["low"]
            ll, hh = l.rolling(14).min(), h.rolling(14).max()
            K = (100 * (c - ll) / (hh - ll).replace(0, np.nan)).rolling(3).mean().to_numpy()
            kw = np.where(sup > 0, K, 100 - K)
            plus = np.where((sup != 0) & (kw >= 20) & (kw <= 40), sup, 0)
            gap = gap_events(df, df1, ind, 0.3, 935, True)
            rth = (hm >= 930) & (hm < 1600)
            dates = np.array(sorted(set(pd.Index(df.index.date)[rth])))
            atrnow[(sym, tf)] = float(np.nanmean(ind["atr"][rth & np.isin(np.array(df.index.date), dates[-20:])]))
            for kind, ent in (("SUPER", sup), ("SUPER+", plus), ("GAP & GO", gap)):
                idx = np.nonzero(ent)[0]
                side = ent[idx]
                g = grade_two_sided(ind, idx)
                ok = ~np.isnan(g[:, 6])
                idx, side, g = idx[ok], side[ok], g[ok]
                hit_s = np.where(side > 0, g[:, 0], g[:, 1])
                hit_o = np.where(side > 0, g[:, 1], g[:, 0])
                names, ex = study_exits(ind, color, mom, idx, side)
                rows.append(pd.DataFrame(dict(kind=kind, sym=sym, tf=tf, side=np.where(side > 0, "LONG", "SHORT"),
                                              per=np.where(df.index[idx] < split, "tr", "te"), win=100 * hit_s,
                                              edge=50.0 * (hit_s - hit_o), opp=ex[:, names.index("Opposite color starts")],
                                              hold=ex[:, names.index("Hold to 15:55")])))
            # random entries (same window 9:35-15:30), graded as a long AND as a short
            pool = np.nonzero((hm >= 935) & (hm < 1530))[0]
            ridx = np.sort(rng.choice(pool, size=min(len(pool), int(os.getenv("SIDES_RANDOM", "4000"))), replace=False))
            g = grade_two_sided(ind, ridx)
            ok = ~np.isnan(g[:, 6])
            ridx, g = ridx[ok], g[ok]
            per = np.where(df.index[ridx] < split, "tr", "te")
            for sd, nm in ((1, "LONG"), (-1, "SHORT")):
                names, ex = study_exits(ind, color, mom, ridx, np.full(len(ridx), sd))
                hs, ho = (g[:, 0], g[:, 1]) if sd > 0 else (g[:, 1], g[:, 0])
                base_rows.append(pd.DataFrame(dict(sym=sym, tf=tf, side=nm, per=per, win=100 * hs, edge=50.0 * (hs - ho),
                                                   opp=ex[:, names.index("Opposite color starts")],
                                                   hold=ex[:, names.index("Hold to 15:55")])))
            print(f"  {sym} {tf}m done ({time.time() - t0:.0f}s)", flush=True)
        del df1
    E = pd.concat(rows, ignore_index=True)
    B = pd.concat(base_rows, ignore_index=True)
    pn = {"tr": f"{START[:4]}-{int(SPLIT[:4]) - 1}", "te": f"{SPLIT[:4]}-now"}
    nC = len(SYMBOLS) * len(ST_TFS)

    def usd(r_, sym, tf):
        return r_ * atrnow[(sym, tf)] * DELTA * 100 - 2.0

    def summ(kind, sd):
        g = E[(E["kind"] == kind) & (E["side"] == sd)]
        out = {}
        for p_ in ("tr", "te"):
            gp, bp = g[g["per"] == p_], B[(B["side"] == sd) & (B["per"] == p_)]
            out[p_] = dict(n=len(gp), win=gp["win"].mean(), edge=gp["edge"].mean(), bedge=bp["edge"].mean(),
                           opp=gp["opp"].mean(), hold=gp["hold"].mean(), bhold=bp["hold"].mean())
        te = g[g["per"] == "te"]
        bte = B[(B["side"] == sd) & (B["per"] == "te")]
        ce = te.groupby(["sym", "tf"])["edge"].mean()
        be = bte.groupby(["sym", "tf"])["edge"].mean()
        out["beat"] = int(sum(1 for k_ in ce.index if ce[k_] > be.get(k_, 0)))
        out["charts"] = len(ce)
        dl = [usd(r_, s_, t_) for s_, t_, r_ in te[["sym", "tf", "hold"]].itertuples(index=False) if not np.isnan(r_)]
        out["usd"] = float(np.mean(dl)) if dl else np.nan
        return out

    md = [f"# LONGS vs SHORTS - SUPER, SUPER+, GAP & GO - {datetime.now(NY):%Y-%m-%d %H:%M} ET",
          f"Data {START} to {end:%Y-%m-%d}, {', '.join(SYMBOLS)}, {', '.join(f'{t}m' for t in ST_TFS)}. DATA ONLY. "
          f"Runtime {(time.time() - t0) / 60:.0f} min.",
          "**Win %** = hit +1 ATR your way before -1 ATR against you. **Edge** = that minus the other way, halved (0 = coin flip). "
          "**Random** = random candles 9:35-15:30 traded the SAME direction (longs drift up in a rising market, so a random "
          "long is not exactly 0). **vs random** = the signal's edge minus random's - this is the fair score. "
          "**Charts beat random** = charts (of 8) where the signal beat random in TEST. **Hold** = ATR per trade held to "
          "15:55, **Opp** = held until the opposite color (3 ATR safety stop), ~$ = rough per option (0.6 delta, $2 costs, no time decay). "
          "Luck check: on RANDOM price data this test showed long-vs-short gaps of up to ~3 by chance, so only a gap that "
          "holds in BOTH periods on 6+ of 8 charts counts.", ""]
    ans = ["## The answer in 30 seconds"]
    tbl = ["## Every number", "| Signal | Side | Period | Signals | Win % | Edge | Random edge | **vs random** | Opp (ATR) | Hold (ATR) | Random hold |",
           "|---|---|---|---|---|---|---|---|---|---|---|"]
    for kind in ("SUPER+", "SUPER", "GAP & GO"):
        S = {sd: summ(kind, sd) for sd in ("LONG", "SHORT")}
        parts = []
        for sd in ("LONG", "SHORT"):
            t_, r_ = S[sd]["te"], S[sd]["tr"]
            parts.append(f"{sd}S {t_['edge'] - t_['bedge']:+.1f} vs random in TEST ({r_['edge'] - r_['bedge']:+.1f} in TRAIN), "
                         f"beat random on {S[sd]['beat']}/{S[sd]['charts']} charts, hold {t_['hold']:+.2f} ATR ≈ ${S[sd]['usd']:+.0f}, "
                         f"{t_['n']} signals")
            for p_ in ("tr", "te"):
                d = S[sd][p_]
                tbl.append(f"| {kind} | {sd} | {pn[p_]} | {d['n']} | {d['win']:.0f}% | {d['edge']:+.1f} | {d['bedge']:+.1f} | "
                           f"**{d['edge'] - d['bedge']:+.1f}** | {d['opp']:+.2f} | {d['hold']:+.2f} | {d['bhold']:+.2f} |")
        def strong(sd):
            return ((S[sd]["te"]["edge"] - S[sd]["te"]["bedge"]) > 1.0 and (S[sd]["tr"]["edge"] - S[sd]["tr"]["bedge"]) > 1.0
                    and S[sd]["beat"] >= 6)
        good = [sd for sd in S if strong(sd)]
        if len(good) == 2:
            verdict = "both sides beat random (1.0+ in both periods, 6+ of 8 charts)"
        elif len(good) == 1:
            verdict = f"**{good[0]}S are better** - only {good[0]}S beat random by 1.0+ in both periods on 6+ of 8 charts"
        else:
            verdict = "no clear winner - neither side beats random by 1.0+ in both periods on 6+ of 8 charts (differences could be luck)"
        small = [sd for sd in S if S[sd]["te"]["n"] < 100]
        ans.append(f"- **{kind}**: {verdict}. " + " | ".join(parts) +
                   (f" - few TEST signals for {', '.join(small)}, so treat with care" if small else ""))
    ans.append("")
    per_chart = ["## TEST edge vs random, every chart", "| Signal | Side | " + " | ".join(f"{s_} {t_}m" for s_ in SYMBOLS for t_ in ST_TFS) + " |",
                 "|---|---|" + "---|" * nC]
    for kind in ("SUPER+", "SUPER", "GAP & GO"):
        for sd in ("LONG", "SHORT"):
            cells = []
            for s_ in SYMBOLS:
                for t_ in ST_TFS:
                    g = E[(E["kind"] == kind) & (E["side"] == sd) & (E["per"] == "te") & (E["sym"] == s_) & (E["tf"] == t_)]
                    b = B[(B["side"] == sd) & (B["per"] == "te") & (B["sym"] == s_) & (B["tf"] == t_)]
                    cells.append(f"{g['edge'].mean() - b['edge'].mean():+.1f} ({len(g)})" if len(g) else "-")
            per_chart.append(f"| {kind} | {sd} | " + " | ".join(cells) + " |")
    text = "\n".join(md + ans + tbl + [""] + per_chart + [""])
    print("\n" + text)
    stamp = datetime.now(NY).strftime("%Y-%m-%d")
    for path in (f"{OUT}/sides_{stamp}.md", f"{OUT}/sides_latest.md"):
        with open(path, "w") as f:
            f.write(text + "\n")
    sm = os.getenv("GITHUB_STEP_SUMMARY")
    if sm:
        with open(sm, "a") as f:
            f.write(text + "\n")


# ================================================================ TREND FLIP v2.7, LAST 2 YEARS (MODE=v27)
def v27_gate(st, sig, okL, okS, inT, W):
    """Pine f_gate: the flip arms a trade; it fires when the filter passes (same candle or up to W later, same color)."""
    ent = np.zeros(len(st), dtype=np.int64)
    arm, armB = 0, 0
    for i in range(len(st)):
        if sig[i] != 0:
            arm, armB = sig[i], 0
        elif arm != 0:
            armB += 1
        if arm != 0 and (st[i] != arm or armB > W or not inT[i]):
            arm = 0
        if arm != 0 and (okL[i] if arm == 1 else okS[i]):
            ent[i] = arm
            arm = 0
    return ent


def v27_sim(ind, sig, ent, mode, hold=15, stop=2.0, arm=2.0, dist=2.0, grace=2, min_hold=15, max_hold=60, flat=1555):
    """Pine f_sim, one trade at a time. mode 1 time, 2 color, 3 hybrid, 4 trail."""
    o, h, l, c, a, hm, day, st = ind["o"], ind["h"], ind["l"], ind["c"], ind["atr"], ind["hm"], ind["day"], ind["st"]
    n = len(o)
    out = []
    starts = np.nonzero(ent)[0]
    k, free = 0, 0
    while k < len(starts):
        i = starts[k]
        k += 1
        e = i + 1
        if i < free or e >= n or day[e] != day[i]:
            continue
        sd = int(ent[i])
        en = o[e]
        ea = a[e - 1] if not np.isnan(a[e - 1]) else a[e]
        if not ea or np.isnan(ea):
            continue
        stp = en - sd * stop * ea
        best, worst, bestj, lost, trl, ft = 0.0, 0.0, e, 0, np.nan, 0
        j = e
        while True:
            held = j - e + 1
            lost = lost + 1 if st[j] != sd else 0
            fav = (h[j] - en) if sd == 1 else (en - l[j])
            adv = (en - l[j]) if sd == 1 else (h[j] - en)
            if ft == 0:
                ft = -1 if adv >= ea else (1 if fav >= ea else 0)
            if fav > best:
                best, bestj = fav, j
            worst = max(worst, adv)
            last = j + 1 >= n or day[j + 1] != day[j]
            code, px = 0, np.nan
            if (l[j] <= stp) if sd == 1 else (h[j] >= stp):
                code, px = 1, (min(o[j], stp) if sd == 1 else max(o[j], stp))
            else:
                if mode == 4 and best >= arm * ea:
                    nt = en + sd * best - sd * dist * ea
                    trl = nt if np.isnan(trl) else (max(trl, nt) if sd == 1 else min(trl, nt))
                too_long = False if mode == 2 else (held >= max_hold if mode in (3, 4) else held >= hold)
                color_out = lost >= grace if mode == 2 else ((held >= min_hold and lost >= grace) if mode == 3 else False)
                trail_out = mode == 4 and not np.isnan(trl) and ((c[j] <= trl) if sd == 1 else (c[j] >= trl))
                if trail_out:
                    code = 4
                elif color_out:
                    code = 3
                elif sig[j] == -sd:
                    code = 5
                elif too_long:
                    code = 2
                elif hm[j] >= flat or last:
                    code = 6
                if code:
                    px = c[j]
            if code:
                out.append((i, e, j, sd, en, px, sd * (px - en) / ea, held, best / ea, worst / ea, bestj - e + 1, ft, code))
                free = j + 1
                break
            j += 1
    cols = ["i", "e", "x", "side", "entry", "exit", "r", "held", "best", "worst", "tbest", "first", "code"]
    return pd.DataFrame(out, columns=cols)


def v27_money(t, df, iv, tf, p_now):
    """0DTE / 1DTE option $ per contract (1 strike out of the money, today's price level, $2 costs)."""
    t = t.copy()
    if not len(t):
        t["d0"] = []
        t["d1"] = []
        return t
    mod = (df.index.hour * 60 + df.index.minute).to_numpy()
    e, x = t["e"].to_numpy(), t["x"].to_numpy()
    S0, S1 = t["entry"].to_numpy(), t["exit"].to_numpy()
    call = t["side"].to_numpy() == 1
    K = np.where(call, np.floor(S0) + 1.0, np.ceil(S0) - 1.0)
    rem0 = np.maximum(960.0 - mod[e], 1.0)
    rem1 = np.maximum(960.0 - (mod[x] + tf), 0.5)
    sg = np.nan_to_num(iv[e], nan=0.18)
    scale = p_now / S0 * 100.0
    ym = 252.0 * 390.0
    for kk, extra in (("d0", 0.0), ("d1", 390.0)):
        v0 = bs_price(S0, K, (rem0 + extra) / ym, sg, call)
        v1 = bs_price(S1, K, (rem1 + extra) / ym, sg, call)
        t[kk] = (v1 - v0) * scale - COST
    return t


def v27_main():
    end = datetime.now(timezone.utc) - timedelta(days=1)
    yrs_back = float(os.getenv("V27_YEARS", "2"))
    start = end - timedelta(days=int(365.25 * yrs_back) + 40)        # +40 days of warm-up for the indicators
    t_from = pd.Timestamp(end - timedelta(days=int(365.25 * yrs_back))).tz_convert(NY)
    half = pd.Timestamp(end - timedelta(days=int(365.25 * yrs_back / 2))).tz_convert(NY)
    test = os.getenv("TEST", "") == "1"
    os.makedirs(OUT, exist_ok=True)
    t0 = time.time()
    HOLDS = [5, 10, 15, 20, 25, 30, 40, 60]
    EXITS = [(f"Time: hold {hh}", dict(mode=1, hold=hh)) for hh in HOLDS] + [
        ("Trail 2/2 (max 60)", dict(mode=4)), ("Hybrid 15-60", dict(mode=3)), ("Color lost 2", dict(mode=2))]
    rng = np.random.default_rng(11)
    R = {}            # (sym, tf, exit) -> trades
    F = {}            # (sym, tf, filter) -> trades (Time 15)
    EQ = {}           # (sym, tf, filter) -> entry quality edge
    META = {}
    for sym in SYMBOLS:
        print(f"\n=== {sym} ===", flush=True)
        df1, feed = fake_1m(sym, start, end) if test else fetch_1m(sym, start, end)
        for tf in ST_TFS:
            df = to_tf(df1, rth_only=False, mins=tf)
            ind = indicators(df, 13, 34, True)
            st, hm = ind["st"], ind["hm"]
            inT = (hm >= 935) & (hm < 1530) & (df.index >= t_from)
            prev = np.r_[0, st[:-1]]
            sig = np.where(inT & (st != 0) & (st != prev), st, 0)
            c, hh_, ll_ = df["close"], df["high"], df["low"]
            lo14, hi14 = ll_.rolling(14).min(), hh_.rolling(14).max()
            K = (100 * (c - lo14) / (hi14 - lo14).replace(0, np.nan)).rolling(3).mean()
            D = K.rolling(3).mean()
            K, D = K.to_numpy(), D.to_numpy()
            basis = c.rolling(20).mean()
            mid = ((hh_.rolling(20).max() + ll_.rolling(20).min()) / 2 + basis) / 2
            mom = linreg_last((c - mid).to_numpy(), 20)
            momp = np.r_[np.nan, mom[:-1]]
            fa, ga = bars_since(ind["fear"]), bars_since(ind["greed"])
            ones = np.ones(len(st), dtype=bool)
            FILT = [("No filter (trend line only)", ones, ones), ("Stoch Room (L<80 / S>20)", K < 80, K > 20),
                    ("Stoch Agree (%K vs %D)", K > D, K < D), ("TTM Agrees (momentum side)", mom > 0, mom < 0),
                    ("TTM Rising (momentum turning)", mom > momp, mom < momp),
                    ("VF Not stretched", ~ind["greed"], ~ind["fear"]), ("YOURS: VF After spike (10 c)", fa <= 10, ga <= 10)]
            ents = {}
            for nm, okL, okS in FILT:
                ents[nm] = v27_gate(st, sig, np.nan_to_num(okL, nan=0).astype(bool), np.nan_to_num(okS, nan=0).astype(bool), inT, 5)
            ent = ents["YOURS: VF After spike (10 c)"]
            ents["YOURS, flip candle only (no wait)"] = v27_gate(st, sig, fa <= 10, ga <= 10, inT, 0)
            lv = daily_levels(df1, df)
            iv = (lv["datr"] / lv["pdc"]).to_numpy() / 1.6 * np.sqrt(252.0) * 1.15
            rth = (hm >= 930) & (hm < 1600)
            dd_ = np.array(df.index.date)
            last20 = np.array(sorted(set(dd_[rth])))[-20:]
            atr_now = float(np.nanmean(ind["atr"][rth & np.isin(dd_, last20)]))
            p_now = float(ind["c"][rth][-1])
            days = np.array(sorted(set(dd_[rth & (df.index >= t_from)])))
            META[(sym, tf)] = dict(atr=atr_now, px=p_now, days=days)
            for nm, kw in EXITS:
                t = v27_money(v27_sim(ind, sig, ent, **kw), df, iv, tf, p_now)
                t["time"] = df.index[t["e"].to_numpy()] if len(t) else []
                R[(sym, tf, nm)] = t
                # coin flip: the same entry times, random direction (5 draws)
                if nm == "Time: hold 15":
                    cf = []
                    for _ in range(5):
                        rnd = np.where(ent != 0, rng.choice([-1, 1], size=len(ent)), 0)
                        cf.append(v27_sim(ind, sig, rnd, **kw)["r"].mean())
                    META[(sym, tf)]["coin"] = float(np.nanmean(cf))
            for nm, e_ in ents.items():
                t = v27_money(v27_sim(ind, sig, e_, mode=1, hold=15), df, iv, tf, p_now)
                t["time"] = df.index[t["e"].to_numpy()] if len(t) else []
                F[(sym, tf, nm)] = t
                idx = np.nonzero(e_)[0]
                g = grade_two_sided(ind, idx)
                okg = ~np.isnan(g[:, 6])
                sd = e_[idx][okg]
                g = g[okg]
                EQ[(sym, tf, nm)] = (float(np.mean(50.0 * (np.where(sd > 0, g[:, 0], g[:, 1]) - np.where(sd > 0, g[:, 1], g[:, 0])))) if len(g) else np.nan,
                                     float(100 * np.mean(np.where(sd > 0, g[:, 0], g[:, 1]))) if len(g) else np.nan)
            print(f"  {sym} {tf}m: {int((ent != 0).sum())} signals ({time.time() - t0:.0f}s)", flush=True)
        del df1

    def stat(t, sym, tf):
        n = len(t)
        if not n:
            return None
        r = t["r"].to_numpy()
        gw, gl = r[r > 0].sum(), -r[r < 0].sum()
        h1, h2 = t[t["time"] < half], t[t["time"] >= half]
        cum0 = np.cumsum(t["d0"].to_numpy())
        dd0 = float(np.max(np.maximum.accumulate(np.r_[0, cum0])[1:] - cum0)) if n else 0.0
        cum1 = np.cumsum(t["d1"].to_numpy())
        dd1 = float(np.max(np.maximum.accumulate(np.r_[0, cum1])[1:] - cum1)) if n else 0.0
        cumr = np.cumsum(r)
        ddr = float(np.max(np.maximum.accumulate(np.r_[0, cumr])[1:] - cumr))
        lose = (r <= 0).astype(int)
        run_, mx = 0, 0
        for v in lose:
            run_ = run_ + 1 if v else 0
            mx = max(mx, run_)
        yrs = max(len(META[(sym, tf)]["days"]) / 252.0, 1e-9)
        dly = t.groupby(pd.DatetimeIndex(t["time"]).date)["d0"].sum().reindex(META[(sym, tf)]["days"], fill_value=0.0).to_numpy()
        return dict(n=n, per_yr=n / yrs, win=100 * (r > 0).mean(), avg=r.mean(), pf=gw / gl if gl > 0 else np.inf,
                    h1=h1["r"].mean() if len(h1) else np.nan, h2=h2["r"].mean() if len(h2) else np.nan,
                    d0=t["d0"].mean(), d1=t["d1"].mean(), y0=t["d0"].sum() / yrs, y1=t["d1"].sum() / yrs,
                    dd0=dd0, dd1=dd1, ddr=ddr, streak=mx, held=t["held"].mean() * tf, best=t["best"].mean(),
                    tbest=t["tbest"].mean() * tf, worst=t["worst"].mean(), daily=dly)

    S = {k: stat(v, k[0], k[1]) for k, v in R.items()}
    SF = {k: stat(v, k[0], k[1]) for k, v in F.items()}
    charts = [(s_, t_) for s_ in SYMBOLS for t_ in ST_TFS]
    exn = [e_[0] for e_ in EXITS]
    p1 = f"{t_from:%Y-%m-%d} to {half:%Y-%m-%d}"
    p2 = f"{half:%Y-%m-%d} to {end:%Y-%m-%d}"

    def money(x):
        return "-" if x is None or (isinstance(x, float) and np.isnan(x)) else f"{'+' if x >= 0 else '-'}${abs(x):,.0f}"

    md = [f"# TREND FLIP v2.7 - LAST {yrs_back:g} YEARS - {datetime.now(NY):%Y-%m-%d %H:%M} ET",
          f"Data {t_from:%Y-%m-%d} to {end:%Y-%m-%d}, {', '.join(SYMBOLS)}, {', '.join(f'{t}m' for t in ST_TFS)}. Setup = your v2.7 box: "
          "13/34 + VWAP flip, Vix Fix After spike within 10 candles (wait up to 5), entry at the next open, 2 ATR stop, "
          f"opposite flip exits, flat 15:55, one trade at a time. DATA ONLY - no orders. Runtime {(time.time() - t0) / 60:.0f} min.",
          "**ATR** = average result per trade in ATR (same as the box). **Year 1 / Year 2** = average ATR in each half "
          f"({p1} | {p2}) - an edge must hold in BOTH. **0DTE / 1DTE $** = per contract, 1 strike out of the money, "
          "Black-Scholes estimate at TODAY's price level incl. time decay and $2 costs (rough: real fills and IV moves differ). "
          "**Worst DD** = biggest peak-to-bottom drop of the running total (1 contract, every trade taken). "
          "**Coin flip** = the same entry times with a random direction, same exit.", ""]
    # ---- answer in 30 seconds
    ans = ["## The answer in 30 seconds"]
    pooled = []
    for nm in exn:
        rows = [S[(s_, t_, nm)] for s_, t_ in charts if S[(s_, t_, nm)]]
        if not rows:
            continue
        n = sum(r_["n"] for r_ in rows)
        avg = sum(r_["avg"] * r_["n"] for r_ in rows) / n
        both = sum(1 for r_ in rows if r_["h1"] > 0 and r_["h2"] > 0)
        d0 = sum(r_["d0"] * r_["n"] for r_ in rows) / n
        d1 = sum(r_["d1"] * r_["n"] for r_ in rows) / n
        pos0 = sum(1 for r_ in rows if r_["d0"] > 0)
        pooled.append((nm, n, avg, both, len(rows), d0, d1, pos0))
    coin = np.nanmean([META[k_].get("coin", np.nan) for k_ in charts])
    bestA = max(pooled, key=lambda z: z[2])
    best0 = max(pooled, key=lambda z: z[5])
    best1 = max(pooled, key=lambda z: z[6])
    ans.append(f"- **Best hold by ATR**: {bestA[0]} - {bestA[2]:+.2f} ATR per trade over {bestA[1]} trades, positive in both years on "
               f"{bestA[3]}/{bestA[4]} charts. Coin flip with the same entries (hold 15): {coin:+.2f} ATR.")
    ans.append(f"- **Best for 0DTE options**: {best0[0]} - {money(best0[5])} per trade per contract, positive on {best0[7]}/8 charts.")
    ans.append(f"- **Best for 1DTE options**: {best1[0]} - {money(best1[6])} per trade per contract.")
    pc = []
    for s_, t_ in charts:
        cand = [(nm, S[(s_, t_, nm)]) for nm in exn if S[(s_, t_, nm)] and S[(s_, t_, nm)]["n"] >= 20]
        good = [(nm, x) for nm, x in cand if x["h1"] > 0 and x["h2"] > 0 and x["d0"] > 0]
        if good:
            nm, x = max(good, key=lambda z: z[1]["d0"])
            pc.append(f"{s_} {t_}m: **{nm}** ({x['avg']:+.2f} ATR, 0DTE {money(x['d0'])}/trade, worst DD {money(-x['dd0'])})")
        else:
            pc.append(f"{s_} {t_}m: no exit was positive in both years AND on 0DTE")
    ans.append("- **Per chart (best exit that made money in both years and on 0DTE)**: " + " | ".join(pc))
    ans.append("")
    # ---- pooled exits
    tbl = ["## Every exit, all 8 charts together", "| Exit | Trades | Avg ATR | Charts + in both years | 0DTE $/trade | 1DTE $/trade | Charts + on 0DTE |",
           "|---|---|---|---|---|---|---|"]
    for nm, n, avg, both, nc, d0, d1, pos0 in pooled:
        tbl.append(f"| {nm} | {n} | **{avg:+.2f}** | {both}/{nc} | {money(d0)} | {money(d1)} | {pos0}/{nc} |")
    tbl.append("")
    # ---- per chart detail
    det = ["## Every chart, every exit",
           "| Chart | Exit | Trades/yr | Win % | ATR | PF | Year 1 | Year 2 | 0DTE $/trade | 1DTE $/trade | 0DTE $/yr | Worst DD 0DTE | Worst DD ATR | Losing run | Avg hold |",
           "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for s_, t_ in charts:
        for nm in exn:
            x = S[(s_, t_, nm)]
            if not x:
                continue
            det.append(f"| {s_} {t_}m | {nm} | {x['per_yr']:.0f} | {x['win']:.0f}% | **{x['avg']:+.2f}** | {x['pf']:.2f} | {x['h1']:+.2f} | {x['h2']:+.2f} | "
                       f"{money(x['d0'])} | {money(x['d1'])} | {money(x['y0'])} | {money(-x['dd0'])} | {x['ddr']:.1f} | {x['streak']} | {x['held']:.0f} min |")
    det.append("")
    # ---- how long to hold: the best move
    mv = ["## How long to hold - the average trade's best move (hold 60 run, ATR)",
          "| Chart | Coin flip ATR (hold 15) | Best move | ...reached after | Worst move against | Entry quality: +1 ATR first | Edge vs coin flip |",
          "|---|---|---|---|---|---|---|"]
    for s_, t_ in charts:
        x = S[(s_, t_, "Time: hold 60")]
        eq = EQ[(s_, t_, "YOURS: VF After spike (10 c)")]
        if x:
            mv.append(f"| {s_} {t_}m | {META[(s_, t_)].get('coin', np.nan):+.2f} | +{x['best']:.2f} | {x['tbest']:.0f} min | -{x['worst']:.2f} | {eq[1]:.0f}% | {eq[0]:+.1f} |")
    mv.append("")
    # ---- filter lab
    fl = ["## FILTER LAB (exit = Time hold 15, like your box) - all 8 charts",
          "| Filter | Trades | Avg ATR | Charts + in both years | 0DTE $/trade | Edge vs coin flip (+1 ATR first, 0 = coin flip) |", "|---|---|---|---|---|---|"]
    for nm in list(ents.keys()):
        rows = [SF[(s_, t_, nm)] for s_, t_ in charts if SF[(s_, t_, nm)]]
        if not rows:
            continue
        n = sum(r_["n"] for r_ in rows)
        avg = sum(r_["avg"] * r_["n"] for r_ in rows) / n
        both = sum(1 for r_ in rows if r_["h1"] > 0 and r_["h2"] > 0)
        d0 = sum(r_["d0"] * r_["n"] for r_ in rows) / n
        edge = np.nanmean([EQ[(s_, t_, nm)][0] for s_, t_ in charts])
        fl.append(f"| {nm} | {n} | **{avg:+.2f}** | {both}/{len(rows)} | {money(d0)} | {edge:+.1f} |")
    fl.append("")
    # ---- Monte Carlo for the best 0DTE exit per chart
    mc = ["## Monte Carlo - 10,000 shuffled years of the best 0DTE exit on each chart (1 contract)", MC_HEAD]
    for s_, t_ in charts:
        cand = [(nm, S[(s_, t_, nm)]) for nm in exn if S[(s_, t_, nm)]]
        nm, x = max(cand, key=lambda z: z[1]["d0"])
        m = monte_carlo(x["daily"], seed=17 + t_ + (0 if s_ == "SPY" else 100))
        mc.append(mc_row(f"{s_} {t_}m {nm}", "0DTE", f"{len(META[(s_, t_)]['days'])} days", m, x["per_yr"]))
    mc.append("")
    text = "\n".join(md + ans + tbl + mv + fl + mc + det)
    print("\n" + text)
    stamp = datetime.now(NY).strftime("%Y-%m-%d")
    for path in (f"{OUT}/v27_{stamp}.md", f"{OUT}/v27_latest.md"):
        with open(path, "w") as f:
            f.write(text + "\n")
    sm = os.getenv("GITHUB_STEP_SUMMARY")
    if sm:
        with open(sm, "a") as f:
            f.write(text + "\n")


# ================================================================ STOCH SCALP PRO, LAST 2 YEARS (MODE=stoch)
def stoch_hook(df, kl, ks, ds, look=3, os_=20.0, ob=80.0):
    c, h, l = df["close"], df["high"], df["low"]
    lo, hi = l.rolling(kl).min(), h.rolling(kl).max()
    k = (100 * (c - lo) / (hi - lo).replace(0, np.nan)).rolling(ks).mean()
    d = k.rolling(ds).mean()
    up = (k > d) & (k.shift(1) <= d.shift(1))
    dn = (k < d) & (k.shift(1) >= d.shift(1))
    lg = up & (k.rolling(look).min() < os_) & (k < 50)
    sh = dn & (k.rolling(look).max() > ob) & (k > 50)
    return np.where(lg.fillna(False), 1, np.where(sh.fillna(False), -1, 0)), k.to_numpy()


def stoch_sim(ind, sig, stop=3.0, tp=0.0, maxb=40, cd=3, slip=0.02, flat=1555, tf=1):
    """Pine f_sim of Stoch Pro v1.2: enter at the open after a signal bar, stop first, then target, then time / 15:55."""
    o, h, l, c, a, hm, day = ind["o"], ind["h"], ind["l"], ind["c"], ind["atr"], ind["hm"], ind["day"]
    n = len(o)
    out = []
    last_x = -10**9
    k = 0
    starts = np.nonzero(sig)[0]
    free = 0
    hm_end = (hm // 100 * 60 + hm % 100 + tf)
    hm_end = (hm_end // 60) * 100 + hm_end % 60
    while k < len(starts):
        i = starts[k]
        k += 1
        e = i + 1
        if e < free or e >= n or e - last_x < cd or not a[i] or np.isnan(a[i]):
            continue
        sd = int(sig[i])
        en, ea = o[e], a[i]
        sl = en - sd * stop * ea
        tpp = en + sd * tp * ea if tp > 0 else np.nan
        j = e
        best = worst = 0.0
        while True:
            fav = (h[j] - en) if sd == 1 else (en - l[j])
            adv = (en - l[j]) if sd == 1 else (h[j] - en)
            best, worst = max(best, fav), max(worst, adv)
            oc, px = 0, np.nan
            if (l[j] <= sl) if sd == 1 else (h[j] >= sl):
                oc, px = 1, (min(o[j], sl) if sd == 1 else max(o[j], sl))
            elif not np.isnan(tpp) and ((h[j] >= tpp) if sd == 1 else (l[j] <= tpp)):
                oc, px = 2, (max(o[j], tpp) if sd == 1 else min(o[j], tpp))
            elif j - e + 1 >= maxb or (hm_end[j] >= flat and hm[j] < 1600) or j + 1 >= n or day[j + 1] != day[j]:
                oc, px = 3, c[j]
            if oc:
                mv = (sd * (px - en) - 2.0 * slip * ea) / ea
                out.append((i, e, j, sd, en, px, mv, j - e + 1, best / ea, worst / ea, oc))
                last_x, free = j, j + 1
                break
            j += 1
    return pd.DataFrame(out, columns=["i", "e", "x", "side", "entry", "exit", "r", "held", "best", "worst", "code"])


def opt_money(t, df, iv, tf, p_now, atr_now):
    """0DTE ATM, 0DTE 1 strike out, 1DTE ATM per contract (Black-Scholes, today's price level, $2 costs) + the box's $."""
    t = t.copy()
    if not len(t):
        for kk in ("atm0", "otm0", "atm1", "box"):
            t[kk] = []
        return t
    mod = (df.index.hour * 60 + df.index.minute).to_numpy()
    e, x = t["e"].to_numpy(), t["x"].to_numpy()
    S0, S1 = t["entry"].to_numpy(), t["exit"].to_numpy()
    call = t["side"].to_numpy() == 1
    rem0 = np.maximum(960.0 - mod[e], 1.0)
    rem1 = np.maximum(960.0 - (mod[x] + tf), 0.5)
    sg = np.nan_to_num(iv[e], nan=0.18)
    scale = p_now / S0 * 100.0
    ym = 252.0 * 390.0
    for kk, K, extra in (("atm0", np.round(S0), 0.0), ("otm0", np.where(call, np.floor(S0) + 1.0, np.ceil(S0) - 1.0), 0.0),
                         ("atm1", np.round(S0), 390.0)):
        v0 = bs_price(S0, K, (rem0 + extra) / ym, sg, call)
        v1 = bs_price(S1, K, (rem1 + extra) / ym, sg, call)
        t[kk] = (v1 - v0) * scale - COST
    hrs = (t["held"].to_numpy() * tf) / 60.0
    t["box"] = 0.5 * t["r"].to_numpy() * atr_now * 100.0 - 8.0 * hrs
    return t


def stoch_main():
    end = datetime.now(timezone.utc) - timedelta(days=1)
    yrs_back = float(os.getenv("STOCH_YEARS", "2"))
    start = end - timedelta(days=int(365.25 * yrs_back) + 40)
    t_from = pd.Timestamp(end - timedelta(days=int(365.25 * yrs_back))).tz_convert(NY)
    half = pd.Timestamp(end - timedelta(days=int(365.25 * yrs_back / 2))).tz_convert(NY)
    test = os.getenv("TEST", "") == "1"
    os.makedirs(OUT, exist_ok=True)
    t0 = time.time()
    STOPS, TPS = [1.0, 1.5, 2.0, 3.0], [0.5, 1.0, 2.0, 3.0, 5.0, 0.0]
    HOLDS = [5, 10, 15, 20, 30, 40, 48, 60]
    MAIN = [("YOUR Oct 14 box: stop 3, no target, 40 bars", 3.0, 0.0, 40), ("YOUR Oct 15 box: stop 3, TP 5, 40 bars", 3.0, 5.0, 40),
            ("v1.2 default: stop 2, no target, 40 bars", 2.0, 0.0, 40)]
    T, META, EQ, CURVE = {}, {}, {}, {}
    rng = np.random.default_rng(5)
    for sym in SYMBOLS:
        print(f"\n=== {sym} ===", flush=True)
        df1, feed = fake_1m(sym, start, end) if test else fetch_1m(sym, start, end)
        for tf in ST_TFS:
            df = to_tf(df1, rth_only=False, mins=tf)
            ind = indicators(df, 21, 50, False)
            hm = ind["hm"]
            c, o_ = df["close"].to_numpy(), df["open"].to_numpy()
            hh_, ll_ = df["high"].to_numpy(), df["low"].to_numpy()
            ef = df["close"].ewm(span=21, adjust=False).mean().to_numpy()
            es = df["close"].ewm(span=50, adjust=False).mean().to_numpy()
            trU, trD = ef > es, ef < es
            vwU, vwD = c > ind["vwap"], c < ind["vwap"]
            h5 = htf_state(df, 21, 50, 5)
            hU, hD = h5 == 1, h5 == -1
            rg = hh_ - ll_
            clv = np.where(rg > 0, (c - ll_) / np.where(rg > 0, rg, 1), 0.5)
            paU, paD = (c > o_) & (clv >= 0.5), (c < o_) & (clv <= 0.5)
            inT = (hm >= 935) & (hm < 1530) & (df.index >= t_from)
            hook, K = stoch_hook(df, 14, 3, 3)
            hkF, _ = stoch_hook(df, 5, 3, 3)
            hkS, _ = stoch_hook(df, 21, 5, 5)

            def filt(hk, lvl):
                L = (hk == 1) & inT
                S_ = (hk == -1) & inT
                if lvl == 9:                                   # your switches (v1.2 defaults): trend + price
                    L, S_ = L & trU & paU, S_ & trD & paD
                else:
                    if lvl >= 2:
                        L, S_ = L & trU, S_ & trD
                    if lvl >= 3:
                        L, S_ = L & vwU, S_ & vwD
                    if lvl >= 4:
                        L, S_ = L & hU, S_ & hD
                    if lvl >= 5:
                        L, S_ = L & paU, S_ & paD
                return np.where(L, 1, np.where(S_, -1, 0))
            SIG = {"1 hook": filt(hook, 1), "2 +trend": filt(hook, 2), "3 +VWAP": filt(hook, 3), "4 +5m": filt(hook, 4),
                   "5 +price": filt(hook, 5), "Fast 5-3-3 (trend + price)": filt(hkF, 9), "Slow 21-5-5 (trend + price)": filt(hkS, 9),
                   "LIVE: trend + price (your switches)": filt(hook, 9)}
            live = SIG["LIVE: trend + price (your switches)"]
            lv = daily_levels(df1, df)
            iv = (lv["datr"] / lv["pdc"]).to_numpy() / 1.6 * np.sqrt(252.0) * 1.15
            rth = (hm >= 930) & (hm < 1600)
            dd_ = np.array(df.index.date)
            last20 = np.array(sorted(set(dd_[rth])))[-20:]
            atr_now = float(np.nanmean(ind["atr"][rth & np.isin(dd_, last20)]))
            p_now = float(ind["c"][rth][-1])
            days = np.array(sorted(set(dd_[rth & (df.index >= t_from)])))
            META[(sym, tf)] = dict(atr=atr_now, px=p_now, days=days)

            def run_(sg, stop, tp, mb):
                t = opt_money(stoch_sim(ind, sg, stop, tp, mb, tf=tf), df, iv, tf, p_now, atr_now)
                t["time"] = df.index[t["e"].to_numpy()] if len(t) else []
                return t
            for nm, sg in SIG.items():
                T[(sym, tf, "lvl", nm)] = run_(sg, 3.0, 0.0, 40)
                idx = np.nonzero(sg)[0]
                g = grade_two_sided(ind, idx)
                okg = ~np.isnan(g[:, 6])
                sd, g = sg[idx][okg], g[okg]
                EQ[(sym, tf, nm)] = float(np.mean(50.0 * (np.where(sd > 0, g[:, 0], g[:, 1]) - np.where(sd > 0, g[:, 1], g[:, 0])))) if len(g) else np.nan
            for nm, stp, tpp, mb in MAIN:
                T[(sym, tf, "main", nm)] = run_(live, stp, tpp, mb)
            rnd = np.where(live != 0, rng.choice([-1, 1], size=len(live)), 0)
            T[(sym, tf, "main", "COIN FLIP: same entries, random direction (stop 3, 40 bars)")] = run_(rnd, 3.0, 0.0, 40)
            for stp in STOPS:
                for tpp in TPS:
                    T[(sym, tf, "grid", (stp, tpp))] = run_(live, stp, tpp, 40)
            for mb in HOLDS:
                T[(sym, tf, "hold", mb)] = run_(live, 3.0, 0.0, mb)
            # hold curve: every live fire, no stop, same day, measured after 3/6/12/24/48 bars
            idx = np.nonzero(live)[0]
            cur = {}
            for hb in (3, 6, 12, 24, 48):
                mvs, pks, hts = [], [], []
                for i in idx:
                    e, x = i + 1, i + hb
                    if x >= len(c) or dd_[x] != dd_[i] or np.isnan(ind["atr"][i]) or not ind["atr"][i]:
                        continue
                    sd = live[i]
                    a_ = ind["atr"][i]
                    en = o_[e]
                    mvs.append(sd * (c[x] - en) / a_)
                    pks.append(((hh_[e:x + 1].max() - en) if sd == 1 else (en - ll_[e:x + 1].min())) / a_)
                    hts.append(((en - ll_[e:x + 1].min()) if sd == 1 else (hh_[e:x + 1].max() - en)) / a_)
                cur[hb] = (len(mvs), np.mean(mvs) if mvs else np.nan, np.mean(pks) if pks else np.nan,
                           np.mean(hts) if hts else np.nan, 100 * np.mean(np.array(mvs) > 0) if mvs else np.nan)
            CURVE[(sym, tf)] = cur
            print(f"  {sym} {tf}m: {int((live != 0).sum())} live signals ({time.time() - t0:.0f}s)", flush=True)
        del df1

    charts = [(s_, t_) for s_ in SYMBOLS for t_ in ST_TFS]

    def st(t, sym, tf):
        n = len(t)
        if not n:
            return None
        r = t["r"].to_numpy()
        gw, gl = r[r > 0].sum(), -r[r < 0].sum()
        h1, h2 = t[t["time"] < half], t[t["time"] >= half]
        yrs = max(len(META[(sym, tf)]["days"]) / 252.0, 1e-9)

        def ddv(col):
            cu = np.cumsum(t[col].to_numpy())
            return float(np.max(np.maximum.accumulate(np.r_[0, cu])[1:] - cu))
        run_, mx = 0, 0
        for v in (r <= 0):
            run_ = run_ + 1 if v else 0
            mx = max(mx, run_)
        dly = t.groupby(pd.DatetimeIndex(t["time"]).date)["atm0"].sum().reindex(META[(sym, tf)]["days"], fill_value=0.0).to_numpy()
        return dict(n=n, per_yr=n / yrs, win=100 * (r > 0).mean(), avg=r.mean(), pf=gw / gl if gl > 0 else np.inf,
                    h1=h1["r"].mean() if len(h1) else np.nan, h2=h2["r"].mean() if len(h2) else np.nan,
                    atm0=t["atm0"].mean(), otm0=t["otm0"].mean(), atm1=t["atm1"].mean(), box=t["box"].mean(),
                    y0=t["atm0"].sum() / yrs, dd0=ddv("atm0"), dd1=ddv("atm1"), ddb=ddv("box"),
                    ddr=float(np.max(np.maximum.accumulate(np.r_[0, np.cumsum(r)])[1:] - np.cumsum(r))),
                    streak=mx, held=t["held"].mean() * tf, daily=dly)

    S = {k_: st(v, k_[0], k_[1]) for k_, v in T.items()}

    def pool(kind, key):
        rows = [S[(s_, t_, kind, key)] for s_, t_ in charts if S.get((s_, t_, kind, key))]
        if not rows:
            return None
        n = sum(r_["n"] for r_ in rows)
        w = lambda f: sum(r_[f] * r_["n"] for r_ in rows) / n
        return dict(n=n, avg=w("avg"), win=w("win"), atm0=w("atm0"), otm0=w("otm0"), atm1=w("atm1"), box=w("box"),
                    both=sum(1 for r_ in rows if r_["h1"] > 0 and r_["h2"] > 0), pos0=sum(1 for r_ in rows if r_["atm0"] > 0),
                    pos1=sum(1 for r_ in rows if r_["atm1"] > 0), nc=len(rows))

    def m_(x):
        return "-" if x is None or (isinstance(x, float) and np.isnan(x)) else f"{'+' if x >= 0 else '-'}${abs(x):,.0f}"

    p1, p2 = f"{t_from:%Y-%m-%d} to {half:%Y-%m-%d}", f"{half:%Y-%m-%d} to {end:%Y-%m-%d}"
    md = [f"# STOCH SCALP PRO - LAST {yrs_back:g} YEARS - {datetime.now(NY):%Y-%m-%d %H:%M} ET",
          f"Data {t_from:%Y-%m-%d} to {end:%Y-%m-%d}, {', '.join(SYMBOLS)}, {', '.join(f'{t}m' for t in ST_TFS)}. Same rules as your Stoch Pro v1.2 box "
          "(Stoch 14-3-3 hook, LIVE = trend + price switches, entry next open, 3-bar cooldown, 0.02 ATR slippage a side, flat 15:55, "
          f"one trade at a time). DATA ONLY - no orders. Runtime {(time.time() - t0) / 60:.0f} min.",
          f"**ATR** = average result per trade in ATR. **Year 1 / Year 2** = {p1} | {p2} (an edge must hold in BOTH). "
          "**$ per contract**: **0DTE ATM** and **0DTE 1 out** (1 strike out of the money) and **1DTE ATM** = Black-Scholes estimate at "
          "today's prices incl. time decay and $2 costs; **Box $** = your box's own math (delta 0.50 x move - $8/hr theta). "
          "**Worst DD** = biggest drop of the running total, 1 contract, every trade taken. Rough: real fills and IV moves differ.", ""]
    ans = ["## The answer in 30 seconds"]
    for nm, *_ in MAIN + [("COIN FLIP: same entries, random direction (stop 3, 40 bars)",)]:
        p_ = pool("main", nm)
        if p_:
            ans.append(f"- **{nm}**: {p_['n']} trades | win {p_['win']:.0f}% | **{p_['avg']:+.2f} ATR** | both years + on {p_['both']}/{p_['nc']} charts | "
                       f"0DTE ATM {m_(p_['atm0'])} | 0DTE 1 out {m_(p_['otm0'])} | 1DTE {m_(p_['atm1'])} | box $ {m_(p_['box'])} per trade")
    gb = max(((stp, tpp) for stp in STOPS for tpp in TPS), key=lambda k_: pool("grid", k_)["atm0"] if pool("grid", k_) else -1e9)
    pg = pool("grid", gb)
    ans.append(f"- **Best stop / target for 0DTE (all charts)**: stop {gb[0]:g} ATR / {'no target' if gb[1] == 0 else f'TP {gb[1]:g} ATR'} -> "
               f"{m_(pg['atm0'])}/trade ATM, {pg['avg']:+.2f} ATR, positive on {pg['pos0']}/{pg['nc']} charts")
    hb = max(HOLDS, key=lambda k_: pool("hold", k_)["atm0"] if pool("hold", k_) else -1e9)
    ph = pool("hold", hb)
    ans.append(f"- **Best max hold for 0DTE (stop 3, no target)**: {hb} candles -> {m_(ph['atm0'])}/trade, {ph['avg']:+.2f} ATR")
    pc = []
    for s_, t_ in charts:
        cand = [(k_, S[(s_, t_, "grid", k_)]) for k_ in ((a_, b_) for a_ in STOPS for b_ in TPS) if S.get((s_, t_, "grid", k_))]
        cand = [(k_, x) for k_, x in cand if x["n"] >= 30 and x["h1"] > 0 and x["h2"] > 0 and x["atm0"] > 0]
        if cand:
            k_, x = max(cand, key=lambda z: z[1]["atm0"])
            pc.append(f"{s_} {t_}m: **stop {k_[0]:g} / {'no TP' if k_[1] == 0 else f'TP {k_[1]:g}'}** ({x['win']:.0f}% win, {x['avg']:+.2f} ATR, "
                      f"0DTE {m_(x['atm0'])}/trade, {m_(x['y0'])}/yr, worst DD {m_(-x['dd0'])})")
        else:
            pc.append(f"{s_} {t_}m: nothing made money on 0DTE in both years")
    ans.append("- **Per chart (best 0DTE stop/target that held up in both years)**: " + " | ".join(pc))
    ans.append("")
    lvl = ["## Setup levels (stop 3, no target, 40 bars) - all 8 charts",
           "| Setup | Trades | Win % | Avg ATR | Charts + both years | 0DTE ATM $ | 1DTE $ | Edge vs coin flip (+1 ATR first) |", "|---|---|---|---|---|---|---|---|"]
    for nm in SIG:
        p_ = pool("lvl", nm)
        if p_:
            eq = np.nanmean([EQ[(s_, t_, nm)] for s_, t_ in charts])
            lvl.append(f"| {nm} | {p_['n']} | {p_['win']:.0f}% | **{p_['avg']:+.2f}** | {p_['both']}/{p_['nc']} | {m_(p_['atm0'])} | {m_(p_['atm1'])} | {eq:+.1f} |")
    lvl.append("")
    grid = ["## Stop x target on your LIVE fires (40-bar max) - all 8 charts: avg ATR | 0DTE ATM $/trade | win %",
            "| Stop \\ Target | " + " | ".join("none" if x == 0 else f"{x:g} ATR" for x in TPS) + " |", "|---|" + "---|" * len(TPS)]
    for stp in STOPS:
        cells = []
        for tpp in TPS:
            p_ = pool("grid", (stp, tpp))
            cells.append(f"{p_['avg']:+.2f} / {m_(p_['atm0'])} / {p_['win']:.0f}%" + (" ★" if (stp, tpp) == gb else "") if p_ else "-")
        grid.append(f"| {stp:g} ATR | " + " | ".join(cells) + " |")
    grid.append("")
    hold = ["## How long to hold (stop 3, no target) - all 8 charts", "| Max hold (candles) | Trades | Win % | Avg ATR | 0DTE ATM $ | 0DTE 1 out $ | 1DTE $ | Charts + both years |",
            "|---|---|---|---|---|---|---|---|"]
    for mb in HOLDS:
        p_ = pool("hold", mb)
        if p_:
            hold.append(f"| {mb} | {p_['n']} | {p_['win']:.0f}% | **{p_['avg']:+.2f}** | {m_(p_['atm0'])} | {m_(p_['otm0'])} | {m_(p_['atm1'])} | {p_['both']}/{p_['nc']} |")
    hold.append("")
    cv = ["## Hold curve - every LIVE fire, no stop: average move after N candles (close / best / worst, ATR, win %)",
          "| Chart | 3 | 6 | 12 | 24 | 48 |", "|---|---|---|---|---|---|"]
    for s_, t_ in charts:
        cur = CURVE[(s_, t_)]
        cv.append(f"| {s_} {t_}m | " + " | ".join(f"{cur[hb_][1]:+.2f} / +{cur[hb_][2]:.2f} / -{cur[hb_][3]:.2f} / {cur[hb_][4]:.0f}%" for hb_ in (3, 6, 12, 24, 48)) + " |")
    cv.append("")
    det = ["## Every chart - your two box setups",
           "| Chart | Setup | Trades/yr | Win % | ATR | PF | Year 1 | Year 2 | 0DTE ATM $ | 0DTE 1 out $ | 1DTE $ | Box $ | 0DTE $/yr | Worst DD 0DTE | Worst DD 1DTE | Losing run | Avg hold |",
           "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for s_, t_ in charts:
        for nm, *_ in MAIN[:2] + [("COIN FLIP: same entries, random direction (stop 3, 40 bars)",)]:
            x = S.get((s_, t_, "main", nm))
            if x:
                det.append(f"| {s_} {t_}m | {nm.split(':')[0]} | {x['per_yr']:.0f} | {x['win']:.0f}% | **{x['avg']:+.2f}** | {x['pf']:.2f} | {x['h1']:+.2f} | {x['h2']:+.2f} | "
                           f"{m_(x['atm0'])} | {m_(x['otm0'])} | {m_(x['atm1'])} | {m_(x['box'])} | {m_(x['y0'])} | {m_(-x['dd0'])} | {m_(-x['dd1'])} | {x['streak']} | {x['held']:.0f} min |")
    det.append("")
    mc = ["## Monte Carlo - 10,000 shuffled years, best 0DTE stop/target on each chart (1 contract, ATM)", MC_HEAD]
    for s_, t_ in charts:
        cand = [(k_, S[(s_, t_, "grid", k_)]) for k_ in ((a_, b_) for a_ in STOPS for b_ in TPS) if S.get((s_, t_, "grid", k_))]
        k_, x = max(cand, key=lambda z: z[1]["atm0"])
        m = monte_carlo(x["daily"], seed=31 + t_ + (0 if s_ == "SPY" else 100))
        mc.append(mc_row(f"{s_} {t_}m stop {k_[0]:g} / {'no TP' if k_[1] == 0 else f'TP {k_[1]:g}'}", "0DTE ATM", f"{len(META[(s_, t_)]['days'])} days", m, x["per_yr"]))
    mc.append("")
    text = "\n".join(md + ans + lvl + grid + hold + cv + mc + det)
    print("\n" + text)
    stamp = datetime.now(NY).strftime("%Y-%m-%d")
    for path in (f"{OUT}/stoch_{stamp}.md", f"{OUT}/stoch_latest.md"):
        with open(path, "w") as f:
            f.write(text + "\n")
    sm = os.getenv("GITHUB_STEP_SUMMARY")
    if sm:
        with open(sm, "a") as f:
            f.write(text + "\n")


# ================================================================ VIX FIX RETEST + LEADERBOARD (MODE=vfx)
VFX_WIN = int(os.getenv("VFX_WIN", "30"))         # candles after the spike ends to find the bounce + retest (same day)
VFX_BOUNCE = float(os.getenv("VFX_BOUNCE", "1.0"))  # the bounce must reach at least this many ATR off the spike low
VFX_PULL = float(os.getenv("VFX_PULL", "0.5"))    # the retest gives back at least this share of the bounce
VFX_DRY = float(os.getenv("VFX_DRY", "0.5"))      # fear "dried up" = fear bar under this share of the spike's tallest bar
VFX_NAMES = ["VF1 retest, fear dried up", "VF2 retest + greed taller than fear (mirror flipped)",
             "VF3 mirror phase first, then VF2", "VF4 VF2 + first green candle (confirmed)",
             "VF5 lower low on a GRAY bar only (old divergence - missed red-bar divergences)", "VF0 reference: spike streak ends (tested before)"]


def vfx_pane(df):
    """Your VIX FIX pane: bar heights 0-100 = wvf / highest(wvf, 50) * 100 (fear) and the same for greed (wvi)."""
    c, h, l = df["close"], df["high"], df["low"]
    hc22, lc22 = c.rolling(22).max(), c.rolling(22).min()
    wvf, wvi = (hc22 - l) / hc22 * 100, (h - lc22) / lc22 * 100
    return (wvf / wvf.rolling(50).max() * 100).to_numpy(), (wvi / wvi.rolling(50).max() * 100).to_numpy()


def vfx_events(df, ind, trace=None):
    """Signals (+1 long / -1 short) on the CLOSED candle i; entry is at candle i+1's open. Uses only candles <= i.
    trace: optional list - every fire is appended as a dict (for the self-check)."""
    fN, gN = vfx_pane(df)
    fear = np.asarray(ind["fear"], dtype=bool)
    greed = np.asarray(ind["greed"], dtype=bool) & ~fear
    hm, day, a = ind["hm"], ind["day"], ind["atr"]
    O, H, L, C = ind["o"], ind["h"], ind["l"], ind["c"]
    n = len(H)
    out = {nm: np.zeros(n, dtype=np.int64) for nm in VFX_NAMES}
    win = (hm >= 935) & (hm < 1530)
    rth = (hm >= 930) & (hm < 1600)
    for side in (1, -1):
        spk = fear if side == 1 else greed
        mine = np.nan_to_num(fN if side == 1 else gN)     # the spike side's bar
        other = np.nan_to_num(gN if side == 1 else fN)
        in_spk = False
        s_day = None
        left = 0
        for i in range(n):
            if not rth[i]:
                continue
            if spk[i]:
                if not in_spk or day[i] != s_day:                      # a new spike streak
                    in_spk, s_day, s_ext, s_ht, s_i = True, day[i], (L[i] if side == 1 else H[i]), 0.0, i
                    done, mirror_n, bounce, armed4 = set(), 0, 0.0, -1
                s_ext = min(s_ext, L[i]) if side == 1 else max(s_ext, H[i])
                s_ht = max(s_ht, mine[i])
                left = 0
                continue
            if in_spk:                                                 # first candle after the streak
                in_spk, left = False, VFX_WIN
                if win[i] and day[i] == s_day:
                    out[VFX_NAMES[5]][i] = side
            if left <= 0 or day[i] != s_day or not (a[i] > 0):
                continue
            left -= 1
            m, o_ = mine[i], other[i]
            if 20 <= m <= 70 and 20 <= o_ <= 70 and 0.67 <= (m + 1e-9) / (o_ + 1e-9) <= 1.5:
                mirror_n += 1
            # the bounce so far (measured BEFORE this candle, so the retest candle can't be its own bounce)
            bounced = bounce >= VFX_BOUNCE * a[i]
            pulled = bounced and ((L[i] <= s_ext + (1 - VFX_PULL) * bounce) if side == 1 else (H[i] >= s_ext - (1 - VFX_PULL) * bounce))
            dry = m < VFX_DRY * s_ht
            flip = o_ > m
            lower = (L[i] < s_ext) if side == 1 else (H[i] > s_ext)
            if win[i]:
                fires = [(0, pulled and dry), (1, pulled and dry and flip), (2, pulled and dry and flip and mirror_n >= 3),
                         (4, lower and m < 0.7 * s_ht)]
                for k, ok in fires:
                    if ok and k not in done:
                        out[VFX_NAMES[k]][i] = side
                        done.add(k)
                        if trace is not None:
                            trace.append(dict(kind=VFX_NAMES[k], side=side, i=i, spike_start=s_i, spike_ext=s_ext, spike_ht=s_ht,
                                              bounce=bounce, bar_low=L[i], bar_high=H[i], mine=m, other=o_, atr=a[i]))
                if pulled and dry and flip and armed4 < 0 and 3 not in done:
                    armed4 = i
                if armed4 >= 0 and 3 not in done and i - armed4 <= 5 and ((C[i] > O[i]) if side == 1 else (C[i] < O[i])):
                    out[VFX_NAMES[3]][i] = side
                    done.add(3)
            # update the bounce AFTER using it (this candle's extreme counts from the next candle on)
            bounce = max(bounce, (H[i] - s_ext) if side == 1 else (s_ext - L[i]))
            # a lower low resets the reference low (the divergence above already used the old one)
            if lower:
                s_ext = L[i] if side == 1 else H[i]
                bounce = 0.0
    return out


VFX_DIV_WIN = int(os.getenv("VFX_DIV_WIN", "30"))   # the 2nd spike must start within this many candles of the 1st spike's end
DIV_NAMES = ["DIV-A early: lower low, fear bar 5+ shorter than the last spike",
             "DIV-B confirmed: 2nd spike = lower low + shorter tallest bar (5+)",
             "DIV-B15 confirmed, clearly smaller (15+)",
             "DIV-D double bottom: 2nd spike low within 0.5 ATR + shorter bar (5+)"]


def vfx_div_events(df, ind, trace=None):
    """Spike-vs-spike divergence on your VIX FIX pane, same day. Long = two FEAR spikes, short = two GREED spikes.
    A spike = a run of red (blue for greed) bars; its height = its tallest bar, its extreme = its lowest low (highest high).
    Everything is decided on the CLOSED candle i; entry at i+1's open."""
    fN, gN = vfx_pane(df)
    fear = np.asarray(ind["fear"], dtype=bool)
    greed = np.asarray(ind["greed"], dtype=bool) & ~fear
    hm, day, a = ind["hm"], ind["day"], ind["atr"]
    H, L = ind["h"], ind["l"]
    n = len(H)
    out = {nm: np.zeros(n, dtype=np.int64) for nm in DIV_NAMES}
    win = (hm >= 935) & (hm < 1530)
    rth = (hm >= 930) & (hm < 1600)
    for side in (1, -1):
        spk = fear if side == 1 else greed
        bar = np.nan_to_num(fN if side == 1 else gN)
        cur_day, prev, cur, fired_a = None, None, None, False
        for i in range(n):
            if not rth[i]:
                continue
            if day[i] != cur_day:                       # new day: forget everything
                cur_day, prev, cur, fired_a = day[i], None, None, False
            ext_i = L[i] if side == 1 else H[i]
            beyond = (lambda x, ref: x < ref) if side == 1 else (lambda x, ref: x > ref)
            if spk[i]:
                if cur is None:
                    cur = dict(start=i, end=i, ext=ext_i, ht=bar[i])
                else:
                    cur["end"], cur["ht"] = i, max(cur["ht"], bar[i])
                    cur["ext"] = min(cur["ext"], ext_i) if side == 1 else max(cur["ext"], ext_i)
            # DIV-A: first candle (red or gray) that goes beyond the last finished spike's extreme with a shorter bar
            if (prev is not None and not fired_a and i - prev["end"] <= VFX_DIV_WIN and win[i] and a[i] > 0
                    and beyond(ext_i, prev["ext"]) and bar[i] <= prev["ht"] - 5 and (cur is None or cur["ht"] <= prev["ht"] - 5)):
                out[DIV_NAMES[0]][i] = side
                fired_a = True
                if trace is not None:
                    trace.append(dict(kind=DIV_NAMES[0], side=side, i=i, p=dict(prev), c=None if cur is None else dict(cur)))
            if not spk[i] and cur is not None:          # the spike just ended (candle i is the first one after it)
                if prev is not None and cur["start"] - prev["end"] <= VFX_DIV_WIN and win[i] and a[i] > 0:
                    lower = beyond(cur["ext"], prev["ext"])
                    shorter = cur["ht"] <= prev["ht"] - 5
                    checks = [(1, lower and shorter), (2, lower and cur["ht"] <= prev["ht"] - 15),
                              (3, abs(cur["ext"] - prev["ext"]) <= 0.5 * a[i] and shorter)]
                    for k, ok in checks:
                        if ok:
                            out[DIV_NAMES[k]][i] = side
                            if trace is not None:
                                trace.append(dict(kind=DIV_NAMES[k], side=side, i=i, p=dict(prev), c=dict(cur)))
                prev, cur, fired_a = cur, None, False
    return out


# ---- NUMBERS ONLY (no red / blue): fear number F (0-100, top of your pane) and greed number G (0-100, bottom, shown as 0 to -100)
NUM_WIN = int(os.getenv("NUM_WIN", "30"))     # look back this many candles (same day) for the last peak
NUM_PEAK = float(os.getenv("NUM_PEAK", "70"))  # a "peak" = the highest number in that window, at least this high
NUM_NAMES = ["N1 divergence: new low / high, number 10+ below its last peak",
             "N2 divergence, 20+ below its last peak",
             "N3 N1 + the next candle turns your way (confirmed)",
             "N4 mirror (fear = greed) after a peak, then the other side takes over by 15+",
             "N5 N4 + price holds above the peak's low (below the peak's high for shorts)"]


def vfx_num_events(df, ind, trace=None):
    """Long side uses F at lows, short side uses G at highs. Candle i is CLOSED; entry is i+1's open.
    Peak = the highest F (G) in the previous NUM_WIN candles of the same day (not counting candle i), at least NUM_PEAK.
    Peak price = the lowest low (highest high) of the candles whose number is within 2 of that peak value."""
    fN, gN = vfx_pane(df)
    F, G = np.nan_to_num(fN), np.nan_to_num(gN)
    hm, day, a = ind["hm"], ind["day"], ind["atr"]
    O, H, L, C = ind["o"], ind["h"], ind["l"], ind["c"]
    n = len(H)
    out = {nm: np.zeros(n, dtype=np.int64) for nm in NUM_NAMES}
    rth = (hm >= 930) & (hm < 1600)
    win = (hm >= 935) & (hm < 1530)
    day_start = np.zeros(n, dtype=np.int64)
    for i in range(1, n):
        day_start[i] = day_start[i - 1] if day[i] == day[i - 1] else i
    for side in (1, -1):
        mine = F if side == 1 else G          # the number that peaks at lows (F) or highs (G)
        other = G if side == 1 else F
        ext = L if side == 1 else H
        last_fire = {k: -1 for k in range(5)}   # one fire per peak: a signal can only fire again after a NEW peak forms after its last fire
        pend3 = {}                            # N1 candle waiting for its confirmation candle
        for i in range(n):
            if not (rth[i] and win[i]) or not (a[i] > 0):
                continue
            # N3: the candle right after an N1 closes your way (checked before anything else on this candle)
            for jj, ii in list(pend3.items()):
                if i == ii + 1 and day[i] == day[ii]:
                    if ((C[i] > O[i]) if side == 1 else (C[i] < O[i])):
                        out[NUM_NAMES[2]][i] = side
                        last_fire[2] = i
                        if trace is not None:
                            trace.append(dict(kind=NUM_NAMES[2], side=side, i=i, j=jj, n1=ii))
                    del pend3[jj]
                elif i > ii + 1:
                    del pend3[jj]
            lo = max(day_start[i], i - NUM_WIN)
            while lo < i and not rth[lo]:
                lo += 1
            if i - lo < 3:
                continue
            w = mine[lo:i]
            pk = float(w.max())
            if pk < NUM_PEAK:
                continue
            near = np.nonzero(w >= pk - 2.0)[0] + lo
            j = int(near[0])                                       # the peak's id = its first candle
            if i - int(near[-1]) < 2:                              # the peak is still forming
                continue
            pk_px = ext[near].min() if side == 1 else ext[near].max()
            beyond = (L[i] < pk_px) if side == 1 else (H[i] > pk_px)
            # N1 / N2: price goes beyond the peak's price, the number is clearly lower than the peak
            for k, gap in ((0, 10.0), (1, 20.0)):
                if beyond and mine[i] <= pk - gap and int(near[-1]) > last_fire[k]:
                    out[NUM_NAMES[k]][i] = side
                    last_fire[k] = i
                    if k == 0:
                        pend3[j] = i
                    if trace is not None:
                        trace.append(dict(kind=NUM_NAMES[k], side=side, i=i, j=j, pk=pk, pk_px=pk_px, lo=lo))
            # N4 / N5: after the peak, a mirror (both numbers 25+ and within 15 of each other) for 3+ candles,
            # then the other side takes over by 15+ while this side is under half the peak
            seg_m, seg_o = mine[j:i], other[j:i]
            mirror_n = int(((seg_m >= 25) & (seg_o >= 25) & (np.abs(seg_m - seg_o) <= 15)).sum())
            takeover = other[i] - mine[i] >= 15 and mine[i] < 0.5 * pk
            if mirror_n >= 3 and takeover:
                holds = (L[i] >= pk_px) if side == 1 else (H[i] <= pk_px)
                for k, ok in ((3, True), (4, holds)):
                    if ok and int(near[-1]) > last_fire[k]:
                        out[NUM_NAMES[k]][i] = side
                        last_fire[k] = i
                        if trace is not None:
                            trace.append(dict(kind=NUM_NAMES[k], side=side, i=i, j=j, pk=pk, pk_px=pk_px, lo=lo, mirror_n=mirror_n))
    return out


def vfx_outcomes(ind, idx, side, holds, flat=1555, stop=3.0):
    """ATR result per entry (entry = next candle's open): close after N candles counting the entry candle (no stop,
    capped at the last candle before 15:55), close of that last candle, and the same with a 3 ATR stop (stop first)."""
    o, h, l, c, a, hm, day = ind["o"], ind["h"], ind["l"], ind["c"], ind["atr"], ind["hm"], ind["day"]
    n = len(o)
    ok_bar = hm < flat
    # last candle before the flat time for every day
    last_of = np.full(n, -1)
    cur = -1
    for j in range(n - 1, -1, -1):
        if j == n - 1 or day[j + 1] != day[j]:
            cur = -1
        if ok_bar[j] and cur == -1:
            cur = j
        last_of[j] = cur
    res = np.full((len(idx), len(holds) + 2), np.nan)
    for q, (i, sd) in enumerate(zip(idx, side)):
        e = i + 1
        if e >= n or day[e] != day[i] or not ok_bar[e] or not (a[i] > 0):
            continue
        last = last_of[e]
        en, at = o[e], a[i]
        for k, hb in enumerate(holds):
            res[q, k] = sd * (c[min(e + hb - 1, last)] - en) / at
        res[q, len(holds)] = sd * (c[last] - en) / at
        stp = en - sd * stop * at
        seg = l[e:last + 1] <= stp if sd == 1 else h[e:last + 1] >= stp
        hit = np.nonzero(seg)[0]
        if len(hit):
            j = e + hit[0]
            px = min(o[j], stp) if sd == 1 else max(o[j], stp)
            res[q, len(holds) + 1] = sd * (px - en) / at
        else:
            res[q, len(holds) + 1] = res[q, len(holds)]
    return res


def vfx_main():
    end = datetime.now(timezone.utc) - timedelta(days=1)
    start = datetime.fromisoformat(START).replace(tzinfo=timezone.utc)
    test = os.getenv("TEST", "") == "1"
    os.makedirs(OUT, exist_ok=True)
    split = pd.Timestamp(SPLIT, tz=NY)
    t0 = time.time()
    HOLDS = [5, 10, 15, 30, 60]
    HN = [f"{x} candles" for x in HOLDS] + ["to 15:55", "to 15:55, 3 ATR stop"]
    rng = np.random.default_rng(3)
    rows, base = [], []
    n_years = max((end - start).days / 365.25, 1e-9)
    for sym in SYMBOLS:
        print(f"\n=== {sym} ===", flush=True)
        df1, feed = fake_1m(sym, start, end) if test else fetch_1m(sym, start, end)
        for tf in ST_TFS:
            df = to_tf(df1, rth_only=False, mins=tf)
            ind, color, mom, sup = super_events(df, 2, "dip")
            ev = vfx_num_events(df, ind)
            ev["VF2 (old, color-based) retest + greed taller than fear"] = vfx_events(df, ind)[VFX_NAMES[1]]
            c, hh_, ll_ = df["close"], df["high"], df["low"]
            lo14, hi14 = ll_.rolling(14).min(), hh_.rolling(14).max()
            K = (100 * (c - lo14) / (hi14 - lo14).replace(0, np.nan)).rolling(3).mean().to_numpy()
            kw = np.where(sup > 0, K, 100 - K)
            ev["SUPER (dip)"] = sup
            ev["SUPER+ (Stoch 20-40 your way)"] = np.where((sup != 0) & (kw >= 20) & (kw <= 40), sup, 0)
            ev["GAP & GO (confirmed)"] = gap_events(df, df1, ind, 0.3, 935, True)
            years = np.asarray(df.index.year)
            for nm, sg in ev.items():
                idx = np.nonzero(sg)[0]
                if not len(idx):
                    continue
                sd = sg[idx]
                g = grade_two_sided(ind, idx)
                R = vfx_outcomes(ind, idx, sd, HOLDS)
                d = pd.DataFrame(R, columns=HN)
                d["edge"] = 50.0 * (np.where(sd > 0, g[:, 0], g[:, 1]) - np.where(sd > 0, g[:, 1], g[:, 0]))
                d["kind"], d["sym"], d["tf"] = nm, sym, tf
                d["side"] = np.where(sd > 0, "LONG", "SHORT")
                d["per"] = np.where(df.index[idx] < split, "tr", "te")
                d["year"] = years[idx]
                rows.append(d.dropna(subset=[HN[0]]))
            hm = ind["hm"]
            pool = np.nonzero((hm >= 935) & (hm < 1530))[0]
            ridx = np.sort(rng.choice(pool, size=min(len(pool), int(os.getenv("VFX_RANDOM", "8000"))), replace=False))
            for sdv, snm in ((1, "LONG"), (-1, "SHORT")):
                R = vfx_outcomes(ind, ridx, np.full(len(ridx), sdv), HOLDS)
                d = pd.DataFrame(R, columns=HN)
                d["sym"], d["tf"], d["side"] = sym, tf, snm
                d["per"] = np.where(df.index[ridx] < split, "tr", "te")
                d["year"] = years[ridx]
                base.append(d.dropna(subset=[HN[0]]))
            print(f"  {sym} {tf}m done ({time.time() - t0:.0f}s) | " +
                  " | ".join(f"{k_.split(' ')[0]} {int((v != 0).sum())}" for k_, v in ev.items()), flush=True)
        del df1
    E = pd.concat(rows, ignore_index=True)
    B = pd.concat(base, ignore_index=True)
    bm_per = B.groupby(["sym", "tf", "side", "per"])[HN].mean()
    bm_yr = B.groupby(["sym", "tf", "side", "year"])[HN].mean()
    pn = {"tr": f"{START[:4]}-{int(SPLIT[:4]) - 1}", "te": f"{SPLIT[:4]}-now"}
    kinds = list(dict.fromkeys(E["kind"]))
    yrs = sorted(int(y) for y in E["year"].unique())

    def adj(g, col, by="per"):
        """Average ATR minus a random entry in the SAME direction on the same chart and the same period (or year)."""
        if not len(g):
            return np.nan
        bm = bm_per if by == "per" else bm_yr
        keys = ["sym", "tf", "side", by]
        tot, nn = 0.0, 0
        for kk, gg in g.groupby(keys):
            if kk not in bm.index:
                continue
            b = bm.loc[kk, col]
            if np.isnan(b):
                continue
            tot += (gg[col].mean() - b) * len(gg)
            nn += len(gg)
        return tot / nn if nn else np.nan

    summ = []
    for k_ in kinds:
        g = E[E["kind"] == k_]
        tr, te = g[g["per"] == "tr"], g[g["per"] == "te"]
        best = max(HN, key=lambda col: np.nan_to_num(adj(tr, col), nan=-9.0))     # hold picked on TRAIN only
        ych = [adj(g[g["year"] == y_], best, by="year") for y_ in yrs]
        charts_pos = sum(1 for _, gg in te.groupby(["sym", "tf"]) if adj(gg, best) > 0)
        nch = te.groupby(["sym", "tf"]).ngroups
        summ.append(dict(k=k_, n=len(g), per_yr=len(g) / n_years / max(len(SYMBOLS) * len(ST_TFS), 1),
                         etr=tr["edge"].mean(), ete=te["edge"].mean(), best=best, atr_te=te[best].mean(),
                         adj_tr=adj(tr, best), adj_te=adj(te, best), charts=charts_pos, nch=nch, ych=ych,
                         ypos=sum(1 for v in ych if v > 0), ny=sum(1 for v in ych if not np.isnan(v))))
    summ.sort(key=lambda z: -(np.nan_to_num(z["adj_te"]) + np.nan_to_num(z["adj_tr"])))

    def real(z):
        return (z["adj_tr"] > 0.05 and z["adj_te"] > 0.05 and z["etr"] > 1.0 and z["ete"] > 1.0 and z["charts"] >= 6
                and z["ypos"] >= max(z["ny"] - 1, 1))
    good = [z for z in summ if real(z)]
    md = [f"# VIX FIX RETEST + LEADERBOARD - {datetime.now(NY):%Y-%m-%d %H:%M} ET",
          f"Data {START} to {end:%Y-%m-%d}, {', '.join(SYMBOLS)}, {', '.join(f'{t}m' for t in ST_TFS)}. DATA ONLY - ATR only (you manage the options). "
          f"Retest = after a spike, price bounces {VFX_BOUNCE:g}+ ATR, then gives back {VFX_PULL:.0%}+ of the bounce within {VFX_WIN} candles (same day); "
          f"dried up = fear bar under {VFX_DRY:.0%} of the spike's tallest bar. Entry = next open, signals 9:35-15:30. Runtime {(time.time() - t0) / 60:.0f} min.",
          "**Edge** = +1-ATR-your-way-first minus the other way, halved (0 = coin flip). **ATR** = average move your way. "
          "**vs random** = minus a random entry in the SAME direction on the same chart and period (removes the market's drift) - the fair score. "
          "**Best hold** is picked on 2020-23 only, then checked on 2024-now and every year. **Charts +** = charts (of 8) that beat random in 2024-now. "
          "**Years +** = years that beat random. **REAL EDGE** = beats random by 0.05+ ATR in both periods, edge above +1 in both, 6+ charts, "
          "and every year but one.", "",
          "## The answer in 30 seconds",
          f"- **Setups with a REAL EDGE: {len(good)}** - " + ("; ".join(
              f"{z['k']}: {z['adj_te']:+.2f} ATR vs random (2024-now) holding {z['best']}, {z['charts']}/{z['nch']} charts, {z['ypos']}/{z['ny']} years"
              for z in good) if good else "none passed every check."), "",
          "## The leaderboard (sorted by the 2020-23 + 2024-now score vs random)",
          "| Setup | Signals | Per chart per year | Edge " + pn["tr"] + " | Edge " + pn["te"] + " | Best hold (picked on " + pn["tr"] + ") | ATR " + pn["te"] +
          " | vs random " + pn["tr"] + " | **vs random " + pn["te"] + "** | Charts + | Years + | |",
          "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for z in summ:
        md.append(f"| {z['k']} | {z['n']} | {z['per_yr']:.0f} | {z['etr']:+.1f} | {z['ete']:+.1f} | {z['best']} | {z['atr_te']:+.2f} | "
                  f"{z['adj_tr']:+.2f} | **{z['adj_te']:+.2f}** | {z['charts']}/{z['nch']} | {z['ypos']}/{z['ny']} | {'✅ REAL EDGE' if real(z) else ''} |")
    md += ["", "## Every year (vs random, ATR per trade, at each setup's best hold)",
           "| Setup | " + " | ".join(str(y_) for y_ in yrs) + " |", "|---|" + "---|" * len(yrs)]
    for z in summ:
        md.append(f"| {z['k']} | " + " | ".join("-" if np.isnan(v) else f"{v:+.2f}" for v in z["ych"]) + " |")
    md += ["", f"## Every hold time ({pn['te']}, vs random, ATR)", "| Setup | " + " | ".join(HN) + " |", "|---|" + "---|" * len(HN)]
    for z in summ:
        te = E[(E["kind"] == z["k"]) & (E["per"] == "te")]
        md.append(f"| {z['k']} | " + " | ".join(f"{adj(te, col):+.2f}" for col in HN) + " |")
    md += ["", f"## Longs vs shorts ({pn['te']}, best hold, vs random)", "| Setup | Longs | ATR vs random | Shorts | ATR vs random |", "|---|---|---|---|---|"]
    for z in summ:
        te = E[(E["kind"] == z["k"]) & (E["per"] == "te")]
        lg, sh = te[te["side"] == "LONG"], te[te["side"] == "SHORT"]
        md.append(f"| {z['k']} | {len(lg)} | {adj(lg, z['best']):+.2f} | {len(sh)} | {adj(sh, z['best']):+.2f} |")
    md += ["", f"## Every chart ({pn['te']}, best hold, vs random | signals)", "| Setup | " + " | ".join(f"{s_} {t_}m" for s_ in SYMBOLS for t_ in ST_TFS) + " |",
           "|---|" + "---|" * (len(SYMBOLS) * len(ST_TFS))]
    for z in summ:
        cells = []
        for s_ in SYMBOLS:
            for t_ in ST_TFS:
                gg = E[(E["kind"] == z["k"]) & (E["per"] == "te") & (E["sym"] == s_) & (E["tf"] == t_)]
                cells.append(f"{adj(gg, z['best']):+.2f} ({len(gg)})" if len(gg) else "-")
        md.append(f"| {z['k']} | " + " | ".join(cells) + " |")
    text = "\n".join(md + [""])
    print("\n" + text)
    stamp = datetime.now(NY).strftime("%Y-%m-%d")
    for path in (f"{OUT}/vfx_{stamp}.md", f"{OUT}/vfx_latest.md"):
        with open(path, "w") as f:
            f.write(text + "\n")
    sm = os.getenv("GITHUB_STEP_SUMMARY")
    if sm:
        with open(sm, "a") as f:
            f.write(text + "\n")


# ================================================================ VF CROSS v2 FIRES, 10 MINUTES LATER (MODE=vfc)
VFC_NAMES = ["HARD LONG", "HARD SHORT", "TURN LONG", "TURN SHORT", "MAX LONG (greed maxed)", "MAX SHORT (fear maxed)",
             "CROSS LONG (after a greed lead)", "CROSS SHORT (after a fear lead)"]


def vfc_events(df, ind, hard=15.0, turn_lvl=8.0, turn_min=2.0, turn_cd=5, max_gap=80.0, re_arm=40.0, big=50.0, meet=5.0,
               look=30, trace=None):
    """Exactly the VF CROSS v2 rules (inverted defaults) on CLOSED candles. Returns {name: +1/-1 array}."""
    fN, gN = vfx_pane(df)
    F, G = np.nan_to_num(fN), np.nan_to_num(gN)
    d = F - G
    hm = ind["hm"]
    n = len(d)
    sess = (hm >= 930) & (hm < 1600)
    out = {nm: np.zeros(n, dtype=np.int64) for nm in VFC_NAMES}
    last_tl, last_ts, last_cf, last_cg = -1000, -1000, -1, -1
    arm_f, arm_g = True, True
    for i in range(1, n):
        # CROSS arming over the last `look` candles incl. this one (Pine ta.highest / ta.highestbars)
        lo = max(0, i - look + 1)
        w = d[lo:i + 1]
        fl = w.max()
        gl = -w.min()
        flb = lo + int(np.nonzero(w == fl)[0][-1])          # most recent candle with the max (Pine returns the latest)
        glb = lo + int(np.nonzero(w == -gl)[0][-1])
        armF = fl >= big and flb >= glb
        armG = gl >= big and glb > flb
        if d[i] < re_arm:
            arm_f = True
        if -d[i] < re_arm:
            arm_g = True
        if not sess[i]:
            continue
        sw = d[i] - d[i - 1]
        fire = []
        if d[i - 1] >= 0 and d[i] < 0 and sw <= -hard:
            fire.append(0)
        if d[i - 1] <= 0 and d[i] > 0 and sw >= hard:
            fire.append(1)
        if G[i - 1] < turn_lvl and G[i] >= G[i - 1] + turn_min and F[i] < F[i - 1] and i - last_tl >= turn_cd:
            fire.append(2)
            last_tl = i
        if F[i - 1] < turn_lvl and F[i] >= F[i - 1] + turn_min and G[i] < G[i - 1] and i - last_ts >= turn_cd:
            fire.append(3)
            last_ts = i
        if arm_f and d[i] >= max_gap:
            fire.append(5)
            arm_f = False
        if arm_g and -d[i] >= max_gap:
            fire.append(4)
            arm_g = False
        if armF and d[i] <= meet and flb > last_cf and flb < i:
            fire.append(7)
            last_cf = flb
        if armG and d[i] >= -meet and glb > last_cg and glb < i:
            fire.append(6)
            last_cg = glb
        for k in fire:
            out[VFC_NAMES[k]][i] = 1 if k % 2 == 0 else -1
            if trace is not None:
                trace.append((VFC_NAMES[k], i))
    return out


def vfc_main():
    end = datetime.now(timezone.utc) - timedelta(days=1)
    start = datetime.fromisoformat(os.getenv("VFC_START", "2020-01-01")).replace(tzinfo=timezone.utc)
    test = os.getenv("TEST", "") == "1"
    os.makedirs(OUT, exist_ok=True)
    split = pd.Timestamp(SPLIT, tz=NY)
    t0 = time.time()
    MINS = [5, 10, 20]
    HN = [f"{m} min" for m in MINS]
    rng = np.random.default_rng(4)
    rows, base = [], []
    for sym in SYMBOLS:
        print(f"\n=== {sym} ===", flush=True)
        df1, feed = fake_1m(sym, start, end) if test else fetch_1m(sym, start, end)
        for tf in ST_TFS:
            df = to_tf(df1, rth_only=False, mins=tf)
            ind = indicators(df, 13, 34, True)
            holds = [max(1, int(round(m / tf))) for m in MINS]
            ev = vfc_events(df, ind)
            years = np.asarray(df.index.year)
            for nm, sg in ev.items():
                for flip, tag in ((1, ""), (-1, " -> FLIPPED")):
                    idx = np.nonzero(sg)[0]
                    if not len(idx):
                        continue
                    sd = sg[idx] * flip
                    R = vfx_outcomes(ind, idx, sd, holds)[:, :len(holds)]
                    d_ = pd.DataFrame(R, columns=HN)
                    d_["kind"], d_["sym"], d_["tf"] = nm + tag, sym, tf
                    d_["side"] = np.where(sd > 0, "LONG", "SHORT")
                    d_["per"] = np.where(df.index[idx] < split, "tr", "te")
                    d_["year"] = years[idx]
                    rows.append(d_.dropna(subset=[HN[0]]))
            hm = ind["hm"]
            pool = np.nonzero((hm >= 930) & (hm < 1555))[0]
            ridx = np.sort(rng.choice(pool, size=min(len(pool), int(os.getenv("VFC_RANDOM", "10000"))), replace=False))
            for sdv, snm in ((1, "LONG"), (-1, "SHORT")):
                R = vfx_outcomes(ind, ridx, np.full(len(ridx), sdv), holds)[:, :len(holds)]
                d_ = pd.DataFrame(R, columns=HN)
                d_["sym"], d_["tf"], d_["side"] = sym, tf, snm
                d_["per"] = np.where(df.index[ridx] < split, "tr", "te")
                d_["year"] = years[ridx]
                base.append(d_.dropna(subset=[HN[0]]))
            print(f"  {sym} {tf}m done ({time.time() - t0:.0f}s) | holds {holds} candles | " +
                  " | ".join(f"{k_.split(' (')[0]} {int((v != 0).sum())}" for k_, v in ev.items()), flush=True)
        del df1
    E = pd.concat(rows, ignore_index=True)
    B = pd.concat(base, ignore_index=True)
    bm_per = B.groupby(["sym", "tf", "side", "per"])[HN].mean()
    bm_yr = B.groupby(["sym", "tf", "side", "year"])[HN].mean()
    pn = {"tr": f"{start:%Y}-{int(SPLIT[:4]) - 1}", "te": f"{SPLIT[:4]}-now"}
    yrs = sorted(int(y) for y in E["year"].unique())

    def adj(g, col, by="per"):
        if not len(g):
            return np.nan
        bm = bm_per if by == "per" else bm_yr
        tot, nn = 0.0, 0
        for kk, gg in g.groupby(["sym", "tf", "side", by]):
            if kk in bm.index and not np.isnan(bm.loc[kk, col]):
                tot += (gg[col].mean() - bm.loc[kk, col]) * len(gg)
                nn += len(gg)
        return tot / nn if nn else np.nan

    col = "10 min"
    summ = []
    for k_ in dict.fromkeys(E["kind"]):
        g = E[E["kind"] == k_]
        tr, te = g[g["per"] == "tr"], g[g["per"] == "te"]
        ych = [adj(g[g["year"] == y_], col, by="year") for y_ in yrs]
        cpos = sum(1 for _, gg in te.groupby(["sym", "tf"]) if adj(gg, col) > 0)
        summ.append(dict(k=k_, n=len(g), win=100 * (g[col] > 0).mean(), atr=g[col].mean(), tr=adj(tr, col), te=adj(te, col),
                         charts=cpos, nch=te.groupby(["sym", "tf"]).ngroups, ych=ych, ypos=sum(1 for v in ych if v > 0),
                         ny=sum(1 for v in ych if not np.isnan(v))))
    summ.sort(key=lambda z: -(np.nan_to_num(z["tr"]) + np.nan_to_num(z["te"])))

    def real(z):
        return z["tr"] > 0.03 and z["te"] > 0.03 and z["charts"] >= 6 and z["ypos"] >= max(z["ny"] - 1, 1) and z["n"] >= 300
    good = [z for z in summ if real(z)]
    md = [f"# VF CROSS v2 FIRES - WHICH HAS THE BEST EDGE AFTER 10 MINUTES - {datetime.now(NY):%Y-%m-%d %H:%M} ET",
          f"Data {start:%Y-%m-%d} to {end:%Y-%m-%d}, {', '.join(SYMBOLS)}, {', '.join(f'{t}m' for t in ST_TFS)}. DATA ONLY. Runtime {(time.time() - t0) / 60:.0f} min.",
          "Exact VF CROSS v2 rules (HARD 15, TURN under 8 / +2, MAX 80 re-arm 40, CROSS 50 lead / within 5 / 30 candles, 9:30-16:00). "
          "**Backtest = the candle's CLOSE**, entry at the next open (live the indicator fires on the first tick - could be better or worse). "
          "**10 min** = 10 candles on 1m, 5 on 2m, 3 on 3m (9 min), 2 on 5m. **ATR** = average move your way. **vs random** = minus a random entry "
          "in the SAME direction on the same chart and period - the fair score. **-> FLIPPED** = the same fire traded the other way. "
          f"**REAL EDGE** = beats random by 0.03+ ATR in {pn['tr']} AND {pn['te']}, on 6+ of 8 charts, every year but one, 300+ fires.", "",
          "## The answer in 30 seconds",
          f"- **Fires with a REAL EDGE at 10 minutes: {len(good)}**" + (" - " + "; ".join(
              f"{z['k']}: {z['te']:+.3f} ATR vs random ({pn['te']}), {z['win']:.0f}% green, {z['charts']}/{z['nch']} charts, {z['ypos']}/{z['ny']} years"
              for z in good) if good else " - none passed every check."),
          f"- **Best overall** (both periods together): {summ[0]['k']} ({summ[0]['tr']:+.3f} / {summ[0]['te']:+.3f} ATR vs random)", "",
          "## Every fire at 10 minutes (sorted by both periods vs random)",
          f"| Fire | Fires | Green after 10 min | Avg ATR | vs random {pn['tr']} | **vs random {pn['te']}** | Charts + | Years + | |",
          "|---|---|---|---|---|---|---|---|---|"]
    for z in summ:
        md.append(f"| {z['k']} | {z['n']} | {z['win']:.0f}% | {z['atr']:+.3f} | {z['tr']:+.3f} | **{z['te']:+.3f}** | {z['charts']}/{z['nch']} | "
                  f"{z['ypos']}/{z['ny']} | {'✅ REAL EDGE' if real(z) else ''} |")
    md += ["", "## Every year (vs random, ATR at 10 min)", "| Fire | " + " | ".join(str(y_) for y_ in yrs) + " |", "|---|" + "---|" * len(yrs)]
    for z in summ:
        md.append(f"| {z['k']} | " + " | ".join("-" if np.isnan(v) else f"{v:+.3f}" for v in z["ych"]) + " |")
    md += ["", f"## 5 / 10 / 20 minutes ({pn['te']}, vs random)", "| Fire | " + " | ".join(HN) + " |", "|---|" + "---|" * len(HN)]
    for z in summ:
        te = E[(E["kind"] == z["k"]) & (E["per"] == "te")]
        md.append(f"| {z['k']} | " + " | ".join(f"{adj(te, c_):+.3f}" for c_ in HN) + " |")
    md += ["", f"## Every chart at 10 min ({pn['te']}, vs random | fires)", "| Fire | " + " | ".join(f"{s_} {t_}m" for s_ in SYMBOLS for t_ in ST_TFS) + " |",
           "|---|" + "---|" * (len(SYMBOLS) * len(ST_TFS))]
    for z in summ:
        cells = []
        for s_ in SYMBOLS:
            for t_ in ST_TFS:
                gg = E[(E["kind"] == z["k"]) & (E["per"] == "te") & (E["sym"] == s_) & (E["tf"] == t_)]
                cells.append(f"{adj(gg, col):+.3f} ({len(gg)})" if len(gg) else "-")
        md.append(f"| {z['k']} | " + " | ".join(cells) + " |")
    text = "\n".join(md + [""])
    print("\n" + text)
    stamp = datetime.now(NY).strftime("%Y-%m-%d")
    for path in (f"{OUT}/vfc_{stamp}.md", f"{OUT}/vfc_latest.md"):
        with open(path, "w") as f:
            f.write(text + "\n")
    sm = os.getenv("GITHUB_STEP_SUMMARY")
    if sm:
        with open(sm, "a") as f:
            f.write(text + "\n")


# ================================================================ VF SCALPER: +$0.50 IN 20 MINUTES (MODE=vfs)
VFS_NAMES = ["FEAR MAX L", "GREED MAX S", "FEAR TURN L", "GREED TURN S", "GREED CROSS L", "FEAR CROSS S",
             "HARD L", "HARD S", "DIV L", "DIV S", "FLIP L", "FLIP S"]


def vfs_events(df, ind, sess_end=1540, look=30, trace=None):
    """Exactly the VF Scalper Pine rules on CLOSED candles. Returns (signals k -> +1/-1 array, trend state array)."""
    fN, gN = vfx_pane(df)
    F, G = np.nan_to_num(fN), np.nan_to_num(gN)
    d = F - G
    H, L, C = ind["h"], ind["l"], ind["c"]
    hm, day = ind["hm"], ind["day"]
    n = len(d)
    ef = df["close"].ewm(span=13, adjust=False).mean().to_numpy()
    es = df["close"].ewm(span=34, adjust=False).mean().to_numpy()
    vw = ind["vwap"]
    st = np.where((ef > es) & (C > vw), 1, np.where((ef < es) & (C < vw), -1, 0))
    rth = (hm >= 930) & (hm < 1600)
    sess = (hm >= 930) & (hm < sess_end)
    out = {nm: np.zeros(n, dtype=np.int64) for nm in VFS_NAMES}
    arm_ml, arm_ms = True, True
    last_tl = last_ts = -1000
    last_cf = last_cg = -1
    lf = {"DL": -1, "DS": -1, "FL": -1, "FS": -1}

    def scan(src, px, is_low, i):
        cnt, pk = 0, 0.0
        for k in range(1, look + 1):
            j = i - k
            if j < 0 or day[j] != day[i] or not rth[j]:
                break
            cnt += 1
            pk = max(pk, src[j])
        pk_px, last_near, first_near = np.nan, -1, -1
        if cnt >= 3 and pk >= 70:
            for k in range(1, cnt + 1):
                j = i - k
                if src[j] >= pk - 2:
                    pk_px = px[j] if np.isnan(pk_px) else (min(pk_px, px[j]) if is_low else max(pk_px, px[j]))
                    if last_near < 0:
                        last_near = k
                    first_near = k
        return pk, cnt, pk_px, last_near, first_near

    def mirror(x, y, from_k, i):
        return sum(1 for k in range(1, from_k + 1) if x[i - k] >= 25 and y[i - k] >= 25 and abs(x[i - k] - y[i - k]) <= 15)

    for i in range(1, n):
        lo = max(0, i - look + 1)
        w = d[lo:i + 1]
        fl, gl = w.max(), -w.min()
        flb = lo + int(np.nonzero(w == fl)[0][-1])
        glb = lo + int(np.nonzero(w == -gl)[0][-1])
        armF = fl >= 50 and flb >= glb
        armG = gl >= 50 and glb > flb
        sw = d[i] - d[i - 1]
        c = {}
        c[0] = arm_ml and d[i] >= 80
        c[1] = arm_ms and -d[i] >= 80
        c[2] = F[i - 1] < 8 and F[i] >= F[i - 1] + 2 and G[i] < G[i - 1] and i - last_tl >= 5
        c[3] = G[i - 1] < 8 and G[i] >= G[i - 1] + 2 and F[i] < F[i - 1] and i - last_ts >= 5
        c[4] = armG and d[i] >= -5 and glb > last_cg and glb < i
        c[5] = armF and d[i] <= 5 and flb > last_cf and flb < i
        c[6] = d[i - 1] >= 0 and d[i] < 0 and sw <= -15
        c[7] = d[i - 1] <= 0 and d[i] > 0 and sw >= 15
        c[8] = c[9] = c[10] = c[11] = False
        if rth[i]:
            pkF, cntF, pxF, lnF, fnF = scan(F, L, True, i)
            pkG, cntG, pxG, lnG, fnG = scan(G, H, False, i)
            okPL = cntF >= 3 and pkF >= 70 and lnF >= 2
            okPS = cntG >= 3 and pkG >= 70 and lnG >= 2
            if okPL:
                c[8] = L[i] < pxF and F[i] <= pkF - 10 and i - lnF > lf["DL"]
                c[10] = mirror(F, G, fnF, i) >= 3 and G[i] - F[i] >= 15 and F[i] < 0.5 * pkF and L[i] >= pxF and i - lnF > lf["FL"]
            if okPS:
                c[9] = H[i] > pxG and G[i] <= pkG - 10 and i - lnG > lf["DS"]
                c[11] = mirror(G, F, fnG, i) >= 3 and F[i] - G[i] >= 15 and G[i] < 0.5 * pkG and H[i] <= pxG and i - lnG > lf["FS"]
        if sess[i]:
            for k in range(12):
                if c[k]:
                    out[VFS_NAMES[k]][i] = 1 if k % 2 == 0 else -1
                    if trace is not None:
                        trace.append((VFS_NAMES[k], i))
        # state updates on the closed candle (same order as the Pine script)
        if d[i] < 40:
            arm_ml = True
        if -d[i] < 40:
            arm_ms = True
        if c[0] and sess[i]:
            arm_ml = False
        if c[1] and sess[i]:
            arm_ms = False
        if c[2] and sess[i]:
            last_tl = i
        if c[3] and sess[i]:
            last_ts = i
        if c[5] and sess[i]:
            last_cf = flb
        if c[4] and sess[i]:
            last_cg = glb
        if c[8]:
            lf["DL"] = i
        if c[9]:
            lf["DS"] = i
        if c[10]:
            lf["FL"] = i
        if c[11]:
            lf["FS"] = i
    return out, st


def vfs_outcomes(ind, idx, side, ncand, tgt=0.5, stops=(0.0, 0.25, 0.5, 1.0)):
    """$ per share for each stop (0 = no stop): +tgt if the target is hit first, -stop if the stop is hit first (checked first
    on the same candle), else the close when the time limit (ncand candles) or 15:55 is reached. Entry = next open.
    Also returns whether the target was hit (no-stop version)."""
    o, h, l, c, hm, day = ind["o"], ind["h"], ind["l"], ind["c"], ind["hm"], ind["day"]
    n = len(o)
    res = np.full((len(idx), len(stops)), np.nan)
    hit = np.full(len(idx), np.nan)
    for q, (i, sd) in enumerate(zip(idx, side)):
        e = i + 1
        if e >= n or day[e] != day[i] or hm[e] >= 1555:
            continue
        en = o[e]
        for s_i, stp in enumerate(stops):
            r = np.nan
            j = e
            while True:
                fav = (h[j] - en) if sd == 1 else (en - l[j])
                adv = (en - l[j]) if sd == 1 else (h[j] - en)
                if stp > 0 and adv >= stp:
                    px = min(o[j], en - stp) if sd == 1 else max(o[j], en + stp)
                    r = sd * (px - en)
                    break
                if fav >= tgt:
                    r = tgt
                    if stp == 0:
                        hit[q] = 1.0
                    break
                if j - i >= ncand or hm[j] >= 1555 or j + 1 >= n or day[j + 1] != day[j]:
                    r = sd * (c[j] - en)
                    if stp == 0:
                        hit[q] = 0.0
                    break
                j += 1
            res[q, s_i] = r
    return res, hit


def vfs_main():
    end = datetime.now(timezone.utc) - timedelta(days=1)
    start = datetime.fromisoformat(os.getenv("VFS_START", "2020-01-01")).replace(tzinfo=timezone.utc)
    test = os.getenv("TEST", "") == "1"
    os.makedirs(OUT, exist_ok=True)
    split = pd.Timestamp(SPLIT, tz=NY)
    t0 = time.time()
    TGT = float(os.getenv("VFS_TGT", "0.5"))
    MINS = int(os.getenv("VFS_MINS", "20"))
    STOPS = (0.0, 0.25, 0.5, 1.0)
    SN = ["no stop", "$0.25 stop", "$0.50 stop", "$1.00 stop"]
    rng = np.random.default_rng(6)
    rows, base = [], []
    for sym in SYMBOLS:
        print(f"\n=== {sym} ===", flush=True)
        df1, feed = fake_1m(sym, start, end) if test else fetch_1m(sym, start, end)
        for tf in ST_TFS:
            df = to_tf(df1, rth_only=False, mins=tf)
            ind = indicators(df, 13, 34, True)
            nC = max(1, int(round(MINS / tf)))
            ev, st = vfs_events(df, ind)
            years = np.asarray(df.index.year)
            for nm, sg in ev.items():
                idx = np.nonzero(sg)[0]
                if not len(idx):
                    continue
                sd = sg[idx]
                R, hit = vfs_outcomes(ind, idx, sd, nC, TGT, STOPS)
                d_ = pd.DataFrame(R, columns=SN)
                d_["hit"] = hit
                d_["kind"], d_["sym"], d_["tf"] = nm, sym, tf
                d_["side"] = np.where(sd > 0, "LONG", "SHORT")
                tr_ = st[idx] * sd
                d_["trend"] = np.where(tr_ > 0, "with", np.where(tr_ < 0, "against", "gray"))
                d_["per"] = np.where(df.index[idx] < split, "tr", "te")
                d_["year"] = years[idx]
                rows.append(d_.dropna(subset=[SN[0]]))
            hm = ind["hm"]
            pool = np.nonzero((hm >= 930) & (hm < 1540))[0]
            ridx = np.sort(rng.choice(pool, size=min(len(pool), int(os.getenv("VFS_RANDOM", "8000"))), replace=False))
            for sdv, snm in ((1, "LONG"), (-1, "SHORT")):
                R, hit = vfs_outcomes(ind, ridx, np.full(len(ridx), sdv), nC, TGT, STOPS)
                d_ = pd.DataFrame(R, columns=SN)
                d_["hit"] = hit
                d_["sym"], d_["tf"], d_["side"] = sym, tf, snm
                d_["per"] = np.where(df.index[ridx] < split, "tr", "te")
                d_["year"] = years[ridx]
                base.append(d_.dropna(subset=[SN[0]]))
            print(f"  {sym} {tf}m done ({time.time() - t0:.0f}s) | 20 min = {nC} candles | " +
                  " | ".join(f"{k_} {int((v != 0).sum())}" for k_, v in ev.items()), flush=True)
        del df1
    E = pd.concat(rows, ignore_index=True)
    B = pd.concat(base, ignore_index=True)
    cols = SN + ["hit"]
    bm_per = B.groupby(["sym", "tf", "side", "per"])[cols].mean()
    bm_yr = B.groupby(["sym", "tf", "side", "year"])[cols].mean()
    pn = {"tr": f"{start:%Y}-{int(SPLIT[:4]) - 1}", "te": f"{SPLIT[:4]}-now"}
    yrs = sorted(int(y) for y in E["year"].unique())

    def adj(g, col, by="per"):
        if not len(g):
            return np.nan
        bm = bm_per if by == "per" else bm_yr
        tot, nn = 0.0, 0
        for kk, gg in g.groupby(["sym", "tf", "side", by]):
            if kk in bm.index and not np.isnan(bm.loc[kk, col]):
                tot += (gg[col].mean() - bm.loc[kk, col]) * len(gg)
                nn += len(gg)
        return tot / nn if nn else np.nan

    def rnd(g, col):
        """the random baseline matched to this group's charts, sides and periods"""
        tot, nn = 0.0, 0
        for kk, gg in g.groupby(["sym", "tf", "side", "per"]):
            if kk in bm_per.index:
                tot += bm_per.loc[kk, col] * len(gg)
                nn += len(gg)
        return tot / nn if nn else np.nan

    FILTERS = [("Off", None), ("With the trend line", "with"), ("Against the trend line", "against")]
    summ = []
    for k_ in VFS_NAMES:
        for fnm, fv in FILTERS:
            g = E[(E["kind"] == k_) & ((E["trend"] == fv) if fv else True)]
            if len(g) < 50:
                continue
            for s_ in SN:
                tr, te = g[g["per"] == "tr"], g[g["per"] == "te"]
                ych = [adj(g[g["year"] == y_], s_, by="year") for y_ in yrs]
                summ.append(dict(k=k_, f=fnm, s=s_, n=len(g), hit=100 * g["hit"].mean(), rhit=100 * rnd(g, "hit"),
                                 usd=g[s_].mean(), tr=adj(tr, s_), te=adj(te, s_),
                                 charts=sum(1 for _, gg in te.groupby(["sym", "tf"]) if adj(gg, s_) > 0),
                                 nch=te.groupby(["sym", "tf"]).ngroups, ych=ych, ypos=sum(1 for v in ych if v > 0),
                                 ny=sum(1 for v in ych if not np.isnan(v))))
    S = pd.DataFrame(summ)
    S["score"] = S["tr"].fillna(-9) + S["te"].fillna(-9)

    def real(z):
        return z["tr"] > 0.01 and z["te"] > 0.01 and z["charts"] >= 6 and z["ypos"] >= max(z["ny"] - 1, 1) and z["n"] >= 300
    S["real"] = S.apply(real, axis=1)
    good = S[S["real"]].sort_values("score", ascending=False)
    top = S.sort_values("score", ascending=False).head(12)
    md = [f"# VF SCALPER - +${TGT:.2f} IN {MINS} MINUTES - {datetime.now(NY):%Y-%m-%d %H:%M} ET",
          f"Data {start:%Y-%m-%d} to {end:%Y-%m-%d}, {', '.join(SYMBOLS)}, {', '.join(f'{t}m' for t in ST_TFS)}. Exact VF Scalper rules, fires 9:30-15:40. "
          f"DATA ONLY. Runtime {(time.time() - t0) / 60:.0f} min.",
          f"**Trade** = entry at the next open (live fires on the first tick), target +${TGT:.2f}, exit at the close after {MINS} minutes (or 15:55), "
          "stop = none / $0.25 / $0.50 / $1.00 (stop checked first inside a candle = conservative). **$** = per share of SPY / QQQ "
          "(x 100 x your option's delta for an option). **Hit %** = reached +$0.50 within 20 min (no stop); **random** = random entries the same "
          "way on the same charts. **vs random** = average $ minus random entries' average $ (the fair score). **Trend** = the trend line "
          f"at the fire: with / against. **REAL EDGE** = beats random by $0.01+ per share in {pn['tr']} AND {pn['te']}, 6+ of 8 charts, "
          "every year but one, 300+ fires.", "",
          "## The answer in 30 seconds",
          f"- **REAL EDGE: {len(good)}**" + (" - " + "; ".join(
              f"{z.k} ({z.f}, {z.s}): ${z.te:+.3f}/share vs random ({pn['te']}), hit {z.hit:.0f}% vs random {z.rhit:.0f}%, {z.charts}/{z.nch} charts, {z.ypos}/{z.ny} years"
              for z in good.head(6).itertuples()) if len(good) else " - none passed every check."), "",
          "## Top 12 (fire + trend filter + stop), sorted by both periods vs random",
          f"| Fire | Trend filter | Stop | Fires | Hit +$0.50 | Random hit | Avg $ | vs random {pn['tr']} | **vs random {pn['te']}** | Charts + | Years + | |",
          "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for z in top.itertuples():
        md.append(f"| {z.k} | {z.f} | {z.s} | {z.n} | {z.hit:.0f}% | {z.rhit:.0f}% | {z.usd:+.3f} | {z.tr:+.3f} | **{z.te:+.3f}** | {z.charts}/{z.nch} | {z.ypos}/{z.ny} | {'✅' if z.real else ''} |")
    md += ["", f"## Every fire, no stop (hit % and $ vs random, {pn['te']}) by trend filter",
           "| Fire | Off: fires / hit / vs random | With the line | Against the line |", "|---|---|---|---|"]
    for k_ in VFS_NAMES:
        cells = []
        for fnm, _ in FILTERS:
            r_ = S[(S["k"] == k_) & (S["f"] == fnm) & (S["s"] == "no stop")]
            cells.append(f"{int(r_.n.iloc[0])} / {r_.hit.iloc[0]:.0f}% / {r_.te.iloc[0]:+.3f}" if len(r_) else "-")
        md.append(f"| {k_} | " + " | ".join(cells) + " |")
    md += ["", f"## Which stop? (trend filter Off, $ vs random, {pn['te']})", "| Fire | " + " | ".join(SN) + " |", "|---|" + "---|" * len(SN)]
    for k_ in VFS_NAMES:
        cells = []
        for s_ in SN:
            r_ = S[(S["k"] == k_) & (S["f"] == "Off") & (S["s"] == s_)]
            cells.append(f"{r_.te.iloc[0]:+.3f}" if len(r_) else "-")
        md.append(f"| {k_} | " + " | ".join(cells) + " |")
    md += ["", "## Top 12 every year ($ vs random)", "| Fire | Filter | Stop | " + " | ".join(str(y_) for y_ in yrs) + " |", "|---|---|---|" + "---|" * len(yrs)]
    for z in top.itertuples():
        md.append(f"| {z.k} | {z.f} | {z.s} | " + " | ".join("-" if np.isnan(v) else f"{v:+.3f}" for v in z.ych) + " |")
    md += ["", f"## Top 12 every chart ({pn['te']}, $ vs random | fires)", "| Fire | Filter | Stop | " + " | ".join(f"{s_} {t_}m" for s_ in SYMBOLS for t_ in ST_TFS) + " |",
           "|---|---|---|" + "---|" * (len(SYMBOLS) * len(ST_TFS))]
    for z in top.itertuples():
        fv = dict(FILTERS)[z.f]
        g = E[(E["kind"] == z.k) & ((E["trend"] == fv) if fv else True) & (E["per"] == "te")]
        cells = []
        for s_ in SYMBOLS:
            for t_ in ST_TFS:
                gg = g[(g["sym"] == s_) & (g["tf"] == t_)]
                cells.append(f"{adj(gg, z.s):+.3f} ({len(gg)})" if len(gg) else "-")
        md.append(f"| {z.k} | {z.f} | {z.s} | " + " | ".join(cells) + " |")
    text = "\n".join(md + [""])
    print("\n" + text)
    stamp = datetime.now(NY).strftime("%Y-%m-%d")
    for path in (f"{OUT}/vfs_{stamp}.md", f"{OUT}/vfs_latest.md"):
        with open(path, "w") as f:
            f.write(text + "\n")
    sm = os.getenv("GITHUB_STEP_SUMMARY")
    if sm:
        with open(sm, "a") as f:
            f.write(text + "\n")


# ================================================================ VIX FIX WHIPLASH (MODE=wsw, the default)
# One side of the Vix Fix pane maxes out, then within N candles the OTHER side maxes out ("99 greed -> 99 fear").
# FOLLOW = trade the side that just took over (greed takes over -> LONG, fear takes over -> SHORT); FADE = the opposite.
WSW_T = (70, 80, 90, 95)          # "maxed out" = the number is at least this
WSW_N = (1, 2, 3, 5, 8, 12)       # the other side was maxed within the last N candles
WSW_K = (1, 2, 3, 5, 10)          # hold N candles


def wsw_events(F, G, hm, day, T, N, sess_end=1540):
    """Fire on the CLOSED candle i (9:30 <= time < sess_end), using only candles <= i:
    LONG  = greed crosses up to >= T now (was < T on i-1) and fear was >= T on one of the previous N candles (same day);
    SHORT = the mirror (fear crosses up, greed was maxed). One fire per swap: the other side needs a fresh >= T reading
    after this side's last fire. Both at once = no fire. Returns (side +1/-1/0, gap in candles, index of that last max)."""
    n = len(F)
    fH = (np.nan_to_num(F) >= T).tolist()
    gH = (np.nan_to_num(G) >= T).tolist()
    newday = np.r_[True, day[1:] != day[:-1]].tolist()
    inw = ((hm >= 930) & (hm < sess_end)).tolist()
    side = np.zeros(n, dtype=np.int64)
    gap = np.full(n, -1, dtype=np.int64)
    src = np.full(n, -1, dtype=np.int64)
    lastF = lastG = -10 ** 9
    firedL = firedS = -10 ** 9
    for i in range(n):
        if newday[i]:
            lastF = lastG = -10 ** 9
        elif inw[i]:
            L_ = gH[i] and not gH[i - 1] and lastF >= i - N and lastF > firedL
            S_ = fH[i] and not fH[i - 1] and lastG >= i - N and lastG > firedS
            if L_ and not S_:
                side[i], gap[i], src[i], firedL = 1, i - lastF, lastF, i
            elif S_ and not L_:
                side[i], gap[i], src[i], firedS = -1, i - lastG, lastG, i
        if fH[i]:
            lastF = i
        if gH[i]:
            lastG = i
    return side, gap, src


def wsw_outcomes(ind, idx, sd, ks=WSW_K):
    """Entry = next candle's open (same day, before 15:55). For each hold k: $ per share at the close of candle k
    (cut at the last candle before 16:00 that day), the worst move against you (heat) and the best move for you up to then."""
    o, h, l, c, hm, day = ind["o"], ind["h"], ind["l"], ind["c"], ind["hm"], ind["day"]
    n = len(o)
    K = max(ks)
    ret = np.full((len(idx), len(ks)), np.nan)
    heat = np.full((len(idx), len(ks)), np.nan)
    fav = np.full((len(idx), len(ks)), np.nan)
    for q, (i, s) in enumerate(zip(idx, sd)):
        e = i + 1
        if e >= n or day[e] != day[i] or hm[e] >= 1555:
            continue
        en = o[e]
        last = e
        while last + 1 < n and day[last + 1] == day[e] and hm[last + 1] < 1600 and last + 1 - e < K:
            last += 1
        lo = np.minimum.accumulate(l[e:last + 1])
        hi = np.maximum.accumulate(h[e:last + 1])
        for kk, k in enumerate(ks):
            j = min(k - 1, last - e)
            ret[q, kk] = s * (c[e + j] - en)
            heat[q, kk] = (en - lo[j]) if s == 1 else (hi[j] - en)
            fav[q, kk] = (hi[j] - en) if s == 1 else (en - lo[j])
    return ret, heat, fav


def wsw_main():
    end = datetime.now(timezone.utc) - timedelta(days=1)
    start = datetime.fromisoformat(os.getenv("WSW_START", "2020-01-01")).replace(tzinfo=timezone.utc)
    test = os.getenv("TEST", "") == "1"
    os.makedirs(OUT, exist_ok=True)
    split = pd.Timestamp(SPLIT, tz=NY)
    t0 = time.time()
    rng = np.random.default_rng(8)
    KN = [f"k{k}" for k in WSW_K]
    HN = [f"h{k}" for k in WSW_K]
    rows, base, anat = [], [], []
    for sym in SYMBOLS:
        print(f"\n=== {sym} ===", flush=True)
        df1, feed = fake_1m(sym, start, end) if test else fetch_1m(sym, start, end)
        for tf in ST_TFS:
            df = to_tf(df1, rth_only=False, mins=tf)
            ind = indicators(df, 13, 34, True)
            F, G = vfx_pane(df)
            hm, day = ind["hm"], ind["day"]
            years = np.asarray(df.index.year)
            per = np.where(df.index < split, "tr", "te")
            ndays = len(np.unique(day[(hm >= 930) & (hm < 1540)]))
            cnt = []
            for T in WSW_T:
                for N in WSW_N:
                    sg, gp, src = wsw_events(F, G, hm, day, T, N)
                    idx = np.nonzero(sg)[0]
                    cnt.append(len(idx))
                    if not len(idx):
                        continue
                    sd = sg[idx]
                    R, Hh, Fv = wsw_outcomes(ind, idx, sd)
                    # how far price already moved from the old side's max candle to the fire candle's close
                    moved = np.array([s * (ind["c"][i] - (ind["l"][a:i + 1].min() if s == 1 else ind["h"][a:i + 1].max()))
                                      for i, s, a in zip(idx, sd, src[idx])])
                    for dname, mult in (("FOLLOW", 1), ("FADE", -1)):
                        sdd = sd * mult
                        Rr, Hr = (R, Hh) if mult == 1 else (-R, Fv)     # fading = the mirror trade
                        d_ = pd.DataFrame(np.c_[Rr, Hr], columns=KN + HN)
                        d_["T"], d_["N"], d_["dir"], d_["sym"], d_["tf"] = T, N, dname, sym, tf
                        d_["side"] = np.where(sdd > 0, "LONG", "SHORT")
                        tr_ = ind["st"][idx] * sdd
                        d_["trend"] = np.where(tr_ > 0, "with", np.where(tr_ < 0, "against", "gray"))
                        d_["per"], d_["year"] = per[idx], years[idx]
                        rows.append(d_.dropna(subset=[KN[0]]))
                    if N == max(WSW_N):
                        anat.append(pd.DataFrame(dict(T=T, sym=sym, tf=tf, gap=gp[idx], moved=moved,
                                                      side=np.where(sd > 0, "fear->greed", "greed->fear"), ndays=ndays)))
            pool = np.nonzero((hm >= 930) & (hm < 1540))[0]
            ridx = np.sort(rng.choice(pool, size=min(len(pool), int(os.getenv("WSW_RANDOM", "8000"))), replace=False))
            for sdv, snm in ((1, "LONG"), (-1, "SHORT")):
                Rr, Hr, _ = wsw_outcomes(ind, ridx, np.full(len(ridx), sdv))
                d_ = pd.DataFrame(np.c_[Rr, Hr], columns=KN + HN)
                d_["sym"], d_["tf"], d_["side"] = sym, tf, snm
                d_["per"], d_["year"] = per[ridx], years[ridx]
                base.append(d_.dropna(subset=[KN[0]]))
            print(f"  {sym} {tf}m done ({time.time() - t0:.0f}s) | fires per setting {min(cnt)}-{max(cnt)}", flush=True)
        del df1
    E = pd.concat(rows, ignore_index=True)
    B = pd.concat(base, ignore_index=True)
    A = pd.concat(anat, ignore_index=True)
    cols = KN + HN
    bm_per = B.groupby(["sym", "tf", "side", "per"])[cols].mean()
    bm_yr = B.groupby(["sym", "tf", "side", "year"])[cols].mean()
    pn = {"tr": f"{start:%Y}-{int(SPLIT[:4]) - 1}", "te": f"{SPLIT[:4]}-now"}
    yrs = sorted(int(y) for y in E["year"].unique())

    def adj(g, col, by="per"):
        """average minus the random entries' average (matched chart, side, period or year)"""
        if not len(g):
            return np.nan
        bm = bm_per if by == "per" else bm_yr
        tot, nn = 0.0, 0
        for kk, gg in g.groupby(["sym", "tf", "side", by]):
            if kk in bm.index and not np.isnan(bm.loc[kk, col]):
                tot += (gg[col].mean() - bm.loc[kk, col]) * len(gg)
                nn += len(gg)
        return tot / nn if nn else np.nan

    summ = []
    for (T, N, dname, tf), g in E.groupby(["T", "N", "dir", "tf"]):
        if len(g) < 100:
            continue
        tr, te = g[g["per"] == "tr"], g[g["per"] == "te"]
        trk = [adj(tr, k_) for k_ in KN]
        if all(np.isnan(v) for v in trk):
            continue
        bk = int(np.nanargmax(trk))                       # the hold is picked on 2020-2023 only
        k_, h_ = KN[bk], HN[bk]
        ych = [adj(g[g["year"] == y_], k_, by="year") for y_ in yrs]
        se_tr = tr[k_].std() / np.sqrt(len(tr)) if len(tr) > 1 else np.nan
        se_te = te[k_].std() / np.sqrt(len(te)) if len(te) > 1 else np.nan
        summ.append(dict(T=T, N=N, d=dname, tf=tf, k=WSW_K[bk], n=len(g), nte=len(te), usd=g[k_].mean(),
                         tr=trk[bk], te=adj(te, k_), ttr=trk[bk] / se_tr if se_tr else np.nan,
                         tte=adj(te, k_) / se_te if se_te else np.nan, heat=te[h_].mean(), hvr=adj(te, h_),
                         green=100 * (te[k_] > 0).mean() if len(te) else np.nan,
                         syms=sum(1 for _, gg in te.groupby("sym") if adj(gg, k_) > 0), nsym=te["sym"].nunique(),
                         ych=ych, ypos=sum(1 for v in ych if v > 0), ny=sum(1 for v in ych if not np.isnan(v)),
                         tek=[adj(te, kk) for kk in KN]))
    S = pd.DataFrame(summ)
    S["score"] = S["tr"].fillna(-9) + S["te"].fillna(-9)

    def real(z):
        return (z["tr"] > 0.01 and z["te"] > 0.01 and z["ttr"] >= 2 and z["tte"] >= 2 and z["syms"] == z["nsym"]
                and z["ypos"] >= max(z["ny"] - 1, 1) and z["n"] >= 200)
    S["real"] = S.apply(real, axis=1)
    good = S[S["real"]].sort_values("score", ascending=False)
    top = S.sort_values("score", ascending=False).head(15)

    md = [f"# VIX FIX WHIPLASH - {datetime.now(NY):%Y-%m-%d %H:%M} ET",
          f"Data {start:%Y-%m-%d} to {end:%Y-%m-%d}, {', '.join(SYMBOLS)}, {', '.join(f'{t}m' for t in ST_TFS)} (pre/post market included in the "
          f"Vix Fix math, like your chart; fires 9:30-15:40 only). DATA ONLY. Runtime {(time.time() - t0) / 60:.0f} min.",
          "**Whiplash** = one side of the pane is maxed (number >= T), then within N candles the OTHER side crosses up to >= T. "
          "Fires on that candle. **FOLLOW** = trade the side that just took over (greed takes over = LONG, fear takes over = SHORT). "
          "**FADE** = the opposite. Entry = next open, exit at the close after k candles (the hold is picked on "
          f"{pn['tr']} only). **$** = per share of SPY / QQQ (x 100 x delta for an option). **vs random** = minus random entries the same way "
          "on the same chart. **Heat** = how far it went against you first (average). "
          f"**REAL EDGE** = +$0.01/share vs random in {pn['tr']} AND {pn['te']}, and at least 2x its noise (t >= 2) in BOTH periods, "
          "SPY and QQQ both positive, every year but one, 200+ fires. **t** = edge / its noise: 2+ = unlikely to be luck.", "",
          "## The answer in 30 seconds",
          f"- **REAL EDGE: {len(good)}**" + (" - " + "; ".join(
              f"{z.tf}m {z.d} T{z.T} within {z.N} candles, hold {z.k} candles ({z.k * z.tf} min): ${z.te:+.3f}/share vs random ({pn['te']}, t {z.tte:.1f}), "
              f"{z.ypos}/{z.ny} years" for z in good.head(6).itertuples()) if len(good) else " - none passed every check."), ""]

    # ---- anatomy: what a whiplash looks like
    md += ["## What a whiplash looks like (the 'average' you asked for), 9:30-15:40, other side maxed within 12 candles",
           "| Chart | Maxed = T | Per day | Gap: median candles (minutes) | Within 1 / 2 / 3 / 5 candles | Price already moved your way (median $) |",
           "|---|---|---|---|---|---|"]
    for (tf, T), g in A.groupby(["tf", "T"]):
        nd = g.drop_duplicates(["sym"])["ndays"].sum()
        gp = g["gap"]
        md.append(f"| {tf}m | {T} | {len(g) / max(nd, 1):.1f} | {gp.median():.0f} ({gp.median() * tf:.0f} min) | "
                  + " / ".join(f"{100 * (gp <= c_).mean():.0f}%" for c_ in (1, 2, 3, 5)) + f" | {g['moved'].median():+.2f} |")

    md += ["", f"## Top 15 settings (sorted by both periods vs random)",
           f"| Chart | Dir | Maxed T | Within N | Hold | Fires | vs random {pn['tr']} (t) | **vs random {pn['te']}** (t) | Green {pn['te']} | Heat (vs random) | SPY+QQQ + | Years + | |",
           "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for z in top.itertuples():
        md.append(f"| {z.tf}m | {z.d} | {z.T} | {z.N} | {z.k} ({z.k * z.tf} min) | {z.n} | {z.tr:+.3f} ({z.ttr:.1f}) | **{z.te:+.3f}** ({z.tte:.1f}) | {z.green:.0f}% | "
                  f"${z.heat:.2f} ({z.hvr:+.3f}) | {z.syms}/{z.nsym} | {z.ypos}/{z.ny} | {'✅' if z.real else ''} |")

    md += ["", f"## Speed: FOLLOW, $ vs random ({pn['te']}) after 1 / 2 / 3 / 5 / 10 candles, best T + N per chart"]
    for d_ in ("FOLLOW", "FADE"):
        md += ["", f"**{d_}**", "| Chart | T | N | Fires | " + " | ".join(f"{k} c" for k in WSW_K) + " |", "|---|---|---|---|" + "---|" * len(WSW_K)]
        for tf in ST_TFS:
            g = S[(S["d"] == d_) & (S["tf"] == tf)].sort_values("score", ascending=False).head(3)
            for z in g.itertuples():
                md.append(f"| {tf}m | {z.T} | {z.N} | {z.n} | " + " | ".join(f"{v:+.3f}" for v in z.tek) + " |")

    md += ["", "## Grid: FOLLOW, $ vs random at the TRAIN-picked hold (2020-23 / 2024-now), every T x N"]
    for tf in ST_TFS:
        md += ["", f"**{tf}m**", "| T \\ N | " + " | ".join(str(N) for N in WSW_N) + " |", "|---|" + "---|" * len(WSW_N)]
        for T in WSW_T:
            cells = []
            for N in WSW_N:
                r_ = S[(S["d"] == "FOLLOW") & (S["tf"] == tf) & (S["T"] == T) & (S["N"] == N)]
                cells.append(f"{r_.tr.iloc[0]:+.3f} / {r_.te.iloc[0]:+.3f}" if len(r_) else "-")
            md.append(f"| {T} | " + " | ".join(cells) + " |")

    md += ["", "## Top 15 every year ($ vs random)", "| Setting | " + " | ".join(str(y_) for y_ in yrs) + " |", "|---|" + "---|" * len(yrs)]
    for z in top.itertuples():
        md.append(f"| {z.tf}m {z.d} T{z.T} N{z.N} k{z.k} | " + " | ".join("-" if np.isnan(v) else f"{v:+.3f}" for v in z.ych) + " |")

    md += ["", f"## Top 5 split by the trend line ({pn['te']}, $ vs random | fires)", "| Setting | With the line | Against the line | Gray |", "|---|---|---|---|"]
    for z in top.head(5).itertuples():
        g = E[(E["T"] == z.T) & (E["N"] == z.N) & (E["dir"] == z.d) & (E["tf"] == z.tf) & (E["per"] == "te")]
        cells = []
        for tv in ("with", "against", "gray"):
            gg = g[g["trend"] == tv]
            cells.append(f"{adj(gg, f'k{z.k}'):+.3f} ({len(gg)})" if len(gg) else "-")
        md.append(f"| {z.tf}m {z.d} T{z.T} N{z.N} k{z.k} | " + " | ".join(cells) + " |")

    text = "\n".join(md + [""])
    print("\n" + text)
    stamp = datetime.now(NY).strftime("%Y-%m-%d")
    for path in (f"{OUT}/wsw_{stamp}.md", f"{OUT}/wsw_latest.md"):
        with open(path, "w") as f:
            f.write(text + "\n")
    sm = os.getenv("GITHUB_STEP_SUMMARY")
    if sm:
        with open(sm, "a") as f:
            f.write(text + "\n")


if __name__ == "__main__":
    main()
