# GEX + FLOW SCAN - Fri Nov 06, 11:30 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (3)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:30 | **NVDA** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/06 192.5C | 0.73 | 0.28 | +12% (20m) | **-62%** | +199% | 193.9 |
| 10:00 | **NVDA** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/06 197.5C | 0.67 | 0.03 | -6% (1m) | **-96%** (done) | +24% | 195 |
| 09:50 | **NFLX** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/06 64C | 0.40 | 0.36 | +32% (4m) | **-10%** (done) | +164% | 65 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 11:30:08 ET, last candle SPY 11:29, QQQ 11:29 | no errors

## Flow surges NOT fired - price disagreed (6 today, last 5)
- 09:55 SMCI PUTS: price +0.09 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 HOOD PUTS: price +3.27 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 MSTR PUTS: price +3.75 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 SMCI PUTS: price +0.89 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 PLTR PUTS: price +5.57 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **AAPL** | 344.71 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 38 | 11/06 347.5C @ 0.40 (delta 0.21) = est +524% at 350 | POS +$147.6M | 343.18 | 350 | 345 | -$19.0M | +$607k bull / -$32k bear | out (clean 29, ADX 13, RVol 0.6) |
| 2 | **TSLA** | 360.92 | - | **-** | 23 | - | NEG -$278.4M | - | 370 | 360 | -$65.2M | +$243k bull / -$372k bear | out (clean 34, ADX 37, RVol 0.6) |
| 3 | **MSTR** | 127.39 | - | **-** | 22 | - | NEG -$2.9M | 127.64 | 135 | 125 | -$7.5M | +$47k bull / +$0 bear | out (clean 31, ADX 14, RVol 0.6) |
| 4 | **DELL** | 335.17 | - | **-** | 20 | - | NEG -$27.1M | - | 340 | 335 | +$4.1M | +$33k bull / -$125k bear | out (clean 33, ADX 14, RVol 0.4) |
| 5 | **SMH** | 464.31 | - | **-** | 19 | - | NEG -$535.7M | - | 505 | 465 | +$6.4M | +$850k bull / -$343k bear | out (clean 34, ADX 12, RVol 0.8) |
| 6 | **META** | 620.63 | - | **-** | 19 | - | NEG -$64.2M | 623.29 | 650 | 625 | -$5.7M | +$613k bull / -$236k bear | out (clean 33, ADX 37, RVol 0.5) |
| 7 | **PLTR** | 161.77 | - | **-** | 19 | - | NEG -$64.0M | - | 165 | 160 | +$2.2M | +$0 bull / -$352k bear | out (clean 28, ADX 26, RVol 0.8) |
| 8 | **HOOD** | 79.68 | - | **-** | 19 | - | NEG -$22.0M | 83.9 | 85 | 80 | +$3.2M | +$60k bull / -$128k bear | out (clean 30, ADX 18, RVol 0.6) |
| 9 | **AMZN** | 263.63 | - | **-** | 18 | - | POS +$350.0M | - | 265 | 265 | -$2.8M | +$82k bull / +$0 bear | out (clean 34, ADX 25, RVol 0.4) |
| 10 | **MU** | 694.41 | - | **-** | 18 | - | NEG -$196.0M | - | 700 | 700 | +$64.0M | +$995k bull / -$5.2M bear | out (clean 32, ADX 12, RVol 0.9) |
| 11 | **NVDA** | 188.39 | - | **-** | 17 | - | NEG -$360.7M | - | 200 | 190 | +$23.0M | +$2.6M bull / -$695k bear | out (clean 35, ADX 17, RVol 0.8) |
| 12 | **ARM** | 172.89 | - | **-** | 17 | - | NEG -$21.6M | - | 190 | 170 | -$420k | +$0 bull / -$38k bear | out (clean 25, ADX 10, RVol 0.9) |
| 13 | **CRM** | 215.95 | - | **-** | 17 | - | NEG -$23.9M | - | 230 | 215 | +$3k | +$58k bull / +$0 bear | out (clean 34, ADX 30, RVol 0.6) |
| 14 | **SPY** | 739.82 | - | **-** | 16 | - | NEG -$14.4B | 768.47 | 770 | 740 | -$73.6M | +$626k bull / -$800k bear | out (clean 35, ADX 13, RVol 0.8) |
| 15 | **IWM** | 272.96 | - | **-** | 16 | - | NEG -$3.2B | 284.87 | 285 | 270 | -$4.8M | +$72k bull / -$134k bear | out (clean 34, ADX 16, RVol 0.5) |
| 16 | **AMD** | 444.17 | - | **-** | 16 | - | NEG -$179.9M | - | 430 | 450 | +$6.7M | +$288k bull / -$465k bear | out (clean 33, ADX 19, RVol 1.0) |
| 17 | **QQQ** | 660.28 | - | **-** | 15 | - | NEG -$4.9B | - | 700 | 680 | +$49.5M | +$308k bull / -$2.7M bear | out (clean 35, ADX 16, RVol 0.6) |
| 18 | **MSFT** | 536.85 | - | **-** | 15 | - | POS +$714.5M | 509.4 | 540 | 540 | +$1.2M | +$300k bull / -$83k bear | out (clean 33, ADX 16, RVol 0.5) |
| 19 | **GOOGL** | 287.69 | - | **-** | 15 | - | POS +$65.0M | 284.27 | 290 | 290 | +$1.1M | +$236k bull / -$836k bear | out (clean 34, ADX 16, RVol 0.4) |
| 20 | **AVGO** | 297.10 | - | **-** | 15 | - | NEG -$145.0M | - | 325 | 300 | +$392k | +$0 bull / -$35k bear | out (clean 31, ADX 14, RVol 0.9) |
| 21 | **COIN** | 132.71 | - | **-** | 13 | - | NEG -$18.2M | 136.02 | 143 | 130 | -$2.9M | - | out (clean 32, ADX 20, RVol 0.7) |
| 22 | **SMCI** | 28.52 | - | **-** | 8 | - | NEG -$4.7M | - | 30 | 30 | +$310k | - | out (clean 35, ADX 23, RVol 0.3) |
| 23 | **SHOP** | 149.15 | - | **-** | 7 | - | NEG -$5.0M | 151.51 | 150 | 150 | -$23k | - | out (clean 36, ADX 27, RVol 0.6) |
| 24 | **BABA** | 108.97 | - | **-** | 7 | - | POS +$23.8M | 104.67 | 110 | 110 | -$237k | - | out (clean 34, ADX 20, RVol 0.6) |
| 25 | **NFLX** | 64.21 | - | **-** | 6 | - | POS +$1.4M | 64.17 | 64 | 65 | -$282k | - | out (clean 32, ADX 16, RVol 0.6) |
| 26 | **UBER** | 69.61 | - | **-** | 5 | - | POS +$15.2M | 68.64 | 70 | 70 | +$83k | - | out (clean 30, ADX 8, RVol 0.4) |
| 27 | **ORCL** | 116.50 | - | **-** | 4 | - | NEG -$73.3M | - | 125 | 115 | +$401k | - | out (clean 30, ADX 10, RVol 0.5) |

## Big prints this scan (89)
- **MU** PUT 700 2026-11-13 (7DTE): 200 @ 45.00 = **+$900k** BUY | vol 629 / OI 1,130
- **MU** PUT 687.5 2026-11-13 (7DTE): 90 @ 38.00 = **+$342k** BUY | vol 144 / OI 0
- **MU** PUT 675 2026-11-13 (7DTE): 70 @ 33.35 = **+$233k** BUY | vol 420 / OI 0
- **MU** PUT 675 2026-11-13 (7DTE): 70 @ 33.35 = **+$233k** BUY | vol 420 / OI 0
- **QQQ** PUT 660 2026-11-06 (0DTE): 501 @ 4.50 = **+$225k** BUY | vol 89,796 / OI 12,054
- **QQQ** PUT 660 2026-11-09 (3DTE): 200 @ 8.30 = **+$166k** BUY | vol 12,033 / OI 1,084
- **QQQ** PUT 660 2026-11-09 (3DTE): 200 @ 8.25 = **+$165k** BUY | vol 12,033 / OI 1,084
- **QQQ** PUT 660 2026-11-09 (3DTE): 200 @ 8.20 = **+$164k** BUY | vol 12,033 / OI 1,084
- **QQQ** CALL 656 2026-11-06 (0DTE): 400 @ 3.90 = **+$156k** SELL | vol 13,690 / OI 0
- **QQQ** CALL 656 2026-11-06 (0DTE): 385 @ 3.75 = **+$144k** SELL | vol 13,690 / OI 0
- **IWM** CALL 270 2026-11-09 (3DTE): 368 @ 3.64 = **+$134k** SELL | vol 1,370 / OI 27
- **META** PUT 612.5 2026-11-06 (0DTE): 926 @ 1.35 = **+$125k** BUY | vol 3,569 / OI 515
- **QQQ** PUT 660 2026-11-09 (3DTE): 145 @ 8.25 = **+$120k** BUY | vol 12,033 / OI 1,084
- **MU** PUT 705 2026-11-11 (5DTE): 20 @ 43.25 = **+$86k** BUY | vol 71 / OI 0
- **SMH** PUT 450 2026-11-09 (3DTE): 154 @ 5.44 = **+$84k** BUY | vol 892 / OI 233

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 779 2026-11-11 (5DTE): 507 traded vs OI 115
- **SPY** CALL 748 2026-11-10 (4DTE): 510 traded vs OI 20
- **SPY** PUT 670 2026-11-09 (3DTE): 545 traded vs OI 101
- **SPY** CALL 743 2026-11-13 (7DTE): 518 traded vs OI 22
- **SPY** PUT 733 2026-11-13 (7DTE): 516 traded vs OI 505
- **SPY** PUT 680 2026-12-04 (28DTE): 710 traded vs OI 658
- **QQQ** PUT 623 2026-11-09 (3DTE): 554 traded vs OI 0
- **QQQ** PUT 624 2026-11-09 (3DTE): 548 traded vs OI 0
- **QQQ** PUT 612 2026-11-06 (0DTE): 626 traded vs OI 0
- **QQQ** PUT 631 2026-11-09 (3DTE): 500 traded vs OI 0
- **QQQ** PUT 648 2026-11-19 (13DTE): 521 traded vs OI 0
- **IWM** PUT 267 2026-11-27 (21DTE): 30,386 traded vs OI 1,803
- **SMH** PUT 450 2026-11-09 (3DTE): 892 traded vs OI 233
- **SMH** PUT 465 2026-11-13 (7DTE): 575 traded vs OI 203
- **SMH** PUT 450 2026-11-11 (5DTE): 535 traded vs OI 170

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
