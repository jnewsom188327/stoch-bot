# GEX + FLOW SCAN - Fri Nov 13, 10:50 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (9)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:36 | **SPY** | **PUTS** | 1m FAILED POP (R3 R4) | 11/13 743P | 0.61 | 0.32 | +13% (1m) | **-48%** | +46% | 747.53 |
| 10:17 | **QQQ** | **CALLS** | 1m WHIPSAW (R1 R2) | 11/13 683C | 0.75 | 0.44 | -1% (0m) | **-41%** | +60% | 678.58 |
| 10:15 | **ARM** | **PUTS** | FLIP CROSS down into negative gamma | 11/13 182.5P | 0.74 | 1.43 | +143% (21m) | **+93%** | +96% | 183.6 |
| 10:15 | **ORCL** | **CALLS** | FLIP CROSS up into positive gamma | 11/13 124C | 0.65 | 1.16 | +89% (28m) | **+78%** | +66% | 123.68 hit |
| 10:10 | **ORCL** | **PUTS** | FLIP CROSS down into negative gamma | 11/13 120P | 0.46 | 0.08 | +7% (5m) | **-83%** | +63% | 121.25 |
| 10:05 | **GOOGL** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/13 297.5P | 0.74 | 3.22 | +396% (33m) | **+335%** | +288% | 295 hit |
| 09:55 | **BABA** | **PUTS** | FLOW SURGE | 11/13 94P | 0.51 | 0.36 | +8% (43m) | **-29%** | +49% | 93.36 |
| 09:45 | **UBER** | **CALLS** | TREND + FLOW | 11/13 70C | 0.59 | 0.06 | +0% (1m) | **-90%** (done) | +32% | 70.7 |
| 09:45 | **ORCL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/13 127C | 0.46 | 0.22 | +22% (2m) | **-52%** (done) | +48% | 126.38 |

## 1m RULES on SPY / QQQ - loose (2 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:50:08 ET, last candle SPY 10:49, QQQ 10:49 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 10:35 | SPY | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | **FIRE** SPY261113P00743000 |
| 10:16 | QQQ | 1m WHIPSAW | R1 R2 | CALLS | TURNING your way | **FIRE** QQQ261113C00683000 |

## Flow surges NOT fired - price disagreed (40 today, last 5)
- 10:50 GOOGL CALLS: price -0.27 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:45 HOOD CALLS: price -0.17 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:45 COIN CALLS: price -0.49 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:45 GOOGL CALLS: price -1.57 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:40 MSTR CALLS: price -0.63 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **HOOD** | 77.53 | TREND (flow not with it) | **PUTS** | 54 | none: 32 puts 0-7DTE > 2 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only +5% at the target (needs +20%) (23 contracts' greeks worked out here) | NEG -$11.2M | 79.22 | 85 | 75 | +$2.7M | - | SHORT (clean 36, ADX 62, RVol 2.7) |
| 2 | **AVGO** | 340.39 | PINNED between the walls (positive gamma) - chop | **-** | 53 | - | POS +$59.9M | - | 340 | 340 | +$21.0M | +$944k bull / +$0 bear | SHORT (clean 36, ADX 47, RVol 0.9) |
| 3 | **DELL** | 341.67 | FLOW SURGE | **CALLS** | 50 | none: 56 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (48 contracts' greeks worked out here) | NEG -$5.5M | 353.16 | 350 | 340 | +$7.9M | +$88k bull / +$0 bear | SHORT (clean 38, ADX 48, RVol 0.9) |
| 4 | **AMD** | 531.43 | TREND (flow not with it) | **PUTS** | 48 | none: 168 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (77 contracts' greeks worked out here) | POS +$58.9M | - | 550 | 530 | +$66.1M | +$3.5M bull / -$4.7M bear | SHORT (clean 36, ADX 52, RVol 1.2) |
| 5 | **GOOGL** | 294.73 | FLOW SURGE | **CALLS** | 48 | 11/13 297.5C @ 0.53 (delta 0.23) = est +133% at 297.5 | POS +$169.7M | 289.54 | 300 | 290 | +$19.7M | +$2.0M bull / +$0 bear | out (clean 31, ADX 33, RVol 1.7) |
| 6 | **IWM** | 276.20 | TREND (flow not with it) | **PUTS** | 47 | 11/13 276P @ 0.72 (delta 0.46) = est +74% at 275 | NEG -$2.6B | 282.95 | 285 | 275 | +$16.0M | +$0 bull / -$747k bear | SHORT (clean 36, ADX 49, RVol 1.0) |
| 7 | **MU** | 762.28 | FLIP CROSS down into negative gamma | **PUTS** | 44 | none: 164 puts 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (85 contracts' greeks worked out here) | NEG -$19.0M | 771.77 | 800 | 750 | +$69.3M | +$4.2M bull / -$3.0M bear | out (clean 31, ADX 38, RVol 1.5) |
| 8 | **SPY** | 750.89 | TREND (flow not with it) | **PUTS** | 43 | none: 664 puts 0-7DTE > 53 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only -16% at the target (needs +20%) (252 contracts' greeks worked out here) | NEG -$8.6B | 760.98 | 750 | 750 | +$238.8M | +$232k bull / -$12.0M bear | SHORT (clean 33, ADX 38, RVol 1.0) |
| 9 | **SMH** | 477.13 | FLOW SURGE | **CALLS** | 43 | none: 141 calls 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (68 contracts' greeks worked out here) | NEG -$313.8M | - | 500 | 475 | +$12.3M | +$1.5M bull / -$839k bear | out (clean 31, ADX 55, RVol 1.0) |
| 10 | **AMZN** | 265.55 | PINNED between the walls (positive gamma) - chop | **-** | 43 | - | POS +$405.9M | 252.77 | 265 | 265 | +$8.0M | +$208k bull / +$0 bear | out (clean 30, ADX 36, RVol 0.7) |
| 11 | **ORCL** | 124.25 | FLIP CROSS down into negative gamma | **PUTS** | 41 | 11/13 123P @ 0.65 (delta 0.33) = est +105% at 122.27 | NEG -$333k | 124.25 | 125 | 125 | -$1.5M | +$0 bull / -$537k bear | out (clean 31, ADX 37, RVol 1.3) |
| 12 | **COIN** | 127.14 | - | **-** | 39 | - | NEG -$20.4M | 133.55 | 137 | 130 | +$3.5M | +$0 bull / -$49k bear | out (clean 32, ADX 49, RVol 2.4) |
| 13 | **QQQ** | 674.69 | - | **-** | 30 | - | NEG -$2.6B | 686.45 | 680 | 680 | +$310.9M | +$481k bull / -$6.8M bear | out (clean 32, ADX 58, RVol 0.9) |
| 14 | **MSTR** | 110.29 | - | **-** | 28 | - | NEG -$40.8M | - | 120 | 110 | +$4.6M | +$79k bull / +$0 bear | out (clean 31, ADX 42, RVol 1.5) |
| 15 | **NVDA** | 160.12 | - | **-** | 27 | - | NEG -$287.8M | - | 175 | 160 | +$117.4M | +$3.4M bull / -$4.6M bear | out (clean 31, ADX 18, RVol 1.1) |
| 16 | **TSLA** | 388.97 | - | **-** | 26 | - | POS +$355.0M | - | 400 | 390 | +$58.7M | +$62k bull / -$3.6M bear | out (clean 29, ADX 22, RVol 1.6) |
| 17 | **PLTR** | 167.64 | - | **-** | 24 | - | POS +$78.4M | 162.32 | 165 | 165 | +$940k | +$0 bull / -$1.3M bear | out (clean 29, ADX 46, RVol 1.7) |
| 18 | **META** | 628.58 | - | **-** | 22 | - | NEG -$62.8M | 631.92 | 630 | 625 | +$10.5M | +$1.6M bull / -$804k bear | out (clean 29, ADX 29, RVol 1.6) |
| 19 | **MSFT** | 524.57 | - | **-** | 22 | - | POS +$134.7M | 521.38 | 530 | 520 | -$3.6M | +$0 bull / -$1.1M bear | out (clean 32, ADX 32, RVol 1.5) |
| 20 | **AAPL** | 359.05 | - | **-** | 21 | - | POS +$1.3B | 348.48 | 360 | 360 | +$8.4M | +$0 bull / -$334k bear | out (clean 30, ADX 30, RVol 0.9) |
| 21 | **NFLX** | 62.82 | - | **-** | 20 | - | NEG -$28.9M | 63.68 | 65 | 60 | +$173k | +$64k bull / +$0 bear | out (clean 31, ADX 34, RVol 1.2) |
| 22 | **UBER** | 69.37 | - | **-** | 20 | - | POS +$10.3M | 68.87 | 70 | 70 | +$307k | - | out (clean 33, ADX 21, RVol 0.5) |
| 23 | **SMCI** | 26.37 | - | **-** | 19 | - | NEG -$3.0M | - | 27 | 25 | +$307k | - | out (clean 34, ADX 30, RVol 1.1) |
| 24 | **CRM** | 216.63 | - | **-** | 16 | - | NEG -$7.7M | 222.36 | 220 | 220 | +$85k | - | out (clean 28, ADX 20, RVol 1.3) |
| 25 | **ARM** | 184.56 | - | **-** | 11 | - | NEG -$2.3M | 188.99 | 185 | 190 | -$107k | - | out (clean 33, ADX 58, RVol 1.1) |
| 26 | **SHOP** | 146.91 | - | **-** | 11 | - | POS +$2.4M | 145.48 | 150 | 140 | -$55k | - | out (clean 31, ADX 27, RVol 1.0) |
| 27 | **BABA** | 94.03 | - | **-** | 7 | - | NEG -$19.5M | - | 100 | 95 | -$10k | - | out (clean 28, ADX 26, RVol 1.0) |

## Big prints this scan (173)
- **SPY** CALL 750 2026-11-16 (3DTE): 1,156 @ 4.50 = **+$520k** SELL | vol 19,311 / OI 1,280
- **AVGO** CALL 330 2026-11-16 (3DTE): 180 @ 14.54 = **+$262k** BUY | vol 201 / OI 114
- **SPY** PUT 754 2026-11-13 (0DTE): 500 @ 4.93 = **+$246k** BUY | vol 92,211 / OI 2,617
- **AMD** PUT 530 2026-11-13 (0DTE): 500 @ 4.85 = **+$242k** SELL | vol 16,841 / OI 2,056
- **AVGO** CALL 330 2026-11-13 (0DTE): 180 @ 12.82 = **+$231k** BUY | vol 308 / OI 4,236
- **MU** PUT 770 2026-11-20 (7DTE): 50 @ 38.09 = **+$190k** SELL | vol 886 / OI 1,722
- **MU** CALL 750 2026-11-13 (0DTE): 100 @ 19.00 = **+$190k** BUY | vol 2,630 / OI 1,528
- **MU** CALL 750 2026-11-13 (0DTE): 100 @ 19.00 = **+$190k** BUY | vol 2,630 / OI 1,528
- **SPY** CALL 731 2026-11-13 (0DTE): 100 @ 18.76 = **+$188k** SELL | vol 307 / OI 616
- **SPY** CALL 731 2026-11-13 (0DTE): 99 @ 18.76 = **+$186k** SELL | vol 307 / OI 616
- **TSLA** CALL 375 2026-11-13 (0DTE): 120 @ 14.00 = **+$168k** SELL | vol 1,991 / OI 4,860
- **MU** CALL 760 2026-11-20 (7DTE): 46 @ 35.64 = **+$164k** SELL | vol 392 / OI 1,062
- **NVDA** PUT 162.5 2026-11-20 (7DTE): 160 @ 9.30 = **+$149k** SELL | vol 2,853 / OI 505
- **NVDA** PUT 162.5 2026-11-20 (7DTE): 157 @ 9.30 = **+$146k** SELL | vol 2,853 / OI 505
- **SPY** CALL 750 2026-11-16 (3DTE): 321 @ 4.50 = **+$144k** SELL | vol 19,311 / OI 1,280

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 770 2026-11-17 (4DTE): 923 traded vs OI 768
- **SPY** CALL 795 2026-11-19 (6DTE): 601 traded vs OI 165
- **SPY** CALL 743 2026-11-13 (0DTE): 1,243 traded vs OI 1,158
- **SPY** CALL 767 2026-11-18 (5DTE): 610 traded vs OI 578
- **SPY** CALL 762 2026-11-19 (6DTE): 725 traded vs OI 381
- **SPY** CALL 800 2026-11-19 (6DTE): 1,898 traded vs OI 382
- **SPY** PUT 750 2026-11-17 (4DTE): 2,033 traded vs OI 2,018
- **SPY** CALL 748 2026-11-16 (3DTE): 1,037 traded vs OI 671
- **QQQ** CALL 700 2026-11-16 (3DTE): 7,720 traded vs OI 7,441
- **QQQ** PUT 635 2026-11-16 (3DTE): 535 traded vs OI 478
- **QQQ** CALL 672 2026-11-16 (3DTE): 560 traded vs OI 107
- **QQQ** CALL 706 2026-11-17 (4DTE): 1,131 traded vs OI 231
- **QQQ** PUT 652 2026-11-16 (3DTE): 502 traded vs OI 334
- **QQQ** CALL 670 2026-11-16 (3DTE): 574 traded vs OI 388
- **IWM** CALL 278 2026-11-17 (4DTE): 578 traded vs OI 94

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
