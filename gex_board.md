# GEX + FLOW SCAN - Wed Nov 11, 09:45 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (4)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 09:45 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/11 282C | 0.68 | 0.67 | -1% (0m) | **-1%** | +68% | 282.96 |
| 09:45 | **QQQ** | **CALLS** | FLOW SURGE | 11/11 690C | 0.63 | 0.62 | -2% (0m) | **-2%** | +171% | 689.78 |
| 09:39 | **QQQ** | **CALLS** | 1m WHIPSAW (R1 R5) | 11/11 693C | 0.52 | 0.26 | -10% (0m) | **-50%** | +92% | 690.43 |
| 09:39 | **SPY** | **CALLS** | 1m WHIPSAW (R1 R5) | 11/11 760C | 0.53 | 0.32 | -2% (0m) | **-40%** | +79% | 758.82 |

## 1m RULES on SPY / QQQ - loose (2 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 09:45:08 ET, last candle SPY 09:44, QQQ 09:44 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 09:38 | QQQ | 1m WHIPSAW | R1 R5 | CALLS | TURNING away | **FIRE** QQQ261111C00693000 |
| 09:38 | SPY | 1m WHIPSAW | R1 R5 | CALLS | TURNING away | **FIRE** SPY261111C00760000 |

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **DELL** | 361.40 | RUN: clean trend + negative gamma + flow agrees | **CALLS** | 72 | none: 29 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$1.3M | - | 350 | 340 | +$202k | - | LONG (clean 34, ADX 35, RVol 2.7) |
| 2 | **IWM** | 282.06 | RUN: clean trend + negative gamma + flow agrees | **CALLS** | 65 | 11/11 282C @ 0.68 (delta 0.52) = est +68% at 282.96 | NEG -$433.0M | 282.96 | 285 | 270 | +$285k | - | LONG (clean 34, ADX 29, RVol 1.9) |
| 3 | **AVGO** | 349.17 | TREND + FLOW | **CALLS** | 65 | none: 112 calls 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (49 contracts' greeks worked out here) | POS +$95.2M | - | 340 | 340 | +$2.9M | - | LONG (clean 34, ADX 40, RVol 3.4) |
| 4 | **QQQ** | 685.72 | FLOW SURGE | **CALLS** | 55 | 11/11 690C @ 0.63 (delta 0.21) = est +171% at 689.78 | NEG -$938.1M | 689.78 | 700 | 680 | +$16.7M | +$115k bull / +$0 bear | out (clean 33, ADX 40, RVol 1.6) |
| 5 | **ARM** | 189.62 | FLIP CROSS down into negative gamma | **PUTS** | 47 | none: 15 puts 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$51k | 189.78 | 200 | 200 | +$36k | - | out (clean 28, ADX 43, RVol 1.8) |
| 6 | **MU** | 778.04 | - | **-** | 42 | - | POS +$140.9M | - | 800 | 800 | -$9.7M | +$60k bull / +$0 bear | out (clean 31, ADX 37, RVol 2.5) |
| 7 | **COIN** | 135.25 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 34 | none: 27 calls 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$16.5M | - | 137 | 135 | +$1k | - | out (clean 28, ADX 29, RVol 1.6) |
| 8 | **CRM** | 213.75 | - | **-** | 30 | - | NEG -$10.3M | - | 230 | 220 | -$9k | - | out (clean 31, ADX 26, RVol 3.4) |
| 9 | **SHOP** | 148.46 | - | **-** | 30 | - | POS +$2.9M | 144.14 | 150 | 140 | +$2k | - | out (clean 32, ADX 40, RVol 1.7) |
| 10 | **HOOD** | 83.04 | - | **-** | 29 | - | POS +$8.6M | 78.71 | 85 | 80 | +$63k | - | out (clean 32, ADX 26, RVol 2.7) |
| 11 | **PLTR** | 173.16 | - | **-** | 27 | - | POS +$74.6M | - | 170 | 180 | +$501k | - | out (clean 29, ADX 41, RVol 2.1) |
| 12 | **UBER** | 69.57 | - | **-** | 27 | - | POS +$9.1M | 68.24 | 70 | 70 | -$4k | - | out (clean 34, ADX 24, RVol 2.2) |
| 13 | **SPY** | 756.11 | - | **-** | 26 | - | NEG -$4.5B | 761.25 | 760 | 750 | +$13.3M | - | out (clean 32, ADX 42, RVol 2.0) |
| 14 | **SMH** | 498.88 | - | **-** | 26 | - | NEG -$81.5M | - | 500 | 475 | +$368k | - | out (clean 30, ADX 28, RVol 2.7) |
| 15 | **TSLA** | 388.43 | - | **-** | 26 | - | POS +$355.2M | - | 400 | 380 | +$5.4M | - | out (clean 32, ADX 26, RVol 2.0) |
| 16 | **META** | 642.45 | - | **-** | 26 | - | POS +$294.0M | 624.99 | 650 | 625 | +$440k | - | out (clean 31, ADX 35, RVol 2.2) |
| 17 | **AMZN** | 269.30 | - | **-** | 26 | - | POS +$512.3M | - | 270 | 265 | +$322k | - | out (clean 34, ADX 35, RVol 2.2) |
| 18 | **GOOGL** | 290.79 | - | **-** | 25 | - | POS +$28.7M | 289.14 | 300 | 290 | -$125k | - | out (clean 29, ADX 32, RVol 1.9) |
| 19 | **ORCL** | 126.03 | - | **-** | 24 | - | NEG -$1.4M | 127.35 | 130 | 125 | +$624k | - | out (clean 27, ADX 30, RVol 2.3) |
| 20 | **NFLX** | 63.34 | - | **-** | 21 | - | NEG -$15.2M | 64.6 | 65 | 65 | -$6k | - | out (clean 28, ADX 22, RVol 2.1) |
| 21 | **AMD** | 524.83 | - | **-** | 19 | - | POS +$111.5M | - | 500 | 500 | +$2.0M | - | out (clean 33, ADX 25, RVol 2.5) |
| 22 | **SMCI** | 29.36 | - | **-** | 17 | - | POS +$9.6M | - | 30 | 30 | -$3k | - | out (clean 31, ADX 29, RVol 2.0) |
| 23 | **NVDA** | 171.83 | - | **-** | 14 | - | NEG -$178.0M | - | 180 | 170 | +$1.8M | - | out (clean 34, ADX 22, RVol 1.9) |
| 24 | **AAPL** | 353.37 | - | **-** | 14 | - | POS +$1.2B | 339.45 | 355 | 350 | -$602k | - | out (clean 28, ADX 30, RVol 2.2) |
| 25 | **MSFT** | 532.74 | - | **-** | 14 | - | POS +$352.8M | 513.79 | 550 | 520 | +$160k | - | out (clean 31, ADX 17, RVol 2.2) |
| 26 | **MSTR** | 122.30 | - | **-** | 10 | - | NEG -$819k | 121.54 | 133 | 120 | +$29k | - | out (clean 29, ADX 17, RVol 2.6) |
| 27 | **BABA** | 102.05 | - | **-** | 9 | - | NEG -$14.9M | 106.33 | 110 | 101 | +$560 | - | out (clean 30, ADX 22, RVol 2.1) |

## Big prints this scan (0)

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 754 2026-11-11 (0DTE): 2,033 traded vs OI 840
- **SPY** CALL 761 2026-11-12 (1DTE): 659 traded vs OI 646
- **SPY** PUT 745 2026-11-11 (0DTE): 1,673 traded vs OI 1,523
- **SPY** PUT 755 2026-11-11 (0DTE): 2,715 traded vs OI 1,546
- **SPY** CALL 762 2026-11-11 (0DTE): 5,783 traded vs OI 1,015
- **SPY** CALL 763 2026-11-11 (0DTE): 2,986 traded vs OI 886
- **SPY** CALL 755 2026-11-11 (0DTE): 6,508 traded vs OI 1,849
- **SPY** CALL 759 2026-11-11 (0DTE): 6,275 traded vs OI 865
- **SPY** PUT 757 2026-11-11 (0DTE): 3,883 traded vs OI 417
- **SPY** CALL 760 2026-11-11 (0DTE): 14,428 traded vs OI 3,774
- **SPY** CALL 757 2026-11-11 (0DTE): 9,077 traded vs OI 1,636
- **SPY** CALL 759 2026-11-12 (1DTE): 2,848 traded vs OI 592
- **SPY** PUT 758 2026-11-11 (0DTE): 1,061 traded vs OI 431
- **SPY** CALL 758 2026-11-11 (0DTE): 7,205 traded vs OI 1,040
- **SPY** PUT 749 2026-11-11 (0DTE): 1,049 traded vs OI 533

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
