"""QQQ / IWM history for the dot tests (data only, no orders).
For each ticker in SYMBOLS (default QQQ,IWM): 1-minute bars since START to results/<sym>_1m.csv.gz, then each day's
1-minute bars for the calls and puts near that day's range, expiring that day and the next trading day,
to results/opt_<sym>/<day>.json.gz. Days already saved are skipped, so a re-run picks up where it stopped."""
import gzip
import json
import math
import os
import time
from datetime import datetime, timedelta, timezone

import pandas as pd

from bars_daily import fetch_1m

NY = "America/New_York"
SYMS = [s.strip().upper() for s in os.getenv("SYMBOLS", "QQQ,IWM").split(",") if s.strip()]
START = os.getenv("START", "2025-10-20")


def main():
    from alpaca.data.historical import OptionHistoricalDataClient
    from alpaca.data.requests import OptionBarsRequest
    from alpaca.data.timeframe import TimeFrame

    oc = OptionHistoricalDataClient(os.getenv("ALPACA_KEY", "").strip(), os.getenv("ALPACA_SECRET", "").strip())
    t0 = time.time()
    for sym in SYMS:
        path = f"results/{sym.lower()}_1m.csv.gz"
        end = datetime.now(timezone.utc) - timedelta(minutes=20)
        df, feed = fetch_1m(sym, datetime.fromisoformat(START).replace(tzinfo=timezone.utc), end)
        df = df.between_time("09:30", "15:59")
        df.index.name = "t"
        df.round(4).to_csv(path, compression="gzip")
        print(sym, len(df), "bars", feed, flush=True)
        bars = pd.read_csv(path)
        bars["day"] = bars["t"].str[:10]
        days = sorted(bars["day"].unique())
        out_dir = f"results/opt_{sym.lower()}"
        os.makedirs(out_dir, exist_ok=True)
        for n, day in enumerate(days):
            if day < "2025-11-03" or os.path.exists(f"{out_dir}/{day}.json.gz"):
                continue
            g = bars[bars["day"] == day]
            nxt = days[n + 1] if n + 1 < len(days) else None
            if nxt is None:
                d = pd.Timestamp(day) + timedelta(days=1)
                while d.weekday() >= 5:
                    d += timedelta(days=1)
                nxt = f"{d:%Y-%m-%d}"
            lo, hi = math.floor(g["low"].min()) - 2, math.ceil(g["high"].max()) + 2
            syms = [f"{sym}{pd.Timestamp(e):%y%m%d}{cp}{K * 1000:08d}" for e in (day, nxt) for cp in "CP" for K in range(lo, hi + 1)]
            start = pd.Timestamp(day).tz_localize(NY) + pd.Timedelta(hours=9, minutes=30)
            stop = start + pd.Timedelta(minutes=391)
            out = {}
            for k0 in range(0, len(syms), 60):
                res = None
                for attempt in range(5):
                    try:
                        res = oc.get_option_bars(OptionBarsRequest(symbol_or_symbols=syms[k0:k0 + 60], timeframe=TimeFrame.Minute,
                                                                   start=start.tz_convert("UTC").to_pydatetime(),
                                                                   end=stop.tz_convert("UTC").to_pydatetime())).df
                        break
                    except Exception as e:  # noqa: BLE001
                        print(f"  {sym} {day} failed ({attempt + 1}/5): {str(e)[:200]}", flush=True)
                        time.sleep(5 * (attempt + 1))
                if res is None or not len(res) or not isinstance(res.index, pd.MultiIndex):
                    continue
                for s_, b in res.groupby(level=0):
                    b = b.droplevel(0)
                    b.index = b.index.tz_convert(NY)
                    i = ((b.index - start) / pd.Timedelta(minutes=1)).astype(int)
                    rows = [[int(k), round(float(r.open), 2), round(float(r.high), 2), round(float(r.low), 2), round(float(r.close), 2), int(r.volume)]
                            for k, r in zip(i, b.itertuples()) if 0 <= k < 390]
                    if rows:
                        out[s_] = rows
            with gzip.open(f"{out_dir}/{day}.json.gz", "wt") as f:
                json.dump({"day": day, "exp1": nxt, "opt": out}, f, separators=(",", ":"))
            print(f"{sym} {day}: {len(out)} of {len(syms)} contracts  ({time.time() - t0:.0f}s)", flush=True)
            if time.time() - t0 > 160 * 60:
                print("Time limit reached; run it again to continue.", flush=True)
                return


if __name__ == "__main__":
    main()
