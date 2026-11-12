# GEX + FLOW SCAN - Thu Nov 12, 02:30 PM ET
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
Last 1m check 14:30:08 ET, last candle SPY 14:29, QQQ 14:29 | no errors
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
| 1 | **GOOGL** | 300.20 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 29 | none: 72 puts 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (5 contracts' greeks worked out here) | POS +$135.4M | 288.42 | 300 | 290 | -$5.2M | - | out (clean 30, ADX 24, RVol 0.9) |
| 2 | **ARM** | 200.33 | PINNED between the walls (positive gamma) - chop | **-** | 29 | - | POS +$10.3M | - | 200 | 200 | -$339k | +$0 bull / -$71k bear | out (clean 31, ADX 21, RVol 0.2) |
| 3 | **MSFT** | 523.80 | - | **-** | 21 | - | POS +$78.3M | 519.8 | 535 | 520 | -$3.8M | +$60k bull / -$65k bear | out (clean 32, ADX 38, RVol 0.8) |
| 4 | **SPY** | 758.62 | - | **-** | 18 | - | NEG -$2.0B | 760.63 | 760 | 760 | -$131.9M | +$0 bull / -$1.1M bear | out (clean 31, ADX 21, RVol 0.4) |
| 5 | **IWM** | 279.49 | - | **-** | 18 | - | NEG -$1.3B | 282.65 | 285 | 275 | -$892k | +$0 bull / -$88k bear | out (clean 34, ADX 38, RVol 0.5) |
| 6 | **QQQ** | 688.88 | - | **-** | 17 | - | NEG -$481.3M | 690.63 | 700 | 680 | -$89.8M | +$710k bull / -$2.6M bear | out (clean 31, ADX 19, RVol 0.5) |
| 7 | **AMZN** | 269.10 | - | **-** | 17 | - | POS +$496.5M | - | 270 | 270 | -$7.5M | +$0 bull / -$31k bear | out (clean 29, ADX 11, RVol 0.6) |
| 8 | **NVDA** | 164.57 | - | **-** | 16 | - | NEG -$191.8M | - | 170 | 160 | -$60.6M | +$870k bull / -$606k bear | out (clean 32, ADX 12, RVol 0.8) |
| 9 | **TSLA** | 390.07 | - | **-** | 16 | - | POS +$359.1M | - | 400 | 380 | +$11.2M | +$0 bull / -$49k bear | out (clean 29, ADX 22, RVol 0.2) |
| 10 | **AVGO** | 365.14 | - | **-** | 16 | - | POS +$133.3M | - | 350 | 350 | +$8.5M | +$0 bull / -$27k bear | out (clean 34, ADX 10, RVol 0.6) |
| 11 | **AMD** | 584.23 | - | **-** | 14 | - | POS +$195.3M | - | 600 | 550 | -$21.3M | +$0 bull / -$1.0M bear | out (clean 34, ADX 12, RVol 0.5) |
| 12 | **MSTR** | 115.70 | - | **-** | 14 | - | NEG -$32.1M | - | 125 | 110 | -$767k | +$28k bull / +$0 bear | out (clean 28, ADX 13, RVol 0.4) |
| 13 | **MU** | 797.48 | - | **-** | 13 | - | POS +$99.1M | - | 800 | 800 | +$2.3M | +$0 bull / -$1.6M bear | out (clean 31, ADX 12, RVol 0.5) |
| 14 | **SMCI** | 27.78 | - | **-** | 11 | - | POS +$1.6M | 26.67 | 30 | 25 | +$1.0M | - | out (clean 34, ADX 24, RVol 1.2) |
| 15 | **BABA** | 94.46 | - | **-** | 10 | - | NEG -$15.3M | - | 100 | 100 | +$314k | - | out (clean 29, ADX 17, RVol 1.0) |
| 16 | **AAPL** | 355.67 | - | **-** | 8 | - | POS +$1.1B | 340.48 | 360 | 350 | +$4.7M | - | out (clean 29, ADX 24, RVol 0.5) |
| 17 | **SMH** | 501.86 | - | **-** | 7 | - | NEG -$101.6M | - | 500 | 500 | -$1.7M | - | out (clean 30, ADX 18, RVol 0.5) |
| 18 | **NFLX** | 63.41 | - | **-** | 7 | - | NEG -$10.6M | 63.89 | 65 | 65 | -$184k | - | out (clean 28, ADX 17, RVol 0.5) |
| 19 | **META** | 622.57 | - | **-** | 6 | - | NEG -$26.5M | 625.02 | 650 | 600 | +$2.0M | - | out (clean 28, ADX 24, RVol 0.2) |
| 20 | **UBER** | 69.64 | - | **-** | 6 | - | POS +$14.7M | 68.37 | 70 | 70 | -$56k | - | out (clean 31, ADX 12, RVol 0.2) |
| 21 | **CRM** | 217.44 | - | **-** | 6 | - | NEG -$8.6M | 226.27 | 220 | 220 | +$40k | - | out (clean 29, ADX 18, RVol 0.1) |
| 22 | **ORCL** | 127.28 | - | **-** | 5 | - | POS +$10.9M | 121.83 | 130 | 125 | -$602k | - | out (clean 30, ADX 8, RVol 0.5) |
| 23 | **HOOD** | 82.78 | - | **-** | 5 | - | POS +$10.3M | 80.12 | 85 | 80 | -$39k | - | out (clean 34, ADX 18, RVol 0.8) |
| 24 | **SHOP** | 147.47 | - | **-** | 5 | - | POS +$3.1M | 144.25 | 150 | 140 | +$406 | - | out (clean 31, ADX 25, RVol 0.3) |
| 25 | **PLTR** | 171.89 | - | **-** | 4 | - | POS +$93.8M | - | 170 | 170 | -$271k | - | out (clean 28, ADX 9, RVol 0.5) |
| 26 | **COIN** | 132.22 | - | **-** | 4 | - | POS +$2.3M | 131.32 | 137 | 135 | +$61k | - | out (clean 30, ADX 14, RVol 0.3) |
| 27 | **DELL** | 374.53 | - | **-** | 4 | - | POS +$5.2M | - | 360 | 380 | +$361k | - | out (clean 37, ADX 18, RVol 0.4) |

## Big prints this scan (56)
- **QQQ** CALL 660 2026-11-13 (1DTE): 108 @ 30.10 = **+$325k** BUY | vol 556 / OI 2,581
- **QQQ** PUT 692 2026-11-16 (4DTE): 200 @ 7.21 = **+$144k** SELL | vol 2,310 / OI 112
- **QQQ** CALL 660 2026-11-13 (1DTE): 42 @ 30.10 = **+$126k** BUY | vol 556 / OI 2,581
- **QQQ** CALL 689 2026-11-12 (0DTE): 760 @ 1.51 = **+$115k** BUY | vol 124,847 / OI 311
- **AMD** CALL 580 2026-11-13 (1DTE): 70 @ 12.95 = **+$91k** SELL | vol 17,900 / OI 977
- **AMD** PUT 580 2026-11-13 (1DTE): 70 @ 10.60 = **+$74k** BUY | vol 10,669 / OI 4
- **AMD** PUT 577.5 2026-11-13 (1DTE): 70 @ 9.60 = **+$67k** BUY | vol 3,394 / OI 10
- **AMD** PUT 577.5 2026-11-13 (1DTE): 70 @ 9.60 = **+$67k** BUY | vol 3,394 / OI 10
- **MU** CALL 800 2026-11-16 (4DTE): 30 @ 19.40 = **+$58k** SELL | vol 2,170 / OI 853
- **AMD** CALL 585 2026-11-13 (1DTE): 50 @ 10.41 = **+$52k** SELL | vol 11,300 / OI 962
- **AMD** CALL 600 2026-11-13 (1DTE): 95 @ 5.00 = **+$48k** SELL | vol 48,664 / OI 3,062
- **NVDA** CALL 157.5 2026-11-16 (4DTE): 50 @ 9.24 = **+$46k** BUY | vol 4,231 / OI 102
- **NVDA** CALL 165 2026-11-16 (4DTE): 99 @ 4.30 = **+$43k** SELL | vol 33,270 / OI 1,076
- **AMD** CALL 590 2026-11-13 (1DTE): 50 @ 8.34 = **+$42k** SELL | vol 23,339 / OI 1,196
- **NVDA** PUT 165 2026-11-13 (1DTE): 124 @ 3.34 = **+$41k** SELL | vol 108,790 / OI 19,300

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 805 2026-12-04 (22DTE): 2,772 traded vs OI 745
- **SMH** PUT 477.5 2026-11-27 (15DTE): 5,028 traded vs OI 7
- **NVDA** PUT 152.5 2026-11-23 (11DTE): 500 traded vs OI 38
- **AMD** CALL 620 2026-11-27 (15DTE): 623 traded vs OI 332
- **AMZN** PUT 257.5 2026-11-18 (6DTE): 500 traded vs OI 26
- **GOOGL** CALL 300 2026-11-27 (15DTE): 5,271 traded vs OI 4,804
- **AVGO** PUT 332.5 2026-11-20 (8DTE): 572 traded vs OI 563
- **SMCI** CALL 30.5 2026-11-20 (8DTE): 515 traded vs OI 0
- **MSTR** CALL 126 2026-11-20 (8DTE): 5,652 traded vs OI 0
- **MSTR** CALL 120 2026-11-20 (8DTE): 7,109 traded vs OI 1,652

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
