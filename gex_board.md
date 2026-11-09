# GEX + FLOW SCAN - Mon Nov 09, 12:30 PM ET
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
Last 1m check 12:30:08 ET, last candle SPY 12:29, QQQ 12:29 | no errors
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
| 1 | **AAPL** | 349.97 | PINNED between the walls (positive gamma) - chop | **-** | 31 | - | POS +$402.1M | 339.59 | 350 | 350 | -$6.1M | +$49k bull / +$0 bear | out (clean 27, ADX 30, RVol 0.4) |
| 2 | **IWM** | 281.36 | - | **-** | 29 | - | NEG -$934.2M | 284.92 | 285 | 270 | -$20.2M | +$107k bull / +$0 bear | out (clean 35, ADX 60, RVol 0.3) |
| 3 | **UBER** | 70.13 | PINNED between the walls (positive gamma) - chop | **-** | 29 | - | POS +$3.7M | 69.17 | 70 | 70 | -$112k | - | out (clean 31, ADX 37, RVol 1.2) |
| 4 | **AVGO** | 320.79 | - | **-** | 28 | - | NEG -$65.3M | - | 340 | 320 | -$9.1M | +$0 bull / -$181k bear | out (clean 31, ADX 54, RVol 0.7) |
| 5 | **SPY** | 752.45 | - | **-** | 27 | - | NEG -$6.1B | 761.65 | 750 | 740 | -$294.0M | +$147k bull / -$2.7M bear | out (clean 32, ADX 52, RVol 0.3) |
| 6 | **QQQ** | 677.74 | - | **-** | 26 | - | NEG -$2.1B | 699.23 | 680 | 680 | -$234.0M | +$106k bull / -$609k bear | out (clean 32, ADX 45, RVol 0.5) |
| 7 | **TSLA** | 378.00 | - | **-** | 26 | - | POS +$123.3M | - | 380 | 380 | -$92.3M | +$28k bull / -$259k bear | out (clean 34, ADX 34, RVol 0.3) |
| 8 | **AMD** | 502.06 | - | **-** | 26 | - | POS +$23.0M | 488.63 | 500 | 500 | -$55.4M | +$0 bull / -$856k bear | out (clean 32, ADX 49, RVol 0.4) |
| 9 | **NVDA** | 177.84 | - | **-** | 23 | - | NEG -$181.1M | - | 190 | 190 | -$58.3M | +$1.6M bull / -$1.9M bear | out (clean 32, ADX 31, RVol 1.5) |
| 10 | **PLTR** | 169.57 | - | **-** | 22 | - | POS +$11.2M | - | 165 | 180 | -$2.7M | +$68k bull / -$54k bear | out (clean 30, ADX 41, RVol 0.3) |
| 11 | **META** | 641.70 | - | **-** | 21 | - | POS +$172.8M | 614 | 650 | 640 | -$8.5M | +$1.5M bull / -$1.5M bear | out (clean 32, ADX 38, RVol 0.3) |
| 12 | **DELL** | 351.68 | - | **-** | 21 | - | NEG -$6.2M | - | 350 | 340 | -$571k | +$0 bull / -$34k bear | out (clean 32, ADX 43, RVol 0.2) |
| 13 | **GOOGL** | 291.48 | - | **-** | 18 | - | POS +$18.2M | 288.82 | 300 | 290 | +$3.9M | +$57k bull / -$26k bear | out (clean 31, ADX 13, RVol 0.6) |
| 14 | **MSTR** | 125.99 | - | **-** | 18 | - | POS +$1.4M | 123.6 | 135 | 120 | -$2.1M | +$88k bull / +$0 bear | out (clean 30, ADX 18, RVol 0.2) |
| 15 | **MSFT** | 544.73 | - | **-** | 17 | - | POS +$618.5M | - | 550 | 540 | +$940k | +$0 bull / -$202k bear | out (clean 34, ADX 32, RVol 0.4) |
| 16 | **MU** | 732.91 | - | **-** | 17 | - | NEG -$1.4M | 734.69 | 750 | 750 | -$12.5M | +$904k bull / +$0 bear | out (clean 31, ADX 34, RVol 0.2) |
| 17 | **ORCL** | 119.14 | - | **-** | 17 | - | NEG -$26.9M | - | 125 | 120 | -$465k | +$43k bull / +$0 bear | out (clean 30, ADX 21, RVol 0.7) |
| 18 | **COIN** | 137.26 | - | **-** | 15 | - | NEG -$6.7M | - | 140 | 135 | -$2.0M | - | out (clean 32, ADX 15, RVol 0.5) |
| 19 | **SMH** | 485.16 | - | **-** | 13 | - | NEG -$218.9M | - | 500 | 475 | -$2.6M | - | out (clean 31, ADX 38, RVol 0.3) |
| 20 | **SMCI** | 29.41 | - | **-** | 13 | - | NEG -$18k | - | 30 | 30 | -$981k | - | out (clean 30, ADX 10, RVol 0.5) |
| 21 | **AMZN** | 268.88 | - | **-** | 12 | - | POS +$395.0M | - | 270 | 265 | +$19.9M | - | out (clean 34, ADX 12, RVol 0.3) |
| 22 | **SHOP** | 151.13 | - | **-** | 12 | - | POS +$1.9M | - | 150 | 140 | -$88k | - | out (clean 34, ADX 20, RVol 0.1) |
| 23 | **HOOD** | 84.24 | - | **-** | 11 | - | NEG -$1.5M | - | 85 | 85 | -$2.1M | - | out (clean 31, ADX 29, RVol 0.4) |
| 24 | **ARM** | 187.39 | - | **-** | 11 | - | NEG -$4.5M | - | 185 | 190 | +$281k | - | out (clean 27, ADX 42, RVol 0.5) |
| 25 | **CRM** | 216.37 | - | **-** | 9 | - | NEG -$11.6M | - | 230 | 220 | -$45k | - | out (clean 34, ADX 26, RVol 0.3) |
| 26 | **BABA** | 105.53 | - | **-** | 7 | - | POS +$2.7M | 104.05 | 110 | 110 | +$111k | - | out (clean 31, ADX 33, RVol 0.3) |
| 27 | **NFLX** | 63.81 | - | **-** | 4 | - | NEG -$18.4M | - | 65 | 65 | +$35k | - | out (clean 31, ADX 16, RVol 0.5) |

## Big prints this scan (100)
- **SPY** CALL 762 2026-11-16 (7DTE): 2,127 @ 2.44 = **+$519k** SELL | vol 2,632 / OI 415
- **SPY** CALL 754 2026-11-10 (1DTE): 2,127 @ 2.38 = **+$506k** SELL | vol 24,058 / OI 1,031
- **SPY** CALL 752 2026-11-10 (1DTE): 1,350 @ 3.29 = **+$444k** SELL | vol 19,306 / OI 472
- **NVDA** CALL 180 2026-11-13 (4DTE): 931 @ 4.43 = **+$412k** BUY | vol 24,941 / OI 564
- **PLTR** CALL 167.5 2026-11-13 (4DTE): 507 @ 5.60 = **+$284k** MID | vol 7,982 / OI 1,196
- **PLTR** CALL 167.5 2026-11-13 (4DTE): 503 @ 5.60 = **+$282k** MID | vol 7,982 / OI 1,196
- **SPY** PUT 744 2026-11-12 (3DTE): 1,000 @ 2.59 = **+$259k** BUY | vol 14,763 / OI 211
- **NVDA** CALL 180 2026-11-16 (7DTE): 500 @ 4.98 = **+$249k** BUY | vol 7,130 / OI 138
- **NVDA** CALL 180 2026-11-16 (7DTE): 500 @ 4.97 = **+$248k** BUY | vol 7,130 / OI 138
- **NVDA** CALL 180 2026-11-16 (7DTE): 496 @ 4.98 = **+$247k** BUY | vol 7,130 / OI 138
- **NVDA** CALL 180 2026-11-16 (7DTE): 383 @ 4.96 = **+$190k** MID | vol 7,130 / OI 138
- **QQQ** CALL 660 2026-11-10 (1DTE): 100 @ 18.50 = **+$185k** SELL | vol 514 / OI 2,123
- **PLTR** CALL 167.5 2026-11-13 (4DTE): 318 @ 5.60 = **+$178k** MID | vol 7,982 / OI 1,196
- **NVDA** CALL 180 2026-11-16 (7DTE): 338 @ 4.97 = **+$168k** BUY | vol 7,130 / OI 138
- **PLTR** CALL 167.5 2026-11-13 (4DTE): 267 @ 5.60 = **+$150k** MID | vol 7,982 / OI 1,196

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 741 2026-11-12 (3DTE): 508 traded vs OI 208
- **SPY** CALL 771 2026-11-11 (2DTE): 548 traded vs OI 503
- **SPY** CALL 768 2026-11-11 (2DTE): 717 traded vs OI 673
- **SPY** PUT 710 2026-11-10 (1DTE): 55,889 traded vs OI 574
- **SPY** PUT 751 2026-11-12 (3DTE): 560 traded vs OI 247
- **SPY** CALL 762 2026-11-16 (7DTE): 2,632 traded vs OI 415
- **SPY** CALL 750 2026-11-27 (18DTE): 627 traded vs OI 618
- **SPY** PUT 710 2026-11-20 (11DTE): 114,992 traded vs OI 23,684
- **SPY** PUT 725 2026-11-20 (11DTE): 122,592 traded vs OI 110,852
- **QQQ** CALL 677 2026-11-13 (4DTE): 698 traded vs OI 686
- **QQQ** CALL 700 2026-11-13 (4DTE): 12,474 traded vs OI 12,454
- **IWM** CALL 287.5 2026-11-11 (2DTE): 11,157 traded vs OI 159
- **SMH** PUT 455 2026-11-09 (0DTE): 515 traded vs OI 214
- **SMH** CALL 500 2026-11-20 (11DTE): 2,231 traded vs OI 2,211
- **SMH** PUT 477.5 2026-11-09 (0DTE): 548 traded vs OI 24

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
