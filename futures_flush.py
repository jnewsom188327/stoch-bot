"""
FLUSH FLIP - FUTURES STUDY (DATA ONLY - no orders).

The move from Oct 28 11:00 (SPY 1m): fear flushes to a peak, then the turn lines up -
  TTM turns up (2 rising candles), Vix Fix + TTM AGREE UP (greed average rising, fear average falling),
  the squeeze FIRES, the trend line turns green. Mirror for shorts (greed peak -> agree down).
Futures (ES / NQ) have no long minute history on Alpaca, so the long test runs on SPY / QQQ (they move with ES / NQ
tick for tick, 2020-now) and results are shown in ATR, then in ES / NQ points (x the ES/SPY and NQ/QQQ price ratio),
net of 2 ticks of cost per round trip. Then the same detector runs on REAL ES / NQ 1-minute candles for the last
~29 days (Yahoo, all 23 hours) as a reality check.

Same indicator math as your TradingView scripts (Flow TTM / Flow Vix Fix Rainbow) and backtest.py (imported).
Writes results/futures_flush.md (+ results/futures_flush_events.csv.gz, main versions).
"""
import os
import sys
import time
from datetime import datetime, timedelta, timezone

import numpy as np
import pandas as pd

import backtest as B

NY = B.NY
OUT = "results"
SYMS = [s.strip().upper() for s in os.getenv("FLUSH_SYMBOLS", "SPY,QQQ").split(",") if s.strip()]
START = os.getenv("FLUSH_START", "2020-01-01").strip() or "2020-01-01"
SPLIT = pd.Timestamp("2024-01-01").date()
FUT = {"SPY": ("ES", "ES=F", 10.0, 50.0), "QQQ": ("NQ", "NQ=F", 41.0, 20.0)}   # name, Yahoo, fallback ratio, $ per point
COST_PTS = 0.5               # 2 ticks round trip (ES / NQ tick = 0.25)
EXITS = ["H10", "H20", "H30", "IND", "BR", "FL"]
EXIT_NAME = {"H10": "hold 10 min", "H20": "hold 20 min", "H30": "hold 30 min",
             "IND": "your exit: TTM turns against or agree flips (max 60)",
             "BR": "stop 1 ATR / target 2 ATR (max 30)", "FL": "stop under the flush low, else your exit"}
TEST = os.getenv("TEST", "") == "1"
RNG = np.random.default_rng(7)


# ---------------------------------------------------------------- the indicators (your Pine math)
def build(df, close_hm=1600):
    ind = B.indicators(df, 13, 34, True)
    F, G = B.vfx_pane(df)
    F, G = np.nan_to_num(F), np.nan_to_num(G)
    mom = np.asarray(B.cl_ttm(df)[0], dtype=float)
    a = ind["atr"]
    m = np.where(a > 0, mom / np.where(a > 0, a, 1), 0.0)
    m = np.nan_to_num(m)
    n = len(m)
    up = np.r_[False, m[1:] > m[:-1]]
    dn = np.r_[False, m[1:] < m[:-1]]
    state = np.zeros(n, dtype=np.int8)
    ur = dr = 0
    s = 0
    for i in range(n):
        ur = ur + 1 if up[i] else 0
        dr = dr + 1 if dn[i] else 0
        if ur >= 2:
            s = 1
        if dr >= 2:
            s = -1
        state[i] = s
    gA = pd.Series(G).ewm(span=10, adjust=False).mean().to_numpy()
    fA = pd.Series(F).ewm(span=10, adjust=False).mean().to_numpy()
    gr, fr = np.r_[False, gA[1:] > gA[:-1]], np.r_[False, fA[1:] > fA[:-1]]
    gf, ff = np.r_[False, gA[1:] < gA[:-1]], np.r_[False, fA[1:] < fA[:-1]]
    agreeUp = (state == 1) & gr & ff
    agreeDn = (state == -1) & gf & fr
    # squeeze like Flow TTM: 2 x stdev(20) inside 1.5 x RMA(true range, 20); FIRED = off now, on in one of the last 3
    c = df["close"]
    pc = c.shift(1)
    tr = pd.concat([df["high"] - df["low"], (df["high"] - pc).abs(), (df["low"] - pc).abs()], axis=1).max(axis=1)
    kc = 1.5 * tr.ewm(alpha=1 / 20, adjust=False).mean()
    sqOn = (2 * c.rolling(20).std(ddof=0) < kc).fillna(False).to_numpy()
    sqF = ~sqOn & (np.r_[False, sqOn[:-1]] | np.r_[False, False, sqOn[:-2]] | np.r_[False, False, False, sqOn[:-3]])
    sqF5 = pd.Series(sqF).rolling(6, min_periods=1).max().astype(bool).to_numpy()   # fired this candle or in the last 5
    zc_up = pd.Series((m >= 0) & (np.r_[0.0, m[:-1]] < 0)).rolling(4, min_periods=1).max().astype(bool).to_numpy()
    zc_dn = pd.Series((m < 0) & (np.r_[0.0, m[:-1]] >= 0)).rolling(4, min_periods=1).max().astype(bool).to_numpy()
    hm, day = ind["hm"], ind["day"]
    idx = np.arange(n)
    dend = pd.Series(np.where(hm < close_hm, idx, -1)).groupby(day).transform("max").to_numpy()
    return dict(against1=(state == -1) | agreeDn, against_1=(state == 1) | agreeUp,
                o=ind["o"], h=ind["h"], l=ind["l"], c=ind["c"], atr=a, hm=hm, day=day, st=ind["st"], F=F, G=G, state=state,
                agreeUp=agreeUp, agreeDn=agreeDn, sqF5=sqF5, zc_up=zc_up, zc_dn=zc_dn, dend=dend, n=n)


# ---------------------------------------------------------------- the setups
def variants(X):
    S = X
    up_base = (S["state"] == 1) & S["agreeUp"]
    dn_base = (S["state"] == -1) & S["agreeDn"]
    V = {}
    for pk in (85, 95, 100):
        for w in (10, 20):
            V[f"base p{pk} w{w}"] = (pk, w, up_base, dn_base)
            V[f"FULL p{pk} w{w}"] = (pk, w, up_base & S["sqF5"] & (S["st"] == 1), dn_base & S["sqF5"] & (S["st"] == -1))
    V["+squeeze p95 w20"] = (95, 20, up_base & S["sqF5"], dn_base & S["sqF5"])
    V["+green/red line p95 w20"] = (95, 20, up_base & (S["st"] == 1), dn_base & (S["st"] == -1))
    V["zero-cross + agree p95 w20"] = (95, 20, S["zc_up"] & S["agreeUp"], S["zc_dn"] & S["agreeDn"])
    return V


def detect(S, peak, win, cond, side, t_from, t_to):
    """one event per flush: the first candle (within `win` candles of the latest peak, same day) where cond is true"""
    X = S["F"] if side == 1 else S["G"]
    hm, day = S["hm"], S["day"]
    nxt_ok = np.r_[day[1:] == day[:-1], False]
    peaks = np.nonzero(X >= peak - 1e-9)[0]
    cand = np.nonzero(cond & (hm >= t_from) & (hm <= t_to) & nxt_ok & (S["atr"] > 0))[0]
    out, used = [], -1
    if not len(peaks):
        return out
    pos = np.searchsorted(peaks, cand, side="right") - 1
    for i, q in zip(cand, pos):
        if q < 0:
            continue
        p = peaks[q]
        if p == used or i - p > win or day[p] != day[i]:
            continue
        out.append(int(i))
        used = p
    return out


# ---------------------------------------------------------------- exits
def sim(S, i, d, kind, win):
    o, h, l, c, a, dend = S["o"], S["h"], S["l"], S["c"], S["atr"], S["dend"]
    e0 = i + 1
    last = dend[i]
    if last < e0:
        return np.nan
    p0, A = o[e0], a[i]
    if kind[0] == "H":
        x = min(e0 + int(kind[1:]) - 1, last)
        return d * (c[x] - p0)
    against = S["against1"] if d == 1 else S["against_1"]
    stp = None
    if kind == "FL":
        lo = max(0, i - win)
        stp = l[lo:i + 1].min() if d == 1 else h[lo:i + 1].max()
    if kind == "BR":
        stp, tgt = p0 - d * A, p0 + 2 * d * A
        for j in range(e0, min(last, e0 + 29) + 1):
            if (d == 1 and l[j] <= stp) or (d == -1 and h[j] >= stp):
                return d * ((min(o[j], stp) if d == 1 else max(o[j], stp)) - p0)
            if (d == 1 and h[j] >= tgt) or (d == -1 and l[j] <= tgt):
                return d * ((max(o[j], tgt) if d == 1 else min(o[j], tgt)) - p0)
        return d * (c[min(last, e0 + 29)] - p0)
    cap = min(last, e0 + 59)
    for j in range(e0, cap + 1):
        if stp is not None and ((d == 1 and l[j] <= stp) or (d == -1 and h[j] >= stp)):
            return d * ((min(o[j], stp) if d == 1 else max(o[j], stp)) - p0)
        if against[j]:
            return d * ((o[j + 1] if j + 1 <= last else c[j]) - p0)
    return d * (c[cap] - p0)


def random_base(S, sym, t_from, t_to, nr=12000):
    hm, day = S["hm"], S["day"]
    nxt_ok = np.r_[day[1:] == day[:-1], False]
    pool = np.nonzero((hm >= t_from) & (hm <= t_to) & nxt_ok & (S["atr"] > 0))[0]
    if not len(pool):
        return pd.DataFrame()
    pick = RNG.choice(pool, size=min(nr, len(pool)), replace=False)
    rows = []
    for i in pick:
        for d in (1, -1):
            r = dict(sym=sym, d=d, year=day[i].year, per="tr" if day[i] < SPLIT else "te")
            for k in EXITS:
                r[k] = sim(S, i, d, k, 20) / S["atr"][i]
            rows.append(r)
    return pd.DataFrame(rows)


def score(ev, base, k):
    """mean edge vs random (ATR) and its t, day-clustered, per period"""
    out = {}
    for p in ("tr", "te", "all"):
        x = ev if p == "all" else ev[ev["per"] == p]
        if len(x) < 20:
            out[p] = (np.nan, np.nan, len(x))
            continue
        b = base.groupby(["sym", "d", "year"])[k].mean()
        adj = x[k] - b.reindex(pd.MultiIndex.from_arrays([x["sym"], x["d"], x["year"]])).to_numpy()
        adj = adj.dropna()
        m = adj.mean()
        cs = (adj - m).groupby(x.loc[adj.index, "date"]).sum()
        se = np.sqrt((cs ** 2).sum()) / len(adj)
        out[p] = (m, m / se if se > 0 and len(cs) > 2 else np.nan, len(adj))
    return out


def fmt(s, p):
    m, t, _ = s[p]
    return "-" if np.isnan(m) else (f"{m:+.2f} ({t:.1f})" if not np.isnan(t) else f"{m:+.2f}")


# ---------------------------------------------------------------- real futures (Yahoo, last ~29 days)
def yahoo_1m(tk):
    import yfinance as yf
    end = datetime.now(timezone.utc)
    parts = []
    cur = end - timedelta(days=29)
    while cur < end:
        nxt = min(cur + timedelta(days=7), end)
        d = yf.download(tk, start=cur, end=nxt, interval="1m", progress=False, auto_adjust=False)
        if d is not None and len(d):
            if isinstance(d.columns, pd.MultiIndex):
                d.columns = d.columns.get_level_values(0)
            parts.append(d)
        cur = nxt
    if not parts:
        raise RuntimeError("no Yahoo bars")
    d = pd.concat(parts)
    d = d[~d.index.duplicated()].sort_index()
    d.index = d.index.tz_convert(NY)
    d = d.rename(columns=str.lower)[["open", "high", "low", "close", "volume"]].astype(float)
    return d[d["volume"] >= 0]


def main():
    t0 = time.time()
    os.makedirs(OUT, exist_ok=True)
    end = datetime.now(timezone.utc) - timedelta(days=1)
    start = datetime.fromisoformat(START).replace(tzinfo=timezone.utc)
    EV, BASE, ratio, live = [], [], {}, {}
    for sym in SYMS:
        print(f"\n=== {sym} ===", flush=True)
        df1, feed = B.fake_1m(sym, start, end) if TEST else B.fetch_1m(sym, start, end)
        df = B.to_tf(df1, rth_only=False, mins=1)
        del df1
        S = build(df)
        print(f"  {len(df):,} candles, indicators {time.time() - t0:.0f}s", flush=True)
        BASE.append(random_base(S, sym, 935, 1530))
        for name, (pk, w, cu, cd) in variants(S).items():
            for side, cond in ((1, cu), (-1, cd)):
                for i in detect(S, pk, w, cond, side, 935, 1530):
                    r = dict(sym=sym, var=name, d=side, t=str(df.index[i]), date=S["day"][i], year=S["day"][i].year,
                             per="tr" if S["day"][i] < SPLIT else "te", px=S["c"][i], atr=S["atr"][i])
                    for k in EXITS:
                        r[k] = sim(S, i, side, k, w) / S["atr"][i]
                        r[k + "_pts"] = sim(S, i, side, k, w)
                    EV.append(r)
        print(f"  events done {time.time() - t0:.0f}s", flush=True)
        ratio[sym] = (FUT[sym][2], float(df["close"].iloc[-1]))
        del df, S
    E = pd.DataFrame(EV)
    BS = pd.concat(BASE, ignore_index=True)
    E[E["var"].isin(["base p95 w20", "FULL p95 w20", "FULL p85 w20", "base p100 w10"])].to_csv(f"{OUT}/futures_flush_events.csv.gz", index=False)

    # real futures
    fut_rows, fut_note = [], ""
    for sym in SYMS:
        nm, tk, rr, _ = FUT.get(sym, (sym, None, 1.0, 1.0))
        if not tk:
            continue
        try:
            fd = yahoo_1m(tk)
            ratio[sym] = (float(fd["close"].iloc[-1]) / ratio[sym][1], ratio[sym][1])
            S = build(fd, close_hm=2400)
            base = random_base(S, nm, 0, 2359, nr=4000)
            for name in ("base p95 w20", "FULL p95 w20", "FULL p85 w20", "base p100 w10"):
                pk, w, cu, cd = variants(S)[name]
                for lab, tf, tt in (("all hours", 0, 2359), ("9:35-15:30", 935, 1530)):
                    rows = []
                    for side, cond in ((1, cu), (-1, cd)):
                        for i in detect(S, pk, w, cond, side, tf, tt):
                            rows.append(dict(d=side, year=S["day"][i].year, **{k: sim(S, i, side, k, w) for k in EXITS},
                                             **{k + "_a": sim(S, i, side, k, w) / S["atr"][i] for k in EXITS}))
                    g = pd.DataFrame(rows)
                    if len(g):
                        bmean = {k: base[k].mean() for k in EXITS} if len(base) else {k: 0 for k in EXITS}
                        fut_rows.append(dict(fut=nm, var=name, hours=lab, n=len(g), **{k: g[k].mean() - COST_PTS for k in EXITS},
                                             **{k + "_edge": g[k + "_a"].mean() - bmean[k] for k in EXITS},
                                             win20=(g["H20"] > COST_PTS).mean()))
            print(f"  {nm} real futures: {len(fd):,} candles", flush=True)
        except Exception as e:  # noqa: BLE001
            fut_note += f"- {nm} ({tk}): could not load real futures candles ({str(e)[:150]}). Only the SPY/QQQ test below.\n"
            print(f"  {nm} real futures failed: {e}", flush=True)
    write(E, BS, ratio, pd.DataFrame(fut_rows), fut_note, t0)


def write(E, BS, ratio, FR, fut_note, t0):
    now = datetime.now(NY)
    L = [f"# FLUSH FLIP - FUTURES STUDY - {now:%Y-%m-%d %H:%M} ET",
         f"SPY -> ES, QQQ -> NQ (1m, {START} to yesterday). DATA ONLY. Runtime {(time.time() - t0) / 60:.0f} min.",
         "**The setup (Oct 28 11:00):** fear peaks (85 / 95 / 100) -> within 10 or 20 candles TTM turns up (2 rising candles) and "
         "Vix Fix + TTM AGREE UP (greed avg rising, fear avg falling). **FULL** = also the squeeze fired in the last 5 candles and "
         "the line is green. Shorts = the mirror (greed peak -> agree down, line red). One trade per flush, signal 9:35-15:30, "
         "entry next open.",
         "**vs random** = ATR result minus random entries the same way, same ticker, same year, same exit (0 = no edge). "
         "**t** = edge / noise by day (2+ = unlikely luck). 2020-23 / **2024-now** are separate checks.",
         f"**Futures points:** SPY x {ratio.get('SPY', (10, 0))[0]:.2f} = ES, QQQ x {ratio.get('QQQ', (41, 0))[0]:.2f} = NQ, minus "
         f"{COST_PTS} pt (2 ticks) per round trip. MES = $5/pt, ES = $50/pt, MNQ = $2/pt, NQ = $20/pt.", ""]
    if E.empty:
        L.append("No events.")
        open(f"{OUT}/futures_flush.md", "w").write("\n".join(L))
        return
    E = E.copy()
    for k in EXITS:
        E[k + "_fut"] = E[k + "_pts"] * E["sym"].map(lambda s: ratio.get(s, (1, 0))[0]) - COST_PTS
    best = []
    L += ["## 1) Every setup - best exit, edge vs random (ATR): 2020-23 / **2024-now**",
          "| Setup | Trades | /day | Best exit | vs random 2020-23 (t) | **vs random 2024-now (t)** | Raw ATR | Win % | ES pts net (SPY) | NQ pts net (QQQ) |",
          "|---|---|---|---|---|---|---|---|---|---|"]
    ndays = max(1, E["date"].nunique())
    alld = max(1, len(pd.bdate_range(START, now.date())))
    for name, g in E.groupby("var", sort=False):
        sc = {k: score(g, BS, k) for k in EXITS}
        k = max(EXITS, key=lambda k: (np.nan_to_num(sc[k]["te"][0], nan=-9), np.nan_to_num(sc[k]["tr"][0], nan=-9)))
        s = sc[k]
        es = g[g["sym"] == "SPY"][k + "_fut"].mean() if (g["sym"] == "SPY").any() else np.nan
        nq = g[g["sym"] == "QQQ"][k + "_fut"].mean() if (g["sym"] == "QQQ").any() else np.nan
        best.append((name, k, s, len(g), es, nq, g))
        L.append(f"| {name} | {len(g)} | {len(g) / alld:.1f} | {EXIT_NAME[k]} | {fmt(s, 'tr')} | **{fmt(s, 'te')}** | {g[k].mean():+.2f} | "
                 f"{(g[k] > 0).mean() * 100:.0f}% | {es:+.2f} | {nq:+.2f} |")
    real = [b for b in best if all(not np.isnan(b[2][p][0]) and b[2][p][0] >= 0.05 and b[2][p][1] >= 2 for p in ("tr", "te"))]
    L += ["", "## 2) Every exit for the main versions (ATR vs random, 2024-now (t)) and ES / NQ points net"]
    for name in ("base p95 w20", "FULL p95 w20", "FULL p85 w20", "base p100 w10"):
        g = E[E["var"] == name]
        if not len(g):
            continue
        L += [f"### {name} ({len(g)} trades)", "| Exit | vs random 2020-23 (t) | **2024-now (t)** | Raw ATR | Win % | ES pts | NQ pts | Longs ATR | Shorts ATR |",
              "|---|---|---|---|---|---|---|---|---|"]
        for k in EXITS:
            s = score(g, BS, k)
            es = g[g["sym"] == "SPY"][k + "_fut"].mean()
            nq = g[g["sym"] == "QQQ"][k + "_fut"].mean()
            L.append(f"| {EXIT_NAME[k]} | {fmt(s, 'tr')} | **{fmt(s, 'te')}** | {g[k].mean():+.2f} | {(g[k] > 0).mean() * 100:.0f}% | "
                     f"{es:+.2f} | {nq:+.2f} | {g[g['d'] == 1][k].mean():+.2f} | {g[g['d'] == -1][k].mean():+.2f} |")
        L.append("")
    L += ["## 3) Every year - FULL p95 w20, your exit (raw ATR / vs random, trades)", "| Year | SPY | QQQ |", "|---|---|---|"]
    g = E[E["var"] == "FULL p95 w20"]
    if len(g):
        b = BS.groupby(["sym", "d", "year"])["IND"].mean()
        g = g.assign(adj=g["IND"] - b.reindex(pd.MultiIndex.from_arrays([g["sym"], g["d"], g["year"]])).to_numpy())
        for y, gy in g.groupby("year"):
            cells = []
            for s_ in ("SPY", "QQQ"):
                x = gy[gy["sym"] == s_]
                cells.append(f"{x['IND'].mean():+.2f} / {x['adj'].mean():+.2f} ({len(x)})" if len(x) else "-")
            L.append(f"| {y} | " + " | ".join(cells) + " |")
    L += ["", "## 4) Real ES / NQ futures - last ~29 days (Yahoo 1m) - points per trade NET of 2 ticks", fut_note]
    if len(FR):
        L += ["| Future | Setup | Hours | Trades | hold 10 | hold 20 | hold 30 | your exit | 1/2 ATR bracket | flush-low stop | Win % (20m) | edge vs random, your exit (ATR) |",
              "|---|---|---|---|---|---|---|---|---|---|---|---|"]
        for _, r in FR.iterrows():
            L.append(f"| {r['fut']} | {r['var']} | {r['hours']} | {r['n']} | {r['H10']:+.2f} | {r['H20']:+.2f} | {r['H30']:+.2f} | "
                     f"{r['IND']:+.2f} | {r['BR']:+.2f} | {r['FL']:+.2f} | {r['win20'] * 100:.0f}% | {r['IND_edge']:+.2f} |")
        L.append("29 days is a small sample - read it as 'does it behave the same on the real contract', not as proof.")
    L += ["", "## The answer in 30 seconds"]
    if real:
        for name, k, s, n, es, nq, _ in sorted(real, key=lambda b: -b[2]["te"][0])[:4]:
            L.append(f"- ✅ **{name}** with *{EXIT_NAME[k]}*: {fmt(s, 'tr')} / **{fmt(s, 'te')}** ATR vs random over {n} trades; "
                     f"about {es:+.2f} ES pts / {nq:+.2f} NQ pts per trade after costs.")
    else:
        L.append("- ❌ No version beat random entries by +0.05 ATR with t 2+ in BOTH 2020-23 and 2024-now.")
        top = sorted(best, key=lambda b: -np.nan_to_num(b[2]["te"][0], nan=-9))[:3]
        for name, k, s, n, es, nq, _ in top:
            L.append(f"- closest: **{name}** / {EXIT_NAME[k]}: {fmt(s, 'tr')} / **{fmt(s, 'te')}** ({n} trades).")
    L.append("- A setup that looks great on one screenshot can still be average over 6 years: the table is the judge.")
    text = "\n".join(L) + "\n"
    open(f"{OUT}/futures_flush.md", "w").write(text)
    print(text)
    sm = os.getenv("GITHUB_STEP_SUMMARY")
    if sm:
        open(sm, "a").write(text)


if __name__ == "__main__":
    main()
