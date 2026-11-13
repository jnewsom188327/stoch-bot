# GEX + FLOW SCAN - Fri Nov 13, 11:50 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (12)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:30 | **GOOGL** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/13 292.5P | 0.56 | 0.52 | +23% (10m) | **-7%** | +237% | 290.96 |
| 11:15 | **ARM** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/13 180P | 0.79 | 0.17 | +0% (2m) | **-78%** | +122% | 180 |
| 11:14 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/13 667P | 0.70 | 0.42 | +59% (9m) | **-40%** | +21% | 672.05 hit |
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
Last 1m check 11:50:08 ET, last candle SPY 11:49, QQQ 11:49 | no errors
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
| 1 | **DELL** | 336.43 | FLOW SURGE | **CALLS** | 51 | none: 54 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (52 contracts' greeks worked out here) | NEG -$9.4M | - | 350 | 340 | +$8.5M | +$621k bull / -$165k bear | out (clean 38, ADX 52, RVol 2.0) |
| 2 | **GOOGL** | 293.89 | FLOW SURGE | **CALLS** | 41 | none: 94 calls 0-7DTE > 6 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only +17% at the target (needs +20%) (49 contracts' greeks worked out here) | POS +$162.0M | 289.42 | 295 | 290 | +$20.5M | +$66k bull / +$0 bear | out (clean 32, ADX 31, RVol 1.0) |
| 3 | **AMZN** | 264.21 | FLOW SURGE | **CALLS** | 38 | none: 84 calls 0-7DTE > 5 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only +13% at the target (needs +20%) (37 contracts' greeks worked out here) | POS +$374.9M | 251.36 | 265 | 265 | +$10.1M | +$199k bull / +$0 bear | out (clean 30, ADX 35, RVol 0.9) |
| 4 | **AVGO** | 342.34 | - | **-** | 31 | - | POS +$64.7M | 327.23 | 340 | 340 | +$21.0M | +$0 bull / -$29k bear | out (clean 36, ADX 42, RVol 0.5) |
| 5 | **HOOD** | 77.12 | - | **-** | 31 | - | NEG -$11.6M | 79.2 | 77 | 75 | +$3.2M | +$0 bull / -$61k bear | out (clean 36, ADX 52, RVol 1.2) |
| 6 | **QQQ** | 674.08 | - | **-** | 27 | - | NEG -$2.9B | 688.11 | 680 | 680 | +$288.4M | +$6.2M bull / -$2.4M bear | out (clean 32, ADX 46, RVol 0.8) |
| 7 | **SMH** | 477.98 | - | **-** | 27 | - | NEG -$375.5M | - | 500 | 475 | +$13.0M | +$62k bull / -$83k bear | out (clean 31, ADX 48, RVol 0.4) |
| 8 | **AMD** | 521.58 | - | **-** | 27 | - | POS +$21.7M | - | 530 | 530 | +$75.8M | +$3.7M bull / +$0 bear | out (clean 36, ADX 50, RVol 0.7) |
| 9 | **MSTR** | 109.15 | - | **-** | 25 | - | NEG -$41.0M | - | 110 | 110 | +$7.3M | +$473k bull / -$122k bear | out (clean 30, ADX 29, RVol 1.3) |
| 10 | **IWM** | 276.05 | - | **-** | 24 | - | NEG -$2.7B | 282.51 | 285 | 275 | +$20.3M | +$227k bull / +$0 bear | out (clean 36, ADX 28, RVol 0.6) |
| 11 | **COIN** | 127.12 | - | **-** | 24 | - | NEG -$20.8M | 132.71 | 137 | 130 | +$3.6M | - | out (clean 30, ADX 37, RVol 2.0) |
| 12 | **NVDA** | 159.81 | - | **-** | 22 | - | NEG -$290.3M | - | 175 | 160 | +$108.0M | +$1.7M bull / -$1.7M bear | out (clean 31, ADX 19, RVol 0.4) |
| 13 | **MU** | 757.61 | - | **-** | 22 | - | NEG -$21.6M | 773.65 | 760 | 750 | +$71.8M | +$3.0M bull / -$3.1M bear | out (clean 31, ADX 33, RVol 0.6) |
| 14 | **SPY** | 749.47 | - | **-** | 21 | - | NEG -$8.4B | 758.45 | 750 | 750 | +$250.8M | +$8.1M bull / -$588k bear | out (clean 33, ADX 28, RVol 0.5) |
| 15 | **SMCI** | 26.16 | - | **-** | 21 | - | NEG -$3.0M | - | 27 | 25 | +$259k | +$0 bull / -$60k bear | out (clean 34, ADX 26, RVol 0.4) |
| 16 | **TSLA** | 388.66 | - | **-** | 20 | - | POS +$330.4M | - | 400 | 390 | +$57.0M | +$2.4M bull / -$1.2M bear | out (clean 29, ADX 15, RVol 0.8) |
| 17 | **AAPL** | 357.60 | - | **-** | 19 | - | POS +$1.3B | 346.96 | 360 | 360 | +$12.6M | +$697k bull / -$228k bear | out (clean 30, ADX 18, RVol 0.7) |
| 18 | **ORCL** | 123.30 | - | **-** | 19 | - | POS +$7.6M | 121.12 | 125 | 125 | -$861k | +$61k bull / +$0 bear | out (clean 31, ADX 32, RVol 0.6) |
| 19 | **META** | 630.98 | - | **-** | 18 | - | NEG -$6.8M | 631.34 | 630 | 625 | +$6.8M | +$110k bull / -$49k bear | out (clean 29, ADX 25, RVol 0.6) |
| 20 | **PLTR** | 167.52 | - | **-** | 17 | - | POS +$87.2M | 161.53 | 165 | 165 | -$522k | +$83k bull / -$81k bear | out (clean 29, ADX 31, RVol 0.3) |
| 21 | **MSFT** | 522.84 | - | **-** | 15 | - | POS +$71.3M | 521.2 | 535 | 520 | -$1.1M | +$35k bull / -$291k bear | out (clean 31, ADX 18, RVol 0.4) |
| 22 | **UBER** | 69.46 | - | **-** | 15 | - | POS +$12.0M | 68.93 | 70 | 70 | +$298k | - | out (clean 33, ADX 12, RVol 0.5) |
| 23 | **NFLX** | 62.18 | - | **-** | 12 | - | NEG -$41.1M | 63.38 | 65 | 62 | +$495k | - | out (clean 32, ADX 37, RVol 0.8) |
| 24 | **ARM** | 185.84 | - | **-** | 12 | - | NEG -$3.0M | 190.78 | 185 | 190 | -$345k | - | out (clean 33, ADX 51, RVol 0.6) |
| 25 | **CRM** | 217.66 | - | **-** | 9 | - | NEG -$7.2M | 222.73 | 220 | 220 | +$72k | - | out (clean 28, ADX 19, RVol 0.8) |
| 26 | **SHOP** | 145.87 | - | **-** | 7 | - | POS +$1.9M | 144.9 | 150 | 140 | +$65k | - | out (clean 31, ADX 21, RVol 0.5) |
| 27 | **BABA** | 93.78 | - | **-** | 6 | - | NEG -$15.4M | - | 100 | 100 | +$39k | - | out (clean 28, ADX 25, RVol 0.3) |

## Big prints this scan (123)
- **SPY** CALL 750 2026-11-16 (3DTE): 2,000 @ 4.65 = **+$930k** BUY | vol 31,050 / OI 1,280
- **SPY** CALL 745 2026-11-16 (3DTE): 1,064 @ 7.90 = **+$841k** BUY | vol 4,877 / OI 981
- **AAPL** CALL 340 2026-11-13 (0DTE): 314 @ 18.31 = **+$575k** BUY | vol 768 / OI 3,088
- **SPY** PUT 755 2026-11-13 (0DTE): 1,370 @ 4.05 = **+$555k** SELL | vol 141,914 / OI 24,184
- **SPY** PUT 755 2026-11-13 (0DTE): 981 @ 4.47 = **+$439k** SELL | vol 141,914 / OI 24,184
- **SPY** PUT 755 2026-11-13 (0DTE): 905 @ 4.09 = **+$370k** SELL | vol 141,914 / OI 24,184
- **SPY** PUT 755 2026-11-13 (0DTE): 731 @ 4.61 = **+$337k** SELL | vol 141,914 / OI 24,184
- **SPY** CALL 745 2026-11-16 (3DTE): 388 @ 7.90 = **+$307k** BUY | vol 4,877 / OI 981
- **SPY** PUT 755 2026-11-13 (0DTE): 762 @ 3.99 = **+$304k** SELL | vol 141,914 / OI 24,184
- **SPY** CALL 745 2026-11-16 (3DTE): 331 @ 7.88 = **+$261k** BUY | vol 4,877 / OI 981
- **SPY** PUT 755 2026-11-13 (0DTE): 569 @ 4.05 = **+$230k** SELL | vol 141,914 / OI 24,184
- **SPY** PUT 755 2026-11-13 (0DTE): 569 @ 4.05 = **+$230k** SELL | vol 141,914 / OI 24,184
- **QQQ** CALL 675 2026-11-20 (7DTE): 193 @ 11.78 = **+$227k** BUY | vol 2,766 / OI 6,650
- **QQQ** CALL 675 2026-11-20 (7DTE): 178 @ 11.79 = **+$210k** BUY | vol 2,766 / OI 6,650
- **QQQ** CALL 675 2026-11-20 (7DTE): 168 @ 11.82 = **+$199k** BUY | vol 2,766 / OI 6,650

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 791 2026-12-11 (28DTE): 554 traded vs OI 221
- **QQQ** CALL 676 2026-11-18 (5DTE): 519 traded vs OI 288
- **QQQ** CALL 694 2026-11-18 (5DTE): 705 traded vs OI 287
- **IWM** PUT 276 2026-11-18 (5DTE): 510 traded vs OI 89
- **SMH** PUT 440 2026-11-20 (7DTE): 2,168 traded vs OI 0
- **SMH** PUT 480 2026-11-13 (0DTE): 5,080 traded vs OI 3,607
- **NVDA** CALL 147 2026-11-16 (3DTE): 571 traded vs OI 0
- **AMZN** PUT 257.5 2026-11-16 (3DTE): 502 traded vs OI 213
- **AMZN** CALL 265 2026-11-16 (3DTE): 511 traded vs OI 505
- **MSFT** PUT 512.5 2026-11-16 (3DTE): 501 traded vs OI 100
- **COIN** PUT 124 2026-11-13 (0DTE): 668 traded vs OI 180
- **DELL** CALL 370 2026-11-13 (0DTE): 832 traded vs OI 680
- **MU** PUT 717.5 2026-11-13 (0DTE): 533 traded vs OI 244
- **MU** CALL 740 2026-11-13 (0DTE): 709 traded vs OI 678
- **MU** PUT 705 2026-11-13 (0DTE): 557 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
