# GEX + FLOW SCAN - Fri Nov 06, 01:30 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (4)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 12:40 | **SPY** | **CALLS** | 1m WHIPSAW (R1) | 11/06 742C | 0.42 | 0.28 | +14% (6m) | **-33%** | +42% | 739.03 |
| 10:30 | **NVDA** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/06 192.5C | 0.73 | 0.28 | +12% (20m) | **-62%** (done) | +199% | 193.9 |
| 10:00 | **NVDA** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/06 197.5C | 0.67 | 0.03 | -6% (1m) | **-96%** (done) | +24% | 195 |
| 09:50 | **NFLX** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/06 64C | 0.40 | 0.36 | +32% (4m) | **-10%** (done) | +164% | 65 |

## 1m RULES on SPY / QQQ - loose (11 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 13:30:08 ET, last candle SPY 13:29, QQQ 13:29 | no errors
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
| 1 | **AAPL** | 344.39 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 33 | none: 112 calls 0-7DTE > 6 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only -13% at the target (needs +20%) (53 contracts' greeks worked out here) | POS +$20.5M | 344.14 | 350 | 345 | -$16.8M | +$143k bull / -$76k bear | out (clean 28, ADX 9, RVol 0.2) |
| 2 | **GOOGL** | 285.52 | PINNED between the walls (positive gamma) - chop | **-** | 29 | - | POS +$84.8M | 282.86 | 285 | 285 | +$2.7M | +$715k bull / +$0 bear | out (clean 33, ADX 18, RVol 0.5) |
| 3 | **ORCL** | 113.69 | - | **-** | 23 | - | NEG -$77.9M | - | 125 | 115 | -$4.4M | +$41k bull / -$293k bear | out (clean 30, ADX 26, RVol 0.9) |
| 4 | **DELL** | 326.13 | - | **-** | 22 | - | NEG -$24.1M | - | 330 | 335 | +$5.9M | +$32k bull / -$26k bear | out (clean 31, ADX 23, RVol 0.5) |
| 5 | **MSTR** | 126.73 | - | **-** | 19 | - | NEG -$18.0M | 128.07 | 135 | 125 | -$7.0M | +$0 bull / -$214k bear | out (clean 31, ADX 19, RVol 0.2) |
| 6 | **TSLA** | 358.99 | - | **-** | 18 | - | NEG -$315.8M | - | 370 | 360 | -$58.3M | +$707k bull / -$248k bear | out (clean 35, ADX 18, RVol 0.5) |
| 7 | **AVGO** | 290.74 | - | **-** | 18 | - | NEG -$119.6M | - | 315 | 300 | +$3.2M | +$110k bull / +$0 bear | out (clean 32, ADX 25, RVol 0.8) |
| 8 | **MU** | 682.75 | - | **-** | 18 | - | NEG -$159.9M | - | 700 | 700 | +$81.4M | +$4.5M bull / -$424k bear | out (clean 32, ADX 17, RVol 0.6) |
| 9 | **NVDA** | 186.35 | - | **-** | 17 | - | NEG -$364.7M | - | 200 | 190 | +$31.6M | +$1.4M bull / -$529k bear | out (clean 33, ADX 21, RVol 0.6) |
| 10 | **META** | 617.74 | - | **-** | 17 | - | NEG -$127.2M | 622.68 | 620 | 610 | -$7.0M | +$599k bull / -$28k bear | out (clean 33, ADX 25, RVol 0.3) |
| 11 | **AMZN** | 262.32 | - | **-** | 17 | - | POS +$345.7M | - | 265 | 260 | -$2.2M | +$0 bull / -$40k bear | out (clean 35, ADX 25, RVol 0.6) |
| 12 | **MSFT** | 533.16 | - | **-** | 17 | - | POS +$629.3M | 514.23 | 535 | 535 | +$4.8M | +$174k bull / +$0 bear | out (clean 34, ADX 16, RVol 0.3) |
| 13 | **SPY** | 737.31 | - | **-** | 16 | - | NEG -$14.9B | 767.5 | 760 | 740 | -$25.5M | +$352k bull / -$3.4M bear | out (clean 34, ADX 25, RVol 0.4) |
| 14 | **QQQ** | 656.80 | - | **-** | 16 | - | NEG -$5.5B | - | 700 | 680 | +$56.2M | +$1.3M bull / -$3.7M bear | out (clean 34, ADX 22, RVol 0.6) |
| 15 | **IWM** | 273.74 | - | **-** | 16 | - | NEG -$3.1B | 285.17 | 285 | 275 | -$6.2M | +$0 bull / -$201k bear | out (clean 33, ADX 13, RVol 0.7) |
| 16 | **AMD** | 438.86 | - | **-** | 16 | - | NEG -$179.5M | - | 430 | 440 | +$11.4M | +$27k bull / -$1.1M bear | out (clean 31, ADX 18, RVol 0.6) |
| 17 | **HOOD** | 79.34 | - | **-** | 16 | - | NEG -$25.4M | 82.09 | 85 | 80 | +$1.9M | +$0 bull / -$63k bear | out (clean 30, ADX 20, RVol 0.3) |
| 18 | **SHOP** | 149.20 | - | **-** | 15 | - | NEG -$1.8M | 150.36 | 150 | 150 | -$1.1M | - | out (clean 37, ADX 19, RVol 0.6) |
| 19 | **UBER** | 69.03 | - | **-** | 12 | - | POS +$9.8M | 68.52 | 70 | 65 | +$270k | - | out (clean 30, ADX 32, RVol 0.3) |
| 20 | **COIN** | 132.90 | - | **-** | 11 | - | NEG -$24.6M | 136.94 | 142 | 130 | -$3.2M | - | out (clean 32, ADX 25, RVol 0.2) |
| 21 | **SMH** | 460.22 | - | **-** | 8 | - | NEG -$494.9M | - | 505 | 465 | +$7.5M | - | out (clean 33, ADX 19, RVol 0.3) |
| 22 | **NFLX** | 63.81 | - | **-** | 7 | - | NEG -$3.8M | 63.89 | 64 | 65 | -$352k | - | out (clean 32, ADX 19, RVol 0.5) |
| 23 | **ARM** | 171.84 | - | **-** | 7 | - | NEG -$28.1M | - | 180 | 170 | -$582k | - | out (clean 26, ADX 11, RVol 0.4) |
| 24 | **CRM** | 215.03 | - | **-** | 7 | - | NEG -$24.2M | - | 230 | 215 | -$230k | - | out (clean 34, ADX 20, RVol 0.8) |
| 25 | **BABA** | 109.19 | - | **-** | 7 | - | POS +$32.4M | - | 110 | 110 | -$481k | - | out (clean 34, ADX 14, RVol 0.4) |
| 26 | **PLTR** | 160.17 | - | **-** | 6 | - | NEG -$80.3M | - | 165 | 160 | +$3.8M | - | out (clean 28, ADX 14, RVol 0.3) |
| 27 | **SMCI** | 28.18 | - | **-** | 6 | - | NEG -$5.1M | - | 30 | 28 | -$373k | - | out (clean 34, ADX 18, RVol 0.3) |

## Big prints this scan (44)
- **QQQ** PUT 685 2026-11-10 (4DTE): 500 @ 29.25 = **+$1.5M** BUY | vol 594 / OI 1,141
- **TSLA** PUT 357.5 2026-11-13 (7DTE): 255 @ 11.00 = **+$280k** SELL | vol 1,341 / OI 737
- **SPY** CALL 750 2026-11-13 (7DTE): 698 @ 3.54 = **+$247k** BUY | vol 10,038 / OI 350
- **MU** CALL 670 2026-11-06 (0DTE): 100 @ 17.25 = **+$172k** BUY | vol 1,891 / OI 0
- **SPY** PUT 730 2026-11-09 (3DTE): 450 @ 2.77 = **+$125k** BUY | vol 36,913 / OI 2,461
- **MSTR** PUT 129 2026-11-13 (7DTE): 160 @ 7.40 = **+$118k** BUY | vol 493 / OI 203
- **QQQ** CALL 656 2026-11-06 (0DTE): 461 @ 2.49 = **+$115k** BUY | vol 36,906 / OI 0
- **AVGO** CALL 290 2026-11-06 (0DTE): 372 @ 2.95 = **+$110k** BUY | vol 1,453 / OI 38
- **SPY** PUT 730 2026-11-09 (3DTE): 367 @ 2.86 = **+$105k** BUY | vol 36,913 / OI 2,461
- **META** PUT 632.5 2026-11-13 (7DTE): 44 @ 23.45 = **+$103k** SELL | vol 76 / OI 60
- **QQQ** CALL 660 2026-11-09 (3DTE): 200 @ 5.15 = **+$103k** BUY | vol 24,963 / OI 10
- **META** PUT 630 2026-11-13 (7DTE): 46 @ 21.90 = **+$101k** SELL | vol 202 / OI 364
- **MSTR** PUT 129 2026-11-13 (7DTE): 129 @ 7.40 = **+$95k** BUY | vol 493 / OI 203
- **NVDA** PUT 192.5 2026-11-09 (3DTE): 134 @ 7.10 = **+$95k** BUY | vol 16,735 / OI 850
- **META** PUT 630 2026-11-13 (7DTE): 43 @ 21.90 = **+$94k** SELL | vol 202 / OI 364

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 762 2026-11-12 (6DTE): 522 traded vs OI 70
- **SPY** CALL 754 2026-11-11 (5DTE): 511 traded vs OI 189
- **SPY** CALL 771 2026-11-13 (7DTE): 2,683 traded vs OI 1,910
- **SPY** CALL 770 2026-11-13 (7DTE): 4,101 traded vs OI 4,087
- **QQQ** CALL 669 2026-11-10 (4DTE): 500 traded vs OI 14
- **QQQ** CALL 672 2026-11-13 (7DTE): 596 traded vs OI 1
- **QQQ** CALL 698 2026-11-13 (7DTE): 552 traded vs OI 434
- **QQQ** CALL 664 2026-11-20 (14DTE): 518 traded vs OI 0
- **NVDA** CALL 182.5 2026-11-13 (7DTE): 546 traded vs OI 4
- **AAPL** CALL 352.5 2026-11-11 (5DTE): 523 traded vs OI 508
- **META** CALL 650 2026-11-11 (5DTE): 556 traded vs OI 167
- **GOOGL** CALL 302.5 2026-11-13 (7DTE): 526 traded vs OI 421
- **AVGO** CALL 305 2026-11-20 (14DTE): 553 traded vs OI 79
- **MU** PUT 620 2026-11-20 (14DTE): 701 traded vs OI 0
- **ORCL** PUT 108 2026-11-13 (7DTE): 503 traded vs OI 339

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
