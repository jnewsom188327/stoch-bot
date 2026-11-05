# GEX + FLOW SCAN - Thu Nov 05, 03:45 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (5)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 15:00 | **SMCI** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/06 28.5C | 0.46 | 0.31 | -7% (0m) | **-33%** | +29% | 28.14 |
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
| 1 | **SPY** | 734.38 | - | **-** | 27 | - | NEG -$13.9B | 769.42 | 760 | 735 | +$1.3B | +$7.1M bull / +$0 bear | out (clean 36, ADX 25, RVol 2.2) |
| 2 | **AVGO** | 294.60 | - | **-** | 27 | - | NEG -$113.4M | - | 320 | 300 | +$9.5M | +$121k bull / +$0 bear | out (clean 31, ADX 22, RVol 2.4) |
| 3 | **NFLX** | 65.13 | PINNED between the walls (positive gamma) - chop | **-** | 26 | - | POS +$27.9M | 62.77 | 65 | 65 | +$743k | - | out (clean 32, ADX 23, RVol 1.0) |
| 4 | **QQQ** | 650.22 | - | **-** | 25 | - | NEG -$4.6B | - | 700 | 650 | +$864.5M | +$4.3M bull / -$196k bear | out (clean 35, ADX 20, RVol 3.2) |
| 5 | **MSFT** | 533.76 | - | **-** | 25 | - | POS +$697.0M | - | 540 | 500 | +$24.1M | +$777k bull / +$0 bear | out (clean 32, ADX 24, RVol 1.0) |
| 6 | **PLTR** | 154.37 | - | **-** | 25 | - | NEG -$52.9M | - | 165 | 150 | +$12.5M | +$85k bull / +$0 bear | out (clean 27, ADX 14, RVol 1.6) |
| 7 | **IWM** | 270.93 | - | **-** | 24 | - | NEG -$2.9B | - | 285 | 270 | +$55.4M | +$679k bull / +$0 bear | out (clean 36, ADX 22, RVol 1.8) |
| 8 | **SMH** | 451.78 | - | **-** | 24 | - | NEG -$275.7M | - | 445 | 465 | +$30.8M | +$192k bull / +$0 bear | out (clean 34, ADX 18, RVol 1.5) |
| 9 | **TSLA** | 342.48 | - | **-** | 23 | - | NEG -$160.6M | - | 350 | 350 | +$107.8M | +$171k bull / -$594k bear | out (clean 35, ADX 14, RVol 2.9) |
| 10 | **BABA** | 107.86 | - | **-** | 23 | - | POS +$20.8M | - | 110 | 110 | +$807k | +$0 bull / -$27k bear | out (clean 35, ADX 22, RVol 1.8) |
| 11 | **NVDA** | 181.78 | - | **-** | 22 | - | NEG -$235.9M | - | 180 | 190 | +$76.7M | +$838k bull / -$40k bear | out (clean 34, ADX 18, RVol 1.2) |
| 12 | **MU** | 669.65 | - | **-** | 22 | - | NEG -$93.8M | - | 700 | 700 | +$238.5M | +$4.6M bull / +$0 bear | out (clean 32, ADX 18, RVol 1.8) |
| 13 | **AAPL** | 345.52 | - | **-** | 21 | - | POS +$512.8M | 335.28 | 350 | 330 | +$25.2M | +$0 bull / -$293k bear | out (clean 31, ADX 17, RVol 2.0) |
| 14 | **AMZN** | 259.16 | - | **-** | 20 | - | POS +$342.1M | - | 265 | 250 | +$25.3M | +$33k bull / +$0 bear | out (clean 34, ADX 13, RVol 0.8) |
| 15 | **MSTR** | 129.49 | - | **-** | 20 | - | POS +$47.5M | - | 135 | 125 | +$3.9M | +$0 bull / -$102k bear | out (clean 33, ADX 18, RVol 1.6) |
| 16 | **AMD** | 412.84 | - | **-** | 19 | - | NEG -$113.7M | - | 430 | 440 | +$36.5M | +$121k bull / +$0 bear | out (clean 32, ADX 16, RVol 0.8) |
| 17 | **CRM** | 221.60 | - | **-** | 19 | - | NEG -$18.9M | - | 240 | 220 | +$534k | - | out (clean 33, ADX 14, RVol 2.5) |
| 18 | **META** | 605.05 | - | **-** | 17 | - | NEG -$153.2M | 623.79 | 650 | 600 | +$18.6M | +$123k bull / +$0 bear | out (clean 33, ADX 10, RVol 1.1) |
| 19 | **DELL** | 319.78 | - | **-** | 16 | - | NEG -$15.1M | - | 310 | 340 | +$7.3M | - | out (clean 32, ADX 20, RVol 1.6) |
| 20 | **COIN** | 137.87 | - | **-** | 13 | - | POS +$13.8M | 134.02 | 142 | 130 | +$1.6M | - | out (clean 33, ADX 24, RVol 0.9) |
| 21 | **ARM** | 169.12 | - | **-** | 12 | - | NEG -$6.8M | - | 180 | 180 | +$1.5M | - | out (clean 26, ADX 15, RVol 1.6) |
| 22 | **HOOD** | 78.28 | - | **-** | 11 | - | NEG -$14.4M | - | 85 | 80 | +$2.1M | - | out (clean 30, ADX 20, RVol 2.0) |
| 23 | **UBER** | 68.31 | - | **-** | 11 | - | POS +$1.1M | 68.22 | 70 | 65 | +$197k | - | out (clean 29, ADX 15, RVol 1.4) |
| 24 | **GOOGL** | 283.73 | - | **-** | 10 | - | POS +$18.2M | 281.49 | 285 | 290 | +$8.8M | - | out (clean 34, ADX 16, RVol 0.8) |
| 25 | **ORCL** | 115.24 | - | **-** | 8 | - | NEG -$66.2M | - | 125 | 115 | +$2.9M | - | out (clean 31, ADX 12, RVol 0.6) |
| 26 | **SMCI** | 27.18 | - | **-** | 7 | - | NEG -$4.0M | - | 28 | 27 | +$193k | - | out (clean 34, ADX 19, RVol 1.0) |
| 27 | **SHOP** | 143.63 | - | **-** | 6 | - | NEG -$5.5M | - | 144 | 135 | -$91k | - | out (clean 37, ADX 14, RVol 0.8) |

## Big prints this scan (72)
- **QQQ** PUT 650 2026-11-06 (1DTE): 1,300 @ 6.80 = **+$884k** SELL | vol 77,218 / OI 11,913
- **IWM** CALL 270 2026-11-06 (1DTE): 1,750 @ 3.52 = **+$616k** BUY | vol 3,003 / OI 444
- **SPY** PUT 745 2026-11-05 (0DTE): 490 @ 9.50 = **+$466k** SELL | vol 176,661 / OI 4,460
- **SPY** CALL 730 2026-11-10 (5DTE): 367 @ 12.25 = **+$450k** BUY | vol 9,352 / OI 5
- **SPY** CALL 730 2026-11-10 (5DTE): 325 @ 12.25 = **+$398k** BUY | vol 9,352 / OI 5
- **QQQ** CALL 640 2026-11-06 (1DTE): 250 @ 15.55 = **+$389k** BUY | vol 1,618 / OI 76
- **SPY** PUT 745 2026-11-05 (0DTE): 400 @ 9.60 = **+$384k** SELL | vol 176,661 / OI 4,460
- **SPY** CALL 730 2026-11-10 (5DTE): 306 @ 12.25 = **+$375k** BUY | vol 9,352 / OI 5
- **SPY** PUT 755 2026-11-05 (0DTE): 150 @ 19.36 = **+$290k** SELL | vol 101,004 / OI 2,900
- **QQQ** CALL 640 2026-11-06 (1DTE): 150 @ 16.00 = **+$240k** BUY | vol 1,618 / OI 76
- **SPY** PUT 755 2026-11-05 (0DTE): 100 @ 18.71 = **+$187k** SELL | vol 101,004 / OI 2,900
- **SPY** PUT 752 2026-11-05 (0DTE): 100 @ 15.71 = **+$157k** SELL | vol 82,406 / OI 392
- **QQQ** CALL 655 2026-11-06 (1DTE): 226 @ 6.43 = **+$145k** BUY | vol 48,420 / OI 1,189
- **SPY** PUT 730 2026-11-06 (1DTE): 444 @ 3.25 = **+$144k** SELL | vol 65,302 / OI 13,922
- **SPY** PUT 745 2026-11-05 (0DTE): 150 @ 9.44 = **+$142k** SELL | vol 176,661 / OI 4,460

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 726 2026-11-11 (6DTE): 501 traded vs OI 16
- **SPY** CALL 767 2026-11-16 (11DTE): 548 traded vs OI 23
- **SPY** PUT 725 2026-11-13 (8DTE): 9,716 traded vs OI 7,187
- **QQQ** CALL 681 2026-11-20 (15DTE): 794 traded vs OI 292
- **QQQ** CALL 700 2026-11-20 (15DTE): 20,589 traded vs OI 20,277
- **SMH** PUT 430 2026-11-11 (6DTE): 502 traded vs OI 0
- **TSLA** CALL 362.5 2026-11-20 (15DTE): 511 traded vs OI 251
- **AMZN** PUT 262.5 2026-11-11 (6DTE): 520 traded vs OI 2
- **MSFT** PUT 535 2026-11-13 (8DTE): 840 traded vs OI 242
- **AVGO** CALL 300 2026-11-20 (15DTE): 500 traded vs OI 423
- **MU** CALL 732.5 2026-11-09 (4DTE): 506 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
