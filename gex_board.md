# GEX + FLOW SCAN - Thu Nov 05, 02:20 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (4)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:55 | **BABA** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/06 102P | 0.75 | 0.33 | -5% (9m) | **-56%** (done) | +27% | 103.58 |
| 09:52 | **SPY** | **PUTS** | 1m WHIPSAW (R1) | 11/05 749P | 0.78 | 11.35 | +1355% (60m) | **+1355%** (done) | +47% | 753.11 hit |
| 09:50 | **BABA** | **CALLS** | TREND + FLOW | 11/06 111C | 0.48 | 0.20 | -12% (0m) | **-58%** (done) | +136% | 110 |
| 09:40 | **QQQ** | **CALLS** | 1m WHIPSAW (R1) | 11/05 683C | 0.78 | 0.10 | -4% (0m) | **-87%** (done) | +66% | 678.43 |

## 1m RULES on SPY / QQQ - loose (5 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 14:20:08 ET, last candle SPY 14:19, QQQ 14:19 | no errors
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
| 1 | **SPY** | 737.26 | - | **-** | 29 | - | NEG -$13.2B | 769.47 | 760 | 740 | +$1.2B | +$457k bull / -$2.1M bear | out (clean 36, ADX 43, RVol 1.3) |
| 2 | **SMH** | 457.62 | - | **-** | 28 | - | NEG -$253.6M | - | 500 | 465 | +$39.5M | +$0 bull / -$593k bear | out (clean 35, ADX 27, RVol 0.7) |
| 3 | **QQQ** | 653.94 | - | **-** | 27 | - | NEG -$4.6B | - | 700 | 680 | +$810.4M | +$108k bull / -$3.3M bear | out (clean 36, ADX 31, RVol 2.1) |
| 4 | **PLTR** | 155.21 | - | **-** | 27 | - | NEG -$46.7M | - | 165 | 150 | +$13.3M | +$0 bull / -$54k bear | out (clean 27, ADX 24, RVol 0.7) |
| 5 | **NFLX** | 65.10 | PINNED between the walls (positive gamma) - chop | **-** | 26 | - | POS +$30.4M | 62.23 | 65 | 65 | +$1.0M | - | out (clean 32, ADX 27, RVol 0.5) |
| 6 | **DELL** | 324.39 | - | **-** | 26 | - | NEG -$12.7M | - | 350 | 340 | +$6.1M | +$41k bull / -$47k bear | out (clean 33, ADX 24, RVol 1.6) |
| 7 | **IWM** | 272.01 | - | **-** | 25 | - | NEG -$2.7B | 286.37 | 285 | 270 | +$54.1M | +$0 bull / -$79k bear | out (clean 37, ADX 38, RVol 0.7) |
| 8 | **NVDA** | 183.57 | - | **-** | 25 | - | NEG -$246.5M | - | 200 | 190 | +$67.7M | +$107k bull / -$1.6M bear | out (clean 34, ADX 34, RVol 1.2) |
| 9 | **MSFT** | 537.38 | - | **-** | 24 | - | POS +$800.9M | - | 540 | 500 | +$20.9M | +$32k bull / +$0 bear | out (clean 32, ADX 26, RVol 0.5) |
| 10 | **TSLA** | 343.65 | - | **-** | 23 | - | NEG -$135.7M | - | 350 | 350 | +$105.6M | +$0 bull / -$397k bear | out (clean 35, ADX 30, RVol 1.1) |
| 11 | **MU** | 678.57 | - | **-** | 23 | - | NEG -$66.7M | - | 700 | 700 | +$233.0M | +$306k bull / -$7.1M bear | out (clean 33, ADX 27, RVol 1.3) |
| 12 | **AAPL** | 343.92 | - | **-** | 21 | - | POS +$439.2M | 334.8 | 350 | 330 | +$23.8M | +$82k bull / -$305k bear | out (clean 31, ADX 27, RVol 0.8) |
| 13 | **AMZN** | 259.95 | - | **-** | 21 | - | POS +$392.4M | - | 265 | 250 | +$22.9M | +$244k bull / -$61k bear | out (clean 35, ADX 18, RVol 0.6) |
| 14 | **AMD** | 416.92 | - | **-** | 20 | - | NEG -$97.8M | - | 430 | 440 | +$33.8M | +$0 bull / -$981k bear | out (clean 33, ADX 25, RVol 0.6) |
| 15 | **GOOGL** | 283.34 | - | **-** | 20 | - | POS +$18.8M | 281.15 | 285 | 290 | +$8.4M | +$0 bull / -$58k bear | out (clean 34, ADX 15, RVol 0.7) |
| 16 | **MSTR** | 129.18 | - | **-** | 18 | - | POS +$58.3M | - | 135 | 125 | +$3.8M | +$0 bull / -$31k bear | out (clean 33, ADX 16, RVol 0.4) |
| 17 | **CRM** | 221.02 | - | **-** | 18 | - | NEG -$16.6M | - | 240 | 220 | +$559k | - | out (clean 34, ADX 20, RVol 1.0) |
| 18 | **META** | 603.84 | - | **-** | 16 | - | NEG -$122.4M | 620.48 | 650 | 600 | +$17.6M | +$0 bull / -$101k bear | out (clean 33, ADX 12, RVol 0.3) |
| 19 | **BABA** | 106.87 | - | **-** | 16 | - | POS +$21.2M | - | 110 | 110 | +$1.3M | - | out (clean 36, ADX 10, RVol 1.1) |
| 20 | **AVGO** | 297.76 | - | **-** | 15 | - | NEG -$105.6M | - | 325 | 300 | +$8.7M | - | out (clean 32, ADX 25, RVol 1.0) |
| 21 | **COIN** | 136.58 | - | **-** | 14 | - | POS +$17.4M | - | 142 | 135 | +$1.9M | - | out (clean 33, ADX 21, RVol 0.5) |
| 22 | **HOOD** | 77.88 | - | **-** | 11 | - | NEG -$9.3M | - | 85 | 80 | +$2.2M | - | out (clean 31, ADX 30, RVol 0.9) |
| 23 | **ARM** | 169.71 | - | **-** | 11 | - | NEG -$7.1M | - | 180 | 180 | +$1.4M | - | out (clean 27, ADX 16, RVol 0.6) |
| 24 | **SMCI** | 27.20 | - | **-** | 10 | - | NEG -$3.1M | - | 28 | 27 | +$362k | - | out (clean 35, ADX 16, RVol 0.9) |
| 25 | **ORCL** | 115.09 | - | **-** | 10 | - | NEG -$57.2M | - | 125 | 115 | +$2.9M | - | out (clean 31, ADX 20, RVol 0.5) |
| 26 | **UBER** | 68.55 | - | **-** | 9 | - | POS +$3.5M | 68 | 70 | 65 | +$194k | - | out (clean 31, ADX 9, RVol 0.5) |
| 27 | **SHOP** | 144.63 | - | **-** | 7 | - | NEG -$4.8M | - | 144 | 135 | -$130k | - | out (clean 37, ADX 15, RVol 0.5) |

## Big prints this scan (67)
- **NVDA** PUT 187.5 2026-11-11 (6DTE): 500 @ 9.22 = **+$461k** BUY | vol 5,607 / OI 357
- **NVDA** PUT 185 2026-11-11 (6DTE): 500 @ 7.82 = **+$391k** BUY | vol 4,762 / OI 1,242
- **QQQ** PUT 640 2026-11-09 (4DTE): 617 @ 6.00 = **+$370k** BUY | vol 15,166 / OI 5,186
- **SPY** CALL 735 2026-11-06 (1DTE): 400 @ 5.95 = **+$238k** SELL | vol 8,181 / OI 399
- **QQQ** PUT 640 2026-11-09 (4DTE): 383 @ 6.00 = **+$230k** BUY | vol 15,166 / OI 5,186
- **MU** PUT 700 2026-11-09 (4DTE): 50 @ 44.95 = **+$225k** BUY | vol 4,096 / OI 0
- **SPY** PUT 753 2026-11-05 (0DTE): 130 @ 17.10 = **+$222k** BUY | vol 77,700 / OI 748
- **QQQ** PUT 655 2026-11-05 (0DTE): 400 @ 5.00 = **+$200k** BUY | vol 148,649 / OI 1,387
- **QQQ** PUT 685 2026-11-05 (0DTE): 50 @ 34.00 = **+$170k** BUY | vol 8,993 / OI 2,551
- **MU** PUT 660 2026-11-06 (1DTE): 100 @ 15.80 = **+$158k** BUY | vol 21,261 / OI 0
- **MU** PUT 660 2026-11-06 (1DTE): 86 @ 16.20 = **+$139k** BUY | vol 21,261 / OI 0
- **SPY** PUT 737 2026-11-06 (1DTE): 200 @ 6.15 = **+$123k** BUY | vol 19,897 / OI 1,597
- **SPY** CALL 740 2026-11-12 (7DTE): 137 @ 8.56 = **+$117k** BUY | vol 1,299 / OI 12
- **SPY** PUT 744 2026-11-09 (4DTE): 100 @ 11.26 = **+$113k** BUY | vol 3,751 / OI 73
- **QQQ** PUT 655 2026-11-05 (0DTE): 200 @ 5.26 = **+$105k** BUY | vol 148,649 / OI 1,387

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 733 2026-11-09 (4DTE): 506 traded vs OI 16
- **SPY** PUT 726 2026-11-10 (5DTE): 501 traded vs OI 43
- **SPY** CALL 774 2026-11-11 (6DTE): 613 traded vs OI 15
- **SPY** CALL 737 2026-11-16 (11DTE): 500 traded vs OI 0
- **SPY** CALL 736 2026-11-13 (8DTE): 662 traded vs OI 18
- **SPY** CALL 780 2026-11-20 (15DTE): 22,846 traded vs OI 22,767
- **SPY** PUT 729 2026-11-20 (15DTE): 11,551 traded vs OI 11,159
- **SPY** PUT 665 2026-11-30 (25DTE): 505 traded vs OI 0
- **QQQ** CALL 660 2026-11-11 (6DTE): 500 traded vs OI 9
- **IWM** PUT 274 2026-11-20 (15DTE): 2,544 traded vs OI 2,529
- **AAPL** CALL 355 2026-11-13 (8DTE): 2,320 traded vs OI 2,317
- **MSFT** CALL 550 2026-11-11 (6DTE): 500 traded vs OI 202
- **AVGO** PUT 280 2026-11-18 (13DTE): 504 traded vs OI 0
- **AVGO** PUT 285 2026-11-18 (13DTE): 501 traded vs OI 0
- **PLTR** CALL 155 2026-11-13 (8DTE): 604 traded vs OI 72

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
