# GEX + FLOW SCAN - Wed Nov 04, 12:10 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (8)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:38 | **QQQ** | **PUTS** | 1m FAILED POP (R3) | 11/04 686P | 0.80 | 0.24 | -1% (0m) | **-70%** | +26% | 689.6 |
| 11:21 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/04 685P | 0.67 | 0.23 | +66% (7m) | **-66%** | +25% | 690.3 hit |
| 10:20 | **SMCI** | **CALLS** | FLOW SURGE | 11/06 33C | 0.65 | 0.13 | -3% (1m) | **-80%** (done) | +39% | 32.81 |
| 10:20 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/04 284C | 0.49 | 0.17 | +2% (22m) | **-65%** (done) | +131% | 284.74 |
| 10:00 | **AMZN** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/04 267.5P | 0.68 | 1.54 | +169% (60m) | **+126%** (done) | +258% | 265.7 |
| 09:50 | **UBER** | **CALLS** | FLIP CROSS up into positive gamma | 11/06 71C | 0.60 | 1.56 | +168% (52m) | **+160%** (done) | +50% | 70 hit |
| 09:50 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/04 286C | 0.53 | 0.06 | +2% (1m) | **-89%** (done) | +150% | 287 |
| 09:45 | **UBER** | **PUTS** | FLIP CROSS down into negative gamma | 11/06 67P | 0.63 | 0.10 | -3% (1m) | **-84%** (done) | +27% | 68.03 |

## 1m RULES on SPY / QQQ - loose (2 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 12:10:08 ET, last candle SPY 12:09, QQQ 12:09 | no errors
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
| 1 | **AAPL** | 353.46 | FLOW SURGE | **PUTS** | 40 | none: 108 puts 0-7DTE > 9 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (62 contracts' greeks worked out here) | POS +$1.1B | 341.82 | 355 | 350 | -$82.7M | +$0 bull / -$420k bear | out (clean 32, ADX 51, RVol 0.9) |
| 2 | **SMH** | 506.71 | - | **-** | 31 | - | NEG -$536.4M | - | 532.5 | 500 | +$16.1M | +$348k bull / -$12.5M bear | out (clean 32, ADX 28, RVol 1.7) |
| 3 | **MSFT** | 556.27 | - | **-** | 27 | - | POS +$999.7M | - | 550 | 535 | -$19.4M | +$474k bull / -$1.4M bear | out (clean 29, ADX 63, RVol 1.6) |
| 4 | **GOOGL** | 291.32 | - | **-** | 26 | - | POS +$95.4M | 284.57 | 290 | 290 | -$27.0M | +$137k bull / +$0 bear | out (clean 36, ADX 29, RVol 0.5) |
| 5 | **MU** | 806.50 | - | **-** | 24 | - | NEG -$351.3M | - | 850 | 800 | +$100.0M | +$3.4M bull / -$909k bear | out (clean 32, ADX 31, RVol 1.1) |
| 6 | **AMZN** | 267.43 | - | **-** | 23 | - | POS +$555.9M | - | 270 | 250 | -$17.7M | +$343k bull / -$126k bear | out (clean 35, ADX 37, RVol 0.8) |
| 7 | **SMCI** | 30.04 | - | **-** | 23 | - | NEG -$558k | - | 33 | 30 | +$1.9M | - | out (clean 34, ADX 45, RVol 1.3) |
| 8 | **TSLA** | 385.94 | - | **-** | 22 | - | NEG -$126.9M | 396.53 | 400 | 380 | -$66.5M | +$145k bull / -$450k bear | out (clean 30, ADX 20, RVol 1.1) |
| 9 | **DELL** | 373.06 | - | **-** | 21 | - | NEG -$29.9M | - | 400 | 400 | +$1.7M | +$0 bull / -$83k bear | out (clean 33, ADX 33, RVol 0.8) |
| 10 | **ORCL** | 125.87 | - | **-** | 21 | - | NEG -$31.1M | - | 130 | 125 | +$2.3M | +$82k bull / +$0 bear | out (clean 35, ADX 13, RVol 1.9) |
| 11 | **UBER** | 71.70 | - | **-** | 21 | - | POS +$13.1M | 68.13 | 70 | 70 | -$1.4M | - | out (clean 30, ADX 47, RVol 1.0) |
| 12 | **SPY** | 767.86 | - | **-** | 20 | - | NEG -$2.5B | 770.1 | 770 | 750 | -$97.8M | +$235k bull / -$1.1M bear | out (clean 32, ADX 27, RVol 1.2) |
| 13 | **IWM** | 283.71 | - | **-** | 20 | - | NEG -$323.1M | 284.65 | 285 | 270 | +$10.8M | +$50k bull / +$0 bear | out (clean 34, ADX 18, RVol 1.3) |
| 14 | **AMD** | 486.69 | - | **-** | 20 | - | NEG -$89.7M | - | 500 | 500 | +$40.3M | +$463k bull / -$452k bear | out (clean 32, ADX 14, RVol 1.1) |
| 15 | **CRM** | 226.10 | - | **-** | 20 | - | NEG -$13.5M | - | 240 | 220 | -$112k | +$36k bull / +$0 bear | out (clean 33, ADX 34, RVol 0.5) |
| 16 | **AVGO** | 327.50 | - | **-** | 19 | - | NEG -$93.5M | - | 340 | 330 | +$1.8M | +$30k bull / -$68k bear | out (clean 31, ADX 25, RVol 1.2) |
| 17 | **BABA** | 107.02 | - | **-** | 19 | - | POS +$16.5M | - | 110 | 110 | -$847k | - | out (clean 36, ADX 46, RVol 1.6) |
| 18 | **NVDA** | 203.36 | - | **-** | 18 | - | NEG -$47.1M | 204.01 | 210 | 200 | +$85k | +$135k bull / -$320k bear | out (clean 30, ADX 31, RVol 1.1) |
| 19 | **MSTR** | 143.91 | - | **-** | 18 | - | POS +$127.1M | - | 135 | 150 | +$201k | +$35k bull / -$64k bear | out (clean 31, ADX 37, RVol 0.7) |
| 20 | **QQQ** | 695.06 | - | **-** | 17 | - | NEG -$4.6B | 721.37 | 700 | 680 | -$121.4M | +$1.4M bull / -$2.4M bear | out (clean 31, ADX 16, RVol 0.7) |
| 21 | **NFLX** | 66.10 | - | **-** | 17 | - | POS +$20.3M | 62.31 | 65 | 65 | -$2.1M | - | out (clean 31, ADX 55, RVol 0.7) |
| 22 | **PLTR** | 171.30 | - | **-** | 17 | - | NEG -$49.7M | - | 165 | 170 | -$1.9M | +$47k bull / +$0 bear | out (clean 26, ADX 22, RVol 0.6) |
| 23 | **META** | 637.71 | - | **-** | 16 | - | POS +$208.5M | 623.85 | 650 | 625 | +$1.8M | +$0 bull / -$333k bear | out (clean 29, ADX 24, RVol 0.6) |
| 24 | **HOOD** | 87.43 | - | **-** | 16 | - | POS +$2.4M | 84.95 | 90 | 90 | -$978k | +$162k bull / +$0 bear | out (clean 28, ADX 16, RVol 0.8) |
| 25 | **SHOP** | 152.16 | - | **-** | 14 | - | NEG -$5.3M | - | 160 | 150 | -$362k | - | out (clean 34, ADX 30, RVol 0.4) |
| 26 | **COIN** | 151.55 | - | **-** | 13 | - | POS +$30.8M | - | 148 | 150 | -$1.3M | - | out (clean 31, ADX 18, RVol 0.8) |
| 27 | **ARM** | 194.80 | - | **-** | 8 | - | NEG -$7.0M | - | 212.5 | 200 | +$119k | - | out (clean 26, ADX 31, RVol 0.9) |

## Big prints this scan (94)
- **MU** CALL 810 2026-11-06 (2DTE): 300 @ 20.50 = **+$615k** BUY | vol 2,445 / OI 59
- **QQQ** PUT 695 2026-11-05 (1DTE): 600 @ 4.80 = **+$288k** BUY | vol 13,616 / OI 1,805
- **MU** CALL 810 2026-11-06 (2DTE): 90 @ 20.85 = **+$188k** BUY | vol 2,445 / OI 59
- **MU** CALL 810 2026-11-06 (2DTE): 84 @ 20.85 = **+$175k** BUY | vol 2,445 / OI 59
- **QQQ** PUT 695 2026-11-04 (0DTE): 953 @ 1.80 = **+$172k** SELL | vol 98,822 / OI 1,605
- **QQQ** PUT 705 2026-11-10 (6DTE): 111 @ 13.68 = **+$152k** SELL | vol 140 / OI 160
- **MU** CALL 810 2026-11-06 (2DTE): 72 @ 20.85 = **+$150k** BUY | vol 2,445 / OI 59
- **HOOD** CALL 87 2026-11-06 (2DTE): 500 @ 2.73 = **+$136k** BUY | vol 6,460 / OI 1,164
- **QQQ** CALL 700 2026-11-04 (0DTE): 1,645 @ 0.80 = **+$132k** BUY | vol 255,672 / OI 4,258
- **QQQ** CALL 700 2026-11-05 (1DTE): 475 @ 2.74 = **+$130k** BUY | vol 39,034 / OI 2,909
- **SPY** PUT 768 2026-11-04 (0DTE): 924 @ 1.39 = **+$128k** SELL | vol 86,986 / OI 1,133
- **AMZN** CALL 275 2026-11-09 (5DTE): 693 @ 1.72 = **+$119k** BUY | vol 3,665 / OI 229
- **AMD** CALL 495 2026-11-06 (2DTE): 101 @ 11.25 = **+$114k** BUY | vol 1,454 / OI 244
- **META** CALL 620 2026-11-06 (2DTE): 40 @ 20.62 = **+$82k** SELL | vol 659 / OI 1,764
- **MSFT** PUT 555 2026-11-04 (0DTE): 499 @ 1.50 = **+$75k** SELL | vol 5,940 / OI 0

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 712 2026-11-05 (1DTE): 1,112 traded vs OI 0
- **SPY** PUT 772 2026-11-05 (1DTE): 501 traded vs OI 0
- **SPY** PUT 750 2026-11-09 (5DTE): 2,660 traded vs OI 2,653
- **SPY** PUT 760 2026-11-16 (12DTE): 559 traded vs OI 339
- **SPY** CALL 790 2026-11-27 (23DTE): 844 traded vs OI 830
- **SPY** PUT 724 2026-11-17 (13DTE): 506 traded vs OI 0
- **SPY** PUT 768 2026-11-27 (23DTE): 523 traded vs OI 441
- **QQQ** PUT 658 2026-11-04 (0DTE): 530 traded vs OI 0
- **QQQ** PUT 657 2026-11-04 (0DTE): 508 traded vs OI 0
- **QQQ** CALL 694 2026-11-11 (7DTE): 545 traded vs OI 0
- **QQQ** CALL 695 2026-12-04 (30DTE): 531 traded vs OI 501
- **QQQ** CALL 729 2026-11-27 (23DTE): 562 traded vs OI 126
- **IWM** CALL 295 2026-11-13 (9DTE): 1,403 traded vs OI 1,277
- **IWM** PUT 282 2026-11-09 (5DTE): 541 traded vs OI 280
- **SMH** CALL 540 2026-11-06 (2DTE): 2,044 traded vs OI 2,043

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
