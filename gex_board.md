# GEX + FLOW SCAN - Tue Nov 10, 01:10 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (10)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 12:33 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 667P | 0.67 | 0.73 | +170% (8m) | **+9%** | +15% | 668.83 hit |
| 12:22 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 667P | 0.66 | 0.73 | +174% (19m) | **+11%** | +11% | 669.29 hit |
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
Last 1m check 13:10:08 ET, last candle SPY 13:09, QQQ 13:09 | no errors
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
| 1 | **PLTR** | 164.96 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 38 | none: 14 puts 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$48.6M | - | 165 | 160 | -$537k | +$70k bull / -$37k bear | out (clean 28, ADX 36, RVol 0.8) |
| 2 | **HOOD** | 80.19 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 30 | none: 16 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$1.4M | 79.22 | 85 | 80 | +$650k | - | out (clean 31, ADX 39, RVol 0.5) |
| 3 | **MSFT** | 531.50 | - | **-** | 28 | - | POS +$389.0M | 503.05 | 550 | 500 | +$14.4M | +$0 bull / -$2.4M bear | out (clean 32, ADX 47, RVol 1.2) |
| 4 | **AAPL** | 347.81 | - | **-** | 23 | - | POS +$413.4M | 336.62 | 350 | 340 | +$17.6M | +$0 bull / -$36k bear | out (clean 28, ADX 14, RVol 0.4) |
| 5 | **AMZN** | 268.65 | - | **-** | 21 | - | POS +$456.2M | - | 270 | 265 | +$8.7M | +$0 bull / -$87k bear | out (clean 33, ADX 25, RVol 0.7) |
| 6 | **DELL** | 325.18 | - | **-** | 21 | - | NEG -$10.5M | - | 350 | 340 | +$987k | +$0 bull / -$27k bear | out (clean 34, ADX 39, RVol 0.8) |
| 7 | **AMD** | 508.00 | - | **-** | 20 | - | POS +$47.4M | - | 500 | 500 | -$46.5M | +$0 bull / -$4.8M bear | out (clean 33, ADX 29, RVol 0.9) |
| 8 | **NVDA** | 168.02 | - | **-** | 18 | - | NEG -$156.8M | - | 180 | 170 | +$9.6M | +$0 bull / -$2.5M bear | out (clean 34, ADX 33, RVol 0.9) |
| 9 | **SPY** | 746.25 | - | **-** | 17 | - | NEG -$7.7B | 759.78 | 750 | 730 | +$59.6M | +$0 bull / -$2.7M bear | out (clean 32, ADX 29, RVol 0.3) |
| 10 | **QQQ** | 669.32 | - | **-** | 17 | - | NEG -$2.1B | 692.3 | 680 | 680 | +$18.3M | +$0 bull / -$3.0M bear | out (clean 32, ADX 32, RVol 0.2) |
| 11 | **AVGO** | 327.28 | - | **-** | 17 | - | NEG -$15.8M | 344.06 | 340 | 320 | -$9.5M | +$0 bull / -$120k bear | out (clean 32, ADX 14, RVol 0.5) |
| 12 | **MSTR** | 119.86 | - | **-** | 17 | - | NEG -$25.6M | - | 130 | 110 | +$126k | +$0 bull / -$30k bear | out (clean 29, ADX 31, RVol 0.8) |
| 13 | **CRM** | 210.21 | - | **-** | 17 | - | NEG -$10.6M | - | 195 | 220 | +$325k | - | out (clean 30, ADX 40, RVol 0.5) |
| 14 | **IWM** | 279.50 | - | **-** | 16 | - | NEG -$1.2B | 283.63 | 280 | 270 | +$2.4M | +$93k bull / -$60k bear | out (clean 36, ADX 24, RVol 0.3) |
| 15 | **SMH** | 478.36 | - | **-** | 15 | - | NEG -$229.4M | - | 500 | 475 | -$12k | +$0 bull / -$34k bear | out (clean 30, ADX 27, RVol 0.3) |
| 16 | **TSLA** | 375.66 | - | **-** | 15 | - | POS +$190.0M | - | 400 | 380 | -$4.2M | +$52k bull / -$805k bear | out (clean 32, ADX 21, RVol 0.3) |
| 17 | **META** | 638.47 | - | **-** | 15 | - | POS +$228.3M | 604.26 | 650 | 650 | +$655k | +$120k bull / +$0 bear | out (clean 32, ADX 20, RVol 0.5) |
| 18 | **MU** | 706.39 | - | **-** | 15 | - | NEG -$33.6M | - | 750 | 750 | -$9.3M | +$28k bull / -$2.3M bear | out (clean 30, ADX 25, RVol 0.2) |
| 19 | **GOOGL** | 286.15 | - | **-** | 12 | - | NEG -$32.7M | 289.22 | 300 | 290 | +$3.4M | - | out (clean 30, ADX 27, RVol 0.3) |
| 20 | **ARM** | 177.03 | - | **-** | 12 | - | NEG -$4.3M | - | 185 | 185 | -$206k | - | out (clean 28, ADX 27, RVol 0.5) |
| 21 | **SHOP** | 142.96 | - | **-** | 12 | - | NEG -$1.8M | 148.31 | 150 | 140 | +$20k | - | out (clean 32, ADX 56, RVol 0.9) |
| 22 | **BABA** | 102.51 | - | **-** | 11 | - | NEG -$9.6M | 106.17 | 110 | 100 | -$78k | - | out (clean 31, ADX 44, RVol 1.1) |
| 23 | **ORCL** | 116.38 | - | **-** | 10 | - | NEG -$24.4M | - | 120 | 120 | +$498k | - | out (clean 28, ADX 39, RVol 0.2) |
| 24 | **COIN** | 130.73 | - | **-** | 9 | - | POS +$1.7M | 129.42 | 137 | 135 | +$192k | - | out (clean 29, ADX 37, RVol 0.4) |
| 25 | **UBER** | 69.48 | - | **-** | 9 | - | POS +$5.7M | 68.42 | 70 | 70 | -$50k | - | out (clean 33, ADX 30, RVol 0.2) |
| 26 | **SMCI** | 27.47 | - | **-** | 8 | - | POS +$978k | 26.29 | 30 | 25 | -$27k | - | out (clean 30, ADX 36, RVol 0.4) |
| 27 | **NFLX** | 62.67 | - | **-** | 6 | - | NEG -$23.9M | 65.64 | 65 | 60 | -$91k | - | out (clean 30, ADX 23, RVol 0.5) |

## Big prints this scan (67)
- **QQQ** PUT 674 2026-11-10 (0DTE): 779 @ 5.30 = **+$413k** BUY | vol 107,244 / OI 221
- **QQQ** PUT 671 2026-11-11 (1DTE): 499 @ 6.04 = **+$301k** BUY | vol 14,714 / OI 170
- **QQQ** PUT 671 2026-11-11 (1DTE): 500 @ 5.80 = **+$290k** BUY | vol 14,714 / OI 170
- **NVDA** CALL 167.5 2026-11-13 (3DTE): 500 @ 4.70 = **+$235k** SELL | vol 11,357 / OI 18
- **SPY** CALL 745 2026-11-10 (0DTE): 1,042 @ 2.05 = **+$214k** SELL | vol 38,627 / OI 1,171
- **QQQ** PUT 672 2026-11-10 (0DTE): 500 @ 3.55 = **+$178k** BUY | vol 139,011 / OI 153
- **MU** PUT 705 2026-11-16 (6DTE): 50 @ 28.45 = **+$142k** BUY | vol 93 / OI 215
- **MSFT** PUT 535 2026-11-11 (1DTE): 150 @ 7.84 = **+$118k** BUY | vol 11,439 / OI 406
- **AMD** CALL 500 2026-11-13 (3DTE): 56 @ 20.60 = **+$115k** SELL | vol 4,191 / OI 2,434
- **SPY** PUT 745 2026-11-16 (6DTE): 182 @ 5.61 = **+$102k** BUY | vol 1,905 / OI 441
- **AMD** CALL 500 2026-11-13 (3DTE): 47 @ 20.60 = **+$97k** SELL | vol 4,191 / OI 2,434
- **AMD** CALL 510 2026-11-11 (1DTE): 100 @ 9.60 = **+$96k** SELL | vol 12,929 / OI 407
- **MSFT** PUT 532.5 2026-11-11 (1DTE): 150 @ 6.33 = **+$95k** BUY | vol 4,008 / OI 329
- **AMD** PUT 527.5 2026-11-16 (6DTE): 30 @ 31.20 = **+$94k** BUY | vol 87 / OI 0
- **MSFT** PUT 527.5 2026-11-13 (3DTE): 150 @ 6.10 = **+$92k** BUY | vol 625 / OI 719

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 784 2026-11-12 (2DTE): 641 traded vs OI 198
- **SPY** CALL 743 2026-11-11 (1DTE): 559 traded vs OI 442
- **SPY** CALL 750 2026-11-13 (3DTE): 11,276 traded vs OI 11,163
- **SPY** CALL 751 2026-11-20 (10DTE): 1,121 traded vs OI 1,006
- **SPY** PUT 720 2026-11-17 (7DTE): 578 traded vs OI 507
- **SPY** PUT 750 2026-11-24 (14DTE): 504 traded vs OI 0
- **QQQ** CALL 692 2026-11-11 (1DTE): 1,153 traded vs OI 1,122
- **QQQ** PUT 610 2026-11-11 (1DTE): 620 traded vs OI 396
- **QQQ** PUT 666 2026-11-12 (2DTE): 500 traded vs OI 180
- **QQQ** CALL 671 2026-11-12 (2DTE): 518 traded vs OI 221
- **SMH** PUT 472.5 2026-11-11 (1DTE): 514 traded vs OI 18
- **PLTR** CALL 180 2026-11-13 (3DTE): 3,976 traded vs OI 3,962
- **ORCL** CALL 126 2026-11-13 (3DTE): 645 traded vs OI 639

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
