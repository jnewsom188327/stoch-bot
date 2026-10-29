# GEX + FLOW SCAN - Thu Oct 29, 11:10 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (4)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:30 | **IWM** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 10/29 284P | 0.65 | 0.36 | +3% (25m) | **-45%** | +232% | 281.86 |
| 10:00 | **ORCL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 10/30 145C | 0.79 | 0.84 | +18% (37m) | **+6%** (done) | +139% | 143.92 |
| 09:55 | **AAPL** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 10/30 345P | 0.77 | 0.68 | +17% (2m) | **-12%** (done) | +198% | 345 |
| 09:50 | **IWM** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 10/29 283P | 0.50 | 0.18 | +20% (21m) | **-64%** (done) | +159% | 282 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 11:10:08 ET, last candle SPY 11:09, QQQ 11:09 | no errors

## Flow surges NOT fired - price disagreed (2 today, last 5)
- 10:05 HOOD PUTS: price +0.99 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:00 HOOD PUTS: price +0.89 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **MSFT** | 523.88 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 53 | none: 126 puts 0-7DTE > 11 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (12 contracts' greeks worked out here) | POS +$519.7M | 499.87 | 525 | 530 | +$27.0M | +$165k bull / -$2.0M bear | out (clean 28, ADX 23, RVol 2.1) |
| 2 | **IWM** | 284.47 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 43 | none: 306 puts 0-7DTE > 16 priced 0.40-0.80 > 5 delta 0.2+ > 5 spread ok > 5 liquid > best one only +14% at the target (needs +20%) (132 contracts' greeks worked out here) | POS +$868.2M | 281.33 | 284 | 270 | -$3.9M | +$244k bull / -$380k bear | out (clean 25, ADX 50, RVol 1.1) |
| 3 | **AMZN** | 247.22 | - | **-** | 28 | - | POS +$17.8M | 241.73 | 265 | 250 | -$11.1M | +$66k bull / -$159k bear | out (clean 31, ADX 37, RVol 1.2) |
| 4 | **GOOGL** | 286.24 | - | **-** | 28 | - | NEG -$201.4M | - | 300 | 290 | -$9.7M | +$161k bull / -$494k bear | out (clean 32, ADX 54, RVol 2.9) |
| 5 | **META** | 628.56 | - | **-** | 25 | - | NEG -$25.1M | 631 | 650 | 625 | -$14.7M | +$0 bull / -$463k bear | out (clean 28, ADX 47, RVol 0.8) |
| 6 | **ARM** | 228.60 | - | **-** | 22 | - | POS +$3.7M | 221.42 | 227.5 | 220 | +$1.7M | - | out (clean 27, ADX 20, RVol 1.7) |
| 7 | **TSLA** | 405.70 | - | **-** | 21 | - | POS +$499.1M | - | 400 | 400 | -$24.9M | +$5.1M bull / -$391k bear | out (clean 29, ADX 27, RVol 0.6) |
| 8 | **AAPL** | 349.12 | - | **-** | 21 | - | POS +$591.3M | 340.28 | 350 | 345 | +$5.2M | +$79k bull / -$309k bear | out (clean 29, ADX 36, RVol 0.8) |
| 9 | **AVGO** | 344.13 | - | **-** | 21 | - | POS +$12.0M | 342.93 | 350 | 340 | +$2.3M | +$0 bull / -$58k bear | out (clean 28, ADX 24, RVol 0.5) |
| 10 | **SPY** | 769.66 | - | **-** | 20 | - | NEG -$4.1B | 773.05 | 770 | 765 | -$105.3M | +$304k bull / -$3.0M bear | out (clean 26, ADX 12, RVol 0.6) |
| 11 | **QQQ** | 716.36 | - | **-** | 19 | - | NEG -$4.5B | 726.7 | 720 | 720 | -$72.8M | +$412k bull / -$992k bear | out (clean 27, ADX 20, RVol 0.7) |
| 12 | **UBER** | 65.42 | - | **-** | 19 | - | NEG -$31.3M | 67.97 | 67 | 65 | -$163k | - | out (clean 29, ADX 19, RVol 0.5) |
| 13 | **NVDA** | 214.22 | - | **-** | 18 | - | POS +$273.4M | 211 | 215 | 210 | -$4.6M | +$157k bull / -$613k bear | out (clean 24, ADX 20, RVol 0.9) |
| 14 | **AMD** | 571.57 | - | **-** | 18 | - | POS +$149.1M | - | 600 | 550 | -$4.6M | +$0 bull / -$127k bear | out (clean 28, ADX 31, RVol 0.3) |
| 15 | **MU** | 954.71 | - | **-** | 18 | - | POS +$398.5M | - | 950 | 950 | +$8.2M | +$28k bull / -$6.1M bear | out (clean 28, ADX 34, RVol 0.5) |
| 16 | **MSTR** | 142.98 | - | **-** | 18 | - | POS +$32.1M | - | 152.5 | 140 | -$696k | +$56k bull / +$0 bear | out (clean 25, ADX 14, RVol 1.2) |
| 17 | **ORCL** | 141.16 | - | **-** | 18 | - | POS +$125.2M | - | 140 | 140 | -$541k | +$0 bull / -$25k bear | out (clean 31, ADX 28, RVol 0.8) |
| 18 | **DELL** | 487.79 | - | **-** | 16 | - | POS +$12.7M | 477.93 | 500 | 500 | -$140k | +$0 bull / -$26k bear | out (clean 30, ADX 30, RVol 0.3) |
| 19 | **NFLX** | 61.90 | - | **-** | 15 | - | NEG -$46.8M | 65.35 | 63 | 61 | -$495k | - | out (clean 31, ADX 32, RVol 0.8) |
| 20 | **CRM** | 230.13 | - | **-** | 14 | - | NEG -$19.8M | - | 240 | 230 | -$189k | - | out (clean 27, ADX 34, RVol 0.8) |
| 21 | **BABA** | 99.97 | - | **-** | 13 | - | NEG -$15.6M | 102.21 | 102 | 100 | -$92k | - | out (clean 28, ADX 16, RVol 0.6) |
| 22 | **SHOP** | 166.99 | - | **-** | 12 | - | NEG -$5.8M | 171.97 | 175 | 165 | -$68k | - | out (clean 26, ADX 10, RVol 0.3) |
| 23 | **COIN** | 160.91 | - | **-** | 10 | - | POS +$5.1M | 153.36 | 170 | 155 | -$212k | - | out (clean 26, ADX 19, RVol 1.4) |
| 24 | **SMCI** | 35.40 | - | **-** | 10 | - | POS +$26.4M | - | 35 | 35 | +$131k | - | out (clean 26, ADX 16, RVol 1.0) |
| 25 | **HOOD** | 91.53 | - | **-** | 9 | - | NEG -$21.7M | - | 95 | 90 | -$972k | - | out (clean 28, ADX 12, RVol 0.9) |
| 26 | **PLTR** | 194.31 | - | **-** | 8 | - | POS +$22.8M | 191.82 | 200 | 190 | -$478k | - | out (clean 25, ADX 11, RVol 2.4) |
| 27 | **SMH** | 562.69 | - | **-** | 5 | - | NEG -$13.9M | 563.6 | 570 | 555 | +$91k | - | out (clean 26, ADX 12, RVol 1.0) |

## Big prints this scan (88)
- **MU** CALL 940 2026-11-02 (4DTE): 475 @ 24.35 = **+$1.2M** SELL | vol 693 / OI 115
- **MU** CALL 940 2026-10-30 (1DTE): 475 @ 18.95 = **+$900k** SELL | vol 3,556 / OI 2,522
- **SPY** PUT 775 2026-11-02 (4DTE): 500 @ 7.72 = **+$386k** BUY | vol 10,958 / OI 149
- **SPY** PUT 775 2026-11-02 (4DTE): 499 @ 7.72 = **+$385k** BUY | vol 10,958 / OI 149
- **QQQ** CALL 707 2026-11-02 (4DTE): 180 @ 10.00 = **+$180k** SELL | vol 434 / OI 58
- **SPY** PUT 765 2026-10-30 (1DTE): 1,000 @ 1.67 = **+$167k** BUY | vol 28,946 / OI 45,690
- **SPY** PUT 765 2026-10-30 (1DTE): 1,000 @ 1.67 = **+$167k** BUY | vol 28,946 / OI 45,690
- **AAPL** CALL 350 2026-11-04 (6DTE): 225 @ 6.60 = **+$148k** MID | vol 1,186 / OI 863
- **SPY** PUT 765 2026-10-30 (1DTE): 878 @ 1.68 = **+$148k** BUY | vol 28,946 / OI 45,690
- **MU** CALL 945 2026-11-04 (6DTE): 50 @ 28.81 = **+$144k** SELL | vol 138 / OI 85
- **MSFT** PUT 550 2026-10-30 (1DTE): 48 @ 29.27 = **+$140k** BUY | vol 582 / OI 199
- **SPY** PUT 765 2026-10-30 (1DTE): 874 @ 1.53 = **+$134k** BUY | vol 28,946 / OI 45,690
- **SPY** PUT 765 2026-10-30 (1DTE): 881 @ 1.45 = **+$128k** BUY | vol 28,946 / OI 45,690
- **GOOGL** PUT 280 2026-11-02 (4DTE): 500 @ 2.50 = **+$125k** BUY | vol 4,208 / OI 63
- **QQQ** PUT 725 2026-10-30 (1DTE): 100 @ 12.41 = **+$124k** BUY | vol 2,966 / OI 25,057

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 760 2026-11-02 (4DTE): 2,274 traded vs OI 2,198
- **SPY** PUT 771 2026-11-02 (4DTE): 520 traded vs OI 452
- **SPY** CALL 781 2026-11-04 (6DTE): 520 traded vs OI 107
- **SPY** PUT 761 2026-11-02 (4DTE): 519 traded vs OI 354
- **SPY** CALL 745 2026-11-06 (8DTE): 925 traded vs OI 237
- **SPY** PUT 760 2026-11-06 (8DTE): 13,992 traded vs OI 12,746
- **SPY** PUT 750 2026-11-12 (14DTE): 597 traded vs OI 0
- **SPY** PUT 768 2026-11-20 (22DTE): 5,916 traded vs OI 4,797
- **QQQ** CALL 712 2026-10-30 (1DTE): 2,243 traded vs OI 2,228
- **QQQ** CALL 715 2026-10-30 (1DTE): 11,271 traded vs OI 10,337
- **QQQ** CALL 728 2026-11-02 (4DTE): 501 traded vs OI 173
- **QQQ** CALL 727 2026-10-30 (1DTE): 2,757 traded vs OI 2,697
- **QQQ** CALL 722 2026-11-02 (4DTE): 500 traded vs OI 388
- **QQQ** PUT 652 2026-10-30 (1DTE): 5,016 traded vs OI 2,389
- **QQQ** CALL 720 2026-11-10 (12DTE): 536 traded vs OI 34

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
