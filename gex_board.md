# GEX + FLOW SCAN - Fri Nov 06, 09:40 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 09:40:08 ET, last candle SPY 09:39, QQQ 09:39 | no errors

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **GOOGL** | 290.37 | PINNED between the walls (positive gamma) - chop | **-** | 34 | - | POS +$73.8M | 284.35 | 290 | 290 | +$0 | - | out (clean 34, ADX 21, RVol 3.1) |
| 2 | **MSTR** | 128.60 | FLIP CROSS up into positive gamma | **CALLS** | 34 | 11/06 134C @ 0.72 (delta 0.21) = est +82% at 131.76 | POS +$18.8M | 125.91 | 135 | 125 | +$0 | - | out (clean 33, ADX 21, RVol 3.0) |
| 3 | **COIN** | 136.67 | FLIP CROSS up into positive gamma | **CALLS** | 25 | none: 55 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (48 contracts' greeks worked out here) | POS +$1.7M | 136.31 | 142 | 135 | +$0 | - | out (clean 32, ADX 23, RVol 1.6) |
| 4 | **SPY** | 737.73 | - | **-** | 19 | - | NEG -$13.7B | 769.9 | 770 | 740 | +$0 | +$0 bull / -$156k bear | out (clean 36, ADX 23, RVol 4.1) |
| 5 | **AMD** | 451.47 | - | **-** | 19 | - | NEG -$152.7M | - | 430 | 450 | +$0 | +$28k bull / -$30k bear | out (clean 32, ADX 21, RVol 3.5) |
| 6 | **TSLA** | 351.13 | - | **-** | 18 | - | NEG -$188.4M | - | 370 | 350 | +$0 | +$25k bull / +$0 bear | out (clean 34, ADX 19, RVol 4.2) |
| 7 | **NFLX** | 63.82 | - | **-** | 10 | - | POS +$8.2M | 63.06 | 63 | 65 | +$0 | - | out (clean 32, ADX 27, RVol 2.4) |
| 8 | **DELL** | 346.23 | - | **-** | 10 | - | NEG -$23.5M | - | 370 | 350 | +$0 | - | out (clean 33, ADX 27, RVol 4.0) |
| 9 | **QQQ** | 660.01 | - | **-** | 9 | - | NEG -$5.4B | - | 700 | 675 | +$0 | - | out (clean 35, ADX 20, RVol 5.3) |
| 10 | **SMH** | 471.27 | - | **-** | 9 | - | NEG -$525.0M | - | 505 | 500 | +$0 | - | out (clean 34, ADX 21, RVol 4.4) |
| 11 | **NVDA** | 193.13 | - | **-** | 9 | - | NEG -$352.6M | - | 210 | 190 | +$0 | - | out (clean 34, ADX 22, RVol 3.4) |
| 12 | **AAPL** | 339.45 | - | **-** | 9 | - | NEG -$109.4M | 341.15 | 350 | 340 | +$0 | - | out (clean 30, ADX 22, RVol 3.3) |
| 13 | **MSFT** | 531.51 | - | **-** | 9 | - | POS +$553.4M | 508.46 | 540 | 535 | +$0 | - | out (clean 32, ADX 25, RVol 2.9) |
| 14 | **AVGO** | 304.64 | - | **-** | 9 | - | NEG -$149.6M | - | 330 | 300 | +$0 | - | out (clean 32, ADX 25, RVol 5.0) |
| 15 | **MU** | 707.00 | - | **-** | 9 | - | NEG -$184.9M | - | 700 | 700 | +$0 | - | out (clean 32, ADX 20, RVol 4.5) |
| 16 | **HOOD** | 79.55 | - | **-** | 9 | - | NEG -$16.0M | 83.7 | 85 | 80 | +$0 | - | out (clean 30, ADX 22, RVol 3.1) |
| 17 | **BABA** | 108.26 | - | **-** | 9 | - | POS +$25.2M | 102.15 | 110 | 110 | +$0 | - | out (clean 35, ADX 22, RVol 3.8) |
| 18 | **IWM** | 271.89 | - | **-** | 8 | - | NEG -$3.1B | 285.99 | 285 | 270 | +$0 | - | out (clean 36, ADX 17, RVol 3.9) |
| 19 | **META** | 621.80 | - | **-** | 8 | - | NEG -$3.1M | 621.83 | 650 | 610 | +$0 | - | out (clean 33, ADX 16, RVol 2.9) |
| 20 | **PLTR** | 160.04 | - | **-** | 8 | - | NEG -$55.0M | - | 165 | 160 | +$0 | - | out (clean 27, ADX 19, RVol 3.2) |
| 21 | **SMCI** | 29.00 | - | **-** | 8 | - | NEG -$3.9M | - | 30 | 30 | +$0 | - | out (clean 34, ADX 22, RVol 2.0) |
| 22 | **ARM** | 174.31 | - | **-** | 8 | - | NEG -$20.3M | - | 190 | 170 | +$0 | - | out (clean 26, ADX 15, RVol 4.3) |
| 23 | **UBER** | 69.53 | - | **-** | 8 | - | POS +$9.4M | 68.82 | 70 | 70 | +$0 | - | out (clean 29, ADX 17, RVol 3.0) |
| 24 | **CRM** | 217.38 | - | **-** | 8 | - | NEG -$22.2M | - | 230 | 220 | +$0 | - | out (clean 33, ADX 19, RVol 4.2) |
| 25 | **SHOP** | 146.33 | - | **-** | 7 | - | NEG -$4.0M | 150.73 | 144 | 145 | +$0 | - | out (clean 37, ADX 16, RVol 2.3) |
| 26 | **AMZN** | 263.22 | - | **-** | 6 | - | POS +$362.2M | - | 265 | 260 | +$0 | - | out (clean 34, ADX 16, RVol 1.6) |
| 27 | **ORCL** | 118.96 | - | **-** | 5 | - | NEG -$68.5M | - | 125 | 120 | +$0 | - | out (clean 31, ADX 15, RVol 1.4) |

## Big prints this scan (3)
- **SPY** CALL 735 2026-11-10 (4DTE): 200 @ 7.79 = **+$156k** SELL | vol 0 / OI 14
- **AMD** CALL 465 2026-11-06 (0DTE): 150 @ 2.00 = **+$30k** SELL | vol 0 / OI 81
- **TSLA** CALL 365 2026-11-06 (0DTE): 250 @ 1.00 = **+$25k** BUY | vol 0 / OI 382

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
