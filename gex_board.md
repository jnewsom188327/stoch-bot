# GEX + FLOW SCAN - Wed Nov 11, 09:50 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (5)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 09:50 | **GOOGL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/11 292.5C | 0.51 | 0.48 | -6% (0m) | **-6%** | +82% | 291.86 |
| 09:45 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/11 282C | 0.68 | 0.98 | +44% (5m) | **+44%** | +68% | 282.96 |
| 09:45 | **QQQ** | **CALLS** | FLOW SURGE | 11/11 690C | 0.63 | 0.40 | +13% (1m) | **-37%** | +171% | 689.78 |
| 09:39 | **QQQ** | **CALLS** | 1m WHIPSAW (R1 R5) | 11/11 693C | 0.52 | 0.13 | -10% (0m) | **-75%** | +92% | 690.43 |
| 09:39 | **SPY** | **CALLS** | 1m WHIPSAW (R1 R5) | 11/11 760C | 0.53 | 0.24 | -2% (0m) | **-55%** | +79% | 758.82 |

## 1m RULES on SPY / QQQ - loose (2 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 09:50:08 ET, last candle SPY 09:49, QQQ 09:49 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 09:38 | QQQ | 1m WHIPSAW | R1 R5 | CALLS | TURNING away | **FIRE** QQQ261111C00693000 |
| 09:38 | SPY | 1m WHIPSAW | R1 R5 | CALLS | TURNING away | **FIRE** SPY261111C00760000 |

## Flow surges NOT fired - price disagreed (3 today, last 5)
- 09:50 MSFT CALLS: price -2.01 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 09:50 NVDA CALLS: price -1.77 over the last 15 min - flow says one way, price says the other
- 09:50 SPY CALLS: price -1.00 over the last 15 min - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **AVGO** | 350.67 | TREND + FLOW | **CALLS** | 67 | none: 112 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (55 contracts' greeks worked out here) | POS +$100.9M | - | 350 | 340 | +$3.8M | +$1.0M bull / -$234k bear | LONG (clean 34, ADX 42, RVol 3.5) |
| 2 | **SMH** | 498.35 | FLOW SURGE | **CALLS** | 60 | none: 160 calls 0-7DTE > 11 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (71 contracts' greeks worked out here) | NEG -$77.5M | - | 500 | 475 | +$1.1M | +$615k bull / +$0 bear | out (clean 30, ADX 29, RVol 2.9) |
| 3 | **GOOGL** | 289.95 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 60 | 11/11 292.5C @ 0.51 (delta 0.24) = est +82% at 291.86 | POS +$22.2M | 288.89 | 300 | 290 | +$847k | +$447k bull / +$0 bear | out (clean 29, ADX 34, RVol 2.0) |
| 4 | **MU** | 776.18 | FLOW SURGE | **PUTS** | 58 | none: 169 puts 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (72 contracts' greeks worked out here) | POS +$135.7M | - | 800 | 800 | -$34.3M | +$964k bull / -$6.6M bear | out (clean 32, ADX 40, RVol 2.5) |
| 5 | **PLTR** | 173.00 | FLOW SURGE | **CALLS** | 53 | none: 14 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$75.3M | - | 170 | 180 | +$1.0M | +$333k bull / +$0 bear | out (clean 29, ADX 42, RVol 2.2) |
| 6 | **DELL** | 362.00 | TREND (flow not with it) | **CALLS** | 52 | none: 29 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$2.1M | - | 350 | 340 | -$72k | +$94k bull / +$0 bear | LONG (clean 34, ADX 38, RVol 2.8) |
| 7 | **AAPL** | 353.69 | FLOW SURGE | **PUTS** | 51 | none: 109 puts 0-7DTE > 8 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (56 contracts' greeks worked out here) | POS +$1.3B | 340.87 | 355 | 350 | -$5.0M | +$25k bull / -$360k bear | out (clean 28, ADX 33, RVol 2.6) |
| 8 | **MSFT** | 530.39 | FLOW SURGE | **CALLS** | 51 | 11/11 535C @ 0.70 (delta 0.21) = est +164% at 535 | POS +$286.2M | 514.43 | 550 | 520 | +$1.7M | +$448k bull / +$0 bear | out (clean 31, ADX 19, RVol 2.5) |
| 9 | **AMZN** | 269.14 | FLOW SURGE | **CALLS** | 50 | none: 88 calls 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (35 contracts' greeks worked out here) | POS +$512.6M | - | 270 | 265 | +$797k | +$90k bull / +$0 bear | out (clean 34, ADX 33, RVol 2.1) |
| 10 | **SPY** | 755.70 | FLOW SURGE | **CALLS** | 49 | 11/11 759C @ 0.46 (delta 0.20) = est +286% at 760 | NEG -$4.5B | 761.09 | 760 | 750 | +$24.9M | +$4.0M bull / +$0 bear | out (clean 32, ADX 43, RVol 1.8) |
| 11 | **COIN** | 135.14 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 49 | none: 27 calls 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$17.6M | - | 141 | 135 | -$79k | - | out (clean 28, ADX 30, RVol 1.6) |
| 12 | **QQQ** | 684.64 | FLOW SURGE | **CALLS** | 48 | 11/11 689C @ 0.70 (delta 0.22) = est +213% at 689.62 | NEG -$1.1B | 689.62 | 700 | 680 | +$29.7M | +$3.1M bull / +$0 bear | out (clean 32, ADX 42, RVol 1.6) |
| 13 | **NVDA** | 172.09 | FLOW SURGE | **CALLS** | 48 | 11/11 175C @ 0.56 (delta 0.24) = est +148% at 175 | NEG -$176.5M | - | 180 | 170 | +$10.6M | +$3.9M bull / +$0 bear | out (clean 34, ADX 23, RVol 2.0) |
| 14 | **MSTR** | 122.53 | FLOW SURGE | **PUTS** | 46 | none: 24 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$1.3M | 121.64 | 133 | 120 | -$611k | +$0 bull / -$192k bear | out (clean 29, ADX 17, RVol 2.4) |
| 15 | **IWM** | 282.25 | TREND (flow not with it) | **CALLS** | 44 | 11/11 283C @ 0.63 (delta 0.38) = est +29% at 283 | NEG -$208.0M | 283.14 | 285 | 270 | -$1.3M | - | LONG (clean 34, ADX 32, RVol 1.8) |
| 16 | **SMCI** | 29.46 | - | **-** | 39 | - | POS +$9.8M | - | 30 | 30 | -$182k | +$33k bull / +$0 bear | out (clean 31, ADX 32, RVol 2.0) |
| 17 | **CRM** | 215.52 | - | **-** | 30 | - | NEG -$11.1M | - | 230 | 220 | -$19k | - | out (clean 31, ADX 28, RVol 3.1) |
| 18 | **TSLA** | 387.48 | - | **-** | 28 | - | POS +$363.4M | - | 400 | 380 | +$8.2M | +$5.2M bull / -$749k bear | out (clean 32, ADX 29, RVol 2.0) |
| 19 | **NFLX** | 63.56 | - | **-** | 26 | - | NEG -$12.4M | 64.56 | 65 | 65 | -$84k | - | out (clean 28, ADX 22, RVol 2.1) |
| 20 | **AMD** | 526.45 | - | **-** | 24 | - | POS +$113.7M | - | 500 | 500 | -$3.1M | +$4.8M bull / -$548k bear | out (clean 33, ADX 26, RVol 2.4) |
| 21 | **ORCL** | 125.67 | - | **-** | 24 | - | NEG -$1.8M | 128.08 | 130 | 125 | +$214k | +$0 bull / -$183k bear | out (clean 27, ADX 33, RVol 2.4) |
| 22 | **BABA** | 101.58 | - | **-** | 22 | - | NEG -$15.4M | 107.13 | 110 | 101 | +$34k | - | out (clean 30, ADX 24, RVol 2.1) |
| 23 | **META** | 638.43 | - | **-** | 21 | - | POS +$231.0M | 622.79 | 650 | 625 | -$83k | +$340k bull / +$0 bear | out (clean 31, ADX 32, RVol 2.4) |
| 24 | **SHOP** | 148.57 | - | **-** | 21 | - | POS +$3.4M | 143.75 | 150 | 140 | -$4k | - | out (clean 33, ADX 42, RVol 1.6) |
| 25 | **HOOD** | 82.77 | - | **-** | 13 | - | POS +$9.3M | 78.74 | 85 | 80 | +$16k | - | out (clean 32, ADX 26, RVol 2.7) |
| 26 | **ARM** | 190.12 | - | **-** | 13 | - | POS +$203k | 190.4 | 200 | 200 | -$6k | - | out (clean 28, ADX 44, RVol 1.7) |
| 27 | **UBER** | 69.35 | - | **-** | 9 | - | POS +$8.1M | 68.3 | 70 | 70 | +$202 | - | out (clean 34, ADX 24, RVol 2.2) |

## Big prints this scan (566)
- **AMD** PUT 550 2026-11-11 (0DTE): 748 @ 16.00 = **+$1.2M** SELL | vol 1,112 / OI 8
- **SPY** CALL 754 2026-11-12 (1DTE): 1,224 @ 4.80 = **+$588k** BUY | vol 2,974 / OI 623
- **SPY** CALL 755 2026-11-11 (0DTE): 1,841 @ 2.95 = **+$543k** BUY | vol 10,374 / OI 1,849
- **MU** CALL 780 2026-11-11 (0DTE): 497 @ 8.80 = **+$437k** BUY | vol 2,934 / OI 2,052
- **AMD** PUT 550 2026-11-11 (0DTE): 195 @ 16.00 = **+$312k** SELL | vol 1,112 / OI 8
- **AVGO** CALL 340 2026-11-13 (2DTE): 200 @ 15.00 = **+$300k** BUY | vol 477 / OI 2,541
- **SPY** CALL 754 2026-11-13 (2DTE): 467 @ 6.13 = **+$286k** BUY | vol 2,773 / OI 2,281
- **SPY** PUT 757 2026-11-12 (1DTE): 913 @ 2.96 = **+$270k** SELL | vol 2,473 / OI 375
- **QQQ** CALL 671 2026-11-13 (2DTE): 150 @ 18.00 = **+$270k** BUY | vol 174 / OI 1,057
- **PLTR** CALL 170 2026-11-13 (2DTE): 426 @ 6.15 = **+$262k** BUY | vol 1,080 / OI 12,901
- **QQQ** CALL 675 2026-11-11 (0DTE): 200 @ 12.82 = **+$256k** BUY | vol 875 / OI 1,701
- **TSLA** CALL 390 2026-11-11 (0DTE): 500 @ 4.85 = **+$242k** BUY | vol 20,456 / OI 2,864
- **SPY** CALL 759 2026-11-12 (1DTE): 1,224 @ 1.96 = **+$240k** BUY | vol 4,086 / OI 592
- **QQQ** CALL 676 2026-11-11 (0DTE): 200 @ 11.87 = **+$237k** BUY | vol 769 / OI 319
- **SPY** CALL 755 2026-11-11 (0DTE): 785 @ 2.95 = **+$232k** BUY | vol 10,374 / OI 1,849

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 767 2026-11-11 (0DTE): 5,405 traded vs OI 2,443
- **SPY** CALL 757 2026-11-12 (1DTE): 1,605 traded vs OI 746
- **SPY** CALL 761 2026-11-13 (2DTE): 2,850 traded vs OI 2,437
- **SPY** CALL 754 2026-11-13 (2DTE): 2,773 traded vs OI 2,281
- **SPY** CALL 752 2026-11-11 (0DTE): 2,055 traded vs OI 1,930
- **SPY** CALL 754 2026-11-11 (0DTE): 2,434 traded vs OI 989
- **SPY** CALL 762 2026-11-12 (1DTE): 1,772 traded vs OI 693
- **SPY** CALL 756 2026-11-12 (1DTE): 622 traded vs OI 493
- **SPY** CALL 800 2026-11-16 (5DTE): 600 traded vs OI 505
- **SPY** PUT 750 2026-11-11 (0DTE): 8,712 traded vs OI 3,845
- **SPY** PUT 754 2026-11-12 (1DTE): 932 traded vs OI 468
- **SPY** CALL 769 2026-11-11 (0DTE): 1,879 traded vs OI 1,501
- **SPY** CALL 751 2026-11-11 (0DTE): 1,338 traded vs OI 869
- **SPY** CALL 766 2026-11-11 (0DTE): 2,569 traded vs OI 1,990
- **SPY** PUT 743 2026-11-11 (0DTE): 1,053 traded vs OI 983

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
