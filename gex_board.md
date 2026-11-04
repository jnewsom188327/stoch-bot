# GEX + FLOW SCAN - Wed Nov 04, 03:00 PM ET
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
Last 1m check 15:00:08 ET, last candle SPY 14:59, QQQ 14:59 | no errors
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
| 1 | **SMH** | 502.49 | FLOW SURGE | **CALLS** | 36 | none: 158 calls 0-7DTE > 9 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only -18% at the target (needs +20%) (60 contracts' greeks worked out here) | NEG -$585.7M | - | 532.5 | 500 | +$22.9M | +$151k bull / +$0 bear | out (clean 32, ADX 19, RVol 0.5) |
| 2 | **UBER** | 70.12 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 31 | none: 14 puts 0-7DTE > 1 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only -14% at the target (needs +20%) | POS +$7.4M | 68.61 | 70 | 65 | -$645k | - | out (clean 31, ADX 22, RVol 1.2) |
| 3 | **AAPL** | 352.08 | - | **-** | 23 | - | POS +$901.3M | 342.88 | 350 | 350 | -$75.1M | +$223k bull / +$0 bear | out (clean 32, ADX 13, RVol 0.7) |
| 4 | **MU** | 798.60 | - | **-** | 22 | - | NEG -$372.0M | - | 850 | 800 | +$119.9M | +$2.8M bull / -$45k bear | out (clean 31, ADX 23, RVol 0.8) |
| 5 | **GOOGL** | 291.29 | - | **-** | 21 | - | POS +$108.8M | 283.39 | 290 | 290 | -$26.4M | +$0 bull / -$70k bear | out (clean 36, ADX 10, RVol 0.3) |
| 6 | **MSFT** | 557.64 | - | **-** | 20 | - | POS +$1.0B | - | 550 | 535 | -$17.3M | +$0 bull / -$815k bear | out (clean 29, ADX 20, RVol 1.2) |
| 7 | **TSLA** | 388.35 | - | **-** | 19 | - | NEG -$114.5M | 394.8 | 400 | 390 | -$77.8M | +$396k bull / -$300k bear | out (clean 30, ADX 15, RVol 0.5) |
| 8 | **AMD** | 482.11 | - | **-** | 19 | - | NEG -$94.6M | - | 500 | 440 | +$50.2M | +$66k bull / -$289k bear | out (clean 32, ADX 15, RVol 0.4) |
| 9 | **META** | 628.32 | - | **-** | 18 | - | POS +$150.1M | 619.84 | 650 | 625 | +$11.4M | +$87k bull / -$340k bear | out (clean 32, ADX 30, RVol 0.4) |
| 10 | **AMZN** | 267.86 | - | **-** | 18 | - | POS +$582.9M | - | 270 | 250 | -$17.5M | +$97k bull / +$0 bear | out (clean 36, ADX 16, RVol 0.6) |
| 11 | **AVGO** | 326.00 | - | **-** | 18 | - | NEG -$106.5M | - | 340 | 320 | +$5.9M | +$89k bull / +$0 bear | out (clean 30, ADX 18, RVol 0.5) |
| 12 | **SMCI** | 29.55 | - | **-** | 18 | - | NEG -$1.0M | - | 32 | 30 | +$2.1M | - | out (clean 34, ADX 27, RVol 0.9) |
| 13 | **NVDA** | 202.49 | - | **-** | 16 | - | NEG -$86.0M | 203.39 | 210 | 200 | +$10.0M | +$143k bull / +$0 bear | out (clean 30, ADX 15, RVol 0.8) |
| 14 | **SPY** | 767.30 | - | **-** | 15 | - | NEG -$3.7B | 769.1 | 770 | 767 | -$94.0M | +$6.4M bull / -$1.1M bear | out (clean 32, ADX 14, RVol 0.5) |
| 15 | **QQQ** | 692.43 | - | **-** | 15 | - | NEG -$5.1B | 717.43 | 700 | 680 | -$82.6M | +$446k bull / -$5.2M bear | out (clean 32, ADX 15, RVol 0.4) |
| 16 | **HOOD** | 87.47 | - | **-** | 15 | - | POS +$2.3M | 85.12 | 90 | 90 | -$638k | +$27k bull / +$0 bear | out (clean 29, ADX 14, RVol 0.8) |
| 17 | **NFLX** | 66.53 | - | **-** | 13 | - | POS +$18.7M | - | 65 | 65 | -$2.1M | - | out (clean 32, ADX 25, RVol 1.0) |
| 18 | **ORCL** | 125.06 | - | **-** | 13 | - | NEG -$34.8M | - | 130 | 125 | +$3.6M | - | out (clean 33, ADX 25, RVol 1.5) |
| 19 | **ARM** | 191.11 | - | **-** | 12 | - | NEG -$7.1M | - | 200 | 200 | +$1.1M | - | out (clean 26, ADX 30, RVol 0.5) |
| 20 | **SHOP** | 152.61 | - | **-** | 11 | - | NEG -$5.1M | - | 160 | 150 | -$382k | - | out (clean 32, ADX 14, RVol 0.5) |
| 21 | **MSTR** | 143.21 | - | **-** | 10 | - | POS +$132.1M | - | 135 | 150 | -$9.2M | - | out (clean 31, ADX 25, RVol 0.4) |
| 22 | **COIN** | 151.31 | - | **-** | 9 | - | POS +$30.0M | - | 148 | 150 | -$1.2M | - | out (clean 31, ADX 12, RVol 0.3) |
| 23 | **DELL** | 367.37 | - | **-** | 7 | - | NEG -$27.4M | - | 400 | 400 | +$970k | - | out (clean 33, ADX 22, RVol 0.9) |
| 24 | **CRM** | 227.49 | - | **-** | 7 | - | NEG -$10.0M | 237.11 | 240 | 220 | -$181k | - | out (clean 34, ADX 13, RVol 0.5) |
| 25 | **IWM** | 283.38 | - | **-** | 6 | - | NEG -$314.4M | 284.16 | 285 | 270 | +$9.4M | - | out (clean 34, ADX 13, RVol 0.3) |
| 26 | **BABA** | 106.04 | - | **-** | 6 | - | POS +$16.8M | - | 110 | 110 | -$216k | - | out (clean 36, ADX 21, RVol 0.6) |
| 27 | **PLTR** | 170.95 | - | **-** | 3 | - | NEG -$51.1M | - | 165 | 170 | -$822k | - | out (clean 26, ADX 10, RVol 0.3) |

## Big prints this scan (34)
- **SPY** PUT 772 2026-11-10 (6DTE): 1,900 @ 6.48 = **+$1.2M** SELL | vol 6,035 / OI 0
- **SPY** PUT 772 2026-11-05 (1DTE): 1,900 @ 4.54 = **+$863k** SELL | vol 16,938 / OI 0
- **MSFT** CALL 557.5 2026-11-06 (2DTE): 191 @ 5.67 = **+$108k** SELL | vol 9,198 / OI 6,272
- **MSFT** CALL 560 2026-11-06 (2DTE): 191 @ 4.52 = **+$86k** SELL | vol 9,969 / OI 5,047
- **AMZN** CALL 257.5 2026-11-04 (0DTE): 50 @ 10.83 = **+$54k** MID | vol 1,717 / OI 2,988
- **MSFT** CALL 532.5 2026-11-04 (0DTE): 20 @ 24.90 = **+$50k** SELL | vol 848 / OI 1,499
- **MSFT** CALL 532.5 2026-11-04 (0DTE): 20 @ 24.50 = **+$49k** SELL | vol 848 / OI 1,499
- **MSFT** CALL 532.5 2026-11-04 (0DTE): 20 @ 24.50 = **+$49k** SELL | vol 848 / OI 1,499
- **MSFT** CALL 532.5 2026-11-04 (0DTE): 20 @ 24.00 = **+$48k** SELL | vol 848 / OI 1,499
- **MSFT** CALL 532.5 2026-11-04 (0DTE): 20 @ 23.90 = **+$48k** SELL | vol 848 / OI 1,499
- **TSLA** PUT 405 2026-11-09 (5DTE): 25 @ 18.50 = **+$46k** SELL | vol 88 / OI 340
- **MU** PUT 800 2026-11-09 (5DTE): 20 @ 22.03 = **+$44k** SELL | vol 1,396 / OI 321
- **MU** PUT 800 2026-11-09 (5DTE): 20 @ 21.80 = **+$44k** SELL | vol 1,396 / OI 321
- **MU** PUT 800 2026-11-04 (0DTE): 179 @ 2.40 = **+$43k** SELL | vol 78,440 / OI 1,387
- **TSLA** CALL 382.5 2026-11-06 (2DTE): 40 @ 10.68 = **+$43k** BUY | vol 6,017 / OI 712

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 775 2026-11-10 (6DTE): 5,186 traded vs OI 4,252
- **SPY** PUT 738 2026-11-11 (7DTE): 1,441 traded vs OI 0
- **SPY** CALL 773 2026-11-13 (9DTE): 1,205 traded vs OI 1,096
- **QQQ** PUT 666 2026-11-05 (1DTE): 536 traded vs OI 0
- **TSLA** PUT 350 2026-11-09 (5DTE): 733 traded vs OI 677
- **AAPL** CALL 360 2026-11-11 (7DTE): 549 traded vs OI 84
- **AAPL** PUT 360 2026-11-04 (0DTE): 517 traded vs OI 25
- **AMD** CALL 485 2026-11-20 (16DTE): 501 traded vs OI 0
- **AMD** PUT 472.5 2026-11-06 (2DTE): 521 traded vs OI 183
- **META** CALL 645 2026-11-09 (5DTE): 539 traded vs OI 114
- **AMZN** PUT 245 2026-11-13 (9DTE): 974 traded vs OI 660
- **MSFT** PUT 510 2026-11-13 (9DTE): 589 traded vs OI 584
- **NFLX** PUT 60 2026-11-27 (23DTE): 1,517 traded vs OI 1,173
- **NFLX** CALL 69 2026-12-04 (30DTE): 803 traded vs OI 167
- **NFLX** CALL 66 2026-12-04 (30DTE): 698 traded vs OI 632

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
