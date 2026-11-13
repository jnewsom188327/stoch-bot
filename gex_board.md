# GEX + FLOW SCAN - Fri Nov 13, 02:20 PM ET
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
Last 1m check 14:20:08 ET, last candle SPY 14:19, QQQ 14:19 | no errors
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
| 1 | **GOOGL** | 295.32 | PINNED between the walls (positive gamma) - chop | **-** | 38 | - | POS +$195.1M | 291.28 | 295 | 295 | +$20.2M | +$308k bull / +$0 bear | out (clean 31, ADX 12, RVol 0.6) |
| 2 | **TSLA** | 391.93 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 36 | none: 124 puts 0-7DTE > 5 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only +9% at the target (needs +20%) (47 contracts' greeks worked out here) | POS +$420.8M | 381.97 | 392.5 | 390 | +$36.1M | +$59k bull / -$1.6M bear | out (clean 28, ADX 13, RVol 0.8) |
| 3 | **ARM** | 190.83 | FLOW SURGE | **PUTS** | 33 | none: 30 puts 0-7DTE > 1 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only -45% at the target (needs +20%) (24 contracts' greeks worked out here) | NEG -$3.1M | 192.09 | 190 | 190 | -$4.2M | +$0 bull / -$55k bear | out (clean 33, ADX 19, RVol 0.1) |
| 4 | **ORCL** | 125.60 | FLIP CROSS down into negative gamma | **PUTS** | 30 | 11/13 126P @ 0.78 (delta 0.62) = est +24% at 125 | NEG -$1.5M | 125.68 | 125 | 125 | -$2.0M | +$0 bull / -$353k bear | out (clean 31, ADX 23, RVol 0.3) |
| 5 | **MU** | 771.68 | FLIP CROSS down into negative gamma | **PUTS** | 29 | none: 160 puts 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (69 contracts' greeks worked out here) | NEG -$46.0M | 784.29 | 770 | 770 | +$56.8M | +$0 bull / -$4.2M bear | out (clean 30, ADX 20, RVol 0.4) |
| 6 | **AVGO** | 347.14 | - | **-** | 20 | - | POS +$94.1M | 338.9 | 350 | 350 | +$16.0M | +$0 bull / -$73k bear | out (clean 36, ADX 16, RVol 0.3) |
| 7 | **QQQ** | 680.15 | - | **-** | 19 | - | NEG -$3.4B | 690.47 | 680 | 680 | +$194.9M | +$516k bull / -$3.7M bear | out (clean 32, ADX 22, RVol 0.6) |
| 8 | **SPY** | 753.65 | - | **-** | 18 | - | NEG -$8.6B | 760.45 | 775 | 755 | +$184.7M | +$1.9M bull / -$10.5M bear | out (clean 33, ADX 23, RVol 0.5) |
| 9 | **SMH** | 486.82 | - | **-** | 18 | - | NEG -$277.4M | - | 500 | 475 | +$6.5M | +$0 bull / -$676k bear | out (clean 31, ADX 23, RVol 0.6) |
| 10 | **NVDA** | 162.80 | - | **-** | 18 | - | NEG -$321.8M | - | 175 | 165 | +$72.3M | +$1.1M bull / -$4.0M bear | out (clean 31, ADX 20, RVol 0.4) |
| 11 | **AMD** | 534.09 | - | **-** | 18 | - | POS +$44.4M | 522.45 | 530 | 530 | +$39.8M | +$0 bull / -$3.9M bear | out (clean 35, ADX 23, RVol 0.5) |
| 12 | **META** | 642.08 | - | **-** | 18 | - | POS +$166.0M | 637.98 | 650 | 640 | -$3.9M | +$306k bull / -$366k bear | out (clean 30, ADX 33, RVol 0.7) |
| 13 | **AMZN** | 265.92 | - | **-** | 18 | - | POS +$466.4M | 253.17 | 265 | 265 | +$7.8M | +$58k bull / +$0 bear | out (clean 29, ADX 14, RVol 0.2) |
| 14 | **COIN** | 128.99 | - | **-** | 18 | - | NEG -$22.4M | 132.26 | 140 | 130 | +$2.1M | +$0 bull / -$734k bear | out (clean 30, ADX 11, RVol 0.3) |
| 15 | **DELL** | 344.44 | - | **-** | 18 | - | NEG -$5.0M | 348.71 | 350 | 350 | +$3.7M | +$32k bull / -$669k bear | out (clean 38, ADX 23, RVol 0.3) |
| 16 | **SMCI** | 26.93 | - | **-** | 17 | - | NEG -$2.9M | 27.72 | 27 | 27 | -$1.8M | - | out (clean 34, ADX 32, RVol 0.3) |
| 17 | **MSTR** | 112.71 | - | **-** | 17 | - | NEG -$42.9M | - | 120 | 110 | +$281k | +$0 bull / -$61k bear | out (clean 31, ADX 31, RVol 0.8) |
| 18 | **AAPL** | 358.02 | - | **-** | 16 | - | POS +$1.5B | 347.43 | 360 | 350 | +$9.2M | +$118k bull / -$41k bear | out (clean 30, ADX 14, RVol 0.5) |
| 19 | **PLTR** | 169.40 | - | **-** | 15 | - | POS +$99.8M | 165.31 | 170 | 170 | -$810k | +$0 bull / -$41k bear | out (clean 29, ADX 17, RVol 0.3) |
| 20 | **MSFT** | 524.88 | - | **-** | 12 | - | POS +$137.4M | 523 | 535 | 520 | -$743k | +$0 bull / -$167k bear | out (clean 31, ADX 7, RVol 0.4) |
| 21 | **HOOD** | 78.60 | - | **-** | 10 | - | NEG -$17.4M | 80.08 | 82 | 79 | +$2.5M | - | out (clean 35, ADX 15, RVol 0.4) |
| 22 | **UBER** | 69.49 | - | **-** | 10 | - | POS +$13.9M | 69.02 | 70 | 70 | +$258k | - | out (clean 33, ADX 16, RVol 0.3) |
| 23 | **CRM** | 218.04 | - | **-** | 10 | - | NEG -$5.2M | 223.18 | 220 | 220 | +$131k | - | out (clean 27, ADX 23, RVol 0.5) |
| 24 | **IWM** | 277.20 | - | **-** | 9 | - | NEG -$2.6B | 282.7 | 285 | 275 | +$15.9M | - | out (clean 36, ADX 20, RVol 0.3) |
| 25 | **NFLX** | 62.36 | - | **-** | 7 | - | NEG -$45.3M | 63.54 | 65 | 62 | +$412k | - | out (clean 31, ADX 19, RVol 0.8) |
| 26 | **SHOP** | 147.77 | - | **-** | 4 | - | POS +$4.6M | 146.52 | 150 | 150 | -$31k | - | out (clean 31, ADX 10, RVol 0.5) |
| 27 | **BABA** | 94.00 | - | **-** | 3 | - | NEG -$17.3M | - | 100 | 94 | -$41k | - | out (clean 27, ADX 12, RVol 0.3) |

## Big prints this scan (90)
- **SPY** CALL 745 2026-11-16 (3DTE): 1,681 @ 9.04 = **+$1.5M** SELL | vol 74,260 / OI 981
- **SPY** CALL 745 2026-11-16 (3DTE): 1,564 @ 9.14 = **+$1.4M** SELL | vol 74,260 / OI 981
- **SPY** CALL 745 2026-11-16 (3DTE): 1,522 @ 9.29 = **+$1.4M** MID | vol 74,260 / OI 981
- **SPY** CALL 745 2026-11-16 (3DTE): 1,579 @ 8.94 = **+$1.4M** SELL | vol 74,260 / OI 981
- **AMD** CALL 550 2026-11-18 (5DTE): 200 @ 11.50 = **+$230k** SELL | vol 1,646 / OI 143
- **SPY** CALL 745 2026-11-16 (3DTE): 238 @ 9.29 = **+$221k** MID | vol 74,260 / OI 981
- **QQQ** CALL 680 2026-11-20 (7DTE): 199 @ 10.69 = **+$213k** SELL | vol 11,222 / OI 32,370
- **QQQ** CALL 686 2026-11-16 (3DTE): 1,000 @ 1.97 = **+$197k** SELL | vol 6,168 / OI 353
- **SPY** CALL 745 2026-11-16 (3DTE): 211 @ 9.29 = **+$196k** MID | vol 74,260 / OI 981
- **COIN** PUT 130 2026-11-20 (7DTE): 300 @ 5.85 = **+$176k** BUY | vol 1,941 / OI 2,991
- **COIN** PUT 130 2026-11-20 (7DTE): 299 @ 5.85 = **+$175k** BUY | vol 1,941 / OI 2,991
- **QQQ** CALL 680 2026-11-20 (7DTE): 119 @ 10.34 = **+$123k** SELL | vol 11,222 / OI 32,370
- **COIN** PUT 130 2026-11-20 (7DTE): 199 @ 5.85 = **+$116k** BUY | vol 1,941 / OI 2,991
- **COIN** PUT 130 2026-11-20 (7DTE): 199 @ 5.85 = **+$116k** BUY | vol 1,941 / OI 2,991
- **AMD** PUT 525 2026-11-16 (3DTE): 119 @ 9.49 = **+$113k** BUY | vol 3,019 / OI 175

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 756 2026-12-11 (28DTE): 1,002 traded vs OI 1,001
- **QQQ** PUT 623 2026-11-16 (3DTE): 501 traded vs OI 88
- **QQQ** PUT 668 2026-11-20 (7DTE): 753 traded vs OI 697
- **QQQ** PUT 670 2026-11-19 (6DTE): 502 traded vs OI 453
- **QQQ** CALL 682 2026-11-30 (17DTE): 500 traded vs OI 263
- **TSLA** CALL 362.5 2026-11-16 (3DTE): 812 traded vs OI 179
- **TSLA** CALL 367.5 2026-11-16 (3DTE): 758 traded vs OI 105
- **AMD** PUT 587.5 2026-11-20 (7DTE): 831 traded vs OI 0
- **AMD** CALL 535 2026-11-20 (7DTE): 961 traded vs OI 932
- **AMD** CALL 587.5 2026-11-16 (3DTE): 1,180 traded vs OI 47
- **META** CALL 660 2026-11-13 (0DTE): 3,239 traded vs OI 3,198
- **MSFT** CALL 570 2026-11-20 (7DTE): 500 traded vs OI 0
- **GOOGL** PUT 270 2026-11-20 (7DTE): 513 traded vs OI 0
- **AVGO** CALL 345 2026-11-27 (14DTE): 521 traded vs OI 519
- **SMCI** CALL 26 2026-11-20 (7DTE): 789 traded vs OI 768

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
