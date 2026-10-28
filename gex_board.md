# GEX + FLOW SCAN - Wed Oct 28, 12:20 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (4)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:40 | **HOOD** | **CALLS** | FLOW SURGE | 10/30 96C | 0.77 | 0.59 | -1% (3m) | **-23%** | +49% | 93.02 |
| 11:05 | **HOOD** | **CALLS** | FLOW SURGE | 10/30 97C | 0.63 | 0.45 | +19% (1m) | **-29%** (done) | +53% | 93.44 |
| 10:50 | **IWM** | **CALLS** | FLOW SURGE | 10/30 284C | 0.57 | 0.54 | +7% (2m) | **-5%** (done) | +22% | 280.64 |
| 10:20 | **IWM** | **CALLS** | FLOW SURGE | 10/29 284C | 0.47 | 0.34 | +11% (0m) | **-28%** (done) | +27% | 281.41 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **SMH** | 565.14 | FLOW SURGE | **PUTS** | 34 | none: 180 puts 0-7DTE > 12 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (83 contracts' greeks worked out here) | POS +$56.9M | 559.65 | 570 | 555 | -$4.2M | +$0 bull / -$672k bear | out (clean 28, ADX 22, RVol 0.4) |
| 2 | **TSLA** | 400.98 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 32 | 10/28 397.5P @ 0.62 (delta 0.22) = est -20% at 400 | POS +$595.3M | - | 400 | 395 | -$17.5M | +$561k bull / -$507k bear | out (clean 29, ADX 13, RVol 0.3) |
| 3 | **HOOD** | 90.84 | - | **-** | 26 | - | NEG -$16.9M | - | 95 | 90 | +$3.9M | +$257k bull / -$118k bear | out (clean 30, ADX 30, RVol 0.6) |
| 4 | **IWM** | 280.09 | - | **-** | 22 | - | NEG -$351.3M | 281.26 | 280 | 270 | +$9.4M | +$219k bull / +$0 bear | out (clean 24, ADX 18, RVol 0.9) |
| 5 | **AAPL** | 345.31 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 22 | none: 81 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (47 contracts' greeks worked out here) | POS +$359.5M | 341.38 | 350 | 345 | -$91k | - | out (clean 29, ADX 15, RVol 0.6) |
| 6 | **META** | 612.86 | - | **-** | 20 | - | NEG -$236.6M | 630.86 | 650 | 610 | +$9.5M | +$794k bull / -$97k bear | out (clean 29, ADX 20, RVol 0.6) |
| 7 | **ORCL** | 130.97 | - | **-** | 20 | - | POS +$11.3M | 126.71 | 135 | 130 | -$721k | +$40k bull / -$277k bear | out (clean 28, ADX 16, RVol 0.5) |
| 8 | **NVDA** | 216.91 | - | **-** | 19 | - | POS +$498.2M | 210.11 | 220 | 215 | +$9.7M | +$693k bull / +$0 bear | out (clean 26, ADX 16, RVol 0.6) |
| 9 | **MSFT** | 528.28 | - | **-** | 19 | - | POS +$461.1M | - | 550 | 500 | +$1.8M | +$269k bull / -$631k bear | out (clean 30, ADX 22, RVol 1.2) |
| 10 | **AMD** | 567.39 | - | **-** | 18 | - | POS +$172.6M | - | 600 | 550 | +$2.8M | +$355k bull / -$347k bear | out (clean 29, ADX 26, RVol 0.8) |
| 11 | **MU** | 972.95 | - | **-** | 18 | - | POS +$614.8M | - | 950 | 950 | +$15.9M | +$379k bull / -$3.1M bear | out (clean 28, ADX 31, RVol 0.3) |
| 12 | **GOOGL** | 323.67 | - | **-** | 16 | - | POS +$13.4M | 321.03 | 355 | 330 | -$1.8M | +$0 bull / -$105k bear | out (clean 33, ADX 15, RVol 0.4) |
| 13 | **AVGO** | 346.59 | - | **-** | 15 | - | POS +$56.4M | 336.46 | 350 | 340 | +$516k | +$0 bull / -$89k bear | out (clean 28, ADX 16, RVol 0.4) |
| 14 | **AMZN** | 252.57 | - | **-** | 14 | - | POS +$177.1M | 240.77 | 255 | 250 | -$406k | +$0 bull / -$964k bear | out (clean 32, ADX 18, RVol 0.4) |
| 15 | **SPY** | 771.13 | - | **-** | 13 | - | NEG -$2.5B | 773.5 | 780 | 750 | -$6.0M | +$656k bull / -$126k bear | out (clean 29, ADX 12, RVol 0.4) |
| 16 | **QQQ** | 722.05 | - | **-** | 12 | - | NEG -$1.7B | 727.74 | 720 | 720 | +$2.9M | +$278k bull / -$273k bear | out (clean 29, ADX 7, RVol 0.4) |
| 17 | **PLTR** | 194.47 | - | **-** | 10 | - | POS +$43.0M | 189.21 | 200 | 190 | -$316k | - | out (clean 27, ADX 44, RVol 0.5) |
| 18 | **SMCI** | 34.80 | - | **-** | 9 | - | POS +$18.9M | - | 35 | 35 | +$110k | - | out (clean 28, ADX 20, RVol 0.4) |
| 19 | **ARM** | 232.06 | - | **-** | 9 | - | POS +$1.8M | 223.1 | 220 | 250 | +$228k | - | out (clean 27, ADX 23, RVol 0.3) |
| 20 | **UBER** | 65.53 | - | **-** | 9 | - | NEG -$29.4M | - | 70 | 65 | -$36k | - | out (clean 29, ADX 31, RVol 0.5) |
| 21 | **SHOP** | 166.47 | - | **-** | 9 | - | NEG -$4.3M | 171.04 | 175 | 165 | +$9k | - | out (clean 28, ADX 22, RVol 1.1) |
| 22 | **NFLX** | 61.77 | - | **-** | 7 | - | NEG -$56.0M | - | 65 | 60 | -$8k | - | out (clean 32, ADX 30, RVol 0.7) |
| 23 | **CRM** | 240.98 | - | **-** | 6 | - | POS +$5.4M | 234.91 | 260 | 240 | +$22k | - | out (clean 27, ADX 19, RVol 0.3) |
| 24 | **BABA** | 100.41 | - | **-** | 6 | - | NEG -$13.6M | 103.57 | 102 | 100 | +$22k | - | out (clean 27, ADX 15, RVol 0.4) |
| 25 | **COIN** | 158.59 | - | **-** | 5 | - | POS +$989k | 155.91 | 170 | 150 | -$31k | - | out (clean 29, ADX 9, RVol 0.4) |
| 26 | **DELL** | 493.73 | - | **-** | 5 | - | POS +$28.9M | - | 500 | 500 | +$135k | - | out (clean 30, ADX 16, RVol 0.5) |
| 27 | **MSTR** | 139.41 | - | **-** | 3 | - | POS +$16.1M | - | 152.5 | 140 | -$106k | - | out (clean 27, ADX 7, RVol 0.4) |

## Big prints this scan (79)
- **SPY** CALL 771 2026-10-28 (0DTE): 983 @ 2.29 = **+$225k** BUY | vol 170,121 / OI 4,302
- **SPY** PUT 773 2026-10-28 (0DTE): 544 @ 3.02 = **+$164k** SELL | vol 30,486 / OI 703
- **SPY** PUT 773 2026-10-28 (0DTE): 456 @ 3.02 = **+$138k** SELL | vol 30,486 / OI 703
- **SPY** PUT 770 2026-10-29 (1DTE): 500 @ 2.58 = **+$129k** SELL | vol 26,928 / OI 727
- **MSFT** PUT 550 2026-10-30 (2DTE): 25 @ 27.27 = **+$68k** MID | vol 31 / OI 213
- **MU** PUT 1,000 2026-10-30 (2DTE): 16 @ 37.46 = **+$60k** BUY | vol 1,113 / OI 1,100
- **META** PUT 620 2026-10-30 (2DTE): 49 @ 11.64 = **+$57k** SELL | vol 1,505 / OI 1,226
- **MU** PUT 970 2026-10-28 (0DTE): 100 @ 5.60 = **+$56k** BUY | vol 19,224 / OI 23
- **MU** PUT 1,000 2026-10-30 (2DTE): 14 @ 37.40 = **+$52k** BUY | vol 1,113 / OI 1,100
- **MU** CALL 950 2026-10-30 (2DTE): 15 @ 33.70 = **+$51k** BUY | vol 10,368 / OI 12,546
- **AMD** CALL 547.5 2026-11-02 (5DTE): 17 @ 27.25 = **+$46k** BUY | vol 77 / OI 117
- **HOOD** CALL 90 2026-10-30 (2DTE): 150 @ 2.78 = **+$42k** BUY | vol 5,802 / OI 495
- **TSLA** CALL 405 2026-10-30 (2DTE): 100 @ 4.10 = **+$41k** BUY | vol 11,620 / OI 3,950
- **META** PUT 620 2026-10-30 (2DTE): 35 @ 11.66 = **+$41k** SELL | vol 1,505 / OI 1,226
- **META** CALL 612.5 2026-10-28 (0DTE): 90 @ 4.50 = **+$40k** BUY | vol 4,580 / OI 20

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 769 2026-11-03 (6DTE): 590 traded vs OI 157
- **QQQ** PUT 675 2026-11-03 (6DTE): 509 traded vs OI 318
- **QQQ** PUT 708 2026-10-29 (1DTE): 1,576 traded vs OI 1,567
- **IWM** PUT 268 2026-10-28 (0DTE): 1,020 traded vs OI 410
- **IWM** CALL 289 2026-10-28 (0DTE): 1,113 traded vs OI 71
- **NVDA** PUT 205 2026-11-02 (5DTE): 511 traded vs OI 475
- **NVDA** CALL 200 2026-11-02 (5DTE): 742 traded vs OI 128
- **TSLA** PUT 377.5 2026-10-30 (2DTE): 1,322 traded vs OI 1,275
- **TSLA** CALL 407.5 2026-11-04 (7DTE): 500 traded vs OI 34
- **META** PUT 620 2026-10-30 (2DTE): 1,505 traded vs OI 1,226
- **META** CALL 652.5 2026-10-30 (2DTE): 658 traded vs OI 657
- **AMZN** PUT 262.5 2026-11-02 (5DTE): 1,023 traded vs OI 10
- **NFLX** PUT 62 2026-11-06 (9DTE): 1,117 traded vs OI 1,106
- **PLTR** PUT 197.5 2026-10-30 (2DTE): 1,671 traded vs OI 1,505
- **HOOD** PUT 87 2026-11-06 (9DTE): 501 traded vs OI 393

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
