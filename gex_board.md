# GEX + FLOW SCAN - Fri Oct 30, 12:50 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (3)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:25 | **COIN** | **PUTS** | FLOW SURGE | 10/30 138P | 0.73 | 0.44 | +25% (7m) | **-40%** (done) | +115% | 137.27 |
| 10:25 | **SMCI** | **PUTS** | FLIP CROSS down into negative gamma | 10/30 32.5P | 0.43 | 0.31 | -12% (1m) | **-28%** (done) | +32% | 32 |
| 10:15 | **AAPL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 10/30 347.5C | 0.50 | 1.24 | +356% (38m) | **+148%** (done) | +104% | 347.56 hit |

## 1m RULES on SPY / QQQ - loose (4 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 12:50:08 ET, last candle SPY 12:49, QQQ 12:49 | no errors
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
| 1 | **NVDA** | 203.75 | FLOW SURGE | **CALLS** | 46 | none: 64 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (27 contracts' greeks worked out here) | NEG -$441.8M | 212.06 | 210 | 205 | +$30.7M | +$1.8M bull / -$90k bear | out (clean 27, ADX 44, RVol 1.4) |
| 2 | **AMD** | 501.17 | - | **-** | 33 | - | NEG -$164.1M | 518.91 | 550 | 500 | +$30.1M | +$2.7M bull / -$413k bear | out (clean 29, ADX 47, RVol 2.8) |
| 3 | **SHOP** | 155.97 | - | **-** | 31 | - | NEG -$16.3M | - | 150 | 157.5 | +$282k | +$0 bull / -$149k bear | out (clean 27, ADX 46, RVol 2.1) |
| 4 | **DELL** | 419.75 | - | **-** | 30 | - | NEG -$54.4M | - | 440 | 425 | +$3.7M | +$366k bull / +$0 bear | out (clean 33, ADX 52, RVol 1.3) |
| 5 | **COIN** | 139.92 | - | **-** | 29 | - | NEG -$15.8M | - | 140 | 140 | -$3.5M | +$67k bull / -$144k bear | out (clean 27, ADX 43, RVol 2.9) |
| 6 | **TSLA** | 399.68 | PINNED between the walls (positive gamma) - chop | **-** | 28 | - | POS +$421.9M | 391.03 | 400 | 400 | -$13.2M | +$374k bull / -$908k bear | out (clean 28, ADX 12, RVol 0.6) |
| 7 | **ARM** | 203.08 | - | **-** | 28 | - | NEG -$19.8M | - | 220 | 205 | +$509k | +$0 bull / -$45k bear | out (clean 26, ADX 38, RVol 2.4) |
| 8 | **SMH** | 519.65 | - | **-** | 27 | - | NEG -$591.8M | - | 532.5 | 530 | +$6.5M | +$0 bull / -$84k bear | out (clean 30, ADX 52, RVol 1.3) |
| 9 | **MSTR** | 133.28 | - | **-** | 25 | - | NEG -$23.4M | - | 135 | 135 | -$9.2M | +$2.1M bull / -$311k bear | out (clean 28, ADX 15, RVol 2.0) |
| 10 | **IWM** | 278.64 | - | **-** | 24 | - | NEG -$1.2B | 281.07 | 278 | 278 | +$10.0M | +$121k bull / +$0 bear | out (clean 28, ADX 39, RVol 0.4) |
| 11 | **AVGO** | 323.40 | - | **-** | 24 | - | NEG -$148.1M | - | 340 | 320 | +$1.8M | +$59k bull / -$40k bear | out (clean 30, ADX 49, RVol 1.1) |
| 12 | **MU** | 878.28 | - | **-** | 24 | - | NEG -$279.0M | 915.13 | 880 | 880 | +$55.2M | +$495k bull / -$1.2M bear | out (clean 30, ADX 34, RVol 0.5) |
| 13 | **SPY** | 756.29 | - | **-** | 23 | - | NEG -$15.2B | 771.94 | 760 | 750 | +$112.6M | +$1.4M bull / -$2.7M bear | out (clean 27, ADX 39, RVol 0.8) |
| 14 | **QQQ** | 690.60 | - | **-** | 23 | - | NEG -$10.3B | 728.8 | 720 | 690 | +$65.5M | +$1.7M bull / -$2.1M bear | out (clean 28, ADX 44, RVol 1.4) |
| 15 | **NFLX** | 62.44 | - | **-** | 21 | - | NEG -$23.1M | 63.11 | 63 | 62 | +$1.1M | +$0 bull / -$80k bear | out (clean 31, ADX 13, RVol 0.8) |
| 16 | **AAPL** | 347.60 | - | **-** | 19 | - | POS +$645.2M | 342.93 | 350 | 345 | -$5.8M | +$1.3M bull / -$1.5M bear | out (clean 31, ADX 15, RVol 1.6) |
| 17 | **AMZN** | 238.81 | - | **-** | 19 | - | NEG -$183.2M | 247.69 | 250 | 240 | -$5.0M | +$53k bull / -$264k bear | out (clean 31, ADX 15, RVol 2.0) |
| 18 | **SMCI** | 31.91 | - | **-** | 19 | - | NEG -$2.3M | 32.44 | 35 | 32 | +$650k | - | out (clean 30, ADX 47, RVol 0.8) |
| 19 | **MSFT** | 521.58 | - | **-** | 18 | - | POS +$507.7M | 516.31 | 525 | 525 | +$2.9M | +$793k bull / -$61k bear | out (clean 26, ADX 16, RVol 0.6) |
| 20 | **PLTR** | 185.76 | - | **-** | 18 | - | NEG -$77.6M | 193 | 185 | 185 | +$1.5M | +$166k bull / +$0 bear | out (clean 25, ADX 24, RVol 1.2) |
| 21 | **GOOGL** | 279.54 | - | **-** | 16 | - | NEG -$244.4M | - | 280 | 280 | -$991k | +$300k bull / -$39k bear | out (clean 32, ADX 21, RVol 0.6) |
| 22 | **ORCL** | 130.98 | - | **-** | 16 | - | POS +$38.1M | 129.15 | 130 | 130 | +$2.7M | - | out (clean 33, ADX 34, RVol 0.9) |
| 23 | **META** | 620.10 | - | **-** | 14 | - | NEG -$32.7M | 621.18 | 625 | 625 | -$1.2M | +$0 bull / -$222k bear | out (clean 28, ADX 15, RVol 0.5) |
| 24 | **HOOD** | 83.56 | - | **-** | 12 | - | NEG -$39.6M | - | 85 | 85 | +$725k | - | out (clean 31, ADX 46, RVol 0.6) |
| 25 | **UBER** | 65.21 | - | **-** | 7 | - | NEG -$34.3M | 66.43 | 65 | 65 | +$65k | - | out (clean 28, ADX 9, RVol 0.8) |
| 26 | **BABA** | 98.58 | - | **-** | 6 | - | NEG -$33.1M | 99.58 | 100 | 99 | +$73k | - | out (clean 29, ADX 12, RVol 1.0) |
| 27 | **CRM** | 230.60 | - | **-** | 4 | - | NEG -$21.7M | 237.72 | 230 | 230 | -$22k | - | out (clean 27, ADX 13, RVol 0.7) |

## Big prints this scan (72)
- **MSTR** CALL 139 2026-11-06 (7DTE): 5,000 @ 4.17 = **+$2.1M** BUY | vol 15,771 / OI 85
- **AMD** PUT 515 2026-10-30 (0DTE): 167 @ 12.50 = **+$209k** SELL | vol 3,478 / OI 822
- **AAPL** PUT 340 2026-11-04 (5DTE): 416 @ 4.95 = **+$206k** BUY | vol 6,039 / OI 1,656
- **MSFT** CALL 500 2026-10-30 (0DTE): 78 @ 23.27 = **+$182k** BUY | vol 677 / OI 1,225
- **QQQ** PUT 700 2026-11-03 (4DTE): 160 @ 11.16 = **+$179k** SELL | vol 968 / OI 1,263
- **QQQ** PUT 695 2026-10-30 (0DTE): 500 @ 3.37 = **+$168k** SELL | vol 168,721 / OI 18,389
- **NVDA** PUT 212.5 2026-10-30 (0DTE): 200 @ 7.85 = **+$157k** SELL | vol 5,495 / OI 8,436
- **NVDA** PUT 212.5 2026-10-30 (0DTE): 190 @ 7.85 = **+$149k** SELL | vol 5,495 / OI 8,436
- **MU** CALL 885 2026-10-30 (0DTE): 300 @ 4.60 = **+$138k** BUY | vol 9,769 / OI 369
- **QQQ** CALL 700 2026-11-03 (4DTE): 381 @ 3.59 = **+$137k** BUY | vol 6,428 / OI 38
- **QQQ** CALL 702 2026-11-03 (4DTE): 381 @ 2.91 = **+$111k** BUY | vol 1,910 / OI 14
- **QQQ** PUT 700 2026-11-03 (4DTE): 99 @ 11.16 = **+$110k** SELL | vol 968 / OI 1,263
- **NVDA** CALL 195 2026-11-06 (7DTE): 100 @ 11.00 = **+$110k** BUY | vol 1,433 / OI 88
- **QQQ** PUT 700 2026-11-03 (4DTE): 98 @ 11.16 = **+$109k** SELL | vol 968 / OI 1,263
- **QQQ** PUT 700 2026-11-05 (6DTE): 80 @ 13.54 = **+$108k** SELL | vol 1,143 / OI 910

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 700 2026-11-03 (4DTE): 502 traded vs OI 102
- **SPY** PUT 737 2026-11-04 (5DTE): 506 traded vs OI 119
- **SPY** PUT 702 2026-11-20 (21DTE): 1,779 traded vs OI 968
- **QQQ** PUT 677 2026-11-04 (5DTE): 518 traded vs OI 0
- **IWM** CALL 292 2026-11-02 (3DTE): 599 traded vs OI 586
- **NVDA** PUT 185 2026-11-02 (3DTE): 1,193 traded vs OI 0
- **TSLA** CALL 425 2026-11-06 (7DTE): 2,702 traded vs OI 2,628
- **AAPL** CALL 340 2026-11-04 (5DTE): 504 traded vs OI 217
- **AAPL** PUT 337.5 2026-11-06 (7DTE): 754 traded vs OI 579
- **AAPL** PUT 322.5 2026-11-13 (14DTE): 571 traded vs OI 4
- **AMD** PUT 470 2026-11-02 (3DTE): 503 traded vs OI 73
- **AMD** CALL 500 2026-11-02 (3DTE): 528 traded vs OI 28
- **AMD** PUT 502.5 2026-11-02 (3DTE): 505 traded vs OI 90
- **AMZN** CALL 237.5 2026-11-04 (5DTE): 501 traded vs OI 1
- **MSFT** CALL 535 2026-11-04 (5DTE): 503 traded vs OI 99

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
