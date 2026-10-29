# GEX + FLOW SCAN - Thu Oct 29, 02:10 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (4)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:30 | **IWM** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 10/29 284P | 0.65 | 0.22 | +3% (25m) | **-66%** (done) | +232% | 281.86 |
| 10:00 | **ORCL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 10/30 145C | 0.79 | 0.84 | +18% (37m) | **+6%** (done) | +139% | 143.92 |
| 09:55 | **AAPL** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 10/30 345P | 0.77 | 0.68 | +17% (2m) | **-12%** (done) | +198% | 345 |
| 09:50 | **IWM** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 10/29 283P | 0.50 | 0.18 | +20% (21m) | **-64%** (done) | +159% | 282 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 14:10:08 ET, last candle SPY 14:09, QQQ 14:09 | no errors

## Flow surges NOT fired - price disagreed (2 today, last 5)
- 10:05 HOOD PUTS: price +0.99 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:00 HOOD PUTS: price +0.89 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **IWM** | 283.43 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 35 | 10/29 284P @ 0.76 (delta 0.71) = est +97% at 282.5 | POS +$521.6M | 282.5 | 284 | 270 | -$301k | +$132k bull / +$0 bear | out (clean 26, ADX 26, RVol 0.8) |
| 2 | **AAPL** | 349.98 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 23 | none: 55 puts 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (7 contracts' greeks worked out here) | POS +$677.3M | 340.88 | 350 | 345 | +$3.2M | - | out (clean 29, ADX 16, RVol 0.6) |
| 3 | **DELL** | 476.53 | - | **-** | 23 | - | NEG -$4.9M | 480.49 | 500 | 460 | +$1.9M | +$203k bull / +$0 bear | out (clean 30, ADX 47, RVol 0.9) |
| 4 | **MSFT** | 528.33 | - | **-** | 22 | - | POS +$597.4M | 501.78 | 525 | 530 | +$25.3M | +$0 bull / -$1.4M bear | out (clean 27, ADX 17, RVol 1.1) |
| 5 | **GOOGL** | 282.38 | - | **-** | 22 | - | NEG -$187.7M | - | 300 | 290 | -$6.5M | +$95k bull / +$0 bear | out (clean 32, ADX 39, RVol 1.6) |
| 6 | **MU** | 932.78 | - | **-** | 21 | - | POS +$252.9M | 882.92 | 950 | 900 | +$35.3M | +$2.2M bull / +$0 bear | out (clean 27, ADX 42, RVol 0.4) |
| 7 | **ORCL** | 137.77 | - | **-** | 21 | - | POS +$117.7M | - | 135 | 140 | +$1.0M | +$0 bull / -$57k bear | out (clean 32, ADX 41, RVol 0.6) |
| 8 | **SMH** | 558.63 | - | **-** | 19 | - | NEG -$80.2M | 562.4 | 560 | 555 | +$1.4M | +$652k bull / +$0 bear | out (clean 26, ADX 19, RVol 0.3) |
| 9 | **SPY** | 767.51 | - | **-** | 18 | - | NEG -$6.4B | 772.41 | 770 | 765 | -$86.4M | +$134k bull / -$221k bear | out (clean 25, ADX 25, RVol 0.5) |
| 10 | **META** | 627.81 | - | **-** | 18 | - | NEG -$42.7M | 631.01 | 650 | 625 | -$9.4M | +$846k bull / +$0 bear | out (clean 28, ADX 30, RVol 0.6) |
| 11 | **QQQ** | 713.24 | - | **-** | 17 | - | NEG -$5.6B | 725.96 | 720 | 700 | -$57.0M | +$824k bull / +$0 bear | out (clean 26, ADX 25, RVol 0.4) |
| 12 | **NVDA** | 212.86 | - | **-** | 16 | - | POS +$151.8M | 211 | 215 | 210 | -$2.4M | +$392k bull / +$0 bear | out (clean 24, ADX 21, RVol 0.6) |
| 13 | **TSLA** | 405.13 | - | **-** | 16 | - | POS +$493.8M | - | 400 | 400 | -$19.7M | +$109k bull / -$258k bear | out (clean 28, ADX 17, RVol 0.3) |
| 14 | **AMZN** | 244.68 | - | **-** | 16 | - | POS +$10.1M | 241.76 | 265 | 250 | -$1.4M | +$643k bull / +$0 bear | out (clean 31, ADX 24, RVol 0.9) |
| 15 | **AMD** | 564.54 | - | **-** | 15 | - | POS +$141.4M | - | 550 | 550 | -$1.3M | +$775k bull / +$0 bear | out (clean 28, ADX 21, RVol 0.3) |
| 16 | **COIN** | 160.02 | - | **-** | 15 | - | POS +$4.9M | 153.53 | 170 | 155 | -$104k | +$79k bull / +$0 bear | out (clean 25, ADX 13, RVol 0.6) |
| 17 | **MSTR** | 141.57 | - | **-** | 15 | - | POS +$27.6M | - | 152.5 | 140 | +$31k | +$59k bull / +$0 bear | out (clean 26, ADX 17, RVol 0.9) |
| 18 | **SMCI** | 34.70 | - | **-** | 14 | - | POS +$22.5M | - | 35 | 35 | +$298k | - | out (clean 26, ADX 31, RVol 0.6) |
| 19 | **UBER** | 65.18 | - | **-** | 14 | - | NEG -$34.0M | 68.5 | 70 | 65 | -$161k | - | out (clean 28, ADX 18, RVol 0.2) |
| 20 | **ARM** | 228.68 | - | **-** | 13 | - | POS +$2.6M | 222.57 | 227.5 | 220 | +$1.6M | - | out (clean 24, ADX 12, RVol 0.5) |
| 21 | **NFLX** | 61.85 | - | **-** | 10 | - | NEG -$56.0M | - | 63 | 60 | -$423k | - | out (clean 31, ADX 28, RVol 0.7) |
| 22 | **CRM** | 231.41 | - | **-** | 8 | - | NEG -$19.8M | - | 240 | 230 | -$242k | - | out (clean 27, ADX 11, RVol 0.6) |
| 23 | **BABA** | 99.09 | - | **-** | 8 | - | NEG -$21.2M | 101.48 | 100 | 100 | -$23k | - | out (clean 29, ADX 26, RVol 1.1) |
| 24 | **HOOD** | 90.78 | - | **-** | 6 | - | NEG -$26.6M | - | 95 | 90 | -$426k | - | out (clean 28, ADX 21, RVol 0.4) |
| 25 | **SHOP** | 166.48 | - | **-** | 5 | - | NEG -$5.5M | 171.64 | 175 | 165 | -$23k | - | out (clean 26, ADX 15, RVol 0.4) |
| 26 | **AVGO** | 344.54 | - | **-** | 4 | - | POS +$27.4M | 340.56 | 350 | 340 | +$768k | - | out (clean 27, ADX 15, RVol 0.4) |
| 27 | **PLTR** | 193.94 | - | **-** | 4 | - | POS +$19.8M | 192.24 | 200 | 190 | -$139k | - | out (clean 25, ADX 18, RVol 0.3) |

## Big prints this scan (52)
- **MSFT** PUT 525 2026-10-30 (1DTE): 1,300 @ 3.92 = **+$510k** BUY | vol 11,469 / OI 1,940
- **MSFT** PUT 525 2026-10-30 (1DTE): 1,300 @ 3.92 = **+$510k** BUY | vol 11,469 / OI 1,940
- **SMH** CALL 540 2026-10-30 (1DTE): 225 @ 20.59 = **+$463k** BUY | vol 234 / OI 2,809
- **AMD** PUT 547.5 2026-11-02 (4DTE): 500 @ 4.95 = **+$248k** SELL | vol 682 / OI 151
- **AMD** PUT 562.5 2026-10-30 (1DTE): 300 @ 7.95 = **+$238k** SELL | vol 2,086 / OI 105
- **SMH** CALL 555 2026-10-30 (1DTE): 225 @ 8.38 = **+$189k** BUY | vol 269 / OI 1,371
- **MSFT** PUT 517.5 2026-10-30 (1DTE): 1,300 @ 1.44 = **+$187k** BUY | vol 5,816 / OI 633
- **AMZN** PUT 245 2026-10-30 (1DTE): 150 @ 9.75 = **+$146k** SELL | vol 8,303 / OI 3,801
- **TSLA** CALL 400 2026-10-30 (1DTE): 239 @ 6.00 = **+$143k** SELL | vol 16,361 / OI 14,892
- **SPY** PUT 767 2026-10-29 (0DTE): 1,327 @ 1.01 = **+$134k** SELL | vol 320,305 / OI 2,012
- **SPY** PUT 767 2026-11-04 (6DTE): 250 @ 4.85 = **+$121k** BUY | vol 12,156 / OI 11,544
- **MU** CALL 935 2026-10-30 (1DTE): 80 @ 14.41 = **+$115k** BUY | vol 3,434 / OI 1,088
- **QQQ** CALL 713 2026-10-29 (0DTE): 500 @ 2.25 = **+$112k** BUY | vol 48,527 / OI 552
- **SPY** PUT 766 2026-10-29 (0DTE): 1,000 @ 1.00 = **+$100k** BUY | vol 189,755 / OI 1,218
- **AMD** PUT 565 2026-10-30 (1DTE): 100 @ 9.19 = **+$92k** SELL | vol 3,982 / OI 404

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 735 2026-11-03 (5DTE): 769 traded vs OI 701
- **SPY** CALL 784 2026-11-03 (5DTE): 942 traded vs OI 458
- **SPY** PUT 771 2026-11-03 (5DTE): 505 traded vs OI 291
- **SPY** PUT 758 2026-11-03 (5DTE): 500 traded vs OI 186
- **SPY** CALL 766 2026-11-02 (4DTE): 658 traded vs OI 593
- **SPY** CALL 767 2026-11-02 (4DTE): 1,271 traded vs OI 1,243
- **SPY** CALL 800 2026-11-05 (7DTE): 548 traded vs OI 329
- **SPY** CALL 807 2026-11-06 (8DTE): 610 traded vs OI 408
- **QQQ** CALL 736 2026-11-02 (4DTE): 548 traded vs OI 331
- **QQQ** PUT 686 2026-10-30 (1DTE): 1,103 traded vs OI 1,098
- **QQQ** CALL 725 2026-11-04 (6DTE): 517 traded vs OI 424
- **QQQ** PUT 682 2026-11-20 (22DTE): 1,073 traded vs OI 948
- **NVDA** CALL 225 2026-11-02 (4DTE): 3,305 traded vs OI 3,284
- **NVDA** CALL 217.5 2026-11-06 (8DTE): 3,203 traded vs OI 3,193
- **NVDA** PUT 202.5 2026-11-04 (6DTE): 573 traded vs OI 143

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
