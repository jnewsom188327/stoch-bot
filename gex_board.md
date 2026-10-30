# GEX + FLOW SCAN - Fri Oct 30, 03:00 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (3)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:25 | **COIN** | **PUTS** | FLOW SURGE | 10/30 138P | 0.73 | 0.44 | +25% (7m) | **-40%** (done) | +115% | 137.27 |
| 10:25 | **SMCI** | **PUTS** | FLIP CROSS down into negative gamma | 10/30 32.5P | 0.43 | 0.31 | -12% (1m) | **-28%** (done) | +32% | 32 |
| 10:15 | **AAPL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 10/30 347.5C | 0.50 | 1.24 | +356% (38m) | **+148%** (done) | +104% | 347.56 hit |

## 1m RULES on SPY / QQQ - loose (4 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 15:00:08 ET, last candle SPY 14:59, QQQ 14:59 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
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
| 1 | **MSFT** | 519.79 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 39 | none: 164 calls 0-7DTE > 9 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only -53% at the target (needs +20%) (69 contracts' greeks worked out here) | POS +$246.8M | 517.38 | 525 | 520 | +$6.8M | +$338k bull / -$145k bear | out (clean 26, ADX 20, RVol 0.6) |
| 2 | **ORCL** | 130.15 | PINNED between the walls (positive gamma) - chop | **-** | 33 | - | POS +$49.2M | 128.82 | 130 | 130 | +$2.7M | +$540k bull / -$216k bear | out (clean 34, ADX 25, RVol 0.6) |
| 3 | **SPY** | 752.06 | - | **-** | 29 | - | NEG -$17.0B | 772.29 | 750 | 750 | +$326.9M | +$31.4M bull / -$28.2M bear | out (clean 28, ADX 56, RVol 2.5) |
| 4 | **AMD** | 495.42 | - | **-** | 29 | - | NEG -$174.8M | 518.96 | 500 | 500 | +$40.9M | +$2.1M bull / -$1.6M bear | out (clean 30, ADX 45, RVol 1.9) |
| 5 | **SMH** | 514.96 | - | **-** | 28 | - | NEG -$645.7M | - | 532.5 | 505 | +$8.9M | +$238k bull / -$812k bear | out (clean 31, ADX 51, RVol 2.1) |
| 6 | **NVDA** | 202.12 | - | **-** | 27 | - | NEG -$464.8M | 212.35 | 210 | 200 | +$36.8M | +$1.7M bull / -$3.8M bear | out (clean 29, ADX 57, RVol 1.5) |
| 7 | **QQQ** | 685.64 | - | **-** | 26 | - | NEG -$9.7B | - | 720 | 690 | +$199.6M | +$11.7M bull / -$5.2M bear | out (clean 30, ADX 57, RVol 1.9) |
| 8 | **COIN** | 138.38 | - | **-** | 25 | - | NEG -$14.6M | - | 140 | 140 | -$1.6M | +$2.1M bull / +$0 bear | out (clean 28, ADX 46, RVol 3.4) |
| 9 | **SMCI** | 31.79 | - | **-** | 25 | - | NEG -$5.2M | 32.9 | 32 | 32 | +$626k | +$0 bull / -$232k bear | out (clean 29, ADX 46, RVol 1.2) |
| 10 | **MU** | 867.32 | - | **-** | 25 | - | NEG -$338.0M | 913.63 | 880 | 850 | +$78.3M | +$1.6M bull / -$2.3M bear | out (clean 31, ADX 44, RVol 0.7) |
| 11 | **HOOD** | 82.52 | - | **-** | 25 | - | NEG -$34.4M | - | 85 | 83 | +$2.5M | +$64k bull / +$0 bear | out (clean 32, ADX 52, RVol 1.2) |
| 12 | **IWM** | 277.52 | - | **-** | 24 | - | NEG -$1.6B | 281 | 278 | 278 | +$13.6M | +$0 bull / -$182k bear | out (clean 30, ADX 49, RVol 0.8) |
| 13 | **NFLX** | 61.74 | - | **-** | 24 | - | NEG -$41.3M | 62.78 | 62 | 61 | +$1.5M | +$43k bull / +$0 bear | out (clean 30, ADX 30, RVol 0.8) |
| 14 | **AVGO** | 321.21 | - | **-** | 24 | - | NEG -$176.3M | - | 340 | 320 | +$3.5M | +$27k bull / -$363k bear | out (clean 30, ADX 51, RVol 1.0) |
| 15 | **AAPL** | 343.26 | - | **-** | 23 | - | POS +$150.4M | 341.87 | 345 | 345 | +$13.3M | +$2.7M bull / -$317k bear | out (clean 32, ADX 40, RVol 1.3) |
| 16 | **GOOGL** | 277.59 | - | **-** | 23 | - | NEG -$229.8M | - | 280 | 280 | +$4.9M | +$573k bull / +$0 bear | out (clean 33, ADX 43, RVol 0.7) |
| 17 | **META** | 612.95 | - | **-** | 22 | - | NEG -$200.6M | 619.46 | 615 | 610 | +$10.1M | +$1.8M bull / -$56k bear | out (clean 30, ADX 48, RVol 0.4) |
| 18 | **DELL** | 417.27 | - | **-** | 22 | - | NEG -$52.3M | - | 440 | 425 | +$9.9M | - | out (clean 34, ADX 40, RVol 1.2) |
| 19 | **SHOP** | 155.54 | - | **-** | 21 | - | NEG -$17.3M | 162.92 | 155 | 157.5 | +$657k | - | out (clean 28, ADX 36, RVol 2.7) |
| 20 | **BABA** | 97.78 | - | **-** | 21 | - | NEG -$52.9M | 99.98 | 100 | 98 | +$708k | - | out (clean 31, ADX 42, RVol 1.0) |
| 21 | **PLTR** | 184.56 | - | **-** | 18 | - | NEG -$75.8M | 192.09 | 185 | 185 | +$2.2M | +$235k bull / -$2.3M bear | out (clean 26, ADX 27, RVol 0.7) |
| 22 | **TSLA** | 396.55 | - | **-** | 17 | - | POS +$350.3M | 391.1 | 395 | 395 | -$841k | +$0 bull / -$8.2M bear | out (clean 30, ADX 28, RVol 1.2) |
| 23 | **AMZN** | 238.37 | - | **-** | 16 | - | NEG -$192.9M | 245.67 | 250 | 240 | -$2.5M | +$2.3M bull / -$172k bear | out (clean 30, ADX 14, RVol 1.4) |
| 24 | **ARM** | 200.79 | - | **-** | 16 | - | NEG -$19.3M | - | 220 | 200 | +$833k | - | out (clean 26, ADX 35, RVol 2.0) |
| 25 | **CRM** | 228.59 | - | **-** | 13 | - | NEG -$24.5M | 233.85 | 230 | 230 | +$335k | - | out (clean 27, ADX 28, RVol 1.1) |
| 26 | **UBER** | 65.14 | - | **-** | 12 | - | NEG -$37.2M | 66.33 | 65 | 65 | +$338k | - | out (clean 26, ADX 16, RVol 0.5) |
| 27 | **MSTR** | 128.94 | - | **-** | 9 | - | NEG -$29.8M | - | 135 | 130 | -$2.2M | - | out (clean 28, ADX 30, RVol 1.2) |

## Big prints this scan (129)
- **SPY** PUT 780 2026-11-06 (7DTE): 728 @ 28.38 = **+$2.1M** BUY | vol 2,292 / OI 1,351
- **AMD** CALL 520 2026-11-06 (7DTE): 500 @ 15.30 = **+$765k** BUY | vol 1,710 / OI 581
- **TSLA** PUT 405 2026-11-06 (7DTE): 500 @ 15.10 = **+$755k** BUY | vol 3,069 / OI 816
- **QQQ** PUT 685 2026-11-03 (4DTE): 800 @ 8.04 = **+$643k** BUY | vol 8,536 / OI 2,236
- **AMD** CALL 520 2026-11-06 (7DTE): 322 @ 15.60 = **+$502k** BUY | vol 1,710 / OI 581
- **SPY** PUT 780 2026-11-06 (7DTE): 148 @ 28.48 = **+$422k** BUY | vol 2,292 / OI 1,351
- **QQQ** PUT 690 2026-10-30 (0DTE): 733 @ 5.45 = **+$399k** BUY | vol 302,372 / OI 65,738
- **QQQ** PUT 708 2026-10-30 (0DTE): 150 @ 23.16 = **+$347k** BUY | vol 3,256 / OI 2,673
- **QQQ** CALL 685 2026-11-06 (7DTE): 247 @ 12.66 = **+$313k** MID | vol 2,518 / OI 153
- **QQQ** CALL 685 2026-11-06 (7DTE): 247 @ 12.66 = **+$313k** MID | vol 2,518 / OI 153
- **QQQ** PUT 690 2026-10-30 (0DTE): 579 @ 5.40 = **+$313k** BUY | vol 302,372 / OI 65,738
- **AAPL** PUT 345 2026-11-06 (7DTE): 341 @ 9.10 = **+$310k** SELL | vol 3,069 / OI 3,868
- **AMD** CALL 520 2026-11-06 (7DTE): 177 @ 15.60 = **+$276k** BUY | vol 1,710 / OI 581
- **SPY** PUT 755 2026-11-02 (3DTE): 400 @ 6.28 = **+$251k** BUY | vol 44,204 / OI 1,591
- **SPY** PUT 770 2026-11-04 (5DTE): 130 @ 18.89 = **+$246k** BUY | vol 767 / OI 859

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 748 2026-11-02 (3DTE): 516 traded vs OI 7
- **SPY** CALL 749 2026-11-02 (3DTE): 559 traded vs OI 54
- **SPY** CALL 789 2026-11-02 (3DTE): 713 traded vs OI 128
- **SPY** PUT 685 2026-11-03 (4DTE): 834 traded vs OI 63
- **SPY** CALL 750 2026-11-04 (5DTE): 686 traded vs OI 16
- **SPY** PUT 726 2026-11-03 (4DTE): 503 traded vs OI 37
- **SPY** CALL 787 2026-11-03 (4DTE): 2,601 traded vs OI 2,252
- **SPY** PUT 713 2026-11-20 (21DTE): 1,567 traded vs OI 1,466
- **SPY** PUT 745 2026-11-06 (7DTE): 18,167 traded vs OI 11,908
- **SPY** PUT 718 2026-11-13 (14DTE): 519 traded vs OI 456
- **SPY** PUT 737 2026-11-06 (7DTE): 1,251 traded vs OI 971
- **SPY** CALL 781 2026-11-06 (7DTE): 1,600 traded vs OI 1,377
- **QQQ** PUT 677 2026-11-06 (7DTE): 569 traded vs OI 452
- **QQQ** CALL 670 2026-11-02 (3DTE): 524 traded vs OI 51
- **QQQ** PUT 625 2026-11-03 (4DTE): 535 traded vs OI 370

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
