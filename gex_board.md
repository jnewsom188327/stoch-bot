# GEX + FLOW SCAN - Tue Nov 10, 12:40 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (10)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 12:33 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 667P | 0.67 | 1.59 | +142% (6m) | **+137%** | +15% | 668.83 hit |
| 12:22 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 667P | 0.66 | 1.59 | +145% (17m) | **+141%** | +11% | 669.29 hit |
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
Last 1m check 12:40:08 ET, last candle SPY 12:39, QQQ 12:39 | no errors
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
| 1 | **MSFT** | 530.99 | FLOW SURGE | **CALLS** | 49 | none: 126 calls 0-7DTE > 10 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (11 contracts' greeks worked out here) | POS +$386.1M | 502.01 | 550 | 500 | +$10.0M | +$1.1M bull / +$0 bear | out (clean 32, ADX 36, RVol 2.4) |
| 2 | **NVDA** | 166.57 | TREND (flow not with it) | **PUTS** | 40 | none: 42 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (1 contracts' greeks worked out here) | NEG -$148.2M | - | 180 | 170 | +$14.8M | +$1.3M bull / -$1.7M bear | SHORT (clean 34, ADX 38, RVol 1.3) |
| 3 | **HOOD** | 80.14 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 30 | none: 16 calls 0-7DTE > 3 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only +15% at the target (needs +20%) (1 contracts' greeks worked out here) | POS +$953k | 79.33 | 85 | 80 | +$637k | - | out (clean 31, ADX 38, RVol 0.4) |
| 4 | **AAPL** | 347.69 | FLOW SURGE | **CALLS** | 29 | none: 81 calls 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (12 contracts' greeks worked out here) | POS +$424.4M | 336.13 | 350 | 340 | +$17.8M | +$211k bull / +$0 bear | out (clean 28, ADX 12, RVol 0.3) |
| 5 | **PLTR** | 164.71 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 26 | none: 14 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$49.0M | - | 165 | 160 | -$568k | - | out (clean 28, ADX 37, RVol 0.4) |
| 6 | **SHOP** | 142.60 | - | **-** | 25 | - | NEG -$1.6M | 146.77 | 150 | 140 | +$101k | - | out (clean 33, ADX 61, RVol 0.8) |
| 7 | **AMZN** | 268.12 | - | **-** | 21 | - | POS +$429.1M | - | 270 | 265 | +$9.0M | +$42k bull / +$0 bear | out (clean 33, ADX 23, RVol 0.7) |
| 8 | **GOOGL** | 285.91 | - | **-** | 21 | - | NEG -$32.6M | 289.13 | 300 | 290 | +$3.4M | +$43k bull / +$0 bear | out (clean 30, ADX 23, RVol 0.3) |
| 9 | **SPY** | 745.34 | - | **-** | 19 | - | NEG -$8.3B | 760.09 | 750 | 730 | +$88.9M | +$528k bull / -$369k bear | out (clean 32, ADX 30, RVol 0.5) |
| 10 | **AMD** | 501.53 | - | **-** | 19 | - | POS +$43.7M | - | 500 | 500 | -$27.6M | +$2.1M bull / -$577k bear | out (clean 33, ADX 31, RVol 0.6) |
| 11 | **MSTR** | 118.75 | - | **-** | 19 | - | NEG -$25.4M | - | 130 | 110 | +$484k | +$133k bull / +$0 bear | out (clean 29, ADX 34, RVol 1.0) |
| 12 | **QQQ** | 667.75 | - | **-** | 17 | - | NEG -$2.3B | 693.63 | 680 | 680 | +$39.3M | +$119k bull / -$358k bear | out (clean 32, ADX 33, RVol 0.2) |
| 13 | **AVGO** | 324.75 | - | **-** | 17 | - | NEG -$18.8M | 343.51 | 340 | 320 | -$7.9M | +$35k bull / -$63k bear | out (clean 32, ADX 16, RVol 0.4) |
| 14 | **SMH** | 474.81 | - | **-** | 16 | - | NEG -$240.1M | - | 500 | 475 | -$58k | +$0 bull / -$60k bear | out (clean 30, ADX 30, RVol 0.3) |
| 15 | **MU** | 701.53 | - | **-** | 16 | - | NEG -$41.3M | - | 750 | 750 | -$1.5M | +$2.9M bull / -$1.3M bear | out (clean 30, ADX 27, RVol 0.3) |
| 16 | **TSLA** | 375.31 | - | **-** | 15 | - | POS +$189.9M | - | 400 | 380 | -$2.6M | +$280k bull / -$331k bear | out (clean 33, ADX 20, RVol 0.2) |
| 17 | **META** | 639.16 | - | **-** | 15 | - | POS +$236.9M | 604.45 | 650 | 650 | +$571k | +$0 bull / -$57k bear | out (clean 32, ADX 21, RVol 0.6) |
| 18 | **ARM** | 176.29 | - | **-** | 13 | - | NEG -$4.5M | - | 185 | 185 | -$205k | - | out (clean 28, ADX 30, RVol 0.4) |
| 19 | **COIN** | 130.09 | - | **-** | 11 | - | POS +$212k | 129.43 | 137 | 120 | +$237k | - | out (clean 29, ADX 41, RVol 0.7) |
| 20 | **DELL** | 322.96 | - | **-** | 11 | - | NEG -$10.6M | - | 350 | 340 | +$1.2M | - | out (clean 33, ADX 38, RVol 0.5) |
| 21 | **UBER** | 69.50 | - | **-** | 11 | - | POS +$5.6M | 68.46 | 70 | 70 | -$52k | - | out (clean 33, ADX 35, RVol 0.4) |
| 22 | **ORCL** | 115.90 | - | **-** | 10 | - | NEG -$25.1M | - | 120 | 110 | +$648k | - | out (clean 28, ADX 33, RVol 0.4) |
| 23 | **BABA** | 102.71 | - | **-** | 10 | - | NEG -$10.3M | 106.64 | 110 | 100 | -$139k | - | out (clean 30, ADX 42, RVol 0.3) |
| 24 | **IWM** | 279.18 | - | **-** | 8 | - | NEG -$1.2B | 283.84 | 280 | 270 | +$3.0M | - | out (clean 36, ADX 32, RVol 0.4) |
| 25 | **SMCI** | 27.25 | - | **-** | 8 | - | NEG -$1.0M | - | 27 | 25 | +$25k | - | out (clean 30, ADX 36, RVol 0.5) |
| 26 | **CRM** | 209.79 | - | **-** | 8 | - | NEG -$10.6M | - | 195 | 220 | +$9k | - | out (clean 30, ADX 36, RVol 0.8) |
| 27 | **NFLX** | 62.69 | - | **-** | 5 | - | NEG -$24.5M | 65.82 | 65 | 60 | -$77k | - | out (clean 30, ADX 21, RVol 0.4) |

## Big prints this scan (90)
- **SPY** PUT 755 2026-11-13 (3DTE): 456 @ 9.38 = **+$428k** SELL | vol 1,641 / OI 7,196
- **NVDA** CALL 167.5 2026-11-11 (1DTE): 1,000 @ 3.20 = **+$320k** BUY | vol 23,702 / OI 80
- **AMD** CALL 510 2026-11-11 (1DTE): 298 @ 10.10 = **+$301k** BUY | vol 8,495 / OI 407
- **AAPL** CALL 340 2026-11-11 (1DTE): 240 @ 8.80 = **+$211k** BUY | vol 1,234 / OI 511
- **MSFT** CALL 540 2026-11-11 (1DTE): 405 @ 3.95 = **+$160k** BUY | vol 1,794 / OI 407
- **QQQ** PUT 673 2026-11-10 (0DTE): 323 @ 3.69 = **+$119k** SELL | vol 137,335 / OI 98
- **NVDA** PUT 167.5 2026-11-11 (1DTE): 275 @ 3.10 = **+$85k** SELL | vol 97,957 / OI 819
- **NVDA** CALL 167.5 2026-11-11 (1DTE): 247 @ 3.20 = **+$79k** BUY | vol 23,702 / OI 80
- **NVDA** CALL 170 2026-11-11 (1DTE): 400 @ 1.95 = **+$78k** BUY | vol 82,458 / OI 252
- **AMD** PUT 490 2026-11-13 (3DTE): 75 @ 9.25 = **+$69k** SELL | vol 1,314 / OI 647
- **MSFT** PUT 545 2026-11-16 (6DTE): 55 @ 12.15 = **+$67k** SELL | vol 156 / OI 38
- **MSFT** PUT 535 2026-11-11 (1DTE): 430 @ 1.50 = **+$64k** SELL | vol 7,457 / OI 406
- **MSFT** PUT 535 2026-11-11 (1DTE): 198 @ 3.10 = **+$61k** SELL | vol 7,457 / OI 406
- **TSLA** CALL 380 2026-11-13 (3DTE): 110 @ 5.45 = **+$60k** BUY | vol 6,471 / OI 7,571
- **MU** CALL 717.5 2026-11-11 (1DTE): 50 @ 11.20 = **+$56k** BUY | vol 2,987 / OI 88

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 735 2026-11-12 (2DTE): 2,539 traded vs OI 2,530
- **SPY** CALL 813 2026-11-13 (3DTE): 598 traded vs OI 349
- **SPY** CALL 762 2026-11-13 (3DTE): 3,048 traded vs OI 3,028
- **SPY** CALL 809 2026-11-13 (3DTE): 922 traded vs OI 893
- **SPY** CALL 753 2026-11-16 (6DTE): 500 traded vs OI 164
- **SPY** CALL 764 2026-11-13 (3DTE): 2,708 traded vs OI 2,528
- **SPY** PUT 732 2026-11-12 (2DTE): 566 traded vs OI 483
- **SPY** PUT 735 2026-11-23 (13DTE): 598 traded vs OI 0
- **IWM** PUT 279 2026-11-16 (6DTE): 516 traded vs OI 138
- **IWM** CALL 281 2026-11-13 (3DTE): 1,521 traded vs OI 1,430
- **IWM** PUT 274 2026-11-13 (3DTE): 1,170 traded vs OI 975
- **NVDA** PUT 150 2026-11-18 (8DTE): 1,286 traded vs OI 0
- **NVDA** PUT 150 2026-11-16 (6DTE): 3,176 traded vs OI 0
- **NVDA** CALL 150 2026-11-13 (3DTE): 1,716 traded vs OI 0
- **NVDA** PUT 150 2026-11-13 (3DTE): 11,670 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
