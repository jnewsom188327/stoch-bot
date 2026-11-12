# ============================================================================================================
# SPY 0DTE EDGE SCORE - BACKTEST ONLY, NO ORDERS. Runs by default while this block is in the file; set EDGE=0 or delete it to go back.
# Scores every minute the way the SPY 0DTE Edge dashboard does (SPY chart factors: Vix Fix 24, TTM 12, RSI 7, stoch 7,
# trend line + EMAs 8, VWAP 3), then checks what SPY and the real 1-OTM 0DTE call / put did next. Gamma is not in here.
# ============================================================================================================
EDGE_MONTHS = float(os.getenv("EDGE_MONTHS", "12") or 12)            # months of SPY 1-minute bars
EDGE_OPT_DAYS = int(float(os.getenv("EDGE_OPT_DAYS", "120") or 0))   # last N trading days get real option prices (0 = skip)
EDGE_W = dict(vix=24, ttm=12, rsi=7, stoch=7, trend=8, vwap=3)
EDGE_BK = ["A calls 62+", "B calls 55-62", "C neutral 45-55", "D puts 55-62", "E puts 62+"]


def edge_ema(x, L):
    k, o = 2 / (L + 1), np.empty(len(x))
    o[0] = x[0]
    for i in range(1, len(x)):
        o[i] = o[i - 1] + k * (x[i] - o[i - 1])
    return o


def edge_rma(x, L):
    o = np.empty(len(x))
    o[0] = x[0]
    for i in range(1, len(x)):
        o[i] = (o[i - 1] * (L - 1) + x[i]) / L
    return o


def edge_score(o, h, l, c, v, reg):
    """calls % (0-100) for every bar - same math as the dashboard's chart factors"""
    n, S = len(c), pd.Series
    cl = lambda a: np.clip(a, -1, 1)  # noqa: E731
    prev = lambda a: np.r_[a[0], a[:-1]]  # noqa: E731
    hc, lc = S(c).rolling(22, min_periods=1).max().to_numpy(), S(c).rolling(22, min_periods=1).min().to_numpy()
    wvf, wvs = (hc - l) / hc * 100, (h - lc) / lc * 100
    wh, sh = S(wvf).rolling(50, min_periods=1).max().to_numpy(), S(wvs).rolling(50, min_periods=1).max().to_numpy()
    F, G = np.where(wh > 0, wvf / np.where(wh > 0, wh, 1) * 100, 0), np.where(sh > 0, wvs / np.where(sh > 0, sh, 1) * 100, 0)
    fA, gA = edge_ema(F, 10), edge_ema(G, 10)
    pc = prev(c)
    tr = np.maximum(h - l, np.maximum(np.abs(h - pc), np.abs(l - pc)))
    tr[0] = h[0] - l[0]
    atr = edge_rma(tr, 14)
    hh, ll = S(h).rolling(20, min_periods=1).max().to_numpy(), S(l).rolling(20, min_periods=1).min().to_numpy()
    d = c - ((hh + ll) / 2 + S(c).rolling(20, min_periods=1).mean().to_numpy()) / 2
    m = np.zeros(n)
    for i in range(4, n):
        y = d[max(0, i - 19):i + 1]
        x = np.arange(len(y)) - (len(y) - 1) / 2
        den = (x * x).sum()
        m[i] = min(10, max(-10, (y.mean() + ((x * (y - y.mean())).sum() / den) * (len(y) - 1) / 2) / max(atr[i], 0.01)))
    e9, e13, e34 = edge_ema(c, 9), edge_ema(c, 13), edge_ema(c, 34)
    tp, w = (h + l + c) / 3, np.maximum(v, 1)
    a = int(np.argmax(reg)) if reg.any() else 0     # VWAP anchors at the 9:30 open
    vw = np.r_[np.cumsum((tp * w)[:a]) / np.maximum(np.cumsum(w[:a]), 1), np.cumsum((tp * w)[a:]) / np.cumsum(w[a:])]
    dc = np.r_[0, np.diff(c)]
    au, ad = edge_rma(np.maximum(dc, 0), 14), edge_rma(np.maximum(-dc, 0), 14)
    rsi = np.where(ad == 0, np.where(au == 0, 50, 100), 100 - 100 / (1 + au / np.where(ad == 0, 1, ad)))
    rsi[:2] = 50
    h14, l14 = S(h).rolling(14, min_periods=1).max().to_numpy(), S(l).rolling(14, min_periods=1).min().to_numpy()
    raw = np.where(h14 > l14, (c - l14) / np.where(h14 > l14, h14 - l14, 1) * 100, 50)
    K = S(raw).rolling(3, min_periods=1).mean().to_numpy()
    D = S(K).rolling(3, min_periods=1).mean().to_numpy()
    fR, gR, mR = F > prev(F), G > prev(G), m > prev(m)
    st, us, ds, state = np.zeros(n), 0, 0, 0
    for i in range(n):
        us = us + 1 if i and m[i] > m[i - 1] else 0
        ds = ds + 1 if i and m[i] < m[i - 1] else 0
        state = 1 if us >= 2 else state
        state = -1 if ds >= 2 else state
        st[i] = state
    ag = np.where((st == 1) & (gA > prev(gA)) & (fA < prev(fA)), 1, np.where((st == -1) & (gA < prev(gA)) & (fA > prev(fA)), -1, 0))
    trend = np.where((e13 > e34) & (c > vw), 1, np.where((e13 < e34) & (c < vw), -1, 0))
    cL, cS = (c < e13) & (e13 < prev(e13)), (c > e13) & (e13 > prev(e13))
    fadeL, fadeS = cL & np.r_[False, cL[:-1]], cS & np.r_[False, cS[:-1]]
    colv = np.where(trend == 1, np.where(fadeL, 0.2, 1.0), np.where(trend == -1, np.where(fadeS, -0.2, -1.0), 0.0))
    stx = (F - G) / 100
    mult = np.where(stx > 0, np.where((F < fA) | ~fR, 1, 0.4), np.where(stx < 0, np.where((G < gA) | ~gR, 1, 0.4), 1))
    s_vix = cl(0.75 * cl(stx * 1.4) * mult + 0.25 * ag)
    am = np.minimum(1, 0.5 + np.abs(m) / 4)
    s_ttm = np.where(m < 0, np.where(mR, am, -0.4), np.where(mR, 0.4, -am))
    s_rsi = cl((50 - rsi) / 25)
    s_sto = cl(0.6 * cl((50 - K) / 40) + np.where(K > D, 0.4, -0.4))
    s_trd = colv * 0.7 + np.where(e9 > e34, 0.3, -0.3)
    s_vw = cl((c - vw) / np.maximum(atr * 3, 0.05))
    W = EDGE_W
    pts = s_vix * W["vix"] + s_ttm * W["ttm"] + s_rsi * W["rsi"] + s_sto * W["stoch"] + s_trd * W["trend"] + s_vw * W["vwap"]
    return 50 + 50 * pts / sum(W.values())


def edge_bucket(s):
    return EDGE_BK[0] if s >= 62 else EDGE_BK[1] if s >= 55 else EDGE_BK[2] if s > 45 else EDGE_BK[3] if s > 38 else EDGE_BK[4]


def edge_opt_fetch(oc, contracts, day):
    """real 1-minute option bars for one day -> {contract: (open[390], close[390])}, closes carried forward 5 minutes at most"""
    from alpaca.data.requests import OptionBarsRequest
    from alpaca.data.timeframe import TimeFrame
    start = pd.Timestamp(day, tz=NY) + pd.Timedelta(hours=9, minutes=30)
    end = start + pd.Timedelta(minutes=391)
    grid, out, cl = pd.date_range(start, periods=390, freq="1min"), {}, sorted(contracts)
    for k0 in range(0, len(cl), 60):
        df = None
        for attempt in range(4):
            try:
                df = oc.get_option_bars(OptionBarsRequest(symbol_or_symbols=cl[k0:k0 + 60], timeframe=TimeFrame.Minute,
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
            g.index = g.index.tz_convert(NY)
            g = g[~g.index.duplicated()].reindex(grid)
            cc = g["close"].astype(float).ffill(limit=5)
            out[sym_] = (g["open"].astype(float).fillna(cc.shift(1)).to_numpy(), cc.to_numpy())
    return out


def edge_main():
    os.makedirs(OUT, exist_ok=True)
    t0 = time.time()
    now = datetime.now(timezone.utc) - timedelta(minutes=20)
    start = now - timedelta(days=int(EDGE_MONTHS * 30.5) + 5)
    print(f"SPY 0DTE EDGE SCORE: {start:%Y-%m-%d} -> {now:%Y-%m-%d}", flush=True)
    df1, feed = fetch_1m("SPY", start, now)
    rows = []
    for day, g in df1.groupby(df1.index.date):
        hm = g.index.hour * 100 + g.index.minute
        g, hm = g[(hm >= 400) & (hm < 1600)], hm[(hm >= 400) & (hm < 1600)]
        reg = np.asarray(hm >= 930)
        if reg.sum() < 300:
            continue
        o, h, l, c, v = (g[k].to_numpy() for k in ("open", "high", "low", "close", "volume"))
        sc = edge_score(o, h, l, c, np.nan_to_num(v), reg)
        mm = np.asarray(g.index.hour * 60 + g.index.minute)
        n = len(c)
        for i in np.where((mm >= 585) & (mm <= 870))[0]:          # 9:45 to 2:30, your trading window
            if i + 1 >= n or mm[i + 1] != mm[i] + 1:
                continue
            r = dict(day=day, mm=int(mm[i]), score=sc[i], S=c[i], ent=o[i + 1])
            for H in (5, 10, 20):
                j = i + H
                r[f"f{H}"] = c[j] - o[i + 1] if j < n and mm[j] == mm[i] + H else np.nan
            rows.append(r)
    R = pd.DataFrame(rows)
    if not len(R):
        sys.exit("No full trading days came back.")
    R["bk"] = R["score"].map(edge_bucket)
    fresh, last = np.zeros(len(R), bool), {}
    for k, (dy, mmv, b) in enumerate(zip(R["day"], R["mm"], R["bk"])):   # fresh = first minute in a bucket after 10+ minutes out of it
        fresh[k] = b != EDGE_BK[2] and mmv - last.get((dy, b), -99) > 10
        last[(dy, b)] = mmv
    R["fresh"] = fresh
    days = sorted(R["day"].unique())
    mid = days[len(days) // 2]
    sgn = {EDGE_BK[0]: 1, EDGE_BK[1]: 1, EDGE_BK[2]: 1, EDGE_BK[3]: -1, EDGE_BK[4]: -1}
    L = [f"# SPY 0DTE Edge score backtest - {days[0]} to {days[-1]}", "",
         f"{len(days)} trading days, SPY 1-minute bars ({feed}), every minute 9:45-2:30 scored with the dashboard's chart factors "
         "(61 of its 100 points; contract charts, gamma and contract math are not in this test). Entry = next minute's open. DATA ONLY.", "",
         "## 1. Every minute: what SPY did next, by score", "",
         "| Score | Minutes | Share | SPY +5m | Up % | SPY +10m | Up % | SPY +20m | Up % |", "|---|---|---|---|---|---|---|---|---|"]

    def row1(name, x):
        cells = [name, f"{len(x):,}", f"{100 * len(x) / len(R):.0f}%"]
        for H in (5, 10, 20):
            f = x[f"f{H}"].dropna()
            cells += [f"{f.mean():+.3f}" if len(f) else "-", f"{100 * (f > 0).mean():.0f}%" if len(f) else "-"]
        return "| " + " | ".join(cells) + " |"
    L += [row1(b, R[R["bk"] == b]) for b in EDGE_BK] + [row1("ALL MINUTES (baseline)", R), "",
          "The score works if SPY +$ falls steadily from the top row to the bottom row, and the top and bottom rows beat the baseline.", "",
          "## 2. Fresh readings only (first minute in a bucket), SPY move in the score's direction", "",
          "| Score | Fires | Per day | +5m | Right % | +10m | Right % | +20m | Right % | +10m 1st half | +10m 2nd half |", "|---|---|---|---|---|---|---|---|---|---|---|"]
    for b in (EDGE_BK[0], EDGE_BK[1], EDGE_BK[3], EDGE_BK[4]):
        x = R[(R["bk"] == b) & R["fresh"]]
        cells = [b, f"{len(x):,}", f"{len(x) / len(days):.1f}"]
        for H in (5, 10, 20):
            f = (x[f"f{H}"] * sgn[b]).dropna()
            cells += [f"{f.mean():+.3f}" if len(f) else "-", f"{100 * (f > 0).mean():.0f}%" if len(f) else "-"]
        for part in (x[x["day"] < mid], x[x["day"] >= mid]):
            f = (part["f10"] * sgn[b]).dropna()
            cells.append(f"{f.mean():+.3f}" if len(f) else "-")
        L.append("| " + " | ".join(cells) + " |")
    L += ["", "An edge is only real if both halves are positive.", ""]

    if EDGE_OPT_DAYS > 0:
        from alpaca.data.historical import OptionHistoricalDataClient
        oc = OptionHistoricalDataClient(os.getenv("ALPACA_KEY", "").strip(), os.getenv("ALPACA_SECRET", "").strip())
        E = R[R["day"].isin(days[-EDGE_OPT_DAYS:]) & (R["fresh"] | (R["mm"] % 15 == 0))].copy()
        E["cK"], E["pK"] = np.floor(E["S"]) + 1, np.ceil(E["S"]) - 1
        recs, got, req = [], 0, 0
        for day, x in E.groupby("day"):
            sym = lambda K, cp: f"SPY{pd.Timestamp(day):%y%m%d}{cp}{int(round(K * 1000)):08d}"  # noqa: E731
            bars = edge_opt_fetch(oc, {sym(K, "C") for K in x["cK"]} | {sym(K, "P") for K in x["pK"]}, day)
            for r in x.itertuples():
                rec, i = dict(day=day, bk=r.bk, fresh=r.fresh, grid=r.mm % 15 == 0), r.mm - 570
                for cp, K in (("C", r.cK), ("P", r.pK)):
                    req += 1
                    b = bars.get(sym(K, cp))
                    for H in (5, 10, 20):
                        ok = b is not None and i + H < 390 and b[0][i + 1] >= 0.05 and b[1][i + H] == b[1][i + H]
                        rec[f"{cp}{H}"] = (b[1][i + H] / b[0][i + 1] - 1) * 100 if ok else np.nan
                        rec[f"{cp}{H}s"] = ((b[1][i + H] - 0.02) / b[0][i + 1] - 1) * 100 if ok else np.nan   # 2 cents of slippage
                    got += int(b is not None and b[0][i + 1] == b[0][i + 1])
                recs.append(rec)
            print(f"  options {day}: {len(x)} entries", flush=True)
        Od = pd.DataFrame(recs)
        L += [f"## 3. Real 1-OTM 0DTE option prices, last {min(EDGE_OPT_DAYS, len(days))} trading days", "",
              f"Alpaca 1-minute option bars: {got:,} of {req:,} entries had a price. Buy at the next minute's open, sell at the close 5 / 10 / 20 minutes later. "
              "'After slip' takes 2 cents off the exit. 'Favored' = the call when the score says calls, the put when it says puts.", "",
              "| Score | Fires | Favored +5m | Win % | Favored +10m | Win % | After slip | Favored +20m | Win % | Other side +10m |", "|---|---|---|---|---|---|---|---|---|---|"]
        mean = lambda s_: f"{s_.dropna().mean():+.1f}%" if s_.notna().any() else "-"  # noqa: E731
        win = lambda s_: f"{100 * (s_.dropna() > 0).mean():.0f}%" if s_.notna().any() else "-"  # noqa: E731
        for b in (EDGE_BK[0], EDGE_BK[1], EDGE_BK[3], EDGE_BK[4]):
            x = Od[(Od["bk"] == b) & Od["fresh"]] if len(Od) else Od
            fv, ot = ("C", "P") if sgn[b] > 0 else ("P", "C")
            L.append("| " + " | ".join([b, f"{len(x):,}", mean(x[f"{fv}5"]), win(x[f"{fv}5"]), mean(x[f"{fv}10"]), win(x[f"{fv}10"]),
                                        mean(x[f"{fv}10s"]), mean(x[f"{fv}20"]), win(x[f"{fv}20"]), mean(x[f"{ot}10"])]) + " |")
        x = Od[Od["grid"]] if len(Od) else Od
        for nm, fv in (("Baseline: any call, every 15 min", "C"), ("Baseline: any put, every 15 min", "P")):
            L.append("| " + " | ".join([nm, f"{len(x):,}", mean(x[f"{fv}5"]), win(x[f"{fv}5"]), mean(x[f"{fv}10"]), win(x[f"{fv}10"]),
                                        mean(x[f"{fv}10s"]), mean(x[f"{fv}20"]), win(x[f"{fv}20"]), "-"]) + " |")
        L += ["", "The score earns its place only if the favored side beats both baselines after slip. Averages on cheap options are pulled up by a few big winners, so read Win % too.", ""]
    with open(f"{OUT}/EDGE_SCORE.md", "w") as f:
        f.write("\n".join(L) + "\n")
    print("\n".join(L), flush=True)
    sm = os.getenv("GITHUB_STEP_SUMMARY")
    if sm:
        with open(sm, "a") as f:
            f.write("\n".join(L) + "\n")
    print(f"total {time.time() - t0:.0f}s", flush=True)


if __name__ == "__main__" and os.getenv("EDGE", "1").strip() == "1":
    edge_main()
    sys.exit(0)
# ======================================= END SPY 0DTE EDGE SCORE BLOCK ===========================================
