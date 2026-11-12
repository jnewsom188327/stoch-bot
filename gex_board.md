# GEX + FLOW SCAN - Thu Nov 12, 03:55 PM ET
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
| 1 | **AMZN** | 267.51 | - | **-** | 24 | - | POS +$447.6M | - | 270 | 270 | -$7.1M | +$43k bull / +$0 bear | out (clean 30, ADX 36, RVol 2.0) |
| 2 | **TSLA** | 396.57 | - | **-** | 23 | - | POS +$403.8M | - | 400 | 380 | -$3.1M | +$4.3M bull / -$2.7M bear | out (clean 30, ADX 42, RVol 3.2) |
| 3 | **ARM** | 199.85 | PINNED between the walls (positive gamma) - chop | **-** | 23 | - | POS +$9.4M | - | 200 | 200 | -$354k | - | out (clean 32, ADX 26, RVol 0.6) |
| 4 | **IWM** | 278.38 | - | **-** | 22 | - | NEG -$1.8B | 282.6 | 285 | 270 | +$1.5M | +$294k bull / +$0 bear | out (clean 34, ADX 47, RVol 1.7) |
| 5 | **SPY** | 756.75 | - | **-** | 21 | - | NEG -$3.8B | 760.17 | 760 | 760 | -$87.9M | +$709k bull / +$0 bear | out (clean 32, ADX 38, RVol 1.3) |
| 6 | **HOOD** | 81.61 | - | **-** | 21 | - | POS +$6.0M | 80.08 | 85 | 80 | +$112k | +$30k bull / +$0 bear | out (clean 34, ADX 33, RVol 1.9) |
| 7 | **QQQ** | 687.75 | - | **-** | 20 | - | NEG -$716.7M | 690.12 | 700 | 680 | -$63.8M | +$1.6M bull / -$154k bear | out (clean 31, ADX 34, RVol 1.4) |
| 8 | **META** | 622.16 | - | **-** | 20 | - | NEG -$30.5M | 625.51 | 650 | 600 | +$5.3M | +$887k bull / -$1.4M bear | out (clean 29, ADX 32, RVol 0.8) |
| 9 | **MSFT** | 522.28 | - | **-** | 20 | - | POS +$59.7M | 519.74 | 535 | 520 | -$968k | +$242k bull / -$785k bear | out (clean 33, ADX 45, RVol 0.8) |
| 10 | **GOOGL** | 298.62 | - | **-** | 20 | - | POS +$138.3M | 288.66 | 300 | 290 | -$5.4M | +$0 bull / -$2.0M bear | out (clean 30, ADX 28, RVol 1.3) |
| 11 | **SMH** | 501.13 | - | **-** | 19 | - | NEG -$121.8M | - | 500 | 475 | -$1.7M | +$0 bull / -$30k bear | out (clean 30, ADX 27, RVol 0.7) |
| 12 | **AAPL** | 354.91 | - | **-** | 19 | - | POS +$1.0B | 340.83 | 360 | 350 | +$6.1M | +$63k bull / -$49k bear | out (clean 30, ADX 27, RVol 1.0) |
| 13 | **AVGO** | 363.20 | - | **-** | 18 | - | POS +$136.6M | - | 350 | 350 | +$8.9M | +$285k bull / -$95k bear | out (clean 34, ADX 15, RVol 1.5) |
| 14 | **DELL** | 371.64 | - | **-** | 17 | - | POS +$6.7M | - | 360 | 400 | +$558k | +$0 bull / -$37k bear | out (clean 38, ADX 23, RVol 1.0) |
| 15 | **NVDA** | 165.46 | - | **-** | 16 | - | NEG -$184.0M | - | 170 | 160 | -$72.8M | +$891k bull / -$2.0M bear | out (clean 32, ADX 12, RVol 1.0) |
| 16 | **AMD** | 582.52 | - | **-** | 15 | - | POS +$222.8M | - | 600 | 550 | -$17.6M | +$487k bull / -$1.0M bear | out (clean 35, ADX 15, RVol 0.7) |
| 17 | **MU** | 797.37 | - | **-** | 14 | - | POS +$104.0M | - | 800 | 800 | +$5.0M | +$265k bull / -$1.0M bear | out (clean 31, ADX 9, RVol 1.0) |
| 18 | **NFLX** | 62.63 | - | **-** | 13 | - | NEG -$26.9M | 63.97 | 65 | 60 | -$149k | - | out (clean 31, ADX 55, RVol 1.3) |
| 19 | **BABA** | 94.64 | - | **-** | 12 | - | NEG -$17.7M | - | 100 | 95 | +$274k | - | out (clean 28, ADX 18, RVol 3.1) |
| 20 | **UBER** | 69.22 | - | **-** | 11 | - | POS +$9.8M | 68.44 | 70 | 70 | -$47k | - | out (clean 33, ADX 28, RVol 1.8) |
| 21 | **SHOP** | 146.70 | - | **-** | 11 | - | POS +$4.4M | 143.54 | 150 | 140 | +$16k | - | out (clean 32, ADX 27, RVol 0.9) |
| 22 | **SMCI** | 27.16 | - | **-** | 10 | - | NEG -$1.1M | - | 28 | 25 | +$1.2M | - | out (clean 34, ADX 18, RVol 1.4) |
| 23 | **COIN** | 131.19 | - | **-** | 9 | - | NEG -$3.0M | 131.43 | 137 | 130 | +$116k | - | out (clean 30, ADX 31, RVol 0.8) |
| 24 | **MSTR** | 115.35 | - | **-** | 8 | - | NEG -$35.2M | - | 125 | 110 | -$596k | - | out (clean 29, ADX 20, RVol 1.7) |
| 25 | **CRM** | 217.35 | - | **-** | 8 | - | NEG -$8.7M | - | 220 | 220 | +$43k | - | out (clean 30, ADX 24, RVol 0.7) |
| 26 | **ORCL** | 127.26 | - | **-** | 7 | - | POS +$12.7M | - | 130 | 125 | -$434k | - | out (clean 31, ADX 20, RVol 0.7) |
| 27 | **PLTR** | 171.55 | - | **-** | 6 | - | POS +$91.7M | - | 170 | 170 | -$30k | - | out (clean 29, ADX 18, RVol 1.1) |

## Big prints this scan (49)
- **IWM** PUT 282 2026-11-13 (1DTE): 500 @ 3.65 = **+$182k** SELL | vol 3,682 / OI 1,590
- **IWM** PUT 278 2026-11-13 (1DTE): 1,000 @ 1.11 = **+$111k** SELL | vol 15,492 / OI 7,514
- **AMD** CALL 555 2026-11-16 (4DTE): 32 @ 32.65 = **+$104k** SELL | vol 552 / OI 89
- **AMD** CALL 555 2026-11-16 (4DTE): 32 @ 32.00 = **+$102k** SELL | vol 552 / OI 89
- **MU** CALL 785 2026-11-13 (1DTE): 49 @ 20.00 = **+$98k** BUY | vol 8,279 / OI 317
- **MU** PUT 800 2026-11-13 (1DTE): 50 @ 18.00 = **+$90k** BUY | vol 7,959 / OI 872
- **MU** CALL 790 2026-11-13 (1DTE): 49 @ 16.10 = **+$79k** SELL | vol 19,214 / OI 1,225
- **AMD** PUT 577.5 2026-11-16 (4DTE): 50 @ 14.18 = **+$71k** MID | vol 303 / OI 2
- **NVDA** CALL 165 2026-11-18 (6DTE): 100 @ 6.95 = **+$70k** SELL | vol 12,404 / OI 517
- **AAPL** PUT 357.5 2026-11-16 (4DTE): 176 @ 3.60 = **+$63k** SELL | vol 2,415 / OI 12
- **NVDA** CALL 160 2026-11-13 (1DTE): 100 @ 5.70 = **+$57k** SELL | vol 135,216 / OI 2,015
- **AMD** PUT 560 2026-11-13 (1DTE): 150 @ 3.80 = **+$57k** MID | vol 9,438 / OI 119
- **AMD** PUT 580 2026-11-13 (1DTE): 50 @ 10.58 = **+$53k** BUY | vol 12,776 / OI 4
- **NVDA** PUT 162.5 2026-11-13 (1DTE): 200 @ 2.61 = **+$52k** BUY | vol 163,093 / OI 20,581
- **MU** CALL 800 2026-11-13 (1DTE): 45 @ 11.25 = **+$51k** SELL | vol 29,845 / OI 5,964

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 744 2026-11-17 (5DTE): 515 traded vs OI 240
- **SPY** PUT 742 2026-11-13 (1DTE): 5,776 traded vs OI 5,748
- **SPY** CALL 768 2026-11-19 (7DTE): 500 traded vs OI 310
- **SPY** PUT 759 2026-12-04 (22DTE): 500 traded vs OI 389
- **SPY** PUT 715 2026-11-27 (15DTE): 3,424 traded vs OI 2,888
- **SPY** PUT 729 2026-12-11 (29DTE): 634 traded vs OI 86
- **QQQ** PUT 648 2026-11-13 (1DTE): 1,270 traded vs OI 1,155
- **QQQ** CALL 695 2026-11-27 (15DTE): 591 traded vs OI 501
- **QQQ** PUT 655 2026-11-27 (15DTE): 1,448 traded vs OI 1,270
- **IWM** CALL 287.5 2026-11-16 (4DTE): 870 traded vs OI 671
- **IWM** CALL 280 2026-11-18 (6DTE): 527 traded vs OI 189
- **SMH** CALL 535 2026-11-20 (8DTE): 1,366 traded vs OI 1,342
- **TSLA** CALL 402.5 2026-11-20 (8DTE): 534 traded vs OI 0
- **AAPL** PUT 342.5 2026-11-16 (4DTE): 1,316 traded vs OI 150
- **AAPL** PUT 340 2026-11-18 (6DTE): 753 traded vs OI 439

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
