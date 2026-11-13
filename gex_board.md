# GEX + FLOW SCAN - Fri Nov 13, 02:30 PM ET
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
Last 1m check 14:30:08 ET, last candle SPY 14:29, QQQ 14:29 | no errors
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
| 1 | **GOOGL** | 295.38 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 42 | none: 90 puts 0-7DTE > 7 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only -54% at the target (needs +20%) (39 contracts' greeks worked out here) | POS +$183.5M | 293.23 | 295 | 290 | +$20.2M | +$308k bull / -$52k bear | out (clean 30, ADX 11, RVol 0.5) |
| 2 | **TSLA** | 391.75 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 35 | none: 124 puts 0-7DTE > 5 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only -9% at the target (needs +20%) (52 contracts' greeks worked out here) | POS +$450.6M | 384.57 | 392.5 | 390 | +$39.0M | +$1.4M bull / -$1.2M bear | out (clean 28, ADX 14, RVol 0.6) |
| 3 | **ARM** | 190.48 | FLOW SURGE | **PUTS** | 33 | none: 30 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (24 contracts' greeks worked out here) | NEG -$3.8M | 192.07 | 190 | 190 | -$4.2M | +$0 bull / -$55k bear | out (clean 33, ADX 20, RVol 0.2) |
| 4 | **AVGO** | 346.47 | - | **-** | 20 | - | POS +$92.6M | 340.84 | 345 | 350 | +$16.3M | +$0 bull / -$40k bear | out (clean 36, ADX 15, RVol 0.2) |
| 5 | **QQQ** | 679.99 | - | **-** | 19 | - | NEG -$3.3B | 690.04 | 680 | 680 | +$209.1M | +$1.5M bull / -$904k bear | out (clean 32, ADX 22, RVol 0.5) |
| 6 | **SPY** | 753.60 | - | **-** | 18 | - | NEG -$8.8B | 760.22 | 755 | 755 | +$195.0M | +$7.0M bull / -$4.5M bear | out (clean 33, ADX 23, RVol 0.4) |
| 7 | **SMH** | 486.08 | - | **-** | 18 | - | NEG -$260.7M | - | 500 | 475 | +$6.2M | +$0 bull / -$632k bear | out (clean 31, ADX 25, RVol 0.4) |
| 8 | **NVDA** | 162.69 | - | **-** | 18 | - | NEG -$322.5M | - | 175 | 160 | +$76.6M | +$1.3M bull / -$3.0M bear | out (clean 31, ADX 21, RVol 0.4) |
| 9 | **AMD** | 533.95 | - | **-** | 18 | - | POS +$37.3M | 527.52 | 530 | 530 | +$44.8M | +$130k bull / -$5.7M bear | out (clean 35, ADX 24, RVol 0.3) |
| 10 | **AMZN** | 265.72 | - | **-** | 18 | - | POS +$438.7M | 253.39 | 265 | 265 | +$8.0M | +$58k bull / -$453k bear | out (clean 29, ADX 13, RVol 0.2) |
| 11 | **COIN** | 129.11 | - | **-** | 18 | - | NEG -$23.5M | 132.66 | 140 | 130 | +$2.0M | +$0 bull / -$734k bear | out (clean 30, ADX 10, RVol 0.3) |
| 12 | **DELL** | 344.46 | - | **-** | 18 | - | NEG -$14.3M | - | 350 | 340 | +$4.0M | +$32k bull / +$0 bear | out (clean 38, ADX 21, RVol 0.5) |
| 13 | **MU** | 771.09 | - | **-** | 18 | - | NEG -$63.0M | 780.83 | 770 | 770 | +$65.1M | +$663k bull / -$3.4M bear | out (clean 30, ADX 23, RVol 0.4) |
| 14 | **MSTR** | 112.95 | - | **-** | 18 | - | NEG -$42.1M | - | 120 | 110 | -$17k | +$0 bull / -$34k bear | out (clean 31, ADX 35, RVol 0.9) |
| 15 | **ORCL** | 125.45 | - | **-** | 18 | - | POS +$8.1M | 124.41 | 125 | 125 | -$1.8M | +$260k bull / -$234k bear | out (clean 31, ADX 25, RVol 0.3) |
| 16 | **META** | 641.16 | - | **-** | 17 | - | POS +$137.1M | 637.43 | 650 | 635 | -$1.9M | +$454k bull / -$58k bear | out (clean 30, ADX 33, RVol 0.6) |
| 17 | **SMCI** | 26.86 | - | **-** | 17 | - | NEG -$2.7M | 27.88 | 27 | 27 | -$1.8M | - | out (clean 34, ADX 34, RVol 0.3) |
| 18 | **AAPL** | 357.99 | - | **-** | 16 | - | POS +$1.2B | 349.32 | 360 | 360 | +$9.9M | +$216k bull / +$0 bear | out (clean 30, ADX 13, RVol 0.4) |
| 19 | **PLTR** | 169.25 | - | **-** | 14 | - | POS +$99.2M | 166.01 | 170 | 170 | -$364k | +$87k bull / -$897k bear | out (clean 29, ADX 18, RVol 0.2) |
| 20 | **MSFT** | 525.01 | - | **-** | 13 | - | POS +$151.2M | 523.05 | 535 | 520 | -$773k | +$0 bull / -$72k bear | out (clean 31, ADX 9, RVol 0.4) |
| 21 | **IWM** | 277.31 | - | **-** | 10 | - | NEG -$2.5B | 282.68 | 285 | 275 | +$16.1M | - | out (clean 36, ADX 20, RVol 0.3) |
| 22 | **UBER** | 69.55 | - | **-** | 10 | - | POS +$15.1M | 69.08 | 70 | 70 | +$259k | - | out (clean 33, ADX 16, RVol 0.2) |
| 23 | **CRM** | 218.01 | - | **-** | 10 | - | NEG -$4.3M | 221.61 | 220 | 220 | +$138k | - | out (clean 27, ADX 22, RVol 0.4) |
| 24 | **HOOD** | 78.66 | - | **-** | 9 | - | NEG -$19.3M | 80.21 | 79 | 80 | +$2.4M | - | out (clean 35, ADX 16, RVol 0.4) |
| 25 | **NFLX** | 62.48 | - | **-** | 7 | - | NEG -$45.0M | 63.65 | 65 | 62 | +$370k | - | out (clean 31, ADX 17, RVol 0.9) |
| 26 | **SHOP** | 147.58 | - | **-** | 3 | - | POS +$4.1M | 146.06 | 150 | 150 | -$31k | - | out (clean 31, ADX 9, RVol 0.5) |
| 27 | **BABA** | 94.00 | - | **-** | 3 | - | NEG -$19.2M | - | 100 | 95 | -$8k | - | out (clean 27, ADX 12, RVol 0.5) |

## Big prints this scan (125)
- **SPY** CALL 745 2026-11-16 (3DTE): 1,997 @ 9.10 = **+$1.8M** MID | vol 82,301 / OI 981
- **SPY** CALL 745 2026-11-16 (3DTE): 1,585 @ 9.50 = **+$1.5M** BUY | vol 82,301 / OI 981
- **SPY** CALL 745 2026-11-16 (3DTE): 801 @ 9.25 = **+$741k** BUY | vol 82,301 / OI 981
- **TSLA** CALL 395 2026-11-20 (7DTE): 500 @ 9.30 = **+$465k** BUY | vol 10,243 / OI 2,968
- **QQQ** CALL 675 2026-11-20 (7DTE): 220 @ 14.00 = **+$308k** BUY | vol 3,992 / OI 6,650
- **TSLA** CALL 405 2026-11-20 (7DTE): 500 @ 5.09 = **+$254k** BUY | vol 3,028 / OI 5,916
- **ORCL** CALL 122 2026-11-20 (7DTE): 369 @ 6.35 = **+$234k** BUY | vol 1,180 / OI 343
- **SPY** CALL 745 2026-11-16 (3DTE): 249 @ 9.25 = **+$230k** BUY | vol 82,301 / OI 981
- **SMH** PUT 500 2026-11-20 (7DTE): 99 @ 22.89 = **+$227k** BUY | vol 1,310 / OI 9,935
- **TSLA** CALL 395 2026-11-20 (7DTE): 248 @ 8.85 = **+$219k** SELL | vol 10,243 / OI 2,968
- **SPY** CALL 745 2026-11-16 (3DTE): 204 @ 9.25 = **+$189k** BUY | vol 82,301 / OI 981
- **SPY** CALL 745 2026-11-16 (3DTE): 199 @ 9.25 = **+$184k** BUY | vol 82,301 / OI 981
- **SPY** CALL 745 2026-11-16 (3DTE): 174 @ 9.25 = **+$161k** BUY | vol 82,301 / OI 981
- **PLTR** CALL 167.5 2026-11-20 (7DTE): 250 @ 6.00 = **+$150k** SELL | vol 863 / OI 1,479
- **AMD** PUT 550 2026-11-13 (0DTE): 80 @ 18.45 = **+$148k** BUY | vol 10,184 / OI 1,836

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 799 2026-11-17 (4DTE): 600 traded vs OI 292
- **SPY** CALL 764 2026-11-17 (4DTE): 562 traded vs OI 561
- **SPY** CALL 754 2026-11-20 (7DTE): 1,891 traded vs OI 1,868
- **QQQ** PUT 661 2026-11-17 (4DTE): 512 traded vs OI 311
- **QQQ** CALL 681 2026-11-20 (7DTE): 941 traded vs OI 684
- **QQQ** CALL 679 2026-11-20 (7DTE): 866 traded vs OI 780
- **TSLA** CALL 415 2026-11-23 (10DTE): 559 traded vs OI 91
- **AMD** PUT 575 2026-11-13 (0DTE): 1,477 traded vs OI 795
- **AMD** CALL 535 2026-11-18 (5DTE): 503 traded vs OI 122
- **AMD** CALL 525 2026-11-20 (7DTE): 912 traded vs OI 908
- **META** PUT 645 2026-11-13 (0DTE): 510 traded vs OI 302
- **META** PUT 580 2026-11-16 (3DTE): 547 traded vs OI 417
- **META** PUT 640 2026-11-16 (3DTE): 524 traded vs OI 214
- **AMZN** PUT 267.5 2026-11-20 (7DTE): 1,516 traded vs OI 776
- **MSFT** PUT 500 2026-11-18 (5DTE): 501 traded vs OI 226

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
