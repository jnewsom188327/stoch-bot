# GEX + FLOW SCAN - Thu Nov 12, 02:00 PM ET
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
Last 1m check 14:00:08 ET, last candle SPY 13:59, QQQ 13:59 | no errors
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
| 1 | **GOOGL** | 300.63 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 41 | none: 72 puts 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (5 contracts' greeks worked out here) | POS +$139.2M | 288.22 | 300 | 290 | -$4.7M | +$173k bull / -$779k bear | out (clean 30, ADX 32, RVol 1.1) |
| 2 | **MSFT** | 524.13 | - | **-** | 20 | - | POS +$66.4M | 520.06 | 535 | 520 | -$2.3M | +$905k bull / +$0 bear | out (clean 31, ADX 35, RVol 0.9) |
| 3 | **AAPL** | 355.85 | - | **-** | 19 | - | POS +$1.1B | 339.27 | 360 | 360 | +$4.3M | +$649k bull / -$706k bear | out (clean 29, ADX 32, RVol 0.8) |
| 4 | **NVDA** | 164.75 | - | **-** | 16 | - | NEG -$189.9M | - | 170 | 160 | -$67.3M | +$4.1M bull / +$0 bear | out (clean 32, ADX 11, RVol 0.8) |
| 5 | **TSLA** | 391.11 | - | **-** | 16 | - | POS +$362.2M | - | 400 | 380 | +$11.0M | +$186k bull / +$0 bear | out (clean 29, ADX 16, RVol 0.2) |
| 6 | **AVGO** | 365.08 | - | **-** | 16 | - | POS +$135.4M | - | 350 | 350 | +$8.9M | +$306k bull / +$0 bear | out (clean 34, ADX 11, RVol 0.7) |
| 7 | **QQQ** | 689.16 | - | **-** | 15 | - | NEG -$437.4M | 690.62 | 700 | 680 | -$77.3M | +$1.9M bull / +$0 bear | out (clean 30, ADX 14, RVol 0.3) |
| 8 | **META** | 623.74 | - | **-** | 15 | - | NEG -$10.9M | 624.4 | 650 | 600 | +$1.9M | +$39k bull / +$0 bear | out (clean 28, ADX 19, RVol 0.5) |
| 9 | **AMD** | 579.12 | - | **-** | 14 | - | POS +$193.8M | - | 600 | 550 | -$13.6M | +$2.3M bull / -$56k bear | out (clean 34, ADX 14, RVol 0.5) |
| 10 | **MU** | 792.94 | - | **-** | 13 | - | POS +$101.5M | - | 800 | 800 | +$5.7M | +$1.7M bull / +$0 bear | out (clean 31, ADX 14, RVol 0.3) |
| 11 | **SMCI** | 27.27 | - | **-** | 12 | - | NEG -$821k | - | 28 | 25 | +$1.1M | - | out (clean 34, ADX 26, RVol 1.3) |
| 12 | **BABA** | 94.78 | - | **-** | 10 | - | NEG -$16.0M | - | 100 | 100 | +$329k | - | out (clean 28, ADX 17, RVol 0.9) |
| 13 | **SPY** | 759.04 | - | **-** | 7 | - | NEG -$1.9B | 760.81 | 760 | 760 | -$110.6M | - | out (clean 31, ADX 15, RVol 0.6) |
| 14 | **NFLX** | 63.72 | - | **-** | 7 | - | NEG -$6.4M | 64 | 65 | 65 | -$201k | - | out (clean 28, ADX 14, RVol 0.5) |
| 15 | **UBER** | 69.72 | - | **-** | 7 | - | POS +$16.0M | 68.39 | 70 | 70 | -$61k | - | out (clean 31, ADX 16, RVol 0.4) |
| 16 | **IWM** | 279.79 | - | **-** | 6 | - | NEG -$1.2B | 282.62 | 285 | 275 | -$260k | - | out (clean 33, ADX 29, RVol 0.5) |
| 17 | **SMH** | 501.81 | - | **-** | 6 | - | NEG -$109.1M | - | 500 | 500 | -$1.6M | - | out (clean 30, ADX 13, RVol 0.5) |
| 18 | **AMZN** | 269.17 | - | **-** | 6 | - | POS +$497.0M | - | 270 | 270 | -$6.4M | - | out (clean 29, ADX 10, RVol 0.7) |
| 19 | **DELL** | 374.39 | - | **-** | 6 | - | POS +$5.3M | - | 360 | 380 | +$438k | - | out (clean 37, ADX 24, RVol 0.3) |
| 20 | **ARM** | 200.56 | - | **-** | 6 | - | POS +$10.6M | - | 200 | 200 | -$194k | - | out (clean 31, ADX 17, RVol 0.1) |
| 21 | **CRM** | 217.50 | - | **-** | 6 | - | NEG -$7.8M | 228.37 | 220 | 220 | +$43k | - | out (clean 28, ADX 19, RVol 0.2) |
| 22 | **MSTR** | 116.28 | - | **-** | 5 | - | NEG -$33.4M | - | 125 | 110 | -$1.4M | - | out (clean 28, ADX 10, RVol 0.3) |
| 23 | **ORCL** | 127.51 | - | **-** | 5 | - | POS +$10.6M | 121.53 | 130 | 125 | -$580k | - | out (clean 30, ADX 10, RVol 0.3) |
| 24 | **SHOP** | 147.49 | - | **-** | 5 | - | POS +$3.8M | 144.02 | 150 | 140 | +$406 | - | out (clean 30, ADX 24, RVol 0.3) |
| 25 | **PLTR** | 172.26 | - | **-** | 4 | - | POS +$96.4M | - | 170 | 170 | -$295k | - | out (clean 28, ADX 12, RVol 0.4) |
| 26 | **COIN** | 132.59 | - | **-** | 4 | - | POS +$3.2M | 131.42 | 137 | 135 | +$68k | - | out (clean 29, ADX 11, RVol 0.4) |
| 27 | **HOOD** | 83.05 | - | **-** | 4 | - | POS +$10.9M | 80.32 | 85 | 80 | -$27k | - | out (clean 34, ADX 12, RVol 0.8) |

## Big prints this scan (64)
- **AAPL** PUT 355 2026-11-18 (6DTE): 1,000 @ 3.00 = **+$300k** SELL | vol 5,441 / OI 20
- **QQQ** CALL 680 2026-11-12 (0DTE): 250 @ 10.59 = **+$265k** BUY | vol 7,397 / OI 2,244
- **MU** CALL 795 2026-11-13 (1DTE): 95 @ 14.25 = **+$135k** BUY | vol 11,152 / OI 462
- **NVDA** PUT 172.5 2026-11-18 (6DTE): 100 @ 12.15 = **+$122k** SELL | vol 794 / OI 0
- **QQQ** CALL 686 2026-11-12 (0DTE): 250 @ 4.79 = **+$120k** BUY | vol 71,254 / OI 503
- **AAPL** PUT 355 2026-11-18 (6DTE): 400 @ 2.96 = **+$118k** SELL | vol 5,441 / OI 20
- **TSLA** CALL 385 2026-11-16 (4DTE): 95 @ 10.50 = **+$100k** BUY | vol 1,243 / OI 301
- **MSFT** PUT 527.5 2026-11-13 (1DTE): 216 @ 4.20 = **+$91k** SELL | vol 4,427 / OI 988
- **MSFT** PUT 527.5 2026-11-13 (1DTE): 215 @ 4.20 = **+$90k** SELL | vol 4,427 / OI 988
- **AAPL** PUT 355 2026-11-18 (6DTE): 300 @ 2.96 = **+$89k** SELL | vol 5,441 / OI 20
- **AAPL** PUT 355 2026-11-18 (6DTE): 300 @ 2.96 = **+$89k** SELL | vol 5,441 / OI 20
- **NVDA** CALL 167.5 2026-11-13 (1DTE): 332 @ 2.35 = **+$78k** BUY | vol 129,217 / OI 6,311
- **MU** PUT 800 2026-11-13 (1DTE): 40 @ 17.80 = **+$71k** SELL | vol 5,756 / OI 872
- **GOOGL** PUT 302.5 2026-11-13 (1DTE): 243 @ 2.88 = **+$70k** SELL | vol 1,628 / OI 164
- **NVDA** PUT 165 2026-11-13 (1DTE): 210 @ 3.00 = **+$63k** SELL | vol 102,565 / OI 19,300

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 775 2026-11-13 (1DTE): 5,911 traded vs OI 5,830
- **SPY** CALL 768 2026-11-16 (4DTE): 2,310 traded vs OI 2,267
- **SPY** PUT 736 2026-11-16 (4DTE): 527 traded vs OI 496
- **QQQ** CALL 698 2026-11-16 (4DTE): 500 traded vs OI 179
- **QQQ** CALL 708 2026-11-16 (4DTE): 561 traded vs OI 148
- **QQQ** PUT 636 2026-11-13 (1DTE): 531 traded vs OI 256
- **QQQ** PUT 691 2026-11-23 (11DTE): 500 traded vs OI 0
- **NVDA** PUT 162.5 2026-11-27 (15DTE): 502 traded vs OI 0
- **TSLA** PUT 365 2026-11-13 (1DTE): 1,198 traded vs OI 1,192
- **AMZN** CALL 270 2026-12-04 (22DTE): 2,533 traded vs OI 1,802
- **MSFT** CALL 550 2026-11-16 (4DTE): 578 traded vs OI 283
- **GOOGL** CALL 310 2026-11-20 (8DTE): 9,125 traded vs OI 7,551
- **AVGO** CALL 390 2026-11-13 (1DTE): 3,375 traded vs OI 3,368
- **AVGO** PUT 365 2026-11-16 (4DTE): 502 traded vs OI 0
- **MSTR** CALL 121 2026-11-20 (8DTE): 5,162 traded vs OI 356

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
