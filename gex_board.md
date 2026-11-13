# GEX + FLOW SCAN - Fri Nov 13, 09:50 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (2)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 09:45 | **UBER** | **CALLS** | TREND + FLOW | 11/13 70C | 0.59 | 0.35 | +0% (1m) | **-41%** | +32% | 70.7 |
| 09:45 | **ORCL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/13 127C | 0.46 | 0.23 | +22% (2m) | **-50%** | +48% | 126.38 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 09:50:08 ET, last candle SPY 09:49, QQQ 09:49 | no errors

## Flow surges NOT fired - price disagreed (5 today, last 5)
- 09:50 MSTR CALLS: under EMA 20 - flow says one way, price says the other
- 09:50 NFLX PUTS: price +0.86 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 GOOGL CALLS: price -2.39 over the last 15 min - flow says one way, price says the other
- 09:50 IWM CALLS: price -0.96 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 09:50 SPY CALLS: price -2.51 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **IWM** | 277.35 | FLOW SURGE | **CALLS** | 64 | 11/13 278C @ 0.58 (delta 0.38) = est +122% at 279 | NEG -$2.3B | 283.4 | 285 | 275 | +$2.1M | +$258k bull / +$0 bear | SHORT (clean 35, ADX 45, RVol 2.9) |
| 2 | **NFLX** | 63.81 | FLOW SURGE | **PUTS** | 64 | 11/13 64P @ 0.59 (delta 0.56) = est +27% at 63.39 | NEG -$2.6M | 63.84 | 64 | 65 | -$218k | +$0 bull / -$53k bear | out (clean 31, ADX 50, RVol 3.4) |
| 3 | **UBER** | 70.04 | TREND + FLOW | **CALLS** | 63 | none: 30 calls 0-7DTE > 3 priced 0.40-0.80 > 2 delta 0.2+ > 2 spread ok > 2 liquid > best one only +12% at the target (needs +20%) (26 contracts' greeks worked out here) | POS +$22.4M | 69.06 | 70 | 70 | +$71k | - | LONG (clean 33, ADX 34, RVol 2.9) |
| 4 | **AVGO** | 345.99 | FLOW SURGE | **CALLS** | 62 | none: 112 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (47 contracts' greeks worked out here) | POS +$93.7M | - | 350 | 340 | +$3.7M | +$191k bull / +$0 bear | SHORT (clean 34, ADX 26, RVol 2.9) |
| 5 | **BABA** | 94.66 | FLOW SURGE | **PUTS** | 61 | none: 30 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (30 contracts' greeks worked out here) | NEG -$19.2M | - | 100 | 95 | -$305k | +$0 bull / -$25k bear | out (clean 28, ADX 20, RVol 5.1) |
| 6 | **TSLA** | 393.61 | FLOW SURGE | **CALLS** | 60 | none: 128 calls 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (63 contracts' greeks worked out here) | POS +$422.4M | 380.37 | 400 | 380 | +$24.2M | +$3.5M bull / +$0 bear | out (clean 30, ADX 36, RVol 6.2) |
| 7 | **GOOGL** | 302.04 | FLOW SURGE | **CALLS** | 57 | 11/13 305C @ 0.60 (delta 0.24) = est +125% at 304.87 | POS +$217.9M | 292.22 | 300 | 290 | +$4.4M | +$1.8M bull / +$0 bear | out (clean 30, ADX 33, RVol 3.6) |
| 8 | **QQQ** | 683.11 | FLOW SURGE | **CALLS** | 56 | none: 732 calls 0-7DTE > 25 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (260 contracts' greeks worked out here) | NEG -$2.3B | 691.12 | 700 | 680 | +$33.5M | +$1.0M bull / +$0 bear | out (clean 31, ADX 37, RVol 2.5) |
| 9 | **MSFT** | 522.88 | FLOW SURGE | **PUTS** | 56 | none: 166 puts 0-7DTE > 10 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (80 contracts' greeks worked out here) | POS +$81.1M | 520.57 | 535 | 520 | -$4.5M | +$0 bull / -$909k bear | out (clean 32, ADX 45, RVol 2.2) |
| 10 | **DELL** | 348.85 | FLOW SURGE | **CALLS** | 56 | none: 56 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (53 contracts' greeks worked out here) | NEG -$8.6M | - | 360 | 360 | +$196k | +$62k bull / +$0 bear | out (clean 37, ADX 25, RVol 2.0) |
| 11 | **AAPL** | 359.71 | PINNED between the walls (positive gamma) - chop | **-** | 55 | - | POS +$1.3B | 348.1 | 360 | 360 | -$5.9M | +$470k bull / -$261k bear | out (clean 30, ADX 38, RVol 2.7) |
| 12 | **AMD** | 548.54 | FLOW SURGE | **CALLS** | 55 | none: 175 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (80 contracts' greeks worked out here) | POS +$154.7M | - | 550 | 550 | +$11.5M | +$4.8M bull / +$0 bear | SHORT (clean 35, ADX 28, RVol 2.2) |
| 13 | **MSTR** | 111.40 | FLOW SURGE | **CALLS** | 55 | 11/13 114C @ 0.45 (delta 0.23) = est +97% at 113.36 | NEG -$36.6M | - | 120 | 110 | +$1.0M | +$480k bull / +$0 bear | out (clean 29, ADX 30, RVol 4.6) |
| 14 | **SPY** | 755.62 | FLOW SURGE | **CALLS** | 54 | 11/13 759C @ 0.67 (delta 0.24) = est +216% at 760 | NEG -$6.6B | 761.45 | 760 | 760 | +$62.1M | +$4.6M bull / +$0 bear | out (clean 32, ADX 32, RVol 1.9) |
| 15 | **META** | 633.41 | FLOW SURGE | **PUTS** | 54 | none: 185 puts 0-7DTE > 10 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (84 contracts' greeks worked out here) | POS +$43.9M | 631.06 | 650 | 625 | -$6.1M | +$0 bull / -$446k bear | out (clean 29, ADX 38, RVol 2.4) |
| 16 | **HOOD** | 78.63 | TREND (flow not with it) | **PUTS** | 54 | 11/13 78P @ 0.74 (delta 0.40) = est +64% at 77.35 | NEG -$7.2M | 79.72 | 81 | 80 | +$205k | - | SHORT (clean 35, ADX 46, RVol 4.5) |
| 17 | **SMH** | 488.67 | FLOW SURGE | **CALLS** | 53 | none: 151 calls 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (69 contracts' greeks worked out here) | NEG -$246.1M | - | 500 | 475 | +$2.2M | +$401k bull / +$0 bear | out (clean 30, ADX 31, RVol 1.4) |
| 18 | **NVDA** | 162.28 | FLOW SURGE | **CALLS** | 50 | none: 60 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (29 contracts' greeks worked out here) | NEG -$262.3M | - | 175 | 160 | +$34.7M | +$4.6M bull / +$0 bear | out (clean 31, ADX 16, RVol 1.8) |
| 19 | **MU** | 782.31 | FLOW SURGE | **CALLS** | 46 | none: 156 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (72 contracts' greeks worked out here) | NEG -$7.2M | 784.1 | 800 | 800 | +$12.0M | +$6.8M bull / +$0 bear | out (clean 30, ADX 18, RVol 2.0) |
| 20 | **ARM** | 189.63 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 43 | none: 30 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (27 contracts' greeks worked out here) | POS +$524k | 189.09 | 200 | 190 | -$60k | - | out (clean 32, ADX 34, RVol 2.3) |
| 21 | **PLTR** | 170.06 | PINNED between the walls (positive gamma) - chop | **-** | 38 | - | POS +$94.8M | 163.7 | 170 | 170 | +$171k | - | out (clean 29, ADX 26, RVol 2.1) |
| 22 | **AMZN** | 268.49 | - | **-** | 29 | - | POS +$556.3M | 253.83 | 270 | 265 | -$689k | +$0 bull / -$123k bear | out (clean 30, ADX 35, RVol 2.1) |
| 23 | **ORCL** | 123.92 | - | **-** | 29 | - | POS +$3.6M | 121.22 | 130 | 125 | +$255k | - | out (clean 31, ADX 26, RVol 2.4) |
| 24 | **SHOP** | 149.78 | PINNED between the walls (positive gamma) - chop | **-** | 29 | - | POS +$7.1M | 145.5 | 150 | 150 | +$745 | - | out (clean 32, ADX 32, RVol 1.8) |
| 25 | **SMCI** | 26.36 | - | **-** | 27 | - | NEG -$2.5M | - | 27 | 25 | +$79k | - | out (clean 34, ADX 24, RVol 3.0) |
| 26 | **CRM** | 218.28 | - | **-** | 27 | - | NEG -$6.5M | 223.55 | 220 | 220 | +$38k | - | out (clean 30, ADX 28, RVol 3.0) |
| 27 | **COIN** | 128.81 | - | **-** | 22 | - | NEG -$13.7M | 132.02 | 137 | 130 | -$15k | +$36k bull / -$31k bear | out (clean 31, ADX 37, RVol 3.0) |

## Big prints this scan (460)
- **SPY** PUT 766 2026-11-16 (3DTE): 1,588 @ 8.00 = **+$1.3M** SELL | vol 8,017 / OI 116
- **SPY** PUT 766 2026-11-16 (3DTE): 1,803 @ 7.00 = **+$1.3M** SELL | vol 8,017 / OI 116
- **SPY** PUT 766 2026-11-16 (3DTE): 1,324 @ 7.45 = **+$986k** SELL | vol 8,017 / OI 116
- **GOOGL** CALL 290 2026-11-20 (7DTE): 499 @ 16.50 = **+$823k** BUY | vol 519 / OI 4,873
- **MU** PUT 790 2026-11-20 (7DTE): 150 @ 30.95 = **+$464k** SELL | vol 166 / OI 1,598
- **SPY** PUT 766 2026-11-16 (3DTE): 575 @ 7.45 = **+$428k** SELL | vol 8,017 / OI 116
- **NVDA** PUT 167.5 2026-11-20 (7DTE): 484 @ 8.10 = **+$392k** SELL | vol 2,145 / OI 5,892
- **AMD** CALL 565 2026-11-13 (0DTE): 339 @ 10.91 = **+$370k** BUY | vol 1,802 / OI 2,898
- **NVDA** PUT 167.5 2026-11-20 (7DTE): 435 @ 8.10 = **+$352k** SELL | vol 2,145 / OI 5,892
- **MU** PUT 810 2026-11-18 (5DTE): 84 @ 40.50 = **+$340k** SELL | vol 85 / OI 74
- **SPY** PUT 761 2026-11-19 (6DTE): 428 @ 6.38 = **+$273k** SELL | vol 500 / OI 98
- **MSTR** PUT 108 2026-11-20 (7DTE): 750 @ 3.61 = **+$271k** SELL | vol 1,005 / OI 0
- **NVDA** PUT 167.5 2026-11-20 (7DTE): 287 @ 8.65 = **+$248k** SELL | vol 2,145 / OI 5,892
- **NVDA** PUT 160 2026-11-20 (7DTE): 477 @ 4.88 = **+$233k** SELL | vol 1,245 / OI 37,700
- **AMD** CALL 565 2026-11-13 (0DTE): 200 @ 11.62 = **+$232k** BUY | vol 1,802 / OI 2,898

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 786 2026-11-17 (4DTE): 596 traded vs OI 266
- **SPY** CALL 758 2026-11-16 (3DTE): 590 traded vs OI 511
- **SPY** PUT 754 2026-11-16 (3DTE): 622 traded vs OI 506
- **SPY** CALL 761 2026-11-16 (3DTE): 659 traded vs OI 548
- **SPY** CALL 761 2026-11-13 (0DTE): 11,955 traded vs OI 7,452
- **SPY** CALL 769 2026-11-13 (0DTE): 5,868 traded vs OI 5,074
- **SPY** CALL 766 2026-11-13 (0DTE): 9,482 traded vs OI 6,705
- **SPY** CALL 765 2026-11-13 (0DTE): 14,286 traded vs OI 11,608
- **SPY** CALL 760 2026-11-13 (0DTE): 13,865 traded vs OI 12,801
- **SPY** CALL 762 2026-11-13 (0DTE): 14,645 traded vs OI 9,105
- **SPY** CALL 759 2026-11-16 (3DTE): 2,001 traded vs OI 862
- **SPY** CALL 760 2026-11-16 (3DTE): 2,649 traded vs OI 1,563
- **SPY** PUT 723 2026-11-13 (0DTE): 2,521 traded vs OI 1,597
- **SPY** PUT 758 2026-11-13 (0DTE): 22,651 traded vs OI 5,357
- **SPY** PUT 753 2026-11-13 (0DTE): 12,124 traded vs OI 8,787

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
