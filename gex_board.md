# GEX + FLOW SCAN - Tue Nov 03, 01:40 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 13:40:08 ET, last candle SPY 13:39, QQQ 13:39 | no errors

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **MSFT** | 520.65 | - | **-** | 29 | - | POS +$255.6M | 501.85 | 540 | 500 | -$11.5M | +$0 bull / -$56k bear | out (clean 29, ADX 42, RVol 0.6) |
| 2 | **ORCL** | 126.78 | - | **-** | 26 | - | NEG -$38.4M | - | 135 | 125 | -$9.7M | +$675k bull / +$0 bear | out (clean 33, ADX 35, RVol 0.5) |
| 3 | **META** | 622.83 | - | **-** | 23 | - | NEG -$18.1M | 625.45 | 650 | 610 | -$17.5M | +$537k bull / +$0 bear | out (clean 28, ADX 31, RVol 0.4) |
| 4 | **AMZN** | 251.00 | - | **-** | 22 | - | POS +$177.7M | - | 250 | 250 | -$4.2M | +$0 bull / -$132k bear | out (clean 33, ADX 36, RVol 0.7) |
| 5 | **MSTR** | 136.28 | - | **-** | 19 | - | POS +$83.0M | - | 135 | 125 | -$4.7M | +$30k bull / +$0 bear | out (clean 29, ADX 15, RVol 0.1) |
| 6 | **SHOP** | 147.29 | - | **-** | 19 | - | NEG -$4.0M | - | 145 | 150 | -$4.3M | - | out (clean 34, ADX 14, RVol 1.0) |
| 7 | **AVGO** | 332.32 | - | **-** | 18 | - | NEG -$64.6M | - | 340 | 340 | +$3.1M | +$71k bull / +$0 bear | out (clean 31, ADX 12, RVol 0.3) |
| 8 | **SPY** | 756.40 | - | **-** | 17 | - | NEG -$8.1B | 770.2 | 770 | 750 | -$79.9M | +$968k bull / -$1.1M bear | out (clean 29, ADX 20, RVol 0.6) |
| 9 | **IWM** | 281.22 | - | **-** | 17 | - | NEG -$1.0B | 286.87 | 285 | 270 | -$4.4M | +$0 bull / -$915k bear | out (clean 32, ADX 19, RVol 0.6) |
| 10 | **TSLA** | 398.54 | - | **-** | 17 | - | POS +$201.3M | - | 400 | 400 | +$15.7M | +$345k bull / -$245k bear | out (clean 31, ADX 24, RVol 0.5) |
| 11 | **QQQ** | 687.35 | - | **-** | 15 | - | NEG -$5.0B | - | 700 | 680 | -$19.4M | +$124k bull / -$449k bear | out (clean 29, ADX 16, RVol 0.6) |
| 12 | **NVDA** | 208.04 | - | **-** | 15 | - | POS +$117.0M | 203.74 | 210 | 200 | +$9.3M | +$297k bull / -$128k bear | out (clean 29, ADX 13, RVol 0.5) |
| 13 | **AAPL** | 331.86 | - | **-** | 15 | - | NEG -$389.4M | 343.16 | 350 | 330 | -$8.3M | +$65k bull / -$283k bear | out (clean 30, ADX 12, RVol 0.6) |
| 14 | **AMD** | 492.30 | - | **-** | 15 | - | NEG -$67.0M | - | 520 | 500 | +$1.7M | +$70k bull / -$240k bear | out (clean 31, ADX 16, RVol 0.7) |
| 15 | **PLTR** | 175.65 | - | **-** | 15 | - | NEG -$24.8M | - | 165 | 180 | -$1.3M | +$184k bull / -$66k bear | out (clean 27, ADX 18, RVol 0.6) |
| 16 | **BABA** | 100.31 | - | **-** | 14 | - | POS +$1.0M | 99.97 | 102 | 100 | +$247k | - | out (clean 36, ADX 35, RVol 0.5) |
| 17 | **MU** | 852.47 | - | **-** | 13 | - | NEG -$203.7M | - | 900 | 850 | -$14.5M | +$852k bull / -$1.5M bear | out (clean 31, ADX 10, RVol 0.3) |
| 18 | **COIN** | 146.45 | - | **-** | 12 | - | POS +$21.0M | - | 148 | 150 | -$2.3M | - | out (clean 29, ADX 31, RVol 0.3) |
| 19 | **CRM** | 222.88 | - | **-** | 12 | - | NEG -$14.0M | - | 240 | 220 | -$368k | - | out (clean 29, ADX 16, RVol 1.2) |
| 20 | **NFLX** | 63.06 | - | **-** | 11 | - | NEG -$8.6M | 64.56 | 63 | 60 | -$533k | - | out (clean 27, ADX 29, RVol 0.6) |
| 21 | **UBER** | 66.72 | - | **-** | 8 | - | NEG -$8.5M | - | 70 | 65 | -$232k | - | out (clean 29, ADX 16, RVol 0.5) |
| 22 | **SMCI** | 31.71 | - | **-** | 7 | - | POS +$2.0M | - | 34.5 | 30 | -$579k | - | out (clean 33, ADX 14, RVol 1.1) |
| 23 | **GOOGL** | 280.10 | - | **-** | 6 | - | NEG -$31.7M | 284.83 | 285 | 290 | +$2.0M | - | out (clean 33, ADX 18, RVol 0.2) |
| 24 | **SMH** | 520.34 | - | **-** | 5 | - | NEG -$282.1M | - | 532.5 | 500 | +$930k | - | out (clean 31, ADX 13, RVol 0.3) |
| 25 | **ARM** | 202.72 | - | **-** | 5 | - | NEG -$6.6M | - | 220 | 200 | -$156k | - | out (clean 25, ADX 10, RVol 0.4) |
| 26 | **DELL** | 409.19 | - | **-** | 4 | - | NEG -$26.0M | - | 440 | 400 | +$654k | - | out (clean 32, ADX 13, RVol 0.1) |
| 27 | **HOOD** | 85.04 | - | **-** | 3 | - | NEG -$2.7M | - | 90 | 90 | -$102k | - | out (clean 31, ADX 10, RVol 0.5) |

## Big prints this scan (52)
- **MU** PUT 890 2026-11-04 (1DTE): 56 @ 43.00 = **+$241k** BUY | vol 266 / OI 327
- **IWM** CALL 282 2026-11-04 (1DTE): 1,196 @ 1.61 = **+$193k** SELL | vol 6,175 / OI 417
- **NVDA** PUT 207.5 2026-11-09 (6DTE): 341 @ 4.50 = **+$153k** MID | vol 5,133 / OI 81
- **IWM** CALL 281 2026-11-04 (1DTE): 532 @ 2.10 = **+$112k** SELL | vol 4,132 / OI 522
- **SPY** CALL 752 2026-11-03 (0DTE): 250 @ 4.32 = **+$108k** SELL | vol 30,262 / OI 1,002
- **AMD** PUT 475 2026-11-06 (3DTE): 70 @ 15.06 = **+$105k** BUY | vol 896 / OI 940
- **META** PUT 620 2026-11-06 (3DTE): 100 @ 10.20 = **+$102k** SELL | vol 1,599 / OI 1,386
- **MU** PUT 830 2026-11-04 (1DTE): 100 @ 8.95 = **+$90k** BUY | vol 7,416 / OI 430
- **IWM** CALL 280 2026-11-03 (0DTE): 776 @ 1.15 = **+$89k** SELL | vol 39,753 / OI 1,006
- **MU** PUT 830 2026-11-04 (1DTE): 85 @ 9.25 = **+$79k** BUY | vol 7,416 / OI 430
- **TSLA** PUT 397.5 2026-11-04 (1DTE): 134 @ 5.80 = **+$78k** BUY | vol 20,572 / OI 2,674
- **AMD** PUT 500 2026-11-04 (1DTE): 30 @ 23.50 = **+$70k** SELL | vol 437 / OI 430
- **MU** PUT 860 2026-11-04 (1DTE): 26 @ 22.70 = **+$59k** BUY | vol 9,193 / OI 273
- **IWM** CALL 281 2026-11-04 (1DTE): 280 @ 2.10 = **+$59k** SELL | vol 4,132 / OI 522
- **AMZN** CALL 242.5 2026-11-06 (3DTE): 56 @ 9.70 = **+$54k** MID | vol 575 / OI 3,278

## New unusual volume (traded more than open interest, 500+)
- **QQQ** PUT 640 2026-11-04 (1DTE): 1,238 traded vs OI 1,200
- **QQQ** PUT 657 2026-11-06 (3DTE): 2,109 traded vs OI 0
- **QQQ** CALL 721 2026-11-03 (0DTE): 504 traded vs OI 352
- **QQQ** CALL 713 2026-11-04 (1DTE): 701 traded vs OI 693
- **QQQ** CALL 687 2026-11-20 (17DTE): 549 traded vs OI 384
- **IWM** PUT 274 2026-11-09 (6DTE): 539 traded vs OI 162
- **AAPL** CALL 355 2026-11-09 (6DTE): 1,928 traded vs OI 164
- **META** PUT 660 2026-11-04 (1DTE): 503 traded vs OI 49
- **MSFT** CALL 522.5 2026-11-06 (3DTE): 592 traded vs OI 538
- **SMCI** CALL 33.5 2026-11-20 (17DTE): 1,332 traded vs OI 1,127
- **ORCL** CALL 138 2026-11-13 (10DTE): 1,416 traded vs OI 0
- **ORCL** PUT 125 2026-11-06 (3DTE): 4,688 traded vs OI 4,669
- **HOOD** PUT 85 2026-11-06 (3DTE): 2,485 traded vs OI 2,379

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
