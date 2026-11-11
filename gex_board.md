# GEX + FLOW SCAN - Wed Nov 11, 12:40 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (12)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:40 | **MSFT** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/11 522.5C | 0.73 | 1.04 | +73% (34m) | **+42%** | +146% | 523.2 |
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
Last 1m check 12:40:08 ET, last candle SPY 12:39, QQQ 12:39 | no errors
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
| 1 | **AAPL** | 354.28 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 34 | none: 109 puts 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (51 contracts' greeks worked out here) | POS +$1.8B | 340.56 | 355 | 350 | +$1.5M | +$381k bull / +$0 bear | out (clean 27, ADX 36, RVol 0.3) |
| 2 | **DELL** | 382.70 | TREND (flow not with it) | **CALLS** | 33 | none: 31 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$2.2M | - | 380 | 380 | -$3.6M | - | LONG (clean 37, ADX 67, RVol 0.6) |
| 3 | **MU** | 824.18 | - | **-** | 28 | - | POS +$146.5M | - | 800 | 800 | -$230.6M | +$801k bull / -$3.9M bear | out (clean 34, ADX 65, RVol 0.5) |
| 4 | **AMD** | 559.02 | - | **-** | 27 | - | POS +$145.1M | - | 550 | 550 | -$83.2M | +$0 bull / -$2.5M bear | out (clean 34, ADX 48, RVol 0.3) |
| 5 | **SMH** | 516.13 | - | **-** | 26 | - | NEG -$24.4M | - | 500 | 500 | -$5.1M | +$0 bull / -$61k bear | out (clean 32, ADX 56, RVol 0.4) |
| 6 | **QQQ** | 694.49 | - | **-** | 25 | - | POS +$881.8M | 690.45 | 700 | 680 | -$173.3M | +$0 bull / -$329k bear | out (clean 33, ADX 57, RVol 0.6) |
| 7 | **SPY** | 761.12 | - | **-** | 24 | - | NEG -$526.3M | 761.92 | 760 | 750 | -$136.1M | +$0 bull / -$279k bear | out (clean 32, ADX 58, RVol 0.4) |
| 8 | **SHOP** | 149.70 | - | **-** | 23 | - | POS +$4.1M | 145.24 | 155 | 140 | -$480k | - | out (clean 33, ADX 41, RVol 0.2) |
| 9 | **ORCL** | 130.51 | - | **-** | 22 | - | POS +$5.4M | 123.41 | 130 | 130 | -$839k | +$0 bull / -$32k bear | out (clean 29, ADX 55, RVol 0.7) |
| 10 | **ARM** | 206.40 | - | **-** | 22 | - | POS +$5.6M | - | 200 | 200 | -$2.0M | - | out (clean 31, ADX 70, RVol 0.9) |
| 11 | **MSFT** | 521.37 | - | **-** | 21 | - | POS +$47.0M | 517.32 | 535 | 520 | +$13.1M | +$52k bull / -$125k bear | out (clean 32, ADX 29, RVol 0.5) |
| 12 | **AVGO** | 356.09 | - | **-** | 21 | - | POS +$108.4M | - | 350 | 350 | +$3.5M | +$0 bull / -$392k bear | out (clean 35, ADX 54, RVol 0.6) |
| 13 | **SMCI** | 31.11 | - | **-** | 21 | - | POS +$12.2M | - | 32 | 30 | -$922k | - | out (clean 33, ADX 65, RVol 0.7) |
| 14 | **NVDA** | 176.91 | - | **-** | 20 | - | NEG -$128.2M | 182.43 | 180 | 175 | -$29.9M | +$323k bull / -$2.9M bear | out (clean 34, ADX 34, RVol 0.6) |
| 15 | **GOOGL** | 294.07 | - | **-** | 20 | - | POS +$98.1M | 289.69 | 300 | 290 | -$426k | +$0 bull / -$156k bear | out (clean 28, ADX 55, RVol 0.7) |
| 16 | **COIN** | 138.40 | - | **-** | 19 | - | POS +$28.3M | - | 141 | 135 | -$226k | +$0 bull / -$92k bear | out (clean 29, ADX 32, RVol 0.4) |
| 17 | **TSLA** | 393.71 | - | **-** | 17 | - | POS +$423.4M | - | 400 | 380 | -$7.5M | +$0 bull / -$1.0M bear | out (clean 32, ADX 30, RVol 0.4) |
| 18 | **AMZN** | 266.29 | - | **-** | 17 | - | POS +$408.5M | - | 270 | 265 | +$3.9M | +$52k bull / +$0 bear | out (clean 32, ADX 17, RVol 0.4) |
| 19 | **HOOD** | 85.52 | - | **-** | 15 | - | POS +$15.6M | - | 85 | 85 | -$909k | - | out (clean 33, ADX 39, RVol 0.7) |
| 20 | **IWM** | 283.39 | - | **-** | 14 | - | POS +$199.7M | 283 | 285 | 270 | -$5.4M | - | out (clean 34, ADX 44, RVol 0.4) |
| 21 | **BABA** | 101.64 | - | **-** | 14 | - | NEG -$17.0M | 106.43 | 110 | 101 | +$345k | - | out (clean 30, ADX 24, RVol 0.2) |
| 22 | **META** | 643.49 | - | **-** | 13 | - | POS +$332.7M | 625.18 | 650 | 650 | -$1.8M | +$0 bull / -$38k bear | out (clean 31, ADX 11, RVol 0.2) |
| 23 | **PLTR** | 173.18 | - | **-** | 12 | - | POS +$76.0M | - | 170 | 180 | +$1.7M | - | out (clean 29, ADX 31, RVol 0.2) |
| 24 | **NFLX** | 64.03 | - | **-** | 11 | - | NEG -$6.6M | 64.59 | 65 | 65 | -$228k | - | out (clean 27, ADX 34, RVol 0.6) |
| 25 | **CRM** | 217.38 | - | **-** | 10 | - | NEG -$11.2M | - | 230 | 220 | -$49k | - | out (clean 29, ADX 32, RVol 0.3) |
| 26 | **UBER** | 70.42 | - | **-** | 9 | - | POS +$18.4M | 68.34 | 70 | 70 | +$19k | - | out (clean 33, ADX 40, RVol 0.5) |
| 27 | **MSTR** | 123.17 | - | **-** | 7 | - | POS +$3.2M | 122.22 | 133 | 120 | +$240k | - | out (clean 28, ADX 28, RVol 0.9) |

## Big prints this scan (101)
- **SPY** PUT 780 2026-11-16 (5DTE): 185 @ 19.10 = **+$353k** MID | vol 470 / OI 3
- **AVGO** CALL 360 2026-11-13 (2DTE): 686 @ 4.80 = **+$329k** SELL | vol 6,145 / OI 2,009
- **AMD** PUT 555 2026-11-11 (0DTE): 977 @ 3.00 = **+$293k** BUY | vol 6,541 / OI 0
- **SPY** PUT 763 2026-11-11 (0DTE): 750 @ 2.23 = **+$167k** BUY | vol 9,535 / OI 2,103
- **NVDA** PUT 180 2026-11-13 (2DTE): 300 @ 5.40 = **+$162k** BUY | vol 2,730 / OI 11,023
- **MU** CALL 840 2026-11-13 (2DTE): 88 @ 14.65 = **+$129k** BUY | vol 2,923 / OI 1,388
- **AMD** CALL 560 2026-11-13 (2DTE): 99 @ 13.00 = **+$129k** SELL | vol 3,616 / OI 1,480
- **AMD** CALL 540 2026-11-13 (2DTE): 49 @ 24.00 = **+$118k** SELL | vol 4,226 / OI 1,314
- **QQQ** PUT 690 2026-11-12 (1DTE): 498 @ 2.30 = **+$115k** BUY | vol 16,008 / OI 434
- **SPY** CALL 761 2026-11-12 (1DTE): 448 @ 2.49 = **+$112k** SELL | vol 21,437 / OI 646
- **TSLA** PUT 395 2026-11-13 (2DTE): 137 @ 6.50 = **+$89k** BUY | vol 2,589 / OI 825
- **MU** CALL 825 2026-11-13 (2DTE): 39 @ 21.45 = **+$84k** BUY | vol 2,782 / OI 428
- **NVDA** CALL 177.5 2026-11-13 (2DTE): 235 @ 3.10 = **+$73k** SELL | vol 32,522 / OI 4,621
- **MU** CALL 820 2026-11-13 (2DTE): 30 @ 23.81 = **+$71k** SELL | vol 5,409 / OI 1,308
- **NVDA** CALL 182.5 2026-11-16 (5DTE): 315 @ 2.04 = **+$64k** SELL | vol 8,418 / OI 1,598

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 782 2026-11-17 (6DTE): 3,149 traded vs OI 2,284
- **SPY** CALL 772 2026-11-16 (5DTE): 864 traded vs OI 785
- **SPY** PUT 742 2026-11-16 (5DTE): 1,268 traded vs OI 1,227
- **SPY** CALL 757 2026-11-20 (9DTE): 1,378 traded vs OI 1,376
- **QQQ** CALL 710 2026-11-13 (2DTE): 11,235 traded vs OI 11,081
- **QQQ** CALL 679 2026-11-13 (2DTE): 515 traded vs OI 509
- **QQQ** CALL 710 2026-11-12 (1DTE): 2,121 traded vs OI 1,968
- **QQQ** PUT 668 2026-11-13 (2DTE): 733 traded vs OI 727
- **QQQ** PUT 660 2026-11-23 (12DTE): 501 traded vs OI 124
- **QQQ** CALL 692 2026-11-20 (9DTE): 870 traded vs OI 822
- **QQQ** CALL 730 2026-11-17 (6DTE): 508 traded vs OI 431
- **SMH** CALL 517.5 2026-11-11 (0DTE): 726 traded vs OI 345
- **NVDA** PUT 187.5 2026-11-18 (7DTE): 611 traded vs OI 565
- **NVDA** PUT 177.5 2026-11-13 (2DTE): 4,953 traded vs OI 4,898
- **NVDA** CALL 185 2026-11-27 (16DTE): 3,002 traded vs OI 2,443

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
