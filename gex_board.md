# GEX + FLOW SCAN - Fri Nov 06, 11:50 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (3)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:30 | **NVDA** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/06 192.5C | 0.73 | 0.28 | +12% (20m) | **-62%** (done) | +199% | 193.9 |
| 10:00 | **NVDA** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/06 197.5C | 0.67 | 0.03 | -6% (1m) | **-96%** (done) | +24% | 195 |
| 09:50 | **NFLX** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/06 64C | 0.40 | 0.36 | +32% (4m) | **-10%** (done) | +164% | 65 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 11:50:08 ET, last candle SPY 11:49, QQQ 11:49 | no errors

## Flow surges NOT fired - price disagreed (6 today, last 5)
- 09:55 SMCI PUTS: price +0.09 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 HOOD PUTS: price +3.27 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 MSTR PUTS: price +3.75 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 SMCI PUTS: price +0.89 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 PLTR PUTS: price +5.57 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **MSFT** | 535.71 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 34 | 11/06 540C @ 0.74 (delta 0.22) = est +138% at 540 | POS +$677.8M | 510.86 | 540 | 535 | +$1.9M | +$980k bull / +$0 bear | out (clean 33, ADX 16, RVol 0.6) |
| 2 | **TSLA** | 360.91 | - | **-** | 24 | - | NEG -$273.9M | - | 370 | 360 | -$73.5M | +$287k bull / -$551k bear | out (clean 35, ADX 38, RVol 0.7) |
| 3 | **COIN** | 133.79 | - | **-** | 22 | - | NEG -$20.1M | 136.86 | 142 | 130 | -$3.3M | +$0 bull / -$994k bear | out (clean 31, ADX 20, RVol 0.5) |
| 4 | **MSTR** | 128.13 | - | **-** | 21 | - | POS +$3.2M | 127.86 | 135 | 125 | -$7.3M | +$0 bull / -$2.0M bear | out (clean 31, ADX 12, RVol 0.5) |
| 5 | **DELL** | 333.56 | - | **-** | 20 | - | NEG -$25.3M | - | 340 | 335 | +$4.4M | +$117k bull / -$25k bear | out (clean 33, ADX 11, RVol 0.5) |
| 6 | **CRM** | 216.30 | - | **-** | 20 | - | NEG -$25.4M | - | 230 | 220 | -$472k | +$0 bull / -$29k bear | out (clean 34, ADX 24, RVol 0.4) |
| 7 | **AAPL** | 343.89 | - | **-** | 19 | - | POS +$38.0M | 343.43 | 350 | 345 | -$17.4M | +$471k bull / +$0 bear | out (clean 29, ADX 11, RVol 0.5) |
| 8 | **META** | 620.45 | - | **-** | 19 | - | NEG -$69.5M | 623.18 | 650 | 625 | -$8.1M | +$58k bull / -$657k bear | out (clean 33, ADX 32, RVol 0.7) |
| 9 | **BABA** | 109.09 | - | **-** | 19 | - | POS +$30.3M | - | 110 | 110 | -$463k | +$0 bull / -$57k bear | out (clean 34, ADX 21, RVol 0.9) |
| 10 | **SMH** | 464.75 | - | **-** | 18 | - | NEG -$573.5M | - | 505 | 465 | +$6.3M | +$27k bull / -$575k bear | out (clean 34, ADX 12, RVol 0.6) |
| 11 | **IWM** | 273.62 | - | **-** | 17 | - | NEG -$3.2B | 285.06 | 285 | 270 | -$5.4M | +$0 bull / -$89k bear | out (clean 34, ADX 20, RVol 0.5) |
| 12 | **AMZN** | 262.77 | - | **-** | 17 | - | POS +$406.7M | - | 265 | 260 | -$2.2M | +$31k bull / -$238k bear | out (clean 34, ADX 23, RVol 0.5) |
| 13 | **MU** | 695.60 | - | **-** | 17 | - | NEG -$177.8M | - | 700 | 700 | +$61.7M | +$2.0M bull / -$6.5M bear | out (clean 32, ADX 11, RVol 0.8) |
| 14 | **HOOD** | 79.98 | - | **-** | 17 | - | NEG -$24.0M | 83.55 | 85 | 80 | +$2.3M | +$0 bull / -$668k bear | out (clean 30, ADX 18, RVol 0.5) |
| 15 | **NVDA** | 188.00 | - | **-** | 16 | - | NEG -$379.7M | - | 200 | 190 | +$21.9M | +$769k bull / -$1.1M bear | out (clean 34, ADX 14, RVol 0.7) |
| 16 | **AMD** | 444.39 | - | **-** | 16 | - | NEG -$183.9M | - | 430 | 450 | +$9.4M | +$361k bull / -$396k bear | out (clean 33, ADX 18, RVol 0.9) |
| 17 | **SPY** | 739.70 | - | **-** | 15 | - | NEG -$14.2B | 767.46 | 760 | 740 | -$59.8M | +$824k bull / -$1.5M bear | out (clean 35, ADX 14, RVol 0.7) |
| 18 | **QQQ** | 659.86 | - | **-** | 15 | - | NEG -$5.1B | - | 700 | 680 | +$29.4M | +$545k bull / -$2.8M bear | out (clean 35, ADX 16, RVol 0.6) |
| 19 | **GOOGL** | 286.97 | - | **-** | 15 | - | POS +$79.0M | 283.56 | 285 | 290 | +$785k | +$42k bull / -$480k bear | out (clean 34, ADX 15, RVol 0.6) |
| 20 | **AVGO** | 296.80 | - | **-** | 15 | - | NEG -$145.7M | - | 325 | 300 | +$1.3M | +$291k bull / -$90k bear | out (clean 31, ADX 11, RVol 0.8) |
| 21 | **ORCL** | 116.53 | - | **-** | 15 | - | NEG -$77.3M | - | 125 | 115 | +$605k | +$216k bull / +$0 bear | out (clean 30, ADX 8, RVol 0.4) |
| 22 | **SHOP** | 150.36 | - | **-** | 10 | - | NEG -$1.6M | 151.39 | 150 | 150 | -$74k | - | out (clean 36, ADX 32, RVol 0.6) |
| 23 | **PLTR** | 161.49 | - | **-** | 8 | - | NEG -$65.0M | - | 165 | 160 | +$2.7M | - | out (clean 28, ADX 25, RVol 0.5) |
| 24 | **ARM** | 172.72 | - | **-** | 8 | - | NEG -$22.7M | - | 180 | 170 | -$461k | - | out (clean 25, ADX 12, RVol 0.8) |
| 25 | **SMCI** | 28.49 | - | **-** | 7 | - | NEG -$3.6M | 29.64 | 30 | 29 | +$312k | - | out (clean 34, ADX 20, RVol 0.3) |
| 26 | **NFLX** | 64.22 | - | **-** | 6 | - | POS +$18.3M | 63.27 | 64 | 65 | -$308k | - | out (clean 32, ADX 13, RVol 0.6) |
| 27 | **UBER** | 69.76 | - | **-** | 5 | - | POS +$15.2M | 69.04 | 70 | 70 | +$93k | - | out (clean 30, ADX 7, RVol 0.5) |

## Big prints this scan (97)
- **MSTR** CALL 133 2026-11-13 (7DTE): 6,000 @ 3.98 = **+$2.4M** MID | vol 21,198 / OI 95
- **MSFT** PUT 550 2026-11-06 (0DTE): 200 @ 12.60 = **+$252k** SELL | vol 753 / OI 2,391
- **SPY** PUT 735 2026-11-09 (3DTE): 660 @ 3.27 = **+$216k** SELL | vol 11,075 / OI 2,336
- **MU** PUT 710 2026-11-06 (0DTE): 150 @ 13.85 = **+$208k** SELL | vol 7,698 / OI 1,511
- **QQQ** CALL 660 2026-11-06 (0DTE): 500 @ 3.84 = **+$192k** BUY | vol 124,119 / OI 330
- **MU** CALL 670 2026-11-06 (0DTE): 60 @ 27.95 = **+$168k** BUY | vol 780 / OI 0
- **SPY** PUT 771 2026-11-06 (0DTE): 45 @ 30.74 = **+$138k** MID | vol 116 / OI 2,018
- **SPY** PUT 771 2026-11-06 (0DTE): 45 @ 30.72 = **+$138k** MID | vol 116 / OI 2,018
- **SPY** PUT 740 2026-11-06 (0DTE): 601 @ 2.25 = **+$135k** SELL | vol 116,666 / OI 21,704
- **SPY** CALL 741 2026-11-06 (0DTE): 700 @ 1.91 = **+$134k** BUY | vol 167,134 / OI 123
- **MSFT** CALL 532.5 2026-11-06 (0DTE): 200 @ 5.90 = **+$118k** BUY | vol 7,864 / OI 2,572
- **QQQ** PUT 670 2026-11-09 (3DTE): 100 @ 11.40 = **+$114k** SELL | vol 1,728 / OI 1,869
- **QQQ** PUT 661 2026-11-06 (0DTE): 390 @ 2.90 = **+$113k** SELL | vol 47,427 / OI 371
- **SPY** PUT 751 2026-11-06 (0DTE): 100 @ 11.29 = **+$113k** SELL | vol 2,018 / OI 2,898
- **SPY** PUT 739 2026-11-06 (0DTE): 601 @ 1.85 = **+$111k** BUY | vol 118,180 / OI 2,524

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 783 2026-11-11 (5DTE): 804 traded vs OI 358
- **SPY** PUT 747 2026-11-06 (0DTE): 2,946 traded vs OI 2,892
- **SPY** PUT 690 2026-11-06 (0DTE): 2,926 traded vs OI 2,922
- **QQQ** PUT 650 2026-11-12 (6DTE): 508 traded vs OI 347
- **NVDA** PUT 175 2026-11-11 (5DTE): 877 traded vs OI 789
- **TSLA** PUT 380 2026-12-04 (28DTE): 600 traded vs OI 377
- **TSLA** CALL 387.5 2026-11-13 (7DTE): 501 traded vs OI 0
- **TSLA** PUT 360 2026-11-11 (5DTE): 536 traded vs OI 160
- **AMD** PUT 415 2026-11-20 (14DTE): 510 traded vs OI 449
- **AMD** CALL 475 2026-11-09 (3DTE): 502 traded vs OI 49
- **AMZN** PUT 247.5 2026-11-06 (0DTE): 2,979 traded vs OI 2,482
- **MSFT** CALL 550 2026-11-11 (5DTE): 562 traded vs OI 283
- **MSFT** CALL 547.5 2026-11-09 (3DTE): 589 traded vs OI 95
- **MSFT** CALL 562.5 2026-11-09 (3DTE): 521 traded vs OI 83
- **MSFT** CALL 547.5 2026-11-06 (0DTE): 1,520 traded vs OI 1,413

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
