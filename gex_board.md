# GEX + FLOW SCAN - Mon Nov 02, 10:30 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:30:08 ET, last candle SPY 10:29, QQQ 10:29 | no errors

## Flow surges NOT fired - price disagreed (4 today, last 5)
- 10:25 SPY PUTS: price +2.69 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:10 BABA PUTS: over EMA 20 - flow says one way, price says the other
- 10:05 BABA PUTS: over EMA 20 - flow says one way, price says the other
- 09:50 BABA PUTS: price +0.75 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **BABA** | 103.75 | TREND (flow not with it) | **CALLS** | 59 | 11/06 108C @ 0.80 (delta 0.24) = est +26% at 105 | POS +$3.1M | 100.94 | 105 | 100 | -$1.3M | - | LONG (clean 33, ADX 58, RVol 3.0) |
| 2 | **TSLA** | 410.83 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 45 | none: 132 puts 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (55 contracts' greeks worked out here) | POS +$297.6M | - | 410 | 400 | -$49.3M | +$0 bull / -$5.3M bear | out (clean 29, ADX 31, RVol 1.2) |
| 3 | **SPY** | 763.63 | FLOW SURGE | **PUTS** | 44 | 11/02 760P @ 0.58 (delta 0.22) = est +90% at 761.06 | NEG -$8.1B | 775.42 | 770 | 750 | -$108.3M | +$0 bull / -$3.9M bear | out (clean 30, ADX 47, RVol 1.0) |
| 4 | **MSFT** | 529.14 | PINNED between the walls (positive gamma) - chop | **-** | 41 | - | POS +$445.5M | 499.06 | 530 | 530 | -$5.6M | +$0 bull / -$122k bear | out (clean 26, ADX 26, RVol 0.9) |
| 5 | **AMZN** | 252.76 | - | **-** | 30 | - | POS +$118.6M | 242.44 | 250 | 250 | -$21.5M | +$0 bull / -$732k bear | out (clean 32, ADX 60, RVol 1.2) |
| 6 | **GOOGL** | 285.65 | TREND (flow not with it) | **CALLS** | 29 | 11/02 287.5C @ 0.53 (delta 0.28) = est +385% at 290 | NEG -$71.6M | - | 285 | 290 | -$1.1M | +$69k bull / -$154k bear | LONG (clean 34, ADX 51, RVol 1.0) |
| 7 | **AVGO** | 333.48 | - | **-** | 29 | - | NEG -$76.6M | - | 340 | 330 | -$5.4M | +$0 bull / -$302k bear | out (clean 31, ADX 51, RVol 0.8) |
| 8 | **MSTR** | 135.41 | - | **-** | 28 | - | POS +$3.6M | - | 135 | 125 | +$2.4M | +$230k bull / -$363k bear | out (clean 27, ADX 42, RVol 1.8) |
| 9 | **QQQ** | 699.29 | - | **-** | 27 | - | NEG -$5.6B | 732.15 | 720 | 700 | -$57.2M | +$0 bull / -$448k bear | out (clean 30, ADX 41, RVol 1.7) |
| 10 | **SMH** | 532.49 | - | **-** | 26 | - | NEG -$291.2M | - | 532.5 | 500 | +$1.5M | +$0 bull / -$54k bear | out (clean 32, ADX 43, RVol 0.9) |
| 11 | **PLTR** | 187.30 | - | **-** | 26 | - | NEG -$9.9M | - | 200 | 180 | -$2.4M | +$0 bull / -$99k bear | out (clean 26, ADX 15, RVol 3.0) |
| 12 | **NFLX** | 61.81 | - | **-** | 25 | - | NEG -$25.5M | - | 63 | 60 | +$444k | +$36k bull / -$57k bear | out (clean 30, ADX 25, RVol 1.5) |
| 13 | **ORCL** | 124.45 | - | **-** | 25 | - | NEG -$39.1M | - | 130 | 120 | -$1.9M | +$0 bull / -$189k bear | out (clean 33, ADX 38, RVol 1.3) |
| 14 | **UBER** | 67.31 | - | **-** | 25 | - | NEG -$8.3M | - | 70 | 65 | -$371k | - | out (clean 28, ADX 50, RVol 1.2) |
| 15 | **MU** | 885.27 | - | **-** | 24 | - | NEG -$218.2M | - | 910 | 900 | +$21.6M | +$0 bull / -$3.9M bear | out (clean 30, ADX 29, RVol 1.2) |
| 16 | **AAPL** | 340.36 | - | **-** | 23 | - | POS +$43.6M | 336.97 | 350 | 330 | +$4.8M | +$388k bull / -$525k bear | out (clean 32, ADX 29, RVol 1.4) |
| 17 | **HOOD** | 86.55 | - | **-** | 23 | - | NEG -$9.3M | - | 93 | 90 | -$573k | +$29k bull / +$0 bear | out (clean 32, ADX 58, RVol 0.5) |
| 18 | **NVDA** | 209.78 | - | **-** | 21 | - | NEG -$155.3M | 215.12 | 210 | 210 | -$3.4M | +$0 bull / -$860k bear | out (clean 30, ADX 38, RVol 1.4) |
| 19 | **AMD** | 507.42 | - | **-** | 21 | - | NEG -$96.9M | - | 550 | 500 | +$1.7M | +$25k bull / -$889k bear | out (clean 30, ADX 36, RVol 1.8) |
| 20 | **META** | 619.11 | - | **-** | 21 | - | NEG -$90.5M | 627.32 | 650 | 610 | -$4.6M | +$2.3M bull / -$51k bear | out (clean 29, ADX 34, RVol 0.6) |
| 21 | **SHOP** | 158.98 | - | **-** | 17 | - | NEG -$330k | - | 170 | 160 | -$72k | - | out (clean 28, ADX 36, RVol 2.8) |
| 22 | **DELL** | 418.73 | - | **-** | 16 | - | NEG -$24.2M | - | 440 | 400 | -$148k | +$0 bull / -$185k bear | out (clean 34, ADX 21, RVol 0.9) |
| 23 | **CRM** | 231.25 | - | **-** | 16 | - | NEG -$5.2M | 241.73 | 240 | 220 | +$75k | - | out (clean 28, ADX 21, RVol 1.5) |
| 24 | **SMCI** | 33.44 | - | **-** | 14 | - | POS +$811k | - | 35 | 33 | -$97k | - | out (clean 32, ADX 48, RVol 1.3) |
| 25 | **ARM** | 206.69 | - | **-** | 14 | - | NEG -$6.4M | - | 220 | 200 | +$230k | - | out (clean 26, ADX 22, RVol 0.7) |
| 26 | **IWM** | 283.04 | - | **-** | 12 | - | NEG -$732.3M | 286.45 | 285 | 270 | -$1.4M | - | out (clean 31, ADX 47, RVol 1.1) |
| 27 | **COIN** | 141.22 | - | **-** | 12 | - | NEG -$8.9M | - | 150 | 130 | -$42k | - | out (clean 26, ADX 34, RVol 2.3) |

## Big prints this scan (123)
- **SPY** CALL 761 2026-11-03 (1DTE): 1,350 @ 3.00 = **+$405k** SELL | vol 10,193 / OI 121
- **SPY** CALL 762 2026-11-03 (1DTE): 1,350 @ 2.47 = **+$333k** SELL | vol 10,023 / OI 183
- **TSLA** PUT 405 2026-11-06 (4DTE): 229 @ 8.90 = **+$204k** BUY | vol 1,226 / OI 1,523
- **AAPL** PUT 337.5 2026-11-06 (4DTE): 274 @ 6.50 = **+$178k** MID | vol 2,409 / OI 600
- **SPY** PUT 759 2026-11-04 (2DTE): 500 @ 3.45 = **+$172k** BUY | vol 2,629 / OI 1,289
- **AAPL** PUT 337.5 2026-11-06 (4DTE): 241 @ 6.50 = **+$157k** MID | vol 2,409 / OI 600
- **AAPL** PUT 337.5 2026-11-06 (4DTE): 233 @ 6.50 = **+$151k** MID | vol 2,409 / OI 600
- **ORCL** CALL 124 2026-11-06 (4DTE): 400 @ 3.60 = **+$144k** SELL | vol 1,646 / OI 139
- **TSLA** CALL 400 2026-11-06 (4DTE): 100 @ 13.00 = **+$130k** SELL | vol 3,137 / OI 4,780
- **SPY** CALL 751 2026-11-06 (4DTE): 95 @ 13.46 = **+$128k** SELL | vol 148 / OI 49
- **TSLA** CALL 400 2026-11-04 (2DTE): 100 @ 11.65 = **+$116k** SELL | vol 3,740 / OI 612
- **SPY** CALL 750 2026-11-02 (0DTE): 100 @ 11.30 = **+$113k** SELL | vol 885 / OI 75
- **MU** PUT 870 2026-11-02 (0DTE): 195 @ 5.70 = **+$111k** BUY | vol 6,949 / OI 677
- **QQQ** PUT 695 2026-11-04 (2DTE): 172 @ 6.45 = **+$111k** BUY | vol 2,085 / OI 2,938
- **MSTR** PUT 136 2026-11-06 (4DTE): 197 @ 5.45 = **+$107k** SELL | vol 578 / OI 424

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 710 2026-11-09 (7DTE): 528 traded vs OI 112
- **SPY** PUT 764 2026-11-02 (0DTE): 1,894 traded vs OI 1,448
- **SPY** CALL 773 2026-11-03 (1DTE): 664 traded vs OI 608
- **SPY** PUT 705 2026-11-05 (3DTE): 505 traded vs OI 489
- **SPY** PUT 736 2026-11-02 (0DTE): 1,983 traded vs OI 911
- **SPY** PUT 766 2026-11-02 (0DTE): 1,363 traded vs OI 1,093
- **SPY** PUT 742 2026-11-02 (0DTE): 1,478 traded vs OI 1,336
- **SPY** CALL 765 2026-11-05 (3DTE): 1,283 traded vs OI 1,173
- **SPY** CALL 781 2026-11-04 (2DTE): 1,175 traded vs OI 335
- **SPY** PUT 747 2026-11-03 (1DTE): 519 traded vs OI 226
- **SPY** CALL 774 2026-11-03 (1DTE): 998 traded vs OI 915
- **QQQ** CALL 718 2026-11-02 (0DTE): 1,088 traded vs OI 987
- **QQQ** CALL 714 2026-11-02 (0DTE): 842 traded vs OI 826
- **QQQ** CALL 698 2026-11-04 (2DTE): 529 traded vs OI 0
- **QQQ** PUT 684 2026-11-03 (1DTE): 674 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
