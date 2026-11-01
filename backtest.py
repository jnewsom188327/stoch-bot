def heat_main():
    """2026, 10:00-3:00, SPY + QQQ: every candle scanned for the 'dip in a trend' agreements (and the angle fire), traded with the
    REAL 0DTE option priced $0.45-1.00 (closest to $0.70). Measures +10% BEFORE -20% (first touch on 1-minute closes) and real plans."""
    test = os.getenv("TEST", "") == "1"
    end = datetime.now(timezone.utc) - timedelta(days=1)
    start = datetime(2025, 12, 1, tzinfo=timezone.utc)
    os.makedirs(OUT, exist_ok=True)
    t0 = time.time()
    H1_END = pd.Timestamp("2026-07-01").date()
    HOLD, COOL = 60, 10
    SETUPS = {
        "A": "15m trend your way + price on the OTHER side of VWAP + your Vix Fix side under 85",
        "B": "15m trend your way + price on the OTHER side of VWAP",
        "C": "60m trend your way + price on the OTHER side of VWAP + your Vix Fix side under 85",
        "D": "15m AND 60m trend your way + price on the OTHER side of VWAP + your Vix Fix side under 85",
        "E": "ANGLE FLATTENS 23 + neither Vix Fix side 85+",
        "T": "BASELINE: random candle, side = the 15m trend",
        "R": "BASELINE: random candle, random side",
    }
    oc = None
    if not test:
        from alpaca.data.historical import OptionHistoricalDataClient
        oc = OptionHistoricalDataClient(os.getenv("ALPACA_KEY", "").strip(), os.getenv("ALPACA_SECRET", "").strip())
    rows, ndays = [], 0
    rng = np.random.default_rng(10)
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
        ndays = max(ndays, sum(1 for d_ in spot if d_.year >= 2026))
        TR = []
        for tf in TFS:
            df = to_tf(df1, rth_only=False, mins=tf)
            ind = indicators(df, 13, 34, True)
            n = len(df)
            ts = df.index
            hm, day = ind["hm"], ind["day"]
            c, vw, h1, h2 = ind["c"], ind["vwap"], ind["h1"], ind["h2"]
            F, G = vfx_pane(df)
            F, G = np.nan_to_num(F), np.nan_to_num(G)
            ang = np.nan_to_num(ang_series(df, ind, 5))
            close_t = ts + pd.Timedelta(minutes=tf)
            mend = (close_t.hour * 60 + close_t.minute).to_numpy() - 570
            same = np.r_[False, day[1:] == day[:-1]]
            win = same & (mend - 1 >= 30) & (mend - 1 <= 330) & (np.asarray([d_.year for d_ in day]) >= 2026)
            prev = np.r_[np.nan, ang[:-1]]
            conds = {}
            for sd in (1, -1):
                yourF = G if sd == 1 else F
                othF = F if sd == 1 else G
                other_vwap = (c - vw) * sd < 0
                conds[("A", sd)] = (h1 == sd) & other_vwap & (yourF < 85)
                conds[("B", sd)] = (h1 == sd) & other_vwap
                conds[("C", sd)] = (h2 == sd) & other_vwap & (yourF < 85)
                conds[("D", sd)] = (h1 == sd) & (h2 == sd) & other_vwap & (yourF < 85)
                flat = ((prev > 23) & (ang <= 23)) if sd == 1 else ((prev < -23) & (ang >= -23))
                conds[("E", sd)] = flat & (yourF < 85) & (othF < 85)
            for (k_, sd), m in conds.items():
                m = m & win
                edge = m & ~np.r_[False, m[:-1]] if k_ != "E" else m          # first candle of each stretch
                last = -10 ** 9
                cnt = 0
                for i in np.nonzero(edge)[0]:
                    mb = int(mend[i] - 1)
                    t_abs = i * tf
                    if t_abs - last < COOL:
                        continue
                    last = t_abs
                    TR.append((day[i], tf, sd, k_, mb, int(hm[i] // 100)))
                    cnt += 1
            okr = np.nonzero(win)[0]
            nA = sum(1 for t in TR if t[1] == tf and t[3] == "A")
            for i in rng.choice(okr, min(len(okr), max(nA, 50)), replace=False) if len(okr) else []:
                TR.append((day[i], tf, int(h1[i]) if h1[i] != 0 else 1, "T", int(mend[i] - 1), int(hm[i] // 100)))
                TR.append((day[i], tf, 1 if rng.random() < 0.5 else -1, "R", int(mend[i] - 1), int(hm[i] // 100)))
            print(f"  {sym} {tf}m: " + ", ".join(f"{k_} {sum(1 for t in TR if t[1] == tf and t[3] == k_)}" for k_ in "ABCDE"), flush=True)
        byday = {}
        for t in TR:
            byday.setdefault(t[0], []).append(t)
        for k, (d_, tl) in enumerate(sorted(byday.items())):
            sp = spot.get(d_)
            if sp is None:
                continue
            lo, hi = np.nanmin(sp), np.nanmax(sp)
            strikes = np.arange(np.floor(lo) - 8, np.ceil(hi) + 9, 1.0)
            cons = [lab_occ(sym, d_, cp, s_) for s_ in strikes for cp in ("C", "P")]
            px = lab_fake_opt(cons, d_, {sym: sp}) if test else div_lock_fetch(oc, cons, d_)
            if k % 20 == 0:
                print(f"  {sym} {d_}: {len(px)} contracts with prices ({k + 1}/{len(byday)} days)", flush=True)
            for (_, tf, sd, k_, mb, hr) in tl:
                cp = "C" if sd == 1 else "P"
                best, bk = None, None
                for s_ in strikes:
                    cc = lab_occ(sym, d_, cp, s_)
                    arr = px.get(cc)
                    if arr is None or np.isnan(arr[mb]) or not (0.45 <= arr[mb] <= 1.00):
                        continue
                    if best is None or abs(arr[mb] - 0.70) < abs(best - 0.70):
                        best, bk = arr[mb], cc
                if bk is None:
                    continue
                path = pd.Series(px[bk][mb + 1:min(mb + 1 + HOLD, 386)]).ffill().to_numpy()
                if not len(path) or np.isnan(path).all():
                    continue
                path = pd.Series(path).bfill().to_numpy()
                cost = lambda p: max(0.01, 0.005 * p)
                ent = best + cost(best)
                g = np.array([(p - cost(p)) / ent - 1 for p in path])

                def first(cond):
                    w = np.nonzero(cond)[0]
                    return int(w[0]) if len(w) else 10 ** 6
                u10, u15, u20 = first(g >= 0.10), first(g >= 0.15), first(g >= 0.20)
                d20, d30 = first(g <= -0.20), first(g <= -0.30)

                def bracket(tp, sl):
                    u, d = first(g >= tp), first(g <= -sl)
                    if u == d == 10 ** 6:
                        return float(g[-1])
                    return float(g[u]) if u < d else float(g[d])
                heat = {L: (float(min(0.0, g[:u].min())) if u > 0 else 0.0) if u < 10 ** 6 else np.nan
                        for L, u in ((10, u10), (15, u15), (20, u20))}
                rows.append(dict(heat10=heat[10], heat15=heat[15], heat20=heat[20], u15=u15 if u15 < 10 ** 6 else np.nan,
                                 u20=u20 if u20 < 10 ** 6 else np.nan, end=float(g[-1]),
                                 sym=sym, tf=tf, side=sd, setup=k_, hour=hr, half=1 if d_ < H1_END else 2, entry=best,
                                 hit10=u10 < 10 ** 6, b10_20=u10 < d20, b10_30=u10 < d30, b15_20=u15 < d20, b20_30=u20 < d30,
                                 min10=u10 if u10 < 10 ** 6 else np.nan, peak=float(g.max()), trough=float(g.min()),
                                 p10_20=bracket(0.10, 0.20), p15_20=bracket(0.15, 0.20), p20_30=bracket(0.20, 0.30),
                                 lock=div_trail_sim(g, 10, 20, "trail10", 0.0), m30=float(g[min(29, len(g) - 1)])))
    R = pd.DataFrame(rows)
    md = ["# NO STOP - time and HEAT to +10% / +15% / +20% - every setup, 10:00-3:00, 2026, real 0DTE options $0.45-1.00", "",
          f"SPY + QQQ | charts {', '.join(str(t) + 'm' for t in TFS)} | Jan 1 2026 to {end:%Y-%m-%d} ({ndays} trading days). Same fires as the dip test. "
          f"NO STOP: each option is watched up to {HOLD} minutes (or 3:55) on 1-minute closes after the fill (+/- max(1c, 0.5%)). "
          "HEAT = how far the option was DOWN (worst close) before it first reached the target. Heat 0% = it never went red first. "
          "Half 1 = Jan-Jun, half 2 = Jul-now. DATA ONLY.", "",
          "Setups:"] + [f"- **{k_}** = {v}" for k_, v in SETUPS.items()] + [""]
    if not len(R):
        md.append("No trades - no option prices came back.")
    else:
        def pc(x):
            return f"{x * 100:.0f}%"

        def q(x, p):
            x = x.dropna()
            return x.quantile(p) if len(x) else np.nan
        md += ["## A) Reaching +10% with NO stop", "",
               "| Setup | Trades | Fires/day | Reached +10% | Half 1 / Half 2 | Within 2 min | 5 min | 10 min | 30 min | Median min | "
               "Never got there: avg end |", "|---|---|---|---|---|---|---|---|---|---|---|"]
        for k_ in SETUPS:
            g = R[R.setup == k_]
            if not len(g):
                continue
            m = g.min10 + 1
            fpd = len(g) / max(ndays, 1) if k_ not in ("T", "R") else np.nan
            nev = g[~g.hit10]
            md.append(f"| **{k_}** | {len(g)} | {div_f(fpd, '{:.1f}')} | **{pc(g.hit10.mean())}** | {pc(g[g.half == 1].hit10.mean())} / "
                      f"{pc(g[g.half == 2].hit10.mean())} | {pc((m <= 2).mean())} | {pc((m <= 5).mean())} | {pc((m <= 10).mean())} | "
                      f"{pc((m <= 30).mean())} | {m.median():.0f} | {nev.end.mean() * 100:+.0f}% |")
        md += ["", "## B) HEAT before +10% (only the trades that got there) - how far down it went first", "",
               "| Setup | Got +10% | Never red first | Heat under 10% | under 20% | under 30% | under 50% | Median heat | 75% of trades | 90% of trades |",
               "|---|---|---|---|---|---|---|---|---|---|"]
        for k_ in SETUPS:
            g = R[(R.setup == k_) & R.hit10]
            if not len(g):
                continue
            h = -g.heat10
            md.append(f"| **{k_}** | {len(g)} | {pc((h <= 0.001).mean())} | {pc((h < 0.10).mean())} | **{pc((h < 0.20).mean())}** | "
                      f"{pc((h < 0.30).mean())} | {pc((h < 0.50).mean())} | -{h.median() * 100:.0f}% | -{q(h, .75) * 100:.0f}% | -{q(h, .90) * 100:.0f}% |")
        md += ["", "## C) Same for +15% and +20%", "",
               "| Setup | Reached +15% | Median min | Median heat | 75% heat | Reached +20% | Median min | Median heat | 75% heat |",
               "|---|---|---|---|---|---|---|---|---|"]
        for k_ in SETUPS:
            g = R[R.setup == k_]
            if not len(g):
                continue
            g15, g20 = g[g.u15.notna()], g[g.u20.notna()]
            md.append(f"| **{k_}** | {pc(len(g15) / len(g))} | {(g15.u15 + 1).median():.0f} | -{-g15.heat15.median() * 100:.0f}% | "
                      f"-{q(-g15.heat15, .75) * 100:.0f}% | {pc(len(g20) / len(g))} | {(g20.u20 + 1).median():.0f} | "
                      f"-{-g20.heat20.median() * 100:.0f}% | -{q(-g20.heat20, .75) * 100:.0f}% |")
        md += ["", "## D) What the heat says: if you hold through X% down with NO stop, how many still reach +10%?", "",
               "Each column = trades that went at least that far red BEFORE reaching +10%, and the share of those that still came back to +10%.", "",
               "| Setup | Went -10% | came back | Went -20% | came back | Went -30% | came back | Went -50% | came back |",
               "|---|---|---|---|---|---|---|---|---|"]
        for k_ in SETUPS:
            g = R[R.setup == k_]
            if not len(g):
                continue
            cells = []
            pre = np.where(g.hit10, g.heat10, g.trough)             # how far red BEFORE +10% (or at all, if it never got there)
            for d in (0.10, 0.20, 0.30, 0.50):
                went = g[pre <= -d]
                back = went[went.hit10]
                cells += [f"{len(went)}", f"**{pc(len(back) / len(went)) if len(went) else '-'}**"]
            md.append(f"| **{k_}** | " + " | ".join(cells) + " |")
        for k_ in ("A", "D", "E"):
            g = R[R.setup == k_]
            if not len(g):
                continue
            md += ["", f"## E{k_}) Setup {k_} split up (no stop)", "",
                   "| Group | Trades | Reached +10% | Median min | Median heat (got there) | 75% heat |", "|---|---|---|---|---|---|"]
            for name, gg in ([(f"{s_} {tf}m", x) for (s_, tf), x in g.groupby(["sym", "tf"])]
                             + [("CALLS" if s == 1 else "PUTS", x) for s, x in g.groupby("side")]
                             + [(f"{h}:00", x) for h, x in g.groupby("hour")]):
                hh = -gg[gg.hit10].heat10
                md.append(f"| {name} | {len(gg)} | {pc(gg.hit10.mean())} | {(gg.min10 + 1).median():.0f} | -{hh.median() * 100:.0f}% | "
                          f"-{q(hh, .75) * 100:.0f}% |")
        R.to_csv(os.path.join(OUT, "heat_trades.csv"), index=False)
    md += ["", f"Runtime {(time.time() - t0) / 60:.1f} min. This is math/data, not financial advice."]
    txt = "\n".join(md)
    with open(os.path.join(OUT, "heat_latest.md"), "w") as fh:
        fh.write(txt)
    print(txt[:6000])
    print(f"\nSaved {OUT}/heat_latest.md")

import os as _os, sys as _sys
if __name__ == "__main__" and _os.getenv("MODE", "").strip().lower() in ("", "div"):
    import subprocess, urllib.request
    _src = urllib.request.urlopen("https://raw.githubusercontent.com/jnewsom188327/stoch-bot/"
                                  "236b6643f9951025d5fde9fe747d9df41c909854/backtest.py", timeout=120).read().decode()
    _me = open(__file__).read()
    _blk = _me[:_me.index("import os as _os, sys as _sys")]
    _old = 'if __name__ == "__main__" and os.getenv("MODE", "").strip().lower() in ("", "div"):\n    dip_main()\n    sys.exit(0)\n'
    if _old not in _src:
        _sys.exit("Could not find the old run lines in the saved backtest.py - nothing changed.")
    _new = _src.replace(_old, _blk + 'if __name__ == "__main__" and os.getenv("MODE", "").strip().lower() in ("", "div"):\n'
                        "    heat_main()\n    sys.exit(0)\n")
    with open(__file__, "w") as _f:
        _f.write(_new)
    subprocess.run(["git", "add", __file__])
    print("Restored the full backtest.py with the 2026 NO-STOP HEAT test added.", flush=True)
    _g = {"__name__": "div_lib", "__file__": __file__}
    exec(compile(_new, __file__, "exec"), _g)
    _g["heat_main"]()
    _sys.exit(0)
