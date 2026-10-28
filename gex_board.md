# GEX + FLOW SCAN - Wed Oct 28, 01:20 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (6)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 12:56 | **QQQ** | **CALLS** | 1m WHIPSAW (R1 R2) | 10/28 730C | 0.63 | 0.63 | +24% (10m) | **+0%** | -35% | 723.9 |
| 12:56 | **SPY** | **CALLS** | 1m WHIPSAW (R1 R2) | 10/29 779C | 0.63 | 0.52 | +3% (9m) | **-17%** | +10% | 772.67 |
| 11:40 | **HOOD** | **CALLS** | FLOW SURGE | 10/30 96C | 0.77 | 0.55 | -1% (3m) | **-29%** (done) | +49% | 93.02 |
| 11:05 | **HOOD** | **CALLS** | FLOW SURGE | 10/30 97C | 0.63 | 0.45 | +19% (1m) | **-29%** (done) | +53% | 93.44 |
| 10:50 | **IWM** | **CALLS** | FLOW SURGE | 10/30 284C | 0.57 | 0.54 | +7% (2m) | **-5%** (done) | +22% | 280.64 |
| 10:20 | **IWM** | **CALLS** | FLOW SURGE | 10/29 284C | 0.47 | 0.34 | +11% (0m) | **-28%** (done) | +27% | 281.41 |

## 1m RULES on SPY / QQQ - loose (2 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 12:55 | QQQ | 1m WHIPSAW | R1 R2 | CALLS | WITH you | **FIRE** QQQ261028C00730000 |
| 12:55 | SPY | 1m WHIPSAW | R1 R2 | CALLS | WITH you | **FIRE** SPY261029C00779000 |

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **ORCL** | 130.15 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 35 | none: 26 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$10.5M | 126.74 | 135 | 130 | -$753k | +$258k bull / +$0 bear | out (clean 29, ADX 14, RVol 0.4) |
| 2 | **SMH** | 565.26 | FLOW SURGE | **PUTS** | 33 | none: 180 puts 0-7DTE > 13 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (79 contracts' greeks worked out here) | POS +$63.1M | 559.74 | 570 | 555 | -$4.5M | +$129k bull / -$450k bear | out (clean 28, ADX 26, RVol 0.5) |
| 3 | **AAPL** | 345.55 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 32 | none: 84 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (44 contracts' greeks worked out here) | POS +$376.5M | 341.54 | 350 | 345 | +$573k | +$443k bull / +$0 bear | out (clean 28, ADX 17, RVol 0.5) |
| 4 | **HOOD** | 90.26 | - | **-** | 25 | - | NEG -$17.4M | - | 95 | 90 | +$4.0M | +$38k bull / +$0 bear | out (clean 30, ADX 24, RVol 1.3) |
| 5 | **AMD** | 569.45 | - | **-** | 19 | - | POS +$180.9M | - | 600 | 550 | +$2.3M | +$1.0M bull / -$790k bear | out (clean 29, ADX 37, RVol 0.8) |
| 6 | **META** | 612.27 | - | **-** | 19 | - | NEG -$265.1M | 634.36 | 650 | 610 | +$8.9M | +$324k bull / +$0 bear | out (clean 28, ADX 17, RVol 1.0) |
| 7 | **GOOGL** | 324.82 | - | **-** | 18 | - | POS +$18.6M | 321.16 | 355 | 330 | -$1.3M | +$200k bull / -$1.5M bear | out (clean 33, ADX 22, RVol 1.6) |
| 8 | **AVGO** | 348.57 | - | **-** | 18 | - | POS +$58.1M | 338.05 | 350 | 340 | -$921k | +$0 bull / -$66k bear | out (clean 29, ADX 31, RVol 0.6) |
| 9 | **MU** | 964.38 | - | **-** | 18 | - | POS +$623.0M | - | 950 | 900 | +$25.5M | +$2.3M bull / -$5.7M bear | out (clean 28, ADX 24, RVol 0.5) |
| 10 | **NVDA** | 217.15 | - | **-** | 17 | - | POS +$521.0M | 210.05 | 220 | 215 | +$9.0M | +$316k bull / -$63k bear | out (clean 26, ADX 14, RVol 0.5) |
| 11 | **ARM** | 232.75 | - | **-** | 17 | - | POS +$1.9M | 221.96 | 220 | 250 | +$77k | +$81k bull / +$0 bear | out (clean 26, ADX 22, RVol 0.7) |
| 12 | **MSFT** | 526.63 | - | **-** | 16 | - | POS +$426.5M | - | 550 | 500 | +$2.3M | +$222k bull / -$765k bear | out (clean 29, ADX 14, RVol 0.6) |
| 13 | **SPY** | 771.05 | - | **-** | 15 | - | NEG -$2.4B | 773.43 | 780 | 750 | -$15.2M | +$1.4M bull / -$101k bear | out (clean 29, ADX 16, RVol 0.8) |
| 14 | **TSLA** | 401.68 | - | **-** | 15 | - | POS +$607.1M | - | 400 | 395 | -$16.9M | +$1.0M bull / -$26k bear | out (clean 29, ADX 12, RVol 0.2) |
| 15 | **AMZN** | 253.03 | - | **-** | 15 | - | POS +$192.9M | 240.35 | 255 | 250 | -$270k | +$456k bull / -$810k bear | out (clean 32, ADX 19, RVol 0.6) |
| 16 | **MSTR** | 139.25 | - | **-** | 15 | - | POS +$15.9M | - | 152.5 | 140 | +$380k | +$33k bull / -$210k bear | out (clean 27, ADX 9, RVol 0.4) |
| 17 | **QQQ** | 721.92 | - | **-** | 14 | - | NEG -$1.8B | 727.93 | 720 | 720 | +$9.6M | +$2.9M bull / +$0 bear | out (clean 29, ADX 13, RVol 0.3) |
| 18 | **IWM** | 280.31 | - | **-** | 12 | - | NEG -$281.6M | 281.29 | 280 | 270 | +$9.6M | - | out (clean 24, ADX 23, RVol 0.6) |
| 19 | **BABA** | 100.16 | - | **-** | 12 | - | NEG -$13.8M | 103.23 | 102 | 100 | +$74k | - | out (clean 28, ADX 18, RVol 1.4) |
| 20 | **SHOP** | 168.48 | - | **-** | 11 | - | NEG -$3.4M | 171.97 | 175 | 165 | -$29k | - | out (clean 29, ADX 28, RVol 0.5) |
| 21 | **PLTR** | 193.82 | - | **-** | 9 | - | POS +$39.0M | 189.29 | 200 | 190 | +$234k | - | out (clean 27, ADX 45, RVol 0.4) |
| 22 | **SMCI** | 34.76 | - | **-** | 8 | - | POS +$18.6M | - | 35 | 35 | +$117k | - | out (clean 28, ADX 18, RVol 0.3) |
| 23 | **UBER** | 65.44 | - | **-** | 8 | - | NEG -$29.9M | 68.82 | 70 | 65 | +$5k | - | out (clean 30, ADX 35, RVol 0.8) |
| 24 | **NFLX** | 61.74 | - | **-** | 6 | - | NEG -$57.0M | - | 65 | 60 | -$99k | - | out (clean 31, ADX 18, RVol 0.7) |
| 25 | **COIN** | 158.13 | - | **-** | 4 | - | POS +$1.0M | 155.74 | 170 | 150 | +$43k | - | out (clean 29, ADX 7, RVol 0.4) |
| 26 | **DELL** | 494.74 | - | **-** | 4 | - | POS +$30.2M | - | 500 | 500 | +$59k | - | out (clean 31, ADX 13, RVol 0.3) |
| 27 | **CRM** | 240.79 | - | **-** | 4 | - | POS +$4.5M | 235.84 | 260 | 240 | +$18k | - | out (clean 27, ADX 13, RVol 0.4) |

## Big prints this scan (44)
- **SPY** PUT 767 2026-11-04 (7DTE): 555 @ 3.99 = **+$221k** SELL | vol 16,727 / OI 94
- **SPY** PUT 773 2026-10-28 (0DTE): 500 @ 2.81 = **+$140k** SELL | vol 41,469 / OI 703
- **SPY** PUT 767 2026-11-04 (7DTE): 338 @ 3.99 = **+$135k** SELL | vol 16,727 / OI 94
- **MU** CALL 925 2026-10-28 (0DTE): 28 @ 46.48 = **+$130k** BUY | vol 971 / OI 909
- **MU** CALL 925 2026-10-28 (0DTE): 28 @ 46.48 = **+$130k** BUY | vol 971 / OI 909
- **MU** CALL 965 2026-10-28 (0DTE): 100 @ 10.82 = **+$108k** BUY | vol 7,976 / OI 281
- **QQQ** CALL 724 2026-10-30 (2DTE): 172 @ 5.87 = **+$101k** BUY | vol 1,759 / OI 3,806
- **MU** CALL 970 2026-10-30 (2DTE): 40 @ 21.80 = **+$87k** BUY | vol 6,231 / OI 1,990
- **MU** CALL 975 2026-10-28 (0DTE): 168 @ 4.55 = **+$76k** BUY | vol 42,057 / OI 683
- **MU** CALL 970 2026-10-28 (0DTE): 100 @ 7.52 = **+$75k** BUY | vol 27,784 / OI 3,109
- **MU** PUT 1,000 2026-10-30 (2DTE): 16 @ 36.41 = **+$58k** SELL | vol 1,601 / OI 1,100
- **GOOGL** CALL 330 2026-11-04 (7DTE): 67 @ 8.69 = **+$58k** BUY | vol 197 / OI 173
- **MU** CALL 1,000 2026-10-30 (2DTE): 63 @ 9.15 = **+$58k** BUY | vol 13,488 / OI 8,792
- **MU** PUT 1,000 2026-10-30 (2DTE): 15 @ 36.24 = **+$54k** SELL | vol 1,601 / OI 1,100
- **GOOGL** CALL 332.5 2026-11-04 (7DTE): 67 @ 7.69 = **+$52k** BUY | vol 114 / OI 352

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 780 2026-11-02 (5DTE): 894 traded vs OI 877
- **QQQ** PUT 695 2026-11-02 (5DTE): 5,206 traded vs OI 5,103
- **QQQ** CALL 726 2026-10-30 (2DTE): 1,125 traded vs OI 1,029
- **QQQ** PUT 703 2026-11-02 (5DTE): 5,068 traded vs OI 315
- **IWM** PUT 275 2026-11-04 (7DTE): 593 traded vs OI 102
- **NVDA** PUT 225 2026-11-04 (7DTE): 516 traded vs OI 159
- **NVDA** PUT 210 2026-10-28 (0DTE): 5,345 traded vs OI 5,334
- **TSLA** PUT 402.5 2026-11-06 (9DTE): 509 traded vs OI 27
- **TSLA** CALL 407.5 2026-11-06 (9DTE): 551 traded vs OI 205
- **META** CALL 610 2026-10-30 (2DTE): 523 traded vs OI 54
- **MSFT** PUT 487.5 2026-10-30 (2DTE): 514 traded vs OI 216
- **GOOGL** CALL 330 2026-10-30 (2DTE): 7,373 traded vs OI 6,833
- **MU** PUT 870 2026-10-30 (2DTE): 711 traded vs OI 0
- **MU** CALL 1,050 2026-11-04 (7DTE): 500 traded vs OI 89
- **ORCL** CALL 138 2026-10-30 (2DTE): 1,904 traded vs OI 1,851

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
