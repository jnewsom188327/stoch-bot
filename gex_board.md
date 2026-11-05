# GEX + FLOW SCAN - Thu Nov 05, 01:00 PM ET
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
Last 1m check 13:00:08 ET, last candle SPY 12:59, QQQ 12:59 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
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
| 1 | **IWM** | 271.61 | FLOW SURGE | **CALLS** | 57 | none: 274 calls 0-7DTE > 16 priced 0.40-0.80 > 2 delta 0.2+ > 2 spread ok > 2 liquid > best one only -12% at the target (needs +20%) (110 contracts' greeks worked out here) | NEG -$2.7B | - | 285 | 270 | +$64.5M | +$8.4M bull / +$0 bear | SHORT (clean 37, ADX 55, RVol 2.2) |
| 2 | **SPY** | 737.23 | FLOW SURGE | **CALLS** | 47 | none: 657 calls 0-7DTE > 25 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (389 contracts' greeks worked out here) | NEG -$12.7B | 770.64 | 760 | 740 | +$1.2B | +$5.8M bull / +$0 bear | SHORT (clean 36, ADX 57, RVol 1.1) |
| 3 | **MU** | 675.54 | TREND (flow not with it) | **PUTS** | 45 | none: 82 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (16 contracts' greeks worked out here) | NEG -$61.9M | - | 700 | 700 | +$223.8M | +$11.3M bull / +$0 bear | SHORT (clean 33, ADX 38, RVol 2.4) |
| 4 | **SMH** | 454.30 | FLOW SURGE | **CALLS** | 44 | none: 86 calls 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (3 contracts' greeks worked out here) | NEG -$197.5M | - | 445 | 465 | +$41.3M | +$156k bull / +$0 bear | out (clean 35, ADX 43, RVol 0.8) |
| 5 | **MSFT** | 540.04 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 44 | none: 129 puts 0-7DTE > 9 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (23 contracts' greeks worked out here) | POS +$822.6M | - | 540 | 500 | +$21.3M | +$452k bull / -$37k bear | out (clean 32, ADX 30, RVol 0.6) |
| 6 | **NVDA** | 182.77 | TREND (flow not with it) | **PUTS** | 39 | none: 36 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (1 contracts' greeks worked out here) | NEG -$238.6M | - | 200 | 190 | +$75.6M | +$4.0M bull / +$0 bear | SHORT (clean 33, ADX 47, RVol 1.4) |
| 7 | **PLTR** | 155.02 | FLOW SURGE | **CALLS** | 39 | none: 16 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (2 contracts' greeks worked out here) | NEG -$43.9M | - | 165 | 150 | +$13.0M | +$48k bull / +$0 bear | out (clean 28, ADX 33, RVol 0.6) |
| 8 | **TSLA** | 340.60 | TREND (flow not with it) | **PUTS** | 38 | none: 68 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (5 contracts' greeks worked out here) | NEG -$125.5M | - | 350 | 350 | +$110.1M | +$1.5M bull / -$519k bear | SHORT (clean 35, ADX 41, RVol 1.5) |
| 9 | **GOOGL** | 284.46 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 38 | none: 69 puts 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (17 contracts' greeks worked out here) | POS +$20.8M | 281.03 | 285 | 290 | +$8.7M | +$116k bull / +$0 bear | out (clean 35, ADX 12, RVol 0.6) |
| 10 | **COIN** | 134.91 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 38 | none: 25 calls 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (5 contracts' greeks worked out here) | POS +$10.8M | - | 142 | 135 | +$2.1M | - | out (clean 34, ADX 43, RVol 0.5) |
| 11 | **QQQ** | 652.47 | - | **-** | 28 | - | NEG -$4.5B | - | 700 | 680 | +$822.4M | +$5.4M bull / +$0 bear | out (clean 36, ADX 45, RVol 0.8) |
| 12 | **AVGO** | 296.98 | - | **-** | 28 | - | NEG -$105.2M | - | 325 | 300 | +$9.1M | +$236k bull / +$0 bear | out (clean 32, ADX 33, RVol 1.0) |
| 13 | **AMD** | 413.96 | - | **-** | 24 | - | NEG -$93.0M | - | 430 | 440 | +$36.9M | +$684k bull / +$0 bear | out (clean 34, ADX 38, RVol 0.9) |
| 14 | **ORCL** | 114.07 | - | **-** | 23 | - | NEG -$54.3M | - | 125 | 110 | +$3.0M | +$26k bull / +$0 bear | out (clean 33, ADX 34, RVol 0.6) |
| 15 | **HOOD** | 77.12 | - | **-** | 23 | - | NEG -$7.6M | - | 83 | 80 | +$2.2M | +$91k bull / +$0 bear | out (clean 32, ADX 42, RVol 0.7) |
| 16 | **AAPL** | 343.90 | - | **-** | 22 | - | POS +$399.4M | 334.38 | 350 | 330 | +$20.9M | +$299k bull / -$708k bear | out (clean 31, ADX 32, RVol 0.8) |
| 17 | **MSTR** | 127.44 | - | **-** | 21 | - | POS +$39.4M | - | 135 | 125 | +$3.9M | +$156k bull / +$0 bear | out (clean 34, ADX 34, RVol 0.4) |
| 18 | **AMZN** | 261.03 | - | **-** | 20 | - | POS +$389.6M | - | 265 | 250 | +$21.6M | +$174k bull / -$108k bear | out (clean 35, ADX 13, RVol 0.7) |
| 19 | **CRM** | 221.34 | - | **-** | 19 | - | NEG -$16.4M | - | 240 | 220 | +$560k | - | out (clean 34, ADX 20, RVol 1.1) |
| 20 | **META** | 604.68 | - | **-** | 17 | - | NEG -$118.5M | 621.89 | 650 | 600 | +$20.7M | +$957k bull / +$0 bear | out (clean 34, ADX 14, RVol 0.4) |
| 21 | **DELL** | 322.54 | - | **-** | 17 | - | NEG -$11.8M | - | 350 | 340 | +$6.4M | - | out (clean 35, ADX 33, RVol 0.5) |
| 22 | **BABA** | 106.58 | - | **-** | 16 | - | POS +$21.7M | - | 110 | 110 | +$1.3M | - | out (clean 36, ADX 15, RVol 0.4) |
| 23 | **NFLX** | 65.41 | - | **-** | 15 | - | POS +$29.8M | 62.05 | 65 | 65 | +$941k | - | out (clean 33, ADX 25, RVol 0.7) |
| 24 | **SMCI** | 26.55 | - | **-** | 14 | - | NEG -$2.8M | - | 28 | 27 | +$465k | - | out (clean 36, ADX 31, RVol 0.7) |
| 25 | **ARM** | 168.79 | - | **-** | 14 | - | NEG -$7.0M | - | 180 | 180 | +$1.4M | - | out (clean 27, ADX 29, RVol 0.7) |
| 26 | **UBER** | 68.50 | - | **-** | 9 | - | POS +$2.5M | 67.93 | 70 | 65 | +$178k | - | out (clean 32, ADX 8, RVol 0.5) |
| 27 | **SHOP** | 143.62 | - | **-** | 8 | - | NEG -$5.0M | - | 144 | 135 | -$133k | - | out (clean 38, ADX 18, RVol 0.4) |

## Big prints this scan (117)
- **NVDA** PUT 185 2026-11-06 (1DTE): 6,360 @ 4.66 = **+$3.0M** SELL | vol 73,035 / OI 9,821
- **IWM** PUT 277 2026-11-06 (1DTE): 4,978 @ 5.57 = **+$2.8M** SELL | vol 20,149 / OI 32,973
- **SPY** PUT 740 2026-11-05 (0DTE): 834 @ 3.66 = **+$305k** SELL | vol 285,761 / OI 3,497
- **SPY** PUT 741 2026-11-05 (0DTE): 590 @ 4.50 = **+$266k** SELL | vol 140,310 / OI 700
- **SPY** PUT 736 2026-11-05 (0DTE): 1,000 @ 2.14 = **+$214k** SELL | vol 122,713 / OI 259
- **SPY** PUT 741 2026-11-05 (0DTE): 433 @ 4.50 = **+$195k** SELL | vol 140,310 / OI 700
- **QQQ** PUT 653 2026-11-06 (1DTE): 200 @ 8.58 = **+$172k** SELL | vol 12,627 / OI 185
- **QQQ** PUT 652 2026-11-09 (4DTE): 148 @ 11.26 = **+$167k** SELL | vol 2,888 / OI 53
- **QQQ** PUT 666 2026-11-06 (1DTE): 99 @ 16.34 = **+$162k** SELL | vol 6,595 / OI 149
- **SPY** PUT 736 2026-11-05 (0DTE): 694 @ 2.22 = **+$154k** SELL | vol 122,713 / OI 259
- **QQQ** PUT 652 2026-11-09 (4DTE): 135 @ 11.26 = **+$152k** SELL | vol 2,888 / OI 53
- **SPY** PUT 738 2026-11-05 (0DTE): 448 @ 3.18 = **+$142k** SELL | vol 158,697 / OI 314
- **TSLA** PUT 347.5 2026-11-09 (4DTE): 100 @ 14.00 = **+$140k** SELL | vol 3,188 / OI 10
- **MU** PUT 660 2026-11-06 (1DTE): 100 @ 13.35 = **+$134k** SELL | vol 15,780 / OI 0
- **QQQ** PUT 675 2026-11-05 (0DTE): 60 @ 22.12 = **+$133k** SELL | vol 34,491 / OI 1,830

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 738 2026-11-11 (6DTE): 1,668 traded vs OI 0
- **SPY** CALL 735 2026-11-09 (4DTE): 549 traded vs OI 13
- **SPY** CALL 763 2026-11-11 (6DTE): 505 traded vs OI 25
- **SPY** PUT 722 2026-11-09 (4DTE): 519 traded vs OI 157
- **SPY** CALL 764 2026-11-10 (5DTE): 505 traded vs OI 87
- **SPY** CALL 761 2026-11-10 (5DTE): 681 traded vs OI 92
- **SPY** CALL 744 2026-11-12 (7DTE): 501 traded vs OI 0
- **SPY** PUT 702 2026-11-12 (7DTE): 522 traded vs OI 3
- **SPY** CALL 736 2026-11-12 (7DTE): 581 traded vs OI 4
- **SPY** PUT 737 2026-11-12 (7DTE): 504 traded vs OI 26
- **SPY** CALL 731 2026-11-13 (8DTE): 516 traded vs OI 92
- **SPY** PUT 734 2026-11-17 (12DTE): 537 traded vs OI 0
- **SPY** CALL 739 2026-11-12 (7DTE): 598 traded vs OI 2
- **SPY** PUT 732 2026-11-30 (25DTE): 529 traded vs OI 396
- **SPY** CALL 759 2026-11-18 (13DTE): 548 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
