# GEX + FLOW SCAN - Thu Nov 12, 10:50 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (5)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:35 | **SPY** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/12 754P | 0.59 | 0.38 | +10% (1m) | **-36%** | +70% | 755 |
| 09:50 | **HOOD** | **PUTS** | TREND + FLOW | 11/13 79P | 0.55 | 0.32 | +5% (19m) | **-42%** | +92% | 80 |
| 09:45 | **ORCL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/13 130C | 0.75 | 0.72 | +4% (60m) | **-4%** (done) | +59% | 126.9 |
| 09:45 | **SMCI** | **PUTS** | TREND + FLOW | 11/13 27P | 0.42 | 0.23 | -5% (6m) | **-45%** (done) | +57% | 27 |
| 09:45 | **SPY** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/12 753P | 0.79 | 0.31 | +23% (18m) | **-61%** (done) | +51% | 754.88 |

## 1m RULES on SPY / QQQ - loose (1 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:50:08 ET, last candle SPY 10:49, QQQ 10:49 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 10:03 | SPY | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |

## Flow surges NOT fired - price disagreed (3 today, last 5)
- 10:30 IWM CALLS: price -0.04 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:25 IWM CALLS: price -0.79 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:20 IWM CALLS: price -0.12 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **NVDA** | 163.89 | RUN: clean trend + negative gamma + flow agrees | **PUTS** | 71 | none: 45 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (5 contracts' greeks worked out here) | NEG -$185.1M | - | 170 | 160 | -$93.6M | +$7.9M bull / -$9.3M bear | SHORT (clean 33, ADX 36, RVol 2.1) |
| 2 | **MSTR** | 114.92 | - | **-** | 26 | - | NEG -$33.0M | - | 125 | 110 | -$2.4M | +$0 bull / -$298k bear | out (clean 27, ADX 35, RVol 1.0) |
| 3 | **AVGO** | 359.76 | - | **-** | 25 | - | POS +$133.3M | - | 350 | 350 | +$7.2M | +$468k bull / +$0 bear | out (clean 36, ADX 36, RVol 1.8) |
| 4 | **IWM** | 280.12 | - | **-** | 24 | - | NEG -$1.0B | 282.75 | 285 | 275 | +$5.0M | +$0 bull / -$388k bear | out (clean 34, ADX 52, RVol 0.9) |
| 5 | **MU** | 777.14 | - | **-** | 24 | - | POS +$87.7M | - | 800 | 800 | +$35.3M | +$270k bull / -$1.5M bear | out (clean 32, ADX 42, RVol 0.8) |
| 6 | **ARM** | 199.79 | PINNED between the walls (positive gamma) - chop | **-** | 24 | - | POS +$8.6M | - | 200 | 200 | -$180k | - | out (clean 30, ADX 33, RVol 0.6) |
| 7 | **SMH** | 499.73 | - | **-** | 22 | - | NEG -$135.7M | - | 500 | 475 | -$1.5M | +$0 bull / -$240k bear | out (clean 31, ADX 39, RVol 0.8) |
| 8 | **AMD** | 570.51 | - | **-** | 22 | - | POS +$194.1M | - | 600 | 550 | +$25.4M | +$0 bull / -$1.3M bear | out (clean 34, ADX 24, RVol 1.0) |
| 9 | **PLTR** | 169.71 | PINNED between the walls (positive gamma) - chop | **-** | 22 | - | POS +$86.6M | - | 170 | 170 | +$69k | - | out (clean 27, ADX 45, RVol 0.5) |
| 10 | **META** | 622.33 | - | **-** | 21 | - | NEG -$28.9M | 624.5 | 650 | 600 | +$1.5M | +$0 bull / -$207k bear | out (clean 28, ADX 54, RVol 0.8) |
| 11 | **MSFT** | 525.06 | - | **-** | 21 | - | POS +$112.5M | 519.58 | 535 | 520 | -$2.7M | +$91k bull / +$0 bear | out (clean 31, ADX 32, RVol 0.5) |
| 12 | **BABA** | 94.34 | - | **-** | 21 | - | NEG -$15.9M | - | 100 | 95 | +$249k | - | out (clean 29, ADX 57, RVol 2.4) |
| 13 | **TSLA** | 389.14 | - | **-** | 20 | - | POS +$334.9M | - | 400 | 380 | +$14.3M | +$151k bull / -$76k bear | out (clean 29, ADX 28, RVol 0.3) |
| 14 | **AAPL** | 357.87 | - | **-** | 19 | - | POS +$1.1B | 339.65 | 360 | 360 | +$404k | +$89k bull / -$86k bear | out (clean 28, ADX 43, RVol 0.6) |
| 15 | **AMZN** | 268.55 | - | **-** | 19 | - | POS +$482.9M | - | 270 | 270 | -$4.5M | +$67k bull / -$94k bear | out (clean 31, ADX 26, RVol 0.6) |
| 16 | **GOOGL** | 295.45 | - | **-** | 19 | - | POS +$102.0M | 288.78 | 300 | 290 | +$1.1M | +$92k bull / +$0 bear | out (clean 29, ADX 19, RVol 1.3) |
| 17 | **DELL** | 357.67 | - | **-** | 19 | - | POS +$2.8M | 347.71 | 360 | 340 | +$398k | +$68k bull / -$34k bear | out (clean 36, ADX 35, RVol 0.7) |
| 18 | **COIN** | 130.75 | - | **-** | 18 | - | NEG -$2.2M | 130.99 | 137 | 135 | +$263k | - | out (clean 29, ADX 44, RVol 0.9) |
| 19 | **SPY** | 758.20 | - | **-** | 17 | - | NEG -$2.2B | 760.78 | 760 | 760 | -$29.9M | +$0 bull / -$2.1M bear | out (clean 31, ADX 23, RVol 0.5) |
| 20 | **QQQ** | 686.84 | - | **-** | 17 | - | NEG -$676.8M | 690.2 | 700 | 680 | -$12.4M | +$0 bull / -$133k bear | out (clean 31, ADX 31, RVol 0.5) |
| 21 | **NFLX** | 63.17 | - | **-** | 13 | - | NEG -$14.7M | 63.89 | 65 | 60 | -$179k | - | out (clean 27, ADX 38, RVol 0.6) |
| 22 | **ORCL** | 126.20 | - | **-** | 13 | - | POS +$10.1M | 120.67 | 130 | 125 | -$728k | - | out (clean 29, ADX 26, RVol 0.6) |
| 23 | **SMCI** | 28.05 | - | **-** | 12 | - | POS +$3.1M | - | 30 | 27 | -$58k | - | out (clean 33, ADX 50, RVol 0.9) |
| 24 | **SHOP** | 147.93 | - | **-** | 12 | - | POS +$4.1M | 143.97 | 150 | 140 | -$3k | - | out (clean 30, ADX 24, RVol 1.3) |
| 25 | **HOOD** | 82.14 | - | **-** | 9 | - | POS +$8.0M | 80.16 | 85 | 80 | +$21k | - | out (clean 33, ADX 30, RVol 1.4) |
| 26 | **UBER** | 69.69 | - | **-** | 9 | - | POS +$13.3M | 68.36 | 70 | 70 | -$8k | - | out (clean 31, ADX 33, RVol 0.9) |
| 27 | **CRM** | 215.78 | - | **-** | 6 | - | NEG -$9.2M | - | 220 | 220 | -$7k | - | out (clean 28, ADX 28, RVol 0.3) |

## Big prints this scan (88)
- **NVDA** CALL 160 2026-11-16 (4DTE): 1,000 @ 7.21 = **+$721k** MID | vol 14,235 / OI 766
- **NVDA** CALL 160 2026-11-13 (1DTE): 1,000 @ 6.13 = **+$613k** BUY | vol 116,409 / OI 2,015
- **NVDA** PUT 165 2026-11-13 (1DTE): 500 @ 4.35 = **+$218k** MID | vol 22,082 / OI 19,300
- **NVDA** CALL 162.5 2026-11-13 (1DTE): 368 @ 5.50 = **+$202k** BUY | vol 74,953 / OI 665
- **NVDA** CALL 162.5 2026-11-13 (1DTE): 368 @ 4.45 = **+$164k** SELL | vol 74,953 / OI 665
- **SPY** CALL 753 2026-11-19 (7DTE): 153 @ 9.52 = **+$146k** SELL | vol 607 / OI 109
- **NVDA** CALL 160 2026-11-13 (1DTE): 194 @ 7.07 = **+$137k** BUY | vol 116,409 / OI 2,015
- **SPY** CALL 761 2026-11-13 (1DTE): 1,000 @ 1.37 = **+$137k** SELL | vol 11,711 / OI 6,498
- **QQQ** CALL 661 2026-11-12 (0DTE): 55 @ 24.21 = **+$133k** SELL | vol 107 / OI 181
- **IWM** PUT 278 2026-11-13 (1DTE): 1,500 @ 0.84 = **+$126k** BUY | vol 7,558 / OI 7,514
- **NVDA** PUT 162.5 2026-11-13 (1DTE): 369 @ 3.36 = **+$124k** BUY | vol 36,376 / OI 20,581
- **NVDA** PUT 162.5 2026-11-13 (1DTE): 350 @ 3.40 = **+$119k** BUY | vol 36,376 / OI 20,581
- **NVDA** PUT 162.5 2026-11-16 (4DTE): 280 @ 4.10 = **+$115k** SELL | vol 6,049 / OI 1,267
- **AMD** CALL 560 2026-11-13 (1DTE): 87 @ 11.00 = **+$96k** SELL | vol 4,954 / OI 2,043
- **NVDA** PUT 167.5 2026-11-18 (6DTE): 83 @ 10.26 = **+$85k** BUY | vol 864 / OI 1,818

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 722 2026-11-12 (0DTE): 822 traded vs OI 821
- **SPY** PUT 732 2026-11-12 (0DTE): 1,250 traded vs OI 1,241
- **SPY** CALL 753 2026-11-19 (7DTE): 607 traded vs OI 109
- **QQQ** PUT 694 2026-11-12 (0DTE): 530 traded vs OI 114
- **QQQ** PUT 683 2026-11-16 (4DTE): 509 traded vs OI 204
- **QQQ** CALL 685 2026-11-16 (4DTE): 645 traded vs OI 591
- **QQQ** PUT 673 2026-11-13 (1DTE): 859 traded vs OI 849
- **QQQ** PUT 685 2026-11-18 (6DTE): 503 traded vs OI 102
- **IWM** PUT 278 2026-11-13 (1DTE): 7,558 traded vs OI 7,514
- **NVDA** CALL 170 2026-12-11 (29DTE): 1,304 traded vs OI 1,291
- **NVDA** PUT 165 2026-11-13 (1DTE): 22,082 traded vs OI 19,300
- **NVDA** CALL 170 2026-11-20 (8DTE): 15,896 traded vs OI 15,460
- **NVDA** CALL 170 2026-12-04 (22DTE): 2,189 traded vs OI 2,103
- **TSLA** CALL 400 2026-11-18 (6DTE): 507 traded vs OI 498
- **AAPL** PUT 355 2026-11-20 (8DTE): 1,533 traded vs OI 1,516

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
