# GEX + FLOW SCAN - Fri Nov 06, 03:00 PM ET
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
Last 1m check 15:00:08 ET, last candle SPY 14:59, QQQ 14:59 | no errors
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
| 1 | **NFLX** | 63.63 | FLIP CROSS down into negative gamma | **PUTS** | 27 | 11/06 64P @ 0.40 (delta 0.89) = est +43% at 63.41 | NEG -$4.2M | 63.76 | 64 | 64 | +$131k | +$332k bull / +$0 bear | out (clean 32, ADX 16, RVol 0.5) |
| 2 | **ORCL** | 115.34 | - | **-** | 20 | - | NEG -$86.3M | - | 116 | 115 | -$5.8M | +$0 bull / -$56k bear | out (clean 30, ADX 13, RVol 0.3) |
| 3 | **SMH** | 465.46 | - | **-** | 18 | - | NEG -$655.1M | - | 505 | 465 | +$7.2M | +$0 bull / -$173k bear | out (clean 32, ADX 18, RVol 0.6) |
| 4 | **TSLA** | 361.04 | - | **-** | 18 | - | NEG -$331.0M | - | 360 | 360 | -$59.0M | +$0 bull / -$479k bear | out (clean 34, ADX 24, RVol 0.2) |
| 5 | **COIN** | 134.80 | - | **-** | 17 | - | NEG -$24.6M | 136.93 | 143 | 135 | -$2.9M | +$0 bull / -$419k bear | out (clean 31, ADX 13, RVol 0.2) |
| 6 | **AAPL** | 343.28 | - | **-** | 16 | - | NEG -$53.2M | 344.05 | 345 | 345 | -$15.7M | +$43k bull / +$0 bear | out (clean 27, ADX 10, RVol 0.2) |
| 7 | **AMD** | 448.16 | - | **-** | 16 | - | NEG -$193.3M | - | 430 | 450 | +$2.1M | +$58k bull / -$252k bear | out (clean 32, ADX 24, RVol 0.6) |
| 8 | **MSFT** | 532.50 | - | **-** | 16 | - | POS +$573.9M | 514.91 | 535 | 535 | +$3.9M | +$25k bull / +$0 bear | out (clean 33, ADX 17, RVol 0.2) |
| 9 | **GOOGL** | 285.43 | PINNED between the walls (positive gamma) - chop | **-** | 16 | - | POS +$59.2M | 284.14 | 285 | 285 | +$2.8M | - | out (clean 33, ADX 14, RVol 0.2) |
| 10 | **MU** | 693.55 | - | **-** | 16 | - | NEG -$193.2M | - | 700 | 700 | +$73.8M | +$271k bull / -$1.6M bear | out (clean 31, ADX 11, RVol 0.4) |
| 11 | **HOOD** | 80.46 | - | **-** | 16 | - | NEG -$30.8M | 83.48 | 85 | 80 | +$1.9M | +$0 bull / -$84k bear | out (clean 30, ADX 15, RVol 0.7) |
| 12 | **IWM** | 274.15 | - | **-** | 15 | - | NEG -$3.2B | 284.95 | 275 | 275 | -$5.1M | +$0 bull / -$420k bear | out (clean 33, ADX 12, RVol 0.7) |
| 13 | **NVDA** | 188.44 | - | **-** | 15 | - | NEG -$416.1M | - | 200 | 190 | +$20.5M | +$0 bull / -$614k bear | out (clean 32, ADX 12, RVol 0.5) |
| 14 | **META** | 615.53 | - | **-** | 15 | - | NEG -$155.1M | 622.61 | 615 | 610 | -$1.5M | +$762k bull / +$0 bear | out (clean 32, ADX 22, RVol 0.3) |
| 15 | **AVGO** | 292.93 | - | **-** | 15 | - | NEG -$139.8M | - | 320 | 300 | +$2.4M | +$0 bull / -$261k bear | out (clean 30, ADX 12, RVol 0.8) |
| 16 | **PLTR** | 161.34 | - | **-** | 15 | - | NEG -$74.0M | 169.98 | 165 | 160 | +$2.5M | +$0 bull / -$271k bear | out (clean 28, ADX 15, RVol 0.4) |
| 17 | **SHOP** | 148.74 | - | **-** | 15 | - | NEG -$2.2M | 149.63 | 150 | 150 | -$1.0M | - | out (clean 35, ADX 26, RVol 0.5) |
| 18 | **SPY** | 738.03 | - | **-** | 14 | - | NEG -$15.4B | 767.6 | 760 | 740 | -$29.3M | +$118k bull / +$0 bear | out (clean 33, ADX 12, RVol 0.5) |
| 19 | **QQQ** | 659.27 | - | **-** | 14 | - | NEG -$6.2B | - | 700 | 660 | +$36.7M | +$124k bull / -$779k bear | out (clean 33, ADX 13, RVol 0.5) |
| 20 | **UBER** | 68.39 | - | **-** | 14 | - | POS +$731k | 68.35 | 70 | 65 | +$297k | - | out (clean 31, ADX 40, RVol 0.4) |
| 21 | **SMCI** | 28.71 | - | **-** | 12 | - | NEG -$5.5M | - | 30 | 29 | -$1.8M | - | out (clean 33, ADX 19, RVol 0.4) |
| 22 | **ARM** | 174.19 | - | **-** | 10 | - | NEG -$24.9M | - | 190 | 170 | -$770k | - | out (clean 25, ADX 22, RVol 0.4) |
| 23 | **DELL** | 331.63 | - | **-** | 9 | - | NEG -$31.8M | - | 335 | 335 | +$5.6M | - | out (clean 31, ADX 12, RVol 0.5) |
| 24 | **CRM** | 213.88 | - | **-** | 8 | - | NEG -$23.9M | - | 230 | 215 | -$128k | - | out (clean 34, ADX 27, RVol 0.9) |
| 25 | **MSTR** | 128.80 | - | **-** | 7 | - | NEG -$4.9M | 129.06 | 135 | 130 | -$3.7M | - | out (clean 30, ADX 21, RVol 0.2) |
| 26 | **BABA** | 109.28 | - | **-** | 7 | - | POS +$37.0M | - | 110 | 110 | -$401k | - | out (clean 32, ADX 17, RVol 0.9) |
| 27 | **AMZN** | 261.57 | - | **-** | 4 | - | POS +$303.3M | - | 260 | 260 | -$513k | - | out (clean 36, ADX 18, RVol 0.2) |

## Big prints this scan (47)
- **IWM** PUT 265 2026-11-13 (7DTE): 3,472 @ 1.21 = **+$420k** BUY | vol 8,247 / OI 11,111
- **MU** PUT 690 2026-11-11 (5DTE): 53 @ 30.95 = **+$164k** BUY | vol 940 / OI 26
- **MU** PUT 690 2026-11-11 (5DTE): 53 @ 30.95 = **+$164k** BUY | vol 940 / OI 26
- **MU** PUT 690 2026-11-11 (5DTE): 53 @ 30.95 = **+$164k** BUY | vol 940 / OI 26
- **MU** PUT 690 2026-11-11 (5DTE): 53 @ 30.95 = **+$164k** BUY | vol 940 / OI 26
- **MU** PUT 690 2026-11-11 (5DTE): 38 @ 30.95 = **+$118k** BUY | vol 940 / OI 26
- **TSLA** CALL 362.5 2026-11-09 (3DTE): 172 @ 5.55 = **+$95k** SELL | vol 5,621 / OI 8
- **META** PUT 617.5 2026-11-13 (7DTE): 50 @ 15.85 = **+$79k** SELL | vol 280 / OI 113
- **META** PUT 617.5 2026-11-13 (7DTE): 47 @ 15.85 = **+$74k** SELL | vol 280 / OI 113
- **MU** CALL 690 2026-11-09 (3DTE): 30 @ 21.39 = **+$64k** SELL | vol 2,197 / OI 0
- **MU** PUT 690 2026-11-09 (3DTE): 27 @ 20.69 = **+$56k** BUY | vol 5,502 / OI 32
- **TSLA** CALL 350 2026-11-06 (0DTE): 50 @ 10.63 = **+$53k** SELL | vol 19,444 / OI 1,342
- **META** PUT 625 2026-11-09 (3DTE): 36 @ 13.09 = **+$47k** SELL | vol 2,982 / OI 106
- **META** PUT 625 2026-11-09 (3DTE): 35 @ 13.04 = **+$46k** SELL | vol 2,982 / OI 106
- **MU** PUT 707.5 2026-11-13 (7DTE): 10 @ 45.45 = **+$45k** MID | vol 151 / OI 0

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 796 2026-11-17 (11DTE): 588 traded vs OI 0
- **SPY** PUT 755 2026-11-27 (21DTE): 2,949 traded vs OI 2,183
- **SPY** CALL 733 2026-11-20 (14DTE): 4,108 traded vs OI 174
- **QQQ** CALL 725 2026-11-10 (4DTE): 1,847 traded vs OI 0
- **QQQ** PUT 628 2026-11-10 (4DTE): 543 traded vs OI 0
- **QQQ** PUT 604 2026-11-09 (3DTE): 526 traded vs OI 0
- **QQQ** CALL 674 2026-11-13 (7DTE): 525 traded vs OI 0
- **QQQ** CALL 684 2026-11-12 (6DTE): 507 traded vs OI 244
- **QQQ** CALL 725 2026-11-12 (6DTE): 801 traded vs OI 0
- **QQQ** CALL 710 2026-11-27 (21DTE): 725 traded vs OI 696
- **QQQ** PUT 659 2026-11-20 (14DTE): 517 traded vs OI 0
- **TSLA** CALL 340 2026-11-09 (3DTE): 504 traded vs OI 15
- **AMD** CALL 492.5 2026-11-06 (0DTE): 764 traded vs OI 0
- **AMD** PUT 425 2026-11-09 (3DTE): 512 traded vs OI 79
- **META** CALL 637.5 2026-11-09 (3DTE): 797 traded vs OI 87

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
