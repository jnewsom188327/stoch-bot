# GEX + FLOW SCAN - Fri Nov 06, 12:30 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (3)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:30 | **NVDA** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/06 192.5C | 0.73 | 0.28 | +12% (20m) | **-62%** (done) | +199% | 193.9 |
| 10:00 | **NVDA** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/06 197.5C | 0.67 | 0.03 | -6% (1m) | **-96%** (done) | +24% | 195 |
| 09:50 | **NFLX** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/06 64C | 0.40 | 0.36 | +32% (4m) | **-10%** (done) | +164% | 65 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 12:30:08 ET, last candle SPY 12:29, QQQ 12:29 | no errors

## Flow surges NOT fired - price disagreed (6 today, last 5)
- 09:55 SMCI PUTS: price +0.09 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 HOOD PUTS: price +3.27 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 MSTR PUTS: price +3.75 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 SMCI PUTS: price +0.89 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 PLTR PUTS: price +5.57 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **NFLX** | 63.95 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 34 | none: 26 puts 0-7DTE > 1 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only +13% at the target (needs +20%) (20 contracts' greeks worked out here) | POS +$10.1M | 62.85 | 64 | 65 | -$345k | +$0 bull / -$33k bear | out (clean 32, ADX 13, RVol 0.6) |
| 2 | **SHOP** | 150.19 | PINNED between the walls (positive gamma) - chop | **-** | 33 | - | POS +$106k | 150.03 | 150 | 150 | -$1.3M | - | out (clean 36, ADX 33, RVol 0.6) |
| 3 | **AAPL** | 344.14 | PINNED between the walls (positive gamma) - chop | **-** | 29 | - | POS +$3.3M | 344.08 | 345 | 345 | -$16.1M | +$335k bull / -$63k bear | out (clean 28, ADX 8, RVol 0.3) |
| 4 | **MSFT** | 534.80 | PINNED between the walls (positive gamma) - chop | **-** | 26 | - | POS +$717.9M | 511.49 | 535 | 535 | +$2.7M | +$37k bull / -$38k bear | out (clean 33, ADX 11, RVol 0.3) |
| 5 | **TSLA** | 359.38 | - | **-** | 21 | - | NEG -$298.8M | - | 370 | 360 | -$63.3M | +$1.1M bull / +$0 bear | out (clean 35, ADX 32, RVol 0.3) |
| 6 | **COIN** | 134.42 | - | **-** | 21 | - | NEG -$20.2M | 137.07 | 141 | 135 | -$3.9M | +$0 bull / -$79k bear | out (clean 32, ADX 13, RVol 0.3) |
| 7 | **MSTR** | 128.60 | - | **-** | 21 | - | POS +$3.4M | 128.36 | 135 | 125 | -$8.7M | +$68k bull / -$2.0M bear | out (clean 31, ADX 14, RVol 0.7) |
| 8 | **DELL** | 335.11 | - | **-** | 19 | - | NEG -$28.9M | - | 340 | 335 | +$4.5M | +$365k bull / -$60k bear | out (clean 32, ADX 7, RVol 0.3) |
| 9 | **PLTR** | 161.48 | - | **-** | 18 | - | NEG -$69.7M | - | 165 | 160 | +$3.1M | +$0 bull / -$97k bear | out (clean 28, ADX 20, RVol 0.5) |
| 10 | **SMH** | 464.22 | - | **-** | 17 | - | NEG -$583.9M | - | 505 | 465 | +$7.2M | +$27k bull / +$0 bear | out (clean 33, ADX 9, RVol 0.3) |
| 11 | **META** | 619.68 | - | **-** | 16 | - | NEG -$90.8M | 623.2 | 620 | 625 | -$6.1M | +$958k bull / -$87k bear | out (clean 33, ADX 20, RVol 0.4) |
| 12 | **SMCI** | 28.66 | - | **-** | 16 | - | NEG -$3.9M | 29.67 | 30 | 29 | -$447k | +$0 bull / -$606k bear | out (clean 34, ADX 15, RVol 0.2) |
| 13 | **NVDA** | 188.32 | - | **-** | 15 | - | NEG -$396.9M | - | 200 | 190 | +$22.0M | +$1.6M bull / -$169k bear | out (clean 34, ADX 9, RVol 0.5) |
| 14 | **AMD** | 443.79 | - | **-** | 15 | - | NEG -$184.1M | - | 430 | 450 | +$13.4M | +$1.3M bull / -$83k bear | out (clean 32, ADX 14, RVol 0.4) |
| 15 | **AMZN** | 262.29 | - | **-** | 15 | - | POS +$372.7M | - | 265 | 260 | -$555k | +$559k bull / -$37k bear | out (clean 34, ADX 20, RVol 0.4) |
| 16 | **MU** | 696.14 | - | **-** | 15 | - | NEG -$184.1M | - | 700 | 700 | +$65.3M | +$3.2M bull / -$1.2M bear | out (clean 32, ADX 8, RVol 0.3) |
| 17 | **HOOD** | 80.10 | - | **-** | 15 | - | NEG -$21.7M | 82.56 | 85 | 80 | +$1.6M | +$57k bull / -$97k bear | out (clean 30, ADX 15, RVol 0.3) |
| 18 | **SPY** | 739.53 | - | **-** | 14 | - | NEG -$15.0B | 768.47 | 760 | 740 | -$59.5M | +$106k bull / -$451k bear | out (clean 34, ADX 10, RVol 0.5) |
| 19 | **QQQ** | 659.64 | - | **-** | 14 | - | NEG -$5.5B | - | 700 | 680 | +$28.0M | +$993k bull / -$968k bear | out (clean 34, ADX 12, RVol 0.5) |
| 20 | **GOOGL** | 286.80 | - | **-** | 14 | - | POS +$67.0M | 283.2 | 285 | 290 | +$1.3M | +$71k bull / +$0 bear | out (clean 34, ADX 13, RVol 0.5) |
| 21 | **ORCL** | 116.69 | - | **-** | 14 | - | NEG -$78.7M | - | 116 | 115 | +$717k | +$27k bull / -$27k bear | out (clean 30, ADX 6, RVol 0.3) |
| 22 | **CRM** | 214.94 | - | **-** | 8 | - | NEG -$22.2M | - | 230 | 215 | -$359k | - | out (clean 35, ADX 18, RVol 0.6) |
| 23 | **BABA** | 108.92 | - | **-** | 8 | - | POS +$36.3M | - | 110 | 110 | -$476k | - | out (clean 34, ADX 18, RVol 0.4) |
| 24 | **IWM** | 274.08 | - | **-** | 7 | - | NEG -$3.4B | 285.69 | 275 | 275 | -$5.0M | - | out (clean 34, ADX 21, RVol 0.8) |
| 25 | **ARM** | 173.31 | - | **-** | 7 | - | NEG -$25.8M | - | 190 | 170 | -$446k | - | out (clean 25, ADX 11, RVol 0.5) |
| 26 | **UBER** | 69.48 | - | **-** | 7 | - | POS +$14.2M | 68.54 | 70 | 70 | +$121k | - | out (clean 30, ADX 13, RVol 0.6) |
| 27 | **AVGO** | 294.49 | - | **-** | 5 | - | NEG -$135.3M | - | 320 | 300 | +$3.4M | - | out (clean 30, ADX 10, RVol 0.6) |

## Big prints this scan (58)
- **SHOP** CALL 144 2026-11-06 (0DTE): 578 @ 6.28 = **+$363k** MID | vol 1,744 / OI 1,899
- **SHOP** CALL 144 2026-11-06 (0DTE): 578 @ 6.28 = **+$363k** MID | vol 1,744 / OI 1,899
- **SHOP** CALL 144 2026-11-06 (0DTE): 290 @ 6.33 = **+$184k** MID | vol 1,744 / OI 1,899
- **SHOP** CALL 144 2026-11-06 (0DTE): 290 @ 6.33 = **+$184k** MID | vol 1,744 / OI 1,899
- **SHOP** CALL 155 2026-11-13 (7DTE): 578 @ 2.93 = **+$169k** MID | vol 2,151 / OI 150
- **SHOP** CALL 155 2026-11-13 (7DTE): 578 @ 2.93 = **+$169k** MID | vol 2,151 / OI 150
- **MU** CALL 700 2026-11-09 (3DTE): 79 @ 19.25 = **+$152k** BUY | vol 3,729 / OI 5
- **QQQ** PUT 660 2026-11-10 (4DTE): 161 @ 9.36 = **+$151k** BUY | vol 4,683 / OI 511
- **MU** PUT 690 2026-11-11 (5DTE): 49 @ 29.00 = **+$142k** SELL | vol 535 / OI 26
- **QQQ** CALL 659 2026-11-06 (0DTE): 499 @ 2.71 = **+$135k** SELL | vol 50,061 / OI 0
- **QQQ** PUT 660 2026-11-10 (4DTE): 134 @ 9.36 = **+$125k** BUY | vol 4,683 / OI 511
- **AMD** PUT 450 2026-11-13 (7DTE): 51 @ 24.58 = **+$125k** SELL | vol 990 / OI 3,956
- **AMD** PUT 450 2026-11-13 (7DTE): 50 @ 24.58 = **+$123k** SELL | vol 990 / OI 3,956
- **AMD** PUT 450 2026-11-13 (7DTE): 50 @ 24.58 = **+$123k** SELL | vol 990 / OI 3,956
- **AMD** PUT 450 2026-11-13 (7DTE): 50 @ 24.58 = **+$123k** SELL | vol 990 / OI 3,956

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 804 2026-11-13 (7DTE): 1,766 traded vs OI 713
- **SPY** PUT 735 2026-11-19 (13DTE): 503 traded vs OI 0
- **QQQ** CALL 661 2026-11-13 (7DTE): 508 traded vs OI 0
- **QQQ** PUT 595 2026-11-20 (14DTE): 2,619 traded vs OI 2,514
- **NVDA** PUT 192.5 2026-11-11 (5DTE): 2,151 traded vs OI 2,140
- **MSFT** CALL 535 2026-11-09 (3DTE): 501 traded vs OI 98
- **AVGO** PUT 295 2026-11-20 (14DTE): 891 traded vs OI 884
- **MU** PUT 690 2026-11-11 (5DTE): 535 traded vs OI 26
- **MU** CALL 740 2026-11-20 (14DTE): 517 traded vs OI 349
- **MSTR** PUT 129 2026-11-06 (0DTE): 887 traded vs OI 872

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
