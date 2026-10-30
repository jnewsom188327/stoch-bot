# GEX + FLOW SCAN - Fri Oct 30, 03:10 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (3)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:25 | **COIN** | **PUTS** | FLOW SURGE | 10/30 138P | 0.73 | 0.44 | +25% (7m) | **-40%** (done) | +115% | 137.27 |
| 10:25 | **SMCI** | **PUTS** | FLIP CROSS down into negative gamma | 10/30 32.5P | 0.43 | 0.31 | -12% (1m) | **-28%** (done) | +32% | 32 |
| 10:15 | **AAPL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 10/30 347.5C | 0.50 | 1.24 | +356% (38m) | **+148%** (done) | +104% | 347.56 hit |

## 1m RULES on SPY / QQQ - loose (5 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 15:10:08 ET, last candle SPY 15:09, QQQ 15:09 | no errors
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
| 1 | **MSFT** | 519.92 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 37 | none: 164 calls 0-7DTE > 8 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only -64% at the target (needs +20%) (85 contracts' greeks worked out here) | POS +$301.0M | 516.05 | 525 | 520 | +$6.6M | +$0 bull / -$27k bear | out (clean 26, ADX 20, RVol 0.5) |
| 2 | **TSLA** | 399.31 | PINNED between the walls (positive gamma) - chop | **-** | 35 | - | POS +$398.1M | 392.2 | 400 | 400 | -$9.9M | +$0 bull / -$6.4M bear | out (clean 30, ADX 27, RVol 1.4) |
| 3 | **ORCL** | 130.04 | PINNED between the walls (positive gamma) - chop | **-** | 32 | - | POS +$5.9M | 129.6 | 130 | 130 | +$2.6M | +$478k bull / -$154k bear | out (clean 34, ADX 24, RVol 0.5) |
| 4 | **AMD** | 496.78 | - | **-** | 30 | - | NEG -$186.4M | 516.41 | 500 | 500 | +$41.0M | +$2.0M bull / -$463k bear | out (clean 30, ADX 43, RVol 2.3) |
| 5 | **SPY** | 753.16 | - | **-** | 28 | - | NEG -$15.0B | 765.86 | 800 | 750 | +$291.4M | +$652k bull / -$22.7M bear | out (clean 28, ADX 52, RVol 2.3) |
| 6 | **SMH** | 516.88 | - | **-** | 27 | - | NEG -$648.2M | - | 532.5 | 520 | +$6.8M | +$0 bull / -$259k bear | out (clean 31, ADX 46, RVol 2.4) |
| 7 | **NVDA** | 203.27 | - | **-** | 26 | - | NEG -$403.9M | 210.02 | 210 | 205 | +$30.6M | +$0 bull / -$1.5M bear | out (clean 29, ADX 51, RVol 1.7) |
| 8 | **QQQ** | 686.69 | - | **-** | 25 | - | NEG -$8.3B | 722.62 | 720 | 690 | +$175.5M | +$591k bull / -$8.0M bear | out (clean 30, ADX 52, RVol 1.7) |
| 9 | **NFLX** | 61.77 | - | **-** | 25 | - | NEG -$36.8M | 62.73 | 62 | 62 | +$1.5M | +$29k bull / +$0 bear | out (clean 30, ADX 33, RVol 1.0) |
| 10 | **IWM** | 278.15 | - | **-** | 24 | - | NEG -$1.5B | 280.41 | 278 | 278 | +$12.5M | +$0 bull / -$249k bear | out (clean 30, ADX 44, RVol 0.8) |
| 11 | **MU** | 870.43 | - | **-** | 24 | - | NEG -$256.7M | 891.82 | 880 | 880 | +$73.3M | +$89k bull / -$2.4M bear | out (clean 31, ADX 40, RVol 0.8) |
| 12 | **HOOD** | 82.69 | - | **-** | 24 | - | NEG -$27.1M | - | 85 | 83 | +$2.2M | +$29k bull / +$0 bear | out (clean 32, ADX 47, RVol 0.9) |
| 13 | **AAPL** | 343.27 | - | **-** | 23 | - | POS +$111.6M | 342.27 | 345 | 345 | +$12.5M | +$1.3M bull / -$333k bear | out (clean 32, ADX 38, RVol 1.2) |
| 14 | **AVGO** | 322.25 | - | **-** | 23 | - | NEG -$126.8M | 331.89 | 340 | 320 | +$2.7M | +$0 bull / -$347k bear | out (clean 30, ADX 47, RVol 1.1) |
| 15 | **SMCI** | 32.09 | - | **-** | 23 | - | NEG -$3.6M | 32.41 | 35 | 32 | +$344k | +$0 bull / -$185k bear | out (clean 29, ADX 43, RVol 1.2) |
| 16 | **META** | 613.63 | - | **-** | 21 | - | NEG -$179.5M | 619.05 | 650 | 610 | +$7.8M | +$179k bull / -$219k bear | out (clean 30, ADX 48, RVol 0.4) |
| 17 | **GOOGL** | 277.99 | - | **-** | 21 | - | NEG -$156.4M | - | 280 | 275 | +$3.7M | +$0 bull / -$279k bear | out (clean 33, ADX 41, RVol 0.8) |
| 18 | **BABA** | 97.73 | - | **-** | 20 | - | NEG -$53.1M | 99.79 | 100 | 98 | +$681k | - | out (clean 31, ADX 41, RVol 1.1) |
| 19 | **DELL** | 419.75 | - | **-** | 19 | - | NEG -$37.7M | - | 440 | 420 | +$8.7M | - | out (clean 34, ADX 36, RVol 1.5) |
| 20 | **SHOP** | 155.18 | - | **-** | 19 | - | NEG -$14.4M | - | 150 | 157.5 | +$640k | - | out (clean 28, ADX 32, RVol 1.7) |
| 21 | **PLTR** | 185.15 | - | **-** | 18 | - | NEG -$72.0M | 190.77 | 185 | 185 | +$2.0M | +$26k bull / -$2.2M bear | out (clean 26, ADX 25, RVol 1.0) |
| 22 | **AMZN** | 239.38 | - | **-** | 16 | - | NEG -$198.3M | 246.47 | 250 | 240 | -$3.9M | +$27k bull / -$1.1M bear | out (clean 30, ADX 14, RVol 1.1) |
| 23 | **ARM** | 202.13 | - | **-** | 16 | - | NEG -$20.5M | - | 220 | 205 | +$793k | - | out (clean 26, ADX 32, RVol 2.1) |
| 24 | **COIN** | 138.59 | - | **-** | 15 | - | NEG -$16.9M | - | 140 | 140 | -$1.7M | - | out (clean 28, ADX 41, RVol 3.3) |
| 25 | **CRM** | 228.27 | - | **-** | 13 | - | NEG -$27.4M | 233.16 | 230 | 230 | +$351k | - | out (clean 27, ADX 30, RVol 1.2) |
| 26 | **UBER** | 65.19 | - | **-** | 12 | - | NEG -$45.4M | 66.19 | 65 | 65 | +$326k | - | out (clean 26, ADX 17, RVol 0.6) |
| 27 | **MSTR** | 129.84 | - | **-** | 10 | - | NEG -$27.5M | 132.15 | 135 | 130 | -$4.2M | - | out (clean 28, ADX 27, RVol 1.3) |

## Big prints this scan (109)
- **PLTR** CALL 187.5 2026-11-06 (7DTE): 800 @ 10.72 = **+$858k** SELL | vol 9,784 / OI 380
- **QQQ** PUT 690 2026-10-30 (0DTE): 1,000 @ 6.54 = **+$654k** BUY | vol 307,121 / OI 65,738
- **SPY** CALL 750 2026-11-03 (4DTE): 988 @ 6.17 = **+$610k** SELL | vol 11,324 / OI 23
- **QQQ** PUT 700 2026-11-03 (4DTE): 200 @ 18.60 = **+$372k** BUY | vol 1,707 / OI 1,263
- **PLTR** CALL 187.5 2026-11-06 (7DTE): 343 @ 10.72 = **+$368k** SELL | vol 9,784 / OI 380
- **PLTR** CALL 187.5 2026-11-06 (7DTE): 343 @ 10.72 = **+$368k** SELL | vol 9,784 / OI 380
- **PLTR** CALL 187.5 2026-11-06 (7DTE): 343 @ 10.72 = **+$368k** SELL | vol 9,784 / OI 380
- **QQQ** PUT 680 2026-11-03 (4DTE): 500 @ 6.57 = **+$328k** BUY | vol 24,217 / OI 16,581
- **SPY** CALL 750 2026-11-03 (4DTE): 466 @ 6.17 = **+$288k** SELL | vol 11,324 / OI 23
- **QQQ** PUT 685 2026-10-30 (0DTE): 1,000 @ 2.53 = **+$253k** BUY | vol 197,667 / OI 20,384
- **QQQ** PUT 688 2026-10-30 (0DTE): 542 @ 4.51 = **+$244k** BUY | vol 144,298 / OI 1,418
- **QQQ** PUT 690 2026-10-30 (0DTE): 285 @ 6.67 = **+$190k** BUY | vol 307,121 / OI 65,738
- **QQQ** PUT 690 2026-10-30 (0DTE): 291 @ 6.31 = **+$184k** BUY | vol 307,121 / OI 65,738
- **PLTR** CALL 187.5 2026-11-06 (7DTE): 171 @ 10.72 = **+$183k** SELL | vol 9,784 / OI 380
- **QQQ** PUT 690 2026-10-30 (0DTE): 291 @ 6.20 = **+$180k** BUY | vol 307,121 / OI 65,738

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 710 2026-11-05 (6DTE): 518 traded vs OI 84
- **SPY** PUT 741 2026-11-04 (5DTE): 508 traded vs OI 124
- **SPY** CALL 778 2026-11-04 (5DTE): 682 traded vs OI 674
- **SPY** PUT 740 2026-11-10 (11DTE): 583 traded vs OI 557
- **SPY** PUT 765 2026-11-09 (10DTE): 1,788 traded vs OI 1,545
- **QQQ** PUT 620 2026-11-02 (3DTE): 501 traded vs OI 0
- **QQQ** CALL 675 2026-10-30 (0DTE): 532 traded vs OI 104
- **QQQ** PUT 665 2026-11-10 (11DTE): 525 traded vs OI 99
- **QQQ** CALL 685 2026-11-20 (21DTE): 1,242 traded vs OI 438
- **IWM** CALL 277.5 2026-11-06 (7DTE): 686 traded vs OI 683
- **SMH** CALL 550 2026-11-06 (7DTE): 1,976 traded vs OI 1,606
- **SMH** PUT 492.5 2026-11-02 (3DTE): 506 traded vs OI 3
- **NVDA** PUT 215 2026-11-04 (5DTE): 660 traded vs OI 618
- **NVDA** PUT 195 2026-11-13 (14DTE): 5,393 traded vs OI 5,338
- **TSLA** PUT 370 2026-11-13 (14DTE): 803 traded vs OI 756

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
