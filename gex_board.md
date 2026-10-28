# GEX + FLOW SCAN - Wed Oct 28, 12:00 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (4)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:40 | **HOOD** | **CALLS** | FLOW SURGE | 10/30 96C | 0.77 | 0.66 | -1% (3m) | **-14%** | +49% | 93.02 |
| 11:05 | **HOOD** | **CALLS** | FLOW SURGE | 10/30 97C | 0.63 | 0.46 | +19% (1m) | **-27%** | +53% | 93.44 |
| 10:50 | **IWM** | **CALLS** | FLOW SURGE | 10/30 284C | 0.57 | 0.54 | +7% (2m) | **-5%** (done) | +22% | 280.64 |
| 10:20 | **IWM** | **CALLS** | FLOW SURGE | 10/29 284C | 0.47 | 0.34 | +11% (0m) | **-28%** (done) | +27% | 281.41 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **HOOD** | 91.08 | FLOW SURGE | **CALLS** | 43 | 10/30 96C @ 0.68 (delta 0.21) = est +44% at 92.5 | NEG -$17.3M | - | 100 | 90 | +$4.3M | +$148k bull / +$0 bear | out (clean 30, ADX 28, RVol 1.1) |
| 2 | **AAPL** | 345.29 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 33 | none: 81 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (46 contracts' greeks worked out here) | POS +$346.8M | 341.48 | 350 | 345 | +$703k | +$36k bull / -$103k bear | out (clean 29, ADX 19, RVol 0.5) |
| 3 | **MSTR** | 139.78 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 30 | none: 26 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$17.4M | - | 152.5 | 140 | -$112k | +$0 bull / -$26k bear | out (clean 27, ADX 8, RVol 0.3) |
| 4 | **IWM** | 280.14 | - | **-** | 23 | - | NEG -$349.9M | 281.31 | 280 | 270 | +$9.5M | +$73k bull / -$410k bear | out (clean 24, ADX 19, RVol 0.8) |
| 5 | **PLTR** | 194.71 | - | **-** | 22 | - | POS +$45.9M | 189.15 | 200 | 190 | -$867k | +$0 bull / -$91k bear | out (clean 27, ADX 49, RVol 0.6) |
| 6 | **META** | 614.37 | - | **-** | 21 | - | NEG -$265.1M | 636.02 | 650 | 610 | +$9.0M | +$0 bull / -$478k bear | out (clean 29, ADX 24, RVol 0.6) |
| 7 | **MSFT** | 527.53 | - | **-** | 21 | - | POS +$457.6M | - | 550 | 500 | +$2.5M | +$299k bull / +$0 bear | out (clean 30, ADX 24, RVol 0.8) |
| 8 | **MU** | 970.84 | - | **-** | 20 | - | POS +$625.9M | - | 950 | 950 | +$22.1M | +$2.8M bull / -$68k bear | out (clean 28, ADX 33, RVol 0.3) |
| 9 | **AMD** | 567.11 | - | **-** | 18 | - | POS +$172.4M | - | 600 | 550 | +$2.8M | +$44k bull / -$352k bear | out (clean 29, ADX 26, RVol 0.5) |
| 10 | **SHOP** | 166.21 | - | **-** | 18 | - | NEG -$4.8M | 171.29 | 175 | 165 | +$22k | - | out (clean 27, ADX 28, RVol 1.5) |
| 11 | **NVDA** | 217.25 | - | **-** | 17 | - | POS +$531.0M | 209.94 | 220 | 215 | +$6.2M | +$390k bull / +$0 bear | out (clean 26, ADX 11, RVol 0.5) |
| 12 | **TSLA** | 401.43 | - | **-** | 17 | - | POS +$597.6M | - | 400 | 395 | -$19.2M | +$1.6M bull / +$0 bear | out (clean 29, ADX 17, RVol 0.3) |
| 13 | **GOOGL** | 324.19 | - | **-** | 17 | - | POS +$17.1M | 320.83 | 355 | 330 | -$2.0M | +$0 bull / -$270k bear | out (clean 33, ADX 15, RVol 0.4) |
| 14 | **ORCL** | 130.90 | - | **-** | 16 | - | POS +$11.1M | 126.62 | 135 | 130 | -$135k | +$0 bull / -$75k bear | out (clean 28, ADX 14, RVol 0.7) |
| 15 | **AVGO** | 346.28 | - | **-** | 15 | - | POS +$50.9M | 336.31 | 350 | 340 | +$739k | +$167k bull / -$35k bear | out (clean 29, ADX 14, RVol 0.5) |
| 16 | **SPY** | 771.33 | - | **-** | 14 | - | NEG -$2.2B | 773.57 | 780 | 750 | -$5.9M | +$0 bull / -$802k bear | out (clean 29, ADX 12, RVol 0.5) |
| 17 | **SMH** | 565.23 | - | **-** | 14 | - | POS +$60.2M | 559.85 | 570 | 555 | -$1.7M | - | out (clean 28, ADX 24, RVol 0.4) |
| 18 | **QQQ** | 722.24 | - | **-** | 13 | - | NEG -$1.6B | 727.58 | 720 | 720 | -$5.6M | +$0 bull / -$624k bear | out (clean 30, ADX 8, RVol 0.3) |
| 19 | **AMZN** | 252.51 | - | **-** | 8 | - | POS +$173.1M | 246.21 | 255 | 250 | +$2.2M | - | out (clean 32, ADX 22, RVol 0.5) |
| 20 | **SMCI** | 34.80 | - | **-** | 8 | - | POS +$19.0M | - | 35 | 35 | +$115k | - | out (clean 28, ADX 18, RVol 0.2) |
| 21 | **ARM** | 232.50 | - | **-** | 8 | - | POS +$2.1M | 222.51 | 227.5 | 250 | +$118k | - | out (clean 27, ADX 27, RVol 0.4) |
| 22 | **UBER** | 65.47 | - | **-** | 8 | - | NEG -$31.0M | - | 70 | 65 | -$13k | - | out (clean 28, ADX 30, RVol 0.8) |
| 23 | **NFLX** | 61.80 | - | **-** | 7 | - | NEG -$57.3M | - | 65 | 60 | +$1k | - | out (clean 32, ADX 38, RVol 0.4) |
| 24 | **BABA** | 100.26 | - | **-** | 7 | - | NEG -$13.8M | 103.48 | 102 | 100 | +$31k | - | out (clean 28, ADX 12, RVol 0.4) |
| 25 | **DELL** | 495.18 | - | **-** | 5 | - | POS +$31.3M | - | 500 | 500 | +$17k | - | out (clean 30, ADX 17, RVol 0.7) |
| 26 | **CRM** | 240.69 | - | **-** | 5 | - | POS +$4.4M | 235.58 | 260 | 240 | +$7k | - | out (clean 27, ADX 20, RVol 0.3) |
| 27 | **COIN** | 158.51 | - | **-** | 4 | - | POS +$1.8M | 154.76 | 170 | 150 | -$17k | - | out (clean 29, ADX 12, RVol 0.4) |

## Big prints this scan (37)
- **QQQ** CALL 715 2026-10-28 (0DTE): 447 @ 8.16 = **+$365k** SELL | vol 2,261 / OI 4,055
- **QQQ** CALL 718 2026-10-28 (0DTE): 447 @ 5.79 = **+$259k** SELL | vol 4,847 / OI 389
- **TSLA** CALL 397.5 2026-10-28 (0DTE): 393 @ 4.90 = **+$193k** BUY | vol 16,738 / OI 2,326
- **TSLA** CALL 397.5 2026-10-28 (0DTE): 371 @ 4.90 = **+$182k** BUY | vol 16,738 / OI 2,326
- **MU** PUT 965 2026-10-28 (0DTE): 478 @ 3.30 = **+$158k** SELL | vol 15,460 / OI 17
- **AVGO** PUT 350 2026-10-30 (2DTE): 170 @ 8.10 = **+$138k** MID | vol 742 / OI 2,680
- **SPY** PUT 772 2026-10-28 (0DTE): 500 @ 2.41 = **+$120k** MID | vol 26,767 / OI 544
- **TSLA** CALL 410 2026-10-30 (2DTE): 497 @ 2.40 = **+$119k** BUY | vol 15,167 / OI 7,751
- **MU** CALL 970 2026-10-30 (2DTE): 50 @ 21.25 = **+$106k** BUY | vol 4,900 / OI 1,990
- **TSLA** PUT 400 2026-10-28 (0DTE): 700 @ 1.12 = **+$78k** SELL | vol 119,388 / OI 868
- **IWM** CALL 280 2026-10-30 (2DTE): 350 @ 2.09 = **+$73k** BUY | vol 2,820 / OI 8,542
- **IWM** PUT 280 2026-10-30 (2DTE): 350 @ 1.91 = **+$67k** BUY | vol 2,750 / OI 5,182
- **MU** CALL 960 2026-10-30 (2DTE): 20 @ 27.00 = **+$54k** BUY | vol 1,779 / OI 2,586
- **NVDA** CALL 217.5 2026-10-28 (0DTE): 450 @ 1.12 = **+$50k** BUY | vol 58,965 / OI 7,446
- **MSFT** CALL 550 2026-10-30 (2DTE): 95 @ 5.00 = **+$48k** MID | vol 1,831 / OI 7,100

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 741 2026-10-29 (1DTE): 625 traded vs OI 264
- **SPY** PUT 770 2026-11-03 (6DTE): 504 traded vs OI 484
- **QQQ** CALL 740 2026-10-29 (1DTE): 1,314 traded vs OI 1,202
- **QQQ** CALL 742 2026-10-29 (1DTE): 717 traded vs OI 701
- **QQQ** CALL 713 2026-10-28 (0DTE): 1,455 traded vs OI 1,449
- **IWM** PUT 280 2026-11-03 (6DTE): 510 traded vs OI 3
- **TSLA** CALL 412.5 2026-11-02 (5DTE): 519 traded vs OI 106

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
