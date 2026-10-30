# GEX + FLOW SCAN - Fri Oct 30, 10:50 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (2)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:25 | **SMCI** | **PUTS** | FLIP CROSS down into negative gamma | 10/30 32.5P | 0.43 | 0.19 | -12% (1m) | **-56%** | +32% | 32 |
| 10:15 | **AAPL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 10/30 347.5C | 0.50 | 2.16 | +346% (35m) | **+332%** | +104% | 347.56 hit |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:50:08 ET, last candle SPY 10:49, QQQ 10:49 | no errors

## Flow surges NOT fired - price disagreed (35 today, last 5)
- 10:50 AAPL PUTS: price +2.30 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:45 SMCI CALLS: under EMA 20 - flow says one way, price says the other
- 10:45 AAPL PUTS: price +2.47 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:40 SMCI CALLS: under EMA 20 - flow says one way, price says the other
- 10:40 NVDA CALLS: under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **AAPL** | 349.03 | FLOW SURGE | **PUTS** | 51 | 10/30 347.5P @ 0.71 (delta 0.32) = est +265% at 345 | POS +$785.4M | 342.22 | 350 | 345 | -$11.3M | +$0 bull / -$893k bear | out (clean 30, ADX 41, RVol 1.8) |
| 2 | **META** | 624.24 | PINNED between the walls (positive gamma) - chop | **-** | 38 | - | POS +$49.7M | 622.12 | 625 | 625 | -$3.8M | +$0 bull / -$424k bear | out (clean 28, ADX 24, RVol 0.9) |
| 3 | **SMCI** | 32.67 | - | **-** | 33 | - | POS +$1.6M | 32.5 | 35 | 32 | +$469k | +$0 bull / -$50k bear | out (clean 28, ADX 44, RVol 1.5) |
| 4 | **DELL** | 434.29 | - | **-** | 30 | - | NEG -$56.5M | - | 440 | 425 | -$938k | +$0 bull / -$279k bear | out (clean 32, ADX 48, RVol 3.7) |
| 5 | **SMH** | 530.47 | - | **-** | 29 | - | NEG -$532.2M | - | 530 | 530 | -$2.4M | +$0 bull / -$3.8M bear | out (clean 28, ADX 47, RVol 2.0) |
| 6 | **ORCL** | 133.20 | - | **-** | 28 | - | POS +$68.6M | 130.14 | 135 | 130 | +$937k | +$335k bull / +$0 bear | out (clean 32, ADX 37, RVol 0.9) |
| 7 | **IWM** | 280.41 | - | **-** | 27 | - | NEG -$489.8M | 281.37 | 280 | 270 | +$5.3M | +$0 bull / -$1.3M bear | out (clean 27, ADX 40, RVol 1.3) |
| 8 | **TSLA** | 403.71 | - | **-** | 27 | - | POS +$529.9M | 381.22 | 400 | 400 | -$26.3M | +$0 bull / -$4.0M bear | out (clean 29, ADX 28, RVol 1.6) |
| 9 | **MSTR** | 130.68 | - | **-** | 27 | - | NEG -$24.4M | - | 135 | 125 | -$1.2M | +$0 bull / -$341k bear | out (clean 27, ADX 42, RVol 2.9) |
| 10 | **ARM** | 205.91 | - | **-** | 27 | - | NEG -$19.2M | - | 220 | 205 | +$374k | - | out (clean 25, ADX 46, RVol 4.0) |
| 11 | **QQQ** | 697.22 | - | **-** | 26 | - | NEG -$9.5B | 727.25 | 720 | 700 | -$30.7M | +$0 bull / -$10.4M bear | out (clean 27, ADX 47, RVol 6.0) |
| 12 | **AMZN** | 239.09 | - | **-** | 26 | - | NEG -$157.6M | 246.46 | 250 | 240 | -$5.8M | +$0 bull / -$3.2M bear | out (clean 32, ADX 25, RVol 3.8) |
| 13 | **PLTR** | 188.26 | - | **-** | 26 | - | NEG -$55.3M | 192.04 | 190 | 190 | -$1.7M | +$0 bull / -$353k bear | out (clean 25, ADX 37, RVol 2.0) |
| 14 | **MU** | 896.70 | - | **-** | 26 | - | NEG -$205.8M | 931.71 | 900 | 900 | +$14.8M | +$0 bull / -$3.0M bear | out (clean 29, ADX 35, RVol 2.0) |
| 15 | **NVDA** | 207.06 | - | **-** | 25 | - | NEG -$404.5M | 212.24 | 210 | 210 | +$2.9M | +$0 bull / -$1.3M bear | out (clean 25, ADX 42, RVol 2.1) |
| 16 | **HOOD** | 84.42 | - | **-** | 25 | - | NEG -$40.0M | - | 85 | 85 | +$476k | +$0 bull / -$90k bear | out (clean 31, ADX 53, RVol 1.4) |
| 17 | **SPY** | 760.01 | - | **-** | 24 | - | NEG -$13.1B | 772.04 | 760 | 760 | +$19.8M | +$0 bull / -$9.4M bear | out (clean 27, ADX 43, RVol 1.9) |
| 18 | **AMD** | 515.66 | - | **-** | 24 | - | NEG -$79.1M | 524.92 | 527.5 | 500 | +$1.2M | +$0 bull / -$2.3M bear | out (clean 28, ADX 41, RVol 2.6) |
| 19 | **SHOP** | 158.06 | - | **-** | 24 | - | NEG -$13.8M | 164.37 | 160 | 157.5 | +$63k | +$30k bull / +$0 bear | out (clean 25, ADX 44, RVol 1.6) |
| 20 | **AVGO** | 328.59 | - | **-** | 23 | - | NEG -$123.4M | 343.42 | 330 | 330 | -$360k | +$0 bull / -$1.4M bear | out (clean 30, ADX 50, RVol 1.3) |
| 21 | **COIN** | 139.90 | - | **-** | 21 | - | NEG -$14.2M | - | 150 | 140 | +$876k | - | out (clean 27, ADX 57, RVol 3.1) |
| 22 | **GOOGL** | 281.44 | - | **-** | 19 | - | NEG -$272.6M | - | 280 | 280 | -$221k | +$0 bull / -$92k bear | out (clean 31, ADX 32, RVol 1.2) |
| 23 | **MSFT** | 522.75 | - | **-** | 18 | - | POS +$542.9M | 514.67 | 525 | 525 | +$64k | +$380k bull / -$188k bear | out (clean 27, ADX 24, RVol 1.6) |
| 24 | **NFLX** | 62.81 | - | **-** | 12 | - | NEG -$10.6M | 63.26 | 63 | 63 | +$215k | - | out (clean 32, ADX 35, RVol 0.9) |
| 25 | **CRM** | 232.06 | - | **-** | 8 | - | NEG -$22.9M | 239.77 | 240 | 230 | -$47k | - | out (clean 27, ADX 16, RVol 0.9) |
| 26 | **UBER** | 65.38 | - | **-** | 7 | - | NEG -$28.8M | 66.33 | 66 | 65 | -$23k | - | out (clean 28, ADX 14, RVol 0.7) |
| 27 | **BABA** | 99.07 | - | **-** | 7 | - | NEG -$32.6M | 100.42 | 100 | 99 | -$22k | - | out (clean 29, ADX 18, RVol 0.6) |

## Big prints this scan (141)
- **TSLA** CALL 395 2026-11-02 (3DTE): 870 @ 6.66 = **+$579k** SELL | vol 6,603 / OI 1,669
- **SPY** CALL 758 2026-11-02 (3DTE): 1,000 @ 3.68 = **+$368k** SELL | vol 10,612 / OI 147
- **TSLA** CALL 400 2026-11-02 (3DTE): 870 @ 3.98 = **+$346k** SELL | vol 7,593 / OI 1,402
- **TSLA** CALL 392.5 2026-11-02 (3DTE): 390 @ 8.32 = **+$324k** SELL | vol 2,828 / OI 677
- **AMD** PUT 527.5 2026-10-30 (0DTE): 157 @ 17.80 = **+$279k** BUY | vol 301 / OI 475
- **AMZN** CALL 240 2026-11-06 (7DTE): 600 @ 4.41 = **+$265k** SELL | vol 6,517 / OI 729
- **AMZN** CALL 240 2026-11-06 (7DTE): 600 @ 4.41 = **+$265k** SELL | vol 6,517 / OI 729
- **AAPL** PUT 340 2026-11-04 (5DTE): 386 @ 4.94 = **+$191k** BUY | vol 2,881 / OI 1,656
- **TSLA** PUT 405 2026-11-06 (7DTE): 145 @ 12.90 = **+$187k** BUY | vol 1,250 / OI 816
- **QQQ** PUT 690 2026-11-04 (5DTE): 273 @ 6.80 = **+$186k** BUY | vol 1,591 / OI 792
- **AMZN** CALL 240 2026-11-06 (7DTE): 400 @ 4.42 = **+$177k** SELL | vol 6,517 / OI 729
- **AMZN** CALL 240 2026-11-06 (7DTE): 400 @ 4.42 = **+$177k** SELL | vol 6,517 / OI 729
- **AMZN** PUT 245 2026-10-30 (0DTE): 250 @ 7.00 = **+$175k** BUY | vol 5,139 / OI 4,298
- **AVGO** PUT 340 2026-10-30 (0DTE): 138 @ 12.63 = **+$174k** BUY | vol 1,137 / OI 3,431
- **AVGO** PUT 340 2026-10-30 (0DTE): 126 @ 12.63 = **+$159k** BUY | vol 1,137 / OI 3,431

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 778 2026-10-30 (0DTE): 6,027 traded vs OI 6,011
- **SPY** PUT 715 2026-11-13 (14DTE): 1,550 traded vs OI 1,501
- **SPY** CALL 770 2026-11-06 (7DTE): 3,839 traded vs OI 3,767
- **SPY** PUT 758 2026-11-13 (14DTE): 1,360 traded vs OI 1,324
- **SPY** CALL 776 2026-11-13 (14DTE): 18,512 traded vs OI 561
- **SPY** CALL 775 2026-11-27 (28DTE): 711 traded vs OI 550
- **QQQ** CALL 721 2026-10-30 (0DTE): 1,814 traded vs OI 1,808
- **QQQ** CALL 694 2026-11-03 (4DTE): 535 traded vs OI 0
- **QQQ** CALL 685 2026-10-30 (0DTE): 500 traded vs OI 234
- **QQQ** PUT 650 2026-11-04 (5DTE): 883 traded vs OI 181
- **QQQ** CALL 710 2026-11-03 (4DTE): 2,962 traded vs OI 2,651
- **QQQ** CALL 720 2026-11-04 (5DTE): 561 traded vs OI 314
- **QQQ** CALL 714 2026-11-02 (3DTE): 531 traded vs OI 236
- **QQQ** CALL 720 2026-11-05 (6DTE): 502 traded vs OI 409
- **QQQ** PUT 667 2026-11-04 (5DTE): 514 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
