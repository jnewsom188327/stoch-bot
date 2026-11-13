# GEX + FLOW SCAN - Fri Nov 13, 12:20 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (12)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:30 | **GOOGL** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/13 292.5P | 0.56 | 0.24 | +23% (10m) | **-57%** | +237% | 290.96 |
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

## 1m RULES on SPY / QQQ - loose (4 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 12:20:08 ET, last candle SPY 12:19, QQQ 12:19 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 11:13 | QQQ | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | **FIRE** QQQ261113P00667000 |
| 11:02 | QQQ | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |
| 10:35 | SPY | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | **FIRE** SPY261113P00743000 |
| 10:16 | QQQ | 1m WHIPSAW | R1 R2 | CALLS | TURNING your way | **FIRE** QQQ261113C00683000 |

## Flow surges NOT fired - price disagreed (40 today, last 5)
- 11:45 HOOD CALLS: price -0.30 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 11:40 HOOD CALLS: under EMA 20 - flow says one way, price says the other
- 11:35 HOOD CALLS: under EMA 20 - flow says one way, price says the other
- 11:25 HOOD CALLS: price -0.54 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 11:20 HOOD CALLS: price -0.21 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **HOOD** | 77.79 | RUN: clean trend + negative gamma + flow agrees | **CALLS** | 56 | none: 30 calls 0-7DTE > 2 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only -20% at the target (needs +20%) (23 contracts' greeks worked out here) | NEG -$13.1M | 79.99 | 81 | 80 | +$2.8M | +$0 bull / -$26k bear | LONG (clean 36, ADX 38, RVol 1.1) |
| 2 | **ARM** | 189.05 | FLOW SURGE | **PUTS** | 50 | none: 30 puts 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (27 contracts' greeks worked out here) | NEG -$515k | 189.54 | 200 | 190 | -$3.6M | +$0 bull / -$103k bear | out (clean 33, ADX 42, RVol 1.8) |
| 3 | **GOOGL** | 294.79 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 48 | none: 90 puts 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (43 contracts' greeks worked out here) | POS +$195.2M | 289.64 | 295 | 290 | +$19.5M | +$0 bull / -$63k bear | out (clean 32, ADX 25, RVol 0.8) |
| 4 | **AMZN** | 265.04 | PINNED between the walls (positive gamma) - chop | **-** | 37 | - | POS +$402.5M | 252.48 | 265 | 265 | +$8.7M | +$0 bull / -$190k bear | out (clean 30, ADX 28, RVol 0.6) |
| 5 | **META** | 633.85 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 34 | none: 185 calls 0-7DTE > 8 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (82 contracts' greeks worked out here) | POS +$26.8M | 632.47 | 630 | 635 | +$5.8M | +$0 bull / -$25k bear | out (clean 29, ADX 25, RVol 0.4) |
| 6 | **DELL** | 336.56 | - | **-** | 29 | - | NEG -$9.2M | - | 350 | 340 | +$7.4M | +$0 bull / -$39k bear | out (clean 38, ADX 45, RVol 1.3) |
| 7 | **AVGO** | 344.86 | - | **-** | 27 | - | POS +$78.1M | 332.96 | 350 | 340 | +$19.5M | +$0 bull / -$235k bear | out (clean 36, ADX 31, RVol 0.4) |
| 8 | **AMD** | 523.43 | - | **-** | 24 | - | POS +$31.1M | - | 530 | 530 | +$65.1M | +$1.2M bull / -$1.8M bear | out (clean 36, ADX 43, RVol 0.6) |
| 9 | **QQQ** | 676.38 | - | **-** | 23 | - | NEG -$3.0B | 690.54 | 680 | 680 | +$257.8M | +$0 bull / -$727k bear | out (clean 32, ADX 34, RVol 0.6) |
| 10 | **SMH** | 480.99 | - | **-** | 23 | - | NEG -$354.6M | - | 500 | 475 | +$10.5M | +$0 bull / -$404k bear | out (clean 31, ADX 34, RVol 0.3) |
| 11 | **PLTR** | 167.84 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 22 | none: 26 puts 0-7DTE > 1 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only -14% at the target (needs +20%) (22 contracts' greeks worked out here) | POS +$101.6M | 161.99 | 167.5 | 165 | -$790k | - | out (clean 29, ADX 23, RVol 0.2) |
| 12 | **SPY** | 751.18 | - | **-** | 20 | - | NEG -$8.8B | 760.47 | 750 | 750 | +$253.5M | +$0 bull / -$4.5M bear | out (clean 33, ADX 22, RVol 0.5) |
| 13 | **NVDA** | 160.85 | - | **-** | 20 | - | NEG -$295.6M | - | 175 | 160 | +$102.8M | +$4.2M bull / -$4.2M bear | out (clean 31, ADX 14, RVol 0.5) |
| 14 | **COIN** | 127.65 | - | **-** | 20 | - | NEG -$21.1M | 132.54 | 140 | 130 | +$3.6M | - | out (clean 30, ADX 28, RVol 0.7) |
| 15 | **MU** | 760.28 | - | **-** | 20 | - | NEG -$34.2M | 776.93 | 760 | 750 | +$70.9M | +$286k bull / -$681k bear | out (clean 30, ADX 24, RVol 0.5) |
| 16 | **TSLA** | 391.34 | - | **-** | 18 | - | POS +$403.3M | 367.96 | 400 | 390 | +$45.3M | +$0 bull / -$654k bear | out (clean 29, ADX 13, RVol 0.6) |
| 17 | **AAPL** | 358.21 | - | **-** | 18 | - | POS +$1.3B | 349.1 | 360 | 360 | +$11.4M | +$0 bull / -$422k bear | out (clean 30, ADX 16, RVol 0.4) |
| 18 | **MSTR** | 109.39 | - | **-** | 17 | - | NEG -$42.8M | - | 110 | 110 | +$2.3M | +$0 bull / -$3.7M bear | out (clean 30, ADX 25, RVol 0.5) |
| 19 | **MSFT** | 524.19 | - | **-** | 14 | - | POS +$114.0M | 522.09 | 530 | 520 | -$227k | +$0 bull / -$4.5M bear | out (clean 32, ADX 15, RVol 0.4) |
| 20 | **IWM** | 276.50 | - | **-** | 13 | - | NEG -$2.7B | 282.7 | 285 | 275 | +$19.5M | - | out (clean 36, ADX 22, RVol 0.7) |
| 21 | **UBER** | 69.59 | - | **-** | 13 | - | POS +$16.4M | 69.02 | 70 | 70 | +$267k | - | out (clean 33, ADX 14, RVol 0.4) |
| 22 | **NFLX** | 62.32 | - | **-** | 12 | - | NEG -$42.0M | 63.65 | 65 | 62 | +$527k | - | out (clean 32, ADX 37, RVol 0.8) |
| 23 | **CRM** | 217.54 | - | **-** | 10 | - | NEG -$6.2M | 223.64 | 220 | 220 | +$84k | - | out (clean 28, ADX 21, RVol 0.9) |
| 24 | **SMCI** | 26.28 | - | **-** | 7 | - | NEG -$3.1M | - | 27 | 26 | +$141k | - | out (clean 34, ADX 22, RVol 0.5) |
| 25 | **ORCL** | 123.82 | - | **-** | 7 | - | POS +$8.2M | 121.7 | 125 | 125 | -$929k | - | out (clean 31, ADX 24, RVol 0.4) |
| 26 | **SHOP** | 146.91 | - | **-** | 5 | - | POS +$3.2M | 145.41 | 150 | 140 | +$22k | - | out (clean 31, ADX 16, RVol 0.4) |
| 27 | **BABA** | 94.03 | - | **-** | 5 | - | NEG -$19.9M | - | 100 | 95 | +$30k | - | out (clean 27, ADX 22, RVol 0.3) |

## Big prints this scan (50)
- **MSTR** CALL 112 2026-11-20 (7DTE): 5,000 @ 3.60 = **+$1.8M** SELL | vol 13,825 / OI 0
- **AMD** PUT 542.5 2026-11-20 (7DTE): 100 @ 34.80 = **+$348k** SELL | vol 166 / OI 385
- **AMD** PUT 540 2026-11-20 (7DTE): 100 @ 33.11 = **+$331k** SELL | vol 1,821 / OI 2,289
- **SPY** CALL 758 2026-11-17 (4DTE): 1,539 @ 1.64 = **+$252k** SELL | vol 3,480 / OI 501
- **SPY** PUT 750 2026-11-20 (7DTE): 270 @ 7.21 = **+$195k** BUY | vol 15,595 / OI 55,813
- **AMD** PUT 540 2026-11-13 (0DTE): 100 @ 17.11 = **+$171k** MID | vol 12,695 / OI 1,096
- **SPY** PUT 747 2026-11-20 (7DTE): 270 @ 6.06 = **+$164k** BUY | vol 856 / OI 2,442
- **TSLA** CALL 385 2026-11-16 (3DTE): 198 @ 8.16 = **+$162k** SELL | vol 967 / OI 526
- **AMD** PUT 537.5 2026-11-13 (0DTE): 100 @ 14.57 = **+$146k** MID | vol 4,552 / OI 290
- **TSLA** CALL 380 2026-11-16 (3DTE): 100 @ 11.70 = **+$117k** SELL | vol 1,158 / OI 697
- **NVDA** PUT 155 2026-11-18 (5DTE): 200 @ 5.30 = **+$106k** BUY | vol 4,271 / OI 1,724
- **TSLA** CALL 385 2026-11-13 (0DTE): 198 @ 5.26 = **+$104k** SELL | vol 6,819 / OI 3,082
- **NVDA** PUT 157.5 2026-11-18 (5DTE): 145 @ 6.25 = **+$91k** BUY | vol 2,696 / OI 2,960
- **AAPL** CALL 342.5 2026-11-20 (7DTE): 49 @ 15.79 = **+$77k** SELL | vol 112 / OI 1,007
- **MU** PUT 765 2026-11-16 (3DTE): 34 @ 21.00 = **+$71k** BUY | vol 2,520 / OI 300

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 754 2026-11-18 (5DTE): 510 traded vs OI 386
- **QQQ** PUT 610 2026-11-16 (3DTE): 573 traded vs OI 0
- **QQQ** PUT 678 2026-11-17 (4DTE): 501 traded vs OI 234
- **QQQ** PUT 637 2026-11-16 (3DTE): 522 traded vs OI 185
- **QQQ** PUT 700 2026-12-11 (28DTE): 613 traded vs OI 397
- **AMD** PUT 475 2026-11-16 (3DTE): 651 traded vs OI 0
- **AMD** CALL 567.5 2026-11-16 (3DTE): 501 traded vs OI 122
- **MSFT** PUT 510 2026-11-27 (14DTE): 515 traded vs OI 487
- **NFLX** CALL 62 2026-11-13 (0DTE): 2,055 traded vs OI 1,664
- **SMCI** PUT 24.5 2026-11-13 (0DTE): 676 traded vs OI 641
- **CRM** PUT 215 2026-11-13 (0DTE): 531 traded vs OI 341

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
