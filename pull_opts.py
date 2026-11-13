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


def main():
    from alpaca.data.historical import OptionHistoricalDataClient
    from alpaca.data.requests import OptionBarsRequest
    from alpaca.data.timeframe import TimeFrame

    oc = OptionHistoricalDataClient(os.getenv("ALPACA_KEY", "").strip(), os.getenv("ALPACA_SECRET", "").strip())
    spy = pd.read_csv("results/spy_1m.csv.gz")
    spy["day"] = spy["t"].str[:10]
    days = sorted(spy["day"].unique())
    os.makedirs(OUT, exist_ok=True)
    t0, done = time.time(), 0
    for n, day in enumerate(days):
        if day < START or os.path.exists(f"{OUT}/{day}.json.gz"):
            continue
        g = spy[spy["day"] == day]
        nxt = days[n + 1] if n + 1 < len(days) else None
        if nxt is None:
            d = pd.Timestamp(day) + timedelta(days=1)
            while d.weekday() >= 5:
                d += timedelta(days=1)
            nxt = f"{d:%Y-%m-%d}"
        lo, hi = math.floor(g["low"].min()) - 2, math.ceil(g["high"].max()) + 2
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
