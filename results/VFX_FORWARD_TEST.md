# VFX forward test — Vix Fix "FEAR / GREED MAXED" (pre-registered 2026-10-24)

Bot: `vfxbot.py` · Workflow: `.github/workflows/vfxbot.yml` · Log: `results/vfx_forward_log.csv` · Report: `python vfx_report.py`
**PAPER ONLY** (`paper=True` hard-coded). Rules are frozen: do not change them during the test.

## Rules
- **SPY + QQQ, 3-minute bars**, extended hours included (Alpaca IEX 1m bars → 3m). Indicator math is imported from `backtest.py`
  (`vfx_pane`, `indicators`, `tlt_colors`, `ang_series`, `agr_series`, `to_tf`), so it matches edge_main.
- **Signal** on a CLOSED 3m bar: Fear F = wvf / highest(wvf, 50) × 100 (lookback 22) crosses up through 95 → LONG calls;
  Greed G crosses up through 95 → SHORT puts. Signal bar close between **9:35 and 14:45 ET**.
- **Skip** if any is true (edge_main bins): 1) trend line AGAINST you strong; 2) price 3+ ATR wrong side of VWAP;
  3) against the day's move (close − 9:30 open); 4) trend-line angle −15° or less against you; 5) TTM against you, turning your way;
  6) your side's Vix Fix (edge_main definition: greed for longs, fear for shorts) rose 15–30 in the last 2 candles.
- **Contract** 1 × 2-ITM 0DTE (strike = round(spot) − 2 for calls, + 2 for puts). Marketable limit **at the ask**.
- **Exit** LINE COLOR (line turns the other color on a closed 3m bar) or hard flat **15:55**. Marketable limit **at the bid**.
- One open trade per symbol; fires while open are logged as `IGNORED`. No averaging, stops or targets.
- **P&L** booked from the logged quotes (ask in, bid out) with **$0.65/contract/side**, not from the paper fill.
- **Control arm (logged, never traded):** for every REAL trade, one random 3m bar in the same 30-minute bucket, same symbol and
  direction, on the next trading day the bot runs; priced and exited the same way. Linked by `fire_id`.

## Log rows (`arm`)
`REAL` trade · `CONTROL` matched random · `SKIPPED` fire blocked by the filter (flags shown) · `IGNORED` fire while a position was open ·
`NOFILL` no contract / no fill. Columns include bid/ask/mid/fill in and out, `gross_pct` (mid→mid), `net_pct` (ask→bid + commission),
`slip_in_pct` / `slip_out_pct` (quote vs mid).

## Checkpoints — look ONLY at 150, 300, 500 REAL trades (~4, 8, 13 months)
- **Success:** net mean > 0 **and** beats control (paired REAL − CONTROL > 0) with day-clustered t ≥ 2.8 @150, ≥ 2.5 @300, ≥ 2.2 @500.
- **Stop (futility):** net mean ≤ 0 at 150; t ≤ −2 at any point after 50 trades; net mean < +1% at 300.
- **Stop (costs):** median fill more than 1% worse than mid per side.
- Expect the true edge to be +0–4%/trade, unproven; t > 2 within a year needs ≥ ~+4% net.

`vfx_report.py` prints mean, median, sd, day-clustered t, day-bootstrap 95% CI for REAL and CONTROL, the paired difference,
the slippage check and a verdict against these rules.
