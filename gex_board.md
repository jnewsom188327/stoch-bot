# GEX + FLOW SCAN - Fri Nov 06, 03:25 PM ET
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
Last 1m check 15:25:08 ET, last candle SPY 15:24, QQQ 15:24 | no errors
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
| 1 | **SHOP** | 148.62 | FLIP CROSS down into negative gamma | **PUTS** | 28 | none: 44 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (35 contracts' greeks worked out here) | NEG -$2.7M | 149.84 | 150 | 150 | -$1.0M | - | out (clean 35, ADX 27, RVol 0.6) |
| 2 | **ORCL** | 115.29 | - | **-** | 20 | - | NEG -$99.9M | - | 116 | 115 | -$5.7M | +$0 bull / -$44k bear | out (clean 30, ADX 13, RVol 0.7) |
| 3 | **SMH** | 464.58 | - | **-** | 19 | - | NEG -$659.3M | - | 505 | 465 | +$7.5M | +$31k bull / -$58k bear | out (clean 32, ADX 20, RVol 0.9) |
| 4 | **TSLA** | 360.44 | - | **-** | 19 | - | NEG -$381.9M | - | 360 | 360 | -$52.6M | +$5.6M bull / -$466k bear | out (clean 34, ADX 28, RVol 0.5) |
| 5 | **MSTR** | 128.78 | - | **-** | 18 | - | POS +$7.6M | 128.3 | 135 | 130 | -$3.6M | +$1.2M bull / -$2.2M bear | out (clean 30, ADX 29, RVol 0.5) |
| 6 | **AAPL** | 343.75 | - | **-** | 17 | - | NEG -$60.3M | 344.5 | 345 | 345 | -$18.0M | +$121k bull / -$1.0M bear | out (clean 27, ADX 13, RVol 0.3) |
| 7 | **NFLX** | 63.71 | FLIP CROSS down into negative gamma | **PUTS** | 17 | none: 26 puts 0-7DTE > 1 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only +4% at the target (needs +20%) (17 contracts' greeks worked out here) | NEG -$9.0M | 63.87 | 64 | 65 | +$150k | - | out (clean 32, ADX 15, RVol 0.5) |
| 8 | **PLTR** | 161.05 | - | **-** | 17 | - | NEG -$69.1M | 168.43 | 165 | 160 | +$2.8M | +$54k bull / -$30k bear | out (clean 28, ADX 21, RVol 0.6) |
| 9 | **HOOD** | 80.52 | - | **-** | 17 | - | NEG -$29.5M | 82.68 | 85 | 80 | +$2.1M | +$38k bull / -$93k bear | out (clean 30, ADX 23, RVol 0.6) |
| 10 | **NVDA** | 188.07 | - | **-** | 16 | - | NEG -$295.0M | - | 200 | 190 | +$21.1M | +$59k bull / -$2.2M bear | out (clean 32, ADX 17, RVol 0.7) |
| 11 | **AMD** | 449.50 | - | **-** | 16 | - | NEG -$203.9M | - | 430 | 450 | +$381k | +$113k bull / -$2.0M bear | out (clean 32, ADX 28, RVol 0.8) |
| 12 | **MSFT** | 531.91 | - | **-** | 16 | - | POS +$696.5M | 513.1 | 530 | 530 | +$4.1M | +$162k bull / -$126k bear | out (clean 34, ADX 19, RVol 0.2) |
| 13 | **AVGO** | 292.87 | - | **-** | 16 | - | NEG -$140.0M | - | 320 | 292.5 | +$3.1M | +$90k bull / -$524k bear | out (clean 30, ADX 14, RVol 1.0) |
| 14 | **MU** | 690.19 | - | **-** | 16 | - | NEG -$160.3M | - | 700 | 700 | +$75.2M | +$1.2M bull / -$863k bear | out (clean 31, ADX 11, RVol 0.6) |
| 15 | **META** | 616.06 | - | **-** | 15 | - | NEG -$129.7M | 622.52 | 615 | 615 | -$935k | +$350k bull / -$840k bear | out (clean 32, ADX 21, RVol 0.4) |
| 16 | **QQQ** | 658.75 | - | **-** | 14 | - | NEG -$5.9B | - | 700 | 660 | +$43.8M | +$1.9M bull / -$709k bear | out (clean 33, ADX 13, RVol 0.5) |
| 17 | **AMZN** | 261.46 | - | **-** | 14 | - | POS +$321.8M | - | 260 | 260 | +$184k | +$582k bull / -$98k bear | out (clean 36, ADX 16, RVol 0.3) |
| 18 | **GOOGL** | 286.30 | - | **-** | 14 | - | POS +$68.5M | 283.28 | 285 | 290 | +$1.5M | +$0 bull / -$1.2M bear | out (clean 33, ADX 12, RVol 0.3) |
| 19 | **SPY** | 737.93 | - | **-** | 13 | - | NEG -$15.9B | 767.08 | 760 | 740 | -$18.8M | +$596k bull / -$2.3M bear | out (clean 33, ADX 10, RVol 0.6) |
| 20 | **SMCI** | 28.77 | - | **-** | 13 | - | NEG -$3.9M | 29.55 | 30 | 29 | -$1.7M | - | out (clean 33, ADX 28, RVol 0.4) |
| 21 | **UBER** | 68.60 | - | **-** | 12 | - | POS +$2.0M | 68.51 | 70 | 65 | +$256k | - | out (clean 32, ADX 35, RVol 0.4) |
| 22 | **DELL** | 332.48 | - | **-** | 10 | - | NEG -$32.5M | - | 335 | 335 | +$5.4M | - | out (clean 31, ADX 19, RVol 0.4) |
| 23 | **ARM** | 172.38 | - | **-** | 10 | - | NEG -$26.3M | - | 180 | 170 | -$732k | - | out (clean 25, ADX 20, RVol 1.0) |
| 24 | **CRM** | 214.40 | - | **-** | 10 | - | NEG -$20.4M | - | 195 | 215 | -$141k | - | out (clean 34, ADX 27, RVol 1.8) |
| 25 | **COIN** | 134.93 | - | **-** | 9 | - | NEG -$27.6M | 136.9 | 142 | 135 | -$2.8M | - | out (clean 31, ADX 20, RVol 0.6) |
| 26 | **BABA** | 108.89 | - | **-** | 7 | - | POS +$24.9M | 106.14 | 110 | 110 | -$352k | - | out (clean 32, ADX 16, RVol 1.1) |
| 27 | **IWM** | 274.17 | - | **-** | 5 | - | NEG -$3.2B | 284.54 | 275 | 275 | -$5.3M | - | out (clean 33, ADX 14, RVol 0.6) |

## Big prints this scan (67)
- **QQQ** CALL 675 2026-11-13 (7DTE): 2,627 @ 4.53 = **+$1.2M** BUY | vol 11,539 / OI 171
- **MSTR** CALL 133 2026-11-13 (7DTE): 2,500 @ 4.22 = **+$1.1M** BUY | vol 40,825 / OI 95
- **TSLA** CALL 362.5 2026-11-13 (7DTE): 500 @ 12.00 = **+$600k** BUY | vol 8,398 / OI 14
- **TSLA** CALL 362.5 2026-11-13 (7DTE): 500 @ 12.00 = **+$600k** BUY | vol 8,398 / OI 14
- **TSLA** CALL 362.5 2026-11-13 (7DTE): 499 @ 11.90 = **+$594k** BUY | vol 8,398 / OI 14
- **TSLA** CALL 362.5 2026-11-13 (7DTE): 265 @ 11.90 = **+$315k** BUY | vol 8,398 / OI 14
- **TSLA** CALL 362.5 2026-11-13 (7DTE): 250 @ 11.85 = **+$296k** BUY | vol 8,398 / OI 14
- **SMH** CALL 445 2026-11-13 (7DTE): 100 @ 28.41 = **+$284k** MID | vol 105 / OI 12
- **GOOGL** PUT 290 2026-11-06 (0DTE): 500 @ 4.43 = **+$222k** BUY | vol 3,934 / OI 4,433
- **GOOGL** PUT 290 2026-11-06 (0DTE): 500 @ 4.37 = **+$218k** BUY | vol 3,934 / OI 4,433
- **GOOGL** PUT 290 2026-11-06 (0DTE): 500 @ 4.35 = **+$218k** BUY | vol 3,934 / OI 4,433
- **QQQ** CALL 675 2026-11-13 (7DTE): 424 @ 4.68 = **+$198k** BUY | vol 11,539 / OI 171
- **TSLA** CALL 362.5 2026-11-13 (7DTE): 144 @ 11.90 = **+$171k** BUY | vol 8,398 / OI 14
- **QQQ** PUT 659 2026-11-06 (0DTE): 990 @ 1.39 = **+$138k** BUY | vol 172,814 / OI 192
- **GOOGL** PUT 290 2026-11-06 (0DTE): 297 @ 4.49 = **+$133k** BUY | vol 3,934 / OI 4,433

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 706 2026-11-11 (5DTE): 505 traded vs OI 102
- **SPY** PUT 751 2026-11-06 (0DTE): 2,900 traded vs OI 2,898
- **SPY** PUT 724 2026-11-10 (4DTE): 539 traded vs OI 165
- **SPY** CALL 761 2026-11-11 (5DTE): 500 traded vs OI 36
- **SPY** PUT 722 2026-11-11 (5DTE): 507 traded vs OI 95
- **QQQ** CALL 673 2026-11-10 (4DTE): 527 traded vs OI 0
- **QQQ** PUT 615 2026-11-10 (4DTE): 530 traded vs OI 204
- **QQQ** CALL 698 2026-11-09 (3DTE): 583 traded vs OI 183
- **QQQ** PUT 611 2026-11-13 (7DTE): 534 traded vs OI 0
- **QQQ** PUT 654 2026-11-13 (7DTE): 506 traded vs OI 42
- **NVDA** CALL 205 2026-11-16 (10DTE): 1,198 traded vs OI 1,195
- **META** PUT 610 2026-11-11 (5DTE): 502 traded vs OI 123
- **AMZN** PUT 242.5 2026-11-11 (5DTE): 1,843 traded vs OI 109
- **GOOGL** CALL 287.5 2026-11-13 (7DTE): 501 traded vs OI 335
- **AVGO** CALL 307.5 2026-11-09 (3DTE): 508 traded vs OI 3

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
