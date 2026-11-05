# GEX + FLOW SCAN - Thu Nov 05, 02:40 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (4)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:55 | **BABA** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/06 102P | 0.75 | 0.33 | -5% (9m) | **-56%** (done) | +27% | 103.58 |
| 09:52 | **SPY** | **PUTS** | 1m WHIPSAW (R1) | 11/05 749P | 0.78 | 11.35 | +1355% (60m) | **+1355%** (done) | +47% | 753.11 hit |
| 09:50 | **BABA** | **CALLS** | TREND + FLOW | 11/06 111C | 0.48 | 0.20 | -12% (0m) | **-58%** (done) | +136% | 110 |
| 09:40 | **QQQ** | **CALLS** | 1m WHIPSAW (R1) | 11/05 683C | 0.78 | 0.10 | -4% (0m) | **-87%** (done) | +66% | 678.43 |

## 1m RULES on SPY / QQQ - loose (5 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 14:40:08 ET, last candle SPY 14:39, QQQ 14:39 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 13:05 | SPY | 1m WHIPSAW | R1 | CALLS | AGAINST you | no contract: 87 calls 0-1DTE > 8 priced 0.40-0.80 > 1 delta 0.15+ > 1 spread ok > 1 liquid |
| 11:44 | SPY | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |
| 10:38 | QQQ | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | no contract: 64 puts 0-1DTE > 1 priced 0.40-0.80 > 0 delta 0.15+ > 0 spread ok > 0 liquid  |
| 09:51 | SPY | 1m WHIPSAW | R1 | PUTS | TURNING away | **FIRE** SPY261105P00749000 |
| 09:39 | QQQ | 1m WHIPSAW | R1 | CALLS | AGAINST you | **FIRE** QQQ261105C00683000 |

## Flow surges NOT fired - price disagreed (36 today, last 5)
- 12:55 IWM CALLS: price -0.16 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 12:50 IWM CALLS: price -0.60 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 12:45 IWM CALLS: price -0.70 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 12:40 IWM CALLS: price -0.66 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 12:20 IWM CALLS: under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **SMH** | 457.02 | FLOW SURGE | **CALLS** | 39 | none: 89 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (3 contracts' greeks worked out here) | NEG -$277.7M | - | 445 | 500 | +$39.9M | +$311k bull / -$242k bear | out (clean 34, ADX 22, RVol 0.8) |
| 2 | **GOOGL** | 284.34 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 38 | none: 69 puts 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (3 contracts' greeks worked out here) | POS +$33.8M | 280.76 | 285 | 290 | +$8.4M | +$75k bull / +$0 bear | out (clean 34, ADX 13, RVol 0.7) |
| 3 | **SPY** | 737.23 | - | **-** | 28 | - | NEG -$13.5B | 768.96 | 760 | 740 | +$1.2B | +$11.9M bull / -$7.9M bear | out (clean 36, ADX 36, RVol 1.2) |
| 4 | **NFLX** | 65.15 | PINNED between the walls (positive gamma) - chop | **-** | 28 | - | POS +$31.5M | 62.17 | 65 | 65 | +$971k | - | out (clean 32, ADX 27, RVol 0.8) |
| 5 | **DELL** | 326.54 | - | **-** | 26 | - | NEG -$13.2M | - | 350 | 340 | +$6.5M | +$0 bull / -$348k bear | out (clean 33, ADX 20, RVol 1.9) |
| 6 | **BABA** | 107.33 | - | **-** | 26 | - | POS +$17.6M | - | 110 | 110 | +$1.2M | +$0 bull / -$29k bear | out (clean 35, ADX 12, RVol 1.5) |
| 7 | **QQQ** | 653.51 | - | **-** | 25 | - | NEG -$4.6B | - | 700 | 680 | +$842.8M | +$4.2M bull / -$3.6M bear | out (clean 35, ADX 25, RVol 1.8) |
| 8 | **IWM** | 271.63 | - | **-** | 25 | - | NEG -$2.8B | 287.08 | 285 | 270 | +$55.6M | +$368k bull / -$72k bear | out (clean 36, ADX 33, RVol 1.0) |
| 9 | **NVDA** | 183.38 | - | **-** | 23 | - | NEG -$244.2M | - | 200 | 190 | +$71.6M | +$3.1M bull / -$440k bear | out (clean 33, ADX 27, RVol 1.0) |
| 10 | **TSLA** | 343.21 | - | **-** | 23 | - | NEG -$134.0M | - | 350 | 350 | +$110.7M | +$2.1M bull / -$344k bear | out (clean 35, ADX 24, RVol 1.2) |
| 11 | **MSFT** | 537.39 | - | **-** | 23 | - | POS +$823.4M | - | 540 | 500 | +$21.6M | +$470k bull / +$0 bear | out (clean 32, ADX 23, RVol 0.5) |
| 12 | **COIN** | 137.04 | - | **-** | 23 | - | POS +$18.7M | - | 142 | 135 | +$1.8M | +$0 bull / -$32k bear | out (clean 33, ADX 21, RVol 0.4) |
| 13 | **MU** | 678.52 | - | **-** | 23 | - | NEG -$66.3M | - | 700 | 700 | +$234.4M | +$5.0M bull / -$3.3M bear | out (clean 32, ADX 22, RVol 1.5) |
| 14 | **AAPL** | 344.13 | - | **-** | 20 | - | POS +$448.4M | 334.65 | 350 | 330 | +$25.2M | +$542k bull / -$565k bear | out (clean 31, ADX 22, RVol 0.8) |
| 15 | **AMZN** | 260.06 | - | **-** | 20 | - | POS +$387.4M | - | 265 | 250 | +$23.2M | +$250k bull / -$192k bear | out (clean 34, ADX 18, RVol 0.5) |
| 16 | **HOOD** | 77.91 | - | **-** | 20 | - | NEG -$9.5M | - | 85 | 80 | +$2.3M | +$26k bull / +$0 bear | out (clean 30, ADX 25, RVol 0.7) |
| 17 | **AMD** | 415.38 | - | **-** | 19 | - | NEG -$97.3M | - | 430 | 440 | +$36.1M | +$850k bull / -$187k bear | out (clean 32, ADX 20, RVol 0.6) |
| 18 | **MSTR** | 128.91 | - | **-** | 18 | - | POS +$53.5M | - | 135 | 125 | +$4.0M | +$60k bull / -$42k bear | out (clean 33, ADX 14, RVol 0.6) |
| 19 | **CRM** | 221.15 | - | **-** | 18 | - | NEG -$16.8M | - | 240 | 220 | +$557k | - | out (clean 34, ADX 21, RVol 0.9) |
| 20 | **PLTR** | 155.17 | - | **-** | 16 | - | NEG -$45.5M | - | 165 | 150 | +$13.5M | - | out (clean 27, ADX 19, RVol 0.8) |
| 21 | **META** | 605.13 | - | **-** | 15 | - | NEG -$115.0M | 621.03 | 650 | 600 | +$17.4M | +$401k bull / -$334k bear | out (clean 33, ADX 11, RVol 0.4) |
| 22 | **AVGO** | 297.71 | - | **-** | 15 | - | NEG -$107.2M | - | 325 | 300 | +$9.0M | - | out (clean 31, ADX 23, RVol 0.9) |
| 23 | **SMCI** | 27.27 | - | **-** | 11 | - | NEG -$3.1M | - | 28 | 27 | +$359k | - | out (clean 35, ADX 18, RVol 1.5) |
| 24 | **ARM** | 168.81 | - | **-** | 11 | - | NEG -$7.1M | - | 180 | 180 | +$1.4M | - | out (clean 27, ADX 15, RVol 0.8) |
| 25 | **ORCL** | 115.18 | - | **-** | 9 | - | NEG -$57.6M | - | 125 | 115 | +$2.9M | - | out (clean 31, ADX 17, RVol 0.6) |
| 26 | **UBER** | 68.73 | - | **-** | 9 | - | POS +$4.9M | 68.04 | 70 | 65 | +$196k | - | out (clean 30, ADX 10, RVol 0.7) |
| 27 | **SHOP** | 144.30 | - | **-** | 6 | - | NEG -$4.5M | - | 144 | 135 | -$127k | - | out (clean 37, ADX 12, RVol 0.4) |

## Big prints this scan (80)
- **QQQ** PUT 660 2026-11-06 (1DTE): 1,012 @ 11.09 = **+$1.1M** SELL | vol 36,872 / OI 14,507
- **QQQ** PUT 650 2026-11-09 (4DTE): 652 @ 9.43 = **+$615k** BUY | vol 13,061 / OI 1,396
- **QQQ** PUT 660 2026-11-06 (1DTE): 414 @ 11.12 = **+$460k** SELL | vol 36,872 / OI 14,507
- **QQQ** PUT 662 2026-11-06 (1DTE): 246 @ 12.95 = **+$319k** BUY | vol 7,425 / OI 96
- **MU** PUT 700 2026-11-09 (4DTE): 70 @ 42.32 = **+$296k** BUY | vol 4,368 / OI 0
- **MU** PUT 700 2026-11-09 (4DTE): 70 @ 42.31 = **+$296k** BUY | vol 4,368 / OI 0
- **QQQ** PUT 683 2026-11-05 (0DTE): 100 @ 29.47 = **+$295k** SELL | vol 7,636 / OI 310
- **TSLA** CALL 355 2026-11-06 (1DTE): 990 @ 2.73 = **+$270k** BUY | vol 28,754 / OI 272
- **QQQ** PUT 655 2026-11-05 (0DTE): 574 @ 4.10 = **+$235k** BUY | vol 157,128 / OI 1,387
- **NVDA** PUT 180 2026-11-09 (4DTE): 512 @ 4.00 = **+$205k** SELL | vol 12,638 / OI 538
- **META** PUT 600 2026-11-06 (1DTE): 228 @ 8.25 = **+$188k** BUY | vol 13,636 / OI 3,434
- **QQQ** PUT 683 2026-11-05 (0DTE): 50 @ 29.51 = **+$148k** SELL | vol 7,636 / OI 310
- **QQQ** PUT 651 2026-11-05 (0DTE): 710 @ 2.00 = **+$142k** BUY | vol 106,725 / OI 200
- **QQQ** PUT 650 2026-11-09 (4DTE): 150 @ 9.42 = **+$141k** BUY | vol 13,061 / OI 1,396
- **QQQ** CALL 660 2026-11-06 (1DTE): 265 @ 5.17 = **+$137k** SELL | vol 41,231 / OI 333

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 712 2026-11-10 (5DTE): 500 traded vs OI 6
- **SPY** PUT 700 2026-11-13 (8DTE): 10,702 traded vs OI 10,233
- **QQQ** CALL 679 2026-11-09 (4DTE): 503 traded vs OI 12
- **QQQ** PUT 655 2026-11-27 (22DTE): 833 traded vs OI 829
- **QQQ** CALL 710 2026-11-16 (11DTE): 611 traded vs OI 219
- **IWM** PUT 270 2026-11-11 (6DTE): 894 traded vs OI 892
- **AMD** PUT 400 2026-11-11 (6DTE): 515 traded vs OI 165
- **META** PUT 605 2026-11-09 (4DTE): 509 traded vs OI 103
- **MSFT** CALL 560 2026-11-13 (8DTE): 779 traded vs OI 716
- **AVGO** PUT 295 2026-11-11 (6DTE): 611 traded vs OI 41
- **MU** PUT 707.5 2026-11-11 (6DTE): 502 traded vs OI 0
- **MU** PUT 695 2026-11-16 (11DTE): 548 traded vs OI 0
- **ORCL** PUT 108 2026-11-06 (1DTE): 516 traded vs OI 0
- **HOOD** PUT 79 2026-11-27 (22DTE): 500 traded vs OI 222
- **ARM** CALL 172.5 2026-11-06 (1DTE): 501 traded vs OI 4

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
