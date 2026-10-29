# GEX + FLOW SCAN - Thu Oct 29, 09:40 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 09:40:08 ET, last candle SPY 09:39, QQQ 09:39 | no errors

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **ARM** | 227.25 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 40 | none: 18 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (3 contracts' greeks worked out here) | POS +$2.6M | 222.66 | 227.5 | 220 | +$0 | - | out (clean 26, ADX 27, RVol 4.1) |
| 2 | **AMD** | 568.83 | - | **-** | 13 | - | POS +$145.0M | - | 600 | 550 | +$0 | - | out (clean 30, ADX 43, RVol 2.7) |
| 3 | **AMZN** | 243.68 | - | **-** | 13 | - | NEG -$2.9M | 245 | 265 | 250 | +$0 | - | out (clean 32, ADX 44, RVol 5.8) |
| 4 | **ORCL** | 140.78 | - | **-** | 13 | - | POS +$117.7M | - | 135 | 140 | +$0 | - | out (clean 31, ADX 50, RVol 5.3) |
| 5 | **AVGO** | 341.82 | - | **-** | 12 | - | NEG -$4.8M | 342.59 | 350 | 340 | +$0 | - | out (clean 29, ADX 40, RVol 3.6) |
| 6 | **QQQ** | 712.50 | - | **-** | 11 | - | NEG -$5.3B | 726.88 | 720 | 700 | +$0 | - | out (clean 29, ADX 32, RVol 3.4) |
| 7 | **IWM** | 283.23 | - | **-** | 11 | - | POS +$587.9M | 281.44 | 284 | 270 | +$0 | - | out (clean 24, ADX 34, RVol 2.5) |
| 8 | **NVDA** | 212.91 | - | **-** | 11 | - | POS +$186.5M | 210.21 | 215 | 210 | +$0 | - | out (clean 26, ADX 32, RVol 2.7) |
| 9 | **MSFT** | 532.23 | - | **-** | 11 | - | POS +$638.7M | - | 525 | 530 | +$0 | - | out (clean 29, ADX 33, RVol 6.3) |
| 10 | **GOOGL** | 281.50 | - | **-** | 10 | - | NEG -$165.9M | - | 300 | 290 | +$0 | - | out (clean 32, ADX 30, RVol 10.8) |
| 11 | **SMCI** | 35.10 | - | **-** | 10 | - | POS +$22.3M | - | 35 | 35 | +$0 | - | out (clean 28, ADX 30, RVol 2.3) |
| 12 | **MU** | 955.93 | - | **-** | 10 | - | POS +$373.6M | - | 950 | 950 | +$0 | - | out (clean 29, ADX 30, RVol 3.7) |
| 13 | **MSTR** | 139.00 | - | **-** | 10 | - | POS +$20.0M | - | 152.5 | 140 | +$0 | - | out (clean 26, ADX 31, RVol 3.5) |
| 14 | **BABA** | 99.50 | - | **-** | 10 | - | NEG -$19.5M | 102 | 102 | 100 | +$0 | - | out (clean 28, ADX 29, RVol 3.0) |
| 15 | **SPY** | 767.76 | - | **-** | 9 | - | NEG -$5.7B | 773.01 | 770 | 765 | +$0 | - | out (clean 28, ADX 25, RVol 4.7) |
| 16 | **SMH** | 557.90 | - | **-** | 9 | - | NEG -$73.0M | 562.59 | 560 | 555 | +$0 | - | out (clean 28, ADX 24, RVol 3.5) |
| 17 | **TSLA** | 401.28 | - | **-** | 9 | - | POS +$446.7M | - | 400 | 400 | +$0 | - | out (clean 29, ADX 28, RVol 1.7) |
| 18 | **NFLX** | 61.50 | - | **-** | 9 | - | NEG -$55.9M | - | 63 | 60 | +$0 | - | out (clean 31, ADX 25, RVol 2.2) |
| 19 | **PLTR** | 192.82 | - | **-** | 9 | - | POS +$16.5M | 191.01 | 200 | 190 | +$0 | - | out (clean 26, ADX 23, RVol 2.9) |
| 20 | **COIN** | 159.36 | - | **-** | 9 | - | POS +$4.6M | 152.06 | 170 | 155 | +$0 | - | out (clean 27, ADX 22, RVol 4.0) |
| 21 | **UBER** | 64.33 | - | **-** | 9 | - | NEG -$35.9M | - | 70 | 65 | +$0 | - | out (clean 29, ADX 24, RVol 2.6) |
| 22 | **CRM** | 227.56 | - | **-** | 9 | - | NEG -$19.1M | - | 240 | 230 | +$0 | - | out (clean 27, ADX 22, RVol 5.2) |
| 23 | **AAPL** | 349.12 | - | **-** | 8 | - | POS +$583.9M | 338.39 | 350 | 345 | +$0 | - | out (clean 28, ADX 18, RVol 3.5) |
| 24 | **META** | 619.59 | - | **-** | 8 | - | NEG -$108.7M | 630.72 | 650 | 625 | +$0 | - | out (clean 28, ADX 22, RVol 1.8) |
| 25 | **DELL** | 484.45 | - | **-** | 8 | - | POS +$11.1M | 475.79 | 500 | 500 | +$0 | - | out (clean 32, ADX 26, RVol 1.8) |
| 26 | **HOOD** | 89.28 | - | **-** | 8 | - | NEG -$27.5M | - | 95 | 90 | +$0 | - | out (clean 29, ADX 18, RVol 2.6) |
| 27 | **SHOP** | 163.79 | - | **-** | 7 | - | NEG -$7.5M | 172.16 | 175 | 165 | +$0 | - | out (clean 28, ADX 20, RVol 1.8) |

## Big prints this scan (0)

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
