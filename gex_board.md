# GEX + FLOW SCAN - Wed Oct 28, 11:20 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (3)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:05 | **HOOD** | **CALLS** | FLOW SURGE | 10/30 97C | 0.63 | 0.73 | +19% (1m) | **+16%** | +53% | 93.44 |
| 10:50 | **IWM** | **CALLS** | FLOW SURGE | 10/30 284C | 0.57 | 0.57 | +7% (2m) | **+0%** | +22% | 280.64 |
| 10:20 | **IWM** | **CALLS** | FLOW SURGE | 10/29 284C | 0.47 | 0.36 | +11% (0m) | **-23%** | +27% | 281.41 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **CRM** | 239.45 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 46 | none: 19 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$3.8M | 235.22 | 260 | 240 | +$82k | - | out (clean 28, ADX 22, RVol 1.3) |
| 2 | **AAPL** | 345.05 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 36 | none: 81 calls 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (47 contracts' greeks worked out here) | POS +$331.8M | 341.16 | 350 | 345 | +$889k | +$1.0M bull / -$30k bear | out (clean 30, ADX 24, RVol 0.7) |
| 3 | **MSTR** | 140.10 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 31 | none: 25 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$18.1M | - | 152.5 | 140 | -$292k | +$0 bull / -$145k bear | out (clean 28, ADX 8, RVol 0.2) |
| 4 | **HOOD** | 92.32 | - | **-** | 29 | - | NEG -$15.4M | - | 100 | 90 | +$2.1M | +$0 bull / -$27k bear | out (clean 30, ADX 32, RVol 2.6) |
| 5 | **META** | 612.53 | - | **-** | 27 | - | NEG -$243.7M | 631.97 | 650 | 610 | +$12.4M | +$137k bull / -$895k bear | out (clean 29, ADX 32, RVol 1.5) |
| 6 | **GOOGL** | 323.54 | - | **-** | 27 | - | POS +$13.2M | 320.93 | 355 | 300 | +$3.1M | +$41k bull / -$46k bear | out (clean 33, ADX 18, RVol 1.3) |
| 7 | **MSFT** | 528.36 | - | **-** | 24 | - | POS +$460.3M | - | 550 | 500 | +$2.5M | +$0 bull / -$323k bear | out (clean 30, ADX 22, RVol 1.1) |
| 8 | **SMH** | 565.30 | - | **-** | 21 | - | POS +$56.7M | 559.97 | 570 | 555 | -$516k | +$0 bull / -$470k bear | out (clean 28, ADX 27, RVol 0.7) |
| 9 | **TSLA** | 401.75 | - | **-** | 21 | - | POS +$590.6M | - | 400 | 395 | -$23.3M | +$0 bull / -$1.9M bear | out (clean 28, ADX 25, RVol 0.7) |
| 10 | **PLTR** | 194.25 | - | **-** | 21 | - | POS +$41.7M | 188.91 | 200 | 190 | -$335k | +$221k bull / +$0 bear | out (clean 28, ADX 53, RVol 0.7) |
| 11 | **AMZN** | 252.43 | - | **-** | 20 | - | POS +$183.5M | 241.26 | 250 | 250 | +$2.6M | +$51k bull / -$1.7M bear | out (clean 32, ADX 23, RVol 1.1) |
| 12 | **MU** | 973.29 | - | **-** | 19 | - | POS +$606.1M | - | 950 | 950 | +$10.3M | +$0 bull / -$3.7M bear | out (clean 28, ADX 35, RVol 0.7) |
| 13 | **SHOP** | 165.80 | - | **-** | 19 | - | NEG -$5.6M | 173.13 | 175 | 165 | +$19k | - | out (clean 27, ADX 24, RVol 0.9) |
| 14 | **AMD** | 567.58 | - | **-** | 18 | - | POS +$171.4M | - | 600 | 550 | -$1.6M | +$0 bull / -$305k bear | out (clean 29, ADX 24, RVol 1.0) |
| 15 | **DELL** | 496.97 | - | **-** | 17 | - | POS +$31.0M | - | 500 | 500 | +$54k | +$0 bull / -$44k bear | out (clean 30, ADX 24, RVol 0.9) |
| 16 | **IWM** | 279.95 | - | **-** | 16 | - | NEG -$366.6M | 281.31 | 280 | 270 | +$10.5M | - | out (clean 24, ADX 21, RVol 0.7) |
| 17 | **NVDA** | 217.82 | - | **-** | 15 | - | POS +$580.2M | 210.11 | 220 | 215 | +$3.1M | +$170k bull / -$110k bear | out (clean 27, ADX 9, RVol 0.6) |
| 18 | **SPY** | 771.11 | - | **-** | 14 | - | NEG -$2.4B | 773.53 | 780 | 750 | +$5.2M | +$0 bull / -$535k bear | out (clean 30, ADX 12, RVol 0.6) |
| 19 | **QQQ** | 722.18 | - | **-** | 14 | - | NEG -$1.7B | 727.83 | 720 | 720 | -$8.6M | +$0 bull / -$101k bear | out (clean 30, ADX 11, RVol 0.3) |
| 20 | **UBER** | 64.93 | - | **-** | 11 | - | NEG -$33.0M | - | 70 | 65 | +$46k | - | out (clean 28, ADX 36, RVol 0.6) |
| 21 | **AVGO** | 346.11 | - | **-** | 10 | - | POS +$52.7M | 336.86 | 350 | 340 | +$1.4M | - | out (clean 30, ADX 14, RVol 1.2) |
| 22 | **NFLX** | 61.76 | - | **-** | 9 | - | NEG -$54.3M | - | 65 | 60 | +$12k | - | out (clean 32, ADX 47, RVol 0.5) |
| 23 | **SMCI** | 34.73 | - | **-** | 9 | - | POS +$18.5M | - | 35 | 35 | +$107k | - | out (clean 28, ADX 17, RVol 0.6) |
| 24 | **BABA** | 100.19 | - | **-** | 9 | - | NEG -$13.9M | 103.17 | 102 | 100 | +$28k | - | out (clean 28, ADX 18, RVol 0.3) |
| 25 | **COIN** | 158.80 | - | **-** | 8 | - | POS +$1.8M | 154.78 | 170 | 150 | -$43k | - | out (clean 29, ADX 16, RVol 0.4) |
| 26 | **ORCL** | 129.57 | - | **-** | 8 | - | POS +$7.0M | 126.91 | 135 | 130 | +$196k | - | out (clean 28, ADX 16, RVol 0.7) |
| 27 | **ARM** | 233.31 | - | **-** | 7 | - | POS +$2.0M | 222.16 | 227.5 | 250 | +$52k | - | out (clean 26, ADX 29, RVol 0.4) |

## Big prints this scan (100)
- **AMZN** CALL 245 2026-10-30 (2DTE): 294 @ 13.62 = **+$400k** SELL | vol 3,383 / OI 3,091
- **SPY** PUT 773 2026-10-28 (0DTE): 899 @ 3.85 = **+$346k** BUY | vol 24,246 / OI 703
- **META** PUT 600 2026-10-30 (2DTE): 798 @ 3.80 = **+$303k** BUY | vol 3,228 / OI 3,579
- **AAPL** CALL 350 2026-10-30 (2DTE): 1,691 @ 1.12 = **+$189k** BUY | vol 9,159 / OI 21,901
- **AMZN** CALL 265 2026-10-30 (2DTE): 319 @ 4.85 = **+$155k** MID | vol 933 / OI 18,534
- **TSLA** CALL 395 2026-10-28 (0DTE): 175 @ 6.30 = **+$110k** SELL | vol 3,161 / OI 3,025
- **TSLA** CALL 400 2026-10-28 (0DTE): 395 @ 2.75 = **+$109k** SELL | vol 63,524 / OI 4,776
- **QQQ** PUT 720 2026-11-04 (7DTE): 123 @ 8.23 = **+$101k** BUY | vol 941 / OI 140
- **AMD** CALL 572.5 2026-10-30 (2DTE): 100 @ 9.20 = **+$92k** SELL | vol 499 / OI 540
- **MSFT** PUT 520 2026-10-30 (2DTE): 95 @ 9.50 = **+$90k** MID | vol 1,172 / OI 2,074
- **MSFT** PUT 520 2026-10-30 (2DTE): 95 @ 9.50 = **+$90k** MID | vol 1,172 / OI 2,074
- **MSFT** PUT 520 2026-10-30 (2DTE): 95 @ 9.50 = **+$90k** MID | vol 1,172 / OI 2,074
- **MSFT** PUT 520 2026-10-30 (2DTE): 95 @ 9.50 = **+$90k** MID | vol 1,172 / OI 2,074
- **MSFT** PUT 520 2026-10-30 (2DTE): 95 @ 9.50 = **+$90k** MID | vol 1,172 / OI 2,074
- **MSFT** PUT 520 2026-10-30 (2DTE): 95 @ 9.50 = **+$90k** MID | vol 1,172 / OI 2,074

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 780 2026-10-28 (0DTE): 503 traded vs OI 10
- **QQQ** PUT 722 2026-10-30 (2DTE): 1,973 traded vs OI 1,850
- **QQQ** PUT 676 2026-10-28 (0DTE): 771 traded vs OI 0
- **QQQ** PUT 697 2026-10-28 (0DTE): 504 traded vs OI 0
- **IWM** CALL 278 2026-10-28 (0DTE): 1,214 traded vs OI 1,086
- **NVDA** CALL 200 2026-10-30 (2DTE): 1,205 traded vs OI 1,024
- **NVDA** CALL 217.5 2026-11-02 (5DTE): 686 traded vs OI 675
- **NVDA** CALL 222.5 2026-11-02 (5DTE): 982 traded vs OI 945
- **TSLA** CALL 395 2026-10-28 (0DTE): 3,161 traded vs OI 3,025
- **TSLA** PUT 397.5 2026-11-02 (5DTE): 517 traded vs OI 185
- **AAPL** CALL 355 2026-11-04 (7DTE): 1,441 traded vs OI 331
- **AMD** PUT 562.5 2026-10-30 (2DTE): 1,320 traded vs OI 50
- **META** CALL 647.5 2026-10-28 (0DTE): 585 traded vs OI 538
- **META** CALL 650 2026-11-06 (9DTE): 600 traded vs OI 594
- **AMZN** CALL 240 2026-10-30 (2DTE): 816 traded vs OI 591

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
