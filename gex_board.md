# GEX + FLOW SCAN - Thu Nov 05, 02:30 PM ET
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
Last 1m check 14:30:08 ET, last candle SPY 14:29, QQQ 14:29 | no errors
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
| 1 | **SPY** | 735.49 | - | **-** | 29 | - | NEG -$13.1B | 769.17 | 760 | 740 | +$1.2B | +$9.6M bull / -$9.9M bear | out (clean 36, ADX 40, RVol 1.4) |
| 2 | **NFLX** | 65.00 | PINNED between the walls (positive gamma) - chop | **-** | 28 | - | POS +$31.2M | 62.2 | 65 | 65 | +$1.0M | - | out (clean 32, ADX 28, RVol 0.8) |
| 3 | **SMH** | 454.99 | - | **-** | 27 | - | NEG -$266.0M | - | 445 | 500 | +$39.9M | +$220k bull / -$795k bear | out (clean 34, ADX 24, RVol 0.9) |
| 4 | **PLTR** | 154.67 | - | **-** | 27 | - | NEG -$46.1M | - | 165 | 150 | +$13.4M | +$0 bull / -$54k bear | out (clean 27, ADX 22, RVol 0.8) |
| 5 | **DELL** | 323.22 | - | **-** | 27 | - | NEG -$12.4M | - | 350 | 340 | +$6.5M | +$0 bull / -$395k bear | out (clean 33, ADX 22, RVol 1.8) |
| 6 | **QQQ** | 651.83 | - | **-** | 26 | - | NEG -$4.4B | - | 700 | 680 | +$834.1M | +$1.4M bull / -$3.6M bear | out (clean 35, ADX 28, RVol 1.9) |
| 7 | **IWM** | 271.13 | - | **-** | 25 | - | NEG -$2.8B | 287.26 | 285 | 270 | +$55.5M | +$0 bull / -$151k bear | out (clean 36, ADX 36, RVol 0.9) |
| 8 | **NVDA** | 182.66 | - | **-** | 24 | - | NEG -$241.9M | - | 200 | 190 | +$69.6M | +$1.1M bull / -$2.0M bear | out (clean 34, ADX 30, RVol 0.9) |
| 9 | **COIN** | 136.38 | - | **-** | 23 | - | POS +$15.8M | - | 142 | 135 | +$1.8M | +$0 bull / -$32k bear | out (clean 33, ADX 20, RVol 0.4) |
| 10 | **MU** | 675.34 | - | **-** | 23 | - | NEG -$63.0M | - | 700 | 700 | +$234.8M | +$1.7M bull / -$5.7M bear | out (clean 33, ADX 24, RVol 1.3) |
| 11 | **TSLA** | 341.30 | - | **-** | 22 | - | NEG -$132.0M | - | 350 | 350 | +$108.1M | +$1.1M bull / -$380k bear | out (clean 35, ADX 27, RVol 0.9) |
| 12 | **AAPL** | 343.81 | - | **-** | 21 | - | POS +$438.7M | 334.53 | 350 | 330 | +$25.5M | +$200k bull / -$664k bear | out (clean 31, ADX 25, RVol 0.9) |
| 13 | **AMZN** | 259.11 | - | **-** | 21 | - | POS +$374.2M | - | 265 | 250 | +$23.1M | +$122k bull / -$161k bear | out (clean 34, ADX 19, RVol 0.6) |
| 14 | **AMD** | 414.02 | - | **-** | 20 | - | NEG -$94.9M | - | 430 | 440 | +$35.1M | +$139k bull / -$730k bear | out (clean 33, ADX 22, RVol 0.6) |
| 15 | **GOOGL** | 283.19 | - | **-** | 20 | - | POS +$21.9M | 280.75 | 285 | 290 | +$8.5M | +$40k bull / -$30k bear | out (clean 34, ADX 14, RVol 0.7) |
| 16 | **MSTR** | 128.00 | - | **-** | 18 | - | POS +$43.0M | - | 135 | 125 | +$4.0M | +$0 bull / -$73k bear | out (clean 33, ADX 14, RVol 0.5) |
| 17 | **CRM** | 220.75 | - | **-** | 18 | - | NEG -$16.3M | - | 240 | 220 | +$560k | - | out (clean 34, ADX 21, RVol 0.8) |
| 18 | **BABA** | 106.82 | - | **-** | 17 | - | POS +$21.9M | - | 110 | 110 | +$1.3M | - | out (clean 36, ADX 9, RVol 1.6) |
| 19 | **META** | 601.99 | - | **-** | 16 | - | NEG -$130.8M | 622.19 | 650 | 600 | +$18.3M | +$362k bull / -$65k bear | out (clean 33, ADX 12, RVol 0.4) |
| 20 | **AVGO** | 296.24 | - | **-** | 15 | - | NEG -$105.2M | - | 325 | 300 | +$8.9M | - | out (clean 32, ADX 25, RVol 1.0) |
| 21 | **MSFT** | 537.04 | - | **-** | 14 | - | POS +$802.6M | - | 540 | 500 | +$21.1M | - | out (clean 32, ADX 25, RVol 0.5) |
| 22 | **ARM** | 168.37 | - | **-** | 11 | - | NEG -$7.0M | - | 180 | 180 | +$1.5M | - | out (clean 27, ADX 16, RVol 0.7) |
| 23 | **SMCI** | 27.00 | - | **-** | 10 | - | NEG -$3.1M | - | 28 | 27 | +$361k | - | out (clean 35, ADX 17, RVol 1.0) |
| 24 | **ORCL** | 114.13 | - | **-** | 10 | - | NEG -$57.5M | - | 125 | 115 | +$2.9M | - | out (clean 31, ADX 19, RVol 0.6) |
| 25 | **HOOD** | 77.69 | - | **-** | 10 | - | NEG -$9.1M | - | 85 | 80 | +$2.3M | - | out (clean 31, ADX 27, RVol 0.7) |
| 26 | **UBER** | 68.36 | - | **-** | 9 | - | POS +$3.1M | 67.9 | 70 | 65 | +$191k | - | out (clean 31, ADX 9, RVol 0.6) |
| 27 | **SHOP** | 143.94 | - | **-** | 7 | - | NEG -$4.8M | - | 144 | 135 | -$130k | - | out (clean 37, ADX 14, RVol 0.4) |

## Big prints this scan (150)
- **SPY** CALL 740 2026-11-10 (5DTE): 2,654 @ 6.60 = **+$1.8M** BUY | vol 27,276 / OI 44
- **SPY** CALL 730 2026-11-10 (5DTE): 400 @ 12.76 = **+$510k** BUY | vol 5,316 / OI 5
- **SPY** CALL 730 2026-11-10 (5DTE): 400 @ 12.76 = **+$510k** BUY | vol 5,316 / OI 5
- **SPY** CALL 730 2026-11-10 (5DTE): 400 @ 12.76 = **+$510k** BUY | vol 5,316 / OI 5
- **SPY** CALL 730 2026-11-10 (5DTE): 400 @ 12.76 = **+$510k** BUY | vol 5,316 / OI 5
- **SPY** CALL 730 2026-11-10 (5DTE): 400 @ 12.76 = **+$510k** BUY | vol 5,316 / OI 5
- **QQQ** CALL 663 2026-11-09 (4DTE): 500 @ 6.29 = **+$314k** BUY | vol 26,317 / OI 0
- **SPY** CALL 740 2026-11-10 (5DTE): 433 @ 6.60 = **+$286k** BUY | vol 27,276 / OI 44
- **NVDA** PUT 185 2026-11-06 (1DTE): 500 @ 4.45 = **+$222k** SELL | vol 80,726 / OI 9,821
- **TSLA** CALL 335 2026-11-06 (1DTE): 190 @ 11.68 = **+$222k** BUY | vol 2,691 / OI 132
- **SPY** PUT 735 2026-11-06 (1DTE): 500 @ 4.39 = **+$220k** SELL | vol 61,321 / OI 24,589
- **SPY** CALL 740 2026-11-10 (5DTE): 327 @ 6.60 = **+$216k** BUY | vol 27,276 / OI 44
- **MU** CALL 680 2026-11-09 (4DTE): 73 @ 29.25 = **+$214k** BUY | vol 1,898 / OI 0
- **QQQ** CALL 650 2026-11-05 (0DTE): 487 @ 4.26 = **+$207k** BUY | vol 50,159 / OI 2
- **NVDA** PUT 175 2026-11-11 (6DTE): 500 @ 3.60 = **+$180k** SELL | vol 2,920 / OI 28

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 719 2026-11-10 (5DTE): 519 traded vs OI 78
- **SPY** CALL 780 2026-11-13 (8DTE): 8,563 traded vs OI 8,540
- **SPY** CALL 751 2026-11-16 (11DTE): 500 traded vs OI 67
- **SPY** PUT 670 2026-11-16 (11DTE): 734 traded vs OI 0
- **SPY** CALL 785 2026-12-04 (29DTE): 1,032 traded vs OI 851
- **SPY** CALL 750 2026-11-20 (15DTE): 12,627 traded vs OI 12,482
- **SPY** CALL 775 2026-11-19 (14DTE): 503 traded vs OI 0
- **SPY** PUT 726 2026-11-18 (13DTE): 604 traded vs OI 0
- **QQQ** CALL 650 2026-11-12 (7DTE): 501 traded vs OI 23
- **QQQ** CALL 653 2026-11-13 (8DTE): 504 traded vs OI 0
- **QQQ** CALL 630 2026-11-05 (0DTE): 500 traded vs OI 0
- **QQQ** CALL 695 2026-11-16 (11DTE): 571 traded vs OI 212
- **QQQ** CALL 682 2026-11-20 (15DTE): 683 traded vs OI 173
- **QQQ** CALL 695 2026-11-13 (8DTE): 2,777 traded vs OI 2,737
- **QQQ** PUT 620 2026-11-13 (8DTE): 2,386 traded vs OI 2,371

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
