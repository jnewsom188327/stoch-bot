# GEX + FLOW SCAN - Tue Nov 03, 01:20 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 13:20:08 ET, last candle SPY 13:19, QQQ 13:19 | no errors

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **MSFT** | 520.39 | FLOW SURGE | **PUTS** | 39 | none: 123 puts 0-7DTE > 15 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (11 contracts' greeks worked out here) | POS +$244.7M | 502.12 | 540 | 500 | -$11.9M | +$0 bull / -$169k bear | out (clean 28, ADX 45, RVol 0.8) |
| 2 | **BABA** | 100.15 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 33 | none: 20 calls 0-7DTE > 2 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only -9% at the target (needs +20%) | POS +$513k | 99.99 | 102 | 100 | +$294k | - | out (clean 36, ADX 43, RVol 0.2) |
| 3 | **ORCL** | 127.29 | - | **-** | 28 | - | NEG -$37.5M | - | 135 | 125 | -$9.2M | +$0 bull / -$28k bear | out (clean 34, ADX 41, RVol 0.7) |
| 4 | **META** | 623.97 | - | **-** | 26 | - | NEG -$13.2M | 625.96 | 650 | 610 | -$19.6M | +$0 bull / -$539k bear | out (clean 28, ADX 36, RVol 0.4) |
| 5 | **AMZN** | 250.68 | - | **-** | 20 | - | POS +$179.8M | - | 250 | 250 | -$3.8M | +$0 bull / -$302k bear | out (clean 32, ADX 29, RVol 0.6) |
| 6 | **SHOP** | 148.20 | - | **-** | 19 | - | NEG -$3.8M | - | 150 | 148 | -$4.4M | - | out (clean 33, ADX 17, RVol 0.8) |
| 7 | **TSLA** | 398.37 | - | **-** | 18 | - | POS +$198.4M | - | 400 | 400 | +$13.3M | +$0 bull / -$682k bear | out (clean 31, ADX 30, RVol 0.4) |
| 8 | **AVGO** | 332.18 | - | **-** | 18 | - | NEG -$64.3M | - | 340 | 340 | +$2.9M | +$145k bull / -$27k bear | out (clean 31, ADX 15, RVol 0.5) |
| 9 | **SPY** | 756.24 | - | **-** | 17 | - | NEG -$8.1B | 770.14 | 770 | 750 | -$88.6M | +$0 bull / -$818k bear | out (clean 29, ADX 17, RVol 0.4) |
| 10 | **NVDA** | 207.93 | - | **-** | 16 | - | POS +$113.1M | 203.65 | 210 | 200 | +$8.3M | +$0 bull / -$281k bear | out (clean 29, ADX 15, RVol 0.5) |
| 11 | **GOOGL** | 280.94 | - | **-** | 16 | - | NEG -$27.8M | 285.07 | 285 | 290 | +$1.1M | +$0 bull / -$28k bear | out (clean 33, ADX 20, RVol 0.4) |
| 12 | **QQQ** | 687.07 | - | **-** | 15 | - | NEG -$4.9B | - | 700 | 680 | -$23.6M | +$0 bull / -$754k bear | out (clean 29, ADX 16, RVol 0.6) |
| 13 | **AAPL** | 331.96 | - | **-** | 15 | - | NEG -$381.5M | 343.3 | 350 | 330 | -$8.4M | +$194k bull / -$162k bear | out (clean 30, ADX 13, RVol 0.8) |
| 14 | **AMD** | 491.65 | - | **-** | 14 | - | NEG -$67.0M | - | 520 | 500 | +$2.6M | +$71k bull / -$1.1M bear | out (clean 31, ADX 16, RVol 0.5) |
| 15 | **MU** | 850.43 | - | **-** | 13 | - | NEG -$204.4M | - | 900 | 850 | -$12.9M | +$398k bull / -$1.5M bear | out (clean 31, ADX 10, RVol 0.3) |
| 16 | **HOOD** | 85.05 | - | **-** | 13 | - | NEG -$2.8M | - | 90 | 90 | -$171k | +$0 bull / -$26k bear | out (clean 31, ADX 11, RVol 0.3) |
| 17 | **COIN** | 146.82 | - | **-** | 12 | - | POS +$20.7M | - | 148 | 150 | -$2.4M | - | out (clean 29, ADX 32, RVol 0.3) |
| 18 | **CRM** | 223.12 | - | **-** | 12 | - | NEG -$13.6M | - | 240 | 220 | -$379k | - | out (clean 30, ADX 16, RVol 0.7) |
| 19 | **NFLX** | 62.83 | - | **-** | 11 | - | NEG -$9.2M | 64.27 | 63 | 60 | -$520k | - | out (clean 27, ADX 27, RVol 0.5) |
| 20 | **MSTR** | 136.13 | - | **-** | 11 | - | POS +$81.4M | - | 135 | 125 | -$4.9M | - | out (clean 29, ADX 18, RVol 0.3) |
| 21 | **SMCI** | 31.62 | - | **-** | 7 | - | POS +$2.0M | - | 34.5 | 30 | -$627k | - | out (clean 33, ADX 14, RVol 0.9) |
| 22 | **UBER** | 66.56 | - | **-** | 7 | - | NEG -$13.6M | - | 70 | 65 | -$71k | - | out (clean 29, ADX 16, RVol 0.9) |
| 23 | **DELL** | 408.84 | - | **-** | 6 | - | NEG -$25.9M | - | 440 | 400 | +$997k | - | out (clean 32, ADX 12, RVol 0.3) |
| 24 | **ARM** | 203.06 | - | **-** | 6 | - | NEG -$6.7M | - | 220 | 200 | -$210k | - | out (clean 25, ADX 12, RVol 0.3) |
| 25 | **IWM** | 281.06 | - | **-** | 5 | - | NEG -$1.1B | 286.91 | 285 | 270 | -$2.5M | - | out (clean 32, ADX 17, RVol 0.3) |
| 26 | **SMH** | 520.01 | - | **-** | 5 | - | NEG -$281.6M | - | 532.5 | 500 | +$919k | - | out (clean 31, ADX 14, RVol 0.4) |
| 27 | **PLTR** | 174.37 | - | **-** | 4 | - | NEG -$24.6M | - | 165 | 180 | -$90k | - | out (clean 27, ADX 16, RVol 0.8) |

## Big prints this scan (28)
- **AVGO** CALL 332.5 2026-11-04 (1DTE): 145 @ 5.95 = **+$86k** BUY | vol 800 / OI 155
- **META** CALL 635 2026-11-06 (3DTE): 111 @ 7.05 = **+$78k** SELL | vol 1,291 / OI 1,669
- **MU** CALL 885 2026-11-04 (1DTE): 150 @ 5.10 = **+$76k** BUY | vol 3,115 / OI 147
- **AAPL** PUT 340 2026-11-04 (1DTE): 82 @ 9.15 = **+$75k** BUY | vol 4,514 / OI 7,977
- **AMZN** PUT 247.5 2026-11-04 (1DTE): 325 @ 1.78 = **+$58k** BUY | vol 8,021 / OI 158
- **AMD** CALL 490 2026-11-04 (1DTE): 25 @ 20.50 = **+$51k** MID | vol 3,166 / OI 55
- **AMZN** CALL 250 2026-11-04 (1DTE): 200 @ 2.50 = **+$50k** SELL | vol 25,385 / OI 1,092
- **AAPL** CALL 335 2026-11-04 (1DTE): 310 @ 1.48 = **+$46k** SELL | vol 53,782 / OI 305
- **AMZN** CALL 250 2026-11-04 (1DTE): 172 @ 2.40 = **+$41k** SELL | vol 25,385 / OI 1,092
- **MU** CALL 885 2026-11-04 (1DTE): 75 @ 5.50 = **+$41k** BUY | vol 3,115 / OI 147
- **AMD** CALL 505 2026-11-06 (3DTE): 24 @ 16.80 = **+$40k** BUY | vol 609 / OI 290
- **META** PUT 622.5 2026-11-04 (1DTE): 50 @ 7.60 = **+$38k** BUY | vol 1,188 / OI 91
- **MU** PUT 855 2026-11-04 (1DTE): 20 @ 19.00 = **+$38k** SELL | vol 10,374 / OI 281
- **META** CALL 625 2026-11-04 (1DTE): 50 @ 6.90 = **+$34k** SELL | vol 7,256 / OI 334
- **MU** PUT 845 2026-11-09 (6DTE): 13 @ 26.12 = **+$34k** SELL | vol 124 / OI 50

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 758 2026-11-06 (3DTE): 1,255 traded vs OI 1,248
- **SPY** CALL 765 2026-11-05 (2DTE): 3,481 traded vs OI 3,405
- **SPY** PUT 766 2026-11-03 (0DTE): 1,092 traded vs OI 1,024
- **SPY** PUT 755 2026-11-09 (6DTE): 647 traded vs OI 638
- **QQQ** PUT 655 2026-11-05 (2DTE): 812 traded vs OI 810
- **QQQ** PUT 650 2026-11-06 (3DTE): 6,642 traded vs OI 5,669
- **NVDA** CALL 222.5 2026-11-06 (3DTE): 8,877 traded vs OI 5,875
- **AAPL** CALL 357.5 2026-11-20 (17DTE): 621 traded vs OI 242
- **META** CALL 622.5 2026-11-06 (3DTE): 500 traded vs OI 346
- **META** CALL 680 2026-11-06 (3DTE): 507 traded vs OI 0
- **AMZN** CALL 250 2026-11-13 (10DTE): 1,701 traded vs OI 1,688
- **GOOGL** CALL 285 2026-11-06 (3DTE): 5,886 traded vs OI 5,874
- **SMCI** PUT 28.5 2026-11-06 (3DTE): 617 traded vs OI 277
- **SMCI** CALL 30.5 2026-11-06 (3DTE): 531 traded vs OI 145
- **MU** PUT 820 2026-11-06 (3DTE): 863 traded vs OI 857

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
