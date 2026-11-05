# GEX + FLOW SCAN - Thu Nov 05, 03:25 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (5)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 15:00 | **SMCI** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/06 28.5C | 0.46 | 0.33 | -7% (0m) | **-28%** | +29% | 28.14 |
| 10:55 | **BABA** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/06 102P | 0.75 | 0.33 | -5% (9m) | **-56%** (done) | +27% | 103.58 |
| 09:52 | **SPY** | **PUTS** | 1m WHIPSAW (R1) | 11/05 749P | 0.78 | 11.35 | +1355% (60m) | **+1355%** (done) | +47% | 753.11 hit |
| 09:50 | **BABA** | **CALLS** | TREND + FLOW | 11/06 111C | 0.48 | 0.20 | -12% (0m) | **-58%** (done) | +136% | 110 |
| 09:40 | **QQQ** | **CALLS** | 1m WHIPSAW (R1) | 11/05 683C | 0.78 | 0.10 | -4% (0m) | **-87%** (done) | +66% | 678.43 |

## 1m RULES on SPY / QQQ - loose (5 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 15:25:08 ET, last candle SPY 15:24, QQQ 15:24 | no errors
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
| 1 | **GOOGL** | 284.48 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 38 | none: 69 puts 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (8 contracts' greeks worked out here) | POS +$19.4M | 281.98 | 285 | 290 | +$8.6M | +$311k bull / +$0 bear | out (clean 34, ADX 16, RVol 0.6) |
| 2 | **DELL** | 323.56 | - | **-** | 26 | - | NEG -$16.3M | - | 350 | 340 | +$6.4M | +$56k bull / +$0 bear | out (clean 32, ADX 19, RVol 1.9) |
| 3 | **SPY** | 736.18 | - | **-** | 25 | - | NEG -$14.2B | 769.29 | 760 | 740 | +$1.2B | +$2.7M bull / -$103k bear | out (clean 36, ADX 25, RVol 1.3) |
| 4 | **AVGO** | 295.65 | - | **-** | 25 | - | NEG -$116.6M | - | 325 | 300 | +$9.1M | +$380k bull / +$0 bear | out (clean 31, ADX 19, RVol 1.5) |
| 5 | **PLTR** | 155.31 | - | **-** | 25 | - | NEG -$56.0M | - | 165 | 150 | +$12.2M | +$326k bull / +$0 bear | out (clean 27, ADX 16, RVol 1.2) |
| 6 | **QQQ** | 652.39 | - | **-** | 23 | - | NEG -$4.8B | - | 700 | 650 | +$853.2M | +$7.2M bull / -$103k bear | out (clean 35, ADX 20, RVol 1.2) |
| 7 | **IWM** | 271.92 | - | **-** | 23 | - | NEG -$2.9B | 287.35 | 285 | 270 | +$55.2M | +$55k bull / +$0 bear | out (clean 36, ADX 22, RVol 1.4) |
| 8 | **MSFT** | 535.51 | - | **-** | 23 | - | POS +$722.6M | - | 540 | 500 | +$22.2M | +$383k bull / +$0 bear | out (clean 32, ADX 20, RVol 0.7) |
| 9 | **MU** | 678.35 | - | **-** | 23 | - | NEG -$101.5M | - | 700 | 700 | +$228.0M | +$7.1M bull / -$976k bear | out (clean 32, ADX 18, RVol 2.1) |
| 10 | **SMH** | 454.68 | - | **-** | 22 | - | NEG -$284.2M | - | 445 | 465 | +$29.2M | +$454k bull / +$0 bear | out (clean 34, ADX 19, RVol 0.9) |
| 11 | **TSLA** | 342.88 | - | **-** | 22 | - | NEG -$165.3M | - | 350 | 350 | +$109.0M | +$1.5M bull / -$477k bear | out (clean 35, ADX 17, RVol 1.8) |
| 12 | **BABA** | 107.97 | - | **-** | 22 | - | POS +$20.5M | - | 110 | 110 | +$800k | +$38k bull / +$0 bear | out (clean 35, ADX 23, RVol 1.2) |
| 13 | **NVDA** | 183.27 | - | **-** | 21 | - | NEG -$280.7M | - | 200 | 190 | +$73.7M | +$939k bull / +$0 bear | out (clean 34, ADX 20, RVol 0.8) |
| 14 | **AAPL** | 345.36 | - | **-** | 21 | - | POS +$484.4M | 335.37 | 350 | 330 | +$25.6M | +$751k bull / -$68k bear | out (clean 31, ADX 17, RVol 1.8) |
| 15 | **AMZN** | 259.68 | - | **-** | 20 | - | POS +$348.6M | - | 265 | 250 | +$24.8M | +$131k bull / -$97k bear | out (clean 34, ADX 15, RVol 0.6) |
| 16 | **AMD** | 415.18 | - | **-** | 19 | - | NEG -$117.8M | - | 430 | 440 | +$35.2M | +$1.1M bull / +$0 bear | out (clean 32, ADX 16, RVol 0.9) |
| 17 | **MSTR** | 129.19 | - | **-** | 19 | - | POS +$43.1M | - | 135 | 125 | +$4.0M | +$0 bull / -$33k bear | out (clean 33, ADX 17, RVol 1.1) |
| 18 | **CRM** | 220.85 | - | **-** | 19 | - | NEG -$18.2M | - | 240 | 220 | +$561k | - | out (clean 33, ADX 17, RVol 1.6) |
| 19 | **ORCL** | 115.46 | - | **-** | 18 | - | NEG -$67.6M | - | 125 | 115 | +$2.9M | +$27k bull / +$0 bear | out (clean 31, ADX 13, RVol 0.6) |
| 20 | **META** | 606.67 | - | **-** | 16 | - | NEG -$147.8M | 624.43 | 650 | 600 | +$17.5M | +$0 bull / -$39k bear | out (clean 33, ADX 11, RVol 0.5) |
| 21 | **ARM** | 168.62 | - | **-** | 14 | - | NEG -$6.8M | - | 180 | 180 | +$1.5M | - | out (clean 26, ADX 15, RVol 2.2) |
| 22 | **COIN** | 137.99 | - | **-** | 13 | - | POS +$11.5M | 133.85 | 142 | 130 | +$1.6M | - | out (clean 33, ADX 26, RVol 0.6) |
| 23 | **NFLX** | 64.79 | - | **-** | 12 | - | POS +$28.1M | 62.43 | 65 | 65 | +$869k | - | out (clean 32, ADX 24, RVol 0.9) |
| 24 | **HOOD** | 78.50 | - | **-** | 9 | - | NEG -$14.5M | - | 85 | 80 | +$2.2M | - | out (clean 31, ADX 24, RVol 0.7) |
| 25 | **UBER** | 68.37 | - | **-** | 9 | - | POS +$1.3M | 68.17 | 70 | 65 | +$193k | - | out (clean 30, ADX 11, RVol 0.7) |
| 26 | **SMCI** | 27.32 | - | **-** | 8 | - | NEG -$4.2M | - | 28 | 27 | +$159k | - | out (clean 34, ADX 24, RVol 0.7) |
| 27 | **SHOP** | 144.18 | - | **-** | 6 | - | NEG -$5.9M | - | 144 | 135 | -$134k | - | out (clean 37, ADX 11, RVol 0.5) |

## Big prints this scan (96)
- **MU** PUT 680 2026-11-09 (4DTE): 300 @ 31.30 = **+$939k** MID | vol 3,669 / OI 0
- **MU** PUT 680 2026-11-09 (4DTE): 201 @ 31.50 = **+$633k** BUY | vol 3,669 / OI 0
- **QQQ** PUT 654 2026-11-09 (4DTE): 300 @ 10.37 = **+$311k** SELL | vol 2,732 / OI 39
- **SPY** PUT 740 2026-11-05 (0DTE): 831 @ 3.70 = **+$307k** SELL | vol 326,816 / OI 3,497
- **QQQ** CALL 655 2026-11-06 (1DTE): 400 @ 7.40 = **+$296k** BUY | vol 35,963 / OI 1,189
- **QQQ** CALL 655 2026-11-06 (1DTE): 359 @ 6.93 = **+$249k** BUY | vol 35,963 / OI 1,189
- **QQQ** CALL 652 2026-11-09 (4DTE): 200 @ 11.80 = **+$236k** BUY | vol 1,869 / OI 0
- **MU** CALL 700 2026-11-09 (4DTE): 100 @ 21.75 = **+$218k** BUY | vol 3,341 / OI 0
- **SMH** PUT 475 2026-11-06 (1DTE): 100 @ 20.70 = **+$207k** SELL | vol 2,411 / OI 1,734
- **MU** PUT 680 2026-11-09 (4DTE): 60 @ 31.50 = **+$189k** BUY | vol 3,669 / OI 0
- **QQQ** CALL 655 2026-11-06 (1DTE): 233 @ 6.92 = **+$161k** BUY | vol 35,963 / OI 1,189
- **SMH** PUT 455 2026-11-06 (1DTE): 150 @ 10.00 = **+$150k** MID | vol 2,549 / OI 619
- **QQQ** CALL 657 2026-11-09 (4DTE): 172 @ 8.41 = **+$145k** BUY | vol 3,428 / OI 0
- **QQQ** PUT 651 2026-11-06 (1DTE): 200 @ 7.11 = **+$142k** MID | vol 17,882 / OI 560
- **SPY** PUT 739 2026-11-05 (0DTE): 500 @ 2.83 = **+$142k** SELL | vol 208,484 / OI 472

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 710 2026-11-09 (4DTE): 1,261 traded vs OI 1,097
- **SPY** PUT 709 2026-11-09 (4DTE): 544 traded vs OI 3
- **SPY** CALL 787 2026-11-17 (12DTE): 500 traded vs OI 0
- **SPY** CALL 797 2026-11-27 (22DTE): 687 traded vs OI 437
- **SPY** PUT 765 2026-11-18 (13DTE): 803 traded vs OI 0
- **QQQ** PUT 697 2026-11-05 (0DTE): 813 traded vs OI 24
- **QQQ** CALL 654 2026-11-13 (8DTE): 514 traded vs OI 0
- **QQQ** PUT 697 2026-11-06 (1DTE): 942 traded vs OI 631
- **QQQ** CALL 655 2026-11-11 (6DTE): 506 traded vs OI 2
- **QQQ** PUT 590 2026-12-04 (29DTE): 512 traded vs OI 348
- **AMD** CALL 415 2026-11-20 (15DTE): 508 traded vs OI 0
- **AMD** PUT 417.5 2026-11-13 (8DTE): 537 traded vs OI 58
- **AMD** CALL 425 2026-11-09 (4DTE): 500 traded vs OI 1
- **MSFT** CALL 537.5 2026-11-20 (15DTE): 500 traded vs OI 385
- **AVGO** CALL 295 2026-11-20 (15DTE): 503 traded vs OI 11

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
