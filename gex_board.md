# GEX + FLOW SCAN - Mon Nov 09, 01:40 PM ET
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
Last 1m check 13:40:08 ET, last candle SPY 13:39, QQQ 13:39 | no errors
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
| 1 | **AMD** | 505.15 | FLIP CROSS up into positive gamma | **CALLS** | 37 | 11/09 510C @ 0.71 (delta 0.21) = est +93% at 509.61 | POS +$26.8M | 493.52 | 500 | 500 | -$60.6M | +$0 bull / -$73k bear | out (clean 31, ADX 42, RVol 0.5) |
| 2 | **GOOGL** | 289.85 | PINNED between the walls (positive gamma) - chop | **-** | 31 | - | POS +$11.1M | 288.98 | 290 | 290 | +$5.0M | +$65k bull / -$73k bear | out (clean 31, ADX 24, RVol 0.4) |
| 3 | **IWM** | 282.24 | - | **-** | 28 | - | NEG -$716.5M | 284.85 | 285 | 270 | -$22.1M | +$0 bull / -$1.0M bear | out (clean 35, ADX 58, RVol 0.5) |
| 4 | **AAPL** | 349.44 | PINNED between the walls (positive gamma) - chop | **-** | 26 | - | POS +$386.3M | 339.81 | 350 | 350 | -$4.9M | +$123k bull / +$0 bear | out (clean 27, ADX 17, RVol 0.2) |
| 5 | **MU** | 729.62 | FLIP CROSS down into negative gamma | **PUTS** | 26 | none: 194 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (78 contracts' greeks worked out here) | NEG -$14.1M | 741.05 | 750 | 750 | -$75k | +$116k bull / -$1.3M bear | out (clean 31, ADX 20, RVol 0.4) |
| 6 | **SPY** | 752.47 | - | **-** | 25 | - | NEG -$6.4B | 761.71 | 750 | 740 | -$303.3M | +$651k bull / -$2.4M bear | out (clean 32, ADX 44, RVol 0.3) |
| 7 | **AVGO** | 318.80 | - | **-** | 23 | - | NEG -$63.4M | - | 340 | 320 | -$7.6M | +$40k bull / -$36k bear | out (clean 31, ADX 35, RVol 0.6) |
| 8 | **QQQ** | 677.12 | - | **-** | 22 | - | NEG -$2.2B | 699.14 | 680 | 680 | -$224.5M | +$0 bull / -$1.2M bear | out (clean 32, ADX 30, RVol 0.4) |
| 9 | **TSLA** | 376.78 | - | **-** | 22 | - | POS +$122.5M | - | 380 | 380 | -$91.8M | +$668k bull / -$503k bear | out (clean 34, ADX 18, RVol 0.3) |
| 10 | **AMZN** | 267.87 | - | **-** | 21 | - | POS +$364.4M | - | 270 | 265 | +$20.5M | +$0 bull / -$26k bear | out (clean 34, ADX 13, RVol 0.3) |
| 11 | **NVDA** | 176.29 | - | **-** | 20 | - | NEG -$193.3M | - | 190 | 190 | -$47.2M | +$769k bull / -$723k bear | out (clean 34, ADX 24, RVol 1.4) |
| 12 | **META** | 642.25 | - | **-** | 20 | - | POS +$162.3M | 613.69 | 650 | 640 | -$10.7M | +$58k bull / +$0 bear | out (clean 32, ADX 31, RVol 0.5) |
| 13 | **ARM** | 186.35 | - | **-** | 20 | - | NEG -$4.6M | - | 185 | 190 | +$794k | +$193k bull / +$0 bear | out (clean 27, ADX 20, RVol 0.6) |
| 14 | **HOOD** | 83.91 | - | **-** | 19 | - | NEG -$1.5M | - | 85 | 85 | -$2.2M | +$33k bull / -$28k bear | out (clean 30, ADX 24, RVol 0.3) |
| 15 | **PLTR** | 168.45 | - | **-** | 18 | - | POS +$11.0M | - | 165 | 170 | -$2.1M | +$0 bull / -$40k bear | out (clean 30, ADX 23, RVol 0.5) |
| 16 | **MSTR** | 125.22 | - | **-** | 18 | - | POS +$765k | 124.04 | 135 | 120 | -$1.6M | +$0 bull / -$525k bear | out (clean 30, ADX 28, RVol 0.3) |
| 17 | **MSFT** | 543.53 | - | **-** | 16 | - | POS +$614.0M | - | 550 | 540 | +$1.1M | +$0 bull / -$63k bear | out (clean 34, ADX 24, RVol 0.3) |
| 18 | **UBER** | 70.75 | - | **-** | 14 | - | POS +$6.7M | 69.14 | 75 | 70 | -$216k | - | out (clean 33, ADX 51, RVol 0.3) |
| 19 | **COIN** | 136.75 | - | **-** | 13 | - | NEG -$6.6M | - | 140 | 135 | -$2.0M | - | out (clean 33, ADX 14, RVol 0.2) |
| 20 | **SHOP** | 151.20 | - | **-** | 12 | - | POS +$2.1M | - | 150 | 140 | -$84k | - | out (clean 34, ADX 20, RVol 0.2) |
| 21 | **SMCI** | 28.85 | - | **-** | 11 | - | NEG -$314k | - | 30 | 30 | -$680k | - | out (clean 30, ADX 22, RVol 0.6) |
| 22 | **SMH** | 484.56 | - | **-** | 10 | - | NEG -$222.9M | - | 485 | 475 | -$2.7M | - | out (clean 31, ADX 26, RVol 0.2) |
| 23 | **CRM** | 216.16 | - | **-** | 8 | - | NEG -$11.4M | - | 230 | 220 | -$64k | - | out (clean 34, ADX 21, RVol 0.4) |
| 24 | **NFLX** | 63.60 | - | **-** | 7 | - | NEG -$20.4M | - | 65 | 65 | +$219k | - | out (clean 30, ADX 18, RVol 0.6) |
| 25 | **DELL** | 347.26 | - | **-** | 6 | - | NEG -$6.5M | - | 350 | 340 | +$298k | - | out (clean 32, ADX 26, RVol 0.2) |
| 26 | **BABA** | 105.40 | - | **-** | 6 | - | POS +$2.2M | 104.13 | 110 | 110 | +$128k | - | out (clean 31, ADX 27, RVol 0.2) |
| 27 | **ORCL** | 118.81 | - | **-** | 4 | - | NEG -$27.0M | - | 125 | 120 | -$375k | - | out (clean 30, ADX 15, RVol 0.2) |

## Big prints this scan (60)
- **IWM** PUT 277 2026-11-13 (4DTE): 10,000 @ 1.04 = **+$1.0M** BUY | vol 10,359 / OI 1,648
- **SPY** PUT 754 2026-11-09 (0DTE): 1,964 @ 2.25 = **+$442k** BUY | vol 67,262 / OI 1,253
- **SPY** PUT 754 2026-11-09 (0DTE): 1,819 @ 2.25 = **+$409k** BUY | vol 67,262 / OI 1,253
- **SPY** PUT 754 2026-11-09 (0DTE): 1,456 @ 2.23 = **+$325k** BUY | vol 67,262 / OI 1,253
- **QQQ** PUT 691 2026-11-09 (0DTE): 200 @ 14.90 = **+$298k** BUY | vol 946 / OI 216
- **SPY** PUT 754 2026-11-09 (0DTE): 1,001 @ 2.20 = **+$220k** BUY | vol 67,262 / OI 1,253
- **SPY** PUT 754 2026-11-09 (0DTE): 971 @ 2.20 = **+$214k** BUY | vol 67,262 / OI 1,253
- **SPY** PUT 755 2026-11-10 (1DTE): 400 @ 4.54 = **+$182k** BUY | vol 2,460 / OI 3,597
- **SPY** PUT 747 2026-11-12 (3DTE): 500 @ 3.25 = **+$162k** BUY | vol 5,518 / OI 183
- **MU** CALL 750 2026-11-13 (4DTE): 80 @ 18.80 = **+$150k** SELL | vol 2,073 / OI 1,316
- **QQQ** PUT 676 2026-11-13 (4DTE): 181 @ 8.26 = **+$150k** BUY | vol 1,678 / OI 670
- **SPY** PUT 763 2026-11-13 (4DTE): 114 @ 12.20 = **+$139k** BUY | vol 465 / OI 996
- **NVDA** CALL 175 2026-11-11 (2DTE): 246 @ 5.05 = **+$124k** BUY | vol 13,069 / OI 255
- **SPY** PUT 754 2026-11-09 (0DTE): 471 @ 2.34 = **+$110k** BUY | vol 67,262 / OI 1,253
- **SPY** PUT 763 2026-11-13 (4DTE): 86 @ 12.20 = **+$105k** BUY | vol 465 / OI 996

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 762 2026-11-09 (0DTE): 519 traded vs OI 10
- **SPY** CALL 751 2026-11-12 (3DTE): 612 traded vs OI 610
- **SPY** PUT 731 2026-11-13 (4DTE): 2,417 traded vs OI 2,394
- **QQQ** PUT 676 2026-11-12 (3DTE): 502 traded vs OI 16
- **IWM** PUT 277 2026-11-13 (4DTE): 10,359 traded vs OI 1,648
- **IWM** PUT 256 2026-11-13 (4DTE): 1,131 traded vs OI 753
- **IWM** CALL 287.5 2026-11-16 (7DTE): 638 traded vs OI 225
- **IWM** PUT 270 2026-11-19 (10DTE): 1,003 traded vs OI 194
- **IWM** PUT 260 2026-11-12 (3DTE): 529 traded vs OI 373
- **IWM** PUT 263 2026-11-12 (3DTE): 812 traded vs OI 250
- **IWM** PUT 281 2026-11-10 (1DTE): 1,905 traded vs OI 1,668
- **IWM** PUT 259 2026-11-13 (4DTE): 924 traded vs OI 672
- **MSFT** PUT 530 2026-11-13 (4DTE): 685 traded vs OI 677
- **DELL** PUT 347.5 2026-11-13 (4DTE): 517 traded vs OI 63
- **MSTR** CALL 123 2026-11-13 (4DTE): 505 traded vs OI 6

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
