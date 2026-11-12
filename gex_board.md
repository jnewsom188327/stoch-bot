# GEX + FLOW SCAN - Thu Nov 12, 03:35 PM ET
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
| 1 | **GOOGL** | 299.79 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 39 | none: 72 puts 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (16 contracts' greeks worked out here) | POS +$142.3M | 288.4 | 300 | 290 | -$5.6M | +$80k bull / +$0 bear | out (clean 30, ADX 26, RVol 0.9) |
| 2 | **TSLA** | 398.59 | - | **-** | 25 | - | POS +$394.4M | - | 400 | 400 | -$22.3M | +$0 bull / -$9.1M bear | out (clean 30, ADX 38, RVol 3.9) |
| 3 | **MSFT** | 521.98 | - | **-** | 21 | - | POS +$45.0M | 519.78 | 535 | 520 | -$2.3M | +$1.2M bull / +$0 bear | out (clean 33, ADX 47, RVol 0.8) |
| 4 | **SPY** | 756.77 | - | **-** | 20 | - | NEG -$3.0B | 760.03 | 760 | 760 | -$106.4M | +$487k bull / +$0 bear | out (clean 32, ADX 35, RVol 0.7) |
| 5 | **IWM** | 278.51 | - | **-** | 20 | - | NEG -$1.5B | 282.51 | 285 | 275 | +$71k | +$211k bull / +$0 bear | out (clean 34, ADX 46, RVol 0.9) |
| 6 | **QQQ** | 686.54 | - | **-** | 19 | - | NEG -$611.7M | 689.78 | 700 | 680 | -$67.4M | +$388k bull / -$7.3M bear | out (clean 31, ADX 33, RVol 0.7) |
| 7 | **SMH** | 498.51 | - | **-** | 18 | - | NEG -$119.4M | - | 500 | 475 | -$1.2M | +$41k bull / +$0 bear | out (clean 31, ADX 26, RVol 0.5) |
| 8 | **META** | 620.13 | - | **-** | 18 | - | NEG -$43.3M | 624.75 | 650 | 600 | +$3.6M | +$704k bull / +$0 bear | out (clean 29, ADX 32, RVol 0.3) |
| 9 | **NVDA** | 163.20 | - | **-** | 16 | - | NEG -$203.2M | - | 170 | 160 | -$66.6M | +$2.1M bull / -$246k bear | out (clean 32, ADX 12, RVol 0.8) |
| 10 | **AMD** | 580.51 | - | **-** | 15 | - | POS +$217.3M | - | 600 | 550 | -$18.2M | +$1.0M bull / +$0 bear | out (clean 35, ADX 15, RVol 0.6) |
| 11 | **PLTR** | 171.15 | - | **-** | 15 | - | POS +$94.1M | - | 170 | 170 | -$4k | +$165k bull / +$0 bear | out (clean 29, ADX 18, RVol 0.7) |
| 12 | **MU** | 791.89 | - | **-** | 13 | - | POS +$100.3M | - | 800 | 800 | +$6.2M | +$490k bull / -$692k bear | out (clean 31, ADX 10, RVol 0.6) |
| 13 | **NFLX** | 62.98 | - | **-** | 12 | - | NEG -$17.2M | 63.63 | 65 | 60 | -$173k | - | out (clean 30, ADX 46, RVol 0.8) |
| 14 | **AMZN** | 267.60 | - | **-** | 11 | - | POS +$459.6M | - | 270 | 270 | -$7.7M | - | out (clean 30, ADX 30, RVol 1.4) |
| 15 | **BABA** | 94.25 | - | **-** | 11 | - | NEG -$14.7M | - | 100 | 95 | +$325k | - | out (clean 28, ADX 17, RVol 1.5) |
| 16 | **SMCI** | 27.02 | - | **-** | 10 | - | NEG -$924k | 28.62 | 28 | 25 | +$1.2M | - | out (clean 34, ADX 18, RVol 0.8) |
| 17 | **UBER** | 69.05 | - | **-** | 10 | - | POS +$7.9M | 68.43 | 70 | 70 | -$44k | - | out (clean 33, ADX 30, RVol 1.0) |
| 18 | **COIN** | 130.50 | - | **-** | 9 | - | NEG -$3.3M | 131.37 | 137 | 130 | +$127k | - | out (clean 30, ADX 30, RVol 0.9) |
| 19 | **ARM** | 198.50 | - | **-** | 9 | - | POS +$9.2M | - | 200 | 200 | -$332k | - | out (clean 32, ADX 25, RVol 0.3) |
| 20 | **AAPL** | 355.48 | - | **-** | 7 | - | POS +$1.1B | 341.56 | 360 | 350 | +$5.3M | - | out (clean 29, ADX 23, RVol 0.5) |
| 21 | **AVGO** | 361.67 | - | **-** | 7 | - | POS +$132.7M | - | 350 | 350 | +$9.0M | - | out (clean 35, ADX 13, RVol 1.1) |
| 22 | **DELL** | 367.83 | - | **-** | 7 | - | POS +$5.7M | - | 360 | 400 | +$805k | - | out (clean 38, ADX 23, RVol 1.1) |
| 23 | **MSTR** | 114.95 | - | **-** | 7 | - | NEG -$33.1M | - | 125 | 110 | -$586k | - | out (clean 29, ADX 21, RVol 1.0) |
| 24 | **ORCL** | 126.27 | - | **-** | 7 | - | POS +$12.1M | 120.8 | 130 | 125 | -$420k | - | out (clean 31, ADX 19, RVol 0.6) |
| 25 | **HOOD** | 81.86 | - | **-** | 7 | - | POS +$8.7M | 80.1 | 85 | 80 | +$55k | - | out (clean 34, ADX 28, RVol 0.7) |
| 26 | **CRM** | 216.64 | - | **-** | 7 | - | NEG -$6.8M | 224.08 | 220 | 220 | +$44k | - | out (clean 30, ADX 25, RVol 0.3) |
| 27 | **SHOP** | 146.53 | - | **-** | 7 | - | POS +$4.3M | 143.59 | 150 | 140 | +$5k | - | out (clean 32, ADX 30, RVol 0.3) |

## Big prints this scan (85)
- **QQQ** PUT 680 2026-11-17 (5DTE): 5,000 @ 5.51 = **+$2.8M** BUY | vol 5,650 / OI 350
- **QQQ** PUT 720 2026-11-13 (1DTE): 339 @ 33.85 = **+$1.1M** BUY | vol 983 / OI 243
- **MSFT** PUT 547.5 2026-11-13 (1DTE): 408 @ 24.62 = **+$1.0M** SELL | vol 503 / OI 746
- **QQQ** PUT 688 2026-11-13 (1DTE): 1,250 @ 5.06 = **+$632k** BUY | vol 21,405 / OI 307
- **QQQ** PUT 687 2026-11-13 (1DTE): 1,250 @ 4.59 = **+$574k** BUY | vol 22,287 / OI 658
- **QQQ** PUT 686 2026-11-13 (1DTE): 1,250 @ 4.18 = **+$522k** BUY | vol 15,314 / OI 444
- **QQQ** PUT 685 2026-11-13 (1DTE): 1,250 @ 3.81 = **+$476k** BUY | vol 42,755 / OI 23,912
- **META** PUT 635 2026-11-13 (1DTE): 199 @ 15.30 = **+$304k** SELL | vol 1,005 / OI 1,158
- **NVDA** PUT 162.5 2026-11-16 (4DTE): 707 @ 3.60 = **+$255k** SELL | vol 24,880 / OI 1,267
- **META** PUT 635 2026-11-13 (1DTE): 160 @ 15.30 = **+$245k** SELL | vol 1,005 / OI 1,158
- **NVDA** PUT 162.5 2026-11-16 (4DTE): 639 @ 3.76 = **+$240k** SELL | vol 24,880 / OI 1,267
- **MSFT** PUT 547.5 2026-11-13 (1DTE): 78 @ 24.63 = **+$192k** SELL | vol 503 / OI 746
- **NVDA** CALL 170 2026-11-18 (6DTE): 347 @ 5.25 = **+$182k** BUY | vol 16,234 / OI 3,097
- **SPY** CALL 755 2026-11-12 (0DTE): 659 @ 2.40 = **+$158k** BUY | vol 50,869 / OI 1,837
- **QQQ** CALL 688 2026-11-13 (1DTE): 320 @ 4.09 = **+$131k** BUY | vol 15,223 / OI 917

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 777 2026-11-17 (5DTE): 643 traded vs OI 632
- **SPY** CALL 788 2026-11-20 (8DTE): 4,122 traded vs OI 2,403
- **SPY** CALL 825 2026-11-23 (11DTE): 601 traded vs OI 100
- **SPY** CALL 830 2026-11-27 (15DTE): 600 traded vs OI 495
- **SPY** PUT 757 2026-11-27 (15DTE): 519 traded vs OI 517
- **QQQ** PUT 671 2026-11-16 (4DTE): 506 traded vs OI 145
- **QQQ** PUT 618 2026-11-13 (1DTE): 1,313 traded vs OI 0
- **QQQ** PUT 661 2026-11-16 (4DTE): 553 traded vs OI 333
- **QQQ** PUT 677 2026-11-16 (4DTE): 504 traded vs OI 226
- **QQQ** CALL 720 2026-11-25 (13DTE): 796 traded vs OI 0
- **QQQ** CALL 718 2026-11-27 (15DTE): 547 traded vs OI 471
- **QQQ** PUT 688 2026-12-04 (22DTE): 551 traded vs OI 75
- **NVDA** CALL 155 2026-11-25 (13DTE): 509 traded vs OI 1
- **NVDA** CALL 165 2026-11-25 (13DTE): 592 traded vs OI 89
- **TSLA** PUT 372.5 2026-11-16 (4DTE): 503 traded vs OI 204

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
