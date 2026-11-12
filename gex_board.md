# GEX + FLOW SCAN - Thu Nov 12, 03:00 PM ET
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
Last 1m check 15:00:08 ET, last candle SPY 14:59, QQQ 14:59 | no errors
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
| 1 | **GOOGL** | 299.67 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 39 | none: 72 puts 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (6 contracts' greeks worked out here) | POS +$131.9M | 289.02 | 300 | 290 | -$5.0M | +$0 bull / -$27k bear | out (clean 30, ADX 26, RVol 1.0) |
| 2 | **MSFT** | 522.13 | - | **-** | 20 | - | POS +$49.1M | 519.2 | 535 | 520 | -$1.9M | +$278k bull / +$0 bear | out (clean 32, ADX 44, RVol 0.4) |
| 3 | **ARM** | 200.23 | PINNED between the walls (positive gamma) - chop | **-** | 20 | - | POS +$10.2M | - | 200 | 200 | -$352k | - | out (clean 31, ADX 23, RVol 0.3) |
| 4 | **SPY** | 757.79 | - | **-** | 18 | - | NEG -$2.6B | 760.57 | 760 | 760 | -$110.5M | +$753k bull / -$1.5M bear | out (clean 32, ADX 28, RVol 0.5) |
| 5 | **AMZN** | 268.15 | - | **-** | 18 | - | POS +$462.0M | - | 270 | 270 | -$7.2M | +$45k bull / +$0 bear | out (clean 29, ADX 20, RVol 0.7) |
| 6 | **QQQ** | 687.92 | - | **-** | 17 | - | NEG -$595.6M | 690.61 | 700 | 680 | -$73.2M | +$704k bull / -$154k bear | out (clean 31, ADX 27, RVol 0.5) |
| 7 | **SMH** | 501.35 | - | **-** | 17 | - | NEG -$113.1M | - | 500 | 475 | -$1.6M | +$0 bull / -$118k bear | out (clean 30, ADX 22, RVol 0.3) |
| 8 | **META** | 622.34 | - | **-** | 17 | - | NEG -$29.5M | 624.91 | 650 | 600 | +$2.4M | +$47k bull / +$0 bear | out (clean 29, ADX 30, RVol 0.4) |
| 9 | **NVDA** | 164.26 | - | **-** | 16 | - | NEG -$200.1M | - | 170 | 160 | -$67.5M | +$444k bull / -$1.7M bear | out (clean 32, ADX 12, RVol 0.8) |
| 10 | **TSLA** | 390.25 | - | **-** | 16 | - | POS +$355.8M | - | 400 | 380 | +$11.4M | +$260k bull / +$0 bear | out (clean 29, ADX 21, RVol 0.2) |
| 11 | **AVGO** | 363.92 | - | **-** | 16 | - | POS +$136.5M | - | 350 | 350 | +$8.9M | +$34k bull / -$57k bear | out (clean 34, ADX 9, RVol 0.7) |
| 12 | **AMD** | 586.47 | - | **-** | 15 | - | POS +$193.6M | - | 600 | 550 | -$23.6M | +$0 bull / -$1.5M bear | out (clean 34, ADX 17, RVol 0.5) |
| 13 | **DELL** | 372.49 | - | **-** | 15 | - | POS +$5.3M | - | 360 | 340 | +$661k | +$136k bull / +$0 bear | out (clean 37, ADX 17, RVol 0.5) |
| 14 | **MSTR** | 115.36 | - | **-** | 15 | - | NEG -$34.0M | - | 125 | 110 | -$527k | +$40k bull / -$50k bear | out (clean 29, ADX 17, RVol 0.4) |
| 15 | **MU** | 795.47 | - | **-** | 13 | - | POS +$104.8M | - | 800 | 800 | +$5.3M | +$1.2M bull / -$1.1M bear | out (clean 31, ADX 9, RVol 0.5) |
| 16 | **SMCI** | 27.49 | - | **-** | 10 | - | POS +$1.1M | 26.84 | 30 | 25 | +$1.2M | - | out (clean 34, ADX 22, RVol 0.8) |
| 17 | **BABA** | 94.75 | - | **-** | 10 | - | NEG -$18.8M | - | 100 | 100 | +$297k | - | out (clean 28, ADX 19, RVol 1.0) |
| 18 | **IWM** | 279.08 | - | **-** | 9 | - | NEG -$1.4B | 282.59 | 279 | 275 | +$37k | - | out (clean 34, ADX 44, RVol 0.4) |
| 19 | **NFLX** | 63.23 | - | **-** | 9 | - | NEG -$13.8M | 63.78 | 65 | 60 | -$162k | - | out (clean 29, ADX 32, RVol 0.5) |
| 20 | **SHOP** | 146.90 | - | **-** | 8 | - | POS +$2.9M | 144.11 | 150 | 140 | +$5k | - | out (clean 31, ADX 30, RVol 0.3) |
| 21 | **AAPL** | 355.49 | - | **-** | 7 | - | POS +$1.1B | 340.18 | 360 | 350 | +$5.6M | - | out (clean 29, ADX 23, RVol 0.3) |
| 22 | **UBER** | 69.14 | - | **-** | 7 | - | POS +$9.8M | 68.35 | 70 | 70 | -$44k | - | out (clean 32, ADX 20, RVol 0.7) |
| 23 | **CRM** | 217.09 | - | **-** | 6 | - | NEG -$8.6M | - | 220 | 220 | +$43k | - | out (clean 29, ADX 17, RVol 0.1) |
| 24 | **COIN** | 131.58 | - | **-** | 5 | - | POS +$41k | 131.4 | 137 | 135 | +$97k | - | out (clean 30, ADX 20, RVol 0.4) |
| 25 | **ORCL** | 127.02 | - | **-** | 5 | - | POS +$11.0M | 120.74 | 130 | 125 | -$541k | - | out (clean 30, ADX 10, RVol 0.5) |
| 26 | **HOOD** | 82.39 | - | **-** | 5 | - | POS +$10.2M | 80.04 | 85 | 80 | -$8k | - | out (clean 34, ADX 24, RVol 0.6) |
| 27 | **PLTR** | 171.38 | - | **-** | 4 | - | POS +$92.2M | - | 170 | 170 | -$159k | - | out (clean 28, ADX 13, RVol 0.6) |

## Big prints this scan (70)
- **QQQ** CALL 660 2026-11-13 (1DTE): 126 @ 28.00 = **+$353k** BUY | vol 708 / OI 2,581
- **AMD** PUT 585 2026-11-13 (1DTE): 229 @ 11.95 = **+$274k** BUY | vol 5,381 / OI 22
- **SPY** PUT 762 2026-11-12 (0DTE): 585 @ 4.50 = **+$263k** BUY | vol 113,590 / OI 594
- **SPY** PUT 761 2026-11-12 (0DTE): 585 @ 3.53 = **+$207k** BUY | vol 236,046 / OI 178
- **AMD** PUT 587.5 2026-11-13 (1DTE): 154 @ 13.20 = **+$203k** BUY | vol 2,809 / OI 20
- **QQQ** PUT 688 2026-11-12 (0DTE): 992 @ 1.55 = **+$154k** BUY | vol 240,040 / OI 89
- **TSLA** CALL 400 2026-11-13 (1DTE): 1,634 @ 0.93 = **+$152k** BUY | vol 65,129 / OI 13,604
- **AMD** PUT 585 2026-11-13 (1DTE): 109 @ 11.95 = **+$130k** BUY | vol 5,381 / OI 22
- **MSFT** PUT 520 2026-11-13 (1DTE): 313 @ 3.35 = **+$105k** SELL | vol 11,104 / OI 6,123
- **NVDA** CALL 165 2026-11-13 (1DTE): 375 @ 2.76 = **+$104k** SELL | vol 241,776 / OI 2,999
- **AMD** PUT 587.5 2026-11-13 (1DTE): 76 @ 13.20 = **+$100k** BUY | vol 2,809 / OI 20
- **NVDA** PUT 165 2026-11-16 (4DTE): 190 @ 5.00 = **+$95k** BUY | vol 18,213 / OI 2,280
- **DELL** CALL 380 2026-11-13 (1DTE): 120 @ 5.30 = **+$64k** BUY | vol 2,827 / OI 612
- **AMD** PUT 585 2026-11-13 (1DTE): 50 @ 11.95 = **+$60k** BUY | vol 5,381 / OI 22
- **SMH** CALL 500 2026-11-16 (4DTE): 59 @ 10.00 = **+$59k** SELL | vol 246 / OI 430

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 767 2026-11-13 (1DTE): 1,135 traded vs OI 1,125
- **SPY** PUT 756 2026-11-17 (5DTE): 518 traded vs OI 72
- **SPY** CALL 757 2026-11-20 (8DTE): 1,298 traded vs OI 1,297
- **SPY** CALL 825 2026-11-19 (7DTE): 1,000 traded vs OI 31
- **SPY** CALL 810 2026-11-19 (7DTE): 2,224 traded vs OI 209
- **SPY** CALL 795 2026-11-19 (7DTE): 1,905 traded vs OI 141
- **SPY** CALL 820 2026-11-19 (7DTE): 2,600 traded vs OI 100
- **QQQ** PUT 633 2026-11-13 (1DTE): 1,155 traded vs OI 1,046
- **QQQ** PUT 632 2026-11-16 (4DTE): 675 traded vs OI 79
- **QQQ** PUT 639 2026-11-13 (1DTE): 665 traded vs OI 300
- **IWM** CALL 288 2026-11-16 (4DTE): 577 traded vs OI 363
- **IWM** CALL 282.5 2026-11-13 (1DTE): 2,237 traded vs OI 2,234
- **TSLA** PUT 385 2026-11-18 (6DTE): 502 traded vs OI 42
- **AAPL** PUT 337.5 2026-11-16 (4DTE): 515 traded vs OI 283
- **AMD** CALL 605 2026-11-16 (4DTE): 502 traded vs OI 20

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
