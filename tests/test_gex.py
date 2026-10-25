"""Unit tests for the log-only GEX math. No network."""

import csv
import gzip
import io
import json
import math
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
import urllib.parse
from contextlib import redirect_stdout
from datetime import date, datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import gex_logger as gex

ET = ZoneInfo("America/New_York")
ROOT = Path(__file__).resolve().parents[1]


def _contract(symbol, expiry, strike, right, oi="10", size="100"):
    return {
        "symbol": symbol,
        "expiration_date": expiry,
        "strike_price": str(strike),
        "type": right,
        "size": size,
        "open_interest": oi,
    }


class MathTests(unittest.TestCase):
    def setUp(self):
        gex._extra_secrets.clear()

    def test_sign_convention_and_one_percent_formula(self):
        call = gex.gex_dollars(0.01, 10, 100, 100, "call")
        put = gex.gex_dollars(0.01, 10, 100, 100, "put")
        # gamma * oi * size * spot^2 * 0.01
        self.assertAlmostEqual(call, 0.01 * 10 * 100 * 100 * 100 * 0.01, places=9)
        self.assertAlmostEqual(call, 1000.0, places=9)
        self.assertAlmostEqual(put, -call, places=9)
        self.assertGreater(call, 0)
        self.assertLess(put, 0)

    def test_bs_gamma_matches_closed_form(self):
        gamma = gex.bs_gamma(100, 100, 0.20, 0.1)
        self.assertAlmostEqual(gamma, 0.063046781777, places=9)
        # Call and put gamma are the same.
        self.assertAlmostEqual(gex.bs_gamma(100, 105, 0.20, 0.1), 0.047976537333, places=9)

    def test_missing_gamma_uses_iv_and_stays_positive_for_calls(self):
        contract = gex.parse_contract(_contract("C100", "2026-10-23", 100, "call", oi="10"))
        snap = {"impliedVolatility": 0.20, "latestQuote": {"bp": 1.0, "ap": 1.2}}
        row = gex.enrich(contract, snap, 100.0, 0.1)
        self.assertEqual(row["gamma_source"], "bs_iv")
        self.assertAlmostEqual(row["gamma"], 0.063046781777, places=9)
        self.assertAlmostEqual(row["gex"], 6304.6781777, places=4)
        self.assertGreater(row["gex"], 0)

        put = gex.parse_contract(_contract("P100", "2026-10-23", 100, "put", oi="10"))
        put_row = gex.enrich(put, snap, 100.0, 0.1)
        self.assertEqual(put_row["gamma_source"], "bs_iv")
        self.assertAlmostEqual(put_row["gex"], -row["gex"], places=4)

    def test_missing_iv_implies_from_mid(self):
        def indep_call(spot, strike, iv, t_years):
            sqrt_t = math.sqrt(t_years)
            d1 = (math.log(spot / strike) + 0.5 * iv * iv * t_years) / (iv * sqrt_t)
            d2 = d1 - iv * sqrt_t
            cdf = lambda x: 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))
            return spot * cdf(d1) - strike * cdf(d2)

        mid = indep_call(100.0, 100.0, 0.20, 0.1)
        contract = gex.parse_contract(_contract("C100", "2026-10-23", 100, "call", oi="10"))
        snap = {"latestQuote": {"bp": mid, "ap": mid}}
        row = gex.enrich(contract, snap, 100.0, 0.1)
        self.assertEqual(row["gamma_source"], "bs_mid")
        self.assertEqual(row["iv_source"], "mid")
        self.assertAlmostEqual(row["gamma"], 0.063046781777, places=4)
        self.assertGreater(row["gex"], 0)

    def test_no_quote_and_no_greeks_is_flagged_and_excluded_from_gex(self):
        contract = gex.parse_contract(_contract("C100", "2026-10-23", 100, "call", oi="10"))
        row = gex.enrich(contract, {}, 100.0, 0.1)
        self.assertEqual(row["gamma_source"], "missing")
        self.assertIsNone(row["gex"])

    def test_synthetic_chain_flip_walls_and_top3(self):
        expiry = date(2026, 10, 23)
        moment = datetime(2026, 10, 23, 10, 30, tzinfo=ET)
        rows = gex.spy_sample_rows(expiry)
        level = gex.build_level_row("SPY", moment, 100.0, "fixture", rows, 0.10, False, "fixture", "fixture")
        self.assertAlmostEqual(level["net_gex_0dte"], 18900.0, places=6)
        self.assertAlmostEqual(level["net_gex_all"], 18900.0, places=6)
        self.assertAlmostEqual(level["gamma_flip_0dte"], 99.25, places=6)
        self.assertEqual(level["call_wall_0dte"], 100.0)
        self.assertAlmostEqual(level["call_wall_0dte_gex"], 30000.0, places=4)
        self.assertEqual(level["put_wall_0dte"], 95.0)
        self.assertLess(level["put_wall_0dte_gex"], 0)
        self.assertAlmostEqual(level["put_wall_0dte_gex"], -12000.0, places=4)
        self.assertEqual(level["top1_strike"], 100.0)
        self.assertEqual(level["top2_strike"], 105.0)
        self.assertEqual(level["top3_strike"], 90.0)
        self.assertAlmostEqual(level["top1_abs_gex"], 20000.0, places=4)
        self.assertAlmostEqual(level["dist_flip_0dte_pts"], -0.75, places=6)
        self.assertAlmostEqual(level["dist_flip_0dte_pct"], -0.75, places=6)
        self.assertEqual(level["n_contracts"], 10)
        self.assertEqual(level["n_0dte"], 10)
        self.assertEqual(level["n_missing_greeks"], 0)
        self.assertEqual(level["total_oi"], 2160)
        self.assertEqual(level["sign_convention"], "dealer_long_calls_short_puts")
        self.assertIn("spot above the 0DTE flip by 0.75 pts (0.75%)", gex.reading_line(level))
        self.assertIn("nearest wall is the call wall at 100.00", gex.reading_line(level))

    def test_0dte_is_split_from_later_expiries(self):
        expiry = date(2026, 10, 23)
        moment = datetime(2026, 10, 23, 10, 30, tzinfo=ET)
        rows = gex.spy_sample_rows(expiry)
        rows.append(gex._row_from_spec("LATER", expiry + timedelta(days=3), 100, "call", 0.005, 100, 100.0))
        level = gex.build_level_row("SPY", moment, 100.0, "fixture", rows, 0.10, False, "fixture", "fixture")
        self.assertAlmostEqual(level["net_gex_0dte"], 18900.0, places=4)
        self.assertAlmostEqual(level["net_gex_all"], 23900.0, places=4)
        self.assertAlmostEqual(level["gamma_flip_0dte"], 99.25, places=6)
        self.assertAlmostEqual(level["gamma_flip_all"], 98.4, places=6)
        self.assertAlmostEqual(level["call_wall_0dte_gex"], 30000.0, places=4)
        self.assertAlmostEqual(level["call_wall_all_gex"], 35000.0, places=4)
        self.assertEqual(level["n_0dte"], 10)
        self.assertEqual(level["n_contracts"], 11)

    def test_volume_adjusted_adds_todays_volume(self):
        expiry = date(2026, 10, 23)
        moment = datetime(2026, 10, 23, 10, 30, tzinfo=ET)
        rows = gex.spy_sample_rows(expiry, volume_on_atm_call=300)
        level = gex.build_level_row("SPY", moment, 100.0, "fixture", rows, 0.10, False, "fixture", "fixture")
        # ATM call oi 300 + volume 300 doubles that contract's 30000 GEX.
        self.assertAlmostEqual(level["net_gex_0dte"], 18900.0, places=4)
        self.assertAlmostEqual(level["net_gex_0dte_voladj"], 48900.0, places=4)
        self.assertEqual(level["call_wall_0dte_voladj"], 100.0)
        self.assertEqual(level["total_volume"], 300)

    def test_cumulative_flip_edges(self):
        self.assertIsNone(gex.cumulative_flip({100: 5}, 100))
        self.assertIsNone(gex.cumulative_flip({90: 1, 100: 2, 110: 3}, 100))
        # Lands exactly on a strike, then leaves zero. The flip is that strike.
        self.assertEqual(gex.cumulative_flip({1: -5, 2: 5, 3: 5}, 3), 2)
        # Two crosses; keep the one closest to spot.
        self.assertAlmostEqual(gex.cumulative_flip({10: -1, 20: 2, 30: -2}, 22), 25.0, places=6)
        self.assertAlmostEqual(gex.cumulative_flip({10: -1, 20: 2, 30: -2}, 14), 15.0, places=6)

    def test_shifted_flip_follows_injected_gamma(self):
        rows = [
            {"strike": 90.0, "right": "put", "oi": 1000.0, "size": 100.0, "iv": 0.2, "t_years": 0.01},
            {"strike": 110.0, "right": "call", "oi": 1000.0, "size": 100.0, "iv": 0.2, "t_years": 0.01},
        ]

        def gamma_fn(hyp, row):
            if row["right"] == "put":
                return 0.05 if hyp <= 90 else 0.001
            return 0.001 if hyp <= 90 else 0.05

        flip = gex.shifted_flip(rows, 100.0, gamma_fn=gamma_fn)
        nets = []
        for hyp in (90.0, 110.0):
            net = 0.0
            for row in rows:
                net += gex.gex_dollars(gamma_fn(hyp, row), row["oi"], row["size"], hyp, row["right"])
            nets.append(net)
        self.assertLess(nets[0], 0)
        self.assertGreater(nets[1], 0)
        weight = abs(nets[0]) / (abs(nets[0]) + abs(nets[1]))
        self.assertAlmostEqual(flip, 90.0 + weight * 20.0, places=6)

        # IV on less than half the open interest blanks the shifted flip.
        thin = [
            {"strike": 90.0, "right": "call", "oi": 10.0, "size": 100.0, "iv": 0.2, "t_years": 0.01},
            {"strike": 110.0, "right": "put", "oi": 100.0, "size": 100.0, "iv": None, "t_years": 0.01},
        ]
        self.assertIsNone(gex.shifted_flip(thin, 100.0, gamma_fn=gamma_fn))

    def test_put_wall_is_the_most_negative_put_gex(self):
        rows = [
            gex._row_from_spec("A", date(2026, 10, 23), 90, "put", 0.01, 10, 100.0),
            gex._row_from_spec("B", date(2026, 10, 23), 95, "put", 0.01, 50, 100.0),
            gex._row_from_spec("C", date(2026, 10, 23), 100, "call", 0.01, 10, 100.0),
        ]
        level = gex.build_level_row(
            "SPY", datetime(2026, 10, 23, 10, 30, tzinfo=ET), 100.0, "fixture", rows, 0.10, False, "x", "x"
        )
        self.assertEqual(level["put_wall_0dte"], 95.0)
        self.assertLess(level["put_wall_0dte_gex"], 0)
        self.assertEqual(level["call_wall_0dte"], 100.0)

    def test_reading_below_flip_names_the_nearer_wall(self):
        row = {
            "ticker": "SPY",
            "spot": 100.0,
            "n_0dte": 3,
            "gamma_flip_0dte": 102.0,
            "call_wall_0dte": 110.0,
            "put_wall_0dte": 101.0,
            "gamma_flip_all": None,
            "call_wall_all": None,
            "put_wall_all": None,
        }
        line = gex.reading_line(row)
        self.assertIn("spot below the 0DTE flip by 2.00 pts (2.00%)", line)
        self.assertIn("nearest wall is the put wall at 101.00, 1.00 pts (1.00%) away", line)

    def test_select_expiries(self):
        today = date(2026, 10, 23)
        dates = [today, today + timedelta(days=1), today + timedelta(days=3), today + timedelta(days=4), today + timedelta(days=10)]
        self.assertEqual(gex.select_expiries(dates, today, extra=2)[:4], dates[:4])
        self.assertEqual(gex.select_expiries(dates, today, extra=0), [today, today + timedelta(days=1)])
        sunday = date(2026, 10, 25)
        self.assertEqual(
            gex.select_expiries(dates, sunday, extra=2),
            [today + timedelta(days=3), today + timedelta(days=4), today + timedelta(days=10)],
        )

    def test_session_gate(self):
        friday = datetime(2026, 10, 23, 10, 30, tzinfo=ET)
        calendar = [{"date": "2026-10-23", "open": "09:30", "close": "16:00"}]
        self.assertEqual(gex.session_status(friday, {"is_open": True}, calendar), (True, "open"))
        self.assertEqual(
            gex.session_status(friday.replace(hour=9, minute=29), {"is_open": True}, calendar)[1],
            "before the open",
        )
        self.assertEqual(
            gex.session_status(friday.replace(hour=16, minute=0), {"is_open": True}, calendar)[1],
            "after the close",
        )
        early = [{"date": "2026-10-23", "open": "09:30", "close": "13:00"}]
        self.assertEqual(gex.session_status(friday.replace(hour=12, minute=59), {"is_open": True}, early)[0], True)
        self.assertEqual(gex.session_status(friday.replace(hour=13, minute=0), {"is_open": False}, early)[1], "after the close")
        self.assertEqual(gex.session_status(friday, {"is_open": False}, calendar)[1], "clock closed")
        self.assertEqual(gex.session_status(friday, {"is_open": True}, [])[1], "holiday")
        saturday = datetime(2026, 10, 24, 10, 30, tzinfo=ET)
        self.assertEqual(gex.session_status(saturday, {"is_open": True}, [{"date": "2026-10-24", "open": "09:30", "close": "16:00"}])[1], "weekend")

    def test_dst_stamps(self):
        winter = datetime(2026, 1, 15, 9, 30, tzinfo=ET)
        summer = datetime(2026, 7, 15, 9, 30, tzinfo=ET)
        self.assertEqual(gex.stamps(winter), ("2026-01-15 09:30:00", "2026-01-15T14:30:00Z"))
        self.assertEqual(gex.stamps(summer), ("2026-07-15 09:30:00", "2026-07-15T13:30:00Z"))


class FileTests(unittest.TestCase):
    def setUp(self):
        gex._extra_secrets.clear()

    def test_dry_run_writes_csv_markdown_pine_and_gzip_without_keys(self):
        saved = {name: os.environ.pop(name) for name in ("ALPACA_KEY", "ALPACA_SECRET") if name in os.environ}
        try:
            with tempfile.TemporaryDirectory() as tmp:
                code = gex.main(["--dry-run", "--out", tmp])
                self.assertEqual(code, 0)
                levels = list(csv.DictReader(open(os.path.join(tmp, "gex_levels.csv"), encoding="utf-8")))
                self.assertEqual([row["ticker"] for row in levels], ["SPY", "QQQ"])
                self.assertEqual(levels[0]["timestamp_et"], "2026-10-23 10:30:00")
                self.assertEqual(levels[0]["timestamp_utc"], "2026-10-23T14:30:00Z")
                self.assertEqual(levels[0]["gamma_flip_0dte"], "99.2500")
                self.assertEqual(levels[0]["sign_convention"], "dealer_long_calls_short_puts")
                self.assertEqual(levels[0]["net_gex_0dte"], "18900.00")
                with gzip.open(os.path.join(tmp, "gex_strikes_2026-10-23.csv.gz"), "rt", encoding="utf-8") as handle:
                    strikes = list(csv.DictReader(handle))
                self.assertEqual(len(strikes), 13)
                self.assertTrue(all(row["dte_flag"] == "0dte" for row in strikes))
                markdown = Path(tmp, "GEX_LATEST.md").read_text(encoding="utf-8")
                self.assertIn("spot above the 0DTE flip", markdown)
                self.assertIn("no orders", markdown.lower())
                pine = Path(tmp, "GEX_PINE_SNIPPET.txt").read_text(encoding="utf-8")
                self.assertIn("//@version=6", pine)
                self.assertIn('input.float(99.25, "SPY gamma flip")', pine)
                self.assertIn('input.float(49.0, "QQQ gamma flip")', pine)
                self.assertIn("input.float", pine)
                # Second write of the same snapshot does not duplicate.
                gex.materialize(json.load(open(os.path.join(tmp, "last_run.json"), encoding="utf-8")), tmp)
                again = list(csv.DictReader(open(os.path.join(tmp, "gex_levels.csv"), encoding="utf-8")))
                self.assertEqual(len(again), 2)
                with gzip.open(os.path.join(tmp, "gex_strikes_2026-10-23.csv.gz"), "rt", encoding="utf-8") as handle:
                    self.assertEqual(len(list(csv.DictReader(handle))), 13)
                printed = io.StringIO()
                with redirect_stdout(printed):
                    self.assertEqual(gex.main(["--pine", "--out", tmp]), 0)
                self.assertIn("//@version=6", printed.getvalue())
                self.assertIn("99.25", printed.getvalue())
        finally:
            os.environ.update(saved)

    def test_fixture_flags_missing_greeks(self):
        payload = {
            "now_et": "2026-10-23T10:30:00-04:00",
            "tickers": {
                "SPY": {
                    "spot": 100,
                    "contracts": [
                        _contract("HAS", "2026-10-23", 100, "call", oi="10"),
                        _contract("FALLBACK", "2026-10-23", 100, "put", oi="10"),
                        _contract("NONE", "2026-10-23", 101, "call", oi="4"),
                    ],
                    "snapshots": {
                        "HAS": {"greeks": {"gamma": 0.01}, "impliedVolatility": 0.2, "dailyBar": {"v": 3}},
                        "FALLBACK": {"impliedVolatility": 0.2, "latestQuote": {"bp": 1.0, "ap": 1.1}},
                    },
                }
            },
        }
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "chain.json")
            json.dump(payload, open(path, "w", encoding="utf-8"))
            out = os.path.join(tmp, "out")
            self.assertEqual(gex.main(["--fixture", path, "--out", out]), 0)
            row = list(csv.DictReader(open(os.path.join(out, "gex_levels.csv"), encoding="utf-8")))[0]
            self.assertEqual(row["n_contracts"], "3")
            self.assertEqual(row["n_missing_greeks"], "2")
            self.assertEqual(row["n_gamma_bs_fallback"], "1")
            self.assertEqual(row["ticker"], "SPY")

    def test_append_second_timestamp(self):
        first = gex.demo_payload()
        second = json.loads(json.dumps(first))
        for row in second["level_rows"]:
            row["timestamp_et"] = "2026-10-23 10:35:00"
            row["timestamp_utc"] = "2026-10-23T14:35:00Z"
        for row in second["strike_rows"]:
            row["timestamp_et"] = "2026-10-23 10:35:00"
            row["timestamp_utc"] = "2026-10-23T14:35:00Z"
        with tempfile.TemporaryDirectory() as tmp:
            gex.materialize(first, tmp)
            gex.materialize(second, tmp)
            levels = list(csv.DictReader(open(os.path.join(tmp, "gex_levels.csv"), encoding="utf-8")))
            self.assertEqual(len(levels), 4)
            with gzip.open(os.path.join(tmp, "gex_strikes_2026-10-23.csv.gz"), "rt", encoding="utf-8") as handle:
                self.assertEqual(len(list(csv.DictReader(handle))), 26)


class ClientTests(unittest.TestCase):
    def setUp(self):
        gex._extra_secrets.clear()

    def test_live_path_pages_retries_redacts_and_places_no_orders(self):
        secret = "SECRETVALUE99"
        key = "KEYVALUE9999"
        urls = []
        state = {"snap": 0}

        def transport(url, headers, timeout):
            self.assertEqual(headers.get("APCA-API-KEY-ID"), key)
            self.assertEqual(headers.get("APCA-API-SECRET-KEY"), secret)
            parts = urllib.parse.urlsplit(url)
            self.assertNotIn("orders", parts.path)
            urls.append(url)
            query = urllib.parse.parse_qs(parts.query)
            if parts.path == "/v2/clock":
                return 200, {}, json.dumps({"is_open": True})
            if parts.path == "/v2/calendar":
                return 200, {}, json.dumps([{"date": "2026-10-23", "open": "09:30", "close": "16:00"}])
            if parts.path.endswith("/trades/latest"):
                symbol = parts.path.split("/")[3]
                price = 100 if symbol == "SPY" else 50
                return 200, {}, json.dumps({"trade": {"p": price}})
            if parts.path == "/v2/options/contracts":
                symbol = query["underlying_symbols"][0]
                strike = "100" if symbol == "SPY" else "50"
                token = (query.get("page_token") or [None])[0]
                if token is None:
                    body = {
                        "option_contracts": [_contract(symbol + "C", "2026-10-23", strike, "call")],
                        "next_page_token": "p2",
                    }
                else:
                    self.assertEqual(token, "p2")
                    body = {
                        "option_contracts": [_contract(symbol + "P", "2026-10-23", strike, "put")],
                        "next_page_token": None,
                    }
                return 200, {}, json.dumps(body)
            if parts.path.startswith("/v1beta1/options/snapshots/"):
                state["snap"] += 1
                if state["snap"] == 1:
                    return 429, {"Retry-After": "0"}, "slow SECRETVALUE99"
                symbol = parts.path.rstrip("/").split("/")[-1]
                strike = 100 if symbol == "SPY" else 50
                snaps = {
                    symbol + "C": {"greeks": {"gamma": 0.01}, "impliedVolatility": 0.2, "dailyBar": {"v": 0}},
                    symbol + "P": {"greeks": {"gamma": 0.01}, "impliedVolatility": 0.2, "dailyBar": {"v": 0}},
                }
                return 200, {}, json.dumps({"snapshots": snaps, "next_page_token": None})
            return 500, {}, "missing SECRETVALUE99"

        client = gex.AlpacaClient(key, secret, transport=transport, sleep_fn=lambda _seconds: None, max_pages=8)
        moment = datetime(2026, 10, 23, 10, 30, tzinfo=ET)
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            payload = gex.collect_live(client, moment, gex.settings_from_env())
        text = buffer.getvalue()
        self.assertNotIn(secret, text)
        self.assertNotIn(key, text)
        self.assertNotIn("SECRETVALUE99", text)
        spy = next(row for row in payload["level_rows"] if row["ticker"] == "SPY")
        qqq = next(row for row in payload["level_rows"] if row["ticker"] == "QQQ")
        self.assertEqual(spy["n_contracts"], 2)
        self.assertAlmostEqual(spy["net_gex_all"], 0.0, places=6)
        self.assertGreater(spy["call_wall_all_gex"], 0)
        self.assertLess(spy["put_wall_all_gex"], 0)
        self.assertEqual(spy["call_wall_all"], 100.0)
        self.assertEqual(qqq["call_wall_all"], 50.0)
        self.assertEqual(spy["spot_source"], "trade")
        self.assertGreaterEqual(state["snap"], 2)
        joined = "\n".join(urls)
        self.assertIn("https://paper-api.alpaca.markets/v2/clock", joined)
        self.assertIn("https://paper-api.alpaca.markets/v2/calendar", joined)
        self.assertIn("https://paper-api.alpaca.markets/v2/options/contracts", joined)
        self.assertIn("https://data.alpaca.markets/v1beta1/options/snapshots/SPY", joined)
        self.assertIn("feed=indicative", joined)
        self.assertIn("feed=iex", joined)
        self.assertIn("page_token=p2", joined)
        self.assertNotIn("/v2/orders", joined)
        for url in urls:
            path = urllib.parse.urlsplit(url).path
            self.assertTrue(
                path.startswith((
                    "/v2/clock",
                    "/v2/calendar",
                    "/v2/options/contracts",
                    "/v2/stocks/",
                    "/v1beta1/options/snapshots/",
                ))
            )

    def test_http_error_redacts_secret(self):
        secret = "SECRETVALUE99"

        def transport(url, headers, timeout):
            return 400, {}, "bad SECRETVALUE99"

        client = gex.AlpacaClient("KEYVALUE9999", secret, transport=transport, sleep_fn=lambda _s: None)
        with self.assertRaises(RuntimeError) as caught:
            client._get("https://paper-api.alpaca.markets/v2/clock")
        self.assertIn("[redacted]", str(caught.exception))
        self.assertNotIn(secret, str(caught.exception))

    def test_missing_keys_do_not_touch_the_network(self):
        saved = {name: os.environ.pop(name) for name in ("ALPACA_KEY", "ALPACA_SECRET") if name in os.environ}
        try:
            with tempfile.TemporaryDirectory() as tmp:
                buffer = io.StringIO()
                with redirect_stdout(buffer):
                    code = gex.main(["--out", tmp], now=datetime(2026, 10, 23, 10, 30, tzinfo=ET))
                self.assertEqual(code, 1)
                self.assertIn("ALPACA_KEY", buffer.getvalue())
                self.assertFalse(os.path.exists(os.path.join(tmp, "last_run.json")))
        finally:
            os.environ.update(saved)

    def test_closed_market_writes_nothing(self):
        class Closed:
            def clock(self):
                return {"is_open": False}

            def calendar(self, day):
                return [{"date": day.isoformat(), "open": "09:30", "close": "16:00"}]

        with tempfile.TemporaryDirectory() as tmp:
            code = gex.main(
                ["--out", tmp],
                client_factory=lambda: Closed(),
                now=datetime(2026, 10, 23, 10, 30, tzinfo=ET),
            )
            self.assertEqual(code, 0)
            self.assertFalse(os.path.exists(os.path.join(tmp, "last_run.json")))

        class Holiday:
            def clock(self):
                return {"is_open": False}

            def calendar(self, day):
                return []

        with tempfile.TemporaryDirectory() as tmp:
            code = gex.main(
                ["--out", tmp],
                client_factory=lambda: Holiday(),
                now=datetime(2026, 10, 23, 10, 30, tzinfo=ET),
            )
            self.assertEqual(code, 0)
            self.assertFalse(os.path.exists(os.path.join(tmp, "gex_levels.csv")))


class RepoTests(unittest.TestCase):
    def test_source_and_workflow_are_log_only(self):
        source = (ROOT / "gex_logger.py").read_text(encoding="utf-8")
        workflow = (ROOT / ".github" / "workflows" / "gex_logger.yml").read_text(encoding="utf-8")
        script = (ROOT / "scripts" / "publish_gex_branch.sh").read_text(encoding="utf-8")
        docs = (ROOT / "docs" / "GEX.md").read_text(encoding="utf-8")
        for blob in (source, workflow, script):
            self.assertNotIn("submit_order", blob)
            self.assertNotIn("/v2/orders", blob)
            self.assertNotIn("MarketOrderRequest", blob)
            self.assertNotIn("git push origin main", blob)
            self.assertNotIn("git push --force", blob)
            self.assertNotIn("git push -f", blob)
        self.assertIn("ALPACA_KEY", workflow)
        self.assertIn("ALPACA_SECRET", workflow)
        self.assertIn("secrets.ALPACA_KEY", workflow)
        self.assertIn("secrets.ALPACA_SECRET", workflow)
        self.assertIn("contents: write", workflow)
        self.assertIn("gex-logger", workflow)
        self.assertIn('cron: "*/5 13-21 * * 1-5"', workflow)
        self.assertIn("gex-data", script)
        self.assertIn("git push origin gex-data", script)
        self.assertIn("https://data.alpaca.markets", source)
        self.assertIn("https://paper-api.alpaca.markets", source)
        self.assertIn("/v1beta1/options/snapshots/", source)
        self.assertIn("/v2/options/contracts", source)
        self.assertIn("dealer_long_calls_short_puts", docs)
        self.assertIn("gamma_flip_0dte", docs)
        self.assertIn("holdout", docs.lower())
        self.assertIn("0.15%", docs)
        self.assertIn("gex-data", docs)
        # Cron hours cover both 13:30 UTC (09:30 EDT) and 21:00 UTC (16:00 EST).
        self.assertIn("13-21", workflow)
        self.assertEqual(len(gex.LEVEL_COLUMNS), len(set(gex.LEVEL_COLUMNS)))

    def test_publish_script_updates_gex_data_and_not_main(self):
        if shutil.which("git") is None:
            self.skipTest("git is not installed")
        payload = gex.demo_payload()
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp) / "repo"
            remote = Path(tmp) / "remote.git"
            subprocess.check_call(["git", "init", "--bare", "-b", "main", str(remote)], stdout=subprocess.DEVNULL)
            hook = remote / "hooks" / "pre-receive"
            hook.write_text(
                "#!/bin/sh\n"
                'flag="$(dirname "$0")/reject-once"\n'
                "while read old new ref; do\n"
                '  if [ "$ref" = "refs/heads/gex-data" ] && [ ! -f "$flag" ]; then\n'
                '    touch "$flag"\n'
                '    echo rejected >&2\n'
                "    exit 1\n"
                "  fi\n"
                "done\n"
                "exit 0\n",
                encoding="utf-8",
            )
            hook.chmod(0o755)
            subprocess.check_call(["git", "init", "-b", "main", str(repo)], stdout=subprocess.DEVNULL)
            env = os.environ.copy()
            env.update({
                "GIT_AUTHOR_NAME": "test",
                "GIT_AUTHOR_EMAIL": "test@example.com",
                "GIT_COMMITTER_NAME": "test",
                "GIT_COMMITTER_EMAIL": "test@example.com",
                "GEX_LOGGER_PY": str(ROOT / "gex_logger.py"),
                "GEX_PYTHON": sys.executable,
                "GEX_PUSH_RETRY_SLEEP": "0",
            })
            def git(*args, cwd=repo):
                return subprocess.check_call(["git", *args], cwd=cwd, env=env, stdout=subprocess.DEVNULL)

            (repo / "README.md").write_text("base\n", encoding="utf-8")
            git("add", "README.md")
            git("commit", "-m", "base")
            git("remote", "add", "origin", str(remote))
            git("push", "-u", "origin", "main")
            main_sha = subprocess.check_output(["git", "rev-parse", "main"], cwd=repo, env=env, text=True).strip()

            snapshot = Path(tmp) / "last_run.json"
            snapshot.write_text(json.dumps(payload), encoding="utf-8")
            subprocess.check_call(
                ["bash", str(ROOT / "scripts" / "publish_gex_branch.sh"), str(snapshot)],
                cwd=repo,
                env=env,
            )
            self.assertTrue((remote / "hooks" / "reject-once").exists())
            after_main = subprocess.check_output(["git", "rev-parse", "main"], cwd=repo, env=env, text=True).strip()
            self.assertEqual(after_main, main_sha)
            listed = subprocess.check_output(["git", "ls-tree", "-r", "main", "--name-only"], cwd=repo, env=env, text=True)
            self.assertNotIn("gex_levels.csv", listed)
            remote_files = subprocess.check_output(
                ["git", "ls-tree", "-r", "gex-data", "--name-only"], cwd=repo, env=env, text=True
            )
            self.assertIn("results/gex/gex_levels.csv", remote_files)
            self.assertIn("results/gex/GEX_PINE_SNIPPET.txt", remote_files)

            # Same snapshot again: no duplicate rows.
            subprocess.check_call(
                ["bash", str(ROOT / "scripts" / "publish_gex_branch.sh"), str(snapshot)],
                cwd=repo,
                env=env,
            )
            csv_text = subprocess.check_output(
                ["git", "show", "gex-data:results/gex/gex_levels.csv"], cwd=repo, env=env, text=True
            )
            rows = list(csv.DictReader(io.StringIO(csv_text)))
            self.assertEqual(len(rows), 2)
            self.assertEqual(sorted(row["ticker"] for row in rows), ["QQQ", "SPY"])

            # A second clone appends a later timestamp; the first repo then appends a third.
            other = Path(tmp) / "other"
            subprocess.check_call(
                ["git", "clone", str(remote), str(other)],
                env=env,
                stdout=subprocess.DEVNULL,
            )
            subprocess.check_call(["git", "checkout", "gex-data"], cwd=other, env=env, stdout=subprocess.DEVNULL)
            later = json.loads(json.dumps(payload))
            for row in later["level_rows"]:
                row["timestamp_et"] = "2026-10-23 10:35:00"
            for row in later["strike_rows"]:
                row["timestamp_et"] = "2026-10-23 10:35:00"
            later_path = Path(tmp) / "later.json"
            later_path.write_text(json.dumps(later), encoding="utf-8")
            subprocess.check_call(
                ["bash", str(ROOT / "scripts" / "publish_gex_branch.sh"), str(later_path)],
                cwd=other,
                env=env,
            )
            third = json.loads(json.dumps(payload))
            for row in third["level_rows"]:
                row["timestamp_et"] = "2026-10-23 10:40:00"
            for row in third["strike_rows"]:
                row["timestamp_et"] = "2026-10-23 10:40:00"
            third_path = Path(tmp) / "third.json"
            third_path.write_text(json.dumps(third), encoding="utf-8")
            subprocess.check_call(
                ["bash", str(ROOT / "scripts" / "publish_gex_branch.sh"), str(third_path)],
                cwd=repo,
                env=env,
            )
            merged = subprocess.check_output(
                ["git", "show", "gex-data:results/gex/gex_levels.csv"], cwd=repo, env=env, text=True
            )
            merged_rows = list(csv.DictReader(io.StringIO(merged)))
            keys = [(row["ticker"], row["timestamp_et"]) for row in merged_rows]
            self.assertEqual(len(keys), len(set(keys)))
            self.assertEqual(len(merged_rows), 6)
            still_main = subprocess.check_output(["git", "rev-parse", "main"], cwd=repo, env=env, text=True).strip()
            self.assertEqual(still_main, main_sha)


if __name__ == "__main__":
    unittest.main()
