# GEX + FLOW SCAN - Wed Nov 04, 02:00 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (10)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 13:05 | **AAPL** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/04 352.5P | 0.58 | 0.71 | +76% (29m) | **+22%** | +57% | 352.38 hit |
| 12:50 | **AMZN** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/04 267.5P | 0.40 | 0.76 | +100% (55m) | **+90%** (done) | +109% | 267.48 |
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
Last 1m check 14:00:08 ET, last candle SPY 13:59, QQQ 13:59 | no errors
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
| 1 | **SMCI** | 29.63 | FLOW SURGE | **CALLS** | 47 | none: 12 calls 0-7DTE > 2 priced 0.40-0.80 > 2 delta 0.2+ > 2 spread ok > 2 liquid > best one only +12% at the target (needs +20%) | NEG -$944k | - | 32 | 30 | +$2.0M | +$38k bull / +$0 bear | SHORT (clean 34, ADX 27, RVol 1.4) |
| 2 | **SMH** | 503.28 | FLOW SURGE | **CALLS** | 36 | 11/04 507.5C @ 0.66 (delta 0.21) = est +54% at 506.89 | NEG -$572.7M | - | 532.5 | 500 | +$22.4M | +$30k bull / +$0 bear | out (clean 33, ADX 18, RVol 0.4) |
| 3 | **GOOGL** | 290.48 | PINNED between the walls (positive gamma) - chop | **-** | 33 | - | POS +$99.3M | 283.44 | 290 | 290 | -$25.9M | +$39k bull / +$0 bear | out (clean 36, ADX 17, RVol 0.2) |
| 4 | **AAPL** | 352.82 | - | **-** | 25 | - | POS +$1.1B | 341.81 | 355 | 350 | -$78.3M | +$60k bull / -$152k bear | out (clean 32, ADX 24, RVol 0.5) |
| 5 | **ARM** | 191.10 | - | **-** | 22 | - | NEG -$7.3M | - | 200 | 200 | +$1.0M | +$27k bull / +$0 bear | out (clean 27, ADX 29, RVol 0.7) |
| 6 | **MSFT** | 555.06 | - | **-** | 21 | - | POS +$1.0B | - | 550 | 535 | -$16.3M | +$33k bull / -$93k bear | out (clean 29, ADX 24, RVol 1.1) |
| 7 | **AMD** | 480.84 | - | **-** | 20 | - | NEG -$99.6M | - | 500 | 440 | +$51.4M | +$940k bull / +$0 bear | out (clean 32, ADX 16, RVol 0.4) |
| 8 | **AMZN** | 268.04 | - | **-** | 20 | - | POS +$565.8M | - | 270 | 250 | -$18.3M | +$332k bull / +$0 bear | out (clean 36, ADX 26, RVol 0.5) |
| 9 | **COIN** | 152.16 | - | **-** | 20 | - | POS +$29.4M | - | 148 | 150 | -$1.2M | +$0 bull / -$248k bear | out (clean 31, ADX 18, RVol 0.2) |
| 10 | **MU** | 803.16 | - | **-** | 20 | - | NEG -$365.7M | - | 850 | 800 | +$110.0M | +$4.2M bull / +$0 bear | out (clean 32, ADX 18, RVol 0.6) |
| 11 | **TSLA** | 388.96 | - | **-** | 19 | - | NEG -$99.0M | 395.06 | 400 | 390 | -$80.5M | +$265k bull / -$688k bear | out (clean 31, ADX 14, RVol 0.3) |
| 12 | **META** | 628.75 | - | **-** | 19 | - | POS +$145.3M | 619.14 | 650 | 625 | +$10.6M | +$890k bull / +$0 bear | out (clean 32, ADX 27, RVol 1.1) |
| 13 | **SPY** | 767.38 | - | **-** | 16 | - | NEG -$3.1B | 769.47 | 770 | 767 | -$80.0M | +$2.8M bull / +$0 bear | out (clean 32, ADX 18, RVol 0.4) |
| 14 | **QQQ** | 693.00 | - | **-** | 15 | - | NEG -$4.9B | 718.99 | 700 | 680 | -$102.2M | +$1.1M bull / +$0 bear | out (clean 33, ADX 14, RVol 0.5) |
| 15 | **NVDA** | 202.92 | - | **-** | 15 | - | NEG -$60.9M | 203.87 | 210 | 200 | +$4.4M | +$700k bull / +$0 bear | out (clean 30, ADX 15, RVol 0.6) |
| 16 | **PLTR** | 170.76 | - | **-** | 14 | - | NEG -$50.4M | - | 165 | 170 | -$1.1M | +$162k bull / +$0 bear | out (clean 26, ADX 13, RVol 0.4) |
| 17 | **MSTR** | 145.29 | - | **-** | 12 | - | POS +$124.8M | - | 135 | 150 | -$9.8M | - | out (clean 31, ADX 31, RVol 0.4) |
| 18 | **UBER** | 71.36 | - | **-** | 12 | - | POS +$12.7M | 68.24 | 70 | 70 | -$1.1M | - | out (clean 30, ADX 18, RVol 0.6) |
| 19 | **NFLX** | 66.06 | - | **-** | 11 | - | POS +$21.0M | 62.31 | 65 | 65 | -$1.9M | - | out (clean 31, ADX 20, RVol 0.6) |
| 20 | **ORCL** | 125.40 | - | **-** | 11 | - | NEG -$32.9M | - | 130 | 125 | +$3.2M | - | out (clean 35, ADX 18, RVol 1.3) |
| 21 | **BABA** | 106.64 | - | **-** | 11 | - | POS +$16.5M | - | 110 | 110 | -$731k | - | out (clean 36, ADX 21, RVol 0.7) |
| 22 | **SHOP** | 151.56 | - | **-** | 10 | - | NEG -$5.7M | - | 160 | 150 | -$350k | - | out (clean 33, ADX 13, RVol 0.4) |
| 23 | **AVGO** | 326.07 | - | **-** | 7 | - | NEG -$102.4M | - | 340 | 320 | +$3.8M | - | out (clean 30, ADX 17, RVol 0.5) |
| 24 | **CRM** | 226.35 | - | **-** | 7 | - | NEG -$12.8M | - | 240 | 220 | -$129k | - | out (clean 34, ADX 20, RVol 0.3) |
| 25 | **IWM** | 283.89 | - | **-** | 6 | - | NEG -$167.4M | 284.35 | 285 | 270 | +$10.4M | - | out (clean 35, ADX 11, RVol 0.4) |
| 26 | **DELL** | 369.37 | - | **-** | 6 | - | NEG -$28.3M | - | 400 | 400 | +$1.6M | - | out (clean 32, ADX 13, RVol 0.8) |
| 27 | **HOOD** | 87.74 | - | **-** | 5 | - | POS +$2.9M | 84.95 | 90 | 90 | -$716k | - | out (clean 29, ADX 18, RVol 0.4) |

## Big prints this scan (26)
- **SPY** CALL 757 2026-11-05 (1DTE): 100 @ 10.99 = **+$110k** BUY | vol 996 / OI 0
- **META** CALL 630 2026-11-06 (2DTE): 100 @ 9.70 = **+$97k** BUY | vol 2,923 / OI 1,996
- **META** CALL 632.5 2026-11-06 (2DTE): 100 @ 8.40 = **+$84k** BUY | vol 2,231 / OI 1,305
- **AMD** PUT 485 2026-11-04 (0DTE): 172 @ 4.50 = **+$77k** SELL | vol 10,490 / OI 351
- **TSLA** PUT 390 2026-11-06 (2DTE): 88 @ 6.60 = **+$58k** SELL | vol 9,100 / OI 4,169
- **NVDA** CALL 202.5 2026-11-11 (7DTE): 100 @ 5.66 = **+$57k** BUY | vol 844 / OI 117
- **META** PUT 635 2026-11-04 (0DTE): 100 @ 5.40 = **+$54k** SELL | vol 11,395 / OI 171
- **MU** PUT 800 2026-11-04 (0DTE): 233 @ 1.88 = **+$44k** SELL | vol 61,764 / OI 1,387
- **AAPL** CALL 340 2026-11-06 (2DTE): 32 @ 13.28 = **+$42k** SELL | vol 3,793 / OI 3,962
- **AMD** CALL 485 2026-11-04 (0DTE): 182 @ 2.33 = **+$42k** BUY | vol 10,219 / OI 228
- **NVDA** CALL 205 2026-11-06 (2DTE): 140 @ 2.72 = **+$38k** BUY | vol 30,406 / OI 5,568
- **MU** CALL 810 2026-11-06 (2DTE): 20 @ 18.50 = **+$37k** BUY | vol 3,721 / OI 59
- **TSLA** PUT 387.5 2026-11-06 (2DTE): 65 @ 5.45 = **+$35k** SELL | vol 6,982 / OI 2,978
- **TSLA** PUT 387.5 2026-11-04 (0DTE): 385 @ 0.89 = **+$34k** BUY | vol 69,851 / OI 703
- **AMZN** CALL 272.5 2026-11-06 (2DTE): 200 @ 1.70 = **+$34k** BUY | vol 7,299 / OI 1,894

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 756 2026-11-09 (5DTE): 526 traded vs OI 0
- **SPY** CALL 800 2026-11-10 (6DTE): 1,190 traded vs OI 1,145
- **SPY** PUT 757 2026-11-10 (6DTE): 508 traded vs OI 0
- **QQQ** PUT 686 2026-11-11 (7DTE): 563 traded vs OI 0
- **QQQ** CALL 695 2026-11-18 (14DTE): 502 traded vs OI 0
- **AAPL** PUT 322.5 2026-11-06 (2DTE): 1,288 traded vs OI 1,190
- **AAPL** CALL 372.5 2026-11-11 (7DTE): 622 traded vs OI 10
- **AAPL** CALL 365 2026-11-11 (7DTE): 693 traded vs OI 114
- **META** PUT 605 2026-11-04 (0DTE): 829 traded vs OI 742
- **MSFT** CALL 585 2026-11-06 (2DTE): 560 traded vs OI 434
- **DELL** CALL 375 2026-11-06 (2DTE): 501 traded vs OI 46
- **DELL** PUT 372.5 2026-11-06 (2DTE): 503 traded vs OI 304

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
