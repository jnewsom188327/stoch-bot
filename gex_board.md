# GEX + FLOW SCAN - Wed Oct 28, 01:10 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (6)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 12:56 | **QQQ** | **CALLS** | 1m WHIPSAW (R1 R2) | 10/28 730C | 0.63 | 0.60 | +24% (10m) | **-5%** | -35% | 723.9 |
| 12:56 | **SPY** | **CALLS** | 1m WHIPSAW (R1 R2) | 10/29 779C | 0.63 | 0.53 | +3% (9m) | **-16%** | +10% | 772.67 |
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
| 1 | **ORCL** | 130.31 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 37 | none: 26 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$10.6M | 126.76 | 135 | 130 | -$852k | +$258k bull / +$0 bear | out (clean 29, ADX 15, RVol 0.6) |
| 2 | **SMH** | 566.08 | FLOW SURGE | **PUTS** | 34 | none: 184 puts 0-7DTE > 13 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (81 contracts' greeks worked out here) | POS +$75.7M | 559.81 | 570 | 555 | -$4.7M | +$0 bull / -$450k bear | out (clean 28, ADX 27, RVol 0.5) |
| 3 | **AAPL** | 345.68 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 32 | none: 84 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (45 contracts' greeks worked out here) | POS +$376.3M | 341.45 | 350 | 345 | +$202k | +$293k bull / -$63k bear | out (clean 28, ADX 18, RVol 0.6) |
| 4 | **HOOD** | 90.59 | - | **-** | 25 | - | NEG -$17.3M | - | 95 | 90 | +$3.9M | +$38k bull / +$0 bear | out (clean 30, ADX 25, RVol 1.0) |
| 5 | **IWM** | 280.23 | - | **-** | 22 | - | NEG -$295.2M | 281.26 | 280 | 270 | +$9.7M | +$0 bull / -$282k bear | out (clean 24, ADX 21, RVol 0.6) |
| 6 | **GOOGL** | 325.04 | - | **-** | 20 | - | POS +$16.7M | 321.3 | 355 | 330 | -$3.1M | +$0 bull / -$1.6M bear | out (clean 33, ADX 18, RVol 1.5) |
| 7 | **AMD** | 570.25 | - | **-** | 18 | - | POS +$187.4M | - | 600 | 550 | -$56k | +$53k bull / -$964k bear | out (clean 29, ADX 36, RVol 0.8) |
| 8 | **META** | 611.29 | - | **-** | 18 | - | NEG -$253.9M | 633.72 | 650 | 610 | +$8.2M | +$298k bull / -$65k bear | out (clean 29, ADX 16, RVol 0.9) |
| 9 | **AVGO** | 348.37 | - | **-** | 17 | - | POS +$59.6M | 336.65 | 350 | 340 | -$842k | +$0 bull / -$66k bear | out (clean 29, ADX 28, RVol 0.5) |
| 10 | **MU** | 969.09 | - | **-** | 17 | - | POS +$639.2M | - | 950 | 950 | +$21.4M | +$467k bull / -$5.7M bear | out (clean 28, ADX 23, RVol 0.6) |
| 11 | **SPY** | 771.24 | - | **-** | 16 | - | NEG -$2.1B | 773.4 | 780 | 750 | -$24.3M | +$484k bull / -$572k bear | out (clean 29, ADX 16, RVol 0.7) |
| 12 | **NVDA** | 217.26 | - | **-** | 16 | - | POS +$541.4M | 210.14 | 220 | 215 | +$7.4M | +$160k bull / -$100k bear | out (clean 26, ADX 15, RVol 0.4) |
| 13 | **MSFT** | 527.38 | - | **-** | 16 | - | POS +$459.1M | - | 550 | 500 | +$1.7M | +$155k bull / -$985k bear | out (clean 29, ADX 14, RVol 0.6) |
| 14 | **TSLA** | 401.44 | - | **-** | 15 | - | POS +$599.7M | - | 400 | 395 | -$16.8M | +$465k bull / -$368k bear | out (clean 29, ADX 13, RVol 0.3) |
| 15 | **AMZN** | 253.03 | - | **-** | 15 | - | POS +$187.9M | 245.54 | 255 | 250 | -$683k | +$428k bull / -$582k bear | out (clean 32, ADX 18, RVol 0.6) |
| 16 | **MSTR** | 139.33 | - | **-** | 15 | - | POS +$16.2M | - | 152.5 | 140 | +$275k | +$0 bull / -$210k bear | out (clean 27, ADX 10, RVol 0.6) |
| 17 | **QQQ** | 722.53 | - | **-** | 13 | - | NEG -$1.5B | 727.67 | 720 | 720 | +$3.3M | +$353k bull / +$0 bear | out (clean 29, ADX 14, RVol 0.3) |
| 18 | **SHOP** | 168.19 | - | **-** | 12 | - | NEG -$3.4M | 171.81 | 175 | 165 | -$27k | - | out (clean 29, ADX 28, RVol 0.7) |
| 19 | **BABA** | 100.17 | - | **-** | 10 | - | NEG -$14.4M | 103.16 | 102 | 100 | +$46k | - | out (clean 28, ADX 19, RVol 0.9) |
| 20 | **PLTR** | 194.06 | - | **-** | 9 | - | POS +$39.7M | 189.29 | 200 | 190 | +$203k | - | out (clean 27, ADX 44, RVol 0.4) |
| 21 | **SMCI** | 34.85 | - | **-** | 8 | - | POS +$18.8M | - | 35 | 35 | +$113k | - | out (clean 28, ADX 20, RVol 0.4) |
| 22 | **UBER** | 65.57 | - | **-** | 8 | - | NEG -$25.4M | 68.36 | 70 | 65 | +$1k | - | out (clean 30, ADX 38, RVol 0.8) |
| 23 | **ARM** | 232.78 | - | **-** | 7 | - | POS +$1.7M | 223.17 | 227.5 | 240 | +$67k | - | out (clean 26, ADX 23, RVol 0.7) |
| 24 | **NFLX** | 61.75 | - | **-** | 6 | - | NEG -$54.2M | - | 65 | 60 | -$79k | - | out (clean 32, ADX 20, RVol 0.7) |
| 25 | **COIN** | 158.03 | - | **-** | 5 | - | POS +$1.2M | 155.49 | 170 | 150 | +$44k | - | out (clean 29, ADX 8, RVol 0.5) |
| 26 | **DELL** | 493.47 | - | **-** | 4 | - | POS +$28.1M | - | 500 | 500 | +$112k | - | out (clean 31, ADX 14, RVol 0.3) |
| 27 | **CRM** | 241.24 | - | **-** | 3 | - | POS +$6.2M | 234.66 | 260 | 240 | +$4k | - | out (clean 27, ADX 14, RVol 0.3) |

## Big prints this scan (123)
- **SPY** PUT 767 2026-11-04 (7DTE): 1,242 @ 3.90 = **+$484k** SELL | vol 14,688 / OI 94
- **QQQ** CALL 722 2026-10-28 (0DTE): 1,000 @ 3.53 = **+$353k** BUY | vol 91,725 / OI 1,416
- **GOOGL** PUT 315 2026-10-30 (2DTE): 435 @ 5.85 = **+$254k** BUY | vol 2,740 / OI 3,493
- **MSTR** PUT 140 2026-10-30 (2DTE): 351 @ 5.25 = **+$184k** BUY | vol 1,645 / OI 3,122
- **META** CALL 610 2026-10-28 (0DTE): 300 @ 6.10 = **+$183k** BUY | vol 2,399 / OI 126
- **AMZN** CALL 260 2026-10-30 (2DTE): 255 @ 6.90 = **+$176k** SELL | vol 1,482 / OI 8,793
- **TSLA** CALL 385 2026-10-28 (0DTE): 83 @ 17.00 = **+$141k** BUY | vol 517 / OI 1,452
- **MSFT** CALL 545 2026-11-02 (5DTE): 200 @ 6.65 = **+$133k** SELL | vol 1,049 / OI 140
- **AMD** PUT 570 2026-10-30 (2DTE): 100 @ 13.20 = **+$132k** BUY | vol 1,468 / OI 700
- **AMD** CALL 567.5 2026-10-28 (0DTE): 201 @ 5.30 = **+$107k** SELL | vol 6,755 / OI 357
- **SPY** PUT 771 2026-10-28 (0DTE): 500 @ 2.02 = **+$101k** BUY | vol 143,595 / OI 1,490
- **AMZN** PUT 255 2026-10-30 (2DTE): 84 @ 11.15 = **+$94k** SELL | vol 3,026 / OI 3,209
- **MU** PUT 970 2026-10-28 (0DTE): 151 @ 6.15 = **+$93k** SELL | vol 23,285 / OI 23
- **MU** CALL 970 2026-10-30 (2DTE): 48 @ 18.95 = **+$91k** SELL | vol 6,058 / OI 1,990
- **MU** PUT 925 2026-10-30 (2DTE): 150 @ 6.00 = **+$90k** BUY | vol 1,203 / OI 597

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 770 2026-11-03 (6DTE): 525 traded vs OI 480
- **SPY** CALL 771 2026-11-03 (6DTE): 554 traded vs OI 340
- **SPY** CALL 771 2026-11-06 (9DTE): 894 traded vs OI 868
- **QQQ** PUT 675 2026-10-29 (1DTE): 969 traded vs OI 773
- **QQQ** CALL 736 2026-10-30 (2DTE): 1,025 traded vs OI 1,017
- **QQQ** CALL 755 2026-11-11 (14DTE): 509 traded vs OI 0
- **IWM** CALL 285 2026-11-04 (7DTE): 508 traded vs OI 14
- **IWM** CALL 284 2026-11-06 (9DTE): 500 traded vs OI 446
- **SMH** CALL 577.5 2026-10-28 (0DTE): 638 traded vs OI 111
- **SMH** CALL 570 2026-10-28 (0DTE): 860 traded vs OI 842
- **SMH** CALL 580 2026-11-04 (7DTE): 769 traded vs OI 761
- **NVDA** PUT 227.5 2026-10-30 (2DTE): 846 traded vs OI 774
- **NVDA** CALL 200 2026-11-04 (7DTE): 688 traded vs OI 43
- **NVDA** CALL 205 2026-11-04 (7DTE): 591 traded vs OI 7
- **TSLA** PUT 385 2026-11-04 (7DTE): 502 traded vs OI 495

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
