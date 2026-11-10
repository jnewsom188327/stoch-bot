# GEX + FLOW SCAN - Tue Nov 10, 10:15 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (3)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:15 | **IWM** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/10 280P | 0.63 | 0.62 | -2% (0m) | **-2%** | +22% | 280 |
| 09:50 | **SPY** | **PUTS** | FLOW SURGE | 11/10 743P | 0.77 | 0.23 | +5% (1m) | **-70%** | +54% | 745.65 |
| 09:45 | **IWM** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/10 279P | 0.52 | 0.31 | +50% (8m) | **-40%** | +87% | 278.66 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:15:08 ET, last candle SPY 10:14, QQQ 10:14 | no errors

## Flow surges NOT fired - price disagreed (6 today, last 5)
- 10:15 BABA PUTS: price +0.24 over the last 15 min - flow says one way, price says the other
- 10:10 BABA PUTS: price +0.73 over the last 15 min - flow says one way, price says the other
- 10:00 NFLX CALLS: price -0.14 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:00 AAPL CALLS: price -2.97 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 09:55 BABA CALLS: price -0.98 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **AMD** | 538.41 | FLOW SURGE | **PUTS** | 57 | none: 129 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (3 contracts' greeks worked out here) | POS +$40.4M | - | 550 | 500 | -$101.4M | +$0 bull / -$5.5M bear | out (clean 31, ADX 36, RVol 2.8) |
| 2 | **IWM** | 280.65 | RUN: clean trend + negative gamma + flow agrees | **PUTS** | 56 | 11/10 280P @ 0.63 (delta 0.39) = est +22% at 280 | NEG -$899.5M | 284.05 | 285 | 270 | -$1.1M | - | SHORT (clean 36, ADX 44, RVol 1.7) |
| 3 | **AVGO** | 333.72 | FLIP CROSS down into negative gamma | **PUTS** | 52 | none: 78 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (9 contracts' greeks worked out here) | NEG -$808k | 334.29 | 340 | 340 | -$8.6M | +$0 bull / -$1.3M bear | out (clean 31, ADX 34, RVol 2.8) |
| 4 | **BABA** | 104.54 | FLOW SURGE | **PUTS** | 50 | 11/13 101P @ 0.65 (delta 0.22) = est +23% at 103.74 | NEG -$4.6M | 106.06 | 110 | 105 | -$582k | +$0 bull / -$134k bear | out (clean 29, ADX 30, RVol 1.7) |
| 5 | **AAPL** | 347.04 | FLOW SURGE | **CALLS** | 46 | none: 84 calls 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (16 contracts' greeks worked out here) | POS +$391.1M | 336.19 | 350 | 340 | +$15.1M | +$457k bull / +$0 bear | out (clean 28, ADX 22, RVol 1.4) |
| 6 | **GOOGL** | 290.24 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 45 | none: 69 calls 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (5 contracts' greeks worked out here) | POS +$10.1M | 289.15 | 300 | 290 | +$750k | +$27k bull / -$102k bear | out (clean 30, ADX 18, RVol 2.0) |
| 7 | **TSLA** | 377.29 | TREND + FLOW | **PUTS** | 42 | none: 93 puts 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (1 contracts' greeks worked out here) | POS +$194.6M | - | 400 | 380 | -$10.1M | +$718k bull / -$2.9M bear | SHORT (clean 34, ADX 40, RVol 0.7) |
| 8 | **SMH** | 490.77 | FLOW SURGE | **PUTS** | 41 | none: 117 puts 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (10 contracts' greeks worked out here) | NEG -$190.8M | - | 500 | 475 | -$2.0M | +$0 bull / -$876k bear | out (clean 29, ADX 26, RVol 1.1) |
| 9 | **UBER** | 70.10 | PINNED between the walls (positive gamma) - chop | **-** | 29 | - | POS +$9.9M | 68.3 | 70 | 70 | -$51k | - | out (clean 33, ADX 39, RVol 0.6) |
| 10 | **MU** | 740.00 | - | **-** | 26 | - | NEG -$7.9M | - | 750 | 750 | -$39.9M | +$815k bull / -$5.2M bear | out (clean 30, ADX 24, RVol 1.3) |
| 11 | **SPY** | 750.98 | - | **-** | 25 | - | NEG -$5.7B | 761 | 750 | 750 | -$77.5M | +$0 bull / -$12.7M bear | out (clean 32, ADX 31, RVol 0.9) |
| 12 | **QQQ** | 679.11 | - | **-** | 25 | - | NEG -$1.5B | 693.4 | 680 | 680 | -$101.8M | +$133k bull / -$1.8M bear | out (clean 31, ADX 26, RVol 0.8) |
| 13 | **PLTR** | 168.31 | - | **-** | 22 | - | POS +$52.5M | - | 165 | 170 | -$595k | +$94k bull / -$27k bear | out (clean 28, ADX 38, RVol 0.4) |
| 14 | **NVDA** | 173.42 | - | **-** | 21 | - | NEG -$177.1M | - | 185 | 180 | -$2.4M | +$258k bull / -$5.9M bear | out (clean 32, ADX 28, RVol 2.9) |
| 15 | **META** | 645.72 | - | **-** | 21 | - | POS +$276.2M | - | 650 | 650 | -$2.3M | +$0 bull / -$969k bear | out (clean 33, ADX 30, RVol 0.7) |
| 16 | **NFLX** | 62.91 | - | **-** | 21 | - | NEG -$22.7M | 65.43 | 65 | 60 | -$194k | +$0 bull / -$66k bear | out (clean 30, ADX 32, RVol 1.1) |
| 17 | **MSFT** | 542.17 | - | **-** | 20 | - | POS +$663.2M | - | 550 | 535 | +$93k | +$68k bull / -$47k bear | out (clean 33, ADX 41, RVol 1.1) |
| 18 | **AMZN** | 271.89 | - | **-** | 19 | - | POS +$489.1M | - | 270 | 265 | +$1.3M | +$0 bull / -$292k bear | out (clean 32, ADX 31, RVol 1.1) |
| 19 | **DELL** | 340.64 | - | **-** | 18 | - | NEG -$8.1M | - | 350 | 340 | -$149k | +$119k bull / -$54k bear | out (clean 32, ADX 26, RVol 1.1) |
| 20 | **MSTR** | 124.04 | - | **-** | 17 | - | POS +$6.7M | 120.43 | 133 | 120 | +$239k | +$0 bull / -$397k bear | out (clean 30, ADX 24, RVol 0.8) |
| 21 | **ARM** | 184.50 | - | **-** | 17 | - | NEG -$4.5M | - | 185 | 190 | -$123k | - | out (clean 27, ADX 24, RVol 0.6) |
| 22 | **CRM** | 213.19 | - | **-** | 17 | - | NEG -$10.7M | - | 195 | 220 | -$94k | - | out (clean 31, ADX 30, RVol 0.7) |
| 23 | **SHOP** | 149.53 | - | **-** | 17 | - | POS +$2.4M | 144.2 | 155 | 140 | -$9k | - | out (clean 31, ADX 36, RVol 0.5) |
| 24 | **SMCI** | 28.70 | - | **-** | 16 | - | POS +$4.0M | - | 30 | 30 | -$131k | - | out (clean 28, ADX 23, RVol 0.5) |
| 25 | **HOOD** | 82.52 | - | **-** | 14 | - | POS +$4.0M | 79.01 | 85 | 80 | +$310k | - | out (clean 30, ADX 30, RVol 1.3) |
| 26 | **ORCL** | 120.04 | - | **-** | 10 | - | NEG -$23.7M | - | 130 | 125 | -$96k | - | out (clean 28, ADX 32, RVol 0.9) |
| 27 | **COIN** | 133.63 | - | **-** | 6 | - | POS +$8.8M | 125.62 | 141 | 135 | -$23k | - | out (clean 32, ADX 24, RVol 0.6) |

## Big prints this scan (224)
- **SPY** PUT 760 2026-11-13 (3DTE): 1,970 @ 11.75 = **+$2.3M** BUY | vol 16,645 / OI 5,844
- **SPY** PUT 760 2026-11-13 (3DTE): 1,826 @ 12.20 = **+$2.2M** BUY | vol 16,645 / OI 5,844
- **NVDA** CALL 170 2026-11-11 (1DTE): 970 @ 4.60 = **+$446k** SELL | vol 14,362 / OI 252
- **QQQ** CALL 674 2026-11-10 (0DTE): 500 @ 5.50 = **+$275k** SELL | vol 33,922 / OI 417
- **META** CALL 630 2026-11-11 (1DTE): 173 @ 14.95 = **+$259k** SELL | vol 376 / OI 1,923
- **NVDA** CALL 170 2026-11-16 (6DTE): 370 @ 6.15 = **+$228k** SELL | vol 2,729 / OI 394
- **MSTR** PUT 123 2026-11-13 (3DTE): 491 @ 4.05 = **+$199k** MID | vol 1,516 / OI 2,696
- **NVDA** CALL 170 2026-11-11 (1DTE): 500 @ 3.83 = **+$192k** SELL | vol 14,362 / OI 252
- **QQQ** PUT 660 2026-11-13 (3DTE): 690 @ 2.71 = **+$187k** BUY | vol 4,431 / OI 7,659
- **QQQ** CALL 670 2026-11-17 (7DTE): 130 @ 14.15 = **+$184k** SELL | vol 310 / OI 98
- **NVDA** CALL 172.5 2026-11-13 (3DTE): 434 @ 4.02 = **+$174k** SELL | vol 4,996 / OI 58
- **SPY** PUT 748 2026-11-13 (3DTE): 366 @ 4.67 = **+$171k** BUY | vol 5,213 / OI 2,268
- **AMD** CALL 530 2026-11-13 (3DTE): 100 @ 16.92 = **+$169k** SELL | vol 1,427 / OI 1,599
- **META** CALL 652.5 2026-11-11 (1DTE): 484 @ 3.15 = **+$152k** SELL | vol 817 / OI 86
- **META** CALL 645 2026-11-11 (1DTE): 242 @ 5.97 = **+$144k** SELL | vol 1,489 / OI 95

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 751 2026-11-12 (2DTE): 743 traded vs OI 697
- **SPY** CALL 748 2026-11-12 (2DTE): 644 traded vs OI 615
- **SPY** PUT 736 2026-11-11 (1DTE): 1,285 traded vs OI 1,053
- **SPY** PUT 709 2026-11-10 (0DTE): 1,060 traded vs OI 573
- **SPY** PUT 738 2026-11-11 (1DTE): 1,693 traded vs OI 1,617
- **SPY** PUT 748 2026-11-16 (6DTE): 515 traded vs OI 188
- **SPY** PUT 747 2026-11-18 (8DTE): 788 traded vs OI 91
- **SPY** PUT 730 2026-11-23 (13DTE): 502 traded vs OI 0
- **QQQ** PUT 657 2026-11-11 (1DTE): 504 traded vs OI 323
- **QQQ** PUT 672 2026-11-13 (3DTE): 634 traded vs OI 621
- **QQQ** CALL 700 2026-11-10 (0DTE): 3,142 traded vs OI 2,949
- **QQQ** PUT 678 2026-11-11 (1DTE): 513 traded vs OI 89
- **QQQ** PUT 682 2026-11-10 (0DTE): 572 traded vs OI 118
- **QQQ** CALL 695 2026-11-11 (1DTE): 1,149 traded vs OI 942
- **QQQ** PUT 680 2026-11-11 (1DTE): 700 traded vs OI 423

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
