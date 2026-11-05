# GEX + FLOW SCAN - Thu Nov 05, 09:35 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **BABA** | 108.52 | TREND (flow not with it) | **CALLS** | 42 | 11/06 111C @ 0.66 (delta 0.26) = est +48% at 110 | POS +$23.1M | - | 110 | 110 | +$0 | - | LONG (clean 37, ADX 36, RVol 4.9) |
| 2 | **UBER** | 69.91 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 40 | 11/06 69P @ 0.69 (delta 0.36) = est +32% at 69.09 | POS +$11.7M | 68.02 | 70 | 65 | +$0 | - | out (clean 31, ADX 27, RVol 3.5) |
| 3 | **SMCI** | 28.14 | TREND (flow not with it) | **PUTS** | 39 | 11/06 28P @ 0.71 (delta 0.42) = est +25% at 27.51 | NEG -$4.4M | - | 30 | 30 | +$0 | - | SHORT (clean 33, ADX 26, RVol 3.6) |
| 4 | **SHOP** | 146.68 | TREND (flow not with it) | **PUTS** | 39 | none: 22 puts 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (3 contracts' greeks worked out here) | NEG -$2.7M | 153.27 | 144 | 145 | +$0 | - | SHORT (clean 34, ADX 30, RVol 2.8) |
| 5 | **AMD** | 441.66 | - | **-** | 18 | - | NEG -$145.7M | - | 430 | 440 | +$0 | +$26k bull / +$0 bear | out (clean 31, ADX 17, RVol 2.6) |
| 6 | **NVDA** | 193.63 | - | **-** | 12 | - | NEG -$304.3M | - | 210 | 200 | +$0 | - | out (clean 30, ADX 37, RVol 4.2) |
| 7 | **NFLX** | 66.65 | - | **-** | 12 | - | POS +$35.9M | - | 65 | 65 | +$0 | - | out (clean 33, ADX 37, RVol 3.7) |
| 8 | **MSTR** | 138.73 | - | **-** | 12 | - | POS +$143.6M | - | 135 | 135 | +$0 | - | out (clean 32, ADX 37, RVol 2.6) |
| 9 | **MU** | 748.67 | - | **-** | 11 | - | NEG -$229.7M | - | 800 | 800 | +$0 | - | out (clean 31, ADX 34, RVol 3.7) |
| 10 | **ARM** | 174.83 | - | **-** | 11 | - | NEG -$9.5M | - | 180 | 180 | +$0 | - | out (clean 26, ADX 32, RVol 5.9) |
| 11 | **TSLA** | 365.22 | - | **-** | 10 | - | NEG -$166.2M | - | 400 | 380 | +$0 | - | out (clean 32, ADX 29, RVol 3.3) |
| 12 | **AVGO** | 311.79 | - | **-** | 10 | - | NEG -$144.4M | - | 340 | 300 | +$0 | - | out (clean 30, ADX 29, RVol 3.7) |
| 13 | **ORCL** | 120.86 | - | **-** | 10 | - | NEG -$48.9M | - | 130 | 120 | +$0 | - | out (clean 33, ADX 30, RVol 2.4) |
| 14 | **QQQ** | 677.76 | - | **-** | 9 | - | NEG -$6.7B | 715.23 | 700 | 680 | +$0 | - | out (clean 33, ADX 20, RVol 2.7) |
| 15 | **SMH** | 479.05 | - | **-** | 9 | - | NEG -$526.8M | - | 520 | 500 | +$0 | - | out (clean 33, ADX 22, RVol 2.9) |
| 16 | **AAPL** | 352.61 | - | **-** | 9 | - | POS +$844.9M | 335.33 | 350 | 340 | +$0 | - | out (clean 32, ADX 23, RVol 3.7) |
| 17 | **MSFT** | 553.04 | - | **-** | 9 | - | POS +$1.1B | - | 550 | 535 | +$0 | - | out (clean 29, ADX 22, RVol 2.8) |
| 18 | **DELL** | 346.90 | - | **-** | 9 | - | NEG -$22.8M | - | 360 | 350 | +$0 | - | out (clean 33, ADX 22, RVol 4.2) |
| 19 | **SPY** | 762.28 | - | **-** | 8 | - | NEG -$5.0B | 768.89 | 770 | 750 | +$0 | - | out (clean 32, ADX 20, RVol 4.0) |
| 20 | **AMZN** | 270.90 | - | **-** | 8 | - | POS +$546.7M | - | 270 | 250 | +$0 | - | out (clean 35, ADX 16, RVol 3.7) |
| 21 | **PLTR** | 161.33 | - | **-** | 8 | - | NEG -$50.8M | - | 165 | 160 | +$0 | - | out (clean 26, ADX 19, RVol 2.6) |
| 22 | **CRM** | 225.22 | - | **-** | 8 | - | NEG -$13.4M | - | 240 | 220 | +$0 | - | out (clean 34, ADX 17, RVol 3.0) |
| 23 | **IWM** | 284.37 | - | **-** | 7 | - | NEG -$130.6M | 285.07 | 285 | 270 | +$0 | - | out (clean 35, ADX 13, RVol 3.1) |
| 24 | **GOOGL** | 293.45 | - | **-** | 7 | - | POS +$89.5M | 282.29 | 300 | 290 | +$0 | - | out (clean 36, ADX 22, RVol 1.8) |
| 25 | **HOOD** | 84.86 | - | **-** | 7 | - | POS +$2.7M | 83.99 | 86 | 80 | +$0 | - | out (clean 29, ADX 20, RVol 1.5) |
| 26 | **META** | 627.13 | - | **-** | 6 | - | POS +$67.9M | 620.17 | 650 | 625 | +$0 | - | out (clean 32, ADX 20, RVol 1.5) |
| 27 | **COIN** | 148.89 | - | **-** | 5 | - | POS +$37.4M | - | 148 | 150 | +$0 | - | out (clean 31, ADX 14, RVol 1.1) |

## Big prints this scan (1)
- **AMD** PUT 450 2026-11-06 (1DTE): 30 @ 8.75 = **+$26k** SELL | vol 0 / OI 5,288

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
