# GEX + FLOW SCAN - Mon Nov 09, 11:30 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (4)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:04 | **SPY** | **CALLS** | 1m WHIPSAW (R1) | 11/09 754C | 0.41 | 0.15 | -2% (0m) | **-63%** | +28% | 752.23 |
| 10:35 | **AMZN** | **CALLS** | TREND + FLOW | 11/09 272.5C | 0.49 | 0.08 | +2% (2m) | **-84%** | +225% | 273.49 |
| 10:00 | **MSFT** | **CALLS** | TREND + FLOW | 11/09 545C | 0.77 | 0.72 | +51% (23m) | **-6%** (done) | +545% | 550 |
| 10:00 | **AMZN** | **CALLS** | TREND + FLOW | 11/09 275C | 0.48 | 0.02 | +13% (6m) | **-96%** (done) | +258% | 275.95 |

## 1m RULES on SPY / QQQ - loose (1 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 11:30:08 ET, last candle SPY 11:29, QQQ 11:29 | no errors
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
| 1 | **IWM** | 280.80 | FLOW SURGE | **PUTS** | 42 | 11/09 281P @ 0.60 (delta 0.56) = est +95% at 279.85 | NEG -$1.0B | 284.91 | 285 | 270 | -$19.9M | +$0 bull / -$106k bear | out (clean 34, ADX 59, RVol 0.6) |
| 2 | **META** | 639.40 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 40 | none: 204 calls 0-7DTE > 9 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (76 contracts' greeks worked out here) | POS +$160.6M | 614.02 | 650 | 640 | -$5.7M | +$116k bull / +$0 bear | out (clean 33, ADX 39, RVol 0.7) |
| 3 | **MSFT** | 540.46 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 39 | none: 172 calls 0-7DTE > 9 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (90 contracts' greeks worked out here) | POS +$554.4M | - | 550 | 540 | +$3.5M | +$189k bull / -$35k bear | out (clean 34, ADX 28, RVol 0.5) |
| 4 | **AAPL** | 349.88 | PINNED between the walls (positive gamma) - chop | **-** | 34 | - | POS +$426.3M | 338.87 | 350 | 350 | -$5.7M | +$253k bull / +$0 bear | out (clean 28, ADX 41, RVol 0.6) |
| 5 | **AMZN** | 267.98 | FLOW SURGE | **CALLS** | 32 | none: 84 calls 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (34 contracts' greeks worked out here) | POS +$359.5M | - | 270 | 265 | +$21.2M | +$357k bull / -$76k bear | out (clean 35, ADX 21, RVol 0.6) |
| 6 | **TSLA** | 377.48 | - | **-** | 29 | - | POS +$113.2M | - | 380 | 380 | -$90.1M | +$1.1M bull / -$117k bear | out (clean 34, ADX 46, RVol 0.6) |
| 7 | **AMD** | 497.44 | - | **-** | 29 | - | POS +$8.9M | 490.56 | 500 | 500 | -$50.6M | +$3.4M bull / -$185k bear | out (clean 32, ADX 58, RVol 1.5) |
| 8 | **AVGO** | 317.25 | - | **-** | 29 | - | NEG -$63.2M | - | 340 | 320 | -$6.4M | +$1.2M bull / +$0 bear | out (clean 31, ADX 66, RVol 1.7) |
| 9 | **PLTR** | 168.68 | - | **-** | 28 | - | POS +$10.6M | - | 165 | 180 | -$4.4M | +$0 bull / -$312k bear | out (clean 30, ADX 53, RVol 0.9) |
| 10 | **SPY** | 749.61 | - | **-** | 27 | - | NEG -$7.0B | 761.76 | 750 | 740 | -$226.5M | +$6.2M bull / +$0 bear | out (clean 33, ADX 51, RVol 0.8) |
| 11 | **QQQ** | 674.91 | - | **-** | 27 | - | NEG -$2.1B | 698.94 | 680 | 680 | -$205.1M | +$2.0M bull / +$0 bear | out (clean 33, ADX 48, RVol 0.7) |
| 12 | **SMH** | 481.45 | - | **-** | 25 | - | NEG -$234.9M | - | 500 | 475 | -$2.1M | +$661k bull / +$0 bear | out (clean 32, ADX 44, RVol 1.1) |
| 13 | **NVDA** | 175.29 | - | **-** | 25 | - | NEG -$193.5M | - | 190 | 190 | -$33.8M | +$5.3M bull / +$0 bear | out (clean 32, ADX 42, RVol 4.9) |
| 14 | **SHOP** | 150.21 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 25 | none: 21 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$1.9M | - | 150 | 140 | -$49k | - | out (clean 35, ADX 14, RVol 0.2) |
| 15 | **HOOD** | 84.14 | - | **-** | 24 | - | NEG -$1.4M | - | 85 | 85 | -$2.0M | +$124k bull / +$0 bear | out (clean 31, ADX 54, RVol 0.7) |
| 16 | **UBER** | 69.54 | - | **-** | 24 | - | POS +$1.8M | 69.11 | 70 | 65 | -$126k | +$0 bull / -$29k bear | out (clean 30, ADX 31, RVol 0.9) |
| 17 | **COIN** | 136.97 | - | **-** | 21 | - | NEG -$6.5M | - | 140 | 135 | -$2.2M | - | out (clean 32, ADX 27, RVol 0.7) |
| 18 | **MSTR** | 126.08 | - | **-** | 21 | - | POS +$1.5M | 123.54 | 135 | 120 | -$2.5M | +$41k bull / +$0 bear | out (clean 30, ADX 20, RVol 0.7) |
| 19 | **GOOGL** | 290.76 | - | **-** | 20 | - | POS +$3.2M | 289.75 | 300 | 290 | +$3.6M | +$60k bull / +$0 bear | out (clean 31, ADX 25, RVol 0.8) |
| 20 | **MU** | 732.49 | - | **-** | 20 | - | NEG -$4.8M | - | 750 | 750 | -$13.7M | +$5.0M bull / +$0 bear | out (clean 33, ADX 49, RVol 0.6) |
| 21 | **ORCL** | 118.56 | - | **-** | 18 | - | NEG -$26.1M | - | 125 | 120 | -$257k | +$401k bull / +$0 bear | out (clean 30, ADX 29, RVol 0.6) |
| 22 | **SMCI** | 29.29 | - | **-** | 14 | - | NEG -$1k | - | 30 | 30 | -$895k | - | out (clean 31, ADX 13, RVol 0.7) |
| 23 | **BABA** | 105.48 | - | **-** | 13 | - | POS +$2.9M | 103.89 | 110 | 110 | +$314k | - | out (clean 32, ADX 38, RVol 1.5) |
| 24 | **DELL** | 349.13 | - | **-** | 12 | - | NEG -$6.3M | - | 350 | 340 | -$422k | - | out (clean 32, ADX 50, RVol 0.7) |
| 25 | **ARM** | 187.05 | - | **-** | 12 | - | NEG -$4.5M | - | 185 | 190 | +$179k | - | out (clean 27, ADX 51, RVol 1.4) |
| 26 | **NFLX** | 63.67 | - | **-** | 7 | - | NEG -$19.4M | - | 65 | 65 | +$122k | - | out (clean 31, ADX 19, RVol 0.7) |
| 27 | **CRM** | 214.87 | - | **-** | 6 | - | NEG -$10.9M | - | 195 | 220 | +$8k | - | out (clean 34, ADX 19, RVol 0.9) |

## Big prints this scan (106)
- **SPY** CALL 745 2026-11-11 (2DTE): 1,000 @ 8.28 = **+$828k** BUY | vol 2,426 / OI 1,005
- **MU** CALL 735 2026-11-11 (2DTE): 252 @ 24.80 = **+$625k** BUY | vol 1,734 / OI 160
- **SPY** PUT 756 2026-11-09 (0DTE): 837 @ 6.00 = **+$502k** SELL | vol 23,617 / OI 382
- **SPY** CALL 750 2026-11-11 (2DTE): 1,000 @ 4.94 = **+$494k** BUY | vol 4,822 / OI 1,538
- **NVDA** CALL 177.5 2026-11-11 (2DTE): 822 @ 4.15 = **+$341k** BUY | vol 14,350 / OI 144
- **NVDA** CALL 177.5 2026-11-11 (2DTE): 895 @ 3.75 = **+$336k** BUY | vol 14,350 / OI 144
- **SPY** PUT 756 2026-11-09 (0DTE): 500 @ 6.10 = **+$305k** SELL | vol 23,617 / OI 382
- **SPY** PUT 756 2026-11-09 (0DTE): 471 @ 6.20 = **+$292k** SELL | vol 23,617 / OI 382
- **QQQ** CALL 668 2026-11-09 (0DTE): 219 @ 8.99 = **+$197k** BUY | vol 26,258 / OI 466
- **NVDA** PUT 177.5 2026-11-13 (4DTE): 300 @ 6.30 = **+$189k** SELL | vol 6,144 / OI 1,585
- **NVDA** PUT 180 2026-11-09 (0DTE): 400 @ 4.00 = **+$160k** SELL | vol 35,169 / OI 5,331
- **SPY** PUT 756 2026-11-09 (0DTE): 241 @ 6.25 = **+$151k** SELL | vol 23,617 / OI 382
- **SPY** PUT 765 2026-11-10 (1DTE): 100 @ 14.74 = **+$147k** SELL | vol 342 / OI 104
- **SPY** PUT 749 2026-11-10 (1DTE): 450 @ 3.08 = **+$139k** SELL | vol 10,800 / OI 438
- **NVDA** PUT 177.5 2026-11-13 (4DTE): 200 @ 6.50 = **+$130k** SELL | vol 6,144 / OI 1,585

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 701 2026-11-11 (2DTE): 700 traded vs OI 187
- **SPY** CALL 804 2026-11-13 (4DTE): 865 traded vs OI 741
- **SPY** PUT 753 2026-11-10 (1DTE): 529 traded vs OI 472
- **SPY** PUT 754 2026-11-10 (1DTE): 585 traded vs OI 410
- **SPY** PUT 751 2026-11-11 (2DTE): 543 traded vs OI 262
- **QQQ** CALL 676 2026-11-11 (2DTE): 526 traded vs OI 79
- **QQQ** PUT 679 2026-11-13 (4DTE): 526 traded vs OI 420
- **NVDA** CALL 170 2026-11-20 (11DTE): 1,908 traded vs OI 1,772
- **NVDA** CALL 190 2026-12-04 (25DTE): 1,144 traded vs OI 1,125
- **NVDA** CALL 160 2026-11-16 (7DTE): 513 traded vs OI 18
- **TSLA** PUT 380 2026-11-13 (4DTE): 1,777 traded vs OI 1,736
- **AAPL** PUT 325 2026-11-13 (4DTE): 1,911 traded vs OI 1,708
- **AMD** CALL 540 2026-11-13 (4DTE): 515 traded vs OI 0
- **AMD** PUT 485 2026-11-11 (2DTE): 511 traded vs OI 181
- **AMD** CALL 527.5 2026-11-09 (0DTE): 507 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
