# GEX + FLOW SCAN - Wed Oct 28, 03:30 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (8)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 14:35 | **QQQ** | **CALLS** | 1m WHIPSAW (R1 R2) | 10/28 730C | 0.67 | 0.08 | +64% (2m) | **-88%** | -70% | 724.9 hit |
| 14:35 | **SPY** | **CALLS** | 1m WHIPSAW (R1 R2 R5 R6) | 10/29 778C | 0.75 | 0.44 | +43% (2m) | **-41%** | +27% | 772.74 hit |
| 12:56 | **QQQ** | **CALLS** | 1m WHIPSAW (R1 R2) | 10/28 730C | 0.63 | 0.67 | +24% (10m) | **+6%** (done) | -35% | 723.9 |
| 12:56 | **SPY** | **CALLS** | 1m WHIPSAW (R1 R2) | 10/29 779C | 0.63 | 0.51 | +3% (9m) | **-19%** (done) | +10% | 772.67 |
| 11:40 | **HOOD** | **CALLS** | FLOW SURGE | 10/30 96C | 0.77 | 0.55 | -1% (3m) | **-29%** (done) | +49% | 93.02 |
| 11:05 | **HOOD** | **CALLS** | FLOW SURGE | 10/30 97C | 0.63 | 0.45 | +19% (1m) | **-29%** (done) | +53% | 93.44 |
| 10:50 | **IWM** | **CALLS** | FLOW SURGE | 10/30 284C | 0.57 | 0.54 | +7% (2m) | **-5%** (done) | +22% | 280.64 |
| 10:20 | **IWM** | **CALLS** | FLOW SURGE | 10/29 284C | 0.47 | 0.34 | +11% (0m) | **-28%** (done) | +27% | 281.41 |

## 1m RULES on SPY / QQQ - loose (4 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 14:34 | QQQ | 1m WHIPSAW | R1 R2 | CALLS | WITH you | **FIRE** QQQ261028C00730000 |
| 14:34 | SPY | 1m WHIPSAW | R1 R2 R5 R6 | CALLS | WITH you | **FIRE** SPY261029C00778000 |
| 12:55 | QQQ | 1m WHIPSAW | R1 R2 | CALLS | WITH you | **FIRE** QQQ261028C00730000 |
| 12:55 | SPY | 1m WHIPSAW | R1 R2 | CALLS | WITH you | **FIRE** SPY261029C00779000 |

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **NVDA** | 215.10 | PINNED between the walls (positive gamma) - chop | **-** | 37 | - | POS +$349.2M | 210.84 | 215 | 215 | +$22.7M | +$547k bull / +$0 bear | out (clean 26, ADX 24, RVol 1.0) |
| 2 | **AVGO** | 350.25 | PINNED between the walls (positive gamma) - chop | **-** | 37 | - | POS +$60.6M | 340.49 | 350 | 350 | +$2.5M | +$434k bull / -$84k bear | out (clean 30, ADX 38, RVol 1.1) |
| 3 | **AAPL** | 344.14 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 34 | none: 84 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (44 contracts' greeks worked out here) | POS +$269.8M | 341.93 | 350 | 345 | +$4.2M | +$427k bull / +$0 bear | out (clean 28, ADX 11, RVol 0.7) |
| 4 | **ORCL** | 146.51 | - | **-** | 33 | - | POS +$30.7M | - | 135 | 140 | -$30.0M | +$402k bull / -$175k bear | out (clean 30, ADX 59, RVol 3.1) |
| 5 | **AMD** | 575.08 | - | **-** | 22 | - | POS +$174.2M | - | 600 | 550 | +$7.4M | +$876k bull / -$236k bear | out (clean 30, ADX 42, RVol 1.3) |
| 6 | **SMH** | 565.31 | - | **-** | 19 | - | POS +$62.3M | 560.26 | 570 | 555 | -$3.0M | +$233k bull / +$0 bear | out (clean 28, ADX 20, RVol 0.6) |
| 7 | **MSTR** | 141.01 | - | **-** | 19 | - | POS +$20.2M | - | 152.5 | 150 | +$1.3M | +$0 bull / -$56k bear | out (clean 26, ADX 26, RVol 0.6) |
| 8 | **QQQ** | 722.75 | - | **-** | 18 | - | NEG -$1.4B | 726.67 | 720 | 720 | +$50.8M | +$1.1M bull / -$268k bear | out (clean 29, ADX 24, RVol 0.7) |
| 9 | **AMZN** | 254.15 | - | **-** | 18 | - | POS +$205.6M | 239.79 | 255 | 250 | -$686k | +$904k bull / -$180k bear | out (clean 31, ADX 31, RVol 1.3) |
| 10 | **GOOGL** | 323.81 | - | **-** | 18 | - | POS +$14.7M | 320.37 | 355 | 300 | -$1.1M | +$2.1M bull / -$103k bear | out (clean 32, ADX 23, RVol 1.4) |
| 11 | **SPY** | 770.89 | - | **-** | 17 | - | NEG -$2.5B | 772.86 | 770 | 765 | +$33.6M | +$1.0M bull / -$814k bear | out (clean 28, ADX 21, RVol 1.2) |
| 12 | **META** | 610.67 | - | **-** | 17 | - | NEG -$262.9M | 633.56 | 650 | 610 | +$7.2M | +$1.2M bull / -$29k bear | out (clean 29, ADX 20, RVol 0.8) |
| 13 | **MU** | 979.69 | - | **-** | 17 | - | POS +$574.3M | - | 1,000 | 950 | +$17.9M | +$3.3M bull / -$2.1M bear | out (clean 29, ADX 23, RVol 0.7) |
| 14 | **TSLA** | 402.91 | - | **-** | 16 | - | POS +$659.4M | - | 400 | 400 | -$4.1M | +$1.6M bull / -$167k bear | out (clean 30, ADX 27, RVol 0.5) |
| 15 | **MSFT** | 529.00 | - | **-** | 16 | - | POS +$473.5M | - | 550 | 500 | -$295k | +$277k bull / -$83k bear | out (clean 29, ADX 23, RVol 0.9) |
| 16 | **NFLX** | 61.63 | - | **-** | 14 | - | NEG -$59.1M | - | 65 | 60 | -$104k | +$0 bull / -$47k bear | out (clean 31, ADX 11, RVol 0.7) |
| 17 | **HOOD** | 90.94 | - | **-** | 13 | - | NEG -$18.8M | - | 100 | 90 | +$4.8M | - | out (clean 29, ADX 13, RVol 1.5) |
| 18 | **IWM** | 279.66 | - | **-** | 10 | - | NEG -$312.0M | 280.6 | 280 | 270 | +$12.8M | - | out (clean 24, ADX 22, RVol 0.7) |
| 19 | **SMCI** | 35.28 | - | **-** | 9 | - | POS +$21.0M | - | 35 | 35 | +$66k | - | out (clean 28, ADX 30, RVol 0.8) |
| 20 | **ARM** | 233.75 | - | **-** | 8 | - | POS +$2.7M | - | 227.5 | 250 | +$469k | - | out (clean 26, ADX 22, RVol 0.2) |
| 21 | **PLTR** | 193.79 | - | **-** | 7 | - | POS +$37.8M | 189.71 | 200 | 190 | +$1.0M | - | out (clean 27, ADX 22, RVol 0.6) |
| 22 | **COIN** | 159.41 | - | **-** | 7 | - | POS +$2.4M | 154.95 | 170 | 150 | +$119k | - | out (clean 28, ADX 14, RVol 0.7) |
| 23 | **DELL** | 494.32 | - | **-** | 7 | - | POS +$28.5M | - | 500 | 500 | +$264k | - | out (clean 31, ADX 20, RVol 0.5) |
| 24 | **UBER** | 65.14 | - | **-** | 7 | - | NEG -$33.0M | - | 70 | 65 | +$61k | - | out (clean 29, ADX 20, RVol 0.8) |
| 25 | **SHOP** | 167.27 | - | **-** | 7 | - | NEG -$3.8M | 171.05 | 175 | 165 | -$21k | - | out (clean 28, ADX 14, RVol 0.8) |
| 26 | **BABA** | 100.44 | - | **-** | 7 | - | NEG -$12.2M | 102.64 | 102 | 100 | +$44k | - | out (clean 28, ADX 23, RVol 0.4) |
| 27 | **CRM** | 240.87 | - | **-** | 5 | - | POS +$5.3M | 235.63 | 260 | 240 | +$31k | - | out (clean 26, ADX 14, RVol 0.7) |

## Big prints this scan (104)
- **SPY** PUT 775 2026-11-02 (5DTE): 840 @ 6.70 = **+$563k** BUY | vol 7,241 / OI 137
- **GOOGL** CALL 315 2026-10-30 (2DTE): 296 @ 15.46 = **+$458k** BUY | vol 1,119 / OI 1,049
- **META** CALL 625 2026-10-30 (2DTE): 1,118 @ 4.00 = **+$447k** BUY | vol 8,184 / OI 131
- **GOOGL** CALL 317.5 2026-10-30 (2DTE): 296 @ 13.94 = **+$413k** BUY | vol 882 / OI 917
- **AAPL** PUT 357.5 2026-10-30 (2DTE): 250 @ 13.11 = **+$328k** MID | vol 2,093 / OI 1,973
- **QQQ** CALL 709 2026-10-29 (1DTE): 200 @ 14.70 = **+$294k** BUY | vol 447 / OI 223
- **QQQ** CALL 710 2026-10-29 (1DTE): 200 @ 13.81 = **+$276k** MID | vol 377 / OI 439
- **GOOGL** CALL 315 2026-10-30 (2DTE): 118 @ 15.46 = **+$182k** BUY | vol 1,119 / OI 1,049
- **GOOGL** CALL 315 2026-10-30 (2DTE): 118 @ 15.46 = **+$182k** BUY | vol 1,119 / OI 1,049
- **GOOGL** CALL 317.5 2026-10-30 (2DTE): 118 @ 13.94 = **+$164k** BUY | vol 882 / OI 917
- **GOOGL** CALL 317.5 2026-10-30 (2DTE): 118 @ 13.94 = **+$164k** BUY | vol 882 / OI 917
- **MU** PUT 975 2026-10-30 (2DTE): 86 @ 19.05 = **+$164k** BUY | vol 4,343 / OI 305
- **AAPL** PUT 357.5 2026-10-30 (2DTE): 126 @ 12.81 = **+$161k** SELL | vol 2,093 / OI 1,973
- **QQQ** PUT 720 2026-10-28 (0DTE): 1,137 @ 1.30 = **+$148k** BUY | vol 145,025 / OI 2,738
- **SPY** PUT 780 2026-10-30 (2DTE): 140 @ 10.41 = **+$146k** BUY | vol 1,802 / OI 3,391

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 775 2026-10-30 (2DTE): 12,529 traded vs OI 11,957
- **SPY** PUT 773 2026-11-02 (5DTE): 502 traded vs OI 158
- **QQQ** CALL 739 2026-10-30 (2DTE): 900 traded vs OI 868
- **QQQ** CALL 722 2026-11-04 (7DTE): 508 traded vs OI 141
- **IWM** CALL 282 2026-11-02 (5DTE): 750 traded vs OI 684
- **IWM** CALL 278 2026-10-29 (1DTE): 529 traded vs OI 310
- **NVDA** PUT 215 2026-11-09 (12DTE): 528 traded vs OI 66
- **AAPL** CALL 320 2026-10-30 (2DTE): 1,006 traded vs OI 806
- **AAPL** PUT 357.5 2026-10-30 (2DTE): 2,093 traded vs OI 1,973
- **META** CALL 580 2026-10-30 (2DTE): 525 traded vs OI 23
- **MSFT** PUT 507.5 2026-10-30 (2DTE): 1,126 traded vs OI 1,081
- **MSFT** PUT 487.5 2026-11-02 (5DTE): 534 traded vs OI 26
- **GOOGL** CALL 315 2026-10-30 (2DTE): 1,119 traded vs OI 1,049
- **MU** CALL 1,010 2026-11-02 (5DTE): 500 traded vs OI 63
- **ORCL** CALL 147 2026-11-06 (9DTE): 565 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
