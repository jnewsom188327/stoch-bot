# GEX + FLOW SCAN - Wed Oct 28, 11:40 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (4)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:40 | **HOOD** | **CALLS** | FLOW SURGE | 10/30 96C | 0.77 | 0.74 | -4% (0m) | **-4%** | +49% | 93.02 |
| 11:05 | **HOOD** | **CALLS** | FLOW SURGE | 10/30 97C | 0.63 | 0.57 | +19% (1m) | **-10%** | +53% | 93.44 |
| 10:50 | **IWM** | **CALLS** | FLOW SURGE | 10/30 284C | 0.57 | 0.60 | +7% (2m) | **+5%** | +22% | 280.64 |
| 10:20 | **IWM** | **CALLS** | FLOW SURGE | 10/29 284C | 0.47 | 0.34 | +11% (0m) | **-28%** (done) | +27% | 281.41 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **HOOD** | 91.38 | FLOW SURGE | **CALLS** | 47 | 10/30 96C @ 0.77 (delta 0.23) = est +49% at 93.02 | NEG -$16.7M | - | 100 | 90 | +$3.7M | +$449k bull / +$0 bear | out (clean 30, ADX 27, RVol 1.8) |
| 2 | **AAPL** | 345.37 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 32 | none: 81 calls 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (50 contracts' greeks worked out here) | POS +$357.6M | 341.28 | 350 | 345 | +$87k | +$768k bull / -$186k bear | out (clean 29, ADX 20, RVol 0.5) |
| 3 | **IWM** | 280.12 | - | **-** | 24 | - | NEG -$344.7M | 281.33 | 280 | 270 | +$9.9M | +$122k bull / -$239k bear | out (clean 24, ADX 19, RVol 0.7) |
| 4 | **SMH** | 565.13 | - | **-** | 24 | - | POS +$58.1M | 559.76 | 570 | 555 | -$1.6M | +$76k bull / +$0 bear | out (clean 28, ADX 26, RVol 0.7) |
| 5 | **META** | 613.53 | - | **-** | 24 | - | NEG -$266.0M | 635.36 | 650 | 610 | +$10.8M | +$254k bull / -$203k bear | out (clean 29, ADX 30, RVol 0.9) |
| 6 | **PLTR** | 194.60 | - | **-** | 22 | - | POS +$45.3M | 189.01 | 200 | 190 | -$553k | +$35k bull / +$0 bear | out (clean 27, ADX 53, RVol 1.0) |
| 7 | **MSFT** | 528.22 | - | **-** | 21 | - | POS +$455.1M | - | 550 | 500 | +$2.1M | +$115k bull / -$301k bear | out (clean 30, ADX 21, RVol 1.1) |
| 8 | **TSLA** | 401.96 | - | **-** | 20 | - | POS +$596.9M | - | 400 | 395 | -$26.4M | +$89k bull / -$2.1M bear | out (clean 29, ADX 20, RVol 0.4) |
| 9 | **MU** | 972.85 | - | **-** | 20 | - | POS +$588.4M | - | 1,000 | 950 | +$18.8M | +$8.4M bull / -$1.3M bear | out (clean 28, ADX 36, RVol 0.5) |
| 10 | **MSTR** | 139.86 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 20 | none: 26 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$17.0M | - | 152.5 | 140 | -$140k | - | out (clean 28, ADX 8, RVol 0.3) |
| 11 | **AMD** | 566.89 | - | **-** | 19 | - | POS +$178.5M | - | 600 | 550 | +$3.4M | +$829k bull / -$695k bear | out (clean 29, ADX 26, RVol 0.8) |
| 12 | **AMZN** | 252.42 | - | **-** | 19 | - | POS +$181.0M | 240.69 | 255 | 250 | +$2.2M | +$251k bull / -$94k bear | out (clean 32, ADX 25, RVol 0.9) |
| 13 | **AVGO** | 346.65 | - | **-** | 18 | - | POS +$56.4M | 336.27 | 350 | 340 | +$893k | +$0 bull / -$69k bear | out (clean 29, ADX 15, RVol 1.2) |
| 14 | **SHOP** | 165.43 | - | **-** | 16 | - | NEG -$5.9M | 172.15 | 175 | 165 | +$21k | - | out (clean 27, ADX 28, RVol 0.8) |
| 15 | **NVDA** | 217.65 | - | **-** | 15 | - | POS +$565.0M | 209.78 | 220 | 215 | +$3.1M | +$161k bull / +$0 bear | out (clean 26, ADX 8, RVol 0.4) |
| 16 | **ORCL** | 130.48 | - | **-** | 15 | - | POS +$9.7M | 126.61 | 135 | 130 | +$65k | +$0 bull / -$112k bear | out (clean 28, ADX 16, RVol 0.8) |
| 17 | **SPY** | 771.47 | - | **-** | 14 | - | NEG -$2.1B | 773.61 | 780 | 750 | -$11.0M | +$112k bull / -$1.2M bear | out (clean 30, ADX 12, RVol 0.5) |
| 18 | **GOOGL** | 323.78 | - | **-** | 14 | - | POS +$13.7M | 320.96 | 355 | 300 | -$48k | +$29k bull / -$3.0M bear | out (clean 33, ADX 15, RVol 0.7) |
| 19 | **CRM** | 240.92 | - | **-** | 14 | - | POS +$5.4M | 234.71 | 260 | 240 | -$3k | +$0 bull / -$27k bear | out (clean 28, ADX 20, RVol 0.3) |
| 20 | **QQQ** | 722.55 | - | **-** | 13 | - | NEG -$1.6B | 727.67 | 720 | 720 | -$7.4M | +$183k bull / +$0 bear | out (clean 30, ADX 9, RVol 0.4) |
| 21 | **BABA** | 100.02 | - | **-** | 10 | - | NEG -$14.9M | 103.4 | 102 | 100 | +$47k | - | out (clean 28, ADX 15, RVol 0.3) |
| 22 | **NFLX** | 61.74 | - | **-** | 9 | - | NEG -$57.0M | - | 65 | 60 | +$29k | - | out (clean 32, ADX 44, RVol 0.5) |
| 23 | **SMCI** | 34.82 | - | **-** | 9 | - | POS +$19.0M | - | 35 | 35 | +$130k | - | out (clean 28, ADX 18, RVol 0.3) |
| 24 | **ARM** | 232.97 | - | **-** | 9 | - | POS +$2.1M | 222.17 | 227.5 | 250 | +$114k | - | out (clean 26, ADX 28, RVol 0.4) |
| 25 | **UBER** | 65.23 | - | **-** | 9 | - | NEG -$32.7M | - | 70 | 65 | +$34k | - | out (clean 28, ADX 31, RVol 0.5) |
| 26 | **COIN** | 158.63 | - | **-** | 8 | - | POS +$1.6M | 155.12 | 170 | 150 | -$53k | - | out (clean 29, ADX 14, RVol 0.4) |
| 27 | **DELL** | 496.92 | - | **-** | 5 | - | POS +$31.8M | - | 500 | 500 | -$24k | - | out (clean 30, ADX 20, RVol 0.8) |

## Big prints this scan (49)
- **GOOGL** CALL 330 2026-10-30 (2DTE): 800 @ 6.78 = **+$542k** SELL | vol 5,471 / OI 6,833
- **GOOGL** CALL 330 2026-10-30 (2DTE): 721 @ 6.83 = **+$492k** SELL | vol 5,471 / OI 6,833
- **GOOGL** CALL 330 2026-10-30 (2DTE): 706 @ 6.78 = **+$479k** SELL | vol 5,471 / OI 6,833
- **GOOGL** CALL 330 2026-10-30 (2DTE): 705 @ 6.78 = **+$478k** SELL | vol 5,471 / OI 6,833
- **SPY** PUT 767 2026-11-04 (7DTE): 1,000 @ 4.05 = **+$405k** BUY | vol 9,240 / OI 94
- **SPY** PUT 767 2026-11-04 (7DTE): 937 @ 4.16 = **+$390k** BUY | vol 9,240 / OI 94
- **GOOGL** CALL 330 2026-10-30 (2DTE): 552 @ 6.78 = **+$374k** SELL | vol 5,471 / OI 6,833
- **NVDA** CALL 220 2026-11-02 (5DTE): 990 @ 2.41 = **+$239k** MID | vol 2,681 / OI 1,997
- **MU** PUT 970 2026-10-30 (2DTE): 88 @ 18.50 = **+$163k** SELL | vol 5,206 / OI 562
- **SPY** CALL 772 2026-10-29 (1DTE): 500 @ 2.99 = **+$150k** SELL | vol 13,577 / OI 836
- **SPY** CALL 771 2026-10-28 (0DTE): 550 @ 2.43 = **+$134k** SELL | vol 142,245 / OI 4,302
- **TSLA** PUT 400 2026-11-04 (7DTE): 171 @ 7.80 = **+$133k** BUY | vol 971 / OI 26
- **AAPL** CALL 345 2026-10-28 (0DTE): 700 @ 1.32 = **+$92k** BUY | vol 20,280 / OI 1,839
- **GOOGL** CALL 330 2026-10-30 (2DTE): 122 @ 6.78 = **+$83k** SELL | vol 5,471 / OI 6,833
- **GOOGL** CALL 330 2026-10-30 (2DTE): 110 @ 6.78 = **+$75k** SELL | vol 5,471 / OI 6,833

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 786 2026-10-28 (0DTE): 1,288 traded vs OI 1,268
- **SPY** PUT 771 2026-10-30 (2DTE): 3,245 traded vs OI 3,237
- **QQQ** CALL 714 2026-10-28 (0DTE): 659 traded vs OI 642
- **QQQ** PUT 718 2026-10-30 (2DTE): 1,129 traded vs OI 1,125
- **IWM** PUT 277 2026-10-30 (2DTE): 2,707 traded vs OI 2,644
- **NVDA** CALL 205 2026-11-06 (9DTE): 530 traded vs OI 509
- **TSLA** CALL 407.5 2026-11-02 (5DTE): 533 traded vs OI 524
- **TSLA** CALL 405 2026-11-06 (9DTE): 1,031 traded vs OI 1,028
- **MSFT** PUT 520 2026-11-06 (9DTE): 804 traded vs OI 424
- **GOOGL** CALL 340 2026-10-30 (2DTE): 11,139 traded vs OI 8,483
- **NFLX** PUT 62 2026-10-30 (2DTE): 5,164 traded vs OI 5,152
- **HOOD** CALL 96 2026-11-06 (9DTE): 500 traded vs OI 389
- **HOOD** CALL 88 2026-10-30 (2DTE): 505 traded vs OI 134
- **HOOD** CALL 87 2026-10-30 (2DTE): 504 traded vs OI 144
- **HOOD** CALL 89 2026-11-06 (9DTE): 500 traded vs OI 150

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
