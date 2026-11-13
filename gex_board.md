# GEX + FLOW SCAN - Fri Nov 13, 01:50 PM ET
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
Last 1m check 13:50:08 ET, last candle SPY 13:49, QQQ 13:49 | no errors
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
| 1 | **MU** | 763.41 | FLIP CROSS down into negative gamma | **PUTS** | 29 | none: 164 puts 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (80 contracts' greeks worked out here) | NEG -$1.8M | 765.08 | 760 | 750 | +$71.8M | +$63k bull / -$1.4M bear | out (clean 30, ADX 14, RVol 0.3) |
| 2 | **GOOGL** | 295.74 | - | **-** | 25 | - | POS +$204.8M | 291.23 | 295 | 290 | +$19.3M | +$0 bull / -$283k bear | out (clean 31, ADX 12, RVol 0.5) |
| 3 | **AVGO** | 345.94 | - | **-** | 21 | - | POS +$107.2M | - | 350 | 340 | +$16.2M | +$0 bull / -$1.2M bear | out (clean 35, ADX 19, RVol 0.2) |
| 4 | **AMZN** | 265.89 | - | **-** | 20 | - | POS +$487.4M | 251.03 | 265 | 265 | +$7.8M | +$0 bull / -$34k bear | out (clean 30, ADX 17, RVol 0.2) |
| 5 | **QQQ** | 678.22 | - | **-** | 19 | - | NEG -$2.6B | 684.82 | 680 | 680 | +$239.1M | +$0 bull / -$870k bear | out (clean 32, ADX 19, RVol 0.3) |
| 6 | **AMD** | 526.90 | - | **-** | 19 | - | POS +$47.2M | 513.73 | 530 | 530 | +$62.5M | +$107k bull / -$1.1M bear | out (clean 35, ADX 22, RVol 0.5) |
| 7 | **SPY** | 752.83 | - | **-** | 18 | - | NEG -$7.1B | 758.12 | 775 | 755 | +$214.3M | +$0 bull / -$7.1M bear | out (clean 33, ADX 18, RVol 0.4) |
| 8 | **SMH** | 483.46 | - | **-** | 18 | - | NEG -$304.9M | - | 500 | 475 | +$8.9M | +$0 bull / -$319k bear | out (clean 31, ADX 18, RVol 0.2) |
| 9 | **DELL** | 343.69 | - | **-** | 18 | - | NEG -$11.7M | 358.83 | 350 | 340 | +$3.7M | +$26k bull / -$37k bear | out (clean 38, ADX 22, RVol 0.3) |
| 10 | **NVDA** | 162.18 | - | **-** | 17 | - | NEG -$299.2M | - | 175 | 160 | +$80.8M | +$0 bull / -$4.5M bear | out (clean 31, ADX 12, RVol 0.3) |
| 11 | **META** | 641.16 | - | **-** | 17 | - | POS +$141.9M | 636.56 | 650 | 635 | +$1.8M | +$0 bull / -$305k bear | out (clean 30, ADX 28, RVol 0.8) |
| 12 | **TSLA** | 391.08 | - | **-** | 16 | - | POS +$445.3M | - | 390 | 390 | +$40.4M | +$350k bull / -$3.0M bear | out (clean 28, ADX 9, RVol 0.3) |
| 13 | **AAPL** | 358.25 | - | **-** | 16 | - | POS +$1.4B | 348.77 | 360 | 360 | +$10.3M | +$763k bull / -$237k bear | out (clean 30, ADX 13, RVol 0.5) |
| 14 | **SMCI** | 26.66 | - | **-** | 16 | - | NEG -$2.9M | 27.97 | 27 | 27 | -$1.8M | - | out (clean 34, ADX 26, RVol 0.5) |
| 15 | **MSTR** | 111.25 | - | **-** | 15 | - | NEG -$40.1M | - | 110 | 110 | -$157k | +$94k bull / -$160k bear | out (clean 31, ADX 25, RVol 0.4) |
| 16 | **ARM** | 189.08 | - | **-** | 13 | - | NEG -$3.3M | 191.19 | 190 | 190 | -$3.4M | - | out (clean 33, ADX 19, RVol 0.1) |
| 17 | **MSFT** | 524.39 | - | **-** | 12 | - | POS +$130.6M | 522.7 | 535 | 520 | -$86k | +$29k bull / +$0 bear | out (clean 31, ADX 7, RVol 0.3) |
| 18 | **COIN** | 128.37 | - | **-** | 12 | - | NEG -$17.7M | 131.49 | 140 | 130 | +$2.9M | - | out (clean 31, ADX 14, RVol 0.6) |
| 19 | **UBER** | 69.42 | - | **-** | 12 | - | POS +$12.1M | 69.05 | 70 | 70 | +$321k | - | out (clean 33, ADX 17, RVol 0.2) |
| 20 | **HOOD** | 78.16 | - | **-** | 11 | - | NEG -$13.7M | 79.68 | 78 | 79 | +$2.6M | - | out (clean 36, ADX 18, RVol 0.9) |
| 21 | **IWM** | 276.95 | - | **-** | 10 | - | NEG -$2.6B | 282.4 | 285 | 275 | +$16.6M | - | out (clean 36, ADX 19, RVol 0.4) |
| 22 | **CRM** | 217.72 | - | **-** | 10 | - | NEG -$2.9M | 218.75 | 220 | 220 | +$124k | - | out (clean 27, ADX 20, RVol 0.7) |
| 23 | **ORCL** | 124.97 | - | **-** | 8 | - | NEG -$1.8M | 125.15 | 125 | 125 | -$1.8M | - | out (clean 31, ADX 14, RVol 0.6) |
| 24 | **NFLX** | 62.45 | - | **-** | 7 | - | NEG -$29.4M | 63 | 65 | 62 | +$380k | - | out (clean 31, ADX 20, RVol 0.6) |
| 25 | **PLTR** | 168.42 | - | **-** | 5 | - | POS +$107.5M | 159.73 | 170 | 170 | +$1.1M | - | out (clean 28, ADX 15, RVol 0.4) |
| 26 | **SHOP** | 146.98 | - | **-** | 3 | - | POS +$4.6M | 145.52 | 150 | 140 | +$18k | - | out (clean 31, ADX 12, RVol 0.3) |
| 27 | **BABA** | 94.03 | - | **-** | 3 | - | NEG -$19.9M | - | 100 | 95 | -$16k | - | out (clean 27, ADX 12, RVol 0.3) |

## Big prints this scan (74)
- **SPY** CALL 745 2026-11-16 (3DTE): 1,924 @ 8.44 = **+$1.6M** SELL | vol 52,002 / OI 981
- **AVGO** PUT 340 2026-11-20 (7DTE): 312 @ 9.33 = **+$291k** BUY | vol 3,875 / OI 15,339
- **QQQ** CALL 678 2026-11-18 (5DTE): 250 @ 8.87 = **+$222k** SELL | vol 2,476 / OI 516
- **TSLA** CALL 400 2026-11-20 (7DTE): 300 @ 6.55 = **+$196k** SELL | vol 12,743 / OI 21,808
- **TSLA** CALL 397.5 2026-11-20 (7DTE): 260 @ 7.40 = **+$192k** SELL | vol 9,086 / OI 0
- **AVGO** PUT 330 2026-11-20 (7DTE): 312 @ 5.83 = **+$182k** BUY | vol 4,396 / OI 10,919
- **GOOGL** PUT 290 2026-11-20 (7DTE): 500 @ 3.55 = **+$178k** BUY | vol 2,505 / OI 18,375
- **SPY** CALL 745 2026-11-13 (0DTE): 200 @ 7.49 = **+$150k** SELL | vol 8,818 / OI 3,254
- **TSLA** CALL 397.5 2026-11-20 (7DTE): 200 @ 7.39 = **+$148k** SELL | vol 9,086 / OI 0
- **TSLA** CALL 397.5 2026-11-20 (7DTE): 200 @ 7.39 = **+$148k** SELL | vol 9,086 / OI 0
- **TSLA** CALL 397.5 2026-11-20 (7DTE): 200 @ 7.39 = **+$148k** SELL | vol 9,086 / OI 0
- **TSLA** CALL 397.5 2026-11-20 (7DTE): 200 @ 7.38 = **+$148k** SELL | vol 9,086 / OI 0
- **TSLA** CALL 397.5 2026-11-20 (7DTE): 200 @ 7.30 = **+$146k** SELL | vol 9,086 / OI 0
- **AAPL** PUT 355 2026-11-20 (7DTE): 400 @ 3.03 = **+$121k** BUY | vol 8,788 / OI 3,032
- **AMD** PUT 535 2026-11-20 (7DTE): 40 @ 28.40 = **+$114k** BUY | vol 799 / OI 1,259

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 725 2026-11-16 (3DTE): 2,748 traded vs OI 1,667
- **SPY** PUT 716 2026-11-16 (3DTE): 1,353 traded vs OI 1,257
- **QQQ** PUT 661 2026-11-20 (7DTE): 545 traded vs OI 451
- **AAPL** CALL 362.5 2026-11-27 (14DTE): 500 traded vs OI 195
- **AMD** CALL 485 2026-11-13 (0DTE): 1,539 traded vs OI 0
- **AMD** CALL 562.5 2026-11-16 (3DTE): 506 traded vs OI 62
- **META** CALL 705 2026-11-20 (7DTE): 795 traded vs OI 0
- **AMZN** CALL 287.5 2026-11-27 (14DTE): 510 traded vs OI 225
- **AVGO** CALL 342.5 2026-11-16 (3DTE): 519 traded vs OI 103
- **AVGO** CALL 320 2026-11-13 (0DTE): 2,108 traded vs OI 0
- **AVGO** CALL 312.5 2026-11-13 (0DTE): 2,065 traded vs OI 0
- **DELL** CALL 340 2026-11-20 (7DTE): 507 traded vs OI 201
- **SMCI** CALL 29 2026-11-27 (14DTE): 639 traded vs OI 371
- **SMCI** CALL 28 2026-11-13 (0DTE): 3,255 traded vs OI 3,167
- **MSTR** PUT 105 2026-12-04 (21DTE): 538 traded vs OI 471

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
