# GEX + FLOW SCAN - Tue Nov 03, 12:30 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 12:30:08 ET, last candle SPY 12:29, QQQ 12:29 | no errors

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **BABA** | 100.14 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 35 | none: 20 calls 0-7DTE > 3 priced 0.40-0.80 > 2 delta 0.2+ > 2 spread ok > 2 liquid > best one only +0% at the target (needs +20%) (1 contracts' greeks worked out here) | POS +$411k | 99.95 | 102 | 100 | +$271k | - | out (clean 36, ADX 55, RVol 0.4) |
| 2 | **META** | 623.32 | - | **-** | 28 | - | NEG -$20.2M | 626.12 | 650 | 610 | -$19.9M | +$0 bull / -$448k bear | out (clean 28, ADX 47, RVol 0.5) |
| 3 | **ORCL** | 126.83 | - | **-** | 27 | - | NEG -$39.9M | - | 135 | 125 | -$7.9M | +$0 bull / -$1.8M bear | out (clean 33, ADX 35, RVol 0.5) |
| 4 | **SHOP** | 147.82 | - | **-** | 22 | - | NEG -$3.6M | - | 145 | 148 | -$4.4M | - | out (clean 32, ADX 21, RVol 1.1) |
| 5 | **COIN** | 149.12 | - | **-** | 21 | - | POS +$20.5M | - | 148 | 150 | -$4.0M | - | out (clean 28, ADX 48, RVol 0.2) |
| 6 | **TSLA** | 397.32 | - | **-** | 20 | - | POS +$184.0M | - | 400 | 380 | +$18.5M | +$1.5M bull / -$88k bear | out (clean 31, ADX 37, RVol 0.3) |
| 7 | **AVGO** | 333.12 | - | **-** | 19 | - | NEG -$64.5M | - | 340 | 340 | +$2.4M | +$0 bull / -$89k bear | out (clean 31, ADX 18, RVol 0.5) |
| 8 | **ARM** | 203.75 | - | **-** | 18 | - | NEG -$6.5M | - | 220 | 200 | -$254k | +$39k bull / +$0 bear | out (clean 25, ADX 16, RVol 0.4) |
| 9 | **NVDA** | 208.82 | - | **-** | 17 | - | POS +$123.8M | 203.72 | 210 | 200 | +$6.2M | +$198k bull / -$668k bear | out (clean 29, ADX 22, RVol 0.8) |
| 10 | **GOOGL** | 280.43 | - | **-** | 17 | - | NEG -$36.3M | 285.7 | 285 | 290 | +$2.3M | +$0 bull / -$170k bear | out (clean 32, ADX 17, RVol 0.2) |
| 11 | **SPY** | 755.71 | - | **-** | 16 | - | NEG -$8.9B | 770.72 | 770 | 750 | -$66.3M | +$0 bull / -$769k bear | out (clean 30, ADX 14, RVol 0.4) |
| 12 | **SMH** | 521.86 | - | **-** | 16 | - | NEG -$275.0M | - | 532.5 | 500 | +$499k | +$27k bull / +$0 bear | out (clean 31, ADX 20, RVol 0.4) |
| 13 | **AMD** | 492.64 | - | **-** | 16 | - | NEG -$66.5M | - | 520 | 500 | +$408k | +$356k bull / -$597k bear | out (clean 31, ADX 26, RVol 0.4) |
| 14 | **MSFT** | 517.24 | - | **-** | 16 | - | POS +$194.4M | 501.65 | 540 | 500 | -$8.0M | - | out (clean 28, ADX 30, RVol 0.4) |
| 15 | **AAPL** | 331.32 | - | **-** | 15 | - | NEG -$399.3M | 343.2 | 350 | 330 | -$8.1M | +$52k bull / -$75k bear | out (clean 30, ADX 15, RVol 0.3) |
| 16 | **AMZN** | 248.58 | - | **-** | 15 | - | POS +$150.5M | 236.25 | 250 | 250 | -$669k | +$0 bull / -$101k bear | out (clean 33, ADX 18, RVol 0.5) |
| 17 | **PLTR** | 174.63 | - | **-** | 15 | - | NEG -$25.0M | - | 165 | 180 | -$764k | +$243k bull / -$26k bear | out (clean 27, ADX 20, RVol 0.6) |
| 18 | **HOOD** | 85.40 | - | **-** | 15 | - | NEG -$2.7M | - | 90 | 90 | -$254k | +$0 bull / -$89k bear | out (clean 31, ADX 17, RVol 0.4) |
| 19 | **QQQ** | 687.34 | - | **-** | 14 | - | NEG -$4.9B | - | 700 | 680 | -$26.5M | +$486k bull / -$548k bear | out (clean 29, ADX 16, RVol 0.3) |
| 20 | **MU** | 855.44 | - | **-** | 14 | - | NEG -$195.2M | - | 900 | 850 | -$14.7M | +$2.9M bull / -$2.3M bear | out (clean 31, ADX 14, RVol 0.3) |
| 21 | **MSTR** | 136.47 | - | **-** | 13 | - | POS +$82.2M | - | 135 | 125 | -$4.9M | - | out (clean 29, ADX 29, RVol 0.3) |
| 22 | **CRM** | 222.57 | - | **-** | 11 | - | NEG -$13.9M | - | 240 | 220 | -$374k | - | out (clean 30, ADX 16, RVol 0.4) |
| 23 | **NFLX** | 62.65 | - | **-** | 10 | - | NEG -$10.9M | 64.37 | 63 | 60 | -$477k | - | out (clean 26, ADX 19, RVol 0.4) |
| 24 | **SMCI** | 31.77 | - | **-** | 10 | - | POS +$2.1M | - | 34.5 | 30 | -$909k | - | out (clean 33, ADX 18, RVol 0.8) |
| 25 | **UBER** | 66.86 | - | **-** | 8 | - | NEG -$8.9M | - | 70 | 65 | -$102k | - | out (clean 29, ADX 11, RVol 0.9) |
| 26 | **IWM** | 280.90 | - | **-** | 6 | - | NEG -$1.1B | 287.07 | 285 | 270 | -$2.4M | - | out (clean 32, ADX 19, RVol 0.7) |
| 27 | **DELL** | 407.92 | - | **-** | 6 | - | NEG -$26.2M | - | 440 | 400 | +$977k | - | out (clean 32, ADX 13, RVol 0.3) |

## Big prints this scan (59)
- **ORCL** CALL 126 2026-11-06 (3DTE): 1,000 @ 3.87 = **+$387k** SELL | vol 8,246 / OI 194
- **ORCL** PUT 126 2026-11-06 (3DTE): 1,000 @ 3.57 = **+$357k** BUY | vol 4,406 / OI 1,033
- **ORCL** CALL 126 2026-11-06 (3DTE): 910 @ 3.86 = **+$351k** SELL | vol 8,246 / OI 194
- **ORCL** PUT 126 2026-11-06 (3DTE): 910 @ 3.57 = **+$325k** BUY | vol 4,406 / OI 1,033
- **TSLA** CALL 402.5 2026-11-06 (3DTE): 300 @ 7.15 = **+$214k** BUY | vol 5,526 / OI 5,017
- **AMD** PUT 492.5 2026-11-04 (1DTE): 95 @ 20.05 = **+$190k** SELL | vol 908 / OI 62
- **MU** PUT 860 2026-11-04 (1DTE): 90 @ 19.00 = **+$171k** SELL | vol 8,464 / OI 273
- **PLTR** CALL 180 2026-11-06 (3DTE): 518 @ 2.97 = **+$154k** BUY | vol 27,636 / OI 502
- **TSLA** PUT 400 2026-11-04 (1DTE): 200 @ 7.50 = **+$150k** SELL | vol 31,052 / OI 1,549
- **GOOGL** PUT 280 2026-11-04 (1DTE): 450 @ 3.10 = **+$140k** BUY | vol 4,202 / OI 684
- **MU** PUT 850 2026-11-06 (3DTE): 34 @ 23.15 = **+$79k** SELL | vol 2,446 / OI 1,813
- **MU** PUT 850 2026-11-04 (1DTE): 50 @ 13.85 = **+$69k** SELL | vol 9,211 / OI 414
- **META** PUT 610 2026-11-06 (3DTE): 99 @ 6.85 = **+$68k** MID | vol 681 / OI 3,277
- **MU** PUT 850 2026-11-04 (1DTE): 45 @ 14.15 = **+$64k** SELL | vol 9,211 / OI 414
- **MU** CALL 850 2026-11-06 (3DTE): 20 @ 29.60 = **+$59k** BUY | vol 1,655 / OI 341

## New unusual volume (traded more than open interest, 500+)
- **QQQ** PUT 666 2026-11-04 (1DTE): 791 traded vs OI 765
- **QQQ** PUT 620 2026-11-17 (14DTE): 501 traded vs OI 0
- **QQQ** CALL 700 2026-11-13 (10DTE): 1,755 traded vs OI 1,751
- **TSLA** PUT 377.5 2026-11-06 (3DTE): 748 traded vs OI 705
- **AMD** CALL 515 2026-11-04 (1DTE): 546 traded vs OI 240
- **META** CALL 675 2026-11-06 (3DTE): 530 traded vs OI 0
- **META** CALL 660 2026-11-11 (8DTE): 535 traded vs OI 18
- **META** PUT 622.5 2026-11-04 (1DTE): 553 traded vs OI 91
- **AMZN** PUT 247.5 2026-11-06 (3DTE): 564 traded vs OI 558
- **MSFT** PUT 485 2026-11-04 (1DTE): 500 traded vs OI 211
- **ORCL** PUT 126 2026-11-06 (3DTE): 4,406 traded vs OI 1,033
- **ORCL** CALL 128 2026-11-13 (10DTE): 534 traded vs OI 66

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
