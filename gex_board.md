# GEX + FLOW SCAN - Fri Nov 06, 11:10 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (3)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:30 | **NVDA** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/06 192.5C | 0.73 | 0.37 | +12% (20m) | **-49%** | +199% | 193.9 |
| 10:00 | **NVDA** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/06 197.5C | 0.67 | 0.03 | -6% (1m) | **-96%** (done) | +24% | 195 |
| 09:50 | **NFLX** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/06 64C | 0.40 | 0.36 | +32% (4m) | **-10%** (done) | +164% | 65 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 11:10:08 ET, last candle SPY 11:09, QQQ 11:09 | no errors

## Flow surges NOT fired - price disagreed (6 today, last 5)
- 09:55 SMCI PUTS: price +0.09 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 HOOD PUTS: price +3.27 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 MSTR PUTS: price +3.75 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 SMCI PUTS: price +0.89 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 PLTR PUTS: price +5.57 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **AAPL** | 344.75 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 41 | 11/06 347.5C @ 0.58 (delta 0.24) = est +366% at 350 | POS +$214.5M | 342.48 | 350 | 345 | -$21.6M | +$163k bull / -$2.0M bear | out (clean 29, ADX 14, RVol 0.7) |
| 2 | **MSTR** | 127.41 | FLIP CROSS down into negative gamma | **PUTS** | 37 | 11/06 124P @ 0.53 (delta 0.21) = est +82% at 125 | NEG -$1.9M | 127.57 | 135 | 125 | -$7.5M | +$0 bull / -$1.3M bear | out (clean 31, ADX 15, RVol 0.8) |
| 3 | **MSFT** | 535.07 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 35 | 11/06 540C @ 0.74 (delta 0.21) = est +167% at 540 | POS +$678.2M | 511.16 | 540 | 535 | +$1.4M | +$0 bull / -$1.1M bear | out (clean 33, ADX 19, RVol 0.7) |
| 4 | **TSLA** | 357.33 | - | **-** | 23 | - | NEG -$259.9M | - | 370 | 360 | -$53.9M | +$1.8M bull / -$1.8M bear | out (clean 35, ADX 40, RVol 0.6) |
| 5 | **META** | 621.70 | - | **-** | 22 | - | NEG -$38.6M | 623.18 | 650 | 625 | -$6.8M | +$1.1M bull / -$294k bear | out (clean 33, ADX 45, RVol 0.8) |
| 6 | **DELL** | 332.31 | - | **-** | 22 | - | NEG -$26.0M | - | 340 | 335 | +$4.0M | +$75k bull / +$0 bear | out (clean 33, ADX 16, RVol 0.6) |
| 7 | **HOOD** | 79.49 | - | **-** | 21 | - | NEG -$20.6M | - | 85 | 80 | +$3.3M | +$129k bull / -$1.1M bear | out (clean 29, ADX 22, RVol 0.8) |
| 8 | **PLTR** | 160.37 | - | **-** | 20 | - | NEG -$72.6M | - | 165 | 160 | +$2.8M | +$688k bull / +$0 bear | out (clean 28, ADX 31, RVol 0.7) |
| 9 | **MU** | 687.22 | - | **-** | 20 | - | NEG -$174.6M | - | 700 | 700 | +$88.4M | +$5.6M bull / -$1.5M bear | out (clean 32, ADX 15, RVol 0.8) |
| 10 | **SMH** | 462.59 | - | **-** | 19 | - | NEG -$511.5M | - | 505 | 465 | +$6.3M | +$952k bull / -$269k bear | out (clean 34, ADX 14, RVol 0.7) |
| 11 | **AMZN** | 263.44 | - | **-** | 19 | - | POS +$376.2M | - | 265 | 265 | -$2.9M | +$2.1M bull / -$37k bear | out (clean 34, ADX 28, RVol 0.5) |
| 12 | **CRM** | 215.07 | - | **-** | 19 | - | NEG -$24.3M | - | 230 | 220 | +$85k | +$0 bull / -$38k bear | out (clean 34, ADX 37, RVol 0.6) |
| 13 | **NVDA** | 188.53 | - | **-** | 18 | - | NEG -$391.4M | - | 200 | 190 | +$19.4M | +$1.6M bull / -$605k bear | out (clean 34, ADX 21, RVol 1.1) |
| 14 | **SPY** | 739.43 | - | **-** | 17 | - | NEG -$14.3B | 769.12 | 770 | 740 | -$98.0M | +$1.0M bull / -$1.2M bear | out (clean 35, ADX 16, RVol 0.8) |
| 15 | **AMD** | 440.62 | - | **-** | 17 | - | NEG -$169.9M | - | 430 | 450 | +$6.5M | +$1.2M bull / -$584k bear | out (clean 33, ADX 21, RVol 0.9) |
| 16 | **GOOGL** | 287.19 | - | **-** | 17 | - | POS +$56.9M | 282.24 | 290 | 290 | +$2.4M | +$62k bull / -$28k bear | out (clean 34, ADX 19, RVol 0.5) |
| 17 | **NFLX** | 64.25 | - | **-** | 17 | - | POS +$18.0M | 63.41 | 65 | 65 | -$291k | +$0 bull / -$76k bear | out (clean 32, ADX 18, RVol 0.7) |
| 18 | **QQQ** | 658.51 | - | **-** | 16 | - | NEG -$5.6B | - | 700 | 680 | +$38.2M | +$2.9M bull / -$3.1M bear | out (clean 35, ADX 18, RVol 0.6) |
| 19 | **IWM** | 272.89 | - | **-** | 16 | - | NEG -$3.4B | 285.6 | 285 | 270 | -$4.1M | +$0 bull / -$453k bear | out (clean 34, ADX 15, RVol 0.6) |
| 20 | **AVGO** | 296.10 | - | **-** | 15 | - | NEG -$135.7M | - | 325 | 300 | +$627k | +$88k bull / +$0 bear | out (clean 31, ADX 16, RVol 0.9) |
| 21 | **ORCL** | 116.48 | - | **-** | 14 | - | NEG -$72.4M | - | 125 | 115 | +$260k | +$42k bull / +$0 bear | out (clean 30, ADX 12, RVol 0.5) |
| 22 | **COIN** | 134.14 | - | **-** | 10 | - | NEG -$14.8M | 136.49 | 142 | 130 | -$2.0M | - | out (clean 31, ADX 16, RVol 0.5) |
| 23 | **SMCI** | 28.59 | - | **-** | 9 | - | NEG -$4.1M | - | 30 | 30 | +$305k | - | out (clean 34, ADX 29, RVol 0.3) |
| 24 | **ARM** | 171.90 | - | **-** | 8 | - | NEG -$22.5M | - | 180 | 170 | -$459k | - | out (clean 25, ADX 11, RVol 1.0) |
| 25 | **SHOP** | 148.21 | - | **-** | 8 | - | NEG -$3.1M | 150.54 | 150 | 150 | -$32k | - | out (clean 37, ADX 26, RVol 0.7) |
| 26 | **BABA** | 108.97 | - | **-** | 7 | - | POS +$26.4M | 105.16 | 110 | 110 | -$262k | - | out (clean 34, ADX 19, RVol 0.4) |
| 27 | **UBER** | 69.75 | - | **-** | 5 | - | POS +$12.8M | 68.73 | 70 | 70 | +$70k | - | out (clean 30, ADX 10, RVol 0.4) |

## Big prints this scan (157)
- **NVDA** PUT 192.5 2026-11-06 (0DTE): 1,250 @ 3.20 = **+$400k** SELL | vol 45,419 / OI 6,354
- **QQQ** PUT 660 2026-11-06 (0DTE): 1,170 @ 3.12 = **+$365k** SELL | vol 73,876 / OI 12,054
- **NVDA** PUT 192.5 2026-11-06 (0DTE): 668 @ 3.70 = **+$247k** SELL | vol 45,419 / OI 6,354
- **MU** CALL 680 2026-11-06 (0DTE): 100 @ 20.95 = **+$210k** BUY | vol 2,987 / OI 21
- **MU** CALL 680 2026-11-06 (0DTE): 99 @ 21.00 = **+$208k** BUY | vol 2,987 / OI 21
- **MU** CALL 692.5 2026-11-09 (3DTE): 80 @ 24.80 = **+$198k** BUY | vol 418 / OI 0
- **QQQ** PUT 655 2026-11-06 (0DTE): 1,170 @ 1.50 = **+$176k** SELL | vol 69,481 / OI 6,673
- **QQQ** PUT 660 2026-11-06 (0DTE): 565 @ 3.10 = **+$175k** SELL | vol 73,876 / OI 12,054
- **SPY** PUT 741 2026-11-06 (0DTE): 597 @ 2.78 = **+$166k** SELL | vol 34,037 / OI 4,188
- **QQQ** PUT 661 2026-11-06 (0DTE): 400 @ 3.91 = **+$156k** SELL | vol 35,956 / OI 371
- **SPY** PUT 740 2026-11-06 (0DTE): 597 @ 2.34 = **+$140k** SELL | vol 82,483 / OI 21,704
- **QQQ** PUT 660 2026-11-09 (3DTE): 200 @ 6.90 = **+$138k** SELL | vol 10,046 / OI 1,084
- **SPY** PUT 741 2026-11-06 (0DTE): 477 @ 2.78 = **+$133k** SELL | vol 34,037 / OI 4,188
- **SPY** CALL 740 2026-11-06 (0DTE): 400 @ 3.21 = **+$128k** BUY | vol 166,004 / OI 314
- **AMD** CALL 450 2026-11-06 (0DTE): 234 @ 5.45 = **+$128k** BUY | vol 12,779 / OI 246

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 701 2026-11-09 (3DTE): 517 traded vs OI 406
- **SPY** CALL 769 2026-11-10 (4DTE): 638 traded vs OI 345
- **SPY** CALL 766 2026-11-06 (0DTE): 7,517 traded vs OI 7,295
- **SPY** CALL 766 2026-11-10 (4DTE): 642 traded vs OI 576
- **SPY** CALL 757 2026-11-10 (4DTE): 516 traded vs OI 106
- **SPY** PUT 680 2026-11-06 (0DTE): 2,398 traded vs OI 2,143
- **SPY** CALL 767 2026-11-06 (0DTE): 6,611 traded vs OI 5,718
- **SPY** CALL 767 2026-11-10 (4DTE): 784 traded vs OI 530
- **SPY** CALL 755 2026-11-12 (6DTE): 515 traded vs OI 331
- **SPY** CALL 761 2026-11-10 (4DTE): 528 traded vs OI 87
- **SPY** CALL 762 2026-11-13 (7DTE): 1,343 traded vs OI 1,311
- **QQQ** PUT 642 2026-11-09 (3DTE): 716 traded vs OI 0
- **QQQ** PUT 638 2026-11-09 (3DTE): 526 traded vs OI 0
- **QQQ** CALL 702 2026-11-06 (0DTE): 2,625 traded vs OI 2,073
- **QQQ** PUT 635 2026-11-13 (7DTE): 1,386 traded vs OI 1,352

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
