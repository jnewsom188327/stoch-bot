# GEX + FLOW SCAN - Wed Oct 28, 01:50 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (6)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 12:56 | **QQQ** | **CALLS** | 1m WHIPSAW (R1 R2) | 10/28 730C | 0.63 | 0.59 | +24% (10m) | **-6%** | -35% | 723.9 |
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
| 1 | **AAPL** | 345.54 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 33 | none: 84 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (47 contracts' greeks worked out here) | POS +$382.6M | 341.54 | 350 | 345 | +$475k | +$73k bull / +$0 bear | out (clean 28, ADX 16, RVol 0.7) |
| 2 | **ORCL** | 130.22 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 24 | none: 26 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$10.6M | 126.79 | 135 | 130 | -$781k | - | out (clean 29, ADX 11, RVol 0.4) |
| 3 | **MSTR** | 139.83 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 20 | none: 26 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$17.8M | - | 152.5 | 140 | +$219k | - | out (clean 27, ADX 9, RVol 0.3) |
| 4 | **AMD** | 567.39 | - | **-** | 19 | - | POS +$186.0M | - | 600 | 550 | +$6.4M | +$1.4M bull / +$0 bear | out (clean 29, ADX 28, RVol 0.5) |
| 5 | **NVDA** | 216.84 | - | **-** | 18 | - | POS +$496.0M | 210.1 | 220 | 215 | +$9.3M | +$36k bull / -$59k bear | out (clean 26, ADX 18, RVol 0.7) |
| 6 | **GOOGL** | 324.74 | - | **-** | 18 | - | POS +$18.2M | 320.97 | 355 | 330 | -$1.5M | +$30k bull / -$532k bear | out (clean 32, ADX 27, RVol 1.1) |
| 7 | **PLTR** | 194.15 | - | **-** | 18 | - | POS +$42.3M | 189.46 | 200 | 190 | +$164k | +$52k bull / +$0 bear | out (clean 27, ADX 40, RVol 0.3) |
| 8 | **META** | 612.34 | - | **-** | 17 | - | NEG -$259.2M | 634.77 | 650 | 610 | +$7.6M | +$31k bull / -$148k bear | out (clean 28, ADX 16, RVol 0.6) |
| 9 | **MSFT** | 527.82 | - | **-** | 17 | - | POS +$468.7M | - | 550 | 500 | -$3.3M | +$0 bull / -$6.4M bear | out (clean 29, ADX 14, RVol 1.0) |
| 10 | **AVGO** | 347.63 | - | **-** | 17 | - | POS +$62.1M | 336.45 | 350 | 340 | -$475k | +$0 bull / -$32k bear | out (clean 29, ADX 30, RVol 0.4) |
| 11 | **MU** | 968.41 | - | **-** | 17 | - | POS +$626.1M | - | 950 | 950 | +$18.7M | +$435k bull / -$3.4M bear | out (clean 28, ADX 23, RVol 0.5) |
| 12 | **AMZN** | 252.66 | - | **-** | 16 | - | POS +$180.2M | 238.52 | 255 | 250 | +$2.9M | +$120k bull / -$84k bear | out (clean 31, ADX 15, RVol 0.6) |
| 13 | **TSLA** | 402.12 | - | **-** | 14 | - | POS +$599.4M | - | 400 | 395 | -$16.5M | +$235k bull / -$145k bear | out (clean 29, ADX 11, RVol 0.1) |
| 14 | **DELL** | 493.14 | - | **-** | 14 | - | POS +$28.0M | - | 500 | 500 | +$124k | +$46k bull / +$0 bear | out (clean 31, ADX 12, RVol 0.3) |
| 15 | **SPY** | 771.13 | - | **-** | 13 | - | NEG -$2.3B | 773.33 | 780 | 750 | -$8.1M | +$5.6M bull / -$9.0M bear | out (clean 28, ADX 11, RVol 0.2) |
| 16 | **QQQ** | 722.07 | - | **-** | 13 | - | NEG -$1.7B | 727.85 | 720 | 720 | +$8.6M | +$268k bull / -$268k bear | out (clean 29, ADX 10, RVol 0.3) |
| 17 | **SMH** | 564.48 | - | **-** | 13 | - | POS +$55.0M | 559.78 | 570 | 555 | -$3.8M | - | out (clean 28, ADX 20, RVol 0.6) |
| 18 | **IWM** | 280.43 | - | **-** | 12 | - | NEG -$228.8M | 281.19 | 280 | 270 | +$9.2M | - | out (clean 24, ADX 30, RVol 0.3) |
| 19 | **HOOD** | 90.89 | - | **-** | 12 | - | NEG -$17.1M | - | 95 | 90 | +$3.8M | - | out (clean 30, ADX 17, RVol 0.5) |
| 20 | **SHOP** | 168.07 | - | **-** | 11 | - | NEG -$3.4M | 171.88 | 175 | 165 | -$28k | - | out (clean 29, ADX 27, RVol 0.3) |
| 21 | **BABA** | 100.17 | - | **-** | 10 | - | NEG -$14.1M | 103.37 | 102 | 100 | +$66k | - | out (clean 28, ADX 16, RVol 0.9) |
| 22 | **SMCI** | 34.84 | - | **-** | 7 | - | POS +$19.2M | - | 35 | 35 | +$111k | - | out (clean 28, ADX 15, RVol 0.3) |
| 23 | **UBER** | 65.60 | - | **-** | 6 | - | NEG -$25.7M | 69.04 | 70 | 65 | +$13k | - | out (clean 30, ADX 27, RVol 0.4) |
| 24 | **NFLX** | 61.78 | - | **-** | 5 | - | NEG -$53.1M | - | 65 | 60 | -$114k | - | out (clean 31, ADX 13, RVol 0.5) |
| 25 | **ARM** | 232.21 | - | **-** | 5 | - | POS +$1.9M | 222.23 | 220 | 240 | +$79k | - | out (clean 26, ADX 15, RVol 0.4) |
| 26 | **COIN** | 158.87 | - | **-** | 4 | - | POS +$2.1M | 154.86 | 170 | 150 | +$37k | - | out (clean 29, ADX 7, RVol 0.6) |
| 27 | **CRM** | 241.10 | - | **-** | 4 | - | POS +$6.0M | 235 | 260 | 240 | +$15k | - | out (clean 27, ADX 12, RVol 0.5) |

## Big prints this scan (46)
- **MSFT** PUT 525 2026-10-30 (2DTE): 1,300 @ 11.97 = **+$1.6M** BUY | vol 3,257 / OI 1,668
- **MSFT** PUT 525 2026-10-30 (2DTE): 1,300 @ 11.97 = **+$1.6M** BUY | vol 3,257 / OI 1,668
- **MSFT** PUT 517.5 2026-10-30 (2DTE): 1,300 @ 8.75 = **+$1.1M** BUY | vol 1,677 / OI 585
- **MSFT** PUT 512.5 2026-10-30 (2DTE): 1,300 @ 6.90 = **+$897k** BUY | vol 1,443 / OI 328
- **SPY** CALL 765 2026-10-30 (2DTE): 500 @ 8.11 = **+$406k** SELL | vol 806 / OI 6,836
- **MU** CALL 970 2026-10-28 (0DTE): 495 @ 4.20 = **+$208k** SELL | vol 32,085 / OI 3,109
- **SPY** CALL 772 2026-10-30 (2DTE): 500 @ 3.56 = **+$178k** SELL | vol 6,290 / OI 4,558
- **MSFT** PUT 532.5 2026-11-04 (7DTE): 97 @ 17.02 = **+$165k** BUY | vol 855 / OI 11
- **QQQ** CALL 721 2026-10-30 (2DTE): 219 @ 6.90 = **+$151k** SELL | vol 2,642 / OI 808
- **MU** CALL 975 2026-10-28 (0DTE): 500 @ 2.79 = **+$140k** SELL | vol 47,963 / OI 683
- **MSFT** PUT 532.5 2026-11-04 (7DTE): 81 @ 17.01 = **+$138k** BUY | vol 855 / OI 11
- **AMD** CALL 550 2026-10-28 (0DTE): 70 @ 18.25 = **+$128k** BUY | vol 326 / OI 1,175
- **SPY** CALL 770 2026-11-02 (5DTE): 200 @ 5.40 = **+$108k** SELL | vol 4,574 / OI 934
- **MU** CALL 980 2026-10-28 (0DTE): 495 @ 1.60 = **+$79k** SELL | vol 44,409 / OI 906
- **MU** CALL 975 2026-10-28 (0DTE): 270 @ 2.70 = **+$73k** SELL | vol 47,963 / OI 683

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 772 2026-11-03 (6DTE): 511 traded vs OI 239
- **SPY** CALL 769 2026-11-04 (7DTE): 503 traded vs OI 53
- **QQQ** CALL 733 2026-11-03 (6DTE): 572 traded vs OI 123
- **QQQ** PUT 680 2026-11-06 (9DTE): 21,987 traded vs OI 21,665
- **IWM** PUT 280 2026-11-06 (9DTE): 500 traded vs OI 370
- **AMD** CALL 600 2026-11-02 (5DTE): 506 traded vs OI 420
- **META** CALL 647.5 2026-10-30 (2DTE): 501 traded vs OI 252
- **MSFT** PUT 512.5 2026-10-30 (2DTE): 1,443 traded vs OI 328
- **MSFT** PUT 525 2026-10-30 (2DTE): 3,257 traded vs OI 1,668
- **MSFT** PUT 517.5 2026-10-30 (2DTE): 1,677 traded vs OI 585
- **AVGO** CALL 365 2026-11-02 (5DTE): 687 traded vs OI 26
- **MU** PUT 965 2026-11-02 (5DTE): 500 traded vs OI 9

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
