# GEX + FLOW SCAN - Tue Nov 03, 02:30 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 14:30:08 ET, last candle SPY 14:29, QQQ 14:29 | no errors

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **MSFT** | 521.47 | - | **-** | 28 | - | POS +$252.9M | 502.52 | 540 | 500 | -$12.5M | +$26k bull / +$0 bear | out (clean 29, ADX 42, RVol 0.6) |
| 2 | **TSLA** | 399.17 | PINNED between the walls (positive gamma) - chop | **-** | 27 | - | POS +$208.1M | - | 400 | 400 | +$15.2M | +$460k bull / -$409k bear | out (clean 31, ADX 19, RVol 0.3) |
| 3 | **ORCL** | 124.38 | - | **-** | 24 | - | NEG -$40.7M | - | 135 | 125 | -$9.3M | +$135k bull / +$0 bear | out (clean 34, ADX 31, RVol 0.7) |
| 4 | **META** | 621.24 | - | **-** | 21 | - | NEG -$35.3M | 626.3 | 650 | 610 | -$15.2M | +$215k bull / -$161k bear | out (clean 28, ADX 23, RVol 0.4) |
| 5 | **AMZN** | 251.75 | - | **-** | 21 | - | POS +$183.5M | - | 250 | 250 | -$3.9M | +$137k bull / -$57k bear | out (clean 33, ADX 38, RVol 0.4) |
| 6 | **NFLX** | 63.08 | - | **-** | 21 | - | NEG -$8.3M | 64.51 | 63 | 65 | -$430k | +$0 bull / -$50k bear | out (clean 28, ADX 38, RVol 0.6) |
| 7 | **AVGO** | 332.17 | - | **-** | 18 | - | NEG -$66.6M | - | 340 | 340 | +$3.8M | +$62k bull / +$0 bear | out (clean 30, ADX 11, RVol 0.4) |
| 8 | **SHOP** | 145.35 | - | **-** | 18 | - | NEG -$4.2M | - | 145 | 148 | -$4.2M | - | out (clean 34, ADX 20, RVol 0.9) |
| 9 | **SMH** | 517.65 | - | **-** | 17 | - | NEG -$301.7M | - | 532.5 | 500 | +$1.8M | +$311k bull / +$0 bear | out (clean 31, ADX 16, RVol 0.3) |
| 10 | **NVDA** | 206.84 | - | **-** | 17 | - | POS +$77.3M | 203.77 | 210 | 200 | +$14.8M | +$477k bull / +$0 bear | out (clean 29, ADX 19, RVol 0.5) |
| 11 | **MSTR** | 135.89 | - | **-** | 17 | - | POS +$82.4M | - | 135 | 125 | -$3.7M | +$30k bull / +$0 bear | out (clean 29, ADX 10, RVol 0.2) |
| 12 | **AMD** | 487.80 | - | **-** | 16 | - | NEG -$88.3M | - | 520 | 440 | +$8.4M | +$3.2M bull / +$0 bear | out (clean 31, ADX 16, RVol 0.5) |
| 13 | **QQQ** | 685.99 | - | **-** | 15 | - | NEG -$5.1B | - | 700 | 680 | +$15.5M | +$2.8M bull / +$0 bear | out (clean 29, ADX 14, RVol 0.9) |
| 14 | **DELL** | 406.51 | - | **-** | 15 | - | NEG -$26.3M | - | 440 | 400 | +$778k | +$36k bull / +$0 bear | out (clean 32, ADX 11, RVol 0.4) |
| 15 | **SMCI** | 31.42 | - | **-** | 15 | - | POS +$1.9M | - | 34.5 | 30 | -$41k | +$0 bull / -$87k bear | out (clean 33, ADX 14, RVol 1.2) |
| 16 | **IWM** | 280.67 | - | **-** | 14 | - | NEG -$1.2B | 286.86 | 285 | 270 | -$1.4M | +$318k bull / +$0 bear | out (clean 32, ADX 13, RVol 0.5) |
| 17 | **AAPL** | 332.28 | - | **-** | 14 | - | NEG -$389.1M | 342.91 | 350 | 330 | -$8.9M | +$0 bull / -$102k bear | out (clean 30, ADX 11, RVol 0.4) |
| 18 | **PLTR** | 174.14 | - | **-** | 14 | - | NEG -$24.9M | - | 165 | 180 | +$89k | +$399k bull / +$0 bear | out (clean 27, ADX 18, RVol 0.3) |
| 19 | **MU** | 850.95 | - | **-** | 14 | - | NEG -$205.2M | - | 900 | 850 | -$13.6M | +$2.6M bull / -$3.7M bear | out (clean 31, ADX 12, RVol 0.4) |
| 20 | **COIN** | 146.01 | - | **-** | 10 | - | POS +$21.3M | - | 148 | 150 | -$2.1M | - | out (clean 30, ADX 28, RVol 0.2) |
| 21 | **UBER** | 66.87 | - | **-** | 10 | - | NEG -$8.5M | - | 70 | 65 | -$360k | - | out (clean 30, ADX 14, RVol 1.2) |
| 22 | **CRM** | 222.82 | - | **-** | 10 | - | NEG -$14.1M | - | 240 | 220 | -$331k | - | out (clean 29, ADX 17, RVol 0.4) |
| 23 | **GOOGL** | 279.37 | - | **-** | 6 | - | NEG -$39.5M | 284.93 | 285 | 290 | +$2.8M | - | out (clean 33, ADX 17, RVol 0.2) |
| 24 | **ARM** | 201.64 | - | **-** | 6 | - | NEG -$6.6M | - | 220 | 200 | -$101k | - | out (clean 25, ADX 19, RVol 0.4) |
| 25 | **BABA** | 100.56 | - | **-** | 6 | - | POS +$1.6M | 99.99 | 102 | 100 | +$66k | - | out (clean 36, ADX 25, RVol 0.2) |
| 26 | **SPY** | 755.39 | - | **-** | 5 | - | NEG -$9.0B | 770.3 | 770 | 750 | -$42.3M | - | out (clean 30, ADX 16, RVol 0.5) |
| 27 | **HOOD** | 85.26 | - | **-** | 4 | - | NEG -$2.8M | - | 90 | 90 | -$86k | - | out (clean 30, ADX 11, RVol 0.7) |

## Big prints this scan (68)
- **MU** PUT 850 2026-11-09 (6DTE): 998 @ 28.65 = **+$2.9M** BUY | vol 1,349 / OI 106
- **QQQ** PUT 689 2026-11-05 (2DTE): 500 @ 9.98 = **+$499k** SELL | vol 1,258 / OI 0
- **QQQ** PUT 688 2026-11-05 (2DTE): 500 @ 9.49 = **+$474k** SELL | vol 1,628 / OI 0
- **AMD** CALL 477.5 2026-11-06 (3DTE): 96 @ 27.82 = **+$267k** BUY | vol 803 / OI 39
- **AMD** CALL 477.5 2026-11-06 (3DTE): 96 @ 27.80 = **+$267k** BUY | vol 803 / OI 39
- **QQQ** PUT 687 2026-11-04 (1DTE): 337 @ 7.20 = **+$243k** SELL | vol 13,856 / OI 343
- **QQQ** CALL 710 2026-11-05 (2DTE): 2,155 @ 1.11 = **+$239k** BUY | vol 4,764 / OI 3,199
- **QQQ** PUT 687 2026-11-04 (1DTE): 305 @ 7.36 = **+$224k** SELL | vol 13,856 / OI 343
- **QQQ** CALL 700 2026-11-06 (3DTE): 431 @ 4.48 = **+$193k** BUY | vol 12,561 / OI 13,477
- **QQQ** PUT 687 2026-11-04 (1DTE): 250 @ 7.21 = **+$180k** SELL | vol 13,856 / OI 343
- **QQQ** PUT 687 2026-11-04 (1DTE): 250 @ 7.18 = **+$180k** SELL | vol 13,856 / OI 343
- **QQQ** PUT 687 2026-11-04 (1DTE): 250 @ 7.05 = **+$176k** SELL | vol 13,856 / OI 343
- **AMD** CALL 497.5 2026-11-09 (6DTE): 90 @ 18.98 = **+$171k** BUY | vol 248 / OI 13
- **AMD** PUT 480 2026-11-04 (1DTE): 100 @ 15.35 = **+$154k** SELL | vol 1,223 / OI 286
- **MU** CALL 860 2026-11-04 (1DTE): 130 @ 11.80 = **+$153k** SELL | vol 11,885 / OI 60

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 761 2026-11-06 (3DTE): 1,792 traded vs OI 1,749
- **SPY** CALL 785 2026-11-04 (1DTE): 834 traded vs OI 809
- **SPY** PUT 731 2026-11-11 (8DTE): 560 traded vs OI 0
- **SPY** CALL 799 2026-11-11 (8DTE): 1,873 traded vs OI 0
- **QQQ** PUT 645 2026-11-05 (2DTE): 517 traded vs OI 0
- **QQQ** CALL 710 2026-11-05 (2DTE): 4,764 traded vs OI 3,199
- **QQQ** CALL 719 2026-11-04 (1DTE): 523 traded vs OI 379
- **QQQ** CALL 722 2026-11-04 (1DTE): 911 traded vs OI 626
- **QQQ** CALL 681 2026-11-04 (1DTE): 511 traded vs OI 37
- **IWM** CALL 285 2026-11-04 (1DTE): 3,943 traded vs OI 3,937
- **NVDA** CALL 195 2026-11-13 (10DTE): 576 traded vs OI 247
- **AMZN** CALL 270 2026-11-04 (1DTE): 958 traded vs OI 608
- **NFLX** CALL 67 2026-11-06 (3DTE): 2,838 traded vs OI 2,798
- **NFLX** PUT 57 2026-11-13 (10DTE): 1,211 traded vs OI 754
- **UBER** PUT 70 2026-11-06 (3DTE): 781 traded vs OI 717

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
