# GEX + FLOW SCAN - Fri Nov 13, 12:45 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (13)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 12:45 | **HOOD** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/13 78C | 0.58 | 0.55 | -5% (0m) | **-5%** | +75% | 79 |
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

## 1m RULES on SPY / QQQ - loose (4 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 12:45:08 ET, last candle SPY 12:44, QQQ 12:44 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
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
| 1 | **HOOD** | 78.08 | RUN: clean trend + negative gamma + flow agrees | **CALLS** | 53 | 11/13 78C @ 0.58 (delta 0.53) = est +75% at 79 | NEG -$14.2M | 79.66 | 78 | 79 | +$2.8M | - | LONG (clean 36, ADX 28, RVol 1.1) |
| 2 | **TSLA** | 390.55 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 36 | none: 124 calls 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (62 contracts' greeks worked out here) | POS +$371.6M | - | 400 | 390 | +$48.8M | +$2.6M bull / +$0 bear | out (clean 28, ADX 12, RVol 0.6) |
| 3 | **META** | 636.25 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 34 | none: 186 calls 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (90 contracts' greeks worked out here) | POS +$59.4M | 633.24 | 650 | 635 | +$3.8M | +$32k bull / -$25k bear | out (clean 29, ADX 24, RVol 0.5) |
| 4 | **GOOGL** | 295.25 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 34 | none: 90 puts 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (44 contracts' greeks worked out here) | POS +$176.0M | 291.11 | 295 | 290 | +$19.3M | - | out (clean 31, ADX 18, RVol 0.4) |
| 5 | **ORCL** | 124.19 | FLIP CROSS up into positive gamma | **CALLS** | 28 | none: 50 calls 0-7DTE > 1 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only +16% at the target (needs +20%) (40 contracts' greeks worked out here) | POS +$267k | 124.06 | 125 | 125 | -$1.1M | +$0 bull / -$31k bear | out (clean 31, ADX 18, RVol 0.3) |
| 6 | **COIN** | 128.36 | - | **-** | 27 | - | NEG -$22.7M | 132.44 | 140 | 130 | +$3.6M | +$0 bull / -$723k bear | out (clean 31, ADX 21, RVol 0.2) |
| 7 | **ARM** | 188.52 | - | **-** | 27 | - | NEG -$1.7M | 190.12 | 190 | 190 | -$3.4M | +$27k bull / +$0 bear | out (clean 33, ADX 32, RVol 0.5) |
| 8 | **AVGO** | 345.34 | - | **-** | 26 | - | POS +$86.9M | - | 350 | 340 | +$19.4M | +$99k bull / -$119k bear | out (clean 36, ADX 28, RVol 0.3) |
| 9 | **DELL** | 340.92 | - | **-** | 26 | - | NEG -$7.8M | 352.79 | 350 | 340 | +$6.7M | +$0 bull / -$686k bear | out (clean 38, ADX 35, RVol 1.0) |
| 10 | **AMD** | 524.46 | - | **-** | 23 | - | POS +$26.6M | 513.2 | 530 | 530 | +$68.5M | +$1.4M bull / -$2.7M bear | out (clean 35, ADX 34, RVol 0.7) |
| 11 | **AMZN** | 265.68 | - | **-** | 22 | - | POS +$396.4M | 254.24 | 265 | 265 | +$8.2M | +$0 bull / -$34k bear | out (clean 30, ADX 23, RVol 0.4) |
| 12 | **QQQ** | 677.42 | - | **-** | 21 | - | NEG -$3.1B | 690.55 | 680 | 680 | +$252.6M | +$1.5M bull / -$1.4M bear | out (clean 32, ADX 28, RVol 0.4) |
| 13 | **IWM** | 276.84 | - | **-** | 21 | - | NEG -$2.6B | 282.94 | 285 | 275 | +$18.8M | +$0 bull / -$53k bear | out (clean 36, ADX 21, RVol 0.3) |
| 14 | **SMH** | 482.25 | - | **-** | 21 | - | NEG -$353.9M | - | 500 | 475 | +$10.2M | +$0 bull / -$495k bear | out (clean 31, ADX 28, RVol 0.3) |
| 15 | **NVDA** | 160.93 | - | **-** | 20 | - | NEG -$306.5M | - | 175 | 160 | +$107.5M | +$1.8M bull / -$4.9M bear | out (clean 31, ADX 12, RVol 0.5) |
| 16 | **NFLX** | 62.41 | - | **-** | 20 | - | NEG -$37.4M | 63.34 | 65 | 62 | +$458k | +$0 bull / -$26k bear | out (clean 32, ADX 33, RVol 0.6) |
| 17 | **SPY** | 752.12 | - | **-** | 19 | - | NEG -$8.2B | 760.99 | 750 | 755 | +$232.4M | +$0 bull / -$8.0M bear | out (clean 33, ADX 20, RVol 0.5) |
| 18 | **MU** | 763.67 | - | **-** | 19 | - | NEG -$18.9M | 773.41 | 760 | 750 | +$65.0M | +$469k bull / -$2.1M bear | out (clean 30, ADX 21, RVol 0.5) |
| 19 | **AAPL** | 358.07 | - | **-** | 18 | - | POS +$1.3B | 349.09 | 360 | 360 | +$12.8M | +$554k bull / -$120k bear | out (clean 30, ADX 13, RVol 0.5) |
| 20 | **MSTR** | 110.69 | - | **-** | 16 | - | NEG -$46.8M | - | 110 | 110 | +$391k | +$0 bull / -$1.3M bear | out (clean 30, ADX 20, RVol 0.9) |
| 21 | **MSFT** | 524.21 | - | **-** | 13 | - | POS +$111.6M | 522.27 | 535 | 520 | -$249k | +$256k bull / +$0 bear | out (clean 31, ADX 11, RVol 0.3) |
| 22 | **UBER** | 69.42 | - | **-** | 12 | - | POS +$13.9M | 68.9 | 70 | 70 | +$308k | - | out (clean 33, ADX 12, RVol 0.3) |
| 23 | **CRM** | 218.09 | - | **-** | 12 | - | NEG -$7.1M | 222.48 | 220 | 220 | +$115k | - | out (clean 28, ADX 24, RVol 0.7) |
| 24 | **SMCI** | 26.57 | - | **-** | 7 | - | NEG -$2.9M | - | 27 | 27 | +$135k | - | out (clean 34, ADX 22, RVol 0.6) |
| 25 | **PLTR** | 168.04 | - | **-** | 4 | - | POS +$99.5M | 161.55 | 170 | 170 | -$545k | - | out (clean 29, ADX 17, RVol 0.2) |
| 26 | **SHOP** | 147.10 | - | **-** | 4 | - | POS +$3.0M | 145.73 | 150 | 140 | +$12k | - | out (clean 31, ADX 14, RVol 0.3) |
| 27 | **BABA** | 94.22 | - | **-** | 4 | - | NEG -$20.9M | - | 100 | 95 | -$22k | - | out (clean 27, ADX 17, RVol 0.3) |

## Big prints this scan (100)
- **SPY** CALL 745 2026-11-16 (3DTE): 1,933 @ 8.25 = **+$1.6M** SELL | vol 23,354 / OI 981
- **SPY** CALL 745 2026-11-16 (3DTE): 1,713 @ 7.93 = **+$1.4M** SELL | vol 23,354 / OI 981
- **DELL** PUT 325 2026-11-20 (7DTE): 500 @ 12.56 = **+$628k** BUY | vol 709 / OI 0
- **NVDA** PUT 160 2026-11-20 (7DTE): 497 @ 7.70 = **+$383k** SELL | vol 19,182 / OI 37,700
- **SPY** CALL 751 2026-11-13 (0DTE): 2,000 @ 1.80 = **+$360k** SELL | vol 219,470 / OI 2,050
- **QQQ** PUT 695 2026-11-18 (5DTE): 167 @ 19.84 = **+$331k** MID | vol 328 / OI 100
- **QQQ** PUT 695 2026-11-16 (3DTE): 167 @ 18.18 = **+$304k** BUY | vol 452 / OI 490
- **TSLA** CALL 400 2026-11-20 (7DTE): 299 @ 7.25 = **+$217k** BUY | vol 11,735 / OI 21,808
- **QQQ** PUT 685 2026-11-18 (5DTE): 167 @ 12.95 = **+$216k** SELL | vol 655 / OI 502
- **MU** CALL 780 2026-11-13 (0DTE): 2,079 @ 0.95 = **+$198k** BUY | vol 30,223 / OI 1,283
- **TSLA** CALL 390 2026-11-16 (3DTE): 295 @ 6.55 = **+$193k** BUY | vol 6,635 / OI 971
- **SPY** CALL 745 2026-11-16 (3DTE): 231 @ 7.93 = **+$183k** SELL | vol 23,354 / OI 981
- **QQQ** PUT 685 2026-11-16 (3DTE): 167 @ 9.89 = **+$165k** BUY | vol 6,330 / OI 1,301
- **SPY** PUT 750 2026-11-20 (7DTE): 238 @ 6.27 = **+$149k** BUY | vol 16,614 / OI 55,813
- **NVDA** PUT 155 2026-11-18 (5DTE): 300 @ 4.84 = **+$145k** SELL | vol 5,016 / OI 1,724

## New unusual volume (traded more than open interest, 500+)
- **QQQ** PUT 685 2026-11-18 (5DTE): 655 traded vs OI 502
- **QQQ** CALL 682 2026-11-20 (7DTE): 502 traded vs OI 439
- **TSLA** CALL 375 2026-11-16 (3DTE): 587 traded vs OI 241
- **TSLA** PUT 360 2026-11-18 (5DTE): 533 traded vs OI 349
- **TSLA** PUT 392.5 2026-11-20 (7DTE): 516 traded vs OI 0
- **AAPL** PUT 340 2026-12-11 (28DTE): 543 traded vs OI 332
- **AMD** CALL 525 2026-11-18 (5DTE): 505 traded vs OI 93
- **AMZN** CALL 262.5 2026-11-13 (0DTE): 1,787 traded vs OI 1,773
- **MSFT** PUT 485 2026-11-16 (3DTE): 682 traded vs OI 31
- **DELL** CALL 375 2026-11-20 (7DTE): 531 traded vs OI 141
- **DELL** PUT 337.5 2026-11-13 (0DTE): 506 traded vs OI 339
- **SMCI** CALL 26.5 2026-11-20 (7DTE): 507 traded vs OI 12
- **BABA** PUT 94 2026-11-13 (0DTE): 622 traded vs OI 617

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
