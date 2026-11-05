# GEX + FLOW SCAN - Thu Nov 05, 01:10 PM ET
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
Last 1m check 13:10:08 ET, last candle SPY 13:09, QQQ 13:09 | no errors
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
| 1 | **IWM** | 271.52 | TREND (flow not with it) | **PUTS** | 49 | 11/05 271P @ 0.57 (delta 0.40) = est +98% at 270 | NEG -$2.7B | 287.18 | 285 | 270 | +$61.9M | +$4.7M bull / -$558k bear | SHORT (clean 38, ADX 56, RVol 2.3) |
| 2 | **SPY** | 736.66 | FLOW SURGE | **CALLS** | 48 | none: 657 calls 0-7DTE > 28 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (214 contracts' greeks worked out here) | NEG -$12.9B | 769.23 | 760 | 740 | +$1.2B | +$10.2M bull / +$0 bear | SHORT (clean 36, ADX 58, RVol 1.2) |
| 3 | **SMH** | 453.64 | FLOW SURGE | **CALLS** | 46 | none: 86 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (4 contracts' greeks worked out here) | NEG -$207.0M | - | 445 | 465 | +$41.6M | +$257k bull / +$0 bear | out (clean 35, ADX 44, RVol 1.1) |
| 4 | **MU** | 678.29 | TREND (flow not with it) | **PUTS** | 46 | none: 82 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (6 contracts' greeks worked out here) | NEG -$65.6M | - | 700 | 700 | +$215.2M | +$9.4M bull / -$5.5M bear | SHORT (clean 33, ADX 38, RVol 2.6) |
| 5 | **MSFT** | 538.78 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 45 | none: 132 puts 0-7DTE > 12 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (21 contracts' greeks worked out here) | POS +$827.2M | - | 540 | 500 | +$21.3M | +$443k bull / +$0 bear | out (clean 32, ADX 32, RVol 0.7) |
| 6 | **PLTR** | 154.82 | FLOW SURGE | **CALLS** | 41 | none: 16 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (3 contracts' greeks worked out here) | NEG -$46.3M | - | 165 | 150 | +$13.1M | +$48k bull / +$0 bear | out (clean 28, ADX 33, RVol 0.7) |
| 7 | **TSLA** | 339.70 | TREND (flow not with it) | **PUTS** | 40 | none: 68 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (3 contracts' greeks worked out here) | NEG -$128.2M | - | 350 | 350 | +$110.2M | +$1.5M bull / +$0 bear | SHORT (clean 35, ADX 42, RVol 1.6) |
| 8 | **NVDA** | 182.32 | TREND (flow not with it) | **PUTS** | 39 | none: 36 puts 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (2 contracts' greeks worked out here) | NEG -$232.5M | - | 200 | 190 | +$76.5M | +$3.7M bull / -$374k bear | SHORT (clean 34, ADX 49, RVol 1.4) |
| 9 | **QQQ** | 651.87 | - | **-** | 28 | - | NEG -$4.5B | - | 700 | 680 | +$827.7M | +$5.1M bull / -$1.1M bear | out (clean 36, ADX 46, RVol 0.9) |
| 10 | **AVGO** | 297.77 | - | **-** | 27 | - | NEG -$106.5M | - | 325 | 300 | +$9.0M | +$51k bull / -$45k bear | out (clean 32, ADX 34, RVol 0.9) |
| 11 | **DELL** | 323.35 | - | **-** | 27 | - | NEG -$12.3M | - | 350 | 340 | +$6.4M | +$80k bull / -$75k bear | out (clean 35, ADX 33, RVol 0.6) |
| 12 | **AMD** | 412.76 | - | **-** | 24 | - | NEG -$92.8M | - | 430 | 440 | +$36.8M | +$515k bull / +$0 bear | out (clean 34, ADX 39, RVol 1.1) |
| 13 | **ORCL** | 114.28 | - | **-** | 23 | - | NEG -$56.3M | - | 125 | 115 | +$3.0M | +$26k bull / +$0 bear | out (clean 32, ADX 34, RVol 0.6) |
| 14 | **AAPL** | 344.28 | - | **-** | 22 | - | POS +$464.1M | 334.12 | 350 | 330 | +$21.4M | +$1.1M bull / -$353k bear | out (clean 31, ADX 33, RVol 0.7) |
| 15 | **MSTR** | 127.45 | - | **-** | 21 | - | POS +$43.7M | - | 135 | 125 | +$3.8M | +$104k bull / +$0 bear | out (clean 34, ADX 34, RVol 0.5) |
| 16 | **AMZN** | 259.95 | - | **-** | 20 | - | POS +$392.5M | - | 265 | 250 | +$22.0M | +$171k bull / -$108k bear | out (clean 35, ADX 14, RVol 0.7) |
| 17 | **COIN** | 135.42 | - | **-** | 20 | - | POS +$13.7M | - | 142 | 135 | +$2.1M | - | out (clean 33, ADX 42, RVol 0.6) |
| 18 | **CRM** | 220.92 | - | **-** | 20 | - | NEG -$16.5M | - | 240 | 220 | +$574k | - | out (clean 34, ADX 24, RVol 1.3) |
| 19 | **META** | 603.27 | - | **-** | 17 | - | NEG -$112.9M | 622.02 | 650 | 600 | +$20.8M | +$1.1M bull / +$0 bear | out (clean 34, ADX 16, RVol 0.5) |
| 20 | **BABA** | 106.69 | - | **-** | 16 | - | POS +$22.2M | - | 110 | 110 | +$1.3M | - | out (clean 36, ADX 14, RVol 0.4) |
| 21 | **NFLX** | 65.33 | - | **-** | 15 | - | POS +$30.0M | 61.97 | 65 | 65 | +$950k | - | out (clean 33, ADX 28, RVol 0.6) |
| 22 | **ARM** | 168.06 | - | **-** | 15 | - | NEG -$5.7M | - | 180 | 180 | +$1.4M | - | out (clean 27, ADX 28, RVol 1.0) |
| 23 | **HOOD** | 76.92 | - | **-** | 14 | - | NEG -$7.8M | - | 83 | 80 | +$2.2M | - | out (clean 32, ADX 44, RVol 1.0) |
| 24 | **SMCI** | 26.58 | - | **-** | 13 | - | NEG -$2.8M | - | 28 | 27 | +$451k | - | out (clean 36, ADX 31, RVol 0.5) |
| 25 | **GOOGL** | 284.09 | - | **-** | 10 | - | POS +$32.1M | 280.85 | 285 | 290 | +$8.6M | - | out (clean 35, ADX 14, RVol 0.6) |
| 26 | **UBER** | 68.42 | - | **-** | 9 | - | POS +$4.4M | 67.91 | 70 | 65 | +$180k | - | out (clean 32, ADX 9, RVol 0.5) |
| 27 | **SHOP** | 144.49 | - | **-** | 8 | - | NEG -$3.8M | - | 144 | 135 | -$134k | - | out (clean 38, ADX 17, RVol 0.5) |

## Big prints this scan (154)
- **MU** PUT 670 2026-11-09 (4DTE): 300 @ 27.60 = **+$828k** BUY | vol 3,486 / OI 0
- **MU** PUT 670 2026-11-09 (4DTE): 299 @ 27.30 = **+$816k** BUY | vol 3,486 / OI 0
- **SPY** PUT 756 2026-11-06 (1DTE): 200 @ 17.94 = **+$359k** SELL | vol 9,238 / OI 2,491
- **SPY** PUT 764 2026-11-05 (0DTE): 136 @ 25.97 = **+$353k** MID | vol 32,401 / OI 9
- **SPY** PUT 764 2026-11-05 (0DTE): 136 @ 25.97 = **+$353k** MID | vol 32,401 / OI 9
- **SPY** PUT 755 2026-11-06 (1DTE): 200 @ 17.04 = **+$341k** SELL | vol 20,317 / OI 8,694
- **AAPL** CALL 350 2026-11-06 (1DTE): 2,154 @ 1.31 = **+$282k** BUY | vol 29,942 / OI 30,841
- **QQQ** PUT 650 2026-11-05 (0DTE): 999 @ 2.45 = **+$245k** BUY | vol 204,991 / OI 3,473
- **QQQ** PUT 660 2026-11-06 (1DTE): 172 @ 12.00 = **+$206k** BUY | vol 32,744 / OI 14,507
- **IWM** PUT 268 2026-11-06 (1DTE): 2,000 @ 1.01 = **+$202k** BUY | vol 4,883 / OI 8,239
- **SPY** PUT 750 2026-11-06 (1DTE): 147 @ 13.03 = **+$192k** MID | vol 41,966 / OI 42,367
- **MU** PUT 670 2026-11-06 (1DTE): 100 @ 19.00 = **+$190k** BUY | vol 22,222 / OI 0
- **QQQ** PUT 655 2026-11-05 (0DTE): 400 @ 4.70 = **+$188k** BUY | vol 129,935 / OI 1,387
- **MU** PUT 650 2026-11-06 (1DTE): 150 @ 12.50 = **+$188k** BUY | vol 31,655 / OI 0
- **QQQ** PUT 655 2026-11-05 (0DTE): 395 @ 4.70 = **+$186k** BUY | vol 129,935 / OI 1,387

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 772 2026-11-16 (11DTE): 518 traded vs OI 93
- **SPY** PUT 717 2026-11-12 (7DTE): 508 traded vs OI 20
- **SPY** PUT 724 2026-11-12 (7DTE): 513 traded vs OI 21
- **SPY** PUT 725 2026-11-11 (6DTE): 940 traded vs OI 935
- **SPY** PUT 670 2026-11-30 (25DTE): 789 traded vs OI 0
- **QQQ** PUT 654 2026-11-30 (25DTE): 521 traded vs OI 78
- **QQQ** PUT 666 2026-11-13 (8DTE): 500 traded vs OI 9
- **QQQ** CALL 703 2026-11-13 (8DTE): 764 traded vs OI 553
- **IWM** PUT 269 2026-11-13 (8DTE): 530 traded vs OI 529
- **TSLA** CALL 342.5 2026-11-13 (8DTE): 524 traded vs OI 29
- **META** CALL 635 2026-11-18 (13DTE): 1,446 traded vs OI 0
- **AVGO** CALL 297.5 2026-11-06 (1DTE): 591 traded vs OI 16
- **MU** PUT 650 2026-11-11 (6DTE): 501 traded vs OI 0
- **MSTR** CALL 126 2026-11-06 (1DTE): 514 traded vs OI 290

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
