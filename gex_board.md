# GEX + FLOW SCAN - Wed Nov 04, 02:50 PM ET
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
Last 1m check 14:50:08 ET, last candle SPY 14:49, QQQ 14:49 | no errors
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
| 1 | **SMH** | 503.47 | FLOW SURGE | **CALLS** | 36 | none: 156 calls 0-7DTE > 9 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (65 contracts' greeks worked out here) | NEG -$605.1M | - | 532.5 | 500 | +$22.9M | +$126k bull / +$0 bear | out (clean 32, ADX 17, RVol 0.5) |
| 2 | **SMCI** | 29.66 | TREND (flow not with it) | **PUTS** | 32 | none: 12 puts 0-7DTE > 2 priced 0.40-0.80 > 2 delta 0.2+ > 2 spread ok > 2 liquid > best one only +13% at the target (needs +20%) | NEG -$1.1M | - | 32 | 30 | +$2.0M | - | SHORT (clean 34, ADX 24, RVol 0.8) |
| 3 | **AAPL** | 352.78 | - | **-** | 23 | - | POS +$996.1M | 342.54 | 355 | 350 | -$76.0M | +$1.0M bull / +$0 bear | out (clean 32, ADX 15, RVol 0.7) |
| 4 | **MU** | 801.32 | - | **-** | 21 | - | NEG -$406.1M | - | 850 | 800 | +$118.5M | +$2.5M bull / -$386k bear | out (clean 31, ADX 20, RVol 0.8) |
| 5 | **MSFT** | 557.51 | - | **-** | 20 | - | POS +$1.0B | - | 550 | 535 | -$17.4M | +$0 bull / -$48k bear | out (clean 29, ADX 19, RVol 1.3) |
| 6 | **TSLA** | 389.85 | - | **-** | 19 | - | NEG -$93.3M | 394.73 | 400 | 390 | -$78.6M | +$349k bull / -$155k bear | out (clean 31, ADX 16, RVol 0.4) |
| 7 | **AMD** | 482.45 | - | **-** | 19 | - | NEG -$104.0M | - | 500 | 500 | +$51.0M | +$66k bull / -$100k bear | out (clean 32, ADX 16, RVol 0.4) |
| 8 | **META** | 628.85 | - | **-** | 19 | - | POS +$139.5M | 621.78 | 650 | 625 | +$11.0M | +$0 bull / -$426k bear | out (clean 32, ADX 30, RVol 0.7) |
| 9 | **AMZN** | 268.48 | - | **-** | 18 | - | POS +$568.4M | - | 270 | 250 | -$17.6M | +$94k bull / +$0 bear | out (clean 36, ADX 17, RVol 0.5) |
| 10 | **SPY** | 767.88 | - | **-** | 15 | - | NEG -$3.3B | 769.64 | 770 | 767 | -$90.5M | +$627k bull / -$1.1M bear | out (clean 32, ADX 14, RVol 0.6) |
| 11 | **QQQ** | 693.25 | - | **-** | 15 | - | NEG -$5.2B | 718.01 | 700 | 680 | -$81.6M | +$747k bull / -$5.2M bear | out (clean 32, ADX 13, RVol 0.4) |
| 12 | **NVDA** | 203.36 | - | **-** | 14 | - | NEG -$66.7M | 204.07 | 210 | 200 | +$4.9M | +$218k bull / +$0 bear | out (clean 30, ADX 11, RVol 0.7) |
| 13 | **PLTR** | 170.58 | - | **-** | 13 | - | NEG -$51.6M | - | 165 | 170 | -$733k | +$269k bull / +$0 bear | out (clean 26, ADX 11, RVol 0.4) |
| 14 | **ORCL** | 125.42 | - | **-** | 13 | - | NEG -$34.0M | - | 130 | 125 | +$3.6M | - | out (clean 34, ADX 23, RVol 1.8) |
| 15 | **GOOGL** | 291.71 | - | **-** | 12 | - | POS +$101.3M | 282.96 | 290 | 290 | -$26.6M | - | out (clean 36, ADX 12, RVol 0.4) |
| 16 | **NFLX** | 66.39 | - | **-** | 12 | - | POS +$18.2M | - | 65 | 65 | -$2.0M | - | out (clean 31, ADX 21, RVol 0.9) |
| 17 | **ARM** | 191.42 | - | **-** | 12 | - | NEG -$7.3M | - | 200 | 200 | +$1.1M | - | out (clean 26, ADX 29, RVol 0.7) |
| 18 | **UBER** | 70.64 | - | **-** | 11 | - | POS +$9.9M | 68.59 | 70 | 65 | -$989k | - | out (clean 31, ADX 16, RVol 0.9) |
| 19 | **MSTR** | 143.48 | - | **-** | 10 | - | POS +$133.3M | - | 135 | 150 | -$9.3M | - | out (clean 31, ADX 22, RVol 0.4) |
| 20 | **SHOP** | 151.84 | - | **-** | 10 | - | NEG -$5.3M | - | 160 | 150 | -$360k | - | out (clean 32, ADX 10, RVol 0.5) |
| 21 | **COIN** | 151.09 | - | **-** | 9 | - | POS +$30.8M | - | 148 | 150 | -$1.2M | - | out (clean 31, ADX 12, RVol 0.2) |
| 22 | **AVGO** | 326.52 | - | **-** | 8 | - | NEG -$108.0M | - | 340 | 330 | +$5.8M | - | out (clean 30, ADX 16, RVol 0.5) |
| 23 | **DELL** | 368.54 | - | **-** | 7 | - | NEG -$27.9M | - | 400 | 400 | +$1.4M | - | out (clean 33, ADX 19, RVol 0.9) |
| 24 | **CRM** | 226.66 | - | **-** | 6 | - | NEG -$13.0M | - | 240 | 220 | -$132k | - | out (clean 34, ADX 12, RVol 0.6) |
| 25 | **BABA** | 106.18 | - | **-** | 6 | - | POS +$16.4M | - | 105 | 110 | -$239k | - | out (clean 36, ADX 19, RVol 0.4) |
| 26 | **IWM** | 283.43 | - | **-** | 5 | - | NEG -$345.7M | 284.21 | 285 | 270 | +$9.5M | - | out (clean 34, ADX 10, RVol 0.3) |
| 27 | **HOOD** | 87.41 | - | **-** | 5 | - | POS +$2.4M | 85.02 | 90 | 90 | -$570k | - | out (clean 29, ADX 12, RVol 0.8) |

## Big prints this scan (41)
- **QQQ** PUT 693 2026-11-06 (2DTE): 5,000 @ 5.57 = **+$2.8M** BUY | vol 14,149 / OI 20,503
- **QQQ** PUT 691 2026-11-06 (2DTE): 5,000 @ 4.77 = **+$2.4M** BUY | vol 13,922 / OI 17,537
- **SPY** PUT 772 2026-11-05 (1DTE): 1,994 @ 5.00 = **+$997k** BUY | vol 10,923 / OI 0
- **MU** PUT 815 2026-11-06 (2DTE): 118 @ 26.46 = **+$312k** SELL | vol 2,096 / OI 1,070
- **MU** PUT 810 2026-11-06 (2DTE): 118 @ 23.57 = **+$278k** SELL | vol 3,525 / OI 1,259
- **MU** PUT 815 2026-11-06 (2DTE): 89 @ 26.46 = **+$235k** SELL | vol 2,096 / OI 1,070
- **MU** PUT 815 2026-11-06 (2DTE): 89 @ 26.46 = **+$235k** SELL | vol 2,096 / OI 1,070
- **MU** PUT 810 2026-11-06 (2DTE): 89 @ 23.57 = **+$210k** SELL | vol 3,525 / OI 1,259
- **MU** PUT 810 2026-11-06 (2DTE): 89 @ 23.57 = **+$210k** SELL | vol 3,525 / OI 1,259
- **SPY** PUT 769 2026-11-05 (1DTE): 500 @ 3.04 = **+$152k** BUY | vol 12,968 / OI 0
- **QQQ** PUT 694 2026-11-04 (0DTE): 775 @ 1.62 = **+$126k** SELL | vol 224,629 / OI 523
- **SMH** PUT 500 2026-11-06 (2DTE): 125 @ 5.75 = **+$72k** SELL | vol 46,728 / OI 37,205
- **META** CALL 625 2026-11-06 (2DTE): 69 @ 10.30 = **+$71k** SELL | vol 1,269 / OI 778
- **TSLA** PUT 387.5 2026-11-06 (2DTE): 125 @ 5.55 = **+$69k** MID | vol 8,186 / OI 2,978
- **MU** PUT 805 2026-11-04 (0DTE): 118 @ 5.72 = **+$67k** SELL | vol 33,027 / OI 922

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 744 2026-11-06 (2DTE): 2,659 traded vs OI 2,651
- **SPY** PUT 751 2026-11-06 (2DTE): 2,463 traded vs OI 2,380
- **SPY** CALL 800 2026-11-18 (14DTE): 589 traded vs OI 0
- **SPY** PUT 757 2026-11-20 (16DTE): 31,479 traded vs OI 30,768
- **QQQ** PUT 645 2026-11-09 (5DTE): 2,429 traded vs OI 1,558
- **QQQ** CALL 697 2026-11-13 (9DTE): 640 traded vs OI 271
- **IWM** PUT 267 2026-12-04 (30DTE): 564 traded vs OI 109
- **AAPL** CALL 370 2026-11-09 (5DTE): 530 traded vs OI 244
- **AMD** PUT 512.5 2026-11-04 (0DTE): 505 traded vs OI 87
- **NFLX** CALL 73 2026-11-27 (23DTE): 659 traded vs OI 0
- **AVGO** PUT 297.5 2026-11-09 (5DTE): 516 traded vs OI 60
- **BABA** CALL 104 2026-11-13 (9DTE): 698 traded vs OI 378

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
