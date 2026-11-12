# GEX + FLOW SCAN - Thu Nov 12, 03:15 PM ET
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
Last 1m check 15:15:08 ET, last candle SPY 15:14, QQQ 15:14 | no errors
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
| 1 | **GOOGL** | 299.71 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 39 | none: 72 puts 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (2 contracts' greeks worked out here) | POS +$141.5M | 288.22 | 300 | 290 | -$5.0M | +$586k bull / -$626k bear | out (clean 30, ADX 26, RVol 1.0) |
| 2 | **TSLA** | 393.93 | - | **-** | 20 | - | POS +$375.2M | - | 400 | 380 | +$11.2M | +$0 bull / -$249k bear | out (clean 29, ADX 27, RVol 1.7) |
| 3 | **MSFT** | 521.37 | - | **-** | 20 | - | POS +$32.7M | 519.19 | 535 | 520 | -$1.7M | +$258k bull / +$0 bear | out (clean 33, ADX 47, RVol 0.6) |
| 4 | **ARM** | 199.78 | PINNED between the walls (positive gamma) - chop | **-** | 20 | - | POS +$9.2M | - | 200 | 200 | -$352k | - | out (clean 31, ADX 22, RVol 0.2) |
| 5 | **SPY** | 757.27 | - | **-** | 19 | - | NEG -$3.2B | 760.61 | 760 | 760 | -$104.1M | +$3.0M bull / +$0 bear | out (clean 32, ADX 32, RVol 0.5) |
| 6 | **QQQ** | 687.41 | - | **-** | 18 | - | NEG -$775.3M | 690.22 | 700 | 680 | -$68.4M | +$664k bull / +$0 bear | out (clean 31, ADX 30, RVol 0.4) |
| 7 | **AAPL** | 355.62 | - | **-** | 18 | - | POS +$1.1B | 340.56 | 360 | 350 | +$5.5M | +$27k bull / +$0 bear | out (clean 29, ADX 24, RVol 0.4) |
| 8 | **META** | 621.35 | - | **-** | 18 | - | NEG -$37.7M | 625.24 | 650 | 600 | +$2.5M | +$69k bull / +$0 bear | out (clean 29, ADX 31, RVol 0.3) |
| 9 | **COIN** | 131.23 | FLIP CROSS down into negative gamma | **PUTS** | 18 | none: 26 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (4 contracts' greeks worked out here) | NEG -$437k | 131.3 | 137 | 135 | +$103k | - | out (clean 30, ADX 23, RVol 0.3) |
| 10 | **SMH** | 500.17 | - | **-** | 17 | - | NEG -$118.0M | - | 500 | 475 | -$1.4M | +$117k bull / +$0 bear | out (clean 30, ADX 23, RVol 0.2) |
| 11 | **NVDA** | 163.67 | - | **-** | 16 | - | NEG -$198.9M | - | 170 | 160 | -$66.4M | +$947k bull / -$401k bear | out (clean 32, ADX 13, RVol 0.7) |
| 12 | **ORCL** | 126.52 | - | **-** | 16 | - | POS +$12.5M | 120.99 | 130 | 125 | -$463k | +$75k bull / +$0 bear | out (clean 30, ADX 14, RVol 0.6) |
| 13 | **AMD** | 584.74 | - | **-** | 15 | - | POS +$222.3M | - | 600 | 550 | -$22.5M | +$2.0M bull / +$0 bear | out (clean 35, ADX 17, RVol 0.5) |
| 14 | **DELL** | 371.57 | - | **-** | 15 | - | POS +$7.2M | - | 360 | 400 | +$739k | +$59k bull / +$0 bear | out (clean 37, ADX 18, RVol 0.6) |
| 15 | **MU** | 793.20 | - | **-** | 13 | - | POS +$96.6M | - | 800 | 800 | +$6.6M | +$1.0M bull / -$437k bear | out (clean 31, ADX 8, RVol 0.4) |
| 16 | **NFLX** | 63.06 | - | **-** | 11 | - | NEG -$14.4M | 63.66 | 65 | 60 | -$161k | - | out (clean 30, ADX 39, RVol 0.5) |
| 17 | **SMCI** | 27.18 | - | **-** | 10 | - | NEG -$891k | - | 28 | 25 | +$1.2M | - | out (clean 34, ADX 19, RVol 0.8) |
| 18 | **IWM** | 278.79 | - | **-** | 9 | - | NEG -$1.5B | 282.49 | 285 | 275 | +$75k | - | out (clean 34, ADX 47, RVol 0.6) |
| 19 | **AMZN** | 267.95 | - | **-** | 9 | - | POS +$462.7M | - | 270 | 270 | -$7.1M | - | out (clean 30, ADX 24, RVol 0.8) |
| 20 | **UBER** | 68.98 | - | **-** | 9 | - | POS +$8.2M | 68.37 | 70 | 70 | -$40k | - | out (clean 32, ADX 27, RVol 0.9) |
| 21 | **BABA** | 94.77 | - | **-** | 9 | - | NEG -$19.3M | - | 100 | 100 | +$297k | - | out (clean 28, ADX 16, RVol 0.9) |
| 22 | **SHOP** | 146.81 | - | **-** | 8 | - | POS +$4.3M | 143.03 | 150 | 140 | +$5k | - | out (clean 31, ADX 32, RVol 0.3) |
| 23 | **CRM** | 216.56 | - | **-** | 7 | - | NEG -$7.3M | 225.73 | 220 | 220 | +$43k | - | out (clean 29, ADX 22, RVol 0.1) |
| 24 | **AVGO** | 363.13 | - | **-** | 6 | - | POS +$135.2M | - | 350 | 350 | +$8.9M | - | out (clean 34, ADX 10, RVol 0.7) |
| 25 | **HOOD** | 82.24 | - | **-** | 6 | - | POS +$10.5M | 80.05 | 85 | 80 | -$517 | - | out (clean 34, ADX 25, RVol 0.6) |
| 26 | **PLTR** | 171.34 | - | **-** | 5 | - | POS +$91.0M | - | 170 | 170 | -$168k | - | out (clean 29, ADX 17, RVol 0.7) |
| 27 | **MSTR** | 115.05 | - | **-** | 5 | - | NEG -$33.2M | - | 125 | 110 | -$499k | - | out (clean 29, ADX 20, RVol 0.5) |

## Big prints this scan (29)
- **SPY** CALL 764 2026-11-16 (4DTE): 2,000 @ 1.36 = **+$272k** BUY | vol 5,410 / OI 1,384
- **SMH** PUT 495 2026-11-13 (1DTE): 300 @ 3.90 = **+$117k** SELL | vol 643 / OI 204
- **QQQ** PUT 697 2026-11-13 (1DTE): 100 @ 10.10 = **+$101k** SELL | vol 1,246 / OI 487
- **AMD** CALL 587.5 2026-11-13 (1DTE): 86 @ 11.70 = **+$101k** BUY | vol 7,127 / OI 195
- **AMD** CALL 580 2026-11-13 (1DTE): 53 @ 15.65 = **+$83k** BUY | vol 18,744 / OI 977
- **AMD** CALL 580 2026-11-13 (1DTE): 50 @ 15.95 = **+$80k** BUY | vol 18,744 / OI 977
- **AMD** CALL 600 2026-11-13 (1DTE): 105 @ 6.25 = **+$66k** BUY | vol 52,574 / OI 3,062
- **NVDA** CALL 170 2026-11-13 (1DTE): 500 @ 1.19 = **+$60k** BUY | vol 217,214 / OI 11,191
- **DELL** CALL 372.5 2026-11-13 (1DTE): 74 @ 7.94 = **+$59k** BUY | vol 472 / OI 294
- **NVDA** CALL 170 2026-11-13 (1DTE): 480 @ 1.17 = **+$56k** BUY | vol 217,214 / OI 11,191
- **NVDA** CALL 167.5 2026-11-13 (1DTE): 230 @ 1.92 = **+$44k** BUY | vol 138,725 / OI 6,311
- **NVDA** PUT 165 2026-11-16 (4DTE): 86 @ 4.90 = **+$42k** SELL | vol 19,142 / OI 2,280
- **NVDA** CALL 162.5 2026-11-13 (1DTE): 94 @ 4.30 = **+$40k** BUY | vol 97,034 / OI 665
- **ORCL** PUT 130 2026-11-13 (1DTE): 100 @ 3.75 = **+$38k** SELL | vol 626 / OI 4,540
- **ORCL** PUT 130 2026-11-13 (1DTE): 100 @ 3.75 = **+$38k** SELL | vol 626 / OI 4,540

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 795 2026-11-18 (6DTE): 808 traded vs OI 114
- **SPY** PUT 739 2026-11-13 (1DTE): 3,051 traded vs OI 2,907
- **SPY** CALL 789 2026-11-19 (7DTE): 662 traded vs OI 66
- **SPY** PUT 753 2026-11-19 (7DTE): 672 traded vs OI 71
- **SPY** PUT 735 2026-11-18 (6DTE): 623 traded vs OI 494
- **SPY** CALL 788 2026-11-19 (7DTE): 902 traded vs OI 9
- **SPY** PUT 745 2026-11-18 (6DTE): 928 traded vs OI 732
- **QQQ** CALL 688 2026-11-18 (6DTE): 508 traded vs OI 154
- **QQQ** CALL 713 2026-11-27 (15DTE): 1,126 traded vs OI 1,085
- **SMH** PUT 495 2026-11-13 (1DTE): 643 traded vs OI 204
- **TSLA** CALL 382.5 2026-11-13 (1DTE): 1,155 traded vs OI 1,116
- **ORCL** CALL 128 2026-11-13 (1DTE): 2,065 traded vs OI 2,062

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
