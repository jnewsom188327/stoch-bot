# GEX + FLOW SCAN - Fri Nov 06, 01:40 PM ET
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
Last 1m check 13:40:08 ET, last candle SPY 13:39, QQQ 13:39 | no errors
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
| 1 | **AAPL** | 344.38 | PINNED between the walls (positive gamma) - chop | **-** | 28 | - | POS +$32.5M | 344.09 | 345 | 345 | -$17.2M | +$62k bull / -$76k bear | out (clean 28, ADX 9, RVol 0.2) |
| 2 | **ORCL** | 114.45 | - | **-** | 23 | - | NEG -$66.4M | - | 125 | 115 | -$4.8M | +$0 bull / -$148k bear | out (clean 29, ADX 24, RVol 0.8) |
| 3 | **DELL** | 328.64 | - | **-** | 21 | - | NEG -$26.9M | - | 335 | 335 | +$5.7M | +$32k bull / -$26k bear | out (clean 31, ADX 20, RVol 0.4) |
| 4 | **NFLX** | 63.79 | FLIP CROSS up into positive gamma | **CALLS** | 19 | none: 26 calls 0-7DTE > 2 priced 0.40-0.80 > 2 delta 0.2+ > 2 spread ok > 2 liquid > best one only +8% at the target (needs +20%) (20 contracts' greeks worked out here) | POS +$9.1M | 62.86 | 64 | 64 | -$358k | - | out (clean 32, ADX 18, RVol 0.5) |
| 5 | **MSTR** | 127.38 | - | **-** | 19 | - | NEG -$11.7M | 128.22 | 135 | 125 | -$7.0M | +$0 bull / -$250k bear | out (clean 31, ADX 19, RVol 0.3) |
| 6 | **SMH** | 461.30 | - | **-** | 18 | - | NEG -$419.1M | - | 505 | 465 | +$7.2M | +$0 bull / -$292k bear | out (clean 32, ADX 17, RVol 0.4) |
| 7 | **TSLA** | 359.47 | - | **-** | 18 | - | NEG -$324.1M | - | 360 | 360 | -$60.6M | +$369k bull / -$208k bear | out (clean 35, ADX 19, RVol 0.3) |
| 8 | **AVGO** | 290.92 | - | **-** | 18 | - | NEG -$123.7M | - | 320 | 300 | +$2.7M | +$110k bull / -$27k bear | out (clean 31, ADX 24, RVol 1.0) |
| 9 | **NVDA** | 186.94 | - | **-** | 17 | - | NEG -$396.4M | - | 200 | 190 | +$30.1M | +$686k bull / -$496k bear | out (clean 33, ADX 18, RVol 0.5) |
| 10 | **META** | 617.50 | - | **-** | 17 | - | NEG -$125.2M | 623.44 | 620 | 610 | -$7.4M | +$631k bull / -$69k bear | out (clean 33, ADX 24, RVol 0.3) |
| 11 | **AMZN** | 262.88 | - | **-** | 17 | - | POS +$380.2M | - | 265 | 265 | -$2.6M | +$0 bull / -$170k bear | out (clean 35, ADX 24, RVol 0.6) |
| 12 | **MSFT** | 533.03 | - | **-** | 17 | - | POS +$632.0M | 514.1 | 535 | 535 | +$4.4M | +$90k bull / +$0 bear | out (clean 34, ADX 17, RVol 0.4) |
| 13 | **MU** | 685.73 | - | **-** | 17 | - | NEG -$148.2M | - | 700 | 700 | +$77.5M | +$1.1M bull / -$2.8M bear | out (clean 32, ADX 15, RVol 0.6) |
| 14 | **SPY** | 737.90 | - | **-** | 16 | - | NEG -$14.3B | 765.75 | 760 | 740 | -$37.3M | +$247k bull / -$883k bear | out (clean 34, ADX 23, RVol 0.5) |
| 15 | **QQQ** | 657.51 | - | **-** | 16 | - | NEG -$4.6B | - | 700 | 660 | +$48.6M | +$450k bull / -$2.5M bear | out (clean 34, ADX 19, RVol 0.6) |
| 16 | **PLTR** | 160.16 | - | **-** | 16 | - | NEG -$77.7M | - | 165 | 160 | +$3.6M | +$0 bull / -$472k bear | out (clean 27, ADX 12, RVol 0.5) |
| 17 | **HOOD** | 79.83 | - | **-** | 16 | - | NEG -$27.2M | 83.8 | 85 | 80 | +$1.8M | +$0 bull / -$85k bear | out (clean 30, ADX 19, RVol 0.3) |
| 18 | **AMD** | 439.80 | - | **-** | 15 | - | NEG -$166.4M | - | 430 | 440 | +$10.1M | +$0 bull / -$633k bear | out (clean 31, ADX 17, RVol 0.7) |
| 19 | **SHOP** | 149.15 | - | **-** | 15 | - | NEG -$1.9M | 150.31 | 150 | 150 | -$1.1M | - | out (clean 36, ADX 19, RVol 0.7) |
| 20 | **UBER** | 69.09 | - | **-** | 12 | - | POS +$8.8M | 68.51 | 70 | 70 | +$268k | - | out (clean 30, ADX 32, RVol 0.2) |
| 21 | **COIN** | 133.74 | - | **-** | 11 | - | NEG -$22.1M | 136.72 | 142 | 135 | -$3.3M | - | out (clean 32, ADX 23, RVol 0.1) |
| 22 | **CRM** | 214.49 | - | **-** | 8 | - | NEG -$22.9M | - | 230 | 215 | -$226k | - | out (clean 34, ADX 20, RVol 1.0) |
| 23 | **ARM** | 172.78 | - | **-** | 7 | - | NEG -$26.1M | - | 190 | 170 | -$591k | - | out (clean 26, ADX 13, RVol 0.3) |
| 24 | **BABA** | 109.29 | - | **-** | 7 | - | POS +$33.5M | - | 110 | 110 | -$490k | - | out (clean 34, ADX 14, RVol 0.4) |
| 25 | **IWM** | 274.13 | - | **-** | 6 | - | NEG -$3.1B | 285.23 | 275 | 275 | -$6.8M | - | out (clean 33, ADX 15, RVol 0.5) |
| 26 | **GOOGL** | 285.79 | - | **-** | 6 | - | POS +$72.9M | 282.78 | 285 | 285 | +$2.4M | - | out (clean 33, ADX 16, RVol 0.5) |
| 27 | **SMCI** | 28.32 | - | **-** | 6 | - | NEG -$4.3M | 29.53 | 30 | 28 | -$409k | - | out (clean 34, ADX 18, RVol 0.2) |

## Big prints this scan (59)
- **QQQ** PUT 652 2026-11-09 (3DTE): 200 @ 5.28 = **+$106k** BUY | vol 2,919 / OI 283
- **QQQ** PUT 655 2026-11-06 (0DTE): 500 @ 2.05 = **+$102k** BUY | vol 203,239 / OI 6,673
- **NVDA** PUT 185 2026-11-13 (7DTE): 160 @ 6.00 = **+$96k** BUY | vol 6,673 / OI 4,433
- **MU** PUT 670 2026-11-06 (0DTE): 294 @ 3.15 = **+$93k** BUY | vol 44,962 / OI 734
- **MU** CALL 685 2026-11-11 (5DTE): 30 @ 30.40 = **+$91k** SELL | vol 196 / OI 0
- **AMD** CALL 450 2026-11-13 (7DTE): 54 @ 16.70 = **+$90k** SELL | vol 2,607 / OI 108
- **MU** CALL 690 2026-11-11 (5DTE): 30 @ 27.90 = **+$84k** SELL | vol 308 / OI 0
- **SMH** PUT 460 2026-11-13 (7DTE): 49 @ 16.84 = **+$83k** BUY | vol 696 / OI 976
- **MU** PUT 660 2026-11-13 (7DTE): 29 @ 27.80 = **+$81k** BUY | vol 1,218 / OI 358
- **MU** PUT 660 2026-11-13 (7DTE): 29 @ 27.65 = **+$80k** BUY | vol 1,218 / OI 358
- **MU** PUT 660 2026-11-13 (7DTE): 29 @ 27.65 = **+$80k** BUY | vol 1,218 / OI 358
- **SMH** CALL 460 2026-11-13 (7DTE): 49 @ 16.05 = **+$79k** SELL | vol 377 / OI 0
- **AMD** CALL 450 2026-11-13 (7DTE): 44 @ 16.92 = **+$74k** SELL | vol 2,607 / OI 108
- **PLTR** CALL 165 2026-11-13 (7DTE): 200 @ 3.32 = **+$66k** SELL | vol 8,630 / OI 277
- **AMD** CALL 450 2026-11-13 (7DTE): 39 @ 17.00 = **+$66k** SELL | vol 2,607 / OI 108

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 732 2026-11-13 (7DTE): 562 traded vs OI 3
- **QQQ** PUT 617 2026-11-20 (14DTE): 3,210 traded vs OI 0
- **NVDA** CALL 202.5 2026-11-20 (14DTE): 1,461 traded vs OI 1,457
- **AMD** PUT 435 2026-11-20 (14DTE): 509 traded vs OI 59
- **META** CALL 660 2026-11-13 (7DTE): 657 traded vs OI 649
- **META** CALL 615 2026-11-13 (7DTE): 552 traded vs OI 526
- **MSFT** CALL 565 2026-11-11 (5DTE): 574 traded vs OI 526
- **PLTR** PUT 152.5 2026-11-06 (0DTE): 2,312 traded vs OI 2,238
- **MU** PUT 620 2026-11-09 (3DTE): 500 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
