# GEX + FLOW SCAN - Thu Nov 05, 12:40 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (4)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:55 | **BABA** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/06 102P | 0.75 | 0.33 | -5% (9m) | **-56%** (done) | +27% | 103.58 |
| 09:52 | **SPY** | **PUTS** | 1m WHIPSAW (R1) | 11/05 749P | 0.78 | 11.35 | +1355% (60m) | **+1355%** (done) | +47% | 753.11 hit |
| 09:50 | **BABA** | **CALLS** | TREND + FLOW | 11/06 111C | 0.48 | 0.20 | -12% (0m) | **-58%** (done) | +136% | 110 |
| 09:40 | **QQQ** | **CALLS** | 1m WHIPSAW (R1) | 11/05 683C | 0.78 | 0.10 | -4% (0m) | **-87%** (done) | +66% | 678.43 |

## 1m RULES on SPY / QQQ - loose (4 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 12:40:08 ET, last candle SPY 12:39, QQQ 12:39 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 11:44 | SPY | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |
| 10:38 | QQQ | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | no contract: 64 puts 0-1DTE > 1 priced 0.40-0.80 > 0 delta 0.15+ > 0 spread ok > 0 liquid  |
| 09:51 | SPY | 1m WHIPSAW | R1 | PUTS | TURNING away | **FIRE** SPY261105P00749000 |
| 09:39 | QQQ | 1m WHIPSAW | R1 | CALLS | AGAINST you | **FIRE** QQQ261105C00683000 |

## Flow surges NOT fired - price disagreed (33 today, last 5)
- 12:40 IWM CALLS: price -0.66 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 12:20 IWM CALLS: under EMA 20 - flow says one way, price says the other
- 12:15 IWM CALLS: price -0.86 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 12:10 IWM CALLS: price -1.05 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 12:05 IWM CALLS: price -1.32 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **IWM** | 271.96 | FLOW SURGE | **CALLS** | 50 | 11/05 273C @ 0.59 (delta 0.34) = est +102% at 273.8 | NEG -$2.7B | 287.27 | 285 | 270 | +$57.5M | +$1.1M bull / +$0 bear | SHORT (clean 37, ADX 54, RVol 1.4) |
| 2 | **SPY** | 737.94 | FLOW SURGE | **CALLS** | 47 | none: 658 calls 0-7DTE > 27 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (246 contracts' greeks worked out here) | NEG -$12.7B | 770 | 760 | 740 | +$1.1B | +$4.6M bull / +$0 bear | SHORT (clean 36, ADX 57, RVol 1.0) |
| 3 | **MSFT** | 540.26 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 46 | none: 129 puts 0-7DTE > 10 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (26 contracts' greeks worked out here) | POS +$817.7M | - | 540 | 500 | +$19.8M | +$316k bull / +$0 bear | out (clean 32, ADX 33, RVol 0.9) |
| 4 | **TSLA** | 341.25 | TREND (flow not with it) | **PUTS** | 39 | none: 71 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (8 contracts' greeks worked out here) | NEG -$125.6M | - | 350 | 350 | +$108.2M | +$1.7M bull / +$0 bear | SHORT (clean 35, ADX 43, RVol 1.6) |
| 5 | **COIN** | 135.09 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 39 | none: 25 calls 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (3 contracts' greeks worked out here) | POS +$11.5M | - | 142 | 135 | +$2.1M | - | out (clean 33, ADX 45, RVol 0.6) |
| 6 | **MU** | 684.10 | TREND (flow not with it) | **PUTS** | 33 | none: 88 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (6 contracts' greeks worked out here) | NEG -$85.5M | - | 700 | 700 | +$203.6M | +$4.6M bull / -$2.4M bear | SHORT (clean 33, ADX 38, RVol 1.1) |
| 7 | **SMH** | 456.51 | - | **-** | 32 | - | NEG -$264.9M | - | 500 | 500 | +$40.9M | +$55k bull / -$170k bear | out (clean 35, ADX 42, RVol 0.9) |
| 8 | **QQQ** | 653.25 | - | **-** | 28 | - | NEG -$4.4B | - | 700 | 680 | +$774.5M | +$4.9M bull / -$325k bear | out (clean 35, ADX 46, RVol 0.8) |
| 9 | **NVDA** | 183.63 | - | **-** | 28 | - | NEG -$247.2M | - | 200 | 190 | +$66.4M | +$748k bull / +$0 bear | out (clean 33, ADX 44, RVol 1.1) |
| 10 | **AVGO** | 298.50 | - | **-** | 27 | - | NEG -$105.5M | - | 325 | 300 | +$7.6M | +$72k bull / +$0 bear | out (clean 32, ADX 31, RVol 1.1) |
| 11 | **DELL** | 323.76 | - | **-** | 27 | - | NEG -$12.3M | - | 350 | 340 | +$6.2M | +$0 bull / -$29k bear | out (clean 35, ADX 32, RVol 0.7) |
| 12 | **AAPL** | 343.61 | - | **-** | 24 | - | POS +$408.4M | 334.22 | 350 | 330 | +$21.2M | +$143k bull / +$0 bear | out (clean 32, ADX 34, RVol 1.1) |
| 13 | **AMD** | 415.72 | - | **-** | 24 | - | NEG -$95.0M | - | 430 | 440 | +$34.2M | +$203k bull / -$412k bear | out (clean 34, ADX 38, RVol 0.8) |
| 14 | **ORCL** | 114.16 | - | **-** | 23 | - | NEG -$55.6M | - | 125 | 115 | +$2.7M | +$27k bull / +$0 bear | out (clean 33, ADX 36, RVol 0.8) |
| 15 | **AMZN** | 260.88 | - | **-** | 21 | - | POS +$388.1M | - | 265 | 250 | +$21.7M | +$125k bull / -$62k bear | out (clean 35, ADX 15, RVol 0.8) |
| 16 | **MSTR** | 127.93 | - | **-** | 21 | - | POS +$41.8M | - | 135 | 125 | +$3.3M | +$0 bull / -$58k bear | out (clean 34, ADX 36, RVol 0.4) |
| 17 | **GOOGL** | 284.94 | - | **-** | 20 | - | POS +$28.2M | 281.05 | 290 | 290 | +$8.1M | +$26k bull / +$0 bear | out (clean 35, ADX 14, RVol 0.8) |
| 18 | **PLTR** | 154.91 | - | **-** | 20 | - | NEG -$43.4M | - | 165 | 150 | +$13.0M | - | out (clean 28, ADX 35, RVol 0.7) |
| 19 | **META** | 605.48 | - | **-** | 18 | - | NEG -$112.1M | 622.88 | 650 | 600 | +$19.3M | +$1.0M bull / -$127k bear | out (clean 34, ADX 16, RVol 0.7) |
| 20 | **CRM** | 222.58 | - | **-** | 17 | - | NEG -$16.0M | - | 240 | 220 | +$525k | - | out (clean 34, ADX 17, RVol 0.4) |
| 21 | **BABA** | 106.58 | - | **-** | 17 | - | POS +$21.4M | - | 110 | 110 | +$1.3M | - | out (clean 37, ADX 18, RVol 0.4) |
| 22 | **SMCI** | 26.62 | - | **-** | 15 | - | NEG -$3.0M | - | 28 | 27 | +$441k | - | out (clean 37, ADX 33, RVol 1.0) |
| 23 | **ARM** | 168.59 | - | **-** | 15 | - | NEG -$7.1M | - | 180 | 180 | +$1.4M | - | out (clean 27, ADX 33, RVol 0.7) |
| 24 | **NFLX** | 65.33 | - | **-** | 14 | - | POS +$29.6M | 62.14 | 65 | 65 | +$806k | - | out (clean 32, ADX 23, RVol 0.7) |
| 25 | **HOOD** | 77.44 | - | **-** | 13 | - | NEG -$8.6M | - | 85 | 80 | +$1.9M | - | out (clean 32, ADX 42, RVol 0.5) |
| 26 | **UBER** | 68.44 | - | **-** | 9 | - | POS +$3.3M | 67.88 | 70 | 65 | +$166k | - | out (clean 32, ADX 10, RVol 0.5) |
| 27 | **SHOP** | 143.41 | - | **-** | 8 | - | NEG -$5.8M | - | 144 | 135 | -$131k | - | out (clean 38, ADX 22, RVol 0.4) |

## Big prints this scan (81)
- **META** PUT 600 2026-11-09 (4DTE): 500 @ 10.50 = **+$525k** SELL | vol 1,551 / OI 309
- **SPY** CALL 725 2026-11-10 (5DTE): 225 @ 19.60 = **+$441k** BUY | vol 286 / OI 21
- **SPY** CALL 727 2026-11-10 (5DTE): 225 @ 17.98 = **+$405k** BUY | vol 240 / OI 0
- **QQQ** PUT 656 2026-11-06 (1DTE): 500 @ 7.92 = **+$396k** SELL | vol 9,739 / OI 214
- **QQQ** PUT 640 2026-11-06 (1DTE): 1,000 @ 2.75 = **+$275k** SELL | vol 31,663 / OI 7,487
- **SPY** PUT 760 2026-11-06 (1DTE): 100 @ 19.70 = **+$197k** SELL | vol 27,742 / OI 11,725
- **QQQ** PUT 656 2026-11-05 (0DTE): 499 @ 3.88 = **+$194k** SELL | vol 67,343 / OI 171
- **MU** PUT 660 2026-11-06 (1DTE): 192 @ 9.95 = **+$191k** SELL | vol 14,561 / OI 0
- **NVDA** PUT 185 2026-11-06 (1DTE): 498 @ 3.80 = **+$189k** SELL | vol 64,708 / OI 9,821
- **QQQ** CALL 665 2026-11-06 (1DTE): 389 @ 4.75 = **+$185k** BUY | vol 16,388 / OI 65
- **IWM** PUT 272 2026-11-05 (0DTE): 2,000 @ 0.81 = **+$162k** SELL | vol 38,363 / OI 927
- **QQQ** PUT 656 2026-11-05 (0DTE): 433 @ 3.70 = **+$160k** SELL | vol 67,343 / OI 171
- **SPY** PUT 745 2026-11-06 (1DTE): 200 @ 7.81 = **+$156k** SELL | vol 26,953 / OI 14,342
- **SPY** PUT 735 2026-11-06 (1DTE): 500 @ 2.97 = **+$148k** SELL | vol 37,509 / OI 24,589
- **TSLA** CALL 335 2026-11-06 (1DTE): 120 @ 12.20 = **+$146k** BUY | vol 899 / OI 132

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 665 2026-11-09 (4DTE): 714 traded vs OI 0
- **SPY** PUT 665 2026-11-10 (5DTE): 938 traded vs OI 0
- **SPY** CALL 759 2026-11-11 (6DTE): 527 traded vs OI 71
- **SPY** PUT 665 2026-11-06 (1DTE): 1,751 traded vs OI 0
- **SPY** PUT 740 2026-11-12 (7DTE): 1,175 traded vs OI 1,159
- **SPY** PUT 739 2026-11-12 (7DTE): 503 traded vs OI 12
- **SPY** PUT 665 2026-11-20 (15DTE): 2,332 traded vs OI 0
- **SPY** CALL 750 2026-11-19 (14DTE): 541 traded vs OI 0
- **SPY** PUT 750 2026-12-04 (29DTE): 736 traded vs OI 716
- **QQQ** CALL 652 2026-11-13 (8DTE): 521 traded vs OI 1
- **QQQ** CALL 662 2026-11-13 (8DTE): 501 traded vs OI 0
- **QQQ** CALL 676 2026-11-13 (8DTE): 549 traded vs OI 157
- **QQQ** PUT 635 2026-11-27 (22DTE): 805 traded vs OI 342
- **QQQ** CALL 707 2026-11-17 (12DTE): 636 traded vs OI 0
- **QQQ** CALL 675 2026-11-17 (12DTE): 569 traded vs OI 14

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
