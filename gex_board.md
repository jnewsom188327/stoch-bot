# GEX + FLOW SCAN - Fri Nov 06, 03:35 PM ET
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
| 1 | **MSTR** | 129.19 | - | **-** | 20 | - | POS +$2.9M | 129.04 | 135 | 130 | -$4.7M | +$1.2M bull / +$0 bear | out (clean 30, ADX 32, RVol 0.6) |
| 2 | **SMH** | 464.92 | - | **-** | 19 | - | NEG -$650.3M | - | 505 | 465 | +$7.4M | +$31k bull / +$0 bear | out (clean 32, ADX 21, RVol 0.7) |
| 3 | **TSLA** | 360.77 | - | **-** | 19 | - | NEG -$380.9M | - | 360 | 360 | -$53.6M | +$7.1M bull / -$114k bear | out (clean 34, ADX 26, RVol 0.6) |
| 4 | **ARM** | 172.45 | - | **-** | 19 | - | NEG -$26.0M | - | 180 | 170 | -$666k | +$28k bull / +$0 bear | out (clean 25, ADX 18, RVol 1.1) |
| 5 | **HOOD** | 80.73 | - | **-** | 18 | - | NEG -$26.5M | 82.62 | 85 | 80 | +$2.1M | +$0 bull / -$26k bear | out (clean 30, ADX 26, RVol 0.7) |
| 6 | **AAPL** | 343.81 | - | **-** | 17 | - | NEG -$49.5M | 344.26 | 345 | 345 | -$17.9M | +$214k bull / -$669k bear | out (clean 27, ADX 12, RVol 0.3) |
| 7 | **AMD** | 448.85 | - | **-** | 17 | - | NEG -$210.9M | - | 430 | 450 | -$2.6M | +$113k bull / -$2.9M bear | out (clean 32, ADX 28, RVol 0.9) |
| 8 | **PLTR** | 160.95 | - | **-** | 17 | - | NEG -$82.9M | - | 165 | 160 | +$3.0M | +$667k bull / +$0 bear | out (clean 28, ADX 19, RVol 0.7) |
| 9 | **NVDA** | 187.72 | - | **-** | 16 | - | NEG -$322.4M | - | 200 | 190 | +$22.6M | +$727k bull / -$59k bear | out (clean 32, ADX 17, RVol 0.8) |
| 10 | **MSFT** | 532.77 | - | **-** | 16 | - | POS +$668.8M | 514.19 | 535 | 535 | +$4.1M | +$42k bull / +$0 bear | out (clean 34, ADX 19, RVol 0.4) |
| 11 | **AVGO** | 293.02 | - | **-** | 16 | - | NEG -$151.1M | - | 320 | 300 | +$2.9M | +$189k bull / +$0 bear | out (clean 30, ADX 14, RVol 1.0) |
| 12 | **MU** | 692.33 | - | **-** | 16 | - | NEG -$184.0M | - | 700 | 700 | +$72.4M | +$1.3M bull / -$716k bear | out (clean 31, ADX 11, RVol 0.8) |
| 13 | **SHOP** | 149.28 | - | **-** | 15 | - | NEG -$3.6M | 150.86 | 150 | 150 | -$1.0M | - | out (clean 35, ADX 25, RVol 0.7) |
| 14 | **QQQ** | 658.85 | - | **-** | 14 | - | NEG -$6.0B | - | 700 | 660 | +$41.5M | +$3.0M bull / -$138k bear | out (clean 33, ADX 12, RVol 0.6) |
| 15 | **META** | 615.48 | - | **-** | 14 | - | NEG -$158.1M | 621.58 | 615 | 615 | -$328k | +$466k bull / -$114k bear | out (clean 32, ADX 21, RVol 0.3) |
| 16 | **AMZN** | 260.75 | - | **-** | 14 | - | POS +$384.7M | - | 260 | 260 | +$1.1M | +$403k bull / +$0 bear | out (clean 36, ADX 18, RVol 0.4) |
| 17 | **GOOGL** | 286.08 | - | **-** | 14 | - | POS +$74.6M | 284.06 | 285 | 290 | +$1.7M | +$59k bull / -$1.1M bear | out (clean 33, ADX 11, RVol 0.4) |
| 18 | **SMCI** | 28.91 | - | **-** | 14 | - | NEG -$4.2M | 29.52 | 30 | 29 | -$1.8M | - | out (clean 33, ADX 31, RVol 0.5) |
| 19 | **SPY** | 737.76 | - | **-** | 13 | - | NEG -$15.9B | 767.75 | 760 | 740 | -$12.0M | +$1.2M bull / +$0 bear | out (clean 33, ADX 9, RVol 0.6) |
| 20 | **UBER** | 68.65 | - | **-** | 12 | - | NEG -$474k | 68.67 | 70 | 65 | +$256k | - | out (clean 32, ADX 32, RVol 0.8) |
| 21 | **ORCL** | 115.28 | - | **-** | 11 | - | NEG -$99.8M | - | 116 | 115 | -$5.9M | - | out (clean 30, ADX 13, RVol 0.7) |
| 22 | **COIN** | 135.32 | - | **-** | 10 | - | NEG -$27.1M | 137.32 | 142 | 135 | -$2.8M | - | out (clean 32, ADX 23, RVol 0.6) |
| 23 | **DELL** | 332.15 | - | **-** | 10 | - | NEG -$34.9M | - | 335 | 335 | +$5.5M | - | out (clean 31, ADX 21, RVol 0.5) |
| 24 | **CRM** | 214.91 | - | **-** | 9 | - | NEG -$26.2M | - | 195 | 215 | -$154k | - | out (clean 34, ADX 25, RVol 1.8) |
| 25 | **BABA** | 108.95 | - | **-** | 7 | - | POS +$30.1M | 103.78 | 110 | 110 | -$326k | - | out (clean 32, ADX 16, RVol 1.3) |
| 26 | **IWM** | 274.46 | - | **-** | 6 | - | NEG -$3.6B | 284.49 | 275 | 275 | -$7.8M | - | out (clean 32, ADX 15, RVol 0.8) |
| 27 | **NFLX** | 63.60 | - | **-** | 6 | - | NEG -$14.8M | 63.72 | 64 | 65 | +$331k | - | out (clean 32, ADX 16, RVol 0.6) |

## Big prints this scan (67)
- **TSLA** PUT 360 2026-11-13 (7DTE): 300 @ 10.75 = **+$322k** MID | vol 5,119 / OI 1,235
- **TSLA** CALL 345 2026-11-06 (0DTE): 132 @ 15.84 = **+$209k** MID | vol 3,243 / OI 106
- **MU** PUT 710 2026-11-06 (0DTE): 100 @ 20.00 = **+$200k** BUY | vol 8,650 / OI 1,511
- **MU** PUT 700 2026-11-11 (5DTE): 51 @ 34.85 = **+$178k** BUY | vol 329 / OI 64
- **QQQ** PUT 658 2026-11-09 (3DTE): 300 @ 5.60 = **+$168k** SELL | vol 14,995 / OI 30
- **QQQ** CALL 660 2026-11-09 (3DTE): 250 @ 5.39 = **+$135k** BUY | vol 32,667 / OI 10
- **QQQ** PUT 650 2026-11-10 (4DTE): 267 @ 4.92 = **+$131k** SELL | vol 4,620 / OI 692
- **AMD** PUT 447.5 2026-11-09 (3DTE): 100 @ 12.00 = **+$120k** BUY | vol 1,142 / OI 239
- **QQQ** PUT 660 2026-11-13 (7DTE): 100 @ 11.98 = **+$120k** SELL | vol 6,485 / OI 5,164
- **AMD** PUT 447.5 2026-11-09 (3DTE): 100 @ 11.85 = **+$118k** BUY | vol 1,142 / OI 239
- **TSLA** PUT 370 2026-11-06 (0DTE): 120 @ 9.50 = **+$114k** BUY | vol 3,388 / OI 4,963
- **SPY** PUT 731 2026-11-13 (7DTE): 186 @ 5.98 = **+$111k** SELL | vol 2,477 / OI 620
- **AAPL** CALL 342.5 2026-11-09 (3DTE): 300 @ 3.64 = **+$109k** BUY | vol 5,448 / OI 256
- **QQQ** PUT 659 2026-11-06 (0DTE): 984 @ 1.10 = **+$108k** MID | vol 188,433 / OI 192
- **TSLA** PUT 370 2026-11-06 (0DTE): 120 @ 9.00 = **+$108k** SELL | vol 3,388 / OI 4,963

## New unusual volume (traded more than open interest, 500+)
- **QQQ** CALL 712 2026-11-09 (3DTE): 598 traded vs OI 312
- **QQQ** CALL 655 2026-11-11 (5DTE): 503 traded vs OI 2
- **QQQ** CALL 675 2026-11-30 (24DTE): 506 traded vs OI 122
- **IWM** PUT 274 2026-11-13 (7DTE): 523 traded vs OI 496
- **NVDA** CALL 197.5 2026-11-16 (10DTE): 502 traded vs OI 6
- **TSLA** CALL 365 2026-11-16 (10DTE): 501 traded vs OI 1
- **AAPL** CALL 337.5 2026-11-13 (7DTE): 512 traded vs OI 259
- **AAPL** PUT 342.5 2026-11-11 (5DTE): 503 traded vs OI 302
- **AAPL** PUT 325 2026-11-09 (3DTE): 2,906 traded vs OI 1,253
- **AMD** CALL 467.5 2026-11-09 (3DTE): 505 traded vs OI 236
- **AMZN** PUT 242.5 2026-11-09 (3DTE): 500 traded vs OI 129
- **AMZN** PUT 247.5 2026-11-09 (3DTE): 505 traded vs OI 156
- **MSFT** CALL 560 2026-11-13 (7DTE): 1,126 traded vs OI 1,124
- **MU** PUT 680 2026-11-11 (5DTE): 503 traded vs OI 11
- **ORCL** CALL 116 2026-11-13 (7DTE): 502 traded vs OI 62

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
