# GEX + FLOW SCAN - Thu Nov 05, 11:30 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (4)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:55 | **BABA** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/06 102P | 0.75 | 0.31 | -5% (9m) | **-59%** | +27% | 103.58 |
| 09:52 | **SPY** | **PUTS** | 1m WHIPSAW (R1) | 11/05 749P | 0.78 | 11.35 | +1355% (60m) | **+1355%** (done) | +47% | 753.11 hit |
| 09:50 | **BABA** | **CALLS** | TREND + FLOW | 11/06 111C | 0.48 | 0.20 | -12% (0m) | **-58%** (done) | +136% | 110 |
| 09:40 | **QQQ** | **CALLS** | 1m WHIPSAW (R1) | 11/05 683C | 0.78 | 0.10 | -4% (0m) | **-87%** (done) | +66% | 678.43 |

## 1m RULES on SPY / QQQ - loose (3 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 11:30:08 ET, last candle SPY 11:29, QQQ 11:29 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 10:38 | QQQ | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | no contract: 64 puts 0-1DTE > 1 priced 0.40-0.80 > 0 delta 0.15+ > 0 spread ok > 0 liquid  |
| 09:51 | SPY | 1m WHIPSAW | R1 | PUTS | TURNING away | **FIRE** SPY261105P00749000 |
| 09:39 | QQQ | 1m WHIPSAW | R1 | CALLS | AGAINST you | **FIRE** QQQ261105C00683000 |

## Flow surges NOT fired - price disagreed (26 today, last 5)
- 11:15 IWM CALLS: price -0.15 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 11:10 IWM CALLS: price -0.10 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 11:05 IWM CALLS: price -1.05 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 11:00 IWM CALLS: price -1.16 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:55 IWM CALLS: price -2.06 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **IWM** | 276.15 | TREND (flow not with it) | **PUTS** | 59 | 11/05 274P @ 0.40 (delta 0.23) = est +125% at 274.08 | NEG -$2.2B | 285.84 | 285 | 270 | +$46.0M | +$0 bull / -$782k bear | SHORT (clean 36, ADX 54, RVol 2.2) |
| 2 | **ORCL** | 115.08 | TREND (flow not with it) | **PUTS** | 48 | none: 23 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (4 contracts' greeks worked out here) | NEG -$56.2M | - | 125 | 115 | +$2.7M | +$0 bull / -$134k bear | SHORT (clean 34, ADX 52, RVol 1.5) |
| 3 | **SMH** | 464.50 | - | **-** | 37 | - | NEG -$337.8M | - | 505 | 500 | +$37.8M | +$0 bull / -$1.7M bear | out (clean 35, ADX 56, RVol 5.4) |
| 4 | **SPY** | 745.69 | - | **-** | 34 | - | NEG -$11.9B | 769.52 | 760 | 750 | +$986.8M | +$105k bull / -$10.4M bear | out (clean 36, ADX 63, RVol 2.7) |
| 5 | **AVGO** | 305.57 | - | **-** | 32 | - | NEG -$127.9M | - | 330 | 300 | +$6.4M | +$0 bull / -$768k bear | out (clean 32, ADX 48, RVol 2.1) |
| 6 | **PLTR** | 157.11 | - | **-** | 32 | - | NEG -$44.5M | - | 165 | 160 | +$11.6M | +$0 bull / -$304k bear | out (clean 28, ADX 47, RVol 1.1) |
| 7 | **COIN** | 138.78 | - | **-** | 32 | - | POS +$21.8M | - | 142 | 135 | +$1.8M | +$0 bull / -$38k bear | out (clean 33, ADX 57, RVol 0.8) |
| 8 | **NVDA** | 186.62 | - | **-** | 31 | - | NEG -$292.3M | - | 200 | 190 | +$55.3M | +$34k bull / -$2.3M bear | out (clean 33, ADX 62, RVol 3.2) |
| 9 | **MSFT** | 544.56 | - | **-** | 31 | - | POS +$891.9M | - | 540 | 500 | +$18.0M | +$0 bull / -$517k bear | out (clean 32, ADX 49, RVol 1.6) |
| 10 | **DELL** | 334.33 | - | **-** | 31 | - | NEG -$15.9M | - | 360 | 350 | +$5.4M | +$0 bull / -$237k bear | out (clean 35, ADX 44, RVol 2.0) |
| 11 | **QQQ** | 661.31 | - | **-** | 30 | - | NEG -$5.1B | - | 700 | 680 | +$666.4M | +$0 bull / -$13.4M bear | out (clean 35, ADX 60, RVol 2.0) |
| 12 | **TSLA** | 349.89 | - | **-** | 30 | - | NEG -$160.3M | - | 370 | 350 | +$93.5M | +$0 bull / -$2.4M bear | out (clean 35, ADX 51, RVol 2.4) |
| 13 | **MU** | 709.86 | - | **-** | 30 | - | NEG -$128.2M | - | 700 | 750 | +$148.5M | +$0 bull / -$10.2M bear | out (clean 34, ADX 62, RVol 4.0) |
| 14 | **ARM** | 170.68 | - | **-** | 29 | - | NEG -$7.1M | - | 180 | 180 | +$1.3M | +$0 bull / -$134k bear | out (clean 28, ADX 53, RVol 1.6) |
| 15 | **AMZN** | 259.93 | - | **-** | 28 | - | POS +$390.0M | - | 265 | 250 | +$28.2M | +$0 bull / -$239k bear | out (clean 34, ADX 31, RVol 1.4) |
| 16 | **MSTR** | 131.25 | - | **-** | 28 | - | POS +$73.7M | - | 135 | 125 | +$3.2M | +$0 bull / -$238k bear | out (clean 34, ADX 55, RVol 2.3) |
| 17 | **AMD** | 428.58 | - | **-** | 26 | - | NEG -$121.1M | - | 430 | 440 | +$27.8M | +$0 bull / -$2.7M bear | out (clean 34, ADX 50, RVol 1.6) |
| 18 | **META** | 609.09 | - | **-** | 25 | - | NEG -$94.0M | 620.31 | 650 | 600 | +$17.2M | +$0 bull / -$7.8M bear | out (clean 34, ADX 39, RVol 2.3) |
| 19 | **GOOGL** | 285.11 | - | **-** | 24 | - | POS +$31.2M | 281.38 | 290 | 290 | +$7.6M | +$0 bull / -$70k bear | out (clean 35, ADX 26, RVol 0.8) |
| 20 | **NFLX** | 65.74 | - | **-** | 24 | - | POS +$30.7M | 62.02 | 65 | 65 | +$745k | +$208k bull / +$0 bear | out (clean 33, ADX 17, RVol 1.2) |
| 21 | **AAPL** | 347.14 | - | **-** | 23 | - | POS +$579.0M | 334.37 | 350 | 340 | +$15.3M | +$585k bull / -$289k bear | out (clean 31, ADX 23, RVol 2.0) |
| 22 | **HOOD** | 79.32 | - | **-** | 23 | - | NEG -$7.6M | - | 85 | 80 | +$1.1M | +$0 bull / -$111k bear | out (clean 32, ADX 62, RVol 0.8) |
| 23 | **BABA** | 107.18 | - | **-** | 21 | - | POS +$18.9M | - | 110 | 110 | +$1.1M | - | out (clean 37, ADX 18, RVol 2.1) |
| 24 | **SMCI** | 27.25 | - | **-** | 18 | - | NEG -$3.2M | - | 28 | 27 | +$369k | - | out (clean 36, ADX 51, RVol 1.5) |
| 25 | **CRM** | 224.46 | - | **-** | 17 | - | NEG -$14.5M | - | 240 | 220 | +$455k | - | out (clean 33, ADX 16, RVol 0.6) |
| 26 | **SHOP** | 143.45 | - | **-** | 14 | - | NEG -$5.3M | - | 144 | 135 | +$109k | - | out (clean 36, ADX 43, RVol 0.6) |
| 27 | **UBER** | 68.55 | - | **-** | 13 | - | POS +$3.7M | 68.03 | 70 | 65 | +$179k | - | out (clean 32, ADX 17, RVol 1.0) |

## Big prints this scan (274)
- **META** CALL 600 2026-11-11 (6DTE): 2,000 @ 15.75 = **+$3.1M** SELL | vol 2,122 / OI 8
- **META** CALL 635 2026-11-11 (6DTE): 2,000 @ 4.35 = **+$870k** SELL | vol 2,063 / OI 37
- **QQQ** PUT 665 2026-11-06 (1DTE): 400 @ 14.71 = **+$588k** BUY | vol 12,422 / OI 7,114
- **SPY** CALL 742 2026-11-05 (0DTE): 855 @ 5.04 = **+$431k** SELL | vol 24,805 / OI 6
- **QQQ** PUT 690 2026-11-06 (1DTE): 123 @ 32.64 = **+$401k** BUY | vol 3,568 / OI 12,919
- **SPY** PUT 765 2026-11-05 (0DTE): 176 @ 22.46 = **+$395k** BUY | vol 20,752 / OI 2,962
- **QQQ** CALL 650 2026-11-05 (0DTE): 402 @ 9.27 = **+$373k** SELL | vol 14,207 / OI 2
- **META** CALL 597.5 2026-11-06 (1DTE): 287 @ 12.49 = **+$358k** SELL | vol 1,654 / OI 104
- **AVGO** PUT 320 2026-11-06 (1DTE): 150 @ 20.57 = **+$309k** BUY | vol 1,707 / OI 2,510
- **TSLA** CALL 360 2026-11-06 (1DTE): 1,200 @ 2.45 = **+$294k** SELL | vol 27,533 / OI 1,069
- **QQQ** PUT 650 2026-11-06 (1DTE): 400 @ 7.03 = **+$281k** BUY | vol 38,630 / OI 11,913
- **AVGO** PUT 317.5 2026-11-06 (1DTE): 150 @ 18.32 = **+$275k** BUY | vol 261 / OI 936
- **SPY** PUT 762 2026-11-05 (0DTE): 133 @ 19.03 = **+$253k** BUY | vol 37,656 / OI 88
- **QQQ** CALL 650 2026-11-05 (0DTE): 284 @ 8.81 = **+$250k** SELL | vol 14,207 / OI 2
- **SPY** CALL 742 2026-11-05 (0DTE): 495 @ 5.05 = **+$250k** SELL | vol 24,805 / OI 6

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 742 2026-11-10 (5DTE): 523 traded vs OI 162
- **SPY** PUT 727 2026-11-10 (5DTE): 612 traded vs OI 235
- **SPY** CALL 745 2026-11-10 (5DTE): 511 traded vs OI 46
- **SPY** PUT 718 2026-11-09 (4DTE): 503 traded vs OI 9
- **SPY** CALL 746 2026-11-10 (5DTE): 554 traded vs OI 7
- **SPY** CALL 781 2026-11-05 (0DTE): 874 traded vs OI 326
- **SPY** CALL 747 2026-11-10 (5DTE): 527 traded vs OI 0
- **SPY** CALL 775 2026-11-17 (12DTE): 617 traded vs OI 242
- **SPY** PUT 734 2026-11-11 (6DTE): 505 traded vs OI 44
- **SPY** CALL 744 2026-11-13 (8DTE): 562 traded vs OI 70
- **SPY** CALL 757 2026-11-13 (8DTE): 558 traded vs OI 550
- **SPY** CALL 743 2026-11-13 (8DTE): 575 traded vs OI 23
- **SPY** PUT 725 2026-11-12 (7DTE): 504 traded vs OI 453
- **SPY** CALL 760 2026-11-16 (11DTE): 517 traded vs OI 453
- **SPY** PUT 742 2026-11-20 (15DTE): 2,313 traded vs OI 1,227

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
