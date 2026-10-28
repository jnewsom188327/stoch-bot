# GEX + FLOW SCAN - Wed Oct 28, 03:55 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (8)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 14:35 | **QQQ** | **CALLS** | 1m WHIPSAW (R1 R2) | 10/28 730C | 0.67 | 0.10 | +64% (2m) | **-85%** (done) | -70% | 724.9 hit |
| 14:35 | **SPY** | **CALLS** | 1m WHIPSAW (R1 R2 R5 R6) | 10/29 778C | 0.75 | 0.45 | +43% (2m) | **-40%** (done) | +27% | 772.74 hit |
| 12:56 | **QQQ** | **CALLS** | 1m WHIPSAW (R1 R2) | 10/28 730C | 0.63 | 0.67 | +24% (10m) | **+6%** (done) | -35% | 723.9 |
| 12:56 | **SPY** | **CALLS** | 1m WHIPSAW (R1 R2) | 10/29 779C | 0.63 | 0.51 | +3% (9m) | **-19%** (done) | +10% | 772.67 |
| 11:40 | **HOOD** | **CALLS** | FLOW SURGE | 10/30 96C | 0.77 | 0.55 | -1% (3m) | **-29%** (done) | +49% | 93.02 |
| 11:05 | **HOOD** | **CALLS** | FLOW SURGE | 10/30 97C | 0.63 | 0.45 | +19% (1m) | **-29%** (done) | +53% | 93.44 |
| 10:50 | **IWM** | **CALLS** | FLOW SURGE | 10/30 284C | 0.57 | 0.54 | +7% (2m) | **-5%** (done) | +22% | 280.64 |
| 10:20 | **IWM** | **CALLS** | FLOW SURGE | 10/29 284C | 0.47 | 0.34 | +11% (0m) | **-28%** (done) | +27% | 281.41 |

## 1m RULES on SPY / QQQ - loose (4 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 14:34 | QQQ | 1m WHIPSAW | R1 R2 | CALLS | WITH you | **FIRE** QQQ261028C00730000 |
| 14:34 | SPY | 1m WHIPSAW | R1 R2 R5 R6 | CALLS | WITH you | **FIRE** SPY261029C00778000 |
| 12:55 | QQQ | 1m WHIPSAW | R1 R2 | CALLS | WITH you | **FIRE** QQQ261028C00730000 |
| 12:55 | SPY | 1m WHIPSAW | R1 R2 | CALLS | WITH you | **FIRE** SPY261029C00779000 |

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **NVDA** | 214.88 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 44 | 10/28 215C @ 0.71 (delta 0.48) = est +79% at 216.31 | POS +$317.1M | 210.62 | 220 | 215 | +$21.6M | +$381k bull / -$803k bear | out (clean 26, ADX 28, RVol 1.3) |
| 2 | **AMZN** | 255.07 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 44 | none: 84 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (28 contracts' greeks worked out here) | POS +$218.4M | 249.17 | 255 | 250 | -$1.2M | +$285k bull / -$173k bear | out (clean 31, ADX 39, RVol 1.7) |
| 3 | **IWM** | 280.82 | FLIP CROSS up into positive gamma | **CALLS** | 36 | 10/29 283C @ 0.47 (delta 0.26) = est +164% at 283 | POS +$79.8M | 280.76 | 280 | 270 | +$10.6M | +$0 bull / -$136k bear | out (clean 24, ADX 26, RVol 1.1) |
| 4 | **AAPL** | 344.51 | PINNED between the walls (positive gamma) - chop | **-** | 36 | - | POS +$281.8M | 342.74 | 345 | 345 | +$4.8M | +$186k bull / -$107k bear | out (clean 28, ADX 10, RVol 1.7) |
| 5 | **ORCL** | 145.24 | - | **-** | 31 | - | POS +$30.8M | - | 135 | 140 | -$27.5M | +$1.9M bull / +$0 bear | out (clean 30, ADX 57, RVol 3.5) |
| 6 | **COIN** | 161.54 | - | **-** | 23 | - | POS +$4.7M | - | 170 | 150 | -$381k | +$0 bull / -$252k bear | out (clean 27, ADX 21, RVol 1.6) |
| 7 | **SMH** | 567.06 | - | **-** | 22 | - | POS +$96.3M | 560.17 | 570 | 555 | -$3.7M | +$0 bull / -$282k bear | out (clean 28, ADX 21, RVol 1.3) |
| 8 | **AMD** | 577.09 | - | **-** | 21 | - | POS +$187.2M | - | 580 | 550 | +$3.3M | +$0 bull / -$1.1M bear | out (clean 30, ADX 44, RVol 1.1) |
| 9 | **QQQ** | 724.93 | - | **-** | 20 | - | NEG -$684.0M | 726.81 | 720 | 720 | +$33.2M | +$0 bull / -$1.6M bear | out (clean 29, ADX 28, RVol 1.7) |
| 10 | **MSFT** | 529.48 | - | **-** | 20 | - | POS +$483.1M | - | 550 | 500 | -$3.8M | +$37k bull / -$1.1M bear | out (clean 29, ADX 23, RVol 2.2) |
| 11 | **GOOGL** | 325.08 | - | **-** | 20 | - | POS +$16.4M | 320.56 | 355 | 300 | -$3.2M | +$992k bull / -$1.6M bear | out (clean 32, ADX 21, RVol 2.9) |
| 12 | **MU** | 986.87 | - | **-** | 20 | - | POS +$489.0M | - | 1,000 | 950 | +$8.6M | +$30k bull / -$5.3M bear | out (clean 29, ADX 28, RVol 2.4) |
| 13 | **SPY** | 771.99 | - | **-** | 19 | - | NEG -$871.8M | 772.81 | 780 | 750 | +$10.0M | +$0 bull / -$752k bear | out (clean 28, ADX 24, RVol 2.0) |
| 14 | **MSTR** | 143.10 | - | **-** | 19 | - | POS +$26.9M | - | 152.5 | 150 | +$920k | +$0 bull / -$28k bear | out (clean 26, ADX 32, RVol 0.8) |
| 15 | **TSLA** | 404.16 | - | **-** | 17 | - | POS +$707.0M | - | 400 | 400 | -$7.5M | +$613k bull / -$3.5M bear | out (clean 29, ADX 27, RVol 0.7) |
| 16 | **META** | 612.84 | - | **-** | 17 | - | NEG -$291.1M | 635.59 | 650 | 610 | +$7.2M | +$210k bull / -$351k bear | out (clean 28, ADX 16, RVol 1.1) |
| 17 | **NFLX** | 61.94 | - | **-** | 17 | - | NEG -$60.5M | - | 65 | 60 | -$248k | +$0 bull / -$44k bear | out (clean 31, ADX 18, RVol 1.1) |
| 18 | **AVGO** | 351.69 | - | **-** | 12 | - | POS +$65.9M | 340.48 | 350 | 350 | +$1.1M | - | out (clean 29, ADX 38, RVol 2.0) |
| 19 | **HOOD** | 91.45 | - | **-** | 12 | - | NEG -$18.2M | - | 100 | 90 | +$4.4M | - | out (clean 29, ADX 16, RVol 1.3) |
| 20 | **ARM** | 235.09 | - | **-** | 10 | - | POS +$2.4M | - | 227.5 | 250 | +$514k | - | out (clean 26, ADX 24, RVol 1.5) |
| 21 | **SHOP** | 167.78 | - | **-** | 9 | - | NEG -$3.4M | 171.35 | 175 | 165 | -$25k | - | out (clean 28, ADX 15, RVol 1.1) |
| 22 | **SMCI** | 35.44 | - | **-** | 8 | - | POS +$22.0M | - | 35 | 35 | +$43k | - | out (clean 28, ADX 31, RVol 1.0) |
| 23 | **BABA** | 100.89 | - | **-** | 8 | - | NEG -$12.0M | 103.41 | 102 | 100 | +$33k | - | out (clean 28, ADX 27, RVol 0.6) |
| 24 | **PLTR** | 195.37 | - | **-** | 7 | - | POS +$61.5M | 190.13 | 200 | 190 | +$446k | - | out (clean 26, ADX 20, RVol 1.1) |
| 25 | **DELL** | 492.02 | - | **-** | 7 | - | POS +$30.2M | - | 500 | 500 | +$263k | - | out (clean 31, ADX 21, RVol 1.0) |
| 26 | **UBER** | 65.25 | - | **-** | 7 | - | NEG -$31.9M | 68.78 | 70 | 65 | +$50k | - | out (clean 29, ADX 20, RVol 1.1) |
| 27 | **CRM** | 242.31 | - | **-** | 6 | - | POS +$8.4M | 234.54 | 260 | 240 | +$17k | - | out (clean 26, ADX 13, RVol 1.5) |

## Big prints this scan (94)
- **MU** CALL 985 2026-10-30 (2DTE): 400 @ 17.20 = **+$688k** SELL | vol 4,164 / OI 957
- **ORCL** CALL 140 2026-10-30 (2DTE): 207 @ 7.15 = **+$148k** BUY | vol 29,403 / OI 14,861
- **SPY** CALL 772 2026-10-29 (1DTE): 570 @ 2.23 = **+$127k** SELL | vol 61,391 / OI 836
- **NVDA** CALL 205 2026-10-30 (2DTE): 100 @ 10.25 = **+$102k** SELL | vol 9,496 / OI 1,545
- **QQQ** CALL 701 2026-10-28 (0DTE): 46 @ 21.76 = **+$100k** SELL | vol 127 / OI 83
- **AMZN** PUT 242.5 2026-11-02 (5DTE): 168 @ 5.45 = **+$92k** MID | vol 237 / OI 116
- **MU** CALL 1,010 2026-10-30 (2DTE): 100 @ 8.20 = **+$82k** SELL | vol 3,676 / OI 1,578
- **AMD** CALL 550 2026-10-28 (0DTE): 32 @ 24.80 = **+$79k** SELL | vol 461 / OI 1,175
- **MSFT** PUT 530 2026-10-30 (2DTE): 50 @ 13.44 = **+$67k** BUY | vol 2,543 / OI 3,046
- **TSLA** CALL 390 2026-10-30 (2DTE): 44 @ 14.00 = **+$62k** SELL | vol 5,838 / OI 7,806
- **AAPL** CALL 342.5 2026-10-30 (2DTE): 160 @ 3.68 = **+$59k** BUY | vol 2,762 / OI 2,029
- **TSLA** CALL 390 2026-10-28 (0DTE): 44 @ 12.69 = **+$56k** SELL | vol 1,209 / OI 1,790
- **TSLA** CALL 405 2026-11-02 (5DTE): 100 @ 5.55 = **+$56k** SELL | vol 2,973 / OI 545
- **MSFT** PUT 510 2026-10-30 (2DTE): 100 @ 5.37 = **+$54k** BUY | vol 3,696 / OI 1,313
- **MSFT** CALL 530 2026-10-30 (2DTE): 42 @ 12.68 = **+$53k** SELL | vol 5,382 / OI 7,642

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 698 2026-10-30 (2DTE): 4,780 traded vs OI 1,949
- **QQQ** PUT 665 2026-10-29 (1DTE): 835 traded vs OI 775
- **QQQ** CALL 748 2026-11-02 (5DTE): 519 traded vs OI 156
- **QQQ** CALL 737 2026-10-30 (2DTE): 2,651 traded vs OI 2,538
- **QQQ** CALL 742 2026-10-30 (2DTE): 1,562 traded vs OI 1,537
- **QQQ** PUT 670 2026-11-13 (16DTE): 5,746 traded vs OI 5,298
- **QQQ** PUT 714 2026-11-04 (7DTE): 547 traded vs OI 114
- **QQQ** PUT 700 2026-11-13 (16DTE): 7,894 traded vs OI 7,333
- **IWM** PUT 269 2026-11-03 (6DTE): 1,593 traded vs OI 309
- **SMH** CALL 585 2026-11-02 (5DTE): 1,059 traded vs OI 23
- **SMH** CALL 585 2026-11-04 (7DTE): 858 traded vs OI 3
- **SMH** PUT 527.5 2026-10-30 (2DTE): 869 traded vs OI 696
- **NVDA** CALL 235 2026-11-13 (16DTE): 6,991 traded vs OI 6,971
- **NVDA** CALL 230 2026-11-11 (14DTE): 595 traded vs OI 0
- **NVDA** CALL 232.5 2026-11-13 (16DTE): 548 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
