# GEX + FLOW SCAN - Fri Nov 13, 02:10 PM ET
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
Last 1m check 14:10:08 ET, last candle SPY 14:09, QQQ 14:09 | no errors
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
| 1 | **GOOGL** | 295.49 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 32 | none: 94 puts 0-7DTE > 6 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only -34% at the target (needs +20%) (42 contracts' greeks worked out here) | POS +$207.1M | 291.25 | 295 | 290 | +$20.0M | - | out (clean 31, ADX 11, RVol 0.6) |
| 2 | **ARM** | 190.45 | FLOW SURGE | **PUTS** | 32 | none: 30 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (23 contracts' greeks worked out here) | NEG -$895k | 190.9 | 190 | 190 | -$3.5M | +$0 bull / -$75k bear | out (clean 33, ADX 18, RVol 0.1) |
| 3 | **MU** | 769.90 | FLIP CROSS down into negative gamma | **PUTS** | 29 | none: 160 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (78 contracts' greeks worked out here) | NEG -$13.6M | 782.98 | 770 | 770 | +$67.0M | +$0 bull / -$3.8M bear | out (clean 30, ADX 17, RVol 0.4) |
| 4 | **AVGO** | 346.92 | - | **-** | 21 | - | POS +$88.1M | 339.16 | 350 | 350 | +$16.3M | +$26k bull / -$34k bear | out (clean 36, ADX 17, RVol 0.2) |
| 5 | **AMZN** | 265.83 | - | **-** | 20 | - | POS +$440.2M | 252.61 | 265 | 265 | +$8.9M | +$58k bull / +$0 bear | out (clean 29, ADX 16, RVol 0.2) |
| 6 | **QQQ** | 680.21 | - | **-** | 19 | - | NEG -$3.4B | 690.52 | 680 | 680 | +$214.7M | +$0 bull / -$3.4M bear | out (clean 32, ADX 21, RVol 0.6) |
| 7 | **AMD** | 532.68 | - | **-** | 19 | - | POS +$51.5M | - | 530 | 530 | +$54.3M | +$0 bull / -$3.4M bear | out (clean 35, ADX 22, RVol 0.6) |
| 8 | **META** | 642.54 | - | **-** | 19 | - | POS +$186.5M | 636.06 | 650 | 640 | -$3.7M | +$0 bull / -$573k bear | out (clean 30, ADX 33, RVol 1.1) |
| 9 | **ORCL** | 125.55 | - | **-** | 19 | - | POS +$555k | 125.5 | 125 | 125 | -$2.1M | +$0 bull / -$119k bear | out (clean 31, ADX 20, RVol 0.6) |
| 10 | **SPY** | 753.84 | - | **-** | 18 | - | NEG -$8.6B | 760.48 | 775 | 755 | +$194.0M | +$0 bull / -$6.2M bear | out (clean 33, ADX 22, RVol 0.5) |
| 11 | **SMH** | 486.30 | - | **-** | 18 | - | NEG -$288.4M | - | 500 | 475 | +$7.3M | +$0 bull / -$270k bear | out (clean 31, ADX 21, RVol 0.5) |
| 12 | **NVDA** | 162.65 | - | **-** | 18 | - | NEG -$319.7M | - | 175 | 165 | +$76.7M | +$753k bull / -$5.4M bear | out (clean 31, ADX 18, RVol 0.4) |
| 13 | **DELL** | 345.68 | - | **-** | 18 | - | NEG -$14.8M | - | 350 | 350 | +$3.8M | +$0 bull / -$917k bear | out (clean 38, ADX 23, RVol 0.3) |
| 14 | **SMCI** | 26.89 | - | **-** | 17 | - | NEG -$2.9M | 27.75 | 27 | 27 | -$1.8M | - | out (clean 34, ADX 30, RVol 0.3) |
| 15 | **MSTR** | 112.21 | - | **-** | 17 | - | NEG -$31.3M | - | 120 | 110 | +$636k | +$0 bull / -$932k bear | out (clean 31, ADX 28, RVol 0.7) |
| 16 | **TSLA** | 392.24 | - | **-** | 16 | - | POS +$438.5M | 377.76 | 400 | 390 | +$38.1M | +$0 bull / -$1.6M bear | out (clean 28, ADX 11, RVol 0.6) |
| 17 | **AAPL** | 358.57 | - | **-** | 16 | - | POS +$1.3B | 350.03 | 360 | 360 | +$8.9M | +$25k bull / -$79k bear | out (clean 30, ADX 16, RVol 0.5) |
| 18 | **PLTR** | 169.09 | - | **-** | 14 | - | POS +$117.9M | 160.07 | 170 | 170 | -$550k | +$183k bull / +$0 bear | out (clean 29, ADX 16, RVol 0.4) |
| 19 | **MSFT** | 525.02 | - | **-** | 12 | - | POS +$122.6M | 523.3 | 535 | 520 | -$218k | +$0 bull / -$95k bear | out (clean 31, ADX 7, RVol 0.3) |
| 20 | **COIN** | 128.91 | - | **-** | 11 | - | NEG -$22.7M | 132.59 | 140 | 130 | +$2.9M | - | out (clean 30, ADX 12, RVol 0.4) |
| 21 | **HOOD** | 78.58 | - | **-** | 11 | - | NEG -$15.7M | 80.15 | 78 | 79 | +$2.5M | - | out (clean 35, ADX 15, RVol 0.8) |
| 22 | **IWM** | 277.19 | - | **-** | 10 | - | NEG -$2.6B | 282.61 | 285 | 275 | +$16.4M | - | out (clean 36, ADX 19, RVol 0.3) |
| 23 | **UBER** | 69.51 | - | **-** | 10 | - | POS +$14.1M | 69.1 | 70 | 70 | +$246k | - | out (clean 33, ADX 17, RVol 0.4) |
| 24 | **CRM** | 218.36 | - | **-** | 9 | - | NEG -$5.2M | 222.52 | 220 | 220 | +$91k | - | out (clean 27, ADX 23, RVol 0.5) |
| 25 | **NFLX** | 62.34 | - | **-** | 7 | - | NEG -$43.2M | 63.33 | 65 | 62 | +$403k | - | out (clean 31, ADX 17, RVol 0.7) |
| 26 | **SHOP** | 147.50 | - | **-** | 3 | - | POS +$3.4M | 146.44 | 150 | 140 | +$17k | - | out (clean 31, ADX 10, RVol 0.4) |
| 27 | **BABA** | 94.03 | - | **-** | 3 | - | NEG -$20.1M | - | 100 | 95 | -$2k | - | out (clean 27, ADX 12, RVol 0.4) |

## Big prints this scan (87)
- **SPY** CALL 745 2026-11-16 (3DTE): 2,000 @ 9.25 = **+$1.9M** SELL | vol 64,223 / OI 981
- **SPY** CALL 745 2026-11-16 (3DTE): 1,582 @ 9.14 = **+$1.4M** SELL | vol 64,223 / OI 981
- **NVDA** CALL 160 2026-11-16 (3DTE): 1,525 @ 4.75 = **+$724k** MID | vol 72,893 / OI 919
- **NVDA** CALL 160 2026-11-16 (3DTE): 1,018 @ 4.75 = **+$484k** MID | vol 72,893 / OI 919
- **NVDA** CALL 160 2026-11-16 (3DTE): 1,000 @ 4.80 = **+$480k** BUY | vol 72,893 / OI 919
- **TSLA** CALL 395 2026-11-20 (7DTE): 498 @ 9.00 = **+$448k** SELL | vol 8,763 / OI 2,968
- **NVDA** CALL 160 2026-11-16 (3DTE): 873 @ 4.75 = **+$415k** MID | vol 72,893 / OI 919
- **MU** CALL 732.5 2026-11-13 (0DTE): 106 @ 32.36 = **+$343k** SELL | vol 189 / OI 333
- **SPY** CALL 759 2026-11-20 (7DTE): 577 @ 4.21 = **+$243k** MID | vol 5,510 / OI 2,563
- **SMH** PUT 500 2026-11-20 (7DTE): 99 @ 24.29 = **+$240k** BUY | vol 1,210 / OI 9,935
- **MU** CALL 732.5 2026-11-13 (0DTE): 70 @ 32.36 = **+$227k** SELL | vol 189 / OI 333
- **NVDA** PUT 155 2026-11-18 (5DTE): 499 @ 4.26 = **+$213k** BUY | vol 6,141 / OI 1,724
- **QQQ** CALL 680 2026-11-20 (7DTE): 191 @ 10.39 = **+$198k** SELL | vol 9,315 / OI 32,370
- **NVDA** CALL 160 2026-11-16 (3DTE): 404 @ 4.75 = **+$192k** MID | vol 72,893 / OI 919
- **QQQ** CALL 680 2026-11-20 (7DTE): 162 @ 10.55 = **+$171k** SELL | vol 9,315 / OI 32,370

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 766 2026-11-18 (5DTE): 873 traded vs OI 862
- **SPY** PUT 742 2026-12-11 (28DTE): 616 traded vs OI 581
- **QQQ** CALL 668 2026-11-16 (3DTE): 501 traded vs OI 163
- **QQQ** CALL 679 2026-11-17 (4DTE): 563 traded vs OI 218
- **QQQ** CALL 673 2026-11-20 (7DTE): 500 traded vs OI 321
- **NVDA** PUT 155 2026-11-20 (7DTE): 14,751 traded vs OI 14,723
- **AMD** CALL 527.5 2026-11-20 (7DTE): 505 traded vs OI 341
- **GOOGL** CALL 302.5 2026-11-18 (5DTE): 505 traded vs OI 50
- **AVGO** CALL 360 2026-11-13 (0DTE): 3,407 traded vs OI 3,384
- **MSTR** CALL 123 2026-11-20 (7DTE): 612 traded vs OI 0
- **MSTR** PUT 123 2026-11-13 (0DTE): 2,302 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
