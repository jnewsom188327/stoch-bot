# GEX + FLOW SCAN - Tue Nov 10, 01:50 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (10)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 12:33 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 667P | 0.67 | 0.28 | +170% (8m) | **-58%** (done) | +15% | 668.83 hit |
| 12:22 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 667P | 0.66 | 0.79 | +174% (19m) | **+20%** (done) | +11% | 669.29 hit |
| 11:18 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 668P | 0.74 | 0.69 | +84% (38m) | **-7%** (done) | +18% | 672.3 hit |
| 11:17 | **SPY** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 744P | 0.60 | 0.36 | +38% (32m) | **-40%** (done) | +41% | 746.01 hit |
| 11:12 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 669P | 0.74 | 1.07 | +135% (44m) | **+45%** (done) | +38% | 671.74 hit |
| 11:12 | **SPY** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 744P | 0.64 | 0.38 | +30% (37m) | **-41%** (done) | +40% | 745.88 |
| 11:06 | **SPY** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 744P | 0.68 | 0.60 | +22% (43m) | **-12%** (done) | +49% | 745.54 |
| 10:15 | **IWM** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/10 280P | 0.63 | 1.39 | +232% (36m) | **+121%** (done) | +22% | 280 hit |
| 09:50 | **SPY** | **PUTS** | FLOW SURGE | 11/10 743P | 0.77 | 0.62 | +21% (60m) | **-19%** (done) | +54% | 745.65 |
| 09:45 | **IWM** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/10 279P | 0.52 | 0.95 | +90% (60m) | **+83%** (done) | +87% | 278.66 |

## 1m RULES on SPY / QQQ - loose (9 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 13:50:08 ET, last candle SPY 13:49, QQQ 13:48 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 12:32 | QQQ | 1m FAILED POP | R3 R4 | PUTS | WITH you | **FIRE** QQQ261110P00667000 |
| 12:21 | QQQ | 1m FAILED POP | R3 R4 | PUTS | TURNING your way | **FIRE** QQQ261110P00667000 |
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
| 1 | **MSFT** | 533.77 | - | **-** | 25 | - | POS +$448.9M | 502.95 | 550 | 500 | +$13.3M | +$0 bull / -$229k bear | out (clean 32, ADX 42, RVol 0.5) |
| 2 | **SHOP** | 144.41 | - | **-** | 24 | - | NEG -$320k | 145.01 | 150 | 140 | -$191k | +$0 bull / -$221k bear | out (clean 33, ADX 37, RVol 0.5) |
| 3 | **BABA** | 102.52 | - | **-** | 21 | - | NEG -$9.8M | 106.31 | 110 | 100 | -$138k | +$0 bull / -$28k bear | out (clean 31, ADX 42, RVol 0.7) |
| 4 | **AMZN** | 269.31 | - | **-** | 19 | - | POS +$464.5M | - | 270 | 265 | +$7.6M | +$0 bull / -$87k bear | out (clean 32, ADX 22, RVol 0.5) |
| 5 | **AMD** | 511.26 | - | **-** | 17 | - | POS +$50.2M | - | 500 | 500 | -$46.1M | +$0 bull / -$1.1M bear | out (clean 33, ADX 20, RVol 0.3) |
| 6 | **PLTR** | 165.57 | - | **-** | 17 | - | POS +$50.9M | - | 165 | 170 | -$786k | +$0 bull / -$126k bear | out (clean 28, ADX 24, RVol 0.1) |
| 7 | **SPY** | 747.28 | - | **-** | 16 | - | NEG -$7.5B | 760.08 | 750 | 730 | +$50.1M | +$0 bull / -$952k bear | out (clean 32, ADX 22, RVol 0.2) |
| 8 | **NVDA** | 168.31 | - | **-** | 16 | - | NEG -$170.2M | - | 185 | 170 | +$8.2M | +$225k bull / -$1.9M bear | out (clean 34, ADX 22, RVol 0.7) |
| 9 | **AVGO** | 328.33 | - | **-** | 16 | - | NEG -$13.3M | 341.88 | 340 | 320 | -$9.5M | +$0 bull / -$343k bear | out (clean 32, ADX 13, RVol 0.2) |
| 10 | **QQQ** | 670.32 | - | **-** | 15 | - | NEG -$2.1B | 692.24 | 670 | 680 | +$12.2M | +$102k bull / -$1.6M bear | out (clean 32, ADX 23, RVol 0.1) |
| 11 | **IWM** | 279.68 | - | **-** | 15 | - | NEG -$1.1B | 283.32 | 280 | 270 | +$2.2M | +$54k bull / +$0 bear | out (clean 36, ADX 17, RVol 0.3) |
| 12 | **MU** | 710.42 | - | **-** | 15 | - | NEG -$33.6M | - | 750 | 750 | -$15.6M | +$0 bull / -$1.7M bear | out (clean 30, ADX 18, RVol 0.2) |
| 13 | **TSLA** | 376.67 | - | **-** | 14 | - | POS +$194.3M | - | 400 | 380 | -$4.7M | +$28k bull / -$389k bear | out (clean 32, ADX 15, RVol 0.3) |
| 14 | **META** | 639.14 | - | **-** | 14 | - | POS +$234.0M | 607.46 | 650 | 650 | +$484k | +$0 bull / -$183k bear | out (clean 32, ADX 20, RVol 0.3) |
| 15 | **CRM** | 210.94 | - | **-** | 14 | - | NEG -$10.7M | - | 195 | 220 | +$308k | - | out (clean 30, ADX 34, RVol 0.2) |
| 16 | **AAPL** | 347.94 | - | **-** | 12 | - | POS +$424.5M | 336.07 | 350 | 340 | +$17.4M | - | out (clean 28, ADX 11, RVol 0.3) |
| 17 | **GOOGL** | 286.15 | - | **-** | 12 | - | NEG -$27.0M | 288.83 | 300 | 290 | +$3.3M | - | out (clean 30, ADX 32, RVol 0.4) |
| 18 | **ARM** | 178.01 | - | **-** | 12 | - | NEG -$4.7M | - | 185 | 190 | -$212k | - | out (clean 28, ADX 19, RVol 1.3) |
| 19 | **HOOD** | 80.35 | - | **-** | 11 | - | POS +$1.4M | 79.34 | 85 | 80 | +$619k | - | out (clean 31, ADX 34, RVol 0.3) |
| 20 | **DELL** | 327.52 | - | **-** | 9 | - | NEG -$11.1M | - | 350 | 340 | +$1.2M | - | out (clean 34, ADX 30, RVol 0.4) |
| 21 | **UBER** | 69.31 | - | **-** | 9 | - | POS +$5.4M | 68.36 | 70 | 70 | -$52k | - | out (clean 33, ADX 29, RVol 0.4) |
| 22 | **ORCL** | 116.88 | - | **-** | 8 | - | NEG -$24.6M | - | 120 | 120 | +$362k | - | out (clean 28, ADX 34, RVol 0.2) |
| 23 | **SMCI** | 27.53 | - | **-** | 7 | - | POS +$949k | 26.44 | 30 | 25 | -$54k | - | out (clean 30, ADX 30, RVol 0.3) |
| 24 | **NFLX** | 62.72 | - | **-** | 6 | - | NEG -$24.2M | 65.61 | 65 | 60 | -$131k | - | out (clean 29, ADX 22, RVol 0.3) |
| 25 | **COIN** | 131.28 | - | **-** | 6 | - | POS +$3.2M | 128.87 | 137 | 135 | +$130k | - | out (clean 29, ADX 24, RVol 0.1) |
| 26 | **MSTR** | 120.30 | - | **-** | 5 | - | NEG -$20.8M | - | 132 | 110 | +$166k | - | out (clean 30, ADX 21, RVol 0.3) |
| 27 | **SMH** | 479.58 | - | **-** | 4 | - | NEG -$226.2M | - | 500 | 475 | +$139k | - | out (clean 30, ADX 20, RVol 0.1) |

## Big prints this scan (47)
- **QQQ** PUT 670 2026-11-11 (1DTE): 500 @ 4.60 = **+$230k** BUY | vol 36,620 / OI 452
- **QQQ** CALL 650 2026-11-13 (3DTE): 74 @ 22.72 = **+$168k** SELL | vol 264 / OI 1,834
- **QQQ** PUT 672 2026-11-10 (0DTE): 690 @ 2.31 = **+$159k** BUY | vol 143,029 / OI 153
- **QQQ** PUT 670 2026-11-11 (1DTE): 325 @ 4.10 = **+$133k** BUY | vol 36,620 / OI 452
- **QQQ** PUT 670 2026-11-11 (1DTE): 256 @ 4.30 = **+$110k** BUY | vol 36,620 / OI 452
- **QQQ** PUT 668 2026-11-11 (1DTE): 300 @ 3.39 = **+$102k** BUY | vol 7,941 / OI 134
- **QQQ** PUT 674 2026-11-16 (6DTE): 100 @ 10.17 = **+$102k** SELL | vol 514 / OI 77
- **SPY** PUT 748 2026-11-10 (0DTE): 600 @ 1.67 = **+$100k** BUY | vol 262,782 / OI 832
- **AMD** PUT 500 2026-11-16 (6DTE): 61 @ 14.70 = **+$90k** BUY | vol 786 / OI 55
- **AMD** CALL 495 2026-11-13 (3DTE): 30 @ 25.80 = **+$77k** SELL | vol 365 / OI 481
- **NVDA** CALL 165 2026-11-13 (3DTE): 100 @ 6.45 = **+$64k** SELL | vol 5,324 / OI 157
- **MSFT** CALL 525 2026-11-11 (1DTE): 65 @ 9.75 = **+$63k** SELL | vol 427 / OI 69
- **NVDA** CALL 170 2026-11-13 (3DTE): 165 @ 3.74 = **+$62k** BUY | vol 25,309 / OI 389
- **AMD** PUT 500 2026-11-11 (1DTE): 100 @ 6.15 = **+$62k** BUY | vol 16,710 / OI 49
- **AVGO** CALL 325 2026-11-11 (1DTE): 100 @ 5.85 = **+$58k** SELL | vol 5,929 / OI 128

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 744 2026-11-12 (2DTE): 587 traded vs OI 536
- **QQQ** PUT 637 2026-11-11 (1DTE): 577 traded vs OI 115
- **QQQ** PUT 664 2026-11-12 (2DTE): 507 traded vs OI 81
- **QQQ** PUT 674 2026-11-16 (6DTE): 514 traded vs OI 77
- **QQQ** CALL 704 2026-11-16 (6DTE): 2,534 traded vs OI 2,533
- **NVDA** CALL 157.5 2026-11-16 (6DTE): 558 traded vs OI 0
- **TSLA** PUT 342.5 2026-11-11 (1DTE): 503 traded vs OI 254
- **META** PUT 637.5 2026-11-13 (3DTE): 513 traded vs OI 50
- **NFLX** CALL 64 2026-12-04 (24DTE): 599 traded vs OI 364
- **HOOD** PUT 80 2026-11-13 (3DTE): 2,711 traded vs OI 2,697

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
