# GEX + FLOW SCAN - Tue Nov 10, 09:40 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 09:40:08 ET, last candle SPY 09:39, QQQ 09:39 | no errors

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **IWM** | 279.96 | TREND (flow not with it) | **PUTS** | 44 | 11/10 278P @ 0.44 (delta 0.25) = est +60% at 278.67 | NEG -$1.1B | 284.36 | 285 | 270 | +$0 | - | SHORT (clean 35, ADX 44, RVol 3.8) |
| 2 | **GOOGL** | 289.73 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 38 | none: 69 calls 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (3 contracts' greeks worked out here) | POS +$5.9M | 289.5 | 300 | 290 | +$0 | - | out (clean 30, ADX 22, RVol 2.7) |
| 3 | **TSLA** | 375.99 | TREND (flow not with it) | **PUTS** | 35 | none: 90 puts 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (4 contracts' greeks worked out here) | POS +$188.3M | - | 400 | 380 | +$0 | - | SHORT (clean 34, ADX 43, RVol 1.9) |
| 4 | **MSTR** | 123.64 | FLIP CROSS up into positive gamma | **CALLS** | 26 | none: 25 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$6.1M | 120.26 | 133 | 120 | +$0 | - | out (clean 31, ADX 24, RVol 1.6) |
| 5 | **SPY** | 749.12 | - | **-** | 11 | - | NEG -$6.6B | 761 | 750 | 730 | +$0 | - | out (clean 31, ADX 33, RVol 2.9) |
| 6 | **QQQ** | 673.89 | - | **-** | 11 | - | NEG -$1.9B | 692.28 | 680 | 680 | +$0 | - | out (clean 31, ADX 33, RVol 2.4) |
| 7 | **AMD** | 511.87 | - | **-** | 11 | - | POS +$48.9M | - | 500 | 500 | +$0 | - | out (clean 31, ADX 35, RVol 2.4) |
| 8 | **META** | 642.10 | - | **-** | 11 | - | POS +$247.5M | - | 650 | 650 | +$0 | - | out (clean 33, ADX 37, RVol 2.2) |
| 9 | **UBER** | 70.33 | - | **-** | 11 | - | POS +$9.4M | 68.38 | 70 | 70 | +$0 | - | out (clean 32, ADX 35, RVol 2.2) |
| 10 | **MSFT** | 542.70 | - | **-** | 10 | - | POS +$676.0M | - | 550 | 535 | +$0 | - | out (clean 33, ADX 37, RVol 1.7) |
| 11 | **NFLX** | 63.05 | - | **-** | 10 | - | NEG -$19.6M | 65.52 | 65 | 60 | +$0 | - | out (clean 29, ADX 26, RVol 2.7) |
| 12 | **AVGO** | 322.69 | - | **-** | 10 | - | NEG -$21.2M | - | 340 | 320 | +$0 | - | out (clean 31, ADX 30, RVol 3.2) |
| 13 | **PLTR** | 168.41 | - | **-** | 10 | - | POS +$50.1M | - | 165 | 170 | +$0 | - | out (clean 29, ADX 32, RVol 2.1) |
| 14 | **SMH** | 480.54 | - | **-** | 9 | - | NEG -$228.4M | - | 500 | 475 | +$0 | - | out (clean 29, ADX 31, RVol 1.6) |
| 15 | **NVDA** | 172.13 | - | **-** | 9 | - | NEG -$175.0M | - | 185 | 180 | +$0 | - | out (clean 32, ADX 24, RVol 3.0) |
| 16 | **COIN** | 134.06 | - | **-** | 9 | - | POS +$9.7M | - | 141 | 135 | +$0 | - | out (clean 32, ADX 22, RVol 2.3) |
| 17 | **DELL** | 331.62 | - | **-** | 9 | - | NEG -$10.5M | - | 350 | 340 | +$0 | - | out (clean 33, ADX 28, RVol 2.2) |
| 18 | **MU** | 711.53 | - | **-** | 9 | - | NEG -$35.4M | - | 750 | 750 | +$0 | - | out (clean 30, ADX 27, RVol 2.0) |
| 19 | **ORCL** | 119.08 | - | **-** | 9 | - | NEG -$24.1M | - | 130 | 120 | +$0 | - | out (clean 29, ADX 37, RVol 1.1) |
| 20 | **HOOD** | 82.13 | - | **-** | 9 | - | POS +$3.8M | 79.12 | 85 | 80 | +$0 | - | out (clean 29, ADX 27, RVol 1.9) |
| 21 | **ARM** | 181.49 | - | **-** | 9 | - | NEG -$4.9M | - | 185 | 190 | +$0 | - | out (clean 27, ADX 25, RVol 2.1) |
| 22 | **CRM** | 213.78 | - | **-** | 9 | - | NEG -$11.2M | - | 230 | 220 | +$0 | - | out (clean 32, ADX 22, RVol 3.2) |
| 23 | **SHOP** | 150.10 | - | **-** | 9 | - | POS +$2.9M | 141.47 | 155 | 140 | +$0 | - | out (clean 32, ADX 32, RVol 1.5) |
| 24 | **BABA** | 104.86 | - | **-** | 9 | - | NEG -$621k | 105.06 | 110 | 105 | +$0 | - | out (clean 30, ADX 25, RVol 2.8) |
| 25 | **AAPL** | 351.31 | - | **-** | 8 | - | POS +$534.8M | 335.44 | 360 | 340 | +$0 | - | out (clean 28, ADX 23, RVol 2.1) |
| 26 | **AMZN** | 271.56 | - | **-** | 8 | - | POS +$468.0M | - | 270 | 265 | +$0 | - | out (clean 32, ADX 22, RVol 2.2) |
| 27 | **SMCI** | 27.87 | - | **-** | 8 | - | POS +$3.0M | - | 30 | 30 | +$0 | - | out (clean 29, ADX 24, RVol 2.1) |

## Big prints this scan (0)

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
