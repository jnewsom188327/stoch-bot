# GEX + FLOW SCAN - Fri Oct 30, 12:00 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (3)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:25 | **COIN** | **PUTS** | FLOW SURGE | 10/30 138P | 0.73 | 0.49 | +25% (7m) | **-33%** | +115% | 137.27 |
| 10:25 | **SMCI** | **PUTS** | FLIP CROSS down into negative gamma | 10/30 32.5P | 0.43 | 0.31 | -12% (1m) | **-28%** (done) | +32% | 32 |
| 10:15 | **AAPL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 10/30 347.5C | 0.50 | 1.24 | +356% (38m) | **+148%** (done) | +104% | 347.56 hit |

## 1m RULES on SPY / QQQ - loose (1 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 12:00:08 ET, last candle SPY 11:59, QQQ 11:59 | no errors
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
| 1 | **ARM** | 203.84 | - | **-** | 35 | - | NEG -$19.3M | - | 220 | 205 | +$625k | +$0 bull / -$66k bear | out (clean 26, ADX 46, RVol 2.5) |
| 2 | **COIN** | 140.55 | - | **-** | 30 | - | NEG -$15.7M | - | 140 | 140 | -$3.6M | +$0 bull / -$80k bear | out (clean 27, ADX 48, RVol 3.1) |
| 3 | **META** | 624.48 | PINNED between the walls (positive gamma) - chop | **-** | 29 | - | POS +$47.3M | 622.81 | 625 | 625 | -$4.7M | +$0 bull / -$193k bear | out (clean 28, ADX 13, RVol 0.5) |
| 4 | **ORCL** | 131.76 | - | **-** | 29 | - | POS +$40.0M | 129.53 | 130 | 130 | +$2.5M | +$0 bull / -$127k bear | out (clean 33, ADX 47, RVol 0.4) |
| 5 | **SMH** | 524.76 | - | **-** | 28 | - | NEG -$578.1M | - | 525 | 530 | +$5.3M | +$0 bull / -$59k bear | out (clean 29, ADX 48, RVol 1.8) |
| 6 | **NVDA** | 205.88 | - | **-** | 28 | - | NEG -$441.0M | 211.72 | 210 | 205 | +$18.4M | +$485k bull / +$0 bear | out (clean 26, ADX 39, RVol 0.9) |
| 7 | **AMD** | 510.48 | - | **-** | 28 | - | NEG -$134.4M | 522.08 | 517.5 | 500 | +$18.5M | +$578k bull / -$202k bear | out (clean 28, ADX 37, RVol 1.2) |
| 8 | **MU** | 885.00 | - | **-** | 26 | - | NEG -$261.5M | 930.91 | 900 | 900 | +$53.3M | +$7.3M bull / -$1.5M bear | out (clean 29, ADX 34, RVol 0.8) |
| 9 | **MSTR** | 132.72 | - | **-** | 25 | - | NEG -$23.6M | - | 135 | 130 | -$5.5M | +$0 bull / -$188k bear | out (clean 28, ADX 20, RVol 2.0) |
| 10 | **SPY** | 758.01 | - | **-** | 24 | - | NEG -$14.3B | 772.12 | 760 | 750 | +$95.1M | +$2.7M bull / -$2.1M bear | out (clean 26, ADX 41, RVol 0.8) |
| 11 | **AVGO** | 326.24 | - | **-** | 24 | - | NEG -$144.2M | - | 330 | 330 | +$1.6M | +$157k bull / +$0 bear | out (clean 29, ADX 51, RVol 0.7) |
| 12 | **NFLX** | 62.47 | - | **-** | 23 | - | NEG -$15.9M | 62.73 | 63 | 63 | +$1.0M | +$0 bull / -$26k bear | out (clean 32, ADX 18, RVol 0.6) |
| 13 | **QQQ** | 694.00 | - | **-** | 22 | - | NEG -$10.2B | 729 | 720 | 690 | +$42.9M | +$5.1M bull / -$803k bear | out (clean 27, ADX 44, RVol 1.1) |
| 14 | **HOOD** | 84.15 | - | **-** | 22 | - | NEG -$42.3M | - | 85 | 85 | +$847k | +$432k bull / -$29k bear | out (clean 31, ADX 50, RVol 0.5) |
| 15 | **PLTR** | 187.09 | - | **-** | 21 | - | NEG -$71.9M | 192.63 | 185 | 190 | -$2.8M | +$0 bull / -$1.9M bear | out (clean 25, ADX 34, RVol 0.9) |
| 16 | **DELL** | 424.91 | - | **-** | 20 | - | NEG -$58.4M | - | 440 | 425 | +$2.1M | - | out (clean 32, ADX 48, RVol 2.8) |
| 17 | **SHOP** | 155.93 | - | **-** | 20 | - | NEG -$13.3M | 164.67 | 150 | 157.5 | +$245k | - | out (clean 26, ADX 52, RVol 1.7) |
| 18 | **GOOGL** | 282.30 | - | **-** | 19 | - | NEG -$269.6M | - | 280 | 280 | -$3.7M | +$932k bull / +$0 bear | out (clean 32, ADX 15, RVol 0.7) |
| 19 | **SMCI** | 32.28 | - | **-** | 19 | - | NEG -$1.1M | 32.44 | 35 | 32 | +$628k | - | out (clean 29, ADX 44, RVol 0.7) |
| 20 | **AAPL** | 346.92 | - | **-** | 18 | - | POS +$562.3M | 343.39 | 350 | 345 | -$2.7M | +$264k bull / -$27k bear | out (clean 31, ADX 21, RVol 1.2) |
| 21 | **AMZN** | 239.07 | - | **-** | 18 | - | NEG -$164.3M | 246.36 | 250 | 240 | -$3.6M | +$1.6M bull / +$0 bear | out (clean 31, ADX 16, RVol 1.7) |
| 22 | **MSFT** | 523.12 | - | **-** | 18 | - | POS +$623.8M | 517.44 | 525 | 525 | +$1.6M | +$81k bull / -$80k bear | out (clean 26, ADX 23, RVol 0.5) |
| 23 | **TSLA** | 401.31 | - | **-** | 16 | - | POS +$413.0M | 394.95 | 400 | 400 | -$14.8M | +$1.2M bull / -$1.6M bear | out (clean 29, ADX 16, RVol 0.5) |
| 24 | **IWM** | 279.38 | - | **-** | 15 | - | NEG -$1.2B | 281.35 | 280 | 278 | +$9.7M | - | out (clean 27, ADX 38, RVol 0.6) |
| 25 | **CRM** | 232.49 | - | **-** | 14 | - | NEG -$23.4M | 239.45 | 240 | 230 | -$22k | +$0 bull / -$101k bear | out (clean 27, ADX 12, RVol 0.5) |
| 26 | **BABA** | 98.77 | - | **-** | 4 | - | NEG -$36.3M | 100.04 | 100 | 99 | +$7k | - | out (clean 29, ADX 12, RVol 0.7) |
| 27 | **UBER** | 65.28 | - | **-** | 2 | - | NEG -$36.6M | 66.34 | 70 | 65 | -$3k | - | out (clean 28, ADX 8, RVol 0.2) |

## Big prints this scan (121)
- **SPY** CALL 756 2026-11-02 (3DTE): 4,000 @ 4.40 = **+$1.8M** SELL | vol 4,776 / OI 45
- **QQQ** PUT 695 2026-11-06 (7DTE): 1,500 @ 11.17 = **+$1.7M** SELL | vol 5,689 / OI 10,815
- **SPY** CALL 758 2026-11-02 (3DTE): 4,000 @ 3.26 = **+$1.3M** BUY | vol 24,334 / OI 147
- **PLTR** CALL 187.5 2026-11-06 (7DTE): 500 @ 11.09 = **+$554k** SELL | vol 1,395 / OI 380
- **PLTR** CALL 187.5 2026-11-06 (7DTE): 500 @ 11.09 = **+$554k** SELL | vol 1,395 / OI 380
- **QQQ** PUT 706 2026-10-30 (0DTE): 317 @ 13.00 = **+$412k** SELL | vol 2,091 / OI 2,830
- **PLTR** CALL 195 2026-11-06 (7DTE): 500 @ 7.96 = **+$398k** SELL | vol 1,603 / OI 1,930
- **PLTR** CALL 195 2026-11-06 (7DTE): 500 @ 7.96 = **+$398k** SELL | vol 1,603 / OI 1,930
- **QQQ** PUT 695 2026-11-06 (7DTE): 250 @ 11.18 = **+$280k** SELL | vol 5,689 / OI 10,815
- **SPY** PUT 767 2026-11-04 (5DTE): 250 @ 10.75 = **+$269k** SELL | vol 12,480 / OI 29,783
- **SPY** PUT 767 2026-11-04 (5DTE): 250 @ 10.65 = **+$266k** SELL | vol 12,480 / OI 29,783
- **NVDA** PUT 215 2026-10-30 (0DTE): 200 @ 9.40 = **+$188k** SELL | vol 4,925 / OI 13,956
- **MU** CALL 880 2026-10-30 (0DTE): 236 @ 7.73 = **+$182k** BUY | vol 4,644 / OI 1,469
- **QQQ** CALL 710 2026-11-03 (4DTE): 1,500 @ 1.21 = **+$182k** BUY | vol 5,165 / OI 2,651
- **MU** PUT 880 2026-10-30 (0DTE): 301 @ 4.50 = **+$135k** MID | vol 25,550 / OI 2,467

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 762 2026-11-04 (5DTE): 536 traded vs OI 110
- **SPY** PUT 743 2026-11-03 (4DTE): 505 traded vs OI 283
- **SPY** CALL 766 2026-11-03 (4DTE): 508 traded vs OI 179
- **SPY** PUT 739 2026-11-04 (5DTE): 15,508 traded vs OI 128
- **SPY** PUT 727 2026-11-02 (3DTE): 753 traded vs OI 702
- **SPY** PUT 720 2026-11-02 (3DTE): 2,359 traded vs OI 1,722
- **SPY** PUT 742 2026-11-03 (4DTE): 539 traded vs OI 361
- **SPY** PUT 747 2026-11-03 (4DTE): 501 traded vs OI 210
- **SPY** PUT 700 2026-11-09 (10DTE): 1,450 traded vs OI 1,379
- **SPY** PUT 755 2026-11-12 (13DTE): 598 traded vs OI 0
- **SPY** CALL 785 2026-11-12 (13DTE): 556 traded vs OI 0
- **QQQ** PUT 666 2026-11-04 (5DTE): 517 traded vs OI 0
- **QQQ** CALL 730 2026-11-03 (4DTE): 790 traded vs OI 785
- **QQQ** CALL 724 2026-11-04 (5DTE): 512 traded vs OI 149
- **QQQ** CALL 709 2026-11-04 (5DTE): 509 traded vs OI 21

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
