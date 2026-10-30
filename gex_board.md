# GEX + FLOW SCAN - Fri Oct 30, 03:40 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (3)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:25 | **COIN** | **PUTS** | FLOW SURGE | 10/30 138P | 0.73 | 0.44 | +25% (7m) | **-40%** (done) | +115% | 137.27 |
| 10:25 | **SMCI** | **PUTS** | FLIP CROSS down into negative gamma | 10/30 32.5P | 0.43 | 0.31 | -12% (1m) | **-28%** (done) | +32% | 32 |
| 10:15 | **AAPL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 10/30 347.5C | 0.50 | 1.24 | +356% (38m) | **+148%** (done) | +104% | 347.56 hit |

## 1m RULES on SPY / QQQ - loose (5 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 15:32:08 ET, last candle SPY 15:31, QQQ 15:31 | no errors
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
| 1 | **COIN** | 140.71 | - | **-** | 28 | - | NEG -$18.7M | - | 140 | 140 | -$5.0M | +$0 bull / -$1.0M bear | out (clean 27, ADX 39, RVol 3.5) |
| 2 | **DELL** | 419.00 | - | **-** | 28 | - | NEG -$40.0M | - | 440 | 420 | +$8.2M | +$38k bull / -$28k bear | out (clean 34, ADX 27, RVol 2.1) |
| 3 | **SPY** | 753.46 | - | **-** | 26 | - | NEG -$15.0B | 765.85 | 800 | 750 | +$253.8M | +$2.9M bull / -$7.0M bear | out (clean 28, ADX 38, RVol 3.0) |
| 4 | **AMD** | 498.49 | - | **-** | 26 | - | NEG -$176.9M | 517.25 | 500 | 500 | +$34.4M | +$0 bull / -$706k bear | out (clean 30, ADX 30, RVol 2.4) |
| 5 | **NVDA** | 202.97 | - | **-** | 25 | - | NEG -$387.3M | 211.72 | 210 | 200 | +$34.0M | +$3.2M bull / -$828k bear | out (clean 29, ADX 36, RVol 1.9) |
| 6 | **MSTR** | 130.34 | - | **-** | 25 | - | NEG -$29.1M | - | 135 | 130 | -$12.2M | +$40k bull / -$2.0M bear | out (clean 28, ADX 27, RVol 2.4) |
| 7 | **QQQ** | 687.99 | - | **-** | 23 | - | NEG -$10.6B | 726.95 | 720 | 690 | +$84.8M | +$1.4M bull / -$8.0M bear | out (clean 29, ADX 37, RVol 2.6) |
| 8 | **AAPL** | 344.12 | - | **-** | 22 | - | POS +$115.8M | 342.31 | 345 | 345 | +$11.3M | +$0 bull / -$1.1M bear | out (clean 32, ADX 32, RVol 1.7) |
| 9 | **SMCI** | 32.26 | - | **-** | 22 | - | NEG -$3.3M | 32.36 | 35 | 32 | +$112k | +$0 bull / -$140k bear | out (clean 30, ADX 42, RVol 1.8) |
| 10 | **MU** | 869.59 | - | **-** | 22 | - | NEG -$248.8M | 884.58 | 880 | 870 | +$65.7M | +$2.3M bull / -$9.5M bear | out (clean 31, ADX 27, RVol 1.6) |
| 11 | **IWM** | 278.50 | - | **-** | 21 | - | NEG -$1.2B | 281 | 278 | 278 | +$7.3M | +$0 bull / -$686k bear | out (clean 30, ADX 32, RVol 1.7) |
| 12 | **HOOD** | 83.41 | - | **-** | 21 | - | NEG -$34.1M | - | 85 | 83 | +$899k | +$0 bull / -$411k bear | out (clean 31, ADX 38, RVol 1.2) |
| 13 | **SMH** | 517.90 | - | **-** | 20 | - | NEG -$511.2M | - | 532.5 | 520 | +$2.3M | +$30k bull / -$946k bear | out (clean 31, ADX 32, RVol 1.7) |
| 14 | **META** | 614.44 | - | **-** | 20 | - | NEG -$149.7M | 617.29 | 615 | 615 | +$6.3M | +$1.1M bull / -$1.0M bear | out (clean 30, ADX 43, RVol 0.4) |
| 15 | **MSFT** | 523.13 | - | **-** | 20 | - | POS +$711.1M | 518.39 | 525 | 525 | +$3.9M | +$0 bull / -$790k bear | out (clean 26, ADX 22, RVol 1.5) |
| 16 | **AVGO** | 322.94 | - | **-** | 20 | - | NEG -$150.3M | 333.12 | 340 | 320 | +$2.0M | +$0 bull / -$126k bear | out (clean 30, ADX 32, RVol 1.2) |
| 17 | **ORCL** | 129.45 | - | **-** | 20 | - | POS +$5.9M | 128.27 | 130 | 130 | +$2.5M | +$152k bull / +$0 bear | out (clean 33, ADX 21, RVol 1.1) |
| 18 | **TSLA** | 398.70 | - | **-** | 19 | - | POS +$474.7M | 385.79 | 400 | 400 | -$7.8M | +$962k bull / -$1.3M bear | out (clean 30, ADX 24, RVol 1.9) |
| 19 | **GOOGL** | 278.68 | - | **-** | 19 | - | NEG -$218.4M | - | 280 | 280 | +$2.3M | +$35k bull / -$683k bear | out (clean 33, ADX 31, RVol 0.8) |
| 20 | **SHOP** | 156.26 | - | **-** | 19 | - | NEG -$23.0M | - | 155 | 157.5 | +$619k | - | out (clean 28, ADX 30, RVol 2.9) |
| 21 | **AMZN** | 239.63 | - | **-** | 18 | - | NEG -$188.7M | 243.48 | 250 | 240 | -$5.8M | +$79k bull / -$149k bear | out (clean 30, ADX 18, RVol 1.6) |
| 22 | **BABA** | 97.79 | - | **-** | 18 | - | NEG -$57.2M | 98.56 | 100 | 98 | +$660k | - | out (clean 31, ADX 32, RVol 1.4) |
| 23 | **NFLX** | 61.87 | - | **-** | 15 | - | NEG -$31.2M | 62.71 | 62 | 62 | +$1.4M | - | out (clean 30, ADX 34, RVol 1.0) |
| 24 | **PLTR** | 185.27 | - | **-** | 15 | - | NEG -$46.9M | 186.95 | 185 | 185 | +$194k | +$0 bull / -$586k bear | out (clean 26, ADX 18, RVol 1.1) |
| 25 | **UBER** | 64.95 | - | **-** | 13 | - | NEG -$42.6M | 65.81 | 65 | 65 | +$478k | - | out (clean 26, ADX 14, RVol 0.7) |
| 26 | **CRM** | 227.94 | - | **-** | 13 | - | NEG -$30.1M | 237.23 | 240 | 230 | +$386k | - | out (clean 27, ADX 31, RVol 1.1) |
| 27 | **ARM** | 204.73 | - | **-** | 11 | - | NEG -$23.3M | - | 205 | 205 | +$76k | - | out (clean 27, ADX 32, RVol 2.2) |

## Big prints this scan (97)
- **MSTR** CALL 136 2026-11-06 (7DTE): 2,400 @ 3.85 = **+$924k** SELL | vol 22,282 / OI 69
- **MSTR** CALL 136 2026-11-06 (7DTE): 2,000 @ 3.85 = **+$770k** SELL | vol 22,282 / OI 69
- **SPY** CALL 750 2026-11-03 (4DTE): 1,000 @ 6.96 = **+$696k** SELL | vol 28,268 / OI 23
- **MU** PUT 900 2026-10-30 (0DTE): 200 @ 31.00 = **+$620k** BUY | vol 12,634 / OI 3,632
- **SPY** CALL 750 2026-11-03 (4DTE): 874 @ 6.88 = **+$601k** SELL | vol 28,268 / OI 23
- **QQQ** PUT 680 2026-11-06 (7DTE): 626 @ 8.72 = **+$546k** BUY | vol 23,528 / OI 27,304
- **PLTR** CALL 187.5 2026-11-06 (7DTE): 426 @ 11.13 = **+$474k** MID | vol 11,473 / OI 380
- **PLTR** CALL 187.5 2026-11-06 (7DTE): 426 @ 11.13 = **+$474k** MID | vol 11,473 / OI 380
- **PLTR** CALL 187.5 2026-11-06 (7DTE): 372 @ 11.12 = **+$414k** MID | vol 11,473 / OI 380
- **PLTR** CALL 187.5 2026-11-06 (7DTE): 372 @ 11.12 = **+$414k** MID | vol 11,473 / OI 380
- **SPY** CALL 750 2026-11-03 (4DTE): 500 @ 6.77 = **+$338k** SELL | vol 28,268 / OI 23
- **SPY** CALL 750 2026-11-03 (4DTE): 456 @ 6.77 = **+$309k** SELL | vol 28,268 / OI 23
- **QQQ** PUT 694 2026-10-30 (0DTE): 400 @ 6.90 = **+$276k** BUY | vol 143,964 / OI 2,190
- **QQQ** PUT 680 2026-11-04 (5DTE): 412 @ 6.60 = **+$272k** BUY | vol 9,887 / OI 476
- **MSTR** CALL 136 2026-11-06 (7DTE): 600 @ 3.85 = **+$231k** SELL | vol 22,282 / OI 69

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 784 2026-11-13 (14DTE): 1,067 traded vs OI 789
- **SPY** PUT 745 2026-11-13 (14DTE): 3,536 traded vs OI 2,375
- **SPY** CALL 781 2026-11-13 (14DTE): 2,533 traded vs OI 1,120
- **SPY** PUT 705 2026-11-06 (7DTE): 2,253 traded vs OI 2,246
- **SPY** PUT 725 2026-11-13 (14DTE): 9,055 traded vs OI 8,820
- **SPY** PUT 725 2026-11-06 (7DTE): 9,813 traded vs OI 9,717
- **SPY** CALL 783 2026-11-13 (14DTE): 1,866 traded vs OI 1,490
- **QQQ** PUT 683 2026-11-04 (5DTE): 624 traded vs OI 0
- **QQQ** CALL 687 2026-11-06 (7DTE): 514 traded vs OI 61
- **QQQ** CALL 715 2026-11-06 (7DTE): 10,830 traded vs OI 10,260
- **QQQ** CALL 745 2026-11-05 (6DTE): 1,070 traded vs OI 950
- **QQQ** CALL 728 2026-11-06 (7DTE): 946 traded vs OI 796
- **QQQ** CALL 721 2026-11-06 (7DTE): 649 traded vs OI 434
- **QQQ** CALL 704 2026-11-20 (21DTE): 514 traded vs OI 366
- **QQQ** CALL 715 2026-11-11 (12DTE): 518 traded vs OI 42

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
