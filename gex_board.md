# GEX + FLOW SCAN - Tue Nov 10, 11:10 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (4)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:06 | **SPY** | **PUTS** | 1m FAILED POP (R3 R4) | 11/10 744P | 0.68 | 0.50 | +12% (0m) | **-26%** | +49% | 745.54 |
| 10:15 | **IWM** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/10 280P | 0.63 | 1.31 | +232% (36m) | **+108%** | +22% | 280 hit |
| 09:50 | **SPY** | **PUTS** | FLOW SURGE | 11/10 743P | 0.77 | 0.62 | +21% (60m) | **-19%** (done) | +54% | 745.65 |
| 09:45 | **IWM** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/10 279P | 0.52 | 0.95 | +90% (60m) | **+83%** (done) | +87% | 278.66 |

## 1m RULES on SPY / QQQ - loose (1 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 11:10:08 ET, last candle SPY 11:09, QQQ 11:08 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 11:05 | SPY | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | **FIRE** SPY261110P00744000 |

## Flow surges NOT fired - price disagreed (6 today, last 5)
- 10:15 BABA PUTS: price +0.24 over the last 15 min - flow says one way, price says the other
- 10:10 BABA PUTS: price +0.73 over the last 15 min - flow says one way, price says the other
- 10:00 NFLX CALLS: price -0.14 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:00 AAPL CALLS: price -2.97 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 09:55 BABA CALLS: price -0.98 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **AMZN** | 270.06 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 38 | none: 63 puts 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (14 contracts' greeks worked out here) | POS +$465.1M | - | 270 | 265 | +$7.3M | +$298k bull / +$0 bear | out (clean 33, ADX 23, RVol 0.6) |
| 2 | **AAPL** | 347.65 | FLOW SURGE | **CALLS** | 34 | none: 81 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (15 contracts' greeks worked out here) | POS +$409.9M | 336.1 | 350 | 340 | +$17.9M | +$97k bull / -$76k bear | out (clean 28, ADX 18, RVol 0.7) |
| 3 | **IWM** | 278.90 | TREND (flow not with it) | **PUTS** | 30 | 11/10 279P @ 0.73 (delta 0.52) = est +115% at 277.48 | NEG -$1.3B | 283.65 | 280 | 270 | +$4.5M | - | SHORT (clean 36, ADX 47, RVol 0.9) |
| 4 | **ARM** | 181.39 | - | **-** | 24 | - | NEG -$4.9M | - | 185 | 190 | -$147k | +$0 bull / -$112k bear | out (clean 27, ADX 30, RVol 1.0) |
| 5 | **AMD** | 529.45 | - | **-** | 23 | - | POS +$47.0M | - | 500 | 500 | -$63.2M | +$244k bull / -$2.8M bear | out (clean 31, ADX 26, RVol 1.0) |
| 6 | **UBER** | 69.84 | PINNED between the walls (positive gamma) - chop | **-** | 22 | - | POS +$7.2M | 68.49 | 70 | 70 | -$9k | - | out (clean 33, ADX 40, RVol 0.6) |
| 7 | **NVDA** | 169.57 | - | **-** | 21 | - | NEG -$174.3M | - | 185 | 170 | +$1.4M | +$1.5M bull / -$3.9M bear | out (clean 32, ADX 35, RVol 2.6) |
| 8 | **GOOGL** | 288.53 | - | **-** | 21 | - | NEG -$11.9M | 289.54 | 300 | 290 | +$2.2M | +$278k bull / +$0 bear | out (clean 30, ADX 16, RVol 1.1) |
| 9 | **AVGO** | 329.16 | - | **-** | 21 | - | NEG -$12.8M | 341.8 | 340 | 320 | -$9.5M | +$182k bull / -$402k bear | out (clean 31, ADX 24, RVol 1.1) |
| 10 | **MSTR** | 120.84 | - | **-** | 21 | - | NEG -$20.0M | - | 132 | 110 | -$507k | +$161k bull / -$473k bear | out (clean 29, ADX 32, RVol 1.9) |
| 11 | **PLTR** | 167.55 | - | **-** | 20 | - | POS +$54.5M | - | 165 | 170 | -$191k | +$0 bull / -$52k bear | out (clean 28, ADX 47, RVol 0.6) |
| 12 | **SPY** | 748.24 | - | **-** | 19 | - | NEG -$7.3B | 760.95 | 750 | 730 | +$26.7M | +$7.6M bull / -$1.5M bear | out (clean 32, ADX 33, RVol 1.1) |
| 13 | **TSLA** | 378.11 | - | **-** | 18 | - | POS +$201.3M | - | 400 | 380 | -$8.0M | +$0 bull / -$2.1M bear | out (clean 34, ADX 29, RVol 0.3) |
| 14 | **DELL** | 334.36 | - | **-** | 18 | - | NEG -$8.8M | - | 350 | 340 | +$168k | +$46k bull / -$55k bear | out (clean 32, ADX 29, RVol 1.2) |
| 15 | **QQQ** | 674.76 | - | **-** | 16 | - | NEG -$1.8B | 691.89 | 680 | 680 | -$8.1M | +$695k bull / -$1.7M bear | out (clean 31, ADX 24, RVol 0.6) |
| 16 | **SMH** | 484.16 | - | **-** | 16 | - | NEG -$213.2M | - | 500 | 475 | -$410k | +$58k bull / -$390k bear | out (clean 29, ADX 20, RVol 0.6) |
| 17 | **MU** | 717.16 | - | **-** | 16 | - | NEG -$29.6M | - | 750 | 750 | +$1.5M | +$1.7M bull / -$2.1M bear | out (clean 30, ADX 24, RVol 0.9) |
| 18 | **META** | 642.52 | - | **-** | 15 | - | POS +$252.6M | 605.53 | 650 | 650 | +$576k | +$36k bull / -$66k bear | out (clean 32, ADX 19, RVol 0.5) |
| 19 | **HOOD** | 81.28 | - | **-** | 15 | - | POS +$2.8M | 79.28 | 85 | 80 | +$649k | - | out (clean 30, ADX 36, RVol 0.6) |
| 20 | **CRM** | 212.50 | - | **-** | 15 | - | NEG -$10.8M | - | 195 | 220 | -$84k | - | out (clean 30, ADX 37, RVol 0.2) |
| 21 | **SHOP** | 148.58 | - | **-** | 14 | - | POS +$2.0M | 144.47 | 150 | 140 | +$16k | - | out (clean 31, ADX 38, RVol 0.4) |
| 22 | **BABA** | 103.42 | - | **-** | 14 | - | NEG -$7.6M | 106.14 | 110 | 100 | -$339k | - | out (clean 29, ADX 34, RVol 0.4) |
| 23 | **COIN** | 130.72 | - | **-** | 13 | - | POS +$1.6M | 129.39 | 137 | 135 | +$280k | - | out (clean 30, ADX 35, RVol 0.9) |
| 24 | **MSFT** | 542.79 | - | **-** | 10 | - | POS +$671.9M | - | 550 | 535 | -$374k | - | out (clean 32, ADX 35, RVol 1.0) |
| 25 | **NFLX** | 62.70 | - | **-** | 8 | - | NEG -$24.4M | 66.04 | 65 | 60 | -$123k | - | out (clean 30, ADX 30, RVol 0.7) |
| 26 | **ORCL** | 118.74 | - | **-** | 7 | - | NEG -$23.7M | - | 130 | 120 | +$96k | - | out (clean 28, ADX 29, RVol 0.2) |
| 27 | **SMCI** | 28.10 | - | **-** | 6 | - | POS +$3.4M | - | 30 | 30 | -$14k | - | out (clean 28, ADX 23, RVol 0.5) |

## Big prints this scan (161)
- **NVDA** CALL 165 2026-11-13 (3DTE): 1,498 @ 6.56 = **+$983k** SELL | vol 2,406 / OI 157
- **AMD** CALL 525 2026-11-11 (1DTE): 498 @ 10.00 = **+$498k** SELL | vol 5,880 / OI 146
- **QQQ** PUT 677 2026-11-10 (0DTE): 532 @ 5.00 = **+$266k** BUY | vol 50,293 / OI 271
- **AVGO** CALL 330 2026-11-11 (1DTE): 600 @ 4.00 = **+$240k** SELL | vol 5,871 / OI 600
- **MU** PUT 725 2026-11-11 (1DTE): 100 @ 23.35 = **+$234k** BUY | vol 2,915 / OI 61
- **SPY** PUT 760 2026-11-13 (3DTE): 160 @ 13.93 = **+$223k** BUY | vol 34,129 / OI 5,844
- **SPY** PUT 747 2026-11-10 (0DTE): 1,000 @ 2.20 = **+$220k** BUY | vol 164,814 / OI 315
- **SPY** PUT 760 2026-11-13 (3DTE): 152 @ 13.93 = **+$212k** BUY | vol 34,129 / OI 5,844
- **NVDA** CALL 170 2026-11-16 (6DTE): 400 @ 4.65 = **+$186k** SELL | vol 6,208 / OI 394
- **TSLA** CALL 375 2026-11-11 (1DTE): 364 @ 4.85 = **+$177k** SELL | vol 20,634 / OI 862
- **TSLA** CALL 375 2026-11-11 (1DTE): 360 @ 4.85 = **+$175k** SELL | vol 20,634 / OI 862
- **AVGO** CALL 330 2026-11-11 (1DTE): 399 @ 4.05 = **+$162k** SELL | vol 5,871 / OI 600
- **SPY** PUT 760 2026-11-13 (3DTE): 113 @ 13.93 = **+$157k** BUY | vol 34,129 / OI 5,844
- **SPY** PUT 760 2026-11-13 (3DTE): 112 @ 13.93 = **+$156k** BUY | vol 34,129 / OI 5,844
- **NVDA** CALL 167.5 2026-11-13 (3DTE): 293 @ 5.15 = **+$151k** SELL | vol 2,860 / OI 18

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 722 2026-11-12 (2DTE): 512 traded vs OI 386
- **SPY** PUT 746 2026-11-13 (3DTE): 1,651 traded vs OI 1,288
- **SPY** PUT 738 2026-11-12 (2DTE): 547 traded vs OI 340
- **SPY** CALL 757 2026-11-13 (3DTE): 1,114 traded vs OI 1,103
- **SPY** CALL 750 2026-11-12 (2DTE): 2,084 traded vs OI 2,044
- **SPY** PUT 707 2026-11-12 (2DTE): 1,800 traded vs OI 1,784
- **SPY** PUT 735 2026-11-17 (7DTE): 763 traded vs OI 718
- **QQQ** CALL 666 2026-11-10 (0DTE): 520 traded vs OI 311
- **QQQ** PUT 656 2026-11-11 (1DTE): 1,149 traded vs OI 1,092
- **QQQ** PUT 676 2026-11-12 (2DTE): 504 traded vs OI 16
- **QQQ** CALL 673 2026-11-12 (2DTE): 568 traded vs OI 224
- **IWM** PUT 274 2026-11-12 (2DTE): 558 traded vs OI 115
- **IWM** CALL 281 2026-11-16 (6DTE): 824 traded vs OI 219
- **IWM** CALL 282 2026-11-13 (3DTE): 942 traded vs OI 847
- **SMH** PUT 475 2026-11-11 (1DTE): 736 traded vs OI 263

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
