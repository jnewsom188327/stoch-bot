# GEX + FLOW SCAN - Fri Oct 30, 10:30 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (2)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:25 | **SMCI** | **PUTS** | FLIP CROSS down into negative gamma | 10/30 32.5P | 0.43 | 0.31 | -12% (1m) | **-28%** | +32% | 32 |
| 10:15 | **AAPL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 10/30 347.5C | 0.50 | 0.71 | +46% (15m) | **+42%** | +104% | 347.56 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:30:08 ET, last candle SPY 10:29, QQQ 10:29 | no errors

## Flow surges NOT fired - price disagreed (23 today, last 5)
- 10:30 HOOD CALLS: under EMA 20 - flow says one way, price says the other
- 10:30 SMCI CALLS: price -0.16 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:30 COIN CALLS: price -0.34 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:30 PLTR CALLS: price -0.12 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:30 AAPL PUTS: price +0.78 over the last 15 min - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **COIN** | 139.23 | FLOW SURGE | **CALLS** | 64 | 10/30 142C @ 0.71 (delta 0.26) = est +207% at 143.51 | NEG -$14.4M | - | 150 | 140 | +$1.1M | +$149k bull / +$0 bear | out (clean 28, ADX 53, RVol 3.3) |
| 2 | **QQQ** | 694.09 | FLOW SURGE | **CALLS** | 61 | none: 564 calls 0-7DTE > 26 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (251 contracts' greeks worked out here) | NEG -$9.5B | 722.71 | 720 | 690 | +$58.4M | +$1.7M bull / +$0 bear | out (clean 28, ADX 48, RVol 4.5) |
| 3 | **PLTR** | 187.15 | FLOW SURGE | **CALLS** | 60 | 10/30 190C @ 0.48 (delta 0.23) = est +162% at 190 | NEG -$62.3M | 192.98 | 200 | 190 | +$1.1M | +$395k bull / +$0 bear | out (clean 26, ADX 37, RVol 3.3) |
| 4 | **SMCI** | 32.51 | FLOW SURGE | **CALLS** | 59 | 10/30 32C @ 0.64 (delta 0.74) = est +86% at 33.2 | NEG -$463k | 32.57 | 35 | 32 | +$466k | +$390k bull / +$0 bear | out (clean 28, ADX 48, RVol 2.0) |
| 5 | **NVDA** | 206.16 | FLOW SURGE | **CALLS** | 58 | 10/30 207.5C @ 0.49 (delta 0.30) = est +411% at 210 | NEG -$389.9M | 211.72 | 210 | 205 | +$6.0M | +$554k bull / +$0 bear | out (clean 26, ADX 44, RVol 2.1) |
| 6 | **AMD** | 511.31 | FLOW SURGE | **CALLS** | 58 | none: 160 calls 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (72 contracts' greeks worked out here) | NEG -$110.7M | 526.14 | 527.5 | 500 | +$4.2M | +$1.8M bull / +$0 bear | out (clean 29, ADX 43, RVol 4.4) |
| 7 | **SPY** | 758.12 | FLOW SURGE | **CALLS** | 56 | 10/30 761C @ 0.75 (delta 0.27) = est +49% at 760 | NEG -$13.9B | 771.95 | 760 | 750 | +$63.8M | +$5.9M bull / +$0 bear | out (clean 27, ADX 45, RVol 2.3) |
| 8 | **SMH** | 527.85 | FLOW SURGE | **CALLS** | 56 | none: 168 calls 0-7DTE > 8 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (73 contracts' greeks worked out here) | NEG -$558.6M | - | 532.5 | 530 | +$1.1M | +$670k bull / +$0 bear | out (clean 28, ADX 47, RVol 2.6) |
| 9 | **MU** | 890.21 | FLOW SURGE | **CALLS** | 52 | none: 158 calls 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (67 contracts' greeks worked out here) | NEG -$216.7M | 932.52 | 900 | 900 | +$21.4M | +$4.6M bull / -$56k bear | out (clean 29, ADX 40, RVol 1.6) |
| 10 | **AVGO** | 327.50 | FLOW SURGE | **CALLS** | 50 | none: 108 calls 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (49 contracts' greeks worked out here) | NEG -$128.5M | 345.84 | 330 | 330 | +$743k | +$72k bull / +$0 bear | out (clean 30, ADX 46, RVol 1.0) |
| 11 | **IWM** | 279.99 | FLOW SURGE | **CALLS** | 49 | 10/30 281C @ 0.43 (delta 0.31) = est +90% at 281.3 | NEG -$677.2M | 281.3 | 280 | 270 | +$4.9M | +$124k bull / +$0 bear | out (clean 27, ADX 40, RVol 1.6) |
| 12 | **AAPL** | 346.35 | FLOW SURGE | **PUTS** | 49 | 10/30 345P @ 0.76 (delta 0.34) = est +43% at 345 | POS +$472.4M | 341.73 | 350 | 345 | -$2.7M | +$39k bull / -$977k bear | out (clean 30, ADX 49, RVol 1.9) |
| 13 | **HOOD** | 83.88 | FLOW SURGE | **CALLS** | 49 | 10/30 85C @ 0.42 (delta 0.30) = est +69% at 85 | NEG -$37.7M | - | 85 | 85 | +$847k | +$537k bull / +$0 bear | out (clean 31, ADX 52, RVol 1.4) |
| 14 | **MSFT** | 522.10 | FLOW SURGE | **CALLS** | 41 | none: 168 calls 0-7DTE > 8 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (100 contracts' greeks worked out here) | POS +$423.7M | 514.69 | 525 | 525 | +$1.1M | +$145k bull / -$38k bear | out (clean 27, ADX 27, RVol 1.6) |
| 15 | **ORCL** | 133.03 | FLOW SURGE | **CALLS** | 37 | 10/30 134C @ 0.76 (delta 0.37) = est +99% at 135 | POS +$67.7M | 129.55 | 135 | 130 | +$507k | +$325k bull / +$0 bear | out (clean 33, ADX 34, RVol 0.9) |
| 16 | **ARM** | 205.25 | - | **-** | 33 | - | NEG -$18.9M | - | 220 | 205 | +$427k | - | out (clean 26, ADX 44, RVol 3.6) |
| 17 | **SHOP** | 158.66 | - | **-** | 30 | - | NEG -$16.3M | - | 160 | 157.5 | +$144k | - | out (clean 25, ADX 43, RVol 1.3) |
| 18 | **GOOGL** | 280.09 | - | **-** | 29 | - | NEG -$233.3M | - | 280 | 280 | +$1.0M | +$718k bull / -$26k bear | out (clean 31, ADX 34, RVol 1.4) |
| 19 | **MSTR** | 129.01 | - | **-** | 29 | - | NEG -$26.4M | - | 135 | 125 | +$708k | +$48k bull / -$430k bear | out (clean 26, ADX 42, RVol 3.6) |
| 20 | **AMZN** | 238.41 | - | **-** | 26 | - | NEG -$179.4M | 247.55 | 250 | 240 | +$2.0M | +$171k bull / -$901k bear | out (clean 32, ADX 30, RVol 3.2) |
| 21 | **NFLX** | 62.64 | - | **-** | 26 | - | NEG -$21.7M | 63.38 | 63 | 63 | +$346k | +$313k bull / -$28k bear | out (clean 31, ADX 31, RVol 0.9) |
| 22 | **BABA** | 98.29 | - | **-** | 24 | - | NEG -$40.0M | 100.33 | 100 | 98 | +$75k | - | out (clean 29, ADX 20, RVol 0.8) |
| 23 | **TSLA** | 398.19 | - | **-** | 23 | - | POS +$365.7M | 390.1 | 400 | 400 | -$6.2M | +$2.3M bull / -$5.5M bear | out (clean 28, ADX 32, RVol 1.5) |
| 24 | **DELL** | 432.50 | - | **-** | 23 | - | NEG -$58.9M | - | 440 | 425 | -$11k | +$122k bull / -$143k bear | out (clean 33, ADX 49, RVol 4.0) |
| 25 | **META** | 618.78 | - | **-** | 20 | - | NEG -$66.7M | 621.6 | 625 | 625 | +$961k | +$827k bull / -$179k bear | out (clean 28, ADX 30, RVol 0.8) |
| 26 | **CRM** | 231.32 | - | **-** | 17 | - | NEG -$21.3M | 238.21 | 240 | 230 | +$75k | - | out (clean 28, ADX 20, RVol 1.3) |
| 27 | **UBER** | 65.10 | - | **-** | 10 | - | NEG -$34.9M | 66.32 | 70 | 65 | +$21k | - | out (clean 28, ADX 16, RVol 0.8) |

## Big prints this scan (155)
- **SPY** PUT 767 2026-11-04 (5DTE): 500 @ 9.95 = **+$498k** SELL | vol 8,363 / OI 29,783
- **SPY** PUT 767 2026-11-04 (5DTE): 500 @ 9.50 = **+$475k** SELL | vol 8,363 / OI 29,783
- **SPY** CALL 759 2026-11-02 (3DTE): 797 @ 3.70 = **+$295k** BUY | vol 5,649 / OI 169
- **SPY** PUT 750 2026-11-02 (3DTE): 3,182 @ 0.84 = **+$267k** SELL | vol 8,522 / OI 8,899
- **QQQ** PUT 695 2026-11-03 (4DTE): 400 @ 6.58 = **+$263k** SELL | vol 1,337 / OI 890
- **SPY** PUT 767 2026-11-04 (5DTE): 259 @ 9.68 = **+$251k** SELL | vol 8,363 / OI 29,783
- **SPY** PUT 767 2026-11-04 (5DTE): 250 @ 9.91 = **+$248k** SELL | vol 8,363 / OI 29,783
- **SPY** PUT 767 2026-11-04 (5DTE): 240 @ 9.73 = **+$234k** SELL | vol 8,363 / OI 29,783
- **SPY** PUT 767 2026-11-04 (5DTE): 249 @ 9.34 = **+$233k** SELL | vol 8,363 / OI 29,783
- **SPY** PUT 767 2026-11-04 (5DTE): 250 @ 9.25 = **+$231k** SELL | vol 8,363 / OI 29,783
- **SPY** PUT 767 2026-11-04 (5DTE): 212 @ 9.85 = **+$209k** SELL | vol 8,363 / OI 29,783
- **TSLA** CALL 390 2026-11-06 (7DTE): 146 @ 13.57 = **+$198k** SELL | vol 2,041 / OI 1,309
- **SPY** PUT 765 2026-11-06 (7DTE): 188 @ 9.70 = **+$182k** SELL | vol 1,770 / OI 6,242
- **NFLX** CALL 61 2026-10-30 (0DTE): 1,036 @ 1.74 = **+$180k** BUY | vol 2,048 / OI 2,341
- **AMZN** PUT 247.5 2026-10-30 (0DTE): 161 @ 10.39 = **+$167k** BUY | vol 671 / OI 1,617

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 753 2026-11-03 (4DTE): 525 traded vs OI 286
- **SPY** PUT 750 2026-11-03 (4DTE): 883 traded vs OI 844
- **SPY** CALL 758 2026-11-02 (3DTE): 689 traded vs OI 147
- **SPY** CALL 764 2026-11-04 (5DTE): 507 traded vs OI 131
- **SPY** CALL 759 2026-11-06 (7DTE): 541 traded vs OI 239
- **SPY** PUT 728 2026-11-02 (3DTE): 1,027 traded vs OI 183
- **SPY** CALL 780 2026-11-04 (5DTE): 1,338 traded vs OI 1,098
- **SPY** CALL 752 2026-10-30 (0DTE): 525 traded vs OI 204
- **SPY** CALL 773 2026-11-04 (5DTE): 4,364 traded vs OI 650
- **SPY** PUT 733 2026-11-02 (3DTE): 594 traded vs OI 127
- **SPY** PUT 755 2026-11-09 (10DTE): 578 traded vs OI 464
- **SPY** PUT 759 2026-11-06 (7DTE): 1,273 traded vs OI 1,020
- **SPY** PUT 690 2026-11-13 (14DTE): 3,516 traded vs OI 3,344
- **QQQ** CALL 717 2026-11-02 (3DTE): 530 traded vs OI 150
- **QQQ** CALL 695 2026-11-03 (4DTE): 604 traded vs OI 7

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
