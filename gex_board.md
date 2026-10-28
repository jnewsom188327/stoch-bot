# GEX + FLOW SCAN - Wed Oct 28, 02:40 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (8)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 14:35 | **QQQ** | **CALLS** | 1m WHIPSAW (R1 R2) | 10/28 730C | 0.67 | 0.56 | +64% (2m) | **-16%** | -70% | 724.9 |
| 14:35 | **SPY** | **CALLS** | 1m WHIPSAW (R1 R2 R5 R6) | 10/29 778C | 0.75 | 0.68 | +43% (2m) | **-9%** | +27% | 772.74 |
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
| 1 | **ORCL** | 143.95 | FLOW SURGE | **PUTS** | 55 | none: 24 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (2 contracts' greeks worked out here) | POS +$35.3M | - | 135 | 140 | -$9.4M | +$0 bull / -$864k bear | out (clean 30, ADX 35, RVol 10.0) |
| 2 | **AAPL** | 344.76 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 36 | 10/28 345C @ 0.59 (delta 0.45) = est -69% at 345 | POS +$307.7M | 341.49 | 350 | 345 | +$1.2M | +$0 bull / -$439k bear | out (clean 28, ADX 14, RVol 1.1) |
| 3 | **AVGO** | 350.24 | PINNED between the walls (positive gamma) - chop | **-** | 33 | - | POS +$68.3M | 337.27 | 350 | 350 | -$498k | +$0 bull / -$164k bear | out (clean 29, ADX 31, RVol 0.9) |
| 4 | **SMH** | 568.00 | - | **-** | 23 | - | POS +$113.6M | 557.36 | 580 | 555 | -$3.8M | +$0 bull / -$60k bear | out (clean 28, ADX 18, RVol 1.2) |
| 5 | **AMD** | 574.47 | - | **-** | 20 | - | POS +$186.5M | - | 600 | 550 | +$3.5M | +$0 bull / -$454k bear | out (clean 29, ADX 32, RVol 1.4) |
| 6 | **META** | 611.88 | - | **-** | 20 | - | NEG -$261.9M | 632.94 | 650 | 610 | +$9.0M | +$53k bull / -$1.1M bear | out (clean 29, ADX 26, RVol 1.2) |
| 7 | **PLTR** | 194.25 | - | **-** | 19 | - | POS +$43.8M | 189.63 | 200 | 190 | +$238k | +$0 bull / -$125k bear | out (clean 27, ADX 34, RVol 0.9) |
| 8 | **NVDA** | 217.24 | - | **-** | 17 | - | POS +$549.0M | 210.2 | 220 | 215 | +$7.4M | +$0 bull / -$265k bear | out (clean 26, ADX 16, RVol 0.9) |
| 9 | **TSLA** | 403.47 | - | **-** | 17 | - | POS +$632.4M | - | 400 | 400 | -$18.7M | +$0 bull / -$425k bear | out (clean 29, ADX 20, RVol 0.6) |
| 10 | **MSFT** | 528.83 | - | **-** | 17 | - | POS +$464.7M | - | 550 | 500 | -$1.4M | +$0 bull / -$1.1M bear | out (clean 29, ADX 18, RVol 1.5) |
| 11 | **GOOGL** | 324.72 | - | **-** | 17 | - | POS +$16.9M | 320.89 | 355 | 330 | -$526k | +$0 bull / -$252k bear | out (clean 32, ADX 20, RVol 1.8) |
| 12 | **MSTR** | 141.31 | - | **-** | 17 | - | POS +$21.1M | - | 152.5 | 150 | +$506k | +$0 bull / -$30k bear | out (clean 27, ADX 19, RVol 1.0) |
| 13 | **SPY** | 771.81 | - | **-** | 16 | - | NEG -$1.3B | 773.25 | 780 | 750 | -$2.5M | +$0 bull / -$853k bear | out (clean 29, ADX 16, RVol 1.4) |
| 14 | **QQQ** | 723.95 | - | **-** | 16 | - | NEG -$1.1B | 727.59 | 720 | 720 | +$21.9M | +$0 bull / -$1.0M bear | out (clean 29, ADX 16, RVol 1.1) |
| 15 | **AMZN** | 253.44 | - | **-** | 16 | - | POS +$200.5M | 238.88 | 255 | 250 | +$1.5M | +$0 bull / -$945k bear | out (clean 31, ADX 20, RVol 1.0) |
| 16 | **MU** | 974.41 | - | **-** | 16 | - | POS +$626.8M | - | 950 | 950 | +$19.0M | +$0 bull / -$2.6M bear | out (clean 28, ADX 19, RVol 0.7) |
| 17 | **BABA** | 100.66 | - | **-** | 16 | - | NEG -$12.1M | 103.3 | 102 | 100 | -$6k | +$0 bull / -$48k bear | out (clean 28, ADX 21, RVol 1.1) |
| 18 | **IWM** | 280.15 | - | **-** | 12 | - | NEG -$237.2M | 281.03 | 280 | 270 | +$9.2M | - | out (clean 25, ADX 29, RVol 0.9) |
| 19 | **HOOD** | 91.24 | - | **-** | 12 | - | NEG -$17.8M | - | 100 | 90 | +$4.0M | - | out (clean 30, ADX 16, RVol 0.9) |
| 20 | **SHOP** | 168.06 | - | **-** | 12 | - | NEG -$3.5M | 171.72 | 175 | 165 | -$28k | - | out (clean 29, ADX 22, RVol 1.6) |
| 21 | **SMCI** | 35.26 | - | **-** | 9 | - | POS +$21.1M | - | 35 | 35 | +$117k | - | out (clean 27, ADX 24, RVol 0.7) |
| 22 | **UBER** | 65.41 | - | **-** | 8 | - | NEG -$29.5M | 68.83 | 70 | 65 | +$43k | - | out (clean 30, ADX 21, RVol 1.5) |
| 23 | **NFLX** | 61.70 | - | **-** | 5 | - | NEG -$58.8M | - | 64 | 60 | -$93k | - | out (clean 31, ADX 15, RVol 0.8) |
| 24 | **COIN** | 159.97 | - | **-** | 5 | - | POS +$2.5M | 155.01 | 170 | 150 | +$23k | - | out (clean 28, ADX 13, RVol 0.9) |
| 25 | **ARM** | 235.37 | - | **-** | 5 | - | POS +$2.2M | - | 250 | 250 | +$6k | - | out (clean 26, ADX 17, RVol 1.1) |
| 26 | **DELL** | 496.74 | - | **-** | 4 | - | POS +$34.3M | - | 500 | 500 | +$48k | - | out (clean 30, ADX 14, RVol 0.6) |
| 27 | **CRM** | 241.39 | - | **-** | 4 | - | POS +$6.3M | 235.06 | 260 | 240 | +$8k | - | out (clean 26, ADX 15, RVol 0.4) |

## Big prints this scan (68)
- **MSFT** CALL 535 2026-10-30 (2DTE): 1,000 @ 9.29 = **+$929k** SELL | vol 2,780 / OI 2,133
- **MU** CALL 970 2026-10-30 (2DTE): 100 @ 18.50 = **+$185k** SELL | vol 8,007 / OI 1,990
- **META** PUT 600 2026-10-30 (2DTE): 363 @ 4.65 = **+$169k** BUY | vol 8,090 / OI 3,579
- **ORCL** CALL 140 2026-10-30 (2DTE): 500 @ 2.45 = **+$122k** SELL | vol 12,550 / OI 14,861
- **QQQ** PUT 721 2026-10-30 (2DTE): 200 @ 5.90 = **+$118k** BUY | vol 3,585 / OI 1,287
- **AMZN** CALL 250 2026-10-30 (2DTE): 100 @ 11.24 = **+$112k** SELL | vol 3,506 / OI 7,101
- **AAPL** PUT 345 2026-10-30 (2DTE): 360 @ 3.11 = **+$112k** BUY | vol 10,906 / OI 9,983
- **MU** CALL 930 2026-10-28 (0DTE): 27 @ 36.98 = **+$100k** SELL | vol 1,127 / OI 714
- **ORCL** CALL 140 2026-10-30 (2DTE): 300 @ 3.00 = **+$90k** SELL | vol 12,550 / OI 14,861
- **ORCL** CALL 140 2026-10-30 (2DTE): 250 @ 2.72 = **+$68k** SELL | vol 12,550 / OI 14,861
- **ORCL** CALL 140 2026-10-30 (2DTE): 250 @ 2.72 = **+$68k** SELL | vol 12,550 / OI 14,861
- **ORCL** PUT 150 2026-10-30 (2DTE): 41 @ 14.98 = **+$61k** BUY | vol 133 / OI 0
- **AMZN** CALL 250 2026-10-30 (2DTE): 54 @ 11.24 = **+$61k** SELL | vol 3,506 / OI 7,101
- **META** CALL 605 2026-10-28 (0DTE): 100 @ 6.05 = **+$60k** SELL | vol 458 / OI 20
- **PLTR** PUT 195 2026-10-30 (2DTE): 150 @ 4.00 = **+$60k** BUY | vol 7,189 / OI 2,664

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 767 2026-11-02 (5DTE): 500 traded vs OI 402
- **QQQ** CALL 728 2026-11-06 (9DTE): 505 traded vs OI 223
- **QQQ** CALL 750 2026-11-05 (8DTE): 508 traded vs OI 140
- **IWM** CALL 283 2026-10-30 (2DTE): 18,139 traded vs OI 4,625
- **IWM** CALL 284 2026-10-30 (2DTE): 32,916 traded vs OI 18,022
- **IWM** CALL 285 2026-11-03 (6DTE): 535 traded vs OI 142
- **SMH** CALL 610 2026-11-27 (30DTE): 501 traded vs OI 97
- **NVDA** PUT 217.5 2026-11-04 (7DTE): 502 traded vs OI 95
- **TSLA** CALL 420 2026-10-30 (2DTE): 18,224 traded vs OI 18,044
- **AMD** PUT 572.5 2026-10-30 (2DTE): 534 traded vs OI 64
- **AMD** CALL 580 2026-11-02 (5DTE): 502 traded vs OI 404
- **META** PUT 607.5 2026-10-30 (2DTE): 506 traded vs OI 260
- **MSFT** CALL 535 2026-10-30 (2DTE): 2,780 traded vs OI 2,133
- **MU** CALL 1,050 2026-11-06 (9DTE): 989 traded vs OI 988
- **MSTR** CALL 155 2026-10-30 (2DTE): 3,337 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
