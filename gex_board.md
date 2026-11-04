# GEX + FLOW SCAN - Wed Nov 04, 03:45 PM ET
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
Last 1m check 15:32:08 ET, last candle SPY 15:31, QQQ 15:31 | no errors
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
| 1 | **SMH** | 500.96 | FLOW SURGE | **CALLS** | 39 | none: 154 calls 0-7DTE > 8 priced 0.40-0.80 > 1 delta 0.2+ > 0 spread ok > 0 liquid (59 contracts' greeks worked out here) | NEG -$615.7M | - | 532.5 | 500 | +$24.2M | +$1.7M bull / -$25k bear | out (clean 33, ADX 21, RVol 0.9) |
| 2 | **MU** | 793.31 | - | **-** | 25 | - | NEG -$402.8M | - | 850 | 800 | +$135.0M | +$2.3M bull / -$1.2M bear | out (clean 31, ADX 32, RVol 1.6) |
| 3 | **AAPL** | 351.91 | - | **-** | 24 | - | POS +$773.2M | 343.21 | 350 | 350 | -$74.4M | +$237k bull / +$0 bear | out (clean 32, ADX 16, RVol 1.1) |
| 4 | **ARM** | 190.10 | - | **-** | 24 | - | NEG -$7.7M | - | 200 | 200 | +$1.3M | +$805k bull / +$0 bear | out (clean 26, ADX 30, RVol 1.4) |
| 5 | **GOOGL** | 290.83 | - | **-** | 22 | - | POS +$116.5M | 282.39 | 290 | 290 | -$26.2M | +$681k bull / +$0 bear | out (clean 36, ADX 14, RVol 0.5) |
| 6 | **TSLA** | 383.56 | - | **-** | 21 | - | NEG -$108.9M | 390.59 | 400 | 380 | -$66.9M | +$2.1M bull / -$201k bear | out (clean 32, ADX 26, RVol 1.1) |
| 7 | **NVDA** | 200.80 | - | **-** | 20 | - | NEG -$187.7M | 203.16 | 210 | 200 | +$12.5M | +$300k bull / -$157k bear | out (clean 30, ADX 29, RVol 1.6) |
| 8 | **MSFT** | 557.58 | - | **-** | 20 | - | POS +$1.0B | - | 550 | 535 | -$15.7M | +$536k bull / -$327k bear | out (clean 29, ADX 20, RVol 1.5) |
| 9 | **AVGO** | 324.79 | - | **-** | 20 | - | NEG -$111.7M | 342.57 | 340 | 320 | +$5.5M | +$277k bull / -$152k bear | out (clean 30, ADX 27, RVol 0.8) |
| 10 | **AMD** | 480.79 | - | **-** | 19 | - | NEG -$93.0M | - | 500 | 480 | +$47.2M | +$263k bull / -$917k bear | out (clean 31, ADX 14, RVol 0.7) |
| 11 | **CRM** | 227.23 | - | **-** | 19 | - | NEG -$13.4M | - | 240 | 220 | -$191k | +$86k bull / +$0 bear | out (clean 34, ADX 18, RVol 1.2) |
| 12 | **AMZN** | 267.89 | - | **-** | 18 | - | POS +$552.1M | - | 270 | 250 | -$17.6M | +$72k bull / -$106k bear | out (clean 35, ADX 11, RVol 1.3) |
| 13 | **SMCI** | 29.55 | - | **-** | 18 | - | NEG -$1.9M | - | 32 | 30 | +$2.1M | - | out (clean 34, ADX 24, RVol 1.2) |
| 14 | **META** | 630.61 | - | **-** | 17 | - | POS +$155.2M | 624.71 | 650 | 625 | +$9.7M | +$268k bull / -$99k bear | out (clean 33, ADX 22, RVol 0.8) |
| 15 | **SPY** | 767.25 | - | **-** | 16 | - | NEG -$4.5B | 769.39 | 770 | 767 | -$96.2M | +$2.7M bull / -$224k bear | out (clean 32, ADX 13, RVol 1.2) |
| 16 | **QQQ** | 691.67 | - | **-** | 16 | - | NEG -$5.1B | 711.47 | 700 | 680 | -$87.6M | +$1.6M bull / -$1.2M bear | out (clean 33, ADX 16, RVol 0.8) |
| 17 | **NFLX** | 66.69 | - | **-** | 16 | - | POS +$25.9M | - | 65 | 65 | -$2.1M | - | out (clean 33, ADX 36, RVol 1.6) |
| 18 | **PLTR** | 171.21 | - | **-** | 15 | - | NEG -$48.4M | - | 165 | 170 | -$1.3M | +$0 bull / -$121k bear | out (clean 26, ADX 17, RVol 0.8) |
| 19 | **ORCL** | 124.97 | - | **-** | 15 | - | NEG -$33.2M | - | 130 | 125 | +$3.7M | - | out (clean 33, ADX 30, RVol 2.3) |
| 20 | **SHOP** | 153.06 | - | **-** | 15 | - | NEG -$4.2M | 158.53 | 160 | 150 | -$410k | - | out (clean 33, ADX 31, RVol 1.1) |
| 21 | **MSTR** | 142.21 | - | **-** | 12 | - | POS +$139.2M | - | 135 | 150 | -$9.3M | - | out (clean 32, ADX 29, RVol 1.0) |
| 22 | **UBER** | 70.23 | - | **-** | 11 | - | POS +$8.6M | 68.54 | 70 | 65 | -$637k | - | out (clean 32, ADX 25, RVol 1.6) |
| 23 | **COIN** | 151.44 | - | **-** | 9 | - | POS +$32.0M | - | 148 | 150 | -$1.2M | - | out (clean 31, ADX 11, RVol 0.4) |
| 24 | **DELL** | 368.92 | - | **-** | 8 | - | NEG -$29.3M | - | 400 | 400 | +$545k | - | out (clean 33, ADX 21, RVol 1.7) |
| 25 | **BABA** | 105.77 | - | **-** | 8 | - | POS +$17.6M | - | 105 | 100 | -$133k | - | out (clean 37, ADX 31, RVol 1.0) |
| 26 | **IWM** | 283.66 | - | **-** | 7 | - | NEG -$301.5M | 284.16 | 285 | 270 | +$8.6M | - | out (clean 35, ADX 14, RVol 1.0) |
| 27 | **HOOD** | 87.03 | - | **-** | 5 | - | POS +$7.5M | 83.14 | 90 | 90 | -$725k | - | out (clean 29, ADX 14, RVol 0.6) |

## Big prints this scan (69)
- **SPY** PUT 772 2026-11-10 (6DTE): 1,773 @ 6.69 = **+$1.2M** SELL | vol 10,041 / OI 0
- **ARM** PUT 190 2026-11-06 (2DTE): 607 @ 8.47 = **+$514k** SELL | vol 1,570 / OI 356
- **ARM** PUT 190 2026-11-06 (2DTE): 300 @ 8.68 = **+$260k** SELL | vol 1,570 / OI 356
- **MSFT** CALL 550 2026-11-06 (2DTE): 147 @ 11.38 = **+$167k** BUY | vol 5,725 / OI 3,993
- **TSLA** PUT 385 2026-11-06 (2DTE): 216 @ 5.90 = **+$127k** SELL | vol 16,248 / OI 3,022
- **MU** PUT 770 2026-11-06 (2DTE): 126 @ 8.95 = **+$113k** SELL | vol 3,539 / OI 1,462
- **MU** PUT 770 2026-11-06 (2DTE): 120 @ 9.10 = **+$109k** SELL | vol 3,539 / OI 1,462
- **AMZN** CALL 257.5 2026-11-04 (0DTE): 100 @ 10.62 = **+$106k** MID | vol 1,917 / OI 2,988
- **MU** PUT 770 2026-11-06 (2DTE): 116 @ 9.10 = **+$106k** SELL | vol 3,539 / OI 1,462
- **MU** CALL 795 2026-11-06 (2DTE): 50 @ 18.73 = **+$94k** BUY | vol 706 / OI 5
- **MU** PUT 770 2026-11-06 (2DTE): 97 @ 9.15 = **+$89k** SELL | vol 3,539 / OI 1,462
- **MSFT** CALL 560 2026-11-06 (2DTE): 151 @ 5.28 = **+$80k** BUY | vol 11,899 / OI 5,047
- **MU** PUT 770 2026-11-06 (2DTE): 85 @ 9.15 = **+$78k** SELL | vol 3,539 / OI 1,462
- **MU** PUT 770 2026-11-06 (2DTE): 84 @ 9.05 = **+$76k** SELL | vol 3,539 / OI 1,462
- **TSLA** PUT 385 2026-11-06 (2DTE): 127 @ 5.90 = **+$75k** SELL | vol 16,248 / OI 3,022

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 760 2026-11-13 (9DTE): 3,093 traded vs OI 3,012
- **QQQ** CALL 692 2026-11-09 (5DTE): 602 traded vs OI 0
- **QQQ** PUT 661 2026-11-06 (2DTE): 525 traded vs OI 0
- **QQQ** PUT 630 2026-11-09 (5DTE): 3,518 traded vs OI 2,009
- **QQQ** PUT 674 2026-11-11 (7DTE): 733 traded vs OI 0
- **IWM** PUT 276 2026-11-05 (1DTE): 538 traded vs OI 473
- **IWM** PUT 279 2026-11-10 (6DTE): 978 traded vs OI 286
- **NVDA** PUT 195 2026-11-06 (2DTE): 11,198 traded vs OI 10,976
- **TSLA** PUT 392.5 2026-11-13 (9DTE): 516 traded vs OI 170
- **TSLA** PUT 375 2026-11-13 (9DTE): 1,270 traded vs OI 1,266
- **AAPL** CALL 330 2026-11-04 (0DTE): 949 traded vs OI 917
- **AAPL** CALL 370 2026-11-27 (23DTE): 1,224 traded vs OI 945
- **AMD** PUT 442.5 2026-11-06 (2DTE): 502 traded vs OI 96
- **AMD** PUT 480 2026-11-09 (5DTE): 502 traded vs OI 64
- **MSFT** CALL 580 2026-11-06 (2DTE): 2,285 traded vs OI 2,086

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
