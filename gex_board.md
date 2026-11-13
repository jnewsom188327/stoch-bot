# GEX + FLOW SCAN - Fri Nov 13, 03:45 PM ET
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
Last 1m check 15:32:08 ET, last candle SPY 15:31, QQQ 15:31 | no errors
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
| 1 | **GOOGL** | 295.44 | PINNED between the walls (positive gamma) - chop | **-** | 38 | - | POS +$207.1M | 290.93 | 295 | 295 | +$20.2M | +$0 bull / -$876k bear | out (clean 30, ADX 12, RVol 0.8) |
| 2 | **META** | 640.58 | PINNED between the walls (positive gamma) - chop | **-** | 32 | - | POS +$191.4M | 630.64 | 640 | 640 | +$106k | +$1.2M bull / -$54k bear | out (clean 30, ADX 24, RVol 1.1) |
| 3 | **MU** | 771.66 | PINNED between the walls (positive gamma) - chop | **-** | 32 | - | POS +$24.6M | 770.33 | 770 | 770 | +$60.8M | +$1.7M bull / -$1.6M bear | out (clean 30, ADX 23, RVol 0.7) |
| 4 | **TSLA** | 390.18 | PINNED between the walls (positive gamma) - chop | **-** | 30 | - | POS +$391.2M | - | 390 | 390 | +$44.1M | +$13.0M bull / -$197k bear | out (clean 28, ADX 10, RVol 0.8) |
| 5 | **AMD** | 530.13 | PINNED between the walls (positive gamma) - chop | **-** | 30 | - | POS +$44.9M | 517.33 | 530 | 530 | +$52.8M | +$3.5M bull / +$0 bear | out (clean 35, ADX 18, RVol 0.5) |
| 6 | **AAPL** | 356.03 | - | **-** | 22 | - | POS +$1.2B | 347.97 | 355 | 355 | +$14.7M | +$698k bull / +$0 bear | out (clean 30, ADX 31, RVol 1.6) |
| 7 | **AVGO** | 345.30 | - | **-** | 20 | - | POS +$85.8M | 333.4 | 350 | 340 | +$18.4M | +$28k bull / +$0 bear | out (clean 36, ADX 10, RVol 0.6) |
| 8 | **IWM** | 277.08 | - | **-** | 19 | - | NEG -$2.7B | 282.09 | 285 | 277 | +$17.7M | +$335k bull / +$0 bear | out (clean 36, ADX 17, RVol 0.5) |
| 9 | **SPY** | 752.59 | - | **-** | 18 | - | NEG -$6.5B | 756.07 | 750 | 753 | +$236.4M | +$1.5M bull / +$0 bear | out (clean 33, ADX 16, RVol 0.8) |
| 10 | **QQQ** | 678.57 | - | **-** | 18 | - | NEG -$2.1B | 682.71 | 680 | 680 | +$231.4M | +$1.6M bull / +$0 bear | out (clean 32, ADX 14, RVol 0.6) |
| 11 | **SMH** | 484.94 | - | **-** | 18 | - | NEG -$231.5M | - | 500 | 485 | +$7.0M | +$222k bull / -$137k bear | out (clean 31, ADX 20, RVol 0.4) |
| 12 | **NVDA** | 161.82 | - | **-** | 18 | - | NEG -$284.2M | 171.4 | 175 | 162.5 | +$86.4M | +$3.8M bull / +$0 bear | out (clean 31, ADX 18, RVol 0.4) |
| 13 | **DELL** | 342.36 | - | **-** | 18 | - | NEG -$11.6M | 350.92 | 350 | 340 | +$4.8M | +$141k bull / +$0 bear | out (clean 38, ADX 11, RVol 1.2) |
| 14 | **MSTR** | 112.06 | - | **-** | 18 | - | NEG -$26.3M | - | 120 | 110 | +$3.0M | +$962k bull / +$0 bear | out (clean 32, ADX 26, RVol 0.8) |
| 15 | **ORCL** | 125.12 | - | **-** | 17 | - | NEG -$12.8M | 125.52 | 125 | 125 | -$1.4M | +$434k bull / -$51k bear | out (clean 32, ADX 16, RVol 0.7) |
| 16 | **BABA** | 94.21 | - | **-** | 17 | - | NEG -$21.4M | - | 100 | 100 | -$370k | +$0 bull / -$51k bear | out (clean 26, ADX 14, RVol 0.5) |
| 17 | **AMZN** | 266.22 | - | **-** | 16 | - | POS +$425.3M | 256.97 | 265 | 265 | +$3.8M | +$0 bull / -$1.5M bear | out (clean 29, ADX 13, RVol 0.6) |
| 18 | **PLTR** | 168.23 | - | **-** | 15 | - | POS +$114.6M | 163.1 | 167.5 | 167.5 | +$586k | +$54k bull / +$0 bear | out (clean 29, ADX 14, RVol 0.8) |
| 19 | **MSFT** | 524.03 | - | **-** | 13 | - | POS +$148.0M | 522.69 | 535 | 520 | +$416k | +$204k bull / +$0 bear | out (clean 30, ADX 9, RVol 0.7) |
| 20 | **SMCI** | 26.61 | - | **-** | 13 | - | NEG -$1.9M | 26.89 | 27 | 25 | -$1.7M | - | out (clean 34, ADX 21, RVol 0.4) |
| 21 | **ARM** | 189.47 | - | **-** | 13 | - | NEG -$10.6M | 191.08 | 190 | 190 | -$4.0M | - | out (clean 33, ADX 14, RVol 0.3) |
| 22 | **HOOD** | 77.93 | - | **-** | 12 | - | NEG -$9.2M | 78.58 | 78 | 78 | +$2.6M | - | out (clean 34, ADX 18, RVol 1.3) |
| 23 | **CRM** | 217.94 | - | **-** | 12 | - | NEG -$3.8M | 222.4 | 217.5 | 220 | +$183k | - | out (clean 27, ADX 25, RVol 1.2) |
| 24 | **UBER** | 69.44 | - | **-** | 11 | - | POS +$5.9M | 69.32 | 70 | 70 | +$284k | - | out (clean 32, ADX 16, RVol 1.0) |
| 25 | **COIN** | 128.36 | - | **-** | 10 | - | NEG -$20.1M | 131.93 | 140 | 130 | +$2.4M | - | out (clean 30, ADX 18, RVol 0.7) |
| 26 | **NFLX** | 62.30 | - | **-** | 8 | - | NEG -$46.5M | 63.44 | 65 | 62 | +$572k | - | out (clean 30, ADX 19, RVol 1.1) |
| 27 | **SHOP** | 147.39 | - | **-** | 4 | - | POS +$6.8M | 146.2 | 147 | 140 | +$54k | - | out (clean 30, ADX 8, RVol 0.7) |

## Big prints this scan (116)
- **TSLA** CALL 380 2026-11-13 (0DTE): 4,671 @ 10.88 = **+$5.1M** BUY | vol 8,545 / OI 7,623
- **TSLA** CALL 377.5 2026-11-13 (0DTE): 2,000 @ 13.32 = **+$2.7M** BUY | vol 4,353 / OI 4,421
- **NVDA** CALL 162.5 2026-11-20 (7DTE): 627 @ 8.05 = **+$505k** BUY | vol 7,414 / OI 11
- **NVDA** CALL 160 2026-11-16 (3DTE): 500 @ 4.43 = **+$222k** BUY | vol 81,504 / OI 919
- **QQQ** CALL 681 2026-11-16 (3DTE): 495 @ 3.80 = **+$188k** BUY | vol 9,962 / OI 119
- **AMD** CALL 545 2026-11-20 (7DTE): 99 @ 18.25 = **+$181k** BUY | vol 1,863 / OI 2,025
- **AMD** CALL 545 2026-11-20 (7DTE): 98 @ 18.08 = **+$177k** BUY | vol 1,863 / OI 2,025
- **AMZN** CALL 267.5 2026-11-20 (7DTE): 400 @ 4.37 = **+$175k** SELL | vol 7,512 / OI 2,672
- **AMZN** CALL 267.5 2026-11-20 (7DTE): 400 @ 4.37 = **+$175k** SELL | vol 7,512 / OI 2,672
- **AMD** CALL 545 2026-11-20 (7DTE): 92 @ 18.07 = **+$166k** BUY | vol 1,863 / OI 2,025
- **GOOGL** PUT 290 2026-11-20 (7DTE): 465 @ 3.42 = **+$159k** BUY | vol 3,771 / OI 18,375
- **GOOGL** PUT 290 2026-11-20 (7DTE): 465 @ 3.42 = **+$159k** BUY | vol 3,771 / OI 18,375
- **AMZN** CALL 265 2026-11-20 (7DTE): 276 @ 5.60 = **+$155k** SELL | vol 3,109 / OI 31,267
- **META** CALL 645 2026-11-18 (5DTE): 155 @ 9.93 = **+$154k** BUY | vol 1,663 / OI 439
- **META** CALL 645 2026-11-18 (5DTE): 155 @ 9.93 = **+$154k** BUY | vol 1,663 / OI 439

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 749 2026-11-20 (7DTE): 3,504 traded vs OI 3,390
- **SPY** CALL 793 2026-12-04 (21DTE): 559 traded vs OI 520
- **SPY** PUT 715 2026-11-27 (14DTE): 3,021 traded vs OI 2,963
- **SPY** PUT 742 2026-11-27 (14DTE): 1,805 traded vs OI 874
- **QQQ** CALL 703 2026-11-24 (11DTE): 1,015 traded vs OI 89
- **QQQ** PUT 665 2026-11-24 (11DTE): 1,121 traded vs OI 88
- **QQQ** PUT 665 2026-11-27 (14DTE): 1,441 traded vs OI 1,381
- **NVDA** CALL 170 2026-11-23 (10DTE): 1,399 traded vs OI 1,347
- **TSLA** CALL 422.5 2026-11-20 (7DTE): 504 traded vs OI 0
- **TSLA** CALL 380 2026-11-13 (0DTE): 8,545 traded vs OI 7,623
- **TSLA** PUT 355 2026-11-16 (3DTE): 666 traded vs OI 353
- **AAPL** CALL 357.5 2026-11-20 (7DTE): 2,340 traded vs OI 2,227
- **AAPL** PUT 350 2026-11-20 (7DTE): 12,394 traded vs OI 11,984
- **META** PUT 615 2026-11-18 (5DTE): 563 traded vs OI 54
- **META** PUT 612.5 2026-11-18 (5DTE): 555 traded vs OI 18

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
