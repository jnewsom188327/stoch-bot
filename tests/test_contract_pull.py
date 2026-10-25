"""Offline tests for OCC parsing and contract-pull reports. No network and no orders."""

import csv
import io
import json
from datetime import date, datetime
from pathlib import Path

import pytest

import contract_pull as cp

NY = cp.NY
DAY = date(2026, 10, 12)
ROOT = Path(__file__).resolve().parents[1]


def _at(hhmm, second=0):
    hour, minute = (int(part) for part in hhmm.split(":"))
    return datetime(2026, 10, 12, hour, minute, second, tzinfo=NY)


def _bar(hhmm, open_, high, low, close, volume=1, trades=1, second=0):
    return cp.MinuteBar(_at(hhmm, second), open_, high, low, close, volume, trades)


def _quote(hhmm, second, bid, ask):
    return cp.QuoteTick(_at(hhmm, second), bid, ask)


def _field(text, name):
    prefix = f"| {name} |"
    for line in text.splitlines():
        if line.startswith(prefix):
            return line
    raise AssertionError(name)


def _md_row(text, hhmm):
    prefix = f"| {hhmm} |"
    for line in text.splitlines():
        if line.startswith(prefix):
            return line
    raise AssertionError(hhmm)


def sample_input():
    """A sparse session. The 09:50 high and the 10:14 high are before the peak window."""
    bars = [
        _bar("15:58", 0.17, 0.18, 0.16, 0.17, volume=3, trades=1),
        _bar("09:31", 0.40, 0.41, 0.05, 0.40, volume=10, trades=3),
        _bar("09:45", 0.32, 0.34, 0.31, 0.33, volume=2, trades=1),
        _bar("09:47", 0.11, 0.12, 0.10, 0.12, volume=4, trades=2),
        _bar("09:50", 0.42, 1.50, 0.30, 0.80, volume=8, trades=4),
        _bar("10:14", 0.19, 0.99, 0.18, 0.20, volume=5, trades=2),
        _bar("10:20", 0.21, 0.50, 0.19, 0.40, volume=6, trades=3),
        _bar("10:30", 0.30, 0.32, 0.15, 0.16, volume=7, trades=2),
        _bar("15:55", 0.24, 0.26, 0.22, 0.25, volume=9, trades=1),
        _bar("16:05", 1.00, 9.99, 1.00, 1.00, volume=1, trades=1),
    ]
    quotes = [
        _quote("08:00", 0, 0.01, 0.02),
        _quote("10:13", 20, 0.08, 0.10),
        _quote("10:14", 5, 0.15, 0.11),
        _quote("10:14", 40, 0.21, 0.27),
        _quote("16:10", 0, 0.01, 0.01),
    ]
    stock = [
        _bar("10:14", 420.0, 421.0, 419.0, 420.50),
        _bar("10:20", 421.0, 422.0, 420.0, 421.00),
        _bar("15:55", 429.0, 431.0, 428.0, 430.00),
    ]
    return cp.ReportInput(
        symbol="MSFT261012C00545000",
        underlying="MSFT",
        day=DAY,
        alert=cp.parse_alert(DAY, "10:14"),
        reference_ask=0.23,
        option_bars=bars,
        quotes=quotes,
        stock_bars=stock,
        option_feed="opra",
        quote_feed="opra",
        stock_feed="iex",
        option_status_lines=["opra: HTTP 200, 10 bars"],
        quote_status_lines=["opra: HTTP 200, 5 quotes"],
        stock_status_lines=["iex: HTTP 200, 3 stock bars"],
    )


def test_occ_symbols_and_the_two_contract_list():
    msft = cp.parse_occ("msft261012c00545000")
    assert msft["symbol"] == "MSFT261012C00545000"
    assert msft["root"] == "MSFT"
    assert msft["expiry"] == DAY
    assert msft["right"] == "C"
    assert msft["strike"] == 545

    qqq = cp.parse_occ("QQQ261012P00744000")
    assert qqq["root"] == "QQQ"
    assert qqq["expiry"] == DAY
    assert qqq["right"] == "P"
    assert qqq["strike"] == 744

    pairs = cp.parse_symbol_pairs("MSFT261012C00545000:MSFT, QQQ261012P00744000:QQQ")
    assert pairs == [
        ("MSFT261012C00545000", "MSFT"),
        ("QQQ261012P00744000", "QQQ"),
    ]
    with pytest.raises(ValueError):
        cp.parse_occ("MSFT261012X00545000")
    with pytest.raises(ValueError):
        cp.parse_occ("MSFT261012C0054500")


def test_reference_asks_default_to_the_two_entry_quotes():
    refs = cp.parse_reference_asks(None)
    assert refs["MSFT"] == pytest.approx(0.23)
    assert refs["QQQ"] == pytest.approx(0.31)
    overridden = cp.parse_reference_asks("QQQ:0.40")
    assert overridden["QQQ"] == pytest.approx(0.40)
    assert overridden["MSFT"] == pytest.approx(0.23)
    assert cp.format_gain(0.40, 0.31) == "+$9.00 per contract (+29.03%)"


def test_regular_hours_window_is_eastern_on_the_sample_day():
    start, end = cp.session_bounds(DAY)
    assert start == "2026-10-12T13:30:00Z"
    assert end == "2026-10-12T20:00:00Z"
    alert = cp.parse_alert(DAY, "10:14 ET")
    assert (alert.hour, alert.minute) == (10, 14)


def test_cli_accepts_the_pair_list_or_one_contract():
    paired = cp.parse_args([
        "--symbols", "MSFT261012C00545000:MSFT,QQQ261012P00744000:QQQ",
        "--date", "2026-10-12",
        "--alert-time", "10:14",
    ])
    assert cp.resolve_pairs(paired) == [
        ("MSFT261012C00545000", "MSFT"),
        ("QQQ261012P00744000", "QQQ"),
    ]
    single = cp.parse_args([
        "--symbol", "MSFT261012C00545000",
        "--underlying", "msft",
        "--date", "2026-10-12",
    ])
    assert cp.resolve_pairs(single) == [("MSFT261012C00545000", "MSFT")]
    with pytest.raises(SystemExit):
        cp.resolve_pairs(cp.parse_args([
            "--symbols", "MSFT261012C00545000:MSFT",
            "--symbol", "MSFT261012C00545000",
            "--underlying", "MSFT",
            "--date", "2026-10-12",
        ]))


def test_report_leads_with_the_peak_after_the_alert_and_does_not_invent_prices():
    text = cp.render_markdown(sample_input())
    assert text.startswith("| Field | Value |")
    positions = [
        text.find("| Alert price |"),
        text.find("| Peak high after the alert |"),
        text.find("| Gain vs reference ask |"),
        text.find("| Low after the alert |"),
        text.find("| Price at 15:55 ET |"),
        text.find("## Option price every 5 minutes"),
    ]
    assert all(pos >= 0 for pos in positions)
    assert positions == sorted(positions)
    assert text.find("not guaranteed fills") < text.find("## Option price every 5 minutes")

    peak = _field(text, "Peak high after the alert")
    assert "0.50 at 10:20 ET" in peak
    assert "0.99" not in peak
    assert "1.50" not in peak
    assert "+$27.00 per contract (+117.39%)" in _field(text, "Gain vs reference ask")
    assert "+$23.00" not in _field(text, "Gain vs reference ask")
    assert "0.15 at 10:30 ET" in _field(text, "Low after the alert")
    assert "0.05" not in _field(text, "Low after the alert")
    assert "0.25 close of the 15:55 ET bar" in _field(text, "Price at 15:55 ET")
    assert "0.20 close" in _field(text, "Alert price")
    assert "10:14 ET bar" in _field(text, "Alert price")
    assert "0.27 at 10:14:40 ET" in _field(text, "Ask at alert")
    assert "0.23" in _field(text, "Reference ask")

    assert "- Day open: 0.40 at 09:31 ET" in text
    assert "- Day high: 1.50 at 09:50 ET." in text
    assert "- Day low: 0.05 at 09:31 ET." in text
    assert "- Day close: 0.17 at 15:58 ET" in text
    first = next(line for line in text.splitlines() if line.startswith("- First bar after 09:45"))
    assert "09:47 ET" in first
    assert "0.33" in _md_row(text, "09:45")

    assert "no bar" in _md_row(text, "10:25")
    assert "0.50" not in _md_row(text, "10:25")
    assert "421" not in _md_row(text, "10:25")
    assert "0.20" not in _md_row(text, "10:15")
    assert "0.50" in _md_row(text, "10:20")
    assert "421.00" in _md_row(text, "10:20")

    assert "381 of 390" in text
    assert "10:21-10:29" in text
    assert "no trade = no bar" in text
    assert "No prices were interpolated." in text
    assert "Ignored 1 option bar outside 09:30-16:00 ET." in text
    assert "9.99" not in text
    assert "0.02" not in text
    assert "-$6.00 per contract (-26.09%)" in text
    assert "+$2.00 per contract (+8.70%)" in text
    assert "Close value: 0.17 at 15:58 ET." in text


def test_csv_leaves_gaps_blank_and_keeps_the_last_quote_in_the_minute():
    rows = list(csv.DictReader(io.StringIO(cp.render_csv(sample_input()))))
    assert len(rows) == 390
    by_time = {row["time_et"]: row for row in rows}
    assert set(by_time) == {f"2026-10-12 {minute.strftime('%H:%M')}" for minute in cp.rth_minutes(DAY)}

    alert = by_time["2026-10-12 10:14"]
    assert alert["option_close"] == "0.20"
    assert alert["option_high"] == "0.99"
    assert alert["option_volume"] == "5"
    assert alert["option_trade_count"] == "2"
    assert alert["bid"] == "0.21"
    assert alert["ask"] == "0.27"
    assert alert["underlying_close"] == "420.50"
    assert by_time["2026-10-12 10:13"]["ask"] == "0.10"
    assert by_time["2026-10-12 10:13"]["option_close"] == ""

    hole = by_time["2026-10-12 10:25"]
    assert hole["option_open"] == ""
    assert hole["option_high"] == ""
    assert hole["option_close"] == ""
    assert hole["bid"] == ""
    assert hole["ask"] == ""
    assert hole["underlying_close"] == ""
    carried = by_time["2026-10-12 10:15"]
    assert carried["option_close"] == ""
    assert carried["ask"] == ""
    assert carried["underlying_close"] == ""
    assert by_time["2026-10-12 10:20"]["option_high"] == "0.50"
    assert by_time["2026-10-12 15:55"]["option_close"] == "0.25"
    assert "2026-10-12 16:05" not in by_time
    blob = cp.render_csv(sample_input())
    assert "9.99" not in blob
    assert "0.02" not in blob


def test_empty_api_response_is_stated_with_the_raw_status():
    data = cp.ReportInput(
        symbol="MSFT261012C00545000",
        underlying="MSFT",
        day=DAY,
        alert=cp.parse_alert(DAY, "10:14"),
        reference_ask=0.23,
        option_bars=[],
        quotes=[],
        stock_bars=[],
        quotes_skipped=True,
        option_status_lines=[
            'opra: HTTP 403, 0 bars. Body: {"message":"forbidden"}',
            'indicative: HTTP 200, 0 bars. Body: {"bars":{}}',
        ],
        quote_status_lines=[
            "opra: HTTP 403, 0 quotes. Body: forbidden",
            'indicative: HTTP 200, 0 quotes. Body: {"quotes":{}}',
        ],
        stock_status_lines=[
            "sip: HTTP 403, 0 stock bars. Body: forbidden",
            'iex: HTTP 200, 0 stock bars. Body: {"bars":[]}',
        ],
    )
    text = cp.render_markdown(data)
    assert text.startswith("| Field | Value |")
    assert "The Alpaca options data API returned no option bars for MSFT261012C00545000 on 2026-10-12." in text
    assert "HTTP 403" in text
    assert "HTTP 200" in text
    assert "not computed; the API returned no option bars" in _field(text, "Gain vs reference ask")
    assert "no option bar after the alert" in _field(text, "Peak high after the alert")
    assert "no bar at 15:55 ET" in _field(text, "Price at 15:55 ET")
    assert "Option quotes: skipped." in text
    assert "Nothing was interpolated." in text
    assert "0.50" not in text
    assert "| 10:20 |" not in text


def test_status_text_scrubs_secrets(monkeypatch):
    secret = "supersecretvalue123"
    monkeypatch.setenv("ALPACA_SECRET", secret)
    data = cp.ReportInput(
        symbol="QQQ261012P00744000",
        underlying="QQQ",
        day=DAY,
        alert=cp.parse_alert(DAY, "10:14"),
        reference_ask=0.31,
        option_bars=[_bar("10:20", 0.31, 0.40, 0.30, 0.35)],
        quotes=[],
        stock_bars=[],
        option_feed="indicative",
        quotes_skipped=True,
        option_status_lines=[f"opra: HTTP 403, 0 bars. Body: bad key {secret}"],
    )
    text = cp.render_markdown(data)
    assert secret not in text
    assert "***" in text
    assert "+$9.00 per contract (+29.03%)" in text


def _client(transport):
    return cp.DataClient("key-sentinel-abc", "secret-sentinel-xyz", transport=transport, sleep_fn=lambda _s: None)


def test_opra_empty_falls_back_to_indicative_and_keeps_status(monkeypatch):
    secret = "supersecretvalue123"
    monkeypatch.setenv("ALPACA_SECRET", secret)
    urls = []

    def transport(url, headers, timeout):
        urls.append(url)
        assert secret not in url
        assert "key-sentinel-abc" not in url
        assert headers["APCA-API-KEY-ID"] == "key-sentinel-abc"
        if "/options/bars" in url and "feed=opra" in url:
            return 200, {}, json.dumps({"bars": {}, "next_page_token": None})
        if "/options/bars" in url and "feed=indicative" in url:
            body = {
                "bars": {
                    "MSFT261012C00545000": [
                        {"t": "2026-10-12T14:14:00Z", "o": 0.22, "h": 0.22, "l": 0.20, "c": 0.22, "v": 2, "n": 1},
                        {"t": "2026-10-12T14:20:00Z", "o": 0.30, "h": 0.40, "l": 0.28, "c": 0.30, "v": 3, "n": 2},
                        {"t": "2026-10-12T19:55:00Z", "o": 0.11, "h": 0.12, "l": 0.10, "c": 0.11, "v": 1, "n": 1},
                    ]
                }
            }
            return 200, {}, json.dumps(body)
        if "/options/quotes" in url and "feed=opra" in url:
            return 403, {}, json.dumps({"message": f"nope {secret}"})
        if "/options/quotes" in url and "feed=indicative" in url:
            body = {
                "quotes": {
                    "MSFT261012C00545000": [
                        {"t": "2026-10-12T14:14:10Z", "bp": 0.20, "ap": 0.23},
                    ]
                }
            }
            return 200, {}, json.dumps(body)
        if "/stocks/MSFT/bars" in url and "feed=sip" in url:
            return 403, {}, json.dumps({"message": "sip forbidden"})
        if "/stocks/MSFT/bars" in url and "feed=iex" in url:
            body = {"bars": [{"t": "2026-10-12T14:20:00Z", "o": 400, "h": 401, "l": 399, "c": 400.5, "v": 10, "n": 4}]}
            return 200, {}, json.dumps(body)
        return 404, {}, "{}"

    report = cp.pull_contract(
        _client(transport), "MSFT261012C00545000", "MSFT", DAY, "10:14", 0.23,
    )
    text = cp.render_markdown(report)
    assert report.option_feed == "indicative"
    assert report.quote_feed == "indicative"
    assert report.stock_feed == "iex"
    assert "Option bar feed used: indicative." in text
    assert "opra: HTTP 200, 0 bars" in text
    assert "HTTP 403" in text
    assert secret not in text
    assert "***" in text
    assert "0.40 at 10:20 ET" in _field(text, "Peak high after the alert")
    assert "+$17.00 per contract (+73.91%)" in text
    assert "0.23 at 10:14:10 ET" in _field(text, "Ask at alert")
    assert "400.50" in cp.render_csv(report)


def test_rejected_feed_parameter_falls_back_to_the_unscoped_bars():
    def transport(url, headers, timeout):
        if "/options/bars" in url and "feed=" in url:
            return 400, {}, json.dumps({"message": "feed not supported"})
        if "/options/bars" in url:
            body = {
                "bars": {
                    "MSFT261012C00545000": [
                        {"t": "2026-10-12T14:20:00Z", "o": 0.20, "h": 0.40, "l": 0.19, "c": 0.30, "v": 1, "n": 1},
                    ]
                }
            }
            return 200, {}, json.dumps(body)
        if "/options/quotes" in url:
            return 404, {}, json.dumps({"message": "not found"})
        if "/stocks/" in url:
            return 200, {}, json.dumps({"bars": []})
        return 404, {}, "{}"

    report = cp.pull_contract(
        _client(transport), "MSFT261012C00545000", "MSFT", DAY, "10:14", 0.23,
    )
    text = cp.render_markdown(report)
    assert report.option_feed == "default"
    assert report.quotes_skipped is True
    assert "HTTP 400" in text
    assert "HTTP 404" in text
    assert "0.40 at 10:20 ET" in _field(text, "Peak high after the alert")
    assert "Option quotes: skipped." in text
    assert "unscoped API response" in text


def test_option_bars_follow_the_page_token_without_mixing_feeds():
    urls = []

    def transport(url, headers, timeout):
        urls.append(url)
        if "/options/bars" in url and "feed=opra" in url and "page_token" not in url:
            body = {
                "bars": {"MSFT261012C00545000": [
                    {"t": "2026-10-12T14:14:00Z", "o": 0.20, "h": 0.21, "l": 0.19, "c": 0.20, "v": 1, "n": 1},
                ]},
                "next_page_token": "abc",
            }
            return 200, {}, json.dumps(body)
        if "/options/bars" in url and "feed=opra" in url and "page_token=abc" in url:
            body = {
                "bars": {"MSFT261012C00545000": [
                    {"t": "2026-10-12T14:20:00Z", "o": 0.40, "h": 0.50, "l": 0.39, "c": 0.40, "v": 2, "n": 1},
                ]},
                "next_page_token": None,
            }
            return 200, {}, json.dumps(body)
        if "/options/quotes" in url or "/stocks/" in url:
            if "quotes" in url:
                return 200, {}, json.dumps({"quotes": {}})
            return 200, {}, json.dumps({"bars": []})
        return 404, {}, "{}"

    report = cp.pull_contract(
        _client(transport), "MSFT261012C00545000", "MSFT", DAY, "10:14", 0.23,
    )
    minutes = [bar.minute.strftime("%H:%M") for bar in report.option_bars]
    assert minutes == ["10:14", "10:20"]
    bar_urls = [url for url in urls if "/options/bars" in url]
    assert len(bar_urls) == 2
    assert all("feed=opra" in url for url in bar_urls)
    assert not any("feed=indicative" in url and "/options/bars" in url for url in urls)


def test_workflow_is_a_manual_data_pull_onto_its_own_branch():
    text = (ROOT / ".github" / "workflows" / "contract_pull.yml").read_text(encoding="utf-8")
    assert "workflow_dispatch" in text
    assert "MSFT261012C00545000:MSFT,QQQ261012P00744000:QQQ" in text
    assert 'default: "2026-10-12"' in text
    assert 'default: "10:14"' in text
    assert 'default: "contract-pull-results"' in text
    assert "python -m pytest -q" in text
    assert "pytest -q" in text and "\n        run: pytest" not in text
    assert "ALPACA_KEY" in text
    assert "ALPACA_SECRET" in text
    assert "contents: write" in text
    assert "contract_pull.py" in text
    assert 'main|master' in text
    assert 'git push origin "HEAD:${BRANCH}"' in text
