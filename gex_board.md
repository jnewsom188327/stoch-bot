# GEX + FLOW SCAN - Fri Nov 13, 03:25 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (13)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 12:45 | **HOOD** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/13 78C | 0.58 | 0.44 | +12% (3m) | **-24%** (done) | +75% | 79 |
| 11:30 | **GOOGL** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/13 292.5P | 0.56 | 0.18 | +23% (10m) | **-68%** (done) | +237% | 290.96 |
| 11:15 | **ARM** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/13 180P | 0.79 | 0.03 | +18% (40m) | **-96%** (done) | +122% | 180 |
| 11:14 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/13 667P | 0.70 | 0.17 | +59% (9m) | **-76%** (done) | +21% | 672.05 hit |
| 10:36 | **SPY** | **PUTS** | 1m FAILED POP (R3 R4) | 11/13 743P | 0.61 | 0.22 | +13% (1m) | **-64%** (done) | +46% | 747.53 |
| 10:17 | **QQQ** | **CALLS** | 1m WHIPSAW (R1 R2) | 11/13 683C | 0.75 | 0.18 | -1% (0m) | **-76%** (done) | +60% | 678.58 |
| 10:15 | **ARM** | **PUTS** | FLIP CROSS down into negative gamma | 11/13 182.5P | 0.74 | 1.47 | +169% (50m) | **+99%** (done) | +96% | 183.6 hit |
| 10:15 | **ORCL** | **CALLS** | FLIP CROSS up into positive gamma | 11/13 124C | 0.65 | 0.35 | +89% (28m) | **-46%** (done) | +66% | 123.68 hit |
| 10:10 | **ORCL** | **PUTS** | FLIP CROSS down into negative gamma | 11/13 120P | 0.46 | 0.15 | +7% (5m) | **-67%** (done) | +63% | 121.25 |
| 10:05 | **GOOGL** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/13 297.5P | 0.74 | 3.42 | +396% (33m) | **+362%** (done) | +288% | 295 hit |
| 09:55 | **BABA** | **PUTS** | FLOW SURGE | 11/13 94P | 0.51 | 0.43 | +8% (43m) | **-16%** (done) | +49% | 93.36 |
| 09:45 | **UBER** | **CALLS** | TREND + FLOW | 11/13 70C | 0.59 | 0.06 | +0% (1m) | **-90%** (done) | +32% | 70.7 |
| 09:45 | **ORCL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/13 127C | 0.46 | 0.22 | +22% (2m) | **-52%** (done) | +48% | 126.38 |

## 1m RULES on SPY / QQQ - loose (5 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 15:25:08 ET, last candle SPY 15:24, QQQ 15:24 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 13:26 | QQQ | 1m AGREE FLIP | FULL | CALLS | up | logged (agree flip) |
| 11:13 | QQQ | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | **FIRE** QQQ261113P00667000 |
| 11:02 | QQQ | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |
| 10:35 | SPY | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | **FIRE** SPY261113P00743000 |
| 10:16 | QQQ | 1m WHIPSAW | R1 R2 | CALLS | TURNING your way | **FIRE** QQQ261113C00683000 |

## Flow surges NOT fired - price disagreed (40 today, last 5)
- 12:25 ARM PUTS: over EMA 20 - flow says one way, price says the other
- 11:45 HOOD CALLS: price -0.30 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 11:40 HOOD CALLS: under EMA 20 - flow says one way, price says the other
- 11:35 HOOD CALLS: under EMA 20 - flow says one way, price says the other
- 11:25 HOOD CALLS: price -0.54 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **GOOGL** | 295.44 | PINNED between the walls (positive gamma) - chop | **-** | 37 | - | POS +$177.4M | 293.46 | 295 | 295 | +$20.0M | +$0 bull / -$152k bear | out (clean 30, ADX 12, RVol 0.6) |
| 2 | **META** | 640.99 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 34 | none: 194 calls 0-7DTE > 8 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (94 contracts' greeks worked out here) | POS +$190.2M | 635.65 | 650 | 640 | -$1.5M | +$164k bull / -$144k bear | out (clean 30, ADX 24, RVol 0.6) |
| 3 | **AMZN** | 265.60 | PINNED between the walls (positive gamma) - chop | **-** | 30 | - | POS +$427.5M | 255.07 | 265 | 265 | +$8.2M | +$53k bull / -$970k bear | out (clean 29, ADX 11, RVol 0.4) |
| 4 | **MU** | 771.67 | FLIP CROSS down into negative gamma | **PUTS** | 30 | none: 160 puts 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (70 contracts' greeks worked out here) | NEG -$91.9M | 785.24 | 770 | 770 | +$64.6M | +$1.4M bull / -$2.0M bear | out (clean 30, ADX 23, RVol 0.5) |
| 5 | **TSLA** | 390.75 | PINNED between the walls (positive gamma) - chop | **-** | 29 | - | POS +$410.5M | 373.52 | 390 | 390 | +$45.1M | +$3.6M bull / -$1.5M bear | out (clean 28, ADX 10, RVol 0.6) |
| 6 | **MSFT** | 524.80 | PINNED between the walls (positive gamma) - chop | **-** | 24 | - | POS +$180.1M | 522.74 | 525 | 525 | -$30k | +$30k bull / -$54k bear | out (clean 30, ADX 8, RVol 0.4) |
| 7 | **IWM** | 277.31 | - | **-** | 20 | - | NEG -$2.5B | 282.04 | 285 | 277 | +$16.9M | +$0 bull / -$420k bear | out (clean 36, ADX 20, RVol 0.4) |
| 8 | **AVGO** | 345.49 | - | **-** | 20 | - | POS +$88.7M | 331.03 | 350 | 340 | +$18.4M | +$0 bull / -$152k bear | out (clean 36, ADX 12, RVol 0.4) |
| 9 | **AAPL** | 356.80 | - | **-** | 19 | - | POS +$1.1B | 348.82 | 360 | 355 | +$12.3M | +$345k bull / -$75k bear | out (clean 30, ADX 24, RVol 0.9) |
| 10 | **SPY** | 753.26 | - | **-** | 18 | - | NEG -$9.2B | 760.1 | 754 | 755 | +$223.5M | +$5.2M bull / -$4.7M bear | out (clean 33, ADX 18, RVol 0.7) |
| 11 | **QQQ** | 679.44 | - | **-** | 18 | - | NEG -$3.8B | 690.67 | 680 | 680 | +$222.5M | +$288k bull / -$2.6M bear | out (clean 32, ADX 18, RVol 0.4) |
| 12 | **SMH** | 485.86 | - | **-** | 18 | - | NEG -$259.4M | - | 500 | 485 | +$6.4M | +$202k bull / -$380k bear | out (clean 31, ADX 24, RVol 0.4) |
| 13 | **NVDA** | 162.44 | - | **-** | 18 | - | NEG -$273.8M | - | 175 | 162.5 | +$80.7M | +$1.1M bull / -$2.9M bear | out (clean 31, ADX 20, RVol 0.4) |
| 14 | **DELL** | 342.84 | - | **-** | 18 | - | NEG -$12.8M | 353.88 | 350 | 340 | +$4.4M | +$34k bull / -$656k bear | out (clean 38, ADX 12, RVol 1.0) |
| 15 | **AMD** | 532.58 | - | **-** | 17 | - | POS +$31.5M | 524.12 | 530 | 530 | +$47.0M | +$790k bull / -$1.2M bear | out (clean 35, ADX 22, RVol 0.4) |
| 16 | **NFLX** | 62.28 | - | **-** | 17 | - | NEG -$46.8M | 63.43 | 65 | 62 | +$484k | +$0 bull / -$32k bear | out (clean 30, ADX 18, RVol 0.8) |
| 17 | **SMCI** | 26.71 | - | **-** | 15 | - | NEG -$2.8M | 27.95 | 27 | 27 | -$1.7M | - | out (clean 34, ADX 26, RVol 0.5) |
| 18 | **PLTR** | 168.65 | - | **-** | 14 | - | POS +$61.6M | 166.32 | 170 | 170 | +$310k | +$827k bull / -$80k bear | out (clean 29, ADX 12, RVol 0.8) |
| 19 | **ARM** | 190.22 | - | **-** | 13 | - | NEG -$5.2M | 192.24 | 190 | 190 | -$4.0M | - | out (clean 33, ADX 17, RVol 0.1) |
| 20 | **CRM** | 218.44 | - | **-** | 11 | - | NEG -$3.2M | 220.55 | 220 | 220 | +$146k | - | out (clean 27, ADX 28, RVol 0.9) |
| 21 | **HOOD** | 78.28 | - | **-** | 10 | - | NEG -$14.8M | 80.01 | 78 | 80 | +$2.4M | - | out (clean 35, ADX 15, RVol 0.8) |
| 22 | **UBER** | 69.29 | - | **-** | 10 | - | POS +$7.7M | 69.08 | 70 | 69 | +$293k | - | out (clean 32, ADX 14, RVol 0.6) |
| 23 | **COIN** | 128.84 | - | **-** | 8 | - | NEG -$21.4M | 132.05 | 140 | 130 | +$2.2M | - | out (clean 30, ADX 14, RVol 0.3) |
| 24 | **MSTR** | 112.69 | - | **-** | 8 | - | NEG -$43.6M | - | 120 | 110 | +$1.9M | - | out (clean 32, ADX 33, RVol 0.5) |
| 25 | **ORCL** | 125.29 | - | **-** | 8 | - | NEG -$5.5M | 125.65 | 125 | 125 | -$1.6M | - | out (clean 32, ADX 20, RVol 0.6) |
| 26 | **SHOP** | 147.45 | - | **-** | 4 | - | POS +$4.5M | 145.86 | 150 | 140 | +$49k | - | out (clean 30, ADX 9, RVol 0.6) |
| 27 | **BABA** | 93.97 | - | **-** | 4 | - | NEG -$21.0M | - | 100 | 94 | -$83k | - | out (clean 27, ADX 16, RVol 0.4) |

## Big prints this scan (68)
- **TSLA** CALL 375 2026-11-13 (0DTE): 1,580 @ 16.95 = **+$2.7M** BUY | vol 4,960 / OI 4,860
- **SPY** CALL 745 2026-11-16 (3DTE): 1,337 @ 9.25 = **+$1.2M** BUY | vol 110,905 / OI 981
- **SPY** CALL 745 2026-11-16 (3DTE): 397 @ 9.25 = **+$367k** BUY | vol 110,905 / OI 981
- **NVDA** PUT 160 2026-11-20 (7DTE): 500 @ 6.70 = **+$335k** BUY | vol 24,121 / OI 37,700
- **NVDA** PUT 160 2026-11-18 (5DTE): 280 @ 6.00 = **+$168k** SELL | vol 16,547 / OI 5,421
- **AMD** CALL 520 2026-11-13 (0DTE): 106 @ 13.50 = **+$143k** BUY | vol 4,306 / OI 947
- **NVDA** PUT 165 2026-11-16 (3DTE): 262 @ 4.30 = **+$113k** SELL | vol 14,617 / OI 5,380
- **MU** PUT 775 2026-11-16 (3DTE): 60 @ 17.20 = **+$103k** SELL | vol 1,656 / OI 70
- **SMH** CALL 490 2026-11-16 (3DTE): 207 @ 4.95 = **+$102k** BUY | vol 1,203 / OI 84
- **MU** PUT 775 2026-11-16 (3DTE): 48 @ 17.10 = **+$82k** SELL | vol 1,656 / OI 70
- **MU** PUT 770 2026-11-16 (3DTE): 49 @ 14.90 = **+$73k** SELL | vol 4,062 / OI 252
- **MU** PUT 775 2026-11-16 (3DTE): 36 @ 17.50 = **+$63k** BUY | vol 1,656 / OI 70
- **COIN** PUT 126 2026-11-20 (7DTE): 160 @ 3.69 = **+$59k** MID | vol 652 / OI 25
- **NVDA** CALL 162.5 2026-11-18 (5DTE): 75 @ 7.50 = **+$56k** BUY | vol 5,714 / OI 126
- **TSLA** PUT 392.5 2026-11-16 (3DTE): 100 @ 5.40 = **+$54k** SELL | vol 3,712 / OI 267

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 778 2026-11-17 (4DTE): 520 traded vs OI 280
- **SPY** CALL 815 2026-11-25 (12DTE): 680 traded vs OI 1
- **IWM** PUT 266 2026-11-16 (3DTE): 673 traded vs OI 583
- **SMH** PUT 462.5 2026-11-16 (3DTE): 798 traded vs OI 283
- **SMH** PUT 437.5 2026-11-16 (3DTE): 558 traded vs OI 0
- **NVDA** CALL 177.5 2026-11-18 (5DTE): 2,264 traded vs OI 2,069
- **TSLA** CALL 375 2026-11-13 (0DTE): 4,960 traded vs OI 4,860
- **AAPL** PUT 355 2026-11-27 (14DTE): 933 traded vs OI 924
- **AMD** CALL 540 2026-11-20 (7DTE): 4,305 traded vs OI 4,301
- **MSFT** CALL 537.5 2026-11-16 (3DTE): 502 traded vs OI 305
- **NFLX** CALL 61 2026-11-20 (7DTE): 656 traded vs OI 442
- **AVGO** CALL 370 2026-11-16 (3DTE): 500 traded vs OI 349
- **AVGO** CALL 370 2026-11-18 (5DTE): 539 traded vs OI 131
- **COIN** PUT 126 2026-11-20 (7DTE): 652 traded vs OI 25
- **MU** PUT 715 2026-11-16 (3DTE): 506 traded vs OI 99

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
