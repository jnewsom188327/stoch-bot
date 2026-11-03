# GEX + FLOW SCAN - Tue Nov 03, 11:30 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 11:30:08 ET, last candle SPY 11:29, QQQ 11:29 | no errors

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **BABA** | 100.05 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 40 | none: 20 calls 0-7DTE > 2 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only -6% at the target (needs +20%) | POS +$325k | 99.99 | 102 | 100 | +$221k | - | out (clean 36, ADX 58, RVol 0.8) |
| 2 | **COIN** | 149.48 | - | **-** | 36 | - | POS +$20.1M | - | 148 | 150 | -$4.4M | +$60k bull / +$0 bear | out (clean 29, ADX 65, RVol 0.9) |
| 3 | **SHOP** | 144.72 | - | **-** | 36 | - | NEG -$3.7M | - | 145 | 148 | -$4.0M | +$54k bull / +$0 bear | out (clean 32, ADX 39, RVol 1.6) |
| 4 | **TSLA** | 399.63 | PINNED between the walls (positive gamma) - chop | **-** | 31 | - | POS +$207.8M | - | 400 | 400 | +$15.8M | +$1.9M bull / +$0 bear | out (clean 30, ADX 24, RVol 0.5) |
| 5 | **ORCL** | 125.41 | - | **-** | 30 | - | NEG -$41.4M | - | 135 | 125 | -$6.1M | +$410k bull / +$0 bear | out (clean 33, ADX 47, RVol 0.9) |
| 6 | **META** | 620.40 | - | **-** | 28 | - | NEG -$39.5M | 626.6 | 650 | 610 | -$14.4M | +$561k bull / +$0 bear | out (clean 28, ADX 44, RVol 0.6) |
| 7 | **MSTR** | 136.80 | - | **-** | 27 | - | POS +$85.3M | - | 135 | 125 | -$4.4M | +$454k bull / +$0 bear | out (clean 29, ADX 44, RVol 0.8) |
| 8 | **MSFT** | 516.64 | - | **-** | 26 | - | POS +$178.3M | 501.71 | 540 | 500 | -$7.3M | +$480k bull / +$0 bear | out (clean 29, ADX 30, RVol 0.6) |
| 9 | **SMH** | 520.98 | - | **-** | 22 | - | NEG -$278.2M | - | 532.5 | 500 | +$1.1M | +$179k bull / +$0 bear | out (clean 32, ADX 30, RVol 1.6) |
| 10 | **NVDA** | 208.62 | - | **-** | 21 | - | POS +$124.4M | 203.65 | 210 | 200 | +$5.5M | +$351k bull / +$0 bear | out (clean 30, ADX 33, RVol 1.9) |
| 11 | **GOOGL** | 278.75 | - | **-** | 20 | - | NEG -$41.2M | 284.83 | 285 | 290 | +$3.3M | +$155k bull / +$0 bear | out (clean 33, ADX 24, RVol 0.3) |
| 12 | **AMD** | 489.67 | - | **-** | 19 | - | NEG -$69.4M | - | 520 | 500 | +$3.7M | +$1.1M bull / +$0 bear | out (clean 32, ADX 37, RVol 0.6) |
| 13 | **PLTR** | 171.96 | - | **-** | 19 | - | NEG -$29.0M | - | 165 | 180 | +$203k | +$695k bull / +$0 bear | out (clean 28, ADX 33, RVol 1.3) |
| 14 | **SPY** | 755.77 | - | **-** | 18 | - | NEG -$8.8B | 770.85 | 770 | 750 | -$75.6M | +$6.6M bull / +$0 bear | out (clean 31, ADX 20, RVol 0.5) |
| 15 | **AAPL** | 330.89 | - | **-** | 18 | - | NEG -$398.2M | 343.68 | 350 | 330 | -$6.2M | +$0 bull / -$133k bear | out (clean 31, ADX 31, RVol 0.8) |
| 16 | **SMCI** | 31.48 | - | **-** | 18 | - | POS +$1.9M | - | 34.5 | 30 | +$162k | +$40k bull / +$0 bear | out (clean 34, ADX 25, RVol 1.3) |
| 17 | **QQQ** | 686.39 | - | **-** | 16 | - | NEG -$5.0B | - | 700 | 680 | -$3.8M | +$617k bull / +$0 bear | out (clean 31, ADX 23, RVol 0.6) |
| 18 | **HOOD** | 85.10 | - | **-** | 16 | - | NEG -$2.9M | - | 90 | 90 | -$158k | +$88k bull / +$0 bear | out (clean 31, ADX 25, RVol 0.2) |
| 19 | **AMZN** | 248.06 | - | **-** | 15 | - | POS +$142.8M | 236.05 | 250 | 250 | +$164k | +$39k bull / -$64k bear | out (clean 33, ADX 19, RVol 0.5) |
| 20 | **DELL** | 405.87 | - | **-** | 15 | - | NEG -$26.1M | - | 440 | 400 | +$2.0M | - | out (clean 34, ADX 24, RVol 0.5) |
| 21 | **MU** | 850.75 | - | **-** | 15 | - | NEG -$205.9M | - | 900 | 850 | -$2.6M | +$3.7M bull / +$0 bear | out (clean 31, ADX 21, RVol 0.6) |
| 22 | **AVGO** | 333.19 | - | **-** | 14 | - | NEG -$65.7M | - | 340 | 340 | +$2.7M | - | out (clean 31, ADX 36, RVol 0.6) |
| 23 | **NFLX** | 62.52 | - | **-** | 13 | - | NEG -$12.1M | 64.74 | 63 | 60 | -$427k | - | out (clean 28, ADX 27, RVol 0.6) |
| 24 | **UBER** | 66.84 | - | **-** | 13 | - | NEG -$8.6M | - | 70 | 65 | -$105k | - | out (clean 30, ADX 16, RVol 0.9) |
| 25 | **CRM** | 222.12 | - | **-** | 13 | - | NEG -$14.7M | - | 240 | 220 | -$310k | - | out (clean 30, ADX 25, RVol 0.8) |
| 26 | **ARM** | 202.77 | - | **-** | 11 | - | NEG -$6.7M | - | 220 | 200 | -$201k | - | out (clean 25, ADX 26, RVol 0.4) |
| 27 | **IWM** | 281.35 | - | **-** | 9 | - | NEG -$992.6M | 286.99 | 285 | 270 | -$3.2M | - | out (clean 33, ADX 25, RVol 0.7) |

## Big prints this scan (91)
- **SPY** PUT 760 2026-11-06 (3DTE): 511 @ 7.95 = **+$406k** SELL | vol 3,041 / OI 12,559
- **TSLA** PUT 405 2026-11-04 (1DTE): 442 @ 8.40 = **+$371k** SELL | vol 8,331 / OI 419
- **SPY** CALL 745 2026-11-05 (2DTE): 258 @ 13.25 = **+$342k** BUY | vol 10,256 / OI 186
- **NVDA** CALL 210 2026-11-06 (3DTE): 800 @ 3.45 = **+$276k** MID | vol 13,960 / OI 22,751
- **SPY** CALL 745 2026-11-05 (2DTE): 200 @ 13.25 = **+$265k** BUY | vol 10,256 / OI 186
- **SPY** CALL 745 2026-11-05 (2DTE): 200 @ 13.25 = **+$265k** BUY | vol 10,256 / OI 186
- **SPY** CALL 745 2026-11-05 (2DTE): 200 @ 13.25 = **+$265k** BUY | vol 10,256 / OI 186
- **QQQ** CALL 708 2026-11-06 (3DTE): 948 @ 2.67 = **+$253k** BUY | vol 1,235 / OI 1,628
- **SPY** CALL 745 2026-11-05 (2DTE): 188 @ 13.26 = **+$249k** BUY | vol 10,256 / OI 186
- **SPY** CALL 745 2026-11-05 (2DTE): 170 @ 13.25 = **+$225k** BUY | vol 10,256 / OI 186
- **SPY** CALL 745 2026-11-05 (2DTE): 170 @ 13.25 = **+$225k** BUY | vol 10,256 / OI 186
- **TSLA** PUT 405 2026-11-04 (1DTE): 246 @ 8.40 = **+$207k** SELL | vol 8,331 / OI 419
- **SPY** CALL 745 2026-11-05 (2DTE): 145 @ 13.26 = **+$192k** BUY | vol 10,256 / OI 186
- **SPY** CALL 745 2026-11-05 (2DTE): 128 @ 13.25 = **+$170k** BUY | vol 10,256 / OI 186
- **SPY** PUT 776 2026-11-04 (1DTE): 85 @ 19.82 = **+$168k** SELL | vol 87 / OI 44

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 757 2026-11-06 (3DTE): 1,347 traded vs OI 1,120
- **SPY** PUT 745 2026-11-04 (1DTE): 2,897 traded vs OI 2,820
- **SPY** CALL 759 2026-11-05 (2DTE): 524 traded vs OI 0
- **QQQ** PUT 650 2026-11-04 (1DTE): 2,460 traded vs OI 2,397
- **QQQ** PUT 670 2026-11-04 (1DTE): 4,288 traded vs OI 4,179
- **QQQ** CALL 708 2026-11-20 (17DTE): 1,446 traded vs OI 931
- **NVDA** PUT 192.5 2026-11-11 (8DTE): 929 traded vs OI 8
- **NVDA** PUT 200 2026-11-09 (6DTE): 1,297 traded vs OI 382
- **NVDA** PUT 202.5 2026-11-11 (8DTE): 802 traded vs OI 35
- **NVDA** PUT 222.5 2026-11-04 (1DTE): 528 traded vs OI 133
- **AAPL** PUT 327.5 2026-11-06 (3DTE): 2,574 traded vs OI 2,521
- **AMD** CALL 530 2026-11-06 (3DTE): 503 traded vs OI 444
- **META** PUT 620 2026-11-04 (1DTE): 602 traded vs OI 250
- **META** CALL 627.5 2026-11-09 (6DTE): 500 traded vs OI 11
- **MSFT** PUT 507.5 2026-11-04 (1DTE): 503 traded vs OI 114

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
