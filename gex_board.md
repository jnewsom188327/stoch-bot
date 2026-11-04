# GEX + FLOW SCAN - Wed Nov 04, 11:10 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (6)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:20 | **SMCI** | **CALLS** | FLOW SURGE | 11/06 33C | 0.65 | 0.12 | -3% (1m) | **-82%** | +39% | 32.81 |
| 10:20 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/04 284C | 0.49 | 0.23 | +2% (22m) | **-53%** | +131% | 284.74 |
| 10:00 | **AMZN** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/04 267.5P | 0.68 | 1.54 | +169% (60m) | **+126%** (done) | +258% | 265.7 |
| 09:50 | **UBER** | **CALLS** | FLIP CROSS up into positive gamma | 11/06 71C | 0.60 | 1.56 | +168% (52m) | **+160%** (done) | +50% | 70 hit |
| 09:50 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/04 286C | 0.53 | 0.06 | +2% (1m) | **-89%** (done) | +150% | 287 |
| 09:45 | **UBER** | **PUTS** | FLIP CROSS down into negative gamma | 11/06 67P | 0.63 | 0.10 | -3% (1m) | **-84%** (done) | +27% | 68.03 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 11:10:08 ET, last candle SPY 11:09, QQQ 11:09 | no errors

## Flow surges NOT fired - price disagreed (28 today, last 5)
- 10:50 SMCI CALLS: price -1.23 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:50 AAPL PUTS: over EMA 20 - flow says one way, price says the other
- 10:45 AAPL PUTS: price +0.02 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:40 AAPL PUTS: price +1.07 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:35 GOOGL PUTS: over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **SMH** | 501.85 | FLOW SURGE | **CALLS** | 57 | none: 154 calls 0-7DTE > 8 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (71 contracts' greeks worked out here) | NEG -$530.4M | - | 532.5 | 500 | +$5.6M | +$555k bull / +$0 bear | out (clean 32, ADX 38, RVol 4.0) |
| 2 | **SMCI** | 29.98 | TREND (flow not with it) | **PUTS** | 56 | 11/06 29P @ 0.56 (delta 0.31) = est +58% at 28.98 | NEG -$844k | - | 32 | 30 | +$1.7M | - | SHORT (clean 33, ADX 40, RVol 4.2) |
| 3 | **MU** | 799.01 | FLOW SURGE | **CALLS** | 53 | none: 136 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (63 contracts' greeks worked out here) | NEG -$336.8M | - | 850 | 800 | +$127.5M | +$12.9M bull / +$0 bear | out (clean 31, ADX 35, RVol 2.4) |
| 4 | **BABA** | 107.33 | TREND (flow not with it) | **CALLS** | 52 | 11/06 111C @ 0.63 (delta 0.23) = est +26% at 108.38 | POS +$16.4M | - | 110 | 110 | -$1.1M | - | LONG (clean 36, ADX 66, RVol 2.3) |
| 5 | **AMZN** | 266.51 | TREND (flow not with it) | **CALLS** | 50 | none: 88 calls 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (42 contracts' greeks worked out here) | POS +$533.0M | - | 270 | 250 | -$19.3M | +$1.5M bull / +$0 bear | LONG (clean 35, ADX 52, RVol 1.8) |
| 6 | **COIN** | 150.18 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 41 | none: 21 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (1 contracts' greeks worked out here) | POS +$29.4M | - | 148 | 150 | -$1.2M | +$0 bull / -$28k bear | out (clean 31, ADX 15, RVol 0.7) |
| 7 | **AAPL** | 352.57 | - | **-** | 35 | - | POS +$927.1M | 341.31 | 355 | 350 | -$82.1M | +$813k bull / -$722k bear | out (clean 32, ADX 60, RVol 1.9) |
| 8 | **GOOGL** | 292.92 | - | **-** | 32 | - | POS +$105.7M | 282.58 | 300 | 290 | -$29.0M | +$115k bull / -$62k bear | out (clean 35, ADX 52, RVol 0.8) |
| 9 | **UBER** | 72.32 | - | **-** | 28 | - | POS +$15.8M | - | 75 | 70 | -$1.6M | - | out (clean 31, ADX 66, RVol 2.1) |
| 10 | **MSFT** | 552.27 | - | **-** | 27 | - | POS +$1.0B | - | 550 | 535 | -$13.9M | +$990k bull / -$819k bear | out (clean 29, ADX 66, RVol 1.8) |
| 11 | **AVGO** | 324.29 | - | **-** | 26 | - | NEG -$102.9M | - | 340 | 320 | +$4.2M | +$514k bull / +$0 bear | out (clean 30, ADX 35, RVol 1.7) |
| 12 | **AMD** | 483.87 | - | **-** | 25 | - | NEG -$85.2M | - | 500 | 440 | +$45.2M | +$1.5M bull / -$1.1M bear | out (clean 33, ADX 22, RVol 1.8) |
| 13 | **SHOP** | 151.57 | - | **-** | 25 | - | NEG -$5.0M | - | 160 | 150 | -$271k | +$0 bull / -$138k bear | out (clean 35, ADX 28, RVol 0.8) |
| 14 | **NVDA** | 202.68 | - | **-** | 24 | - | NEG -$57.7M | 203.68 | 210 | 200 | +$5.6M | +$1.1M bull / -$237k bear | out (clean 30, ADX 39, RVol 2.5) |
| 15 | **TSLA** | 384.46 | - | **-** | 24 | - | NEG -$128.8M | 394.67 | 400 | 380 | -$59.0M | +$4.4M bull / +$0 bear | out (clean 30, ADX 22, RVol 1.7) |
| 16 | **ARM** | 193.75 | - | **-** | 24 | - | NEG -$6.4M | - | 200 | 200 | +$842k | - | out (clean 26, ADX 36, RVol 0.8) |
| 17 | **SPY** | 765.49 | - | **-** | 23 | - | NEG -$4.3B | 770.07 | 770 | 750 | -$72.6M | +$2.0M bull / -$722k bear | out (clean 32, ADX 37, RVol 1.6) |
| 18 | **META** | 630.87 | - | **-** | 21 | - | POS +$159.6M | 619.98 | 650 | 625 | +$6.9M | +$234k bull / -$429k bear | out (clean 30, ADX 40, RVol 0.9) |
| 19 | **NFLX** | 66.32 | - | **-** | 21 | - | POS +$19.0M | - | 65 | 65 | -$2.4M | - | out (clean 31, ADX 70, RVol 1.5) |
| 20 | **MSTR** | 143.58 | - | **-** | 21 | - | POS +$116.7M | - | 135 | 150 | -$44k | +$212k bull / -$385k bear | out (clean 31, ADX 45, RVol 1.3) |
| 21 | **QQQ** | 692.30 | - | **-** | 19 | - | NEG -$5.1B | 719.71 | 700 | 680 | -$63.4M | +$14.9M bull / -$4.0M bear | out (clean 31, ADX 26, RVol 1.2) |
| 22 | **ORCL** | 126.56 | - | **-** | 18 | - | NEG -$29.0M | - | 130 | 125 | +$227k | +$35k bull / -$26k bear | out (clean 35, ADX 15, RVol 2.2) |
| 23 | **PLTR** | 174.30 | - | **-** | 17 | - | NEG -$43.7M | - | 180 | 170 | -$1.4M | +$181k bull / -$305k bear | out (clean 26, ADX 16, RVol 1.1) |
| 24 | **HOOD** | 86.68 | - | **-** | 17 | - | POS +$1.6M | 85.47 | 90 | 90 | -$1.0M | +$39k bull / -$27k bear | out (clean 28, ADX 15, RVol 0.9) |
| 25 | **CRM** | 229.90 | - | **-** | 17 | - | NEG -$8.2M | 237.99 | 240 | 220 | -$228k | - | out (clean 31, ADX 52, RVol 0.9) |
| 26 | **DELL** | 372.65 | - | **-** | 16 | - | NEG -$28.4M | - | 400 | 400 | +$1.5M | - | out (clean 32, ADX 39, RVol 2.6) |
| 27 | **IWM** | 282.23 | - | **-** | 13 | - | NEG -$702.4M | 284.53 | 285 | 270 | +$15.2M | - | out (clean 34, ADX 19, RVol 1.1) |

## Big prints this scan (155)
- **QQQ** PUT 693 2026-11-06 (2DTE): 5,000 @ 6.69 = **+$3.3M** BUY | vol 6,143 / OI 20,503
- **QQQ** PUT 691 2026-11-06 (2DTE): 5,000 @ 5.88 = **+$2.9M** MID | vol 5,688 / OI 17,537
- **QQQ** PUT 693 2026-11-04 (0DTE): 1,081 @ 3.38 = **+$365k** BUY | vol 57,727 / OI 528
- **AMD** CALL 480 2026-11-04 (0DTE): 500 @ 7.00 = **+$350k** SELL | vol 2,254 / OI 253
- **SPY** PUT 768 2026-11-04 (0DTE): 600 @ 3.16 = **+$190k** BUY | vol 62,688 / OI 1,133
- **SPY** PUT 768 2026-11-04 (0DTE): 560 @ 3.23 = **+$181k** BUY | vol 62,688 / OI 1,133
- **TSLA** PUT 385 2026-11-09 (5DTE): 250 @ 7.15 = **+$179k** SELL | vol 2,936 / OI 308
- **TSLA** PUT 385 2026-11-09 (5DTE): 250 @ 7.00 = **+$175k** SELL | vol 2,936 / OI 308
- **MSFT** CALL 557.5 2026-11-06 (2DTE): 408 @ 4.17 = **+$170k** SELL | vol 7,592 / OI 6,272
- **TSLA** PUT 385 2026-11-09 (5DTE): 235 @ 7.00 = **+$164k** SELL | vol 2,936 / OI 308
- **MU** CALL 800 2026-11-06 (2DTE): 67 @ 23.60 = **+$158k** BUY | vol 597 / OI 342
- **SPY** PUT 768 2026-11-04 (0DTE): 500 @ 3.04 = **+$152k** SELL | vol 62,688 / OI 1,133
- **QQQ** PUT 693 2026-11-04 (0DTE): 480 @ 2.89 = **+$139k** BUY | vol 57,727 / OI 528
- **QQQ** PUT 698 2026-11-04 (0DTE): 246 @ 5.62 = **+$138k** SELL | vol 48,467 / OI 420
- **MSFT** CALL 557.5 2026-11-06 (2DTE): 337 @ 4.00 = **+$135k** SELL | vol 7,592 / OI 6,272

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 751 2026-11-09 (5DTE): 512 traded vs OI 0
- **SPY** PUT 744 2026-11-09 (5DTE): 523 traded vs OI 0
- **SPY** CALL 761 2026-11-05 (1DTE): 512 traded vs OI 0
- **SPY** PUT 760 2026-11-09 (5DTE): 2,091 traded vs OI 2,023
- **SPY** PUT 764 2026-11-09 (5DTE): 526 traded vs OI 0
- **SPY** PUT 752 2026-11-09 (5DTE): 532 traded vs OI 0
- **SPY** PUT 764 2026-11-11 (7DTE): 513 traded vs OI 0
- **SPY** CALL 768 2026-12-04 (30DTE): 588 traded vs OI 239
- **QQQ** PUT 671 2026-11-05 (1DTE): 540 traded vs OI 0
- **QQQ** PUT 688 2026-11-06 (2DTE): 2,249 traded vs OI 1,689
- **QQQ** CALL 683 2026-11-04 (0DTE): 510 traded vs OI 285
- **QQQ** PUT 674 2026-11-05 (1DTE): 568 traded vs OI 0
- **QQQ** PUT 707 2026-11-04 (0DTE): 507 traded vs OI 163
- **QQQ** CALL 684 2026-11-04 (0DTE): 783 traded vs OI 738
- **QQQ** PUT 673 2026-11-05 (1DTE): 500 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
