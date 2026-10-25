"""
Download one regular-hours session for one or more option contracts and write a report.

DATA ONLY. This script sends GET requests to Alpaca's market-data API. It does
not import an order client, submit an order, or send a trade.

Keys come from the ALPACA_KEY and ALPACA_SECRET environment variables, the same
pair scalp_real.py uses. They are sent only as request headers. Every log line
and report snippet is passed through scalp_real._scrub so a key cannot land in
the output.

    ALPACA_KEY=... ALPACA_SECRET=... python contract_pull.py \
        --symbols MSFT261012C00545000:MSFT,QQQ261012P00744000:QQQ \
        --date 2026-10-12 --alert-time 10:14

A single contract still works:

    python contract_pull.py --symbol MSFT261012C00545000 --date 2026-10-12 --underlying MSFT

The supported run is .github/workflows/contract_pull.yml (Actions tab,
contract_pull, Run workflow). For each contract the script writes:

    results/contract_pull/<symbol>_<date>.csv
    results/contract_pull/<symbol>_<date>.md

Option bars try the OPRA feed first and the indicative feed when OPRA is
missing or empty. Quotes are requested the same way and left blank when the
API returns none. Nothing is interpolated: a minute with no trade has no bar.
"""

from __future__ import annotations

import argparse
import csv
import io
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass, field, replace
from datetime import date, datetime, time as dtime, timedelta, timezone
from zoneinfo import ZoneInfo

from scalp_real import _scrub

NY = ZoneInfo("America/New_York")
DATA_BASE = "https://data.alpaca.markets"
DEFAULT_REFERENCE_ASKS = {"MSFT": 0.23, "QQQ": 0.31}
PAGE_LIMIT = 10000
MAX_PAGES = 40
CSV_FIELDS = [
    "time_et",
    "option_open",
    "option_high",
    "option_low",
    "option_close",
    "option_volume",
    "option_trade_count",
    "bid",
    "ask",
    "underlying_close",
]


def scrub(text) -> str:
    return _scrub(text)


def log(msg) -> None:
    print(scrub(msg), flush=True)


# ----- parsing -----

def parse_occ(symbol: str) -> dict:
    """Parse a compact OCC symbol such as MSFT261012C00545000."""
    import re

    text = symbol.strip().upper()
    match = re.fullmatch(r"([A-Z]{1,6})(\d{2})(\d{2})(\d{2})([CP])(\d{8})", text)
    if not match:
        raise ValueError(f"not an OCC option symbol: {symbol.strip()}")
    root, year, month, day, right, strike_raw = match.groups()
    try:
        expiry = date(2000 + int(year), int(month), int(day))
    except ValueError as exc:
        raise ValueError(f"bad expiration in {text}") from exc
    return {
        "symbol": text,
        "root": root,
        "expiry": expiry,
        "right": right,
        "strike": int(strike_raw) / 1000.0,
    }


def parse_symbol_pairs(text: str) -> list[tuple[str, str]]:
    """Parse 'OCC:UNDERLYING,OCC:UNDERLYING'."""
    import re

    pairs = []
    for part in text.split(","):
        part = part.strip()
        if not part:
            continue
        if ":" not in part:
            raise ValueError(f"expected OCC:underlying, got {part}")
        occ, underlying = part.split(":", 1)
        parsed = parse_occ(occ)
        ticker = underlying.strip().upper()
        if not re.fullmatch(r"[A-Z][A-Z0-9.]{0,9}", ticker):
            raise ValueError(f"bad underlying: {underlying.strip()}")
        pairs.append((parsed["symbol"], ticker))
    if not pairs:
        raise ValueError("no contracts given")
    return pairs


def parse_reference_asks(text: str | None) -> dict[str, float]:
    """Default MSFT 0.23 and QQQ 0.31, overridden by UNDERLYING:price pairs."""
    out = dict(DEFAULT_REFERENCE_ASKS)
    if not text or not text.strip():
        return out
    for part in text.split(","):
        part = part.strip()
        if not part:
            continue
        if ":" not in part:
            raise ValueError(f"expected UNDERLYING:price, got {part}")
        name, raw = part.split(":", 1)
        out[name.strip().upper()] = float(raw)
    return out


def parse_date(text: str) -> date:
    try:
        return date.fromisoformat(text.strip())
    except ValueError as exc:
        raise ValueError(f"date must be YYYY-MM-DD, got {text}") from exc


def parse_alert(day: date, text: str) -> datetime:
    import re

    raw = text.strip().upper().replace("ET", "").strip()
    match = re.fullmatch(r"(\d{1,2}):(\d{2})", raw)
    if not match:
        raise ValueError(f"alert time must be HH:MM ET, got {text}")
    hour, minute = int(match.group(1)), int(match.group(2))
    if hour > 23 or minute > 59:
        raise ValueError(f"alert time must be HH:MM ET, got {text}")
    return datetime.combine(day, dtime(hour, minute), tzinfo=NY)


def session_bounds(day: date) -> tuple[str, str]:
    """Regular hours 09:30 inclusive to 16:00 exclusive, as UTC RFC3339."""
    start = datetime.combine(day, dtime(9, 30), tzinfo=NY)
    end = datetime.combine(day, dtime(16, 0), tzinfo=NY)
    return _utc_z(start), _utc_z(end)


def rth_start(day: date) -> datetime:
    return datetime.combine(day, dtime(9, 30), tzinfo=NY)


def rth_end(day: date) -> datetime:
    return datetime.combine(day, dtime(16, 0), tzinfo=NY)


def rth_minutes(day: date) -> list[datetime]:
    start = rth_start(day)
    return [start + timedelta(minutes=i) for i in range(390)]


def five_minute_marks(day: date) -> list[datetime]:
    start = rth_start(day)
    last = datetime.combine(day, dtime(15, 55), tzinfo=NY)
    marks = []
    cursor = start
    while cursor <= last:
        marks.append(cursor)
        cursor += timedelta(minutes=5)
    return marks


def _utc_z(moment: datetime) -> str:
    utc = moment.astimezone(timezone.utc).replace(microsecond=0)
    return utc.strftime("%Y-%m-%dT%H:%M:%SZ")


def parse_ts(value) -> datetime:
    text = str(value).strip()
    if text.endswith("Z"):
        text = text[:-1] + "+00:00"
    moment = datetime.fromisoformat(text)
    if moment.tzinfo is None:
        moment = moment.replace(tzinfo=timezone.utc)
    return moment.astimezone(NY)


def in_rth(moment: datetime, day: date) -> bool:
    return rth_start(day) <= moment < rth_end(day)


# ----- formatting -----

def fmt_px(value) -> str:
    if value is None:
        return ""
    number = float(value)
    text = f"{number:.4f}"
    if "." in text:
        text = text.rstrip("0").rstrip(".")
    if "." not in text:
        return text + ".00"
    if len(text.split(".")[1]) == 1:
        return text + "0"
    return text


def fmt_count(value) -> str:
    if value is None:
        return ""
    number = float(value)
    if abs(number - round(number)) < 1e-9:
        return str(int(round(number)))
    return fmt_px(number)


def fmt_strike(strike: float) -> str:
    if abs(strike - round(strike)) < 1e-9:
        return str(int(round(strike)))
    return f"{strike:.3f}".rstrip("0").rstrip(".")


def fmt_signed_money(dollars: float) -> str:
    cents = round(float(dollars), 2)
    if cents > 0:
        return f"+${cents:.2f}"
    if cents < 0:
        return f"-${abs(cents):.2f}"
    return "$0.00"


def format_gain(price: float, reference: float) -> str:
    """Dollar gain per contract uses the standard 100 multiplier."""
    if round(float(reference) * 100) == 0:
        return "not computed; the reference ask is 0"
    dollars = (float(price) - float(reference)) * 100.0
    pct = (float(price) - float(reference)) / float(reference) * 100.0
    return f"{fmt_signed_money(dollars)} per contract ({pct:+.2f}%)"


def describe_contract(symbol: str) -> str:
    parsed = parse_occ(symbol)
    side = "call" if parsed["right"] == "C" else "put"
    return (
        f"{parsed['root']} {side}, strike {fmt_strike(parsed['strike'])}, "
        f"expiring {parsed['expiry'].isoformat()}"
    )


def _md_cell(text) -> str:
    return str(text).replace("|", "/").replace("\n", " ")


def _table(headers: list[str], rows: list[list[str]]) -> list[str]:
    lines = [
        "| " + " | ".join(_md_cell(cell) for cell in headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(_md_cell(cell) for cell in row) + " |")
    return lines


# ----- report model -----

@dataclass
class MinuteBar:
    minute: datetime
    open: float
    high: float
    low: float
    close: float
    volume: float | None = None
    trade_count: float | None = None


@dataclass
class QuoteTick:
    time: datetime
    bid: float | None
    ask: float | None


@dataclass
class ReportInput:
    symbol: str
    underlying: str
    day: date
    alert: datetime
    reference_ask: float | None
    option_bars: list[MinuteBar]
    quotes: list[QuoteTick]
    stock_bars: list[MinuteBar]
    option_feed: str | None = None
    quote_feed: str | None = None
    stock_feed: str | None = None
    option_status_lines: list[str] = field(default_factory=list)
    quote_status_lines: list[str] = field(default_factory=list)
    stock_status_lines: list[str] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)
    quotes_skipped: bool = False
    option_truncated: bool = False
    quote_truncated: bool = False
    stock_truncated: bool = False


@dataclass
class Prepared:
    data: ReportInput
    option_bars: list[MinuteBar]
    stock_bars: list[MinuteBar]
    quotes: list[QuoteTick]
    opt_by_min: dict
    stock_by_min: dict
    quote_by_min: dict
    ignored_option: int
    ignored_stock: int
    ignored_quotes: int
    duplicate_option: int


def _take_bars(bars: list[MinuteBar], day: date):
    ignored = 0
    kept = []
    for bar in bars:
        minute = bar.minute.astimezone(NY).replace(second=0, microsecond=0)
        if not in_rth(minute, day):
            ignored += 1
            continue
        kept.append(replace(bar, minute=minute))
    kept.sort(key=lambda bar: bar.minute)
    deduped = []
    duplicates = 0
    for bar in kept:
        if deduped and deduped[-1].minute == bar.minute:
            duplicates += 1
            continue
        deduped.append(bar)
    return deduped, ignored, duplicates


def _take_quotes(quotes: list[QuoteTick], day: date):
    ignored = 0
    kept = []
    for quote in quotes:
        moment = quote.time.astimezone(NY)
        if not in_rth(moment, day):
            ignored += 1
            continue
        kept.append(replace(quote, time=moment))
    kept.sort(key=lambda quote: quote.time)
    by_minute = {}
    for quote in kept:
        minute = quote.time.replace(second=0, microsecond=0)
        by_minute[minute] = quote
    return kept, by_minute, ignored


def prepare(data: ReportInput) -> Prepared:
    option_bars, ignored_option, duplicate_option = _take_bars(data.option_bars, data.day)
    stock_bars, ignored_stock, _dup_stock = _take_bars(data.stock_bars, data.day)
    quotes, quote_by_min, ignored_quotes = _take_quotes(data.quotes, data.day)
    return Prepared(
        data=data,
        option_bars=option_bars,
        stock_bars=stock_bars,
        quotes=quotes,
        opt_by_min={bar.minute: bar for bar in option_bars},
        stock_by_min={bar.minute: bar for bar in stock_bars},
        quote_by_min=quote_by_min,
        ignored_option=ignored_option,
        ignored_stock=ignored_stock,
        ignored_quotes=ignored_quotes,
        duplicate_option=duplicate_option,
    )


def _alert_minute(data: ReportInput) -> datetime:
    return data.alert.astimezone(NY).replace(second=0, microsecond=0)


def _bars_after(prep: Prepared):
    minute = _alert_minute(prep.data)
    return [bar for bar in prep.option_bars if bar.minute > minute]


def _alert_bar(prep: Prepared):
    minute = _alert_minute(prep.data)
    prior = [bar for bar in prep.option_bars if bar.minute <= minute]
    return prior[-1] if prior else None


def _peak_bar(prep: Prepared):
    after = _bars_after(prep)
    if not after:
        return None
    return max(after, key=lambda bar: (bar.high, -bar.minute.timestamp()))


def _low_bar(prep: Prepared):
    after = _bars_after(prep)
    if not after:
        return None
    return min(after, key=lambda bar: (bar.low, bar.minute.timestamp()))


def _gain_text(price, reference, missing: str) -> str:
    if price is None:
        return missing
    if reference is None:
        return "not computed; no reference ask was supplied"
    return format_gain(price, reference)


def _ask_at_alert(prep: Prepared) -> str:
    data = prep.data
    minute = _alert_minute(data)
    cutoff = minute + timedelta(minutes=1)
    eligible = [quote for quote in prep.quotes if quote.time < cutoff and quote.ask is not None]
    if not eligible:
        if data.quotes_skipped or not prep.quotes:
            return "no quotes returned"
        return f"no quote at or before {minute.strftime('%H:%M')} ET"
    quote = max(eligible, key=lambda item: item.time)
    return f"{fmt_px(quote.ask)} at {quote.time.strftime('%H:%M:%S')} ET"


def _alert_price_text(prep: Prepared) -> str:
    bar = _alert_bar(prep)
    minute = _alert_minute(prep.data)
    if bar is None:
        return f"no option bar at or before {minute.strftime('%H:%M')} ET"
    text = (
        f"{fmt_px(bar.close)} close "
        f"({bar.minute.strftime('%H:%M')} ET bar, open {fmt_px(bar.open)} "
        f"high {fmt_px(bar.high)} low {fmt_px(bar.low)})"
    )
    if bar.minute != minute:
        text += (
            f"; last bar at or before {minute.strftime('%H:%M')} ET, "
            "there is no bar at the alert minute"
        )
    return text


def _clock_bar(prep: Prepared, hour: int, minute: int):
    key = datetime.combine(prep.data.day, dtime(hour, minute), tzinfo=NY)
    return prep.opt_by_min.get(key)


def _gap_text(prep: Prepared) -> str:
    missing = [minute for minute in rth_minutes(prep.data.day) if minute not in prep.opt_by_min]
    count = len(missing)
    if count == 0:
        return "Every regular-hours minute has an option bar. no trade = no bar, and none were missing."
    return (
        f"{count} of 390 regular-hours minutes have no option trade. "
        f"no trade = no bar. Ranges (ET): {_format_ranges(missing)}."
    )


def _format_ranges(minutes: list[datetime]) -> str:
    if not minutes:
        return "none"
    ranges = []
    start = previous = minutes[0]
    for moment in minutes[1:]:
        if moment - previous == timedelta(minutes=1):
            previous = moment
            continue
        ranges.append((start, previous))
        start = previous = moment
    ranges.append((start, previous))
    parts = []
    for start, end in ranges:
        if start == end:
            parts.append(start.strftime("%H:%M"))
        else:
            parts.append(f"{start.strftime('%H:%M')}-{end.strftime('%H:%M')}")
    return ", ".join(parts)


def _lead_rows(prep: Prepared) -> list[list[str]]:
    data = prep.data
    minute = _alert_minute(data)
    peak = _peak_bar(prep)
    low = _low_bar(prep)
    at_1555 = _clock_bar(prep, 15, 55)
    if not prep.option_bars:
        if data.option_bars:
            gain = "not computed; no regular-hours option bars"
        else:
            gain = "not computed; the API returned no option bars"
    else:
        gain = _gain_text(
            None if peak is None else peak.high,
            data.reference_ask,
            "not computed; no option bar after the alert",
        )
    if data.reference_ask is None:
        reference = f"none supplied for {data.underlying}"
    else:
        reference = (
            f"{fmt_px(data.reference_ask)} "
            f"(supplied reference entry ask for {data.underlying}; not a market fill)"
        )
    if peak is None:
        peak_text = "no option bar after the alert"
    else:
        peak_text = f"**{fmt_px(peak.high)} at {peak.minute.strftime('%H:%M')} ET**"
    if low is None:
        low_text = "no option bar after the alert"
    else:
        low_text = f"{fmt_px(low.low)} at {low.minute.strftime('%H:%M')} ET"
    if at_1555 is None:
        price_1555 = "no bar at 15:55 ET"
    else:
        price_1555 = f"{fmt_px(at_1555.close)} close of the 15:55 ET bar"
    try:
        described = describe_contract(data.symbol)
        contract = f"{data.symbol} ({described})"
    except ValueError:
        contract = data.symbol
    return [
        ["Contract", contract],
        ["Underlying", data.underlying],
        ["Session", f"{data.day.isoformat()} 09:30-16:00 ET"],
        ["Alert time", f"{minute.strftime('%H:%M')} ET"],
        ["Alert price", _alert_price_text(prep)],
        ["Ask at alert", _ask_at_alert(prep)],
        ["Reference ask", reference],
        ["Peak high after the alert", peak_text],
        ["Gain vs reference ask", gain],
        ["Low after the alert", low_text],
        ["Price at 15:55 ET", price_1555],
    ]


def _five_minute_lines(prep: Prepared) -> list[str]:
    lines = ["## Option price every 5 minutes", ""]
    if not prep.option_bars:
        if prep.data.option_bars:
            lines.append(
                "No regular-hours option bars remained. Bars outside 09:30-16:00 ET were dropped. "
                "Nothing was interpolated."
            )
        else:
            lines.append(
                "The Alpaca options data API returned no option bars for "
                f"{prep.data.symbol} on {prep.data.day.isoformat()}. "
                "There is no 5-minute table because there are no prices. "
                "Nothing was interpolated."
            )
        return lines
    has_quotes = bool(prep.quotes)
    headers = ["Time ET", "Open", "High", "Low", "Close", "Volume"]
    if has_quotes:
        headers += ["Bid", "Ask"]
    headers.append("Underlying close")
    rows = []
    for mark in five_minute_marks(prep.data.day):
        bar = prep.opt_by_min.get(mark)
        stock = prep.stock_by_min.get(mark)
        quote = prep.quote_by_min.get(mark)
        underlying = fmt_px(stock.close) if stock else "—"
        if bar is None:
            row = [mark.strftime("%H:%M"), "no bar", "—", "—", "—", "—"]
            if has_quotes:
                row += [
                    fmt_px(quote.bid) if quote and quote.bid is not None else "—",
                    fmt_px(quote.ask) if quote and quote.ask is not None else "—",
                ]
            row.append(underlying)
        else:
            row = [
                mark.strftime("%H:%M"),
                fmt_px(bar.open),
                fmt_px(bar.high),
                fmt_px(bar.low),
                fmt_px(bar.close),
                fmt_count(bar.volume) or "—",
            ]
            if has_quotes:
                row += [
                    fmt_px(quote.bid) if quote and quote.bid is not None else "—",
                    fmt_px(quote.ask) if quote and quote.ask is not None else "—",
                ]
            row.append(underlying)
        rows.append(row)
    lines.extend(_table(headers, rows))
    lines.append("")
    lines.append(
        "Each row is the 1-minute bar that starts at that clock time. "
        "A missing minute stays \"no bar\"; neighboring minutes are not copied in."
    )
    return lines


def _bar_details(bar: MinuteBar) -> str:
    extra = []
    if bar.volume is not None:
        extra.append(f"volume {fmt_count(bar.volume)}")
    if bar.trade_count is not None:
        extra.append(f"{fmt_count(bar.trade_count)} trades")
    tail = (", " + ", ".join(extra)) if extra else ""
    return (
        f"{bar.minute.strftime('%H:%M')} ET open {fmt_px(bar.open)} high {fmt_px(bar.high)} "
        f"low {fmt_px(bar.low)} close {fmt_px(bar.close)}{tail}"
    )


def _session_lines(prep: Prepared) -> list[str]:
    data = prep.data
    lines = ["## Session open, high, low, close", ""]
    if not prep.option_bars:
        if prep.data.option_bars:
            lines.append("No session prices. Every returned option bar was outside 09:30-16:00 ET.")
        else:
            lines.append("No session prices. The API returned no option bars, so open, high, low, and close are unavailable.")
        return lines
    first = prep.option_bars[0]
    last = prep.option_bars[-1]
    high = max(prep.option_bars, key=lambda bar: (bar.high, -bar.minute.timestamp()))
    low = min(prep.option_bars, key=lambda bar: (bar.low, bar.minute.timestamp()))
    after_945 = next((bar for bar in prep.option_bars if bar.minute > datetime.combine(data.day, dtime(9, 45), tzinfo=NY)), None)
    lines.append(f"- Day open: {fmt_px(first.open)} at {first.minute.strftime('%H:%M')} ET (open of the first bar).")
    lines.append(f"- Day high: {fmt_px(high.high)} at {high.minute.strftime('%H:%M')} ET.")
    lines.append(f"- Day low: {fmt_px(low.low)} at {low.minute.strftime('%H:%M')} ET.")
    lines.append(f"- Day close: {fmt_px(last.close)} at {last.minute.strftime('%H:%M')} ET (close of the last bar).")
    if after_945 is None:
        lines.append("- First bar after 09:45 ET: no bar after 09:45 ET.")
    else:
        lines.append(f"- First bar after 09:45 ET: {_bar_details(after_945)}.")
    return lines


def _bought_lines(prep: Prepared) -> list[str]:
    data = prep.data
    lines = ["## Bought at the reference ask", ""]
    if data.reference_ask is None:
        lines.append(
            f"No reference ask was supplied for {data.underlying}, "
            "so gain versus a reference ask was not computed."
        )
        return lines
    lines.append(
        f"Reference ask: {fmt_px(data.reference_ask)}. "
        "This is the supplied reference entry ask, not a claim that the tape printed it. "
        "Dollars per contract are the premium difference times 100, the standard equity-option multiplier."
    )
    peak = _peak_bar(prep)
    if not prep.option_bars:
        reason = (
            "no regular-hours option bars"
            if data.option_bars
            else "the API returned no option bars"
        )
        lines.append(f"Max available gain: not computed; {reason}.")
        lines.append("Close value: no option bars.")
        lines.append(f"Gain/loss at close: not computed; {reason}.")
        return lines
    if peak is None:
        lines.append("Max available gain: not computed; no option bar after the alert.")
    else:
        lines.append(
            "Max available gain (peak high after the alert minus the reference ask): "
            f"{format_gain(peak.high, data.reference_ask)}."
        )
    last = prep.option_bars[-1]
    lines.append(f"Close value: {fmt_px(last.close)} at {last.minute.strftime('%H:%M')} ET.")
    lines.append(f"Gain/loss at close: {format_gain(last.close, data.reference_ask)}.")
    at_1555 = _clock_bar(prep, 15, 55)
    if at_1555 is None:
        lines.append("Price at 15:55 ET: no bar at 15:55 ET. Gain/loss at 15:55 was not computed.")
    else:
        lines.append(
            f"Price at 15:55 ET: {fmt_px(at_1555.close)}. "
            f"Gain/loss vs the reference ask at 15:55: {format_gain(at_1555.close, data.reference_ask)}."
        )
    return lines


def _coverage_lines(prep: Prepared) -> list[str]:
    data = prep.data
    lines = ["## Missing data", ""]
    if data.option_feed == "default":
        lines.append(
            "- Option bar feed used: default. OPRA and indicative did not return bars, "
            "so these bars are the unscoped API response."
        )
    elif data.option_feed:
        lines.append(f"- Option bar feed used: {data.option_feed}.")
    else:
        lines.append("- Option bar feed used: none. The API returned no option bars.")
    if data.option_truncated:
        lines.append("- Option bars stopped early. Minutes after the last returned bar are missing, not filled.")
    if data.quotes_skipped or not prep.quotes:
        lines.append("- Option quotes: skipped. The quotes API returned no in-session quotes. Bid and ask are blank.")
    else:
        lines.append(
            f"- Option quotes feed used: {data.quote_feed or 'unknown'}. "
            "Bid and ask are the last quote inside that minute. "
            "Minutes with no quote are blank. Quotes were not carried forward."
        )
        if data.quote_truncated:
            last = prep.quotes[-1].time.strftime("%H:%M:%S")
            lines.append(
                f"- Quote download stopped early at {last} ET. "
                "Later bid/ask cells are blank because those quotes were not returned."
            )
    if data.stock_feed:
        lines.append(f"- Underlying {data.underlying} bar feed used: {data.stock_feed}.")
    else:
        lines.append(f"- Underlying {data.underlying} bars: none returned.")
    if data.stock_truncated:
        lines.append("- Underlying bars stopped early. Later underlying closes are blank, not carried forward.")
    lines.append(f"- {_gap_text(prep)}")
    if prep.ignored_option:
        lines.append(
            f"- Ignored {prep.ignored_option} option bar"
            f"{'s' if prep.ignored_option != 1 else ''} outside 09:30-16:00 ET."
        )
    if prep.ignored_stock:
        lines.append(
            f"- Ignored {prep.ignored_stock} underlying bar"
            f"{'s' if prep.ignored_stock != 1 else ''} outside 09:30-16:00 ET."
        )
    if prep.ignored_quotes:
        lines.append(
            f"- Ignored {prep.ignored_quotes} quote"
            f"{'s' if prep.ignored_quotes != 1 else ''} outside 09:30-16:00 ET."
        )
    if prep.duplicate_option:
        lines.append(
            f"- {prep.duplicate_option} duplicate option minute"
            f"{'s were' if prep.duplicate_option != 1 else ' was'} "
            "kept once (the first bar). Duplicates were not averaged."
        )
    try:
        parsed = parse_occ(data.symbol)
        if parsed["expiry"] != data.day:
            lines.append(
                f"- This session ({data.day.isoformat()}) is not the expiration day "
                f"({parsed['expiry'].isoformat()})."
            )
        if parsed["root"] != data.underlying:
            lines.append(
                f"- OCC root {parsed['root']} differs from the requested underlying {data.underlying}. "
                f"Stock bars use {data.underlying}."
            )
    except ValueError:
        pass
    for note in data.notes:
        lines.append(f"- {scrub(note)}")
    lines.append("- No prices were interpolated.")
    return lines


def _status_lines(prep: Prepared) -> list[str]:
    lines = ["## Raw API response status", ""]
    groups = [
        ("Option bars", prep.data.option_status_lines),
        ("Option quotes", prep.data.quote_status_lines),
        ("Underlying bars", prep.data.stock_status_lines),
    ]
    any_line = False
    for title, group in groups:
        if not group:
            continue
        any_line = True
        lines.append(f"{title}:")
        for line in group:
            lines.append("- " + scrub(line).replace("|", "/"))
        lines.append("")
    if not any_line:
        lines.append("No API status was recorded.")
    if not prep.option_bars and not prep.data.option_bars:
        lines.append(
            "The Alpaca options data API returned no option bars for "
            f"{prep.data.symbol} on {prep.data.day.isoformat()}."
        )
    return lines


def render_markdown(data: ReportInput) -> str:
    prep = prepare(data)
    feed = prep.data.option_feed or "none"
    disclaimer = (
        "Bar highs and lows are the high and low of 1-minute bars of trades. "
        "They are not guaranteed fills. The peak and the low after the alert use only bars "
        f"that start after { _alert_minute(prep.data).strftime('%H:%M') } ET. "
        "The alert price is the close of the last 1-minute bar at or before that minute. "
        "No price was interpolated. A minute with no trade has no option bar."
    )
    parts = [
        *_table(["Field", "Value"], _lead_rows(prep)),
        "",
        disclaimer,
        "",
        f"Option bar feed used: {feed}.",
        "",
        *_five_minute_lines(prep),
        "",
        *_session_lines(prep),
        "",
        *_bought_lines(prep),
        "",
        *_coverage_lines(prep),
        "",
        *_status_lines(prep),
        "",
    ]
    return "\n".join(parts).rstrip() + "\n"


def csv_rows(data: ReportInput) -> list[dict]:
    prep = prepare(data)
    rows = []
    for minute in rth_minutes(data.day):
        bar = prep.opt_by_min.get(minute)
        stock = prep.stock_by_min.get(minute)
        quote = prep.quote_by_min.get(minute)
        rows.append({
            "time_et": minute.strftime("%Y-%m-%d %H:%M"),
            "option_open": fmt_px(bar.open) if bar else "",
            "option_high": fmt_px(bar.high) if bar else "",
            "option_low": fmt_px(bar.low) if bar else "",
            "option_close": fmt_px(bar.close) if bar else "",
            "option_volume": fmt_count(bar.volume) if bar else "",
            "option_trade_count": fmt_count(bar.trade_count) if bar else "",
            "bid": fmt_px(quote.bid) if quote and quote.bid is not None else "",
            "ask": fmt_px(quote.ask) if quote and quote.ask is not None else "",
            "underlying_close": fmt_px(stock.close) if stock else "",
        })
    return rows


def render_csv(data: ReportInput) -> str:
    buffer = io.StringIO()
    writer = csv.DictWriter(buffer, fieldnames=CSV_FIELDS, lineterminator="\n")
    writer.writeheader()
    for row in csv_rows(data):
        writer.writerow(row)
    return buffer.getvalue()


# ----- Alpaca HTTP (GET only) -----

def urllib_transport(url, headers, timeout):
    request = urllib.request.Request(url, headers=headers, method="GET")
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            body = response.read().decode("utf-8", errors="replace")
            return response.status, {key: value for key, value in response.headers.items()}, body
    except urllib.error.HTTPError as error:
        body = error.read().decode("utf-8", errors="replace")
        return error.code, {key: value for key, value in error.headers.items()}, body


def build_url(path: str, params: dict) -> str:
    clean = {key: value for key, value in params.items() if value is not None}
    query = urllib.parse.urlencode(clean)
    return DATA_BASE.rstrip("/") + path + ("?" + query if query else "")


def _snippet(body: str) -> str:
    text = scrub(body or "")
    text = " ".join(text.split())
    return text.replace("|", "/")[:300]


def _retry_wait(headers, attempt: int) -> float:
    raw = None
    if isinstance(headers, dict):
        raw = headers.get("Retry-After", headers.get("retry-after"))
    try:
        wait = float(raw)
    except (TypeError, ValueError):
        wait = float(2 ** attempt)
    return min(max(wait, 0.0), 30.0)


@dataclass
class Batch:
    items: list
    status: int | None
    snippet: str
    truncated: bool
    error: str

    @property
    def http_ok(self) -> bool:
        return self.status is not None and 200 <= self.status < 300


def attempt_line(feed: str, batch: Batch, noun: str) -> str:
    if batch.status is None:
        text = f"{feed}: no HTTP status ({batch.error or 'request failed'})"
    else:
        text = f"{feed}: HTTP {batch.status}, {len(batch.items)} {noun}"
        if batch.truncated:
            text += ", truncated"
        extras = []
        if batch.error:
            extras.append(batch.error)
        show_body = (
            len(batch.items) == 0 or batch.status >= 400 or batch.truncated or bool(batch.error)
        )
        if show_body and batch.snippet:
            extras.append(f"Body: {batch.snippet}")
        if extras:
            text += ". " + ". ".join(extras)
    return scrub(text)


def extract_symbol_rows(data, key: str, symbol: str) -> list:
    if not isinstance(data, dict):
        return []
    payload = data.get(key)
    if payload is None:
        return []
    if isinstance(payload, list):
        return payload
    if isinstance(payload, dict):
        if symbol in payload:
            return payload[symbol] or []
        wanted = symbol.upper()
        for name, rows in payload.items():
            if str(name).upper() == wanted:
                return rows or []
        return []
    return []


class DataClient:
    """Read-only Alpaca data client. There is no order method."""

    def __init__(self, key, secret, transport=None, sleep_fn=None, max_pages=MAX_PAGES):
        self.key = key
        self.secret = secret
        self.transport = transport or urllib_transport
        self.sleep_fn = sleep_fn or time.sleep
        self.max_pages = max_pages

    def _headers(self) -> dict:
        return {
            "APCA-API-KEY-ID": self.key,
            "APCA-API-SECRET-KEY": self.secret,
            "Accept": "application/json",
        }

    def _get(self, url: str):
        last_status = None
        last_body = ""
        last_error = ""
        for attempt in range(4):
            try:
                status, headers, body = self.transport(url, self._headers(), 30)
            except Exception as exc:
                last_status = None
                last_body = ""
                last_error = scrub(exc)
                self.sleep_fn(min(2 ** attempt, 8))
                continue
            last_status = status
            last_body = body or ""
            if status == 429 or 500 <= status <= 599:
                last_error = f"giving up after retries (HTTP {status})"
                self.sleep_fn(_retry_wait(headers, attempt))
                continue
            return status, last_body, ""
        if last_status is None:
            return None, "", last_error or "request failed"
        return last_status, last_body, last_error or f"giving up after retries (HTTP {last_status})"

    def collect(self, path: str, params: dict, extract) -> Batch:
        items = []
        token = None
        seen = set()
        first_ok = None
        snippet = ""
        for _page in range(self.max_pages):
            query = dict(params)
            if token:
                query["page_token"] = token
            status, body, error = self._get(build_url(path, query))
            snippet = _snippet(body)
            ok = status is not None and 200 <= status < 300 and not error
            if not ok:
                if items and first_ok is not None:
                    reason = error or f"later page failed (HTTP {status})"
                    return Batch(items, first_ok, snippet, True, reason)
                return Batch([], status, snippet, False, error)
            if first_ok is None:
                first_ok = status
            try:
                data = json.loads(body)
            except json.JSONDecodeError:
                if items:
                    return Batch(items, first_ok, snippet, True, "non-JSON response")
                return Batch([], status, snippet, False, "non-JSON response")
            if not isinstance(data, dict):
                if items:
                    return Batch(items, first_ok, snippet, True, "response was not a JSON object")
                return Batch([], status, snippet, False, "response was not a JSON object")
            chunk = extract(data)
            if isinstance(chunk, list):
                items.extend(chunk)
            token = data.get("next_page_token") or data.get("nextPageToken")
            if not token:
                return Batch(items, first_ok, snippet, False, "")
            if token in seen:
                return Batch(items, first_ok, snippet, True, "repeated page token")
            seen.add(token)
        return Batch(items, first_ok, snippet, True, f"stopped after {self.max_pages} pages")


def _num(value):
    if value is None or value == "":
        return None
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    if number != number or number in (float("inf"), float("-inf")):
        return None
    return number


def _parse_bar(row) -> MinuteBar | None:
    if not isinstance(row, dict):
        return None
    stamp = row.get("t", row.get("timestamp"))
    if not stamp:
        return None
    open_ = _num(row.get("o", row.get("open")))
    high = _num(row.get("h", row.get("high")))
    low = _num(row.get("l", row.get("low")))
    close = _num(row.get("c", row.get("close")))
    if None in (open_, high, low, close):
        return None
    return MinuteBar(
        minute=parse_ts(stamp),
        open=open_,
        high=high,
        low=low,
        close=close,
        volume=_num(row.get("v", row.get("volume"))),
        trade_count=_num(row.get("n", row.get("trade_count"))),
    )


def _parse_quote(row) -> QuoteTick | None:
    if not isinstance(row, dict):
        return None
    stamp = row.get("t", row.get("timestamp"))
    if not stamp:
        return None
    bid = _num(row.get("bp", row.get("bid")))
    ask = _num(row.get("ap", row.get("ask")))
    if bid is None and ask is None:
        return None
    return QuoteTick(time=parse_ts(stamp), bid=bid, ask=ask)


def _choose_feed(fetch_feed, feeds: tuple, noun: str):
    """Try feeds in order. Use the first one that returns rows.

    A feed of None omits the feed query (labeled "default"). That is the last
    attempt, for a plan that rejects the feed parameter or returns it empty.
    """
    lines = []
    chosen_feed = None
    chosen_batch = None
    for feed in feeds:
        batch = fetch_feed(feed)
        label = feed or "default"
        lines.append(attempt_line(label, batch, noun))
        if chosen_batch is None and batch.http_ok and batch.items:
            chosen_feed = label
            chosen_batch = batch
            break
    return chosen_feed, chosen_batch, lines


def _bars_from_batch(batch: Batch | None):
    bars = []
    skipped = 0
    if batch is None:
        return bars, skipped
    for row in batch.items:
        parsed = _parse_bar(row)
        if parsed is None:
            skipped += 1
            continue
        bars.append(parsed)
    return bars, skipped


def pull_contract(client: DataClient, symbol: str, underlying: str, day: date, alert_text: str, reference_ask) -> ReportInput:
    symbol = parse_occ(symbol)["symbol"]
    alert = parse_alert(day, alert_text)
    start, end = session_bounds(day)
    notes = []

    def fetch_option_bars(feed):
        params = {
            "symbols": symbol,
            "timeframe": "1Min",
            "start": start,
            "end": end,
            "limit": str(PAGE_LIMIT),
            "sort": "asc",
        }
        if feed:
            params["feed"] = feed
        return client.collect(
            "/v1beta1/options/bars",
            params,
            lambda data: extract_symbol_rows(data, "bars", symbol),
        )

    def fetch_quotes(feed):
        params = {
            "symbols": symbol,
            "start": start,
            "end": end,
            "limit": str(PAGE_LIMIT),
            "sort": "asc",
        }
        if feed:
            params["feed"] = feed
        return client.collect(
            "/v1beta1/options/quotes",
            params,
            lambda data: extract_symbol_rows(data, "quotes", symbol),
        )

    def fetch_stock(feed):
        quoted = urllib.parse.quote(underlying, safe="")
        params = {
            "timeframe": "1Min",
            "start": start,
            "end": end,
            "limit": str(PAGE_LIMIT),
            "adjustment": "raw",
            "sort": "asc",
        }
        if feed:
            params["feed"] = feed
        return client.collect(
            f"/v2/stocks/{quoted}/bars",
            params,
            lambda data: extract_symbol_rows(data, "bars", underlying),
        )

    # None means "do not send feed". Historical option bars in the public docs
    # have no feed parameter; OPRA and indicative are still tried first because
    # subscribed plans accept them.
    option_feed, option_batch, option_lines = _choose_feed(
        fetch_option_bars, ("opra", "indicative", None), "bars",
    )
    quote_feed, quote_batch, quote_lines = _choose_feed(
        fetch_quotes, ("opra", "indicative", None), "quotes",
    )
    stock_feed, stock_batch, stock_lines = _choose_feed(
        fetch_stock, ("sip", "iex", None), "stock bars",
    )

    option_bars, skipped_bars = _bars_from_batch(option_batch)
    stock_bars, skipped_stock = _bars_from_batch(stock_batch)
    quotes = []
    skipped_quotes = 0
    if quote_batch is not None:
        for row in quote_batch.items:
            parsed = _parse_quote(row)
            if parsed is None:
                skipped_quotes += 1
                continue
            quotes.append(parsed)
    if skipped_bars:
        notes.append(f"Skipped {skipped_bars} option rows that had no open, high, low, and close.")
    if skipped_stock:
        notes.append(f"Skipped {skipped_stock} underlying rows that had no open, high, low, and close.")
    if skipped_quotes:
        notes.append(f"Skipped {skipped_quotes} quotes that had no bid and no ask.")

    return ReportInput(
        symbol=symbol,
        underlying=underlying,
        day=day,
        alert=alert,
        reference_ask=reference_ask,
        option_bars=option_bars,
        quotes=quotes,
        stock_bars=stock_bars,
        option_feed=option_feed,
        quote_feed=quote_feed,
        stock_feed=stock_feed,
        option_status_lines=option_lines,
        quote_status_lines=quote_lines,
        stock_status_lines=stock_lines,
        notes=notes,
        quotes_skipped=quote_feed is None,
        option_truncated=bool(option_batch and option_batch.truncated),
        quote_truncated=bool(quote_batch and quote_batch.truncated),
        stock_truncated=bool(stock_batch and stock_batch.truncated),
    )


# ----- CLI -----

def parse_args(argv=None):
    parser = argparse.ArgumentParser(
        description="Download one session of option bars and write a report. Data only; no orders.",
    )
    parser.add_argument("--symbols", help="Comma-separated OCC:underlying pairs")
    parser.add_argument("--symbol", help="One OCC option symbol")
    parser.add_argument("--underlying", help="Underlying ticker, used with --symbol")
    parser.add_argument("--date", required=True, help="Session date YYYY-MM-DD")
    parser.add_argument("--alert-time", default="10:14", help="Alert time ET, HH:MM (default 10:14)")
    parser.add_argument(
        "--reference-asks",
        default=None,
        help="Optional UNDERLYING:price overrides. Defaults include MSFT:0.23 and QQQ:0.31.",
    )
    parser.add_argument("--out", default=os.path.join("results", "contract_pull"), help="Output directory")
    return parser.parse_args(argv)


def resolve_pairs(args) -> list[tuple[str, str]]:
    if args.symbols and (args.symbol or args.underlying):
        raise SystemExit("Pass --symbols or --symbol with --underlying, not both.")
    if args.symbols:
        return parse_symbol_pairs(args.symbols)
    if args.symbol or args.underlying:
        if not args.symbol or not args.underlying:
            raise SystemExit("--symbol and --underlying are both required for a single contract.")
        parsed = parse_occ(args.symbol)
        ticker = args.underlying.strip().upper()
        return [(parsed["symbol"], ticker)]
    raise SystemExit("Pass --symbols OCC:UNDERLYING,OCC:UNDERLYING or --symbol and --underlying.")


def load_keys() -> tuple[str, str]:
    key = os.getenv("ALPACA_KEY", "").strip()
    secret = os.getenv("ALPACA_SECRET", "").strip()
    if not key or not secret:
        raise SystemExit(
            "ALPACA_KEY / ALPACA_SECRET are missing. "
            "Add them in Settings > Secrets and variables > Actions."
        )
    return key, secret


def write_text(path: str, text: str) -> None:
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)


def main(argv=None) -> int:
    args = parse_args(argv)
    pairs = resolve_pairs(args)
    day = parse_date(args.date)
    references = parse_reference_asks(args.reference_asks)
    key, secret = load_keys()
    client = DataClient(key, secret)
    os.makedirs(args.out, exist_ok=True)
    written = []
    for symbol, underlying in pairs:
        report_input = pull_contract(
            client, symbol, underlying, day, args.alert_time, references.get(underlying),
        )
        markdown = render_markdown(report_input)
        csv_text = render_csv(report_input)
        stem = f"{report_input.symbol}_{day.isoformat()}"
        md_path = os.path.join(args.out, stem + ".md")
        csv_path = os.path.join(args.out, stem + ".csv")
        write_text(md_path, markdown)
        write_text(csv_path, csv_text)
        written.append(markdown)
        log(
            f"wrote {md_path} and {csv_path} "
            f"option_feed={report_input.option_feed or 'none'} "
            f"bars={len(report_input.option_bars)} "
            f"quotes={len(report_input.quotes)} "
            f"stock_feed={report_input.stock_feed or 'none'}"
        )
    summary = os.getenv("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as handle:
            for markdown in written:
                handle.write(markdown)
                handle.write("\n")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ValueError as exc:
        raise SystemExit(scrub(str(exc)))
