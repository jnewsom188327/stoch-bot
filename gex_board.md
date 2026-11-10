# GEX + FLOW SCAN - Tue Nov 10, 03:35 PM ET
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
| 1 | **MSFT** | 533.90 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 36 | none: 126 calls 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (16 contracts' greeks worked out here) | POS +$445.6M | 506.87 | 550 | 535 | +$11.1M | +$0 bull / -$27k bear | out (clean 32, ADX 17, RVol 0.4) |
| 2 | **AMZN** | 271.84 | TREND (flow not with it) | **CALLS** | 25 | none: 66 calls 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (7 contracts' greeks worked out here) | POS +$490.6M | - | 270 | 265 | -$565k | - | LONG (clean 34, ADX 41, RVol 0.8) |
| 3 | **ARM** | 180.63 | - | **-** | 25 | - | NEG -$5.0M | - | 185 | 190 | -$335k | +$0 bull / -$62k bear | out (clean 27, ADX 27, RVol 1.2) |
| 4 | **AAPL** | 348.75 | - | **-** | 22 | - | POS +$442.5M | 337.34 | 350 | 340 | +$16.9M | +$0 bull / -$105k bear | out (clean 28, ADX 14, RVol 0.6) |
| 5 | **AVGO** | 332.52 | - | **-** | 21 | - | NEG -$3.1M | 334.88 | 340 | 340 | -$11.9M | +$0 bull / -$440k bear | out (clean 34, ADX 34, RVol 0.6) |
| 6 | **AMD** | 515.89 | - | **-** | 18 | - | POS +$46.4M | - | 500 | 500 | -$51.8M | +$716k bull / -$1.3M bear | out (clean 33, ADX 22, RVol 0.7) |
| 7 | **META** | 645.65 | - | **-** | 18 | - | POS +$286.5M | - | 650 | 650 | -$1.8M | +$0 bull / -$59k bear | out (clean 32, ADX 32, RVol 0.5) |
| 8 | **SPY** | 749.36 | - | **-** | 17 | - | NEG -$6.3B | 760.58 | 750 | 750 | +$6.6M | +$0 bull / -$1.5M bear | out (clean 32, ADX 30, RVol 0.6) |
| 9 | **GOOGL** | 287.63 | - | **-** | 17 | - | NEG -$16.8M | 289.07 | 300 | 290 | +$1.7M | +$0 bull / -$72k bear | out (clean 29, ADX 20, RVol 0.5) |
| 10 | **PLTR** | 167.39 | - | **-** | 16 | - | POS +$54.4M | - | 165 | 170 | -$913k | +$0 bull / -$355k bear | out (clean 28, ADX 19, RVol 0.4) |
| 11 | **MU** | 717.33 | - | **-** | 16 | - | NEG -$29.6M | - | 750 | 750 | -$25.2M | +$0 bull / -$1.4M bear | out (clean 31, ADX 23, RVol 0.4) |
| 12 | **SMH** | 482.88 | - | **-** | 15 | - | NEG -$216.6M | - | 500 | 475 | -$658k | +$0 bull / -$272k bear | out (clean 30, ADX 17, RVol 0.3) |
| 13 | **NVDA** | 168.20 | - | **-** | 15 | - | NEG -$158.8M | - | 180 | 170 | +$6.4M | +$377k bull / -$2.3M bear | out (clean 33, ADX 14, RVol 1.3) |
| 14 | **TSLA** | 377.81 | - | **-** | 14 | - | POS +$214.0M | - | 400 | 380 | -$7.8M | +$0 bull / -$302k bear | out (clean 32, ADX 10, RVol 0.3) |
| 15 | **MSTR** | 120.63 | - | **-** | 14 | - | NEG -$26.3M | - | 130 | 110 | +$454k | +$0 bull / -$146k bear | out (clean 29, ADX 13, RVol 0.6) |
| 16 | **SHOP** | 145.69 | - | **-** | 12 | - | POS +$386k | 144.92 | 150 | 140 | -$220k | - | out (clean 32, ADX 24, RVol 0.6) |
| 17 | **CRM** | 212.62 | - | **-** | 11 | - | NEG -$10.9M | - | 195 | 220 | +$298k | - | out (clean 31, ADX 17, RVol 0.3) |
| 18 | **UBER** | 69.82 | - | **-** | 10 | - | POS +$7.2M | 68.52 | 70 | 70 | -$74k | - | out (clean 34, ADX 25, RVol 0.6) |
| 19 | **HOOD** | 81.08 | - | **-** | 7 | - | POS +$1.5M | 80.1 | 85 | 80 | +$542k | - | out (clean 32, ADX 15, RVol 0.5) |
| 20 | **BABA** | 102.59 | - | **-** | 7 | - | NEG -$10.4M | 106.53 | 110 | 100 | -$170k | - | out (clean 30, ADX 18, RVol 0.7) |
| 21 | **QQQ** | 673.86 | - | **-** | 6 | - | NEG -$1.9B | 692.41 | 680 | 680 | -$12.3M | - | out (clean 32, ADX 28, RVol 0.5) |
| 22 | **NFLX** | 63.02 | - | **-** | 6 | - | NEG -$21.2M | 65.24 | 65 | 60 | -$203k | - | out (clean 29, ADX 17, RVol 0.7) |
| 23 | **COIN** | 131.84 | - | **-** | 6 | - | POS +$3.7M | 129.3 | 137 | 135 | +$132k | - | out (clean 28, ADX 18, RVol 1.0) |
| 24 | **DELL** | 332.44 | - | **-** | 6 | - | NEG -$10.8M | - | 350 | 340 | +$858k | - | out (clean 34, ADX 19, RVol 0.5) |
| 25 | **IWM** | 280.06 | - | **-** | 5 | - | NEG -$971.9M | 283.04 | 280 | 280 | +$1.4M | - | out (clean 34, ADX 16, RVol 0.5) |
| 26 | **SMCI** | 27.75 | - | **-** | 5 | - | POS +$1.1M | 26.57 | 30 | 25 | -$56k | - | out (clean 30, ADX 15, RVol 0.7) |
| 27 | **ORCL** | 117.87 | - | **-** | 4 | - | NEG -$24.8M | - | 120 | 120 | +$75k | - | out (clean 27, ADX 18, RVol 0.2) |

## Big prints this scan (31)
- **AMD** PUT 530 2026-11-11 (1DTE): 200 @ 18.50 = **+$370k** MID | vol 5,105 / OI 45
- **PLTR** CALL 160 2026-11-13 (3DTE): 250 @ 8.20 = **+$205k** SELL | vol 617 / OI 7,797
- **BABA** CALL 105 2026-11-13 (3DTE): 1,912 @ 0.97 = **+$185k** MID | vol 5,850 / OI 1,179
- **SPY** CALL 748 2026-11-10 (0DTE): 1,340 @ 1.32 = **+$177k** SELL | vol 474,122 / OI 4,785
- **AMD** CALL 515 2026-11-11 (1DTE): 100 @ 11.15 = **+$112k** BUY | vol 10,038 / OI 238
- **SPY** CALL 748 2026-11-13 (3DTE): 200 @ 5.27 = **+$105k** SELL | vol 10,455 / OI 1,196
- **NVDA** CALL 167.5 2026-11-16 (6DTE): 150 @ 5.75 = **+$86k** BUY | vol 5,369 / OI 9
- **NVDA** PUT 170 2026-11-11 (1DTE): 181 @ 4.15 = **+$75k** BUY | vol 137,235 / OI 4,288
- **MSTR** CALL 123 2026-11-13 (3DTE): 247 @ 3.00 = **+$74k** SELL | vol 3,927 / OI 65
- **NVDA** CALL 162.5 2026-11-11 (1DTE): 75 @ 6.56 = **+$49k** BUY | vol 2,198 / OI 26
- **MU** PUT 700 2026-11-16 (6DTE): 20 @ 21.09 = **+$42k** BUY | vol 237 / OI 139
- **AMD** CALL 500 2026-11-13 (3DTE): 16 @ 26.10 = **+$42k** MID | vol 5,325 / OI 2,434
- **NVDA** CALL 165 2026-11-11 (1DTE): 80 @ 4.87 = **+$39k** BUY | vol 12,001 / OI 99
- **NVDA** CALL 165 2026-11-11 (1DTE): 75 @ 4.71 = **+$35k** SELL | vol 12,001 / OI 99
- **META** CALL 630 2026-11-11 (1DTE): 22 @ 15.20 = **+$33k** SELL | vol 1,114 / OI 1,923

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 734 2026-11-13 (3DTE): 2,098 traded vs OI 2,010
- **SPY** CALL 782 2026-11-16 (6DTE): 567 traded vs OI 508
- **SPY** PUT 711 2026-11-11 (1DTE): 694 traded vs OI 313
- **SPY** CALL 749 2026-11-17 (7DTE): 521 traded vs OI 68
- **SPY** PUT 695 2026-11-16 (6DTE): 577 traded vs OI 384
- **SPY** CALL 745 2026-11-17 (7DTE): 511 traded vs OI 354
- **QQQ** PUT 618 2026-11-11 (1DTE): 713 traded vs OI 214
- **NVDA** PUT 155 2026-11-20 (10DTE): 11,466 traded vs OI 10,527
- **META** CALL 710 2026-11-20 (10DTE): 1,175 traded vs OI 0
- **META** CALL 700 2026-11-11 (1DTE): 659 traded vs OI 326

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
