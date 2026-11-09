# GEX + FLOW SCAN - Mon Nov 09, 11:20 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (4)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:04 | **SPY** | **CALLS** | 1m WHIPSAW (R1) | 11/09 754C | 0.41 | 0.24 | -2% (0m) | **-41%** | +28% | 752.23 |
| 10:35 | **AMZN** | **CALLS** | TREND + FLOW | 11/09 272.5C | 0.49 | 0.09 | +2% (2m) | **-82%** | +225% | 273.49 |
| 10:00 | **MSFT** | **CALLS** | TREND + FLOW | 11/09 545C | 0.77 | 0.72 | +51% (23m) | **-6%** (done) | +545% | 550 |
| 10:00 | **AMZN** | **CALLS** | TREND + FLOW | 11/09 275C | 0.48 | 0.02 | +13% (6m) | **-96%** (done) | +258% | 275.95 |

## 1m RULES on SPY / QQQ - loose (1 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 11:20:08 ET, last candle SPY 11:19, QQQ 11:19 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 11:03 | SPY | 1m WHIPSAW | R1 | CALLS | TURNING away | **FIRE** SPY261109C00754000 |

## Flow surges NOT fired - price disagreed (17 today, last 5)
- 10:55 AVGO PUTS: price +2.40 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:40 AVGO PUTS: price +1.16 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:40 QQQ PUTS: price +0.45 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:35 AVGO PUTS: price +1.05 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:30 QQQ PUTS: price +0.53 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **IWM** | 281.04 | FLOW SURGE | **PUTS** | 43 | 11/09 281P @ 0.67 (delta 0.49) = est +66% at 280.01 | NEG -$1.0B | 285.12 | 285 | 270 | -$19.3M | +$0 bull / -$252k bear | out (clean 34, ADX 57, RVol 0.7) |
| 2 | **MSFT** | 539.65 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 40 | 11/09 542.5C @ 0.62 (delta 0.25) = est +162% at 543.13 | POS +$541.2M | - | 550 | 540 | +$3.7M | +$134k bull / +$0 bear | out (clean 34, ADX 31, RVol 0.5) |
| 3 | **META** | 639.31 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 39 | none: 204 calls 0-7DTE > 8 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (76 contracts' greeks worked out here) | POS +$163.2M | 613.69 | 650 | 640 | -$5.9M | +$161k bull / -$173k bear | out (clean 33, ADX 41, RVol 0.5) |
| 4 | **AAPL** | 350.02 | PINNED between the walls (positive gamma) - chop | **-** | 35 | - | POS +$437.0M | 338.48 | 350 | 350 | -$7.3M | +$124k bull / -$38k bear | out (clean 28, ADX 42, RVol 0.5) |
| 5 | **MU** | 736.95 | FLIP CROSS down into negative gamma | **PUTS** | 35 | none: 191 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (70 contracts' greeks worked out here) | NEG -$6.9M | 741.28 | 750 | 750 | -$22.4M | +$2.9M bull / -$4.2M bear | out (clean 33, ADX 50, RVol 0.7) |
| 6 | **AMZN** | 268.00 | FLOW SURGE | **CALLS** | 33 | none: 84 calls 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (32 contracts' greeks worked out here) | POS +$366.7M | - | 270 | 265 | +$20.9M | +$277k bull / +$0 bear | out (clean 35, ADX 24, RVol 0.7) |
| 7 | **AVGO** | 319.51 | - | **-** | 31 | - | NEG -$67.6M | - | 340 | 320 | -$7.6M | +$656k bull / -$318k bear | out (clean 31, ADX 69, RVol 1.7) |
| 8 | **TSLA** | 378.13 | - | **-** | 30 | - | POS +$117.6M | - | 380 | 380 | -$94.6M | +$1.4M bull / +$0 bear | out (clean 34, ADX 47, RVol 0.6) |
| 9 | **AMD** | 501.90 | - | **-** | 30 | - | POS +$16.9M | 489.26 | 500 | 500 | -$55.7M | +$1.7M bull / -$2.8M bear | out (clean 33, ADX 59, RVol 1.7) |
| 10 | **SMH** | 483.89 | - | **-** | 29 | - | NEG -$237.6M | - | 500 | 475 | -$2.9M | +$555k bull / +$0 bear | out (clean 32, ADX 47, RVol 1.7) |
| 11 | **SPY** | 750.21 | - | **-** | 28 | - | NEG -$6.8B | 761.87 | 750 | 740 | -$228.2M | +$7.8M bull / +$0 bear | out (clean 33, ADX 52, RVol 0.9) |
| 12 | **QQQ** | 676.03 | - | **-** | 28 | - | NEG -$2.3B | 699.91 | 680 | 680 | -$224.4M | +$3.8M bull / -$242k bear | out (clean 33, ADX 50, RVol 0.8) |
| 13 | **PLTR** | 170.00 | - | **-** | 28 | - | POS +$10.9M | - | 165 | 180 | -$4.2M | +$0 bull / -$455k bear | out (clean 30, ADX 53, RVol 0.9) |
| 14 | **NVDA** | 176.58 | - | **-** | 27 | - | NEG -$195.6M | - | 190 | 190 | -$47.1M | +$2.3M bull / +$0 bear | out (clean 32, ADX 40, RVol 4.2) |
| 15 | **HOOD** | 84.42 | - | **-** | 27 | - | NEG -$1.5M | - | 85 | 85 | -$2.8M | +$169k bull / +$0 bear | out (clean 31, ADX 58, RVol 0.7) |
| 16 | **SMCI** | 29.29 | - | **-** | 25 | - | NEG -$36k | - | 30 | 30 | -$890k | +$30k bull / +$0 bear | out (clean 31, ADX 14, RVol 0.7) |
| 17 | **COIN** | 137.90 | - | **-** | 23 | - | NEG -$6.3M | - | 140 | 135 | -$2.3M | - | out (clean 32, ADX 29, RVol 0.9) |
| 18 | **DELL** | 350.66 | - | **-** | 23 | - | NEG -$6.3M | - | 350 | 340 | -$632k | +$83k bull / +$0 bear | out (clean 32, ADX 51, RVol 0.6) |
| 19 | **ARM** | 187.58 | - | **-** | 23 | - | NEG -$4.6M | - | 185 | 190 | +$130k | +$80k bull / +$0 bear | out (clean 27, ADX 54, RVol 1.7) |
| 20 | **BABA** | 105.34 | - | **-** | 23 | - | POS +$2.6M | 103.92 | 110 | 110 | +$367k | +$139k bull / +$0 bear | out (clean 32, ADX 38, RVol 1.2) |
| 21 | **GOOGL** | 291.17 | - | **-** | 20 | - | POS +$15.6M | 288.79 | 300 | 290 | +$2.7M | +$26k bull / +$0 bear | out (clean 31, ADX 27, RVol 0.7) |
| 22 | **ORCL** | 119.03 | - | **-** | 19 | - | NEG -$26.8M | - | 125 | 120 | -$503k | +$216k bull / +$0 bear | out (clean 30, ADX 31, RVol 0.5) |
| 23 | **MSTR** | 127.27 | - | **-** | 14 | - | POS +$1.8M | 123.82 | 135 | 120 | -$2.9M | - | out (clean 30, ADX 22, RVol 0.9) |
| 24 | **UBER** | 69.66 | - | **-** | 12 | - | POS +$2.2M | 69.12 | 70 | 65 | -$78k | - | out (clean 30, ADX 29, RVol 0.8) |
| 25 | **SHOP** | 150.60 | - | **-** | 10 | - | POS +$1.7M | - | 150 | 140 | -$52k | - | out (clean 35, ADX 15, RVol 0.3) |
| 26 | **NFLX** | 63.52 | - | **-** | 8 | - | NEG -$19.5M | - | 65 | 65 | +$130k | - | out (clean 31, ADX 19, RVol 0.6) |
| 27 | **CRM** | 215.12 | - | **-** | 7 | - | NEG -$11.4M | - | 195 | 220 | +$15k | - | out (clean 34, ADX 19, RVol 0.9) |

## Big prints this scan (143)
- **SPY** PUT 744 2026-11-12 (3DTE): 876 @ 3.07 = **+$269k** SELL | vol 12,451 / OI 211
- **QQQ** PUT 675 2026-11-11 (2DTE): 500 @ 5.17 = **+$258k** SELL | vol 5,710 / OI 627
- **SPY** PUT 756 2026-11-09 (0DTE): 498 @ 4.71 = **+$235k** SELL | vol 16,887 / OI 382
- **AMD** PUT 490 2026-11-09 (0DTE): 1,990 @ 1.10 = **+$219k** SELL | vol 8,288 / OI 162
- **MU** PUT 720 2026-11-13 (4DTE): 100 @ 19.38 = **+$194k** SELL | vol 593 / OI 1,345
- **TSLA** PUT 390 2026-11-16 (7DTE): 120 @ 16.11 = **+$193k** MID | vol 134 / OI 167
- **MU** CALL 750 2026-11-11 (2DTE): 100 @ 19.12 = **+$191k** BUY | vol 2,542 / OI 955
- **PLTR** CALL 170 2026-11-13 (4DTE): 435 @ 4.35 = **+$189k** SELL | vol 9,046 / OI 2,642
- **MU** CALL 742.5 2026-11-09 (0DTE): 250 @ 7.50 = **+$188k** BUY | vol 4,695 / OI 112
- **SPY** PUT 744 2026-11-12 (3DTE): 616 @ 3.00 = **+$185k** SELL | vol 12,451 / OI 211
- **MU** CALL 750 2026-11-11 (2DTE): 94 @ 19.50 = **+$183k** BUY | vol 2,542 / OI 955
- **NVDA** CALL 182.5 2026-11-11 (2DTE): 625 @ 2.80 = **+$175k** BUY | vol 8,271 / OI 437
- **AMD** CALL 500 2026-11-09 (0DTE): 250 @ 6.43 = **+$161k** BUY | vol 33,598 / OI 1,188
- **AVGO** PUT 330 2026-11-11 (2DTE): 123 @ 12.15 = **+$149k** SELL | vol 186 / OI 95
- **QQQ** PUT 675 2026-11-11 (2DTE): 260 @ 5.03 = **+$131k** SELL | vol 5,710 / OI 627

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 702 2026-11-09 (0DTE): 2,352 traded vs OI 718
- **SPY** PUT 722 2026-11-10 (1DTE): 509 traded vs OI 386
- **SPY** PUT 711 2026-11-11 (2DTE): 523 traded vs OI 183
- **SPY** CALL 764 2026-11-13 (4DTE): 1,773 traded vs OI 1,701
- **SPY** CALL 769 2026-11-12 (3DTE): 781 traded vs OI 754
- **QQQ** PUT 684 2026-11-09 (0DTE): 532 traded vs OI 197
- **QQQ** PUT 680 2026-11-10 (1DTE): 816 traded vs OI 713
- **QQQ** PUT 627 2026-11-09 (0DTE): 528 traded vs OI 0
- **QQQ** CALL 656 2026-11-09 (0DTE): 503 traded vs OI 492
- **QQQ** PUT 648 2026-11-10 (1DTE): 508 traded vs OI 270
- **QQQ** PUT 677 2026-11-13 (4DTE): 619 traded vs OI 391
- **QQQ** PUT 673 2026-11-13 (4DTE): 503 traded vs OI 190
- **QQQ** CALL 669 2026-11-13 (4DTE): 500 traded vs OI 277
- **QQQ** CALL 675 2026-11-20 (11DTE): 2,654 traded vs OI 2,486
- **IWM** PUT 281 2026-11-11 (2DTE): 546 traded vs OI 534

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
