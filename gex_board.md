# GEX + FLOW SCAN - Tue Nov 03, 10:10 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:10:08 ET, last candle SPY 10:09, QQQ 10:09 | no errors

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **DELL** | 410.16 | RUN: clean trend + negative gamma + flow agrees | **CALLS** | 73 | none: 33 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$25.9M | - | 440 | 400 | +$1.9M | +$273k bull / +$0 bear | LONG (clean 35, ADX 41, RVol 1.2) |
| 2 | **SHOP** | 141.62 | FLOW SURGE | **PUTS** | 64 | none: 25 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$4.2M | - | 145 | 140 | -$2.9M | +$0 bull / -$1.0M bear | out (clean 32, ADX 54, RVol 3.2) |
| 3 | **ORCL** | 124.15 | FLOW SURGE | **PUTS** | 57 | none: 25 puts 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$41.6M | - | 135 | 120 | -$2.7M | +$0 bull / -$350k bear | out (clean 32, ADX 41, RVol 3.2) |
| 4 | **MSTR** | 134.71 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 56 | none: 27 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$76.3M | - | 135 | 125 | -$2.3M | +$30k bull / -$303k bear | out (clean 27, ADX 33, RVol 1.4) |
| 5 | **AVGO** | 333.51 | FLOW SURGE | **CALLS** | 47 | none: 78 calls 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (6 contracts' greeks worked out here) | NEG -$45.8M | - | 340 | 340 | +$3.1M | +$1.8M bull / +$0 bear | out (clean 31, ADX 36, RVol 1.5) |
| 6 | **SMCI** | 31.69 | TREND (flow not with it) | **CALLS** | 45 | none: 12 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$2.1M | - | 34.5 | 30 | -$161k | +$87k bull / +$0 bear | LONG (clean 36, ADX 35, RVol 1.7) |
| 7 | **BABA** | 100.84 | TREND (flow not with it) | **PUTS** | 45 | 11/06 98P @ 0.78 (delta 0.26) = est +24% at 100.03 | POS +$2.5M | 100.03 | 102 | 100 | +$61k | - | SHORT (clean 35, ADX 60, RVol 1.5) |
| 8 | **GOOGL** | 278.36 | FLOW SURGE | **CALLS** | 44 | none: 66 calls 0-7DTE > 8 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (2 contracts' greeks worked out here) | NEG -$44.6M | 285.35 | 285 | 290 | +$2.8M | +$228k bull / +$0 bear | SHORT (clean 34, ADX 35, RVol 0.6) |
| 9 | **META** | 615.84 | FLOW SURGE | **PUTS** | 39 | none: 146 puts 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$70.2M | 627.34 | 650 | 610 | -$5.5M | +$0 bull / -$1.5M bear | out (clean 27, ADX 24, RVol 0.8) |
| 10 | **COIN** | 144.63 | - | **-** | 30 | - | POS +$20.7M | - | 148 | 140 | -$905k | - | out (clean 26, ADX 45, RVol 1.1) |
| 11 | **PLTR** | 169.94 | - | **-** | 29 | - | NEG -$27.7M | - | 165 | 180 | +$2.8M | +$933k bull / +$0 bear | out (clean 28, ADX 58, RVol 3.2) |
| 12 | **SMH** | 520.24 | - | **-** | 27 | - | NEG -$288.6M | - | 532.5 | 500 | +$1.3M | +$427k bull / +$0 bear | out (clean 33, ADX 38, RVol 1.9) |
| 13 | **AMD** | 489.28 | - | **-** | 27 | - | NEG -$68.5M | - | 520 | 500 | +$5.8M | +$7.4M bull / -$29k bear | out (clean 33, ADX 47, RVol 2.3) |
| 14 | **MSFT** | 512.61 | - | **-** | 27 | - | POS +$136.3M | 500.7 | 535 | 500 | -$1.5M | +$716k bull / -$283k bear | out (clean 29, ADX 46, RVol 0.9) |
| 15 | **AAPL** | 332.93 | - | **-** | 26 | - | NEG -$345.1M | 343.05 | 350 | 330 | -$15.0M | +$1.4M bull / -$2.3M bear | out (clean 32, ADX 31, RVol 2.8) |
| 16 | **NVDA** | 208.14 | - | **-** | 24 | - | POS +$109.7M | 203.56 | 210 | 200 | +$7.9M | +$2.6M bull / -$68k bear | out (clean 31, ADX 40, RVol 1.2) |
| 17 | **MU** | 860.42 | - | **-** | 23 | - | NEG -$189.4M | - | 900 | 850 | +$10.9M | +$6.4M bull / -$1.0M bear | out (clean 32, ADX 40, RVol 1.3) |
| 18 | **CRM** | 217.65 | - | **-** | 23 | - | NEG -$15.4M | - | 230 | 220 | -$41k | +$0 bull / -$29k bear | out (clean 28, ADX 55, RVol 1.9) |
| 19 | **QQQ** | 685.94 | - | **-** | 22 | - | NEG -$5.0B | - | 700 | 680 | +$32.9M | +$11.2M bull / -$138k bear | out (clean 32, ADX 30, RVol 1.1) |
| 20 | **AMZN** | 246.95 | - | **-** | 22 | - | POS +$134.1M | 236.15 | 250 | 250 | +$1.5M | +$131k bull / +$0 bear | out (clean 34, ADX 30, RVol 0.8) |
| 21 | **TSLA** | 402.31 | - | **-** | 20 | - | POS +$248.6M | - | 400 | 400 | +$6.3M | +$647k bull / -$1.9M bear | out (clean 31, ADX 26, RVol 0.8) |
| 22 | **SPY** | 754.05 | - | **-** | 19 | - | NEG -$9.2B | 770.56 | 770 | 750 | +$3.1M | +$2.2M bull / -$541k bear | out (clean 31, ADX 31, RVol 1.6) |
| 23 | **NFLX** | 62.18 | - | **-** | 18 | - | NEG -$14.2M | 64.57 | 63 | 60 | -$53k | +$0 bull / -$30k bear | out (clean 28, ADX 25, RVol 0.6) |
| 24 | **HOOD** | 84.71 | - | **-** | 18 | - | NEG -$3.0M | - | 90 | 85 | -$81k | +$81k bull / +$0 bear | out (clean 32, ADX 28, RVol 0.9) |
| 25 | **IWM** | 280.44 | - | **-** | 17 | - | NEG -$1.2B | 287.3 | 285 | 270 | -$725k | +$0 bull / -$291k bear | out (clean 33, ADX 19, RVol 0.9) |
| 26 | **ARM** | 203.31 | - | **-** | 9 | - | NEG -$6.7M | - | 220 | 200 | -$48k | - | out (clean 25, ADX 32, RVol 0.8) |
| 27 | **UBER** | 66.34 | - | **-** | 9 | - | NEG -$13.5M | - | 70 | 65 | -$9k | - | out (clean 29, ADX 29, RVol 1.0) |

## Big prints this scan (158)
- **MU** PUT 860 2026-11-04 (1DTE): 246 @ 15.90 = **+$391k** SELL | vol 2,293 / OI 273
- **QQQ** CALL 685 2026-11-05 (2DTE): 418 @ 9.00 = **+$376k** BUY | vol 967 / OI 185
- **MU** PUT 840 2026-11-04 (1DTE): 358 @ 9.95 = **+$356k** SELL | vol 1,699 / OI 244
- **SPY** CALL 760 2026-11-06 (3DTE): 848 @ 3.76 = **+$319k** SELL | vol 5,506 / OI 4,400
- **TSLA** PUT 397.5 2026-11-04 (1DTE): 601 @ 5.03 = **+$302k** BUY | vol 4,020 / OI 2,674
- **AMZN** CALL 252.5 2026-11-06 (3DTE): 1,500 @ 1.90 = **+$285k** MID | vol 1,926 / OI 2,082
- **AMD** PUT 500 2026-11-04 (1DTE): 97 @ 24.00 = **+$233k** SELL | vol 228 / OI 430
- **SPY** CALL 760 2026-11-06 (3DTE): 590 @ 3.76 = **+$222k** SELL | vol 5,506 / OI 4,400
- **MU** CALL 860 2026-11-06 (3DTE): 73 @ 27.40 = **+$200k** BUY | vol 645 / OI 194
- **MU** PUT 855 2026-11-04 (1DTE): 96 @ 17.50 = **+$168k** BUY | vol 1,305 / OI 281
- **SMH** CALL 510 2026-11-04 (1DTE): 100 @ 15.43 = **+$154k** BUY | vol 110 / OI 0
- **QQQ** PUT 700 2026-11-06 (3DTE): 82 @ 17.88 = **+$147k** SELL | vol 1,272 / OI 22,016
- **META** CALL 620 2026-11-06 (3DTE): 150 @ 9.65 = **+$145k** SELL | vol 790 / OI 1,626
- **QQQ** PUT 684 2026-11-04 (1DTE): 217 @ 6.37 = **+$138k** BUY | vol 1,949 / OI 263
- **MU** PUT 855 2026-11-04 (1DTE): 77 @ 17.78 = **+$137k** BUY | vol 1,305 / OI 281

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 747 2026-11-03 (0DTE): 616 traded vs OI 81
- **SPY** CALL 756 2026-11-06 (3DTE): 876 traded vs OI 875
- **SPY** PUT 748 2026-11-04 (1DTE): 662 traded vs OI 600
- **SPY** CALL 761 2026-11-04 (1DTE): 1,623 traded vs OI 1,464
- **SPY** CALL 760 2026-11-06 (3DTE): 5,506 traded vs OI 4,400
- **SPY** PUT 723 2026-11-03 (0DTE): 608 traded vs OI 0
- **QQQ** CALL 707 2026-11-04 (1DTE): 2,258 traded vs OI 528
- **QQQ** CALL 695 2026-11-04 (1DTE): 2,169 traded vs OI 2,013
- **QQQ** CALL 714 2026-11-03 (0DTE): 911 traded vs OI 823
- **QQQ** CALL 686 2026-11-06 (3DTE): 541 traded vs OI 398
- **QQQ** CALL 704 2026-11-04 (1DTE): 584 traded vs OI 338
- **QQQ** CALL 685 2026-11-05 (2DTE): 967 traded vs OI 185
- **QQQ** CALL 708 2026-11-04 (1DTE): 510 traded vs OI 363
- **QQQ** CALL 705 2026-11-05 (2DTE): 823 traded vs OI 766
- **IWM** CALL 283 2026-11-04 (1DTE): 507 traded vs OI 365

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
