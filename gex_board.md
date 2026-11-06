# GEX + FLOW SCAN - Fri Nov 06, 02:30 PM ET
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
Last 1m check 14:30:08 ET, last candle SPY 14:29, QQQ 14:29 | no errors
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
| 1 | **TSLA** | 359.86 | - | **-** | 18 | - | NEG -$339.7M | - | 360 | 360 | -$56.2M | +$272k bull / +$0 bear | out (clean 34, ADX 22, RVol 0.2) |
| 2 | **COIN** | 133.59 | - | **-** | 18 | - | NEG -$23.0M | 136.91 | 142 | 135 | -$2.4M | +$880k bull / +$0 bear | out (clean 31, ADX 17, RVol 0.4) |
| 3 | **SMH** | 463.60 | - | **-** | 17 | - | NEG -$585.5M | - | 505 | 465 | +$6.4M | +$158k bull / +$0 bear | out (clean 32, ADX 18, RVol 0.4) |
| 4 | **AAPL** | 344.17 | - | **-** | 17 | - | NEG -$3.8M | 344.19 | 345 | 345 | -$17.2M | +$62k bull / +$0 bear | out (clean 27, ADX 9, RVol 0.2) |
| 5 | **AMD** | 445.87 | - | **-** | 16 | - | NEG -$175.0M | - | 430 | 450 | +$4.5M | +$418k bull / -$1.5M bear | out (clean 32, ADX 24, RVol 0.5) |
| 6 | **NFLX** | 63.85 | PINNED between the walls (positive gamma) - chop | **-** | 16 | - | POS +$10.5M | 63.71 | 64 | 64 | -$379k | - | out (clean 32, ADX 10, RVol 0.2) |
| 7 | **AVGO** | 291.93 | - | **-** | 16 | - | NEG -$131.3M | - | 320 | 300 | +$3.1M | +$681k bull / +$0 bear | out (clean 31, ADX 15, RVol 0.8) |
| 8 | **MU** | 691.23 | - | **-** | 16 | - | NEG -$184.4M | - | 700 | 700 | +$73.4M | +$949k bull / -$304k bear | out (clean 32, ADX 14, RVol 0.3) |
| 9 | **MSTR** | 127.58 | - | **-** | 16 | - | NEG -$11.8M | 128.41 | 135 | 125 | -$3.6M | +$1.5M bull / +$0 bear | out (clean 30, ADX 19, RVol 0.3) |
| 10 | **QQQ** | 658.57 | - | **-** | 15 | - | NEG -$5.8B | - | 700 | 680 | +$48.2M | +$2.4M bull / -$258k bear | out (clean 33, ADX 15, RVol 0.6) |
| 11 | **IWM** | 273.91 | - | **-** | 15 | - | NEG -$3.4B | 285.76 | 275 | 275 | -$4.1M | +$0 bull / -$117k bear | out (clean 33, ADX 14, RVol 0.4) |
| 12 | **NVDA** | 187.37 | - | **-** | 15 | - | NEG -$406.2M | - | 200 | 190 | +$23.0M | +$272k bull / -$65k bear | out (clean 33, ADX 11, RVol 0.5) |
| 13 | **META** | 616.60 | - | **-** | 15 | - | NEG -$131.8M | 621.97 | 620 | 610 | -$6.1M | +$432k bull / +$0 bear | out (clean 32, ADX 17, RVol 0.2) |
| 14 | **MSFT** | 532.79 | - | **-** | 15 | - | POS +$674.4M | 512.12 | 535 | 535 | +$3.0M | +$297k bull / +$0 bear | out (clean 34, ADX 14, RVol 0.2) |
| 15 | **PLTR** | 160.79 | - | **-** | 15 | - | NEG -$83.4M | - | 165 | 160 | +$3.4M | +$0 bull / -$54k bear | out (clean 27, ADX 10, RVol 0.4) |
| 16 | **SHOP** | 149.07 | - | **-** | 15 | - | NEG -$1.3M | 149.91 | 150 | 150 | -$1.1M | - | out (clean 35, ADX 21, RVol 0.4) |
| 17 | **SPY** | 737.94 | - | **-** | 14 | - | NEG -$15.6B | 768.61 | 760 | 740 | -$30.5M | +$572k bull / +$0 bear | out (clean 33, ADX 13, RVol 0.6) |
| 18 | **AMZN** | 261.83 | - | **-** | 14 | - | POS +$347.8M | - | 260 | 260 | -$938k | +$31k bull / +$0 bear | out (clean 35, ADX 16, RVol 0.2) |
| 19 | **GOOGL** | 285.83 | - | **-** | 14 | - | POS +$88.0M | 282.86 | 285 | 285 | +$2.2M | +$791k bull / +$0 bear | out (clean 33, ADX 12, RVol 0.2) |
| 20 | **UBER** | 68.77 | - | **-** | 13 | - | POS +$4.5M | 68.4 | 70 | 65 | +$286k | - | out (clean 30, ADX 34, RVol 0.5) |
| 21 | **DELL** | 328.51 | - | **-** | 10 | - | NEG -$28.7M | - | 330 | 335 | +$6.2M | - | out (clean 31, ADX 12, RVol 0.3) |
| 22 | **ORCL** | 114.83 | - | **-** | 10 | - | NEG -$75.9M | - | 116 | 115 | -$5.4M | - | out (clean 30, ADX 16, RVol 0.3) |
| 23 | **ARM** | 173.50 | - | **-** | 9 | - | NEG -$24.4M | - | 190 | 170 | -$760k | - | out (clean 26, ADX 21, RVol 0.3) |
| 24 | **CRM** | 214.52 | - | **-** | 8 | - | NEG -$23.8M | - | 230 | 215 | -$198k | - | out (clean 34, ADX 23, RVol 0.9) |
| 25 | **BABA** | 109.59 | - | **-** | 6 | - | POS +$32.2M | 105.1 | 110 | 110 | -$409k | - | out (clean 33, ADX 14, RVol 0.6) |
| 26 | **SMCI** | 28.29 | - | **-** | 5 | - | NEG -$4.7M | - | 30 | 28 | -$400k | - | out (clean 33, ADX 14, RVol 0.2) |
| 27 | **HOOD** | 79.64 | - | **-** | 5 | - | NEG -$27.5M | 81.79 | 85 | 80 | +$2.1M | - | out (clean 30, ADX 14, RVol 0.3) |

## Big prints this scan (51)
- **MSTR** CALL 133 2026-11-13 (7DTE): 3,950 @ 3.74 = **+$1.5M** BUY | vol 29,227 / OI 95
- **COIN** CALL 137 2026-11-13 (7DTE): 2,000 @ 4.40 = **+$880k** BUY | vol 6,530 / OI 93
- **GOOGL** CALL 290 2026-11-13 (7DTE): 999 @ 4.26 = **+$426k** BUY | vol 3,577 / OI 2,185
- **COIN** PUT 135 2026-11-13 (7DTE): 500 @ 6.50 = **+$325k** MID | vol 1,569 / OI 777
- **GOOGL** CALL 285 2026-11-06 (0DTE): 999 @ 1.83 = **+$183k** BUY | vol 11,955 / OI 6,680
- **GOOGL** CALL 297.5 2026-11-13 (7DTE): 999 @ 1.83 = **+$183k** BUY | vol 4,303 / OI 322
- **QQQ** PUT 658 2026-11-09 (3DTE): 300 @ 5.84 = **+$175k** SELL | vol 9,229 / OI 30
- **QQQ** CALL 659 2026-11-06 (0DTE): 763 @ 1.86 = **+$142k** BUY | vol 105,078 / OI 0
- **SPY** PUT 715 2026-11-13 (7DTE): 442 @ 2.83 = **+$125k** SELL | vol 4,802 / OI 1,935
- **QQQ** CALL 658 2026-11-06 (0DTE): 500 @ 2.40 = **+$120k** BUY | vol 113,440 / OI 0
- **QQQ** CALL 658 2026-11-06 (0DTE): 500 @ 2.20 = **+$110k** BUY | vol 113,440 / OI 0
- **AVGO** PUT 300 2026-11-13 (7DTE): 79 @ 13.80 = **+$109k** SELL | vol 860 / OI 1,090
- **SPY** PUT 710 2026-11-13 (7DTE): 442 @ 2.31 = **+$102k** SELL | vol 11,316 / OI 3,271
- **NVDA** PUT 185 2026-11-13 (7DTE): 200 @ 5.10 = **+$102k** SELL | vol 7,245 / OI 4,433
- **MSFT** PUT 535 2026-11-13 (7DTE): 87 @ 9.65 = **+$84k** SELL | vol 1,184 / OI 350

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 714 2026-11-11 (5DTE): 506 traded vs OI 158
- **SPY** PUT 720 2026-11-10 (4DTE): 866 traded vs OI 855
- **SPY** CALL 748 2026-11-11 (5DTE): 508 traded vs OI 2
- **QQQ** CALL 724 2026-11-10 (4DTE): 1,274 traded vs OI 0
- **QQQ** CALL 666 2026-11-10 (4DTE): 527 traded vs OI 0
- **QQQ** PUT 611 2026-11-11 (5DTE): 500 traded vs OI 0
- **QQQ** CALL 697 2026-11-12 (6DTE): 603 traded vs OI 30
- **SMH** CALL 505 2026-11-20 (14DTE): 525 traded vs OI 360
- **META** CALL 640 2026-11-11 (5DTE): 501 traded vs OI 81
- **COIN** CALL 143 2026-11-06 (0DTE): 8,281 traded vs OI 8,028
- **MU** PUT 692.5 2026-11-09 (3DTE): 501 traded vs OI 0
- **ARM** CALL 177.5 2026-11-06 (0DTE): 518 traded vs OI 41

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
