# GEX + FLOW SCAN - Fri Nov 06, 03:15 PM ET
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
Last 1m check 15:15:08 ET, last candle SPY 15:14, QQQ 15:14 | no errors
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
| 1 | **CRM** | 213.78 | RUN: clean trend + negative gamma + flow agrees | **PUTS** | 50 | none: 34 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (27 contracts' greeks worked out here) | NEG -$23.6M | - | 195 | 215 | -$128k | - | SHORT (clean 34, ADX 29, RVol 1.5) |
| 2 | **AAPL** | 343.50 | FLIP CROSS up into positive gamma | **CALLS** | 29 | none: 112 calls 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (58 contracts' greeks worked out here) | POS +$260.5M | 341.99 | 345 | 340 | -$17.0M | +$165k bull / -$361k bear | out (clean 27, ADX 13, RVol 0.3) |
| 3 | **UBER** | 68.59 | FLIP CROSS up into positive gamma | **CALLS** | 25 | none: 28 calls 0-7DTE > 2 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only +14% at the target (needs +20%) (17 contracts' greeks worked out here) | POS +$2.2M | 68.5 | 70 | 65 | +$295k | - | out (clean 31, ADX 37, RVol 0.4) |
| 4 | **ORCL** | 115.50 | - | **-** | 21 | - | NEG -$88.6M | - | 116 | 115 | -$5.8M | +$0 bull / -$44k bear | out (clean 30, ADX 13, RVol 0.7) |
| 5 | **TSLA** | 361.76 | - | **-** | 20 | - | NEG -$357.6M | - | 360 | 360 | -$58.1M | +$0 bull / -$697k bear | out (clean 34, ADX 29, RVol 0.4) |
| 6 | **SMH** | 465.52 | - | **-** | 19 | - | NEG -$667.3M | - | 505 | 465 | +$7.3M | +$0 bull / -$84k bear | out (clean 32, ADX 21, RVol 0.9) |
| 7 | **MSTR** | 129.13 | - | **-** | 18 | - | POS +$6.9M | 128.85 | 135 | 130 | -$3.6M | +$0 bull / -$2.2M bear | out (clean 30, ADX 26, RVol 0.5) |
| 8 | **NFLX** | 63.74 | FLIP CROSS down into negative gamma | **PUTS** | 17 | none: 26 puts 0-7DTE > 1 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only +7% at the target (needs +20%) (17 contracts' greeks worked out here) | NEG -$816k | 63.75 | 64 | 64 | +$120k | - | out (clean 32, ADX 15, RVol 0.5) |
| 9 | **PLTR** | 161.49 | - | **-** | 17 | - | NEG -$78.1M | - | 165 | 160 | +$2.5M | +$0 bull / -$30k bear | out (clean 28, ADX 22, RVol 0.6) |
| 10 | **HOOD** | 80.36 | - | **-** | 17 | - | NEG -$28.0M | 81.91 | 85 | 80 | +$2.2M | +$38k bull / -$119k bear | out (clean 30, ADX 21, RVol 0.6) |
| 11 | **NVDA** | 188.53 | - | **-** | 16 | - | NEG -$436.4M | - | 200 | 190 | +$21.4M | +$0 bull / -$2.3M bear | out (clean 32, ADX 15, RVol 0.7) |
| 12 | **AMD** | 448.72 | - | **-** | 16 | - | NEG -$192.9M | - | 430 | 450 | +$2.5M | +$0 bull / -$869k bear | out (clean 32, ADX 27, RVol 0.6) |
| 13 | **MSFT** | 532.17 | - | **-** | 16 | - | POS +$699.1M | 513.03 | 530 | 535 | +$4.0M | +$162k bull / -$126k bear | out (clean 34, ADX 18, RVol 0.2) |
| 14 | **AVGO** | 293.27 | - | **-** | 16 | - | NEG -$150.9M | - | 320 | 300 | +$3.0M | +$0 bull / -$579k bear | out (clean 30, ADX 14, RVol 1.0) |
| 15 | **MU** | 693.30 | - | **-** | 16 | - | NEG -$184.1M | - | 700 | 700 | +$75.5M | +$204k bull / -$1.9M bear | out (clean 31, ADX 12, RVol 0.6) |
| 16 | **IWM** | 274.25 | - | **-** | 15 | - | NEG -$3.5B | 284.74 | 275 | 275 | -$5.1M | +$0 bull / -$420k bear | out (clean 33, ADX 14, RVol 0.8) |
| 17 | **META** | 616.36 | - | **-** | 15 | - | NEG -$114.9M | 621.85 | 620 | 615 | -$1.7M | +$553k bull / -$726k bear | out (clean 32, ADX 21, RVol 0.4) |
| 18 | **GOOGL** | 286.14 | - | **-** | 15 | - | POS +$79.2M | 283.06 | 285 | 285 | +$2.7M | +$0 bull / -$118k bear | out (clean 33, ADX 14, RVol 0.2) |
| 19 | **SHOP** | 148.61 | - | **-** | 15 | - | NEG -$2.9M | 150.57 | 150 | 150 | -$1.0M | - | out (clean 36, ADX 27, RVol 0.5) |
| 20 | **SPY** | 738.20 | - | **-** | 14 | - | NEG -$15.7B | 767.41 | 760 | 740 | -$26.1M | +$0 bull / -$2.3M bear | out (clean 33, ADX 12, RVol 0.6) |
| 21 | **QQQ** | 659.62 | - | **-** | 14 | - | NEG -$6.1B | - | 700 | 660 | +$39.7M | +$146k bull / -$571k bear | out (clean 33, ADX 15, RVol 0.4) |
| 22 | **AMZN** | 261.70 | - | **-** | 14 | - | POS +$287.6M | - | 265 | 260 | -$626k | +$302k bull / -$98k bear | out (clean 36, ADX 16, RVol 0.3) |
| 23 | **SMCI** | 28.70 | - | **-** | 12 | - | NEG -$5.1M | 30.16 | 30 | 29 | -$1.7M | - | out (clean 33, ADX 25, RVol 0.5) |
| 24 | **DELL** | 332.00 | - | **-** | 10 | - | NEG -$31.3M | - | 335 | 335 | +$5.5M | - | out (clean 31, ADX 16, RVol 0.4) |
| 25 | **ARM** | 173.13 | - | **-** | 10 | - | NEG -$25.2M | - | 190 | 170 | -$756k | - | out (clean 25, ADX 22, RVol 0.8) |
| 26 | **COIN** | 134.94 | - | **-** | 9 | - | NEG -$26.3M | 136.94 | 143 | 135 | -$2.9M | - | out (clean 31, ADX 18, RVol 0.6) |
| 27 | **BABA** | 109.20 | - | **-** | 7 | - | POS +$39.8M | - | 110 | 110 | -$393k | - | out (clean 32, ADX 16, RVol 0.9) |

## Big prints this scan (72)
- **NVDA** PUT 187.5 2026-11-13 (7DTE): 731 @ 5.90 = **+$431k** BUY | vol 7,666 / OI 3,561
- **SPY** CALL 738 2026-11-13 (7DTE): 207 @ 8.87 = **+$184k** SELL | vol 3,440 / OI 120
- **QQQ** CALL 658 2026-11-06 (0DTE): 800 @ 1.83 = **+$146k** BUY | vol 138,832 / OI 0
- **NVDA** PUT 187.5 2026-11-13 (7DTE): 199 @ 5.80 = **+$115k** BUY | vol 7,666 / OI 3,561
- **SPY** PUT 730 2026-11-09 (3DTE): 496 @ 2.24 = **+$111k** BUY | vol 50,793 / OI 2,461
- **MSTR** CALL 131 2026-11-13 (7DTE): 230 @ 4.72 = **+$109k** SELL | vol 2,168 / OI 188
- **MSTR** CALL 131 2026-11-13 (7DTE): 230 @ 4.72 = **+$109k** SELL | vol 2,168 / OI 188
- **SPY** CALL 734 2026-11-13 (7DTE): 95 @ 11.09 = **+$105k** SELL | vol 952 / OI 15
- **AVGO** PUT 297.5 2026-11-13 (7DTE): 74 @ 12.90 = **+$95k** BUY | vol 1,241 / OI 200
- **AVGO** PUT 297.5 2026-11-13 (7DTE): 74 @ 12.90 = **+$95k** BUY | vol 1,241 / OI 200
- **MSFT** PUT 535 2026-11-13 (7DTE): 90 @ 10.15 = **+$91k** MID | vol 1,303 / OI 350
- **MSTR** PUT 123 2026-11-13 (7DTE): 250 @ 3.63 = **+$91k** BUY | vol 2,536 / OI 329
- **TSLA** CALL 362.5 2026-11-09 (3DTE): 151 @ 5.80 = **+$88k** SELL | vol 6,069 / OI 8
- **SMH** CALL 485 2026-11-09 (3DTE): 496 @ 1.71 = **+$85k** MID | vol 1,450 / OI 0
- **MU** CALL 715 2026-11-09 (3DTE): 81 @ 10.35 = **+$84k** BUY | vol 886 / OI 0

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 718 2026-11-10 (4DTE): 514 traded vs OI 188
- **SPY** PUT 665 2026-11-13 (7DTE): 1,677 traded vs OI 0
- **SPY** PUT 737 2026-11-12 (6DTE): 509 traded vs OI 37
- **SPY** PUT 750 2026-12-04 (28DTE): 966 traded vs OI 955
- **SPY** CALL 730 2026-11-27 (21DTE): 501 traded vs OI 38
- **SPY** PUT 665 2026-11-20 (14DTE): 969 traded vs OI 0
- **QQQ** CALL 684 2026-11-11 (5DTE): 500 traded vs OI 51
- **QQQ** CALL 688 2026-11-12 (6DTE): 586 traded vs OI 30
- **IWM** PUT 268 2026-11-09 (3DTE): 1,352 traded vs OI 1,320
- **IWM** PUT 269 2026-11-10 (4DTE): 506 traded vs OI 235
- **IWM** PUT 267 2026-11-10 (4DTE): 981 traded vs OI 910
- **SMH** PUT 445 2026-11-20 (14DTE): 511 traded vs OI 505
- **NVDA** CALL 205 2026-11-18 (12DTE): 505 traded vs OI 296
- **NVDA** CALL 185 2026-11-20 (14DTE): 3,208 traded vs OI 3,112
- **TSLA** CALL 395 2026-12-04 (28DTE): 519 traded vs OI 426

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
