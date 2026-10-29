# GEX + FLOW SCAN - Thu Oct 29, 02:20 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (4)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:30 | **IWM** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 10/29 284P | 0.65 | 0.22 | +3% (25m) | **-66%** (done) | +232% | 281.86 |
| 10:00 | **ORCL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 10/30 145C | 0.79 | 0.84 | +18% (37m) | **+6%** (done) | +139% | 143.92 |
| 09:55 | **AAPL** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 10/30 345P | 0.77 | 0.68 | +17% (2m) | **-12%** (done) | +198% | 345 |
| 09:50 | **IWM** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 10/29 283P | 0.50 | 0.18 | +20% (21m) | **-64%** (done) | +159% | 282 |

## 1m RULES on SPY / QQQ - loose (2 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 14:20:08 ET, last candle SPY 14:19, QQQ 14:19 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 14:17 | QQQ | 1m FAILED POP | R3 R4 | PUTS | TURNING your way | no contract: 86 puts 0-1DTE > 6 priced 0.40-0.80 > 2 delta 0.15+ > 2 spread ok > 2 liquid  |
| 14:12 | QQQ | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | no contract: 86 puts 0-1DTE > 8 priced 0.40-0.80 > 3 delta 0.15+ > 3 spread ok > 3 liquid  |

## Flow surges NOT fired - price disagreed (2 today, last 5)
- 10:05 HOOD PUTS: price +0.99 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:00 HOOD PUTS: price +0.89 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **MSFT** | 529.17 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 43 | none: 126 calls 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (37 contracts' greeks worked out here) | POS +$642.6M | 500.96 | 525 | 530 | +$23.7M | +$0 bull / -$1.8M bear | out (clean 28, ADX 22, RVol 1.1) |
| 2 | **IWM** | 283.34 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 25 | 10/30 282.5P @ 0.79 (delta 0.38) = est +23% at 282.69 | POS +$697.9M | 281.32 | 284 | 270 | -$380k | - | out (clean 26, ADX 27, RVol 0.7) |
| 3 | **DELL** | 476.00 | - | **-** | 24 | - | NEG -$4.5M | 479.63 | 500 | 460 | +$2.0M | +$33k bull / +$0 bear | out (clean 30, ADX 48, RVol 0.9) |
| 4 | **AAPL** | 349.73 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 23 | none: 55 puts 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (10 contracts' greeks worked out here) | POS +$665.8M | 340.79 | 350 | 345 | +$3.1M | - | out (clean 29, ADX 15, RVol 0.6) |
| 5 | **GOOGL** | 281.56 | - | **-** | 23 | - | NEG -$170.3M | - | 300 | 290 | -$5.6M | +$205k bull / +$0 bear | out (clean 32, ADX 40, RVol 1.9) |
| 6 | **MU** | 932.56 | - | **-** | 22 | - | POS +$250.4M | 882.92 | 950 | 900 | +$40.1M | +$3.6M bull / -$30k bear | out (clean 28, ADX 45, RVol 0.5) |
| 7 | **SMH** | 558.62 | - | **-** | 20 | - | NEG -$84.2M | 562.56 | 560 | 555 | +$1.4M | +$652k bull / +$0 bear | out (clean 26, ADX 21, RVol 0.5) |
| 8 | **META** | 626.80 | - | **-** | 19 | - | NEG -$39.4M | 630.17 | 650 | 625 | -$10.4M | +$536k bull / -$452k bear | out (clean 28, ADX 29, RVol 0.8) |
| 9 | **ORCL** | 138.27 | - | **-** | 19 | - | POS +$123.7M | - | 135 | 140 | +$732k | +$0 bull / -$57k bear | out (clean 32, ADX 37, RVol 0.8) |
| 10 | **SPY** | 767.38 | - | **-** | 18 | - | NEG -$6.5B | 772.43 | 770 | 765 | -$95.3M | +$243k bull / -$1.3M bear | out (clean 25, ADX 25, RVol 0.5) |
| 11 | **QQQ** | 713.27 | - | **-** | 17 | - | NEG -$5.5B | 726.05 | 720 | 700 | -$62.2M | +$250k bull / -$491k bear | out (clean 26, ADX 25, RVol 0.5) |
| 12 | **AMZN** | 244.56 | - | **-** | 17 | - | POS +$9.1M | 241.93 | 265 | 250 | -$1.3M | +$490k bull / -$233k bear | out (clean 32, ADX 25, RVol 1.0) |
| 13 | **NVDA** | 212.79 | - | **-** | 16 | - | POS +$148.0M | 211.11 | 215 | 210 | -$2.3M | +$412k bull / -$126k bear | out (clean 24, ADX 24, RVol 0.6) |
| 14 | **TSLA** | 405.76 | - | **-** | 16 | - | POS +$504.4M | - | 400 | 400 | -$20.5M | +$29k bull / -$614k bear | out (clean 28, ADX 16, RVol 0.4) |
| 15 | **AMD** | 564.49 | - | **-** | 15 | - | POS +$140.7M | - | 550 | 550 | -$672k | +$756k bull / +$0 bear | out (clean 28, ADX 23, RVol 0.3) |
| 16 | **COIN** | 160.18 | - | **-** | 15 | - | POS +$4.9M | 153.64 | 170 | 155 | -$134k | +$79k bull / -$374k bear | out (clean 25, ADX 13, RVol 0.7) |
| 17 | **MSTR** | 141.74 | - | **-** | 15 | - | POS +$27.0M | - | 152.5 | 140 | +$43k | +$59k bull / +$0 bear | out (clean 26, ADX 18, RVol 1.0) |
| 18 | **UBER** | 65.15 | - | **-** | 14 | - | NEG -$34.7M | 68.17 | 70 | 65 | -$162k | - | out (clean 28, ADX 19, RVol 0.5) |
| 19 | **SMCI** | 34.76 | - | **-** | 13 | - | POS +$21.7M | - | 35 | 35 | +$278k | - | out (clean 26, ADX 34, RVol 0.6) |
| 20 | **ARM** | 229.22 | - | **-** | 13 | - | POS +$3.1M | 222.51 | 227.5 | 220 | +$1.5M | - | out (clean 24, ADX 11, RVol 0.6) |
| 21 | **NFLX** | 61.88 | - | **-** | 10 | - | NEG -$52.8M | - | 63 | 60 | -$494k | - | out (clean 31, ADX 24, RVol 0.6) |
| 22 | **SHOP** | 166.68 | - | **-** | 9 | - | NEG -$5.9M | 171.39 | 175 | 165 | -$74k | - | out (clean 25, ADX 15, RVol 0.4) |
| 23 | **CRM** | 231.45 | - | **-** | 8 | - | NEG -$20.1M | - | 240 | 230 | -$238k | - | out (clean 27, ADX 10, RVol 0.7) |
| 24 | **HOOD** | 90.70 | - | **-** | 7 | - | NEG -$25.9M | - | 95 | 90 | -$447k | - | out (clean 28, ADX 25, RVol 0.7) |
| 25 | **BABA** | 99.20 | - | **-** | 7 | - | NEG -$20.2M | 101.65 | 100 | 100 | -$18k | - | out (clean 29, ADX 26, RVol 0.9) |
| 26 | **AVGO** | 344.74 | - | **-** | 5 | - | POS +$29.5M | 340.46 | 350 | 340 | +$1.5M | - | out (clean 28, ADX 14, RVol 0.5) |
| 27 | **PLTR** | 194.28 | - | **-** | 4 | - | POS +$21.3M | 192.37 | 200 | 190 | -$198k | - | out (clean 26, ADX 16, RVol 0.4) |

## Big prints this scan (54)
- **AVGO** PUT 355 2026-10-30 (1DTE): 750 @ 10.95 = **+$821k** MID | vol 979 / OI 1,479
- **SPY** CALL 735 2026-10-30 (1DTE): 148 @ 32.47 = **+$481k** SELL | vol 169 / OI 493
- **SPY** CALL 730 2026-10-30 (1DTE): 122 @ 37.09 = **+$452k** MID | vol 173 / OI 937
- **SPY** CALL 766 2026-10-29 (0DTE): 878 @ 1.95 = **+$171k** SELL | vol 25,506 / OI 865
- **SPY** PUT 780 2026-10-30 (1DTE): 122 @ 12.91 = **+$158k** BUY | vol 3,187 / OI 4,038
- **MSFT** CALL 527.5 2026-11-04 (6DTE): 200 @ 7.50 = **+$150k** SELL | vol 1,111 / OI 43
- **QQQ** PUT 712 2026-10-29 (0DTE): 857 @ 1.70 = **+$146k** BUY | vol 181,157 / OI 1,739
- **SPY** PUT 775 2026-10-30 (1DTE): 148 @ 7.89 = **+$117k** BUY | vol 4,113 / OI 4,017
- **QQQ** PUT 712 2026-10-30 (1DTE): 300 @ 3.85 = **+$116k** BUY | vol 14,500 / OI 7,961
- **SPY** PUT 767 2026-10-29 (0DTE): 1,052 @ 1.04 = **+$109k** SELL | vol 338,802 / OI 2,012
- **MU** CALL 935 2026-10-30 (1DTE): 70 @ 13.39 = **+$94k** BUY | vol 3,952 / OI 1,088
- **MU** CALL 940 2026-10-30 (1DTE): 64 @ 11.70 = **+$75k** BUY | vol 8,506 / OI 2,522
- **META** CALL 625 2026-10-30 (1DTE): 100 @ 7.40 = **+$74k** SELL | vol 20,432 / OI 1,463
- **MU** PUT 955 2026-11-02 (4DTE): 21 @ 31.50 = **+$66k** SELL | vol 559 / OI 29
- **TSLA** CALL 400 2026-10-30 (1DTE): 106 @ 6.05 = **+$64k** SELL | vol 16,653 / OI 14,892

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 775 2026-10-30 (1DTE): 4,113 traded vs OI 4,017
- **SPY** CALL 785 2026-11-03 (5DTE): 602 traded vs OI 306
- **QQQ** CALL 726 2026-11-13 (15DTE): 503 traded vs OI 424
- **SMH** PUT 545 2026-11-06 (8DTE): 1,584 traded vs OI 273
- **AMD** PUT 530 2026-10-30 (1DTE): 2,190 traded vs OI 1,529
- **AMD** PUT 515 2026-10-30 (1DTE): 766 traded vs OI 733
- **AMZN** CALL 247.5 2026-11-06 (8DTE): 504 traded vs OI 165
- **GOOGL** CALL 285 2026-11-11 (13DTE): 500 traded vs OI 0
- **NFLX** PUT 59 2026-11-06 (8DTE): 1,457 traded vs OI 1,101
- **NFLX** CALL 60 2026-10-30 (1DTE): 711 traded vs OI 710
- **ARM** PUT 225 2026-10-30 (1DTE): 500 traded vs OI 339
- **BABA** CALL 101 2026-11-06 (8DTE): 618 traded vs OI 240

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
