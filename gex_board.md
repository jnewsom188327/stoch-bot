# GEX + FLOW SCAN - Tue Nov 03, 10:20 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:20:08 ET, last candle SPY 10:19, QQQ 10:19 | no errors

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **DELL** | 408.95 | RUN: clean trend + negative gamma + flow agrees | **CALLS** | 70 | none: 32 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$25.9M | - | 440 | 400 | +$2.1M | +$29k bull / +$0 bear | LONG (clean 35, ADX 38, RVol 0.9) |
| 2 | **ORCL** | 125.03 | FLOW SURGE | **PUTS** | 55 | none: 25 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$40.4M | - | 135 | 125 | -$4.5M | +$86k bull / -$513k bear | out (clean 33, ADX 43, RVol 2.4) |
| 3 | **MSTR** | 134.84 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 53 | none: 27 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$77.2M | - | 135 | 125 | -$2.6M | +$0 bull / -$244k bear | out (clean 27, ADX 34, RVol 1.0) |
| 4 | **COIN** | 144.70 | FLOW SURGE | **PUTS** | 50 | none: 23 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$20.3M | - | 148 | 140 | -$1.2M | +$0 bull / -$124k bear | out (clean 27, ADX 49, RVol 1.1) |
| 5 | **BABA** | 100.89 | TREND (flow not with it) | **PUTS** | 47 | 11/06 98P @ 0.79 (delta 0.26) = est +27% at 100 | POS +$2.7M | 99.98 | 102 | 100 | +$43k | +$0 bull / -$28k bear | SHORT (clean 35, ADX 59, RVol 1.2) |
| 6 | **AVGO** | 332.89 | FLOW SURGE | **CALLS** | 43 | none: 81 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (3 contracts' greeks worked out here) | NEG -$61.6M | - | 340 | 340 | +$2.9M | +$403k bull / +$0 bear | out (clean 32, ADX 35, RVol 1.2) |
| 7 | **META** | 616.60 | FLOW SURGE | **PUTS** | 42 | none: 149 puts 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (5 contracts' greeks worked out here) | NEG -$60.3M | 626.36 | 650 | 610 | -$11.0M | +$174k bull / -$1.9M bear | out (clean 27, ADX 27, RVol 0.7) |
| 8 | **SMCI** | 31.71 | TREND (flow not with it) | **CALLS** | 36 | none: 12 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$2.2M | - | 34.5 | 30 | -$260k | +$0 bull / -$81k bear | LONG (clean 36, ADX 33, RVol 1.8) |
| 9 | **SHOP** | 142.47 | - | **-** | 31 | - | NEG -$3.9M | - | 145 | 140 | -$3.8M | - | out (clean 32, ADX 55, RVol 2.9) |
| 10 | **GOOGL** | 278.85 | TREND (flow not with it) | **PUTS** | 28 | none: 66 puts 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (6 contracts' greeks worked out here) | NEG -$39.0M | 284.53 | 285 | 290 | +$2.1M | - | SHORT (clean 34, ADX 36, RVol 0.5) |
| 11 | **MSFT** | 514.14 | - | **-** | 27 | - | POS +$158.1M | 500.97 | 540 | 500 | -$2.2M | +$0 bull / -$192k bear | out (clean 29, ADX 40, RVol 0.8) |
| 12 | **PLTR** | 171.26 | - | **-** | 26 | - | NEG -$29.0M | - | 165 | 180 | +$1.6M | +$334k bull / -$521k bear | out (clean 28, ADX 57, RVol 3.1) |
| 13 | **SMH** | 520.64 | - | **-** | 24 | - | NEG -$269.3M | - | 532.5 | 500 | +$1.2M | +$288k bull / +$0 bear | out (clean 33, ADX 36, RVol 1.0) |
| 14 | **CRM** | 219.44 | - | **-** | 24 | - | NEG -$14.7M | - | 240 | 220 | -$149k | +$0 bull / -$29k bear | out (clean 28, ADX 52, RVol 0.7) |
| 15 | **AAPL** | 332.43 | - | **-** | 23 | - | NEG -$372.0M | 343.59 | 350 | 330 | -$13.5M | +$209k bull / -$2.5M bear | out (clean 32, ADX 31, RVol 1.6) |
| 16 | **AMD** | 490.59 | - | **-** | 22 | - | NEG -$66.4M | - | 520 | 500 | +$1.8M | +$684k bull / -$1.6M bear | out (clean 33, ADX 44, RVol 1.6) |
| 17 | **NVDA** | 208.03 | - | **-** | 21 | - | POS +$113.9M | 203.63 | 210 | 200 | +$3.8M | +$262k bull / -$546k bear | out (clean 31, ADX 39, RVol 0.9) |
| 18 | **SPY** | 754.48 | - | **-** | 20 | - | NEG -$9.0B | 770.29 | 770 | 750 | -$21.7M | +$0 bull / -$2.0M bear | out (clean 31, ADX 27, RVol 1.0) |
| 19 | **MU** | 860.22 | - | **-** | 20 | - | NEG -$187.5M | - | 900 | 850 | +$6.0M | +$6.1M bull / -$1.7M bear | out (clean 32, ADX 37, RVol 1.1) |
| 20 | **HOOD** | 84.55 | - | **-** | 20 | - | NEG -$2.8M | - | 90 | 85 | -$214k | +$72k bull / +$0 bear | out (clean 31, ADX 27, RVol 0.8) |
| 21 | **TSLA** | 401.88 | - | **-** | 19 | - | POS +$241.9M | - | 400 | 400 | +$8.0M | +$1.3M bull / -$1.7M bear | out (clean 31, ADX 23, RVol 0.7) |
| 22 | **AMZN** | 247.12 | - | **-** | 19 | - | POS +$135.7M | 236.2 | 250 | 250 | +$772k | +$27k bull / -$28k bear | out (clean 33, ADX 27, RVol 0.6) |
| 23 | **QQQ** | 686.52 | - | **-** | 18 | - | NEG -$5.0B | - | 700 | 680 | +$5.6M | +$868k bull / -$779k bear | out (clean 32, ADX 28, RVol 1.1) |
| 24 | **IWM** | 280.97 | - | **-** | 13 | - | NEG -$1.0B | 287.18 | 285 | 270 | -$3.9M | - | out (clean 33, ADX 19, RVol 1.1) |
| 25 | **UBER** | 66.55 | - | **-** | 12 | - | NEG -$13.6M | - | 70 | 65 | -$29k | - | out (clean 29, ADX 26, RVol 0.9) |
| 26 | **NFLX** | 62.29 | - | **-** | 10 | - | NEG -$12.7M | 64.28 | 63 | 60 | -$147k | - | out (clean 28, ADX 26, RVol 0.6) |
| 27 | **ARM** | 203.57 | - | **-** | 9 | - | NEG -$6.5M | - | 220 | 200 | -$65k | - | out (clean 25, ADX 30, RVol 0.4) |

## Big prints this scan (117)
- **AAPL** PUT 335 2026-11-06 (3DTE): 1,540 @ 6.75 = **+$1.0M** BUY | vol 7,257 / OI 9,304
- **META** PUT 590 2026-11-06 (3DTE): 1,025 @ 3.67 = **+$376k** BUY | vol 2,132 / OI 4,468
- **SPY** CALL 745 2026-11-05 (2DTE): 342 @ 10.95 = **+$374k** SELL | vol 3,128 / OI 186
- **SPY** CALL 745 2026-11-05 (2DTE): 335 @ 10.95 = **+$367k** SELL | vol 3,128 / OI 186
- **NVDA** PUT 207.5 2026-11-06 (3DTE): 712 @ 3.80 = **+$271k** MID | vol 5,542 / OI 3,523
- **META** CALL 620 2026-11-06 (3DTE): 240 @ 10.50 = **+$252k** MID | vol 1,212 / OI 1,626
- **SPY** CALL 745 2026-11-05 (2DTE): 214 @ 10.95 = **+$234k** SELL | vol 3,128 / OI 186
- **META** PUT 590 2026-11-06 (3DTE): 512 @ 3.75 = **+$192k** BUY | vol 2,132 / OI 4,468
- **META** PUT 590 2026-11-06 (3DTE): 512 @ 3.65 = **+$187k** BUY | vol 2,132 / OI 4,468
- **SPY** PUT 753 2026-11-03 (0DTE): 1,000 @ 1.83 = **+$183k** BUY | vol 56,317 / OI 1,327
- **MU** CALL 850 2026-11-06 (3DTE): 52 @ 34.20 = **+$178k** BUY | vol 407 / OI 341
- **SPY** PUT 753 2026-11-09 (6DTE): 252 @ 6.90 = **+$174k** BUY | vol 929 / OI 0
- **QQQ** CALL 680 2026-11-03 (0DTE): 250 @ 6.84 = **+$171k** SELL | vol 1,836 / OI 340
- **AAPL** PUT 335 2026-11-06 (3DTE): 210 @ 6.74 = **+$142k** BUY | vol 7,257 / OI 9,304
- **PLTR** PUT 170 2026-11-06 (3DTE): 259 @ 5.04 = **+$131k** BUY | vol 5,212 / OI 2,434

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 753 2026-11-05 (2DTE): 517 traded vs OI 0
- **SPY** CALL 776 2026-11-05 (2DTE): 666 traded vs OI 0
- **SPY** CALL 746 2026-11-03 (0DTE): 518 traded vs OI 73
- **SPY** PUT 760 2026-11-03 (0DTE): 1,398 traded vs OI 1,389
- **SPY** CALL 754 2026-11-05 (2DTE): 510 traded vs OI 0
- **SPY** CALL 751 2026-11-04 (1DTE): 561 traded vs OI 214
- **SPY** PUT 753 2026-11-09 (6DTE): 929 traded vs OI 0
- **SPY** PUT 680 2026-11-10 (7DTE): 705 traded vs OI 0
- **SPY** CALL 790 2026-11-16 (13DTE): 501 traded vs OI 0
- **QQQ** PUT 672 2026-11-04 (1DTE): 641 traded vs OI 275
- **QQQ** CALL 699 2026-11-05 (2DTE): 540 traded vs OI 0
- **QQQ** PUT 630 2026-11-05 (2DTE): 847 traded vs OI 0
- **QQQ** CALL 729 2026-11-04 (1DTE): 891 traded vs OI 768
- **QQQ** CALL 691 2026-11-04 (1DTE): 922 traded vs OI 914
- **QQQ** CALL 697 2026-11-05 (2DTE): 639 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
