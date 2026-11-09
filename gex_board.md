# GEX + FLOW SCAN - Mon Nov 09, 01:00 PM ET
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
Last 1m check 13:00:08 ET, last candle SPY 12:59, QQQ 12:59 | no errors
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
| 1 | **GOOGL** | 290.65 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 36 | none: 92 calls 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (36 contracts' greeks worked out here) | POS +$11.5M | 289.3 | 300 | 290 | +$4.5M | +$163k bull / +$0 bear | out (clean 31, ADX 14, RVol 0.6) |
| 2 | **AVGO** | 319.94 | - | **-** | 28 | - | NEG -$64.4M | - | 340 | 320 | -$8.5M | +$131k bull / -$32k bear | out (clean 31, ADX 51, RVol 1.4) |
| 3 | **SPY** | 752.43 | - | **-** | 26 | - | NEG -$5.7B | 761.47 | 750 | 740 | -$300.3M | +$2.9M bull / -$607k bear | out (clean 32, ADX 52, RVol 0.4) |
| 4 | **AMD** | 503.25 | - | **-** | 26 | - | POS +$23.5M | 488.71 | 500 | 500 | -$57.5M | +$2.7M bull / -$781k bear | out (clean 32, ADX 46, RVol 0.5) |
| 5 | **QQQ** | 677.12 | - | **-** | 25 | - | NEG -$2.1B | 698.9 | 680 | 680 | -$225.4M | +$100k bull / -$377k bear | out (clean 32, ADX 41, RVol 0.5) |
| 6 | **TSLA** | 377.46 | - | **-** | 25 | - | POS +$119.5M | - | 380 | 380 | -$92.3M | +$241k bull / -$117k bear | out (clean 34, ADX 28, RVol 0.3) |
| 7 | **CRM** | 216.50 | - | **-** | 23 | - | NEG -$11.3M | - | 230 | 220 | -$73k | +$0 bull / -$26k bear | out (clean 34, ADX 31, RVol 1.0) |
| 8 | **NVDA** | 177.22 | - | **-** | 21 | - | NEG -$199.3M | - | 190 | 190 | -$55.3M | +$1.3M bull / -$68k bear | out (clean 32, ADX 24, RVol 1.4) |
| 9 | **META** | 642.03 | - | **-** | 21 | - | POS +$175.5M | 611.91 | 650 | 640 | -$9.3M | +$52k bull / -$746k bear | out (clean 32, ADX 34, RVol 0.5) |
| 10 | **HOOD** | 83.98 | - | **-** | 19 | - | NEG -$1.5M | - | 85 | 85 | -$2.1M | +$0 bull / -$28k bear | out (clean 30, ADX 24, RVol 0.4) |
| 11 | **IWM** | 281.68 | - | **-** | 18 | - | NEG -$822.7M | 284.8 | 285 | 270 | -$21.0M | - | out (clean 34, ADX 57, RVol 0.3) |
| 12 | **MSTR** | 125.37 | - | **-** | 18 | - | POS +$778k | 123.89 | 135 | 120 | -$2.0M | +$102k bull / -$25k bear | out (clean 30, ADX 24, RVol 0.2) |
| 13 | **AAPL** | 349.09 | - | **-** | 17 | - | POS +$382.5M | 338.88 | 350 | 350 | -$5.1M | +$87k bull / +$0 bear | out (clean 27, ADX 24, RVol 0.2) |
| 14 | **MSFT** | 544.01 | - | **-** | 17 | - | POS +$629.5M | - | 550 | 540 | +$1.0M | +$25k bull / -$70k bear | out (clean 34, ADX 32, RVol 0.3) |
| 15 | **NFLX** | 63.68 | - | **-** | 16 | - | NEG -$20.2M | - | 65 | 65 | +$91k | +$56k bull / +$0 bear | out (clean 30, ADX 16, RVol 0.8) |
| 16 | **MU** | 729.19 | - | **-** | 16 | - | NEG -$9.1M | 739.14 | 750 | 750 | -$7.1M | +$953k bull / -$193k bear | out (clean 31, ADX 26, RVol 0.3) |
| 17 | **ORCL** | 118.74 | - | **-** | 15 | - | NEG -$27.2M | - | 125 | 125 | -$342k | +$40k bull / +$0 bear | out (clean 29, ADX 19, RVol 0.2) |
| 18 | **COIN** | 136.80 | - | **-** | 14 | - | NEG -$6.8M | - | 140 | 135 | -$1.9M | - | out (clean 32, ADX 14, RVol 0.5) |
| 19 | **SMCI** | 29.16 | - | **-** | 13 | - | NEG -$22k | - | 30 | 30 | -$951k | - | out (clean 29, ADX 10, RVol 0.4) |
| 20 | **UBER** | 70.61 | - | **-** | 13 | - | POS +$5.9M | 69.17 | 70 | 70 | -$109k | - | out (clean 32, ADX 45, RVol 0.7) |
| 21 | **SHOP** | 151.13 | - | **-** | 13 | - | POS +$2.2M | - | 150 | 140 | -$89k | - | out (clean 34, ADX 22, RVol 0.1) |
| 22 | **SMH** | 484.89 | - | **-** | 12 | - | NEG -$219.4M | - | 500 | 475 | -$2.6M | - | out (clean 31, ADX 35, RVol 0.4) |
| 23 | **AMZN** | 268.35 | - | **-** | 11 | - | POS +$402.4M | - | 270 | 265 | +$20.3M | - | out (clean 34, ADX 11, RVol 0.2) |
| 24 | **PLTR** | 169.26 | - | **-** | 10 | - | POS +$11.0M | - | 165 | 180 | -$2.6M | - | out (clean 30, ADX 33, RVol 0.3) |
| 25 | **ARM** | 186.84 | - | **-** | 9 | - | NEG -$4.6M | - | 185 | 190 | +$383k | - | out (clean 27, ADX 28, RVol 0.6) |
| 26 | **DELL** | 349.44 | - | **-** | 7 | - | NEG -$6.4M | - | 350 | 340 | -$163k | - | out (clean 32, ADX 33, RVol 0.2) |
| 27 | **BABA** | 105.47 | - | **-** | 6 | - | POS +$2.8M | 103.99 | 110 | 110 | +$105k | - | out (clean 31, ADX 29, RVol 0.2) |

## Big prints this scan (37)
- **SPY** CALL 750 2026-11-10 (1DTE): 250 @ 4.70 = **+$118k** SELL | vol 35,606 / OI 8,230
- **SPY** CALL 750 2026-11-10 (1DTE): 250 @ 4.65 = **+$116k** SELL | vol 35,606 / OI 8,230
- **SPY** CALL 750 2026-11-10 (1DTE): 246 @ 4.68 = **+$115k** SELL | vol 35,606 / OI 8,230
- **AMD** CALL 490 2026-11-13 (4DTE): 43 @ 26.25 = **+$113k** SELL | vol 3,039 / OI 1,648
- **SPY** CALL 741 2026-11-09 (0DTE): 98 @ 11.29 = **+$111k** SELL | vol 10,042 / OI 590
- **NVDA** CALL 177.5 2026-11-13 (4DTE): 158 @ 5.80 = **+$92k** BUY | vol 13,006 / OI 121
- **TSLA** PUT 377.5 2026-11-09 (0DTE): 540 @ 1.54 = **+$83k** BUY | vol 50,028 / OI 267
- **NVDA** CALL 177.5 2026-11-13 (4DTE): 142 @ 5.80 = **+$82k** BUY | vol 13,006 / OI 121
- **MU** PUT 730 2026-11-09 (0DTE): 200 @ 3.65 = **+$73k** SELL | vol 15,886 / OI 118
- **AMD** CALL 490 2026-11-13 (4DTE): 27 @ 26.25 = **+$71k** SELL | vol 3,039 / OI 1,648
- **MU** PUT 730 2026-11-11 (2DTE): 31 @ 20.60 = **+$64k** SELL | vol 1,426 / OI 40
- **MU** CALL 740 2026-11-11 (2DTE): 31 @ 18.55 = **+$58k** BUY | vol 1,696 / OI 120
- **AMD** PUT 497.5 2026-11-09 (0DTE): 300 @ 1.67 = **+$50k** BUY | vol 8,330 / OI 90
- **AMD** PUT 510 2026-11-11 (2DTE): 25 @ 19.36 = **+$48k** BUY | vol 125 / OI 88
- **MSFT** CALL 540 2026-11-16 (7DTE): 49 @ 9.82 = **+$48k** MID | vol 99 / OI 99

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 767 2026-11-10 (1DTE): 1,419 traded vs OI 1,414
- **SPY** CALL 797 2026-11-12 (3DTE): 947 traded vs OI 64
- **SPY** CALL 753 2026-11-13 (4DTE): 1,625 traded vs OI 1,072
- **QQQ** CALL 686 2026-11-13 (4DTE): 500 traded vs OI 383
- **QQQ** CALL 691 2026-11-13 (4DTE): 506 traded vs OI 253
- **IWM** CALL 289 2026-11-18 (9DTE): 502 traded vs OI 299
- **SMH** CALL 490 2026-11-20 (11DTE): 956 traded vs OI 726
- **NVDA** CALL 182.5 2026-11-18 (9DTE): 769 traded vs OI 292
- **AMD** CALL 502.5 2026-11-11 (2DTE): 506 traded vs OI 42
- **MSFT** CALL 547.5 2026-11-11 (2DTE): 515 traded vs OI 84
- **GOOGL** PUT 282.5 2026-11-11 (2DTE): 537 traded vs OI 101
- **COIN** CALL 149 2026-11-13 (4DTE): 501 traded vs OI 0
- **MU** CALL 760 2026-11-11 (2DTE): 908 traded vs OI 810

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
