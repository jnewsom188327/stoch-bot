# GEX + FLOW SCAN - Wed Nov 11, 11:40 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (12)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:40 | **MSFT** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/11 522.5C | 0.73 | 0.72 | -1% (0m) | **-1%** | +146% | 523.2 |
| 11:05 | **MSFT** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/11 525C | 0.64 | 0.24 | +2% (1m) | **-62%** | +363% | 527.5 |
| 10:45 | **AVGO** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/11 345P | 0.78 | 0.09 | +6% (1m) | **-88%** | +149% | 345 |
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
Last 1m check 11:40:08 ET, last candle SPY 11:39, QQQ 11:39 | no errors
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
| 1 | **DELL** | 379.56 | PINNED between the walls (positive gamma) - chop | **-** | 52 | - | POS +$2.0M | - | 380 | 380 | -$3.3M | +$0 bull / -$73k bear | LONG (clean 36, ADX 69, RVol 1.4) |
| 2 | **MSFT** | 519.70 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 46 | 11/11 522.5C @ 0.73 (delta 0.27) = est +146% at 523.2 | POS +$50.7M | 515.35 | 535 | 520 | +$16.2M | +$67k bull / +$0 bear | out (clean 32, ADX 46, RVol 0.7) |
| 3 | **SMCI** | 30.79 | FLOW SURGE | **PUTS** | 41 | 11/13 30P @ 0.54 (delta 0.34) = est +52% at 30 | POS +$12.4M | - | 30 | 30 | -$780k | +$0 bull / -$154k bear | out (clean 32, ADX 68, RVol 1.0) |
| 4 | **ARM** | 204.72 | FLOW SURGE | **PUTS** | 41 | none: 17 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$5.2M | - | 200 | 200 | -$1.7M | +$0 bull / -$47k bear | out (clean 30, ADX 72, RVol 0.8) |
| 5 | **SMH** | 512.01 | FLOW SURGE | **PUTS** | 40 | none: 164 puts 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (70 contracts' greeks worked out here) | NEG -$25.9M | - | 500 | 500 | -$5.1M | +$0 bull / -$1.1M bear | out (clean 31, ADX 51, RVol 0.6) |
| 6 | **MU** | 820.52 | FLOW SURGE | **PUTS** | 37 | none: 145 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (59 contracts' greeks worked out here) | POS +$143.8M | - | 800 | 800 | -$223.0M | +$35k bull / -$10.9M bear | LONG (clean 33, ADX 70, RVol 0.4) |
| 7 | **AMD** | 552.28 | - | **-** | 28 | - | POS +$141.6M | - | 550 | 500 | -$76.5M | +$944k bull / -$2.6M bear | out (clean 33, ADX 48, RVol 0.5) |
| 8 | **QQQ** | 691.85 | - | **-** | 25 | - | POS +$406.8M | 689.89 | 700 | 680 | -$134.5M | +$0 bull / -$2.2M bear | out (clean 32, ADX 56, RVol 0.5) |
| 9 | **PLTR** | 173.01 | - | **-** | 24 | - | POS +$78.0M | - | 170 | 180 | +$1.8M | +$333k bull / -$252k bear | out (clean 29, ADX 40, RVol 0.3) |
| 10 | **AVGO** | 353.44 | - | **-** | 23 | - | POS +$99.6M | - | 350 | 350 | +$5.3M | +$0 bull / -$359k bear | out (clean 34, ADX 52, RVol 0.4) |
| 11 | **SPY** | 759.08 | - | **-** | 22 | - | NEG -$1.9B | 761.37 | 760 | 750 | -$60.0M | +$0 bull / -$3.6M bear | out (clean 32, ADX 52, RVol 0.5) |
| 12 | **UBER** | 69.85 | PINNED between the walls (positive gamma) - chop | **-** | 22 | - | POS +$13.2M | 68.35 | 70 | 70 | +$41k | - | out (clean 31, ADX 20, RVol 0.7) |
| 13 | **GOOGL** | 292.33 | - | **-** | 21 | - | POS +$65.7M | 289.16 | 300 | 290 | -$360k | +$43k bull / +$0 bear | out (clean 28, ADX 54, RVol 0.9) |
| 14 | **ORCL** | 127.83 | - | **-** | 21 | - | POS +$3.1M | 124.57 | 130 | 125 | -$453k | +$117k bull / -$205k bear | out (clean 29, ADX 52, RVol 0.8) |
| 15 | **NVDA** | 175.53 | - | **-** | 20 | - | NEG -$154.1M | - | 180 | 175 | -$20.6M | +$270k bull / -$5.0M bear | out (clean 34, ADX 33, RVol 0.9) |
| 16 | **AMZN** | 266.95 | - | **-** | 20 | - | POS +$422.1M | - | 270 | 265 | +$3.3M | +$0 bull / -$266k bear | out (clean 32, ADX 26, RVol 0.9) |
| 17 | **BABA** | 101.37 | - | **-** | 20 | - | NEG -$17.5M | 106.71 | 110 | 101 | +$388k | - | out (clean 29, ADX 40, RVol 0.3) |
| 18 | **TSLA** | 392.23 | - | **-** | 19 | - | POS +$408.3M | - | 400 | 380 | -$3.1M | +$1.6M bull / +$0 bear | out (clean 32, ADX 49, RVol 0.3) |
| 19 | **AAPL** | 354.01 | - | **-** | 19 | - | POS +$1.6B | 339.62 | 355 | 350 | -$943k | +$0 bull / -$96k bear | out (clean 27, ADX 42, RVol 0.5) |
| 20 | **MSTR** | 122.74 | - | **-** | 19 | - | POS +$1.1M | 122.2 | 133 | 120 | +$373k | +$0 bull / -$174k bear | out (clean 28, ADX 29, RVol 1.3) |
| 21 | **COIN** | 137.31 | - | **-** | 18 | - | POS +$24.6M | - | 141 | 135 | -$37k | +$0 bull / -$226k bear | out (clean 29, ADX 36, RVol 0.5) |
| 22 | **HOOD** | 84.66 | - | **-** | 16 | - | POS +$15.6M | - | 85 | 85 | -$829k | - | out (clean 33, ADX 37, RVol 0.8) |
| 23 | **META** | 640.36 | - | **-** | 14 | - | POS +$289.9M | 624.39 | 650 | 635 | -$1.2M | +$149k bull / -$320k bear | out (clean 31, ADX 15, RVol 0.3) |
| 24 | **IWM** | 282.74 | - | **-** | 13 | - | NEG -$36.2M | 282.85 | 285 | 270 | -$3.5M | - | out (clean 35, ADX 45, RVol 0.3) |
| 25 | **SHOP** | 149.19 | - | **-** | 13 | - | POS +$3.3M | 145.15 | 150 | 140 | +$26k | - | out (clean 33, ADX 38, RVol 0.5) |
| 26 | **CRM** | 217.85 | - | **-** | 12 | - | NEG -$10.8M | - | 230 | 220 | -$49k | - | out (clean 31, ADX 35, RVol 0.6) |
| 27 | **NFLX** | 63.63 | - | **-** | 5 | - | NEG -$12.3M | 64.58 | 65 | 65 | -$29k | - | out (clean 26, ADX 17, RVol 0.7) |

## Big prints this scan (98)
- **MU** CALL 785 2026-11-11 (0DTE): 80 @ 32.00 = **+$256k** SELL | vol 9,596 / OI 277
- **AMD** PUT 550 2026-11-13 (2DTE): 175 @ 12.97 = **+$227k** BUY | vol 887 / OI 154
- **PLTR** CALL 175 2026-11-13 (2DTE): 1,057 @ 2.13 = **+$225k** BUY | vol 10,518 / OI 5,598
- **QQQ** CALL 691 2026-11-12 (1DTE): 495 @ 3.76 = **+$186k** SELL | vol 8,810 / OI 310
- **SPY** CALL 755 2026-11-11 (0DTE): 446 @ 3.95 = **+$176k** SELL | vol 63,147 / OI 1,849
- **NVDA** CALL 177.5 2026-11-16 (5DTE): 401 @ 3.25 = **+$130k** SELL | vol 7,091 / OI 1,501
- **MU** CALL 785 2026-11-11 (0DTE): 38 @ 33.64 = **+$128k** SELL | vol 9,596 / OI 277
- **QQQ** PUT 690 2026-11-12 (1DTE): 357 @ 3.16 = **+$113k** BUY | vol 9,137 / OI 434
- **SPY** CALL 754 2026-11-11 (0DTE): 225 @ 4.75 = **+$107k** SELL | vol 19,269 / OI 989
- **NVDA** PUT 175 2026-11-13 (2DTE): 304 @ 3.50 = **+$106k** BUY | vol 16,469 / OI 10,522
- **TSLA** CALL 392.5 2026-11-11 (0DTE): 456 @ 2.20 = **+$100k** BUY | vol 86,408 / OI 701
- **QQQ** CALL 690 2026-11-11 (0DTE): 500 @ 2.00 = **+$100k** SELL | vol 218,995 / OI 2,827
- **META** PUT 640 2026-11-13 (2DTE): 100 @ 8.30 = **+$83k** MID | vol 1,468 / OI 696
- **TSLA** PUT 392.5 2026-11-13 (2DTE): 150 @ 5.25 = **+$79k** SELL | vol 8,853 / OI 294
- **MU** CALL 780 2026-11-11 (0DTE): 20 @ 38.80 = **+$78k** SELL | vol 14,789 / OI 2,052

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 750 2026-11-13 (2DTE): 11,615 traded vs OI 10,861
- **SPY** PUT 712 2026-11-12 (1DTE): 913 traded vs OI 883
- **SPY** CALL 771 2026-11-12 (1DTE): 512 traded vs OI 350
- **SPY** CALL 791 2026-11-17 (6DTE): 2,299 traded vs OI 37
- **SPY** CALL 759 2026-11-20 (9DTE): 6,498 traded vs OI 1,197
- **QQQ** CALL 707 2026-11-13 (2DTE): 1,217 traded vs OI 1,014
- **QQQ** CALL 698 2026-11-13 (2DTE): 1,065 traded vs OI 1,063
- **QQQ** CALL 695 2026-11-16 (5DTE): 611 traded vs OI 568
- **QQQ** PUT 649 2026-11-11 (0DTE): 661 traded vs OI 245
- **QQQ** PUT 689 2026-11-13 (2DTE): 1,163 traded vs OI 990
- **AMD** PUT 505 2026-11-13 (2DTE): 586 traded vs OI 465
- **COIN** CALL 140 2026-11-13 (2DTE): 3,574 traded vs OI 3,529
- **MU** PUT 760 2026-11-16 (5DTE): 532 traded vs OI 25
- **MU** PUT 740 2026-11-13 (2DTE): 742 traded vs OI 737
- **MU** PUT 825 2026-11-11 (0DTE): 547 traded vs OI 75

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
