# GEX + FLOW SCAN - Mon Nov 09, 03:35 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (5)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 14:40 | **QQQ** | **CALLS** | 1m WHIPSAW (R1 R2) | 11/09 681C | 0.67 | 0.79 | +78% (36m) | **+18%** | +28% | 681.56 hit |
| 11:04 | **SPY** | **CALLS** | 1m WHIPSAW (R1) | 11/09 754C | 0.41 | 0.23 | -2% (0m) | **-44%** (done) | +28% | 752.23 |
| 10:35 | **AMZN** | **CALLS** | TREND + FLOW | 11/09 272.5C | 0.49 | 0.05 | +2% (2m) | **-90%** (done) | +225% | 273.49 |
| 10:00 | **MSFT** | **CALLS** | TREND + FLOW | 11/09 545C | 0.77 | 0.72 | +51% (23m) | **-6%** (done) | +545% | 550 |
| 10:00 | **AMZN** | **CALLS** | TREND + FLOW | 11/09 275C | 0.48 | 0.02 | +13% (6m) | **-96%** (done) | +258% | 275.95 |

## 1m RULES on SPY / QQQ - loose (4 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 15:32:08 ET, last candle SPY 15:31, QQQ 15:31 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 15:08 | QQQ | 1m AGREE FLIP | FULL | CALLS | up | logged (agree flip) |
| 15:08 | SPY | 1m AGREE FLIP | FULL | CALLS | up | logged (agree flip) |
| 14:39 | QQQ | 1m WHIPSAW | R1 R2 | CALLS | WITH you | **FIRE** QQQ261109C00681000 |
| 11:03 | SPY | 1m WHIPSAW | R1 | CALLS | TURNING away | **FIRE** SPY261109C00754000 |

## Flow surges NOT fired - price disagreed (17 today, last 5)
- 10:55 AVGO PUTS: price +2.40 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:40 AVGO PUTS: price +1.16 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:40 QQQ PUTS: price +0.45 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:35 AVGO PUTS: price +1.05 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:30 QQQ PUTS: price +0.53 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **META** | 646.58 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 43 | none: 208 calls 0-7DTE > 9 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (92 contracts' greeks worked out here) | POS +$245.3M | 612.04 | 650 | 645 | -$13.7M | +$0 bull / -$540k bear | out (clean 33, ADX 39, RVol 0.9) |
| 2 | **AAPL** | 350.79 | PINNED between the walls (positive gamma) - chop | **-** | 35 | - | POS +$468.6M | 338.88 | 350 | 350 | -$9.1M | +$1.0M bull / +$0 bear | out (clean 28, ADX 26, RVol 1.1) |
| 3 | **MU** | 737.33 | FLIP CROSS up into positive gamma | **CALLS** | 31 | none: 191 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (68 contracts' greeks worked out here) | POS +$4.4M | 736.34 | 750 | 750 | -$23.6M | +$0 bull / -$1.7M bear | out (clean 30, ADX 24, RVol 0.8) |
| 4 | **TSLA** | 381.01 | - | **-** | 28 | - | POS +$186.2M | - | 380 | 380 | -$94.3M | +$0 bull / -$368k bear | out (clean 33, ADX 44, RVol 0.9) |
| 5 | **AMD** | 513.36 | - | **-** | 26 | - | POS +$59.5M | - | 500 | 500 | -$76.0M | +$63k bull / -$2.7M bear | out (clean 31, ADX 40, RVol 1.0) |
| 6 | **SPY** | 754.59 | - | **-** | 24 | - | NEG -$5.7B | 761.68 | 750 | 755 | -$337.0M | +$3.0M bull / -$4.0M bear | out (clean 31, ADX 35, RVol 0.9) |
| 7 | **AVGO** | 322.09 | - | **-** | 24 | - | NEG -$59.9M | - | 340 | 320 | -$8.2M | +$0 bull / -$110k bear | out (clean 31, ADX 31, RVol 1.4) |
| 8 | **QQQ** | 680.82 | - | **-** | 23 | - | NEG -$1.7B | 695.8 | 680 | 680 | -$258.3M | +$1.9M bull / -$1.5M bear | out (clean 31, ADX 34, RVol 0.6) |
| 9 | **SMH** | 489.57 | - | **-** | 22 | - | NEG -$225.8M | - | 500 | 475 | -$3.6M | +$0 bull / -$277k bear | out (clean 29, ADX 29, RVol 0.5) |
| 10 | **AMZN** | 268.49 | - | **-** | 22 | - | POS +$399.0M | - | 270 | 265 | +$19.6M | +$0 bull / -$243k bear | out (clean 32, ADX 22, RVol 0.6) |
| 11 | **NVDA** | 178.07 | - | **-** | 20 | - | NEG -$192.2M | - | 190 | 190 | -$52.7M | +$564k bull / -$1.9M bear | out (clean 32, ADX 21, RVol 1.6) |
| 12 | **MSFT** | 546.53 | - | **-** | 20 | - | POS +$700.3M | - | 550 | 545 | +$1.3M | +$139k bull / +$0 bear | out (clean 33, ADX 41, RVol 0.9) |
| 13 | **HOOD** | 84.44 | - | **-** | 20 | - | NEG -$2.1M | - | 85 | 85 | -$2.9M | +$47k bull / +$0 bear | out (clean 29, ADX 23, RVol 0.5) |
| 14 | **IWM** | 283.51 | - | **-** | 19 | - | NEG -$317.5M | 284.54 | 285 | 270 | -$25.7M | - | out (clean 35, ADX 52, RVol 1.1) |
| 15 | **GOOGL** | 289.64 | - | **-** | 19 | - | NEG -$158k | 289.99 | 290 | 290 | +$4.4M | +$0 bull / -$143k bear | out (clean 31, ADX 20, RVol 0.7) |
| 16 | **SHOP** | 151.83 | - | **-** | 14 | - | POS +$2.1M | - | 150 | 140 | -$93k | - | out (clean 32, ADX 28, RVol 0.5) |
| 17 | **COIN** | 137.50 | - | **-** | 13 | - | NEG -$6.9M | - | 140 | 135 | -$2.0M | - | out (clean 31, ADX 19, RVol 0.3) |
| 18 | **UBER** | 71.12 | - | **-** | 13 | - | POS +$10.0M | 68.69 | 75 | 70 | -$266k | - | out (clean 32, ADX 35, RVol 0.8) |
| 19 | **SMCI** | 29.00 | - | **-** | 11 | - | POS +$182k | - | 30 | 30 | -$651k | - | out (clean 28, ADX 22, RVol 0.7) |
| 20 | **ARM** | 187.79 | - | **-** | 11 | - | NEG -$3.3M | - | 200 | 200 | +$661k | - | out (clean 27, ADX 21, RVol 1.5) |
| 21 | **PLTR** | 170.30 | - | **-** | 10 | - | POS +$10.7M | - | 165 | 180 | -$2.0M | - | out (clean 29, ADX 31, RVol 1.0) |
| 22 | **CRM** | 214.97 | - | **-** | 10 | - | NEG -$10.9M | - | 195 | 220 | +$149k | - | out (clean 32, ADX 16, RVol 0.9) |
| 23 | **MSTR** | 126.50 | - | **-** | 9 | - | POS +$2.2M | 123.19 | 135 | 120 | -$2.7M | - | out (clean 30, ADX 25, RVol 0.5) |
| 24 | **ORCL** | 120.03 | - | **-** | 9 | - | NEG -$26.3M | - | 130 | 125 | -$638k | - | out (clean 29, ADX 31, RVol 0.5) |
| 25 | **NFLX** | 63.73 | - | **-** | 7 | - | NEG -$19.9M | 67.34 | 65 | 65 | +$124k | - | out (clean 29, ADX 17, RVol 1.3) |
| 26 | **BABA** | 105.58 | - | **-** | 6 | - | POS +$3.3M | 103.98 | 110 | 110 | +$26k | - | out (clean 30, ADX 27, RVol 0.5) |
| 27 | **DELL** | 349.02 | - | **-** | 5 | - | NEG -$7.0M | - | 350 | 340 | +$347k | - | out (clean 32, ADX 21, RVol 0.3) |

## Big prints this scan (94)
- **SPY** PUT 760 2026-11-13 (4DTE): 1,938 @ 8.05 = **+$1.6M** SELL | vol 2,967 / OI 5,777
- **AAPL** CALL 355 2026-11-11 (2DTE): 4,320 @ 1.23 = **+$531k** BUY | vol 43,037 / OI 505
- **SPY** CALL 754 2026-11-09 (0DTE): 3,179 @ 1.56 = **+$496k** BUY | vol 440,324 / OI 974
- **QQQ** PUT 713 2026-11-13 (4DTE): 105 @ 32.18 = **+$338k** SELL | vol 123 / OI 190
- **QQQ** PUT 676 2026-11-13 (4DTE): 500 @ 6.10 = **+$305k** SELL | vol 3,319 / OI 670
- **QQQ** PUT 676 2026-11-13 (4DTE): 500 @ 6.10 = **+$305k** SELL | vol 3,319 / OI 670
- **NVDA** PUT 180 2026-11-11 (2DTE): 500 @ 5.10 = **+$255k** BUY | vol 13,621 / OI 2,044
- **QQQ** CALL 650 2026-11-12 (3DTE): 75 @ 31.75 = **+$238k** SELL | vol 102 / OI 264
- **MU** PUT 727.5 2026-11-11 (2DTE): 125 @ 17.02 = **+$213k** BUY | vol 1,582 / OI 50
- **QQQ** PUT 674 2026-11-12 (3DTE): 440 @ 4.49 = **+$198k** SELL | vol 4,816 / OI 86
- **SPY** CALL 759 2026-11-13 (4DTE): 499 @ 3.90 = **+$195k** BUY | vol 4,923 / OI 2,412
- **SPY** PUT 752 2026-11-10 (1DTE): 1,000 @ 1.89 = **+$189k** SELL | vol 28,030 / OI 285
- **SPY** CALL 759 2026-11-13 (4DTE): 470 @ 3.86 = **+$181k** BUY | vol 4,923 / OI 2,412
- **AMD** PUT 515 2026-11-09 (0DTE): 493 @ 3.35 = **+$165k** BUY | vol 1,384 / OI 1
- **QQQ** PUT 681 2026-11-09 (0DTE): 1,696 @ 0.95 = **+$161k** BUY | vol 25,225 / OI 407

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 748 2026-11-12 (3DTE): 595 traded vs OI 592
- **SPY** CALL 754 2026-11-13 (4DTE): 1,614 traded vs OI 1,541
- **SPY** PUT 729 2026-11-11 (2DTE): 632 traded vs OI 190
- **SPY** PUT 755 2026-11-11 (2DTE): 1,309 traded vs OI 1,227
- **SPY** PUT 753 2026-11-16 (7DTE): 508 traded vs OI 346
- **SPY** PUT 710 2026-11-18 (9DTE): 514 traded vs OI 208
- **QQQ** CALL 696 2026-11-12 (3DTE): 503 traded vs OI 217
- **QQQ** PUT 681 2026-11-11 (2DTE): 770 traded vs OI 111
- **QQQ** PUT 672 2026-11-12 (3DTE): 511 traded vs OI 69
- **QQQ** PUT 663 2026-11-13 (4DTE): 500 traded vs OI 193
- **IWM** CALL 285 2026-11-16 (7DTE): 524 traded vs OI 376
- **SMH** CALL 500 2026-11-11 (2DTE): 600 traded vs OI 248
- **SMH** PUT 460 2026-11-20 (11DTE): 2,103 traded vs OI 1,996
- **TSLA** CALL 380 2026-11-18 (9DTE): 506 traded vs OI 267
- **AAPL** CALL 355 2026-11-16 (7DTE): 5,496 traded vs OI 109

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
