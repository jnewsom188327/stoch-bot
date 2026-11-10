# GEX + FLOW SCAN - Tue Nov 10, 11:30 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (8)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:18 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 668P | 0.74 | 0.58 | +1% (9m) | **-22%** | +18% | 672.3 |
| 11:17 | **SPY** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 744P | 0.60 | 0.52 | +22% (1m) | **-13%** | +41% | 746.01 |
| 11:12 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 669P | 0.74 | 0.71 | +35% (15m) | **-4%** | +38% | 671.74 |
| 11:12 | **SPY** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 744P | 0.64 | 0.52 | +14% (6m) | **-19%** | +40% | 745.88 |
| 11:06 | **SPY** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 744P | 0.68 | 0.52 | +12% (0m) | **-24%** | +49% | 745.54 |
| 10:15 | **IWM** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/10 280P | 0.63 | 1.39 | +232% (36m) | **+121%** (done) | +22% | 280 hit |
| 09:50 | **SPY** | **PUTS** | FLOW SURGE | 11/10 743P | 0.77 | 0.62 | +21% (60m) | **-19%** (done) | +54% | 745.65 |
| 09:45 | **IWM** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/10 279P | 0.52 | 0.95 | +90% (60m) | **+83%** (done) | +87% | 278.66 |

## 1m RULES on SPY / QQQ - loose (7 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 11:30:08 ET, last candle SPY 11:29, QQQ 11:29 | no errors
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
| 1 | **AAPL** | 347.41 | FLOW SURGE | **CALLS** | 33 | none: 81 calls 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (15 contracts' greeks worked out here) | POS +$392.8M | 335.96 | 350 | 340 | +$18.3M | +$34k bull / +$0 bear | out (clean 28, ADX 18, RVol 0.5) |
| 2 | **IWM** | 278.95 | TREND (flow not with it) | **PUTS** | 25 | 11/10 279P @ 0.71 (delta 0.51) = est +102% at 277.63 | NEG -$1.3B | 283.79 | 280 | 270 | +$2.9M | - | SHORT (clean 36, ADX 47, RVol 0.5) |
| 3 | **GOOGL** | 287.24 | - | **-** | 22 | - | NEG -$19.8M | 289.08 | 300 | 290 | +$2.9M | +$178k bull / +$0 bear | out (clean 30, ADX 18, RVol 0.9) |
| 4 | **BABA** | 103.09 | - | **-** | 21 | - | NEG -$8.8M | 106.23 | 110 | 100 | -$199k | +$30k bull / +$0 bear | out (clean 30, ADX 38, RVol 0.5) |
| 5 | **NVDA** | 169.10 | - | **-** | 20 | - | NEG -$170.4M | - | 185 | 170 | +$4.1M | +$5.1M bull / -$108k bear | out (clean 33, ADX 36, RVol 1.8) |
| 6 | **AMD** | 521.72 | - | **-** | 20 | - | POS +$44.4M | - | 500 | 500 | -$54.5M | +$3.2M bull / -$559k bear | out (clean 31, ADX 21, RVol 0.9) |
| 7 | **AMZN** | 269.02 | - | **-** | 20 | - | POS +$463.1M | - | 270 | 265 | +$8.9M | +$225k bull / +$0 bear | out (clean 33, ADX 22, RVol 0.4) |
| 8 | **PLTR** | 167.26 | - | **-** | 20 | - | POS +$53.6M | - | 165 | 170 | -$204k | +$40k bull / -$26k bear | out (clean 28, ADX 45, RVol 0.3) |
| 9 | **SHOP** | 146.68 | - | **-** | 20 | - | POS +$841k | 144.82 | 150 | 140 | +$41k | - | out (clean 32, ADX 45, RVol 0.4) |
| 10 | **AVGO** | 327.25 | - | **-** | 19 | - | NEG -$16.2M | 342.44 | 340 | 320 | -$8.9M | +$328k bull / +$0 bear | out (clean 32, ADX 19, RVol 0.8) |
| 11 | **SPY** | 747.61 | - | **-** | 18 | - | NEG -$7.3B | 760.47 | 750 | 730 | +$38.7M | +$3.0M bull / +$0 bear | out (clean 32, ADX 33, RVol 0.5) |
| 12 | **TSLA** | 376.43 | - | **-** | 16 | - | POS +$195.4M | - | 400 | 380 | -$6.7M | +$693k bull / +$0 bear | out (clean 34, ADX 25, RVol 0.2) |
| 13 | **CRM** | 212.66 | - | **-** | 16 | - | NEG -$11.0M | - | 195 | 220 | -$99k | - | out (clean 30, ADX 37, RVol 0.1) |
| 14 | **QQQ** | 673.29 | - | **-** | 15 | - | NEG -$1.9B | 692.46 | 680 | 680 | +$627k | +$981k bull / -$514k bear | out (clean 31, ADX 24, RVol 0.3) |
| 15 | **SMH** | 481.55 | - | **-** | 15 | - | NEG -$224.9M | - | 500 | 475 | -$380k | +$250k bull / +$0 bear | out (clean 29, ADX 20, RVol 0.4) |
| 16 | **MU** | 714.96 | - | **-** | 15 | - | NEG -$28.5M | - | 750 | 750 | -$2.5M | +$348k bull / -$1.3M bear | out (clean 30, ADX 23, RVol 0.6) |
| 17 | **ARM** | 179.81 | - | **-** | 15 | - | NEG -$5.0M | - | 185 | 190 | -$246k | - | out (clean 28, ADX 28, RVol 0.5) |
| 18 | **META** | 643.50 | - | **-** | 14 | - | POS +$255.7M | 606.77 | 650 | 650 | -$168k | +$70k bull / +$0 bear | out (clean 32, ADX 18, RVol 0.6) |
| 19 | **HOOD** | 81.18 | - | **-** | 13 | - | POS +$3.1M | 79.09 | 85 | 80 | +$482k | - | out (clean 30, ADX 35, RVol 0.6) |
| 20 | **COIN** | 131.19 | - | **-** | 9 | - | POS +$3.7M | 128.76 | 137 | 135 | +$87k | - | out (clean 30, ADX 36, RVol 0.6) |
| 21 | **UBER** | 69.44 | - | **-** | 9 | - | POS +$5.7M | 68.42 | 70 | 70 | -$1k | - | out (clean 33, ADX 45, RVol 0.6) |
| 22 | **MSFT** | 542.49 | - | **-** | 8 | - | POS +$676.5M | - | 550 | 535 | -$288k | - | out (clean 32, ADX 33, RVol 0.6) |
| 23 | **NFLX** | 62.76 | - | **-** | 8 | - | NEG -$23.5M | 65.36 | 65 | 60 | -$98k | - | out (clean 30, ADX 32, RVol 0.7) |
| 24 | **MSTR** | 121.33 | - | **-** | 8 | - | NEG -$6.6M | 124.02 | 133 | 110 | -$748k | - | out (clean 29, ADX 30, RVol 0.6) |
| 25 | **DELL** | 333.04 | - | **-** | 7 | - | NEG -$10.8M | - | 350 | 340 | +$278k | - | out (clean 33, ADX 28, RVol 0.5) |
| 26 | **SMCI** | 28.09 | - | **-** | 7 | - | POS +$3.4M | - | 30 | 30 | -$73k | - | out (clean 29, ADX 22, RVol 0.5) |
| 27 | **ORCL** | 119.00 | - | **-** | 6 | - | NEG -$23.2M | - | 130 | 120 | -$75k | - | out (clean 28, ADX 26, RVol 0.3) |

## Big prints this scan (43)
- **SPY** PUT 760 2026-11-13 (3DTE): 400 @ 12.95 = **+$518k** MID | vol 38,315 / OI 5,844
- **SPY** PUT 760 2026-11-13 (3DTE): 400 @ 12.95 = **+$518k** MID | vol 38,315 / OI 5,844
- **SPY** PUT 760 2026-11-13 (3DTE): 399 @ 12.95 = **+$517k** MID | vol 38,315 / OI 5,844
- **SPY** PUT 760 2026-11-13 (3DTE): 390 @ 12.95 = **+$505k** MID | vol 38,315 / OI 5,844
- **NVDA** PUT 162.5 2026-11-13 (3DTE): 2,463 @ 1.92 = **+$473k** SELL | vol 21,292 / OI 1,181
- **SPY** PUT 760 2026-11-13 (3DTE): 360 @ 12.95 = **+$466k** MID | vol 38,315 / OI 5,844
- **AVGO** PUT 335 2026-11-13 (3DTE): 300 @ 10.92 = **+$328k** SELL | vol 595 / OI 1,840
- **SPY** CALL 749 2026-11-13 (3DTE): 483 @ 4.99 = **+$241k** BUY | vol 4,565 / OI 3,471
- **QQQ** CALL 673 2026-11-10 (0DTE): 450 @ 2.76 = **+$124k** BUY | vol 39,418 / OI 434
- **QQQ** PUT 673 2026-11-10 (0DTE): 668 @ 1.59 = **+$106k** SELL | vol 99,343 / OI 98
- **NVDA** PUT 170 2026-11-11 (1DTE): 300 @ 3.25 = **+$98k** SELL | vol 113,168 / OI 4,288
- **MU** PUT 715 2026-11-11 (1DTE): 51 @ 15.20 = **+$78k** BUY | vol 5,020 / OI 81
- **AMD** CALL 525 2026-11-11 (1DTE): 40 @ 14.15 = **+$57k** BUY | vol 7,234 / OI 146
- **NVDA** PUT 162.5 2026-11-16 (6DTE): 200 @ 2.62 = **+$52k** SELL | vol 1,121 / OI 73
- **AMZN** CALL 270 2026-11-11 (1DTE): 200 @ 2.52 = **+$50k** BUY | vol 15,154 / OI 1,320

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 742 2026-11-12 (2DTE): 551 traded vs OI 188
- **SPY** CALL 768 2026-11-10 (0DTE): 3,060 traded vs OI 3,057
- **SPY** PUT 747 2026-11-16 (6DTE): 507 traded vs OI 158
- **SPY** PUT 748 2026-11-18 (8DTE): 569 traded vs OI 72
- **SPY** PUT 745 2026-11-18 (8DTE): 548 traded vs OI 208
- **SPY** CALL 760 2026-11-23 (13DTE): 525 traded vs OI 0
- **QQQ** PUT 677 2026-11-12 (2DTE): 534 traded vs OI 176
- **QQQ** PUT 678 2026-11-12 (2DTE): 691 traded vs OI 49
- **QQQ** PUT 682 2026-11-12 (2DTE): 543 traded vs OI 86
- **QQQ** CALL 674 2026-11-12 (2DTE): 585 traded vs OI 212
- **IWM** CALL 278 2026-11-11 (1DTE): 535 traded vs OI 329
- **AAPL** PUT 345 2026-11-16 (6DTE): 504 traded vs OI 225
- **AMD** PUT 477.5 2026-11-11 (1DTE): 500 traded vs OI 18
- **AMD** CALL 532.5 2026-11-13 (3DTE): 521 traded vs OI 231
- **AMD** CALL 545 2026-11-13 (3DTE): 502 traded vs OI 395

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
