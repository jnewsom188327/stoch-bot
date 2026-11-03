# GEX + FLOW SCAN - Tue Nov 03, 03:00 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 15:00:08 ET, last candle SPY 14:59, QQQ 14:59 | no errors

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **SHOP** | 144.21 | RUN: clean trend + negative gamma + flow agrees | **PUTS** | 59 | none: 24 puts 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$4.3M | - | 145 | 148 | -$3.8M | +$41k bull / +$0 bear | SHORT (clean 34, ADX 32, RVol 1.3) |
| 2 | **MSTR** | 134.82 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 33 | none: 27 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$80.4M | - | 135 | 125 | -$3.1M | +$32k bull / +$0 bear | out (clean 29, ADX 14, RVol 0.3) |
| 3 | **MSFT** | 522.36 | - | **-** | 29 | - | POS +$285.2M | 500.62 | 540 | 500 | -$12.8M | +$0 bull / -$57k bear | out (clean 28, ADX 41, RVol 1.1) |
| 4 | **ORCL** | 124.47 | - | **-** | 25 | - | NEG -$40.5M | - | 135 | 120 | -$8.8M | +$94k bull / +$0 bear | out (clean 35, ADX 41, RVol 0.6) |
| 5 | **SMH** | 516.40 | - | **-** | 20 | - | NEG -$302.3M | - | 532.5 | 500 | +$2.9M | +$570k bull / +$0 bear | out (clean 32, ADX 22, RVol 0.7) |
| 6 | **META** | 619.60 | - | **-** | 20 | - | NEG -$44.5M | 625.74 | 650 | 610 | -$14.7M | +$31k bull / +$0 bear | out (clean 29, ADX 25, RVol 0.4) |
| 7 | **AMZN** | 251.40 | - | **-** | 20 | - | POS +$185.7M | - | 250 | 250 | -$3.7M | +$30k bull / -$88k bear | out (clean 33, ADX 36, RVol 0.7) |
| 8 | **AVGO** | 331.25 | - | **-** | 20 | - | NEG -$71.5M | - | 340 | 340 | +$4.6M | +$224k bull / +$0 bear | out (clean 31, ADX 16, RVol 0.3) |
| 9 | **NVDA** | 206.51 | - | **-** | 19 | - | POS +$67.2M | 203.98 | 210 | 200 | +$15.6M | +$188k bull / -$45k bear | out (clean 29, ADX 26, RVol 0.5) |
| 10 | **AMD** | 486.27 | - | **-** | 18 | - | NEG -$88.5M | - | 520 | 440 | +$10.9M | +$481k bull / -$65k bear | out (clean 32, ADX 23, RVol 0.6) |
| 11 | **SMCI** | 31.71 | - | **-** | 17 | - | POS +$2.1M | - | 34.5 | 30 | +$131k | +$27k bull / +$0 bear | out (clean 33, ADX 14, RVol 2.2) |
| 12 | **QQQ** | 684.34 | - | **-** | 16 | - | NEG -$5.2B | - | 700 | 680 | +$35.1M | +$616k bull / +$0 bear | out (clean 30, ADX 20, RVol 1.0) |
| 13 | **TSLA** | 397.57 | - | **-** | 16 | - | POS +$192.9M | - | 400 | 400 | +$18.0M | +$225k bull / +$0 bear | out (clean 31, ADX 18, RVol 0.3) |
| 14 | **SPY** | 753.88 | - | **-** | 15 | - | NEG -$9.5B | 770.27 | 750 | 750 | -$18.3M | +$613k bull / +$0 bear | out (clean 30, ADX 19, RVol 0.6) |
| 15 | **IWM** | 280.18 | - | **-** | 15 | - | NEG -$1.2B | 286.86 | 285 | 270 | +$1.1M | +$50k bull / +$0 bear | out (clean 33, ADX 18, RVol 0.5) |
| 16 | **PLTR** | 175.45 | - | **-** | 15 | - | NEG -$24.6M | - | 165 | 180 | +$54k | +$0 bull / -$359k bear | out (clean 27, ADX 15, RVol 1.0) |
| 17 | **AAPL** | 329.94 | - | **-** | 14 | - | NEG -$417.1M | 342.39 | 350 | 330 | -$6.9M | +$52k bull / +$0 bear | out (clean 30, ADX 14, RVol 0.4) |
| 18 | **HOOD** | 85.16 | - | **-** | 14 | - | NEG -$2.6M | - | 90 | 90 | -$26k | +$60k bull / +$0 bear | out (clean 30, ADX 16, RVol 0.7) |
| 19 | **MU** | 847.38 | - | **-** | 13 | - | NEG -$211.5M | - | 900 | 850 | -$13.1M | +$2.0M bull / +$0 bear | out (clean 31, ADX 11, RVol 0.2) |
| 20 | **UBER** | 66.69 | - | **-** | 11 | - | NEG -$8.6M | - | 70 | 65 | -$410k | - | out (clean 30, ADX 20, RVol 1.0) |
| 21 | **COIN** | 145.28 | - | **-** | 10 | - | POS +$21.4M | - | 148 | 140 | -$2.0M | - | out (clean 30, ADX 26, RVol 0.3) |
| 22 | **CRM** | 222.65 | - | **-** | 10 | - | NEG -$14.2M | - | 240 | 220 | -$322k | - | out (clean 29, ADX 12, RVol 0.7) |
| 23 | **GOOGL** | 278.50 | - | **-** | 8 | - | NEG -$42.5M | 284.54 | 285 | 290 | +$3.1M | - | out (clean 33, ADX 24, RVol 0.3) |
| 24 | **NFLX** | 62.94 | - | **-** | 8 | - | NEG -$8.9M | 64.37 | 63 | 60 | -$168k | - | out (clean 28, ADX 30, RVol 0.7) |
| 25 | **ARM** | 200.77 | - | **-** | 7 | - | NEG -$6.6M | - | 220 | 200 | -$72k | - | out (clean 26, ADX 30, RVol 0.4) |
| 26 | **BABA** | 100.33 | - | **-** | 6 | - | POS +$1.2M | 99.95 | 102 | 100 | +$74k | - | out (clean 36, ADX 23, RVol 0.3) |
| 27 | **DELL** | 405.61 | - | **-** | 5 | - | NEG -$25.9M | - | 440 | 400 | +$693k | - | out (clean 32, ADX 16, RVol 0.2) |

## Big prints this scan (51)
- **SMH** PUT 500 2026-11-06 (3DTE): 1,000 @ 5.34 = **+$534k** SELL | vol 2,800 / OI 41,518
- **MU** CALL 855 2026-11-06 (3DTE): 36 @ 23.30 = **+$84k** BUY | vol 2,593 / OI 99
- **AMD** PUT 465 2026-11-04 (1DTE): 70 @ 9.80 = **+$69k** SELL | vol 829 / OI 123
- **MU** CALL 855 2026-11-06 (3DTE): 28 @ 23.30 = **+$65k** BUY | vol 2,593 / OI 99
- **MU** CALL 855 2026-11-06 (3DTE): 27 @ 23.30 = **+$63k** BUY | vol 2,593 / OI 99
- **MU** CALL 855 2026-11-06 (3DTE): 25 @ 23.30 = **+$58k** BUY | vol 2,593 / OI 99
- **MSFT** PUT 505 2026-11-06 (3DTE): 284 @ 2.02 = **+$57k** BUY | vol 1,218 / OI 1,100
- **MU** PUT 850 2026-11-06 (3DTE): 22 @ 25.15 = **+$55k** SELL | vol 4,050 / OI 1,813
- **IWM** PUT 280 2026-11-06 (3DTE): 179 @ 2.80 = **+$50k** SELL | vol 2,740 / OI 4,747
- **MU** CALL 855 2026-11-06 (3DTE): 21 @ 23.30 = **+$49k** BUY | vol 2,593 / OI 99
- **MU** CALL 855 2026-11-06 (3DTE): 21 @ 23.30 = **+$49k** BUY | vol 2,593 / OI 99
- **MU** CALL 855 2026-11-06 (3DTE): 21 @ 23.30 = **+$49k** BUY | vol 2,593 / OI 99
- **MU** CALL 855 2026-11-06 (3DTE): 20 @ 23.30 = **+$47k** BUY | vol 2,593 / OI 99
- **MU** CALL 855 2026-11-06 (3DTE): 20 @ 23.30 = **+$47k** BUY | vol 2,593 / OI 99
- **MU** CALL 855 2026-11-06 (3DTE): 20 @ 23.13 = **+$46k** BUY | vol 2,593 / OI 99

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 750 2026-11-10 (7DTE): 931 traded vs OI 870
- **QQQ** PUT 630 2026-11-04 (1DTE): 1,452 traded vs OI 1,443
- **QQQ** PUT 675 2026-11-10 (7DTE): 551 traded vs OI 307
- **TSLA** PUT 390 2026-11-13 (10DTE): 506 traded vs OI 404
- **AMZN** CALL 267.5 2026-11-06 (3DTE): 503 traded vs OI 460
- **MSFT** PUT 505 2026-11-06 (3DTE): 1,218 traded vs OI 1,100
- **MSFT** PUT 502.5 2026-11-04 (1DTE): 791 traded vs OI 787
- **PLTR** CALL 180 2026-11-27 (24DTE): 524 traded vs OI 147
- **COIN** PUT 144 2026-11-06 (3DTE): 505 traded vs OI 138
- **ORCL** CALL 127 2026-11-13 (10DTE): 805 traded vs OI 150

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
