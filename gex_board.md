# GEX + FLOW SCAN - Fri Oct 30, 11:50 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (3)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:25 | **COIN** | **PUTS** | FLOW SURGE | 10/30 138P | 0.73 | 0.67 | +25% (7m) | **-8%** | +115% | 137.27 |
| 10:25 | **SMCI** | **PUTS** | FLIP CROSS down into negative gamma | 10/30 32.5P | 0.43 | 0.31 | -12% (1m) | **-28%** (done) | +32% | 32 |
| 10:15 | **AAPL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 10/30 347.5C | 0.50 | 1.24 | +356% (38m) | **+148%** (done) | +104% | 347.56 hit |

## 1m RULES on SPY / QQQ - loose (1 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 11:50:08 ET, last candle SPY 11:49, QQQ 11:49 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 11:05 | SPY | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |

## Flow surges NOT fired - price disagreed (40 today, last 5)
- 11:20 ARM CALLS: under EMA 20 - flow says one way, price says the other
- 11:20 COIN PUTS: price +0.22 over the last 15 min - flow says one way, price says the other
- 11:15 MSTR PUTS: price +1.54 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 11:10 MSTR PUTS: price +1.77 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:55 AAPL PUTS: price +1.23 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **ARM** | 204.16 | FLOW SURGE | **CALLS** | 60 | none: 32 calls 0-7DTE > 1 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only -18% at the target (needs +20%) (27 contracts' greeks worked out here) | NEG -$20.6M | - | 220 | 205 | +$695k | +$32k bull / +$0 bear | out (clean 26, ADX 47, RVol 3.1) |
| 2 | **ORCL** | 131.36 | FLOW SURGE | **CALLS** | 38 | 10/30 132C @ 0.65 (delta 0.39) = est +92% at 132.93 | POS +$37.2M | 129.32 | 130 | 130 | +$3.0M | +$38k bull / +$0 bear | out (clean 33, ADX 47, RVol 0.4) |
| 3 | **TSLA** | 400.32 | PINNED between the walls (positive gamma) - chop | **-** | 30 | - | POS +$434.9M | 391.1 | 400 | 400 | -$8.6M | +$1.9M bull / +$0 bear | out (clean 29, ADX 18, RVol 0.8) |
| 4 | **COIN** | 140.20 | - | **-** | 30 | - | NEG -$14.5M | - | 150 | 140 | -$3.4M | +$0 bull / -$80k bear | out (clean 27, ADX 50, RVol 3.5) |
| 5 | **NVDA** | 205.84 | - | **-** | 29 | - | NEG -$423.3M | 211.47 | 210 | 205 | +$17.9M | +$687k bull / +$0 bear | out (clean 26, ADX 40, RVol 1.1) |
| 6 | **DELL** | 426.91 | - | **-** | 29 | - | NEG -$60.8M | - | 440 | 425 | +$1.7M | +$35k bull / +$0 bear | out (clean 32, ADX 48, RVol 4.1) |
| 7 | **SMH** | 524.87 | - | **-** | 27 | - | NEG -$604.7M | - | 532.5 | 530 | +$5.4M | +$27k bull / +$0 bear | out (clean 28, ADX 48, RVol 0.9) |
| 8 | **AMD** | 511.71 | - | **-** | 27 | - | NEG -$119.6M | 522.87 | 517.5 | 500 | +$16.6M | +$843k bull / +$0 bear | out (clean 28, ADX 37, RVol 1.2) |
| 9 | **MU** | 887.05 | - | **-** | 27 | - | NEG -$255.9M | 929.89 | 900 | 900 | +$52.6M | +$5.6M bull / -$185k bear | out (clean 29, ADX 34, RVol 0.8) |
| 10 | **MSTR** | 132.27 | - | **-** | 25 | - | NEG -$23.5M | - | 135 | 130 | -$5.6M | +$365k bull / -$38k bear | out (clean 28, ADX 23, RVol 1.9) |
| 11 | **SPY** | 757.61 | - | **-** | 24 | - | NEG -$14.2B | 772.13 | 760 | 750 | +$102.7M | +$3.1M bull / +$0 bear | out (clean 26, ADX 41, RVol 0.9) |
| 12 | **AVGO** | 326.33 | - | **-** | 24 | - | NEG -$145.8M | - | 330 | 330 | +$1.6M | +$194k bull / +$0 bear | out (clean 29, ADX 52, RVol 0.7) |
| 13 | **HOOD** | 83.89 | - | **-** | 24 | - | NEG -$40.0M | - | 85 | 85 | +$1.1M | +$432k bull / +$0 bear | out (clean 31, ADX 52, RVol 0.6) |
| 14 | **QQQ** | 693.62 | - | **-** | 23 | - | NEG -$10.2B | 727.56 | 720 | 690 | +$51.7M | +$4.9M bull / +$0 bear | out (clean 27, ADX 44, RVol 1.4) |
| 15 | **NFLX** | 62.39 | - | **-** | 23 | - | NEG -$23.1M | 63.37 | 63 | 62 | +$1.1M | +$0 bull / -$26k bear | out (clean 32, ADX 19, RVol 0.6) |
| 16 | **GOOGL** | 282.08 | - | **-** | 22 | - | NEG -$257.2M | - | 280 | 280 | -$4.7M | +$309k bull / -$65k bear | out (clean 32, ADX 18, RVol 0.7) |
| 17 | **AMZN** | 239.07 | - | **-** | 20 | - | NEG -$163.7M | 246.65 | 250 | 240 | -$5.5M | +$509k bull / +$0 bear | out (clean 31, ADX 15, RVol 1.9) |
| 18 | **PLTR** | 186.18 | - | **-** | 20 | - | NEG -$60.2M | 192.42 | 185 | 185 | -$827k | +$203k bull / +$0 bear | out (clean 25, ADX 37, RVol 1.0) |
| 19 | **SMCI** | 32.31 | - | **-** | 20 | - | NEG -$1.4M | 32.52 | 35 | 32 | +$627k | - | out (clean 29, ADX 43, RVol 0.8) |
| 20 | **SHOP** | 156.06 | - | **-** | 20 | - | NEG -$15.2M | - | 150 | 157.5 | +$244k | - | out (clean 26, ADX 52, RVol 1.6) |
| 21 | **AAPL** | 347.26 | - | **-** | 19 | - | POS +$651.4M | 342.87 | 350 | 345 | -$3.1M | +$350k bull / +$0 bear | out (clean 31, ADX 22, RVol 1.3) |
| 22 | **MSFT** | 521.83 | - | **-** | 19 | - | POS +$471.2M | 515.97 | 525 | 525 | +$2.0M | +$106k bull / +$0 bear | out (clean 26, ADX 25, RVol 0.5) |
| 23 | **IWM** | 279.24 | - | **-** | 16 | - | NEG -$920.7M | 281.16 | 278 | 278 | +$9.5M | - | out (clean 27, ADX 38, RVol 0.7) |
| 24 | **META** | 622.71 | - | **-** | 16 | - | POS +$22.8M | 621.9 | 625 | 625 | -$3.9M | +$165k bull / -$152k bear | out (clean 28, ADX 14, RVol 0.6) |
| 25 | **CRM** | 231.61 | - | **-** | 4 | - | NEG -$24.6M | 239.85 | 240 | 230 | +$5k | - | out (clean 27, ADX 12, RVol 0.7) |
| 26 | **BABA** | 98.75 | - | **-** | 4 | - | NEG -$34.9M | 100.24 | 100 | 99 | +$8k | - | out (clean 29, ADX 13, RVol 0.7) |
| 27 | **UBER** | 65.15 | - | **-** | 3 | - | NEG -$37.4M | 66.1 | 70 | 65 | -$5k | - | out (clean 28, ADX 9, RVol 0.2) |

## Big prints this scan (104)
- **MU** PUT 925 2026-11-04 (5DTE): 150 @ 46.11 = **+$692k** SELL | vol 398 / OI 125
- **MU** PUT 925 2026-10-30 (0DTE): 150 @ 37.98 = **+$570k** SELL | vol 963 / OI 1,189
- **QQQ** PUT 714 2026-10-30 (0DTE): 282 @ 19.51 = **+$550k** SELL | vol 1,085 / OI 6,113
- **HOOD** CALL 86 2026-11-06 (7DTE): 1,998 @ 2.16 = **+$432k** BUY | vol 8,324 / OI 1,507
- **QQQ** CALL 724 2026-11-06 (7DTE): 3,500 @ 1.18 = **+$413k** BUY | vol 4,475 / OI 660
- **QQQ** CALL 725 2026-11-06 (7DTE): 3,500 @ 1.06 = **+$371k** BUY | vol 5,508 / OI 6,645
- **SPY** PUT 767 2026-11-04 (5DTE): 250 @ 10.20 = **+$255k** SELL | vol 11,479 / OI 29,783
- **SPY** PUT 755 2026-11-05 (6DTE): 500 @ 4.78 = **+$239k** SELL | vol 1,130 / OI 453
- **QQQ** PUT 695 2026-10-30 (0DTE): 980 @ 2.31 = **+$226k** SELL | vol 151,777 / OI 18,389
- **QQQ** PUT 695 2026-10-30 (0DTE): 937 @ 2.36 = **+$221k** SELL | vol 151,777 / OI 18,389
- **QQQ** PUT 690 2026-11-02 (3DTE): 594 @ 3.25 = **+$193k** SELL | vol 11,842 / OI 2,363
- **MU** CALL 870 2026-10-30 (0DTE): 100 @ 17.04 = **+$170k** BUY | vol 1,050 / OI 331
- **SPY** PUT 750 2026-11-05 (6DTE): 500 @ 3.33 = **+$166k** SELL | vol 1,010 / OI 800
- **QQQ** PUT 696 2026-10-30 (0DTE): 500 @ 2.80 = **+$140k** SELL | vol 95,177 / OI 13,896
- **TSLA** PUT 395 2026-11-06 (7DTE): 199 @ 6.85 = **+$136k** SELL | vol 5,732 / OI 2,235

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 750 2026-11-05 (6DTE): 1,010 traded vs OI 800
- **SPY** CALL 780 2026-11-02 (3DTE): 1,582 traded vs OI 1,564
- **SPY** PUT 695 2026-11-03 (4DTE): 608 traded vs OI 416
- **QQQ** CALL 719 2026-11-03 (4DTE): 500 traded vs OI 71
- **QQQ** PUT 646 2026-10-30 (0DTE): 1,524 traded vs OI 1,295
- **QQQ** CALL 712 2026-11-04 (5DTE): 629 traded vs OI 126
- **IWM** PUT 266 2026-11-20 (21DTE): 32,100 traded vs OI 25,937
- **AMZN** PUT 235 2026-11-04 (5DTE): 510 traded vs OI 35
- **MSFT** PUT 505 2026-11-06 (7DTE): 642 traded vs OI 640
- **GOOGL** CALL 310 2026-11-06 (7DTE): 500 traded vs OI 0
- **GOOGL** CALL 290 2026-11-04 (5DTE): 720 traded vs OI 3
- **GOOGL** CALL 310 2026-10-30 (0DTE): 500 traded vs OI 0
- **COIN** CALL 146 2026-10-30 (0DTE): 507 traded vs OI 3
- **DELL** CALL 432.5 2026-10-30 (0DTE): 509 traded vs OI 11
- **MU** CALL 890 2026-11-06 (7DTE): 517 traded vs OI 238

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
