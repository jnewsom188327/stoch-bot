# GEX + FLOW SCAN - Tue Nov 03, 11:50 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 11:50:08 ET, last candle SPY 11:49, QQQ 11:49 | no errors

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **BABA** | 100.01 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 47 | none: 20 calls 0-7DTE > 2 priced 0.40-0.80 > 2 delta 0.2+ > 2 spread ok > 2 liquid > best one only +7% at the target (needs +20%) | POS +$695k | 99.87 | 102 | 100 | +$249k | +$28k bull / +$0 bear | out (clean 36, ADX 61, RVol 0.6) |
| 2 | **COIN** | 148.71 | - | **-** | 33 | - | POS +$20.7M | - | 148 | 150 | -$4.0M | +$158k bull / +$0 bear | out (clean 29, ADX 58, RVol 0.7) |
| 3 | **META** | 619.42 | - | **-** | 28 | - | NEG -$42.0M | 626.35 | 650 | 610 | -$16.1M | +$177k bull / -$446k bear | out (clean 28, ADX 44, RVol 0.4) |
| 4 | **ORCL** | 125.03 | - | **-** | 27 | - | NEG -$40.9M | - | 135 | 125 | -$6.3M | +$162k bull / -$34k bear | out (clean 33, ADX 38, RVol 0.7) |
| 5 | **MSFT** | 516.00 | - | **-** | 26 | - | POS +$179.3M | 501.68 | 540 | 500 | -$7.6M | +$0 bull / -$1.0M bear | out (clean 29, ADX 29, RVol 0.5) |
| 6 | **MSTR** | 136.37 | - | **-** | 26 | - | POS +$81.9M | - | 135 | 125 | -$5.0M | +$42k bull / -$1.0M bear | out (clean 29, ADX 39, RVol 0.7) |
| 7 | **SHOP** | 145.10 | - | **-** | 25 | - | NEG -$3.7M | - | 145 | 148 | -$4.1M | - | out (clean 31, ADX 32, RVol 1.6) |
| 8 | **DELL** | 406.54 | - | **-** | 24 | - | NEG -$25.6M | - | 440 | 400 | +$2.2M | +$105k bull / +$0 bear | out (clean 33, ADX 21, RVol 0.3) |
| 9 | **AVGO** | 331.38 | - | **-** | 22 | - | NEG -$69.0M | - | 340 | 340 | +$2.8M | +$220k bull / -$83k bear | out (clean 31, ADX 27, RVol 0.6) |
| 10 | **TSLA** | 398.28 | - | **-** | 21 | - | POS +$199.1M | - | 400 | 400 | +$19.8M | +$4.0M bull / -$117k bear | out (clean 30, ADX 32, RVol 0.6) |
| 11 | **NVDA** | 207.88 | - | **-** | 19 | - | POS +$116.8M | 203.64 | 210 | 200 | +$7.9M | +$694k bull / +$0 bear | out (clean 30, ADX 26, RVol 1.0) |
| 12 | **GOOGL** | 278.43 | - | **-** | 19 | - | NEG -$42.8M | 284.76 | 285 | 290 | +$2.9M | +$30k bull / -$30k bear | out (clean 33, ADX 20, RVol 0.5) |
| 13 | **SMH** | 519.81 | - | **-** | 18 | - | NEG -$273.1M | - | 532.5 | 500 | +$911k | +$132k bull / +$0 bear | out (clean 32, ADX 24, RVol 0.5) |
| 14 | **AMD** | 489.53 | - | **-** | 18 | - | NEG -$67.0M | - | 520 | 500 | +$4.8M | +$2.3M bull / -$246k bear | out (clean 32, ADX 29, RVol 0.6) |
| 15 | **SPY** | 754.63 | - | **-** | 17 | - | NEG -$9.0B | 770.41 | 770 | 750 | -$47.9M | +$5.1M bull / +$0 bear | out (clean 30, ADX 19, RVol 0.5) |
| 16 | **IWM** | 280.85 | - | **-** | 17 | - | NEG -$1.1B | 287.14 | 285 | 270 | -$2.0M | +$399k bull / +$0 bear | out (clean 32, ADX 23, RVol 0.8) |
| 17 | **AAPL** | 330.71 | - | **-** | 17 | - | NEG -$389.2M | 342.11 | 350 | 330 | -$7.9M | +$234k bull / -$667k bear | out (clean 31, ADX 25, RVol 0.7) |
| 18 | **PLTR** | 173.06 | - | **-** | 17 | - | NEG -$25.1M | - | 165 | 180 | +$443k | +$230k bull / -$125k bear | out (clean 27, ADX 26, RVol 1.1) |
| 19 | **QQQ** | 685.40 | - | **-** | 16 | - | NEG -$5.1B | - | 700 | 680 | +$8.2M | +$3.8M bull / -$250k bear | out (clean 30, ADX 20, RVol 0.8) |
| 20 | **MU** | 849.90 | - | **-** | 16 | - | NEG -$204.7M | - | 900 | 850 | -$3.8M | +$5.0M bull / -$2.6M bear | out (clean 32, ADX 22, RVol 0.6) |
| 21 | **AMZN** | 247.92 | - | **-** | 15 | - | POS +$147.7M | 236 | 250 | 250 | -$489k | +$0 bull / -$65k bear | out (clean 33, ADX 19, RVol 0.5) |
| 22 | **HOOD** | 84.81 | - | **-** | 14 | - | NEG -$2.7M | - | 90 | 90 | -$77k | +$93k bull / +$0 bear | out (clean 31, ADX 19, RVol 0.1) |
| 23 | **CRM** | 222.80 | - | **-** | 13 | - | NEG -$13.9M | - | 240 | 220 | -$381k | - | out (clean 30, ADX 19, RVol 0.7) |
| 24 | **UBER** | 66.75 | - | **-** | 10 | - | NEG -$8.9M | - | 70 | 65 | -$126k | - | out (clean 29, ADX 13, RVol 0.6) |
| 25 | **NFLX** | 62.31 | - | **-** | 9 | - | NEG -$12.6M | 64.29 | 63 | 60 | -$276k | - | out (clean 28, ADX 24, RVol 0.6) |
| 26 | **SMCI** | 31.34 | - | **-** | 9 | - | NEG -$468k | - | 33 | 30 | +$219k | - | out (clean 34, ADX 21, RVol 1.6) |
| 27 | **ARM** | 202.00 | - | **-** | 8 | - | NEG -$6.5M | - | 220 | 200 | -$140k | - | out (clean 25, ADX 22, RVol 0.5) |

## Big prints this scan (95)
- **SPY** PUT 760 2026-11-05 (2DTE): 500 @ 8.00 = **+$400k** SELL | vol 4,297 / OI 2,551
- **TSLA** CALL 395 2026-11-04 (1DTE): 479 @ 8.10 = **+$388k** MID | vol 2,419 / OI 719
- **SPY** PUT 760 2026-11-05 (2DTE): 469 @ 8.00 = **+$375k** SELL | vol 4,297 / OI 2,551
- **AAPL** PUT 325 2026-11-06 (3DTE): 1,198 @ 1.95 = **+$234k** SELL | vol 13,973 / OI 14,287
- **TSLA** CALL 402.5 2026-11-06 (3DTE): 300 @ 7.45 = **+$224k** MID | vol 3,424 / OI 5,017
- **MU** PUT 825 2026-11-04 (1DTE): 200 @ 9.00 = **+$180k** BUY | vol 2,600 / OI 322
- **MU** PUT 825 2026-11-04 (1DTE): 200 @ 9.00 = **+$180k** BUY | vol 2,600 / OI 322
- **MU** PUT 825 2026-11-04 (1DTE): 190 @ 9.00 = **+$171k** BUY | vol 2,600 / OI 322
- **MU** PUT 825 2026-11-04 (1DTE): 184 @ 9.00 = **+$166k** BUY | vol 2,600 / OI 322
- **SPY** PUT 756 2026-11-04 (1DTE): 298 @ 4.91 = **+$146k** SELL | vol 12,028 / OI 448
- **MU** PUT 860 2026-11-04 (1DTE): 60 @ 24.00 = **+$144k** BUY | vol 7,330 / OI 273
- **QQQ** PUT 685 2026-11-04 (1DTE): 180 @ 7.05 = **+$127k** BUY | vol 14,571 / OI 3,872
- **QQQ** CALL 684 2026-11-03 (0DTE): 411 @ 3.00 = **+$123k** SELL | vol 21,874 / OI 310
- **SPY** PUT 754 2026-11-06 (3DTE): 200 @ 5.85 = **+$117k** MID | vol 4,850 / OI 1,982
- **SPY** PUT 754 2026-11-06 (3DTE): 200 @ 5.80 = **+$116k** SELL | vol 4,850 / OI 1,982

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 770 2026-11-03 (0DTE): 5,957 traded vs OI 5,322
- **SPY** CALL 778 2026-11-04 (1DTE): 7,590 traded vs OI 866
- **SPY** PUT 756 2026-11-05 (2DTE): 511 traded vs OI 0
- **SPY** PUT 751 2026-11-04 (1DTE): 4,286 traded vs OI 4,034
- **SPY** PUT 760 2026-11-05 (2DTE): 4,297 traded vs OI 2,551
- **SPY** CALL 765 2026-11-13 (10DTE): 1,517 traded vs OI 1,513
- **IWM** CALL 295 2026-11-11 (8DTE): 525 traded vs OI 0
- **IWM** CALL 282 2026-11-13 (10DTE): 906 traded vs OI 763
- **IWM** PUT 260 2026-11-04 (1DTE): 771 traded vs OI 276
- **NVDA** PUT 192.5 2026-11-09 (6DTE): 515 traded vs OI 332
- **NVDA** CALL 222.5 2026-11-04 (1DTE): 4,354 traded vs OI 3,308
- **NVDA** CALL 225 2026-11-16 (13DTE): 1,193 traded vs OI 0
- **TSLA** CALL 405 2026-11-27 (24DTE): 769 traded vs OI 685
- **TSLA** PUT 365 2026-11-04 (1DTE): 1,130 traded vs OI 1,093
- **AMD** PUT 465 2026-11-04 (1DTE): 529 traded vs OI 123

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
