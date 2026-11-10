# GEX + FLOW SCAN - Tue Nov 10, 03:00 PM ET
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
Last 1m check 15:00:08 ET, last candle SPY 14:59, QQQ 14:59 | no errors
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
| 1 | **MSFT** | 534.08 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 36 | none: 126 calls 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (13 contracts' greeks worked out here) | POS +$456.0M | 506.94 | 550 | 535 | +$12.0M | +$0 bull / -$31k bear | out (clean 32, ADX 20, RVol 0.3) |
| 2 | **AAPL** | 348.39 | - | **-** | 22 | - | POS +$434.5M | 336.63 | 350 | 340 | +$17.1M | +$335k bull / +$0 bear | out (clean 28, ADX 15, RVol 0.4) |
| 3 | **AVGO** | 331.56 | - | **-** | 21 | - | NEG -$9.3M | 341.04 | 340 | 340 | -$12.3M | +$0 bull / -$50k bear | out (clean 34, ADX 32, RVol 0.6) |
| 4 | **AMD** | 516.50 | - | **-** | 18 | - | POS +$44.2M | - | 500 | 500 | -$51.8M | +$0 bull / -$777k bear | out (clean 33, ADX 19, RVol 0.6) |
| 5 | **AMZN** | 271.91 | - | **-** | 17 | - | POS +$486.8M | - | 270 | 265 | -$117k | +$0 bull / -$118k bear | out (clean 34, ADX 31, RVol 0.7) |
| 6 | **SPY** | 748.88 | - | **-** | 16 | - | NEG -$6.5B | 760.44 | 750 | 750 | +$14.2M | +$0 bull / -$911k bear | out (clean 32, ADX 30, RVol 0.3) |
| 7 | **NVDA** | 166.90 | - | **-** | 16 | - | NEG -$153.8M | - | 180 | 170 | +$14.2M | +$1.3M bull / -$116k bear | out (clean 33, ADX 15, RVol 1.2) |
| 8 | **QQQ** | 672.63 | - | **-** | 15 | - | NEG -$1.9B | 692.63 | 672 | 680 | -$8.0M | +$0 bull / -$121k bear | out (clean 32, ADX 28, RVol 0.2) |
| 9 | **TSLA** | 378.24 | - | **-** | 15 | - | POS +$208.7M | - | 400 | 380 | -$8.9M | +$717k bull / -$1.1M bear | out (clean 32, ADX 15, RVol 0.5) |
| 10 | **META** | 642.76 | - | **-** | 15 | - | POS +$257.4M | 608.14 | 650 | 650 | -$714k | +$126k bull / -$28k bear | out (clean 32, ADX 21, RVol 0.5) |
| 11 | **DELL** | 331.18 | - | **-** | 15 | - | NEG -$11.1M | - | 350 | 340 | +$911k | +$54k bull / +$0 bear | out (clean 34, ADX 18, RVol 0.2) |
| 12 | **MU** | 713.55 | - | **-** | 15 | - | NEG -$32.7M | - | 750 | 750 | -$23.0M | +$99k bull / -$934k bear | out (clean 31, ADX 18, RVol 0.2) |
| 13 | **ORCL** | 117.17 | - | **-** | 15 | - | NEG -$25.4M | - | 120 | 120 | +$302k | +$0 bull / -$55k bear | out (clean 27, ADX 18, RVol 0.4) |
| 14 | **IWM** | 280.09 | - | **-** | 14 | - | NEG -$975.1M | 283.31 | 280 | 270 | +$1.4M | +$0 bull / -$70k bear | out (clean 35, ADX 19, RVol 0.2) |
| 15 | **CRM** | 210.93 | - | **-** | 12 | - | NEG -$10.8M | - | 195 | 220 | +$311k | - | out (clean 31, ADX 18, RVol 0.5) |
| 16 | **SHOP** | 145.09 | - | **-** | 12 | - | NEG -$250k | 145.4 | 150 | 140 | -$219k | - | out (clean 32, ADX 23, RVol 0.7) |
| 17 | **ARM** | 179.12 | - | **-** | 10 | - | NEG -$5.1M | - | 185 | 185 | -$224k | - | out (clean 27, ADX 19, RVol 0.2) |
| 18 | **UBER** | 69.56 | - | **-** | 9 | - | POS +$6.3M | 68.48 | 70 | 70 | -$68k | - | out (clean 33, ADX 23, RVol 0.2) |
| 19 | **GOOGL** | 287.19 | - | **-** | 8 | - | NEG -$17.4M | 288.77 | 300 | 290 | +$2.3M | - | out (clean 29, ADX 20, RVol 0.3) |
| 20 | **HOOD** | 80.76 | - | **-** | 7 | - | POS +$1.8M | 79.39 | 85 | 80 | +$573k | - | out (clean 32, ADX 18, RVol 0.3) |
| 21 | **BABA** | 102.51 | - | **-** | 7 | - | NEG -$10.2M | 106.26 | 110 | 100 | -$161k | - | out (clean 30, ADX 20, RVol 0.4) |
| 22 | **NFLX** | 62.91 | - | **-** | 6 | - | NEG -$22.6M | 65.14 | 65 | 60 | -$199k | - | out (clean 29, ADX 20, RVol 0.6) |
| 23 | **PLTR** | 166.19 | - | **-** | 6 | - | POS +$52.2M | - | 165 | 170 | -$932k | - | out (clean 28, ADX 16, RVol 0.4) |
| 24 | **COIN** | 131.48 | - | **-** | 5 | - | POS +$2.8M | 129.23 | 137 | 135 | +$173k | - | out (clean 28, ADX 18, RVol 0.3) |
| 25 | **SMCI** | 27.59 | - | **-** | 5 | - | POS +$944k | 26.5 | 30 | 25 | -$45k | - | out (clean 30, ADX 15, RVol 0.6) |
| 26 | **MSTR** | 119.90 | - | **-** | 4 | - | NEG -$26.1M | - | 130 | 110 | +$543k | - | out (clean 29, ADX 11, RVol 0.3) |
| 27 | **SMH** | 481.52 | - | **-** | 3 | - | NEG -$224.9M | - | 500 | 475 | -$134k | - | out (clean 30, ADX 17, RVol 0.1) |

## Big prints this scan (31)
- **TSLA** CALL 377.5 2026-11-11 (1DTE): 398 @ 4.40 = **+$175k** BUY | vol 39,884 / OI 273
- **TSLA** CALL 377.5 2026-11-11 (1DTE): 347 @ 4.40 = **+$153k** BUY | vol 39,884 / OI 273
- **NVDA** CALL 160 2026-11-11 (1DTE): 100 @ 7.85 = **+$78k** BUY | vol 2,813 / OI 34
- **TSLA** CALL 377.5 2026-11-11 (1DTE): 173 @ 4.40 = **+$76k** BUY | vol 39,884 / OI 273
- **TSLA** CALL 377.5 2026-11-11 (1DTE): 172 @ 4.40 = **+$76k** BUY | vol 39,884 / OI 273
- **NVDA** CALL 167.5 2026-11-13 (3DTE): 150 @ 4.40 = **+$66k** BUY | vol 15,531 / OI 18
- **TSLA** CALL 377.5 2026-11-11 (1DTE): 132 @ 4.40 = **+$58k** BUY | vol 39,884 / OI 273
- **AAPL** PUT 347.5 2026-11-11 (1DTE): 320 @ 1.47 = **+$47k** SELL | vol 28,884 / OI 376
- **AAPL** PUT 347.5 2026-11-11 (1DTE): 320 @ 1.47 = **+$47k** SELL | vol 28,884 / OI 376
- **AAPL** PUT 347.5 2026-11-11 (1DTE): 320 @ 1.47 = **+$47k** SELL | vol 28,884 / OI 376
- **AAPL** PUT 347.5 2026-11-11 (1DTE): 320 @ 1.47 = **+$47k** SELL | vol 28,884 / OI 376
- **AAPL** PUT 347.5 2026-11-11 (1DTE): 320 @ 1.47 = **+$47k** SELL | vol 28,884 / OI 376
- **AAPL** PUT 347.5 2026-11-11 (1DTE): 320 @ 1.47 = **+$47k** SELL | vol 28,884 / OI 376
- **NVDA** CALL 172.5 2026-11-11 (1DTE): 480 @ 0.95 = **+$46k** SELL | vol 92,934 / OI 111
- **TSLA** CALL 385 2026-11-13 (3DTE): 100 @ 4.15 = **+$42k** BUY | vol 2,533 / OI 2,088

## New unusual volume (traded more than open interest, 500+)
- **QQQ** CALL 685 2026-11-12 (2DTE): 1,063 traded vs OI 1,008
- **QQQ** PUT 641 2026-11-20 (10DTE): 811 traded vs OI 810
- **TSLA** PUT 387.5 2026-11-11 (1DTE): 520 traded vs OI 118
- **TSLA** PUT 345 2026-11-13 (3DTE): 1,355 traded vs OI 1,144
- **HOOD** CALL 83 2026-11-20 (10DTE): 531 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
