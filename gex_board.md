# GEX + FLOW SCAN - Mon Nov 09, 12:10 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (4)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:04 | **SPY** | **CALLS** | 1m WHIPSAW (R1) | 11/09 754C | 0.41 | 0.23 | -2% (0m) | **-44%** (done) | +28% | 752.23 |
| 10:35 | **AMZN** | **CALLS** | TREND + FLOW | 11/09 272.5C | 0.49 | 0.05 | +2% (2m) | **-90%** (done) | +225% | 273.49 |
| 10:00 | **MSFT** | **CALLS** | TREND + FLOW | 11/09 545C | 0.77 | 0.72 | +51% (23m) | **-6%** (done) | +545% | 550 |
| 10:00 | **AMZN** | **CALLS** | TREND + FLOW | 11/09 275C | 0.48 | 0.02 | +13% (6m) | **-96%** (done) | +258% | 275.95 |

## 1m RULES on SPY / QQQ - loose (1 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 12:10:08 ET, last candle SPY 12:09, QQQ 12:09 | no errors
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
| 1 | **IWM** | 281.43 | FLOW SURGE | **PUTS** | 40 | 11/10 279P @ 0.75 (delta 0.28) = est +24% at 280.64 | NEG -$927.4M | 284.92 | 285 | 270 | -$20.7M | +$0 bull / -$92k bear | out (clean 35, ADX 61, RVol 0.4) |
| 2 | **AMD** | 501.05 | PINNED between the walls (positive gamma) - chop | **-** | 38 | - | POS +$19.8M | 487.98 | 500 | 500 | -$51.2M | +$106k bull / -$606k bear | out (clean 32, ADX 49, RVol 0.4) |
| 3 | **AAPL** | 350.23 | PINNED between the walls (positive gamma) - chop | **-** | 32 | - | POS +$426.9M | 338.93 | 350 | 350 | -$6.0M | +$0 bull / -$90k bear | out (clean 28, ADX 33, RVol 0.4) |
| 4 | **UBER** | 69.94 | PINNED between the walls (positive gamma) - chop | **-** | 29 | - | POS +$3.3M | 69.15 | 70 | 70 | -$144k | - | out (clean 31, ADX 33, RVol 1.0) |
| 5 | **SPY** | 752.08 | - | **-** | 27 | - | NEG -$6.4B | 761.75 | 750 | 740 | -$258.4M | +$0 bull / -$1.2M bear | out (clean 32, ADX 49, RVol 0.4) |
| 6 | **AVGO** | 320.11 | - | **-** | 27 | - | NEG -$66.4M | - | 340 | 320 | -$7.8M | +$0 bull / -$283k bear | out (clean 31, ADX 54, RVol 0.8) |
| 7 | **PLTR** | 169.53 | - | **-** | 27 | - | POS +$11.8M | - | 165 | 180 | -$4.6M | +$29k bull / +$0 bear | out (clean 30, ADX 44, RVol 0.4) |
| 8 | **QQQ** | 677.80 | - | **-** | 26 | - | NEG -$2.2B | 698.54 | 680 | 680 | -$225.9M | +$0 bull / -$368k bear | out (clean 32, ADX 44, RVol 0.4) |
| 9 | **NVDA** | 177.40 | - | **-** | 26 | - | NEG -$190.6M | - | 190 | 190 | -$52.3M | +$0 bull / -$3.0M bear | out (clean 32, ADX 38, RVol 2.5) |
| 10 | **TSLA** | 378.29 | - | **-** | 26 | - | POS +$116.8M | - | 380 | 380 | -$92.2M | +$0 bull / -$458k bear | out (clean 34, ADX 36, RVol 0.2) |
| 11 | **SMCI** | 29.52 | FLIP CROSS up into positive gamma | **CALLS** | 26 | 11/13 32C @ 0.40 (delta 0.23) = est +24% at 30 | POS +$3k | 29.43 | 30 | 30 | -$920k | - | out (clean 30, ADX 10, RVol 0.6) |
| 12 | **SMH** | 486.11 | - | **-** | 23 | - | NEG -$219.4M | - | 500 | 475 | -$2.7M | +$0 bull / -$39k bear | out (clean 31, ADX 38, RVol 0.4) |
| 13 | **HOOD** | 84.44 | - | **-** | 23 | - | NEG -$1.3M | - | 85 | 85 | -$2.1M | +$0 bull / -$25k bear | out (clean 31, ADX 37, RVol 0.7) |
| 14 | **META** | 642.59 | - | **-** | 21 | - | POS +$174.8M | 615.37 | 650 | 640 | -$8.2M | +$0 bull / -$67k bear | out (clean 32, ADX 37, RVol 0.2) |
| 15 | **DELL** | 352.46 | - | **-** | 21 | - | NEG -$6.2M | - | 350 | 340 | -$594k | +$0 bull / -$124k bear | out (clean 32, ADX 44, RVol 0.3) |
| 16 | **MU** | 735.35 | - | **-** | 19 | - | POS +$5.0M | 728.91 | 750 | 750 | -$11.9M | +$208k bull / -$1.5M bear | out (clean 32, ADX 38, RVol 0.5) |
| 17 | **MSTR** | 126.31 | - | **-** | 19 | - | POS +$1.5M | 123.72 | 135 | 120 | -$2.6M | +$0 bull / -$210k bear | out (clean 30, ADX 17, RVol 0.5) |
| 18 | **MSFT** | 542.77 | - | **-** | 18 | - | POS +$591.0M | - | 550 | 540 | +$2.2M | +$73k bull / -$56k bear | out (clean 33, ADX 27, RVol 0.3) |
| 19 | **BABA** | 105.54 | - | **-** | 18 | - | POS +$2.7M | 104.05 | 110 | 110 | +$110k | +$0 bull / -$154k bear | out (clean 32, ADX 35, RVol 0.3) |
| 20 | **ORCL** | 119.31 | - | **-** | 17 | - | NEG -$26.1M | - | 125 | 125 | -$432k | +$0 bull / -$50k bear | out (clean 30, ADX 21, RVol 0.6) |
| 21 | **COIN** | 137.46 | - | **-** | 16 | - | NEG -$6.4M | - | 140 | 135 | -$2.1M | - | out (clean 32, ADX 19, RVol 0.3) |
| 22 | **AMZN** | 268.58 | - | **-** | 12 | - | POS +$386.7M | - | 270 | 265 | +$20.5M | - | out (clean 34, ADX 13, RVol 0.3) |
| 23 | **ARM** | 188.43 | - | **-** | 11 | - | NEG -$4.5M | - | 185 | 190 | +$255k | - | out (clean 27, ADX 48, RVol 0.8) |
| 24 | **GOOGL** | 291.35 | - | **-** | 9 | - | POS +$15.8M | 288.52 | 300 | 290 | +$4.0M | - | out (clean 31, ADX 17, RVol 0.9) |
| 25 | **SHOP** | 150.38 | - | **-** | 9 | - | POS +$1.8M | - | 150 | 140 | -$51k | - | out (clean 34, ADX 16, RVol 0.1) |
| 26 | **NFLX** | 63.90 | - | **-** | 5 | - | NEG -$19.1M | 67.48 | 65 | 65 | +$57k | - | out (clean 31, ADX 15, RVol 0.5) |
| 27 | **CRM** | 215.69 | - | **-** | 5 | - | NEG -$11.6M | - | 230 | 220 | +$3k | - | out (clean 34, ADX 20, RVol 0.4) |

## Big prints this scan (45)
- **SPY** PUT 754 2026-11-09 (0DTE): 1,384 @ 3.20 = **+$443k** BUY | vol 10,406 / OI 1,253
- **TSLA** PUT 377.5 2026-11-13 (4DTE): 300 @ 8.70 = **+$261k** BUY | vol 2,566 / OI 350
- **MU** CALL 750 2026-11-13 (4DTE): 100 @ 21.72 = **+$217k** SELL | vol 1,834 / OI 1,316
- **QQQ** CALL 676 2026-11-09 (0DTE): 608 @ 1.99 = **+$121k** SELL | vol 113,395 / OI 618
- **NVDA** CALL 175 2026-11-11 (2DTE): 150 @ 5.50 = **+$82k** SELL | vol 9,970 / OI 255
- **NVDA** CALL 170 2026-11-13 (4DTE): 86 @ 9.45 = **+$81k** SELL | vol 2,272 / OI 300
- **MU** CALL 730 2026-11-09 (0DTE): 84 @ 9.01 = **+$76k** BUY | vol 21,260 / OI 259
- **NVDA** CALL 177.5 2026-11-16 (7DTE): 124 @ 5.60 = **+$69k** SELL | vol 2,305 / OI 12
- **NVDA** CALL 175 2026-11-13 (4DTE): 86 @ 6.25 = **+$54k** SELL | vol 15,666 / OI 627
- **NVDA** CALL 170 2026-11-13 (4DTE): 50 @ 10.06 = **+$50k** SELL | vol 2,272 / OI 300
- **AMD** CALL 515 2026-11-13 (4DTE): 39 @ 12.60 = **+$49k** SELL | vol 731 / OI 648
- **DELL** CALL 362.5 2026-11-13 (4DTE): 43 @ 10.20 = **+$44k** SELL | vol 73 / OI 14
- **AMD** CALL 515 2026-11-13 (4DTE): 33 @ 12.65 = **+$42k** SELL | vol 731 / OI 648
- **MU** PUT 730 2026-11-11 (2DTE): 20 @ 20.10 = **+$40k** BUY | vol 999 / OI 40
- **NVDA** CALL 177.5 2026-11-11 (2DTE): 100 @ 3.85 = **+$38k** SELL | vol 18,803 / OI 144

## New unusual volume (traded more than open interest, 500+)
- **QQQ** PUT 676 2026-11-11 (2DTE): 846 traded vs OI 843
- **QQQ** CALL 702 2026-11-10 (1DTE): 864 traded vs OI 230
- **QQQ** CALL 726 2026-11-13 (4DTE): 1,369 traded vs OI 582
- **QQQ** CALL 699 2026-11-13 (4DTE): 513 traded vs OI 466
- **QQQ** CALL 745 2026-11-30 (21DTE): 740 traded vs OI 0
- **QQQ** CALL 745 2026-11-20 (11DTE): 643 traded vs OI 0
- **IWM** CALL 286 2026-11-13 (4DTE): 2,293 traded vs OI 2,183
- **AAPL** PUT 335 2026-11-13 (4DTE): 1,730 traded vs OI 1,724
- **AMD** CALL 480 2026-11-27 (18DTE): 502 traded vs OI 267
- **AMZN** PUT 267.5 2026-11-20 (11DTE): 514 traded vs OI 394
- **NFLX** CALL 64 2026-12-04 (25DTE): 699 traded vs OI 307
- **MU** CALL 785 2026-11-11 (2DTE): 500 traded vs OI 0
- **MU** PUT 725 2026-11-20 (11DTE): 500 traded vs OI 0
- **MU** PUT 755 2026-11-23 (14DTE): 520 traded vs OI 0
- **HOOD** CALL 81 2026-11-27 (18DTE): 588 traded vs OI 224

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
