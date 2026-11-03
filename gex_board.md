# GEX + FLOW SCAN - Tue Nov 03, 02:20 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 14:20:08 ET, last candle SPY 14:19, QQQ 14:19 | no errors

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **MSFT** | 521.61 | FLOW SURGE | **PUTS** | 36 | none: 126 puts 0-7DTE > 12 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (10 contracts' greeks worked out here) | POS +$262.7M | 502.01 | 540 | 500 | -$13.1M | +$0 bull / -$61k bear | out (clean 29, ADX 43, RVol 0.6) |
| 2 | **TSLA** | 399.65 | PINNED between the walls (positive gamma) - chop | **-** | 27 | - | POS +$214.4M | - | 400 | 400 | +$14.1M | +$267k bull / -$383k bear | out (clean 31, ADX 18, RVol 0.2) |
| 3 | **ORCL** | 125.43 | - | **-** | 24 | - | NEG -$40.5M | - | 135 | 125 | -$9.3M | +$335k bull / +$0 bear | out (clean 34, ADX 28, RVol 0.6) |
| 4 | **NFLX** | 63.12 | - | **-** | 22 | - | NEG -$6.9M | 64.24 | 63 | 65 | -$568k | +$0 bull / -$50k bear | out (clean 28, ADX 39, RVol 0.6) |
| 5 | **META** | 621.56 | - | **-** | 21 | - | NEG -$32.9M | 626.32 | 650 | 610 | -$15.6M | +$148k bull / +$0 bear | out (clean 28, ADX 23, RVol 0.3) |
| 6 | **AMZN** | 251.26 | - | **-** | 21 | - | POS +$183.2M | - | 250 | 250 | -$3.9M | +$137k bull / -$55k bear | out (clean 33, ADX 38, RVol 0.6) |
| 7 | **COIN** | 145.70 | - | **-** | 21 | - | POS +$21.7M | - | 148 | 150 | -$2.1M | +$77k bull / +$0 bear | out (clean 30, ADX 30, RVol 0.2) |
| 8 | **AVGO** | 332.38 | - | **-** | 18 | - | NEG -$64.4M | - | 340 | 340 | +$3.0M | +$0 bull / -$41k bear | out (clean 30, ADX 12, RVol 0.3) |
| 9 | **SHOP** | 146.07 | - | **-** | 18 | - | NEG -$4.0M | - | 145 | 148 | -$4.2M | - | out (clean 34, ADX 18, RVol 0.9) |
| 10 | **SMH** | 518.06 | - | **-** | 17 | - | NEG -$293.1M | - | 532.5 | 500 | +$1.7M | +$311k bull / +$0 bear | out (clean 31, ADX 15, RVol 0.2) |
| 11 | **NVDA** | 207.42 | - | **-** | 17 | - | POS +$97.9M | 203.81 | 210 | 200 | +$12.9M | +$461k bull / -$57k bear | out (clean 29, ADX 17, RVol 0.5) |
| 12 | **MSTR** | 135.87 | - | **-** | 17 | - | POS +$83.1M | - | 135 | 125 | -$3.9M | +$195k bull / +$0 bear | out (clean 29, ADX 11, RVol 0.3) |
| 13 | **BABA** | 100.49 | - | **-** | 17 | - | POS +$2.0M | 99.87 | 102 | 100 | +$62k | +$0 bull / -$28k bear | out (clean 36, ADX 26, RVol 0.3) |
| 14 | **SPY** | 755.74 | - | **-** | 16 | - | NEG -$8.2B | 769.89 | 770 | 750 | -$59.7M | +$121k bull / +$0 bear | out (clean 30, ADX 17, RVol 0.4) |
| 15 | **GOOGL** | 279.13 | - | **-** | 16 | - | NEG -$37.6M | 284.58 | 285 | 290 | +$2.7M | +$26k bull / +$0 bear | out (clean 33, ADX 16, RVol 0.2) |
| 16 | **IWM** | 280.82 | - | **-** | 15 | - | NEG -$1.1B | 286.85 | 285 | 270 | -$2.1M | +$938k bull / +$0 bear | out (clean 32, ADX 15, RVol 0.5) |
| 17 | **AMD** | 487.85 | - | **-** | 15 | - | NEG -$87.1M | - | 520 | 440 | +$6.6M | +$2.0M bull / +$0 bear | out (clean 31, ADX 14, RVol 0.4) |
| 18 | **AAPL** | 332.25 | - | **-** | 14 | - | NEG -$379.4M | 342.91 | 350 | 330 | -$9.0M | +$232k bull / -$506k bear | out (clean 30, ADX 10, RVol 0.4) |
| 19 | **PLTR** | 174.95 | - | **-** | 14 | - | NEG -$25.1M | - | 165 | 180 | -$769k | +$183k bull / +$0 bear | out (clean 27, ADX 20, RVol 0.3) |
| 20 | **MU** | 851.97 | - | **-** | 14 | - | NEG -$205.2M | - | 900 | 850 | -$12.7M | +$3.6M bull / -$220k bear | out (clean 31, ADX 12, RVol 0.5) |
| 21 | **QQQ** | 686.50 | - | **-** | 13 | - | NEG -$4.9B | - | 700 | 680 | +$1.9M | +$496k bull / +$0 bear | out (clean 29, ADX 15, RVol 0.4) |
| 22 | **CRM** | 223.09 | - | **-** | 10 | - | NEG -$13.7M | - | 240 | 220 | -$338k | - | out (clean 29, ADX 17, RVol 0.4) |
| 23 | **UBER** | 66.84 | - | **-** | 9 | - | NEG -$8.3M | - | 70 | 65 | -$357k | - | out (clean 30, ADX 13, RVol 0.7) |
| 24 | **DELL** | 406.58 | - | **-** | 5 | - | NEG -$25.8M | - | 440 | 400 | +$786k | - | out (clean 32, ADX 11, RVol 0.4) |
| 25 | **SMCI** | 31.49 | - | **-** | 5 | - | POS +$2.0M | - | 34.5 | 30 | +$27k | - | out (clean 33, ADX 13, RVol 1.3) |
| 26 | **ARM** | 201.72 | - | **-** | 5 | - | NEG -$6.5M | - | 220 | 200 | -$104k | - | out (clean 25, ADX 16, RVol 0.3) |
| 27 | **HOOD** | 85.03 | - | **-** | 3 | - | NEG -$2.6M | - | 90 | 90 | -$60k | - | out (clean 30, ADX 11, RVol 0.6) |

## Big prints this scan (52)
- **AMD** CALL 477.5 2026-11-06 (3DTE): 64 @ 28.75 = **+$184k** BUY | vol 514 / OI 39
- **META** PUT 620 2026-11-06 (3DTE): 100 @ 10.80 = **+$108k** MID | vol 1,857 / OI 1,386
- **MU** CALL 830 2026-11-04 (1DTE): 32 @ 30.39 = **+$97k** BUY | vol 514 / OI 19
- **AMD** CALL 477.5 2026-11-06 (3DTE): 32 @ 28.98 = **+$93k** BUY | vol 514 / OI 39
- **AMD** PUT 495 2026-11-06 (3DTE): 30 @ 24.35 = **+$73k** SELL | vol 981 / OI 847
- **MU** CALL 830 2026-11-04 (1DTE): 24 @ 30.39 = **+$73k** BUY | vol 514 / OI 19
- **MU** CALL 830 2026-11-04 (1DTE): 24 @ 30.39 = **+$73k** BUY | vol 514 / OI 19
- **AMD** CALL 477.5 2026-11-06 (3DTE): 25 @ 29.00 = **+$72k** BUY | vol 514 / OI 39
- **META** CALL 635 2026-11-06 (3DTE): 111 @ 6.45 = **+$72k** BUY | vol 1,640 / OI 1,669
- **IWM** PUT 288 2026-11-06 (3DTE): 88 @ 7.53 = **+$66k** SELL | vol 144 / OI 103
- **AMZN** PUT 252.5 2026-11-04 (1DTE): 200 @ 3.25 = **+$65k** MID | vol 669 / OI 194
- **MU** CALL 830 2026-11-04 (1DTE): 20 @ 30.03 = **+$60k** SELL | vol 514 / OI 19
- **TSLA** PUT 405 2026-11-06 (3DTE): 50 @ 11.97 = **+$60k** BUY | vol 1,840 / OI 1,980
- **TSLA** CALL 395 2026-11-06 (3DTE): 50 @ 11.43 = **+$57k** SELL | vol 832 / OI 1,893
- **MU** CALL 850 2026-11-04 (1DTE): 32 @ 17.84 = **+$57k** BUY | vol 6,169 / OI 64

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 740 2026-11-05 (2DTE): 2,581 traded vs OI 2,573
- **SPY** CALL 757 2026-11-10 (7DTE): 508 traded vs OI 0
- **QQQ** PUT 675 2026-11-05 (2DTE): 910 traded vs OI 908
- **NVDA** PUT 222.5 2026-11-06 (3DTE): 702 traded vs OI 693
- **NVDA** CALL 195 2026-11-09 (6DTE): 559 traded vs OI 7
- **NVDA** CALL 227.5 2026-11-04 (1DTE): 850 traded vs OI 834
- **AMD** CALL 477.5 2026-11-06 (3DTE): 514 traded vs OI 39
- **AMD** PUT 500 2026-11-04 (1DTE): 556 traded vs OI 430
- **MSFT** CALL 545 2026-11-04 (1DTE): 504 traded vs OI 495
- **NFLX** PUT 63 2026-11-06 (3DTE): 2,981 traded vs OI 2,850
- **PLTR** CALL 177.5 2026-11-20 (17DTE): 500 traded vs OI 163
- **SMCI** PUT 31 2026-11-06 (3DTE): 1,911 traded vs OI 1,842
- **MU** CALL 895 2026-11-06 (3DTE): 500 traded vs OI 231
- **MU** CALL 830 2026-11-04 (1DTE): 514 traded vs OI 19

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
