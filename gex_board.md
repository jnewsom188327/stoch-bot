# GEX + FLOW SCAN - Thu Nov 05, 01:20 PM ET
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
Last 1m check 13:20:08 ET, last candle SPY 13:19, QQQ 13:19 | no errors
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
| 1 | **MU** | 678.31 | TREND (flow not with it) | **PUTS** | 55 | none: 82 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (10 contracts' greeks worked out here) | NEG -$65.7M | - | 700 | 700 | +$206.7M | +$3.1M bull / -$11.8M bear | SHORT (clean 33, ADX 36, RVol 2.6) |
| 2 | **IWM** | 271.82 | TREND (flow not with it) | **PUTS** | 53 | 11/05 271P @ 0.70 (delta 0.38) = est +80% at 270 | NEG -$2.7B | 287.13 | 285 | 270 | +$56.5M | +$1.5M bull / -$5.0M bear | SHORT (clean 38, ADX 53, RVol 1.8) |
| 3 | **SPY** | 736.60 | TREND (flow not with it) | **PUTS** | 51 | none: 657 puts 0-7DTE > 16 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (230 contracts' greeks worked out here) | NEG -$12.7B | 769.85 | 760 | 740 | +$1.1B | +$6.1M bull / -$6.8M bear | SHORT (clean 37, ADX 56, RVol 1.4) |
| 4 | **NVDA** | 182.59 | TREND (flow not with it) | **PUTS** | 47 | none: 36 puts 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (2 contracts' greeks worked out here) | NEG -$238.6M | - | 200 | 190 | +$72.2M | +$210k bull / -$1.7M bear | SHORT (clean 34, ADX 47, RVol 1.3) |
| 5 | **SMH** | 454.55 | FLOW SURGE | **CALLS** | 44 | none: 89 calls 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (6 contracts' greeks worked out here) | NEG -$268.1M | - | 445 | 500 | +$41.1M | +$257k bull / -$188k bear | out (clean 35, ADX 42, RVol 0.9) |
| 6 | **PLTR** | 155.17 | - | **-** | 29 | - | NEG -$46.3M | - | 165 | 150 | +$12.9M | +$0 bull / -$56k bear | out (clean 28, ADX 31, RVol 0.8) |
| 7 | **QQQ** | 651.91 | - | **-** | 27 | - | NEG -$4.4B | - | 700 | 680 | +$797.4M | +$2.5M bull / -$7.4M bear | out (clean 36, ADX 44, RVol 1.0) |
| 8 | **TSLA** | 341.31 | - | **-** | 26 | - | NEG -$128.3M | - | 350 | 350 | +$104.9M | +$887k bull / -$2.0M bear | out (clean 35, ADX 40, RVol 1.5) |
| 9 | **MSFT** | 537.32 | - | **-** | 26 | - | POS +$788.2M | - | 540 | 500 | +$21.1M | +$134k bull / +$0 bear | out (clean 32, ADX 33, RVol 0.8) |
| 10 | **AVGO** | 297.67 | - | **-** | 26 | - | NEG -$105.3M | - | 325 | 300 | +$8.7M | +$0 bull / -$253k bear | out (clean 32, ADX 32, RVol 0.7) |
| 11 | **DELL** | 324.80 | - | **-** | 26 | - | NEG -$12.8M | - | 350 | 340 | +$6.2M | +$80k bull / -$75k bear | out (clean 35, ADX 31, RVol 0.5) |
| 12 | **AMD** | 413.21 | - | **-** | 23 | - | NEG -$92.6M | - | 430 | 440 | +$34.4M | +$421k bull / -$911k bear | out (clean 34, ADX 38, RVol 0.9) |
| 13 | **AAPL** | 343.74 | - | **-** | 21 | - | POS +$408.4M | 334.46 | 350 | 330 | +$18.7M | +$1.1M bull / -$911k bear | out (clean 31, ADX 32, RVol 0.7) |
| 14 | **AMZN** | 259.55 | - | **-** | 20 | - | POS +$382.3M | - | 265 | 250 | +$22.2M | +$220k bull / +$0 bear | out (clean 35, ADX 14, RVol 0.8) |
| 15 | **MSTR** | 128.03 | - | **-** | 20 | - | POS +$42.7M | - | 135 | 125 | +$3.5M | +$0 bull / -$32k bear | out (clean 34, ADX 30, RVol 0.5) |
| 16 | **COIN** | 135.53 | - | **-** | 19 | - | POS +$14.9M | - | 142 | 135 | +$2.0M | - | out (clean 33, ADX 37, RVol 0.6) |
| 17 | **CRM** | 221.26 | - | **-** | 19 | - | NEG -$16.4M | - | 240 | 220 | +$560k | - | out (clean 34, ADX 24, RVol 1.0) |
| 18 | **META** | 601.69 | - | **-** | 17 | - | NEG -$123.6M | 621.8 | 650 | 600 | +$18.3M | +$771k bull / -$314k bear | out (clean 34, ADX 16, RVol 0.5) |
| 19 | **BABA** | 106.68 | - | **-** | 16 | - | POS +$21.0M | - | 110 | 110 | +$1.3M | - | out (clean 36, ADX 13, RVol 0.6) |
| 20 | **NFLX** | 65.28 | - | **-** | 14 | - | POS +$30.6M | 62.23 | 65 | 65 | +$951k | - | out (clean 33, ADX 28, RVol 0.4) |
| 21 | **HOOD** | 77.05 | - | **-** | 14 | - | NEG -$7.3M | - | 83 | 80 | +$2.0M | - | out (clean 32, ADX 42, RVol 1.2) |
| 22 | **ARM** | 168.56 | - | **-** | 14 | - | NEG -$6.9M | - | 180 | 180 | +$1.4M | - | out (clean 27, ADX 26, RVol 0.9) |
| 23 | **SMCI** | 26.68 | - | **-** | 13 | - | NEG -$2.9M | - | 28 | 27 | +$419k | - | out (clean 36, ADX 27, RVol 0.9) |
| 24 | **ORCL** | 114.81 | - | **-** | 12 | - | NEG -$57.0M | - | 125 | 115 | +$2.9M | - | out (clean 32, ADX 30, RVol 0.7) |
| 25 | **GOOGL** | 283.36 | - | **-** | 10 | - | POS +$19.6M | 281.04 | 285 | 290 | +$8.4M | - | out (clean 35, ADX 15, RVol 0.6) |
| 26 | **UBER** | 68.36 | - | **-** | 9 | - | POS +$2.6M | 67.91 | 70 | 65 | +$184k | - | out (clean 32, ADX 8, RVol 0.5) |
| 27 | **SHOP** | 144.38 | - | **-** | 8 | - | NEG -$5.7M | - | 144 | 135 | -$135k | - | out (clean 38, ADX 18, RVol 0.5) |

## Big prints this scan (195)
- **IWM** PUT 277 2026-11-06 (1DTE): 5,292 @ 6.52 = **+$3.5M** BUY | vol 26,704 / OI 32,973
- **SPY** PUT 740 2026-11-09 (4DTE): 1,000 @ 10.22 = **+$1.0M** BUY | vol 14,055 / OI 2,475
- **QQQ** CALL 660 2026-11-09 (4DTE): 500 @ 7.48 = **+$374k** SELL | vol 6,841 / OI 10
- **SPY** PUT 735 2026-11-05 (0DTE): 1,215 @ 3.00 = **+$364k** BUY | vol 245,431 / OI 15,976
- **SPY** PUT 753 2026-11-06 (1DTE): 200 @ 17.00 = **+$340k** BUY | vol 10,492 / OI 3,354
- **SPY** PUT 735 2026-11-05 (0DTE): 950 @ 3.24 = **+$308k** BUY | vol 245,431 / OI 15,976
- **MU** PUT 670 2026-11-09 (4DTE): 100 @ 29.95 = **+$300k** BUY | vol 3,768 / OI 0
- **TSLA** PUT 335 2026-11-06 (1DTE): 450 @ 6.30 = **+$284k** BUY | vol 17,436 / OI 1,231
- **META** CALL 600 2026-11-09 (4DTE): 192 @ 14.45 = **+$277k** SELL | vol 1,218 / OI 38
- **TSLA** PUT 335 2026-11-06 (1DTE): 450 @ 6.15 = **+$277k** BUY | vol 17,436 / OI 1,231
- **SPY** CALL 735 2026-11-05 (0DTE): 950 @ 2.75 = **+$261k** SELL | vol 11,661 / OI 27
- **AAPL** PUT 352.5 2026-11-06 (1DTE): 200 @ 10.00 = **+$200k** BUY | vol 17,765 / OI 92
- **AAPL** PUT 352.5 2026-11-06 (1DTE): 200 @ 10.00 = **+$200k** BUY | vol 17,765 / OI 92
- **QQQ** CALL 670 2026-11-09 (4DTE): 500 @ 3.98 = **+$199k** SELL | vol 11,560 / OI 106
- **QQQ** PUT 655 2026-11-05 (0DTE): 361 @ 5.50 = **+$199k** BUY | vol 133,171 / OI 1,387

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 770 2026-11-11 (6DTE): 1,662 traded vs OI 1,653
- **SPY** CALL 742 2026-11-11 (6DTE): 501 traded vs OI 0
- **SPY** PUT 725 2026-11-06 (1DTE): 15,669 traded vs OI 15,530
- **SPY** CALL 776 2026-11-10 (5DTE): 517 traded vs OI 153
- **SPY** CALL 738 2026-11-13 (8DTE): 502 traded vs OI 120
- **SPY** CALL 746 2026-11-12 (7DTE): 504 traded vs OI 0
- **SPY** PUT 733 2026-11-16 (11DTE): 513 traded vs OI 14
- **SPY** PUT 722 2026-11-18 (13DTE): 572 traded vs OI 0
- **SPY** PUT 704 2026-11-20 (15DTE): 5,332 traded vs OI 1,001
- **SPY** PUT 710 2026-11-20 (15DTE): 21,626 traded vs OI 21,357
- **SPY** CALL 742 2026-11-27 (22DTE): 661 traded vs OI 8
- **SPY** PUT 702 2026-11-20 (15DTE): 4,848 traded vs OI 2,438
- **SPY** PUT 685 2026-11-27 (22DTE): 614 traded vs OI 0
- **SPY** PUT 708 2026-11-20 (15DTE): 6,656 traded vs OI 2,474
- **SPY** PUT 700 2026-12-04 (29DTE): 2,891 traded vs OI 2,712

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
