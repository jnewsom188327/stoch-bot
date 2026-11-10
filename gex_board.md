# GEX + FLOW SCAN - Tue Nov 10, 01:30 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (10)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 12:33 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 667P | 0.67 | 0.52 | +170% (8m) | **-22%** | +15% | 668.83 hit |
| 12:22 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 667P | 0.66 | 0.79 | +174% (19m) | **+20%** (done) | +11% | 669.29 hit |
| 11:18 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 668P | 0.74 | 0.69 | +84% (38m) | **-7%** (done) | +18% | 672.3 hit |
| 11:17 | **SPY** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 744P | 0.60 | 0.36 | +38% (32m) | **-40%** (done) | +41% | 746.01 hit |
| 11:12 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 669P | 0.74 | 1.07 | +135% (44m) | **+45%** (done) | +38% | 671.74 hit |
| 11:12 | **SPY** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 744P | 0.64 | 0.38 | +30% (37m) | **-41%** (done) | +40% | 745.88 |
| 11:06 | **SPY** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 744P | 0.68 | 0.60 | +22% (43m) | **-12%** (done) | +49% | 745.54 |
| 10:15 | **IWM** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/10 280P | 0.63 | 1.39 | +232% (36m) | **+121%** (done) | +22% | 280 hit |
| 09:50 | **SPY** | **PUTS** | FLOW SURGE | 11/10 743P | 0.77 | 0.62 | +21% (60m) | **-19%** (done) | +54% | 745.65 |
| 09:45 | **IWM** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/10 279P | 0.52 | 0.95 | +90% (60m) | **+83%** (done) | +87% | 278.66 |

## 1m RULES on SPY / QQQ - loose (9 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 13:30:08 ET, last candle SPY 13:29, QQQ 13:29 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 12:32 | QQQ | 1m FAILED POP | R3 R4 | PUTS | WITH you | **FIRE** QQQ261110P00667000 |
| 12:21 | QQQ | 1m FAILED POP | R3 R4 | PUTS | TURNING your way | **FIRE** QQQ261110P00667000 |
| 11:23 | QQQ | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |
| 11:17 | QQQ | 1m FAILED POP | R3 R4 | PUTS | TURNING your way | **FIRE** QQQ261110P00668000 |
| 11:16 | SPY | 1m FAILED POP | R3 R4 | PUTS | TURNING your way | **FIRE** SPY261110P00744000 |
| 11:14 | QQQ | 1m FAILED POP | R3 R4 | PUTS | TURNING your way | 5-minute cooldown |
| 11:11 | QQQ | 1m FAILED POP | R3 R4 | PUTS | TURNING your way | **FIRE** QQQ261110P00669000 |
| 11:11 | SPY | 1m FAILED POP | R3 R4 | PUTS | TURNING your way | **FIRE** SPY261110P00744000 |
| 11:05 | SPY | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | **FIRE** SPY261110P00744000 |

## Flow surges NOT fired - price disagreed (6 today, last 5)
- 10:15 BABA PUTS: price +0.24 over the last 15 min - flow says one way, price says the other
- 10:10 BABA PUTS: price +0.73 over the last 15 min - flow says one way, price says the other
- 10:00 NFLX CALLS: price -0.14 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:00 AAPL CALLS: price -2.97 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 09:55 BABA CALLS: price -0.98 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **MSFT** | 531.70 | - | **-** | 26 | - | POS +$406.9M | 502.81 | 550 | 500 | +$15.3M | +$114k bull / -$33k bear | out (clean 32, ADX 48, RVol 0.4) |
| 2 | **AAPL** | 348.13 | - | **-** | 22 | - | POS +$425.3M | 336.16 | 350 | 340 | +$17.3M | +$28k bull / +$0 bear | out (clean 28, ADX 13, RVol 0.3) |
| 3 | **GOOGL** | 286.02 | - | **-** | 22 | - | NEG -$32.0M | 289.12 | 300 | 290 | +$3.3M | +$0 bull / -$94k bear | out (clean 30, ADX 29, RVol 0.3) |
| 4 | **AMZN** | 268.62 | - | **-** | 21 | - | POS +$456.5M | - | 270 | 265 | +$9.2M | +$120k bull / +$0 bear | out (clean 32, ADX 26, RVol 0.4) |
| 5 | **DELL** | 326.07 | - | **-** | 20 | - | NEG -$10.4M | - | 350 | 340 | +$1.4M | +$44k bull / -$241k bear | out (clean 34, ADX 36, RVol 0.3) |
| 6 | **ORCL** | 116.47 | - | **-** | 20 | - | NEG -$23.9M | - | 120 | 120 | +$457k | +$29k bull / +$0 bear | out (clean 28, ADX 40, RVol 0.2) |
| 7 | **AMD** | 508.36 | - | **-** | 18 | - | POS +$49.0M | - | 500 | 500 | -$40.9M | +$2.4M bull / +$0 bear | out (clean 33, ADX 26, RVol 0.2) |
| 8 | **PLTR** | 165.42 | - | **-** | 18 | - | POS +$50.0M | - | 165 | 170 | -$570k | +$0 bull / -$27k bear | out (clean 28, ADX 32, RVol 0.2) |
| 9 | **SPY** | 746.35 | - | **-** | 17 | - | NEG -$7.8B | 760.04 | 750 | 730 | +$65.5M | +$101k bull / -$1.4M bear | out (clean 32, ADX 28, RVol 0.3) |
| 10 | **NVDA** | 167.60 | - | **-** | 17 | - | NEG -$155.7M | - | 180 | 170 | +$12.4M | +$1.8M bull / +$0 bear | out (clean 34, ADX 28, RVol 0.7) |
| 11 | **CRM** | 210.04 | - | **-** | 17 | - | NEG -$10.4M | - | 195 | 220 | +$345k | - | out (clean 30, ADX 41, RVol 0.2) |
| 12 | **QQQ** | 669.51 | - | **-** | 16 | - | NEG -$2.2B | 692.29 | 680 | 680 | +$25.8M | +$375k bull / -$263k bear | out (clean 32, ADX 29, RVol 0.2) |
| 13 | **AVGO** | 326.51 | - | **-** | 16 | - | NEG -$16.0M | 342.59 | 340 | 320 | -$8.7M | +$68k bull / +$0 bear | out (clean 32, ADX 11, RVol 0.3) |
| 14 | **MSTR** | 120.25 | - | **-** | 16 | - | NEG -$20.7M | - | 132 | 110 | +$229k | +$0 bull / -$106k bear | out (clean 29, ADX 26, RVol 0.5) |
| 15 | **SHOP** | 143.41 | - | **-** | 16 | - | NEG -$294k | 144.28 | 150 | 140 | +$94k | - | out (clean 32, ADX 47, RVol 1.0) |
| 16 | **TSLA** | 377.39 | - | **-** | 15 | - | POS +$190.7M | - | 400 | 380 | -$5.0M | +$0 bull / -$163k bear | out (clean 32, ADX 18, RVol 0.3) |
| 17 | **META** | 638.24 | - | **-** | 15 | - | POS +$226.1M | 602.57 | 650 | 650 | +$1.4M | +$123k bull / +$0 bear | out (clean 32, ADX 23, RVol 0.3) |
| 18 | **MU** | 706.74 | - | **-** | 15 | - | NEG -$31.8M | - | 750 | 750 | -$10.0M | +$397k bull / -$1.1M bear | out (clean 30, ADX 21, RVol 0.2) |
| 19 | **ARM** | 177.76 | - | **-** | 13 | - | NEG -$4.6M | - | 185 | 185 | -$205k | - | out (clean 28, ADX 23, RVol 1.5) |
| 20 | **HOOD** | 80.28 | - | **-** | 12 | - | POS +$1.5M | 79.2 | 85 | 80 | +$646k | - | out (clean 31, ADX 38, RVol 0.5) |
| 21 | **BABA** | 102.59 | - | **-** | 12 | - | NEG -$9.4M | 106.2 | 110 | 100 | -$67k | - | out (clean 31, ADX 44, RVol 1.4) |
| 22 | **UBER** | 69.48 | - | **-** | 9 | - | POS +$6.3M | 68.36 | 70 | 70 | -$47k | - | out (clean 33, ADX 30, RVol 0.3) |
| 23 | **COIN** | 130.80 | - | **-** | 8 | - | POS +$1.7M | 129.42 | 137 | 135 | +$199k | - | out (clean 29, ADX 31, RVol 0.3) |
| 24 | **SMCI** | 27.46 | - | **-** | 8 | - | POS +$993k | 26.29 | 30 | 25 | -$40k | - | out (clean 30, ADX 34, RVol 0.4) |
| 25 | **NFLX** | 62.72 | - | **-** | 6 | - | NEG -$24.7M | 65.66 | 65 | 60 | -$124k | - | out (clean 30, ADX 24, RVol 0.4) |
| 26 | **IWM** | 279.56 | - | **-** | 5 | - | NEG -$1.1B | 283.28 | 280 | 270 | +$2.2M | - | out (clean 36, ADX 22, RVol 0.2) |
| 27 | **SMH** | 477.43 | - | **-** | 5 | - | NEG -$231.4M | - | 500 | 475 | +$246k | - | out (clean 30, ADX 25, RVol 0.2) |

## Big prints this scan (52)
- **SPY** PUT 752 2026-11-13 (3DTE): 633 @ 8.15 = **+$516k** BUY | vol 2,389 / OI 1,994
- **AMD** CALL 500 2026-11-13 (3DTE): 200 @ 22.00 = **+$440k** BUY | vol 4,927 / OI 2,434
- **SPY** PUT 750 2026-11-13 (3DTE): 350 @ 6.78 = **+$237k** BUY | vol 9,074 / OI 5,505
- **SPY** PUT 750 2026-11-11 (1DTE): 350 @ 5.08 = **+$178k** BUY | vol 21,738 / OI 3,489
- **AMD** CALL 510 2026-11-11 (1DTE): 134 @ 10.10 = **+$135k** BUY | vol 14,231 / OI 407
- **QQQ** PUT 671 2026-11-11 (1DTE): 242 @ 5.49 = **+$133k** BUY | vol 15,216 / OI 170
- **QQQ** CALL 669 2026-11-12 (2DTE): 200 @ 6.53 = **+$131k** SELL | vol 508 / OI 155
- **SPY** PUT 746 2026-11-13 (3DTE): 250 @ 5.02 = **+$126k** BUY | vol 5,517 / OI 1,288
- **SPY** PUT 745 2026-11-16 (6DTE): 200 @ 5.55 = **+$111k** BUY | vol 2,963 / OI 441
- **NVDA** CALL 167.5 2026-11-13 (3DTE): 200 @ 5.00 = **+$100k** BUY | vol 12,159 / OI 18
- **NVDA** CALL 167.5 2026-11-13 (3DTE): 200 @ 5.00 = **+$100k** BUY | vol 12,159 / OI 18
- **MU** CALL 692.5 2026-11-13 (3DTE): 25 @ 32.25 = **+$81k** SELL | vol 285 / OI 47
- **NVDA** CALL 170 2026-11-11 (1DTE): 335 @ 2.00 = **+$67k** BUY | vol 103,646 / OI 252
- **AMD** CALL 510 2026-11-11 (1DTE): 66 @ 10.10 = **+$67k** BUY | vol 14,231 / OI 407
- **NVDA** CALL 165 2026-11-13 (3DTE): 99 @ 6.35 = **+$63k** BUY | vol 5,100 / OI 157

## New unusual volume (traded more than open interest, 500+)
- **QQQ** CALL 682 2026-11-12 (2DTE): 500 traded vs OI 279
- **QQQ** CALL 669 2026-11-12 (2DTE): 508 traded vs OI 155
- **IWM** CALL 291 2026-11-16 (6DTE): 707 traded vs OI 160
- **TSLA** CALL 415 2026-11-20 (10DTE): 527 traded vs OI 0
- **TSLA** CALL 415 2026-11-11 (1DTE): 548 traded vs OI 0
- **AMZN** PUT 272.5 2026-11-20 (10DTE): 501 traded vs OI 65
- **MSTR** PUT 124 2026-11-13 (3DTE): 504 traded vs OI 386

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
