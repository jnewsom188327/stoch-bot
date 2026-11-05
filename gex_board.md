# GEX + FLOW SCAN - Thu Nov 05, 03:55 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (5)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 15:00 | **SMCI** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/06 28.5C | 0.46 | 0.32 | -7% (0m) | **-30%** (done) | +29% | 28.14 |
| 10:55 | **BABA** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/06 102P | 0.75 | 0.33 | -5% (9m) | **-56%** (done) | +27% | 103.58 |
| 09:52 | **SPY** | **PUTS** | 1m WHIPSAW (R1) | 11/05 749P | 0.78 | 11.35 | +1355% (60m) | **+1355%** (done) | +47% | 753.11 hit |
| 09:50 | **BABA** | **CALLS** | TREND + FLOW | 11/06 111C | 0.48 | 0.20 | -12% (0m) | **-58%** (done) | +136% | 110 |
| 09:40 | **QQQ** | **CALLS** | 1m WHIPSAW (R1) | 11/05 683C | 0.78 | 0.10 | -4% (0m) | **-87%** (done) | +66% | 678.43 |

## 1m RULES on SPY / QQQ - loose (5 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 15:32:08 ET, last candle SPY 15:31, QQQ 15:31 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 13:05 | SPY | 1m WHIPSAW | R1 | CALLS | AGAINST you | no contract: 87 calls 0-1DTE > 8 priced 0.40-0.80 > 1 delta 0.15+ > 1 spread ok > 1 liquid |
| 11:44 | SPY | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |
| 10:38 | QQQ | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | no contract: 64 puts 0-1DTE > 1 priced 0.40-0.80 > 0 delta 0.15+ > 0 spread ok > 0 liquid  |
| 09:51 | SPY | 1m WHIPSAW | R1 | PUTS | TURNING away | **FIRE** SPY261105P00749000 |
| 09:39 | QQQ | 1m WHIPSAW | R1 | CALLS | AGAINST you | **FIRE** QQQ261105C00683000 |

## Flow surges NOT fired - price disagreed (36 today, last 5)
- 12:55 IWM CALLS: price -0.16 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 12:50 IWM CALLS: price -0.60 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 12:45 IWM CALLS: price -0.70 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 12:40 IWM CALLS: price -0.66 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 12:20 IWM CALLS: under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **SPY** | 735.84 | - | **-** | 27 | - | NEG -$14.5B | 771.09 | 760 | 735 | +$1.3B | +$8.3M bull / -$23.1M bear | out (clean 36, ADX 24, RVol 2.7) |
| 2 | **AVGO** | 296.14 | - | **-** | 27 | - | NEG -$113.0M | - | 325 | 300 | +$9.5M | +$173k bull / -$134k bear | out (clean 32, ADX 21, RVol 3.2) |
| 3 | **SMH** | 452.66 | - | **-** | 26 | - | NEG -$281.8M | - | 445 | 465 | +$32.4M | +$124k bull / +$0 bear | out (clean 34, ADX 18, RVol 2.4) |
| 4 | **DELL** | 320.40 | - | **-** | 26 | - | NEG -$15.4M | - | 310 | 340 | +$7.2M | +$54k bull / +$0 bear | out (clean 33, ADX 22, RVol 1.6) |
| 5 | **QQQ** | 651.63 | - | **-** | 25 | - | NEG -$4.8B | - | 700 | 650 | +$880.5M | +$22.1M bull / -$2.7M bear | out (clean 36, ADX 20, RVol 3.7) |
| 6 | **IWM** | 271.60 | - | **-** | 25 | - | NEG -$3.0B | 287.25 | 285 | 270 | +$54.4M | +$679k bull / -$164k bear | out (clean 36, ADX 20, RVol 2.6) |
| 7 | **PLTR** | 155.61 | - | **-** | 25 | - | NEG -$52.8M | - | 165 | 150 | +$12.0M | +$35k bull / -$118k bear | out (clean 27, ADX 13, RVol 2.0) |
| 8 | **MSFT** | 537.11 | - | **-** | 24 | - | POS +$761.0M | - | 540 | 500 | +$22.7M | +$209k bull / -$354k bear | out (clean 32, ADX 22, RVol 1.2) |
| 9 | **MU** | 670.70 | - | **-** | 24 | - | NEG -$95.2M | - | 700 | 700 | +$244.1M | +$4.8M bull / -$109k bear | out (clean 32, ADX 18, RVol 2.5) |
| 10 | **ARM** | 169.94 | - | **-** | 24 | - | NEG -$6.8M | - | 180 | 180 | +$1.4M | +$0 bull / -$44k bear | out (clean 26, ADX 13, RVol 2.5) |
| 11 | **NVDA** | 183.31 | - | **-** | 23 | - | NEG -$281.1M | - | 200 | 190 | +$76.7M | +$854k bull / -$54k bear | out (clean 34, ADX 16, RVol 1.8) |
| 12 | **TSLA** | 344.89 | - | **-** | 23 | - | NEG -$158.4M | - | 370 | 350 | +$106.6M | +$127k bull / -$298k bear | out (clean 35, ADX 13, RVol 3.4) |
| 13 | **AAPL** | 346.08 | - | **-** | 23 | - | POS +$470.4M | 335.48 | 350 | 330 | +$25.1M | +$378k bull / -$323k bear | out (clean 31, ADX 19, RVol 2.5) |
| 14 | **BABA** | 108.24 | - | **-** | 23 | - | POS +$20.6M | - | 110 | 110 | +$726k | +$0 bull / -$30k bear | out (clean 35, ADX 22, RVol 2.1) |
| 15 | **GOOGL** | 283.43 | - | **-** | 21 | - | POS +$17.3M | 281.2 | 285 | 290 | +$8.9M | +$28k bull / +$0 bear | out (clean 34, ADX 17, RVol 1.3) |
| 16 | **MSTR** | 130.40 | - | **-** | 21 | - | POS +$51.1M | - | 135 | 125 | +$3.6M | +$0 bull / -$95k bear | out (clean 33, ADX 19, RVol 2.0) |
| 17 | **NFLX** | 65.50 | - | **-** | 20 | - | POS +$27.3M | 62.26 | 65 | 65 | +$615k | +$0 bull / -$25k bear | out (clean 32, ADX 24, RVol 1.1) |
| 18 | **AMD** | 413.69 | - | **-** | 19 | - | NEG -$114.3M | - | 430 | 440 | +$35.9M | +$2.5M bull / -$165k bear | out (clean 32, ADX 16, RVol 1.0) |
| 19 | **CRM** | 222.64 | - | **-** | 19 | - | NEG -$16.3M | - | 240 | 220 | +$532k | - | out (clean 33, ADX 14, RVol 3.2) |
| 20 | **META** | 605.66 | - | **-** | 18 | - | NEG -$132.5M | 621.04 | 650 | 600 | +$18.3M | +$50k bull / +$0 bear | out (clean 33, ADX 10, RVol 1.9) |
| 21 | **COIN** | 138.84 | - | **-** | 13 | - | POS +$12.9M | 134.16 | 142 | 130 | +$1.5M | - | out (clean 33, ADX 24, RVol 1.1) |
| 22 | **UBER** | 68.68 | - | **-** | 12 | - | POS +$2.6M | 68.26 | 70 | 65 | +$195k | - | out (clean 29, ADX 17, RVol 1.7) |
| 23 | **HOOD** | 79.12 | - | **-** | 11 | - | NEG -$14.9M | - | 85 | 80 | +$1.8M | - | out (clean 30, ADX 20, RVol 2.7) |
| 24 | **AMZN** | 260.18 | - | **-** | 10 | - | POS +$357.1M | - | 265 | 250 | +$24.5M | - | out (clean 34, ADX 12, RVol 1.0) |
| 25 | **SMCI** | 27.39 | - | **-** | 8 | - | NEG -$4.1M | - | 28 | 27 | +$206k | - | out (clean 34, ADX 18, RVol 1.2) |
| 26 | **ORCL** | 116.12 | - | **-** | 8 | - | NEG -$66.8M | - | 125 | 115 | +$2.9M | - | out (clean 31, ADX 11, RVol 0.8) |
| 27 | **SHOP** | 144.13 | - | **-** | 8 | - | NEG -$5.9M | - | 144 | 135 | -$95k | - | out (clean 37, ADX 14, RVol 1.6) |

## Big prints this scan (103)
- **AMD** CALL 415 2026-11-06 (1DTE): 600 @ 10.72 = **+$643k** BUY | vol 6,649 / OI 33
- **AMD** CALL 417.5 2026-11-06 (1DTE): 600 @ 9.55 = **+$573k** BUY | vol 2,993 / OI 36
- **QQQ** PUT 660 2026-11-05 (0DTE): 500 @ 10.11 = **+$506k** MID | vol 155,230 / OI 2,574
- **QQQ** PUT 655 2026-11-06 (1DTE): 500 @ 9.95 = **+$498k** SELL | vol 37,524 / OI 5,889
- **SPY** PUT 769 2026-11-05 (0DTE): 100 @ 33.66 = **+$337k** SELL | vol 3,617 / OI 3
- **QQQ** PUT 651 2026-11-05 (0DTE): 1,350 @ 2.08 = **+$281k** BUY | vol 158,773 / OI 200
- **QQQ** PUT 660 2026-11-05 (0DTE): 289 @ 9.16 = **+$265k** SELL | vol 155,230 / OI 2,574
- **SPY** PUT 760 2026-11-09 (4DTE): 100 @ 23.82 = **+$238k** SELL | vol 4,941 / OI 1,984
- **QQQ** PUT 660 2026-11-06 (1DTE): 180 @ 13.00 = **+$234k** SELL | vol 40,248 / OI 14,507
- **SPY** PUT 760 2026-11-09 (4DTE): 87 @ 24.32 = **+$212k** MID | vol 4,941 / OI 1,984
- **SPY** PUT 760 2026-11-09 (4DTE): 87 @ 24.16 = **+$210k** SELL | vol 4,941 / OI 1,984
- **SPY** PUT 745 2026-11-06 (1DTE): 196 @ 10.55 = **+$207k** SELL | vol 32,195 / OI 14,342
- **QQQ** PUT 660 2026-11-05 (0DTE): 199 @ 10.14 = **+$202k** MID | vol 155,230 / OI 2,574
- **QQQ** PUT 655 2026-11-06 (1DTE): 200 @ 9.92 = **+$198k** SELL | vol 37,524 / OI 5,889
- **AMD** CALL 417.5 2026-11-06 (1DTE): 200 @ 9.75 = **+$195k** BUY | vol 2,993 / OI 36

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 703 2026-11-09 (4DTE): 500 traded vs OI 371
- **SPY** CALL 765 2026-11-16 (11DTE): 510 traded vs OI 312
- **SPY** PUT 736 2026-11-18 (13DTE): 594 traded vs OI 0
- **SPY** CALL 733 2026-11-20 (15DTE): 581 traded vs OI 175
- **SPY** PUT 738 2026-11-30 (25DTE): 820 traded vs OI 806
- **SPY** CALL 779 2026-12-04 (29DTE): 570 traded vs OI 185
- **QQQ** PUT 664 2026-11-09 (4DTE): 508 traded vs OI 17
- **QQQ** CALL 654 2026-11-12 (7DTE): 500 traded vs OI 0
- **QQQ** PUT 610 2026-11-12 (7DTE): 992 traded vs OI 281
- **IWM** PUT 262 2026-11-10 (5DTE): 666 traded vs OI 62
- **TSLA** CALL 352.5 2026-11-13 (8DTE): 500 traded vs OI 12
- **TSLA** PUT 320 2026-12-04 (29DTE): 500 traded vs OI 297
- **TSLA** PUT 337.5 2026-11-13 (8DTE): 563 traded vs OI 130
- **AAPL** PUT 315 2026-11-09 (4DTE): 835 traded vs OI 228
- **AAPL** PUT 317.5 2026-11-09 (4DTE): 517 traded vs OI 254

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
