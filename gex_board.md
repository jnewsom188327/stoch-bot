# GEX + FLOW SCAN - Fri Oct 30, 11:25 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (3)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:25 | **COIN** | **PUTS** | FLOW SURGE | 10/30 138P | 0.73 | 0.59 | -19% (0m) | **-19%** | +115% | 137.27 |
| 10:25 | **SMCI** | **PUTS** | FLIP CROSS down into negative gamma | 10/30 32.5P | 0.43 | 0.31 | -12% (1m) | **-28%** | +32% | 32 |
| 10:15 | **AAPL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 10/30 347.5C | 0.50 | 1.24 | +356% (38m) | **+148%** (done) | +104% | 347.56 hit |

## 1m RULES on SPY / QQQ - loose (1 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 11:25:08 ET, last candle SPY 11:24, QQQ 11:24 | no errors
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
| 1 | **ARM** | 205.62 | FLOW SURGE | **CALLS** | 59 | none: 32 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (27 contracts' greeks worked out here) | NEG -$20.1M | - | 220 | 205 | +$472k | +$27k bull / +$0 bear | out (clean 26, ADX 49, RVol 3.2) |
| 2 | **COIN** | 140.43 | FLOW SURGE | **PUTS** | 58 | 10/30 138P @ 0.73 (delta 0.27) = est +115% at 137.27 | NEG -$15.1M | - | 150 | 140 | -$4.7M | +$28k bull / -$1.5M bear | out (clean 27, ADX 52, RVol 3.0) |
| 3 | **ORCL** | 131.97 | FLOW SURGE | **CALLS** | 39 | 10/30 133C @ 0.49 (delta 0.32) = est +136% at 133.85 | POS +$48.3M | 129.17 | 130 | 130 | +$2.5M | +$822k bull / +$0 bear | out (clean 33, ADX 42, RVol 0.6) |
| 4 | **NVDA** | 206.45 | - | **-** | 28 | - | NEG -$424.4M | 211.92 | 210 | 205 | +$13.9M | +$1.0M bull / -$166k bear | out (clean 26, ADX 40, RVol 1.3) |
| 5 | **MSTR** | 133.26 | - | **-** | 28 | - | NEG -$19.9M | - | 135 | 130 | -$5.4M | +$0 bull / -$2.4M bear | out (clean 27, ADX 29, RVol 2.0) |
| 6 | **AMZN** | 241.39 | - | **-** | 27 | - | NEG -$145.4M | 247.71 | 250 | 240 | -$12.1M | +$0 bull / -$923k bear | out (clean 32, ADX 18, RVol 2.7) |
| 7 | **DELL** | 428.49 | - | **-** | 27 | - | NEG -$54.5M | - | 440 | 425 | +$949k | +$29k bull / +$0 bear | out (clean 32, ADX 48, RVol 3.6) |
| 8 | **AMD** | 513.32 | - | **-** | 26 | - | NEG -$101.7M | 524.15 | 517.5 | 500 | +$11.2M | +$1.1M bull / -$60k bear | out (clean 28, ADX 38, RVol 1.2) |
| 9 | **GOOGL** | 282.37 | - | **-** | 25 | - | NEG -$237.0M | - | 280 | 280 | -$3.7M | +$0 bull / -$782k bear | out (clean 32, ADX 22, RVol 1.2) |
| 10 | **MU** | 889.84 | - | **-** | 25 | - | NEG -$232.7M | 933.5 | 900 | 900 | +$35.6M | +$3.0M bull / +$0 bear | out (clean 29, ADX 32, RVol 0.6) |
| 11 | **NFLX** | 62.44 | - | **-** | 24 | - | NEG -$19.6M | 62.99 | 63 | 62 | +$880k | +$49k bull / +$0 bear | out (clean 31, ADX 26, RVol 0.6) |
| 12 | **SPY** | 758.77 | - | **-** | 23 | - | NEG -$13.9B | 771.98 | 760 | 760 | +$57.8M | +$4.5M bull / +$0 bear | out (clean 26, ADX 40, RVol 0.9) |
| 13 | **AAPL** | 348.43 | - | **-** | 23 | - | POS +$768.8M | 342.7 | 350 | 345 | -$6.3M | +$70k bull / -$42k bear | out (clean 31, ADX 28, RVol 1.3) |
| 14 | **PLTR** | 186.85 | - | **-** | 23 | - | NEG -$71.5M | 192.45 | 185 | 190 | -$2.4M | +$186k bull / +$0 bear | out (clean 25, ADX 35, RVol 1.2) |
| 15 | **QQQ** | 695.15 | - | **-** | 20 | - | NEG -$10.0B | 727.38 | 720 | 690 | +$10.0M | +$4.4M bull / +$0 bear | out (clean 27, ADX 44, RVol 1.0) |
| 16 | **TSLA** | 401.78 | - | **-** | 20 | - | POS +$476.9M | 389.56 | 400 | 400 | -$25.7M | +$2.4M bull / -$1.6M bear | out (clean 29, ADX 23, RVol 1.2) |
| 17 | **META** | 623.22 | - | **-** | 20 | - | POS +$34.1M | 621.9 | 625 | 625 | -$6.8M | +$1.6M bull / +$0 bear | out (clean 28, ADX 16, RVol 0.7) |
| 18 | **MSFT** | 521.99 | - | **-** | 20 | - | POS +$481.2M | 515.66 | 525 | 525 | +$1.8M | +$29k bull / +$0 bear | out (clean 26, ADX 25, RVol 0.9) |
| 19 | **SMCI** | 32.49 | - | **-** | 20 | - | POS +$707k | 32.39 | 35 | 32 | +$594k | - | out (clean 28, ADX 41, RVol 0.8) |
| 20 | **SHOP** | 156.60 | - | **-** | 19 | - | NEG -$15.5M | - | 160 | 157.5 | +$200k | - | out (clean 26, ADX 49, RVol 1.4) |
| 21 | **SMH** | 526.07 | - | **-** | 18 | - | NEG -$542.1M | - | 530 | 530 | +$4.7M | - | out (clean 28, ADX 47, RVol 1.6) |
| 22 | **IWM** | 279.88 | - | **-** | 14 | - | NEG -$718.7M | 281.35 | 280 | 270 | +$6.1M | - | out (clean 27, ADX 37, RVol 0.6) |
| 23 | **AVGO** | 326.91 | - | **-** | 13 | - | NEG -$116.6M | 336.55 | 330 | 330 | +$1.2M | - | out (clean 29, ADX 52, RVol 0.8) |
| 24 | **HOOD** | 84.19 | - | **-** | 12 | - | NEG -$42.2M | - | 85 | 85 | +$461k | - | out (clean 31, ADX 52, RVol 0.8) |
| 25 | **CRM** | 232.18 | - | **-** | 8 | - | NEG -$18.5M | 237.59 | 240 | 230 | -$76k | - | out (clean 28, ADX 14, RVol 0.6) |
| 26 | **UBER** | 65.38 | - | **-** | 4 | - | NEG -$31.4M | 66.47 | 66 | 65 | -$9k | - | out (clean 28, ADX 10, RVol 0.3) |
| 27 | **BABA** | 99.06 | - | **-** | 4 | - | NEG -$34.4M | 100.36 | 100 | 99 | -$12k | - | out (clean 29, ADX 15, RVol 0.3) |

## Big prints this scan (107)
- **QQQ** CALL 700 2026-11-06 (7DTE): 444 @ 8.41 = **+$373k** BUY | vol 28,401 / OI 1,011
- **MU** PUT 920 2026-10-30 (0DTE): 125 @ 27.80 = **+$348k** SELL | vol 1,051 / OI 1,471
- **MU** PUT 920 2026-10-30 (0DTE): 125 @ 27.80 = **+$348k** SELL | vol 1,051 / OI 1,471
- **SPY** CALL 758 2026-11-02 (3DTE): 778 @ 4.02 = **+$313k** BUY | vol 17,313 / OI 147
- **MU** PUT 910 2026-10-30 (0DTE): 125 @ 18.55 = **+$232k** SELL | vol 1,367 / OI 1,105
- **MU** PUT 910 2026-10-30 (0DTE): 125 @ 18.55 = **+$232k** SELL | vol 1,367 / OI 1,105
- **TSLA** CALL 400 2026-10-30 (0DTE): 625 @ 3.45 = **+$216k** BUY | vol 113,964 / OI 13,581
- **TSLA** CALL 405 2026-11-02 (3DTE): 415 @ 3.95 = **+$164k** BUY | vol 7,498 / OI 1,326
- **QQQ** CALL 696 2026-10-30 (0DTE): 840 @ 1.94 = **+$163k** BUY | vol 107,322 / OI 757
- **META** PUT 640 2026-11-06 (7DTE): 70 @ 23.21 = **+$162k** SELL | vol 99 / OI 1,785
- **GOOGL** CALL 282.5 2026-11-06 (7DTE): 300 @ 5.15 = **+$154k** SELL | vol 2,869 / OI 0
- **META** PUT 645 2026-10-30 (0DTE): 70 @ 20.86 = **+$146k** SELL | vol 145 / OI 945
- **TSLA** CALL 410 2026-11-06 (7DTE): 200 @ 6.45 = **+$129k** BUY | vol 6,622 / OI 2,432
- **TSLA** CALL 402.5 2026-10-30 (0DTE): 625 @ 2.03 = **+$127k** BUY | vol 59,761 / OI 2,780
- **QQQ** CALL 695 2026-10-30 (0DTE): 500 @ 2.50 = **+$125k** BUY | vol 86,442 / OI 1,463

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 763 2026-11-02 (3DTE): 987 traded vs OI 887
- **SPY** PUT 748 2026-11-04 (5DTE): 504 traded vs OI 186
- **SPY** PUT 755 2026-11-05 (6DTE): 548 traded vs OI 453
- **SPY** CALL 777 2026-11-02 (3DTE): 507 traded vs OI 444
- **SPY** PUT 750 2026-11-09 (10DTE): 1,489 traded vs OI 1,122
- **SPY** PUT 745 2026-11-09 (10DTE): 982 traded vs OI 424
- **QQQ** PUT 660 2026-11-04 (5DTE): 659 traded vs OI 657
- **QQQ** PUT 685 2026-11-02 (3DTE): 5,120 traded vs OI 5,039
- **QQQ** CALL 714 2026-11-03 (4DTE): 501 traded vs OI 64
- **QQQ** PUT 640 2026-11-02 (3DTE): 796 traded vs OI 412
- **QQQ** CALL 715 2026-11-05 (6DTE): 527 traded vs OI 233
- **QQQ** PUT 640 2026-11-13 (14DTE): 646 traded vs OI 592
- **QQQ** PUT 655 2026-11-09 (10DTE): 530 traded vs OI 182
- **TSLA** CALL 432.5 2026-11-02 (3DTE): 1,267 traded vs OI 1,265
- **TSLA** PUT 400 2026-11-13 (14DTE): 535 traded vs OI 496

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
