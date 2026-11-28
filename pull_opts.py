"""Option price history for the 0DTE vs 1DTE test (data only, no orders).
For every day in results/spy_1m.csv.gz, saves 1-minute bars of the SPY calls and puts near that day's range,
expiring the same day (0DTE) and the next trading day (1DTE), to results/opt_1m/<day>.json.gz.
Days already saved are skipped, so a re-run picks up where it stopped. START=YYYY-MM-DD sets the first day."""
import gzip
import json
import math
import os
import time
from datetime import timedelta

import pandas as pd

NY = "America/New_York"
OUT = "results/opt_1m"
START = os.getenv("START", "2025-11-03")
END = os.getenv("END", "9999-12-31")
WIDEN = int(os.getenv("WIDEN", "2"))  # strikes past the day's low/high; 6 covers the shadow log's 3-ITM strikes
REDO = os.getenv("REDO", "") == "yes"
HOLIDAYS = {"2026-11-26", "2026-12-25", "2027-01-01", "2027-01-18", "2027-02-15", "2027-03-26", "2027-05-31", "2027-06-18", "2027-07-05", "2027-09-06", "2027-11-25", "2027-12-24"}  # pull days that are already saved again (e.g. with a wider strike range)


def main():
    from alpaca.data.historical import OptionHistoricalDataClient
    from alpaca.data.requests import OptionBarsRequest
    from alpaca.data.timeframe import TimeFrame

    oc = OptionHistoricalDataClient(os.getenv("ALPACA_KEY", "").strip(), os.getenv("ALPACA_SECRET", "").strip())
    spy = pd.read_csv("results/spy_1m.csv.gz")
    spy["day"] = spy["t"].str[:10]
    # days after spy_1m.csv.gz ends: take SPY's bars from the saved results/bars_<day>.json files (Nov 2026 on)
    extra = []
    for f in sorted(os.listdir("results")):
        if f.startswith("bars_") and f.endswith(".json") and f[5:15] not in set(spy["day"]):
            B = json.load(open(f"results/{f}"))
            extra += [{"t": r[0], "open": r[1], "high": r[2], "low": r[3], "close": r[4], "volume": r[5], "day": B["day"]} for r in B["spy"]]
    if extra:
        spy = pd.concat([spy, pd.DataFrame(extra)], ignore_index=True)
    days = sorted(spy["day"].unique())
    os.makedirs(OUT, exist_ok=True)
    t0, done = time.time(), 0
    for n, day in enumerate(days):
        if day < START or day > END or (os.path.exists(f"{OUT}/{day}.json.gz") and not REDO):
            continue
        g = spy[spy["day"] == day]
        nxt = days[n + 1] if n + 1 < len(days) else None
        if nxt is None:
            d = pd.Timestamp(day) + timedelta(days=1)
            while d.weekday() >= 5 or f"{d:%Y-%m-%d}" in HOLIDAYS:
                d += timedelta(days=1)
            nxt = f"{d:%Y-%m-%d}"
        lo, hi = math.floor(g["low"].min()) - WIDEN, math.ceil(g["high"].max()) + WIDEN
        syms = [f"SPY{pd.Timestamp(e):%y%m%d}{cp}{K * 1000:08d}" for e in (day, nxt) for cp in "CP" for K in range(lo, hi + 1)]
        start = pd.Timestamp(day).tz_localize(NY) + pd.Timedelta(hours=9, minutes=30)
        end = start + pd.Timedelta(minutes=391)
        out = {}
        for k0 in range(0, len(syms), 60):
            df = None
            for attempt in range(5):
                try:
                    df = oc.get_option_bars(OptionBarsRequest(symbol_or_symbols=syms[k0:k0 + 60], timeframe=TimeFrame.Minute,
                                                              start=start.tz_convert("UTC").to_pydatetime(),
                                                              end=end.tz_convert("UTC").to_pydatetime())).df
                    break
                except Exception as e:  # noqa: BLE001
                    print(f"  {day} failed ({attempt + 1}/5): {str(e)[:200]}", flush=True)
                    time.sleep(5 * (attempt + 1))
            if df is None or not len(df) or not isinstance(df.index, pd.MultiIndex):
                continue
            for sym, b in df.groupby(level=0):
                b = b.droplevel(0)
                b.index = b.index.tz_convert(NY)
                i = ((b.index - start) / pd.Timedelta(minutes=1)).astype(int)
                rows = [[int(k), round(float(r.open), 2), round(float(r.high), 2), round(float(r.low), 2), round(float(r.close), 2), int(r.volume)]
                        for k, r in zip(i, b.itertuples()) if 0 <= k < 390]
                if rows:
                    out[sym] = rows
        with gzip.open(f"{OUT}/{day}.json.gz", "wt") as f:
            json.dump({"day": day, "exp1": nxt, "opt": out}, f, separators=(",", ":"))
        done += 1
        print(f"{day}: {len(out)} of {len(syms)} contracts had prices  ({time.time() - t0:.0f}s)", flush=True)
        if time.time() - t0 > 160 * 60:
            print("Time limit reached; run it again to continue.", flush=True)
            break
    print(f"saved {done} days", flush=True)


if __name__ == "__main__":
    main()
