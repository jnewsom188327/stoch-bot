# GEX + FLOW SCAN - Tue Nov 03, 02:00 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 14:00:08 ET, last candle SPY 13:59, QQQ 13:59 | no errors

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **MSFT** | 521.13 | FLOW SURGE | **PUTS** | 37 | none: 126 puts 0-7DTE > 16 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (23 contracts' greeks worked out here) | POS +$256.7M | 501.99 | 540 | 500 | -$12.5M | +$0 bull / -$102k bear | out (clean 29, ADX 42, RVol 0.7) |
| 2 | **TSLA** | 399.07 | PINNED between the walls (positive gamma) - chop | **-** | 28 | - | POS +$208.6M | - | 400 | 400 | +$13.5M | +$0 bull / -$651k bear | out (clean 31, ADX 21, RVol 0.3) |
| 3 | **ORCL** | 126.53 | - | **-** | 25 | - | NEG -$39.5M | - | 135 | 125 | -$10.1M | +$511k bull / +$0 bear | out (clean 33, ADX 28, RVol 0.4) |
| 4 | **META** | 621.93 | - | **-** | 22 | - | NEG -$26.1M | 626.18 | 650 | 610 | -$16.7M | +$243k bull / -$86k bear | out (clean 28, ADX 26, RVol 0.4) |
| 5 | **AMZN** | 251.38 | - | **-** | 22 | - | POS +$182.2M | - | 250 | 250 | -$4.0M | +$231k bull / -$503k bear | out (clean 33, ADX 40, RVol 0.9) |
| 6 | **NFLX** | 63.05 | - | **-** | 21 | - | NEG -$7.4M | 64.33 | 63 | 60 | -$502k | +$0 bull / -$50k bear | out (clean 28, ADX 33, RVol 0.6) |
| 7 | **MSTR** | 135.96 | - | **-** | 18 | - | POS +$83.3M | - | 135 | 125 | -$4.3M | +$153k bull / +$0 bear | out (clean 29, ADX 14, RVol 0.2) |
| 8 | **SHOP** | 147.39 | - | **-** | 18 | - | NEG -$3.9M | - | 145 | 148 | -$4.3M | - | out (clean 33, ADX 14, RVol 1.0) |
| 9 | **SPY** | 756.44 | - | **-** | 17 | - | NEG -$8.2B | 770.38 | 770 | 750 | -$74.5M | +$672k bull / -$624k bear | out (clean 29, ADX 20, RVol 0.5) |
| 10 | **IWM** | 281.05 | - | **-** | 17 | - | NEG -$1.1B | 286.89 | 285 | 270 | -$4.8M | +$311k bull / -$199k bear | out (clean 32, ADX 17, RVol 0.7) |
| 11 | **SMH** | 519.51 | - | **-** | 16 | - | NEG -$279.4M | - | 532.5 | 500 | +$1.2M | +$25k bull / +$0 bear | out (clean 31, ADX 12, RVol 0.5) |
| 12 | **NVDA** | 207.79 | - | **-** | 16 | - | POS +$106.7M | 203.88 | 210 | 200 | +$10.9M | +$331k bull / +$0 bear | out (clean 29, ADX 13, RVol 0.5) |
| 13 | **GOOGL** | 279.59 | - | **-** | 16 | - | NEG -$36.8M | 284.87 | 285 | 290 | +$2.4M | +$213k bull / +$0 bear | out (clean 33, ADX 15, RVol 0.2) |
| 14 | **PLTR** | 176.15 | - | **-** | 16 | - | NEG -$24.9M | - | 165 | 180 | -$1.8M | +$0 bull / -$187k bear | out (clean 27, ADX 22, RVol 0.4) |
| 15 | **ARM** | 202.12 | - | **-** | 15 | - | NEG -$6.5M | - | 220 | 200 | -$138k | +$29k bull / +$0 bear | out (clean 25, ADX 11, RVol 0.4) |
| 16 | **QQQ** | 687.43 | - | **-** | 14 | - | NEG -$5.0B | - | 700 | 680 | -$10.0M | +$2.2M bull / -$106k bear | out (clean 29, ADX 15, RVol 0.3) |
| 17 | **AAPL** | 332.04 | - | **-** | 14 | - | NEG -$380.8M | 342.4 | 350 | 330 | -$8.4M | +$58k bull / -$65k bear | out (clean 30, ADX 11, RVol 0.5) |
| 18 | **AMD** | 490.68 | - | **-** | 14 | - | NEG -$68.0M | - | 520 | 500 | +$3.7M | +$1.0M bull / +$0 bear | out (clean 31, ADX 13, RVol 0.5) |
| 19 | **MU** | 854.00 | - | **-** | 14 | - | NEG -$204.5M | - | 900 | 850 | -$19.1M | +$315k bull / -$2.1M bear | out (clean 31, ADX 12, RVol 0.5) |
| 20 | **HOOD** | 85.25 | - | **-** | 13 | - | NEG -$2.8M | - | 90 | 85 | -$54k | +$0 bull / -$34k bear | out (clean 30, ADX 11, RVol 0.5) |
| 21 | **BABA** | 100.45 | - | **-** | 13 | - | POS +$1.9M | 99.84 | 102 | 100 | +$245k | - | out (clean 36, ADX 28, RVol 0.5) |
| 22 | **CRM** | 222.98 | - | **-** | 12 | - | NEG -$13.8M | - | 240 | 220 | -$366k | - | out (clean 29, ADX 15, RVol 1.1) |
| 23 | **COIN** | 146.38 | - | **-** | 11 | - | POS +$20.9M | - | 148 | 150 | -$2.3M | - | out (clean 30, ADX 29, RVol 0.2) |
| 24 | **UBER** | 66.80 | - | **-** | 9 | - | NEG -$8.7M | - | 70 | 65 | -$320k | - | out (clean 29, ADX 13, RVol 0.5) |
| 25 | **AVGO** | 333.07 | - | **-** | 8 | - | NEG -$63.1M | - | 340 | 340 | +$2.9M | - | out (clean 31, ADX 13, RVol 0.3) |
| 26 | **SMCI** | 31.55 | - | **-** | 7 | - | POS +$2.0M | - | 34.5 | 30 | -$364k | - | out (clean 33, ADX 13, RVol 1.5) |
| 27 | **DELL** | 408.31 | - | **-** | 4 | - | NEG -$26.0M | - | 440 | 400 | +$712k | - | out (clean 32, ADX 11, RVol 0.2) |

## Big prints this scan (29)
- **ORCL** CALL 130 2026-11-06 (3DTE): 549 @ 2.45 = **+$135k** BUY | vol 33,035 / OI 3,741
- **TSLA** CALL 410 2026-11-04 (1DTE): 500 @ 1.85 = **+$92k** SELL | vol 25,520 / OI 1,873
- **META** CALL 620 2026-11-04 (1DTE): 100 @ 9.25 = **+$92k** BUY | vol 10,273 / OI 383
- **AAPL** PUT 340 2026-11-04 (1DTE): 100 @ 8.64 = **+$86k** MID | vol 4,794 / OI 7,977
- **AMZN** PUT 250 2026-11-06 (3DTE): 231 @ 3.50 = **+$81k** BUY | vol 1,842 / OI 4,023
- **META** CALL 635 2026-11-06 (3DTE): 111 @ 6.70 = **+$74k** MID | vol 1,498 / OI 1,669
- **AAPL** PUT 330 2026-11-04 (1DTE): 300 @ 2.18 = **+$65k** BUY | vol 48,869 / OI 5,416
- **MU** PUT 840 2026-11-06 (3DTE): 30 @ 19.50 = **+$58k** SELL | vol 857 / OI 1,144
- **META** PUT 630 2026-11-09 (6DTE): 30 @ 16.80 = **+$50k** SELL | vol 52 / OI 375
- **ORCL** CALL 130 2026-11-06 (3DTE): 200 @ 2.45 = **+$49k** BUY | vol 33,035 / OI 3,741
- **AMD** CALL 477.5 2026-11-06 (3DTE): 16 @ 30.50 = **+$49k** BUY | vol 127 / OI 39
- **MU** PUT 850 2026-11-06 (3DTE): 20 @ 24.27 = **+$49k** BUY | vol 3,014 / OI 1,813
- **MU** CALL 860 2026-11-09 (6DTE): 19 @ 25.40 = **+$48k** SELL | vol 614 / OI 2
- **AMD** CALL 497.5 2026-11-04 (1DTE): 27 @ 17.00 = **+$46k** BUY | vol 692 / OI 47
- **AMZN** PUT 250 2026-11-06 (3DTE): 113 @ 3.50 = **+$40k** BUY | vol 1,842 / OI 4,023

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 767 2026-11-09 (6DTE): 790 traded vs OI 0
- **SPY** PUT 757 2026-11-05 (2DTE): 515 traded vs OI 0
- **SPY** PUT 756 2026-11-09 (6DTE): 505 traded vs OI 0
- **SPY** PUT 700 2026-11-17 (14DTE): 914 traded vs OI 0
- **QQQ** CALL 693 2026-11-06 (3DTE): 512 traded vs OI 435
- **QQQ** CALL 695 2026-11-06 (3DTE): 2,375 traded vs OI 2,363
- **QQQ** PUT 635 2026-11-04 (1DTE): 2,131 traded vs OI 1,917
- **IWM** PUT 277 2026-11-10 (7DTE): 532 traded vs OI 171
- **SMH** CALL 532.5 2026-11-04 (1DTE): 650 traded vs OI 619
- **NVDA** CALL 215 2026-11-13 (10DTE): 6,627 traded vs OI 6,625
- **AAPL** CALL 357.5 2026-11-13 (10DTE): 550 traded vs OI 113
- **META** PUT 560 2026-11-13 (10DTE): 1,273 traded vs OI 1,124
- **AMZN** CALL 257.5 2026-11-06 (3DTE): 1,456 traded vs OI 1,450
- **AMZN** PUT 255 2026-11-04 (1DTE): 599 traded vs OI 174
- **MSFT** PUT 480 2026-11-04 (1DTE): 598 traded vs OI 151

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
