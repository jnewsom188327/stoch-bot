# GEX + FLOW SCAN - Thu Oct 29, 10:20 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (3)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:00 | **ORCL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 10/30 145C | 0.79 | 0.72 | +9% (2m) | **-9%** | +139% | 143.92 |
| 09:55 | **AAPL** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 10/30 345P | 0.77 | 0.60 | +17% (2m) | **-22%** | +198% | 345 |
| 09:50 | **IWM** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 10/29 283P | 0.50 | 0.28 | +20% (21m) | **-44%** | +159% | 282 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:20:08 ET, last candle SPY 10:19, QQQ 10:19 | no errors

## Flow surges NOT fired - price disagreed (2 today, last 5)
- 10:05 HOOD PUTS: price +0.99 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:00 HOOD PUTS: price +0.89 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **MSFT** | 524.63 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 67 | none: 126 puts 0-7DTE > 9 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (13 contracts' greeks worked out here) | POS +$505.5M | 499.43 | 525 | 530 | +$30.1M | +$3.7M bull / +$0 bear | out (clean 28, ADX 34, RVol 3.0) |
| 2 | **ARM** | 229.00 | FLOW SURGE | **CALLS** | 53 | none: 18 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (2 contracts' greeks worked out here) | POS +$3.2M | 222.63 | 227.5 | 240 | +$1.8M | +$2.6M bull / -$40k bear | out (clean 27, ADX 26, RVol 2.4) |
| 3 | **IWM** | 284.39 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 50 | none: 307 puts 0-7DTE > 17 priced 0.40-0.80 > 6 delta 0.2+ > 6 spread ok > 6 liquid > best one only +11% at the target (needs +20%) (131 contracts' greeks worked out here) | POS +$850.8M | 281.6 | 284 | 270 | -$3.9M | +$1.2M bull / -$600k bear | out (clean 25, ADX 50, RVol 1.8) |
| 4 | **AAPL** | 349.99 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 44 | none: 55 puts 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (7 contracts' greeks worked out here) | POS +$626.8M | 339.4 | 350 | 345 | +$4.1M | +$0 bull / -$903k bear | out (clean 29, ADX 38, RVol 1.3) |
| 5 | **AVGO** | 342.83 | FLIP CROSS up into positive gamma | **CALLS** | 41 | none: 81 calls 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$3.5M | 342.42 | 350 | 340 | +$2.6M | +$26k bull / -$32k bear | out (clean 29, ADX 37, RVol 0.7) |
| 6 | **ORCL** | 140.20 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 41 | 10/30 145C @ 0.80 (delta 0.23) = est +130% at 143.8 | POS +$120.3M | - | 135 | 140 | +$123k | +$240k bull / -$26k bear | out (clean 31, ADX 37, RVol 1.2) |
| 7 | **AMZN** | 246.12 | - | **-** | 32 | - | POS +$13.6M | 242.11 | 265 | 250 | -$7.4M | +$0 bull / -$2.2M bear | out (clean 31, ADX 47, RVol 2.3) |
| 8 | **GOOGL** | 285.76 | - | **-** | 29 | - | NEG -$197.3M | - | 300 | 290 | -$7.8M | +$464k bull / -$3.1M bear | out (clean 33, ADX 49, RVol 6.3) |
| 9 | **MU** | 954.87 | - | **-** | 24 | - | POS +$387.6M | - | 950 | 950 | +$18.2M | +$1.4M bull / -$4.2M bear | out (clean 29, ADX 36, RVol 1.1) |
| 10 | **META** | 623.22 | - | **-** | 23 | - | NEG -$81.9M | 630.44 | 650 | 625 | -$6.1M | +$676k bull / -$1.5M bear | out (clean 28, ADX 42, RVol 1.1) |
| 11 | **UBER** | 65.02 | - | **-** | 23 | - | NEG -$32.0M | - | 70 | 65 | -$152k | - | out (clean 28, ADX 30, RVol 0.6) |
| 12 | **QQQ** | 716.07 | - | **-** | 22 | - | NEG -$4.3B | 727.01 | 720 | 720 | -$52.1M | +$569k bull / -$2.4M bear | out (clean 28, ADX 27, RVol 1.4) |
| 13 | **NFLX** | 62.02 | - | **-** | 22 | - | NEG -$47.4M | - | 63 | 60 | -$559k | - | out (clean 30, ADX 39, RVol 1.3) |
| 14 | **NVDA** | 213.70 | - | **-** | 21 | - | POS +$216.6M | 210.74 | 215 | 210 | +$2.5M | +$507k bull / -$336k bear | out (clean 26, ADX 32, RVol 1.5) |
| 15 | **TSLA** | 404.10 | - | **-** | 21 | - | POS +$485.1M | - | 400 | 400 | -$9.6M | +$569k bull / -$1.1M bear | out (clean 29, ADX 27, RVol 0.9) |
| 16 | **AMD** | 569.90 | - | **-** | 21 | - | POS +$131.3M | - | 600 | 550 | +$848k | +$205k bull / -$1.1M bear | out (clean 29, ADX 39, RVol 1.9) |
| 17 | **SMCI** | 35.74 | - | **-** | 21 | - | POS +$26.9M | - | 37 | 35 | +$73k | +$0 bull / -$27k bear | out (clean 27, ADX 24, RVol 0.8) |
| 18 | **SPY** | 769.41 | - | **-** | 20 | - | NEG -$4.1B | 773.08 | 770 | 765 | -$39.6M | +$330k bull / -$5.0M bear | out (clean 27, ADX 18, RVol 1.1) |
| 19 | **DELL** | 490.62 | - | **-** | 20 | - | POS +$17.7M | 475.25 | 500 | 500 | +$659k | +$0 bull / -$109k bear | out (clean 31, ADX 28, RVol 0.8) |
| 20 | **MSTR** | 141.01 | - | **-** | 19 | - | POS +$24.2M | - | 152.5 | 140 | -$404k | +$61k bull / +$0 bear | out (clean 26, ADX 19, RVol 1.2) |
| 21 | **CRM** | 232.53 | - | **-** | 19 | - | NEG -$18.7M | - | 240 | 230 | -$298k | - | out (clean 27, ADX 28, RVol 0.9) |
| 22 | **BABA** | 99.61 | - | **-** | 19 | - | NEG -$16.6M | 102.28 | 102 | 100 | -$61k | - | out (clean 28, ADX 27, RVol 1.6) |
| 23 | **PLTR** | 195.44 | - | **-** | 17 | - | POS +$40.3M | 191.05 | 200 | 190 | -$117k | +$258k bull / +$0 bear | out (clean 26, ADX 16, RVol 2.1) |
| 24 | **SHOP** | 167.39 | - | **-** | 16 | - | NEG -$4.3M | 171.81 | 175 | 165 | -$52k | - | out (clean 26, ADX 16, RVol 0.9) |
| 25 | **HOOD** | 91.11 | - | **-** | 12 | - | NEG -$22.5M | - | 95 | 90 | -$1.0M | - | out (clean 28, ADX 13, RVol 1.4) |
| 26 | **SMH** | 562.02 | - | **-** | 11 | - | NEG -$12.6M | 563 | 560 | 555 | +$425k | - | out (clean 27, ADX 20, RVol 1.1) |
| 27 | **COIN** | 161.81 | - | **-** | 9 | - | POS +$7.5M | - | 170 | 155 | -$47k | - | out (clean 27, ADX 18, RVol 1.4) |

## Big prints this scan (135)
- **GOOGL** PUT 295 2026-10-30 (1DTE): 500 @ 10.70 = **+$535k** BUY | vol 5,190 / OI 5,774
- **GOOGL** PUT 290 2026-10-30 (1DTE): 500 @ 6.70 = **+$335k** BUY | vol 3,572 / OI 4,338
- **SPY** CALL 754 2026-10-29 (0DTE): 212 @ 15.56 = **+$330k** BUY | vol 303 / OI 45
- **GOOGL** PUT 285 2026-11-02 (4DTE): 500 @ 4.40 = **+$220k** BUY | vol 733 / OI 80
- **QQQ** CALL 710 2026-10-30 (1DTE): 200 @ 9.00 = **+$180k** BUY | vol 2,139 / OI 9,068
- **SPY** PUT 775 2026-11-02 (4DTE): 249 @ 7.01 = **+$175k** BUY | vol 5,125 / OI 149
- **QQQ** CALL 710 2026-10-30 (1DTE): 191 @ 9.00 = **+$172k** BUY | vol 2,139 / OI 9,068
- **SPY** PUT 775 2026-11-02 (4DTE): 240 @ 7.00 = **+$168k** BUY | vol 5,125 / OI 149
- **QQQ** PUT 716 2026-10-30 (1DTE): 386 @ 4.35 = **+$168k** BUY | vol 5,798 / OI 4,780
- **SPY** PUT 770 2026-11-02 (4DTE): 400 @ 4.08 = **+$163k** BUY | vol 1,611 / OI 1,156
- **META** CALL 632.5 2026-10-30 (1DTE): 432 @ 3.65 = **+$158k** BUY | vol 3,115 / OI 615
- **SPY** PUT 770 2026-11-02 (4DTE): 400 @ 3.82 = **+$153k** BUY | vol 1,611 / OI 1,156
- **GOOGL** PUT 300 2026-10-30 (1DTE): 100 @ 14.97 = **+$150k** BUY | vol 9,355 / OI 8,616
- **IWM** CALL 284 2026-10-30 (1DTE): 813 @ 1.71 = **+$139k** BUY | vol 11,854 / OI 20,104
- **SPY** CALL 756 2026-10-29 (0DTE): 100 @ 13.31 = **+$133k** MID | vol 1,829 / OI 25

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 767 2026-11-04 (6DTE): 576 traded vs OI 223
- **SPY** PUT 719 2026-10-30 (1DTE): 1,934 traded vs OI 1,239
- **SPY** PUT 778 2026-10-29 (0DTE): 508 traded vs OI 33
- **SPY** CALL 783 2026-10-29 (0DTE): 1,686 traded vs OI 1,265
- **SPY** CALL 780 2026-11-02 (4DTE): 1,131 traded vs OI 985
- **SPY** PUT 770 2026-11-02 (4DTE): 1,611 traded vs OI 1,156
- **SPY** PUT 769 2026-11-03 (5DTE): 1,222 traded vs OI 365
- **SPY** CALL 778 2026-11-02 (4DTE): 573 traded vs OI 319
- **SPY** CALL 769 2026-11-06 (8DTE): 1,222 traded vs OI 1,101
- **QQQ** PUT 718 2026-10-29 (0DTE): 3,402 traded vs OI 2,934
- **QQQ** PUT 684 2026-10-29 (0DTE): 502 traded vs OI 317
- **QQQ** PUT 708 2026-10-30 (1DTE): 2,745 traded vs OI 2,504
- **QQQ** PUT 716 2026-10-30 (1DTE): 5,798 traded vs OI 4,780
- **QQQ** CALL 731 2026-11-02 (4DTE): 510 traded vs OI 275
- **QQQ** PUT 676 2026-10-29 (0DTE): 1,252 traded vs OI 8

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
