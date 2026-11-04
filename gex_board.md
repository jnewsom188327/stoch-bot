# GEX + FLOW SCAN - Wed Nov 04, 11:35 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (7)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:21 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/04 685P | 0.67 | 0.48 | +66% (7m) | **-28%** | +25% | 690.3 hit |
| 10:20 | **SMCI** | **CALLS** | FLOW SURGE | 11/06 33C | 0.65 | 0.13 | -3% (1m) | **-80%** (done) | +39% | 32.81 |
| 10:20 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/04 284C | 0.49 | 0.17 | +2% (22m) | **-65%** (done) | +131% | 284.74 |
| 10:00 | **AMZN** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/04 267.5P | 0.68 | 1.54 | +169% (60m) | **+126%** (done) | +258% | 265.7 |
| 09:50 | **UBER** | **CALLS** | FLIP CROSS up into positive gamma | 11/06 71C | 0.60 | 1.56 | +168% (52m) | **+160%** (done) | +50% | 70 hit |
| 09:50 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/04 286C | 0.53 | 0.06 | +2% (1m) | **-89%** (done) | +150% | 287 |
| 09:45 | **UBER** | **PUTS** | FLIP CROSS down into negative gamma | 11/06 67P | 0.63 | 0.10 | -3% (1m) | **-84%** (done) | +27% | 68.03 |

## 1m RULES on SPY / QQQ - loose (1 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 11:35:08 ET, last candle SPY 11:34, QQQ 11:34 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 11:20 | QQQ | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | **FIRE** QQQ261104P00685000 |

## Flow surges NOT fired - price disagreed (33 today, last 5)
- 11:35 SMCI CALLS: price -0.19 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 11:30 SMCI CALLS: price -0.20 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 11:25 SMCI CALLS: price -0.14 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 11:20 SMCI CALLS: under EMA 20 - flow says one way, price says the other
- 11:15 SMCI CALLS: price -0.11 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **SMCI** | 30.00 | FLOW SURGE | **CALLS** | 62 | 11/06 31.5C @ 0.44 (delta 0.29) = est +56% at 30.9 | NEG -$558k | - | 33 | 30 | +$2.0M | +$53k bull / +$0 bear | SHORT (clean 34, ADX 48, RVol 2.4) |
| 2 | **DELL** | 369.98 | TREND (flow not with it) | **PUTS** | 47 | none: 23 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$27.5M | - | 400 | 400 | +$2.2M | +$288k bull / +$0 bear | SHORT (clean 33, ADX 42, RVol 3.9) |
| 3 | **GOOGL** | 290.19 | PINNED between the walls (positive gamma) - chop | **-** | 42 | - | POS +$88.0M | 282.84 | 290 | 290 | -$25.7M | +$259k bull / +$0 bear | out (clean 35, ADX 39, RVol 0.7) |
| 4 | **ARM** | 194.46 | - | **-** | 33 | - | NEG -$6.7M | - | 212.5 | 200 | +$852k | +$0 bull / -$46k bear | out (clean 26, ADX 39, RVol 1.0) |
| 5 | **AAPL** | 351.96 | - | **-** | 32 | - | POS +$892.4M | 341.92 | 350 | 350 | -$76.7M | +$517k bull / -$34k bear | out (clean 32, ADX 55, RVol 1.2) |
| 6 | **NFLX** | 66.09 | - | **-** | 27 | - | POS +$18.9M | - | 65 | 65 | -$2.1M | +$34k bull / +$0 bear | out (clean 31, ADX 64, RVol 0.8) |
| 7 | **MU** | 806.27 | - | **-** | 27 | - | NEG -$345.5M | - | 850 | 800 | +$101.7M | +$1.7M bull / -$7.7M bear | out (clean 31, ADX 36, RVol 1.4) |
| 8 | **SMH** | 504.57 | - | **-** | 26 | - | NEG -$516.5M | - | 532.5 | 500 | +$4.0M | +$0 bull / -$324k bear | out (clean 32, ADX 39, RVol 1.2) |
| 9 | **AMZN** | 266.03 | - | **-** | 25 | - | POS +$535.1M | - | 270 | 250 | -$17.1M | +$222k bull / +$0 bear | out (clean 35, ADX 42, RVol 1.2) |
| 10 | **MSFT** | 554.53 | - | **-** | 25 | - | POS +$963.7M | - | 550 | 535 | -$14.9M | +$159k bull / -$82k bear | out (clean 28, ADX 64, RVol 1.1) |
| 11 | **UBER** | 71.66 | - | **-** | 25 | - | POS +$12.4M | 68.15 | 70 | 70 | -$1.4M | - | out (clean 31, ADX 60, RVol 1.9) |
| 12 | **TSLA** | 384.15 | - | **-** | 23 | - | NEG -$116.9M | 392.45 | 400 | 380 | -$59.8M | +$2.8M bull / -$435k bear | out (clean 30, ADX 24, RVol 1.7) |
| 13 | **ORCL** | 125.03 | - | **-** | 23 | - | NEG -$33.2M | - | 130 | 125 | +$2.3M | +$1.2M bull / +$0 bear | out (clean 35, ADX 16, RVol 2.9) |
| 14 | **IWM** | 282.30 | - | **-** | 22 | - | NEG -$742.8M | 284.61 | 285 | 270 | +$14.5M | +$55k bull / +$0 bear | out (clean 34, ADX 16, RVol 1.2) |
| 15 | **AVGO** | 326.70 | - | **-** | 22 | - | NEG -$97.4M | - | 340 | 320 | +$2.6M | +$0 bull / -$70k bear | out (clean 30, ADX 34, RVol 1.2) |
| 16 | **NVDA** | 202.54 | - | **-** | 21 | - | NEG -$87.2M | 204.04 | 210 | 200 | +$3.6M | +$614k bull / -$210k bear | out (clean 30, ADX 39, RVol 1.7) |
| 17 | **AMD** | 484.62 | - | **-** | 21 | - | NEG -$90.6M | - | 500 | 500 | +$40.0M | +$500k bull / -$1.1M bear | out (clean 32, ADX 20, RVol 1.0) |
| 18 | **META** | 629.43 | - | **-** | 20 | - | POS +$143.5M | 620.37 | 650 | 625 | +$7.7M | +$129k bull / -$27k bear | out (clean 30, ADX 30, RVol 0.9) |
| 19 | **MSTR** | 143.66 | - | **-** | 20 | - | POS +$123.4M | - | 135 | 150 | +$396k | +$278k bull / +$0 bear | out (clean 31, ADX 42, RVol 0.9) |
| 20 | **BABA** | 106.57 | - | **-** | 20 | - | POS +$15.4M | - | 110 | 110 | -$809k | - | out (clean 36, ADX 56, RVol 2.2) |
| 21 | **SPY** | 765.34 | - | **-** | 19 | - | NEG -$4.4B | 769.9 | 770 | 750 | -$46.6M | +$2.4M bull / +$0 bear | out (clean 32, ADX 29, RVol 1.1) |
| 22 | **PLTR** | 170.52 | - | **-** | 19 | - | NEG -$50.0M | - | 165 | 170 | -$1.7M | +$396k bull / +$0 bear | out (clean 26, ADX 20, RVol 1.7) |
| 23 | **QQQ** | 692.41 | - | **-** | 17 | - | NEG -$5.0B | 719.43 | 700 | 680 | -$58.0M | +$2.7M bull / -$3.3M bear | out (clean 31, ADX 22, RVol 1.0) |
| 24 | **HOOD** | 86.82 | - | **-** | 15 | - | POS +$1.8M | 85.16 | 90 | 90 | -$813k | +$28k bull / -$60k bear | out (clean 28, ADX 13, RVol 0.7) |
| 25 | **CRM** | 227.53 | - | **-** | 14 | - | NEG -$9.4M | 238.48 | 240 | 220 | -$194k | - | out (clean 32, ADX 41, RVol 0.7) |
| 26 | **SHOP** | 151.41 | - | **-** | 14 | - | NEG -$5.4M | - | 160 | 150 | -$306k | - | out (clean 34, ADX 30, RVol 0.4) |
| 27 | **COIN** | 151.13 | - | **-** | 12 | - | POS +$29.7M | - | 148 | 150 | -$1.2M | - | out (clean 30, ADX 16, RVol 0.5) |

## Big prints this scan (65)
- **MU** CALL 810 2026-11-09 (5DTE): 298 @ 23.65 = **+$705k** BUY | vol 750 / OI 0
- **MU** CALL 810 2026-11-09 (5DTE): 224 @ 23.55 = **+$528k** BUY | vol 750 / OI 0
- **TSLA** PUT 385 2026-11-09 (5DTE): 229 @ 8.60 = **+$197k** BUY | vol 3,799 / OI 308
- **SPY** PUT 764 2026-11-05 (1DTE): 837 @ 2.28 = **+$191k** SELL | vol 22,740 / OI 0
- **MU** PUT 805 2026-11-06 (2DTE): 75 @ 21.47 = **+$161k** BUY | vol 1,514 / OI 615
- **QQQ** CALL 697 2026-11-04 (0DTE): 1,500 @ 0.96 = **+$144k** BUY | vol 91,218 / OI 930
- **MU** PUT 800 2026-11-06 (2DTE): 75 @ 19.12 = **+$143k** BUY | vol 6,597 / OI 3,802
- **MU** CALL 810 2026-11-09 (5DTE): 54 @ 23.55 = **+$127k** BUY | vol 750 / OI 0
- **TSLA** CALL 390 2026-11-11 (7DTE): 150 @ 7.75 = **+$116k** BUY | vol 1,957 / OI 87
- **SPY** CALL 766 2026-11-05 (1DTE): 399 @ 2.85 = **+$114k** BUY | vol 16,305 / OI 0
- **QQQ** PUT 693 2026-11-09 (5DTE): 144 @ 7.70 = **+$111k** SELL | vol 811 / OI 0
- **TSLA** CALL 390 2026-11-11 (7DTE): 150 @ 7.25 = **+$109k** SELL | vol 1,957 / OI 87
- **SPY** CALL 766 2026-11-06 (2DTE): 250 @ 4.13 = **+$103k** BUY | vol 8,959 / OI 5,917
- **MU** CALL 810 2026-11-06 (2DTE): 55 @ 18.63 = **+$102k** SELL | vol 1,363 / OI 59
- **QQQ** CALL 692 2026-11-05 (1DTE): 185 @ 5.53 = **+$102k** BUY | vol 3,298 / OI 0

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 789 2026-11-17 (13DTE): 503 traded vs OI 0
- **QQQ** PUT 667 2026-11-05 (1DTE): 516 traded vs OI 0
- **IWM** PUT 276 2026-11-04 (0DTE): 983 traded vs OI 979
- **NVDA** PUT 207.5 2026-11-09 (5DTE): 505 traded vs OI 396
- **TSLA** PUT 372.5 2026-11-06 (2DTE): 1,857 traded vs OI 1,834
- **AAPL** PUT 355 2026-11-06 (2DTE): 2,216 traded vs OI 2,094
- **MSFT** PUT 517.5 2026-11-06 (2DTE): 526 traded vs OI 354
- **PLTR** CALL 165 2026-11-06 (2DTE): 500 traded vs OI 155
- **SMCI** CALL 30 2026-11-13 (9DTE): 707 traded vs OI 248
- **MU** CALL 810 2026-11-09 (5DTE): 750 traded vs OI 0
- **ORCL** PUT 125 2026-11-06 (2DTE): 4,581 traded vs OI 4,573
- **UBER** CALL 71 2026-11-20 (16DTE): 1,311 traded vs OI 1,019
- **UBER** CALL 72 2026-11-13 (9DTE): 534 traded vs OI 529
- **UBER** CALL 76 2026-11-06 (2DTE): 580 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
