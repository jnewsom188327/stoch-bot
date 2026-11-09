# GEX + FLOW SCAN - Mon Nov 09, 01:30 PM ET
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
Last 1m check 13:30:08 ET, last candle SPY 13:29, QQQ 13:29 | no errors
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
| 1 | **SPY** | 752.20 | - | **-** | 26 | - | NEG -$5.9B | 761.56 | 750 | 740 | -$299.1M | +$323k bull / -$105k bear | out (clean 32, ADX 46, RVol 0.3) |
| 2 | **AMD** | 504.37 | - | **-** | 25 | - | POS +$24.9M | 488.86 | 500 | 500 | -$58.1M | +$308k bull / -$34k bear | out (clean 31, ADX 42, RVol 0.6) |
| 3 | **TSLA** | 376.41 | - | **-** | 23 | - | POS +$136.5M | - | 380 | 380 | -$89.9M | +$1.1M bull / +$0 bear | out (clean 34, ADX 21, RVol 0.3) |
| 4 | **QQQ** | 676.78 | - | **-** | 22 | - | NEG -$2.0B | 698.45 | 680 | 680 | -$215.8M | +$402k bull / -$153k bear | out (clean 32, ADX 32, RVol 0.3) |
| 5 | **GOOGL** | 289.61 | PINNED between the walls (positive gamma) - chop | **-** | 22 | - | POS +$10.4M | 288.46 | 290 | 290 | +$5.4M | - | out (clean 32, ADX 22, RVol 0.5) |
| 6 | **META** | 642.35 | - | **-** | 21 | - | POS +$163.8M | 615.22 | 650 | 640 | -$10.8M | +$118k bull / +$0 bear | out (clean 32, ADX 33, RVol 0.5) |
| 7 | **ARM** | 186.37 | - | **-** | 21 | - | NEG -$4.6M | - | 185 | 190 | +$836k | +$232k bull / +$0 bear | out (clean 27, ADX 23, RVol 0.6) |
| 8 | **NVDA** | 176.29 | - | **-** | 20 | - | NEG -$195.2M | - | 190 | 190 | -$45.0M | +$1.2M bull / +$0 bear | out (clean 33, ADX 24, RVol 1.5) |
| 9 | **IWM** | 282.00 | - | **-** | 19 | - | NEG -$726.1M | 284.7 | 285 | 270 | -$22.7M | - | out (clean 35, ADX 57, RVol 0.4) |
| 10 | **HOOD** | 83.79 | - | **-** | 19 | - | NEG -$1.5M | - | 85 | 85 | -$2.1M | +$59k bull / +$0 bear | out (clean 30, ADX 25, RVol 0.3) |
| 11 | **MSFT** | 543.34 | - | **-** | 17 | - | POS +$611.4M | - | 550 | 540 | +$1.4M | +$86k bull / +$0 bear | out (clean 34, ADX 26, RVol 0.3) |
| 12 | **AAPL** | 349.09 | - | **-** | 16 | - | POS +$389.7M | 339.28 | 350 | 350 | -$4.6M | +$123k bull / +$0 bear | out (clean 27, ADX 19, RVol 0.2) |
| 13 | **MU** | 728.56 | - | **-** | 15 | - | NEG -$1.2M | 729.98 | 750 | 750 | +$3.5M | +$2.1M bull / -$301k bear | out (clean 31, ADX 22, RVol 0.5) |
| 14 | **UBER** | 70.75 | - | **-** | 15 | - | POS +$6.0M | 69.21 | 70 | 70 | -$231k | - | out (clean 33, ADX 51, RVol 0.5) |
| 15 | **AVGO** | 319.17 | - | **-** | 14 | - | NEG -$66.5M | - | 340 | 320 | -$7.5M | - | out (clean 31, ADX 40, RVol 0.6) |
| 16 | **COIN** | 136.15 | - | **-** | 14 | - | NEG -$6.6M | - | 140 | 135 | -$1.9M | - | out (clean 33, ADX 15, RVol 0.3) |
| 17 | **SMCI** | 29.01 | - | **-** | 13 | - | NEG -$16k | - | 30 | 30 | -$870k | - | out (clean 29, ADX 18, RVol 0.5) |
| 18 | **AMZN** | 267.88 | - | **-** | 12 | - | POS +$375.4M | - | 270 | 265 | +$21.0M | - | out (clean 33, ADX 13, RVol 0.3) |
| 19 | **SHOP** | 151.04 | - | **-** | 12 | - | POS +$1.8M | - | 150 | 140 | -$84k | - | out (clean 34, ADX 21, RVol 0.1) |
| 20 | **SMH** | 484.41 | - | **-** | 10 | - | NEG -$226.2M | - | 500 | 475 | -$2.4M | - | out (clean 31, ADX 27, RVol 0.3) |
| 21 | **MSTR** | 124.66 | - | **-** | 9 | - | POS +$659k | 123.83 | 135 | 120 | -$1.6M | - | out (clean 30, ADX 29, RVol 0.3) |
| 22 | **PLTR** | 168.31 | - | **-** | 8 | - | POS +$11.2M | - | 165 | 170 | -$2.0M | - | out (clean 30, ADX 24, RVol 0.5) |
| 23 | **CRM** | 216.07 | - | **-** | 8 | - | NEG -$10.9M | - | 230 | 220 | -$49k | - | out (clean 34, ADX 24, RVol 0.4) |
| 24 | **NFLX** | 63.48 | - | **-** | 7 | - | NEG -$20.6M | - | 65 | 65 | +$193k | - | out (clean 30, ADX 19, RVol 0.7) |
| 25 | **DELL** | 347.92 | - | **-** | 7 | - | NEG -$6.4M | - | 350 | 340 | +$380k | - | out (clean 32, ADX 26, RVol 0.2) |
| 26 | **BABA** | 105.32 | - | **-** | 6 | - | POS +$1.9M | 104.28 | 110 | 110 | +$125k | - | out (clean 31, ADX 28, RVol 0.2) |
| 27 | **ORCL** | 118.72 | - | **-** | 5 | - | NEG -$26.8M | - | 125 | 125 | -$344k | - | out (clean 30, ADX 17, RVol 0.2) |

## Big prints this scan (46)
- **SPY** CALL 735 2026-11-13 (4DTE): 113 @ 19.65 = **+$222k** BUY | vol 1,216 / OI 2,240
- **ARM** CALL 180 2026-11-13 (4DTE): 172 @ 11.20 = **+$193k** BUY | vol 800 / OI 278
- **AAPL** PUT 355 2026-11-09 (0DTE): 300 @ 5.60 = **+$168k** MID | vol 1,172 / OI 700
- **QQQ** PUT 676 2026-11-09 (0DTE): 2,100 @ 0.73 = **+$153k** BUY | vol 155,167 / OI 98
- **SPY** CALL 735 2026-11-13 (4DTE): 54 @ 19.42 = **+$105k** SELL | vol 1,216 / OI 2,240
- **NVDA** CALL 175 2026-11-11 (2DTE): 198 @ 5.14 = **+$102k** BUY | vol 12,522 / OI 255
- **AMD** CALL 485 2026-11-09 (0DTE): 50 @ 20.16 = **+$101k** MID | vol 7,621 / OI 229
- **NVDA** PUT 175 2026-11-11 (2DTE): 300 @ 3.35 = **+$100k** SELL | vol 23,294 / OI 3,198
- **AAPL** PUT 352.5 2026-11-09 (0DTE): 300 @ 3.13 = **+$94k** SELL | vol 5,882 / OI 501
- **SMH** CALL 470 2026-11-11 (2DTE): 45 @ 18.16 = **+$82k** MID | vol 80 / OI 30
- **TSLA** CALL 360 2026-11-11 (2DTE): 40 @ 18.67 = **+$75k** BUY | vol 1,445 / OI 507
- **TSLA** CALL 365 2026-11-11 (2DTE): 48 @ 14.53 = **+$70k** BUY | vol 1,378 / OI 394
- **TSLA** CALL 360 2026-11-09 (0DTE): 40 @ 17.01 = **+$68k** BUY | vol 5,219 / OI 1,052
- **SMH** CALL 475 2026-11-11 (2DTE): 45 @ 14.48 = **+$65k** MID | vol 289 / OI 11
- **TSLA** CALL 360 2026-11-11 (2DTE): 32 @ 18.50 = **+$59k** BUY | vol 1,445 / OI 507

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 740 2026-11-11 (2DTE): 3,160 traded vs OI 3,129
- **SPY** CALL 753 2026-11-12 (3DTE): 545 traded vs OI 542
- **SPY** CALL 777 2026-11-18 (9DTE): 695 traded vs OI 31
- **SPY** CALL 755 2026-11-18 (9DTE): 525 traded vs OI 264
- **IWM** PUT 279 2026-11-13 (4DTE): 818 traded vs OI 803
- **IWM** CALL 282 2026-11-13 (4DTE): 1,150 traded vs OI 751
- **NVDA** PUT 192.5 2026-11-13 (4DTE): 555 traded vs OI 0
- **NVDA** PUT 192.5 2026-11-18 (9DTE): 1,018 traded vs OI 0
- **NVDA** PUT 160 2026-11-18 (9DTE): 2,637 traded vs OI 2,046
- **TSLA** CALL 357.5 2026-11-09 (0DTE): 526 traded vs OI 214
- **TSLA** PUT 362.5 2026-11-13 (4DTE): 500 traded vs OI 341
- **AAPL** PUT 330 2026-11-11 (2DTE): 2,216 traded vs OI 2,201
- **AMD** PUT 507.5 2026-11-09 (0DTE): 538 traded vs OI 59
- **GOOGL** CALL 302.5 2026-11-20 (11DTE): 989 traded vs OI 0
- **AVGO** PUT 315 2026-11-11 (2DTE): 505 traded vs OI 89

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
