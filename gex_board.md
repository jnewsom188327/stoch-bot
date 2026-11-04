# GEX + FLOW SCAN - Wed Nov 04, 11:50 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (8)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:38 | **QQQ** | **PUTS** | 1m FAILED POP (R3) | 11/04 686P | 0.80 | 0.31 | -1% (0m) | **-61%** | +26% | 689.6 |
| 11:21 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/04 685P | 0.67 | 0.20 | +66% (7m) | **-70%** | +25% | 690.3 hit |
| 10:20 | **SMCI** | **CALLS** | FLOW SURGE | 11/06 33C | 0.65 | 0.13 | -3% (1m) | **-80%** (done) | +39% | 32.81 |
| 10:20 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/04 284C | 0.49 | 0.17 | +2% (22m) | **-65%** (done) | +131% | 284.74 |
| 10:00 | **AMZN** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/04 267.5P | 0.68 | 1.54 | +169% (60m) | **+126%** (done) | +258% | 265.7 |
| 09:50 | **UBER** | **CALLS** | FLIP CROSS up into positive gamma | 11/06 71C | 0.60 | 1.56 | +168% (52m) | **+160%** (done) | +50% | 70 hit |
| 09:50 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/04 286C | 0.53 | 0.06 | +2% (1m) | **-89%** (done) | +150% | 287 |
| 09:45 | **UBER** | **PUTS** | FLIP CROSS down into negative gamma | 11/06 67P | 0.63 | 0.10 | -3% (1m) | **-84%** (done) | +27% | 68.03 |

## 1m RULES on SPY / QQQ - loose (2 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 11:50:08 ET, last candle SPY 11:49, QQQ 11:49 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 11:37 | QQQ | 1m FAILED POP | R3 | PUTS | TURNING away | **FIRE** QQQ261104P00686000 |
| 11:20 | QQQ | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | **FIRE** QQQ261104P00685000 |

## Flow surges NOT fired - price disagreed (36 today, last 5)
- 11:50 SMCI CALLS: under EMA 20 - flow says one way, price says the other
- 11:45 SMCI CALLS: under EMA 20 - flow says one way, price says the other
- 11:40 SMCI CALLS: under EMA 20 - flow says one way, price says the other
- 11:35 SMCI CALLS: price -0.19 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 11:30 SMCI CALLS: price -0.20 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **SMCI** | 30.12 | FLOW SURGE | **CALLS** | 54 | 11/06 31.5C @ 0.48 (delta 0.31) = est +48% at 30.96 | NEG -$512k | - | 33 | 30 | +$1.9M | +$53k bull / -$37k bear | SHORT (clean 34, ADX 48, RVol 1.6) |
| 2 | **AAPL** | 353.30 | FLOW SURGE | **PUTS** | 41 | none: 108 puts 0-7DTE > 8 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (61 contracts' greeks worked out here) | POS +$993.5M | 343.25 | 355 | 350 | -$80.3M | +$150k bull / -$983k bear | out (clean 32, ADX 52, RVol 1.0) |
| 3 | **GOOGL** | 292.12 | - | **-** | 28 | - | POS +$97.8M | 283.88 | 290 | 290 | -$26.9M | +$618k bull / -$140k bear | out (clean 36, ADX 34, RVol 0.7) |
| 4 | **ARM** | 194.91 | - | **-** | 28 | - | NEG -$6.6M | - | 212.5 | 200 | +$658k | +$0 bull / -$30k bear | out (clean 26, ADX 36, RVol 1.1) |
| 5 | **MSFT** | 556.88 | - | **-** | 26 | - | POS +$990.0M | - | 550 | 535 | -$18.5M | +$0 bull / -$1.2M bear | out (clean 28, ADX 64, RVol 1.2) |
| 6 | **MU** | 804.90 | - | **-** | 26 | - | NEG -$358.2M | - | 850 | 800 | +$107.4M | +$3.9M bull / -$2.2M bear | out (clean 31, ADX 35, RVol 1.2) |
| 7 | **DELL** | 371.19 | - | **-** | 25 | - | NEG -$28.0M | - | 400 | 400 | +$1.8M | +$0 bull / -$59k bear | out (clean 33, ADX 40, RVol 2.0) |
| 8 | **AMZN** | 268.03 | - | **-** | 24 | - | POS +$535.0M | - | 270 | 250 | -$18.4M | +$62k bull / -$149k bear | out (clean 35, ADX 39, RVol 1.1) |
| 9 | **TSLA** | 385.28 | - | **-** | 23 | - | NEG -$133.9M | 396.28 | 400 | 380 | -$68.8M | +$116k bull / -$2.6M bear | out (clean 30, ADX 22, RVol 1.6) |
| 10 | **ORCL** | 126.07 | - | **-** | 23 | - | NEG -$30.4M | - | 130 | 125 | +$2.4M | +$29k bull / +$0 bear | out (clean 35, ADX 16, RVol 2.9) |
| 11 | **UBER** | 71.92 | - | **-** | 23 | - | POS +$12.9M | 68.24 | 70 | 70 | -$1.5M | - | out (clean 31, ADX 54, RVol 1.0) |
| 12 | **SPY** | 767.58 | - | **-** | 20 | - | NEG -$2.7B | 770.15 | 770 | 750 | -$97.5M | +$408k bull / -$3.6M bear | out (clean 32, ADX 27, RVol 1.1) |
| 13 | **IWM** | 283.76 | - | **-** | 20 | - | NEG -$309.1M | 284.69 | 285 | 270 | +$11.9M | +$55k bull / -$451k bear | out (clean 34, ADX 16, RVol 0.8) |
| 14 | **NVDA** | 202.94 | - | **-** | 20 | - | NEG -$56.2M | 203.79 | 210 | 200 | +$920k | +$408k bull / -$1.0M bear | out (clean 30, ADX 38, RVol 1.6) |
| 15 | **AMD** | 485.94 | - | **-** | 20 | - | NEG -$90.3M | - | 500 | 500 | +$38.9M | +$303k bull / -$862k bear | out (clean 32, ADX 17, RVol 0.8) |
| 16 | **AVGO** | 327.49 | - | **-** | 20 | - | NEG -$95.9M | - | 340 | 330 | +$1.9M | +$0 bull / -$136k bear | out (clean 30, ADX 32, RVol 0.9) |
| 17 | **PLTR** | 170.98 | - | **-** | 19 | - | NEG -$50.2M | - | 165 | 170 | -$1.8M | +$241k bull / -$524k bear | out (clean 26, ADX 23, RVol 1.7) |
| 18 | **MSTR** | 144.64 | - | **-** | 19 | - | POS +$122.0M | - | 135 | 150 | +$443k | +$106k bull / -$212k bear | out (clean 31, ADX 40, RVol 0.7) |
| 19 | **BABA** | 107.27 | - | **-** | 19 | - | POS +$15.4M | - | 110 | 110 | -$857k | - | out (clean 36, ADX 51, RVol 1.6) |
| 20 | **QQQ** | 694.69 | - | **-** | 18 | - | NEG -$4.6B | 720.44 | 700 | 680 | -$120.2M | +$638k bull / -$30.9M bear | out (clean 31, ADX 19, RVol 0.9) |
| 21 | **NFLX** | 66.22 | - | **-** | 18 | - | POS +$18.9M | 62.28 | 65 | 65 | -$2.2M | - | out (clean 31, ADX 60, RVol 0.8) |
| 22 | **META** | 634.59 | - | **-** | 17 | - | POS +$198.7M | 620 | 650 | 625 | +$4.6M | +$0 bull / -$1.2M bear | out (clean 30, ADX 26, RVol 0.6) |
| 23 | **SMH** | 505.80 | - | **-** | 15 | - | NEG -$522.7M | - | 532.5 | 500 | +$3.4M | - | out (clean 32, ADX 35, RVol 1.5) |
| 24 | **SHOP** | 153.01 | - | **-** | 15 | - | NEG -$4.7M | - | 160 | 150 | -$357k | - | out (clean 34, ADX 31, RVol 0.4) |
| 25 | **COIN** | 152.49 | - | **-** | 14 | - | POS +$27.4M | - | 148 | 150 | -$1.3M | - | out (clean 30, ADX 18, RVol 0.8) |
| 26 | **CRM** | 226.91 | - | **-** | 13 | - | NEG -$13.0M | - | 240 | 220 | -$189k | - | out (clean 32, ADX 36, RVol 0.6) |
| 27 | **HOOD** | 87.78 | - | **-** | 5 | - | POS +$2.8M | 84.63 | 90 | 90 | -$914k | - | out (clean 28, ADX 14, RVol 0.6) |

## Big prints this scan (79)
- **QQQ** PUT 690 2026-11-04 (0DTE): 2,000 @ 1.50 = **+$300k** BUY | vol 155,572 / OI 3,140
- **META** PUT 625 2026-11-06 (2DTE): 300 @ 9.10 = **+$273k** BUY | vol 1,421 / OI 3,279
- **IWM** PUT 283 2026-11-04 (0DTE): 1,499 @ 1.45 = **+$217k** BUY | vol 52,359 / OI 324
- **MU** CALL 800 2026-11-04 (0DTE): 188 @ 9.70 = **+$182k** BUY | vol 5,964 / OI 48
- **AMD** PUT 485 2026-11-04 (0DTE): 250 @ 6.26 = **+$156k** BUY | vol 6,778 / OI 351
- **QQQ** PUT 693 2026-11-04 (0DTE): 474 @ 3.13 = **+$148k** BUY | vol 86,253 / OI 528
- **TSLA** PUT 395 2026-11-04 (0DTE): 120 @ 11.70 = **+$140k** BUY | vol 2,036 / OI 2,219
- **NVDA** PUT 207.5 2026-11-06 (2DTE): 185 @ 6.45 = **+$119k** BUY | vol 3,849 / OI 3,670
- **QQQ** PUT 722 2026-11-04 (0DTE): 37 @ 30.96 = **+$115k** BUY | vol 68 / OI 390
- **QQQ** CALL 690 2026-11-05 (1DTE): 175 @ 6.21 = **+$109k** SELL | vol 5,497 / OI 925
- **AAPL** PUT 355 2026-11-04 (0DTE): 260 @ 4.05 = **+$105k** BUY | vol 8,749 / OI 76
- **TSLA** CALL 390 2026-11-11 (7DTE): 145 @ 7.25 = **+$105k** SELL | vol 2,573 / OI 87
- **MU** CALL 800 2026-11-04 (0DTE): 99 @ 10.60 = **+$105k** BUY | vol 5,964 / OI 48
- **AMD** PUT 480 2026-11-04 (0DTE): 250 @ 4.03 = **+$101k** BUY | vol 12,351 / OI 525
- **QQQ** PUT 691 2026-11-04 (0DTE): 400 @ 2.51 = **+$100k** BUY | vol 64,533 / OI 1,212

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 782 2026-11-05 (1DTE): 561 traded vs OI 0
- **SPY** CALL 785 2026-11-09 (5DTE): 1,161 traded vs OI 974
- **SPY** CALL 752 2026-11-04 (0DTE): 716 traded vs OI 714
- **SPY** PUT 731 2026-11-05 (1DTE): 542 traded vs OI 0
- **SPY** PUT 763 2026-11-12 (8DTE): 500 traded vs OI 0
- **SPY** CALL 767 2026-12-04 (30DTE): 607 traded vs OI 170
- **QQQ** PUT 651 2026-11-04 (0DTE): 554 traded vs OI 0
- **QQQ** PUT 692 2026-11-06 (2DTE): 1,604 traded vs OI 1,529
- **QQQ** CALL 690 2026-11-13 (9DTE): 1,655 traded vs OI 734
- **QQQ** CALL 760 2026-11-30 (26DTE): 501 traded vs OI 0
- **SMH** PUT 492.5 2026-11-04 (0DTE): 628 traded vs OI 278
- **NVDA** CALL 215 2026-11-09 (5DTE): 1,241 traded vs OI 1,203
- **NVDA** CALL 215 2026-11-16 (12DTE): 511 traded vs OI 115
- **NVDA** CALL 210 2026-11-06 (2DTE): 26,417 traded vs OI 26,310
- **NVDA** PUT 207.5 2026-11-06 (2DTE): 3,849 traded vs OI 3,670

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
