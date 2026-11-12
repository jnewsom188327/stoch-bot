# GEX + FLOW SCAN - Thu Nov 12, 02:10 PM ET
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
Last 1m check 14:10:08 ET, last candle SPY 14:09, QQQ 14:09 | no errors
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
| 1 | **SMCI** | 27.10 | - | **-** | 22 | - | NEG -$906k | - | 28 | 25 | +$1.1M | +$0 bull / -$34k bear | out (clean 34, ADX 24, RVol 1.3) |
| 2 | **MSFT** | 525.44 | - | **-** | 21 | - | POS +$106.7M | 520.72 | 535 | 520 | -$4.6M | +$410k bull / -$243k bear | out (clean 31, ADX 36, RVol 0.8) |
| 3 | **GOOGL** | 301.15 | - | **-** | 21 | - | POS +$136.2M | 287.31 | 300 | 290 | -$5.9M | +$109k bull / -$1.9M bear | out (clean 30, ADX 29, RVol 1.1) |
| 4 | **AAPL** | 356.26 | - | **-** | 19 | - | POS +$1.1B | 341.72 | 360 | 360 | +$4.5M | +$621k bull / -$97k bear | out (clean 29, ADX 30, RVol 0.8) |
| 5 | **SPY** | 758.96 | - | **-** | 18 | - | NEG -$1.4B | 760.84 | 760 | 760 | -$119.3M | +$352k bull / -$2.8M bear | out (clean 31, ADX 19, RVol 0.7) |
| 6 | **AMZN** | 269.31 | - | **-** | 17 | - | POS +$501.9M | - | 270 | 270 | -$7.6M | +$0 bull / -$671k bear | out (clean 29, ADX 11, RVol 0.7) |
| 7 | **ARM** | 200.17 | PINNED between the walls (positive gamma) - chop | **-** | 17 | - | POS +$10.8M | - | 200 | 200 | -$203k | - | out (clean 31, ADX 19, RVol 0.1) |
| 8 | **QQQ** | 689.02 | - | **-** | 16 | - | NEG -$153.5M | 690.22 | 700 | 680 | -$82.3M | +$728k bull / -$564k bear | out (clean 31, ADX 16, RVol 0.4) |
| 9 | **NVDA** | 164.08 | - | **-** | 16 | - | NEG -$193.5M | - | 170 | 160 | -$64.3M | +$2.1M bull / -$910k bear | out (clean 32, ADX 13, RVol 0.9) |
| 10 | **TSLA** | 390.20 | - | **-** | 16 | - | POS +$358.9M | - | 400 | 380 | +$11.6M | +$382k bull / -$188k bear | out (clean 29, ADX 19, RVol 0.2) |
| 11 | **AMD** | 580.09 | - | **-** | 15 | - | POS +$195.8M | - | 600 | 550 | -$18.3M | +$388k bull / -$2.3M bear | out (clean 34, ADX 13, RVol 0.6) |
| 12 | **META** | 623.38 | - | **-** | 15 | - | NEG -$8.7M | 624.69 | 650 | 600 | +$1.2M | +$130k bull / -$36k bear | out (clean 28, ADX 20, RVol 0.4) |
| 13 | **MSTR** | 115.61 | - | **-** | 14 | - | NEG -$32.8M | - | 125 | 110 | -$863k | +$34k bull / +$0 bear | out (clean 28, ADX 12, RVol 0.4) |
| 14 | **MU** | 791.90 | - | **-** | 13 | - | POS +$101.9M | - | 800 | 800 | +$4.4M | +$862k bull / -$391k bear | out (clean 31, ADX 13, RVol 0.4) |
| 15 | **BABA** | 94.83 | - | **-** | 9 | - | NEG -$18.3M | - | 100 | 100 | +$316k | - | out (clean 29, ADX 16, RVol 0.9) |
| 16 | **IWM** | 279.47 | - | **-** | 8 | - | NEG -$1.2B | 282.53 | 285 | 275 | -$311k | - | out (clean 34, ADX 34, RVol 0.7) |
| 17 | **SMH** | 501.20 | - | **-** | 7 | - | NEG -$95.3M | - | 500 | 500 | -$1.6M | - | out (clean 30, ADX 15, RVol 0.7) |
| 18 | **NFLX** | 63.69 | - | **-** | 7 | - | NEG -$6.8M | 64.03 | 65 | 65 | -$201k | - | out (clean 28, ADX 13, RVol 0.5) |
| 19 | **AVGO** | 364.68 | - | **-** | 6 | - | POS +$130.9M | - | 380 | 350 | +$8.4M | - | out (clean 34, ADX 10, RVol 0.7) |
| 20 | **UBER** | 69.58 | - | **-** | 6 | - | POS +$14.6M | 68.39 | 70 | 70 | -$53k | - | out (clean 31, ADX 14, RVol 0.3) |
| 21 | **CRM** | 217.59 | - | **-** | 6 | - | NEG -$7.8M | 227.36 | 220 | 220 | +$41k | - | out (clean 28, ADX 19, RVol 0.1) |
| 22 | **PLTR** | 172.30 | - | **-** | 5 | - | POS +$93.3M | - | 170 | 170 | -$412k | - | out (clean 28, ADX 11, RVol 0.4) |
| 23 | **DELL** | 373.58 | - | **-** | 5 | - | POS +$5.1M | - | 360 | 380 | +$553k | - | out (clean 37, ADX 23, RVol 0.2) |
| 24 | **ORCL** | 127.46 | - | **-** | 5 | - | POS +$6.3M | 124.33 | 130 | 125 | -$611k | - | out (clean 30, ADX 9, RVol 0.4) |
| 25 | **SHOP** | 147.38 | - | **-** | 5 | - | POS +$4.0M | 143.94 | 150 | 140 | +$406 | - | out (clean 31, ADX 26, RVol 0.2) |
| 26 | **COIN** | 132.10 | - | **-** | 4 | - | POS +$3.0M | 131.37 | 137 | 135 | +$88k | - | out (clean 30, ADX 13, RVol 0.5) |
| 27 | **HOOD** | 82.88 | - | **-** | 4 | - | POS +$12.0M | 80.03 | 85 | 80 | -$40k | - | out (clean 34, ADX 14, RVol 0.8) |

## Big prints this scan (111)
- **SPY** PUT 766 2026-11-16 (4DTE): 2,000 @ 8.00 = **+$1.6M** BUY | vol 12,060 / OI 116
- **SPY** PUT 763 2026-11-16 (4DTE): 1,493 @ 6.00 = **+$896k** BUY | vol 25,963 / OI 216
- **GOOGL** CALL 292.5 2026-11-13 (1DTE): 713 @ 9.13 = **+$651k** SELL | vol 2,473 / OI 6,133
- **GOOGL** CALL 292.5 2026-11-13 (1DTE): 712 @ 9.13 = **+$650k** SELL | vol 2,473 / OI 6,133
- **NVDA** PUT 160 2026-11-18 (6DTE): 1,000 @ 6.05 = **+$605k** SELL | vol 12,344 / OI 3,836
- **SPY** PUT 763 2026-11-16 (4DTE): 500 @ 6.00 = **+$300k** BUY | vol 25,963 / OI 216
- **GOOGL** CALL 300 2026-11-13 (1DTE): 713 @ 3.32 = **+$237k** SELL | vol 48,518 / OI 8,687
- **GOOGL** CALL 300 2026-11-13 (1DTE): 712 @ 3.32 = **+$236k** SELL | vol 48,518 / OI 8,687
- **NVDA** PUT 170 2026-11-13 (1DTE): 304 @ 6.81 = **+$207k** BUY | vol 23,848 / OI 14,967
- **QQQ** PUT 692 2026-11-16 (4DTE): 200 @ 8.02 = **+$160k** BUY | vol 2,086 / OI 112
- **QQQ** PUT 692 2026-11-16 (4DTE): 200 @ 7.99 = **+$160k** BUY | vol 2,086 / OI 112
- **NVDA** PUT 170 2026-11-13 (1DTE): 219 @ 6.81 = **+$149k** BUY | vol 23,848 / OI 14,967
- **NVDA** PUT 170 2026-11-13 (1DTE): 218 @ 6.81 = **+$148k** BUY | vol 23,848 / OI 14,967
- **AMZN** PUT 267.5 2026-11-13 (1DTE): 921 @ 1.58 = **+$146k** BUY | vol 15,307 / OI 1,264
- **AMZN** PUT 267.5 2026-11-13 (1DTE): 876 @ 1.62 = **+$142k** BUY | vol 15,307 / OI 1,264

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 763 2026-11-18 (6DTE): 1,021 traded vs OI 738
- **SPY** CALL 791 2026-11-18 (6DTE): 1,347 traded vs OI 112
- **SPY** PUT 736 2026-11-23 (11DTE): 508 traded vs OI 142
- **SPY** PUT 760 2026-11-18 (6DTE): 758 traded vs OI 757
- **QQQ** PUT 653 2026-11-13 (1DTE): 556 traded vs OI 553
- **QQQ** PUT 683 2026-11-19 (7DTE): 500 traded vs OI 13
- **IWM** PUT 284 2026-11-12 (0DTE): 595 traded vs OI 451
- **IWM** CALL 281 2026-11-19 (7DTE): 594 traded vs OI 92
- **AAPL** PUT 355 2026-11-23 (11DTE): 3,252 traded vs OI 12
- **AVGO** PUT 350 2026-12-04 (22DTE): 2,055 traded vs OI 126
- **SMCI** CALL 28 2026-12-04 (22DTE): 500 traded vs OI 167
- **ARM** PUT 197.5 2026-11-13 (1DTE): 615 traded vs OI 289

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
