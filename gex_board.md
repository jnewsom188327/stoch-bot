# GEX + FLOW SCAN - Fri Nov 13, 11:10 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (9)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:36 | **SPY** | **PUTS** | 1m FAILED POP (R3 R4) | 11/13 743P | 0.61 | 0.31 | +13% (1m) | **-49%** | +46% | 747.53 |
| 10:17 | **QQQ** | **CALLS** | 1m WHIPSAW (R1 R2) | 11/13 683C | 0.75 | 0.28 | -1% (0m) | **-63%** | +60% | 678.58 |
| 10:15 | **ARM** | **PUTS** | FLIP CROSS down into negative gamma | 11/13 182.5P | 0.74 | 1.13 | +169% (50m) | **+53%** | +96% | 183.6 hit |
| 10:15 | **ORCL** | **CALLS** | FLIP CROSS up into positive gamma | 11/13 124C | 0.65 | 0.59 | +89% (28m) | **-9%** | +66% | 123.68 hit |
| 10:10 | **ORCL** | **PUTS** | FLIP CROSS down into negative gamma | 11/13 120P | 0.46 | 0.15 | +7% (5m) | **-67%** | +63% | 121.25 |
| 10:05 | **GOOGL** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/13 297.5P | 0.74 | 3.42 | +396% (33m) | **+362%** (done) | +288% | 295 hit |
| 09:55 | **BABA** | **PUTS** | FLOW SURGE | 11/13 94P | 0.51 | 0.43 | +8% (43m) | **-16%** (done) | +49% | 93.36 |
| 09:45 | **UBER** | **CALLS** | TREND + FLOW | 11/13 70C | 0.59 | 0.06 | +0% (1m) | **-90%** (done) | +32% | 70.7 |
| 09:45 | **ORCL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/13 127C | 0.46 | 0.22 | +22% (2m) | **-52%** (done) | +48% | 126.38 |

## 1m RULES on SPY / QQQ - loose (3 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 11:10:08 ET, last candle SPY 11:09, QQQ 11:09 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 11:02 | QQQ | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |
| 10:35 | SPY | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | **FIRE** SPY261113P00743000 |
| 10:16 | QQQ | 1m WHIPSAW | R1 R2 | CALLS | TURNING your way | **FIRE** QQQ261113C00683000 |

## Flow surges NOT fired - price disagreed (40 today, last 5)
- 11:10 COIN CALLS: under EMA 20 - flow says one way, price says the other
- 11:05 COIN CALLS: price -0.05 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:55 GOOGL CALLS: under EMA 20 - flow says one way, price says the other
- 10:50 GOOGL CALLS: price -0.27 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:45 HOOD CALLS: price -0.17 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **AVGO** | 339.56 | PINNED between the walls (positive gamma) - chop | **-** | 51 | - | POS +$61.4M | - | 340 | 340 | +$23.2M | +$531k bull / +$0 bear | SHORT (clean 36, ADX 51, RVol 0.7) |
| 2 | **COIN** | 127.45 | FLOW SURGE | **CALLS** | 51 | 11/13 129C @ 0.60 (delta 0.30) = est +144% at 130 | NEG -$20.9M | 132.92 | 140 | 130 | +$3.4M | +$107k bull / +$0 bear | out (clean 31, ADX 44, RVol 1.5) |
| 3 | **ARM** | 184.84 | RUN: clean trend + negative gamma + flow agrees | **PUTS** | 49 | none: 30 puts 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (24 contracts' greeks worked out here) | NEG -$2.7M | 189.36 | 185 | 190 | -$170k | - | SHORT (clean 33, ADX 60, RVol 1.0) |
| 4 | **DELL** | 340.50 | FLOW SURGE | **CALLS** | 45 | none: 54 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (46 contracts' greeks worked out here) | NEG -$9.1M | - | 350 | 340 | +$8.1M | +$35k bull / +$0 bear | out (clean 38, ADX 48, RVol 0.7) |
| 5 | **TSLA** | 390.29 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 39 | 11/13 395C @ 0.80 (delta 0.22) = est +522% at 400 | POS +$336.4M | 380.15 | 400 | 390 | +$48.7M | +$198k bull / -$4.8M bear | out (clean 30, ADX 18, RVol 0.6) |
| 6 | **NVDA** | 159.66 | FLOW SURGE | **CALLS** | 38 | 11/13 162.5C @ 0.48 (delta 0.22) = est +156% at 162.59 | NEG -$286.6M | - | 175 | 160 | +$116.4M | +$3.6M bull / -$346k bear | out (clean 31, ADX 21, RVol 0.8) |
| 7 | **AMD** | 528.61 | TREND (flow not with it) | **PUTS** | 33 | none: 168 puts 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (79 contracts' greeks worked out here) | POS +$51.1M | - | 550 | 530 | +$70.6M | +$2.3M bull / -$808k bear | SHORT (clean 35, ADX 51, RVol 0.7) |
| 8 | **GOOGL** | 295.27 | - | **-** | 33 | - | POS +$181.3M | 288.9 | 300 | 290 | +$19.3M | +$25k bull / -$28k bear | out (clean 32, ADX 32, RVol 1.2) |
| 9 | **SMH** | 476.75 | - | **-** | 31 | - | NEG -$323.8M | - | 500 | 475 | +$13.1M | +$871k bull / +$0 bear | out (clean 31, ADX 56, RVol 1.5) |
| 10 | **QQQ** | 674.67 | - | **-** | 29 | - | NEG -$3.1B | 690.76 | 680 | 680 | +$314.0M | +$1.7M bull / -$1.6M bear | out (clean 32, ADX 57, RVol 0.6) |
| 11 | **IWM** | 276.05 | - | **-** | 29 | - | NEG -$2.8B | 283.12 | 285 | 275 | +$21.4M | +$2.0M bull / -$408k bear | out (clean 36, ADX 44, RVol 0.7) |
| 12 | **AMZN** | 265.87 | - | **-** | 28 | - | POS +$425.9M | 253.13 | 265 | 265 | +$7.9M | +$0 bull / -$25k bear | out (clean 30, ADX 35, RVol 0.6) |
| 13 | **MU** | 758.29 | - | **-** | 26 | - | NEG -$23.1M | 770.75 | 760 | 750 | +$76.1M | +$3.1M bull / -$964k bear | out (clean 31, ADX 38, RVol 1.1) |
| 14 | **SPY** | 750.82 | - | **-** | 24 | - | NEG -$8.9B | 760.48 | 750 | 750 | +$246.6M | +$1.7M bull / -$797k bear | out (clean 33, ADX 34, RVol 0.6) |
| 15 | **MSTR** | 110.39 | - | **-** | 24 | - | NEG -$45.7M | - | 110 | 110 | +$4.2M | +$230k bull / -$182k bear | out (clean 31, ADX 36, RVol 0.7) |
| 16 | **AAPL** | 357.92 | - | **-** | 21 | - | POS +$1.2B | 348.1 | 360 | 360 | +$10.3M | +$593k bull / -$150k bear | out (clean 30, ADX 26, RVol 0.8) |
| 17 | **ORCL** | 123.22 | - | **-** | 21 | - | POS +$3.5M | 122.29 | 125 | 125 | -$684k | +$216k bull / +$0 bear | out (clean 31, ADX 36, RVol 1.3) |
| 18 | **HOOD** | 77.62 | - | **-** | 21 | - | NEG -$15.2M | 79.9 | 80 | 80 | +$2.7M | - | out (clean 36, ADX 60, RVol 1.4) |
| 19 | **META** | 631.39 | - | **-** | 19 | - | NEG -$13.7M | 632.21 | 630 | 625 | +$8.3M | +$0 bull / -$1.5M bear | out (clean 29, ADX 26, RVol 0.8) |
| 20 | **PLTR** | 167.65 | - | **-** | 19 | - | POS +$85.8M | 162.6 | 170 | 165 | +$80k | +$82k bull / -$34k bear | out (clean 29, ADX 41, RVol 0.7) |
| 21 | **MSFT** | 524.00 | - | **-** | 18 | - | POS +$126.8M | 521.07 | 530 | 520 | -$2.1M | +$246k bull / -$654k bear | out (clean 32, ADX 26, RVol 1.0) |
| 22 | **SMCI** | 26.27 | - | **-** | 18 | - | NEG -$2.5M | - | 27 | 25 | +$377k | - | out (clean 34, ADX 29, RVol 0.7) |
| 23 | **UBER** | 69.42 | - | **-** | 18 | - | POS +$11.2M | 68.95 | 70 | 70 | +$295k | - | out (clean 33, ADX 17, RVol 0.5) |
| 24 | **CRM** | 216.29 | - | **-** | 17 | - | NEG -$8.9M | 221.2 | 220 | 220 | +$152k | - | out (clean 28, ADX 19, RVol 0.5) |
| 25 | **NFLX** | 62.83 | - | **-** | 11 | - | NEG -$26.9M | 63.5 | 65 | 60 | +$357k | - | out (clean 32, ADX 32, RVol 0.8) |
| 26 | **SHOP** | 146.69 | - | **-** | 10 | - | POS +$2.9M | 145.17 | 150 | 140 | -$82k | - | out (clean 32, ADX 23, RVol 0.5) |
| 27 | **BABA** | 94.06 | - | **-** | 5 | - | NEG -$19.1M | - | 100 | 95 | -$4k | - | out (clean 28, ADX 25, RVol 0.5) |

## Big prints this scan (162)
- **TSLA** CALL 397.5 2026-11-20 (7DTE): 1,800 @ 7.40 = **+$1.3M** SELL | vol 2,596 / OI 0
- **TSLA** CALL 387.5 2026-11-16 (3DTE): 860 @ 6.55 = **+$563k** SELL | vol 2,251 / OI 346
- **META** CALL 640 2026-11-20 (7DTE): 500 @ 10.91 = **+$546k** SELL | vol 2,104 / OI 4,178
- **SMH** CALL 500 2026-11-20 (7DTE): 749 @ 6.75 = **+$506k** BUY | vol 2,036 / OI 3,710
- **NVDA** CALL 160 2026-11-16 (3DTE): 1,154 @ 3.25 = **+$375k** BUY | vol 15,725 / OI 919
- **GOOGL** CALL 302.5 2026-11-20 (7DTE): 1,000 @ 3.22 = **+$322k** MID | vol 1,392 / OI 1,099
- **META** CALL 655 2026-11-20 (7DTE): 500 @ 6.19 = **+$310k** SELL | vol 2,282 / OI 1,391
- **IWM** PUT 270 2026-11-20 (7DTE): 2,500 @ 1.22 = **+$305k** MID | vol 23,749 / OI 136,015
- **IWM** PUT 270 2026-11-20 (7DTE): 2,500 @ 1.21 = **+$302k** MID | vol 23,749 / OI 136,015
- **QQQ** PUT 675 2026-11-20 (7DTE): 272 @ 10.97 = **+$298k** SELL | vol 4,548 / OI 31,245
- **QQQ** PUT 685 2026-11-13 (0DTE): 200 @ 9.20 = **+$184k** SELL | vol 48,151 / OI 26,536
- **NVDA** CALL 160 2026-11-16 (3DTE): 525 @ 3.45 = **+$181k** BUY | vol 15,725 / OI 919
- **META** CALL 630 2026-11-13 (0DTE): 500 @ 3.57 = **+$178k** SELL | vol 11,542 / OI 2,874
- **QQQ** PUT 683 2026-11-13 (0DTE): 200 @ 8.18 = **+$164k** SELL | vol 39,394 / OI 1,322
- **QQQ** PUT 680 2026-11-20 (7DTE): 116 @ 13.63 = **+$158k** SELL | vol 7,435 / OI 87,076

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 753 2026-11-18 (5DTE): 505 traded vs OI 371
- **SPY** PUT 730 2026-11-13 (0DTE): 24,130 traded vs OI 23,983
- **SPY** CALL 756 2026-11-18 (5DTE): 783 traded vs OI 760
- **SPY** PUT 703 2026-11-16 (3DTE): 593 traded vs OI 288
- **SPY** CALL 753 2026-11-17 (4DTE): 669 traded vs OI 644
- **SPY** CALL 741 2026-11-13 (0DTE): 659 traded vs OI 619
- **SPY** PUT 760 2026-11-17 (4DTE): 706 traded vs OI 684
- **SPY** PUT 748 2026-11-18 (5DTE): 730 traded vs OI 705
- **SPY** PUT 726 2026-11-13 (0DTE): 1,815 traded vs OI 1,705
- **SPY** CALL 795 2026-11-23 (10DTE): 812 traded vs OI 19
- **QQQ** CALL 704 2026-11-18 (5DTE): 561 traded vs OI 214
- **QQQ** CALL 706 2026-11-18 (5DTE): 1,254 traded vs OI 282
- **QQQ** PUT 634 2026-11-13 (0DTE): 579 traded vs OI 161
- **QQQ** PUT 660 2026-11-18 (5DTE): 521 traded vs OI 468
- **QQQ** CALL 676 2026-11-17 (4DTE): 502 traded vs OI 164

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
