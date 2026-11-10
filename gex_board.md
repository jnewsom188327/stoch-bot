# GEX + FLOW SCAN - Tue Nov 10, 02:30 PM ET
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
Last 1m check 14:30:08 ET, last candle SPY 14:29, QQQ 14:29 | no errors
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
| 1 | **MSFT** | 535.17 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 38 | none: 129 calls 0-7DTE > 8 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (13 contracts' greeks worked out here) | POS +$471.3M | 506.45 | 550 | 535 | +$12.2M | +$31k bull / -$27k bear | out (clean 32, ADX 27, RVol 0.4) |
| 2 | **AMZN** | 270.49 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 34 | none: 66 puts 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (8 contracts' greeks worked out here) | POS +$472.9M | - | 270 | 265 | +$2.6M | +$0 bull / -$180k bear | out (clean 33, ADX 21, RVol 0.5) |
| 3 | **AVGO** | 330.62 | - | **-** | 20 | - | NEG -$10.3M | 341.08 | 340 | 340 | -$11.8M | +$50k bull / -$80k bear | out (clean 33, ADX 26, RVol 0.6) |
| 4 | **HOOD** | 80.80 | - | **-** | 18 | - | POS +$2.1M | 79.36 | 85 | 80 | +$551k | +$0 bull / -$26k bear | out (clean 32, ADX 23, RVol 0.2) |
| 5 | **AMD** | 512.68 | - | **-** | 17 | - | POS +$51.8M | - | 500 | 500 | -$47.3M | +$1.4M bull / -$177k bear | out (clean 34, ADX 19, RVol 0.3) |
| 6 | **DELL** | 330.71 | - | **-** | 17 | - | NEG -$10.9M | - | 350 | 340 | +$935k | +$31k bull / +$0 bear | out (clean 34, ADX 23, RVol 0.4) |
| 7 | **SPY** | 748.56 | - | **-** | 16 | - | NEG -$6.8B | 760.31 | 750 | 750 | +$33.5M | +$0 bull / -$252k bear | out (clean 32, ADX 24, RVol 0.4) |
| 8 | **PLTR** | 166.08 | - | **-** | 16 | - | POS +$51.8M | - | 165 | 170 | -$895k | +$59k bull / +$0 bear | out (clean 28, ADX 18, RVol 0.3) |
| 9 | **QQQ** | 671.95 | - | **-** | 15 | - | NEG -$2.0B | 692.08 | 680 | 680 | -$590k | +$2.0M bull / -$260k bear | out (clean 33, ADX 25, RVol 0.2) |
| 10 | **NVDA** | 167.61 | - | **-** | 15 | - | NEG -$158.3M | - | 180 | 170 | +$7.0M | +$720k bull / -$352k bear | out (clean 34, ADX 15, RVol 1.0) |
| 11 | **MU** | 710.56 | - | **-** | 15 | - | NEG -$35.1M | - | 750 | 750 | -$20.9M | +$666k bull / -$118k bear | out (clean 31, ADX 19, RVol 0.1) |
| 12 | **IWM** | 280.02 | - | **-** | 14 | - | NEG -$957.9M | 283.09 | 280 | 270 | +$1.7M | +$0 bull / -$66k bear | out (clean 36, ADX 16, RVol 0.3) |
| 13 | **META** | 641.85 | - | **-** | 14 | - | POS +$249.2M | 607.26 | 650 | 650 | -$415k | +$0 bull / -$235k bear | out (clean 32, ADX 17, RVol 0.3) |
| 14 | **TSLA** | 377.88 | - | **-** | 13 | - | POS +$201.5M | - | 400 | 380 | -$7.5M | +$0 bull / -$256k bear | out (clean 32, ADX 10, RVol 0.3) |
| 15 | **AAPL** | 348.35 | - | **-** | 12 | - | POS +$442.8M | 336.46 | 350 | 340 | +$16.9M | - | out (clean 28, ADX 12, RVol 0.4) |
| 16 | **ARM** | 178.60 | - | **-** | 12 | - | NEG -$4.9M | - | 185 | 185 | -$217k | - | out (clean 28, ADX 20, RVol 1.2) |
| 17 | **CRM** | 210.90 | - | **-** | 12 | - | NEG -$10.8M | - | 195 | 220 | +$312k | - | out (clean 31, ADX 24, RVol 0.3) |
| 18 | **SHOP** | 144.90 | - | **-** | 11 | - | NEG -$40k | 144.91 | 150 | 140 | -$187k | - | out (clean 33, ADX 23, RVol 0.6) |
| 19 | **UBER** | 69.51 | - | **-** | 9 | - | POS +$5.3M | 68.5 | 70 | 70 | -$56k | - | out (clean 33, ADX 29, RVol 0.2) |
| 20 | **GOOGL** | 287.20 | - | **-** | 8 | - | NEG -$18.2M | 288.9 | 300 | 290 | +$2.5M | - | out (clean 29, ADX 22, RVol 0.3) |
| 21 | **BABA** | 102.55 | - | **-** | 8 | - | NEG -$9.7M | 106.09 | 110 | 100 | -$156k | - | out (clean 30, ADX 29, RVol 0.6) |
| 22 | **COIN** | 130.92 | - | **-** | 6 | - | POS +$2.6M | 129.01 | 137 | 135 | +$204k | - | out (clean 28, ADX 20, RVol 0.3) |
| 23 | **ORCL** | 117.23 | - | **-** | 6 | - | NEG -$25.2M | - | 120 | 120 | +$305k | - | out (clean 28, ADX 24, RVol 0.1) |
| 24 | **NFLX** | 62.88 | - | **-** | 5 | - | NEG -$21.5M | 65.23 | 65 | 60 | -$177k | - | out (clean 29, ADX 16, RVol 0.6) |
| 25 | **SMCI** | 27.58 | - | **-** | 5 | - | POS +$1.0M | 26.43 | 30 | 25 | -$50k | - | out (clean 30, ADX 20, RVol 0.3) |
| 26 | **SMH** | 480.68 | - | **-** | 4 | - | NEG -$221.8M | - | 500 | 475 | -$17k | - | out (clean 30, ADX 19, RVol 0.1) |
| 27 | **MSTR** | 120.40 | - | **-** | 4 | - | NEG -$21.0M | - | 132 | 110 | +$347k | - | out (clean 30, ADX 14, RVol 0.4) |

## Big prints this scan (51)
- **QQQ** CALL 685 2026-11-13 (3DTE): 2,000 @ 2.22 = **+$444k** BUY | vol 8,002 / OI 1,402
- **AMD** CALL 515 2026-11-11 (1DTE): 310 @ 9.70 = **+$301k** BUY | vol 7,727 / OI 238
- **QQQ** PUT 675 2026-11-10 (0DTE): 1,000 @ 2.79 = **+$279k** SELL | vol 139,811 / OI 718
- **SPY** CALL 748 2026-11-13 (3DTE): 500 @ 5.05 = **+$252k** SELL | vol 9,068 / OI 1,196
- **QQQ** PUT 674 2026-11-11 (1DTE): 459 @ 5.03 = **+$231k** SELL | vol 11,531 / OI 824
- **QQQ** CALL 674 2026-11-11 (1DTE): 545 @ 3.55 = **+$193k** BUY | vol 16,327 / OI 202
- **QQQ** PUT 675 2026-11-10 (0DTE): 614 @ 2.75 = **+$169k** SELL | vol 139,811 / OI 718
- **QQQ** PUT 674 2026-11-11 (1DTE): 295 @ 5.21 = **+$154k** BUY | vol 11,531 / OI 824
- **QQQ** PUT 673 2026-11-10 (0DTE): 1,000 @ 1.40 = **+$140k** SELL | vol 150,711 / OI 98
- **AMD** CALL 505 2026-11-13 (3DTE): 50 @ 21.80 = **+$109k** BUY | vol 2,007 / OI 582
- **QQQ** PUT 674 2026-11-11 (1DTE): 204 @ 5.21 = **+$106k** BUY | vol 11,531 / OI 824
- **QQQ** PUT 675 2026-11-10 (0DTE): 386 @ 2.75 = **+$106k** SELL | vol 139,811 / OI 718
- **AMD** CALL 515 2026-11-11 (1DTE): 105 @ 9.70 = **+$102k** BUY | vol 7,727 / OI 238
- **AMD** CALL 510 2026-11-11 (1DTE): 75 @ 11.55 = **+$87k** BUY | vol 16,024 / OI 407
- **AMD** CALL 510 2026-11-11 (1DTE): 73 @ 11.55 = **+$84k** BUY | vol 16,024 / OI 407

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 733 2026-11-13 (3DTE): 1,656 traded vs OI 1,578
- **SPY** CALL 749 2026-11-20 (10DTE): 2,096 traded vs OI 2,086
- **SPY** CALL 756 2026-11-17 (7DTE): 522 traded vs OI 147
- **QQQ** PUT 653 2026-11-12 (2DTE): 556 traded vs OI 409
- **QQQ** CALL 694 2026-11-13 (3DTE): 770 traded vs OI 701
- **NVDA** CALL 170 2026-11-23 (13DTE): 1,275 traded vs OI 0
- **TSLA** CALL 402.5 2026-11-13 (3DTE): 930 traded vs OI 912
- **AAPL** PUT 330 2026-11-16 (6DTE): 1,265 traded vs OI 690

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
