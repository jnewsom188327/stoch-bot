def div_trail_sim(g, L, S, after, part):
    """One option trade on 1-minute closes (g = % gain as a fraction, after fills). Initial stop -S%. Once +L% is
    reached: sell `part` there, then the rest exits on the lock rule. Returns the trade's % on premium (fraction)."""
    locked, peak, real, w = False, 0.0, 0.0, 1.0
    for x in g:
        if not locked:
            if x <= -S / 100:
                return real + w * x
            if x >= L / 100:
                locked, peak = True, x
                if part:
                    real += part * x
                    w -= part
            continue
        peak = max(peak, x)
        if after == "BE":
            stop = 0.0
        elif after == "+5":
            stop = 0.05
        else:
            stop = max(0.0, peak - int(after[5:]) / 100)
        if x <= stop:
            return real + w * x
    return real + w * g[-1]


def div_trail_main():
    """DIV PRO fires in 2026 on REAL 0DTE options $0.45-1.00: lock green at +10/15/20%, then breakeven / +5% / trailing
    stop, with or without selling half at the lock. Up to 60 minutes, out by 3:55."""
    test = os.getenv("TEST", "") == "1"
    end = datetime.now(timezone.utc) - timedelta(days=1)
    start = datetime(2025, 12, 1, tzinfo=timezone.utc)
    os.makedirs(OUT, exist_ok=True)
    t0 = time.time()
    P = dict(DIV_DEF)
    LO, HI, AIM, HOLD, SLIP = 0.45, 1.00, 0.70, 60, 0.01
    PLANS = [(L, S, a, p) for L in (10, 15, 20) for S in (20, 30) for a in ("BE", "+5", "trail10", "trail15", "trail20")
             for p in (0.0, 0.5)]
    oc = None
    if not test:
        from alpaca.data.historical import OptionHistoricalDataClient
        oc = OptionHistoricalDataClient(os.getenv("ALPACA_KEY", "").strip(), os.getenv("ALPACA_SECRET", "").strip())
    rows = []
    rng = np.random.default_rng(11)
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
        fires = []
        for tf in TFS:
            df = to_tf(df1, rth_only=False, mins=tf)
            I = div_ind(df)
            T = div_run(I, P)
            if not len(T):
                continue
            T = T[T.year >= 2026]
            ts = df.index
            for _, t in T.iterrows():
                tt = ts[int(t.bar)]
                m0 = tt.hour * 60 + tt.minute - 570
                if m0 < 1 or m0 > 385 - 15:
                    continue
                fires.append((tf, tt.date(), int(m0), int(t.side), int(t.grade), "fire"))
                for _ in range(2):
                    fires.append((tf, tt.date(), int(rng.integers(15, 300)), int(t.side), 0, "random"))
        print(f"  {sum(f[5] == 'fire' for f in fires)} regular-hours fires in 2026 (+ random entries)", flush=True)
        byday = {}
        for f in fires:
            byday.setdefault(f[1], []).append(f)
        for k, (day, fl) in enumerate(sorted(byday.items())):
            sp = spot.get(day)
            if sp is None:
                continue
            lo, hi = np.nanmin(sp), np.nanmax(sp)
            strikes = np.arange(np.floor(lo) - 8, np.ceil(hi) + 9, 1.0)
            cons = [lab_occ(sym, day, cp, s_) for s_ in strikes for cp in ("C", "P")]
            px = lab_fake_opt(cons, day, {sym: sp}) if test else div_lock_fetch(oc, cons, day)
            if k % 20 == 0:
                print(f"  {sym} {day}: {len(px)} contracts with prices ({k + 1}/{len(byday)} days)", flush=True)
            for tf, _, m0, side, grade, kind in fl:
                cp = "C" if side == 1 else "P"
                best, bk = None, None
                for s_ in strikes:
                    c = lab_occ(sym, day, cp, s_)
                    arr = px.get(c)
                    if arr is None:
                        continue
                    p0 = arr[m0 - 1]
                    if np.isnan(p0) or not (LO <= p0 <= HI):
                        continue
                    if best is None or abs(p0 - AIM) < abs(best - AIM):
                        best, bk = p0, c
                if bk is None:
                    continue
                path = px[bk][m0:min(m0 + HOLD, 385)]
                if np.isnan(path).all():
                    continue
                path = pd.Series(path).ffill().bfill().to_numpy()
                ent = best + SLIP
                g = (path - SLIP) / ent - 1
                rec = dict(sym=sym, tf=tf, side=side, grade=grade, kind=kind, hour=9 + (m0 + 30) // 60)
                rec["hold"] = float(g[-1])
                for j, (L, S, a_, p_) in enumerate(PLANS):
                    rec[f"p{j}"] = div_trail_sim(g, L, S, a_, p_)
                rows.append(rec)
    R = pd.DataFrame(rows)
    md = ["# DIV PRO lock-green + runner study - 2026, real 0DTE options $0.45-1.00", "",
          f"Charts {', '.join(str(t) + 'm' for t in TFS)} | Jan 1 2026 to {end:%Y-%m-%d}. Same contract rule as before (closest to $0.70 "
          "inside $0.45-1.00, same-day expiry, 1c each way). Start stop -20% or -30%. When the option first closes at the LOCK level: "
          "optionally sell HALF there, then the rest exits on the after-lock rule: BE = stop at the entry price, +5 = stop at +5%, "
          "trailN = stop N points under the best close (never below entry). Up to 60 minutes, out by 3:55. "
          "All exits at 1-minute closes. Random = 2 random times per fire, same day + side, best plan. DATA ONLY.", ""]
    if not len(R):
        md.append("No trades - no option prices came back.")
    else:
        F, RN = R[R.kind == "fire"], R[R.kind == "random"]
        res = []
        for j, (L, S, a_, p_) in enumerate(PLANS):
            x = F[f"p{j}"] * 100
            wins, losses = x[x > 0], x[x <= 0]
            pf = wins.sum() / -losses.sum() if losses.sum() < 0 else np.nan
            res.append((x.mean(), j, L, S, a_, p_, (x > 0).mean() * 100, wins.mean() if len(wins) else 0,
                        losses.mean() if len(losses) else 0, pf, RN[f"p{j}"].mean() * 100 if len(RN) else np.nan))
        res.sort(reverse=True)
        md += [f"Trades: {len(F)} DIV fires, {len(RN)} random. Just holding 60 min (or to 3:55) with no stop: "
               f"DIV {F.hold.mean() * 100:+.1f}%, random {RN.hold.mean() * 100:+.1f}% per trade.", "",
               "## A) Every plan, best first (avg % on the premium per trade)", "",
               "| # | Lock at | Start stop | Sell half at lock? | After the lock | **Avg % per trade** | Green trades % | Avg green % | "
               "Avg red % | Profit factor | Random, same plan |", "|---|---|---|---|---|---|---|---|---|---|---|"]
        for r_, (m_, j, L, S, a_, p_, w_, aw, al, pf, rn) in enumerate(res, 1):
            md.append(f"| {r_} | +{L}% | -{S}% | {'yes' if p_ else 'no'} | {a_} | **{m_:+.1f}%** | {w_:.0f}% | {aw:+.0f}% | {al:+.0f}% | "
                      f"{div_f(pf, '{:.2f}')} | {rn:+.1f}% |")
        bj = res[0][1]
        L, S, a_, p_ = PLANS[bj]
        md += ["", f"## B) The best plan (lock +{L}%, start stop -{S}%, {'sell half at the lock, ' if p_ else ''}then {a_}) by group", "",
               "| Group | Trades | Avg % per trade | Green % |", "|---|---|---|---|"]
        for name, g in ([("**ALL DIV**", F), ("Random", RN)] + [(f"{s_} {tf}m", g) for (s_, tf), g in F.groupby(["sym", "tf"])]
                        + [("CALLS" if k == 1 else "PUTS", g) for k, g in F.groupby("side")]
                        + [(f"{k}:00", g) for k, g in F.groupby("hour")] + [(f"G{k}", g) for k, g in F.groupby("grade")]):
            md.append(f"| {name} | {len(g)} | **{g[f'p{bj}'].mean() * 100:+.1f}%** | {(g[f'p{bj}'] > 0).mean() * 100:.0f}% |")
        R.to_csv(os.path.join(OUT, "divtrail_trades.csv"), index=False)
    md += ["", f"Runtime {(time.time() - t0) / 60:.1f} min. This is math/data, not financial advice."]
    txt = "\n".join(md)
    with open(os.path.join(OUT, "divtrail_latest.md"), "w") as fh:
        fh.write(txt)
    print(txt[:6000])
    print(f"\nSaved {OUT}/divtrail_latest.md")

import os as _os, sys as _sys
if __name__ == "__main__" and _os.getenv("MODE", "").strip().lower() in ("", "div"):
    import subprocess, urllib.request
    _src = urllib.request.urlopen("https://raw.githubusercontent.com/jnewsom188327/stoch-bot/"
                                  "44c165b2e961bd89a7c1078942bf7dbb103f9870/backtest.py", timeout=120).read().decode()
    _me = open(__file__).read()
    _blk = _me[:_me.index("import os as _os, sys as _sys")]
    _old = 'if __name__ == "__main__" and os.getenv("MODE", "").strip().lower() in ("", "div"):\n    div_lock_main()\n    sys.exit(0)\n'
    if _old not in _src:
        _sys.exit("Could not find the old DIV run lines in the saved backtest.py - nothing changed.")
    _new = _src.replace(_old, _blk + 'if __name__ == "__main__" and os.getenv("MODE", "").strip().lower() in ("", "div"):\n'
                        "    div_trail_main()\n    sys.exit(0)\n")
    with open(__file__, "w") as _f:
        _f.write(_new)
    subprocess.run(["git", "add", __file__])
    print("Restored the full backtest.py with the 2026 DIV lock-green + runner test added.", flush=True)
    _g = {"__name__": "div_lib", "__file__": __file__}
    exec(compile(_new, __file__, "exec"), _g)
    _g["div_trail_main"]()
    _sys.exit(0)
