# GEX + FLOW SCAN - Thu Nov 05, 02:00 PM ET
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
Last 1m check 14:00:08 ET, last candle SPY 13:59, QQQ 13:59 | no errors
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
| 1 | **MSFT** | 539.08 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 44 | none: 129 puts 0-7DTE > 9 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (21 contracts' greeks worked out here) | POS +$824.6M | - | 540 | 500 | +$20.6M | +$0 bull / -$304k bear | out (clean 32, ADX 30, RVol 0.7) |
| 2 | **SMH** | 456.13 | FLOW SURGE | **CALLS** | 40 | none: 86 calls 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (6 contracts' greeks worked out here) | NEG -$278.0M | - | 445 | 500 | +$41.5M | +$60k bull / +$0 bear | out (clean 35, ADX 32, RVol 0.5) |
| 3 | **PLTR** | 154.90 | FLOW SURGE | **CALLS** | 37 | none: 16 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (3 contracts' greeks worked out here) | NEG -$45.8M | - | 165 | 150 | +$13.3M | +$49k bull / -$45k bear | out (clean 27, ADX 26, RVol 0.4) |
| 4 | **COIN** | 135.22 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 31 | none: 25 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (5 contracts' greeks worked out here) | POS +$11.7M | - | 142 | 135 | +$1.9M | - | out (clean 33, ADX 24, RVol 0.3) |
| 5 | **SPY** | 736.96 | - | **-** | 29 | - | NEG -$13.2B | 770.09 | 760 | 740 | +$1.2B | +$2.4M bull / -$1.5M bear | out (clean 36, ADX 49, RVol 1.1) |
| 6 | **QQQ** | 652.93 | - | **-** | 26 | - | NEG -$4.6B | - | 700 | 650 | +$825.0M | +$1.7M bull / -$2.8M bear | out (clean 36, ADX 36, RVol 1.0) |
| 7 | **IWM** | 271.62 | - | **-** | 26 | - | NEG -$2.8B | 287.23 | 285 | 270 | +$55.2M | +$67k bull / +$0 bear | out (clean 37, ADX 44, RVol 0.6) |
| 8 | **NVDA** | 183.32 | - | **-** | 26 | - | NEG -$246.3M | - | 200 | 190 | +$74.5M | +$494k bull / -$109k bear | out (clean 34, ADX 40, RVol 1.0) |
| 9 | **AVGO** | 297.90 | - | **-** | 26 | - | NEG -$107.3M | - | 325 | 300 | +$8.9M | +$187k bull / +$0 bear | out (clean 32, ADX 28, RVol 0.8) |
| 10 | **MU** | 676.38 | - | **-** | 25 | - | NEG -$62.8M | - | 700 | 700 | +$243.4M | +$6.4M bull / -$1.8M bear | out (clean 33, ADX 31, RVol 1.2) |
| 11 | **TSLA** | 340.96 | - | **-** | 24 | - | NEG -$132.7M | - | 350 | 350 | +$110.0M | +$140k bull / -$395k bear | out (clean 35, ADX 35, RVol 1.0) |
| 12 | **HOOD** | 76.97 | - | **-** | 22 | - | NEG -$7.7M | - | 83 | 80 | +$2.4M | +$0 bull / -$35k bear | out (clean 31, ADX 34, RVol 1.0) |
| 13 | **AAPL** | 343.60 | - | **-** | 21 | - | POS +$407.4M | 334.66 | 350 | 330 | +$23.0M | +$48k bull / -$415k bear | out (clean 31, ADX 31, RVol 0.6) |
| 14 | **AMD** | 415.00 | - | **-** | 21 | - | NEG -$95.6M | - | 430 | 440 | +$34.6M | +$28k bull / -$189k bear | out (clean 33, ADX 30, RVol 0.5) |
| 15 | **AMZN** | 259.69 | - | **-** | 20 | - | POS +$385.4M | - | 265 | 250 | +$23.0M | +$0 bull / -$206k bear | out (clean 35, ADX 17, RVol 0.5) |
| 16 | **GOOGL** | 283.68 | - | **-** | 20 | - | POS +$22.6M | 280.84 | 285 | 290 | +$8.7M | +$62k bull / +$0 bear | out (clean 35, ADX 18, RVol 0.4) |
| 17 | **CRM** | 221.12 | - | **-** | 19 | - | NEG -$16.4M | - | 240 | 220 | +$560k | - | out (clean 34, ADX 20, RVol 1.4) |
| 18 | **MSTR** | 128.06 | - | **-** | 18 | - | POS +$42.5M | - | 135 | 125 | +$3.7M | +$27k bull / +$0 bear | out (clean 34, ADX 18, RVol 0.4) |
| 19 | **META** | 604.41 | - | **-** | 16 | - | NEG -$119.4M | 621.85 | 650 | 600 | +$18.1M | +$0 bull / -$137k bear | out (clean 34, ADX 13, RVol 0.3) |
| 20 | **DELL** | 324.48 | - | **-** | 15 | - | NEG -$12.5M | - | 350 | 340 | +$6.2M | - | out (clean 34, ADX 27, RVol 0.8) |
| 21 | **BABA** | 106.87 | - | **-** | 15 | - | POS +$21.0M | - | 110 | 110 | +$1.3M | - | out (clean 36, ADX 10, RVol 0.6) |
| 22 | **NFLX** | 65.18 | - | **-** | 14 | - | POS +$30.4M | 62.06 | 65 | 65 | +$963k | - | out (clean 32, ADX 25, RVol 0.5) |
| 23 | **ARM** | 169.15 | - | **-** | 11 | - | NEG -$7.0M | - | 180 | 180 | +$1.4M | - | out (clean 27, ADX 18, RVol 0.5) |
| 24 | **SMCI** | 26.75 | - | **-** | 10 | - | NEG -$3.0M | - | 28 | 27 | +$414k | - | out (clean 36, ADX 17, RVol 0.6) |
| 25 | **ORCL** | 114.75 | - | **-** | 10 | - | NEG -$57.3M | - | 125 | 115 | +$2.9M | - | out (clean 31, ADX 22, RVol 0.6) |
| 26 | **UBER** | 68.47 | - | **-** | 9 | - | POS +$2.4M | 67.94 | 70 | 65 | +$191k | - | out (clean 31, ADX 8, RVol 0.4) |
| 27 | **SHOP** | 143.89 | - | **-** | 7 | - | NEG -$5.3M | - | 144 | 135 | -$131k | - | out (clean 38, ADX 16, RVol 0.3) |

## Big prints this scan (93)
- **QQQ** PUT 650 2026-11-05 (0DTE): 2,273 @ 2.56 = **+$582k** BUY | vol 266,158 / OI 3,473
- **QQQ** PUT 685 2026-11-06 (1DTE): 99 @ 33.10 = **+$328k** SELL | vol 7,969 / OI 9,276
- **QQQ** CALL 663 2026-11-09 (4DTE): 529 @ 6.16 = **+$326k** BUY | vol 21,395 / OI 0
- **SPY** CALL 735 2026-11-06 (1DTE): 340 @ 6.30 = **+$214k** BUY | vol 5,797 / OI 399
- **MU** PUT 670 2026-11-09 (4DTE): 68 @ 30.00 = **+$204k** BUY | vol 4,148 / OI 0
- **MU** CALL 710 2026-11-06 (1DTE): 222 @ 8.55 = **+$190k** SELL | vol 16,773 / OI 16
- **QQQ** CALL 663 2026-11-09 (4DTE): 271 @ 6.16 = **+$167k** BUY | vol 21,395 / OI 0
- **MU** PUT 660 2026-11-06 (1DTE): 99 @ 15.80 = **+$156k** SELL | vol 19,716 / OI 0
- **QQQ** PUT 650 2026-11-06 (1DTE): 200 @ 7.30 = **+$146k** BUY | vol 57,267 / OI 11,913
- **NVDA** PUT 185 2026-11-06 (1DTE): 261 @ 4.76 = **+$124k** SELL | vol 78,353 / OI 9,821
- **QQQ** CALL 663 2026-11-09 (4DTE): 200 @ 6.16 = **+$123k** BUY | vol 21,395 / OI 0
- **MU** PUT 700 2026-11-09 (4DTE): 26 @ 44.85 = **+$117k** SELL | vol 4,042 / OI 0
- **QQQ** PUT 655 2026-11-05 (0DTE): 200 @ 5.60 = **+$112k** BUY | vol 143,653 / OI 1,387
- **SPY** PUT 758 2026-11-06 (1DTE): 50 @ 22.20 = **+$111k** MID | vol 7,787 / OI 2,698
- **QQQ** PUT 655 2026-11-05 (0DTE): 200 @ 5.45 = **+$109k** BUY | vol 143,653 / OI 1,387

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 766 2026-11-12 (7DTE): 500 traded vs OI 34
- **SPY** PUT 741 2026-11-16 (11DTE): 517 traded vs OI 24
- **SPY** PUT 737 2026-11-18 (13DTE): 571 traded vs OI 0
- **SPY** PUT 725 2026-12-04 (29DTE): 1,047 traded vs OI 1,025
- **QQQ** PUT 605 2026-11-11 (6DTE): 534 traded vs OI 0
- **QQQ** CALL 675 2026-11-11 (6DTE): 501 traded vs OI 43
- **IWM** PUT 269 2026-11-10 (5DTE): 548 traded vs OI 196
- **IWM** CALL 275 2026-11-13 (8DTE): 1,823 traded vs OI 1,802
- **NVDA** CALL 185 2026-11-18 (13DTE): 582 traded vs OI 2
- **AMZN** CALL 257.5 2026-11-13 (8DTE): 750 traded vs OI 715
- **PLTR** PUT 149 2026-11-13 (8DTE): 519 traded vs OI 210
- **MU** CALL 640 2026-11-06 (1DTE): 505 traded vs OI 0
- **ORCL** PUT 111 2026-11-13 (8DTE): 532 traded vs OI 279
- **UBER** CALL 73 2026-11-13 (8DTE): 501 traded vs OI 378
- **BABA** PUT 100 2026-11-13 (8DTE): 1,450 traded vs OI 1,442

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
