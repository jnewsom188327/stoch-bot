# GEX + FLOW SCAN - Thu Nov 05, 12:10 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (4)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:55 | **BABA** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/06 102P | 0.75 | 0.33 | -5% (9m) | **-56%** (done) | +27% | 103.58 |
| 09:52 | **SPY** | **PUTS** | 1m WHIPSAW (R1) | 11/05 749P | 0.78 | 11.35 | +1355% (60m) | **+1355%** (done) | +47% | 753.11 hit |
| 09:50 | **BABA** | **CALLS** | TREND + FLOW | 11/06 111C | 0.48 | 0.20 | -12% (0m) | **-58%** (done) | +136% | 110 |
| 09:40 | **QQQ** | **CALLS** | 1m WHIPSAW (R1) | 11/05 683C | 0.78 | 0.10 | -4% (0m) | **-87%** (done) | +66% | 678.43 |

## 1m RULES on SPY / QQQ - loose (4 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 12:10:08 ET, last candle SPY 12:09, QQQ 12:09 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 11:44 | SPY | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |
| 10:38 | QQQ | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | no contract: 64 puts 0-1DTE > 1 priced 0.40-0.80 > 0 delta 0.15+ > 0 spread ok > 0 liquid  |
| 09:51 | SPY | 1m WHIPSAW | R1 | PUTS | TURNING away | **FIRE** SPY261105P00749000 |
| 09:39 | QQQ | 1m WHIPSAW | R1 | CALLS | AGAINST you | **FIRE** QQQ261105C00683000 |

## Flow surges NOT fired - price disagreed (30 today, last 5)
- 12:10 IWM CALLS: price -1.05 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 12:05 IWM CALLS: price -1.32 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 12:00 IWM CALLS: price -0.69 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 11:55 IWM CALLS: price -1.66 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 11:15 IWM CALLS: price -0.15 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **IWM** | 273.09 | FLOW SURGE | **CALLS** | 52 | 11/05 275C @ 0.45 (delta 0.26) = est +107% at 275.05 | NEG -$2.6B | 286.43 | 285 | 270 | +$53.0M | +$119k bull / +$0 bear | SHORT (clean 36, ADX 53, RVol 1.6) |
| 2 | **SMH** | 457.14 | FLOW SURGE | **CALLS** | 49 | none: 89 calls 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (3 contracts' greeks worked out here) | NEG -$251.3M | - | 500 | 465 | +$40.8M | +$551k bull / +$0 bear | out (clean 35, ADX 47, RVol 1.5) |
| 3 | **SPY** | 740.72 | FLOW SURGE | **CALLS** | 45 | none: 656 calls 0-7DTE > 26 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (202 contracts' greeks worked out here) | NEG -$12.7B | 769.21 | 760 | 740 | +$1.1B | +$3.4M bull / +$0 bear | out (clean 36, ADX 58, RVol 1.2) |
| 4 | **PLTR** | 155.26 | FLOW SURGE | **CALLS** | 41 | none: 16 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (2 contracts' greeks worked out here) | NEG -$45.5M | - | 165 | 150 | +$13.3M | +$176k bull / +$0 bear | out (clean 28, ADX 40, RVol 0.4) |
| 5 | **COIN** | 134.70 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 39 | none: 25 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (3 contracts' greeks worked out here) | POS +$11.3M | - | 142 | 135 | +$2.1M | - | out (clean 33, ADX 51, RVol 0.6) |
| 6 | **NVDA** | 185.22 | - | **-** | 29 | - | NEG -$263.1M | - | 200 | 190 | +$59.4M | +$1.7M bull / +$0 bear | out (clean 33, ADX 48, RVol 1.7) |
| 7 | **MSFT** | 541.98 | - | **-** | 29 | - | POS +$864.1M | - | 540 | 500 | +$19.2M | +$71k bull / -$35k bear | out (clean 32, ADX 38, RVol 1.6) |
| 8 | **QQQ** | 655.40 | - | **-** | 28 | - | NEG -$4.7B | - | 700 | 680 | +$744.1M | +$9.5M bull / +$0 bear | out (clean 35, ADX 51, RVol 1.2) |
| 9 | **TSLA** | 343.53 | - | **-** | 28 | - | NEG -$132.3M | - | 370 | 350 | +$99.2M | +$2.0M bull / +$0 bear | out (clean 34, ADX 43, RVol 1.8) |
| 10 | **AVGO** | 300.64 | - | **-** | 28 | - | NEG -$118.7M | - | 330 | 300 | +$7.4M | +$51k bull / +$0 bear | out (clean 31, ADX 35, RVol 1.1) |
| 11 | **MU** | 688.53 | - | **-** | 28 | - | NEG -$89.4M | - | 700 | 700 | +$186.0M | +$10.5M bull / +$0 bear | out (clean 34, ADX 45, RVol 1.5) |
| 12 | **SHOP** | 144.56 | TREND (flow not with it) | **CALLS** | 28 | none: 23 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (3 contracts' greeks worked out here) | NEG -$4.2M | - | 144 | 135 | -$93k | - | LONG (clean 38, ADX 31, RVol 1.0) |
| 13 | **AMD** | 414.17 | - | **-** | 25 | - | NEG -$96.0M | - | 430 | 440 | +$38.5M | +$433k bull / +$0 bear | out (clean 33, ADX 42, RVol 0.8) |
| 14 | **MSTR** | 127.20 | - | **-** | 25 | - | POS +$35.3M | - | 135 | 125 | +$3.9M | +$41k bull / +$0 bear | out (clean 34, ADX 43, RVol 1.2) |
| 15 | **AAPL** | 345.17 | - | **-** | 24 | - | POS +$502.5M | 334.11 | 350 | 330 | +$20.2M | +$498k bull / -$537k bear | out (clean 31, ADX 29, RVol 1.6) |
| 16 | **AMZN** | 261.73 | - | **-** | 24 | - | POS +$404.2M | - | 265 | 250 | +$21.2M | +$163k bull / -$158k bear | out (clean 35, ADX 20, RVol 1.7) |
| 17 | **GOOGL** | 285.76 | - | **-** | 22 | - | POS +$36.7M | 281.2 | 290 | 290 | +$7.9M | +$0 bull / -$48k bear | out (clean 35, ADX 18, RVol 1.0) |
| 18 | **META** | 606.77 | - | **-** | 20 | - | NEG -$82.4M | 620.14 | 650 | 600 | +$19.3M | +$231k bull / -$449k bear | out (clean 34, ADX 23, RVol 1.0) |
| 19 | **DELL** | 325.12 | - | **-** | 18 | - | NEG -$12.8M | - | 350 | 340 | +$6.2M | - | out (clean 35, ADX 33, RVol 0.9) |
| 20 | **CRM** | 222.75 | - | **-** | 18 | - | NEG -$14.9M | - | 240 | 220 | +$520k | - | out (clean 34, ADX 18, RVol 0.6) |
| 21 | **BABA** | 107.10 | - | **-** | 18 | - | POS +$20.8M | - | 110 | 110 | +$1.2M | - | out (clean 38, ADX 21, RVol 0.7) |
| 22 | **ARM** | 167.49 | - | **-** | 17 | - | NEG -$5.7M | - | 180 | 180 | +$1.4M | - | out (clean 27, ADX 41, RVol 0.8) |
| 23 | **SMCI** | 26.64 | - | **-** | 16 | - | NEG -$2.9M | - | 28 | 27 | +$448k | - | out (clean 36, ADX 40, RVol 0.8) |
| 24 | **ORCL** | 114.50 | - | **-** | 16 | - | NEG -$55.6M | - | 125 | 115 | +$2.8M | - | out (clean 34, ADX 43, RVol 1.3) |
| 25 | **NFLX** | 65.55 | - | **-** | 14 | - | POS +$32.3M | 62.01 | 65 | 65 | +$814k | - | out (clean 32, ADX 20, RVol 0.8) |
| 26 | **HOOD** | 77.61 | - | **-** | 14 | - | NEG -$8.7M | - | 85 | 80 | +$2.0M | - | out (clean 31, ADX 48, RVol 0.6) |
| 27 | **UBER** | 68.78 | - | **-** | 9 | - | POS +$4.8M | 68.07 | 70 | 65 | +$157k | - | out (clean 32, ADX 13, RVol 0.6) |

## Big prints this scan (89)
- **MU** PUT 670 2026-11-06 (1DTE): 200 @ 11.45 = **+$229k** SELL | vol 18,014 / OI 0
- **PLTR** PUT 155 2026-11-06 (1DTE): 550 @ 3.20 = **+$176k** SELL | vol 11,345 / OI 5,607
- **SPY** PUT 776 2026-11-06 (1DTE): 50 @ 33.43 = **+$167k** SELL | vol 460 / OI 1,101
- **QQQ** CALL 660 2026-11-05 (0DTE): 495 @ 3.00 = **+$148k** BUY | vol 107,638 / OI 12
- **QQQ** PUT 656 2026-11-06 (1DTE): 200 @ 7.14 = **+$143k** SELL | vol 7,549 / OI 214
- **MU** PUT 690 2026-11-09 (4DTE): 52 @ 24.35 = **+$127k** SELL | vol 2,108 / OI 0
- **SPY** PUT 752 2026-11-09 (4DTE): 100 @ 12.50 = **+$125k** SELL | vol 1,664 / OI 193
- **MU** PUT 707.5 2026-11-09 (4DTE): 35 @ 34.60 = **+$121k** SELL | vol 883 / OI 0
- **MU** PUT 707.5 2026-11-09 (4DTE): 35 @ 34.50 = **+$121k** SELL | vol 883 / OI 0
- **MU** PUT 670 2026-11-06 (1DTE): 100 @ 11.77 = **+$118k** SELL | vol 18,014 / OI 0
- **SPY** PUT 766 2026-11-05 (0DTE): 50 @ 23.49 = **+$117k** SELL | vol 12,158 / OI 4
- **META** CALL 600 2026-11-06 (1DTE): 80 @ 14.49 = **+$116k** SELL | vol 4,284 / OI 258
- **SPY** PUT 743 2026-11-06 (1DTE): 199 @ 5.77 = **+$115k** SELL | vol 16,693 / OI 1,527
- **SPY** PUT 743 2026-11-05 (0DTE): 372 @ 3.01 = **+$112k** SELL | vol 134,595 / OI 1,127
- **QQQ** PUT 669 2026-11-05 (0DTE): 100 @ 11.01 = **+$110k** SELL | vol 30,256 / OI 168

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 781 2026-11-06 (1DTE): 3,027 traded vs OI 3,013
- **SPY** PUT 700 2026-11-09 (4DTE): 4,743 traded vs OI 4,715
- **SPY** CALL 796 2026-11-10 (5DTE): 502 traded vs OI 40
- **SPY** PUT 752 2026-11-10 (5DTE): 500 traded vs OI 108
- **SPY** CALL 752 2026-11-11 (6DTE): 517 traded vs OI 10
- **SPY** PUT 700 2026-11-27 (22DTE): 22,678 traded vs OI 4,360
- **SPY** PUT 705 2026-11-20 (15DTE): 9,308 traded vs OI 8,993
- **SPY** CALL 745 2026-11-30 (25DTE): 863 traded vs OI 714
- **SPY** PUT 730 2026-11-27 (22DTE): 23,367 traded vs OI 3,320
- **QQQ** PUT 640 2026-11-12 (7DTE): 535 traded vs OI 380
- **QQQ** CALL 689 2026-11-09 (4DTE): 683 traded vs OI 33
- **QQQ** PUT 630 2026-11-17 (12DTE): 505 traded vs OI 32
- **QQQ** CALL 687 2026-11-30 (25DTE): 500 traded vs OI 93
- **QQQ** CALL 675 2026-11-27 (22DTE): 741 traded vs OI 72
- **QQQ** PUT 645 2026-11-18 (13DTE): 519 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
