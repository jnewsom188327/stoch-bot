# GEX + FLOW SCAN - Wed Nov 11, 11:20 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (11)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:05 | **MSFT** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/11 525C | 0.64 | 0.32 | +2% (1m) | **-50%** | +363% | 527.5 |
| 10:45 | **AVGO** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/11 345P | 0.78 | 0.22 | +6% (1m) | **-72%** | +149% | 345 |
| 10:35 | **MSFT** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/11 525C | 0.76 | 0.32 | +96% (9m) | **-58%** | +343% | 527.5 |
| 10:20 | **AVGO** | **CALLS** | TREND + FLOW | 11/11 355C | 0.71 | 0.70 | +127% (38m) | **-1%** | +280% | 356.78 |
| 10:15 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/11 282C | 0.65 | 1.05 | +72% (56m) | **+62%** (done) | +66% | 282.84 hit |
| 10:05 | **NVDA** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/11 175C | 0.76 | 1.54 | +142% (51m) | **+103%** (done) | +58% | 175 hit |
| 09:50 | **GOOGL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/11 292.5C | 0.51 | 0.62 | +39% (28m) | **+22%** (done) | +82% | 291.86 |
| 09:45 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/11 282C | 0.68 | 0.64 | +85% (6m) | **-6%** (done) | +68% | 282.96 |
| 09:45 | **QQQ** | **CALLS** | FLOW SURGE | 11/11 690C | 0.63 | 1.23 | +103% (59m) | **+95%** (done) | +171% | 689.78 |
| 09:39 | **QQQ** | **CALLS** | 1m WHIPSAW (R1 R5) | 11/11 693C | 0.52 | 0.29 | -10% (0m) | **-44%** (done) | +92% | 690.43 |
| 09:39 | **SPY** | **CALLS** | 1m WHIPSAW (R1 R5) | 11/11 760C | 0.53 | 0.17 | -2% (0m) | **-68%** (done) | +79% | 758.82 |

## 1m RULES on SPY / QQQ - loose (3 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 11:20:08 ET, last candle SPY 11:19, QQQ 11:19 | no errors
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
| 1 | **MSFT** | 519.92 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 49 | none: 162 calls 0-7DTE > 11 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (74 contracts' greeks worked out here) | POS +$74.2M | 515.06 | 535 | 520 | +$14.2M | +$227k bull / +$0 bear | out (clean 32, ADX 45, RVol 1.2) |
| 2 | **MU** | 816.02 | TREND (flow not with it) | **CALLS** | 46 | none: 149 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (59 contracts' greeks worked out here) | POS +$150.4M | - | 800 | 800 | -$196.2M | +$9.9M bull / -$3.4M bear | LONG (clean 33, ADX 69, RVol 0.8) |
| 3 | **DELL** | 377.11 | TREND (flow not with it) | **CALLS** | 43 | none: 30 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$81k | 384.76 | 380 | 380 | -$2.7M | +$0 bull / -$199k bear | LONG (clean 36, ADX 68, RVol 1.6) |
| 4 | **ARM** | 202.58 | FLOW SURGE | **PUTS** | 42 | none: 17 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (1 contracts' greeks worked out here) | POS +$5.1M | - | 200 | 200 | -$1.6M | +$0 bull / -$56k bear | out (clean 30, ADX 69, RVol 0.8) |
| 5 | **NVDA** | 174.82 | TREND (flow not with it) | **CALLS** | 39 | none: 56 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (22 contracts' greeks worked out here) | NEG -$155.0M | 180.84 | 180 | 175 | -$12.0M | +$2.7M bull / -$498k bear | LONG (clean 34, ADX 34, RVol 1.3) |
| 6 | **SMH** | 509.65 | - | **-** | 28 | - | NEG -$36.8M | - | 500 | 500 | -$3.0M | +$0 bull / -$38k bear | out (clean 31, ADX 48, RVol 1.0) |
| 7 | **AMD** | 551.51 | - | **-** | 28 | - | POS +$140.4M | - | 550 | 500 | -$66.7M | +$7.2M bull / -$1.8M bear | out (clean 33, ADX 47, RVol 1.0) |
| 8 | **AMZN** | 266.25 | TREND (flow not with it) | **PUTS** | 28 | 11/11 265P @ 0.46 (delta 0.29) = est +57% at 265 | POS +$409.4M | - | 270 | 265 | +$4.4M | +$30k bull / +$0 bear | SHORT (clean 33, ADX 29, RVol 1.0) |
| 9 | **AVGO** | 351.92 | - | **-** | 25 | - | POS +$105.3M | - | 350 | 350 | +$6.1M | +$1.4M bull / -$37k bear | out (clean 34, ADX 51, RVol 0.8) |
| 10 | **QQQ** | 690.84 | - | **-** | 24 | - | POS +$284.2M | 689.9 | 700 | 680 | -$105.5M | +$3.5M bull / -$1.5M bear | out (clean 32, ADX 55, RVol 0.6) |
| 11 | **IWM** | 282.89 | - | **-** | 23 | - | POS +$20.2M | 282.94 | 285 | 270 | -$3.3M | +$0 bull / -$297k bear | out (clean 34, ADX 44, RVol 0.3) |
| 12 | **ORCL** | 128.52 | - | **-** | 23 | - | POS +$4.8M | 122.21 | 130 | 125 | -$783k | +$0 bull / -$160k bear | out (clean 29, ADX 52, RVol 1.1) |
| 13 | **BABA** | 101.19 | - | **-** | 23 | - | NEG -$17.3M | 106.53 | 110 | 101 | +$449k | - | out (clean 29, ADX 38, RVol 0.5) |
| 14 | **SPY** | 758.41 | - | **-** | 22 | - | NEG -$2.3B | 761.1 | 760 | 750 | -$40.5M | +$224k bull / -$125k bear | out (clean 32, ADX 52, RVol 0.6) |
| 15 | **GOOGL** | 291.73 | - | **-** | 21 | - | POS +$57.9M | 288.92 | 300 | 290 | +$352k | +$42k bull / -$63k bear | out (clean 28, ADX 55, RVol 1.1) |
| 16 | **TSLA** | 393.59 | - | **-** | 20 | - | POS +$438.8M | - | 400 | 380 | -$9.4M | +$2.7M bull / -$30k bear | out (clean 33, ADX 55, RVol 0.4) |
| 17 | **AAPL** | 353.76 | - | **-** | 20 | - | POS +$1.5B | 340.99 | 355 | 350 | -$950k | +$77k bull / -$88k bear | out (clean 27, ADX 44, RVol 0.5) |
| 18 | **SMCI** | 30.68 | - | **-** | 20 | - | POS +$12.3M | - | 30 | 30 | -$498k | - | out (clean 32, ADX 66, RVol 1.0) |
| 19 | **MSTR** | 122.93 | - | **-** | 18 | - | POS +$2.4M | 122.32 | 133 | 120 | -$675k | +$399k bull / -$273k bear | out (clean 28, ADX 26, RVol 0.7) |
| 20 | **COIN** | 137.24 | - | **-** | 17 | - | POS +$25.3M | - | 141 | 135 | -$7k | +$89k bull / +$0 bear | out (clean 28, ADX 35, RVol 0.6) |
| 21 | **HOOD** | 84.49 | - | **-** | 17 | - | POS +$15.9M | - | 85 | 85 | -$791k | - | out (clean 33, ADX 37, RVol 0.9) |
| 22 | **SHOP** | 149.27 | - | **-** | 17 | - | POS +$3.6M | 144.98 | 150 | 140 | -$19k | - | out (clean 33, ADX 38, RVol 0.6) |
| 23 | **META** | 640.79 | - | **-** | 15 | - | POS +$282.7M | 623.65 | 650 | 635 | -$337k | +$0 bull / -$1.3M bear | out (clean 31, ADX 18, RVol 0.7) |
| 24 | **PLTR** | 172.89 | - | **-** | 15 | - | POS +$75.6M | - | 170 | 180 | +$1.3M | - | out (clean 30, ADX 42, RVol 0.5) |
| 25 | **UBER** | 69.55 | - | **-** | 11 | - | POS +$10.2M | 68.28 | 70 | 70 | +$57k | - | out (clean 30, ADX 20, RVol 0.6) |
| 26 | **CRM** | 217.02 | - | **-** | 10 | - | NEG -$11.6M | - | 230 | 220 | -$26k | - | out (clean 31, ADX 31, RVol 0.4) |
| 27 | **NFLX** | 63.55 | - | **-** | 5 | - | NEG -$13.1M | 64.44 | 65 | 65 | +$13k | - | out (clean 26, ADX 15, RVol 0.9) |

## Big prints this scan (175)
- **QQQ** CALL 700 2026-11-16 (5DTE): 5,000 @ 3.09 = **+$1.5M** MID | vol 6,560 / OI 1,199
- **AMD** CALL 567.5 2026-11-13 (2DTE): 1,470 @ 7.89 = **+$1.2M** BUY | vol 1,752 / OI 221
- **AMD** CALL 575 2026-11-13 (2DTE): 1,470 @ 5.69 = **+$836k** BUY | vol 2,770 / OI 1,572
- **AMD** CALL 545 2026-11-11 (0DTE): 764 @ 9.00 = **+$688k** SELL | vol 17,426 / OI 951
- **MU** CALL 800 2026-11-13 (2DTE): 149 @ 33.65 = **+$501k** BUY | vol 11,258 / OI 5,495
- **META** PUT 652.5 2026-11-18 (7DTE): 201 @ 22.50 = **+$452k** BUY | vol 248 / OI 0
- **QQQ** PUT 690 2026-11-13 (2DTE): 538 @ 4.65 = **+$250k** SELL | vol 3,650 / OI 10,639
- **MU** CALL 820 2026-11-11 (0DTE): 300 @ 8.00 = **+$240k** BUY | vol 32,559 / OI 598
- **MSTR** CALL 121 2026-11-13 (2DTE): 437 @ 4.65 = **+$203k** BUY | vol 3,585 / OI 57
- **QQQ** PUT 692 2026-11-12 (1DTE): 485 @ 4.18 = **+$203k** BUY | vol 2,530 / OI 73
- **DELL** CALL 372.5 2026-11-13 (2DTE): 150 @ 13.25 = **+$199k** SELL | vol 308 / OI 263
- **MU** CALL 800 2026-11-13 (2DTE): 58 @ 31.45 = **+$182k** MID | vol 11,258 / OI 5,495
- **MU** CALL 815 2026-11-11 (0DTE): 132 @ 11.45 = **+$151k** BUY | vol 22,610 / OI 988
- **MU** PUT 820 2026-11-11 (0DTE): 200 @ 7.55 = **+$151k** MID | vol 3,039 / OI 72
- **MU** PUT 820 2026-11-11 (0DTE): 200 @ 7.00 = **+$140k** SELL | vol 3,039 / OI 72

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 789 2026-11-17 (6DTE): 802 traded vs OI 506
- **SPY** PUT 754 2026-11-13 (2DTE): 2,134 traded vs OI 2,043
- **SPY** CALL 768 2026-11-13 (2DTE): 2,335 traded vs OI 2,200
- **SPY** CALL 792 2026-11-17 (6DTE): 801 traded vs OI 672
- **SPY** CALL 796 2026-11-17 (6DTE): 800 traded vs OI 45
- **SPY** CALL 805 2026-11-17 (6DTE): 898 traded vs OI 112
- **SPY** CALL 797 2026-11-17 (6DTE): 1,602 traded vs OI 296
- **QQQ** CALL 694 2026-11-13 (2DTE): 880 traded vs OI 808
- **QQQ** CALL 705 2026-11-12 (1DTE): 1,215 traded vs OI 1,107
- **QQQ** PUT 692 2026-11-13 (2DTE): 662 traded vs OI 377
- **QQQ** CALL 705 2026-11-13 (2DTE): 4,039 traded vs OI 2,865
- **QQQ** CALL 695 2026-11-13 (2DTE): 5,094 traded vs OI 5,024
- **QQQ** CALL 708 2026-11-13 (2DTE): 879 traded vs OI 835
- **QQQ** PUT 694 2026-11-11 (0DTE): 1,150 traded vs OI 92
- **QQQ** PUT 697 2026-11-11 (0DTE): 525 traded vs OI 29

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
