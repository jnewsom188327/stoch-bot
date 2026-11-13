# GEX + FLOW SCAN - Fri Nov 13, 02:40 PM ET
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
Last 1m check 14:40:08 ET, last candle SPY 14:39, QQQ 14:39 | no errors
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
| 1 | **GOOGL** | 295.11 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 43 | 11/13 295P @ 0.72 (delta 0.48) = est +41% at 293.97 | POS +$194.9M | 289.87 | 295 | 290 | +$20.5M | +$112k bull / -$52k bear | out (clean 31, ADX 12, RVol 0.6) |
| 2 | **TSLA** | 391.59 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 34 | none: 128 puts 0-7DTE > 7 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only -25% at the target (needs +20%) (50 contracts' greeks worked out here) | POS +$408.4M | 384.5 | 392.5 | 390 | +$39.8M | +$1.4M bull / -$490k bear | out (clean 28, ADX 12, RVol 0.5) |
| 3 | **META** | 640.79 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 34 | none: 190 calls 0-7DTE > 9 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (84 contracts' greeks worked out here) | POS +$142.8M | 636.05 | 650 | 640 | -$1.3M | +$206k bull / +$0 bear | out (clean 30, ADX 30, RVol 0.5) |
| 4 | **AMZN** | 265.50 | PINNED between the walls (positive gamma) - chop | **-** | 30 | - | POS +$489.9M | 251.73 | 265 | 265 | +$8.2M | +$827k bull / -$453k bear | out (clean 29, ADX 13, RVol 0.2) |
| 5 | **MU** | 770.05 | FLIP CROSS down into negative gamma | **PUTS** | 30 | none: 160 puts 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (82 contracts' greeks worked out here) | NEG -$2.3M | 774.07 | 770 | 770 | +$64.0M | +$2.1M bull / -$1.5M bear | out (clean 30, ADX 23, RVol 0.4) |
| 6 | **ORCL** | 125.50 | FLIP CROSS down into negative gamma | **PUTS** | 30 | 11/13 126P @ 0.74 (delta 0.68) = est +32% at 125 | NEG -$8.2M | 125.84 | 125 | 125 | -$1.7M | +$260k bull / +$0 bear | out (clean 31, ADX 26, RVol 0.4) |
| 7 | **AVGO** | 345.79 | - | **-** | 20 | - | POS +$88.0M | - | 350 | 350 | +$16.8M | +$107k bull / +$0 bear | out (clean 36, ADX 14, RVol 0.2) |
| 8 | **SPY** | 753.35 | - | **-** | 18 | - | NEG -$7.7B | 758.62 | 775 | 755 | +$201.8M | +$12.5M bull / -$2.0M bear | out (clean 33, ADX 21, RVol 0.4) |
| 9 | **QQQ** | 679.37 | - | **-** | 18 | - | NEG -$2.7B | 684.7 | 680 | 680 | +$214.7M | +$3.1M bull / -$236k bear | out (clean 32, ADX 20, RVol 0.4) |
| 10 | **SMH** | 485.31 | - | **-** | 18 | - | NEG -$260.8M | 502.15 | 500 | 475 | +$6.4M | +$346k bull / -$227k bear | out (clean 31, ADX 25, RVol 0.3) |
| 11 | **NVDA** | 162.45 | - | **-** | 18 | - | NEG -$320.5M | - | 175 | 160 | +$78.3M | +$1.9M bull / -$2.2M bear | out (clean 31, ADX 20, RVol 0.3) |
| 12 | **AMD** | 532.37 | - | **-** | 18 | - | POS +$65.6M | - | 530 | 530 | +$44.3M | +$2.9M bull / -$2.9M bear | out (clean 35, ADX 24, RVol 0.3) |
| 13 | **DELL** | 343.67 | - | **-** | 18 | - | NEG -$10.4M | - | 350 | 340 | +$4.0M | +$63k bull / +$0 bear | out (clean 38, ADX 19, RVol 0.6) |
| 14 | **MSTR** | 112.74 | - | **-** | 18 | - | NEG -$32.2M | - | 120 | 110 | +$127k | +$0 bull / -$275k bear | out (clean 32, ADX 37, RVol 0.9) |
| 15 | **SMCI** | 26.86 | - | **-** | 17 | - | NEG -$3.2M | 27.85 | 27 | 27 | -$1.8M | - | out (clean 34, ADX 35, RVol 0.3) |
| 16 | **AAPL** | 357.92 | - | **-** | 16 | - | POS +$1.2B | 349.37 | 360 | 360 | +$10.3M | +$181k bull / +$0 bear | out (clean 30, ADX 12, RVol 0.4) |
| 17 | **PLTR** | 169.22 | - | **-** | 14 | - | POS +$107.1M | 162.01 | 170 | 170 | -$6k | +$186k bull / -$856k bear | out (clean 30, ADX 18, RVol 0.3) |
| 18 | **ARM** | 190.10 | - | **-** | 14 | - | NEG -$3.2M | 191.63 | 190 | 190 | -$4.2M | - | out (clean 33, ADX 19, RVol 0.2) |
| 19 | **MSFT** | 524.50 | - | **-** | 13 | - | POS +$138.3M | 522.74 | 535 | 520 | -$398k | +$75k bull / +$0 bear | out (clean 31, ADX 7, RVol 0.7) |
| 20 | **IWM** | 277.30 | - | **-** | 10 | - | NEG -$2.5B | 282.68 | 285 | 275 | +$16.1M | - | out (clean 36, ADX 20, RVol 0.4) |
| 21 | **HOOD** | 78.53 | - | **-** | 10 | - | NEG -$16.7M | 80.26 | 78 | 79 | +$2.5M | - | out (clean 35, ADX 15, RVol 0.4) |
| 22 | **CRM** | 217.95 | - | **-** | 10 | - | NEG -$4.6M | 220.38 | 220 | 220 | +$141k | - | out (clean 28, ADX 22, RVol 0.3) |
| 23 | **UBER** | 69.64 | - | **-** | 9 | - | POS +$17.9M | 69.32 | 70 | 70 | +$247k | - | out (clean 33, ADX 18, RVol 0.2) |
| 24 | **COIN** | 128.94 | - | **-** | 7 | - | NEG -$23.3M | 132.11 | 140 | 130 | +$2.1M | - | out (clean 30, ADX 9, RVol 0.3) |
| 25 | **NFLX** | 62.44 | - | **-** | 6 | - | NEG -$37.4M | 63.37 | 65 | 62 | +$358k | - | out (clean 31, ADX 15, RVol 0.8) |
| 26 | **SHOP** | 147.44 | - | **-** | 3 | - | POS +$4.4M | 145.98 | 150 | 140 | -$30k | - | out (clean 31, ADX 8, RVol 0.5) |
| 27 | **BABA** | 94.05 | - | **-** | 3 | - | NEG -$20.9M | - | 100 | 95 | -$24k | - | out (clean 27, ADX 13, RVol 0.4) |

## Big prints this scan (68)
- **SPY** CALL 745 2026-11-16 (3DTE): 1,880 @ 9.29 = **+$1.7M** SELL | vol 90,411 / OI 981
- **SPY** CALL 745 2026-11-16 (3DTE): 335 @ 9.51 = **+$319k** BUY | vol 90,411 / OI 981
- **SPY** CALL 745 2026-11-16 (3DTE): 303 @ 9.51 = **+$288k** BUY | vol 90,411 / OI 981
- **SPY** CALL 745 2026-11-16 (3DTE): 297 @ 9.51 = **+$282k** BUY | vol 90,411 / OI 981
- **SPY** CALL 745 2026-11-16 (3DTE): 290 @ 9.51 = **+$276k** BUY | vol 90,411 / OI 981
- **SPY** CALL 745 2026-11-16 (3DTE): 279 @ 9.52 = **+$266k** BUY | vol 90,411 / OI 981
- **SPY** CALL 745 2026-11-16 (3DTE): 257 @ 9.51 = **+$244k** BUY | vol 90,411 / OI 981
- **MU** CALL 780 2026-11-20 (7DTE): 80 @ 30.08 = **+$241k** BUY | vol 1,852 / OI 1,054
- **QQQ** CALL 672 2026-11-13 (0DTE): 290 @ 8.03 = **+$233k** BUY | vol 20,151 / OI 893
- **QQQ** PUT 671 2026-11-16 (3DTE): 1,000 @ 1.84 = **+$184k** SELL | vol 8,952 / OI 236
- **SMH** CALL 500 2026-11-20 (7DTE): 199 @ 9.21 = **+$183k** BUY | vol 2,842 / OI 3,710
- **COIN** PUT 130 2026-11-20 (7DTE): 320 @ 5.39 = **+$172k** MID | vol 2,286 / OI 2,991
- **MU** CALL 770 2026-11-13 (0DTE): 300 @ 4.75 = **+$142k** BUY | vol 35,139 / OI 1,258
- **COIN** PUT 133 2026-11-13 (0DTE): 320 @ 4.24 = **+$136k** MID | vol 410 / OI 758
- **QQQ** CALL 675 2026-11-13 (0DTE): 264 @ 4.87 = **+$129k** BUY | vol 153,957 / OI 5,568

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 680 2026-11-27 (14DTE): 506 traded vs OI 0
- **QQQ** CALL 694 2026-12-04 (21DTE): 559 traded vs OI 375
- **TSLA** CALL 422.5 2026-11-16 (3DTE): 664 traded vs OI 655
- **AMD** PUT 530 2026-11-18 (5DTE): 511 traded vs OI 97
- **AMD** CALL 552.5 2026-11-16 (3DTE): 509 traded vs OI 94
- **AMD** CALL 570 2026-11-18 (5DTE): 505 traded vs OI 124
- **META** CALL 680 2026-11-16 (3DTE): 500 traded vs OI 175
- **MSFT** PUT 525 2026-11-16 (3DTE): 528 traded vs OI 341
- **AVGO** CALL 365 2026-11-18 (5DTE): 507 traded vs OI 49
- **MU** CALL 780 2026-11-18 (5DTE): 511 traded vs OI 280

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
