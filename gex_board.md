# GEX + FLOW SCAN - Wed Oct 28, 03:10 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (8)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 14:35 | **QQQ** | **CALLS** | 1m WHIPSAW (R1 R2) | 10/28 730C | 0.67 | 0.28 | +64% (2m) | **-58%** | -70% | 724.9 hit |
| 14:35 | **SPY** | **CALLS** | 1m WHIPSAW (R1 R2 R5 R6) | 10/29 778C | 0.75 | 0.48 | +43% (2m) | **-36%** | +27% | 772.74 hit |
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
| 1 | **ORCL** | 145.75 | FLOW SURGE | **PUTS** | 55 | none: 23 puts 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$31.0M | - | 135 | 140 | -$33.4M | +$1.3M bull / -$2.8M bear | out (clean 30, ADX 54, RVol 6.7) |
| 2 | **AAPL** | 344.85 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 33 | 10/28 345C @ 0.41 (delta 0.45) = est +132% at 345.97 | POS +$295.7M | 342.35 | 350 | 345 | +$2.2M | +$243k bull / -$712k bear | out (clean 28, ADX 12, RVol 0.7) |
| 3 | **SMH** | 566.79 | - | **-** | 22 | - | POS +$72.5M | 560.03 | 570 | 555 | -$3.5M | +$26k bull / +$0 bear | out (clean 28, ADX 24, RVol 1.1) |
| 4 | **AMD** | 575.77 | - | **-** | 22 | - | POS +$174.1M | - | 600 | 550 | +$5.0M | +$799k bull / -$426k bear | out (clean 30, ADX 43, RVol 1.4) |
| 5 | **NVDA** | 215.94 | - | **-** | 20 | - | POS +$422.4M | 210.65 | 220 | 215 | +$16.8M | +$495k bull / -$26k bear | out (clean 26, ADX 19, RVol 1.0) |
| 6 | **AVGO** | 350.92 | - | **-** | 20 | - | POS +$62.6M | 341.11 | 350 | 350 | +$834k | +$156k bull / -$406k bear | out (clean 29, ADX 38, RVol 1.1) |
| 7 | **ARM** | 233.79 | - | **-** | 19 | - | POS +$2.8M | - | 227.5 | 250 | +$342k | +$51k bull / -$105k bear | out (clean 26, ADX 24, RVol 1.2) |
| 8 | **SPY** | 771.14 | - | **-** | 18 | - | NEG -$2.7B | 772.89 | 770 | 765 | +$22.2M | +$115k bull / -$985k bear | out (clean 28, ADX 23, RVol 1.6) |
| 9 | **QQQ** | 723.53 | - | **-** | 18 | - | NEG -$1.5B | 727.17 | 720 | 720 | +$33.4M | +$1.7M bull / -$1.0M bear | out (clean 29, ADX 26, RVol 0.8) |
| 10 | **AMZN** | 254.18 | - | **-** | 18 | - | POS +$197.2M | 246.73 | 255 | 250 | -$248k | +$28k bull / -$519k bear | out (clean 31, ADX 27, RVol 1.3) |
| 11 | **MSFT** | 529.31 | - | **-** | 18 | - | POS +$468.6M | - | 550 | 500 | -$2.0M | +$338k bull / -$444k bear | out (clean 29, ADX 25, RVol 1.4) |
| 12 | **GOOGL** | 325.02 | - | **-** | 18 | - | POS +$18.1M | 320.63 | 355 | 300 | -$2.8M | +$251k bull / -$104k bear | out (clean 32, ADX 25, RVol 1.1) |
| 13 | **PLTR** | 194.14 | - | **-** | 18 | - | POS +$36.1M | 189.65 | 200 | 190 | +$993k | +$132k bull / +$0 bear | out (clean 27, ADX 24, RVol 0.8) |
| 14 | **TSLA** | 403.43 | - | **-** | 17 | - | POS +$601.5M | - | 400 | 400 | -$8.0M | +$1.1M bull / -$70k bear | out (clean 30, ADX 27, RVol 0.6) |
| 15 | **META** | 612.29 | - | **-** | 17 | - | NEG -$270.6M | 634.72 | 650 | 610 | +$4.8M | +$0 bull / -$310k bear | out (clean 29, ADX 21, RVol 0.9) |
| 16 | **MU** | 979.78 | - | **-** | 17 | - | POS +$512.2M | - | 1,000 | 950 | +$15.0M | +$2.9M bull / -$6.5M bear | out (clean 28, ADX 25, RVol 1.0) |
| 17 | **IWM** | 279.96 | - | **-** | 12 | - | NEG -$472.8M | 280.73 | 280 | 270 | +$13.1M | - | out (clean 24, ADX 26, RVol 0.9) |
| 18 | **HOOD** | 91.00 | - | **-** | 12 | - | NEG -$18.1M | - | 100 | 90 | +$4.7M | - | out (clean 29, ADX 16, RVol 0.9) |
| 19 | **MSTR** | 140.75 | - | **-** | 10 | - | POS +$18.7M | - | 152.5 | 140 | +$1.4M | - | out (clean 27, ADX 26, RVol 0.9) |
| 20 | **COIN** | 159.18 | - | **-** | 9 | - | POS +$1.7M | 155.49 | 170 | 150 | +$130k | - | out (clean 28, ADX 16, RVol 1.4) |
| 21 | **SMCI** | 35.27 | - | **-** | 9 | - | POS +$20.6M | - | 35 | 35 | +$76k | - | out (clean 28, ADX 32, RVol 1.0) |
| 22 | **DELL** | 495.51 | - | **-** | 8 | - | POS +$29.9M | - | 500 | 500 | +$235k | - | out (clean 31, ADX 24, RVol 0.9) |
| 23 | **SHOP** | 167.34 | - | **-** | 8 | - | NEG -$5.2M | 172.93 | 175 | 165 | -$24k | - | out (clean 28, ADX 17, RVol 0.4) |
| 24 | **BABA** | 100.56 | - | **-** | 7 | - | NEG -$13.9M | 103.44 | 102 | 100 | +$36k | - | out (clean 28, ADX 25, RVol 0.5) |
| 25 | **UBER** | 65.19 | - | **-** | 6 | - | NEG -$34.2M | - | 70 | 65 | +$58k | - | out (clean 30, ADX 19, RVol 0.6) |
| 26 | **CRM** | 240.90 | - | **-** | 5 | - | POS +$4.0M | 236.52 | 260 | 240 | +$33k | - | out (clean 26, ADX 13, RVol 0.3) |
| 27 | **NFLX** | 61.70 | - | **-** | 4 | - | NEG -$58.4M | - | 65 | 60 | -$21k | - | out (clean 31, ADX 13, RVol 0.7) |

## Big prints this scan (102)
- **ORCL** CALL 145 2026-10-30 (2DTE): 1,901 @ 4.54 = **+$863k** BUY | vol 21,565 / OI 0
- **QQQ** PUT 720 2026-10-28 (0DTE): 1,500 @ 1.50 = **+$225k** BUY | vol 131,514 / OI 2,738
- **MU** PUT 990 2026-10-28 (0DTE): 200 @ 11.22 = **+$224k** SELL | vol 4,037 / OI 19
- **MU** CALL 980 2026-10-30 (2DTE): 100 @ 21.00 = **+$210k** BUY | vol 7,266 / OI 1,631
- **ORCL** CALL 145 2026-10-30 (2DTE): 443 @ 4.52 = **+$200k** MID | vol 21,565 / OI 0
- **ORCL** CALL 145 2026-10-30 (2DTE): 441 @ 4.52 = **+$199k** MID | vol 21,565 / OI 0
- **GOOGL** PUT 322.5 2026-10-30 (2DTE): 200 @ 8.60 = **+$172k** MID | vol 1,730 / OI 1,055
- **MU** CALL 965 2026-10-28 (0DTE): 100 @ 16.95 = **+$170k** BUY | vol 13,834 / OI 281
- **ORCL** CALL 140 2026-10-30 (2DTE): 219 @ 7.45 = **+$163k** SELL | vol 26,584 / OI 14,861
- **AAPL** PUT 357.5 2026-10-30 (2DTE): 124 @ 13.09 = **+$162k** MID | vol 1,093 / OI 1,973
- **MU** PUT 985 2026-10-28 (0DTE): 200 @ 7.72 = **+$154k** SELL | vol 4,179 / OI 25
- **MU** CALL 990 2026-10-30 (2DTE): 89 @ 16.25 = **+$145k** BUY | vol 4,127 / OI 3,193
- **NVDA** PUT 215 2026-11-02 (5DTE): 545 @ 2.65 = **+$144k** SELL | vol 3,198 / OI 516
- **ORCL** CALL 150 2026-10-30 (2DTE): 570 @ 2.51 = **+$143k** BUY | vol 22,300 / OI 0
- **MU** PUT 980 2026-10-28 (0DTE): 199 @ 6.50 = **+$129k** MID | vol 7,407 / OI 138

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 786 2026-10-30 (2DTE): 3,826 traded vs OI 3,334
- **SPY** PUT 696 2026-10-30 (2DTE): 1,015 traded vs OI 527
- **SPY** CALL 781 2026-11-02 (5DTE): 615 traded vs OI 586
- **SPY** CALL 775 2026-11-09 (12DTE): 503 traded vs OI 148
- **SPY** PUT 725 2026-11-09 (12DTE): 556 traded vs OI 132
- **SPY** PUT 715 2026-11-09 (12DTE): 542 traded vs OI 27
- **SPY** PUT 772 2026-11-06 (9DTE): 827 traded vs OI 790
- **SPY** CALL 775 2026-11-27 (30DTE): 560 traded vs OI 415
- **QQQ** PUT 691 2026-10-28 (0DTE): 1,172 traded vs OI 0
- **QQQ** PUT 676 2026-10-29 (1DTE): 528 traded vs OI 0
- **QQQ** PUT 696 2026-10-29 (1DTE): 507 traded vs OI 0
- **QQQ** CALL 723 2026-11-06 (9DTE): 524 traded vs OI 445
- **QQQ** PUT 690 2026-11-27 (30DTE): 2,059 traded vs OI 1,440
- **IWM** CALL 280 2026-11-04 (7DTE): 536 traded vs OI 170
- **IWM** CALL 277 2026-10-28 (0DTE): 1,051 traded vs OI 1,031

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
