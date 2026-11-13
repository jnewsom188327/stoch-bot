# GEX + FLOW SCAN - Fri Nov 13, 02:50 PM ET
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
Last 1m check 14:50:08 ET, last candle SPY 14:49, QQQ 14:49 | no errors
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
| 1 | **GOOGL** | 295.07 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 43 | 11/13 295P @ 0.69 (delta 0.48) = est +47% at 293.97 | POS +$207.8M | 289.44 | 295 | 290 | +$20.3M | +$284k bull / +$0 bear | out (clean 31, ADX 13, RVol 0.6) |
| 2 | **AVGO** | 345.05 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 37 | none: 108 puts 0-7DTE > 3 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only -34% at the target (needs +20%) (41 contracts' greeks worked out here) | POS +$97.9M | - | 345 | 340 | +$17.4M | +$332k bull / +$0 bear | out (clean 36, ADX 14, RVol 0.2) |
| 3 | **META** | 640.19 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 34 | none: 190 calls 0-7DTE > 9 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (86 contracts' greeks worked out here) | POS +$146.5M | 635.51 | 650 | 640 | -$1.6M | +$90k bull / -$513k bear | out (clean 30, ADX 27, RVol 0.5) |
| 4 | **ORCL** | 125.14 | PINNED between the walls (positive gamma) - chop | **-** | 31 | - | POS +$11.7M | 123.88 | 125 | 125 | -$1.6M | +$32k bull / +$0 bear | out (clean 32, ADX 25, RVol 0.5) |
| 5 | **AMZN** | 265.29 | PINNED between the walls (positive gamma) - chop | **-** | 30 | - | POS +$446.3M | 253.31 | 265 | 265 | +$8.5M | +$769k bull / +$0 bear | out (clean 29, ADX 14, RVol 0.2) |
| 6 | **AMD** | 530.22 | PINNED between the walls (positive gamma) - chop | **-** | 29 | - | POS +$30.6M | 524.18 | 530 | 530 | +$49.7M | +$5.7M bull / -$78k bear | out (clean 35, ADX 23, RVol 0.3) |
| 7 | **ARM** | 189.27 | - | **-** | 23 | - | NEG -$3.7M | 191.33 | 190 | 190 | -$4.0M | +$37k bull / +$0 bear | out (clean 33, ADX 18, RVol 0.1) |
| 8 | **IWM** | 276.99 | - | **-** | 19 | - | NEG -$2.7B | 282.44 | 285 | 275 | +$16.4M | +$55k bull / +$0 bear | out (clean 36, ADX 18, RVol 0.4) |
| 9 | **MSTR** | 112.19 | - | **-** | 19 | - | NEG -$43.0M | - | 120 | 110 | +$2.1M | +$252k bull / -$275k bear | out (clean 32, ADX 37, RVol 0.8) |
| 10 | **QQQ** | 678.42 | - | **-** | 18 | - | NEG -$3.6B | 690.31 | 680 | 680 | +$226.7M | +$2.6M bull / -$135k bear | out (clean 32, ADX 18, RVol 0.4) |
| 11 | **SMH** | 484.10 | - | **-** | 18 | - | NEG -$262.3M | - | 500 | 475 | +$6.8M | +$413k bull / +$0 bear | out (clean 31, ADX 24, RVol 0.2) |
| 12 | **NVDA** | 162.07 | - | **-** | 18 | - | NEG -$344.4M | - | 175 | 160 | +$81.5M | +$2.5M bull / +$0 bear | out (clean 31, ADX 19, RVol 0.3) |
| 13 | **DELL** | 342.57 | - | **-** | 18 | - | NEG -$13.5M | 359.91 | 350 | 340 | +$4.2M | +$63k bull / +$0 bear | out (clean 38, ADX 17, RVol 0.7) |
| 14 | **MU** | 767.28 | - | **-** | 18 | - | NEG -$29.8M | 780.93 | 770 | 770 | +$68.9M | +$3.3M bull / -$243k bear | out (clean 30, ADX 22, RVol 0.4) |
| 15 | **SPY** | 752.70 | - | **-** | 17 | - | NEG -$8.9B | 760.35 | 750 | 755 | +$217.1M | +$11.2M bull / -$2.1M bear | out (clean 33, ADX 19, RVol 0.3) |
| 16 | **SMCI** | 26.70 | - | **-** | 17 | - | NEG -$2.7M | 27.45 | 27 | 27 | -$1.8M | - | out (clean 34, ADX 33, RVol 0.3) |
| 17 | **TSLA** | 391.21 | - | **-** | 16 | - | POS +$416.0M | 376.06 | 390 | 390 | +$40.9M | +$254k bull / -$64k bear | out (clean 28, ADX 11, RVol 0.4) |
| 18 | **AAPL** | 357.46 | - | **-** | 16 | - | POS +$1.0B | 349.92 | 360 | 360 | +$10.9M | +$89k bull / +$0 bear | out (clean 30, ADX 14, RVol 0.5) |
| 19 | **PLTR** | 168.78 | - | **-** | 14 | - | POS +$120.5M | 158.83 | 170 | 170 | +$293k | +$585k bull / +$0 bear | out (clean 29, ADX 16, RVol 0.4) |
| 20 | **MSFT** | 524.87 | - | **-** | 13 | - | POS +$145.5M | 523.05 | 535 | 520 | +$210k | +$75k bull / -$50k bear | out (clean 31, ADX 7, RVol 0.8) |
| 21 | **HOOD** | 77.86 | - | **-** | 10 | - | NEG -$11.7M | 79.3 | 78 | 80 | +$2.6M | - | out (clean 35, ADX 16, RVol 0.5) |
| 22 | **CRM** | 218.09 | - | **-** | 10 | - | NEG -$4.7M | 219.96 | 220 | 220 | +$139k | - | out (clean 27, ADX 22, RVol 0.7) |
| 23 | **UBER** | 69.47 | - | **-** | 9 | - | POS +$12.5M | 68.99 | 70 | 70 | +$262k | - | out (clean 33, ADX 17, RVol 0.2) |
| 24 | **COIN** | 128.23 | - | **-** | 8 | - | NEG -$19.6M | 131.85 | 140 | 130 | +$2.1M | - | out (clean 30, ADX 10, RVol 0.4) |
| 25 | **NFLX** | 62.30 | - | **-** | 7 | - | NEG -$44.4M | 63.29 | 65 | 62 | +$381k | - | out (clean 31, ADX 15, RVol 0.9) |
| 26 | **SHOP** | 147.38 | - | **-** | 3 | - | POS +$6.0M | 145.98 | 150 | 140 | -$23k | - | out (clean 31, ADX 8, RVol 0.5) |
| 27 | **BABA** | 94.03 | - | **-** | 3 | - | NEG -$20.5M | - | 100 | 95 | -$11k | - | out (clean 27, ADX 12, RVol 0.4) |

## Big prints this scan (86)
- **SPY** CALL 745 2026-11-16 (3DTE): 2,000 @ 9.06 = **+$1.8M** BUY | vol 96,484 / OI 981
- **SPY** CALL 745 2026-11-16 (3DTE): 1,499 @ 9.15 = **+$1.4M** BUY | vol 96,484 / OI 981
- **NVDA** PUT 160 2026-11-18 (5DTE): 923 @ 6.25 = **+$577k** SELL | vol 15,160 / OI 5,421
- **SPY** CALL 745 2026-11-16 (3DTE): 500 @ 9.15 = **+$458k** BUY | vol 96,484 / OI 981
- **NVDA** PUT 160 2026-11-20 (7DTE): 423 @ 6.95 = **+$294k** SELL | vol 22,984 / OI 37,700
- **AMZN** PUT 267.5 2026-11-20 (7DTE): 412 @ 6.34 = **+$261k** MID | vol 1,932 / OI 776
- **AMD** CALL 545 2026-11-20 (7DTE): 128 @ 18.10 = **+$232k** BUY | vol 1,036 / OI 2,025
- **QQQ** PUT 680 2026-11-20 (7DTE): 200 @ 10.80 = **+$216k** SELL | vol 10,713 / OI 87,076
- **AMD** CALL 545 2026-11-20 (7DTE): 112 @ 18.24 = **+$204k** BUY | vol 1,036 / OI 2,025
- **MU** CALL 760 2026-11-13 (0DTE): 160 @ 11.50 = **+$184k** BUY | vol 23,738 / OI 1,855
- **AMD** CALL 545 2026-11-20 (7DTE): 97 @ 18.25 = **+$177k** BUY | vol 1,036 / OI 2,025
- **AMD** CALL 545 2026-11-20 (7DTE): 92 @ 18.24 = **+$168k** BUY | vol 1,036 / OI 2,025
- **QQQ** PUT 685 2026-11-16 (3DTE): 195 @ 8.20 = **+$160k** SELL | vol 6,939 / OI 1,301
- **META** CALL 632.5 2026-11-13 (0DTE): 187 @ 8.13 = **+$152k** MID | vol 15,671 / OI 358
- **SPY** PUT 760 2026-11-13 (0DTE): 200 @ 7.38 = **+$148k** SELL | vol 25,849 / OI 34,901

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 751 2026-11-20 (7DTE): 5,342 traded vs OI 4,294
- **SPY** PUT 745 2026-11-23 (10DTE): 515 traded vs OI 289
- **SPY** CALL 825 2026-11-25 (12DTE): 800 traded vs OI 0
- **SPY** CALL 809 2026-11-20 (7DTE): 1,662 traded vs OI 1,522
- **QQQ** PUT 663 2026-11-20 (7DTE): 504 traded vs OI 371
- **QQQ** PUT 667 2026-11-25 (12DTE): 504 traded vs OI 0
- **QQQ** PUT 675 2026-11-27 (14DTE): 1,681 traded vs OI 1,676
- **AAPL** PUT 365 2026-11-13 (0DTE): 502 traded vs OI 492
- **AAPL** PUT 342.5 2026-11-18 (5DTE): 537 traded vs OI 65
- **AAPL** CALL 372.5 2026-11-27 (14DTE): 572 traded vs OI 0
- **AMZN** CALL 272.5 2026-11-20 (7DTE): 4,741 traded vs OI 4,738
- **GOOGL** CALL 295 2026-11-18 (5DTE): 500 traded vs OI 207
- **GOOGL** CALL 300 2026-11-18 (5DTE): 741 traded vs OI 736
- **DELL** CALL 360 2026-11-13 (0DTE): 1,696 traded vs OI 1,695
- **MSTR** CALL 121 2026-11-20 (7DTE): 4,204 traded vs OI 431

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
