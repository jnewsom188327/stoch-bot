# GEX + FLOW SCAN - Thu Nov 12, 12:00 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (5)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:35 | **SPY** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/12 754P | 0.59 | 0.17 | +10% (1m) | **-71%** (done) | +70% | 755 |
| 09:50 | **HOOD** | **PUTS** | TREND + FLOW | 11/13 79P | 0.55 | 0.36 | +5% (19m) | **-35%** (done) | +92% | 80 |
| 09:45 | **ORCL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/13 130C | 0.75 | 0.72 | +4% (60m) | **-4%** (done) | +59% | 126.9 |
| 09:45 | **SMCI** | **PUTS** | TREND + FLOW | 11/13 27P | 0.42 | 0.23 | -5% (6m) | **-45%** (done) | +57% | 27 |
| 09:45 | **SPY** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/12 753P | 0.79 | 0.31 | +23% (18m) | **-61%** (done) | +51% | 754.88 |

## 1m RULES on SPY / QQQ - loose (1 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 12:00:08 ET, last candle SPY 11:59, QQQ 11:59 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 10:03 | SPY | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |

## Flow surges NOT fired - price disagreed (7 today, last 5)
- 12:00 SMCI CALLS: price -0.27 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 11:55 SMCI CALLS: price -0.04 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 11:50 SMCI CALLS: price -0.48 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 11:45 SMCI CALLS: price -0.74 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:30 IWM CALLS: price -0.04 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **SMCI** | 26.44 | FLOW SURGE | **CALLS** | 62 | 11/13 27.5C @ 0.51 (delta 0.36) = est +137% at 28 | NEG -$1.0M | - | 28 | 25 | +$1.6M | +$259k bull / +$0 bear | SHORT (clean 34, ADX 44, RVol 7.3) |
| 2 | **GOOGL** | 300.21 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 45 | none: 72 puts 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (16 contracts' greeks worked out here) | POS +$134.7M | 287.22 | 300 | 290 | -$5.6M | +$26k bull / -$34k bear | out (clean 29, ADX 33, RVol 1.2) |
| 3 | **AMZN** | 269.98 | PINNED between the walls (positive gamma) - chop | **-** | 30 | - | POS +$509.5M | - | 270 | 270 | -$7.7M | +$55k bull / -$443k bear | out (clean 30, ADX 16, RVol 0.5) |
| 4 | **MSFT** | 527.93 | - | **-** | 21 | - | POS +$170.7M | 521.3 | 535 | 520 | -$4.1M | +$79k bull / +$0 bear | out (clean 31, ADX 31, RVol 0.4) |
| 5 | **SPY** | 761.15 | - | **-** | 20 | - | NEG -$41.7M | 761.44 | 760 | 760 | -$138.3M | +$236k bull / -$1.5M bear | out (clean 32, ADX 21, RVol 0.6) |
| 6 | **NVDA** | 165.28 | - | **-** | 20 | - | NEG -$185.4M | - | 170 | 160 | -$79.5M | +$4.8M bull / -$2.6M bear | out (clean 32, ADX 23, RVol 1.2) |
| 7 | **AMD** | 586.11 | - | **-** | 20 | - | POS +$197.2M | - | 600 | 550 | -$24.5M | +$4.1M bull / -$1.9M bear | out (clean 34, ADX 36, RVol 0.8) |
| 8 | **AVGO** | 365.04 | - | **-** | 20 | - | POS +$133.8M | - | 350 | 350 | +$6.8M | +$3.0M bull / +$0 bear | out (clean 35, ADX 28, RVol 1.2) |
| 9 | **DELL** | 373.03 | - | **-** | 20 | - | POS +$5.3M | - | 360 | 380 | +$223k | +$0 bull / -$373k bear | out (clean 36, ADX 25, RVol 2.8) |
| 10 | **MSTR** | 117.61 | - | **-** | 20 | - | NEG -$29.7M | - | 125 | 110 | -$2.0M | +$83k bull / -$75k bear | out (clean 28, ADX 24, RVol 0.8) |
| 11 | **QQQ** | 691.59 | - | **-** | 18 | - | POS +$279.3M | 690.49 | 700 | 680 | -$108.1M | +$1.5M bull / -$1.8M bear | out (clean 31, ADX 21, RVol 0.4) |
| 12 | **SMH** | 504.12 | - | **-** | 18 | - | NEG -$93.1M | - | 500 | 500 | -$1.5M | +$207k bull / -$47k bear | out (clean 30, ADX 21, RVol 0.5) |
| 13 | **AAPL** | 357.33 | - | **-** | 17 | - | POS +$1.1B | 341.15 | 360 | 360 | +$918k | +$479k bull / +$0 bear | out (clean 28, ADX 26, RVol 0.8) |
| 14 | **META** | 625.92 | - | **-** | 17 | - | POS +$18.0M | 624.42 | 650 | 600 | +$1.5M | +$187k bull / -$36k bear | out (clean 28, ADX 30, RVol 0.5) |
| 15 | **ORCL** | 127.55 | - | **-** | 17 | - | POS +$11.8M | 121.17 | 130 | 125 | -$389k | +$25k bull / +$0 bear | out (clean 29, ADX 20, RVol 0.5) |
| 16 | **HOOD** | 83.81 | - | **-** | 17 | - | POS +$15.9M | 79.17 | 85 | 80 | -$143k | +$82k bull / +$0 bear | out (clean 34, ADX 20, RVol 0.7) |
| 17 | **IWM** | 280.96 | - | **-** | 16 | - | NEG -$688.5M | 282.65 | 285 | 275 | -$1.7M | +$0 bull / -$197k bear | out (clean 34, ADX 23, RVol 0.4) |
| 18 | **TSLA** | 391.92 | - | **-** | 16 | - | POS +$376.8M | - | 400 | 380 | +$9.6M | +$344k bull / -$86k bear | out (clean 29, ADX 17, RVol 0.3) |
| 19 | **MU** | 788.61 | - | **-** | 16 | - | POS +$97.7M | - | 800 | 800 | +$10.8M | +$1.3M bull / -$1.4M bear | out (clean 31, ADX 20, RVol 0.6) |
| 20 | **BABA** | 94.94 | - | **-** | 15 | - | NEG -$17.7M | - | 100 | 100 | +$213k | - | out (clean 29, ADX 43, RVol 1.7) |
| 21 | **UBER** | 69.81 | - | **-** | 10 | - | POS +$17.7M | 68.31 | 70 | 70 | -$81k | - | out (clean 31, ADX 21, RVol 0.4) |
| 22 | **NFLX** | 63.65 | - | **-** | 9 | - | NEG -$9.6M | 64.17 | 65 | 65 | -$192k | - | out (clean 28, ADX 18, RVol 0.6) |
| 23 | **PLTR** | 172.34 | - | **-** | 9 | - | POS +$89.2M | - | 170 | 170 | -$470k | - | out (clean 28, ADX 24, RVol 0.7) |
| 24 | **SHOP** | 149.08 | - | **-** | 9 | - | POS +$5.6M | 143.92 | 150 | 150 | -$11k | - | out (clean 30, ADX 16, RVol 0.4) |
| 25 | **ARM** | 201.62 | - | **-** | 8 | - | POS +$10.1M | - | 200 | 200 | -$263k | - | out (clean 30, ADX 20, RVol 0.3) |
| 26 | **CRM** | 218.23 | - | **-** | 8 | - | NEG -$8.9M | - | 220 | 220 | -$36k | - | out (clean 29, ADX 23, RVol 0.2) |
| 27 | **COIN** | 133.85 | - | **-** | 7 | - | POS +$11.6M | 130.1 | 137 | 135 | +$615 | - | out (clean 29, ADX 28, RVol 1.0) |

## Big prints this scan (118)
- **MU** PUT 800 2026-11-16 (4DTE): 200 @ 30.55 = **+$611k** BUY | vol 965 / OI 71
- **AMD** PUT 615 2026-11-18 (6DTE): 97 @ 41.77 = **+$405k** BUY | vol 402 / OI 0
- **AMD** PUT 615 2026-11-18 (6DTE): 76 @ 41.77 = **+$317k** BUY | vol 402 / OI 0
- **NVDA** CALL 160 2026-11-18 (6DTE): 300 @ 10.45 = **+$314k** SELL | vol 8,319 / OI 1,177
- **NVDA** CALL 162.5 2026-11-18 (6DTE): 300 @ 9.05 = **+$272k** SELL | vol 9,399 / OI 61
- **AMD** CALL 565 2026-11-13 (1DTE): 100 @ 24.95 = **+$250k** SELL | vol 6,759 / OI 618
- **NVDA** PUT 162.5 2026-11-16 (4DTE): 500 @ 3.90 = **+$195k** BUY | vol 14,422 / OI 1,267
- **QQQ** CALL 689 2026-11-13 (1DTE): 347 @ 5.40 = **+$187k** SELL | vol 6,629 / OI 1,463
- **NVDA** PUT 162.5 2026-11-13 (1DTE): 500 @ 2.73 = **+$136k** BUY | vol 83,289 / OI 20,581
- **MU** PUT 790 2026-11-13 (1DTE): 80 @ 17.00 = **+$136k** BUY | vol 5,424 / OI 457
- **SPY** PUT 763 2026-11-13 (1DTE): 365 @ 3.72 = **+$136k** BUY | vol 3,671 / OI 957
- **QQQ** CALL 670 2026-11-13 (1DTE): 60 @ 21.17 = **+$127k** SELL | vol 564 / OI 2,726
- **MU** PUT 775 2026-11-13 (1DTE): 115 @ 11.00 = **+$126k** BUY | vol 6,400 / OI 632
- **NVDA** PUT 162.5 2026-11-13 (1DTE): 450 @ 2.70 = **+$122k** BUY | vol 83,289 / OI 20,581
- **QQQ** PUT 690 2026-11-12 (0DTE): 663 @ 1.77 = **+$117k** BUY | vol 87,292 / OI 443

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 764 2026-11-13 (1DTE): 1,006 traded vs OI 951
- **SPY** PUT 764 2026-11-17 (5DTE): 502 traded vs OI 68
- **SPY** PUT 757 2026-11-17 (5DTE): 530 traded vs OI 118
- **SPY** PUT 750 2026-11-23 (11DTE): 763 traded vs OI 762
- **SPY** PUT 745 2026-11-19 (7DTE): 557 traded vs OI 446
- **QQQ** PUT 681 2026-11-16 (4DTE): 503 traded vs OI 94
- **QQQ** PUT 691 2026-11-16 (4DTE): 643 traded vs OI 29
- **QQQ** PUT 692 2026-11-16 (4DTE): 502 traded vs OI 112
- **QQQ** CALL 715 2026-11-13 (1DTE): 1,865 traded vs OI 1,812
- **QQQ** PUT 670 2026-11-17 (5DTE): 506 traded vs OI 408
- **QQQ** PUT 680 2026-11-19 (7DTE): 675 traded vs OI 64
- **QQQ** CALL 730 2026-11-23 (11DTE): 1,022 traded vs OI 116
- **QQQ** PUT 680 2026-11-23 (11DTE): 517 traded vs OI 225
- **AMD** CALL 567.5 2026-11-20 (8DTE): 970 traded vs OI 0
- **AMD** CALL 605 2026-12-04 (22DTE): 507 traded vs OI 115

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
