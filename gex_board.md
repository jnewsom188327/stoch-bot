# GEX + FLOW SCAN - Fri Nov 13, 01:20 PM ET
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
Last 1m check 13:20:08 ET, last candle SPY 13:19, QQQ 13:18 | no errors
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
| 1 | **GOOGL** | 295.19 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 44 | 11/13 295P @ 0.78 (delta 0.46) = est +69% at 293.76 | POS +$202.7M | 290.23 | 295 | 290 | +$20.1M | +$506k bull / +$0 bear | out (clean 31, ADX 14, RVol 0.6) |
| 2 | **META** | 635.17 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 39 | none: 189 calls 0-7DTE > 9 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (80 contracts' greeks worked out here) | POS +$45.1M | 632.85 | 650 | 635 | +$7.1M | +$1.8M bull / -$61k bear | out (clean 29, ADX 25, RVol 1.1) |
| 3 | **AMZN** | 265.27 | PINNED between the walls (positive gamma) - chop | **-** | 33 | - | POS +$382.5M | 252.18 | 265 | 265 | +$8.8M | +$26k bull / +$0 bear | out (clean 30, ADX 19, RVol 0.3) |
| 4 | **PLTR** | 167.86 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 32 | none: 26 puts 0-7DTE > 1 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only -21% at the target (needs +20%) (21 contracts' greeks worked out here) | POS +$96.1M | 163.03 | 167.5 | 170 | +$1.6M | +$1.5M bull / +$0 bear | out (clean 28, ADX 12, RVol 0.4) |
| 5 | **TSLA** | 389.88 | PINNED between the walls (positive gamma) - chop | **-** | 29 | - | POS +$358.0M | - | 390 | 390 | +$45.6M | +$538k bull / -$62k bear | out (clean 28, ADX 10, RVol 0.4) |
| 6 | **DELL** | 339.71 | - | **-** | 24 | - | NEG -$9.1M | - | 350 | 340 | +$7.3M | +$38k bull / -$33k bear | out (clean 38, ADX 23, RVol 1.1) |
| 7 | **AVGO** | 344.90 | - | **-** | 23 | - | POS +$76.2M | 336.55 | 350 | 340 | +$18.6M | +$221k bull / -$272k bear | out (clean 36, ADX 21, RVol 0.3) |
| 8 | **COIN** | 128.45 | - | **-** | 22 | - | NEG -$21.9M | 132.53 | 140 | 130 | +$2.9M | +$101k bull / -$516k bear | out (clean 31, ADX 16, RVol 0.3) |
| 9 | **AMD** | 523.42 | - | **-** | 21 | - | POS +$23.3M | - | 530 | 530 | +$72.4M | +$913k bull / -$550k bear | out (clean 35, ADX 28, RVol 0.3) |
| 10 | **QQQ** | 676.24 | - | **-** | 19 | - | NEG -$2.6B | 684.21 | 680 | 680 | +$256.2M | +$578k bull / -$289k bear | out (clean 32, ADX 19, RVol 0.2) |
| 11 | **SMH** | 481.37 | - | **-** | 19 | - | NEG -$354.9M | - | 500 | 475 | +$9.7M | +$27k bull / -$267k bear | out (clean 31, ADX 20, RVol 0.1) |
| 12 | **NVDA** | 161.06 | - | **-** | 18 | - | NEG -$321.7M | - | 175 | 160 | +$103.9M | +$529k bull / -$252k bear | out (clean 31, ADX 8, RVol 0.3) |
| 13 | **MU** | 761.21 | - | **-** | 18 | - | NEG -$8.4M | 768.2 | 760 | 750 | +$74.5M | +$1.5M bull / -$91k bear | out (clean 30, ADX 16, RVol 0.3) |
| 14 | **SPY** | 751.52 | - | **-** | 17 | - | NEG -$8.5B | 760.4 | 750 | 750 | +$238.6M | +$3.2M bull / -$2.3M bear | out (clean 33, ADX 16, RVol 0.2) |
| 15 | **AAPL** | 358.06 | - | **-** | 17 | - | POS +$1.2B | 348.54 | 360 | 360 | +$11.2M | +$0 bull / -$1.3M bear | out (clean 30, ADX 11, RVol 0.9) |
| 16 | **ORCL** | 124.19 | - | **-** | 16 | - | POS +$488k | 123.66 | 125 | 125 | -$1.4M | +$256k bull / +$0 bear | out (clean 31, ADX 14, RVol 0.5) |
| 17 | **ARM** | 188.09 | - | **-** | 15 | - | NEG -$3.0M | 190.95 | 190 | 190 | -$3.3M | - | out (clean 33, ADX 26, RVol 0.1) |
| 18 | **MSFT** | 524.54 | - | **-** | 13 | - | POS +$143.9M | 522.08 | 535 | 520 | -$959k | +$30k bull / +$0 bear | out (clean 31, ADX 8, RVol 0.3) |
| 19 | **UBER** | 69.27 | - | **-** | 13 | - | POS +$8.7M | 68.94 | 70 | 70 | +$328k | - | out (clean 33, ADX 14, RVol 0.3) |
| 20 | **CRM** | 217.38 | - | **-** | 13 | - | NEG -$5.9M | 219.67 | 220 | 220 | +$131k | - | out (clean 27, ADX 22, RVol 1.4) |
| 21 | **HOOD** | 78.16 | - | **-** | 12 | - | NEG -$13.3M | 79.84 | 78 | 80 | +$2.6M | - | out (clean 36, ADX 21, RVol 1.1) |
| 22 | **IWM** | 276.71 | - | **-** | 10 | - | NEG -$2.7B | 282.69 | 285 | 275 | +$17.9M | - | out (clean 36, ADX 17, RVol 0.3) |
| 23 | **NFLX** | 62.31 | - | **-** | 9 | - | NEG -$45.3M | 63.34 | 65 | 62 | +$491k | - | out (clean 31, ADX 29, RVol 0.6) |
| 24 | **SMCI** | 26.45 | - | **-** | 7 | - | NEG -$3.2M | - | 27 | 27 | +$185k | - | out (clean 34, ADX 20, RVol 0.3) |
| 25 | **MSTR** | 110.68 | - | **-** | 5 | - | NEG -$44.3M | - | 110 | 110 | +$516k | - | out (clean 30, ADX 21, RVol 0.3) |
| 26 | **SHOP** | 147.08 | - | **-** | 3 | - | POS +$2.9M | 145.67 | 150 | 140 | +$12k | - | out (clean 31, ADX 13, RVol 0.2) |
| 27 | **BABA** | 93.90 | - | **-** | 3 | - | NEG -$15.6M | - | 100 | 100 | -$8k | - | out (clean 28, ADX 15, RVol 0.1) |

## Big prints this scan (60)
- **SPY** CALL 745 2026-11-16 (3DTE): 2,000 @ 8.01 = **+$1.6M** SELL | vol 39,763 / OI 981
- **AAPL** CALL 360 2026-11-20 (7DTE): 1,707 @ 3.29 = **+$562k** SELL | vol 8,466 / OI 25,141
- **AAPL** CALL 355 2026-11-13 (0DTE): 1,707 @ 2.74 = **+$468k** SELL | vol 7,280 / OI 14,672
- **SPY** CALL 745 2026-11-16 (3DTE): 546 @ 7.79 = **+$425k** SELL | vol 39,763 / OI 981
- **QQQ** PUT 677 2026-11-13 (0DTE): 1,200 @ 2.41 = **+$289k** BUY | vol 80,650 / OI 2,463
- **SMH** PUT 500 2026-11-20 (7DTE): 99 @ 26.97 = **+$267k** BUY | vol 1,006 / OI 9,935
- **COIN** CALL 132 2026-11-20 (7DTE): 750 @ 3.44 = **+$258k** SELL | vol 1,606 / OI 37
- **AAPL** CALL 365 2026-11-20 (7DTE): 1,707 @ 1.50 = **+$256k** SELL | vol 20,075 / OI 45,955
- **COIN** CALL 132 2026-11-20 (7DTE): 600 @ 3.44 = **+$206k** SELL | vol 1,606 / OI 37
- **SPY** CALL 745 2026-11-16 (3DTE): 254 @ 7.79 = **+$198k** SELL | vol 39,763 / OI 981
- **AVGO** CALL 342.5 2026-11-20 (7DTE): 100 @ 13.48 = **+$135k** MID | vol 514 / OI 2,060
- **QQQ** CALL 678 2026-11-13 (0DTE): 1,000 @ 1.13 = **+$113k** BUY | vol 144,780 / OI 1,154
- **SPY** CALL 745 2026-11-16 (3DTE): 141 @ 7.79 = **+$110k** SELL | vol 39,763 / OI 981
- **AVGO** PUT 342.5 2026-11-20 (7DTE): 100 @ 10.67 = **+$107k** SELL | vol 577 / OI 518
- **MU** CALL 725 2026-11-20 (7DTE): 16 @ 56.94 = **+$91k** SELL | vol 51 / OI 170

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 754 2026-11-19 (6DTE): 629 traded vs OI 122
- **SPY** CALL 770 2026-11-16 (3DTE): 7,292 traded vs OI 6,922
- **QQQ** CALL 703 2026-11-16 (3DTE): 902 traded vs OI 878
- **QQQ** PUT 674 2026-11-18 (5DTE): 500 traded vs OI 179
- **QQQ** CALL 700 2026-11-23 (10DTE): 5,785 traded vs OI 4,729
- **QQQ** CALL 705 2026-11-19 (6DTE): 5,185 traded vs OI 208
- **QQQ** CALL 675 2026-11-19 (6DTE): 527 traded vs OI 389
- **QQQ** CALL 677 2026-11-27 (14DTE): 505 traded vs OI 0
- **IWM** PUT 275 2026-11-19 (6DTE): 565 traded vs OI 130
- **SMH** CALL 487.5 2026-11-13 (0DTE): 1,019 traded vs OI 360
- **NVDA** PUT 162.5 2026-11-23 (10DTE): 500 traded vs OI 86
- **AAPL** CALL 367.5 2026-11-27 (14DTE): 10,200 traded vs OI 284
- **AMD** PUT 487.5 2026-11-13 (0DTE): 635 traded vs OI 0
- **META** CALL 642.5 2026-11-16 (3DTE): 513 traded vs OI 260
- **AMZN** CALL 290 2026-11-16 (3DTE): 617 traded vs OI 610

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
