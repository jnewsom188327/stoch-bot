# GEX + FLOW SCAN - Fri Nov 13, 09:45 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (2)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 09:45 | **UBER** | **CALLS** | TREND + FLOW | 11/13 70C | 0.59 | 0.53 | -10% (0m) | **-10%** | +32% | 70.7 |
| 09:45 | **ORCL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/13 127C | 0.46 | 0.37 | -20% (0m) | **-20%** | +48% | 126.38 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 09:45:08 ET, last candle SPY 09:44, QQQ 09:44 | no errors

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **IWM** | 277.65 | TREND (flow not with it) | **PUTS** | 63 | 11/13 276P @ 0.49 (delta 0.28) = est +96% at 276 | NEG -$2.2B | 283.24 | 285 | 275 | +$1.3M | - | SHORT (clean 35, ADX 45, RVol 3.0) |
| 2 | **HOOD** | 78.64 | TREND (flow not with it) | **PUTS** | 61 | 11/13 78P @ 0.60 (delta 0.38) = est +63% at 77.42 | NEG -$6.1M | 79.5 | 81 | 80 | +$52k | - | SHORT (clean 35, ADX 44, RVol 4.4) |
| 3 | **TSLA** | 392.95 | FLOW SURGE | **CALLS** | 58 | none: 124 calls 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (59 contracts' greeks worked out here) | POS +$449.2M | - | 400 | 380 | +$4.5M | +$189k bull / +$0 bear | out (clean 30, ADX 37, RVol 6.0) |
| 4 | **MSFT** | 519.91 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 57 | none: 162 calls 0-7DTE > 10 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (89 contracts' greeks worked out here) | POS +$10.8M | 519.89 | 535 | 520 | -$1.7M | - | out (clean 32, ADX 47, RVol 2.1) |
| 5 | **META** | 633.53 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 55 | none: 185 calls 0-7DTE > 9 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (104 contracts' greeks worked out here) | POS +$33.9M | 631.82 | 650 | 635 | -$1.4M | - | out (clean 29, ADX 36, RVol 2.1) |
| 6 | **ORCL** | 125.02 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 54 | 11/13 127C @ 0.46 (delta 0.25) = est +48% at 126.38 | POS +$4.9M | 124.36 | 130 | 125 | +$44k | - | out (clean 31, ADX 24, RVol 2.1) |
| 7 | **AMD** | 551.66 | FLOW SURGE | **CALLS** | 52 | none: 175 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (80 contracts' greeks worked out here) | POS +$171.4M | - | 550 | 550 | +$4.7M | +$48k bull / +$0 bear | out (clean 35, ADX 24, RVol 2.0) |
| 8 | **AAPL** | 359.94 | PINNED between the walls (positive gamma) - chop | **-** | 51 | - | POS +$1.3B | 345.82 | 360 | 360 | -$3.5M | - | out (clean 30, ADX 36, RVol 2.5) |
| 9 | **UBER** | 70.25 | TREND + FLOW | **CALLS** | 50 | 11/13 70C @ 0.59 (delta 0.60) = est +32% at 70.7 | POS +$23.5M | 68.89 | 70 | 70 | +$2k | - | LONG (clean 33, ADX 32, RVol 3.0) |
| 10 | **NVDA** | 162.55 | FLOW SURGE | **CALLS** | 49 | none: 60 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (26 contracts' greeks worked out here) | NEG -$240.9M | - | 175 | 160 | +$7.9M | +$36k bull / +$0 bear | out (clean 31, ADX 16, RVol 1.7) |
| 11 | **QQQ** | 684.33 | - | **-** | 29 | - | NEG -$2.0B | 691.3 | 700 | 680 | +$11.3M | - | out (clean 31, ADX 35, RVol 2.6) |
| 12 | **NFLX** | 63.79 | - | **-** | 29 | - | NEG -$2.0M | 63.85 | 65 | 65 | -$18k | - | out (clean 31, ADX 50, RVol 3.3) |
| 13 | **AVGO** | 348.48 | - | **-** | 29 | - | POS +$111.4M | - | 350 | 340 | +$2.1M | - | out (clean 34, ADX 23, RVol 2.9) |
| 14 | **SMCI** | 26.66 | - | **-** | 29 | - | NEG -$2.1M | 28.19 | 27 | 25 | +$11k | - | out (clean 34, ADX 22, RVol 3.0) |
| 15 | **SHOP** | 149.50 | - | **-** | 29 | - | POS +$6.0M | 145.88 | 150 | 150 | -$6k | - | out (clean 32, ADX 30, RVol 1.8) |
| 16 | **BABA** | 94.37 | - | **-** | 29 | - | NEG -$20.2M | - | 100 | 95 | -$48k | - | out (clean 28, ADX 21, RVol 5.5) |
| 17 | **SMH** | 491.58 | - | **-** | 28 | - | NEG -$224.8M | - | 500 | 475 | +$687k | - | out (clean 30, ADX 29, RVol 1.4) |
| 18 | **GOOGL** | 302.71 | - | **-** | 27 | - | POS +$243.8M | 289.05 | 300 | 290 | +$1.1M | - | out (clean 30, ADX 32, RVol 3.4) |
| 19 | **DELL** | 358.25 | - | **-** | 27 | - | NEG -$8.1M | 373.31 | 360 | 360 | +$28k | - | out (clean 37, ADX 22, RVol 1.6) |
| 20 | **CRM** | 217.69 | - | **-** | 27 | - | NEG -$7.2M | 222.79 | 220 | 220 | +$11k | - | out (clean 30, ADX 27, RVol 3.0) |
| 21 | **SPY** | 756.00 | - | **-** | 26 | - | NEG -$6.0B | 761.95 | 775 | 760 | +$15.5M | - | out (clean 32, ADX 33, RVol 2.0) |
| 22 | **MSTR** | 111.63 | - | **-** | 25 | - | NEG -$34.0M | - | 120 | 110 | -$112k | - | out (clean 29, ADX 29, RVol 4.3) |
| 23 | **PLTR** | 169.56 | - | **-** | 24 | - | POS +$98.8M | - | 170 | 170 | +$83k | - | out (clean 29, ADX 24, RVol 2.1) |
| 24 | **ARM** | 192.91 | - | **-** | 24 | - | POS +$4.2M | 190 | 200 | 190 | -$105k | - | out (clean 32, ADX 31, RVol 1.7) |
| 25 | **AMZN** | 268.74 | - | **-** | 21 | - | POS +$565.1M | - | 270 | 270 | +$194k | - | out (clean 30, ADX 36, RVol 2.1) |
| 26 | **COIN** | 129.84 | - | **-** | 21 | - | NEG -$10.8M | 132.05 | 137 | 130 | -$152k | - | out (clean 30, ADX 36, RVol 2.9) |
| 27 | **MU** | 781.97 | - | **-** | 18 | - | POS +$4.1M | 779.93 | 800 | 800 | -$2.9M | - | out (clean 30, ADX 17, RVol 2.0) |

## Big prints this scan (0)

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 759 2026-11-13 (0DTE): 6,877 traded vs OI 3,639
- **SPY** CALL 773 2026-11-16 (3DTE): 10,791 traded vs OI 939
- **SPY** CALL 763 2026-11-13 (0DTE): 5,247 traded vs OI 5,036
- **QQQ** CALL 688 2026-11-13 (0DTE): 2,933 traded vs OI 1,067
- **QQQ** PUT 687 2026-11-13 (0DTE): 1,732 traded vs OI 1,621
- **QQQ** PUT 689 2026-11-13 (0DTE): 1,631 traded vs OI 1,384
- **QQQ** CALL 701 2026-11-13 (0DTE): 1,251 traded vs OI 1,109
- **QQQ** PUT 684 2026-11-13 (0DTE): 1,288 traded vs OI 1,105
- **QQQ** CALL 707 2026-11-16 (3DTE): 3,218 traded vs OI 199
- **QQQ** CALL 694 2026-11-13 (0DTE): 2,203 traded vs OI 1,416
- **NVDA** CALL 170 2026-11-13 (0DTE): 10,353 traded vs OI 9,217
- **TSLA** PUT 397.5 2026-11-13 (0DTE): 902 traded vs OI 374
- **AAPL** CALL 362.5 2026-11-16 (3DTE): 512 traded vs OI 327
- **AMD** CALL 590 2026-11-16 (3DTE): 1,521 traded vs OI 332
- **AMD** PUT 565 2026-11-13 (0DTE): 646 traded vs OI 303

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
