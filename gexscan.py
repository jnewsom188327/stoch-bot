"""
GEX + FLOW SCAN - the Clean Scan, upgraded: every 5 minutes, 15 liquid tickers, ranked on one board (gex_board.md).
LOG ONLY - this bot never sends an order. Keys come from GitHub Secrets ALPACA_KEY / ALPACA_SECRET.

FOR EVERY TICKER, EVERY SCAN:
  TREND  : the Clean Scan on closed 5-minute candles (Clean, ADX, RVol, long / short / out) - same math as cleanbot.py.
  GEX    : dealer gamma from the option chain (gamma x open interest x 100 x price^2 x 1%), calls +, puts -, strikes within
           10% and expirations within 30 days. Gives: NET GEX ($ per 1% move), the GAMMA FLIP (price where net GEX crosses 0),
           the CALL WALL (biggest call gamma strike) and PUT WALL (biggest put gamma strike), and how much of it is 0DTE.
           Positive gamma = dealers sell rips / buy dips (moves get pinned). Negative gamma = dealers chase (moves run).
  FLOW   : REAL TIME from the option chain: contracts traded since the last scan (today's volume change) x the last price,
           near the money (within 5%, 0-7 DTE), tagged BUY (last trade at / near the ask) or SELL (at / near the bid).
           Bullish $ = calls bought + puts sold, bearish $ = puts bought + calls sold.
           BIG PRINTS = single trades over $100k (SPY / QQQ), $50k (IWM), $25k (stocks) from the option trades feed - on the
           free Alpaca plan that feed is 16 minutes behind, so big prints show 16 minutes late (the board says so).
           UNUSUAL = contracts that traded more than their open interest today (500+ contracts).
  PICK   : for every ticker with a bias, the best contract for the move: calls or puts, 0-7 DTE, ask $0.40-$0.80, delta 0.20+,
           spread under 20%, 50+ open interest or volume. Target = the next GEX level that way (walls / flip) if it is in
           reach, else 2.5 x the 5-minute ATR. Juice = % gain if price gets there in ~30 min (delta + gamma - time decay,
           sold at the bid). The pick = the most juice.
  FIRE   : watch score 45+ with a bias (not before 9:35, not after 15:30, 30-minute cooldown per ticker and side) = the
           picked contract is "bought" at the ask on paper and its REAL bid is followed every 30 seconds for 60 minutes:
           % at 15 / 30 / 60 min, best %, worst %, when it first hit +25% / +50% / +100% / -30%, and whether price hit the
           target. Saved to gex_fires.csv - that is the grade. No orders are sent.
  SETUP  : one plain call per ticker (RUN, TREND + FLOW, PIN AT A WALL, FLOW SURGE, FLIP CROSS) with a bias
           (CALLS / PUTS) and a 0-100 WATCH SCORE. The score is a ranking, NOT a tested edge - the logs are for grading it.
  1m RULES (SPY + QQQ, LOOSE): every minute, the Trend Flip backtest's rules on the 1-minute chart, same math as
           backtest.py (it is imported, not copied):
             WHIPSAW    = Vix Fix side breaks back under 100 with the other side 60+ (first break) -> reversal
                          tags R2 = TTM with you / turning your way, R5 = within 1 ATR of VWAP, R6 = both
             FAILED POP = red / pink line, candle closes back down through it, greed 60-90 + fear 10-30 -> PUTS
                          tag R4 = TTM not turning away
           LOOSE = every whipsaw and every failed pop fires (the tags say which tighter rule it also meets, so it can be
           tightened from the log). Contract: 0-1 DTE, $0.40-$0.80, delta 0.15+, target 3 x the 1-minute ATR. Tracked
           exactly like the other FIRES (+ the 20-minute mark = the backtest's exit). Every signal, fired or not, goes to
           gex_rules.csv with the reason.
  v3 (after the Oct 28 grade): a fire needs its contract worth +20% at the target (+10% for the 1m rules); FLOW SURGE
           fires only when price moved with the flow (last 15 min) and sits on the right side of EMA 20; every fire also
           records what a +40% take-profit and selling at the target would have paid (tp40_pct, sell_at_target_pct) and
           three trailing exits off the real bid (lock_pct: +15% then never below +5%; trail_pct: +20% then 20% off the best,
           floor break-even; tpbe_pct: +40% or break-even after +15%);
           the 1m AGREE FLIP is logged (never traded); the board shows the last 1m check and any 1m error.
  GREEKS : if the free feed leaves out greeks on a contract, delta / gamma / theta are worked out (Black-Scholes) from
           its implied volatility, or from its own mid price. The board says how many were filled in.
LOGS (committed to the repo):
  gex_board.md   - the live board (pushed every 10 minutes, open it on GitHub)
  gex_log.csv    - one row per ticker per scan: price, every GEX level, flow $, trend numbers, setup, score
  gex_prints.csv - every big print and every unusual-volume contract
  gex_fires.csv  - every FIRE and what the contract actually did
  gex_state.json - today's running flow totals (so the next scheduled run picks up the day)
Free Alpaca data: option quotes / greeks are the 'indicative' feed. If recent option trades are not allowed on the
plan, flow automatically runs 16 minutes behind and the board says so.
"""
import csv
import json
import math
import os
import subprocess
import sys
import time
from datetime import date, datetime, timedelta, timezone
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd

# ===== SETTINGS (edit here) =====
SYMBOLS = ["SPY", "QQQ", "IWM", "SMH", "NVDA", "TSLA", "AAPL", "AMD", "META", "AMZN",
           "MSFT", "GOOGL", "NFLX", "AVGO", "PLTR", "COIN", "DELL", "SMCI", "MU", "MSTR",
           "ORCL", "HOOD", "ARM", "UBER", "CRM", "SHOP", "BABA"]
MAX_DTE = 30                 # expirations used for GEX
STRIKE_PCT = 0.10            # strikes within this % of the price (GEX)
FLOW_DTE = 7                 # expirations watched for flow
FLOW_PCT = 0.05              # strikes within this % of the price (flow)
BIG_PREM = {"SPY": 100_000, "QQQ": 100_000, "IWM": 50_000}
BIG_PREM_DEFAULT = 25_000
UNUSUAL_MIN = 500            # contracts traded today, and more than the open interest
WALL_NEAR = 0.0025           # "at a wall" = within 0.25%
SCAN_MIN = 5
SCAN_FROM, SCAN_TO = 935, 1555
PUSH_EVERY = 2               # push the board every N scans (2 x 5 min = 10 min)
RUN_MINUTES = 340
RATE = 0.04                  # risk-free rate for the gamma-flip math
FEED = os.getenv("OPTIONS_FEED", "indicative").strip().lower()   # "indicative" (free) or "opra" (paid)
BOARD, LOG, PRINTS, STATE = "gex_board.md", "gex_log.csv", "gex_prints.csv", "gex_state.json"
FIRES = "gex_fires.csv"
# ===== the contract picker + FIRES =====
PICK_MIN, PICK_MAX = 0.40, 0.80   # option price (the ask) must be in this range
PICK_DTE = 7                 # expirations the picker may use
PICK_SPREAD = 0.30           # bid / ask spread at most this share of the mid (free 'indicative' quotes run wider)
PICK_LIQ = 50                # open interest OR today's volume at least this
PICK_DELTA = 0.20            # delta at least this (no lottery tickets that need a miracle)
PICK_ATR = 2.5               # no GEX level close enough? the target = 2.5 x the 5-minute ATR (about a 30-minute move)
PICK_HOLD = 30               # minutes the move is assumed to take (time decay in the juice math)
FIRE_MIN = 45                # watch score needed to FIRE
FIRE_COOL = 30               # minutes before the same ticker can fire the same way again
TRACK_MIN = 60               # each fired contract is followed this long (or to 15:55)
TRACK_SECS = 30              # how often fired contracts are re-quoted
# ===== 1m RULES on SPY + QQQ (loose) =====
RULE_ON = os.getenv("RULES", "1").strip() != "0"
RULE_SYMS = ["SPY", "QQQ"]
RULE_COOL = 5                # minutes before the same ticker can rule-fire the same way again
RULE_DTE = 1                 # 0-1 DTE for the 1m scalps
RULE_DELTA = 0.15            # loose: delta at least this
RULE_TGT = 3.0               # target = this x the 1-minute ATR
RULE_HOLD = 20               # minutes (the backtest's exit = 20 candles later)
RULE_LATE = 3                # a signal first seen more than this many minutes after its candle closed is logged, not fired
RULES = "gex_rules.csv"
# ===== v3 fixes (after the Oct 28 grade) =====
PICK_MIN_JUICE = 0.20        # GEX fires: the contract must be worth at least +20% if price reaches the target
RULE_MIN_JUICE = 0.10        # 1m rule fires: at least +10% at the (small, 3 x 1m ATR) target - never a contract that loses when right
SURGE_CONFIRM = 3            # FLOW SURGE fires only if price moved WITH the flow over the last 3 five-minute candles + is on the right side of EMA 20
TP_PCT = 0.40                # take-profit tracking: what +40% (and selling at the target) would have paid - graded, not traded
# trailing exits, graded on every fire from the real bid every 30 s (never traded):
#   LOCK  = once it is +15% green, sell if it falls back to +5% (never let a green trade go red)
#   TRAIL = once it is +20% green, sell if the bid drops 20% from its best (floor: break-even)
#   TPBE  = sell at +40%, or at break-even once it has been +15%
LOCK_ARM, LOCK_FLOOR = 0.15, 0.05
TRAIL_ARM, TRAIL_GIVE = 0.20, 0.20
AGREE_LOG = True             # log the 1m AGREE FLIP (fear peak -> TTM up + agree up + squeeze fired + green line) - log only, never fires

ET = ZoneInfo("America/New_York")
KEY = os.getenv("ALPACA_KEY", "").strip()
SECRET = os.getenv("ALPACA_SECRET", "").strip()
FLOW_DELAY = [0]             # minutes the flow runs behind (set to 16 if the plan blocks recent option trades)
PICK_WHY = [""]              # why the last pick found what it found (shown when no contract qualifies)
VOL_SEEN = {}                # today's volume per contract at the last scan (real-time flow = the change)
ERRS = {}                    # data problems this scan (shown on the board so they can be fixed without the job log)


def note_err(where, e):
    import traceback
    msg = f"{type(e).__name__}: {str(e)[:400]}"
    if where not in ERRS:
        log(f"PROBLEM {where}: {msg}\n{traceback.format_exc()[-1500:]}")
    ERRS[where] = msg


def now_et():
    return datetime.now(ET)


def sleep(s):
    time.sleep(max(0.0, s))


def log(msg):
    print(now_et().strftime("%H:%M:%S"), msg, flush=True)


def hhmm(t):
    return t.hour * 100 + t.minute


# ===== math =====
def bs_gamma(S, K, T, iv, r=RATE):
    S, K, T, iv = (np.asarray(x, float) for x in (S, K, T, iv))
    sq = iv * np.sqrt(T)
    with np.errstate(divide="ignore", invalid="ignore"):
        d1 = (np.log(S / K) + (r + 0.5 * iv * iv) * T) / sq
        g = np.exp(-0.5 * d1 * d1) / (np.sqrt(2 * np.pi) * S * sq)
    return np.nan_to_num(g)


def bs_greeks(S, K, T, iv, cp, r=RATE):
    """Black-Scholes (price, delta, gamma, theta per calendar day) for one contract; None if it cannot be priced"""
    if not (S > 0 and K > 0 and T > 0 and iv > 0):
        return None
    sq = iv * math.sqrt(T)
    d1 = (math.log(S / K) + (r + 0.5 * iv * iv) * T) / sq
    d2 = d1 - sq
    N = lambda x: 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))  # noqa: E731
    pdf = math.exp(-0.5 * d1 * d1) / math.sqrt(2 * math.pi)
    disc = math.exp(-r * T)
    price = cp * (S * N(cp * d1) - K * disc * N(cp * d2))
    delta = N(d1) if cp == 1 else N(d1) - 1.0
    gamma = pdf / (S * sq)
    theta = (-S * pdf * iv / (2 * math.sqrt(T)) - cp * r * K * disc * N(cp * d2)) / 365.0
    return price, delta, gamma, theta


def implied_vol(px, S, K, T, cp):
    """the volatility that prices the contract at px (bisection); 0 if px is at / under intrinsic or unusable"""
    if not (px > 0 and S > 0 and K > 0 and T > 0) or px <= max(0.0, cp * (S - K)) + 0.005:
        return 0.0
    lo, hi = 0.01, 5.0
    if bs_greeks(S, K, T, hi, cp)[0] < px:
        return 0.0
    for _ in range(50):
        mid = 0.5 * (lo + hi)
        if bs_greeks(S, K, T, mid, cp)[0] > px:
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)


def occ_parse(sym):
    """'SPY261027C00680000' -> ('SPY', date, +1 call / -1 put, strike)"""
    i = len(sym) - 15
    root, ymd, cp, k = sym[:i], sym[i:i + 6], sym[i + 6], sym[i + 7:]
    return root, date(2000 + int(ymd[:2]), int(ymd[2:4]), int(ymd[4:6])), (1 if cp == "C" else -1), int(k) / 1000.0


def years_to(exp, t):
    close = datetime(exp.year, exp.month, exp.day, 16, 0, tzinfo=ET)
    return max((close - t).total_seconds(), 3600.0) / (365.0 * 24 * 3600)


# ===== data (small wrappers so the simulator can swap them) =====
def fetch_bars(dc):
    """closed 5-minute candles, regular hours, last 14 days, every ticker (IEX feed)"""
    from alpaca.data.enums import DataFeed
    from alpaca.data.requests import StockBarsRequest
    from alpaca.data.timeframe import TimeFrame, TimeFrameUnit
    now = datetime.now(timezone.utc)
    df = dc.get_stock_bars(StockBarsRequest(symbol_or_symbols=SYMBOLS, timeframe=TimeFrame(5, TimeFrameUnit.Minute),
                                            start=now - timedelta(days=14), end=now, feed=DataFeed.IEX)).df
    out = {}
    if df is None or df.empty:
        return out
    cut = pd.Timestamp(now).tz_convert(ET)
    for s in SYMBOLS:
        try:
            d = df.xs(s, level=0) if isinstance(df.index, pd.MultiIndex) else df
        except KeyError:
            continue
        d = d.sort_index()
        d.index = d.index.tz_convert(ET)
        d = d[d.index + pd.Timedelta(minutes=5) <= cut]
        hm = d.index.hour * 100 + d.index.minute
        out[s] = d[(hm >= 930) & (hm < 1600)][["open", "high", "low", "close", "volume"]].astype(float)
    return out


def fetch_oi(tc, sym, lo, hi, today):
    """open interest for every contract in the window (once a day per ticker): {contract: oi}"""
    from alpaca.trading.requests import GetOptionContractsRequest
    out, tok = {}, None
    for _ in range(20):
        req = GetOptionContractsRequest(underlying_symbols=[sym], expiration_date_gte=today,
                                        expiration_date_lte=today + timedelta(days=MAX_DTE),
                                        strike_price_gte=str(round(lo, 2)), strike_price_lte=str(round(hi, 2)),
                                        limit=10000, page_token=tok)
        r = tc.get_option_contracts(req)
        for c in (r.option_contracts or []):
            try:
                out[c.symbol] = float(c.open_interest or 0)
            except (TypeError, ValueError):
                out[c.symbol] = 0.0
        tok = getattr(r, "next_page_token", None)
        if not tok:
            break
    return out


def fetch_chain(oc, sym, lo, hi, today):
    """raw option chain snapshots: {contract: {latestQuote, latestTrade, greeks, impliedVolatility, dailyBar, ...}}"""
    from alpaca.data.enums import OptionsFeed
    from alpaca.data.requests import OptionChainRequest
    req = OptionChainRequest(underlying_symbol=sym, feed=OptionsFeed.OPRA if FEED == "opra" else OptionsFeed.INDICATIVE,
                             strike_price_gte=round(lo, 2), strike_price_lte=round(hi, 2),
                             expiration_date_gte=today, expiration_date_lte=today + timedelta(days=MAX_DTE))
    return oc.get_option_chain(req) or {}


def fetch_trades(oc, contracts, start, end):
    """raw option trades {contract: [{t, p, s, x, c}, ...]} between start and end"""
    from alpaca.data.requests import OptionTradesRequest
    out = {}
    cl = sorted(contracts)
    for i in range(0, len(cl), 100):
        r = oc.get_option_trades(OptionTradesRequest(symbol_or_symbols=cl[i:i + 100], start=start, end=end)) or {}
        for k, v in r.items():
            out.setdefault(k, []).extend(v or [])
    return out


def fetch_quotes(oc, contracts):
    """latest bid / ask for a few contracts: {contract: (bid, ask)}"""
    from alpaca.data.enums import OptionsFeed
    from alpaca.data.requests import OptionLatestQuoteRequest
    out = {}
    for i in range(0, len(contracts), 100):
        r = oc.get_option_latest_quote(OptionLatestQuoteRequest(symbol_or_symbols=contracts[i:i + 100],
                                       feed=OptionsFeed.OPRA if FEED == "opra" else OptionsFeed.INDICATIVE)) or {}
        for k, v in r.items():
            out[k] = (float(v.get("bp", 0) or 0), float(v.get("ap", 0) or 0))
    return out


def parse_chain(chain, oi, today, spot, t):
    """raw chain snapshots -> GEX rows, quotes, today's volume, picker rows, last prices, and how many contracts had their
    greeks worked out here because the feed left them out"""
    rows, quotes, vol_today, crow, last_px, filled = [], {}, {}, [], {}, 0
    for c, s in chain.items():
        try:
            _, exp, cp, k = occ_parse(c)
        except Exception:  # noqa: BLE001
            continue
        q = s.get("latestQuote") or {}
        bid, ask = float(q.get("bp", 0) or 0), float(q.get("ap", 0) or 0)
        quotes[c] = (bid, ask)
        lt = s.get("latestTrade") or {}
        last_px[c] = float(lt.get("p", 0) or 0)
        db = s.get("dailyBar") or {}
        # only TODAY's bar counts (early in the day the free feed still shows yesterday's bar)
        vol_today[c] = float(db.get("v", 0) or 0) if str(db.get("t", ""))[:10] == today.isoformat() else 0.0
        gm = s.get("greeks") or {}
        iv = float(s.get("impliedVolatility") or 0)
        delta, gamma, theta = float(gm.get("delta") or 0), float(gm.get("gamma") or 0), float(gm.get("theta") or 0)
        if delta == 0 or gamma == 0:
            # greeks missing: work them out from the implied vol, or from the contract's own mid (else last trade)
            T = years_to(exp, t)
            if not iv > 0:
                px = (bid + ask) / 2 if bid > 0 and ask >= bid else last_px[c]
                iv = implied_vol(px, spot, k, T, cp)
            g = bs_greeks(spot, k, T, iv, cp) if iv > 0 else None
            if g:
                _, delta, gamma, theta = g
                filled += 1
        rows.append(dict(cp=cp, K=k, exp=exp, iv=iv, gamma=gamma, oi=float(oi.get(c, 0))))
        crow.append(dict(contract=c, cp=cp, K=k, exp=exp, dte=(exp - today).days, bid=bid, ask=ask,
                         delta=delta, gamma=gamma, theta=theta, vol=vol_today[c], oi=float(oi.get(c, 0))))
    return rows, quotes, vol_today, crow, last_px, filled


# ===== one ticker =====
def gex_levels(rows, spot, t):
    """rows: list of dicts (cp, K, exp, iv, gamma, oi). Returns the GEX levels."""
    if not rows:
        return None
    d = pd.DataFrame(rows)
    d = d[(d["oi"] > 0) & (d["iv"] > 0.01) & (d["iv"] < 5)]
    if d.empty:
        return None
    d["T"] = [years_to(e, t) for e in d["exp"]]
    g = np.where(d["gamma"] > 0, d["gamma"], bs_gamma(spot, d["K"], d["T"], d["iv"]))
    d["gex"] = d["cp"] * g * d["oi"] * 100 * spot * spot * 0.01
    net = float(d["gex"].sum())
    today = t.date()
    net0 = float(d.loc[d["exp"] == today, "gex"].sum())
    gross = float(d["gex"].abs().sum())
    calls = d[d["cp"] == 1].groupby("K")["gex"].sum()
    puts = d[d["cp"] == -1].groupby("K")["gex"].sum()
    cw = float(calls.idxmax()) if len(calls) else np.nan
    pw = float(puts.idxmin()) if len(puts) else np.nan
    c0 = d[(d["cp"] == 1) & (d["exp"] == today)].groupby("K")["gex"].sum()
    p0 = d[(d["cp"] == -1) & (d["exp"] == today)].groupby("K")["gex"].sum()
    # gamma flip: re-price every contract's gamma across a +/-6% grid of prices, find where net GEX crosses zero
    grid = spot * (1 + np.linspace(-0.06, 0.06, 121))
    K, T, iv, w = d["K"].to_numpy(), d["T"].to_numpy(), d["iv"].to_numpy(), (d["cp"] * d["oi"]).to_numpy()
    prof = np.array([float((bs_gamma(s, K, T, iv) * w).sum() * 100 * s * s * 0.01) for s in grid])
    flip = np.nan
    cross = np.nonzero(np.sign(prof[:-1]) != np.sign(prof[1:]))[0]
    if len(cross):
        j = cross[np.argmin(np.abs(grid[cross] - spot))]
        a, b = prof[j], prof[j + 1]
        flip = float(grid[j] + (grid[j + 1] - grid[j]) * (a / (a - b))) if a != b else float(grid[j])
    return dict(net=net, net0=net0, share0=abs(net0) / gross if gross else 0.0, flip=flip, call_wall=cw, put_wall=pw,
                call_wall0=float(c0.idxmax()) if len(c0) else np.nan, put_wall0=float(p0.idxmin()) if len(p0) else np.nan)


def side_of(p, bid, ask):
    if bid > 0 and ask > 0 and ask >= bid:
        mid, half = (bid + ask) / 2, max((ask - bid) / 2, 0.01)
        if p >= mid + 0.5 * half:
            return "BUY"
        if p <= mid - 0.5 * half:
            return "SELL"
    return "MID"


def flow_of(sym, trades, quotes, oi, vol_today, t):
    """flow totals for this window + big prints"""
    big = BIG_PREM.get(sym, BIG_PREM_DEFAULT)
    tot = dict(cb=0.0, cs=0.0, pb=0.0, ps=0.0)
    prints = []
    for c, lst in trades.items():
        try:
            _, exp, cp, k = occ_parse(c)
        except Exception:  # noqa: BLE001
            continue
        bid, ask = quotes.get(c, (0.0, 0.0))
        for tr in lst:
            p, s = float(tr.get("p", 0) or 0), float(tr.get("s", 0) or 0)
            prem = p * s * 100
            sd = side_of(p, bid, ask)
            if sd == "BUY":
                tot["cb" if cp == 1 else "pb"] += prem
            elif sd == "SELL":
                tot["cs" if cp == 1 else "ps"] += prem
            if prem >= big:
                prints.append(dict(t=t.isoformat(timespec="seconds"), trade_time=str(tr.get("t", ""))[:19], sym=sym, kind="BIG PRINT",
                                   contract=c, type="CALL" if cp == 1 else "PUT", strike=k, exp=exp.isoformat(), dte=(exp - t.date()).days,
                                   size=int(s), price=p, premium=round(prem), side=sd, vol_today=int(vol_today.get(c, 0)),
                                   oi=int(oi.get(c, 0))))
    return tot, prints


def setup_of(r):
    """plain-English call + bias + 0-100 watch score (a ranking, not a tested edge)"""
    st, flow_dir, strength = r["trend"], np.sign(r["flow_net_day"]), r["flow_strength"]
    neg = r["net_gex"] < 0
    spot = r["price"]
    near_cw = np.isfinite(r["call_wall"]) and abs(spot - r["call_wall"]) / spot <= WALL_NEAR
    near_pw = np.isfinite(r["put_wall"]) and abs(spot - r["put_wall"]) / spot <= WALL_NEAR
    big_dir = np.sign(r["big_bull_15"] - r["big_bear_15"])
    crossed = r.get("flip_cross", 0)
    trend_pts = (min(r["clean"], 60) / 60 * 15 + min(r["adx"], 45) / 45 * 10 + min(r["rvol"], 2.5) / 2.5 * 10) if st != 0 else \
        (min(r["adx"], 45) / 45 * 8 + min(r["rvol"], 2.5) / 2.5 * 5)
    flow_pts = min(strength, 1.0) * 20 + (10 if big_dir != 0 and (st == 0 or big_dir == st) else 0)
    if st != 0 and neg and flow_dir == st:
        name, bias, g_pts = "RUN: clean trend + negative gamma + flow agrees", st, 20
    elif st != 0 and flow_dir == st:
        name, bias, g_pts = "TREND + FLOW", st, 8 if neg else 4
    elif not neg and near_cw and near_pw:
        name, bias, g_pts = "PINNED between the walls (positive gamma) - chop", 0, 10
    elif not neg and near_cw:
        name, bias, g_pts = "PIN AT CALL WALL (positive gamma) - fade", -1, 15
    elif not neg and near_pw:
        name, bias, g_pts = "PIN AT PUT WALL (positive gamma) - bounce", 1, 15
    elif strength >= 0.5 and big_dir != 0 and big_dir == flow_dir:
        name, bias, g_pts = "FLOW SURGE", int(flow_dir), 8 if neg else 4
    elif crossed != 0:
        name, bias, g_pts = "FLIP CROSS " + ("up into positive gamma" if crossed == 1 else "down into negative gamma"), crossed, 10
    elif st != 0:
        name, bias, g_pts = "TREND (flow not with it)", st, 0
    else:
        name, bias, g_pts = "-", 0, 0
    score = int(round(min(100.0, trend_pts + flow_pts + g_pts + (min(r["rvol"], 3) / 3 * 15 if name != "-" else 0))))
    return name, int(bias), score


def target_of(r, bias, atr5):
    """where the move is headed: the nearest GEX level that way (call wall, put wall, flip, 0DTE walls) if it is within
    reach, otherwise 2.5 x the 5-minute ATR"""
    spot = r["price"]
    lv = [r[k] for k in ("call_wall", "put_wall", "flip", "call_wall_0dte", "put_wall_0dte")]
    lv = [x for x in lv if x is not None and np.isfinite(x)]
    if bias == 1:
        cand = sorted(x for x in lv if x >= spot + 0.5 * atr5)
    else:
        cand = sorted((x for x in lv if x <= spot - 0.5 * atr5), reverse=True)
    if cand and abs(cand[0] - spot) <= 2 * PICK_ATR * atr5:
        return float(cand[0]), "GEX level"
    return float(spot + bias * PICK_ATR * atr5), "2.5 ATR"


def pick_contract(crow, spot, bias, target, dte=None, dmin=None, hold=None, minj=None):
    """among calls (bias +1) or puts (-1), 0-7 DTE, ask $0.40-$0.80, delta 0.20+, tight enough and traded enough:
    the one with the biggest % gain if price reaches the target in about 30 minutes
    (value at the target = mid + delta x move + 1/2 gamma x move^2 + 30 minutes of time decay, sold at the bid)
    dte / dmin / hold override PICK_DTE / PICK_DELTA / PICK_HOLD (the 1m rules use 0-1 DTE, delta 0.15, 20 minutes)"""
    dte = PICK_DTE if dte is None else dte
    dmin = PICK_DELTA if dmin is None else dmin
    hold = PICK_HOLD if hold is None else hold
    mv = target - spot
    best = None
    why = dict(side=0, price=0, delta=0, spread=0, liq=0)
    for o in crow:
        if o["cp"] != bias or o["dte"] > dte:
            continue
        why["side"] += 1
        bid, ask = o["bid"], o["ask"]
        if not (PICK_MIN <= ask <= PICK_MAX) or bid <= 0 or ask < bid:
            continue
        why["price"] += 1
        if abs(o["delta"]) < dmin:
            continue
        why["delta"] += 1
        mid = (bid + ask) / 2
        if (ask - bid) / mid > PICK_SPREAD:
            continue
        why["spread"] += 1
        if o["oi"] < PICK_LIQ and o["vol"] < PICK_LIQ:
            continue
        why["liq"] += 1
        est = mid + o["delta"] * mv + 0.5 * o["gamma"] * mv * mv + o["theta"] * hold / 390
        est = max(est, max(0.0, (target - o["K"]) if bias == 1 else (o["K"] - target)))
        sell = max(est - (ask - bid) / 2, 0.0)
        juice = sell / ask - 1
        if best is None or juice > best["juice"] or (juice == best["juice"] and o["vol"] > best["vol"]):
            best = dict(o, est=sell, juice=juice)
    PICK_WHY[0] = (f"{why['side']} {'calls' if bias == 1 else 'puts'} 0-{dte}DTE > {why['price']} priced {PICK_MIN:.2f}-{PICK_MAX:.2f} > "
                   f"{why['delta']} delta {dmin}+ > {why['spread']} spread ok > {why['liq']} liquid")
    minj = PICK_MIN_JUICE if minj is None else minj
    if best is not None and best["juice"] < minj:
        PICK_WHY[0] += f" > best one only {best['juice'] * 100:+.0f}% at the target (needs +{minj * 100:.0f}%)"
        return None
    return best


def scan_ticker(sym, tc, oc, bars, st_day, t, delay_min):
    import cleanbot as CB
    d = bars.get(sym)
    if d is None or len(d) < 50:
        return None, [], []
    spot = float(d["close"].iloc[-1])
    stt, _, info = CB.scan(d)
    ema20 = float(d["close"].ewm(span=20, adjust=False).mean().iloc[-1])
    today = t.date()
    lo, hi = spot * (1 - STRIKE_PCT), spot * (1 + STRIKE_PCT)
    day = st_day.setdefault(sym, {})
    if day.get("oi_date") != today.isoformat() or not day.get("oi"):
        try:
            day["oi"] = fetch_oi(tc, sym, lo, hi, today)
            day["oi_date"] = today.isoformat()
        except Exception as e:  # noqa: BLE001
            note_err(f"{sym} open interest", e)
            day["oi"] = {}
    oi = day["oi"]
    try:
        chain = fetch_chain(oc, sym, lo, hi, today)
    except Exception as e:  # noqa: BLE001
        note_err(f"{sym} option chain", e)
        chain = {}
    rows, quotes, vol_today, crow, last_px, filled = parse_chain(chain, oi, today, spot, t)
    lv = gex_levels(rows, spot, t) or dict(net=np.nan, net0=np.nan, share0=np.nan, flip=np.nan, call_wall=np.nan, put_wall=np.nan,
                                         call_wall0=np.nan, put_wall0=np.nan)
    # flow since the last scan (near the money, 0-7 DTE)
    near = [c for c in quotes if abs(occ_parse(c)[3] - spot) / spot <= FLOW_PCT and (occ_parse(c)[1] - today).days <= FLOW_DTE]
    end = datetime.now(timezone.utc) - timedelta(minutes=delay_min)
    start = datetime.fromisoformat(day["last_end"]) if day.get("last_end") else end - timedelta(minutes=SCAN_MIN)
    start = max(start, end - timedelta(minutes=30))
    # REAL-TIME flow: contracts traded since the last scan (today's volume now minus last scan's), x the last price,
    # tagged BUY / SELL by where the last trade sat in the quote. Exact prints (big prints) come from the trades feed.
    tot, prints = dict(cb=0.0, cs=0.0, pb=0.0, ps=0.0), []
    pv = VOL_SEEN.setdefault(sym, {})
    for c in near:
        v = vol_today.get(c, 0.0)
        dv = v - pv[c] if c in pv else 0.0
        pv[c] = v
        px = last_px.get(c) or sum(quotes.get(c, (0.0, 0.0))) / 2
        if dv <= 0 or px <= 0:
            continue
        cp = occ_parse(c)[2]
        sd = side_of(px, *quotes.get(c, (0.0, 0.0)))
        if sd == "BUY":
            tot["cb" if cp == 1 else "pb"] += dv * px * 100
        elif sd == "SELL":
            tot["cs" if cp == 1 else "ps"] += dv * px * 100
    if near and end > start:
        try:
            trades = fetch_trades(oc, near, start, end)
        except Exception as e:  # noqa: BLE001
            m_ = str(e).lower()
            if delay_min == 0 and any(w in m_ for w in ("subscription", "recent", "permit", "403", "forbidden", "opra", "not signed")):
                raise                                     # one_scan switches flow to 16 minutes behind and retries
            note_err(f"{sym} option trades", e)
            trades = {}
        _, prints = flow_of(sym, trades, quotes, oi, vol_today, t)
    day["last_end"] = end.isoformat()
    for k_ in tot:
        day[k_] = day.get(k_, 0.0) + tot[k_]
    bull_d, bear_d = day["cb"] + day["ps"], day["pb"] + day["cs"]
    hist = day.setdefault("big_hist", [])
    hist.append([t.isoformat(), sum(p["premium"] for p in prints if (p["type"] == "CALL") == (p["side"] != "SELL") and p["side"] != "MID"),
                 sum(p["premium"] for p in prints if (p["type"] == "PUT") == (p["side"] != "SELL") and p["side"] != "MID")])
    hist[:] = [h for h in hist if datetime.fromisoformat(h[0]) >= t - timedelta(minutes=15)]
    # unusual volume
    for c, v in vol_today.items():
        o = oi.get(c, 0)
        if v >= UNUSUAL_MIN and v > o and c not in day.setdefault("unusual_seen", []):
            day["unusual_seen"].append(c)
            _, exp, cp, k = occ_parse(c)
            prints.append(dict(t=t.isoformat(timespec="seconds"), trade_time="", sym=sym, kind="UNUSUAL VOLUME", contract=c,
                               type="CALL" if cp == 1 else "PUT", strike=k, exp=exp.isoformat(), dte=(exp - today).days, size=int(v),
                               price=quotes.get(c, (0, 0))[1], premium="", side="", vol_today=int(v), oi=int(o)))
    prev_side = day.get("flip_side")
    side_now = 0 if not np.isfinite(lv["flip"]) else (1 if spot > lv["flip"] else -1)
    day["flip_side"] = side_now
    r = dict(t=t.isoformat(timespec="seconds"), sym=sym, price=round(spot, 2),
             trend=int(stt[-1]), clean=round(float(info["clean"]), 1), adx=round(float(info["adx"]), 1), rvol=round(float(info["rv"]), 2),
             above_ema20=int(spot > ema20),
             net_gex=lv["net"], net_gex_0dte=lv["net0"], share_0dte=lv["share0"], flip=lv["flip"],
             call_wall=lv["call_wall"], put_wall=lv["put_wall"], call_wall_0dte=lv["call_wall0"], put_wall_0dte=lv["put_wall0"],
             flow_bull=round(tot["cb"] + tot["ps"]), flow_bear=round(tot["pb"] + tot["cs"]),
             flow_net_day=round(bull_d - bear_d), flow_strength=round(abs(bull_d - bear_d) / (bull_d + bear_d), 3) if bull_d + bear_d > 0 else 0.0,
             big_bull_15=sum(h[1] for h in hist), big_bear_15=sum(h[2] for h in hist), n_big=sum(1 for p in prints if p["kind"] == "BIG PRINT"),
             flip_cross=(side_now if prev_side not in (None, 0) and side_now != 0 and side_now != prev_side else 0),
             flow_delay_min=delay_min, feed=FEED)
    r["setup"], r["bias"], r["score"] = setup_of(r)
    # the best contract for the move ($0.40-$0.80, most % gain if price reaches the target)
    hl, lc_ = d["high"] - d["low"], d["close"].shift(1)
    atr5 = float(pd.concat([hl, (d["high"] - lc_).abs(), (d["low"] - lc_).abs()], axis=1).max(axis=1).ewm(alpha=1 / 14, adjust=False).mean().iloc[-1])
    r["atr5"] = round(atr5, 3)
    pk, tg, tk = None, np.nan, ""
    PICK_WHY[0] = ""
    if r["bias"] != 0:
        tg, tk = target_of(r, r["bias"], atr5)
        pk = pick_contract(crow, spot, r["bias"], tg)
        if filled:
            PICK_WHY[0] += f" ({filled} contracts' greeks worked out here)"
    r["pick_why"] = PICK_WHY[0]
    r.update(target=round(tg, 2) if np.isfinite(tg) else np.nan, target_kind=tk, pick=pk["contract"] if pk else "",
             pick_bid=pk["bid"] if pk else np.nan, pick_ask=pk["ask"] if pk else np.nan, pick_delta=round(pk["delta"], 2) if pk else np.nan,
             pick_est=round(pk["est"], 2) if pk else np.nan, pick_juice=round(pk["juice"] * 100, 1) if pk else np.nan)
    return r, prints, crow


# ===== outputs =====
def append_csv(path, rows):
    if not rows:
        return
    cols = list(rows[0].keys())
    if os.path.exists(path):
        with open(path, newline="") as f:
            old_cols = next(csv.reader(f), [])
        if old_cols != cols:                      # columns changed (new version): rewrite the file with every column
            with open(path, newline="") as f:
                old = list(csv.DictReader(f))
            cols = old_cols + [k for k in cols if k not in old_cols]
            with open(path, "w", newline="") as f:
                w = csv.DictWriter(f, fieldnames=cols, restval="", extrasaction="ignore")
                w.writeheader()
                for r in old:
                    w.writerow({k: v for k, v in r.items() if k in cols})
    new = not os.path.exists(path)
    with open(path, "a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols, restval="", extrasaction="ignore")
        if new:
            w.writeheader()
        for r in rows:
            w.writerow({k: (round(v, 4) if isinstance(v, float) else v) for k, v in r.items()})


def money(x):
    if x is None or not np.isfinite(x):
        return "-"
    a = abs(x)
    s = f"{a / 1e9:.1f}B" if a >= 1e9 else f"{a / 1e6:.1f}M" if a >= 1e6 else f"{a / 1e3:.0f}k" if a >= 1e3 else f"{a:.0f}"
    return ("-" if x < 0 else "+") + "$" + s


def lvl(x):
    return "-" if x is None or not np.isfinite(x) else f"{x:,.2f}".rstrip("0").rstrip(".")


def pick_txt(contract, ask, delta, juice, target):
    if not contract:
        return "-"
    _, exp, cp, k = occ_parse(contract)
    return (f"{exp:%m/%d} {lvl(k)}{'C' if cp == 1 else 'P'} @ {ask:.2f} (delta {abs(delta):.2f}) "
            f"= est {juice:+.0f}% at {lvl(target)}")


def write_board(rows, prints, t, delay, state=None):
    rows = sorted(rows, key=lambda r: -r["score"])
    L = [f"# GEX + FLOW SCAN - {t:%a %b %d, %I:%M %p} ET",
         f"Log only, no orders. Options feed: {FEED}. Flow = real time (volume change x price)." + (f" Big prints run {delay} min behind (free plan limit on option trades)." if delay else "")
         + f" FIRE = score {FIRE_MIN}+ with a bias: the bot picks the {PICK_MIN:.2f}-{PICK_MAX:.2f} contract with the most juice "
         "for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.", ""]
    fires = (state or {}).get("fires", [])
    if fires:
        L += [f"## FIRES today ({len(fires)})", "| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |",
              "|---|---|---|---|---|---|---|---|---|---|---|"]
        for f in reversed(fires[-20:]):
            a = f["entry_ask"]
            now_p = (f["last_bid"] / a - 1) * 100 if a else 0
            best_p = (f["max_bid"] / a - 1) * 100 if a else 0
            _, exp, cp, k = occ_parse(f["contract"])
            L.append(f"| {f['t_entry'][11:16]} | **{f['sym']}** | **{f['side']}** | {f['setup']} | {exp:%m/%d} {lvl(k)}{'C' if cp == 1 else 'P'} | "
                     f"{a:.2f} | {f['last_bid']:.2f} | {best_p:+.0f}% ({f['max_min']}m) | **{now_p:+.0f}%**{' (done)' if f['closed'] else ''} | "
                     f"{f['est_juice_pct']:+.0f}% | {lvl(f['target'])}{' hit' if f['target_hit_min'] is not None else ''} |")
        L.append("")
    rlog = (state or {}).get("rule_log", [])
    if RULE_ON:
        L += [f"## 1m RULES on SPY / QQQ - loose ({len(rlog)} signals today, last 10)",
              "Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). "
              "Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv."]
        hb = (state or {}).get("rule_hb", {})
        if hb:
            L.append(f"Last 1m check {hb.get('t', '')[11:19]} ET, last candle " + ", ".join(f"{k} {v}" for k, v in hb.get("last", {}).items())
                     + (f" | **ERROR: {hb['err']}**" if hb.get("err") else " | no errors"))
        if rlog:
            L += ["| Candle | Ticker | Rule | Tags | Side | TTM | Result |", "|---|---|---|---|---|---|---|"]
            for g in reversed(rlog[-10:]):
                res = f"**FIRE** {g['contract']}" if g["fired"] == "FIRE" else ("logged (agree flip)" if g["fired"] == "LOG" else g["why"][:90])
                L.append(f"| {g['candle']} | {g['sym']} | {g['rule']} | {g['tags']} | {g['side']} | {g['ttm']} | {res} |")
        L.append("")
    bl = (state or {}).get("blocked", [])
    if bl:
        L += [f"## Flow surges NOT fired - price disagreed ({len(bl)} today, last 5)"] + [f"- {b['t'][11:16]} {b['sym']} {b['side']}: {b['why']}" for b in reversed(bl[-5:])] + [""]
    L += ["| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |",
          "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for i, r in enumerate(rows, 1):
        gam = ("NEG" if r["net_gex"] < 0 else "POS") + " " + money(r["net_gex"]) if np.isfinite(r["net_gex"]) else "-"
        bias = "CALLS" if r["bias"] == 1 else "PUTS" if r["bias"] == -1 else "-"
        tr = ("LONG" if r["trend"] == 1 else "SHORT" if r["trend"] == -1 else "out") + f" (clean {r['clean']:.0f}, ADX {r['adx']:.0f}, RVol {r['rvol']:.1f})"
        big = f"{money(r['big_bull_15'])} bull / {money(-r['big_bear_15'])} bear" if r["big_bull_15"] or r["big_bear_15"] else "-"
        pk = pick_txt(r["pick"], r["pick_ask"], r["pick_delta"], r["pick_juice"], r["target"]) if r["pick"] else (f"none: {r['pick_why']}" if r["bias"] else "-")
        L.append(f"| {i} | **{r['sym']}** | {r['price']:,.2f} | {r['setup']} | **{bias}** | {r['score']} | {pk} | {gam} | {lvl(r['flip'])} | "
                 f"{lvl(r['call_wall'])} | {lvl(r['put_wall'])} | {money(r['flow_net_day'])} | {big} | {tr} |")
    bp = [p for p in prints if p["kind"] == "BIG PRINT"]
    uv = [p for p in prints if p["kind"] == "UNUSUAL VOLUME"]
    L += ["", f"## Big prints this scan ({len(bp)})"]
    for p in sorted(bp, key=lambda p: -float(p["premium"]))[:15]:
        L.append(f"- **{p['sym']}** {p['type']} {lvl(p['strike'])} {p['exp']} ({p['dte']}DTE): {p['size']:,} @ {p['price']:.2f} = "
                 f"**{money(p['premium'])}** {p['side']} | vol {p['vol_today']:,} / OI {p['oi']:,}")
    if uv:
        L += ["", f"## New unusual volume (traded more than open interest, {UNUSUAL_MIN}+)"]
        for p in uv[:15]:
            L.append(f"- **{p['sym']}** {p['type']} {lvl(p['strike'])} {p['exp']} ({p['dte']}DTE): {p['vol_today']:,} traded vs OI {p['oi']:,}")
    if ERRS:
        L += ["", f"## Data problems this scan ({len(ERRS)})"] + [f"- {k}: `{v}`" for k, v in list(ERRS.items())[:20]]
    if not rows:
        L += ["", "No ticker could be scanned - see Data problems."]
    L += ["", "**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). "
          "Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma "
          "(magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), "
          "near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote."]
    with open(BOARD, "w") as f:
        f.write("\n".join(L) + "\n")
    return "\n".join(L)


def push(msg):
    try:
        files = [f for f in (BOARD, LOG, PRINTS, STATE, FIRES, RULES) if os.path.exists(f)]
        subprocess.run(["git", "add"] + files, check=False, capture_output=True)
        if subprocess.run(["git", "diff", "--cached", "--quiet"]).returncode == 0:
            return
        subprocess.run(["git", "commit", "-q", "-m", msg], check=False, capture_output=True)
        subprocess.run(["git", "pull", "-q", "--rebase", "origin", "main"], check=False, capture_output=True)
        subprocess.run(["git", "push", "-q"], check=False, capture_output=True)
    except Exception as e:  # noqa: BLE001
        log(f"push failed: {e}")


def load_state(today):
    try:
        s = json.load(open(STATE))
        if s.get("day") == today.isoformat():
            return s
    except Exception:  # noqa: BLE001
        pass
    return {"day": today.isoformat(), "tickers": {}}


def save_state(s):
    slim = {"day": s["day"], "flow_delay": s.get("flow_delay", 0), "fires": s.get("fires", []), "last_fire": s.get("last_fire", {}), "blocked": s.get("blocked", []), "rule_hb": s.get("rule_hb", {}),
            "rule_seen": s.get("rule_seen", {}), "rule_log": s.get("rule_log", [])[-30:],
            "tickers": {}}
    for k, v in s["tickers"].items():
        slim["tickers"][k] = {x: y for x, y in v.items() if x != "oi"}
    with open(STATE, "w") as f:
        json.dump(slim, f)


# ===== FIRES: the picked contract, followed for 60 minutes on its real quotes =====
def fire_check(rows, bars, state, t):
    fires = state.setdefault("fires", [])
    last = state.setdefault("last_fire", {})
    # did price reach the target? (5-minute highs / lows since the fire)
    for f in fires:
        if f["closed"] or f["target_hit_min"] is not None:
            continue
        d = bars.get(f["sym"])
        if d is None:
            continue
        d = d[d.index >= pd.Timestamp(f["t_entry"])]
        if len(d) and ((f["bias"] == 1 and d["high"].max() >= f["target"]) or (f["bias"] == -1 and d["low"].min() <= f["target"])):
            f["target_hit_min"] = round((t - datetime.fromisoformat(f["t_entry"])).total_seconds() / 60)
            f["pct_at_target"] = round((f["last_bid"] / f["entry_ask"] - 1) * 100, 1) if f["entry_ask"] else None
    for r in rows:
        if r["bias"] == 0 or r["score"] < FIRE_MIN or not r["pick"] or r["setup"].startswith("TREND (flow not") or hhmm(t) > 1530:
            continue
        key = f"{r['sym']}|{r['bias']}"
        if key in last and (t - datetime.fromisoformat(last[key])).total_seconds() < FIRE_COOL * 60:
            continue
        if r["setup"].startswith("FLOW SURGE"):
            d = bars.get(r["sym"])
            mv = float(d["close"].iloc[-1] - d["close"].iloc[-1 - SURGE_CONFIRM]) if d is not None and len(d) > SURGE_CONFIRM else 0.0
            side_ok = (r["above_ema20"] == 1) if r["bias"] == 1 else (r["above_ema20"] == 0)
            if mv * r["bias"] <= 0 or not side_ok:
                bl = state.setdefault("blocked", [])
                key2 = f"{r['sym']}|{r['bias']}|{t:%H%M}"
                if not any(b["key"] == key2 for b in bl):
                    bl.append(dict(key=key2, t=t.isoformat(timespec="seconds"), sym=r["sym"], side="CALLS" if r["bias"] == 1 else "PUTS",
                                   setup=r["setup"], why=(f"price {mv:+.2f} over the last {SURGE_CONFIRM * 5} min" if mv * r["bias"] <= 0 else "")
                                   + ("" if side_ok else (" / " if mv * r["bias"] <= 0 else "") + ("under" if r["bias"] == 1 else "over") + " EMA 20")
                                   + " - flow says one way, price says the other"))
                    del bl[:-40]
                continue
        last[key] = t.isoformat()
        f = dict(id=f"{r['sym']}-{t:%H%M}", t_entry=t.isoformat(timespec="seconds"), sym=r["sym"], bias=r["bias"],
                 side="CALLS" if r["bias"] == 1 else "PUTS", setup=r["setup"], score=r["score"], contract=r["pick"],
                 entry_bid=r["pick_bid"], entry_ask=r["pick_ask"], delta=r["pick_delta"], spot=r["price"], target=r["target"],
                 target_kind=r["target_kind"], est_juice_pct=r["pick_juice"], last_bid=r["pick_bid"], max_bid=r["pick_bid"],
                 max_min=0, min_bid=r["pick_bid"], bid_15=None, bid_20=None, bid_30=None, bid_60=None, hit25_min=None, hit50_min=None,
                 hit100_min=None, down30_min=None, target_hit_min=None, closed=False)
        fires.append(f)
        log(f"FIRE {f['side']} {r['sym']} {r['setup']} | {f['contract']} ask {f['entry_ask']:.2f} | target {f['target']} "
            f"({f['target_kind']}) | est +{f['est_juice_pct']:.0f}%")


def track_fires(oc, state, t):
    open_ = [f for f in state.get("fires", []) if not f["closed"]]
    if not open_:
        return
    try:
        q = fetch_quotes(oc, sorted({f["contract"] for f in open_}))
    except Exception as e:  # noqa: BLE001
        log(f"fire quotes failed: {str(e)[:150]}")
        return
    done = []
    for f in open_:
        bid = q.get(f["contract"], (0.0, 0.0))[0]
        el = (t - datetime.fromisoformat(f["t_entry"])).total_seconds() / 60
        if bid > 0:
            f["last_bid"] = bid
            if bid > f["max_bid"]:
                f["max_bid"], f["max_min"] = bid, round(el)
            f["min_bid"] = min(f["min_bid"], bid)
            pct = bid / f["entry_ask"] - 1
            for k, lvl_ in (("hit25_min", 0.25), ("hit50_min", 0.5), ("hit100_min", 1.0)):
                if f[k] is None and pct >= lvl_:
                    f[k] = round(el)
            if f.get("pct_at_tp") is None and pct >= TP_PCT:
                f["pct_at_tp"], f["tp_min"] = round(pct * 100, 1), round(el)
            sx = f.setdefault("sx", {})
            best_ = f["max_bid"] / f["entry_ask"] - 1
            if "lock" not in sx and best_ >= LOCK_ARM and pct <= LOCK_FLOOR:
                sx["lock"] = [round(pct * 100, 1), round(el)]
            if "trail" not in sx and best_ >= TRAIL_ARM and (bid <= f["max_bid"] * (1 - TRAIL_GIVE) or pct <= 0):
                sx["trail"] = [round(pct * 100, 1), round(el)]
            if "tpbe" not in sx and (pct >= TP_PCT or (best_ >= LOCK_ARM and pct <= 0)):
                sx["tpbe"] = [round(pct * 100, 1), round(el)]
            if f["down30_min"] is None and pct <= -0.30:
                f["down30_min"] = round(el)
        for k, m_ in (("bid_15", 15), ("bid_20", 20), ("bid_30", 30), ("bid_60", 60)):
            if f.get(k) is None and el >= m_:
                f[k] = f["last_bid"]
        if el >= TRACK_MIN or hhmm(t) >= 1555:
            for k in ("bid_15", "bid_20", "bid_30", "bid_60"):
                if f.get(k) is None:
                    f[k] = f["last_bid"]
            f["closed"] = True
            done.append(f)
    rows = []
    for f in done:
        a = f["entry_ask"]
        pc = lambda x: round((x / a - 1) * 100, 1) if x is not None and a else None
        rows.append(dict(t_entry=f["t_entry"], sym=f["sym"], side=f["side"], setup=f["setup"], score=f["score"], contract=f["contract"],
                         entry_ask=a, delta=f["delta"], spot=f["spot"], target=f["target"], target_kind=f["target_kind"],
                         est_pct=f["est_juice_pct"], pct_15=pc(f["bid_15"]), pct_20=pc(f.get("bid_20")), pct_30=pc(f["bid_30"]), pct_60=pc(f["bid_60"]),
                         best_pct=pc(f["max_bid"]), best_at_min=f["max_min"], worst_pct=pc(f["min_bid"]), hit25_min=f["hit25_min"],
                         hit50_min=f["hit50_min"], hit100_min=f["hit100_min"], down30_min=f["down30_min"], target_hit_min=f["target_hit_min"],
                         tp40_pct=f["pct_at_tp"] if f.get("pct_at_tp") is not None else pc(f["bid_60"]), tp40_min=f.get("tp_min"),
                         sell_at_target_pct=f["pct_at_target"] if f.get("pct_at_target") is not None else pc(f["bid_60"]),
                         lock_pct=f.get("sx", {}).get("lock", [pc(f["bid_60"])])[0], trail_pct=f.get("sx", {}).get("trail", [pc(f["bid_60"])])[0],
                         tpbe_pct=f.get("sx", {}).get("tpbe", [pc(f["bid_60"])])[0]))
        log(f"FIRE DONE {f['id']} {f['contract']}: 15m {pc(f['bid_15'])}% | 30m {pc(f['bid_30'])}% | best {pc(f['max_bid'])}% at {f['max_min']}m")
    append_csv(FIRES, rows)


# ===== 1m RULES on SPY + QQQ (the Trend Flip backtest's whipsaw / failed pop, fired loose) =====
_BT = [None]
TTM_REL = {("cyan", 1): "WITH you", ("yellow", 1): "TURNING your way", ("dark blue", 1): "TURNING away",
           ("red", 1): "AGAINST you", ("red", -1): "WITH you", ("dark blue", -1): "TURNING your way",
           ("yellow", -1): "TURNING away", ("cyan", -1): "AGAINST you"}


def bt():
    """backtest.py, imported once (only its functions are used - same math as the test)"""
    if _BT[0] is None:
        import backtest as B
        _BT[0] = B
    return _BT[0]


def fetch_1m(dc, syms):
    """closed 1-minute candles (all sessions, like the backtest), last 5 days, IEX feed"""
    from alpaca.data.enums import DataFeed
    from alpaca.data.requests import StockBarsRequest
    from alpaca.data.timeframe import TimeFrame
    now = datetime.now(timezone.utc)
    df = dc.get_stock_bars(StockBarsRequest(symbol_or_symbols=syms, timeframe=TimeFrame.Minute,
                                            start=now - timedelta(days=5), end=now, feed=DataFeed.IEX)).df
    out = {}
    if df is None or df.empty:
        return out
    cut = pd.Timestamp(now).tz_convert(ET)
    for s in syms:
        try:
            d = df.xs(s, level=0) if isinstance(df.index, pd.MultiIndex) else df
        except KeyError:
            continue
        d = d.sort_index()
        d.index = d.index.tz_convert(ET)
        out[s] = d[d.index + pd.Timedelta(minutes=1) <= cut][["open", "high", "low", "close", "volume"]].astype(float)
    return out


def rule_events(d):
    """every whipsaw / failed pop in d (1m candles), with the tags of the tighter rules each one also meets.
    A copy of the last candle is added as a stand-in 'next candle' so the backtest's event code can see the last one."""
    B = bt()
    n = len(d)
    if n < 120:
        return []
    pad = d.iloc[[-1]].copy()
    pad.index = pad.index + pd.Timedelta(minutes=1)
    df = pd.concat([d, pad])
    ind = B.indicators(df, 13, 34, True)
    ev, F, G, _, _, _ = B.vs_events(df, ind)
    mom = np.asarray(B.cl_ttm(df)[0], dtype=float)
    c, a, vw = ind["c"], ind["atr"], ind["vwap"]
    out = []
    for setup, i, side in ev:
        if setup not in ("VF_WHIP", "TL_FAILPOP") or i >= n or not (a[i] > 0):
            continue
        if np.isfinite(mom[i]) and i > 0:
            raw = ("cyan" if mom[i] > mom[i - 1] else "dark blue") if mom[i] >= 0 else ("yellow" if mom[i] > mom[i - 1] else "red")
            rel = TTM_REL[(raw, side)]
        else:
            raw, rel = "n/a", "n/a"
        vwx = side * (c[i] - vw[i]) / a[i] if np.isfinite(vw[i]) else np.nan
        if setup == "VF_WHIP":
            name, tags = "1m WHIPSAW", ["R1"]
            ttm_ok = rel in ("WITH you", "TURNING your way")
            near = np.isfinite(vwx) and abs(vwx) < 1
            if ttm_ok:
                tags.append("R2")
            if near:
                tags.append("R5")
            if ttm_ok and near:
                tags.append("R6")
        else:
            name, tags = "1m FAILED POP", ["R3"]
            if rel != "TURNING away":
                tags.append("R4")
        out.append(dict(t=d.index[i], setup=setup, name=name, tags=tags, d=side, ttm=raw, rel=rel, vwx=vwx,
                        atr=float(a[i]), close=float(c[i]), fear=float(np.nan_to_num(F[i])), greed=float(np.nan_to_num(G[i]))))
    return out


def rule_pick(tc, oc, state, sym, e, t):
    """the best 0-1 DTE $0.40-$0.80 contract for a 1m rule signal, from a fresh chain"""
    today = t.date()
    spot = e["close"]
    day = state["tickers"].setdefault(sym, {})
    if day.get("oi_date") != today.isoformat() or not day.get("oi"):
        try:
            day["oi"] = fetch_oi(tc, sym, spot * (1 - STRIKE_PCT), spot * (1 + STRIKE_PCT), today)
            day["oi_date"] = today.isoformat()
        except Exception as ex:  # noqa: BLE001
            note_err(f"{sym} open interest", ex)
            day["oi"] = {}
    chain = fetch_chain(oc, sym, spot * 0.97, spot * 1.03, today)
    _, _, _, crow, _, filled = parse_chain(chain, day.get("oi", {}), today, spot, t)
    target = spot + e["d"] * RULE_TGT * e["atr"]
    PICK_WHY[0] = ""
    pk = pick_contract(crow, spot, e["d"], target, dte=RULE_DTE, dmin=RULE_DELTA, hold=RULE_HOLD, minj=RULE_MIN_JUICE)
    why = PICK_WHY[0] + (f" ({filled} greeks worked out here)" if filled else "")
    return pk, target, why


def agree_log(d, sym, seen, rlog, t):
    """your AGREE FLIP on the 1m chart (fear peak 95+ -> within 20 candles TTM turns up + Vix Fix / TTM agree up + squeeze fired
    in the last 5 + line green; mirror for puts) - same code as futures_flush.py. LOG ONLY: written to gex_rules.csv, never fired."""
    import futures_flush as FF
    pad = d.iloc[[-1]].copy()
    pad.index = pad.index + pd.Timedelta(minutes=1)
    df = pd.concat([d, pad])
    S = FF.build(df)
    pk, w, cu, cd = FF.variants(S)["FULL p95 w20"]
    out, key = [], sym + "|agree"
    prev = seen.get(key, "")
    for side, cond in ((1, cu), (-1, cd)):
        for i in FF.detect(S, pk, w, cond, side, 935, 1530):
            if i >= len(d):
                continue
            ts = d.index[i]
            if ts.date() != t.date() or ts.isoformat() <= prev:
                continue
            seen[key] = max(seen.get(key, ""), ts.isoformat())
            row = dict(t=t.isoformat(timespec="seconds"), candle=ts.strftime("%H:%M"), sym=sym, rule="1m AGREE FLIP", tags="FULL",
                       side="CALLS" if side == 1 else "PUTS", close=round(float(d["close"].iloc[i]), 2), atr1=round(float(S["atr"][i]), 3),
                       ttm="up" if side == 1 else "down", vwap_atr="", fear=round(float(S["F"][i])), greed=round(float(S["G"][i])),
                       seen_after_min=round((t - (ts + pd.Timedelta(minutes=1))).total_seconds() / 60, 1), fired="LOG", contract="",
                       ask="", delta="", target="", why="log only - your agree flip, graded later, never traded")
            out.append(row)
            rlog.append({k: row[k] for k in ("candle", "sym", "rule", "tags", "side", "ttm", "fired", "contract", "why")})
    return out


def rule_check(tc, dc, oc, state, t):
    """runs every minute: new 1m rule signals on SPY / QQQ -> FIRE (loose). Returns how many fired."""
    if not RULE_ON or hhmm(t) < 936 or hhmm(t) > 1532:
        return 0
    hb = state.setdefault("rule_hb", {})
    hb.update(t=t.isoformat(timespec="seconds"), err="")
    try:
        bars1 = fetch_1m(dc, RULE_SYMS)
    except Exception as ex:  # noqa: BLE001
        note_err("1m candles", ex)
        hb["err"] = f"1m candles: {str(ex)[:120]}"
        return 0
    hb["last"] = {s_: f"{bars1[s_].index[-1]:%H:%M}" for s_ in RULE_SYMS if s_ in bars1 and len(bars1[s_])}
    seen = state.setdefault("rule_seen", {})
    last = state.setdefault("last_fire", {})
    fires = state.setdefault("fires", [])
    rlog = state.setdefault("rule_log", [])
    rows, new = [], 0
    for sym in RULE_SYMS:
        d = bars1.get(sym)
        if d is None or len(d) < 120:
            continue
        try:
            evs = rule_events(d)
        except Exception as ex:  # noqa: BLE001
            note_err(f"{sym} 1m rules", ex)
            hb["err"] = f"{sym} 1m rules: {str(ex)[:120]}"
            continue
        if AGREE_LOG:
            try:
                rows += agree_log(d, sym, seen, rlog, t)
            except Exception as ex:  # noqa: BLE001
                hb["err"] = f"{sym} agree flip: {str(ex)[:120]}"
        prev = seen.get(sym, "")
        for e in evs:
            ts = e["t"].isoformat()
            if e["t"].date() != t.date() or ts <= prev:
                continue
            seen[sym] = max(seen.get(sym, ""), ts)
            age = (t - (e["t"] + pd.Timedelta(minutes=1))).total_seconds() / 60
            side = "CALLS" if e["d"] == 1 else "PUTS"
            row = dict(t=t.isoformat(timespec="seconds"), candle=e["t"].strftime("%H:%M"), sym=sym, rule=e["name"],
                       tags=" ".join(e["tags"]), side=side, close=round(e["close"], 2), atr1=round(e["atr"], 3), ttm=e["rel"],
                       vwap_atr=round(e["vwx"], 2) if np.isfinite(e["vwx"]) else "", fear=round(e["fear"]), greed=round(e["greed"]),
                       seen_after_min=round(age, 1), fired="", contract="", ask="", delta="", target="", why="")
            key = f"{sym}|{e['d']}|1m"
            if age > RULE_LATE:
                row["why"] = "seen late (not fired)"
            elif key in last and (t - datetime.fromisoformat(last[key])).total_seconds() < RULE_COOL * 60:
                row["why"] = f"{RULE_COOL}-minute cooldown"
            else:
                try:
                    pk, tg, why = rule_pick(tc, oc, state, sym, e, t)
                except Exception as ex:  # noqa: BLE001
                    note_err(f"{sym} 1m rule contract", ex)
                    pk, tg, why = None, np.nan, f"chain failed: {str(ex)[:80]}"
                row["target"] = round(tg, 2) if np.isfinite(tg) else ""
                if not pk:
                    row["why"] = "no contract: " + why
                else:
                    last[key] = t.isoformat()
                    setup = f"{e['name']} ({' '.join(e['tags'])})"
                    f = dict(id=f"{sym}-1m-{t:%H%M}", t_entry=t.isoformat(timespec="seconds"), sym=sym, bias=e["d"], side=side,
                             setup=setup, score=None, contract=pk["contract"], entry_bid=pk["bid"], entry_ask=pk["ask"],
                             delta=round(pk["delta"], 2), spot=round(e["close"], 2), target=round(tg, 2), target_kind=f"{RULE_TGT:g} x 1m ATR",
                             est_juice_pct=round(pk["juice"] * 100, 1), last_bid=pk["bid"], max_bid=pk["bid"], max_min=0,
                             min_bid=pk["bid"], bid_15=None, bid_20=None, bid_30=None, bid_60=None, hit25_min=None, hit50_min=None,
                             hit100_min=None, down30_min=None, target_hit_min=None, closed=False)
                    fires.append(f)
                    new += 1
                    row.update(fired="FIRE", contract=pk["contract"], ask=pk["ask"], delta=round(pk["delta"], 2), why=why)
                    log(f"FIRE 1m {side} {sym} {setup} | {f['contract']} ask {f['entry_ask']:.2f} | target {f['target']} "
                        f"| est +{f['est_juice_pct']:.0f}%")
            rows.append(row)
            rlog.append({k: row[k] for k in ("candle", "sym", "rule", "tags", "side", "ttm", "fired", "contract", "why")})
    del rlog[:-30]
    append_csv(RULES, rows)
    return new


# ===== loop =====
def one_scan(tc, dc, oc, state, t):
    ERRS.clear()
    try:
        bars = fetch_bars(dc)
    except Exception as e:  # noqa: BLE001
        note_err("stock candles", e)
        bars = {}
    rows, prints = [], []
    for sym in SYMBOLS:
        delay = state.get("flow_delay", 0)
        try:
            r, p, _ = scan_ticker(sym, tc, oc, bars, state["tickers"], t, delay)
        except Exception as e:  # noqa: BLE001
            msg = str(e).lower()
            if delay == 0 and any(w in msg for w in ("subscription", "recent", "permit", "403", "forbidden", "opra", "not signed")):
                log(f"{sym}: recent option trades not allowed on this plan - flow switches to 16 minutes behind")
                state["flow_delay"] = 16
                try:
                    r, p, _ = scan_ticker(sym, tc, oc, bars, state["tickers"], t, 16)
                except Exception as e2:  # noqa: BLE001
                    note_err(f"{sym} scan", e2)
                    continue
            else:
                note_err(f"{sym} scan", e)
                continue
        if r:
            rows.append(r)
            prints += p
    append_csv(LOG, rows)
    append_csv(PRINTS, prints)
    fire_check(rows, bars, state, t)
    save_state(state)
    text = write_board(rows, prints, t, state.get("flow_delay", 0), state)
    top = sorted(rows, key=lambda r: -r["score"])[:3]
    log(f"scan done: {len(rows)} tickers, {len(prints)} prints | top: " + ", ".join(f"{r['sym']} {r['score']} {r['setup']}" for r in top))
    return text


def run_loop(tc, dc, oc):
    t0 = time.time()
    today = now_et().date()
    state = load_state(today)
    log(f"GEX + FLOW SCAN | {len(SYMBOLS)} tickers | feed {FEED} | log only")
    n, text = 0, ""
    while time.time() - t0 < RUN_MINUTES * 60:
        t = now_et()
        if hhmm(t) >= 1600 or t.weekday() >= 5:
            break
        if hhmm(t) < SCAN_FROM:
            sleep(min(60, (datetime(t.year, t.month, t.day, 9, 35, 5, tzinfo=ET) - t).total_seconds()))
            continue
        if hhmm(t) <= SCAN_TO:
            nf = len(state.get("fires", []))
            text = one_scan(tc, dc, oc, state, t) or text
            n += 1
            if n % PUSH_EVERY == 0 or len(state.get("fires", [])) > nf:      # a new FIRE goes out right away
                push(f"gex scan {t:%Y-%m-%d %H:%M}")
        t = now_et()
        nxt = t.replace(second=20, microsecond=0) + timedelta(minutes=SCAN_MIN - t.minute % SCAN_MIN)
        nrule = t                                   # the 1m rules run right after a scan, then 8 seconds into every minute
        while now_et() < nxt:
            if now_et() >= nrule:
                try:
                    if rule_check(tc, dc, oc, state, now_et()):
                        save_state(state)
                        push(f"gex 1m rule fire {now_et():%Y-%m-%d %H:%M}")
                except Exception as ex:  # noqa: BLE001
                    log(f"1m rules failed: {str(ex)[:200]}")
                tn = now_et()
                nrule = tn.replace(second=8, microsecond=0) + timedelta(minutes=1)
            track_fires(oc, state, now_et())
            sleep(min(TRACK_SECS, max(0.0, (min(nxt, nrule) - now_et()).total_seconds())))
        save_state(state)
    push(f"gex scan {now_et():%Y-%m-%d %H:%M}")
    s = os.getenv("GITHUB_STEP_SUMMARY")
    if s and text:
        with open(s, "a") as f:
            f.write(text + "\n")


def main():
    if not KEY or not SECRET:
        sys.exit("ALPACA_KEY / ALPACA_SECRET are missing. Add them in Settings > Secrets and variables > Actions.")
    from alpaca.data.historical import OptionHistoricalDataClient, StockHistoricalDataClient
    from alpaca.trading.client import TradingClient
    tc = TradingClient(KEY, SECRET, paper=True)          # read-only use: option contracts + open interest
    dc = StockHistoricalDataClient(KEY, SECRET)
    oc = OptionHistoricalDataClient(KEY, SECRET, raw_data=True)
    try:
        clk = tc.get_clock()
        if not clk.is_open and pd.Timestamp(clk.next_open).tz_convert(ET).date() != now_et().date():
            log("market closed today - nothing to scan")
            return
    except Exception as e:  # noqa: BLE001
        log(f"clock check failed ({e}) - scanning anyway")
    if os.getenv("MODE", "run") == "check":
        t = now_et()
        state = load_state(t.date())
        print(one_scan(tc, dc, oc, state, t))
        return
    run_loop(tc, dc, oc)


if __name__ == "__main__":
    main()
