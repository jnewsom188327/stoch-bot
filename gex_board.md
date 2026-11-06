# GEX + FLOW SCAN - Fri Nov 06, 02:40 PM ET
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
Last 1m check 14:40:08 ET, last candle SPY 14:39, QQQ 14:39 | no errors
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
| 1 | **ARM** | 173.54 | - | **-** | 19 | - | NEG -$24.7M | - | 190 | 170 | -$728k | +$27k bull / +$0 bear | out (clean 26, ADX 21, RVol 0.3) |
| 2 | **TSLA** | 360.25 | - | **-** | 18 | - | NEG -$333.0M | - | 360 | 360 | -$58.6M | +$143k bull / -$954k bear | out (clean 34, ADX 23, RVol 0.2) |
| 3 | **SMH** | 463.20 | - | **-** | 17 | - | NEG -$560.1M | - | 505 | 465 | +$6.7M | +$34k bull / +$0 bear | out (clean 32, ADX 17, RVol 0.4) |
| 4 | **COIN** | 133.67 | - | **-** | 17 | - | NEG -$23.8M | 136.68 | 142 | 135 | -$2.3M | +$935k bull / +$0 bear | out (clean 31, ADX 15, RVol 0.3) |
| 5 | **AAPL** | 344.20 | - | **-** | 16 | - | NEG -$7.6M | 344.26 | 345 | 345 | -$16.7M | +$155k bull / +$0 bear | out (clean 27, ADX 7, RVol 0.2) |
| 6 | **AMD** | 444.13 | - | **-** | 16 | - | NEG -$183.2M | - | 430 | 450 | +$5.3M | +$957k bull / -$162k bear | out (clean 32, ADX 23, RVol 0.5) |
| 7 | **MU** | 690.03 | - | **-** | 16 | - | NEG -$159.0M | - | 700 | 700 | +$76.1M | +$828k bull / -$27k bear | out (clean 31, ADX 12, RVol 0.3) |
| 8 | **MSTR** | 127.67 | - | **-** | 16 | - | NEG -$4.3M | 127.91 | 135 | 125 | -$3.6M | +$1.5M bull / -$1.4M bear | out (clean 30, ADX 18, RVol 0.2) |
| 9 | **META** | 616.24 | - | **-** | 15 | - | NEG -$128.9M | 623.12 | 620 | 610 | -$5.0M | +$436k bull / +$0 bear | out (clean 32, ADX 18, RVol 0.2) |
| 10 | **MSFT** | 533.13 | - | **-** | 15 | - | POS +$677.9M | 513.09 | 535 | 535 | +$2.8M | +$154k bull / -$53k bear | out (clean 34, ADX 14, RVol 0.2) |
| 11 | **AVGO** | 291.70 | - | **-** | 15 | - | NEG -$137.2M | - | 320 | 300 | +$3.2M | +$496k bull / +$0 bear | out (clean 31, ADX 14, RVol 0.7) |
| 12 | **PLTR** | 160.69 | - | **-** | 15 | - | NEG -$70.5M | 167.88 | 165 | 160 | +$3.2M | +$0 bull / -$54k bear | out (clean 27, ADX 10, RVol 0.3) |
| 13 | **HOOD** | 79.64 | - | **-** | 15 | - | NEG -$30.4M | 82.55 | 85 | 80 | +$2.2M | +$27k bull / +$0 bear | out (clean 30, ADX 13, RVol 0.5) |
| 14 | **SHOP** | 148.82 | - | **-** | 15 | - | NEG -$2.3M | 150.19 | 150 | 150 | -$1.1M | - | out (clean 35, ADX 23, RVol 0.5) |
| 15 | **SPY** | 737.72 | - | **-** | 14 | - | NEG -$15.4B | 767.71 | 760 | 740 | -$25.0M | +$1.3M bull / +$0 bear | out (clean 33, ADX 14, RVol 0.5) |
| 16 | **QQQ** | 658.33 | - | **-** | 14 | - | NEG -$5.1B | - | 700 | 660 | +$43.9M | +$1.4M bull / -$608k bear | out (clean 33, ADX 14, RVol 0.5) |
| 17 | **NVDA** | 187.26 | - | **-** | 14 | - | NEG -$393.1M | - | 200 | 190 | +$23.8M | +$289k bull / -$345k bear | out (clean 32, ADX 10, RVol 0.5) |
| 18 | **AMZN** | 261.89 | - | **-** | 14 | - | POS +$373.5M | - | 260 | 260 | -$1.0M | +$120k bull / +$0 bear | out (clean 35, ADX 17, RVol 0.2) |
| 19 | **GOOGL** | 285.84 | - | **-** | 14 | - | POS +$91.1M | 282.42 | 285 | 285 | +$2.7M | +$993k bull / +$0 bear | out (clean 33, ADX 12, RVol 0.2) |
| 20 | **UBER** | 68.68 | - | **-** | 13 | - | POS +$5.5M | 68.46 | 70 | 65 | +$286k | - | out (clean 30, ADX 35, RVol 0.3) |
| 21 | **DELL** | 327.99 | - | **-** | 10 | - | NEG -$26.8M | - | 330 | 335 | +$6.4M | - | out (clean 31, ADX 12, RVol 0.4) |
| 22 | **ORCL** | 114.68 | - | **-** | 10 | - | NEG -$79.8M | - | 116 | 115 | -$5.5M | - | out (clean 30, ADX 16, RVol 0.3) |
| 23 | **CRM** | 214.37 | - | **-** | 8 | - | NEG -$21.1M | - | 230 | 215 | -$165k | - | out (clean 34, ADX 23, RVol 0.9) |
| 24 | **BABA** | 109.54 | - | **-** | 7 | - | POS +$36.9M | - | 110 | 110 | -$447k | - | out (clean 33, ADX 16, RVol 0.8) |
| 25 | **SMCI** | 28.41 | - | **-** | 5 | - | NEG -$4.1M | 29.53 | 30 | 28 | -$419k | - | out (clean 33, ADX 14, RVol 0.2) |
| 26 | **IWM** | 273.86 | - | **-** | 4 | - | NEG -$3.3B | 285.35 | 275 | 275 | -$4.5M | - | out (clean 33, ADX 13, RVol 0.3) |
| 27 | **NFLX** | 63.77 | - | **-** | 4 | - | POS +$1.4M | 63.75 | 64 | 64 | -$262k | - | out (clean 32, ADX 11, RVol 0.3) |

## Big prints this scan (38)
- **MSTR** CALL 133 2026-11-13 (7DTE): 4,000 @ 3.62 = **+$1.4M** SELL | vol 33,247 / OI 95
- **QQQ** PUT 658 2026-11-06 (0DTE): 2,984 @ 1.45 = **+$433k** BUY | vol 170,423 / OI 466
- **TSLA** PUT 375 2026-11-13 (7DTE): 100 @ 20.40 = **+$204k** BUY | vol 430 / OI 1,316
- **QQQ** PUT 658 2026-11-09 (3DTE): 285 @ 6.16 = **+$176k** BUY | vol 10,963 / OI 30
- **TSLA** PUT 370 2026-11-13 (7DTE): 100 @ 17.25 = **+$172k** BUY | vol 539 / OI 962
- **TSLA** PUT 375 2026-11-06 (0DTE): 100 @ 15.80 = **+$158k** BUY | vol 857 / OI 4,143
- **QQQ** CALL 660 2026-11-06 (0DTE): 1,489 @ 0.90 = **+$134k** BUY | vol 263,628 / OI 330
- **NVDA** PUT 182.5 2026-11-11 (5DTE): 392 @ 3.40 = **+$133k** BUY | vol 2,238 / OI 363
- **NVDA** CALL 185 2026-11-11 (5DTE): 200 @ 6.50 = **+$130k** MID | vol 2,011 / OI 10
- **AMD** CALL 462.5 2026-11-13 (7DTE): 88 @ 14.50 = **+$128k** SELL | vol 4,946 / OI 70
- **QQQ** CALL 654 2026-11-09 (3DTE): 123 @ 9.07 = **+$112k** BUY | vol 1,479 / OI 0
- **AMD** CALL 462.5 2026-11-13 (7DTE): 74 @ 14.65 = **+$108k** BUY | vol 4,946 / OI 70
- **TSLA** PUT 370 2026-11-06 (0DTE): 100 @ 10.80 = **+$108k** BUY | vol 2,333 / OI 4,963
- **AMD** CALL 462.5 2026-11-13 (7DTE): 65 @ 14.65 = **+$95k** BUY | vol 4,946 / OI 70
- **AMD** CALL 462.5 2026-11-13 (7DTE): 61 @ 14.65 = **+$89k** BUY | vol 4,946 / OI 70

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 717 2026-11-10 (4DTE): 626 traded vs OI 233
- **SPY** CALL 751 2026-11-11 (5DTE): 501 traded vs OI 17
- **SPY** CALL 770 2026-11-11 (5DTE): 1,951 traded vs OI 1,931
- **SPY** CALL 765 2026-11-11 (5DTE): 2,981 traded vs OI 1,613
- **QQQ** CALL 722 2026-11-10 (4DTE): 1,865 traded vs OI 145
- **QQQ** PUT 633 2026-11-13 (7DTE): 505 traded vs OI 0
- **IWM** CALL 281 2026-11-09 (3DTE): 1,035 traded vs OI 866
- **IWM** PUT 273 2026-11-20 (14DTE): 4,774 traded vs OI 3,667
- **NVDA** PUT 180 2026-11-16 (10DTE): 1,318 traded vs OI 217
- **AMD** PUT 420 2026-11-11 (5DTE): 530 traded vs OI 60
- **META** CALL 620 2026-11-13 (7DTE): 738 traded vs OI 737
- **NFLX** CALL 65 2026-11-13 (7DTE): 5,401 traded vs OI 5,189
- **SMCI** CALL 27.5 2026-11-13 (7DTE): 506 traded vs OI 32
- **MSTR** CALL 125 2026-11-06 (0DTE): 506 traded vs OI 340

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
