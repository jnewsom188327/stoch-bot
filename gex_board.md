# GEX + FLOW SCAN - Wed Oct 28, 12:55 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (4)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:40 | **HOOD** | **CALLS** | FLOW SURGE | 10/30 96C | 0.77 | 0.55 | -1% (3m) | **-29%** (done) | +49% | 93.02 |
| 11:05 | **HOOD** | **CALLS** | FLOW SURGE | 10/30 97C | 0.63 | 0.45 | +19% (1m) | **-29%** (done) | +53% | 93.44 |
| 10:50 | **IWM** | **CALLS** | FLOW SURGE | 10/30 284C | 0.57 | 0.54 | +7% (2m) | **-5%** (done) | +22% | 280.64 |
| 10:20 | **IWM** | **CALLS** | FLOW SURGE | 10/29 284C | 0.47 | 0.34 | +11% (0m) | **-28%** (done) | +27% | 281.41 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **SMH** | 567.04 | FLOW SURGE | **PUTS** | 35 | none: 180 puts 0-7DTE > 12 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (79 contracts' greeks worked out here) | POS +$81.0M | 558.85 | 570 | 555 | -$4.3M | +$0 bull / -$148k bear | out (clean 28, ADX 24, RVol 0.5) |
| 2 | **HOOD** | 91.21 | - | **-** | 25 | - | NEG -$17.3M | - | 100 | 90 | +$3.7M | +$0 bull / -$198k bear | out (clean 30, ADX 29, RVol 0.7) |
| 3 | **MSTR** | 139.68 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 21 | none: 26 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$18.0M | - | 152.5 | 140 | -$23k | - | out (clean 27, ADX 11, RVol 0.6) |
| 4 | **SMCI** | 34.94 | PINNED between the walls (positive gamma) - chop | **-** | 20 | - | POS +$19.3M | - | 35 | 35 | +$115k | - | out (clean 28, ADX 21, RVol 0.3) |
| 5 | **ORCL** | 130.84 | - | **-** | 20 | - | POS +$11.3M | 126.86 | 135 | 130 | -$987k | +$27k bull / +$0 bear | out (clean 29, ADX 16, RVol 0.4) |
| 6 | **PLTR** | 194.13 | - | **-** | 19 | - | POS +$41.7M | 189.35 | 200 | 190 | +$88k | +$0 bull / -$36k bear | out (clean 27, ADX 44, RVol 0.4) |
| 7 | **MSFT** | 527.80 | - | **-** | 18 | - | POS +$463.5M | - | 550 | 500 | +$2.6M | +$83k bull / -$25k bear | out (clean 29, ADX 16, RVol 0.7) |
| 8 | **GOOGL** | 323.94 | - | **-** | 18 | - | POS +$18.1M | 320.61 | 355 | 330 | -$3.2M | +$1.4M bull / -$153k bear | out (clean 33, ADX 12, RVol 0.8) |
| 9 | **MU** | 970.02 | - | **-** | 18 | - | POS +$618.8M | - | 950 | 950 | +$20.4M | +$1.2M bull / -$145k bear | out (clean 28, ADX 26, RVol 0.5) |
| 10 | **NVDA** | 217.69 | - | **-** | 17 | - | POS +$548.9M | 210.1 | 220 | 215 | +$7.2M | +$0 bull / -$233k bear | out (clean 27, ADX 17, RVol 0.4) |
| 11 | **AMD** | 570.74 | - | **-** | 17 | - | POS +$175.3M | - | 600 | 550 | +$100k | +$0 bull / -$648k bear | out (clean 29, ADX 30, RVol 0.6) |
| 12 | **META** | 614.36 | - | **-** | 17 | - | NEG -$268.1M | 635.46 | 650 | 610 | +$7.2M | +$541k bull / -$442k bear | out (clean 29, ADX 16, RVol 0.5) |
| 13 | **AVGO** | 348.82 | - | **-** | 17 | - | POS +$55.0M | 338.3 | 350 | 340 | -$918k | +$0 bull / -$156k bear | out (clean 29, ADX 22, RVol 0.5) |
| 14 | **AAPL** | 346.28 | - | **-** | 16 | - | POS +$406.5M | 342.05 | 350 | 345 | -$1.5M | +$0 bull / -$85k bear | out (clean 28, ADX 17, RVol 0.7) |
| 15 | **SPY** | 772.59 | - | **-** | 15 | - | NEG -$1.2B | 773.7 | 780 | 750 | -$26.1M | +$555k bull / -$1.3M bear | out (clean 29, ADX 12, RVol 0.5) |
| 16 | **TSLA** | 402.74 | - | **-** | 15 | - | POS +$588.6M | - | 400 | 395 | -$18.2M | +$25k bull / -$623k bear | out (clean 29, ADX 12, RVol 0.2) |
| 17 | **AMZN** | 252.92 | - | **-** | 14 | - | POS +$180.9M | 243.17 | 255 | 250 | -$766k | +$26k bull / +$0 bear | out (clean 32, ADX 15, RVol 0.5) |
| 18 | **SHOP** | 168.54 | - | **-** | 13 | - | NEG -$2.5M | 171.46 | 175 | 165 | -$34k | - | out (clean 29, ADX 28, RVol 0.7) |
| 19 | **QQQ** | 723.64 | - | **-** | 12 | - | NEG -$1.2B | 727.79 | 720 | 720 | -$484k | +$666k bull / -$151k bear | out (clean 29, ADX 9, RVol 0.3) |
| 20 | **IWM** | 280.87 | - | **-** | 11 | - | NEG -$184.6M | 281.34 | 280 | 270 | +$9.7M | - | out (clean 24, ADX 17, RVol 0.6) |
| 21 | **UBER** | 65.84 | - | **-** | 9 | - | NEG -$26.4M | 69.52 | 70 | 65 | -$38k | - | out (clean 30, ADX 36, RVol 0.6) |
| 22 | **NFLX** | 61.99 | - | **-** | 6 | - | NEG -$54.6M | - | 65 | 60 | -$71k | - | out (clean 32, ADX 22, RVol 0.6) |
| 23 | **ARM** | 233.60 | - | **-** | 6 | - | POS +$2.7M | - | 227.5 | 250 | +$46k | - | out (clean 27, ADX 22, RVol 0.8) |
| 24 | **BABA** | 100.47 | - | **-** | 6 | - | NEG -$13.6M | 103.83 | 102 | 100 | +$18k | - | out (clean 28, ADX 18, RVol 0.6) |
| 25 | **COIN** | 158.72 | - | **-** | 4 | - | POS +$1.2M | 155.79 | 170 | 150 | -$20k | - | out (clean 29, ADX 8, RVol 0.5) |
| 26 | **DELL** | 494.64 | - | **-** | 4 | - | POS +$29.3M | - | 500 | 500 | +$86k | - | out (clean 30, ADX 17, RVol 0.2) |
| 27 | **CRM** | 241.22 | - | **-** | 4 | - | POS +$6.9M | 234.1 | 260 | 240 | -$5k | - | out (clean 27, ADX 16, RVol 0.2) |

## Big prints this scan (43)
- **SPY** PUT 771 2026-10-28 (0DTE): 675 @ 2.14 = **+$144k** BUY | vol 135,751 / OI 1,490
- **AMD** CALL 570 2026-10-28 (0DTE): 399 @ 3.60 = **+$144k** SELL | vol 16,418 / OI 956
- **SPY** CALL 771 2026-10-29 (1DTE): 341 @ 3.38 = **+$115k** SELL | vol 28,519 / OI 811
- **SPY** CALL 771 2026-10-29 (1DTE): 292 @ 3.57 = **+$104k** SELL | vol 28,519 / OI 811
- **SPY** CALL 771 2026-10-29 (1DTE): 300 @ 3.37 = **+$101k** SELL | vol 28,519 / OI 811
- **META** PUT 640 2026-10-30 (2DTE): 30 @ 28.18 = **+$85k** BUY | vol 309 / OI 1,094
- **MU** PUT 975 2026-10-28 (0DTE): 100 @ 8.05 = **+$80k** SELL | vol 9,877 / OI 11
- **HOOD** PUT 91 2026-10-30 (2DTE): 360 @ 2.20 = **+$79k** BUY | vol 6,423 / OI 1,766
- **MU** PUT 965 2026-10-28 (0DTE): 200 @ 3.60 = **+$72k** SELL | vol 18,978 / OI 17
- **MU** CALL 975 2026-10-28 (0DTE): 145 @ 4.75 = **+$69k** BUY | vol 37,156 / OI 683
- **MU** CALL 975 2026-10-28 (0DTE): 132 @ 5.10 = **+$67k** BUY | vol 37,156 / OI 683
- **TSLA** CALL 397.5 2026-10-28 (0DTE): 145 @ 4.07 = **+$59k** SELL | vol 18,115 / OI 2,326
- **MU** PUT 1,000 2026-10-30 (2DTE): 14 @ 36.84 = **+$52k** SELL | vol 1,427 / OI 1,100
- **TSLA** PUT 400 2026-10-30 (2DTE): 106 @ 4.85 = **+$51k** BUY | vol 18,429 / OI 1,925
- **MU** CALL 980 2026-10-28 (0DTE): 168 @ 3.05 = **+$51k** BUY | vol 34,139 / OI 906

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 744 2026-10-28 (0DTE): 845 traded vs OI 802
- **SPY** PUT 771 2026-11-04 (7DTE): 529 traded vs OI 43
- **QQQ** PUT 677 2026-10-29 (1DTE): 548 traded vs OI 0
- **IWM** PUT 283 2026-10-28 (0DTE): 521 traded vs OI 18
- **AMD** CALL 575 2026-10-30 (2DTE): 1,978 traded vs OI 1,973
- **AMZN** PUT 257.5 2026-10-30 (2DTE): 501 traded vs OI 486
- **AMZN** CALL 242.5 2026-10-30 (2DTE): 508 traded vs OI 460
- **MU** PUT 950 2026-11-02 (5DTE): 502 traded vs OI 65

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
