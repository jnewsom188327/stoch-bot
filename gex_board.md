# GEX + FLOW SCAN - Tue Nov 10, 09:45 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (1)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 09:45 | **IWM** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/10 279P | 0.52 | 0.51 | -2% (0m) | **-2%** | +87% | 278.66 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 09:45:08 ET, last candle SPY 09:44, QQQ 09:44 | no errors

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **IWM** | 280.02 | RUN: clean trend + negative gamma + flow agrees | **PUTS** | 79 | 11/10 279P @ 0.52 (delta 0.33) = est +87% at 278.66 | NEG -$987.9M | 284.31 | 285 | 270 | -$916k | - | SHORT (clean 36, ADX 45, RVol 3.8) |
| 2 | **TSLA** | 376.03 | TREND + FLOW | **PUTS** | 53 | none: 90 puts 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (6 contracts' greeks worked out here) | POS +$184.9M | - | 400 | 380 | -$1.7M | - | SHORT (clean 34, ADX 43, RVol 2.0) |
| 3 | **UBER** | 70.06 | PINNED between the walls (positive gamma) - chop | **-** | 52 | - | POS +$8.4M | 68.36 | 70 | 70 | +$2k | - | out (clean 32, ADX 36, RVol 2.2) |
| 4 | **GOOGL** | 289.44 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 47 | none: 69 calls 0-7DTE > 8 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (8 contracts' greeks worked out here) | POS +$4.2M | 288.86 | 300 | 290 | -$100k | - | out (clean 30, ADX 20, RVol 2.9) |
| 5 | **PLTR** | 168.88 | - | **-** | 30 | - | POS +$51.3M | - | 165 | 170 | -$82k | - | out (clean 29, ADX 33, RVol 1.9) |
| 6 | **SMH** | 483.45 | - | **-** | 29 | - | NEG -$212.2M | - | 500 | 475 | -$190k | - | out (clean 29, ADX 30, RVol 1.8) |
| 7 | **ARM** | 181.89 | - | **-** | 29 | - | NEG -$4.7M | - | 185 | 190 | -$11k | - | out (clean 27, ADX 27, RVol 1.9) |
| 8 | **CRM** | 213.72 | - | **-** | 29 | - | NEG -$10.2M | - | 195 | 220 | -$2k | - | out (clean 31, ADX 23, RVol 3.1) |
| 9 | **NVDA** | 172.03 | - | **-** | 28 | - | NEG -$175.6M | - | 185 | 180 | +$7.4M | - | out (clean 32, ADX 26, RVol 2.8) |
| 10 | **AAPL** | 350.98 | - | **-** | 28 | - | POS +$515.4M | 335.44 | 350 | 340 | +$1.5M | - | out (clean 28, ADX 24, RVol 2.1) |
| 11 | **AMD** | 518.60 | - | **-** | 28 | - | POS +$42.9M | - | 500 | 500 | -$3.2M | - | out (clean 30, ADX 33, RVol 2.3) |
| 12 | **HOOD** | 82.25 | - | **-** | 27 | - | POS +$4.0M | 78.8 | 85 | 80 | -$50k | - | out (clean 30, ADX 28, RVol 2.3) |
| 13 | **SHOP** | 150.43 | - | **-** | 26 | - | POS +$3.3M | - | 155 | 140 | +$2k | - | out (clean 32, ADX 33, RVol 1.5) |
| 14 | **QQQ** | 675.25 | - | **-** | 25 | - | NEG -$1.9B | 692.6 | 680 | 680 | -$13.7M | - | out (clean 31, ADX 34, RVol 2.5) |
| 15 | **SPY** | 749.25 | - | **-** | 24 | - | NEG -$7.1B | 761.43 | 750 | 730 | -$14.8M | - | out (clean 32, ADX 35, RVol 2.9) |
| 16 | **NFLX** | 62.92 | - | **-** | 24 | - | NEG -$22.2M | 65.58 | 65 | 60 | +$10k | - | out (clean 29, ADX 27, RVol 2.6) |
| 17 | **COIN** | 134.39 | - | **-** | 23 | - | POS +$9.4M | - | 141 | 135 | -$12k | - | out (clean 32, ADX 23, RVol 2.3) |
| 18 | **AMZN** | 271.07 | - | **-** | 22 | - | POS +$462.9M | - | 270 | 265 | -$237k | - | out (clean 32, ADX 24, RVol 2.4) |
| 19 | **MU** | 718.50 | - | **-** | 22 | - | NEG -$28.0M | - | 750 | 750 | -$1.3M | - | out (clean 30, ADX 29, RVol 2.0) |
| 20 | **ORCL** | 118.69 | - | **-** | 20 | - | NEG -$24.1M | - | 130 | 120 | +$29k | - | out (clean 29, ADX 37, RVol 1.1) |
| 21 | **SMCI** | 28.09 | - | **-** | 19 | - | POS +$3.2M | - | 30 | 30 | -$7k | - | out (clean 29, ADX 26, RVol 2.0) |
| 22 | **MSTR** | 123.74 | - | **-** | 18 | - | POS +$6.5M | 120.15 | 133 | 120 | -$58k | - | out (clean 31, ADX 25, RVol 1.8) |
| 23 | **AVGO** | 324.59 | - | **-** | 17 | - | NEG -$20.6M | 342.49 | 340 | 320 | +$375k | - | out (clean 31, ADX 28, RVol 3.4) |
| 24 | **META** | 641.23 | - | **-** | 13 | - | POS +$244.2M | 604.23 | 650 | 650 | +$58k | - | out (clean 33, ADX 37, RVol 2.2) |
| 25 | **MSFT** | 543.33 | - | **-** | 11 | - | POS +$667.2M | - | 550 | 535 | -$18k | - | out (clean 33, ADX 38, RVol 1.7) |
| 26 | **DELL** | 336.29 | - | **-** | 10 | - | NEG -$7.9M | - | 350 | 340 | +$0 | - | out (clean 33, ADX 29, RVol 2.3) |
| 27 | **BABA** | 104.67 | - | **-** | 10 | - | NEG -$2.7M | 105.34 | 110 | 105 | +$0 | - | out (clean 30, ADX 26, RVol 3.0) |

## Big prints this scan (0)

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 728 2026-11-10 (0DTE): 674 traded vs OI 533
- **SPY** PUT 737 2026-11-10 (0DTE): 1,278 traded vs OI 573
- **SPY** PUT 748 2026-11-11 (1DTE): 704 traded vs OI 442
- **SPY** CALL 756 2026-11-10 (0DTE): 2,139 traded vs OI 818
- **SPY** PUT 751 2026-11-10 (0DTE): 1,404 traded vs OI 512
- **SPY** PUT 751 2026-11-11 (1DTE): 569 traded vs OI 282
- **SPY** CALL 754 2026-11-10 (0DTE): 3,143 traded vs OI 1,400
- **SPY** PUT 740 2026-11-10 (0DTE): 9,901 traded vs OI 1,258
- **SPY** PUT 738 2026-11-10 (0DTE): 2,019 traded vs OI 623
- **SPY** PUT 745 2026-11-10 (0DTE): 7,335 traded vs OI 1,663
- **SPY** PUT 748 2026-11-10 (0DTE): 7,667 traded vs OI 832
- **SPY** PUT 736 2026-11-10 (0DTE): 1,474 traded vs OI 1,197
- **SPY** PUT 741 2026-11-10 (0DTE): 1,456 traded vs OI 336
- **SPY** CALL 749 2026-11-11 (1DTE): 655 traded vs OI 446
- **SPY** CALL 759 2026-11-10 (0DTE): 1,078 traded vs OI 1,015

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
