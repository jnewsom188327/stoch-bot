# GEX + FLOW SCAN - Tue Nov 03, 03:45 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 15:32:08 ET, last candle SPY 15:31, QQQ 15:31 | no errors

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **SHOP** | 143.28 | RUN: clean trend + negative gamma + flow agrees | **PUTS** | 70 | none: 25 puts 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$4.3M | - | 145 | 148 | -$3.8M | - | SHORT (clean 34, ADX 41, RVol 2.3) |
| 2 | **MSFT** | 521.24 | - | **-** | 27 | - | POS +$326.7M | 499.53 | 540 | 500 | -$12.1M | +$389k bull / +$0 bear | out (clean 28, ADX 39, RVol 1.1) |
| 3 | **ARM** | 202.34 | - | **-** | 25 | - | NEG -$6.6M | - | 220 | 200 | -$940k | +$0 bull / -$686k bear | out (clean 26, ADX 27, RVol 0.7) |
| 4 | **META** | 618.85 | - | **-** | 22 | - | NEG -$43.4M | 624.78 | 650 | 610 | -$13.9M | +$420k bull / -$129k bear | out (clean 30, ADX 33, RVol 0.7) |
| 5 | **AVGO** | 332.34 | - | **-** | 19 | - | NEG -$65.2M | - | 340 | 340 | +$4.1M | +$0 bull / -$76k bear | out (clean 30, ADX 12, RVol 0.5) |
| 6 | **NVDA** | 207.21 | - | **-** | 18 | - | POS +$89.5M | 204.07 | 210 | 200 | +$15.7M | +$311k bull / -$245k bear | out (clean 29, ADX 23, RVol 0.7) |
| 7 | **AMD** | 487.77 | - | **-** | 17 | - | NEG -$86.5M | - | 520 | 440 | +$6.1M | +$0 bull / -$1.0M bear | out (clean 32, ADX 22, RVol 0.9) |
| 8 | **GOOGL** | 279.11 | - | **-** | 17 | - | NEG -$37.1M | 284.3 | 285 | 290 | +$2.5M | +$0 bull / -$251k bear | out (clean 33, ADX 22, RVol 0.3) |
| 9 | **SMCI** | 31.55 | - | **-** | 17 | - | POS +$2.0M | - | 34.5 | 30 | +$409k | +$69k bull / +$0 bear | out (clean 33, ADX 11, RVol 1.9) |
| 10 | **SPY** | 754.20 | - | **-** | 16 | - | NEG -$9.5B | 769.95 | 750 | 750 | -$8.1M | +$1.7M bull / +$0 bear | out (clean 30, ADX 19, RVol 1.0) |
| 11 | **QQQ** | 685.62 | - | **-** | 16 | - | NEG -$5.0B | - | 700 | 680 | +$28.2M | +$215k bull / -$3.3M bear | out (clean 29, ADX 16, RVol 1.2) |
| 12 | **IWM** | 279.92 | - | **-** | 16 | - | NEG -$1.2B | 286.78 | 280 | 270 | +$1.5M | +$115k bull / +$0 bear | out (clean 33, ADX 24, RVol 0.5) |
| 13 | **SMH** | 519.38 | - | **-** | 16 | - | NEG -$285.0M | - | 532.5 | 500 | +$1.2M | +$0 bull / -$35k bear | out (clean 32, ADX 18, RVol 0.6) |
| 14 | **TSLA** | 397.14 | - | **-** | 16 | - | POS +$184.9M | - | 400 | 400 | +$19.2M | +$247k bull / +$0 bear | out (clean 31, ADX 16, RVol 0.5) |
| 15 | **AAPL** | 331.04 | - | **-** | 16 | - | NEG -$421.7M | 342.36 | 350 | 330 | -$9.2M | +$130k bull / +$0 bear | out (clean 30, ADX 17, RVol 0.9) |
| 16 | **DELL** | 408.20 | - | **-** | 15 | - | NEG -$25.9M | - | 440 | 400 | +$592k | +$0 bull / -$59k bear | out (clean 32, ADX 12, RVol 0.5) |
| 17 | **PLTR** | 175.45 | - | **-** | 14 | - | NEG -$17.6M | - | 190 | 180 | +$725k | +$200k bull / -$86k bear | out (clean 27, ADX 13, RVol 0.8) |
| 18 | **MU** | 853.31 | - | **-** | 14 | - | NEG -$217.2M | - | 900 | 850 | -$15.7M | +$514k bull / -$1.9M bear | out (clean 31, ADX 12, RVol 0.4) |
| 19 | **ORCL** | 125.75 | - | **-** | 14 | - | NEG -$38.8M | - | 135 | 125 | -$9.4M | - | out (clean 35, ADX 31, RVol 0.8) |
| 20 | **AMZN** | 252.03 | - | **-** | 12 | - | POS +$215.8M | - | 250 | 250 | -$4.0M | - | out (clean 33, ADX 36, RVol 1.3) |
| 21 | **UBER** | 66.89 | - | **-** | 12 | - | NEG -$7.9M | - | 70 | 65 | -$563k | - | out (clean 30, ADX 17, RVol 1.5) |
| 22 | **CRM** | 221.87 | - | **-** | 10 | - | NEG -$13.9M | - | 240 | 220 | -$305k | - | out (clean 29, ADX 16, RVol 0.8) |
| 23 | **COIN** | 145.33 | - | **-** | 9 | - | POS +$20.7M | - | 148 | 140 | -$1.9M | - | out (clean 30, ADX 20, RVol 0.4) |
| 24 | **NFLX** | 63.16 | - | **-** | 7 | - | NEG -$4.5M | 63.89 | 65 | 65 | -$177k | - | out (clean 28, ADX 22, RVol 0.9) |
| 25 | **MSTR** | 135.35 | - | **-** | 7 | - | POS +$90.6M | - | 135 | 125 | -$3.4M | - | out (clean 29, ADX 14, RVol 0.5) |
| 26 | **BABA** | 100.39 | - | **-** | 7 | - | POS +$1.6M | 99.91 | 102 | 100 | +$116k | - | out (clean 35, ADX 20, RVol 0.5) |
| 27 | **HOOD** | 85.36 | - | **-** | 5 | - | NEG -$162k | 85.63 | 90 | 90 | -$205k | - | out (clean 30, ADX 13, RVol 0.8) |

## Big prints this scan (33)
- **META** CALL 625 2026-11-06 (3DTE): 150 @ 9.02 = **+$135k** MID | vol 1,413 / OI 769
- **IWM** PUT 278 2026-11-06 (3DTE): 526 @ 2.18 = **+$115k** SELL | vol 1,798 / OI 6,182
- **QQQ** PUT 686 2026-11-05 (2DTE): 129 @ 8.87 = **+$114k** BUY | vol 1,558 / OI 0
- **AMD** PUT 477.5 2026-11-06 (3DTE): 50 @ 17.56 = **+$88k** BUY | vol 308 / OI 319
- **MSFT** CALL 530 2026-11-06 (3DTE): 172 @ 4.28 = **+$74k** BUY | vol 2,826 / OI 4,596
- **AAPL** PUT 340 2026-11-04 (1DTE): 82 @ 8.87 = **+$73k** SELL | vol 5,712 / OI 7,977
- **AMD** PUT 477.5 2026-11-06 (3DTE): 34 @ 17.56 = **+$60k** BUY | vol 308 / OI 319
- **AMD** PUT 465 2026-11-06 (3DTE): 45 @ 12.47 = **+$56k** BUY | vol 847 / OI 1,151
- **MU** CALL 865 2026-11-06 (3DTE): 30 @ 18.20 = **+$55k** SELL | vol 2,803 / OI 185
- **MU** PUT 845 2026-11-04 (1DTE): 35 @ 13.07 = **+$46k** BUY | vol 7,870 / OI 274
- **MU** PUT 845 2026-11-04 (1DTE): 34 @ 12.90 = **+$44k** BUY | vol 7,870 / OI 274
- **MU** CALL 880 2026-11-04 (1DTE): 80 @ 5.42 = **+$43k** SELL | vol 9,011 / OI 294
- **MU** CALL 880 2026-11-04 (1DTE): 80 @ 5.42 = **+$43k** SELL | vol 9,011 / OI 294
- **AMD** PUT 475 2026-11-04 (1DTE): 30 @ 13.58 = **+$41k** BUY | vol 1,362 / OI 204
- **AMD** PUT 475 2026-11-04 (1DTE): 30 @ 13.58 = **+$41k** BUY | vol 1,362 / OI 204

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 758 2026-11-13 (10DTE): 526 traded vs OI 459
- **SPY** CALL 754 2026-11-10 (7DTE): 503 traded vs OI 0
- **SPY** CALL 785 2026-11-17 (14DTE): 544 traded vs OI 0
- **QQQ** CALL 721 2026-11-04 (1DTE): 1,199 traded vs OI 710
- **QQQ** CALL 716 2026-11-06 (3DTE): 946 traded vs OI 909
- **QQQ** CALL 700 2026-11-06 (3DTE): 13,508 traded vs OI 13,477
- **QQQ** CALL 726 2026-11-27 (24DTE): 530 traded vs OI 357
- **SMH** PUT 517.5 2026-11-06 (3DTE): 863 traded vs OI 216
- **TSLA** PUT 397.5 2026-11-13 (10DTE): 501 traded vs OI 122
- **TSLA** PUT 370 2026-11-09 (6DTE): 501 traded vs OI 182
- **TSLA** PUT 405 2026-11-06 (3DTE): 2,003 traded vs OI 1,980
- **META** CALL 665 2026-11-04 (1DTE): 975 traded vs OI 289
- **AMZN** PUT 240 2026-11-06 (3DTE): 5,594 traded vs OI 5,224
- **MSFT** PUT 515 2026-11-06 (3DTE): 761 traded vs OI 752

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
