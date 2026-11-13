# GEX + FLOW SCAN - Fri Nov 13, 12:40 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (12)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
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
Last 1m check 12:40:08 ET, last candle SPY 12:39, QQQ 12:39 | no errors
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
| 1 | **TSLA** | 389.08 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 36 | none: 124 calls 0-7DTE > 6 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only -31% at the target (needs +20%) (52 contracts' greeks worked out here) | POS +$351.4M | - | 400 | 390 | +$49.5M | +$681k bull / +$0 bear | out (clean 29, ADX 13, RVol 0.6) |
| 2 | **AMZN** | 265.34 | PINNED between the walls (positive gamma) - chop | **-** | 36 | - | POS +$434.2M | 249.48 | 265 | 265 | +$8.4M | +$0 bull / -$34k bear | out (clean 30, ADX 24, RVol 0.5) |
| 3 | **GOOGL** | 295.03 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 35 | none: 90 puts 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (43 contracts' greeks worked out here) | POS +$197.3M | 289.82 | 295 | 290 | +$19.1M | - | out (clean 31, ADX 20, RVol 0.6) |
| 4 | **META** | 634.30 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 33 | none: 189 calls 0-7DTE > 9 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (90 contracts' greeks worked out here) | POS +$41.5M | 632.12 | 630 | 635 | +$4.2M | +$32k bull / -$25k bear | out (clean 29, ADX 24, RVol 0.4) |
| 5 | **MU** | 762.13 | FLIP CROSS down into negative gamma | **PUTS** | 32 | none: 164 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (78 contracts' greeks worked out here) | NEG -$17.0M | 769.42 | 760 | 750 | +$67.8M | +$167k bull / -$1.6M bear | out (clean 30, ADX 21, RVol 0.5) |
| 6 | **ORCL** | 124.27 | FLIP CROSS down into negative gamma | **PUTS** | 29 | 11/13 124P @ 0.69 (delta 0.44) = est +72% at 122.97 | NEG -$1.8M | 124.43 | 125 | 125 | -$1.1M | +$0 bull / -$31k bear | out (clean 31, ADX 19, RVol 0.4) |
| 7 | **COIN** | 128.14 | - | **-** | 27 | - | NEG -$23.0M | 132.92 | 140 | 130 | +$3.6M | +$0 bull / -$723k bear | out (clean 31, ADX 22, RVol 0.3) |
| 8 | **AVGO** | 344.88 | - | **-** | 26 | - | POS +$79.5M | 335.19 | 350 | 340 | +$19.4M | +$99k bull / -$119k bear | out (clean 36, ADX 29, RVol 0.4) |
| 9 | **AMD** | 522.94 | - | **-** | 23 | - | POS +$30.4M | - | 530 | 530 | +$64.4M | +$680k bull / -$2.3M bear | out (clean 35, ADX 36, RVol 0.7) |
| 10 | **QQQ** | 676.71 | - | **-** | 22 | - | NEG -$3.1B | 689.92 | 680 | 680 | +$257.5M | +$1.3M bull / -$900k bear | out (clean 32, ADX 29, RVol 0.5) |
| 11 | **IWM** | 276.61 | - | **-** | 22 | - | NEG -$2.6B | 282.72 | 285 | 275 | +$19.0M | +$0 bull / -$53k bear | out (clean 36, ADX 21, RVol 0.5) |
| 12 | **SMH** | 481.48 | - | **-** | 22 | - | NEG -$348.3M | - | 500 | 475 | +$10.1M | +$0 bull / -$495k bear | out (clean 31, ADX 30, RVol 0.3) |
| 13 | **NVDA** | 160.63 | - | **-** | 20 | - | NEG -$297.7M | - | 175 | 160 | +$100.7M | +$573k bull / -$4.9M bear | out (clean 31, ADX 13, RVol 0.5) |
| 14 | **NFLX** | 62.49 | - | **-** | 20 | - | NEG -$39.1M | 63.54 | 65 | 62 | +$473k | +$0 bull / -$26k bear | out (clean 32, ADX 34, RVol 0.6) |
| 15 | **PLTR** | 167.79 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 20 | 11/13 167.5P @ 0.73 (delta 0.44) = est +235% at 165 | POS +$106.0M | 160.26 | 167.5 | 165 | -$524k | - | out (clean 29, ADX 18, RVol 0.2) |
| 16 | **SPY** | 751.29 | - | **-** | 19 | - | NEG -$7.7B | 758.62 | 750 | 750 | +$238.1M | +$0 bull / -$4.3M bear | out (clean 33, ADX 21, RVol 0.5) |
| 17 | **AAPL** | 357.84 | - | **-** | 18 | - | POS +$1.3B | 347.3 | 360 | 360 | +$12.8M | +$504k bull / -$120k bear | out (clean 30, ADX 14, RVol 0.5) |
| 18 | **ARM** | 188.03 | - | **-** | 18 | - | NEG -$2.0M | 190.15 | 190 | 190 | -$3.4M | - | out (clean 33, ADX 33, RVol 0.7) |
| 19 | **DELL** | 340.38 | - | **-** | 16 | - | NEG -$10.6M | - | 350 | 340 | +$6.8M | - | out (clean 38, ADX 37, RVol 1.0) |
| 20 | **MSTR** | 110.36 | - | **-** | 16 | - | NEG -$46.6M | - | 110 | 110 | +$540k | +$0 bull / -$1.3M bear | out (clean 30, ADX 20, RVol 0.9) |
| 21 | **HOOD** | 77.80 | - | **-** | 15 | - | NEG -$14.4M | 80.02 | 78 | 80 | +$2.8M | - | out (clean 36, ADX 30, RVol 1.3) |
| 22 | **MSFT** | 523.60 | - | **-** | 13 | - | POS +$106.9M | 521.88 | 535 | 520 | -$158k | +$256k bull / +$0 bear | out (clean 31, ADX 12, RVol 0.3) |
| 23 | **UBER** | 69.50 | - | **-** | 13 | - | POS +$15.4M | 68.96 | 70 | 70 | +$310k | - | out (clean 33, ADX 12, RVol 0.3) |
| 24 | **CRM** | 217.78 | - | **-** | 12 | - | NEG -$6.7M | 222.47 | 220 | 220 | +$116k | - | out (clean 28, ADX 23, RVol 0.8) |
| 25 | **SMCI** | 26.39 | - | **-** | 7 | - | NEG -$2.9M | 27.71 | 27 | 27 | +$144k | - | out (clean 34, ADX 21, RVol 0.6) |
| 26 | **SHOP** | 146.82 | - | **-** | 4 | - | POS +$4.1M | 145.07 | 150 | 140 | +$28k | - | out (clean 31, ADX 15, RVol 0.3) |
| 27 | **BABA** | 94.12 | - | **-** | 4 | - | NEG -$20.6M | - | 100 | 95 | -$21k | - | out (clean 27, ADX 18, RVol 0.3) |

## Big prints this scan (76)
- **SPY** CALL 745 2026-11-16 (3DTE): 1,507 @ 7.59 = **+$1.1M** SELL | vol 19,332 / OI 981
- **NVDA** CALL 160 2026-11-16 (3DTE): 1,275 @ 3.90 = **+$497k** MID | vol 43,874 / OI 919
- **SPY** CALL 751 2026-11-13 (0DTE): 1,000 @ 1.43 = **+$143k** SELL | vol 209,773 / OI 2,050
- **SPY** CALL 751 2026-11-13 (0DTE): 1,000 @ 1.41 = **+$141k** SELL | vol 209,773 / OI 2,050
- **SMH** PUT 500 2026-11-18 (5DTE): 34 @ 24.00 = **+$82k** BUY | vol 146 / OI 65
- **MU** PUT 775 2026-11-16 (3DTE): 30 @ 26.30 = **+$79k** BUY | vol 1,027 / OI 70
- **NVDA** CALL 160 2026-11-16 (3DTE): 186 @ 3.80 = **+$71k** SELL | vol 43,874 / OI 919
- **NVDA** CALL 160 2026-11-16 (3DTE): 186 @ 3.80 = **+$71k** SELL | vol 43,874 / OI 919
- **NVDA** CALL 160 2026-11-16 (3DTE): 186 @ 3.80 = **+$71k** SELL | vol 43,874 / OI 919
- **NVDA** CALL 160 2026-11-16 (3DTE): 185 @ 3.80 = **+$70k** SELL | vol 43,874 / OI 919
- **AMD** CALL 510 2026-11-18 (5DTE): 25 @ 28.04 = **+$70k** MID | vol 64 / OI 188
- **NVDA** CALL 162.5 2026-11-18 (5DTE): 100 @ 7.00 = **+$70k** BUY | vol 3,681 / OI 126
- **NVDA** CALL 160 2026-11-16 (3DTE): 160 @ 3.90 = **+$62k** MID | vol 43,874 / OI 919
- **NVDA** CALL 160 2026-11-16 (3DTE): 157 @ 3.85 = **+$60k** SELL | vol 43,874 / OI 919
- **AAPL** PUT 357.5 2026-11-16 (3DTE): 300 @ 2.00 = **+$60k** BUY | vol 9,096 / OI 49

## New unusual volume (traded more than open interest, 500+)
- **QQQ** CALL 696 2026-11-30 (17DTE): 611 traded vs OI 267
- **SMH** CALL 520 2026-12-04 (21DTE): 5,313 traded vs OI 368
- **SMH** CALL 485 2026-11-16 (3DTE): 500 traded vs OI 211
- **TSLA** CALL 417.5 2026-11-18 (5DTE): 502 traded vs OI 137
- **AMD** PUT 522.5 2026-11-16 (3DTE): 502 traded vs OI 52
- **AMD** CALL 520 2026-11-16 (3DTE): 503 traded vs OI 79
- **META** CALL 697.5 2026-11-20 (7DTE): 1,245 traded vs OI 0
- **META** CALL 697.5 2026-11-13 (0DTE): 608 traded vs OI 0
- **META** PUT 620 2026-11-16 (3DTE): 504 traded vs OI 379
- **NFLX** PUT 58 2026-11-20 (7DTE): 618 traded vs OI 614
- **AVGO** CALL 345 2026-11-16 (3DTE): 589 traded vs OI 339
- **DELL** PUT 325 2026-11-20 (7DTE): 704 traded vs OI 0
- **MU** PUT 690 2026-11-13 (0DTE): 511 traded vs OI 0
- **MU** CALL 747.5 2026-11-13 (0DTE): 522 traded vs OI 112

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
