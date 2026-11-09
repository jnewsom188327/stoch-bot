# GEX + FLOW SCAN - Mon Nov 09, 09:40 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 09:40:08 ET, last candle SPY 09:39, QQQ 09:39 | no errors

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **AMZN** | 274.14 | TREND (flow not with it) | **CALLS** | 39 | none: 88 calls 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (48 contracts' greeks worked out here) | POS +$441.8M | - | 270 | 265 | +$0 | - | LONG (clean 36, ADX 31, RVol 2.6) |
| 2 | **PLTR** | 164.98 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 39 | none: 14 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$6.4M | 156.02 | 165 | 170 | +$0 | - | out (clean 28, ADX 24, RVol 3.8) |
| 3 | **MSFT** | 542.71 | TREND (flow not with it) | **CALLS** | 34 | none: 172 calls 0-7DTE > 12 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (81 contracts' greeks worked out here) | POS +$577.6M | - | 550 | 540 | +$0 | - | LONG (clean 34, ADX 26, RVol 2.2) |
| 4 | **MSTR** | 122.88 | FLIP CROSS down into negative gamma | **PUTS** | 34 | none: 25 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$482k | 123.68 | 135 | 120 | +$0 | - | out (clean 30, ADX 39, RVol 2.5) |
| 5 | **UBER** | 69.36 | FLIP CROSS up into positive gamma | **CALLS** | 32 | 11/13 72C @ 0.43 (delta 0.23) = est +29% at 70 | POS +$272k | 69.32 | 70 | 65 | +$0 | - | out (clean 32, ADX 27, RVol 2.4) |
| 6 | **AAPL** | 349.80 | PINNED between the walls (positive gamma) - chop | **-** | 25 | - | POS +$405.5M | 338 | 350 | 350 | +$0 | - | out (clean 27, ADX 22, RVol 1.7) |
| 7 | **SPY** | 744.92 | - | **-** | 18 | - | NEG -$8.3B | 761.91 | 750 | 740 | +$0 | +$0 bull / -$392k bear | out (clean 32, ADX 18, RVol 2.5) |
| 8 | **HOOD** | 81.63 | - | **-** | 12 | - | NEG -$4.1M | - | 85 | 80 | +$0 | - | out (clean 30, ADX 37, RVol 2.5) |
| 9 | **META** | 641.68 | - | **-** | 11 | - | POS +$170.9M | 611.41 | 650 | 600 | +$0 | - | out (clean 33, ADX 34, RVol 3.0) |
| 10 | **NVDA** | 174.62 | - | **-** | 10 | - | NEG -$161.6M | - | 190 | 190 | +$0 | - | out (clean 32, ADX 26, RVol 8.2) |
| 11 | **TSLA** | 371.94 | - | **-** | 10 | - | POS +$84.8M | - | 400 | 380 | +$0 | - | out (clean 34, ADX 26, RVol 2.9) |
| 12 | **AMD** | 475.37 | - | **-** | 10 | - | NEG -$28.6M | - | 500 | 440 | +$0 | - | out (clean 32, ADX 29, RVol 4.1) |
| 13 | **SMCI** | 27.64 | - | **-** | 10 | - | NEG -$719k | - | 30 | 25 | +$0 | - | out (clean 32, ADX 35, RVol 1.8) |
| 14 | **IWM** | 277.98 | - | **-** | 9 | - | NEG -$1.6B | 285.53 | 285 | 270 | +$0 | - | out (clean 32, ADX 22, RVol 3.1) |
| 15 | **GOOGL** | 294.92 | - | **-** | 9 | - | POS +$30.3M | 290.57 | 300 | 290 | +$0 | - | out (clean 32, ADX 23, RVol 2.9) |
| 16 | **NFLX** | 63.47 | - | **-** | 9 | - | NEG -$21.3M | - | 65 | 65 | +$0 | - | out (clean 32, ADX 29, RVol 2.0) |
| 17 | **AVGO** | 311.86 | - | **-** | 9 | - | NEG -$68.6M | - | 340 | 300 | +$0 | - | out (clean 30, ADX 24, RVol 4.5) |
| 18 | **DELL** | 330.72 | - | **-** | 9 | - | NEG -$8.8M | - | 350 | 340 | +$0 | - | out (clean 31, ADX 22, RVol 2.4) |
| 19 | **ARM** | 178.77 | - | **-** | 9 | - | NEG -$5.0M | - | 185 | 190 | +$0 | - | out (clean 24, ADX 22, RVol 2.6) |
| 20 | **CRM** | 214.95 | - | **-** | 9 | - | NEG -$10.8M | - | 195 | 220 | +$0 | - | out (clean 34, ADX 22, RVol 3.4) |
| 21 | **SHOP** | 149.19 | - | **-** | 9 | - | POS +$836k | 142.28 | 150 | 140 | +$0 | - | out (clean 35, ADX 21, RVol 2.5) |
| 22 | **BABA** | 105.94 | - | **-** | 9 | - | POS +$4.1M | 103.45 | 110 | 110 | +$0 | - | out (clean 33, ADX 21, RVol 3.6) |
| 23 | **QQQ** | 667.66 | - | **-** | 8 | - | NEG -$2.3B | 701.12 | 670 | 650 | +$0 | - | out (clean 32, ADX 20, RVol 2.4) |
| 24 | **COIN** | 132.20 | - | **-** | 8 | - | NEG -$8.4M | - | 140 | 130 | +$0 | - | out (clean 31, ADX 25, RVol 1.8) |
| 25 | **SMH** | 470.74 | - | **-** | 7 | - | NEG -$261.4M | - | 500 | 445 | +$0 | - | out (clean 31, ADX 20, RVol 1.7) |
| 26 | **MU** | 699.96 | - | **-** | 6 | - | NEG -$46.4M | - | 750 | 700 | +$0 | - | out (clean 30, ADX 14, RVol 1.8) |
| 27 | **ORCL** | 116.38 | - | **-** | 6 | - | NEG -$32.8M | - | 125 | 105 | +$0 | - | out (clean 29, ADX 17, RVol 1.6) |

## Big prints this scan (2)
- **SPY** PUT 747 2026-11-13 (4DTE): 288 @ 10.07 = **+$290k** BUY | vol 0 / OI 1,786
- **SPY** PUT 747 2026-11-13 (4DTE): 100 @ 10.17 = **+$102k** BUY | vol 0 / OI 1,786

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
