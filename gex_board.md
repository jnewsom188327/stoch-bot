# GEX + FLOW SCAN - Fri Nov 13, 12:00 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (12)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:30 | **GOOGL** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/13 292.5P | 0.56 | 0.51 | +23% (10m) | **-9%** | +237% | 290.96 |
| 11:15 | **ARM** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/13 180P | 0.79 | 0.45 | +18% (40m) | **-43%** | +122% | 180 |
| 11:14 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/13 667P | 0.70 | 0.37 | +59% (9m) | **-47%** | +21% | 672.05 hit |
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
Last 1m check 12:00:08 ET, last candle SPY 11:59, QQQ 11:59 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 11:13 | QQQ | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | **FIRE** QQQ261113P00667000 |
| 11:02 | QQQ | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |
| 10:35 | SPY | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | **FIRE** SPY261113P00743000 |
| 10:16 | QQQ | 1m WHIPSAW | R1 R2 | CALLS | TURNING your way | **FIRE** QQQ261113C00683000 |

## Flow surges NOT fired - price disagreed (40 today, last 5)
- 11:45 HOOD CALLS: price -0.30 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 11:40 HOOD CALLS: under EMA 20 - flow says one way, price says the other
- 11:35 HOOD CALLS: under EMA 20 - flow says one way, price says the other
- 11:25 HOOD CALLS: price -0.54 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 11:20 HOOD CALLS: price -0.21 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **AMZN** | 264.57 | PINNED between the walls (positive gamma) - chop | **-** | 41 | - | POS +$368.0M | 253.58 | 265 | 265 | +$9.6M | +$207k bull / +$0 bear | out (clean 30, ADX 34, RVol 0.8) |
| 2 | **GOOGL** | 294.01 | FLOW SURGE | **CALLS** | 39 | none: 94 calls 0-7DTE > 6 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only +20% at the target (needs +20%) (39 contracts' greeks worked out here) | POS +$159.8M | 288.93 | 295 | 290 | +$20.4M | +$66k bull / +$0 bear | out (clean 32, ADX 30, RVol 0.9) |
| 3 | **TSLA** | 390.06 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 37 | none: 124 calls 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (56 contracts' greeks worked out here) | POS +$332.1M | - | 400 | 390 | +$51.4M | +$228k bull / -$435k bear | out (clean 29, ADX 13, RVol 0.6) |
| 4 | **DELL** | 337.58 | - | **-** | 31 | - | NEG -$6.8M | 352.95 | 350 | 340 | +$7.3M | +$0 bull / -$699k bear | out (clean 38, ADX 50, RVol 2.0) |
| 5 | **AVGO** | 343.40 | - | **-** | 29 | - | POS +$68.5M | 334.02 | 340 | 340 | +$20.6M | +$0 bull / -$352k bear | out (clean 36, ADX 37, RVol 0.4) |
| 6 | **HOOD** | 77.40 | - | **-** | 29 | - | NEG -$15.2M | 79.82 | 77 | 80 | +$3.1M | +$145k bull / -$122k bear | out (clean 36, ADX 49, RVol 1.0) |
| 7 | **ARM** | 185.46 | - | **-** | 29 | - | NEG -$3.2M | 190.8 | 185 | 190 | -$1.5M | +$0 bull / -$1.1M bear | out (clean 33, ADX 52, RVol 1.2) |
| 8 | **SMH** | 479.36 | - | **-** | 26 | - | NEG -$367.3M | - | 500 | 475 | +$12.6M | +$107k bull / +$0 bear | out (clean 31, ADX 44, RVol 0.4) |
| 9 | **AMD** | 522.91 | - | **-** | 26 | - | POS +$27.3M | - | 530 | 530 | +$71.8M | +$2.3M bull / -$1.4M bear | out (clean 36, ADX 48, RVol 0.6) |
| 10 | **QQQ** | 675.02 | - | **-** | 25 | - | NEG -$3.1B | 689.53 | 680 | 680 | +$281.6M | +$1.5M bull / -$287k bear | out (clean 32, ADX 42, RVol 0.6) |
| 11 | **MSTR** | 109.19 | - | **-** | 25 | - | NEG -$42.4M | - | 110 | 110 | +$7.3M | +$476k bull / +$0 bear | out (clean 30, ADX 29, RVol 1.0) |
| 12 | **IWM** | 276.25 | - | **-** | 24 | - | NEG -$2.7B | 282.97 | 285 | 275 | +$20.3M | +$51k bull / +$0 bear | out (clean 36, ADX 25, RVol 0.6) |
| 13 | **COIN** | 127.37 | - | **-** | 23 | - | NEG -$21.5M | 132.89 | 140 | 130 | +$3.7M | - | out (clean 30, ADX 35, RVol 1.5) |
| 14 | **NVDA** | 160.24 | - | **-** | 22 | - | NEG -$298.5M | - | 175 | 160 | +$109.0M | +$2.5M bull / -$1.3M bear | out (clean 31, ADX 17, RVol 0.4) |
| 15 | **SPY** | 750.03 | - | **-** | 21 | - | NEG -$9.3B | 760.1 | 750 | 750 | +$271.7M | +$10.6M bull / -$139k bear | out (clean 33, ADX 26, RVol 0.4) |
| 16 | **MU** | 757.99 | - | **-** | 21 | - | NEG -$16.5M | 767.13 | 760 | 750 | +$67.8M | +$2.3M bull / -$710k bear | out (clean 30, ADX 30, RVol 0.5) |
| 17 | **AAPL** | 357.58 | - | **-** | 19 | - | POS +$1.2B | 348.5 | 360 | 360 | +$13.4M | +$867k bull / +$0 bear | out (clean 30, ADX 16, RVol 0.6) |
| 18 | **ORCL** | 123.62 | - | **-** | 19 | - | NEG -$3.9M | 124.12 | 125 | 125 | -$864k | +$61k bull / +$0 bear | out (clean 31, ADX 30, RVol 0.5) |
| 19 | **PLTR** | 167.76 | - | **-** | 17 | - | POS +$91.7M | 160.13 | 170 | 165 | -$734k | +$86k bull / -$70k bear | out (clean 29, ADX 28, RVol 0.2) |
| 20 | **UBER** | 69.52 | - | **-** | 15 | - | POS +$15.0M | 68.95 | 70 | 70 | +$300k | - | out (clean 33, ADX 11, RVol 0.4) |
| 21 | **NFLX** | 62.28 | - | **-** | 12 | - | NEG -$41.2M | 63.33 | 65 | 62 | +$537k | - | out (clean 32, ADX 37, RVol 0.7) |
| 22 | **SMCI** | 26.15 | - | **-** | 10 | - | NEG -$2.9M | - | 27 | 25 | +$232k | - | out (clean 34, ADX 26, RVol 0.4) |
| 23 | **CRM** | 217.62 | - | **-** | 9 | - | NEG -$7.0M | 222.72 | 220 | 220 | +$77k | - | out (clean 28, ADX 19, RVol 0.6) |
| 24 | **META** | 631.80 | - | **-** | 8 | - | NEG -$1.3M | 631.71 | 630 | 625 | +$6.9M | - | out (clean 29, ADX 26, RVol 0.6) |
| 25 | **SHOP** | 146.57 | - | **-** | 6 | - | POS +$2.4M | 145.39 | 150 | 140 | +$49k | - | out (clean 31, ADX 19, RVol 0.3) |
| 26 | **BABA** | 93.81 | - | **-** | 6 | - | NEG -$17.3M | - | 100 | 100 | +$44k | - | out (clean 27, ADX 25, RVol 0.4) |
| 27 | **MSFT** | 522.34 | - | **-** | 4 | - | POS +$42.1M | 521.48 | 535 | 520 | -$842k | - | out (clean 31, ADX 18, RVol 0.3) |

## Big prints this scan (88)
- **SPY** CALL 745 2026-11-16 (3DTE): 1,965 @ 7.00 = **+$1.4M** BUY | vol 8,944 / OI 981
- **ARM** CALL 192.5 2026-11-20 (7DTE): 1,853 @ 6.09 = **+$1.1M** SELL | vol 1,983 / OI 178
- **AMD** CALL 515 2026-11-13 (0DTE): 500 @ 9.75 = **+$488k** SELL | vol 996 / OI 978
- **NVDA** CALL 160 2026-11-18 (5DTE): 500 @ 7.70 = **+$385k** SELL | vol 3,996 / OI 1,255
- **AMD** PUT 520 2026-11-20 (7DTE): 150 @ 23.40 = **+$351k** BUY | vol 1,350 / OI 1,791
- **SPY** CALL 749 2026-11-16 (3DTE): 499 @ 4.60 = **+$230k** BUY | vol 5,471 / OI 473
- **HOOD** PUT 81 2026-11-13 (0DTE): 546 @ 3.77 = **+$206k** MID | vol 898 / OI 2,484
- **HOOD** PUT 78 2026-11-20 (7DTE): 546 @ 3.31 = **+$181k** MID | vol 897 / OI 374
- **SPY** PUT 755 2026-11-16 (3DTE): 257 @ 6.94 = **+$178k** MID | vol 13,891 / OI 2,248
- **NVDA** PUT 160 2026-11-18 (5DTE): 199 @ 7.50 = **+$149k** SELL | vol 5,928 / OI 5,421
- **SPY** CALL 752 2026-11-17 (4DTE): 362 @ 3.85 = **+$139k** SELL | vol 3,187 / OI 110
- **QQQ** CALL 674 2026-11-16 (3DTE): 199 @ 5.81 = **+$116k** SELL | vol 5,487 / OI 153
- **NVDA** PUT 160 2026-11-20 (7DTE): 132 @ 8.35 = **+$110k** SELL | vol 14,930 / OI 37,700
- **AMD** CALL 530 2026-11-20 (7DTE): 50 @ 21.50 = **+$108k** BUY | vol 1,545 / OI 2,460
- **AMD** PUT 530 2026-11-13 (0DTE): 100 @ 10.00 = **+$100k** BUY | vol 20,533 / OI 2,056

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 710 2026-11-16 (3DTE): 1,039 traded vs OI 958
- **SPY** PUT 739 2026-11-17 (4DTE): 1,337 traded vs OI 140
- **QQQ** CALL 671 2026-11-16 (3DTE): 520 traded vs OI 124
- **QQQ** CALL 674 2026-11-17 (4DTE): 502 traded vs OI 194
- **IWM** PUT 271 2026-11-16 (3DTE): 502 traded vs OI 141
- **IWM** CALL 277 2026-11-18 (5DTE): 525 traded vs OI 30
- **SMH** PUT 477.5 2026-11-20 (7DTE): 503 traded vs OI 133
- **NVDA** PUT 147 2026-11-18 (5DTE): 505 traded vs OI 0
- **AMD** PUT 505 2026-11-16 (3DTE): 507 traded vs OI 0
- **AMD** CALL 522.5 2026-11-13 (0DTE): 697 traded vs OI 323
- **AMD** PUT 532.5 2026-11-20 (7DTE): 500 traded vs OI 210
- **META** PUT 610 2026-11-13 (0DTE): 3,128 traded vs OI 2,977
- **MSFT** CALL 550 2026-11-18 (5DTE): 505 traded vs OI 155
- **ARM** CALL 192.5 2026-11-20 (7DTE): 1,983 traded vs OI 178
- **ARM** CALL 197.5 2026-11-20 (7DTE): 1,964 traded vs OI 80

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
