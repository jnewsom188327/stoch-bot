# GEX + FLOW SCAN - Wed Nov 11, 11:05 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (11)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:05 | **MSFT** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/11 525C | 0.64 | 0.63 | -2% (0m) | **-2%** | +363% | 527.5 |
| 10:45 | **AVGO** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/11 345P | 0.78 | 0.25 | +6% (1m) | **-68%** | +149% | 345 |
| 10:35 | **MSFT** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/11 525C | 0.76 | 0.67 | +96% (9m) | **-12%** | +343% | 527.5 |
| 10:20 | **AVGO** | **CALLS** | TREND + FLOW | 11/11 355C | 0.71 | 0.94 | +127% (38m) | **+32%** | +280% | 356.78 |
| 10:15 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/11 282C | 0.65 | 1.06 | +69% (49m) | **+63%** | +66% | 282.84 hit |
| 10:05 | **NVDA** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/11 175C | 0.76 | 1.50 | +142% (51m) | **+97%** | +58% | 175 hit |
| 09:50 | **GOOGL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/11 292.5C | 0.51 | 0.62 | +39% (28m) | **+22%** (done) | +82% | 291.86 |
| 09:45 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/11 282C | 0.68 | 0.64 | +85% (6m) | **-6%** (done) | +68% | 282.96 |
| 09:45 | **QQQ** | **CALLS** | FLOW SURGE | 11/11 690C | 0.63 | 1.23 | +103% (59m) | **+95%** (done) | +171% | 689.78 |
| 09:39 | **QQQ** | **CALLS** | 1m WHIPSAW (R1 R5) | 11/11 693C | 0.52 | 0.29 | -10% (0m) | **-44%** (done) | +92% | 690.43 |
| 09:39 | **SPY** | **CALLS** | 1m WHIPSAW (R1 R5) | 11/11 760C | 0.53 | 0.17 | -2% (0m) | **-68%** (done) | +79% | 758.82 |

## 1m RULES on SPY / QQQ - loose (3 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 11:05:08 ET, last candle SPY 11:04, QQQ 11:04 | no errors
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
| 1 | **MSFT** | 521.19 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 51 | 11/11 525C @ 0.64 (delta 0.22) = est +363% at 527.5 | POS +$61.2M | 515.42 | 535 | 520 | +$12.2M | +$496k bull / -$846k bear | out (clean 32, ADX 44, RVol 1.6) |
| 2 | **DELL** | 376.48 | FLOW SURGE | **PUTS** | 47 | none: 30 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$316k | - | 380 | 380 | -$3.0M | +$0 bull / -$141k bear | LONG (clean 36, ADX 68, RVol 0.9) |
| 3 | **HOOD** | 84.83 | PINNED between the walls (positive gamma) - chop | **-** | 45 | - | POS +$14.7M | - | 85 | 85 | -$888k | +$0 bull / -$52k bear | out (clean 33, ADX 39, RVol 0.9) |
| 4 | **AMD** | 552.05 | FLOW SURGE | **PUTS** | 43 | none: 176 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (71 contracts' greeks worked out here) | POS +$130.7M | - | 550 | 500 | -$71.6M | +$0 bull / -$4.9M bear | LONG (clean 33, ADX 47, RVol 1.1) |
| 5 | **MU** | 817.49 | FLOW SURGE | **PUTS** | 43 | none: 145 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (57 contracts' greeks worked out here) | POS +$127.2M | - | 800 | 800 | -$199.7M | +$0 bull / -$14.3M bear | LONG (clean 33, ADX 68, RVol 0.9) |
| 6 | **ARM** | 201.69 | FLOW SURGE | **PUTS** | 42 | none: 16 puts 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$5.0M | - | 200 | 200 | -$1.3M | +$0 bull / -$408k bear | out (clean 30, ADX 66, RVol 0.9) |
| 7 | **AMZN** | 267.07 | TREND (flow not with it) | **PUTS** | 36 | none: 84 puts 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (31 contracts' greeks worked out here) | POS +$428.6M | - | 270 | 265 | +$3.9M | +$100k bull / -$530k bear | SHORT (clean 33, ADX 29, RVol 0.7) |
| 8 | **NVDA** | 175.82 | TREND (flow not with it) | **CALLS** | 34 | 11/11 177.5C @ 0.57 (delta 0.29) = est +347% at 180 | NEG -$147.1M | 185.14 | 180 | 175 | -$25.2M | +$0 bull / -$4.2M bear | LONG (clean 34, ADX 35, RVol 1.5) |
| 9 | **SMH** | 510.18 | - | **-** | 31 | - | NEG -$47.2M | - | 500 | 500 | -$3.0M | +$0 bull / -$276k bear | out (clean 31, ADX 46, RVol 2.0) |
| 10 | **QQQ** | 691.31 | - | **-** | 26 | - | POS +$177.0M | 690.28 | 700 | 680 | -$124.0M | +$0 bull / -$5.0M bear | out (clean 32, ADX 55, RVol 0.6) |
| 11 | **AVGO** | 352.42 | - | **-** | 25 | - | POS +$95.1M | - | 350 | 350 | +$4.5M | +$0 bull / -$269k bear | out (clean 34, ADX 52, RVol 1.2) |
| 12 | **PLTR** | 173.38 | - | **-** | 24 | - | POS +$77.1M | - | 170 | 180 | +$1.1M | +$0 bull / -$29k bear | out (clean 30, ADX 44, RVol 0.4) |
| 13 | **UBER** | 69.33 | - | **-** | 24 | - | POS +$8.5M | 68.36 | 70 | 70 | +$68k | +$32k bull / +$0 bear | out (clean 31, ADX 23, RVol 0.6) |
| 14 | **SPY** | 758.50 | - | **-** | 22 | - | NEG -$2.5B | 761.35 | 760 | 750 | -$43.9M | +$0 bull / -$351k bear | out (clean 32, ADX 52, RVol 0.5) |
| 15 | **TSLA** | 393.94 | - | **-** | 22 | - | POS +$421.2M | - | 400 | 380 | -$18.3M | +$130k bull / -$3.0M bear | out (clean 33, ADX 56, RVol 0.6) |
| 16 | **BABA** | 101.30 | - | **-** | 22 | - | NEG -$16.8M | 106.47 | 110 | 101 | +$405k | - | out (clean 29, ADX 35, RVol 0.4) |
| 17 | **SMCI** | 30.73 | - | **-** | 21 | - | POS +$12.1M | - | 30 | 30 | -$466k | - | out (clean 32, ADX 63, RVol 1.0) |
| 18 | **AAPL** | 353.73 | - | **-** | 20 | - | POS +$1.5B | 341.62 | 355 | 350 | -$1.3M | +$28k bull / -$38k bear | out (clean 27, ADX 46, RVol 0.5) |
| 19 | **COIN** | 137.69 | - | **-** | 18 | - | POS +$25.0M | - | 141 | 135 | -$13k | +$0 bull / -$147k bear | out (clean 28, ADX 34, RVol 0.9) |
| 20 | **META** | 639.93 | - | **-** | 16 | - | POS +$256.5M | 624.56 | 650 | 635 | +$1.0M | +$0 bull / -$501k bear | out (clean 31, ADX 20, RVol 0.8) |
| 21 | **SHOP** | 149.16 | - | **-** | 12 | - | POS +$3.7M | 144.6 | 150 | 140 | -$6k | - | out (clean 33, ADX 35, RVol 0.3) |
| 22 | **IWM** | 282.83 | - | **-** | 11 | - | NEG -$37.0M | 282.91 | 285 | 270 | -$1.7M | - | out (clean 34, ADX 42, RVol 0.3) |
| 23 | **ORCL** | 128.60 | - | **-** | 11 | - | POS +$2.5M | 125.69 | 130 | 125 | +$183k | - | out (clean 29, ADX 52, RVol 0.9) |
| 24 | **GOOGL** | 291.84 | - | **-** | 10 | - | POS +$58.2M | 289.27 | 300 | 290 | +$22k | - | out (clean 28, ADX 53, RVol 1.0) |
| 25 | **MSTR** | 123.12 | - | **-** | 6 | - | POS +$898k | 122.28 | 133 | 120 | +$249k | - | out (clean 28, ADX 22, RVol 0.8) |
| 26 | **CRM** | 216.67 | - | **-** | 6 | - | NEG -$10.9M | - | 230 | 220 | -$3k | - | out (clean 30, ADX 29, RVol 0.3) |
| 27 | **NFLX** | 63.50 | - | **-** | 5 | - | NEG -$11.5M | 64.46 | 65 | 65 | +$4k | - | out (clean 26, ADX 16, RVol 0.8) |

## Big prints this scan (148)
- **QQQ** CALL 707 2026-11-17 (6DTE): 10,000 @ 1.60 = **+$1.6M** SELL | vol 12,091 / OI 745
- **AMD** CALL 530 2026-11-16 (5DTE): 100 @ 28.15 = **+$282k** SELL | vol 513 / OI 131
- **NVDA** CALL 175 2026-11-16 (5DTE): 700 @ 3.90 = **+$273k** SELL | vol 9,219 / OI 1,029
- **MU** CALL 795 2026-11-11 (0DTE): 100 @ 18.96 = **+$190k** SELL | vol 11,717 / OI 466
- **QQQ** CALL 686 2026-11-11 (0DTE): 447 @ 4.03 = **+$180k** SELL | vol 69,027 / OI 593
- **QQQ** CALL 687 2026-11-11 (0DTE): 499 @ 3.15 = **+$157k** SELL | vol 98,452 / OI 753
- **MU** CALL 800 2026-11-11 (0DTE): 100 @ 15.04 = **+$150k** SELL | vol 47,538 / OI 2,486
- **QQQ** CALL 687 2026-11-11 (0DTE): 450 @ 3.34 = **+$150k** SELL | vol 98,452 / OI 753
- **MU** CALL 785 2026-11-11 (0DTE): 50 @ 27.78 = **+$139k** SELL | vol 8,729 / OI 277
- **MU** CALL 785 2026-11-11 (0DTE): 50 @ 27.78 = **+$139k** SELL | vol 8,729 / OI 277
- **MU** CALL 810 2026-11-11 (0DTE): 150 @ 9.05 = **+$136k** SELL | vol 28,596 / OI 513
- **MU** CALL 810 2026-11-11 (0DTE): 150 @ 8.80 = **+$132k** SELL | vol 28,596 / OI 513
- **MU** CALL 810 2026-11-13 (2DTE): 60 @ 21.67 = **+$130k** SELL | vol 2,191 / OI 645
- **NVDA** CALL 175 2026-11-13 (2DTE): 375 @ 3.26 = **+$122k** SELL | vol 33,755 / OI 8,003
- **QQQ** CALL 687 2026-11-11 (0DTE): 337 @ 3.30 = **+$111k** SELL | vol 98,452 / OI 753

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 758 2026-11-16 (5DTE): 514 traded vs OI 341
- **SPY** PUT 752 2026-11-18 (7DTE): 562 traded vs OI 370
- **SPY** CALL 758 2026-11-18 (7DTE): 518 traded vs OI 344
- **QQQ** CALL 704 2026-11-12 (1DTE): 513 traded vs OI 112
- **QQQ** CALL 709 2026-11-11 (0DTE): 521 traded vs OI 93
- **QQQ** PUT 696 2026-11-11 (0DTE): 562 traded vs OI 307
- **QQQ** CALL 688 2026-11-16 (5DTE): 545 traded vs OI 136
- **QQQ** CALL 700 2026-11-16 (5DTE): 1,369 traded vs OI 1,199
- **QQQ** CALL 710 2026-11-19 (8DTE): 529 traded vs OI 378
- **QQQ** CALL 707 2026-11-17 (6DTE): 12,091 traded vs OI 745
- **QQQ** CALL 724 2026-11-23 (12DTE): 519 traded vs OI 0
- **QQQ** CALL 701 2026-11-30 (19DTE): 721 traded vs OI 647
- **NVDA** CALL 175 2026-12-04 (23DTE): 1,085 traded vs OI 1,066
- **TSLA** PUT 370 2026-11-16 (5DTE): 706 traded vs OI 460
- **TSLA** CALL 390 2026-11-27 (16DTE): 1,134 traded vs OI 1,133

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
