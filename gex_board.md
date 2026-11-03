# GEX + FLOW SCAN - Tue Nov 03, 11:10 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 11:10:08 ET, last candle SPY 11:09, QQQ 11:09 | no errors

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **COIN** | 150.25 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 60 | none: 21 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$21.5M | - | 148 | 150 | -$4.2M | +$0 bull / -$566k bear | out (clean 28, ADX 65, RVol 1.3) |
| 2 | **META** | 621.72 | FLOW SURGE | **PUTS** | 43 | none: 150 puts 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (2 contracts' greeks worked out here) | NEG -$35.3M | 626.99 | 650 | 610 | -$17.6M | +$0 bull / -$297k bear | out (clean 28, ADX 43, RVol 0.6) |
| 3 | **MSFT** | 516.63 | FLOW SURGE | **PUTS** | 37 | none: 125 puts 0-7DTE > 13 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (13 contracts' greeks worked out here) | POS +$180.7M | 501.55 | 540 | 500 | -$8.0M | +$0 bull / -$389k bear | out (clean 29, ADX 32, RVol 0.7) |
| 4 | **ORCL** | 125.98 | - | **-** | 33 | - | NEG -$41.2M | - | 135 | 125 | -$7.5M | +$42k bull / +$0 bear | out (clean 33, ADX 53, RVol 0.8) |
| 5 | **MSTR** | 137.67 | - | **-** | 30 | - | POS +$84.6M | - | 135 | 125 | -$3.9M | +$28k bull / -$256k bear | out (clean 29, ADX 45, RVol 1.5) |
| 6 | **SHOP** | 144.56 | - | **-** | 28 | - | NEG -$3.8M | - | 145 | 150 | -$3.9M | - | out (clean 32, ADX 44, RVol 3.0) |
| 7 | **DELL** | 410.56 | - | **-** | 25 | - | NEG -$26.1M | - | 440 | 400 | +$1.9M | +$0 bull / -$79k bear | out (clean 34, ADX 30, RVol 0.3) |
| 8 | **AVGO** | 334.25 | - | **-** | 23 | - | NEG -$41.5M | 351.98 | 340 | 340 | +$2.3M | +$0 bull / -$33k bear | out (clean 31, ADX 38, RVol 0.4) |
| 9 | **PLTR** | 173.59 | - | **-** | 23 | - | NEG -$24.6M | - | 165 | 180 | -$2.9M | +$168k bull / -$544k bear | out (clean 28, ADX 41, RVol 1.8) |
| 10 | **ARM** | 204.34 | - | **-** | 23 | - | NEG -$6.7M | - | 220 | 200 | -$255k | +$0 bull / -$75k bear | out (clean 25, ADX 31, RVol 0.4) |
| 11 | **SPY** | 756.21 | - | **-** | 21 | - | NEG -$8.3B | 770.65 | 770 | 750 | -$96.1M | +$0 bull / -$6.5M bear | out (clean 31, ADX 22, RVol 0.5) |
| 12 | **SMH** | 523.12 | - | **-** | 21 | - | NEG -$260.2M | - | 532.5 | 500 | +$416k | +$0 bull / -$206k bear | out (clean 33, ADX 32, RVol 1.7) |
| 13 | **NVDA** | 208.43 | - | **-** | 21 | - | POS +$122.8M | 203.74 | 210 | 200 | +$4.6M | +$56k bull / -$295k bear | out (clean 31, ADX 34, RVol 1.6) |
| 14 | **GOOGL** | 279.24 | - | **-** | 20 | - | NEG -$38.2M | 284.82 | 285 | 290 | +$2.1M | +$0 bull / -$168k bear | out (clean 33, ADX 27, RVol 0.4) |
| 15 | **HOOD** | 85.31 | - | **-** | 20 | - | NEG -$2.5M | - | 90 | 90 | -$472k | +$32k bull / -$27k bear | out (clean 31, ADX 26, RVol 0.9) |
| 16 | **IWM** | 281.83 | - | **-** | 19 | - | NEG -$876.8M | 286.97 | 285 | 270 | -$3.2M | +$170k bull / -$67k bear | out (clean 33, ADX 27, RVol 0.8) |
| 17 | **AAPL** | 330.67 | - | **-** | 19 | - | NEG -$414.5M | 343.85 | 350 | 330 | -$258k | +$390k bull / -$219k bear | out (clean 31, ADX 35, RVol 1.2) |
| 18 | **AMD** | 491.77 | - | **-** | 19 | - | NEG -$67.5M | - | 520 | 500 | +$1.9M | +$93k bull / -$679k bear | out (clean 33, ADX 39, RVol 0.7) |
| 19 | **BABA** | 100.41 | - | **-** | 19 | - | POS +$932k | 100.1 | 102 | 100 | +$173k | - | out (clean 35, ADX 55, RVol 0.6) |
| 20 | **QQQ** | 687.85 | - | **-** | 18 | - | NEG -$4.9B | - | 700 | 680 | -$31.6M | +$0 bull / -$1.1M bear | out (clean 32, ADX 27, RVol 0.6) |
| 21 | **TSLA** | 401.19 | - | **-** | 17 | - | POS +$236.6M | - | 400 | 400 | +$10.7M | +$341k bull / -$561k bear | out (clean 31, ADX 19, RVol 0.5) |
| 22 | **MU** | 857.46 | - | **-** | 16 | - | NEG -$194.1M | - | 900 | 850 | -$3.2M | +$2.3M bull / -$1.4M bear | out (clean 32, ADX 26, RVol 0.5) |
| 23 | **CRM** | 222.71 | - | **-** | 16 | - | NEG -$13.6M | - | 240 | 220 | -$349k | - | out (clean 29, ADX 32, RVol 0.8) |
| 24 | **UBER** | 66.88 | - | **-** | 13 | - | NEG -$8.4M | - | 70 | 65 | -$77k | - | out (clean 29, ADX 18, RVol 0.8) |
| 25 | **NFLX** | 62.35 | - | **-** | 12 | - | NEG -$12.9M | 64.17 | 63 | 60 | -$324k | - | out (clean 28, ADX 27, RVol 0.8) |
| 26 | **SMCI** | 31.70 | - | **-** | 11 | - | POS +$2.1M | - | 34.5 | 30 | -$349k | - | out (clean 35, ADX 29, RVol 0.9) |
| 27 | **AMZN** | 248.00 | - | **-** | 5 | - | POS +$142.9M | 236.06 | 250 | 250 | +$225k | - | out (clean 33, ADX 20, RVol 0.7) |

## Big prints this scan (55)
- **SPY** PUT 760 2026-11-06 (3DTE): 920 @ 8.32 = **+$765k** BUY | vol 1,990 / OI 12,559
- **SPY** PUT 767 2026-11-04 (1DTE): 500 @ 12.11 = **+$606k** BUY | vol 3,514 / OI 18,478
- **NVDA** PUT 207.5 2026-11-09 (6DTE): 300 @ 4.60 = **+$138k** BUY | vol 2,618 / OI 81
- **MU** PUT 860 2026-11-06 (3DTE): 44 @ 26.00 = **+$114k** SELL | vol 1,531 / OI 672
- **SPY** CALL 756 2026-11-04 (1DTE): 256 @ 4.04 = **+$103k** SELL | vol 6,289 / OI 680
- **MU** PUT 840 2026-11-04 (1DTE): 98 @ 9.95 = **+$98k** SELL | vol 6,464 / OI 244
- **MU** CALL 855 2026-11-06 (3DTE): 34 @ 28.48 = **+$97k** BUY | vol 546 / OI 99
- **MU** PUT 855 2026-11-06 (3DTE): 40 @ 23.45 = **+$94k** SELL | vol 686 / OI 740
- **MU** PUT 855 2026-11-06 (3DTE): 38 @ 23.66 = **+$90k** SELL | vol 686 / OI 740
- **MU** CALL 860 2026-11-06 (3DTE): 26 @ 25.95 = **+$67k** BUY | vol 1,675 / OI 194
- **IWM** PUT 280 2026-11-09 (6DTE): 250 @ 2.68 = **+$67k** BUY | vol 316 / OI 213
- **TSLA** CALL 405 2026-11-06 (3DTE): 81 @ 7.63 = **+$62k** BUY | vol 3,366 / OI 3,643
- **MU** CALL 865 2026-11-06 (3DTE): 26 @ 23.50 = **+$61k** BUY | vol 1,527 / OI 185
- **MU** CALL 865 2026-11-06 (3DTE): 25 @ 23.50 = **+$59k** BUY | vol 1,527 / OI 185
- **PLTR** PUT 167.5 2026-11-06 (3DTE): 200 @ 2.77 = **+$55k** BUY | vol 2,954 / OI 1,484

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 756 2026-11-20 (17DTE): 836 traded vs OI 806
- **IWM** PUT 280 2026-11-04 (1DTE): 1,882 traded vs OI 1,843
- **TSLA** PUT 385 2026-11-06 (3DTE): 3,058 traded vs OI 2,975
- **AAPL** PUT 330 2026-11-09 (6DTE): 993 traded vs OI 992
- **META** CALL 647.5 2026-11-04 (1DTE): 529 traded vs OI 74
- **COIN** CALL 155 2026-11-20 (17DTE): 503 traded vs OI 0
- **COIN** CALL 165 2026-11-06 (3DTE): 558 traded vs OI 0
- **COIN** CALL 160 2026-11-20 (17DTE): 519 traded vs OI 0
- **MU** PUT 785 2026-11-04 (1DTE): 503 traded vs OI 241
- **MU** CALL 855 2026-11-06 (3DTE): 546 traded vs OI 99
- **MSTR** PUT 137 2026-11-06 (3DTE): 576 traded vs OI 372

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
