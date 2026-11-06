# GEX + FLOW SCAN - Fri Nov 06, 12:20 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (3)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:30 | **NVDA** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/06 192.5C | 0.73 | 0.28 | +12% (20m) | **-62%** (done) | +199% | 193.9 |
| 10:00 | **NVDA** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/06 197.5C | 0.67 | 0.03 | -6% (1m) | **-96%** (done) | +24% | 195 |
| 09:50 | **NFLX** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/06 64C | 0.40 | 0.36 | +32% (4m) | **-10%** (done) | +164% | 65 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 12:20:08 ET, last candle SPY 12:19, QQQ 12:19 | no errors

## Flow surges NOT fired - price disagreed (6 today, last 5)
- 09:55 SMCI PUTS: price +0.09 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 HOOD PUTS: price +3.27 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 MSTR PUTS: price +3.75 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 SMCI PUTS: price +0.89 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 PLTR PUTS: price +5.57 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **MSFT** | 535.19 | PINNED between the walls (positive gamma) - chop | **-** | 27 | - | POS +$645.4M | 514.68 | 535 | 535 | +$3.0M | +$179k bull / +$0 bear | out (clean 33, ADX 12, RVol 0.4) |
| 2 | **NFLX** | 64.05 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 24 | none: 26 puts 0-7DTE > 2 priced 0.40-0.80 > 2 delta 0.2+ > 2 spread ok > 2 liquid > best one only +8% at the target (needs +20%) (20 contracts' greeks worked out here) | POS +$8.9M | 63.79 | 64 | 65 | -$288k | - | out (clean 32, ADX 13, RVol 0.6) |
| 3 | **TSLA** | 359.86 | - | **-** | 22 | - | NEG -$311.3M | - | 370 | 360 | -$64.9M | +$1.5M bull / +$0 bear | out (clean 35, ADX 35, RVol 0.4) |
| 4 | **COIN** | 134.49 | - | **-** | 22 | - | NEG -$19.5M | 136.98 | 142 | 135 | -$3.9M | +$0 bull / -$122k bear | out (clean 32, ADX 15, RVol 0.3) |
| 5 | **MSTR** | 128.75 | - | **-** | 20 | - | POS +$8.3M | 128.23 | 135 | 125 | -$7.3M | +$0 bull / -$615k bear | out (clean 30, ADX 13, RVol 0.6) |
| 6 | **DELL** | 334.91 | - | **-** | 19 | - | NEG -$28.9M | - | 340 | 335 | +$4.6M | +$365k bull / +$0 bear | out (clean 32, ADX 8, RVol 0.4) |
| 7 | **SMH** | 464.29 | - | **-** | 18 | - | NEG -$562.0M | - | 505 | 465 | +$7.2M | +$166k bull / +$0 bear | out (clean 33, ADX 10, RVol 0.3) |
| 8 | **PLTR** | 161.44 | - | **-** | 18 | - | NEG -$74.3M | - | 165 | 160 | +$3.3M | +$135k bull / +$0 bear | out (clean 28, ADX 21, RVol 0.3) |
| 9 | **IWM** | 273.69 | - | **-** | 17 | - | NEG -$3.4B | 285.78 | 285 | 270 | -$4.4M | +$57k bull / +$0 bear | out (clean 34, ADX 22, RVol 0.5) |
| 10 | **AAPL** | 343.85 | - | **-** | 17 | - | POS +$19.4M | 343.58 | 350 | 345 | -$15.5M | +$435k bull / -$45k bear | out (clean 28, ADX 9, RVol 0.3) |
| 11 | **SHOP** | 150.41 | - | **-** | 17 | - | NEG -$1.8M | 151.5 | 150 | 150 | +$4k | +$43k bull / +$0 bear | out (clean 36, ADX 34, RVol 0.6) |
| 12 | **META** | 620.45 | - | **-** | 16 | - | NEG -$77.1M | 623.37 | 620 | 625 | -$6.3M | +$814k bull / +$0 bear | out (clean 33, ADX 23, RVol 0.3) |
| 13 | **SMCI** | 28.67 | - | **-** | 16 | - | NEG -$4.8M | - | 30 | 30 | -$453k | +$0 bull / -$643k bear | out (clean 34, ADX 16, RVol 0.2) |
| 14 | **MU** | 697.13 | - | **-** | 16 | - | NEG -$201.5M | - | 700 | 700 | +$63.9M | +$3.1M bull / -$1.3M bear | out (clean 32, ADX 9, RVol 0.4) |
| 15 | **HOOD** | 79.98 | - | **-** | 16 | - | NEG -$23.4M | 83.83 | 85 | 80 | +$2.0M | +$60k bull / -$33k bear | out (clean 30, ADX 16, RVol 0.3) |
| 16 | **NVDA** | 188.14 | - | **-** | 15 | - | NEG -$405.7M | - | 200 | 190 | +$22.5M | +$887k bull / -$488k bear | out (clean 34, ADX 10, RVol 0.5) |
| 17 | **AMD** | 444.19 | - | **-** | 15 | - | NEG -$181.4M | - | 430 | 450 | +$11.3M | +$740k bull / -$131k bear | out (clean 32, ADX 15, RVol 0.4) |
| 18 | **AMZN** | 262.29 | - | **-** | 15 | - | POS +$362.2M | - | 265 | 260 | -$886k | +$396k bull / +$0 bear | out (clean 34, ADX 20, RVol 0.3) |
| 19 | **GOOGL** | 286.24 | - | **-** | 15 | - | POS +$74.0M | 282.86 | 285 | 290 | +$1.6M | +$71k bull / +$0 bear | out (clean 34, ADX 14, RVol 0.5) |
| 20 | **AVGO** | 295.19 | - | **-** | 15 | - | NEG -$141.7M | - | 320 | 300 | +$2.4M | +$173k bull / +$0 bear | out (clean 30, ADX 9, RVol 0.7) |
| 21 | **SPY** | 739.38 | - | **-** | 14 | - | NEG -$14.8B | 768.77 | 770 | 740 | -$49.1M | +$614k bull / -$348k bear | out (clean 34, ADX 11, RVol 0.8) |
| 22 | **QQQ** | 659.78 | - | **-** | 14 | - | NEG -$6.0B | - | 700 | 680 | +$34.5M | +$2.5M bull / +$0 bear | out (clean 34, ADX 14, RVol 0.5) |
| 23 | **CRM** | 215.53 | - | **-** | 8 | - | NEG -$26.0M | - | 230 | 220 | -$358k | - | out (clean 35, ADX 19, RVol 0.5) |
| 24 | **BABA** | 109.12 | - | **-** | 8 | - | POS +$23.7M | 106.97 | 110 | 110 | -$484k | - | out (clean 34, ADX 20, RVol 0.4) |
| 25 | **ARM** | 173.20 | - | **-** | 7 | - | NEG -$26.5M | - | 190 | 170 | -$435k | - | out (clean 25, ADX 12, RVol 0.4) |
| 26 | **UBER** | 69.40 | - | **-** | 7 | - | POS +$13.1M | 68.76 | 70 | 70 | +$139k | - | out (clean 30, ADX 11, RVol 0.6) |
| 27 | **ORCL** | 116.74 | - | **-** | 4 | - | NEG -$78.4M | - | 116 | 115 | +$722k | - | out (clean 30, ADX 6, RVol 0.3) |

## Big prints this scan (57)
- **MSTR** CALL 132 2026-11-13 (7DTE): 1,372 @ 4.48 = **+$615k** SELL | vol 16,280 / OI 365
- **DELL** PUT 325 2026-11-13 (7DTE): 250 @ 13.25 = **+$331k** SELL | vol 502 / OI 1,062
- **MU** CALL 680 2026-11-09 (3DTE): 100 @ 30.52 = **+$305k** BUY | vol 1,396 / OI 0
- **MU** CALL 680 2026-11-09 (3DTE): 99 @ 30.71 = **+$304k** BUY | vol 1,396 / OI 0
- **SPY** PUT 738 2026-11-06 (0DTE): 1,407 @ 1.68 = **+$236k** BUY | vol 154,661 / OI 2,709
- **MU** CALL 680 2026-11-06 (0DTE): 99 @ 18.51 = **+$183k** BUY | vol 4,196 / OI 21
- **MU** CALL 680 2026-11-06 (0DTE): 100 @ 18.22 = **+$182k** BUY | vol 4,196 / OI 21
- **AAPL** CALL 345 2026-11-13 (7DTE): 297 @ 5.00 = **+$148k** BUY | vol 3,069 / OI 5,444
- **MU** PUT 707.5 2026-11-13 (7DTE): 31 @ 43.60 = **+$135k** MID | vol 124 / OI 0
- **MU** PUT 707.5 2026-11-13 (7DTE): 31 @ 43.55 = **+$135k** MID | vol 124 / OI 0
- **MU** PUT 707.5 2026-11-13 (7DTE): 31 @ 43.55 = **+$135k** MID | vol 124 / OI 0
- **MU** CALL 700 2026-11-06 (0DTE): 198 @ 5.90 = **+$117k** BUY | vol 27,821 / OI 67
- **NVDA** PUT 187.5 2026-11-13 (7DTE): 199 @ 5.75 = **+$114k** SELL | vol 3,593 / OI 3,561
- **MU** CALL 700 2026-11-06 (0DTE): 198 @ 5.70 = **+$113k** BUY | vol 27,821 / OI 67
- **SPY** PUT 738 2026-11-06 (0DTE): 700 @ 1.60 = **+$112k** BUY | vol 154,661 / OI 2,709

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 695 2026-11-10 (4DTE): 545 traded vs OI 420
- **SPY** PUT 685 2026-11-16 (10DTE): 520 traded vs OI 396
- **SPY** PUT 730 2026-11-16 (10DTE): 513 traded vs OI 304
- **SPY** CALL 733 2026-11-13 (7DTE): 501 traded vs OI 11
- **QQQ** PUT 658 2026-11-11 (5DTE): 533 traded vs OI 37
- **QQQ** CALL 696 2026-11-11 (5DTE): 534 traded vs OI 82
- **QQQ** CALL 659 2026-11-10 (4DTE): 500 traded vs OI 1
- **QQQ** CALL 701 2026-11-09 (3DTE): 860 traded vs OI 156
- **NVDA** PUT 187.5 2026-11-13 (7DTE): 3,593 traded vs OI 3,561
- **NVDA** PUT 190 2026-11-18 (12DTE): 800 traded vs OI 65
- **TSLA** CALL 382.5 2026-11-11 (5DTE): 500 traded vs OI 71
- **TSLA** PUT 357.5 2026-11-11 (5DTE): 505 traded vs OI 97
- **TSLA** PUT 345 2026-11-11 (5DTE): 502 traded vs OI 101
- **AVGO** CALL 300 2026-11-09 (3DTE): 506 traded vs OI 24
- **PLTR** PUT 152.5 2026-11-13 (7DTE): 527 traded vs OI 338

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
