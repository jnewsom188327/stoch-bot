# GEX + FLOW SCAN - Thu Nov 12, 02:40 PM ET
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
Last 1m check 14:40:08 ET, last candle SPY 14:39, QQQ 14:39 | no errors
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
| 1 | **GOOGL** | 299.43 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 39 | none: 72 puts 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (2 contracts' greeks worked out here) | POS +$131.2M | 288.53 | 300 | 290 | -$4.9M | +$166k bull / +$0 bear | out (clean 30, ADX 25, RVol 0.9) |
| 2 | **MSFT** | 523.00 | - | **-** | 21 | - | POS +$65.6M | 519.65 | 535 | 520 | -$3.5M | +$27k bull / +$0 bear | out (clean 32, ADX 40, RVol 0.6) |
| 3 | **ARM** | 199.64 | PINNED between the walls (positive gamma) - chop | **-** | 20 | - | POS +$9.9M | - | 200 | 200 | -$336k | - | out (clean 31, ADX 23, RVol 0.2) |
| 4 | **QQQ** | 687.54 | - | **-** | 17 | - | NEG -$622.7M | 690.39 | 700 | 680 | -$79.1M | +$710k bull / +$0 bear | out (clean 31, ADX 22, RVol 0.5) |
| 5 | **TSLA** | 390.43 | - | **-** | 17 | - | POS +$352.1M | - | 400 | 380 | +$11.3M | +$380k bull / +$0 bear | out (clean 29, ADX 22, RVol 0.2) |
| 6 | **AAPL** | 355.58 | - | **-** | 17 | - | POS +$1.1B | 340.17 | 360 | 350 | +$5.2M | +$28k bull / +$0 bear | out (clean 29, ADX 23, RVol 0.4) |
| 7 | **NVDA** | 163.30 | - | **-** | 16 | - | NEG -$199.5M | - | 170 | 160 | -$59.2M | +$679k bull / -$43k bear | out (clean 32, ADX 13, RVol 0.6) |
| 8 | **AMD** | 583.38 | - | **-** | 14 | - | POS +$196.1M | - | 600 | 550 | -$22.3M | +$0 bull / -$812k bear | out (clean 34, ADX 13, RVol 0.4) |
| 9 | **MU** | 793.36 | - | **-** | 13 | - | POS +$105.4M | - | 800 | 800 | +$4.4M | +$2.1M bull / -$1.2M bear | out (clean 31, ADX 11, RVol 0.5) |
| 10 | **SMCI** | 27.54 | - | **-** | 11 | - | POS +$1.2M | 26.78 | 30 | 25 | +$1.1M | - | out (clean 34, ADX 24, RVol 1.3) |
| 11 | **BABA** | 94.44 | - | **-** | 10 | - | NEG -$16.2M | - | 100 | 100 | +$316k | - | out (clean 29, ADX 20, RVol 1.0) |
| 12 | **SPY** | 757.68 | - | **-** | 8 | - | NEG -$2.8B | 760.61 | 760 | 760 | -$121.0M | - | out (clean 32, ADX 24, RVol 0.3) |
| 13 | **IWM** | 279.04 | - | **-** | 8 | - | NEG -$1.4B | 282.59 | 285 | 275 | -$258k | - | out (clean 34, ADX 40, RVol 0.3) |
| 14 | **NFLX** | 63.30 | - | **-** | 8 | - | NEG -$12.7M | 63.93 | 65 | 65 | -$175k | - | out (clean 28, ADX 22, RVol 0.6) |
| 15 | **SMH** | 499.83 | - | **-** | 7 | - | NEG -$128.4M | - | 500 | 475 | -$1.4M | - | out (clean 31, ADX 20, RVol 0.3) |
| 16 | **AMZN** | 268.37 | - | **-** | 7 | - | POS +$482.5M | - | 270 | 270 | -$7.4M | - | out (clean 29, ADX 13, RVol 0.6) |
| 17 | **META** | 621.61 | - | **-** | 6 | - | NEG -$36.1M | 624.99 | 650 | 600 | +$2.1M | - | out (clean 28, ADX 26, RVol 0.3) |
| 18 | **AVGO** | 363.17 | - | **-** | 6 | - | POS +$135.9M | - | 350 | 350 | +$8.9M | - | out (clean 34, ADX 10, RVol 0.6) |
| 19 | **UBER** | 69.31 | - | **-** | 6 | - | POS +$11.2M | 68.43 | 70 | 70 | -$50k | - | out (clean 32, ADX 13, RVol 0.3) |
| 20 | **SHOP** | 147.06 | - | **-** | 6 | - | POS +$2.8M | 144.23 | 150 | 140 | +$2k | - | out (clean 31, ADX 26, RVol 0.2) |
| 21 | **COIN** | 131.57 | - | **-** | 5 | - | POS +$159k | 131.34 | 137 | 135 | +$95k | - | out (clean 30, ADX 17, RVol 0.3) |
| 22 | **ORCL** | 127.00 | - | **-** | 5 | - | POS +$10.5M | 121.43 | 130 | 125 | -$584k | - | out (clean 30, ADX 8, RVol 0.5) |
| 23 | **HOOD** | 82.31 | - | **-** | 5 | - | POS +$9.9M | 80.05 | 85 | 80 | -$25k | - | out (clean 34, ADX 21, RVol 0.7) |
| 24 | **CRM** | 217.48 | - | **-** | 5 | - | NEG -$8.8M | 228.46 | 220 | 220 | +$40k | - | out (clean 29, ADX 17, RVol 0.1) |
| 25 | **PLTR** | 171.69 | - | **-** | 4 | - | POS +$90.8M | - | 170 | 170 | -$208k | - | out (clean 28, ADX 10, RVol 0.7) |
| 26 | **DELL** | 372.91 | - | **-** | 4 | - | POS +$5.1M | - | 360 | 340 | +$400k | - | out (clean 37, ADX 17, RVol 0.4) |
| 27 | **MSTR** | 115.27 | - | **-** | 4 | - | NEG -$32.4M | - | 125 | 110 | -$689k | - | out (clean 29, ADX 14, RVol 0.4) |

## Big prints this scan (61)
- **MU** CALL 790 2026-11-13 (1DTE): 99 @ 18.00 = **+$178k** BUY | vol 17,187 / OI 1,225
- **TSLA** CALL 377.5 2026-11-13 (1DTE): 100 @ 13.97 = **+$140k** BUY | vol 638 / OI 4,895
- **MU** PUT 785 2026-11-13 (1DTE): 131 @ 10.00 = **+$131k** SELL | vol 9,391 / OI 256
- **MU** CALL 780 2026-11-13 (1DTE): 50 @ 25.00 = **+$125k** BUY | vol 15,056 / OI 1,424
- **MU** CALL 780 2026-11-13 (1DTE): 50 @ 25.00 = **+$125k** BUY | vol 15,056 / OI 1,424
- **TSLA** CALL 380 2026-11-13 (1DTE): 100 @ 11.72 = **+$117k** BUY | vol 1,889 / OI 8,365
- **MU** PUT 800 2026-11-13 (1DTE): 60 @ 16.06 = **+$96k** SELL | vol 6,679 / OI 872
- **TSLA** CALL 385 2026-11-16 (4DTE): 100 @ 9.60 = **+$96k** BUY | vol 1,446 / OI 301
- **MU** CALL 760 2026-11-13 (1DTE): 20 @ 39.05 = **+$78k** BUY | vol 1,423 / OI 2,475
- **NVDA** CALL 165 2026-11-13 (1DTE): 230 @ 3.05 = **+$70k** BUY | vol 233,548 / OI 2,999
- **MU** CALL 765 2026-11-13 (1DTE): 20 @ 34.90 = **+$70k** BUY | vol 2,388 / OI 987
- **MU** PUT 805 2026-11-13 (1DTE): 27 @ 19.00 = **+$51k** SELL | vol 786 / OI 364
- **MU** PUT 805 2026-11-13 (1DTE): 26 @ 19.00 = **+$49k** SELL | vol 786 / OI 364
- **MU** CALL 795 2026-11-13 (1DTE): 30 @ 15.70 = **+$47k** BUY | vol 12,446 / OI 462
- **MU** CALL 815 2026-11-13 (1DTE): 66 @ 7.07 = **+$47k** BUY | vol 4,237 / OI 346

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 766 2026-11-18 (6DTE): 665 traded vs OI 656
- **SPY** CALL 761 2026-11-19 (7DTE): 503 traded vs OI 149
- **IWM** CALL 291 2026-11-17 (5DTE): 1,526 traded vs OI 264
- **NVDA** PUT 147 2026-11-18 (6DTE): 797 traded vs OI 232
- **AMD** CALL 582.5 2026-11-20 (8DTE): 500 traded vs OI 0
- **META** CALL 670 2026-11-18 (6DTE): 559 traded vs OI 132
- **DELL** CALL 392.5 2026-11-13 (1DTE): 509 traded vs OI 0
- **MU** PUT 805 2026-11-13 (1DTE): 786 traded vs OI 364
- **ORCL** CALL 139 2026-11-13 (1DTE): 644 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
