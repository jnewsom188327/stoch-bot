"""Older history for the out-of-sample check (data only, no orders).
1) SPY 1-minute bars Feb 2024 - Oct 2025 -> results/spy_1m_old.csv.gz
2) For each of those days, 1-minute bars of the SPY calls and puts near that day's range, expiring that day (0DTE) and
   the next trading day (1DTE) -> results/opt_old/<day>.json.gz.
Days already saved are skipped, so run it again until it says it is finished (each run stops itself after ~2h40m)."""
import os
from datetime import datetime, timedelta, timezone

import pandas as pd

import pull_opts
from bars_daily import fetch_1m

START, END = os.getenv("START", "2024-02-01"), os.getenv("END", "2025-11-01")
CSV = "results/spy_1m_old.csv.gz"

if not os.path.exists(CSV):
    df, feed = fetch_1m("SPY", datetime.fromisoformat(START).replace(tzinfo=timezone.utc),
                        datetime.fromisoformat(END).replace(tzinfo=timezone.utc))
    df = df.between_time("09:30", "15:59")
    df.index.name = "t"
    os.makedirs("results", exist_ok=True)
    df.to_csv(CSV, compression="gzip")
    print("SPY bars", len(df), feed, flush=True)

# reuse the option puller with the older file and folder
pull_opts.OUT = "results/opt_old"
pull_opts.START = START
_read = pd.read_csv
pd.read_csv = lambda p, *a, **k: _read(CSV if p == "results/spy_1m.csv.gz" else p, *a, **k)
pull_opts.main()
left = [d for d in sorted(set(_read(CSV)["t"].str[:10])) if not os.path.exists(f"results/opt_old/{d}.json.gz")]
print("FINISHED - all days saved" if not left else f"{len(left)} days left - run it again", flush=True)
