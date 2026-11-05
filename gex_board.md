# GEX + FLOW SCAN - Thu Nov 05, 01:40 PM ET
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
Last 1m check 13:40:08 ET, last candle SPY 13:39, QQQ 13:39 | no errors
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
| 1 | **SMH** | 454.79 | FLOW SURGE | **CALLS** | 40 | none: 89 calls 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (6 contracts' greeks worked out here) | NEG -$266.3M | - | 445 | 500 | +$41.4M | +$479k bull / -$451k bear | out (clean 35, ADX 36, RVol 0.5) |
| 2 | **MU** | 674.50 | TREND (flow not with it) | **PUTS** | 35 | none: 79 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (13 contracts' greeks worked out here) | NEG -$61.6M | - | 700 | 700 | +$229.2M | +$7.5M bull / -$2.7M bear | SHORT (clean 34, ADX 31, RVol 1.5) |
| 3 | **SPY** | 736.44 | - | **-** | 30 | - | NEG -$13.1B | 769.4 | 760 | 740 | +$1.2B | +$4.1M bull / -$3.5M bear | out (clean 37, ADX 52, RVol 1.4) |
| 4 | **PLTR** | 154.89 | - | **-** | 28 | - | NEG -$45.6M | - | 165 | 150 | +$13.3M | +$34k bull / -$132k bear | out (clean 28, ADX 28, RVol 0.6) |
| 5 | **IWM** | 271.74 | - | **-** | 27 | - | NEG -$2.8B | 287.42 | 285 | 270 | +$52.8M | +$82k bull / -$2.5M bear | out (clean 37, ADX 47, RVol 1.2) |
| 6 | **NVDA** | 183.02 | - | **-** | 27 | - | NEG -$235.2M | - | 200 | 190 | +$71.3M | +$501k bull / -$2.2M bear | out (clean 34, ADX 44, RVol 1.1) |
| 7 | **MSFT** | 538.12 | - | **-** | 27 | - | POS +$811.1M | - | 540 | 500 | +$21.7M | +$230k bull / -$157k bear | out (clean 33, ADX 35, RVol 0.9) |
| 8 | **QQQ** | 651.75 | - | **-** | 26 | - | NEG -$4.4B | - | 700 | 680 | +$818.5M | +$5.4M bull / -$4.4M bear | out (clean 36, ADX 41, RVol 0.7) |
| 9 | **AVGO** | 297.48 | - | **-** | 26 | - | NEG -$103.6M | - | 325 | 300 | +$8.8M | +$0 bull / -$32k bear | out (clean 32, ADX 30, RVol 0.7) |
| 10 | **TSLA** | 340.25 | - | **-** | 25 | - | NEG -$128.1M | - | 350 | 350 | +$109.3M | +$1.2M bull / -$1.0M bear | out (clean 35, ADX 38, RVol 1.2) |
| 11 | **HOOD** | 77.10 | - | **-** | 23 | - | NEG -$7.7M | - | 83 | 80 | +$2.1M | +$28k bull / -$93k bear | out (clean 32, ADX 36, RVol 1.0) |
| 12 | **AAPL** | 343.49 | - | **-** | 22 | - | POS +$402.9M | 334.39 | 350 | 330 | +$24.7M | +$1.1M bull / -$100k bear | out (clean 31, ADX 34, RVol 0.7) |
| 13 | **AMD** | 413.41 | - | **-** | 22 | - | NEG -$92.0M | - | 430 | 440 | +$34.2M | +$0 bull / -$1.5M bear | out (clean 34, ADX 34, RVol 0.5) |
| 14 | **AMZN** | 259.25 | - | **-** | 21 | - | POS +$375.2M | - | 265 | 250 | +$23.4M | +$166k bull / -$41k bear | out (clean 35, ADX 16, RVol 0.6) |
| 15 | **GOOGL** | 283.77 | - | **-** | 20 | - | POS +$20.7M | 281.24 | 285 | 290 | +$8.5M | +$177k bull / -$113k bear | out (clean 35, ADX 17, RVol 0.4) |
| 16 | **MSTR** | 128.50 | - | **-** | 19 | - | POS +$50.0M | - | 135 | 125 | +$3.5M | +$38k bull / -$39k bear | out (clean 34, ADX 24, RVol 0.5) |
| 17 | **CRM** | 221.47 | - | **-** | 18 | - | NEG -$16.5M | - | 240 | 220 | +$555k | - | out (clean 34, ADX 22, RVol 0.7) |
| 18 | **META** | 604.72 | - | **-** | 16 | - | NEG -$112.7M | 622.29 | 650 | 600 | +$18.0M | +$466k bull / -$1.2M bear | out (clean 34, ADX 15, RVol 0.3) |
| 19 | **COIN** | 135.53 | - | **-** | 16 | - | POS +$15.7M | - | 142 | 135 | +$1.9M | - | out (clean 33, ADX 30, RVol 0.4) |
| 20 | **BABA** | 106.98 | - | **-** | 16 | - | POS +$20.3M | - | 110 | 110 | +$1.3M | - | out (clean 36, ADX 11, RVol 0.9) |
| 21 | **NFLX** | 65.42 | - | **-** | 15 | - | POS +$30.0M | 62.19 | 65 | 65 | +$968k | - | out (clean 32, ADX 28, RVol 0.6) |
| 22 | **DELL** | 323.40 | - | **-** | 15 | - | NEG -$12.5M | - | 350 | 340 | +$6.2M | - | out (clean 34, ADX 28, RVol 0.5) |
| 23 | **SMCI** | 26.74 | - | **-** | 12 | - | NEG -$2.9M | - | 28 | 27 | +$412k | - | out (clean 36, ADX 21, RVol 1.0) |
| 24 | **ARM** | 169.11 | - | **-** | 12 | - | NEG -$6.9M | - | 180 | 180 | +$1.4M | - | out (clean 27, ADX 21, RVol 0.7) |
| 25 | **ORCL** | 114.34 | - | **-** | 11 | - | NEG -$55.4M | - | 125 | 115 | +$2.8M | - | out (clean 32, ADX 24, RVol 0.7) |
| 26 | **UBER** | 68.51 | - | **-** | 8 | - | POS +$2.5M | 68.05 | 70 | 65 | +$187k | - | out (clean 32, ADX 8, RVol 0.4) |
| 27 | **SHOP** | 144.10 | - | **-** | 7 | - | NEG -$5.1M | - | 144 | 135 | -$132k | - | out (clean 38, ADX 17, RVol 0.3) |

## Big prints this scan (75)
- **QQQ** PUT 655 2026-11-06 (1DTE): 476 @ 10.55 = **+$502k** BUY | vol 28,653 / OI 5,889
- **SMH** CALL 465 2026-11-09 (4DTE): 239 @ 8.45 = **+$202k** BUY | vol 1,422 / OI 0
- **QQQ** PUT 655 2026-11-06 (1DTE): 178 @ 10.55 = **+$188k** BUY | vol 28,653 / OI 5,889
- **SMH** CALL 465 2026-11-09 (4DTE): 222 @ 8.40 = **+$186k** BUY | vol 1,422 / OI 0
- **QQQ** CALL 650 2026-11-06 (1DTE): 193 @ 9.14 = **+$176k** SELL | vol 7,199 / OI 889
- **META** PUT 600 2026-11-06 (1DTE): 180 @ 9.50 = **+$171k** BUY | vol 12,246 / OI 3,434
- **SPY** CALL 740 2026-11-06 (1DTE): 399 @ 3.82 = **+$152k** SELL | vol 18,842 / OI 358
- **SMH** PUT 460 2026-11-06 (1DTE): 100 @ 13.09 = **+$131k** BUY | vol 4,547 / OI 2,930
- **TSLA** CALL 335 2026-11-06 (1DTE): 120 @ 10.85 = **+$130k** BUY | vol 2,312 / OI 132
- **SMH** PUT 460 2026-11-06 (1DTE): 100 @ 12.78 = **+$128k** BUY | vol 4,547 / OI 2,930
- **SMH** PUT 460 2026-11-06 (1DTE): 100 @ 12.78 = **+$128k** BUY | vol 4,547 / OI 2,930
- **SPY** PUT 735 2026-11-05 (0DTE): 430 @ 2.87 = **+$123k** BUY | vol 279,318 / OI 15,976
- **MU** PUT 660 2026-11-06 (1DTE): 79 @ 15.00 = **+$118k** SELL | vol 18,386 / OI 0
- **QQQ** PUT 655 2026-11-06 (1DTE): 112 @ 10.55 = **+$118k** BUY | vol 28,653 / OI 5,889
- **QQQ** PUT 655 2026-11-05 (0DTE): 191 @ 5.98 = **+$114k** BUY | vol 138,920 / OI 1,387

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 746 2026-11-16 (11DTE): 500 traded vs OI 4
- **SPY** PUT 725 2026-11-16 (11DTE): 514 traded vs OI 180
- **SPY** CALL 755 2026-11-20 (15DTE): 6,469 traded vs OI 5,682
- **SPY** PUT 710 2026-12-04 (29DTE): 1,115 traded vs OI 1,032
- **QQQ** PUT 590 2026-11-09 (4DTE): 595 traded vs OI 0
- **QQQ** CALL 697 2026-11-09 (4DTE): 519 traded vs OI 42
- **QQQ** PUT 655 2026-11-10 (5DTE): 655 traded vs OI 620
- **MSFT** PUT 525 2026-11-13 (8DTE): 598 traded vs OI 396
- **SMCI** PUT 25 2026-11-13 (8DTE): 507 traded vs OI 0
- **UBER** CALL 70 2026-11-27 (22DTE): 509 traded vs OI 359

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
