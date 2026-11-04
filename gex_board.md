# GEX + FLOW SCAN - Wed Nov 04, 01:20 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (10)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 13:05 | **AAPL** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/04 352.5P | 0.58 | 0.60 | +7% (6m) | **+3%** | +57% | 352.38 |
| 12:50 | **AMZN** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/04 267.5P | 0.40 | 0.22 | +17% (7m) | **-45%** | +109% | 267.48 |
| 11:38 | **QQQ** | **PUTS** | 1m FAILED POP (R3) | 11/04 686P | 0.80 | 0.15 | -1% (0m) | **-81%** (done) | +26% | 689.6 |
| 11:21 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/04 685P | 0.67 | 0.12 | +66% (7m) | **-82%** (done) | +25% | 690.3 hit |
| 10:20 | **SMCI** | **CALLS** | FLOW SURGE | 11/06 33C | 0.65 | 0.13 | -3% (1m) | **-80%** (done) | +39% | 32.81 |
| 10:20 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/04 284C | 0.49 | 0.17 | +2% (22m) | **-65%** (done) | +131% | 284.74 |
| 10:00 | **AMZN** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/04 267.5P | 0.68 | 1.54 | +169% (60m) | **+126%** (done) | +258% | 265.7 |
| 09:50 | **UBER** | **CALLS** | FLIP CROSS up into positive gamma | 11/06 71C | 0.60 | 1.56 | +168% (52m) | **+160%** (done) | +50% | 70 hit |
| 09:50 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/04 286C | 0.53 | 0.06 | +2% (1m) | **-89%** (done) | +150% | 287 |
| 09:45 | **UBER** | **PUTS** | FLIP CROSS down into negative gamma | 11/06 67P | 0.63 | 0.10 | -3% (1m) | **-84%** (done) | +27% | 68.03 |

## 1m RULES on SPY / QQQ - loose (2 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 13:20:08 ET, last candle SPY 13:19, QQQ 13:19 | no errors
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
| 1 | **AMZN** | 269.83 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 48 | none: 84 puts 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (38 contracts' greeks worked out here) | POS +$562.7M | - | 270 | 250 | -$22.7M | +$0 bull / -$988k bear | LONG (clean 36, ADX 37, RVol 1.2) |
| 2 | **AAPL** | 353.80 | FLOW SURGE | **PUTS** | 37 | 11/04 352.5P @ 0.64 (delta 0.32) = est +59% at 351.98 | POS +$1.1B | 342.34 | 355 | 350 | -$81.8M | +$462k bull / -$530k bear | out (clean 32, ADX 41, RVol 0.8) |
| 3 | **SMH** | 506.42 | FLOW SURGE | **CALLS** | 34 | none: 156 calls 0-7DTE > 8 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (71 contracts' greeks worked out here) | NEG -$547.7M | - | 532.5 | 500 | +$21.3M | +$56k bull / +$0 bear | out (clean 32, ADX 14, RVol 0.3) |
| 4 | **NVDA** | 204.07 | FLIP CROSS up into positive gamma | **CALLS** | 28 | 11/04 205C @ 0.40 (delta 0.31) = est +21% at 205 | NEG -$3.9M | 204.06 | 210 | 200 | -$483k | +$129k bull / -$415k bear | out (clean 30, ADX 16, RVol 0.7) |
| 5 | **GOOGL** | 292.44 | - | **-** | 24 | - | POS +$98.3M | 285.63 | 290 | 290 | -$27.1M | +$53k bull / -$48k bear | out (clean 36, ADX 20, RVol 0.3) |
| 6 | **MSFT** | 556.09 | - | **-** | 22 | - | POS +$1.0B | - | 550 | 535 | -$16.6M | +$328k bull / -$176k bear | out (clean 29, ADX 35, RVol 0.6) |
| 7 | **TSLA** | 389.28 | - | **-** | 21 | - | NEG -$102.6M | 396.11 | 400 | 380 | -$81.0M | +$2.0M bull / -$634k bear | out (clean 31, ADX 20, RVol 0.6) |
| 8 | **MSTR** | 145.53 | - | **-** | 21 | - | POS +$121.8M | - | 135 | 150 | -$6.4M | +$0 bull / -$11.7M bear | out (clean 31, ADX 34, RVol 0.3) |
| 9 | **MU** | 806.93 | - | **-** | 20 | - | NEG -$378.8M | - | 850 | 800 | +$103.2M | +$1.9M bull / -$537k bear | out (clean 31, ADX 19, RVol 0.4) |
| 10 | **SPY** | 768.53 | - | **-** | 18 | - | NEG -$1.8B | 769.89 | 770 | 767 | -$118.4M | +$1.2M bull / +$0 bear | out (clean 32, ADX 27, RVol 0.4) |
| 11 | **AMD** | 483.28 | - | **-** | 18 | - | NEG -$95.0M | - | 500 | 440 | +$46.0M | +$430k bull / -$56k bear | out (clean 32, ADX 10, RVol 0.5) |
| 12 | **SMCI** | 30.15 | - | **-** | 18 | - | NEG -$580k | 31.94 | 33 | 30 | +$2.0M | - | out (clean 33, ADX 25, RVol 1.1) |
| 13 | **ORCL** | 126.05 | - | **-** | 18 | - | NEG -$31.8M | - | 130 | 125 | +$2.6M | +$85k bull / +$0 bear | out (clean 34, ADX 8, RVol 1.0) |
| 14 | **IWM** | 284.10 | - | **-** | 17 | - | NEG -$139.0M | 284.48 | 285 | 270 | +$9.4M | +$111k bull / -$61k bear | out (clean 35, ADX 16, RVol 0.6) |
| 15 | **HOOD** | 88.05 | - | **-** | 17 | - | POS +$3.3M | 84.4 | 90 | 90 | -$833k | +$87k bull / +$0 bear | out (clean 28, ADX 23, RVol 0.8) |
| 16 | **QQQ** | 695.48 | - | **-** | 16 | - | NEG -$4.6B | 719.55 | 700 | 680 | -$133.9M | +$570k bull / +$0 bear | out (clean 32, ADX 11, RVol 0.6) |
| 17 | **META** | 636.72 | - | **-** | 16 | - | POS +$214.5M | 623.33 | 650 | 625 | +$3.0M | +$1.0M bull / +$0 bear | out (clean 31, ADX 24, RVol 0.5) |
| 18 | **UBER** | 71.46 | - | **-** | 14 | - | POS +$13.1M | 68.13 | 70 | 70 | -$1.2M | - | out (clean 30, ADX 25, RVol 0.7) |
| 19 | **BABA** | 107.29 | - | **-** | 14 | - | POS +$16.1M | - | 110 | 110 | -$847k | - | out (clean 36, ADX 28, RVol 0.7) |
| 20 | **NFLX** | 66.03 | - | **-** | 13 | - | POS +$21.8M | 62.54 | 65 | 65 | -$1.9M | - | out (clean 31, ADX 28, RVol 0.9) |
| 21 | **COIN** | 152.73 | - | **-** | 11 | - | POS +$28.5M | - | 148 | 150 | -$1.2M | - | out (clean 31, ADX 20, RVol 0.2) |
| 22 | **SHOP** | 151.86 | - | **-** | 11 | - | NEG -$5.2M | - | 160 | 150 | -$349k | - | out (clean 33, ADX 18, RVol 0.3) |
| 23 | **ARM** | 192.72 | - | **-** | 10 | - | NEG -$7.3M | - | 200 | 200 | +$728k | - | out (clean 26, ADX 22, RVol 0.6) |
| 24 | **CRM** | 226.66 | - | **-** | 9 | - | NEG -$13.0M | - | 240 | 220 | -$185k | - | out (clean 34, ADX 24, RVol 0.3) |
| 25 | **AVGO** | 328.37 | - | **-** | 6 | - | NEG -$88.6M | 346.82 | 340 | 330 | +$2.5M | - | out (clean 30, ADX 14, RVol 0.8) |
| 26 | **PLTR** | 171.34 | - | **-** | 6 | - | NEG -$51.3M | - | 165 | 170 | -$1.3M | - | out (clean 26, ADX 20, RVol 0.5) |
| 27 | **DELL** | 373.63 | - | **-** | 6 | - | NEG -$30.6M | - | 400 | 400 | +$1.5M | - | out (clean 32, ADX 16, RVol 0.5) |

## Big prints this scan (38)
- **SPY** CALL 768 2026-11-04 (0DTE): 6,445 @ 1.67 = **+$1.1M** BUY | vol 411,380 / OI 1,095
- **TSLA** PUT 392.5 2026-11-06 (2DTE): 200 @ 7.17 = **+$143k** SELL | vol 1,123 / OI 3,501
- **AAPL** CALL 360 2026-11-06 (2DTE): 860 @ 1.40 = **+$120k** BUY | vol 46,149 / OI 14,715
- **TSLA** CALL 392.5 2026-11-06 (2DTE): 194 @ 6.00 = **+$116k** BUY | vol 5,231 / OI 718
- **AAPL** PUT 350 2026-11-06 (2DTE): 436 @ 1.97 = **+$86k** SELL | vol 22,368 / OI 2,166
- **NVDA** CALL 202.5 2026-11-06 (2DTE): 201 @ 3.90 = **+$78k** SELL | vol 7,343 / OI 1,974
- **AMZN** PUT 270 2026-11-04 (0DTE): 450 @ 1.24 = **+$56k** BUY | vol 16,425 / OI 0
- **MU** PUT 800 2026-11-06 (2DTE): 35 @ 15.25 = **+$53k** SELL | vol 9,126 / OI 3,802
- **GOOGL** CALL 290 2026-11-04 (0DTE): 200 @ 2.65 = **+$53k** BUY | vol 22,707 / OI 1,742
- **MU** CALL 815 2026-11-09 (5DTE): 20 @ 23.22 = **+$46k** BUY | vol 658 / OI 7
- **NVDA** PUT 202.5 2026-11-04 (0DTE): 1,058 @ 0.43 = **+$45k** BUY | vol 152,495 / OI 3,586
- **TSLA** CALL 385 2026-11-06 (2DTE): 45 @ 10.00 = **+$45k** BUY | vol 11,742 / OI 1,566
- **TSLA** PUT 390 2026-11-04 (0DTE): 300 @ 1.50 = **+$45k** SELL | vol 27,860 / OI 2,517
- **TSLA** PUT 390 2026-11-04 (0DTE): 259 @ 1.65 = **+$43k** SELL | vol 27,860 / OI 2,517
- **META** CALL 635 2026-11-09 (5DTE): 30 @ 14.00 = **+$42k** BUY | vol 614 / OI 58

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 789 2026-11-10 (6DTE): 690 traded vs OI 0
- **SPY** CALL 779 2026-11-09 (5DTE): 552 traded vs OI 0
- **SPY** PUT 767 2026-11-27 (23DTE): 590 traded vs OI 471
- **SPY** PUT 760 2026-12-04 (30DTE): 636 traded vs OI 493
- **QQQ** CALL 713 2026-11-06 (2DTE): 8,993 traded vs OI 8,652
- **NVDA** CALL 192.5 2026-11-09 (5DTE): 519 traded vs OI 41
- **TSLA** CALL 390 2026-11-20 (16DTE): 2,284 traded vs OI 2,272
- **AMZN** CALL 275 2026-11-13 (9DTE): 2,302 traded vs OI 2,300
- **AMZN** CALL 285 2026-12-04 (30DTE): 658 traded vs OI 614
- **MSFT** CALL 552.5 2026-11-13 (9DTE): 505 traded vs OI 143
- **AVGO** PUT 345 2026-11-04 (0DTE): 508 traded vs OI 110
- **MU** PUT 810 2026-11-09 (5DTE): 743 traded vs OI 710
- **HOOD** PUT 90 2026-11-13 (9DTE): 1,299 traded vs OI 1,255
- **HOOD** PUT 89 2026-11-27 (23DTE): 504 traded vs OI 248
- **BABA** CALL 107 2026-11-06 (2DTE): 1,156 traded vs OI 1,140

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
