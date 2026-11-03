# GEX + FLOW SCAN - Tue Nov 03, 03:55 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 15:32:08 ET, last candle SPY 15:31, QQQ 15:31 | no errors

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **AMZN** | 250.57 | PINNED between the walls (positive gamma) - chop | **-** | 39 | - | POS +$209.8M | - | 250 | 250 | -$3.6M | +$61k bull / +$0 bear | out (clean 33, ADX 35, RVol 1.5) |
| 2 | **MSFT** | 522.11 | - | **-** | 27 | - | POS +$341.8M | 499.76 | 540 | 500 | -$12.7M | +$112k bull / -$133k bear | out (clean 28, ADX 36, RVol 1.3) |
| 3 | **ARM** | 202.28 | - | **-** | 23 | - | NEG -$6.8M | - | 220 | 200 | -$773k | +$140k bull / +$0 bear | out (clean 26, ADX 25, RVol 1.0) |
| 4 | **SHOP** | 143.75 | - | **-** | 23 | - | NEG -$4.6M | - | 145 | 148 | -$3.8M | - | out (clean 34, ADX 42, RVol 3.6) |
| 5 | **META** | 620.65 | - | **-** | 22 | - | NEG -$31.1M | 624.95 | 650 | 610 | -$15.0M | +$168k bull / -$272k bear | out (clean 29, ADX 29, RVol 1.0) |
| 6 | **UBER** | 66.61 | - | **-** | 21 | - | NEG -$12.6M | - | 70 | 65 | -$311k | +$59k bull / +$0 bear | out (clean 30, ADX 18, RVol 2.5) |
| 7 | **NVDA** | 206.59 | - | **-** | 19 | - | POS +$84.7M | 204.02 | 210 | 200 | +$16.4M | +$359k bull / -$343k bear | out (clean 29, ADX 22, RVol 1.0) |
| 8 | **AMD** | 485.86 | - | **-** | 19 | - | NEG -$87.3M | - | 520 | 440 | +$8.3M | +$140k bull / -$519k bear | out (clean 32, ADX 21, RVol 1.7) |
| 9 | **IWM** | 279.55 | - | **-** | 18 | - | NEG -$1.4B | 286.84 | 285 | 270 | +$2.6M | +$368k bull / +$0 bear | out (clean 33, ADX 26, RVol 1.1) |
| 10 | **QQQ** | 685.47 | - | **-** | 17 | - | NEG -$5.1B | - | 700 | 680 | +$31.8M | +$338k bull / -$1.2M bear | out (clean 29, ADX 15, RVol 1.6) |
| 11 | **SMH** | 518.02 | - | **-** | 17 | - | NEG -$293.8M | - | 532.5 | 500 | +$1.3M | +$0 bull / -$85k bear | out (clean 32, ADX 17, RVol 1.1) |
| 12 | **AAPL** | 331.75 | - | **-** | 17 | - | NEG -$398.1M | 342.08 | 350 | 330 | -$8.8M | +$144k bull / -$463k bear | out (clean 30, ADX 17, RVol 1.4) |
| 13 | **GOOGL** | 279.60 | - | **-** | 17 | - | NEG -$32.0M | 284.31 | 285 | 290 | +$2.3M | +$0 bull / -$69k bear | out (clean 33, ADX 23, RVol 0.5) |
| 14 | **SPY** | 754.11 | - | **-** | 16 | - | NEG -$9.6B | 770.19 | 770 | 750 | -$3.1M | +$2.9M bull / -$1.1M bear | out (clean 29, ADX 18, RVol 1.4) |
| 15 | **TSLA** | 398.49 | - | **-** | 16 | - | POS +$208.3M | - | 400 | 400 | +$17.8M | +$0 bull / -$314k bear | out (clean 31, ADX 14, RVol 0.7) |
| 16 | **PLTR** | 175.77 | - | **-** | 15 | - | NEG -$18.4M | - | 190 | 180 | +$647k | +$128k bull / -$29k bear | out (clean 27, ADX 14, RVol 1.0) |
| 17 | **DELL** | 407.91 | - | **-** | 15 | - | NEG -$26.4M | - | 440 | 400 | +$559k | +$0 bull / -$84k bear | out (clean 32, ADX 12, RVol 0.6) |
| 18 | **MU** | 852.39 | - | **-** | 15 | - | NEG -$216.9M | - | 900 | 850 | -$19.0M | +$0 bull / -$2.8M bear | out (clean 31, ADX 14, RVol 0.6) |
| 19 | **HOOD** | 85.40 | - | **-** | 15 | - | NEG -$70k | 85.6 | 90 | 90 | -$307k | +$0 bull / -$42k bear | out (clean 30, ADX 14, RVol 1.0) |
| 20 | **ORCL** | 126.36 | - | **-** | 14 | - | NEG -$39.6M | - | 135 | 125 | -$9.6M | - | out (clean 36, ADX 30, RVol 1.1) |
| 21 | **AVGO** | 331.56 | - | **-** | 10 | - | NEG -$70.5M | - | 340 | 340 | +$4.3M | - | out (clean 30, ADX 12, RVol 1.1) |
| 22 | **CRM** | 222.06 | - | **-** | 10 | - | NEG -$14.4M | - | 240 | 220 | -$182k | - | out (clean 30, ADX 20, RVol 1.9) |
| 23 | **NFLX** | 63.36 | - | **-** | 9 | - | NEG -$3.1M | 63.87 | 65 | 65 | -$183k | - | out (clean 29, ADX 25, RVol 1.7) |
| 24 | **COIN** | 145.75 | - | **-** | 9 | - | POS +$20.6M | - | 148 | 140 | -$1.9M | - | out (clean 30, ADX 18, RVol 0.8) |
| 25 | **SMCI** | 31.48 | - | **-** | 9 | - | POS +$2.0M | - | 34.5 | 30 | +$612k | - | out (clean 33, ADX 11, RVol 2.4) |
| 26 | **MSTR** | 135.78 | - | **-** | 8 | - | POS +$92.7M | - | 135 | 125 | -$3.4M | - | out (clean 29, ADX 14, RVol 0.7) |
| 27 | **BABA** | 100.47 | - | **-** | 7 | - | POS +$977k | 100.02 | 102 | 100 | +$115k | - | out (clean 34, ADX 19, RVol 0.7) |

## Big prints this scan (65)
- **SPY** PUT 760 2026-11-05 (2DTE): 500 @ 8.50 = **+$425k** BUY | vol 12,525 / OI 2,551
- **SPY** PUT 760 2026-11-05 (2DTE): 500 @ 8.50 = **+$425k** BUY | vol 12,525 / OI 2,551
- **AAPL** PUT 345 2026-11-06 (3DTE): 243 @ 14.06 = **+$342k** BUY | vol 852 / OI 4,291
- **SPY** PUT 767 2026-11-04 (1DTE): 200 @ 13.44 = **+$269k** BUY | vol 8,460 / OI 18,478
- **MU** PUT 835 2026-11-06 (3DTE): 150 @ 17.27 = **+$259k** BUY | vol 1,181 / OI 411
- **MU** PUT 820 2026-11-06 (3DTE): 150 @ 12.17 = **+$183k** BUY | vol 1,267 / OI 857
- **QQQ** CALL 690 2026-11-05 (2DTE): 246 @ 6.54 = **+$161k** SELL | vol 3,486 / OI 451
- **QQQ** PUT 670 2026-11-05 (2DTE): 395 @ 3.53 = **+$139k** BUY | vol 12,531 / OI 683
- **QQQ** CALL 690 2026-11-05 (2DTE): 198 @ 6.56 = **+$130k** SELL | vol 3,486 / OI 451
- **QQQ** CALL 690 2026-11-05 (2DTE): 198 @ 6.56 = **+$130k** SELL | vol 3,486 / OI 451
- **QQQ** CALL 690 2026-11-04 (1DTE): 246 @ 4.77 = **+$117k** MID | vol 19,316 / OI 2,234
- **QQQ** CALL 690 2026-11-05 (2DTE): 156 @ 6.56 = **+$102k** SELL | vol 3,486 / OI 451
- **QQQ** CALL 690 2026-11-05 (2DTE): 154 @ 6.56 = **+$101k** SELL | vol 3,486 / OI 451
- **QQQ** CALL 690 2026-11-05 (2DTE): 154 @ 6.55 = **+$101k** SELL | vol 3,486 / OI 451
- **IWM** PUT 280 2026-11-04 (1DTE): 389 @ 2.12 = **+$82k** SELL | vol 7,084 / OI 1,843

## New unusual volume (traded more than open interest, 500+)
- **QQQ** CALL 720 2026-11-04 (1DTE): 2,176 traded vs OI 2,174
- **QQQ** CALL 745 2026-11-04 (1DTE): 686 traded vs OI 558
- **IWM** PUT 275 2026-11-13 (10DTE): 6,500 traded vs OI 1,685
- **IWM** PUT 264 2026-11-04 (1DTE): 1,185 traded vs OI 142
- **IWM** CALL 290 2026-11-04 (1DTE): 1,190 traded vs OI 522
- **SMH** PUT 495 2026-11-04 (1DTE): 717 traded vs OI 48
- **SMH** CALL 540 2026-11-04 (1DTE): 1,115 traded vs OI 900
- **TSLA** CALL 397.5 2026-11-13 (10DTE): 522 traded vs OI 252
- **TSLA** CALL 420 2026-11-06 (3DTE): 8,205 traded vs OI 8,099
- **UBER** CALL 68 2026-11-06 (3DTE): 1,206 traded vs OI 1,148

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
