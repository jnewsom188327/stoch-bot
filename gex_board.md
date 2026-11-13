# GEX + FLOW SCAN - Fri Nov 13, 12:30 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (12)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:30 | **GOOGL** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/13 292.5P | 0.56 | 0.14 | +23% (10m) | **-75%** | +237% | 290.96 |
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
Last 1m check 12:30:08 ET, last candle SPY 12:29, QQQ 12:29 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
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
| 1 | **AMZN** | 265.43 | PINNED between the walls (positive gamma) - chop | **-** | 37 | - | POS +$430.5M | 252 | 265 | 265 | +$8.8M | +$0 bull / -$34k bear | out (clean 30, ADX 26, RVol 0.5) |
| 2 | **GOOGL** | 295.42 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 37 | none: 90 puts 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (35 contracts' greeks worked out here) | POS +$167.1M | 291.05 | 295 | 290 | +$19.2M | - | out (clean 31, ADX 23, RVol 0.7) |
| 3 | **TSLA** | 390.75 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 36 | none: 124 calls 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (46 contracts' greeks worked out here) | POS +$357.3M | 381.49 | 400 | 390 | +$47.5M | +$614k bull / -$1.4M bear | out (clean 29, ADX 14, RVol 0.6) |
| 4 | **META** | 633.82 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 33 | none: 185 calls 0-7DTE > 8 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (82 contracts' greeks worked out here) | POS +$28.3M | 632.21 | 630 | 635 | +$5.0M | +$32k bull / +$0 bear | out (clean 29, ADX 25, RVol 0.3) |
| 5 | **AVGO** | 345.52 | FLOW SURGE | **CALLS** | 33 | none: 112 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (45 contracts' greeks worked out here) | POS +$85.7M | 335.6 | 350 | 340 | +$19.7M | +$147k bull / -$84k bear | out (clean 36, ADX 29, RVol 0.5) |
| 6 | **MU** | 763.99 | FLIP CROSS down into negative gamma | **PUTS** | 32 | none: 164 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (72 contracts' greeks worked out here) | NEG -$53.7M | 777.61 | 760 | 750 | +$69.5M | +$794k bull / -$1.0M bear | out (clean 30, ADX 22, RVol 0.5) |
| 7 | **DELL** | 338.25 | - | **-** | 27 | - | NEG -$9.0M | - | 350 | 340 | +$7.3M | +$32k bull / +$0 bear | out (clean 38, ADX 42, RVol 0.9) |
| 8 | **AMD** | 525.90 | - | **-** | 23 | - | POS +$24.1M | 518.01 | 530 | 530 | +$65.3M | +$2.5M bull / -$1.1M bear | out (clean 36, ADX 39, RVol 0.5) |
| 9 | **QQQ** | 677.25 | - | **-** | 22 | - | NEG -$3.0B | 689.97 | 680 | 680 | +$261.2M | +$2.7M bull / -$1.1M bear | out (clean 32, ADX 31, RVol 0.5) |
| 10 | **SMH** | 482.45 | - | **-** | 22 | - | NEG -$342.1M | - | 500 | 475 | +$10.5M | +$86k bull / -$83k bear | out (clean 31, ADX 31, RVol 0.3) |
| 11 | **SPY** | 751.73 | - | **-** | 20 | - | NEG -$8.6B | 760.46 | 750 | 750 | +$253.8M | +$5.6M bull / -$3.1M bear | out (clean 33, ADX 21, RVol 0.4) |
| 12 | **NVDA** | 161.46 | - | **-** | 20 | - | NEG -$308.0M | - | 175 | 160 | +$100.4M | +$305k bull / -$5.9M bear | out (clean 31, ADX 13, RVol 0.5) |
| 13 | **ORCL** | 124.16 | FLIP CROSS down into negative gamma | **PUTS** | 19 | 11/13 124P @ 0.77 (delta 0.47) = est +74% at 122.74 | NEG -$453k | 124.19 | 125 | 125 | -$892k | - | out (clean 31, ADX 21, RVol 0.4) |
| 14 | **ARM** | 189.46 | - | **-** | 19 | - | NEG -$954k | 190.13 | 190 | 190 | -$3.4M | - | out (clean 34, ADX 37, RVol 1.0) |
| 15 | **AAPL** | 357.98 | - | **-** | 18 | - | POS +$1.2B | 348.81 | 360 | 360 | +$12.2M | +$313k bull / -$278k bear | out (clean 30, ADX 15, RVol 0.5) |
| 16 | **COIN** | 127.88 | - | **-** | 18 | - | NEG -$22.0M | 133.05 | 140 | 130 | +$3.6M | - | out (clean 31, ADX 25, RVol 0.5) |
| 17 | **MSTR** | 109.99 | - | **-** | 18 | - | NEG -$46.2M | - | 110 | 110 | +$2.0M | +$0 bull / -$1.9M bear | out (clean 30, ADX 22, RVol 1.0) |
| 18 | **HOOD** | 77.68 | - | **-** | 16 | - | NEG -$13.6M | 80.08 | 78 | 80 | +$2.8M | - | out (clean 36, ADX 34, RVol 1.1) |
| 19 | **PLTR** | 168.08 | - | **-** | 15 | - | POS +$93.3M | 162.96 | 167.5 | 170 | -$524k | +$836k bull / +$0 bear | out (clean 29, ADX 20, RVol 0.2) |
| 20 | **MSFT** | 524.05 | - | **-** | 13 | - | POS +$115.0M | 521.73 | 530 | 520 | -$126k | +$201k bull / -$118k bear | out (clean 31, ADX 13, RVol 0.4) |
| 21 | **UBER** | 69.56 | - | **-** | 13 | - | POS +$14.0M | 69.16 | 70 | 70 | +$274k | - | out (clean 33, ADX 14, RVol 0.4) |
| 22 | **IWM** | 276.56 | - | **-** | 12 | - | NEG -$2.6B | 282.7 | 285 | 275 | +$19.3M | - | out (clean 36, ADX 21, RVol 0.6) |
| 23 | **CRM** | 217.33 | - | **-** | 12 | - | NEG -$4.2M | 218.8 | 220 | 220 | +$118k | - | out (clean 28, ADX 22, RVol 0.9) |
| 24 | **NFLX** | 62.30 | - | **-** | 11 | - | NEG -$34.8M | 63.04 | 65 | 62 | +$501k | - | out (clean 32, ADX 38, RVol 0.6) |
| 25 | **SMCI** | 26.39 | - | **-** | 8 | - | NEG -$3.1M | - | 27 | 25 | +$158k | - | out (clean 34, ADX 21, RVol 0.7) |
| 26 | **SHOP** | 146.96 | - | **-** | 5 | - | POS +$3.1M | 145.65 | 150 | 140 | +$29k | - | out (clean 31, ADX 16, RVol 0.4) |
| 27 | **BABA** | 94.02 | - | **-** | 4 | - | NEG -$19.9M | - | 100 | 95 | +$6k | - | out (clean 27, ADX 20, RVol 0.3) |

## Big prints this scan (128)
- **QQQ** CALL 680 2026-11-20 (7DTE): 1,000 @ 10.17 = **+$1.0M** BUY | vol 5,453 / OI 32,370
- **NVDA** CALL 160 2026-11-16 (3DTE): 1,007 @ 3.55 = **+$357k** SELL | vol 37,647 / OI 919
- **NVDA** CALL 160 2026-11-16 (3DTE): 965 @ 3.50 = **+$338k** SELL | vol 37,647 / OI 919
- **NVDA** CALL 160 2026-11-16 (3DTE): 665 @ 3.55 = **+$236k** SELL | vol 37,647 / OI 919
- **AMD** PUT 500 2026-11-20 (7DTE): 175 @ 13.09 = **+$229k** SELL | vol 3,697 / OI 0
- **AAPL** CALL 355 2026-11-13 (0DTE): 600 @ 3.75 = **+$225k** BUY | vol 5,296 / OI 14,672
- **NVDA** PUT 155 2026-11-20 (7DTE): 307 @ 5.95 = **+$183k** BUY | vol 12,605 / OI 14,723
- **NVDA** CALL 160 2026-11-20 (7DTE): 200 @ 8.88 = **+$178k** SELL | vol 11,788 / OI 4,520
- **QQQ** PUT 676 2026-11-13 (0DTE): 1,000 @ 1.61 = **+$161k** SELL | vol 63,356 / OI 1,842
- **NVDA** CALL 160 2026-11-16 (3DTE): 432 @ 3.55 = **+$153k** SELL | vol 37,647 / OI 919
- **NVDA** CALL 160 2026-11-16 (3DTE): 421 @ 3.55 = **+$149k** SELL | vol 37,647 / OI 919
- **TSLA** CALL 397.5 2026-11-16 (3DTE): 459 @ 3.10 = **+$142k** BUY | vol 3,087 / OI 499
- **NVDA** CALL 160 2026-11-16 (3DTE): 405 @ 3.50 = **+$142k** SELL | vol 37,647 / OI 919
- **NVDA** CALL 160 2026-11-16 (3DTE): 405 @ 3.50 = **+$142k** SELL | vol 37,647 / OI 919
- **AMD** PUT 520 2026-11-13 (0DTE): 500 @ 2.60 = **+$130k** BUY | vol 23,273 / OI 1,013

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 753 2026-11-18 (5DTE): 690 traded vs OI 359
- **SPY** PUT 755 2026-11-18 (5DTE): 1,169 traded vs OI 1,155
- **SPY** PUT 752 2026-11-27 (14DTE): 556 traded vs OI 499
- **QQQ** CALL 688 2026-11-17 (4DTE): 503 traded vs OI 179
- **QQQ** CALL 693 2026-11-23 (10DTE): 560 traded vs OI 46
- **QQQ** PUT 645 2026-11-27 (14DTE): 2,346 traded vs OI 1,377
- **NVDA** PUT 177.5 2026-11-16 (3DTE): 2,208 traded vs OI 1,965
- **NVDA** CALL 152.5 2026-11-13 (0DTE): 503 traded vs OI 257
- **AMD** PUT 482.5 2026-11-16 (3DTE): 502 traded vs OI 0
- **NFLX** CALL 68 2026-11-27 (14DTE): 2,112 traded vs OI 1,849
- **SMCI** CALL 27 2026-11-27 (14DTE): 563 traded vs OI 128
- **MU** CALL 840 2026-11-16 (3DTE): 586 traded vs OI 351
- **MU** CALL 815 2026-11-16 (3DTE): 531 traded vs OI 272

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
