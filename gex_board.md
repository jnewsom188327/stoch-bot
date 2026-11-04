# GEX + FLOW SCAN - Wed Nov 04, 01:30 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (10)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 13:05 | **AAPL** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/04 352.5P | 0.58 | 0.86 | +50% (19m) | **+48%** | +57% | 352.38 |
| 12:50 | **AMZN** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/04 267.5P | 0.40 | 0.25 | +17% (7m) | **-38%** | +109% | 267.48 |
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
Last 1m check 13:30:08 ET, last candle SPY 13:29, QQQ 13:29 | no errors
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
| 1 | **AMZN** | 269.24 | TREND (flow not with it) | **CALLS** | 31 | none: 88 calls 0-7DTE > 6 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only -2% at the target (needs +20%) (35 contracts' greeks worked out here) | POS +$574.5M | - | 270 | 250 | -$21.3M | +$222k bull / -$366k bear | LONG (clean 36, ADX 36, RVol 1.1) |
| 2 | **AAPL** | 352.76 | - | **-** | 28 | - | POS +$1.0B | 341.74 | 355 | 350 | -$80.2M | +$368k bull / -$304k bear | out (clean 32, ADX 36, RVol 0.8) |
| 3 | **GOOGL** | 291.62 | - | **-** | 23 | - | POS +$103.2M | 283.91 | 290 | 290 | -$27.0M | +$53k bull / +$0 bear | out (clean 36, ADX 18, RVol 0.3) |
| 4 | **MSTR** | 145.60 | - | **-** | 23 | - | POS +$120.1M | - | 135 | 150 | -$10.3M | +$3.8M bull / -$4.4M bear | out (clean 31, ADX 34, RVol 0.3) |
| 5 | **MSFT** | 555.35 | - | **-** | 21 | - | POS +$1.0B | - | 550 | 535 | -$16.9M | +$0 bull / -$293k bear | out (clean 29, ADX 32, RVol 0.7) |
| 6 | **TSLA** | 388.50 | - | **-** | 20 | - | NEG -$98.8M | 397.63 | 400 | 380 | -$80.2M | +$2.2M bull / +$0 bear | out (clean 31, ADX 18, RVol 0.5) |
| 7 | **MU** | 809.03 | - | **-** | 20 | - | NEG -$382.2M | - | 850 | 800 | +$100.7M | +$1.6M bull / -$1.3M bear | out (clean 31, ADX 18, RVol 0.4) |
| 8 | **AMD** | 483.56 | - | **-** | 19 | - | NEG -$89.9M | - | 500 | 440 | +$47.6M | +$355k bull / -$30k bear | out (clean 32, ADX 12, RVol 0.5) |
| 9 | **ORCL** | 125.68 | - | **-** | 19 | - | NEG -$31.5M | - | 130 | 125 | +$2.6M | +$85k bull / +$0 bear | out (clean 34, ADX 10, RVol 1.3) |
| 10 | **SPY** | 768.11 | - | **-** | 18 | - | NEG -$2.2B | 769.8 | 770 | 767 | -$109.9M | +$1.5M bull / +$0 bear | out (clean 32, ADX 25, RVol 0.4) |
| 11 | **SMCI** | 30.04 | - | **-** | 18 | - | NEG -$611k | - | 33 | 30 | +$2.0M | - | out (clean 33, ADX 24, RVol 1.0) |
| 12 | **META** | 634.67 | - | **-** | 16 | - | POS +$199.2M | 621.02 | 650 | 625 | +$3.7M | +$587k bull / +$0 bear | out (clean 31, ADX 22, RVol 0.8) |
| 13 | **HOOD** | 88.02 | - | **-** | 16 | - | POS +$3.6M | 84.23 | 90 | 90 | -$809k | +$25k bull / +$0 bear | out (clean 28, ADX 22, RVol 0.7) |
| 14 | **QQQ** | 694.95 | - | **-** | 15 | - | NEG -$4.7B | 718.14 | 700 | 680 | -$127.7M | +$418k bull / +$0 bear | out (clean 32, ADX 10, RVol 0.6) |
| 15 | **SMH** | 506.09 | - | **-** | 14 | - | NEG -$551.0M | - | 532.5 | 500 | +$21.4M | - | out (clean 32, ADX 14, RVol 0.2) |
| 16 | **NVDA** | 204.07 | - | **-** | 14 | - | NEG -$11.8M | 204.19 | 210 | 200 | -$80k | +$0 bull / -$335k bear | out (clean 30, ADX 15, RVol 0.8) |
| 17 | **UBER** | 71.55 | - | **-** | 14 | - | POS +$13.1M | 68.25 | 70 | 70 | -$1.2M | - | out (clean 30, ADX 23, RVol 0.6) |
| 18 | **BABA** | 107.14 | - | **-** | 13 | - | POS +$16.3M | - | 110 | 110 | -$853k | - | out (clean 36, ADX 27, RVol 0.5) |
| 19 | **NFLX** | 65.92 | - | **-** | 12 | - | POS +$20.8M | 62.32 | 65 | 65 | -$1.9M | - | out (clean 31, ADX 25, RVol 0.8) |
| 20 | **COIN** | 152.78 | - | **-** | 11 | - | POS +$28.7M | - | 148 | 155 | -$1.2M | - | out (clean 31, ADX 21, RVol 0.2) |
| 21 | **ARM** | 192.98 | - | **-** | 11 | - | NEG -$7.0M | - | 200 | 200 | +$922k | - | out (clean 26, ADX 24, RVol 0.8) |
| 22 | **SHOP** | 151.68 | - | **-** | 11 | - | NEG -$5.6M | - | 160 | 150 | -$349k | - | out (clean 33, ADX 17, RVol 0.3) |
| 23 | **CRM** | 225.49 | - | **-** | 8 | - | NEG -$13.5M | - | 240 | 220 | -$142k | - | out (clean 34, ADX 24, RVol 0.4) |
| 24 | **IWM** | 284.06 | - | **-** | 7 | - | NEG -$166.8M | 284.45 | 285 | 270 | +$9.8M | - | out (clean 35, ADX 14, RVol 0.7) |
| 25 | **AVGO** | 328.28 | - | **-** | 6 | - | NEG -$91.8M | - | 340 | 330 | +$2.6M | - | out (clean 30, ADX 13, RVol 0.8) |
| 26 | **PLTR** | 171.09 | - | **-** | 6 | - | NEG -$50.4M | - | 165 | 170 | -$1.3M | - | out (clean 26, ADX 18, RVol 0.6) |
| 27 | **DELL** | 376.46 | - | **-** | 6 | - | NEG -$30.8M | - | 400 | 400 | +$1.4M | - | out (clean 32, ADX 14, RVol 0.4) |

## Big prints this scan (49)
- **MU** CALL 810 2026-11-04 (0DTE): 498 @ 3.55 = **+$177k** SELL | vol 23,376 / OI 30
- **TSLA** PUT 390 2026-11-06 (2DTE): 256 @ 6.75 = **+$173k** SELL | vol 8,012 / OI 4,169
- **QQQ** PUT 697 2026-11-04 (0DTE): 623 @ 2.18 = **+$136k** SELL | vol 91,585 / OI 457
- **MU** PUT 805 2026-11-09 (5DTE): 50 @ 22.91 = **+$115k** BUY | vol 649 / OI 219
- **QQQ** CALL 686 2026-11-04 (0DTE): 120 @ 9.48 = **+$114k** BUY | vol 2,893 / OI 368
- **AMZN** CALL 270 2026-11-06 (2DTE): 302 @ 3.60 = **+$109k** BUY | vol 37,582 / OI 13,073
- **MU** PUT 800 2026-11-06 (2DTE): 60 @ 16.30 = **+$98k** BUY | vol 9,320 / OI 3,802
- **TSLA** CALL 387.5 2026-11-04 (0DTE): 350 @ 2.79 = **+$98k** BUY | vol 78,675 / OI 101
- **MU** PUT 800 2026-11-04 (0DTE): 400 @ 2.30 = **+$92k** BUY | vol 53,854 / OI 1,387
- **MSFT** CALL 565 2026-11-06 (2DTE): 400 @ 2.15 = **+$86k** SELL | vol 3,611 / OI 2,065
- **MU** PUT 800 2026-11-04 (0DTE): 375 @ 2.21 = **+$83k** BUY | vol 53,854 / OI 1,387
- **TSLA** CALL 390 2026-11-06 (2DTE): 118 @ 6.45 = **+$76k** BUY | vol 19,707 / OI 2,560
- **MU** PUT 800 2026-11-04 (0DTE): 321 @ 2.20 = **+$71k** BUY | vol 53,854 / OI 1,387
- **TSLA** CALL 392.5 2026-11-09 (5DTE): 100 @ 6.60 = **+$66k** BUY | vol 663 / OI 175
- **MU** CALL 815 2026-11-06 (2DTE): 36 @ 16.20 = **+$58k** SELL | vol 2,122 / OI 51

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 707 2026-11-05 (1DTE): 928 traded vs OI 0
- **SPY** PUT 703 2026-11-05 (1DTE): 583 traded vs OI 0
- **QQQ** CALL 739 2026-11-06 (2DTE): 1,011 traded vs OI 740
- **QQQ** PUT 661 2026-11-05 (1DTE): 507 traded vs OI 0
- **QQQ** CALL 695 2026-11-13 (9DTE): 3,011 traded vs OI 2,851
- **QQQ** PUT 690 2026-11-18 (14DTE): 525 traded vs OI 0
- **NVDA** CALL 185 2026-11-06 (2DTE): 500 traded vs OI 227
- **NVDA** CALL 220 2026-11-13 (9DTE): 13,284 traded vs OI 12,839
- **AMD** PUT 482.5 2026-11-06 (2DTE): 506 traded vs OI 282
- **AMZN** PUT 252.5 2026-11-13 (9DTE): 1,647 traded vs OI 273
- **AMZN** CALL 280 2026-11-13 (9DTE): 3,260 traded vs OI 3,259
- **AMZN** PUT 262.5 2026-11-13 (9DTE): 830 traded vs OI 18
- **GOOGL** PUT 265 2026-11-13 (9DTE): 548 traded vs OI 512
- **COIN** PUT 149 2026-11-06 (2DTE): 502 traded vs OI 108

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
