"""Daily price pull for the Edge Stress Test (data only, no orders).
After the close, saves SPY 1-minute bars and every nearby 0DTE call/put's 1-minute bars to results/bars_<day>.json.
Run by .github/workflows/daily_bars.yml every weekday. BARS_DAYS=2026-11-12,2026-11-13 pulls other days."""
import math
import os
import sys
import json
import time
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd

NY = ZoneInfo("America/New_York")
OUT = "results"


def fetch_1m(symbol, start, end):
    """1-minute bars 4:00-20:00 ET from Alpaca (SIP first, IEX if the plan does not allow SIP)."""
    from alpaca.data.enums import Adjustment, DataFeed
    from alpaca.data.historical import StockHistoricalDataClient
    from alpaca.data.requests import StockBarsRequest
    from alpaca.data.timeframe import TimeFrame

    key, sec = os.getenv("ALPACA_KEY", "").strip(), os.getenv("ALPACA_SECRET", "").strip()
    if not key or not sec:
        sys.exit("ALPACA_KEY / ALPACA_SECRET are missing. Add them in Settings > Secrets and variables > Actions.")
    client = StockHistoricalDataClient(key, sec)
    last_err = None
    for feed in (DataFeed.SIP, DataFeed.IEX):
        try:
            parts = []
            cur = start
            while cur < end:
                nxt = min(cur + timedelta(days=120), end)
                req = StockBarsRequest(symbol_or_symbols=symbol, timeframe=TimeFrame.Minute,
                                       start=cur, end=nxt, feed=feed, adjustment=Adjustment.SPLIT)
                df = client.get_stock_bars(req).df
                if len(df):
                    parts.append(df)
                print(f"  {symbol} {feed.value}: {cur:%Y-%m-%d} -> {nxt:%Y-%m-%d}  {len(df):,} bars", flush=True)
                cur = nxt
            if not parts:
                raise RuntimeError("no bars returned")
            df = pd.concat(parts)
            if isinstance(df.index, pd.MultiIndex):
                df = df.reset_index(level=0, drop=True)
            df = df[~df.index.duplicated()].sort_index()
            df.index = df.index.tz_convert(NY)
            return df[["open", "high", "low", "close", "volume"]].astype(float), feed.value
        except Exception as e:  # noqa: BLE001
            last_err = e
            msg = str(e)
            print(f"  {symbol}: feed {feed.value} failed: {msg[:300]}", flush=True)
            if "401" in msg or "unauthorized" in msg.lower():
                break  # bad keys - the other feed will fail the same way
    sys.exit(f"Could not download {symbol}: {last_err}\n"
             "If it says 401 / unauthorized / forbidden: the API keys in GitHub Secrets are wrong or expired. "
             "Make new PAPER keys in Alpaca and paste them into ALPACA_KEY and ALPACA_SECRET again.")




def dots_occ(day, cp, k):
    return f"SPY{day:%y%m%d}{cp}{int(round(k * 1000)):08d}"


def dots_fetch_options(oc, contracts, day):
    """Real 1-minute OHLC for each contract on `day`, as arrays of 390 (NaN = no trade that minute)."""
    from alpaca.data.requests import OptionBarsRequest
    from alpaca.data.timeframe import TimeFrame
    start = pd.Timestamp(day, tz=NY) + pd.Timedelta(hours=9, minutes=30)
    end = start + pd.Timedelta(minutes=390)
    out = {}
    contracts = sorted(set(contracts))
    for k0 in range(0, len(contracts), 60):
        chunk = contracts[k0:k0 + 60]
        df = None
        for attempt in range(4):
            try:
                df = oc.get_option_bars(OptionBarsRequest(symbol_or_symbols=chunk, timeframe=TimeFrame.Minute,
                                                          start=start.tz_convert("UTC").to_pydatetime(),
                                                          end=end.tz_convert("UTC").to_pydatetime())).df
                break
            except Exception as e:  # noqa: BLE001
                print(f"  option bars {day} retry {attempt + 1}: {str(e)[:120]}", flush=True)
                time.sleep(4 * (attempt + 1))
        if df is None or not len(df) or not isinstance(df.index, pd.MultiIndex):
            continue
        for sym, g in df.groupby(level=0):
            g = g.droplevel(0)
            ix = g.index.tz_convert(NY)
            mm = (ix.hour * 60 + ix.minute - 570).to_numpy()
            ok = (mm >= 0) & (mm < 390)
            rec = {col: np.full(390, np.nan) for col in ("open", "high", "low", "close")}
            for col in rec:
                rec[col][mm[ok]] = g[col].to_numpy()[ok]
            out[sym] = rec
    return out


def main():
    from alpaca.data.historical import OptionHistoricalDataClient
    os.makedirs(OUT, exist_ok=True)
    days = [d.strip() for d in (os.getenv("BARS_DAYS", "") or datetime.now(NY).strftime("%Y-%m-%d")).split(",") if d.strip()]
    oc = OptionHistoricalDataClient(os.getenv("ALPACA_KEY", "").strip(), os.getenv("ALPACA_SECRET", "").strip())
    for ds in days:
        day = pd.Timestamp(ds).date()
        if day.weekday() >= 5:
            print(f"{ds}: weekend, skipped"); continue
        st = pd.Timestamp(ds, tz=NY) + pd.Timedelta(hours=9)
        df1, feed = fetch_1m("SPY", st.tz_convert("UTC").to_pydatetime(), (st + pd.Timedelta(hours=8)).tz_convert("UTC").to_pydatetime())
        g = df1[(df1.index.tz_convert(NY).date == day)]
        hm = g.index.tz_convert(NY).hour * 100 + g.index.tz_convert(NY).minute
        g = g[(hm >= 930) & (hm < 1600)]
        if len(g) < 300:
            print(f"{ds}: only {len(g)} SPY bars (holiday or half day?), skipped"); continue
        lo, hi = math.floor(g["low"].min()) - 2, math.ceil(g["high"].max()) + 2
        syms = [dots_occ(day, cp, k) for k in range(lo, hi + 1) for cp in ("C", "P")]
        opt = dots_fetch_options(oc, syms, day)
        out = {"day": ds, "feed": feed,
               "spy": [[ix.tz_convert(NY).isoformat(), float(r.open), float(r.high), float(r.low), float(r.close), float(getattr(r, "volume", 0) or 0)] for ix, r in g.iterrows()],
               "opt": {s: [[i, float(v["open"][i]), float(v["high"][i]), float(v["low"][i]), float(v["close"][i])] for i in range(390) if v["close"][i] > 0] for s, v in opt.items()}}
        with open(f"{OUT}/bars_{ds}.json", "w") as f:
            json.dump(out, f)
        print(f"{ds}: SPY {len(out['spy'])} bars, {len(out['opt'])} contracts, strikes {lo}-{hi}", flush=True)


if __name__ == "__main__":
    main()
