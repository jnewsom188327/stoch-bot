# GEX + FLOW SCAN - Fri Nov 13, 09:40 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 09:40:08 ET, last candle SPY 09:39, QQQ 09:39 | no errors

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **UBER** | 70.00 | PINNED between the walls (positive gamma) - chop | **-** | 49 | - | POS +$18.6M | 68.86 | 70 | 70 | +$0 | - | LONG (clean 33, ADX 30, RVol 2.8) |
| 2 | **HOOD** | 79.20 | TREND (flow not with it) | **PUTS** | 43 | 11/13 78P @ 0.57 (delta 0.31) = est +35% at 78.04 | NEG -$6.5M | 80.18 | 81 | 80 | +$0 | - | SHORT (clean 35, ADX 41, RVol 4.2) |
| 3 | **MSFT** | 518.86 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 37 | none: 164 calls 0-7DTE > 13 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (101 contracts' greeks worked out here) | POS +$12.8M | 518.94 | 535 | 520 | +$0 | - | out (clean 33, ADX 46, RVol 2.1) |
| 4 | **AAPL** | 359.78 | PINNED between the walls (positive gamma) - chop | **-** | 32 | - | POS +$1.3B | 346.7 | 360 | 360 | +$0 | - | out (clean 30, ADX 34, RVol 2.3) |
| 5 | **ORCL** | 125.08 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 31 | 11/13 127C @ 0.61 (delta 0.28) = est +31% at 126.37 | POS +$9.0M | 122.67 | 130 | 125 | +$0 | - | out (clean 31, ADX 22, RVol 1.7) |
| 6 | **PLTR** | 170.38 | PINNED between the walls (positive gamma) - chop | **-** | 28 | - | POS +$98.2M | 162.43 | 170 | 170 | +$0 | - | out (clean 29, ADX 23, RVol 2.0) |
| 7 | **TSLA** | 392.33 | - | **-** | 22 | - | POS +$402.5M | - | 400 | 380 | +$0 | +$189k bull / +$0 bear | out (clean 30, ADX 40, RVol 4.8) |
| 8 | **AMD** | 559.14 | - | **-** | 17 | - | POS +$212.7M | - | 550 | 550 | +$0 | +$48k bull / +$0 bear | out (clean 34, ADX 21, RVol 1.8) |
| 9 | **NVDA** | 164.02 | - | **-** | 16 | - | NEG -$242.2M | - | 175 | 160 | +$0 | +$36k bull / +$0 bear | out (clean 31, ADX 16, RVol 1.6) |
| 10 | **IWM** | 277.85 | - | **-** | 13 | - | NEG -$2.0B | 282.9 | 285 | 275 | +$0 | - | out (clean 34, ADX 45, RVol 3.3) |
| 11 | **NFLX** | 63.21 | - | **-** | 13 | - | NEG -$16.6M | 63.96 | 65 | 60 | +$0 | - | out (clean 31, ADX 52, RVol 3.0) |
| 12 | **QQQ** | 685.29 | - | **-** | 11 | - | NEG -$1.8B | 691.39 | 700 | 680 | +$0 | - | out (clean 31, ADX 34, RVol 2.6) |
| 13 | **AMZN** | 268.85 | - | **-** | 11 | - | POS +$552.3M | - | 270 | 270 | +$0 | - | out (clean 30, ADX 36, RVol 2.3) |
| 14 | **COIN** | 129.71 | - | **-** | 11 | - | NEG -$13.4M | 132.47 | 137 | 130 | +$0 | - | out (clean 30, ADX 36, RVol 2.7) |
| 15 | **SPY** | 756.93 | - | **-** | 10 | - | NEG -$5.3B | 762.11 | 775 | 760 | +$0 | - | out (clean 32, ADX 35, RVol 2.0) |
| 16 | **GOOGL** | 303.58 | - | **-** | 10 | - | POS +$221.7M | 289.04 | 300 | 290 | +$0 | - | out (clean 30, ADX 31, RVol 3.3) |
| 17 | **MSTR** | 111.43 | - | **-** | 10 | - | NEG -$36.4M | - | 120 | 110 | +$0 | - | out (clean 29, ADX 28, RVol 3.7) |
| 18 | **CRM** | 216.79 | - | **-** | 10 | - | NEG -$8.2M | 221.52 | 220 | 220 | +$0 | - | out (clean 30, ADX 26, RVol 3.0) |
| 19 | **META** | 631.88 | - | **-** | 9 | - | NEG -$1.8M | 632.33 | 650 | 635 | +$0 | - | out (clean 29, ADX 33, RVol 1.7) |
| 20 | **SMCI** | 27.01 | - | **-** | 9 | - | NEG -$1.8M | - | 28 | 27 | +$0 | - | out (clean 34, ADX 20, RVol 3.0) |
| 21 | **SHOP** | 148.89 | - | **-** | 9 | - | POS +$4.2M | 145.47 | 150 | 150 | +$0 | - | out (clean 31, ADX 28, RVol 1.8) |
| 22 | **BABA** | 94.14 | - | **-** | 9 | - | NEG -$19.8M | - | 100 | 95 | +$0 | - | out (clean 28, ADX 21, RVol 5.8) |
| 23 | **AVGO** | 352.55 | - | **-** | 8 | - | POS +$126.5M | - | 350 | 350 | +$0 | - | out (clean 34, ADX 20, RVol 2.8) |
| 24 | **ARM** | 195.94 | - | **-** | 8 | - | POS +$10.0M | 189.68 | 200 | 200 | +$0 | - | out (clean 32, ADX 28, RVol 1.4) |
| 25 | **SMH** | 495.09 | - | **-** | 7 | - | NEG -$193.0M | 520.31 | 500 | 475 | +$0 | - | out (clean 30, ADX 27, RVol 1.2) |
| 26 | **DELL** | 367.20 | - | **-** | 7 | - | NEG -$4.6M | 372.79 | 360 | 360 | +$0 | - | out (clean 37, ADX 21, RVol 1.5) |
| 27 | **MU** | 784.13 | - | **-** | 6 | - | POS +$23.1M | 776 | 800 | 800 | +$0 | - | out (clean 30, ADX 14, RVol 1.9) |

## Big prints this scan (5)
- **TSLA** CALL 400 2026-11-13 (0DTE): 100 @ 5.75 = **+$58k** BUY | vol 0 / OI 19,668
- **TSLA** CALL 402.5 2026-11-13 (0DTE): 96 @ 4.25 = **+$41k** BUY | vol 0 / OI 2,738
- **NVDA** CALL 165 2026-11-18 (5DTE): 33 @ 10.90 = **+$36k** BUY | vol 0 / OI 504
- **TSLA** CALL 405 2026-11-13 (0DTE): 98 @ 3.10 = **+$30k** BUY | vol 0 / OI 7,876
- **TSLA** CALL 405 2026-11-13 (0DTE): 100 @ 3.00 = **+$30k** BUY | vol 0 / OI 7,876

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
