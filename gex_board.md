# GEX + FLOW SCAN - Fri Nov 13, 10:10 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (5)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:10 | **ORCL** | **PUTS** | FLIP CROSS down into negative gamma | 11/13 120P | 0.46 | 0.43 | -7% (0m) | **-7%** | +63% | 121.25 |
| 10:05 | **GOOGL** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/13 297.5P | 0.74 | 1.31 | +77% (5m) | **+77%** | +288% | 295 |
| 09:55 | **BABA** | **PUTS** | FLOW SURGE | 11/13 94P | 0.51 | 0.27 | -8% (0m) | **-47%** | +49% | 93.36 |
| 09:45 | **UBER** | **CALLS** | TREND + FLOW | 11/13 70C | 0.59 | 0.13 | +0% (1m) | **-78%** | +32% | 70.7 |
| 09:45 | **ORCL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/13 127C | 0.46 | 0.13 | +22% (2m) | **-72%** | +48% | 126.38 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:10:08 ET, last candle SPY 10:09, QQQ 10:09 | no errors

## Flow surges NOT fired - price disagreed (22 today, last 5)
- 10:10 COIN CALLS: price -0.49 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:10 IWM CALLS: price -1.19 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:10 SPY CALLS: price -3.55 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:05 HOOD CALLS: price -0.53 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:05 COIN CALLS: price -1.46 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **DELL** | 342.28 | FLOW SURGE | **CALLS** | 63 | none: 54 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (45 contracts' greeks worked out here) | NEG -$5.9M | - | 350 | 360 | +$2.7M | +$125k bull / +$0 bear | SHORT (clean 38, ADX 36, RVol 2.1) |
| 2 | **SMH** | 482.74 | FLOW SURGE | **CALLS** | 59 | none: 146 calls 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (67 contracts' greeks worked out here) | NEG -$286.1M | - | 500 | 475 | +$6.4M | +$1.0M bull / +$0 bear | out (clean 30, ADX 42, RVol 2.0) |
| 3 | **TSLA** | 387.75 | FLOW SURGE | **CALLS** | 54 | none: 124 calls 0-7DTE > 8 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (53 contracts' greeks worked out here) | POS +$301.9M | 364.53 | 400 | 380 | +$59.1M | +$8.6M bull / +$0 bear | out (clean 30, ADX 28, RVol 4.4) |
| 4 | **IWM** | 276.06 | FLOW SURGE | **CALLS** | 53 | 11/13 277C @ 0.44 (delta 0.32) = est +74% at 277.22 | NEG -$2.7B | 283.32 | 285 | 275 | +$12.1M | +$925k bull / +$0 bear | SHORT (clean 36, ADX 48, RVol 1.2) |
| 5 | **AVGO** | 344.82 | FLOW SURGE | **CALLS** | 52 | none: 108 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (50 contracts' greeks worked out here) | POS +$76.0M | 333.99 | 340 | 340 | +$15.9M | +$1.6M bull / +$0 bear | SHORT (clean 35, ADX 37, RVol 1.4) |
| 6 | **COIN** | 128.21 | FLOW SURGE | **CALLS** | 52 | 11/13 130C @ 0.58 (delta 0.29) = est +80% at 130 | NEG -$15.2M | 131.88 | 140 | 130 | +$1.7M | +$1.3M bull / +$0 bear | out (clean 31, ADX 42, RVol 1.6) |
| 7 | **ORCL** | 123.05 | FLIP CROSS down into negative gamma | **PUTS** | 52 | 11/13 120P @ 0.46 (delta 0.20) = est +63% at 121.25 | NEG -$8.0M | 123.82 | 125 | 125 | +$1.5M | - | out (clean 31, ADX 35, RVol 2.6) |
| 8 | **AMD** | 537.99 | FLOW SURGE | **CALLS** | 51 | none: 171 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (72 contracts' greeks worked out here) | POS +$80.0M | 520.19 | 550 | 550 | +$50.3M | +$6.5M bull / +$0 bear | SHORT (clean 35, ADX 40, RVol 1.7) |
| 9 | **GOOGL** | 298.67 | FLOW SURGE | **CALLS** | 51 | none: 94 calls 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (45 contracts' greeks worked out here) | POS +$227.1M | 292.08 | 300 | 290 | +$11.4M | +$2.0M bull / +$0 bear | out (clean 30, ADX 29, RVol 1.9) |
| 10 | **QQQ** | 678.10 | FLOW SURGE | **CALLS** | 49 | none: 740 calls 0-7DTE > 25 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (279 contracts' greeks worked out here) | NEG -$2.8B | 690.79 | 680 | 680 | +$186.3M | +$8.2M bull / +$0 bear | out (clean 31, ADX 46, RVol 1.1) |
| 11 | **SPY** | 752.09 | FLOW SURGE | **CALLS** | 47 | 11/13 756C @ 0.65 (delta 0.22) = est +98% at 755 | NEG -$8.2B | 761.16 | 750 | 750 | +$195.6M | +$1.9M bull / +$0 bear | out (clean 32, ADX 34, RVol 1.0) |
| 12 | **MU** | 766.79 | FLOW SURGE | **CALLS** | 46 | none: 160 calls 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (71 contracts' greeks worked out here) | NEG -$21.2M | 774.06 | 800 | 750 | +$54.7M | +$10.3M bull / +$0 bear | out (clean 31, ADX 28, RVol 1.5) |
| 13 | **PLTR** | 168.22 | FLOW SURGE | **CALLS** | 44 | 11/13 170C @ 0.48 (delta 0.27) = est +106% at 170 | POS +$71.3M | 165.16 | 170 | 165 | +$1.3M | +$216k bull / +$0 bear | out (clean 28, ADX 32, RVol 1.6) |
| 14 | **HOOD** | 78.17 | TREND (flow not with it) | **PUTS** | 44 | 11/13 77P @ 0.52 (delta 0.31) = est +59% at 76.88 | NEG -$12.3M | 80.02 | 81 | 80 | +$1.1M | +$1.3M bull / +$0 bear | SHORT (clean 35, ADX 53, RVol 1.7) |
| 15 | **NVDA** | 161.73 | FLOW SURGE | **CALLS** | 43 | 11/13 165C @ 0.49 (delta 0.21) = est +182% at 165 | NEG -$268.8M | - | 175 | 160 | +$83.7M | +$11.5M bull / -$331k bear | out (clean 31, ADX 12, RVol 1.2) |
| 16 | **MSFT** | 521.36 | FLIP CROSS up into positive gamma | **CALLS** | 40 | none: 166 calls 0-7DTE > 10 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (84 contracts' greeks worked out here) | POS +$21.9M | 520.44 | 535 | 520 | -$2.0M | +$2.5M bull / -$304k bear | out (clean 32, ADX 42, RVol 1.4) |
| 17 | **ARM** | 189.39 | FLIP CROSS up into positive gamma | **CALLS** | 34 | none: 30 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (24 contracts' greeks worked out here) | POS +$197k | 189.18 | 200 | 190 | -$55k | - | out (clean 32, ADX 45, RVol 2.1) |
| 18 | **NFLX** | 63.62 | - | **-** | 32 | - | NEG -$4.6M | 63.73 | 64 | 65 | -$489k | +$50k bull / -$63k bear | out (clean 31, ADX 42, RVol 3.0) |
| 19 | **MSTR** | 110.26 | - | **-** | 31 | - | NEG -$39.8M | - | 110 | 110 | +$2.6M | +$830k bull / +$0 bear | out (clean 30, ADX 36, RVol 2.6) |
| 20 | **UBER** | 69.40 | - | **-** | 26 | - | POS +$12.6M | 68.77 | 70 | 70 | +$232k | - | out (clean 33, ADX 32, RVol 0.8) |
| 21 | **AMZN** | 267.50 | - | **-** | 25 | - | POS +$514.1M | 254.33 | 270 | 265 | +$2.4M | +$139k bull / -$229k bear | out (clean 29, ADX 30, RVol 1.0) |
| 22 | **META** | 634.50 | - | **-** | 24 | - | POS +$62.9M | 630.38 | 630 | 625 | -$1.5M | +$1.9M bull / -$493k bear | out (clean 29, ADX 44, RVol 2.8) |
| 23 | **AAPL** | 358.88 | - | **-** | 23 | - | POS +$1.3B | 347.41 | 360 | 360 | +$2.8M | +$718k bull / -$349k bear | out (clean 30, ADX 39, RVol 1.7) |
| 24 | **SMCI** | 26.48 | - | **-** | 23 | - | NEG -$2.5M | - | 27 | 25 | +$208k | - | out (clean 34, ADX 29, RVol 1.2) |
| 25 | **SHOP** | 148.70 | - | **-** | 20 | - | POS +$6.8M | 145.36 | 150 | 150 | -$18k | +$26k bull / -$58k bear | out (clean 32, ADX 30, RVol 1.0) |
| 26 | **BABA** | 94.28 | - | **-** | 18 | - | NEG -$19.8M | - | 100 | 95 | -$50k | +$349k bull / +$0 bear | out (clean 28, ADX 21, RVol 1.3) |
| 27 | **CRM** | 217.71 | - | **-** | 12 | - | NEG -$6.2M | 222.63 | 220 | 220 | +$22k | - | out (clean 30, ADX 31, RVol 0.4) |

## Big prints this scan (268)
- **NVDA** PUT 160 2026-11-20 (7DTE): 697 @ 7.15 = **+$498k** SELL | vol 6,258 / OI 37,700
- **HOOD** PUT 76 2026-11-20 (7DTE): 2,316 @ 1.99 = **+$461k** SELL | vol 2,410 / OI 427
- **AMD** PUT 545 2026-11-13 (0DTE): 746 @ 5.75 = **+$429k** SELL | vol 4,099 / OI 407
- **MU** PUT 780 2026-11-20 (7DTE): 120 @ 34.00 = **+$408k** SELL | vol 1,047 / OI 1,660
- **HOOD** CALL 82 2026-11-20 (7DTE): 2,316 @ 1.75 = **+$405k** BUY | vol 2,489 / OI 294
- **QQQ** PUT 685 2026-11-13 (0DTE): 800 @ 4.62 = **+$370k** SELL | vol 40,210 / OI 26,536
- **MSFT** CALL 500 2026-11-20 (7DTE): 140 @ 26.05 = **+$365k** BUY | vol 204 / OI 8,743
- **TSLA** CALL 400 2026-11-20 (7DTE): 347 @ 7.75 = **+$269k** BUY | vol 4,978 / OI 21,808
- **QQQ** PUT 700 2026-11-13 (0DTE): 149 @ 16.90 = **+$252k** SELL | vol 762 / OI 3,040
- **QQQ** PUT 700 2026-11-13 (0DTE): 149 @ 16.90 = **+$252k** SELL | vol 762 / OI 3,040
- **NVDA** PUT 157.5 2026-11-20 (7DTE): 363 @ 6.35 = **+$231k** SELL | vol 3,224 / OI 424
- **AMD** CALL 550 2026-11-20 (7DTE): 100 @ 23.00 = **+$230k** BUY | vol 353 / OI 5,879
- **MU** PUT 780 2026-11-13 (0DTE): 199 @ 10.00 = **+$199k** SELL | vol 5,072 / OI 1,619
- **BABA** CALL 95 2026-11-20 (7DTE): 607 @ 3.25 = **+$197k** BUY | vol 2,114 / OI 278
- **META** PUT 632.5 2026-11-13 (0DTE): 477 @ 4.10 = **+$196k** SELL | vol 1,199 / OI 463

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 735 2026-11-13 (0DTE): 12,620 traded vs OI 11,710
- **SPY** CALL 783 2026-11-17 (4DTE): 995 traded vs OI 397
- **SPY** CALL 760 2026-11-17 (4DTE): 1,203 traded vs OI 1,157
- **SPY** CALL 761 2026-11-17 (4DTE): 559 traded vs OI 445
- **SPY** PUT 739 2026-11-13 (0DTE): 5,370 traded vs OI 2,811
- **SPY** CALL 750 2026-11-16 (3DTE): 2,386 traded vs OI 1,280
- **SPY** PUT 752 2026-11-17 (4DTE): 519 traded vs OI 162
- **SPY** PUT 737 2026-11-13 (0DTE): 3,835 traded vs OI 2,705
- **SPY** CALL 753 2026-11-13 (0DTE): 2,294 traded vs OI 1,459
- **SPY** CALL 765 2026-11-17 (4DTE): 826 traded vs OI 822
- **SPY** PUT 747 2026-11-17 (4DTE): 600 traded vs OI 419
- **SPY** PUT 734 2026-11-16 (3DTE): 516 traded vs OI 475
- **SPY** PUT 738 2026-11-13 (0DTE): 6,372 traded vs OI 4,458
- **SPY** PUT 749 2026-11-16 (3DTE): 1,320 traded vs OI 1,015
- **SPY** PUT 748 2026-11-16 (3DTE): 936 traded vs OI 884

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
