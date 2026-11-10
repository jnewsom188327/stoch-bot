# GEX + FLOW SCAN - Tue Nov 10, 02:50 PM ET
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
Last 1m check 14:50:08 ET, last candle SPY 14:49, QQQ 14:49 | no errors
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
| 1 | **MSFT** | 535.83 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 36 | none: 129 calls 0-7DTE > 8 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (15 contracts' greeks worked out here) | POS +$494.1M | 503.9 | 550 | 535 | +$11.9M | +$0 bull / -$31k bear | out (clean 32, ADX 23, RVol 0.3) |
| 2 | **TSLA** | 379.19 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 31 | none: 90 calls 0-7DTE > 8 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (2 contracts' greeks worked out here) | POS +$206.3M | - | 400 | 380 | -$10.5M | +$0 bull / -$965k bear | out (clean 33, ADX 12, RVol 0.3) |
| 3 | **AVGO** | 332.21 | - | **-** | 21 | - | NEG -$10.5M | 342.77 | 340 | 340 | -$12.1M | +$0 bull / -$77k bear | out (clean 34, ADX 30, RVol 0.5) |
| 4 | **AMD** | 516.41 | - | **-** | 17 | - | POS +$45.9M | - | 500 | 500 | -$50.2M | +$257k bull / -$370k bear | out (clean 33, ADX 18, RVol 0.5) |
| 5 | **SPY** | 749.50 | - | **-** | 16 | - | NEG -$5.9B | 760.05 | 750 | 750 | +$21.0M | +$0 bull / -$484k bear | out (clean 32, ADX 28, RVol 0.3) |
| 6 | **AMZN** | 271.57 | - | **-** | 16 | - | POS +$481.2M | - | 270 | 265 | +$458k | +$0 bull / -$131k bear | out (clean 33, ADX 27, RVol 0.4) |
| 7 | **DELL** | 330.53 | - | **-** | 16 | - | NEG -$11.0M | - | 350 | 340 | +$942k | +$54k bull / +$0 bear | out (clean 34, ADX 19, RVol 0.2) |
| 8 | **ORCL** | 117.36 | - | **-** | 16 | - | NEG -$24.2M | - | 120 | 120 | +$370k | +$0 bull / -$25k bear | out (clean 28, ADX 20, RVol 0.3) |
| 9 | **NVDA** | 167.44 | - | **-** | 15 | - | NEG -$156.4M | - | 180 | 170 | +$11.8M | +$843k bull / +$0 bear | out (clean 33, ADX 15, RVol 1.0) |
| 10 | **MU** | 714.31 | - | **-** | 15 | - | NEG -$29.4M | - | 750 | 750 | -$21.2M | +$1.1M bull / -$154k bear | out (clean 31, ADX 17, RVol 0.2) |
| 11 | **IWM** | 280.26 | - | **-** | 14 | - | NEG -$847.2M | 282.99 | 280 | 280 | +$1.4M | +$0 bull / -$70k bear | out (clean 35, ADX 17, RVol 0.2) |
| 12 | **META** | 641.46 | - | **-** | 14 | - | POS +$250.2M | 607.48 | 650 | 650 | -$534k | +$126k bull / -$332k bear | out (clean 32, ADX 19, RVol 0.3) |
| 13 | **SMH** | 481.80 | - | **-** | 13 | - | NEG -$212.5M | - | 500 | 475 | -$22k | +$56k bull / +$0 bear | out (clean 30, ADX 17, RVol 0.1) |
| 14 | **SHOP** | 145.05 | - | **-** | 13 | - | POS +$121k | 144.93 | 150 | 140 | -$219k | - | out (clean 33, ADX 22, RVol 1.0) |
| 15 | **AAPL** | 348.71 | - | **-** | 12 | - | POS +$445.7M | 336.58 | 350 | 340 | +$16.4M | - | out (clean 28, ADX 14, RVol 0.4) |
| 16 | **CRM** | 211.15 | - | **-** | 12 | - | NEG -$10.9M | - | 195 | 220 | +$311k | - | out (clean 31, ADX 20, RVol 0.5) |
| 17 | **ARM** | 179.00 | - | **-** | 10 | - | NEG -$4.8M | - | 185 | 185 | -$216k | - | out (clean 27, ADX 18, RVol 0.2) |
| 18 | **UBER** | 69.62 | - | **-** | 9 | - | POS +$7.2M | 68.4 | 70 | 70 | -$64k | - | out (clean 33, ADX 24, RVol 0.2) |
| 19 | **GOOGL** | 287.63 | - | **-** | 8 | - | NEG -$16.7M | 289.1 | 300 | 290 | +$2.3M | - | out (clean 29, ADX 20, RVol 0.2) |
| 20 | **HOOD** | 80.87 | - | **-** | 8 | - | POS +$2.6M | 79.15 | 85 | 80 | +$586k | - | out (clean 32, ADX 19, RVol 0.2) |
| 21 | **BABA** | 102.59 | - | **-** | 7 | - | NEG -$9.5M | 106.26 | 110 | 100 | -$169k | - | out (clean 30, ADX 22, RVol 0.5) |
| 22 | **NFLX** | 62.96 | - | **-** | 6 | - | NEG -$22.8M | 65.35 | 65 | 60 | -$195k | - | out (clean 29, ADX 19, RVol 0.7) |
| 23 | **PLTR** | 166.51 | - | **-** | 6 | - | POS +$54.1M | - | 165 | 170 | -$915k | - | out (clean 28, ADX 16, RVol 0.4) |
| 24 | **QQQ** | 673.42 | - | **-** | 5 | - | NEG -$1.8B | 691.78 | 680 | 680 | -$6.5M | - | out (clean 33, ADX 26, RVol 0.2) |
| 25 | **COIN** | 131.61 | - | **-** | 5 | - | POS +$3.8M | 129.05 | 137 | 135 | +$171k | - | out (clean 28, ADX 17, RVol 0.3) |
| 26 | **SMCI** | 27.61 | - | **-** | 4 | - | POS +$1.2M | 26.38 | 30 | 25 | -$34k | - | out (clean 30, ADX 17, RVol 0.4) |
| 27 | **MSTR** | 120.32 | - | **-** | 4 | - | NEG -$20.7M | - | 132 | 110 | +$463k | - | out (clean 29, ADX 12, RVol 0.4) |

## Big prints this scan (22)
- **SPY** CALL 748 2026-11-10 (0DTE): 1,858 @ 1.08 = **+$201k** SELL | vol 393,602 / OI 4,785
- **SPY** CALL 748 2026-11-10 (0DTE): 1,488 @ 1.17 = **+$174k** SELL | vol 393,602 / OI 4,785
- **TSLA** PUT 380 2026-11-13 (3DTE): 190 @ 7.95 = **+$151k** BUY | vol 3,345 / OI 1,798
- **TSLA** PUT 375 2026-11-11 (1DTE): 489 @ 2.78 = **+$136k** BUY | vol 40,656 / OI 346
- **MU** CALL 735 2026-11-13 (3DTE): 70 @ 13.35 = **+$93k** SELL | vol 668 / OI 335
- **IWM** PUT 279 2026-11-16 (6DTE): 347 @ 2.03 = **+$70k** BUY | vol 2,270 / OI 138
- **TSLA** PUT 375 2026-11-11 (1DTE): 226 @ 2.77 = **+$63k** BUY | vol 40,656 / OI 346
- **TSLA** PUT 380 2026-11-13 (3DTE): 63 @ 7.95 = **+$50k** BUY | vol 3,345 / OI 1,798
- **AMZN** CALL 275 2026-11-16 (6DTE): 190 @ 2.55 = **+$48k** SELL | vol 2,901 / OI 345
- **AMD** CALL 512.5 2026-11-11 (1DTE): 48 @ 10.00 = **+$48k** SELL | vol 6,345 / OI 442
- **TSLA** PUT 375 2026-11-11 (1DTE): 150 @ 2.77 = **+$42k** BUY | vol 40,656 / OI 346
- **TSLA** PUT 375 2026-11-11 (1DTE): 149 @ 2.77 = **+$41k** BUY | vol 40,656 / OI 346
- **AMD** PUT 510 2026-11-11 (1DTE): 45 @ 8.60 = **+$39k** BUY | vol 8,169 / OI 85
- **AMD** PUT 510 2026-11-11 (1DTE): 44 @ 8.60 = **+$38k** BUY | vol 8,169 / OI 85
- **TSLA** PUT 380 2026-11-13 (3DTE): 47 @ 7.95 = **+$37k** BUY | vol 3,345 / OI 1,798

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 716 2026-11-12 (2DTE): 500 traded vs OI 328
- **SPY** CALL 758 2026-11-16 (6DTE): 503 traded vs OI 219
- **SPY** CALL 758 2026-11-17 (7DTE): 507 traded vs OI 131
- **SPY** CALL 755 2026-11-17 (7DTE): 753 traded vs OI 695
- **SPY** CALL 782 2026-11-27 (17DTE): 730 traded vs OI 672
- **IWM** CALL 285 2026-11-13 (3DTE): 4,923 traded vs OI 4,851
- **NVDA** CALL 165 2026-11-27 (17DTE): 525 traded vs OI 147
- **AVGO** CALL 365 2026-11-11 (1DTE): 559 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
