# GEX + FLOW SCAN - Fri Nov 06, 12:10 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (3)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:30 | **NVDA** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/06 192.5C | 0.73 | 0.28 | +12% (20m) | **-62%** (done) | +199% | 193.9 |
| 10:00 | **NVDA** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/06 197.5C | 0.67 | 0.03 | -6% (1m) | **-96%** (done) | +24% | 195 |
| 09:50 | **NFLX** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/06 64C | 0.40 | 0.36 | +32% (4m) | **-10%** (done) | +164% | 65 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 12:10:08 ET, last candle SPY 12:09, QQQ 12:09 | no errors

## Flow surges NOT fired - price disagreed (6 today, last 5)
- 09:55 SMCI PUTS: price +0.09 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 HOOD PUTS: price +3.27 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 MSTR PUTS: price +3.75 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 SMCI PUTS: price +0.89 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 PLTR PUTS: price +5.57 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **MSFT** | 534.38 | PINNED between the walls (positive gamma) - chop | **-** | 28 | - | POS +$724.4M | 511.58 | 535 | 535 | +$2.8M | +$188k bull / -$46k bear | out (clean 33, ADX 14, RVol 0.5) |
| 2 | **NFLX** | 63.98 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 24 | none: 26 puts 0-7DTE > 1 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only -3% at the target (needs +20%) (21 contracts' greeks worked out here) | POS +$4.4M | 63.86 | 64 | 65 | -$274k | - | out (clean 32, ADX 12, RVol 0.7) |
| 3 | **TSLA** | 360.08 | - | **-** | 23 | - | NEG -$284.4M | - | 370 | 360 | -$71.3M | +$738k bull / -$174k bear | out (clean 35, ADX 37, RVol 0.7) |
| 4 | **COIN** | 134.40 | - | **-** | 22 | - | NEG -$20.3M | 136.99 | 141 | 135 | -$3.7M | +$0 bull / -$43k bear | out (clean 31, ADX 17, RVol 0.3) |
| 5 | **MSTR** | 128.57 | - | **-** | 21 | - | POS +$10.5M | 127.73 | 135 | 125 | -$8.2M | +$0 bull / -$730k bear | out (clean 30, ADX 12, RVol 0.5) |
| 6 | **IWM** | 273.70 | - | **-** | 18 | - | NEG -$3.3B | 285.68 | 285 | 270 | -$6.1M | +$57k bull / +$0 bear | out (clean 34, ADX 23, RVol 0.5) |
| 7 | **SMH** | 463.98 | - | **-** | 18 | - | NEG -$552.0M | - | 505 | 465 | +$7.1M | +$325k bull / -$47k bear | out (clean 33, ADX 12, RVol 0.3) |
| 8 | **AAPL** | 343.78 | - | **-** | 18 | - | POS +$46.0M | 343.34 | 350 | 345 | -$16.2M | +$274k bull / -$45k bear | out (clean 28, ADX 9, RVol 0.3) |
| 9 | **META** | 619.61 | - | **-** | 18 | - | NEG -$75.9M | 622.61 | 650 | 625 | -$8.0M | +$507k bull / +$0 bear | out (clean 33, ADX 27, RVol 0.3) |
| 10 | **PLTR** | 161.05 | - | **-** | 18 | - | NEG -$69.0M | - | 165 | 160 | +$3.1M | +$349k bull / +$0 bear | out (clean 28, ADX 22, RVol 0.4) |
| 11 | **SHOP** | 149.73 | - | **-** | 18 | - | NEG -$1.7M | 150.55 | 150 | 150 | -$7k | +$43k bull / +$0 bear | out (clean 36, ADX 35, RVol 0.6) |
| 12 | **AMZN** | 262.26 | - | **-** | 16 | - | POS +$405.0M | - | 265 | 260 | -$2.1M | +$112k bull / +$0 bear | out (clean 34, ADX 20, RVol 0.4) |
| 13 | **SMCI** | 28.61 | - | **-** | 16 | - | NEG -$4.9M | - | 30 | 29 | +$245k | +$0 bull / -$36k bear | out (clean 34, ADX 16, RVol 0.2) |
| 14 | **MU** | 695.91 | - | **-** | 16 | - | NEG -$185.1M | - | 700 | 700 | +$59.5M | +$2.3M bull / -$2.5M bear | out (clean 32, ADX 10, RVol 0.5) |
| 15 | **HOOD** | 79.99 | - | **-** | 16 | - | NEG -$24.3M | 84.23 | 85 | 80 | +$1.8M | +$33k bull / -$33k bear | out (clean 30, ADX 17, RVol 0.3) |
| 16 | **SPY** | 738.92 | - | **-** | 15 | - | NEG -$14.4B | 768.23 | 770 | 740 | -$48.3M | +$908k bull / -$628k bear | out (clean 34, ADX 12, RVol 0.7) |
| 17 | **NVDA** | 188.41 | - | **-** | 15 | - | NEG -$374.9M | - | 200 | 190 | +$20.2M | +$2.1M bull / -$488k bear | out (clean 34, ADX 11, RVol 0.6) |
| 18 | **AMD** | 443.69 | - | **-** | 15 | - | NEG -$182.4M | - | 430 | 450 | +$9.4M | +$1.1M bull / -$365k bear | out (clean 32, ADX 16, RVol 0.6) |
| 19 | **AVGO** | 295.35 | - | **-** | 15 | - | NEG -$133.2M | - | 320 | 300 | +$2.0M | +$286k bull / +$0 bear | out (clean 31, ADX 9, RVol 0.8) |
| 20 | **QQQ** | 659.08 | - | **-** | 14 | - | NEG -$5.2B | - | 700 | 680 | +$25.5M | +$3.2M bull / -$116k bear | out (clean 35, ADX 16, RVol 0.4) |
| 21 | **DELL** | 334.06 | - | **-** | 9 | - | NEG -$26.3M | - | 340 | 335 | +$4.4M | - | out (clean 32, ADX 8, RVol 0.4) |
| 22 | **BABA** | 109.04 | - | **-** | 9 | - | POS +$35.2M | - | 110 | 110 | -$522k | - | out (clean 34, ADX 21, RVol 0.5) |
| 23 | **CRM** | 215.26 | - | **-** | 8 | - | NEG -$22.1M | - | 230 | 215 | -$372k | - | out (clean 35, ADX 20, RVol 0.3) |
| 24 | **ARM** | 172.75 | - | **-** | 7 | - | NEG -$26.6M | - | 190 | 170 | -$447k | - | out (clean 25, ADX 12, RVol 0.4) |
| 25 | **UBER** | 69.44 | - | **-** | 6 | - | POS +$12.8M | 68.64 | 70 | 70 | +$120k | - | out (clean 30, ADX 8, RVol 0.5) |
| 26 | **GOOGL** | 286.12 | - | **-** | 4 | - | POS +$92.5M | 283.02 | 285 | 285 | +$1.1M | - | out (clean 34, ADX 13, RVol 0.5) |
| 27 | **ORCL** | 116.48 | - | **-** | 4 | - | NEG -$80.8M | - | 125 | 115 | +$581k | - | out (clean 30, ADX 7, RVol 0.4) |

## Big prints this scan (51)
- **SPY** CALL 740 2026-11-06 (0DTE): 1,000 @ 2.35 = **+$235k** BUY | vol 232,775 / OI 314
- **IWM** CALL 268 2026-11-06 (0DTE): 400 @ 5.65 = **+$226k** MID | vol 1,106 / OI 64
- **TSLA** PUT 362.5 2026-11-06 (0DTE): 642 @ 2.95 = **+$189k** SELL | vol 9,283 / OI 1,629
- **SMH** PUT 467.5 2026-11-13 (7DTE): 97 @ 17.15 = **+$166k** SELL | vol 1,125 / OI 52
- **MU** CALL 700 2026-11-06 (0DTE): 268 @ 6.20 = **+$166k** BUY | vol 25,844 / OI 67
- **QQQ** CALL 660 2026-11-06 (0DTE): 475 @ 3.15 = **+$150k** BUY | vol 134,776 / OI 330
- **QQQ** CALL 640 2026-11-13 (7DTE): 50 @ 26.44 = **+$132k** MID | vol 81 / OI 39
- **META** PUT 600 2026-11-09 (3DTE): 610 @ 2.15 = **+$131k** SELL | vol 1,643 / OI 517
- **QQQ** CALL 660 2026-11-06 (0DTE): 408 @ 3.20 = **+$131k** BUY | vol 134,776 / OI 330
- **NVDA** PUT 187.5 2026-11-13 (7DTE): 193 @ 5.97 = **+$115k** BUY | vol 3,362 / OI 3,561
- **NVDA** PUT 190 2026-11-09 (3DTE): 240 @ 4.40 = **+$106k** BUY | vol 12,154 / OI 1,554
- **SPY** CALL 750 2026-11-13 (7DTE): 250 @ 4.13 = **+$103k** BUY | vol 7,531 / OI 350
- **MU** PUT 720 2026-11-06 (0DTE): 40 @ 22.65 = **+$91k** SELL | vol 3,065 / OI 857
- **AMD** CALL 450 2026-11-09 (3DTE): 80 @ 10.40 = **+$83k** BUY | vol 2,968 / OI 29
- **MU** CALL 700 2026-11-13 (7DTE): 20 @ 35.87 = **+$72k** MID | vol 993 / OI 38

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 781 2026-11-11 (5DTE): 562 traded vs OI 411
- **SPY** CALL 789 2026-11-12 (6DTE): 1,862 traded vs OI 394
- **SPY** CALL 742 2026-11-12 (6DTE): 504 traded vs OI 0
- **SPY** CALL 787 2026-11-12 (6DTE): 687 traded vs OI 394
- **SPY** CALL 740 2026-11-16 (10DTE): 508 traded vs OI 5
- **SPY** CALL 740 2026-11-20 (14DTE): 2,615 traded vs OI 2,583
- **IWM** CALL 270 2026-11-13 (7DTE): 510 traded vs OI 149
- **SMH** CALL 495 2026-11-11 (5DTE): 1,372 traded vs OI 0
- **AAPL** CALL 375 2026-11-20 (14DTE): 599 traded vs OI 0
- **META** PUT 590 2026-11-09 (3DTE): 1,001 traded vs OI 109
- **AMZN** PUT 252.5 2026-11-09 (3DTE): 501 traded vs OI 246
- **AMZN** CALL 267.5 2026-11-13 (7DTE): 3,486 traded vs OI 3,410
- **MSFT** CALL 545 2026-11-06 (0DTE): 6,635 traded vs OI 5,656
- **COIN** PUT 135 2026-11-13 (7DTE): 782 traded vs OI 777
- **ORCL** PUT 105 2026-11-13 (7DTE): 610 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
