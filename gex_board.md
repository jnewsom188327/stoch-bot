# GEX + FLOW SCAN - Wed Nov 04, 01:50 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (10)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 13:05 | **AAPL** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/04 352.5P | 0.58 | 0.90 | +76% (29m) | **+55%** | +57% | 352.38 hit |
| 12:50 | **AMZN** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/04 267.5P | 0.40 | 0.70 | +100% (55m) | **+75%** | +109% | 267.48 |
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
Last 1m check 13:50:08 ET, last candle SPY 13:49, QQQ 13:49 | no errors
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
| 1 | **GOOGL** | 290.70 | PINNED between the walls (positive gamma) - chop | **-** | 34 | - | POS +$105.8M | 282.75 | 290 | 290 | -$26.3M | +$39k bull / +$0 bear | out (clean 36, ADX 16, RVol 0.3) |
| 2 | **AAPL** | 352.62 | - | **-** | 26 | - | POS +$1.0B | 342.46 | 355 | 350 | -$78.0M | +$105k bull / -$27k bear | out (clean 32, ADX 27, RVol 0.6) |
| 3 | **AMZN** | 267.80 | - | **-** | 21 | - | POS +$567.8M | - | 270 | 250 | -$19.1M | +$423k bull / +$0 bear | out (clean 36, ADX 30, RVol 0.6) |
| 4 | **MSFT** | 554.92 | - | **-** | 21 | - | POS +$1.0B | - | 550 | 535 | -$16.5M | +$0 bull / -$93k bear | out (clean 29, ADX 28, RVol 0.9) |
| 5 | **COIN** | 152.60 | - | **-** | 21 | - | POS +$28.6M | - | 148 | 150 | -$1.2M | +$0 bull / -$248k bear | out (clean 31, ADX 20, RVol 0.2) |
| 6 | **ARM** | 191.67 | - | **-** | 21 | - | NEG -$7.1M | - | 200 | 200 | +$919k | +$27k bull / +$0 bear | out (clean 26, ADX 27, RVol 0.7) |
| 7 | **MU** | 806.74 | - | **-** | 20 | - | NEG -$380.9M | - | 850 | 800 | +$104.0M | +$1.2M bull / -$70k bear | out (clean 31, ADX 17, RVol 0.5) |
| 8 | **TSLA** | 389.50 | - | **-** | 19 | - | NEG -$104.4M | 396.6 | 400 | 390 | -$82.2M | +$213k bull / -$1.0M bear | out (clean 31, ADX 16, RVol 0.3) |
| 9 | **AMD** | 482.27 | - | **-** | 19 | - | NEG -$102.2M | - | 500 | 500 | +$49.6M | +$643k bull / -$52k bear | out (clean 32, ADX 14, RVol 0.5) |
| 10 | **META** | 630.25 | - | **-** | 18 | - | POS +$145.7M | 621.48 | 650 | 625 | +$7.5M | +$651k bull / +$0 bear | out (clean 31, ADX 24, RVol 1.2) |
| 11 | **SMCI** | 29.93 | - | **-** | 18 | - | NEG -$994k | - | 32 | 30 | +$2.0M | - | out (clean 34, ADX 24, RVol 0.9) |
| 12 | **SPY** | 767.59 | - | **-** | 16 | - | NEG -$3.1B | 769.77 | 770 | 767 | -$89.0M | +$2.2M bull / +$0 bear | out (clean 32, ADX 20, RVol 0.4) |
| 13 | **QQQ** | 693.58 | - | **-** | 15 | - | NEG -$4.9B | 719.57 | 700 | 680 | -$111.4M | +$716k bull / +$0 bear | out (clean 32, ADX 11, RVol 0.6) |
| 14 | **SMH** | 504.10 | - | **-** | 15 | - | NEG -$577.4M | - | 532.5 | 500 | +$21.7M | - | out (clean 32, ADX 15, RVol 0.3) |
| 15 | **PLTR** | 170.92 | - | **-** | 15 | - | NEG -$50.1M | - | 165 | 170 | -$1.3M | +$223k bull / +$0 bear | out (clean 26, ADX 14, RVol 0.7) |
| 16 | **NVDA** | 203.50 | - | **-** | 14 | - | NEG -$46.6M | 204.02 | 210 | 200 | +$2.4M | +$405k bull / +$0 bear | out (clean 30, ADX 14, RVol 0.8) |
| 17 | **MSTR** | 145.50 | - | **-** | 13 | - | POS +$122.6M | - | 135 | 150 | -$10.2M | - | out (clean 31, ADX 33, RVol 0.3) |
| 18 | **UBER** | 71.24 | - | **-** | 12 | - | POS +$12.5M | 68.38 | 70 | 70 | -$1.1M | - | out (clean 30, ADX 20, RVol 0.7) |
| 19 | **BABA** | 106.76 | - | **-** | 12 | - | POS +$16.9M | - | 110 | 110 | -$771k | - | out (clean 36, ADX 22, RVol 0.6) |
| 20 | **NFLX** | 65.83 | - | **-** | 11 | - | POS +$21.5M | 62.19 | 65 | 65 | -$1.9M | - | out (clean 31, ADX 23, RVol 0.6) |
| 21 | **ORCL** | 125.48 | - | **-** | 11 | - | NEG -$32.4M | - | 130 | 125 | +$3.0M | - | out (clean 35, ADX 16, RVol 1.4) |
| 22 | **SHOP** | 151.27 | - | **-** | 10 | - | NEG -$5.7M | - | 160 | 150 | -$347k | - | out (clean 33, ADX 14, RVol 0.3) |
| 23 | **CRM** | 225.87 | - | **-** | 7 | - | NEG -$13.1M | - | 240 | 220 | -$123k | - | out (clean 34, ADX 23, RVol 0.4) |
| 24 | **IWM** | 283.90 | - | **-** | 6 | - | NEG -$195.1M | 284.41 | 285 | 270 | +$10.1M | - | out (clean 35, ADX 11, RVol 0.5) |
| 25 | **AVGO** | 326.82 | - | **-** | 6 | - | NEG -$99.5M | - | 340 | 330 | +$3.2M | - | out (clean 30, ADX 15, RVol 0.4) |
| 26 | **DELL** | 372.70 | - | **-** | 6 | - | NEG -$29.0M | - | 400 | 400 | +$1.6M | - | out (clean 32, ADX 12, RVol 0.7) |
| 27 | **HOOD** | 87.90 | - | **-** | 6 | - | POS +$3.2M | 84.37 | 90 | 90 | -$838k | - | out (clean 28, ADX 21, RVol 0.3) |

## Big prints this scan (49)
- **COIN** CALL 147 2026-11-06 (2DTE): 349 @ 7.11 = **+$248k** SELL | vol 640 / OI 6,274
- **QQQ** PUT 696 2026-11-04 (0DTE): 966 @ 2.00 = **+$193k** SELL | vol 132,727 / OI 1,233
- **QQQ** PUT 697 2026-11-06 (2DTE): 270 @ 6.67 = **+$180k** SELL | vol 3,320 / OI 657
- **TSLA** PUT 400 2026-11-11 (7DTE): 100 @ 16.25 = **+$162k** MID | vol 133 / OI 283
- **TSLA** PUT 395 2026-11-11 (7DTE): 100 @ 13.10 = **+$131k** BUY | vol 153 / OI 250
- **SPY** PUT 760 2026-11-06 (2DTE): 1,000 @ 1.25 = **+$125k** SELL | vol 27,441 / OI 12,306
- **QQQ** CALL 694 2026-11-06 (2DTE): 196 @ 6.33 = **+$124k** BUY | vol 3,913 / OI 566
- **SPY** PUT 760 2026-11-06 (2DTE): 1,000 @ 1.22 = **+$122k** SELL | vol 27,441 / OI 12,306
- **SPY** PUT 760 2026-11-06 (2DTE): 1,000 @ 1.21 = **+$121k** SELL | vol 27,441 / OI 12,306
- **SPY** PUT 760 2026-11-06 (2DTE): 990 @ 1.19 = **+$118k** SELL | vol 27,441 / OI 12,306
- **SPY** PUT 760 2026-11-06 (2DTE): 926 @ 1.20 = **+$111k** SELL | vol 27,441 / OI 12,306
- **SPY** CALL 773 2026-11-10 (6DTE): 358 @ 2.92 = **+$105k** BUY | vol 2,840 / OI 0
- **SPY** CALL 773 2026-11-10 (6DTE): 358 @ 2.92 = **+$105k** BUY | vol 2,840 / OI 0
- **TSLA** CALL 390 2026-11-06 (2DTE): 171 @ 6.05 = **+$103k** SELL | vol 20,294 / OI 2,560
- **TSLA** PUT 390 2026-11-06 (2DTE): 148 @ 6.80 = **+$101k** SELL | vol 8,911 / OI 4,169

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 773 2026-11-10 (6DTE): 2,840 traded vs OI 0
- **QQQ** CALL 710 2026-11-10 (6DTE): 1,230 traded vs OI 1,201
- **QQQ** CALL 712 2026-11-06 (2DTE): 2,612 traded vs OI 2,555
- **QQQ** PUT 650 2026-11-11 (7DTE): 511 traded vs OI 344
- **IWM** CALL 291 2026-11-20 (16DTE): 2,939 traded vs OI 2,931
- **AMD** CALL 510 2026-11-13 (9DTE): 506 traded vs OI 268
- **AMZN** CALL 290 2026-12-04 (30DTE): 500 traded vs OI 398
- **PLTR** PUT 167.5 2026-11-13 (9DTE): 685 traded vs OI 668
- **MU** PUT 780 2026-11-09 (5DTE): 501 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
