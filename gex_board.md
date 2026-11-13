# GEX + FLOW SCAN - Fri Nov 13, 10:30 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (8)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:17 | **QQQ** | **CALLS** | 1m WHIPSAW (R1 R2) | 11/13 683C | 0.75 | 0.58 | -1% (0m) | **-23%** | +60% | 678.58 |
| 10:15 | **ARM** | **PUTS** | FLIP CROSS down into negative gamma | 11/13 182.5P | 0.74 | 0.79 | +65% (7m) | **+7%** | +96% | 183.6 |
| 10:15 | **ORCL** | **CALLS** | FLIP CROSS up into positive gamma | 11/13 124C | 0.65 | 0.78 | +32% (14m) | **+20%** | +66% | 123.68 |
| 10:10 | **ORCL** | **PUTS** | FLIP CROSS down into negative gamma | 11/13 120P | 0.46 | 0.17 | +7% (5m) | **-63%** | +63% | 121.25 |
| 10:05 | **GOOGL** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/13 297.5P | 0.74 | 2.53 | +332% (18m) | **+242%** | +288% | 295 hit |
| 09:55 | **BABA** | **PUTS** | FLOW SURGE | 11/13 94P | 0.51 | 0.49 | +0% (31m) | **-4%** | +49% | 93.36 |
| 09:45 | **UBER** | **CALLS** | TREND + FLOW | 11/13 70C | 0.59 | 0.07 | +0% (1m) | **-88%** | +32% | 70.7 |
| 09:45 | **ORCL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/13 127C | 0.46 | 0.13 | +22% (2m) | **-72%** | +48% | 126.38 |

## 1m RULES on SPY / QQQ - loose (1 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:30:08 ET, last candle SPY 10:29, QQQ 10:29 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 10:16 | QQQ | 1m WHIPSAW | R1 R2 | CALLS | TURNING your way | **FIRE** QQQ261113C00683000 |

## Flow surges NOT fired - price disagreed (36 today, last 5)
- 10:30 HOOD CALLS: price +0.00 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:30 MSTR CALLS: price -0.30 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:30 COIN CALLS: price -0.66 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:30 PLTR CALLS: under EMA 20 - flow says one way, price says the other
- 10:30 SPY CALLS: under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **DELL** | 341.89 | FLOW SURGE | **CALLS** | 59 | none: 54 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (48 contracts' greeks worked out here) | NEG -$7.6M | - | 360 | 340 | +$7.9M | +$414k bull / +$0 bear | SHORT (clean 38, ADX 45, RVol 1.7) |
| 2 | **HOOD** | 77.47 | FLOW SURGE | **CALLS** | 59 | 11/13 78C @ 0.52 (delta 0.39) = est +288% at 80 | NEG -$12.8M | 80.16 | 81 | 80 | +$2.1M | +$675k bull / +$0 bear | SHORT (clean 36, ADX 60, RVol 2.2) |
| 3 | **COIN** | 126.75 | FLOW SURGE | **CALLS** | 58 | 11/13 128C @ 0.66 (delta 0.34) = est +236% at 130 | NEG -$18.6M | 133.66 | 137 | 130 | +$3.3M | +$1.3M bull / +$0 bear | out (clean 31, ADX 46, RVol 2.2) |
| 4 | **QQQ** | 675.50 | FLOW SURGE | **CALLS** | 53 | none: 750 calls 0-7DTE > 27 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (244 contracts' greeks worked out here) | NEG -$3.0B | 691.08 | 680 | 680 | +$328.1M | +$5.6M bull / -$620k bear | out (clean 32, ADX 54, RVol 1.8) |
| 5 | **IWM** | 275.64 | FLOW SURGE | **CALLS** | 52 | none: 321 calls 0-7DTE > 13 priced 0.40-0.80 > 7 delta 0.2+ > 7 spread ok > 7 liquid > best one only +10% at the target (needs +20%) (163 contracts' greeks worked out here) | NEG -$2.7B | 282.88 | 285 | 275 | +$19.0M | +$881k bull / -$57k bear | SHORT (clean 36, ADX 54, RVol 1.3) |
| 6 | **PLTR** | 166.15 | FLOW SURGE | **CALLS** | 52 | 11/13 167.5C @ 0.58 (delta 0.32) = est +152% at 168.46 | POS +$74.6M | 162.39 | 165 | 165 | +$3.5M | +$217k bull / +$0 bear | out (clean 29, ADX 43, RVol 2.2) |
| 7 | **GOOGL** | 296.02 | FLOW SURGE | **CALLS** | 51 | none: 94 calls 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (45 contracts' greeks worked out here) | POS +$195.5M | 290.48 | 300 | 290 | +$16.0M | +$1.3M bull / +$0 bear | out (clean 30, ADX 30, RVol 2.2) |
| 8 | **SMH** | 480.77 | FLOW SURGE | **CALLS** | 50 | none: 142 calls 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (73 contracts' greeks worked out here) | NEG -$296.2M | - | 500 | 475 | +$9.0M | +$1.7M bull / -$306k bear | out (clean 31, ADX 50, RVol 1.7) |
| 9 | **AMD** | 534.82 | FLOW SURGE | **CALLS** | 50 | none: 171 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (82 contracts' greeks worked out here) | POS +$78.8M | - | 550 | 550 | +$66.6M | +$6.4M bull / -$2.6M bear | SHORT (clean 35, ADX 49, RVol 1.9) |
| 10 | **AVGO** | 343.76 | FLOW SURGE | **CALLS** | 49 | none: 112 calls 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (47 contracts' greeks worked out here) | POS +$73.2M | 330.35 | 340 | 340 | +$18.4M | +$202k bull / +$0 bear | SHORT (clean 35, ADX 44, RVol 1.1) |
| 11 | **MSTR** | 109.64 | FLOW SURGE | **CALLS** | 49 | 11/13 111C @ 0.58 (delta 0.32) = est +116% at 111.61 | NEG -$39.1M | - | 110 | 110 | +$5.8M | +$2.4M bull / +$0 bear | out (clean 30, ADX 41, RVol 1.6) |
| 12 | **SPY** | 750.11 | FLOW SURGE | **CALLS** | 47 | 11/13 754C @ 0.76 (delta 0.24) = est +109% at 753.55 | NEG -$8.9B | 761.13 | 750 | 750 | +$323.4M | +$5.8M bull / -$412k bear | out (clean 33, ADX 40, RVol 1.3) |
| 13 | **TSLA** | 387.94 | FLOW SURGE | **CALLS** | 45 | none: 124 calls 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (59 contracts' greeks worked out here) | POS +$329.4M | - | 400 | 380 | +$70.6M | +$3.6M bull / -$788k bear | out (clean 29, ADX 25, RVol 2.1) |
| 14 | **NVDA** | 160.27 | FLOW SURGE | **CALLS** | 41 | none: 64 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (28 contracts' greeks worked out here) | NEG -$261.0M | - | 175 | 160 | +$100.1M | +$4.6M bull / -$1.6M bear | out (clean 31, ADX 15, RVol 1.2) |
| 15 | **MSFT** | 521.75 | FLIP CROSS up into positive gamma | **CALLS** | 41 | none: 166 calls 0-7DTE > 8 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (74 contracts' greeks worked out here) | POS +$35.5M | 520.61 | 535 | 520 | +$516k | +$173k bull / -$274k bear | out (clean 32, ADX 40, RVol 1.9) |
| 16 | **AMZN** | 266.01 | FLOW SURGE | **CALLS** | 38 | 11/13 267.5C @ 0.69 (delta 0.32) = est +281% at 270 | POS +$451.7M | 252.43 | 270 | 265 | +$5.8M | +$1.1M bull / +$0 bear | out (clean 29, ADX 32, RVol 0.9) |
| 17 | **MU** | 764.97 | - | **-** | 29 | - | NEG -$15.3M | 772.44 | 800 | 750 | +$72.9M | +$12.1M bull / -$2.8M bear | out (clean 31, ADX 35, RVol 1.8) |
| 18 | **ORCL** | 123.49 | - | **-** | 29 | - | NEG -$3.8M | 123.88 | 125 | 125 | +$1.2M | +$35k bull / -$168k bear | out (clean 31, ADX 42, RVol 2.0) |
| 19 | **AAPL** | 357.96 | - | **-** | 25 | - | POS +$1.2B | 347.71 | 360 | 360 | +$12.5M | +$2.6M bull / -$167k bear | out (clean 30, ADX 32, RVol 1.2) |
| 20 | **META** | 628.08 | - | **-** | 25 | - | NEG -$59.3M | 631.45 | 630 | 625 | +$6.8M | +$2.2M bull / +$0 bear | out (clean 29, ADX 37, RVol 3.1) |
| 21 | **UBER** | 69.22 | - | **-** | 23 | - | POS +$9.0M | 68.79 | 70 | 70 | +$250k | - | out (clean 33, ADX 25, RVol 0.3) |
| 22 | **NFLX** | 62.97 | - | **-** | 22 | - | NEG -$22.7M | 63.58 | 65 | 60 | +$38k | +$38k bull / +$0 bear | out (clean 31, ADX 35, RVol 2.8) |
| 23 | **SMCI** | 26.39 | - | **-** | 22 | - | NEG -$2.7M | - | 27 | 25 | +$304k | - | out (clean 34, ADX 30, RVol 1.2) |
| 24 | **ARM** | 187.52 | - | **-** | 22 | - | NEG -$1.4M | 189.27 | 190 | 190 | -$139k | +$62k bull / +$0 bear | out (clean 32, ADX 53, RVol 1.0) |
| 25 | **CRM** | 216.62 | - | **-** | 15 | - | NEG -$6.8M | 220.07 | 220 | 220 | +$71k | - | out (clean 29, ADX 25, RVol 1.0) |
| 26 | **SHOP** | 146.41 | - | **-** | 8 | - | POS +$3.7M | 144.55 | 150 | 140 | +$7k | - | out (clean 31, ADX 30, RVol 0.9) |
| 27 | **BABA** | 93.90 | - | **-** | 6 | - | NEG -$15.9M | - | 100 | 95 | +$25k | - | out (clean 28, ADX 24, RVol 0.8) |

## Big prints this scan (337)
- **COIN** CALL 131 2026-11-20 (7DTE): 2,999 @ 3.71 = **+$1.1M** BUY | vol 3,143 / OI 20
- **MSTR** CALL 114 2026-11-20 (7DTE): 2,999 @ 3.47 = **+$1.0M** BUY | vol 5,074 / OI 0
- **MSTR** CALL 114 2026-11-20 (7DTE): 2,000 @ 3.47 = **+$694k** BUY | vol 5,074 / OI 0
- **NVDA** PUT 160 2026-11-16 (3DTE): 2,142 @ 3.20 = **+$685k** BUY | vol 23,798 / OI 4,240
- **MU** PUT 750 2026-11-20 (7DTE): 198 @ 29.20 = **+$578k** BUY | vol 1,234 / OI 6,865
- **AMZN** CALL 255 2026-11-13 (0DTE): 300 @ 11.68 = **+$350k** BUY | vol 361 / OI 2,369
- **QQQ** PUT 665 2026-11-20 (7DTE): 450 @ 7.56 = **+$340k** SELL | vol 4,431 / OI 10,430
- **AMZN** CALL 260 2026-11-20 (7DTE): 300 @ 9.68 = **+$290k** BUY | vol 4,728 / OI 15,661
- **QQQ** PUT 680 2026-11-13 (0DTE): 492 @ 5.12 = **+$252k** SELL | vol 74,597 / OI 11,590
- **QQQ** PUT 675 2026-11-13 (0DTE): 725 @ 3.37 = **+$244k** BUY | vol 65,491 / OI 7,712
- **AMD** CALL 515 2026-11-16 (3DTE): 100 @ 24.02 = **+$240k** SELL | vol 122 / OI 146
- **SPY** PUT 730 2026-11-20 (7DTE): 1,000 @ 2.37 = **+$237k** SELL | vol 7,745 / OI 64,657
- **SPY** PUT 750 2026-11-13 (0DTE): 1,000 @ 2.23 = **+$223k** SELL | vol 151,868 / OI 11,683
- **AMD** CALL 517.5 2026-11-16 (3DTE): 100 @ 22.13 = **+$221k** SELL | vol 104 / OI 32
- **SPY** PUT 756 2026-11-13 (0DTE): 324 @ 6.79 = **+$220k** BUY | vol 77,744 / OI 4,364

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 750 2026-11-13 (0DTE): 10,127 traded vs OI 8,929
- **SPY** CALL 748 2026-11-13 (0DTE): 2,221 traded vs OI 1,992
- **SPY** PUT 762 2026-11-16 (3DTE): 543 traded vs OI 296
- **SPY** PUT 724 2026-11-16 (3DTE): 557 traded vs OI 505
- **SPY** CALL 751 2026-11-16 (3DTE): 852 traded vs OI 674
- **SPY** PUT 740 2026-11-13 (0DTE): 37,210 traded vs OI 18,409
- **SPY** CALL 774 2026-11-13 (0DTE): 3,515 traded vs OI 3,030
- **SPY** PUT 715 2026-11-18 (5DTE): 1,564 traded vs OI 984
- **SPY** PUT 731 2026-11-13 (0DTE): 4,916 traded vs OI 4,539
- **SPY** PUT 730 2026-11-16 (3DTE): 2,009 traded vs OI 1,629
- **SPY** PUT 728 2026-11-13 (0DTE): 2,962 traded vs OI 2,910
- **SPY** PUT 734 2026-11-13 (0DTE): 5,180 traded vs OI 2,829
- **SPY** PUT 729 2026-11-13 (0DTE): 4,579 traded vs OI 4,015
- **SPY** PUT 742 2026-11-16 (3DTE): 3,579 traded vs OI 2,682
- **SPY** PUT 750 2026-11-23 (10DTE): 1,622 traded vs OI 933

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
