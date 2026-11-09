# GEX + FLOW SCAN - Mon Nov 09, 02:10 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (4)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:04 | **SPY** | **CALLS** | 1m WHIPSAW (R1) | 11/09 754C | 0.41 | 0.23 | -2% (0m) | **-44%** (done) | +28% | 752.23 |
| 10:35 | **AMZN** | **CALLS** | TREND + FLOW | 11/09 272.5C | 0.49 | 0.05 | +2% (2m) | **-90%** (done) | +225% | 273.49 |
| 10:00 | **MSFT** | **CALLS** | TREND + FLOW | 11/09 545C | 0.77 | 0.72 | +51% (23m) | **-6%** (done) | +545% | 550 |
| 10:00 | **AMZN** | **CALLS** | TREND + FLOW | 11/09 275C | 0.48 | 0.02 | +13% (6m) | **-96%** (done) | +258% | 275.95 |

## 1m RULES on SPY / QQQ - loose (1 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 14:10:08 ET, last candle SPY 14:09, QQQ 14:09 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 11:03 | SPY | 1m WHIPSAW | R1 | CALLS | TURNING away | **FIRE** SPY261109C00754000 |

## Flow surges NOT fired - price disagreed (17 today, last 5)
- 10:55 AVGO PUTS: price +2.40 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:40 AVGO PUTS: price +1.16 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:40 QQQ PUTS: price +0.45 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:35 AVGO PUTS: price +1.05 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:30 QQQ PUTS: price +0.53 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **SPY** | 752.76 | - | **-** | 25 | - | NEG -$6.4B | 761.91 | 750 | 740 | -$313.5M | +$1.3M bull / -$729k bear | out (clean 32, ADX 41, RVol 0.3) |
| 2 | **AMD** | 507.43 | - | **-** | 25 | - | POS +$29.1M | 520.56 | 500 | 500 | -$63.0M | +$2.8M bull / -$1.3M bear | out (clean 31, ADX 42, RVol 0.5) |
| 3 | **QQQ** | 677.60 | - | **-** | 22 | - | NEG -$2.1B | 698.76 | 680 | 680 | -$234.0M | +$967k bull / -$1.5M bear | out (clean 32, ADX 31, RVol 0.3) |
| 4 | **TSLA** | 377.37 | - | **-** | 22 | - | POS +$117.0M | - | 380 | 380 | -$91.3M | +$282k bull / -$403k bear | out (clean 33, ADX 19, RVol 0.3) |
| 5 | **GOOGL** | 290.21 | PINNED between the walls (positive gamma) - chop | **-** | 22 | - | POS +$17.2M | 288.56 | 290 | 290 | +$4.3M | - | out (clean 31, ADX 25, RVol 0.5) |
| 6 | **AVGO** | 319.12 | - | **-** | 22 | - | NEG -$66.3M | - | 340 | 320 | -$7.6M | +$0 bull / -$72k bear | out (clean 31, ADX 27, RVol 0.9) |
| 7 | **SMCI** | 28.81 | - | **-** | 22 | - | NEG -$315k | - | 30 | 30 | -$635k | +$0 bull / -$27k bear | out (clean 29, ADX 28, RVol 0.6) |
| 8 | **SMH** | 484.25 | - | **-** | 20 | - | NEG -$222.1M | - | 485 | 475 | -$2.8M | +$0 bull / -$47k bear | out (clean 30, ADX 26, RVol 0.3) |
| 9 | **AMZN** | 268.08 | - | **-** | 20 | - | POS +$378.2M | - | 270 | 265 | +$20.0M | +$0 bull / -$27k bear | out (clean 33, ADX 11, RVol 0.3) |
| 10 | **IWM** | 282.38 | - | **-** | 19 | - | NEG -$657.9M | 284.73 | 283 | 270 | -$24.0M | - | out (clean 35, ADX 60, RVol 0.6) |
| 11 | **HOOD** | 83.95 | - | **-** | 19 | - | NEG -$1.5M | - | 85 | 85 | -$2.4M | +$0 bull / -$113k bear | out (clean 29, ADX 18, RVol 0.4) |
| 12 | **NVDA** | 176.59 | - | **-** | 18 | - | NEG -$201.0M | - | 190 | 190 | -$44.8M | +$1.1M bull / -$444k bear | out (clean 33, ADX 17, RVol 0.9) |
| 13 | **AAPL** | 351.44 | - | **-** | 18 | - | POS +$475.8M | 339.96 | 350 | 350 | -$7.1M | +$0 bull / -$137k bear | out (clean 28, ADX 25, RVol 0.4) |
| 14 | **META** | 641.70 | - | **-** | 18 | - | POS +$161.5M | 613.64 | 650 | 640 | -$10.6M | +$0 bull / -$74k bear | out (clean 32, ADX 22, RVol 0.4) |
| 15 | **MSFT** | 544.39 | - | **-** | 15 | - | POS +$633.0M | - | 550 | 540 | +$1.1M | +$59k bull / +$0 bear | out (clean 33, ADX 22, RVol 0.1) |
| 16 | **MU** | 727.92 | - | **-** | 14 | - | NEG -$11.6M | 738.53 | 750 | 750 | +$4.8M | +$876k bull / -$810k bear | out (clean 31, ADX 15, RVol 0.3) |
| 17 | **UBER** | 70.84 | - | **-** | 14 | - | POS +$7.0M | 69.14 | 75 | 70 | -$244k | - | out (clean 33, ADX 52, RVol 0.5) |
| 18 | **COIN** | 137.03 | - | **-** | 13 | - | NEG -$6.6M | - | 140 | 135 | -$2.0M | - | out (clean 33, ADX 13, RVol 0.1) |
| 19 | **SHOP** | 151.55 | - | **-** | 12 | - | POS +$1.9M | - | 150 | 140 | -$85k | - | out (clean 34, ADX 24, RVol 0.1) |
| 20 | **DELL** | 346.65 | - | **-** | 8 | - | NEG -$6.6M | - | 350 | 340 | +$492k | - | out (clean 33, ADX 29, RVol 0.4) |
| 21 | **ARM** | 185.79 | - | **-** | 8 | - | NEG -$4.7M | - | 185 | 190 | +$751k | - | out (clean 27, ADX 16, RVol 0.4) |
| 22 | **MSTR** | 125.46 | - | **-** | 7 | - | POS +$749k | 124.28 | 135 | 120 | -$1.9M | - | out (clean 30, ADX 21, RVol 0.3) |
| 23 | **CRM** | 215.69 | - | **-** | 7 | - | NEG -$11.4M | - | 195 | 220 | -$59k | - | out (clean 34, ADX 18, RVol 0.3) |
| 24 | **PLTR** | 168.64 | - | **-** | 6 | - | POS +$11.6M | - | 165 | 170 | -$1.9M | - | out (clean 30, ADX 17, RVol 0.4) |
| 25 | **BABA** | 105.40 | - | **-** | 6 | - | POS +$1.7M | 104.45 | 110 | 110 | +$77k | - | out (clean 31, ADX 21, RVol 0.5) |
| 26 | **NFLX** | 63.67 | - | **-** | 5 | - | NEG -$19.9M | - | 65 | 65 | +$165k | - | out (clean 30, ADX 13, RVol 0.4) |
| 27 | **ORCL** | 118.91 | - | **-** | 4 | - | NEG -$27.1M | - | 125 | 120 | -$429k | - | out (clean 29, ADX 12, RVol 0.3) |

## Big prints this scan (41)
- **AMD** PUT 500 2026-11-11 (2DTE): 498 @ 11.15 = **+$555k** SELL | vol 1,559 / OI 49
- **AMD** PUT 485 2026-11-13 (4DTE): 200 @ 10.00 = **+$200k** SELL | vol 2,942 / OI 518
- **SPY** PUT 778 2026-11-13 (4DTE): 80 @ 24.81 = **+$198k** MID | vol 160 / OI 5
- **AMD** PUT 485 2026-11-13 (4DTE): 190 @ 10.00 = **+$190k** SELL | vol 2,942 / OI 518
- **AMD** PUT 485 2026-11-13 (4DTE): 176 @ 10.10 = **+$178k** SELL | vol 2,942 / OI 518
- **SPY** PUT 754 2026-11-09 (0DTE): 1,277 @ 1.29 = **+$165k** SELL | vol 97,547 / OI 1,253
- **SPY** CALL 738 2026-11-09 (0DTE): 100 @ 15.27 = **+$153k** BUY | vol 4,234 / OI 906
- **SPY** CALL 755 2026-11-13 (4DTE): 261 @ 4.92 = **+$128k** BUY | vol 13,058 / OI 2,927
- **SPY** PUT 740 2026-11-13 (4DTE): 601 @ 2.12 = **+$127k** BUY | vol 18,043 / OI 8,834
- **SPY** PUT 754 2026-11-09 (0DTE): 946 @ 1.33 = **+$126k** SELL | vol 97,547 / OI 1,253
- **SPY** PUT 754 2026-11-09 (0DTE): 953 @ 1.30 = **+$124k** SELL | vol 97,547 / OI 1,253
- **SPY** PUT 754 2026-11-09 (0DTE): 987 @ 1.25 = **+$123k** SELL | vol 97,547 / OI 1,253
- **TSLA** PUT 377.5 2026-11-11 (2DTE): 198 @ 5.94 = **+$118k** SELL | vol 3,444 / OI 601
- **QQQ** PUT 690 2026-11-13 (4DTE): 80 @ 14.67 = **+$117k** SELL | vol 478 / OI 10,715
- **NVDA** CALL 177.5 2026-11-16 (7DTE): 200 @ 5.65 = **+$113k** BUY | vol 3,803 / OI 12

## New unusual volume (traded more than open interest, 500+)
- **QQQ** CALL 701 2026-11-30 (21DTE): 685 traded vs OI 127
- **QQQ** CALL 705 2026-11-23 (14DTE): 689 traded vs OI 0
- **IWM** CALL 286 2026-11-10 (1DTE): 2,152 traded vs OI 2,102
- **IWM** PUT 269 2026-11-20 (11DTE): 28,497 traded vs OI 28,056
- **IWM** PUT 266 2026-11-20 (11DTE): 78,797 traded vs OI 67,754
- **TSLA** PUT 357.5 2026-11-13 (4DTE): 821 traded vs OI 788
- **TSLA** PUT 340 2026-11-13 (4DTE): 2,238 traded vs OI 2,229
- **AMD** PUT 505 2026-11-13 (4DTE): 574 traded vs OI 280
- **META** CALL 645 2026-11-11 (2DTE): 507 traded vs OI 67
- **AVGO** CALL 310 2026-11-11 (2DTE): 504 traded vs OI 27
- **SMCI** CALL 29.5 2026-11-20 (11DTE): 505 traded vs OI 0
- **MU** CALL 690 2026-11-13 (4DTE): 535 traded vs OI 302
- **BABA** CALL 106 2026-11-13 (4DTE): 1,436 traded vs OI 1,394

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
