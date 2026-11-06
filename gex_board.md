# GEX + FLOW SCAN - Fri Nov 06, 03:55 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (4)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 12:40 | **SPY** | **CALLS** | 1m WHIPSAW (R1) | 11/06 742C | 0.42 | 0.26 | +14% (6m) | **-38%** (done) | +42% | 739.03 |
| 10:30 | **NVDA** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/06 192.5C | 0.73 | 0.28 | +12% (20m) | **-62%** (done) | +199% | 193.9 |
| 10:00 | **NVDA** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/06 197.5C | 0.67 | 0.03 | -6% (1m) | **-96%** (done) | +24% | 195 |
| 09:50 | **NFLX** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/06 64C | 0.40 | 0.36 | +32% (4m) | **-10%** (done) | +164% | 65 |

## 1m RULES on SPY / QQQ - loose (11 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 15:32:08 ET, last candle SPY 15:31, QQQ 15:31 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 13:17 | SPY | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |
| 13:16 | QQQ | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |
| 13:11 | QQQ | 1m FAILED POP | R3 R4 | PUTS | TURNING your way | no contract: 39 puts 0-1DTE > 4 priced 0.40-0.80 > 2 delta 0.15+ > 2 spread ok > 2 liquid  |
| 13:11 | SPY | 1m FAILED POP | R3 R4 | PUTS | TURNING your way | no contract: 44 puts 0-1DTE > 4 priced 0.40-0.80 > 3 delta 0.15+ > 3 spread ok > 3 liquid  |
| 13:00 | QQQ | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | no contract: 40 puts 0-1DTE > 4 priced 0.40-0.80 > 2 delta 0.15+ > 2 spread ok > 2 liquid  |
| 13:00 | SPY | 1m FAILED POP | R3 | PUTS | TURNING away | no contract: 44 puts 0-1DTE > 4 priced 0.40-0.80 > 2 delta 0.15+ > 2 spread ok > 2 liquid  |
| 12:39 | SPY | 1m WHIPSAW | R1 | CALLS | AGAINST you | **FIRE** SPY261106C00742000 |
| 12:38 | QQQ | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |
| 12:38 | SPY | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |
| 12:37 | QQQ | 1m WHIPSAW | R1 R2 | PUTS | WITH you | no contract: 39 puts 0-1DTE > 5 priced 0.40-0.80 > 1 delta 0.15+ > 1 spread ok > 1 liquid  |

## Flow surges NOT fired - price disagreed (6 today, last 5)
- 09:55 SMCI PUTS: price +0.09 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 HOOD PUTS: price +3.27 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 MSTR PUTS: price +3.75 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 SMCI PUTS: price +0.89 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 PLTR PUTS: price +5.57 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **NFLX** | 63.37 | FLIP CROSS down into negative gamma | **PUTS** | 33 | none: 24 puts 0-7DTE > 3 priced 0.40-0.80 > 2 delta 0.2+ > 2 spread ok > 2 liquid > best one only +16% at the target (needs +20%) (17 contracts' greeks worked out here) | NEG -$21.3M | 63.55 | 64 | 63 | +$491k | +$25k bull / -$26k bear | out (clean 32, ADX 22, RVol 0.9) |
| 2 | **MSFT** | 530.73 | PINNED between the walls (positive gamma) - chop | **-** | 31 | - | POS +$698.1M | 511.44 | 530 | 530 | +$4.2M | +$92k bull / -$735k bear | out (clean 33, ADX 18, RVol 0.8) |
| 3 | **AMZN** | 259.68 | PINNED between the walls (positive gamma) - chop | **-** | 30 | - | POS +$364.5M | - | 260 | 260 | +$2.4M | +$174k bull / +$0 bear | out (clean 36, ADX 23, RVol 0.7) |
| 4 | **GOOGL** | 284.66 | PINNED between the walls (positive gamma) - chop | **-** | 29 | - | POS +$33.1M | 282.68 | 285 | 285 | +$2.2M | +$106k bull / +$0 bear | out (clean 32, ADX 14, RVol 0.7) |
| 5 | **ORCL** | 115.60 | - | **-** | 21 | - | NEG -$94.3M | - | 116 | 115 | -$6.3M | +$0 bull / -$98k bear | out (clean 30, ADX 12, RVol 0.9) |
| 6 | **ARM** | 173.74 | - | **-** | 21 | - | NEG -$22.6M | - | 190 | 170 | -$739k | +$0 bull / -$98k bear | out (clean 24, ADX 16, RVol 1.8) |
| 7 | **HOOD** | 80.69 | - | **-** | 20 | - | NEG -$25.9M | 81.65 | 85 | 80 | +$1.8M | +$0 bull / -$139k bear | out (clean 30, ADX 31, RVol 1.5) |
| 8 | **SMH** | 462.49 | - | **-** | 19 | - | NEG -$608.7M | - | 505 | 465 | +$8.2M | +$422k bull / +$0 bear | out (clean 31, ADX 17, RVol 0.6) |
| 9 | **IWM** | 273.59 | - | **-** | 18 | - | NEG -$2.7B | 284.3 | 285 | 270 | -$6.8M | +$92k bull / +$0 bear | out (clean 32, ADX 14, RVol 1.5) |
| 10 | **TSLA** | 358.58 | - | **-** | 18 | - | NEG -$400.6M | - | 360 | 360 | -$49.4M | +$1.0M bull / -$447k bear | out (clean 34, ADX 21, RVol 1.0) |
| 11 | **AAPL** | 342.55 | - | **-** | 18 | - | NEG -$169.8M | 342.77 | 345 | 342.5 | -$16.5M | +$225k bull / +$0 bear | out (clean 27, ADX 14, RVol 0.7) |
| 12 | **AVGO** | 292.29 | - | **-** | 18 | - | NEG -$149.1M | - | 320 | 292.5 | +$2.9M | +$42k bull / +$0 bear | out (clean 30, ADX 14, RVol 2.0) |
| 13 | **NVDA** | 186.57 | - | **-** | 17 | - | NEG -$434.4M | - | 200 | 190 | +$24.2M | +$944k bull / +$0 bear | out (clean 32, ADX 15, RVol 1.2) |
| 14 | **AMD** | 444.77 | - | **-** | 17 | - | NEG -$205.0M | - | 430 | 450 | +$2.0M | +$1.4M bull / +$0 bear | out (clean 32, ADX 23, RVol 1.5) |
| 15 | **MU** | 688.04 | - | **-** | 17 | - | NEG -$166.9M | - | 700 | 690 | +$78.4M | +$2.9M bull / -$208k bear | out (clean 31, ADX 9, RVol 0.9) |
| 16 | **QQQ** | 655.96 | - | **-** | 16 | - | NEG -$4.6B | - | 655 | 655 | +$66.3M | +$1.9M bull / +$0 bear | out (clean 32, ADX 14, RVol 1.3) |
| 17 | **META** | 612.04 | - | **-** | 16 | - | NEG -$243.3M | 615.78 | 650 | 610 | +$1.1M | +$562k bull / +$0 bear | out (clean 32, ADX 26, RVol 0.6) |
| 18 | **SPY** | 735.31 | - | **-** | 15 | - | NEG -$16.4B | 766.42 | 760 | 735 | -$7.7M | +$49.0M bull / +$0 bear | out (clean 32, ADX 12, RVol 1.3) |
| 19 | **SHOP** | 148.99 | - | **-** | 15 | - | NEG -$4.4M | 150.38 | 150 | 150 | -$1.0M | - | out (clean 35, ADX 20, RVol 1.4) |
| 20 | **SMCI** | 28.75 | - | **-** | 14 | - | NEG -$4.7M | - | 30 | 29 | -$1.8M | - | out (clean 32, ADX 32, RVol 0.6) |
| 21 | **DELL** | 329.83 | - | **-** | 12 | - | NEG -$32.0M | - | 330 | 335 | +$5.8M | - | out (clean 31, ADX 19, RVol 1.1) |
| 22 | **UBER** | 68.60 | - | **-** | 12 | - | POS +$3.0M | 68.49 | 70 | 65 | +$243k | - | out (clean 32, ADX 26, RVol 1.6) |
| 23 | **MSTR** | 128.71 | - | **-** | 11 | - | POS +$19.5M | 128.09 | 135 | 125 | -$5.8M | - | out (clean 30, ADX 36, RVol 0.8) |
| 24 | **PLTR** | 160.25 | - | **-** | 9 | - | NEG -$85.0M | - | 160 | 160 | +$3.1M | - | out (clean 28, ADX 17, RVol 1.6) |
| 25 | **COIN** | 134.54 | - | **-** | 9 | - | NEG -$13.3M | 136.04 | 142 | 134 | -$2.3M | - | out (clean 31, ADX 22, RVol 1.0) |
| 26 | **BABA** | 108.96 | - | **-** | 9 | - | POS +$31.6M | 103.14 | 110 | 110 | -$392k | - | out (clean 33, ADX 14, RVol 2.1) |
| 27 | **CRM** | 213.84 | - | **-** | 8 | - | NEG -$21.6M | - | 195 | 215 | -$135k | - | out (clean 34, ADX 21, RVol 1.6) |

## Big prints this scan (81)
- **SPY** PUT 760 2026-11-13 (7DTE): 270 @ 23.06 = **+$623k** SELL | vol 552 / OI 6,735
- **AMD** CALL 437.5 2026-11-13 (7DTE): 131 @ 28.15 = **+$369k** BUY | vol 316 / OI 41
- **SPY** PUT 750 2026-11-06 (0DTE): 200 @ 12.50 = **+$250k** SELL | vol 14,776 / OI 38,550
- **SPY** PUT 735 2026-11-10 (4DTE): 400 @ 5.32 = **+$213k** SELL | vol 4,990 / OI 1,432
- **QQQ** PUT 660 2026-11-06 (0DTE): 1,000 @ 1.85 = **+$185k** SELL | vol 208,981 / OI 12,054
- **QQQ** PUT 660 2026-11-06 (0DTE): 994 @ 1.85 = **+$184k** SELL | vol 208,981 / OI 12,054
- **QQQ** PUT 660 2026-11-06 (0DTE): 994 @ 1.85 = **+$184k** SELL | vol 208,981 / OI 12,054
- **QQQ** PUT 660 2026-11-06 (0DTE): 989 @ 1.85 = **+$183k** SELL | vol 208,981 / OI 12,054
- **QQQ** PUT 660 2026-11-06 (0DTE): 988 @ 1.85 = **+$183k** SELL | vol 208,981 / OI 12,054
- **SPY** PUT 740 2026-11-06 (0DTE): 664 @ 2.64 = **+$175k** SELL | vol 213,738 / OI 21,704
- **QQQ** PUT 660 2026-11-06 (0DTE): 938 @ 1.85 = **+$174k** SELL | vol 208,981 / OI 12,054
- **MU** CALL 670 2026-11-09 (3DTE): 50 @ 33.30 = **+$166k** BUY | vol 399 / OI 0
- **SPY** CALL 740 2026-11-09 (3DTE): 492 @ 3.13 = **+$154k** BUY | vol 33,983 / OI 53
- **SPY** CALL 734 2026-11-06 (0DTE): 445 @ 3.40 = **+$151k** BUY | vol 18,340 / OI 21
- **SMH** PUT 445 2026-11-13 (7DTE): 168 @ 8.70 = **+$146k** SELL | vol 1,681 / OI 418

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 708 2026-11-11 (5DTE): 507 traded vs OI 9
- **SPY** PUT 741 2026-11-11 (5DTE): 502 traded vs OI 156
- **SPY** CALL 755 2026-11-19 (13DTE): 579 traded vs OI 0
- **SPY** CALL 745 2026-11-30 (24DTE): 811 traded vs OI 715
- **QQQ** PUT 621 2026-11-11 (5DTE): 2,306 traded vs OI 0
- **QQQ** CALL 712 2026-11-10 (4DTE): 2,005 traded vs OI 171
- **QQQ** CALL 700 2026-11-09 (3DTE): 7,256 traded vs OI 6,679
- **QQQ** PUT 607 2026-11-09 (3DTE): 577 traded vs OI 0
- **QQQ** CALL 709 2026-11-09 (3DTE): 562 traded vs OI 164
- **QQQ** CALL 663 2026-11-11 (5DTE): 504 traded vs OI 1
- **QQQ** CALL 685 2026-11-12 (6DTE): 1,735 traded vs OI 119
- **QQQ** PUT 615 2026-11-13 (7DTE): 1,422 traded vs OI 1,417
- **QQQ** CALL 700 2026-11-12 (6DTE): 701 traded vs OI 699
- **QQQ** PUT 620 2026-11-12 (6DTE): 511 traded vs OI 306
- **QQQ** PUT 661 2026-11-13 (7DTE): 527 traded vs OI 282

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
