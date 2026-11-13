# GEX + FLOW SCAN - Fri Nov 13, 12:50 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (13)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 12:45 | **HOOD** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/13 78C | 0.58 | 0.56 | +12% (3m) | **-3%** | +75% | 79 |
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
Last 1m check 12:50:08 ET, last candle SPY 12:49, QQQ 12:49 | no errors
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
| 1 | **HOOD** | 78.31 | RUN: clean trend + negative gamma + flow agrees | **CALLS** | 52 | 11/13 78C @ 0.58 (delta 0.63) = est +68% at 79 | NEG -$14.6M | 80.2 | 78 | 80 | +$2.5M | - | LONG (clean 36, ADX 27, RVol 1.1) |
| 2 | **TSLA** | 390.69 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 35 | none: 124 calls 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (56 contracts' greeks worked out here) | POS +$368.9M | - | 400 | 390 | +$45.9M | +$2.0M bull / -$3.1M bear | out (clean 28, ADX 12, RVol 0.5) |
| 3 | **GOOGL** | 295.44 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 33 | none: 90 puts 0-7DTE > 7 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only -12% at the target (needs +20%) (35 contracts' greeks worked out here) | POS +$204.0M | 290.13 | 295 | 290 | +$19.2M | - | out (clean 31, ADX 17, RVol 0.4) |
| 4 | **AVGO** | 345.35 | FLOW SURGE | **CALLS** | 31 | none: 108 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (50 contracts' greeks worked out here) | POS +$70.8M | 338.18 | 350 | 340 | +$19.6M | +$65k bull / +$0 bear | out (clean 36, ADX 27, RVol 0.3) |
| 5 | **MU** | 764.70 | FLIP CROSS up into positive gamma | **CALLS** | 31 | none: 164 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (76 contracts' greeks worked out here) | NEG -$50.2M | 750.85 | 760 | 750 | +$67.4M | +$328k bull / -$2.8M bear | out (clean 30, ADX 21, RVol 0.5) |
| 6 | **ARM** | 188.25 | - | **-** | 27 | - | NEG -$1.6M | 189.8 | 190 | 190 | -$3.4M | +$27k bull / +$0 bear | out (clean 33, ADX 31, RVol 0.5) |
| 7 | **DELL** | 339.85 | - | **-** | 25 | - | NEG -$10.4M | - | 350 | 340 | +$6.9M | +$0 bull / -$686k bear | out (clean 38, ADX 32, RVol 0.9) |
| 8 | **AMD** | 523.59 | - | **-** | 23 | - | POS +$32.4M | - | 530 | 530 | +$70.0M | +$1.9M bull / -$620k bear | out (clean 35, ADX 33, RVol 0.7) |
| 9 | **SMH** | 482.17 | - | **-** | 22 | - | NEG -$345.0M | - | 500 | 475 | +$10.2M | +$32k bull / -$192k bear | out (clean 31, ADX 28, RVol 0.5) |
| 10 | **QQQ** | 677.30 | - | **-** | 21 | - | NEG -$3.2B | 690.67 | 680 | 680 | +$259.7M | +$216k bull / -$469k bear | out (clean 32, ADX 27, RVol 0.5) |
| 11 | **NVDA** | 161.00 | - | **-** | 20 | - | NEG -$308.9M | - | 175 | 160 | +$109.9M | +$2.5M bull / -$1.1M bear | out (clean 31, ADX 11, RVol 0.5) |
| 12 | **NFLX** | 62.38 | - | **-** | 20 | - | NEG -$39.7M | 63.44 | 65 | 62 | +$505k | +$0 bull / -$26k bear | out (clean 32, ADX 32, RVol 0.7) |
| 13 | **SPY** | 752.03 | - | **-** | 19 | - | NEG -$8.4B | 760.66 | 750 | 750 | +$234.5M | +$0 bull / -$7.5M bear | out (clean 33, ADX 21, RVol 0.5) |
| 14 | **AAPL** | 357.97 | - | **-** | 17 | - | POS +$1.3B | 349.13 | 360 | 360 | +$11.6M | +$124k bull / -$120k bear | out (clean 30, ADX 13, RVol 0.5) |
| 15 | **META** | 637.20 | - | **-** | 17 | - | POS +$76.8M | 633.5 | 650 | 635 | +$3.0M | +$0 bull / -$47k bear | out (clean 29, ADX 25, RVol 0.6) |
| 16 | **COIN** | 128.90 | - | **-** | 15 | - | NEG -$20.7M | 132.58 | 140 | 130 | +$3.2M | - | out (clean 31, ADX 21, RVol 0.2) |
| 17 | **MSTR** | 110.63 | - | **-** | 15 | - | NEG -$48.0M | - | 110 | 110 | +$428k | +$0 bull / -$56k bear | out (clean 30, ADX 20, RVol 0.7) |
| 18 | **PLTR** | 168.02 | - | **-** | 14 | - | POS +$116.0M | 159.73 | 167.5 | 170 | -$497k | +$0 bull / -$51k bear | out (clean 29, ADX 16, RVol 0.2) |
| 19 | **AMZN** | 265.77 | - | **-** | 12 | - | POS +$426.1M | 253.63 | 265 | 265 | +$8.1M | - | out (clean 30, ADX 23, RVol 0.3) |
| 20 | **MSFT** | 524.20 | - | **-** | 12 | - | POS +$123.6M | 522.06 | 535 | 520 | -$205k | +$55k bull / -$96k bear | out (clean 31, ADX 10, RVol 0.2) |
| 21 | **UBER** | 69.45 | - | **-** | 12 | - | POS +$13.4M | 68.9 | 70 | 70 | +$309k | - | out (clean 32, ADX 12, RVol 0.3) |
| 22 | **IWM** | 276.83 | - | **-** | 11 | - | NEG -$2.6B | 282.9 | 285 | 275 | +$18.7M | - | out (clean 36, ADX 21, RVol 0.3) |
| 23 | **CRM** | 218.00 | - | **-** | 11 | - | NEG -$6.3M | 221.68 | 220 | 220 | +$111k | - | out (clean 28, ADX 25, RVol 0.7) |
| 24 | **SMCI** | 26.54 | - | **-** | 7 | - | NEG -$2.7M | 27.8 | 27 | 27 | +$125k | - | out (clean 34, ADX 22, RVol 0.5) |
| 25 | **ORCL** | 124.45 | - | **-** | 6 | - | POS +$2.4M | 123.82 | 125 | 125 | -$1.1M | - | out (clean 31, ADX 17, RVol 0.3) |
| 26 | **SHOP** | 147.16 | - | **-** | 4 | - | POS +$3.5M | 145.72 | 150 | 140 | +$11k | - | out (clean 31, ADX 14, RVol 0.3) |
| 27 | **BABA** | 94.16 | - | **-** | 4 | - | NEG -$18.6M | - | 100 | 95 | -$25k | - | out (clean 27, ADX 17, RVol 0.3) |

## Big prints this scan (96)
- **TSLA** CALL 375 2026-11-16 (3DTE): 500 @ 16.77 = **+$838k** SELL | vol 1,087 / OI 241
- **TSLA** CALL 375 2026-11-16 (3DTE): 500 @ 16.65 = **+$832k** SELL | vol 1,087 / OI 241
- **TSLA** CALL 380 2026-11-16 (3DTE): 500 @ 12.57 = **+$628k** SELL | vol 2,175 / OI 697
- **TSLA** CALL 380 2026-11-16 (3DTE): 500 @ 12.25 = **+$612k** SELL | vol 2,175 / OI 697
- **SPY** CALL 755 2026-11-20 (7DTE): 1,000 @ 5.47 = **+$547k** SELL | vol 6,215 / OI 15,917
- **MU** CALL 750 2026-11-20 (7DTE): 114 @ 42.10 = **+$480k** SELL | vol 868 / OI 2,179
- **SPY** CALL 745 2026-11-16 (3DTE): 500 @ 8.26 = **+$413k** SELL | vol 25,385 / OI 981
- **AAPL** CALL 365 2026-11-18 (5DTE): 4,040 @ 0.85 = **+$343k** MID | vol 8,628 / OI 348
- **SPY** CALL 745 2026-11-16 (3DTE): 400 @ 8.26 = **+$330k** SELL | vol 25,385 / OI 981
- **SPY** CALL 745 2026-11-16 (3DTE): 400 @ 8.26 = **+$330k** SELL | vol 25,385 / OI 981
- **MU** CALL 770 2026-11-20 (7DTE): 82 @ 31.05 = **+$255k** SELL | vol 1,116 / OI 1,190
- **SPY** CALL 745 2026-11-16 (3DTE): 240 @ 8.26 = **+$198k** SELL | vol 25,385 / OI 981
- **SPY** CALL 745 2026-11-16 (3DTE): 240 @ 8.26 = **+$198k** SELL | vol 25,385 / OI 981
- **MU** CALL 760 2026-11-13 (0DTE): 250 @ 7.10 = **+$178k** SELL | vol 17,588 / OI 1,855
- **SPY** CALL 745 2026-11-16 (3DTE): 200 @ 8.26 = **+$165k** SELL | vol 25,385 / OI 981

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 748 2026-11-19 (6DTE): 517 traded vs OI 161
- **QQQ** CALL 712 2026-11-16 (3DTE): 641 traded vs OI 258
- **QQQ** PUT 660 2026-11-25 (12DTE): 508 traded vs OI 209
- **TSLA** CALL 382.5 2026-11-13 (0DTE): 1,123 traded vs OI 1,122
- **TSLA** PUT 352.5 2026-11-13 (0DTE): 670 traded vs OI 0
- **TSLA** CALL 370 2026-12-04 (21DTE): 669 traded vs OI 496
- **AAPL** PUT 360 2026-11-20 (7DTE): 3,898 traded vs OI 3,893
- **META** CALL 700 2026-11-20 (7DTE): 3,826 traded vs OI 0
- **AVGO** PUT 312.5 2026-11-20 (7DTE): 944 traded vs OI 0
- **AVGO** PUT 327.5 2026-11-16 (3DTE): 932 traded vs OI 90
- **DELL** PUT 332.5 2026-11-13 (0DTE): 509 traded vs OI 225
- **MU** PUT 700 2026-11-27 (14DTE): 502 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
