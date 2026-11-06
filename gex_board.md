# GEX + FLOW SCAN - Fri Nov 06, 02:50 PM ET
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
Last 1m check 14:50:08 ET, last candle SPY 14:49, QQQ 14:49 | no errors
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
| 1 | **GOOGL** | 285.62 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 20 | none: 92 puts 0-7DTE > 8 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only -71% at the target (needs +20%) (34 contracts' greeks worked out here) | POS +$60.3M | 284.18 | 285 | 290 | +$2.7M | - | out (clean 33, ADX 12, RVol 0.1) |
| 2 | **ORCL** | 115.04 | - | **-** | 20 | - | NEG -$88.8M | - | 116 | 115 | -$5.6M | +$69k bull / -$31k bear | out (clean 30, ADX 15, RVol 0.3) |
| 3 | **DELL** | 329.41 | - | **-** | 19 | - | NEG -$27.8M | - | 330 | 335 | +$5.8M | +$0 bull / -$370k bear | out (clean 31, ADX 11, RVol 0.4) |
| 4 | **ARM** | 173.73 | - | **-** | 19 | - | NEG -$23.8M | - | 190 | 170 | -$727k | +$27k bull / +$0 bear | out (clean 25, ADX 21, RVol 0.3) |
| 5 | **SMH** | 464.03 | - | **-** | 18 | - | NEG -$647.7M | - | 505 | 465 | +$7.3M | +$104k bull / -$85k bear | out (clean 32, ADX 17, RVol 0.4) |
| 6 | **TSLA** | 360.19 | - | **-** | 18 | - | NEG -$335.3M | - | 360 | 360 | -$58.3M | +$357k bull / -$964k bear | out (clean 34, ADX 24, RVol 0.2) |
| 7 | **COIN** | 133.83 | - | **-** | 17 | - | NEG -$26.4M | 136.83 | 143 | 135 | -$2.4M | +$55k bull / +$0 bear | out (clean 31, ADX 13, RVol 0.2) |
| 8 | **AAPL** | 343.71 | - | **-** | 16 | - | NEG -$82.8M | 344.34 | 345 | 345 | -$16.2M | +$124k bull / +$0 bear | out (clean 27, ADX 8, RVol 0.2) |
| 9 | **AMD** | 445.61 | - | **-** | 16 | - | NEG -$186.7M | - | 430 | 450 | +$4.5M | +$563k bull / -$350k bear | out (clean 32, ADX 23, RVol 0.5) |
| 10 | **MU** | 691.28 | - | **-** | 16 | - | NEG -$169.6M | - | 700 | 700 | +$75.9M | +$492k bull / -$403k bear | out (clean 31, ADX 12, RVol 0.4) |
| 11 | **MSTR** | 127.99 | - | **-** | 16 | - | NEG -$2.4M | 128.16 | 135 | 125 | -$3.7M | +$0 bull / -$1.5M bear | out (clean 30, ADX 19, RVol 0.2) |
| 12 | **MSFT** | 532.20 | - | **-** | 15 | - | POS +$720.4M | 512.33 | 530 | 535 | +$3.4M | +$307k bull / -$53k bear | out (clean 33, ADX 15, RVol 0.2) |
| 13 | **AVGO** | 292.46 | - | **-** | 15 | - | NEG -$134.4M | - | 320 | 300 | +$2.5M | +$0 bull / -$561k bear | out (clean 31, ADX 13, RVol 0.7) |
| 14 | **PLTR** | 161.06 | - | **-** | 15 | - | NEG -$71.2M | - | 165 | 160 | +$2.6M | +$53k bull / -$178k bear | out (clean 27, ADX 12, RVol 0.3) |
| 15 | **HOOD** | 79.81 | - | **-** | 15 | - | NEG -$33.3M | 82 | 80 | 80 | +$2.2M | +$0 bull / -$58k bear | out (clean 30, ADX 12, RVol 0.6) |
| 16 | **SHOP** | 148.67 | - | **-** | 15 | - | NEG -$1.7M | 149.43 | 150 | 150 | -$1.1M | - | out (clean 35, ADX 24, RVol 0.5) |
| 17 | **QQQ** | 658.57 | - | **-** | 14 | - | NEG -$5.3B | - | 700 | 660 | +$42.5M | +$1.0M bull / -$1.2M bear | out (clean 33, ADX 13, RVol 0.5) |
| 18 | **NVDA** | 187.80 | - | **-** | 14 | - | NEG -$389.2M | - | 200 | 190 | +$23.5M | +$203k bull / -$677k bear | out (clean 32, ADX 10, RVol 0.4) |
| 19 | **META** | 615.23 | - | **-** | 14 | - | NEG -$168.8M | 621.75 | 615 | 610 | -$3.0M | +$352k bull / +$0 bear | out (clean 32, ADX 19, RVol 0.2) |
| 20 | **SPY** | 737.87 | - | **-** | 13 | - | NEG -$15.7B | 767 | 760 | 740 | -$27.7M | +$118k bull / +$0 bear | out (clean 33, ADX 12, RVol 0.4) |
| 21 | **NFLX** | 63.68 | - | **-** | 13 | - | POS +$17.5M | 62.82 | 64 | 64 | +$35k | +$276k bull / +$0 bear | out (clean 32, ADX 13, RVol 0.3) |
| 22 | **UBER** | 68.58 | - | **-** | 13 | - | POS +$1.2M | 68.51 | 70 | 65 | +$292k | - | out (clean 31, ADX 37, RVol 0.3) |
| 23 | **CRM** | 214.09 | - | **-** | 8 | - | NEG -$24.2M | - | 230 | 215 | -$156k | - | out (clean 34, ADX 25, RVol 0.9) |
| 24 | **BABA** | 109.40 | - | **-** | 7 | - | POS +$33.9M | - | 110 | 110 | -$413k | - | out (clean 32, ADX 18, RVol 0.9) |
| 25 | **SMCI** | 28.53 | - | **-** | 6 | - | NEG -$5.1M | - | 30 | 29 | -$464k | - | out (clean 33, ADX 16, RVol 0.4) |
| 26 | **IWM** | 273.97 | - | **-** | 4 | - | NEG -$3.4B | 285.09 | 275 | 275 | -$4.4M | - | out (clean 33, ADX 12, RVol 0.5) |
| 27 | **AMZN** | 261.86 | - | **-** | 4 | - | POS +$283.0M | - | 265 | 260 | -$978k | - | out (clean 36, ADX 17, RVol 0.2) |

## Big prints this scan (36)
- **QQQ** PUT 658 2026-11-06 (0DTE): 1,200 @ 1.54 = **+$185k** BUY | vol 181,935 / OI 466
- **QQQ** PUT 658 2026-11-09 (3DTE): 279 @ 6.22 = **+$174k** BUY | vol 12,491 / OI 30
- **QQQ** CALL 640 2026-11-06 (0DTE): 90 @ 18.05 = **+$162k** SELL | vol 863 / OI 75
- **NFLX** CALL 63 2026-11-06 (0DTE): 1,682 @ 0.88 = **+$148k** BUY | vol 6,026 / OI 14,233
- **AVGO** CALL 302.5 2026-11-13 (7DTE): 216 @ 6.30 = **+$136k** SELL | vol 841 / OI 2
- **NFLX** CALL 65 2026-11-13 (7DTE): 1,682 @ 0.76 = **+$128k** BUY | vol 7,146 / OI 5,189
- **SPY** PUT 750 2026-11-09 (3DTE): 100 @ 12.70 = **+$127k** MID | vol 1,274 / OI 5,150
- **QQQ** PUT 658 2026-11-09 (3DTE): 191 @ 6.25 = **+$119k** BUY | vol 12,491 / OI 30
- **NVDA** CALL 182.5 2026-11-06 (0DTE): 256 @ 4.60 = **+$118k** SELL | vol 2,834 / OI 135
- **SPY** PUT 749 2026-11-09 (3DTE): 100 @ 11.75 = **+$118k** SELL | vol 483 / OI 223
- **TSLA** PUT 360 2026-11-09 (3DTE): 143 @ 6.50 = **+$93k** BUY | vol 10,373 / OI 451
- **NVDA** PUT 190 2026-11-06 (0DTE): 300 @ 3.01 = **+$90k** BUY | vol 127,270 / OI 17,283
- **NVDA** CALL 187.5 2026-11-09 (3DTE): 256 @ 3.21 = **+$82k** SELL | vol 8,509 / OI 281
- **MU** PUT 695 2026-11-06 (0DTE): 100 @ 7.60 = **+$76k** BUY | vol 22,329 / OI 0
- **MU** PUT 705 2026-11-09 (3DTE): 25 @ 28.70 = **+$72k** BUY | vol 493 / OI 0

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 690 2026-11-11 (5DTE): 500 traded vs OI 149
- **SPY** CALL 768 2026-11-11 (5DTE): 513 traded vs OI 282
- **SPY** CALL 782 2026-11-12 (6DTE): 706 traded vs OI 286
- **SPY** PUT 721 2026-11-11 (5DTE): 507 traded vs OI 32
- **SPY** PUT 740 2026-11-19 (13DTE): 692 traded vs OI 0
- **QQQ** PUT 613 2026-11-09 (3DTE): 518 traded vs OI 0
- **QQQ** CALL 718 2026-11-10 (4DTE): 540 traded vs OI 188
- **QQQ** CALL 686 2026-11-13 (7DTE): 505 traded vs OI 260
- **QQQ** PUT 660 2026-11-19 (13DTE): 501 traded vs OI 0
- **IWM** PUT 255 2026-11-09 (3DTE): 503 traded vs OI 3
- **TSLA** CALL 387.5 2026-11-11 (5DTE): 515 traded vs OI 0
- **META** PUT 625 2026-11-06 (0DTE): 3,407 traded vs OI 3,353
- **AVGO** CALL 302.5 2026-11-13 (7DTE): 841 traded vs OI 2
- **SMCI** PUT 28 2026-11-13 (7DTE): 912 traded vs OI 908
- **MU** CALL 717.5 2026-11-09 (3DTE): 513 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
