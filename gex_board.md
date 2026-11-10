# GEX + FLOW SCAN - Tue Nov 10, 11:50 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (8)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:18 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 668P | 0.74 | 1.03 | +64% (31m) | **+39%** | +18% | 672.3 hit |
| 11:17 | **SPY** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 744P | 0.60 | 0.68 | +38% (32m) | **+13%** | +41% | 746.01 |
| 11:12 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 669P | 0.74 | 1.27 | +107% (37m) | **+72%** | +38% | 671.74 hit |
| 11:12 | **SPY** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 744P | 0.64 | 0.68 | +30% (37m) | **+6%** | +40% | 745.88 |
| 11:06 | **SPY** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 744P | 0.68 | 0.68 | +22% (43m) | **+0%** | +49% | 745.54 |
| 10:15 | **IWM** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/10 280P | 0.63 | 1.39 | +232% (36m) | **+121%** (done) | +22% | 280 hit |
| 09:50 | **SPY** | **PUTS** | FLOW SURGE | 11/10 743P | 0.77 | 0.62 | +21% (60m) | **-19%** (done) | +54% | 745.65 |
| 09:45 | **IWM** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/10 279P | 0.52 | 0.95 | +90% (60m) | **+83%** (done) | +87% | 278.66 |

## 1m RULES on SPY / QQQ - loose (7 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 11:50:08 ET, last candle SPY 11:49, QQQ 11:49 | no errors
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
| 1 | **AAPL** | 347.66 | - | **-** | 26 | - | POS +$410.8M | 335.91 | 350 | 340 | +$18.2M | +$0 bull / -$31k bear | out (clean 28, ADX 18, RVol 0.4) |
| 2 | **SHOP** | 145.51 | - | **-** | 22 | - | POS +$748k | 144.17 | 150 | 140 | +$69k | - | out (clean 33, ADX 53, RVol 0.3) |
| 3 | **IWM** | 278.70 | - | **-** | 21 | - | NEG -$1.3B | 283.68 | 280 | 270 | +$4.3M | +$368k bull / +$0 bear | out (clean 36, ADX 45, RVol 0.4) |
| 4 | **NVDA** | 167.24 | - | **-** | 21 | - | NEG -$151.8M | - | 180 | 170 | +$19.4M | +$1.7M bull / +$0 bear | out (clean 33, ADX 37, RVol 1.5) |
| 5 | **PLTR** | 166.22 | - | **-** | 20 | - | POS +$51.3M | - | 165 | 170 | -$133k | +$159k bull / +$0 bear | out (clean 28, ADX 45, RVol 0.6) |
| 6 | **SPY** | 746.51 | - | **-** | 19 | - | NEG -$7.9B | 760.63 | 750 | 730 | +$65.0M | +$516k bull / +$0 bear | out (clean 32, ADX 32, RVol 0.4) |
| 7 | **AMD** | 511.77 | - | **-** | 19 | - | POS +$48.5M | - | 500 | 500 | -$37.3M | +$2.8M bull / +$0 bear | out (clean 31, ADX 22, RVol 0.9) |
| 8 | **DELL** | 328.94 | - | **-** | 19 | - | NEG -$10.9M | - | 350 | 340 | +$1.1M | +$29k bull / +$0 bear | out (clean 32, ADX 30, RVol 0.4) |
| 9 | **AVGO** | 324.82 | - | **-** | 18 | - | NEG -$18.8M | 342.16 | 340 | 320 | -$7.7M | +$191k bull / +$0 bear | out (clean 32, ADX 18, RVol 0.4) |
| 10 | **QQQ** | 670.67 | - | **-** | 17 | - | NEG -$2.2B | 693.56 | 680 | 680 | +$39.9M | +$1.6M bull / +$0 bear | out (clean 31, ADX 27, RVol 0.4) |
| 11 | **MSFT** | 543.31 | - | **-** | 17 | - | POS +$672.8M | - | 550 | 535 | -$191k | +$103k bull / +$0 bear | out (clean 32, ADX 32, RVol 0.4) |
| 12 | **MSTR** | 120.13 | - | **-** | 17 | - | NEG -$20.6M | - | 132 | 110 | +$95k | +$25k bull / +$0 bear | out (clean 29, ADX 32, RVol 0.4) |
| 13 | **SMH** | 477.01 | - | **-** | 16 | - | NEG -$238.9M | - | 500 | 475 | +$290k | +$129k bull / +$0 bear | out (clean 29, ADX 23, RVol 0.6) |
| 14 | **TSLA** | 375.22 | - | **-** | 16 | - | POS +$190.4M | - | 380 | 380 | -$1.0M | +$367k bull / +$0 bear | out (clean 34, ADX 25, RVol 0.5) |
| 15 | **MU** | 705.16 | - | **-** | 16 | - | NEG -$41.1M | - | 750 | 750 | +$4.9M | +$1.3M bull / +$0 bear | out (clean 30, ADX 25, RVol 0.4) |
| 16 | **CRM** | 212.53 | - | **-** | 16 | - | NEG -$10.9M | - | 195 | 220 | -$98k | - | out (clean 30, ADX 37, RVol 0.2) |
| 17 | **META** | 640.41 | - | **-** | 15 | - | POS +$247.2M | 604.88 | 650 | 650 | +$1.3M | +$123k bull / +$0 bear | out (clean 32, ADX 16, RVol 0.8) |
| 18 | **HOOD** | 80.52 | - | **-** | 14 | - | POS +$1.6M | 79.3 | 85 | 80 | +$629k | - | out (clean 30, ADX 37, RVol 0.7) |
| 19 | **ARM** | 178.13 | - | **-** | 13 | - | NEG -$5.1M | - | 185 | 185 | -$218k | - | out (clean 27, ADX 29, RVol 0.4) |
| 20 | **GOOGL** | 286.98 | - | **-** | 12 | - | NEG -$19.0M | 289.02 | 300 | 290 | +$3.2M | - | out (clean 30, ADX 20, RVol 0.5) |
| 21 | **COIN** | 130.18 | - | **-** | 12 | - | POS +$412k | 129.62 | 137 | 135 | +$242k | - | out (clean 29, ADX 39, RVol 1.0) |
| 22 | **BABA** | 102.94 | - | **-** | 11 | - | NEG -$8.4M | 106.07 | 110 | 100 | -$157k | - | out (clean 30, ADX 42, RVol 0.6) |
| 23 | **AMZN** | 268.74 | - | **-** | 10 | - | POS +$463.9M | - | 270 | 265 | +$9.4M | - | out (clean 33, ADX 22, RVol 0.3) |
| 24 | **UBER** | 69.50 | - | **-** | 9 | - | POS +$6.5M | 68.35 | 70 | 70 | -$8k | - | out (clean 33, ADX 48, RVol 0.3) |
| 25 | **NFLX** | 62.80 | - | **-** | 8 | - | NEG -$23.5M | 65.33 | 65 | 60 | -$102k | - | out (clean 30, ADX 30, RVol 0.6) |
| 26 | **SMCI** | 27.54 | - | **-** | 7 | - | POS +$923k | 26.4 | 30 | 25 | -$32k | - | out (clean 29, ADX 26, RVol 0.7) |
| 27 | **ORCL** | 118.57 | - | **-** | 5 | - | NEG -$24.1M | - | 130 | 120 | +$56k | - | out (clean 28, ADX 26, RVol 0.2) |

## Big prints this scan (29)
- **QQQ** PUT 686 2026-11-10 (0DTE): 1,000 @ 12.30 = **+$1.2M** SELL | vol 1,599 / OI 1,156
- **AMD** CALL 500 2026-11-13 (3DTE): 150 @ 30.00 = **+$450k** BUY | vol 2,348 / OI 2,434
- **IWM** PUT 278 2026-11-13 (3DTE): 2,000 @ 1.84 = **+$368k** SELL | vol 3,448 / OI 4,401
- **AMD** CALL 500 2026-11-13 (3DTE): 89 @ 30.00 = **+$267k** BUY | vol 2,348 / OI 2,434
- **AMD** CALL 500 2026-11-13 (3DTE): 89 @ 30.00 = **+$267k** BUY | vol 2,348 / OI 2,434
- **QQQ** PUT 671 2026-11-10 (0DTE): 1,000 @ 1.05 = **+$105k** SELL | vol 86,870 / OI 1,263
- **AMD** CALL 525 2026-11-11 (1DTE): 77 @ 9.66 = **+$74k** BUY | vol 8,143 / OI 146
- **NVDA** CALL 167.5 2026-11-16 (6DTE): 115 @ 6.25 = **+$72k** BUY | vol 2,265 / OI 9
- **AMD** CALL 500 2026-11-13 (3DTE): 22 @ 30.00 = **+$66k** BUY | vol 2,348 / OI 2,434
- **MSFT** PUT 542.5 2026-11-13 (3DTE): 100 @ 5.45 = **+$54k** SELL | vol 358 / OI 1,029
- **MSFT** PUT 542.5 2026-11-13 (3DTE): 89 @ 5.45 = **+$49k** SELL | vol 358 / OI 1,029
- **MU** CALL 730 2026-11-13 (3DTE): 25 @ 18.70 = **+$47k** BUY | vol 1,911 / OI 552
- **MU** CALL 730 2026-11-13 (3DTE): 25 @ 18.70 = **+$47k** BUY | vol 1,911 / OI 552
- **MU** PUT 700 2026-11-16 (6DTE): 20 @ 21.62 = **+$43k** SELL | vol 131 / OI 139
- **AMD** CALL 520 2026-11-11 (1DTE): 30 @ 12.20 = **+$37k** BUY | vol 10,296 / OI 166

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 706 2026-11-12 (2DTE): 626 traded vs OI 474
- **SPY** PUT 727 2026-11-13 (3DTE): 1,547 traded vs OI 1,497
- **SPY** CALL 789 2026-11-12 (2DTE): 507 traded vs OI 408
- **SPY** CALL 808 2026-11-20 (10DTE): 1,129 traded vs OI 877
- **SPY** CALL 743 2026-11-17 (7DTE): 500 traded vs OI 238
- **SPY** CALL 793 2026-11-17 (7DTE): 2,794 traded vs OI 260
- **QQQ** PUT 686 2026-11-10 (0DTE): 1,599 traded vs OI 1,156
- **QQQ** CALL 675 2026-11-16 (6DTE): 532 traded vs OI 117
- **TSLA** PUT 375 2026-12-04 (24DTE): 512 traded vs OI 335
- **AAPL** CALL 367.5 2026-11-11 (1DTE): 752 traded vs OI 147
- **AMD** PUT 465 2026-11-11 (1DTE): 1,208 traded vs OI 28
- **COIN** PUT 125 2026-11-13 (3DTE): 1,100 traded vs OI 1,038
- **MU** PUT 635 2026-11-11 (1DTE): 562 traded vs OI 0
- **MU** PUT 635 2026-11-20 (10DTE): 587 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
