# GEX + FLOW SCAN - Tue Nov 10, 12:10 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (8)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:18 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 668P | 0.74 | 0.97 | +84% (38m) | **+31%** | +18% | 672.3 hit |
| 11:17 | **SPY** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 744P | 0.60 | 0.45 | +38% (32m) | **-25%** | +41% | 746.01 hit |
| 11:12 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 669P | 0.74 | 1.27 | +135% (44m) | **+72%** | +38% | 671.74 hit |
| 11:12 | **SPY** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 744P | 0.64 | 0.45 | +30% (37m) | **-30%** | +40% | 745.88 |
| 11:06 | **SPY** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 744P | 0.68 | 0.60 | +22% (43m) | **-12%** (done) | +49% | 745.54 |
| 10:15 | **IWM** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/10 280P | 0.63 | 1.39 | +232% (36m) | **+121%** (done) | +22% | 280 hit |
| 09:50 | **SPY** | **PUTS** | FLOW SURGE | 11/10 743P | 0.77 | 0.62 | +21% (60m) | **-19%** (done) | +54% | 745.65 |
| 09:45 | **IWM** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/10 279P | 0.52 | 0.95 | +90% (60m) | **+83%** (done) | +87% | 278.66 |

## 1m RULES on SPY / QQQ - loose (7 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 12:10:08 ET, last candle SPY 12:09, QQQ 12:09 | no errors
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
| 1 | **NVDA** | 166.93 | TREND (flow not with it) | **PUTS** | 33 | none: 39 puts 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$151.6M | - | 180 | 170 | +$23.4M | +$2.5M bull / -$1.1M bear | SHORT (clean 33, ADX 40, RVol 1.6) |
| 2 | **AAPL** | 348.21 | - | **-** | 24 | - | POS +$434.7M | 335.91 | 350 | 340 | +$17.3M | +$0 bull / -$80k bear | out (clean 28, ADX 15, RVol 0.4) |
| 3 | **SHOP** | 144.28 | - | **-** | 24 | - | NEG -$340k | 144.96 | 150 | 140 | +$85k | - | out (clean 33, ADX 57, RVol 0.6) |
| 4 | **GOOGL** | 287.36 | - | **-** | 22 | - | NEG -$16.8M | 289.15 | 300 | 290 | +$3.3M | +$57k bull / +$0 bear | out (clean 30, ADX 20, RVol 0.5) |
| 5 | **BABA** | 102.97 | - | **-** | 21 | - | NEG -$8.3M | 106.09 | 110 | 100 | -$144k | +$38k bull / +$0 bear | out (clean 30, ADX 43, RVol 0.3) |
| 6 | **AMD** | 509.13 | - | **-** | 20 | - | POS +$46.8M | - | 500 | 500 | -$33.5M | +$2.9M bull / -$415k bear | out (clean 32, ADX 27, RVol 1.1) |
| 7 | **PLTR** | 165.81 | - | **-** | 20 | - | POS +$51.7M | - | 165 | 170 | -$91k | +$63k bull / +$0 bear | out (clean 28, ADX 42, RVol 0.9) |
| 8 | **SPY** | 747.06 | - | **-** | 19 | - | NEG -$7.4B | 759.88 | 750 | 730 | +$72.7M | +$0 bull / -$225k bear | out (clean 32, ADX 33, RVol 0.5) |
| 9 | **AVGO** | 324.38 | - | **-** | 18 | - | NEG -$18.1M | 341.26 | 340 | 320 | -$8.1M | +$274k bull / -$113k bear | out (clean 32, ADX 20, RVol 0.3) |
| 10 | **QQQ** | 670.46 | - | **-** | 17 | - | NEG -$2.2B | 691.71 | 680 | 680 | +$35.6M | +$2.7M bull / -$861k bear | out (clean 32, ADX 32, RVol 0.3) |
| 11 | **MU** | 705.07 | - | **-** | 17 | - | NEG -$32.9M | - | 750 | 750 | -$807k | +$2.0M bull / -$1.6M bear | out (clean 30, ADX 29, RVol 0.9) |
| 12 | **MSTR** | 119.69 | - | **-** | 17 | - | NEG -$25.4M | - | 130 | 110 | +$125k | +$42k bull / +$0 bear | out (clean 29, ADX 33, RVol 0.4) |
| 13 | **ORCL** | 117.72 | - | **-** | 17 | - | NEG -$23.7M | - | 120 | 120 | +$350k | +$753k bull / +$0 bear | out (clean 28, ADX 26, RVol 0.2) |
| 14 | **TSLA** | 375.66 | - | **-** | 16 | - | POS +$186.1M | - | 400 | 380 | -$1.1M | +$238k bull / -$544k bear | out (clean 33, ADX 24, RVol 0.6) |
| 15 | **META** | 640.55 | - | **-** | 16 | - | POS +$241.8M | 606.81 | 650 | 650 | +$920k | +$0 bull / -$319k bear | out (clean 32, ADX 20, RVol 0.8) |
| 16 | **CRM** | 212.35 | - | **-** | 15 | - | NEG -$10.7M | - | 195 | 220 | -$103k | - | out (clean 29, ADX 32, RVol 0.4) |
| 17 | **COIN** | 130.10 | - | **-** | 14 | - | POS +$1.2M | 129.2 | 137 | 135 | +$300k | - | out (clean 29, ADX 41, RVol 1.4) |
| 18 | **HOOD** | 80.43 | - | **-** | 14 | - | POS +$1.8M | 79.16 | 85 | 80 | +$628k | - | out (clean 31, ADX 39, RVol 0.7) |
| 19 | **ARM** | 177.35 | - | **-** | 13 | - | NEG -$4.7M | - | 185 | 185 | -$212k | - | out (clean 27, ADX 32, RVol 0.3) |
| 20 | **UBER** | 69.70 | - | **-** | 12 | - | POS +$7.0M | 68.45 | 70 | 70 | -$49k | - | out (clean 33, ADX 43, RVol 0.3) |
| 21 | **IWM** | 278.94 | - | **-** | 11 | - | NEG -$1.2B | 283.42 | 280 | 270 | +$4.4M | - | out (clean 36, ADX 44, RVol 0.5) |
| 22 | **AMZN** | 268.84 | - | **-** | 10 | - | POS +$461.4M | - | 270 | 265 | +$8.9M | - | out (clean 34, ADX 22, RVol 0.4) |
| 23 | **DELL** | 327.99 | - | **-** | 9 | - | NEG -$11.1M | - | 350 | 340 | +$775k | - | out (clean 33, ADX 34, RVol 0.6) |
| 24 | **SMH** | 476.10 | - | **-** | 7 | - | NEG -$229.2M | - | 500 | 475 | +$99k | - | out (clean 30, ADX 29, RVol 0.7) |
| 25 | **MSFT** | 542.88 | - | **-** | 7 | - | POS +$689.1M | - | 550 | 535 | -$311k | - | out (clean 32, ADX 28, RVol 0.4) |
| 26 | **SMCI** | 27.48 | - | **-** | 7 | - | POS +$1.0M | 26.37 | 30 | 25 | -$17k | - | out (clean 29, ADX 31, RVol 0.6) |
| 27 | **NFLX** | 62.92 | - | **-** | 6 | - | NEG -$21.2M | 65.17 | 65 | 60 | -$101k | - | out (clean 30, ADX 25, RVol 0.5) |

## Big prints this scan (121)
- **QQQ** PUT 670 2026-11-12 (2DTE): 837 @ 6.26 = **+$524k** BUY | vol 5,248 / OI 1,092
- **QQQ** PUT 650 2026-11-13 (3DTE): 2,000 @ 1.93 = **+$386k** SELL | vol 9,570 / OI 49,500
- **NVDA** PUT 167.5 2026-11-11 (1DTE): 919 @ 3.35 = **+$308k** BUY | vol 90,876 / OI 819
- **MU** PUT 725 2026-11-11 (1DTE): 100 @ 30.00 = **+$300k** BUY | vol 3,548 / OI 61
- **MU** CALL 740 2026-11-11 (1DTE): 702 @ 3.60 = **+$253k** SELL | vol 9,221 / OI 238
- **AMD** PUT 500 2026-11-11 (1DTE): 361 @ 6.50 = **+$235k** SELL | vol 13,142 / OI 49
- **QQQ** PUT 674 2026-11-10 (0DTE): 486 @ 3.74 = **+$182k** SELL | vol 102,798 / OI 221
- **AMD** PUT 525 2026-11-11 (1DTE): 95 @ 19.00 = **+$180k** SELL | vol 4,585 / OI 28
- **AMD** PUT 510 2026-11-11 (1DTE): 150 @ 11.35 = **+$170k** BUY | vol 5,707 / OI 85
- **NVDA** CALL 172.5 2026-11-16 (6DTE): 500 @ 3.15 = **+$158k** MID | vol 8,803 / OI 10
- **NVDA** CALL 172.5 2026-11-16 (6DTE): 500 @ 3.14 = **+$157k** MID | vol 8,803 / OI 10
- **QQQ** CALL 670 2026-11-10 (0DTE): 566 @ 2.38 = **+$135k** BUY | vol 18,016 / OI 1,753
- **NVDA** PUT 175 2026-11-11 (1DTE): 150 @ 8.70 = **+$130k** BUY | vol 15,576 / OI 3,758
- **QQQ** PUT 671 2026-11-10 (0DTE): 500 @ 2.45 = **+$122k** BUY | vol 114,386 / OI 1,263
- **AMD** PUT 510 2026-11-11 (1DTE): 100 @ 11.40 = **+$114k** BUY | vol 5,707 / OI 85

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 741 2026-11-10 (0DTE): 1,899 traded vs OI 1,804
- **SPY** CALL 809 2026-11-20 (10DTE): 803 traded vs OI 792
- **QQQ** PUT 668 2026-11-12 (2DTE): 539 traded vs OI 112
- **QQQ** CALL 710 2026-11-12 (2DTE): 1,237 traded vs OI 413
- **QQQ** CALL 693 2026-11-13 (3DTE): 518 traded vs OI 506
- **QQQ** PUT 667 2026-11-13 (3DTE): 508 traded vs OI 144
- **QQQ** CALL 676 2026-11-13 (3DTE): 722 traded vs OI 721
- **IWM** CALL 287 2026-11-16 (6DTE): 508 traded vs OI 232
- **IWM** PUT 280 2026-11-16 (6DTE): 502 traded vs OI 209
- **SMH** PUT 470 2026-11-20 (10DTE): 2,426 traded vs OI 2,339
- **NVDA** CALL 152.5 2026-11-16 (6DTE): 697 traded vs OI 0
- **NVDA** PUT 177.5 2026-11-13 (3DTE): 2,954 traded vs OI 2,794
- **AMD** CALL 512.5 2026-11-13 (3DTE): 512 traded vs OI 488
- **AMD** PUT 462.5 2026-11-11 (1DTE): 574 traded vs OI 44
- **META** PUT 632.5 2026-11-11 (1DTE): 520 traded vs OI 52

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
