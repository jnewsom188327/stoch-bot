# GEX + FLOW SCAN - Wed Oct 28, 12:10 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (4)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:40 | **HOOD** | **CALLS** | FLOW SURGE | 10/30 96C | 0.77 | 0.64 | -1% (3m) | **-17%** | +49% | 93.02 |
| 11:05 | **HOOD** | **CALLS** | FLOW SURGE | 10/30 97C | 0.63 | 0.45 | +19% (1m) | **-29%** (done) | +53% | 93.44 |
| 10:50 | **IWM** | **CALLS** | FLOW SURGE | 10/30 284C | 0.57 | 0.54 | +7% (2m) | **-5%** (done) | +22% | 280.64 |
| 10:20 | **IWM** | **CALLS** | FLOW SURGE | 10/29 284C | 0.47 | 0.34 | +11% (0m) | **-28%** (done) | +27% | 281.41 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **HOOD** | 91.07 | FLOW SURGE | **CALLS** | 37 | 10/30 96C @ 0.65 (delta 0.21) = est +39% at 92.35 | NEG -$17.1M | - | 100 | 90 | +$3.9M | +$322k bull / +$0 bear | out (clean 30, ADX 29, RVol 0.5) |
| 2 | **MU** | 972.26 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 36 | none: 158 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (65 contracts' greeks worked out here) | POS +$610.1M | - | 970 | 950 | +$19.6M | +$1.7M bull / -$2.0M bear | out (clean 28, ADX 32, RVol 0.3) |
| 3 | **SMH** | 565.21 | FLOW SURGE | **PUTS** | 35 | none: 180 puts 0-7DTE > 12 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (88 contracts' greeks worked out here) | POS +$56.9M | 559.68 | 570 | 555 | -$4.2M | +$0 bull / -$672k bear | out (clean 28, ADX 23, RVol 0.5) |
| 4 | **IWM** | 280.15 | - | **-** | 23 | - | NEG -$350.2M | 281.28 | 280 | 270 | +$9.2M | +$73k bull / -$67k bear | out (clean 24, ADX 18, RVol 1.0) |
| 5 | **AAPL** | 345.53 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 22 | none: 84 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (49 contracts' greeks worked out here) | POS +$366.9M | 341.58 | 350 | 345 | +$93k | - | out (clean 29, ADX 17, RVol 0.6) |
| 6 | **PLTR** | 194.63 | - | **-** | 22 | - | POS +$44.0M | 189.14 | 200 | 190 | -$757k | +$0 bull / -$43k bear | out (clean 27, ADX 46, RVol 0.6) |
| 7 | **CRM** | 240.42 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 22 | none: 19 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$4.1M | 235.62 | 260 | 240 | +$20k | - | out (clean 27, ADX 20, RVol 0.2) |
| 8 | **MSFT** | 527.59 | - | **-** | 20 | - | POS +$459.7M | - | 550 | 500 | +$2.3M | +$110k bull / +$0 bear | out (clean 30, ADX 24, RVol 0.7) |
| 9 | **META** | 614.27 | - | **-** | 19 | - | NEG -$259.2M | 634.9 | 650 | 610 | +$7.8M | +$0 bull / -$155k bear | out (clean 29, ADX 22, RVol 0.6) |
| 10 | **NVDA** | 217.11 | - | **-** | 18 | - | POS +$519.8M | 210.17 | 220 | 215 | +$8.0M | +$712k bull / +$0 bear | out (clean 26, ADX 13, RVol 0.5) |
| 11 | **ORCL** | 130.81 | - | **-** | 18 | - | POS +$10.3M | 126.79 | 135 | 130 | -$431k | +$0 bull / -$71k bear | out (clean 28, ADX 16, RVol 0.5) |
| 12 | **AMD** | 566.80 | - | **-** | 17 | - | POS +$180.2M | - | 600 | 550 | +$2.5M | +$139k bull / -$246k bear | out (clean 29, ADX 26, RVol 0.5) |
| 13 | **GOOGL** | 324.01 | - | **-** | 17 | - | POS +$18.0M | 320.78 | 355 | 330 | -$2.0M | +$0 bull / -$230k bear | out (clean 33, ADX 15, RVol 0.4) |
| 14 | **TSLA** | 401.47 | - | **-** | 16 | - | POS +$589.6M | - | 400 | 395 | -$18.9M | +$1.3M bull / -$507k bear | out (clean 29, ADX 14, RVol 0.3) |
| 15 | **AMZN** | 252.72 | - | **-** | 16 | - | POS +$189.1M | 240.96 | 255 | 250 | +$1.7M | +$0 bull / -$166k bear | out (clean 32, ADX 20, RVol 0.4) |
| 16 | **AVGO** | 346.58 | - | **-** | 15 | - | POS +$51.6M | 337.79 | 350 | 340 | +$601k | +$46k bull / -$27k bear | out (clean 29, ADX 14, RVol 0.3) |
| 17 | **SPY** | 771.43 | - | **-** | 14 | - | NEG -$2.1B | 773.53 | 780 | 750 | -$12.8M | +$0 bull / -$126k bear | out (clean 29, ADX 12, RVol 0.4) |
| 18 | **MSTR** | 139.63 | - | **-** | 13 | - | POS +$17.2M | - | 152.5 | 140 | -$146k | +$0 bull / -$26k bear | out (clean 27, ADX 7, RVol 0.4) |
| 19 | **QQQ** | 722.22 | - | **-** | 12 | - | NEG -$1.7B | 727.91 | 720 | 720 | -$2.6M | +$119k bull / -$781k bear | out (clean 30, ADX 8, RVol 0.4) |
| 20 | **SHOP** | 166.29 | - | **-** | 12 | - | NEG -$5.0M | 171.41 | 175 | 165 | +$13k | - | out (clean 27, ADX 25, RVol 1.6) |
| 21 | **ARM** | 232.18 | - | **-** | 9 | - | POS +$1.9M | 222.6 | 227.5 | 250 | +$191k | - | out (clean 27, ADX 24, RVol 0.3) |
| 22 | **UBER** | 65.52 | - | **-** | 9 | - | NEG -$30.0M | - | 70 | 65 | -$29k | - | out (clean 29, ADX 30, RVol 0.8) |
| 23 | **SMCI** | 34.77 | - | **-** | 8 | - | POS +$18.3M | - | 35 | 35 | +$115k | - | out (clean 28, ADX 18, RVol 0.3) |
| 24 | **NFLX** | 61.92 | - | **-** | 7 | - | NEG -$56.9M | - | 65 | 60 | -$11k | - | out (clean 32, ADX 33, RVol 0.7) |
| 25 | **BABA** | 100.33 | - | **-** | 7 | - | NEG -$13.8M | 103.46 | 102 | 100 | +$28k | - | out (clean 27, ADX 13, RVol 0.4) |
| 26 | **COIN** | 158.65 | - | **-** | 5 | - | POS +$1.6M | 155.02 | 170 | 150 | -$34k | - | out (clean 29, ADX 10, RVol 0.4) |
| 27 | **DELL** | 494.60 | - | **-** | 5 | - | POS +$30.0M | - | 500 | 500 | +$102k | - | out (clean 30, ADX 15, RVol 0.6) |

## Big prints this scan (83)
- **SMH** CALL 542.5 2026-10-28 (0DTE): 116 @ 22.20 = **+$258k** SELL | vol 551 / OI 704
- **SMH** CALL 545 2026-10-30 (2DTE): 116 @ 21.95 = **+$255k** MID | vol 557 / OI 2,556
- **MU** PUT 965 2026-10-28 (0DTE): 588 @ 4.20 = **+$247k** BUY | vol 17,547 / OI 17
- **SMH** CALL 550 2026-10-30 (2DTE): 124 @ 18.16 = **+$225k** MID | vol 1,376 / OI 3,703
- **AMZN** CALL 252.5 2026-10-30 (2DTE): 170 @ 9.75 = **+$166k** SELL | vol 2,952 / OI 5,384
- **GOOGL** CALL 330 2026-10-30 (2DTE): 228 @ 6.90 = **+$157k** MID | vol 5,828 / OI 6,833
- **SMH** CALL 542.5 2026-10-28 (0DTE): 67 @ 22.22 = **+$149k** SELL | vol 551 / OI 704
- **SMH** CALL 545 2026-10-30 (2DTE): 67 @ 21.97 = **+$147k** MID | vol 557 / OI 2,556
- **SMH** CALL 550 2026-10-30 (2DTE): 76 @ 18.00 = **+$137k** MID | vol 1,376 / OI 3,703
- **MU** CALL 1,000 2026-10-30 (2DTE): 153 @ 8.70 = **+$133k** SELL | vol 12,022 / OI 8,792
- **MU** PUT 965 2026-10-28 (0DTE): 323 @ 4.10 = **+$132k** BUY | vol 17,547 / OI 17
- **SPY** PUT 772 2026-10-28 (0DTE): 500 @ 2.53 = **+$126k** BUY | vol 31,126 / OI 544
- **MU** CALL 955 2026-10-28 (0DTE): 75 @ 16.50 = **+$124k** SELL | vol 2,129 / OI 340
- **NVDA** CALL 220 2026-10-30 (2DTE): 750 @ 1.60 = **+$120k** BUY | vol 33,350 / OI 53,027
- **QQQ** PUT 720 2026-10-30 (2DTE): 231 @ 5.17 = **+$119k** SELL | vol 5,689 / OI 20,177

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 780 2026-11-03 (6DTE): 1,999 traded vs OI 565
- **NVDA** PUT 212.5 2026-11-04 (7DTE): 515 traded vs OI 182
- **NVDA** CALL 207.5 2026-11-02 (5DTE): 538 traded vs OI 411
- **TSLA** PUT 390 2026-11-04 (7DTE): 648 traded vs OI 137
- **TSLA** PUT 365 2026-11-06 (9DTE): 1,701 traded vs OI 1,641
- **AMD** CALL 590 2026-11-02 (5DTE): 581 traded vs OI 37
- **HOOD** PUT 89 2026-11-06 (9DTE): 501 traded vs OI 359
- **UBER** CALL 67 2026-11-06 (9DTE): 512 traded vs OI 362

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
