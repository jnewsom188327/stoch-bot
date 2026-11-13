# GEX + FLOW SCAN - Fri Nov 13, 11:40 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (12)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:30 | **GOOGL** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/13 292.5P | 0.56 | 0.69 | +23% (10m) | **+23%** | +237% | 290.96 |
| 11:15 | **ARM** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/13 180P | 0.79 | 0.33 | +0% (2m) | **-58%** | +122% | 180 |
| 11:14 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/13 667P | 0.70 | 0.53 | +59% (9m) | **-24%** | +21% | 672.05 hit |
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
Last 1m check 11:40:08 ET, last candle SPY 11:39, QQQ 11:39 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 11:13 | QQQ | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | **FIRE** QQQ261113P00667000 |
| 11:02 | QQQ | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |
| 10:35 | SPY | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | **FIRE** SPY261113P00743000 |
| 10:16 | QQQ | 1m WHIPSAW | R1 R2 | CALLS | TURNING your way | **FIRE** QQQ261113C00683000 |

## Flow surges NOT fired - price disagreed (40 today, last 5)
- 11:40 HOOD CALLS: under EMA 20 - flow says one way, price says the other
- 11:35 HOOD CALLS: under EMA 20 - flow says one way, price says the other
- 11:25 HOOD CALLS: price -0.54 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 11:20 HOOD CALLS: price -0.21 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 11:15 HOOD CALLS: price -0.56 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **HOOD** | 77.20 | FLOW SURGE | **CALLS** | 47 | 11/13 77C @ 0.73 (delta 0.56) = est +192% at 79.15 | NEG -$10.5M | 79.15 | 77 | 75 | +$3.2M | +$460k bull / -$61k bear | out (clean 36, ADX 55, RVol 1.6) |
| 2 | **AMZN** | 264.64 | PINNED between the walls (positive gamma) - chop | **-** | 43 | - | POS +$406.7M | 248.95 | 265 | 265 | +$9.0M | +$232k bull / +$0 bear | out (clean 30, ADX 34, RVol 0.9) |
| 3 | **GOOGL** | 293.46 | FLOW SURGE | **CALLS** | 41 | 11/13 295C @ 0.74 (delta 0.33) = est +45% at 295 | POS +$138.4M | 289.69 | 300 | 290 | +$20.1M | +$47k bull / +$0 bear | out (clean 32, ADX 31, RVol 1.1) |
| 4 | **MU** | 756.00 | FLIP CROSS down into negative gamma | **PUTS** | 36 | none: 169 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (83 contracts' greeks worked out here) | NEG -$4.7M | 757.55 | 760 | 750 | +$67.1M | +$229k bull / -$5.0M bear | out (clean 31, ADX 35, RVol 0.6) |
| 5 | **DELL** | 332.57 | - | **-** | 35 | - | NEG -$4.1M | 342.12 | 350 | 340 | +$8.8M | +$26k bull / -$81k bear | out (clean 38, ADX 51, RVol 2.0) |
| 6 | **COIN** | 126.83 | - | **-** | 34 | - | NEG -$20.5M | 133.21 | 137 | 125 | +$3.5M | +$0 bull / -$28k bear | out (clean 31, ADX 39, RVol 2.0) |
| 7 | **AVGO** | 341.09 | - | **-** | 32 | - | POS +$66.5M | - | 340 | 340 | +$21.0M | +$0 bull / -$267k bear | out (clean 36, ADX 45, RVol 0.5) |
| 8 | **SMH** | 477.43 | - | **-** | 27 | - | NEG -$377.3M | - | 500 | 475 | +$11.5M | +$0 bull / -$390k bear | out (clean 31, ADX 51, RVol 0.8) |
| 9 | **QQQ** | 674.05 | - | **-** | 26 | - | NEG -$2.7B | 685.39 | 680 | 680 | +$267.4M | +$738k bull / -$10.3M bear | out (clean 32, ADX 49, RVol 0.7) |
| 10 | **AMD** | 521.44 | - | **-** | 26 | - | POS +$23.2M | - | 550 | 530 | +$70.7M | +$3.7M bull / -$492k bear | out (clean 35, ADX 50, RVol 0.8) |
| 11 | **MSTR** | 109.30 | - | **-** | 25 | - | NEG -$41.4M | - | 110 | 110 | +$5.8M | +$78k bull / -$187k bear | out (clean 30, ADX 30, RVol 1.3) |
| 12 | **NVDA** | 159.83 | - | **-** | 23 | - | NEG -$258.7M | - | 175 | 160 | +$99.7M | +$43k bull / -$5.5M bear | out (clean 31, ADX 20, RVol 0.6) |
| 13 | **SPY** | 749.85 | - | **-** | 22 | - | NEG -$7.7B | 757.69 | 750 | 750 | +$233.0M | +$438k bull / -$5.0M bear | out (clean 33, ADX 29, RVol 0.5) |
| 14 | **SMCI** | 26.04 | - | **-** | 22 | - | NEG -$2.3M | 26.86 | 27 | 25 | +$277k | +$0 bull / -$60k bear | out (clean 34, ADX 27, RVol 0.5) |
| 15 | **TSLA** | 388.31 | - | **-** | 20 | - | POS +$334.7M | - | 400 | 390 | +$50.2M | +$262k bull / -$1.9M bear | out (clean 29, ADX 16, RVol 0.9) |
| 16 | **AAPL** | 358.28 | - | **-** | 19 | - | POS +$1.3B | 348.48 | 360 | 360 | +$10.4M | +$0 bull / -$254k bear | out (clean 30, ADX 20, RVol 0.7) |
| 17 | **ORCL** | 123.38 | - | **-** | 19 | - | POS +$6.9M | 121.63 | 125 | 125 | -$760k | +$0 bull / -$75k bear | out (clean 31, ADX 34, RVol 0.4) |
| 18 | **META** | 631.41 | - | **-** | 18 | - | NEG -$1.1M | 631.58 | 630 | 625 | +$5.3M | +$154k bull / -$359k bear | out (clean 29, ADX 26, RVol 0.7) |
| 19 | **PLTR** | 167.40 | - | **-** | 18 | - | POS +$85.3M | 161.46 | 165 | 165 | -$503k | +$0 bull / -$289k bear | out (clean 29, ADX 34, RVol 0.4) |
| 20 | **MSFT** | 523.28 | - | **-** | 16 | - | POS +$111.9M | 521.15 | 535 | 520 | -$1.6M | +$0 bull / -$343k bear | out (clean 31, ADX 20, RVol 0.5) |
| 21 | **IWM** | 276.36 | - | **-** | 15 | - | NEG -$2.6B | 282.62 | 285 | 275 | +$19.2M | - | out (clean 36, ADX 32, RVol 0.6) |
| 22 | **UBER** | 69.43 | - | **-** | 15 | - | POS +$12.0M | 68.84 | 70 | 70 | +$288k | - | out (clean 33, ADX 13, RVol 0.6) |
| 23 | **NFLX** | 62.29 | - | **-** | 12 | - | NEG -$31.9M | 63.02 | 65 | 62 | +$481k | - | out (clean 32, ADX 36, RVol 0.9) |
| 24 | **ARM** | 185.20 | - | **-** | 12 | - | NEG -$2.6M | 189.57 | 185 | 190 | -$337k | - | out (clean 33, ADX 54, RVol 0.8) |
| 25 | **CRM** | 217.29 | - | **-** | 10 | - | NEG -$7.4M | 222 | 220 | 220 | +$85k | - | out (clean 28, ADX 19, RVol 0.8) |
| 26 | **SHOP** | 146.00 | - | **-** | 8 | - | POS +$2.8M | 144.82 | 150 | 140 | +$64k | - | out (clean 31, ADX 22, RVol 0.7) |
| 27 | **BABA** | 94.06 | - | **-** | 5 | - | NEG -$19.8M | - | 100 | 95 | +$4k | - | out (clean 28, ADX 23, RVol 0.3) |

## Big prints this scan (147)
- **MU** PUT 750 2026-11-20 (7DTE): 314 @ 31.55 = **+$991k** BUY | vol 2,876 / OI 6,865
- **QQQ** PUT 670 2026-11-13 (0DTE): 3,000 @ 1.53 = **+$459k** BUY | vol 123,938 / OI 7,701
- **NVDA** PUT 160 2026-11-20 (7DTE): 382 @ 8.69 = **+$332k** BUY | vol 14,214 / OI 37,700
- **NVDA** PUT 155 2026-11-20 (7DTE): 500 @ 6.28 = **+$314k** BUY | vol 10,065 / OI 14,723
- **QQQ** PUT 667 2026-11-13 (0DTE): 3,000 @ 0.83 = **+$249k** BUY | vol 39,786 / OI 755
- **QQQ** PUT 670 2026-11-13 (0DTE): 1,700 @ 1.38 = **+$235k** BUY | vol 123,938 / OI 7,701
- **AMD** CALL 525 2026-11-13 (0DTE): 448 @ 4.95 = **+$222k** BUY | vol 4,027 / OI 1,344
- **SPY** CALL 752 2026-11-20 (7DTE): 300 @ 6.26 = **+$188k** SELL | vol 1,372 / OI 3,851
- **QQQ** CALL 672 2026-11-13 (0DTE): 523 @ 3.25 = **+$170k** SELL | vol 15,818 / OI 893
- **QQQ** PUT 690 2026-11-16 (3DTE): 98 @ 17.20 = **+$169k** BUY | vol 2,237 / OI 1,636
- **NVDA** CALL 157.5 2026-11-16 (3DTE): 396 @ 4.10 = **+$162k** SELL | vol 2,590 / OI 534
- **AMD** PUT 525 2026-11-20 (7DTE): 63 @ 25.30 = **+$159k** MID | vol 1,068 / OI 464
- **NVDA** PUT 162.5 2026-11-20 (7DTE): 160 @ 9.95 = **+$159k** BUY | vol 4,177 / OI 505
- **AMD** PUT 525 2026-11-20 (7DTE): 62 @ 25.25 = **+$157k** MID | vol 1,068 / OI 464
- **QQQ** CALL 675 2026-11-13 (0DTE): 818 @ 1.85 = **+$151k** SELL | vol 84,701 / OI 5,568

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 768 2026-11-17 (4DTE): 732 traded vs OI 682
- **SPY** PUT 675 2026-11-18 (5DTE): 570 traded vs OI 0
- **SPY** PUT 690 2026-11-24 (11DTE): 812 traded vs OI 75
- **SPY** CALL 770 2026-11-23 (10DTE): 501 traded vs OI 456
- **SPY** PUT 725 2026-11-24 (11DTE): 1,252 traded vs OI 258
- **QQQ** PUT 665 2026-11-17 (4DTE): 677 traded vs OI 642
- **QQQ** PUT 642 2026-11-16 (3DTE): 502 traded vs OI 40
- **QQQ** PUT 634 2026-11-16 (3DTE): 505 traded vs OI 46
- **QQQ** CALL 681 2026-11-27 (14DTE): 503 traded vs OI 176
- **IWM** PUT 272 2026-11-27 (14DTE): 916 traded vs OI 371
- **SMH** PUT 470 2026-11-16 (3DTE): 565 traded vs OI 368
- **NVDA** PUT 160 2026-11-23 (10DTE): 506 traded vs OI 415
- **TSLA** PUT 350 2026-11-16 (3DTE): 900 traded vs OI 0
- **TSLA** CALL 385 2026-11-16 (3DTE): 690 traded vs OI 526
- **AMD** PUT 470 2026-11-16 (3DTE): 572 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
