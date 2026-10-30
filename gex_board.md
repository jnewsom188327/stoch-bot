# GEX + FLOW SCAN - Fri Oct 30, 02:10 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (3)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:25 | **COIN** | **PUTS** | FLOW SURGE | 10/30 138P | 0.73 | 0.44 | +25% (7m) | **-40%** (done) | +115% | 137.27 |
| 10:25 | **SMCI** | **PUTS** | FLIP CROSS down into negative gamma | 10/30 32.5P | 0.43 | 0.31 | -12% (1m) | **-28%** (done) | +32% | 32 |
| 10:15 | **AAPL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 10/30 347.5C | 0.50 | 1.24 | +356% (38m) | **+148%** (done) | +104% | 347.56 hit |

## 1m RULES on SPY / QQQ - loose (4 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 14:10:08 ET, last candle SPY 14:09, QQQ 14:09 | no errors
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
| 1 | **DELL** | 415.80 | FLOW SURGE | **CALLS** | 55 | none: 66 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (53 contracts' greeks worked out here) | NEG -$40.2M | - | 440 | 420 | +$10.1M | +$26k bull / +$0 bear | out (clean 34, ADX 56, RVol 2.3) |
| 2 | **MSFT** | 521.25 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 36 | none: 168 calls 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (84 contracts' greeks worked out here) | POS +$417.2M | 516.56 | 525 | 520 | +$4.4M | +$33k bull / +$0 bear | out (clean 26, ADX 14, RVol 0.6) |
| 3 | **TSLA** | 394.45 | PINNED between the walls (positive gamma) - chop | **-** | 31 | - | POS +$382.7M | 380.37 | 395 | 395 | +$3.6M | +$1.2M bull / +$0 bear | out (clean 29, ADX 21, RVol 1.0) |
| 4 | **AMD** | 498.43 | - | **-** | 29 | - | NEG -$166.0M | 512.83 | 500 | 500 | +$36.4M | +$929k bull / -$127k bear | out (clean 30, ADX 48, RVol 1.4) |
| 5 | **NVDA** | 202.61 | - | **-** | 28 | - | NEG -$378.5M | 209.5 | 210 | 200 | +$37.4M | +$638k bull / -$302k bear | out (clean 28, ADX 53, RVol 1.0) |
| 6 | **SPY** | 753.45 | - | **-** | 27 | - | NEG -$15.9B | 771.06 | 800 | 750 | +$233.9M | +$5.3M bull / +$0 bear | out (clean 27, ADX 48, RVol 1.3) |
| 7 | **QQQ** | 686.76 | - | **-** | 26 | - | NEG -$8.9B | 721.58 | 720 | 690 | +$151.3M | +$8.7M bull / -$102k bear | out (clean 28, ADX 52, RVol 2.1) |
| 8 | **SMH** | 515.57 | - | **-** | 26 | - | NEG -$622.2M | - | 532.5 | 505 | +$8.0M | +$145k bull / +$0 bear | out (clean 30, ADX 54, RVol 0.8) |
| 9 | **MU** | 869.18 | - | **-** | 25 | - | NEG -$248.9M | 888.01 | 880 | 880 | +$71.5M | +$6.7M bull / -$988k bear | out (clean 30, ADX 43, RVol 0.8) |
| 10 | **NFLX** | 61.95 | - | **-** | 24 | - | NEG -$34.3M | 63.06 | 62 | 62 | +$1.4M | +$33k bull / +$0 bear | out (clean 30, ADX 24, RVol 0.8) |
| 11 | **AVGO** | 321.70 | - | **-** | 24 | - | NEG -$152.8M | 340.71 | 340 | 320 | +$2.2M | +$129k bull / +$0 bear | out (clean 30, ADX 45, RVol 1.2) |
| 12 | **IWM** | 278.07 | - | **-** | 23 | - | NEG -$1.4B | 281.05 | 278 | 278 | +$10.8M | +$889k bull / +$0 bear | out (clean 29, ADX 43, RVol 0.6) |
| 13 | **ORCL** | 130.53 | - | **-** | 23 | - | POS +$13.9M | 129.95 | 130 | 130 | +$2.5M | +$0 bull / -$32k bear | out (clean 34, ADX 28, RVol 0.6) |
| 14 | **SHOP** | 154.66 | - | **-** | 23 | - | NEG -$14.4M | - | 150 | 157.5 | +$754k | - | out (clean 27, ADX 50, RVol 1.4) |
| 15 | **AAPL** | 343.33 | - | **-** | 22 | - | POS +$176.1M | 341.38 | 345 | 345 | +$10.0M | +$762k bull / +$0 bear | out (clean 31, ADX 31, RVol 1.5) |
| 16 | **PLTR** | 184.76 | - | **-** | 20 | - | NEG -$58.0M | 187.29 | 185 | 185 | +$3.4M | +$80k bull / +$0 bear | out (clean 26, ADX 32, RVol 0.9) |
| 17 | **META** | 615.34 | - | **-** | 19 | - | NEG -$120.0M | 620.48 | 650 | 610 | +$6.1M | +$1.2M bull / +$0 bear | out (clean 29, ADX 32, RVol 0.4) |
| 18 | **GOOGL** | 278.64 | - | **-** | 19 | - | NEG -$219.3M | - | 280 | 280 | +$1.7M | +$756k bull / +$0 bear | out (clean 33, ADX 39, RVol 0.5) |
| 19 | **SMCI** | 31.53 | - | **-** | 19 | - | NEG -$3.7M | 32.4 | 32 | 32 | +$788k | - | out (clean 30, ADX 52, RVol 1.2) |
| 20 | **ARM** | 201.13 | - | **-** | 18 | - | NEG -$14.0M | - | 220 | 200 | +$882k | - | out (clean 26, ADX 34, RVol 1.9) |
| 21 | **AMZN** | 239.35 | - | **-** | 16 | - | NEG -$183.1M | 247.2 | 250 | 240 | -$5.5M | +$1.1M bull / -$99k bear | out (clean 30, ADX 12, RVol 0.9) |
| 22 | **COIN** | 138.57 | - | **-** | 16 | - | NEG -$15.3M | - | 140 | 140 | -$1.6M | - | out (clean 28, ADX 49, RVol 3.3) |
| 23 | **BABA** | 97.89 | - | **-** | 16 | - | NEG -$47.9M | 98.78 | 100 | 98 | +$573k | - | out (clean 30, ADX 25, RVol 0.7) |
| 24 | **UBER** | 64.90 | - | **-** | 14 | - | NEG -$39.1M | 66.36 | 65 | 65 | +$340k | - | out (clean 28, ADX 23, RVol 0.6) |
| 25 | **HOOD** | 82.83 | - | **-** | 13 | - | NEG -$27.4M | - | 85 | 83 | +$2.1M | - | out (clean 32, ADX 51, RVol 0.7) |
| 26 | **CRM** | 229.76 | - | **-** | 12 | - | NEG -$30.5M | 240.12 | 230 | 230 | +$300k | - | out (clean 28, ADX 30, RVol 0.7) |
| 27 | **MSTR** | 129.15 | - | **-** | 9 | - | NEG -$26.6M | 132.63 | 135 | 130 | -$4.0M | - | out (clean 29, ADX 29, RVol 0.6) |

## Big prints this scan (131)
- **QQQ** PUT 713 2026-10-30 (0DTE): 200 @ 24.80 = **+$496k** SELL | vol 2,426 / OI 3,537
- **QQQ** PUT 713 2026-10-30 (0DTE): 200 @ 24.55 = **+$491k** SELL | vol 2,426 / OI 3,537
- **GOOGL** CALL 282.5 2026-11-06 (7DTE): 1,093 @ 4.07 = **+$445k** MID | vol 6,413 / OI 0
- **QQQ** PUT 680 2026-11-04 (5DTE): 676 @ 6.43 = **+$435k** SELL | vol 4,364 / OI 476
- **MU** PUT 895 2026-11-02 (3DTE): 145 @ 29.15 = **+$423k** SELL | vol 2,090 / OI 131
- **QQQ** PUT 692 2026-10-30 (0DTE): 577 @ 5.00 = **+$288k** SELL | vol 186,520 / OI 2,435
- **MSTR** PUT 135 2026-10-30 (0DTE): 500 @ 5.70 = **+$285k** MID | vol 3,989 / OI 3,709
- **SPY** PUT 767 2026-11-04 (5DTE): 200 @ 13.72 = **+$274k** SELL | vol 20,234 / OI 29,783
- **GOOGL** CALL 290 2026-11-06 (7DTE): 1,093 @ 1.86 = **+$203k** BUY | vol 5,124 / OI 21
- **SPY** PUT 767 2026-11-04 (5DTE): 135 @ 14.00 = **+$189k** SELL | vol 20,234 / OI 29,783
- **QQQ** PUT 680 2026-11-04 (5DTE): 289 @ 6.42 = **+$186k** SELL | vol 4,364 / OI 476
- **QQQ** PUT 680 2026-11-02 (3DTE): 593 @ 3.10 = **+$184k** SELL | vol 19,030 / OI 2,638
- **QQQ** PUT 680 2026-11-06 (7DTE): 207 @ 8.77 = **+$182k** SELL | vol 17,964 / OI 27,304
- **GOOGL** CALL 282.5 2026-11-06 (7DTE): 400 @ 4.07 = **+$163k** MID | vol 6,413 / OI 0
- **QQQ** PUT 680 2026-11-02 (3DTE): 486 @ 3.10 = **+$151k** SELL | vol 19,030 / OI 2,638

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 754 2026-11-04 (5DTE): 527 traded vs OI 280
- **SPY** CALL 764 2026-11-06 (7DTE): 1,683 traded vs OI 1,346
- **SPY** PUT 749 2026-11-04 (5DTE): 524 traded vs OI 322
- **SPY** PUT 735 2026-11-12 (13DTE): 510 traded vs OI 0
- **SPY** CALL 780 2026-11-11 (12DTE): 502 traded vs OI 67
- **QQQ** PUT 689 2026-11-04 (5DTE): 505 traded vs OI 0
- **QQQ** PUT 687 2026-11-03 (4DTE): 500 traded vs OI 0
- **QQQ** PUT 708 2026-10-30 (0DTE): 2,690 traded vs OI 2,673
- **QQQ** CALL 689 2026-11-03 (4DTE): 504 traded vs OI 0
- **QQQ** CALL 683 2026-10-30 (0DTE): 756 traded vs OI 57
- **QQQ** PUT 660 2026-11-03 (4DTE): 1,923 traded vs OI 1,878
- **QQQ** CALL 703 2026-11-04 (5DTE): 530 traded vs OI 17
- **QQQ** CALL 710 2026-11-20 (21DTE): 7,613 traded vs OI 7,592
- **QQQ** CALL 718 2026-11-13 (14DTE): 1,212 traded vs OI 91
- **QQQ** PUT 680 2026-11-10 (11DTE): 512 traded vs OI 206

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
