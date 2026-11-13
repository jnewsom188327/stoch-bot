# GEX + FLOW SCAN - Fri Nov 13, 01:40 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (13)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 12:45 | **HOOD** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/13 78C | 0.58 | 0.45 | +12% (3m) | **-22%** | +75% | 79 |
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
Last 1m check 13:40:08 ET, last candle SPY 13:39, QQQ 13:39 | no errors
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
| 1 | **GOOGL** | 295.61 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 43 | none: 94 puts 0-7DTE > 7 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only -14% at the target (needs +20%) (42 contracts' greeks worked out here) | POS +$215.8M | 289.9 | 295 | 290 | +$19.9M | +$0 bull / -$38k bear | out (clean 31, ADX 12, RVol 0.5) |
| 2 | **SMCI** | 26.70 | FLOW SURGE | **PUTS** | 36 | 11/13 27P @ 0.41 (delta 0.74) = est +48% at 26.36 | NEG -$2.9M | 27.71 | 27 | 27 | -$1.7M | +$0 bull / -$808k bear | out (clean 34, ADX 24, RVol 0.4) |
| 3 | **MU** | 764.10 | FLIP CROSS up into positive gamma | **CALLS** | 29 | none: 164 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (85 contracts' greeks worked out here) | POS +$15.3M | 759.56 | 760 | 770 | +$73.5M | +$160k bull / -$3.0M bear | out (clean 30, ADX 14, RVol 0.2) |
| 4 | **ORCL** | 124.58 | FLIP CROSS up into positive gamma | **CALLS** | 29 | none: 50 calls 0-7DTE > 2 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only -20% at the target (needs +20%) (42 contracts' greeks worked out here) | POS +$4.4M | 122.78 | 125 | 125 | -$1.6M | +$0 bull / -$32k bear | out (clean 31, ADX 13, RVol 0.4) |
| 5 | **TSLA** | 390.68 | PINNED between the walls (positive gamma) - chop | **-** | 28 | - | POS +$396.0M | - | 390 | 390 | +$41.8M | +$0 bull / -$1.0M bear | out (clean 28, ADX 9, RVol 0.4) |
| 6 | **ARM** | 189.53 | - | **-** | 24 | - | NEG -$2.5M | 191.28 | 190 | 190 | -$3.4M | +$0 bull / -$30k bear | out (clean 33, ADX 21, RVol 0.2) |
| 7 | **AMZN** | 265.63 | PINNED between the walls (positive gamma) - chop | **-** | 22 | - | POS +$449.7M | 250.9 | 265 | 265 | +$8.4M | - | out (clean 30, ADX 17, RVol 0.3) |
| 8 | **AVGO** | 346.44 | - | **-** | 22 | - | POS +$99.9M | - | 350 | 350 | +$17.6M | +$0 bull / -$433k bear | out (clean 35, ADX 19, RVol 0.3) |
| 9 | **COIN** | 128.88 | - | **-** | 22 | - | NEG -$20.9M | 132.14 | 140 | 130 | +$2.8M | +$0 bull / -$29k bear | out (clean 31, ADX 15, RVol 0.6) |
| 10 | **AMD** | 527.89 | - | **-** | 20 | - | POS +$50.0M | - | 530 | 530 | +$67.9M | +$0 bull / -$2.1M bear | out (clean 35, ADX 24, RVol 0.2) |
| 11 | **QQQ** | 678.00 | - | **-** | 19 | - | NEG -$2.6B | 685.15 | 680 | 680 | +$241.9M | +$0 bull / -$1.7M bear | out (clean 32, ADX 18, RVol 0.3) |
| 12 | **IWM** | 276.87 | - | **-** | 19 | - | NEG -$2.5B | 282.2 | 285 | 275 | +$16.7M | +$0 bull / -$101k bear | out (clean 36, ADX 17, RVol 0.3) |
| 13 | **SMH** | 483.52 | - | **-** | 19 | - | NEG -$319.4M | - | 500 | 475 | +$9.2M | +$0 bull / -$270k bear | out (clean 31, ADX 18, RVol 0.2) |
| 14 | **NVDA** | 161.90 | - | **-** | 18 | - | NEG -$253.9M | - | 175 | 160 | +$98.1M | +$187k bull / -$7.8M bear | out (clean 31, ADX 10, RVol 0.3) |
| 15 | **NFLX** | 62.45 | - | **-** | 18 | - | NEG -$38.3M | 63.34 | 65 | 62 | +$406k | +$0 bull / -$27k bear | out (clean 31, ADX 23, RVol 0.7) |
| 16 | **DELL** | 343.44 | - | **-** | 18 | - | NEG -$12.7M | - | 350 | 340 | +$3.7M | +$0 bull / -$92k bear | out (clean 38, ADX 22, RVol 0.4) |
| 17 | **SPY** | 752.48 | - | **-** | 17 | - | NEG -$7.4B | 758.25 | 750 | 755 | +$219.4M | +$0 bull / -$1.4M bear | out (clean 33, ADX 16, RVol 0.3) |
| 18 | **AAPL** | 358.04 | - | **-** | 17 | - | POS +$1.3B | 347.36 | 360 | 360 | +$11.2M | +$0 bull / -$133k bear | out (clean 30, ADX 12, RVol 0.8) |
| 19 | **META** | 637.89 | - | **-** | 16 | - | POS +$79.4M | 634.52 | 650 | 635 | +$3.5M | +$165k bull / -$600k bear | out (clean 29, ADX 25, RVol 0.6) |
| 20 | **PLTR** | 168.46 | - | **-** | 15 | - | POS +$92.3M | 162.91 | 170 | 170 | +$1.3M | +$0 bull / -$108k bear | out (clean 28, ADX 13, RVol 0.5) |
| 21 | **MSTR** | 111.39 | - | **-** | 15 | - | NEG -$38.6M | - | 110 | 110 | -$388k | +$0 bull / -$2.0M bear | out (clean 30, ADX 26, RVol 0.3) |
| 22 | **UBER** | 69.34 | - | **-** | 13 | - | POS +$8.9M | 69.04 | 70 | 70 | +$328k | - | out (clean 33, ADX 18, RVol 0.2) |
| 23 | **HOOD** | 78.27 | - | **-** | 11 | - | NEG -$12.3M | 79.47 | 78 | 79 | +$2.5M | - | out (clean 36, ADX 20, RVol 0.6) |
| 24 | **CRM** | 217.80 | - | **-** | 11 | - | NEG -$4.1M | 221.5 | 220 | 220 | +$129k | - | out (clean 27, ADX 20, RVol 0.7) |
| 25 | **SHOP** | 147.59 | - | **-** | 3 | - | POS +$4.1M | 146.42 | 150 | 140 | +$12k | - | out (clean 31, ADX 13, RVol 0.3) |
| 26 | **BABA** | 94.07 | - | **-** | 3 | - | NEG -$20.6M | - | 100 | 95 | -$12k | - | out (clean 27, ADX 13, RVol 0.1) |
| 27 | **MSFT** | 523.82 | - | **-** | 2 | - | POS +$100.2M | 522.35 | 535 | 520 | -$43k | - | out (clean 31, ADX 7, RVol 0.3) |

## Big prints this scan (63)
- **NVDA** PUT 160 2026-11-18 (5DTE): 1,887 @ 7.00 = **+$1.3M** BUY | vol 12,981 / OI 5,421
- **NVDA** PUT 160 2026-11-18 (5DTE): 1,000 @ 7.05 = **+$705k** BUY | vol 12,981 / OI 5,421
- **TSLA** CALL 395 2026-11-20 (7DTE): 383 @ 8.50 = **+$326k** SELL | vol 7,865 / OI 2,968
- **MU** CALL 765 2026-11-18 (5DTE): 100 @ 25.90 = **+$259k** SELL | vol 695 / OI 337
- **TSLA** CALL 395 2026-11-20 (7DTE): 293 @ 8.50 = **+$249k** SELL | vol 7,865 / OI 2,968
- **MU** CALL 765 2026-11-18 (5DTE): 95 @ 25.85 = **+$246k** SELL | vol 695 / OI 337
- **NVDA** PUT 160 2026-11-18 (5DTE): 294 @ 7.05 = **+$207k** BUY | vol 12,981 / OI 5,421
- **NVDA** PUT 160 2026-11-18 (5DTE): 240 @ 7.00 = **+$168k** BUY | vol 12,981 / OI 5,421
- **AVGO** CALL 345 2026-11-16 (3DTE): 280 @ 6.00 = **+$168k** SELL | vol 1,179 / OI 339
- **MSTR** PUT 107 2026-11-20 (7DTE): 500 @ 3.19 = **+$160k** BUY | vol 617 / OI 0
- **MU** CALL 730 2026-11-16 (3DTE): 43 @ 37.00 = **+$159k** SELL | vol 85 / OI 266
- **NVDA** PUT 162.5 2026-11-20 (7DTE): 130 @ 9.20 = **+$120k** BUY | vol 4,847 / OI 505
- **NVDA** PUT 160 2026-11-18 (5DTE): 152 @ 7.00 = **+$106k** BUY | vol 12,981 / OI 5,421
- **QQQ** PUT 687 2026-11-13 (0DTE): 95 @ 10.69 = **+$102k** BUY | vol 20,894 / OI 1,621
- **NVDA** PUT 155 2026-11-20 (7DTE): 178 @ 5.65 = **+$101k** BUY | vol 14,284 / OI 14,723

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 773 2026-11-17 (4DTE): 542 traded vs OI 381
- **SPY** PUT 747 2026-11-18 (5DTE): 610 traded vs OI 607
- **SPY** PUT 732 2026-11-17 (4DTE): 673 traded vs OI 239
- **SPY** CALL 820 2026-11-24 (11DTE): 1,000 traded vs OI 19
- **SPY** CALL 825 2026-11-24 (11DTE): 800 traded vs OI 0
- **SPY** CALL 755 2026-12-04 (21DTE): 968 traded vs OI 957
- **QQQ** PUT 668 2026-11-17 (4DTE): 507 traded vs OI 239
- **QQQ** CALL 710 2026-11-23 (10DTE): 510 traded vs OI 456
- **QQQ** CALL 690 2026-11-25 (12DTE): 503 traded vs OI 50
- **SMH** PUT 495 2026-11-13 (0DTE): 500 traded vs OI 333
- **SMH** CALL 482.5 2026-11-13 (0DTE): 501 traded vs OI 282
- **TSLA** CALL 365 2026-11-16 (3DTE): 502 traded vs OI 184
- **TSLA** CALL 360 2026-11-16 (3DTE): 547 traded vs OI 185
- **AMD** CALL 522.5 2026-11-16 (3DTE): 520 traded vs OI 61
- **AMD** PUT 532.5 2026-11-16 (3DTE): 513 traded vs OI 83

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
