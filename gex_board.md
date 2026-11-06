# GEX + FLOW SCAN - Fri Nov 06, 10:20 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (2)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:00 | **NVDA** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/06 197.5C | 0.67 | 0.24 | -6% (1m) | **-64%** | +24% | 195 |
| 09:50 | **NFLX** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/06 64C | 0.40 | 0.40 | +32% (4m) | **+0%** | +164% | 65 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:20:08 ET, last candle SPY 10:19, QQQ 10:19 | no errors

## Flow surges NOT fired - price disagreed (6 today, last 5)
- 09:55 SMCI PUTS: price +0.09 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 HOOD PUTS: price +3.27 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 MSTR PUTS: price +3.75 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 SMCI PUTS: price +0.89 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 PLTR PUTS: price +5.57 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **NVDA** | 191.93 | RUN: clean trend + negative gamma + flow agrees | **CALLS** | 65 | 11/06 195C @ 0.76 (delta 0.26) = est +166% at 195.85 | NEG -$350.9M | - | 210 | 190 | +$22.0M | +$8.0M bull / -$31k bear | LONG (clean 34, ADX 34, RVol 1.6) |
| 2 | **TSLA** | 361.03 | FLOW SURGE | **PUTS** | 49 | none: 116 puts 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (51 contracts' greeks worked out here) | NEG -$260.2M | - | 370 | 360 | -$85.5M | +$0 bull / -$11.2M bear | LONG (clean 35, ADX 40, RVol 0.9) |
| 3 | **NFLX** | 64.11 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 40 | 11/13 62P @ 0.57 (delta 0.26) = est +24% at 63.38 | POS +$1.9M | 64.03 | 64 | 65 | -$268k | +$0 bull / -$29k bear | out (clean 32, ADX 25, RVol 1.0) |
| 4 | **CRM** | 213.38 | TREND (flow not with it) | **PUTS** | 40 | 11/06 210P @ 0.62 (delta 0.22) = est +86% at 210.7 | NEG -$19.2M | - | 230 | 215 | +$267k | - | SHORT (clean 33, ADX 37, RVol 1.4) |
| 5 | **META** | 619.61 | TREND (flow not with it) | **CALLS** | 38 | none: 196 calls 0-7DTE > 9 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (86 contracts' greeks worked out here) | NEG -$72.6M | 623.13 | 650 | 610 | -$7.2M | +$1.5M bull / -$622k bear | LONG (clean 33, ADX 33, RVol 0.9) |
| 6 | **SMCI** | 29.02 | TREND (flow not with it) | **CALLS** | 34 | 11/06 29C @ 0.50 (delta 0.52) = est +110% at 30 | NEG -$4.1M | - | 30 | 30 | -$90k | +$25k bull / +$0 bear | LONG (clean 35, ADX 34, RVol 0.6) |
| 7 | **COIN** | 135.59 | FLIP CROSS down into negative gamma | **PUTS** | 30 | none: 53 puts 0-7DTE > 3 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only -33% at the target (needs +20%) (46 contracts' greeks worked out here) | NEG -$4.1M | 136.15 | 142 | 135 | +$496k | +$406k bull / +$0 bear | out (clean 31, ADX 17, RVol 0.4) |
| 8 | **DELL** | 337.73 | - | **-** | 29 | - | NEG -$22.7M | - | 370 | 335 | +$2.9M | +$498k bull / +$0 bear | out (clean 32, ADX 27, RVol 2.6) |
| 9 | **MU** | 703.65 | - | **-** | 26 | - | NEG -$189.7M | - | 700 | 700 | +$61.1M | +$22.7M bull / +$0 bear | out (clean 32, ADX 21, RVol 2.1) |
| 10 | **HOOD** | 80.16 | - | **-** | 25 | - | NEG -$19.5M | 84.27 | 85 | 80 | +$2.3M | +$784k bull / +$0 bear | out (clean 30, ADX 31, RVol 1.0) |
| 11 | **AMZN** | 263.31 | - | **-** | 24 | - | POS +$365.9M | - | 265 | 265 | -$4.9M | +$61k bull / -$1.3M bear | out (clean 34, ADX 27, RVol 0.5) |
| 12 | **SMH** | 467.17 | - | **-** | 22 | - | NEG -$523.1M | - | 505 | 470 | +$2.1M | +$2.7M bull / +$0 bear | out (clean 34, ADX 22, RVol 3.3) |
| 13 | **GOOGL** | 288.27 | - | **-** | 22 | - | POS +$64.5M | 284.06 | 290 | 290 | +$2.3M | +$108k bull / -$402k bear | out (clean 34, ADX 27, RVol 1.4) |
| 14 | **AVGO** | 300.79 | - | **-** | 22 | - | NEG -$152.1M | - | 330 | 300 | +$1.2M | +$658k bull / +$0 bear | out (clean 31, ADX 25, RVol 2.0) |
| 15 | **BABA** | 109.34 | - | **-** | 21 | - | POS +$22.2M | 107.11 | 110 | 110 | -$228k | +$0 bull / -$116k bear | out (clean 35, ADX 18, RVol 1.4) |
| 16 | **SPY** | 740.68 | - | **-** | 20 | - | NEG -$14.2B | 769.63 | 770 | 740 | -$75.3M | +$4.0M bull / -$1.9M bear | out (clean 35, ADX 21, RVol 1.3) |
| 17 | **IWM** | 273.18 | - | **-** | 20 | - | NEG -$3.4B | 285.88 | 285 | 270 | -$5.5M | +$881k bull / +$0 bear | out (clean 35, ADX 16, RVol 1.0) |
| 18 | **MSFT** | 532.96 | - | **-** | 20 | - | POS +$622.4M | 510.6 | 540 | 535 | -$938k | +$159k bull / -$367k bear | out (clean 32, ADX 32, RVol 1.0) |
| 19 | **PLTR** | 162.13 | - | **-** | 20 | - | NEG -$66.0M | - | 165 | 160 | +$613k | +$3.5M bull / +$0 bear | out (clean 28, ADX 36, RVol 1.4) |
| 20 | **AMD** | 448.64 | - | **-** | 19 | - | NEG -$165.2M | - | 430 | 450 | -$3.2M | +$7.1M bull / +$0 bear | out (clean 32, ADX 28, RVol 1.6) |
| 21 | **ORCL** | 117.55 | - | **-** | 19 | - | NEG -$74.4M | - | 125 | 120 | +$419k | +$252k bull / -$74k bear | out (clean 31, ADX 16, RVol 0.8) |
| 22 | **ARM** | 173.74 | - | **-** | 19 | - | NEG -$21.6M | - | 190 | 170 | -$303k | +$28k bull / +$0 bear | out (clean 26, ADX 15, RVol 0.8) |
| 23 | **QQQ** | 660.99 | - | **-** | 18 | - | NEG -$5.9B | - | 700 | 680 | +$21.8M | +$13.9M bull / -$753k bear | out (clean 35, ADX 24, RVol 1.3) |
| 24 | **AAPL** | 342.47 | - | **-** | 18 | - | POS +$14.6M | 342.17 | 350 | 345 | -$2.5M | +$1.2M bull / -$586k bear | out (clean 30, ADX 20, RVol 1.2) |
| 25 | **MSTR** | 127.73 | - | **-** | 16 | - | POS +$5.5M | 127.11 | 135 | 125 | -$212k | +$357k bull / -$371k bear | out (clean 32, ADX 19, RVol 0.9) |
| 26 | **SHOP** | 148.40 | - | **-** | 16 | - | NEG -$3.0M | 151.43 | 150 | 145 | -$94k | - | out (clean 37, ADX 24, RVol 1.6) |
| 27 | **UBER** | 69.78 | - | **-** | 12 | - | POS +$15.3M | 68.58 | 70 | 70 | -$78k | - | out (clean 30, ADX 13, RVol 1.7) |

## Big prints this scan (171)
- **MU** CALL 692.5 2026-11-13 (7DTE): 109 @ 49.13 = **+$536k** BUY | vol 119 / OI 0
- **SPY** CALL 745 2026-11-11 (5DTE): 1,000 @ 5.30 = **+$530k** SELL | vol 1,438 / OI 17
- **MU** CALL 700 2026-11-13 (7DTE): 109 @ 44.60 = **+$486k** BUY | vol 380 / OI 38
- **QQQ** PUT 670 2026-11-09 (3DTE): 300 @ 12.37 = **+$371k** SELL | vol 992 / OI 1,869
- **QQQ** CALL 658 2026-11-06 (0DTE): 586 @ 6.10 = **+$357k** BUY | vol 14,279 / OI 0
- **MU** CALL 690 2026-11-13 (7DTE): 54 @ 50.15 = **+$271k** BUY | vol 155 / OI 16
- **SPY** CALL 752 2026-11-11 (5DTE): 1,000 @ 2.65 = **+$265k** SELL | vol 1,396 / OI 10
- **MU** CALL 697.5 2026-11-13 (7DTE): 49 @ 45.55 = **+$223k** BUY | vol 100 / OI 0
- **TSLA** CALL 362.5 2026-11-13 (7DTE): 243 @ 8.85 = **+$215k** SELL | vol 2,191 / OI 14
- **SPY** PUT 759 2026-11-06 (0DTE): 110 @ 19.50 = **+$214k** BUY | vol 668 / OI 3,834
- **NVDA** CALL 192.5 2026-11-06 (0DTE): 866 @ 2.47 = **+$214k** BUY | vol 41,912 / OI 620
- **MU** CALL 720 2026-11-13 (7DTE): 60 @ 32.65 = **+$196k** BUY | vol 331 / OI 14
- **TSLA** CALL 362.5 2026-11-13 (7DTE): 219 @ 8.82 = **+$193k** SELL | vol 2,191 / OI 14
- **COIN** PUT 138 2026-11-13 (7DTE): 293 @ 6.55 = **+$192k** SELL | vol 304 / OI 154
- **TSLA** CALL 362.5 2026-11-13 (7DTE): 215 @ 8.76 = **+$188k** SELL | vol 2,191 / OI 14

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 738 2026-11-10 (4DTE): 693 traded vs OI 133
- **SPY** CALL 752 2026-11-11 (5DTE): 1,396 traded vs OI 10
- **SPY** CALL 760 2026-11-10 (4DTE): 673 traded vs OI 672
- **SPY** CALL 725 2026-11-06 (0DTE): 559 traded vs OI 181
- **SPY** CALL 745 2026-11-11 (5DTE): 1,438 traded vs OI 17
- **SPY** CALL 721 2026-11-06 (0DTE): 596 traded vs OI 41
- **SPY** PUT 744 2026-11-06 (0DTE): 3,131 traded vs OI 2,822
- **SPY** PUT 720 2026-11-06 (0DTE): 15,982 traded vs OI 14,761
- **SPY** CALL 763 2026-11-09 (3DTE): 2,283 traded vs OI 153
- **SPY** CALL 750 2026-11-19 (13DTE): 511 traded vs OI 0
- **SPY** PUT 706 2026-11-20 (14DTE): 1,066 traded vs OI 776
- **QQQ** PUT 652 2026-11-09 (3DTE): 512 traded vs OI 283
- **QQQ** CALL 683 2026-11-06 (0DTE): 2,615 traded vs OI 2,540
- **QQQ** CALL 678 2026-11-09 (3DTE): 506 traded vs OI 11
- **IWM** PUT 266 2026-11-06 (0DTE): 4,033 traded vs OI 3,455

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
