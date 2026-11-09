# GEX + FLOW SCAN - Mon Nov 09, 01:10 PM ET
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
Last 1m check 13:10:08 ET, last candle SPY 13:09, QQQ 13:09 | no errors
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
| 1 | **SPY** | 752.32 | - | **-** | 26 | - | NEG -$6.1B | 761.52 | 750 | 740 | -$303.1M | +$479k bull / -$1.5M bear | out (clean 32, ADX 51, RVol 0.4) |
| 2 | **AMD** | 504.33 | - | **-** | 26 | - | POS +$23.2M | 491.5 | 500 | 500 | -$59.1M | +$0 bull / -$532k bear | out (clean 32, ADX 45, RVol 0.5) |
| 3 | **AVGO** | 319.71 | - | **-** | 26 | - | NEG -$64.6M | - | 340 | 320 | -$8.1M | +$60k bull / +$0 bear | out (clean 31, ADX 48, RVol 0.7) |
| 4 | **QQQ** | 676.73 | - | **-** | 24 | - | NEG -$2.1B | 698.23 | 680 | 680 | -$222.8M | +$128k bull / +$0 bear | out (clean 32, ADX 39, RVol 0.3) |
| 5 | **TSLA** | 377.10 | - | **-** | 24 | - | POS +$119.6M | - | 380 | 380 | -$92.2M | +$58k bull / -$117k bear | out (clean 34, ADX 26, RVol 0.3) |
| 6 | **SMH** | 483.89 | - | **-** | 21 | - | NEG -$220.1M | - | 500 | 475 | -$2.5M | +$26k bull / +$0 bear | out (clean 31, ADX 32, RVol 0.5) |
| 7 | **NVDA** | 176.63 | - | **-** | 21 | - | NEG -$193.2M | - | 190 | 190 | -$51.4M | +$1.3M bull / +$0 bear | out (clean 33, ADX 24, RVol 1.5) |
| 8 | **META** | 642.52 | - | **-** | 21 | - | POS +$178.2M | 612.76 | 650 | 640 | -$11.8M | +$0 bull / -$674k bear | out (clean 32, ADX 34, RVol 0.6) |
| 9 | **AMZN** | 267.87 | - | **-** | 21 | - | POS +$373.4M | - | 270 | 265 | +$20.6M | +$27k bull / +$0 bear | out (clean 33, ADX 11, RVol 0.2) |
| 10 | **GOOGL** | 290.27 | PINNED between the walls (positive gamma) - chop | **-** | 21 | - | POS +$11.2M | 288.83 | 290 | 290 | +$4.8M | - | out (clean 31, ADX 16, RVol 0.5) |
| 11 | **IWM** | 281.83 | - | **-** | 19 | - | NEG -$836.3M | 284.91 | 285 | 270 | -$21.8M | - | out (clean 34, ADX 56, RVol 0.3) |
| 12 | **HOOD** | 83.93 | - | **-** | 19 | - | NEG -$1.5M | - | 85 | 85 | -$2.0M | +$28k bull / -$28k bear | out (clean 30, ADX 24, RVol 0.3) |
| 13 | **AAPL** | 349.33 | PINNED between the walls (positive gamma) - chop | **-** | 18 | - | POS +$395.4M | 339.4 | 350 | 350 | -$5.3M | - | out (clean 27, ADX 22, RVol 0.2) |
| 14 | **MSTR** | 125.59 | - | **-** | 18 | - | POS +$1.1M | 123.63 | 135 | 120 | -$2.1M | +$34k bull / -$25k bear | out (clean 30, ADX 25, RVol 0.1) |
| 15 | **NFLX** | 63.51 | - | **-** | 17 | - | NEG -$20.2M | - | 65 | 65 | +$129k | +$30k bull / +$0 bear | out (clean 30, ADX 18, RVol 0.8) |
| 16 | **MU** | 727.44 | - | **-** | 15 | - | NEG -$749k | 727.99 | 750 | 750 | -$4.5M | +$1.2M bull / +$0 bear | out (clean 31, ADX 24, RVol 0.4) |
| 17 | **COIN** | 137.01 | - | **-** | 14 | - | NEG -$6.7M | - | 140 | 135 | -$2.0M | - | out (clean 32, ADX 13, RVol 0.5) |
| 18 | **UBER** | 70.52 | - | **-** | 14 | - | POS +$5.7M | 69.1 | 70 | 70 | -$161k | - | out (clean 32, ADX 48, RVol 0.8) |
| 19 | **SMCI** | 29.05 | - | **-** | 13 | - | NEG -$58k | - | 30 | 30 | -$928k | - | out (clean 29, ADX 12, RVol 0.4) |
| 20 | **SHOP** | 151.12 | - | **-** | 13 | - | POS +$1.8M | - | 150 | 140 | -$89k | - | out (clean 34, ADX 22, RVol 0.1) |
| 21 | **CRM** | 216.04 | - | **-** | 11 | - | NEG -$11.0M | - | 195 | 220 | -$68k | - | out (clean 34, ADX 29, RVol 0.8) |
| 22 | **PLTR** | 168.95 | - | **-** | 10 | - | POS +$10.9M | - | 165 | 180 | -$2.6M | - | out (clean 30, ADX 30, RVol 0.4) |
| 23 | **ARM** | 186.76 | - | **-** | 9 | - | NEG -$4.6M | - | 185 | 190 | +$398k | - | out (clean 27, ADX 26, RVol 0.6) |
| 24 | **MSFT** | 543.99 | - | **-** | 7 | - | POS +$617.2M | - | 550 | 540 | +$821k | - | out (clean 34, ADX 31, RVol 0.3) |
| 25 | **DELL** | 348.80 | - | **-** | 6 | - | NEG -$6.3M | - | 350 | 340 | +$43k | - | out (clean 32, ADX 29, RVol 0.2) |
| 26 | **BABA** | 105.40 | - | **-** | 6 | - | POS +$2.1M | 104.25 | 110 | 110 | +$108k | - | out (clean 31, ADX 28, RVol 0.3) |
| 27 | **ORCL** | 118.90 | - | **-** | 5 | - | NEG -$27.0M | - | 125 | 120 | -$335k | - | out (clean 30, ADX 17, RVol 0.2) |

## Big prints this scan (29)
- **SPY** PUT 754 2026-11-09 (0DTE): 765 @ 1.77 = **+$135k** SELL | vol 37,954 / OI 1,253
- **SPY** CALL 730 2026-11-12 (3DTE): 50 @ 23.65 = **+$118k** BUY | vol 311 / OI 242
- **SPY** CALL 753 2026-11-10 (1DTE): 333 @ 3.04 = **+$101k** BUY | vol 31,042 / OI 487
- **NVDA** PUT 175 2026-11-13 (4DTE): 200 @ 4.30 = **+$86k** SELL | vol 19,875 / OI 5,460
- **NVDA** CALL 180 2026-11-13 (4DTE): 195 @ 4.31 = **+$84k** BUY | vol 26,706 / OI 564
- **MU** CALL 715 2026-11-11 (2DTE): 25 @ 31.70 = **+$79k** BUY | vol 435 / OI 229
- **MU** PUT 730 2026-11-13 (4DTE): 20 @ 28.05 = **+$56k** SELL | vol 605 / OI 797
- **MU** PUT 732.5 2026-11-13 (4DTE): 17 @ 29.25 = **+$50k** SELL | vol 250 / OI 246
- **MU** PUT 707.5 2026-11-13 (4DTE): 25 @ 18.80 = **+$47k** SELL | vol 121 / OI 116
- **MU** PUT 730 2026-11-09 (0DTE): 100 @ 4.10 = **+$41k** SELL | vol 17,154 / OI 118
- **MU** CALL 720 2026-11-13 (4DTE): 11 @ 36.09 = **+$40k** BUY | vol 1,770 / OI 408
- **MSFT** PUT 540 2026-11-13 (4DTE): 76 @ 5.05 = **+$38k** MID | vol 672 / OI 630
- **NVDA** CALL 175 2026-11-16 (7DTE): 50 @ 7.35 = **+$37k** BUY | vol 1,977 / OI 229
- **MSTR** CALL 126 2026-11-13 (4DTE): 72 @ 4.66 = **+$34k** BUY | vol 1,491 / OI 85
- **AVGO** PUT 320 2026-11-11 (2DTE): 50 @ 6.55 = **+$33k** SELL | vol 326 / OI 318

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 753 2026-11-11 (2DTE): 2,950 traded vs OI 124
- **SPY** PUT 707 2026-11-11 (2DTE): 523 traded vs OI 123
- **SPY** CALL 773 2026-11-11 (2DTE): 691 traded vs OI 609
- **SPY** PUT 716 2026-11-17 (8DTE): 586 traded vs OI 132
- **AAPL** PUT 347.5 2026-11-13 (4DTE): 1,293 traded vs OI 1,285
- **DELL** PUT 350 2026-11-13 (4DTE): 514 traded vs OI 213
- **MU** CALL 732.5 2026-11-13 (4DTE): 540 traded vs OI 217
- **UBER** CALL 71 2026-11-13 (4DTE): 3,109 traded vs OI 3,041

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
