# GEX + FLOW SCAN - Thu Oct 29, 02:35 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (4)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:30 | **IWM** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 10/29 284P | 0.65 | 0.22 | +3% (25m) | **-66%** (done) | +232% | 281.86 |
| 10:00 | **ORCL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 10/30 145C | 0.79 | 0.84 | +18% (37m) | **+6%** (done) | +139% | 143.92 |
| 09:55 | **AAPL** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 10/30 345P | 0.77 | 0.68 | +17% (2m) | **-12%** (done) | +198% | 345 |
| 09:50 | **IWM** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 10/29 283P | 0.50 | 0.18 | +20% (21m) | **-64%** (done) | +159% | 282 |

## 1m RULES on SPY / QQQ - loose (4 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 14:35:08 ET, last candle SPY 14:34, QQQ 14:34 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 14:31 | SPY | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |
| 14:23 | QQQ | 1m FAILED POP | R3 R4 | PUTS | TURNING your way | no contract: 86 puts 0-1DTE > 5 priced 0.40-0.80 > 1 delta 0.15+ > 1 spread ok > 1 liquid  |
| 14:17 | QQQ | 1m FAILED POP | R3 R4 | PUTS | TURNING your way | no contract: 86 puts 0-1DTE > 6 priced 0.40-0.80 > 2 delta 0.15+ > 2 spread ok > 2 liquid  |
| 14:12 | QQQ | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | no contract: 86 puts 0-1DTE > 8 priced 0.40-0.80 > 3 delta 0.15+ > 3 spread ok > 3 liquid  |

## Flow surges NOT fired - price disagreed (2 today, last 5)
- 10:05 HOOD PUTS: price +0.99 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:00 HOOD PUTS: price +0.89 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **AAPL** | 350.00 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 33 | none: 57 puts 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (12 contracts' greeks worked out here) | POS +$673.7M | 340.82 | 350 | 345 | +$3.6M | +$29k bull / +$0 bear | out (clean 29, ADX 13, RVol 0.6) |
| 2 | **AMZN** | 244.22 | FLIP CROSS down into negative gamma | **PUTS** | 32 | none: 60 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (10 contracts' greeks worked out here) | NEG -$2.6M | 244.92 | 265 | 250 | -$2.1M | +$1.5M bull / -$74k bear | out (clean 32, ADX 27, RVol 1.0) |
| 3 | **MSFT** | 528.40 | - | **-** | 24 | - | POS +$610.3M | 503.29 | 525 | 530 | +$25.1M | +$804k bull / -$385k bear | out (clean 28, ADX 25, RVol 1.5) |
| 4 | **GOOGL** | 281.53 | - | **-** | 23 | - | NEG -$174.0M | - | 300 | 290 | -$5.1M | +$89k bull / +$0 bear | out (clean 32, ADX 42, RVol 2.1) |
| 5 | **MU** | 930.20 | - | **-** | 22 | - | POS +$224.4M | 884.16 | 950 | 900 | +$45.3M | +$1.8M bull / -$84k bear | out (clean 28, ADX 49, RVol 0.4) |
| 6 | **SPY** | 766.99 | - | **-** | 18 | - | NEG -$6.7B | 772.22 | 770 | 765 | -$84.7M | +$477k bull / -$112k bear | out (clean 25, ADX 27, RVol 0.5) |
| 7 | **QQQ** | 712.38 | - | **-** | 18 | - | NEG -$5.8B | 725.76 | 720 | 700 | -$58.0M | +$269k bull / +$0 bear | out (clean 26, ADX 27, RVol 0.6) |
| 8 | **META** | 625.51 | - | **-** | 18 | - | NEG -$56.3M | 629.9 | 650 | 625 | -$9.6M | +$108k bull / +$0 bear | out (clean 28, ADX 30, RVol 0.8) |
| 9 | **NFLX** | 61.70 | - | **-** | 18 | - | NEG -$56.4M | - | 63 | 61 | -$345k | +$40k bull / +$0 bear | out (clean 31, ADX 23, RVol 0.6) |
| 10 | **NVDA** | 212.42 | - | **-** | 16 | - | POS +$109.0M | 210.97 | 215 | 210 | -$717k | +$123k bull / -$59k bear | out (clean 24, ADX 28, RVol 0.6) |
| 11 | **TSLA** | 404.97 | - | **-** | 16 | - | POS +$500.9M | - | 400 | 400 | -$18.7M | +$295k bull / -$44k bear | out (clean 28, ADX 15, RVol 0.4) |
| 12 | **SMH** | 557.17 | - | **-** | 15 | - | NEG -$91.7M | 562.46 | 560 | 555 | +$2.7M | - | out (clean 27, ADX 26, RVol 0.9) |
| 13 | **AMD** | 562.97 | - | **-** | 15 | - | POS +$122.6M | - | 550 | 550 | +$327k | +$314k bull / -$154k bear | out (clean 28, ADX 23, RVol 0.3) |
| 14 | **PLTR** | 193.86 | - | **-** | 14 | - | POS +$16.1M | 192.41 | 200 | 190 | -$213k | +$61k bull / +$0 bear | out (clean 25, ADX 14, RVol 0.4) |
| 15 | **DELL** | 474.41 | - | **-** | 14 | - | NEG -$5.9M | 479.8 | 500 | 460 | +$2.3M | - | out (clean 31, ADX 51, RVol 0.8) |
| 16 | **SMCI** | 34.53 | - | **-** | 14 | - | POS +$20.4M | - | 35 | 35 | +$299k | - | out (clean 26, ADX 38, RVol 0.6) |
| 17 | **UBER** | 65.03 | - | **-** | 14 | - | NEG -$32.3M | 68.37 | 70 | 65 | -$151k | - | out (clean 28, ADX 22, RVol 0.6) |
| 18 | **ARM** | 226.50 | - | **-** | 13 | - | POS +$2.2M | 222.12 | 220 | 220 | +$1.5M | - | out (clean 24, ADX 15, RVol 0.5) |
| 19 | **ORCL** | 138.27 | - | **-** | 9 | - | POS +$122.3M | - | 135 | 140 | +$616k | - | out (clean 32, ADX 31, RVol 1.1) |
| 20 | **CRM** | 231.67 | - | **-** | 9 | - | NEG -$20.0M | - | 240 | 230 | -$241k | - | out (clean 27, ADX 10, RVol 0.8) |
| 21 | **HOOD** | 90.27 | - | **-** | 8 | - | NEG -$27.7M | - | 95 | 90 | -$315k | - | out (clean 28, ADX 31, RVol 0.8) |
| 22 | **SHOP** | 166.56 | - | **-** | 8 | - | NEG -$5.4M | 171.55 | 175 | 165 | -$63k | - | out (clean 25, ADX 16, RVol 0.4) |
| 23 | **BABA** | 98.95 | - | **-** | 8 | - | NEG -$21.4M | 101.57 | 100 | 100 | -$15k | - | out (clean 29, ADX 28, RVol 1.0) |
| 24 | **IWM** | 282.84 | - | **-** | 7 | - | POS +$697.0M | 280.92 | 282 | 270 | +$196k | - | out (clean 26, ADX 30, RVol 0.8) |
| 25 | **COIN** | 158.98 | - | **-** | 6 | - | POS +$2.1M | 155.54 | 170 | 155 | -$85k | - | out (clean 25, ADX 18, RVol 1.1) |
| 26 | **MSTR** | 140.92 | - | **-** | 6 | - | POS +$23.4M | - | 152.5 | 140 | +$247k | - | out (clean 26, ADX 22, RVol 1.0) |
| 27 | **AVGO** | 343.92 | - | **-** | 5 | - | POS +$11.3M | 342.25 | 350 | 340 | +$1.7M | - | out (clean 28, ADX 13, RVol 0.4) |

## Big prints this scan (70)
- **QQQ** PUT 745 2026-10-30 (1DTE): 2,980 @ 32.39 = **+$9.7M** MID | vol 3,007 / OI 1,306
- **SPY** PUT 800 2026-10-30 (1DTE): 80 @ 33.10 = **+$265k** MID | vol 80 / OI 24
- **SPY** PUT 790 2026-10-30 (1DTE): 100 @ 23.31 = **+$233k** MID | vol 118 / OI 20
- **AMD** CALL 565 2026-10-30 (1DTE): 180 @ 9.39 = **+$169k** BUY | vol 3,923 / OI 956
- **SPY** CALL 766 2026-10-29 (0DTE): 634 @ 2.25 = **+$143k** BUY | vol 29,924 / OI 865
- **QQQ** PUT 746 2026-10-30 (1DTE): 40 @ 32.61 = **+$130k** SELL | vol 40 / OI 20
- **SPY** CALL 769 2026-10-30 (1DTE): 563 @ 2.02 = **+$114k** BUY | vol 46,107 / OI 3,870
- **AMZN** CALL 252.5 2026-10-30 (1DTE): 171 @ 6.39 = **+$109k** BUY | vol 3,855 / OI 6,011
- **SPY** PUT 795 2026-10-30 (1DTE): 40 @ 26.47 = **+$106k** SELL | vol 54 / OI 13
- **AMZN** CALL 252.5 2026-10-30 (1DTE): 149 @ 6.41 = **+$96k** BUY | vol 3,855 / OI 6,011
- **AMZN** CALL 252.5 2026-10-30 (1DTE): 149 @ 6.40 = **+$95k** BUY | vol 3,855 / OI 6,011
- **AMZN** CALL 252.5 2026-10-30 (1DTE): 147 @ 6.38 = **+$94k** BUY | vol 3,855 / OI 6,011
- **MSFT** CALL 532.5 2026-10-30 (1DTE): 258 @ 3.10 = **+$80k** BUY | vol 8,631 / OI 1,809
- **AMZN** CALL 252.5 2026-10-30 (1DTE): 120 @ 6.39 = **+$77k** BUY | vol 3,855 / OI 6,011
- **AMZN** CALL 252.5 2026-10-30 (1DTE): 116 @ 6.39 = **+$74k** BUY | vol 3,855 / OI 6,011

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 776 2026-10-30 (1DTE): 1,897 traded vs OI 1,895
- **SPY** PUT 766 2026-11-06 (8DTE): 944 traded vs OI 894
- **QQQ** PUT 750 2026-10-30 (1DTE): 7,447 traded vs OI 2,905
- **QQQ** PUT 760 2026-10-30 (1DTE): 6,572 traded vs OI 3,029
- **QQQ** PUT 745 2026-10-30 (1DTE): 3,007 traded vs OI 1,306
- **QQQ** PUT 775 2026-11-06 (8DTE): 2,540 traded vs OI 1,000
- **IWM** CALL 291 2026-11-06 (8DTE): 833 traded vs OI 792
- **SMH** PUT 600 2026-10-30 (1DTE): 1,373 traded vs OI 1,252
- **SMH** PUT 605 2026-10-30 (1DTE): 973 traded vs OI 262
- **AAPL** PUT 355 2026-10-30 (1DTE): 1,514 traded vs OI 1,471
- **AAPL** PUT 320 2026-11-04 (6DTE): 500 traded vs OI 465
- **AMZN** PUT 220 2026-11-06 (8DTE): 2,284 traded vs OI 1,272
- **AMZN** PUT 220 2026-10-30 (1DTE): 16,857 traded vs OI 7,936
- **AMZN** PUT 220 2026-11-02 (4DTE): 1,037 traded vs OI 151
- **AMZN** CALL 257.5 2026-11-20 (22DTE): 893 traded vs OI 700

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
