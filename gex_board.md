# GEX + FLOW SCAN - Thu Nov 05, 02:10 PM ET
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
Last 1m check 14:10:08 ET, last candle SPY 14:09, QQQ 14:09 | no errors
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
| 1 | **COIN** | 135.24 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 31 | none: 25 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (3 contracts' greeks worked out here) | POS +$11.9M | - | 142 | 135 | +$2.0M | - | out (clean 33, ADX 22, RVol 0.3) |
| 2 | **SPY** | 735.68 | - | **-** | 30 | - | NEG -$13.0B | 768.94 | 760 | 740 | +$1.2B | +$1.7M bull / -$982k bear | out (clean 36, ADX 48, RVol 1.2) |
| 3 | **SMH** | 455.74 | - | **-** | 29 | - | NEG -$239.5M | - | 445 | 465 | +$41.5M | +$0 bull / -$40k bear | out (clean 35, ADX 31, RVol 0.6) |
| 4 | **NFLX** | 65.03 | PINNED between the walls (positive gamma) - chop | **-** | 27 | - | POS +$30.4M | 62.16 | 65 | 65 | +$1.1M | - | out (clean 32, ADX 27, RVol 0.5) |
| 5 | **PLTR** | 154.59 | - | **-** | 27 | - | NEG -$43.6M | - | 165 | 150 | +$13.3M | +$0 bull / -$45k bear | out (clean 27, ADX 26, RVol 0.5) |
| 6 | **QQQ** | 652.02 | - | **-** | 26 | - | NEG -$4.5B | - | 700 | 680 | +$833.0M | +$1.5M bull / -$4.0M bear | out (clean 36, ADX 35, RVol 1.3) |
| 7 | **IWM** | 271.34 | - | **-** | 26 | - | NEG -$2.8B | 287.35 | 285 | 270 | +$55.8M | +$67k bull / +$0 bear | out (clean 37, ADX 43, RVol 0.5) |
| 8 | **NVDA** | 182.84 | - | **-** | 26 | - | NEG -$237.6M | - | 200 | 190 | +$75.3M | +$854k bull / -$109k bear | out (clean 34, ADX 38, RVol 1.1) |
| 9 | **DELL** | 323.13 | - | **-** | 26 | - | NEG -$12.2M | - | 350 | 340 | +$6.3M | +$41k bull / +$0 bear | out (clean 34, ADX 27, RVol 1.1) |
| 10 | **MSFT** | 537.84 | - | **-** | 25 | - | POS +$798.2M | - | 540 | 500 | +$21.0M | +$65k bull / -$267k bear | out (clean 32, ADX 29, RVol 0.6) |
| 11 | **TSLA** | 341.24 | - | **-** | 24 | - | NEG -$131.0M | - | 350 | 350 | +$110.2M | +$132k bull / -$583k bear | out (clean 35, ADX 33, RVol 0.9) |
| 12 | **MU** | 674.82 | - | **-** | 24 | - | NEG -$61.9M | - | 700 | 700 | +$239.5M | +$3.7M bull / -$8.3M bear | out (clean 33, ADX 30, RVol 1.3) |
| 13 | **AAPL** | 343.57 | - | **-** | 22 | - | POS +$408.3M | 334.51 | 350 | 330 | +$24.6M | +$289k bull / -$274k bear | out (clean 31, ADX 30, RVol 0.7) |
| 14 | **HOOD** | 77.08 | - | **-** | 22 | - | NEG -$7.8M | - | 83 | 80 | +$2.4M | +$0 bull / -$35k bear | out (clean 31, ADX 34, RVol 1.1) |
| 15 | **AMD** | 414.03 | - | **-** | 21 | - | NEG -$95.2M | - | 430 | 440 | +$35.7M | +$185k bull / -$627k bear | out (clean 33, ADX 28, RVol 0.5) |
| 16 | **AMZN** | 259.09 | - | **-** | 21 | - | POS +$373.7M | - | 265 | 250 | +$23.5M | +$274k bull / -$177k bear | out (clean 35, ADX 19, RVol 0.5) |
| 17 | **GOOGL** | 283.46 | - | **-** | 20 | - | POS +$17.8M | 281.22 | 285 | 290 | +$8.6M | +$164k bull / -$29k bear | out (clean 35, ADX 17, RVol 0.5) |
| 18 | **CRM** | 220.99 | - | **-** | 19 | - | NEG -$16.4M | - | 240 | 220 | +$559k | - | out (clean 34, ADX 20, RVol 1.4) |
| 19 | **MSTR** | 127.89 | - | **-** | 18 | - | POS +$41.1M | - | 135 | 125 | +$3.8M | +$32k bull / +$0 bear | out (clean 34, ADX 18, RVol 0.4) |
| 20 | **META** | 603.39 | - | **-** | 16 | - | NEG -$122.3M | 621.11 | 650 | 600 | +$18.4M | +$0 bull / -$78k bear | out (clean 33, ADX 14, RVol 0.3) |
| 21 | **AVGO** | 297.43 | - | **-** | 16 | - | NEG -$104.0M | - | 325 | 300 | +$8.8M | - | out (clean 32, ADX 28, RVol 0.9) |
| 22 | **BABA** | 106.48 | - | **-** | 15 | - | POS +$21.1M | - | 110 | 110 | +$1.3M | - | out (clean 36, ADX 10, RVol 0.8) |
| 23 | **ARM** | 169.02 | - | **-** | 11 | - | NEG -$7.0M | - | 180 | 180 | +$1.4M | - | out (clean 27, ADX 18, RVol 0.5) |
| 24 | **SMCI** | 26.74 | - | **-** | 10 | - | NEG -$2.9M | - | 28 | 27 | +$410k | - | out (clean 35, ADX 15, RVol 0.6) |
| 25 | **ORCL** | 114.57 | - | **-** | 10 | - | NEG -$57.9M | - | 125 | 115 | +$3.0M | - | out (clean 31, ADX 22, RVol 0.6) |
| 26 | **UBER** | 68.24 | - | **-** | 9 | - | POS +$2.3M | 67.86 | 70 | 65 | +$195k | - | out (clean 31, ADX 8, RVol 0.4) |
| 27 | **SHOP** | 144.50 | - | **-** | 7 | - | NEG -$4.4M | - | 144 | 135 | -$129k | - | out (clean 37, ADX 15, RVol 0.5) |

## Big prints this scan (111)
- **QQQ** CALL 663 2026-11-09 (4DTE): 1,000 @ 6.00 = **+$600k** SELL | vol 23,397 / OI 0
- **MU** PUT 685 2026-11-11 (6DTE): 54 @ 45.65 = **+$247k** BUY | vol 966 / OI 0
- **MU** PUT 685 2026-11-11 (6DTE): 54 @ 45.45 = **+$245k** BUY | vol 966 / OI 0
- **MU** PUT 685 2026-11-11 (6DTE): 53 @ 45.65 = **+$242k** BUY | vol 966 / OI 0
- **MU** PUT 685 2026-11-11 (6DTE): 53 @ 45.50 = **+$241k** BUY | vol 966 / OI 0
- **SPY** CALL 735 2026-11-06 (1DTE): 380 @ 6.04 = **+$230k** BUY | vol 6,665 / OI 399
- **QQQ** PUT 655 2026-11-05 (0DTE): 390 @ 5.30 = **+$207k** BUY | vol 146,376 / OI 1,387
- **SPY** PUT 753 2026-11-05 (0DTE): 100 @ 17.39 = **+$174k** MID | vol 77,491 / OI 748
- **AMD** PUT 420 2026-11-06 (1DTE): 100 @ 16.60 = **+$166k** BUY | vol 6,372 / OI 2,350
- **QQQ** PUT 665 2026-11-05 (0DTE): 109 @ 14.11 = **+$154k** BUY | vol 63,538 / OI 2,574
- **SPY** PUT 750 2026-11-06 (1DTE): 100 @ 15.00 = **+$150k** MID | vol 43,679 / OI 42,367
- **MU** CALL 670 2026-11-06 (1DTE): 50 @ 23.85 = **+$119k** SELL | vol 5,944 / OI 0
- **QQQ** PUT 650 2026-11-06 (1DTE): 150 @ 7.70 = **+$116k** BUY | vol 58,344 / OI 11,913
- **QQQ** PUT 655 2026-11-05 (0DTE): 200 @ 5.65 = **+$113k** BUY | vol 146,376 / OI 1,387
- **SPY** CALL 736 2026-11-06 (1DTE): 200 @ 5.51 = **+$110k** BUY | vol 6,159 / OI 39

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 769 2026-11-10 (5DTE): 500 traded vs OI 165
- **SPY** CALL 735 2026-11-12 (7DTE): 505 traded vs OI 8
- **SPY** PUT 726 2026-11-16 (11DTE): 548 traded vs OI 80
- **SPY** PUT 727 2026-11-11 (6DTE): 538 traded vs OI 56
- **SPY** CALL 741 2026-11-18 (13DTE): 544 traded vs OI 0
- **SPY** CALL 767 2026-12-04 (29DTE): 512 traded vs OI 188
- **SPY** PUT 680 2026-12-04 (29DTE): 500 traded vs OI 0
- **SPY** CALL 773 2026-11-27 (22DTE): 961 traded vs OI 952
- **QQQ** CALL 656 2026-11-10 (5DTE): 506 traded vs OI 0
- **QQQ** CALL 670 2026-11-16 (11DTE): 521 traded vs OI 2
- **QQQ** PUT 635 2026-12-04 (29DTE): 827 traded vs OI 826
- **IWM** CALL 280 2026-11-06 (1DTE): 8,762 traded vs OI 8,757
- **IWM** CALL 271 2026-11-09 (4DTE): 533 traded vs OI 45
- **SMH** PUT 485 2026-11-20 (15DTE): 1,212 traded vs OI 1,124
- **AMZN** PUT 257.5 2026-11-13 (8DTE): 535 traded vs OI 47

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
