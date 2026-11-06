# GEX + FLOW SCAN - Fri Nov 06, 02:20 PM ET
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
Last 1m check 14:20:08 ET, last candle SPY 14:19, QQQ 14:19 | no errors
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
| 1 | **AAPL** | 344.21 | PINNED between the walls (positive gamma) - chop | **-** | 28 | - | POS +$14.9M | 344.05 | 345 | 345 | -$17.7M | +$54k bull / -$68k bear | out (clean 27, ADX 9, RVol 0.2) |
| 2 | **ORCL** | 114.90 | - | **-** | 21 | - | NEG -$79.5M | - | 116 | 115 | -$5.6M | +$0 bull / -$113k bear | out (clean 30, ADX 16, RVol 0.3) |
| 3 | **TSLA** | 359.28 | - | **-** | 18 | - | NEG -$339.1M | - | 360 | 360 | -$55.5M | +$129k bull / -$120k bear | out (clean 35, ADX 22, RVol 0.2) |
| 4 | **MSTR** | 127.45 | - | **-** | 18 | - | NEG -$13.0M | 128.34 | 135 | 125 | -$5.1M | +$0 bull / -$1.5M bear | out (clean 30, ADX 20, RVol 0.3) |
| 5 | **SMH** | 463.57 | - | **-** | 17 | - | NEG -$575.9M | - | 505 | 465 | +$6.3M | +$158k bull / -$36k bear | out (clean 32, ADX 18, RVol 0.4) |
| 6 | **NFLX** | 63.86 | PINNED between the walls (positive gamma) - chop | **-** | 17 | - | POS +$11.2M | 62.7 | 64 | 64 | -$419k | - | out (clean 32, ADX 12, RVol 0.3) |
| 7 | **QQQ** | 658.42 | - | **-** | 16 | - | NEG -$5.3B | - | 700 | 680 | +$40.2M | +$1.5M bull / -$961k bear | out (clean 34, ADX 16, RVol 1.0) |
| 8 | **AMD** | 446.47 | - | **-** | 16 | - | NEG -$178.5M | - | 430 | 450 | +$3.5M | +$34k bull / -$3.6M bear | out (clean 32, ADX 23, RVol 0.6) |
| 9 | **AVGO** | 292.44 | - | **-** | 16 | - | NEG -$135.4M | - | 320 | 300 | +$1.8M | +$103k bull / +$0 bear | out (clean 31, ADX 17, RVol 1.2) |
| 10 | **MU** | 691.71 | - | **-** | 16 | - | NEG -$186.6M | - | 700 | 700 | +$71.5M | +$377k bull / -$2.4M bear | out (clean 32, ADX 14, RVol 0.4) |
| 11 | **IWM** | 273.93 | - | **-** | 15 | - | NEG -$3.4B | 285.75 | 275 | 275 | -$4.3M | +$82k bull / +$0 bear | out (clean 33, ADX 16, RVol 0.4) |
| 12 | **NVDA** | 187.22 | - | **-** | 15 | - | NEG -$419.0M | - | 200 | 190 | +$23.7M | +$162k bull / -$142k bear | out (clean 33, ADX 12, RVol 0.5) |
| 13 | **META** | 616.97 | - | **-** | 15 | - | NEG -$123.4M | 622.48 | 620 | 610 | -$6.4M | +$138k bull / +$0 bear | out (clean 32, ADX 16, RVol 0.2) |
| 14 | **MSFT** | 532.75 | - | **-** | 15 | - | POS +$700.0M | 512.35 | 535 | 535 | +$2.6M | +$85k bull / -$136k bear | out (clean 34, ADX 13, RVol 0.4) |
| 15 | **SPY** | 738.05 | - | **-** | 14 | - | NEG -$15.4B | 768.41 | 760 | 740 | -$36.7M | +$230k bull / +$0 bear | out (clean 34, ADX 14, RVol 0.6) |
| 16 | **GOOGL** | 285.92 | - | **-** | 14 | - | POS +$74.7M | 282.67 | 285 | 290 | +$1.3M | +$0 bull / -$230k bear | out (clean 33, ADX 13, RVol 0.2) |
| 17 | **SHOP** | 148.84 | - | **-** | 14 | - | NEG -$2.3M | 150.2 | 150 | 150 | -$1.1M | - | out (clean 35, ADX 20, RVol 0.5) |
| 18 | **UBER** | 68.81 | - | **-** | 12 | - | POS +$6.1M | 68.51 | 70 | 65 | +$278k | - | out (clean 30, ADX 33, RVol 0.4) |
| 19 | **COIN** | 133.76 | - | **-** | 11 | - | NEG -$23.8M | 136.74 | 142 | 135 | -$3.3M | - | out (clean 31, ADX 19, RVol 0.5) |
| 20 | **DELL** | 329.02 | - | **-** | 10 | - | NEG -$28.4M | - | 330 | 335 | +$6.1M | - | out (clean 30, ADX 14, RVol 0.3) |
| 21 | **ARM** | 173.64 | - | **-** | 9 | - | NEG -$23.5M | - | 190 | 170 | -$768k | - | out (clean 26, ADX 19, RVol 0.3) |
| 22 | **CRM** | 214.56 | - | **-** | 8 | - | NEG -$21.0M | - | 230 | 215 | -$199k | - | out (clean 34, ADX 23, RVol 0.9) |
| 23 | **PLTR** | 160.39 | - | **-** | 6 | - | NEG -$84.2M | - | 165 | 160 | +$3.7M | - | out (clean 27, ADX 10, RVol 0.4) |
| 24 | **SMCI** | 28.30 | - | **-** | 6 | - | NEG -$4.3M | 29.55 | 30 | 28 | -$412k | - | out (clean 33, ADX 16, RVol 0.3) |
| 25 | **HOOD** | 79.72 | - | **-** | 5 | - | NEG -$31.4M | 83.83 | 85 | 80 | +$2.1M | - | out (clean 30, ADX 16, RVol 0.3) |
| 26 | **BABA** | 109.44 | - | **-** | 5 | - | POS +$29.1M | 104.98 | 110 | 110 | -$390k | - | out (clean 33, ADX 12, RVol 0.4) |
| 27 | **AMZN** | 261.96 | - | **-** | 4 | - | POS +$362.9M | - | 265 | 260 | -$1.2M | - | out (clean 35, ADX 16, RVol 0.2) |

## Big prints this scan (58)
- **QQQ** PUT 645 2026-11-13 (7DTE): 450 @ 7.16 = **+$322k** SELL | vol 3,039 / OI 2,223
- **QQQ** PUT 640 2026-11-13 (7DTE): 450 @ 6.00 = **+$270k** SELL | vol 6,016 / OI 2,420
- **QQQ** PUT 645 2026-11-13 (7DTE): 271 @ 7.18 = **+$195k** SELL | vol 3,039 / OI 2,223
- **QQQ** PUT 640 2026-11-13 (7DTE): 271 @ 5.98 = **+$162k** SELL | vol 6,016 / OI 2,420
- **AMD** PUT 450 2026-11-06 (0DTE): 200 @ 6.50 = **+$130k** BUY | vol 8,337 / OI 5,339
- **SPY** CALL 745 2026-11-13 (7DTE): 211 @ 5.51 = **+$116k** BUY | vol 7,030 / OI 168
- **QQQ** CALL 658 2026-11-06 (0DTE): 490 @ 2.35 = **+$115k** BUY | vol 108,145 / OI 0
- **QQQ** CALL 658 2026-11-06 (0DTE): 500 @ 2.30 = **+$115k** BUY | vol 108,145 / OI 0
- **QQQ** CALL 658 2026-11-06 (0DTE): 500 @ 2.30 = **+$115k** BUY | vol 108,145 / OI 0
- **SPY** CALL 737 2026-11-06 (0DTE): 540 @ 2.10 = **+$113k** BUY | vol 110,987 / OI 267
- **QQQ** CALL 659 2026-11-12 (6DTE): 100 @ 11.06 = **+$111k** BUY | vol 403 / OI 0
- **QQQ** CALL 661 2026-11-09 (3DTE): 200 @ 5.39 = **+$108k** BUY | vol 6,952 / OI 0
- **AVGO** CALL 300 2026-11-13 (7DTE): 140 @ 7.35 = **+$103k** BUY | vol 1,352 / OI 88
- **MSFT** PUT 535 2026-11-13 (7DTE): 90 @ 9.40 = **+$85k** SELL | vol 1,093 / OI 350
- **AMD** CALL 450 2026-11-13 (7DTE): 41 @ 19.76 = **+$81k** SELL | vol 3,194 / OI 108

## New unusual volume (traded more than open interest, 500+)
- **QQQ** PUT 635 2026-11-09 (3DTE): 9,446 traded vs OI 9,441
- **QQQ** CALL 658 2026-11-10 (4DTE): 539 traded vs OI 0
- **QQQ** PUT 645 2026-11-13 (7DTE): 3,039 traded vs OI 2,223
- **QQQ** CALL 658 2026-11-13 (7DTE): 524 traded vs OI 0
- **QQQ** PUT 656 2026-11-12 (6DTE): 1,652 traded vs OI 38
- **QQQ** CALL 702 2026-11-12 (6DTE): 734 traded vs OI 30
- **QQQ** CALL 656 2026-11-12 (6DTE): 1,843 traded vs OI 0
- **QQQ** CALL 701 2026-11-12 (6DTE): 969 traded vs OI 43
- **QQQ** PUT 625 2026-11-30 (24DTE): 2,312 traded vs OI 903
- **QQQ** CALL 676 2026-11-20 (14DTE): 517 traded vs OI 357
- **NVDA** PUT 175 2026-11-16 (10DTE): 500 traded vs OI 46
- **TSLA** PUT 365 2026-11-06 (0DTE): 4,193 traded vs OI 4,113
- **AMD** PUT 410 2026-11-13 (7DTE): 507 traded vs OI 320
- **AMD** PUT 437.5 2026-11-09 (3DTE): 501 traded vs OI 62
- **UBER** CALL 74 2026-11-13 (7DTE): 587 traded vs OI 585

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
