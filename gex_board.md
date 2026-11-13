# GEX + FLOW SCAN - Fri Nov 13, 01:00 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (13)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 12:45 | **HOOD** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/13 78C | 0.58 | 0.43 | +12% (3m) | **-26%** | +75% | 79 |
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
Last 1m check 13:00:08 ET, last candle SPY 12:59, QQQ 12:59 | no errors
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
| 1 | **HOOD** | 78.12 | RUN: clean trend + negative gamma + flow agrees | **CALLS** | 53 | 11/13 78C @ 0.46 (delta 0.56) = est +109% at 79 | NEG -$15.3M | 80.15 | 78 | 80 | +$2.6M | +$0 bull / -$540k bear | LONG (clean 36, ADX 25, RVol 1.3) |
| 2 | **GOOGL** | 295.51 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 43 | none: 94 puts 0-7DTE > 7 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only -22% at the target (needs +20%) (35 contracts' greeks worked out here) | POS +$186.6M | 292.92 | 295 | 290 | +$18.9M | +$0 bull / -$52k bear | out (clean 31, ADX 16, RVol 0.5) |
| 3 | **TSLA** | 390.55 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 34 | none: 124 calls 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (54 contracts' greeks worked out here) | POS +$378.6M | - | 400 | 390 | +$45.1M | +$0 bull / -$3.4M bear | out (clean 28, ADX 12, RVol 0.4) |
| 4 | **AMZN** | 265.60 | PINNED between the walls (positive gamma) - chop | **-** | 32 | - | POS +$388.0M | 251.81 | 265 | 265 | +$7.9M | +$100k bull / -$103k bear | out (clean 30, ADX 22, RVol 0.2) |
| 5 | **PLTR** | 167.88 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 31 | none: 26 puts 0-7DTE > 1 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only -15% at the target (needs +20%) (21 contracts' greeks worked out here) | POS +$107.4M | 160.38 | 167.5 | 170 | +$1.3M | +$0 bull / -$51k bear | out (clean 28, ADX 15, RVol 0.2) |
| 6 | **AVGO** | 345.06 | - | **-** | 25 | - | POS +$82.8M | - | 350 | 340 | +$19.0M | +$1.1M bull / -$110k bear | out (clean 36, ADX 26, RVol 0.3) |
| 7 | **DELL** | 338.70 | - | **-** | 25 | - | NEG -$11.0M | - | 337.5 | 340 | +$7.4M | +$31k bull / +$0 bear | out (clean 38, ADX 29, RVol 1.0) |
| 8 | **AMD** | 523.38 | - | **-** | 22 | - | POS +$28.5M | - | 530 | 530 | +$72.3M | +$2.2M bull / -$232k bear | out (clean 35, ADX 30, RVol 0.6) |
| 9 | **QQQ** | 677.06 | - | **-** | 21 | - | NEG -$3.1B | 690.14 | 680 | 680 | +$256.8M | +$392k bull / -$797k bear | out (clean 32, ADX 25, RVol 0.4) |
| 10 | **SMH** | 481.57 | - | **-** | 21 | - | NEG -$346.1M | - | 500 | 475 | +$10.3M | +$32k bull / -$25k bear | out (clean 31, ADX 26, RVol 0.4) |
| 11 | **SPY** | 751.77 | - | **-** | 19 | - | NEG -$8.7B | 760.45 | 750 | 750 | +$237.8M | +$2.9M bull / -$4.0M bear | out (clean 33, ADX 20, RVol 0.5) |
| 12 | **NVDA** | 161.03 | - | **-** | 19 | - | NEG -$323.4M | - | 175 | 160 | +$105.4M | +$1.0M bull / -$492k bear | out (clean 31, ADX 10, RVol 0.4) |
| 13 | **MU** | 763.33 | - | **-** | 19 | - | NEG -$29.9M | 776.33 | 760 | 750 | +$68.5M | +$842k bull / -$2.7M bear | out (clean 30, ADX 20, RVol 0.4) |
| 14 | **AAPL** | 357.97 | - | **-** | 17 | - | POS +$1.3B | 347.41 | 360 | 360 | +$11.7M | +$198k bull / -$901k bear | out (clean 30, ADX 13, RVol 0.4) |
| 15 | **META** | 637.80 | - | **-** | 17 | - | POS +$90.7M | 631.28 | 650 | 635 | +$585k | +$0 bull / -$261k bear | out (clean 29, ADX 28, RVol 1.1) |
| 16 | **ARM** | 188.14 | - | **-** | 16 | - | NEG -$1.6M | 189.94 | 190 | 190 | -$3.3M | - | out (clean 33, ADX 28, RVol 0.4) |
| 17 | **COIN** | 128.68 | - | **-** | 15 | - | NEG -$19.9M | 132.36 | 140 | 130 | +$3.3M | - | out (clean 31, ADX 20, RVol 0.1) |
| 18 | **MSTR** | 110.52 | - | **-** | 15 | - | NEG -$47.4M | - | 110 | 110 | +$705k | +$36k bull / -$56k bear | out (clean 30, ADX 21, RVol 0.3) |
| 19 | **CRM** | 217.92 | - | **-** | 13 | - | NEG -$5.1M | 221.66 | 220 | 220 | +$110k | - | out (clean 28, ADX 27, RVol 1.3) |
| 20 | **MSFT** | 524.32 | - | **-** | 12 | - | POS +$129.2M | 522.03 | 535 | 520 | -$428k | +$0 bull / -$157k bear | out (clean 31, ADX 9, RVol 0.2) |
| 21 | **UBER** | 69.45 | - | **-** | 12 | - | POS +$13.6M | 68.84 | 70 | 70 | +$306k | - | out (clean 32, ADX 12, RVol 0.3) |
| 22 | **IWM** | 276.56 | - | **-** | 11 | - | NEG -$2.7B | 282.89 | 285 | 275 | +$18.8M | - | out (clean 36, ADX 21, RVol 0.3) |
| 23 | **NFLX** | 62.38 | - | **-** | 10 | - | NEG -$41.5M | 63.38 | 65 | 62 | +$496k | - | out (clean 32, ADX 30, RVol 0.8) |
| 24 | **SMCI** | 26.50 | - | **-** | 7 | - | NEG -$2.8M | 27.83 | 27 | 27 | +$152k | - | out (clean 34, ADX 23, RVol 0.4) |
| 25 | **ORCL** | 124.49 | - | **-** | 6 | - | POS +$764k | 124.35 | 125 | 125 | -$1.1M | - | out (clean 31, ADX 16, RVol 0.3) |
| 26 | **SHOP** | 147.32 | - | **-** | 4 | - | POS +$3.9M | 145.78 | 150 | 140 | +$11k | - | out (clean 31, ADX 14, RVol 0.4) |
| 27 | **BABA** | 94.09 | - | **-** | 4 | - | NEG -$18.2M | - | 100 | 95 | -$46k | - | out (clean 27, ADX 15, RVol 0.2) |

## Big prints this scan (75)
- **SPY** CALL 745 2026-11-16 (3DTE): 2,000 @ 8.43 = **+$1.7M** BUY | vol 31,472 / OI 981
- **SPY** CALL 745 2026-11-16 (3DTE): 788 @ 8.10 = **+$638k** BUY | vol 31,472 / OI 981
- **SPY** CALL 745 2026-11-16 (3DTE): 500 @ 8.09 = **+$404k** BUY | vol 31,472 / OI 981
- **SMH** PUT 500 2026-11-20 (7DTE): 99 @ 26.03 = **+$258k** MID | vol 906 / OI 9,935
- **SPY** CALL 745 2026-11-16 (3DTE): 196 @ 8.09 = **+$159k** BUY | vol 31,472 / OI 981
- **QQQ** PUT 677 2026-11-13 (0DTE): 750 @ 2.09 = **+$157k** BUY | vol 65,562 / OI 2,463
- **AMZN** PUT 257.5 2026-11-20 (7DTE): 592 @ 2.37 = **+$140k** MID | vol 1,515 / OI 1,354
- **NVDA** CALL 160 2026-11-16 (3DTE): 300 @ 4.05 = **+$122k** MID | vol 46,007 / OI 919
- **QQQ** CALL 677 2026-11-16 (3DTE): 200 @ 5.17 = **+$103k** SELL | vol 7,209 / OI 255
- **QQQ** PUT 675 2026-11-16 (3DTE): 200 @ 5.04 = **+$101k** BUY | vol 15,073 / OI 906
- **QQQ** PUT 710 2026-11-16 (3DTE): 30 @ 33.60 = **+$101k** BUY | vol 103 / OI 36
- **AVGO** PUT 342.5 2026-11-20 (7DTE): 73 @ 11.00 = **+$80k** MID | vol 455 / OI 518
- **AMZN** CALL 277.5 2026-11-20 (7DTE): 592 @ 1.24 = **+$73k** SELL | vol 1,336 / OI 1,876
- **MU** PUT 775 2026-11-16 (3DTE): 30 @ 24.20 = **+$73k** BUY | vol 1,111 / OI 70
- **AVGO** CALL 350 2026-11-20 (7DTE): 75 @ 9.45 = **+$71k** SELL | vol 1,221 / OI 7,974

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 744 2026-11-19 (6DTE): 631 traded vs OI 61
- **QQQ** PUT 695 2026-11-16 (3DTE): 505 traded vs OI 490
- **QQQ** CALL 722 2026-11-16 (3DTE): 517 traded vs OI 84
- **QQQ** PUT 660 2026-11-19 (6DTE): 1,257 traded vs OI 413
- **TSLA** PUT 357.5 2026-11-20 (7DTE): 817 traded vs OI 0
- **META** CALL 657.5 2026-11-13 (0DTE): 501 traded vs OI 439
- **PLTR** CALL 177.5 2026-11-20 (7DTE): 5,892 traded vs OI 3,956
- **HOOD** PUT 75 2026-11-13 (0DTE): 1,889 traded vs OI 1,883

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
