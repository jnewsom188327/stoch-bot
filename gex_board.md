# GEX + FLOW SCAN - Wed Oct 28, 03:50 PM ET
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
| 1 | **AMZN** | 254.90 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 44 | none: 84 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (31 contracts' greeks worked out here) | POS +$206.1M | 247.86 | 255 | 250 | -$2.0M | +$0 bull / -$173k bear | out (clean 31, ADX 37, RVol 1.7) |
| 2 | **NVDA** | 215.21 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 43 | 10/28 215C @ 0.72 (delta 0.56) = est +124% at 216.64 | POS +$355.7M | 210.67 | 220 | 215 | +$22.7M | +$381k bull / -$503k bear | out (clean 26, ADX 29, RVol 1.1) |
| 3 | **AAPL** | 344.44 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 38 | none: 84 calls 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (48 contracts' greeks worked out here) | POS +$250.1M | 342.59 | 350 | 345 | +$4.1M | +$0 bull / -$107k bear | out (clean 28, ADX 9, RVol 1.2) |
| 4 | **ORCL** | 145.28 | - | **-** | 32 | - | POS +$33.7M | - | 135 | 140 | -$27.9M | +$1.5M bull / +$0 bear | out (clean 30, ADX 59, RVol 3.1) |
| 5 | **AVGO** | 350.40 | PINNED between the walls (positive gamma) - chop | **-** | 28 | - | POS +$63.5M | 338.93 | 350 | 350 | +$1.4M | - | out (clean 29, ADX 37, RVol 1.5) |
| 6 | **AMD** | 577.19 | - | **-** | 21 | - | POS +$185.7M | - | 580 | 550 | +$4.0M | +$0 bull / -$772k bear | out (clean 30, ADX 43, RVol 1.2) |
| 7 | **COIN** | 161.63 | - | **-** | 21 | - | POS +$4.5M | - | 170 | 150 | -$340k | +$0 bull / -$252k bear | out (clean 27, ADX 19, RVol 1.1) |
| 8 | **IWM** | 280.69 | - | **-** | 20 | - | NEG -$4.3M | 280.74 | 280 | 270 | +$10.9M | +$0 bull / -$136k bear | out (clean 24, ADX 25, RVol 0.7) |
| 9 | **SMH** | 567.25 | - | **-** | 20 | - | POS +$95.4M | 560.58 | 570 | 555 | -$3.5M | +$0 bull / -$282k bear | out (clean 28, ADX 20, RVol 0.9) |
| 10 | **GOOGL** | 325.35 | - | **-** | 20 | - | POS +$20.1M | 320.5 | 355 | 300 | -$2.7M | +$992k bull / -$1.5M bear | out (clean 32, ADX 20, RVol 2.5) |
| 11 | **QQQ** | 724.67 | - | **-** | 19 | - | NEG -$783.7M | 726.94 | 720 | 720 | +$36.4M | +$0 bull / -$1.4M bear | out (clean 29, ADX 26, RVol 1.4) |
| 12 | **MSFT** | 530.13 | - | **-** | 19 | - | POS +$487.3M | - | 550 | 500 | -$2.3M | +$37k bull / -$564k bear | out (clean 29, ADX 22, RVol 1.8) |
| 13 | **MSTR** | 142.68 | - | **-** | 19 | - | POS +$23.7M | - | 152.5 | 150 | +$1.0M | +$0 bull / -$28k bear | out (clean 26, ADX 30, RVol 0.6) |
| 14 | **SPY** | 771.88 | - | **-** | 18 | - | NEG -$1.1B | 772.86 | 780 | 765 | +$14.1M | +$0 bull / -$625k bear | out (clean 28, ADX 22, RVol 1.7) |
| 15 | **MU** | 986.25 | - | **-** | 18 | - | POS +$610.2M | - | 1,000 | 950 | +$10.4M | +$30k bull / -$3.9M bear | out (clean 29, ADX 26, RVol 1.5) |
| 16 | **META** | 611.89 | - | **-** | 17 | - | NEG -$285.1M | 634.84 | 650 | 610 | +$7.8M | +$210k bull / -$319k bear | out (clean 29, ADX 16, RVol 1.1) |
| 17 | **NFLX** | 61.87 | - | **-** | 17 | - | NEG -$59.8M | - | 65 | 60 | -$289k | +$0 bull / -$44k bear | out (clean 31, ADX 16, RVol 1.0) |
| 18 | **TSLA** | 403.67 | - | **-** | 16 | - | POS +$539.7M | - | 400 | 400 | -$5.7M | +$613k bull / -$2.8M bear | out (clean 30, ADX 26, RVol 0.5) |
| 19 | **HOOD** | 91.77 | - | **-** | 12 | - | NEG -$17.4M | - | 100 | 90 | +$4.4M | - | out (clean 29, ADX 14, RVol 1.5) |
| 20 | **ARM** | 234.45 | - | **-** | 9 | - | POS +$2.8M | - | 227.5 | 250 | +$526k | - | out (clean 26, ADX 23, RVol 0.8) |
| 21 | **SMCI** | 35.49 | - | **-** | 8 | - | POS +$22.3M | - | 35 | 35 | +$62k | - | out (clean 28, ADX 30, RVol 0.7) |
| 22 | **SHOP** | 167.91 | - | **-** | 8 | - | NEG -$3.2M | 171.53 | 175 | 165 | -$25k | - | out (clean 28, ADX 14, RVol 0.9) |
| 23 | **DELL** | 493.60 | - | **-** | 7 | - | POS +$29.4M | - | 500 | 500 | +$325k | - | out (clean 31, ADX 20, RVol 0.8) |
| 24 | **UBER** | 65.19 | - | **-** | 7 | - | NEG -$31.7M | - | 70 | 65 | +$51k | - | out (clean 29, ADX 21, RVol 1.0) |
| 25 | **BABA** | 100.98 | - | **-** | 7 | - | NEG -$11.6M | 103.41 | 102 | 100 | +$31k | - | out (clean 28, ADX 26, RVol 0.4) |
| 26 | **PLTR** | 194.85 | - | **-** | 6 | - | POS +$48.0M | 190.02 | 200 | 190 | +$752k | - | out (clean 26, ADX 19, RVol 0.8) |
| 27 | **CRM** | 241.26 | - | **-** | 6 | - | POS +$7.3M | 234.66 | 260 | 240 | +$24k | - | out (clean 26, ADX 12, RVol 1.1) |

## Big prints this scan (75)
- **TSLA** CALL 400 2026-10-28 (0DTE): 2,925 @ 2.94 = **+$860k** SELL | vol 102,652 / OI 4,776
- **TSLA** CALL 390 2026-10-30 (2DTE): 525 @ 14.20 = **+$746k** SELL | vol 5,580 / OI 7,806
- **TSLA** PUT 400 2026-11-04 (7DTE): 450 @ 6.80 = **+$306k** BUY | vol 2,456 / OI 26
- **TSLA** PUT 400 2026-11-04 (7DTE): 450 @ 6.80 = **+$306k** BUY | vol 2,456 / OI 26
- **TSLA** CALL 402.5 2026-10-28 (0DTE): 2,925 @ 0.93 = **+$272k** SELL | vol 182,340 / OI 1,982
- **QQQ** CALL 710 2026-10-28 (0DTE): 200 @ 13.39 = **+$268k** SELL | vol 1,366 / OI 1,068
- **MU** CALL 985 2026-10-30 (2DTE): 150 @ 16.25 = **+$244k** SELL | vol 4,095 / OI 957
- **QQQ** CALL 712 2026-10-28 (0DTE): 200 @ 11.41 = **+$228k** SELL | vol 1,283 / OI 639
- **QQQ** CALL 719 2026-10-29 (1DTE): 280 @ 6.98 = **+$195k** SELL | vol 1,448 / OI 194
- **IWM** CALL 282 2026-10-29 (1DTE): 2,188 @ 0.62 = **+$136k** SELL | vol 16,405 / OI 10,649
- **META** PUT 625 2026-10-28 (0DTE): 89 @ 14.25 = **+$127k** MID | vol 1,155 / OI 1,146
- **ORCL** CALL 150 2026-10-30 (2DTE): 438 @ 2.63 = **+$115k** BUY | vol 36,790 / OI 0
- **TSLA** CALL 410 2026-10-30 (2DTE): 450 @ 2.43 = **+$109k** BUY | vol 26,937 / OI 7,751
- **NVDA** CALL 205 2026-10-30 (2DTE): 100 @ 10.10 = **+$101k** SELL | vol 9,247 / OI 1,545
- **TSLA** PUT 405 2026-10-30 (2DTE): 164 @ 6.10 = **+$100k** BUY | vol 12,498 / OI 157

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 747 2026-10-29 (1DTE): 514 traded vs OI 372
- **SPY** CALL 779 2026-11-02 (5DTE): 522 traded vs OI 313
- **SPY** PUT 777 2026-10-29 (1DTE): 544 traded vs OI 76
- **SPY** PUT 710 2026-11-02 (5DTE): 701 traded vs OI 227
- **SPY** PUT 763 2026-10-30 (2DTE): 3,931 traded vs OI 3,854
- **SPY** PUT 754 2026-11-02 (5DTE): 504 traded vs OI 203
- **SPY** CALL 778 2026-10-30 (2DTE): 4,425 traded vs OI 4,370
- **SPY** CALL 782 2026-11-02 (5DTE): 513 traded vs OI 184
- **SPY** PUT 755 2026-11-03 (6DTE): 2,490 traded vs OI 1,622
- **SPY** PUT 752 2026-11-04 (7DTE): 540 traded vs OI 154
- **SPY** PUT 759 2026-11-03 (6DTE): 2,091 traded vs OI 179
- **SPY** CALL 780 2026-11-10 (13DTE): 620 traded vs OI 0
- **SPY** PUT 740 2026-11-10 (13DTE): 671 traded vs OI 0
- **QQQ** PUT 706 2026-10-30 (2DTE): 1,695 traded vs OI 1,670
- **QQQ** PUT 686 2026-10-30 (2DTE): 1,199 traded vs OI 1,032

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
