# GEX + FLOW SCAN - Wed Oct 28, 12:30 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (4)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:40 | **HOOD** | **CALLS** | FLOW SURGE | 10/30 96C | 0.77 | 0.61 | -1% (3m) | **-21%** | +49% | 93.02 |
| 11:05 | **HOOD** | **CALLS** | FLOW SURGE | 10/30 97C | 0.63 | 0.45 | +19% (1m) | **-29%** (done) | +53% | 93.44 |
| 10:50 | **IWM** | **CALLS** | FLOW SURGE | 10/30 284C | 0.57 | 0.54 | +7% (2m) | **-5%** (done) | +22% | 280.64 |
| 10:20 | **IWM** | **CALLS** | FLOW SURGE | 10/29 284C | 0.47 | 0.34 | +11% (0m) | **-28%** (done) | +27% | 281.41 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **AAPL** | 345.51 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 32 | none: 84 calls 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (51 contracts' greeks worked out here) | POS +$368.5M | 341.56 | 350 | 345 | +$8k | +$109k bull / +$0 bear | out (clean 28, ADX 14, RVol 0.6) |
| 2 | **HOOD** | 90.88 | - | **-** | 26 | - | NEG -$16.9M | - | 95 | 90 | +$3.9M | +$42k bull / -$118k bear | out (clean 30, ADX 31, RVol 0.6) |
| 3 | **IWM** | 280.14 | - | **-** | 22 | - | NEG -$334.6M | 281.26 | 280 | 270 | +$9.4M | +$219k bull / +$0 bear | out (clean 24, ADX 17, RVol 0.8) |
| 4 | **ORCL** | 130.88 | - | **-** | 22 | - | POS +$12.5M | 126.49 | 135 | 130 | -$1.0M | +$40k bull / -$344k bear | out (clean 29, ADX 18, RVol 0.5) |
| 5 | **NVDA** | 217.07 | - | **-** | 19 | - | POS +$523.5M | 210.09 | 220 | 215 | +$10.2M | +$393k bull / -$368k bear | out (clean 27, ADX 18, RVol 0.6) |
| 6 | **META** | 613.63 | - | **-** | 19 | - | NEG -$265.7M | 635.65 | 650 | 610 | +$8.5M | +$996k bull / +$0 bear | out (clean 29, ADX 19, RVol 0.8) |
| 7 | **MSFT** | 528.19 | - | **-** | 19 | - | POS +$461.4M | - | 550 | 500 | +$1.6M | +$269k bull / -$656k bear | out (clean 29, ADX 20, RVol 1.3) |
| 8 | **SMH** | 565.11 | - | **-** | 18 | - | POS +$62.9M | 559.34 | 570 | 555 | -$4.2M | - | out (clean 28, ADX 21, RVol 0.5) |
| 9 | **AMD** | 567.10 | - | **-** | 18 | - | POS +$176.8M | - | 600 | 550 | +$2.3M | +$319k bull / -$355k bear | out (clean 29, ADX 26, RVol 0.9) |
| 10 | **MU** | 972.04 | - | **-** | 18 | - | POS +$626.1M | - | 950 | 950 | +$16.3M | +$830k bull / -$1.9M bear | out (clean 28, ADX 29, RVol 0.3) |
| 11 | **TSLA** | 401.11 | - | **-** | 16 | - | POS +$602.4M | - | 400 | 395 | -$15.8M | +$421k bull / +$0 bear | out (clean 29, ADX 14, RVol 0.3) |
| 12 | **GOOGL** | 323.45 | - | **-** | 16 | - | POS +$7.9M | 321.62 | 355 | 300 | -$1.7M | +$0 bull / -$40k bear | out (clean 33, ADX 13, RVol 0.5) |
| 13 | **AMZN** | 252.79 | - | **-** | 14 | - | POS +$175.5M | 243.11 | 255 | 250 | -$502k | +$0 bull / -$921k bear | out (clean 32, ADX 16, RVol 0.5) |
| 14 | **AVGO** | 347.19 | - | **-** | 14 | - | POS +$54.2M | 337.53 | 350 | 340 | -$31k | +$0 bull / -$117k bear | out (clean 29, ADX 17, RVol 0.5) |
| 15 | **SPY** | 771.25 | - | **-** | 13 | - | NEG -$2.4B | 773.65 | 780 | 750 | -$5.7M | +$882k bull / +$0 bear | out (clean 29, ADX 11, RVol 0.3) |
| 16 | **QQQ** | 722.18 | - | **-** | 12 | - | NEG -$1.7B | 727.81 | 720 | 720 | +$4.0M | +$304k bull / -$440k bear | out (clean 29, ADX 7, RVol 0.4) |
| 17 | **UBER** | 65.70 | - | **-** | 10 | - | NEG -$26.3M | 69.26 | 70 | 65 | -$59k | - | out (clean 30, ADX 32, RVol 0.5) |
| 18 | **PLTR** | 194.18 | - | **-** | 9 | - | POS +$41.3M | 189.22 | 200 | 190 | -$244k | - | out (clean 27, ADX 43, RVol 0.4) |
| 19 | **SMCI** | 34.83 | - | **-** | 9 | - | POS +$18.9M | - | 35 | 35 | +$112k | - | out (clean 28, ADX 21, RVol 0.4) |
| 20 | **SHOP** | 167.78 | - | **-** | 9 | - | NEG -$3.7M | 171.79 | 175 | 165 | -$14k | - | out (clean 28, ADX 23, RVol 0.8) |
| 21 | **NFLX** | 61.90 | - | **-** | 7 | - | NEG -$57.5M | - | 65 | 60 | +$27k | - | out (clean 32, ADX 27, RVol 0.7) |
| 22 | **ARM** | 232.36 | - | **-** | 6 | - | POS +$1.8M | 223.22 | 220 | 250 | +$99k | - | out (clean 27, ADX 20, RVol 0.2) |
| 23 | **BABA** | 100.37 | - | **-** | 6 | - | NEG -$13.6M | 103.59 | 102 | 100 | +$17k | - | out (clean 27, ADX 16, RVol 0.4) |
| 24 | **COIN** | 158.45 | - | **-** | 5 | - | POS +$1.7M | 155.03 | 170 | 150 | -$30k | - | out (clean 29, ADX 9, RVol 0.4) |
| 25 | **DELL** | 493.41 | - | **-** | 5 | - | POS +$28.8M | - | 500 | 500 | +$149k | - | out (clean 30, ADX 16, RVol 0.4) |
| 26 | **CRM** | 240.80 | - | **-** | 5 | - | POS +$4.8M | 235.4 | 260 | 240 | +$19k | - | out (clean 27, ADX 19, RVol 0.2) |
| 27 | **MSTR** | 139.28 | - | **-** | 3 | - | POS +$16.7M | - | 152.5 | 140 | -$90k | - | out (clean 27, ADX 9, RVol 0.3) |

## Big prints this scan (37)
- **MU** CALL 930 2026-10-28 (0DTE): 60 @ 41.88 = **+$251k** SELL | vol 972 / OI 714
- **QQQ** CALL 713 2026-10-28 (0DTE): 200 @ 9.71 = **+$194k** SELL | vol 1,708 / OI 1,449
- **QQQ** PUT 725 2026-10-29 (1DTE): 200 @ 6.56 = **+$131k** BUY | vol 1,124 / OI 643
- **MU** CALL 970 2026-10-30 (2DTE): 60 @ 21.26 = **+$128k** SELL | vol 5,227 / OI 1,990
- **AMD** CALL 567.5 2026-10-30 (2DTE): 100 @ 12.15 = **+$122k** SELL | vol 890 / OI 726
- **NVDA** PUT 217.5 2026-10-28 (0DTE): 862 @ 1.33 = **+$115k** BUY | vol 84,595 / OI 2,087
- **SPY** PUT 775 2026-10-30 (2DTE): 194 @ 5.62 = **+$109k** SELL | vol 2,084 / OI 3,175
- **MU** CALL 975 2026-10-28 (0DTE): 200 @ 4.50 = **+$90k** SELL | vol 34,209 / OI 683
- **NVDA** CALL 215 2026-10-28 (0DTE): 336 @ 2.28 = **+$77k** SELL | vol 9,820 / OI 4,474
- **MU** PUT 1,000 2026-10-30 (2DTE): 18 @ 36.71 = **+$66k** BUY | vol 1,366 / OI 1,100
- **MU** PUT 1,000 2026-10-30 (2DTE): 12 @ 36.90 = **+$44k** BUY | vol 1,366 / OI 1,100
- **MU** PUT 1,000 2026-10-30 (2DTE): 12 @ 36.87 = **+$44k** BUY | vol 1,366 / OI 1,100
- **NVDA** PUT 225 2026-10-30 (2DTE): 50 @ 8.40 = **+$42k** BUY | vol 1,280 / OI 8,407
- **ORCL** CALL 132 2026-10-30 (2DTE): 104 @ 3.90 = **+$41k** MID | vol 1,495 / OI 1,444
- **AAPL** CALL 340 2026-10-30 (2DTE): 60 @ 6.75 = **+$40k** BUY | vol 1,283 / OI 3,956

## New unusual volume (traded more than open interest, 500+)
- **NVDA** PUT 232.5 2026-11-02 (5DTE): 657 traded vs OI 52
- **NVDA** CALL 227.5 2026-11-02 (5DTE): 530 traded vs OI 519
- **NVDA** PUT 215 2026-10-30 (2DTE): 11,106 traded vs OI 10,934
- **NVDA** PUT 237.5 2026-11-02 (5DTE): 632 traded vs OI 38
- **META** PUT 587.5 2026-10-30 (2DTE): 503 traded vs OI 283
- **MSFT** PUT 500 2026-11-02 (5DTE): 503 traded vs OI 406
- **MU** CALL 975 2026-10-30 (2DTE): 5,369 traded vs OI 5,300
- **HOOD** PUT 85 2026-10-30 (2DTE): 3,653 traded vs OI 3,570
- **HOOD** CALL 87 2026-11-06 (9DTE): 507 traded vs OI 119

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
