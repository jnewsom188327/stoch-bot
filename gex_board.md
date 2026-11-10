# GEX + FLOW SCAN - Tue Nov 10, 03:45 PM ET
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
| 1 | **AAPL** | 349.27 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 40 | none: 84 puts 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (23 contracts' greeks worked out here) | POS +$463.2M | 337.18 | 350 | 340 | +$16.2M | +$0 bull / -$61k bear | out (clean 28, ADX 17, RVol 0.6) |
| 2 | **MSFT** | 534.18 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 25 | none: 129 calls 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (17 contracts' greeks worked out here) | POS +$453.5M | 506.73 | 550 | 535 | +$10.8M | - | out (clean 32, ADX 15, RVol 0.4) |
| 3 | **AVGO** | 331.47 | - | **-** | 21 | - | NEG -$3.5M | 334.02 | 340 | 340 | -$11.3M | +$96k bull / -$32k bear | out (clean 34, ADX 32, RVol 0.7) |
| 4 | **META** | 644.18 | - | **-** | 18 | - | POS +$278.9M | 606.57 | 650 | 650 | -$1.5M | +$31k bull / -$33k bear | out (clean 32, ADX 36, RVol 0.6) |
| 5 | **SPY** | 749.26 | - | **-** | 17 | - | NEG -$5.9B | 760.09 | 750 | 750 | +$6.0M | +$2.6M bull / -$417k bear | out (clean 32, ADX 31, RVol 0.6) |
| 6 | **AMD** | 512.63 | - | **-** | 17 | - | POS +$43.9M | - | 500 | 500 | -$48.7M | +$688k bull / +$0 bear | out (clean 33, ADX 20, RVol 0.6) |
| 7 | **GOOGL** | 287.32 | - | **-** | 17 | - | NEG -$15.8M | 288.83 | 300 | 290 | +$1.9M | +$158k bull / +$0 bear | out (clean 29, ADX 21, RVol 0.5) |
| 8 | **PLTR** | 167.32 | - | **-** | 17 | - | POS +$54.7M | - | 165 | 170 | -$909k | +$0 bull / -$232k bear | out (clean 29, ADX 22, RVol 0.3) |
| 9 | **QQQ** | 673.38 | - | **-** | 16 | - | NEG -$1.8B | 692.75 | 680 | 680 | -$2k | +$359k bull / +$0 bear | out (clean 32, ADX 28, RVol 0.6) |
| 10 | **DELL** | 332.39 | - | **-** | 16 | - | NEG -$10.8M | - | 350 | 340 | +$974k | +$75k bull / +$0 bear | out (clean 34, ADX 20, RVol 0.5) |
| 11 | **MU** | 715.23 | - | **-** | 16 | - | NEG -$30.2M | - | 750 | 750 | -$20.6M | +$1.1M bull / -$188k bear | out (clean 31, ADX 23, RVol 0.4) |
| 12 | **NVDA** | 168.13 | - | **-** | 15 | - | NEG -$160.0M | - | 180 | 170 | +$12.6M | +$2.6M bull / -$136k bear | out (clean 33, ADX 12, RVol 1.0) |
| 13 | **ORCL** | 117.40 | - | **-** | 15 | - | NEG -$25.4M | - | 120 | 120 | +$568k | +$65k bull / +$0 bear | out (clean 27, ADX 17, RVol 0.3) |
| 14 | **SMH** | 481.88 | - | **-** | 14 | - | NEG -$217.0M | - | 500 | 475 | -$447k | +$31k bull / +$0 bear | out (clean 30, ADX 15, RVol 0.3) |
| 15 | **TSLA** | 377.46 | - | **-** | 14 | - | POS +$207.0M | - | 400 | 380 | -$7.2M | +$57k bull / +$0 bear | out (clean 32, ADX 10, RVol 0.3) |
| 16 | **MSTR** | 120.49 | - | **-** | 14 | - | NEG -$26.6M | - | 130 | 110 | +$637k | +$26k bull / -$74k bear | out (clean 29, ADX 12, RVol 0.7) |
| 17 | **ARM** | 180.36 | - | **-** | 14 | - | NEG -$5.2M | - | 185 | 190 | -$342k | - | out (clean 27, ADX 30, RVol 0.4) |
| 18 | **SHOP** | 145.88 | - | **-** | 13 | - | POS +$365k | 145.23 | 150 | 140 | -$224k | - | out (clean 32, ADX 26, RVol 0.7) |
| 19 | **CRM** | 212.21 | - | **-** | 11 | - | NEG -$11.0M | - | 195 | 220 | +$287k | - | out (clean 31, ADX 18, RVol 0.4) |
| 20 | **UBER** | 69.69 | - | **-** | 9 | - | POS +$7.3M | 68.47 | 70 | 70 | -$69k | - | out (clean 34, ADX 24, RVol 0.6) |
| 21 | **AMZN** | 271.01 | - | **-** | 8 | - | POS +$490.5M | - | 270 | 265 | -$287k | - | out (clean 34, ADX 40, RVol 0.6) |
| 22 | **HOOD** | 80.77 | - | **-** | 8 | - | POS +$1.5M | 79.98 | 85 | 80 | +$596k | - | out (clean 32, ADX 14, RVol 1.1) |
| 23 | **NFLX** | 62.98 | - | **-** | 7 | - | NEG -$20.6M | 65.27 | 65 | 60 | -$211k | - | out (clean 29, ADX 18, RVol 0.9) |
| 24 | **COIN** | 131.90 | - | **-** | 7 | - | POS +$3.8M | 129.34 | 137 | 135 | +$146k | - | out (clean 28, ADX 19, RVol 1.1) |
| 25 | **IWM** | 280.19 | - | **-** | 5 | - | NEG -$904.0M | 282.93 | 280 | 280 | +$1.6M | - | out (clean 34, ADX 16, RVol 0.7) |
| 26 | **BABA** | 102.59 | - | **-** | 5 | - | NEG -$9.8M | 106.29 | 110 | 100 | -$38k | - | out (clean 30, ADX 16, RVol 0.7) |
| 27 | **SMCI** | 27.76 | - | **-** | 4 | - | POS +$1.2M | 26.53 | 30 | 25 | -$38k | - | out (clean 30, ADX 15, RVol 0.6) |

## Big prints this scan (53)
- **SPY** PUT 760 2026-11-13 (3DTE): 1,835 @ 11.24 = **+$2.1M** SELL | vol 47,329 / OI 5,844
- **AMD** CALL 515 2026-11-11 (1DTE): 200 @ 11.45 = **+$229k** BUY | vol 10,737 / OI 238
- **SPY** CALL 749 2026-11-10 (0DTE): 1,625 @ 0.90 = **+$146k** BUY | vol 451,963 / OI 1,190
- **QQQ** PUT 671 2026-11-12 (2DTE): 300 @ 4.65 = **+$140k** SELL | vol 1,784 / OI 102
- **NVDA** CALL 160 2026-11-13 (3DTE): 100 @ 10.22 = **+$102k** BUY | vol 2,328 / OI 144
- **QQQ** CALL 674 2026-11-10 (0DTE): 932 @ 1.08 = **+$101k** BUY | vol 254,024 / OI 417
- **NVDA** CALL 167.5 2026-11-11 (1DTE): 251 @ 3.30 = **+$83k** BUY | vol 86,406 / OI 80
- **GOOGL** CALL 287.5 2026-11-13 (3DTE): 200 @ 4.05 = **+$81k** BUY | vol 1,235 / OI 846
- **MU** PUT 740 2026-11-11 (1DTE): 30 @ 27.00 = **+$81k** SELL | vol 2,489 / OI 137
- **GOOGL** CALL 287.5 2026-11-13 (3DTE): 193 @ 4.00 = **+$77k** BUY | vol 1,235 / OI 846
- **MU** CALL 715 2026-11-13 (3DTE): 30 @ 25.50 = **+$76k** BUY | vol 1,367 / OI 240
- **NVDA** PUT 175 2026-11-11 (1DTE): 100 @ 7.30 = **+$73k** SELL | vol 19,599 / OI 3,758
- **AMD** CALL 517.5 2026-11-13 (3DTE): 40 @ 16.30 = **+$65k** BUY | vol 1,258 / OI 388
- **NVDA** CALL 165 2026-11-13 (3DTE): 100 @ 6.50 = **+$65k** BUY | vol 7,478 / OI 157
- **AVGO** CALL 325 2026-11-11 (1DTE): 62 @ 9.45 = **+$59k** BUY | vol 6,682 / OI 128

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 746 2026-11-17 (7DTE): 514 traded vs OI 99
- **SPY** PUT 743 2026-11-20 (10DTE): 3,162 traded vs OI 2,534
- **SPY** CALL 750 2026-11-27 (17DTE): 687 traded vs OI 676
- **QQQ** CALL 706 2026-11-13 (3DTE): 644 traded vs OI 432
- **NVDA** CALL 160 2026-11-27 (17DTE): 553 traded vs OI 62
- **META** CALL 637.5 2026-11-13 (3DTE): 501 traded vs OI 149
- **GOOGL** CALL 287.5 2026-11-13 (3DTE): 1,235 traded vs OI 846
- **PLTR** PUT 157.5 2026-11-13 (3DTE): 2,453 traded vs OI 2,169
- **MU** PUT 665 2026-11-13 (3DTE): 518 traded vs OI 329
- **ORCL** PUT 118 2026-11-20 (10DTE): 1,108 traded vs OI 704
- **BABA** CALL 104 2026-11-13 (3DTE): 1,422 traded vs OI 749

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
