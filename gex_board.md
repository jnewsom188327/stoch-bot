# GEX + FLOW SCAN - Thu Nov 12, 12:30 PM ET
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
Last 1m check 12:30:08 ET, last candle SPY 12:29, QQQ 12:29 | no errors
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
| 1 | **SMCI** | 26.54 | TREND (flow not with it) | **PUTS** | 46 | 11/13 25.5P @ 0.48 (delta 0.30) = est +115% at 25 | NEG -$1.2M | - | 28 | 25 | +$1.7M | - | SHORT (clean 34, ADX 48, RVol 2.1) |
| 2 | **AMZN** | 269.51 | PINNED between the walls (positive gamma) - chop | **-** | 31 | - | POS +$511.2M | - | 270 | 270 | -$6.3M | +$473k bull / -$53k bear | out (clean 30, ADX 12, RVol 0.7) |
| 3 | **GOOGL** | 301.94 | - | **-** | 25 | - | POS +$137.6M | 288.62 | 300 | 290 | -$6.2M | +$0 bull / -$973k bear | out (clean 29, ADX 40, RVol 1.1) |
| 4 | **NVDA** | 163.98 | - | **-** | 19 | - | NEG -$187.6M | - | 170 | 160 | -$74.8M | +$3.1M bull / -$183k bear | out (clean 32, ADX 23, RVol 0.8) |
| 5 | **ARM** | 200.11 | PINNED between the walls (positive gamma) - chop | **-** | 19 | - | POS +$10.1M | - | 200 | 200 | -$226k | - | out (clean 31, ADX 23, RVol 0.2) |
| 6 | **SPY** | 760.95 | - | **-** | 17 | - | NEG -$627.9M | 761.43 | 760 | 760 | -$125.7M | +$100k bull / +$0 bear | out (clean 31, ADX 15, RVol 0.3) |
| 7 | **SMH** | 500.52 | - | **-** | 17 | - | NEG -$106.4M | - | 500 | 475 | -$1.1M | +$58k bull / +$0 bear | out (clean 31, ADX 21, RVol 0.5) |
| 8 | **AAPL** | 356.50 | - | **-** | 17 | - | POS +$1.1B | 340.46 | 360 | 360 | +$2.5M | +$1.0M bull / +$0 bear | out (clean 28, ADX 24, RVol 0.7) |
| 9 | **AMD** | 577.72 | - | **-** | 17 | - | POS +$196.9M | - | 600 | 550 | -$12.0M | +$3.6M bull / +$0 bear | out (clean 35, ADX 27, RVol 0.8) |
| 10 | **META** | 624.32 | - | **-** | 17 | - | NEG -$2.2M | 624.26 | 650 | 600 | +$1.6M | +$88k bull / -$74k bear | out (clean 28, ADX 26, RVol 0.5) |
| 11 | **PLTR** | 172.49 | - | **-** | 17 | - | POS +$94.0M | - | 170 | 170 | -$492k | +$29k bull / +$0 bear | out (clean 28, ADX 18, RVol 0.6) |
| 12 | **DELL** | 373.97 | - | **-** | 17 | - | POS +$5.4M | - | 360 | 340 | -$392k | +$103k bull / -$84k bear | out (clean 36, ADX 24, RVol 1.0) |
| 13 | **QQQ** | 690.38 | - | **-** | 16 | - | NEG -$152.5M | 690.78 | 700 | 680 | -$86.8M | +$739k bull / +$0 bear | out (clean 31, ADX 16, RVol 0.3) |
| 14 | **TSLA** | 391.44 | - | **-** | 16 | - | POS +$372.8M | - | 400 | 380 | +$8.7M | +$152k bull / -$61k bear | out (clean 29, ADX 18, RVol 0.2) |
| 15 | **BABA** | 94.62 | - | **-** | 16 | - | NEG -$15.7M | - | 100 | 95 | +$385k | - | out (clean 28, ADX 36, RVol 1.4) |
| 16 | **MU** | 785.33 | - | **-** | 15 | - | POS +$96.0M | - | 800 | 800 | +$10.6M | +$1.5M bull / -$177k bear | out (clean 31, ADX 17, RVol 0.4) |
| 17 | **MSFT** | 529.00 | - | **-** | 11 | - | POS +$205.0M | 521.24 | 535 | 520 | -$5.2M | - | out (clean 31, ADX 28, RVol 0.4) |
| 18 | **NFLX** | 63.94 | - | **-** | 9 | - | NEG -$2.8M | 64.09 | 65 | 65 | -$230k | - | out (clean 28, ADX 18, RVol 0.6) |
| 19 | **MSTR** | 117.00 | - | **-** | 9 | - | NEG -$29.6M | - | 125 | 110 | -$1.7M | - | out (clean 28, ADX 18, RVol 1.2) |
| 20 | **UBER** | 69.77 | - | **-** | 9 | - | POS +$16.0M | 68.32 | 70 | 70 | -$84k | - | out (clean 31, ADX 17, RVol 0.4) |
| 21 | **AVGO** | 363.24 | - | **-** | 8 | - | POS +$131.1M | - | 350 | 350 | +$7.7M | - | out (clean 35, ADX 20, RVol 0.7) |
| 22 | **CRM** | 219.18 | - | **-** | 8 | - | NEG -$8.6M | - | 230 | 220 | -$28k | - | out (clean 29, ADX 27, RVol 0.8) |
| 23 | **ORCL** | 127.40 | - | **-** | 6 | - | POS +$9.4M | - | 130 | 125 | -$414k | - | out (clean 30, ADX 15, RVol 0.4) |
| 24 | **IWM** | 280.92 | - | **-** | 4 | - | NEG -$774.9M | 282.69 | 285 | 275 | -$1.1M | - | out (clean 33, ADX 18, RVol 0.2) |
| 25 | **COIN** | 133.13 | - | **-** | 4 | - | POS +$6.0M | 131.34 | 137 | 135 | +$5k | - | out (clean 30, ADX 19, RVol 0.5) |
| 26 | **HOOD** | 83.25 | - | **-** | 4 | - | POS +$12.7M | 80.05 | 85 | 80 | -$60k | - | out (clean 34, ADX 16, RVol 0.4) |
| 27 | **SHOP** | 148.43 | - | **-** | 4 | - | POS +$4.6M | 144.21 | 150 | 140 | -$625 | - | out (clean 30, ADX 14, RVol 0.6) |

## Big prints this scan (69)
- **AAPL** PUT 360 2026-11-13 (1DTE): 889 @ 3.60 = **+$320k** SELL | vol 6,882 / OI 6,822
- **AMZN** CALL 270 2026-11-16 (4DTE): 500 @ 3.10 = **+$155k** BUY | vol 3,603 / OI 488
- **AMD** CALL 582.5 2026-11-13 (1DTE): 93 @ 12.30 = **+$114k** BUY | vol 3,090 / OI 413
- **AMD** PUT 582.5 2026-11-13 (1DTE): 83 @ 12.00 = **+$100k** SELL | vol 2,254 / OI 3
- **NVDA** CALL 165 2026-11-18 (6DTE): 100 @ 8.05 = **+$80k** MID | vol 8,637 / OI 517
- **MU** CALL 820 2026-11-18 (6DTE): 48 @ 16.35 = **+$78k** MID | vol 637 / OI 81
- **AMD** CALL 600 2026-11-13 (1DTE): 163 @ 4.75 = **+$77k** BUY | vol 40,050 / OI 3,062
- **NVDA** CALL 165 2026-11-13 (1DTE): 176 @ 3.56 = **+$63k** BUY | vol 197,317 / OI 2,999
- **NVDA** PUT 160 2026-11-18 (6DTE): 100 @ 6.20 = **+$62k** MID | vol 9,285 / OI 3,836
- **MU** CALL 820 2026-11-18 (6DTE): 36 @ 16.90 = **+$61k** BUY | vol 637 / OI 81
- **AMD** CALL 587.5 2026-11-18 (6DTE): 30 @ 19.19 = **+$58k** BUY | vol 142 / OI 10
- **NVDA** PUT 162.5 2026-11-13 (1DTE): 200 @ 2.75 = **+$55k** SELL | vol 95,637 / OI 20,581
- **NVDA** CALL 170 2026-11-13 (1DTE): 340 @ 1.58 = **+$54k** BUY | vol 170,318 / OI 11,191
- **AAPL** PUT 357.5 2026-11-13 (1DTE): 262 @ 2.05 = **+$54k** SELL | vol 16,505 / OI 867
- **AMD** PUT 577.5 2026-11-13 (1DTE): 58 @ 9.25 = **+$54k** SELL | vol 1,138 / OI 10

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 781 2026-11-18 (6DTE): 502 traded vs OI 58
- **SPY** PUT 748 2026-11-13 (1DTE): 7,193 traded vs OI 5,616
- **SPY** PUT 690 2026-11-23 (11DTE): 1,000 traded vs OI 86
- **QQQ** PUT 692 2026-11-17 (5DTE): 501 traded vs OI 33
- **SMH** PUT 460 2026-12-04 (22DTE): 1,599 traded vs OI 1,329
- **AAPL** PUT 340 2026-11-27 (15DTE): 1,893 traded vs OI 1,631
- **AMZN** CALL 257.5 2026-11-13 (1DTE): 1,427 traded vs OI 1,294
- **MSFT** PUT 520 2026-11-16 (4DTE): 502 traded vs OI 493
- **GOOGL** CALL 315 2026-11-16 (4DTE): 547 traded vs OI 178
- **MSTR** PUT 111 2026-11-13 (1DTE): 743 traded vs OI 717
- **CRM** CALL 220 2026-11-13 (1DTE): 525 traded vs OI 327

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
