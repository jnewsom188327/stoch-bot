def edgebt_main():
    """EDGE (Edge Score) indicator backtest - last 5 years. Exact Pine logic: triggers E (angle flattens through 23), D (15m+60m trend,
    price across VWAP, your Vix Fix side under 85), A (15m trend, across VWAP, under 85); score 0-6; window 9:40-3:00; 10 min cooldown
    per side. STOCK moves for all 5 years; REAL 0DTE $0.45-1.00 options from Feb 2024 (Alpaca option history starts then)."""
    test = os.getenv("TEST", "") == "1"
    end = datetime.now(timezone.utc) - timedelta(days=1)
    t_start = pd.Timestamp("2021-11-01").date()
    start = datetime(2021, 10, 1, tzinfo=timezone.utc)
    opt_from = pd.Timestamp("2024-02-15").date()
    if test:
        start, t_start, opt_from = datetime(2025, 6, 1, tzinfo=timezone.utc), pd.Timestamp("2025-07-01").date(), pd.Timestamp("2026-01-01").date()
    os.makedirs(OUT, exist_ok=True)
    t0 = time.time()
    COOL, VF, VOLM, TSTOP = 10, 85.0, 1.5, 10
    POINTS = ["60m trend your way", "Your Vix Fix side under 85", "Other Vix Fix side under 85", "No volume spike",
              "TTM momentum rising your way", "No DIV your way in the last 10 candles"]
    oc = None
    if not test:
        from alpaca.data.historical import OptionHistoricalDataClient
        oc = OptionHistoricalDataClient(os.getenv("ALPACA_KEY", "").strip(), os.getenv("ALPACA_SECRET", "").strip())
    rows, days_all = [], set()
    rng = np.random.default_rng(6)
    for sym in [s for s in SYMBOLS if s in ("SPY", "QQQ", "IWM")]:
        print(f"\n=== {sym} ===", flush=True)
        df1 = fake_1m(sym, start, end)[0] if test else fetch_1m(sym, start, end)[0]
        t1 = df1.index
        o1, h1a, l1a, c1 = (df1[k].to_numpy(float) for k in ("open", "high", "low", "close"))
        d1 = np.asarray(t1.date)
        mod1 = (t1.hour * 60 + t1.minute).to_numpy() - 570
        rth = (mod1 >= 0) & (mod1 < 390)
        spot = {}
        for d_, ix in pd.Series(np.nonzero(rth)[0]).groupby(d1[rth]):
            a = np.full(390, np.nan)
            ii = ix.to_numpy()
            a[mod1[ii]] = c1[ii]
            spot[d_] = pd.Series(a).ffill().bfill().to_numpy()
        days_all |= {d_ for d_ in spot if d_ >= t_start}
        CAND = []
        for tf in TFS:
            df = to_tf(df1, rth_only=False, mins=tf)
            ind = indicators(df, 13, 34, True)
            n = len(df)
            ts = df.index
            hm, day = ind["hm"], ind["day"]
            c, vw, a_ = ind["c"], ind["vwap"], ind["atr"]
            t15, t60 = ind["h1"], ind["h2"]
            F, G = vfx_pane(df)
            F, G = np.nan_to_num(F), np.nan_to_num(G)
            ang = np.nan_to_num(ang_series(df, ind, 5))
            cs = df["close"]
            mid = ((df["high"].rolling(20).max() + df["low"].rolling(20).min()) / 2 + cs.rolling(20).mean()) / 2
            mom = np.nan_to_num(linreg_last((cs - mid).to_numpy(), 20))
            momUp = np.r_[False, mom[1:] > mom[:-1]]
            momDn = np.r_[False, mom[1:] < mom[:-1]]
            vol = df["volume"].to_numpy()
            vavg = df["volume"].rolling(20).mean().shift(1).to_numpy()
            spike = (vol >= VOLM * np.nan_to_num(vavg, nan=np.inf))
            cc = c.astype(float)
            macd = div_ema(cc, 12) - div_ema(cc, 26)
            lastB, lastS = np.full(n, -10 ** 6), np.full(n, -10 ** 6)
            for side, arr in ((1, lastB), (-1, lastS)):
                piv = div_pivots(ind["l"] if side == 1 else ind["h"], 5, 2, low=(side == 1))
                pr = ind["l"] if side == 1 else ind["h"]
                prev = None
                for cb in piv:
                    if np.isnan(macd[cb]):
                        continue
                    if prev is not None:
                        lp, lm = prev
                        if (pr[cb] < lp and macd[cb] > lm) if side == 1 else (pr[cb] > lp and macd[cb] < lm):
                            arr[cb + 2:] = cb + 2
                    prev = (pr[cb], macd[cb])
            idx = np.arange(n)
            divL, divS = (idx - lastB) <= 10, (idx - lastS) <= 10
            prv = np.r_[np.nan, ang[:-1]]
            eL, eS = (prv > 23) & (ang <= 23), (prv < -23) & (ang >= -23)
            aL, aS = (t15 == 1) & (c < vw) & (G < VF), (t15 == -1) & (c > vw) & (F < VF)
            dL, dS = aL & (t60 == 1), aS & (t60 == -1)
            sh = lambda x: np.r_[False, x[:-1]]
            aLf, aSf, dLf, dSf = aL & ~sh(aL), aS & ~sh(aS), dL & ~sh(dL), dS & ~sh(dS)
            pts = {1: [t60 == 1, G < VF, F < VF, ~spike, momUp, ~divL], -1: [t60 == -1, F < VF, G < VF, ~spike, momDn, ~divS]}
            win = (hm >= 940) & (hm < 1500) & np.asarray([d_ >= t_start for d_ in day])
            close_t = ts + pd.Timedelta(minutes=tf)
            e1 = np.searchsorted(t1.values, close_t.values)                  # first 1m bar after the candle closes
            for sd, trig in ((1, (eL, dLf, aLf)), (-1, (eS, dSf, aSf))):
                why = np.where(trig[0], "E", np.where(trig[1], "D", np.where(trig[2], "A", "")))
                P = np.vstack(pts[sd]).T.astype(int)
                for i in np.nonzero(win & (why != ""))[0]:
                    CAND.append(dict(tf=tf, i=int(i), side=sd, why=str(why[i]), score=int(P[i].sum()), pts=P[i].copy(),
                                     t=ts[i], e=int(e1[i]), atr=float(a_[i]), day=day[i], hour=int(hm[i] // 100), kind="fire"))
            okr = np.nonzero(win)[0]
            for i in rng.choice(okr, min(len(okr), 4000), replace=False) if len(okr) else []:
                CAND.append(dict(tf=tf, i=int(i), side=1 if rng.random() < 0.5 else -1, why="R", score=-1, pts=np.zeros(6, int),
                                 t=ts[i], e=int(e1[i]), atr=float(a_[i]), day=day[i], hour=int(hm[i] // 100), kind="random"))
            print(f"  {sym} {tf}m: {sum(1 for x in CAND if x['tf'] == tf and x['kind'] == 'fire')} trigger candles", flush=True)
        # cooldown per chart and side, per min-score threshold (as the indicator: only fires that pass the min score start a cooldown)
        CAND.sort(key=lambda x: (x["tf"], x["t"], -x["side"]))
        for x in CAND:
            x["sel"] = np.zeros(7, bool)
        for thr in range(7):
            last = {}
            fired_bar = set()
            for x in CAND:
                if x["kind"] != "fire" or x["score"] < thr:
                    continue
                k = (x["tf"], x["side"])
                if x["side"] == -1 and (x["tf"], x["i"]) in fired_bar:
                    continue
                if k in last and (x["t"] - last[k]).total_seconds() < COOL * 60:
                    continue
                last[k] = x["t"]
                x["sel"][thr] = True
                if x["side"] == 1:
                    fired_bar.add((x["tf"], x["i"]))
        CAND = [x for x in CAND if x["kind"] == "random" or x["sel"].any()]
        # stock outcomes (1-minute bars), every year
        for x in CAND:
            e, sd, a = x["e"], x["side"], x["atr"]
            if not (a > 0) or e < 1 or e + 30 >= len(c1) or d1[e + 30] != x["day"]:
                x["ok"] = False
                continue
            ent = c1[e - 1]
            hi, lo = h1a[e:e + 30], l1a[e:e + 30]
            fav = ((hi - ent) if sd == 1 else (ent - lo)) / a
            adv = ((ent - lo) if sd == 1 else (hi - ent)) / a
            up = np.nonzero(fav >= 0.5)[0]
            dn = np.nonzero(adv >= 0.5)[0]
            u, d = (up[0] if len(up) else 99), (dn[0] if len(dn) else 99)
            x.update(ok=True, r5=(c1[e + 4] - ent) * sd / a, r10=(c1[e + 9] - ent) * sd / a, r30=(c1[e + 29] - ent) * sd / a,
                     mfe10=float(fav[:10].max()), mae10=float(adv[:10].max()),
                     ab=(1.0 if u < d else 0.0) if min(u, d) < 99 else np.nan, usd10=(c1[e + 9] - ent) * sd)
        # option outcomes (real prices, Feb 2024 on): take +10%, out at -25% or 10 minutes
        byday = {}
        for x in CAND:
            if x.get("ok") and x["day"] >= opt_from:
                byday.setdefault(x["day"], []).append(x)
        for k, (d_, xl) in enumerate(sorted(byday.items())):
            sp = spot.get(d_)
            if sp is None:
                continue
            lo_, hi_ = np.nanmin(sp), np.nanmax(sp)
            strikes = np.arange(np.floor(lo_) - 8, np.ceil(hi_) + 9, 1.0)
            cons = [lab_occ(sym, d_, cp, s_) for s_ in strikes for cp in ("C", "P")]
            px = lab_fake_opt(cons, d_, {sym: sp}) if test else div_lock_fetch(oc, cons, d_)
            if k % 25 == 0:
                print(f"  {sym} {d_}: options ({k + 1}/{len(byday)} days)", flush=True)
            for x in xl:
                mb = int(mod1[x["e"] - 1]) if x["e"] >= 1 else -1
                if mb < 0 or mb > 380:
                    continue
                cp = "C" if x["side"] == 1 else "P"
                best, bk = None, None
                for s_ in strikes:
                    arr = px.get(lab_occ(sym, d_, cp, s_))
                    if arr is None or np.isnan(arr[mb]) or not (0.45 <= arr[mb] <= 1.00):
                        continue
                    if best is None or abs(arr[mb] - 0.70) < abs(best - 0.70):
                        best, bk = arr[mb], lab_occ(sym, d_, cp, s_)
                if bk is None:
                    continue
                path = pd.Series(px[bk][mb + 1:min(mb + 61, 386)]).ffill().bfill().to_numpy()
                if not len(path) or np.isnan(path).all():
                    continue
                cost = lambda p: max(0.01, 0.005 * p)
                ent = best + cost(best)
                g = np.array([(p - cost(p)) / ent - 1 for p in path])
                res = float(g[min(TSTOP - 1, len(g) - 1)])
                for j in range(min(TSTOP, len(g))):
                    if g[j] >= 0.10 or g[j] <= -0.25:
                        res = float(g[j])
                        break
                u10 = np.nonzero(g >= 0.10)[0]
                d25 = np.nonzero(g <= -0.25)[0]
                x.update(opt=res, o_hit10=bool(len(u10)), o_b10_25=bool(len(u10) and (not len(d25) or u10[0] < d25[0])),
                         o_heat=float(min(0.0, g[:u10[0]].min())) if len(u10) and u10[0] > 0 else (0.0 if len(u10) else np.nan),
                         o_entry=best)
        for x in CAND:
            if not x.get("ok"):
                continue
            r = {kk: x.get(kk, np.nan) for kk in ("tf", "side", "why", "score", "day", "hour", "kind", "r5", "r10", "r30", "mfe10",
                                                    "mae10", "ab", "usd10", "opt", "o_hit10", "o_b10_25", "o_heat", "o_entry")}
            r["sym"] = sym
            r["year"] = x["day"].year
            for j in range(7):
                r[f"sel{j}"] = bool(x["sel"][j]) if x["kind"] == "fire" else False
            for j, pn in enumerate(POINTS):
                r[f"p{j}"] = int(x["pts"][j])
            rows.append(r)
    R = pd.DataFrame(rows)
    nd = max(len(days_all), 1)
    md = ["# EDGE SCORE - full backtest, last 5 years", "",
          f"{', '.join(SYMBOLS)} | charts {', '.join(str(t) + 'm' for t in TFS)} | stock moves {t_start} to {end:%Y-%m-%d} ({nd} trading days) | "
          f"REAL 0DTE options $0.45-1.00 from {opt_from} (Alpaca option history starts Feb 2024). Exact indicator rules: E > D > A, "
          "score 0-6, 9:40-3:00, 10 min cooldown per chart and side. Entry = the signal candle's close. DATA ONLY.", "",
          "**Stock columns** (all 5 years, in ATR of that chart): avg move your way after 10 / 30 min, % green at 10 min, and "
          "**+0.5 ATR before -0.5 ATR** (1-minute highs/lows, 30 min max; same minute = loss).",
          "**Option columns** (Feb 2024 on): the indicator's rule - **take +10%, out at -25% or 10 minutes** - avg % per trade and % green; "
          "plus +10% before -25%, and +10% at all within 60 min (no stop).", ""]
    if not len(R):
        md.append("No trades.")
    else:
        F_, RN = R[R.kind == "fire"], R[R.kind == "random"]

        def line(name, g, perday=True):
            o = g[g.opt.notna()]
            fpd = f"{len(g) / nd:.1f}" if perday else "-"
            return (f"| {name} | {len(g)} | {fpd} | {g.r10.mean():+.3f} | {g.r30.mean():+.3f} | {(g.r10 > 0).mean() * 100:.0f}% | "
                    f"**{g.ab.mean() * 100:.0f}%** | {len(o)} | **{o.opt.mean() * 100:+.1f}%** | {(o.opt > 0).mean() * 100:.0f}% | "
                    f"{o.o_b10_25.astype(float).mean() * 100:.0f}% | {o.o_hit10.astype(float).mean() * 100:.0f}% |" if len(o) else
                    f"| {name} | {len(g)} | {fpd} | {g.r10.mean():+.3f} | {g.r30.mean():+.3f} | {(g.r10 > 0).mean() * 100:.0f}% | "
                    f"**{g.ab.mean() * 100:.0f}%** | 0 | - | - | - | - |")
        H = ("| Group | Fires | Per day | Move 10m (ATR) | Move 30m | Green at 10m | +0.5 before -0.5 ATR | Option trades | "
             "**Rule avg %** | Rule green | +10% before -25% | +10% at all |")
        HS = "|---|---|---|---|---|---|---|---|---|---|---|---|"
        AS = F_[F_.sel4]                                                   # as shipped: min score 4
        md += ["## A) The indicator as shipped (min score 4) vs random", "", H, HS,
               line("**EDGE, min score 4, all triggers**", AS), line("Random candle, random side", RN, False)]
        for w in ("E", "D", "A"):
            md.append(line(f"Trigger {w}", AS[AS.why == w]))
        md += ["", "## B) Raise the bar: every min score (all triggers, its own cooldown)", "", H, HS]
        for thr in range(7):
            md.append(line(f"min score {thr}", F_[F_[f"sel{thr}"]]))
        md += ["", "## C) Each trigger at each EXACT score (min score 0 list)", "", H, HS]
        Z = F_[F_.sel0]
        for w in ("E", "D", "A"):
            for s_ in range(7):
                g = Z[(Z.why == w) & (Z.score == s_)]
                if len(g) >= 20:
                    md.append(line(f"{w} score {s_}", g))
        md += ["", "## D) Which points help? (min score 0 list, YES vs NO)", "",
               "| Point | YES fires | YES +0.5 before -0.5 | NO +0.5 before -0.5 | YES rule avg | NO rule avg | Helps? |", "|---|---|---|---|---|---|---|"]
        for j, pn in enumerate(POINTS):
            y, nn = Z[Z[f"p{j}"] == 1], Z[Z[f"p{j}"] == 0]
            yo, no = y.opt.mean() * 100, nn.opt.mean() * 100
            helps = (y.ab.mean() > nn.ab.mean()) and (yo > no)
            md.append(f"| {pn} | {len(y)} | {y.ab.mean() * 100:.1f}% | {nn.ab.mean() * 100:.1f}% | {yo:+.1f}% | {no:+.1f}% | "
                      f"{'YES (both)' if helps else ('stock only' if y.ab.mean() > nn.ab.mean() else ('options only' if yo > no else 'no'))} |")
        md += ["", "## E) Year by year (as shipped, min score 4)", "", H, HS]
        for yr, g in AS.groupby("year"):
            md.append(line(str(yr), g, False))
        md.append(line("Random, all years", RN, False))
        md += ["", "## F) By chart, side and hour (as shipped, min score 4)", "", H, HS]
        for (s_, tf), g in AS.groupby(["sym", "tf"]):
            md.append(line(f"{s_} {tf}m", g))
        for k_, g in AS.groupby("side"):
            md.append(line("LONG (calls)" if k_ == 1 else "SHORT (puts)", g))
        for k_, g in AS.groupby("hour"):
            md.append(line(f"{k_}:00", g, False))
        md += ["", "## G) E only, min score 5+ (the tags to watch), by year", "", H, HS]
        E5 = F_[F_.sel5 & (F_.why == "E")]
        md.append(line("**E, score 5+**", E5))
        for yr, g in E5.groupby("year"):
            md.append(line(str(yr), g, False))
        R.to_csv(os.path.join(OUT, "edgebt_trades.csv.gz"), index=False, compression="gzip")
    md += ["", f"Runtime {(time.time() - t0) / 60:.1f} min. This is math/data, not financial advice."]
    txt = "\n".join(md)
    with open(os.path.join(OUT, "edgebt_latest.md"), "w") as fh:
        fh.write(txt)
    print(txt[:6000])
    print(f"\nSaved {OUT}/edgebt_latest.md")

import os as _os, sys as _sys
if __name__ == "__main__" and _os.getenv("MODE", "").strip().lower() in ("", "div"):
    import subprocess, urllib.request
    _src = urllib.request.urlopen("https://raw.githubusercontent.com/jnewsom188327/stoch-bot/"
                                  "6c1daa72e84dbf2385801e7019fcc841cdfa0702/backtest.py", timeout=120).read().decode()
    _me = open(__file__).read()
    _blk = _me[:_me.index("import os as _os, sys as _sys")]
    _old = 'if __name__ == "__main__" and os.getenv("MODE", "").strip().lower() in ("", "div"):\n    heat_main()\n    sys.exit(0)\n'
    if _old not in _src:
        _sys.exit("Could not find the old run lines in the saved backtest.py - nothing changed.")
    _new = _src.replace(_old, _blk + 'if __name__ == "__main__" and os.getenv("MODE", "").strip().lower() in ("", "div"):\n'
                        "    edgebt_main()\n    sys.exit(0)\n")
    with open(__file__, "w") as _f:
        _f.write(_new)
    subprocess.run(["git", "add", __file__])
    print("Restored the full backtest.py with the 5-year EDGE SCORE backtest added.", flush=True)
    _g = {"__name__": "div_lib", "__file__": __file__}
    exec(compile(_new, __file__, "exec"), _g)
    _g["edgebt_main"]()
    _sys.exit(0)
