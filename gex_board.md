# GEX + FLOW SCAN - Tue Nov 10, 12:20 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (8)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:18 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 668P | 0.74 | 0.69 | +84% (38m) | **-7%** (done) | +18% | 672.3 hit |
| 11:17 | **SPY** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 744P | 0.60 | 0.36 | +38% (32m) | **-40%** (done) | +41% | 746.01 hit |
| 11:12 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 669P | 0.74 | 1.07 | +135% (44m) | **+45%** (done) | +38% | 671.74 hit |
| 11:12 | **SPY** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 744P | 0.64 | 0.38 | +30% (37m) | **-41%** (done) | +40% | 745.88 |
| 11:06 | **SPY** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 744P | 0.68 | 0.60 | +22% (43m) | **-12%** (done) | +49% | 745.54 |
| 10:15 | **IWM** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/10 280P | 0.63 | 1.39 | +232% (36m) | **+121%** (done) | +22% | 280 hit |
| 09:50 | **SPY** | **PUTS** | FLOW SURGE | 11/10 743P | 0.77 | 0.62 | +21% (60m) | **-19%** (done) | +54% | 745.65 |
| 09:45 | **IWM** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/10 279P | 0.52 | 0.95 | +90% (60m) | **+83%** (done) | +87% | 278.66 |

## 1m RULES on SPY / QQQ - loose (7 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 12:20:08 ET, last candle SPY 12:19, QQQ 12:19 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 11:23 | QQQ | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |
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
| 1 | **NVDA** | 167.54 | TREND (flow not with it) | **PUTS** | 41 | none: 39 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$153.6M | - | 180 | 170 | +$15.5M | +$609k bull / -$3.0M bear | SHORT (clean 33, ADX 40, RVol 1.4) |
| 2 | **SHOP** | 145.01 | FLIP CROSS down into negative gamma | **PUTS** | 38 | none: 23 puts 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$227k | 145.17 | 150 | 140 | +$92k | - | out (clean 33, ADX 58, RVol 0.7) |
| 3 | **AAPL** | 348.08 | - | **-** | 24 | - | POS +$425.5M | 336.36 | 350 | 340 | +$17.4M | +$25k bull / -$80k bear | out (clean 28, ADX 13, RVol 0.3) |
| 4 | **PLTR** | 166.12 | - | **-** | 22 | - | POS +$52.5M | - | 165 | 170 | -$1.0M | +$71k bull / -$1.1M bear | out (clean 28, ADX 39, RVol 0.7) |
| 5 | **AMD** | 510.08 | - | **-** | 19 | - | POS +$48.6M | - | 500 | 500 | -$33.7M | +$1.3M bull / -$3.9M bear | out (clean 32, ADX 28, RVol 0.8) |
| 6 | **SPY** | 747.60 | - | **-** | 18 | - | NEG -$7.2B | 760.42 | 750 | 730 | +$56.2M | +$0 bull / -$647k bear | out (clean 32, ADX 31, RVol 0.5) |
| 7 | **AVGO** | 325.81 | - | **-** | 18 | - | NEG -$18.0M | - | 340 | 320 | -$8.2M | +$0 bull / -$144k bear | out (clean 32, ADX 19, RVol 0.3) |
| 8 | **ORCL** | 117.62 | - | **-** | 18 | - | NEG -$24.5M | - | 120 | 120 | +$394k | +$28k bull / +$0 bear | out (clean 28, ADX 27, RVol 0.3) |
| 9 | **MSFT** | 543.62 | - | **-** | 17 | - | POS +$683.3M | - | 550 | 535 | -$432k | +$0 bull / -$28k bear | out (clean 32, ADX 25, RVol 0.3) |
| 10 | **MU** | 708.92 | - | **-** | 17 | - | NEG -$31.9M | - | 750 | 750 | -$6.4M | +$0 bull / -$2.9M bear | out (clean 30, ADX 28, RVol 0.9) |
| 11 | **QQQ** | 671.23 | - | **-** | 16 | - | NEG -$2.1B | 692.47 | 680 | 680 | +$9.8M | +$702k bull / -$5.5M bear | out (clean 32, ADX 31, RVol 0.2) |
| 12 | **TSLA** | 376.27 | - | **-** | 15 | - | POS +$189.8M | - | 400 | 380 | -$3.4M | +$26k bull / -$992k bear | out (clean 33, ADX 22, RVol 0.3) |
| 13 | **META** | 641.14 | - | **-** | 15 | - | POS +$244.3M | 604.96 | 650 | 650 | +$35k | +$30k bull / -$647k bear | out (clean 32, ADX 20, RVol 0.7) |
| 14 | **CRM** | 212.37 | - | **-** | 15 | - | NEG -$10.8M | - | 195 | 220 | -$103k | - | out (clean 29, ADX 30, RVol 0.4) |
| 15 | **HOOD** | 80.61 | - | **-** | 13 | - | POS +$2.1M | 79.17 | 85 | 80 | +$549k | - | out (clean 31, ADX 38, RVol 0.7) |
| 16 | **ARM** | 177.74 | - | **-** | 13 | - | NEG -$5.0M | - | 185 | 185 | -$217k | - | out (clean 28, ADX 31, RVol 0.3) |
| 17 | **COIN** | 130.52 | - | **-** | 12 | - | POS +$1.2M | 129.42 | 137 | 135 | +$209k | - | out (clean 29, ADX 42, RVol 1.1) |
| 18 | **UBER** | 69.74 | - | **-** | 12 | - | POS +$7.0M | 68.44 | 70 | 70 | -$56k | - | out (clean 33, ADX 39, RVol 0.3) |
| 19 | **GOOGL** | 287.34 | - | **-** | 11 | - | NEG -$18.5M | 289.1 | 300 | 290 | +$3.0M | - | out (clean 30, ADX 20, RVol 0.5) |
| 20 | **BABA** | 102.97 | - | **-** | 11 | - | NEG -$8.8M | 106.12 | 110 | 100 | -$168k | - | out (clean 30, ADX 43, RVol 0.3) |
| 21 | **IWM** | 279.28 | - | **-** | 10 | - | NEG -$1.2B | 283.48 | 280 | 270 | +$3.8M | - | out (clean 36, ADX 40, RVol 0.3) |
| 22 | **AMZN** | 269.02 | - | **-** | 10 | - | POS +$458.3M | - | 270 | 265 | +$8.8M | - | out (clean 34, ADX 22, RVol 0.5) |
| 23 | **DELL** | 327.23 | - | **-** | 10 | - | NEG -$10.6M | - | 350 | 340 | +$987k | - | out (clean 33, ADX 34, RVol 0.5) |
| 24 | **MSTR** | 120.04 | - | **-** | 8 | - | NEG -$20.5M | - | 132 | 110 | +$260k | - | out (clean 29, ADX 34, RVol 0.9) |
| 25 | **SMCI** | 27.47 | - | **-** | 7 | - | POS +$901k | 26.33 | 30 | 25 | -$17k | - | out (clean 29, ADX 33, RVol 0.5) |
| 26 | **SMH** | 477.35 | - | **-** | 6 | - | NEG -$231.3M | - | 500 | 475 | -$97k | - | out (clean 30, ADX 29, RVol 0.4) |
| 27 | **NFLX** | 62.95 | - | **-** | 6 | - | NEG -$21.6M | 65.28 | 65 | 60 | -$117k | - | out (clean 31, ADX 21, RVol 0.4) |

## Big prints this scan (89)
- **QQQ** PUT 675 2026-11-10 (0DTE): 1,000 @ 5.44 = **+$544k** BUY | vol 132,887 / OI 718
- **QQQ** PUT 665 2026-11-13 (3DTE): 934 @ 5.74 = **+$536k** BUY | vol 8,205 / OI 2,925
- **MU** PUT 740 2026-11-11 (1DTE): 85 @ 41.50 = **+$353k** BUY | vol 2,409 / OI 137
- **QQQ** PUT 675 2026-11-10 (0DTE): 600 @ 5.44 = **+$326k** BUY | vol 132,887 / OI 718
- **QQQ** PUT 672 2026-11-10 (0DTE): 1,000 @ 3.14 = **+$314k** BUY | vol 130,559 / OI 153
- **AMD** CALL 510 2026-11-11 (1DTE): 300 @ 10.25 = **+$308k** SELL | vol 7,533 / OI 407
- **QQQ** PUT 670 2026-11-11 (1DTE): 474 @ 4.93 = **+$234k** BUY | vol 23,449 / OI 452
- **QQQ** PUT 675 2026-11-10 (0DTE): 400 @ 5.44 = **+$218k** BUY | vol 132,887 / OI 718
- **SPY** PUT 746 2026-11-10 (0DTE): 1,823 @ 1.13 = **+$206k** BUY | vol 247,183 / OI 242
- **QQQ** PUT 672 2026-11-10 (0DTE): 600 @ 3.11 = **+$187k** BUY | vol 130,559 / OI 153
- **QQQ** PUT 671 2026-11-11 (1DTE): 345 @ 5.36 = **+$185k** BUY | vol 11,470 / OI 170
- **NVDA** CALL 170 2026-11-16 (6DTE): 395 @ 4.20 = **+$166k** SELL | vol 9,405 / OI 394
- **QQQ** PUT 671 2026-11-11 (1DTE): 329 @ 5.00 = **+$164k** BUY | vol 11,470 / OI 170
- **QQQ** PUT 672 2026-11-10 (0DTE): 400 @ 3.11 = **+$124k** BUY | vol 130,559 / OI 153
- **NVDA** PUT 165 2026-11-13 (3DTE): 333 @ 3.70 = **+$123k** BUY | vol 35,257 / OI 19,307

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 745 2026-11-11 (1DTE): 2,251 traded vs OI 2,201
- **SPY** CALL 748 2026-11-20 (10DTE): 715 traded vs OI 655
- **SPY** CALL 790 2026-11-17 (7DTE): 1,803 traded vs OI 734
- **QQQ** CALL 672 2026-11-13 (3DTE): 876 traded vs OI 861
- **QQQ** CALL 663 2026-11-10 (0DTE): 508 traded vs OI 205
- **QQQ** PUT 665 2026-11-16 (6DTE): 519 traded vs OI 513
- **IWM** PUT 277 2026-11-11 (1DTE): 2,970 traded vs OI 2,896
- **NVDA** PUT 160 2026-11-27 (17DTE): 1,145 traded vs OI 1,139
- **TSLA** PUT 377.5 2026-11-20 (10DTE): 611 traded vs OI 607
- **AAPL** CALL 350 2026-11-16 (6DTE): 501 traded vs OI 348
- **AMD** PUT 472.5 2026-11-11 (1DTE): 532 traded vs OI 88
- **AMD** PUT 470 2026-11-13 (3DTE): 1,112 traded vs OI 938
- **MSFT** CALL 540 2026-11-11 (1DTE): 513 traded vs OI 407
- **MU** PUT 712.5 2026-11-13 (3DTE): 530 traded vs OI 284
- **MU** CALL 735 2026-11-13 (3DTE): 501 traded vs OI 335

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
