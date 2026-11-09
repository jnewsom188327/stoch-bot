# GEX + FLOW SCAN - Mon Nov 09, 01:20 PM ET
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
Last 1m check 13:20:08 ET, last candle SPY 13:19, QQQ 13:19 | no errors
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
| 1 | **SPY** | 752.30 | - | **-** | 26 | - | NEG -$6.4B | 761.75 | 750 | 740 | -$301.7M | +$456k bull / -$177k bear | out (clean 32, ADX 50, RVol 0.3) |
| 2 | **AMD** | 503.07 | - | **-** | 26 | - | POS +$25.1M | 491.35 | 500 | 500 | -$57.8M | +$0 bull / -$58k bear | out (clean 32, ADX 44, RVol 0.7) |
| 3 | **AVGO** | 319.27 | - | **-** | 25 | - | NEG -$65.7M | - | 340 | 320 | -$7.8M | +$60k bull / +$0 bear | out (clean 31, ADX 45, RVol 0.5) |
| 4 | **QQQ** | 676.35 | - | **-** | 23 | - | NEG -$2.2B | 699.13 | 680 | 680 | -$218.4M | +$402k bull / +$0 bear | out (clean 32, ADX 36, RVol 0.3) |
| 5 | **TSLA** | 376.81 | - | **-** | 23 | - | POS +$109.7M | - | 380 | 380 | -$90.3M | +$516k bull / +$0 bear | out (clean 34, ADX 23, RVol 0.3) |
| 6 | **SMH** | 483.67 | - | **-** | 21 | - | NEG -$226.7M | - | 485 | 475 | -$2.4M | +$26k bull / +$0 bear | out (clean 31, ADX 30, RVol 0.5) |
| 7 | **META** | 641.78 | - | **-** | 21 | - | POS +$170.6M | 613.67 | 650 | 640 | -$11.1M | +$55k bull / -$27k bear | out (clean 32, ADX 34, RVol 0.5) |
| 8 | **AMZN** | 268.01 | - | **-** | 21 | - | POS +$362.0M | - | 270 | 265 | +$20.9M | +$27k bull / +$0 bear | out (clean 33, ADX 11, RVol 0.3) |
| 9 | **GOOGL** | 289.73 | PINNED between the walls (positive gamma) - chop | **-** | 21 | - | POS +$9.9M | 288.39 | 290 | 290 | +$5.0M | - | out (clean 31, ADX 18, RVol 0.5) |
| 10 | **NVDA** | 176.47 | - | **-** | 20 | - | NEG -$199.2M | - | 190 | 190 | -$48.6M | +$1.0M bull / +$0 bear | out (clean 33, ADX 24, RVol 1.4) |
| 11 | **IWM** | 281.92 | - | **-** | 19 | - | NEG -$841.6M | 284.96 | 285 | 270 | -$21.9M | - | out (clean 35, ADX 57, RVol 0.3) |
| 12 | **MSTR** | 124.53 | - | **-** | 19 | - | POS +$16k | 124.06 | 135 | 120 | -$2.0M | +$34k bull / +$0 bear | out (clean 30, ADX 27, RVol 0.2) |
| 13 | **HOOD** | 83.69 | - | **-** | 19 | - | NEG -$1.6M | - | 85 | 85 | -$2.0M | +$26k bull / +$0 bear | out (clean 30, ADX 24, RVol 0.3) |
| 14 | **AAPL** | 349.16 | PINNED between the walls (positive gamma) - chop | **-** | 17 | - | POS +$386.1M | 339.58 | 350 | 350 | -$5.1M | - | out (clean 27, ADX 20, RVol 0.2) |
| 15 | **MSFT** | 542.88 | - | **-** | 17 | - | POS +$607.7M | - | 550 | 540 | +$1.2M | +$86k bull / +$0 bear | out (clean 34, ADX 29, RVol 0.3) |
| 16 | **MU** | 726.00 | - | **-** | 15 | - | NEG -$4.3M | 730.44 | 750 | 750 | +$884k | +$2.2M bull / -$28k bear | out (clean 31, ADX 23, RVol 0.5) |
| 17 | **UBER** | 70.75 | - | **-** | 15 | - | POS +$6.3M | 69.14 | 70 | 70 | -$213k | - | out (clean 32, ADX 49, RVol 0.7) |
| 18 | **COIN** | 136.21 | - | **-** | 13 | - | NEG -$6.9M | - | 140 | 135 | -$1.9M | - | out (clean 32, ADX 13, RVol 0.5) |
| 19 | **SMCI** | 29.03 | - | **-** | 13 | - | NEG -$47k | - | 30 | 30 | -$917k | - | out (clean 29, ADX 14, RVol 0.4) |
| 20 | **SHOP** | 151.14 | - | **-** | 12 | - | POS +$1.7M | - | 150 | 140 | -$84k | - | out (clean 34, ADX 22, RVol 0.1) |
| 21 | **CRM** | 215.88 | - | **-** | 10 | - | NEG -$11.0M | - | 195 | 220 | -$54k | - | out (clean 34, ADX 27, RVol 0.6) |
| 22 | **PLTR** | 168.76 | - | **-** | 9 | - | POS +$10.7M | - | 165 | 170 | -$2.6M | - | out (clean 30, ADX 26, RVol 0.3) |
| 23 | **ARM** | 185.85 | - | **-** | 9 | - | NEG -$4.7M | - | 185 | 190 | +$536k | - | out (clean 27, ADX 24, RVol 0.6) |
| 24 | **NFLX** | 63.60 | - | **-** | 7 | - | NEG -$20.5M | - | 65 | 65 | +$173k | - | out (clean 30, ADX 18, RVol 0.9) |
| 25 | **DELL** | 347.78 | - | **-** | 6 | - | NEG -$6.4M | - | 350 | 340 | +$211k | - | out (clean 32, ADX 27, RVol 0.1) |
| 26 | **BABA** | 105.44 | - | **-** | 6 | - | POS +$1.8M | 104.31 | 110 | 110 | +$123k | - | out (clean 31, ADX 28, RVol 0.3) |
| 27 | **ORCL** | 118.46 | - | **-** | 5 | - | NEG -$27.7M | - | 125 | 120 | -$343k | - | out (clean 30, ADX 17, RVol 0.2) |

## Big prints this scan (38)
- **QQQ** PUT 691 2026-11-09 (0DTE): 107 @ 13.86 = **+$148k** SELL | vol 704 / OI 216
- **QQQ** PUT 679 2026-11-09 (0DTE): 618 @ 2.31 = **+$143k** SELL | vol 19,872 / OI 139
- **QQQ** PUT 691 2026-11-09 (0DTE): 80 @ 13.86 = **+$111k** SELL | vol 704 / OI 216
- **TSLA** PUT 377.5 2026-11-09 (0DTE): 740 @ 1.39 = **+$103k** SELL | vol 55,242 / OI 267
- **SPY** PUT 754 2026-11-09 (0DTE): 550 @ 1.84 = **+$101k** SELL | vol 41,842 / OI 1,253
- **MU** CALL 722.5 2026-11-13 (4DTE): 30 @ 32.78 = **+$98k** BUY | vol 204 / OI 515
- **MU** CALL 735 2026-11-13 (4DTE): 30 @ 26.08 = **+$78k** BUY | vol 1,328 / OI 179
- **MU** CALL 740 2026-11-13 (4DTE): 30 @ 23.73 = **+$71k** BUY | vol 1,316 / OI 217
- **NVDA** CALL 180 2026-11-11 (2DTE): 231 @ 2.82 = **+$65k** BUY | vol 34,587 / OI 390
- **MU** CALL 730 2026-11-16 (7DTE): 20 @ 32.30 = **+$65k** BUY | vol 367 / OI 97
- **MU** PUT 730 2026-11-09 (0DTE): 99 @ 6.10 = **+$60k** SELL | vol 18,777 / OI 118
- **MU** PUT 725 2026-11-16 (7DTE): 19 @ 30.50 = **+$58k** SELL | vol 102 / OI 10
- **NVDA** CALL 175 2026-11-09 (0DTE): 231 @ 2.37 = **+$55k** BUY | vol 86,167 / OI 296
- **MU** PUT 750 2026-11-13 (4DTE): 12 @ 40.73 = **+$49k** SELL | vol 596 / OI 888
- **MU** PUT 750 2026-11-13 (4DTE): 12 @ 40.71 = **+$49k** SELL | vol 596 / OI 888

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 758 2026-11-11 (2DTE): 505 traded vs OI 415
- **SPY** CALL 820 2026-11-13 (4DTE): 855 traded vs OI 0
- **SPY** CALL 825 2026-11-13 (4DTE): 896 traded vs OI 0
- **QQQ** PUT 691 2026-11-09 (0DTE): 704 traded vs OI 216
- **IWM** CALL 290 2026-11-17 (8DTE): 527 traded vs OI 102
- **IWM** CALL 282 2026-11-20 (11DTE): 4,124 traded vs OI 3,991
- **META** CALL 705 2026-11-13 (4DTE): 648 traded vs OI 0
- **META** CALL 690 2026-11-13 (4DTE): 1,405 traded vs OI 580
- **META** CALL 702.5 2026-11-13 (4DTE): 541 traded vs OI 0
- **META** CALL 700 2026-11-13 (4DTE): 2,000 traded vs OI 1,992
- **META** CALL 665 2026-11-13 (4DTE): 528 traded vs OI 309
- **AVGO** PUT 312.5 2026-11-11 (2DTE): 568 traded vs OI 86
- **ARM** CALL 180 2026-11-13 (4DTE): 530 traded vs OI 278

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
