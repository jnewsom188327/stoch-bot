# GEX + FLOW SCAN - Wed Oct 28, 01:40 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (6)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 12:56 | **QQQ** | **CALLS** | 1m WHIPSAW (R1 R2) | 10/28 730C | 0.63 | 0.56 | +24% (10m) | **-11%** | -35% | 723.9 |
| 12:56 | **SPY** | **CALLS** | 1m WHIPSAW (R1 R2) | 10/29 779C | 0.63 | 0.46 | +3% (9m) | **-27%** | +10% | 772.67 |
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
| 1 | **AAPL** | 345.32 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 32 | none: 81 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (46 contracts' greeks worked out here) | POS +$355.1M | 341.44 | 350 | 345 | +$923k | +$73k bull / +$0 bear | out (clean 28, ADX 15, RVol 0.6) |
| 2 | **SMH** | 564.72 | - | **-** | 24 | - | POS +$55.6M | 559.62 | 570 | 555 | -$3.8M | +$74k bull / +$0 bear | out (clean 28, ADX 22, RVol 0.6) |
| 3 | **ORCL** | 130.21 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 24 | none: 26 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$11.0M | 126.79 | 135 | 130 | -$757k | - | out (clean 29, ADX 12, RVol 0.4) |
| 4 | **AMD** | 568.26 | - | **-** | 19 | - | POS +$177.1M | - | 600 | 550 | +$4.6M | +$76k bull / +$0 bear | out (clean 29, ADX 32, RVol 0.5) |
| 5 | **GOOGL** | 324.95 | - | **-** | 19 | - | POS +$18.1M | 321.13 | 355 | 330 | -$2.3M | +$164k bull / -$570k bear | out (clean 32, ADX 27, RVol 1.2) |
| 6 | **NVDA** | 217.06 | - | **-** | 18 | - | POS +$519.7M | 210.11 | 220 | 215 | +$9.8M | +$104k bull / +$0 bear | out (clean 26, ADX 18, RVol 0.6) |
| 7 | **MU** | 967.75 | - | **-** | 18 | - | POS +$631.4M | - | 950 | 950 | +$23.9M | +$3.3M bull / -$1.8M bear | out (clean 28, ADX 25, RVol 0.5) |
| 8 | **META** | 612.65 | - | **-** | 17 | - | NEG -$268.3M | 635.97 | 650 | 610 | +$7.4M | +$0 bull / -$435k bear | out (clean 28, ADX 16, RVol 0.6) |
| 9 | **MSFT** | 527.45 | - | **-** | 16 | - | POS +$463.0M | - | 550 | 500 | +$1.1M | +$0 bull / -$806k bear | out (clean 29, ADX 15, RVol 1.0) |
| 10 | **SPY** | 770.95 | - | **-** | 14 | - | NEG -$2.4B | 773.42 | 780 | 750 | -$13.5M | +$3.5M bull / -$4.4M bear | out (clean 28, ADX 13, RVol 0.3) |
| 11 | **TSLA** | 401.56 | - | **-** | 14 | - | POS +$613.3M | - | 400 | 395 | -$15.5M | +$239k bull / +$0 bear | out (clean 29, ADX 11, RVol 0.1) |
| 12 | **AMZN** | 252.76 | - | **-** | 14 | - | POS +$189.8M | 238.27 | 255 | 250 | +$452k | +$228k bull / -$59k bear | out (clean 31, ADX 16, RVol 0.6) |
| 13 | **QQQ** | 721.99 | - | **-** | 13 | - | NEG -$1.8B | 727.88 | 720 | 720 | +$12.9M | +$268k bull / +$0 bear | out (clean 29, ADX 12, RVol 0.2) |
| 14 | **HOOD** | 90.48 | - | **-** | 13 | - | NEG -$17.5M | - | 95 | 90 | +$3.9M | - | out (clean 30, ADX 19, RVol 0.9) |
| 15 | **IWM** | 280.50 | - | **-** | 12 | - | NEG -$226.8M | 281.29 | 280 | 270 | +$9.1M | - | out (clean 24, ADX 29, RVol 0.2) |
| 16 | **SHOP** | 167.93 | - | **-** | 11 | - | NEG -$3.5M | 171.83 | 175 | 165 | -$28k | - | out (clean 29, ADX 27, RVol 0.4) |
| 17 | **BABA** | 100.14 | - | **-** | 11 | - | NEG -$14.1M | 103.1 | 102 | 100 | +$69k | - | out (clean 28, ADX 16, RVol 1.4) |
| 18 | **PLTR** | 194.47 | - | **-** | 8 | - | POS +$44.6M | 189.42 | 200 | 190 | +$24k | - | out (clean 27, ADX 42, RVol 0.2) |
| 19 | **AVGO** | 348.16 | - | **-** | 7 | - | POS +$59.4M | 337.09 | 350 | 340 | -$500k | - | out (clean 29, ADX 31, RVol 0.5) |
| 20 | **SMCI** | 34.80 | - | **-** | 7 | - | POS +$19.3M | - | 35 | 35 | +$117k | - | out (clean 28, ADX 15, RVol 0.3) |
| 21 | **UBER** | 65.38 | - | **-** | 7 | - | NEG -$30.7M | - | 70 | 65 | +$22k | - | out (clean 30, ADX 28, RVol 0.3) |
| 22 | **NFLX** | 61.77 | - | **-** | 5 | - | NEG -$57.2M | - | 65 | 60 | -$126k | - | out (clean 31, ADX 14, RVol 0.5) |
| 23 | **ARM** | 232.34 | - | **-** | 5 | - | POS +$1.8M | 223.46 | 227.5 | 250 | +$69k | - | out (clean 26, ADX 17, RVol 0.4) |
| 24 | **CRM** | 241.21 | - | **-** | 5 | - | POS +$7.1M | 233.91 | 260 | 240 | +$27k | - | out (clean 27, ADX 12, RVol 0.4) |
| 25 | **COIN** | 158.39 | - | **-** | 4 | - | POS +$1.1M | 155.69 | 170 | 150 | +$40k | - | out (clean 29, ADX 6, RVol 0.3) |
| 26 | **DELL** | 493.70 | - | **-** | 4 | - | POS +$28.4M | - | 500 | 500 | +$125k | - | out (clean 31, ADX 12, RVol 0.4) |
| 27 | **MSTR** | 139.32 | - | **-** | 4 | - | POS +$16.3M | - | 152.5 | 140 | +$346k | - | out (clean 27, ADX 8, RVol 0.3) |

## Big prints this scan (60)
- **SPY** CALL 758 2026-10-29 (1DTE): 414 @ 13.49 = **+$558k** SELL | vol 1,500 / OI 36
- **SPY** CALL 758 2026-10-29 (1DTE): 414 @ 13.49 = **+$558k** SELL | vol 1,500 / OI 36
- **SPY** CALL 758 2026-10-29 (1DTE): 414 @ 13.49 = **+$558k** SELL | vol 1,500 / OI 36
- **SPY** CALL 760 2026-10-28 (0DTE): 414 @ 11.16 = **+$462k** BUY | vol 3,119 / OI 943
- **SPY** CALL 760 2026-10-28 (0DTE): 414 @ 11.16 = **+$462k** BUY | vol 3,119 / OI 943
- **SPY** CALL 760 2026-10-28 (0DTE): 414 @ 11.16 = **+$462k** BUY | vol 3,119 / OI 943
- **SPY** CALL 763 2026-10-29 (1DTE): 414 @ 9.05 = **+$375k** SELL | vol 1,688 / OI 1,316
- **SPY** CALL 763 2026-10-29 (1DTE): 414 @ 9.05 = **+$375k** SELL | vol 1,688 / OI 1,316
- **SPY** CALL 763 2026-10-29 (1DTE): 414 @ 9.05 = **+$375k** SELL | vol 1,688 / OI 1,316
- **SPY** CALL 758 2026-10-29 (1DTE): 217 @ 13.49 = **+$293k** SELL | vol 1,500 / OI 36
- **SPY** CALL 765 2026-10-28 (0DTE): 414 @ 6.48 = **+$268k** SELL | vol 4,857 / OI 2,022
- **SPY** CALL 765 2026-10-28 (0DTE): 414 @ 6.48 = **+$268k** SELL | vol 4,857 / OI 2,022
- **SPY** CALL 765 2026-10-28 (0DTE): 414 @ 6.48 = **+$268k** SELL | vol 4,857 / OI 2,022
- **SPY** CALL 760 2026-10-28 (0DTE): 217 @ 11.16 = **+$242k** BUY | vol 3,119 / OI 943
- **SPY** PUT 771 2026-10-28 (0DTE): 980 @ 2.10 = **+$206k** BUY | vol 165,197 / OI 1,490

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 758 2026-10-29 (1DTE): 1,500 traded vs OI 36
- **SPY** CALL 763 2026-10-29 (1DTE): 1,688 traded vs OI 1,316
- **SPY** CALL 797 2026-10-29 (1DTE): 582 traded vs OI 121
- **QQQ** PUT 703 2026-10-29 (1DTE): 504 traded vs OI 222
- **NVDA** PUT 230 2026-11-02 (5DTE): 510 traded vs OI 55
- **AMD** CALL 612.5 2026-10-30 (2DTE): 525 traded vs OI 340

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
