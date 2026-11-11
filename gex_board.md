# GEX + FLOW SCAN - Wed Nov 11, 11:30 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (11)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:05 | **MSFT** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/11 525C | 0.64 | 0.33 | +2% (1m) | **-48%** | +363% | 527.5 |
| 10:45 | **AVGO** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/11 345P | 0.78 | 0.09 | +6% (1m) | **-88%** | +149% | 345 |
| 10:35 | **MSFT** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/11 525C | 0.76 | 0.33 | +96% (9m) | **-57%** | +343% | 527.5 |
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
Last 1m check 11:30:08 ET, last candle SPY 11:29, QQQ 11:29 | no errors
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
| 1 | **MSFT** | 519.75 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 46 | 11/11 522.5C @ 0.78 (delta 0.27) = est +150% at 523.44 | POS +$50.1M | 515.11 | 535 | 520 | +$14.8M | +$63k bull / +$0 bear | out (clean 32, ADX 46, RVol 0.8) |
| 2 | **DELL** | 378.98 | TREND (flow not with it) | **CALLS** | 43 | none: 30 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$1.9M | - | 380 | 380 | -$3.0M | +$0 bull / -$236k bear | LONG (clean 36, ADX 69, RVol 1.6) |
| 3 | **SMCI** | 30.82 | FLOW SURGE | **PUTS** | 40 | 11/13 30P @ 0.55 (delta 0.35) = est +56% at 30 | POS +$12.2M | - | 30 | 30 | -$638k | +$0 bull / -$37k bear | out (clean 32, ADX 67, RVol 0.9) |
| 4 | **MU** | 820.79 | FLOW SURGE | **PUTS** | 38 | none: 145 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (67 contracts' greeks worked out here) | POS +$140.5M | - | 800 | 800 | -$213.3M | +$2.5M bull / -$10.1M bear | LONG (clean 33, ADX 70, RVol 0.5) |
| 5 | **AAPL** | 354.12 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 37 | none: 109 puts 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (51 contracts' greeks worked out here) | POS +$1.7B | 341.94 | 355 | 350 | -$1.6M | +$0 bull / -$58k bear | out (clean 27, ADX 44, RVol 0.5) |
| 6 | **IWM** | 282.89 | FLIP CROSS down into negative gamma | **PUTS** | 34 | 11/11 283P @ 0.50 (delta 0.54) = est +85% at 282.12 | POS +$2.1M | 282.94 | 285 | 270 | -$3.8M | +$0 bull / -$297k bear | out (clean 34, ADX 45, RVol 0.2) |
| 7 | **HOOD** | 84.91 | PINNED between the walls (positive gamma) - chop | **-** | 33 | - | POS +$14.9M | - | 85 | 85 | -$860k | - | out (clean 33, ADX 38, RVol 1.0) |
| 8 | **SMH** | 512.40 | - | **-** | 29 | - | NEG -$39.1M | - | 500 | 500 | -$4.6M | +$0 bull / -$1.0M bear | out (clean 31, ADX 50, RVol 0.6) |
| 9 | **AMD** | 554.48 | - | **-** | 28 | - | POS +$138.3M | - | 550 | 500 | -$74.3M | +$3.3M bull / -$2.4M bear | out (clean 33, ADX 48, RVol 0.6) |
| 10 | **NVDA** | 176.17 | TREND (flow not with it) | **CALLS** | 27 | 11/11 177.5C @ 0.52 (delta 0.31) = est +64% at 177.5 | NEG -$147.6M | - | 180 | 175 | -$18.0M | +$978k bull / -$3.5M bear | LONG (clean 34, ADX 33, RVol 0.9) |
| 11 | **QQQ** | 692.49 | - | **-** | 25 | - | POS +$411.5M | 690.42 | 700 | 680 | -$127.6M | +$250k bull / -$2.0M bear | out (clean 32, ADX 55, RVol 0.5) |
| 12 | **PLTR** | 173.34 | - | **-** | 25 | - | POS +$77.1M | - | 170 | 180 | +$1.4M | +$0 bull / -$175k bear | out (clean 30, ADX 42, RVol 0.5) |
| 13 | **AVGO** | 353.80 | - | **-** | 24 | - | POS +$99.5M | - | 350 | 350 | +$5.4M | +$140k bull / -$294k bear | out (clean 34, ADX 52, RVol 0.7) |
| 14 | **ARM** | 204.53 | - | **-** | 23 | - | POS +$4.9M | - | 200 | 200 | -$1.6M | - | out (clean 30, ADX 71, RVol 0.7) |
| 15 | **SPY** | 759.25 | - | **-** | 22 | - | NEG -$2.0B | 761.5 | 760 | 750 | -$54.3M | +$0 bull / -$3.2M bear | out (clean 32, ADX 53, RVol 0.6) |
| 16 | **ORCL** | 128.32 | - | **-** | 22 | - | POS +$2.9M | 125.08 | 130 | 125 | -$597k | +$117k bull / -$266k bear | out (clean 29, ADX 53, RVol 1.1) |
| 17 | **GOOGL** | 292.34 | - | **-** | 21 | - | POS +$53.1M | 290.23 | 300 | 290 | -$549k | +$42k bull / +$0 bear | out (clean 28, ADX 56, RVol 1.0) |
| 18 | **BABA** | 101.25 | - | **-** | 21 | - | NEG -$16.7M | 106.57 | 110 | 101 | +$402k | - | out (clean 29, ADX 40, RVol 0.5) |
| 19 | **AMZN** | 266.97 | - | **-** | 20 | - | POS +$423.8M | - | 270 | 265 | +$3.2M | +$0 bull / -$229k bear | out (clean 33, ADX 27, RVol 1.0) |
| 20 | **TSLA** | 393.04 | - | **-** | 19 | - | POS +$425.5M | - | 400 | 380 | -$5.6M | +$1.3M bull / +$0 bear | out (clean 32, ADX 53, RVol 0.3) |
| 21 | **COIN** | 137.65 | - | **-** | 18 | - | POS +$25.2M | - | 141 | 135 | -$55k | +$89k bull / +$0 bear | out (clean 29, ADX 36, RVol 0.5) |
| 22 | **MSTR** | 123.71 | - | **-** | 17 | - | POS +$4.0M | 122.24 | 133 | 120 | -$14k | +$399k bull / -$448k bear | out (clean 28, ADX 29, RVol 1.0) |
| 23 | **META** | 641.83 | - | **-** | 15 | - | POS +$304.2M | 625.84 | 650 | 635 | -$1.8M | +$0 bull / -$1.4M bear | out (clean 31, ADX 16, RVol 0.6) |
| 24 | **CRM** | 217.66 | - | **-** | 13 | - | NEG -$11.2M | - | 230 | 220 | -$50k | - | out (clean 31, ADX 34, RVol 0.5) |
| 25 | **SHOP** | 149.39 | - | **-** | 13 | - | POS +$3.1M | 145.07 | 150 | 140 | +$22k | - | out (clean 33, ADX 39, RVol 0.7) |
| 26 | **UBER** | 69.75 | - | **-** | 10 | - | POS +$12.0M | 68.38 | 70 | 70 | +$48k | - | out (clean 31, ADX 19, RVol 0.8) |
| 27 | **NFLX** | 63.56 | - | **-** | 5 | - | NEG -$12.3M | 64.51 | 65 | 65 | -$11k | - | out (clean 26, ADX 16, RVol 0.7) |

## Big prints this scan (156)
- **MU** CALL 785 2026-11-11 (0DTE): 199 @ 28.50 = **+$567k** SELL | vol 9,460 / OI 277
- **TSLA** CALL 390 2026-11-11 (0DTE): 495 @ 4.70 = **+$233k** BUY | vol 82,410 / OI 2,864
- **SMH** PUT 510 2026-11-16 (5DTE): 200 @ 10.00 = **+$200k** BUY | vol 227 / OI 119
- **MU** CALL 785 2026-11-11 (0DTE): 60 @ 28.80 = **+$173k** SELL | vol 9,460 / OI 277
- **MU** CALL 785 2026-11-11 (0DTE): 60 @ 28.80 = **+$173k** SELL | vol 9,460 / OI 277
- **MSTR** CALL 122 2026-11-13 (2DTE): 400 @ 4.20 = **+$168k** MID | vol 1,465 / OI 101
- **NVDA** PUT 175 2026-11-16 (5DTE): 409 @ 4.00 = **+$164k** BUY | vol 2,584 / OI 1,839
- **QQQ** CALL 686 2026-11-11 (0DTE): 327 @ 4.91 = **+$161k** SELL | vol 72,465 / OI 593
- **QQQ** CALL 686 2026-11-11 (0DTE): 318 @ 4.89 = **+$156k** SELL | vol 72,465 / OI 593
- **QQQ** CALL 699 2026-11-13 (2DTE): 755 @ 2.00 = **+$151k** SELL | vol 2,991 / OI 656
- **META** PUT 640 2026-11-13 (2DTE): 171 @ 8.80 = **+$150k** BUY | vol 1,345 / OI 696
- **QQQ** CALL 692 2026-11-12 (1DTE): 468 @ 3.17 = **+$148k** SELL | vol 8,404 / OI 373
- **QQQ** CALL 686 2026-11-11 (0DTE): 284 @ 4.89 = **+$139k** SELL | vol 72,465 / OI 593
- **QQQ** CALL 687 2026-11-11 (0DTE): 362 @ 3.72 = **+$135k** SELL | vol 101,500 / OI 753
- **MSTR** CALL 125 2026-11-13 (2DTE): 500 @ 2.60 = **+$130k** SELL | vol 3,579 / OI 1,342

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 755 2026-11-13 (2DTE): 9,591 traded vs OI 9,468
- **SPY** CALL 835 2026-11-20 (9DTE): 4,197 traded vs OI 0
- **QQQ** CALL 675 2026-11-11 (0DTE): 1,706 traded vs OI 1,701
- **IWM** CALL 287 2026-11-16 (5DTE): 1,302 traded vs OI 1,254
- **IWM** CALL 286 2026-11-16 (5DTE): 877 traded vs OI 864
- **IWM** CALL 283 2026-11-12 (1DTE): 3,031 traded vs OI 2,971
- **NVDA** CALL 192.5 2026-11-23 (12DTE): 513 traded vs OI 0
- **NVDA** CALL 190 2026-12-11 (30DTE): 3,757 traded vs OI 1,702
- **NVDA** CALL 180 2026-12-11 (30DTE): 1,045 traded vs OI 1,026
- **TSLA** PUT 400 2026-11-13 (2DTE): 1,341 traded vs OI 1,312
- **AAPL** PUT 345 2026-11-13 (2DTE): 4,743 traded vs OI 4,670
- **AMD** PUT 515 2026-11-13 (2DTE): 501 traded vs OI 425
- **AMD** CALL 557.5 2026-11-13 (2DTE): 506 traded vs OI 207
- **AMD** CALL 555 2026-11-13 (2DTE): 1,322 traded vs OI 1,168
- **AMD** CALL 552.5 2026-11-13 (2DTE): 662 traded vs OI 245

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
