# GEX + FLOW SCAN - Tue Nov 10, 01:40 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (10)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 12:33 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 667P | 0.67 | 0.28 | +170% (8m) | **-58%** (done) | +15% | 668.83 hit |
| 12:22 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 667P | 0.66 | 0.79 | +174% (19m) | **+20%** (done) | +11% | 669.29 hit |
| 11:18 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 668P | 0.74 | 0.69 | +84% (38m) | **-7%** (done) | +18% | 672.3 hit |
| 11:17 | **SPY** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 744P | 0.60 | 0.36 | +38% (32m) | **-40%** (done) | +41% | 746.01 hit |
| 11:12 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 669P | 0.74 | 1.07 | +135% (44m) | **+45%** (done) | +38% | 671.74 hit |
| 11:12 | **SPY** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 744P | 0.64 | 0.38 | +30% (37m) | **-41%** (done) | +40% | 745.88 |
| 11:06 | **SPY** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 744P | 0.68 | 0.60 | +22% (43m) | **-12%** (done) | +49% | 745.54 |
| 10:15 | **IWM** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/10 280P | 0.63 | 1.39 | +232% (36m) | **+121%** (done) | +22% | 280 hit |
| 09:50 | **SPY** | **PUTS** | FLOW SURGE | 11/10 743P | 0.77 | 0.62 | +21% (60m) | **-19%** (done) | +54% | 745.65 |
| 09:45 | **IWM** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/10 279P | 0.52 | 0.95 | +90% (60m) | **+83%** (done) | +87% | 278.66 |

## 1m RULES on SPY / QQQ - loose (9 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 13:40:08 ET, last candle SPY 13:39, QQQ 13:39 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 12:32 | QQQ | 1m FAILED POP | R3 R4 | PUTS | WITH you | **FIRE** QQQ261110P00667000 |
| 12:21 | QQQ | 1m FAILED POP | R3 R4 | PUTS | TURNING your way | **FIRE** QQQ261110P00667000 |
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
| 1 | **AMZN** | 269.55 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 37 | 11/11 265P @ 0.79 (delta 0.22) = est +29% at 268.2 | POS +$463.1M | - | 270 | 265 | +$8.2M | +$0 bull / -$87k bear | out (clean 32, ADX 23, RVol 0.4) |
| 2 | **MSFT** | 532.65 | - | **-** | 26 | - | POS +$431.9M | 502.79 | 550 | 500 | +$14.4M | +$0 bull / -$98k bear | out (clean 32, ADX 46, RVol 0.4) |
| 3 | **GOOGL** | 285.92 | - | **-** | 22 | - | NEG -$35.7M | 289.29 | 300 | 290 | +$3.4M | +$0 bull / -$31k bear | out (clean 30, ADX 30, RVol 0.4) |
| 4 | **DELL** | 326.49 | - | **-** | 19 | - | NEG -$10.5M | - | 350 | 340 | +$1.3M | +$0 bull / -$43k bear | out (clean 33, ADX 33, RVol 0.3) |
| 5 | **NVDA** | 168.12 | - | **-** | 17 | - | NEG -$158.0M | - | 180 | 170 | +$9.0M | +$522k bull / -$1.3M bear | out (clean 34, ADX 25, RVol 0.7) |
| 6 | **AMD** | 511.00 | - | **-** | 17 | - | POS +$48.2M | - | 500 | 500 | -$43.6M | +$737k bull / -$445k bear | out (clean 33, ADX 23, RVol 0.3) |
| 7 | **PLTR** | 165.74 | - | **-** | 17 | - | POS +$50.4M | - | 165 | 170 | -$681k | +$0 bull / -$77k bear | out (clean 28, ADX 28, RVol 0.2) |
| 8 | **SPY** | 746.87 | - | **-** | 16 | - | NEG -$7.6B | 760.1 | 750 | 730 | +$62.5M | +$0 bull / -$1.9M bear | out (clean 32, ADX 24, RVol 0.3) |
| 9 | **AVGO** | 327.57 | - | **-** | 16 | - | NEG -$15.7M | 343.53 | 340 | 320 | -$9.1M | +$31k bull / -$284k bear | out (clean 32, ADX 11, RVol 0.2) |
| 10 | **CRM** | 210.94 | - | **-** | 16 | - | NEG -$10.7M | - | 195 | 220 | +$329k | - | out (clean 30, ADX 38, RVol 0.2) |
| 11 | **QQQ** | 670.29 | - | **-** | 15 | - | NEG -$2.1B | 692.3 | 680 | 680 | +$20.6M | +$0 bull / -$830k bear | out (clean 32, ADX 26, RVol 0.2) |
| 12 | **TSLA** | 376.80 | - | **-** | 15 | - | POS +$194.8M | - | 400 | 380 | -$6.1M | +$0 bull / -$247k bear | out (clean 32, ADX 17, RVol 0.3) |
| 13 | **META** | 638.54 | - | **-** | 15 | - | POS +$228.7M | 603.98 | 650 | 650 | +$846k | +$0 bull / -$125k bear | out (clean 32, ADX 22, RVol 0.3) |
| 14 | **MU** | 709.41 | - | **-** | 15 | - | NEG -$33.5M | - | 750 | 750 | -$11.6M | +$0 bull / -$2.0M bear | out (clean 30, ADX 19, RVol 0.2) |
| 15 | **SHOP** | 143.73 | - | **-** | 15 | - | NEG -$556k | 144.98 | 150 | 140 | -$182k | - | out (clean 32, ADX 42, RVol 0.7) |
| 16 | **ARM** | 177.78 | - | **-** | 14 | - | NEG -$4.9M | - | 185 | 185 | -$224k | - | out (clean 28, ADX 21, RVol 1.8) |
| 17 | **AAPL** | 347.61 | - | **-** | 12 | - | POS +$413.0M | 336.29 | 350 | 340 | +$17.3M | - | out (clean 28, ADX 12, RVol 0.3) |
| 18 | **HOOD** | 80.55 | - | **-** | 12 | - | POS +$1.8M | 79.24 | 85 | 80 | +$628k | - | out (clean 31, ADX 35, RVol 0.5) |
| 19 | **BABA** | 102.56 | - | **-** | 11 | - | NEG -$9.8M | 106.32 | 110 | 100 | -$53k | - | out (clean 31, ADX 43, RVol 1.1) |
| 20 | **ORCL** | 116.83 | - | **-** | 9 | - | NEG -$24.5M | - | 120 | 120 | +$362k | - | out (clean 28, ADX 37, RVol 0.2) |
| 21 | **UBER** | 69.33 | - | **-** | 9 | - | POS +$5.5M | 68.41 | 70 | 70 | -$47k | - | out (clean 33, ADX 28, RVol 0.3) |
| 22 | **SMCI** | 27.55 | - | **-** | 7 | - | POS +$996k | 26.37 | 30 | 25 | -$52k | - | out (clean 30, ADX 32, RVol 0.3) |
| 23 | **NFLX** | 62.69 | - | **-** | 6 | - | NEG -$25.4M | 65.71 | 65 | 60 | -$132k | - | out (clean 29, ADX 23, RVol 0.4) |
| 24 | **COIN** | 131.57 | - | **-** | 6 | - | POS +$3.6M | 128.84 | 137 | 135 | +$124k | - | out (clean 29, ADX 28, RVol 0.2) |
| 25 | **IWM** | 279.88 | - | **-** | 5 | - | NEG -$1.1B | 283.42 | 280 | 270 | +$2.1M | - | out (clean 36, ADX 19, RVol 0.2) |
| 26 | **SMH** | 478.96 | - | **-** | 5 | - | NEG -$228.1M | - | 500 | 475 | +$155k | - | out (clean 30, ADX 22, RVol 0.2) |
| 27 | **MSTR** | 120.86 | - | **-** | 5 | - | NEG -$20.4M | - | 132 | 110 | +$165k | - | out (clean 29, ADX 23, RVol 0.4) |

## Big prints this scan (41)
- **MU** PUT 725 2026-11-11 (1DTE): 100 @ 27.00 = **+$270k** BUY | vol 4,094 / OI 61
- **MU** PUT 725 2026-11-11 (1DTE): 100 @ 26.00 = **+$260k** BUY | vol 4,094 / OI 61
- **AVGO** PUT 330 2026-11-13 (3DTE): 247 @ 9.80 = **+$242k** BUY | vol 1,792 / OI 2,093
- **SPY** CALL 745 2026-11-10 (0DTE): 1,000 @ 1.67 = **+$167k** SELL | vol 53,784 / OI 1,171
- **SPY** PUT 746 2026-11-10 (0DTE): 918 @ 1.27 = **+$117k** BUY | vol 399,731 / OI 242
- **QQQ** PUT 671 2026-11-17 (7DTE): 100 @ 10.98 = **+$110k** BUY | vol 276 / OI 164
- **NVDA** CALL 167.5 2026-11-11 (1DTE): 372 @ 2.88 = **+$107k** SELL | vol 59,058 / OI 80
- **SPY** CALL 745 2026-11-10 (0DTE): 624 @ 1.68 = **+$105k** SELL | vol 53,784 / OI 1,171
- **QQQ** PUT 670 2026-11-11 (1DTE): 200 @ 5.15 = **+$103k** BUY | vol 33,868 / OI 452
- **META** PUT 640 2026-11-13 (3DTE): 75 @ 12.10 = **+$91k** BUY | vol 736 / OI 519
- **NVDA** CALL 167.5 2026-11-13 (3DTE): 130 @ 4.50 = **+$58k** SELL | vol 12,478 / OI 18
- **NVDA** CALL 167.5 2026-11-11 (1DTE): 200 @ 2.88 = **+$58k** SELL | vol 59,058 / OI 80
- **NVDA** CALL 167.5 2026-11-11 (1DTE): 200 @ 2.88 = **+$58k** SELL | vol 59,058 / OI 80
- **MU** PUT 675 2026-11-11 (1DTE): 100 @ 4.80 = **+$48k** BUY | vol 5,852 / OI 27
- **AMD** CALL 500 2026-11-11 (1DTE): 30 @ 14.95 = **+$45k** SELL | vol 3,952 / OI 943

## New unusual volume (traded more than open interest, 500+)
- **QQQ** CALL 668 2026-11-13 (3DTE): 748 traded vs OI 747
- **TSLA** CALL 377.5 2026-11-20 (10DTE): 831 traded vs OI 828
- **TSLA** CALL 410 2026-11-16 (6DTE): 672 traded vs OI 615
- **TSLA** PUT 347.5 2026-11-16 (6DTE): 505 traded vs OI 75
- **AMD** CALL 507.5 2026-11-13 (3DTE): 520 traded vs OI 213
- **AMZN** PUT 277.5 2026-11-13 (3DTE): 606 traded vs OI 55
- **AMZN** PUT 277.5 2026-11-11 (1DTE): 556 traded vs OI 33
- **MSFT** CALL 545 2026-11-13 (3DTE): 1,762 traded vs OI 1,632
- **MSFT** PUT 515 2026-11-13 (3DTE): 1,494 traded vs OI 1,466
- **MSFT** PUT 520 2026-11-16 (6DTE): 511 traded vs OI 25
- **HOOD** CALL 81 2026-11-20 (10DTE): 527 traded vs OI 0
- **HOOD** CALL 80 2026-11-13 (3DTE): 701 traded vs OI 692
- **SHOP** CALL 147 2026-11-13 (3DTE): 1,409 traded vs OI 50

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
