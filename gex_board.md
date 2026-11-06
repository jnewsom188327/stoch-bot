# GEX + FLOW SCAN - Fri Nov 06, 12:35 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (3)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:30 | **NVDA** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/06 192.5C | 0.73 | 0.28 | +12% (20m) | **-62%** (done) | +199% | 193.9 |
| 10:00 | **NVDA** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/06 197.5C | 0.67 | 0.03 | -6% (1m) | **-96%** (done) | +24% | 195 |
| 09:50 | **NFLX** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/06 64C | 0.40 | 0.36 | +32% (4m) | **-10%** (done) | +164% | 65 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 12:35:08 ET, last candle SPY 12:34, QQQ 12:34 | no errors

## Flow surges NOT fired - price disagreed (6 today, last 5)
- 09:55 SMCI PUTS: price +0.09 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 HOOD PUTS: price +3.27 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 MSTR PUTS: price +3.75 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 SMCI PUTS: price +0.89 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 PLTR PUTS: price +5.57 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **NFLX** | 63.93 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 34 | none: 26 puts 0-7DTE > 1 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only +16% at the target (needs +20%) (19 contracts' greeks worked out here) | POS +$1.4M | 63.89 | 64 | 65 | -$337k | +$0 bull / -$33k bear | out (clean 32, ADX 14, RVol 0.5) |
| 2 | **AAPL** | 344.19 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 33 | none: 112 calls 0-7DTE > 5 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only +0% at the target (needs +20%) (50 contracts' greeks worked out here) | POS +$3.4M | 344.12 | 350 | 345 | -$16.3M | +$56k bull / -$148k bear | out (clean 28, ADX 8, RVol 0.2) |
| 3 | **SHOP** | 149.83 | FLIP CROSS down into negative gamma | **PUTS** | 33 | 11/06 149P @ 0.66 (delta 0.36) = est +63% at 148.29 | NEG -$836k | 150.31 | 150 | 150 | -$1.3M | - | out (clean 36, ADX 31, RVol 0.6) |
| 4 | **MSFT** | 534.24 | PINNED between the walls (positive gamma) - chop | **-** | 26 | - | POS +$679.7M | 512.47 | 535 | 535 | +$3.0M | +$0 bull / -$38k bear | out (clean 33, ADX 10, RVol 0.3) |
| 5 | **TSLA** | 360.06 | - | **-** | 21 | - | NEG -$304.5M | - | 370 | 360 | -$65.6M | +$423k bull / -$108k bear | out (clean 35, ADX 32, RVol 0.3) |
| 6 | **MSTR** | 128.18 | - | **-** | 21 | - | POS +$2.6M | 127.99 | 135 | 125 | -$8.5M | +$68k bull / -$1.4M bear | out (clean 31, ADX 13, RVol 0.6) |
| 7 | **DELL** | 333.60 | - | **-** | 19 | - | NEG -$28.3M | - | 335 | 335 | +$4.7M | +$0 bull / -$60k bear | out (clean 32, ADX 7, RVol 0.3) |
| 8 | **SMH** | 462.96 | - | **-** | 18 | - | NEG -$534.5M | - | 505 | 465 | +$7.5M | +$82k bull / +$0 bear | out (clean 33, ADX 9, RVol 0.3) |
| 9 | **PLTR** | 161.21 | - | **-** | 17 | - | NEG -$73.2M | - | 165 | 160 | +$3.1M | +$0 bull / -$97k bear | out (clean 28, ADX 19, RVol 0.5) |
| 10 | **META** | 618.09 | - | **-** | 16 | - | NEG -$115.8M | 622.92 | 620 | 610 | -$5.8M | +$370k bull / -$87k bear | out (clean 33, ADX 20, RVol 0.4) |
| 11 | **AVGO** | 294.11 | - | **-** | 16 | - | NEG -$138.0M | - | 320 | 300 | +$4.0M | +$294k bull / +$0 bear | out (clean 31, ADX 12, RVol 0.5) |
| 12 | **MU** | 693.63 | - | **-** | 16 | - | NEG -$189.6M | - | 700 | 700 | +$67.8M | +$2.3M bull / -$448k bear | out (clean 32, ADX 8, RVol 0.3) |
| 13 | **NVDA** | 187.85 | - | **-** | 15 | - | NEG -$401.1M | - | 200 | 190 | +$23.0M | +$1.6M bull / -$169k bear | out (clean 33, ADX 9, RVol 0.6) |
| 14 | **AMD** | 442.12 | - | **-** | 15 | - | NEG -$179.8M | - | 430 | 450 | +$13.7M | +$1.1M bull / +$0 bear | out (clean 32, ADX 13, RVol 0.4) |
| 15 | **AMZN** | 261.97 | - | **-** | 15 | - | POS +$346.9M | - | 265 | 260 | -$433k | +$222k bull / -$37k bear | out (clean 34, ADX 20, RVol 0.3) |
| 16 | **HOOD** | 79.84 | - | **-** | 15 | - | NEG -$24.5M | 83.73 | 85 | 80 | +$1.8M | +$63k bull / -$97k bear | out (clean 30, ADX 14, RVol 0.4) |
| 17 | **SPY** | 739.00 | - | **-** | 14 | - | NEG -$15.0B | 769.1 | 760 | 740 | -$51.1M | +$113k bull / -$103k bear | out (clean 34, ADX 10, RVol 0.5) |
| 18 | **QQQ** | 658.53 | - | **-** | 14 | - | NEG -$5.6B | - | 700 | 680 | +$34.1M | +$172k bull / -$968k bear | out (clean 34, ADX 12, RVol 0.5) |
| 19 | **ORCL** | 116.46 | - | **-** | 14 | - | NEG -$77.1M | - | 125 | 115 | +$755k | +$27k bull / -$27k bear | out (clean 30, ADX 6, RVol 0.3) |
| 20 | **COIN** | 133.91 | - | **-** | 11 | - | NEG -$18.2M | 136.43 | 142 | 135 | -$3.8M | - | out (clean 32, ADX 13, RVol 0.3) |
| 21 | **CRM** | 214.84 | - | **-** | 8 | - | NEG -$21.6M | - | 230 | 215 | -$342k | - | out (clean 35, ADX 19, RVol 0.7) |
| 22 | **BABA** | 108.89 | - | **-** | 8 | - | POS +$33.5M | - | 110 | 110 | -$469k | - | out (clean 34, ADX 17, RVol 0.4) |
| 23 | **IWM** | 273.86 | - | **-** | 7 | - | NEG -$3.3B | 285.86 | 275 | 270 | -$5.2M | - | out (clean 34, ADX 21, RVol 0.8) |
| 24 | **SMCI** | 28.43 | - | **-** | 6 | - | NEG -$4.5M | - | 30 | 30 | -$422k | - | out (clean 34, ADX 15, RVol 0.2) |
| 25 | **ARM** | 172.84 | - | **-** | 6 | - | NEG -$25.0M | - | 190 | 170 | -$407k | - | out (clean 25, ADX 10, RVol 0.6) |
| 26 | **UBER** | 69.36 | - | **-** | 6 | - | POS +$11.8M | 68.71 | 70 | 70 | +$109k | - | out (clean 30, ADX 14, RVol 0.4) |
| 27 | **GOOGL** | 286.80 | - | **-** | 4 | - | POS +$55.1M | 284.65 | 285 | 290 | +$1.2M | - | out (clean 34, ADX 12, RVol 0.5) |

## Big prints this scan (40)
- **TSLA** PUT 362.5 2026-11-06 (0DTE): 542 @ 3.70 = **+$201k** SELL | vol 12,019 / OI 1,629
- **AVGO** PUT 305 2026-11-06 (0DTE): 168 @ 9.80 = **+$165k** SELL | vol 1,559 / OI 1,466
- **AVGO** PUT 305 2026-11-06 (0DTE): 132 @ 9.80 = **+$129k** SELL | vol 1,559 / OI 1,466
- **NVDA** CALL 187.5 2026-11-06 (0DTE): 860 @ 1.46 = **+$126k** BUY | vol 23,919 / OI 72
- **SPY** PUT 740 2026-11-06 (0DTE): 470 @ 2.41 = **+$113k** SELL | vol 159,830 / OI 21,704
- **NVDA** PUT 185 2026-11-06 (0DTE): 3,000 @ 0.37 = **+$111k** SELL | vol 100,862 / OI 17,457
- **MU** PUT 675 2026-11-09 (3DTE): 80 @ 13.10 = **+$105k** SELL | vol 796 / OI 0
- **AMZN** CALL 265 2026-11-13 (7DTE): 201 @ 4.28 = **+$86k** MID | vol 6,230 / OI 2,381
- **MU** CALL 717.5 2026-11-13 (7DTE): 30 @ 27.05 = **+$81k** BUY | vol 348 / OI 0
- **TSLA** CALL 360 2026-11-11 (5DTE): 72 @ 9.43 = **+$68k** SELL | vol 1,814 / OI 5
- **NVDA** PUT 190 2026-11-13 (7DTE): 80 @ 7.32 = **+$59k** SELL | vol 9,618 / OI 9,756
- **AMZN** PUT 255 2026-11-13 (7DTE): 201 @ 2.90 = **+$58k** SELL | vol 812 / OI 1,003
- **SMH** CALL 475 2026-11-13 (7DTE): 50 @ 11.08 = **+$55k** BUY | vol 355 / OI 0
- **AAPL** PUT 340 2026-11-13 (7DTE): 135 @ 4.00 = **+$54k** BUY | vol 2,177 / OI 3,565
- **MU** CALL 700 2026-11-06 (0DTE): 100 @ 5.25 = **+$52k** BUY | vol 29,580 / OI 67

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 715 2026-11-13 (7DTE): 1,943 traded vs OI 1,935
- **QQQ** CALL 661 2026-11-11 (5DTE): 512 traded vs OI 1
- **QQQ** CALL 667 2026-11-10 (4DTE): 501 traded vs OI 29
- **QQQ** PUT 666 2026-11-09 (3DTE): 530 traded vs OI 84
- **QQQ** PUT 630 2026-11-10 (4DTE): 883 traded vs OI 114
- **QQQ** PUT 635 2026-11-10 (4DTE): 837 traded vs OI 826
- **IWM** PUT 269 2026-11-13 (7DTE): 515 traded vs OI 476
- **META** CALL 650 2026-11-06 (0DTE): 4,076 traded vs OI 3,967
- **META** CALL 605 2026-11-06 (0DTE): 515 traded vs OI 326
- **AVGO** PUT 305 2026-11-06 (0DTE): 1,559 traded vs OI 1,466
- **MSTR** PUT 121 2026-11-06 (0DTE): 846 traded vs OI 839

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
