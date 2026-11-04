# GEX + FLOW SCAN - Wed Nov 04, 01:05 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (10)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 13:05 | **AAPL** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/04 352.5P | 0.58 | 0.51 | -12% (0m) | **-12%** | +57% | 352.38 |
| 12:50 | **AMZN** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/04 267.5P | 0.40 | 0.31 | +17% (7m) | **-23%** | +109% | 267.48 |
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
Last 1m check 13:05:08 ET, last candle SPY 13:04, QQQ 13:04 | no errors
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
| 1 | **AMZN** | 269.69 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 48 | none: 84 puts 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (38 contracts' greeks worked out here) | POS +$553.4M | - | 270 | 250 | -$21.9M | +$44k bull / -$631k bear | LONG (clean 35, ADX 35, RVol 1.3) |
| 2 | **AAPL** | 354.30 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 47 | 11/04 352.5P @ 0.58 (delta 0.28) = est +57% at 352.38 | POS +$1.1B | 342.29 | 355 | 350 | -$81.8M | +$0 bull / -$324k bear | out (clean 32, ADX 42, RVol 0.6) |
| 3 | **SMH** | 507.19 | FLOW SURGE | **CALLS** | 36 | none: 160 calls 0-7DTE > 8 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (64 contracts' greeks worked out here) | NEG -$528.2M | - | 532.5 | 500 | +$20.9M | +$56k bull / +$0 bear | out (clean 32, ADX 14, RVol 0.6) |
| 4 | **GOOGL** | 292.50 | - | **-** | 24 | - | POS +$101.8M | 283.07 | 290 | 290 | -$27.4M | +$0 bull / -$48k bear | out (clean 36, ADX 20, RVol 0.4) |
| 5 | **MSFT** | 553.54 | - | **-** | 23 | - | POS +$1.0B | - | 550 | 535 | -$15.6M | +$433k bull / +$0 bear | out (clean 29, ADX 40, RVol 1.2) |
| 6 | **TSLA** | 390.82 | - | **-** | 22 | - | NEG -$71.1M | 394.94 | 400 | 390 | -$89.6M | +$0 bull / -$2.4M bear | out (clean 31, ADX 21, RVol 0.6) |
| 7 | **MU** | 809.96 | - | **-** | 20 | - | NEG -$372.4M | - | 850 | 800 | +$98.8M | +$387k bull / -$995k bear | out (clean 32, ADX 20, RVol 0.5) |
| 8 | **MSTR** | 145.52 | - | **-** | 20 | - | POS +$120.6M | - | 135 | 150 | -$4.1M | +$0 bull / -$7.7M bear | out (clean 31, ADX 33, RVol 0.2) |
| 9 | **SPY** | 768.85 | - | **-** | 19 | - | NEG -$1.6B | 769.97 | 770 | 750 | -$134.5M | +$0 bull / -$3.0M bear | out (clean 32, ADX 27, RVol 0.5) |
| 10 | **IWM** | 284.15 | - | **-** | 19 | - | NEG -$106.6M | 284.52 | 285 | 270 | +$8.7M | +$0 bull / -$61k bear | out (clean 34, ADX 18, RVol 1.3) |
| 11 | **SMCI** | 30.14 | - | **-** | 19 | - | NEG -$570k | - | 33 | 30 | +$1.9M | - | out (clean 33, ADX 29, RVol 1.1) |
| 12 | **AMD** | 486.16 | - | **-** | 18 | - | NEG -$87.5M | - | 500 | 500 | +$43.5M | +$35k bull / -$128k bear | out (clean 32, ADX 8, RVol 0.5) |
| 13 | **QQQ** | 696.08 | - | **-** | 17 | - | NEG -$4.5B | 718.33 | 700 | 680 | -$146.4M | +$105k bull / -$300k bear | out (clean 32, ADX 13, RVol 0.6) |
| 14 | **NVDA** | 203.56 | - | **-** | 16 | - | NEG -$34.4M | 204.01 | 210 | 200 | -$442k | +$0 bull / -$720k bear | out (clean 30, ADX 20, RVol 1.0) |
| 15 | **META** | 639.86 | - | **-** | 16 | - | POS +$265.2M | 620.09 | 650 | 625 | +$140k | +$728k bull / +$0 bear | out (clean 31, ADX 26, RVol 0.7) |
| 16 | **AVGO** | 328.89 | - | **-** | 16 | - | NEG -$84.5M | - | 340 | 330 | +$1.9M | +$0 bull / -$68k bear | out (clean 30, ADX 16, RVol 0.8) |
| 17 | **PLTR** | 170.59 | - | **-** | 16 | - | NEG -$50.3M | - | 165 | 170 | -$1.3M | +$0 bull / -$46k bear | out (clean 26, ADX 23, RVol 0.5) |
| 18 | **UBER** | 71.22 | - | **-** | 15 | - | POS +$12.3M | 68.28 | 70 | 70 | -$1.1M | - | out (clean 30, ADX 28, RVol 0.9) |
| 19 | **NFLX** | 66.21 | - | **-** | 14 | - | POS +$19.5M | 62.36 | 65 | 65 | -$2.0M | - | out (clean 31, ADX 33, RVol 1.0) |
| 20 | **BABA** | 106.83 | - | **-** | 14 | - | POS +$17.0M | - | 110 | 110 | -$801k | - | out (clean 36, ADX 29, RVol 0.8) |
| 21 | **SHOP** | 151.57 | - | **-** | 12 | - | NEG -$5.6M | - | 160 | 150 | -$357k | - | out (clean 33, ADX 21, RVol 0.3) |
| 22 | **COIN** | 152.86 | - | **-** | 11 | - | POS +$27.4M | - | 148 | 150 | -$1.3M | - | out (clean 31, ADX 19, RVol 0.2) |
| 23 | **ARM** | 192.23 | - | **-** | 9 | - | NEG -$6.9M | - | 200 | 200 | +$738k | - | out (clean 26, ADX 19, RVol 0.5) |
| 24 | **CRM** | 226.30 | - | **-** | 9 | - | NEG -$13.5M | - | 240 | 220 | -$122k | - | out (clean 33, ADX 28, RVol 0.4) |
| 25 | **ORCL** | 126.29 | - | **-** | 8 | - | NEG -$30.2M | - | 130 | 125 | +$2.4M | - | out (clean 34, ADX 9, RVol 1.1) |
| 26 | **DELL** | 374.44 | - | **-** | 7 | - | NEG -$30.6M | - | 400 | 400 | +$1.3M | - | out (clean 33, ADX 19, RVol 0.6) |
| 27 | **HOOD** | 88.62 | - | **-** | 6 | - | POS +$3.3M | 84.54 | 90 | 90 | -$1.0M | - | out (clean 28, ADX 21, RVol 0.5) |

## Big prints this scan (68)
- **MSTR** CALL 139 2026-11-06 (2DTE): 2,519 @ 7.80 = **+$2.0M** SELL | vol 6,379 / OI 19,575
- **MSTR** CALL 146 2026-11-06 (2DTE): 4,697 @ 3.61 = **+$1.7M** SELL | vol 11,857 / OI 17,342
- **MSTR** CALL 139 2026-11-06 (2DTE): 1,680 @ 7.80 = **+$1.3M** SELL | vol 6,379 / OI 19,575
- **MSTR** CALL 150 2026-11-06 (2DTE): 4,697 @ 2.15 = **+$1.0M** SELL | vol 13,554 / OI 4,831
- **MSTR** CALL 146 2026-11-06 (2DTE): 2,519 @ 3.65 = **+$919k** SELL | vol 11,857 / OI 17,342
- **MSTR** CALL 146 2026-11-06 (2DTE): 1,680 @ 3.65 = **+$613k** SELL | vol 11,857 / OI 17,342
- **AMZN** CALL 270 2026-11-06 (2DTE): 525 @ 3.10 = **+$163k** SELL | vol 36,149 / OI 13,073
- **AMZN** CALL 270 2026-11-06 (2DTE): 450 @ 3.10 = **+$140k** SELL | vol 36,149 / OI 13,073
- **TSLA** PUT 400 2026-11-06 (2DTE): 100 @ 13.00 = **+$130k** BUY | vol 2,231 / OI 5,459
- **TSLA** PUT 400 2026-11-04 (0DTE): 120 @ 10.50 = **+$126k** BUY | vol 1,332 / OI 3,748
- **QQQ** PUT 706 2026-11-05 (1DTE): 100 @ 10.50 = **+$105k** SELL | vol 291 / OI 0
- **MSTR** CALL 146 2026-11-06 (2DTE): 282 @ 3.62 = **+$102k** SELL | vol 11,857 / OI 17,342
- **TSLA** PUT 390 2026-11-06 (2DTE): 139 @ 6.75 = **+$94k** BUY | vol 5,934 / OI 4,169
- **META** CALL 637.5 2026-11-04 (0DTE): 200 @ 4.65 = **+$93k** BUY | vol 15,259 / OI 366
- **NVDA** PUT 202.5 2026-11-06 (2DTE): 241 @ 3.05 = **+$74k** BUY | vol 22,620 / OI 4,698

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 761 2026-11-09 (5DTE): 505 traded vs OI 0
- **SPY** PUT 745 2026-11-09 (5DTE): 6,664 traded vs OI 6,652
- **SPY** PUT 700 2026-12-04 (30DTE): 583 traded vs OI 570
- **QQQ** CALL 693 2026-11-09 (5DTE): 519 traded vs OI 0
- **QQQ** PUT 690 2026-11-06 (2DTE): 14,110 traded vs OI 13,671
- **QQQ** PUT 672 2026-11-13 (9DTE): 639 traded vs OI 0
- **IWM** PUT 272 2026-12-04 (30DTE): 3,239 traded vs OI 329
- **IWM** PUT 262 2026-12-04 (30DTE): 3,005 traded vs OI 464
- **NVDA** PUT 200 2026-11-06 (2DTE): 21,388 traded vs OI 20,851
- **NVDA** CALL 200 2026-11-09 (5DTE): 502 traded vs OI 186
- **TSLA** CALL 410 2026-11-11 (7DTE): 639 traded vs OI 633
- **AAPL** CALL 355 2026-12-04 (30DTE): 503 traded vs OI 287
- **META** CALL 635 2026-11-09 (5DTE): 537 traded vs OI 58
- **META** CALL 680 2026-11-06 (2DTE): 1,362 traded vs OI 1,227
- **AMZN** PUT 247.5 2026-11-06 (2DTE): 1,444 traded vs OI 1,296

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
