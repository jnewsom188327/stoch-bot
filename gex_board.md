# GEX + FLOW SCAN - Mon Nov 09, 03:45 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (5)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 14:40 | **QQQ** | **CALLS** | 1m WHIPSAW (R1 R2) | 11/09 681C | 0.67 | 0.55 | +78% (36m) | **-18%** (done) | +28% | 681.56 hit |
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
| 1 | **TSLA** | 380.94 | PINNED between the walls (positive gamma) - chop | **-** | 43 | - | POS +$182.1M | - | 380 | 380 | -$96.8M | +$92k bull / -$463k bear | out (clean 33, ADX 46, RVol 1.0) |
| 2 | **META** | 645.45 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 43 | 11/09 647.5C @ 0.53 (delta 0.26) = est +368% at 650 | POS +$239.3M | 611.5 | 650 | 645 | -$13.1M | +$151k bull / -$33k bear | out (clean 33, ADX 39, RVol 1.1) |
| 3 | **AAPL** | 350.76 | PINNED between the walls (positive gamma) - chop | **-** | 35 | - | POS +$482.0M | 338.92 | 350 | 350 | -$8.3M | +$1.9M bull / +$0 bear | out (clean 28, ADX 23, RVol 1.3) |
| 4 | **IWM** | 283.00 | - | **-** | 29 | - | NEG -$423.8M | 284.46 | 283 | 270 | -$25.0M | +$115k bull / +$0 bear | out (clean 35, ADX 50, RVol 1.2) |
| 5 | **AMD** | 512.79 | - | **-** | 26 | - | POS +$60.7M | - | 500 | 500 | -$73.8M | +$3.2M bull / -$1.9M bear | out (clean 31, ADX 41, RVol 1.2) |
| 6 | **SPY** | 753.93 | - | **-** | 24 | - | NEG -$4.9B | 761.57 | 750 | 740 | -$321.8M | +$4.4M bull / -$1.3M bear | out (clean 31, ADX 33, RVol 1.0) |
| 7 | **AVGO** | 322.28 | - | **-** | 24 | - | NEG -$53.3M | - | 340 | 320 | -$8.3M | +$0 bull / -$86k bear | out (clean 31, ADX 31, RVol 1.7) |
| 8 | **AMZN** | 268.15 | - | **-** | 23 | - | POS +$368.6M | - | 270 | 265 | +$20.3M | +$366k bull / -$85k bear | out (clean 32, ADX 22, RVol 0.7) |
| 9 | **QQQ** | 680.22 | - | **-** | 22 | - | NEG -$1.8B | 695.69 | 680 | 680 | -$239.6M | +$14.0M bull / -$1.1M bear | out (clean 30, ADX 34, RVol 0.7) |
| 10 | **PLTR** | 169.95 | - | **-** | 21 | - | POS +$10.4M | - | 165 | 180 | -$2.0M | +$67k bull / +$0 bear | out (clean 29, ADX 32, RVol 1.3) |
| 11 | **SMH** | 488.82 | - | **-** | 20 | - | NEG -$229.0M | - | 500 | 475 | -$2.4M | +$912k bull / -$168k bear | out (clean 29, ADX 31, RVol 0.5) |
| 12 | **NVDA** | 177.56 | - | **-** | 20 | - | NEG -$180.4M | - | 190 | 190 | -$49.1M | +$1.8M bull / -$1.5M bear | out (clean 32, ADX 19, RVol 2.2) |
| 13 | **MSFT** | 546.95 | - | **-** | 20 | - | POS +$717.4M | - | 550 | 535 | +$1.4M | +$172k bull / +$0 bear | out (clean 33, ADX 38, RVol 0.9) |
| 14 | **GOOGL** | 288.84 | - | **-** | 19 | - | POS +$15.2M | 288.13 | 290 | 290 | +$4.6M | +$55k bull / -$86k bear | out (clean 31, ADX 20, RVol 0.8) |
| 15 | **MU** | 734.34 | - | **-** | 17 | - | NEG -$858k | 734.62 | 800 | 750 | -$20.4M | +$2.1M bull / -$1.5M bear | out (clean 30, ADX 25, RVol 0.9) |
| 16 | **UBER** | 71.12 | - | **-** | 14 | - | POS +$10.1M | 68.67 | 75 | 70 | -$295k | - | out (clean 32, ADX 36, RVol 1.0) |
| 17 | **COIN** | 137.13 | - | **-** | 13 | - | NEG -$7.1M | - | 140 | 135 | -$1.9M | - | out (clean 31, ADX 18, RVol 0.3) |
| 18 | **SHOP** | 151.71 | - | **-** | 13 | - | POS +$1.9M | - | 150 | 140 | -$89k | - | out (clean 32, ADX 28, RVol 0.6) |
| 19 | **ARM** | 187.43 | - | **-** | 11 | - | NEG -$3.4M | - | 200 | 200 | +$666k | - | out (clean 26, ADX 22, RVol 1.6) |
| 20 | **SMCI** | 28.86 | - | **-** | 10 | - | POS +$235k | - | 30 | 30 | -$629k | - | out (clean 28, ADX 20, RVol 0.8) |
| 21 | **ORCL** | 120.02 | - | **-** | 10 | - | NEG -$25.7M | - | 130 | 125 | -$774k | - | out (clean 29, ADX 35, RVol 0.6) |
| 22 | **HOOD** | 84.14 | - | **-** | 10 | - | NEG -$2.3M | - | 85 | 85 | -$2.8M | - | out (clean 29, ADX 21, RVol 0.6) |
| 23 | **CRM** | 214.96 | - | **-** | 10 | - | NEG -$11.0M | - | 195 | 220 | +$152k | - | out (clean 32, ADX 17, RVol 1.2) |
| 24 | **MSTR** | 126.49 | - | **-** | 8 | - | POS +$2.0M | 123.35 | 135 | 120 | -$2.7M | - | out (clean 30, ADX 22, RVol 0.4) |
| 25 | **NFLX** | 63.80 | - | **-** | 7 | - | NEG -$18.8M | 67.42 | 65 | 65 | +$104k | - | out (clean 29, ADX 19, RVol 1.5) |
| 26 | **BABA** | 105.48 | - | **-** | 6 | - | POS +$1.2M | 104.97 | 110 | 110 | +$53k | - | out (clean 30, ADX 26, RVol 0.6) |
| 27 | **DELL** | 347.60 | - | **-** | 5 | - | NEG -$7.2M | - | 350 | 340 | +$427k | - | out (clean 32, ADX 19, RVol 0.3) |

## Big prints this scan (104)
- **AMD** CALL 530 2026-11-13 (4DTE): 364 @ 11.77 = **+$428k** BUY | vol 3,590 / OI 769
- **AMD** CALL 517.5 2026-11-11 (2DTE): 309 @ 12.56 = **+$388k** BUY | vol 1,416 / OI 9
- **AMD** CALL 490 2026-11-13 (4DTE): 100 @ 33.50 = **+$335k** BUY | vol 4,184 / OI 1,648
- **SPY** PUT 755 2026-11-09 (0DTE): 4,544 @ 0.69 = **+$314k** SELL | vol 86,009 / OI 7,413
- **AMD** CALL 525 2026-11-11 (2DTE): 309 @ 9.40 = **+$290k** BUY | vol 2,139 / OI 122
- **QQQ** CALL 680 2026-11-10 (1DTE): 500 @ 5.55 = **+$278k** BUY | vol 30,409 / OI 1,376
- **MU** CALL 740 2026-11-11 (2DTE): 124 @ 20.90 = **+$259k** BUY | vol 3,187 / OI 120
- **SPY** CALL 745 2026-11-09 (0DTE): 200 @ 10.38 = **+$208k** BUY | vol 67,849 / OI 2,168
- **AMD** CALL 520 2026-11-11 (2DTE): 157 @ 11.31 = **+$178k** BUY | vol 3,608 / OI 157
- **SPY** CALL 740 2026-11-13 (4DTE): 98 @ 17.30 = **+$170k** BUY | vol 3,104 / OI 2,265
- **SMH** PUT 505 2026-11-13 (4DTE): 83 @ 20.10 = **+$167k** SELL | vol 446 / OI 1,307
- **AMZN** CALL 270 2026-11-13 (4DTE): 428 @ 3.80 = **+$163k** BUY | vol 7,385 / OI 7,386
- **QQQ** PUT 679 2026-11-13 (4DTE): 200 @ 7.15 = **+$143k** SELL | vol 1,625 / OI 420
- **SPY** PUT 754 2026-11-09 (0DTE): 4,544 @ 0.31 = **+$141k** SELL | vol 215,763 / OI 1,253
- **MU** CALL 740 2026-11-13 (4DTE): 47 @ 29.00 = **+$136k** BUY | vol 1,765 / OI 217

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 776 2026-11-10 (1DTE): 1,691 traded vs OI 1,662
- **SPY** CALL 766 2026-11-12 (3DTE): 526 traded vs OI 338
- **SPY** CALL 777 2026-11-10 (1DTE): 2,832 traded vs OI 2,797
- **SPY** CALL 756 2026-11-13 (4DTE): 2,681 traded vs OI 2,324
- **SPY** CALL 767 2026-11-12 (3DTE): 925 traded vs OI 916
- **SPY** CALL 797 2026-11-16 (7DTE): 642 traded vs OI 140
- **SPY** PUT 739 2026-11-13 (4DTE): 2,663 traded vs OI 2,420
- **SPY** CALL 763 2026-11-27 (18DTE): 672 traded vs OI 379
- **QQQ** PUT 685 2026-11-10 (1DTE): 1,081 traded vs OI 1,079
- **QQQ** CALL 700 2026-11-12 (3DTE): 1,417 traded vs OI 1,413
- **QQQ** CALL 710 2026-11-12 (3DTE): 766 traded vs OI 566
- **QQQ** PUT 639 2026-11-10 (1DTE): 804 traded vs OI 0
- **QQQ** PUT 655 2026-11-12 (3DTE): 1,193 traded vs OI 1,045
- **QQQ** PUT 649 2026-11-13 (4DTE): 4,581 traded vs OI 0
- **QQQ** CALL 673 2026-11-13 (4DTE): 500 traded vs OI 448

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
