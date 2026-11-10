# GEX + FLOW SCAN - Tue Nov 10, 11:05 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (3)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:15 | **IWM** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/10 280P | 0.63 | 1.63 | +232% (36m) | **+159%** | +22% | 280 hit |
| 09:50 | **SPY** | **PUTS** | FLOW SURGE | 11/10 743P | 0.77 | 0.62 | +21% (60m) | **-19%** (done) | +54% | 745.65 |
| 09:45 | **IWM** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/10 279P | 0.52 | 0.95 | +90% (60m) | **+83%** (done) | +87% | 278.66 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 11:05:08 ET, last candle SPY 11:04, QQQ 11:04 | no errors

## Flow surges NOT fired - price disagreed (6 today, last 5)
- 10:15 BABA PUTS: price +0.24 over the last 15 min - flow says one way, price says the other
- 10:10 BABA PUTS: price +0.73 over the last 15 min - flow says one way, price says the other
- 10:00 NFLX CALLS: price -0.14 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:00 AAPL CALLS: price -2.97 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 09:55 BABA CALLS: price -0.98 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **AMZN** | 269.99 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 38 | none: 63 puts 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (2 contracts' greeks worked out here) | POS +$470.1M | - | 270 | 265 | +$6.1M | +$449k bull / +$0 bear | out (clean 33, ADX 25, RVol 0.5) |
| 2 | **IWM** | 278.67 | TREND (flow not with it) | **PUTS** | 33 | 11/10 278P @ 0.52 (delta 0.37) = est +111% at 277.22 | NEG -$1.4B | 283.78 | 280 | 270 | +$4.6M | - | SHORT (clean 36, ADX 47, RVol 1.1) |
| 3 | **AAPL** | 347.75 | - | **-** | 27 | - | POS +$405.8M | 336 | 350 | 340 | +$18.0M | +$134k bull / -$137k bear | out (clean 28, ADX 18, RVol 0.7) |
| 4 | **AMD** | 528.11 | - | **-** | 23 | - | POS +$46.8M | - | 500 | 500 | -$63.7M | +$2.3M bull / -$1.3M bear | out (clean 31, ADX 26, RVol 1.1) |
| 5 | **NVDA** | 169.68 | - | **-** | 22 | - | NEG -$173.4M | - | 185 | 170 | +$6.5M | +$2.2M bull / -$1.2M bear | out (clean 32, ADX 35, RVol 2.5) |
| 6 | **UBER** | 69.95 | PINNED between the walls (positive gamma) - chop | **-** | 22 | - | POS +$7.6M | 68.46 | 70 | 70 | -$10k | - | out (clean 33, ADX 40, RVol 0.6) |
| 7 | **GOOGL** | 288.24 | - | **-** | 21 | - | NEG -$11.3M | 289.28 | 300 | 290 | +$2.1M | +$280k bull / +$0 bear | out (clean 30, ADX 16, RVol 0.9) |
| 8 | **AVGO** | 328.57 | - | **-** | 21 | - | NEG -$14.7M | 343.58 | 340 | 320 | -$8.6M | +$207k bull / +$0 bear | out (clean 31, ADX 25, RVol 1.0) |
| 9 | **PLTR** | 167.81 | - | **-** | 21 | - | POS +$53.3M | - | 165 | 170 | -$195k | +$0 bull / -$52k bear | out (clean 28, ADX 47, RVol 0.9) |
| 10 | **MSTR** | 120.67 | - | **-** | 20 | - | NEG -$20.6M | - | 132 | 110 | -$319k | +$214k bull / -$473k bear | out (clean 29, ADX 32, RVol 1.9) |
| 11 | **SPY** | 748.24 | - | **-** | 19 | - | NEG -$7.4B | 760.97 | 750 | 730 | +$30.7M | +$11.3M bull / -$122k bear | out (clean 32, ADX 33, RVol 1.1) |
| 12 | **TSLA** | 377.22 | - | **-** | 18 | - | POS +$193.5M | - | 400 | 380 | -$8.2M | +$462k bull / -$811k bear | out (clean 34, ADX 31, RVol 0.3) |
| 13 | **DELL** | 332.03 | - | **-** | 18 | - | NEG -$11.3M | - | 350 | 340 | +$264k | +$128k bull / -$55k bear | out (clean 32, ADX 29, RVol 1.1) |
| 14 | **MU** | 713.47 | - | **-** | 17 | - | NEG -$34.1M | - | 750 | 750 | +$8.2M | +$4.4M bull / +$0 bear | out (clean 30, ADX 24, RVol 0.8) |
| 15 | **ORCL** | 118.58 | - | **-** | 17 | - | NEG -$23.9M | - | 130 | 120 | +$164k | +$136k bull / +$0 bear | out (clean 28, ADX 29, RVol 0.2) |
| 16 | **QQQ** | 674.19 | - | **-** | 16 | - | NEG -$1.9B | 692.63 | 680 | 680 | -$7.5M | +$3.3M bull / -$1.1M bear | out (clean 31, ADX 25, RVol 0.7) |
| 17 | **SMH** | 483.64 | - | **-** | 16 | - | NEG -$216.6M | - | 500 | 475 | +$180k | +$58k bull / -$112k bear | out (clean 29, ADX 21, RVol 0.7) |
| 18 | **HOOD** | 81.24 | - | **-** | 16 | - | POS +$2.4M | 79.35 | 85 | 80 | +$701k | - | out (clean 30, ADX 36, RVol 0.6) |
| 19 | **META** | 642.95 | - | **-** | 15 | - | POS +$254.0M | 606.34 | 650 | 650 | -$329k | +$269k bull / -$31k bear | out (clean 32, ADX 20, RVol 0.4) |
| 20 | **CRM** | 212.68 | - | **-** | 15 | - | NEG -$10.9M | - | 195 | 220 | -$86k | - | out (clean 30, ADX 37, RVol 0.2) |
| 21 | **COIN** | 130.91 | - | **-** | 14 | - | POS +$1.8M | 128.95 | 137 | 135 | +$346k | - | out (clean 30, ADX 34, RVol 0.8) |
| 22 | **SHOP** | 148.66 | - | **-** | 14 | - | POS +$1.9M | 144.73 | 150 | 140 | +$16k | - | out (clean 31, ADX 38, RVol 0.4) |
| 23 | **BABA** | 103.61 | - | **-** | 14 | - | NEG -$7.0M | 106.03 | 110 | 100 | -$350k | - | out (clean 29, ADX 34, RVol 0.4) |
| 24 | **ARM** | 180.80 | - | **-** | 13 | - | NEG -$5.0M | - | 185 | 190 | -$134k | - | out (clean 27, ADX 30, RVol 1.0) |
| 25 | **MSFT** | 542.91 | - | **-** | 10 | - | POS +$677.3M | - | 550 | 535 | -$343k | - | out (clean 32, ADX 36, RVol 0.9) |
| 26 | **NFLX** | 62.79 | - | **-** | 8 | - | NEG -$22.7M | 65.52 | 65 | 60 | -$122k | - | out (clean 30, ADX 30, RVol 0.6) |
| 27 | **SMCI** | 28.00 | - | **-** | 8 | - | POS +$3.1M | - | 30 | 30 | +$54k | - | out (clean 28, ADX 23, RVol 0.5) |

## Big prints this scan (111)
- **SPY** PUT 760 2026-11-13 (3DTE): 2,000 @ 12.55 = **+$2.5M** SELL | vol 33,338 / OI 5,844
- **AMD** CALL 512.5 2026-11-11 (1DTE): 205 @ 17.30 = **+$355k** SELL | vol 3,175 / OI 442
- **SMH** PUT 485 2026-11-13 (3DTE): 270 @ 11.65 = **+$315k** MID | vol 1,668 / OI 308
- **QQQ** PUT 679 2026-11-16 (6DTE): 200 @ 11.58 = **+$232k** BUY | vol 384 / OI 98
- **QQQ** CALL 674 2026-11-10 (0DTE): 990 @ 2.21 = **+$219k** SELL | vol 48,582 / OI 417
- **NVDA** CALL 172.5 2026-11-16 (6DTE): 500 @ 3.55 = **+$178k** SELL | vol 5,609 / OI 10
- **NVDA** CALL 172.5 2026-11-16 (6DTE): 500 @ 3.55 = **+$178k** SELL | vol 5,609 / OI 10
- **AMD** PUT 520 2026-11-11 (1DTE): 168 @ 10.40 = **+$175k** BUY | vol 2,608 / OI 31
- **MU** PUT 700 2026-11-11 (1DTE): 172 @ 9.50 = **+$163k** SELL | vol 9,220 / OI 160
- **MU** PUT 700 2026-11-11 (1DTE): 164 @ 9.00 = **+$148k** SELL | vol 9,220 / OI 160
- **QQQ** PUT 674 2026-11-10 (0DTE): 500 @ 2.87 = **+$144k** BUY | vol 72,224 / OI 221
- **QQQ** PUT 676 2026-11-10 (0DTE): 300 @ 4.16 = **+$125k** BUY | vol 57,557 / OI 296
- **GOOGL** PUT 280 2026-11-13 (3DTE): 1,000 @ 1.24 = **+$124k** SELL | vol 2,021 / OI 2,369
- **AMD** PUT 525 2026-11-11 (1DTE): 96 @ 12.90 = **+$124k** BUY | vol 2,950 / OI 28
- **QQQ** PUT 676 2026-11-10 (0DTE): 300 @ 4.11 = **+$123k** BUY | vol 57,557 / OI 296

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 754 2026-11-12 (2DTE): 564 traded vs OI 141
- **SPY** CALL 755 2026-11-16 (6DTE): 881 traded vs OI 859
- **SPY** CALL 747 2026-11-12 (2DTE): 573 traded vs OI 292
- **SPY** PUT 726 2026-11-12 (2DTE): 604 traded vs OI 568
- **SPY** CALL 755 2026-11-13 (3DTE): 4,301 traded vs OI 4,237
- **SPY** CALL 746 2026-11-12 (2DTE): 505 traded vs OI 301
- **SPY** PUT 750 2026-11-12 (2DTE): 1,598 traded vs OI 1,591
- **SPY** CALL 753 2026-11-13 (3DTE): 1,209 traded vs OI 1,205
- **SPY** CALL 763 2026-11-13 (3DTE): 1,276 traded vs OI 1,247
- **SPY** CALL 745 2026-11-12 (2DTE): 728 traded vs OI 695
- **SPY** PUT 715 2026-11-18 (8DTE): 613 traded vs OI 347
- **SPY** CALL 755 2026-11-24 (14DTE): 525 traded vs OI 0
- **SPY** PUT 740 2026-11-24 (14DTE): 619 traded vs OI 0
- **SPY** CALL 750 2026-11-24 (14DTE): 688 traded vs OI 0
- **QQQ** CALL 680 2026-11-12 (2DTE): 1,143 traded vs OI 1,134

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
