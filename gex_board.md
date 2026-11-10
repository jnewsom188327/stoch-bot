# GEX + FLOW SCAN - Tue Nov 10, 03:55 PM ET
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
Last 1m check 15:32:08 ET, last candle SPY 15:31, QQQ 15:31 | no errors
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
| 1 | **AAPL** | 349.42 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 42 | 11/11 345P @ 0.61 (delta 0.21) = est +25% at 348.42 | POS +$460.8M | 337.46 | 350 | 340 | +$16.5M | +$0 bull / -$99k bear | out (clean 28, ADX 21, RVol 0.8) |
| 2 | **UBER** | 70.14 | PINNED between the walls (positive gamma) - chop | **-** | 26 | - | POS +$9.3M | 68.48 | 70 | 70 | -$72k | - | out (clean 34, ADX 24, RVol 1.1) |
| 3 | **AVGO** | 332.02 | - | **-** | 21 | - | NEG -$3.4M | 334.85 | 340 | 340 | -$11.4M | +$138k bull / +$0 bear | out (clean 34, ADX 31, RVol 1.0) |
| 4 | **META** | 642.74 | - | **-** | 19 | - | POS +$272.0M | 605.65 | 650 | 650 | -$1.1M | +$31k bull / -$27k bear | out (clean 32, ADX 37, RVol 0.9) |
| 5 | **AMZN** | 271.43 | - | **-** | 19 | - | POS +$491.8M | - | 270 | 265 | -$64k | +$33k bull / +$0 bear | out (clean 34, ADX 38, RVol 0.9) |
| 6 | **SPY** | 750.48 | - | **-** | 18 | - | NEG -$5.4B | 760.59 | 750 | 750 | -$417k | +$2.6M bull / -$404k bear | out (clean 32, ADX 34, RVol 1.2) |
| 7 | **AMD** | 516.63 | - | **-** | 18 | - | POS +$46.9M | - | 500 | 500 | -$49.9M | +$578k bull / -$234k bear | out (clean 33, ADX 19, RVol 1.0) |
| 8 | **GOOGL** | 287.67 | - | **-** | 18 | - | NEG -$13.4M | 288.69 | 300 | 290 | +$1.9M | +$158k bull / +$0 bear | out (clean 29, ADX 22, RVol 0.8) |
| 9 | **QQQ** | 675.28 | - | **-** | 17 | - | NEG -$1.7B | 692.35 | 680 | 680 | -$7.9M | +$359k bull / -$529k bear | out (clean 32, ADX 31, RVol 0.9) |
| 10 | **DELL** | 334.71 | - | **-** | 17 | - | NEG -$8.7M | - | 350 | 340 | +$889k | +$75k bull / -$42k bear | out (clean 34, ADX 22, RVol 0.6) |
| 11 | **MU** | 723.16 | - | **-** | 17 | - | NEG -$14.0M | - | 750 | 750 | -$23.7M | +$1.1M bull / -$867k bear | out (clean 31, ADX 25, RVol 0.8) |
| 12 | **MSTR** | 121.52 | - | **-** | 16 | - | NEG -$26.6M | - | 130 | 110 | +$515k | +$26k bull / +$0 bear | out (clean 29, ADX 13, RVol 1.4) |
| 13 | **ORCL** | 117.89 | - | **-** | 16 | - | NEG -$25.2M | - | 120 | 120 | +$561k | +$65k bull / +$0 bear | out (clean 27, ADX 17, RVol 0.4) |
| 14 | **SMH** | 484.10 | - | **-** | 15 | - | NEG -$200.0M | - | 500 | 475 | -$832k | +$31k bull / -$405k bear | out (clean 30, ADX 17, RVol 0.4) |
| 15 | **NVDA** | 168.76 | - | **-** | 15 | - | NEG -$163.1M | - | 180 | 170 | +$9.3M | +$2.4M bull / -$692k bear | out (clean 33, ADX 12, RVol 1.0) |
| 16 | **TSLA** | 379.01 | - | **-** | 15 | - | POS +$217.1M | - | 400 | 380 | -$8.2M | +$57k bull / -$137k bear | out (clean 32, ADX 12, RVol 0.6) |
| 17 | **ARM** | 181.54 | - | **-** | 15 | - | NEG -$4.7M | - | 185 | 190 | -$353k | - | out (clean 27, ADX 33, RVol 0.7) |
| 18 | **SHOP** | 146.74 | - | **-** | 14 | - | POS +$678k | 145.48 | 150 | 140 | -$230k | - | out (clean 32, ADX 30, RVol 0.9) |
| 19 | **CRM** | 213.26 | - | **-** | 13 | - | NEG -$10.9M | - | 195 | 220 | +$282k | - | out (clean 31, ADX 19, RVol 1.4) |
| 20 | **PLTR** | 168.77 | - | **-** | 9 | - | POS +$56.5M | - | 165 | 170 | -$986k | - | out (clean 29, ADX 27, RVol 0.8) |
| 21 | **HOOD** | 81.72 | - | **-** | 9 | - | POS +$3.6M | 79.25 | 85 | 80 | +$549k | - | out (clean 32, ADX 17, RVol 1.4) |
| 22 | **MSFT** | 533.27 | - | **-** | 8 | - | POS +$416.5M | 507.23 | 550 | 535 | +$10.9M | - | out (clean 32, ADX 14, RVol 0.6) |
| 23 | **NFLX** | 63.09 | - | **-** | 8 | - | NEG -$19.8M | 65.05 | 65 | 65 | -$217k | - | out (clean 29, ADX 21, RVol 1.0) |
| 24 | **IWM** | 280.81 | - | **-** | 6 | - | NEG -$665.4M | 282.83 | 281 | 270 | +$1.3M | - | out (clean 34, ADX 19, RVol 1.1) |
| 25 | **COIN** | 132.83 | - | **-** | 6 | - | POS +$4.9M | 129.42 | 137 | 135 | +$108k | - | out (clean 28, ADX 20, RVol 0.8) |
| 26 | **SMCI** | 27.89 | - | **-** | 5 | - | POS +$1.9M | - | 30 | 30 | -$42k | - | out (clean 30, ADX 16, RVol 0.8) |
| 27 | **BABA** | 102.79 | - | **-** | 5 | - | NEG -$9.4M | 106.14 | 110 | 100 | -$42k | - | out (clean 30, ADX 17, RVol 1.0) |

## Big prints this scan (27)
- **QQQ** CALL 670 2026-11-10 (0DTE): 996 @ 3.56 = **+$355k** SELL | vol 160,746 / OI 1,753
- **NVDA** CALL 167.5 2026-11-11 (1DTE): 760 @ 3.17 = **+$241k** SELL | vol 88,353 / OI 80
- **SMH** PUT 485 2026-11-13 (3DTE): 186 @ 11.80 = **+$219k** BUY | vol 2,438 / OI 308
- **QQQ** PUT 675 2026-11-10 (0DTE): 996 @ 1.75 = **+$174k** BUY | vol 156,210 / OI 718
- **SPY** CALL 749 2026-11-10 (0DTE): 1,980 @ 0.85 = **+$168k** SELL | vol 470,930 / OI 1,190
- **NVDA** CALL 167.5 2026-11-11 (1DTE): 507 @ 3.17 = **+$161k** SELL | vol 88,353 / OI 80
- **MU** CALL 750 2026-11-11 (1DTE): 330 @ 3.22 = **+$106k** SELL | vol 19,187 / OI 728
- **AMD** CALL 517.5 2026-11-11 (1DTE): 100 @ 8.88 = **+$89k** SELL | vol 5,450 / OI 13
- **MU** PUT 740 2026-11-11 (1DTE): 30 @ 28.57 = **+$86k** BUY | vol 2,519 / OI 137
- **SMH** CALL 470 2026-11-11 (1DTE): 50 @ 14.70 = **+$74k** SELL | vol 164 / OI 302
- **MU** PUT 720 2026-11-13 (3DTE): 20 @ 24.40 = **+$49k** BUY | vol 3,230 / OI 1,457
- **SMH** CALL 470 2026-11-11 (1DTE): 30 @ 14.82 = **+$44k** SELL | vol 164 / OI 302
- **NVDA** CALL 170 2026-11-16 (6DTE): 100 @ 4.44 = **+$44k** SELL | vol 16,235 / OI 394
- **NVDA** CALL 170 2026-11-16 (6DTE): 97 @ 4.44 = **+$43k** SELL | vol 16,235 / OI 394
- **AMD** CALL 510 2026-11-11 (1DTE): 34 @ 12.49 = **+$42k** SELL | vol 17,515 / OI 407

## New unusual volume (traded more than open interest, 500+)
- **QQQ** CALL 740 2026-11-20 (10DTE): 500 traded vs OI 0
- **SMH** CALL 480 2026-11-11 (1DTE): 639 traded vs OI 627
- **SMH** CALL 487.5 2026-11-11 (1DTE): 501 traded vs OI 261
- **AMZN** CALL 277.5 2026-11-16 (6DTE): 510 traded vs OI 102
- **AVGO** PUT 330 2026-11-13 (3DTE): 2,115 traded vs OI 2,093
- **PLTR** CALL 185 2026-11-13 (3DTE): 1,043 traded vs OI 0
- **PLTR** CALL 185 2026-11-20 (10DTE): 570 traded vs OI 0
- **MSTR** PUT 117 2026-11-20 (10DTE): 505 traded vs OI 0
- **UBER** CALL 77 2026-11-13 (3DTE): 528 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
