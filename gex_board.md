# GEX + FLOW SCAN - Thu Nov 12, 10:00 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (4)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 09:50 | **HOOD** | **PUTS** | TREND + FLOW | 11/13 79P | 0.55 | 0.42 | -9% (4m) | **-24%** | +92% | 80 |
| 09:45 | **ORCL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/13 130C | 0.75 | 0.59 | -1% (8m) | **-21%** | +59% | 126.9 |
| 09:45 | **SMCI** | **PUTS** | TREND + FLOW | 11/13 27P | 0.42 | 0.27 | -5% (6m) | **-36%** | +57% | 27 |
| 09:45 | **SPY** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/12 753P | 0.79 | 0.60 | +6% (1m) | **-24%** | +51% | 754.88 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:00:08 ET, last candle SPY 09:59, QQQ 09:59 | no errors

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **NVDA** | 162.62 | RUN: clean trend + negative gamma + flow agrees | **PUTS** | 82 | none: 45 puts 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (3 contracts' greeks worked out here) | NEG -$186.1M | - | 170 | 160 | -$68.0M | +$1.5M bull / -$34.7M bear | SHORT (clean 34, ADX 44, RVol 5.7) |
| 2 | **DELL** | 363.34 | TREND + FLOW | **PUTS** | 69 | none: 29 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (4 contracts' greeks worked out here) | POS +$4.0M | - | 360 | 340 | -$1.5M | +$0 bull / -$792k bear | SHORT (clean 38, ADX 40, RVol 3.5) |
| 3 | **AMD** | 566.97 | TREND + FLOW | **CALLS** | 63 | none: 135 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (5 contracts' greeks worked out here) | POS +$185.4M | - | 600 | 550 | +$18.4M | +$7.2M bull / -$3.1M bear | LONG (clean 35, ADX 32, RVol 4.1) |
| 4 | **AVGO** | 361.86 | TREND + FLOW | **CALLS** | 63 | none: 81 calls 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (3 contracts' greeks worked out here) | POS +$132.0M | - | 350 | 350 | +$3.1M | +$1.6M bull / -$97k bear | LONG (clean 37, ADX 46, RVol 5.3) |
| 5 | **SPY** | 757.79 | RUN: clean trend + negative gamma + flow agrees | **PUTS** | 60 | 11/12 753P @ 0.77 (delta 0.22) = est +56% at 755.21 | NEG -$2.9B | 760.89 | 760 | 760 | -$28.8M | +$321k bull / -$3.6M bear | SHORT (clean 33, ADX 30, RVol 1.0) |
| 6 | **SMCI** | 28.20 | TREND + FLOW | **PUTS** | 54 | 11/13 27.5P @ 0.47 (delta 0.35) = est +96% at 27 | POS +$3.5M | - | 30 | 27 | -$76k | - | SHORT (clean 34, ADX 50, RVol 2.6) |
| 7 | **AMZN** | 273.05 | FLOW SURGE | **PUTS** | 53 | none: 66 puts 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (15 contracts' greeks worked out here) | POS +$548.6M | - | 270 | 270 | -$11.5M | +$0 bull / -$948k bear | out (clean 32, ADX 34, RVol 2.0) |
| 8 | **ORCL** | 125.22 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 48 | 11/13 129C @ 0.77 (delta 0.24) = est +66% at 127.25 | POS +$8.3M | 120.52 | 130 | 125 | -$317k | +$0 bull / -$558k bear | out (clean 30, ADX 28, RVol 1.8) |
| 9 | **MU** | 779.13 | FLOW SURGE | **CALLS** | 47 | none: 128 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (3 contracts' greeks worked out here) | POS +$84.4M | - | 800 | 750 | +$25.8M | +$9.2M bull / -$6.7M bear | SHORT (clean 33, ADX 37, RVol 1.8) |
| 10 | **AAPL** | 358.81 | FLOW SURGE | **PUTS** | 45 | none: 79 puts 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (8 contracts' greeks worked out here) | POS +$1.2B | 338.13 | 360 | 360 | -$3.4M | +$97k bull / -$332k bear | out (clean 28, ADX 45, RVol 1.7) |
| 11 | **MSFT** | 525.92 | FLOW SURGE | **PUTS** | 44 | none: 126 puts 0-7DTE > 16 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (26 contracts' greeks worked out here) | POS +$128.5M | 519.1 | 535 | 520 | -$5.6M | +$0 bull / -$4.6M bear | out (clean 32, ADX 36, RVol 1.2) |
| 12 | **IWM** | 279.86 | TREND (flow not with it) | **PUTS** | 43 | 11/12 279P @ 0.55 (delta 0.35) = est +40% at 279 | NEG -$1.2B | 282.96 | 285 | 275 | +$1.9M | +$50k bull / +$0 bear | SHORT (clean 35, ADX 39, RVol 2.2) |
| 13 | **HOOD** | 82.45 | TREND + FLOW | **PUTS** | 39 | 11/13 79P @ 0.52 (delta 0.21) = est +116% at 80 | POS +$7.3M | 79.9 | 85 | 80 | -$25k | - | SHORT (clean 35, ADX 28, RVol 2.0) |
| 14 | **QQQ** | 687.77 | TREND (flow not with it) | **PUTS** | 37 | none: 697 puts 0-7DTE > 66 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (283 contracts' greeks worked out here) | NEG -$702.5M | 690.4 | 700 | 680 | +$11.3M | +$3.7M bull / -$4.3M bear | SHORT (clean 33, ADX 39, RVol 1.0) |
| 15 | **META** | 626.63 | - | **-** | 31 | - | POS +$10.7M | 623.96 | 650 | 600 | +$2.9M | +$1.2M bull / -$65k bear | out (clean 30, ADX 53, RVol 1.6) |
| 16 | **SHOP** | 147.63 | - | **-** | 28 | - | POS +$3.0M | 143.92 | 150 | 140 | -$2k | - | out (clean 32, ADX 26, RVol 2.1) |
| 17 | **UBER** | 69.84 | PINNED between the walls (positive gamma) - chop | **-** | 25 | - | POS +$15.2M | 68.34 | 70 | 70 | +$2k | - | out (clean 31, ADX 29, RVol 1.3) |
| 18 | **TSLA** | 392.46 | - | **-** | 24 | - | POS +$358.8M | - | 400 | 380 | +$12.4M | +$2.1M bull / -$1.4M bear | out (clean 31, ADX 26, RVol 1.1) |
| 19 | **COIN** | 131.59 | - | **-** | 24 | - | POS +$445k | 130.51 | 137 | 135 | +$176k | - | out (clean 31, ADX 44, RVol 1.2) |
| 20 | **SMH** | 497.88 | - | **-** | 23 | - | NEG -$149.1M | - | 500 | 475 | +$470k | +$186k bull / -$1.4M bear | out (clean 32, ADX 45, RVol 0.8) |
| 21 | **MSTR** | 114.00 | - | **-** | 23 | - | NEG -$31.9M | - | 125 | 110 | +$125k | +$104k bull / -$134k bear | out (clean 28, ADX 36, RVol 3.4) |
| 22 | **BABA** | 94.71 | - | **-** | 22 | - | NEG -$18.2M | - | 100 | 100 | +$164k | - | out (clean 29, ADX 42, RVol 6.5) |
| 23 | **GOOGL** | 296.86 | - | **-** | 21 | - | POS +$103.8M | 288.82 | 300 | 290 | -$199k | +$75k bull / -$140k bear | out (clean 30, ADX 29, RVol 3.8) |
| 24 | **PLTR** | 170.93 | - | **-** | 20 | - | POS +$85.5M | - | 170 | 170 | -$76k | +$0 bull / -$55k bear | out (clean 28, ADX 32, RVol 1.3) |
| 25 | **NFLX** | 63.45 | - | **-** | 18 | - | NEG -$12.1M | 64.05 | 65 | 65 | -$152k | - | out (clean 27, ADX 36, RVol 1.0) |
| 26 | **ARM** | 200.52 | - | **-** | 14 | - | POS +$9.2M | - | 200 | 200 | -$97k | - | out (clean 31, ADX 27, RVol 1.4) |
| 27 | **CRM** | 215.24 | - | **-** | 10 | - | NEG -$8.4M | 227.4 | 210 | 220 | -$14k | - | out (clean 28, ADX 26, RVol 1.3) |

## Big prints this scan (381)
- **AMD** CALL 560 2026-11-13 (1DTE): 500 @ 19.45 = **+$972k** BUY | vol 2,577 / OI 2,043
- **AMD** PUT 575 2026-11-13 (1DTE): 494 @ 15.45 = **+$763k** SELL | vol 2,450 / OI 31
- **NVDA** CALL 165 2026-11-13 (1DTE): 3,200 @ 2.38 = **+$762k** SELL | vol 59,590 / OI 2,999
- **AMD** PUT 575 2026-11-13 (1DTE): 500 @ 12.20 = **+$610k** SELL | vol 2,450 / OI 31
- **SPY** PUT 762 2026-11-12 (0DTE): 852 @ 5.29 = **+$451k** BUY | vol 1,900 / OI 594
- **NVDA** PUT 167.5 2026-11-13 (1DTE): 450 @ 9.77 = **+$440k** BUY | vol 4,360 / OI 6,383
- **SPY** PUT 761 2026-11-12 (0DTE): 852 @ 4.49 = **+$383k** BUY | vol 1,942 / OI 178
- **QQQ** PUT 695 2026-11-13 (1DTE): 292 @ 9.60 = **+$280k** SELL | vol 2,229 / OI 4,281
- **NVDA** PUT 155 2026-11-13 (1DTE): 1,000 @ 2.50 = **+$250k** BUY | vol 38,945 / OI 9,956
- **QQQ** CALL 687 2026-11-13 (1DTE): 386 @ 5.84 = **+$225k** BUY | vol 3,853 / OI 923
- **QQQ** CALL 687 2026-11-13 (1DTE): 377 @ 5.70 = **+$215k** BUY | vol 3,853 / OI 923
- **SPY** CALL 755 2026-11-12 (0DTE): 566 @ 3.78 = **+$214k** BUY | vol 22,493 / OI 1,837
- **QQQ** CALL 687 2026-11-13 (1DTE): 324 @ 5.78 = **+$187k** BUY | vol 3,853 / OI 923
- **QQQ** PUT 695 2026-11-13 (1DTE): 195 @ 9.58 = **+$187k** SELL | vol 2,229 / OI 4,281
- **QQQ** CALL 680 2026-11-12 (0DTE): 200 @ 9.19 = **+$184k** BUY | vol 3,375 / OI 2,244

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 716 2026-11-12 (0DTE): 1,552 traded vs OI 698
- **SPY** CALL 763 2026-11-13 (1DTE): 3,619 traded vs OI 2,717
- **SPY** PUT 731 2026-11-12 (0DTE): 1,379 traded vs OI 868
- **SPY** PUT 757 2026-11-13 (1DTE): 1,844 traded vs OI 1,593
- **SPY** CALL 797 2026-11-18 (6DTE): 800 traded vs OI 196
- **SPY** CALL 774 2026-11-12 (0DTE): 882 traded vs OI 647
- **QQQ** PUT 676 2026-11-13 (1DTE): 2,340 traded vs OI 1,238
- **QQQ** CALL 695 2026-11-13 (1DTE): 8,226 traded vs OI 5,374
- **QQQ** PUT 685 2026-11-16 (4DTE): 627 traded vs OI 435
- **QQQ** CALL 682 2026-11-13 (1DTE): 1,040 traded vs OI 987
- **QQQ** PUT 640 2026-11-16 (4DTE): 2,061 traded vs OI 1,127
- **QQQ** CALL 712 2026-11-12 (0DTE): 560 traded vs OI 91
- **QQQ** PUT 688 2026-11-13 (1DTE): 668 traded vs OI 307
- **QQQ** CALL 679 2026-11-12 (0DTE): 621 traded vs OI 427
- **QQQ** PUT 683 2026-11-13 (1DTE): 629 traded vs OI 271

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
