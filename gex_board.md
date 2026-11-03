# GEX + FLOW SCAN - Tue Nov 03, 03:25 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 15:25:08 ET, last candle SPY 15:24, QQQ 15:24 | no errors

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **SHOP** | 143.91 | RUN: clean trend + negative gamma + flow agrees | **PUTS** | 71 | none: 24 puts 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$4.3M | - | 145 | 148 | -$3.8M | +$0 bull / -$45k bear | SHORT (clean 35, ADX 37, RVol 1.5) |
| 2 | **MSFT** | 523.07 | - | **-** | 30 | - | POS +$367.9M | 499.09 | 540 | 500 | -$13.6M | +$0 bull / -$317k bear | out (clean 28, ADX 46, RVol 1.3) |
| 3 | **ORCL** | 125.29 | - | **-** | 25 | - | NEG -$40.2M | - | 135 | 125 | -$9.2M | +$0 bull / -$958k bear | out (clean 35, ADX 37, RVol 1.0) |
| 4 | **UBER** | 66.79 | - | **-** | 23 | - | NEG -$8.1M | - | 70 | 65 | -$484k | +$0 bull / -$34k bear | out (clean 30, ADX 20, RVol 1.7) |
| 5 | **META** | 619.58 | - | **-** | 21 | - | NEG -$38.2M | 624.5 | 650 | 610 | -$14.6M | +$335k bull / -$153k bear | out (clean 29, ADX 30, RVol 0.3) |
| 6 | **AMZN** | 252.12 | - | **-** | 20 | - | POS +$217.2M | - | 250 | 250 | -$3.8M | +$42k bull / -$25k bear | out (clean 33, ADX 35, RVol 0.7) |
| 7 | **SMH** | 518.47 | - | **-** | 19 | - | NEG -$294.5M | - | 532.5 | 500 | +$2.6M | +$0 bull / -$207k bear | out (clean 32, ADX 20, RVol 0.7) |
| 8 | **NVDA** | 206.91 | - | **-** | 19 | - | POS +$79.0M | 204.01 | 210 | 200 | +$15.4M | +$0 bull / -$803k bear | out (clean 30, ADX 26, RVol 0.5) |
| 9 | **GOOGL** | 279.00 | - | **-** | 19 | - | NEG -$40.7M | 284.32 | 285 | 290 | +$2.9M | +$37k bull / +$0 bear | out (clean 33, ADX 28, RVol 0.4) |
| 10 | **AVGO** | 332.26 | - | **-** | 19 | - | NEG -$66.7M | - | 340 | 340 | +$4.3M | +$0 bull / -$127k bear | out (clean 30, ADX 14, RVol 0.5) |
| 11 | **AMD** | 486.71 | - | **-** | 18 | - | NEG -$87.5M | - | 520 | 440 | +$9.5M | +$412k bull / -$1.6M bear | out (clean 32, ADX 25, RVol 0.8) |
| 12 | **QQQ** | 685.68 | - | **-** | 17 | - | NEG -$5.1B | - | 700 | 680 | +$31.4M | +$493k bull / -$2.8M bear | out (clean 29, ADX 19, RVol 1.2) |
| 13 | **MSTR** | 135.43 | - | **-** | 17 | - | POS +$89.5M | - | 135 | 125 | -$3.4M | +$72k bull / -$802k bear | out (clean 29, ADX 16, RVol 0.3) |
| 14 | **SPY** | 754.68 | - | **-** | 16 | - | NEG -$9.6B | 770.37 | 770 | 750 | -$12.8M | +$1.0M bull / -$2.1M bear | out (clean 30, ADX 20, RVol 0.8) |
| 15 | **IWM** | 280.16 | - | **-** | 16 | - | NEG -$1.2B | 286.77 | 285 | 270 | +$1.6M | +$0 bull / -$130k bear | out (clean 33, ADX 22, RVol 0.6) |
| 16 | **AAPL** | 331.32 | - | **-** | 16 | - | NEG -$403.2M | 341.75 | 350 | 330 | -$8.8M | +$0 bull / -$250k bear | out (clean 30, ADX 16, RVol 1.0) |
| 17 | **SMCI** | 31.78 | - | **-** | 16 | - | POS +$2.1M | - | 34.5 | 30 | +$311k | +$32k bull / -$104k bear | out (clean 33, ADX 14, RVol 1.5) |
| 18 | **TSLA** | 397.87 | - | **-** | 15 | - | POS +$192.2M | - | 400 | 400 | +$18.5M | +$370k bull / -$376k bear | out (clean 31, ADX 15, RVol 0.3) |
| 19 | **PLTR** | 176.03 | - | **-** | 14 | - | NEG -$16.6M | - | 190 | 180 | +$83k | +$0 bull / -$324k bear | out (clean 27, ADX 15, RVol 0.6) |
| 20 | **ARM** | 202.05 | - | **-** | 14 | - | NEG -$6.5M | - | 220 | 200 | -$865k | - | out (clean 26, ADX 30, RVol 0.3) |
| 21 | **MU** | 851.30 | - | **-** | 13 | - | NEG -$221.3M | - | 900 | 850 | -$16.0M | +$0 bull / -$3.5M bear | out (clean 31, ADX 10, RVol 0.3) |
| 22 | **COIN** | 145.54 | - | **-** | 9 | - | POS +$20.2M | - | 148 | 150 | -$2.0M | - | out (clean 30, ADX 24, RVol 0.4) |
| 23 | **CRM** | 222.63 | - | **-** | 9 | - | NEG -$14.2M | - | 240 | 220 | -$309k | - | out (clean 29, ADX 11, RVol 0.6) |
| 24 | **NFLX** | 62.95 | - | **-** | 7 | - | NEG -$7.2M | 64 | 63 | 60 | -$203k | - | out (clean 28, ADX 24, RVol 0.6) |
| 25 | **BABA** | 100.39 | - | **-** | 6 | - | POS +$1.8M | 99.87 | 102 | 100 | +$82k | - | out (clean 35, ADX 18, RVol 0.4) |
| 26 | **DELL** | 407.50 | - | **-** | 5 | - | NEG -$26.3M | - | 440 | 400 | +$667k | - | out (clean 32, ADX 13, RVol 0.3) |
| 27 | **HOOD** | 85.16 | - | **-** | 4 | - | NEG -$360k | 85.55 | 90 | 90 | -$6k | - | out (clean 30, ADX 14, RVol 0.6) |

## Big prints this scan (41)
- **NVDA** PUT 200 2026-11-04 (1DTE): 1,466 @ 0.67 = **+$98k** BUY | vol 31,687 / OI 7,174
- **MSTR** PUT 135 2026-11-06 (3DTE): 200 @ 4.77 = **+$95k** MID | vol 2,458 / OI 1,986
- **AMD** PUT 495 2026-11-04 (1DTE): 30 @ 22.51 = **+$68k** SELL | vol 769 / OI 167
- **META** PUT 622.5 2026-11-06 (3DTE): 50 @ 13.27 = **+$66k** BUY | vol 359 / OI 196
- **META** PUT 620 2026-11-06 (3DTE): 50 @ 11.97 = **+$60k** BUY | vol 2,223 / OI 1,386
- **MU** CALL 855 2026-11-06 (3DTE): 26 @ 22.12 = **+$58k** SELL | vol 2,762 / OI 99
- **MU** CALL 850 2026-11-04 (1DTE): 36 @ 15.93 = **+$57k** SELL | vol 8,971 / OI 64
- **AMD** CALL 490 2026-11-04 (1DTE): 30 @ 17.02 = **+$51k** SELL | vol 3,761 / OI 55
- **AMD** CALL 490 2026-11-04 (1DTE): 30 @ 17.02 = **+$51k** SELL | vol 3,761 / OI 55
- **MU** PUT 850 2026-11-04 (1DTE): 30 @ 17.00 = **+$51k** BUY | vol 17,771 / OI 414
- **MU** CALL 850 2026-11-04 (1DTE): 30 @ 15.60 = **+$47k** SELL | vol 8,971 / OI 64
- **MU** CALL 830 2026-11-04 (1DTE): 15 @ 28.97 = **+$43k** MID | vol 685 / OI 19
- **MU** PUT 850 2026-11-06 (3DTE): 17 @ 25.30 = **+$43k** BUY | vol 4,259 / OI 1,813
- **TSLA** CALL 397.5 2026-11-04 (1DTE): 70 @ 5.90 = **+$41k** MID | vol 9,791 / OI 1,004
- **AMD** CALL 490 2026-11-06 (3DTE): 19 @ 20.35 = **+$39k** SELL | vol 3,215 / OI 257

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 772 2026-11-09 (6DTE): 504 traded vs OI 0
- **SPY** PUT 726 2026-11-05 (2DTE): 649 traded vs OI 0
- **SPY** PUT 718 2026-11-06 (3DTE): 513 traded vs OI 452
- **SPY** CALL 815 2026-11-12 (9DTE): 601 traded vs OI 5
- **SPY** PUT 715 2026-11-12 (9DTE): 1,055 traded vs OI 480
- **QQQ** CALL 695 2026-11-05 (2DTE): 1,099 traded vs OI 1,056
- **QQQ** CALL 685 2026-11-13 (10DTE): 535 traded vs OI 403
- **QQQ** CALL 705 2026-11-27 (24DTE): 691 traded vs OI 684
- **AMD** PUT 450 2026-11-06 (3DTE): 4,197 traded vs OI 4,194
- **AMZN** CALL 260 2026-11-06 (3DTE): 8,273 traded vs OI 8,243
- **AMZN** CALL 265 2026-11-06 (3DTE): 5,990 traded vs OI 5,657
- **AVGO** PUT 300 2026-11-04 (1DTE): 663 traded vs OI 528
- **SMCI** PUT 29.5 2026-11-06 (3DTE): 574 traded vs OI 278
- **SMCI** CALL 34 2026-11-06 (3DTE): 2,954 traded vs OI 2,877
- **MU** CALL 825 2026-11-16 (13DTE): 507 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
