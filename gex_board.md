# GEX + FLOW SCAN - Fri Nov 06, 10:00 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (2)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:00 | **NVDA** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/06 197.5C | 0.67 | 0.62 | -7% (0m) | **-7%** | +24% | 195 |
| 09:50 | **NFLX** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/06 64C | 0.40 | 0.43 | +32% (4m) | **+7%** | +164% | 65 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:00:08 ET, last candle SPY 09:59, QQQ 09:59 | no errors

## Flow surges NOT fired - price disagreed (6 today, last 5)
- 09:55 SMCI PUTS: price +0.09 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 HOOD PUTS: price +3.27 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 MSTR PUTS: price +3.75 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 SMCI PUTS: price +0.89 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 PLTR PUTS: price +5.57 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **NVDA** | 193.31 | RUN: clean trend + negative gamma + flow agrees | **CALLS** | 72 | 11/06 197.5C @ 0.67 (delta 0.22) = est +24% at 195 | NEG -$342.9M | - | 210 | 190 | +$4.9M | +$12.2M bull / -$8.6M bear | LONG (clean 34, ADX 32, RVol 3.0) |
| 2 | **AMD** | 456.70 | FLOW SURGE | **PUTS** | 54 | none: 144 puts 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (64 contracts' greeks worked out here) | NEG -$145.3M | - | 430 | 450 | -$29.5M | +$280k bull / -$15.2M bear | out (clean 32, ADX 28, RVol 3.8) |
| 3 | **TSLA** | 356.24 | FLOW SURGE | **PUTS** | 50 | none: 112 puts 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (49 contracts' greeks worked out here) | NEG -$239.9M | - | 370 | 360 | -$42.7M | +$0 bull / -$8.2M bear | LONG (clean 35, ADX 30, RVol 1.2) |
| 4 | **AAPL** | 342.89 | FLOW SURGE | **PUTS** | 42 | none: 108 puts 0-7DTE > 11 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (56 contracts' greeks worked out here) | POS +$43.2M | 342.18 | 350 | 345 | -$6.9M | +$0 bull / -$2.3M bear | out (clean 30, ADX 22, RVol 1.8) |
| 5 | **COIN** | 137.26 | FLOW SURGE | **PUTS** | 31 | none: 54 puts 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (51 contracts' greeks worked out here) | POS +$6.5M | 136.25 | 142 | 135 | -$533k | +$78k bull / -$302k bear | out (clean 32, ADX 19, RVol 0.5) |
| 6 | **SMCI** | 29.17 | TREND (flow not with it) | **CALLS** | 31 | 11/06 29C @ 0.47 (delta 0.58) = est +117% at 30 | NEG -$3.4M | - | 30 | 30 | -$214k | +$0 bull / -$1.7M bear | LONG (clean 35, ADX 32, RVol 0.9) |
| 7 | **GOOGL** | 287.46 | - | **-** | 30 | - | POS +$49.1M | 284.25 | 290 | 290 | +$4.3M | +$442k bull / -$851k bear | out (clean 34, ADX 25, RVol 2.5) |
| 8 | **AMZN** | 262.43 | - | **-** | 29 | - | POS +$371.3M | - | 265 | 260 | -$4.4M | +$3.0M bull / -$885k bear | out (clean 34, ADX 22, RVol 1.1) |
| 9 | **ARM** | 173.94 | - | **-** | 29 | - | NEG -$22.6M | - | 190 | 170 | -$586k | +$91k bull / -$48k bear | out (clean 26, ADX 19, RVol 1.8) |
| 10 | **PLTR** | 162.83 | - | **-** | 28 | - | NEG -$62.8M | - | 165 | 160 | -$2.8M | +$0 bull / -$1.7M bear | out (clean 28, ADX 31, RVol 1.8) |
| 11 | **SPY** | 740.38 | - | **-** | 25 | - | NEG -$13.3B | 766.07 | 770 | 740 | -$70.5M | +$0 bull / -$6.7M bear | out (clean 35, ADX 22, RVol 2.2) |
| 12 | **SMH** | 471.43 | - | **-** | 25 | - | NEG -$495.0M | - | 505 | 475 | -$2.4M | +$544k bull / -$5.5M bear | out (clean 34, ADX 25, RVol 4.2) |
| 13 | **DELL** | 344.33 | - | **-** | 25 | - | NEG -$25.2M | - | 370 | 350 | +$704k | +$0 bull / -$339k bear | out (clean 33, ADX 31, RVol 2.2) |
| 14 | **SHOP** | 147.22 | - | **-** | 25 | - | NEG -$2.5M | 151.05 | 144 | 145 | -$78k | - | out (clean 37, ADX 21, RVol 1.7) |
| 15 | **QQQ** | 662.62 | - | **-** | 23 | - | NEG -$5.7B | - | 700 | 680 | -$40.7M | +$0 bull / -$33.9M bear | out (clean 35, ADX 23, RVol 2.8) |
| 16 | **META** | 616.27 | - | **-** | 22 | - | NEG -$109.8M | 622.2 | 650 | 610 | -$4.5M | +$2.9M bull / -$2.6M bear | out (clean 33, ADX 26, RVol 1.8) |
| 17 | **MSFT** | 529.83 | - | **-** | 22 | - | POS +$521.5M | 510.03 | 535 | 535 | +$639k | +$454k bull / -$773k bear | out (clean 32, ADX 32, RVol 1.7) |
| 18 | **BABA** | 108.06 | - | **-** | 22 | - | POS +$23.3M | 104.49 | 110 | 110 | +$107k | +$44k bull / +$0 bear | out (clean 34, ADX 17, RVol 2.5) |
| 19 | **AVGO** | 304.60 | - | **-** | 20 | - | NEG -$147.9M | - | 330 | 300 | +$310k | +$110k bull / -$273k bear | out (clean 31, ADX 28, RVol 2.0) |
| 20 | **MU** | 719.29 | - | **-** | 20 | - | NEG -$214.4M | - | 700 | 750 | +$4.3M | +$249k bull / -$31.9M bear | out (clean 32, ADX 23, RVol 3.0) |
| 21 | **ORCL** | 118.00 | - | **-** | 20 | - | NEG -$69.3M | - | 125 | 120 | +$210k | +$181k bull / -$120k bear | out (clean 31, ADX 19, RVol 1.3) |
| 22 | **HOOD** | 80.39 | - | **-** | 20 | - | NEG -$18.0M | 84.42 | 85 | 80 | +$208k | +$0 bull / -$1.2M bear | out (clean 30, ADX 31, RVol 1.4) |
| 23 | **UBER** | 69.34 | - | **-** | 20 | - | POS +$6.2M | 68.89 | 70 | 70 | -$87k | - | out (clean 29, ADX 13, RVol 2.5) |
| 24 | **IWM** | 272.05 | - | **-** | 19 | - | NEG -$3.2B | 285.1 | 285 | 270 | -$1.7M | +$0 bull / -$777k bear | out (clean 35, ADX 14, RVol 1.5) |
| 25 | **NFLX** | 64.14 | - | **-** | 18 | - | POS +$7.9M | 63.64 | 65 | 65 | -$417k | - | out (clean 32, ADX 27, RVol 1.7) |
| 26 | **CRM** | 214.31 | - | **-** | 17 | - | NEG -$22.5M | - | 230 | 220 | +$81k | - | out (clean 33, ADX 28, RVol 0.9) |
| 27 | **MSTR** | 128.20 | - | **-** | 16 | - | POS +$13.3M | 126.79 | 135 | 125 | -$153k | +$416k bull / -$646k bear | out (clean 32, ADX 19, RVol 1.0) |

## Big prints this scan (543)
- **NVDA** CALL 200 2026-11-13 (7DTE): 10,000 @ 3.80 = **+$3.8M** BUY | vol 30,065 / OI 2,763
- **SMCI** CALL 30.5 2026-11-13 (7DTE): 13,774 @ 0.82 = **+$1.1M** SELL | vol 15,117 / OI 452
- **NVDA** CALL 200 2026-11-13 (7DTE): 2,988 @ 3.61 = **+$1.1M** BUY | vol 30,065 / OI 2,763
- **NVDA** PUT 192.5 2026-11-09 (3DTE): 1,427 @ 3.50 = **+$499k** SELL | vol 5,431 / OI 850
- **NVDA** CALL 200 2026-11-13 (7DTE): 1,001 @ 3.62 = **+$362k** BUY | vol 30,065 / OI 2,763
- **NVDA** CALL 200 2026-11-13 (7DTE): 1,000 @ 3.62 = **+$362k** BUY | vol 30,065 / OI 2,763
- **AMZN** CALL 252.5 2026-11-06 (0DTE): 317 @ 10.64 = **+$337k** BUY | vol 358 / OI 4,174
- **QQQ** CALL 655 2026-11-12 (6DTE): 200 @ 15.41 = **+$308k** SELL | vol 337 / OI 1
- **QQQ** CALL 656 2026-11-12 (6DTE): 200 @ 14.81 = **+$296k** SELL | vol 242 / OI 0
- **AMD** CALL 445 2026-11-06 (0DTE): 200 @ 14.00 = **+$280k** BUY | vol 2,999 / OI 79
- **MU** CALL 720 2026-11-11 (5DTE): 100 @ 27.97 = **+$280k** SELL | vol 406 / OI 0
- **QQQ** CALL 655 2026-11-13 (7DTE): 162 @ 16.79 = **+$272k** SELL | vol 4,232 / OI 58
- **AMD** CALL 445 2026-11-06 (0DTE): 202 @ 13.00 = **+$263k** SELL | vol 2,999 / OI 79
- **MU** CALL 690 2026-11-09 (3DTE): 80 @ 32.77 = **+$262k** SELL | vol 230 / OI 0
- **QQQ** CALL 655 2026-11-13 (7DTE): 150 @ 16.74 = **+$251k** SELL | vol 4,232 / OI 58

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 746 2026-11-09 (3DTE): 531 traded vs OI 8
- **SPY** CALL 736 2026-11-10 (4DTE): 519 traded vs OI 5
- **SPY** CALL 760 2026-11-09 (3DTE): 1,992 traded vs OI 1,551
- **SPY** CALL 762 2026-11-09 (3DTE): 500 traded vs OI 127
- **SPY** PUT 713 2026-11-09 (3DTE): 666 traded vs OI 242
- **SPY** PUT 738 2026-11-09 (3DTE): 982 traded vs OI 524
- **SPY** CALL 758 2026-11-09 (3DTE): 576 traded vs OI 190
- **SPY** PUT 726 2026-11-09 (3DTE): 548 traded vs OI 49
- **SPY** PUT 712 2026-11-09 (3DTE): 567 traded vs OI 271
- **SPY** CALL 759 2026-11-06 (0DTE): 4,114 traded vs OI 3,674
- **SPY** CALL 743 2026-11-09 (3DTE): 713 traded vs OI 23
- **SPY** CALL 750 2026-11-10 (4DTE): 566 traded vs OI 231
- **SPY** PUT 724 2026-11-06 (0DTE): 3,560 traded vs OI 3,534
- **SPY** PUT 738 2026-11-06 (0DTE): 5,327 traded vs OI 2,709
- **SPY** PUT 739 2026-11-06 (0DTE): 3,526 traded vs OI 2,524

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
