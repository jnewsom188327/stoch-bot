# GEX + FLOW SCAN - Fri Nov 13, 01:30 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (13)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 12:45 | **HOOD** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/13 78C | 0.58 | 0.59 | +12% (3m) | **+2%** | +75% | 79 |
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
Last 1m check 13:30:08 ET, last candle SPY 13:29, QQQ 13:29 | no errors
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
| 1 | **SMCI** | 26.70 | FLOW SURGE | **PUTS** | 35 | 11/13 27P @ 0.45 (delta 0.71) = est +35% at 26.35 | NEG -$3.1M | 28 | 27 | 27 | -$1.7M | +$0 bull / -$808k bear | out (clean 34, ADX 22, RVol 0.4) |
| 2 | **GOOGL** | 295.56 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 33 | none: 94 puts 0-7DTE > 7 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only -17% at the target (needs +20%) (43 contracts' greeks worked out here) | POS +$207.9M | 291.15 | 295 | 290 | +$20.1M | - | out (clean 31, ADX 12, RVol 0.5) |
| 3 | **TSLA** | 390.83 | PINNED between the walls (positive gamma) - chop | **-** | 29 | - | POS +$360.0M | 384 | 390 | 390 | +$44.0M | +$381k bull / -$188k bear | out (clean 28, ADX 9, RVol 0.5) |
| 4 | **MU** | 763.23 | FLIP CROSS down into negative gamma | **PUTS** | 29 | none: 164 puts 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (76 contracts' greeks worked out here) | NEG -$46.3M | 776.19 | 760 | 750 | +$75.8M | +$794k bull / -$1.6M bear | out (clean 30, ADX 14, RVol 0.3) |
| 5 | **AVGO** | 345.54 | - | **-** | 23 | - | POS +$77.3M | 338.97 | 350 | 340 | +$18.3M | +$221k bull / -$307k bear | out (clean 35, ADX 20, RVol 0.3) |
| 6 | **COIN** | 128.96 | - | **-** | 22 | - | NEG -$21.4M | 132.53 | 140 | 130 | +$2.9M | +$0 bull / -$545k bear | out (clean 31, ADX 15, RVol 0.5) |
| 7 | **AMD** | 526.53 | - | **-** | 20 | - | POS +$23.7M | 517.63 | 530 | 530 | +$70.0M | +$0 bull / -$2.0M bear | out (clean 35, ADX 25, RVol 0.2) |
| 8 | **QQQ** | 677.82 | - | **-** | 19 | - | NEG -$3.1B | 689.34 | 680 | 680 | +$247.9M | +$113k bull / -$1.8M bear | out (clean 32, ADX 18, RVol 0.2) |
| 9 | **IWM** | 276.90 | - | **-** | 19 | - | NEG -$2.6B | 282.42 | 285 | 275 | +$16.9M | +$0 bull / -$101k bear | out (clean 36, ADX 17, RVol 0.3) |
| 10 | **SMH** | 482.65 | - | **-** | 19 | - | NEG -$341.7M | - | 500 | 475 | +$9.6M | +$0 bull / -$267k bear | out (clean 31, ADX 18, RVol 0.2) |
| 11 | **NFLX** | 62.43 | - | **-** | 19 | - | NEG -$38.0M | 63.51 | 65 | 62 | +$434k | +$0 bull / -$27k bear | out (clean 31, ADX 26, RVol 0.7) |
| 12 | **DELL** | 342.92 | - | **-** | 19 | - | NEG -$10.7M | - | 350 | 340 | +$4.0M | +$0 bull / -$88k bear | out (clean 38, ADX 22, RVol 0.9) |
| 13 | **NVDA** | 161.34 | - | **-** | 18 | - | NEG -$303.5M | - | 175 | 160 | +$98.9M | +$475k bull / -$1.3M bear | out (clean 31, ADX 8, RVol 0.3) |
| 14 | **AAPL** | 357.98 | - | **-** | 18 | - | POS +$1.3B | 348.69 | 360 | 360 | +$10.8M | +$0 bull / -$1.4M bear | out (clean 30, ADX 12, RVol 1.1) |
| 15 | **SPY** | 752.26 | - | **-** | 17 | - | NEG -$8.5B | 760.45 | 750 | 755 | +$228.6M | +$1.6M bull / -$3.8M bear | out (clean 33, ADX 15, RVol 0.3) |
| 16 | **META** | 637.75 | - | **-** | 17 | - | POS +$82.0M | 633.95 | 650 | 635 | +$4.8M | +$814k bull / -$363k bear | out (clean 29, ADX 24, RVol 0.6) |
| 17 | **ORCL** | 124.43 | - | **-** | 16 | - | POS +$6.3M | 123.33 | 125 | 125 | -$1.4M | +$256k bull / +$0 bear | out (clean 31, ADX 13, RVol 0.5) |
| 18 | **PLTR** | 168.18 | - | **-** | 15 | - | POS +$75.4M | 165.99 | 167.5 | 170 | +$1.4M | +$0 bull / -$108k bear | out (clean 28, ADX 12, RVol 0.5) |
| 19 | **MSTR** | 111.28 | - | **-** | 15 | - | NEG -$44.0M | - | 110 | 110 | +$457k | +$0 bull / -$88k bear | out (clean 30, ADX 23, RVol 0.3) |
| 20 | **ARM** | 189.25 | - | **-** | 14 | - | NEG -$2.2M | 190.99 | 190 | 190 | -$3.4M | - | out (clean 33, ADX 24, RVol 0.2) |
| 21 | **UBER** | 69.29 | - | **-** | 13 | - | POS +$8.6M | 68.97 | 70 | 70 | +$346k | - | out (clean 33, ADX 17, RVol 0.3) |
| 22 | **AMZN** | 265.67 | - | **-** | 11 | - | POS +$423.0M | 253.01 | 265 | 265 | +$8.9M | - | out (clean 30, ADX 17, RVol 0.3) |
| 23 | **HOOD** | 78.42 | - | **-** | 11 | - | NEG -$15.5M | 80.36 | 81 | 80 | +$2.5M | - | out (clean 36, ADX 21, RVol 0.6) |
| 24 | **CRM** | 217.26 | - | **-** | 11 | - | NEG -$3.4M | 218.37 | 220 | 220 | +$131k | - | out (clean 27, ADX 20, RVol 0.7) |
| 25 | **SHOP** | 147.35 | - | **-** | 3 | - | POS +$2.7M | 146.52 | 150 | 140 | +$12k | - | out (clean 31, ADX 12, RVol 0.2) |
| 26 | **BABA** | 93.97 | - | **-** | 3 | - | NEG -$18.6M | - | 100 | 95 | -$12k | - | out (clean 27, ADX 14, RVol 0.1) |
| 27 | **MSFT** | 524.65 | - | **-** | 2 | - | POS +$118.1M | 523.04 | 535 | 520 | -$606k | - | out (clean 31, ADX 8, RVol 0.3) |

## Big prints this scan (45)
- **NVDA** CALL 160 2026-11-16 (3DTE): 2,774 @ 3.90 = **+$1.1M** SELL | vol 55,719 / OI 919
- **SMCI** CALL 28 2026-11-20 (7DTE): 11,226 @ 0.72 = **+$808k** SELL | vol 22,656 / OI 1,125
- **SPY** CALL 745 2026-11-16 (3DTE): 500 @ 7.94 = **+$397k** SELL | vol 43,847 / OI 981
- **SPY** CALL 745 2026-11-16 (3DTE): 500 @ 7.94 = **+$397k** SELL | vol 43,847 / OI 981
- **AMD** PUT 540 2026-11-18 (5DTE): 130 @ 29.87 = **+$388k** BUY | vol 770 / OI 40
- **MU** PUT 760 2026-11-18 (5DTE): 135 @ 26.60 = **+$359k** BUY | vol 1,221 / OI 117
- **SPY** CALL 745 2026-11-16 (3DTE): 380 @ 7.94 = **+$302k** SELL | vol 43,847 / OI 981
- **MU** PUT 760 2026-11-18 (5DTE): 90 @ 26.80 = **+$241k** BUY | vol 1,221 / OI 117
- **AMD** PUT 545 2026-11-18 (5DTE): 70 @ 32.94 = **+$231k** BUY | vol 241 / OI 14
- **MU** PUT 760 2026-11-18 (5DTE): 78 @ 26.80 = **+$209k** BUY | vol 1,221 / OI 117
- **QQQ** CALL 678 2026-11-18 (5DTE): 256 @ 8.15 = **+$209k** SELL | vol 1,943 / OI 516
- **AMD** PUT 545 2026-11-18 (5DTE): 60 @ 32.95 = **+$198k** BUY | vol 241 / OI 14
- **QQQ** CALL 678 2026-11-18 (5DTE): 234 @ 8.15 = **+$191k** SELL | vol 1,943 / OI 516
- **AMD** PUT 542.5 2026-11-13 (0DTE): 90 @ 19.52 = **+$176k** BUY | vol 3,535 / OI 253
- **QQQ** CALL 678 2026-11-18 (5DTE): 213 @ 8.15 = **+$174k** SELL | vol 1,943 / OI 516

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 711 2026-11-17 (4DTE): 583 traded vs OI 183
- **QQQ** PUT 662 2026-11-20 (7DTE): 864 traded vs OI 863
- **IWM** PUT 280 2026-11-17 (4DTE): 866 traded vs OI 426
- **SMH** CALL 490 2026-11-16 (3DTE): 523 traded vs OI 84
- **NVDA** PUT 157.5 2026-11-18 (5DTE): 2,963 traded vs OI 2,960
- **MSTR** CALL 122 2026-11-13 (0DTE): 649 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
