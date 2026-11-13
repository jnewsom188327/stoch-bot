# GEX + FLOW SCAN - Fri Nov 13, 10:35 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (8)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:17 | **QQQ** | **CALLS** | 1m WHIPSAW (R1 R2) | 11/13 683C | 0.75 | 0.47 | -1% (0m) | **-37%** | +60% | 678.58 |
| 10:15 | **ARM** | **PUTS** | FLIP CROSS down into negative gamma | 11/13 182.5P | 0.74 | 1.25 | +76% (19m) | **+69%** | +96% | 183.6 |
| 10:15 | **ORCL** | **CALLS** | FLIP CROSS up into positive gamma | 11/13 124C | 0.65 | 0.86 | +48% (18m) | **+32%** | +66% | 123.68 hit |
| 10:10 | **ORCL** | **PUTS** | FLIP CROSS down into negative gamma | 11/13 120P | 0.46 | 0.20 | +7% (5m) | **-57%** | +63% | 121.25 |
| 10:05 | **GOOGL** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/13 297.5P | 0.74 | 2.88 | +332% (18m) | **+289%** | +288% | 295 hit |
| 09:55 | **BABA** | **PUTS** | FLOW SURGE | 11/13 94P | 0.51 | 0.38 | +4% (36m) | **-25%** | +49% | 93.36 |
| 09:45 | **UBER** | **CALLS** | TREND + FLOW | 11/13 70C | 0.59 | 0.16 | +0% (1m) | **-73%** | +32% | 70.7 |
| 09:45 | **ORCL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/13 127C | 0.46 | 0.13 | +22% (2m) | **-72%** | +48% | 126.38 |

## 1m RULES on SPY / QQQ - loose (1 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:35:08 ET, last candle SPY 10:34, QQQ 10:34 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 10:16 | QQQ | 1m WHIPSAW | R1 R2 | CALLS | TURNING your way | **FIRE** QQQ261113C00683000 |

## Flow surges NOT fired - price disagreed (40 today, last 5)
- 10:35 HOOD CALLS: price -0.35 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:35 MSTR CALLS: price -1.55 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:35 COIN CALLS: price -1.02 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:35 GOOGL CALLS: price -1.17 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:30 HOOD CALLS: price +0.00 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **HOOD** | 77.18 | FLOW SURGE | **CALLS** | 63 | 11/13 78C @ 0.46 (delta 0.34) = est +91% at 78.54 | NEG -$10.1M | 80.2 | 81 | 75 | +$2.1M | +$43k bull / +$0 bear | SHORT (clean 36, ADX 61, RVol 2.9) |
| 2 | **COIN** | 126.25 | FLOW SURGE | **CALLS** | 60 | 11/13 128C @ 0.62 (delta 0.30) = est +89% at 128.19 | NEG -$17.4M | 132.82 | 137 | 125 | +$3.4M | +$1.1M bull / +$0 bear | out (clean 31, ADX 47, RVol 2.4) |
| 3 | **AMD** | 530.10 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 58 | none: 171 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (77 contracts' greeks worked out here) | POS +$60.6M | - | 550 | 530 | +$62.5M | +$4.9M bull / -$2.6M bear | SHORT (clean 35, ADX 50, RVol 1.6) |
| 4 | **DELL** | 340.15 | TREND (flow not with it) | **PUTS** | 57 | none: 54 puts 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (45 contracts' greeks worked out here) | NEG -$8.2M | - | 350 | 360 | +$8.1M | +$26k bull / -$36k bear | SHORT (clean 38, ADX 46, RVol 1.3) |
| 5 | **IWM** | 275.93 | TREND (flow not with it) | **PUTS** | 53 | 11/13 275P @ 0.55 (delta 0.34) = est +42% at 275 | NEG -$2.7B | 283.25 | 285 | 275 | +$18.6M | +$122k bull / -$185k bear | SHORT (clean 36, ADX 52, RVol 1.3) |
| 6 | **GOOGL** | 295.00 | FLOW SURGE | **CALLS** | 52 | 11/13 297.5C @ 0.70 (delta 0.27) = est +92% at 297.5 | POS +$179.0M | 289.08 | 300 | 290 | +$17.7M | +$1.9M bull / +$0 bear | out (clean 30, ADX 30, RVol 2.2) |
| 7 | **QQQ** | 674.34 | FLOW SURGE | **CALLS** | 51 | none: 752 calls 0-7DTE > 27 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (281 contracts' greeks worked out here) | NEG -$3.1B | 690.29 | 680 | 680 | +$328.1M | +$9.7M bull / -$620k bear | out (clean 32, ADX 55, RVol 1.7) |
| 8 | **MSTR** | 108.76 | FLOW SURGE | **CALLS** | 51 | 11/13 111C @ 0.54 (delta 0.26) = est +32% at 110 | NEG -$34.7M | - | 110 | 110 | +$6.2M | +$2.6M bull / +$0 bear | out (clean 30, ADX 42, RVol 1.9) |
| 9 | **AVGO** | 341.87 | FLOW SURGE | **CALLS** | 48 | none: 108 calls 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (51 contracts' greeks worked out here) | POS +$69.1M | - | 340 | 340 | +$19.4M | +$225k bull / +$0 bear | SHORT (clean 35, ADX 45, RVol 1.0) |
| 10 | **SMH** | 478.17 | FLOW SURGE | **CALLS** | 47 | none: 141 calls 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (69 contracts' greeks worked out here) | NEG -$301.7M | - | 500 | 475 | +$10.6M | +$3.1M bull / -$306k bear | out (clean 31, ADX 51, RVol 1.6) |
| 11 | **ORCL** | 123.49 | FLIP CROSS up into positive gamma | **CALLS** | 47 | 11/13 125C @ 0.55 (delta 0.30) = est +64% at 125 | POS +$4.9M | 122.1 | 125 | 125 | +$1.2M | +$0 bull / -$283k bear | out (clean 31, ADX 41, RVol 1.7) |
| 12 | **PLTR** | 165.35 | PINNED between the walls (positive gamma) - chop | **-** | 46 | - | POS +$66.8M | 158.13 | 165 | 165 | +$3.6M | - | out (clean 29, ADX 45, RVol 2.1) |
| 13 | **SPY** | 750.52 | FLOW SURGE | **CALLS** | 45 | none: 664 calls 0-7DTE > 20 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (249 contracts' greeks worked out here) | NEG -$8.6B | 760.5 | 750 | 750 | +$297.0M | +$2.6M bull / -$2.5M bear | out (clean 33, ADX 39, RVol 1.4) |
| 14 | **AMZN** | 265.59 | PINNED between the walls (positive gamma) - chop | **-** | 44 | - | POS +$440.1M | 252.08 | 265 | 265 | +$6.8M | +$7.6M bull / +$0 bear | out (clean 29, ADX 33, RVol 0.9) |
| 15 | **NVDA** | 159.97 | FLOW SURGE | **CALLS** | 42 | 11/13 162.5C @ 0.67 (delta 0.27) = est +142% at 163 | NEG -$284.9M | - | 175 | 160 | +$107.9M | +$5.2M bull / -$1.6M bear | out (clean 31, ADX 16, RVol 1.2) |
| 16 | **TSLA** | 388.11 | FLOW SURGE | **CALLS** | 42 | none: 124 calls 0-7DTE > 8 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (51 contracts' greeks worked out here) | POS +$260.7M | 378.71 | 400 | 380 | +$67.2M | +$2.1M bull / -$788k bear | out (clean 29, ADX 24, RVol 1.8) |
| 17 | **MU** | 759.44 | - | **-** | 29 | - | NEG -$18.8M | 770.68 | 800 | 750 | +$75.8M | +$11.7M bull / -$2.9M bear | out (clean 31, ADX 36, RVol 1.6) |
| 18 | **META** | 627.66 | - | **-** | 25 | - | NEG -$61.5M | 631.12 | 630 | 625 | +$8.1M | +$2.4M bull / +$0 bear | out (clean 29, ADX 34, RVol 2.7) |
| 19 | **AAPL** | 358.69 | - | **-** | 23 | - | POS +$1.3B | 349.06 | 360 | 360 | +$11.2M | +$2.3M bull / -$394k bear | out (clean 30, ADX 32, RVol 1.0) |
| 20 | **SMCI** | 26.25 | - | **-** | 22 | - | NEG -$2.6M | - | 27 | 25 | +$309k | - | out (clean 34, ADX 30, RVol 1.2) |
| 21 | **ARM** | 185.58 | - | **-** | 22 | - | NEG -$2.3M | 189.79 | 185 | 190 | -$116k | +$62k bull / +$0 bear | out (clean 33, ADX 54, RVol 1.1) |
| 22 | **UBER** | 69.39 | - | **-** | 21 | - | POS +$9.8M | 68.89 | 70 | 70 | +$236k | - | out (clean 33, ADX 24, RVol 0.3) |
| 23 | **MSFT** | 521.98 | - | **-** | 20 | - | POS +$40.0M | 520.84 | 535 | 520 | -$38k | +$0 bull / -$315k bear | out (clean 32, ADX 39, RVol 1.8) |
| 24 | **CRM** | 216.35 | - | **-** | 16 | - | NEG -$6.9M | 220.3 | 220 | 220 | +$76k | - | out (clean 29, ADX 23, RVol 1.2) |
| 25 | **NFLX** | 62.88 | - | **-** | 12 | - | NEG -$25.3M | 63.63 | 65 | 60 | +$67k | - | out (clean 31, ADX 35, RVol 2.8) |
| 26 | **SHOP** | 146.65 | - | **-** | 8 | - | POS +$3.6M | 144.75 | 150 | 140 | +$7k | - | out (clean 31, ADX 29, RVol 1.2) |
| 27 | **BABA** | 93.91 | - | **-** | 7 | - | NEG -$16.7M | - | 100 | 95 | +$15k | - | out (clean 28, ADX 24, RVol 1.0) |

## Big prints this scan (256)
- **AMZN** CALL 260 2026-11-20 (7DTE): 3,460 @ 9.21 = **+$3.2M** BUY | vol 4,763 / OI 15,661
- **AMZN** CALL 260 2026-11-13 (0DTE): 3,460 @ 6.11 = **+$2.1M** BUY | vol 4,516 / OI 12,073
- **QQQ** PUT 685 2026-11-13 (0DTE): 941 @ 11.18 = **+$1.1M** SELL | vol 47,046 / OI 26,536
- **MU** PUT 735 2026-11-16 (3DTE): 1,500 @ 6.37 = **+$956k** SELL | vol 1,622 / OI 105
- **QQQ** PUT 685 2026-11-13 (0DTE): 919 @ 9.80 = **+$901k** SELL | vol 47,046 / OI 26,536
- **SMH** CALL 480 2026-11-20 (7DTE): 573 @ 15.27 = **+$875k** BUY | vol 1,270 / OI 3,062
- **MU** PUT 730 2026-11-16 (3DTE): 1,500 @ 5.12 = **+$768k** SELL | vol 1,795 / OI 98
- **QQQ** PUT 680 2026-11-13 (0DTE): 941 @ 7.03 = **+$662k** SELL | vol 76,969 / OI 11,590
- **META** PUT 630 2026-11-16 (3DTE): 632 @ 8.10 = **+$512k** SELL | vol 1,105 / OI 212
- **MSTR** PUT 112 2026-11-20 (7DTE): 794 @ 6.25 = **+$496k** SELL | vol 2,209 / OI 0
- **NVDA** CALL 160 2026-11-16 (3DTE): 1,134 @ 4.10 = **+$465k** BUY | vol 4,326 / OI 919
- **QQQ** PUT 685 2026-11-13 (0DTE): 476 @ 9.70 = **+$462k** SELL | vol 47,046 / OI 26,536
- **AMZN** CALL 260 2026-11-20 (7DTE): 430 @ 9.05 = **+$389k** BUY | vol 4,763 / OI 15,661
- **SMH** CALL 480 2026-11-20 (7DTE): 241 @ 15.35 = **+$370k** BUY | vol 1,270 / OI 3,062
- **QQQ** CALL 675 2026-11-20 (7DTE): 250 @ 12.46 = **+$312k** BUY | vol 657 / OI 6,650

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 762 2026-11-13 (0DTE): 4,525 traded vs OI 4,518
- **SPY** PUT 724 2026-11-13 (0DTE): 2,704 traded vs OI 1,994
- **SPY** CALL 750 2026-11-17 (4DTE): 550 traded vs OI 488
- **SPY** CALL 747 2026-11-13 (0DTE): 2,412 traded vs OI 1,939
- **SPY** CALL 754 2026-11-17 (4DTE): 546 traded vs OI 289
- **SPY** CALL 749 2026-11-13 (0DTE): 7,546 traded vs OI 3,489
- **SPY** CALL 760 2026-11-18 (5DTE): 1,084 traded vs OI 1,008
- **SPY** CALL 752 2026-11-17 (4DTE): 1,063 traded vs OI 110
- **SPY** CALL 749 2026-11-16 (3DTE): 755 traded vs OI 473
- **SPY** PUT 701 2026-11-16 (3DTE): 745 traded vs OI 92
- **SPY** PUT 740 2026-11-17 (4DTE): 1,460 traded vs OI 1,345
- **SPY** PUT 728 2026-11-16 (3DTE): 640 traded vs OI 585
- **SPY** CALL 773 2026-11-13 (0DTE): 3,549 traded vs OI 3,521
- **QQQ** PUT 688 2026-11-16 (3DTE): 793 traded vs OI 731
- **QQQ** CALL 675 2026-11-16 (3DTE): 843 traded vs OI 384

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
