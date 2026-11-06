# GEX + FLOW SCAN - Fri Nov 06, 01:00 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (4)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 12:40 | **SPY** | **CALLS** | 1m WHIPSAW (R1) | 11/06 742C | 0.42 | 0.34 | +14% (6m) | **-19%** | +42% | 739.03 |
| 10:30 | **NVDA** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/06 192.5C | 0.73 | 0.28 | +12% (20m) | **-62%** (done) | +199% | 193.9 |
| 10:00 | **NVDA** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/06 197.5C | 0.67 | 0.03 | -6% (1m) | **-96%** (done) | +24% | 195 |
| 09:50 | **NFLX** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/06 64C | 0.40 | 0.36 | +32% (4m) | **-10%** (done) | +164% | 65 |

## 1m RULES on SPY / QQQ - loose (5 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 13:00:08 ET, last candle SPY 12:59, QQQ 12:59 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 12:39 | SPY | 1m WHIPSAW | R1 | CALLS | AGAINST you | **FIRE** SPY261106C00742000 |
| 12:38 | QQQ | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |
| 12:38 | SPY | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |
| 12:37 | QQQ | 1m WHIPSAW | R1 R2 | PUTS | WITH you | no contract: 39 puts 0-1DTE > 5 priced 0.40-0.80 > 1 delta 0.15+ > 1 spread ok > 1 liquid  |
| 12:37 | SPY | 1m WHIPSAW | R1 R2 | PUTS | WITH you | no contract: 43 puts 0-1DTE > 3 priced 0.40-0.80 > 1 delta 0.15+ > 1 spread ok > 1 liquid  |

## Flow surges NOT fired - price disagreed (6 today, last 5)
- 09:55 SMCI PUTS: price +0.09 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 HOOD PUTS: price +3.27 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 MSTR PUTS: price +3.75 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 SMCI PUTS: price +0.89 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 PLTR PUTS: price +5.57 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **AAPL** | 344.19 | FLIP CROSS down into negative gamma | **PUTS** | 29 | 11/06 342.5P @ 0.57 (delta 0.29) = est +66% at 342.35 | NEG -$8.4M | 344.21 | 350 | 345 | -$16.9M | +$144k bull / -$643k bear | out (clean 29, ADX 9, RVol 0.3) |
| 2 | **ORCL** | 114.09 | - | **-** | 24 | - | NEG -$67.7M | - | 125 | 115 | -$3.3M | +$63k bull / -$1.4M bear | out (clean 30, ADX 22, RVol 1.8) |
| 3 | **GOOGL** | 285.57 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 23 | none: 92 puts 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (39 contracts' greeks worked out here) | POS +$39.6M | 284.43 | 285 | 290 | +$2.1M | - | out (clean 34, ADX 16, RVol 0.5) |
| 4 | **DELL** | 328.98 | - | **-** | 23 | - | NEG -$25.7M | - | 335 | 335 | +$5.8M | +$54k bull / +$0 bear | out (clean 32, ADX 17, RVol 0.9) |
| 5 | **SMH** | 459.80 | - | **-** | 21 | - | NEG -$493.8M | - | 505 | 465 | +$9.3M | +$494k bull / -$182k bear | out (clean 33, ADX 17, RVol 0.9) |
| 6 | **COIN** | 132.98 | - | **-** | 21 | - | NEG -$22.2M | 136.67 | 141 | 130 | -$2.9M | +$610k bull / +$0 bear | out (clean 32, ADX 21, RVol 0.5) |
| 7 | **MSTR** | 126.90 | - | **-** | 20 | - | NEG -$14.5M | 128 | 135 | 125 | -$7.8M | +$27k bull / +$0 bear | out (clean 31, ADX 18, RVol 0.5) |
| 8 | **TSLA** | 359.00 | - | **-** | 19 | - | NEG -$311.4M | - | 360 | 360 | -$55.0M | +$1.1M bull / -$192k bear | out (clean 35, ADX 24, RVol 0.5) |
| 9 | **NVDA** | 186.43 | - | **-** | 18 | - | NEG -$393.9M | - | 200 | 190 | +$32.9M | +$2.5M bull / -$1.8M bear | out (clean 33, ADX 18, RVol 0.9) |
| 10 | **MU** | 686.81 | - | **-** | 18 | - | NEG -$180.4M | - | 700 | 700 | +$80.2M | +$7.1M bull / -$458k bear | out (clean 32, ADX 14, RVol 0.9) |
| 11 | **UBER** | 69.22 | - | **-** | 18 | - | POS +$10.1M | 68.58 | 70 | 70 | +$157k | +$0 bull / -$39k bear | out (clean 30, ADX 22, RVol 0.3) |
| 12 | **QQQ** | 656.71 | - | **-** | 17 | - | NEG -$5.6B | - | 700 | 680 | +$70.1M | +$3.0M bull / -$136k bear | out (clean 35, ADX 20, RVol 0.9) |
| 13 | **IWM** | 273.27 | - | **-** | 17 | - | NEG -$3.3B | 286.16 | 285 | 270 | -$3.8M | +$64k bull / +$0 bear | out (clean 34, ADX 18, RVol 1.1) |
| 14 | **AMD** | 438.19 | - | **-** | 17 | - | NEG -$177.5M | - | 430 | 440 | +$18.1M | +$864k bull / -$47k bear | out (clean 32, ADX 19, RVol 0.6) |
| 15 | **META** | 617.83 | - | **-** | 17 | - | NEG -$124.3M | 622.67 | 620 | 610 | -$6.7M | +$240k bull / -$729k bear | out (clean 33, ADX 24, RVol 0.6) |
| 16 | **MSFT** | 533.65 | - | **-** | 17 | - | POS +$615.1M | 514.82 | 535 | 535 | +$4.9M | +$270k bull / -$96k bear | out (clean 34, ADX 13, RVol 0.5) |
| 17 | **PLTR** | 161.01 | - | **-** | 17 | - | NEG -$74.5M | - | 165 | 160 | +$3.5M | +$370k bull / +$0 bear | out (clean 28, ADX 16, RVol 0.4) |
| 18 | **HOOD** | 78.88 | - | **-** | 17 | - | NEG -$22.7M | - | 85 | 80 | +$2.4M | +$245k bull / +$0 bear | out (clean 30, ADX 22, RVol 0.6) |
| 19 | **CRM** | 214.63 | - | **-** | 17 | - | NEG -$22.5M | - | 230 | 215 | -$195k | +$26k bull / +$0 bear | out (clean 35, ADX 22, RVol 0.8) |
| 20 | **BABA** | 109.12 | - | **-** | 17 | - | POS +$25.2M | 106.66 | 110 | 110 | -$452k | +$37k bull / +$0 bear | out (clean 34, ADX 16, RVol 0.6) |
| 21 | **AMZN** | 261.50 | - | **-** | 16 | - | POS +$326.4M | - | 260 | 260 | +$96k | +$132k bull / -$51k bear | out (clean 35, ADX 27, RVol 0.3) |
| 22 | **AVGO** | 292.98 | - | **-** | 16 | - | NEG -$132.8M | - | 320 | 300 | +$2.5M | +$1.3M bull / -$236k bear | out (clean 31, ADX 20, RVol 0.7) |
| 23 | **SHOP** | 149.59 | - | **-** | 16 | - | NEG -$3.7M | 151.46 | 150 | 150 | -$1.1M | - | out (clean 36, ADX 24, RVol 0.5) |
| 24 | **SPY** | 737.03 | - | **-** | 15 | - | NEG -$14.6B | 769.64 | 760 | 740 | +$9.9M | +$1.3M bull / -$770k bear | out (clean 34, ADX 20, RVol 0.8) |
| 25 | **ARM** | 171.53 | - | **-** | 8 | - | NEG -$25.5M | - | 180 | 170 | -$494k | - | out (clean 26, ADX 15, RVol 0.8) |
| 26 | **NFLX** | 63.67 | - | **-** | 6 | - | POS +$13.7M | 63.3 | 64 | 65 | -$242k | - | out (clean 32, ADX 18, RVol 0.7) |
| 27 | **SMCI** | 28.14 | - | **-** | 6 | - | NEG -$4.8M | - | 30 | 30 | -$308k | - | out (clean 34, ADX 20, RVol 0.4) |

## Big prints this scan (114)
- **NVDA** PUT 192.5 2026-11-09 (3DTE): 1,625 @ 7.30 = **+$1.2M** SELL | vol 15,931 / OI 850
- **QQQ** CALL 635 2026-11-09 (3DTE): 189 @ 23.10 = **+$437k** BUY | vol 527 / OI 0
- **QQQ** CALL 635 2026-11-09 (3DTE): 189 @ 23.10 = **+$437k** BUY | vol 527 / OI 0
- **MU** PUT 705 2026-11-06 (0DTE): 200 @ 21.00 = **+$420k** SELL | vol 7,046 / OI 0
- **NVDA** PUT 192.5 2026-11-09 (3DTE): 517 @ 7.67 = **+$397k** BUY | vol 15,931 / OI 850
- **NVDA** PUT 192.5 2026-11-09 (3DTE): 329 @ 7.67 = **+$252k** BUY | vol 15,931 / OI 850
- **NVDA** PUT 192.5 2026-11-09 (3DTE): 306 @ 7.67 = **+$235k** BUY | vol 15,931 / OI 850
- **SMH** PUT 460 2026-11-09 (3DTE): 250 @ 9.20 = **+$230k** SELL | vol 1,391 / OI 296
- **NVDA** PUT 192.5 2026-11-09 (3DTE): 299 @ 7.67 = **+$229k** BUY | vol 15,931 / OI 850
- **MU** PUT 705 2026-11-06 (0DTE): 105 @ 21.50 = **+$226k** SELL | vol 7,046 / OI 0
- **META** CALL 610 2026-11-13 (7DTE): 102 @ 20.80 = **+$212k** BUY | vol 525 / OI 118
- **NVDA** PUT 192.5 2026-11-09 (3DTE): 250 @ 7.67 = **+$192k** BUY | vol 15,931 / OI 850
- **MU** CALL 670 2026-11-06 (0DTE): 100 @ 17.50 = **+$175k** BUY | vol 1,056 / OI 0
- **QQQ** CALL 655 2026-11-06 (0DTE): 478 @ 3.60 = **+$172k** BUY | vol 14,129 / OI 1,184
- **MU** PUT 705 2026-11-06 (0DTE): 71 @ 21.50 = **+$153k** SELL | vol 7,046 / OI 0

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 745 2026-11-12 (6DTE): 504 traded vs OI 28
- **SPY** CALL 751 2026-11-10 (4DTE): 531 traded vs OI 77
- **SPY** CALL 758 2026-11-11 (5DTE): 563 traded vs OI 13
- **SPY** CALL 753 2026-11-10 (4DTE): 528 traded vs OI 87
- **SPY** CALL 780 2026-11-11 (5DTE): 1,716 traded vs OI 1,232
- **SPY** CALL 750 2026-11-16 (10DTE): 501 traded vs OI 199
- **SPY** PUT 732 2026-11-12 (6DTE): 500 traded vs OI 66
- **SPY** CALL 734 2026-11-13 (7DTE): 519 traded vs OI 15
- **SPY** CALL 750 2026-11-27 (21DTE): 509 traded vs OI 301
- **SPY** CALL 755 2026-12-04 (28DTE): 722 traded vs OI 451
- **SPY** CALL 745 2026-11-20 (14DTE): 3,446 traded vs OI 3,364
- **QQQ** PUT 600 2026-11-11 (5DTE): 508 traded vs OI 59
- **QQQ** CALL 635 2026-11-09 (3DTE): 527 traded vs OI 0
- **QQQ** PUT 602 2026-11-09 (3DTE): 500 traded vs OI 0
- **QQQ** CALL 688 2026-11-11 (5DTE): 521 traded vs OI 33

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
