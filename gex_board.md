# GEX + FLOW SCAN - Mon Nov 09, 10:10 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (2)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:00 | **MSFT** | **CALLS** | TREND + FLOW | 11/09 545C | 0.77 | 0.43 | +4% (3m) | **-44%** | +545% | 550 |
| 10:00 | **AMZN** | **CALLS** | TREND + FLOW | 11/09 275C | 0.48 | 0.38 | +13% (6m) | **-21%** | +258% | 275.95 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:10:08 ET, last candle SPY 10:09, QQQ 10:09 | no errors

## Flow surges NOT fired - price disagreed (9 today, last 5)
- 10:10 SMCI PUTS: price +0.22 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:10 IWM PUTS: price +0.10 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:10 SPY PUTS: price +0.55 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:05 SMCI PUTS: price +0.29 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:05 SPY PUTS: price +1.39 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **META** | 639.65 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 64 | none: 204 calls 0-7DTE > 9 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (94 contracts' greeks worked out here) | POS +$162.4M | 609.82 | 650 | 640 | -$2.3M | +$2.1M bull / -$232k bear | LONG (clean 33, ADX 43, RVol 2.1) |
| 2 | **AVGO** | 315.46 | FLOW SURGE | **PUTS** | 59 | none: 100 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (42 contracts' greeks worked out here) | NEG -$66.4M | - | 340 | 320 | -$5.1M | +$0 bull / -$334k bear | out (clean 30, ADX 46, RVol 2.8) |
| 3 | **AMZN** | 271.76 | TREND + FLOW | **CALLS** | 57 | none: 88 calls 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (39 contracts' greeks worked out here) | POS +$411.5M | - | 270 | 265 | +$9.3M | +$2.7M bull / -$33k bear | LONG (clean 35, ADX 40, RVol 2.0) |
| 4 | **MSFT** | 538.89 | TREND + FLOW | **CALLS** | 57 | none: 176 calls 0-7DTE > 9 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (76 contracts' greeks worked out here) | POS +$526.2M | - | 550 | 540 | +$4.3M | +$330k bull / -$34k bear | LONG (clean 34, ADX 31, RVol 1.4) |
| 5 | **SMH** | 479.15 | FLOW SURGE | **PUTS** | 53 | none: 152 puts 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (61 contracts' greeks worked out here) | NEG -$234.6M | - | 500 | 475 | -$2.6M | +$0 bull / -$1.0M bear | out (clean 31, ADX 36, RVol 2.1) |
| 6 | **IWM** | 279.17 | FLOW SURGE | **PUTS** | 50 | 11/09 279P @ 0.66 (delta 0.46) = est +114% at 277.74 | NEG -$1.4B | 285.02 | 285 | 270 | -$11.4M | +$0 bull / -$2.6M bear | out (clean 32, ADX 38, RVol 1.5) |
| 7 | **TSLA** | 375.04 | FLOW SURGE | **PUTS** | 50 | none: 120 puts 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (51 contracts' greeks worked out here) | POS +$103.7M | - | 400 | 380 | -$77.6M | +$1.5M bull / -$1.7M bear | LONG (clean 34, ADX 40, RVol 1.6) |
| 8 | **QQQ** | 672.55 | FLOW SURGE | **PUTS** | 49 | none: 779 puts 0-7DTE > 59 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (276 contracts' greeks worked out here) | NEG -$2.2B | 698.84 | 680 | 680 | -$168.5M | +$0 bull / -$5.8M bear | out (clean 32, ADX 36, RVol 1.5) |
| 9 | **SPY** | 748.13 | FLOW SURGE | **PUTS** | 47 | 11/09 744P @ 0.65 (delta 0.21) = est +106% at 745 | NEG -$7.2B | 761.28 | 750 | 740 | -$167.2M | +$0 bull / -$8.4M bear | out (clean 32, ADX 34, RVol 1.3) |
| 10 | **SMCI** | 29.24 | FLOW SURGE | **PUTS** | 45 | 11/13 27.5P @ 0.64 (delta 0.27) = est +28% at 28.45 | POS +$39k | - | 30 | 30 | -$974k | +$0 bull / -$222k bear | out (clean 31, ADX 28, RVol 0.9) |
| 11 | **COIN** | 135.28 | FLOW SURGE | **PUTS** | 43 | none: 27 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$6.1M | - | 140 | 135 | -$1.0M | +$0 bull / -$523k bear | out (clean 31, ADX 18, RVol 0.7) |
| 12 | **PLTR** | 167.03 | FLOW SURGE | **PUTS** | 41 | none: 13 puts 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (1 contracts' greeks worked out here) | POS +$11.7M | - | 165 | 170 | -$2.9M | +$254k bull / -$555k bear | out (clean 29, ADX 39, RVol 1.3) |
| 13 | **NVDA** | 178.56 | - | **-** | 31 | - | NEG -$169.2M | - | 190 | 190 | -$52.0M | +$906k bull / -$9.4M bear | out (clean 32, ADX 37, RVol 7.0) |
| 14 | **AMD** | 485.53 | - | **-** | 30 | - | NEG -$19.6M | - | 500 | 440 | -$19.4M | +$4.3M bull / -$2.3M bear | out (clean 32, ADX 46, RVol 3.2) |
| 15 | **HOOD** | 84.26 | - | **-** | 28 | - | NEG -$1.5M | - | 85 | 85 | -$1.5M | +$86k bull / -$673k bear | out (clean 30, ADX 54, RVol 1.4) |
| 16 | **MSTR** | 126.59 | - | **-** | 27 | - | POS +$2.0M | 123.19 | 135 | 120 | -$1.3M | +$34k bull / -$136k bear | out (clean 30, ADX 33, RVol 1.7) |
| 17 | **AAPL** | 348.72 | - | **-** | 22 | - | POS +$380.3M | 337.97 | 350 | 350 | +$3.3M | +$1.4M bull / -$168k bear | out (clean 27, ADX 30, RVol 1.1) |
| 18 | **ARM** | 184.12 | - | **-** | 22 | - | NEG -$4.5M | - | 185 | 190 | +$147k | +$0 bull / -$481k bear | out (clean 25, ADX 38, RVol 1.0) |
| 19 | **BABA** | 106.02 | - | **-** | 22 | - | POS +$3.6M | 103.87 | 110 | 110 | +$102k | +$35k bull / +$0 bear | out (clean 32, ADX 30, RVol 2.2) |
| 20 | **MU** | 724.40 | - | **-** | 21 | - | NEG -$7.9M | 733.33 | 750 | 750 | -$8.5M | +$580k bull / -$8.8M bear | out (clean 31, ADX 32, RVol 1.8) |
| 21 | **ORCL** | 118.23 | - | **-** | 20 | - | NEG -$25.1M | - | 125 | 125 | -$206k | +$0 bull / -$280k bear | out (clean 29, ADX 32, RVol 0.7) |
| 22 | **GOOGL** | 294.33 | - | **-** | 19 | - | POS +$25.6M | 290.99 | 300 | 290 | -$2k | +$212k bull / -$1.2M bear | out (clean 32, ADX 32, RVol 1.6) |
| 23 | **DELL** | 345.57 | - | **-** | 18 | - | NEG -$6.1M | - | 350 | 340 | -$421k | - | out (clean 31, ADX 36, RVol 1.5) |
| 24 | **CRM** | 214.07 | - | **-** | 16 | - | NEG -$10.7M | - | 195 | 220 | +$21k | - | out (clean 34, ADX 22, RVol 0.8) |
| 25 | **NFLX** | 63.78 | - | **-** | 13 | - | NEG -$19.0M | - | 65 | 65 | -$55k | - | out (clean 32, ADX 28, RVol 2.1) |
| 26 | **SHOP** | 149.02 | - | **-** | 13 | - | POS +$1.7M | - | 150 | 140 | -$9k | - | out (clean 34, ADX 16, RVol 0.4) |
| 27 | **UBER** | 69.16 | - | **-** | 11 | - | NEG -$255k | 69.29 | 70 | 65 | -$30k | - | out (clean 31, ADX 24, RVol 0.8) |

## Big prints this scan (252)
- **SPY** CALL 730 2026-11-10 (1DTE): 1,000 @ 18.00 = **+$1.8M** SELL | vol 1,025 / OI 5,480
- **AMD** CALL 475 2026-11-09 (0DTE): 489 @ 14.90 = **+$729k** BUY | vol 4,787 / OI 143
- **AMD** CALL 475 2026-11-09 (0DTE): 386 @ 13.60 = **+$525k** SELL | vol 4,787 / OI 143
- **SPY** CALL 743 2026-11-09 (0DTE): 930 @ 5.51 = **+$512k** SELL | vol 27,525 / OI 1,035
- **AMZN** CALL 280 2026-11-13 (4DTE): 2,000 @ 2.24 = **+$448k** BUY | vol 5,541 / OI 3,953
- **GOOGL** CALL 300 2026-11-16 (7DTE): 981 @ 2.94 = **+$288k** SELL | vol 4,806 / OI 5,075
- **NVDA** CALL 177.5 2026-11-11 (2DTE): 457 @ 5.45 = **+$249k** SELL | vol 4,974 / OI 144
- **SMH** CALL 480 2026-11-13 (4DTE): 205 @ 11.60 = **+$238k** SELL | vol 666 / OI 133
- **GOOGL** CALL 300 2026-11-16 (7DTE): 826 @ 2.85 = **+$235k** SELL | vol 4,806 / OI 5,075
- **QQQ** CALL 674 2026-11-09 (0DTE): 991 @ 2.20 = **+$218k** SELL | vol 27,653 / OI 2,191
- **AMD** CALL 500 2026-11-09 (0DTE): 978 @ 2.09 = **+$204k** BUY | vol 12,989 / OI 1,188
- **GOOGL** CALL 300 2026-11-16 (7DTE): 682 @ 2.89 = **+$197k** SELL | vol 4,806 / OI 5,075
- **SPY** CALL 728 2026-11-09 (0DTE): 100 @ 19.70 = **+$197k** SELL | vol 257 / OI 14
- **SPY** CALL 747 2026-11-10 (1DTE): 448 @ 4.28 = **+$192k** SELL | vol 6,290 / OI 485
- **SPY** PUT 747 2026-11-09 (0DTE): 852 @ 2.16 = **+$184k** BUY | vol 14,792 / OI 1,091

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 745 2026-11-10 (1DTE): 2,175 traded vs OI 2,145
- **SPY** CALL 761 2026-11-10 (1DTE): 887 traded vs OI 687
- **SPY** PUT 720 2026-11-10 (1DTE): 1,306 traded vs OI 1,281
- **SPY** PUT 748 2026-11-10 (1DTE): 1,013 traded vs OI 790
- **SPY** CALL 748 2026-11-13 (4DTE): 1,097 traded vs OI 760
- **SPY** CALL 750 2026-11-11 (2DTE): 1,930 traded vs OI 1,538
- **SPY** CALL 760 2026-11-10 (1DTE): 3,594 traded vs OI 3,521
- **SPY** PUT 733 2026-11-10 (1DTE): 642 traded vs OI 639
- **SPY** CALL 762 2026-11-11 (2DTE): 533 traded vs OI 146
- **SPY** CALL 732 2026-11-09 (0DTE): 511 traded vs OI 319
- **SPY** CALL 766 2026-11-10 (1DTE): 1,275 traded vs OI 1,265
- **SPY** PUT 748 2026-12-04 (25DTE): 657 traded vs OI 167
- **QQQ** PUT 666 2026-11-10 (1DTE): 537 traded vs OI 202
- **QQQ** PUT 664 2026-11-10 (1DTE): 545 traded vs OI 229
- **QQQ** PUT 675 2026-11-09 (0DTE): 1,930 traded vs OI 1,826

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
