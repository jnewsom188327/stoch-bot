# GEX + FLOW SCAN - Wed Nov 04, 12:20 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (8)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:38 | **QQQ** | **PUTS** | 1m FAILED POP (R3) | 11/04 686P | 0.80 | 0.19 | -1% (0m) | **-76%** | +26% | 689.6 |
| 11:21 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/04 685P | 0.67 | 0.19 | +66% (7m) | **-72%** | +25% | 690.3 hit |
| 10:20 | **SMCI** | **CALLS** | FLOW SURGE | 11/06 33C | 0.65 | 0.13 | -3% (1m) | **-80%** (done) | +39% | 32.81 |
| 10:20 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/04 284C | 0.49 | 0.17 | +2% (22m) | **-65%** (done) | +131% | 284.74 |
| 10:00 | **AMZN** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/04 267.5P | 0.68 | 1.54 | +169% (60m) | **+126%** (done) | +258% | 265.7 |
| 09:50 | **UBER** | **CALLS** | FLIP CROSS up into positive gamma | 11/06 71C | 0.60 | 1.56 | +168% (52m) | **+160%** (done) | +50% | 70 hit |
| 09:50 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/04 286C | 0.53 | 0.06 | +2% (1m) | **-89%** (done) | +150% | 287 |
| 09:45 | **UBER** | **PUTS** | FLIP CROSS down into negative gamma | 11/06 67P | 0.63 | 0.10 | -3% (1m) | **-84%** (done) | +27% | 68.03 |

## 1m RULES on SPY / QQQ - loose (2 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 12:20:08 ET, last candle SPY 12:19, QQQ 12:19 | no errors
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
| 1 | **SMH** | 505.31 | FLOW SURGE | **CALLS** | 42 | none: 160 calls 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (66 contracts' greeks worked out here) | NEG -$528.1M | - | 532.5 | 500 | +$20.8M | +$5.4M bull / -$27k bear | out (clean 32, ADX 26, RVol 1.0) |
| 2 | **AAPL** | 353.78 | FLOW SURGE | **PUTS** | 41 | none: 108 puts 0-7DTE > 9 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (48 contracts' greeks worked out here) | POS +$1.1B | 342.3 | 355 | 350 | -$84.5M | +$0 bull / -$499k bear | out (clean 32, ADX 51, RVol 1.0) |
| 3 | **MSFT** | 556.17 | - | **-** | 26 | - | POS +$982.2M | - | 550 | 535 | -$18.5M | +$1.3M bull / +$0 bear | out (clean 29, ADX 61, RVol 1.5) |
| 4 | **GOOGL** | 291.67 | - | **-** | 25 | - | POS +$98.3M | 283.42 | 290 | 290 | -$27.0M | +$152k bull / -$40k bear | out (clean 36, ADX 26, RVol 0.5) |
| 5 | **MU** | 804.78 | - | **-** | 24 | - | NEG -$337.6M | - | 850 | 800 | +$100.3M | +$4.1M bull / -$73k bear | out (clean 31, ADX 31, RVol 0.9) |
| 6 | **SMCI** | 29.90 | - | **-** | 23 | - | NEG -$934k | - | 32 | 30 | +$1.9M | - | out (clean 34, ADX 45, RVol 1.3) |
| 7 | **AMZN** | 267.88 | - | **-** | 22 | - | POS +$552.6M | - | 270 | 250 | -$17.8M | +$311k bull / -$36k bear | out (clean 35, ADX 34, RVol 0.6) |
| 8 | **TSLA** | 386.01 | - | **-** | 21 | - | NEG -$75.8M | 389.91 | 400 | 380 | -$69.9M | +$0 bull / -$608k bear | out (clean 30, ADX 18, RVol 0.8) |
| 9 | **SPY** | 767.48 | - | **-** | 20 | - | NEG -$2.6B | 769.97 | 770 | 767 | -$101.6M | +$475k bull / +$0 bear | out (clean 32, ADX 26, RVol 1.2) |
| 10 | **AMD** | 484.81 | - | **-** | 20 | - | NEG -$80.4M | - | 500 | 440 | +$42.9M | +$3.9M bull / -$28k bear | out (clean 32, ADX 13, RVol 0.8) |
| 11 | **DELL** | 371.26 | - | **-** | 20 | - | NEG -$28.2M | - | 400 | 400 | +$1.5M | +$0 bull / -$83k bear | out (clean 33, ADX 32, RVol 0.8) |
| 12 | **ORCL** | 125.80 | - | **-** | 20 | - | NEG -$30.8M | - | 130 | 125 | +$2.4M | +$82k bull / +$0 bear | out (clean 35, ADX 13, RVol 1.6) |
| 13 | **ARM** | 194.88 | - | **-** | 20 | - | NEG -$6.6M | - | 212.5 | 200 | +$364k | +$229k bull / +$0 bear | out (clean 26, ADX 30, RVol 0.6) |
| 14 | **UBER** | 71.56 | - | **-** | 20 | - | POS +$12.2M | 68.2 | 70 | 70 | -$1.3M | - | out (clean 30, ADX 42, RVol 1.0) |
| 15 | **CRM** | 225.19 | - | **-** | 20 | - | NEG -$13.0M | - | 240 | 220 | -$95k | +$36k bull / +$0 bear | out (clean 33, ADX 35, RVol 0.6) |
| 16 | **IWM** | 283.54 | - | **-** | 19 | - | NEG -$264.8M | 284.65 | 285 | 270 | +$9.9M | +$0 bull / -$349k bear | out (clean 34, ADX 17, RVol 1.2) |
| 17 | **AVGO** | 326.48 | - | **-** | 18 | - | NEG -$95.6M | 345.42 | 340 | 320 | +$1.6M | +$30k bull / +$0 bear | out (clean 31, ADX 24, RVol 1.2) |
| 18 | **MSTR** | 143.93 | - | **-** | 18 | - | POS +$119.6M | - | 135 | 150 | +$406k | +$130k bull / +$0 bear | out (clean 31, ADX 34, RVol 0.6) |
| 19 | **QQQ** | 694.66 | - | **-** | 17 | - | NEG -$4.6B | 718.83 | 700 | 680 | -$130.9M | +$2.0M bull / -$850k bear | out (clean 31, ADX 14, RVol 0.7) |
| 20 | **NVDA** | 202.70 | - | **-** | 17 | - | NEG -$39.8M | 203.34 | 210 | 200 | +$227k | +$558k bull / +$0 bear | out (clean 30, ADX 30, RVol 0.9) |
| 21 | **NFLX** | 66.09 | - | **-** | 17 | - | POS +$20.4M | 62.49 | 65 | 65 | -$2.0M | - | out (clean 31, ADX 50, RVol 0.7) |
| 22 | **PLTR** | 170.00 | - | **-** | 17 | - | NEG -$49.5M | - | 165 | 170 | -$1.7M | +$137k bull / +$0 bear | out (clean 26, ADX 23, RVol 0.6) |
| 23 | **BABA** | 107.01 | - | **-** | 17 | - | POS +$16.5M | - | 110 | 110 | -$831k | - | out (clean 36, ADX 42, RVol 1.2) |
| 24 | **META** | 637.75 | - | **-** | 16 | - | POS +$234.2M | 620.43 | 650 | 625 | -$167k | +$0 bull / -$299k bear | out (clean 30, ADX 23, RVol 0.8) |
| 25 | **HOOD** | 87.45 | - | **-** | 16 | - | POS +$2.3M | 85.22 | 90 | 90 | -$1.0M | +$162k bull / +$0 bear | out (clean 28, ADX 15, RVol 0.8) |
| 26 | **SHOP** | 152.13 | - | **-** | 14 | - | NEG -$4.9M | - | 160 | 150 | -$359k | - | out (clean 34, ADX 28, RVol 0.4) |
| 27 | **COIN** | 150.56 | - | **-** | 11 | - | POS +$29.9M | - | 148 | 150 | -$1.2M | - | out (clean 31, ADX 16, RVol 0.3) |

## Big prints this scan (56)
- **AMD** PUT 475 2026-11-06 (2DTE): 500 @ 7.50 = **+$375k** SELL | vol 3,224 / OI 892
- **MU** PUT 805 2026-11-04 (0DTE): 599 @ 5.00 = **+$300k** SELL | vol 17,343 / OI 922
- **QQQ** PUT 695 2026-11-05 (1DTE): 600 @ 4.90 = **+$294k** BUY | vol 15,720 / OI 1,805
- **AMD** CALL 490 2026-11-06 (2DTE): 150 @ 14.30 = **+$214k** BUY | vol 3,042 / OI 355
- **IWM** PUT 285 2026-11-04 (0DTE): 1,203 @ 1.72 = **+$207k** BUY | vol 19,051 / OI 131
- **QQQ** CALL 697 2026-11-04 (0DTE): 1,331 @ 1.33 = **+$177k** BUY | vol 130,986 / OI 930
- **MSFT** PUT 552.5 2026-11-04 (0DTE): 1,997 @ 0.75 = **+$150k** SELL | vol 14,023 / OI 0
- **QQQ** PUT 695 2026-11-05 (1DTE): 298 @ 4.88 = **+$145k** BUY | vol 15,720 / OI 1,805
- **QQQ** CALL 696 2026-11-04 (0DTE): 814 @ 1.50 = **+$122k** SELL | vol 112,502 / OI 1,408
- **TSLA** CALL 390 2026-11-11 (7DTE): 150 @ 7.75 = **+$116k** SELL | vol 2,887 / OI 87
- **QQQ** CALL 700 2026-11-09 (5DTE): 200 @ 5.58 = **+$112k** BUY | vol 2,985 / OI 977
- **MU** PUT 835 2026-11-06 (2DTE): 30 @ 36.72 = **+$110k** MID | vol 658 / OI 795
- **MU** PUT 835 2026-11-06 (2DTE): 25 @ 36.65 = **+$92k** MID | vol 658 / OI 795
- **IWM** PUT 284 2026-11-04 (0DTE): 829 @ 0.97 = **+$80k** BUY | vol 32,945 / OI 236
- **MSFT** PUT 552.5 2026-11-04 (0DTE): 1,000 @ 0.75 = **+$75k** SELL | vol 14,023 / OI 0

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 780 2026-11-06 (2DTE): 16,485 traded vs OI 16,348
- **SPY** CALL 765 2026-11-10 (6DTE): 1,542 traded vs OI 1,539
- **SPY** CALL 782 2026-11-11 (7DTE): 500 traded vs OI 0
- **QQQ** PUT 654 2026-11-05 (1DTE): 507 traded vs OI 0
- **QQQ** PUT 696 2026-11-09 (5DTE): 541 traded vs OI 0
- **QQQ** PUT 630 2026-11-05 (1DTE): 503 traded vs OI 385
- **QQQ** PUT 689 2026-11-06 (2DTE): 1,290 traded vs OI 1,281
- **QQQ** PUT 695 2026-11-09 (5DTE): 780 traded vs OI 751
- **IWM** CALL 284 2026-11-09 (5DTE): 510 traded vs OI 381
- **IWM** CALL 289 2026-11-06 (2DTE): 10,844 traded vs OI 9,920
- **IWM** CALL 290 2026-11-18 (14DTE): 500 traded vs OI 0
- **SMH** CALL 512.5 2026-11-04 (0DTE): 971 traded vs OI 20
- **NVDA** CALL 197.5 2026-11-04 (0DTE): 534 traded vs OI 107
- **NVDA** CALL 197.5 2026-11-06 (2DTE): 500 traded vs OI 144
- **NVDA** CALL 222.5 2026-11-09 (5DTE): 500 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
