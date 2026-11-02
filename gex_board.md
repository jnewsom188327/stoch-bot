# GEX + FLOW SCAN - Mon Nov 02, 09:40 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 09:40:08 ET, last candle SPY 09:39, QQQ 09:39 | no errors

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **SMCI** | 32.93 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 43 | none: 13 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$610k | - | 35 | 33 | +$0 | - | out (clean 31, ADX 48, RVol 3.9) |
| 2 | **AMZN** | 249.52 | PINNED between the walls (positive gamma) - chop | **-** | 36 | - | POS +$81.7M | 242.59 | 250 | 250 | +$0 | - | out (clean 31, ADX 32, RVol 3.1) |
| 3 | **HOOD** | 86.18 | - | **-** | 13 | - | NEG -$9.1M | - | 93 | 90 | +$0 | - | out (clean 32, ADX 47, RVol 3.7) |
| 4 | **COIN** | 142.35 | - | **-** | 12 | - | NEG -$8.9M | - | 150 | 150 | +$0 | - | out (clean 27, ADX 42, RVol 6.1) |
| 5 | **SHOP** | 159.80 | - | **-** | 12 | - | NEG -$469k | - | 175 | 175 | +$0 | - | out (clean 28, ADX 40, RVol 6.9) |
| 6 | **SPY** | 759.39 | - | **-** | 11 | - | NEG -$9.6B | 775.57 | 800 | 750 | +$0 | - | out (clean 28, ADX 35, RVol 8.0) |
| 7 | **QQQ** | 695.27 | - | **-** | 11 | - | NEG -$5.5B | 733.17 | 720 | 680 | +$0 | - | out (clean 29, ADX 35, RVol 5.0) |
| 8 | **IWM** | 281.00 | - | **-** | 11 | - | NEG -$1.1B | 286.67 | 285 | 270 | +$0 | - | out (clean 30, ADX 33, RVol 3.9) |
| 9 | **SMH** | 526.39 | - | **-** | 11 | - | NEG -$323.1M | - | 532.5 | 500 | +$0 | - | out (clean 31, ADX 34, RVol 4.2) |
| 10 | **NVDA** | 207.88 | - | **-** | 11 | - | NEG -$183.5M | 215.24 | 210 | 210 | +$0 | - | out (clean 29, ADX 34, RVol 3.3) |
| 11 | **AMD** | 505.89 | - | **-** | 11 | - | NEG -$94.3M | - | 550 | 500 | +$0 | - | out (clean 30, ADX 32, RVol 4.3) |
| 12 | **GOOGL** | 285.05 | - | **-** | 11 | - | NEG -$78.9M | - | 285 | 290 | +$0 | - | out (clean 33, ADX 38, RVol 2.4) |
| 13 | **NFLX** | 62.66 | - | **-** | 11 | - | NEG -$20.8M | - | 63 | 60 | +$0 | - | out (clean 31, ADX 35, RVol 4.1) |
| 14 | **AVGO** | 325.79 | - | **-** | 11 | - | NEG -$116.2M | - | 340 | 320 | +$0 | - | out (clean 30, ADX 33, RVol 3.4) |
| 15 | **MSTR** | 134.02 | - | **-** | 11 | - | POS +$3.3M | - | 135 | 125 | +$0 | - | out (clean 28, ADX 32, RVol 6.4) |
| 16 | **BABA** | 103.11 | - | **-** | 11 | - | POS +$2.5M | 101.04 | 105 | 100 | +$0 | - | out (clean 31, ADX 34, RVol 5.5) |
| 17 | **TSLA** | 405.61 | - | **-** | 10 | - | POS +$250.9M | - | 410 | 400 | +$0 | - | out (clean 31, ADX 31, RVol 4.1) |
| 18 | **AAPL** | 340.71 | - | **-** | 10 | - | POS +$52.9M | 337.22 | 350 | 330 | +$0 | - | out (clean 32, ADX 28, RVol 4.7) |
| 19 | **META** | 614.62 | - | **-** | 10 | - | NEG -$121.7M | 627.71 | 650 | 600 | +$0 | - | out (clean 29, ADX 34, RVol 2.0) |
| 20 | **DELL** | 413.67 | - | **-** | 10 | - | NEG -$24.3M | - | 440 | 400 | +$0 | - | out (clean 34, ADX 25, RVol 2.9) |
| 21 | **MU** | 882.12 | - | **-** | 10 | - | NEG -$208.8M | - | 910 | 900 | +$0 | - | out (clean 31, ADX 30, RVol 3.9) |
| 22 | **ORCL** | 124.81 | - | **-** | 10 | - | NEG -$39.4M | - | 130 | 120 | +$0 | - | out (clean 32, ADX 26, RVol 3.4) |
| 23 | **ARM** | 202.87 | - | **-** | 10 | - | NEG -$6.8M | - | 220 | 200 | +$0 | - | out (clean 26, ADX 31, RVol 5.7) |
| 24 | **CRM** | 231.66 | - | **-** | 10 | - | NEG -$5.7M | 243.47 | 240 | 220 | +$0 | - | out (clean 28, ADX 29, RVol 2.2) |
| 25 | **MSFT** | 524.12 | - | **-** | 9 | - | POS +$368.1M | 498.03 | 540 | 500 | +$0 | - | out (clean 26, ADX 22, RVol 4.2) |
| 26 | **PLTR** | 184.33 | - | **-** | 8 | - | NEG -$10.6M | - | 200 | 180 | +$0 | - | out (clean 26, ADX 16, RVol 4.8) |
| 27 | **UBER** | 66.50 | - | **-** | 8 | - | NEG -$13.6M | - | 70 | 65 | +$0 | - | out (clean 26, ADX 23, RVol 2.1) |

## Big prints this scan (0)

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
