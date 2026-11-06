# GEX + FLOW SCAN - Fri Nov 06, 01:20 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (4)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 12:40 | **SPY** | **CALLS** | 1m WHIPSAW (R1) | 11/06 742C | 0.42 | 0.26 | +14% (6m) | **-38%** | +42% | 739.03 |
| 10:30 | **NVDA** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/06 192.5C | 0.73 | 0.28 | +12% (20m) | **-62%** (done) | +199% | 193.9 |
| 10:00 | **NVDA** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/06 197.5C | 0.67 | 0.03 | -6% (1m) | **-96%** (done) | +24% | 195 |
| 09:50 | **NFLX** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/06 64C | 0.40 | 0.36 | +32% (4m) | **-10%** (done) | +164% | 65 |

## 1m RULES on SPY / QQQ - loose (11 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 13:20:08 ET, last candle SPY 13:19, QQQ 13:19 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 13:17 | SPY | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |
| 13:16 | QQQ | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |
| 13:11 | QQQ | 1m FAILED POP | R3 R4 | PUTS | TURNING your way | no contract: 39 puts 0-1DTE > 4 priced 0.40-0.80 > 2 delta 0.15+ > 2 spread ok > 2 liquid  |
| 13:11 | SPY | 1m FAILED POP | R3 R4 | PUTS | TURNING your way | no contract: 44 puts 0-1DTE > 4 priced 0.40-0.80 > 3 delta 0.15+ > 3 spread ok > 3 liquid  |
| 13:00 | QQQ | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | no contract: 40 puts 0-1DTE > 4 priced 0.40-0.80 > 2 delta 0.15+ > 2 spread ok > 2 liquid  |
| 13:00 | SPY | 1m FAILED POP | R3 | PUTS | TURNING away | no contract: 44 puts 0-1DTE > 4 priced 0.40-0.80 > 2 delta 0.15+ > 2 spread ok > 2 liquid  |
| 12:39 | SPY | 1m WHIPSAW | R1 | CALLS | AGAINST you | **FIRE** SPY261106C00742000 |
| 12:38 | QQQ | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |
| 12:38 | SPY | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |
| 12:37 | QQQ | 1m WHIPSAW | R1 R2 | PUTS | WITH you | no contract: 39 puts 0-1DTE > 5 priced 0.40-0.80 > 1 delta 0.15+ > 1 spread ok > 1 liquid  |

## Flow surges NOT fired - price disagreed (6 today, last 5)
- 09:55 SMCI PUTS: price +0.09 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 HOOD PUTS: price +3.27 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 MSTR PUTS: price +3.75 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 SMCI PUTS: price +0.89 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 PLTR PUTS: price +5.57 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **GOOGL** | 285.40 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 34 | none: 92 puts 0-7DTE > 8 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (36 contracts' greeks worked out here) | POS +$50.2M | 282.93 | 285 | 290 | +$2.9M | +$845k bull / -$40k bear | out (clean 33, ADX 18, RVol 0.5) |
| 2 | **ORCL** | 113.86 | - | **-** | 23 | - | NEG -$76.6M | - | 125 | 115 | -$4.5M | +$41k bull / -$404k bear | out (clean 30, ADX 25, RVol 1.0) |
| 3 | **MSTR** | 126.46 | - | **-** | 19 | - | NEG -$12.8M | 127.39 | 135 | 125 | -$6.8M | +$0 bull / -$631k bear | out (clean 31, ADX 20, RVol 0.3) |
| 4 | **SMH** | 459.22 | - | **-** | 18 | - | NEG -$479.0M | - | 505 | 465 | +$7.4M | +$0 bull / -$1.3M bear | out (clean 33, ADX 19, RVol 0.4) |
| 5 | **NVDA** | 185.99 | - | **-** | 18 | - | NEG -$374.8M | - | 200 | 190 | +$31.4M | +$729k bull / -$1.1M bear | out (clean 33, ADX 20, RVol 0.7) |
| 6 | **TSLA** | 358.55 | - | **-** | 18 | - | NEG -$308.9M | - | 370 | 360 | -$57.9M | +$337k bull / -$784k bear | out (clean 35, ADX 19, RVol 0.5) |
| 7 | **MU** | 681.85 | - | **-** | 18 | - | NEG -$155.1M | - | 700 | 700 | +$78.4M | +$3.5M bull / -$1.4M bear | out (clean 32, ADX 16, RVol 0.7) |
| 8 | **AAPL** | 343.79 | - | **-** | 17 | - | NEG -$46.5M | 344.27 | 345 | 345 | -$16.7M | +$81k bull / -$41k bear | out (clean 29, ADX 10, RVol 0.2) |
| 9 | **META** | 617.49 | - | **-** | 17 | - | NEG -$127.1M | 622.49 | 620 | 610 | -$6.9M | +$0 bull / -$28k bear | out (clean 33, ADX 25, RVol 0.3) |
| 10 | **AMZN** | 261.81 | - | **-** | 17 | - | POS +$340.2M | - | 260 | 260 | -$1.8M | +$0 bull / -$1.2M bear | out (clean 35, ADX 28, RVol 0.4) |
| 11 | **MSFT** | 532.91 | - | **-** | 17 | - | POS +$663.9M | 512.28 | 535 | 535 | +$4.4M | +$84k bull / -$135k bear | out (clean 34, ADX 15, RVol 0.4) |
| 12 | **NFLX** | 63.77 | - | **-** | 17 | - | POS +$14.5M | 63.14 | 64 | 64 | -$328k | +$25k bull / +$0 bear | out (clean 32, ADX 20, RVol 0.5) |
| 13 | **SPY** | 736.75 | - | **-** | 16 | - | NEG -$14.5B | 768.31 | 760 | 740 | -$29.7M | +$105k bull / -$3.4M bear | out (clean 34, ADX 24, RVol 0.4) |
| 14 | **QQQ** | 656.13 | - | **-** | 16 | - | NEG -$5.2B | - | 700 | 680 | +$57.1M | +$872k bull / -$3.6M bear | out (clean 34, ADX 22, RVol 0.6) |
| 15 | **IWM** | 273.33 | - | **-** | 16 | - | NEG -$3.1B | 285.21 | 285 | 270 | -$5.5M | +$0 bull / -$379k bear | out (clean 34, ADX 15, RVol 0.9) |
| 16 | **AMD** | 438.59 | - | **-** | 16 | - | NEG -$175.7M | - | 430 | 440 | +$12.0M | +$27k bull / -$1.2M bear | out (clean 31, ADX 19, RVol 0.6) |
| 17 | **AVGO** | 291.12 | - | **-** | 16 | - | NEG -$130.6M | - | 320 | 300 | +$2.6M | +$0 bull / -$28k bear | out (clean 31, ADX 22, RVol 0.4) |
| 18 | **HOOD** | 79.22 | - | **-** | 16 | - | NEG -$23.4M | 81.93 | 85 | 80 | +$2.1M | +$0 bull / -$33k bear | out (clean 30, ADX 21, RVol 0.3) |
| 19 | **SHOP** | 149.10 | - | **-** | 15 | - | NEG -$2.8M | 150.87 | 150 | 150 | -$1.1M | - | out (clean 37, ADX 20, RVol 0.5) |
| 20 | **DELL** | 325.80 | - | **-** | 13 | - | NEG -$21.2M | - | 330 | 325 | +$5.9M | - | out (clean 31, ADX 21, RVol 0.9) |
| 21 | **COIN** | 132.54 | - | **-** | 11 | - | NEG -$22.3M | 136.33 | 142 | 130 | -$3.1M | - | out (clean 32, ADX 24, RVol 0.3) |
| 22 | **UBER** | 69.07 | - | **-** | 11 | - | POS +$8.3M | 68.55 | 70 | 70 | +$271k | - | out (clean 30, ADX 29, RVol 0.3) |
| 23 | **ARM** | 171.50 | - | **-** | 7 | - | NEG -$27.4M | - | 180 | 170 | -$575k | - | out (clean 26, ADX 13, RVol 0.4) |
| 24 | **CRM** | 215.12 | - | **-** | 7 | - | NEG -$27.1M | - | 230 | 215 | -$223k | - | out (clean 34, ADX 22, RVol 0.8) |
| 25 | **BABA** | 109.22 | - | **-** | 7 | - | POS +$26.2M | 103.65 | 110 | 110 | -$467k | - | out (clean 34, ADX 14, RVol 0.4) |
| 26 | **PLTR** | 160.07 | - | **-** | 6 | - | NEG -$73.7M | - | 165 | 160 | +$3.6M | - | out (clean 28, ADX 14, RVol 0.3) |
| 27 | **SMCI** | 28.10 | - | **-** | 6 | - | NEG -$5.4M | - | 30 | 28 | -$354k | - | out (clean 34, ADX 20, RVol 0.4) |

## Big prints this scan (53)
- **MU** PUT 685 2026-11-13 (7DTE): 400 @ 38.45 = **+$1.5M** SELL | vol 762 / OI 0
- **MU** CALL 685 2026-11-13 (7DTE): 400 @ 36.60 = **+$1.5M** MID | vol 522 / OI 0
- **MSTR** CALL 131 2026-11-13 (7DTE): 1,000 @ 4.19 = **+$419k** MID | vol 1,481 / OI 188
- **QQQ** PUT 660 2026-11-09 (3DTE): 200 @ 9.50 = **+$190k** BUY | vol 20,685 / OI 1,084
- **QQQ** PUT 660 2026-11-09 (3DTE): 200 @ 9.30 = **+$186k** BUY | vol 20,685 / OI 1,084
- **QQQ** PUT 660 2026-11-09 (3DTE): 194 @ 9.40 = **+$182k** BUY | vol 20,685 / OI 1,084
- **QQQ** PUT 687 2026-11-06 (0DTE): 49 @ 31.24 = **+$153k** SELL | vol 283 / OI 1,140
- **MU** CALL 670 2026-11-06 (0DTE): 100 @ 14.80 = **+$148k** BUY | vol 1,479 / OI 0
- **AMD** PUT 435 2026-11-06 (0DTE): 462 @ 3.00 = **+$139k** BUY | vol 13,716 / OI 973
- **NVDA** CALL 185 2026-11-11 (5DTE): 220 @ 6.25 = **+$138k** BUY | vol 1,488 / OI 10
- **SPY** PUT 736 2026-11-13 (7DTE): 150 @ 9.15 = **+$137k** BUY | vol 2,363 / OI 1,194
- **MU** PUT 670 2026-11-06 (0DTE): 400 @ 3.40 = **+$136k** BUY | vol 42,977 / OI 734
- **QQQ** PUT 655 2026-11-09 (3DTE): 195 @ 6.95 = **+$136k** BUY | vol 16,281 / OI 1,021
- **QQQ** PUT 655 2026-11-09 (3DTE): 171 @ 6.95 = **+$119k** BUY | vol 16,281 / OI 1,021
- **QQQ** PUT 655 2026-11-09 (3DTE): 165 @ 6.93 = **+$114k** BUY | vol 16,281 / OI 1,021

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 730 2026-11-11 (5DTE): 1,751 traded vs OI 1,748
- **SPY** CALL 744 2026-11-11 (5DTE): 525 traded vs OI 4
- **QQQ** PUT 631 2026-11-10 (4DTE): 803 traded vs OI 0
- **QQQ** CALL 692 2026-11-13 (7DTE): 500 traded vs OI 316
- **IWM** CALL 278 2026-11-13 (7DTE): 890 traded vs OI 802
- **IWM** CALL 277 2026-11-12 (6DTE): 557 traded vs OI 43
- **NVDA** PUT 195 2026-11-06 (0DTE): 15,043 traded vs OI 14,974
- **NVDA** PUT 192.5 2026-11-13 (7DTE): 2,625 traded vs OI 2,606
- **TSLA** PUT 365 2026-11-09 (3DTE): 890 traded vs OI 882
- **AAPL** PUT 345 2026-11-11 (5DTE): 589 traded vs OI 439
- **AMD** PUT 410 2026-11-11 (5DTE): 513 traded vs OI 17
- **AMZN** CALL 280 2026-11-09 (3DTE): 518 traded vs OI 511
- **MSFT** CALL 555 2026-11-13 (7DTE): 1,760 traded vs OI 1,364
- **NFLX** CALL 64 2026-11-13 (7DTE): 1,675 traded vs OI 1,672
- **AVGO** PUT 285 2026-11-09 (3DTE): 506 traded vs OI 96

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
