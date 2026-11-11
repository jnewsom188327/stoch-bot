# GEX + FLOW SCAN - Wed Nov 11, 01:30 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (12)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:40 | **MSFT** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/11 522.5C | 0.73 | 1.07 | +73% (34m) | **+47%** (done) | +146% | 523.2 |
| 11:05 | **MSFT** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/11 525C | 0.64 | 0.36 | +2% (1m) | **-44%** (done) | +363% | 527.5 |
| 10:45 | **AVGO** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/11 345P | 0.78 | 0.10 | +6% (1m) | **-87%** (done) | +149% | 345 |
| 10:35 | **MSFT** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/11 525C | 0.76 | 0.25 | +96% (9m) | **-67%** (done) | +343% | 527.5 |
| 10:20 | **AVGO** | **CALLS** | TREND + FLOW | 11/11 355C | 0.71 | 0.76 | +127% (38m) | **+7%** (done) | +280% | 356.78 |
| 10:15 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/11 282C | 0.65 | 1.05 | +72% (56m) | **+62%** (done) | +66% | 282.84 hit |
| 10:05 | **NVDA** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/11 175C | 0.76 | 1.54 | +142% (51m) | **+103%** (done) | +58% | 175 hit |
| 09:50 | **GOOGL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/11 292.5C | 0.51 | 0.62 | +39% (28m) | **+22%** (done) | +82% | 291.86 |
| 09:45 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/11 282C | 0.68 | 0.64 | +85% (6m) | **-6%** (done) | +68% | 282.96 |
| 09:45 | **QQQ** | **CALLS** | FLOW SURGE | 11/11 690C | 0.63 | 1.23 | +103% (59m) | **+95%** (done) | +171% | 689.78 |
| 09:39 | **QQQ** | **CALLS** | 1m WHIPSAW (R1 R5) | 11/11 693C | 0.52 | 0.29 | -10% (0m) | **-44%** (done) | +92% | 690.43 |
| 09:39 | **SPY** | **CALLS** | 1m WHIPSAW (R1 R5) | 11/11 760C | 0.53 | 0.17 | -2% (0m) | **-68%** (done) | +79% | 758.82 |

## 1m RULES on SPY / QQQ - loose (3 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 13:30:08 ET, last candle SPY 13:29, QQQ 13:29 | no errors
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
| 1 | **ORCL** | 130.04 | PINNED between the walls (positive gamma) - chop | **-** | 31 | - | POS +$5.7M | 123.03 | 130 | 130 | +$375k | +$50k bull / -$118k bear | out (clean 30, ADX 47, RVol 0.4) |
| 2 | **AAPL** | 355.06 | PINNED between the walls (positive gamma) - chop | **-** | 28 | - | POS +$2.1B | 341.86 | 355 | 355 | +$242k | +$526k bull / -$666k bear | out (clean 27, ADX 34, RVol 0.3) |
| 3 | **AMD** | 564.23 | - | **-** | 28 | - | POS +$143.8M | - | 550 | 550 | -$107.7M | +$0 bull / -$3.0M bear | out (clean 34, ADX 55, RVol 0.3) |
| 4 | **MU** | 823.97 | - | **-** | 27 | - | POS +$153.2M | - | 800 | 800 | -$224.0M | +$742k bull / -$3.3M bear | out (clean 34, ADX 54, RVol 0.3) |
| 5 | **SMH** | 515.86 | - | **-** | 26 | - | NEG -$8.5M | - | 515 | 500 | -$5.4M | +$110k bull / -$122k bear | out (clean 32, ADX 49, RVol 0.3) |
| 6 | **SPY** | 762.14 | - | **-** | 25 | - | NEG -$187.1M | 762.26 | 760 | 750 | -$158.7M | +$0 bull / -$266k bear | out (clean 33, ADX 53, RVol 0.5) |
| 7 | **QQQ** | 695.17 | - | **-** | 24 | - | POS +$931.1M | 690.63 | 700 | 680 | -$184.9M | +$0 bull / -$2.1M bear | out (clean 33, ADX 49, RVol 0.5) |
| 8 | **PLTR** | 173.56 | - | **-** | 22 | - | POS +$79.6M | - | 170 | 180 | +$1.8M | +$0 bull / -$95k bear | out (clean 29, ADX 33, RVol 0.3) |
| 9 | **GOOGL** | 295.55 | - | **-** | 21 | - | POS +$124.7M | 289.28 | 300 | 290 | -$1.7M | +$0 bull / -$161k bear | out (clean 29, ADX 59, RVol 0.7) |
| 10 | **SHOP** | 149.75 | - | **-** | 21 | - | POS +$4.2M | 145.05 | 155 | 140 | -$475k | - | out (clean 33, ADX 28, RVol 0.2) |
| 11 | **AVGO** | 353.24 | - | **-** | 20 | - | POS +$99.9M | - | 350 | 350 | +$5.1M | +$152k bull / +$0 bear | out (clean 35, ADX 35, RVol 0.6) |
| 12 | **ARM** | 207.18 | - | **-** | 20 | - | POS +$5.5M | - | 200 | 200 | -$1.9M | - | out (clean 31, ADX 57, RVol 0.6) |
| 13 | **NVDA** | 177.19 | - | **-** | 19 | - | NEG -$115.5M | 179.79 | 180 | 175 | -$30.1M | +$80k bull / -$1.5M bear | out (clean 34, ADX 32, RVol 0.3) |
| 14 | **MSFT** | 522.25 | - | **-** | 19 | - | POS +$53.2M | 518.6 | 535 | 520 | +$12.6M | +$0 bull / -$374k bear | out (clean 32, ADX 18, RVol 0.4) |
| 15 | **NFLX** | 63.95 | - | **-** | 18 | - | NEG -$6.1M | 64.41 | 65 | 65 | -$185k | +$36k bull / +$0 bear | out (clean 28, ADX 24, RVol 0.7) |
| 16 | **AMZN** | 266.53 | - | **-** | 17 | - | POS +$404.3M | - | 270 | 265 | +$3.9M | +$0 bull / -$55k bear | out (clean 32, ADX 18, RVol 0.4) |
| 17 | **DELL** | 384.00 | - | **-** | 17 | - | POS +$2.4M | - | 380 | 380 | -$4.1M | - | out (clean 37, ADX 58, RVol 0.4) |
| 18 | **SMCI** | 31.05 | - | **-** | 17 | - | POS +$12.6M | - | 30 | 30 | -$753k | - | out (clean 33, ADX 48, RVol 0.5) |
| 19 | **MSTR** | 122.80 | - | **-** | 16 | - | POS +$1.9M | 122.28 | 133 | 120 | +$844k | +$92k bull / +$0 bear | out (clean 28, ADX 20, RVol 0.3) |
| 20 | **TSLA** | 393.45 | - | **-** | 15 | - | POS +$424.7M | - | 400 | 380 | -$5.5M | +$45k bull / -$498k bear | out (clean 31, ADX 20, RVol 0.3) |
| 21 | **META** | 639.62 | - | **-** | 14 | - | POS +$278.6M | 627.13 | 650 | 635 | +$927k | +$134k bull / -$110k bear | out (clean 31, ADX 18, RVol 0.4) |
| 22 | **IWM** | 283.56 | - | **-** | 13 | - | POS +$274.5M | 282.92 | 285 | 270 | -$6.1M | - | out (clean 35, ADX 42, RVol 0.2) |
| 23 | **HOOD** | 85.89 | - | **-** | 13 | - | POS +$16.0M | - | 85 | 85 | -$811k | - | out (clean 34, ADX 38, RVol 0.5) |
| 24 | **BABA** | 101.70 | - | **-** | 12 | - | NEG -$17.1M | 106.49 | 110 | 101 | +$352k | - | out (clean 30, ADX 15, RVol 0.2) |
| 25 | **UBER** | 70.92 | - | **-** | 9 | - | POS +$20.2M | 68.3 | 70 | 70 | -$5k | - | out (clean 32, ADX 46, RVol 0.3) |
| 26 | **CRM** | 216.93 | - | **-** | 7 | - | NEG -$11.2M | - | 230 | 220 | -$35k | - | out (clean 29, ADX 19, RVol 0.5) |
| 27 | **COIN** | 138.20 | - | **-** | 6 | - | POS +$27.7M | - | 141 | 135 | +$88k | - | out (clean 29, ADX 26, RVol 0.5) |

## Big prints this scan (48)
- **MU** CALL 800 2026-11-11 (0DTE): 100 @ 23.40 = **+$234k** SELL | vol 52,356 / OI 2,486
- **NVDA** CALL 175 2026-11-11 (0DTE): 1,000 @ 1.74 = **+$174k** SELL | vol 279,560 / OI 3,333
- **QQQ** CALL 665 2026-11-11 (0DTE): 55 @ 28.92 = **+$159k** SELL | vol 152 / OI 647
- **AMD** CALL 562.5 2026-11-13 (2DTE): 100 @ 13.80 = **+$138k** SELL | vol 1,081 / OI 273
- **AMD** PUT 565 2026-11-11 (0DTE): 298 @ 4.60 = **+$137k** BUY | vol 1,322 / OI 0
- **SMH** CALL 495 2026-11-11 (0DTE): 61 @ 19.93 = **+$122k** SELL | vol 824 / OI 1,817
- **MSFT** CALL 530 2026-11-13 (2DTE): 532 @ 1.90 = **+$101k** SELL | vol 5,926 / OI 1,091
- **PLTR** CALL 175 2026-11-13 (2DTE): 497 @ 1.92 = **+$95k** SELL | vol 12,846 / OI 5,598
- **MU** CALL 830 2026-11-18 (7DTE): 23 @ 30.48 = **+$70k** BUY | vol 134 / OI 73
- **AMD** CALL 570 2026-11-13 (2DTE): 63 @ 10.95 = **+$69k** SELL | vol 2,860 / OI 870
- **NVDA** CALL 182.5 2026-11-13 (2DTE): 500 @ 1.37 = **+$68k** SELL | vol 26,669 / OI 4,853
- **MU** PUT 825 2026-11-13 (2DTE): 30 @ 20.82 = **+$62k** BUY | vol 1,678 / OI 411
- **MU** CALL 785 2026-11-11 (0DTE): 16 @ 39.00 = **+$62k** SELL | vol 9,852 / OI 277
- **AVGO** CALL 355 2026-11-13 (2DTE): 92 @ 5.83 = **+$54k** BUY | vol 2,979 / OI 1,238
- **MU** CALL 800 2026-11-11 (0DTE): 20 @ 25.00 = **+$50k** BUY | vol 52,356 / OI 2,486

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 739 2026-11-12 (1DTE): 945 traded vs OI 878
- **SPY** PUT 764 2026-11-12 (1DTE): 674 traded vs OI 672
- **QQQ** PUT 657 2026-11-12 (1DTE): 597 traded vs OI 594
- **QQQ** PUT 647 2026-11-20 (9DTE): 715 traded vs OI 649
- **QQQ** PUT 670 2026-11-17 (6DTE): 555 traded vs OI 309
- **IWM** PUT 280 2026-12-11 (30DTE): 1,021 traded vs OI 192
- **AMD** CALL 592.5 2026-11-13 (2DTE): 502 traded vs OI 0
- **AMD** CALL 615 2026-11-13 (2DTE): 507 traded vs OI 0
- **AMZN** PUT 267.5 2026-11-16 (5DTE): 540 traded vs OI 40
- **MSFT** PUT 510 2026-11-20 (9DTE): 4,991 traded vs OI 4,323
- **GOOGL** CALL 325 2026-11-20 (9DTE): 600 traded vs OI 0
- **PLTR** PUT 167.5 2026-11-13 (2DTE): 1,774 traded vs OI 1,474
- **COIN** PUT 150 2026-11-20 (9DTE): 639 traded vs OI 0
- **ORCL** PUT 129 2026-11-20 (9DTE): 545 traded vs OI 544
- **HOOD** PUT 84 2026-11-13 (2DTE): 1,032 traded vs OI 940

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
