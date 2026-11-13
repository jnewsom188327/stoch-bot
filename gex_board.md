# GEX + FLOW SCAN - Fri Nov 13, 09:55 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (3)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 09:55 | **BABA** | **PUTS** | FLOW SURGE | 11/13 94P | 0.51 | 0.39 | -24% (0m) | **-24%** | +49% | 93.36 |
| 09:45 | **UBER** | **CALLS** | TREND + FLOW | 11/13 70C | 0.59 | 0.24 | +0% (1m) | **-59%** | +32% | 70.7 |
| 09:45 | **ORCL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/13 127C | 0.46 | 0.25 | +22% (2m) | **-46%** | +48% | 126.38 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 09:55:08 ET, last candle SPY 09:54, QQQ 09:54 | no errors

## Flow surges NOT fired - price disagreed (9 today, last 5)
- 09:55 NFLX PUTS: price +0.51 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:55 GOOGL CALLS: price -1.32 over the last 15 min - flow says one way, price says the other
- 09:55 IWM CALLS: price -0.60 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 09:55 SPY CALLS: price -1.29 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 09:50 MSTR CALLS: under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **META** | 635.99 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 68 | none: 189 calls 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (85 contracts' greeks worked out here) | POS +$69.8M | 632.1 | 650 | 635 | -$14.1M | +$0 bull / -$715k bear | out (clean 29, ADX 40, RVol 2.5) |
| 2 | **DELL** | 349.19 | FLOW SURGE | **CALLS** | 63 | none: 56 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (47 contracts' greeks worked out here) | NEG -$8.0M | - | 360 | 360 | +$436k | +$192k bull / +$0 bear | SHORT (clean 37, ADX 28, RVol 2.1) |
| 3 | **IWM** | 277.25 | FLOW SURGE | **CALLS** | 62 | 11/13 278C @ 0.52 (delta 0.36) = est +150% at 279 | NEG -$2.3B | 283.35 | 285 | 275 | +$3.8M | +$388k bull / +$0 bear | SHORT (clean 35, ADX 45, RVol 2.6) |
| 4 | **AVGO** | 348.07 | FLOW SURGE | **CALLS** | 61 | none: 112 calls 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (47 contracts' greeks worked out here) | POS +$99.2M | 333.53 | 350 | 340 | +$7.2M | +$685k bull / +$0 bear | SHORT (clean 34, ADX 29, RVol 2.6) |
| 5 | **BABA** | 94.13 | FLOW SURGE | **PUTS** | 61 | 11/13 94P @ 0.51 (delta 0.46) = est +49% at 93.36 | NEG -$17.0M | - | 100 | 95 | -$312k | +$0 bull / -$51k bear | out (clean 28, ADX 20, RVol 4.5) |
| 6 | **NFLX** | 63.72 | FLOW SURGE | **PUTS** | 60 | 11/13 64P @ 0.54 (delta 0.62) = est +42% at 63.27 | NEG -$4.4M | 63.85 | 65 | 65 | -$313k | +$0 bull / -$53k bear | out (clean 31, ADX 47, RVol 3.6) |
| 7 | **ORCL** | 124.40 | FLOW SURGE | **CALLS** | 60 | none: 50 calls 0-7DTE > 1 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only +5% at the target (needs +20%) (40 contracts' greeks worked out here) | NEG -$1.9M | 124.56 | 125 | 125 | +$1.0M | +$425k bull / +$0 bear | out (clean 31, ADX 28, RVol 2.5) |
| 8 | **GOOGL** | 302.26 | FLOW SURGE | **CALLS** | 58 | 11/13 305C @ 0.63 (delta 0.25) = est +126% at 305.1 | POS +$239.1M | 290.47 | 300 | 290 | +$7.2M | +$2.7M bull / +$0 bear | out (clean 30, ADX 32, RVol 3.5) |
| 9 | **HOOD** | 78.75 | TREND (flow not with it) | **PUTS** | 58 | 11/13 78P @ 0.64 (delta 0.37) = est +61% at 77.45 | NEG -$9.4M | 80.16 | 81 | 80 | +$428k | - | SHORT (clean 35, ADX 48, RVol 4.0) |
| 10 | **UBER** | 69.70 | TREND + FLOW | **CALLS** | 58 | none: 30 calls 0-7DTE > 3 priced 0.40-0.80 > 3 delta 0.2+ > 3 spread ok > 3 liquid > best one only +5% at the target (needs +20%) (22 contracts' greeks worked out here) | POS +$17.1M | 68.83 | 70 | 70 | +$155k | - | LONG (clean 33, ADX 34, RVol 2.1) |
| 11 | **AMD** | 548.29 | FLOW SURGE | **CALLS** | 57 | none: 175 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (78 contracts' greeks worked out here) | POS +$150.7M | - | 550 | 550 | +$26.3M | +$8.4M bull / +$0 bear | SHORT (clean 35, ADX 31, RVol 2.2) |
| 12 | **QQQ** | 683.53 | FLOW SURGE | **CALLS** | 55 | none: 726 calls 0-7DTE > 25 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only +7% at the target (needs +20%) (255 contracts' greeks worked out here) | NEG -$2.2B | 691.16 | 700 | 680 | +$64.9M | +$2.7M bull / +$0 bear | out (clean 31, ADX 39, RVol 2.3) |
| 13 | **SMH** | 489.20 | FLOW SURGE | **CALLS** | 55 | none: 147 calls 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (68 contracts' greeks worked out here) | NEG -$242.2M | - | 500 | 475 | +$3.2M | +$829k bull / +$0 bear | out (clean 30, ADX 34, RVol 1.6) |
| 14 | **MSFT** | 522.46 | FLOW SURGE | **PUTS** | 55 | none: 162 puts 0-7DTE > 12 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (83 contracts' greeks worked out here) | POS +$65.1M | 520.57 | 535 | 520 | -$7.2M | +$0 bull / -$1.1M bear | out (clean 32, ADX 44, RVol 2.1) |
| 15 | **SPY** | 755.64 | FLOW SURGE | **CALLS** | 51 | 11/13 759C @ 0.58 (delta 0.23) = est +245% at 760 | NEG -$6.5B | 761.56 | 760 | 760 | +$93.6M | +$8.0M bull / +$0 bear | out (clean 32, ADX 32, RVol 1.6) |
| 16 | **TSLA** | 394.25 | FLOW SURGE | **CALLS** | 51 | none: 128 calls 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (56 contracts' greeks worked out here) | POS +$440.0M | 380.55 | 400 | 380 | +$24.6M | +$4.5M bull / -$3.2M bear | out (clean 30, ADX 34, RVol 6.1) |
| 17 | **NVDA** | 162.72 | FLOW SURGE | **CALLS** | 50 | none: 60 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (27 contracts' greeks worked out here) | NEG -$260.6M | - | 175 | 160 | +$55.3M | +$8.8M bull / -$32k bear | out (clean 31, ADX 15, RVol 1.8) |
| 18 | **MU** | 783.26 | FLOW SURGE | **CALLS** | 50 | none: 156 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (74 contracts' greeks worked out here) | NEG -$13.2M | 786.17 | 800 | 800 | +$28.0M | +$9.9M bull / -$551k bear | out (clean 30, ADX 20, RVol 1.9) |
| 19 | **AAPL** | 359.73 | PINNED between the walls (positive gamma) - chop | **-** | 47 | - | POS +$1.3B | 348.01 | 360 | 360 | -$2.2M | +$548k bull / -$565k bear | out (clean 30, ADX 39, RVol 2.5) |
| 20 | **PLTR** | 170.35 | PINNED between the walls (positive gamma) - chop | **-** | 46 | - | POS +$91.6M | 165.33 | 170 | 170 | +$226k | +$0 bull / -$25k bear | out (clean 29, ADX 26, RVol 2.1) |
| 21 | **SHOP** | 150.25 | PINNED between the walls (positive gamma) - chop | **-** | 44 | - | POS +$7.6M | 146.46 | 150 | 150 | -$75k | - | out (clean 32, ADX 33, RVol 1.7) |
| 22 | **MSTR** | 111.34 | - | **-** | 36 | - | NEG -$37.6M | - | 120 | 110 | +$2.5M | +$515k bull / -$635k bear | out (clean 30, ADX 32, RVol 4.4) |
| 23 | **COIN** | 128.70 | - | **-** | 28 | - | NEG -$13.9M | 131.97 | 137 | 130 | +$204k | +$36k bull / -$31k bear | out (clean 31, ADX 39, RVol 3.1) |
| 24 | **SMCI** | 26.52 | - | **-** | 27 | - | NEG -$2.4M | - | 28 | 25 | +$137k | - | out (clean 34, ADX 26, RVol 2.7) |
| 25 | **AMZN** | 268.94 | - | **-** | 24 | - | POS +$554.6M | 254.06 | 270 | 265 | +$616k | +$0 bull / -$218k bear | out (clean 30, ADX 34, RVol 1.9) |
| 26 | **CRM** | 217.66 | - | **-** | 20 | - | NEG -$5.8M | 221.9 | 220 | 220 | +$28k | - | out (clean 30, ADX 28, RVol 2.8) |
| 27 | **ARM** | 191.42 | - | **-** | 14 | - | POS +$1.5M | 190.41 | 200 | 190 | -$66k | - | out (clean 32, ADX 37, RVol 2.1) |

## Big prints this scan (402)
- **SPY** PUT 766 2026-11-16 (3DTE): 2,000 @ 8.50 = **+$1.7M** SELL | vol 8,018 / OI 116
- **SPY** CALL 760 2026-11-20 (7DTE): 1,498 @ 5.18 = **+$776k** BUY | vol 4,433 / OI 10,946
- **SPY** CALL 740 2026-11-20 (7DTE): 195 @ 20.00 = **+$390k** BUY | vol 276 / OI 3,832
- **SPY** PUT 761 2026-11-13 (0DTE): 700 @ 5.00 = **+$350k** SELL | vol 4,641 / OI 5,128
- **NVDA** PUT 167.5 2026-11-20 (7DTE): 350 @ 10.00 = **+$350k** SELL | vol 2,667 / OI 5,892
- **MSTR** PUT 106 2026-11-20 (7DTE): 1,000 @ 3.41 = **+$341k** BUY | vol 1,016 / OI 0
- **MU** PUT 780 2026-11-20 (7DTE): 100 @ 33.05 = **+$330k** BUY | vol 341 / OI 1,660
- **MU** CALL 790 2026-11-20 (7DTE): 100 @ 31.50 = **+$315k** BUY | vol 431 / OI 618
- **TSLA** PUT 397.5 2026-11-16 (3DTE): 200 @ 12.00 = **+$240k** BUY | vol 570 / OI 112
- **AMD** CALL 545 2026-11-13 (0DTE): 95 @ 23.27 = **+$221k** BUY | vol 139 / OI 635
- **GOOGL** CALL 307.5 2026-11-20 (7DTE): 500 @ 4.21 = **+$210k** BUY | vol 2,233 / OI 658
- **GOOGL** CALL 307.5 2026-11-20 (7DTE): 500 @ 4.21 = **+$210k** BUY | vol 2,233 / OI 658
- **SPY** PUT 759 2026-11-13 (0DTE): 567 @ 3.65 = **+$207k** SELL | vol 25,386 / OI 3,639
- **TSLA** PUT 387.5 2026-11-20 (7DTE): 200 @ 10.00 = **+$200k** BUY | vol 460 / OI 0
- **ORCL** PUT 125 2026-11-20 (7DTE): 468 @ 4.24 = **+$198k** SELL | vol 1,020 / OI 14,122

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 765 2026-11-16 (3DTE): 1,985 traded vs OI 1,797
- **SPY** PUT 743 2026-11-13 (0DTE): 3,852 traded vs OI 2,863
- **SPY** PUT 751 2026-11-16 (3DTE): 704 traded vs OI 556
- **SPY** CALL 756 2026-11-16 (3DTE): 1,030 traded vs OI 604
- **SPY** PUT 723 2026-11-16 (3DTE): 741 traded vs OI 674
- **SPY** PUT 755 2026-11-16 (3DTE): 3,384 traded vs OI 2,248
- **SPY** CALL 767 2026-11-13 (0DTE): 9,456 traded vs OI 5,873
- **SPY** PUT 761 2026-11-16 (3DTE): 838 traded vs OI 423
- **SPY** CALL 767 2026-11-16 (3DTE): 1,260 traded vs OI 1,168
- **SPY** CALL 757 2026-11-13 (0DTE): 7,961 traded vs OI 1,876
- **SPY** PUT 760 2026-11-16 (3DTE): 1,388 traded vs OI 1,327
- **SPY** PUT 746 2026-11-13 (0DTE): 4,227 traded vs OI 3,541
- **SPY** PUT 755 2026-11-13 (0DTE): 26,977 traded vs OI 24,184
- **SPY** CALL 762 2026-11-17 (4DTE): 557 traded vs OI 545
- **SPY** PUT 752 2026-11-16 (3DTE): 1,195 traded vs OI 793

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
