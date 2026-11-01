def div_lock_fetch(oc, contracts, day):
    """1-minute option closes 9:30-15:59 ET -> {contract: np.array(390)} (gaps filled up to 3 min)."""
    from alpaca.data.requests import OptionBarsRequest
    from alpaca.data.timeframe import TimeFrame
    start = pd.Timestamp(day, tz=NY) + pd.Timedelta(hours=9, minutes=30)
    end = start + pd.Timedelta(minutes=390)
    out = {}
    cl = sorted(contracts)
    for k0 in range(0, len(cl), 60):
        chunk = cl[k0:k0 + 60]
        df = None
        for attempt in range(4):
            try:
                df = oc.get_option_bars(OptionBarsRequest(symbol_or_symbols=chunk, timeframe=TimeFrame.Minute,
                                                          start=start.tz_convert("UTC").to_pydatetime(),
                                                          end=end.tz_convert("UTC").to_pydatetime())).df
                break
            except Exception as e:  # noqa: BLE001
                print(f"  option bars {day} failed ({attempt + 1}/4): {str(e)[:200]}", flush=True)
                time.sleep(5 * (attempt + 1))
        if df is None or not len(df) or not isinstance(df.index, pd.MultiIndex):
            continue
        for sym_, g in df.groupby(level=0):
            g = g.droplevel(0)
            ix = g.index.tz_convert(NY)
            mm = (ix.hour * 60 + ix.minute - 570).to_numpy()
            ok = (mm >= 0) & (mm < 390)
            a = np.full(390, np.nan)
            a[mm[ok]] = g["close"].to_numpy()[ok]
            out[sym_] = pd.Series(a).ffill(limit=3).to_numpy()
    return out


def div_lock_main():
    """DIV PRO fires in 2026, traded with a REAL 0DTE option priced $0.45-1.00 at the fire:
    how far the option runs (% gain), how often each lock-green level gets hit, and what each lock level pays."""
    test = os.getenv("TEST", "") == "1"
    end = datetime.now(timezone.utc) - timedelta(days=1)
    start = datetime(2025, 12, 1, tzinfo=timezone.utc)          # December = warm-up only, fires counted from Jan 1 2026
    os.makedirs(OUT, exist_ok=True)
    t0 = time.time()
    P = dict(DIV_DEF)
    LO, HI, AIM = 0.45, 1.00, 0.70        # contract price band at the fire, pick the one closest to $0.70
    HOLD = 30                             # minutes the trade is watched
    SLIP = 0.01                           # $ per contract-share each side (buy 1c over, sell 1c under the last trade)
    LOCKS = (10, 15, 20, 25, 30, 40, 50, 75, 100)
    STOPS = (20, 30, 50)
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
        spot = {}                                           # day -> 390 1m closes (regular hours)
        for d_, ix in pd.Series(np.nonzero(rth)[0]).groupby(d1[rth]):
            a = np.full(390, np.nan)
            ii = ix.to_numpy()
            a[mod1[ii]] = df1["close"].to_numpy()[ii]
            spot[d_] = pd.Series(a).ffill().bfill().to_numpy()
        fires = []                                          # (tf, day, minute, side, grade, kind)
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
                if m0 < 1 or m0 > 390 - HOLD - 5:
                    continue                                 # premarket fires have no options; need room to hold
                fires.append((tf, tt.date(), int(m0), int(t.side), int(t.grade), "fire"))
                for _ in range(2):                           # 2 random entries per fire: same day, same side
                    fires.append((tf, tt.date(), int(rng.integers(15, 390 - HOLD - 5)), int(t.side), 0, "random"))
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
                path = px[bk][m0:m0 + HOLD]
                if np.isnan(path).all():
                    continue
                path = pd.Series(path).ffill().to_numpy()
                ent = best + SLIP
                g = (path - SLIP) / ent - 1                  # % gain if sold at each minute's close
                g = np.nan_to_num(g, nan=g[~np.isnan(g)][0] if (~np.isnan(g)).any() else 0.0)
                rec = dict(sym=sym, tf=tf, day=day, minute=m0, hour=9 + (m0 + 30) // 60, side=side, grade=grade,
                           kind=kind, contract=bk, entry=ent, peak=float(g.max()) * 100, trough=float(g.min()) * 100,
                           end=float(g[-1]) * 100, min_to_peak=int(np.argmax(g)) + 1)
                for L in LOCKS:                              # first minute the lock level is reached (or -1)
                    hit = np.nonzero(g >= L / 100)[0]
                    rec[f"hit{L}"] = int(hit[0]) if len(hit) else -1
                for S in STOPS:
                    hit = np.nonzero(g <= -S / 100)[0]
                    rec[f"stop{S}"] = int(hit[0]) if len(hit) else -1
                rec["path_end"] = float(g[-1])
                rows.append(rec)
    R = pd.DataFrame(rows)

    def ev(g, L, S):
        """sell everything at +L%, or at -S% (stop first if both in the same minute), or at the 30-minute close"""
        out = []
        for _, r in g.iterrows():
            h, s = r[f"hit{L}"], (r[f"stop{S}"] if S else -1)
            if s >= 0 and (h < 0 or s <= h):
                out.append(-S)
            elif h >= 0:
                out.append(L)
            else:
                out.append(r.end)
        return float(np.mean(out)) if out else np.nan

    md = ["# DIV PRO lock-green study - 2026, real 0DTE options $0.45-1.00", "",
          f"{', '.join(sorted(R.sym.unique())) if len(R) else ''} | charts {', '.join(str(t) + 'm' for t in TFS)} | Jan 1 2026 to "
          f"{end:%Y-%m-%d}. Each DIV PRO fire (9:45-2:30 ET, options trade 9:30-4) buys the same-day call (long) or put (short) "
          f"priced closest to $0.70 inside $0.45-1.00, at the last 1-minute close before the fire candle opens + 1c. Sold at "
          f"1-minute closes - 1c. Watched {HOLD} minutes. Random row = 2 random times per fire, same day and side, same contract rule. "
          "Real Alpaca option prices. DATA ONLY.", ""]
    if not len(R):
        md.append("No trades - no option prices came back.")
    else:
        F, RN = R[R.kind == "fire"], R[R.kind == "random"]
        md += ["## A) How far the option runs in 30 minutes", "",
               "| Group | Trades | Avg entry $ | Avg best % | Median best % | Avg worst % | Median worst % | Median minutes to best | "
               "Avg % if just held 30 min |", "|---|---|---|---|---|---|---|---|---|"]

        def rowA(name, g):
            return (f"| {name} | {len(g)} | {g.entry.mean():.2f} | **{g.peak.mean():.0f}%** | {g.peak.median():.0f}% | "
                    f"{g.trough.mean():.0f}% | {g.trough.median():.0f}% | {g.min_to_peak.median():.0f} | {g.end.mean():+.0f}% |")
        md.append(rowA("**DIV fires**", F))
        md.append(rowA("Random entries", RN))
        for (s_, tf), g in F.groupby(["sym", "tf"]):
            md.append(rowA(f"{s_} {tf}m", g))
        for k, g in F.groupby("side"):
            md.append(rowA("CALLS (long fires)" if k == 1 else "PUTS (short fires)", g))

        md += ["", "## B) How often each lock-green level gets hit (within 30 min)", "",
               "Hit = the option's 1-minute close reached that gain at least once. 'Before -30%' = it got there before ever closing 30% down.",
               "", "| Lock level | DIV hit % | Hit before -20% | Hit before -30% | Median minutes to hit | Random hit % |",
               "|---|---|---|---|---|---|"]
        for L in LOCKS:
            hit = F[f"hit{L}"] >= 0
            b20 = hit & ((F["stop20"] < 0) | (F["stop20"] > F[f"hit{L}"]))
            b30 = hit & ((F["stop30"] < 0) | (F["stop30"] > F[f"hit{L}"]))
            md.append(f"| +{L}% | **{hit.mean() * 100:.0f}%** | {b20.mean() * 100:.0f}% | {b30.mean() * 100:.0f}% | "
                      f"{F.loc[hit, f'hit{L}'].median() + 1 if hit.any() else 0:.0f} | {(RN[f'hit{L}'] >= 0).mean() * 100:.0f}% |")

        md += ["", "## C) What each plan pays per trade (avg % on the premium, after the 1c fills)", "",
               "Sell ALL at the lock level, stop at the % shown, otherwise sell at the 30-minute close. Best cell = the lock to use.",
               "", "| Lock (sell all at) | stop -20% | stop -30% | stop -50% | no stop | Random, stop -30% |", "|---|---|---|---|---|---|"]
        best = (None, -1e9)
        for L in LOCKS:
            vals = [ev(F, L, S) for S in (20, 30, 50, 0)]
            for S, v in zip((20, 30, 50, 0), vals):
                if v > best[1]:
                    best = ((L, S), v)
            md.append(f"| +{L}% | " + " | ".join(f"{v:+.1f}%" for v in vals) + f" | {ev(RN, L, 30):+.1f}% |")
        md += ["", f"**Best plan: sell at +{best[0][0]}%, stop {('-' + str(best[0][1]) + '%') if best[0][1] else 'none'} -> "
                   f"{best[1]:+.1f}% per trade on average.**"]

        md += ["", "## D) Best plan by chart and by hour (sell at the best lock above)", "",
               "| Group | Trades | Hit the lock % | Stopped % | Avg % per trade |", "|---|---|---|---|---|"]
        L, S = best[0]

        def rowD(name, g):
            h = g[f"hit{L}"]
            s = g[f"stop{S}"] if S else pd.Series(-1, index=g.index)
            stopped = (s >= 0) & ((h < 0) | (s <= h))
            locked = (h >= 0) & ~stopped
            return f"| {name} | {len(g)} | {locked.mean() * 100:.0f}% | {stopped.mean() * 100:.0f}% | **{ev(g, L, S):+.1f}%** |"
        for (s_, tf), g in F.groupby(["sym", "tf"]):
            md.append(rowD(f"{s_} {tf}m", g))
        for k, g in F.groupby("side"):
            md.append(rowD("CALLS" if k == 1 else "PUTS", g))
        for k, g in F.groupby("hour"):
            md.append(rowD(f"{k}:00", g))
        for k, g in F.groupby("grade"):
            md.append(rowD(f"G{k}", g))
        R.to_csv(os.path.join(OUT, "divlock_trades.csv"), index=False)
    md += ["", f"Runtime {(time.time() - t0) / 60:.1f} min. This is math/data, not financial advice."]
    txt = "\n".join(md)
    with open(os.path.join(OUT, "divlock_latest.md"), "w") as fh:
        fh.write(txt)
    print(txt[:6000])
    print(f"\nSaved {OUT}/divlock_latest.md")

import os as _os, sys as _sys
if __name__ == "__main__" and _os.getenv("MODE", "").strip().lower() in ("", "div"):
    import subprocess, urllib.request
    _src = urllib.request.urlopen("https://raw.githubusercontent.com/jnewsom188327/stoch-bot/"
                                  "2dbafeeff72ea4fb85ab7d8484942527039a1bd4/backtest.py", timeout=120).read().decode()
    _me = open(__file__).read()
    _blk = _me[:_me.index("import os as _os, sys as _sys")]
    _old = 'if __name__ == "__main__" and os.getenv("MODE", "").strip().lower() in ("", "div"):\n    div_mfe_main()\n    sys.exit(0)\n'
    if _old not in _src:
        _sys.exit("Could not find the old DIV run lines in the saved backtest.py - nothing changed.")
    _new = _src.replace(_old, _blk + 'if __name__ == "__main__" and os.getenv("MODE", "").strip().lower() in ("", "div"):\n'
                        "    div_lock_main()\n    sys.exit(0)\n")
    with open(__file__, "w") as _f:
        _f.write(_new)
    subprocess.run(["git", "add", __file__])
    print("Restored the full backtest.py with the 2026 DIV lock-green options test added.", flush=True)
    _g = {"__name__": "div_lib", "__file__": __file__}
    exec(compile(_new, __file__, "exec"), _g)
    _g["div_lock_main"]()
    _sys.exit(0)
