# GEX + FLOW SCAN - Tue Nov 03, 01:10 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 13:10:08 ET, last candle SPY 13:09, QQQ 13:09 | no errors

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **MSFT** | 521.01 | FLOW SURGE | **PUTS** | 38 | none: 126 puts 0-7DTE > 14 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (14 contracts' greeks worked out here) | POS +$253.3M | 501.33 | 540 | 500 | -$10.9M | +$0 bull / -$298k bear | out (clean 28, ADX 42, RVol 0.8) |
| 2 | **BABA** | 100.22 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 34 | none: 20 calls 0-7DTE > 3 priced 0.40-0.80 > 2 delta 0.2+ > 2 spread ok > 2 liquid > best one only +6% at the target (needs +20%) | POS +$1.4M | 99.82 | 102 | 100 | +$303k | - | out (clean 36, ADX 48, RVol 0.2) |
| 3 | **AMZN** | 250.28 | PINNED between the walls (positive gamma) - chop | **-** | 31 | - | POS +$176.9M | - | 250 | 250 | -$2.1M | +$0 bull / -$164k bear | out (clean 32, ADX 25, RVol 0.6) |
| 4 | **COIN** | 147.64 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 29 | none: 22 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$20.6M | - | 148 | 150 | -$2.5M | - | out (clean 29, ADX 33, RVol 0.2) |
| 5 | **ORCL** | 127.98 | - | **-** | 28 | - | NEG -$31.7M | - | 135 | 125 | -$9.3M | +$0 bull / -$252k bear | out (clean 33, ADX 39, RVol 0.7) |
| 6 | **META** | 623.60 | - | **-** | 26 | - | NEG -$12.4M | 625.62 | 650 | 610 | -$19.1M | +$30k bull / -$289k bear | out (clean 28, ADX 37, RVol 0.5) |
| 7 | **TSLA** | 398.44 | - | **-** | 19 | - | POS +$203.3M | - | 400 | 400 | +$14.0M | +$46k bull / -$900k bear | out (clean 31, ADX 34, RVol 0.3) |
| 8 | **SHOP** | 148.77 | - | **-** | 19 | - | NEG -$3.6M | - | 150 | 148 | -$4.5M | - | out (clean 33, ADX 17, RVol 0.6) |
| 9 | **AVGO** | 333.37 | - | **-** | 18 | - | NEG -$43.8M | 351.12 | 340 | 340 | +$2.4M | +$97k bull / -$27k bear | out (clean 31, ADX 15, RVol 0.4) |
| 10 | **SMCI** | 31.73 | - | **-** | 18 | - | POS +$2.1M | - | 34.5 | 30 | -$742k | +$51k bull / +$0 bear | out (clean 33, ADX 14, RVol 1.1) |
| 11 | **SPY** | 756.53 | - | **-** | 16 | - | NEG -$8.0B | 770.41 | 770 | 750 | -$83.8M | +$0 bull / -$818k bear | out (clean 29, ADX 15, RVol 0.3) |
| 12 | **NVDA** | 208.72 | - | **-** | 16 | - | POS +$133.5M | 203.74 | 210 | 200 | +$8.1M | +$123k bull / -$398k bear | out (clean 29, ADX 16, RVol 0.5) |
| 13 | **GOOGL** | 280.88 | - | **-** | 16 | - | NEG -$25.6M | 284.78 | 285 | 290 | +$1.2M | +$61k bull / +$0 bear | out (clean 33, ADX 18, RVol 0.6) |
| 14 | **DELL** | 409.30 | - | **-** | 16 | - | NEG -$25.9M | - | 440 | 400 | +$1.0M | +$28k bull / +$0 bear | out (clean 32, ADX 11, RVol 0.3) |
| 15 | **AAPL** | 330.72 | - | **-** | 15 | - | NEG -$392.7M | 342.64 | 350 | 330 | -$6.9M | +$235k bull / -$161k bear | out (clean 30, ADX 13, RVol 0.8) |
| 16 | **AMD** | 492.53 | - | **-** | 15 | - | NEG -$67.3M | - | 520 | 500 | +$2.5M | +$428k bull / -$1.2M bear | out (clean 31, ADX 17, RVol 0.4) |
| 17 | **QQQ** | 688.10 | - | **-** | 14 | - | NEG -$4.9B | - | 700 | 680 | -$26.1M | +$0 bull / -$1.1M bear | out (clean 29, ADX 15, RVol 0.4) |
| 18 | **MU** | 854.93 | - | **-** | 14 | - | NEG -$196.8M | - | 900 | 850 | -$14.1M | +$1.1M bull / -$2.5M bear | out (clean 31, ADX 11, RVol 0.3) |
| 19 | **HOOD** | 85.14 | - | **-** | 13 | - | NEG -$2.9M | - | 90 | 90 | -$133k | +$0 bull / -$26k bear | out (clean 31, ADX 12, RVol 0.2) |
| 20 | **CRM** | 223.40 | - | **-** | 12 | - | NEG -$13.6M | - | 240 | 220 | -$378k | - | out (clean 30, ADX 14, RVol 0.7) |
| 21 | **NFLX** | 62.77 | - | **-** | 11 | - | NEG -$9.9M | 64.21 | 63 | 60 | -$518k | - | out (clean 27, ADX 25, RVol 0.4) |
| 22 | **MSTR** | 136.71 | - | **-** | 11 | - | POS +$84.0M | - | 135 | 125 | -$5.0M | - | out (clean 29, ADX 20, RVol 0.4) |
| 23 | **UBER** | 66.52 | - | **-** | 8 | - | NEG -$13.5M | - | 70 | 65 | -$94k | - | out (clean 29, ADX 15, RVol 0.9) |
| 24 | **ARM** | 203.94 | - | **-** | 7 | - | NEG -$6.6M | - | 220 | 200 | -$229k | - | out (clean 25, ADX 12, RVol 0.3) |
| 25 | **IWM** | 281.05 | - | **-** | 5 | - | NEG -$1.0B | 287 | 285 | 270 | -$2.2M | - | out (clean 32, ADX 18, RVol 0.3) |
| 26 | **SMH** | 521.56 | - | **-** | 5 | - | NEG -$271.9M | - | 532.5 | 500 | +$856k | - | out (clean 31, ADX 15, RVol 0.4) |
| 27 | **PLTR** | 175.84 | - | **-** | 5 | - | NEG -$24.7M | - | 165 | 180 | -$917k | - | out (clean 27, ADX 15, RVol 0.7) |

## Big prints this scan (45)
- **AMD** CALL 497.5 2026-11-09 (6DTE): 90 @ 21.22 = **+$191k** SELL | vol 122 / OI 13
- **QQQ** PUT 688 2026-11-03 (0DTE): 846 @ 2.10 = **+$178k** BUY | vol 45,222 / OI 553
- **META** CALL 610 2026-11-09 (6DTE): 80 @ 21.88 = **+$175k** MID | vol 236 / OI 129
- **META** CALL 610 2026-11-09 (6DTE): 63 @ 21.88 = **+$138k** MID | vol 236 / OI 129
- **META** CALL 610 2026-11-09 (6DTE): 57 @ 21.88 = **+$125k** MID | vol 236 / OI 129
- **QQQ** PUT 689 2026-11-05 (2DTE): 130 @ 9.58 = **+$125k** BUY | vol 316 / OI 0
- **NVDA** CALL 210 2026-11-06 (3DTE): 250 @ 3.45 = **+$86k** SELL | vol 17,948 / OI 22,751
- **META** PUT 610 2026-11-09 (6DTE): 80 @ 8.27 = **+$66k** BUY | vol 225 / OI 73
- **MU** PUT 875 2026-11-04 (1DTE): 20 @ 29.99 = **+$60k** BUY | vol 671 / OI 241
- **MU** PUT 850 2026-11-06 (3DTE): 24 @ 24.60 = **+$59k** BUY | vol 2,743 / OI 1,813
- **MU** PUT 870 2026-11-04 (1DTE): 20 @ 26.68 = **+$53k** BUY | vol 1,866 / OI 1,093
- **TSLA** CALL 400 2026-11-04 (1DTE): 100 @ 5.25 = **+$52k** SELL | vol 15,474 / OI 1,213
- **META** PUT 610 2026-11-09 (6DTE): 63 @ 8.27 = **+$52k** BUY | vol 225 / OI 73
- **AMD** CALL 475 2026-11-06 (3DTE): 16 @ 31.50 = **+$50k** SELL | vol 275 / OI 115
- **TSLA** CALL 402.5 2026-11-04 (1DTE): 118 @ 4.18 = **+$49k** SELL | vol 19,118 / OI 1,041

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 685 2026-11-04 (1DTE): 503 traded vs OI 84
- **SPY** PUT 733 2026-11-03 (0DTE): 1,502 traded vs OI 959
- **SPY** CALL 785 2026-11-06 (3DTE): 4,794 traded vs OI 4,113
- **SPY** CALL 756 2026-11-10 (7DTE): 505 traded vs OI 0
- **QQQ** PUT 668 2026-11-04 (1DTE): 1,029 traded vs OI 884
- **QQQ** CALL 705 2026-11-30 (27DTE): 4,055 traded vs OI 756
- **QQQ** CALL 695 2026-11-20 (17DTE): 3,342 traded vs OI 3,341
- **AMZN** CALL 275 2026-11-13 (10DTE): 790 traded vs OI 0
- **AMZN** CALL 275 2026-11-20 (17DTE): 1,159 traded vs OI 0
- **AMZN** CALL 275 2026-11-06 (3DTE): 813 traded vs OI 0
- **MSFT** PUT 482.5 2026-11-04 (1DTE): 500 traded vs OI 15
- **MSFT** CALL 540 2026-11-04 (1DTE): 1,679 traded vs OI 1,616
- **MSFT** CALL 520 2026-11-06 (3DTE): 1,365 traded vs OI 1,299
- **PLTR** PUT 162.5 2026-11-13 (10DTE): 503 traded vs OI 178
- **ORCL** PUT 117 2026-11-06 (3DTE): 1,294 traded vs OI 388

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
