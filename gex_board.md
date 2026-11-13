# GEX + FLOW SCAN - Fri Nov 13, 11:20 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (11)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:15 | **ARM** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/13 180P | 0.79 | 0.57 | +0% (2m) | **-28%** | +122% | 180 |
| 11:14 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/13 667P | 0.70 | 0.80 | +46% (2m) | **+14%** | +21% | 672.05 |
| 10:36 | **SPY** | **PUTS** | 1m FAILED POP (R3 R4) | 11/13 743P | 0.61 | 0.42 | +13% (1m) | **-31%** | +46% | 747.53 |
| 10:17 | **QQQ** | **CALLS** | 1m WHIPSAW (R1 R2) | 11/13 683C | 0.75 | 0.18 | -1% (0m) | **-76%** (done) | +60% | 678.58 |
| 10:15 | **ARM** | **PUTS** | FLIP CROSS down into negative gamma | 11/13 182.5P | 0.74 | 1.47 | +169% (50m) | **+99%** (done) | +96% | 183.6 hit |
| 10:15 | **ORCL** | **CALLS** | FLIP CROSS up into positive gamma | 11/13 124C | 0.65 | 0.35 | +89% (28m) | **-46%** (done) | +66% | 123.68 hit |
| 10:10 | **ORCL** | **PUTS** | FLIP CROSS down into negative gamma | 11/13 120P | 0.46 | 0.15 | +7% (5m) | **-67%** (done) | +63% | 121.25 |
| 10:05 | **GOOGL** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/13 297.5P | 0.74 | 3.42 | +396% (33m) | **+362%** (done) | +288% | 295 hit |
| 09:55 | **BABA** | **PUTS** | FLOW SURGE | 11/13 94P | 0.51 | 0.43 | +8% (43m) | **-16%** (done) | +49% | 93.36 |
| 09:45 | **UBER** | **CALLS** | TREND + FLOW | 11/13 70C | 0.59 | 0.06 | +0% (1m) | **-90%** (done) | +32% | 70.7 |
| 09:45 | **ORCL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/13 127C | 0.46 | 0.22 | +22% (2m) | **-52%** (done) | +48% | 126.38 |

## 1m RULES on SPY / QQQ - loose (4 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 11:20:08 ET, last candle SPY 11:19, QQQ 11:19 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 11:13 | QQQ | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | **FIRE** QQQ261113P00667000 |
| 11:02 | QQQ | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |
| 10:35 | SPY | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | **FIRE** SPY261113P00743000 |
| 10:16 | QQQ | 1m WHIPSAW | R1 R2 | CALLS | TURNING your way | **FIRE** QQQ261113C00683000 |

## Flow surges NOT fired - price disagreed (40 today, last 5)
- 11:20 HOOD CALLS: price -0.21 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 11:15 HOOD CALLS: price -0.56 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 11:15 COIN CALLS: price -1.07 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 11:10 COIN CALLS: under EMA 20 - flow says one way, price says the other
- 11:05 COIN CALLS: price -0.05 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **ARM** | 184.56 | RUN: clean trend + negative gamma + flow agrees | **PUTS** | 50 | none: 30 puts 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (27 contracts' greeks worked out here) | NEG -$2.7M | 189.06 | 185 | 190 | -$201k | - | SHORT (clean 33, ADX 61, RVol 1.1) |
| 2 | **AVGO** | 339.42 | PINNED between the walls (positive gamma) - chop | **-** | 48 | - | POS +$56.6M | - | 340 | 340 | +$23.1M | +$378k bull / +$0 bear | SHORT (clean 36, ADX 52, RVol 0.5) |
| 3 | **DELL** | 334.61 | FLOW SURGE | **CALLS** | 47 | none: 54 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (53 contracts' greeks worked out here) | NEG -$6.7M | - | 350 | 340 | +$8.4M | +$35k bull / +$0 bear | out (clean 38, ADX 50, RVol 1.1) |
| 4 | **HOOD** | 76.87 | FLOW SURGE | **CALLS** | 47 | 11/13 77C @ 0.60 (delta 0.47) = est +109% at 78.18 | NEG -$13.4M | 79.68 | 77 | 80 | +$2.9M | +$29k bull / +$0 bear | out (clean 36, ADX 60, RVol 1.4) |
| 5 | **GOOGL** | 294.22 | FLOW SURGE | **CALLS** | 42 | none: 94 calls 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (42 contracts' greeks worked out here) | POS +$166.3M | 289.7 | 300 | 290 | +$19.9M | +$332k bull / -$56k bear | out (clean 32, ADX 32, RVol 1.1) |
| 6 | **AMZN** | 264.89 | PINNED between the walls (positive gamma) - chop | **-** | 40 | - | POS +$408.5M | 251.16 | 265 | 265 | +$8.1M | +$156k bull / -$25k bear | out (clean 30, ADX 34, RVol 0.6) |
| 7 | **META** | 631.11 | FLIP CROSS down into negative gamma | **PUTS** | 32 | none: 185 puts 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (86 contracts' greeks worked out here) | NEG -$5.5M | 631.33 | 630 | 625 | +$7.2M | +$0 bull / -$1.3M bear | out (clean 29, ADX 27, RVol 0.8) |
| 8 | **SMH** | 476.19 | - | **-** | 30 | - | NEG -$342.9M | - | 500 | 475 | +$12.7M | +$934k bull / +$0 bear | out (clean 31, ADX 57, RVol 1.6) |
| 9 | **QQQ** | 672.79 | - | **-** | 28 | - | NEG -$3.1B | 689.35 | 680 | 680 | +$299.5M | +$2.1M bull / +$0 bear | out (clean 32, ADX 57, RVol 0.5) |
| 10 | **IWM** | 275.80 | - | **-** | 28 | - | NEG -$2.7B | 282.51 | 285 | 275 | +$20.3M | +$0 bull / -$69k bear | out (clean 36, ADX 41, RVol 0.8) |
| 11 | **AMD** | 525.59 | - | **-** | 27 | - | POS +$37.6M | - | 550 | 530 | +$75.2M | +$2.5M bull / +$0 bear | out (clean 35, ADX 51, RVol 0.7) |
| 12 | **NVDA** | 159.15 | - | **-** | 26 | - | NEG -$286.2M | - | 175 | 160 | +$113.4M | +$4.2M bull / +$0 bear | out (clean 31, ADX 23, RVol 0.9) |
| 13 | **COIN** | 126.78 | - | **-** | 24 | - | NEG -$19.2M | 133.34 | 137 | 130 | +$3.5M | - | out (clean 31, ADX 42, RVol 1.1) |
| 14 | **MU** | 754.84 | - | **-** | 24 | - | NEG -$34.8M | 773.44 | 760 | 750 | +$73.4M | +$3.4M bull / -$38k bear | out (clean 31, ADX 39, RVol 0.6) |
| 15 | **MSTR** | 109.28 | - | **-** | 24 | - | NEG -$38.8M | - | 110 | 110 | +$5.9M | +$199k bull / +$0 bear | out (clean 31, ADX 34, RVol 0.5) |
| 16 | **SPY** | 749.33 | - | **-** | 23 | - | NEG -$8.7B | 759.58 | 750 | 750 | +$237.7M | +$2.4M bull / +$0 bear | out (clean 33, ADX 33, RVol 0.6) |
| 17 | **TSLA** | 387.65 | - | **-** | 21 | - | POS +$300.3M | - | 400 | 380 | +$53.0M | +$3.0M bull / -$2.5M bear | out (clean 29, ADX 18, RVol 0.6) |
| 18 | **AAPL** | 357.64 | - | **-** | 21 | - | POS +$1.2B | 347.17 | 360 | 360 | +$12.4M | +$723k bull / +$0 bear | out (clean 30, ADX 23, RVol 0.8) |
| 19 | **SHOP** | 145.14 | - | **-** | 20 | - | POS +$122k | 145.09 | 150 | 140 | -$78k | +$85k bull / +$0 bear | out (clean 32, ADX 22, RVol 0.7) |
| 20 | **PLTR** | 166.45 | - | **-** | 19 | - | POS +$80.1M | 159.6 | 165 | 165 | +$343k | +$145k bull / +$0 bear | out (clean 29, ADX 40, RVol 0.5) |
| 21 | **SMCI** | 25.98 | - | **-** | 18 | - | NEG -$2.7M | - | 27 | 25 | +$404k | - | out (clean 34, ADX 29, RVol 0.7) |
| 22 | **UBER** | 69.31 | - | **-** | 17 | - | POS +$10.8M | 68.86 | 70 | 70 | +$282k | - | out (clean 33, ADX 16, RVol 0.6) |
| 23 | **MSFT** | 521.97 | - | **-** | 16 | - | POS +$32.7M | 521.16 | 535 | 520 | -$322k | +$401k bull / +$0 bear | out (clean 32, ADX 24, RVol 1.0) |
| 24 | **CRM** | 215.92 | - | **-** | 16 | - | NEG -$8.2M | 220.26 | 220 | 220 | +$148k | - | out (clean 28, ADX 19, RVol 0.5) |
| 25 | **NFLX** | 62.34 | - | **-** | 11 | - | NEG -$33.0M | 63.25 | 65 | 62 | +$434k | - | out (clean 32, ADX 33, RVol 0.9) |
| 26 | **ORCL** | 122.41 | - | **-** | 10 | - | POS +$3.6M | 121.62 | 130 | 125 | -$644k | - | out (clean 31, ADX 37, RVol 0.9) |
| 27 | **BABA** | 94.05 | - | **-** | 5 | - | NEG -$18.6M | - | 100 | 95 | -$22k | - | out (clean 28, ADX 23, RVol 0.3) |

## Big prints this scan (94)
- **TSLA** CALL 397.5 2026-11-20 (7DTE): 2,238 @ 7.50 = **+$1.7M** BUY | vol 4,939 / OI 0
- **QQQ** PUT 675 2026-11-19 (6DTE): 373 @ 10.62 = **+$396k** SELL | vol 2,332 / OI 161
- **SPY** PUT 750 2026-11-13 (0DTE): 1,773 @ 2.20 = **+$390k** SELL | vol 243,844 / OI 11,683
- **SPY** PUT 750 2026-11-13 (0DTE): 1,773 @ 2.20 = **+$390k** SELL | vol 243,844 / OI 11,683
- **SPY** CALL 755 2026-11-20 (7DTE): 500 @ 4.91 = **+$246k** BUY | vol 2,571 / OI 15,917
- **SPY** CALL 751 2026-11-13 (0DTE): 933 @ 1.70 = **+$159k** BUY | vol 84,335 / OI 2,050
- **SPY** PUT 750 2026-11-20 (7DTE): 219 @ 6.97 = **+$153k** SELL | vol 12,200 / OI 55,813
- **QQQ** CALL 705 2026-11-20 (7DTE): 1,000 @ 1.45 = **+$145k** BUY | vol 2,371 / OI 23,908
- **SPY** PUT 752 2026-11-13 (0DTE): 400 @ 3.26 = **+$130k** SELL | vol 129,370 / OI 4,070
- **SPY** PUT 751 2026-11-13 (0DTE): 478 @ 2.67 = **+$128k** SELL | vol 122,842 / OI 4,041
- **AMD** CALL 500 2026-11-20 (7DTE): 29 @ 42.00 = **+$122k** BUY | vol 779 / OI 0
- **SMH** CALL 480 2026-11-20 (7DTE): 80 @ 14.15 = **+$113k** MID | vol 2,322 / OI 3,062
- **SMH** CALL 480 2026-11-20 (7DTE): 80 @ 14.15 = **+$113k** MID | vol 2,322 / OI 3,062
- **SPY** PUT 751 2026-11-13 (0DTE): 400 @ 2.68 = **+$107k** SELL | vol 122,842 / OI 4,041
- **NVDA** PUT 165 2026-11-20 (7DTE): 91 @ 11.45 = **+$104k** MID | vol 4,373 / OI 20,598

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 706 2026-11-16 (3DTE): 501 traded vs OI 321
- **SPY** PUT 685 2026-11-16 (3DTE): 716 traded vs OI 566
- **SPY** PUT 700 2026-11-16 (3DTE): 1,007 traded vs OI 981
- **SPY** CALL 788 2026-11-18 (5DTE): 612 traded vs OI 102
- **SPY** PUT 704 2026-11-16 (3DTE): 732 traded vs OI 356
- **SPY** CALL 759 2026-11-27 (14DTE): 740 traded vs OI 647
- **SPY** PUT 749 2026-12-11 (28DTE): 784 traded vs OI 478
- **SPY** CALL 755 2026-11-27 (14DTE): 832 traded vs OI 807
- **QQQ** PUT 675 2026-11-18 (5DTE): 939 traded vs OI 373
- **QQQ** PUT 674 2026-11-17 (4DTE): 507 traded vs OI 225
- **QQQ** PUT 639 2026-11-16 (3DTE): 505 traded vs OI 84
- **QQQ** CALL 705 2026-11-17 (4DTE): 888 traded vs OI 880
- **QQQ** CALL 674 2026-11-20 (7DTE): 676 traded vs OI 472
- **IWM** PUT 264 2026-11-19 (6DTE): 1,022 traded vs OI 32
- **SMH** PUT 465 2026-11-13 (0DTE): 1,122 traded vs OI 1,099

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
