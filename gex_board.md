# GEX + FLOW SCAN - Fri Nov 06, 01:10 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (4)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 12:40 | **SPY** | **CALLS** | 1m WHIPSAW (R1) | 11/06 742C | 0.42 | 0.31 | +14% (6m) | **-26%** | +42% | 739.03 |
| 10:30 | **NVDA** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/06 192.5C | 0.73 | 0.28 | +12% (20m) | **-62%** (done) | +199% | 193.9 |
| 10:00 | **NVDA** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/06 197.5C | 0.67 | 0.03 | -6% (1m) | **-96%** (done) | +24% | 195 |
| 09:50 | **NFLX** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/06 64C | 0.40 | 0.36 | +32% (4m) | **-10%** (done) | +164% | 65 |

## 1m RULES on SPY / QQQ - loose (7 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 13:10:08 ET, last candle SPY 13:09, QQQ 13:09 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 13:00 | QQQ | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | no contract: 40 puts 0-1DTE > 4 priced 0.40-0.80 > 2 delta 0.15+ > 2 spread ok > 2 liquid  |
| 13:00 | SPY | 1m FAILED POP | R3 | PUTS | TURNING away | no contract: 44 puts 0-1DTE > 4 priced 0.40-0.80 > 2 delta 0.15+ > 2 spread ok > 2 liquid  |
| 12:39 | SPY | 1m WHIPSAW | R1 | CALLS | AGAINST you | **FIRE** SPY261106C00742000 |
| 12:38 | QQQ | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |
| 12:38 | SPY | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |
| 12:37 | QQQ | 1m WHIPSAW | R1 R2 | PUTS | WITH you | no contract: 39 puts 0-1DTE > 5 priced 0.40-0.80 > 1 delta 0.15+ > 1 spread ok > 1 liquid  |
| 12:37 | SPY | 1m WHIPSAW | R1 R2 | PUTS | WITH you | no contract: 43 puts 0-1DTE > 3 priced 0.40-0.80 > 1 delta 0.15+ > 1 spread ok > 1 liquid  |

## Flow surges NOT fired - price disagreed (6 today, last 5)
- 09:55 SMCI PUTS: price +0.09 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 HOOD PUTS: price +3.27 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 MSTR PUTS: price +3.75 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 SMCI PUTS: price +0.89 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 PLTR PUTS: price +5.57 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **GOOGL** | 285.17 | PINNED between the walls (positive gamma) - chop | **-** | 28 | - | POS +$70.9M | 282.64 | 285 | 285 | +$2.4M | +$216k bull / -$40k bear | out (clean 34, ADX 18, RVol 0.5) |
| 2 | **ORCL** | 113.83 | - | **-** | 24 | - | NEG -$68.7M | - | 125 | 115 | -$4.1M | +$63k bull / -$1.7M bear | out (clean 30, ADX 24, RVol 1.4) |
| 3 | **DELL** | 326.84 | - | **-** | 23 | - | NEG -$22.8M | - | 330 | 335 | +$5.8M | +$317k bull / +$0 bear | out (clean 31, ADX 19, RVol 1.0) |
| 4 | **COIN** | 132.71 | - | **-** | 21 | - | NEG -$23.4M | 136.76 | 142 | 130 | -$3.1M | +$610k bull / +$0 bear | out (clean 32, ADX 23, RVol 0.4) |
| 5 | **UBER** | 69.17 | - | **-** | 21 | - | POS +$7.7M | 68.73 | 70 | 70 | +$268k | +$0 bull / -$39k bear | out (clean 30, ADX 26, RVol 0.3) |
| 6 | **MSTR** | 126.75 | - | **-** | 20 | - | NEG -$14.6M | 127.87 | 135 | 125 | -$7.5M | +$188k bull / -$631k bear | out (clean 31, ADX 19, RVol 0.3) |
| 7 | **SMH** | 459.52 | - | **-** | 19 | - | NEG -$475.7M | - | 505 | 465 | +$7.4M | +$468k bull / -$1.5M bear | out (clean 33, ADX 18, RVol 0.6) |
| 8 | **TSLA** | 358.42 | - | **-** | 19 | - | NEG -$282.7M | - | 370 | 360 | -$59.3M | +$845k bull / -$1.3M bear | out (clean 35, ADX 22, RVol 0.5) |
| 9 | **IWM** | 273.21 | - | **-** | 17 | - | NEG -$3.1B | 285.3 | 285 | 270 | -$4.3M | +$64k bull / -$178k bear | out (clean 34, ADX 17, RVol 1.0) |
| 10 | **NVDA** | 186.51 | - | **-** | 17 | - | NEG -$394.3M | - | 200 | 190 | +$30.6M | +$2.4M bull / -$2.7M bear | out (clean 33, ADX 19, RVol 0.7) |
| 11 | **AAPL** | 343.98 | - | **-** | 17 | - | NEG -$31.0M | 344.21 | 345 | 345 | -$17.1M | +$115k bull / -$684k bear | out (clean 29, ADX 9, RVol 0.2) |
| 12 | **META** | 617.63 | - | **-** | 17 | - | NEG -$108.7M | 622.95 | 620 | 610 | -$7.2M | +$212k bull / -$729k bear | out (clean 33, ADX 25, RVol 0.5) |
| 13 | **AMZN** | 261.63 | - | **-** | 17 | - | POS +$342.8M | - | 260 | 260 | -$1.5M | +$106k bull / -$1.3M bear | out (clean 35, ADX 29, RVol 0.3) |
| 14 | **MSFT** | 533.37 | - | **-** | 17 | - | POS +$686.1M | 511.6 | 535 | 535 | +$4.5M | +$317k bull / -$231k bear | out (clean 34, ADX 14, RVol 0.5) |
| 15 | **NFLX** | 63.72 | - | **-** | 17 | - | POS +$15.6M | 63.11 | 64 | 64 | -$265k | +$25k bull / +$0 bear | out (clean 32, ADX 20, RVol 0.6) |
| 16 | **MU** | 684.48 | - | **-** | 17 | - | NEG -$162.7M | - | 700 | 700 | +$73.2M | +$7.2M bull / -$3.7M bear | out (clean 32, ADX 15, RVol 0.7) |
| 17 | **HOOD** | 79.17 | - | **-** | 17 | - | NEG -$23.8M | 83.51 | 85 | 80 | +$2.3M | +$272k bull / -$72k bear | out (clean 30, ADX 22, RVol 0.4) |
| 18 | **CRM** | 215.10 | - | **-** | 17 | - | NEG -$27.9M | - | 230 | 215 | -$195k | +$26k bull / +$0 bear | out (clean 35, ADX 23, RVol 0.7) |
| 19 | **QQQ** | 656.40 | - | **-** | 16 | - | NEG -$5.2B | - | 700 | 680 | +$62.2M | +$2.4M bull / -$2.9M bear | out (clean 34, ADX 21, RVol 0.7) |
| 20 | **AMD** | 437.77 | - | **-** | 16 | - | NEG -$174.2M | - | 430 | 440 | +$14.3M | +$697k bull / -$855k bear | out (clean 32, ADX 20, RVol 0.6) |
| 21 | **AVGO** | 291.93 | - | **-** | 16 | - | NEG -$130.6M | - | 320 | 300 | +$2.1M | +$1.3M bull / -$395k bear | out (clean 31, ADX 21, RVol 0.5) |
| 22 | **PLTR** | 160.59 | - | **-** | 16 | - | NEG -$70.4M | - | 165 | 160 | +$3.4M | +$330k bull / +$0 bear | out (clean 28, ADX 14, RVol 0.4) |
| 23 | **SPY** | 737.02 | - | **-** | 15 | - | NEG -$14.0B | 766.69 | 770 | 740 | -$16.7M | +$1.0M bull / -$1.1M bear | out (clean 34, ADX 23, RVol 0.5) |
| 24 | **SHOP** | 149.45 | - | **-** | 15 | - | NEG -$4.3M | 151.48 | 150 | 150 | -$1.1M | - | out (clean 36, ADX 22, RVol 0.4) |
| 25 | **ARM** | 171.11 | - | **-** | 8 | - | NEG -$25.2M | - | 180 | 170 | -$547k | - | out (clean 26, ADX 14, RVol 0.5) |
| 26 | **SMCI** | 28.06 | - | **-** | 7 | - | NEG -$5.0M | - | 30 | 28 | -$377k | - | out (clean 34, ADX 20, RVol 0.4) |
| 27 | **BABA** | 109.08 | - | **-** | 7 | - | POS +$25.8M | 104.98 | 110 | 110 | -$461k | - | out (clean 34, ADX 15, RVol 0.5) |

## Big prints this scan (117)
- **MU** PUT 675 2026-11-13 (7DTE): 200 @ 33.10 = **+$662k** MID | vol 814 / OI 0
- **MSTR** PUT 128 2026-11-13 (7DTE): 870 @ 7.25 = **+$631k** BUY | vol 2,252 / OI 177
- **SMH** PUT 450 2026-11-09 (3DTE): 890 @ 6.49 = **+$578k** BUY | vol 1,924 / OI 233
- **SMH** PUT 452.5 2026-11-09 (3DTE): 400 @ 7.25 = **+$290k** BUY | vol 769 / OI 0
- **MU** PUT 700 2026-11-09 (3DTE): 70 @ 30.40 = **+$213k** BUY | vol 4,437 / OI 183
- **QQQ** PUT 680 2026-11-13 (7DTE): 75 @ 27.44 = **+$206k** BUY | vol 741 / OI 10,074
- **AMZN** CALL 265 2026-11-13 (7DTE): 472 @ 3.85 = **+$182k** SELL | vol 8,418 / OI 2,381
- **QQQ** PUT 655 2026-11-06 (0DTE): 657 @ 2.49 = **+$164k** BUY | vol 163,944 / OI 6,673
- **QQQ** PUT 655 2026-11-06 (0DTE): 492 @ 3.20 = **+$157k** BUY | vol 163,944 / OI 6,673
- **AMZN** CALL 265 2026-11-13 (7DTE): 400 @ 3.86 = **+$154k** SELL | vol 8,418 / OI 2,381
- **AMZN** CALL 265 2026-11-13 (7DTE): 400 @ 3.86 = **+$154k** SELL | vol 8,418 / OI 2,381
- **QQQ** PUT 655 2026-11-09 (3DTE): 200 @ 7.65 = **+$153k** BUY | vol 14,739 / OI 1,021
- **QQQ** PUT 655 2026-11-09 (3DTE): 200 @ 7.65 = **+$153k** BUY | vol 14,739 / OI 1,021
- **QQQ** PUT 655 2026-11-06 (0DTE): 500 @ 3.00 = **+$150k** BUY | vol 163,944 / OI 6,673
- **QQQ** PUT 655 2026-11-09 (3DTE): 200 @ 7.00 = **+$140k** BUY | vol 14,739 / OI 1,021

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 769 2026-11-09 (3DTE): 846 traded vs OI 827
- **SPY** PUT 708 2026-11-10 (4DTE): 594 traded vs OI 587
- **SPY** PUT 723 2026-11-10 (4DTE): 510 traded vs OI 332
- **SPY** CALL 758 2026-11-12 (6DTE): 506 traded vs OI 83
- **SPY** PUT 705 2026-11-10 (4DTE): 504 traded vs OI 388
- **QQQ** CALL 651 2026-11-09 (3DTE): 504 traded vs OI 0
- **QQQ** PUT 620 2026-11-10 (4DTE): 610 traded vs OI 602
- **QQQ** CALL 686 2026-11-10 (4DTE): 640 traded vs OI 85
- **QQQ** CALL 690 2026-11-12 (6DTE): 515 traded vs OI 183
- **QQQ** PUT 625 2026-11-12 (6DTE): 1,004 traded vs OI 294
- **IWM** PUT 274 2026-11-11 (5DTE): 507 traded vs OI 446
- **IWM** CALL 280 2026-11-13 (7DTE): 1,741 traded vs OI 1,635
- **IWM** CALL 279 2026-11-12 (6DTE): 541 traded vs OI 77
- **IWM** CALL 279 2026-11-13 (7DTE): 852 traded vs OI 800
- **SMH** CALL 462.5 2026-11-09 (3DTE): 621 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
