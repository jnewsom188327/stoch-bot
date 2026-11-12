# GEX + FLOW SCAN - Thu Nov 12, 01:10 PM ET
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
Last 1m check 13:10:08 ET, last candle SPY 13:09, QQQ 13:09 | no errors
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
| 1 | **DELL** | 377.46 | TREND (flow not with it) | **CALLS** | 41 | none: 31 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (6 contracts' greeks worked out here) | POS +$4.7M | - | 360 | 380 | -$270k | +$43k bull / +$0 bear | LONG (clean 36, ADX 30, RVol 1.7) |
| 2 | **GOOGL** | 301.81 | - | **-** | 25 | - | POS +$142.9M | 288.45 | 300 | 290 | -$6.2M | +$98k bull / -$41k bear | out (clean 30, ADX 44, RVol 1.3) |
| 3 | **AAPL** | 355.52 | - | **-** | 21 | - | POS +$1.1B | 339.45 | 360 | 350 | +$5.1M | +$95k bull / -$26k bear | out (clean 29, ADX 37, RVol 0.6) |
| 4 | **MSFT** | 528.38 | - | **-** | 20 | - | POS +$198.8M | 520.69 | 535 | 520 | -$4.9M | +$70k bull / +$0 bear | out (clean 30, ADX 27, RVol 0.4) |
| 5 | **NVDA** | 165.40 | - | **-** | 18 | - | NEG -$185.6M | - | 170 | 160 | -$79.0M | +$2.0M bull / -$1.9M bear | out (clean 32, ADX 16, RVol 0.9) |
| 6 | **ARM** | 200.01 | PINNED between the walls (positive gamma) - chop | **-** | 18 | - | POS +$10.4M | - | 200 | 200 | -$263k | - | out (clean 31, ADX 21, RVol 0.1) |
| 7 | **AVGO** | 363.20 | - | **-** | 17 | - | POS +$133.2M | - | 350 | 350 | +$8.4M | +$274k bull / +$0 bear | out (clean 34, ADX 15, RVol 0.6) |
| 8 | **SMCI** | 26.86 | - | **-** | 17 | - | NEG -$1.0M | - | 28 | 25 | +$1.6M | - | out (clean 34, ADX 39, RVol 1.0) |
| 9 | **CRM** | 218.36 | - | **-** | 17 | - | NEG -$8.2M | - | 220 | 220 | +$27k | +$34k bull / +$0 bear | out (clean 28, ADX 26, RVol 0.1) |
| 10 | **SPY** | 760.40 | - | **-** | 16 | - | NEG -$712.5M | 761.01 | 760 | 760 | -$131.4M | +$223k bull / +$0 bear | out (clean 31, ADX 12, RVol 0.3) |
| 11 | **MSTR** | 116.86 | - | **-** | 16 | - | NEG -$29.4M | - | 125 | 110 | -$1.7M | +$0 bull / -$71k bear | out (clean 28, ADX 12, RVol 0.5) |
| 12 | **QQQ** | 690.24 | - | **-** | 15 | - | NEG -$95.2M | 690.51 | 700 | 680 | -$86.1M | +$1.1M bull / -$376k bear | out (clean 30, ADX 12, RVol 0.4) |
| 13 | **TSLA** | 391.46 | - | **-** | 15 | - | POS +$371.4M | - | 400 | 380 | +$10.5M | +$149k bull / -$111k bear | out (clean 28, ADX 14, RVol 0.3) |
| 14 | **AMD** | 578.67 | - | **-** | 15 | - | POS +$195.5M | - | 600 | 550 | -$17.5M | +$1.6M bull / -$2.9M bear | out (clean 34, ADX 18, RVol 0.4) |
| 15 | **META** | 624.96 | - | **-** | 15 | - | POS +$2.2M | 624.11 | 650 | 600 | +$1.2M | +$57k bull / -$79k bear | out (clean 28, ADX 18, RVol 0.4) |
| 16 | **IWM** | 280.36 | - | **-** | 14 | - | NEG -$1.0B | 282.65 | 285 | 275 | -$487k | +$64k bull / +$0 bear | out (clean 32, ADX 16, RVol 0.3) |
| 17 | **MU** | 792.03 | - | **-** | 14 | - | POS +$104.9M | - | 800 | 800 | +$5.9M | +$1.3M bull / -$2.0M bear | out (clean 31, ADX 17, RVol 0.4) |
| 18 | **BABA** | 94.75 | - | **-** | 12 | - | NEG -$16.1M | - | 100 | 95 | +$343k | - | out (clean 28, ADX 27, RVol 0.8) |
| 19 | **NFLX** | 63.73 | - | **-** | 8 | - | NEG -$4.6M | 63.94 | 65 | 65 | -$204k | - | out (clean 28, ADX 16, RVol 0.5) |
| 20 | **UBER** | 69.60 | - | **-** | 8 | - | POS +$13.2M | 68.42 | 70 | 70 | -$82k | - | out (clean 31, ADX 13, RVol 0.2) |
| 21 | **SMH** | 502.21 | - | **-** | 7 | - | NEG -$101.9M | - | 500 | 500 | -$1.7M | - | out (clean 30, ADX 15, RVol 0.4) |
| 22 | **AMZN** | 268.95 | - | **-** | 6 | - | POS +$506.0M | - | 270 | 270 | -$6.5M | - | out (clean 30, ADX 10, RVol 0.6) |
| 23 | **PLTR** | 172.07 | - | **-** | 6 | - | POS +$94.9M | - | 170 | 170 | -$451k | - | out (clean 28, ADX 17, RVol 0.5) |
| 24 | **ORCL** | 127.33 | - | **-** | 6 | - | POS +$11.6M | 122.03 | 130 | 125 | -$512k | - | out (clean 30, ADX 15, RVol 0.4) |
| 25 | **COIN** | 133.15 | - | **-** | 4 | - | POS +$6.7M | 131.41 | 137 | 135 | +$50k | - | out (clean 29, ADX 13, RVol 0.4) |
| 26 | **HOOD** | 83.22 | - | **-** | 4 | - | POS +$11.9M | 80.25 | 85 | 80 | -$82k | - | out (clean 34, ADX 12, RVol 0.3) |
| 27 | **SHOP** | 148.25 | - | **-** | 4 | - | POS +$3.4M | 144.7 | 150 | 140 | -$605 | - | out (clean 30, ADX 17, RVol 0.3) |

## Big prints this scan (70)
- **NVDA** CALL 160 2026-11-16 (4DTE): 500 @ 8.07 = **+$404k** BUY | vol 17,691 / OI 766
- **NVDA** CALL 160 2026-11-13 (1DTE): 500 @ 6.82 = **+$341k** SELL | vol 130,322 / OI 2,015
- **QQQ** PUT 693 2026-11-12 (0DTE): 1,358 @ 1.97 = **+$268k** SELL | vol 46,453 / OI 38
- **NVDA** CALL 167.5 2026-11-13 (1DTE): 830 @ 2.63 = **+$218k** BUY | vol 116,428 / OI 6,311
- **QQQ** CALL 691 2026-11-12 (0DTE): 664 @ 2.40 = **+$159k** BUY | vol 149,759 / OI 387
- **NVDA** CALL 170 2026-11-16 (4DTE): 500 @ 2.83 = **+$142k** SELL | vol 37,662 / OI 5,341
- **MU** CALL 820 2026-11-18 (6DTE): 62 @ 20.15 = **+$125k** BUY | vol 787 / OI 81
- **QQQ** PUT 692 2026-11-12 (0DTE): 1,000 @ 1.23 = **+$123k** SELL | vol 70,922 / OI 92
- **NVDA** PUT 162.5 2026-11-13 (1DTE): 440 @ 2.35 = **+$103k** BUY | vol 108,972 / OI 20,581
- **AMD** CALL 565 2026-11-18 (6DTE): 31 @ 33.14 = **+$103k** BUY | vol 228 / OI 98
- **AMD** CALL 590 2026-11-13 (1DTE): 100 @ 9.70 = **+$97k** BUY | vol 21,838 / OI 1,196
- **AMD** CALL 575 2026-11-18 (6DTE): 31 @ 27.18 = **+$84k** BUY | vol 511 / OI 54
- **MU** CALL 800 2026-11-13 (1DTE): 60 @ 13.75 = **+$82k** BUY | vol 23,937 / OI 5,964
- **NVDA** CALL 170 2026-11-13 (1DTE): 500 @ 1.63 = **+$82k** SELL | vol 181,026 / OI 11,191
- **NVDA** PUT 165 2026-11-13 (1DTE): 228 @ 3.35 = **+$76k** MID | vol 86,635 / OI 19,300

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 765 2026-11-17 (5DTE): 722 traded vs OI 720
- **SPY** CALL 760 2026-11-18 (6DTE): 896 traded vs OI 863
- **SPY** PUT 762 2026-11-18 (6DTE): 523 traded vs OI 25
- **QQQ** CALL 705 2026-11-17 (5DTE): 690 traded vs OI 677
- **QQQ** PUT 663 2026-11-16 (4DTE): 511 traded vs OI 273
- **NVDA** PUT 155 2026-12-04 (22DTE): 4,820 traded vs OI 4,251
- **AAPL** PUT 355 2026-12-04 (22DTE): 542 traded vs OI 244
- **AMD** CALL 575 2026-11-18 (6DTE): 511 traded vs OI 54
- **MSFT** CALL 550 2026-11-18 (6DTE): 566 traded vs OI 111
- **AVGO** CALL 397.5 2026-11-13 (1DTE): 574 traded vs OI 270
- **DELL** PUT 370 2026-11-13 (1DTE): 555 traded vs OI 183
- **DELL** CALL 365 2026-11-13 (1DTE): 505 traded vs OI 274
- **MU** CALL 850 2026-11-16 (4DTE): 970 traded vs OI 938
- **ARM** CALL 220 2026-11-13 (1DTE): 505 traded vs OI 0
- **BABA** CALL 102 2026-11-20 (8DTE): 513 traded vs OI 281

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
