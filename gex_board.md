# GEX + FLOW SCAN - Tue Nov 10, 01:20 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (10)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 12:33 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 667P | 0.67 | 0.78 | +170% (8m) | **+16%** | +15% | 668.83 hit |
| 12:22 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 667P | 0.66 | 0.78 | +174% (19m) | **+18%** | +11% | 669.29 hit |
| 11:18 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 668P | 0.74 | 0.69 | +84% (38m) | **-7%** (done) | +18% | 672.3 hit |
| 11:17 | **SPY** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 744P | 0.60 | 0.36 | +38% (32m) | **-40%** (done) | +41% | 746.01 hit |
| 11:12 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 669P | 0.74 | 1.07 | +135% (44m) | **+45%** (done) | +38% | 671.74 hit |
| 11:12 | **SPY** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 744P | 0.64 | 0.38 | +30% (37m) | **-41%** (done) | +40% | 745.88 |
| 11:06 | **SPY** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 744P | 0.68 | 0.60 | +22% (43m) | **-12%** (done) | +49% | 745.54 |
| 10:15 | **IWM** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/10 280P | 0.63 | 1.39 | +232% (36m) | **+121%** (done) | +22% | 280 hit |
| 09:50 | **SPY** | **PUTS** | FLOW SURGE | 11/10 743P | 0.77 | 0.62 | +21% (60m) | **-19%** (done) | +54% | 745.65 |
| 09:45 | **IWM** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/10 279P | 0.52 | 0.95 | +90% (60m) | **+83%** (done) | +87% | 278.66 |

## 1m RULES on SPY / QQQ - loose (9 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 13:20:08 ET, last candle SPY 13:19, QQQ 13:18 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 12:32 | QQQ | 1m FAILED POP | R3 R4 | PUTS | WITH you | **FIRE** QQQ261110P00667000 |
| 12:21 | QQQ | 1m FAILED POP | R3 R4 | PUTS | TURNING your way | **FIRE** QQQ261110P00667000 |
| 11:23 | QQQ | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |
| 11:17 | QQQ | 1m FAILED POP | R3 R4 | PUTS | TURNING your way | **FIRE** QQQ261110P00668000 |
| 11:16 | SPY | 1m FAILED POP | R3 R4 | PUTS | TURNING your way | **FIRE** SPY261110P00744000 |
| 11:14 | QQQ | 1m FAILED POP | R3 R4 | PUTS | TURNING your way | 5-minute cooldown |
| 11:11 | QQQ | 1m FAILED POP | R3 R4 | PUTS | TURNING your way | **FIRE** QQQ261110P00669000 |
| 11:11 | SPY | 1m FAILED POP | R3 R4 | PUTS | TURNING your way | **FIRE** SPY261110P00744000 |
| 11:05 | SPY | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | **FIRE** SPY261110P00744000 |

## Flow surges NOT fired - price disagreed (6 today, last 5)
- 10:15 BABA PUTS: price +0.24 over the last 15 min - flow says one way, price says the other
- 10:10 BABA PUTS: price +0.73 over the last 15 min - flow says one way, price says the other
- 10:00 NFLX CALLS: price -0.14 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:00 AAPL CALLS: price -2.97 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 09:55 BABA CALLS: price -0.98 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **PLTR** | 165.08 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 36 | none: 14 puts 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$48.5M | - | 165 | 170 | -$496k | +$70k bull / -$27k bear | out (clean 28, ADX 35, RVol 0.5) |
| 2 | **MSFT** | 530.48 | - | **-** | 27 | - | POS +$378.3M | 504.32 | 550 | 500 | +$14.9M | +$33k bull / -$1.3M bear | out (clean 32, ADX 48, RVol 0.5) |
| 3 | **AAPL** | 347.78 | - | **-** | 23 | - | POS +$414.3M | 336.37 | 350 | 340 | +$17.4M | +$0 bull / -$36k bear | out (clean 28, ADX 14, RVol 0.2) |
| 4 | **DELL** | 325.12 | - | **-** | 20 | - | NEG -$10.4M | - | 350 | 340 | +$1.3M | +$293k bull / +$0 bear | out (clean 34, ADX 38, RVol 0.3) |
| 5 | **AMD** | 507.94 | - | **-** | 19 | - | POS +$50.1M | - | 500 | 500 | -$43.1M | +$1.3M bull / -$1.6M bear | out (clean 33, ADX 27, RVol 0.4) |
| 6 | **NVDA** | 167.37 | - | **-** | 18 | - | NEG -$153.2M | - | 180 | 170 | +$9.9M | +$929k bull / -$1.1M bear | out (clean 34, ADX 30, RVol 0.8) |
| 7 | **SPY** | 745.84 | - | **-** | 17 | - | NEG -$8.2B | 760.32 | 750 | 730 | +$62.5M | +$749k bull / -$570k bear | out (clean 32, ADX 28, RVol 0.3) |
| 8 | **MSTR** | 119.94 | - | **-** | 17 | - | NEG -$25.5M | - | 130 | 110 | +$335k | +$0 bull / -$106k bear | out (clean 29, ADX 29, RVol 0.6) |
| 9 | **CRM** | 209.69 | - | **-** | 17 | - | NEG -$10.3M | - | 195 | 220 | +$337k | - | out (clean 30, ADX 41, RVol 0.3) |
| 10 | **QQQ** | 668.91 | - | **-** | 16 | - | NEG -$2.2B | 692.24 | 680 | 680 | +$26.7M | +$582k bull / -$1.2M bear | out (clean 32, ADX 30, RVol 0.2) |
| 11 | **IWM** | 279.51 | - | **-** | 16 | - | NEG -$1.1B | 283.41 | 280 | 270 | +$2.3M | +$75k bull / +$0 bear | out (clean 36, ADX 23, RVol 0.2) |
| 12 | **SHOP** | 143.16 | - | **-** | 16 | - | NEG -$1.3M | 146.72 | 150 | 140 | +$99k | - | out (clean 32, ADX 52, RVol 1.0) |
| 13 | **SMH** | 477.46 | - | **-** | 15 | - | NEG -$233.6M | - | 500 | 475 | +$179k | +$28k bull / +$0 bear | out (clean 30, ADX 25, RVol 0.3) |
| 14 | **TSLA** | 376.09 | - | **-** | 15 | - | POS +$187.8M | - | 400 | 380 | -$4.3M | +$108k bull / -$153k bear | out (clean 32, ADX 20, RVol 0.2) |
| 15 | **META** | 637.75 | - | **-** | 15 | - | POS +$225.3M | 606.23 | 650 | 650 | +$1.4M | +$160k bull / +$0 bear | out (clean 32, ADX 22, RVol 0.4) |
| 16 | **MU** | 705.86 | - | **-** | 15 | - | NEG -$33.5M | - | 750 | 750 | -$7.3M | +$841k bull / -$536k bear | out (clean 30, ADX 23, RVol 0.2) |
| 17 | **ARM** | 177.00 | - | **-** | 13 | - | NEG -$4.5M | - | 185 | 185 | -$205k | - | out (clean 28, ADX 25, RVol 1.2) |
| 18 | **GOOGL** | 286.15 | - | **-** | 12 | - | NEG -$30.5M | 289.14 | 300 | 290 | +$3.4M | - | out (clean 30, ADX 28, RVol 0.3) |
| 19 | **HOOD** | 80.28 | - | **-** | 12 | - | POS +$1.2M | 79.34 | 85 | 80 | +$657k | - | out (clean 31, ADX 39, RVol 0.5) |
| 20 | **BABA** | 102.51 | - | **-** | 12 | - | NEG -$9.9M | 106.41 | 110 | 100 | -$66k | - | out (clean 31, ADX 45, RVol 1.5) |
| 21 | **AMZN** | 268.51 | - | **-** | 10 | - | POS +$454.7M | - | 270 | 265 | +$9.1M | - | out (clean 33, ADX 25, RVol 0.4) |
| 22 | **ORCL** | 116.50 | - | **-** | 10 | - | NEG -$25.2M | - | 120 | 120 | +$507k | - | out (clean 28, ADX 39, RVol 0.1) |
| 23 | **COIN** | 130.96 | - | **-** | 9 | - | POS +$2.5M | 128.85 | 137 | 135 | +$200k | - | out (clean 29, ADX 34, RVol 0.4) |
| 24 | **UBER** | 69.44 | - | **-** | 9 | - | POS +$5.6M | 68.44 | 70 | 70 | -$47k | - | out (clean 33, ADX 30, RVol 0.2) |
| 25 | **SMCI** | 27.47 | - | **-** | 8 | - | POS +$919k | 26.36 | 30 | 25 | -$41k | - | out (clean 30, ADX 35, RVol 0.3) |
| 26 | **AVGO** | 326.21 | - | **-** | 7 | - | NEG -$15.8M | 341.76 | 340 | 320 | -$9.1M | - | out (clean 32, ADX 12, RVol 0.4) |
| 27 | **NFLX** | 62.63 | - | **-** | 6 | - | NEG -$24.9M | 65.86 | 65 | 60 | -$104k | - | out (clean 30, ADX 25, RVol 0.4) |

## Big prints this scan (50)
- **NVDA** CALL 170 2026-11-16 (6DTE): 499 @ 4.35 = **+$217k** BUY | vol 11,092 / OI 394
- **SPY** PUT 747 2026-11-10 (0DTE): 747 @ 1.98 = **+$148k** BUY | vol 354,291 / OI 315
- **QQQ** PUT 670 2026-11-11 (1DTE): 280 @ 4.82 = **+$135k** SELL | vol 31,298 / OI 452
- **QQQ** CALL 668 2026-11-10 (0DTE): 442 @ 2.73 = **+$121k** BUY | vol 21,589 / OI 429
- **AMD** CALL 500 2026-11-11 (1DTE): 73 @ 16.50 = **+$120k** BUY | vol 3,781 / OI 943
- **SPY** PUT 746 2026-11-10 (0DTE): 747 @ 1.43 = **+$107k** BUY | vol 371,741 / OI 242
- **QQQ** PUT 650 2026-11-11 (1DTE): 2,000 @ 0.53 = **+$106k** MID | vol 11,168 / OI 1,648
- **SPY** CALL 744 2026-11-10 (0DTE): 393 @ 2.57 = **+$101k** BUY | vol 15,023 / OI 980
- **NVDA** CALL 160 2026-11-13 (3DTE): 97 @ 9.75 = **+$95k** BUY | vol 1,287 / OI 144
- **AMD** CALL 490 2026-11-13 (3DTE): 30 @ 28.45 = **+$85k** BUY | vol 731 / OI 1,487
- **AMD** CALL 500 2026-11-11 (1DTE): 48 @ 16.50 = **+$79k** BUY | vol 3,781 / OI 943
- **MSTR** PUT 125 2026-11-13 (3DTE): 100 @ 7.56 = **+$76k** BUY | vol 2,642 / OI 5,777
- **NVDA** PUT 170 2026-11-11 (1DTE): 163 @ 4.30 = **+$70k** SELL | vol 127,552 / OI 4,288
- **NVDA** CALL 167.5 2026-11-11 (1DTE): 200 @ 3.15 = **+$63k** BUY | vol 53,179 / OI 80
- **AMD** CALL 490 2026-11-13 (3DTE): 19 @ 28.45 = **+$54k** BUY | vol 731 / OI 1,487

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 766 2026-11-17 (7DTE): 500 traded vs OI 173
- **SPY** CALL 745 2026-11-27 (17DTE): 716 traded vs OI 683
- **QQQ** PUT 654 2026-11-13 (3DTE): 620 traded vs OI 617
- **QQQ** PUT 660 2026-11-23 (13DTE): 504 traded vs OI 0
- **IWM** PUT 277 2026-11-16 (6DTE): 745 traded vs OI 291
- **IWM** PUT 276 2026-11-16 (6DTE): 528 traded vs OI 87
- **IWM** PUT 276 2026-11-17 (7DTE): 580 traded vs OI 64
- **SMH** PUT 445 2026-11-11 (1DTE): 667 traded vs OI 186
- **NVDA** CALL 160 2026-11-16 (6DTE): 536 traded vs OI 19
- **NVDA** PUT 157.5 2026-11-18 (8DTE): 2,543 traded vs OI 6
- **AAPL** PUT 345 2026-11-27 (17DTE): 669 traded vs OI 649
- **DELL** CALL 330 2026-11-13 (3DTE): 513 traded vs OI 105
- **MU** CALL 717.5 2026-11-13 (3DTE): 500 traded vs OI 338

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
