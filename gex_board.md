# GEX + FLOW SCAN - Fri Nov 13, 03:05 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (13)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 12:45 | **HOOD** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/13 78C | 0.58 | 0.44 | +12% (3m) | **-24%** (done) | +75% | 79 |
| 11:30 | **GOOGL** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/13 292.5P | 0.56 | 0.18 | +23% (10m) | **-68%** (done) | +237% | 290.96 |
| 11:15 | **ARM** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/13 180P | 0.79 | 0.03 | +18% (40m) | **-96%** (done) | +122% | 180 |
| 11:14 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/13 667P | 0.70 | 0.17 | +59% (9m) | **-76%** (done) | +21% | 672.05 hit |
| 10:36 | **SPY** | **PUTS** | 1m FAILED POP (R3 R4) | 11/13 743P | 0.61 | 0.22 | +13% (1m) | **-64%** (done) | +46% | 747.53 |
| 10:17 | **QQQ** | **CALLS** | 1m WHIPSAW (R1 R2) | 11/13 683C | 0.75 | 0.18 | -1% (0m) | **-76%** (done) | +60% | 678.58 |
| 10:15 | **ARM** | **PUTS** | FLIP CROSS down into negative gamma | 11/13 182.5P | 0.74 | 1.47 | +169% (50m) | **+99%** (done) | +96% | 183.6 hit |
| 10:15 | **ORCL** | **CALLS** | FLIP CROSS up into positive gamma | 11/13 124C | 0.65 | 0.35 | +89% (28m) | **-46%** (done) | +66% | 123.68 hit |
| 10:10 | **ORCL** | **PUTS** | FLIP CROSS down into negative gamma | 11/13 120P | 0.46 | 0.15 | +7% (5m) | **-67%** (done) | +63% | 121.25 |
| 10:05 | **GOOGL** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/13 297.5P | 0.74 | 3.42 | +396% (33m) | **+362%** (done) | +288% | 295 hit |
| 09:55 | **BABA** | **PUTS** | FLOW SURGE | 11/13 94P | 0.51 | 0.43 | +8% (43m) | **-16%** (done) | +49% | 93.36 |
| 09:45 | **UBER** | **CALLS** | TREND + FLOW | 11/13 70C | 0.59 | 0.06 | +0% (1m) | **-90%** (done) | +32% | 70.7 |
| 09:45 | **ORCL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/13 127C | 0.46 | 0.22 | +22% (2m) | **-52%** (done) | +48% | 126.38 |

## 1m RULES on SPY / QQQ - loose (5 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 15:05:08 ET, last candle SPY 15:04, QQQ 15:04 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 13:26 | QQQ | 1m AGREE FLIP | FULL | CALLS | up | logged (agree flip) |
| 11:13 | QQQ | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | **FIRE** QQQ261113P00667000 |
| 11:02 | QQQ | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |
| 10:35 | SPY | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | **FIRE** SPY261113P00743000 |
| 10:16 | QQQ | 1m WHIPSAW | R1 R2 | CALLS | TURNING your way | **FIRE** QQQ261113C00683000 |

## Flow surges NOT fired - price disagreed (40 today, last 5)
- 12:25 ARM PUTS: over EMA 20 - flow says one way, price says the other
- 11:45 HOOD CALLS: price -0.30 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 11:40 HOOD CALLS: under EMA 20 - flow says one way, price says the other
- 11:35 HOOD CALLS: under EMA 20 - flow says one way, price says the other
- 11:25 HOOD CALLS: price -0.54 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **TSLA** | 391.73 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 33 | none: 124 puts 0-7DTE > 5 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only -41% at the target (needs +20%) (51 contracts' greeks worked out here) | POS +$468.1M | - | 392.5 | 390 | +$40.2M | +$387k bull / +$0 bear | out (clean 28, ADX 12, RVol 0.5) |
| 2 | **META** | 641.12 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 33 | none: 194 calls 0-7DTE > 8 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (81 contracts' greeks worked out here) | POS +$142.3M | 637.12 | 650 | 640 | -$1.3M | +$64k bull / -$32k bear | out (clean 30, ADX 25, RVol 0.5) |
| 3 | **MU** | 772.13 | FLIP CROSS up into positive gamma | **CALLS** | 29 | none: 160 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (73 contracts' greeks worked out here) | POS +$4.6M | 769.01 | 770 | 770 | +$63.0M | +$646k bull / -$3.0M bear | out (clean 30, ADX 21, RVol 0.3) |
| 4 | **GOOGL** | 294.97 | PINNED between the walls (positive gamma) - chop | **-** | 27 | - | POS +$138.9M | 293.22 | 295 | 295 | +$20.4M | - | out (clean 30, ADX 13, RVol 0.5) |
| 5 | **HOOD** | 78.33 | - | **-** | 21 | - | NEG -$11.7M | 79.5 | 78 | 79 | +$2.4M | +$25k bull / +$0 bear | out (clean 35, ADX 17, RVol 1.0) |
| 6 | **AVGO** | 345.52 | - | **-** | 20 | - | POS +$102.8M | - | 350 | 340 | +$18.3M | +$84k bull / -$1.3M bear | out (clean 36, ADX 14, RVol 0.3) |
| 7 | **AMZN** | 265.40 | PINNED between the walls (positive gamma) - chop | **-** | 19 | - | POS +$413.1M | 254.38 | 265 | 265 | +$8.7M | - | out (clean 29, ADX 13, RVol 0.2) |
| 8 | **COIN** | 128.58 | - | **-** | 19 | - | NEG -$19.0M | 132 | 140 | 130 | +$2.3M | +$82k bull / +$0 bear | out (clean 30, ADX 14, RVol 0.5) |
| 9 | **QQQ** | 679.38 | - | **-** | 18 | - | NEG -$2.7B | 683.79 | 680 | 680 | +$224.8M | +$715k bull / -$606k bear | out (clean 32, ADX 18, RVol 0.3) |
| 10 | **SMH** | 486.03 | - | **-** | 18 | - | NEG -$271.9M | - | 500 | 485 | +$6.6M | +$235k bull / -$85k bear | out (clean 31, ADX 23, RVol 0.2) |
| 11 | **NVDA** | 162.69 | - | **-** | 18 | - | NEG -$248.7M | - | 175 | 162.5 | +$75.3M | +$442k bull / -$3.2M bear | out (clean 31, ADX 19, RVol 0.4) |
| 12 | **AAPL** | 357.04 | - | **-** | 18 | - | POS +$1.0B | 349.87 | 360 | 355 | +$12.3M | +$297k bull / +$0 bear | out (clean 30, ADX 19, RVol 0.6) |
| 13 | **MSTR** | 112.41 | - | **-** | 18 | - | NEG -$43.3M | - | 120 | 110 | +$2.1M | +$1.4M bull / +$0 bear | out (clean 32, ADX 34, RVol 0.6) |
| 14 | **ORCL** | 125.35 | - | **-** | 18 | - | NEG -$20.2M | 125.97 | 125 | 125 | -$1.6M | +$0 bull / -$48k bear | out (clean 31, ADX 22, RVol 0.6) |
| 15 | **SPY** | 753.42 | - | **-** | 17 | - | NEG -$8.2B | 759.55 | 755 | 755 | +$213.7M | +$2.2M bull / -$451k bear | out (clean 33, ADX 18, RVol 0.5) |
| 16 | **AMD** | 532.72 | - | **-** | 17 | - | POS +$62.1M | - | 530 | 530 | +$45.6M | +$560k bull / -$1.5M bear | out (clean 35, ADX 22, RVol 0.3) |
| 17 | **SMCI** | 26.68 | - | **-** | 16 | - | NEG -$1.2M | 26.96 | 27 | 25 | -$1.8M | - | out (clean 34, ADX 30, RVol 0.5) |
| 18 | **ARM** | 190.16 | - | **-** | 13 | - | NEG -$2.7M | 190.93 | 190 | 190 | -$4.0M | - | out (clean 33, ADX 17, RVol 0.1) |
| 19 | **SHOP** | 147.59 | - | **-** | 13 | - | POS +$3.8M | 146.05 | 150 | 140 | +$33k | +$33k bull / +$0 bear | out (clean 30, ADX 8, RVol 0.6) |
| 20 | **BABA** | 93.91 | - | **-** | 13 | - | NEG -$19.7M | - | 100 | 95 | +$25k | +$30k bull / +$0 bear | out (clean 27, ADX 14, RVol 0.3) |
| 21 | **CRM** | 218.56 | - | **-** | 11 | - | NEG -$3.7M | 220.66 | 220 | 220 | +$131k | - | out (clean 28, ADX 24, RVol 1.1) |
| 22 | **UBER** | 69.52 | - | **-** | 10 | - | POS +$11.3M | 69.28 | 70 | 70 | +$284k | - | out (clean 32, ADX 15, RVol 0.2) |
| 23 | **IWM** | 277.39 | - | **-** | 9 | - | NEG -$2.5B | 282.38 | 285 | 275 | +$16.3M | - | out (clean 36, ADX 18, RVol 0.4) |
| 24 | **NFLX** | 62.30 | - | **-** | 7 | - | NEG -$47.3M | 63.39 | 65 | 62 | +$387k | - | out (clean 30, ADX 17, RVol 0.7) |
| 25 | **DELL** | 342.08 | - | **-** | 7 | - | NEG -$3.6M | 344.43 | 350 | 340 | +$4.3M | - | out (clean 38, ADX 15, RVol 0.7) |
| 26 | **MSFT** | 524.97 | - | **-** | 3 | - | POS +$166.7M | 522.67 | 535 | 520 | -$411k | - | out (clean 31, ADX 8, RVol 0.5) |
| 27 | **PLTR** | 169.25 | - | **-** | 3 | - | POS +$88.2M | 166.26 | 170 | 170 | +$198k | - | out (clean 29, ADX 15, RVol 0.3) |

## Big prints this scan (82)
- **AVGO** PUT 350 2026-11-20 (7DTE): 860 @ 14.00 = **+$1.2M** BUY | vol 1,617 / OI 11,920
- **NVDA** CALL 160 2026-11-16 (3DTE): 1,032 @ 4.20 = **+$433k** SELL | vol 79,727 / OI 919
- **NVDA** CALL 160 2026-11-16 (3DTE): 946 @ 4.20 = **+$397k** SELL | vol 79,727 / OI 919
- **NVDA** CALL 160 2026-11-16 (3DTE): 815 @ 4.38 = **+$357k** SELL | vol 79,727 / OI 919
- **MU** PUT 800 2026-11-13 (0DTE): 80 @ 32.50 = **+$260k** BUY | vol 2,030 / OI 2,029
- **NVDA** CALL 160 2026-11-16 (3DTE): 578 @ 4.25 = **+$246k** SELL | vol 79,727 / OI 919
- **NVDA** CALL 160 2026-11-16 (3DTE): 517 @ 4.38 = **+$226k** SELL | vol 79,727 / OI 919
- **NVDA** CALL 160 2026-11-16 (3DTE): 531 @ 4.25 = **+$226k** SELL | vol 79,727 / OI 919
- **AMD** CALL 520 2026-11-16 (3DTE): 100 @ 17.40 = **+$174k** SELL | vol 1,155 / OI 79
- **NVDA** PUT 160 2026-11-16 (3DTE): 697 @ 2.16 = **+$151k** BUY | vol 81,718 / OI 4,240
- **QQQ** PUT 678 2026-11-17 (4DTE): 200 @ 6.47 = **+$129k** BUY | vol 1,422 / OI 234
- **MU** CALL 760 2026-11-16 (3DTE): 65 @ 19.49 = **+$127k** SELL | vol 5,885 / OI 921
- **AMD** PUT 520 2026-11-20 (7DTE): 63 @ 18.55 = **+$117k** BUY | vol 2,216 / OI 1,791
- **MU** CALL 780 2026-11-16 (3DTE): 110 @ 10.15 = **+$112k** SELL | vol 6,088 / OI 479
- **AMD** CALL 550 2026-11-18 (5DTE): 100 @ 11.00 = **+$110k** SELL | vol 1,828 / OI 143

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 775 2026-11-18 (5DTE): 947 traded vs OI 887
- **SPY** CALL 774 2026-11-16 (3DTE): 1,397 traded vs OI 1,291
- **SPY** PUT 731 2026-11-17 (4DTE): 546 traded vs OI 509
- **SPY** CALL 752 2026-11-19 (6DTE): 515 traded vs OI 201
- **SPY** CALL 780 2026-11-17 (4DTE): 745 traded vs OI 699
- **SPY** CALL 815 2026-11-23 (10DTE): 800 traded vs OI 240
- **SPY** PUT 715 2026-11-23 (10DTE): 791 traded vs OI 428
- **SPY** CALL 820 2026-11-23 (10DTE): 2,200 traded vs OI 240
- **IWM** PUT 280 2026-11-16 (3DTE): 638 traded vs OI 637
- **SMH** CALL 520 2026-11-16 (3DTE): 506 traded vs OI 217
- **SMH** PUT 465 2026-11-18 (5DTE): 536 traded vs OI 58
- **TSLA** CALL 427.5 2026-11-20 (7DTE): 502 traded vs OI 0
- **TSLA** PUT 390 2026-12-11 (28DTE): 507 traded vs OI 202
- **AMD** PUT 542.5 2026-11-16 (3DTE): 511 traded vs OI 51
- **PLTR** CALL 175 2026-11-20 (7DTE): 7,506 traded vs OI 7,474

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
