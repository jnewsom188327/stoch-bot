# GEX + FLOW SCAN - Fri Oct 30, 11:20 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (2)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:25 | **SMCI** | **PUTS** | FLIP CROSS down into negative gamma | 10/30 32.5P | 0.43 | 0.28 | -12% (1m) | **-35%** | +32% | 32 |
| 10:15 | **AAPL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 10/30 347.5C | 0.50 | 1.24 | +356% (38m) | **+148%** (done) | +104% | 347.56 hit |

## 1m RULES on SPY / QQQ - loose (1 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 11:20:08 ET, last candle SPY 11:19, QQQ 11:19 | no errors
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
| 1 | **COIN** | 140.53 | FLOW SURGE | **PUTS** | 57 | 10/30 138P @ 0.67 (delta 0.26) = est +140% at 137.26 | NEG -$14.2M | - | 150 | 140 | -$4.7M | +$28k bull / -$1.6M bear | out (clean 27, ADX 53, RVol 2.8) |
| 2 | **ARM** | 204.78 | FLOW SURGE | **CALLS** | 56 | 10/30 207.5C @ 0.73 (delta 0.27) = est +136% at 208.11 | NEG -$20.3M | - | 220 | 205 | +$474k | +$62k bull / +$0 bear | out (clean 26, ADX 50, RVol 2.5) |
| 3 | **ORCL** | 131.80 | FLOW SURGE | **CALLS** | 40 | 10/30 133C @ 0.46 (delta 0.30) = est +144% at 133.71 | POS +$51.1M | 129.12 | 130 | 130 | +$2.4M | +$896k bull / +$0 bear | out (clean 33, ADX 41, RVol 0.8) |
| 4 | **META** | 623.80 | PINNED between the walls (positive gamma) - chop | **-** | 36 | - | POS +$40.0M | 622.25 | 625 | 625 | -$8.7M | +$852k bull / -$2.2M bear | out (clean 28, ADX 18, RVol 0.8) |
| 5 | **SMCI** | 32.43 | FLIP CROSS up into positive gamma | **CALLS** | 34 | 10/30 32C @ 0.58 (delta 0.73) = est +67% at 32.99 | POS +$809k | 32.32 | 35 | 32 | +$589k | - | out (clean 28, ADX 41, RVol 0.8) |
| 6 | **MSTR** | 132.91 | - | **-** | 29 | - | NEG -$21.9M | - | 135 | 130 | -$5.6M | +$0 bull / -$2.3M bear | out (clean 27, ADX 31, RVol 1.9) |
| 7 | **SHOP** | 156.35 | - | **-** | 29 | - | NEG -$13.5M | 163.52 | 150 | 157.5 | +$194k | +$45k bull / +$0 bear | out (clean 26, ADX 48, RVol 1.6) |
| 8 | **NVDA** | 206.30 | - | **-** | 28 | - | NEG -$386.4M | 211.66 | 210 | 205 | +$12.0M | +$3.4M bull / -$59k bear | out (clean 26, ADX 40, RVol 1.2) |
| 9 | **SMH** | 525.91 | - | **-** | 27 | - | NEG -$556.8M | - | 530 | 530 | +$4.5M | +$32k bull / +$0 bear | out (clean 28, ADX 47, RVol 1.5) |
| 10 | **AMZN** | 241.16 | - | **-** | 27 | - | NEG -$144.8M | 247.87 | 250 | 240 | -$10.2M | +$172k bull / -$914k bear | out (clean 32, ADX 18, RVol 3.1) |
| 11 | **GOOGL** | 281.76 | - | **-** | 27 | - | NEG -$241.0M | - | 280 | 280 | -$4.2M | +$0 bull / -$1.3M bear | out (clean 32, ADX 24, RVol 1.2) |
| 12 | **DELL** | 428.77 | - | **-** | 27 | - | NEG -$58.0M | - | 440 | 425 | +$872k | +$29k bull / +$0 bear | out (clean 32, ADX 48, RVol 3.1) |
| 13 | **AMD** | 512.48 | - | **-** | 26 | - | NEG -$94.4M | 521.22 | 517.5 | 500 | +$10.5M | +$1.3M bull / -$29k bear | out (clean 28, ADX 38, RVol 1.2) |
| 14 | **NFLX** | 62.39 | - | **-** | 25 | - | NEG -$18.8M | 62.89 | 63 | 62 | +$837k | +$74k bull / +$0 bear | out (clean 31, ADX 28, RVol 0.8) |
| 15 | **MU** | 889.77 | - | **-** | 24 | - | NEG -$243.2M | 927.93 | 900 | 900 | +$32.1M | +$2.4M bull / -$429k bear | out (clean 29, ADX 32, RVol 0.7) |
| 16 | **IWM** | 279.80 | - | **-** | 23 | - | NEG -$689.6M | 281.3 | 280 | 270 | +$5.6M | +$0 bull / -$67k bear | out (clean 27, ADX 38, RVol 0.5) |
| 17 | **AAPL** | 347.86 | - | **-** | 23 | - | POS +$703.8M | 342.34 | 350 | 345 | -$5.8M | +$291k bull / -$87k bear | out (clean 31, ADX 30, RVol 1.3) |
| 18 | **AVGO** | 326.86 | - | **-** | 23 | - | NEG -$134.2M | - | 330 | 330 | +$1.1M | +$221k bull / +$0 bear | out (clean 30, ADX 52, RVol 0.8) |
| 19 | **PLTR** | 187.02 | - | **-** | 23 | - | NEG -$61.0M | 192.75 | 200 | 190 | -$2.6M | +$763k bull / +$0 bear | out (clean 25, ADX 35, RVol 1.2) |
| 20 | **SPY** | 758.54 | - | **-** | 22 | - | NEG -$13.8B | 771.88 | 760 | 760 | +$50.1M | +$4.8M bull / -$129k bear | out (clean 26, ADX 41, RVol 0.9) |
| 21 | **TSLA** | 401.71 | - | **-** | 22 | - | POS +$414.8M | 394.12 | 400 | 400 | -$31.0M | +$2.8M bull / -$2.3M bear | out (clean 29, ADX 24, RVol 1.5) |
| 22 | **QQQ** | 694.93 | - | **-** | 20 | - | NEG -$9.9B | 727.12 | 720 | 690 | +$4.0M | +$5.5M bull / -$666k bear | out (clean 27, ADX 44, RVol 0.9) |
| 23 | **HOOD** | 84.27 | - | **-** | 12 | - | NEG -$40.5M | - | 85 | 85 | +$362k | - | out (clean 31, ADX 52, RVol 0.9) |
| 24 | **MSFT** | 522.06 | - | **-** | 10 | - | POS +$473.5M | 515.26 | 525 | 525 | +$1.6M | - | out (clean 26, ADX 24, RVol 1.0) |
| 25 | **CRM** | 232.45 | - | **-** | 9 | - | NEG -$19.2M | 237.74 | 240 | 230 | -$94k | - | out (clean 27, ADX 14, RVol 0.7) |
| 26 | **UBER** | 65.25 | - | **-** | 4 | - | NEG -$31.1M | 66.38 | 70 | 65 | -$9k | - | out (clean 28, ADX 11, RVol 0.3) |
| 27 | **BABA** | 98.89 | - | **-** | 4 | - | NEG -$37.0M | 100.33 | 100 | 99 | -$11k | - | out (clean 29, ADX 15, RVol 0.3) |

## Big prints this scan (98)
- **SPY** PUT 751 2026-11-04 (5DTE): 3,475 @ 2.59 = **+$900k** SELL | vol 3,718 / OI 144
- **SPY** CALL 765 2026-11-04 (5DTE): 2,003 @ 2.82 = **+$565k** BUY | vol 4,517 / OI 357
- **SPY** PUT 753 2026-11-02 (3DTE): 3,475 @ 1.30 = **+$452k** SELL | vol 9,641 / OI 387
- **SPY** CALL 765 2026-11-04 (5DTE): 1,427 @ 2.81 = **+$401k** BUY | vol 4,517 / OI 357
- **SPY** CALL 763 2026-11-02 (3DTE): 2,003 @ 1.74 = **+$349k** BUY | vol 10,812 / OI 1,010
- **SPY** CALL 763 2026-11-02 (3DTE): 1,427 @ 1.73 = **+$247k** BUY | vol 10,812 / OI 1,010
- **QQQ** CALL 696 2026-10-30 (0DTE): 1,000 @ 2.29 = **+$229k** BUY | vol 100,212 / OI 757
- **SPY** PUT 749 2026-11-06 (7DTE): 593 @ 3.34 = **+$198k** SELL | vol 13,474 / OI 10,592
- **QQQ** PUT 698 2026-11-02 (3DTE): 296 @ 6.21 = **+$184k** SELL | vol 2,784 / OI 0
- **AMZN** CALL 232.5 2026-10-30 (0DTE): 250 @ 7.25 = **+$181k** SELL | vol 5,773 / OI 226
- **QQQ** CALL 713 2026-11-02 (3DTE): 3,538 @ 0.51 = **+$180k** BUY | vol 16,340 / OI 214
- **NVDA** PUT 210 2026-10-30 (0DTE): 499 @ 3.60 = **+$180k** SELL | vol 14,270 / OI 26,115
- **SPY** PUT 749 2026-11-06 (7DTE): 464 @ 3.34 = **+$155k** SELL | vol 13,474 / OI 10,592
- **QQQ** PUT 700 2026-10-30 (0DTE): 296 @ 5.09 = **+$151k** SELL | vol 31,503 / OI 42,068
- **QQQ** CALL 694 2026-11-02 (3DTE): 250 @ 5.85 = **+$146k** BUY | vol 4,161 / OI 0

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 735 2026-11-02 (3DTE): 751 traded vs OI 675
- **SPY** PUT 751 2026-11-04 (5DTE): 3,718 traded vs OI 144
- **SPY** PUT 749 2026-11-06 (7DTE): 13,474 traded vs OI 10,592
- **QQQ** PUT 680 2026-11-05 (6DTE): 712 traded vs OI 701
- **QQQ** CALL 706 2026-11-03 (4DTE): 859 traded vs OI 22
- **QQQ** CALL 710 2026-11-11 (12DTE): 541 traded vs OI 7
- **NVDA** CALL 207.5 2026-11-13 (14DTE): 519 traded vs OI 35
- **NVDA** CALL 200 2026-11-06 (7DTE): 504 traded vs OI 355
- **NVDA** CALL 190 2026-11-04 (5DTE): 675 traded vs OI 8
- **TSLA** CALL 415 2026-10-30 (0DTE): 8,687 traded vs OI 8,683
- **META** CALL 635 2026-11-02 (3DTE): 504 traded vs OI 365
- **META** CALL 655 2026-11-02 (3DTE): 536 traded vs OI 399
- **META** CALL 675 2026-11-04 (5DTE): 527 traded vs OI 157
- **META** CALL 637.5 2026-11-02 (3DTE): 684 traded vs OI 167
- **META** PUT 620 2026-11-02 (3DTE): 524 traded vs OI 360

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
