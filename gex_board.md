# GEX + FLOW SCAN - Thu Oct 29, 10:00 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (3)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:00 | **ORCL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 10/30 145C | 0.79 | 0.74 | -6% (0m) | **-6%** | +139% | 143.92 |
| 09:55 | **AAPL** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 10/30 345P | 0.77 | 0.80 | +17% (2m) | **+4%** | +198% | 345 |
| 09:50 | **IWM** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 10/29 283P | 0.50 | 0.47 | +4% (7m) | **-6%** | +159% | 282 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:00:08 ET, last candle SPY 09:59, QQQ 09:59 | no errors

## Flow surges NOT fired - price disagreed (1 today, last 5)
- 10:00 HOOD PUTS: price +0.89 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **IWM** | 283.88 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 61 | 10/29 283P @ 0.40 (delta 0.31) = est +195% at 282 | POS +$745.6M | 281.79 | 284 | 270 | -$4.6M | +$0 bull / -$552k bear | out (clean 25, ADX 43, RVol 2.8) |
| 2 | **CRM** | 232.07 | FLOW SURGE | **PUTS** | 60 | none: 19 puts 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (7 contracts' greeks worked out here) | NEG -$17.2M | - | 240 | 230 | -$229k | +$0 bull / -$144k bear | out (clean 27, ADX 28, RVol 3.2) |
| 3 | **AAPL** | 349.73 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 57 | 10/30 345P @ 0.76 (delta 0.22) = est +195% at 345 | POS +$602.1M | 339.18 | 350 | 345 | +$9.1M | +$5.6M bull / -$856k bear | out (clean 28, ADX 29, RVol 2.7) |
| 4 | **GOOGL** | 284.56 | FLOW SURGE | **PUTS** | 57 | none: 51 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (3 contracts' greeks worked out here) | NEG -$193.8M | - | 300 | 290 | -$9.2M | +$762k bull / -$7.8M bear | out (clean 33, ADX 43, RVol 14.1) |
| 5 | **MSFT** | 527.27 | FLOW SURGE | **CALLS** | 55 | none: 129 calls 0-7DTE > 11 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (19 contracts' greeks worked out here) | POS +$570.5M | 496.21 | 525 | 530 | +$17.4M | +$5.7M bull / -$904k bear | out (clean 29, ADX 39, RVol 6.5) |
| 6 | **AVGO** | 341.26 | FLOW SURGE | **CALLS** | 53 | none: 84 calls 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (9 contracts' greeks worked out here) | NEG -$3.2M | 342.36 | 350 | 340 | +$2.6M | +$142k bull / +$0 bear | out (clean 29, ADX 41, RVol 1.9) |
| 7 | **AMZN** | 245.17 | FLOW SURGE | **PUTS** | 52 | none: 57 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (6 contracts' greeks worked out here) | POS +$13.0M | 241.75 | 265 | 250 | -$4.8M | +$547k bull / -$2.3M bear | out (clean 31, ADX 48, RVol 7.2) |
| 8 | **MU** | 949.85 | PINNED between the walls (positive gamma) - chop | **-** | 52 | - | POS +$369.6M | - | 950 | 950 | +$23.9M | +$15.4M bull / -$588k bear | out (clean 29, ADX 36, RVol 2.0) |
| 9 | **ORCL** | 140.04 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 51 | 10/30 145C @ 0.79 (delta 0.22) = est +139% at 143.92 | POS +$109.4M | - | 135 | 140 | -$311k | +$475k bull / +$0 bear | out (clean 31, ADX 41, RVol 2.3) |
| 10 | **PLTR** | 197.00 | FLOW SURGE | **PUTS** | 49 | none: 16 puts 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (1 contracts' greeks worked out here) | POS +$49.9M | 190.94 | 200 | 200 | -$2.5M | +$0 bull / -$337k bear | out (clean 26, ADX 20, RVol 2.8) |
| 11 | **META** | 623.07 | FLOW SURGE | **PUTS** | 48 | none: 144 puts 0-7DTE > 9 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (10 contracts' greeks worked out here) | NEG -$72.6M | 630.3 | 650 | 625 | -$13.0M | +$520k bull / -$1.7M bear | out (clean 28, ADX 34, RVol 1.6) |
| 12 | **HOOD** | 91.00 | FLOW SURGE | **PUTS** | 48 | 10/30 88P @ 0.59 (delta 0.23) = est +25% at 90 | NEG -$24.1M | - | 95 | 90 | -$1.1M | +$0 bull / -$58k bear | out (clean 29, ADX 15, RVol 1.8) |
| 13 | **SHOP** | 167.21 | FLOW SURGE | **PUTS** | 48 | none: 13 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (2 contracts' greeks worked out here) | NEG -$4.8M | 172.48 | 175 | 165 | -$56k | +$0 bull / -$29k bear | out (clean 27, ADX 20, RVol 1.3) |
| 14 | **MSTR** | 141.35 | - | **-** | 33 | - | POS +$26.8M | - | 152.5 | 140 | -$1.1M | +$165k bull / -$31k bear | out (clean 26, ADX 24, RVol 2.1) |
| 15 | **NFLX** | 62.10 | - | **-** | 31 | - | NEG -$49.8M | - | 63 | 60 | -$296k | +$30k bull / +$0 bear | out (clean 31, ADX 33, RVol 1.3) |
| 16 | **AMD** | 565.94 | - | **-** | 30 | - | POS +$138.9M | - | 600 | 550 | +$5.7M | +$1.9M bull / -$935k bear | out (clean 30, ADX 42, RVol 2.8) |
| 17 | **ARM** | 225.78 | - | **-** | 30 | - | POS +$3.0M | 221.9 | 227.5 | 220 | +$1.9M | - | out (clean 26, ADX 29, RVol 2.4) |
| 18 | **SMH** | 559.07 | - | **-** | 28 | - | NEG -$61.2M | 563.58 | 560 | 555 | +$518k | +$148k bull / -$63k bear | out (clean 28, ADX 25, RVol 2.1) |
| 19 | **QQQ** | 714.97 | - | **-** | 27 | - | NEG -$4.6B | 727.06 | 720 | 700 | -$45.7M | +$2.3M bull / -$4.6M bear | out (clean 28, ADX 32, RVol 1.8) |
| 20 | **COIN** | 162.69 | - | **-** | 27 | - | POS +$7.9M | - | 170 | 155 | -$135k | - | out (clean 27, ADX 19, RVol 2.3) |
| 21 | **SPY** | 768.71 | - | **-** | 26 | - | NEG -$4.9B | 773.23 | 770 | 765 | -$37.7M | +$1.5M bull / -$7.2M bear | out (clean 27, ADX 22, RVol 1.9) |
| 22 | **UBER** | 64.79 | - | **-** | 25 | - | NEG -$34.1M | 68.38 | 70 | 65 | -$118k | - | out (clean 29, ADX 29, RVol 1.7) |
| 23 | **NVDA** | 213.04 | - | **-** | 24 | - | POS +$191.3M | 210.51 | 215 | 210 | +$2.0M | +$1.4M bull / -$435k bear | out (clean 26, ADX 33, RVol 2.3) |
| 24 | **BABA** | 99.74 | - | **-** | 21 | - | NEG -$15.8M | 102.11 | 102 | 100 | -$50k | - | out (clean 28, ADX 30, RVol 1.5) |
| 25 | **TSLA** | 402.93 | - | **-** | 20 | - | POS +$470.5M | - | 400 | 400 | -$4.9M | +$2.5M bull / -$1.6M bear | out (clean 29, ADX 27, RVol 1.2) |
| 26 | **DELL** | 489.75 | - | **-** | 17 | - | POS +$16.7M | 474.37 | 500 | 500 | -$16k | +$31k bull / -$290k bear | out (clean 31, ADX 30, RVol 0.6) |
| 27 | **SMCI** | 35.26 | - | **-** | 17 | - | POS +$25.4M | - | 35 | 35 | +$88k | - | out (clean 27, ADX 25, RVol 1.0) |

## Big prints this scan (231)
- **MU** CALL 930 2026-10-30 (1DTE): 650 @ 31.28 = **+$2.0M** BUY | vol 1,152 / OI 1,361
- **MU** CALL 940 2026-10-30 (1DTE): 650 @ 24.38 = **+$1.6M** BUY | vol 1,404 / OI 2,522
- **MU** CALL 930 2026-10-30 (1DTE): 349 @ 31.28 = **+$1.1M** BUY | vol 1,152 / OI 1,361
- **SPY** PUT 780 2026-10-30 (1DTE): 727 @ 11.86 = **+$862k** BUY | vol 2,551 / OI 4,038
- **MU** CALL 940 2026-10-30 (1DTE): 349 @ 24.38 = **+$851k** BUY | vol 1,404 / OI 2,522
- **SPY** CALL 756 2026-10-29 (0DTE): 499 @ 11.89 = **+$593k** SELL | vol 1,591 / OI 25
- **SPY** PUT 775 2026-11-02 (4DTE): 666 @ 7.67 = **+$511k** BUY | vol 1,117 / OI 149
- **MU** PUT 970 2026-10-30 (1DTE): 200 @ 25.25 = **+$505k** MID | vol 819 / OI 537
- **SPY** CALL 758 2026-10-29 (0DTE): 426 @ 9.67 = **+$412k** SELL | vol 1,954 / OI 32
- **SPY** CALL 756 2026-10-29 (0DTE): 337 @ 11.93 = **+$402k** SELL | vol 1,591 / OI 25
- **SPY** CALL 756 2026-10-29 (0DTE): 337 @ 11.93 = **+$402k** SELL | vol 1,591 / OI 25
- **SPY** CALL 761 2026-10-29 (0DTE): 499 @ 7.07 = **+$353k** SELL | vol 1,858 / OI 248
- **SPY** PUT 775 2026-11-02 (4DTE): 334 @ 7.67 = **+$256k** BUY | vol 1,117 / OI 149
- **SPY** CALL 756 2026-10-29 (0DTE): 213 @ 11.89 = **+$253k** SELL | vol 1,591 / OI 25
- **MSFT** CALL 515 2026-10-30 (1DTE): 100 @ 24.10 = **+$241k** BUY | vol 196 / OI 1,011

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 775 2026-11-02 (4DTE): 1,117 traded vs OI 149
- **SPY** PUT 754 2026-10-29 (0DTE): 628 traded vs OI 614
- **SPY** CALL 756 2026-10-29 (0DTE): 1,591 traded vs OI 25
- **SPY** CALL 761 2026-10-29 (0DTE): 1,858 traded vs OI 248
- **SPY** PUT 765 2026-11-03 (5DTE): 662 traded vs OI 596
- **SPY** CALL 768 2026-11-02 (4DTE): 595 traded vs OI 377
- **SPY** CALL 769 2026-11-02 (4DTE): 933 traded vs OI 365
- **SPY** CALL 771 2026-11-02 (4DTE): 615 traded vs OI 438
- **SPY** CALL 770 2026-11-03 (5DTE): 1,348 traded vs OI 932
- **SPY** PUT 774 2026-10-29 (0DTE): 538 traded vs OI 491
- **SPY** CALL 770 2026-11-04 (6DTE): 1,402 traded vs OI 594
- **SPY** CALL 764 2026-10-29 (0DTE): 878 traded vs OI 770
- **SPY** CALL 784 2026-10-29 (0DTE): 1,638 traded vs OI 1,370
- **SPY** PUT 780 2026-11-06 (8DTE): 1,880 traded vs OI 1,348
- **SPY** PUT 773 2026-11-13 (15DTE): 1,466 traded vs OI 1,057

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
