# GEX + FLOW SCAN - Wed Nov 04, 02:10 PM ET
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
Last 1m check 14:10:08 ET, last candle SPY 14:09, QQQ 14:09 | no errors
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
| 1 | **SMCI** | 29.90 | TREND (flow not with it) | **PUTS** | 39 | none: 12 puts 0-7DTE > 2 priced 0.40-0.80 > 2 delta 0.2+ > 2 spread ok > 2 liquid > best one only +19% at the target (needs +20%) | NEG -$1.0M | - | 32 | 30 | +$2.0M | - | SHORT (clean 34, ADX 26, RVol 1.4) |
| 2 | **SMH** | 505.99 | - | **-** | 26 | - | NEG -$574.0M | - | 532.5 | 500 | +$22.2M | +$0 bull / -$250k bear | out (clean 33, ADX 16, RVol 0.6) |
| 3 | **AAPL** | 352.56 | - | **-** | 24 | - | POS +$970.0M | 342.94 | 355 | 350 | -$77.3M | +$227k bull / -$42k bear | out (clean 32, ADX 22, RVol 0.5) |
| 4 | **MSFT** | 555.85 | - | **-** | 20 | - | POS +$1.0B | - | 550 | 535 | -$16.8M | +$0 bull / -$29k bear | out (clean 29, ADX 23, RVol 0.8) |
| 5 | **MU** | 808.67 | - | **-** | 20 | - | NEG -$397.2M | - | 850 | 800 | +$108.4M | +$269k bull / -$915k bear | out (clean 32, ADX 17, RVol 0.8) |
| 6 | **TSLA** | 390.87 | - | **-** | 19 | - | NEG -$66.3M | 396.54 | 400 | 390 | -$82.5M | +$94k bull / -$62k bear | out (clean 31, ADX 15, RVol 0.3) |
| 7 | **AMD** | 483.99 | - | **-** | 19 | - | NEG -$97.7M | - | 500 | 500 | +$50.2M | +$120k bull / -$1.5M bear | out (clean 32, ADX 15, RVol 0.4) |
| 8 | **META** | 629.75 | - | **-** | 19 | - | POS +$163.8M | 620 | 650 | 625 | +$9.3M | +$326k bull / -$93k bear | out (clean 32, ADX 28, RVol 1.0) |
| 9 | **AMZN** | 268.92 | - | **-** | 19 | - | POS +$564.0M | - | 270 | 250 | -$18.7M | +$87k bull / +$0 bear | out (clean 36, ADX 25, RVol 0.6) |
| 10 | **AVGO** | 327.58 | - | **-** | 17 | - | NEG -$101.7M | - | 340 | 330 | +$3.5M | +$26k bull / +$0 bear | out (clean 30, ADX 17, RVol 0.6) |
| 11 | **SPY** | 768.62 | - | **-** | 16 | - | NEG -$1.9B | 769.88 | 770 | 767 | -$89.5M | +$110k bull / -$665k bear | out (clean 32, ADX 17, RVol 0.4) |
| 12 | **HOOD** | 88.12 | - | **-** | 15 | - | POS +$2.9M | 84.7 | 90 | 90 | -$807k | +$29k bull / -$44k bear | out (clean 29, ADX 17, RVol 0.4) |
| 13 | **NVDA** | 203.96 | - | **-** | 14 | - | NEG -$5.9M | 204.02 | 210 | 200 | +$3.1M | +$95k bull / -$954k bear | out (clean 30, ADX 14, RVol 0.6) |
| 14 | **GOOGL** | 291.62 | - | **-** | 12 | - | POS +$93.9M | 285.7 | 290 | 290 | -$26.2M | - | out (clean 36, ADX 15, RVol 0.2) |
| 15 | **MSTR** | 145.17 | - | **-** | 12 | - | POS +$124.0M | - | 135 | 150 | -$9.8M | - | out (clean 31, ADX 27, RVol 0.5) |
| 16 | **ARM** | 191.91 | - | **-** | 12 | - | NEG -$7.2M | - | 200 | 200 | +$971k | - | out (clean 27, ADX 29, RVol 0.7) |
| 17 | **NFLX** | 66.02 | - | **-** | 11 | - | POS +$20.9M | 62.46 | 65 | 65 | -$2.0M | - | out (clean 31, ADX 18, RVol 0.7) |
| 18 | **ORCL** | 125.90 | - | **-** | 11 | - | NEG -$31.5M | - | 130 | 125 | +$3.0M | - | out (clean 35, ADX 19, RVol 1.4) |
| 19 | **UBER** | 71.13 | - | **-** | 11 | - | POS +$12.8M | 68.21 | 70 | 70 | -$1.0M | - | out (clean 30, ADX 17, RVol 0.6) |
| 20 | **BABA** | 106.56 | - | **-** | 11 | - | POS +$16.8M | - | 110 | 110 | -$727k | - | out (clean 36, ADX 21, RVol 0.8) |
| 21 | **COIN** | 152.27 | - | **-** | 10 | - | POS +$29.0M | - | 148 | 150 | -$1.2M | - | out (clean 31, ADX 16, RVol 0.2) |
| 22 | **SHOP** | 151.88 | - | **-** | 10 | - | NEG -$5.2M | - | 160 | 150 | -$353k | - | out (clean 33, ADX 12, RVol 0.5) |
| 23 | **DELL** | 370.23 | - | **-** | 7 | - | NEG -$28.5M | - | 400 | 400 | +$1.6M | - | out (clean 32, ADX 14, RVol 0.8) |
| 24 | **IWM** | 284.27 | - | **-** | 6 | - | NEG -$35.4M | 284.42 | 285 | 270 | +$10.1M | - | out (clean 35, ADX 10, RVol 0.5) |
| 25 | **CRM** | 226.53 | - | **-** | 6 | - | NEG -$12.8M | - | 240 | 220 | -$132k | - | out (clean 33, ADX 18, RVol 0.2) |
| 26 | **QQQ** | 695.03 | - | **-** | 5 | - | NEG -$4.7B | 719.51 | 700 | 680 | -$110.8M | - | out (clean 33, ADX 13, RVol 0.6) |
| 27 | **PLTR** | 171.88 | - | **-** | 4 | - | NEG -$51.5M | - | 165 | 170 | -$1.3M | - | out (clean 26, ADX 13, RVol 0.4) |

## Big prints this scan (20)
- **AAPL** CALL 360 2026-11-09 (5DTE): 942 @ 1.42 = **+$134k** BUY | vol 1,995 / OI 336
- **AMD** PUT 460 2026-11-06 (2DTE): 144 @ 5.60 = **+$81k** BUY | vol 2,253 / OI 4,085
- **AMD** PUT 485 2026-11-06 (2DTE): 50 @ 15.50 = **+$78k** BUY | vol 2,080 / OI 426
- **MU** CALL 815 2026-11-06 (2DTE): 33 @ 15.68 = **+$52k** SELL | vol 2,343 / OI 51
- **NVDA** CALL 205 2026-11-06 (2DTE): 200 @ 2.47 = **+$49k** SELL | vol 31,699 / OI 5,568
- **HOOD** CALL 87 2026-11-06 (2DTE): 167 @ 2.61 = **+$44k** SELL | vol 7,995 / OI 1,164
- **MU** PUT 810 2026-11-06 (2DTE): 20 @ 21.38 = **+$43k** BUY | vol 3,042 / OI 1,259
- **MU** PUT 810 2026-11-06 (2DTE): 20 @ 21.35 = **+$43k** BUY | vol 3,042 / OI 1,259
- **META** PUT 625 2026-11-04 (0DTE): 500 @ 0.82 = **+$41k** BUY | vol 14,097 / OI 250
- **AAPL** CALL 362.5 2026-11-09 (5DTE): 394 @ 0.93 = **+$37k** BUY | vol 1,454 / OI 74
- **META** CALL 637.5 2026-11-06 (2DTE): 54 @ 6.15 = **+$33k** BUY | vol 1,464 / OI 883
- **MU** PUT 805 2026-11-06 (2DTE): 17 @ 19.35 = **+$33k** BUY | vol 2,797 / OI 615
- **META** CALL 637.5 2026-11-06 (2DTE): 54 @ 6.00 = **+$32k** MID | vol 1,464 / OI 883
- **MU** CALL 805 2026-11-04 (0DTE): 64 @ 4.95 = **+$32k** SELL | vol 12,663 / OI 15
- **AMD** CALL 485 2026-11-04 (0DTE): 146 @ 2.01 = **+$29k** SELL | vol 10,694 / OI 228

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 770 2026-11-09 (5DTE): 3,821 traded vs OI 3,768
- **SPY** PUT 730 2026-11-05 (1DTE): 4,427 traded vs OI 3,949
- **SPY** PUT 757 2026-11-11 (7DTE): 551 traded vs OI 0
- **SPY** CALL 769 2026-11-12 (8DTE): 501 traded vs OI 0
- **SPY** CALL 775 2026-11-13 (9DTE): 3,338 traded vs OI 3,337
- **SPY** PUT 699 2026-11-30 (26DTE): 504 traded vs OI 192
- **SPY** PUT 755 2026-11-18 (14DTE): 572 traded vs OI 0
- **QQQ** PUT 666 2026-11-06 (2DTE): 502 traded vs OI 0
- **SMH** CALL 505 2026-11-04 (0DTE): 505 traded vs OI 11
- **SMH** CALL 520 2026-11-20 (16DTE): 914 traded vs OI 847
- **NVDA** PUT 217.5 2026-11-06 (2DTE): 2,322 traded vs OI 2,078
- **TSLA** PUT 387.5 2026-11-13 (9DTE): 506 traded vs OI 172
- **AAPL** CALL 362.5 2026-11-09 (5DTE): 1,454 traded vs OI 74
- **META** PUT 592.5 2026-11-06 (2DTE): 500 traded vs OI 208

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
