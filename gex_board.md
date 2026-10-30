# GEX + FLOW SCAN - Fri Oct 30, 12:30 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (3)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:25 | **COIN** | **PUTS** | FLOW SURGE | 10/30 138P | 0.73 | 0.44 | +25% (7m) | **-40%** (done) | +115% | 137.27 |
| 10:25 | **SMCI** | **PUTS** | FLIP CROSS down into negative gamma | 10/30 32.5P | 0.43 | 0.31 | -12% (1m) | **-28%** (done) | +32% | 32 |
| 10:15 | **AAPL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 10/30 347.5C | 0.50 | 1.24 | +356% (38m) | **+148%** (done) | +104% | 347.56 hit |

## 1m RULES on SPY / QQQ - loose (1 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 12:30:08 ET, last candle SPY 12:29, QQQ 12:29 | no errors
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
| 1 | **AMD** | 502.78 | FLOW SURGE | **CALLS** | 55 | none: 164 calls 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (72 contracts' greeks worked out here) | NEG -$168.3M | 521.81 | 517.5 | 500 | +$27.0M | +$3.2M bull / +$0 bear | out (clean 29, ADX 43, RVol 2.8) |
| 2 | **NVDA** | 204.68 | FLOW SURGE | **CALLS** | 47 | none: 68 calls 0-7DTE > 5 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only -13% at the target (needs +20%) (31 contracts' greeks worked out here) | NEG -$428.3M | 211.69 | 210 | 205 | +$26.2M | +$827k bull / +$0 bear | out (clean 26, ADX 42, RVol 1.6) |
| 3 | **ARM** | 204.16 | - | **-** | 31 | - | NEG -$20.5M | - | 220 | 205 | +$621k | +$0 bull / -$33k bear | out (clean 26, ADX 42, RVol 2.1) |
| 4 | **SMH** | 522.50 | - | **-** | 30 | - | NEG -$616.0M | - | 532.5 | 530 | +$6.8M | +$172k bull / -$74k bear | out (clean 29, ADX 52, RVol 2.2) |
| 5 | **TSLA** | 400.17 | PINNED between the walls (positive gamma) - chop | **-** | 28 | - | POS +$375.6M | 391.95 | 400 | 400 | -$11.1M | +$477k bull / -$450k bear | out (clean 28, ADX 12, RVol 0.7) |
| 6 | **ORCL** | 131.90 | - | **-** | 27 | - | POS +$46.8M | 130.4 | 130 | 130 | +$2.3M | +$98k bull / -$26k bear | out (clean 33, ADX 37, RVol 1.0) |
| 7 | **MU** | 883.82 | - | **-** | 25 | - | NEG -$279.2M | 935.97 | 900 | 900 | +$58.8M | +$1.7M bull / -$2.6M bear | out (clean 30, ADX 36, RVol 0.5) |
| 8 | **MSTR** | 133.40 | - | **-** | 25 | - | NEG -$20.9M | - | 135 | 135 | -$9.2M | +$0 bull / -$5.0M bear | out (clean 28, ADX 14, RVol 1.7) |
| 9 | **SPY** | 757.67 | - | **-** | 24 | - | NEG -$14.7B | 771.81 | 760 | 750 | +$106.0M | +$693k bull / -$2.2M bear | out (clean 27, ADX 42, RVol 1.0) |
| 10 | **QQQ** | 692.70 | - | **-** | 23 | - | NEG -$10.4B | 729.58 | 720 | 690 | +$64.7M | +$1.3M bull / -$487k bear | out (clean 28, ADX 46, RVol 1.5) |
| 11 | **IWM** | 279.34 | - | **-** | 23 | - | NEG -$967.9M | 281.28 | 280 | 278 | +$9.2M | +$88k bull / -$174k bear | out (clean 28, ADX 39, RVol 0.3) |
| 12 | **DELL** | 422.39 | - | **-** | 22 | - | NEG -$56.9M | - | 440 | 425 | +$3.2M | - | out (clean 32, ADX 50, RVol 3.6) |
| 13 | **AAPL** | 347.56 | - | **-** | 20 | - | POS +$560.1M | 345.05 | 350 | 345 | -$6.5M | +$0 bull / -$1.5M bear | out (clean 31, ADX 18, RVol 1.5) |
| 14 | **PLTR** | 187.19 | - | **-** | 20 | - | NEG -$72.3M | 192.76 | 190 | 190 | -$2.9M | +$0 bull / -$27k bear | out (clean 25, ADX 27, RVol 0.8) |
| 15 | **COIN** | 140.42 | - | **-** | 20 | - | NEG -$16.1M | - | 140 | 140 | -$3.6M | - | out (clean 27, ADX 45, RVol 2.9) |
| 16 | **AMZN** | 239.34 | - | **-** | 19 | - | NEG -$176.4M | 246.02 | 250 | 240 | -$4.6M | +$44k bull / -$729k bear | out (clean 31, ADX 17, RVol 1.7) |
| 17 | **SMCI** | 32.13 | - | **-** | 19 | - | NEG -$3.1M | 32.57 | 35 | 32 | +$645k | - | out (clean 29, ADX 48, RVol 0.9) |
| 18 | **SHOP** | 156.06 | - | **-** | 19 | - | NEG -$17.8M | - | 155 | 157.5 | +$291k | - | out (clean 27, ADX 52, RVol 1.2) |
| 19 | **MSFT** | 523.34 | - | **-** | 18 | - | POS +$622.5M | 516.85 | 525 | 525 | +$1.6M | +$177k bull / -$96k bear | out (clean 26, ADX 20, RVol 0.8) |
| 20 | **GOOGL** | 280.85 | - | **-** | 17 | - | NEG -$270.3M | - | 280 | 280 | -$2.1M | +$412k bull / +$0 bear | out (clean 32, ADX 16, RVol 0.9) |
| 21 | **AVGO** | 325.50 | - | **-** | 15 | - | NEG -$151.4M | - | 330 | 325 | +$2.1M | - | out (clean 30, ADX 52, RVol 1.0) |
| 22 | **META** | 620.19 | - | **-** | 14 | - | NEG -$38.7M | 621.37 | 625 | 625 | +$158k | +$1.4M bull / +$0 bear | out (clean 28, ADX 14, RVol 0.7) |
| 23 | **NFLX** | 62.30 | - | **-** | 12 | - | NEG -$23.1M | 62.83 | 63 | 62 | +$1.2M | - | out (clean 31, ADX 15, RVol 0.8) |
| 24 | **HOOD** | 83.88 | - | **-** | 12 | - | NEG -$41.7M | - | 85 | 85 | +$748k | - | out (clean 31, ADX 47, RVol 0.6) |
| 25 | **BABA** | 98.48 | - | **-** | 8 | - | NEG -$22.5M | 98.92 | 100 | 98 | +$132k | - | out (clean 29, ADX 13, RVol 0.2) |
| 26 | **UBER** | 65.28 | - | **-** | 4 | - | NEG -$34.3M | 66.39 | 65 | 65 | +$21k | - | out (clean 28, ADX 8, RVol 0.4) |
| 27 | **CRM** | 231.40 | - | **-** | 4 | - | NEG -$22.9M | 240.23 | 240 | 230 | -$57k | - | out (clean 27, ADX 10, RVol 0.4) |

## Big prints this scan (87)
- **MSTR** CALL 138 2026-11-06 (7DTE): 3,750 @ 4.22 = **+$1.6M** SELL | vol 10,778 / OI 55
- **COIN** CALL 143 2026-11-06 (7DTE): 2,625 @ 5.02 = **+$1.3M** MID | vol 8,013 / OI 0
- **MSTR** CALL 138 2026-11-06 (7DTE): 3,000 @ 4.06 = **+$1.2M** SELL | vol 10,778 / OI 55
- **MSTR** CALL 138 2026-11-06 (7DTE): 2,000 @ 4.06 = **+$812k** SELL | vol 10,778 / OI 55
- **MSTR** CALL 138 2026-11-06 (7DTE): 1,250 @ 4.22 = **+$528k** SELL | vol 10,778 / OI 55
- **QQQ** CALL 725 2026-11-06 (7DTE): 5,000 @ 1.03 = **+$515k** BUY | vol 10,775 / OI 6,645
- **SPY** PUT 767 2026-11-04 (5DTE): 245 @ 11.56 = **+$283k** BUY | vol 14,922 / OI 29,783
- **META** CALL 645 2026-11-06 (7DTE): 500 @ 5.33 = **+$266k** MID | vol 2,996 / OI 3,329
- **SPY** PUT 767 2026-11-04 (5DTE): 199 @ 11.35 = **+$226k** BUY | vol 14,922 / OI 29,783
- **AAPL** PUT 347.5 2026-10-30 (0DTE): 1,799 @ 1.25 = **+$225k** BUY | vol 45,500 / OI 2,195
- **SPY** PUT 767 2026-11-04 (5DTE): 199 @ 11.23 = **+$223k** BUY | vol 14,922 / OI 29,783
- **SPY** PUT 767 2026-11-04 (5DTE): 200 @ 11.16 = **+$223k** BUY | vol 14,922 / OI 29,783
- **AMZN** CALL 237.5 2026-11-02 (3DTE): 500 @ 4.00 = **+$200k** MID | vol 3,318 / OI 108
- **QQQ** PUT 720 2026-10-30 (0DTE): 63 @ 27.94 = **+$176k** BUY | vol 1,457 / OI 22,475
- **SPY** PUT 767 2026-11-04 (5DTE): 145 @ 11.38 = **+$165k** BUY | vol 14,922 / OI 29,783

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 730 2026-11-04 (5DTE): 2,418 traded vs OI 983
- **SPY** PUT 738 2026-11-03 (4DTE): 511 traded vs OI 447
- **SPY** CALL 775 2026-10-30 (0DTE): 14,491 traded vs OI 14,149
- **SPY** CALL 779 2026-11-06 (7DTE): 1,018 traded vs OI 947
- **SPY** PUT 710 2026-11-09 (10DTE): 523 traded vs OI 115
- **QQQ** CALL 727 2026-11-02 (3DTE): 1,368 traded vs OI 538
- **QQQ** CALL 693 2026-11-06 (7DTE): 510 traded vs OI 74
- **QQQ** CALL 709 2026-11-03 (4DTE): 591 traded vs OI 23
- **QQQ** CALL 716 2026-11-04 (5DTE): 624 traded vs OI 66
- **QQQ** CALL 691 2026-11-02 (3DTE): 545 traded vs OI 0
- **QQQ** CALL 716 2026-11-03 (4DTE): 542 traded vs OI 116
- **QQQ** PUT 625 2026-11-13 (14DTE): 608 traded vs OI 600
- **QQQ** CALL 705 2026-11-09 (10DTE): 500 traded vs OI 106
- **NVDA** PUT 205 2026-11-06 (7DTE): 5,956 traded vs OI 5,814
- **NVDA** PUT 195 2026-11-04 (5DTE): 502 traded vs OI 452

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
