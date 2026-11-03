# GEX + FLOW SCAN - Tue Nov 03, 01:30 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 13:30:08 ET, last candle SPY 13:29, QQQ 13:29 | no errors

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **ORCL** | 126.85 | - | **-** | 27 | - | NEG -$38.2M | - | 135 | 125 | -$9.7M | +$648k bull / +$0 bear | out (clean 33, ADX 38, RVol 0.7) |
| 2 | **META** | 623.67 | - | **-** | 25 | - | NEG -$14.2M | 625.69 | 650 | 610 | -$18.8M | +$117k bull / -$179k bear | out (clean 28, ADX 34, RVol 0.4) |
| 3 | **AMZN** | 250.81 | - | **-** | 20 | - | POS +$177.8M | - | 250 | 250 | -$2.8M | +$0 bull / -$220k bear | out (clean 33, ADX 33, RVol 0.6) |
| 4 | **MSTR** | 136.00 | - | **-** | 20 | - | POS +$81.5M | - | 135 | 125 | -$4.8M | +$30k bull / +$0 bear | out (clean 29, ADX 16, RVol 0.2) |
| 5 | **MSFT** | 519.99 | - | **-** | 19 | - | POS +$238.7M | 502.36 | 540 | 500 | -$11.2M | - | out (clean 28, ADX 43, RVol 0.7) |
| 6 | **SHOP** | 148.62 | - | **-** | 19 | - | NEG -$3.6M | - | 150 | 150 | -$4.4M | - | out (clean 33, ADX 15, RVol 0.8) |
| 7 | **TSLA** | 398.35 | - | **-** | 18 | - | POS +$199.7M | - | 400 | 400 | +$16.0M | +$448k bull / -$148k bear | out (clean 31, ADX 28, RVol 0.5) |
| 8 | **AVGO** | 332.30 | - | **-** | 18 | - | NEG -$64.4M | - | 340 | 340 | +$3.2M | +$185k bull / +$0 bear | out (clean 31, ADX 14, RVol 0.4) |
| 9 | **SMCI** | 31.68 | - | **-** | 17 | - | POS +$2.1M | - | 34.5 | 30 | -$540k | +$82k bull / +$0 bear | out (clean 33, ADX 13, RVol 1.0) |
| 10 | **BABA** | 100.29 | - | **-** | 17 | - | POS +$1.1M | 99.91 | 102 | 100 | +$294k | - | out (clean 36, ADX 38, RVol 0.5) |
| 11 | **SPY** | 756.35 | - | **-** | 16 | - | NEG -$8.5B | 770.52 | 770 | 750 | -$68.0M | +$968k bull / -$132k bear | out (clean 29, ADX 17, RVol 0.5) |
| 12 | **NVDA** | 208.08 | - | **-** | 16 | - | POS +$116.8M | 203.72 | 210 | 200 | +$9.4M | +$272k bull / +$0 bear | out (clean 29, ADX 15, RVol 0.5) |
| 13 | **AAPL** | 332.17 | - | **-** | 15 | - | NEG -$388.7M | 343.47 | 350 | 330 | -$8.0M | +$0 bull / -$121k bear | out (clean 30, ADX 13, RVol 0.7) |
| 14 | **AMD** | 492.78 | - | **-** | 15 | - | NEG -$65.3M | - | 520 | 500 | +$2.4M | +$159k bull / -$98k bear | out (clean 31, ADX 15, RVol 0.6) |
| 15 | **PLTR** | 175.35 | - | **-** | 15 | - | NEG -$24.7M | - | 165 | 180 | -$756k | +$325k bull / +$0 bear | out (clean 27, ADX 16, RVol 0.9) |
| 16 | **QQQ** | 687.16 | - | **-** | 14 | - | NEG -$4.9B | - | 700 | 680 | -$10.6M | +$468k bull / +$0 bear | out (clean 29, ADX 15, RVol 0.6) |
| 17 | **MU** | 851.99 | - | **-** | 14 | - | NEG -$203.5M | - | 900 | 850 | -$12.2M | +$2.0M bull / +$0 bear | out (clean 31, ADX 11, RVol 0.4) |
| 18 | **COIN** | 146.51 | - | **-** | 12 | - | POS +$20.7M | - | 148 | 150 | -$2.3M | - | out (clean 29, ADX 32, RVol 0.3) |
| 19 | **CRM** | 222.81 | - | **-** | 12 | - | NEG -$14.0M | - | 240 | 220 | -$365k | - | out (clean 30, ADX 15, RVol 0.8) |
| 20 | **NFLX** | 62.78 | - | **-** | 10 | - | NEG -$9.6M | 64.34 | 63 | 60 | -$454k | - | out (clean 27, ADX 27, RVol 0.6) |
| 21 | **GOOGL** | 280.51 | - | **-** | 6 | - | NEG -$28.3M | 284.68 | 285 | 290 | +$1.7M | - | out (clean 33, ADX 20, RVol 0.2) |
| 22 | **DELL** | 408.66 | - | **-** | 6 | - | NEG -$25.7M | - | 440 | 400 | +$1.0M | - | out (clean 32, ADX 11, RVol 0.3) |
| 23 | **ARM** | 202.88 | - | **-** | 6 | - | NEG -$6.6M | - | 220 | 200 | -$172k | - | out (clean 25, ADX 12, RVol 0.4) |
| 24 | **UBER** | 66.61 | - | **-** | 6 | - | NEG -$13.5M | - | 70 | 65 | +$61k | - | out (clean 29, ADX 17, RVol 0.6) |
| 25 | **IWM** | 281.16 | - | **-** | 5 | - | NEG -$1.0B | 286.86 | 285 | 270 | -$2.7M | - | out (clean 32, ADX 17, RVol 0.2) |
| 26 | **SMH** | 520.00 | - | **-** | 5 | - | NEG -$284.4M | - | 532.5 | 500 | +$960k | - | out (clean 31, ADX 14, RVol 0.2) |
| 27 | **HOOD** | 85.13 | - | **-** | 3 | - | NEG -$2.7M | - | 90 | 90 | -$171k | - | out (clean 31, ADX 10, RVol 0.3) |

## Big prints this scan (67)
- **ORCL** CALL 133 2026-11-06 (3DTE): 1,228 @ 1.79 = **+$220k** BUY | vol 5,562 / OI 1,002
- **ORCL** CALL 133 2026-11-06 (3DTE): 1,227 @ 1.79 = **+$220k** BUY | vol 5,562 / OI 1,002
- **SPY** CALL 760 2026-11-04 (1DTE): 538 @ 2.83 = **+$152k** BUY | vol 21,461 / OI 2,273
- **SPY** CALL 760 2026-11-04 (1DTE): 538 @ 2.83 = **+$152k** BUY | vol 21,461 / OI 2,273
- **SPY** CALL 760 2026-11-04 (1DTE): 499 @ 2.82 = **+$141k** BUY | vol 21,461 / OI 2,273
- **SPY** CALL 763 2026-11-05 (2DTE): 538 @ 2.50 = **+$134k** BUY | vol 2,218 / OI 0
- **SPY** CALL 763 2026-11-05 (2DTE): 538 @ 2.50 = **+$134k** BUY | vol 2,218 / OI 0
- **SPY** CALL 756 2026-11-03 (0DTE): 861 @ 1.50 = **+$129k** BUY | vol 353,750 / OI 3,833
- **SPY** CALL 763 2026-11-05 (2DTE): 499 @ 2.50 = **+$125k** BUY | vol 2,218 / OI 0
- **QQQ** PUT 692 2026-11-03 (0DTE): 300 @ 4.14 = **+$124k** SELL | vol 2,145 / OI 456
- **META** PUT 620 2026-11-06 (3DTE): 100 @ 10.00 = **+$100k** MID | vol 1,490 / OI 1,386
- **MU** CALL 860 2026-11-09 (6DTE): 24 @ 27.05 = **+$65k** BUY | vol 574 / OI 2
- **ORCL** CALL 133 2026-11-06 (3DTE): 334 @ 1.79 = **+$60k** BUY | vol 5,562 / OI 1,002
- **MU** CALL 850 2026-11-06 (3DTE): 19 @ 28.85 = **+$55k** BUY | vol 1,913 / OI 341
- **MU** CALL 850 2026-11-06 (3DTE): 19 @ 28.85 = **+$55k** BUY | vol 1,913 / OI 341

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 761 2026-11-05 (2DTE): 518 traded vs OI 0
- **QQQ** CALL 700 2026-11-05 (2DTE): 2,467 traded vs OI 2,418
- **QQQ** CALL 706 2026-11-05 (2DTE): 520 traded vs OI 0
- **QQQ** PUT 696 2026-11-03 (0DTE): 522 traded vs OI 253
- **QQQ** CALL 731 2026-11-06 (3DTE): 1,392 traded vs OI 393
- **QQQ** PUT 676 2026-11-04 (1DTE): 1,228 traded vs OI 1,213
- **NVDA** CALL 220 2026-11-18 (15DTE): 620 traded vs OI 0
- **AAPL** CALL 350 2026-11-11 (8DTE): 501 traded vs OI 108
- **META** PUT 620 2026-11-06 (3DTE): 1,490 traded vs OI 1,386
- **META** CALL 677.5 2026-11-06 (3DTE): 578 traded vs OI 0
- **AVGO** PUT 327.5 2026-11-04 (1DTE): 521 traded vs OI 181
- **ORCL** PUT 119 2026-11-06 (3DTE): 969 traded vs OI 853
- **ORCL** PUT 128 2026-11-13 (10DTE): 752 traded vs OI 341

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
