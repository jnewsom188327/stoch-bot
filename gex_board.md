# GEX + FLOW SCAN - Fri Nov 13, 03:55 PM ET
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
Last 1m check 15:32:08 ET, last candle SPY 15:31, QQQ 15:31 | no errors
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
| 1 | **HOOD** | 78.08 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 41 | none: 30 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (24 contracts' greeks worked out here) | POS +$184k | 78.08 | 78 | 80 | +$2.6M | - | out (clean 34, ADX 18, RVol 2.4) |
| 2 | **TSLA** | 392.49 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 38 | none: 124 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (50 contracts' greeks worked out here) | POS +$1.1B | 391.32 | 392.5 | 390 | +$41.9M | +$8.0M bull / -$1.7M bear | out (clean 28, ADX 11, RVol 1.1) |
| 3 | **AMZN** | 267.15 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 35 | none: 83 puts 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (52 contracts' greeks worked out here) | POS +$664.7M | 255.78 | 267.5 | 265 | +$2.1M | +$0 bull / -$2.7M bear | out (clean 29, ADX 19, RVol 0.9) |
| 4 | **MU** | 783.82 | FLIP CROSS down into negative gamma | **PUTS** | 35 | none: 152 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (59 contracts' greeks worked out here) | NEG -$137.5M | 789.16 | 785 | 780 | +$54.4M | +$0 bull / -$2.5M bear | out (clean 30, ADX 28, RVol 1.1) |
| 5 | **GOOGL** | 296.00 | - | **-** | 25 | - | POS +$57.2M | 295.62 | 297.5 | 295 | +$20.0M | +$0 bull / -$1.1M bear | out (clean 31, ADX 15, RVol 1.2) |
| 6 | **AAPL** | 356.38 | - | **-** | 24 | - | POS +$768.9M | 349.86 | 360 | 355 | +$14.9M | +$491k bull / -$210k bear | out (clean 30, ADX 33, RVol 2.3) |
| 7 | **IWM** | 277.93 | - | **-** | 21 | - | NEG -$2.2B | 282.56 | 278 | 275 | +$17.3M | +$0 bull / -$111k bear | out (clean 36, ADX 18, RVol 1.2) |
| 8 | **AVGO** | 348.00 | - | **-** | 21 | - | POS +$73.4M | 345.23 | 350 | 350 | +$17.6M | +$0 bull / -$183k bear | out (clean 36, ADX 12, RVol 1.1) |
| 9 | **QQQ** | 681.36 | - | **-** | 19 | - | NEG -$4.2B | 690.33 | 700 | 680 | +$220.8M | +$188k bull / -$1.4M bear | out (clean 32, ADX 16, RVol 1.1) |
| 10 | **META** | 641.72 | - | **-** | 19 | - | POS +$280.4M | 634.66 | 645 | 640 | -$1.0M | +$1.0M bull / -$516k bear | out (clean 30, ADX 27, RVol 1.9) |
| 11 | **DELL** | 345.35 | - | **-** | 19 | - | NEG -$14.5M | 358.08 | 345 | 360 | +$4.6M | +$36k bull / -$444k bear | out (clean 38, ADX 12, RVol 1.5) |
| 12 | **BABA** | 94.44 | - | **-** | 19 | - | NEG -$23.2M | - | 100 | 95 | -$415k | +$0 bull / -$51k bear | out (clean 26, ADX 18, RVol 1.0) |
| 13 | **SPY** | 754.59 | - | **-** | 18 | - | NEG -$8.8B | 759.96 | 755 | 755 | +$221.4M | +$0 bull / -$298k bear | out (clean 33, ADX 16, RVol 1.2) |
| 14 | **SMH** | 488.77 | - | **-** | 18 | - | NEG -$267.4M | - | 490 | 490 | +$6.1M | +$0 bull / -$801k bear | out (clean 31, ADX 21, RVol 0.9) |
| 15 | **NVDA** | 163.13 | - | **-** | 18 | - | NEG -$374.0M | - | 175 | 162.5 | +$79.9M | +$1.3M bull / -$3.5M bear | out (clean 31, ADX 17, RVol 0.6) |
| 16 | **AMD** | 536.94 | - | **-** | 18 | - | POS +$1.1M | 536.9 | 540 | 530 | +$48.1M | +$1.7M bull / -$888k bear | out (clean 35, ADX 19, RVol 0.8) |
| 17 | **NFLX** | 62.37 | - | **-** | 18 | - | NEG -$44.7M | 63.35 | 65 | 62 | +$533k | +$132k bull / +$0 bear | out (clean 30, ADX 19, RVol 1.2) |
| 18 | **MSTR** | 112.29 | - | **-** | 18 | - | NEG -$41.2M | - | 120 | 110 | +$2.9M | +$141k bull / -$717k bear | out (clean 32, ADX 24, RVol 1.2) |
| 19 | **ORCL** | 125.57 | - | **-** | 17 | - | NEG -$42.5M | 126.11 | 126 | 125 | -$1.6M | +$105k bull / -$97k bear | out (clean 32, ADX 17, RVol 0.8) |
| 20 | **MSFT** | 525.50 | - | **-** | 14 | - | POS +$102.3M | 524.25 | 535 | 520 | -$303k | +$150k bull / -$40k bear | out (clean 30, ADX 11, RVol 1.1) |
| 21 | **SMCI** | 26.84 | - | **-** | 14 | - | NEG -$2.4M | 27.42 | 27 | 27 | -$1.7M | - | out (clean 34, ADX 22, RVol 0.6) |
| 22 | **CRM** | 217.98 | - | **-** | 14 | - | NEG -$3.3M | 221.77 | 217.5 | 220 | +$201k | - | out (clean 27, ADX 22, RVol 1.9) |
| 23 | **ARM** | 191.92 | - | **-** | 13 | - | NEG -$4.7M | 192.41 | 192.5 | 190 | -$4.0M | - | out (clean 33, ADX 14, RVol 0.6) |
| 24 | **COIN** | 128.66 | - | **-** | 12 | - | NEG -$16.5M | 131.73 | 140 | 130 | +$2.4M | - | out (clean 29, ADX 19, RVol 1.3) |
| 25 | **UBER** | 69.62 | - | **-** | 11 | - | POS +$13.8M | 69.43 | 70 | 70 | +$277k | - | out (clean 32, ADX 15, RVol 1.3) |
| 26 | **PLTR** | 168.60 | - | **-** | 5 | - | POS +$19.3M | 168.36 | 170 | 170 | +$545k | - | out (clean 29, ADX 15, RVol 0.8) |
| 27 | **SHOP** | 147.56 | - | **-** | 5 | - | POS +$4.0M | 146.4 | 147 | 140 | +$50k | - | out (clean 30, ADX 8, RVol 1.2) |

## Big prints this scan (92)
- **NVDA** PUT 160 2026-11-16 (3DTE): 2,000 @ 2.30 = **+$460k** BUY | vol 102,784 / OI 4,240
- **NVDA** PUT 160 2026-11-16 (3DTE): 2,000 @ 2.30 = **+$460k** BUY | vol 102,784 / OI 4,240
- **NVDA** PUT 160 2026-11-16 (3DTE): 1,162 @ 2.30 = **+$267k** BUY | vol 102,784 / OI 4,240
- **QQQ** PUT 679 2026-11-16 (3DTE): 405 @ 4.86 = **+$197k** BUY | vol 18,214 / OI 211
- **AMZN** CALL 267.5 2026-11-20 (7DTE): 400 @ 4.46 = **+$178k** SELL | vol 8,530 / OI 2,672
- **AMZN** CALL 267.5 2026-11-20 (7DTE): 400 @ 4.46 = **+$178k** SELL | vol 8,530 / OI 2,672
- **MU** CALL 745 2026-11-20 (7DTE): 30 @ 50.00 = **+$150k** SELL | vol 146 / OI 181
- **NVDA** PUT 157.5 2026-11-18 (5DTE): 250 @ 5.18 = **+$130k** BUY | vol 5,908 / OI 2,960
- **TSLA** PUT 392.5 2026-11-16 (3DTE): 200 @ 6.35 = **+$127k** BUY | vol 4,471 / OI 267
- **QQQ** CALL 675 2026-11-13 (0DTE): 300 @ 4.00 = **+$120k** SELL | vol 156,605 / OI 5,568
- **NVDA** CALL 155 2026-11-20 (7DTE): 100 @ 11.80 = **+$118k** SELL | vol 2,540 / OI 2,970
- **NVDA** PUT 157.5 2026-11-18 (5DTE): 220 @ 5.20 = **+$114k** BUY | vol 5,908 / OI 2,960
- **TSLA** PUT 392.5 2026-11-16 (3DTE): 184 @ 6.05 = **+$111k** BUY | vol 4,471 / OI 267
- **IWM** CALL 283 2026-11-20 (7DTE): 1,764 @ 0.63 = **+$111k** SELL | vol 4,031 / OI 14,376
- **QQQ** PUT 678 2026-11-16 (3DTE): 242 @ 4.50 = **+$109k** BUY | vol 12,011 / OI 225

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 786 2026-11-18 (5DTE): 928 traded vs OI 306
- **SPY** CALL 753 2026-11-19 (6DTE): 506 traded vs OI 97
- **SPY** CALL 787 2026-11-18 (5DTE): 729 traded vs OI 20
- **SPY** CALL 830 2026-11-20 (7DTE): 3,249 traded vs OI 0
- **SPY** CALL 830 2026-11-23 (10DTE): 3,606 traded vs OI 0
- **SPY** CALL 830 2026-11-24 (11DTE): 5,650 traded vs OI 0
- **SPY** CALL 830 2026-11-25 (12DTE): 4,600 traded vs OI 0
- **SPY** CALL 830 2026-12-04 (21DTE): 518 traded vs OI 0
- **QQQ** PUT 678 2026-11-18 (5DTE): 599 traded vs OI 349
- **QQQ** CALL 749 2026-11-20 (7DTE): 947 traded vs OI 0
- **IWM** CALL 280 2026-11-17 (4DTE): 539 traded vs OI 293
- **SMH** CALL 537.5 2026-11-20 (7DTE): 1,270 traded vs OI 0
- **NVDA** PUT 157.5 2026-11-23 (10DTE): 1,155 traded vs OI 941
- **NVDA** PUT 155 2026-11-23 (10DTE): 505 traded vs OI 235
- **AMD** CALL 590 2026-11-20 (7DTE): 1,578 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
