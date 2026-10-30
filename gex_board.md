# GEX + FLOW SCAN - Fri Oct 30, 11:40 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (3)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:25 | **COIN** | **PUTS** | FLOW SURGE | 10/30 138P | 0.73 | 0.74 | +25% (7m) | **+1%** | +115% | 137.27 |
| 10:25 | **SMCI** | **PUTS** | FLIP CROSS down into negative gamma | 10/30 32.5P | 0.43 | 0.31 | -12% (1m) | **-28%** (done) | +32% | 32 |
| 10:15 | **AAPL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 10/30 347.5C | 0.50 | 1.24 | +356% (38m) | **+148%** (done) | +104% | 347.56 hit |

## 1m RULES on SPY / QQQ - loose (1 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 11:40:08 ET, last candle SPY 11:39, QQQ 11:39 | no errors
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
| 1 | **ARM** | 203.03 | FLOW SURGE | **CALLS** | 60 | none: 32 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (29 contracts' greeks worked out here) | NEG -$19.0M | - | 220 | 205 | +$652k | +$32k bull / +$0 bear | out (clean 26, ADX 48, RVol 3.2) |
| 2 | **ORCL** | 131.27 | FLOW SURGE | **CALLS** | 37 | 10/30 132C @ 0.60 (delta 0.38) = est +107% at 132.95 | POS +$35.3M | 129.22 | 130 | 130 | +$2.7M | +$30k bull / +$0 bear | out (clean 33, ADX 45, RVol 0.3) |
| 3 | **TSLA** | 399.79 | PINNED between the walls (positive gamma) - chop | **-** | 32 | - | POS +$439.2M | 390.38 | 400 | 400 | -$14.9M | +$4.1M bull / -$58k bear | out (clean 29, ADX 19, RVol 0.9) |
| 4 | **COIN** | 139.77 | - | **-** | 30 | - | NEG -$14.5M | - | 150 | 140 | -$3.4M | +$1.5M bull / +$0 bear | out (clean 27, ADX 51, RVol 3.8) |
| 5 | **DELL** | 426.13 | - | **-** | 29 | - | NEG -$51.6M | - | 440 | 425 | +$1.5M | +$36k bull / +$0 bear | out (clean 32, ADX 48, RVol 4.1) |
| 6 | **NVDA** | 205.75 | - | **-** | 28 | - | NEG -$439.1M | 211.77 | 210 | 205 | +$16.0M | +$2.2M bull / -$107k bear | out (clean 26, ADX 40, RVol 0.9) |
| 7 | **SMH** | 524.07 | - | **-** | 27 | - | NEG -$582.9M | - | 532.5 | 530 | +$5.3M | +$85k bull / +$0 bear | out (clean 28, ADX 48, RVol 0.8) |
| 8 | **AMD** | 510.65 | - | **-** | 27 | - | NEG -$111.7M | 521.34 | 517.5 | 500 | +$15.8M | +$1.9M bull / -$31k bear | out (clean 28, ADX 37, RVol 1.1) |
| 9 | **MU** | 884.36 | - | **-** | 26 | - | NEG -$278.6M | 934.38 | 900 | 900 | +$45.0M | +$3.4M bull / +$0 bear | out (clean 29, ADX 34, RVol 0.6) |
| 10 | **MSTR** | 132.00 | - | **-** | 26 | - | NEG -$24.6M | - | 135 | 130 | -$5.5M | +$394k bull / -$77k bear | out (clean 28, ADX 25, RVol 1.8) |
| 11 | **IWM** | 279.38 | - | **-** | 25 | - | NEG -$919.2M | 281.33 | 278 | 278 | +$8.7M | +$854k bull / +$0 bear | out (clean 27, ADX 37, RVol 0.6) |
| 12 | **GOOGL** | 282.41 | - | **-** | 25 | - | NEG -$245.9M | - | 280 | 280 | -$5.5M | +$27k bull / -$1.2M bear | out (clean 32, ADX 20, RVol 1.0) |
| 13 | **AVGO** | 325.75 | - | **-** | 24 | - | NEG -$133.5M | 339.74 | 330 | 325 | +$1.5M | +$59k bull / +$0 bear | out (clean 29, ADX 52, RVol 0.6) |
| 14 | **SPY** | 757.83 | - | **-** | 23 | - | NEG -$14.3B | 771.91 | 760 | 750 | +$85.0M | +$3.3M bull / +$0 bear | out (clean 26, ADX 40, RVol 0.8) |
| 15 | **NFLX** | 62.30 | - | **-** | 23 | - | NEG -$19.6M | 62.84 | 63 | 62 | +$962k | +$49k bull / +$0 bear | out (clean 32, ADX 21, RVol 0.4) |
| 16 | **QQQ** | 693.46 | - | **-** | 22 | - | NEG -$10.3B | 727.81 | 720 | 690 | +$34.7M | +$5.1M bull / +$0 bear | out (clean 27, ADX 43, RVol 1.0) |
| 17 | **AMZN** | 240.21 | - | **-** | 22 | - | NEG -$148.0M | 246.1 | 250 | 240 | -$8.3M | +$582k bull / -$303k bear | out (clean 31, ADX 15, RVol 2.2) |
| 18 | **PLTR** | 185.55 | - | **-** | 22 | - | NEG -$55.5M | 189.06 | 185 | 185 | -$1.8M | +$243k bull / +$0 bear | out (clean 25, ADX 36, RVol 1.2) |
| 19 | **AAPL** | 347.28 | - | **-** | 20 | - | POS +$620.0M | 342.85 | 350 | 345 | -$4.4M | +$726k bull / -$42k bear | out (clean 31, ADX 24, RVol 1.2) |
| 20 | **SMCI** | 32.23 | - | **-** | 20 | - | NEG -$1.4M | 32.44 | 35 | 32 | +$603k | - | out (clean 29, ADX 42, RVol 0.9) |
| 21 | **MSFT** | 521.71 | - | **-** | 19 | - | POS +$498.3M | 515.4 | 525 | 525 | +$1.8M | +$29k bull / -$121k bear | out (clean 26, ADX 25, RVol 0.7) |
| 22 | **SHOP** | 155.81 | - | **-** | 19 | - | NEG -$15.1M | - | 150 | 157.5 | +$205k | - | out (clean 26, ADX 52, RVol 1.6) |
| 23 | **META** | 622.68 | - | **-** | 16 | - | POS +$21.0M | 621.92 | 625 | 625 | -$3.1M | +$2.1M bull / +$0 bear | out (clean 28, ADX 15, RVol 0.5) |
| 24 | **HOOD** | 83.80 | - | **-** | 12 | - | NEG -$40.5M | - | 85 | 85 | +$551k | - | out (clean 31, ADX 52, RVol 0.8) |
| 25 | **CRM** | 231.38 | - | **-** | 4 | - | NEG -$20.0M | 237.41 | 240 | 230 | -$21k | - | out (clean 28, ADX 12, RVol 0.6) |
| 26 | **UBER** | 65.23 | - | **-** | 3 | - | NEG -$30.1M | 66.33 | 65 | 65 | -$9k | - | out (clean 28, ADX 9, RVol 0.2) |
| 27 | **BABA** | 98.67 | - | **-** | 3 | - | NEG -$34.4M | 100.08 | 100 | 99 | -$2k | - | out (clean 29, ADX 14, RVol 0.4) |

## Big prints this scan (96)
- **QQQ** CALL 695 2026-11-06 (7DTE): 500 @ 10.79 = **+$540k** BUY | vol 3,644 / OI 120
- **SPY** CALL 758 2026-11-02 (3DTE): 898 @ 4.03 = **+$362k** BUY | vol 18,793 / OI 147
- **SPY** PUT 749 2026-11-06 (7DTE): 954 @ 3.60 = **+$343k** SELL | vol 14,888 / OI 10,592
- **QQQ** CALL 695 2026-11-06 (7DTE): 239 @ 10.75 = **+$257k** BUY | vol 3,644 / OI 120
- **SPY** PUT 767 2026-11-04 (5DTE): 250 @ 10.12 = **+$253k** SELL | vol 11,223 / OI 29,783
- **MU** CALL 870 2026-10-30 (0DTE): 96 @ 21.42 = **+$206k** BUY | vol 949 / OI 331
- **SPY** PUT 741 2026-11-06 (7DTE): 954 @ 2.15 = **+$205k** SELL | vol 1,699 / OI 710
- **QQQ** CALL 696 2026-10-30 (0DTE): 1,000 @ 1.87 = **+$187k** BUY | vol 125,778 / OI 757
- **MSTR** PUT 134 2026-10-30 (0DTE): 750 @ 2.40 = **+$180k** SELL | vol 1,474 / OI 2,786
- **QQQ** PUT 700 2026-10-30 (0DTE): 353 @ 5.08 = **+$179k** SELL | vol 33,698 / OI 42,068
- **QQQ** CALL 696 2026-10-30 (0DTE): 1,000 @ 1.71 = **+$171k** BUY | vol 125,778 / OI 757
- **SPY** PUT 749 2026-11-06 (7DTE): 446 @ 3.59 = **+$160k** SELL | vol 14,888 / OI 10,592
- **QQQ** CALL 696 2026-10-30 (0DTE): 999 @ 1.55 = **+$155k** BUY | vol 125,778 / OI 757
- **SPY** PUT 765 2026-11-03 (4DTE): 200 @ 7.59 = **+$152k** SELL | vol 772 / OI 717
- **QQQ** CALL 695 2026-11-06 (7DTE): 131 @ 10.83 = **+$142k** BUY | vol 3,644 / OI 120

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 756 2026-11-06 (7DTE): 509 traded vs OI 116
- **SPY** PUT 765 2026-11-02 (3DTE): 3,972 traded vs OI 3,902
- **SPY** PUT 765 2026-11-03 (4DTE): 772 traded vs OI 717
- **SPY** CALL 775 2026-11-02 (3DTE): 1,583 traded vs OI 1,582
- **SPY** PUT 725 2026-11-05 (6DTE): 1,371 traded vs OI 158
- **SPY** PUT 740 2026-11-04 (5DTE): 1,890 traded vs OI 1,456
- **SPY** PUT 740 2026-11-02 (3DTE): 2,741 traded vs OI 2,657
- **SPY** PUT 760 2026-11-04 (5DTE): 2,874 traded vs OI 2,557
- **SPY** PUT 755 2026-11-04 (5DTE): 1,937 traded vs OI 1,817
- **SPY** PUT 741 2026-11-06 (7DTE): 1,699 traded vs OI 710
- **SPY** PUT 785 2026-11-27 (28DTE): 1,232 traded vs OI 87
- **QQQ** CALL 700 2026-11-05 (6DTE): 1,198 traded vs OI 1,170
- **QQQ** CALL 730 2026-11-09 (10DTE): 571 traded vs OI 289
- **IWM** CALL 287 2026-11-06 (7DTE): 708 traded vs OI 704
- **SMH** CALL 555 2026-11-02 (3DTE): 1,834 traded vs OI 92

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
