# GEX + FLOW SCAN - Thu Nov 12, 03:45 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (5)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:35 | **SPY** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/12 754P | 0.59 | 0.17 | +10% (1m) | **-71%** (done) | +70% | 755 |
| 09:50 | **HOOD** | **PUTS** | TREND + FLOW | 11/13 79P | 0.55 | 0.36 | +5% (19m) | **-35%** (done) | +92% | 80 |
| 09:45 | **ORCL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/13 130C | 0.75 | 0.72 | +4% (60m) | **-4%** (done) | +59% | 126.9 |
| 09:45 | **SMCI** | **PUTS** | TREND + FLOW | 11/13 27P | 0.42 | 0.23 | -5% (6m) | **-45%** (done) | +57% | 27 |
| 09:45 | **SPY** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/12 753P | 0.79 | 0.31 | +23% (18m) | **-61%** (done) | +51% | 754.88 |

## 1m RULES on SPY / QQQ - loose (5 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 15:32:08 ET, last candle SPY 15:31, QQQ 15:31 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 15:27 | SPY | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |
| 15:26 | QQQ | 1m FAILED POP | R3 R4 | PUTS | TURNING your way | no contract: 84 puts 0-1DTE > 7 priced 0.40-0.80 > 2 delta 0.15+ > 2 spread ok > 2 liquid  |
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
| 1 | **GOOGL** | 299.32 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 39 | none: 72 puts 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (8 contracts' greeks worked out here) | POS +$140.5M | 289 | 300 | 290 | -$5.7M | +$80k bull / -$2.0M bear | out (clean 30, ADX 26, RVol 0.9) |
| 2 | **SMCI** | 27.27 | FLIP CROSS up into positive gamma | **CALLS** | 24 | 11/13 27.5C @ 0.56 (delta 0.46) = est +31% at 27.75 | POS +$1.0M | 26.76 | 30 | 25 | +$1.2M | - | out (clean 34, ADX 19, RVol 0.9) |
| 3 | **TSLA** | 397.50 | - | **-** | 23 | - | POS +$393.4M | - | 400 | 380 | -$9.2M | +$3.6M bull / -$7.3M bear | out (clean 30, ADX 41, RVol 3.2) |
| 4 | **SPY** | 756.90 | - | **-** | 20 | - | NEG -$2.8B | 759.87 | 760 | 760 | -$96.5M | +$756k bull / +$0 bear | out (clean 32, ADX 37, RVol 0.9) |
| 5 | **IWM** | 278.60 | - | **-** | 20 | - | NEG -$1.5B | 282.47 | 285 | 275 | +$207k | +$211k bull / +$0 bear | out (clean 34, ADX 46, RVol 1.2) |
| 6 | **MSFT** | 521.84 | - | **-** | 20 | - | POS +$39.5M | 519.92 | 535 | 520 | -$774k | +$1.4M bull / -$785k bear | out (clean 33, ADX 46, RVol 0.7) |
| 7 | **QQQ** | 687.17 | - | **-** | 19 | - | NEG -$528.3M | 690.07 | 700 | 680 | -$63.3M | +$1.9M bull / -$7.3M bear | out (clean 31, ADX 34, RVol 1.0) |
| 8 | **META** | 620.65 | - | **-** | 19 | - | NEG -$43.0M | 625.55 | 650 | 600 | +$3.6M | +$855k bull / +$0 bear | out (clean 29, ADX 34, RVol 0.4) |
| 9 | **SMH** | 499.65 | - | **-** | 18 | - | NEG -$111.7M | 527.4 | 500 | 475 | -$1.3M | +$41k bull / +$0 bear | out (clean 30, ADX 27, RVol 0.6) |
| 10 | **AAPL** | 355.20 | - | **-** | 18 | - | POS +$1.0B | 340.81 | 360 | 350 | +$5.6M | +$0 bull / -$49k bear | out (clean 29, ADX 25, RVol 0.5) |
| 11 | **AVGO** | 361.58 | - | **-** | 18 | - | POS +$135.9M | - | 350 | 350 | +$9.7M | +$285k bull / +$0 bear | out (clean 34, ADX 14, RVol 1.1) |
| 12 | **HOOD** | 81.89 | - | **-** | 18 | - | POS +$8.5M | 80.08 | 85 | 80 | +$82k | +$30k bull / +$0 bear | out (clean 34, ADX 31, RVol 1.0) |
| 13 | **NVDA** | 164.34 | - | **-** | 16 | - | NEG -$193.3M | - | 170 | 160 | -$68.2M | +$2.9M bull / -$162k bear | out (clean 32, ADX 13, RVol 0.9) |
| 14 | **AMD** | 580.86 | - | **-** | 15 | - | POS +$213.9M | - | 600 | 550 | -$16.2M | +$995k bull / +$0 bear | out (clean 35, ADX 15, RVol 0.6) |
| 15 | **PLTR** | 171.44 | - | **-** | 15 | - | POS +$93.6M | - | 170 | 170 | +$5k | +$165k bull / +$0 bear | out (clean 29, ADX 20, RVol 0.7) |
| 16 | **MU** | 794.91 | - | **-** | 14 | - | POS +$104.5M | - | 800 | 800 | +$5.4M | +$448k bull / -$1.1M bear | out (clean 31, ADX 10, RVol 0.8) |
| 17 | **AMZN** | 267.49 | - | **-** | 12 | - | POS +$457.8M | - | 270 | 270 | -$7.4M | - | out (clean 30, ADX 33, RVol 1.7) |
| 18 | **NFLX** | 62.77 | - | **-** | 12 | - | NEG -$22.8M | 63.79 | 65 | 60 | -$159k | - | out (clean 31, ADX 50, RVol 0.9) |
| 19 | **BABA** | 94.48 | - | **-** | 12 | - | NEG -$17.7M | - | 100 | 95 | +$325k | - | out (clean 28, ADX 18, RVol 2.0) |
| 20 | **SHOP** | 146.68 | - | **-** | 11 | - | POS +$4.7M | 143.45 | 150 | 140 | +$16k | - | out (clean 32, ADX 30, RVol 0.5) |
| 21 | **UBER** | 69.08 | - | **-** | 10 | - | POS +$9.6M | 68.42 | 70 | 70 | -$46k | - | out (clean 33, ADX 31, RVol 1.1) |
| 22 | **COIN** | 130.96 | - | **-** | 9 | - | NEG -$2.4M | 131.53 | 137 | 130 | +$125k | - | out (clean 30, ADX 32, RVol 1.1) |
| 23 | **ARM** | 198.98 | - | **-** | 9 | - | POS +$9.2M | - | 200 | 200 | -$339k | - | out (clean 32, ADX 27, RVol 0.3) |
| 24 | **DELL** | 370.01 | - | **-** | 8 | - | POS +$7.2M | - | 360 | 400 | +$722k | - | out (clean 38, ADX 25, RVol 1.1) |
| 25 | **CRM** | 216.54 | - | **-** | 8 | - | NEG -$7.0M | 226.01 | 220 | 220 | +$44k | - | out (clean 30, ADX 26, RVol 0.4) |
| 26 | **MSTR** | 115.26 | - | **-** | 7 | - | NEG -$32.7M | - | 125 | 110 | -$593k | - | out (clean 29, ADX 21, RVol 1.2) |
| 27 | **ORCL** | 126.45 | - | **-** | 7 | - | POS +$10.3M | 121 | 130 | 125 | -$395k | - | out (clean 31, ADX 21, RVol 0.5) |

## Big prints this scan (95)
- **TSLA** PUT 392.5 2026-11-16 (4DTE): 868 @ 3.80 = **+$330k** SELL | vol 3,350 / OI 11
- **NVDA** PUT 162.5 2026-11-16 (4DTE): 938 @ 3.50 = **+$328k** SELL | vol 26,484 / OI 1,267
- **TSLA** PUT 400 2026-11-16 (4DTE): 450 @ 6.50 = **+$292k** SELL | vol 984 / OI 86
- **TSLA** CALL 405 2026-11-13 (1DTE): 500 @ 3.35 = **+$168k** BUY | vol 51,133 / OI 5,528
- **TSLA** CALL 382.5 2026-11-13 (1DTE): 80 @ 18.65 = **+$149k** BUY | vol 1,535 / OI 1,116
- **MSFT** PUT 520 2026-11-13 (1DTE): 422 @ 3.15 = **+$133k** SELL | vol 14,011 / OI 6,123
- **TSLA** PUT 400 2026-11-13 (1DTE): 171 @ 5.30 = **+$91k** SELL | vol 5,391 / OI 1,309
- **TSLA** CALL 397.5 2026-11-13 (1DTE): 115 @ 7.22 = **+$83k** BUY | vol 30,807 / OI 1,998
- **AVGO** PUT 365 2026-11-13 (1DTE): 120 @ 6.70 = **+$80k** MID | vol 3,856 / OI 26
- **TSLA** CALL 400 2026-11-13 (1DTE): 140 @ 5.60 = **+$78k** BUY | vol 99,455 / OI 13,604
- **TSLA** CALL 392.5 2026-11-13 (1DTE): 75 @ 9.80 = **+$74k** BUY | vol 37,706 / OI 1,586
- **TSLA** CALL 395 2026-11-13 (1DTE): 100 @ 7.25 = **+$72k** BUY | vol 57,611 / OI 5,642
- **TSLA** CALL 405 2026-11-18 (6DTE): 100 @ 6.65 = **+$66k** BUY | vol 1,311 / OI 259
- **TSLA** CALL 410 2026-11-13 (1DTE): 399 @ 1.65 = **+$66k** BUY | vol 37,380 / OI 4,367
- **TSLA** CALL 390 2026-11-13 (1DTE): 50 @ 12.00 = **+$60k** BUY | vol 22,262 / OI 6,197

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 737 2026-11-13 (1DTE): 2,757 traded vs OI 2,755
- **SPY** CALL 761 2026-11-24 (12DTE): 518 traded vs OI 0
- **SPY** PUT 761 2026-11-18 (6DTE): 518 traded vs OI 306
- **QQQ** CALL 695 2026-11-17 (5DTE): 500 traded vs OI 376
- **QQQ** PUT 675 2026-11-18 (6DTE): 531 traded vs OI 191
- **IWM** CALL 284 2026-11-19 (7DTE): 500 traded vs OI 119
- **SMH** PUT 540 2026-11-13 (1DTE): 1,692 traded vs OI 1,299
- **TSLA** PUT 402.5 2026-11-13 (1DTE): 564 traded vs OI 221
- **TSLA** PUT 380 2026-11-18 (6DTE): 611 traded vs OI 102
- **TSLA** CALL 435 2026-11-13 (1DTE): 581 traded vs OI 0
- **TSLA** CALL 425 2026-11-13 (1DTE): 3,404 traded vs OI 2,618
- **TSLA** PUT 400 2026-11-16 (4DTE): 984 traded vs OI 86
- **MSFT** PUT 490 2026-11-13 (1DTE): 3,893 traded vs OI 1,497
- **GOOGL** PUT 285 2026-11-16 (4DTE): 555 traded vs OI 124
- **COIN** PUT 127 2026-11-20 (8DTE): 893 traded vs OI 30

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
