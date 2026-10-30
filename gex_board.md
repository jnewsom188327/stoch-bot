# GEX + FLOW SCAN - Fri Oct 30, 01:10 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (3)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:25 | **COIN** | **PUTS** | FLOW SURGE | 10/30 138P | 0.73 | 0.44 | +25% (7m) | **-40%** (done) | +115% | 137.27 |
| 10:25 | **SMCI** | **PUTS** | FLIP CROSS down into negative gamma | 10/30 32.5P | 0.43 | 0.31 | -12% (1m) | **-28%** (done) | +32% | 32 |
| 10:15 | **AAPL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 10/30 347.5C | 0.50 | 1.24 | +356% (38m) | **+148%** (done) | +104% | 347.56 hit |

## 1m RULES on SPY / QQQ - loose (4 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 13:10:08 ET, last candle SPY 13:09, QQQ 13:09 | no errors
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
| 1 | **DELL** | 416.27 | FLOW SURGE | **CALLS** | 50 | none: 68 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (57 contracts' greeks worked out here) | NEG -$44.3M | - | 440 | 425 | +$4.5M | +$128k bull / +$0 bear | SHORT (clean 33, ADX 56, RVol 1.5) |
| 2 | **SHOP** | 155.63 | FLOW SURGE | **CALLS** | 49 | none: 36 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (33 contracts' greeks worked out here) | NEG -$15.5M | - | 150 | 157.5 | +$703k | +$233k bull / +$0 bear | out (clean 26, ADX 43, RVol 1.5) |
| 3 | **UBER** | 64.92 | FLOW SURGE | **CALLS** | 38 | none: 26 calls 0-7DTE > 1 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only -12% at the target (needs +20%) (20 contracts' greeks worked out here) | NEG -$37.0M | 65.92 | 65 | 65 | +$384k | +$53k bull / +$0 bear | out (clean 28, ADX 15, RVol 0.8) |
| 4 | **AMD** | 499.24 | - | **-** | 30 | - | NEG -$164.9M | 516.66 | 540 | 500 | +$33.3M | +$4.2M bull / -$110k bear | out (clean 30, ADX 50, RVol 1.1) |
| 5 | **NVDA** | 203.34 | - | **-** | 29 | - | NEG -$430.3M | 211.48 | 210 | 205 | +$31.7M | +$1.7M bull / -$976k bear | out (clean 27, ADX 46, RVol 0.9) |
| 6 | **SMCI** | 31.81 | - | **-** | 29 | - | NEG -$5.2M | 32.99 | 32 | 32 | +$717k | +$76k bull / +$0 bear | out (clean 30, ADX 50, RVol 1.1) |
| 7 | **SMH** | 517.78 | - | **-** | 27 | - | NEG -$575.0M | - | 532.5 | 505 | +$7.8M | +$568k bull / -$25k bear | out (clean 30, ADX 53, RVol 1.1) |
| 8 | **QQQ** | 689.36 | - | **-** | 25 | - | NEG -$10.0B | 730.24 | 720 | 690 | +$88.8M | +$9.9M bull / -$1.4M bear | out (clean 28, ADX 46, RVol 2.1) |
| 9 | **IWM** | 278.30 | - | **-** | 25 | - | NEG -$1.3B | 281.13 | 278 | 278 | +$10.8M | +$149k bull / +$0 bear | out (clean 28, ADX 44, RVol 0.6) |
| 10 | **SPY** | 755.27 | - | **-** | 24 | - | NEG -$13.7B | 766.55 | 800 | 750 | +$121.6M | +$4.2M bull / +$0 bear | out (clean 27, ADX 41, RVol 1.3) |
| 11 | **AVGO** | 323.22 | - | **-** | 23 | - | NEG -$148.9M | - | 340 | 320 | +$1.6M | +$0 bull / -$188k bear | out (clean 30, ADX 50, RVol 1.1) |
| 12 | **MU** | 876.84 | - | **-** | 23 | - | NEG -$253.5M | 908.13 | 880 | 880 | +$53.4M | +$3.1M bull / -$1.6M bear | out (clean 30, ADX 35, RVol 0.7) |
| 13 | **MSTR** | 130.01 | - | **-** | 23 | - | NEG -$23.5M | 136.75 | 135 | 130 | -$7.0M | +$358k bull / +$0 bear | out (clean 28, ADX 16, RVol 2.2) |
| 14 | **HOOD** | 83.09 | - | **-** | 23 | - | NEG -$34.4M | - | 85 | 85 | +$1.5M | +$480k bull / +$0 bear | out (clean 31, ADX 47, RVol 0.5) |
| 15 | **BABA** | 98.45 | - | **-** | 23 | - | NEG -$36.9M | 99.52 | 100 | 98 | +$482k | +$351k bull / +$0 bear | out (clean 29, ADX 11, RVol 0.7) |
| 16 | **NFLX** | 62.24 | - | **-** | 21 | - | NEG -$21.4M | 62.87 | 62 | 62 | +$1.2M | +$69k bull / +$0 bear | out (clean 31, ADX 12, RVol 0.6) |
| 17 | **COIN** | 139.01 | - | **-** | 19 | - | NEG -$14.8M | - | 140 | 140 | -$3.4M | - | out (clean 27, ADX 44, RVol 2.9) |
| 18 | **AMZN** | 238.26 | - | **-** | 18 | - | NEG -$177.6M | 244.48 | 250 | 240 | -$4.9M | +$406k bull / -$382k bear | out (clean 31, ADX 15, RVol 1.7) |
| 19 | **MSFT** | 521.52 | - | **-** | 18 | - | POS +$469.1M | 516.5 | 525 | 520 | +$3.4M | +$0 bull / -$618k bear | out (clean 26, ADX 14, RVol 0.4) |
| 20 | **PLTR** | 184.87 | - | **-** | 18 | - | NEG -$77.8M | 192.72 | 185 | 185 | +$1.9M | +$189k bull / -$198k bear | out (clean 25, ADX 27, RVol 1.0) |
| 21 | **AAPL** | 346.70 | - | **-** | 17 | - | POS +$531.3M | 342.26 | 350 | 345 | -$2.5M | +$748k bull / +$0 bear | out (clean 31, ADX 14, RVol 1.4) |
| 22 | **GOOGL** | 279.12 | - | **-** | 17 | - | NEG -$230.5M | - | 280 | 280 | -$295k | +$44k bull / +$0 bear | out (clean 32, ADX 28, RVol 0.7) |
| 23 | **ARM** | 202.66 | - | **-** | 17 | - | NEG -$20.7M | - | 220 | 205 | +$697k | - | out (clean 26, ADX 37, RVol 1.6) |
| 24 | **ORCL** | 130.84 | - | **-** | 15 | - | POS +$30.7M | 129.42 | 130 | 130 | +$2.6M | - | out (clean 33, ADX 34, RVol 0.6) |
| 25 | **TSLA** | 398.98 | - | **-** | 14 | - | POS +$450.1M | 387.37 | 400 | 400 | -$11.6M | +$1.5M bull / +$0 bear | out (clean 28, ADX 11, RVol 0.6) |
| 26 | **META** | 620.04 | - | **-** | 14 | - | NEG -$16.2M | 620.82 | 625 | 625 | -$893k | +$178k bull / -$152k bear | out (clean 28, ADX 18, RVol 0.4) |
| 27 | **CRM** | 229.71 | - | **-** | 11 | - | NEG -$25.9M | 236.73 | 240 | 230 | +$317k | - | out (clean 28, ADX 20, RVol 0.7) |

## Big prints this scan (140)
- **QQQ** PUT 710 2026-10-30 (0DTE): 496 @ 19.68 = **+$976k** SELL | vol 11,260 / OI 27,653
- **QQQ** PUT 710 2026-10-30 (0DTE): 484 @ 20.11 = **+$973k** SELL | vol 11,260 / OI 27,653
- **NVDA** CALL 207.5 2026-11-06 (7DTE): 2,467 @ 2.88 = **+$710k** BUY | vol 7,303 / OI 171
- **MSFT** CALL 530 2026-11-06 (7DTE): 1,000 @ 4.94 = **+$494k** SELL | vol 3,607 / OI 1,409
- **NVDA** CALL 207.5 2026-11-06 (7DTE): 1,644 @ 2.88 = **+$473k** BUY | vol 7,303 / OI 171
- **QQQ** PUT 710 2026-10-30 (0DTE): 226 @ 19.92 = **+$450k** SELL | vol 11,260 / OI 27,653
- **SPY** PUT 770 2026-11-06 (7DTE): 280 @ 15.50 = **+$434k** SELL | vol 2,321 / OI 4,714
- **NVDA** CALL 212.5 2026-11-06 (7DTE): 2,500 @ 1.34 = **+$335k** SELL | vol 27,431 / OI 1,349
- **NVDA** CALL 212.5 2026-11-06 (7DTE): 2,467 @ 1.33 = **+$328k** SELL | vol 27,431 / OI 1,349
- **QQQ** PUT 700 2026-10-30 (0DTE): 306 @ 9.75 = **+$298k** SELL | vol 41,696 / OI 42,068
- **QQQ** PUT 710 2026-10-30 (0DTE): 150 @ 19.50 = **+$292k** SELL | vol 11,260 / OI 27,653
- **QQQ** PUT 700 2026-10-30 (0DTE): 279 @ 9.74 = **+$272k** SELL | vol 41,696 / OI 42,068
- **QQQ** PUT 710 2026-10-30 (0DTE): 129 @ 19.92 = **+$257k** SELL | vol 11,260 / OI 27,653
- **QQQ** PUT 700 2026-11-05 (6DTE): 168 @ 15.15 = **+$255k** SELL | vol 1,656 / OI 910
- **MU** CALL 880 2026-11-02 (3DTE): 163 @ 15.45 = **+$252k** BUY | vol 2,089 / OI 316

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 739 2026-11-03 (4DTE): 504 traded vs OI 293
- **SPY** CALL 755 2026-11-04 (5DTE): 651 traded vs OI 30
- **SPY** PUT 746 2026-11-03 (4DTE): 929 traded vs OI 914
- **SPY** PUT 680 2026-11-02 (3DTE): 538 traded vs OI 0
- **SPY** CALL 755 2026-11-03 (4DTE): 549 traded vs OI 85
- **SPY** PUT 730 2026-11-09 (10DTE): 1,273 traded vs OI 822
- **QQQ** CALL 690 2026-11-04 (5DTE): 507 traded vs OI 30
- **QQQ** PUT 660 2026-11-06 (7DTE): 6,806 traded vs OI 6,548
- **QQQ** PUT 660 2026-11-05 (6DTE): 661 traded vs OI 660
- **QQQ** PUT 674 2026-11-04 (5DTE): 522 traded vs OI 0
- **QQQ** PUT 640 2026-11-04 (5DTE): 914 traded vs OI 909
- **QQQ** CALL 717 2026-11-04 (5DTE): 534 traded vs OI 73
- **QQQ** PUT 684 2026-11-04 (5DTE): 503 traded vs OI 0
- **QQQ** PUT 670 2026-11-03 (4DTE): 1,761 traded vs OI 1,531
- **QQQ** CALL 721 2026-11-02 (3DTE): 645 traded vs OI 386

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
