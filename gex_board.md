# GEX + FLOW SCAN - Mon Nov 09, 02:20 PM ET
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
Last 1m check 14:20:08 ET, last candle SPY 14:19, QQQ 14:19 | no errors
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
| 1 | **AMD** | 505.94 | FLIP CROSS down into negative gamma | **PUTS** | 37 | none: 160 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (69 contracts' greeks worked out here) | POS +$30.5M | 520.07 | 500 | 500 | -$60.5M | +$2.3M bull / -$30k bear | out (clean 31, ADX 41, RVol 0.5) |
| 2 | **GOOGL** | 289.92 | PINNED between the walls (positive gamma) - chop | **-** | 31 | - | POS +$16.1M | 288.42 | 290 | 290 | +$4.3M | +$0 bull / -$34k bear | out (clean 31, ADX 25, RVol 0.4) |
| 3 | **META** | 641.34 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 25 | none: 208 calls 0-7DTE > 11 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (79 contracts' greeks worked out here) | POS +$165.3M | 613.66 | 650 | 640 | -$10.7M | - | out (clean 32, ADX 21, RVol 0.4) |
| 4 | **MU** | 726.87 | FLIP CROSS up into positive gamma | **CALLS** | 25 | none: 193 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (78 contracts' greeks worked out here) | POS +$4.8M | 724.28 | 750 | 750 | +$5.2M | +$345k bull / +$0 bear | out (clean 31, ADX 14, RVol 0.3) |
| 5 | **SPY** | 752.32 | - | **-** | 24 | - | NEG -$6.2B | 761.66 | 750 | 740 | -$311.3M | +$3.6M bull / -$127k bear | out (clean 32, ADX 38, RVol 0.2) |
| 6 | **TSLA** | 377.28 | - | **-** | 22 | - | POS +$120.1M | - | 380 | 380 | -$90.6M | +$375k bull / +$0 bear | out (clean 33, ADX 19, RVol 0.2) |
| 7 | **QQQ** | 677.18 | - | **-** | 21 | - | NEG -$2.2B | 698.89 | 680 | 680 | -$230.7M | +$117k bull / +$0 bear | out (clean 31, ADX 29, RVol 0.2) |
| 8 | **AVGO** | 318.46 | - | **-** | 21 | - | NEG -$64.7M | - | 340 | 320 | -$7.3M | +$27k bull / +$0 bear | out (clean 31, ADX 24, RVol 0.8) |
| 9 | **SMH** | 483.52 | - | **-** | 20 | - | NEG -$218.4M | - | 485 | 475 | -$2.7M | +$33k bull / +$0 bear | out (clean 30, ADX 23, RVol 0.4) |
| 10 | **AMZN** | 267.87 | - | **-** | 20 | - | POS +$372.6M | - | 270 | 265 | +$20.5M | +$152k bull / +$0 bear | out (clean 33, ADX 10, RVol 0.3) |
| 11 | **AAPL** | 351.85 | - | **-** | 19 | - | POS +$515.0M | 338.67 | 350 | 350 | -$8.9M | +$0 bull / -$218k bear | out (clean 28, ADX 30, RVol 0.4) |
| 12 | **IWM** | 282.14 | - | **-** | 18 | - | NEG -$743.4M | 284.73 | 285 | 270 | -$23.9M | - | out (clean 35, ADX 58, RVol 0.6) |
| 13 | **NVDA** | 176.15 | - | **-** | 18 | - | NEG -$191.5M | - | 190 | 190 | -$44.3M | +$665k bull / +$0 bear | out (clean 33, ADX 18, RVol 0.9) |
| 14 | **MSFT** | 545.15 | - | **-** | 16 | - | POS +$651.4M | - | 550 | 540 | +$875k | +$0 bull / -$29k bear | out (clean 33, ADX 24, RVol 0.2) |
| 15 | **PLTR** | 168.31 | - | **-** | 15 | - | POS +$11.3M | - | 165 | 170 | -$1.6M | +$252k bull / +$0 bear | out (clean 30, ADX 15, RVol 0.3) |
| 16 | **ORCL** | 118.79 | - | **-** | 14 | - | NEG -$27.4M | - | 125 | 120 | -$412k | +$0 bull / -$27k bear | out (clean 29, ADX 10, RVol 0.2) |
| 17 | **COIN** | 137.23 | - | **-** | 13 | - | NEG -$6.8M | - | 140 | 135 | -$2.0M | - | out (clean 33, ADX 13, RVol 0.2) |
| 18 | **UBER** | 70.68 | - | **-** | 13 | - | POS +$6.3M | 69.2 | 70 | 70 | -$199k | - | out (clean 33, ADX 48, RVol 0.4) |
| 19 | **SMCI** | 28.79 | - | **-** | 12 | - | NEG -$299k | - | 30 | 30 | -$611k | - | out (clean 29, ADX 29, RVol 0.5) |
| 20 | **SHOP** | 151.49 | - | **-** | 12 | - | POS +$1.7M | - | 150 | 140 | -$81k | - | out (clean 34, ADX 26, RVol 0.1) |
| 21 | **DELL** | 346.19 | - | **-** | 8 | - | NEG -$6.6M | - | 350 | 340 | +$537k | - | out (clean 33, ADX 30, RVol 0.3) |
| 22 | **HOOD** | 83.95 | - | **-** | 8 | - | NEG -$1.5M | - | 85 | 85 | -$2.3M | - | out (clean 29, ADX 16, RVol 0.4) |
| 23 | **ARM** | 185.69 | - | **-** | 8 | - | NEG -$4.7M | - | 185 | 190 | +$755k | - | out (clean 27, ADX 16, RVol 0.5) |
| 24 | **MSTR** | 125.69 | - | **-** | 7 | - | POS +$911k | 124.07 | 135 | 120 | -$1.9M | - | out (clean 30, ADX 19, RVol 0.2) |
| 25 | **CRM** | 215.00 | - | **-** | 7 | - | NEG -$10.8M | - | 195 | 220 | -$55k | - | out (clean 33, ADX 18, RVol 0.4) |
| 26 | **NFLX** | 63.66 | - | **-** | 5 | - | NEG -$20.0M | - | 65 | 65 | +$168k | - | out (clean 30, ADX 12, RVol 0.3) |
| 27 | **BABA** | 105.33 | - | **-** | 5 | - | POS +$1.6M | 104.4 | 110 | 100 | +$81k | - | out (clean 31, ADX 20, RVol 0.5) |

## Big prints this scan (28)
- **SPY** CALL 730 2026-11-10 (1DTE): 1,000 @ 23.15 = **+$2.3M** BUY | vol 5,095 / OI 5,480
- **SPY** PUT 755 2026-11-10 (1DTE): 500 @ 3.94 = **+$197k** SELL | vol 4,126 / OI 3,597
- **SPY** PUT 755 2026-11-10 (1DTE): 500 @ 3.94 = **+$197k** SELL | vol 4,126 / OI 3,597
- **AMD** CALL 500 2026-11-09 (0DTE): 200 @ 8.10 = **+$162k** BUY | vol 46,607 / OI 1,188
- **AMZN** CALL 270 2026-11-13 (4DTE): 428 @ 3.55 = **+$152k** BUY | vol 5,478 / OI 7,386
- **AMD** CALL 520 2026-11-13 (4DTE): 90 @ 13.25 = **+$119k** BUY | vol 2,669 / OI 0
- **PLTR** CALL 167.5 2026-11-13 (4DTE): 164 @ 4.95 = **+$81k** BUY | vol 9,210 / OI 1,196
- **PLTR** CALL 167.5 2026-11-13 (4DTE): 150 @ 4.95 = **+$74k** BUY | vol 9,210 / OI 1,196
- **AMD** CALL 520 2026-11-13 (4DTE): 50 @ 13.81 = **+$69k** BUY | vol 2,669 / OI 0
- **AMD** CALL 520 2026-11-13 (4DTE): 50 @ 13.81 = **+$69k** BUY | vol 2,669 / OI 0
- **AAPL** CALL 360 2026-11-13 (4DTE): 727 @ 0.83 = **+$60k** SELL | vol 9,282 / OI 8,819
- **AMD** CALL 510 2026-11-11 (2DTE): 37 @ 13.45 = **+$50k** BUY | vol 2,075 / OI 432
- **MU** CALL 710 2026-11-13 (4DTE): 12 @ 39.92 = **+$48k** BUY | vol 740 / OI 642
- **PLTR** CALL 167.5 2026-11-13 (4DTE): 80 @ 4.95 = **+$40k** BUY | vol 9,210 / OI 1,196
- **AAPL** CALL 350 2026-11-11 (2DTE): 100 @ 3.55 = **+$36k** SELL | vol 11,352 / OI 705

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 743 2026-11-12 (3DTE): 509 traded vs OI 342
- **SPY** PUT 755 2026-11-10 (1DTE): 4,126 traded vs OI 3,597
- **SPY** CALL 757 2026-11-13 (4DTE): 904 traded vs OI 864
- **SPY** CALL 754 2026-11-16 (7DTE): 509 traded vs OI 119
- **QQQ** PUT 633 2026-11-11 (2DTE): 1,074 traded vs OI 0
- **QQQ** CALL 685 2026-11-20 (11DTE): 5,932 traded vs OI 4,444
- **QQQ** CALL 714 2026-11-20 (11DTE): 3,144 traded vs OI 1,268
- **IWM** PUT 284 2026-11-09 (0DTE): 648 traded vs OI 193
- **IWM** PUT 283 2026-11-10 (1DTE): 597 traded vs OI 592
- **TSLA** CALL 400 2026-11-18 (9DTE): 515 traded vs OI 192
- **AAPL** PUT 355 2026-11-11 (2DTE): 512 traded vs OI 259
- **AAPL** PUT 365 2026-11-20 (11DTE): 1,037 traded vs OI 160
- **AAPL** CALL 360 2026-11-13 (4DTE): 9,282 traded vs OI 8,819
- **AMD** CALL 467.5 2026-11-09 (0DTE): 507 traded vs OI 287
- **MU** PUT 727.5 2026-11-13 (4DTE): 503 traded vs OI 283

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
