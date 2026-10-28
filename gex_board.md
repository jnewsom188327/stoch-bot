# GEX + FLOW SCAN - Wed Oct 28, 02:20 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (6)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 12:56 | **QQQ** | **CALLS** | 1m WHIPSAW (R1 R2) | 10/28 730C | 0.63 | 0.67 | +24% (10m) | **+6%** (done) | -35% | 723.9 |
| 12:56 | **SPY** | **CALLS** | 1m WHIPSAW (R1 R2) | 10/29 779C | 0.63 | 0.51 | +3% (9m) | **-19%** (done) | +10% | 772.67 |
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
| 1 | **AAPL** | 344.35 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 37 | 10/30 350C @ 0.79 (delta 0.21) = est +11% at 345 | POS +$288.1M | 341.49 | 350 | 345 | +$2.5M | +$219k bull / +$0 bear | out (clean 28, ADX 14, RVol 1.1) |
| 2 | **IWM** | 279.68 | - | **-** | 24 | - | NEG -$503.7M | 281.01 | 280 | 270 | +$12.2M | +$385k bull / +$0 bear | out (clean 24, ADX 29, RVol 0.6) |
| 3 | **SMH** | 564.81 | - | **-** | 22 | - | POS +$50.0M | 560.42 | 570 | 555 | -$3.3M | +$35k bull / +$0 bear | out (clean 28, ADX 16, RVol 1.1) |
| 4 | **HOOD** | 90.03 | - | **-** | 22 | - | NEG -$18.0M | - | 95 | 90 | +$4.3M | +$95k bull / +$0 bear | out (clean 30, ADX 16, RVol 0.8) |
| 5 | **AMD** | 570.32 | - | **-** | 20 | - | POS +$171.5M | - | 600 | 550 | +$6.5M | +$890k bull / -$309k bear | out (clean 29, ADX 28, RVol 1.1) |
| 6 | **META** | 610.01 | - | **-** | 20 | - | NEG -$259.7M | 634.13 | 650 | 600 | +$10.8M | +$266k bull / +$0 bear | out (clean 29, ADX 23, RVol 0.9) |
| 7 | **PLTR** | 193.56 | - | **-** | 20 | - | POS +$34.2M | 189.4 | 200 | 190 | +$546k | +$56k bull / +$0 bear | out (clean 27, ADX 38, RVol 0.9) |
| 8 | **NVDA** | 216.58 | - | **-** | 18 | - | POS +$480.2M | 210.22 | 220 | 215 | +$10.6M | +$387k bull / +$0 bear | out (clean 26, ADX 17, RVol 0.7) |
| 9 | **AMZN** | 252.35 | - | **-** | 17 | - | POS +$176.6M | 242.17 | 250 | 250 | +$4.2M | +$798k bull / +$0 bear | out (clean 31, ADX 17, RVol 0.8) |
| 10 | **MSTR** | 139.47 | - | **-** | 17 | - | POS +$16.8M | - | 152.5 | 140 | +$1.1M | +$58k bull / -$29k bear | out (clean 27, ADX 12, RVol 0.4) |
| 11 | **GOOGL** | 323.10 | - | **-** | 16 | - | POS +$7.8M | 321.27 | 355 | 300 | +$582k | +$882k bull / +$0 bear | out (clean 32, ADX 22, RVol 1.1) |
| 12 | **AVGO** | 347.88 | - | **-** | 16 | - | POS +$61.8M | 336.26 | 350 | 340 | +$363k | +$265k bull / -$56k bear | out (clean 29, ADX 26, RVol 0.6) |
| 13 | **MU** | 967.10 | - | **-** | 16 | - | POS +$623.5M | - | 950 | 950 | +$24.9M | +$4.7M bull / -$800k bear | out (clean 28, ADX 19, RVol 0.4) |
| 14 | **QQQ** | 721.45 | - | **-** | 15 | - | NEG -$2.0B | 727.61 | 720 | 720 | +$29.2M | +$926k bull / -$487k bear | out (clean 29, ADX 11, RVol 0.7) |
| 15 | **TSLA** | 401.90 | - | **-** | 15 | - | POS +$600.2M | - | 400 | 400 | -$14.8M | +$1.9M bull / -$201k bear | out (clean 29, ADX 15, RVol 0.4) |
| 16 | **MSFT** | 526.58 | - | **-** | 15 | - | POS +$426.4M | - | 550 | 500 | +$184k | +$543k bull / +$0 bear | out (clean 29, ADX 14, RVol 1.4) |
| 17 | **SPY** | 770.12 | - | **-** | 14 | - | NEG -$3.2B | 773.08 | 770 | 750 | +$7.1M | +$2.0M bull / +$0 bear | out (clean 29, ADX 12, RVol 0.7) |
| 18 | **SHOP** | 167.10 | - | **-** | 11 | - | NEG -$4.5M | 172.28 | 175 | 165 | -$28k | - | out (clean 29, ADX 24, RVol 0.9) |
| 19 | **ORCL** | 131.32 | - | **-** | 10 | - | POS +$18.3M | 126.53 | 135 | 130 | -$805k | - | out (clean 29, ADX 18, RVol 1.3) |
| 20 | **BABA** | 99.88 | - | **-** | 10 | - | NEG -$15.7M | 102.85 | 102 | 100 | +$70k | - | out (clean 28, ADX 17, RVol 0.8) |
| 21 | **SMCI** | 34.77 | - | **-** | 8 | - | POS +$19.4M | - | 35 | 35 | +$140k | - | out (clean 28, ADX 17, RVol 0.5) |
| 22 | **UBER** | 65.29 | - | **-** | 8 | - | NEG -$33.2M | - | 70 | 65 | +$46k | - | out (clean 30, ADX 23, RVol 1.3) |
| 23 | **COIN** | 158.42 | - | **-** | 6 | - | POS +$1.3M | 155.57 | 170 | 150 | +$63k | - | out (clean 29, ADX 10, RVol 1.0) |
| 24 | **NFLX** | 61.59 | - | **-** | 5 | - | NEG -$58.3M | - | 65 | 60 | -$38k | - | out (clean 31, ADX 15, RVol 0.9) |
| 25 | **DELL** | 493.24 | - | **-** | 5 | - | POS +$28.9M | - | 500 | 500 | +$228k | - | out (clean 30, ADX 12, RVol 0.4) |
| 26 | **ARM** | 231.84 | - | **-** | 5 | - | POS +$1.6M | 223.74 | 227.5 | 250 | +$101k | - | out (clean 26, ADX 14, RVol 0.5) |
| 27 | **CRM** | 241.40 | - | **-** | 5 | - | POS +$6.4M | 234.85 | 260 | 240 | +$18k | - | out (clean 26, ADX 14, RVol 0.6) |

## Big prints this scan (79)
- **GOOGL** CALL 332.5 2026-10-30 (2DTE): 998 @ 6.40 = **+$639k** BUY | vol 3,637 / OI 7,806
- **MU** PUT 965 2026-10-28 (0DTE): 899 @ 3.70 = **+$333k** SELL | vol 30,740 / OI 17
- **SPY** PUT 775 2026-10-30 (2DTE): 450 @ 5.00 = **+$225k** SELL | vol 2,777 / OI 3,175
- **QQQ** PUT 726 2026-10-29 (1DTE): 338 @ 6.45 = **+$218k** SELL | vol 3,263 / OI 321
- **MSFT** CALL 532.5 2026-11-02 (5DTE): 200 @ 10.90 = **+$218k** MID | vol 251 / OI 82
- **SPY** CALL 770 2026-10-30 (2DTE): 392 @ 4.72 = **+$185k** BUY | vol 7,349 / OI 22,207
- **MU** CALL 955 2026-10-28 (0DTE): 100 @ 18.00 = **+$180k** BUY | vol 3,282 / OI 340
- **TSLA** CALL 400 2026-10-28 (0DTE): 487 @ 3.50 = **+$170k** BUY | vol 89,529 / OI 4,776
- **MU** CALL 970 2026-10-28 (0DTE): 195 @ 7.00 = **+$136k** BUY | vol 36,919 / OI 3,109
- **SPY** PUT 780 2026-10-30 (2DTE): 140 @ 9.18 = **+$129k** SELL | vol 897 / OI 3,391
- **MU** CALL 930 2026-11-04 (7DTE): 23 @ 55.25 = **+$127k** BUY | vol 214 / OI 30
- **MSFT** CALL 545 2026-11-02 (5DTE): 200 @ 6.20 = **+$124k** MID | vol 1,629 / OI 140
- **MSFT** CALL 545 2026-11-02 (5DTE): 200 @ 6.20 = **+$124k** MID | vol 1,629 / OI 140
- **MU** CALL 930 2026-11-04 (7DTE): 21 @ 55.20 = **+$116k** BUY | vol 214 / OI 30
- **AMD** CALL 567.5 2026-10-28 (0DTE): 166 @ 6.00 = **+$100k** BUY | vol 8,868 / OI 357

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 769 2026-11-04 (7DTE): 527 traded vs OI 55
- **QQQ** CALL 741 2026-10-29 (1DTE): 583 traded vs OI 71
- **QQQ** PUT 688 2026-10-28 (0DTE): 672 traded vs OI 0
- **QQQ** PUT 690 2026-10-29 (1DTE): 2,012 traded vs OI 1,923
- **QQQ** PUT 722 2026-11-13 (16DTE): 973 traded vs OI 169
- **IWM** CALL 283 2026-11-13 (16DTE): 1,022 traded vs OI 406
- **NVDA** CALL 227.5 2026-11-04 (7DTE): 500 traded vs OI 226
- **AAPL** PUT 310 2026-11-06 (9DTE): 2,235 traded vs OI 0
- **AMD** CALL 580 2026-10-30 (2DTE): 2,010 traded vs OI 1,965
- **ORCL** CALL 144 2026-10-30 (2DTE): 582 traded vs OI 0
- **ORCL** CALL 131 2026-10-30 (2DTE): 1,066 traded vs OI 1,059
- **HOOD** CALL 91 2026-11-20 (23DTE): 600 traded vs OI 520

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
