# GEX + FLOW SCAN - Wed Nov 11, 09:35 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **AVGO** | 351.79 | TREND (flow not with it) | **CALLS** | 40 | none: 112 calls 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (45 contracts' greeks worked out here) | POS +$91.3M | - | 350 | 340 | +$0 | - | LONG (clean 34, ADX 34, RVol 2.8) |
| 2 | **DELL** | 362.55 | TREND (flow not with it) | **CALLS** | 30 | none: 29 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$3.2M | - | 350 | 340 | +$0 | - | LONG (clean 34, ADX 27, RVol 1.7) |
| 3 | **MU** | 769.06 | - | **-** | 20 | - | POS +$113.3M | 729 | 800 | 750 | +$0 | +$60k bull / +$0 bear | out (clean 31, ADX 31, RVol 2.0) |
| 4 | **QQQ** | 687.18 | - | **-** | 19 | - | NEG -$651.5M | 689.78 | 700 | 680 | +$0 | +$115k bull / +$0 bear | out (clean 32, ADX 36, RVol 1.5) |
| 5 | **SPY** | 756.70 | - | **-** | 11 | - | NEG -$4.0B | 761.21 | 760 | 750 | +$0 | - | out (clean 32, ADX 38, RVol 2.1) |
| 6 | **AMZN** | 273.50 | - | **-** | 11 | - | POS +$622.5M | - | 275 | 260 | +$0 | - | out (clean 34, ADX 38, RVol 2.0) |
| 7 | **META** | 647.40 | - | **-** | 10 | - | POS +$350.6M | 623.82 | 650 | 650 | +$0 | - | out (clean 32, ADX 36, RVol 1.9) |
| 8 | **PLTR** | 174.34 | - | **-** | 10 | - | POS +$75.5M | - | 170 | 180 | +$0 | - | out (clean 29, ADX 34, RVol 1.8) |
| 9 | **ARM** | 190.81 | - | **-** | 10 | - | POS +$53k | 190.09 | 200 | 200 | +$0 | - | out (clean 27, ADX 39, RVol 1.8) |
| 10 | **SHOP** | 147.81 | - | **-** | 10 | - | POS +$3.0M | 143.25 | 150 | 140 | +$0 | - | out (clean 32, ADX 35, RVol 1.8) |
| 11 | **HOOD** | 83.12 | - | **-** | 9 | - | POS +$8.3M | 78.68 | 85 | 80 | +$0 | - | out (clean 32, ADX 22, RVol 3.1) |
| 12 | **UBER** | 69.36 | - | **-** | 9 | - | POS +$9.7M | 68.23 | 70 | 70 | +$0 | - | out (clean 34, ADX 26, RVol 2.1) |
| 13 | **CRM** | 214.21 | - | **-** | 9 | - | NEG -$11.3M | - | 230 | 220 | +$0 | - | out (clean 31, ADX 23, RVol 3.5) |
| 14 | **IWM** | 281.90 | - | **-** | 8 | - | NEG -$466.7M | 282.99 | 285 | 270 | +$0 | - | out (clean 34, ADX 25, RVol 2.0) |
| 15 | **AAPL** | 352.06 | - | **-** | 8 | - | POS +$1.0B | 340.81 | 355 | 350 | +$0 | - | out (clean 28, ADX 24, RVol 1.8) |
| 16 | **AMD** | 532.39 | - | **-** | 8 | - | POS +$124.8M | - | 550 | 500 | +$0 | - | out (clean 33, ADX 22, RVol 2.1) |
| 17 | **GOOGL** | 291.40 | - | **-** | 8 | - | POS +$41.2M | 288.95 | 300 | 290 | +$0 | - | out (clean 29, ADX 26, RVol 1.6) |
| 18 | **NFLX** | 63.22 | - | **-** | 8 | - | NEG -$15.1M | 64.51 | 65 | 65 | +$0 | - | out (clean 29, ADX 22, RVol 2.0) |
| 19 | **SMH** | 501.79 | - | **-** | 7 | - | NEG -$76.4M | - | 500 | 475 | +$0 | - | out (clean 30, ADX 22, RVol 1.4) |
| 20 | **TSLA** | 391.07 | - | **-** | 7 | - | POS +$368.2M | - | 400 | 380 | +$0 | - | out (clean 32, ADX 19, RVol 1.7) |
| 21 | **COIN** | 133.85 | - | **-** | 7 | - | POS +$16.2M | 126.36 | 137 | 135 | +$0 | - | out (clean 28, ADX 23, RVol 1.5) |
| 22 | **SMCI** | 29.25 | - | **-** | 7 | - | POS +$9.2M | - | 30 | 30 | +$0 | - | out (clean 31, ADX 21, RVol 1.7) |
| 23 | **MSTR** | 121.40 | - | **-** | 7 | - | NEG -$4.4M | 123.18 | 133 | 120 | +$0 | - | out (clean 29, ADX 14, RVol 2.4) |
| 24 | **BABA** | 101.93 | - | **-** | 7 | - | NEG -$14.1M | 106.27 | 110 | 101 | +$0 | - | out (clean 30, ADX 18, RVol 2.1) |
| 25 | **NVDA** | 173.86 | - | **-** | 6 | - | NEG -$171.3M | - | 180 | 175 | +$0 | - | out (clean 33, ADX 17, RVol 1.7) |
| 26 | **MSFT** | 532.41 | - | **-** | 6 | - | POS +$377.2M | 512.93 | 550 | 520 | +$0 | - | out (clean 32, ADX 15, RVol 1.8) |
| 27 | **ORCL** | 125.09 | - | **-** | 6 | - | NEG -$4.2M | 129.34 | 130 | 125 | +$0 | - | out (clean 27, ADX 22, RVol 1.1) |

## Big prints this scan (3)
- **QQQ** CALL 680 2026-11-13 (2DTE): 100 @ 11.50 = **+$115k** BUY | vol 0 / OI 4,338
- **MU** CALL 780 2026-11-11 (0DTE): 37 @ 8.65 = **+$32k** BUY | vol 0 / OI 2,052
- **MU** CALL 785 2026-11-11 (0DTE): 37 @ 7.50 = **+$28k** BUY | vol 0 / OI 277

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
