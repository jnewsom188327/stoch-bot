# GEX + FLOW SCAN - Thu Nov 05, 09:40 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (1)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 09:40 | **QQQ** | **CALLS** | 1m WHIPSAW (R1) | 11/05 683C | 0.78 | 0.75 | -4% (0m) | **-4%** | +66% | 678.43 |

## 1m RULES on SPY / QQQ - loose (1 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 09:40:08 ET, last candle SPY 09:39, QQQ 09:39 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 09:39 | QQQ | 1m WHIPSAW | R1 | CALLS | AGAINST you | **FIRE** QQQ261105C00683000 |

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **BABA** | 107.77 | TREND (flow not with it) | **CALLS** | 43 | 11/06 110C @ 0.74 (delta 0.30) = est +107% at 110 | POS +$23.0M | - | 110 | 110 | +$0 | - | LONG (clean 37, ADX 37, RVol 6.0) |
| 2 | **SMCI** | 27.76 | TREND (flow not with it) | **PUTS** | 40 | 11/06 27P @ 0.57 (delta 0.37) = est +44% at 27.04 | NEG -$4.3M | - | 30 | 30 | +$0 | - | SHORT (clean 34, ADX 29, RVol 3.6) |
| 3 | **SHOP** | 145.83 | TREND (flow not with it) | **PUTS** | 39 | none: 23 puts 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (6 contracts' greeks worked out here) | NEG -$4.8M | - | 144 | 145 | +$0 | - | SHORT (clean 34, ADX 33, RVol 2.7) |
| 4 | **AMZN** | 269.66 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 38 | none: 63 puts 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (31 contracts' greeks worked out here) | POS +$530.7M | - | 270 | 250 | +$0 | - | out (clean 35, ADX 18, RVol 3.7) |
| 5 | **HOOD** | 82.69 | FLIP CROSS down into negative gamma | **PUTS** | 25 | 11/06 79P @ 0.73 (delta 0.24) = est +104% at 80 | NEG -$4.7M | 85.57 | 86 | 80 | +$0 | - | out (clean 29, ADX 24, RVol 1.6) |
| 6 | **AMD** | 439.25 | - | **-** | 19 | - | NEG -$144.3M | - | 430 | 440 | +$0 | +$26k bull / +$0 bear | out (clean 31, ADX 20, RVol 3.0) |
| 7 | **NVDA** | 192.39 | - | **-** | 12 | - | NEG -$305.7M | - | 210 | 190 | +$0 | - | out (clean 30, ADX 41, RVol 4.6) |
| 8 | **MU** | 741.83 | - | **-** | 12 | - | NEG -$221.5M | - | 800 | 800 | +$0 | - | out (clean 31, ADX 37, RVol 4.0) |
| 9 | **MSTR** | 136.87 | - | **-** | 12 | - | POS +$123.7M | - | 135 | 135 | +$0 | - | out (clean 32, ADX 40, RVol 2.7) |
| 10 | **TSLA** | 360.82 | - | **-** | 11 | - | NEG -$204.8M | - | 370 | 350 | +$0 | - | out (clean 32, ADX 32, RVol 4.0) |
| 11 | **NFLX** | 66.03 | - | **-** | 11 | - | POS +$30.6M | 63.12 | 65 | 65 | +$0 | - | out (clean 33, ADX 36, RVol 3.5) |
| 12 | **AVGO** | 310.23 | - | **-** | 11 | - | NEG -$142.9M | - | 340 | 300 | +$0 | - | out (clean 30, ADX 33, RVol 4.2) |
| 13 | **ARM** | 172.48 | - | **-** | 11 | - | NEG -$8.1M | - | 180 | 180 | +$0 | - | out (clean 26, ADX 36, RVol 6.4) |
| 14 | **SMH** | 477.77 | - | **-** | 10 | - | NEG -$484.8M | - | 520 | 500 | +$0 | - | out (clean 33, ADX 26, RVol 3.7) |
| 15 | **DELL** | 346.27 | - | **-** | 10 | - | NEG -$22.3M | - | 360 | 350 | +$0 | - | out (clean 33, ADX 26, RVol 4.3) |
| 16 | **ORCL** | 119.19 | - | **-** | 10 | - | NEG -$56.4M | - | 130 | 120 | +$0 | - | out (clean 33, ADX 33, RVol 2.2) |
| 17 | **UBER** | 69.19 | - | **-** | 10 | - | POS +$7.4M | 68.05 | 70 | 65 | +$0 | - | out (clean 31, ADX 25, RVol 3.6) |
| 18 | **SPY** | 760.62 | - | **-** | 9 | - | NEG -$6.9B | 769.13 | 770 | 750 | +$0 | - | out (clean 32, ADX 23, RVol 4.1) |
| 19 | **QQQ** | 675.00 | - | **-** | 9 | - | NEG -$6.8B | - | 700 | 680 | +$0 | - | out (clean 33, ADX 25, RVol 3.1) |
| 20 | **AAPL** | 353.71 | - | **-** | 9 | - | POS +$857.7M | 334.03 | 350 | 340 | +$0 | - | out (clean 32, ADX 23, RVol 4.0) |
| 21 | **MSFT** | 553.29 | - | **-** | 9 | - | POS +$1.1B | - | 550 | 535 | +$0 | - | out (clean 29, ADX 25, RVol 2.9) |
| 22 | **PLTR** | 160.18 | - | **-** | 9 | - | NEG -$49.8M | - | 165 | 160 | +$0 | - | out (clean 26, ADX 22, RVol 2.9) |
| 23 | **GOOGL** | 291.29 | - | **-** | 8 | - | POS +$81.8M | 281.41 | 290 | 290 | +$0 | - | out (clean 36, ADX 21, RVol 2.1) |
| 24 | **CRM** | 223.24 | - | **-** | 8 | - | NEG -$16.4M | - | 240 | 220 | +$0 | - | out (clean 34, ADX 17, RVol 2.9) |
| 25 | **IWM** | 282.96 | - | **-** | 7 | - | NEG -$717.3M | 284.94 | 285 | 270 | +$0 | - | out (clean 34, ADX 12, RVol 3.2) |
| 26 | **META** | 624.06 | - | **-** | 7 | - | POS +$12.1M | 620.09 | 650 | 610 | +$0 | - | out (clean 32, ADX 19, RVol 1.6) |
| 27 | **COIN** | 147.38 | - | **-** | 5 | - | POS +$39.4M | - | 148 | 140 | +$0 | - | out (clean 31, ADX 18, RVol 1.1) |

## Big prints this scan (0)

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
