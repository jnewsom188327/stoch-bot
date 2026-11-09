# GEX + FLOW SCAN - Mon Nov 09, 11:40 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (4)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:04 | **SPY** | **CALLS** | 1m WHIPSAW (R1) | 11/09 754C | 0.41 | 0.16 | -2% (0m) | **-61%** | +28% | 752.23 |
| 10:35 | **AMZN** | **CALLS** | TREND + FLOW | 11/09 272.5C | 0.49 | 0.05 | +2% (2m) | **-90%** (done) | +225% | 273.49 |
| 10:00 | **MSFT** | **CALLS** | TREND + FLOW | 11/09 545C | 0.77 | 0.72 | +51% (23m) | **-6%** (done) | +545% | 550 |
| 10:00 | **AMZN** | **CALLS** | TREND + FLOW | 11/09 275C | 0.48 | 0.02 | +13% (6m) | **-96%** (done) | +258% | 275.95 |

## 1m RULES on SPY / QQQ - loose (1 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 11:40:08 ET, last candle SPY 11:39, QQQ 11:39 | no errors
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
| 1 | **META** | 640.36 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 40 | none: 204 calls 0-7DTE > 9 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (81 contracts' greeks worked out here) | POS +$158.6M | 614.23 | 650 | 640 | -$6.1M | +$0 bull / -$189k bear | out (clean 32, ADX 37, RVol 0.8) |
| 2 | **AAPL** | 349.69 | PINNED between the walls (positive gamma) - chop | **-** | 34 | - | POS +$415.3M | 338.95 | 350 | 350 | -$5.5M | +$586k bull / +$0 bear | out (clean 28, ADX 38, RVol 0.7) |
| 3 | **TSLA** | 376.59 | - | **-** | 28 | - | POS +$109.4M | - | 380 | 380 | -$88.0M | +$683k bull / -$117k bear | out (clean 34, ADX 42, RVol 0.5) |
| 4 | **PLTR** | 168.59 | - | **-** | 28 | - | POS +$11.0M | - | 165 | 180 | -$4.3M | +$26k bull / +$0 bear | out (clean 30, ADX 49, RVol 0.8) |
| 5 | **SPY** | 749.74 | - | **-** | 27 | - | NEG -$6.8B | 761.46 | 750 | 740 | -$219.6M | +$5.8M bull / -$712k bear | out (clean 32, ADX 49, RVol 0.7) |
| 6 | **AVGO** | 316.79 | - | **-** | 27 | - | NEG -$66.0M | - | 340 | 320 | -$5.8M | +$312k bull / +$0 bear | out (clean 31, ADX 62, RVol 1.3) |
| 7 | **QQQ** | 675.14 | - | **-** | 26 | - | NEG -$2.2B | 699 | 680 | 680 | -$190.2M | +$1.5M bull / -$239k bear | out (clean 32, ADX 46, RVol 0.5) |
| 8 | **AMD** | 497.11 | - | **-** | 26 | - | POS +$7.2M | 491.94 | 500 | 500 | -$43.5M | +$2.5M bull / +$0 bear | out (clean 32, ADX 54, RVol 0.7) |
| 9 | **NVDA** | 174.81 | - | **-** | 25 | - | NEG -$180.6M | - | 190 | 190 | -$26.0M | +$4.4M bull / +$0 bear | out (clean 32, ADX 44, RVol 4.5) |
| 10 | **HOOD** | 83.93 | - | **-** | 24 | - | NEG -$1.5M | - | 85 | 85 | -$2.0M | +$29k bull / +$0 bear | out (clean 31, ADX 48, RVol 0.6) |
| 11 | **SMH** | 481.59 | - | **-** | 23 | - | NEG -$235.2M | - | 500 | 475 | -$1.8M | +$352k bull / +$0 bear | out (clean 31, ADX 40, RVol 0.8) |
| 12 | **GOOGL** | 291.13 | - | **-** | 21 | - | POS +$11.0M | 289.38 | 300 | 290 | +$4.3M | +$193k bull / +$0 bear | out (clean 31, ADX 23, RVol 1.0) |
| 13 | **IWM** | 280.81 | - | **-** | 20 | - | NEG -$1.1B | 285 | 285 | 270 | -$19.2M | - | out (clean 34, ADX 59, RVol 0.6) |
| 14 | **MSFT** | 542.03 | - | **-** | 20 | - | POS +$582.8M | - | 550 | 540 | +$2.9M | +$0 bull / -$98k bear | out (clean 34, ADX 28, RVol 0.4) |
| 15 | **MSTR** | 125.57 | - | **-** | 20 | - | POS +$956k | 123.63 | 135 | 120 | -$2.2M | +$27k bull / +$0 bear | out (clean 30, ADX 20, RVol 0.7) |
| 16 | **MU** | 731.23 | - | **-** | 19 | - | NEG -$7.7M | - | 750 | 750 | -$3.5M | +$3.5M bull / +$0 bear | out (clean 32, ADX 45, RVol 0.4) |
| 17 | **COIN** | 136.81 | - | **-** | 17 | - | NEG -$6.6M | - | 140 | 135 | -$1.9M | - | out (clean 32, ADX 24, RVol 0.5) |
| 18 | **ORCL** | 118.13 | - | **-** | 16 | - | NEG -$26.5M | - | 125 | 120 | -$41k | +$374k bull / +$0 bear | out (clean 30, ADX 25, RVol 0.6) |
| 19 | **AMZN** | 268.87 | - | **-** | 14 | - | POS +$393.2M | - | 270 | 265 | +$20.7M | - | out (clean 35, ADX 18, RVol 0.6) |
| 20 | **SMCI** | 29.28 | - | **-** | 14 | - | NEG -$44k | - | 30 | 30 | -$867k | - | out (clean 30, ADX 11, RVol 0.7) |
| 21 | **UBER** | 69.61 | - | **-** | 14 | - | POS +$2.1M | 69.15 | 70 | 70 | -$144k | - | out (clean 31, ADX 31, RVol 0.9) |
| 22 | **BABA** | 105.36 | - | **-** | 13 | - | POS +$1.8M | 104.34 | 110 | 110 | +$285k | - | out (clean 32, ADX 39, RVol 1.4) |
| 23 | **ARM** | 188.09 | - | **-** | 12 | - | NEG -$4.5M | - | 185 | 190 | +$219k | - | out (clean 27, ADX 50, RVol 1.2) |
| 24 | **DELL** | 348.80 | - | **-** | 11 | - | NEG -$6.3M | - | 350 | 340 | -$292k | - | out (clean 32, ADX 47, RVol 0.4) |
| 25 | **SHOP** | 150.57 | - | **-** | 9 | - | POS +$1.9M | - | 150 | 140 | -$50k | - | out (clean 35, ADX 15, RVol 0.1) |
| 26 | **NFLX** | 63.71 | - | **-** | 7 | - | NEG -$19.1M | 67.45 | 65 | 65 | +$134k | - | out (clean 31, ADX 18, RVol 0.7) |
| 27 | **CRM** | 214.31 | - | **-** | 7 | - | NEG -$10.8M | - | 195 | 220 | +$21k | - | out (clean 34, ADX 17, RVol 0.8) |

## Big prints this scan (83)
- **SPY** PUT 756 2026-11-09 (0DTE): 972 @ 6.00 = **+$583k** SELL | vol 28,780 / OI 382
- **MU** CALL 700 2026-11-13 (4DTE): 110 @ 51.00 = **+$561k** BUY | vol 961 / OI 556
- **AMD** CALL 505 2026-11-16 (7DTE): 200 @ 19.20 = **+$384k** BUY | vol 454 / OI 20
- **QQQ** PUT 670 2026-11-13 (4DTE): 500 @ 6.57 = **+$328k** MID | vol 6,716 / OI 4,388
- **SPY** PUT 756 2026-11-09 (0DTE): 489 @ 6.10 = **+$298k** SELL | vol 28,780 / OI 382
- **QQQ** PUT 691 2026-11-09 (0DTE): 193 @ 14.77 = **+$285k** SELL | vol 478 / OI 216
- **SPY** PUT 756 2026-11-09 (0DTE): 463 @ 6.00 = **+$278k** SELL | vol 28,780 / OI 382
- **SPY** PUT 747 2026-11-13 (4DTE): 500 @ 5.06 = **+$253k** BUY | vol 2,672 / OI 1,786
- **QQQ** PUT 650 2026-11-13 (4DTE): 1,000 @ 2.39 = **+$239k** BUY | vol 5,613 / OI 61,638
- **NVDA** PUT 180 2026-11-09 (0DTE): 500 @ 4.05 = **+$202k** SELL | vol 37,025 / OI 5,331
- **SPY** PUT 756 2026-11-09 (0DTE): 317 @ 6.17 = **+$196k** BUY | vol 28,780 / OI 382
- **SPY** PUT 756 2026-11-09 (0DTE): 280 @ 6.00 = **+$168k** SELL | vol 28,780 / OI 382
- **SPY** PUT 730 2026-11-13 (4DTE): 1,000 @ 1.59 = **+$159k** BUY | vol 10,042 / OI 25,107
- **MU** CALL 725 2026-11-09 (0DTE): 120 @ 13.00 = **+$156k** BUY | vol 9,272 / OI 233
- **SPY** PUT 756 2026-11-09 (0DTE): 241 @ 6.00 = **+$145k** SELL | vol 28,780 / OI 382

## New unusual volume (traded more than open interest, 500+)
- **QQQ** PUT 678 2026-11-11 (2DTE): 509 traded vs OI 87
- **QQQ** PUT 619 2026-11-09 (0DTE): 500 traded vs OI 0
- **QQQ** PUT 632 2026-11-20 (11DTE): 3,319 traded vs OI 0
- **QQQ** PUT 676 2026-11-20 (11DTE): 3,309 traded vs OI 1,436
- **QQQ** PUT 642 2026-11-20 (11DTE): 5,014 traded vs OI 0
- **QQQ** PUT 617 2026-11-20 (11DTE): 3,202 traded vs OI 0
- **IWM** CALL 288 2026-11-11 (2DTE): 1,082 traded vs OI 155
- **IWM** PUT 277 2026-11-27 (18DTE): 1,365 traded vs OI 801
- **NVDA** PUT 165 2026-12-04 (25DTE): 981 traded vs OI 964
- **NVDA** CALL 177.5 2026-11-27 (18DTE): 512 traded vs OI 0
- **AAPL** PUT 340 2026-11-18 (9DTE): 507 traded vs OI 87
- **AMD** CALL 500 2026-11-27 (18DTE): 510 traded vs OI 454
- **META** CALL 645 2026-11-13 (4DTE): 613 traded vs OI 560
- **MSFT** PUT 520 2026-11-09 (0DTE): 964 traded vs OI 949
- **GOOGL** PUT 280 2026-11-09 (0DTE): 522 traded vs OI 363

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
