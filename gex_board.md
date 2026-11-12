# GEX + FLOW SCAN - Thu Nov 12, 12:20 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (5)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:35 | **SPY** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/12 754P | 0.59 | 0.17 | +10% (1m) | **-71%** (done) | +70% | 755 |
| 09:50 | **HOOD** | **PUTS** | TREND + FLOW | 11/13 79P | 0.55 | 0.36 | +5% (19m) | **-35%** (done) | +92% | 80 |
| 09:45 | **ORCL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/13 130C | 0.75 | 0.72 | +4% (60m) | **-4%** (done) | +59% | 126.9 |
| 09:45 | **SMCI** | **PUTS** | TREND + FLOW | 11/13 27P | 0.42 | 0.23 | -5% (6m) | **-45%** (done) | +57% | 27 |
| 09:45 | **SPY** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/12 753P | 0.79 | 0.31 | +23% (18m) | **-61%** (done) | +51% | 754.88 |

## 1m RULES on SPY / QQQ - loose (1 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 12:20:08 ET, last candle SPY 12:19, QQQ 12:19 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 10:03 | SPY | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |

## Flow surges NOT fired - price disagreed (7 today, last 5)
- 12:00 SMCI CALLS: price -0.27 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 11:55 SMCI CALLS: price -0.04 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 11:50 SMCI CALLS: price -0.48 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 11:45 SMCI CALLS: price -0.74 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:30 IWM CALLS: price -0.04 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **SMCI** | 26.50 | TREND (flow not with it) | **PUTS** | 53 | 11/13 26P @ 0.60 (delta 0.38) = est +122% at 25 | NEG -$1.3M | - | 28 | 25 | +$1.6M | - | SHORT (clean 34, ADX 47, RVol 4.7) |
| 2 | **GOOGL** | 300.64 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 46 | none: 72 puts 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (2 contracts' greeks worked out here) | POS +$142.0M | 288.58 | 300 | 290 | -$5.1M | +$0 bull / -$942k bear | out (clean 29, ADX 37, RVol 1.4) |
| 3 | **AMZN** | 269.48 | PINNED between the walls (positive gamma) - chop | **-** | 30 | - | POS +$511.4M | - | 270 | 270 | -$7.1M | +$318k bull / -$157k bear | out (clean 30, ADX 13, RVol 0.6) |
| 4 | **QQQ** | 690.26 | FLIP CROSS down into negative gamma | **PUTS** | 28 | 11/12 687P @ 0.75 (delta 0.25) = est +121% at 686.61 | NEG -$79.7M | 690.48 | 700 | 680 | -$95.5M | +$794k bull / -$812k bear | out (clean 31, ADX 17, RVol 0.3) |
| 5 | **BABA** | 94.60 | - | **-** | 26 | - | NEG -$15.4M | - | 100 | 95 | +$361k | +$62k bull / +$0 bear | out (clean 28, ADX 38, RVol 1.3) |
| 6 | **MSFT** | 528.34 | - | **-** | 21 | - | POS +$203.1M | 520.36 | 535 | 520 | -$5.0M | +$62k bull / +$0 bear | out (clean 31, ADX 29, RVol 0.5) |
| 7 | **ARM** | 200.06 | PINNED between the walls (positive gamma) - chop | **-** | 20 | - | POS +$9.7M | - | 200 | 200 | -$253k | - | out (clean 31, ADX 22, RVol 0.2) |
| 8 | **SPY** | 760.71 | FLIP CROSS down into negative gamma | **PUTS** | 19 | none: 654 puts 0-7DTE > 48 priced 0.40-0.80 > 2 delta 0.2+ > 2 spread ok > 2 liquid > best one only -10% at the target (needs +20%) (247 contracts' greeks worked out here) | NEG -$570.9M | 761.31 | 760 | 760 | -$130.2M | - | out (clean 32, ADX 16, RVol 0.3) |
| 9 | **NVDA** | 164.74 | - | **-** | 19 | - | NEG -$184.6M | - | 170 | 160 | -$78.8M | +$2.6M bull / -$1.2M bear | out (clean 32, ADX 22, RVol 0.9) |
| 10 | **DELL** | 373.58 | - | **-** | 19 | - | POS +$4.8M | - | 360 | 340 | -$356k | +$246k bull / -$57k bear | out (clean 37, ADX 25, RVol 1.7) |
| 11 | **AMD** | 580.45 | - | **-** | 18 | - | POS +$196.0M | - | 600 | 550 | -$18.7M | +$2.9M bull / -$1.3M bear | out (clean 34, ADX 29, RVol 0.7) |
| 12 | **AVGO** | 363.44 | - | **-** | 18 | - | POS +$133.7M | - | 350 | 350 | +$7.0M | +$0 bull / -$91k bear | out (clean 35, ADX 23, RVol 0.8) |
| 13 | **SMH** | 501.32 | - | **-** | 17 | - | NEG -$102.1M | - | 500 | 500 | -$1.2M | +$88k bull / -$32k bear | out (clean 31, ADX 20, RVol 0.4) |
| 14 | **META** | 624.65 | - | **-** | 17 | - | POS +$2.1M | 624.13 | 650 | 600 | +$1.8M | +$88k bull / -$132k bear | out (clean 28, ADX 27, RVol 0.5) |
| 15 | **TSLA** | 391.00 | - | **-** | 16 | - | POS +$365.6M | - | 400 | 380 | +$10.1M | +$150k bull / -$33k bear | out (clean 29, ADX 18, RVol 0.2) |
| 16 | **AAPL** | 356.65 | - | **-** | 16 | - | POS +$1.1B | 339.92 | 360 | 360 | +$1.4M | +$522k bull / +$0 bear | out (clean 28, ADX 23, RVol 0.7) |
| 17 | **MU** | 785.98 | - | **-** | 15 | - | POS +$90.8M | - | 800 | 800 | +$11.1M | +$1.5M bull / -$575k bear | out (clean 31, ADX 18, RVol 0.3) |
| 18 | **UBER** | 69.58 | - | **-** | 10 | - | POS +$14.8M | 68.38 | 70 | 70 | -$80k | - | out (clean 31, ADX 19, RVol 0.4) |
| 19 | **NFLX** | 63.79 | - | **-** | 9 | - | NEG -$5.3M | 64.04 | 65 | 65 | -$209k | - | out (clean 28, ADX 18, RVol 0.6) |
| 20 | **MSTR** | 116.92 | - | **-** | 9 | - | NEG -$29.1M | - | 125 | 110 | -$1.7M | - | out (clean 28, ADX 20, RVol 1.2) |
| 21 | **PLTR** | 171.79 | - | **-** | 8 | - | POS +$94.6M | - | 170 | 170 | -$458k | - | out (clean 28, ADX 19, RVol 0.7) |
| 22 | **ORCL** | 126.89 | - | **-** | 6 | - | POS +$10.7M | 120.66 | 130 | 125 | -$363k | - | out (clean 29, ADX 16, RVol 0.4) |
| 23 | **CRM** | 217.93 | - | **-** | 6 | - | NEG -$8.1M | - | 220 | 220 | +$2k | - | out (clean 29, ADX 25, RVol 0.5) |
| 24 | **COIN** | 132.99 | - | **-** | 5 | - | POS +$6.4M | 131.19 | 137 | 135 | +$6k | - | out (clean 29, ADX 22, RVol 0.4) |
| 25 | **HOOD** | 83.19 | - | **-** | 5 | - | POS +$12.2M | 80.11 | 85 | 80 | -$71k | - | out (clean 34, ADX 17, RVol 0.5) |
| 26 | **IWM** | 280.95 | - | **-** | 4 | - | NEG -$784.2M | 282.69 | 285 | 275 | -$1.3M | - | out (clean 34, ADX 18, RVol 0.2) |
| 27 | **SHOP** | 148.57 | - | **-** | 4 | - | POS +$5.3M | 143.95 | 150 | 140 | -$1k | - | out (clean 29, ADX 14, RVol 0.5) |

## Big prints this scan (58)
- **GOOGL** CALL 290 2026-11-13 (1DTE): 396 @ 11.05 = **+$438k** SELL | vol 1,182 / OI 5,773
- **GOOGL** CALL 290 2026-11-13 (1DTE): 396 @ 11.00 = **+$436k** SELL | vol 1,182 / OI 5,773
- **AAPL** CALL 360 2026-11-13 (1DTE): 4,365 @ 0.82 = **+$358k** BUY | vol 64,693 / OI 16,819
- **QQQ** CALL 670 2026-11-13 (1DTE): 59 @ 22.21 = **+$131k** BUY | vol 701 / OI 2,726
- **AMD** CALL 590 2026-11-13 (1DTE): 100 @ 9.10 = **+$91k** BUY | vol 19,226 / OI 1,196
- **NVDA** PUT 172.5 2026-11-13 (1DTE): 100 @ 8.35 = **+$84k** SELL | vol 5,167 / OI 0
- **NVDA** CALL 165 2026-11-18 (6DTE): 100 @ 8.16 = **+$82k** BUY | vol 8,250 / OI 517
- **NVDA** PUT 162.5 2026-11-13 (1DTE): 300 @ 2.46 = **+$74k** SELL | vol 91,400 / OI 20,581
- **NVDA** CALL 165 2026-11-13 (1DTE): 199 @ 3.60 = **+$72k** SELL | vol 192,652 / OI 2,999
- **DELL** PUT 360 2026-11-13 (1DTE): 198 @ 3.45 = **+$68k** SELL | vol 3,042 / OI 331
- **NVDA** PUT 160 2026-11-16 (4DTE): 242 @ 2.71 = **+$66k** SELL | vol 30,834 / OI 4,794
- **NVDA** PUT 170 2026-11-13 (1DTE): 100 @ 6.45 = **+$64k** SELL | vol 20,398 / OI 14,967
- **NVDA** PUT 160 2026-11-16 (4DTE): 200 @ 2.85 = **+$57k** SELL | vol 30,834 / OI 4,794
- **NVDA** CALL 162.5 2026-11-13 (1DTE): 110 @ 5.05 = **+$56k** BUY | vol 88,368 / OI 665
- **MU** PUT 790 2026-11-13 (1DTE): 35 @ 15.81 = **+$55k** SELL | vol 6,523 / OI 457

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 748 2026-11-12 (0DTE): 1,089 traded vs OI 1,067
- **SPY** CALL 764 2026-11-19 (7DTE): 642 traded vs OI 310
- **SPY** CALL 835 2026-11-19 (7DTE): 3,401 traded vs OI 0
- **NVDA** PUT 177.5 2026-11-16 (4DTE): 503 traded vs OI 0
- **AMD** PUT 590 2026-11-20 (8DTE): 575 traded vs OI 99
- **GOOGL** CALL 305 2026-11-20 (8DTE): 5,562 traded vs OI 4,629
- **NFLX** PUT 62 2026-11-13 (1DTE): 7,342 traded vs OI 7,230
- **AVGO** CALL 375 2026-11-18 (6DTE): 516 traded vs OI 8
- **AVGO** CALL 365 2026-11-18 (6DTE): 508 traded vs OI 31
- **PLTR** PUT 162.5 2026-11-13 (1DTE): 1,492 traded vs OI 1,255
- **MU** PUT 810 2026-12-04 (22DTE): 526 traded vs OI 427
- **MSTR** PUT 115 2026-11-13 (1DTE): 3,777 traded vs OI 3,473

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
