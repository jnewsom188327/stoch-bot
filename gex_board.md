# GEX + FLOW SCAN - Wed Nov 11, 11:00 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (10)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:45 | **AVGO** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/11 345P | 0.78 | 0.20 | +6% (1m) | **-74%** | +149% | 345 |
| 10:35 | **MSFT** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/11 525C | 0.76 | 0.92 | +96% (9m) | **+21%** | +343% | 527.5 |
| 10:20 | **AVGO** | **CALLS** | TREND + FLOW | 11/11 355C | 0.71 | 1.40 | +127% (38m) | **+97%** | +280% | 356.78 |
| 10:15 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/11 282C | 0.65 | 0.97 | +49% (45m) | **+49%** | +66% | 282.84 |
| 10:05 | **NVDA** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/11 175C | 0.76 | 1.78 | +142% (51m) | **+134%** | +58% | 175 hit |
| 09:50 | **GOOGL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/11 292.5C | 0.51 | 0.62 | +39% (28m) | **+22%** (done) | +82% | 291.86 |
| 09:45 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/11 282C | 0.68 | 0.64 | +85% (6m) | **-6%** (done) | +68% | 282.96 |
| 09:45 | **QQQ** | **CALLS** | FLOW SURGE | 11/11 690C | 0.63 | 1.23 | +103% (59m) | **+95%** (done) | +171% | 689.78 |
| 09:39 | **QQQ** | **CALLS** | 1m WHIPSAW (R1 R5) | 11/11 693C | 0.52 | 0.29 | -10% (0m) | **-44%** (done) | +92% | 690.43 |
| 09:39 | **SPY** | **CALLS** | 1m WHIPSAW (R1 R5) | 11/11 760C | 0.53 | 0.17 | -2% (0m) | **-68%** (done) | +79% | 758.82 |

## 1m RULES on SPY / QQQ - loose (3 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 11:00:08 ET, last candle SPY 10:59, QQQ 10:59 | no errors
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
| 1 | **DELL** | 377.15 | FLOW SURGE | **PUTS** | 47 | none: 30 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$443k | - | 380 | 380 | -$3.0M | +$0 bull / -$141k bear | LONG (clean 36, ADX 67, RVol 0.9) |
| 2 | **ARM** | 202.26 | FLOW SURGE | **PUTS** | 45 | none: 16 puts 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$5.0M | - | 200 | 200 | -$1.2M | +$0 bull / -$246k bear | out (clean 30, ADX 65, RVol 1.2) |
| 3 | **MU** | 820.91 | FLOW SURGE | **PUTS** | 44 | none: 145 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (55 contracts' greeks worked out here) | POS +$106.0M | - | 800 | 800 | -$193.4M | +$0 bull / -$10.6M bear | LONG (clean 33, ADX 67, RVol 1.0) |
| 4 | **AMD** | 554.93 | TREND (flow not with it) | **CALLS** | 38 | none: 180 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (79 contracts' greeks worked out here) | POS +$135.5M | - | 550 | 500 | -$63.1M | +$0 bull / -$3.7M bear | LONG (clean 33, ADX 46, RVol 1.1) |
| 5 | **AMZN** | 267.01 | TREND (flow not with it) | **PUTS** | 37 | none: 84 puts 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (41 contracts' greeks worked out here) | POS +$435.6M | - | 270 | 265 | +$4.2M | +$100k bull / -$505k bear | SHORT (clean 33, ADX 29, RVol 0.8) |
| 6 | **HOOD** | 84.75 | FLOW SURGE | **PUTS** | 37 | 11/13 81P @ 0.69 (delta 0.22) = est +32% at 83.59 | POS +$15.7M | - | 85 | 85 | -$840k | +$0 bull / -$52k bear | out (clean 33, ADX 38, RVol 0.8) |
| 7 | **NVDA** | 176.18 | TREND (flow not with it) | **CALLS** | 34 | 11/11 177.5C @ 0.66 (delta 0.33) = est +295% at 180 | NEG -$147.8M | - | 180 | 175 | -$22.2M | +$0 bull / -$3.3M bear | LONG (clean 34, ADX 34, RVol 1.5) |
| 8 | **SMH** | 511.16 | - | **-** | 30 | - | NEG -$46.8M | - | 500 | 500 | -$2.6M | +$0 bull / -$187k bear | out (clean 31, ADX 45, RVol 2.3) |
| 9 | **MSFT** | 522.21 | - | **-** | 28 | - | POS +$69.4M | 515.8 | 535 | 520 | +$11.5M | +$223k bull / -$846k bear | out (clean 32, ADX 43, RVol 1.6) |
| 10 | **QQQ** | 692.00 | - | **-** | 26 | - | POS +$252.9M | 690.61 | 700 | 680 | -$106.3M | +$0 bull / -$2.8M bear | out (clean 33, ADX 54, RVol 0.6) |
| 11 | **AVGO** | 353.83 | - | **-** | 25 | - | POS +$86.3M | - | 350 | 350 | +$4.8M | +$0 bull / -$145k bear | out (clean 35, ADX 51, RVol 1.2) |
| 12 | **UBER** | 69.27 | - | **-** | 25 | - | POS +$8.6M | 68.33 | 70 | 70 | +$71k | +$32k bull / +$0 bear | out (clean 31, ADX 23, RVol 0.6) |
| 13 | **PLTR** | 173.27 | - | **-** | 24 | - | POS +$76.3M | - | 170 | 180 | +$1.1M | +$0 bull / -$29k bear | out (clean 30, ADX 43, RVol 0.3) |
| 14 | **ORCL** | 128.41 | FLIP CROSS up into positive gamma | **CALLS** | 24 | none: 26 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$3.7M | 123.8 | 130 | 125 | +$143k | - | out (clean 29, ADX 51, RVol 0.8) |
| 15 | **TSLA** | 395.03 | - | **-** | 23 | - | POS +$424.0M | - | 400 | 380 | -$21.0M | +$0 bull / -$2.6M bear | out (clean 33, ADX 56, RVol 0.7) |
| 16 | **SMCI** | 30.81 | - | **-** | 23 | - | POS +$12.1M | - | 30 | 30 | -$499k | - | out (clean 32, ADX 62, RVol 1.0) |
| 17 | **SPY** | 758.69 | - | **-** | 22 | - | NEG -$2.4B | 761.38 | 760 | 750 | -$34.8M | +$0 bull / -$246k bear | out (clean 32, ADX 52, RVol 0.5) |
| 18 | **BABA** | 101.31 | - | **-** | 22 | - | NEG -$16.9M | 106.69 | 110 | 101 | +$404k | - | out (clean 29, ADX 34, RVol 0.4) |
| 19 | **AAPL** | 353.62 | - | **-** | 20 | - | POS +$1.4B | 341.79 | 355 | 350 | -$958k | +$28k bull / +$0 bear | out (clean 27, ADX 46, RVol 0.5) |
| 20 | **COIN** | 137.05 | - | **-** | 19 | - | POS +$25.1M | - | 141 | 135 | -$55k | +$0 bull / -$72k bear | out (clean 28, ADX 32, RVol 1.0) |
| 21 | **META** | 638.81 | - | **-** | 17 | - | POS +$250.9M | 624.79 | 650 | 635 | +$1.7M | +$0 bull / -$501k bear | out (clean 31, ADX 20, RVol 0.8) |
| 22 | **GOOGL** | 291.33 | - | **-** | 11 | - | POS +$53.0M | 289.17 | 300 | 290 | +$211k | - | out (clean 28, ADX 52, RVol 1.1) |
| 23 | **IWM** | 282.69 | - | **-** | 10 | - | NEG -$60.8M | 282.93 | 285 | 270 | -$1.6M | - | out (clean 34, ADX 41, RVol 0.3) |
| 24 | **SHOP** | 148.44 | - | **-** | 9 | - | POS +$3.6M | 144.24 | 150 | 140 | +$2k | - | out (clean 33, ADX 35, RVol 0.2) |
| 25 | **MSTR** | 122.42 | - | **-** | 7 | - | POS +$938k | 122.19 | 133 | 120 | +$297k | - | out (clean 28, ADX 20, RVol 0.8) |
| 26 | **CRM** | 216.12 | - | **-** | 6 | - | NEG -$13.2M | - | 230 | 220 | +$253 | - | out (clean 30, ADX 28, RVol 0.6) |
| 27 | **NFLX** | 63.47 | - | **-** | 5 | - | NEG -$11.9M | 64.4 | 65 | 65 | +$11k | - | out (clean 26, ADX 15, RVol 0.8) |

## Big prints this scan (150)
- **QQQ** PUT 660 2026-11-13 (2DTE): 13,412 @ 0.45 = **+$604k** BUY | vol 21,102 / OI 24,570
- **TSLA** PUT 392.5 2026-11-13 (2DTE): 718 @ 5.75 = **+$413k** BUY | vol 4,778 / OI 294
- **QQQ** PUT 682 2026-11-11 (0DTE): 13,412 @ 0.30 = **+$402k** BUY | vol 65,879 / OI 155
- **MU** CALL 780 2026-11-11 (0DTE): 100 @ 31.05 = **+$310k** SELL | vol 14,516 / OI 2,052
- **TSLA** PUT 392.5 2026-11-13 (2DTE): 496 @ 5.80 = **+$288k** BUY | vol 4,778 / OI 294
- **AMD** PUT 550 2026-11-11 (0DTE): 287 @ 9.00 = **+$258k** BUY | vol 2,636 / OI 8
- **TSLA** PUT 392.5 2026-11-13 (2DTE): 431 @ 5.60 = **+$241k** BUY | vol 4,778 / OI 294
- **AMD** CALL 535 2026-11-11 (0DTE): 198 @ 11.50 = **+$228k** SELL | vol 12,944 / OI 268
- **AMD** PUT 545 2026-11-16 (5DTE): 100 @ 16.83 = **+$168k** BUY | vol 163 / OI 10
- **MU** CALL 805 2026-11-11 (0DTE): 140 @ 9.13 = **+$128k** SELL | vol 18,497 / OI 820
- **QQQ** CALL 687 2026-11-11 (0DTE): 418 @ 3.05 = **+$127k** SELL | vol 95,200 / OI 753
- **QQQ** CALL 687 2026-11-11 (0DTE): 478 @ 2.65 = **+$127k** SELL | vol 95,200 / OI 753
- **MU** CALL 805 2026-11-11 (0DTE): 140 @ 9.00 = **+$126k** SELL | vol 18,497 / OI 820
- **MU** CALL 805 2026-11-11 (0DTE): 136 @ 9.13 = **+$124k** SELL | vol 18,497 / OI 820
- **MU** CALL 805 2026-11-11 (0DTE): 134 @ 9.15 = **+$123k** SELL | vol 18,497 / OI 820

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 731 2026-11-12 (1DTE): 942 traded vs OI 280
- **SPY** PUT 710 2026-11-19 (8DTE): 511 traded vs OI 317
- **SPY** PUT 750 2026-11-25 (14DTE): 545 traded vs OI 0
- **QQQ** CALL 689 2026-11-13 (2DTE): 1,554 traded vs OI 1,412
- **QQQ** CALL 690 2026-11-16 (5DTE): 910 traded vs OI 880
- **QQQ** CALL 691 2026-11-13 (2DTE): 684 traded vs OI 658
- **QQQ** PUT 641 2026-11-11 (0DTE): 548 traded vs OI 301
- **IWM** PUT 268 2026-11-27 (16DTE): 4,013 traded vs OI 1,162
- **IWM** PUT 261 2026-11-27 (16DTE): 4,002 traded vs OI 596
- **NVDA** CALL 187.5 2026-11-20 (9DTE): 1,128 traded vs OI 941
- **NVDA** CALL 172.5 2026-11-27 (16DTE): 611 traded vs OI 97
- **TSLA** CALL 370 2026-11-11 (0DTE): 1,275 traded vs OI 1,238
- **AMD** CALL 605 2026-11-11 (0DTE): 656 traded vs OI 0
- **AMD** CALL 547.5 2026-11-13 (2DTE): 514 traded vs OI 390
- **AMD** PUT 502.5 2026-11-11 (0DTE): 1,813 traded vs OI 1,806

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
