# GEX + FLOW SCAN - Thu Nov 12, 01:20 PM ET
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
Last 1m check 13:20:08 ET, last candle SPY 13:19, QQQ 13:19 | no errors
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
| 1 | **DELL** | 377.60 | TREND (flow not with it) | **CALLS** | 37 | none: 31 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (6 contracts' greeks worked out here) | POS +$4.3M | - | 360 | 380 | -$249k | +$207k bull / +$0 bear | LONG (clean 36, ADX 30, RVol 1.2) |
| 2 | **GOOGL** | 301.92 | - | **-** | 24 | - | POS +$142.2M | 288.21 | 300 | 290 | -$5.2M | +$219k bull / +$0 bear | out (clean 30, ADX 42, RVol 1.3) |
| 3 | **AAPL** | 355.64 | - | **-** | 21 | - | POS +$1.1B | 340.2 | 360 | 350 | +$5.2M | +$56k bull / -$47k bear | out (clean 29, ADX 39, RVol 0.6) |
| 4 | **MSFT** | 526.98 | - | **-** | 20 | - | POS +$149.0M | 520.5 | 535 | 520 | -$4.8M | +$70k bull / +$0 bear | out (clean 30, ADX 25, RVol 0.4) |
| 5 | **AMZN** | 269.39 | PINNED between the walls (positive gamma) - chop | **-** | 19 | - | POS +$505.2M | - | 270 | 270 | -$6.6M | - | out (clean 30, ADX 10, RVol 0.6) |
| 6 | **ARM** | 200.45 | PINNED between the walls (positive gamma) - chop | **-** | 18 | - | POS +$11.4M | - | 200 | 200 | -$260k | - | out (clean 31, ADX 21, RVol 0.1) |
| 7 | **NVDA** | 165.59 | - | **-** | 17 | - | NEG -$182.5M | - | 170 | 160 | -$81.5M | +$1.4M bull / -$2.5M bear | out (clean 31, ADX 14, RVol 0.9) |
| 8 | **SPY** | 760.51 | - | **-** | 16 | - | NEG -$660.8M | 761.17 | 760 | 760 | -$126.0M | +$603k bull / +$0 bear | out (clean 30, ADX 12, RVol 0.3) |
| 9 | **SMCI** | 26.84 | - | **-** | 16 | - | NEG -$971k | - | 28 | 25 | +$1.6M | - | out (clean 34, ADX 38, RVol 0.8) |
| 10 | **MSTR** | 116.77 | - | **-** | 16 | - | NEG -$30.6M | - | 125 | 110 | -$1.7M | +$38k bull / -$31k bear | out (clean 28, ADX 10, RVol 0.6) |
| 11 | **ORCL** | 127.36 | - | **-** | 16 | - | POS +$10.2M | 121.05 | 130 | 125 | -$496k | +$119k bull / +$0 bear | out (clean 30, ADX 13, RVol 0.3) |
| 12 | **QQQ** | 690.77 | - | **-** | 15 | - | NEG -$24.2M | 690.87 | 700 | 680 | -$84.8M | +$2.0M bull / -$524k bear | out (clean 30, ADX 12, RVol 0.4) |
| 13 | **TSLA** | 391.46 | - | **-** | 15 | - | POS +$369.0M | - | 400 | 380 | +$10.3M | +$74k bull / +$0 bear | out (clean 28, ADX 15, RVol 0.2) |
| 14 | **AMD** | 582.71 | - | **-** | 15 | - | POS +$195.9M | - | 600 | 550 | -$17.9M | +$2.1M bull / -$514k bear | out (clean 34, ADX 16, RVol 0.4) |
| 15 | **META** | 625.66 | - | **-** | 15 | - | POS +$3.4M | 624.69 | 650 | 600 | +$1.3M | +$85k bull / +$0 bear | out (clean 28, ADX 18, RVol 0.4) |
| 16 | **IWM** | 280.28 | - | **-** | 14 | - | NEG -$949.6M | 282.57 | 285 | 275 | -$83k | +$64k bull / +$0 bear | out (clean 32, ADX 19, RVol 0.3) |
| 17 | **MU** | 794.39 | - | **-** | 14 | - | POS +$103.2M | - | 800 | 800 | +$7.3M | +$1.5M bull / -$1.1M bear | out (clean 31, ADX 16, RVol 0.3) |
| 18 | **BABA** | 94.80 | - | **-** | 12 | - | NEG -$18.8M | - | 100 | 100 | +$356k | - | out (clean 28, ADX 24, RVol 0.9) |
| 19 | **UBER** | 69.61 | - | **-** | 8 | - | POS +$14.2M | 68.4 | 70 | 70 | -$81k | - | out (clean 31, ADX 14, RVol 0.2) |
| 20 | **NFLX** | 63.63 | - | **-** | 7 | - | NEG -$7.1M | 63.97 | 65 | 65 | -$168k | - | out (clean 28, ADX 16, RVol 0.5) |
| 21 | **SMH** | 503.67 | - | **-** | 6 | - | NEG -$89.6M | - | 500 | 500 | -$1.7M | - | out (clean 30, ADX 14, RVol 0.4) |
| 22 | **AVGO** | 364.20 | - | **-** | 6 | - | POS +$133.4M | - | 350 | 350 | +$8.5M | - | out (clean 34, ADX 13, RVol 0.5) |
| 23 | **CRM** | 217.83 | - | **-** | 6 | - | NEG -$8.0M | 228.27 | 220 | 220 | +$29k | - | out (clean 28, ADX 24, RVol 0.1) |
| 24 | **PLTR** | 172.20 | - | **-** | 5 | - | POS +$88.8M | - | 170 | 170 | -$365k | - | out (clean 28, ADX 16, RVol 0.5) |
| 25 | **COIN** | 133.07 | - | **-** | 4 | - | POS +$6.3M | 131.4 | 137 | 135 | +$56k | - | out (clean 29, ADX 12, RVol 0.4) |
| 26 | **SHOP** | 147.90 | - | **-** | 4 | - | POS +$4.6M | 144.22 | 150 | 140 | -$605 | - | out (clean 30, ADX 19, RVol 0.3) |
| 27 | **HOOD** | 83.28 | - | **-** | 3 | - | POS +$13.4M | 79.99 | 85 | 80 | -$58k | - | out (clean 34, ADX 12, RVol 0.4) |

## Big prints this scan (57)
- **SPY** PUT 764 2026-11-18 (6DTE): 498 @ 6.59 = **+$328k** SELL | vol 557 / OI 20
- **QQQ** PUT 684 2026-11-13 (1DTE): 1,000 @ 2.04 = **+$204k** BUY | vol 8,451 / OI 349
- **QQQ** PUT 691 2026-11-12 (0DTE): 1,207 @ 1.61 = **+$194k** BUY | vol 116,061 / OI 46
- **MU** PUT 785 2026-11-13 (1DTE): 150 @ 11.00 = **+$165k** BUY | vol 7,826 / OI 256
- **SPY** CALL 755 2026-11-12 (0DTE): 261 @ 5.70 = **+$149k** BUY | vol 40,576 / OI 1,837
- **QQQ** CALL 664 2026-11-12 (0DTE): 51 @ 26.50 = **+$135k** MID | vol 129 / OI 315
- **AMD** CALL 557.5 2026-11-13 (1DTE): 50 @ 26.07 = **+$130k** SELL | vol 1,342 / OI 579
- **SPY** CALL 755 2026-11-12 (0DTE): 222 @ 5.69 = **+$126k** BUY | vol 40,576 / OI 1,837
- **QQQ** PUT 680 2026-11-13 (1DTE): 1,000 @ 1.26 = **+$126k** BUY | vol 33,508 / OI 5,045
- **NVDA** CALL 165 2026-11-13 (1DTE): 325 @ 3.60 = **+$117k** SELL | vol 212,799 / OI 2,999
- **DELL** CALL 370 2026-11-13 (1DTE): 80 @ 14.50 = **+$116k** BUY | vol 1,531 / OI 623
- **QQQ** CALL 691 2026-11-12 (0DTE): 750 @ 1.44 = **+$108k** BUY | vol 160,785 / OI 387
- **QQQ** CALL 691 2026-11-12 (0DTE): 703 @ 1.49 = **+$105k** BUY | vol 160,785 / OI 387
- **AMD** CALL 585 2026-11-18 (6DTE): 50 @ 20.00 = **+$100k** SELL | vol 233 / OI 39
- **NVDA** PUT 160 2026-11-13 (1DTE): 500 @ 1.66 = **+$83k** BUY | vol 206,302 / OI 24,121

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 764 2026-11-18 (6DTE): 2,115 traded vs OI 2,112
- **SPY** PUT 760 2026-11-13 (1DTE): 29,111 traded vs OI 27,552
- **SPY** CALL 761 2026-11-18 (6DTE): 523 traded vs OI 480
- **SPY** PUT 770 2026-11-12 (0DTE): 507 traded vs OI 18
- **SPY** PUT 761 2026-12-11 (29DTE): 531 traded vs OI 304
- **IWM** PUT 279 2026-11-17 (5DTE): 860 traded vs OI 351
- **AMD** CALL 580 2026-11-20 (8DTE): 3,415 traded vs OI 3,413
- **AMZN** PUT 257.5 2026-11-13 (1DTE): 1,332 traded vs OI 1,307
- **GOOGL** CALL 320 2026-11-16 (4DTE): 595 traded vs OI 370
- **MU** PUT 765 2026-11-16 (4DTE): 501 traded vs OI 166
- **MU** PUT 810 2026-11-13 (1DTE): 508 traded vs OI 391
- **BABA** CALL 99 2026-11-13 (1DTE): 502 traded vs OI 123

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
