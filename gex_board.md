# GEX + FLOW SCAN - Wed Nov 04, 03:25 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (10)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 13:05 | **AAPL** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/04 352.5P | 0.58 | 0.89 | +76% (29m) | **+53%** (done) | +57% | 352.38 hit |
| 12:50 | **AMZN** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/04 267.5P | 0.40 | 0.76 | +100% (55m) | **+90%** (done) | +109% | 267.48 |
| 11:38 | **QQQ** | **PUTS** | 1m FAILED POP (R3) | 11/04 686P | 0.80 | 0.15 | -1% (0m) | **-81%** (done) | +26% | 689.6 |
| 11:21 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/04 685P | 0.67 | 0.12 | +66% (7m) | **-82%** (done) | +25% | 690.3 hit |
| 10:20 | **SMCI** | **CALLS** | FLOW SURGE | 11/06 33C | 0.65 | 0.13 | -3% (1m) | **-80%** (done) | +39% | 32.81 |
| 10:20 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/04 284C | 0.49 | 0.17 | +2% (22m) | **-65%** (done) | +131% | 284.74 |
| 10:00 | **AMZN** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/04 267.5P | 0.68 | 1.54 | +169% (60m) | **+126%** (done) | +258% | 265.7 |
| 09:50 | **UBER** | **CALLS** | FLIP CROSS up into positive gamma | 11/06 71C | 0.60 | 1.56 | +168% (52m) | **+160%** (done) | +50% | 70 hit |
| 09:50 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/04 286C | 0.53 | 0.06 | +2% (1m) | **-89%** (done) | +150% | 287 |
| 09:45 | **UBER** | **PUTS** | FLIP CROSS down into negative gamma | 11/06 67P | 0.63 | 0.10 | -3% (1m) | **-84%** (done) | +27% | 68.03 |

## 1m RULES on SPY / QQQ - loose (3 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 15:25:08 ET, last candle SPY 15:24, QQQ 15:24 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 14:01 | QQQ | 1m WHIPSAW | R1 | PUTS | TURNING away | no contract: 82 puts 0-1DTE > 8 priced 0.40-0.80 > 2 delta 0.15+ > 2 spread ok > 2 liquid  |
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
| 1 | **SMH** | 502.08 | - | **-** | 26 | - | NEG -$594.8M | - | 532.5 | 500 | +$22.4M | +$25k bull / -$1.1M bear | out (clean 33, ADX 21, RVol 0.6) |
| 2 | **MU** | 794.37 | - | **-** | 24 | - | NEG -$393.6M | - | 850 | 800 | +$127.0M | +$2.5M bull / +$0 bear | out (clean 31, ADX 29, RVol 1.4) |
| 3 | **AAPL** | 352.62 | - | **-** | 23 | - | POS +$908.0M | 342.48 | 355 | 350 | -$77.3M | +$52k bull / -$1.2M bear | out (clean 32, ADX 14, RVol 0.9) |
| 4 | **MSTR** | 143.48 | - | **-** | 21 | - | POS +$137.2M | - | 135 | 150 | -$9.2M | +$76k bull / -$38k bear | out (clean 32, ADX 26, RVol 0.5) |
| 5 | **MSFT** | 558.82 | - | **-** | 20 | - | POS +$1.0B | - | 550 | 535 | -$17.7M | +$88k bull / -$923k bear | out (clean 29, ADX 22, RVol 1.2) |
| 6 | **TSLA** | 386.20 | - | **-** | 19 | - | NEG -$39.1M | 387.53 | 400 | 380 | -$68.0M | +$1.2M bull / +$0 bear | out (clean 31, ADX 20, RVol 0.8) |
| 7 | **AMD** | 482.88 | - | **-** | 19 | - | NEG -$88.4M | - | 500 | 440 | +$48.7M | +$96k bull / -$444k bear | out (clean 31, ADX 13, RVol 0.5) |
| 8 | **AVGO** | 325.29 | - | **-** | 19 | - | NEG -$108.7M | 342.49 | 340 | 320 | +$5.8M | +$85k bull / +$0 bear | out (clean 29, ADX 24, RVol 0.6) |
| 9 | **NVDA** | 202.09 | - | **-** | 18 | - | NEG -$113.5M | 203.43 | 210 | 200 | +$10.7M | +$575k bull / -$72k bear | out (clean 30, ADX 23, RVol 1.1) |
| 10 | **SMCI** | 29.59 | - | **-** | 18 | - | NEG -$1.8M | - | 32 | 30 | +$2.1M | - | out (clean 34, ADX 28, RVol 0.8) |
| 11 | **META** | 630.57 | - | **-** | 17 | - | POS +$188.3M | 620.72 | 650 | 625 | +$10.2M | +$0 bull / -$336k bear | out (clean 32, ADX 23, RVol 0.7) |
| 12 | **AMZN** | 268.19 | - | **-** | 17 | - | POS +$551.5M | - | 270 | 250 | -$17.3M | +$45k bull / -$75k bear | out (clean 35, ADX 13, RVol 0.6) |
| 13 | **SPY** | 767.69 | - | **-** | 16 | - | NEG -$3.5B | 769.48 | 770 | 767 | -$90.9M | +$665k bull / +$0 bear | out (clean 32, ADX 14, RVol 0.8) |
| 14 | **IWM** | 283.44 | - | **-** | 16 | - | NEG -$285.0M | 284.1 | 285 | 270 | +$8.9M | +$0 bull / -$699k bear | out (clean 35, ADX 14, RVol 0.5) |
| 15 | **QQQ** | 692.64 | - | **-** | 15 | - | NEG -$5.2B | 715.84 | 700 | 680 | -$83.7M | +$1.8M bull / -$439k bear | out (clean 32, ADX 17, RVol 0.5) |
| 16 | **ORCL** | 124.36 | - | **-** | 15 | - | NEG -$35.4M | - | 130 | 125 | +$3.8M | - | out (clean 33, ADX 28, RVol 2.0) |
| 17 | **PLTR** | 172.14 | - | **-** | 14 | - | NEG -$47.5M | - | 165 | 170 | -$1.3M | +$0 bull / -$721k bear | out (clean 26, ADX 12, RVol 0.4) |
| 18 | **HOOD** | 87.49 | - | **-** | 14 | - | POS +$9.9M | 82.59 | 90 | 90 | -$694k | +$0 bull / -$31k bear | out (clean 29, ADX 14, RVol 0.3) |
| 19 | **NFLX** | 66.54 | - | **-** | 13 | - | POS +$20.3M | 62.56 | 65 | 65 | -$2.0M | - | out (clean 32, ADX 32, RVol 1.0) |
| 20 | **SHOP** | 153.14 | - | **-** | 13 | - | NEG -$3.9M | 158.42 | 160 | 150 | -$411k | - | out (clean 33, ADX 25, RVol 0.6) |
| 21 | **GOOGL** | 290.87 | - | **-** | 11 | - | POS +$103.1M | 284.21 | 290 | 290 | -$25.8M | - | out (clean 36, ADX 11, RVol 0.4) |
| 22 | **ARM** | 191.95 | - | **-** | 11 | - | NEG -$8.6M | - | 200 | 200 | +$1.0M | - | out (clean 26, ADX 28, RVol 0.7) |
| 23 | **UBER** | 70.50 | - | **-** | 11 | - | POS +$10.2M | 68.46 | 70 | 65 | -$669k | - | out (clean 32, ADX 27, RVol 1.1) |
| 24 | **COIN** | 152.19 | - | **-** | 9 | - | POS +$30.9M | - | 148 | 150 | -$1.2M | - | out (clean 31, ADX 10, RVol 0.4) |
| 25 | **CRM** | 227.94 | - | **-** | 8 | - | NEG -$10.7M | 237.88 | 240 | 220 | -$196k | - | out (clean 34, ADX 20, RVol 0.5) |
| 26 | **DELL** | 368.62 | - | **-** | 7 | - | NEG -$29.2M | - | 400 | 400 | +$678k | - | out (clean 33, ADX 24, RVol 0.9) |
| 27 | **BABA** | 105.86 | - | **-** | 7 | - | POS +$17.1M | - | 105 | 110 | -$177k | - | out (clean 37, ADX 26, RVol 0.6) |

## Big prints this scan (52)
- **QQQ** PUT 710 2026-11-05 (1DTE): 250 @ 17.34 = **+$434k** SELL | vol 422 / OI 623
- **QQQ** PUT 710 2026-11-04 (0DTE): 250 @ 17.33 = **+$433k** SELL | vol 820 / OI 1,541
- **MU** PUT 770 2026-11-06 (2DTE): 510 @ 8.35 = **+$426k** SELL | vol 2,668 / OI 1,462
- **MU** CALL 790 2026-11-06 (2DTE): 43 @ 23.98 = **+$103k** BUY | vol 735 / OI 15
- **MU** PUT 800 2026-11-06 (2DTE): 40 @ 19.45 = **+$78k** SELL | vol 12,292 / OI 3,802
- **MU** PUT 800 2026-11-06 (2DTE): 40 @ 19.45 = **+$78k** SELL | vol 12,292 / OI 3,802
- **MSFT** CALL 565 2026-11-06 (2DTE): 250 @ 3.10 = **+$78k** SELL | vol 4,617 / OI 2,065
- **MSTR** CALL 143 2026-11-06 (2DTE): 190 @ 4.00 = **+$76k** BUY | vol 2,505 / OI 7,853
- **MSFT** CALL 560 2026-11-06 (2DTE): 152 @ 4.95 = **+$75k** SELL | vol 11,112 / OI 5,047
- **MU** CALL 800 2026-11-09 (5DTE): 31 @ 22.33 = **+$69k** BUY | vol 538 / OI 17
- **PLTR** PUT 175 2026-11-06 (2DTE): 118 @ 5.40 = **+$64k** BUY | vol 6,097 / OI 4,401
- **PLTR** PUT 175 2026-11-06 (2DTE): 117 @ 5.40 = **+$63k** BUY | vol 6,097 / OI 4,401
- **AMD** CALL 485 2026-11-06 (2DTE): 50 @ 12.55 = **+$63k** SELL | vol 2,895 / OI 241
- **AAPL** PUT 350 2026-11-06 (2DTE): 250 @ 2.47 = **+$62k** BUY | vol 31,248 / OI 2,166
- **MSFT** CALL 567.5 2026-11-06 (2DTE): 250 @ 2.39 = **+$60k** SELL | vol 2,406 / OI 638

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 737 2026-11-06 (2DTE): 2,131 traded vs OI 1,793
- **SPY** PUT 753 2026-11-10 (6DTE): 512 traded vs OI 0
- **QQQ** PUT 651 2026-11-09 (5DTE): 518 traded vs OI 0
- **NVDA** CALL 220 2026-11-11 (7DTE): 1,788 traded vs OI 1,757
- **TSLA** PUT 380 2026-11-27 (23DTE): 764 traded vs OI 763
- **AAPL** PUT 325 2026-11-13 (9DTE): 2,352 traded vs OI 2,220
- **AMD** PUT 480 2026-11-13 (9DTE): 521 traded vs OI 351
- **META** CALL 670 2026-11-13 (9DTE): 500 traded vs OI 404
- **META** PUT 597.5 2026-11-06 (2DTE): 1,069 traded vs OI 1,040
- **GOOGL** CALL 300 2026-11-27 (23DTE): 1,524 traded vs OI 1,517
- **GOOGL** PUT 275 2026-11-04 (0DTE): 707 traded vs OI 706
- **GOOGL** PUT 285 2026-11-11 (7DTE): 507 traded vs OI 71
- **COIN** PUT 140 2026-11-06 (2DTE): 1,164 traded vs OI 948
- **DELL** CALL 385 2026-11-06 (2DTE): 503 traded vs OI 71
- **MU** PUT 795 2026-11-09 (5DTE): 564 traded vs OI 66

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
