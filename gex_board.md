# GEX + FLOW SCAN - Fri Nov 13, 11:00 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (9)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:36 | **SPY** | **PUTS** | 1m FAILED POP (R3 R4) | 11/13 743P | 0.61 | 0.32 | +13% (1m) | **-48%** | +46% | 747.53 |
| 10:17 | **QQQ** | **CALLS** | 1m WHIPSAW (R1 R2) | 11/13 683C | 0.75 | 0.32 | -1% (0m) | **-57%** | +60% | 678.58 |
| 10:15 | **ARM** | **PUTS** | FLIP CROSS down into negative gamma | 11/13 182.5P | 0.74 | 1.19 | +143% (21m) | **+61%** | +96% | 183.6 |
| 10:15 | **ORCL** | **CALLS** | FLIP CROSS up into positive gamma | 11/13 124C | 0.65 | 0.76 | +89% (28m) | **+17%** | +66% | 123.68 hit |
| 10:10 | **ORCL** | **PUTS** | FLIP CROSS down into negative gamma | 11/13 120P | 0.46 | 0.11 | +7% (5m) | **-76%** | +63% | 121.25 |
| 10:05 | **GOOGL** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/13 297.5P | 0.74 | 3.03 | +396% (33m) | **+309%** | +288% | 295 hit |
| 09:55 | **BABA** | **PUTS** | FLOW SURGE | 11/13 94P | 0.51 | 0.43 | +8% (43m) | **-16%** (done) | +49% | 93.36 |
| 09:45 | **UBER** | **CALLS** | TREND + FLOW | 11/13 70C | 0.59 | 0.06 | +0% (1m) | **-90%** (done) | +32% | 70.7 |
| 09:45 | **ORCL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/13 127C | 0.46 | 0.22 | +22% (2m) | **-52%** (done) | +48% | 126.38 |

## 1m RULES on SPY / QQQ - loose (2 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 11:00:08 ET, last candle SPY 10:59, QQQ 10:59 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 10:35 | SPY | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | **FIRE** SPY261113P00743000 |
| 10:16 | QQQ | 1m WHIPSAW | R1 R2 | CALLS | TURNING your way | **FIRE** QQQ261113C00683000 |

## Flow surges NOT fired - price disagreed (40 today, last 5)
- 10:55 GOOGL CALLS: under EMA 20 - flow says one way, price says the other
- 10:50 GOOGL CALLS: price -0.27 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:45 HOOD CALLS: price -0.17 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:45 COIN CALLS: price -0.49 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:45 GOOGL CALLS: price -1.57 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **AMD** | 531.05 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 58 | none: 167 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (78 contracts' greeks worked out here) | POS +$58.7M | - | 550 | 530 | +$65.4M | +$1.3M bull / -$3.0M bear | SHORT (clean 35, ADX 51, RVol 0.7) |
| 2 | **ARM** | 185.12 | RUN: clean trend + negative gamma + flow agrees | **PUTS** | 50 | none: 30 puts 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (27 contracts' greeks worked out here) | NEG -$3.2M | 190.72 | 185 | 190 | -$187k | - | SHORT (clean 33, ADX 59, RVol 1.1) |
| 3 | **HOOD** | 77.67 | TREND (flow not with it) | **PUTS** | 49 | 11/13 77P @ 0.45 (delta 0.35) = est +108% at 76.38 | NEG -$14.6M | 80.15 | 80 | 80 | +$2.6M | - | SHORT (clean 36, ADX 61, RVol 2.2) |
| 4 | **AVGO** | 340.91 | FLOW SURGE | **CALLS** | 46 | none: 112 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (48 contracts' greeks worked out here) | POS +$56.6M | - | 340 | 340 | +$22.0M | +$793k bull / -$288k bear | SHORT (clean 36, ADX 49, RVol 0.8) |
| 5 | **TSLA** | 389.82 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 43 | none: 124 calls 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (57 contracts' greeks worked out here) | POS +$348.6M | - | 400 | 390 | +$50.6M | +$28k bull / -$2.2M bear | out (clean 29, ADX 19, RVol 1.0) |
| 6 | **AMZN** | 265.48 | PINNED between the walls (positive gamma) - chop | **-** | 42 | - | POS +$416.8M | 253.41 | 265 | 265 | +$7.7M | +$75k bull / +$0 bear | out (clean 30, ADX 36, RVol 0.7) |
| 7 | **DELL** | 342.19 | TREND (flow not with it) | **PUTS** | 41 | none: 54 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (53 contracts' greeks worked out here) | NEG -$8.6M | - | 350 | 340 | +$7.8M | - | SHORT (clean 38, ADX 48, RVol 0.8) |
| 8 | **SPY** | 750.75 | TREND (flow not with it) | **PUTS** | 40 | none: 664 puts 0-7DTE > 55 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (228 contracts' greeks worked out here) | NEG -$8.7B | 760.55 | 750 | 750 | +$238.1M | +$491k bull / -$2.9M bear | SHORT (clean 33, ADX 35, RVol 0.8) |
| 9 | **ORCL** | 123.63 | FLIP CROSS down into negative gamma | **PUTS** | 39 | 11/13 122P @ 0.50 (delta 0.28) = est +110% at 121.72 | NEG -$2.6M | 123.97 | 125 | 125 | -$1.1M | +$216k bull / -$155k bear | out (clean 31, ADX 35, RVol 1.4) |
| 10 | **IWM** | 275.71 | TREND (flow not with it) | **PUTS** | 36 | 11/16 272P @ 0.58 (delta 0.21) = est +24% at 275 | NEG -$2.8B | 283.23 | 285 | 275 | +$20.4M | +$829k bull / -$408k bear | SHORT (clean 36, ADX 47, RVol 0.8) |
| 11 | **COIN** | 127.90 | - | **-** | 36 | - | NEG -$20.2M | 132.94 | 140 | 130 | +$3.2M | +$0 bull / -$48k bear | out (clean 32, ADX 46, RVol 2.0) |
| 12 | **SMH** | 477.86 | - | **-** | 30 | - | NEG -$345.4M | - | 500 | 475 | +$11.9M | +$208k bull / -$605k bear | out (clean 31, ADX 55, RVol 1.1) |
| 13 | **QQQ** | 675.11 | - | **-** | 29 | - | NEG -$3.1B | 690.55 | 680 | 680 | +$304.9M | +$137k bull / -$2.1M bear | out (clean 32, ADX 57, RVol 0.7) |
| 14 | **NVDA** | 159.92 | - | **-** | 26 | - | NEG -$293.0M | - | 175 | 160 | +$120.3M | +$2.4M bull / -$2.6M bear | out (clean 31, ADX 19, RVol 0.9) |
| 15 | **MU** | 761.88 | - | **-** | 26 | - | NEG -$33.0M | 775.48 | 800 | 750 | +$72.5M | +$2.5M bull / -$4.9M bear | out (clean 31, ADX 37, RVol 1.3) |
| 16 | **MSTR** | 110.24 | - | **-** | 25 | - | NEG -$43.6M | - | 110 | 110 | +$4.1M | +$0 bull / -$227k bear | out (clean 31, ADX 39, RVol 1.1) |
| 17 | **GOOGL** | 294.86 | - | **-** | 24 | - | POS +$164.3M | 290.76 | 300 | 290 | +$19.6M | - | out (clean 31, ADX 33, RVol 1.3) |
| 18 | **AAPL** | 358.77 | - | **-** | 21 | - | POS +$1.3B | 348.53 | 360 | 360 | +$8.5M | +$85k bull / -$233k bear | out (clean 30, ADX 30, RVol 0.8) |
| 19 | **META** | 629.95 | - | **-** | 21 | - | NEG -$20.7M | 630.91 | 630 | 625 | +$9.4M | +$0 bull / -$750k bear | out (clean 29, ADX 27, RVol 1.1) |
| 20 | **MSFT** | 524.75 | - | **-** | 21 | - | POS +$163.5M | 520.94 | 530 | 520 | -$6.0M | +$0 bull / -$1.5M bear | out (clean 32, ADX 30, RVol 0.9) |
| 21 | **PLTR** | 167.81 | - | **-** | 21 | - | POS +$84.2M | 160.98 | 170 | 165 | -$430k | +$0 bull / -$2.6M bear | out (clean 29, ADX 43, RVol 1.0) |
| 22 | **UBER** | 69.40 | - | **-** | 19 | - | POS +$12.4M | 68.85 | 70 | 70 | +$293k | - | out (clean 33, ADX 19, RVol 0.5) |
| 23 | **SMCI** | 26.30 | - | **-** | 18 | - | NEG -$2.5M | - | 27 | 25 | +$341k | - | out (clean 34, ADX 28, RVol 0.8) |
| 24 | **CRM** | 216.29 | - | **-** | 16 | - | NEG -$7.8M | 222.07 | 220 | 220 | +$115k | - | out (clean 28, ADX 18, RVol 0.9) |
| 25 | **SHOP** | 146.94 | - | **-** | 13 | - | POS +$2.8M | 145.48 | 150 | 140 | -$103k | - | out (clean 32, ADX 24, RVol 0.9) |
| 26 | **NFLX** | 62.83 | - | **-** | 10 | - | NEG -$26.2M | 63.54 | 65 | 60 | +$207k | - | out (clean 32, ADX 32, RVol 0.9) |
| 27 | **BABA** | 94.00 | - | **-** | 6 | - | NEG -$18.5M | - | 100 | 95 | -$6k | - | out (clean 28, ADX 26, RVol 0.8) |

## Big prints this scan (140)
- **IWM** PUT 270 2026-11-20 (7DTE): 5,037 @ 1.32 = **+$665k** SELL | vol 18,599 / OI 136,015
- **IWM** PUT 270 2026-11-20 (7DTE): 3,000 @ 1.36 = **+$408k** BUY | vol 18,599 / OI 136,015
- **SPY** PUT 760 2026-11-20 (7DTE): 275 @ 12.59 = **+$346k** BUY | vol 2,616 / OI 18,984
- **QQQ** PUT 680 2026-11-20 (7DTE): 235 @ 14.42 = **+$339k** BUY | vol 7,005 / OI 87,076
- **MU** PUT 750 2026-11-20 (7DTE): 100 @ 30.50 = **+$305k** BUY | vol 2,053 / OI 6,865
- **QQQ** PUT 674 2026-11-13 (0DTE): 800 @ 3.47 = **+$278k** BUY | vol 62,828 / OI 1,251
- **SPY** PUT 755 2026-11-16 (3DTE): 377 @ 6.70 = **+$253k** BUY | vol 12,451 / OI 2,248
- **QQQ** PUT 673 2026-11-13 (0DTE): 900 @ 2.79 = **+$251k** BUY | vol 60,630 / OI 1,102
- **ORCL** CALL 124 2026-11-13 (0DTE): 1,999 @ 1.08 = **+$216k** BUY | vol 5,895 / OI 2,581
- **SPY** PUT 727 2026-11-20 (7DTE): 998 @ 1.99 = **+$199k** BUY | vol 4,471 / OI 7,873
- **QQQ** PUT 677 2026-11-16 (3DTE): 261 @ 7.48 = **+$195k** BUY | vol 5,021 / OI 365
- **QQQ** PUT 677 2026-11-16 (3DTE): 236 @ 7.47 = **+$176k** BUY | vol 5,021 / OI 365
- **TSLA** CALL 375 2026-11-13 (0DTE): 120 @ 14.25 = **+$171k** SELL | vol 2,491 / OI 4,860
- **QQQ** PUT 670 2026-11-16 (3DTE): 384 @ 4.30 = **+$165k** BUY | vol 11,130 / OI 1,115
- **NVDA** PUT 160 2026-11-16 (3DTE): 433 @ 3.15 = **+$136k** SELL | vol 32,123 / OI 4,240

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 747 2026-11-16 (3DTE): 829 traded vs OI 789
- **SPY** CALL 758 2026-11-18 (5DTE): 947 traded vs OI 907
- **SPY** PUT 752 2026-11-18 (5DTE): 544 traded vs OI 541
- **SPY** CALL 748 2026-11-17 (4DTE): 507 traded vs OI 389
- **SPY** CALL 771 2026-11-16 (3DTE): 1,326 traded vs OI 1,313
- **SPY** CALL 802 2026-11-20 (7DTE): 1,621 traded vs OI 1,237
- **QQQ** PUT 655 2026-11-13 (0DTE): 6,987 traded vs OI 6,542
- **QQQ** CALL 667 2026-11-13 (0DTE): 533 traded vs OI 320
- **QQQ** PUT 655 2026-11-18 (5DTE): 501 traded vs OI 319
- **QQQ** PUT 630 2026-11-16 (3DTE): 672 traded vs OI 628
- **QQQ** PUT 653 2026-11-16 (3DTE): 545 traded vs OI 192
- **IWM** CALL 286 2026-11-17 (4DTE): 775 traded vs OI 374
- **IWM** CALL 276 2026-11-16 (3DTE): 560 traded vs OI 203
- **NVDA** CALL 170 2026-12-11 (28DTE): 1,362 traded vs OI 1,349
- **NVDA** PUT 146 2026-11-20 (7DTE): 508 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
