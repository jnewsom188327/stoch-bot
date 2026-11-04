# GEX + FLOW SCAN - Wed Nov 04, 01:00 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (9)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 12:50 | **AMZN** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/04 267.5P | 0.40 | 0.40 | +17% (7m) | **+0%** | +109% | 267.48 |
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
Last 1m check 13:00:08 ET, last candle SPY 12:59, QQQ 12:59 | no errors
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
| 1 | **SMH** | 508.46 | FLOW SURGE | **CALLS** | 37 | none: 158 calls 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (74 contracts' greeks worked out here) | NEG -$531.6M | - | 532.5 | 500 | +$20.7M | +$26k bull / +$0 bear | out (clean 32, ADX 15, RVol 0.7) |
| 2 | **AAPL** | 354.00 | FLOW SURGE | **PUTS** | 36 | 11/04 352.5P @ 0.67 (delta 0.31) = est +61% at 352.05 | POS +$1.1B | 342.97 | 355 | 350 | -$81.1M | +$0 bull / -$637k bear | out (clean 32, ADX 42, RVol 0.6) |
| 3 | **AMZN** | 269.09 | TREND (flow not with it) | **CALLS** | 33 | none: 88 calls 0-7DTE > 7 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only +8% at the target (needs +20%) (41 contracts' greeks worked out here) | POS +$562.4M | - | 270 | 250 | -$21.4M | +$44k bull / -$149k bear | LONG (clean 35, ADX 35, RVol 1.3) |
| 4 | **MSFT** | 552.83 | - | **-** | 24 | - | POS +$1.0B | - | 550 | 535 | -$16.1M | +$361k bull / -$250k bear | out (clean 29, ADX 43, RVol 1.3) |
| 5 | **TSLA** | 391.04 | - | **-** | 21 | - | NEG -$68.3M | 395.47 | 400 | 390 | -$87.9M | +$0 bull / -$2.1M bear | out (clean 31, ADX 20, RVol 0.6) |
| 6 | **MU** | 812.21 | - | **-** | 21 | - | NEG -$369.9M | - | 850 | 800 | +$99.1M | +$694k bull / -$672k bear | out (clean 32, ADX 21, RVol 0.5) |
| 7 | **SPY** | 768.83 | - | **-** | 19 | - | NEG -$1.3B | 769.92 | 770 | 750 | -$132.7M | +$170k bull / -$3.1M bear | out (clean 32, ADX 27, RVol 0.6) |
| 8 | **SMCI** | 30.34 | - | **-** | 19 | - | NEG -$551k | - | 33 | 30 | +$1.9M | - | out (clean 33, ADX 30, RVol 1.0) |
| 9 | **AMD** | 487.77 | - | **-** | 18 | - | NEG -$86.4M | - | 500 | 500 | +$42.9M | +$68k bull / -$73k bear | out (clean 32, ADX 8, RVol 0.5) |
| 10 | **DELL** | 374.17 | - | **-** | 18 | - | NEG -$30.4M | - | 400 | 400 | +$1.3M | +$226k bull / +$0 bear | out (clean 33, ADX 20, RVol 0.9) |
| 11 | **QQQ** | 696.49 | - | **-** | 17 | - | NEG -$4.3B | 718.81 | 700 | 680 | -$148.2M | +$0 bull / -$588k bear | out (clean 31, ADX 13, RVol 0.6) |
| 12 | **NVDA** | 203.57 | - | **-** | 16 | - | NEG -$33.6M | 203.98 | 210 | 200 | -$152k | +$82k bull / -$633k bear | out (clean 30, ADX 21, RVol 1.0) |
| 13 | **META** | 639.72 | - | **-** | 16 | - | POS +$248.3M | 624.4 | 650 | 625 | -$685k | +$635k bull / -$140k bear | out (clean 31, ADX 26, RVol 0.7) |
| 14 | **AVGO** | 329.69 | - | **-** | 16 | - | NEG -$81.7M | 348.85 | 340 | 330 | +$1.9M | +$0 bull / -$68k bear | out (clean 30, ADX 17, RVol 0.9) |
| 15 | **PLTR** | 170.86 | - | **-** | 16 | - | NEG -$51.1M | - | 165 | 170 | -$1.3M | +$0 bull / -$46k bear | out (clean 26, ADX 23, RVol 0.5) |
| 16 | **UBER** | 71.11 | - | **-** | 15 | - | POS +$11.3M | 68.55 | 70 | 70 | -$1.1M | - | out (clean 30, ADX 30, RVol 1.1) |
| 17 | **GOOGL** | 292.03 | - | **-** | 14 | - | POS +$104.4M | 282.12 | 290 | 290 | -$27.3M | - | out (clean 36, ADX 20, RVol 0.4) |
| 18 | **NFLX** | 66.16 | - | **-** | 14 | - | POS +$19.3M | 62.25 | 65 | 65 | -$1.9M | - | out (clean 31, ADX 34, RVol 0.9) |
| 19 | **BABA** | 106.81 | - | **-** | 14 | - | POS +$16.7M | - | 110 | 110 | -$809k | - | out (clean 36, ADX 30, RVol 0.8) |
| 20 | **SHOP** | 152.12 | - | **-** | 12 | - | NEG -$5.3M | - | 160 | 150 | -$359k | - | out (clean 33, ADX 22, RVol 0.3) |
| 21 | **COIN** | 152.40 | - | **-** | 11 | - | POS +$28.2M | - | 148 | 150 | -$1.3M | - | out (clean 31, ADX 18, RVol 0.2) |
| 22 | **IWM** | 284.30 | - | **-** | 9 | - | NEG -$58.4M | 284.54 | 285 | 270 | +$8.9M | - | out (clean 34, ADX 18, RVol 1.3) |
| 23 | **CRM** | 225.94 | - | **-** | 9 | - | NEG -$12.6M | - | 240 | 220 | -$122k | - | out (clean 33, ADX 30, RVol 0.3) |
| 24 | **ORCL** | 126.32 | - | **-** | 8 | - | NEG -$30.1M | - | 130 | 125 | +$2.4M | - | out (clean 35, ADX 9, RVol 1.1) |
| 25 | **MSTR** | 145.18 | - | **-** | 7 | - | POS +$122.5M | - | 135 | 150 | +$704k | - | out (clean 31, ADX 32, RVol 0.2) |
| 26 | **HOOD** | 88.47 | - | **-** | 6 | - | POS +$3.0M | 84.82 | 90 | 90 | -$1.0M | - | out (clean 28, ADX 20, RVol 0.4) |
| 27 | **ARM** | 196.59 | - | **-** | 6 | - | NEG -$7.2M | - | 212.5 | 200 | +$284k | - | out (clean 26, ADX 18, RVol 0.3) |

## Big prints this scan (54)
- **SPY** PUT 772 2026-11-05 (1DTE): 5,993 @ 4.72 = **+$2.8M** BUY | vol 6,602 / OI 0
- **TSLA** PUT 395 2026-11-04 (0DTE): 474 @ 5.25 = **+$249k** BUY | vol 3,002 / OI 2,219
- **META** CALL 650 2026-11-06 (2DTE): 188 @ 6.10 = **+$115k** BUY | vol 7,097 / OI 4,249
- **TSLA** CALL 390 2026-11-06 (2DTE): 174 @ 6.50 = **+$113k** SELL | vol 17,719 / OI 2,560
- **TSLA** CALL 392.5 2026-11-06 (2DTE): 187 @ 5.05 = **+$94k** SELL | vol 4,415 / OI 718
- **META** CALL 640 2026-11-06 (2DTE): 89 @ 10.04 = **+$89k** BUY | vol 7,469 / OI 6,825
- **META** CALL 640 2026-11-04 (0DTE): 301 @ 2.80 = **+$84k** BUY | vol 43,455 / OI 670
- **META** CALL 642.5 2026-11-06 (2DTE): 89 @ 8.80 = **+$78k** BUY | vol 1,567 / OI 665
- **META** CALL 650 2026-11-06 (2DTE): 125 @ 6.10 = **+$76k** BUY | vol 7,097 / OI 4,249
- **NVDA** CALL 202.5 2026-11-06 (2DTE): 199 @ 3.62 = **+$72k** SELL | vol 7,036 / OI 1,974
- **MU** PUT 795 2026-11-04 (0DTE): 496 @ 1.40 = **+$69k** BUY | vol 20,007 / OI 1,083
- **MU** PUT 850 2026-11-06 (2DTE): 15 @ 46.25 = **+$69k** BUY | vol 1,306 / OI 1,724
- **TSLA** CALL 392.5 2026-11-06 (2DTE): 136 @ 5.00 = **+$68k** SELL | vol 4,415 / OI 718
- **NVDA** CALL 210 2026-11-11 (7DTE): 300 @ 2.21 = **+$66k** SELL | vol 3,137 / OI 204
- **TSLA** CALL 390 2026-11-06 (2DTE): 100 @ 6.49 = **+$65k** SELL | vol 17,719 / OI 2,560

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 722 2026-11-05 (1DTE): 526 traded vs OI 0
- **SPY** PUT 721 2026-11-05 (1DTE): 543 traded vs OI 0
- **QQQ** PUT 695 2026-11-06 (2DTE): 8,742 traded vs OI 8,477
- **QQQ** CALL 765 2026-11-20 (16DTE): 541 traded vs OI 0
- **NVDA** CALL 212.5 2026-11-11 (7DTE): 501 traded vs OI 128
- **TSLA** CALL 430 2026-11-09 (5DTE): 688 traded vs OI 0
- **TSLA** CALL 430 2026-11-27 (23DTE): 621 traded vs OI 0
- **TSLA** CALL 430 2026-11-13 (9DTE): 913 traded vs OI 0
- **TSLA** CALL 430 2026-11-20 (16DTE): 2,170 traded vs OI 0
- **TSLA** CALL 395 2026-11-11 (7DTE): 556 traded vs OI 429
- **TSLA** CALL 430 2026-11-06 (2DTE): 3,478 traded vs OI 0
- **TSLA** CALL 430 2026-11-04 (0DTE): 1,060 traded vs OI 0
- **AAPL** CALL 347.5 2026-11-09 (5DTE): 504 traded vs OI 148
- **AMZN** CALL 267.5 2026-11-09 (5DTE): 510 traded vs OI 55
- **AMZN** PUT 247.5 2026-11-13 (9DTE): 689 traded vs OI 401

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
