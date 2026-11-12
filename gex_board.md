# GEX + FLOW SCAN - Thu Nov 12, 10:10 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (4)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 09:50 | **HOOD** | **PUTS** | TREND + FLOW | 11/13 79P | 0.55 | 0.56 | +5% (19m) | **+2%** | +92% | 80 |
| 09:45 | **ORCL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/13 130C | 0.75 | 0.38 | -1% (8m) | **-49%** | +59% | 126.9 |
| 09:45 | **SMCI** | **PUTS** | TREND + FLOW | 11/13 27P | 0.42 | 0.29 | -5% (6m) | **-31%** | +57% | 27 |
| 09:45 | **SPY** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/12 753P | 0.79 | 0.92 | +23% (18m) | **+16%** | +51% | 754.88 |

## 1m RULES on SPY / QQQ - loose (1 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:10:08 ET, last candle SPY 10:09, QQQ 10:09 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 10:03 | SPY | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **NVDA** | 160.25 | RUN: clean trend + negative gamma + flow agrees | **PUTS** | 80 | none: 48 puts 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (5 contracts' greeks worked out here) | NEG -$202.8M | - | 170 | 160 | -$71.7M | +$7.6M bull / -$11.1M bear | SHORT (clean 33, ADX 44, RVol 3.6) |
| 2 | **DELL** | 354.91 | TREND + FLOW | **PUTS** | 57 | none: 29 puts 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (9 contracts' greeks worked out here) | POS +$440k | 354.18 | 360 | 340 | -$1.0M | +$65k bull / -$96k bear | SHORT (clean 38, ADX 39, RVol 2.2) |
| 3 | **AVGO** | 359.47 | TREND + FLOW | **CALLS** | 49 | none: 83 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (2 contracts' greeks worked out here) | POS +$129.4M | - | 350 | 350 | +$2.5M | +$699k bull / -$822k bear | LONG (clean 37, ADX 44, RVol 2.7) |
| 4 | **MU** | 769.08 | FLOW SURGE | **CALLS** | 49 | none: 134 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (9 contracts' greeks worked out here) | POS +$75.0M | - | 800 | 750 | +$50.0M | +$10.2M bull / +$0 bear | SHORT (clean 33, ADX 40, RVol 1.6) |
| 5 | **AMZN** | 271.37 | FLOW SURGE | **PUTS** | 43 | none: 66 puts 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (5 contracts' greeks worked out here) | POS +$520.4M | - | 270 | 270 | -$10.2M | +$428k bull / -$728k bear | out (clean 32, ADX 38, RVol 1.4) |
| 6 | **SPY** | 755.95 | RUN: clean trend + negative gamma + flow agrees | **PUTS** | 42 | 11/12 752P @ 0.76 (delta 0.23) = est +74% at 753.23 | NEG -$3.7B | 760.64 | 760 | 760 | -$3.4M | +$1.9M bull / -$939k bear | SHORT (clean 33, ADX 30, RVol 0.7) |
| 7 | **IWM** | 279.59 | TREND (flow not with it) | **PUTS** | 42 | 11/12 279P @ 0.56 (delta 0.38) = est +22% at 279 | NEG -$1.2B | 282.93 | 285 | 275 | +$3.2M | - | SHORT (clean 35, ADX 46, RVol 1.6) |
| 8 | **SMCI** | 27.91 | TREND + FLOW | **PUTS** | 42 | 11/13 27P @ 0.46 (delta 0.34) = est +60% at 27 | POS +$2.7M | - | 30 | 27 | -$88k | - | SHORT (clean 34, ADX 51, RVol 1.4) |
| 9 | **COIN** | 130.50 | FLIP CROSS down into negative gamma | **PUTS** | 37 | none: 26 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (6 contracts' greeks worked out here) | NEG -$3.1M | 130.63 | 137 | 130 | +$221k | - | out (clean 31, ADX 44, RVol 1.0) |
| 10 | **PLTR** | 170.03 | PINNED between the walls (positive gamma) - chop | **-** | 36 | - | POS +$84.1M | - | 170 | 170 | -$136k | +$0 bull / -$65k bear | out (clean 28, ADX 35, RVol 1.1) |
| 11 | **AMD** | 558.58 | - | **-** | 29 | - | POS +$155.5M | - | 600 | 550 | +$25.0M | +$9.6M bull / +$0 bear | out (clean 35, ADX 30, RVol 2.7) |
| 12 | **META** | 619.23 | - | **-** | 28 | - | NEG -$30.3M | 624.09 | 650 | 600 | +$3.2M | +$661k bull / +$0 bear | out (clean 30, ADX 54, RVol 1.1) |
| 13 | **MSFT** | 524.84 | - | **-** | 28 | - | POS +$123.9M | 519.29 | 535 | 520 | -$4.3M | +$203k bull / -$276k bear | out (clean 32, ADX 36, RVol 1.1) |
| 14 | **QQQ** | 684.20 | TREND (flow not with it) | **PUTS** | 25 | none: 706 puts 0-7DTE > 66 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (232 contracts' greeks worked out here) | NEG -$1.0B | 689.82 | 700 | 680 | +$210k | +$4.3M bull / -$292k bear | SHORT (clean 32, ADX 39, RVol 0.9) |
| 15 | **SMH** | 493.22 | - | **-** | 25 | - | NEG -$183.1M | - | 500 | 475 | +$1.0M | +$986k bull / +$0 bear | out (clean 32, ADX 46, RVol 0.9) |
| 16 | **TSLA** | 390.43 | - | **-** | 24 | - | POS +$331.5M | - | 400 | 380 | +$14.9M | +$1.9M bull / -$66k bear | out (clean 30, ADX 26, RVol 0.9) |
| 17 | **AAPL** | 358.24 | - | **-** | 24 | - | POS +$1.1B | 338.76 | 360 | 360 | -$2.2M | +$0 bull / -$91k bear | out (clean 28, ADX 49, RVol 1.1) |
| 18 | **HOOD** | 81.63 | TREND (flow not with it) | **PUTS** | 24 | 11/13 79P @ 0.58 (delta 0.24) = est +72% at 80 | POS +$5.9M | 79.99 | 85 | 80 | +$49k | - | SHORT (clean 35, ADX 30, RVol 0.7) |
| 19 | **MSTR** | 113.79 | - | **-** | 22 | - | NEG -$32.3M | - | 125 | 110 | +$35k | +$27k bull / -$68k bear | out (clean 28, ADX 39, RVol 2.6) |
| 20 | **GOOGL** | 294.00 | - | **-** | 20 | - | POS +$82.0M | 288.64 | 300 | 290 | -$16k | +$222k bull / +$0 bear | out (clean 30, ADX 27, RVol 2.3) |
| 21 | **BABA** | 94.39 | - | **-** | 20 | - | NEG -$16.2M | - | 100 | 100 | +$155k | - | out (clean 29, ADX 47, RVol 4.8) |
| 22 | **SHOP** | 147.68 | - | **-** | 18 | - | POS +$4.9M | 142.86 | 150 | 140 | -$3k | - | out (clean 31, ADX 28, RVol 2.0) |
| 23 | **UBER** | 69.28 | - | **-** | 16 | - | POS +$12.0M | 68.18 | 70 | 70 | +$22k | - | out (clean 31, ADX 31, RVol 1.1) |
| 24 | **NFLX** | 63.05 | - | **-** | 13 | - | NEG -$15.5M | 63.93 | 65 | 60 | -$82k | - | out (clean 27, ADX 37, RVol 1.0) |
| 25 | **ORCL** | 124.03 | - | **-** | 12 | - | POS +$7.1M | 120.04 | 130 | 125 | -$238k | - | out (clean 30, ADX 32, RVol 1.2) |
| 26 | **CRM** | 215.32 | - | **-** | 8 | - | NEG -$9.2M | - | 220 | 220 | -$8k | - | out (clean 28, ADX 29, RVol 0.9) |
| 27 | **ARM** | 196.71 | - | **-** | 7 | - | POS +$6.4M | - | 200 | 200 | -$5k | - | out (clean 31, ADX 29, RVol 0.6) |

## Big prints this scan (312)
- **SPY** PUT 763 2026-11-16 (4DTE): 500 @ 7.25 = **+$362k** SELL | vol 2,982 / OI 216
- **TSLA** PUT 395 2026-11-16 (4DTE): 450 @ 6.75 = **+$304k** SELL | vol 657 / OI 51
- **SPY** PUT 763 2026-11-16 (4DTE): 401 @ 7.25 = **+$291k** SELL | vol 2,982 / OI 216
- **AMD** CALL 560 2026-11-18 (6DTE): 98 @ 28.00 = **+$274k** BUY | vol 371 / OI 63
- **NVDA** CALL 160 2026-11-13 (1DTE): 500 @ 5.45 = **+$272k** BUY | vol 87,119 / OI 2,015
- **QQQ** CALL 686 2026-11-12 (0DTE): 698 @ 3.73 = **+$260k** BUY | vol 23,607 / OI 503
- **NVDA** PUT 162.5 2026-11-13 (1DTE): 488 @ 4.38 = **+$214k** SELL | vol 8,011 / OI 20,581
- **SPY** CALL 730 2026-11-13 (1DTE): 76 @ 28.01 = **+$213k** BUY | vol 83 / OI 685
- **QQQ** PUT 700 2026-11-13 (1DTE): 150 @ 13.28 = **+$199k** SELL | vol 426 / OI 2,829
- **SPY** CALL 757 2026-11-13 (1DTE): 442 @ 4.26 = **+$188k** BUY | vol 6,460 / OI 1,638
- **NVDA** PUT 160 2026-11-13 (1DTE): 500 @ 3.45 = **+$172k** SELL | vol 43,252 / OI 24,121
- **SPY** CALL 757 2026-11-13 (1DTE): 407 @ 4.23 = **+$172k** BUY | vol 6,460 / OI 1,638
- **QQQ** PUT 687 2026-11-12 (0DTE): 492 @ 3.25 = **+$160k** SELL | vol 18,392 / OI 97
- **NVDA** PUT 160 2026-11-13 (1DTE): 451 @ 3.14 = **+$142k** SELL | vol 43,252 / OI 24,121
- **SMH** CALL 497.5 2026-11-13 (1DTE): 185 @ 7.50 = **+$139k** BUY | vol 1,034 / OI 195

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 763 2026-11-12 (0DTE): 581 traded vs OI 326
- **SPY** PUT 734 2026-11-12 (0DTE): 1,319 traded vs OI 730
- **SPY** PUT 756 2026-11-16 (4DTE): 515 traded vs OI 256
- **SPY** CALL 772 2026-11-12 (0DTE): 1,105 traded vs OI 959
- **SPY** PUT 718 2026-11-12 (0DTE): 731 traded vs OI 721
- **SPY** CALL 804 2026-11-16 (4DTE): 504 traded vs OI 68
- **SPY** CALL 761 2026-11-16 (4DTE): 563 traded vs OI 304
- **SPY** CALL 759 2026-11-16 (4DTE): 1,061 traded vs OI 743
- **QQQ** PUT 690 2026-11-16 (4DTE): 548 traded vs OI 417
- **QQQ** CALL 694 2026-11-13 (1DTE): 987 traded vs OI 961
- **QQQ** CALL 678 2026-11-12 (0DTE): 523 traded vs OI 508
- **IWM** CALL 282 2026-11-17 (5DTE): 509 traded vs OI 318
- **IWM** PUT 279 2026-11-20 (8DTE): 8,649 traded vs OI 6,879
- **SMH** CALL 497.5 2026-11-13 (1DTE): 1,034 traded vs OI 195
- **NVDA** CALL 162.5 2026-11-23 (11DTE): 550 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
