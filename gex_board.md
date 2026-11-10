# GEX + FLOW SCAN - Tue Nov 10, 11:15 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (6)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:12 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 669P | 0.74 | 0.58 | -1% (0m) | **-22%** | +38% | 671.74 |
| 11:12 | **SPY** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 744P | 0.64 | 0.49 | -2% (0m) | **-23%** | +40% | 745.88 |
| 11:06 | **SPY** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 744P | 0.68 | 0.49 | +12% (0m) | **-28%** | +49% | 745.54 |
| 10:15 | **IWM** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/10 280P | 0.63 | 1.36 | +232% (36m) | **+116%** | +22% | 280 hit |
| 09:50 | **SPY** | **PUTS** | FLOW SURGE | 11/10 743P | 0.77 | 0.62 | +21% (60m) | **-19%** (done) | +54% | 745.65 |
| 09:45 | **IWM** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/10 279P | 0.52 | 0.95 | +90% (60m) | **+83%** (done) | +87% | 278.66 |

## 1m RULES on SPY / QQQ - loose (4 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 11:15:08 ET, last candle SPY 11:14, QQQ 11:14 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 11:14 | QQQ | 1m FAILED POP | R3 R4 | PUTS | TURNING your way | 5-minute cooldown |
| 11:11 | QQQ | 1m FAILED POP | R3 R4 | PUTS | TURNING your way | **FIRE** QQQ261110P00669000 |
| 11:11 | SPY | 1m FAILED POP | R3 R4 | PUTS | TURNING your way | **FIRE** SPY261110P00744000 |
| 11:05 | SPY | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | **FIRE** SPY261110P00744000 |

## Flow surges NOT fired - price disagreed (6 today, last 5)
- 10:15 BABA PUTS: price +0.24 over the last 15 min - flow says one way, price says the other
- 10:10 BABA PUTS: price +0.73 over the last 15 min - flow says one way, price says the other
- 10:00 NFLX CALLS: price -0.14 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:00 AAPL CALLS: price -2.97 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 09:55 BABA CALLS: price -0.98 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **IWM** | 278.72 | TREND (flow not with it) | **PUTS** | 39 | 11/10 279P @ 0.75 (delta 0.57) = est +121% at 277.34 | NEG -$1.3B | 283.4 | 280 | 270 | +$3.7M | +$0 bull / -$204k bear | SHORT (clean 36, ADX 47, RVol 0.8) |
| 2 | **AAPL** | 347.53 | - | **-** | 27 | - | POS +$402.2M | 336.06 | 350 | 340 | +$17.8M | +$66k bull / -$76k bear | out (clean 28, ADX 18, RVol 0.7) |
| 3 | **ARM** | 180.94 | - | **-** | 24 | - | NEG -$5.0M | - | 185 | 190 | -$154k | +$0 bull / -$112k bear | out (clean 27, ADX 29, RVol 1.0) |
| 4 | **AMD** | 528.32 | - | **-** | 23 | - | POS +$48.6M | - | 500 | 500 | -$69.0M | +$0 bull / -$3.8M bear | out (clean 31, ADX 25, RVol 0.9) |
| 5 | **NVDA** | 169.42 | - | **-** | 22 | - | NEG -$173.8M | - | 185 | 170 | -$6.7M | +$448k bull / -$7.0M bear | out (clean 32, ADX 35, RVol 2.5) |
| 6 | **GOOGL** | 287.81 | - | **-** | 21 | - | NEG -$12.0M | 289.3 | 300 | 290 | +$2.2M | +$278k bull / +$0 bear | out (clean 30, ADX 16, RVol 1.1) |
| 7 | **AVGO** | 329.08 | - | **-** | 21 | - | NEG -$11.7M | 343.15 | 340 | 340 | -$9.7M | +$54k bull / -$536k bear | out (clean 31, ADX 22, RVol 1.1) |
| 8 | **AMZN** | 269.30 | - | **-** | 20 | - | POS +$469.2M | - | 270 | 265 | +$7.6M | +$376k bull / +$0 bear | out (clean 33, ADX 23, RVol 0.5) |
| 9 | **PLTR** | 167.16 | - | **-** | 20 | - | POS +$53.4M | - | 165 | 170 | -$175k | +$0 bull / -$52k bear | out (clean 28, ADX 47, RVol 0.6) |
| 10 | **MSTR** | 121.43 | - | **-** | 20 | - | NEG -$5.4M | 124.01 | 133 | 120 | -$613k | +$63k bull / -$29k bear | out (clean 29, ADX 32, RVol 1.6) |
| 11 | **SPY** | 747.52 | - | **-** | 19 | - | NEG -$7.0B | 760.09 | 750 | 730 | +$24.6M | +$2.5M bull / -$1.6M bear | out (clean 32, ADX 33, RVol 1.1) |
| 12 | **TSLA** | 377.70 | - | **-** | 18 | - | POS +$194.5M | - | 400 | 380 | -$11.9M | +$0 bull / -$2.3M bear | out (clean 34, ADX 27, RVol 0.3) |
| 13 | **DELL** | 333.62 | - | **-** | 17 | - | NEG -$8.8M | - | 350 | 340 | +$46k | +$46k bull / -$142k bear | out (clean 32, ADX 28, RVol 1.2) |
| 14 | **SHOP** | 147.21 | - | **-** | 17 | - | POS +$888k | 145.26 | 150 | 140 | +$25k | - | out (clean 32, ADX 40, RVol 0.6) |
| 15 | **QQQ** | 673.94 | - | **-** | 16 | - | NEG -$1.9B | 692.32 | 680 | 680 | -$20.7M | +$0 bull / -$2.4M bear | out (clean 31, ADX 24, RVol 0.6) |
| 16 | **SMH** | 483.22 | - | **-** | 16 | - | NEG -$205.6M | - | 500 | 475 | -$680k | +$0 bull / -$390k bear | out (clean 29, ADX 19, RVol 0.5) |
| 17 | **MU** | 716.25 | - | **-** | 16 | - | NEG -$30.5M | - | 750 | 750 | -$754k | +$725k bull / -$3.5M bear | out (clean 30, ADX 23, RVol 0.9) |
| 18 | **CRM** | 212.16 | - | **-** | 15 | - | NEG -$10.4M | - | 195 | 220 | -$81k | - | out (clean 30, ADX 39, RVol 0.2) |
| 19 | **META** | 641.70 | - | **-** | 14 | - | POS +$256.3M | 605.69 | 650 | 650 | +$155k | +$267k bull / -$66k bear | out (clean 32, ADX 19, RVol 0.4) |
| 20 | **HOOD** | 81.12 | - | **-** | 14 | - | POS +$3.1M | 79.21 | 85 | 80 | +$545k | - | out (clean 30, ADX 36, RVol 0.5) |
| 21 | **BABA** | 103.33 | - | **-** | 14 | - | NEG -$7.8M | 106.11 | 110 | 100 | -$333k | - | out (clean 29, ADX 35, RVol 0.5) |
| 22 | **COIN** | 130.88 | - | **-** | 11 | - | POS +$2.1M | 129.49 | 137 | 135 | +$201k | - | out (clean 30, ADX 36, RVol 0.7) |
| 23 | **MSFT** | 542.48 | - | **-** | 10 | - | POS +$682.3M | - | 550 | 535 | -$483k | - | out (clean 32, ADX 35, RVol 1.0) |
| 24 | **UBER** | 69.50 | - | **-** | 9 | - | POS +$5.7M | 68.45 | 70 | 70 | -$8k | - | out (clean 33, ADX 41, RVol 0.7) |
| 25 | **NFLX** | 62.70 | - | **-** | 8 | - | NEG -$22.5M | 65.65 | 65 | 60 | -$115k | - | out (clean 30, ADX 31, RVol 0.7) |
| 26 | **SMCI** | 28.01 | - | **-** | 8 | - | POS +$3.4M | - | 30 | 30 | -$69k | - | out (clean 29, ADX 23, RVol 0.5) |
| 27 | **ORCL** | 118.64 | - | **-** | 6 | - | NEG -$23.6M | - | 130 | 120 | -$23k | - | out (clean 28, ADX 29, RVol 0.2) |

## Big prints this scan (118)
- **QQQ** CALL 672 2026-11-10 (0DTE): 999 @ 3.05 = **+$305k** SELL | vol 25,504 / OI 3,705
- **NVDA** PUT 177.5 2026-11-13 (3DTE): 234 @ 10.45 = **+$245k** BUY | vol 2,640 / OI 2,794
- **QQQ** CALL 674 2026-11-10 (0DTE): 999 @ 1.98 = **+$198k** SELL | vol 61,689 / OI 417
- **AMD** CALL 525 2026-11-11 (1DTE): 177 @ 10.60 = **+$188k** SELL | vol 6,399 / OI 146
- **NVDA** PUT 177.5 2026-11-13 (3DTE): 166 @ 10.45 = **+$173k** BUY | vol 2,640 / OI 2,794
- **NVDA** CALL 167.5 2026-11-13 (3DTE): 300 @ 4.80 = **+$144k** SELL | vol 3,497 / OI 18
- **NVDA** CALL 167.5 2026-11-13 (3DTE): 300 @ 4.79 = **+$144k** SELL | vol 3,497 / OI 18
- **NVDA** CALL 167.5 2026-11-13 (3DTE): 300 @ 4.79 = **+$144k** SELL | vol 3,497 / OI 18
- **NVDA** CALL 167.5 2026-11-13 (3DTE): 280 @ 5.10 = **+$143k** SELL | vol 3,497 / OI 18
- **IWM** CALL 279 2026-11-11 (1DTE): 1,000 @ 1.40 = **+$140k** SELL | vol 2,837 / OI 392
- **NVDA** CALL 170 2026-11-13 (3DTE): 380 @ 3.55 = **+$135k** SELL | vol 11,403 / OI 389
- **AMD** PUT 520 2026-11-11 (1DTE): 120 @ 11.20 = **+$134k** BUY | vol 3,460 / OI 31
- **NVDA** PUT 167.5 2026-11-13 (3DTE): 300 @ 4.36 = **+$131k** BUY | vol 10,866 / OI 1,236
- **NVDA** PUT 167.5 2026-11-13 (3DTE): 300 @ 4.35 = **+$130k** BUY | vol 10,866 / OI 1,236
- **NVDA** PUT 167.5 2026-11-13 (3DTE): 300 @ 4.34 = **+$130k** BUY | vol 10,866 / OI 1,236

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 729 2026-11-12 (2DTE): 638 traded vs OI 633
- **SPY** PUT 726 2026-11-13 (3DTE): 1,095 traded vs OI 988
- **SPY** PUT 741 2026-11-12 (2DTE): 512 traded vs OI 248
- **SPY** CALL 756 2026-11-12 (2DTE): 596 traded vs OI 485
- **SPY** PUT 763 2026-11-10 (0DTE): 518 traded vs OI 0
- **SPY** CALL 757 2026-11-12 (2DTE): 506 traded vs OI 485
- **SPY** CALL 779 2026-11-13 (3DTE): 3,409 traded vs OI 1,591
- **SPY** PUT 760 2026-12-04 (24DTE): 966 traded vs OI 863
- **QQQ** CALL 681 2026-11-13 (3DTE): 739 traded vs OI 721
- **QQQ** PUT 667 2026-11-12 (2DTE): 506 traded vs OI 67
- **QQQ** PUT 673 2026-11-12 (2DTE): 503 traded vs OI 90
- **QQQ** CALL 699 2026-11-11 (1DTE): 510 traded vs OI 178
- **QQQ** CALL 698 2026-11-11 (1DTE): 848 traded vs OI 324
- **QQQ** PUT 638 2026-11-11 (1DTE): 511 traded vs OI 64
- **QQQ** PUT 669 2026-11-13 (3DTE): 533 traded vs OI 400

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
