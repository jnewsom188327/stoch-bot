# GEX + FLOW SCAN - Tue Nov 10, 12:00 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (8)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:18 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 668P | 0.74 | 1.28 | +84% (38m) | **+73%** | +18% | 672.3 hit |
| 11:17 | **SPY** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 744P | 0.60 | 0.75 | +38% (32m) | **+25%** | +41% | 746.01 hit |
| 11:12 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 669P | 0.74 | 1.71 | +135% (44m) | **+131%** | +38% | 671.74 hit |
| 11:12 | **SPY** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 744P | 0.64 | 0.75 | +30% (37m) | **+17%** | +40% | 745.88 |
| 11:06 | **SPY** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 744P | 0.68 | 0.75 | +22% (43m) | **+10%** | +49% | 745.54 |
| 10:15 | **IWM** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/10 280P | 0.63 | 1.39 | +232% (36m) | **+121%** (done) | +22% | 280 hit |
| 09:50 | **SPY** | **PUTS** | FLOW SURGE | 11/10 743P | 0.77 | 0.62 | +21% (60m) | **-19%** (done) | +54% | 745.65 |
| 09:45 | **IWM** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/10 279P | 0.52 | 0.95 | +90% (60m) | **+83%** (done) | +87% | 278.66 |

## 1m RULES on SPY / QQQ - loose (7 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 12:00:08 ET, last candle SPY 11:59, QQQ 11:59 | no errors
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
| 1 | **AAPL** | 348.17 | - | **-** | 25 | - | POS +$427.6M | 336.11 | 350 | 340 | +$18.1M | +$0 bull / -$31k bear | out (clean 28, ADX 17, RVol 0.4) |
| 2 | **SHOP** | 145.19 | - | **-** | 23 | - | POS +$424k | 144.69 | 150 | 140 | +$78k | - | out (clean 33, ADX 55, RVol 0.3) |
| 3 | **IWM** | 278.56 | - | **-** | 22 | - | NEG -$1.4B | 283.81 | 280 | 270 | +$5.1M | +$368k bull / +$0 bear | out (clean 36, ADX 45, RVol 0.4) |
| 4 | **NVDA** | 166.87 | - | **-** | 22 | - | NEG -$151.9M | - | 180 | 170 | +$29.8M | +$2.0M bull / +$0 bear | out (clean 33, ADX 38, RVol 1.5) |
| 5 | **GOOGL** | 287.12 | - | **-** | 21 | - | NEG -$18.3M | 288.9 | 300 | 290 | +$3.2M | +$25k bull / +$0 bear | out (clean 30, ADX 20, RVol 0.5) |
| 6 | **PLTR** | 165.95 | - | **-** | 20 | - | POS +$51.9M | - | 165 | 170 | -$96k | +$188k bull / +$0 bear | out (clean 28, ADX 44, RVol 0.8) |
| 7 | **DELL** | 326.76 | - | **-** | 20 | - | NEG -$10.4M | - | 350 | 340 | +$992k | +$29k bull / +$0 bear | out (clean 33, ADX 32, RVol 0.5) |
| 8 | **AMD** | 508.92 | - | **-** | 19 | - | POS +$48.1M | - | 500 | 500 | -$32.4M | +$3.3M bull / +$0 bear | out (clean 32, ADX 25, RVol 1.1) |
| 9 | **QQQ** | 669.90 | - | **-** | 18 | - | NEG -$2.2B | 692.56 | 680 | 680 | +$53.1M | +$2.0M bull / +$0 bear | out (clean 31, ADX 30, RVol 0.4) |
| 10 | **MSFT** | 542.88 | - | **-** | 18 | - | POS +$682.7M | - | 550 | 535 | -$378k | +$103k bull / +$0 bear | out (clean 32, ADX 30, RVol 0.4) |
| 11 | **AVGO** | 324.32 | - | **-** | 18 | - | NEG -$19.1M | 343.18 | 340 | 320 | -$7.4M | +$551k bull / +$0 bear | out (clean 32, ADX 20, RVol 0.4) |
| 12 | **MU** | 702.56 | - | **-** | 18 | - | NEG -$33.2M | - | 750 | 750 | +$8.4M | +$2.0M bull / +$0 bear | out (clean 30, ADX 28, RVol 0.9) |
| 13 | **TSLA** | 375.29 | - | **-** | 16 | - | POS +$190.1M | - | 380 | 380 | +$1.4M | +$486k bull / -$266k bear | out (clean 33, ADX 26, RVol 0.6) |
| 14 | **META** | 639.30 | - | **-** | 16 | - | POS +$240.0M | 605.22 | 650 | 650 | +$1.7M | +$161k bull / +$0 bear | out (clean 32, ADX 20, RVol 0.9) |
| 15 | **CRM** | 212.13 | - | **-** | 16 | - | NEG -$10.8M | - | 195 | 220 | -$104k | - | out (clean 29, ADX 35, RVol 0.3) |
| 16 | **COIN** | 129.93 | - | **-** | 14 | - | NEG -$1.5M | 131.62 | 137 | 120 | +$304k | - | out (clean 29, ADX 41, RVol 1.4) |
| 17 | **HOOD** | 80.33 | - | **-** | 14 | - | POS +$2.0M | 79.03 | 85 | 80 | +$694k | - | out (clean 30, ADX 39, RVol 0.6) |
| 18 | **ARM** | 177.48 | - | **-** | 13 | - | NEG -$4.6M | - | 185 | 185 | -$216k | - | out (clean 27, ADX 31, RVol 0.4) |
| 19 | **AMZN** | 268.59 | - | **-** | 11 | - | POS +$461.9M | - | 270 | 265 | +$9.6M | - | out (clean 33, ADX 23, RVol 0.3) |
| 20 | **BABA** | 102.83 | - | **-** | 11 | - | NEG -$8.6M | 106.02 | 110 | 100 | -$140k | - | out (clean 30, ADX 43, RVol 0.6) |
| 21 | **SPY** | 746.22 | - | **-** | 10 | - | NEG -$7.9B | 760.27 | 750 | 730 | +$83.7M | - | out (clean 32, ADX 33, RVol 0.5) |
| 22 | **UBER** | 69.69 | - | **-** | 10 | - | POS +$7.2M | 68.43 | 70 | 70 | -$21k | - | out (clean 33, ADX 46, RVol 0.3) |
| 23 | **SMH** | 475.78 | - | **-** | 7 | - | NEG -$231.5M | - | 500 | 475 | +$557k | - | out (clean 29, ADX 26, RVol 0.6) |
| 24 | **NFLX** | 62.83 | - | **-** | 7 | - | NEG -$22.5M | 65.26 | 65 | 60 | -$103k | - | out (clean 30, ADX 28, RVol 0.5) |
| 25 | **SMCI** | 27.40 | - | **-** | 7 | - | POS +$967k | 26.28 | 30 | 25 | -$17k | - | out (clean 29, ADX 29, RVol 0.7) |
| 26 | **MSTR** | 120.09 | - | **-** | 7 | - | NEG -$20.4M | - | 132 | 110 | +$189k | - | out (clean 29, ADX 33, RVol 0.4) |
| 27 | **ORCL** | 117.83 | - | **-** | 6 | - | NEG -$23.8M | - | 120 | 120 | +$121k | - | out (clean 28, ADX 26, RVol 0.2) |

## Big prints this scan (44)
- **AMD** CALL 500 2026-11-13 (3DTE): 100 @ 27.40 = **+$274k** BUY | vol 2,487 / OI 2,434
- **QQQ** PUT 671 2026-11-11 (1DTE): 427 @ 4.33 = **+$185k** SELL | vol 5,946 / OI 170
- **QQQ** PUT 673 2026-11-10 (0DTE): 779 @ 2.32 = **+$181k** SELL | vol 129,908 / OI 98
- **AVGO** CALL 327.5 2026-11-11 (1DTE): 396 @ 4.05 = **+$160k** BUY | vol 3,669 / OI 78
- **QQQ** PUT 672 2026-11-10 (0DTE): 779 @ 1.83 = **+$143k** SELL | vol 118,828 / OI 153
- **MU** PUT 675 2026-11-11 (1DTE): 176 @ 3.80 = **+$67k** SELL | vol 3,573 / OI 27
- **NVDA** PUT 165 2026-11-13 (3DTE): 200 @ 3.20 = **+$64k** SELL | vol 29,325 / OI 19,307
- **NVDA** PUT 167.5 2026-11-13 (3DTE): 147 @ 4.23 = **+$62k** SELL | vol 14,020 / OI 1,236
- **NVDA** PUT 167.5 2026-11-11 (1DTE): 176 @ 2.81 = **+$49k** SELL | vol 84,808 / OI 819
- **NVDA** PUT 165 2026-11-13 (3DTE): 144 @ 3.37 = **+$49k** SELL | vol 29,325 / OI 19,307
- **NVDA** PUT 165 2026-11-13 (3DTE): 147 @ 3.23 = **+$47k** SELL | vol 29,325 / OI 19,307
- **NVDA** PUT 162.5 2026-11-11 (1DTE): 450 @ 1.05 = **+$47k** SELL | vol 39,633 / OI 376
- **NVDA** PUT 170 2026-11-16 (6DTE): 74 @ 6.35 = **+$47k** SELL | vol 6,716 / OI 729
- **MU** PUT 710 2026-11-11 (1DTE): 30 @ 14.92 = **+$45k** SELL | vol 6,977 / OI 128
- **MU** PUT 700 2026-11-11 (1DTE): 40 @ 10.75 = **+$43k** SELL | vol 11,485 / OI 160

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 756 2026-11-13 (3DTE): 2,999 traded vs OI 2,468
- **SPY** CALL 771 2026-11-11 (1DTE): 604 traded vs OI 595
- **SPY** PUT 705 2026-11-18 (8DTE): 515 traded vs OI 318
- **SPY** CALL 795 2026-11-17 (7DTE): 981 traded vs OI 171
- **QQQ** PUT 636 2026-11-10 (0DTE): 527 traded vs OI 32
- **QQQ** CALL 681 2026-11-12 (2DTE): 508 traded vs OI 261
- **QQQ** PUT 643 2026-11-12 (2DTE): 532 traded vs OI 71
- **QQQ** PUT 646 2026-11-12 (2DTE): 603 traded vs OI 55
- **IWM** CALL 281 2026-11-17 (7DTE): 658 traded vs OI 127
- **IWM** CALL 284 2026-11-17 (7DTE): 576 traded vs OI 193
- **IWM** CALL 282 2026-11-17 (7DTE): 585 traded vs OI 145
- **NVDA** CALL 167.5 2026-11-18 (8DTE): 505 traded vs OI 0
- **NVDA** PUT 167.5 2026-11-27 (17DTE): 719 traded vs OI 0
- **TSLA** CALL 350 2026-11-11 (1DTE): 583 traded vs OI 575
- **AMD** CALL 500 2026-11-13 (3DTE): 2,487 traded vs OI 2,434

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
