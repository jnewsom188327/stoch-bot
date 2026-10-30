# GEX + FLOW SCAN - Fri Oct 30, 10:40 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (2)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:25 | **SMCI** | **PUTS** | FLIP CROSS down into negative gamma | 10/30 32.5P | 0.43 | 0.25 | -12% (1m) | **-42%** | +32% | 32 |
| 10:15 | **AAPL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 10/30 347.5C | 0.50 | 1.30 | +160% (25m) | **+160%** | +104% | 347.56 hit |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:40:08 ET, last candle SPY 10:39, QQQ 10:39 | no errors

## Flow surges NOT fired - price disagreed (32 today, last 5)
- 10:40 SMCI CALLS: under EMA 20 - flow says one way, price says the other
- 10:40 NVDA CALLS: under EMA 20 - flow says one way, price says the other
- 10:35 HOOD CALLS: price -0.27 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:35 SMCI CALLS: price -0.09 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:35 COIN CALLS: price -1.36 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **COIN** | 138.27 | FLOW SURGE | **CALLS** | 61 | none: 49 calls 0-7DTE > 2 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only +14% at the target (needs +20%) (43 contracts' greeks worked out here) | NEG -$12.8M | - | 150 | 140 | +$1.3M | +$120k bull / +$0 bear | out (clean 27, ADX 56, RVol 3.5) |
| 2 | **NVDA** | 207.12 | FLOW SURGE | **CALLS** | 53 | 10/30 207.5C @ 0.80 (delta 0.44) = est +221% at 210 | NEG -$379.2M | 212.24 | 210 | 210 | +$6.6M | +$487k bull / -$257k bear | out (clean 25, ADX 44, RVol 2.2) |
| 3 | **AAPL** | 347.72 | FLOW SURGE | **PUTS** | 50 | none: 81 puts 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (46 contracts' greeks worked out here) | POS +$624.2M | 342.03 | 350 | 345 | -$6.3M | +$0 bull / -$951k bear | out (clean 30, ADX 43, RVol 1.7) |
| 4 | **SMCI** | 32.69 | FLOW SURGE | **CALLS** | 47 | 10/30 32.5C @ 0.45 (delta 0.59) = est +91% at 33.34 | POS +$525k | 32.62 | 35 | 32 | +$516k | +$442k bull / +$0 bear | out (clean 28, ADX 47, RVol 1.5) |
| 5 | **TSLA** | 399.64 | PINNED between the walls (positive gamma) - chop | **-** | 41 | - | POS +$445.0M | 381.3 | 400 | 400 | -$13.8M | +$0 bull / -$2.5M bear | out (clean 29, ADX 30, RVol 1.2) |
| 6 | **ORCL** | 133.18 | FLOW SURGE | **CALLS** | 40 | 10/30 135C @ 0.45 (delta 0.26) = est +105% at 135 | POS +$63.8M | 129.81 | 135 | 130 | +$1.0M | +$425k bull / +$0 bear | out (clean 32, ADX 36, RVol 0.9) |
| 7 | **MSFT** | 524.00 | PINNED between the walls (positive gamma) - chop | **-** | 37 | - | POS +$580.0M | 515.1 | 525 | 525 | -$666k | +$0 bull / -$581k bear | out (clean 27, ADX 26, RVol 1.4) |
| 8 | **META** | 622.66 | FLIP CROSS up into positive gamma | **CALLS** | 35 | none: 195 calls 0-7DTE > 8 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (77 contracts' greeks worked out here) | POS +$15.1M | 621.94 | 625 | 625 | -$1.5M | +$0 bull / -$765k bear | out (clean 28, ADX 28, RVol 0.8) |
| 9 | **ARM** | 205.75 | - | **-** | 30 | - | NEG -$18.2M | - | 220 | 205 | +$417k | - | out (clean 26, ADX 46, RVol 3.5) |
| 10 | **IWM** | 280.26 | - | **-** | 29 | - | NEG -$553.6M | 281.37 | 280 | 270 | +$5.0M | +$185k bull / -$136k bear | out (clean 27, ADX 41, RVol 1.5) |
| 11 | **AMD** | 517.34 | - | **-** | 29 | - | NEG -$76.8M | 526.35 | 527.5 | 500 | +$3.5M | +$701k bull / -$1.5M bear | out (clean 28, ADX 43, RVol 3.1) |
| 12 | **MU** | 898.67 | - | **-** | 29 | - | NEG -$210.8M | 931.96 | 900 | 900 | +$17.4M | +$1.6M bull / -$2.4M bear | out (clean 29, ADX 38, RVol 1.5) |
| 13 | **SPY** | 759.49 | - | **-** | 28 | - | NEG -$13.3B | 772.25 | 770 | 760 | +$43.5M | +$4.5M bull / -$7.4M bear | out (clean 27, ADX 45, RVol 2.2) |
| 14 | **DELL** | 435.38 | - | **-** | 28 | - | NEG -$57.0M | - | 440 | 425 | -$621k | +$56k bull / -$514k bear | out (clean 32, ADX 49, RVol 4.2) |
| 15 | **SMH** | 530.93 | - | **-** | 27 | - | NEG -$538.9M | - | 532.5 | 530 | -$1.2M | +$455k bull / -$2.7M bear | out (clean 28, ADX 48, RVol 2.3) |
| 16 | **PLTR** | 188.59 | - | **-** | 27 | - | NEG -$53.8M | 192.49 | 200 | 190 | -$1.5M | +$341k bull / -$223k bear | out (clean 26, ADX 38, RVol 3.1) |
| 17 | **QQQ** | 696.73 | - | **-** | 26 | - | NEG -$9.6B | 728.15 | 720 | 700 | +$23.1M | +$878k bull / -$5.0M bear | out (clean 28, ADX 49, RVol 6.0) |
| 18 | **HOOD** | 84.24 | - | **-** | 25 | - | NEG -$37.6M | - | 85 | 85 | +$468k | +$0 bull / -$32k bear | out (clean 31, ADX 53, RVol 1.1) |
| 19 | **MSTR** | 129.00 | - | **-** | 23 | - | NEG -$23.8M | 136.17 | 135 | 125 | -$143k | +$47k bull / -$512k bear | out (clean 26, ADX 43, RVol 3.2) |
| 20 | **GOOGL** | 280.22 | - | **-** | 22 | - | NEG -$241.9M | - | 280 | 280 | +$528k | +$28k bull / -$26k bear | out (clean 31, ADX 35, RVol 1.3) |
| 21 | **NFLX** | 62.96 | - | **-** | 22 | - | NEG -$1.9M | 63.02 | 63 | 63 | +$219k | +$313k bull / +$0 bear | out (clean 32, ADX 34, RVol 1.0) |
| 22 | **AMZN** | 239.53 | - | **-** | 21 | - | NEG -$165.5M | 247.45 | 250 | 240 | -$602k | +$0 bull / -$1.8M bear | out (clean 32, ADX 28, RVol 3.4) |
| 23 | **AVGO** | 327.94 | - | **-** | 21 | - | NEG -$129.6M | 344.89 | 330 | 330 | +$828k | - | out (clean 30, ADX 49, RVol 1.0) |
| 24 | **SHOP** | 158.88 | - | **-** | 11 | - | NEG -$13.3M | 164.08 | 160 | 157.5 | +$10k | - | out (clean 25, ADX 44, RVol 1.5) |
| 25 | **BABA** | 98.59 | - | **-** | 9 | - | NEG -$41.8M | 100.19 | 100 | 99 | +$28k | - | out (clean 29, ADX 17, RVol 0.7) |
| 26 | **UBER** | 65.32 | - | **-** | 6 | - | NEG -$28.6M | 66.37 | 70 | 65 | -$6k | - | out (clean 28, ADX 14, RVol 0.8) |
| 27 | **CRM** | 231.79 | - | **-** | 6 | - | NEG -$20.9M | 238.17 | 240 | 230 | -$13k | - | out (clean 27, ADX 18, RVol 1.0) |

## Big prints this scan (162)
- **SMH** PUT 520 2026-11-06 (7DTE): 2,006 @ 9.99 = **+$2.0M** BUY | vol 2,330 / OI 1,783
- **SPY** CALL 758 2026-11-02 (3DTE): 3,000 @ 3.67 = **+$1.1M** SELL | vol 5,960 / OI 147
- **SPY** CALL 759 2026-11-02 (3DTE): 3,000 @ 3.13 = **+$939k** SELL | vol 10,111 / OI 169
- **QQQ** PUT 728 2026-11-06 (7DTE): 225 @ 34.11 = **+$767k** BUY | vol 883 / OI 2,046
- **SPY** PUT 767 2026-11-04 (5DTE): 500 @ 11.00 = **+$550k** BUY | vol 10,637 / OI 29,783
- **SPY** PUT 780 2026-11-06 (7DTE): 241 @ 21.79 = **+$525k** BUY | vol 1,357 / OI 1,351
- **SPY** PUT 780 2026-11-06 (7DTE): 241 @ 21.78 = **+$525k** BUY | vol 1,357 / OI 1,351
- **SPY** PUT 780 2026-11-06 (7DTE): 241 @ 21.78 = **+$525k** BUY | vol 1,357 / OI 1,351
- **SPY** PUT 780 2026-11-06 (7DTE): 213 @ 21.79 = **+$464k** BUY | vol 1,357 / OI 1,351
- **QQQ** CALL 690 2026-11-03 (4DTE): 450 @ 9.25 = **+$416k** SELL | vol 722 / OI 105
- **QQQ** PUT 697 2026-10-30 (0DTE): 800 @ 5.15 = **+$412k** BUY | vol 30,993 / OI 2,680
- **QQQ** CALL 700 2026-11-06 (7DTE): 409 @ 7.57 = **+$310k** SELL | vol 13,946 / OI 1,011
- **SMH** PUT 547.5 2026-10-30 (0DTE): 165 @ 17.80 = **+$294k** BUY | vol 520 / OI 973
- **SMH** PUT 555 2026-10-30 (0DTE): 108 @ 25.33 = **+$274k** BUY | vol 490 / OI 19,582
- **SPY** PUT 767 2026-11-04 (5DTE): 250 @ 10.90 = **+$272k** BUY | vol 10,637 / OI 29,783

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 759 2026-11-04 (5DTE): 988 traded vs OI 979
- **SPY** PUT 747 2026-10-30 (0DTE): 6,986 traded vs OI 3,925
- **SPY** PUT 739 2026-11-02 (3DTE): 601 traded vs OI 141
- **SPY** PUT 752 2026-11-03 (4DTE): 536 traded vs OI 446
- **SPY** PUT 746 2026-10-30 (0DTE): 5,959 traded vs OI 5,584
- **SPY** CALL 791 2026-11-02 (3DTE): 1,395 traded vs OI 1,288
- **SPY** PUT 750 2026-11-04 (5DTE): 1,347 traded vs OI 1,126
- **SPY** CALL 767 2026-11-03 (4DTE): 539 traded vs OI 493
- **SPY** PUT 726 2026-11-02 (3DTE): 909 traded vs OI 717
- **SPY** PUT 742 2026-11-02 (3DTE): 1,361 traded vs OI 1,032
- **SPY** CALL 792 2026-11-02 (3DTE): 861 traded vs OI 354
- **SPY** PUT 780 2026-11-06 (7DTE): 1,357 traded vs OI 1,351
- **QQQ** CALL 702 2026-11-03 (4DTE): 644 traded vs OI 14
- **QQQ** CALL 689 2026-10-30 (0DTE): 561 traded vs OI 74
- **QQQ** CALL 698 2026-11-04 (5DTE): 545 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
