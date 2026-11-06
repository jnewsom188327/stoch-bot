# GEX + FLOW SCAN - Fri Nov 06, 12:40 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (4)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 12:40 | **SPY** | **CALLS** | 1m WHIPSAW (R1) | 11/06 742C | 0.42 | 0.45 | +7% (0m) | **+7%** | +42% | 739.03 |
| 10:30 | **NVDA** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/06 192.5C | 0.73 | 0.28 | +12% (20m) | **-62%** (done) | +199% | 193.9 |
| 10:00 | **NVDA** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/06 197.5C | 0.67 | 0.03 | -6% (1m) | **-96%** (done) | +24% | 195 |
| 09:50 | **NFLX** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/06 64C | 0.40 | 0.36 | +32% (4m) | **-10%** (done) | +164% | 65 |

## 1m RULES on SPY / QQQ - loose (5 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 12:40:08 ET, last candle SPY 12:39, QQQ 12:39 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 12:39 | SPY | 1m WHIPSAW | R1 | CALLS | AGAINST you | **FIRE** SPY261106C00742000 |
| 12:38 | QQQ | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |
| 12:38 | SPY | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |
| 12:37 | QQQ | 1m WHIPSAW | R1 R2 | PUTS | WITH you | no contract: 39 puts 0-1DTE > 5 priced 0.40-0.80 > 1 delta 0.15+ > 1 spread ok > 1 liquid  |
| 12:37 | SPY | 1m WHIPSAW | R1 R2 | PUTS | WITH you | no contract: 43 puts 0-1DTE > 3 priced 0.40-0.80 > 1 delta 0.15+ > 1 spread ok > 1 liquid  |

## Flow surges NOT fired - price disagreed (6 today, last 5)
- 09:55 SMCI PUTS: price +0.09 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 HOOD PUTS: price +3.27 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 MSTR PUTS: price +3.75 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 SMCI PUTS: price +0.89 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 PLTR PUTS: price +5.57 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **MSTR** | 127.06 | FLIP CROSS down into negative gamma | **PUTS** | 34 | 11/06 126P @ 0.72 (delta 0.35) = est +90% at 125 | NEG -$6.4M | 127.62 | 135 | 125 | -$8.0M | +$134k bull / +$0 bear | out (clean 31, ADX 14, RVol 0.7) |
| 2 | **AAPL** | 343.82 | FLIP CROSS down into negative gamma | **PUTS** | 29 | 11/06 342.5P @ 0.72 (delta 0.33) = est +78% at 341.8 | NEG -$37.4M | 344.24 | 345 | 345 | -$16.1M | +$0 bull / -$123k bear | out (clean 29, ADX 8, RVol 0.3) |
| 3 | **NFLX** | 63.88 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 24 | none: 26 puts 0-7DTE > 1 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only +9% at the target (needs +20%) (20 contracts' greeks worked out here) | POS +$1.8M | 63.85 | 64 | 65 | -$325k | - | out (clean 32, ADX 15, RVol 0.6) |
| 4 | **TSLA** | 358.60 | - | **-** | 21 | - | NEG -$299.5M | - | 370 | 360 | -$63.6M | +$821k bull / -$108k bear | out (clean 35, ADX 30, RVol 0.3) |
| 5 | **SHOP** | 149.34 | - | **-** | 19 | - | NEG -$1.9M | 150.62 | 150 | 150 | -$1.3M | - | out (clean 36, ADX 29, RVol 0.7) |
| 6 | **IWM** | 273.22 | - | **-** | 18 | - | NEG -$3.1B | 285.54 | 285 | 270 | -$5.3M | +$110k bull / +$0 bear | out (clean 34, ADX 20, RVol 1.0) |
| 7 | **SMH** | 459.31 | - | **-** | 18 | - | NEG -$459.7M | - | 505 | 465 | +$7.5M | +$114k bull / +$0 bear | out (clean 33, ADX 11, RVol 0.6) |
| 8 | **PLTR** | 160.51 | - | **-** | 17 | - | NEG -$66.1M | - | 165 | 160 | +$3.3M | +$0 bull / -$61k bear | out (clean 28, ADX 18, RVol 0.4) |
| 9 | **NVDA** | 186.41 | - | **-** | 16 | - | NEG -$365.0M | - | 200 | 190 | +$23.8M | +$687k bull / +$0 bear | out (clean 33, ADX 11, RVol 0.8) |
| 10 | **META** | 616.73 | - | **-** | 16 | - | NEG -$97.6M | 620.14 | 650 | 610 | -$6.1M | +$368k bull / +$0 bear | out (clean 33, ADX 21, RVol 0.5) |
| 11 | **AVGO** | 292.17 | - | **-** | 16 | - | NEG -$122.5M | - | 320 | 300 | +$3.8M | +$294k bull / +$0 bear | out (clean 31, ADX 14, RVol 0.8) |
| 12 | **MU** | 686.32 | - | **-** | 16 | - | NEG -$175.1M | - | 700 | 700 | +$69.0M | +$2.1M bull / -$250k bear | out (clean 32, ADX 10, RVol 0.6) |
| 13 | **HOOD** | 79.06 | - | **-** | 16 | - | NEG -$21.7M | 82.47 | 85 | 80 | +$1.5M | +$102k bull / +$0 bear | out (clean 30, ADX 16, RVol 0.6) |
| 14 | **SPY** | 737.06 | - | **-** | 15 | - | NEG -$14.5B | 768.92 | 760 | 740 | -$44.8M | +$358k bull / +$0 bear | out (clean 34, ADX 12, RVol 0.7) |
| 15 | **QQQ** | 656.29 | - | **-** | 15 | - | NEG -$4.6B | - | 700 | 650 | +$34.0M | +$248k bull / -$411k bear | out (clean 34, ADX 14, RVol 0.8) |
| 16 | **AMD** | 437.49 | - | **-** | 15 | - | NEG -$184.1M | - | 430 | 440 | +$13.9M | +$1.2M bull / +$0 bear | out (clean 32, ADX 15, RVol 0.4) |
| 17 | **AMZN** | 261.35 | - | **-** | 15 | - | POS +$334.5M | - | 260 | 260 | -$387k | +$111k bull / -$37k bear | out (clean 34, ADX 22, RVol 0.4) |
| 18 | **MSFT** | 533.48 | - | **-** | 15 | - | POS +$638.7M | 509.86 | 535 | 535 | +$3.0M | +$43k bull / +$0 bear | out (clean 33, ADX 12, RVol 0.3) |
| 19 | **ORCL** | 112.33 | - | **-** | 15 | - | NEG -$53.6M | - | 120 | 110 | +$548k | +$27k bull / +$0 bear | out (clean 30, ADX 11, RVol 0.8) |
| 20 | **COIN** | 132.75 | - | **-** | 11 | - | NEG -$22.6M | 136.54 | 142 | 130 | -$3.8M | - | out (clean 32, ADX 14, RVol 0.3) |
| 21 | **DELL** | 330.88 | - | **-** | 9 | - | NEG -$26.3M | - | 335 | 335 | +$4.7M | - | out (clean 32, ADX 9, RVol 0.3) |
| 22 | **CRM** | 214.58 | - | **-** | 9 | - | NEG -$25.3M | - | 230 | 215 | -$330k | - | out (clean 35, ADX 20, RVol 0.8) |
| 23 | **BABA** | 108.60 | - | **-** | 8 | - | POS +$29.8M | - | 110 | 110 | -$456k | - | out (clean 34, ADX 17, RVol 0.5) |
| 24 | **ARM** | 171.01 | - | **-** | 7 | - | NEG -$26.1M | - | 180 | 170 | -$394k | - | out (clean 25, ADX 12, RVol 0.8) |
| 25 | **SMCI** | 28.04 | - | **-** | 6 | - | NEG -$3.9M | - | 30 | 28 | -$396k | - | out (clean 34, ADX 16, RVol 0.3) |
| 26 | **UBER** | 69.22 | - | **-** | 6 | - | POS +$11.3M | 68.54 | 70 | 70 | +$108k | - | out (clean 30, ADX 16, RVol 0.5) |
| 27 | **GOOGL** | 285.80 | - | **-** | 4 | - | POS +$62.1M | 283.31 | 285 | 290 | +$1.4M | - | out (clean 34, ADX 13, RVol 0.5) |

## Big prints this scan (50)
- **META** CALL 612.5 2026-11-06 (0DTE): 200 @ 8.11 = **+$162k** BUY | vol 1,506 / OI 298
- **QQQ** CALL 660 2026-11-06 (0DTE): 500 @ 2.65 = **+$132k** BUY | vol 153,886 / OI 330
- **TSLA** PUT 370 2026-11-06 (0DTE): 120 @ 10.40 = **+$125k** SELL | vol 1,847 / OI 4,963
- **SPY** PUT 769 2026-11-13 (7DTE): 40 @ 30.73 = **+$123k** SELL | vol 153 / OI 1,473
- **SPY** PUT 769 2026-11-13 (7DTE): 40 @ 30.54 = **+$122k** SELL | vol 153 / OI 1,473
- **QQQ** CALL 658 2026-11-06 (0DTE): 299 @ 3.85 = **+$115k** BUY | vol 46,527 / OI 0
- **META** CALL 617.5 2026-11-06 (0DTE): 200 @ 4.22 = **+$84k** BUY | vol 5,516 / OI 163
- **MU** CALL 690 2026-11-11 (5DTE): 20 @ 35.07 = **+$70k** BUY | vol 263 / OI 0
- **AMD** PUT 452.5 2026-11-09 (3DTE): 38 @ 18.25 = **+$69k** SELL | vol 756 / OI 54
- **NVDA** CALL 177.5 2026-11-13 (7DTE): 50 @ 13.45 = **+$67k** BUY | vol 314 / OI 0
- **MSTR** PUT 130 2026-11-13 (7DTE): 100 @ 6.65 = **+$66k** SELL | vol 417 / OI 1,658
- **IWM** PUT 281 2026-11-11 (5DTE): 76 @ 7.42 = **+$56k** SELL | vol 93 / OI 575
- **IWM** PUT 281 2026-11-09 (3DTE): 76 @ 7.11 = **+$54k** SELL | vol 103 / OI 563
- **TSLA** CALL 360 2026-11-06 (0DTE): 199 @ 2.32 = **+$46k** BUY | vol 132,609 / OI 599
- **MSFT** CALL 542.5 2026-11-13 (7DTE): 70 @ 6.17 = **+$43k** BUY | vol 1,603 / OI 140

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 733 2026-11-11 (5DTE): 501 traded vs OI 237
- **SPY** PUT 728 2026-11-10 (4DTE): 507 traded vs OI 373
- **SPY** CALL 805 2026-11-17 (11DTE): 589 traded vs OI 11
- **SPY** CALL 739 2026-11-18 (12DTE): 510 traded vs OI 0
- **SPY** CALL 763 2026-11-13 (7DTE): 917 traded vs OI 916
- **QQQ** PUT 595 2026-11-10 (4DTE): 642 traded vs OI 24
- **QQQ** CALL 694 2026-11-13 (7DTE): 501 traded vs OI 251
- **IWM** PUT 257.5 2026-11-09 (3DTE): 677 traded vs OI 1
- **SMH** CALL 500 2026-11-13 (7DTE): 527 traded vs OI 150
- **SMH** PUT 452.5 2026-11-06 (0DTE): 919 traded vs OI 23
- **NVDA** PUT 170 2026-12-04 (28DTE): 569 traded vs OI 0
- **AAPL** PUT 322.5 2026-11-09 (3DTE): 569 traded vs OI 132
- **AMD** PUT 397.5 2026-11-06 (0DTE): 750 traded vs OI 19
- **AVGO** CALL 295 2026-11-09 (3DTE): 506 traded vs OI 5
- **COIN** PUT 120 2026-11-20 (14DTE): 2,224 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
