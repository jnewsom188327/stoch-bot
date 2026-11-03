# GEX + FLOW SCAN - Tue Nov 03, 09:50 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 09:50:08 ET, last candle SPY 09:49, QQQ 09:49 | no errors

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **CRM** | 215.35 | FLOW SURGE | **CALLS** | 66 | none: 16 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$14.8M | - | 230 | 220 | +$244k | +$66k bull / +$0 bear | out (clean 28, ADX 49, RVol 4.6) |
| 2 | **BABA** | 100.92 | TREND (flow not with it) | **PUTS** | 64 | 11/06 98P @ 0.75 (delta 0.26) = est +31% at 100 | POS +$3.2M | 99.88 | 102 | 100 | +$29k | - | SHORT (clean 34, ADX 56, RVol 4.4) |
| 3 | **ARM** | 205.27 | FLOW SURGE | **PUTS** | 63 | none: 17 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$6.5M | - | 220 | 200 | -$234k | +$0 bull / -$31k bear | out (clean 26, ADX 36, RVol 3.2) |
| 4 | **ORCL** | 123.97 | FLOW SURGE | **PUTS** | 62 | none: 25 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$42.1M | - | 135 | 120 | -$1.3M | +$0 bull / -$60k bear | out (clean 32, ADX 36, RVol 6.8) |
| 5 | **AAPL** | 333.78 | FLOW SURGE | **PUTS** | 60 | none: 77 puts 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (5 contracts' greeks worked out here) | NEG -$311.4M | 343.9 | 350 | 330 | -$15.4M | +$0 bull / -$3.3M bear | out (clean 32, ADX 32, RVol 7.4) |
| 6 | **SHOP** | 141.22 | FLOW SURGE | **PUTS** | 59 | none: 25 puts 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$3.6M | - | 145 | 140 | -$330k | +$0 bull / -$160k bear | out (clean 31, ADX 50, RVol 7.1) |
| 7 | **MSFT** | 510.65 | FLOW SURGE | **PUTS** | 58 | none: 121 puts 0-7DTE > 11 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (10 contracts' greeks worked out here) | POS +$111.1M | 500.8 | 535 | 500 | -$868k | +$39k bull / -$298k bear | out (clean 29, ADX 57, RVol 3.4) |
| 8 | **SMCI** | 32.06 | TREND (flow not with it) | **CALLS** | 58 | none: 13 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$2.2M | - | 34.5 | 30 | -$133k | - | LONG (clean 36, ADX 40, RVol 3.1) |
| 9 | **SMH** | 522.80 | FLOW SURGE | **PUTS** | 57 | none: 126 puts 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (11 contracts' greeks worked out here) | NEG -$266.9M | - | 532.5 | 500 | -$652k | +$0 bull / -$752k bear | out (clean 33, ADX 45, RVol 3.9) |
| 10 | **MSTR** | 134.35 | FLOW SURGE | **PUTS** | 57 | none: 27 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$75.6M | - | 135 | 125 | -$1.0M | +$0 bull / -$399k bear | out (clean 26, ADX 31, RVol 2.5) |
| 11 | **NVDA** | 208.65 | FLOW SURGE | **PUTS** | 52 | none: 48 puts 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (2 contracts' greeks worked out here) | POS +$121.3M | 203.3 | 210 | 200 | -$6.9M | +$186k bull / -$1.4M bear | out (clean 30, ADX 41, RVol 3.3) |
| 12 | **DELL** | 415.25 | TREND (flow not with it) | **CALLS** | 49 | none: 33 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$25.0M | - | 440 | 400 | -$121k | +$0 bull / -$688k bear | LONG (clean 35, ADX 46, RVol 3.0) |
| 13 | **GOOGL** | 279.15 | TREND (flow not with it) | **PUTS** | 43 | none: 66 puts 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (2 contracts' greeks worked out here) | NEG -$41.7M | 285.93 | 285 | 290 | +$269k | - | SHORT (clean 33, ADX 30, RVol 2.1) |
| 14 | **MU** | 867.52 | - | **-** | 33 | - | NEG -$174.2M | - | 900 | 850 | +$14.9M | +$3.3M bull / -$5.9M bear | out (clean 32, ADX 47, RVol 3.8) |
| 15 | **COIN** | 143.55 | - | **-** | 32 | - | POS +$18.3M | - | 142 | 140 | -$151k | - | out (clean 25, ADX 37, RVol 3.1) |
| 16 | **AMZN** | 246.21 | - | **-** | 31 | - | POS +$124.9M | 236.04 | 250 | 250 | +$1.0M | +$319k bull / +$0 bear | out (clean 34, ADX 37, RVol 2.3) |
| 17 | **PLTR** | 169.71 | - | **-** | 31 | - | NEG -$27.6M | - | 165 | 180 | +$1.7M | +$26k bull / -$469k bear | out (clean 27, ADX 54, RVol 9.2) |
| 18 | **SPY** | 754.03 | - | **-** | 29 | - | NEG -$9.2B | 770.5 | 750 | 750 | -$16.1M | +$0 bull / -$5.4M bear | out (clean 31, ADX 37, RVol 4.6) |
| 19 | **AMD** | 492.75 | - | **-** | 27 | - | NEG -$66.1M | - | 520 | 500 | -$1.5M | +$0 bull / -$3.9M bear | out (clean 33, ADX 53, RVol 5.4) |
| 20 | **NFLX** | 61.95 | - | **-** | 27 | - | NEG -$16.2M | 64.68 | 63 | 60 | +$121k | - | out (clean 29, ADX 25, RVol 2.5) |
| 21 | **AVGO** | 335.34 | - | **-** | 27 | - | NEG -$39.1M | 352.11 | 340 | 340 | -$322k | +$0 bull / -$28k bear | out (clean 32, ADX 36, RVol 3.6) |
| 22 | **HOOD** | 85.04 | - | **-** | 26 | - | NEG -$2.7M | - | 90 | 85 | -$267k | - | out (clean 32, ADX 29, RVol 1.6) |
| 23 | **TSLA** | 401.92 | - | **-** | 25 | - | POS +$236.9M | - | 400 | 400 | +$2.6M | +$2.2M bull / -$819k bear | out (clean 31, ADX 31, RVol 1.9) |
| 24 | **QQQ** | 686.48 | - | **-** | 24 | - | NEG -$5.0B | - | 700 | 680 | -$4.7M | +$0 bull / -$6.0M bear | out (clean 32, ADX 39, RVol 2.9) |
| 25 | **IWM** | 279.96 | - | **-** | 24 | - | NEG -$1.3B | 287.45 | 285 | 270 | +$664k | +$52k bull / +$0 bear | out (clean 32, ADX 22, RVol 2.7) |
| 26 | **META** | 612.04 | - | **-** | 22 | - | NEG -$82.3M | 626.28 | 650 | 610 | -$515k | +$312k bull / -$143k bear | out (clean 27, ADX 18, RVol 2.1) |
| 27 | **UBER** | 66.22 | - | **-** | 20 | - | NEG -$13.8M | - | 70 | 65 | -$10k | - | out (clean 29, ADX 35, RVol 3.3) |

## Big prints this scan (449)
- **QQQ** PUT 685 2026-11-04 (1DTE): 2,808 @ 7.56 = **+$2.1M** BUY | vol 6,305 / OI 3,872
- **QQQ** PUT 685 2026-11-04 (1DTE): 1,675 @ 7.56 = **+$1.3M** BUY | vol 6,305 / OI 3,872
- **SPY** PUT 756 2026-11-04 (1DTE): 2,000 @ 5.85 = **+$1.2M** BUY | vol 6,102 / OI 448
- **AMD** PUT 495 2026-11-06 (3DTE): 182 @ 33.50 = **+$610k** BUY | vol 553 / OI 847
- **QQQ** PUT 685 2026-11-04 (1DTE): 798 @ 7.56 = **+$603k** BUY | vol 6,305 / OI 3,872
- **SPY** PUT 756 2026-11-04 (1DTE): 904 @ 5.95 = **+$538k** BUY | vol 6,102 / OI 448
- **AMD** CALL 472.5 2026-11-06 (3DTE): 200 @ 25.25 = **+$505k** SELL | vol 204 / OI 56
- **SPY** PUT 756 2026-11-04 (1DTE): 822 @ 5.75 = **+$473k** BUY | vol 6,102 / OI 448
- **AMD** PUT 495 2026-11-06 (3DTE): 143 @ 31.65 = **+$453k** BUY | vol 553 / OI 847
- **TSLA** PUT 405 2026-11-04 (1DTE): 500 @ 8.10 = **+$405k** SELL | vol 3,690 / OI 419
- **AMD** CALL 472.5 2026-11-04 (1DTE): 180 @ 21.90 = **+$394k** SELL | vol 232 / OI 38
- **SPY** PUT 760 2026-11-04 (1DTE): 436 @ 8.48 = **+$370k** BUY | vol 705 / OI 2,103
- **AMD** CALL 492.5 2026-11-06 (3DTE): 200 @ 16.20 = **+$324k** SELL | vol 210 / OI 69
- **SPY** PUT 760 2026-11-03 (0DTE): 436 @ 7.22 = **+$315k** BUY | vol 702 / OI 1,389
- **MU** CALL 880 2026-11-06 (3DTE): 150 @ 18.55 = **+$278k** SELL | vol 391 / OI 913

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 756 2026-11-03 (0DTE): 939 traded vs OI 727
- **SPY** CALL 775 2026-11-03 (0DTE): 2,129 traded vs OI 2,054
- **SPY** PUT 742 2026-11-05 (2DTE): 713 traded vs OI 0
- **SPY** PUT 722 2026-11-03 (0DTE): 540 traded vs OI 0
- **SPY** PUT 743 2026-11-05 (2DTE): 638 traded vs OI 0
- **SPY** CALL 754 2026-11-04 (1DTE): 1,403 traded vs OI 184
- **SPY** PUT 741 2026-11-03 (0DTE): 2,100 traded vs OI 2,047
- **SPY** CALL 790 2026-11-09 (6DTE): 1,202 traded vs OI 1,121
- **SPY** PUT 718 2026-11-03 (0DTE): 3,533 traded vs OI 0
- **SPY** CALL 752 2026-11-04 (1DTE): 583 traded vs OI 447
- **SPY** PUT 754 2026-11-03 (0DTE): 3,418 traded vs OI 2,686
- **SPY** CALL 755 2026-11-04 (1DTE): 978 traded vs OI 640
- **SPY** CALL 757 2026-11-03 (0DTE): 7,213 traded vs OI 3,269
- **SPY** CALL 776 2026-11-03 (0DTE): 3,903 traded vs OI 1,262
- **SPY** PUT 719 2026-11-03 (0DTE): 1,154 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
