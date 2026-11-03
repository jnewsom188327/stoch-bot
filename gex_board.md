# GEX + FLOW SCAN - Tue Nov 03, 12:40 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 12:40:08 ET, last candle SPY 12:39, QQQ 12:39 | no errors

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **BABA** | 100.05 | FLIP CROSS down into negative gamma | **PUTS** | 31 | none: 20 puts 0-7DTE > 2 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only +1% at the target (needs +20%) | NEG -$68k | 100.05 | 102 | 100 | +$269k | - | out (clean 36, ADX 53, RVol 0.5) |
| 2 | **META** | 622.34 | - | **-** | 27 | - | NEG -$17.5M | 625.41 | 650 | 610 | -$19.0M | +$93k bull / +$0 bear | out (clean 28, ADX 45, RVol 0.3) |
| 3 | **ORCL** | 126.82 | - | **-** | 26 | - | NEG -$38.3M | - | 135 | 125 | -$8.0M | +$0 bull / -$1.5M bear | out (clean 33, ADX 35, RVol 0.5) |
| 4 | **SHOP** | 147.95 | - | **-** | 21 | - | NEG -$3.5M | - | 145 | 150 | -$4.4M | - | out (clean 32, ADX 19, RVol 1.1) |
| 5 | **TSLA** | 397.38 | - | **-** | 20 | - | POS +$190.2M | - | 400 | 400 | +$16.9M | +$1.3M bull / -$565k bear | out (clean 31, ADX 38, RVol 0.4) |
| 6 | **COIN** | 148.77 | - | **-** | 20 | - | POS +$20.2M | - | 148 | 150 | -$3.9M | - | out (clean 28, ADX 44, RVol 0.2) |
| 7 | **SMCI** | 31.55 | - | **-** | 18 | - | POS +$1.9M | - | 34.5 | 30 | -$723k | +$0 bull / -$47k bear | out (clean 33, ADX 18, RVol 0.7) |
| 8 | **ARM** | 203.27 | - | **-** | 18 | - | NEG -$6.7M | - | 220 | 200 | -$248k | +$39k bull / +$0 bear | out (clean 25, ADX 16, RVol 0.4) |
| 9 | **NVDA** | 208.30 | - | **-** | 17 | - | POS +$117.8M | 203.6 | 210 | 200 | +$7.9M | +$412k bull / -$38k bear | out (clean 29, ADX 20, RVol 0.6) |
| 10 | **IWM** | 280.47 | - | **-** | 16 | - | NEG -$1.2B | 287.02 | 285 | 270 | -$2.0M | +$139k bull / +$0 bear | out (clean 32, ADX 20, RVol 0.7) |
| 11 | **SMH** | 520.60 | - | **-** | 16 | - | NEG -$278.1M | - | 532.5 | 500 | +$737k | +$58k bull / +$0 bear | out (clean 31, ADX 18, RVol 0.6) |
| 12 | **AMD** | 490.74 | - | **-** | 16 | - | NEG -$66.7M | - | 520 | 500 | +$2.1M | +$774k bull / +$0 bear | out (clean 31, ADX 24, RVol 0.5) |
| 13 | **AMZN** | 248.62 | - | **-** | 16 | - | POS +$150.4M | 236.12 | 250 | 250 | -$556k | +$0 bull / -$46k bear | out (clean 32, ADX 19, RVol 0.7) |
| 14 | **MSFT** | 517.85 | - | **-** | 16 | - | POS +$209.8M | 501.09 | 540 | 500 | -$8.2M | - | out (clean 28, ADX 31, RVol 0.5) |
| 15 | **GOOGL** | 280.41 | - | **-** | 16 | - | NEG -$31.8M | 285.38 | 285 | 290 | +$1.6M | +$0 bull / -$170k bear | out (clean 32, ADX 16, RVol 0.4) |
| 16 | **SPY** | 754.81 | - | **-** | 15 | - | NEG -$9.0B | 770.6 | 770 | 750 | -$64.1M | +$258k bull / +$0 bear | out (clean 30, ADX 13, RVol 0.4) |
| 17 | **AAPL** | 331.40 | - | **-** | 15 | - | NEG -$395.4M | 343.26 | 350 | 330 | -$8.0M | +$0 bull / -$85k bear | out (clean 30, ADX 13, RVol 0.4) |
| 18 | **HOOD** | 85.08 | - | **-** | 15 | - | NEG -$2.8M | - | 90 | 90 | -$227k | +$0 bull / -$29k bear | out (clean 31, ADX 17, RVol 0.2) |
| 19 | **PLTR** | 173.68 | - | **-** | 14 | - | NEG -$24.9M | - | 165 | 180 | -$607k | +$312k bull / +$0 bear | out (clean 27, ADX 18, RVol 0.4) |
| 20 | **MU** | 852.71 | - | **-** | 14 | - | NEG -$201.3M | - | 900 | 850 | -$13.3M | +$4.4M bull / +$0 bear | out (clean 31, ADX 12, RVol 0.3) |
| 21 | **MSTR** | 136.25 | - | **-** | 12 | - | POS +$81.5M | - | 135 | 125 | -$4.9M | - | out (clean 29, ADX 26, RVol 0.3) |
| 22 | **CRM** | 222.33 | - | **-** | 11 | - | NEG -$13.9M | - | 240 | 220 | -$369k | - | out (clean 30, ADX 14, RVol 0.4) |
| 23 | **NFLX** | 62.72 | - | **-** | 10 | - | NEG -$9.5M | 64.08 | 63 | 60 | -$515k | - | out (clean 26, ADX 22, RVol 0.4) |
| 24 | **AVGO** | 333.30 | - | **-** | 8 | - | NEG -$62.5M | - | 340 | 340 | +$2.3M | - | out (clean 31, ADX 18, RVol 0.3) |
| 25 | **UBER** | 66.78 | - | **-** | 8 | - | NEG -$8.8M | - | 70 | 65 | -$109k | - | out (clean 29, ADX 12, RVol 0.9) |
| 26 | **DELL** | 406.85 | - | **-** | 6 | - | NEG -$26.0M | - | 440 | 400 | +$996k | - | out (clean 32, ADX 12, RVol 0.4) |
| 27 | **QQQ** | 686.26 | - | **-** | 4 | - | NEG -$5.0B | - | 700 | 680 | -$15.9M | - | out (clean 29, ADX 14, RVol 0.3) |

## Big prints this scan (71)
- **TSLA** PUT 397.5 2026-11-06 (3DTE): 267 @ 9.40 = **+$251k** BUY | vol 2,090 / OI 1,483
- **MU** PUT 855 2026-11-06 (3DTE): 69 @ 25.37 = **+$175k** SELL | vol 1,598 / OI 740
- **SPY** CALL 755 2026-11-03 (0DTE): 1,032 @ 1.38 = **+$142k** BUY | vol 304,340 / OI 1,485
- **SPY** CALL 756 2026-11-05 (2DTE): 229 @ 5.04 = **+$115k** BUY | vol 2,836 / OI 0
- **MU** CALL 870 2026-11-04 (1DTE): 100 @ 11.00 = **+$110k** BUY | vol 9,194 / OI 154
- **AMD** PUT 470 2026-11-04 (1DTE): 100 @ 10.35 = **+$104k** SELL | vol 1,113 / OI 310
- **ORCL** PUT 125 2026-11-06 (3DTE): 330 @ 2.93 = **+$97k** BUY | vol 3,941 / OI 4,669
- **MU** PUT 855 2026-11-06 (3DTE): 37 @ 25.60 = **+$95k** SELL | vol 1,598 / OI 740
- **MU** PUT 860 2026-11-04 (1DTE): 44 @ 20.40 = **+$90k** SELL | vol 8,745 / OI 273
- **MU** PUT 855 2026-11-06 (3DTE): 34 @ 26.30 = **+$89k** SELL | vol 1,598 / OI 740
- **AAPL** CALL 325 2026-11-06 (3DTE): 100 @ 8.50 = **+$85k** SELL | vol 1,335 / OI 419
- **IWM** PUT 285 2026-11-04 (1DTE): 168 @ 4.87 = **+$82k** SELL | vol 415 / OI 112
- **MU** PUT 830 2026-11-04 (1DTE): 98 @ 8.30 = **+$81k** SELL | vol 5,774 / OI 430
- **PLTR** PUT 180 2026-11-06 (3DTE): 100 @ 8.05 = **+$80k** SELL | vol 3,377 / OI 3,397
- **MU** PUT 855 2026-11-06 (3DTE): 28 @ 25.50 = **+$71k** SELL | vol 1,598 / OI 740

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 767 2026-11-10 (7DTE): 526 traded vs OI 0
- **IWM** PUT 267 2026-11-04 (1DTE): 523 traded vs OI 228
- **IWM** PUT 266 2026-11-04 (1DTE): 622 traded vs OI 539
- **MSFT** PUT 517.5 2026-11-04 (1DTE): 506 traded vs OI 165
- **HOOD** CALL 78 2026-11-06 (3DTE): 501 traded vs OI 31

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
