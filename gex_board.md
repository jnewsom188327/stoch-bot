# GEX + FLOW SCAN - Wed Oct 28, 10:40 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (1)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:20 | **IWM** | **CALLS** | FLOW SURGE | 10/29 284C | 0.47 | 0.34 | +11% (0m) | **-28%** | +27% | 281.41 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **IWM** | 279.95 | FLOW SURGE | **CALLS** | 49 | 10/29 283C @ 0.57 (delta 0.24) = est +23% at 280.67 | NEG -$413.0M | 281.46 | 280 | 270 | +$6.4M | +$286k bull / +$0 bear | out (clean 23, ADX 20, RVol 1.7) |
| 2 | **PLTR** | 195.59 | FLOW SURGE | **PUTS** | 43 | none: 16 puts 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$56.8M | 188.64 | 200 | 190 | -$2.0M | +$32k bull / -$160k bear | out (clean 28, ADX 51, RVol 0.9) |
| 3 | **META** | 613.00 | FLOW SURGE | **CALLS** | 42 | none: 179 calls 0-7DTE > 12 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (78 contracts' greeks worked out here) | NEG -$255.1M | 636.33 | 650 | 600 | +$7.1M | +$1.6M bull / +$0 bear | out (clean 28, ADX 27, RVol 1.0) |
| 4 | **TSLA** | 399.31 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 38 | 10/28 395P @ 0.78 (delta 0.23) = est +146% at 395 | POS +$548.5M | - | 400 | 395 | +$252k | +$692k bull / -$2.3M bear | out (clean 28, ADX 34, RVol 1.0) |
| 5 | **AAPL** | 344.78 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 37 | none: 81 calls 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (46 contracts' greeks worked out here) | POS +$315.4M | 341.1 | 350 | 345 | -$88k | +$0 bull / -$28k bear | out (clean 30, ADX 31, RVol 0.9) |
| 6 | **MSTR** | 139.79 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 33 | none: 26 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$17.3M | - | 152.5 | 140 | -$192k | +$0 bull / -$226k bear | out (clean 29, ADX 11, RVol 0.3) |
| 7 | **GOOGL** | 323.94 | - | **-** | 25 | - | POS +$13.3M | 321.02 | 355 | 330 | +$936k | +$180k bull / -$154k bear | out (clean 33, ADX 28, RVol 1.2) |
| 8 | **HOOD** | 90.94 | - | **-** | 25 | - | NEG -$17.1M | - | 100 | 90 | +$1.5M | - | out (clean 31, ADX 45, RVol 1.6) |
| 9 | **MU** | 966.92 | - | **-** | 24 | - | POS +$599.1M | - | 950 | 950 | +$23.1M | +$4.9M bull / -$1.2M bear | out (clean 28, ADX 35, RVol 0.8) |
| 10 | **UBER** | 64.82 | - | **-** | 24 | - | NEG -$32.1M | - | 70 | 65 | +$68k | - | out (clean 27, ADX 35, RVol 0.9) |
| 11 | **SHOP** | 166.75 | - | **-** | 23 | - | NEG -$4.3M | 171.87 | 175 | 165 | +$14k | - | out (clean 26, ADX 17, RVol 1.1) |
| 12 | **DELL** | 494.57 | - | **-** | 22 | - | POS +$29.5M | - | 500 | 500 | +$210k | +$29k bull / -$139k bear | out (clean 30, ADX 29, RVol 0.6) |
| 13 | **ORCL** | 130.61 | - | **-** | 22 | - | POS +$10.8M | 126.65 | 135 | 130 | -$172k | +$0 bull / -$104k bear | out (clean 28, ADX 12, RVol 1.2) |
| 14 | **AVGO** | 345.64 | - | **-** | 21 | - | POS +$51.9M | 336.55 | 350 | 340 | +$961k | +$0 bull / -$152k bear | out (clean 30, ADX 22, RVol 0.9) |
| 15 | **CRM** | 241.90 | - | **-** | 20 | - | POS +$7.1M | 233.93 | 260 | 240 | +$29k | - | out (clean 27, ADX 16, RVol 1.1) |
| 16 | **AMZN** | 252.82 | - | **-** | 19 | - | POS +$191.4M | 239.25 | 255 | 250 | +$595k | +$389k bull / -$173k bear | out (clean 32, ADX 18, RVol 0.8) |
| 17 | **MSFT** | 529.41 | - | **-** | 19 | - | POS +$468.5M | - | 550 | 500 | +$339k | +$0 bull / -$1.2M bear | out (clean 30, ADX 18, RVol 1.3) |
| 18 | **AMD** | 562.75 | - | **-** | 18 | - | POS +$175.5M | - | 550 | 550 | +$1.4M | +$0 bull / -$366k bear | out (clean 28, ADX 21, RVol 0.7) |
| 19 | **SMCI** | 34.97 | PINNED between the walls (positive gamma) - chop | **-** | 18 | - | POS +$18.8M | - | 35 | 35 | +$8k | - | out (clean 27, ADX 18, RVol 0.6) |
| 20 | **SPY** | 770.35 | - | **-** | 16 | - | NEG -$3.2B | 773.55 | 780 | 750 | -$6.5M | +$727k bull / -$1.0M bear | out (clean 30, ADX 15, RVol 0.7) |
| 21 | **QQQ** | 721.39 | - | **-** | 16 | - | NEG -$1.9B | 727.9 | 720 | 720 | -$6.6M | +$237k bull / -$485k bear | out (clean 30, ADX 15, RVol 0.7) |
| 22 | **NVDA** | 217.84 | - | **-** | 15 | - | POS +$577.9M | 209.77 | 220 | 215 | -$768k | +$239k bull / -$942k bear | out (clean 27, ADX 13, RVol 0.7) |
| 23 | **COIN** | 157.90 | - | **-** | 15 | - | POS +$1.3M | 154.93 | 170 | 150 | +$47k | - | out (clean 30, ADX 23, RVol 0.7) |
| 24 | **NFLX** | 61.66 | - | **-** | 10 | - | NEG -$56.7M | - | 65 | 60 | -$35k | - | out (clean 32, ADX 42, RVol 0.5) |
| 25 | **BABA** | 100.27 | - | **-** | 10 | - | NEG -$13.4M | 103.23 | 102 | 100 | +$9k | - | out (clean 29, ADX 27, RVol 0.5) |
| 26 | **SMH** | 563.47 | - | **-** | 9 | - | POS +$38.5M | 559.53 | 570 | 555 | +$70k | - | out (clean 28, ADX 32, RVol 0.8) |
| 27 | **ARM** | 231.51 | - | **-** | 9 | - | POS +$2.0M | 222.34 | 220 | 250 | +$49k | - | out (clean 26, ADX 30, RVol 0.6) |

## Big prints this scan (72)
- **MU** CALL 990 2026-10-30 (2DTE): 694 @ 12.03 = **+$835k** BUY | vol 1,791 / OI 3,193
- **MU** CALL 1,000 2026-10-30 (2DTE): 694 @ 8.88 = **+$616k** BUY | vol 7,751 / OI 8,792
- **MSFT** CALL 550 2026-10-30 (2DTE): 800 @ 5.37 = **+$430k** SELL | vol 1,360 / OI 7,100
- **SPY** CALL 770 2026-10-28 (0DTE): 1,189 @ 2.70 = **+$321k** BUY | vol 52,179 / OI 3,329
- **MSFT** CALL 530 2026-11-02 (5DTE): 200 @ 13.55 = **+$271k** SELL | vol 875 / OI 2,275
- **MSFT** CALL 530 2026-11-02 (5DTE): 200 @ 13.55 = **+$271k** SELL | vol 875 / OI 2,275
- **MSFT** CALL 530 2026-11-02 (5DTE): 200 @ 13.55 = **+$271k** SELL | vol 875 / OI 2,275
- **QQQ** CALL 725 2026-10-30 (2DTE): 500 @ 4.74 = **+$237k** BUY | vol 4,762 / OI 12,148
- **SPY** CALL 770 2026-10-28 (0DTE): 654 @ 2.70 = **+$177k** BUY | vol 52,179 / OI 3,329
- **QQQ** CALL 720 2026-11-03 (6DTE): 185 @ 9.35 = **+$173k** MID | vol 651 / OI 584
- **QQQ** CALL 730 2026-10-30 (2DTE): 500 @ 2.76 = **+$138k** SELL | vol 2,061 / OI 13,989
- **SPY** PUT 770 2026-10-28 (0DTE): 625 @ 1.99 = **+$124k** SELL | vol 92,437 / OI 1,789
- **MU** CALL 960 2026-10-30 (2DTE): 48 @ 25.80 = **+$124k** BUY | vol 1,308 / OI 2,586
- **META** PUT 622.5 2026-10-30 (2DTE): 58 @ 13.20 = **+$77k** SELL | vol 177 / OI 181
- **ORCL** PUT 125 2026-10-30 (2DTE): 319 @ 2.02 = **+$64k** MID | vol 597 / OI 8,023

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 705 2026-11-02 (5DTE): 506 traded vs OI 161
- **SPY** PUT 760 2026-10-29 (1DTE): 1,902 traded vs OI 1,798
- **QQQ** CALL 720 2026-11-03 (6DTE): 651 traded vs OI 584
- **QQQ** CALL 716 2026-10-28 (0DTE): 639 traded vs OI 528
- **QQQ** CALL 722 2026-10-30 (2DTE): 1,867 traded vs OI 1,865
- **QQQ** CALL 738 2026-10-29 (1DTE): 1,366 traded vs OI 1,231
- **QQQ** CALL 717 2026-10-28 (0DTE): 1,127 traded vs OI 1,087
- **IWM** CALL 287 2026-11-05 (8DTE): 653 traded vs OI 8
- **NVDA** CALL 215 2026-10-28 (0DTE): 4,592 traded vs OI 4,474
- **TSLA** CALL 415 2026-10-30 (2DTE): 6,004 traded vs OI 5,992
- **TSLA** PUT 395 2026-11-04 (7DTE): 519 traded vs OI 148
- **AMD** PUT 542.5 2026-10-28 (0DTE): 501 traded vs OI 75
- **AMD** PUT 560 2026-10-30 (2DTE): 984 traded vs OI 961
- **NFLX** CALL 60 2026-11-06 (9DTE): 1,344 traded vs OI 173
- **PLTR** CALL 215 2026-10-30 (2DTE): 818 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
