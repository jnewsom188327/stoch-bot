# GEX + FLOW SCAN - Fri Oct 30, 12:10 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (3)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:25 | **COIN** | **PUTS** | FLOW SURGE | 10/30 138P | 0.73 | 0.55 | +25% (7m) | **-25%** | +115% | 137.27 |
| 10:25 | **SMCI** | **PUTS** | FLIP CROSS down into negative gamma | 10/30 32.5P | 0.43 | 0.31 | -12% (1m) | **-28%** (done) | +32% | 32 |
| 10:15 | **AAPL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 10/30 347.5C | 0.50 | 1.24 | +356% (38m) | **+148%** (done) | +104% | 347.56 hit |

## 1m RULES on SPY / QQQ - loose (1 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 12:10:08 ET, last candle SPY 12:09, QQQ 12:09 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 11:05 | SPY | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |

## Flow surges NOT fired - price disagreed (40 today, last 5)
- 11:20 ARM CALLS: under EMA 20 - flow says one way, price says the other
- 11:20 COIN PUTS: price +0.22 over the last 15 min - flow says one way, price says the other
- 11:15 MSTR PUTS: price +1.54 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 11:10 MSTR PUTS: price +1.77 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:55 AAPL PUTS: price +1.23 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **SMH** | 522.94 | - | **-** | 30 | - | NEG -$608.5M | - | 532.5 | 530 | +$6.0M | +$1.0M bull / -$59k bear | out (clean 29, ADX 49, RVol 2.6) |
| 2 | **COIN** | 139.96 | - | **-** | 30 | - | NEG -$15.0M | - | 140 | 140 | -$3.4M | +$58k bull / +$0 bear | out (clean 27, ADX 47, RVol 2.9) |
| 3 | **NVDA** | 205.40 | - | **-** | 28 | - | NEG -$433.1M | 211.86 | 210 | 205 | +$20.6M | +$1.1M bull / -$152k bear | out (clean 26, ADX 39, RVol 0.9) |
| 4 | **TSLA** | 399.91 | PINNED between the walls (positive gamma) - chop | **-** | 28 | - | POS +$464.6M | 383.65 | 400 | 400 | -$12.9M | +$123k bull / -$1.9M bear | out (clean 29, ADX 14, RVol 0.6) |
| 5 | **AMD** | 508.38 | - | **-** | 28 | - | NEG -$140.0M | 522.26 | 517.5 | 500 | +$19.7M | +$1.2M bull / +$0 bear | out (clean 28, ADX 38, RVol 1.1) |
| 6 | **ORCL** | 132.29 | - | **-** | 28 | - | POS +$49.8M | 128.79 | 135 | 130 | +$2.4M | +$0 bull / -$234k bear | out (clean 33, ADX 44, RVol 0.6) |
| 7 | **MU** | 883.03 | - | **-** | 26 | - | NEG -$278.0M | 935.65 | 900 | 900 | +$56.4M | +$4.5M bull / -$1.7M bear | out (clean 29, ADX 35, RVol 0.8) |
| 8 | **AVGO** | 325.80 | - | **-** | 25 | - | NEG -$132.0M | 341.6 | 330 | 325 | +$1.9M | +$35k bull / +$0 bear | out (clean 30, ADX 51, RVol 0.9) |
| 9 | **SPY** | 757.08 | - | **-** | 24 | - | NEG -$13.8B | 771.04 | 760 | 750 | +$109.8M | +$2.2M bull / -$1.9M bear | out (clean 27, ADX 42, RVol 1.0) |
| 10 | **MSTR** | 132.67 | - | **-** | 23 | - | NEG -$23.0M | - | 135 | 130 | -$5.3M | +$0 bull / -$210k bear | out (clean 28, ADX 17, RVol 1.9) |
| 11 | **ARM** | 203.24 | - | **-** | 23 | - | NEG -$20.1M | - | 220 | 205 | +$623k | - | out (clean 26, ADX 46, RVol 2.1) |
| 12 | **QQQ** | 692.52 | - | **-** | 22 | - | NEG -$10.1B | 724.74 | 720 | 690 | +$51.4M | +$3.0M bull / -$119k bear | out (clean 27, ADX 44, RVol 1.1) |
| 13 | **HOOD** | 84.05 | - | **-** | 22 | - | NEG -$36.0M | - | 85 | 85 | +$758k | +$0 bull / -$55k bear | out (clean 31, ADX 49, RVol 0.3) |
| 14 | **PLTR** | 186.90 | - | **-** | 21 | - | NEG -$66.2M | 192.31 | 200 | 190 | -$2.9M | +$0 bull / -$1.9M bear | out (clean 25, ADX 32, RVol 0.8) |
| 15 | **DELL** | 423.75 | - | **-** | 21 | - | NEG -$53.5M | - | 440 | 425 | +$2.5M | - | out (clean 32, ADX 49, RVol 2.4) |
| 16 | **SMCI** | 32.12 | - | **-** | 20 | - | NEG -$2.7M | 32.48 | 35 | 32 | +$653k | - | out (clean 29, ADX 46, RVol 0.7) |
| 17 | **SHOP** | 155.56 | - | **-** | 20 | - | NEG -$13.7M | 161.33 | 150 | 157.5 | +$262k | - | out (clean 26, ADX 52, RVol 1.5) |
| 18 | **GOOGL** | 282.27 | - | **-** | 19 | - | NEG -$248.1M | - | 280 | 280 | -$3.7M | +$27k bull / -$58k bear | out (clean 32, ADX 13, RVol 0.6) |
| 19 | **AMZN** | 238.90 | - | **-** | 18 | - | NEG -$184.4M | 247.41 | 250 | 240 | -$2.5M | +$327k bull / -$44k bear | out (clean 31, ADX 17, RVol 1.7) |
| 20 | **AAPL** | 346.29 | - | **-** | 17 | - | POS +$494.0M | 342.83 | 350 | 345 | -$1.3M | +$580k bull / +$0 bear | out (clean 32, ADX 22, RVol 1.2) |
| 21 | **MSFT** | 521.58 | - | **-** | 17 | - | POS +$493.7M | 515.92 | 525 | 525 | +$1.5M | +$0 bull / -$69k bear | out (clean 26, ADX 22, RVol 0.5) |
| 22 | **META** | 621.44 | - | **-** | 16 | - | POS +$2.9M | 621.24 | 625 | 625 | -$3.9M | +$363k bull / -$28k bear | out (clean 28, ADX 12, RVol 0.7) |
| 23 | **IWM** | 279.11 | - | **-** | 15 | - | NEG -$977.9M | 281.18 | 278 | 278 | +$10.0M | - | out (clean 28, ADX 40, RVol 0.5) |
| 24 | **CRM** | 231.94 | - | **-** | 14 | - | NEG -$22.8M | 240.55 | 240 | 230 | -$28k | +$0 bull / -$101k bear | out (clean 27, ADX 11, RVol 0.4) |
| 25 | **NFLX** | 62.46 | - | **-** | 12 | - | NEG -$22.9M | 63.34 | 63 | 63 | +$982k | - | out (clean 31, ADX 16, RVol 0.7) |
| 26 | **BABA** | 98.68 | - | **-** | 5 | - | NEG -$33.5M | 99.97 | 100 | 99 | +$39k | - | out (clean 29, ADX 11, RVol 0.6) |
| 27 | **UBER** | 65.20 | - | **-** | 2 | - | NEG -$32.5M | 66.25 | 70 | 65 | -$5k | - | out (clean 28, ADX 7, RVol 0.2) |

## Big prints this scan (74)
- **AMD** PUT 505 2026-11-06 (7DTE): 201 @ 21.99 = **+$442k** SELL | vol 245 / OI 485
- **SMH** PUT 547.5 2026-10-30 (0DTE): 83 @ 22.58 = **+$187k** SELL | vol 778 / OI 973
- **TSLA** CALL 390 2026-11-06 (7DTE): 100 @ 15.85 = **+$158k** MID | vol 2,508 / OI 1,309
- **SPY** PUT 767 2026-10-30 (0DTE): 149 @ 9.44 = **+$141k** SELL | vol 7,323 / OI 6,927
- **MU** CALL 850 2026-10-30 (0DTE): 38 @ 35.85 = **+$136k** BUY | vol 237 / OI 312
- **MU** PUT 900 2026-11-02 (3DTE): 50 @ 23.00 = **+$115k** SELL | vol 2,664 / OI 448
- **QQQ** PUT 710 2026-10-30 (0DTE): 65 @ 16.38 = **+$106k** SELL | vol 7,993 / OI 27,653
- **MSFT** CALL 530 2026-11-06 (7DTE): 200 @ 4.90 = **+$98k** MID | vol 1,652 / OI 1,409
- **NVDA** PUT 207.5 2026-10-30 (0DTE): 450 @ 1.97 = **+$89k** SELL | vol 40,846 / OI 7,471
- **MU** CALL 840 2026-11-06 (7DTE): 15 @ 58.32 = **+$87k** BUY | vol 73 / OI 27
- **TSLA** PUT 400 2026-10-30 (0DTE): 400 @ 1.93 = **+$77k** BUY | vol 82,298 / OI 4,157
- **NVDA** PUT 212.5 2026-11-04 (5DTE): 100 @ 7.71 = **+$77k** SELL | vol 387 / OI 1,183
- **MU** CALL 900 2026-11-04 (5DTE): 40 @ 17.83 = **+$71k** BUY | vol 920 / OI 102
- **MU** CALL 900 2026-11-04 (5DTE): 40 @ 17.83 = **+$71k** BUY | vol 920 / OI 102
- **NVDA** PUT 207.5 2026-10-30 (0DTE): 370 @ 1.92 = **+$71k** SELL | vol 40,846 / OI 7,471

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 744 2026-10-30 (0DTE): 4,597 traded vs OI 4,533
- **SPY** CALL 741 2026-11-06 (7DTE): 513 traded vs OI 15
- **SPY** CALL 757 2026-11-04 (5DTE): 502 traded vs OI 115
- **SPY** PUT 716 2026-11-06 (7DTE): 1,891 traded vs OI 477
- **SPY** PUT 722 2026-11-06 (7DTE): 1,227 traded vs OI 659
- **QQQ** PUT 700 2026-11-05 (6DTE): 925 traded vs OI 910
- **QQQ** PUT 680 2026-10-30 (0DTE): 18,958 traded vs OI 18,943
- **QQQ** CALL 730 2026-11-05 (6DTE): 1,037 traded vs OI 477
- **QQQ** CALL 705 2026-11-06 (7DTE): 3,679 traded vs OI 3,642
- **QQQ** PUT 655 2026-11-06 (7DTE): 1,849 traded vs OI 1,827
- **IWM** PUT 280 2026-11-06 (7DTE): 2,951 traded vs OI 2,945
- **NVDA** PUT 187.5 2026-11-06 (7DTE): 501 traded vs OI 253
- **META** PUT 600 2026-10-30 (0DTE): 5,720 traded vs OI 5,681
- **AMZN** CALL 250 2026-11-13 (14DTE): 753 traded vs OI 743
- **MSFT** CALL 570 2026-11-27 (28DTE): 537 traded vs OI 324

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
