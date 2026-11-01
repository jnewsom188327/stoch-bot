# ============================================================================================================
# MODE=div - DIV PRO (DIV Reversal Pro) BACKTEST. Same math as the Pine indicator: 5/2 swings, MACD line +
# histogram + RSI divergence, Vix Fix grade point, turn candle, fire at the next open, swing stop, TP1 1x / TP2 2x
# ATR, original stop kept, 30-bar time limit, windows 4:45-9:30 + 9:45-14:30 ET. Every chart in TFS, every ticker
# in SYMBOLS, START to now. Baseline = random entries (same day, side and stop size). Settings sweep picked on TRAIN
# (before SPLIT), checked on TEST (SPLIT to now). DATA ONLY - no orders.
# This block runs when MODE is empty or "div" (the backtest workflow does not set MODE).
# ============================================================================================================
DIV_DEF = dict(trig="turn", min_grade=2, arm=6, cooldown=5, max_day=6, pvL=5, pvR=2, min_gap=5, max_gap=60,
               use_hist=True, use_rsi=True, use_wvf=True, sl="swing", sl_buf=0.2, sl_min=0.5, sl_max=2.0, sl_atr=1.5,
               tp1=1.0, tp2=2.0, max_hold=30)


def div_rma(x, n):
    x = pd.Series(x)
    return x.ewm(alpha=1.0 / n, adjust=False, min_periods=n).mean().to_numpy()


def div_ema(x, n):
    return pd.Series(x).ewm(span=n, adjust=False, min_periods=n).mean().to_numpy()


def div_ind(df):
    o, h, l, c = (df[k].to_numpy(float) for k in ("open", "high", "low", "close"))
    pc = np.r_[np.nan, c[:-1]]
    tr = np.nanmax(np.vstack([h - l, np.abs(h - pc), np.abs(l - pc)]), axis=0)
    atr = div_rma(tr, 14)
    macd = div_ema(c, 12) - div_ema(c, 26)
    hist = macd - div_ema(macd, 9)
    d = np.diff(c, prepend=np.nan)
    up, dn = div_rma(np.where(d > 0, d, 0.0), 14), div_rma(np.where(d < 0, -d, 0.0), 14)
    rsi = np.where(dn == 0, 100.0, 100.0 - 100.0 / (1.0 + up / np.where(dn == 0, 1, dn)))
    cs = pd.Series(c)
    hiC, loC = cs.rolling(22).max().to_numpy(), cs.rolling(22).min().to_numpy()
    fear = (hiC - l) / hiC * 100
    greed = (h - loC) / loC * 100

    def hot(x):
        s = pd.Series(x)
        bb = s.rolling(20).mean() + 2.0 * s.rolling(20).std(ddof=0)
        rng = s.rolling(50).max() * 0.85
        return ((s >= bb) | (s >= rng)).fillna(False).to_numpy()

    fearRec = pd.Series(hot(fear).astype(float)).rolling(11, min_periods=1).max().to_numpy() > 0
    greedRec = pd.Series(hot(greed).astype(float)).rolling(11, min_periods=1).max().to_numpy() > 0
    t = df.index
    hm = (t.hour * 100 + t.minute).to_numpy()
    day = np.asarray(t.date)
    tf_min = int(round((t[1] - t[0]).total_seconds() / 60)) if len(t) > 1 else 1
    end_t = t + pd.Timedelta(minutes=tf_min)
    hm_end = (end_t.hour * 100 + end_t.minute).to_numpy()
    eod = (hm < 1600) & ((hm_end >= 1600) | (np.asarray(end_t.date) != day))
    sess = ((hm >= 445) & (hm < 930)) | ((hm >= 945) & (hm < 1430))
    return dict(o=o, h=h, l=l, c=c, atr=atr, macd=macd, hist=hist, rsi=rsi, fearRec=fearRec, greedRec=greedRec,
                hm=hm, day=day, eod=eod, sess=sess, year=t.year.to_numpy(), n=len(c))


def div_pivots(x, L, R, low=True):
    """Pivot index c confirmed at bar c+R: lowest (highest) of the L bars on the left (strict) and R on the right."""
    s = pd.Series(x if low else -x)
    left = s.shift(1).rolling(L).min()
    right = s[::-1].shift(1).rolling(R).min()[::-1]
    ok = (s < left) & (s <= right)
    return np.nonzero(ok.fillna(False).to_numpy())[0]


def div_events(I, P):
    """Bull / bear divergences: list of (detected_bar, swing_price, count of oscillators that diverge)."""
    out = {}
    for side in (1, -1):
        piv = div_pivots(I["l"] if side == 1 else I["h"], P["pvL"], P["pvR"], low=(side == 1))
        price = I["l"] if side == 1 else I["h"]
        ev, last = [], None
        for cb in piv:
            m, hh, r = I["macd"][cb], I["hist"][cb], I["rsi"][cb]
            if np.isnan(m) or np.isnan(hh) or np.isnan(r):
                last = (cb, price[cb], m, hh, r)
                continue
            if last is not None:
                lb, lp, lm, lh, lr = last
                gap = cb - lb
                newer = price[cb] < lp if side == 1 else price[cb] > lp
                if newer and P["min_gap"] <= gap <= P["max_gap"]:
                    if side == 1:
                        k = int(m > lm) + int(bool(P["use_hist"]) and hh > lh) + int(bool(P["use_rsi"]) and r > lr)
                    else:
                        k = int(m < lm) + int(bool(P["use_hist"]) and hh < lh) + int(bool(P["use_rsi"]) and r < lr)
                    if k > 0:
                        ev.append((cb + P["pvR"], price[cb], int(k)))
            last = (cb, price[cb], m, hh, r)
        out[side] = ev
    return out


def div_signals(I, EV, P):
    """Signal bars (judged on the closed candle): dict bar -> (side, grade, stop price)."""
    n, h, l, hist, atr = I["n"], I["h"], I["l"], I["hist"], I["atr"]
    turnUp = np.zeros(n, bool)
    turnDn = np.zeros(n, bool)
    turnUp[1:] = (I["c"][1:] > h[:-1]) & (hist[1:] > hist[:-1])
    turnDn[1:] = (I["c"][1:] < l[:-1]) & (hist[1:] < hist[:-1])
    sig = {}
    for side in (1, -1):
        ev = EV[side]
        nxt = [e[0] for e in ev[1:]] + [n]
        rec = I["fearRec"] if side == 1 else I["greedRec"]
        turn = turnUp if side == 1 else turnDn
        for (b, swing, k), stop_next in zip(ev, nxt):
            last = min(b + P["arm"] - 1, stop_next - 1, n - 1)
            for j in range(b, last + 1):
                if j > b and (l[j] < swing if side == 1 else h[j] > swing):
                    break
                trig = (j == b) if P["trig"] == "div" else turn[j]
                g = k + (1 if P["use_wvf"] and rec[j] else 0)
                if trig and g >= P["min_grade"]:
                    stop = swing - side * P["sl_buf"] * atr[j]
                    if side == 1 or j not in sig:      # a long wins a same-candle tie, like the Pine
                        sig[j] = (side, g, stop)
                    break
    return sig


def div_trade(I, f, d, dist_atr, P):
    """Grade one trade entered at bar f's open. Returns (outcome, R in ATR, exit bar, TP1 hit)."""
    o, h, l, c, a = I["o"], I["h"], I["l"], I["c"], I["atr"][f - 1]
    e = o[f]
    t1, t2, sl = e + d * P["tp1"] * a, e + d * P["tp2"] * a, e - d * dist_atr * a
    hit1 = False
    for j in range(f, min(I["n"], f + 400)):
        hs = l[j] <= sl if d > 0 else h[j] >= sl
        h1 = h[j] >= t1 if d > 0 else l[j] <= t1
        h2 = h[j] >= t2 if d > 0 else l[j] <= t2
        if not hit1:
            if hs:
                return "SL", -dist_atr, j, False
            if h1:
                hit1 = True
                if h2:
                    return "TP2", 0.5 * P["tp1"] + 0.5 * P["tp2"], j, True
        else:
            if hs:
                return "SL1", 0.5 * P["tp1"] - 0.5 * dist_atr, j, True
            if h2:
                return "TP2", 0.5 * P["tp1"] + 0.5 * P["tp2"], j, True
        if j - f >= P["max_hold"] or I["eod"][j]:
            cl = (c[j] - e) * d / a
            return "T", (0.5 * P["tp1"] + 0.5 * cl) if hit1 else cl, j, hit1
    return "T", 0.0, I["n"] - 1, hit1


def div_run(I, P, EV=None):
    EV = EV if EV is not None else div_events(I, P)
    sig = div_signals(I, EV, P)
    o, a, day, sess = I["o"], I["atr"], I["day"], I["sess"]
    rows, last_fire, busy_until, cur_day, cnt = [], -10 ** 9, -1, None, 0
    for s in sorted(sig):
        f = s + 1
        if f >= I["n"] or not sess[f] or not (a[s] > 0):
            continue
        if day[f] != cur_day:
            cur_day, cnt = day[f], 0
        if f <= busy_until or f - last_fire < P["cooldown"] or cnt >= P["max_day"]:
            continue
        d, g, stop = sig[s]
        if P["sl"] == "swing":
            sw = (o[f] - stop) if d > 0 else (stop - o[f])
            dist = min(max(sw, P["sl_min"] * a[s]), P["sl_max"] * a[s]) / a[s]
        else:
            dist = P["sl_atr"]
        out, r, x, w = div_trade(I, f, d, dist, P)
        rows.append(dict(bar=f, side=d, grade=g, dist=dist, out=out, r=r, win=w, usd=r * a[s], atr=a[s],
                         year=I["year"][f], hm=I["hm"][f], exit=x))
        last_fire, busy_until, cnt = f, x, cnt + 1
    return pd.DataFrame(rows)


def div_random(I, T, P, seeds=5):
    """Same count, same day, same side and same stop size - random candle inside the fire windows."""
    if not len(T):
        return np.nan
    ok = np.nonzero(I["sess"] & (I["atr"] > 0))[0]
    ok = ok[ok > 0]
    byday = pd.Series(ok).groupby(I["day"][ok]).apply(lambda s: s.to_numpy()).to_dict()
    vals = []
    for sd in range(seeds):
        rng = np.random.default_rng(100 + sd)
        for _, t in T.iterrows():
            cand = byday.get(I["day"][int(t.bar)])
            if cand is None or not len(cand):
                continue
            f = int(rng.choice(cand))
            vals.append(div_trade(I, f, int(t.side), float(t.dist), P)[1])
    return float(np.mean(vals)) if vals else np.nan


def div_stats(T):
    if not len(T):
        return dict(n=0)
    r = T.r.to_numpy()
    gp, gl = r[r > 0].sum(), -r[r < 0].sum()
    L, S = T[T.side == 1], T[T.side == -1]
    return dict(n=len(T), win=T.win.mean() * 100, winL=L.win.mean() * 100 if len(L) else np.nan,
                winS=S.win.mean() * 100 if len(S) else np.nan, nL=len(L), nS=len(S),
                tp2=(T.out == "TP2").mean() * 100, sl=(T.out == "SL").mean() * 100, to=(T.out == "T").mean() * 100,
                exp=r.mean(), usd=T.usd.mean(), pf=gp / gl if gl > 0 else np.nan, stop=T.dist.mean())


def div_f(x, fmt="{:.1f}"):
    return "-" if x is None or (isinstance(x, float) and np.isnan(x)) else fmt.format(x)


def div_main():
    test = os.getenv("TEST", "") == "1"
    end = datetime.now(timezone.utc) - timedelta(days=1)
    start = datetime.fromisoformat(START).replace(tzinfo=timezone.utc)
    if test:
        start = datetime(2025, 6, 1, tzinfo=timezone.utc)
    os.makedirs(OUT, exist_ok=True)
    t0 = time.time()
    split_year = int(SPLIT[:4])
    P0 = dict(DIV_DEF)
    sweep = []
    for trig in ("turn", "div"):
        for mg in (1, 2, 3):
            for pvR in (1, 2, 3):
                for sl in ("swing", "atr"):
                    for arm in (3, 6, 10):
                        sweep.append(dict(P0, trig=trig, min_grade=mg, pvR=pvR, sl=sl, arm=arm))
    A, ALLT, SW = [], [], []
    for sym in SYMBOLS:
        print(f"\n=== {sym} ===", flush=True)
        df1 = fake_1m(sym, start, end)[0] if test else fetch_1m(sym, start, end)[0]
        days = df1.index.normalize().nunique()
        for tf in TFS:
            df = to_tf(df1, rth_only=False, mins=tf)
            I = div_ind(df)
            T = div_run(I, P0)
            rnd = div_random(I, T, P0)
            st = div_stats(T)
            A.append(dict(sym=sym, tf=tf, days=days, rnd=rnd, **st))
            if len(T):
                ALLT.append(T.assign(sym=sym, tf=tf))
            print(f"  {sym} {tf}m defaults: {st.get('n', 0)} fires, win {div_f(st.get('win'))}%, "
                  f"exp {div_f(st.get('exp'), '{:+.3f}')} ATR, random {div_f(rnd, '{:+.3f}')}", flush=True)
            ev_cache = {}
            for P in sweep:
                key = P["pvR"]
                if key not in ev_cache:
                    ev_cache[key] = div_events(I, P)
                Ts = div_run(I, P, ev_cache[key])
                tr, te = (Ts[Ts.year < split_year], Ts[Ts.year >= split_year]) if len(Ts) else (Ts, Ts)
                SW.append(dict(sym=sym, tf=tf, trig=P["trig"], mg=P["min_grade"], pvR=P["pvR"], sl=P["sl"], arm=P["arm"],
                               tr=div_stats(tr), te=div_stats(te), all=div_stats(Ts)))
    TT = pd.concat(ALLT) if ALLT else pd.DataFrame()

    md = ["# DIV PRO backtest", "",
          f"{', '.join(SYMBOLS)} | charts {', '.join(str(t) + 'm' for t in TFS)} | {START} to {end:%Y-%m-%d} | "
          f"TRAIN before {SPLIT[:4]}, TEST {SPLIT[:4]}-now. Win = TP1 before the stop (timeouts count as losses). "
          "R is in ATR per trade: half off at TP1, rest at TP2 / original stop / time. No slippage. DATA ONLY.", "",
          "## A) DIV PRO defaults (turn candle, min grade 2, 5/2 swings, swing stop, TP1 1x / TP2 2x ATR)", "",
          "| Ticker | Chart | Fires | Per day | Win % | Long win % (n) | Short win % (n) | TP2 % | Full stop % | Timeout % | "
          "Exp ATR | Exp $/share | Profit factor | Avg stop ATR | Random exp ATR | Edge vs random |",
          "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in A:
        if not r.get("n"):
            md.append(f"| {r['sym']} | {r['tf']}m | 0 | | | | | | | | | | | | | |")
            continue
        edge = r["exp"] - r["rnd"] if not np.isnan(r["rnd"]) else np.nan
        md.append(f"| {r['sym']} | {r['tf']}m | {r['n']} | {r['n'] / max(r['days'], 1):.2f} | {r['win']:.1f} | "
                  f"{div_f(r['winL'])} ({r['nL']}) | {div_f(r['winS'])} ({r['nS']}) | {r['tp2']:.1f} | {r['sl']:.1f} | {r['to']:.1f} | "
                  f"**{r['exp']:+.3f}** | {r['usd']:+.3f} | {div_f(r['pf'], '{:.2f}')} | {r['stop']:.2f} | "
                  f"{div_f(r['rnd'], '{:+.3f}')} | {div_f(edge, '{:+.3f}')} |")

    if len(TT):
        def block(title, col, labels=None):
            out = ["", title, "", "| " + col + " | Fires | Win % | Long win % | Short win % | TP2 % | Exp ATR | Exp $/share |",
                   "|---|---|---|---|---|---|---|---|"]
            for k, g in TT.groupby(col):
                s = div_stats(g)
                out.append(f"| {labels(k) if labels else k} | {s['n']} | {s['win']:.1f} | {div_f(s['winL'])} | {div_f(s['winS'])} | "
                           f"{s['tp2']:.1f} | **{s['exp']:+.3f}** | {s['usd']:+.3f} |")
            return out
        md += block("## B) Defaults year by year (all tickers and charts together)", "year", lambda k: str(k))
        md += block("## C) By grade at the fire (G2 = 2 points ... G4 = all 3 oscillators + Vix Fix maxed)", "grade",
                    lambda k: f"G{k}")
        TT["hour"] = TT.hm // 100
        md += block("## D) By hour of the fire (ET)", "hour", lambda k: f"{k}:00")
        md += block("## E) Long vs short", "side", lambda k: "LONG" if k == 1 else "SHORT")

    md += ["", "## F) Settings sweep - picked on TRAIN, checked on TEST",
           "Each row is one setting on one ticker + chart. Ranked by TRAIN expectancy (min 60 TRAIN fires). "
           "A setting is only real if TEST (never used to pick) stays positive.", "",
           "| Ticker | Chart | Fire on | Min grade | Swing right bars | Stop | Armed bars | TRAIN fires | TRAIN win % | TRAIN exp | "
           "TEST fires | TEST win % | TEST exp | TEST $/share |", "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    rows = [s for s in SW if s["tr"].get("n", 0) >= 60]
    rows.sort(key=lambda s: -s["tr"]["exp"])
    for s in rows[:25]:
        tr, te = s["tr"], s["te"]
        md.append(f"| {s['sym']} | {s['tf']}m | {'turn candle' if s['trig'] == 'turn' else 'DIV itself'} | {s['mg']} | {s['pvR']} | "
                  f"{s['sl']} | {s['arm']} | {tr['n']} | {tr['win']:.1f} | {tr['exp']:+.3f} | {te.get('n', 0)} | "
                  f"{div_f(te.get('win'))} | **{div_f(te.get('exp'), '{:+.3f}')}** | {div_f(te.get('usd'), '{:+.3f}')} |")
    both = [s for s in rows if s["te"].get("n", 0) >= 30 and s["te"]["exp"] > 0]
    md += ["", f"Settings positive on BOTH halves (TEST 30+ fires): **{len(both)} of {len(rows)}** with 60+ TRAIN fires."]

    # one line per chart: the best TRAIN setting and what it did on TEST
    md += ["", "## G) Best TRAIN setting per ticker + chart, and its TEST result", "",
           "| Ticker | Chart | Setting | TRAIN exp (n) | TEST exp (n) | TEST win % |", "|---|---|---|---|---|---|"]
    for (sym, tf), grp in pd.DataFrame([dict(sym=s["sym"], tf=s["tf"], s=s) for s in rows]).groupby(["sym", "tf"]) \
            if rows else []:
        s = max(grp.s, key=lambda z: z["tr"]["exp"])
        tr, te = s["tr"], s["te"]
        md.append(f"| {sym} | {tf}m | {'turn' if s['trig'] == 'turn' else 'DIV'} / G{s['mg']} / R{s['pvR']} / {s['sl']} / arm {s['arm']} | "
                  f"{tr['exp']:+.3f} ({tr['n']}) | **{div_f(te.get('exp'), '{:+.3f}')}** ({te.get('n', 0)}) | {div_f(te.get('win'))} |")
    md += ["", f"Runtime {(time.time() - t0) / 60:.1f} min. This is math/data, not financial advice."]
    txt = "\n".join(md)
    stamp = datetime.now(NY).strftime("%Y-%m-%d")
    for fn in (f"div_{stamp}.md", "div_latest.md"):
        with open(os.path.join(OUT, fn), "w") as fh:
            fh.write(txt)
    if len(TT):
        TT.to_csv(os.path.join(OUT, "div_trades.csv"), index=False)
    print(txt[:6000])
    print(f"\nSaved {OUT}/div_latest.md")


import os as _os, sys as _sys, runpy as _runpy
if __name__ == "__main__" and _os.getenv("MODE", "").strip().lower() in ("", "div"):
    _runpy.run_path(__file__, run_name="div_lib")["div_main"]()
    _sys.exit(0)
