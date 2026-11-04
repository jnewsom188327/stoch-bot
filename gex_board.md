# GEX + FLOW SCAN - Wed Nov 04, 02:20 PM ET
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
Last 1m check 14:20:08 ET, last candle SPY 14:19, QQQ 14:19 | no errors
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
| 1 | **SMCI** | 29.91 | TREND (flow not with it) | **PUTS** | 37 | none: 12 puts 0-7DTE > 3 priced 0.40-0.80 > 3 delta 0.2+ > 3 spread ok > 3 liquid > best one only +16% at the target (needs +20%) | NEG -$963k | - | 32 | 30 | +$2.0M | - | SHORT (clean 34, ADX 24, RVol 1.3) |
| 2 | **SMH** | 505.05 | - | **-** | 25 | - | NEG -$574.7M | - | 532.5 | 500 | +$22.1M | +$0 bull / -$250k bear | out (clean 33, ADX 15, RVol 0.5) |
| 3 | **AAPL** | 353.23 | - | **-** | 24 | - | POS +$1.1B | 342.02 | 355 | 350 | -$78.0M | +$325k bull / -$367k bear | out (clean 32, ADX 20, RVol 0.6) |
| 4 | **GOOGL** | 291.69 | - | **-** | 22 | - | POS +$94.1M | 285.25 | 290 | 290 | -$26.5M | +$0 bull / -$32k bear | out (clean 36, ADX 14, RVol 0.2) |
| 5 | **MSTR** | 145.35 | - | **-** | 21 | - | POS +$125.2M | - | 135 | 150 | -$9.8M | +$0 bull / -$52k bear | out (clean 31, ADX 25, RVol 0.5) |
| 6 | **TSLA** | 390.70 | - | **-** | 20 | - | NEG -$74.6M | 395.58 | 400 | 390 | -$86.1M | +$0 bull / -$1.8M bear | out (clean 31, ADX 18, RVol 0.4) |
| 7 | **MU** | 805.59 | - | **-** | 20 | - | NEG -$394.6M | - | 850 | 800 | +$110.2M | +$208k bull / -$2.5M bear | out (clean 32, ADX 16, RVol 0.7) |
| 8 | **AMD** | 483.05 | - | **-** | 19 | - | NEG -$98.1M | - | 500 | 500 | +$49.8M | +$0 bull / -$2.5M bear | out (clean 32, ADX 13, RVol 0.3) |
| 9 | **META** | 628.40 | - | **-** | 19 | - | POS +$133.3M | 621.43 | 650 | 625 | +$10.7M | +$195k bull / -$170k bear | out (clean 32, ADX 28, RVol 1.0) |
| 10 | **AMZN** | 268.77 | - | **-** | 19 | - | POS +$553.2M | - | 270 | 250 | -$18.6M | +$0 bull / -$39k bear | out (clean 36, ADX 24, RVol 0.6) |
| 11 | **MSFT** | 555.13 | - | **-** | 19 | - | POS +$1.0B | - | 550 | 535 | -$16.9M | +$26k bull / -$326k bear | out (clean 29, ADX 21, RVol 0.8) |
| 12 | **AVGO** | 327.15 | - | **-** | 17 | - | NEG -$100.7M | 343.69 | 340 | 330 | +$4.9M | +$26k bull / -$1.5M bear | out (clean 30, ADX 16, RVol 0.6) |
| 13 | **SPY** | 768.32 | - | **-** | 16 | - | NEG -$2.3B | 769.7 | 770 | 767 | -$98.8M | +$0 bull / -$2.0M bear | out (clean 32, ADX 18, RVol 0.4) |
| 14 | **IWM** | 284.06 | - | **-** | 16 | - | NEG -$116.1M | 284.34 | 285 | 270 | +$8.8M | +$0 bull / -$821k bear | out (clean 34, ADX 10, RVol 0.6) |
| 15 | **QQQ** | 694.28 | - | **-** | 15 | - | NEG -$4.8B | 718.67 | 700 | 680 | -$115.1M | +$0 bull / -$1.9M bear | out (clean 33, ADX 12, RVol 0.5) |
| 16 | **HOOD** | 87.89 | - | **-** | 15 | - | POS +$2.8M | 84.75 | 90 | 90 | -$798k | +$29k bull / -$86k bear | out (clean 29, ADX 16, RVol 0.3) |
| 17 | **NVDA** | 203.95 | - | **-** | 14 | - | NEG -$17.1M | 204.15 | 210 | 200 | +$2.3M | +$0 bull / -$1.2M bear | out (clean 30, ADX 13, RVol 0.6) |
| 18 | **ARM** | 191.41 | - | **-** | 12 | - | NEG -$7.4M | - | 200 | 200 | +$963k | - | out (clean 27, ADX 28, RVol 0.7) |
| 19 | **NFLX** | 66.04 | - | **-** | 11 | - | POS +$20.0M | 62.25 | 65 | 65 | -$2.0M | - | out (clean 31, ADX 17, RVol 0.8) |
| 20 | **ORCL** | 125.32 | - | **-** | 11 | - | NEG -$33.6M | - | 130 | 125 | +$3.1M | - | out (clean 35, ADX 19, RVol 1.5) |
| 21 | **UBER** | 71.26 | - | **-** | 11 | - | POS +$12.5M | 68.25 | 70 | 70 | -$1.0M | - | out (clean 30, ADX 15, RVol 0.7) |
| 22 | **BABA** | 106.64 | - | **-** | 11 | - | POS +$16.9M | - | 110 | 110 | -$731k | - | out (clean 36, ADX 18, RVol 0.8) |
| 23 | **COIN** | 152.32 | - | **-** | 10 | - | POS +$28.4M | - | 148 | 150 | -$1.2M | - | out (clean 31, ADX 14, RVol 0.3) |
| 24 | **SHOP** | 152.00 | - | **-** | 10 | - | NEG -$5.6M | - | 160 | 150 | -$359k | - | out (clean 33, ADX 12, RVol 0.5) |
| 25 | **DELL** | 370.14 | - | **-** | 6 | - | NEG -$28.6M | - | 400 | 400 | +$1.4M | - | out (clean 32, ADX 15, RVol 0.8) |
| 26 | **CRM** | 226.69 | - | **-** | 6 | - | NEG -$13.1M | - | 240 | 220 | -$136k | - | out (clean 33, ADX 16, RVol 0.3) |
| 27 | **PLTR** | 171.59 | - | **-** | 4 | - | NEG -$50.5M | - | 165 | 170 | -$1.3M | - | out (clean 26, ADX 14, RVol 0.3) |

## Big prints this scan (51)
- **TSLA** PUT 390 2026-11-06 (2DTE): 2,000 @ 7.04 = **+$1.4M** BUY | vol 11,782 / OI 4,169
- **AAPL** PUT 350 2026-11-06 (2DTE): 948 @ 2.39 = **+$227k** BUY | vol 25,371 / OI 2,166
- **SPY** PUT 770 2026-11-06 (2DTE): 370 @ 4.36 = **+$161k** BUY | vol 8,768 / OI 6,117
- **QQQ** PUT 696 2026-11-05 (1DTE): 300 @ 5.32 = **+$160k** BUY | vol 13,580 / OI 0
- **QQQ** PUT 698 2026-11-04 (0DTE): 300 @ 4.86 = **+$146k** BUY | vol 58,653 / OI 420
- **IWM** PUT 284 2026-11-05 (1DTE): 1,200 @ 1.16 = **+$139k** BUY | vol 12,252 / OI 134
- **MU** CALL 825 2026-11-11 (7DTE): 67 @ 19.50 = **+$131k** SELL | vol 210 / OI 2
- **IWM** PUT 284 2026-11-05 (1DTE): 1,097 @ 1.16 = **+$127k** BUY | vol 12,252 / OI 134
- **SPY** PUT 768 2026-11-05 (1DTE): 500 @ 2.53 = **+$126k** BUY | vol 44,967 / OI 0
- **QQQ** CALL 685 2026-11-04 (0DTE): 150 @ 8.09 = **+$121k** SELL | vol 5,068 / OI 3,466
- **QQQ** PUT 694 2026-11-06 (2DTE): 196 @ 5.91 = **+$116k** BUY | vol 3,916 / OI 1,129
- **TSLA** PUT 390 2026-11-06 (2DTE): 158 @ 6.70 = **+$106k** BUY | vol 11,782 / OI 4,169
- **META** PUT 635 2026-11-04 (0DTE): 149 @ 6.30 = **+$94k** SELL | vol 11,887 / OI 171
- **MU** CALL 840 2026-11-09 (5DTE): 91 @ 9.90 = **+$90k** BUY | vol 874 / OI 334
- **AMD** CALL 480 2026-11-06 (2DTE): 60 @ 15.00 = **+$90k** SELL | vol 1,837 / OI 265

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 767 2026-11-12 (8DTE): 504 traded vs OI 0
- **QQQ** CALL 685 2026-11-05 (1DTE): 858 traded vs OI 852
- **QQQ** PUT 653 2026-11-05 (1DTE): 622 traded vs OI 0
- **QQQ** CALL 717 2026-11-20 (16DTE): 1,200 traded vs OI 1,128
- **QQQ** PUT 725 2026-11-27 (23DTE): 506 traded vs OI 338
- **QQQ** CALL 718 2026-11-20 (16DTE): 986 traded vs OI 912
- **IWM** PUT 270 2026-12-04 (30DTE): 1,042 traded vs OI 512
- **TSLA** PUT 355 2026-11-11 (7DTE): 507 traded vs OI 91
- **AAPL** CALL 362.5 2026-11-13 (9DTE): 1,344 traded vs OI 362
- **AMD** PUT 457.5 2026-11-06 (2DTE): 506 traded vs OI 236
- **AVGO** PUT 322.5 2026-11-06 (2DTE): 528 traded vs OI 504
- **DELL** CALL 370 2026-11-06 (2DTE): 509 traded vs OI 10
- **MU** CALL 830 2026-11-13 (9DTE): 516 traded vs OI 59
- **MSTR** CALL 155 2026-11-13 (9DTE): 502 traded vs OI 0
- **MSTR** CALL 140 2026-11-13 (9DTE): 642 traded vs OI 543

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
