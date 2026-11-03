# GEX + FLOW SCAN - Tue Nov 03, 12:10 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 12:10:08 ET, last candle SPY 12:09, QQQ 12:08 | no errors

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **SHOP** | 146.97 | FLOW SURGE | **PUTS** | 50 | none: 22 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (1 contracts' greeks worked out here) | NEG -$3.6M | - | 145 | 150 | -$4.2M | +$0 bull / -$44k bear | out (clean 31, ADX 25, RVol 1.7) |
| 2 | **COIN** | 149.70 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 39 | none: 21 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$20.3M | - | 148 | 150 | -$4.1M | - | out (clean 29, ADX 55, RVol 0.4) |
| 3 | **BABA** | 100.24 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 34 | none: 20 calls 0-7DTE > 3 priced 0.40-0.80 > 2 delta 0.2+ > 2 spread ok > 2 liquid > best one only +9% at the target (needs +20%) | POS +$1.1M | 99.89 | 102 | 100 | +$243k | - | out (clean 36, ADX 59, RVol 0.2) |
| 4 | **META** | 622.83 | - | **-** | 29 | - | NEG -$16.5M | 625.6 | 650 | 610 | -$18.4M | +$344k bull / -$1.7M bear | out (clean 28, ADX 44, RVol 0.6) |
| 5 | **ORCL** | 126.16 | - | **-** | 26 | - | NEG -$39.9M | - | 135 | 125 | -$7.0M | +$0 bull / -$82k bear | out (clean 33, ADX 33, RVol 0.3) |
| 6 | **MSFT** | 516.75 | - | **-** | 25 | - | POS +$191.3M | 501.51 | 540 | 500 | -$7.8M | +$75k bull / -$127k bear | out (clean 28, ADX 29, RVol 0.5) |
| 7 | **MSTR** | 136.95 | - | **-** | 25 | - | POS +$84.8M | - | 135 | 125 | -$5.1M | +$32k bull / -$66k bear | out (clean 29, ADX 36, RVol 0.5) |
| 8 | **SMCI** | 31.66 | - | **-** | 21 | - | POS +$2.0M | - | 34.5 | 30 | -$896k | +$191k bull / -$370k bear | out (clean 33, ADX 18, RVol 1.3) |
| 9 | **TSLA** | 398.00 | - | **-** | 19 | - | POS +$195.1M | - | 400 | 380 | +$16.3M | +$378k bull / -$1.9M bear | out (clean 30, ADX 33, RVol 0.3) |
| 10 | **ARM** | 203.53 | - | **-** | 19 | - | NEG -$6.6M | - | 220 | 200 | -$274k | +$0 bull / -$45k bear | out (clean 25, ADX 18, RVol 0.5) |
| 11 | **NVDA** | 208.75 | - | **-** | 18 | - | POS +$136.7M | 203.68 | 210 | 200 | +$5.2M | +$0 bull / -$584k bear | out (clean 30, ADX 24, RVol 1.1) |
| 12 | **SPY** | 755.37 | - | **-** | 17 | - | NEG -$8.6B | 770.3 | 770 | 750 | -$66.2M | +$0 bull / -$3.2M bear | out (clean 30, ADX 16, RVol 0.5) |
| 13 | **IWM** | 281.03 | - | **-** | 16 | - | NEG -$1.0B | 287.01 | 285 | 270 | -$2.9M | +$0 bull / -$139k bear | out (clean 32, ADX 20, RVol 0.2) |
| 14 | **AAPL** | 331.35 | - | **-** | 16 | - | NEG -$395.1M | 343.02 | 350 | 330 | -$8.2M | +$32k bull / -$154k bear | out (clean 31, ADX 19, RVol 0.5) |
| 15 | **AMD** | 493.04 | - | **-** | 16 | - | NEG -$66.7M | - | 520 | 500 | +$1.3M | +$0 bull / -$1.6M bear | out (clean 31, ADX 27, RVol 0.6) |
| 16 | **DELL** | 408.12 | - | **-** | 16 | - | NEG -$26.0M | - | 440 | 400 | +$895k | +$0 bull / -$1.2M bear | out (clean 33, ADX 17, RVol 0.1) |
| 17 | **MU** | 857.75 | - | **-** | 16 | - | NEG -$192.9M | - | 900 | 850 | -$17.1M | +$0 bull / -$5.0M bear | out (clean 31, ADX 18, RVol 0.4) |
| 18 | **QQQ** | 687.25 | - | **-** | 15 | - | NEG -$4.9B | - | 700 | 680 | -$33.4M | +$0 bull / -$20.8M bear | out (clean 30, ADX 17, RVol 0.5) |
| 19 | **AMZN** | 248.18 | - | **-** | 15 | - | POS +$144.1M | 236.22 | 250 | 250 | -$445k | +$108k bull / +$0 bear | out (clean 33, ADX 18, RVol 0.5) |
| 20 | **PLTR** | 174.87 | - | **-** | 15 | - | NEG -$24.7M | - | 165 | 180 | -$97k | +$99k bull / -$117k bear | out (clean 27, ADX 21, RVol 0.7) |
| 21 | **HOOD** | 85.36 | - | **-** | 14 | - | NEG -$2.6M | - | 90 | 90 | -$141k | +$0 bull / -$27k bear | out (clean 31, ADX 17, RVol 0.3) |
| 22 | **CRM** | 223.24 | - | **-** | 12 | - | NEG -$13.6M | - | 240 | 220 | -$384k | - | out (clean 30, ADX 17, RVol 0.6) |
| 23 | **AVGO** | 332.81 | - | **-** | 10 | - | NEG -$65.0M | - | 340 | 340 | +$2.5M | - | out (clean 31, ADX 21, RVol 0.6) |
| 24 | **GOOGL** | 279.21 | - | **-** | 8 | - | NEG -$37.2M | 284.55 | 285 | 290 | +$2.5M | - | out (clean 33, ADX 17, RVol 0.5) |
| 25 | **NFLX** | 62.45 | - | **-** | 8 | - | NEG -$12.0M | 64.24 | 63 | 60 | -$289k | - | out (clean 27, ADX 18, RVol 0.6) |
| 26 | **UBER** | 66.75 | - | **-** | 7 | - | NEG -$8.7M | - | 70 | 65 | -$88k | - | out (clean 29, ADX 12, RVol 0.6) |
| 27 | **SMH** | 522.40 | - | **-** | 6 | - | NEG -$259.0M | - | 532.5 | 500 | +$702k | - | out (clean 31, ADX 21, RVol 0.3) |

## Big prints this scan (43)
- **QQQ** PUT 680 2026-11-05 (2DTE): 550 @ 6.41 = **+$353k** BUY | vol 2,889 / OI 1,258
- **QQQ** PUT 686 2026-11-04 (1DTE): 252 @ 6.64 = **+$167k** BUY | vol 7,733 / OI 334
- **SPY** PUT 756 2026-11-04 (1DTE): 250 @ 4.94 = **+$124k** BUY | vol 15,847 / OI 448
- **SPY** PUT 756 2026-11-04 (1DTE): 250 @ 4.89 = **+$122k** BUY | vol 15,847 / OI 448
- **SPY** CALL 756 2026-11-06 (3DTE): 200 @ 5.93 = **+$119k** SELL | vol 3,713 / OI 875
- **SPY** PUT 755 2026-11-04 (1DTE): 231 @ 4.45 = **+$103k** BUY | vol 17,336 / OI 5,209
- **TSLA** CALL 395 2026-11-06 (3DTE): 84 @ 11.35 = **+$95k** BUY | vol 523 / OI 1,893
- **MU** CALL 850 2026-11-06 (3DTE): 30 @ 27.90 = **+$84k** SELL | vol 1,406 / OI 341
- **META** PUT 620 2026-11-04 (1DTE): 100 @ 8.05 = **+$80k** BUY | vol 1,963 / OI 250
- **AMD** PUT 487.5 2026-11-06 (3DTE): 38 @ 21.10 = **+$80k** BUY | vol 387 / OI 265
- **AMD** PUT 485 2026-11-04 (1DTE): 40 @ 17.20 = **+$69k** BUY | vol 1,321 / OI 166
- **MU** CALL 850 2026-11-06 (3DTE): 23 @ 26.65 = **+$61k** SELL | vol 1,406 / OI 341
- **TSLA** CALL 400 2026-11-04 (1DTE): 97 @ 5.55 = **+$54k** BUY | vol 10,690 / OI 1,213
- **TSLA** PUT 405 2026-11-04 (1DTE): 55 @ 9.47 = **+$52k** SELL | vol 9,113 / OI 419
- **MU** PUT 845 2026-11-04 (1DTE): 34 @ 13.93 = **+$47k** BUY | vol 3,742 / OI 274

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 768 2026-11-03 (0DTE): 2,816 traded vs OI 2,765
- **SPY** PUT 757 2026-11-04 (1DTE): 1,537 traded vs OI 1,530
- **SPY** PUT 753 2026-11-06 (3DTE): 2,114 traded vs OI 1,999
- **SPY** PUT 742 2026-11-10 (7DTE): 615 traded vs OI 0
- **IWM** CALL 283 2026-11-13 (10DTE): 2,288 traded vs OI 2,286
- **SMH** PUT 487.5 2026-11-04 (1DTE): 549 traded vs OI 40
- **TSLA** PUT 400 2026-11-09 (6DTE): 508 traded vs OI 483
- **TSLA** PUT 402.5 2026-11-06 (3DTE): 1,483 traded vs OI 1,482
- **AAPL** PUT 330 2026-11-13 (10DTE): 1,436 traded vs OI 1,433
- **AAPL** CALL 337.5 2026-11-20 (17DTE): 530 traded vs OI 384
- **AMD** CALL 540 2026-11-06 (3DTE): 621 traded vs OI 0
- **AMD** CALL 485 2026-11-16 (13DTE): 555 traded vs OI 0
- **AMZN** PUT 250 2026-11-04 (1DTE): 826 traded vs OI 186
- **GOOGL** CALL 290 2026-11-11 (8DTE): 704 traded vs OI 651
- **SMCI** CALL 32.5 2026-11-20 (17DTE): 914 traded vs OI 582

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
