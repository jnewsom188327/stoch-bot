# GEX + FLOW SCAN - Thu Nov 12, 01:50 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (5)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:35 | **SPY** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/12 754P | 0.59 | 0.17 | +10% (1m) | **-71%** (done) | +70% | 755 |
| 09:50 | **HOOD** | **PUTS** | TREND + FLOW | 11/13 79P | 0.55 | 0.36 | +5% (19m) | **-35%** (done) | +92% | 80 |
| 09:45 | **ORCL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/13 130C | 0.75 | 0.72 | +4% (60m) | **-4%** (done) | +59% | 126.9 |
| 09:45 | **SMCI** | **PUTS** | TREND + FLOW | 11/13 27P | 0.42 | 0.23 | -5% (6m) | **-45%** (done) | +57% | 27 |
| 09:45 | **SPY** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/12 753P | 0.79 | 0.31 | +23% (18m) | **-61%** (done) | +51% | 754.88 |

## 1m RULES on SPY / QQQ - loose (1 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 13:50:08 ET, last candle SPY 13:49, QQQ 13:49 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 10:03 | SPY | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |

## Flow surges NOT fired - price disagreed (7 today, last 5)
- 12:00 SMCI CALLS: price -0.27 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 11:55 SMCI CALLS: price -0.04 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 11:50 SMCI CALLS: price -0.48 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 11:45 SMCI CALLS: price -0.74 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:30 IWM CALLS: price -0.04 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **GOOGL** | 301.20 | - | **-** | 21 | - | POS +$136.6M | 287.49 | 300 | 290 | -$4.7M | +$103k bull / -$813k bear | out (clean 30, ADX 36, RVol 1.0) |
| 2 | **AAPL** | 355.93 | - | **-** | 20 | - | POS +$1.1B | 340.75 | 360 | 360 | +$4.9M | +$28k bull / -$311k bear | out (clean 29, ADX 36, RVol 0.6) |
| 3 | **MSFT** | 523.69 | - | **-** | 20 | - | POS +$62.9M | 520.49 | 535 | 520 | -$3.8M | +$614k bull / -$243k bear | out (clean 31, ADX 31, RVol 0.8) |
| 4 | **ARM** | 200.47 | PINNED between the walls (positive gamma) - chop | **-** | 17 | - | POS +$10.9M | - | 200 | 200 | -$227k | - | out (clean 31, ADX 16, RVol 0.1) |
| 5 | **SPY** | 759.24 | - | **-** | 16 | - | NEG -$1.6B | 760.76 | 760 | 760 | -$127.7M | +$0 bull / -$280k bear | out (clean 31, ADX 12, RVol 0.4) |
| 6 | **NVDA** | 164.69 | - | **-** | 16 | - | NEG -$190.1M | - | 170 | 160 | -$74.0M | +$2.4M bull / -$636k bear | out (clean 32, ADX 11, RVol 0.7) |
| 7 | **AVGO** | 364.03 | - | **-** | 16 | - | POS +$134.8M | - | 350 | 350 | +$8.9M | +$220k bull / +$0 bear | out (clean 34, ADX 11, RVol 0.5) |
| 8 | **DELL** | 374.78 | - | **-** | 16 | - | POS +$4.9M | - | 360 | 380 | +$375k | +$50k bull / +$0 bear | out (clean 37, ADX 28, RVol 0.4) |
| 9 | **TSLA** | 390.86 | - | **-** | 15 | - | POS +$364.8M | - | 400 | 380 | +$10.5M | +$0 bull / -$215k bear | out (clean 28, ADX 14, RVol 0.2) |
| 10 | **META** | 624.25 | - | **-** | 15 | - | NEG -$4.5M | 624.18 | 650 | 600 | +$2.0M | +$39k bull / +$0 bear | out (clean 28, ADX 17, RVol 0.4) |
| 11 | **QQQ** | 689.25 | - | **-** | 14 | - | NEG -$422.6M | 690.7 | 700 | 680 | -$79.9M | +$1.6M bull / -$127k bear | out (clean 30, ADX 11, RVol 0.2) |
| 12 | **AMD** | 578.64 | - | **-** | 14 | - | POS +$196.8M | - | 600 | 550 | -$15.5M | +$1.6M bull / -$646k bear | out (clean 34, ADX 14, RVol 0.4) |
| 13 | **MU** | 792.08 | - | **-** | 14 | - | POS +$103.4M | - | 800 | 800 | +$6.1M | +$891k bull / -$95k bear | out (clean 31, ADX 15, RVol 0.3) |
| 14 | **SMCI** | 27.00 | - | **-** | 11 | - | NEG -$787k | - | 28 | 25 | +$1.1M | - | out (clean 34, ADX 30, RVol 0.6) |
| 15 | **UBER** | 69.80 | - | **-** | 9 | - | POS +$15.9M | 68.39 | 70 | 70 | -$73k | - | out (clean 31, ADX 17, RVol 0.5) |
| 16 | **BABA** | 94.78 | - | **-** | 9 | - | NEG -$15.7M | - | 100 | 95 | +$307k | - | out (clean 29, ADX 17, RVol 0.8) |
| 17 | **NFLX** | 63.70 | - | **-** | 7 | - | NEG -$4.5M | 63.88 | 65 | 65 | -$194k | - | out (clean 28, ADX 15, RVol 0.5) |
| 18 | **IWM** | 279.93 | - | **-** | 6 | - | NEG -$1.2B | 282.62 | 285 | 275 | -$340k | - | out (clean 33, ADX 25, RVol 0.8) |
| 19 | **SMH** | 502.39 | - | **-** | 6 | - | NEG -$99.9M | 531.89 | 500 | 500 | -$1.7M | - | out (clean 30, ADX 11, RVol 0.3) |
| 20 | **AMZN** | 268.97 | - | **-** | 6 | - | POS +$502.5M | - | 270 | 270 | -$6.7M | - | out (clean 29, ADX 9, RVol 0.5) |
| 21 | **CRM** | 217.59 | - | **-** | 6 | - | NEG -$8.6M | 227.96 | 220 | 220 | +$41k | - | out (clean 28, ADX 19, RVol 0.2) |
| 22 | **MSTR** | 116.24 | - | **-** | 5 | - | NEG -$33.1M | - | 125 | 110 | -$1.5M | - | out (clean 28, ADX 10, RVol 0.3) |
| 23 | **ORCL** | 127.22 | - | **-** | 5 | - | POS +$10.8M | 122.19 | 130 | 125 | -$562k | - | out (clean 30, ADX 11, RVol 0.2) |
| 24 | **SHOP** | 147.38 | - | **-** | 5 | - | POS +$3.8M | 144.32 | 150 | 140 | -$1k | - | out (clean 30, ADX 23, RVol 0.3) |
| 25 | **PLTR** | 171.94 | - | **-** | 4 | - | POS +$92.3M | - | 170 | 170 | -$275k | - | out (clean 28, ADX 12, RVol 0.5) |
| 26 | **COIN** | 132.75 | - | **-** | 4 | - | POS +$3.9M | 131.35 | 137 | 135 | +$54k | - | out (clean 29, ADX 10, RVol 0.5) |
| 27 | **HOOD** | 83.15 | - | **-** | 4 | - | POS +$13.0M | 80.07 | 85 | 80 | -$62k | - | out (clean 34, ADX 10, RVol 0.7) |

## Big prints this scan (53)
- **MU** CALL 780 2026-11-13 (1DTE): 100 @ 25.00 = **+$250k** BUY | vol 14,617 / OI 1,424
- **QQQ** CALL 690 2026-11-12 (0DTE): 999 @ 1.92 = **+$192k** BUY | vol 242,826 / OI 1,788
- **QQQ** CALL 688 2026-11-12 (0DTE): 327 @ 3.33 = **+$109k** BUY | vol 102,579 / OI 896
- **MSFT** CALL 527.5 2026-11-13 (1DTE): 344 @ 3.00 = **+$103k** BUY | vol 9,437 / OI 503
- **MSFT** CALL 527.5 2026-11-13 (1DTE): 304 @ 3.00 = **+$91k** BUY | vol 9,437 / OI 503
- **MSFT** CALL 535 2026-11-18 (6DTE): 270 @ 3.30 = **+$89k** MID | vol 566 / OI 316
- **MU** CALL 797.5 2026-11-13 (1DTE): 50 @ 14.50 = **+$72k** BUY | vol 3,414 / OI 194
- **AMD** CALL 582.5 2026-11-13 (1DTE): 50 @ 12.19 = **+$61k** BUY | vol 4,870 / OI 413
- **MSFT** CALL 527.5 2026-11-13 (1DTE): 178 @ 3.00 = **+$53k** BUY | vol 9,437 / OI 503
- **NVDA** PUT 165 2026-11-13 (1DTE): 180 @ 2.90 = **+$52k** SELL | vol 97,275 / OI 19,300
- **AMD** PUT 580 2026-11-13 (1DTE): 50 @ 10.18 = **+$51k** SELL | vol 9,470 / OI 4
- **MSFT** PUT 520 2026-11-16 (4DTE): 150 @ 3.35 = **+$50k** SELL | vol 1,586 / OI 493
- **MSFT** PUT 525 2026-11-13 (1DTE): 100 @ 4.45 = **+$44k** SELL | vol 4,892 / OI 1,167
- **MSFT** CALL 527.5 2026-11-13 (1DTE): 138 @ 3.00 = **+$41k** BUY | vol 9,437 / OI 503
- **NVDA** PUT 165 2026-11-13 (1DTE): 139 @ 2.95 = **+$41k** SELL | vol 97,275 / OI 19,300

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 770 2026-11-16 (4DTE): 6,544 traded vs OI 6,528
- **SPY** PUT 744 2026-11-16 (4DTE): 697 traded vs OI 681
- **QQQ** CALL 693 2026-11-18 (6DTE): 505 traded vs OI 141
- **META** CALL 667.5 2026-11-13 (1DTE): 545 traded vs OI 354
- **MSFT** PUT 522.5 2026-11-16 (4DTE): 538 traded vs OI 90
- **MSFT** PUT 505 2026-11-13 (1DTE): 1,762 traded vs OI 1,066
- **DELL** PUT 352.5 2026-11-13 (1DTE): 501 traded vs OI 104
- **MU** CALL 790 2026-11-20 (8DTE): 755 traded vs OI 705

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
