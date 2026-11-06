# GEX + FLOW SCAN - Fri Nov 06, 01:50 PM ET
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
Last 1m check 13:50:08 ET, last candle SPY 13:49, QQQ 13:49 | no errors
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
| 1 | **MSFT** | 533.76 | PINNED between the walls (positive gamma) - chop | **-** | 28 | - | POS +$687.8M | 511.93 | 535 | 535 | +$3.6M | +$0 bull / -$570k bear | out (clean 34, ADX 17, RVol 0.4) |
| 2 | **ORCL** | 114.97 | - | **-** | 22 | - | NEG -$80.9M | - | 125 | 115 | -$5.2M | +$0 bull / -$148k bear | out (clean 30, ADX 23, RVol 0.5) |
| 3 | **COIN** | 133.87 | - | **-** | 20 | - | NEG -$23.7M | 136.81 | 141 | 135 | -$3.2M | +$0 bull / -$102k bear | out (clean 32, ADX 22, RVol 0.2) |
| 4 | **NFLX** | 63.84 | FLIP CROSS down into negative gamma | **PUTS** | 19 | none: 26 puts 0-7DTE > 1 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only +8% at the target (needs +20%) (19 contracts' greeks worked out here) | NEG -$6.4M | 64.02 | 64 | 64 | -$370k | - | out (clean 32, ADX 16, RVol 0.5) |
| 5 | **MSTR** | 127.51 | - | **-** | 19 | - | NEG -$7.5M | 127.99 | 135 | 125 | -$6.7M | +$0 bull / -$82k bear | out (clean 30, ADX 18, RVol 0.3) |
| 6 | **TSLA** | 359.50 | - | **-** | 18 | - | NEG -$317.2M | - | 360 | 360 | -$58.7M | +$157k bull / -$349k bear | out (clean 35, ADX 20, RVol 0.2) |
| 7 | **SMH** | 462.80 | - | **-** | 17 | - | NEG -$565.4M | - | 505 | 465 | +$6.5M | +$0 bull / -$544k bear | out (clean 32, ADX 16, RVol 0.5) |
| 8 | **AAPL** | 344.38 | - | **-** | 17 | - | NEG -$17.4M | 344.54 | 345 | 345 | -$17.1M | +$32k bull / -$53k bear | out (clean 28, ADX 8, RVol 0.2) |
| 9 | **AVGO** | 292.20 | - | **-** | 17 | - | NEG -$129.4M | - | 320 | 300 | +$1.5M | +$0 bull / -$152k bear | out (clean 31, ADX 23, RVol 1.2) |
| 10 | **MU** | 688.59 | - | **-** | 17 | - | NEG -$162.1M | - | 700 | 700 | +$77.5M | +$141k bull / -$5.1M bear | out (clean 32, ADX 13, RVol 0.5) |
| 11 | **BABA** | 109.31 | - | **-** | 17 | - | POS +$31.4M | - | 110 | 110 | -$547k | +$0 bull / -$27k bear | out (clean 34, ADX 14, RVol 0.4) |
| 12 | **QQQ** | 658.35 | - | **-** | 16 | - | NEG -$5.0B | - | 700 | 660 | +$44.4M | +$216k bull / -$982k bear | out (clean 34, ADX 17, RVol 0.8) |
| 13 | **IWM** | 274.24 | - | **-** | 16 | - | NEG -$3.4B | 285.36 | 275 | 275 | -$6.0M | +$0 bull / -$87k bear | out (clean 33, ADX 17, RVol 0.3) |
| 14 | **NVDA** | 187.40 | - | **-** | 16 | - | NEG -$365.1M | - | 200 | 190 | +$23.0M | +$0 bull / -$5.4M bear | out (clean 33, ADX 16, RVol 0.5) |
| 15 | **META** | 617.97 | - | **-** | 16 | - | NEG -$116.9M | 623.05 | 620 | 610 | -$7.4M | +$83k bull / -$69k bear | out (clean 33, ADX 22, RVol 0.2) |
| 16 | **AMZN** | 262.58 | - | **-** | 16 | - | POS +$390.9M | - | 265 | 260 | -$2.3M | +$0 bull / -$131k bear | out (clean 35, ADX 22, RVol 0.6) |
| 17 | **PLTR** | 160.23 | - | **-** | 16 | - | NEG -$77.3M | - | 165 | 160 | +$3.7M | +$0 bull / -$472k bear | out (clean 27, ADX 12, RVol 0.4) |
| 18 | **HOOD** | 79.91 | - | **-** | 16 | - | NEG -$29.0M | 83.88 | 85 | 80 | +$2.4M | +$452k bull / -$114k bear | out (clean 30, ADX 18, RVol 0.3) |
| 19 | **SPY** | 738.46 | - | **-** | 15 | - | NEG -$14.8B | 768.14 | 770 | 740 | -$43.3M | +$0 bull / -$3.6M bear | out (clean 34, ADX 20, RVol 0.6) |
| 20 | **AMD** | 442.06 | - | **-** | 15 | - | NEG -$162.5M | - | 430 | 440 | +$8.3M | +$0 bull / -$944k bear | out (clean 31, ADX 16, RVol 0.6) |
| 21 | **SHOP** | 149.38 | - | **-** | 15 | - | NEG -$2.9M | 150.97 | 150 | 150 | -$1.1M | - | out (clean 36, ADX 18, RVol 0.6) |
| 22 | **UBER** | 69.17 | - | **-** | 12 | - | POS +$10.7M | 68.63 | 70 | 70 | +$266k | - | out (clean 30, ADX 31, RVol 0.3) |
| 23 | **DELL** | 329.67 | - | **-** | 11 | - | NEG -$28.1M | - | 335 | 335 | +$5.7M | - | out (clean 30, ADX 17, RVol 0.3) |
| 24 | **CRM** | 214.72 | - | **-** | 8 | - | NEG -$26.2M | - | 230 | 215 | -$210k | - | out (clean 34, ADX 21, RVol 1.0) |
| 25 | **ARM** | 172.82 | - | **-** | 7 | - | NEG -$27.2M | - | 190 | 170 | -$593k | - | out (clean 26, ADX 13, RVol 0.3) |
| 26 | **SMCI** | 28.39 | - | **-** | 6 | - | NEG -$5.3M | - | 30 | 29 | -$450k | - | out (clean 34, ADX 17, RVol 0.3) |
| 27 | **GOOGL** | 286.29 | - | **-** | 5 | - | POS +$67.5M | 282.69 | 285 | 290 | +$1.6M | - | out (clean 33, ADX 15, RVol 0.4) |

## Big prints this scan (78)
- **NVDA** CALL 190 2026-11-13 (7DTE): 6,010 @ 4.73 = **+$2.8M** SELL | vol 14,842 / OI 711
- **NVDA** CALL 195 2026-11-13 (7DTE): 5,990 @ 2.83 = **+$1.7M** SELL | vol 27,120 / OI 582
- **SPY** PUT 725 2026-11-12 (6DTE): 2,000 @ 4.50 = **+$900k** BUY | vol 2,767 / OI 476
- **SPY** PUT 735 2026-11-12 (6DTE): 1,000 @ 7.42 = **+$742k** BUY | vol 1,935 / OI 1,057
- **MU** PUT 720 2026-11-13 (7DTE): 100 @ 57.85 = **+$578k** BUY | vol 284 / OI 1,201
- **MU** PUT 720 2026-11-06 (0DTE): 100 @ 37.55 = **+$376k** BUY | vol 3,261 / OI 857
- **SPY** PUT 760 2026-11-10 (4DTE): 146 @ 22.40 = **+$327k** BUY | vol 403 / OI 3,594
- **SPY** PUT 715 2026-11-12 (6DTE): 1,000 @ 2.83 = **+$283k** BUY | vol 2,945 / OI 3,594
- **SPY** PUT 753 2026-11-06 (0DTE): 155 @ 15.71 = **+$244k** BUY | vol 1,535 / OI 3,679
- **SPY** PUT 751 2026-11-06 (0DTE): 155 @ 13.75 = **+$213k** BUY | vol 2,541 / OI 2,898
- **SPY** CALL 745 2026-11-13 (7DTE): 354 @ 5.41 = **+$192k** SELL | vol 6,499 / OI 168
- **MU** CALL 670 2026-11-06 (0DTE): 100 @ 19.00 = **+$190k** SELL | vol 2,508 / OI 0
- **HOOD** CALL 82 2026-11-13 (7DTE): 764 @ 2.44 = **+$186k** BUY | vol 7,045 / OI 386
- **MSFT** PUT 532.5 2026-11-13 (7DTE): 200 @ 9.15 = **+$183k** BUY | vol 521 / OI 224
- **MSFT** PUT 532.5 2026-11-13 (7DTE): 200 @ 9.15 = **+$183k** BUY | vol 521 / OI 224

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 764 2026-11-11 (5DTE): 566 traded vs OI 263
- **SPY** CALL 751 2026-11-13 (7DTE): 515 traded vs OI 272
- **SPY** CALL 756 2026-11-13 (7DTE): 1,017 traded vs OI 1,014
- **SPY** CALL 744 2026-11-20 (14DTE): 522 traded vs OI 412
- **QQQ** PUT 620 2026-11-11 (5DTE): 513 traded vs OI 195
- **QQQ** PUT 669 2026-11-09 (3DTE): 549 traded vs OI 138
- **QQQ** PUT 654 2026-11-10 (4DTE): 501 traded vs OI 57
- **QQQ** PUT 640 2026-11-13 (7DTE): 2,467 traded vs OI 2,420
- **QQQ** CALL 681 2026-11-13 (7DTE): 504 traded vs OI 42
- **QQQ** CALL 673 2026-11-13 (7DTE): 504 traded vs OI 1
- **QQQ** CALL 669 2026-11-13 (7DTE): 556 traded vs OI 3
- **QQQ** CALL 660 2026-11-12 (6DTE): 512 traded vs OI 13
- **QQQ** PUT 605 2026-11-13 (7DTE): 4,934 traded vs OI 3,765
- **QQQ** CALL 685 2026-11-20 (14DTE): 2,732 traded vs OI 2,694
- **IWM** PUT 267 2026-11-09 (3DTE): 608 traded vs OI 564

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
