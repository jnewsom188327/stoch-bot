# GEX + FLOW SCAN - Fri Nov 13, 02:00 PM ET
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
Last 1m check 14:00:08 ET, last candle SPY 13:59, QQQ 13:59 | no errors
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
| 1 | **GOOGL** | 295.57 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 43 | none: 94 puts 0-7DTE > 8 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only -29% at the target (needs +20%) (48 contracts' greeks worked out here) | POS +$237.7M | 290.26 | 295 | 290 | +$19.5M | +$0 bull / -$283k bear | out (clean 31, ADX 13, RVol 0.6) |
| 2 | **AMD** | 530.09 | PINNED between the walls (positive gamma) - chop | **-** | 32 | - | POS +$32.3M | 520.53 | 530 | 530 | +$61.0M | +$676k bull / -$4.0M bear | out (clean 35, ADX 21, RVol 0.6) |
| 3 | **ARM** | 190.26 | FLOW SURGE | **PUTS** | 32 | none: 30 puts 0-7DTE > 1 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only +17% at the target (needs +20%) (23 contracts' greeks worked out here) | NEG -$2.2M | 191.32 | 190 | 190 | -$3.5M | +$0 bull / -$75k bear | out (clean 33, ADX 18, RVol 0.1) |
| 4 | **AVGO** | 346.31 | - | **-** | 21 | - | POS +$109.4M | - | 350 | 340 | +$16.5M | +$26k bull / -$986k bear | out (clean 36, ADX 19, RVol 0.2) |
| 5 | **ORCL** | 125.31 | PINNED between the walls (positive gamma) - chop | **-** | 21 | - | POS +$194k | 125.29 | 125 | 125 | -$1.8M | - | out (clean 31, ADX 17, RVol 0.6) |
| 6 | **AMZN** | 265.84 | - | **-** | 20 | - | POS +$447.3M | 253.93 | 265 | 265 | +$8.6M | +$0 bull / -$34k bear | out (clean 30, ADX 18, RVol 0.2) |
| 7 | **QQQ** | 679.24 | - | **-** | 19 | - | NEG -$3.4B | 690.17 | 680 | 680 | +$228.5M | +$0 bull / -$1.4M bear | out (clean 32, ADX 20, RVol 0.5) |
| 8 | **SMH** | 485.01 | - | **-** | 19 | - | NEG -$294.3M | - | 500 | 475 | +$8.3M | +$0 bull / -$379k bear | out (clean 31, ADX 20, RVol 0.4) |
| 9 | **SPY** | 753.27 | - | **-** | 18 | - | NEG -$8.7B | 760.49 | 775 | 755 | +$210.8M | +$0 bull / -$10.5M bear | out (clean 33, ADX 21, RVol 0.5) |
| 10 | **DELL** | 345.50 | - | **-** | 18 | - | NEG -$17.2M | - | 350 | 360 | +$3.9M | +$26k bull / -$277k bear | out (clean 38, ADX 22, RVol 0.3) |
| 11 | **NVDA** | 162.62 | - | **-** | 17 | - | NEG -$327.6M | - | 175 | 160 | +$78.5M | +$139k bull / -$7.0M bear | out (clean 31, ADX 15, RVol 0.3) |
| 12 | **META** | 641.26 | - | **-** | 17 | - | POS +$138.4M | 637.58 | 650 | 635 | -$83k | +$0 bull / -$516k bear | out (clean 30, ADX 31, RVol 1.0) |
| 13 | **MU** | 767.44 | - | **-** | 17 | - | NEG -$41.6M | 780.37 | 770 | 750 | +$71.7M | +$96k bull / -$3.4M bear | out (clean 30, ADX 15, RVol 0.3) |
| 14 | **TSLA** | 391.18 | - | **-** | 16 | - | POS +$438.8M | - | 390 | 390 | +$39.2M | +$350k bull / -$3.0M bear | out (clean 28, ADX 10, RVol 0.5) |
| 15 | **AAPL** | 358.31 | - | **-** | 16 | - | POS +$1.3B | 347.6 | 360 | 360 | +$9.1M | +$763k bull / -$276k bear | out (clean 30, ADX 14, RVol 0.5) |
| 16 | **SMCI** | 26.81 | - | **-** | 16 | - | NEG -$2.7M | 27.81 | 27 | 27 | -$1.8M | - | out (clean 34, ADX 28, RVol 0.4) |
| 17 | **MSTR** | 111.67 | - | **-** | 16 | - | NEG -$42.2M | - | 120 | 110 | +$838k | +$94k bull / -$1.0M bear | out (clean 31, ADX 26, RVol 0.5) |
| 18 | **PLTR** | 168.45 | - | **-** | 15 | - | POS +$91.2M | 166.37 | 170 | 170 | +$852k | +$183k bull / -$93k bear | out (clean 28, ADX 16, RVol 0.5) |
| 19 | **BABA** | 94.02 | - | **-** | 13 | - | NEG -$19.1M | - | 100 | 95 | -$2k | +$0 bull / -$62k bear | out (clean 27, ADX 11, RVol 0.3) |
| 20 | **MSFT** | 524.66 | - | **-** | 12 | - | POS +$90.9M | 522.14 | 535 | 520 | -$137k | +$29k bull / -$26k bear | out (clean 31, ADX 7, RVol 0.3) |
| 21 | **UBER** | 69.50 | - | **-** | 12 | - | POS +$13.3M | 69.12 | 70 | 70 | +$316k | - | out (clean 33, ADX 16, RVol 0.3) |
| 22 | **COIN** | 128.66 | - | **-** | 11 | - | NEG -$20.7M | 132.54 | 140 | 130 | +$2.9M | - | out (clean 30, ADX 13, RVol 0.4) |
| 23 | **HOOD** | 78.32 | - | **-** | 11 | - | NEG -$16.1M | 80.14 | 78 | 80 | +$2.6M | - | out (clean 35, ADX 16, RVol 1.0) |
| 24 | **IWM** | 276.98 | - | **-** | 10 | - | NEG -$2.7B | 282.76 | 285 | 275 | +$16.8M | - | out (clean 36, ADX 20, RVol 0.3) |
| 25 | **CRM** | 218.01 | - | **-** | 9 | - | NEG -$3.2M | 219.08 | 220 | 220 | +$101k | - | out (clean 27, ADX 20, RVol 0.8) |
| 26 | **NFLX** | 62.45 | - | **-** | 7 | - | NEG -$42.0M | 63.65 | 65 | 62 | +$399k | - | out (clean 31, ADX 18, RVol 0.5) |
| 27 | **SHOP** | 147.24 | - | **-** | 3 | - | POS +$5.4M | 145.73 | 150 | 140 | +$18k | - | out (clean 31, ADX 11, RVol 0.3) |

## Big prints this scan (114)
- **NVDA** CALL 160 2026-11-16 (3DTE): 2,304 @ 4.45 = **+$1.0M** SELL | vol 66,634 / OI 919
- **TSLA** CALL 400 2026-11-20 (7DTE): 900 @ 6.62 = **+$596k** SELL | vol 13,688 / OI 21,808
- **AMZN** CALL 265 2026-11-20 (7DTE): 1,000 @ 5.80 = **+$580k** MID | vol 2,365 / OI 31,267
- **MSTR** CALL 114 2026-11-20 (7DTE): 1,250 @ 3.62 = **+$452k** SELL | vol 13,069 / OI 0
- **MSTR** CALL 114 2026-11-20 (7DTE): 1,250 @ 3.62 = **+$452k** SELL | vol 13,069 / OI 0
- **AMD** CALL 530 2026-11-20 (7DTE): 150 @ 23.65 = **+$355k** SELL | vol 2,720 / OI 2,460
- **AMD** CALL 535 2026-11-20 (7DTE): 150 @ 21.25 = **+$319k** SELL | vol 889 / OI 932
- **AMD** PUT 540 2026-11-20 (7DTE): 100 @ 30.35 = **+$304k** BUY | vol 2,417 / OI 2,289
- **AMD** CALL 540 2026-11-20 (7DTE): 104 @ 19.15 = **+$199k** SELL | vol 4,143 / OI 4,301
- **NVDA** CALL 160 2026-11-16 (3DTE): 434 @ 4.45 = **+$193k** SELL | vol 66,634 / OI 919
- **MU** CALL 747.5 2026-11-13 (0DTE): 100 @ 17.83 = **+$178k** SELL | vol 756 / OI 112
- **AMD** CALL 540 2026-11-20 (7DTE): 92 @ 19.28 = **+$177k** MID | vol 4,143 / OI 4,301
- **QQQ** CALL 675 2026-11-13 (0DTE): 458 @ 3.74 = **+$171k** SELL | vol 151,122 / OI 5,568
- **AMD** CALL 540 2026-11-20 (7DTE): 80 @ 19.30 = **+$154k** MID | vol 4,143 / OI 4,301
- **AMD** CALL 540 2026-11-20 (7DTE): 76 @ 19.28 = **+$147k** MID | vol 4,143 / OI 4,301

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 769 2026-11-18 (5DTE): 500 traded vs OI 496
- **SPY** CALL 748 2026-11-20 (7DTE): 795 traded vs OI 786
- **QQQ** PUT 688 2026-11-17 (4DTE): 686 traded vs OI 119
- **IWM** PUT 279 2026-11-17 (4DTE): 501 traded vs OI 440
- **NVDA** CALL 170 2026-12-04 (21DTE): 1,786 traded vs OI 1,750
- **META** PUT 637.5 2026-11-16 (3DTE): 502 traded vs OI 126
- **DELL** CALL 380 2026-11-13 (0DTE): 802 traded vs OI 544
- **MU** PUT 707.5 2026-11-13 (0DTE): 540 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
