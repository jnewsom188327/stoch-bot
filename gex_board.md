# GEX + FLOW SCAN - Wed Nov 11, 10:45 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (10)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:45 | **AVGO** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/11 345P | 0.78 | 0.77 | -1% (0m) | **-1%** | +149% | 345 |
| 10:35 | **MSFT** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/11 525C | 0.76 | 1.29 | +96% (9m) | **+70%** | +343% | 527.5 |
| 10:20 | **AVGO** | **CALLS** | TREND + FLOW | 11/11 355C | 0.71 | 0.34 | +8% (8m) | **-52%** | +280% | 356.78 |
| 10:15 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/11 282C | 0.65 | 0.67 | +14% (3m) | **+3%** | +66% | 282.84 |
| 10:05 | **NVDA** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/11 175C | 0.76 | 0.93 | +82% (34m) | **+22%** | +58% | 175 hit |
| 09:50 | **GOOGL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/11 292.5C | 0.51 | 0.54 | +39% (28m) | **+6%** | +82% | 291.86 |
| 09:45 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/11 282C | 0.68 | 0.67 | +85% (6m) | **-1%** | +68% | 282.96 |
| 09:45 | **QQQ** | **CALLS** | FLOW SURGE | 11/11 690C | 0.63 | 1.24 | +103% (59m) | **+97%** | +171% | 689.78 |
| 09:39 | **QQQ** | **CALLS** | 1m WHIPSAW (R1 R5) | 11/11 693C | 0.52 | 0.29 | -10% (0m) | **-44%** (done) | +92% | 690.43 |
| 09:39 | **SPY** | **CALLS** | 1m WHIPSAW (R1 R5) | 11/11 760C | 0.53 | 0.17 | -2% (0m) | **-68%** (done) | +79% | 758.82 |

## 1m RULES on SPY / QQQ - loose (3 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:45:08 ET, last candle SPY 10:44, QQQ 10:44 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 10:02 | QQQ | 1m AGREE FLIP | FULL | CALLS | up | logged (agree flip) |
| 09:38 | QQQ | 1m WHIPSAW | R1 R5 | CALLS | TURNING away | **FIRE** QQQ261111C00693000 |
| 09:38 | SPY | 1m WHIPSAW | R1 R5 | CALLS | TURNING away | **FIRE** SPY261111C00760000 |

## Flow surges NOT fired - price disagreed (7 today, last 5)
- 10:15 BABA CALLS: under EMA 20 - flow says one way, price says the other
- 10:00 MSFT CALLS: price -4.55 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:00 AMZN CALLS: price -0.73 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 09:55 AAPL PUTS: price +1.32 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 MSFT CALLS: price -2.01 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **DELL** | 372.60 | FLOW SURGE | **PUTS** | 55 | none: 29 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$151k | 383.71 | 380 | 340 | -$2.6M | +$0 bull / -$108k bear | LONG (clean 36, ADX 62, RVol 1.8) |
| 2 | **AVGO** | 349.44 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 46 | 11/11 345P @ 0.78 (delta 0.22) = est +149% at 345 | POS +$100.5M | - | 350 | 340 | +$4.8M | +$61k bull / +$0 bear | out (clean 35, ADX 50, RVol 1.1) |
| 3 | **MU** | 809.61 | FLOW SURGE | **PUTS** | 45 | none: 153 puts 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (67 contracts' greeks worked out here) | POS +$153.4M | - | 800 | 800 | -$156.3M | +$0 bull / -$8.5M bear | LONG (clean 33, ADX 62, RVol 1.1) |
| 4 | **SMCI** | 30.39 | FLOW SURGE | **PUTS** | 41 | none: 12 puts 0-7DTE > 3 priced 0.40-0.80 > 3 delta 0.2+ > 3 spread ok > 3 liquid > best one only +16% at the target (needs +20%) (1 contracts' greeks worked out here) | POS +$11.8M | - | 30 | 30 | -$418k | +$0 bull / -$36k bear | out (clean 32, ADX 56, RVol 1.0) |
| 5 | **AMD** | 545.29 | TREND (flow not with it) | **CALLS** | 35 | none: 172 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (74 contracts' greeks worked out here) | POS +$134.3M | - | 550 | 500 | -$49.1M | +$0 bull / -$2.7M bear | LONG (clean 33, ADX 42, RVol 0.9) |
| 6 | **MSFT** | 523.02 | - | **-** | 33 | - | POS +$95.5M | 515.36 | 535 | 520 | +$15.7M | +$287k bull / -$365k bear | out (clean 32, ADX 44, RVol 1.7) |
| 7 | **SMH** | 505.70 | - | **-** | 27 | - | NEG -$55.0M | - | 500 | 500 | -$1.6M | +$30k bull / -$51k bear | out (clean 31, ADX 41, RVol 1.9) |
| 8 | **AMZN** | 267.08 | - | **-** | 27 | - | POS +$424.2M | - | 270 | 265 | +$6.0M | +$40k bull / -$127k bear | out (clean 33, ADX 30, RVol 1.4) |
| 9 | **ARM** | 198.31 | - | **-** | 27 | - | POS +$3.7M | - | 200 | 200 | -$814k | - | out (clean 29, ADX 60, RVol 0.9) |
| 10 | **PLTR** | 172.70 | - | **-** | 25 | - | POS +$74.1M | - | 170 | 170 | +$1.2M | +$0 bull / -$84k bear | out (clean 30, ADX 42, RVol 0.3) |
| 11 | **QQQ** | 689.09 | - | **-** | 23 | - | NEG -$87.5M | 689.63 | 700 | 680 | -$54.6M | +$0 bull / -$2.5M bear | out (clean 32, ADX 50, RVol 0.5) |
| 12 | **TSLA** | 393.39 | - | **-** | 22 | - | POS +$419.6M | - | 400 | 380 | -$12.5M | +$1.4M bull / -$933k bear | out (clean 32, ADX 53, RVol 0.8) |
| 13 | **META** | 637.54 | - | **-** | 22 | - | POS +$222.0M | 626.03 | 650 | 625 | +$5.6M | +$220k bull / -$29k bear | out (clean 31, ADX 23, RVol 0.7) |
| 14 | **GOOGL** | 291.47 | - | **-** | 22 | - | POS +$51.9M | 289.03 | 300 | 290 | +$656k | +$103k bull / -$28k bear | out (clean 28, ADX 48, RVol 0.8) |
| 15 | **BABA** | 101.61 | - | **-** | 22 | - | NEG -$16.2M | 106.77 | 110 | 101 | +$404k | - | out (clean 29, ADX 33, RVol 0.7) |
| 16 | **ORCL** | 126.43 | - | **-** | 21 | - | NEG -$1.8M | 128.32 | 130 | 125 | +$316k | +$0 bull / -$310k bear | out (clean 28, ADX 49, RVol 0.8) |
| 17 | **SPY** | 757.43 | - | **-** | 20 | - | NEG -$3.1B | 761.08 | 760 | 750 | -$6.7M | +$0 bull / -$1.6M bear | out (clean 31, ADX 49, RVol 0.4) |
| 18 | **AAPL** | 353.81 | - | **-** | 20 | - | POS +$1.5B | 341.17 | 355 | 350 | -$831k | +$114k bull / +$0 bear | out (clean 27, ADX 46, RVol 0.5) |
| 19 | **IWM** | 282.22 | - | **-** | 19 | - | NEG -$239.3M | 282.84 | 285 | 270 | -$1.1M | +$0 bull / -$123k bear | out (clean 34, ADX 39, RVol 0.3) |
| 20 | **NVDA** | 174.43 | - | **-** | 19 | - | NEG -$174.8M | - | 180 | 175 | -$6.6M | +$680k bull / -$2.3M bear | out (clean 34, ADX 31, RVol 1.1) |
| 21 | **MSTR** | 122.26 | - | **-** | 15 | - | NEG -$671k | 122.06 | 133 | 120 | +$140k | +$0 bull / -$86k bear | out (clean 28, ADX 17, RVol 0.7) |
| 22 | **HOOD** | 84.26 | - | **-** | 15 | - | POS +$13.9M | - | 85 | 85 | -$321k | - | out (clean 32, ADX 35, RVol 0.7) |
| 23 | **CRM** | 216.24 | - | **-** | 10 | - | NEG -$11.2M | - | 230 | 220 | -$20k | - | out (clean 30, ADX 27, RVol 0.6) |
| 24 | **COIN** | 136.81 | - | **-** | 9 | - | POS +$22.0M | - | 141 | 135 | +$43k | - | out (clean 28, ADX 31, RVol 1.0) |
| 25 | **UBER** | 69.29 | - | **-** | 8 | - | POS +$8.7M | 68.29 | 70 | 70 | +$14k | - | out (clean 32, ADX 23, RVol 0.6) |
| 26 | **SHOP** | 147.75 | - | **-** | 8 | - | POS +$2.2M | 144.99 | 150 | 140 | +$985 | - | out (clean 33, ADX 38, RVol 0.2) |
| 27 | **NFLX** | 63.58 | - | **-** | 6 | - | NEG -$11.9M | 64.47 | 65 | 65 | +$50k | - | out (clean 26, ADX 14, RVol 0.7) |

## Big prints this scan (178)
- **AMD** CALL 535 2026-11-13 (2DTE): 187 @ 15.80 = **+$295k** SELL | vol 1,548 / OI 647
- **MU** CALL 775 2026-11-11 (0DTE): 100 @ 27.78 = **+$278k** SELL | vol 5,509 / OI 627
- **QQQ** CALL 687 2026-11-13 (2DTE): 448 @ 6.14 = **+$275k** SELL | vol 2,257 / OI 762
- **MU** CALL 780 2026-11-11 (0DTE): 100 @ 23.36 = **+$234k** SELL | vol 14,176 / OI 2,052
- **MU** CALL 790 2026-11-13 (2DTE): 75 @ 29.40 = **+$220k** SELL | vol 2,694 / OI 1,404
- **QQQ** CALL 689 2026-11-12 (1DTE): 600 @ 3.37 = **+$202k** SELL | vol 4,581 / OI 221
- **NVDA** PUT 170 2026-11-13 (2DTE): 1,000 @ 1.79 = **+$179k** BUY | vol 20,767 / OI 17,981
- **AMD** CALL 540 2026-11-11 (0DTE): 298 @ 5.55 = **+$165k** SELL | vol 15,523 / OI 507
- **QQQ** CALL 680 2026-11-11 (0DTE): 200 @ 7.80 = **+$156k** SELL | vol 6,371 / OI 2,402
- **QQQ** CALL 680 2026-11-11 (0DTE): 200 @ 7.80 = **+$156k** SELL | vol 6,371 / OI 2,402
- **QQQ** CALL 680 2026-11-11 (0DTE): 200 @ 7.80 = **+$156k** SELL | vol 6,371 / OI 2,402
- **SPY** CALL 741 2026-11-11 (0DTE): 100 @ 15.31 = **+$153k** SELL | vol 180 / OI 837
- **QQQ** CALL 686 2026-11-11 (0DTE): 500 @ 3.00 = **+$150k** SELL | vol 63,088 / OI 593
- **MU** CALL 800 2026-11-11 (0DTE): 131 @ 10.90 = **+$143k** SELL | vol 44,772 / OI 2,486
- **SPY** PUT 755 2026-11-13 (2DTE): 500 @ 2.80 = **+$140k** BUY | vol 7,457 / OI 9,468

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 779 2026-11-12 (1DTE): 1,507 traded vs OI 528
- **SPY** CALL 763 2026-11-16 (5DTE): 566 traded vs OI 464
- **SPY** CALL 763 2026-11-13 (2DTE): 1,967 traded vs OI 1,895
- **SPY** CALL 810 2026-11-17 (6DTE): 904 traded vs OI 164
- **SPY** PUT 735 2026-11-24 (13DTE): 544 traded vs OI 0
- **SPY** CALL 760 2026-11-25 (14DTE): 541 traded vs OI 0
- **QQQ** PUT 637 2026-11-12 (1DTE): 503 traded vs OI 46
- **QQQ** PUT 695 2026-11-11 (0DTE): 670 traded vs OI 628
- **QQQ** PUT 636 2026-11-12 (1DTE): 501 traded vs OI 35
- **QQQ** CALL 685 2026-11-13 (2DTE): 8,699 traded vs OI 8,669
- **QQQ** CALL 695 2026-11-18 (7DTE): 585 traded vs OI 259
- **SMH** CALL 512.5 2026-11-13 (2DTE): 531 traded vs OI 436
- **SMH** CALL 535 2026-11-27 (16DTE): 1,756 traded vs OI 100
- **NVDA** PUT 170 2026-11-13 (2DTE): 20,767 traded vs OI 17,981
- **NVDA** PUT 162.5 2026-11-13 (2DTE): 3,978 traded vs OI 3,607

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
