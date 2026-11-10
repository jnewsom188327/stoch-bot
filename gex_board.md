# GEX + FLOW SCAN - Tue Nov 10, 02:00 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (10)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 12:33 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 667P | 0.67 | 0.28 | +170% (8m) | **-58%** (done) | +15% | 668.83 hit |
| 12:22 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 667P | 0.66 | 0.79 | +174% (19m) | **+20%** (done) | +11% | 669.29 hit |
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
Last 1m check 14:00:08 ET, last candle SPY 13:59, QQQ 13:59 | no errors
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
| 1 | **MSFT** | 533.92 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 42 | none: 126 calls 0-7DTE > 8 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (11 contracts' greeks worked out here) | POS +$449.7M | 503.74 | 550 | 535 | +$12.5M | +$0 bull / -$287k bear | out (clean 32, ADX 39, RVol 0.6) |
| 2 | **AMZN** | 269.75 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 36 | 11/11 265P @ 0.69 (delta 0.20) = est +32% at 268.42 | POS +$466.0M | - | 270 | 265 | +$6.9M | +$106k bull / -$26k bear | out (clean 32, ADX 20, RVol 0.6) |
| 3 | **SHOP** | 144.57 | - | **-** | 23 | - | NEG -$258k | 144.97 | 150 | 140 | -$192k | +$0 bull / -$221k bear | out (clean 33, ADX 33, RVol 0.5) |
| 4 | **AAPL** | 348.12 | - | **-** | 22 | - | POS +$424.1M | 336.16 | 350 | 340 | +$17.2M | +$0 bull / -$25k bear | out (clean 28, ADX 11, RVol 0.3) |
| 5 | **BABA** | 102.64 | - | **-** | 20 | - | NEG -$9.5M | 106.15 | 110 | 100 | -$154k | +$0 bull / -$28k bear | out (clean 31, ADX 39, RVol 0.5) |
| 6 | **AVGO** | 329.67 | - | **-** | 18 | - | NEG -$12.2M | 342.68 | 340 | 320 | -$10.5M | +$0 bull / -$121k bear | out (clean 33, ADX 16, RVol 0.4) |
| 7 | **AMD** | 513.25 | - | **-** | 17 | - | POS +$51.6M | - | 500 | 500 | -$49.5M | +$0 bull / -$1.0M bear | out (clean 33, ADX 20, RVol 0.3) |
| 8 | **NVDA** | 167.87 | - | **-** | 16 | - | NEG -$157.6M | - | 180 | 170 | +$7.3M | +$878k bull / -$662k bear | out (clean 34, ADX 20, RVol 0.8) |
| 9 | **PLTR** | 165.78 | - | **-** | 16 | - | POS +$51.3M | - | 165 | 170 | -$808k | +$0 bull / -$50k bear | out (clean 28, ADX 22, RVol 0.2) |
| 10 | **SPY** | 747.80 | - | **-** | 15 | - | NEG -$7.2B | 759.99 | 750 | 730 | +$43.6M | +$0 bull / -$1.3M bear | out (clean 32, ADX 21, RVol 0.3) |
| 11 | **IWM** | 280.06 | - | **-** | 15 | - | NEG -$1.0B | 283.44 | 280 | 270 | +$2.0M | +$54k bull / +$0 bear | out (clean 36, ADX 16, RVol 0.4) |
| 12 | **MU** | 712.36 | - | **-** | 15 | - | NEG -$32.6M | - | 750 | 750 | -$17.3M | +$0 bull / -$1.5M bear | out (clean 30, ADX 18, RVol 0.2) |
| 13 | **QQQ** | 671.26 | - | **-** | 14 | - | NEG -$2.0B | 692.58 | 680 | 680 | +$1.3M | +$102k bull / -$4.7M bear | out (clean 32, ADX 23, RVol 0.1) |
| 14 | **META** | 639.07 | - | **-** | 14 | - | POS +$238.3M | 607.19 | 650 | 650 | +$240k | +$0 bull / -$146k bear | out (clean 32, ADX 18, RVol 0.3) |
| 15 | **CRM** | 211.20 | - | **-** | 14 | - | NEG -$10.8M | - | 195 | 220 | +$302k | - | out (clean 30, ADX 31, RVol 0.3) |
| 16 | **TSLA** | 377.08 | - | **-** | 13 | - | POS +$195.8M | - | 400 | 380 | -$4.6M | +$58k bull / -$200k bear | out (clean 32, ADX 13, RVol 0.2) |
| 17 | **ARM** | 178.55 | - | **-** | 12 | - | NEG -$4.9M | - | 185 | 185 | -$220k | - | out (clean 28, ADX 19, RVol 1.4) |
| 18 | **GOOGL** | 286.68 | - | **-** | 11 | - | NEG -$24.8M | 289.01 | 300 | 290 | +$3.2M | - | out (clean 30, ADX 29, RVol 0.4) |
| 19 | **HOOD** | 80.65 | - | **-** | 10 | - | POS +$1.5M | 79.48 | 85 | 80 | +$647k | - | out (clean 31, ADX 31, RVol 0.3) |
| 20 | **UBER** | 69.31 | - | **-** | 9 | - | POS +$5.1M | 68.37 | 70 | 70 | -$46k | - | out (clean 33, ADX 30, RVol 0.4) |
| 21 | **DELL** | 329.12 | - | **-** | 7 | - | NEG -$11.0M | - | 350 | 340 | +$1.1M | - | out (clean 34, ADX 27, RVol 0.3) |
| 22 | **ORCL** | 117.23 | - | **-** | 7 | - | NEG -$25.3M | - | 120 | 120 | +$258k | - | out (clean 28, ADX 30, RVol 0.2) |
| 23 | **NFLX** | 62.73 | - | **-** | 6 | - | NEG -$23.3M | 65.09 | 65 | 60 | -$136k | - | out (clean 29, ADX 20, RVol 0.3) |
| 24 | **COIN** | 131.30 | - | **-** | 6 | - | POS +$2.6M | 129.07 | 137 | 135 | +$155k | - | out (clean 29, ADX 21, RVol 0.1) |
| 25 | **SMCI** | 27.63 | - | **-** | 6 | - | POS +$1.1M | 26.35 | 30 | 25 | -$62k | - | out (clean 30, ADX 26, RVol 0.3) |
| 26 | **MSTR** | 120.59 | - | **-** | 5 | - | NEG -$21.2M | - | 132 | 110 | +$293k | - | out (clean 30, ADX 19, RVol 0.5) |
| 27 | **SMH** | 480.60 | - | **-** | 4 | - | NEG -$225.6M | - | 500 | 475 | +$71k | - | out (clean 30, ADX 20, RVol 0.2) |

## Big prints this scan (41)
- **QQQ** PUT 670 2026-11-10 (0DTE): 2,000 @ 1.16 = **+$232k** BUY | vol 319,746 / OI 387
- **QQQ** PUT 670 2026-11-11 (1DTE): 499 @ 4.30 = **+$215k** BUY | vol 40,262 / OI 452
- **QQQ** PUT 670 2026-11-11 (1DTE): 480 @ 4.43 = **+$213k** BUY | vol 40,262 / OI 452
- **QQQ** PUT 673 2026-11-10 (0DTE): 590 @ 3.05 = **+$180k** BUY | vol 143,214 / OI 98
- **QQQ** PUT 670 2026-11-11 (1DTE): 404 @ 4.25 = **+$172k** BUY | vol 40,262 / OI 452
- **QQQ** PUT 670 2026-11-11 (1DTE): 293 @ 4.28 = **+$125k** BUY | vol 40,262 / OI 452
- **SPY** CALL 748 2026-11-13 (3DTE): 250 @ 4.66 = **+$116k** SELL | vol 7,430 / OI 1,196
- **QQQ** PUT 673 2026-11-10 (0DTE): 343 @ 3.05 = **+$105k** BUY | vol 143,214 / OI 98
- **MU** PUT 715 2026-11-11 (1DTE): 50 @ 17.80 = **+$89k** BUY | vol 7,324 / OI 81
- **NVDA** CALL 170 2026-11-11 (1DTE): 325 @ 2.01 = **+$65k** BUY | vol 115,971 / OI 252
- **MSFT** PUT 532.5 2026-11-13 (3DTE): 100 @ 6.00 = **+$60k** BUY | vol 979 / OI 756
- **MU** CALL 700 2026-11-11 (1DTE): 25 @ 19.75 = **+$49k** SELL | vol 3,200 / OI 348
- **MU** PUT 705 2026-11-11 (1DTE): 40 @ 12.30 = **+$49k** BUY | vol 6,343 / OI 134
- **MU** CALL 700 2026-11-11 (1DTE): 25 @ 19.40 = **+$48k** SELL | vol 3,200 / OI 348
- **AMZN** CALL 270 2026-11-11 (1DTE): 199 @ 2.22 = **+$44k** BUY | vol 22,398 / OI 1,320

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 804 2026-11-13 (3DTE): 960 traded vs OI 853
- **SPY** CALL 746 2026-11-20 (10DTE): 745 traded vs OI 682
- **IWM** PUT 275 2026-11-12 (2DTE): 596 traded vs OI 303
- **TSLA** CALL 377.5 2026-11-27 (17DTE): 504 traded vs OI 0
- **TSLA** CALL 385 2026-11-13 (3DTE): 2,091 traded vs OI 2,088
- **AMZN** CALL 287.5 2026-11-13 (3DTE): 1,076 traded vs OI 284
- **AMZN** PUT 275 2026-11-13 (3DTE): 522 traded vs OI 84
- **HOOD** PUT 81 2026-11-13 (3DTE): 1,655 traded vs OI 1,603
- **UBER** CALL 76 2026-11-13 (3DTE): 564 traded vs OI 563

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
