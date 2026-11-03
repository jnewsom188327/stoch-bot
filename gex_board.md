# GEX + FLOW SCAN - Tue Nov 03, 09:40 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 09:40:08 ET, last candle SPY 09:39, QQQ 09:39 | no errors

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **BABA** | 100.82 | TREND (flow not with it) | **PUTS** | 43 | none: 20 puts 0-7DTE > 3 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only +16% at the target (needs +20%) | POS +$1.8M | 100.08 | 102 | 100 | +$0 | - | SHORT (clean 34, ADX 52, RVol 4.1) |
| 2 | **AAPL** | 329.85 | - | **-** | 20 | - | NEG -$422.2M | 343.91 | 350 | 330 | +$0 | +$0 bull / -$26k bear | out (clean 32, ADX 30, RVol 6.9) |
| 3 | **QQQ** | 685.52 | - | **-** | 13 | - | NEG -$5.0B | - | 700 | 680 | +$0 | - | out (clean 32, ADX 44, RVol 3.2) |
| 4 | **SMH** | 521.80 | - | **-** | 13 | - | NEG -$266.1M | - | 532.5 | 500 | +$0 | - | out (clean 33, ADX 46, RVol 3.3) |
| 5 | **AMD** | 490.75 | - | **-** | 13 | - | NEG -$65.7M | - | 520 | 500 | +$0 | - | out (clean 33, ADX 53, RVol 4.7) |
| 6 | **AMZN** | 247.06 | - | **-** | 13 | - | POS +$132.1M | 236.09 | 250 | 250 | +$0 | - | out (clean 34, ADX 42, RVol 2.5) |
| 7 | **MSFT** | 509.94 | - | **-** | 13 | - | POS +$108.5M | 500.63 | 535 | 500 | +$0 | - | out (clean 29, ADX 64, RVol 3.8) |
| 8 | **PLTR** | 171.19 | - | **-** | 13 | - | NEG -$26.9M | - | 165 | 180 | +$0 | - | out (clean 27, ADX 52, RVol 8.7) |
| 9 | **DELL** | 410.79 | - | **-** | 13 | - | NEG -$25.5M | - | 440 | 400 | +$0 | - | out (clean 35, ADX 46, RVol 2.8) |
| 10 | **MU** | 867.31 | - | **-** | 13 | - | NEG -$171.6M | - | 900 | 850 | +$0 | - | out (clean 31, ADX 46, RVol 4.5) |
| 11 | **CRM** | 216.38 | - | **-** | 13 | - | NEG -$15.6M | - | 230 | 220 | +$0 | - | out (clean 28, ADX 44, RVol 4.1) |
| 12 | **SHOP** | 140.57 | - | **-** | 13 | - | NEG -$3.2M | - | 145 | 140 | +$0 | - | out (clean 31, ADX 46, RVol 7.1) |
| 13 | **SPY** | 753.72 | - | **-** | 12 | - | NEG -$9.4B | 770.77 | 750 | 750 | +$0 | - | out (clean 31, ADX 41, RVol 4.3) |
| 14 | **NVDA** | 208.68 | - | **-** | 12 | - | POS +$126.6M | 203.22 | 210 | 200 | +$0 | - | out (clean 30, ADX 40, RVol 3.9) |
| 15 | **SMCI** | 31.80 | - | **-** | 12 | - | POS +$2.2M | - | 34.5 | 30 | +$0 | - | out (clean 36, ADX 39, RVol 3.4) |
| 16 | **AVGO** | 334.11 | - | **-** | 11 | - | NEG -$41.9M | 353.57 | 340 | 340 | +$0 | - | out (clean 32, ADX 34, RVol 3.5) |
| 17 | **COIN** | 142.56 | - | **-** | 11 | - | POS +$17.5M | - | 142 | 130 | +$0 | - | out (clean 25, ADX 33, RVol 3.6) |
| 18 | **ORCL** | 122.86 | - | **-** | 11 | - | NEG -$41.9M | - | 135 | 120 | +$0 | - | out (clean 32, ADX 34, RVol 6.5) |
| 19 | **ARM** | 202.87 | - | **-** | 11 | - | NEG -$6.6M | - | 220 | 200 | +$0 | - | out (clean 26, ADX 36, RVol 3.3) |
| 20 | **UBER** | 66.17 | - | **-** | 11 | - | NEG -$14.3M | - | 70 | 65 | +$0 | - | out (clean 29, ADX 34, RVol 3.7) |
| 21 | **TSLA** | 401.88 | - | **-** | 10 | - | POS +$234.1M | - | 400 | 400 | +$0 | - | out (clean 32, ADX 35, RVol 1.9) |
| 22 | **GOOGL** | 278.71 | - | **-** | 10 | - | NEG -$42.2M | 285.75 | 285 | 290 | +$0 | - | out (clean 33, ADX 29, RVol 2.5) |
| 23 | **NFLX** | 62.13 | - | **-** | 10 | - | NEG -$16.4M | 65.85 | 63 | 60 | +$0 | - | out (clean 28, ADX 27, RVol 2.8) |
| 24 | **MSTR** | 133.08 | - | **-** | 10 | - | POS +$69.6M | - | 135 | 125 | +$0 | - | out (clean 26, ADX 32, RVol 2.4) |
| 25 | **IWM** | 280.15 | - | **-** | 9 | - | NEG -$1.2B | 287.58 | 285 | 270 | +$0 | - | out (clean 33, ADX 24, RVol 2.8) |
| 26 | **META** | 612.09 | - | **-** | 8 | - | NEG -$89.7M | 627.09 | 650 | 610 | +$0 | - | out (clean 28, ADX 17, RVol 2.4) |
| 27 | **HOOD** | 84.42 | - | **-** | 8 | - | NEG -$3.7M | - | 90 | 85 | +$0 | - | out (clean 32, ADX 28, RVol 1.6) |

## Big prints this scan (0)

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
