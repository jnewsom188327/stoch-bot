# GEX + FLOW SCAN - Fri Nov 06, 10:30 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (3)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:30 | **NVDA** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/06 192.5C | 0.73 | 0.72 | -1% (0m) | **-1%** | +199% | 193.9 |
| 10:00 | **NVDA** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/06 197.5C | 0.67 | 0.12 | -6% (1m) | **-82%** | +24% | 195 |
| 09:50 | **NFLX** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/06 64C | 0.40 | 0.29 | +32% (4m) | **-28%** | +164% | 65 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:30:08 ET, last candle SPY 10:29, QQQ 10:29 | no errors

## Flow surges NOT fired - price disagreed (6 today, last 5)
- 09:55 SMCI PUTS: price +0.09 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 HOOD PUTS: price +3.27 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 MSTR PUTS: price +3.75 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 SMCI PUTS: price +0.89 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 PLTR PUTS: price +5.57 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **NVDA** | 190.03 | RUN: clean trend + negative gamma + flow agrees | **CALLS** | 61 | 11/06 192.5C @ 0.73 (delta 0.28) = est +199% at 193.9 | NEG -$378.0M | - | 200 | 190 | +$25.9M | +$3.0M bull / -$40k bear | LONG (clean 34, ADX 33, RVol 1.2) |
| 2 | **CRM** | 211.67 | FLOW SURGE | **CALLS** | 51 | none: 32 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (25 contracts' greeks worked out here) | NEG -$20.9M | - | 230 | 220 | +$389k | +$31k bull / +$0 bear | SHORT (clean 34, ADX 40, RVol 1.5) |
| 3 | **DELL** | 334.96 | FLOW SURGE | **CALLS** | 49 | none: 48 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (37 contracts' greeks worked out here) | NEG -$23.6M | - | 340 | 340 | +$3.6M | +$633k bull / -$25k bear | out (clean 32, ADX 24, RVol 2.4) |
| 4 | **TSLA** | 359.97 | TREND (flow not with it) | **CALLS** | 47 | none: 116 calls 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (52 contracts' greeks worked out here) | NEG -$268.7M | - | 370 | 360 | -$71.2M | +$7.8M bull / -$4.7M bear | LONG (clean 36, ADX 45, RVol 1.0) |
| 5 | **SMCI** | 28.77 | RUN: clean trend + negative gamma + flow agrees | **CALLS** | 43 | 11/06 28.5C @ 0.46 (delta 0.64) = est +240% at 30 | NEG -$3.7M | - | 30 | 30 | +$28k | - | LONG (clean 35, ADX 35, RVol 0.6) |
| 6 | **MSTR** | 126.99 | FLIP CROSS down into negative gamma | **PUTS** | 36 | 11/06 123P @ 0.76 (delta 0.23) = est +31% at 125 | NEG -$3.3M | 127.3 | 135 | 125 | -$2.6M | +$51k bull / -$2.1M bear | out (clean 32, ADX 19, RVol 1.0) |
| 7 | **MU** | 691.33 | - | **-** | 26 | - | NEG -$172.2M | - | 700 | 700 | +$91.4M | +$15.1M bull / +$0 bear | out (clean 32, ADX 19, RVol 2.0) |
| 8 | **META** | 619.46 | TREND (flow not with it) | **CALLS** | 25 | none: 196 calls 0-7DTE > 9 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (88 contracts' greeks worked out here) | NEG -$76.3M | 623.15 | 650 | 625 | -$8.3M | +$138k bull / -$466k bear | LONG (clean 33, ADX 36, RVol 0.5) |
| 9 | **HOOD** | 79.48 | - | **-** | 24 | - | NEG -$18.4M | - | 85 | 80 | +$2.8M | +$29k bull / -$91k bear | out (clean 29, ADX 30, RVol 1.0) |
| 10 | **SMH** | 462.51 | - | **-** | 23 | - | NEG -$486.7M | - | 505 | 475 | +$3.5M | +$889k bull / +$0 bear | out (clean 34, ADX 20, RVol 3.1) |
| 11 | **AMZN** | 262.70 | - | **-** | 23 | - | POS +$367.3M | - | 265 | 260 | -$4.6M | +$123k bull / -$422k bear | out (clean 34, ADX 28, RVol 0.5) |
| 12 | **AAPL** | 343.26 | - | **-** | 21 | - | POS +$35.4M | 342.81 | 350 | 345 | -$8.2M | +$147k bull / -$1.5M bear | out (clean 30, ADX 18, RVol 1.1) |
| 13 | **GOOGL** | 286.99 | - | **-** | 21 | - | POS +$50.2M | 284.68 | 285 | 290 | +$3.0M | +$326k bull / -$339k bear | out (clean 34, ADX 27, RVol 1.0) |
| 14 | **AVGO** | 297.02 | - | **-** | 21 | - | NEG -$137.8M | - | 325 | 300 | +$1.9M | +$145k bull / +$0 bear | out (clean 30, ADX 23, RVol 1.9) |
| 15 | **PLTR** | 160.50 | - | **-** | 21 | - | NEG -$65.7M | - | 165 | 160 | +$1.4M | +$148k bull / +$0 bear | out (clean 28, ADX 36, RVol 1.0) |
| 16 | **COIN** | 134.90 | - | **-** | 21 | - | NEG -$8.3M | 136.06 | 142 | 130 | -$2.2M | +$3.8M bull / +$0 bear | out (clean 31, ADX 16, RVol 0.3) |
| 17 | **BABA** | 108.81 | - | **-** | 20 | - | POS +$27.2M | 103.15 | 110 | 110 | -$249k | +$27k bull / +$0 bear | out (clean 35, ADX 19, RVol 1.2) |
| 18 | **SPY** | 738.98 | - | **-** | 19 | - | NEG -$14.1B | 769.84 | 770 | 740 | -$69.0M | +$762k bull / -$2.1M bear | out (clean 35, ADX 20, RVol 1.1) |
| 19 | **AMD** | 442.29 | - | **-** | 19 | - | NEG -$167.1M | - | 430 | 450 | +$4.6M | +$2.3M bull / +$0 bear | out (clean 32, ADX 28, RVol 1.5) |
| 20 | **ORCL** | 116.61 | - | **-** | 19 | - | NEG -$69.6M | - | 125 | 115 | +$586k | +$58k bull / -$100k bear | out (clean 30, ADX 15, RVol 0.8) |
| 21 | **QQQ** | 658.19 | - | **-** | 18 | - | NEG -$5.6B | - | 700 | 680 | +$40.1M | +$4.8M bull / -$795k bear | out (clean 35, ADX 24, RVol 1.1) |
| 22 | **IWM** | 272.64 | - | **-** | 18 | - | NEG -$3.4B | 286.1 | 285 | 270 | -$4.0M | +$56k bull / +$0 bear | out (clean 35, ADX 17, RVol 1.1) |
| 23 | **NFLX** | 63.83 | - | **-** | 18 | - | POS +$12.1M | 63.33 | 63 | 64 | -$131k | +$52k bull / +$0 bear | out (clean 32, ADX 25, RVol 0.8) |
| 24 | **UBER** | 69.72 | - | **-** | 18 | - | POS +$10.5M | 69.11 | 70 | 70 | +$86k | +$0 bull / -$397k bear | out (clean 30, ADX 12, RVol 1.1) |
| 25 | **MSFT** | 532.71 | - | **-** | 17 | - | POS +$608.0M | 511.07 | 535 | 535 | +$72k | +$286k bull / -$775k bear | out (clean 32, ADX 30, RVol 0.9) |
| 26 | **ARM** | 173.51 | - | **-** | 10 | - | NEG -$22.2M | - | 190 | 170 | -$415k | - | out (clean 25, ADX 15, RVol 0.8) |
| 27 | **SHOP** | 147.24 | - | **-** | 7 | - | NEG -$2.1M | 149.91 | 144 | 145 | -$8k | - | out (clean 37, ADX 24, RVol 0.8) |

## Big prints this scan (330)
- **MU** PUT 690 2026-11-13 (7DTE): 598 @ 30.80 = **+$1.8M** SELL | vol 809 / OI 272
- **TSLA** PUT 360 2026-11-13 (7DTE): 1,000 @ 11.88 = **+$1.2M** SELL | vol 1,164 / OI 1,235
- **TSLA** CALL 377.5 2026-11-13 (7DTE): 1,500 @ 4.50 = **+$675k** MID | vol 11,257 / OI 221
- **TSLA** PUT 342.5 2026-11-13 (7DTE): 1,000 @ 5.69 = **+$569k** SELL | vol 1,373 / OI 434
- **TSLA** CALL 377.5 2026-11-13 (7DTE): 1,000 @ 4.65 = **+$465k** BUY | vol 11,257 / OI 221
- **TSLA** CALL 377.5 2026-11-13 (7DTE): 834 @ 5.00 = **+$417k** BUY | vol 11,257 / OI 221
- **TSLA** CALL 350 2026-11-06 (0DTE): 400 @ 10.01 = **+$400k** BUY | vol 15,136 / OI 1,342
- **TSLA** CALL 365 2026-11-13 (7DTE): 338 @ 9.40 = **+$318k** BUY | vol 3,071 / OI 322
- **TSLA** CALL 355 2026-11-06 (0DTE): 494 @ 6.00 = **+$296k** BUY | vol 42,845 / OI 250
- **MU** CALL 712.5 2026-11-13 (7DTE): 90 @ 31.58 = **+$284k** BUY | vol 190 / OI 5
- **MU** PUT 710 2026-11-13 (7DTE): 64 @ 40.80 = **+$261k** SELL | vol 377 / OI 603
- **AAPL** CALL 332.5 2026-11-06 (0DTE): 277 @ 9.41 = **+$261k** SELL | vol 387 / OI 1,379
- **MU** CALL 717.5 2026-11-06 (0DTE): 374 @ 6.95 = **+$260k** BUY | vol 3,883 / OI 0
- **TSLA** PUT 360 2026-11-06 (0DTE): 592 @ 3.95 = **+$234k** SELL | vol 4,702 / OI 9,936
- **QQQ** PUT 656 2026-11-13 (7DTE): 200 @ 11.56 = **+$231k** SELL | vol 338 / OI 198

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 720 2026-11-06 (0DTE): 500 traded vs OI 65
- **SPY** CALL 759 2026-11-11 (5DTE): 514 traded vs OI 69
- **SPY** CALL 744 2026-11-10 (4DTE): 505 traded vs OI 24
- **SPY** PUT 703 2026-11-09 (3DTE): 702 traded vs OI 690
- **SPY** CALL 757 2026-11-13 (7DTE): 594 traded vs OI 499
- **SPY** PUT 710 2026-11-13 (7DTE): 5,225 traded vs OI 3,271
- **QQQ** CALL 684 2026-11-09 (3DTE): 576 traded vs OI 89
- **QQQ** CALL 677 2026-11-09 (3DTE): 531 traded vs OI 23
- **QQQ** PUT 617 2026-11-06 (0DTE): 512 traded vs OI 0
- **QQQ** CALL 717 2026-11-09 (3DTE): 533 traded vs OI 119
- **QQQ** PUT 664 2026-11-06 (0DTE): 7,535 traded vs OI 6,969
- **QQQ** PUT 600 2026-11-10 (4DTE): 501 traded vs OI 54
- **QQQ** PUT 655 2026-11-10 (4DTE): 582 traded vs OI 581
- **QQQ** PUT 653 2026-11-09 (3DTE): 566 traded vs OI 257
- **QQQ** CALL 693 2026-11-09 (3DTE): 582 traded vs OI 299

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
