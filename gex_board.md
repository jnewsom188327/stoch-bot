# GEX + FLOW SCAN - Tue Nov 03, 02:40 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 14:40:08 ET, last candle SPY 14:39, QQQ 14:39 | no errors

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **TSLA** | 399.01 | PINNED between the walls (positive gamma) - chop | **-** | 28 | - | POS +$207.0M | - | 400 | 400 | +$16.2M | +$901k bull / -$27k bear | out (clean 31, ADX 19, RVol 0.3) |
| 2 | **MSFT** | 521.61 | - | **-** | 27 | - | POS +$267.5M | 502 | 540 | 500 | -$12.2M | +$183k bull / +$0 bear | out (clean 28, ADX 41, RVol 0.6) |
| 3 | **ORCL** | 124.72 | - | **-** | 24 | - | NEG -$41.0M | - | 135 | 125 | -$8.9M | +$141k bull / +$0 bear | out (clean 34, ADX 35, RVol 0.6) |
| 4 | **META** | 621.44 | - | **-** | 20 | - | NEG -$29.9M | 625.76 | 650 | 610 | -$15.5M | +$123k bull / -$323k bear | out (clean 29, ADX 23, RVol 0.3) |
| 5 | **AMZN** | 251.35 | - | **-** | 20 | - | POS +$182.2M | - | 250 | 250 | -$3.7M | +$0 bull / -$103k bear | out (clean 33, ADX 38, RVol 0.5) |
| 6 | **SHOP** | 144.76 | - | **-** | 19 | - | NEG -$3.8M | - | 145 | 148 | -$4.0M | - | out (clean 34, ADX 24, RVol 1.0) |
| 7 | **SMH** | 517.42 | - | **-** | 18 | - | NEG -$297.8M | - | 532.5 | 500 | +$2.1M | +$73k bull / +$0 bear | out (clean 32, ADX 18, RVol 0.5) |
| 8 | **NVDA** | 207.01 | - | **-** | 18 | - | POS +$87.6M | 203.72 | 210 | 200 | +$15.3M | +$536k bull / +$0 bear | out (clean 29, ADX 21, RVol 0.5) |
| 9 | **AVGO** | 331.98 | - | **-** | 18 | - | NEG -$66.9M | - | 340 | 340 | +$3.9M | +$543k bull / +$0 bear | out (clean 30, ADX 12, RVol 0.4) |
| 10 | **GOOGL** | 279.07 | - | **-** | 17 | - | NEG -$40.2M | 284.71 | 285 | 290 | +$3.0M | +$56k bull / +$0 bear | out (clean 33, ADX 19, RVol 0.3) |
| 11 | **MSTR** | 135.72 | - | **-** | 17 | - | POS +$82.9M | - | 135 | 125 | -$3.4M | +$121k bull / +$0 bear | out (clean 29, ADX 11, RVol 0.3) |
| 12 | **AMD** | 486.99 | - | **-** | 16 | - | NEG -$87.8M | - | 520 | 440 | +$9.0M | +$2.6M bull / +$0 bear | out (clean 32, ADX 17, RVol 0.6) |
| 13 | **SMCI** | 31.82 | - | **-** | 16 | - | POS +$2.1M | - | 34.5 | 30 | -$101k | +$0 bull / -$129k bear | out (clean 33, ADX 15, RVol 1.7) |
| 14 | **SPY** | 755.00 | - | **-** | 15 | - | NEG -$9.0B | 770.2 | 770 | 750 | -$29.0M | +$444k bull / +$0 bear | out (clean 30, ADX 16, RVol 0.5) |
| 15 | **QQQ** | 685.67 | - | **-** | 15 | - | NEG -$5.1B | - | 700 | 680 | +$19.3M | +$2.9M bull / +$0 bear | out (clean 29, ADX 15, RVol 1.0) |
| 16 | **PLTR** | 173.65 | - | **-** | 15 | - | NEG -$24.0M | - | 165 | 180 | +$695k | +$306k bull / +$0 bear | out (clean 27, ADX 18, RVol 0.6) |
| 17 | **DELL** | 407.07 | - | **-** | 15 | - | NEG -$26.4M | - | 440 | 400 | +$706k | +$36k bull / +$0 bear | out (clean 32, ADX 12, RVol 0.3) |
| 18 | **AAPL** | 331.66 | - | **-** | 14 | - | NEG -$383.2M | 342.3 | 350 | 330 | -$8.1M | +$70k bull / -$138k bear | out (clean 30, ADX 10, RVol 0.3) |
| 19 | **HOOD** | 85.39 | - | **-** | 14 | - | NEG -$2.5M | - | 90 | 90 | -$125k | +$0 bull / -$28k bear | out (clean 30, ADX 13, RVol 0.7) |
| 20 | **IWM** | 280.56 | - | **-** | 13 | - | NEG -$1.2B | 286.83 | 285 | 270 | -$66k | +$388k bull / +$0 bear | out (clean 33, ADX 14, RVol 0.5) |
| 21 | **MU** | 849.73 | - | **-** | 13 | - | NEG -$207.2M | - | 900 | 850 | -$11.3M | +$1.9M bull / -$3.5M bear | out (clean 31, ADX 10, RVol 0.3) |
| 22 | **UBER** | 66.72 | - | **-** | 11 | - | NEG -$8.6M | - | 70 | 65 | -$446k | - | out (clean 30, ADX 15, RVol 1.1) |
| 23 | **NFLX** | 63.02 | - | **-** | 10 | - | NEG -$7.4M | 64.19 | 63 | 60 | -$321k | - | out (clean 28, ADX 35, RVol 0.7) |
| 24 | **COIN** | 146.15 | - | **-** | 10 | - | POS +$21.6M | - | 148 | 150 | -$2.1M | - | out (clean 30, ADX 26, RVol 0.3) |
| 25 | **CRM** | 222.56 | - | **-** | 10 | - | NEG -$14.2M | - | 240 | 220 | -$326k | - | out (clean 29, ADX 15, RVol 0.5) |
| 26 | **ARM** | 201.25 | - | **-** | 6 | - | NEG -$6.6M | - | 220 | 200 | -$80k | - | out (clean 25, ADX 22, RVol 0.4) |
| 27 | **BABA** | 100.53 | - | **-** | 6 | - | POS +$1.8M | 99.95 | 102 | 100 | +$70k | - | out (clean 36, ADX 25, RVol 0.2) |

## Big prints this scan (43)
- **IWM** PUT 275 2026-11-06 (3DTE): 3,500 @ 1.11 = **+$388k** SELL | vol 4,595 / OI 23,758
- **QQQ** PUT 687 2026-11-04 (1DTE): 167 @ 7.13 = **+$119k** SELL | vol 15,402 / OI 343
- **META** CALL 625 2026-11-04 (1DTE): 198 @ 5.73 = **+$113k** SELL | vol 8,923 / OI 334
- **META** PUT 625 2026-11-04 (1DTE): 100 @ 9.40 = **+$94k** MID | vol 770 / OI 179
- **TSLA** PUT 400 2026-11-04 (1DTE): 132 @ 5.90 = **+$78k** SELL | vol 34,722 / OI 1,549
- **AMD** PUT 490 2026-11-09 (6DTE): 32 @ 24.12 = **+$77k** SELL | vol 168 / OI 39
- **NVDA** PUT 210 2026-11-04 (1DTE): 180 @ 4.15 = **+$75k** SELL | vol 13,444 / OI 2,044
- **NVDA** CALL 205 2026-11-04 (1DTE): 173 @ 4.30 = **+$74k** BUY | vol 5,917 / OI 2,680
- **NVDA** CALL 210 2026-11-06 (3DTE): 245 @ 3.00 = **+$74k** BUY | vol 20,643 / OI 22,751
- **MU** CALL 860 2026-11-04 (1DTE): 46 @ 13.10 = **+$60k** BUY | vol 12,214 / OI 60
- **AMD** CALL 485 2026-11-04 (1DTE): 26 @ 20.65 = **+$54k** BUY | vol 1,870 / OI 71
- **NVDA** CALL 207.5 2026-11-04 (1DTE): 200 @ 2.61 = **+$52k** BUY | vol 30,410 / OI 2,809
- **MU** PUT 870 2026-11-06 (3DTE): 15 @ 34.35 = **+$52k** SELL | vol 1,130 / OI 775
- **MU** PUT 870 2026-11-06 (3DTE): 15 @ 34.35 = **+$52k** SELL | vol 1,130 / OI 775
- **MU** CALL 855 2026-11-06 (3DTE): 21 @ 24.37 = **+$51k** BUY | vol 2,122 / OI 99

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 733 2026-11-05 (2DTE): 779 traded vs OI 0
- **SPY** CALL 825 2026-11-13 (10DTE): 2,617 traded vs OI 933
- **SPY** CALL 820 2026-11-13 (10DTE): 2,820 traded vs OI 1,766
- **SPY** CALL 819 2026-11-13 (10DTE): 2,700 traded vs OI 34
- **QQQ** PUT 654 2026-11-04 (1DTE): 512 traded vs OI 0
- **QQQ** PUT 625 2026-11-05 (2DTE): 1,072 traded vs OI 0
- **QQQ** CALL 700 2026-11-27 (24DTE): 1,599 traded vs OI 808
- **NVDA** PUT 220 2026-11-09 (6DTE): 583 traded vs OI 73
- **AAPL** CALL 332.5 2026-11-09 (6DTE): 511 traded vs OI 3
- **NFLX** CALL 63 2026-11-06 (3DTE): 15,142 traded vs OI 15,133

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
