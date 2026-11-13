# GEX + FLOW SCAN - Fri Nov 13, 10:20 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (8)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:17 | **QQQ** | **CALLS** | 1m WHIPSAW (R1 R2) | 11/13 683C | 0.75 | 0.59 | -1% (0m) | **-21%** | +60% | 678.58 |
| 10:15 | **ARM** | **PUTS** | FLIP CROSS down into negative gamma | 11/13 182.5P | 0.74 | 1.14 | +54% (5m) | **+54%** | +96% | 183.6 |
| 10:15 | **ORCL** | **CALLS** | FLIP CROSS up into positive gamma | 11/13 124C | 0.65 | 0.47 | -5% (2m) | **-28%** | +66% | 123.68 |
| 10:10 | **ORCL** | **PUTS** | FLIP CROSS down into negative gamma | 11/13 120P | 0.46 | 0.39 | +7% (5m) | **-15%** | +63% | 121.25 |
| 10:05 | **GOOGL** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/13 297.5P | 0.74 | 2.44 | +236% (14m) | **+230%** | +288% | 295 |
| 09:55 | **BABA** | **PUTS** | FLOW SURGE | 11/13 94P | 0.51 | 0.48 | -4% (24m) | **-6%** | +49% | 93.36 |
| 09:45 | **UBER** | **CALLS** | TREND + FLOW | 11/13 70C | 0.59 | 0.07 | +0% (1m) | **-88%** | +32% | 70.7 |
| 09:45 | **ORCL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/13 127C | 0.46 | 0.09 | +22% (2m) | **-80%** | +48% | 126.38 |

## 1m RULES on SPY / QQQ - loose (1 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:20:08 ET, last candle SPY 10:19, QQQ 10:19 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 10:16 | QQQ | 1m WHIPSAW | R1 R2 | CALLS | TURNING your way | **FIRE** QQQ261113C00683000 |

## Flow surges NOT fired - price disagreed (27 today, last 5)
- 10:20 HOOD CALLS: price -0.56 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:20 COIN CALLS: price -0.08 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:20 PLTR CALLS: price -1.87 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:20 IWM CALLS: price -1.27 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:15 GOOGL CALLS: price -5.09 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **DELL** | 339.33 | FLOW SURGE | **CALLS** | 63 | none: 54 calls 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (47 contracts' greeks worked out here) | NEG -$7.5M | - | 350 | 360 | +$8.5M | +$533k bull / +$0 bear | SHORT (clean 38, ADX 41, RVol 2.0) |
| 2 | **AMD** | 529.32 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 61 | none: 167 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (75 contracts' greeks worked out here) | POS +$60.6M | - | 550 | 530 | +$66.4M | +$8.6M bull / +$0 bear | SHORT (clean 35, ADX 45, RVol 1.6) |
| 3 | **SMH** | 478.47 | FLOW SURGE | **CALLS** | 57 | none: 141 calls 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (65 contracts' greeks worked out here) | NEG -$296.9M | - | 500 | 475 | +$9.3M | +$2.5M bull / +$0 bear | out (clean 30, ADX 47, RVol 2.3) |
| 4 | **COIN** | 127.27 | FLOW SURGE | **CALLS** | 56 | 11/13 129C @ 0.61 (delta 0.29) = est +150% at 130 | NEG -$16.8M | 132.41 | 140 | 130 | +$2.1M | +$199k bull / +$0 bear | out (clean 31, ADX 44, RVol 2.0) |
| 5 | **IWM** | 274.95 | FLOW SURGE | **CALLS** | 55 | 11/13 276C @ 0.49 (delta 0.32) = est +50% at 276 | NEG -$2.9B | 283.52 | 285 | 270 | +$20.2M | +$980k bull / +$0 bear | SHORT (clean 36, ADX 52, RVol 1.3) |
| 6 | **ORCL** | 122.24 | FLOW SURGE | **CALLS** | 55 | none: 48 calls 0-7DTE > 1 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only -1% at the target (needs +20%) (43 contracts' greeks worked out here) | NEG -$3.5M | 123.03 | 120 | 125 | +$1.6M | +$35k bull / +$0 bear | out (clean 31, ADX 40, RVol 2.2) |
| 7 | **HOOD** | 77.53 | FLOW SURGE | **CALLS** | 54 | 11/13 78C @ 0.46 (delta 0.39) = est +314% at 79.92 | NEG -$12.9M | 79.92 | 81 | 80 | +$1.9M | +$1.5M bull / +$0 bear | SHORT (clean 36, ADX 57, RVol 1.7) |
| 8 | **QQQ** | 674.62 | FLOW SURGE | **CALLS** | 53 | none: 748 calls 0-7DTE > 28 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (319 contracts' greeks worked out here) | NEG -$3.0B | 689.83 | 680 | 680 | +$275.3M | +$6.8M bull / +$0 bear | out (clean 31, ADX 51, RVol 1.7) |
| 9 | **GOOGL** | 296.17 | FLOW SURGE | **CALLS** | 52 | none: 94 calls 0-7DTE > 8 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (48 contracts' greeks worked out here) | POS +$196.4M | 290.25 | 300 | 290 | +$14.1M | +$343k bull / +$0 bear | out (clean 30, ADX 29, RVol 2.0) |
| 10 | **SPY** | 749.13 | FLOW SURGE | **CALLS** | 50 | none: 664 calls 0-7DTE > 19 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (287 contracts' greeks worked out here) | NEG -$9.5B | 760.54 | 750 | 750 | +$317.0M | +$6.2M bull / +$0 bear | out (clean 32, ADX 38, RVol 1.2) |
| 11 | **AVGO** | 342.18 | FLOW SURGE | **CALLS** | 50 | none: 108 calls 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (47 contracts' greeks worked out here) | POS +$64.9M | 327.14 | 340 | 340 | +$16.5M | +$2.6M bull / +$0 bear | SHORT (clean 35, ADX 41, RVol 1.3) |
| 12 | **TSLA** | 388.17 | FLOW SURGE | **CALLS** | 49 | none: 124 calls 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (57 contracts' greeks worked out here) | POS +$264.5M | 379.44 | 400 | 380 | +$73.2M | +$6.3M bull / +$0 bear | out (clean 29, ADX 26, RVol 2.3) |
| 13 | **META** | 631.68 | FLIP CROSS up into positive gamma | **CALLS** | 48 | none: 185 calls 0-7DTE > 10 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (103 contracts' greeks worked out here) | POS +$7.4M | 630.97 | 630 | 625 | +$1.7M | +$4.0M bull / +$0 bear | out (clean 29, ADX 42, RVol 3.1) |
| 14 | **PLTR** | 166.00 | FLOW SURGE | **CALLS** | 47 | 11/13 167.5C @ 0.67 (delta 0.32) = est +108% at 168.22 | POS +$71.6M | 161.13 | 165 | 165 | +$2.4M | +$657k bull / +$0 bear | out (clean 28, ADX 38, RVol 1.9) |
| 15 | **MU** | 762.79 | FLOW SURGE | **CALLS** | 47 | none: 164 calls 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (78 contracts' greeks worked out here) | NEG -$21.2M | 772.58 | 800 | 750 | +$67.6M | +$11.2M bull / +$0 bear | out (clean 31, ADX 32, RVol 1.8) |
| 16 | **NVDA** | 160.42 | FLOW SURGE | **CALLS** | 41 | none: 64 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (29 contracts' greeks worked out here) | NEG -$275.9M | - | 175 | 160 | +$90.2M | +$12.1M bull / +$0 bear | out (clean 31, ADX 13, RVol 1.1) |
| 17 | **MSTR** | 110.31 | - | **-** | 28 | - | NEG -$42.3M | - | 110 | 110 | +$2.8M | +$438k bull / -$31k bear | out (clean 30, ADX 38, RVol 1.5) |
| 18 | **AMZN** | 266.12 | - | **-** | 26 | - | POS +$449.4M | 252.25 | 270 | 265 | +$3.3M | +$284k bull / +$0 bear | out (clean 29, ADX 30, RVol 1.0) |
| 19 | **NFLX** | 63.27 | - | **-** | 26 | - | NEG -$16.8M | 63.76 | 65 | 65 | -$292k | +$38k bull / +$0 bear | out (clean 31, ADX 37, RVol 3.2) |
| 20 | **AAPL** | 358.16 | - | **-** | 24 | - | POS +$1.2B | 348.18 | 360 | 360 | +$8.1M | +$901k bull / +$0 bear | out (clean 30, ADX 36, RVol 1.3) |
| 21 | **ARM** | 186.48 | - | **-** | 24 | - | NEG -$1.3M | 188.5 | 185 | 190 | -$187k | +$30k bull / +$0 bear | out (clean 32, ADX 50, RVol 1.4) |
| 22 | **UBER** | 69.16 | - | **-** | 24 | - | POS +$8.4M | 68.73 | 70 | 70 | +$245k | - | out (clean 33, ADX 28, RVol 0.3) |
| 23 | **SMCI** | 26.33 | - | **-** | 22 | - | NEG -$2.4M | - | 27 | 25 | +$241k | - | out (clean 34, ADX 30, RVol 1.1) |
| 24 | **MSFT** | 519.86 | - | **-** | 20 | - | NEG -$27.2M | 520.21 | 535 | 520 | +$199k | +$963k bull / +$0 bear | out (clean 32, ADX 42, RVol 1.3) |
| 25 | **SHOP** | 146.83 | - | **-** | 17 | - | POS +$3.5M | 144.92 | 150 | 140 | +$3k | +$26k bull / +$0 bear | out (clean 31, ADX 29, RVol 0.8) |
| 26 | **BABA** | 93.89 | - | **-** | 17 | - | NEG -$16.7M | - | 100 | 95 | -$21k | +$197k bull / +$0 bear | out (clean 28, ADX 22, RVol 1.1) |
| 27 | **CRM** | 216.75 | - | **-** | 16 | - | NEG -$7.3M | 220.8 | 220 | 220 | +$66k | - | out (clean 29, ADX 28, RVol 0.4) |

## Big prints this scan (343)
- **SPY** CALL 750 2026-11-16 (3DTE): 1,299 @ 6.31 = **+$820k** BUY | vol 8,431 / OI 1,280
- **HOOD** CALL 80 2026-11-20 (7DTE): 1,998 @ 2.25 = **+$450k** BUY | vol 3,406 / OI 2,713
- **SPY** CALL 750 2026-11-16 (3DTE): 750 @ 5.52 = **+$414k** BUY | vol 8,431 / OI 1,280
- **SMH** PUT 477.5 2026-11-20 (7DTE): 224 @ 13.25 = **+$297k** SELL | vol 271 / OI 133
- **MU** PUT 800 2026-11-13 (0DTE): 80 @ 35.00 = **+$280k** SELL | vol 921 / OI 2,029
- **META** PUT 630 2026-11-20 (7DTE): 204 @ 12.88 = **+$263k** SELL | vol 271 / OI 3,103
- **QQQ** CALL 672 2026-11-13 (0DTE): 290 @ 8.07 = **+$234k** BUY | vol 482 / OI 893
- **HOOD** CALL 80 2026-11-20 (7DTE): 1,002 @ 2.25 = **+$225k** BUY | vol 3,406 / OI 2,713
- **SPY** CALL 750 2026-11-16 (3DTE): 400 @ 5.52 = **+$221k** BUY | vol 8,431 / OI 1,280
- **SPY** CALL 750 2026-11-16 (3DTE): 400 @ 5.52 = **+$221k** BUY | vol 8,431 / OI 1,280
- **SPY** CALL 750 2026-11-16 (3DTE): 400 @ 5.52 = **+$221k** BUY | vol 8,431 / OI 1,280
- **QQQ** PUT 678 2026-11-20 (7DTE): 200 @ 11.03 = **+$221k** SELL | vol 299 / OI 1,720
- **MU** PUT 775 2026-11-13 (0DTE): 150 @ 14.70 = **+$220k** SELL | vol 5,698 / OI 938
- **NVDA** PUT 160 2026-11-18 (5DTE): 320 @ 6.58 = **+$211k** SELL | vol 2,633 / OI 5,421
- **MU** CALL 742.5 2026-11-13 (0DTE): 67 @ 29.66 = **+$199k** BUY | vol 78 / OI 384

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 770 2026-11-13 (0DTE): 19,758 traded vs OI 19,510
- **SPY** PUT 732 2026-11-16 (3DTE): 1,055 traded vs OI 709
- **SPY** CALL 782 2026-11-17 (4DTE): 2,103 traded vs OI 1,499
- **SPY** CALL 755 2026-11-17 (4DTE): 565 traded vs OI 554
- **SPY** CALL 763 2026-11-17 (4DTE): 761 traded vs OI 683
- **SPY** CALL 752 2026-11-16 (3DTE): 1,406 traded vs OI 525
- **SPY** PUT 717 2026-11-17 (4DTE): 506 traded vs OI 391
- **SPY** CALL 758 2026-11-17 (4DTE): 520 traded vs OI 501
- **SPY** CALL 753 2026-11-16 (3DTE): 884 traded vs OI 642
- **SPY** PUT 733 2026-11-13 (0DTE): 6,064 traded vs OI 2,569
- **SPY** CALL 781 2026-11-17 (4DTE): 560 traded vs OI 186
- **SPY** PUT 731 2026-11-16 (3DTE): 513 traded vs OI 346
- **SPY** CALL 751 2026-11-13 (0DTE): 2,950 traded vs OI 2,050
- **SPY** PUT 754 2026-11-17 (4DTE): 582 traded vs OI 315
- **SPY** PUT 757 2026-11-17 (4DTE): 515 traded vs OI 275

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
