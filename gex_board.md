# GEX + FLOW SCAN - Wed Oct 28, 01:30 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (6)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 12:56 | **QQQ** | **CALLS** | 1m WHIPSAW (R1 R2) | 10/28 730C | 0.63 | 0.53 | +24% (10m) | **-16%** | -35% | 723.9 |
| 12:56 | **SPY** | **CALLS** | 1m WHIPSAW (R1 R2) | 10/29 779C | 0.63 | 0.49 | +3% (9m) | **-22%** | +10% | 772.67 |
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
| 1 | **AAPL** | 345.49 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 32 | none: 84 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (48 contracts' greeks worked out here) | POS +$371.3M | 341.63 | 350 | 345 | +$878k | +$72k bull / +$0 bear | out (clean 28, ADX 17, RVol 0.5) |
| 2 | **ORCL** | 130.16 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 25 | none: 26 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$10.5M | 126.75 | 135 | 130 | -$734k | - | out (clean 29, ADX 13, RVol 0.4) |
| 3 | **SMH** | 564.22 | - | **-** | 24 | - | POS +$55.7M | 559.06 | 570 | 555 | -$3.8M | +$127k bull / +$0 bear | out (clean 28, ADX 24, RVol 0.5) |
| 4 | **BABA** | 100.12 | - | **-** | 22 | - | NEG -$14.3M | 103.14 | 102 | 100 | +$80k | +$29k bull / +$0 bear | out (clean 28, ADX 16, RVol 1.3) |
| 5 | **GOOGL** | 324.58 | - | **-** | 20 | - | POS +$15.8M | 321.15 | 355 | 330 | -$1.9M | +$794k bull / -$589k bear | out (clean 32, ADX 25, RVol 1.9) |
| 6 | **AMD** | 568.10 | - | **-** | 19 | - | POS +$186.4M | - | 600 | 550 | +$3.7M | +$446k bull / +$0 bear | out (clean 29, ADX 35, RVol 0.5) |
| 7 | **NVDA** | 216.77 | - | **-** | 18 | - | POS +$500.1M | 210.1 | 220 | 215 | +$10.0M | +$165k bull / +$0 bear | out (clean 26, ADX 16, RVol 0.6) |
| 8 | **META** | 612.78 | - | **-** | 18 | - | NEG -$267.5M | 635.38 | 650 | 610 | +$7.3M | +$44k bull / -$332k bear | out (clean 28, ADX 16, RVol 0.8) |
| 9 | **MU** | 965.22 | - | **-** | 18 | - | POS +$626.0M | - | 950 | 950 | +$26.7M | +$4.7M bull / +$0 bear | out (clean 28, ADX 26, RVol 0.5) |
| 10 | **MSFT** | 527.00 | - | **-** | 17 | - | POS +$426.7M | - | 550 | 500 | +$2.3M | +$35k bull / -$57k bear | out (clean 29, ADX 16, RVol 0.9) |
| 11 | **TSLA** | 401.64 | - | **-** | 15 | - | POS +$606.0M | - | 400 | 395 | -$16.4M | +$182k bull / -$1.3M bear | out (clean 29, ADX 12, RVol 0.1) |
| 12 | **SPY** | 770.90 | - | **-** | 14 | - | NEG -$2.6B | 773.39 | 780 | 750 | -$7.4M | +$2.6M bull / +$0 bear | out (clean 28, ADX 15, RVol 0.4) |
| 13 | **QQQ** | 721.57 | - | **-** | 14 | - | NEG -$1.9B | 727.91 | 720 | 720 | +$15.2M | +$1.4M bull / +$0 bear | out (clean 29, ADX 12, RVol 0.2) |
| 14 | **AMZN** | 252.69 | - | **-** | 14 | - | POS +$195.4M | 237.96 | 255 | 250 | +$308k | +$204k bull / +$0 bear | out (clean 32, ADX 19, RVol 0.5) |
| 15 | **HOOD** | 90.57 | - | **-** | 14 | - | NEG -$17.4M | - | 95 | 90 | +$3.9M | - | out (clean 30, ADX 22, RVol 1.3) |
| 16 | **IWM** | 280.40 | - | **-** | 11 | - | NEG -$259.1M | 281.27 | 280 | 270 | +$9.4M | - | out (clean 24, ADX 25, RVol 0.3) |
| 17 | **SHOP** | 168.31 | - | **-** | 11 | - | NEG -$3.6M | 172.02 | 175 | 165 | -$29k | - | out (clean 29, ADX 28, RVol 0.3) |
| 18 | **PLTR** | 194.10 | - | **-** | 9 | - | POS +$41.1M | 189.32 | 200 | 190 | +$152k | - | out (clean 27, ADX 45, RVol 0.3) |
| 19 | **AVGO** | 347.99 | - | **-** | 8 | - | POS +$60.8M | 336.25 | 350 | 340 | -$709k | - | out (clean 29, ADX 32, RVol 0.5) |
| 20 | **SMCI** | 34.76 | - | **-** | 8 | - | POS +$19.2M | - | 35 | 35 | +$123k | - | out (clean 28, ADX 17, RVol 0.3) |
| 21 | **UBER** | 65.39 | - | **-** | 7 | - | NEG -$30.8M | 68.79 | 70 | 65 | +$14k | - | out (clean 30, ADX 32, RVol 0.5) |
| 22 | **NFLX** | 61.73 | - | **-** | 6 | - | NEG -$56.7M | - | 65 | 60 | -$123k | - | out (clean 31, ADX 16, RVol 0.5) |
| 23 | **ARM** | 231.97 | - | **-** | 6 | - | POS +$1.8M | 222.7 | 227.5 | 250 | +$88k | - | out (clean 26, ADX 19, RVol 0.5) |
| 24 | **CRM** | 240.99 | - | **-** | 5 | - | POS +$6.2M | 234.46 | 260 | 240 | +$36k | - | out (clean 27, ADX 12, RVol 0.4) |
| 25 | **COIN** | 158.17 | - | **-** | 4 | - | POS +$1.5M | 155.02 | 170 | 150 | +$43k | - | out (clean 29, ADX 7, RVol 0.3) |
| 26 | **MSTR** | 139.11 | - | **-** | 4 | - | POS +$16.1M | - | 152.5 | 140 | +$358k | - | out (clean 27, ADX 8, RVol 0.2) |
| 27 | **DELL** | 494.40 | - | **-** | 3 | - | POS +$29.0M | - | 500 | 500 | +$55k | - | out (clean 31, ADX 13, RVol 0.3) |

## Big prints this scan (75)
- **SPY** PUT 758 2026-11-04 (7DTE): 2,628 @ 2.11 = **+$555k** SELL | vol 3,609 / OI 79
- **SPY** PUT 760 2026-11-02 (5DTE): 2,628 @ 1.44 = **+$378k** SELL | vol 4,049 / OI 1,885
- **MU** CALL 950 2026-10-30 (2DTE): 100 @ 31.38 = **+$314k** BUY | vol 10,991 / OI 12,546
- **MU** CALL 955 2026-10-30 (2DTE): 100 @ 28.22 = **+$282k** BUY | vol 556 / OI 738
- **MSFT** CALL 515 2026-10-30 (2DTE): 100 @ 20.20 = **+$202k** MID | vol 369 / OI 981
- **SPY** PUT 771 2026-10-29 (1DTE): 560 @ 3.08 = **+$172k** SELL | vol 36,772 / OI 583
- **MU** CALL 980 2026-10-30 (2DTE): 100 @ 15.27 = **+$153k** BUY | vol 4,971 / OI 1,631
- **MU** CALL 955 2026-10-28 (0DTE): 100 @ 15.00 = **+$150k** BUY | vol 2,586 / OI 340
- **MU** PUT 965 2026-10-28 (0DTE): 310 @ 4.70 = **+$146k** SELL | vol 24,952 / OI 17
- **SPY** PUT 771 2026-10-29 (1DTE): 448 @ 3.08 = **+$138k** SELL | vol 36,772 / OI 583
- **MU** CALL 975 2026-10-28 (0DTE): 400 @ 3.40 = **+$136k** BUY | vol 44,183 / OI 683
- **MU** CALL 985 2026-10-30 (2DTE): 100 @ 13.26 = **+$133k** BUY | vol 1,752 / OI 957
- **SPY** CALL 771 2026-10-28 (0DTE): 550 @ 2.23 = **+$123k** BUY | vol 210,165 / OI 4,302
- **MU** PUT 965 2026-10-28 (0DTE): 226 @ 4.70 = **+$106k** SELL | vol 24,952 / OI 17
- **SPY** PUT 772 2026-10-29 (1DTE): 300 @ 3.52 = **+$106k** SELL | vol 17,069 / OI 264

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 760 2026-11-02 (5DTE): 4,049 traded vs OI 1,885
- **SPY** PUT 758 2026-11-04 (7DTE): 3,609 traded vs OI 79
- **TSLA** CALL 402.5 2026-11-04 (7DTE): 504 traded vs OI 180
- **TSLA** CALL 440 2026-11-20 (23DTE): 552 traded vs OI 0
- **AMD** CALL 600 2026-10-30 (2DTE): 3,551 traded vs OI 3,532
- **META** PUT 592.5 2026-10-30 (2DTE): 509 traded vs OI 389
- **AMZN** PUT 250 2026-11-02 (5DTE): 621 traded vs OI 305
- **AMZN** PUT 255 2026-10-30 (2DTE): 3,443 traded vs OI 3,209
- **HOOD** PUT 82 2026-11-06 (9DTE): 527 traded vs OI 247

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
