# GEX + FLOW SCAN - Fri Oct 30, 03:20 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (3)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:25 | **COIN** | **PUTS** | FLOW SURGE | 10/30 138P | 0.73 | 0.44 | +25% (7m) | **-40%** (done) | +115% | 137.27 |
| 10:25 | **SMCI** | **PUTS** | FLIP CROSS down into negative gamma | 10/30 32.5P | 0.43 | 0.31 | -12% (1m) | **-28%** (done) | +32% | 32 |
| 10:15 | **AAPL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 10/30 347.5C | 0.50 | 1.24 | +356% (38m) | **+148%** (done) | +104% | 347.56 hit |

## 1m RULES on SPY / QQQ - loose (5 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 15:20:08 ET, last candle SPY 15:19, QQQ 15:19 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 15:02 | SPY | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | no contract: 46 puts 0-1DTE > 2 priced 0.40-0.80 > 2 delta 0.15+ > 2 spread ok > 2 liquid  |
| 12:45 | QQQ | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |
| 12:32 | SPY | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |
| 12:31 | SPY | 1m FAILED POP | R3 R4 | PUTS | TURNING your way | no contract: 45 puts 0-1DTE > 1 priced 0.40-0.80 > 1 delta 0.15+ > 1 spread ok > 1 liquid  |
| 11:05 | SPY | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |

## Flow surges NOT fired - price disagreed (40 today, last 5)
- 12:40 NVDA CALLS: under EMA 20 - flow says one way, price says the other
- 11:20 ARM CALLS: under EMA 20 - flow says one way, price says the other
- 11:20 COIN PUTS: price +0.22 over the last 15 min - flow says one way, price says the other
- 11:15 MSTR PUTS: price +1.54 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 11:10 MSTR PUTS: price +1.77 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **MSFT** | 520.82 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 38 | 10/30 522.5C @ 0.76 (delta 0.32) = est +222% at 525 | POS +$389.0M | 516.51 | 525 | 520 | +$5.9M | +$0 bull / -$353k bear | out (clean 26, ADX 19, RVol 0.8) |
| 2 | **ORCL** | 129.77 | PINNED between the walls (positive gamma) - chop | **-** | 33 | - | POS +$23.0M | 128.9 | 130 | 130 | +$2.8M | +$104k bull / -$257k bear | out (clean 34, ADX 22, RVol 0.6) |
| 3 | **AMD** | 497.52 | - | **-** | 29 | - | NEG -$187.0M | 516.42 | 500 | 500 | +$38.5M | +$34k bull / -$1.2M bear | out (clean 30, ADX 39, RVol 2.5) |
| 4 | **DELL** | 418.34 | - | **-** | 29 | - | NEG -$49.3M | - | 440 | 420 | +$8.2M | +$0 bull / -$209k bear | out (clean 34, ADX 34, RVol 1.8) |
| 5 | **SPY** | 752.35 | - | **-** | 28 | - | NEG -$16.0B | 770.66 | 750 | 750 | +$266.6M | +$0 bull / -$25.4M bear | out (clean 28, ADX 46, RVol 2.5) |
| 6 | **NVDA** | 202.60 | - | **-** | 26 | - | NEG -$415.7M | 210.77 | 210 | 200 | +$29.5M | +$0 bull / -$3.3M bear | out (clean 29, ADX 45, RVol 1.9) |
| 7 | **QQQ** | 686.24 | - | **-** | 25 | - | NEG -$9.6B | - | 720 | 690 | +$148.2M | +$262k bull / -$12.7M bear | out (clean 30, ADX 47, RVol 2.2) |
| 8 | **NFLX** | 61.80 | - | **-** | 25 | - | NEG -$37.6M | 62.98 | 62 | 62 | +$1.5M | +$29k bull / +$0 bear | out (clean 30, ADX 34, RVol 1.1) |
| 9 | **SMH** | 516.31 | - | **-** | 24 | - | NEG -$539.8M | - | 532.5 | 500 | +$4.5M | +$0 bull / -$1.3M bear | out (clean 31, ADX 40, RVol 2.2) |
| 10 | **AAPL** | 343.06 | - | **-** | 23 | - | POS +$148.2M | 341.56 | 345 | 345 | +$12.3M | +$167k bull / -$455k bear | out (clean 32, ADX 38, RVol 1.4) |
| 11 | **MU** | 866.38 | - | **-** | 23 | - | NEG -$244.7M | 883.03 | 880 | 850 | +$72.8M | +$400k bull / -$4.9M bear | out (clean 31, ADX 35, RVol 1.2) |
| 12 | **IWM** | 277.98 | - | **-** | 22 | - | NEG -$1.6B | 280.36 | 278 | 278 | +$10.3M | +$0 bull / -$504k bear | out (clean 30, ADX 39, RVol 1.1) |
| 13 | **AVGO** | 322.32 | - | **-** | 22 | - | NEG -$168.2M | - | 340 | 320 | +$2.2M | +$0 bull / -$369k bear | out (clean 30, ADX 41, RVol 1.2) |
| 14 | **MSTR** | 130.09 | - | **-** | 22 | - | NEG -$24.1M | 135.49 | 135 | 130 | -$9.5M | +$0 bull / -$4.7M bear | out (clean 28, ADX 26, RVol 1.5) |
| 15 | **HOOD** | 82.83 | - | **-** | 22 | - | NEG -$25.0M | - | 85 | 83 | +$2.0M | +$0 bull / -$98k bear | out (clean 31, ADX 42, RVol 0.9) |
| 16 | **META** | 613.51 | - | **-** | 21 | - | NEG -$183.4M | 619.57 | 615 | 610 | +$6.2M | +$106k bull / -$1.3M bear | out (clean 30, ADX 46, RVol 0.4) |
| 17 | **SMCI** | 32.07 | - | **-** | 21 | - | NEG -$4.7M | 32.5 | 35 | 32 | +$158k | +$0 bull / -$278k bear | out (clean 29, ADX 42, RVol 1.3) |
| 18 | **GOOGL** | 277.94 | - | **-** | 20 | - | NEG -$206.7M | - | 280 | 280 | +$2.2M | +$0 bull / -$1.2M bear | out (clean 33, ADX 38, RVol 0.7) |
| 19 | **SHOP** | 155.64 | - | **-** | 20 | - | NEG -$17.4M | - | 150 | 157.5 | +$632k | - | out (clean 28, ADX 31, RVol 2.6) |
| 20 | **TSLA** | 398.36 | - | **-** | 19 | - | POS +$333.8M | 387.04 | 400 | 400 | -$13.2M | +$0 bull / -$6.5M bear | out (clean 30, ADX 27, RVol 1.7) |
| 21 | **BABA** | 97.66 | - | **-** | 19 | - | NEG -$23.7M | 99.47 | 100 | 97 | +$672k | - | out (clean 31, ADX 40, RVol 1.0) |
| 22 | **AMZN** | 239.11 | - | **-** | 17 | - | NEG -$197.8M | 246.41 | 250 | 240 | -$5.6M | +$0 bull / -$1.4M bear | out (clean 30, ADX 15, RVol 1.1) |
| 23 | **PLTR** | 184.93 | - | **-** | 17 | - | NEG -$59.2M | 187.16 | 185 | 185 | +$1.2M | +$0 bull / -$2.9M bear | out (clean 26, ADX 22, RVol 1.0) |
| 24 | **COIN** | 139.16 | - | **-** | 16 | - | NEG -$18.7M | - | 140 | 140 | -$2.9M | - | out (clean 27, ADX 37, RVol 3.5) |
| 25 | **ARM** | 202.99 | - | **-** | 13 | - | NEG -$21.6M | - | 205 | 205 | +$524k | - | out (clean 26, ADX 30, RVol 2.0) |
| 26 | **CRM** | 228.88 | - | **-** | 13 | - | NEG -$26.2M | 237.85 | 230 | 230 | +$352k | - | out (clean 27, ADX 30, RVol 1.2) |
| 27 | **UBER** | 65.03 | - | **-** | 12 | - | NEG -$51.8M | 65.82 | 65 | 65 | +$371k | - | out (clean 26, ADX 16, RVol 0.6) |

## Big prints this scan (159)
- **MSTR** CALL 135 2026-11-06 (7DTE): 5,246 @ 3.79 = **+$2.0M** SELL | vol 21,351 / OI 219
- **SPY** CALL 750 2026-11-03 (4DTE): 1,924 @ 6.44 = **+$1.2M** SELL | vol 19,054 / OI 23
- **MSTR** CALL 135 2026-11-06 (7DTE): 2,500 @ 3.76 = **+$940k** SELL | vol 21,351 / OI 219
- **MSTR** CALL 135 2026-11-06 (7DTE): 2,500 @ 3.76 = **+$940k** SELL | vol 21,351 / OI 219
- **MU** PUT 900 2026-10-30 (0DTE): 200 @ 33.95 = **+$679k** BUY | vol 12,044 / OI 3,632
- **MSTR** CALL 135 2026-11-06 (7DTE): 1,750 @ 3.79 = **+$663k** SELL | vol 21,351 / OI 219
- **QQQ** PUT 695 2026-11-06 (7DTE): 362 @ 17.06 = **+$618k** BUY | vol 10,705 / OI 10,815
- **NVDA** PUT 202.5 2026-11-06 (7DTE): 1,200 @ 4.99 = **+$599k** BUY | vol 10,463 / OI 1,409
- **MU** PUT 900 2026-10-30 (0DTE): 165 @ 34.42 = **+$568k** BUY | vol 12,044 / OI 3,632
- **SPY** PUT 744 2026-11-06 (7DTE): 1,000 @ 5.04 = **+$504k** BUY | vol 3,291 / OI 999
- **MU** PUT 890 2026-10-30 (0DTE): 165 @ 24.50 = **+$404k** BUY | vol 24,182 / OI 1,303
- **SPY** CALL 750 2026-11-03 (4DTE): 500 @ 6.44 = **+$322k** SELL | vol 19,054 / OI 23
- **SPY** CALL 750 2026-11-03 (4DTE): 500 @ 6.44 = **+$322k** SELL | vol 19,054 / OI 23
- **IWM** PUT 276 2026-11-06 (7DTE): 1,015 @ 2.87 = **+$291k** BUY | vol 6,319 / OI 7,139
- **MU** CALL 875 2026-11-06 (7DTE): 100 @ 26.95 = **+$270k** SELL | vol 1,666 / OI 53

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 771 2026-11-04 (5DTE): 1,444 traded vs OI 1,282
- **SPY** PUT 745 2026-10-30 (0DTE): 66,379 traded vs OI 64,012
- **SPY** CALL 778 2026-11-06 (7DTE): 1,935 traded vs OI 1,930
- **SPY** PUT 719 2026-11-13 (14DTE): 593 traded vs OI 313
- **QQQ** PUT 687 2026-11-04 (5DTE): 526 traded vs OI 0
- **IWM** PUT 272 2026-11-06 (7DTE): 4,363 traded vs OI 4,347
- **IWM** PUT 259 2026-11-06 (7DTE): 1,450 traded vs OI 875
- **IWM** PUT 270 2026-11-05 (6DTE): 511 traded vs OI 98
- **SMH** CALL 545 2026-11-02 (3DTE): 527 traded vs OI 33
- **TSLA** CALL 432.5 2026-11-06 (7DTE): 501 traded vs OI 480
- **AAPL** CALL 342.5 2026-11-04 (5DTE): 636 traded vs OI 152
- **AMD** CALL 495 2026-11-02 (3DTE): 579 traded vs OI 0
- **GOOGL** CALL 287.5 2026-11-04 (5DTE): 501 traded vs OI 1
- **NFLX** PUT 58 2026-11-06 (7DTE): 2,317 traded vs OI 1,292
- **AVGO** PUT 292.5 2026-11-06 (7DTE): 1,353 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
