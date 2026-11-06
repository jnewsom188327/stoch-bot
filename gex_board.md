# GEX + FLOW SCAN - Fri Nov 06, 03:45 PM ET
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
| 1 | **MSTR** | 128.96 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 38 | 11/06 129C @ 0.51 (delta 0.49) = est +289% at 131 | POS +$18.1M | 128.22 | 135 | 129 | -$4.8M | +$0 bull / -$992k bear | out (clean 30, ADX 36, RVol 0.5) |
| 2 | **SHOP** | 148.92 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 34 | none: 42 calls 0-7DTE > 1 priced 0.40-0.80 > 1 delta 0.2+ > 0 spread ok > 0 liquid (32 contracts' greeks worked out here) | POS +$2.1M | 148.47 | 150 | 149 | -$1.1M | - | out (clean 35, ADX 22, RVol 0.8) |
| 3 | **NFLX** | 63.53 | FLIP CROSS up into positive gamma | **CALLS** | 30 | none: 24 calls 0-7DTE > 2 priced 0.40-0.80 > 2 delta 0.2+ > 2 spread ok > 2 liquid > best one only +14% at the target (needs +20%) (18 contracts' greeks worked out here) | POS +$13.8M | 62.73 | 63 | 65 | +$370k | +$25k bull / -$26k bear | out (clean 32, ADX 19, RVol 0.7) |
| 4 | **AAPL** | 343.49 | FLIP CROSS up into positive gamma | **CALLS** | 29 | none: 112 calls 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (47 contracts' greeks worked out here) | NEG -$2.6M | 343.32 | 345 | 345 | -$17.2M | +$300k bull / +$0 bear | out (clean 27, ADX 11, RVol 0.4) |
| 5 | **AMZN** | 260.02 | PINNED between the walls (positive gamma) - chop | **-** | 28 | - | POS +$353.8M | - | 260 | 260 | +$1.6M | +$270k bull / +$0 bear | out (clean 36, ADX 21, RVol 0.5) |
| 6 | **COIN** | 134.88 | - | **-** | 19 | - | NEG -$29.2M | 136.74 | 142 | 135 | -$2.4M | +$430k bull / +$0 bear | out (clean 32, ADX 23, RVol 0.6) |
| 7 | **TSLA** | 360.05 | - | **-** | 18 | - | NEG -$516.9M | 371.44 | 360 | 360 | -$53.3M | +$1.7M bull / -$561k bear | out (clean 34, ADX 22, RVol 0.6) |
| 8 | **HOOD** | 80.52 | - | **-** | 18 | - | NEG -$25.2M | 81.36 | 85 | 80 | +$1.9M | +$0 bull / -$118k bear | out (clean 30, ADX 29, RVol 0.8) |
| 9 | **AMD** | 446.88 | - | **-** | 17 | - | NEG -$197.4M | - | 430 | 450 | -$999k | +$631k bull / -$295k bear | out (clean 32, ADX 26, RVol 1.1) |
| 10 | **MSFT** | 531.90 | - | **-** | 17 | - | POS +$749.7M | 512.37 | 530 | 530 | +$4.1M | +$92k bull / +$0 bear | out (clean 34, ADX 19, RVol 0.5) |
| 11 | **AVGO** | 293.04 | - | **-** | 17 | - | NEG -$145.0M | - | 320 | 292.5 | +$2.4M | +$64k bull / +$0 bear | out (clean 30, ADX 15, RVol 1.5) |
| 12 | **PLTR** | 160.94 | - | **-** | 17 | - | NEG -$76.3M | - | 165 | 160 | +$3.0M | +$613k bull / +$0 bear | out (clean 28, ADX 17, RVol 0.9) |
| 13 | **NVDA** | 187.34 | - | **-** | 16 | - | NEG -$343.7M | - | 200 | 190 | +$23.4M | +$765k bull / +$0 bear | out (clean 32, ADX 15, RVol 1.0) |
| 14 | **MU** | 689.48 | - | **-** | 16 | - | NEG -$135.6M | - | 700 | 690 | +$74.2M | +$733k bull / -$872k bear | out (clean 31, ADX 10, RVol 0.8) |
| 15 | **QQQ** | 657.78 | - | **-** | 15 | - | NEG -$4.9B | - | 700 | 660 | +$48.9M | +$1.2M bull / +$0 bear | out (clean 32, ADX 12, RVol 0.8) |
| 16 | **META** | 614.94 | - | **-** | 15 | - | NEG -$103.4M | 616.92 | 615 | 615 | +$273k | +$53k bull / +$0 bear | out (clean 32, ADX 22, RVol 0.4) |
| 17 | **GOOGL** | 285.73 | - | **-** | 15 | - | POS +$93.3M | 282.49 | 285 | 285 | +$2.0M | +$91k bull / +$0 bear | out (clean 32, ADX 12, RVol 0.5) |
| 18 | **SPY** | 737.17 | - | **-** | 14 | - | NEG -$13.7B | 766.23 | 760 | 735 | -$23.5M | +$48.1M bull / +$0 bear | out (clean 32, ADX 10, RVol 0.8) |
| 19 | **SMCI** | 28.84 | - | **-** | 14 | - | NEG -$5.4M | 29.41 | 30 | 29 | -$1.8M | - | out (clean 33, ADX 33, RVol 0.5) |
| 20 | **UBER** | 68.70 | - | **-** | 12 | - | POS +$194k | 68.7 | 70 | 65 | +$246k | - | out (clean 32, ADX 28, RVol 1.1) |
| 21 | **DELL** | 331.14 | - | **-** | 11 | - | NEG -$32.6M | - | 335 | 335 | +$5.7M | - | out (clean 31, ADX 21, RVol 0.7) |
| 22 | **ORCL** | 115.41 | - | **-** | 10 | - | NEG -$104.8M | - | 116 | 115 | -$6.0M | - | out (clean 30, ADX 12, RVol 0.6) |
| 23 | **ARM** | 172.37 | - | **-** | 10 | - | NEG -$28.2M | - | 180 | 170 | -$659k | - | out (clean 25, ADX 16, RVol 1.4) |
| 24 | **SMH** | 463.57 | - | **-** | 8 | - | NEG -$644.2M | - | 505 | 465 | +$7.5M | - | out (clean 32, ADX 19, RVol 0.6) |
| 25 | **CRM** | 214.62 | - | **-** | 8 | - | NEG -$26.4M | - | 195 | 215 | -$160k | - | out (clean 34, ADX 23, RVol 1.5) |
| 26 | **BABA** | 108.93 | - | **-** | 8 | - | POS +$29.0M | 105.19 | 110 | 110 | -$330k | - | out (clean 33, ADX 16, RVol 1.5) |
| 27 | **IWM** | 274.15 | - | **-** | 7 | - | NEG -$3.2B | 284.52 | 275 | 275 | -$7.8M | - | out (clean 32, ADX 15, RVol 1.1) |

## Big prints this scan (45)
- **SPY** PUT 730 2026-11-13 (7DTE): 55,626 @ 5.73 = **+$31.9M** SELL | vol 61,228 / OI 27,576
- **SPY** PUT 715 2026-11-13 (7DTE): 55,626 @ 2.72 = **+$15.1M** SELL | vol 61,061 / OI 1,935
- **QQQ** PUT 659 2026-11-09 (3DTE): 300 @ 5.93 = **+$178k** SELL | vol 11,796 / OI 94
- **SPY** PUT 745 2026-11-06 (0DTE): 200 @ 7.32 = **+$146k** SELL | vol 12,118 / OI 12,418
- **SPY** PUT 740 2026-11-10 (4DTE): 200 @ 7.05 = **+$141k** SELL | vol 2,316 / OI 1,039
- **SPY** PUT 740 2026-11-10 (4DTE): 200 @ 6.99 = **+$140k** SELL | vol 2,316 / OI 1,039
- **TSLA** PUT 370 2026-11-06 (0DTE): 120 @ 10.00 = **+$120k** BUY | vol 3,717 / OI 4,963
- **MU** CALL 697.5 2026-11-11 (5DTE): 40 @ 28.30 = **+$113k** BUY | vol 537 / OI 0
- **MU** CALL 697.5 2026-11-11 (5DTE): 40 @ 28.25 = **+$113k** BUY | vol 537 / OI 0
- **NVDA** CALL 190 2026-11-13 (7DTE): 182 @ 5.20 = **+$95k** BUY | vol 17,721 / OI 711
- **MSFT** PUT 535 2026-11-13 (7DTE): 90 @ 10.25 = **+$92k** SELL | vol 1,406 / OI 350
- **MU** CALL 690 2026-11-11 (5DTE): 30 @ 30.55 = **+$92k** SELL | vol 508 / OI 0
- **MU** CALL 660 2026-11-13 (7DTE): 16 @ 56.09 = **+$90k** BUY | vol 328 / OI 33
- **MU** CALL 695 2026-11-11 (5DTE): 30 @ 28.05 = **+$84k** SELL | vol 382 / OI 0
- **TSLA** CALL 350 2026-11-09 (3DTE): 64 @ 13.03 = **+$83k** SELL | vol 6,247 / OI 14

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 749 2026-11-09 (3DTE): 509 traded vs OI 223
- **SPY** PUT 680 2026-11-10 (4DTE): 1,548 traded vs OI 1,416
- **SPY** PUT 675 2026-11-10 (4DTE): 661 traded vs OI 205
- **SPY** PUT 723 2026-11-11 (5DTE): 505 traded vs OI 27
- **SPY** PUT 730 2026-11-13 (7DTE): 61,228 traded vs OI 27,576
- **SPY** CALL 770 2026-11-18 (12DTE): 591 traded vs OI 458
- **SPY** PUT 730 2026-11-27 (21DTE): 34,026 traded vs OI 3,359
- **SPY** PUT 700 2026-11-27 (21DTE): 13,789 traded vs OI 4,336
- **SPY** PUT 720 2026-11-27 (21DTE): 45,448 traded vs OI 3,232
- **QQQ** PUT 613 2026-11-11 (5DTE): 591 traded vs OI 0
- **QQQ** PUT 603 2026-11-09 (3DTE): 514 traded vs OI 0
- **QQQ** CALL 683 2026-11-12 (6DTE): 667 traded vs OI 8
- **QQQ** CALL 705 2026-11-13 (7DTE): 1,477 traded vs OI 1,456
- **IWM** PUT 271 2026-11-10 (4DTE): 525 traded vs OI 113
- **SMH** PUT 440 2026-11-09 (3DTE): 566 traded vs OI 4

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
