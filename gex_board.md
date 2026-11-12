# GEX + FLOW SCAN - Thu Nov 12, 09:40 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 09:40:08 ET, last candle SPY 09:39, QQQ 09:39 | no errors

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **NVDA** | 159.55 | TREND (flow not with it) | **PUTS** | 53 | none: 51 puts 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (8 contracts' greeks worked out here) | NEG -$193.2M | - | 170 | 160 | +$0 | +$0 bull / -$1.6M bear | SHORT (clean 34, ADX 41, RVol 4.0) |
| 2 | **DELL** | 356.91 | FLIP CROSS up into positive gamma | **CALLS** | 53 | none: 29 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (8 contracts' greeks worked out here) | POS +$2.2M | 347.36 | 360 | 340 | +$0 | - | SHORT (clean 38, ADX 40, RVol 4.2) |
| 3 | **AVGO** | 364.10 | TREND (flow not with it) | **CALLS** | 44 | none: 81 calls 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (5 contracts' greeks worked out here) | POS +$127.2M | - | 350 | 350 | +$0 | - | LONG (clean 37, ADX 48, RVol 5.0) |
| 4 | **QQQ** | 687.26 | TREND (flow not with it) | **PUTS** | 42 | none: 696 puts 0-7DTE > 64 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (204 contracts' greeks worked out here) | NEG -$625.2M | 690.27 | 700 | 680 | +$0 | - | SHORT (clean 33, ADX 40, RVol 3.2) |
| 5 | **SMCI** | 27.84 | TREND (flow not with it) | **PUTS** | 42 | 11/13 27P @ 0.41 (delta 0.30) = est +66% at 27 | POS +$3.1M | - | 30 | 27 | +$0 | - | SHORT (clean 34, ADX 43, RVol 2.8) |
| 6 | **AMD** | 571.32 | TREND (flow not with it) | **CALLS** | 41 | none: 138 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (9 contracts' greeks worked out here) | POS +$187.6M | - | 600 | 550 | +$0 | +$0 bull / -$88k bear | LONG (clean 36, ADX 31, RVol 3.0) |
| 7 | **SPY** | 757.25 | TREND (flow not with it) | **PUTS** | 39 | 11/12 752P @ 0.77 (delta 0.21) = est +46% at 754.81 | NEG -$3.1B | 761.02 | 760 | 760 | +$0 | - | SHORT (clean 34, ADX 31, RVol 2.6) |
| 8 | **IWM** | 281.25 | TREND (flow not with it) | **PUTS** | 35 | 11/13 279P @ 0.78 (delta 0.30) = est +30% at 280.35 | NEG -$740.7M | 283.11 | 285 | 275 | +$0 | - | SHORT (clean 35, ADX 27, RVol 2.3) |
| 9 | **MU** | 796.64 | TREND (flow not with it) | **PUTS** | 31 | none: 122 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (8 contracts' greeks worked out here) | POS +$92.5M | - | 800 | 850 | +$0 | - | SHORT (clean 33, ADX 30, RVol 1.8) |
| 10 | **META** | 628.66 | - | **-** | 13 | - | POS +$36.8M | 623.38 | 650 | 600 | +$0 | - | out (clean 30, ADX 51, RVol 2.4) |
| 11 | **COIN** | 132.01 | - | **-** | 11 | - | POS +$2.6M | 130.28 | 137 | 135 | +$0 | - | out (clean 30, ADX 39, RVol 1.8) |
| 12 | **SMH** | 498.48 | - | **-** | 10 | - | NEG -$134.1M | - | 500 | 475 | +$0 | - | out (clean 32, ADX 43, RVol 1.4) |
| 13 | **AAPL** | 356.49 | - | **-** | 10 | - | POS +$1.1B | 337.56 | 360 | 360 | +$0 | - | out (clean 28, ADX 35, RVol 2.1) |
| 14 | **NFLX** | 63.26 | - | **-** | 10 | - | NEG -$15.3M | 64.05 | 65 | 65 | +$0 | - | out (clean 27, ADX 33, RVol 2.1) |
| 15 | **MSTR** | 114.81 | - | **-** | 10 | - | NEG -$31.5M | - | 125 | 110 | +$0 | - | out (clean 28, ADX 29, RVol 3.7) |
| 16 | **UBER** | 69.61 | - | **-** | 10 | - | POS +$13.0M | 68.17 | 70 | 70 | +$0 | - | out (clean 32, ADX 27, RVol 2.9) |
| 17 | **BABA** | 94.61 | - | **-** | 10 | - | NEG -$17.9M | - | 100 | 100 | +$0 | - | out (clean 28, ADX 27, RVol 4.5) |
| 18 | **TSLA** | 393.10 | - | **-** | 9 | - | POS +$372.1M | - | 400 | 380 | +$0 | - | out (clean 31, ADX 31, RVol 1.9) |
| 19 | **MSFT** | 523.70 | - | **-** | 9 | - | POS +$102.9M | 517.95 | 535 | 520 | +$0 | - | out (clean 32, ADX 25, RVol 2.4) |
| 20 | **GOOGL** | 295.70 | - | **-** | 9 | - | POS +$103.6M | 288.3 | 300 | 290 | +$0 | - | out (clean 29, ADX 23, RVol 2.9) |
| 21 | **ORCL** | 125.94 | - | **-** | 9 | - | POS +$8.5M | 120.22 | 130 | 125 | +$0 | - | out (clean 30, ADX 21, RVol 2.5) |
| 22 | **HOOD** | 82.98 | - | **-** | 9 | - | POS +$9.0M | 79.86 | 85 | 80 | +$0 | - | out (clean 35, ADX 23, RVol 3.5) |
| 23 | **ARM** | 200.99 | - | **-** | 9 | - | POS +$9.2M | - | 200 | 200 | +$0 | - | out (clean 32, ADX 24, RVol 3.1) |
| 24 | **AMZN** | 271.40 | - | **-** | 8 | - | POS +$514.4M | - | 270 | 270 | +$0 | - | out (clean 31, ADX 19, RVol 2.1) |
| 25 | **PLTR** | 171.19 | - | **-** | 8 | - | POS +$86.8M | - | 170 | 170 | +$0 | - | out (clean 29, ADX 23, RVol 1.9) |
| 26 | **CRM** | 216.00 | - | **-** | 8 | - | NEG -$9.3M | - | 220 | 220 | +$0 | - | out (clean 29, ADX 20, RVol 2.2) |
| 27 | **SHOP** | 147.31 | - | **-** | 8 | - | POS +$4.4M | 142.56 | 150 | 140 | +$0 | - | out (clean 32, ADX 20, RVol 2.2) |

## Big prints this scan (9)
- **NVDA** PUT 155 2026-11-13 (1DTE): 362 @ 7.25 = **+$262k** BUY | vol 0 / OI 9,956
- **NVDA** PUT 167.5 2026-11-16 (4DTE): 66 @ 17.10 = **+$113k** BUY | vol 0 / OI 1,806
- **NVDA** PUT 155 2026-11-13 (1DTE): 150 @ 7.20 = **+$108k** BUY | vol 0 / OI 9,956
- **NVDA** PUT 155 2026-11-13 (1DTE): 150 @ 6.75 = **+$101k** BUY | vol 0 / OI 9,956
- **NVDA** PUT 167.5 2026-11-16 (4DTE): 34 @ 17.10 = **+$58k** BUY | vol 0 / OI 1,806
- **NVDA** PUT 155 2026-11-13 (1DTE): 57 @ 7.50 = **+$43k** BUY | vol 0 / OI 9,956
- **NVDA** CALL 160 2026-11-16 (4DTE): 100 @ 2.70 = **+$27k** SELL | vol 0 / OI 766
- **NVDA** PUT 155 2026-11-13 (1DTE): 40 @ 6.60 = **+$26k** BUY | vol 0 / OI 9,956
- **NVDA** PUT 165 2026-11-13 (1DTE): 17 @ 14.90 = **+$25k** BUY | vol 0 / OI 19,300

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
