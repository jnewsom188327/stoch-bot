# GEX + FLOW SCAN - Fri Nov 13, 03:00 PM ET
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
Last 1m check 15:00:08 ET, last candle SPY 14:59, QQQ 14:59 | no errors
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
| 1 | **GOOGL** | 295.13 | PINNED between the walls (positive gamma) - chop | **-** | 37 | - | POS +$165.4M | 293.29 | 295 | 295 | +$20.3M | +$172k bull / +$0 bear | out (clean 30, ADX 13, RVol 0.5) |
| 2 | **AAPL** | 357.30 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 35 | 11/13 357.5P @ 0.68 (delta 0.55) = est +63% at 356.38 | POS +$1.1B | 349.34 | 357.5 | 355 | +$11.6M | +$134k bull / +$0 bear | out (clean 30, ADX 17, RVol 0.6) |
| 3 | **META** | 641.01 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 34 | none: 194 calls 0-7DTE > 10 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (86 contracts' greeks worked out here) | POS +$166.0M | 635.22 | 650 | 640 | -$1.0M | +$97k bull / -$513k bear | out (clean 30, ADX 25, RVol 0.6) |
| 4 | **TSLA** | 391.93 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 33 | none: 124 puts 0-7DTE > 5 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only -38% at the target (needs +20%) (44 contracts' greeks worked out here) | POS +$452.4M | 385.68 | 392.5 | 390 | +$40.9M | +$546k bull / +$0 bear | out (clean 28, ADX 11, RVol 0.4) |
| 5 | **ORCL** | 125.36 | FLIP CROSS down into negative gamma | **PUTS** | 31 | none: 50 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (39 contracts' greeks worked out here) | NEG -$8.9M | 125.82 | 125 | 125 | -$1.6M | +$32k bull / +$0 bear | out (clean 32, ADX 23, RVol 0.6) |
| 6 | **MU** | 771.55 | FLIP CROSS down into negative gamma | **PUTS** | 29 | none: 160 puts 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (72 contracts' greeks worked out here) | NEG -$75.2M | 784.5 | 770 | 770 | +$67.2M | +$2.5M bull / -$1.4M bear | out (clean 30, ADX 21, RVol 0.3) |
| 7 | **ARM** | 190.54 | - | **-** | 23 | - | NEG -$1.7M | 191.61 | 190 | 190 | -$4.0M | +$37k bull / +$0 bear | out (clean 33, ADX 17, RVol 0.1) |
| 8 | **AVGO** | 346.21 | - | **-** | 21 | - | POS +$102.6M | - | 350 | 350 | +$18.5M | +$308k bull / -$32k bear | out (clean 36, ADX 14, RVol 0.2) |
| 9 | **HOOD** | 78.42 | - | **-** | 21 | - | NEG -$14.2M | 80.04 | 78 | 80 | +$2.6M | +$25k bull / +$0 bear | out (clean 35, ADX 17, RVol 0.9) |
| 10 | **AMZN** | 265.35 | PINNED between the walls (positive gamma) - chop | **-** | 20 | - | POS +$423.0M | 252.97 | 265 | 265 | +$8.7M | - | out (clean 29, ADX 14, RVol 0.2) |
| 11 | **IWM** | 277.24 | - | **-** | 19 | - | NEG -$2.6B | 282.48 | 285 | 277 | +$16.5M | +$55k bull / +$0 bear | out (clean 36, ADX 17, RVol 0.4) |
| 12 | **COIN** | 128.71 | - | **-** | 19 | - | NEG -$22.0M | 132.57 | 140 | 130 | +$2.3M | +$82k bull / +$0 bear | out (clean 30, ADX 12, RVol 0.4) |
| 13 | **QQQ** | 679.75 | - | **-** | 18 | - | NEG -$3.5B | 690.64 | 680 | 680 | +$228.5M | +$1.2M bull / -$371k bear | out (clean 32, ADX 18, RVol 0.4) |
| 14 | **NVDA** | 163.21 | - | **-** | 18 | - | NEG -$317.6M | - | 175 | 165 | +$80.9M | +$1.9M bull / -$379k bear | out (clean 31, ADX 18, RVol 0.3) |
| 15 | **MSTR** | 112.52 | - | **-** | 18 | - | NEG -$44.1M | - | 120 | 110 | +$2.2M | +$1.7M bull / +$0 bear | out (clean 32, ADX 34, RVol 0.6) |
| 16 | **SPY** | 753.65 | - | **-** | 17 | - | NEG -$9.0B | 760.3 | 755 | 755 | +$218.7M | +$5.9M bull / -$573k bear | out (clean 33, ADX 18, RVol 0.3) |
| 17 | **SMH** | 486.69 | - | **-** | 17 | - | NEG -$263.7M | - | 500 | 490 | +$6.7M | +$303k bull / -$27k bear | out (clean 31, ADX 22, RVol 0.1) |
| 18 | **AMD** | 533.71 | - | **-** | 17 | - | POS +$35.1M | 528.34 | 530 | 530 | +$48.4M | +$3.5M bull / -$460k bear | out (clean 35, ADX 22, RVol 0.3) |
| 19 | **SMCI** | 26.78 | - | **-** | 16 | - | NEG -$2.8M | 27.96 | 27 | 27 | -$1.7M | - | out (clean 34, ADX 31, RVol 0.4) |
| 20 | **PLTR** | 169.16 | - | **-** | 14 | - | POS +$108.6M | 161.88 | 170 | 170 | +$227k | +$486k bull / +$0 bear | out (clean 29, ADX 15, RVol 0.4) |
| 21 | **MSFT** | 525.14 | - | **-** | 13 | - | POS +$167.0M | 522.83 | 535 | 520 | -$318k | +$0 bull / -$50k bear | out (clean 31, ADX 8, RVol 0.7) |
| 22 | **SHOP** | 147.37 | - | **-** | 13 | - | POS +$6.0M | 146.02 | 147 | 140 | +$36k | +$33k bull / +$0 bear | out (clean 30, ADX 7, RVol 0.5) |
| 23 | **BABA** | 93.97 | - | **-** | 13 | - | NEG -$20.2M | - | 100 | 95 | -$1k | +$30k bull / +$0 bear | out (clean 27, ADX 13, RVol 0.3) |
| 24 | **CRM** | 218.37 | - | **-** | 11 | - | NEG -$4.2M | 221.57 | 220 | 220 | +$137k | - | out (clean 28, ADX 24, RVol 1.0) |
| 25 | **UBER** | 69.50 | - | **-** | 10 | - | POS +$11.7M | 69.27 | 70 | 70 | +$283k | - | out (clean 33, ADX 15, RVol 0.2) |
| 26 | **DELL** | 342.69 | - | **-** | 8 | - | NEG -$11.3M | - | 350 | 340 | +$4.3M | - | out (clean 38, ADX 16, RVol 0.6) |
| 27 | **NFLX** | 62.30 | - | **-** | 7 | - | NEG -$48.0M | 63.6 | 65 | 62 | +$378k | - | out (clean 30, ADX 16, RVol 0.8) |

## Big prints this scan (56)
- **SPY** CALL 745 2026-11-16 (3DTE): 1,995 @ 9.30 = **+$1.9M** MID | vol 98,548 / OI 981
- **MU** CALL 780 2026-11-20 (7DTE): 142 @ 29.60 = **+$420k** SELL | vol 2,196 / OI 1,054
- **MU** CALL 780 2026-11-20 (7DTE): 90 @ 29.35 = **+$264k** SELL | vol 2,196 / OI 1,054
- **QQQ** PUT 675 2026-11-20 (7DTE): 300 @ 8.78 = **+$263k** BUY | vol 7,562 / OI 31,245
- **AMD** CALL 530 2026-11-18 (5DTE): 100 @ 21.15 = **+$212k** BUY | vol 901 / OI 56
- **QQQ** PUT 680 2026-11-20 (7DTE): 193 @ 10.62 = **+$205k** SELL | vol 11,552 / OI 87,076
- **SPY** CALL 762 2026-11-18 (5DTE): 1,178 @ 1.59 = **+$187k** SELL | vol 4,858 / OI 405
- **MU** CALL 780 2026-11-20 (7DTE): 52 @ 29.53 = **+$154k** SELL | vol 2,196 / OI 1,054
- **QQQ** PUT 680 2026-11-20 (7DTE): 141 @ 10.53 = **+$148k** SELL | vol 11,552 / OI 87,076
- **SPY** CALL 762 2026-11-18 (5DTE): 920 @ 1.59 = **+$146k** SELL | vol 4,858 / OI 405
- **SPY** CALL 753 2026-11-17 (4DTE): 260 @ 4.53 = **+$118k** SELL | vol 4,812 / OI 644
- **QQQ** CALL 680 2026-11-16 (3DTE): 248 @ 4.33 = **+$107k** SELL | vol 22,328 / OI 407
- **COIN** PUT 127 2026-11-20 (7DTE): 204 @ 4.04 = **+$82k** SELL | vol 621 / OI 74
- **AMD** PUT 540 2026-11-20 (7DTE): 25 @ 28.27 = **+$71k** BUY | vol 2,501 / OI 2,289
- **AMD** PUT 540 2026-11-20 (7DTE): 25 @ 28.27 = **+$71k** BUY | vol 2,501 / OI 2,289

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 777 2026-11-16 (3DTE): 1,107 traded vs OI 904
- **SPY** CALL 808 2026-11-20 (7DTE): 1,405 traded vs OI 1,312
- **SPY** PUT 748 2026-11-20 (7DTE): 3,470 traded vs OI 3,307
- **QQQ** PUT 644 2026-11-18 (5DTE): 511 traded vs OI 90
- **QQQ** PUT 629 2026-11-18 (5DTE): 528 traded vs OI 37
- **QQQ** PUT 631 2026-11-20 (7DTE): 609 traded vs OI 108
- **QQQ** PUT 612 2026-11-20 (7DTE): 539 traded vs OI 0
- **QQQ** CALL 735 2026-11-25 (12DTE): 529 traded vs OI 31
- **QQQ** PUT 674 2026-12-11 (28DTE): 564 traded vs OI 170
- **MSFT** PUT 505 2026-11-20 (7DTE): 4,191 traded vs OI 3,662
- **AVGO** PUT 342.5 2026-11-16 (3DTE): 501 traded vs OI 56
- **COIN** PUT 122 2026-11-20 (7DTE): 701 traded vs OI 577
- **COIN** PUT 127 2026-11-20 (7DTE): 621 traded vs OI 74
- **SMCI** PUT 27 2026-11-13 (0DTE): 3,290 traded vs OI 3,056
- **MU** CALL 780 2026-11-27 (14DTE): 591 traded vs OI 271

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
