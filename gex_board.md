# GEX + FLOW SCAN - Fri Nov 13, 03:35 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (13)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 12:45 | **HOOD** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/13 78C | 0.58 | 0.44 | +12% (3m) | **-24%** (done) | +75% | 79 |
| 11:30 | **GOOGL** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/13 292.5P | 0.56 | 0.18 | +23% (10m) | **-68%** (done) | +237% | 290.96 |
| 11:15 | **ARM** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/13 180P | 0.79 | 0.03 | +18% (40m) | **-96%** (done) | +122% | 180 |
| 11:14 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/13 667P | 0.70 | 0.17 | +59% (9m) | **-76%** (done) | +21% | 672.05 hit |
| 10:36 | **SPY** | **PUTS** | 1m FAILED POP (R3 R4) | 11/13 743P | 0.61 | 0.22 | +13% (1m) | **-64%** (done) | +46% | 747.53 |
| 10:17 | **QQQ** | **CALLS** | 1m WHIPSAW (R1 R2) | 11/13 683C | 0.75 | 0.18 | -1% (0m) | **-76%** (done) | +60% | 678.58 |
| 10:15 | **ARM** | **PUTS** | FLIP CROSS down into negative gamma | 11/13 182.5P | 0.74 | 1.47 | +169% (50m) | **+99%** (done) | +96% | 183.6 hit |
| 10:15 | **ORCL** | **CALLS** | FLIP CROSS up into positive gamma | 11/13 124C | 0.65 | 0.35 | +89% (28m) | **-46%** (done) | +66% | 123.68 hit |
| 10:10 | **ORCL** | **PUTS** | FLIP CROSS down into negative gamma | 11/13 120P | 0.46 | 0.15 | +7% (5m) | **-67%** (done) | +63% | 121.25 |
| 10:05 | **GOOGL** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/13 297.5P | 0.74 | 3.42 | +396% (33m) | **+362%** (done) | +288% | 295 hit |
| 09:55 | **BABA** | **PUTS** | FLOW SURGE | 11/13 94P | 0.51 | 0.43 | +8% (43m) | **-16%** (done) | +49% | 93.36 |
| 09:45 | **UBER** | **CALLS** | TREND + FLOW | 11/13 70C | 0.59 | 0.06 | +0% (1m) | **-90%** (done) | +32% | 70.7 |
| 09:45 | **ORCL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/13 127C | 0.46 | 0.22 | +22% (2m) | **-52%** (done) | +48% | 126.38 |

## 1m RULES on SPY / QQQ - loose (5 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 15:32:08 ET, last candle SPY 15:31, QQQ 15:31 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 13:26 | QQQ | 1m AGREE FLIP | FULL | CALLS | up | logged (agree flip) |
| 11:13 | QQQ | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | **FIRE** QQQ261113P00667000 |
| 11:02 | QQQ | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |
| 10:35 | SPY | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | **FIRE** SPY261113P00743000 |
| 10:16 | QQQ | 1m WHIPSAW | R1 R2 | CALLS | TURNING your way | **FIRE** QQQ261113C00683000 |

## Flow surges NOT fired - price disagreed (40 today, last 5)
- 12:25 ARM PUTS: over EMA 20 - flow says one way, price says the other
- 11:45 HOOD CALLS: price -0.30 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 11:40 HOOD CALLS: under EMA 20 - flow says one way, price says the other
- 11:35 HOOD CALLS: under EMA 20 - flow says one way, price says the other
- 11:25 HOOD CALLS: price -0.54 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **GOOGL** | 295.25 | PINNED between the walls (positive gamma) - chop | **-** | 37 | - | POS +$199.9M | 291.63 | 295 | 295 | +$20.1M | +$0 bull / -$60k bear | out (clean 30, ADX 11, RVol 0.6) |
| 2 | **META** | 640.69 | PINNED between the walls (positive gamma) - chop | **-** | 31 | - | POS +$216.4M | 633.28 | 640 | 640 | -$1.9M | +$213k bull / -$54k bear | out (clean 30, ADX 25, RVol 0.9) |
| 3 | **MU** | 770.85 | PINNED between the walls (positive gamma) - chop | **-** | 31 | - | POS +$33.8M | 767.49 | 770 | 770 | +$63.6M | +$2.1M bull / -$567k bear | out (clean 30, ADX 22, RVol 0.5) |
| 4 | **TSLA** | 390.14 | PINNED between the walls (positive gamma) - chop | **-** | 30 | - | POS +$421.2M | - | 390 | 390 | +$50.2M | +$7.5M bull / +$0 bear | out (clean 28, ADX 10, RVol 0.7) |
| 5 | **AMD** | 530.17 | PINNED between the walls (positive gamma) - chop | **-** | 30 | - | POS +$52.0M | 518.44 | 530 | 530 | +$49.7M | +$1.4M bull / +$0 bear | out (clean 35, ADX 20, RVol 0.5) |
| 6 | **MSFT** | 524.41 | PINNED between the walls (positive gamma) - chop | **-** | 25 | - | POS +$154.9M | 522.69 | 525 | 525 | +$77k | +$54k bull / -$54k bear | out (clean 30, ADX 7, RVol 0.5) |
| 7 | **AAPL** | 356.31 | - | **-** | 20 | - | POS +$1.3B | 348.19 | 355 | 355 | +$13.1M | +$318k bull / +$0 bear | out (clean 30, ADX 27, RVol 1.2) |
| 8 | **AVGO** | 345.10 | - | **-** | 20 | - | POS +$84.7M | 330.81 | 350 | 340 | +$18.6M | +$28k bull / -$43k bear | out (clean 36, ADX 11, RVol 0.5) |
| 9 | **ORCL** | 124.96 | FLIP CROSS down into negative gamma | **PUTS** | 20 | none: 50 puts 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (36 contracts' greeks worked out here) | NEG -$4.6M | 125.18 | 125 | 125 | -$1.5M | - | out (clean 32, ADX 18, RVol 0.6) |
| 10 | **SPY** | 752.51 | - | **-** | 18 | - | NEG -$6.6B | 756.12 | 750 | 753 | +$229.7M | +$3.1M bull / +$0 bear | out (clean 33, ADX 16, RVol 0.7) |
| 11 | **QQQ** | 678.53 | - | **-** | 18 | - | NEG -$2.8B | 683.68 | 680 | 680 | +$225.9M | +$1.2M bull / +$0 bear | out (clean 32, ADX 16, RVol 0.6) |
| 12 | **SMH** | 484.82 | - | **-** | 18 | - | NEG -$200.3M | 500.59 | 500 | 485 | +$6.7M | +$162k bull / +$0 bear | out (clean 31, ADX 22, RVol 0.4) |
| 13 | **NVDA** | 161.63 | - | **-** | 18 | - | NEG -$294.8M | - | 175 | 160 | +$83.6M | +$2.7M bull / -$335k bear | out (clean 31, ADX 19, RVol 0.4) |
| 14 | **DELL** | 342.00 | - | **-** | 18 | - | NEG -$14.0M | 353.94 | 337.5 | 340 | +$4.4M | +$34k bull / +$0 bear | out (clean 38, ADX 11, RVol 1.0) |
| 15 | **MSTR** | 112.22 | - | **-** | 18 | - | NEG -$28.3M | - | 120 | 110 | +$2.6M | +$682k bull / +$0 bear | out (clean 32, ADX 30, RVol 0.6) |
| 16 | **AMZN** | 265.83 | - | **-** | 17 | - | POS +$444.4M | 253.85 | 265 | 265 | +$6.6M | +$0 bull / -$157k bear | out (clean 29, ADX 11, RVol 0.5) |
| 17 | **SMCI** | 26.61 | - | **-** | 14 | - | NEG -$2.9M | 27.37 | 27 | 27 | -$1.7M | - | out (clean 34, ADX 24, RVol 0.4) |
| 18 | **ARM** | 189.69 | - | **-** | 13 | - | NEG -$6.0M | 191.11 | 190 | 190 | -$4.0M | - | out (clean 33, ADX 15, RVol 0.2) |
| 19 | **CRM** | 218.47 | - | **-** | 12 | - | NEG -$5.3M | 219.53 | 220 | 220 | +$148k | - | out (clean 27, ADX 27, RVol 1.0) |
| 20 | **UBER** | 69.33 | - | **-** | 11 | - | POS +$3.4M | 69.24 | 70 | 70 | +$315k | - | out (clean 32, ADX 15, RVol 0.9) |
| 21 | **IWM** | 277.19 | - | **-** | 10 | - | NEG -$2.6B | 282.43 | 285 | 277 | +$17.4M | - | out (clean 36, ADX 19, RVol 0.4) |
| 22 | **HOOD** | 78.10 | - | **-** | 10 | - | NEG -$10.0M | 78.69 | 78 | 78 | +$2.5M | - | out (clean 34, ADX 16, RVol 0.8) |
| 23 | **COIN** | 128.66 | - | **-** | 9 | - | NEG -$22.7M | 132.35 | 140 | 130 | +$2.4M | - | out (clean 30, ADX 15, RVol 0.3) |
| 24 | **NFLX** | 62.26 | - | **-** | 7 | - | NEG -$43.7M | 62.97 | 65 | 62 | +$440k | - | out (clean 30, ADX 18, RVol 0.9) |
| 25 | **PLTR** | 168.50 | - | **-** | 5 | - | POS +$109.8M | 160.33 | 167.5 | 165 | +$349k | - | out (clean 29, ADX 13, RVol 1.0) |
| 26 | **BABA** | 93.99 | - | **-** | 5 | - | NEG -$17.2M | - | 100 | 94 | -$165k | - | out (clean 27, ADX 15, RVol 0.4) |
| 27 | **SHOP** | 147.43 | - | **-** | 4 | - | POS +$5.1M | 145.87 | 147 | 140 | +$49k | - | out (clean 30, ADX 9, RVol 0.5) |

## Big prints this scan (58)
- **TSLA** CALL 372.5 2026-11-13 (0DTE): 2,338 @ 18.68 = **+$4.4M** BUY | vol 2,549 / OI 3,109
- **NVDA** CALL 160 2026-11-20 (7DTE): 500 @ 9.57 = **+$478k** BUY | vol 16,364 / OI 4,520
- **SPY** PUT 754 2026-11-13 (0DTE): 3,922 @ 1.09 = **+$427k** SELL | vol 178,988 / OI 2,617
- **SPY** PUT 756 2026-11-20 (7DTE): 467 @ 7.66 = **+$358k** SELL | vol 2,034 / OI 6,304
- **SPY** PUT 770 2026-11-20 (7DTE): 200 @ 17.30 = **+$346k** SELL | vol 2,122 / OI 21,385
- **MSTR** CALL 116 2026-11-20 (7DTE): 800 @ 3.41 = **+$273k** BUY | vol 6,713 / OI 135
- **QQQ** PUT 680 2026-11-20 (7DTE): 193 @ 10.60 = **+$205k** SELL | vol 12,923 / OI 87,076
- **SPY** PUT 756 2026-11-20 (7DTE): 257 @ 7.66 = **+$197k** SELL | vol 2,034 / OI 6,304
- **QQQ** PUT 710 2026-11-16 (3DTE): 57 @ 29.75 = **+$170k** SELL | vol 178 / OI 36
- **MSTR** CALL 116 2026-11-20 (7DTE): 480 @ 3.41 = **+$164k** BUY | vol 6,713 / OI 135
- **MSTR** CALL 116 2026-11-20 (7DTE): 480 @ 3.41 = **+$164k** BUY | vol 6,713 / OI 135
- **NVDA** CALL 162.5 2026-11-13 (0DTE): 2,100 @ 0.75 = **+$158k** BUY | vol 369,096 / OI 687
- **NVDA** CALL 160 2026-11-13 (0DTE): 500 @ 2.82 = **+$141k** BUY | vol 217,638 / OI 1,997
- **MU** PUT 760 2026-11-20 (7DTE): 50 @ 28.00 = **+$140k** SELL | vol 1,617 / OI 2,048
- **SPY** PUT 756 2026-11-20 (7DTE): 181 @ 7.64 = **+$138k** SELL | vol 2,034 / OI 6,304

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 777 2026-11-18 (5DTE): 1,466 traded vs OI 1,081
- **SPY** PUT 756 2026-11-27 (14DTE): 1,181 traded vs OI 657
- **QQQ** PUT 692 2026-11-13 (0DTE): 1,321 traded vs OI 1,317
- **QQQ** PUT 745 2026-11-20 (7DTE): 1,236 traded vs OI 825
- **QQQ** PUT 740 2026-11-20 (7DTE): 2,874 traded vs OI 2,110
- **QQQ** PUT 735 2026-11-20 (7DTE): 736 traded vs OI 491
- **QQQ** PUT 730 2026-11-19 (6DTE): 2,055 traded vs OI 822
- **QQQ** PUT 743 2026-11-20 (7DTE): 1,557 traded vs OI 1,039
- **QQQ** PUT 742 2026-11-20 (7DTE): 1,500 traded vs OI 1,000
- **NVDA** CALL 177.5 2026-11-20 (7DTE): 9,914 traded vs OI 9,890
- **TSLA** CALL 420 2026-11-20 (7DTE): 10,008 traded vs OI 9,958
- **AAPL** PUT 362.5 2026-11-20 (7DTE): 584 traded vs OI 206
- **AMD** CALL 565 2026-11-20 (7DTE): 1,074 traded vs OI 1,066
- **AMZN** CALL 282.5 2026-11-25 (12DTE): 708 traded vs OI 23
- **NFLX** CALL 62.5 2026-11-20 (7DTE): 1,573 traded vs OI 1,553

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
