# GEX + FLOW SCAN - Wed Oct 28, 03:20 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (8)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 14:35 | **QQQ** | **CALLS** | 1m WHIPSAW (R1 R2) | 10/28 730C | 0.67 | 0.19 | +64% (2m) | **-72%** | -70% | 724.9 hit |
| 14:35 | **SPY** | **CALLS** | 1m WHIPSAW (R1 R2 R5 R6) | 10/29 778C | 0.75 | 0.51 | +43% (2m) | **-32%** | +27% | 772.74 hit |
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
| 1 | **AVGO** | 350.78 | PINNED between the walls (positive gamma) - chop | **-** | 36 | - | POS +$61.6M | 340.33 | 350 | 350 | +$1.6M | +$228k bull / -$261k bear | out (clean 30, ADX 38, RVol 1.1) |
| 2 | **ORCL** | 146.85 | - | **-** | 34 | - | POS +$28.8M | - | 135 | 140 | -$29.7M | +$2.6M bull / -$463k bear | out (clean 30, ADX 57, RVol 4.2) |
| 3 | **AAPL** | 344.20 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 33 | none: 84 calls 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (45 contracts' greeks worked out here) | POS +$253.1M | 341.79 | 350 | 345 | +$2.8M | +$33k bull / -$113k bear | out (clean 28, ADX 11, RVol 0.6) |
| 4 | **MSTR** | 140.35 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 28 | none: 25 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$18.7M | - | 152.5 | 140 | +$1.4M | - | out (clean 27, ADX 25, RVol 0.7) |
| 5 | **HOOD** | 90.98 | - | **-** | 22 | - | NEG -$17.2M | - | 100 | 90 | +$4.7M | +$0 bull / -$41k bear | out (clean 29, ADX 14, RVol 1.0) |
| 6 | **NVDA** | 215.60 | - | **-** | 21 | - | POS +$386.9M | 210.46 | 220 | 215 | +$18.8M | +$660k bull / +$0 bear | out (clean 26, ADX 21, RVol 1.1) |
| 7 | **AMD** | 574.91 | - | **-** | 21 | - | POS +$188.6M | - | 600 | 550 | +$5.6M | +$795k bull / -$374k bear | out (clean 30, ADX 42, RVol 1.2) |
| 8 | **SMH** | 565.88 | - | **-** | 20 | - | POS +$78.7M | 559.48 | 570 | 555 | -$3.2M | +$26k bull / -$42k bear | out (clean 28, ADX 22, RVol 0.8) |
| 9 | **QQQ** | 722.69 | - | **-** | 18 | - | NEG -$1.2B | 726.59 | 720 | 720 | +$45.0M | +$482k bull / -$331k bear | out (clean 29, ADX 25, RVol 0.7) |
| 10 | **AMZN** | 254.02 | - | **-** | 18 | - | POS +$203.5M | 239.69 | 255 | 250 | +$58k | +$0 bull / -$119k bear | out (clean 31, ADX 29, RVol 1.2) |
| 11 | **GOOGL** | 325.00 | - | **-** | 18 | - | POS +$18.9M | 320.61 | 355 | 300 | -$2.8M | +$217k bull / -$226k bear | out (clean 32, ADX 26, RVol 1.1) |
| 12 | **SPY** | 771.04 | - | **-** | 17 | - | NEG -$2.2B | 772.97 | 770 | 765 | +$36.7M | +$639k bull / -$167k bear | out (clean 28, ADX 22, RVol 1.1) |
| 13 | **META** | 611.67 | - | **-** | 17 | - | NEG -$266.2M | 632.89 | 650 | 610 | +$5.3M | +$63k bull / +$0 bear | out (clean 29, ADX 21, RVol 0.9) |
| 14 | **PLTR** | 193.63 | - | **-** | 17 | - | POS +$37.4M | 189.69 | 200 | 190 | +$954k | +$28k bull / +$0 bear | out (clean 27, ADX 23, RVol 0.7) |
| 15 | **MU** | 980.38 | - | **-** | 17 | - | POS +$575.2M | - | 1,000 | 950 | +$16.7M | +$4.3M bull / -$2.4M bear | out (clean 28, ADX 24, RVol 0.8) |
| 16 | **TSLA** | 402.73 | - | **-** | 16 | - | POS +$620.0M | - | 400 | 400 | -$5.2M | +$1.0M bull / -$198k bear | out (clean 30, ADX 27, RVol 0.5) |
| 17 | **MSFT** | 528.35 | - | **-** | 16 | - | POS +$468.9M | - | 550 | 500 | +$288k | +$71k bull / -$125k bear | out (clean 29, ADX 24, RVol 1.0) |
| 18 | **IWM** | 279.62 | - | **-** | 11 | - | NEG -$350.7M | 280.68 | 280 | 270 | +$13.4M | - | out (clean 24, ADX 23, RVol 0.8) |
| 19 | **SMCI** | 35.24 | - | **-** | 10 | - | POS +$21.3M | - | 35 | 35 | +$92k | - | out (clean 28, ADX 31, RVol 1.0) |
| 20 | **COIN** | 159.04 | - | **-** | 8 | - | POS +$1.8M | 155.27 | 170 | 150 | +$138k | - | out (clean 28, ADX 14, RVol 1.1) |
| 21 | **ARM** | 233.00 | - | **-** | 8 | - | POS +$2.0M | 221.03 | 227.5 | 250 | +$321k | - | out (clean 26, ADX 23, RVol 0.7) |
| 22 | **DELL** | 495.74 | - | **-** | 7 | - | POS +$31.6M | - | 500 | 500 | +$250k | - | out (clean 31, ADX 23, RVol 0.6) |
| 23 | **UBER** | 65.19 | - | **-** | 7 | - | NEG -$32.6M | - | 70 | 65 | +$59k | - | out (clean 29, ADX 20, RVol 0.6) |
| 24 | **SHOP** | 166.99 | - | **-** | 7 | - | NEG -$3.8M | 171.02 | 175 | 165 | -$21k | - | out (clean 28, ADX 16, RVol 0.5) |
| 25 | **BABA** | 100.38 | - | **-** | 7 | - | NEG -$12.4M | 103.12 | 102 | 100 | +$36k | - | out (clean 28, ADX 24, RVol 0.5) |
| 26 | **CRM** | 240.62 | - | **-** | 5 | - | POS +$5.0M | 235.57 | 260 | 240 | +$34k | - | out (clean 26, ADX 14, RVol 0.5) |
| 27 | **NFLX** | 61.63 | - | **-** | 4 | - | NEG -$59.0M | - | 65 | 60 | -$6k | - | out (clean 31, ADX 12, RVol 0.7) |

## Big prints this scan (111)
- **TSLA** PUT 405 2026-10-30 (2DTE): 401 @ 6.04 = **+$242k** SELL | vol 11,343 / OI 157
- **QQQ** CALL 715 2026-10-28 (0DTE): 170 @ 10.19 = **+$173k** BUY | vol 3,320 / OI 4,055
- **QQQ** CALL 716 2026-10-28 (0DTE): 170 @ 9.26 = **+$157k** BUY | vol 1,795 / OI 528
- **AMD** CALL 575 2026-10-30 (2DTE): 100 @ 13.40 = **+$134k** BUY | vol 4,074 / OI 1,973
- **MU** CALL 970 2026-10-28 (0DTE): 92 @ 12.54 = **+$115k** BUY | vol 42,567 / OI 3,109
- **MU** PUT 975 2026-10-30 (2DTE): 58 @ 18.25 = **+$106k** BUY | vol 3,580 / OI 305
- **ORCL** CALL 147 2026-10-30 (2DTE): 200 @ 4.47 = **+$89k** BUY | vol 5,263 / OI 0
- **MU** PUT 975 2026-10-30 (2DTE): 50 @ 17.60 = **+$88k** BUY | vol 3,580 / OI 305
- **AVGO** CALL 347.5 2026-11-04 (7DTE): 81 @ 10.67 = **+$86k** MID | vol 153 / OI 14
- **AAPL** PUT 357.5 2026-10-30 (2DTE): 66 @ 12.87 = **+$85k** MID | vol 1,343 / OI 1,973
- **AAPL** PUT 357.5 2026-10-30 (2DTE): 66 @ 12.87 = **+$85k** MID | vol 1,343 / OI 1,973
- **AMD** CALL 575 2026-10-28 (0DTE): 200 @ 4.20 = **+$84k** BUY | vol 15,243 / OI 552
- **MU** PUT 985 2026-10-28 (0DTE): 120 @ 7.00 = **+$84k** SELL | vol 4,723 / OI 25
- **MU** PUT 980 2026-10-28 (0DTE): 195 @ 4.18 = **+$82k** SELL | vol 9,702 / OI 138
- **AMD** CALL 555 2026-10-30 (2DTE): 30 @ 25.65 = **+$77k** MID | vol 616 / OI 804

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 775 2026-11-03 (6DTE): 511 traded vs OI 494
- **SPY** PUT 764 2026-10-30 (2DTE): 3,657 traded vs OI 3,570
- **SPY** CALL 788 2026-11-03 (6DTE): 545 traded vs OI 216
- **SPY** CALL 784 2026-11-03 (6DTE): 721 traded vs OI 155
- **SPY** PUT 776 2026-10-29 (1DTE): 520 traded vs OI 86
- **SPY** CALL 775 2026-11-11 (14DTE): 517 traded vs OI 0
- **SPY** CALL 775 2026-11-13 (16DTE): 1,659 traded vs OI 1,637
- **SPY** PUT 765 2026-11-04 (7DTE): 501 traded vs OI 459
- **QQQ** PUT 699 2026-10-30 (2DTE): 1,566 traded vs OI 1,502
- **QQQ** PUT 715 2026-11-04 (7DTE): 501 traded vs OI 341
- **QQQ** CALL 740 2026-11-13 (16DTE): 3,817 traded vs OI 1,570
- **QQQ** CALL 760 2026-11-13 (16DTE): 3,619 traded vs OI 1,619
- **QQQ** PUT 718 2026-11-04 (7DTE): 544 traded vs OI 65
- **NVDA** CALL 230 2026-11-02 (5DTE): 3,095 traded vs OI 2,671
- **NVDA** PUT 207.5 2026-10-30 (2DTE): 5,522 traded vs OI 5,291

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
