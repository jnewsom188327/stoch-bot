# GEX + FLOW SCAN - Wed Nov 11, 02:40 PM ET
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
Last 1m check 14:40:08 ET, last candle SPY 14:38, QQQ 14:39 | no errors
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
| 1 | **AMD** | 560.87 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 43 | none: 180 puts 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (71 contracts' greeks worked out here) | POS +$136.8M | - | 560 | 550 | -$105.4M | +$673k bull / -$701k bear | out (clean 34, ADX 43, RVol 0.4) |
| 2 | **META** | 636.08 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 40 | none: 204 calls 0-7DTE > 10 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (82 contracts' greeks worked out here) | POS +$176.3M | 630.2 | 650 | 635 | +$4.9M | +$112k bull / -$92k bear | out (clean 30, ADX 41, RVol 0.8) |
| 3 | **AVGO** | 349.16 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 39 | none: 112 puts 0-7DTE > 7 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only -4% at the target (needs +20%) (43 contracts' greeks worked out here) | POS +$93.0M | - | 350 | 340 | +$8.6M | +$347k bull / +$0 bear | out (clean 36, ADX 32, RVol 0.6) |
| 4 | **MSFT** | 521.15 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 35 | none: 166 calls 0-7DTE > 7 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only +15% at the target (needs +20%) (74 contracts' greeks worked out here) | POS +$56.7M | 518.25 | 535 | 520 | +$13.0M | +$0 bull / -$143k bear | out (clean 32, ADX 15, RVol 0.5) |
| 5 | **IWM** | 283.13 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 27 | none: 340 puts 0-7DTE > 16 priced 0.40-0.80 > 6 delta 0.2+ > 6 spread ok > 6 liquid > best one only +0% at the target (needs +20%) (156 contracts' greeks worked out here) | POS +$211.5M | 282.72 | 283 | 270 | -$5.6M | - | out (clean 35, ADX 26, RVol 0.4) |
| 6 | **AAPL** | 354.96 | PINNED between the walls (positive gamma) - chop | **-** | 27 | - | POS +$2.7B | 342.11 | 355 | 355 | -$2k | +$0 bull / -$477k bear | out (clean 28, ADX 29, RVol 0.3) |
| 7 | **MU** | 818.11 | - | **-** | 24 | - | POS +$125.3M | - | 800 | 800 | -$202.4M | +$3.1M bull / -$1.7M bear | out (clean 34, ADX 32, RVol 0.6) |
| 8 | **DELL** | 378.00 | - | **-** | 23 | - | POS +$2.2M | - | 380 | 380 | -$2.3M | +$50k bull / +$0 bear | out (clean 37, ADX 41, RVol 0.6) |
| 9 | **SPY** | 760.59 | - | **-** | 21 | - | NEG -$826.5M | 761.75 | 760 | 750 | -$124.7M | +$7.3M bull / -$2.2M bear | out (clean 33, ADX 36, RVol 0.5) |
| 10 | **QQQ** | 692.64 | - | **-** | 21 | - | POS +$489.2M | 690.26 | 700 | 680 | -$150.4M | +$882k bull / -$1.3M bear | out (clean 32, ADX 33, RVol 0.5) |
| 11 | **SMH** | 511.05 | - | **-** | 20 | - | NEG -$48.4M | - | 500 | 500 | -$2.8M | +$281k bull / +$0 bear | out (clean 31, ADX 35, RVol 0.4) |
| 12 | **NVDA** | 175.36 | - | **-** | 19 | - | NEG -$173.6M | - | 175 | 175 | -$20.1M | +$2.3M bull / -$36k bear | out (clean 35, ADX 30, RVol 0.8) |
| 13 | **SHOP** | 149.41 | - | **-** | 18 | - | POS +$4.0M | 145.11 | 150 | 140 | -$477k | - | out (clean 33, ADX 18, RVol 0.3) |
| 14 | **ORCL** | 129.16 | - | **-** | 17 | - | POS +$3.7M | 124.89 | 130 | 125 | +$237k | +$0 bull / -$298k bear | out (clean 30, ADX 30, RVol 0.4) |
| 15 | **AMZN** | 266.61 | - | **-** | 16 | - | POS +$403.2M | - | 270 | 265 | +$3.4M | +$0 bull / -$91k bear | out (clean 31, ADX 15, RVol 0.6) |
| 16 | **MSTR** | 121.99 | - | **-** | 16 | - | NEG -$6.9M | 123.63 | 133 | 120 | +$1.3M | +$0 bull / -$209k bear | out (clean 28, ADX 19, RVol 0.3) |
| 17 | **ARM** | 204.89 | - | **-** | 16 | - | POS +$5.4M | - | 200 | 200 | -$1.8M | - | out (clean 31, ADX 30, RVol 0.5) |
| 18 | **TSLA** | 392.30 | - | **-** | 15 | - | POS +$428.5M | - | 400 | 380 | -$4.3M | +$2.0M bull / -$246k bear | out (clean 32, ADX 20, RVol 0.3) |
| 19 | **COIN** | 137.52 | - | **-** | 15 | - | POS +$24.8M | - | 141 | 135 | +$28k | +$0 bull / -$50k bear | out (clean 29, ADX 23, RVol 0.4) |
| 20 | **BABA** | 101.73 | - | **-** | 13 | - | NEG -$17.1M | 106.6 | 110 | 101 | +$364k | - | out (clean 29, ADX 17, RVol 0.2) |
| 21 | **SMCI** | 30.68 | - | **-** | 12 | - | POS +$13.1M | - | 30 | 30 | -$591k | - | out (clean 33, ADX 31, RVol 0.5) |
| 22 | **NFLX** | 64.31 | - | **-** | 10 | - | NEG -$2.8M | 64.53 | 65 | 65 | -$283k | - | out (clean 28, ADX 22, RVol 1.0) |
| 23 | **PLTR** | 173.19 | - | **-** | 9 | - | POS +$79.4M | - | 170 | 170 | +$1.6M | - | out (clean 29, ADX 25, RVol 0.3) |
| 24 | **HOOD** | 85.27 | - | **-** | 9 | - | POS +$15.5M | - | 85 | 85 | -$626k | - | out (clean 34, ADX 26, RVol 0.5) |
| 25 | **UBER** | 71.04 | - | **-** | 9 | - | POS +$20.8M | 68.35 | 70 | 70 | -$17k | - | out (clean 32, ADX 43, RVol 0.5) |
| 26 | **GOOGL** | 294.36 | - | **-** | 8 | - | POS +$101.4M | 290.63 | 300 | 290 | -$829k | - | out (clean 30, ADX 36, RVol 0.4) |
| 27 | **CRM** | 217.50 | - | **-** | 7 | - | NEG -$11.5M | - | 230 | 220 | -$57k | - | out (clean 30, ADX 13, RVol 0.3) |

## Big prints this scan (65)
- **AAPL** CALL 345 2026-11-13 (2DTE): 1,099 @ 10.22 = **+$1.1M** MID | vol 1,805 / OI 6,974
- **AAPL** CALL 352.5 2026-11-13 (2DTE): 1,099 @ 4.02 = **+$442k** SELL | vol 7,322 / OI 2,451
- **AMD** CALL 555 2026-11-11 (0DTE): 500 @ 6.00 = **+$300k** MID | vol 31,405 / OI 266
- **AAPL** CALL 355 2026-11-13 (2DTE): 1,099 @ 2.55 = **+$280k** MID | vol 21,068 / OI 10,645
- **SPY** PUT 760 2026-11-13 (2DTE): 592 @ 3.10 = **+$184k** BUY | vol 33,831 / OI 6,054
- **SMH** CALL 500 2026-11-13 (2DTE): 123 @ 14.70 = **+$181k** MID | vol 2,210 / OI 4,456
- **MU** PUT 825 2026-11-11 (0DTE): 200 @ 8.10 = **+$162k** SELL | vol 19,762 / OI 75
- **QQQ** PUT 691 2026-11-12 (1DTE): 441 @ 3.40 = **+$150k** BUY | vol 8,337 / OI 19
- **QQQ** PUT 684 2026-11-12 (1DTE): 1,000 @ 1.30 = **+$130k** BUY | vol 8,527 / OI 32
- **QQQ** CALL 668 2026-11-13 (2DTE): 50 @ 24.80 = **+$124k** SELL | vol 399 / OI 905
- **QQQ** CALL 668 2026-11-13 (2DTE): 50 @ 24.77 = **+$124k** SELL | vol 399 / OI 905
- **QQQ** PUT 689 2026-11-13 (2DTE): 300 @ 3.90 = **+$117k** BUY | vol 2,785 / OI 990
- **NVDA** CALL 180 2026-11-18 (7DTE): 180 @ 6.20 = **+$112k** BUY | vol 8,583 / OI 2,150
- **MU** PUT 820 2026-11-11 (0DTE): 200 @ 5.00 = **+$100k** SELL | vol 43,333 / OI 72
- **MU** CALL 790 2026-11-13 (2DTE): 26 @ 37.27 = **+$97k** MID | vol 3,199 / OI 1,404

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 726 2026-11-13 (2DTE): 983 traded vs OI 981
- **SPY** PUT 769 2026-11-11 (0DTE): 523 traded vs OI 0
- **SPY** PUT 735 2026-11-18 (7DTE): 748 traded vs OI 390
- **QQQ** CALL 722 2026-11-12 (1DTE): 631 traded vs OI 95
- **QQQ** CALL 695 2026-11-17 (6DTE): 519 traded vs OI 314
- **QQQ** PUT 690 2026-11-18 (7DTE): 515 traded vs OI 247
- **QQQ** PUT 685 2026-11-18 (7DTE): 504 traded vs OI 74
- **IWM** CALL 287 2026-11-17 (6DTE): 550 traded vs OI 278
- **IWM** PUT 283 2026-11-18 (7DTE): 645 traded vs OI 62
- **IWM** CALL 288 2026-11-17 (6DTE): 664 traded vs OI 170
- **IWM** CALL 292 2026-11-17 (6DTE): 500 traded vs OI 331
- **SMH** CALL 535 2026-11-20 (9DTE): 2,210 traded vs OI 1,332
- **TSLA** CALL 395 2026-11-20 (9DTE): 3,216 traded vs OI 3,204
- **AAPL** CALL 360 2026-11-13 (2DTE): 16,856 traded vs OI 16,260
- **AAPL** CALL 350 2026-11-16 (5DTE): 501 traded vs OI 353

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
