# GEX + FLOW SCAN - Fri Nov 13, 10:00 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (3)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 09:55 | **BABA** | **PUTS** | FLOW SURGE | 11/13 94P | 0.51 | 0.45 | -8% (0m) | **-12%** | +49% | 93.36 |
| 09:45 | **UBER** | **CALLS** | TREND + FLOW | 11/13 70C | 0.59 | 0.14 | +0% (1m) | **-76%** | +32% | 70.7 |
| 09:45 | **ORCL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/13 127C | 0.46 | 0.22 | +22% (2m) | **-52%** | +48% | 126.38 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:00:08 ET, last candle SPY 09:59, QQQ 09:59 | no errors

## Flow surges NOT fired - price disagreed (15 today, last 5)
- 10:00 HOOD CALLS: price -0.14 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:00 MSTR CALLS: price -0.83 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:00 COIN CALLS: price -1.69 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:00 NFLX PUTS: price +0.01 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:00 NVDA CALLS: price -0.05 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **HOOD** | 78.50 | FLOW SURGE | **CALLS** | 65 | 11/13 79C @ 0.54 (delta 0.40) = est +119% at 79.99 | NEG -$9.5M | 79.99 | 81 | 80 | +$1.0M | +$34k bull / +$0 bear | SHORT (clean 35, ADX 50, RVol 2.4) |
| 2 | **NFLX** | 63.80 | FLOW SURGE | **PUTS** | 62 | 11/13 64P @ 0.43 (delta 0.60) = est +58% at 63.34 | NEG -$925k | 63.82 | 65 | 65 | -$577k | +$0 bull / -$116k bear | out (clean 31, ADX 46, RVol 2.9) |
| 3 | **DELL** | 345.74 | FLOW SURGE | **CALLS** | 60 | none: 56 calls 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (48 contracts' greeks worked out here) | NEG -$8.2M | - | 360 | 360 | +$827k | +$241k bull / +$0 bear | SHORT (clean 38, ADX 31, RVol 1.7) |
| 4 | **ORCL** | 124.03 | FLOW SURGE | **CALLS** | 59 | 11/13 125C @ 0.57 (delta 0.35) = est +42% at 125 | NEG -$1.3M | 124.07 | 125 | 125 | +$1.3M | +$425k bull / +$0 bear | out (clean 31, ADX 30, RVol 2.2) |
| 5 | **GOOGL** | 301.32 | FLOW SURGE | **CALLS** | 57 | none: 94 calls 0-7DTE > 8 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (48 contracts' greeks worked out here) | POS +$212.8M | 295.33 | 300 | 290 | +$8.2M | +$3.7M bull / +$0 bear | out (clean 30, ADX 32, RVol 2.9) |
| 6 | **MSTR** | 110.80 | FLOW SURGE | **CALLS** | 57 | 11/13 113C @ 0.50 (delta 0.25) = est +100% at 112.76 | NEG -$42.5M | - | 110 | 110 | +$2.7M | +$640k bull / -$635k bear | out (clean 30, ADX 33, RVol 2.9) |
| 7 | **SMH** | 485.54 | FLOW SURGE | **CALLS** | 56 | none: 146 calls 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (66 contracts' greeks worked out here) | NEG -$268.2M | - | 500 | 475 | +$4.8M | +$975k bull / +$0 bear | out (clean 30, ADX 36, RVol 1.7) |
| 8 | **COIN** | 128.15 | FLOW SURGE | **CALLS** | 56 | 11/13 130C @ 0.63 (delta 0.29) = est +64% at 130 | NEG -$16.6M | 133.03 | 137 | 130 | +$1.5M | +$1.4M bull / -$31k bear | out (clean 31, ADX 40, RVol 2.3) |
| 9 | **IWM** | 276.83 | FLOW SURGE | **CALLS** | 55 | 11/13 277.5C @ 0.53 (delta 0.37) = est +66% at 277.86 | NEG -$2.5B | 283.33 | 285 | 275 | +$7.1M | +$1.1M bull / +$0 bear | SHORT (clean 35, ADX 46, RVol 1.5) |
| 10 | **TSLA** | 390.93 | FLOW SURGE | **CALLS** | 53 | none: 128 calls 0-7DTE > 8 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (59 contracts' greeks worked out here) | POS +$365.5M | 373.22 | 400 | 380 | +$36.0M | +$7.1M bull / -$3.2M bear | out (clean 30, ADX 32, RVol 5.2) |
| 11 | **AVGO** | 345.34 | FLOW SURGE | **CALLS** | 52 | none: 108 calls 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (44 contracts' greeks worked out here) | POS +$82.7M | 332.19 | 350 | 340 | +$10.6M | +$1.1M bull / +$0 bear | SHORT (clean 35, ADX 32, RVol 1.6) |
| 12 | **MSFT** | 521.61 | FLOW SURGE | **PUTS** | 51 | none: 166 puts 0-7DTE > 13 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (87 contracts' greeks worked out here) | POS +$32.0M | 520.54 | 535 | 520 | -$8.0M | +$0 bull / -$1.4M bear | out (clean 32, ADX 42, RVol 1.8) |
| 13 | **NVDA** | 162.50 | FLOW SURGE | **CALLS** | 48 | 11/13 165C @ 0.68 (delta 0.27) = est +164% at 165.76 | NEG -$258.6M | - | 175 | 160 | +$73.4M | +$13.5M bull / -$68k bear | out (clean 31, ADX 14, RVol 1.5) |
| 14 | **AMD** | 540.43 | FLOW SURGE | **CALLS** | 48 | none: 171 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (76 contracts' greeks worked out here) | POS +$95.5M | - | 550 | 550 | +$25.3M | +$10.3M bull / +$0 bear | SHORT (clean 35, ADX 34, RVol 1.8) |
| 15 | **SPY** | 754.42 | FLOW SURGE | **CALLS** | 47 | none: 664 calls 0-7DTE > 20 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only -16% at the target (needs +20%) (263 contracts' greeks worked out here) | NEG -$7.0B | 761.24 | 775 | 755 | +$121.7M | +$9.2M bull / +$0 bear | out (clean 32, ADX 32, RVol 1.1) |
| 16 | **QQQ** | 681.17 | FLOW SURGE | **CALLS** | 47 | none: 730 calls 0-7DTE > 26 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (253 contracts' greeks worked out here) | NEG -$2.5B | 690.73 | 680 | 680 | +$104.4M | +$7.9M bull / +$0 bear | out (clean 31, ADX 41, RVol 0.9) |
| 17 | **PLTR** | 169.65 | PINNED between the walls (positive gamma) - chop | **-** | 46 | - | POS +$89.2M | 165.23 | 170 | 170 | +$443k | +$27k bull / -$25k bear | out (clean 28, ADX 28, RVol 1.6) |
| 18 | **MU** | 772.82 | FLOW SURGE | **CALLS** | 45 | none: 160 calls 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (79 contracts' greeks worked out here) | NEG -$21.0M | 780.38 | 800 | 800 | +$32.3M | +$12.2M bull / -$551k bear | out (clean 30, ADX 22, RVol 1.6) |
| 19 | **AAPL** | 360.12 | PINNED between the walls (positive gamma) - chop | **-** | 43 | - | POS +$1.3B | 348.4 | 360 | 360 | -$570k | +$647k bull / -$915k bear | out (clean 30, ADX 40, RVol 2.2) |
| 20 | **ARM** | 190.04 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 40 | none: 30 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (26 contracts' greeks worked out here) | POS +$631k | 189.42 | 200 | 190 | -$63k | - | out (clean 32, ADX 40, RVol 2.2) |
| 21 | **SHOP** | 149.38 | FLOW SURGE | **PUTS** | 39 | none: 41 puts 0-7DTE > 2 priced 0.40-0.80 > 1 delta 0.2+ > 0 spread ok > 0 liquid (37 contracts' greeks worked out here) | POS +$6.8M | 145.52 | 150 | 150 | -$66k | +$0 bull / -$58k bear | out (clean 32, ADX 34, RVol 1.0) |
| 22 | **META** | 634.93 | - | **-** | 31 | - | POS +$63.8M | 631.08 | 650 | 625 | -$9.6M | +$527k bull / -$1.2M bear | out (clean 29, ADX 42, RVol 2.0) |
| 23 | **UBER** | 69.48 | - | **-** | 27 | - | POS +$12.6M | 68.76 | 70 | 70 | +$194k | - | out (clean 33, ADX 34, RVol 0.9) |
| 24 | **SMCI** | 26.66 | - | **-** | 25 | - | NEG -$2.2M | - | 27 | 25 | +$168k | - | out (clean 34, ADX 27, RVol 1.1) |
| 25 | **AMZN** | 268.96 | - | **-** | 24 | - | POS +$543.7M | 254.94 | 270 | 265 | +$1.1M | +$62k bull / -$446k bear | out (clean 30, ADX 33, RVol 1.3) |
| 26 | **BABA** | 94.01 | - | **-** | 21 | - | NEG -$17.6M | - | 100 | 95 | -$61k | +$0 bull / -$51k bear | out (clean 28, ADX 20, RVol 2.8) |
| 27 | **CRM** | 218.06 | - | **-** | 12 | - | NEG -$6.9M | 223.48 | 220 | 220 | +$11k | - | out (clean 30, ADX 30, RVol 1.7) |

## Big prints this scan (331)
- **QQQ** PUT 680 2026-11-20 (7DTE): 2,000 @ 8.78 = **+$1.8M** SELL | vol 3,954 / OI 87,076
- **COIN** CALL 133 2026-11-20 (7DTE): 2,400 @ 4.10 = **+$984k** BUY | vol 3,006 / OI 39
- **IWM** PUT 275 2026-11-20 (7DTE): 4,000 @ 1.89 = **+$756k** SELL | vol 4,306 / OI 45,234
- **QQQ** PUT 706 2026-11-13 (0DTE): 275 @ 21.50 = **+$591k** SELL | vol 451 / OI 427
- **QQQ** PUT 700 2026-11-16 (3DTE): 275 @ 16.05 = **+$441k** SELL | vol 295 / OI 408
- **QQQ** CALL 685 2026-11-13 (0DTE): 1,091 @ 3.29 = **+$359k** BUY | vol 10,931 / OI 8,151
- **GOOGL** CALL 307.5 2026-11-20 (7DTE): 600 @ 4.64 = **+$278k** BUY | vol 2,253 / OI 658
- **SPY** PUT 754 2026-11-20 (7DTE): 500 @ 5.47 = **+$274k** SELL | vol 580 / OI 2,052
- **QQQ** PUT 675 2026-11-17 (4DTE): 685 @ 3.79 = **+$260k** SELL | vol 912 / OI 499
- **QQQ** PUT 686 2026-11-13 (0DTE): 737 @ 3.37 = **+$248k** SELL | vol 20,731 / OI 1,850
- **QQQ** PUT 670 2026-11-20 (7DTE): 428 @ 5.76 = **+$247k** SELL | vol 1,199 / OI 34,948
- **COIN** CALL 133 2026-11-20 (7DTE): 600 @ 4.10 = **+$246k** BUY | vol 3,006 / OI 39
- **SPY** PUT 761 2026-11-16 (3DTE): 396 @ 5.50 = **+$218k** SELL | vol 849 / OI 423
- **AMD** CALL 557.5 2026-11-13 (0DTE): 251 @ 8.50 = **+$213k** BUY | vol 1,025 / OI 698
- **TSLA** CALL 390 2026-11-13 (0DTE): 401 @ 5.32 = **+$213k** BUY | vol 3,941 / OI 7,011

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 764 2026-11-16 (3DTE): 1,598 traded vs OI 1,529
- **SPY** PUT 721 2026-11-16 (3DTE): 668 traded vs OI 503
- **SPY** CALL 784 2026-11-17 (4DTE): 1,405 traded vs OI 432
- **SPY** PUT 750 2026-11-16 (3DTE): 2,830 traded vs OI 2,006
- **SPY** PUT 747 2026-11-13 (0DTE): 5,065 traded vs OI 4,517
- **SPY** PUT 758 2026-11-16 (3DTE): 3,002 traded vs OI 2,627
- **SPY** CALL 756 2026-11-13 (0DTE): 9,598 traded vs OI 4,631
- **SPY** PUT 680 2026-12-11 (28DTE): 510 traded vs OI 0
- **QQQ** PUT 659 2026-11-17 (4DTE): 1,029 traded vs OI 160
- **QQQ** CALL 685 2026-11-13 (0DTE): 10,931 traded vs OI 8,151
- **QQQ** PUT 614 2026-11-16 (3DTE): 530 traded vs OI 0
- **QQQ** CALL 713 2026-11-17 (4DTE): 781 traded vs OI 231
- **QQQ** PUT 643 2026-11-16 (3DTE): 1,022 traded vs OI 58
- **QQQ** CALL 683 2026-11-13 (0DTE): 1,368 traded vs OI 1,038
- **QQQ** PUT 685 2026-11-13 (0DTE): 29,311 traded vs OI 26,536

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
