# GEX + FLOW SCAN - Fri Nov 13, 10:15 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (7)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:15 | **ARM** | **PUTS** | FLIP CROSS down into negative gamma | 11/13 182.5P | 0.74 | 0.63 | -15% (0m) | **-15%** | +96% | 183.6 |
| 10:15 | **ORCL** | **CALLS** | FLIP CROSS up into positive gamma | 11/13 124C | 0.65 | 0.58 | -11% (0m) | **-11%** | +66% | 123.68 |
| 10:10 | **ORCL** | **PUTS** | FLIP CROSS down into negative gamma | 11/13 120P | 0.46 | 0.49 | +7% (5m) | **+7%** | +63% | 121.25 |
| 10:05 | **GOOGL** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/13 297.5P | 0.74 | 2.38 | +222% (10m) | **+222%** | +288% | 295 |
| 09:55 | **BABA** | **PUTS** | FLOW SURGE | 11/13 94P | 0.51 | 0.45 | -8% (0m) | **-12%** | +49% | 93.36 |
| 09:45 | **UBER** | **CALLS** | TREND + FLOW | 11/13 70C | 0.59 | 0.07 | +0% (1m) | **-88%** | +32% | 70.7 |
| 09:45 | **ORCL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/13 127C | 0.46 | 0.04 | +22% (2m) | **-91%** | +48% | 126.38 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:15:08 ET, last candle SPY 10:14, QQQ 10:14 | no errors

## Flow surges NOT fired - price disagreed (23 today, last 5)
- 10:15 GOOGL CALLS: price -5.09 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:10 COIN CALLS: price -0.49 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:10 IWM CALLS: price -1.19 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:10 SPY CALLS: price -3.55 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:05 HOOD CALLS: price -0.53 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **DELL** | 337.37 | FLOW SURGE | **CALLS** | 64 | none: 54 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (44 contracts' greeks worked out here) | NEG -$3.4M | 345.81 | 350 | 340 | +$7.3M | +$145k bull / +$0 bear | SHORT (clean 38, ADX 39, RVol 2.2) |
| 2 | **AMD** | 529.25 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 62 | none: 167 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (70 contracts' greeks worked out here) | POS +$53.4M | - | 550 | 530 | +$54.8M | +$7.5M bull / +$0 bear | SHORT (clean 35, ADX 43, RVol 1.8) |
| 3 | **IWM** | 275.45 | FLOW SURGE | **CALLS** | 54 | none: 322 calls 0-7DTE > 12 priced 0.40-0.80 > 5 delta 0.2+ > 5 spread ok > 5 liquid > best one only +19% at the target (needs +20%) (164 contracts' greeks worked out here) | NEG -$2.7B | 282.89 | 285 | 275 | +$14.9M | +$220k bull / +$0 bear | SHORT (clean 36, ADX 50, RVol 1.3) |
| 4 | **SMH** | 478.70 | FLOW SURGE | **CALLS** | 54 | none: 141 calls 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (62 contracts' greeks worked out here) | NEG -$295.9M | - | 500 | 475 | +$5.4M | +$2.3M bull / +$0 bear | out (clean 30, ADX 44, RVol 2.2) |
| 5 | **TSLA** | 387.76 | FLOW SURGE | **CALLS** | 52 | none: 124 calls 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (56 contracts' greeks worked out here) | POS +$319.1M | - | 400 | 380 | +$62.6M | +$8.7M bull / +$0 bear | out (clean 30, ADX 27, RVol 2.8) |
| 6 | **GOOGL** | 296.23 | FLOW SURGE | **CALLS** | 52 | 11/13 300C @ 0.61 (delta 0.22) = est +164% at 300 | POS +$187.0M | 289.33 | 300 | 290 | +$12.1M | +$1.1M bull / +$0 bear | out (clean 30, ADX 29, RVol 2.2) |
| 7 | **QQQ** | 674.34 | FLOW SURGE | **CALLS** | 50 | none: 752 calls 0-7DTE > 25 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (279 contracts' greeks worked out here) | NEG -$2.6B | 685.7 | 700 | 680 | +$218.6M | +$5.5M bull / +$0 bear | out (clean 31, ADX 48, RVol 1.2) |
| 8 | **AVGO** | 342.57 | FLOW SURGE | **CALLS** | 50 | none: 108 calls 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (49 contracts' greeks worked out here) | POS +$74.4M | - | 340 | 340 | +$15.4M | +$3.0M bull / +$0 bear | SHORT (clean 35, ADX 39, RVol 1.4) |
| 9 | **ORCL** | 121.78 | FLIP CROSS up into positive gamma | **CALLS** | 50 | 11/13 124C @ 0.65 (delta 0.28) = est +66% at 123.68 | POS +$4.1M | 121.33 | 130 | 120 | +$1.5M | - | out (clean 31, ADX 37, RVol 2.4) |
| 10 | **SPY** | 749.10 | FLOW SURGE | **CALLS** | 48 | none: 664 calls 0-7DTE > 19 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (248 contracts' greeks worked out here) | NEG -$7.9B | 757.72 | 775 | 750 | +$234.1M | +$3.5M bull / +$0 bear | out (clean 32, ADX 36, RVol 1.2) |
| 11 | **META** | 630.34 | FLIP CROSS down into negative gamma | **PUTS** | 48 | none: 188 puts 0-7DTE > 8 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (98 contracts' greeks worked out here) | NEG -$12.8M | 631.38 | 650 | 625 | -$813k | +$3.7M bull / +$0 bear | out (clean 29, ADX 43, RVol 2.9) |
| 12 | **ARM** | 187.39 | FLIP CROSS down into negative gamma | **PUTS** | 45 | 11/13 182.5P @ 0.74 (delta 0.20) = est +96% at 183.6 | NEG -$1.8M | 189.31 | 200 | 190 | -$241k | +$30k bull / +$0 bear | out (clean 32, ADX 47, RVol 1.8) |
| 13 | **PLTR** | 165.88 | FLOW SURGE | **CALLS** | 44 | none: 26 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (21 contracts' greeks worked out here) | POS +$56.2M | 158.29 | 165 | 165 | +$1.5M | +$575k bull / +$0 bear | out (clean 28, ADX 35, RVol 1.9) |
| 14 | **HOOD** | 77.47 | TREND (flow not with it) | **PUTS** | 43 | 11/13 77P @ 0.44 (delta 0.38) = est +22% at 77 | NEG -$7.3M | 78.51 | 81 | 75 | +$1.2M | +$1.3M bull / +$0 bear | SHORT (clean 35, ADX 55, RVol 1.6) |
| 15 | **NVDA** | 160.28 | FLOW SURGE | **CALLS** | 42 | none: 64 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (28 contracts' greeks worked out here) | NEG -$238.3M | - | 175 | 160 | +$86.1M | +$13.6M bull / -$295k bear | out (clean 31, ADX 13, RVol 1.1) |
| 16 | **MU** | 759.66 | FLOW SURGE | **CALLS** | 41 | none: 168 calls 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (85 contracts' greeks worked out here) | POS +$1.2M | 759.42 | 800 | 750 | +$52.6M | +$11.0M bull / +$0 bear | out (clean 31, ADX 30, RVol 1.7) |
| 17 | **MSFT** | 518.95 | FLIP CROSS down into negative gamma | **PUTS** | 39 | none: 164 puts 0-7DTE > 11 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (87 contracts' greeks worked out here) | NEG -$29.0M | 520.06 | 535 | 520 | -$1.9M | +$2.7M bull / +$0 bear | out (clean 32, ADX 42, RVol 1.4) |
| 18 | **NFLX** | 63.22 | - | **-** | 30 | - | NEG -$13.4M | 63.66 | 65 | 63 | -$429k | +$50k bull / +$0 bear | out (clean 31, ADX 40, RVol 3.0) |
| 19 | **MSTR** | 109.94 | - | **-** | 28 | - | NEG -$36.2M | - | 120 | 110 | +$2.3M | +$705k bull / -$31k bear | out (clean 30, ADX 38, RVol 1.9) |
| 20 | **COIN** | 127.41 | - | **-** | 26 | - | NEG -$17.3M | 132.09 | 140 | 130 | +$1.7M | - | out (clean 31, ADX 43, RVol 1.6) |
| 21 | **AMZN** | 265.88 | - | **-** | 25 | - | POS +$465.6M | - | 270 | 265 | +$2.7M | +$153k bull / +$0 bear | out (clean 29, ADX 30, RVol 1.1) |
| 22 | **UBER** | 69.28 | - | **-** | 25 | - | POS +$9.4M | 68.78 | 70 | 70 | +$239k | - | out (clean 33, ADX 31, RVol 0.5) |
| 23 | **AAPL** | 357.60 | - | **-** | 23 | - | POS +$1.2B | 346.33 | 360 | 360 | +$3.6M | +$975k bull / +$0 bear | out (clean 30, ADX 37, RVol 1.6) |
| 24 | **SMCI** | 26.32 | - | **-** | 22 | - | NEG -$2.3M | 27.7 | 28 | 25 | +$213k | - | out (clean 34, ADX 30, RVol 1.1) |
| 25 | **SHOP** | 147.26 | - | **-** | 19 | - | POS +$4.7M | 145.09 | 150 | 140 | -$12k | +$26k bull / +$0 bear | out (clean 32, ADX 30, RVol 0.9) |
| 26 | **BABA** | 94.03 | - | **-** | 19 | - | NEG -$14.4M | - | 100 | 100 | -$106k | +$349k bull / +$0 bear | out (clean 28, ADX 22, RVol 1.2) |
| 27 | **CRM** | 216.42 | - | **-** | 14 | - | NEG -$7.5M | 220.86 | 220 | 220 | +$39k | - | out (clean 29, ADX 30, RVol 0.5) |

## Big prints this scan (318)
- **SPY** CALL 750 2026-11-16 (3DTE): 1,999 @ 7.45 = **+$1.5M** BUY | vol 4,120 / OI 1,280
- **NVDA** CALL 167.5 2026-11-20 (7DTE): 2,000 @ 6.16 = **+$1.2M** BUY | vol 5,968 / OI 1,962
- **NVDA** CALL 167.5 2026-11-20 (7DTE): 2,000 @ 6.16 = **+$1.2M** BUY | vol 5,968 / OI 1,962
- **SPY** CALL 750 2026-11-16 (3DTE): 1,599 @ 6.50 = **+$1.0M** BUY | vol 4,120 / OI 1,280
- **AVGO** PUT 340 2026-11-20 (7DTE): 1,250 @ 7.88 = **+$985k** SELL | vol 1,616 / OI 15,339
- **QQQ** PUT 664 2026-11-19 (6DTE): 2,357 @ 4.14 = **+$976k** SELL | vol 5,002 / OI 88
- **NVDA** PUT 152.5 2026-11-20 (7DTE): 1,448 @ 4.20 = **+$608k** SELL | vol 1,900 / OI 853
- **AVGO** PUT 330 2026-11-20 (7DTE): 1,250 @ 4.72 = **+$590k** SELL | vol 2,083 / OI 10,919
- **TSLA** CALL 392.5 2026-11-13 (0DTE): 1,999 @ 2.66 = **+$532k** BUY | vol 9,758 / OI 7,163
- **QQQ** PUT 664 2026-11-19 (6DTE): 1,250 @ 4.14 = **+$518k** SELL | vol 5,002 / OI 88
- **NVDA** PUT 160 2026-11-20 (7DTE): 675 @ 7.50 = **+$506k** SELL | vol 6,917 / OI 37,700
- **QQQ** PUT 664 2026-11-19 (6DTE): 1,109 @ 4.14 = **+$459k** SELL | vol 5,002 / OI 88
- **NVDA** PUT 157.5 2026-11-20 (7DTE): 724 @ 5.97 = **+$432k** SELL | vol 3,557 / OI 424
- **NVDA** CALL 167.5 2026-11-20 (7DTE): 585 @ 6.15 = **+$360k** BUY | vol 5,968 / OI 1,962
- **SMH** PUT 465 2026-11-20 (7DTE): 400 @ 6.65 = **+$266k** SELL | vol 617 / OI 6,220

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 769 2026-11-16 (3DTE): 1,487 traded vs OI 1,326
- **SPY** PUT 740 2026-11-16 (3DTE): 3,736 traded vs OI 3,668
- **SPY** CALL 755 2026-11-16 (3DTE): 1,446 traded vs OI 1,093
- **SPY** CALL 754 2026-11-16 (3DTE): 598 traded vs OI 383
- **SPY** CALL 754 2026-11-13 (0DTE): 8,232 traded vs OI 4,505
- **SPY** PUT 742 2026-11-13 (0DTE): 6,534 traded vs OI 6,374
- **SPY** PUT 733 2026-11-16 (3DTE): 1,482 traded vs OI 505
- **SPY** PUT 748 2026-11-17 (4DTE): 515 traded vs OI 369
- **SPY** PUT 719 2026-11-16 (3DTE): 1,113 traded vs OI 1,045
- **SPY** CALL 752 2026-11-13 (0DTE): 2,005 traded vs OI 1,839
- **SPY** PUT 737 2026-11-16 (3DTE): 1,072 traded vs OI 1,017
- **SPY** PUT 739 2026-11-16 (3DTE): 613 traded vs OI 405
- **SPY** PUT 764 2026-11-13 (0DTE): 1,014 traded vs OI 979
- **SPY** CALL 767 2026-11-17 (4DTE): 597 traded vs OI 574
- **QQQ** PUT 650 2026-11-16 (3DTE): 1,373 traded vs OI 1,356

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
