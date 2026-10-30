# GEX + FLOW SCAN - Fri Oct 30, 01:30 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (3)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:25 | **COIN** | **PUTS** | FLOW SURGE | 10/30 138P | 0.73 | 0.44 | +25% (7m) | **-40%** (done) | +115% | 137.27 |
| 10:25 | **SMCI** | **PUTS** | FLIP CROSS down into negative gamma | 10/30 32.5P | 0.43 | 0.31 | -12% (1m) | **-28%** (done) | +32% | 32 |
| 10:15 | **AAPL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 10/30 347.5C | 0.50 | 1.24 | +356% (38m) | **+148%** (done) | +104% | 347.56 hit |

## 1m RULES on SPY / QQQ - loose (4 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 13:30:08 ET, last candle SPY 13:29, QQQ 13:29 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 12:45 | QQQ | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |
| 12:32 | SPY | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |
| 12:31 | SPY | 1m FAILED POP | R3 R4 | PUTS | TURNING your way | no contract: 45 puts 0-1DTE > 1 priced 0.40-0.80 > 1 delta 0.15+ > 1 spread ok > 1 liquid  |
| 11:05 | SPY | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |

## Flow surges NOT fired - price disagreed (40 today, last 5)
- 12:40 NVDA CALLS: under EMA 20 - flow says one way, price says the other
- 11:20 ARM CALLS: under EMA 20 - flow says one way, price says the other
- 11:20 COIN PUTS: price +0.22 over the last 15 min - flow says one way, price says the other
- 11:15 MSTR PUTS: price +1.54 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 11:10 MSTR PUTS: price +1.77 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **DELL** | 415.64 | FLOW SURGE | **CALLS** | 51 | none: 66 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (56 contracts' greeks worked out here) | NEG -$49.1M | - | 440 | 425 | +$5.1M | +$138k bull / +$0 bear | SHORT (clean 34, ADX 60, RVol 1.6) |
| 2 | **AMD** | 499.92 | - | **-** | 28 | - | NEG -$176.5M | 519.56 | 500 | 500 | +$32.5M | +$1.6M bull / -$677k bear | out (clean 30, ADX 52, RVol 1.0) |
| 3 | **NVDA** | 203.40 | - | **-** | 27 | - | NEG -$410.0M | 211.17 | 210 | 205 | +$30.8M | +$2.3M bull / -$2.7M bear | out (clean 27, ADX 48, RVol 0.8) |
| 4 | **SMH** | 518.99 | - | **-** | 26 | - | NEG -$668.5M | - | 532.5 | 530 | +$7.3M | +$309k bull / -$586k bear | out (clean 30, ADX 54, RVol 1.1) |
| 5 | **SHOP** | 155.00 | - | **-** | 26 | - | NEG -$12.8M | - | 150 | 157.5 | +$741k | - | out (clean 26, ADX 44, RVol 3.4) |
| 6 | **IWM** | 278.44 | - | **-** | 25 | - | NEG -$1.2B | 281.17 | 278 | 278 | +$10.8M | +$773k bull / +$0 bear | out (clean 28, ADX 44, RVol 0.9) |
| 7 | **SPY** | 755.59 | - | **-** | 24 | - | NEG -$15.7B | 771.85 | 800 | 750 | +$158.3M | +$1.8M bull / -$14.9M bear | out (clean 27, ADX 43, RVol 0.9) |
| 8 | **QQQ** | 689.52 | - | **-** | 24 | - | NEG -$10.5B | - | 720 | 690 | +$79.4M | +$1.9M bull / -$1.2M bear | out (clean 28, ADX 47, RVol 1.9) |
| 9 | **MU** | 875.77 | - | **-** | 24 | - | NEG -$306.5M | - | 880 | 880 | +$62.0M | +$7.4M bull / -$27k bear | out (clean 30, ADX 37, RVol 0.7) |
| 10 | **NFLX** | 62.00 | - | **-** | 22 | - | NEG -$30.7M | 63.14 | 62 | 62 | +$1.3M | +$27k bull / +$0 bear | out (clean 30, ADX 17, RVol 0.5) |
| 11 | **AVGO** | 323.93 | - | **-** | 22 | - | NEG -$166.1M | - | 340 | 320 | +$1.4M | +$60k bull / +$0 bear | out (clean 30, ADX 48, RVol 0.9) |
| 12 | **HOOD** | 83.02 | - | **-** | 22 | - | NEG -$35.8M | - | 85 | 85 | +$1.0M | +$84k bull / -$198k bear | out (clean 31, ADX 49, RVol 0.7) |
| 13 | **MSTR** | 129.97 | - | **-** | 20 | - | NEG -$28.5M | - | 135 | 130 | -$4.9M | +$267k bull / +$0 bear | out (clean 28, ADX 22, RVol 1.3) |
| 14 | **COIN** | 138.91 | - | **-** | 19 | - | NEG -$15.2M | - | 140 | 140 | -$3.3M | - | out (clean 27, ADX 46, RVol 3.4) |
| 15 | **AMZN** | 238.62 | - | **-** | 18 | - | NEG -$198.9M | 246.94 | 250 | 240 | -$5.1M | +$148k bull / -$297k bear | out (clean 31, ADX 14, RVol 1.6) |
| 16 | **MSFT** | 521.31 | - | **-** | 18 | - | POS +$430.7M | 517.82 | 525 | 520 | +$3.8M | +$432k bull / +$0 bear | out (clean 26, ADX 15, RVol 0.3) |
| 17 | **GOOGL** | 278.91 | - | **-** | 18 | - | NEG -$237.2M | - | 280 | 280 | +$527k | +$44k bull / +$0 bear | out (clean 32, ADX 34, RVol 0.6) |
| 18 | **SMCI** | 31.76 | - | **-** | 18 | - | NEG -$4.6M | 33.01 | 32 | 32 | +$728k | - | out (clean 30, ADX 52, RVol 0.8) |
| 19 | **AAPL** | 346.56 | - | **-** | 16 | - | POS +$479.7M | 342.25 | 350 | 345 | -$2.1M | +$60k bull / +$0 bear | out (clean 30, ADX 16, RVol 1.1) |
| 20 | **ARM** | 203.59 | - | **-** | 16 | - | NEG -$21.9M | - | 205 | 205 | +$670k | - | out (clean 26, ADX 34, RVol 1.6) |
| 21 | **UBER** | 64.96 | - | **-** | 16 | - | NEG -$41.5M | 66.07 | 65 | 65 | +$380k | - | out (clean 28, ADX 20, RVol 0.4) |
| 22 | **TSLA** | 398.91 | - | **-** | 15 | - | POS +$418.6M | 386.84 | 400 | 400 | -$12.0M | +$1.0M bull / -$1.6M bear | out (clean 28, ADX 12, RVol 0.8) |
| 23 | **META** | 619.72 | - | **-** | 15 | - | NEG -$41.9M | 621.01 | 625 | 625 | -$175k | +$494k bull / -$84k bear | out (clean 28, ADX 20, RVol 0.5) |
| 24 | **ORCL** | 131.00 | - | **-** | 15 | - | POS +$34.7M | 128.94 | 130 | 130 | +$2.7M | - | out (clean 34, ADX 32, RVol 0.5) |
| 25 | **BABA** | 98.37 | - | **-** | 13 | - | NEG -$40.8M | 99.53 | 100 | 98 | +$511k | - | out (clean 28, ADX 14, RVol 0.5) |
| 26 | **CRM** | 229.75 | - | **-** | 11 | - | NEG -$25.6M | 237.45 | 230 | 230 | +$293k | - | out (clean 28, ADX 26, RVol 0.6) |
| 27 | **PLTR** | 185.25 | - | **-** | 8 | - | NEG -$70.2M | 192.91 | 185 | 185 | +$1.3M | - | out (clean 26, ADX 30, RVol 0.7) |

## Big prints this scan (120)
- **NVDA** CALL 212.5 2026-11-06 (7DTE): 12,499 @ 1.35 = **+$1.7M** SELL | vol 43,386 / OI 1,349
- **TSLA** PUT 395 2026-11-06 (7DTE): 999 @ 8.25 = **+$824k** BUY | vol 9,028 / OI 2,235
- **MU** CALL 880 2026-11-06 (7DTE): 180 @ 29.16 = **+$525k** BUY | vol 898 / OI 537
- **SPY** PUT 765 2026-11-06 (7DTE): 275 @ 12.34 = **+$339k** SELL | vol 4,111 / OI 6,242
- **NVDA** CALL 212.5 2026-11-06 (7DTE): 2,500 @ 1.35 = **+$338k** SELL | vol 43,386 / OI 1,349
- **QQQ** PUT 690 2026-11-02 (3DTE): 530 @ 6.24 = **+$331k** BUY | vol 21,663 / OI 2,363
- **SPY** PUT 752 2026-11-06 (7DTE): 500 @ 6.15 = **+$308k** SELL | vol 2,422 / OI 1,360
- **MU** CALL 910 2026-11-06 (7DTE): 180 @ 16.56 = **+$298k** BUY | vol 1,565 / OI 221
- **SPY** PUT 767 2026-11-04 (5DTE): 220 @ 12.82 = **+$282k** MID | vol 17,523 / OI 29,783
- **QQQ** PUT 697 2026-11-04 (5DTE): 200 @ 13.20 = **+$264k** SELL | vol 636 / OI 0
- **QQQ** PUT 685 2026-11-02 (3DTE): 530 @ 4.20 = **+$223k** BUY | vol 13,105 / OI 5,039
- **QQQ** PUT 692 2026-11-04 (5DTE): 200 @ 10.49 = **+$210k** SELL | vol 1,571 / OI 0
- **AMD** PUT 510 2026-11-02 (3DTE): 80 @ 16.73 = **+$134k** BUY | vol 1,672 / OI 164
- **MU** CALL 880 2026-11-06 (7DTE): 45 @ 29.15 = **+$131k** BUY | vol 898 / OI 537
- **MU** PUT 870 2026-11-06 (7DTE): 49 @ 26.75 = **+$131k** SELL | vol 938 / OI 632

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 750 2026-11-06 (7DTE): 525 traded vs OI 308
- **SPY** CALL 775 2026-11-05 (6DTE): 2,025 traded vs OI 1,853
- **SPY** CALL 760 2026-11-12 (13DTE): 507 traded vs OI 0
- **SPY** CALL 777 2026-11-06 (7DTE): 1,261 traded vs OI 1,243
- **QQQ** PUT 665 2026-11-04 (5DTE): 1,005 traded vs OI 917
- **QQQ** CALL 690 2026-11-05 (6DTE): 541 traded vs OI 15
- **QQQ** CALL 707 2026-11-03 (4DTE): 518 traded vs OI 102
- **QQQ** CALL 722 2026-11-03 (4DTE): 549 traded vs OI 368
- **QQQ** PUT 677 2026-11-03 (4DTE): 552 traded vs OI 0
- **QQQ** PUT 671 2026-11-04 (5DTE): 502 traded vs OI 0
- **QQQ** PUT 660 2026-11-11 (12DTE): 545 traded vs OI 73
- **IWM** PUT 275 2026-11-09 (10DTE): 513 traded vs OI 106
- **SMH** PUT 507.5 2026-10-30 (0DTE): 606 traded vs OI 270
- **NVDA** PUT 210 2026-11-02 (3DTE): 2,792 traded vs OI 2,785
- **NVDA** CALL 190 2026-11-13 (14DTE): 663 traded vs OI 627

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
