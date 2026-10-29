# GEX + FLOW SCAN - Thu Oct 29, 10:40 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (4)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:30 | **IWM** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 10/29 284P | 0.65 | 0.50 | -3% (0m) | **-23%** | +232% | 281.86 |
| 10:00 | **ORCL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 10/30 145C | 0.79 | 0.84 | +18% (37m) | **+6%** | +139% | 143.92 |
| 09:55 | **AAPL** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 10/30 345P | 0.77 | 0.56 | +17% (2m) | **-27%** | +198% | 345 |
| 09:50 | **IWM** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 10/29 283P | 0.50 | 0.19 | +20% (21m) | **-62%** | +159% | 282 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:40:08 ET, last candle SPY 10:39, QQQ 10:39 | no errors

## Flow surges NOT fired - price disagreed (2 today, last 5)
- 10:05 HOOD PUTS: price +0.99 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:00 HOOD PUTS: price +0.89 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **ARM** | 227.08 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 52 | none: 18 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (3 contracts' greeks worked out here) | POS +$2.9M | 222.45 | 227.5 | 220 | +$1.8M | - | out (clean 27, ADX 23, RVol 2.2) |
| 2 | **IWM** | 284.26 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 43 | 10/29 284P @ 0.50 (delta 0.43) = est +459% at 281.28 | POS +$864.8M | 281.28 | 284 | 270 | -$3.1M | +$355k bull / -$2.7M bear | out (clean 26, ADX 51, RVol 1.1) |
| 3 | **AAPL** | 349.88 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 43 | none: 55 puts 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (7 contracts' greeks worked out here) | POS +$629.5M | 339.89 | 350 | 345 | +$5.4M | +$812k bull / -$557k bear | out (clean 29, ADX 42, RVol 1.1) |
| 4 | **AMZN** | 247.40 | FLOW SURGE | **PUTS** | 42 | none: 57 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (8 contracts' greeks worked out here) | POS +$19.4M | 241.25 | 265 | 250 | -$11.4M | +$0 bull / -$2.6M bear | out (clean 31, ADX 42, RVol 1.3) |
| 5 | **COIN** | 163.28 | FLOW SURGE | **PUTS** | 38 | none: 15 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (9 contracts' greeks worked out here) | POS +$7.7M | - | 170 | 155 | -$450k | +$0 bull / -$133k bear | out (clean 26, ADX 20, RVol 1.1) |
| 6 | **MSFT** | 526.63 | - | **-** | 32 | - | POS +$555.6M | 499.54 | 525 | 530 | +$27.1M | +$404k bull / -$628k bear | out (clean 28, ADX 30, RVol 2.0) |
| 7 | **GOOGL** | 285.64 | - | **-** | 29 | - | NEG -$201.3M | - | 300 | 290 | -$10.8M | +$290k bull / -$1.0M bear | out (clean 32, ADX 52, RVol 4.2) |
| 8 | **META** | 625.09 | - | **-** | 26 | - | NEG -$58.0M | 629.94 | 650 | 625 | -$12.3M | +$111k bull / -$1.1M bear | out (clean 28, ADX 47, RVol 1.1) |
| 9 | **TSLA** | 406.69 | - | **-** | 25 | - | POS +$514.2M | - | 400 | 400 | -$25.5M | +$0 bull / -$1.9M bear | out (clean 29, ADX 30, RVol 1.0) |
| 10 | **MU** | 953.13 | - | **-** | 23 | - | POS +$379.3M | - | 950 | 950 | +$23.7M | +$1.8M bull / -$2.1M bear | out (clean 29, ADX 35, RVol 0.8) |
| 11 | **SPY** | 769.93 | - | **-** | 22 | - | NEG -$3.8B | 773.13 | 770 | 765 | -$80.4M | +$0 bull / -$1.6M bear | out (clean 26, ADX 15, RVol 1.2) |
| 12 | **UBER** | 65.20 | - | **-** | 22 | - | NEG -$32.8M | 68.71 | 67 | 65 | -$170k | - | out (clean 28, ADX 26, RVol 0.5) |
| 13 | **QQQ** | 716.12 | - | **-** | 21 | - | NEG -$4.5B | 726.56 | 720 | 720 | -$73.9M | +$102k bull / -$1.9M bear | out (clean 28, ADX 22, RVol 0.7) |
| 14 | **NFLX** | 61.87 | - | **-** | 19 | - | NEG -$51.9M | - | 63 | 60 | -$483k | - | out (clean 30, ADX 39, RVol 1.1) |
| 15 | **MSTR** | 142.69 | - | **-** | 19 | - | POS +$29.4M | - | 152.5 | 140 | -$543k | +$135k bull / +$0 bear | out (clean 26, ADX 16, RVol 1.3) |
| 16 | **ORCL** | 141.01 | - | **-** | 19 | - | POS +$128.4M | - | 135 | 140 | +$171k | +$139k bull / -$138k bear | out (clean 32, ADX 33, RVol 1.1) |
| 17 | **AMD** | 568.29 | - | **-** | 18 | - | POS +$142.3M | - | 600 | 550 | -$161k | +$29k bull / -$533k bear | out (clean 28, ADX 35, RVol 0.8) |
| 18 | **NVDA** | 214.01 | - | **-** | 17 | - | POS +$255.9M | 210.88 | 215 | 210 | -$517k | +$0 bull / -$1.0M bear | out (clean 25, ADX 26, RVol 1.0) |
| 19 | **PLTR** | 195.55 | - | **-** | 17 | - | POS +$39.1M | 191.39 | 200 | 190 | -$217k | +$27k bull / +$0 bear | out (clean 25, ADX 12, RVol 2.0) |
| 20 | **BABA** | 100.14 | - | **-** | 16 | - | NEG -$13.1M | 101.98 | 102 | 100 | -$74k | - | out (clean 28, ADX 21, RVol 0.7) |
| 21 | **AVGO** | 343.22 | - | **-** | 15 | - | POS +$3.6M | 342.47 | 350 | 340 | +$2.7M | - | out (clean 29, ADX 31, RVol 0.5) |
| 22 | **CRM** | 231.53 | - | **-** | 15 | - | NEG -$19.0M | - | 240 | 230 | -$227k | - | out (clean 27, ADX 30, RVol 0.8) |
| 23 | **SHOP** | 167.14 | - | **-** | 15 | - | NEG -$5.6M | 172.38 | 175 | 165 | -$69k | - | out (clean 26, ADX 13, RVol 0.5) |
| 24 | **SMCI** | 35.50 | - | **-** | 12 | - | POS +$25.5M | - | 35 | 35 | +$133k | - | out (clean 27, ADX 24, RVol 0.8) |
| 25 | **HOOD** | 91.58 | - | **-** | 10 | - | NEG -$21.1M | - | 95 | 90 | -$1.0M | - | out (clean 29, ADX 13, RVol 0.8) |
| 26 | **DELL** | 486.64 | - | **-** | 9 | - | POS +$12.4M | 476.71 | 500 | 500 | +$633k | - | out (clean 30, ADX 28, RVol 0.7) |
| 27 | **SMH** | 562.02 | - | **-** | 8 | - | NEG -$18.6M | 562.74 | 560 | 555 | +$243k | - | out (clean 27, ADX 16, RVol 1.3) |

## Big prints this scan (67)
- **SPY** PUT 775 2026-11-02 (4DTE): 258 @ 6.74 = **+$174k** BUY | vol 7,129 / OI 149
- **SPY** PUT 775 2026-11-02 (4DTE): 258 @ 6.73 = **+$174k** BUY | vol 7,129 / OI 149
- **GOOGL** PUT 297.5 2026-10-30 (1DTE): 100 @ 12.10 = **+$121k** SELL | vol 548 / OI 778
- **TSLA** CALL 405 2026-10-30 (1DTE): 265 @ 4.30 = **+$114k** SELL | vol 27,119 / OI 4,208
- **MU** CALL 945 2026-10-30 (1DTE): 50 @ 20.61 = **+$103k** BUY | vol 2,242 / OI 759
- **QQQ** CALL 713 2026-11-04 (6DTE): 100 @ 10.22 = **+$102k** BUY | vol 628 / OI 77
- **MU** CALL 950 2026-10-30 (1DTE): 50 @ 17.62 = **+$88k** BUY | vol 6,240 / OI 12,588
- **TSLA** CALL 405 2026-10-30 (1DTE): 200 @ 4.35 = **+$87k** SELL | vol 27,119 / OI 4,208
- **TSLA** CALL 405 2026-10-30 (1DTE): 200 @ 4.30 = **+$86k** SELL | vol 27,119 / OI 4,208
- **TSLA** CALL 405 2026-10-30 (1DTE): 200 @ 4.30 = **+$86k** SELL | vol 27,119 / OI 4,208
- **TSLA** CALL 405 2026-10-30 (1DTE): 200 @ 4.30 = **+$86k** SELL | vol 27,119 / OI 4,208
- **AMZN** CALL 250 2026-10-30 (1DTE): 100 @ 8.40 = **+$84k** SELL | vol 3,091 / OI 7,932
- **MSFT** PUT 550 2026-10-30 (1DTE): 32 @ 26.25 = **+$84k** BUY | vol 403 / OI 199
- **NVDA** PUT 212.5 2026-11-04 (6DTE): 258 @ 3.25 = **+$84k** BUY | vol 2,829 / OI 260
- **NVDA** PUT 212.5 2026-10-30 (1DTE): 582 @ 1.38 = **+$80k** BUY | vol 36,929 / OI 5,164

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 777 2026-11-04 (6DTE): 599 traded vs OI 387
- **SPY** PUT 761 2026-10-30 (1DTE): 4,896 traded vs OI 4,893
- **SPY** PUT 770 2026-11-11 (13DTE): 630 traded vs OI 0
- **QQQ** PUT 722 2026-10-29 (0DTE): 959 traded vs OI 955
- **QQQ** PUT 708 2026-11-02 (4DTE): 591 traded vs OI 214
- **QQQ** CALL 755 2026-11-13 (15DTE): 7,653 traded vs OI 1,310
- **QQQ** CALL 735 2026-11-13 (15DTE): 1,965 traded vs OI 1,691
- **IWM** CALL 287.5 2026-11-06 (8DTE): 563 traded vs OI 326
- **NVDA** CALL 235 2026-11-13 (15DTE): 514 traded vs OI 0
- **NVDA** CALL 210 2026-11-02 (4DTE): 1,362 traded vs OI 521
- **TSLA** CALL 402.5 2026-11-06 (8DTE): 612 traded vs OI 543
- **AMD** PUT 530 2026-11-02 (4DTE): 568 traded vs OI 164
- **AMD** CALL 590 2026-10-30 (1DTE): 1,471 traded vs OI 1,453
- **AMD** CALL 562.5 2026-10-30 (1DTE): 612 traded vs OI 597
- **META** CALL 630 2026-11-02 (4DTE): 671 traded vs OI 647

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
