# GEX + FLOW SCAN - Fri Oct 30, 10:15 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (1)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:15 | **AAPL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 10/30 347.5C | 0.50 | 0.44 | -12% (0m) | **-12%** | +104% | 347.56 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **AAPL** | 345.57 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 48 | 10/30 347.5C @ 0.50 (delta 0.26) = est +104% at 347.56 | POS +$395.5M | 342.34 | 350 | 345 | +$0 | +$150k bull / -$1.9M bear | out (clean 30, ADX 50, RVol 2.1) |
| 2 | **COIN** | 139.57 | - | **-** | 23 | - | NEG -$13.7M | - | 150 | 140 | +$0 | +$54k bull / +$0 bear | out (clean 27, ADX 48, RVol 2.9) |
| 3 | **DELL** | 432.59 | - | **-** | 23 | - | NEG -$56.6M | - | 440 | 425 | +$0 | +$31k bull / +$0 bear | out (clean 32, ADX 47, RVol 2.9) |
| 4 | **QQQ** | 694.23 | - | **-** | 22 | - | NEG -$9.0B | 718.33 | 720 | 690 | +$0 | +$2.7M bull / +$0 bear | out (clean 27, ADX 43, RVol 2.3) |
| 5 | **AMD** | 513.31 | - | **-** | 22 | - | NEG -$86.5M | 524.36 | 527.5 | 500 | +$0 | +$35k bull / -$185k bear | out (clean 28, ADX 39, RVol 4.8) |
| 6 | **AVGO** | 328.56 | - | **-** | 22 | - | NEG -$118.5M | 341.31 | 330 | 330 | +$0 | +$0 bull / -$61k bear | out (clean 29, ADX 41, RVol 2.7) |
| 7 | **MSTR** | 127.43 | - | **-** | 22 | - | NEG -$30.8M | - | 135 | 125 | +$0 | +$231k bull / +$0 bear | out (clean 26, ADX 40, RVol 5.2) |
| 8 | **ARM** | 205.51 | - | **-** | 22 | - | NEG -$17.3M | 216.86 | 220 | 205 | +$0 | +$368k bull / +$0 bear | out (clean 25, ADX 40, RVol 4.8) |
| 9 | **SPY** | 758.60 | - | **-** | 21 | - | NEG -$12.7B | 770.29 | 770 | 760 | +$0 | +$103k bull / +$0 bear | out (clean 27, ADX 40, RVol 2.2) |
| 10 | **NVDA** | 206.86 | - | **-** | 21 | - | NEG -$345.7M | 211.52 | 210 | 210 | +$0 | +$180k bull / +$0 bear | out (clean 25, ADX 40, RVol 2.1) |
| 11 | **PLTR** | 187.27 | - | **-** | 21 | - | NEG -$53.7M | 192.82 | 200 | 190 | +$0 | +$32k bull / +$0 bear | out (clean 26, ADX 33, RVol 3.7) |
| 12 | **MU** | 890.56 | - | **-** | 21 | - | NEG -$192.1M | 912 | 900 | 900 | +$0 | +$2.7M bull / +$0 bear | out (clean 29, ADX 41, RVol 1.8) |
| 13 | **IWM** | 280.14 | - | **-** | 20 | - | NEG -$620.2M | 281.37 | 280 | 270 | +$0 | +$89k bull / +$0 bear | out (clean 27, ADX 36, RVol 1.6) |
| 14 | **AMZN** | 237.23 | - | **-** | 20 | - | NEG -$176.1M | 245.08 | 250 | 240 | +$0 | +$390k bull / +$0 bear | out (clean 32, ADX 29, RVol 4.6) |
| 15 | **TSLA** | 396.49 | - | **-** | 19 | - | POS +$361.3M | 383.02 | 400 | 400 | +$0 | +$0 bull / -$1.0M bear | out (clean 28, ADX 34, RVol 1.8) |
| 16 | **MSFT** | 521.63 | - | **-** | 19 | - | POS +$445.2M | 513.53 | 525 | 525 | +$0 | +$702k bull / -$136k bear | out (clean 27, ADX 26, RVol 2.1) |
| 17 | **GOOGL** | 279.84 | - | **-** | 19 | - | NEG -$214.1M | - | 280 | 280 | +$0 | +$120k bull / +$0 bear | out (clean 31, ADX 32, RVol 1.6) |
| 18 | **META** | 617.16 | - | **-** | 17 | - | NEG -$85.9M | 621.39 | 625 | 625 | +$0 | +$445k bull / +$0 bear | out (clean 28, ADX 28, RVol 1.0) |
| 19 | **NFLX** | 62.74 | - | **-** | 17 | - | NEG -$13.6M | 63.17 | 63 | 63 | +$0 | +$0 bull / -$26k bear | out (clean 31, ADX 30, RVol 1.0) |
| 20 | **CRM** | 230.30 | - | **-** | 16 | - | NEG -$22.0M | 237.18 | 240 | 230 | +$0 | +$36k bull / +$0 bear | out (clean 28, ADX 21, RVol 1.2) |
| 21 | **SMH** | 528.49 | - | **-** | 13 | - | NEG -$515.7M | 546.75 | 532.5 | 530 | +$0 | - | out (clean 28, ADX 43, RVol 3.5) |
| 22 | **SMCI** | 32.67 | - | **-** | 13 | - | POS +$1.6M | 32.45 | 35 | 32 | +$0 | - | out (clean 28, ADX 48, RVol 2.3) |
| 23 | **HOOD** | 83.66 | - | **-** | 13 | - | NEG -$31.3M | - | 85 | 85 | +$0 | - | out (clean 31, ADX 48, RVol 4.8) |
| 24 | **SHOP** | 158.81 | - | **-** | 9 | - | NEG -$13.5M | - | 160 | 157.5 | +$0 | - | out (clean 25, ADX 38, RVol 1.1) |
| 25 | **ORCL** | 133.52 | - | **-** | 7 | - | POS +$68.8M | 130.02 | 135 | 130 | +$0 | - | out (clean 32, ADX 30, RVol 1.0) |
| 26 | **BABA** | 98.41 | - | **-** | 6 | - | NEG -$35.0M | 100.16 | 100 | 98 | +$0 | - | out (clean 29, ADX 20, RVol 1.4) |
| 27 | **UBER** | 65.26 | - | **-** | 5 | - | NEG -$30.0M | 66.63 | 67 | 65 | +$0 | - | out (clean 28, ADX 17, RVol 0.9) |

## Big prints this scan (154)
- **QQQ** PUT 705 2026-11-06 (7DTE): 680 @ 14.06 = **+$956k** SELL | vol 2,373 / OI 5,161
- **QQQ** PUT 705 2026-11-06 (7DTE): 600 @ 14.07 = **+$844k** SELL | vol 2,373 / OI 5,161
- **AAPL** CALL 347.5 2026-11-06 (7DTE): 600 @ 6.50 = **+$390k** SELL | vol 3,263 / OI 563
- **AAPL** CALL 347.5 2026-11-06 (7DTE): 600 @ 6.50 = **+$390k** SELL | vol 3,263 / OI 563
- **QQQ** PUT 700 2026-11-06 (7DTE): 300 @ 11.32 = **+$340k** SELL | vol 4,866 / OI 23,974
- **AAPL** CALL 347.5 2026-11-06 (7DTE): 446 @ 6.50 = **+$290k** SELL | vol 3,263 / OI 563
- **ARM** PUT 200 2026-11-06 (7DTE): 342 @ 8.37 = **+$286k** SELL | vol 2,646 / OI 1,811
- **AAPL** CALL 347.5 2026-11-06 (7DTE): 433 @ 6.50 = **+$281k** SELL | vol 3,263 / OI 563
- **MU** CALL 880 2026-11-02 (3DTE): 95 @ 28.20 = **+$268k** BUY | vol 809 / OI 316
- **MU** CALL 880 2026-10-30 (0DTE): 100 @ 21.67 = **+$217k** BUY | vol 2,158 / OI 1,469
- **META** CALL 620 2026-10-30 (0DTE): 501 @ 4.00 = **+$200k** BUY | vol 8,200 / OI 1,308
- **MSTR** CALL 127 2026-11-06 (7DTE): 270 @ 7.15 = **+$193k** BUY | vol 794 / OI 34
- **AAPL** CALL 347.5 2026-11-06 (7DTE): 296 @ 6.50 = **+$192k** SELL | vol 3,263 / OI 563
- **QQQ** PUT 700 2026-10-30 (0DTE): 500 @ 3.65 = **+$182k** SELL | vol 18,490 / OI 42,068
- **MU** CALL 900 2026-10-30 (0DTE): 200 @ 8.24 = **+$165k** BUY | vol 16,527 / OI 2,857

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 764 2026-11-02 (3DTE): 2,267 traded vs OI 283
- **SPY** CALL 760 2026-11-06 (7DTE): 5,144 traded vs OI 1,347
- **SPY** PUT 754 2026-11-02 (3DTE): 1,262 traded vs OI 800
- **SPY** CALL 765 2026-11-04 (5DTE): 537 traded vs OI 357
- **SPY** CALL 768 2026-10-30 (0DTE): 20,843 traded vs OI 4,169
- **SPY** CALL 760 2026-10-30 (0DTE): 39,770 traded vs OI 6,108
- **SPY** CALL 768 2026-11-02 (3DTE): 4,741 traded vs OI 389
- **SPY** PUT 752 2026-11-02 (3DTE): 1,479 traded vs OI 332
- **SPY** CALL 761 2026-11-04 (5DTE): 1,847 traded vs OI 168
- **SPY** PUT 760 2026-11-02 (3DTE): 11,226 traded vs OI 5,269
- **SPY** CALL 775 2026-11-03 (4DTE): 755 traded vs OI 564
- **SPY** PUT 761 2026-10-30 (0DTE): 33,989 traded vs OI 5,997
- **SPY** CALL 758 2026-10-30 (0DTE): 6,390 traded vs OI 406
- **SPY** PUT 747 2026-11-02 (3DTE): 1,563 traded vs OI 536
- **SPY** PUT 759 2026-11-02 (3DTE): 4,204 traded vs OI 2,269

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
