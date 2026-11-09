# GEX + FLOW SCAN - Mon Nov 09, 02:40 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (5)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 14:40 | **QQQ** | **CALLS** | 1m WHIPSAW (R1 R2) | 11/09 681C | 0.67 | 0.69 | +3% (0m) | **+3%** | +28% | 681.56 |
| 11:04 | **SPY** | **CALLS** | 1m WHIPSAW (R1) | 11/09 754C | 0.41 | 0.23 | -2% (0m) | **-44%** (done) | +28% | 752.23 |
| 10:35 | **AMZN** | **CALLS** | TREND + FLOW | 11/09 272.5C | 0.49 | 0.05 | +2% (2m) | **-90%** (done) | +225% | 273.49 |
| 10:00 | **MSFT** | **CALLS** | TREND + FLOW | 11/09 545C | 0.77 | 0.72 | +51% (23m) | **-6%** (done) | +545% | 550 |
| 10:00 | **AMZN** | **CALLS** | TREND + FLOW | 11/09 275C | 0.48 | 0.02 | +13% (6m) | **-96%** (done) | +258% | 275.95 |

## 1m RULES on SPY / QQQ - loose (2 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 14:40:08 ET, last candle SPY 14:39, QQQ 14:39 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
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
| 1 | **AMD** | 510.45 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 41 | none: 164 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (69 contracts' greeks worked out here) | POS +$28.4M | 501.32 | 510 | 500 | -$63.4M | +$6.3M bull / -$514k bear | out (clean 31, ADX 40, RVol 0.4) |
| 2 | **MU** | 732.33 | FLIP CROSS down into negative gamma | **PUTS** | 25 | none: 194 puts 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (80 contracts' greeks worked out here) | NEG -$294k | 732.57 | 750 | 750 | +$1.7M | +$459k bull / -$1.5M bear | out (clean 30, ADX 14, RVol 0.4) |
| 3 | **SPY** | 754.48 | - | **-** | 23 | - | NEG -$5.8B | 762.15 | 760 | 740 | -$310.2M | +$1.1M bull / -$132k bear | out (clean 31, ADX 33, RVol 0.4) |
| 4 | **TSLA** | 381.06 | - | **-** | 23 | - | POS +$136.9M | - | 380 | 380 | -$90.8M | +$62k bull / +$0 bear | out (clean 33, ADX 24, RVol 0.4) |
| 5 | **GOOGL** | 290.01 | PINNED between the walls (positive gamma) - chop | **-** | 23 | - | POS +$7.4M | 288.85 | 290 | 290 | +$4.5M | - | out (clean 31, ADX 25, RVol 0.6) |
| 6 | **QQQ** | 680.20 | - | **-** | 21 | - | NEG -$2.0B | 698.59 | 680 | 680 | -$234.1M | +$401k bull / -$616k bear | out (clean 31, ADX 27, RVol 0.5) |
| 7 | **AMZN** | 268.90 | - | **-** | 20 | - | POS +$395.9M | - | 270 | 265 | +$20.3M | +$126k bull / -$44k bear | out (clean 32, ADX 11, RVol 0.3) |
| 8 | **AVGO** | 320.64 | - | **-** | 20 | - | NEG -$65.9M | - | 340 | 320 | -$7.3M | +$66k bull / -$28k bear | out (clean 30, ADX 22, RVol 0.6) |
| 9 | **SMH** | 487.17 | - | **-** | 19 | - | NEG -$213.6M | - | 485 | 475 | -$2.8M | +$0 bull / -$36k bear | out (clean 29, ADX 20, RVol 0.3) |
| 10 | **AAPL** | 351.95 | - | **-** | 19 | - | POS +$476.4M | 339.27 | 365 | 350 | -$8.1M | +$782k bull / -$203k bear | out (clean 28, ADX 32, RVol 0.5) |
| 11 | **META** | 644.61 | - | **-** | 19 | - | POS +$199.0M | 612.56 | 650 | 640 | -$11.8M | +$0 bull / -$548k bear | out (clean 32, ADX 24, RVol 0.6) |
| 12 | **IWM** | 283.25 | - | **-** | 18 | - | NEG -$444.7M | 284.68 | 285 | 270 | -$24.2M | - | out (clean 34, ADX 50, RVol 0.7) |
| 13 | **HOOD** | 84.94 | - | **-** | 18 | - | NEG -$827k | - | 85 | 85 | -$2.5M | +$0 bull / -$58k bear | out (clean 29, ADX 18, RVol 0.4) |
| 14 | **NVDA** | 176.81 | - | **-** | 17 | - | NEG -$194.6M | - | 190 | 190 | -$41.0M | +$364k bull / -$400k bear | out (clean 32, ADX 18, RVol 0.9) |
| 15 | **MSFT** | 547.27 | - | **-** | 17 | - | POS +$690.1M | - | 550 | 540 | +$659k | +$29k bull / -$226k bear | out (clean 33, ADX 30, RVol 0.6) |
| 16 | **NFLX** | 63.76 | - | **-** | 15 | - | NEG -$20.1M | 67.43 | 65 | 65 | +$115k | +$0 bull / -$29k bear | out (clean 30, ADX 14, RVol 0.6) |
| 17 | **COIN** | 137.87 | - | **-** | 13 | - | NEG -$6.2M | - | 140 | 135 | -$2.0M | - | out (clean 32, ADX 12, RVol 0.4) |
| 18 | **UBER** | 71.07 | - | **-** | 13 | - | POS +$8.0M | 69.07 | 75 | 70 | -$230k | - | out (clean 32, ADX 42, RVol 0.4) |
| 19 | **SMCI** | 29.03 | - | **-** | 12 | - | NEG -$891 | - | 30 | 30 | -$608k | - | out (clean 28, ADX 30, RVol 0.8) |
| 20 | **SHOP** | 151.91 | - | **-** | 12 | - | POS +$2.1M | - | 150 | 140 | -$79k | - | out (clean 33, ADX 26, RVol 0.2) |
| 21 | **ARM** | 188.07 | - | **-** | 9 | - | NEG -$4.3M | - | 185 | 190 | +$718k | - | out (clean 26, ADX 16, RVol 1.2) |
| 22 | **CRM** | 215.22 | - | **-** | 8 | - | NEG -$11.2M | - | 195 | 220 | -$55k | - | out (clean 33, ADX 21, RVol 0.7) |
| 23 | **DELL** | 350.09 | - | **-** | 7 | - | NEG -$6.3M | - | 350 | 340 | +$399k | - | out (clean 33, ADX 30, RVol 0.4) |
| 24 | **MSTR** | 127.25 | - | **-** | 7 | - | POS +$3.7M | 122.66 | 135 | 120 | -$2.3M | - | out (clean 30, ADX 17, RVol 0.2) |
| 25 | **PLTR** | 170.05 | - | **-** | 6 | - | POS +$12.7M | - | 165 | 180 | -$1.7M | - | out (clean 30, ADX 16, RVol 0.4) |
| 26 | **BABA** | 105.68 | - | **-** | 5 | - | POS +$3.4M | 103.76 | 110 | 110 | +$54k | - | out (clean 30, ADX 20, RVol 0.4) |
| 27 | **ORCL** | 119.55 | - | **-** | 4 | - | NEG -$26.4M | - | 125 | 125 | -$454k | - | out (clean 29, ADX 11, RVol 0.2) |

## Big prints this scan (30)
- **SPY** PUT 753 2026-11-10 (1DTE): 400 @ 3.30 = **+$132k** BUY | vol 8,937 / OI 472
- **QQQ** PUT 671 2026-11-10 (1DTE): 478 @ 2.28 = **+$109k** BUY | vol 5,455 / OI 1,264
- **AMD** CALL 525 2026-11-11 (2DTE): 150 @ 6.72 = **+$101k** SELL | vol 1,486 / OI 0
- **AMD** CALL 525 2026-11-11 (2DTE): 143 @ 6.73 = **+$96k** SELL | vol 1,486 / OI 0
- **AMD** CALL 510 2026-11-11 (2DTE): 78 @ 12.20 = **+$95k** SELL | vol 2,287 / OI 432
- **NVDA** CALL 177.5 2026-11-13 (4DTE): 160 @ 4.65 = **+$74k** SELL | vol 15,217 / OI 121
- **NVDA** CALL 170 2026-11-13 (4DTE): 79 @ 9.15 = **+$72k** SELL | vol 2,865 / OI 300
- **MU** CALL 700 2026-11-09 (0DTE): 19 @ 28.15 = **+$53k** SELL | vol 5,966 / OI 761
- **AAPL** CALL 355 2026-11-13 (4DTE): 205 @ 2.47 = **+$51k** SELL | vol 9,447 / OI 2,726
- **NVDA** CALL 175 2026-11-11 (2DTE): 100 @ 4.75 = **+$48k** SELL | vol 14,836 / OI 255
- **MU** CALL 720 2026-11-11 (2DTE): 18 @ 25.40 = **+$46k** SELL | vol 2,520 / OI 227
- **MU** CALL 720 2026-11-11 (2DTE): 18 @ 25.40 = **+$46k** SELL | vol 2,520 / OI 227
- **AMZN** PUT 272.5 2026-11-13 (4DTE): 65 @ 6.84 = **+$44k** BUY | vol 1,373 / OI 344
- **META** PUT 632.5 2026-11-13 (4DTE): 50 @ 8.52 = **+$43k** BUY | vol 102 / OI 61
- **MU** CALL 725 2026-11-11 (2DTE): 18 @ 22.60 = **+$41k** SELL | vol 1,210 / OI 148

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 786 2026-11-13 (4DTE): 837 traded vs OI 808
- **SPY** PUT 762 2026-11-10 (1DTE): 636 traded vs OI 201
- **SPY** PUT 718 2026-11-11 (2DTE): 557 traded vs OI 301
- **SPY** CALL 819 2026-11-13 (4DTE): 913 traded vs OI 0
- **SPY** CALL 816 2026-11-13 (4DTE): 975 traded vs OI 99
- **SPY** CALL 825 2026-11-17 (8DTE): 2,100 traded vs OI 0
- **QQQ** PUT 631 2026-11-12 (3DTE): 561 traded vs OI 0
- **QQQ** PUT 618 2026-11-12 (3DTE): 1,057 traded vs OI 0
- **QQQ** CALL 687 2026-11-13 (4DTE): 609 traded vs OI 407
- **IWM** PUT 282 2026-11-10 (1DTE): 2,150 traded vs OI 2,014
- **IWM** PUT 277 2026-11-16 (7DTE): 508 traded vs OI 276
- **IWM** CALL 284 2026-11-18 (9DTE): 672 traded vs OI 299
- **NVDA** PUT 175 2026-11-27 (18DTE): 7,039 traded vs OI 4,251
- **AMD** CALL 560 2026-11-20 (11DTE): 530 traded vs OI 0
- **AMD** PUT 470 2026-11-13 (4DTE): 940 traded vs OI 927

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
