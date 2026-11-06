# GEX + FLOW SCAN - Fri Nov 06, 10:40 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (3)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:30 | **NVDA** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/06 192.5C | 0.73 | 0.53 | +1% (3m) | **-27%** | +199% | 193.9 |
| 10:00 | **NVDA** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/06 197.5C | 0.67 | 0.07 | -6% (1m) | **-90%** | +24% | 195 |
| 09:50 | **NFLX** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/06 64C | 0.40 | 0.29 | +32% (4m) | **-28%** | +164% | 65 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:40:08 ET, last candle SPY 10:39, QQQ 10:39 | no errors

## Flow surges NOT fired - price disagreed (6 today, last 5)
- 09:55 SMCI PUTS: price +0.09 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 HOOD PUTS: price +3.27 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 MSTR PUTS: price +3.75 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 SMCI PUTS: price +0.89 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 PLTR PUTS: price +5.57 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **TSLA** | 356.99 | TREND (flow not with it) | **CALLS** | 45 | none: 116 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (50 contracts' greeks worked out here) | NEG -$243.1M | - | 370 | 360 | -$56.9M | +$11.5M bull / -$504k bear | LONG (clean 35, ADX 44, RVol 1.1) |
| 2 | **CRM** | 212.16 | TREND (flow not with it) | **PUTS** | 43 | none: 32 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (24 contracts' greeks worked out here) | NEG -$22.1M | - | 230 | 220 | +$461k | - | SHORT (clean 34, ADX 43, RVol 1.3) |
| 3 | **DELL** | 334.26 | FLOW SURGE | **CALLS** | 42 | none: 48 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (34 contracts' greeks worked out here) | NEG -$22.8M | - | 350 | 335 | +$4.3M | +$378k bull / +$0 bear | out (clean 32, ADX 22, RVol 1.4) |
| 4 | **MSFT** | 534.72 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 39 | none: 172 calls 0-7DTE > 12 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (83 contracts' greeks worked out here) | POS +$666.9M | 510.51 | 540 | 535 | -$391k | +$349k bull / -$662k bear | out (clean 32, ADX 27, RVol 1.2) |
| 5 | **NFLX** | 63.91 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 36 | 11/06 64P @ 0.40 (delta 0.54) = est +94% at 63.25 | POS +$13.2M | 63.25 | 64 | 65 | -$62k | +$79k bull / +$0 bear | out (clean 32, ADX 24, RVol 0.8) |
| 6 | **MU** | 680.78 | - | **-** | 27 | - | NEG -$121.9M | - | 700 | 700 | +$108.1M | +$15.2M bull / +$0 bear | out (clean 32, ADX 19, RVol 2.2) |
| 7 | **SMH** | 459.70 | - | **-** | 24 | - | NEG -$395.0M | - | 505 | 465 | +$5.2M | +$903k bull / +$0 bear | out (clean 34, ADX 19, RVol 4.6) |
| 8 | **HOOD** | 79.01 | - | **-** | 24 | - | NEG -$18.0M | 82.79 | 85 | 80 | +$3.5M | +$151k bull / +$0 bear | out (clean 29, ADX 27, RVol 0.9) |
| 9 | **NVDA** | 188.12 | - | **-** | 23 | - | NEG -$342.2M | - | 200 | 190 | +$30.5M | +$3.7M bull / +$0 bear | out (clean 34, ADX 29, RVol 1.3) |
| 10 | **META** | 619.30 | - | **-** | 22 | - | NEG -$78.1M | 622.86 | 650 | 625 | -$8.0M | +$445k bull / -$674k bear | out (clean 33, ADX 38, RVol 0.6) |
| 11 | **AVGO** | 295.40 | - | **-** | 22 | - | NEG -$124.8M | - | 320 | 300 | +$2.6M | +$184k bull / +$0 bear | out (clean 30, ADX 22, RVol 1.8) |
| 12 | **SMCI** | 28.48 | - | **-** | 22 | - | NEG -$3.1M | 29.63 | 30 | 29 | +$381k | +$88k bull / +$0 bear | out (clean 35, ADX 32, RVol 0.6) |
| 13 | **AMZN** | 262.83 | - | **-** | 21 | - | POS +$371.4M | - | 265 | 260 | -$3.7M | +$274k bull / -$54k bear | out (clean 34, ADX 27, RVol 0.6) |
| 14 | **GOOGL** | 286.35 | - | **-** | 21 | - | POS +$49.6M | 283.52 | 290 | 290 | +$3.4M | +$467k bull / +$0 bear | out (clean 34, ADX 23, RVol 0.9) |
| 15 | **PLTR** | 160.50 | - | **-** | 21 | - | NEG -$60.9M | - | 165 | 160 | +$2.1M | +$499k bull / +$0 bear | out (clean 28, ADX 34, RVol 0.8) |
| 16 | **COIN** | 134.54 | - | **-** | 21 | - | NEG -$12.5M | 136.48 | 141 | 135 | -$2.1M | +$692k bull / +$0 bear | out (clean 31, ADX 16, RVol 0.4) |
| 17 | **AAPL** | 344.10 | - | **-** | 20 | - | POS +$113.3M | 342.94 | 350 | 345 | -$8.8M | +$327k bull / -$1.1M bear | out (clean 30, ADX 16, RVol 0.9) |
| 18 | **AMD** | 438.88 | - | **-** | 20 | - | NEG -$169.4M | - | 430 | 450 | +$15.2M | +$2.1M bull / +$0 bear | out (clean 32, ADX 24, RVol 1.4) |
| 19 | **ORCL** | 115.48 | - | **-** | 20 | - | NEG -$67.8M | - | 125 | 115 | +$819k | +$125k bull / +$0 bear | out (clean 31, ADX 15, RVol 0.7) |
| 20 | **MSTR** | 126.27 | - | **-** | 19 | - | NEG -$4.8M | 126.76 | 135 | 125 | -$1.7M | +$108k bull / +$0 bear | out (clean 31, ADX 20, RVol 1.1) |
| 21 | **QQQ** | 657.05 | - | **-** | 18 | - | NEG -$4.5B | - | 700 | 680 | +$61.5M | +$6.9M bull / +$0 bear | out (clean 35, ADX 20, RVol 1.0) |
| 22 | **SPY** | 738.14 | - | **-** | 17 | - | NEG -$13.4B | 765.59 | 760 | 740 | -$52.2M | +$1.7M bull / +$0 bear | out (clean 35, ADX 18, RVol 1.1) |
| 23 | **IWM** | 271.89 | - | **-** | 17 | - | NEG -$3.1B | 285.24 | 285 | 270 | -$3.5M | +$203k bull / +$0 bear | out (clean 34, ADX 15, RVol 1.0) |
| 24 | **BABA** | 108.42 | - | **-** | 17 | - | POS +$31.9M | - | 110 | 110 | -$97k | +$128k bull / +$0 bear | out (clean 34, ADX 17, RVol 1.1) |
| 25 | **UBER** | 69.40 | - | **-** | 9 | - | POS +$11.6M | 68.53 | 70 | 70 | +$116k | - | out (clean 30, ADX 12, RVol 0.9) |
| 26 | **ARM** | 172.23 | - | **-** | 8 | - | NEG -$21.8M | - | 180 | 170 | -$299k | - | out (clean 25, ADX 13, RVol 0.8) |
| 27 | **SHOP** | 147.54 | - | **-** | 7 | - | NEG -$3.8M | 151.27 | 144 | 145 | +$30k | - | out (clean 37, ADX 24, RVol 0.6) |

## Big prints this scan (132)
- **MU** PUT 695 2026-11-06 (0DTE): 547 @ 9.95 = **+$544k** SELL | vol 8,686 / OI 0
- **QQQ** PUT 665 2026-11-06 (0DTE): 399 @ 6.48 = **+$259k** SELL | vol 6,334 / OI 6,782
- **QQQ** PUT 664 2026-11-06 (0DTE): 400 @ 6.00 = **+$240k** SELL | vol 9,007 / OI 6,969
- **QQQ** PUT 664 2026-11-06 (0DTE): 399 @ 5.70 = **+$227k** SELL | vol 9,007 / OI 6,969
- **MU** PUT 675 2026-11-13 (7DTE): 76 @ 25.94 = **+$197k** SELL | vol 236 / OI 0
- **QQQ** PUT 663 2026-11-06 (0DTE): 400 @ 4.90 = **+$196k** SELL | vol 13,522 / OI 190
- **QQQ** PUT 663 2026-11-06 (0DTE): 400 @ 4.83 = **+$193k** SELL | vol 13,522 / OI 190
- **PLTR** CALL 160 2026-11-06 (0DTE): 523 @ 2.89 = **+$151k** BUY | vol 7,489 / OI 639
- **TSLA** CALL 355 2026-11-06 (0DTE): 188 @ 8.00 = **+$150k** BUY | vol 45,004 / OI 250
- **NVDA** CALL 195 2026-11-13 (7DTE): 300 @ 5.00 = **+$150k** BUY | vol 4,691 / OI 582
- **TSLA** CALL 355 2026-11-06 (0DTE): 196 @ 7.60 = **+$149k** BUY | vol 45,004 / OI 250
- **TSLA** CALL 355 2026-11-06 (0DTE): 173 @ 8.00 = **+$138k** BUY | vol 45,004 / OI 250
- **MU** CALL 650 2026-11-06 (0DTE): 25 @ 49.90 = **+$125k** BUY | vol 191 / OI 6
- **QQQ** PUT 675 2026-11-09 (3DTE): 75 @ 16.42 = **+$123k** SELL | vol 226 / OI 2,144
- **TSLA** CALL 355 2026-11-06 (0DTE): 158 @ 7.60 = **+$120k** BUY | vol 45,004 / OI 250

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 716 2026-11-06 (0DTE): 541 traded vs OI 41
- **SPY** PUT 740 2026-11-09 (3DTE): 4,903 traded vs OI 4,499
- **SPY** PUT 732 2026-11-11 (5DTE): 510 traded vs OI 101
- **SPY** CALL 766 2026-11-09 (3DTE): 933 traded vs OI 881
- **SPY** PUT 690 2026-11-09 (3DTE): 1,583 traded vs OI 1,445
- **SPY** PUT 748 2026-11-06 (0DTE): 1,821 traded vs OI 1,800
- **SPY** CALL 740 2026-11-18 (12DTE): 511 traded vs OI 1
- **SPY** CALL 752 2026-11-13 (7DTE): 945 traded vs OI 523
- **SPY** CALL 742 2026-11-30 (24DTE): 544 traded vs OI 104
- **QQQ** CALL 685 2026-11-13 (7DTE): 502 traded vs OI 458
- **QQQ** CALL 690 2026-11-20 (14DTE): 6,231 traded vs OI 5,463
- **IWM** CALL 280 2026-11-09 (3DTE): 801 traded vs OI 800
- **TSLA** CALL 385 2026-11-09 (3DTE): 605 traded vs OI 0
- **TSLA** PUT 335 2026-11-09 (3DTE): 915 traded vs OI 785
- **TSLA** CALL 340 2026-11-13 (7DTE): 501 traded vs OI 69

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
