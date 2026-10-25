"""
Log-only intraday GEX (dealer gamma exposure) for SPY and QQQ.

Places no orders. Does not import the trading bots and does not call any order
endpoint. Keys are the same GitHub Actions secrets the other workflows use:
ALPACA_KEY and ALPACA_SECRET. They are sent only as request headers and are
never printed.

Hosts match alpaca-py as used by the other bots (TradingClient paper=True, and
the data clients):

  trading (paper): https://paper-api.alpaca.markets
  market data:     https://data.alpaca.markets

GET only:
  /v2/clock
  /v2/calendar
  /v2/options/contracts                         open interest, size, strike, type
  /v2/stocks/{symbol}/trades/latest             underlying price (IEX, like the bots)
  /v2/stocks/{symbol}/snapshot                  only if the latest trade is missing
  /v1beta1/options/snapshots/{underlying}       greeks, IV, quotes, trades

Sign convention (an assumption, see docs/GEX.md): dealers are long calls and
short puts. Call GEX is positive, put GEX is negative.

Dollar GEX per contract, for a 1% move in the underlying:

  sign * gamma * open_interest * size * spot^2 * 0.01

sign is +1 for a call and -1 for a put. size is the contract multiplier
(100 shares when the contract does not say otherwise).
"""

from __future__ import annotations

import argparse
import csv
import gzip
import io
import json
import math
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import date, datetime, time as dtime, timedelta, timezone
from zoneinfo import ZoneInfo

ET = ZoneInfo("America/New_York")

DATA_BASE = "https://data.alpaca.markets"
TRADE_BASE = "https://paper-api.alpaca.markets"

SIGN_CONVENTION = "dealer_long_calls_short_puts"
FLIP_METHOD = "cumulative_from_low_strike"
SHIFTED_FLIP_METHOD = "spot_shifted_bs_r0_q0"

# European BS fallback. Alpaca's own gamma is used whenever they send one.
BS_RATE = 0.0
BS_DIVIDEND = 0.0
YEAR_DAYS = 365.0
EXPIRY_HOUR = 16
EXPIRY_MINUTE = 0
T_FLOOR_SECONDS = 60.0
SHIFTED_IV_COVERAGE = 0.5

LEVEL_COLUMNS = [
    "timestamp_et",
    "timestamp_utc",
    "ticker",
    "spot",
    "spot_source",
    "net_gex_0dte",
    "net_gex_all",
    "net_gex_0dte_voladj",
    "net_gex_all_voladj",
    "gamma_flip_0dte",
    "gamma_flip_all",
    "gamma_flip_0dte_shifted",
    "gamma_flip_all_shifted",
    "call_wall_0dte",
    "call_wall_0dte_gex",
    "put_wall_0dte",
    "put_wall_0dte_gex",
    "call_wall_all",
    "call_wall_all_gex",
    "put_wall_all",
    "put_wall_all_gex",
    "gamma_flip_0dte_voladj",
    "call_wall_0dte_voladj",
    "put_wall_0dte_voladj",
    "dist_flip_0dte_pts",
    "dist_flip_0dte_pct",
    "dist_call_wall_0dte_pts",
    "dist_call_wall_0dte_pct",
    "dist_put_wall_0dte_pts",
    "dist_put_wall_0dte_pct",
    "dist_flip_all_pts",
    "dist_flip_all_pct",
    "dist_call_wall_all_pts",
    "dist_call_wall_all_pct",
    "dist_put_wall_all_pts",
    "dist_put_wall_all_pct",
    "top1_strike",
    "top1_abs_gex",
    "top1_dist_pts",
    "top1_dist_pct",
    "top2_strike",
    "top2_abs_gex",
    "top2_dist_pts",
    "top2_dist_pct",
    "top3_strike",
    "top3_abs_gex",
    "top3_dist_pts",
    "top3_dist_pct",
    "top_strikes_scope",
    "total_oi",
    "total_volume",
    "n_contracts",
    "n_0dte",
    "n_missing_greeks",
    "n_gamma_bs_fallback",
    "n_missing_oi",
    "expiries",
    "sign_convention",
    "flip_method",
    "shifted_flip_method",
    "strike_window_pct",
    "option_feed",
    "stock_feed",
    "chain_truncated",
]

STRIKE_COLUMNS = [
    "ticker",
    "timestamp_et",
    "timestamp_utc",
    "spot",
    "expiry",
    "dte_flag",
    "strike",
    "type",
    "symbol",
    "oi",
    "oi_date",
    "volume",
    "size",
    "gamma",
    "gamma_source",
    "iv",
    "iv_source",
    "mid",
    "t_years",
    "gex",
    "gex_voladj",
]

_PRICE_FIELDS = {
    "spot",
    "gamma_flip_0dte",
    "gamma_flip_all",
    "gamma_flip_0dte_shifted",
    "gamma_flip_all_shifted",
    "call_wall_0dte",
    "put_wall_0dte",
    "call_wall_all",
    "put_wall_all",
    "gamma_flip_0dte_voladj",
    "call_wall_0dte_voladj",
    "put_wall_0dte_voladj",
    "top1_strike",
    "top2_strike",
    "top3_strike",
}
_GEX_FIELDS = {
    "net_gex_0dte",
    "net_gex_all",
    "net_gex_0dte_voladj",
    "net_gex_all_voladj",
    "call_wall_0dte_gex",
    "put_wall_0dte_gex",
    "call_wall_all_gex",
    "put_wall_all_gex",
    "top1_abs_gex",
    "top2_abs_gex",
    "top3_abs_gex",
}
_DIST_FIELDS = {c for c in LEVEL_COLUMNS if c.startswith("dist_")}
_COUNT_FIELDS = {
    "total_oi",
    "total_volume",
    "n_contracts",
    "n_0dte",
    "n_missing_greeks",
    "n_gamma_bs_fallback",
    "n_missing_oi",
}

_extra_secrets: list[str] = []


def register_secrets(*values: str) -> None:
    for value in values:
        if value and len(value) >= 8 and value not in _extra_secrets:
            _extra_secrets.append(value)


def redact(text) -> str:
    out = str(text)
    found = list(_extra_secrets)
    for name in ("ALPACA_KEY", "ALPACA_SECRET"):
        value = os.getenv(name, "").strip()
        if len(value) >= 8 and value not in found:
            found.append(value)
    for secret in found:
        out = out.replace(secret, "[redacted]")
    return out


def now_et() -> datetime:
    return datetime.now(ET)


def log(msg) -> None:
    print(now_et().strftime("%H:%M:%S"), redact(msg), flush=True)


def as_et(moment: datetime) -> datetime:
    if moment.tzinfo is None:
        return moment.replace(tzinfo=ET)
    return moment.astimezone(ET)


def stamps(moment: datetime) -> tuple[str, str]:
    moment = as_et(moment).replace(microsecond=0)
    utc = moment.astimezone(timezone.utc)
    return moment.strftime("%Y-%m-%d %H:%M:%S"), utc.strftime("%Y-%m-%dT%H:%M:%SZ")


def parse_hhmm(value) -> int:
    text = str(value).strip()
    if ":" in text:
        hour, minute = text.split(":", 1)
        return int(hour) * 60 + int(minute)
    text = text.zfill(4)
    return int(text[:2]) * 60 + int(text[2:4])


def session_status(moment: datetime, clock: dict, calendar_rows) -> tuple[bool, str]:
    """Regular-hours gate. Weekend and the cash session window are checked here.

    Alpaca's clock is still required: is_open is true only during the regular
    session, including early closes, and false on holidays. The calendar row
    supplies that day's open and close so a half day ends when the exchange says.
    """
    moment = as_et(moment)
    if moment.weekday() >= 5:
        return False, "weekend"
    today = moment.date().isoformat()
    row = None
    for item in calendar_rows or []:
        if str(item.get("date")) == today:
            row = item
            break
    if row is None:
        return False, "holiday"
    opened = parse_hhmm(row.get("open"))
    closed = parse_hhmm(row.get("close"))
    minute_of_day = moment.hour * 60 + moment.minute
    if minute_of_day < opened:
        return False, "before the open"
    if minute_of_day >= closed:
        return False, "after the close"
    if not isinstance(clock, dict) or clock.get("is_open") is not True:
        return False, "clock closed"
    return True, "open"


def settings_from_env() -> dict:
    tickers = [part.strip().upper() for part in os.getenv("GEX_TICKERS", "SPY,QQQ").split(",") if part.strip()]
    return {
        "tickers": tickers or ["SPY", "QQQ"],
        "window": float(os.getenv("GEX_STRIKE_WINDOW_PCT", "0.10")),
        "extra": int(os.getenv("GEX_EXTRA_EXPIRIES", "2")),
        "option_feed": os.getenv("GEX_OPTION_FEED", "indicative").strip() or "indicative",
        "stock_feed": os.getenv("GEX_STOCK_FEED", "iex").strip() or "iex",
        "lookahead_days": int(os.getenv("GEX_EXPIRY_LOOKAHEAD_DAYS", "21")),
        "max_pages": int(os.getenv("GEX_MAX_PAGES", "8")),
    }


# ----- GEX math (no network) -----

def gex_dollars(gamma, oi, size, spot, right) -> float:
    """Signed dollar gamma for a 1% spot move. Calls positive, puts negative."""
    sign = 1.0 if right == "call" else -1.0
    return sign * float(gamma) * float(oi) * float(size) * float(spot) * float(spot) * 0.01


def norm_cdf(x: float) -> float:
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def norm_pdf(x: float) -> float:
    return math.exp(-0.5 * x * x) / math.sqrt(2.0 * math.pi)


def bs_d1(spot, strike, iv, t_years, rate=BS_RATE, div=BS_DIVIDEND) -> float:
    return (math.log(spot / strike) + (rate - div + 0.5 * iv * iv) * t_years) / (iv * math.sqrt(t_years))


def bs_gamma(spot, strike, iv, t_years, rate=BS_RATE, div=BS_DIVIDEND):
    """Black-Scholes gamma. Same number for a call and a put. r = q = 0 by default."""
    if spot <= 0 or strike <= 0 or iv <= 0 or t_years <= 0:
        return None
    if not all(math.isfinite(x) for x in (float(spot), float(strike), float(iv), float(t_years))):
        return None
    d1 = bs_d1(spot, strike, iv, t_years, rate, div)
    gamma = math.exp(-div * t_years) * norm_pdf(d1) / (spot * iv * math.sqrt(t_years))
    if not math.isfinite(gamma) or gamma <= 0:
        return None
    return gamma


def bs_price(right, spot, strike, iv, t_years, rate=BS_RATE, div=BS_DIVIDEND):
    if spot <= 0 or strike <= 0 or iv <= 0 or t_years <= 0:
        return None
    sqrt_t = math.sqrt(t_years)
    d1 = bs_d1(spot, strike, iv, t_years, rate, div)
    d2 = d1 - iv * sqrt_t
    call = math.exp(-div * t_years) * spot * norm_cdf(d1) - math.exp(-rate * t_years) * strike * norm_cdf(d2)
    if right == "call":
        price = call
    else:
        price = call - math.exp(-div * t_years) * spot + math.exp(-rate * t_years) * strike
    if not math.isfinite(price):
        return None
    return price


def imply_iv(right, spot, strike, price, t_years, rate=BS_RATE, div=BS_DIVIDEND):
    """Bisection IV from a mid price. None when the mid is below intrinsic or above 500% vol."""
    if price is None or price <= 0 or spot <= 0 or strike <= 0 or t_years <= 0:
        return None
    disc_s = math.exp(-div * t_years) * spot
    disc_k = math.exp(-rate * t_years) * strike
    intrinsic = max(disc_s - disc_k, 0.0) if right == "call" else max(disc_k - disc_s, 0.0)
    if price < intrinsic - 1e-6:
        return None
    lo, hi = 1e-4, 5.0
    price_hi = bs_price(right, spot, strike, hi, t_years, rate, div)
    if price_hi is None or price > price_hi + 1e-6:
        return None
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        quoted = bs_price(right, spot, strike, mid, t_years, rate, div)
        if quoted is None:
            return None
        if quoted > price:
            hi = mid
        else:
            lo = mid
    iv = 0.5 * (lo + hi)
    return iv if iv > 0 else None


def year_fraction(moment: datetime, expiry: date) -> float:
    """Time to 16:00 ET on the expiration date, as a 365-day year. Floor of one minute."""
    moment = as_et(moment)
    expiry_at = datetime(expiry.year, expiry.month, expiry.day, EXPIRY_HOUR, EXPIRY_MINUTE, tzinfo=ET)
    seconds = max((expiry_at - moment).total_seconds(), T_FLOOR_SECONDS)
    return seconds / (YEAR_DAYS * 24.0 * 3600.0)


def zero_crosses(xs, ys) -> list[float]:
    """Interpolated roots of a series. xs must be sorted ascending."""
    found = []
    for i in range(1, len(xs)):
        y0, y1 = ys[i - 1], ys[i]
        crossed = (y0 < 0 <= y1) or (y0 > 0 >= y1)
        if not crossed:
            continue
        if y1 == 0 or y0 == 0:
            found.append(float(xs[i] if y1 == 0 else xs[i - 1]))
        else:
            weight = abs(y0) / (abs(y0) + abs(y1))
            found.append(float(xs[i - 1]) + weight * (float(xs[i]) - float(xs[i - 1])))
    unique = []
    for value in found:
        if not unique or abs(unique[-1] - value) > 1e-9:
            unique.append(value)
    return unique


def pick_closest(levels, spot):
    if not levels:
        return None
    return min(levels, key=lambda level: (abs(level - spot), level))


def cumulative_flip(strike_net: dict, spot):
    """Zero-cross of GEX summed from the lowest strike up. Closest cross to spot wins."""
    items = sorted((float(k), float(v)) for k, v in strike_net.items())
    if len(items) < 2:
        return None
    xs = []
    ys = []
    running = 0.0
    for strike, gex in items:
        running += gex
        xs.append(strike)
        ys.append(running)
    return pick_closest(zero_crosses(xs, ys), spot)


def shifted_flip(rows, spot, gamma_fn=None):
    """Recompute net GEX at each strike as if spot were there. Needs IV on most of the OI.

    gamma_fn(hypothetical_spot, row) defaults to r=0, q=0 Black-Scholes. The reported
    flip is the zero of that net-GEX curve closest to the real spot.
    """
    if gamma_fn is None:
        def gamma_fn(hyp, row):
            return bs_gamma(hyp, row["strike"], row["iv"], row["t_years"])

    usable = []
    oi_all = 0.0
    oi_ok = 0.0
    for row in rows:
        oi = float(row.get("oi") or 0.0)
        oi_all += oi
        iv = row.get("iv")
        if iv and iv > 0 and oi > 0 and row.get("t_years"):
            oi_ok += oi
            usable.append(row)
    if oi_all <= 0 or oi_ok / oi_all < SHIFTED_IV_COVERAGE or len(usable) < 2:
        return None
    strikes = sorted({float(row["strike"]) for row in usable})
    if len(strikes) < 2:
        return None
    if len(strikes) * len(usable) > 2_000_000:
        return None
    xs = []
    ys = []
    for hyp in strikes:
        net = 0.0
        any_gamma = False
        for row in usable:
            gamma = gamma_fn(hyp, row)
            if gamma is None or gamma <= 0 or not math.isfinite(gamma):
                continue
            any_gamma = True
            net += gex_dollars(gamma, row["oi"], row["size"], hyp, row["right"])
        if not any_gamma:
            return None
        xs.append(hyp)
        ys.append(net)
    return pick_closest(zero_crosses(xs, ys), spot)


def _by_strike(rows, key: str) -> dict:
    out = {}
    for row in rows:
        value = row.get(key)
        if value is None:
            continue
        strike = float(row["strike"])
        out[strike] = out.get(strike, 0.0) + float(value)
    return out


def _side_by_strike(rows, right: str, key: str) -> dict:
    return _by_strike([row for row in rows if row["right"] == right], key)


def _sum_or_none(rows, key: str):
    values = [float(row[key]) for row in rows if row.get(key) is not None]
    if not values:
        return None
    return sum(values)


def _arg_best(levels: dict, spot, want_max: bool):
    items = [(strike, value) for strike, value in levels.items() if value != 0]
    if not items:
        return None, None
    if want_max:
        strike, value = sorted(items, key=lambda item: (-item[1], abs(item[0] - spot), item[0]))[0]
    else:
        strike, value = sorted(items, key=lambda item: (item[1], abs(item[0] - spot), item[0]))[0]
    return strike, value


def _distances(spot, level):
    if spot is None or level is None or spot == 0:
        return None, None
    points = float(level) - float(spot)
    return points, points / float(spot) * 100.0


def _top_strikes(strike_net: dict, spot, n=3):
    ranked = sorted(strike_net.items(), key=lambda item: (-abs(item[1]), abs(item[0] - spot), item[0]))
    out = []
    for strike, gex in ranked[:n]:
        points, pct = _distances(spot, strike)
        out.append((strike, abs(gex), points, pct))
    while len(out) < n:
        out.append((None, None, None, None))
    return out


def build_level_row(ticker, moment, spot, spot_source, rows, window, truncated, option_feed, stock_feed) -> dict:
    moment = as_et(moment)
    today = moment.date()
    ts_et, ts_utc = stamps(moment)
    dte_rows = []
    for row in rows:
        expiry = row["expiry"]
        if isinstance(expiry, str):
            expiry = datetime.strptime(expiry[:10], "%Y-%m-%d").date()
        if expiry == today:
            dte_rows.append(row)

    scope_all = _scope_metrics(rows, spot)
    scope_0d = _scope_metrics(dte_rows, spot)
    # Volume-adjusted walls and flip are stored for 0DTE, the book this is meant to sit next to.
    vol_flip = cumulative_flip(_by_strike(dte_rows, "gex_voladj"), spot)
    vol_call, _vol_call_gex = _arg_best(_side_by_strike(dte_rows, "call", "gex_voladj"), spot, True)
    vol_put, _vol_put_gex = _arg_best(_side_by_strike(dte_rows, "put", "gex_voladj"), spot, False)
    top = _top_strikes(_by_strike(rows, "gex"), spot, 3)

    expiries = []
    for row in rows:
        expiry = row["expiry"]
        text = expiry.isoformat() if hasattr(expiry, "isoformat") else str(expiry)[:10]
        if text not in expiries:
            expiries.append(text)
    expiries.sort()

    shifted_any = scope_0d["shifted"] is not None or scope_all["shifted"] is not None
    level = {
        "timestamp_et": ts_et,
        "timestamp_utc": ts_utc,
        "ticker": ticker,
        "spot": float(spot),
        "spot_source": spot_source,
        "net_gex_0dte": scope_0d["net"],
        "net_gex_all": scope_all["net"],
        "net_gex_0dte_voladj": scope_0d["net_vol"],
        "net_gex_all_voladj": scope_all["net_vol"],
        "gamma_flip_0dte": scope_0d["flip"],
        "gamma_flip_all": scope_all["flip"],
        "gamma_flip_0dte_shifted": scope_0d["shifted"],
        "gamma_flip_all_shifted": scope_all["shifted"],
        "call_wall_0dte": scope_0d["call_wall"],
        "call_wall_0dte_gex": scope_0d["call_wall_gex"],
        "put_wall_0dte": scope_0d["put_wall"],
        "put_wall_0dte_gex": scope_0d["put_wall_gex"],
        "call_wall_all": scope_all["call_wall"],
        "call_wall_all_gex": scope_all["call_wall_gex"],
        "put_wall_all": scope_all["put_wall"],
        "put_wall_all_gex": scope_all["put_wall_gex"],
        "gamma_flip_0dte_voladj": vol_flip,
        "call_wall_0dte_voladj": vol_call,
        "put_wall_0dte_voladj": vol_put,
        "top_strikes_scope": "all",
        "total_oi": float(sum(float(row.get("oi") or 0.0) for row in rows)),
        "total_volume": float(sum(float(row.get("volume") or 0.0) for row in rows)),
        "n_contracts": len(rows),
        "n_0dte": len(dte_rows),
        "n_missing_greeks": sum(1 for row in rows if row.get("gamma_source") != "alpaca"),
        "n_gamma_bs_fallback": sum(1 for row in rows if row.get("gamma_source") in ("bs_iv", "bs_mid")),
        "n_missing_oi": sum(1 for row in rows if row.get("missing_oi")),
        "expiries": ",".join(expiries),
        "sign_convention": SIGN_CONVENTION,
        "flip_method": FLIP_METHOD,
        "shifted_flip_method": SHIFTED_FLIP_METHOD if shifted_any else "",
        "strike_window_pct": float(window),
        "option_feed": option_feed,
        "stock_feed": stock_feed,
        "chain_truncated": "yes" if truncated else "no",
    }
    for name, value in (
        ("flip_0dte", scope_0d["flip"]),
        ("call_wall_0dte", scope_0d["call_wall"]),
        ("put_wall_0dte", scope_0d["put_wall"]),
        ("flip_all", scope_all["flip"]),
        ("call_wall_all", scope_all["call_wall"]),
        ("put_wall_all", scope_all["put_wall"]),
    ):
        points, pct = _distances(spot, value)
        level[f"dist_{name}_pts"] = points
        level[f"dist_{name}_pct"] = pct
    for index, (strike, abs_gex, points, pct) in enumerate(top, start=1):
        level[f"top{index}_strike"] = strike
        level[f"top{index}_abs_gex"] = abs_gex
        level[f"top{index}_dist_pts"] = points
        level[f"top{index}_dist_pct"] = pct
    return level


def _scope_metrics(rows, spot) -> dict:
    call_wall, call_gex = _arg_best(_side_by_strike(rows, "call", "gex"), spot, True)
    put_wall, put_gex = _arg_best(_side_by_strike(rows, "put", "gex"), spot, False)
    return {
        "net": _sum_or_none(rows, "gex"),
        "net_vol": _sum_or_none(rows, "gex_voladj"),
        "flip": cumulative_flip(_by_strike(rows, "gex"), spot),
        "call_wall": call_wall,
        "call_wall_gex": call_gex,
        "put_wall": put_wall,
        "put_wall_gex": put_gex,
        "shifted": shifted_flip(rows, spot),
    }


def select_expiries(dates, today: date, extra: int) -> list:
    """0DTE when today is an expiry, then the next expiry, then `extra` expiries after that."""
    clean = sorted({day for day in dates})
    chosen = []
    if today in clean:
        chosen.append(today)
    future = [day for day in clean if day > today]
    chosen.extend(future[: 1 + max(0, int(extra))])
    return chosen


# ----- Chain join -----

def positive_float(value):
    try:
        if value is None or value == "":
            return None
        number = float(value)
    except (TypeError, ValueError):
        return None
    if not math.isfinite(number) or number <= 0:
        return None
    return number


def parse_date(value) -> date:
    return datetime.strptime(str(value)[:10], "%Y-%m-%d").date()


def parse_oi(value) -> tuple[float, bool]:
    if value is None or value == "":
        return 0.0, True
    return float(value), False


def parse_size(size, multiplier) -> float:
    for value in (size, multiplier):
        if value is None or value == "":
            continue
        try:
            number = float(value)
        except (TypeError, ValueError):
            continue
        if number > 0:
            return number
    return 100.0


def parse_contract(raw: dict):
    symbol = str(raw.get("symbol") or "").strip()
    right = str(raw.get("type") or "").strip().lower()
    if right not in ("call", "put") or not symbol:
        return None
    try:
        strike = float(raw.get("strike_price"))
        expiry = parse_date(raw.get("expiration_date"))
    except (TypeError, ValueError):
        return None
    oi, missing_oi = parse_oi(raw.get("open_interest"))
    return {
        "symbol": symbol,
        "right": right,
        "strike": strike,
        "expiry": expiry,
        "oi": oi,
        "missing_oi": missing_oi,
        "oi_date": str(raw.get("open_interest_date") or ""),
        "size": parse_size(raw.get("size"), raw.get("multiplier")),
    }


def mid_from_snapshot(snap: dict):
    quote = snap.get("latestQuote") or {}
    try:
        bid = float(quote.get("bp") or 0)
        ask = float(quote.get("ap") or 0)
    except (TypeError, ValueError):
        bid, ask = 0.0, 0.0
    if bid > 0 and ask > 0:
        return (bid + ask) / 2.0
    trade = snap.get("latestTrade") or {}
    try:
        price = float(trade.get("p") or 0)
    except (TypeError, ValueError):
        price = 0.0
    if price > 0:
        return price
    return None


def daily_volume(snap: dict) -> float:
    bar = snap.get("dailyBar") or {}
    try:
        volume = float(bar.get("v")) if bar.get("v") not in (None, "") else 0.0
    except (TypeError, ValueError):
        return 0.0
    if not math.isfinite(volume) or volume < 0:
        return 0.0
    return volume


def enrich(contract: dict, snap: dict, spot: float, t_years: float) -> dict:
    """Attach gamma, IV, and signed GEX to one contract. Fallback gamma is flagged."""
    greeks = snap.get("greeks") or {}
    gamma = positive_float(greeks.get("gamma")) if isinstance(greeks, dict) else None
    iv = positive_float(snap.get("impliedVolatility"))
    iv_source = "alpaca" if iv is not None else "missing"
    gamma_source = "alpaca" if gamma is not None else "missing"
    mid = mid_from_snapshot(snap)
    if gamma is None:
        if iv is None and mid is not None:
            iv = imply_iv(contract["right"], spot, contract["strike"], mid, t_years)
            if iv is not None:
                iv_source = "mid"
        if iv is not None:
            gamma = bs_gamma(spot, contract["strike"], iv, t_years)
            gamma_source = ("bs_iv" if iv_source == "alpaca" else "bs_mid") if gamma is not None else "missing"
    gex = None
    gex_vol = None
    if gamma is not None:
        gex = gex_dollars(gamma, contract["oi"], contract["size"], spot, contract["right"])
        gex_vol = gex_dollars(
            gamma, contract["oi"] + daily_volume(snap), contract["size"], spot, contract["right"]
        )
    return {
        "symbol": contract["symbol"],
        "expiry": contract["expiry"],
        "strike": float(contract["strike"]),
        "right": contract["right"],
        "oi": float(contract["oi"]),
        "missing_oi": bool(contract["missing_oi"]),
        "oi_date": contract["oi_date"],
        "volume": daily_volume(snap),
        "size": float(contract["size"]),
        "gamma": gamma,
        "gamma_source": gamma_source,
        "iv": iv,
        "iv_source": iv_source,
        "mid": mid,
        "t_years": float(t_years),
        "gex": gex,
        "gex_voladj": gex_vol,
    }


def join_chain(contracts, snapshots, spot: float, moment: datetime) -> list:
    rows = []
    for contract in contracts:
        if contract is None:
            continue
        snap = snapshots.get(contract["symbol"]) or {}
        rows.append(enrich(contract, snap, spot, year_fraction(moment, contract["expiry"])))
    rows.sort(key=lambda row: (row["expiry"], row["strike"], 0 if row["right"] == "call" else 1))
    return rows


def strike_output(ticker, moment, spot, row) -> dict:
    ts_et, ts_utc = stamps(moment)
    expiry = row["expiry"]
    expiry_text = expiry.isoformat() if hasattr(expiry, "isoformat") else str(expiry)[:10]
    return {
        "ticker": ticker,
        "timestamp_et": ts_et,
        "timestamp_utc": ts_utc,
        "spot": float(spot),
        "expiry": expiry_text,
        "dte_flag": "0dte" if expiry_text == ts_et[:10] else "other",
        "strike": float(row["strike"]),
        "type": row["right"],
        "symbol": row["symbol"],
        "oi": float(row["oi"]),
        "oi_date": row.get("oi_date") or "",
        "volume": float(row["volume"]),
        "size": float(row["size"]),
        "gamma": row.get("gamma"),
        "gamma_source": row.get("gamma_source") or "",
        "iv": row.get("iv"),
        "iv_source": row.get("iv_source") or "",
        "mid": row.get("mid"),
        "t_years": row.get("t_years"),
        "gex": row.get("gex"),
        "gex_voladj": row.get("gex_voladj"),
    }


def pack(ticker, moment, spot, spot_source, rows, window, truncated, option_feed, stock_feed):
    level = build_level_row(
        ticker, moment, spot, spot_source, rows, window, truncated, option_feed, stock_feed
    )
    strikes = [strike_output(ticker, moment, spot, row) for row in rows]
    return level, strikes


# ----- Text -----

def money(value) -> str:
    if value is None or value == "":
        return ""
    number = float(value)
    if not math.isfinite(number):
        return ""
    sign = "-" if number < 0 else ""
    magnitude = abs(number)
    if magnitude >= 1e9:
        return f"{sign}${magnitude / 1e9:.2f}B"
    if magnitude >= 1e6:
        return f"{sign}${magnitude / 1e6:.2f}M"
    if magnitude >= 1e3:
        return f"{sign}${magnitude / 1e3:.2f}K"
    return f"{sign}${magnitude:.2f}"


def displayed_levels(row):
    """0DTE flip and walls when that expiry was in the snapshot, otherwise all-expiry."""
    if (row.get("n_0dte") or 0) > 0:
        return row.get("gamma_flip_0dte"), row.get("call_wall_0dte"), row.get("put_wall_0dte"), "0DTE"
    return row.get("gamma_flip_all"), row.get("call_wall_all"), row.get("put_wall_all"), "all-expiry"


def reading_line(row) -> str:
    ticker = row["ticker"]
    spot = row.get("spot")
    flip, call_wall, put_wall, label = displayed_levels(row)
    if not spot:
        return f"{ticker}: no spot."
    if flip is None:
        where = f"no {label} gamma flip (cumulative GEX did not cross zero)"
    else:
        gap = float(spot) - float(flip)
        points = abs(gap)
        pct = points / float(spot) * 100.0
        if points < 1e-9:
            where = f"spot on the {label} flip ({float(flip):.2f})"
        elif gap > 0:
            where = f"spot above the {label} flip by {points:.2f} pts ({pct:.2f}%)"
        else:
            where = f"spot below the {label} flip by {points:.2f} pts ({pct:.2f}%)"
    walls = []
    if call_wall is not None:
        walls.append(("call wall", float(call_wall), abs(float(spot) - float(call_wall))))
    if put_wall is not None:
        walls.append(("put wall", float(put_wall), abs(float(spot) - float(put_wall))))
    if not walls:
        wall_text = "no call or put wall"
    else:
        walls.sort(key=lambda item: (item[2], 0 if item[0] == "call wall" else 1))
        if len(walls) == 2 and abs(walls[0][2] - walls[1][2]) <= 1e-6:
            dist = walls[0][2]
            wall_text = (
                f"the call wall and the put wall are the same distance, "
                f"{dist:.2f} pts ({dist / float(spot) * 100.0:.2f}%) away"
            )
        else:
            name, level, dist = walls[0]
            wall_text = (
                f"nearest wall is the {name} at {level:.2f}, "
                f"{dist:.2f} pts ({dist / float(spot) * 100.0:.2f}%) away"
            )
    return f"{ticker}: {where}; {wall_text}."


def _fmt_px(value) -> str:
    if value is None or value == "":
        return ""
    return f"{float(value):.2f}"


def _top_line(row) -> str:
    bits = []
    for index in (1, 2, 3):
        strike = row.get(f"top{index}_strike")
        gex = row.get(f"top{index}_abs_gex")
        if strike is None:
            continue
        bits.append(f"{float(strike):.2f} ({money(gex)})")
    if not bits:
        return ""
    return f"{row['ticker']} top |GEX| strikes: " + ", ".join(bits) + "."


def render_markdown(level_rows) -> str:
    if not level_rows:
        return "# GEX latest\n\nNo snapshot.\n"
    lines = [
        "# GEX latest",
        "",
        f"{level_rows[0]['timestamp_et']} ET. Log only. This run places no orders.",
        "",
        "Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). "
        "Dollar GEX is the hedge notional for a 1% move in the underlying. "
        "Open interest is the overnight print, so this is an estimate.",
        "",
    ]
    for row in level_rows:
        lines.append(reading_line(row))
    lines.append("")
    for row in level_rows:
        extra = _top_line(row)
        if extra:
            lines.append(extra)
    lines.append("")
    headers = ["", *[row["ticker"] for row in level_rows]]

    def cells(label, getter):
        return [label, *[getter(row) for row in level_rows]]

    table = [
        cells("Spot", lambda row: _fmt_px(row.get("spot"))),
        cells("0DTE flip", lambda row: _fmt_px(row.get("gamma_flip_0dte"))),
        cells("All-expiry flip", lambda row: _fmt_px(row.get("gamma_flip_all"))),
        cells("0DTE call wall", lambda row: _fmt_px(row.get("call_wall_0dte"))),
        cells("0DTE put wall", lambda row: _fmt_px(row.get("put_wall_0dte"))),
        cells("Net GEX 0DTE", lambda row: money(row.get("net_gex_0dte"))),
        cells("Net GEX all", lambda row: money(row.get("net_gex_all"))),
        cells("Vol-adj net 0DTE", lambda row: money(row.get("net_gex_0dte_voladj"))),
        cells("Vol-adj net all", lambda row: money(row.get("net_gex_all_voladj"))),
        cells("Missing greeks", lambda row: f"{int(row.get('n_missing_greeks') or 0)}/{int(row.get('n_contracts') or 0)}"),
        cells("OI used", lambda row: f"{float(row['total_oi']):.0f}" if row.get("total_oi") is not None else ""),
    ]
    lines.append("| " + " | ".join(headers) + " |")
    lines.append("|" + "|".join(["---"] + ["---:"] * (len(headers) - 1)) + "|")
    for table_row in table:
        lines.append("| " + " | ".join(table_row) + " |")
    lines.append("")
    lines.append(
        "The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. "
        "CSV distances are level minus spot: positive means the level is above spot."
    )
    lines.append("")
    lines.append("Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.")
    lines.append("")
    return "\n".join(lines)


def pine_num(value) -> str:
    if value is None or value == "":
        return "0.0"
    text = f"{float(value):.4f}".rstrip("0").rstrip(".")
    if "." not in text:
        text += ".0"
    return text


def render_pine(level_rows) -> str:
    by_ticker = {row["ticker"]: row for row in level_rows}
    timestamp = level_rows[0]["timestamp_et"] if level_rows else ""

    def levels_for(ticker):
        row = by_ticker.get(ticker)
        if not row:
            return None, None, None
        flip, call_wall, put_wall, _label = displayed_levels(row)
        return flip, call_wall, put_wall

    spy_flip, spy_call, spy_put = levels_for("SPY")
    qqq_flip, qqq_call, qqq_put = levels_for("QQQ")
    lines = [
        "//@version=6",
        f"// GEX levels captured {timestamp} ET. Paste onto a SPY or QQQ chart.",
        "// Horizontal lines are the 0DTE gamma flip, call wall, and put wall.",
        "// Falls back to all-expiry levels when that snapshot had no 0DTE contracts.",
        "// Convention: dealers long calls, short puts. Not an order signal.",
        'indicator("GEX flip and walls", overlay=true)',
        f'spyFlip = input.float({pine_num(spy_flip)}, "SPY gamma flip")',
        f'spyCall = input.float({pine_num(spy_call)}, "SPY call wall")',
        f'spyPut = input.float({pine_num(spy_put)}, "SPY put wall")',
        f'qqqFlip = input.float({pine_num(qqq_flip)}, "QQQ gamma flip")',
        f'qqqCall = input.float({pine_num(qqq_call)}, "QQQ call wall")',
        f'qqqPut = input.float({pine_num(qqq_put)}, "QQQ put wall")',
        'isSpy = syminfo.ticker == "SPY"',
        'isQqq = syminfo.ticker == "QQQ"',
        "flip = isSpy ? spyFlip : isQqq ? qqqFlip : na",
        "callW = isSpy ? spyCall : isQqq ? qqqCall : na",
        "putW = isSpy ? spyPut : isQqq ? qqqPut : na",
        'plot(flip > 0 ? flip : na, "Gamma flip", color=color.orange, linewidth=2)',
        'plot(callW > 0 ? callW : na, "Call wall", color=color.teal, linewidth=1)',
        'plot(putW > 0 ? putW : na, "Put wall", color=color.red, linewidth=1)',
        "",
    ]
    return "\n".join(lines)


# ----- Files -----

def _fnum(value, digits: int) -> str:
    if value is None or value == "":
        return ""
    number = float(value)
    if not math.isfinite(number):
        return ""
    return f"{number:.{digits}f}"


def format_level(row: dict) -> dict:
    out = {}
    for column in LEVEL_COLUMNS:
        value = row.get(column, "")
        if column in _PRICE_FIELDS or column in _DIST_FIELDS or column == "strike_window_pct":
            out[column] = _fnum(value, 4)
        elif column in _GEX_FIELDS:
            out[column] = _fnum(value, 2)
        elif column in _COUNT_FIELDS:
            out[column] = "" if value is None or value == "" else str(int(round(float(value))))
        else:
            out[column] = "" if value is None else str(value)
    return out


def format_strike(row: dict) -> dict:
    out = {}
    for column in STRIKE_COLUMNS:
        value = row.get(column, "")
        if column in ("spot", "strike", "mid"):
            out[column] = _fnum(value, 4)
        elif column in ("oi", "volume", "size"):
            out[column] = _fnum(value, 0)
        elif column == "gamma":
            out[column] = _fnum(value, 8)
        elif column == "iv":
            out[column] = _fnum(value, 6)
        elif column == "t_years":
            out[column] = _fnum(value, 8)
        elif column in ("gex", "gex_voladj"):
            out[column] = _fnum(value, 2)
        else:
            out[column] = "" if value is None else str(value)
    return out


def _append_dict_rows(path, fieldnames, rows, key_fields):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    fresh_file = (not os.path.exists(path)) or os.path.getsize(path) == 0
    seen = set()
    if not fresh_file:
        with open(path, newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            if list(reader.fieldnames or []) != list(fieldnames):
                raise RuntimeError(f"{path} header does not match this logger. Refusing to append.")
            for record in reader:
                seen.add(tuple(record.get(field) for field in key_fields))
    fresh = [row for row in rows if tuple(row.get(field) for field in key_fields) not in seen]
    if not fresh and not fresh_file:
        return 0
    with open(path, "a", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n", extrasaction="ignore")
        if fresh_file:
            writer.writeheader()
        for row in fresh:
            writer.writerow(row)
    return len(fresh)


def _gzip_member(text: str) -> bytes:
    return gzip.compress(text.encode("utf-8"))


def append_strikes(path, formatted_rows):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    fresh_file = (not os.path.exists(path)) or os.path.getsize(path) == 0
    if not fresh_file:
        with gzip.open(path, "rt", newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            if list(reader.fieldnames or []) != list(STRIKE_COLUMNS):
                raise RuntimeError(f"{path} header does not match this logger. Refusing to append.")
            seen = {(record.get("ticker"), record.get("timestamp_et")) for record in reader}
        formatted_rows = [row for row in formatted_rows if (row["ticker"], row["timestamp_et"]) not in seen]
        if not formatted_rows:
            return 0
    buffer = io.StringIO()
    writer = csv.DictWriter(buffer, fieldnames=STRIKE_COLUMNS, lineterminator="\n", extrasaction="ignore")
    if fresh_file:
        writer.writeheader()
    for row in formatted_rows:
        writer.writerow(row)
    mode = "wb" if fresh_file else "ab"
    with open(path, mode) as handle:
        handle.write(_gzip_member(buffer.getvalue()))
    return len(formatted_rows)


def materialize(payload: dict, out_dir: str) -> None:
    os.makedirs(out_dir, exist_ok=True)
    level_rows = payload.get("level_rows") or []
    strike_rows = payload.get("strike_rows") or []
    formatted_levels = [format_level(row) for row in level_rows]
    _append_dict_rows(
        os.path.join(out_dir, "gex_levels.csv"),
        LEVEL_COLUMNS,
        formatted_levels,
        ("ticker", "timestamp_et"),
    )
    by_day = {}
    for row in strike_rows:
        formatted = format_strike(row)
        by_day.setdefault(formatted["timestamp_et"][:10], []).append(formatted)
    for day, rows in by_day.items():
        append_strikes(os.path.join(out_dir, f"gex_strikes_{day}.csv.gz"), rows)
    markdown = render_markdown(level_rows)
    pine = render_pine(level_rows)
    with open(os.path.join(out_dir, "GEX_LATEST.md"), "w", encoding="utf-8") as handle:
        handle.write(markdown)
    with open(os.path.join(out_dir, "GEX_PINE_SNIPPET.txt"), "w", encoding="utf-8") as handle:
        handle.write(pine)


def write_outputs(out_dir: str, payload: dict) -> None:
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "last_run.json"), "w", encoding="utf-8") as handle:
        json.dump(payload, handle)
    materialize(payload, out_dir)


def parse_level_csv_row(row: dict) -> dict:
    parsed = dict(row)
    for column in list(_PRICE_FIELDS | _GEX_FIELDS | _DIST_FIELDS | _COUNT_FIELDS | {"strike_window_pct"}):
        text = (row.get(column) or "").strip()
        if text == "":
            parsed[column] = None
        elif column in _COUNT_FIELDS:
            parsed[column] = int(float(text))
        else:
            parsed[column] = float(text)
    return parsed


def latest_levels_from_csv(path: str) -> list:
    with open(path, newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        return []
    latest = max(row["timestamp_et"] for row in rows)
    chosen = {}
    for row in rows:
        if row["timestamp_et"] == latest:
            chosen[row["ticker"]] = parse_level_csv_row(row)
    order = [ticker for ticker in ("SPY", "QQQ") if ticker in chosen]
    order += [ticker for ticker in chosen if ticker not in order]
    return [chosen[ticker] for ticker in order]


def pine_from_csv(path: str) -> str:
    return render_pine(latest_levels_from_csv(path))


# ----- Alpaca (GET only) -----

def build_url(base: str, path: str, params: dict) -> str:
    clean = {key: value for key, value in params.items() if value is not None}
    query = urllib.parse.urlencode(clean)
    return base.rstrip("/") + path + ("?" + query if query else "")


def with_query(url: str, extra: dict) -> str:
    parts = urllib.parse.urlsplit(url)
    query = [(key, value) for key, value in urllib.parse.parse_qsl(parts.query, keep_blank_values=True) if key not in extra]
    query.extend(extra.items())
    return urllib.parse.urlunsplit((parts.scheme, parts.netloc, parts.path, urllib.parse.urlencode(query), ""))


def path_only(url: str) -> str:
    return urllib.parse.urlsplit(url).path


def urllib_transport(url, headers, timeout):
    request = urllib.request.Request(url, headers=headers, method="GET")
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            body = response.read().decode("utf-8", errors="replace")
            return response.status, {key: value for key, value in response.headers.items()}, body
    except urllib.error.HTTPError as error:
        body = error.read().decode("utf-8", errors="replace")
        return error.code, {key: value for key, value in error.headers.items()}, body


class AlpacaClient:
    """Read-only Alpaca client. There is no order method on purpose."""

    def __init__(self, key, secret, data_base=DATA_BASE, trade_base=TRADE_BASE,
                 option_feed="indicative", stock_feed="iex", transport=None,
                 sleep_fn=None, max_pages=8, timeout=20):
        self.key = key
        self.secret = secret
        register_secrets(key, secret)
        self.data_base = data_base.rstrip("/")
        self.trade_base = trade_base.rstrip("/")
        self.option_feed = option_feed
        self.stock_feed = stock_feed
        self.transport = transport or urllib_transport
        self.sleep_fn = sleep_fn or time.sleep
        self.max_pages = max_pages
        self.timeout = timeout

    def _headers(self) -> dict:
        return {
            "APCA-API-KEY-ID": self.key,
            "APCA-API-SECRET-KEY": self.secret,
            "Accept": "application/json",
        }

    def _retry_wait(self, headers, attempt: int) -> float:
        raw = None
        if isinstance(headers, dict):
            raw = headers.get("Retry-After", headers.get("retry-after"))
        try:
            wait = float(raw)
        except (TypeError, ValueError):
            wait = float(2 ** attempt)
        return min(max(wait, 0.0), 30.0)

    def _get(self, url: str):
        last_status = None
        for attempt in range(4):
            try:
                status, headers, body = self.transport(url, self._headers(), self.timeout)
            except Exception as error:
                raise RuntimeError(redact(f"request failed for {path_only(url)}: {error}")) from None
            last_status = status
            if status == 429 or 500 <= status <= 599:
                wait = self._retry_wait(headers, attempt)
                log(f"HTTP {status} on {path_only(url)}, retry in {wait:.0f}s")
                self.sleep_fn(wait)
                continue
            if status >= 400:
                snippet = redact(body[:300] if body else "")
                raise RuntimeError(redact(f"HTTP {status} on {path_only(url)}: {snippet}"))
            try:
                return json.loads(body)
            except json.JSONDecodeError:
                raise RuntimeError(f"non-JSON response on {path_only(url)}") from None
        raise RuntimeError(f"giving up after retries on {path_only(url)} (last HTTP {last_status})")

    def _pages(self, url: str, on_page) -> bool:
        token = None
        pages = 0
        while pages < self.max_pages:
            page_url = url if not token else with_query(url, {"page_token": token})
            data = self._get(page_url)
            pages += 1
            on_page(data)
            token = data.get("next_page_token") or data.get("nextPageToken")
            if not token:
                return False
        log(f"stopped after {self.max_pages} pages for {path_only(url)}")
        return True

    def clock(self) -> dict:
        return self._get(self.trade_base + "/v2/clock")

    def calendar(self, day: date):
        url = build_url(self.trade_base, "/v2/calendar", {"start": day.isoformat(), "end": day.isoformat()})
        data = self._get(url)
        if isinstance(data, list):
            return data
        return []

    def latest_price(self, symbol: str):
        quoted = urllib.parse.quote(symbol, safe="")
        trade_url = build_url(
            self.data_base, f"/v2/stocks/{quoted}/trades/latest", {"feed": self.stock_feed}
        )
        try:
            data = self._get(trade_url)
            price = float((data.get("trade") or {}).get("p") or 0)
            if price > 0:
                return price, "trade"
        except Exception as error:
            log(f"{symbol} latest trade unavailable ({error})")
        snap_url = build_url(self.data_base, f"/v2/stocks/{quoted}/snapshot", {"feed": self.stock_feed})
        data = self._get(snap_url)
        trade = (data.get("latestTrade") or {}).get("p")
        if trade and float(trade) > 0:
            return float(trade), "snapshot_trade"
        minute = (data.get("minuteBar") or {}).get("c")
        if minute and float(minute) > 0:
            return float(minute), "snapshot_minute"
        quote = data.get("latestQuote") or {}
        bid = float(quote.get("bp") or 0)
        ask = float(quote.get("ap") or 0)
        if bid > 0 and ask > 0:
            return (bid + ask) / 2.0, "snapshot_quote_mid"
        raise RuntimeError(f"no price for {symbol}")

    def contracts(self, symbol, exp_gte: date, exp_lte: date, strike_gte: float, strike_lte: float):
        url = build_url(self.trade_base, "/v2/options/contracts", {
            "underlying_symbols": symbol,
            "status": "active",
            "expiration_date_gte": exp_gte.isoformat(),
            "expiration_date_lte": exp_lte.isoformat(),
            "strike_price_gte": f"{strike_gte:.4f}",
            "strike_price_lte": f"{strike_lte:.4f}",
            "limit": "1000",
        })
        found = []

        def on_page(data):
            for raw in data.get("option_contracts") or []:
                parsed = parse_contract(raw)
                if parsed:
                    found.append(parsed)

        truncated = self._pages(url, on_page)
        return found, truncated

    def snapshots(self, symbol, exp_gte: date, exp_lte: date, strike_gte: float, strike_lte: float):
        quoted = urllib.parse.quote(symbol, safe="")
        url = build_url(self.data_base, f"/v1beta1/options/snapshots/{quoted}", {
            "feed": self.option_feed,
            "limit": "1000",
            "expiration_date_gte": exp_gte.isoformat(),
            "expiration_date_lte": exp_lte.isoformat(),
            "strike_price_gte": f"{strike_gte:.4f}",
            "strike_price_lte": f"{strike_lte:.4f}",
        })
        found = {}

        def on_page(data):
            found.update(data.get("snapshots") or {})

        truncated = self._pages(url, on_page)
        return found, truncated


def collect_live(client: AlpacaClient, moment: datetime, settings: dict):
    moment = as_et(moment).replace(microsecond=0)
    if moment.weekday() >= 5:
        log("Market closed (weekend). Exiting.")
        return None
    open_now, reason = session_status(moment, client.clock(), client.calendar(moment.date()))
    if not open_now:
        log(f"Market closed ({reason}). Exiting.")
        return None
    today = moment.date()
    exp_lte = today + timedelta(days=settings["lookahead_days"])
    level_rows = []
    strike_rows = []
    for ticker in settings["tickers"]:
        try:
            spot, source = client.latest_price(ticker)
        except Exception as error:
            log(f"{ticker} price failed: {error}")
            continue
        if spot <= 0:
            log(f"{ticker} price ignored")
            continue
        lo = spot * (1.0 - settings["window"])
        hi = spot * (1.0 + settings["window"])
        try:
            contracts, trunc_contracts = client.contracts(ticker, today, exp_lte, lo, hi)
        except Exception as error:
            log(f"{ticker} contracts failed: {error}")
            continue
        chosen = select_expiries([contract["expiry"] for contract in contracts], today, settings["extra"])
        chosen_set = set(chosen)
        contracts = [
            contract for contract in contracts
            if contract["expiry"] in chosen_set and lo - 1e-6 <= contract["strike"] <= hi + 1e-6
        ]
        snapshots = {}
        trunc_snaps = False
        if contracts and chosen:
            try:
                snapshots, trunc_snaps = client.snapshots(ticker, min(chosen), max(chosen), lo, hi)
            except Exception as error:
                log(f"{ticker} snapshots failed: {error}")
                continue
        rows = join_chain(contracts, snapshots, spot, moment)
        names = ",".join(day.isoformat() for day in chosen) or "none"
        log(f"{ticker} spot {spot:.2f} ({source}) contracts {len(rows)} expiries {names}")
        level, strikes = pack(
            ticker, moment, spot, source, rows, settings["window"],
            trunc_contracts or trunc_snaps, settings["option_feed"], settings["stock_feed"],
        )
        level_rows.append(level)
        strike_rows.extend(strikes)
    if not level_rows:
        raise RuntimeError("no ticker could be recorded")
    return {"level_rows": level_rows, "strike_rows": strike_rows}


# ----- Demo / fixture -----

def _row_from_spec(symbol, expiry, strike, right, gamma, oi, spot, volume=0.0, size=100.0,
                   gamma_source="alpaca", iv=None, iv_source="missing", mid=None, t_years=1 / 365):
    gex = None if gamma is None else gex_dollars(gamma, oi, size, spot, right)
    gex_vol = None if gamma is None else gex_dollars(gamma, oi + volume, size, spot, right)
    return {
        "symbol": symbol,
        "expiry": expiry,
        "strike": float(strike),
        "right": right,
        "oi": float(oi),
        "missing_oi": False,
        "oi_date": "",
        "volume": float(volume),
        "size": float(size),
        "gamma": gamma,
        "gamma_source": gamma_source,
        "iv": iv,
        "iv_source": iv_source,
        "mid": mid,
        "t_years": t_years,
        "gex": gex,
        "gex_voladj": gex_vol,
    }


def spy_sample_rows(expiry: date, spot=100.0, volume_on_atm_call=0.0):
    """Hand-checkable 0DTE chain. Flip is 99.25, call wall 100, put wall 95, net 18900."""
    spec = [
        (90, "call", 0.001, 100),
        (90, "put", 0.002, 500),
        (95, "call", 0.002, 200),
        (95, "put", 0.003, 400),
        (100, "call", 0.01, 300),
        (100, "put", 0.01, 100),
        (105, "call", 0.004, 400),
        (105, "put", 0.002, 50),
        (110, "call", 0.001, 100),
        (110, "put", 0.001, 10),
    ]
    rows = []
    for strike, right, gamma, oi in spec:
        volume = volume_on_atm_call if strike == 100 and right == "call" else 0.0
        rows.append(_row_from_spec(
            f"SPY{expiry.strftime('%y%m%d')}{'C' if right == 'call' else 'P'}{int(strike * 1000):08d}",
            expiry, strike, right, gamma, oi, spot, volume=volume,
        ))
    return rows


def qqq_sample_rows(expiry: date, spot=50.0):
    spec = [
        (48, "put", 0.02, 100),
        (50, "call", 0.02, 200),
        (52, "call", 0.01, 50),
    ]
    rows = []
    for strike, right, gamma, oi in spec:
        rows.append(_row_from_spec(
            f"QQQ{expiry.strftime('%y%m%d')}{'C' if right == 'call' else 'P'}{int(strike * 1000):08d}",
            expiry, strike, right, gamma, oi, spot,
        ))
    return rows


def demo_payload() -> dict:
    moment = datetime(2026, 10, 23, 10, 30, tzinfo=ET)
    expiry = moment.date()
    parts = [("SPY", 100.0, spy_sample_rows(expiry)), ("QQQ", 50.0, qqq_sample_rows(expiry))]
    level_rows = []
    strike_rows = []
    for ticker, spot, rows in parts:
        level, strikes = pack(ticker, moment, spot, "fixture", rows, 0.10, False, "fixture", "fixture")
        level_rows.append(level)
        strike_rows.extend(strikes)
    return {"level_rows": level_rows, "strike_rows": strike_rows}


def payload_from_fixture(data: dict) -> dict:
    moment = as_et(datetime.fromisoformat(data["now_et"]))
    window = float(data.get("strike_window_pct", 0.10))
    level_rows = []
    strike_rows = []
    for ticker, part in data["tickers"].items():
        spot = float(part["spot"])
        contracts = [parse_contract(raw) for raw in part.get("contracts") or []]
        rows = join_chain(contracts, part.get("snapshots") or {}, spot, moment)
        level, strikes = pack(
            ticker, moment, spot, part.get("spot_source") or "fixture", rows, window, False, "fixture", "fixture"
        )
        level_rows.append(level)
        strike_rows.extend(strikes)
    if not level_rows:
        raise RuntimeError("fixture has no tickers")
    return {"level_rows": level_rows, "strike_rows": strike_rows}


# ----- CLI -----

def main(argv=None, client_factory=None, now=None) -> int:
    parser = argparse.ArgumentParser(description="Log-only intraday GEX for SPY and QQQ. Places no orders.")
    parser.add_argument("--dry-run", action="store_true", help="Built-in sample chain. No keys and no network.")
    parser.add_argument("--fixture", default="", help="JSON chain fixture. No keys and no network.")
    parser.add_argument("--out", default="results/gex", help="Directory for the CSVs, markdown, and Pine snippet.")
    parser.add_argument("--publish", default="", help="Merge this last_run.json into --out. No network.")
    parser.add_argument("--pine", action="store_true", help="Print a Pine v6 snippet from --out/gex_levels.csv.")
    args = parser.parse_args(argv)

    if args.publish:
        with open(args.publish, encoding="utf-8") as handle:
            payload = json.load(handle)
        materialize(payload, args.out)
        return 0
    if args.pine:
        path = os.path.join(args.out, "gex_levels.csv")
        sys.stdout.write(pine_from_csv(path))
        return 0
    if args.dry_run or args.fixture:
        if args.fixture:
            with open(args.fixture, encoding="utf-8") as handle:
                payload = payload_from_fixture(json.load(handle))
        else:
            payload = demo_payload()
        write_outputs(args.out, payload)
        log("dry run, no network, no orders")
        for row in payload["level_rows"]:
            log(reading_line(row))
        return 0

    settings = settings_from_env()
    moment = as_et(now) if now is not None else now_et()
    if client_factory is not None:
        client = client_factory()
    else:
        key = os.getenv("ALPACA_KEY", "").strip()
        secret = os.getenv("ALPACA_SECRET", "").strip()
        if not key or not secret:
            log("Missing ALPACA_KEY / ALPACA_SECRET secrets in the repo settings.")
            return 1
        client = AlpacaClient(
            key, secret,
            option_feed=settings["option_feed"],
            stock_feed=settings["stock_feed"],
            max_pages=settings["max_pages"],
        )
    try:
        payload = collect_live(client, moment, settings)
    except Exception as error:
        log(f"GEX run failed: {error}")
        return 1
    if payload is None:
        return 0
    write_outputs(args.out, payload)
    for row in payload["level_rows"]:
        log(reading_line(row))
    return 0


if __name__ == "__main__":
    sys.exit(main())
