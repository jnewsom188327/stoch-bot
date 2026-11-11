# GEX + FLOW SCAN - Wed Nov 11, 09:40 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (2)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 09:39 | **QQQ** | **CALLS** | 1m WHIPSAW (R1 R5) | 11/11 693C | 0.52 | 0.43 | -10% (0m) | **-17%** | +92% | 690.43 |
| 09:39 | **SPY** | **CALLS** | 1m WHIPSAW (R1 R5) | 11/11 760C | 0.53 | 0.47 | -2% (0m) | **-11%** | +79% | 758.82 |

## 1m RULES on SPY / QQQ - loose (2 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 09:40:08 ET, last candle SPY 09:39, QQQ 09:39 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 09:38 | QQQ | 1m WHIPSAW | R1 R5 | CALLS | TURNING away | **FIRE** QQQ261111C00693000 |
| 09:38 | SPY | 1m WHIPSAW | R1 R5 | CALLS | TURNING away | **FIRE** SPY261111C00760000 |

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **AVGO** | 351.96 | TREND (flow not with it) | **CALLS** | 42 | none: 112 calls 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (46 contracts' greeks worked out here) | POS +$90.0M | - | 350 | 350 | +$0 | - | LONG (clean 34, ADX 38, RVol 3.2) |
| 2 | **DELL** | 363.40 | TREND (flow not with it) | **CALLS** | 35 | none: 29 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$2.8M | - | 350 | 340 | +$0 | - | LONG (clean 34, ADX 31, RVol 2.1) |
| 3 | **IWM** | 282.01 | TREND (flow not with it) | **CALLS** | 32 | 11/11 282C @ 0.78 (delta 0.51) = est +55% at 282.93 | NEG -$327.9M | 282.93 | 285 | 270 | +$0 | - | LONG (clean 34, ADX 27, RVol 1.9) |
| 4 | **MSTR** | 123.20 | FLIP CROSS up into positive gamma | **CALLS** | 31 | none: 25 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$3.7M | 121.39 | 133 | 120 | +$0 | - | out (clean 29, ADX 16, RVol 2.6) |
| 5 | **UBER** | 69.86 | PINNED between the walls (positive gamma) - chop | **-** | 30 | - | POS +$10.0M | 68.25 | 70 | 70 | +$0 | - | out (clean 34, ADX 25, RVol 2.2) |
| 6 | **MU** | 773.18 | - | **-** | 21 | - | POS +$135.3M | - | 800 | 750 | +$0 | +$60k bull / +$0 bear | out (clean 31, ADX 34, RVol 2.3) |
| 7 | **QQQ** | 687.32 | - | **-** | 20 | - | NEG -$537.1M | 689.92 | 700 | 680 | +$0 | +$115k bull / +$0 bear | out (clean 33, ADX 39, RVol 1.6) |
| 8 | **SPY** | 756.76 | - | **-** | 11 | - | NEG -$3.6B | 761.22 | 760 | 750 | +$0 | - | out (clean 32, ADX 40, RVol 2.1) |
| 9 | **META** | 644.52 | - | **-** | 11 | - | POS +$311.5M | 624.85 | 650 | 625 | +$0 | - | out (clean 31, ADX 36, RVol 2.1) |
| 10 | **AMZN** | 271.52 | - | **-** | 11 | - | POS +$554.4M | - | 270 | 265 | +$0 | - | out (clean 34, ADX 37, RVol 2.1) |
| 11 | **PLTR** | 174.68 | - | **-** | 11 | - | POS +$75.7M | - | 170 | 180 | +$0 | - | out (clean 29, ADX 38, RVol 2.0) |
| 12 | **ARM** | 190.34 | - | **-** | 11 | - | POS +$350k | 189.57 | 200 | 200 | +$0 | - | out (clean 27, ADX 42, RVol 1.8) |
| 13 | **SHOP** | 148.50 | - | **-** | 10 | - | POS +$1.6M | 145.08 | 150 | 140 | +$0 | - | out (clean 32, ADX 38, RVol 1.8) |
| 14 | **AAPL** | 352.33 | - | **-** | 9 | - | POS +$1.1B | 340.4 | 355 | 350 | +$0 | - | out (clean 28, ADX 27, RVol 2.0) |
| 15 | **AMD** | 528.53 | - | **-** | 9 | - | POS +$123.2M | - | 500 | 500 | +$0 | - | out (clean 33, ADX 24, RVol 2.4) |
| 16 | **GOOGL** | 290.92 | - | **-** | 9 | - | POS +$34.5M | 288.7 | 300 | 290 | +$0 | - | out (clean 29, ADX 30, RVol 1.8) |
| 17 | **HOOD** | 83.28 | - | **-** | 9 | - | POS +$9.5M | 78.65 | 85 | 80 | +$0 | - | out (clean 32, ADX 24, RVol 2.6) |
| 18 | **CRM** | 213.91 | - | **-** | 9 | - | NEG -$11.6M | - | 195 | 220 | +$0 | - | out (clean 31, ADX 25, RVol 3.5) |
| 19 | **SMH** | 502.30 | - | **-** | 8 | - | NEG -$75.6M | - | 500 | 475 | +$0 | - | out (clean 30, ADX 25, RVol 1.8) |
| 20 | **TSLA** | 390.48 | - | **-** | 8 | - | POS +$355.3M | - | 400 | 380 | +$0 | - | out (clean 32, ADX 23, RVol 1.9) |
| 21 | **NFLX** | 63.67 | - | **-** | 8 | - | NEG -$12.8M | 64.72 | 65 | 65 | +$0 | - | out (clean 28, ADX 22, RVol 2.0) |
| 22 | **COIN** | 136.00 | - | **-** | 8 | - | POS +$19.1M | - | 141 | 135 | +$0 | - | out (clean 28, ADX 26, RVol 1.5) |
| 23 | **SMCI** | 29.70 | - | **-** | 8 | - | POS +$9.7M | - | 30 | 30 | +$0 | - | out (clean 31, ADX 25, RVol 1.9) |
| 24 | **ORCL** | 126.48 | - | **-** | 8 | - | NEG -$2.0M | 128.92 | 130 | 125 | +$0 | - | out (clean 27, ADX 26, RVol 1.4) |
| 25 | **BABA** | 102.11 | - | **-** | 8 | - | NEG -$14.3M | 106.17 | 110 | 101 | +$0 | - | out (clean 30, ADX 20, RVol 2.1) |
| 26 | **NVDA** | 174.57 | - | **-** | 7 | - | NEG -$168.0M | - | 180 | 175 | +$0 | - | out (clean 34, ADX 21, RVol 1.8) |
| 27 | **MSFT** | 532.64 | - | **-** | 7 | - | POS +$393.3M | 512.26 | 550 | 535 | +$0 | - | out (clean 32, ADX 16, RVol 2.0) |

## Big prints this scan (0)

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
