# GEX + FLOW SCAN - Fri Nov 13, 03:15 PM ET
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
Last 1m check 15:15:08 ET, last candle SPY 15:14, QQQ 15:14 | no errors
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
| 1 | **GOOGL** | 295.18 | PINNED between the walls (positive gamma) - chop | **-** | 37 | - | POS +$191.2M | 290.53 | 295 | 295 | +$20.2M | +$0 bull / -$152k bear | out (clean 30, ADX 12, RVol 0.5) |
| 2 | **META** | 641.33 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 34 | none: 194 calls 0-7DTE > 9 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (80 contracts' greeks worked out here) | POS +$202.8M | 635.21 | 650 | 640 | -$1.5M | +$31k bull / -$32k bear | out (clean 30, ADX 24, RVol 0.6) |
| 3 | **TSLA** | 390.96 | PINNED between the walls (positive gamma) - chop | **-** | 29 | - | POS +$464.8M | - | 390 | 390 | +$41.5M | +$874k bull / -$1.5M bear | out (clean 28, ADX 11, RVol 0.5) |
| 4 | **AMZN** | 265.48 | PINNED between the walls (positive gamma) - chop | **-** | 29 | - | POS +$435.2M | 255.34 | 265 | 265 | +$8.7M | +$0 bull / -$813k bear | out (clean 29, ADX 12, RVol 0.2) |
| 5 | **MU** | 773.19 | FLIP CROSS down into negative gamma | **PUTS** | 29 | none: 160 puts 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (66 contracts' greeks worked out here) | NEG -$87.7M | 786.62 | 770 | 770 | +$60.7M | +$154k bull / -$4.4M bear | out (clean 30, ADX 23, RVol 0.3) |
| 6 | **AVGO** | 345.95 | - | **-** | 21 | - | POS +$86.2M | 332.67 | 350 | 350 | +$18.5M | +$0 bull / -$1.4M bear | out (clean 36, ADX 13, RVol 0.3) |
| 7 | **HOOD** | 78.40 | - | **-** | 20 | - | NEG -$14.2M | 79.66 | 78 | 79 | +$2.4M | +$25k bull / +$0 bear | out (clean 35, ADX 16, RVol 1.0) |
| 8 | **AAPL** | 356.89 | - | **-** | 19 | - | POS +$1.3B | 347.27 | 355 | 355 | +$12.5M | +$407k bull / +$0 bear | out (clean 30, ADX 22, RVol 0.8) |
| 9 | **COIN** | 128.94 | - | **-** | 19 | - | NEG -$24.4M | 132.22 | 140 | 130 | +$2.2M | +$82k bull / +$0 bear | out (clean 30, ADX 15, RVol 0.5) |
| 10 | **SPY** | 753.57 | - | **-** | 18 | - | NEG -$8.6B | 759.76 | 755 | 755 | +$215.8M | +$3.6M bull / -$3.4M bear | out (clean 33, ADX 19, RVol 0.6) |
| 11 | **QQQ** | 679.83 | - | **-** | 18 | - | NEG -$3.3B | 688.87 | 680 | 680 | +$218.7M | +$475k bull / -$804k bear | out (clean 32, ADX 19, RVol 0.4) |
| 12 | **SMH** | 487.02 | - | **-** | 18 | - | NEG -$285.7M | - | 500 | 490 | +$6.2M | +$0 bull / -$465k bear | out (clean 31, ADX 24, RVol 0.3) |
| 13 | **NVDA** | 162.97 | - | **-** | 18 | - | NEG -$347.0M | - | 175 | 165 | +$77.5M | +$157k bull / -$5.7M bear | out (clean 31, ADX 21, RVol 0.4) |
| 14 | **ORCL** | 125.28 | - | **-** | 18 | - | NEG -$1.7M | 125.38 | 125 | 125 | -$1.6M | +$0 bull / -$48k bear | out (clean 31, ADX 21, RVol 0.7) |
| 15 | **AMD** | 534.09 | - | **-** | 17 | - | POS +$39.8M | 524.08 | 530 | 530 | +$44.2M | +$431k bull / -$2.7M bear | out (clean 35, ADX 24, RVol 0.4) |
| 16 | **NFLX** | 62.27 | - | **-** | 17 | - | NEG -$44.5M | 63.44 | 65 | 62 | +$421k | +$0 bull / -$32k bear | out (clean 30, ADX 17, RVol 0.7) |
| 17 | **DELL** | 342.86 | - | **-** | 17 | - | NEG -$12.8M | 351.59 | 350 | 340 | +$4.3M | +$0 bull / -$656k bear | out (clean 38, ADX 13, RVol 0.8) |
| 18 | **SMCI** | 26.71 | - | **-** | 16 | - | NEG -$2.7M | 27.52 | 27 | 27 | -$1.8M | - | out (clean 34, ADX 29, RVol 0.5) |
| 19 | **PLTR** | 168.85 | - | **-** | 14 | - | POS +$136.0M | 160.51 | 170 | 165 | +$205k | +$258k bull / -$80k bear | out (clean 29, ADX 13, RVol 0.5) |
| 20 | **BABA** | 93.92 | - | **-** | 14 | - | NEG -$19.2M | - | 100 | 95 | +$22k | +$30k bull / +$0 bear | out (clean 27, ADX 15, RVol 0.3) |
| 21 | **ARM** | 190.66 | - | **-** | 13 | - | NEG -$4.1M | 191.94 | 190 | 190 | -$4.0M | - | out (clean 33, ADX 17, RVol 0.1) |
| 22 | **SHOP** | 147.54 | - | **-** | 13 | - | POS +$3.4M | 146.41 | 150 | 140 | +$33k | +$33k bull / +$0 bear | out (clean 30, ADX 8, RVol 0.5) |
| 23 | **MSFT** | 524.40 | - | **-** | 12 | - | POS +$194.3M | 522.31 | 535 | 520 | +$37k | +$30k bull / +$0 bear | out (clean 30, ADX 8, RVol 0.4) |
| 24 | **CRM** | 218.50 | - | **-** | 12 | - | NEG -$3.4M | 220.81 | 220 | 220 | +$138k | - | out (clean 27, ADX 26, RVol 1.3) |
| 25 | **IWM** | 277.43 | - | **-** | 10 | - | NEG -$2.5B | 282.22 | 285 | 275 | +$16.3M | - | out (clean 36, ADX 20, RVol 0.4) |
| 26 | **UBER** | 69.39 | - | **-** | 10 | - | POS +$9.1M | 69.18 | 70 | 69 | +$285k | - | out (clean 32, ADX 14, RVol 0.4) |
| 27 | **MSTR** | 112.48 | - | **-** | 8 | - | NEG -$29.4M | - | 120 | 110 | +$2.0M | - | out (clean 32, ADX 32, RVol 0.5) |

## Big prints this scan (87)
- **SPY** CALL 745 2026-11-16 (3DTE): 1,998 @ 9.00 = **+$1.8M** SELL | vol 106,824 / OI 981
- **SPY** CALL 745 2026-11-16 (3DTE): 1,852 @ 9.50 = **+$1.8M** BUY | vol 106,824 / OI 981
- **SPY** CALL 745 2026-11-16 (3DTE): 1,813 @ 9.50 = **+$1.7M** BUY | vol 106,824 / OI 981
- **SPY** CALL 745 2026-11-16 (3DTE): 500 @ 8.75 = **+$438k** SELL | vol 106,824 / OI 981
- **NVDA** PUT 160 2026-11-18 (5DTE): 526 @ 6.02 = **+$317k** BUY | vol 16,031 / OI 5,421
- **SPY** CALL 745 2026-11-16 (3DTE): 317 @ 8.75 = **+$277k** SELL | vol 106,824 / OI 981
- **AMD** CALL 525 2026-11-18 (5DTE): 100 @ 24.00 = **+$240k** SELL | vol 966 / OI 93
- **SMH** PUT 500 2026-11-20 (7DTE): 99 @ 22.80 = **+$226k** BUY | vol 1,514 / OI 9,935
- **MU** CALL 770 2026-11-13 (0DTE): 921 @ 2.25 = **+$207k** SELL | vol 46,403 / OI 1,258
- **AMD** PUT 530 2026-11-16 (3DTE): 150 @ 11.00 = **+$165k** BUY | vol 3,020 / OI 202
- **SPY** CALL 745 2026-11-16 (3DTE): 148 @ 9.50 = **+$141k** BUY | vol 106,824 / OI 981
- **NVDA** CALL 162.5 2026-11-16 (3DTE): 412 @ 3.17 = **+$131k** SELL | vol 37,399 / OI 410
- **QQQ** CALL 674 2026-11-13 (0DTE): 200 @ 6.10 = **+$122k** BUY | vol 71,873 / OI 807
- **MU** PUT 770 2026-11-16 (3DTE): 74 @ 14.64 = **+$108k** BUY | vol 3,829 / OI 252
- **SMH** CALL 477.5 2026-11-13 (0DTE): 150 @ 7.00 = **+$105k** SELL | vol 630 / OI 353

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 730 2026-11-17 (4DTE): 1,226 traded vs OI 1,220
- **SPY** PUT 748 2026-12-11 (28DTE): 898 traded vs OI 896
- **SPY** CALL 753 2026-12-04 (21DTE): 552 traded vs OI 395
- **QQQ** CALL 706 2026-11-16 (3DTE): 545 traded vs OI 209
- **QQQ** CALL 698 2026-11-17 (4DTE): 517 traded vs OI 270
- **QQQ** CALL 715 2026-11-13 (0DTE): 2,706 traded vs OI 2,493
- **QQQ** PUT 679 2026-11-18 (5DTE): 516 traded vs OI 227
- **QQQ** CALL 689 2026-11-20 (7DTE): 2,983 traded vs OI 1,480
- **QQQ** PUT 679 2026-11-20 (7DTE): 1,352 traded vs OI 1,310
- **QQQ** PUT 650 2026-11-27 (14DTE): 4,245 traded vs OI 3,415
- **SMH** PUT 472.5 2026-11-16 (3DTE): 512 traded vs OI 11
- **SMH** CALL 535 2026-11-20 (7DTE): 503 traded vs OI 0
- **NVDA** CALL 157.5 2026-11-27 (14DTE): 509 traded vs OI 0
- **TSLA** CALL 430 2026-11-20 (7DTE): 2,201 traded vs OI 0
- **TSLA** CALL 430 2026-11-13 (0DTE): 1,838 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
