# GEX + FLOW SCAN - Thu Nov 05, 10:55 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (4)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:55 | **BABA** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/06 102P | 0.75 | 0.63 | -16% (0m) | **-16%** | +27% | 103.58 |
| 09:52 | **SPY** | **PUTS** | 1m WHIPSAW (R1) | 11/05 749P | 0.78 | 11.35 | +1355% (60m) | **+1355%** (done) | +47% | 753.11 hit |
| 09:50 | **BABA** | **CALLS** | TREND + FLOW | 11/06 111C | 0.48 | 0.20 | -12% (0m) | **-58%** (done) | +136% | 110 |
| 09:40 | **QQQ** | **CALLS** | 1m WHIPSAW (R1) | 11/05 683C | 0.78 | 0.10 | -4% (0m) | **-87%** (done) | +66% | 678.43 |

## 1m RULES on SPY / QQQ - loose (3 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:55:08 ET, last candle SPY 10:54, QQQ 10:54 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 10:38 | QQQ | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | no contract: 64 puts 0-1DTE > 1 priced 0.40-0.80 > 0 delta 0.15+ > 0 spread ok > 0 liquid  |
| 09:51 | SPY | 1m WHIPSAW | R1 | PUTS | TURNING away | **FIRE** SPY261105P00749000 |
| 09:39 | QQQ | 1m WHIPSAW | R1 | CALLS | AGAINST you | **FIRE** QQQ261105C00683000 |

## Flow surges NOT fired - price disagreed (22 today, last 5)
- 10:55 IWM CALLS: price -2.06 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:50 HOOD CALLS: price -1.37 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:50 IWM CALLS: price -2.31 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:45 IWM CALLS: price -1.06 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:40 ORCL CALLS: price -0.25 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **SMH** | 452.12 | FLOW SURGE | **CALLS** | 68 | none: 83 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (4 contracts' greeks worked out here) | NEG -$196.4M | - | 445 | 465 | +$42.7M | +$18.2M bull / +$0 bear | SHORT (clean 35, ADX 60, RVol 2.7) |
| 2 | **MSTR** | 124.71 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 67 | none: 25 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (9 contracts' greeks worked out here) | POS +$20.9M | - | 135 | 125 | +$4.6M | +$281k bull / +$0 bear | SHORT (clean 34, ADX 69, RVol 2.5) |
| 3 | **QQQ** | 650.73 | FLOW SURGE | **CALLS** | 65 | none: 474 calls 0-7DTE > 50 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (124 contracts' greeks worked out here) | NEG -$4.3B | - | 700 | 680 | +$746.8M | +$20.3M bull / +$0 bear | SHORT (clean 35, ADX 64, RVol 3.2) |
| 4 | **IWM** | 275.38 | FLOW SURGE | **CALLS** | 64 | 11/05 278C @ 0.59 (delta 0.25) = est +48% at 277 | NEG -$2.2B | 286.76 | 285 | 270 | +$41.3M | +$2.3M bull / +$0 bear | SHORT (clean 35, ADX 50, RVol 3.4) |
| 5 | **SPY** | 739.23 | FLOW SURGE | **CALLS** | 63 | none: 655 calls 0-7DTE > 26 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (205 contracts' greeks worked out here) | NEG -$11.5B | 771.21 | 760 | 740 | +$951.0M | +$37.7M bull / +$0 bear | SHORT (clean 35, ADX 66, RVol 2.5) |
| 6 | **AVGO** | 295.58 | FLOW SURGE | **CALLS** | 63 | none: 59 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (3 contracts' greeks worked out here) | NEG -$98.7M | - | 325 | 300 | +$7.9M | +$348k bull / -$79k bear | out (clean 31, ADX 58, RVol 3.6) |
| 7 | **DELL** | 320.50 | FLOW SURGE | **CALLS** | 62 | none: 18 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (12 contracts' greeks worked out here) | NEG -$11.0M | - | 350 | 340 | +$7.1M | +$126k bull / -$116k bear | SHORT (clean 34, ADX 51, RVol 2.0) |
| 8 | **META** | 591.02 | FLOW SURGE | **CALLS** | 61 | none: 135 calls 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (2 contracts' greeks worked out here) | NEG -$165.4M | - | 650 | 600 | +$45.7M | +$9.6M bull / +$0 bear | SHORT (clean 34, ADX 48, RVol 2.4) |
| 9 | **PLTR** | 153.91 | FLOW SURGE | **CALLS** | 59 | none: 15 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (1 contracts' greeks worked out here) | NEG -$38.8M | - | 165 | 150 | +$12.4M | +$238k bull / +$0 bear | out (clean 28, ADX 53, RVol 2.5) |
| 10 | **NVDA** | 183.16 | FLOW SURGE | **CALLS** | 58 | none: 36 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (2 contracts' greeks worked out here) | NEG -$242.9M | - | 200 | 190 | +$61.5M | +$3.8M bull / -$1.5M bear | out (clean 33, ADX 67, RVol 3.5) |
| 11 | **MU** | 671.49 | FLOW SURGE | **CALLS** | 58 | none: 76 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (10 contracts' greeks worked out here) | NEG -$54.1M | - | 700 | 700 | +$167.3M | +$10.5M bull / +$0 bear | out (clean 33, ADX 71, RVol 3.6) |
| 12 | **ARM** | 164.81 | FLOW SURGE | **CALLS** | 56 | none: 11 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (2 contracts' greeks worked out here) | NEG -$5.1M | - | 180 | 180 | +$1.6M | +$30k bull / +$0 bear | out (clean 27, ADX 58, RVol 2.7) |
| 13 | **AMD** | 410.88 | FLOW SURGE | **CALLS** | 55 | none: 99 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (14 contracts' greeks worked out here) | NEG -$85.7M | - | 430 | 440 | +$46.2M | +$4.2M bull / -$59k bear | SHORT (clean 33, ADX 54, RVol 1.8) |
| 14 | **ORCL** | 112.28 | FLOW SURGE | **CALLS** | 55 | none: 22 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (6 contracts' greeks worked out here) | NEG -$44.1M | - | 120 | 110 | +$2.7M | +$55k bull / +$0 bear | SHORT (clean 34, ADX 52, RVol 1.5) |
| 15 | **COIN** | 134.16 | FLOW SURGE | **CALLS** | 53 | none: 24 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (3 contracts' greeks worked out here) | POS +$8.4M | - | 142 | 135 | +$2.1M | +$25k bull / +$0 bear | SHORT (clean 33, ADX 61, RVol 1.4) |
| 16 | **TSLA** | 341.38 | TREND (flow not with it) | **PUTS** | 52 | none: 71 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (4 contracts' greeks worked out here) | NEG -$128.6M | - | 370 | 350 | +$96.4M | +$4.2M bull / -$1.4M bear | SHORT (clean 35, ADX 56, RVol 2.9) |
| 17 | **GOOGL** | 278.26 | FLOW SURGE | **CALLS** | 52 | none: 66 calls 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (7 contracts' greeks worked out here) | NEG -$7.9M | 279.79 | 285 | 290 | +$10.3M | +$741k bull / +$0 bear | SHORT (clean 35, ADX 29, RVol 1.9) |
| 18 | **MSFT** | 533.27 | FLOW SURGE | **CALLS** | 51 | none: 129 calls 0-7DTE > 13 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (19 contracts' greeks worked out here) | POS +$712.0M | - | 540 | 500 | +$19.3M | +$925k bull / +$0 bear | out (clean 32, ADX 56, RVol 2.3) |
| 19 | **SMCI** | 26.04 | TREND (flow not with it) | **PUTS** | 51 | 11/06 25P @ 0.48 (delta 0.28) = est +41% at 25.19 | NEG -$2.1M | - | 28 | 27 | +$572k | - | SHORT (clean 36, ADX 58, RVol 1.9) |
| 20 | **BABA** | 104.97 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 50 | 11/06 102P @ 0.75 (delta 0.23) = est +27% at 103.58 | POS +$21.6M | - | 105 | 100 | +$1.2M | - | out (clean 37, ADX 21, RVol 2.0) |
| 21 | **AMZN** | 253.10 | FLOW SURGE | **CALLS** | 49 | none: 60 calls 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (8 contracts' greeks worked out here) | POS +$285.1M | - | 260 | 250 | +$32.8M | +$2.3M bull / -$27k bear | SHORT (clean 34, ADX 34, RVol 1.7) |
| 22 | **SHOP** | 138.72 | TREND (flow not with it) | **PUTS** | 43 | none: 27 puts 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (10 contracts' greeks worked out here) | NEG -$5.8M | - | 144 | 135 | +$246k | - | SHORT (clean 36, ADX 59, RVol 0.7) |
| 23 | **HOOD** | 75.87 | - | **-** | 32 | - | NEG -$6.8M | - | 83 | 80 | +$2.1M | +$53k bull / +$0 bear | out (clean 31, ADX 67, RVol 2.1) |
| 24 | **UBER** | 67.89 | FLIP CROSS down into negative gamma | **PUTS** | 31 | 11/06 67P @ 0.63 (delta 0.33) = est +34% at 66.99 | NEG -$1.3M | 68.4 | 70 | 65 | +$172k | - | out (clean 32, ADX 18, RVol 1.1) |
| 25 | **AAPL** | 346.65 | - | **-** | 26 | - | POS +$562.0M | 332.86 | 350 | 330 | +$18.4M | +$1.9M bull / +$0 bear | out (clean 31, ADX 21, RVol 2.0) |
| 26 | **CRM** | 225.02 | - | **-** | 18 | - | NEG -$11.6M | - | 240 | 220 | +$251k | - | out (clean 34, ADX 21, RVol 2.1) |
| 27 | **NFLX** | 65.45 | - | **-** | 15 | - | POS +$30.0M | 61.71 | 65 | 65 | +$394k | - | out (clean 33, ADX 20, RVol 1.3) |

## Big prints this scan (176)
- **SPY** PUT 770 2026-11-06 (1DTE): 450 @ 22.50 = **+$1.0M** SELL | vol 2,894 / OI 6,051
- **SPY** PUT 760 2026-11-06 (1DTE): 302 @ 14.05 = **+$424k** SELL | vol 25,260 / OI 11,725
- **SPY** PUT 760 2026-11-06 (1DTE): 302 @ 14.05 = **+$424k** SELL | vol 25,260 / OI 11,725
- **QQQ** CALL 660 2026-11-06 (1DTE): 411 @ 8.40 = **+$345k** BUY | vol 6,924 / OI 333
- **META** PUT 595 2026-11-06 (1DTE): 291 @ 10.80 = **+$314k** SELL | vol 7,467 / OI 1,135
- **SPY** PUT 750 2026-11-06 (1DTE): 400 @ 6.49 = **+$260k** SELL | vol 31,515 / OI 42,367
- **QQQ** PUT 670 2026-11-05 (0DTE): 205 @ 10.20 = **+$209k** SELL | vol 56,269 / OI 11,268
- **QQQ** CALL 660 2026-11-05 (0DTE): 442 @ 4.69 = **+$207k** BUY | vol 24,861 / OI 12
- **QQQ** CALL 660 2026-11-06 (1DTE): 240 @ 8.37 = **+$201k** BUY | vol 6,924 / OI 333
- **NVDA** CALL 185 2026-11-06 (1DTE): 389 @ 4.82 = **+$187k** BUY | vol 4,694 / OI 282
- **NVDA** CALL 190 2026-11-09 (4DTE): 500 @ 3.73 = **+$186k** BUY | vol 3,560 / OI 97
- **SMH** PUT 465 2026-11-06 (1DTE): 167 @ 11.15 = **+$186k** SELL | vol 12,853 / OI 10,681
- **NVDA** CALL 187.5 2026-11-06 (1DTE): 500 @ 3.63 = **+$182k** BUY | vol 11,813 / OI 151
- **QQQ** CALL 660 2026-11-06 (1DTE): 178 @ 9.05 = **+$161k** BUY | vol 6,924 / OI 333
- **MU** PUT 670 2026-11-06 (1DTE): 135 @ 11.70 = **+$158k** SELL | vol 6,401 / OI 0

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 725 2026-11-05 (0DTE): 3,174 traded vs OI 3,025
- **SPY** PUT 749 2026-11-10 (5DTE): 530 traded vs OI 67
- **SPY** CALL 747 2026-11-09 (4DTE): 768 traded vs OI 1
- **SPY** PUT 675 2026-11-09 (4DTE): 1,076 traded vs OI 0
- **SPY** CALL 777 2026-11-11 (6DTE): 500 traded vs OI 94
- **SPY** CALL 745 2026-11-06 (1DTE): 1,215 traded vs OI 1,181
- **SPY** CALL 740 2026-11-06 (1DTE): 560 traded vs OI 358
- **SPY** PUT 737 2026-11-10 (5DTE): 521 traded vs OI 55
- **SPY** PUT 747 2026-11-11 (6DTE): 509 traded vs OI 98
- **SPY** PUT 737 2026-11-13 (8DTE): 578 traded vs OI 565
- **SPY** CALL 747 2026-11-13 (8DTE): 509 traded vs OI 93
- **SPY** CALL 805 2026-11-17 (12DTE): 560 traded vs OI 16
- **SPY** CALL 790 2026-11-16 (11DTE): 528 traded vs OI 516
- **SPY** CALL 749 2026-11-20 (15DTE): 613 traded vs OI 174
- **SPY** CALL 770 2026-12-04 (29DTE): 1,013 traded vs OI 862

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
