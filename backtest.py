def div_mfe_main():
    """DIV PRO fires in 2026 only: how far each fire runs in your favor (max favorable move, in ATR and $/share)."""
    test = os.getenv("TEST", "") == "1"
    end = datetime.now(timezone.utc) - timedelta(days=1)
    start = datetime(2025, 12, 1, tzinfo=timezone.utc)          # December is warm-up only - fires counted from Jan 1
    os.makedirs(OUT, exist_ok=True)
    t0 = time.time()
    P = dict(DIV_DEF)
    WINS = (5, 10, 20, 30)
    rows = []
    for sym in SYMBOLS:
        print(f"\n=== {sym} ===", flush=True)
        df1 = fake_1m(sym, start, end)[0] if test else fetch_1m(sym, start, end)[0]
        for tf in TFS:
            df = to_tf(df1, rth_only=False, mins=tf)
            I = div_ind(df)
            T = div_run(I, P)
            if not len(T):
                continue
            T = T[T.year >= 2026]
            h, l, o, eod, n = I["h"], I["l"], I["o"], I["eod"], I["n"]
            ok = np.nonzero(I["sess"] & (I["atr"] > 0))[0]
            ok = ok[ok > 0]
            byday = pd.Series(ok).groupby(I["day"][ok]).apply(lambda s: s.to_numpy()).to_dict()
            rng = np.random.default_rng(7)

            def one(f, d, dist):
                a = I["atr"][f - 1]
                e = o[f]
                sl = e - d * dist * a
                last = f
                while last < n - 1 and last - f < max(WINS) - 1 and not eod[last]:
                    last += 1
                fav = ((h[f:last + 1] - e) if d > 0 else (e - l[f:last + 1])) / a
                adv = ((e - l[f:last + 1]) if d > 0 else (h[f:last + 1] - e)) / a
                hit = np.nonzero((l[f:last + 1] <= sl) if d > 0 else (h[f:last + 1] >= sl))[0]
                k = int(hit[0]) if len(hit) else len(fav)
                rec = dict(atr=a, mfe_stop=float(fav[:k].max()) if k > 0 else 0.0, stopped=bool(len(hit)),
                           mae=float(adv.max()), bars_to_peak=int(np.argmax(fav[:k])) + 1 if k > 0 else 0)
                for w in WINS:
                    rec[f"mfe{w}"] = float(fav[:w].max())
                return rec

            for _, t in T.iterrows():
                f, d, dist = int(t.bar), int(t.side), float(t.dist)
                rows.append(dict(sym=sym, tf=tf, side=d, grade=int(t.grade), dist=dist, hm=int(t.hm), kind="fire",
                                 **one(f, d, dist)))
                cand = byday.get(I["day"][f])
                for _ in range(3):
                    if cand is not None and len(cand):
                        rows.append(dict(sym=sym, tf=tf, side=d, grade=0, dist=dist, hm=0, kind="random",
                                         **one(int(rng.choice(cand)), d, dist)))
            print(f"  {sym} {tf}m: {len(T)} fires in 2026", flush=True)
    RA = pd.DataFrame(rows)
    R = RA[RA.kind == "fire"].copy() if len(RA) else RA
    RN = RA[RA.kind == "random"] if len(RA) else RA

    def line(name, g):
        return (f"| {name} | {len(g)} | **{g.mfe_stop.mean():.2f}** (${(g.mfe_stop * g.atr).mean():.2f}) | {g.mfe_stop.median():.2f} | "
                f"{g.mfe10.mean():.2f} | {g.mfe20.mean():.2f} | {g.mfe30.mean():.2f} | "
                f"{(g.mfe_stop >= 0.5).mean() * 100:.0f}% | {(g.mfe_stop >= 1).mean() * 100:.0f}% | {(g.mfe_stop >= 2).mean() * 100:.0f}% | "
                f"{(g.mfe_stop >= 3).mean() * 100:.0f}% | {g.mae.mean():.2f} | {g.bars_to_peak.median():.0f} |")

    head = ["| Group | Fires | Avg best move before stop ATR ($/sh) | Median | Avg best in 10 bars | in 20 | in 30 | "
            "Reached 0.5 ATR | 1 ATR | 2 ATR | 3 ATR | Avg worst move ATR | Bars to the best |",
            "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    md = ["# DIV PRO - 2026 only: how far each fire runs", "",
          f"{', '.join(SYMBOLS)} | charts {', '.join(str(t) + 'm' for t in TFS)} | Jan 1 2026 to {end:%Y-%m-%d} | "
          "DIV PRO defaults. Entry = the fire candle's open. Best move = the furthest price went your way, measured "
          "until the DIV stop was hit, 30 bars passed or 4 PM (whichever came first). In ATR of that chart, and $ per share. "
          "This is the most each fire OFFERED - a real exit catches less. The random row is 3 random candles per fire "
          "(same day, same side, same stop) - DIV only adds value by the amount it beats that row. DATA ONLY.", "",
          "## Every fire", ""] + head
    if len(R):
        md.append(line("**ALL DIV fires**", R))
        md.append(line("Random entries (same day, side, stop)", RN))
        for (s, tf), g in R.groupby(["sym", "tf"]):
            md.append(line(f"{s} {tf}m", g))
            gr = RN[(RN.sym == s) & (RN.tf == tf)]
            if len(gr):
                md.append(line(f"{s} {tf}m random", gr))
        md += ["", "## Long vs short", ""] + head
        for k, g in R.groupby("side"):
            md.append(line("LONG" if k == 1 else "SHORT", g))
        md += ["", "## By how far the entry was from the DIV swing (stop distance)", ""] + head
        R["db"] = pd.cut(R.dist, [0, 0.75, 1.25, 1.75, 9], labels=["under 0.75 ATR", "0.75-1.25", "1.25-1.75", "1.75+"])
        for k, g in R.groupby("db", observed=True):
            md.append(line(str(k), g))
        md += ["", "## By grade", ""] + head
        for k, g in R.groupby("grade"):
            md.append(line(f"G{k}", g))
        md += ["", "## By hour (ET)", ""] + head
        for k, g in R.groupby(R.hm // 100):
            md.append(line(f"{k}:00", g))
        R.to_csv(os.path.join(OUT, "divmfe_trades.csv"), index=False)
    md += ["", f"Runtime {(time.time() - t0) / 60:.1f} min. This is math/data, not financial advice."]
    txt = "\n".join(md)
    for fn in ("divmfe_latest.md",):
        with open(os.path.join(OUT, fn), "w") as fh:
            fh.write(txt)
    print(txt[:6000])
    print(f"\nSaved {OUT}/divmfe_latest.md")

import os as _os, sys as _sys
if __name__ == "__main__" and _os.getenv("MODE", "").strip().lower() in ("", "div"):
    import subprocess, urllib.request
    _src = urllib.request.urlopen("https://raw.githubusercontent.com/jnewsom188327/stoch-bot/"
                                  "4de18105b009598c59a20fc6af86abfd0dd66243/backtest.py", timeout=120).read().decode()
    _me = open(__file__).read()
    _blk = _me[:_me.index("import os as _os, sys as _sys")]
    _old = 'if __name__ == "__main__" and os.getenv("MODE", "").strip().lower() in ("", "div"):\n    div_main()\n    sys.exit(0)\n'
    _new = _src.replace(_old, _blk + 'if __name__ == "__main__" and os.getenv("MODE", "").strip().lower() in ("", "div"):\n'
                        "    div_mfe_main()\n    sys.exit(0)\n")
    with open(__file__, "w") as _f:
        _f.write(_new)
    subprocess.run(["git", "add", __file__])
    print("Restored the full backtest.py with the 2026 DIV best-move test added.", flush=True)
    _g = {"__name__": "div_lib", "__file__": __file__}
    exec(compile(_new, __file__, "exec"), _g)
    _g["div_mfe_main"]()
    _sys.exit(0)
