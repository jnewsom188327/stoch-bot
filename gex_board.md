# GEX + FLOW SCAN - Fri Nov 06, 02:10 PM ET
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
Last 1m check 14:10:08 ET, last candle SPY 14:09, QQQ 14:09 | no errors
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
| 1 | **MSFT** | 534.05 | PINNED between the walls (positive gamma) - chop | **-** | 27 | - | POS +$653.1M | 513.48 | 535 | 535 | +$2.3M | +$0 bull / -$672k bear | out (clean 34, ADX 13, RVol 0.4) |
| 2 | **ORCL** | 115.37 | - | **-** | 21 | - | NEG -$84.4M | - | 116 | 115 | -$5.8M | +$0 bull / -$145k bear | out (clean 30, ADX 18, RVol 0.3) |
| 3 | **DELL** | 329.66 | - | **-** | 20 | - | NEG -$28.8M | - | 335 | 335 | +$6.0M | +$383k bull / +$0 bear | out (clean 30, ADX 15, RVol 0.3) |
| 4 | **ARM** | 173.59 | - | **-** | 19 | - | NEG -$27.5M | - | 190 | 170 | -$786k | +$0 bull / -$60k bear | out (clean 26, ADX 17, RVol 0.3) |
| 5 | **TSLA** | 359.56 | - | **-** | 18 | - | NEG -$305.4M | - | 360 | 360 | -$55.6M | +$2.7M bull / -$63k bear | out (clean 35, ADX 22, RVol 0.2) |
| 6 | **MSTR** | 127.84 | - | **-** | 18 | - | NEG -$9.7M | 128.49 | 135 | 125 | -$5.3M | +$319k bull / -$1.5M bear | out (clean 30, ADX 20, RVol 0.3) |
| 7 | **SMH** | 463.76 | - | **-** | 17 | - | NEG -$599.0M | - | 505 | 465 | +$6.0M | +$0 bull / -$36k bear | out (clean 32, ADX 16, RVol 0.4) |
| 8 | **AAPL** | 344.64 | - | **-** | 17 | - | NEG -$4.2M | 344.65 | 345 | 345 | -$18.2M | +$0 bull / -$68k bear | out (clean 28, ADX 9, RVol 0.2) |
| 9 | **NFLX** | 63.88 | PINNED between the walls (positive gamma) - chop | **-** | 17 | - | POS +$16.1M | 63.42 | 64 | 64 | -$418k | - | out (clean 32, ADX 13, RVol 0.3) |
| 10 | **AVGO** | 293.11 | - | **-** | 17 | - | NEG -$139.6M | - | 320 | 300 | +$1.4M | +$0 bull / -$329k bear | out (clean 31, ADX 18, RVol 1.4) |
| 11 | **QQQ** | 659.00 | - | **-** | 16 | - | NEG -$5.3B | - | 700 | 680 | +$35.3M | +$125k bull / -$1.9M bear | out (clean 34, ADX 17, RVol 1.2) |
| 12 | **MU** | 692.70 | - | **-** | 16 | - | NEG -$189.6M | - | 700 | 700 | +$67.1M | +$26k bull / -$3.9M bear | out (clean 32, ADX 13, RVol 0.5) |
| 13 | **SPY** | 738.67 | - | **-** | 15 | - | NEG -$15.3B | 767.98 | 760 | 740 | -$42.9M | +$205k bull / -$461k bear | out (clean 34, ADX 15, RVol 0.7) |
| 14 | **IWM** | 273.98 | - | **-** | 15 | - | NEG -$3.2B | 285.17 | 275 | 275 | -$5.1M | +$189k bull / +$0 bear | out (clean 33, ADX 17, RVol 0.3) |
| 15 | **NVDA** | 187.66 | - | **-** | 15 | - | NEG -$419.0M | - | 200 | 190 | +$22.9M | +$69k bull / -$494k bear | out (clean 33, ADX 13, RVol 0.4) |
| 16 | **AMD** | 445.67 | - | **-** | 15 | - | NEG -$189.4M | - | 430 | 450 | +$3.2M | +$26k bull / -$2.4M bear | out (clean 32, ADX 20, RVol 0.6) |
| 17 | **META** | 617.67 | - | **-** | 15 | - | NEG -$73.8M | 619.97 | 620 | 620 | -$7.0M | +$103k bull / -$40k bear | out (clean 33, ADX 18, RVol 0.2) |
| 18 | **BABA** | 109.12 | - | **-** | 15 | - | POS +$35.0M | - | 110 | 110 | -$385k | +$154k bull / +$0 bear | out (clean 34, ADX 12, RVol 0.2) |
| 19 | **AMZN** | 262.51 | - | **-** | 14 | - | POS +$361.9M | - | 265 | 260 | -$1.6M | +$155k bull / +$0 bear | out (clean 35, ADX 17, RVol 0.2) |
| 20 | **GOOGL** | 286.33 | - | **-** | 14 | - | POS +$93.8M | 283.06 | 285 | 285 | +$1.3M | +$0 bull / -$411k bear | out (clean 33, ADX 13, RVol 0.2) |
| 21 | **SHOP** | 149.23 | - | **-** | 14 | - | NEG -$1.3M | 149.99 | 150 | 150 | -$1.1M | - | out (clean 35, ADX 19, RVol 0.5) |
| 22 | **UBER** | 68.94 | - | **-** | 12 | - | POS +$8.5M | 68.53 | 70 | 65 | +$271k | - | out (clean 30, ADX 30, RVol 0.4) |
| 23 | **COIN** | 134.37 | - | **-** | 11 | - | NEG -$22.3M | 137.11 | 142 | 135 | -$3.4M | - | out (clean 31, ADX 21, RVol 0.4) |
| 24 | **CRM** | 214.44 | - | **-** | 8 | - | NEG -$20.8M | - | 230 | 215 | -$216k | - | out (clean 34, ADX 23, RVol 0.8) |
| 25 | **PLTR** | 160.53 | - | **-** | 6 | - | NEG -$85.4M | - | 165 | 160 | +$3.6M | - | out (clean 27, ADX 10, RVol 0.4) |
| 26 | **SMCI** | 28.34 | - | **-** | 6 | - | NEG -$5.0M | - | 30 | 28 | -$434k | - | out (clean 33, ADX 16, RVol 0.3) |
| 27 | **HOOD** | 79.81 | - | **-** | 5 | - | NEG -$28.8M | 82.35 | 85 | 80 | +$2.0M | - | out (clean 30, ADX 16, RVol 0.3) |

## Big prints this scan (60)
- **MSTR** CALL 133 2026-11-13 (7DTE): 4,000 @ 3.68 = **+$1.5M** SELL | vol 25,277 / OI 95
- **AMD** CALL 440 2026-11-13 (7DTE): 400 @ 23.89 = **+$956k** SELL | vol 878 / OI 109
- **AMD** PUT 440 2026-11-13 (7DTE): 400 @ 20.81 = **+$832k** BUY | vol 1,056 / OI 1,204
- **MU** CALL 660 2026-11-13 (7DTE): 44 @ 54.15 = **+$238k** SELL | vol 227 / OI 33
- **MU** CALL 660 2026-11-13 (7DTE): 35 @ 53.95 = **+$189k** SELL | vol 227 / OI 33
- **QQQ** CALL 658 2026-11-06 (0DTE): 500 @ 2.10 = **+$105k** SELL | vol 100,573 / OI 0
- **QQQ** CALL 658 2026-11-06 (0DTE): 500 @ 2.10 = **+$105k** SELL | vol 100,573 / OI 0
- **MU** CALL 660 2026-11-13 (7DTE): 19 @ 54.15 = **+$103k** SELL | vol 227 / OI 33
- **QQQ** PUT 656 2026-11-06 (0DTE): 1,000 @ 1.00 = **+$100k** BUY | vol 139,314 / OI 464
- **MU** CALL 660 2026-11-13 (7DTE): 18 @ 54.10 = **+$97k** SELL | vol 227 / OI 33
- **ORCL** CALL 120 2026-11-13 (7DTE): 349 @ 2.50 = **+$87k** SELL | vol 3,248 / OI 212
- **MU** CALL 660 2026-11-13 (7DTE): 16 @ 54.15 = **+$87k** SELL | vol 227 / OI 33
- **GOOGL** PUT 300 2026-11-09 (3DTE): 60 @ 14.06 = **+$84k** BUY | vol 324 / OI 342
- **IWM** CALL 267.5 2026-11-13 (7DTE): 97 @ 8.46 = **+$82k** BUY | vol 105 / OI 53
- **MU** CALL 685 2026-11-11 (5DTE): 24 @ 32.80 = **+$79k** SELL | vol 259 / OI 0

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 739 2026-11-12 (6DTE): 507 traded vs OI 2
- **SPY** PUT 710 2026-11-12 (6DTE): 517 traded vs OI 378
- **QQQ** CALL 703 2026-11-09 (3DTE): 598 traded vs OI 116
- **QQQ** PUT 619 2026-11-10 (4DTE): 643 traded vs OI 0
- **QQQ** CALL 666 2026-11-13 (7DTE): 597 traded vs OI 9
- **QQQ** CALL 670 2026-11-12 (6DTE): 536 traded vs OI 34
- **QQQ** PUT 635 2026-11-12 (6DTE): 505 traded vs OI 282
- **QQQ** PUT 653 2026-11-13 (7DTE): 525 traded vs OI 94
- **QQQ** PUT 640 2026-11-12 (6DTE): 502 traded vs OI 381
- **SMH** PUT 440 2026-11-13 (7DTE): 537 traded vs OI 435
- **NFLX** PUT 61 2026-11-13 (7DTE): 1,332 traded vs OI 955
- **MU** PUT 645 2026-11-09 (3DTE): 507 traded vs OI 0
- **MU** CALL 712.5 2026-11-18 (12DTE): 1,119 traded vs OI 0
- **ORCL** PUT 114 2026-11-13 (7DTE): 521 traded vs OI 194
- **ARM** CALL 170 2026-11-06 (0DTE): 501 traded vs OI 11

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
