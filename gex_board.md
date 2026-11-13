# GEX + FLOW SCAN - Fri Nov 13, 11:30 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (12)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:30 | **GOOGL** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/13 292.5P | 0.56 | 0.51 | -9% (0m) | **-9%** | +237% | 290.96 |
| 11:15 | **ARM** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/13 180P | 0.79 | 0.23 | +0% (2m) | **-71%** | +122% | 180 |
| 11:14 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/13 667P | 0.70 | 0.52 | +59% (9m) | **-26%** | +21% | 672.05 hit |
| 10:36 | **SPY** | **PUTS** | 1m FAILED POP (R3 R4) | 11/13 743P | 0.61 | 0.27 | +13% (1m) | **-56%** | +46% | 747.53 |
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
Last 1m check 11:30:08 ET, last candle SPY 11:29, QQQ 11:29 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 11:13 | QQQ | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | **FIRE** QQQ261113P00667000 |
| 11:02 | QQQ | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |
| 10:35 | SPY | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | **FIRE** SPY261113P00743000 |
| 10:16 | QQQ | 1m WHIPSAW | R1 R2 | CALLS | TURNING your way | **FIRE** QQQ261113C00683000 |

## Flow surges NOT fired - price disagreed (40 today, last 5)
- 11:25 HOOD CALLS: price -0.54 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 11:20 HOOD CALLS: price -0.21 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 11:15 HOOD CALLS: price -0.56 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 11:15 COIN CALLS: price -1.07 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 11:10 COIN CALLS: under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **GOOGL** | 294.60 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 52 | 11/13 292.5P @ 0.56 (delta 0.26) = est +237% at 290.96 | POS +$166.9M | 290.96 | 295 | 290 | +$20.1M | +$93k bull / -$28k bear | out (clean 32, ADX 31, RVol 1.0) |
| 2 | **HOOD** | 77.39 | FLOW SURGE | **CALLS** | 49 | none: 32 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (28 contracts' greeks worked out here) | NEG -$14.1M | 80.38 | 85 | 80 | +$3.3M | +$460k bull / +$0 bear | out (clean 36, ADX 58, RVol 1.7) |
| 3 | **AMZN** | 264.97 | PINNED between the walls (positive gamma) - chop | **-** | 42 | - | POS +$378.1M | 255.35 | 265 | 265 | +$8.7M | +$268k bull / +$0 bear | out (clean 30, ADX 34, RVol 0.8) |
| 4 | **TSLA** | 390.92 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 40 | 11/13 395C @ 0.71 (delta 0.22) = est +601% at 400 | POS +$351.7M | 382.98 | 400 | 390 | +$53.6M | +$2.5M bull / -$1.2M bear | out (clean 30, ADX 17, RVol 0.8) |
| 5 | **AVGO** | 342.10 | FLOW SURGE | **CALLS** | 40 | none: 108 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (47 contracts' greeks worked out here) | POS +$63.5M | - | 340 | 340 | +$22.1M | +$160k bull / -$58k bear | out (clean 36, ADX 49, RVol 0.6) |
| 6 | **DELL** | 334.90 | - | **-** | 35 | - | NEG -$8.0M | - | 350 | 340 | +$9.2M | +$26k bull / -$81k bear | out (clean 38, ADX 51, RVol 1.4) |
| 7 | **META** | 632.50 | FLIP CROSS up into positive gamma | **CALLS** | 32 | none: 189 calls 0-7DTE > 8 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (83 contracts' greeks worked out here) | POS +$7.8M | 631.96 | 630 | 625 | +$7.0M | +$127k bull / -$173k bear | out (clean 29, ADX 26, RVol 0.8) |
| 8 | **SHOP** | 145.99 | FLIP CROSS up into positive gamma | **CALLS** | 32 | none: 42 calls 0-7DTE > 3 priced 0.40-0.80 > 2 delta 0.2+ > 0 spread ok > 0 liquid (35 contracts' greeks worked out here) | POS +$1.9M | 145.1 | 150 | 140 | +$78k | +$62k bull / +$0 bear | out (clean 32, ADX 23, RVol 0.7) |
| 9 | **SMH** | 479.17 | - | **-** | 29 | - | NEG -$354.3M | - | 500 | 475 | +$11.9M | +$124k bull / -$323k bear | out (clean 31, ADX 55, RVol 1.3) |
| 10 | **QQQ** | 675.44 | - | **-** | 27 | - | NEG -$3.1B | 690.39 | 680 | 680 | +$290.2M | +$1.6M bull / -$2.6M bear | out (clean 32, ADX 54, RVol 0.6) |
| 11 | **AMD** | 526.68 | - | **-** | 27 | - | POS +$36.3M | - | 550 | 530 | +$72.2M | +$3.4M bull / -$834k bear | out (clean 35, ADX 51, RVol 0.8) |
| 12 | **IWM** | 276.65 | - | **-** | 26 | - | NEG -$2.6B | 283.03 | 285 | 275 | +$19.5M | +$0 bull / -$69k bear | out (clean 37, ADX 36, RVol 0.7) |
| 13 | **NVDA** | 160.28 | - | **-** | 24 | - | NEG -$302.0M | - | 175 | 160 | +$105.2M | +$438k bull / -$6.2M bear | out (clean 31, ADX 22, RVol 0.8) |
| 14 | **COIN** | 127.17 | - | **-** | 24 | - | NEG -$21.1M | 132.91 | 137 | 130 | +$3.5M | - | out (clean 31, ADX 41, RVol 1.5) |
| 15 | **MU** | 759.24 | - | **-** | 24 | - | NEG -$32.1M | 772.78 | 760 | 750 | +$72.6M | +$1.6M bull / -$2.1M bear | out (clean 31, ADX 38, RVol 0.5) |
| 16 | **MSTR** | 109.97 | - | **-** | 24 | - | NEG -$43.5M | - | 110 | 110 | +$6.1M | +$31k bull / +$0 bear | out (clean 31, ADX 32, RVol 0.6) |
| 17 | **SPY** | 750.83 | - | **-** | 23 | - | NEG -$8.9B | 760.64 | 750 | 750 | +$237.3M | +$2.1M bull / -$2.4M bear | out (clean 33, ADX 32, RVol 0.6) |
| 18 | **NFLX** | 62.40 | - | **-** | 22 | - | NEG -$36.9M | 63.55 | 65 | 62 | +$536k | +$68k bull / +$0 bear | out (clean 32, ADX 35, RVol 0.9) |
| 19 | **AAPL** | 358.50 | - | **-** | 20 | - | POS +$1.2B | 349.2 | 360 | 360 | +$12.0M | +$303k bull / -$26k bear | out (clean 30, ADX 21, RVol 0.9) |
| 20 | **ORCL** | 122.95 | - | **-** | 19 | - | POS +$5.5M | 121.72 | 125 | 125 | -$472k | +$134k bull / +$0 bear | out (clean 31, ADX 37, RVol 0.4) |
| 21 | **PLTR** | 167.66 | - | **-** | 18 | - | POS +$78.6M | 162.78 | 170 | 165 | -$62k | +$241k bull / -$77k bear | out (clean 29, ADX 37, RVol 0.6) |
| 22 | **SMCI** | 26.18 | - | **-** | 17 | - | NEG -$2.8M | - | 27 | 25 | +$386k | - | out (clean 34, ADX 28, RVol 0.6) |
| 23 | **MSFT** | 523.12 | - | **-** | 16 | - | POS +$66.5M | 521.65 | 535 | 520 | -$59k | +$66k bull / +$0 bear | out (clean 31, ADX 23, RVol 0.7) |
| 24 | **UBER** | 69.51 | - | **-** | 16 | - | POS +$11.8M | 68.98 | 70 | 70 | +$294k | - | out (clean 33, ADX 14, RVol 0.6) |
| 25 | **CRM** | 217.15 | - | **-** | 15 | - | NEG -$7.7M | 221.84 | 220 | 220 | +$131k | - | out (clean 28, ADX 19, RVol 0.8) |
| 26 | **ARM** | 186.41 | - | **-** | 12 | - | NEG -$1.6M | 188.58 | 185 | 190 | -$313k | - | out (clean 33, ADX 58, RVol 0.9) |
| 27 | **BABA** | 94.09 | - | **-** | 5 | - | NEG -$20.2M | - | 100 | 95 | -$18k | - | out (clean 28, ADX 23, RVol 0.3) |

## Big prints this scan (139)
- **QQQ** CALL 675 2026-11-13 (0DTE): 2,490 @ 2.46 = **+$613k** BUY | vol 70,975 / OI 5,568
- **QQQ** CALL 676 2026-11-13 (0DTE): 2,490 @ 1.97 = **+$491k** MID | vol 50,289 / OI 1,099
- **QQQ** PUT 680 2026-11-20 (7DTE): 340 @ 13.97 = **+$475k** BUY | vol 7,960 / OI 87,076
- **HOOD** CALL 79 2026-11-20 (7DTE): 2,000 @ 2.30 = **+$460k** BUY | vol 5,439 / OI 188
- **AMD** CALL 550 2026-11-20 (7DTE): 230 @ 15.84 = **+$364k** BUY | vol 2,793 / OI 5,879
- **AMD** CALL 550 2026-11-20 (7DTE): 207 @ 15.79 = **+$327k** BUY | vol 2,793 / OI 5,879
- **SPY** CALL 755 2026-11-20 (7DTE): 499 @ 5.31 = **+$265k** BUY | vol 3,211 / OI 15,917
- **AMD** CALL 530 2026-11-20 (7DTE): 100 @ 23.70 = **+$237k** BUY | vol 1,174 / OI 2,460
- **AMD** CALL 530 2026-11-18 (5DTE): 102 @ 19.00 = **+$194k** BUY | vol 353 / OI 56
- **QQQ** CALL 674 2026-11-13 (0DTE): 612 @ 3.02 = **+$185k** SELL | vol 38,365 / OI 807
- **QQQ** PUT 674 2026-11-13 (0DTE): 750 @ 2.42 = **+$182k** BUY | vol 91,839 / OI 1,251
- **TSLA** CALL 375 2026-11-13 (0DTE): 115 @ 15.35 = **+$177k** MID | vol 2,928 / OI 4,860
- **SPY** CALL 751 2026-11-13 (0DTE): 970 @ 1.78 = **+$173k** BUY | vol 99,454 / OI 2,050
- **NVDA** PUT 162.5 2026-11-20 (7DTE): 160 @ 9.80 = **+$157k** BUY | vol 3,849 / OI 505
- **NVDA** PUT 162.5 2026-11-20 (7DTE): 159 @ 9.80 = **+$156k** BUY | vol 3,849 / OI 505

## New unusual volume (traded more than open interest, 500+)
- **QQQ** CALL 698 2026-11-20 (7DTE): 12,290 traded vs OI 10,139
- **QQQ** CALL 703 2026-11-20 (7DTE): 7,158 traded vs OI 1,514
- **QQQ** CALL 687 2026-12-11 (28DTE): 604 traded vs OI 48
- **IWM** CALL 289 2026-11-19 (6DTE): 760 traded vs OI 119
- **IWM** PUT 272 2026-11-24 (11DTE): 630 traded vs OI 35
- **NVDA** CALL 175 2026-11-20 (7DTE): 19,693 traded vs OI 19,509
- **TSLA** CALL 430 2026-11-16 (3DTE): 1,625 traded vs OI 898
- **TSLA** CALL 430 2026-11-18 (5DTE): 2,523 traded vs OI 415
- **META** CALL 695 2026-11-20 (7DTE): 714 traded vs OI 0
- **AMZN** PUT 275 2026-11-16 (3DTE): 551 traded vs OI 146
- **AMZN** PUT 260 2026-11-16 (3DTE): 857 traded vs OI 837
- **GOOGL** CALL 310 2026-11-20 (7DTE): 7,793 traded vs OI 7,746
- **AVGO** PUT 320 2026-11-13 (0DTE): 514 traded vs OI 0
- **DELL** CALL 340 2026-11-13 (0DTE): 666 traded vs OI 212
- **DELL** CALL 342.5 2026-11-13 (0DTE): 504 traded vs OI 108

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
