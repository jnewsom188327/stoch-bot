# GEX + FLOW SCAN - Tue Nov 10, 11:40 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (8)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:18 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 668P | 0.74 | 0.84 | +15% (22m) | **+14%** | +18% | 672.3 hit |
| 11:17 | **SPY** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 744P | 0.60 | 0.64 | +22% (1m) | **+7%** | +41% | 746.01 |
| 11:12 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 669P | 0.74 | 1.07 | +53% (28m) | **+45%** | +38% | 671.74 hit |
| 11:12 | **SPY** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 744P | 0.64 | 0.64 | +14% (6m) | **+0%** | +40% | 745.88 |
| 11:06 | **SPY** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 744P | 0.68 | 0.64 | +12% (0m) | **-6%** | +49% | 745.54 |
| 10:15 | **IWM** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/10 280P | 0.63 | 1.39 | +232% (36m) | **+121%** (done) | +22% | 280 hit |
| 09:50 | **SPY** | **PUTS** | FLOW SURGE | 11/10 743P | 0.77 | 0.62 | +21% (60m) | **-19%** (done) | +54% | 745.65 |
| 09:45 | **IWM** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/10 279P | 0.52 | 0.95 | +90% (60m) | **+83%** (done) | +87% | 278.66 |

## 1m RULES on SPY / QQQ - loose (7 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 11:40:08 ET, last candle SPY 11:39, QQQ 11:39 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 11:23 | QQQ | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |
| 11:17 | QQQ | 1m FAILED POP | R3 R4 | PUTS | TURNING your way | **FIRE** QQQ261110P00668000 |
| 11:16 | SPY | 1m FAILED POP | R3 R4 | PUTS | TURNING your way | **FIRE** SPY261110P00744000 |
| 11:14 | QQQ | 1m FAILED POP | R3 R4 | PUTS | TURNING your way | 5-minute cooldown |
| 11:11 | QQQ | 1m FAILED POP | R3 R4 | PUTS | TURNING your way | **FIRE** QQQ261110P00669000 |
| 11:11 | SPY | 1m FAILED POP | R3 R4 | PUTS | TURNING your way | **FIRE** SPY261110P00744000 |
| 11:05 | SPY | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | **FIRE** SPY261110P00744000 |

## Flow surges NOT fired - price disagreed (6 today, last 5)
- 10:15 BABA PUTS: price +0.24 over the last 15 min - flow says one way, price says the other
- 10:10 BABA PUTS: price +0.73 over the last 15 min - flow says one way, price says the other
- 10:00 NFLX CALLS: price -0.14 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:00 AAPL CALLS: price -2.97 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 09:55 BABA CALLS: price -0.98 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **IWM** | 278.75 | TREND (flow not with it) | **PUTS** | 25 | 11/10 278P @ 0.42 (delta 0.33) = est +96% at 277.48 | NEG -$1.4B | 283.75 | 280 | 270 | +$3.7M | - | SHORT (clean 36, ADX 45, RVol 0.4) |
| 2 | **GOOGL** | 287.13 | - | **-** | 22 | - | NEG -$17.6M | 289.03 | 300 | 290 | +$3.1M | +$81k bull / +$0 bear | out (clean 30, ADX 19, RVol 0.5) |
| 3 | **SHOP** | 145.54 | - | **-** | 22 | - | POS +$136k | 145.03 | 150 | 140 | +$58k | - | out (clean 32, ADX 49, RVol 0.4) |
| 4 | **NVDA** | 168.29 | - | **-** | 21 | - | NEG -$167.8M | - | 185 | 170 | +$12.3M | +$1.9M bull / +$0 bear | out (clean 33, ADX 36, RVol 1.5) |
| 5 | **AMZN** | 269.00 | - | **-** | 21 | - | POS +$465.6M | - | 270 | 265 | +$9.4M | +$95k bull / +$0 bear | out (clean 33, ADX 21, RVol 0.3) |
| 6 | **BABA** | 103.00 | - | **-** | 21 | - | NEG -$9.2M | 106.26 | 110 | 100 | -$157k | +$30k bull / +$0 bear | out (clean 30, ADX 40, RVol 0.6) |
| 7 | **AMD** | 517.63 | - | **-** | 19 | - | POS +$43.4M | - | 500 | 500 | -$49.3M | +$1.2M bull / +$0 bear | out (clean 31, ADX 20, RVol 0.7) |
| 8 | **SPY** | 746.91 | - | **-** | 18 | - | NEG -$7.6B | 760.31 | 750 | 730 | +$45.5M | +$1.8M bull / -$103k bear | out (clean 32, ADX 32, RVol 0.3) |
| 9 | **AVGO** | 325.91 | - | **-** | 18 | - | NEG -$16.0M | 339.85 | 340 | 320 | -$8.1M | +$328k bull / +$0 bear | out (clean 32, ADX 18, RVol 0.6) |
| 10 | **MSFT** | 541.35 | - | **-** | 17 | - | POS +$646.7M | - | 550 | 535 | -$49k | +$116k bull / +$0 bear | out (clean 32, ADX 34, RVol 0.5) |
| 11 | **MSTR** | 120.23 | - | **-** | 17 | - | NEG -$20.8M | - | 132 | 110 | -$345k | +$59k bull / +$0 bear | out (clean 29, ADX 31, RVol 0.5) |
| 12 | **QQQ** | 671.72 | - | **-** | 16 | - | NEG -$2.0B | 691.95 | 680 | 680 | +$21.1M | +$3.3M bull / +$0 bear | out (clean 31, ADX 25, RVol 0.3) |
| 13 | **AAPL** | 347.38 | - | **-** | 16 | - | POS +$389.5M | 336.27 | 350 | 340 | +$18.3M | - | out (clean 28, ADX 18, RVol 0.5) |
| 14 | **CRM** | 212.01 | - | **-** | 16 | - | NEG -$10.7M | - | 195 | 220 | -$98k | - | out (clean 30, ADX 37, RVol 0.1) |
| 15 | **SMH** | 479.31 | - | **-** | 15 | - | NEG -$230.6M | - | 500 | 475 | +$135k | +$185k bull / +$0 bear | out (clean 29, ADX 21, RVol 0.4) |
| 16 | **TSLA** | 376.00 | - | **-** | 15 | - | POS +$190.0M | - | 400 | 380 | -$2.3M | +$913k bull / +$0 bear | out (clean 34, ADX 24, RVol 0.2) |
| 17 | **MU** | 710.47 | - | **-** | 15 | - | NEG -$34.7M | - | 750 | 750 | -$1.1M | +$1.3M bull / -$243k bear | out (clean 30, ADX 23, RVol 0.4) |
| 18 | **HOOD** | 80.78 | - | **-** | 13 | - | POS +$2.1M | 79.21 | 85 | 80 | +$596k | - | out (clean 30, ADX 35, RVol 0.7) |
| 19 | **ARM** | 178.89 | - | **-** | 13 | - | NEG -$4.9M | - | 185 | 185 | -$220k | - | out (clean 27, ADX 28, RVol 0.4) |
| 20 | **PLTR** | 166.14 | - | **-** | 10 | - | POS +$51.4M | - | 165 | 170 | -$237k | - | out (clean 28, ADX 44, RVol 0.3) |
| 21 | **COIN** | 130.37 | - | **-** | 10 | - | POS +$993k | 129.45 | 137 | 135 | +$162k | - | out (clean 30, ADX 37, RVol 0.5) |
| 22 | **UBER** | 69.34 | - | **-** | 10 | - | POS +$4.7M | 68.42 | 70 | 70 | -$5k | - | out (clean 33, ADX 47, RVol 0.5) |
| 23 | **NFLX** | 62.72 | - | **-** | 8 | - | NEG -$24.1M | 65.58 | 65 | 60 | -$108k | - | out (clean 30, ADX 31, RVol 0.6) |
| 24 | **DELL** | 331.09 | - | **-** | 8 | - | NEG -$11.0M | - | 350 | 340 | +$591k | - | out (clean 33, ADX 28, RVol 0.4) |
| 25 | **SMCI** | 27.75 | - | **-** | 7 | - | POS +$2.4M | - | 30 | 25 | -$44k | - | out (clean 29, ADX 23, RVol 0.7) |
| 26 | **ORCL** | 118.28 | - | **-** | 5 | - | NEG -$24.4M | - | 130 | 120 | +$49k | - | out (clean 28, ADX 26, RVol 0.2) |
| 27 | **META** | 642.02 | - | **-** | 4 | - | POS +$256.9M | 605.01 | 650 | 650 | +$284k | - | out (clean 32, ADX 16, RVol 0.7) |

## Big prints this scan (46)
- **SPY** CALL 748 2026-11-13 (3DTE): 800 @ 5.17 = **+$414k** BUY | vol 5,475 / OI 1,196
- **AMD** CALL 525 2026-11-11 (1DTE): 200 @ 11.10 = **+$222k** BUY | vol 7,802 / OI 146
- **AMD** CALL 527.5 2026-11-13 (3DTE): 85 @ 16.28 = **+$138k** BUY | vol 985 / OI 116
- **QQQ** CALL 670 2026-11-11 (1DTE): 200 @ 6.59 = **+$132k** BUY | vol 1,428 / OI 1,811
- **NVDA** PUT 175 2026-11-13 (3DTE): 160 @ 8.23 = **+$132k** SELL | vol 6,797 / OI 6,657
- **SPY** CALL 748 2026-11-13 (3DTE): 200 @ 5.12 = **+$102k** BUY | vol 5,475 / OI 1,196
- **NVDA** CALL 170 2026-11-13 (3DTE): 221 @ 4.10 = **+$91k** BUY | vol 14,600 / OI 389
- **AMD** PUT 535 2026-11-11 (1DTE): 44 @ 17.25 = **+$76k** SELL | vol 2,512 / OI 9
- **AMD** PUT 525 2026-11-11 (1DTE): 66 @ 11.35 = **+$75k** SELL | vol 3,936 / OI 28
- **AAPL** PUT 342.5 2026-11-13 (3DTE): 400 @ 1.84 = **+$74k** MID | vol 1,529 / OI 1,408
- **SMH** CALL 472.5 2026-11-11 (1DTE): 50 @ 12.90 = **+$64k** BUY | vol 52 / OI 195
- **NVDA** CALL 170 2026-11-11 (1DTE): 267 @ 2.39 = **+$64k** BUY | vol 52,063 / OI 252
- **AMD** PUT 525 2026-11-11 (1DTE): 59 @ 10.60 = **+$63k** SELL | vol 3,936 / OI 28
- **NVDA** CALL 167.5 2026-11-16 (6DTE): 100 @ 6.05 = **+$60k** BUY | vol 2,119 / OI 9
- **MU** PUT 722.5 2026-11-13 (3DTE): 19 @ 28.30 = **+$54k** SELL | vol 235 / OI 517

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 786 2026-11-16 (6DTE): 805 traded vs OI 112
- **SPY** CALL 754 2026-11-13 (3DTE): 1,828 traded vs OI 1,732
- **SPY** PUT 724 2026-11-13 (3DTE): 1,233 traded vs OI 1,197
- **SPY** PUT 714 2026-11-11 (1DTE): 645 traded vs OI 541
- **SPY** CALL 748 2026-11-17 (7DTE): 525 traded vs OI 148
- **SPY** PUT 747 2026-11-17 (7DTE): 503 traded vs OI 67
- **SPY** CALL 791 2026-11-17 (7DTE): 783 traded vs OI 17
- **SPY** PUT 750 2026-11-23 (13DTE): 530 traded vs OI 0
- **IWM** PUT 278 2026-11-12 (2DTE): 706 traded vs OI 142
- **SMH** PUT 480 2026-11-11 (1DTE): 565 traded vs OI 133
- **NVDA** CALL 185 2026-11-20 (10DTE): 21,537 traded vs OI 7,095
- **TSLA** CALL 410 2026-11-18 (8DTE): 543 traded vs OI 111
- **TSLA** CALL 395 2026-11-13 (3DTE): 1,557 traded vs OI 1,549
- **TSLA** PUT 362.5 2026-11-13 (3DTE): 654 traded vs OI 632
- **AAPL** PUT 342.5 2026-11-13 (3DTE): 1,529 traded vs OI 1,408

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
