# GEX + FLOW SCAN - Tue Nov 10, 12:30 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (9)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 12:22 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 667P | 0.66 | 0.70 | +36% (4m) | **+6%** | +11% | 669.29 |
| 11:18 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 668P | 0.74 | 0.69 | +84% (38m) | **-7%** (done) | +18% | 672.3 hit |
| 11:17 | **SPY** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 744P | 0.60 | 0.36 | +38% (32m) | **-40%** (done) | +41% | 746.01 hit |
| 11:12 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 669P | 0.74 | 1.07 | +135% (44m) | **+45%** (done) | +38% | 671.74 hit |
| 11:12 | **SPY** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 744P | 0.64 | 0.38 | +30% (37m) | **-41%** (done) | +40% | 745.88 |
| 11:06 | **SPY** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 744P | 0.68 | 0.60 | +22% (43m) | **-12%** (done) | +49% | 745.54 |
| 10:15 | **IWM** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/10 280P | 0.63 | 1.39 | +232% (36m) | **+121%** (done) | +22% | 280 hit |
| 09:50 | **SPY** | **PUTS** | FLOW SURGE | 11/10 743P | 0.77 | 0.62 | +21% (60m) | **-19%** (done) | +54% | 745.65 |
| 09:45 | **IWM** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/10 279P | 0.52 | 0.95 | +90% (60m) | **+83%** (done) | +87% | 278.66 |

## 1m RULES on SPY / QQQ - loose (8 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 12:30:08 ET, last candle SPY 12:29, QQQ 12:29 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
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
| 1 | **MSFT** | 534.21 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 42 | none: 129 calls 0-7DTE > 10 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (37 contracts' greeks worked out here) | POS +$486.0M | - | 550 | 535 | -$310k | +$42k bull / -$28k bear | out (clean 32, ADX 30, RVol 1.5) |
| 2 | **NVDA** | 167.54 | TREND (flow not with it) | **PUTS** | 40 | none: 39 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (2 contracts' greeks worked out here) | NEG -$154.0M | - | 180 | 170 | +$11.6M | +$153k bull / -$3.8M bear | SHORT (clean 34, ADX 38, RVol 1.3) |
| 3 | **PLTR** | 165.24 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 38 | none: 14 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (1 contracts' greeks worked out here) | POS +$50.5M | - | 165 | 170 | -$887k | +$71k bull / -$1.1M bear | out (clean 28, ADX 38, RVol 0.5) |
| 4 | **AAPL** | 348.21 | FLOW SURGE | **CALLS** | 29 | none: 84 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (28 contracts' greeks worked out here) | POS +$427.8M | 336.13 | 350 | 340 | +$17.4M | +$25k bull / +$0 bear | out (clean 28, ADX 13, RVol 0.3) |
| 5 | **SHOP** | 144.18 | - | **-** | 24 | - | NEG -$593k | 145.4 | 150 | 140 | +$93k | - | out (clean 33, ADX 59, RVol 0.7) |
| 6 | **AMD** | 508.74 | - | **-** | 19 | - | POS +$46.3M | - | 500 | 500 | -$30.2M | +$1.1M bull / -$4.0M bear | out (clean 32, ADX 29, RVol 0.6) |
| 7 | **SPY** | 746.88 | - | **-** | 18 | - | NEG -$7.5B | 759.92 | 750 | 730 | +$66.6M | +$100k bull / -$909k bear | out (clean 32, ADX 30, RVol 0.5) |
| 8 | **AVGO** | 325.89 | - | **-** | 18 | - | NEG -$16.6M | 342.59 | 340 | 320 | -$8.6M | +$0 bull / -$93k bear | out (clean 32, ADX 17, RVol 0.5) |
| 9 | **MSTR** | 119.65 | - | **-** | 18 | - | NEG -$25.1M | - | 130 | 110 | +$266k | +$85k bull / +$0 bear | out (clean 29, ADX 34, RVol 0.8) |
| 10 | **QQQ** | 670.06 | - | **-** | 17 | - | NEG -$2.1B | 692.09 | 680 | 680 | +$19.9M | +$0 bull / -$5.0M bear | out (clean 32, ADX 32, RVol 0.2) |
| 11 | **SMH** | 477.58 | - | **-** | 16 | - | NEG -$225.6M | - | 500 | 475 | -$198k | +$0 bull / -$60k bear | out (clean 30, ADX 29, RVol 0.4) |
| 12 | **MU** | 707.18 | - | **-** | 16 | - | NEG -$31.7M | - | 750 | 750 | -$6.8M | +$492k bull / -$2.7M bear | out (clean 30, ADX 27, RVol 0.4) |
| 13 | **TSLA** | 376.02 | - | **-** | 15 | - | POS +$190.8M | - | 400 | 380 | -$3.6M | +$191k bull / -$986k bear | out (clean 33, ADX 21, RVol 0.2) |
| 14 | **META** | 640.26 | - | **-** | 15 | - | POS +$240.6M | 602.48 | 650 | 650 | -$54k | +$30k bull / -$386k bear | out (clean 32, ADX 20, RVol 0.5) |
| 15 | **ARM** | 177.75 | - | **-** | 13 | - | NEG -$4.8M | - | 185 | 190 | -$218k | - | out (clean 28, ADX 31, RVol 0.3) |
| 16 | **CRM** | 209.95 | - | **-** | 13 | - | NEG -$10.3M | - | 195 | 220 | -$83k | - | out (clean 30, ADX 32, RVol 0.6) |
| 17 | **HOOD** | 80.61 | - | **-** | 12 | - | POS +$2.0M | 79.28 | 85 | 80 | +$532k | - | out (clean 31, ADX 38, RVol 0.6) |
| 18 | **GOOGL** | 286.82 | - | **-** | 11 | - | NEG -$21.5M | 288.87 | 300 | 290 | +$3.1M | - | out (clean 30, ADX 20, RVol 0.4) |
| 19 | **COIN** | 130.55 | - | **-** | 11 | - | POS +$1.7M | 129.34 | 137 | 135 | +$151k | - | out (clean 29, ADX 42, RVol 0.7) |
| 20 | **UBER** | 69.68 | - | **-** | 11 | - | POS +$6.7M | 68.46 | 70 | 70 | -$54k | - | out (clean 33, ADX 36, RVol 0.3) |
| 21 | **BABA** | 102.97 | - | **-** | 11 | - | NEG -$8.3M | 105.99 | 110 | 100 | -$164k | - | out (clean 30, ADX 42, RVol 0.4) |
| 22 | **AMZN** | 269.04 | - | **-** | 10 | - | POS +$462.1M | - | 270 | 265 | +$8.7M | - | out (clean 33, ADX 22, RVol 0.6) |
| 23 | **DELL** | 326.31 | - | **-** | 10 | - | NEG -$10.6M | - | 350 | 340 | +$1.1M | - | out (clean 33, ADX 36, RVol 0.5) |
| 24 | **IWM** | 279.42 | - | **-** | 9 | - | NEG -$1.1B | 283.36 | 280 | 270 | +$3.4M | - | out (clean 36, ADX 36, RVol 0.4) |
| 25 | **ORCL** | 116.89 | - | **-** | 9 | - | NEG -$24.4M | - | 120 | 120 | +$472k | - | out (clean 28, ADX 30, RVol 0.3) |
| 26 | **SMCI** | 27.38 | - | **-** | 8 | - | POS +$941k | 26.33 | 30 | 25 | -$20k | - | out (clean 30, ADX 35, RVol 0.5) |
| 27 | **NFLX** | 62.75 | - | **-** | 5 | - | NEG -$23.2M | 65.4 | 65 | 60 | -$99k | - | out (clean 31, ADX 21, RVol 0.4) |

## Big prints this scan (77)
- **NVDA** CALL 167.5 2026-11-13 (3DTE): 255 @ 4.80 = **+$122k** SELL | vol 8,478 / OI 18
- **NVDA** CALL 162.5 2026-11-13 (3DTE): 155 @ 7.78 = **+$121k** SELL | vol 791 / OI 0
- **NVDA** CALL 167.5 2026-11-13 (3DTE): 243 @ 4.80 = **+$117k** SELL | vol 8,478 / OI 18
- **SPY** CALL 748 2026-11-13 (3DTE): 200 @ 5.01 = **+$100k** BUY | vol 6,298 / OI 1,196
- **MU** CALL 700 2026-11-11 (1DTE): 50 @ 19.89 = **+$99k** SELL | vol 1,840 / OI 348
- **AMD** CALL 525 2026-11-11 (1DTE): 196 @ 5.00 = **+$98k** BUY | vol 10,357 / OI 146
- **MU** CALL 705 2026-11-11 (1DTE): 50 @ 17.04 = **+$85k** SELL | vol 1,604 / OI 114
- **AMD** CALL 525 2026-11-11 (1DTE): 168 @ 5.00 = **+$84k** BUY | vol 10,357 / OI 146
- **MU** PUT 710 2026-11-11 (1DTE): 50 @ 16.50 = **+$82k** MID | vol 8,208 / OI 128
- **NVDA** CALL 170 2026-11-11 (1DTE): 402 @ 1.91 = **+$77k** SELL | vol 77,368 / OI 252
- **NVDA** CALL 167.5 2026-11-13 (3DTE): 155 @ 4.77 = **+$74k** SELL | vol 8,478 / OI 18
- **MU** CALL 742.5 2026-11-11 (1DTE): 190 @ 3.85 = **+$73k** SELL | vol 2,286 / OI 153
- **TSLA** CALL 377.5 2026-11-11 (1DTE): 199 @ 3.55 = **+$71k** SELL | vol 27,730 / OI 273
- **TSLA** CALL 377.5 2026-11-11 (1DTE): 200 @ 3.53 = **+$71k** SELL | vol 27,730 / OI 273
- **AMD** PUT 510 2026-11-11 (1DTE): 60 @ 11.36 = **+$68k** BUY | vol 6,483 / OI 85

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 741 2026-11-12 (2DTE): 504 traded vs OI 350
- **SPY** CALL 770 2026-11-13 (3DTE): 8,970 traded vs OI 8,618
- **SPY** PUT 728 2026-11-13 (3DTE): 1,473 traded vs OI 1,470
- **SPY** CALL 756 2026-11-16 (6DTE): 502 traded vs OI 296
- **SPY** PUT 740 2026-11-13 (3DTE): 8,771 traded vs OI 8,686
- **SPY** PUT 690 2026-11-18 (8DTE): 590 traded vs OI 356
- **SPY** CALL 805 2026-11-17 (7DTE): 900 traded vs OI 92
- **SPY** CALL 798 2026-11-17 (7DTE): 1,176 traded vs OI 224
- **QQQ** PUT 661 2026-11-13 (3DTE): 647 traded vs OI 645
- **QQQ** PUT 657 2026-11-13 (3DTE): 589 traded vs OI 579
- **QQQ** PUT 663 2026-11-13 (3DTE): 524 traded vs OI 245
- **QQQ** CALL 705 2026-11-23 (13DTE): 503 traded vs OI 0
- **IWM** PUT 275 2026-11-16 (6DTE): 773 traded vs OI 252
- **NVDA** CALL 155 2026-11-11 (1DTE): 503 traded vs OI 33
- **NVDA** CALL 167.5 2026-11-27 (17DTE): 511 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
