# GEX + FLOW SCAN - Thu Nov 12, 03:25 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (5)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:35 | **SPY** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/12 754P | 0.59 | 0.17 | +10% (1m) | **-71%** (done) | +70% | 755 |
| 09:50 | **HOOD** | **PUTS** | TREND + FLOW | 11/13 79P | 0.55 | 0.36 | +5% (19m) | **-35%** (done) | +92% | 80 |
| 09:45 | **ORCL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/13 130C | 0.75 | 0.72 | +4% (60m) | **-4%** (done) | +59% | 126.9 |
| 09:45 | **SMCI** | **PUTS** | TREND + FLOW | 11/13 27P | 0.42 | 0.23 | -5% (6m) | **-45%** (done) | +57% | 27 |
| 09:45 | **SPY** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/12 753P | 0.79 | 0.31 | +23% (18m) | **-61%** (done) | +51% | 754.88 |

## 1m RULES on SPY / QQQ - loose (3 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 15:25:08 ET, last candle SPY 15:24, QQQ 15:24 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 14:27 | SPY | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |
| 14:15 | SPY | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | no contract: 90 puts 0-1DTE > 6 priced 0.40-0.80 > 2 delta 0.15+ > 2 spread ok > 2 liquid  |
| 10:03 | SPY | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |

## Flow surges NOT fired - price disagreed (7 today, last 5)
- 12:00 SMCI CALLS: price -0.27 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 11:55 SMCI CALLS: price -0.04 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 11:50 SMCI CALLS: price -0.48 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 11:45 SMCI CALLS: price -0.74 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:30 IWM CALLS: price -0.04 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **GOOGL** | 299.52 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 39 | none: 72 puts 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (6 contracts' greeks worked out here) | POS +$142.5M | 289.11 | 300 | 290 | -$4.9M | +$586k bull / -$626k bear | out (clean 30, ADX 26, RVol 1.0) |
| 2 | **TSLA** | 398.68 | - | **-** | 23 | - | POS +$407.1M | - | 400 | 400 | -$12.7M | +$0 bull / -$4.6M bear | out (clean 29, ADX 33, RVol 2.8) |
| 3 | **SMCI** | 27.25 | FLIP CROSS down into negative gamma | **PUTS** | 23 | 11/13 27P @ 0.57 (delta 0.42) = est +32% at 26.74 | NEG -$745k | 28.61 | 28 | 25 | +$1.2M | - | out (clean 34, ADX 18, RVol 0.8) |
| 4 | **MSFT** | 522.29 | - | **-** | 21 | - | POS +$46.1M | 520.3 | 535 | 520 | -$1.9M | +$299k bull / +$0 bear | out (clean 33, ADX 48, RVol 0.8) |
| 5 | **SPY** | 757.66 | - | **-** | 19 | - | NEG -$2.2B | 760.32 | 760 | 760 | -$111.1M | +$3.0M bull / -$1.8M bear | out (clean 32, ADX 33, RVol 0.6) |
| 6 | **QQQ** | 687.72 | - | **-** | 18 | - | NEG -$387.1M | 689.79 | 700 | 680 | -$69.9M | +$1.1M bull / +$0 bear | out (clean 31, ADX 31, RVol 0.5) |
| 7 | **META** | 622.00 | - | **-** | 18 | - | NEG -$36.3M | 625.6 | 650 | 600 | +$2.5M | +$69k bull / +$0 bear | out (clean 29, ADX 31, RVol 0.3) |
| 8 | **SMH** | 500.19 | - | **-** | 17 | - | NEG -$109.8M | 526.53 | 500 | 475 | -$1.3M | +$117k bull / +$0 bear | out (clean 30, ADX 24, RVol 0.4) |
| 9 | **AAPL** | 355.58 | - | **-** | 17 | - | POS +$1.1B | 340.56 | 360 | 350 | +$5.2M | +$27k bull / +$0 bear | out (clean 29, ADX 23, RVol 0.3) |
| 10 | **NVDA** | 164.66 | - | **-** | 16 | - | NEG -$192.7M | - | 170 | 160 | -$69.6M | +$947k bull / -$1.1M bear | out (clean 32, ADX 12, RVol 0.8) |
| 11 | **DELL** | 369.62 | - | **-** | 16 | - | POS +$6.8M | - | 360 | 400 | +$807k | +$59k bull / +$0 bear | out (clean 38, ADX 20, RVol 0.9) |
| 12 | **ORCL** | 126.52 | - | **-** | 16 | - | POS +$9.5M | - | 130 | 125 | -$471k | +$75k bull / +$0 bear | out (clean 30, ADX 17, RVol 0.6) |
| 13 | **AMD** | 582.92 | - | **-** | 15 | - | POS +$223.9M | - | 600 | 550 | -$19.5M | +$2.9M bull / +$0 bear | out (clean 35, ADX 15, RVol 0.6) |
| 14 | **MU** | 794.04 | - | **-** | 13 | - | POS +$108.5M | - | 800 | 800 | +$7.3M | +$1.5M bull / -$607k bear | out (clean 31, ADX 9, RVol 0.6) |
| 15 | **NFLX** | 63.07 | - | **-** | 12 | - | NEG -$14.8M | 63.65 | 65 | 60 | -$189k | - | out (clean 30, ADX 43, RVol 0.6) |
| 16 | **IWM** | 278.95 | - | **-** | 10 | - | NEG -$1.4B | 282.52 | 285 | 275 | -$564k | - | out (clean 34, ADX 46, RVol 0.7) |
| 17 | **AMZN** | 268.03 | - | **-** | 10 | - | POS +$463.6M | - | 270 | 270 | -$7.4M | - | out (clean 30, ADX 26, RVol 0.8) |
| 18 | **UBER** | 69.06 | - | **-** | 10 | - | POS +$7.9M | 68.42 | 70 | 70 | -$41k | - | out (clean 32, ADX 29, RVol 1.1) |
| 19 | **ARM** | 199.45 | - | **-** | 9 | - | POS +$8.9M | - | 200 | 200 | -$347k | - | out (clean 31, ADX 23, RVol 0.2) |
| 20 | **BABA** | 94.69 | - | **-** | 9 | - | NEG -$19.4M | - | 100 | 100 | +$299k | - | out (clean 28, ADX 15, RVol 1.2) |
| 21 | **COIN** | 131.05 | - | **-** | 8 | - | NEG -$811k | 131.36 | 137 | 135 | +$113k | - | out (clean 30, ADX 26, RVol 0.9) |
| 22 | **SHOP** | 146.98 | - | **-** | 8 | - | POS +$4.0M | 143.49 | 150 | 140 | +$5k | - | out (clean 31, ADX 30, RVol 0.3) |
| 23 | **CRM** | 216.70 | - | **-** | 7 | - | NEG -$8.7M | - | 220 | 220 | +$43k | - | out (clean 29, ADX 24, RVol 0.2) |
| 24 | **AVGO** | 362.43 | - | **-** | 6 | - | POS +$136.2M | - | 350 | 350 | +$9.1M | - | out (clean 34, ADX 11, RVol 0.8) |
| 25 | **MSTR** | 115.27 | - | **-** | 6 | - | NEG -$33.8M | - | 125 | 110 | -$610k | - | out (clean 29, ADX 20, RVol 0.6) |
| 26 | **HOOD** | 82.28 | - | **-** | 6 | - | POS +$10.3M | 80.1 | 85 | 80 | +$8k | - | out (clean 34, ADX 26, RVol 0.6) |
| 27 | **PLTR** | 171.78 | - | **-** | 5 | - | POS +$87.3M | - | 170 | 170 | -$196k | - | out (clean 29, ADX 18, RVol 0.7) |

## Big prints this scan (95)
- **TSLA** CALL 385 2026-11-13 (1DTE): 199 @ 9.00 = **+$179k** SELL | vol 3,579 / OI 3,234
- **TSLA** CALL 405 2026-11-13 (1DTE): 1,000 @ 1.55 = **+$155k** SELL | vol 36,922 / OI 5,528
- **TSLA** PUT 390 2026-11-16 (4DTE): 321 @ 4.25 = **+$136k** BUY | vol 4,267 / OI 177
- **AMD** CALL 555 2026-11-13 (1DTE): 40 @ 33.10 = **+$132k** BUY | vol 3,410 / OI 1,386
- **TSLA** PUT 390 2026-11-16 (4DTE): 302 @ 4.20 = **+$127k** BUY | vol 4,267 / OI 177
- **QQQ** CALL 687 2026-11-12 (0DTE): 800 @ 1.56 = **+$125k** BUY | vol 120,960 / OI 452
- **TSLA** CALL 402.5 2026-11-13 (1DTE): 650 @ 1.78 = **+$116k** SELL | vol 24,287 / OI 2,130
- **TSLA** CALL 405 2026-11-13 (1DTE): 742 @ 1.54 = **+$114k** SELL | vol 36,922 / OI 5,528
- **TSLA** CALL 402.5 2026-11-13 (1DTE): 500 @ 2.19 = **+$110k** SELL | vol 24,287 / OI 2,130
- **TSLA** CALL 387.5 2026-11-13 (1DTE): 92 @ 10.30 = **+$95k** SELL | vol 3,953 / OI 1,728
- **TSLA** CALL 390 2026-11-18 (6DTE): 89 @ 10.57 = **+$94k** SELL | vol 892 / OI 518
- **TSLA** CALL 395 2026-11-13 (1DTE): 206 @ 4.50 = **+$93k** SELL | vol 48,539 / OI 5,642
- **TSLA** CALL 395 2026-11-13 (1DTE): 206 @ 4.50 = **+$93k** SELL | vol 48,539 / OI 5,642
- **TSLA** CALL 395 2026-11-13 (1DTE): 206 @ 4.50 = **+$93k** SELL | vol 48,539 / OI 5,642
- **TSLA** CALL 395 2026-11-13 (1DTE): 206 @ 4.50 = **+$93k** SELL | vol 48,539 / OI 5,642

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 763 2026-11-18 (6DTE): 513 traded vs OI 107
- **QQQ** CALL 714 2026-11-27 (15DTE): 748 traded vs OI 263
- **IWM** CALL 285 2026-11-16 (4DTE): 2,304 traded vs OI 2,290
- **NVDA** PUT 150 2026-11-20 (8DTE): 34,586 traded vs OI 34,320
- **NVDA** PUT 150 2026-11-23 (11DTE): 1,599 traded vs OI 1,310
- **NVDA** CALL 170 2026-11-23 (11DTE): 1,772 traded vs OI 1,402
- **TSLA** CALL 385 2026-11-13 (1DTE): 3,579 traded vs OI 3,234
- **TSLA** CALL 417.5 2026-11-20 (8DTE): 610 traded vs OI 0
- **TSLA** CALL 417.5 2026-11-16 (4DTE): 530 traded vs OI 148
- **TSLA** CALL 420 2026-11-18 (6DTE): 536 traded vs OI 195
- **TSLA** CALL 420 2026-12-11 (29DTE): 849 traded vs OI 785
- **TSLA** CALL 387.5 2026-11-16 (4DTE): 776 traded vs OI 256
- **TSLA** CALL 425 2026-11-16 (4DTE): 517 traded vs OI 445
- **TSLA** CALL 405 2026-11-18 (6DTE): 962 traded vs OI 259
- **TSLA** CALL 397.5 2026-11-18 (6DTE): 517 traded vs OI 97

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
