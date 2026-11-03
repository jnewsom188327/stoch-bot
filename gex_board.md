# GEX + FLOW SCAN - Tue Nov 03, 02:10 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 14:10:08 ET, last candle SPY 14:09, QQQ 14:09 | no errors

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **MSFT** | 521.31 | FLOW SURGE | **PUTS** | 37 | none: 126 puts 0-7DTE > 14 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (12 contracts' greeks worked out here) | POS +$258.5M | 502.27 | 540 | 500 | -$12.8M | +$0 bull / -$61k bear | out (clean 29, ADX 43, RVol 0.8) |
| 2 | **TSLA** | 399.19 | PINNED between the walls (positive gamma) - chop | **-** | 27 | - | POS +$206.2M | - | 400 | 400 | +$14.6M | +$236k bull / -$92k bear | out (clean 31, ADX 20, RVol 0.2) |
| 3 | **ORCL** | 125.98 | - | **-** | 24 | - | NEG -$40.5M | - | 135 | 125 | -$9.3M | +$424k bull / +$0 bear | out (clean 34, ADX 27, RVol 0.5) |
| 4 | **AMZN** | 250.79 | - | **-** | 22 | - | POS +$178.7M | - | 250 | 250 | -$4.4M | +$0 bull / -$219k bear | out (clean 33, ADX 40, RVol 0.7) |
| 5 | **META** | 621.31 | - | **-** | 21 | - | NEG -$31.7M | 626.12 | 650 | 610 | -$16.0M | +$205k bull / +$0 bear | out (clean 28, ADX 24, RVol 0.4) |
| 6 | **COIN** | 145.85 | - | **-** | 21 | - | POS +$21.5M | - | 148 | 150 | -$2.1M | +$77k bull / +$0 bear | out (clean 30, ADX 29, RVol 0.2) |
| 7 | **AVGO** | 332.12 | - | **-** | 18 | - | NEG -$66.3M | - | 340 | 340 | +$3.0M | +$0 bull / -$41k bear | out (clean 30, ADX 12, RVol 0.4) |
| 8 | **MSTR** | 135.84 | - | **-** | 18 | - | POS +$83.4M | - | 135 | 125 | -$3.9M | +$195k bull / +$0 bear | out (clean 29, ADX 12, RVol 0.2) |
| 9 | **SHOP** | 146.16 | - | **-** | 18 | - | NEG -$4.1M | - | 145 | 148 | -$4.2M | - | out (clean 34, ADX 16, RVol 0.8) |
| 10 | **BABA** | 100.48 | - | **-** | 17 | - | POS +$1.6M | 99.95 | 102 | 100 | +$68k | +$0 bull / -$28k bear | out (clean 36, ADX 27, RVol 0.4) |
| 11 | **SPY** | 755.55 | - | **-** | 16 | - | NEG -$8.9B | 770.23 | 770 | 750 | -$66.2M | +$121k bull / +$0 bear | out (clean 29, ADX 18, RVol 0.4) |
| 12 | **NVDA** | 207.34 | - | **-** | 16 | - | POS +$88.6M | 203.81 | 210 | 200 | +$11.6M | +$216k bull / -$57k bear | out (clean 29, ADX 14, RVol 0.5) |
| 13 | **GOOGL** | 279.25 | - | **-** | 16 | - | NEG -$39.1M | 284.92 | 285 | 290 | +$2.6M | +$26k bull / +$0 bear | out (clean 32, ADX 15, RVol 0.2) |
| 14 | **IWM** | 280.76 | - | **-** | 15 | - | NEG -$1.1B | 286.86 | 285 | 270 | -$2.6M | +$620k bull / +$0 bear | out (clean 32, ADX 15, RVol 0.4) |
| 15 | **PLTR** | 175.19 | - | **-** | 15 | - | NEG -$24.9M | - | 165 | 180 | -$1.1M | +$90k bull / +$0 bear | out (clean 27, ADX 22, RVol 0.3) |
| 16 | **ARM** | 201.91 | - | **-** | 15 | - | NEG -$6.6M | - | 220 | 200 | -$122k | +$29k bull / +$0 bear | out (clean 25, ADX 12, RVol 0.4) |
| 17 | **AAPL** | 332.28 | - | **-** | 14 | - | NEG -$381.5M | 342.79 | 350 | 330 | -$8.3M | +$232k bull / -$469k bear | out (clean 30, ADX 10, RVol 0.5) |
| 18 | **AMD** | 488.73 | - | **-** | 14 | - | NEG -$87.9M | - | 520 | 440 | +$5.5M | +$1.0M bull / +$0 bear | out (clean 31, ADX 13, RVol 0.4) |
| 19 | **MU** | 850.12 | - | **-** | 14 | - | NEG -$205.2M | - | 900 | 850 | -$12.9M | +$2.1M bull / -$249k bear | out (clean 31, ADX 12, RVol 0.5) |
| 20 | **QQQ** | 686.40 | - | **-** | 13 | - | NEG -$5.1B | - | 700 | 680 | -$4.2M | +$496k bull / +$0 bear | out (clean 29, ADX 14, RVol 0.4) |
| 21 | **NFLX** | 63.15 | - | **-** | 12 | - | NEG -$7.6M | 64.41 | 65 | 65 | -$548k | - | out (clean 28, ADX 36, RVol 0.6) |
| 22 | **CRM** | 223.26 | - | **-** | 11 | - | NEG -$14.0M | - | 240 | 220 | -$336k | - | out (clean 29, ADX 17, RVol 0.7) |
| 23 | **UBER** | 66.87 | - | **-** | 9 | - | NEG -$8.6M | - | 70 | 65 | -$332k | - | out (clean 30, ADX 13, RVol 0.6) |
| 24 | **SMH** | 518.39 | - | **-** | 6 | - | NEG -$294.5M | - | 532.5 | 500 | +$1.3M | - | out (clean 31, ADX 12, RVol 0.4) |
| 25 | **SMCI** | 31.45 | - | **-** | 6 | - | POS +$1.9M | - | 34.5 | 30 | -$88k | - | out (clean 33, ADX 12, RVol 1.6) |
| 26 | **DELL** | 407.21 | - | **-** | 5 | - | NEG -$26.3M | - | 440 | 400 | +$715k | - | out (clean 32, ADX 10, RVol 0.4) |
| 27 | **HOOD** | 85.09 | - | **-** | 3 | - | NEG -$2.7M | - | 90 | 85 | -$69k | - | out (clean 30, ADX 12, RVol 0.5) |

## Big prints this scan (76)
- **QQQ** PUT 687 2026-11-03 (0DTE): 1,955 @ 1.23 = **+$240k** SELL | vol 165,011 / OI 337
- **AMD** CALL 477.5 2026-11-06 (3DTE): 64 @ 29.50 = **+$189k** BUY | vol 385 / OI 39
- **ORCL** CALL 130 2026-11-06 (3DTE): 691 @ 2.46 = **+$170k** BUY | vol 34,827 / OI 3,741
- **QQQ** CALL 660 2026-11-03 (0DTE): 55 @ 27.37 = **+$151k** BUY | vol 195 / OI 32
- **IWM** CALL 283 2026-11-04 (1DTE): 1,093 @ 1.20 = **+$131k** BUY | vol 4,541 / OI 365
- **IWM** CALL 281 2026-11-04 (1DTE): 622 @ 2.09 = **+$130k** BUY | vol 5,371 / OI 522
- **MU** PUT 855 2026-11-06 (3DTE): 50 @ 25.82 = **+$129k** SELL | vol 2,188 / OI 740
- **IWM** CALL 280 2026-11-04 (1DTE): 480 @ 2.56 = **+$123k** BUY | vol 5,511 / OI 484
- **AAPL** CALL 330 2026-11-06 (3DTE): 200 @ 5.47 = **+$109k** SELL | vol 6,914 / OI 664
- **IWM** CALL 282 2026-11-04 (1DTE): 677 @ 1.60 = **+$108k** BUY | vol 8,771 / OI 417
- **QQQ** CALL 688 2026-11-03 (0DTE): 1,166 @ 0.90 = **+$105k** BUY | vol 246,718 / OI 461
- **AMD** CALL 477.5 2026-11-06 (3DTE): 34 @ 29.38 = **+$100k** BUY | vol 385 / OI 39
- **TSLA** CALL 400 2026-11-04 (1DTE): 150 @ 5.70 = **+$86k** BUY | vol 20,636 / OI 1,213
- **TSLA** CALL 400 2026-11-04 (1DTE): 150 @ 5.50 = **+$82k** MID | vol 20,636 / OI 1,213
- **MU** CALL 860 2026-11-04 (1DTE): 50 @ 15.25 = **+$76k** BUY | vol 11,290 / OI 60

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 792 2026-11-05 (2DTE): 511 traded vs OI 0
- **SPY** PUT 680 2026-11-04 (1DTE): 928 traded vs OI 324
- **SPY** PUT 715 2026-11-04 (1DTE): 3,063 traded vs OI 2,435
- **SPY** PUT 690 2026-11-17 (14DTE): 1,130 traded vs OI 0
- **IWM** CALL 286 2026-11-05 (2DTE): 2,267 traded vs OI 200
- **NVDA** PUT 205 2026-11-06 (3DTE): 9,376 traded vs OI 9,312
- **AMD** PUT 440 2026-11-06 (3DTE): 882 traded vs OI 728
- **META** PUT 605 2026-11-04 (1DTE): 823 traded vs OI 817
- **AMZN** CALL 247.5 2026-11-20 (17DTE): 853 traded vs OI 852
- **MSTR** CALL 146 2026-11-06 (3DTE): 513 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
