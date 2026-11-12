# GEX + FLOW SCAN - Thu Nov 12, 12:40 PM ET
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
Last 1m check 12:40:08 ET, last candle SPY 12:39, QQQ 12:39 | no errors
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
| 1 | **AMZN** | 269.65 | PINNED between the walls (positive gamma) - chop | **-** | 31 | - | POS +$502.5M | - | 270 | 270 | -$6.7M | +$155k bull / +$0 bear | out (clean 30, ADX 10, RVol 0.8) |
| 2 | **SPY** | 761.30 | PINNED between the walls (positive gamma) - chop | **-** | 29 | - | POS +$127.6M | 761.36 | 760 | 760 | -$138.2M | +$100k bull / -$117k bear | out (clean 31, ADX 13, RVol 0.3) |
| 3 | **GOOGL** | 301.43 | - | **-** | 24 | - | POS +$141.2M | 287.93 | 300 | 290 | -$6.4M | +$0 bull / -$32k bear | out (clean 30, ADX 41, RVol 0.8) |
| 4 | **NVDA** | 165.06 | - | **-** | 19 | - | NEG -$182.3M | - | 170 | 160 | -$79.4M | +$1.3M bull / -$1.7M bear | out (clean 32, ADX 22, RVol 0.8) |
| 5 | **SMCI** | 26.70 | - | **-** | 19 | - | NEG -$1.1M | - | 28 | 25 | +$1.5M | - | out (clean 34, ADX 47, RVol 1.5) |
| 6 | **AAPL** | 355.72 | - | **-** | 18 | - | POS +$1.1B | 340.16 | 360 | 360 | +$3.6M | +$812k bull / +$0 bear | out (clean 28, ADX 27, RVol 0.7) |
| 7 | **PLTR** | 172.63 | - | **-** | 18 | - | POS +$91.3M | - | 170 | 170 | -$642k | +$29k bull / +$0 bear | out (clean 28, ADX 18, RVol 0.4) |
| 8 | **AMD** | 580.52 | - | **-** | 17 | - | POS +$194.5M | - | 600 | 550 | -$15.9M | +$3.0M bull / -$5.3M bear | out (clean 35, ADX 24, RVol 0.7) |
| 9 | **AVGO** | 365.04 | - | **-** | 17 | - | POS +$130.9M | - | 380 | 350 | +$7.1M | +$0 bull / -$28k bear | out (clean 35, ADX 18, RVol 0.6) |
| 10 | **DELL** | 375.48 | - | **-** | 17 | - | POS +$4.7M | - | 360 | 380 | -$535k | +$0 bull / -$56k bear | out (clean 36, ADX 25, RVol 0.9) |
| 11 | **MSTR** | 116.74 | - | **-** | 17 | - | NEG -$29.8M | - | 125 | 110 | -$1.8M | +$0 bull / -$38k bear | out (clean 28, ADX 15, RVol 0.5) |
| 12 | **QQQ** | 691.53 | - | **-** | 16 | - | POS +$294.0M | 690.51 | 700 | 680 | -$91.7M | +$507k bull / -$1.4M bear | out (clean 31, ADX 15, RVol 0.3) |
| 13 | **META** | 626.24 | - | **-** | 16 | - | POS +$14.8M | 624.9 | 650 | 600 | +$1.3M | +$0 bull / -$238k bear | out (clean 28, ADX 23, RVol 0.5) |
| 14 | **TSLA** | 392.66 | - | **-** | 15 | - | POS +$379.0M | - | 400 | 380 | +$8.1M | +$30k bull / -$95k bear | out (clean 29, ADX 16, RVol 0.2) |
| 15 | **BABA** | 94.52 | - | **-** | 15 | - | NEG -$15.2M | - | 100 | 95 | +$379k | - | out (clean 28, ADX 35, RVol 1.2) |
| 16 | **MU** | 791.92 | - | **-** | 14 | - | POS +$105.5M | - | 800 | 800 | +$6.6M | +$581k bull / -$998k bear | out (clean 31, ADX 16, RVol 0.4) |
| 17 | **MSFT** | 528.42 | - | **-** | 11 | - | POS +$195.4M | 521.41 | 535 | 520 | -$5.3M | - | out (clean 30, ADX 28, RVol 0.4) |
| 18 | **NFLX** | 63.97 | - | **-** | 10 | - | NEG -$1.9M | 64.09 | 65 | 65 | -$245k | - | out (clean 28, ADX 19, RVol 0.7) |
| 19 | **UBER** | 69.73 | - | **-** | 9 | - | POS +$14.7M | 68.38 | 70 | 70 | -$84k | - | out (clean 31, ADX 15, RVol 0.3) |
| 20 | **CRM** | 218.54 | - | **-** | 9 | - | NEG -$8.3M | - | 220 | 220 | -$29k | - | out (clean 29, ADX 28, RVol 0.8) |
| 21 | **SMH** | 503.24 | - | **-** | 8 | - | NEG -$87.4M | - | 500 | 500 | -$1.6M | - | out (clean 31, ADX 20, RVol 0.5) |
| 22 | **ARM** | 200.81 | - | **-** | 8 | - | POS +$10.7M | - | 200 | 200 | -$236k | - | out (clean 31, ADX 24, RVol 0.2) |
| 23 | **ORCL** | 127.67 | - | **-** | 6 | - | POS +$9.9M | - | 130 | 125 | -$531k | - | out (clean 30, ADX 15, RVol 0.3) |
| 24 | **COIN** | 132.88 | - | **-** | 5 | - | POS +$6.6M | 131.27 | 137 | 135 | +$43k | - | out (clean 30, ADX 17, RVol 0.5) |
| 25 | **IWM** | 280.84 | - | **-** | 4 | - | NEG -$731.2M | 282.66 | 285 | 275 | -$1.3M | - | out (clean 33, ADX 16, RVol 0.2) |
| 26 | **HOOD** | 83.39 | - | **-** | 4 | - | POS +$15.6M | 79.3 | 85 | 80 | -$83k | - | out (clean 34, ADX 14, RVol 0.4) |
| 27 | **SHOP** | 147.97 | - | **-** | 4 | - | POS +$4.8M | 144.13 | 150 | 140 | -$405 | - | out (clean 30, ADX 14, RVol 0.6) |

## Big prints this scan (65)
- **AMD** CALL 567.5 2026-11-13 (1DTE): 1,474 @ 17.49 = **+$2.6M** SELL | vol 4,456 / OI 329
- **AMD** CALL 575 2026-11-13 (1DTE): 1,474 @ 13.12 = **+$1.9M** SELL | vol 15,164 / OI 1,800
- **NVDA** PUT 160 2026-11-18 (6DTE): 460 @ 6.28 = **+$289k** BUY | vol 10,102 / OI 3,836
- **QQQ** PUT 700 2026-11-13 (1DTE): 200 @ 10.38 = **+$208k** BUY | vol 1,079 / OI 2,829
- **QQQ** PUT 690 2026-11-12 (0DTE): 980 @ 1.95 = **+$191k** BUY | vol 137,534 / OI 443
- **QQQ** CALL 693 2026-11-12 (0DTE): 2,927 @ 0.50 = **+$146k** SELL | vol 152,234 / OI 1,504
- **NVDA** PUT 160 2026-11-18 (6DTE): 200 @ 6.30 = **+$126k** BUY | vol 10,102 / OI 3,836
- **META** CALL 630 2026-11-13 (1DTE): 299 @ 4.00 = **+$120k** SELL | vol 4,807 / OI 2,880
- **AAPL** CALL 362.5 2026-11-18 (6DTE): 904 @ 1.30 = **+$118k** BUY | vol 2,346 / OI 7,037
- **SPY** PUT 760 2026-11-12 (0DTE): 991 @ 1.18 = **+$117k** BUY | vol 193,057 / OI 1,476
- **QQQ** PUT 692 2026-11-13 (1DTE): 200 @ 5.55 = **+$111k** BUY | vol 5,798 / OI 368
- **NVDA** PUT 157.5 2026-11-18 (6DTE): 200 @ 5.36 = **+$107k** BUY | vol 2,184 / OI 2,812
- **AMD** CALL 582.5 2026-11-13 (1DTE): 87 @ 10.50 = **+$91k** SELL | vol 3,326 / OI 413
- **MU** PUT 770 2026-11-16 (4DTE): 55 @ 15.95 = **+$88k** BUY | vol 890 / OI 75
- **NVDA** CALL 165 2026-11-13 (1DTE): 220 @ 3.20 = **+$70k** SELL | vol 199,933 / OI 2,999

## New unusual volume (traded more than open interest, 500+)
- **QQQ** PUT 699 2026-11-12 (0DTE): 500 traded vs OI 22
- **QQQ** CALL 690 2026-11-18 (6DTE): 501 traded vs OI 198
- **IWM** CALL 283 2026-11-18 (6DTE): 585 traded vs OI 160
- **SMH** CALL 507.5 2026-11-13 (1DTE): 1,041 traded vs OI 266
- **SMH** CALL 512.5 2026-11-13 (1DTE): 807 traded vs OI 725
- **NVDA** PUT 165 2026-11-18 (6DTE): 3,361 traded vs OI 3,311
- **NVDA** CALL 155 2026-12-11 (29DTE): 503 traded vs OI 24
- **AMD** CALL 607.5 2026-11-20 (8DTE): 1,602 traded vs OI 0
- **AMD** CALL 627.5 2026-11-20 (8DTE): 1,713 traded vs OI 0
- **META** PUT 610 2026-11-16 (4DTE): 527 traded vs OI 197
- **AVGO** PUT 337.5 2026-11-16 (4DTE): 594 traded vs OI 33
- **SMCI** PUT 26 2026-12-04 (22DTE): 506 traded vs OI 453
- **ORCL** PUT 127 2026-11-13 (1DTE): 511 traded vs OI 263
- **ORCL** PUT 129 2026-11-13 (1DTE): 512 traded vs OI 328

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
