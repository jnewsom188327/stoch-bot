# GEX + FLOW SCAN - Tue Nov 10, 11:20 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (8)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:18 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 668P | 0.74 | 0.54 | -3% (0m) | **-27%** | +18% | 672.3 |
| 11:17 | **SPY** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 744P | 0.60 | 0.55 | +22% (1m) | **-8%** | +41% | 746.01 |
| 11:12 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 669P | 0.74 | 0.68 | +14% (6m) | **-8%** | +38% | 671.74 |
| 11:12 | **SPY** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 744P | 0.64 | 0.55 | +14% (6m) | **-14%** | +40% | 745.88 |
| 11:06 | **SPY** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 744P | 0.68 | 0.55 | +12% (0m) | **-19%** | +49% | 745.54 |
| 10:15 | **IWM** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/10 280P | 0.63 | 1.39 | +232% (36m) | **+121%** (done) | +22% | 280 hit |
| 09:50 | **SPY** | **PUTS** | FLOW SURGE | 11/10 743P | 0.77 | 0.62 | +21% (60m) | **-19%** (done) | +54% | 745.65 |
| 09:45 | **IWM** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/10 279P | 0.52 | 0.95 | +90% (60m) | **+83%** (done) | +87% | 278.66 |

## 1m RULES on SPY / QQQ - loose (6 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 11:20:08 ET, last candle SPY 11:19, QQQ 11:19 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 11:17 | QQQ | 1m FAILED POP | R3 R4 | PUTS | TURNING your way | **FIRE** QQQ261110P00668000 |
| 11:16 | SPY | 1m FAILED POP | R3 R4 | PUTS | TURNING your way | **FIRE** SPY261110P00744000 |
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
| 1 | **IWM** | 278.79 | TREND (flow not with it) | **PUTS** | 38 | 11/10 279P @ 0.77 (delta 0.55) = est +107% at 277.44 | NEG -$1.3B | 283.63 | 280 | 270 | +$3.5M | +$0 bull / -$204k bear | SHORT (clean 36, ADX 47, RVol 0.8) |
| 2 | **AMZN** | 269.34 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 38 | none: 66 puts 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (6 contracts' greeks worked out here) | POS +$466.5M | - | 270 | 265 | +$7.9M | +$300k bull / +$0 bear | out (clean 33, ADX 22, RVol 0.5) |
| 3 | **AAPL** | 347.24 | - | **-** | 27 | - | POS +$404.4M | 335.8 | 350 | 340 | +$18.0M | +$39k bull / -$76k bear | out (clean 28, ADX 18, RVol 0.7) |
| 4 | **ARM** | 180.95 | - | **-** | 25 | - | NEG -$5.2M | - | 185 | 190 | -$252k | +$0 bull / -$112k bear | out (clean 27, ADX 28, RVol 0.6) |
| 5 | **AMD** | 526.46 | - | **-** | 22 | - | POS +$47.5M | - | 500 | 500 | -$64.7M | +$505k bull / -$3.1M bear | out (clean 31, ADX 23, RVol 1.0) |
| 6 | **NVDA** | 168.91 | - | **-** | 21 | - | NEG -$171.7M | - | 185 | 170 | +$117k | +$1.5M bull / -$5.9M bear | out (clean 32, ADX 35, RVol 2.4) |
| 7 | **GOOGL** | 287.73 | - | **-** | 21 | - | NEG -$13.8M | 289.19 | 300 | 290 | +$2.4M | +$123k bull / +$0 bear | out (clean 30, ADX 16, RVol 1.0) |
| 8 | **AVGO** | 328.62 | - | **-** | 21 | - | NEG -$13.4M | 341.91 | 340 | 320 | -$9.9M | +$0 bull / -$536k bear | out (clean 31, ADX 22, RVol 1.0) |
| 9 | **PLTR** | 167.35 | - | **-** | 20 | - | POS +$54.4M | - | 165 | 170 | -$159k | +$40k bull / +$0 bear | out (clean 28, ADX 47, RVol 0.5) |
| 10 | **SPY** | 747.62 | - | **-** | 19 | - | NEG -$7.3B | 760.74 | 750 | 730 | +$25.9M | +$341k bull / -$1.4M bear | out (clean 32, ADX 33, RVol 0.9) |
| 11 | **SHOP** | 147.23 | - | **-** | 18 | - | POS +$1.5M | 144.44 | 150 | 140 | +$26k | - | out (clean 32, ADX 42, RVol 0.6) |
| 12 | **TSLA** | 376.76 | - | **-** | 17 | - | POS +$194.6M | - | 400 | 380 | -$10.3M | +$69k bull / -$1.7M bear | out (clean 34, ADX 26, RVol 0.2) |
| 13 | **DELL** | 332.92 | - | **-** | 17 | - | NEG -$11.1M | - | 350 | 340 | +$24k | +$0 bull / -$88k bear | out (clean 32, ADX 28, RVol 0.9) |
| 14 | **QQQ** | 673.94 | - | **-** | 16 | - | NEG -$1.9B | 693.04 | 680 | 680 | -$23.3M | +$262k bull / -$1.8M bear | out (clean 31, ADX 24, RVol 0.5) |
| 15 | **SMH** | 482.65 | - | **-** | 16 | - | NEG -$226.0M | - | 500 | 475 | -$607k | +$0 bull / -$278k bear | out (clean 29, ADX 19, RVol 0.5) |
| 16 | **MU** | 715.25 | - | **-** | 16 | - | NEG -$30.6M | - | 750 | 750 | -$4.7M | +$0 bull / -$4.3M bear | out (clean 30, ADX 23, RVol 0.8) |
| 17 | **CRM** | 212.92 | - | **-** | 15 | - | NEG -$11.0M | - | 195 | 220 | -$83k | - | out (clean 30, ADX 38, RVol 0.2) |
| 18 | **META** | 642.63 | - | **-** | 14 | - | POS +$251.7M | 606.4 | 650 | 650 | +$325k | +$336k bull / -$35k bear | out (clean 32, ADX 18, RVol 0.4) |
| 19 | **BABA** | 103.22 | - | **-** | 14 | - | NEG -$8.4M | 106.41 | 110 | 100 | -$328k | - | out (clean 30, ADX 36, RVol 0.5) |
| 20 | **HOOD** | 81.34 | - | **-** | 12 | - | POS +$3.0M | 79.24 | 85 | 80 | +$482k | - | out (clean 30, ADX 35, RVol 0.5) |
| 21 | **MSFT** | 543.08 | - | **-** | 10 | - | POS +$685.5M | - | 550 | 535 | -$497k | - | out (clean 32, ADX 34, RVol 0.8) |
| 22 | **COIN** | 131.36 | - | **-** | 10 | - | POS +$3.1M | 128.95 | 137 | 135 | +$154k | - | out (clean 30, ADX 36, RVol 0.7) |
| 23 | **MSTR** | 121.97 | - | **-** | 10 | - | NEG -$1.9M | 122.79 | 133 | 120 | -$896k | - | out (clean 29, ADX 32, RVol 1.0) |
| 24 | **UBER** | 69.44 | - | **-** | 10 | - | POS +$5.1M | 68.45 | 70 | 70 | -$7k | - | out (clean 33, ADX 42, RVol 0.7) |
| 25 | **NFLX** | 62.67 | - | **-** | 8 | - | NEG -$23.3M | 65.7 | 65 | 60 | -$94k | - | out (clean 30, ADX 31, RVol 0.8) |
| 26 | **SMCI** | 28.11 | - | **-** | 7 | - | POS +$3.3M | - | 30 | 30 | -$72k | - | out (clean 29, ADX 22, RVol 0.5) |
| 27 | **ORCL** | 119.00 | - | **-** | 6 | - | NEG -$22.7M | - | 130 | 120 | -$52k | - | out (clean 28, ADX 28, RVol 0.2) |

## Big prints this scan (87)
- **SPY** CALL 748 2026-11-13 (3DTE): 624 @ 5.46 = **+$341k** BUY | vol 3,264 / OI 1,196
- **QQQ** CALL 672 2026-11-10 (0DTE): 959 @ 2.80 = **+$269k** SELL | vol 26,512 / OI 3,705
- **MU** PUT 725 2026-11-11 (1DTE): 100 @ 22.30 = **+$223k** BUY | vol 3,073 / OI 61
- **NVDA** CALL 167.5 2026-11-16 (6DTE): 350 @ 6.10 = **+$214k** BUY | vol 1,897 / OI 9
- **NVDA** CALL 172.5 2026-11-16 (6DTE): 500 @ 3.85 = **+$192k** BUY | vol 6,849 / OI 10
- **NVDA** CALL 172.5 2026-11-16 (6DTE): 470 @ 4.00 = **+$188k** BUY | vol 6,849 / OI 10
- **QQQ** CALL 675 2026-11-13 (3DTE): 200 @ 7.34 = **+$147k** BUY | vol 2,804 / OI 7,037
- **AMD** CALL 530 2026-11-13 (3DTE): 98 @ 14.55 = **+$143k** SELL | vol 3,373 / OI 1,599
- **MU** CALL 720 2026-11-11 (1DTE): 100 @ 12.40 = **+$124k** SELL | vol 4,466 / OI 279
- **QQQ** CALL 672 2026-11-10 (0DTE): 432 @ 2.84 = **+$123k** SELL | vol 26,512 / OI 3,705
- **QQQ** PUT 670 2026-11-11 (1DTE): 350 @ 3.50 = **+$122k** BUY | vol 16,148 / OI 452
- **AMD** CALL 540 2026-11-13 (3DTE): 108 @ 11.15 = **+$120k** BUY | vol 2,756 / OI 668
- **QQQ** CALL 674 2026-11-10 (0DTE): 480 @ 2.40 = **+$115k** BUY | vol 69,981 / OI 417
- **AMD** CALL 550 2026-11-11 (1DTE): 244 @ 2.99 = **+$73k** SELL | vol 15,219 / OI 176
- **GOOGL** CALL 290 2026-11-13 (3DTE): 200 @ 3.55 = **+$71k** BUY | vol 1,786 / OI 5,801

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 816 2026-11-13 (3DTE): 504 traded vs OI 99
- **SPY** CALL 812 2026-11-13 (3DTE): 801 traded vs OI 368
- **SPY** CALL 814 2026-11-13 (3DTE): 571 traded vs OI 457
- **SPY** CALL 766 2026-11-13 (3DTE): 1,914 traded vs OI 1,867
- **SPY** CALL 758 2026-11-13 (3DTE): 2,139 traded vs OI 2,125
- **SPY** PUT 721 2026-11-12 (2DTE): 542 traded vs OI 269
- **SPY** CALL 787 2026-11-16 (6DTE): 931 traded vs OI 167
- **SPY** PUT 717 2026-11-12 (2DTE): 504 traded vs OI 334
- **SPY** PUT 739 2026-11-12 (2DTE): 507 traded vs OI 409
- **SPY** CALL 809 2026-11-30 (20DTE): 2,500 traded vs OI 1,470
- **QQQ** PUT 649 2026-11-11 (1DTE): 505 traded vs OI 72
- **QQQ** CALL 676 2026-11-12 (2DTE): 547 traded vs OI 143
- **QQQ** PUT 615 2026-11-30 (20DTE): 8,114 traded vs OI 5,230
- **QQQ** CALL 697 2026-11-20 (10DTE): 771 traded vs OI 568
- **IWM** PUT 277.5 2026-11-13 (3DTE): 500 traded vs OI 484

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
