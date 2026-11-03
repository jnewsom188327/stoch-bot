# GEX + FLOW SCAN - Tue Nov 03, 11:40 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 11:40:08 ET, last candle SPY 11:39, QQQ 11:39 | no errors

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **BABA** | 100.08 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 48 | none: 20 calls 0-7DTE > 2 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only -10% at the target (needs +20%) | POS +$614k | 99.9 | 102 | 100 | +$247k | +$28k bull / +$0 bear | out (clean 36, ADX 60, RVol 0.7) |
| 2 | **DELL** | 405.78 | FLOW SURGE | **CALLS** | 36 | none: 32 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$26.1M | - | 440 | 400 | +$2.4M | +$105k bull / +$0 bear | out (clean 33, ADX 22, RVol 0.4) |
| 3 | **COIN** | 148.94 | - | **-** | 33 | - | POS +$20.5M | - | 148 | 150 | -$4.0M | +$219k bull / +$0 bear | out (clean 29, ADX 61, RVol 0.8) |
| 4 | **META** | 620.71 | - | **-** | 28 | - | NEG -$33.3M | 626.32 | 650 | 610 | -$16.3M | +$391k bull / -$446k bear | out (clean 28, ADX 45, RVol 0.4) |
| 5 | **ORCL** | 125.37 | - | **-** | 28 | - | NEG -$41.2M | - | 135 | 125 | -$5.9M | +$216k bull / +$0 bear | out (clean 33, ADX 42, RVol 0.8) |
| 6 | **MSTR** | 136.79 | - | **-** | 27 | - | POS +$83.3M | - | 135 | 125 | -$4.9M | +$423k bull / -$1.0M bear | out (clean 29, ADX 42, RVol 0.6) |
| 7 | **MSFT** | 515.92 | - | **-** | 25 | - | POS +$181.0M | 501.47 | 540 | 500 | -$7.1M | +$44k bull / -$883k bear | out (clean 29, ADX 29, RVol 0.5) |
| 8 | **SHOP** | 145.81 | - | **-** | 25 | - | NEG -$3.5M | - | 145 | 148 | -$4.0M | - | out (clean 32, ADX 36, RVol 1.4) |
| 9 | **AVGO** | 332.00 | - | **-** | 23 | - | NEG -$66.9M | - | 340 | 340 | +$3.1M | +$163k bull / +$0 bear | out (clean 31, ADX 31, RVol 0.6) |
| 10 | **SMH** | 519.89 | - | **-** | 21 | - | NEG -$284.8M | - | 532.5 | 500 | +$1.5M | +$88k bull / +$0 bear | out (clean 32, ADX 27, RVol 0.9) |
| 11 | **TSLA** | 398.00 | - | **-** | 21 | - | POS +$196.4M | - | 400 | 400 | +$22.3M | +$4.7M bull / +$0 bear | out (clean 30, ADX 28, RVol 0.6) |
| 12 | **NVDA** | 207.68 | - | **-** | 20 | - | POS +$102.1M | 203.61 | 210 | 200 | +$7.7M | +$495k bull / +$0 bear | out (clean 30, ADX 30, RVol 1.1) |
| 13 | **AMD** | 488.83 | - | **-** | 19 | - | NEG -$86.6M | - | 520 | 440 | +$6.2M | +$1.7M bull / +$0 bear | out (clean 32, ADX 32, RVol 0.6) |
| 14 | **GOOGL** | 279.04 | - | **-** | 19 | - | NEG -$37.2M | 284.49 | 285 | 290 | +$3.0M | +$184k bull / +$0 bear | out (clean 33, ADX 22, RVol 0.3) |
| 15 | **PLTR** | 172.50 | - | **-** | 19 | - | NEG -$24.9M | - | 165 | 180 | +$1.4M | +$926k bull / -$95k bear | out (clean 28, ADX 30, RVol 1.2) |
| 16 | **SMCI** | 31.38 | - | **-** | 19 | - | POS +$1.9M | - | 34.5 | 30 | +$211k | +$40k bull / +$0 bear | out (clean 34, ADX 23, RVol 1.4) |
| 17 | **IWM** | 281.02 | - | **-** | 18 | - | NEG -$1.1B | 287.22 | 285 | 270 | -$2.5M | +$324k bull / +$0 bear | out (clean 32, ADX 24, RVol 0.9) |
| 18 | **AAPL** | 331.58 | - | **-** | 18 | - | NEG -$381.5M | 342.65 | 350 | 330 | -$8.8M | +$0 bull / -$699k bear | out (clean 31, ADX 27, RVol 0.8) |
| 19 | **SPY** | 754.97 | - | **-** | 17 | - | NEG -$9.0B | 770.85 | 770 | 750 | -$46.5M | +$7.6M bull / +$0 bear | out (clean 31, ADX 20, RVol 0.6) |
| 20 | **QQQ** | 685.80 | - | **-** | 16 | - | NEG -$5.0B | - | 700 | 680 | +$19.7M | +$1.1M bull / +$0 bear | out (clean 31, ADX 22, RVol 0.7) |
| 21 | **MU** | 850.01 | - | **-** | 16 | - | NEG -$202.1M | - | 900 | 850 | +$4.7M | +$5.5M bull / +$0 bear | out (clean 32, ADX 22, RVol 0.7) |
| 22 | **AMZN** | 248.32 | - | **-** | 14 | - | POS +$148.4M | 236.03 | 250 | 250 | -$221k | +$39k bull / -$65k bear | out (clean 33, ADX 18, RVol 0.4) |
| 23 | **HOOD** | 84.81 | - | **-** | 14 | - | NEG -$2.8M | - | 90 | 90 | +$12k | +$88k bull / +$0 bear | out (clean 31, ADX 22, RVol 0.2) |
| 24 | **CRM** | 222.52 | - | **-** | 13 | - | NEG -$13.5M | - | 240 | 220 | -$374k | - | out (clean 30, ADX 22, RVol 0.8) |
| 25 | **UBER** | 66.76 | - | **-** | 12 | - | NEG -$8.7M | - | 70 | 65 | -$149k | - | out (clean 30, ADX 14, RVol 0.7) |
| 26 | **NFLX** | 62.47 | - | **-** | 10 | - | NEG -$11.6M | 64.43 | 63 | 60 | -$293k | - | out (clean 28, ADX 26, RVol 0.5) |
| 27 | **ARM** | 202.30 | - | **-** | 8 | - | NEG -$6.7M | - | 220 | 200 | -$128k | - | out (clean 25, ADX 24, RVol 0.4) |

## Big prints this scan (115)
- **MSTR** CALL 140 2026-11-06 (3DTE): 1,500 @ 3.56 = **+$534k** SELL | vol 9,717 / OI 2,913
- **MSTR** CALL 141 2026-11-06 (3DTE): 1,500 @ 3.20 = **+$480k** SELL | vol 6,026 / OI 19,333
- **MSFT** CALL 515 2026-11-06 (3DTE): 500 @ 8.20 = **+$410k** SELL | vol 3,153 / OI 253
- **MSFT** CALL 515 2026-11-06 (3DTE): 500 @ 8.20 = **+$410k** SELL | vol 3,153 / OI 253
- **TSLA** PUT 400 2026-11-04 (1DTE): 584 @ 6.50 = **+$380k** SELL | vol 24,574 / OI 1,549
- **SPY** PUT 760 2026-11-05 (2DTE): 500 @ 7.42 = **+$371k** SELL | vol 2,289 / OI 2,551
- **SPY** PUT 760 2026-11-05 (2DTE): 492 @ 7.42 = **+$365k** SELL | vol 2,289 / OI 2,551
- **QQQ** PUT 688 2026-11-04 (1DTE): 400 @ 8.00 = **+$320k** SELL | vol 2,930 / OI 258
- **AAPL** PUT 335 2026-11-04 (1DTE): 498 @ 5.80 = **+$289k** BUY | vol 8,172 / OI 2,490
- **IWM** CALL 278 2026-11-04 (1DTE): 460 @ 4.38 = **+$201k** BUY | vol 1,169 / OI 236
- **QQQ** PUT 686 2026-11-04 (1DTE): 259 @ 6.78 = **+$176k** SELL | vol 6,063 / OI 334
- **TSLA** CALL 405 2026-11-04 (1DTE): 424 @ 4.00 = **+$170k** BUY | vol 17,968 / OI 1,099
- **MU** PUT 840 2026-11-04 (1DTE): 150 @ 10.90 = **+$164k** SELL | vol 8,265 / OI 244
- **AAPL** PUT 335 2026-11-04 (1DTE): 283 @ 5.75 = **+$163k** BUY | vol 8,172 / OI 2,490
- **TSLA** PUT 402.5 2026-11-04 (1DTE): 199 @ 8.00 = **+$159k** SELL | vol 10,834 / OI 654

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 772 2026-11-05 (2DTE): 557 traded vs OI 0
- **SPY** PUT 763 2026-11-03 (0DTE): 672 traded vs OI 642
- **SPY** CALL 753 2026-11-09 (6DTE): 598 traded vs OI 0
- **SPY** CALL 756 2026-11-13 (10DTE): 545 traded vs OI 273
- **SPY** PUT 754 2026-11-10 (7DTE): 504 traded vs OI 0
- **QQQ** CALL 719 2026-11-03 (0DTE): 913 traded vs OI 685
- **QQQ** PUT 651 2026-11-06 (3DTE): 622 traded vs OI 0
- **IWM** CALL 282.5 2026-11-13 (10DTE): 664 traded vs OI 661
- **SMH** PUT 490 2026-11-04 (1DTE): 542 traded vs OI 286
- **NVDA** CALL 195 2026-11-04 (1DTE): 611 traded vs OI 89
- **TSLA** PUT 370 2026-11-04 (1DTE): 2,880 traded vs OI 2,604
- **TSLA** CALL 390 2026-11-04 (1DTE): 529 traded vs OI 417
- **AMD** PUT 495 2026-11-04 (1DTE): 587 traded vs OI 167
- **AMD** PUT 482.5 2026-11-06 (3DTE): 731 traded vs OI 229
- **META** PUT 602.5 2026-11-04 (1DTE): 513 traded vs OI 107

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
