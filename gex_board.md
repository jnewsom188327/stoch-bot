# GEX + FLOW SCAN - Fri Nov 13, 01:10 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (13)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 12:45 | **HOOD** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/13 78C | 0.58 | 0.44 | +12% (3m) | **-24%** | +75% | 79 |
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

## 1m RULES on SPY / QQQ - loose (4 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 13:10:08 ET, last candle SPY 13:09, QQQ 13:09 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
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
| 1 | **GOOGL** | 295.25 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 44 | 11/13 295P @ 0.76 (delta 0.45) = est +78% at 293.74 | POS +$213.2M | 290.12 | 295 | 290 | +$20.2M | +$506k bull / -$52k bear | out (clean 31, ADX 15, RVol 0.5) |
| 2 | **META** | 635.46 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 39 | none: 189 calls 0-7DTE > 8 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (82 contracts' greeks worked out here) | POS +$69.1M | 631.88 | 650 | 635 | +$4.0M | +$1.1M bull / -$275k bear | out (clean 29, ADX 27, RVol 1.2) |
| 3 | **TSLA** | 389.49 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 34 | 11/13 392.5C @ 0.71 (delta 0.25) = est +111% at 392.97 | POS +$385.8M | - | 400 | 390 | +$46.0M | +$156k bull / -$304k bear | out (clean 28, ADX 11, RVol 0.4) |
| 4 | **COIN** | 128.46 | FLOW SURGE | **CALLS** | 33 | 11/13 129C @ 0.54 (delta 0.39) = est +103% at 130 | NEG -$22.0M | 132.57 | 140 | 130 | +$3.5M | +$101k bull / +$0 bear | out (clean 31, ADX 18, RVol 0.2) |
| 5 | **AMZN** | 265.50 | PINNED between the walls (positive gamma) - chop | **-** | 32 | - | POS +$463.1M | 251.28 | 265 | 265 | +$8.1M | +$125k bull / -$103k bear | out (clean 30, ADX 21, RVol 0.2) |
| 6 | **PLTR** | 167.56 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 31 | 11/13 167.5P @ 0.79 (delta 0.48) = est +57% at 166.32 | POS +$96.4M | 161.08 | 167.5 | 165 | +$1.7M | +$1.5M bull / +$0 bear | out (clean 28, ADX 14, RVol 0.2) |
| 7 | **MU** | 761.83 | FLIP CROSS down into negative gamma | **PUTS** | 31 | none: 164 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (80 contracts' greeks worked out here) | NEG -$13.7M | 774.79 | 760 | 750 | +$71.8M | +$1.7M bull / -$674k bear | out (clean 30, ADX 18, RVol 0.4) |
| 8 | **DELL** | 338.96 | - | **-** | 25 | - | NEG -$6.9M | 351.88 | 337.5 | 340 | +$7.6M | +$69k bull / +$0 bear | out (clean 38, ADX 26, RVol 1.1) |
| 9 | **AVGO** | 344.99 | - | **-** | 24 | - | POS +$81.2M | 332.82 | 350 | 340 | +$18.9M | +$1.1M bull / -$110k bear | out (clean 36, ADX 24, RVol 0.3) |
| 10 | **HOOD** | 78.11 | - | **-** | 23 | - | NEG -$16.4M | 80.16 | 78 | 80 | +$2.6M | +$0 bull / -$540k bear | out (clean 36, ADX 22, RVol 1.2) |
| 11 | **AMD** | 523.13 | - | **-** | 22 | - | POS +$27.6M | - | 530 | 530 | +$75.0M | +$1.8M bull / -$232k bear | out (clean 35, ADX 29, RVol 0.4) |
| 12 | **QQQ** | 676.33 | - | **-** | 20 | - | NEG -$3.1B | 689.6 | 680 | 680 | +$261.3M | +$857k bull / -$797k bear | out (clean 32, ADX 22, RVol 0.3) |
| 13 | **SMH** | 481.04 | - | **-** | 20 | - | NEG -$354.3M | - | 500 | 475 | +$10.1M | +$27k bull / -$25k bear | out (clean 31, ADX 22, RVol 0.3) |
| 14 | **NVDA** | 160.90 | - | **-** | 19 | - | NEG -$287.6M | - | 175 | 160 | +$104.8M | +$574k bull / -$652k bear | out (clean 31, ADX 9, RVol 0.3) |
| 15 | **SPY** | 751.22 | - | **-** | 18 | - | NEG -$8.5B | 760.12 | 750 | 750 | +$246.5M | +$4.5M bull / -$1.6M bear | out (clean 33, ADX 18, RVol 0.3) |
| 16 | **AAPL** | 357.39 | - | **-** | 17 | - | POS +$1.3B | 346.95 | 360 | 360 | +$12.3M | +$198k bull / -$901k bear | out (clean 30, ADX 12, RVol 0.7) |
| 17 | **MSTR** | 110.66 | - | **-** | 15 | - | NEG -$49.1M | - | 110 | 110 | +$684k | +$36k bull / +$0 bear | out (clean 30, ADX 21, RVol 0.4) |
| 18 | **ARM** | 187.87 | - | **-** | 15 | - | NEG -$2.4M | 190.49 | 190 | 190 | -$3.3M | - | out (clean 33, ADX 27, RVol 0.2) |
| 19 | **CRM** | 217.16 | - | **-** | 13 | - | NEG -$4.1M | 218.53 | 220 | 220 | +$120k | - | out (clean 27, ADX 24, RVol 1.4) |
| 20 | **MSFT** | 524.38 | - | **-** | 12 | - | POS +$132.0M | 522.51 | 535 | 520 | -$622k | +$30k bull / -$61k bear | out (clean 31, ADX 9, RVol 0.3) |
| 21 | **UBER** | 69.34 | - | **-** | 12 | - | POS +$11.1M | 68.94 | 70 | 70 | +$310k | - | out (clean 32, ADX 12, RVol 0.3) |
| 22 | **IWM** | 276.44 | - | **-** | 11 | - | NEG -$2.6B | 282.26 | 285 | 275 | +$18.9M | - | out (clean 36, ADX 18, RVol 0.3) |
| 23 | **NFLX** | 62.28 | - | **-** | 10 | - | NEG -$40.7M | 63.33 | 65 | 62 | +$501k | - | out (clean 31, ADX 29, RVol 0.7) |
| 24 | **SMCI** | 26.38 | - | **-** | 8 | - | NEG -$3.0M | 27.84 | 27 | 25 | +$177k | - | out (clean 34, ADX 22, RVol 0.5) |
| 25 | **ORCL** | 124.00 | - | **-** | 6 | - | POS +$7.1M | 123.22 | 125 | 125 | -$1.0M | - | out (clean 31, ADX 15, RVol 0.4) |
| 26 | **BABA** | 93.94 | - | **-** | 4 | - | NEG -$17.9M | - | 100 | 95 | -$36k | - | out (clean 27, ADX 15, RVol 0.2) |
| 27 | **SHOP** | 147.03 | - | **-** | 3 | - | POS +$3.7M | 145.69 | 150 | 140 | +$12k | - | out (clean 31, ADX 14, RVol 0.3) |

## Big prints this scan (54)
- **SPY** CALL 745 2026-11-16 (3DTE): 1,938 @ 8.56 = **+$1.7M** BUY | vol 33,532 / OI 981
- **META** CALL 640 2026-11-18 (5DTE): 197 @ 11.80 = **+$232k** BUY | vol 533 / OI 109
- **META** CALL 642.5 2026-11-18 (5DTE): 197 @ 10.63 = **+$209k** BUY | vol 328 / OI 31
- **META** CALL 637.5 2026-11-13 (0DTE): 530 @ 3.70 = **+$196k** BUY | vol 21,002 / OI 590
- **GOOGL** CALL 302.5 2026-11-20 (7DTE): 500 @ 3.23 = **+$162k** BUY | vol 2,640 / OI 1,099
- **GOOGL** CALL 302.5 2026-11-20 (7DTE): 500 @ 3.23 = **+$162k** BUY | vol 2,640 / OI 1,099
- **QQQ** PUT 697 2026-11-20 (7DTE): 50 @ 22.65 = **+$113k** SELL | vol 138 / OI 1,850
- **QQQ** PUT 697 2026-11-18 (5DTE): 50 @ 21.44 = **+$107k** SELL | vol 65 / OI 69
- **GOOGL** CALL 310 2026-11-20 (7DTE): 500 @ 1.48 = **+$74k** BUY | vol 9,763 / OI 7,746
- **GOOGL** CALL 310 2026-11-20 (7DTE): 500 @ 1.48 = **+$74k** BUY | vol 9,763 / OI 7,746
- **META** CALL 640 2026-11-20 (7DTE): 40 @ 15.25 = **+$61k** BUY | vol 2,570 / OI 4,178
- **MU** CALL 765 2026-11-13 (0DTE): 119 @ 5.05 = **+$60k** BUY | vol 18,291 / OI 930
- **META** CALL 635 2026-11-13 (0DTE): 110 @ 5.15 = **+$57k** BUY | vol 35,403 / OI 1,018
- **TSLA** CALL 400 2026-11-20 (7DTE): 80 @ 6.95 = **+$56k** BUY | vol 12,145 / OI 21,808
- **AMD** PUT 515 2026-11-20 (7DTE): 25 @ 20.42 = **+$51k** SELL | vol 246 / OI 321

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 745 2026-11-18 (5DTE): 872 traded vs OI 870
- **SPY** CALL 812 2026-11-20 (7DTE): 1,750 traded vs OI 1,554
- **QQQ** PUT 677 2026-11-17 (4DTE): 507 traded vs OI 462
- **QQQ** CALL 720 2026-12-11 (28DTE): 2,095 traded vs OI 586
- **META** CALL 640 2026-11-18 (5DTE): 533 traded vs OI 109
- **GOOGL** CALL 312.5 2026-11-13 (0DTE): 2,105 traded vs OI 2,042
- **DELL** CALL 347.5 2026-11-13 (0DTE): 510 traded vs OI 104

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
