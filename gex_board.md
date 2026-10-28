# GEX + FLOW SCAN - Wed Oct 28, 11:05 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (3)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:05 | **HOOD** | **CALLS** | FLOW SURGE | 10/30 97C | 0.63 | 0.61 | -3% (0m) | **-3%** | +53% | 93.44 |
| 10:50 | **IWM** | **CALLS** | FLOW SURGE | 10/30 284C | 0.57 | 0.53 | +7% (2m) | **-7%** | +22% | 280.64 |
| 10:20 | **IWM** | **CALLS** | FLOW SURGE | 10/29 284C | 0.47 | 0.33 | +11% (0m) | **-30%** | +27% | 281.41 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **HOOD** | 91.83 | FLOW SURGE | **CALLS** | 51 | 10/30 97C @ 0.63 (delta 0.20) = est +53% at 93.44 | NEG -$16.1M | - | 100 | 90 | +$2.2M | +$264k bull / -$49k bear | out (clean 30, ADX 37, RVol 2.3) |
| 2 | **META** | 613.04 | FLOW SURGE | **CALLS** | 46 | none: 179 calls 0-7DTE > 11 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (73 contracts' greeks worked out here) | NEG -$259.6M | 635.28 | 650 | 610 | +$12.5M | +$768k bull / -$112k bear | out (clean 29, ADX 32, RVol 1.6) |
| 3 | **GOOGL** | 323.76 | FLOW SURGE | **CALLS** | 44 | none: 78 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$17.9M | 320.31 | 355 | 300 | +$3.0M | +$160k bull / +$0 bear | out (clean 33, ADX 21, RVol 1.9) |
| 4 | **IWM** | 279.72 | FLOW SURGE | **CALLS** | 41 | 11/02 284C @ 0.76 (delta 0.23) = est +4% at 280 | NEG -$498.4M | 281.34 | 280 | 270 | +$11.3M | +$51k bull / +$0 bear | out (clean 24, ADX 21, RVol 0.9) |
| 5 | **AAPL** | 345.28 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 38 | none: 81 calls 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (47 contracts' greeks worked out here) | POS +$345.7M | 341.36 | 350 | 345 | -$633k | +$45k bull / -$124k bear | out (clean 30, ADX 26, RVol 0.9) |
| 6 | **AMZN** | 252.50 | FLOW SURGE | **CALLS** | 37 | none: 84 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (34 contracts' greeks worked out here) | POS +$186.8M | 240.43 | 255 | 250 | +$4.4M | +$2.4M bull / +$0 bear | out (clean 32, ADX 20, RVol 1.0) |
| 7 | **MSFT** | 528.39 | - | **-** | 25 | - | POS +$457.9M | - | 550 | 500 | +$1.8M | +$254k bull / +$0 bear | out (clean 30, ADX 21, RVol 1.2) |
| 8 | **PLTR** | 194.88 | - | **-** | 25 | - | POS +$46.0M | 189.01 | 200 | 190 | -$1.0M | +$82k bull / +$0 bear | out (clean 28, ADX 52, RVol 0.7) |
| 9 | **ORCL** | 130.22 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 25 | none: 26 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$9.0M | 126.74 | 135 | 130 | +$126k | - | out (clean 28, ADX 14, RVol 0.7) |
| 10 | **SHOP** | 166.09 | - | **-** | 24 | - | NEG -$5.5M | 172.4 | 175 | 165 | +$22k | - | out (clean 26, ADX 22, RVol 0.9) |
| 11 | **AVGO** | 345.27 | - | **-** | 23 | - | POS +$43.8M | 337.09 | 350 | 340 | +$1.9M | +$53k bull / +$0 bear | out (clean 30, ADX 16, RVol 0.9) |
| 12 | **DELL** | 493.20 | - | **-** | 23 | - | POS +$28.7M | - | 500 | 500 | +$264k | +$25k bull / +$0 bear | out (clean 30, ADX 28, RVol 1.3) |
| 13 | **CRM** | 240.80 | - | **-** | 23 | - | POS +$4.4M | 235.49 | 260 | 240 | +$62k | - | out (clean 27, ADX 19, RVol 1.4) |
| 14 | **SMH** | 564.49 | - | **-** | 21 | - | POS +$47.7M | 559.9 | 570 | 555 | +$355k | +$0 bull / -$119k bear | out (clean 29, ADX 27, RVol 0.6) |
| 15 | **MU** | 970.65 | - | **-** | 21 | - | POS +$610.2M | - | 950 | 950 | +$18.9M | +$1.9M bull / -$3.4M bear | out (clean 28, ADX 34, RVol 0.4) |
| 16 | **TSLA** | 401.31 | - | **-** | 19 | - | POS +$571.2M | - | 400 | 395 | -$8.6M | +$0 bull / -$977k bear | out (clean 28, ADX 31, RVol 0.8) |
| 17 | **COIN** | 158.53 | - | **-** | 19 | - | POS +$1.3M | 155.31 | 170 | 150 | -$39k | +$0 bull / -$81k bear | out (clean 30, ADX 20, RVol 0.8) |
| 18 | **MSTR** | 139.80 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 19 | none: 26 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$17.2M | - | 152.5 | 140 | -$33k | - | out (clean 29, ADX 9, RVol 0.2) |
| 19 | **NVDA** | 217.90 | - | **-** | 17 | - | POS +$580.3M | 210.14 | 220 | 215 | +$4.1M | +$623k bull / +$0 bear | out (clean 27, ADX 10, RVol 0.7) |
| 20 | **SPY** | 770.73 | - | **-** | 16 | - | NEG -$3.0B | 773.59 | 780 | 750 | +$17.8M | +$2.3M bull / -$166k bear | out (clean 30, ADX 14, RVol 0.6) |
| 21 | **AMD** | 565.01 | - | **-** | 16 | - | POS +$169.9M | - | 550 | 550 | +$805k | +$0 bull / -$897k bear | out (clean 28, ADX 20, RVol 0.6) |
| 22 | **BABA** | 100.16 | - | **-** | 16 | - | NEG -$14.0M | 103.22 | 102 | 100 | +$50k | - | out (clean 28, ADX 20, RVol 0.6) |
| 23 | **UBER** | 64.94 | - | **-** | 13 | - | NEG -$34.2M | - | 70 | 65 | +$41k | - | out (clean 28, ADX 39, RVol 0.8) |
| 24 | **SMCI** | 34.84 | - | **-** | 12 | - | POS +$18.8M | - | 35 | 35 | +$148k | - | out (clean 28, ADX 18, RVol 0.5) |
| 25 | **NFLX** | 61.83 | - | **-** | 9 | - | NEG -$57.6M | - | 65 | 60 | -$5k | - | out (clean 32, ADX 47, RVol 0.5) |
| 26 | **ARM** | 233.12 | - | **-** | 9 | - | POS +$1.9M | 222.84 | 227.5 | 250 | +$90k | - | out (clean 26, ADX 28, RVol 0.5) |
| 27 | **QQQ** | 722.04 | - | **-** | 5 | - | NEG -$1.8B | 727.89 | 720 | 720 | +$9.6M | - | out (clean 31, ADX 13, RVol 0.4) |

## Big prints this scan (75)
- **AMZN** CALL 247.5 2026-10-30 (2DTE): 240 @ 12.70 = **+$305k** BUY | vol 1,636 / OI 2,411
- **AMZN** CALL 247.5 2026-10-30 (2DTE): 172 @ 12.70 = **+$218k** BUY | vol 1,636 / OI 2,411
- **AMZN** CALL 247.5 2026-10-30 (2DTE): 171 @ 12.70 = **+$217k** BUY | vol 1,636 / OI 2,411
- **AMZN** CALL 247.5 2026-10-30 (2DTE): 158 @ 12.65 = **+$200k** MID | vol 1,636 / OI 2,411
- **SPY** PUT 773 2026-10-28 (0DTE): 444 @ 3.75 = **+$166k** BUY | vol 19,708 / OI 703
- **AMZN** CALL 247.5 2026-10-30 (2DTE): 106 @ 12.75 = **+$135k** BUY | vol 1,636 / OI 2,411
- **AMZN** CALL 247.5 2026-10-28 (0DTE): 240 @ 5.49 = **+$132k** BUY | vol 1,141 / OI 3,053
- **SPY** CALL 771 2026-10-28 (0DTE): 500 @ 2.13 = **+$106k** BUY | vol 103,337 / OI 4,302
- **AMZN** PUT 257.5 2026-10-28 (0DTE): 200 @ 4.90 = **+$98k** SELL | vol 280 / OI 393
- **AMZN** CALL 247.5 2026-10-28 (0DTE): 172 @ 5.49 = **+$94k** BUY | vol 1,141 / OI 3,053
- **AMZN** CALL 247.5 2026-10-28 (0DTE): 171 @ 5.49 = **+$94k** BUY | vol 1,141 / OI 3,053
- **TSLA** CALL 400 2026-10-30 (2DTE): 157 @ 5.65 = **+$89k** SELL | vol 10,179 / OI 16,597
- **AMZN** CALL 247.5 2026-10-28 (0DTE): 158 @ 5.45 = **+$86k** BUY | vol 1,141 / OI 3,053
- **TSLA** CALL 400 2026-11-04 (7DTE): 100 @ 8.50 = **+$85k** SELL | vol 344 / OI 453
- **MU** PUT 970 2026-11-02 (5DTE): 30 @ 23.41 = **+$70k** BUY | vol 529 / OI 23

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 782 2026-10-29 (1DTE): 1,090 traded vs OI 1,057
- **QQQ** CALL 721 2026-10-30 (2DTE): 1,047 traded vs OI 808
- **QQQ** PUT 700 2026-10-29 (1DTE): 1,869 traded vs OI 1,851
- **QQQ** CALL 725 2026-10-29 (1DTE): 2,350 traded vs OI 2,322
- **QQQ** PUT 726 2026-10-29 (1DTE): 508 traded vs OI 321
- **IWM** CALL 281 2026-11-03 (6DTE): 500 traded vs OI 387
- **AAPL** PUT 342.5 2026-10-30 (2DTE): 2,833 traded vs OI 2,738
- **AAPL** CALL 335 2026-10-28 (0DTE): 508 traded vs OI 266
- **AMD** CALL 595 2026-10-28 (0DTE): 518 traded vs OI 159
- **AMD** CALL 620 2026-10-30 (2DTE): 788 traded vs OI 0
- **MU** PUT 970 2026-11-02 (5DTE): 529 traded vs OI 23
- **ORCL** PUT 134 2026-11-20 (23DTE): 1,903 traded vs OI 746

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
