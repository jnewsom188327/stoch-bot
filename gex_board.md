# GEX + FLOW SCAN - Thu Nov 05, 12:30 PM ET
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
Last 1m check 12:30:08 ET, last candle SPY 12:29, QQQ 12:29 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 11:44 | SPY | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |
| 10:38 | QQQ | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | no contract: 64 puts 0-1DTE > 1 priced 0.40-0.80 > 0 delta 0.15+ > 0 spread ok > 0 liquid  |
| 09:51 | SPY | 1m WHIPSAW | R1 | PUTS | TURNING away | **FIRE** SPY261105P00749000 |
| 09:39 | QQQ | 1m WHIPSAW | R1 | CALLS | AGAINST you | **FIRE** QQQ261105C00683000 |

## Flow surges NOT fired - price disagreed (32 today, last 5)
- 12:20 IWM CALLS: under EMA 20 - flow says one way, price says the other
- 12:15 IWM CALLS: price -0.86 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 12:10 IWM CALLS: price -1.05 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 12:05 IWM CALLS: price -1.32 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 12:00 IWM CALLS: price -0.69 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **MSFT** | 540.30 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 49 | none: 129 puts 0-7DTE > 11 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (9 contracts' greeks worked out here) | POS +$858.0M | - | 540 | 500 | +$19.2M | +$62k bull / -$90k bear | out (clean 32, ADX 34, RVol 1.2) |
| 2 | **IWM** | 272.53 | TREND (flow not with it) | **PUTS** | 44 | none: 277 puts 0-7DTE > 16 priced 0.40-0.80 > 2 delta 0.2+ > 2 spread ok > 2 liquid > best one only +4% at the target (needs +20%) (85 contracts' greeks worked out here) | NEG -$2.7B | 287.02 | 285 | 270 | +$52.3M | +$1.6M bull / +$0 bear | SHORT (clean 37, ADX 53, RVol 1.7) |
| 3 | **SPY** | 739.41 | FLOW SURGE | **CALLS** | 43 | none: 655 calls 0-7DTE > 27 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (233 contracts' greeks worked out here) | NEG -$12.7B | 769.75 | 760 | 740 | +$1.1B | +$2.1M bull / -$1.9M bear | out (clean 36, ADX 57, RVol 0.9) |
| 4 | **MU** | 691.00 | TREND (flow not with it) | **PUTS** | 43 | none: 91 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (6 contracts' greeks worked out here) | NEG -$94.8M | - | 700 | 750 | +$176.0M | +$236k bull / -$8.3M bear | SHORT (clean 33, ADX 39, RVol 1.0) |
| 5 | **TSLA** | 341.24 | TREND (flow not with it) | **PUTS** | 39 | none: 71 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (4 contracts' greeks worked out here) | NEG -$128.3M | - | 370 | 350 | +$105.4M | +$1.7M bull / +$0 bear | SHORT (clean 35, ADX 43, RVol 1.6) |
| 6 | **SMH** | 457.53 | - | **-** | 33 | - | NEG -$296.8M | - | 500 | 500 | +$40.3M | +$0 bull / -$424k bear | out (clean 35, ADX 43, RVol 1.4) |
| 7 | **COIN** | 136.04 | - | **-** | 31 | - | POS +$16.7M | - | 142 | 135 | +$2.0M | +$0 bull / -$32k bear | out (clean 33, ADX 46, RVol 0.7) |
| 8 | **PLTR** | 155.29 | - | **-** | 30 | - | NEG -$45.1M | - | 165 | 150 | +$12.9M | +$0 bull / -$52k bear | out (clean 28, ADX 36, RVol 0.6) |
| 9 | **QQQ** | 654.78 | - | **-** | 28 | - | NEG -$4.6B | - | 700 | 680 | +$753.2M | +$3.6M bull / -$4.7M bear | out (clean 35, ADX 47, RVol 0.9) |
| 10 | **NVDA** | 184.32 | - | **-** | 27 | - | NEG -$256.7M | - | 200 | 190 | +$59.4M | +$599k bull / -$500k bear | out (clean 33, ADX 45, RVol 1.1) |
| 11 | **AVGO** | 299.15 | - | **-** | 27 | - | NEG -$107.9M | - | 325 | 300 | +$7.3M | +$0 bull / -$46k bear | out (clean 32, ADX 32, RVol 1.1) |
| 12 | **DELL** | 325.07 | - | **-** | 27 | - | NEG -$12.8M | - | 350 | 340 | +$6.1M | +$0 bull / -$29k bear | out (clean 35, ADX 32, RVol 0.8) |
| 13 | **AMD** | 417.23 | - | **-** | 24 | - | NEG -$96.1M | - | 430 | 440 | +$32.2M | +$0 bull / -$4.6M bear | out (clean 34, ADX 39, RVol 0.8) |
| 14 | **AAPL** | 344.68 | - | **-** | 23 | - | POS +$474.2M | 334.11 | 350 | 330 | +$20.1M | +$209k bull / -$233k bear | out (clean 31, ADX 31, RVol 1.2) |
| 15 | **HOOD** | 77.69 | - | **-** | 23 | - | NEG -$9.2M | - | 85 | 80 | +$1.6M | +$0 bull / -$63k bear | out (clean 32, ADX 44, RVol 0.7) |
| 16 | **MSTR** | 127.91 | - | **-** | 22 | - | POS +$45.4M | - | 135 | 125 | +$3.2M | +$0 bull / -$170k bear | out (clean 34, ADX 38, RVol 0.7) |
| 17 | **AMZN** | 261.78 | - | **-** | 21 | - | POS +$415.8M | - | 265 | 250 | +$20.9M | +$0 bull / -$122k bear | out (clean 35, ADX 17, RVol 1.0) |
| 18 | **GOOGL** | 285.89 | - | **-** | 21 | - | POS +$42.8M | 280.66 | 290 | 290 | +$7.4M | +$26k bull / -$29k bear | out (clean 35, ADX 16, RVol 0.9) |
| 19 | **SHOP** | 143.91 | - | **-** | 19 | - | NEG -$4.0M | - | 144 | 135 | -$134k | +$0 bull / -$32k bear | out (clean 38, ADX 26, RVol 0.4) |
| 20 | **META** | 606.30 | - | **-** | 18 | - | NEG -$92.7M | 620.38 | 650 | 600 | +$17.6M | +$482k bull / -$1.2M bear | out (clean 34, ADX 18, RVol 0.8) |
| 21 | **BABA** | 106.69 | - | **-** | 18 | - | POS +$22.0M | - | 110 | 110 | +$1.3M | - | out (clean 37, ADX 20, RVol 0.7) |
| 22 | **CRM** | 222.69 | - | **-** | 17 | - | NEG -$15.2M | - | 240 | 220 | +$520k | - | out (clean 34, ADX 17, RVol 0.4) |
| 23 | **SMCI** | 26.70 | - | **-** | 15 | - | NEG -$2.9M | - | 28 | 27 | +$430k | - | out (clean 37, ADX 35, RVol 1.0) |
| 24 | **ARM** | 168.93 | - | **-** | 15 | - | NEG -$6.9M | - | 180 | 180 | +$1.4M | - | out (clean 27, ADX 35, RVol 0.8) |
| 25 | **ORCL** | 114.74 | - | **-** | 14 | - | NEG -$55.9M | - | 125 | 115 | +$2.5M | - | out (clean 34, ADX 37, RVol 1.3) |
| 26 | **NFLX** | 65.52 | - | **-** | 13 | - | POS +$32.3M | 62.08 | 65 | 65 | +$757k | - | out (clean 32, ADX 21, RVol 0.7) |
| 27 | **UBER** | 68.51 | - | **-** | 9 | - | POS +$4.4M | 67.92 | 70 | 65 | +$156k | - | out (clean 32, ADX 11, RVol 0.7) |

## Big prints this scan (122)
- **IWM** PUT 272.5 2026-11-06 (1DTE): 4,000 @ 1.96 = **+$784k** SELL | vol 18,442 / OI 10,271
- **META** PUT 600 2026-11-09 (4DTE): 500 @ 10.20 = **+$510k** MID | vol 1,035 / OI 309
- **QQQ** CALL 645 2026-11-05 (0DTE): 420 @ 11.38 = **+$478k** BUY | vol 2,847 / OI 0
- **QQQ** PUT 660 2026-11-05 (0DTE): 464 @ 7.00 = **+$325k** BUY | vol 142,315 / OI 2,574
- **QQQ** PUT 655 2026-11-06 (1DTE): 400 @ 7.87 = **+$315k** SELL | vol 21,860 / OI 5,889
- **QQQ** CALL 650 2026-11-05 (0DTE): 420 @ 7.36 = **+$309k** BUY | vol 17,247 / OI 2
- **TSLA** PUT 350 2026-11-11 (6DTE): 166 @ 15.40 = **+$256k** SELL | vol 1,451 / OI 276
- **QQQ** PUT 630 2026-11-09 (4DTE): 803 @ 3.18 = **+$255k** SELL | vol 12,279 / OI 4,873
- **MU** PUT 700 2026-11-09 (4DTE): 60 @ 36.00 = **+$216k** BUY | vol 3,434 / OI 0
- **QQQ** CALL 680 2026-11-12 (7DTE): 400 @ 5.00 = **+$200k** MID | vol 1,741 / OI 163
- **SPY** CALL 740 2026-11-10 (5DTE): 211 @ 9.38 = **+$198k** BUY | vol 11,803 / OI 44
- **SPY** PUT 735 2026-11-06 (1DTE): 500 @ 3.61 = **+$180k** SELL | vol 35,600 / OI 24,589
- **QQQ** CALL 655 2026-11-05 (0DTE): 390 @ 4.50 = **+$176k** BUY | vol 39,050 / OI 2
- **QQQ** PUT 655 2026-11-06 (1DTE): 200 @ 7.87 = **+$157k** SELL | vol 21,860 / OI 5,889
- **QQQ** PUT 655 2026-11-06 (1DTE): 200 @ 7.87 = **+$157k** SELL | vol 21,860 / OI 5,889

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 716 2026-11-09 (4DTE): 506 traded vs OI 51
- **SPY** PUT 734 2026-11-16 (11DTE): 519 traded vs OI 9
- **SPY** PUT 736 2026-11-11 (6DTE): 510 traded vs OI 14
- **SPY** PUT 695 2026-11-13 (8DTE): 7,678 traded vs OI 5,313
- **SPY** CALL 740 2026-11-12 (7DTE): 504 traded vs OI 12
- **SPY** CALL 762 2026-11-13 (8DTE): 1,540 traded vs OI 1,386
- **SPY** CALL 749 2026-11-12 (7DTE): 500 traded vs OI 0
- **SPY** CALL 750 2026-11-17 (12DTE): 509 traded vs OI 21
- **SPY** PUT 725 2026-11-19 (14DTE): 518 traded vs OI 0
- **QQQ** CALL 696 2026-11-09 (4DTE): 506 traded vs OI 89
- **QQQ** PUT 651 2026-11-12 (7DTE): 514 traded vs OI 10
- **QQQ** CALL 662 2026-11-12 (7DTE): 501 traded vs OI 0
- **QQQ** CALL 715 2026-11-16 (11DTE): 6,932 traded vs OI 6,915
- **IWM** CALL 273 2026-11-06 (1DTE): 587 traded vs OI 500
- **IWM** CALL 272 2026-11-05 (0DTE): 550 traded vs OI 30

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
