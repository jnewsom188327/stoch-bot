# GEX + FLOW SCAN - Tue Nov 10, 02:40 PM ET
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
Last 1m check 14:40:08 ET, last candle SPY 14:39, QQQ 14:39 | no errors
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
| 1 | **MSFT** | 534.88 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 37 | none: 129 calls 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (15 contracts' greeks worked out here) | POS +$475.1M | 504.71 | 550 | 535 | +$12.1M | +$31k bull / -$27k bear | out (clean 32, ADX 24, RVol 0.3) |
| 2 | **AVGO** | 330.14 | - | **-** | 20 | - | NEG -$10.0M | 340.75 | 340 | 340 | -$11.8M | +$0 bull / -$76k bear | out (clean 34, ADX 28, RVol 0.6) |
| 3 | **AMD** | 511.26 | - | **-** | 17 | - | POS +$52.2M | - | 500 | 500 | -$46.4M | +$1.2M bull / -$323k bear | out (clean 33, ADX 18, RVol 0.3) |
| 4 | **SPY** | 748.33 | - | **-** | 16 | - | NEG -$6.7B | 760.37 | 750 | 750 | +$32.9M | +$0 bull / -$252k bear | out (clean 32, ADX 26, RVol 0.3) |
| 5 | **AMZN** | 270.92 | - | **-** | 16 | - | POS +$479.3M | - | 270 | 265 | +$2.2M | +$0 bull / -$47k bear | out (clean 33, ADX 23, RVol 0.4) |
| 6 | **PLTR** | 166.02 | - | **-** | 16 | - | POS +$52.1M | - | 165 | 170 | -$889k | +$59k bull / +$0 bear | out (clean 28, ADX 16, RVol 0.4) |
| 7 | **DELL** | 330.04 | - | **-** | 16 | - | NEG -$11.0M | - | 350 | 340 | +$908k | +$31k bull / +$0 bear | out (clean 34, ADX 21, RVol 0.3) |
| 8 | **QQQ** | 671.41 | - | **-** | 15 | - | NEG -$2.0B | 692.02 | 680 | 680 | +$112k | +$1.6M bull / -$260k bear | out (clean 33, ADX 25, RVol 0.2) |
| 9 | **NVDA** | 166.85 | - | **-** | 15 | - | NEG -$155.6M | - | 180 | 170 | +$9.5M | +$731k bull / +$0 bear | out (clean 33, ADX 15, RVol 0.9) |
| 10 | **MU** | 708.49 | - | **-** | 15 | - | NEG -$31.4M | - | 750 | 750 | -$19.6M | +$1.2M bull / +$0 bear | out (clean 31, ADX 18, RVol 0.1) |
| 11 | **IWM** | 280.01 | - | **-** | 14 | - | NEG -$1.0B | 283.32 | 280 | 270 | +$1.8M | +$0 bull / -$66k bear | out (clean 36, ADX 16, RVol 0.3) |
| 12 | **TSLA** | 378.05 | - | **-** | 14 | - | POS +$203.9M | - | 400 | 380 | -$8.5M | +$0 bull / -$183k bear | out (clean 32, ADX 10, RVol 0.3) |
| 13 | **META** | 641.70 | - | **-** | 14 | - | POS +$249.5M | 604.88 | 650 | 650 | -$619k | +$0 bull / -$436k bear | out (clean 32, ADX 18, RVol 0.3) |
| 14 | **SMH** | 479.30 | - | **-** | 13 | - | NEG -$227.2M | - | 500 | 475 | +$47k | +$56k bull / +$0 bear | out (clean 30, ADX 18, RVol 0.1) |
| 15 | **AAPL** | 348.53 | - | **-** | 12 | - | POS +$441.1M | 336.5 | 350 | 340 | +$16.5M | - | out (clean 28, ADX 13, RVol 0.4) |
| 16 | **ARM** | 178.21 | - | **-** | 12 | - | NEG -$5.0M | - | 185 | 185 | -$216k | - | out (clean 27, ADX 19, RVol 1.2) |
| 17 | **CRM** | 211.31 | - | **-** | 12 | - | NEG -$10.8M | - | 195 | 220 | +$311k | - | out (clean 31, ADX 22, RVol 0.4) |
| 18 | **SHOP** | 144.66 | - | **-** | 11 | - | NEG -$552k | 145.7 | 150 | 140 | -$189k | - | out (clean 33, ADX 22, RVol 0.6) |
| 19 | **UBER** | 69.58 | - | **-** | 9 | - | POS +$6.0M | 68.51 | 70 | 70 | -$62k | - | out (clean 33, ADX 26, RVol 0.2) |
| 20 | **GOOGL** | 287.26 | - | **-** | 8 | - | NEG -$20.0M | 289.06 | 300 | 290 | +$2.4M | - | out (clean 29, ADX 21, RVol 0.2) |
| 21 | **HOOD** | 80.44 | - | **-** | 8 | - | POS +$1.4M | 79.49 | 85 | 80 | +$606k | - | out (clean 32, ADX 21, RVol 0.3) |
| 22 | **BABA** | 102.60 | - | **-** | 8 | - | NEG -$9.7M | 106.31 | 110 | 100 | -$161k | - | out (clean 30, ADX 25, RVol 0.5) |
| 23 | **NFLX** | 62.97 | - | **-** | 6 | - | NEG -$20.3M | 65.26 | 65 | 60 | -$185k | - | out (clean 29, ADX 18, RVol 0.7) |
| 24 | **ORCL** | 116.85 | - | **-** | 6 | - | NEG -$25.6M | - | 120 | 120 | +$384k | - | out (clean 28, ADX 22, RVol 0.2) |
| 25 | **COIN** | 130.99 | - | **-** | 5 | - | POS +$2.3M | 129.21 | 137 | 135 | +$200k | - | out (clean 28, ADX 18, RVol 0.3) |
| 26 | **SMCI** | 27.48 | - | **-** | 4 | - | POS +$932k | 26.43 | 30 | 25 | -$33k | - | out (clean 30, ADX 18, RVol 0.3) |
| 27 | **MSTR** | 119.94 | - | **-** | 4 | - | NEG -$26.3M | - | 130 | 110 | +$450k | - | out (clean 30, ADX 13, RVol 0.3) |

## Big prints this scan (33)
- **MU** PUT 710 2026-11-13 (3DTE): 74 @ 23.50 = **+$174k** SELL | vol 2,005 / OI 491
- **AMD** PUT 505 2026-11-13 (3DTE): 62 @ 13.00 = **+$81k** SELL | vol 1,752 / OI 276
- **MU** PUT 675 2026-11-11 (1DTE): 200 @ 3.20 = **+$64k** SELL | vol 8,701 / OI 27
- **NVDA** PUT 170 2026-11-11 (1DTE): 160 @ 3.95 = **+$63k** SELL | vol 132,573 / OI 4,288
- **NVDA** PUT 170 2026-11-11 (1DTE): 155 @ 3.70 = **+$57k** SELL | vol 132,573 / OI 4,288
- **SMH** CALL 482.5 2026-11-16 (6DTE): 50 @ 11.30 = **+$56k** BUY | vol 136 / OI 1
- **MU** CALL 735 2026-11-13 (3DTE): 37 @ 14.05 = **+$52k** BUY | vol 598 / OI 335
- **MU** PUT 720 2026-11-13 (3DTE): 18 @ 28.40 = **+$51k** SELL | vol 2,848 / OI 1,457
- **NVDA** CALL 170 2026-11-11 (1DTE): 266 @ 1.91 = **+$51k** BUY | vol 132,153 / OI 252
- **MSFT** PUT 520 2026-11-16 (6DTE): 200 @ 2.53 = **+$51k** MID | vol 915 / OI 25
- **AMD** CALL 512.5 2026-11-11 (1DTE): 40 @ 10.09 = **+$40k** BUY | vol 6,240 / OI 442
- **AMD** PUT 505 2026-11-13 (3DTE): 31 @ 13.00 = **+$40k** SELL | vol 1,752 / OI 276
- **MU** PUT 675 2026-11-11 (1DTE): 128 @ 3.00 = **+$38k** SELL | vol 8,701 / OI 27
- **MU** CALL 722.5 2026-11-13 (3DTE): 19 @ 18.75 = **+$36k** BUY | vol 412 / OI 572
- **AMD** PUT 505 2026-11-13 (3DTE): 27 @ 13.00 = **+$35k** SELL | vol 1,752 / OI 276

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 764 2026-11-12 (2DTE): 793 traded vs OI 783
- **SPY** PUT 751 2026-11-16 (6DTE): 514 traded vs OI 177
- **QQQ** CALL 701 2026-11-11 (1DTE): 582 traded vs OI 324
- **NVDA** PUT 182.5 2026-11-20 (10DTE): 518 traded vs OI 0
- **AAPL** PUT 350 2026-11-16 (6DTE): 500 traded vs OI 133
- **MSFT** PUT 495 2026-11-27 (17DTE): 541 traded vs OI 363
- **AVGO** PUT 307.5 2026-11-13 (3DTE): 545 traded vs OI 331
- **DELL** PUT 330 2026-11-13 (3DTE): 506 traded vs OI 464

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
