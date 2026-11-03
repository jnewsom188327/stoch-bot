# GEX + FLOW SCAN - Tue Nov 03, 03:15 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 15:15:08 ET, last candle SPY 15:14, QQQ 15:14 | no errors

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **SHOP** | 144.16 | RUN: clean trend + negative gamma + flow agrees | **PUTS** | 70 | none: 24 puts 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$4.3M | - | 145 | 148 | -$3.8M | +$0 bull / -$45k bear | SHORT (clean 34, ADX 35, RVol 1.4) |
| 2 | **MSTR** | 134.78 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 33 | none: 27 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$88.1M | - | 135 | 125 | -$3.2M | +$72k bull / -$802k bear | out (clean 29, ADX 17, RVol 0.2) |
| 3 | **MSFT** | 522.52 | - | **-** | 29 | - | POS +$343.2M | 499.46 | 540 | 500 | -$13.3M | +$0 bull / -$115k bear | out (clean 29, ADX 44, RVol 1.2) |
| 4 | **ORCL** | 124.99 | - | **-** | 26 | - | NEG -$40.5M | - | 135 | 125 | -$9.1M | +$0 bull / -$786k bear | out (clean 35, ADX 41, RVol 0.8) |
| 5 | **SMH** | 516.95 | - | **-** | 21 | - | NEG -$306.0M | - | 532.5 | 500 | +$2.9M | +$0 bull / -$41k bear | out (clean 32, ADX 23, RVol 0.7) |
| 6 | **META** | 618.65 | - | **-** | 21 | - | NEG -$50.6M | 624.9 | 650 | 610 | -$13.9M | +$125k bull / +$0 bear | out (clean 29, ADX 29, RVol 0.4) |
| 7 | **AMZN** | 251.53 | - | **-** | 20 | - | POS +$208.4M | - | 250 | 250 | -$3.4M | +$182k bull / -$25k bear | out (clean 33, ADX 34, RVol 0.6) |
| 8 | **AVGO** | 331.79 | - | **-** | 20 | - | NEG -$71.8M | - | 340 | 340 | +$4.6M | +$0 bull / -$26k bear | out (clean 31, ADX 15, RVol 0.4) |
| 9 | **COIN** | 145.32 | - | **-** | 20 | - | POS +$20.6M | - | 148 | 140 | -$1.9M | +$42k bull / +$0 bear | out (clean 30, ADX 26, RVol 0.3) |
| 10 | **NVDA** | 206.59 | - | **-** | 19 | - | POS +$65.5M | 204.03 | 210 | 200 | +$15.7M | +$95k bull / -$661k bear | out (clean 30, ADX 26, RVol 0.5) |
| 11 | **GOOGL** | 278.20 | - | **-** | 19 | - | NEG -$45.3M | 284.69 | 285 | 290 | +$3.2M | +$37k bull / +$0 bear | out (clean 34, ADX 29, RVol 0.4) |
| 12 | **AMD** | 486.20 | - | **-** | 18 | - | NEG -$88.6M | - | 520 | 440 | +$10.7M | +$262k bull / -$1.2M bear | out (clean 32, ADX 24, RVol 0.7) |
| 13 | **ARM** | 200.93 | - | **-** | 18 | - | NEG -$6.6M | - | 220 | 200 | -$132k | +$0 bull / -$58k bear | out (clean 26, ADX 33, RVol 0.3) |
| 14 | **QQQ** | 684.53 | - | **-** | 17 | - | NEG -$5.2B | - | 700 | 680 | +$39.6M | +$493k bull / -$985k bear | out (clean 30, ADX 22, RVol 1.2) |
| 15 | **IWM** | 279.95 | - | **-** | 16 | - | NEG -$1.2B | 286.89 | 285 | 270 | +$1.6M | +$0 bull / -$65k bear | out (clean 33, ADX 21, RVol 0.7) |
| 16 | **TSLA** | 397.69 | - | **-** | 16 | - | POS +$184.9M | - | 400 | 400 | +$19.0M | +$368k bull / -$323k bear | out (clean 31, ADX 17, RVol 0.3) |
| 17 | **AAPL** | 330.88 | - | **-** | 16 | - | NEG -$430.8M | 342.69 | 350 | 330 | -$7.0M | +$0 bull / -$110k bear | out (clean 31, ADX 18, RVol 0.9) |
| 18 | **SMCI** | 31.75 | - | **-** | 16 | - | POS +$2.0M | - | 34.5 | 30 | +$202k | +$0 bull / -$104k bear | out (clean 33, ADX 14, RVol 1.5) |
| 19 | **SPY** | 753.92 | - | **-** | 15 | - | NEG -$9.9B | 770.25 | 770 | 750 | -$4.4M | +$1.3M bull / -$1.6M bear | out (clean 30, ADX 22, RVol 0.6) |
| 20 | **DELL** | 407.06 | - | **-** | 15 | - | NEG -$26.3M | - | 440 | 400 | +$601k | +$0 bull / -$49k bear | out (clean 32, ADX 14, RVol 0.2) |
| 21 | **PLTR** | 175.06 | - | **-** | 14 | - | NEG -$17.7M | - | 190 | 180 | +$42k | +$0 bull / -$260k bear | out (clean 27, ADX 15, RVol 0.6) |
| 22 | **MU** | 849.18 | - | **-** | 13 | - | NEG -$225.5M | - | 900 | 850 | -$14.9M | +$272k bull / -$1.7M bear | out (clean 31, ADX 10, RVol 0.2) |
| 23 | **UBER** | 66.77 | - | **-** | 12 | - | NEG -$8.0M | - | 70 | 65 | -$400k | - | out (clean 30, ADX 22, RVol 1.5) |
| 24 | **CRM** | 222.72 | - | **-** | 9 | - | NEG -$14.0M | - | 240 | 220 | -$309k | - | out (clean 29, ADX 11, RVol 0.8) |
| 25 | **NFLX** | 62.84 | - | **-** | 7 | - | NEG -$8.4M | 64.04 | 63 | 60 | -$153k | - | out (clean 28, ADX 27, RVol 0.6) |
| 26 | **BABA** | 100.38 | - | **-** | 6 | - | POS +$1.2M | 99.97 | 102 | 100 | +$83k | - | out (clean 36, ADX 19, RVol 0.2) |
| 27 | **HOOD** | 85.08 | - | **-** | 4 | - | NEG -$422k | 85.59 | 90 | 90 | -$13k | - | out (clean 30, ADX 16, RVol 0.6) |

## Big prints this scan (70)
- **SPY** PUT 755 2026-11-03 (0DTE): 2,858 @ 1.60 = **+$457k** BUY | vol 552,799 / OI 4,672
- **MSTR** CALL 140 2026-11-06 (3DTE): 1,500 @ 2.83 = **+$424k** SELL | vol 12,042 / OI 2,913
- **MSTR** CALL 141 2026-11-06 (3DTE): 1,500 @ 2.52 = **+$378k** SELL | vol 9,912 / OI 19,333
- **SPY** PUT 767 2026-11-04 (1DTE): 256 @ 13.57 = **+$347k** MID | vol 7,944 / OI 18,478
- **SPY** PUT 767 2026-11-04 (1DTE): 200 @ 13.65 = **+$273k** BUY | vol 7,944 / OI 18,478
- **SPY** PUT 767 2026-11-04 (1DTE): 200 @ 13.56 = **+$271k** MID | vol 7,944 / OI 18,478
- **SPY** PUT 767 2026-11-04 (1DTE): 200 @ 13.43 = **+$269k** SELL | vol 7,944 / OI 18,478
- **QQQ** CALL 692 2026-11-06 (3DTE): 360 @ 6.97 = **+$251k** BUY | vol 1,058 / OI 1,115
- **NVDA** PUT 207.5 2026-11-06 (3DTE): 400 @ 4.65 = **+$186k** BUY | vol 13,032 / OI 3,523
- **TSLA** CALL 400 2026-11-04 (1DTE): 309 @ 4.49 = **+$139k** MID | vol 25,484 / OI 1,213
- **QQQ** CALL 702 2026-11-06 (3DTE): 360 @ 3.50 = **+$126k** BUY | vol 2,070 / OI 707
- **QQQ** PUT 686 2026-11-04 (1DTE): 148 @ 8.16 = **+$121k** BUY | vol 15,482 / OI 334
- **QQQ** PUT 686 2026-11-04 (1DTE): 139 @ 7.92 = **+$110k** BUY | vol 15,482 / OI 334
- **QQQ** PUT 685 2026-11-06 (3DTE): 100 @ 10.65 = **+$106k** BUY | vol 5,568 / OI 9,290
- **META** PUT 645 2026-11-06 (3DTE): 30 @ 28.60 = **+$86k** MID | vol 50 / OI 587

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 754 2026-11-06 (3DTE): 5,524 traded vs OI 5,457
- **SPY** CALL 743 2026-11-06 (3DTE): 502 traded vs OI 78
- **SPY** CALL 767 2026-11-13 (10DTE): 733 traded vs OI 700
- **SPY** CALL 775 2026-11-17 (14DTE): 551 traded vs OI 0
- **QQQ** PUT 660 2026-11-05 (2DTE): 1,181 traded vs OI 1,094
- **QQQ** PUT 681 2026-11-05 (2DTE): 523 traded vs OI 0
- **QQQ** CALL 680 2026-11-06 (3DTE): 549 traded vs OI 234
- **IWM** CALL 287 2026-11-09 (6DTE): 502 traded vs OI 0
- **IWM** CALL 288 2026-11-13 (10DTE): 1,108 traded vs OI 1,107
- **IWM** CALL 280 2026-11-13 (10DTE): 1,534 traded vs OI 1,509
- **SMH** PUT 505 2026-11-04 (1DTE): 594 traded vs OI 57
- **NVDA** PUT 192.5 2026-11-04 (1DTE): 3,538 traded vs OI 3,519
- **NVDA** CALL 190 2026-11-06 (3DTE): 985 traded vs OI 927
- **NVDA** PUT 187.5 2026-11-09 (6DTE): 908 traded vs OI 835
- **TSLA** CALL 397.5 2026-11-06 (3DTE): 1,454 traded vs OI 1,447

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
