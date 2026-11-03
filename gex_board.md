# GEX + FLOW SCAN - Tue Nov 03, 12:20 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 12:20:08 ET, last candle SPY 12:19, QQQ 12:19 | no errors

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **BABA** | 100.08 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 34 | none: 20 calls 0-7DTE > 2 priced 0.40-0.80 > 2 delta 0.2+ > 2 spread ok > 2 liquid > best one only +5% at the target (needs +20%) | POS +$521k | 99.94 | 102 | 100 | +$241k | - | out (clean 36, ADX 57, RVol 0.3) |
| 2 | **META** | 623.42 | - | **-** | 29 | - | NEG -$12.7M | 625.58 | 650 | 610 | -$19.4M | +$0 bull / -$367k bear | out (clean 28, ADX 46, RVol 0.6) |
| 3 | **ORCL** | 126.53 | - | **-** | 27 | - | NEG -$38.7M | - | 135 | 125 | -$7.2M | +$0 bull / -$32k bear | out (clean 33, ADX 34, RVol 0.4) |
| 4 | **MSFT** | 516.56 | - | **-** | 26 | - | POS +$182.6M | 502 | 540 | 500 | -$7.9M | +$0 bull / -$41k bear | out (clean 28, ADX 30, RVol 0.4) |
| 5 | **MSTR** | 136.19 | - | **-** | 24 | - | POS +$82.6M | - | 135 | 125 | -$5.0M | +$32k bull / +$0 bear | out (clean 29, ADX 32, RVol 0.2) |
| 6 | **SHOP** | 147.41 | - | **-** | 22 | - | NEG -$3.7M | - | 145 | 150 | -$4.3M | - | out (clean 32, ADX 23, RVol 1.2) |
| 7 | **COIN** | 148.77 | - | **-** | 21 | - | POS +$20.5M | - | 148 | 150 | -$4.0M | - | out (clean 29, ADX 51, RVol 0.3) |
| 8 | **TSLA** | 397.55 | - | **-** | 20 | - | POS +$189.3M | - | 400 | 380 | +$17.0M | +$890k bull / +$0 bear | out (clean 30, ADX 35, RVol 0.3) |
| 9 | **AVGO** | 332.50 | - | **-** | 19 | - | NEG -$64.5M | - | 340 | 340 | +$2.4M | +$0 bull / -$29k bear | out (clean 31, ADX 19, RVol 0.5) |
| 10 | **SPY** | 755.15 | - | **-** | 17 | - | NEG -$8.8B | 770.61 | 770 | 750 | -$75.4M | +$0 bull / -$1.2M bear | out (clean 30, ADX 15, RVol 0.5) |
| 11 | **NVDA** | 208.63 | - | **-** | 17 | - | POS +$128.1M | 203.63 | 210 | 200 | +$4.3M | +$0 bull / -$632k bear | out (clean 29, ADX 23, RVol 1.1) |
| 12 | **AMD** | 492.74 | - | **-** | 16 | - | NEG -$65.8M | - | 520 | 500 | -$16k | +$0 bull / -$734k bear | out (clean 31, ADX 27, RVol 0.6) |
| 13 | **QQQ** | 687.17 | - | **-** | 15 | - | NEG -$4.9B | - | 700 | 680 | -$41.9M | +$0 bull / -$633k bear | out (clean 30, ADX 17, RVol 0.4) |
| 14 | **AAPL** | 331.31 | - | **-** | 15 | - | NEG -$390.3M | 343.07 | 350 | 330 | -$8.7M | +$0 bull / -$130k bear | out (clean 31, ADX 17, RVol 0.4) |
| 15 | **AMZN** | 248.68 | - | **-** | 15 | - | POS +$149.9M | 236.19 | 250 | 250 | -$735k | +$0 bull / -$101k bear | out (clean 33, ADX 18, RVol 0.5) |
| 16 | **PLTR** | 174.84 | - | **-** | 15 | - | NEG -$25.3M | - | 165 | 180 | -$354k | +$0 bull / -$57k bear | out (clean 27, ADX 21, RVol 0.6) |
| 17 | **MU** | 855.70 | - | **-** | 15 | - | NEG -$194.4M | - | 900 | 850 | -$20.2M | +$209k bull / -$2.9M bear | out (clean 31, ADX 16, RVol 0.3) |
| 18 | **HOOD** | 85.16 | - | **-** | 15 | - | NEG -$2.8M | - | 90 | 85 | -$267k | +$0 bull / -$59k bear | out (clean 31, ADX 17, RVol 0.4) |
| 19 | **CRM** | 223.00 | - | **-** | 12 | - | NEG -$13.7M | - | 240 | 220 | -$385k | - | out (clean 30, ADX 17, RVol 0.6) |
| 20 | **SMCI** | 31.68 | - | **-** | 10 | - | POS +$2.0M | - | 34.5 | 30 | -$933k | - | out (clean 33, ADX 18, RVol 0.9) |
| 21 | **ARM** | 203.34 | - | **-** | 9 | - | NEG -$6.6M | - | 220 | 200 | -$289k | - | out (clean 25, ADX 17, RVol 0.4) |
| 22 | **NFLX** | 62.54 | - | **-** | 8 | - | NEG -$11.9M | 64.46 | 63 | 60 | -$342k | - | out (clean 27, ADX 18, RVol 0.5) |
| 23 | **UBER** | 66.72 | - | **-** | 8 | - | NEG -$8.8M | - | 70 | 65 | -$101k | - | out (clean 29, ADX 11, RVol 0.9) |
| 24 | **GOOGL** | 279.84 | - | **-** | 7 | - | NEG -$33.1M | 284.79 | 285 | 290 | +$2.3M | - | out (clean 32, ADX 16, RVol 0.2) |
| 25 | **IWM** | 280.82 | - | **-** | 6 | - | NEG -$1.1B | 287.03 | 285 | 270 | -$2.9M | - | out (clean 32, ADX 19, RVol 0.4) |
| 26 | **SMH** | 521.46 | - | **-** | 6 | - | NEG -$273.0M | - | 532.5 | 500 | +$644k | - | out (clean 31, ADX 20, RVol 0.3) |
| 27 | **DELL** | 408.10 | - | **-** | 6 | - | NEG -$25.9M | - | 440 | 400 | +$848k | - | out (clean 32, ADX 15, RVol 0.3) |

## Big prints this scan (50)
- **NVDA** PUT 207.5 2026-11-09 (6DTE): 426 @ 4.35 = **+$185k** BUY | vol 3,475 / OI 81
- **NVDA** PUT 210 2026-11-04 (1DTE): 450 @ 3.60 = **+$162k** BUY | vol 8,819 / OI 2,044
- **TSLA** CALL 402.5 2026-11-06 (3DTE): 174 @ 7.53 = **+$131k** BUY | vol 5,187 / OI 5,017
- **QQQ** PUT 688 2026-11-03 (0DTE): 389 @ 2.90 = **+$113k** BUY | vol 30,504 / OI 553
- **MU** CALL 860 2026-11-06 (3DTE): 32 @ 24.05 = **+$77k** SELL | vol 2,759 / OI 194
- **AAPL** PUT 340 2026-11-04 (1DTE): 82 @ 9.18 = **+$75k** BUY | vol 4,182 / OI 7,977
- **META** PUT 610 2026-11-06 (3DTE): 100 @ 7.30 = **+$73k** BUY | vol 458 / OI 3,277
- **TSLA** CALL 402.5 2026-11-06 (3DTE): 89 @ 7.55 = **+$67k** BUY | vol 5,187 / OI 5,017
- **MU** CALL 870 2026-11-06 (3DTE): 33 @ 19.48 = **+$64k** SELL | vol 1,967 / OI 296
- **META** CALL 615 2026-11-06 (3DTE): 40 @ 15.75 = **+$63k** SELL | vol 1,175 / OI 1,264
- **TSLA** CALL 400 2026-11-04 (1DTE): 100 @ 5.80 = **+$58k** BUY | vol 11,485 / OI 1,213
- **META** CALL 627.5 2026-11-09 (6DTE): 50 @ 11.10 = **+$56k** SELL | vol 557 / OI 11
- **TSLA** PUT 400 2026-11-06 (3DTE): 58 @ 9.50 = **+$55k** SELL | vol 5,178 / OI 4,592
- **AMD** PUT 470 2026-11-06 (3DTE): 40 @ 13.52 = **+$54k** BUY | vol 667 / OI 1,996
- **MU** PUT 855 2026-11-06 (3DTE): 21 @ 25.50 = **+$54k** MID | vol 1,201 / OI 740

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 752 2026-11-06 (3DTE): 656 traded vs OI 645
- **SPY** PUT 755 2026-11-05 (2DTE): 1,363 traded vs OI 1,314
- **SPY** PUT 711 2026-11-04 (1DTE): 515 traded vs OI 0
- **SPY** CALL 754 2026-11-11 (8DTE): 502 traded vs OI 0
- **QQQ** CALL 695 2026-11-09 (6DTE): 501 traded vs OI 320
- **QQQ** PUT 680 2026-11-04 (1DTE): 6,657 traded vs OI 6,321
- **AMD** PUT 475 2026-11-04 (1DTE): 506 traded vs OI 204
- **PLTR** CALL 182.5 2026-11-13 (10DTE): 502 traded vs OI 186
- **BABA** PUT 95 2026-11-13 (10DTE): 646 traded vs OI 634

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
