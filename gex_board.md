# GEX + FLOW SCAN - Wed Nov 04, 03:15 PM ET
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
Last 1m check 15:15:08 ET, last candle SPY 15:14, QQQ 15:14 | no errors
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
| 1 | **SMH** | 502.05 | FLOW SURGE | **CALLS** | 37 | none: 154 calls 0-7DTE > 9 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only -30% at the target (needs +20%) (62 contracts' greeks worked out here) | NEG -$589.8M | - | 532.5 | 500 | +$23.2M | +$25k bull / +$0 bear | out (clean 33, ADX 22, RVol 0.6) |
| 2 | **UBER** | 70.11 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 31 | none: 14 puts 0-7DTE > 1 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only -5% at the target (needs +20%) | POS +$8.6M | 68.44 | 70 | 65 | -$645k | - | out (clean 31, ADX 27, RVol 1.1) |
| 3 | **AAPL** | 352.43 | - | **-** | 23 | - | POS +$905.8M | 343.26 | 350 | 350 | -$75.3M | +$157k bull / -$102k bear | out (clean 31, ADX 14, RVol 0.8) |
| 4 | **MU** | 795.36 | - | **-** | 23 | - | NEG -$389.0M | - | 850 | 800 | +$123.0M | +$1.4M bull / -$63k bear | out (clean 31, ADX 27, RVol 1.0) |
| 5 | **ARM** | 190.92 | - | **-** | 22 | - | NEG -$8.1M | - | 200 | 200 | +$1.1M | +$0 bull / -$28k bear | out (clean 26, ADX 31, RVol 0.6) |
| 6 | **MSTR** | 143.13 | - | **-** | 21 | - | POS +$134.3M | - | 135 | 150 | -$9.4M | +$130k bull / -$38k bear | out (clean 32, ADX 26, RVol 0.4) |
| 7 | **MSFT** | 558.26 | - | **-** | 20 | - | POS +$1.0B | - | 550 | 535 | -$18.3M | +$0 bull / -$320k bear | out (clean 29, ADX 21, RVol 1.2) |
| 8 | **TSLA** | 386.34 | - | **-** | 19 | - | NEG -$94.5M | 391.91 | 400 | 380 | -$73.0M | +$415k bull / +$0 bear | out (clean 31, ADX 17, RVol 0.5) |
| 9 | **AMD** | 482.10 | - | **-** | 19 | - | NEG -$90.3M | - | 500 | 440 | +$49.7M | +$260k bull / -$473k bear | out (clean 31, ADX 15, RVol 0.6) |
| 10 | **AVGO** | 325.54 | - | **-** | 19 | - | NEG -$107.4M | - | 340 | 320 | +$5.9M | +$27k bull / +$0 bear | out (clean 29, ADX 22, RVol 0.6) |
| 11 | **NVDA** | 202.12 | - | **-** | 18 | - | NEG -$122.5M | 203.37 | 210 | 200 | +$11.4M | +$460k bull / +$0 bear | out (clean 30, ADX 20, RVol 1.2) |
| 12 | **META** | 629.50 | - | **-** | 18 | - | POS +$149.9M | 621.89 | 650 | 625 | +$10.8M | +$57k bull / -$472k bear | out (clean 32, ADX 26, RVol 0.6) |
| 13 | **SMCI** | 29.57 | - | **-** | 18 | - | NEG -$1.8M | - | 32 | 30 | +$2.1M | - | out (clean 34, ADX 29, RVol 1.0) |
| 14 | **AMZN** | 267.64 | - | **-** | 17 | - | POS +$564.5M | - | 270 | 250 | -$16.8M | +$130k bull / +$0 bear | out (clean 36, ADX 14, RVol 0.6) |
| 15 | **DELL** | 367.86 | - | **-** | 17 | - | NEG -$29.1M | - | 400 | 400 | +$754k | +$36k bull / +$0 bear | out (clean 33, ADX 26, RVol 0.8) |
| 16 | **SPY** | 767.36 | - | **-** | 16 | - | NEG -$3.7B | 769.44 | 770 | 767 | -$86.5M | +$665k bull / +$0 bear | out (clean 32, ADX 16, RVol 0.7) |
| 17 | **QQQ** | 692.27 | - | **-** | 16 | - | NEG -$5.2B | 715.58 | 700 | 680 | -$78.2M | +$964k bull / -$583k bear | out (clean 32, ADX 19, RVol 0.5) |
| 18 | **IWM** | 283.57 | - | **-** | 16 | - | NEG -$277.8M | 284.2 | 285 | 270 | +$9.0M | +$65k bull / -$699k bear | out (clean 35, ADX 15, RVol 0.3) |
| 19 | **HOOD** | 87.30 | - | **-** | 15 | - | POS +$9.7M | 82.52 | 90 | 90 | -$736k | +$0 bull / -$31k bear | out (clean 29, ADX 13, RVol 0.7) |
| 20 | **NFLX** | 66.56 | - | **-** | 14 | - | POS +$22.3M | - | 65 | 65 | -$2.0M | - | out (clean 32, ADX 30, RVol 1.1) |
| 21 | **ORCL** | 124.69 | - | **-** | 14 | - | NEG -$34.7M | - | 130 | 125 | +$3.6M | - | out (clean 33, ADX 27, RVol 1.8) |
| 22 | **PLTR** | 171.40 | - | **-** | 13 | - | NEG -$48.4M | - | 165 | 170 | -$1.0M | +$0 bull / -$294k bear | out (clean 26, ADX 10, RVol 0.4) |
| 23 | **SHOP** | 152.95 | - | **-** | 12 | - | NEG -$4.0M | 158.47 | 160 | 150 | -$403k | - | out (clean 33, ADX 20, RVol 0.5) |
| 24 | **GOOGL** | 291.16 | - | **-** | 11 | - | POS +$112.0M | 282.71 | 290 | 290 | -$26.2M | - | out (clean 36, ADX 10, RVol 0.3) |
| 25 | **COIN** | 151.50 | - | **-** | 9 | - | POS +$31.9M | - | 148 | 150 | -$1.2M | - | out (clean 31, ADX 11, RVol 0.3) |
| 26 | **CRM** | 227.82 | - | **-** | 8 | - | NEG -$10.4M | 237.71 | 240 | 220 | -$189k | - | out (clean 34, ADX 18, RVol 0.4) |
| 27 | **BABA** | 105.98 | - | **-** | 7 | - | POS +$17.0M | - | 105 | 110 | -$188k | - | out (clean 36, ADX 24, RVol 0.7) |

## Big prints this scan (50)
- **QQQ** PUT 695 2026-11-04 (0DTE): 999 @ 2.60 = **+$260k** SELL | vol 241,939 / OI 1,605
- **QQQ** PUT 700 2026-11-04 (0DTE): 240 @ 7.58 = **+$182k** BUY | vol 43,604 / OI 3,668
- **SPY** PUT 763 2026-11-06 (2DTE): 1,000 @ 1.79 = **+$179k** SELL | vol 8,425 / OI 2,747
- **QQQ** PUT 720 2026-11-11 (7DTE): 55 @ 27.56 = **+$152k** SELL | vol 62 / OI 93
- **QQQ** PUT 720 2026-11-09 (5DTE): 55 @ 27.34 = **+$150k** SELL | vol 1,210 / OI 2,092
- **QQQ** PUT 718 2026-11-10 (6DTE): 50 @ 25.76 = **+$129k** BUY | vol 53 / OI 0
- **QQQ** PUT 718 2026-11-09 (5DTE): 50 @ 25.64 = **+$128k** BUY | vol 112 / OI 0
- **IWM** CALL 284 2026-11-05 (1DTE): 1,499 @ 0.85 = **+$127k** SELL | vol 18,732 / OI 505
- **IWM** CALL 284 2026-11-05 (1DTE): 1,488 @ 0.85 = **+$126k** SELL | vol 18,732 / OI 505
- **MU** PUT 835 2026-11-04 (0DTE): 32 @ 36.50 = **+$117k** SELL | vol 5,524 / OI 535
- **MU** PUT 795 2026-11-11 (7DTE): 41 @ 26.15 = **+$107k** MID | vol 228 / OI 14
- **TSLA** PUT 390 2026-11-06 (2DTE): 148 @ 7.20 = **+$107k** SELL | vol 13,424 / OI 4,169
- **MU** PUT 795 2026-11-11 (7DTE): 40 @ 26.15 = **+$105k** MID | vol 228 / OI 14
- **MU** PUT 795 2026-11-11 (7DTE): 39 @ 26.15 = **+$102k** MID | vol 228 / OI 14
- **MSFT** CALL 555 2026-11-04 (0DTE): 300 @ 3.37 = **+$101k** SELL | vol 27,133 / OI 251

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 771 2026-12-04 (30DTE): 511 traded vs OI 226
- **QQQ** PUT 659 2026-11-05 (1DTE): 1,184 traded vs OI 0
- **QQQ** CALL 714 2026-11-06 (2DTE): 3,349 traded vs OI 3,321
- **QQQ** PUT 656 2026-11-05 (1DTE): 1,999 traded vs OI 0
- **QQQ** PUT 658 2026-11-05 (1DTE): 519 traded vs OI 0
- **QQQ** PUT 655 2026-11-05 (1DTE): 2,084 traded vs OI 1,103
- **SMH** CALL 507.5 2026-11-06 (2DTE): 500 traded vs OI 52
- **TSLA** PUT 357.5 2026-11-06 (2DTE): 1,078 traded vs OI 1,076
- **TSLA** CALL 410 2026-11-13 (9DTE): 1,747 traded vs OI 1,746
- **AAPL** PUT 345 2026-11-11 (7DTE): 512 traded vs OI 252
- **AAPL** PUT 330 2026-12-04 (30DTE): 950 traded vs OI 304
- **AMD** PUT 485 2026-11-13 (9DTE): 503 traded vs OI 315
- **NFLX** CALL 69 2026-11-13 (9DTE): 1,502 traded vs OI 1,463
- **NFLX** CALL 70 2026-11-13 (9DTE): 3,353 traded vs OI 3,283
- **MSTR** PUT 129 2026-11-06 (2DTE): 667 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
