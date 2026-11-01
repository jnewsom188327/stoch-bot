def ang23_main():
    """ANGLE FLATTENS THROUGH 23 - 2026 only, real option prices. A steep trend line (EMA 13 angle over 5 candles) flattens back
    through 23 deg: long when it drops from above +23 to +23 or under, short when it rises from under -23 to -23 or over.
    Same signal as the Edge Finder. Contracts: your $0.45-1.00 (closest to $0.70) 0DTE, ATM 0DTE, 2 ITM 0DTE, 2 ITM 1DTE.
    Exits: angle back -20, line color, 15 / 30 min, option +20/-10, lock +10 then trail 10, lock +20 then breakeven.
    Plus every reading (Vix Fix, TTM, squeeze, VWAP, volume, line color, DIV, 15m trend, hour) for the best trade."""
    test = os.getenv("TEST", "") == "1"
    end = datetime.now(timezone.utc) - timedelta(days=1)
    start = datetime(2025, 12, 1, tzinfo=timezone.utc)                # December = warm-up only
    os.makedirs(OUT, exist_ok=True)
    t0 = time.time()
    H1_END = pd.Timestamp("2026-07-01").date()                        # first half = Jan-Jun, second half = Jul-now
    CAP = 90
    OPTS = ["$0.45-1.00 0DTE", "ATM 0DTE", "2 ITM 0DTE", "2 ITM 1DTE"]
    EXITS = ["ANGLE BACK -20", "LINE COLOR", "15 MINUTES", "30 MINUTES", "OPTION +20% / -10%",
             "LOCK +10% THEN TRAIL 10 (stop -20%)", "LOCK +20% THEN BREAKEVEN (stop -30%)"]
    oc = None
    if not test:
        from alpaca.data.historical import OptionHistoricalDataClient
        oc = OptionHistoricalDataClient(os.getenv("ALPACA_KEY", "").strip(), os.getenv("ALPACA_SECRET", "").strip())
    rows = []
    rng = np.random.default_rng(23)
    for sym in [s for s in SYMBOLS if s in ("SPY", "QQQ", "IWM")]:
        print(f"\n=== {sym} ===", flush=True)
        df1 = fake_1m(sym, start, end)[0] if test else fetch_1m(sym, start, end)[0]
        t1 = df1.index
        mod1 = (t1.hour * 60 + t1.minute).to_numpy() - 570
        rth = (mod1 >= 0) & (mod1 < 390)
        d1 = np.asarray(t1.date)
        spot = {}
        for d_, ix in pd.Series(np.nonzero(rth)[0]).groupby(d1[rth]):
            a = np.full(390, np.nan)
            ii = ix.to_numpy()
            a[mod1[ii]] = df1["close"].to_numpy()[ii]
            spot[d_] = pd.Series(a).ffill().bfill().to_numpy()
        days_sorted = sorted(spot)
        nxt_day = {d_: (days_sorted[i + 1] if i + 1 < len(days_sorted) else None) for i, d_ in enumerate(days_sorted)}
        TR = []                                                        # (day, tf, side, kind, buy_min, exit minutes dict, readings)
        for tf in TFS:
            df = to_tf(df1, rth_only=False, mins=tf)
            ind = indicators(df, 13, 34, True)
            n = len(df)
            ts = df.index
            hm, day = ind["hm"], ind["day"]
            ang = np.nan_to_num(ang_series(df, ind, 5))
            col, _ = tlt_colors(df, ind)
            F, G = vfx_pane(df)
            F, G = np.nan_to_num(F), np.nan_to_num(G)
            cs = df["close"]
            mid = ((df["high"].rolling(20).max() + df["low"].rolling(20).min()) / 2 + cs.rolling(20).mean()) / 2
            mom = np.nan_to_num(linreg_last((cs - mid).to_numpy(), 20))
            dev = 2 * cs.rolling(20).std(ddof=0)
            trr = pd.concat([df["high"] - df["low"], (df["high"] - cs.shift(1)).abs(), (df["low"] - cs.shift(1)).abs()], axis=1).max(axis=1)
            sqz = (dev < 1.5 * trr.ewm(alpha=1 / 20, adjust=False).mean()).to_numpy()
            vol = df["volume"].to_numpy()
            vavg = df["volume"].rolling(20).mean().shift(1).to_numpy()
            DI = div_ind(df)
            EV = div_events(DI, DIV_DEF)
            divL, divS = np.zeros(n, bool), np.zeros(n, bool)
            for b, _, _ in EV[1]:
                divL[b:min(b + 10, n)] = True
            for b, _, _ in EV[-1]:
                divS[b:min(b + 10, n)] = True
            close_t = ts + pd.Timedelta(minutes=tf)
            mend = ((close_t.hour * 60 + close_t.minute).to_numpy() - 570)  # minute index the candle closes on
            same = np.r_[False, day[1:] == day[:-1]]
            prev = np.r_[np.nan, ang[:-1]]
            L = (prev > 23) & (ang <= 23) & same
            S = (prev < -23) & (ang >= -23) & same
            win = (hm >= 930) & (mend - 1 >= 5) & (mend - 1 <= 315) & (np.asarray([d_.year for d_ in day]) >= 2026)
            nxL_ang, nxS_ang = angs_next_true(ang < -20), angs_next_true(ang > 20)
            nxL_col, nxS_col = angs_next_true(col <= -1), angs_next_true(col >= 1)

            def add(i, sd, kind):
                mb = int(mend[i] - 1)
                cap = min(mb + CAP, 385)
                ex = {}
                for name, arr in (("ANGLE BACK -20", nxL_ang if sd == 1 else nxS_ang), ("LINE COLOR", nxL_col if sd == 1 else nxS_col)):
                    j = arr[min(i + 1, n - 1)] if i + 1 < n else n
                    ex[name] = int(min(mend[j] - 1, cap)) if (j < n and day[j] == day[i] and mend[j] - 1 > mb) else cap
                ex["15 MINUTES"], ex["30 MINUTES"] = min(mb + 15, cap), min(mb + 30, cap)
                rd = {"Vix Fix your side 85+ (greed longs / fear shorts)": (G[i] if sd == 1 else F[i]) >= 85,
                      "Vix Fix other side 85+ (fear longs / greed shorts)": (F[i] if sd == 1 else G[i]) >= 85,
                      "TTM momentum on your side of zero": mom[i] * sd > 0,
                      "TTM momentum rising your way": (mom[i] - mom[i - 1]) * sd > 0,
                      "Squeeze ON": bool(sqz[i]),
                      "Price on your side of VWAP": (ind["c"][i] - ind["vwap"][i]) * sd > 0,
                      "Volume 1.5x+ the 20-candle average": vavg[i] > 0 and vol[i] >= 1.5 * vavg[i],
                      "Trend line still your STRONG color": col[i] * sd == 2,
                      "DIV your way in the last 10 candles": bool(divL[i] if sd == 1 else divS[i]),
                      "15m trend your way": ind["h1"][i] == sd,
                      "60m trend your way": ind["h2"][i] == sd}
                TR.append((day[i], tf, sd, kind, mb, cap, ex, rd, int(hm[i] // 100)))
            for i in np.nonzero(L & win)[0]:
                add(i, 1, "fire")
            for i in np.nonzero(S & win)[0]:
                add(i, -1, "fire")
            okr = np.nonzero(win & same)[0]
            nf = int((L & win).sum() + (S & win).sum())
            if len(okr) and nf:
                for i in rng.choice(okr, min(len(okr), 3 * nf), replace=False):
                    add(int(i), 1 if rng.random() < 0.5 else -1, "random")
            print(f"  {sym} {tf}m: {nf} angle-flatten fires in 2026", flush=True)
        byday = {}
        for t in TR:
            byday.setdefault(t[0], []).append(t)
        for k, (d_, tl) in enumerate(sorted(byday.items())):
            sp = spot.get(d_)
            if sp is None:
                continue
            lo, hi = np.nanmin(sp), np.nanmax(sp)
            k0 = np.arange(np.floor(lo) - 8, np.ceil(hi) + 9, 1.0)
            k1 = np.arange(np.floor(lo) - 4, np.ceil(hi) + 5, 1.0)
            d1x = nxt_day.get(d_)
            cons = [lab_occ(sym, d_, cp, s_) for s_ in k0 for cp in ("C", "P")]
            if d1x is not None:
                cons += [lab_occ(sym, d1x, cp, s_) for s_ in k1 for cp in ("C", "P")]
            if test:
                px = lab_fake_opt([c for c in cons if c[3:9] == f"{d_:%y%m%d}"], d_, {sym: sp})
                if d1x is not None:
                    px.update(lab_fake_opt([c for c in cons if c[3:9] == f"{d1x:%y%m%d}"], d_, {sym: sp}))
            else:
                px = div_lock_fetch(oc, cons, d_)
            if k % 20 == 0:
                print(f"  {sym} {d_}: {len(px)} contracts with prices ({k + 1}/{len(byday)} days)", flush=True)
            for (_, tf, sd, kind, mb, cap, ex, rd, hr) in tl:
                cp = "C" if sd == 1 else "P"
                s0 = sp[mb]
                atm = float(np.round(s0))
                picks = {}
                best, bk = None, None
                for s_ in k0:
                    c = lab_occ(sym, d_, cp, s_)
                    arr = px.get(c)
                    if arr is None or np.isnan(arr[mb]) or not (0.45 <= arr[mb] <= 1.00):
                        continue
                    if best is None or abs(arr[mb] - 0.70) < abs(best - 0.70):
                        best, bk = arr[mb], c
                picks["$0.45-1.00 0DTE"] = bk
                picks["ATM 0DTE"] = lab_occ(sym, d_, cp, atm)
                picks["2 ITM 0DTE"] = lab_occ(sym, d_, cp, atm - 2 * sd)
                picks["2 ITM 1DTE"] = lab_occ(sym, d1x, cp, atm - 2 * sd) if d1x is not None else None
                for on, c in picks.items():
                    arr = px.get(c) if c else None
                    if arr is None or np.isnan(arr[mb]) or arr[mb] < 0.05:
                        continue
                    path = pd.Series(arr[mb:cap + 1]).ffill().to_numpy()
                    p0 = arr[mb]
                    cost = lambda p: max(0.01, 0.005 * p)
                    ent = p0 + cost(p0)
                    g = np.array([(p - cost(p)) / ent - 1 for p in path])
                    gg = g[1:] if len(g) > 1 else g
                    res = {}
                    for name in ("ANGLE BACK -20", "LINE COLOR", "15 MINUTES", "30 MINUTES"):
                        res[name] = float(g[min(ex[name] - mb, len(g) - 1)])
                    r = gg[-1]
                    for x in gg:
                        if x <= -0.10:
                            r = x
                            break
                        if x >= 0.20:
                            r = x
                            break
                    res["OPTION +20% / -10%"] = float(r)
                    res["LOCK +10% THEN TRAIL 10 (stop -20%)"] = div_trail_sim(gg, 10, 20, "trail10", 0.0)
                    res["LOCK +20% THEN BREAKEVEN (stop -30%)"] = div_trail_sim(gg, 20, 30, "BE", 0.0)
                    rec = dict(sym=sym, tf=tf, side=sd, kind=kind, opt=on, half=1 if d_ < H1_END else 2, hour=hr, entry=p0,
                               peak=float(gg.max()), **{f"x:{kk}": v for kk, v in res.items()}, **{f"r:{kk}": bool(v) for kk, v in rd.items()})
                    rows.append(rec)
    R = pd.DataFrame(rows)
    md = ["# ANGLE FLATTENS THROUGH 23 - 2026 only, real option prices", "",
          f"SPY + QQQ | charts {', '.join(str(t) + 'm' for t in TFS)} | Jan 1 2026 to {end:%Y-%m-%d}. Signal: the trend line (EMA 13) angle over "
          "5 candles was steeper than 23 deg and flattens back through 23 = LONG (mirror under -23 = SHORT). It buys the PAUSE in a strong "
          "run (with the trend). Buy at the 1-minute close when the signal candle closes (+ max(1c, 0.5%)), sell at 1-minute closes (- the same). "
          "Signals 9:35-2:45, out by 3:55, 90 min max. Half 1 = Jan-Jun, half 2 = Jul-now. Random = 3 random candles per fire (random side). "
          "Real Alpaca option prices. DATA ONLY.", ""]
    if not len(R):
        md.append("No trades - no option prices came back.")
    else:
        F_, RN = R[R.kind == "fire"], R[R.kind == "random"]
        nf = F_.groupby("opt").size().max()
        md += [f"Fires with an option price: about {nf} per contract type ({nf / max(len(set(zip(R.sym, R.half))), 1):.0f} per ticker-half).", "",
               "## A) Every contract x exit - avg % on the premium per trade (all charts)", "",
               "| Contract | Exit | Trades | Win % | **Avg %** | Half 1 / Half 2 | Random same trade | Edge vs random |",
               "|---|---|---|---|---|---|---|---|"]
        cells = []
        for on in OPTS:
            for xn in EXITS:
                f_ = F_[F_.opt == on][f"x:{xn}"] * 100
                if not len(f_):
                    continue
                h1 = F_[(F_.opt == on) & (F_.half == 1)][f"x:{xn}"].mean() * 100
                h2 = F_[(F_.opt == on) & (F_.half == 2)][f"x:{xn}"].mean() * 100
                rn = RN[RN.opt == on][f"x:{xn}"].mean() * 100
                cells.append((on, xn, len(f_), (f_ > 0).mean() * 100, f_.mean(), h1, h2, rn))
                md.append(f"| {on} | {xn} | {len(f_)} | {(f_ > 0).mean() * 100:.0f}% | **{f_.mean():+.1f}%** | {h1:+.1f}% / {h2:+.1f}% | "
                          f"{rn:+.1f}% | {f_.mean() - rn:+.1f} |")
        good = [c for c in cells if c[2] >= 40]
        bc = max(good, key=lambda c: c[5]) if good else max(cells, key=lambda c: c[4])
        on, xn = bc[0], bc[1]
        G_ = F_[F_.opt == on]
        col_ = f"x:{xn}"
        md += ["", f"**Picked on half 1 (Jan-Jun): {on} / {xn}** -> half 1 {bc[5]:+.1f}%, half 2 (never used to pick) **{bc[6]:+.1f}%**.", "",
               f"## B) That trade by chart, side and hour", "", "| Group | Trades | Win % | Avg % | Half 1 | Half 2 |", "|---|---|---|---|---|---|"]

        def rowB(name, g):
            x = g[col_] * 100
            return (f"| {name} | {len(g)} | {(x > 0).mean() * 100:.0f}% | **{x.mean():+.1f}%** | "
                    f"{(g[g.half == 1][col_].mean() * 100):+.1f}% | {(g[g.half == 2][col_].mean() * 100):+.1f}% |")
        md.append(rowB("**ALL**", G_))
        md.append(rowB("Random", RN[RN.opt == on]))
        for (s_, tf), g in G_.groupby(["sym", "tf"]):
            md.append(rowB(f"{s_} {tf}m", g))
        for k_, g in G_.groupby("side"):
            md.append(rowB("LONG (calls)" if k_ == 1 else "SHORT (puts)", g))
        for k_, g in G_.groupby("hour"):
            md.append(rowB(f"{k_}:00", g))
        md += ["", "## C) Which readings help? (same trade, YES vs NO at the signal candle)", "",
               "A reading only counts if YES beats NO in BOTH halves.", "",
               "| Reading | YES trades | YES avg | NO avg | YES half 1 / half 2 | Helps both halves? |", "|---|---|---|---|---|---|"]
        for rc in [c for c in G_.columns if c.startswith("r:")]:
            y, nn = G_[G_[rc]], G_[~G_[rc]]
            if len(y) < 15 or len(nn) < 15:
                continue
            y1, y2 = y[y.half == 1][col_].mean() * 100, y[y.half == 2][col_].mean() * 100
            n1, n2 = nn[nn.half == 1][col_].mean() * 100, nn[nn.half == 2][col_].mean() * 100
            both = (y1 > n1) and (y2 > n2)
            md.append(f"| {rc[2:]} | {len(y)} | **{y[col_].mean() * 100:+.1f}%** | {nn[col_].mean() * 100:+.1f}% | "
                      f"{y1:+.1f}% / {y2:+.1f}% | {'YES' if both else 'no'} |")
        R.to_csv(os.path.join(OUT, "ang23_trades.csv"), index=False)
    md += ["", f"Runtime {(time.time() - t0) / 60:.1f} min. This is math/data, not financial advice."]
    txt = "\n".join(md)
    with open(os.path.join(OUT, "ang23_latest.md"), "w") as fh:
        fh.write(txt)
    print(txt[:6000])
    print(f"\nSaved {OUT}/ang23_latest.md")

import os as _os, sys as _sys
if __name__ == "__main__" and _os.getenv("MODE", "").strip().lower() in ("", "div"):
    import subprocess, urllib.request
    _src = urllib.request.urlopen("https://raw.githubusercontent.com/jnewsom188327/stoch-bot/"
                                  "8ee9cb69b57225c37516d63dd5af2fc6798acea4/backtest.py", timeout=120).read().decode()
    _me = open(__file__).read()
    _blk = _me[:_me.index("import os as _os, sys as _sys")]
    _old = 'if __name__ == "__main__" and os.getenv("MODE", "").strip().lower() in ("", "div"):\n    div_trail_main()\n    sys.exit(0)\n'
    if _old not in _src:
        _sys.exit("Could not find the old DIV run lines in the saved backtest.py - nothing changed.")
    _new = _src.replace(_old, _blk + 'if __name__ == "__main__" and os.getenv("MODE", "").strip().lower() in ("", "div"):\n'
                        "    ang23_main()\n    sys.exit(0)\n")
    with open(__file__, "w") as _f:
        _f.write(_new)
    subprocess.run(["git", "add", __file__])
    print("Restored the full backtest.py with the 2026 ANGLE FLATTENS options test added.", flush=True)
    _g = {"__name__": "div_lib", "__file__": __file__}
    exec(compile(_new, __file__, "exec"), _g)
    _g["ang23_main"]()
    _sys.exit(0)
