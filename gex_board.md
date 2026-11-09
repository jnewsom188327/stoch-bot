# GEX + FLOW SCAN - Mon Nov 09, 12:40 PM ET
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
Last 1m check 12:40:08 ET, last candle SPY 12:39, QQQ 12:39 | no errors
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
| 1 | **META** | 640.88 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 37 | 11/09 645C @ 0.61 (delta 0.21) = est +89% at 644.17 | POS +$165.8M | 613.53 | 650 | 640 | -$8.2M | +$2.1M bull / +$0 bear | out (clean 32, ADX 36, RVol 0.4) |
| 2 | **IWM** | 281.48 | - | **-** | 29 | - | NEG -$935.3M | 284.95 | 285 | 270 | -$20.4M | +$107k bull / -$94k bear | out (clean 35, ADX 59, RVol 0.4) |
| 3 | **AAPL** | 349.24 | PINNED between the walls (positive gamma) - chop | **-** | 29 | - | POS +$387.7M | 339.45 | 350 | 350 | -$5.7M | +$49k bull / +$0 bear | out (clean 27, ADX 28, RVol 0.3) |
| 4 | **AVGO** | 321.36 | - | **-** | 29 | - | NEG -$66.1M | - | 340 | 320 | -$9.4M | +$0 bull / -$242k bear | out (clean 31, ADX 55, RVol 1.3) |
| 5 | **MU** | 734.01 | FLIP CROSS down into negative gamma | **PUTS** | 28 | none: 190 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (74 contracts' greeks worked out here) | NEG -$4.5M | 738.14 | 750 | 750 | -$11.8M | +$796k bull / -$192k bear | out (clean 31, ADX 32, RVol 0.2) |
| 6 | **SPY** | 752.32 | - | **-** | 27 | - | NEG -$6.3B | 761.83 | 750 | 740 | -$308.4M | +$388k bull / -$11.6M bear | out (clean 32, ADX 53, RVol 0.3) |
| 7 | **QQQ** | 677.52 | - | **-** | 26 | - | NEG -$2.3B | 698.9 | 680 | 680 | -$231.2M | +$3.2M bull / -$385k bear | out (clean 32, ADX 45, RVol 0.6) |
| 8 | **AMD** | 502.81 | - | **-** | 26 | - | POS +$23.0M | 490.91 | 500 | 500 | -$54.6M | +$661k bull / -$915k bear | out (clean 32, ADX 48, RVol 0.5) |
| 9 | **TSLA** | 377.49 | - | **-** | 25 | - | POS +$111.6M | - | 380 | 380 | -$91.5M | +$113k bull / -$71k bear | out (clean 34, ADX 33, RVol 0.3) |
| 10 | **SMH** | 485.57 | - | **-** | 23 | - | NEG -$223.5M | - | 500 | 475 | -$2.7M | +$76k bull / +$0 bear | out (clean 31, ADX 38, RVol 0.3) |
| 11 | **NVDA** | 178.06 | - | **-** | 21 | - | NEG -$183.4M | - | 190 | 190 | -$60.4M | +$1.8M bull / -$1.3M bear | out (clean 32, ADX 28, RVol 1.2) |
| 12 | **AMZN** | 268.84 | - | **-** | 21 | - | POS +$404.0M | - | 270 | 265 | +$19.6M | +$0 bull / -$34k bear | out (clean 34, ADX 13, RVol 0.3) |
| 13 | **PLTR** | 169.07 | - | **-** | 21 | - | POS +$11.3M | - | 165 | 170 | -$2.6M | +$68k bull / +$0 bear | out (clean 30, ADX 38, RVol 0.3) |
| 14 | **HOOD** | 83.98 | - | **-** | 20 | - | NEG -$1.5M | - | 85 | 85 | -$2.0M | +$27k bull / +$0 bear | out (clean 31, ADX 26, RVol 0.5) |
| 15 | **MSFT** | 543.77 | - | **-** | 18 | - | POS +$613.9M | - | 550 | 540 | +$1.4M | +$79k bull / -$174k bear | out (clean 34, ADX 32, RVol 0.4) |
| 16 | **GOOGL** | 291.20 | - | **-** | 17 | - | POS +$18.0M | 288.6 | 300 | 290 | +$4.0M | +$57k bull / +$0 bear | out (clean 31, ADX 12, RVol 0.5) |
| 17 | **ORCL** | 119.38 | - | **-** | 16 | - | NEG -$26.5M | - | 125 | 125 | -$475k | +$43k bull / +$0 bear | out (clean 30, ADX 21, RVol 0.4) |
| 18 | **COIN** | 136.90 | - | **-** | 15 | - | NEG -$6.8M | - | 140 | 135 | -$2.0M | - | out (clean 32, ADX 13, RVol 0.5) |
| 19 | **SMCI** | 29.34 | - | **-** | 13 | - | NEG -$34k | - | 30 | 30 | -$969k | - | out (clean 30, ADX 10, RVol 0.5) |
| 20 | **SHOP** | 150.92 | - | **-** | 13 | - | POS +$1.8M | - | 150 | 140 | -$91k | - | out (clean 34, ADX 22, RVol 0.1) |
| 21 | **UBER** | 70.22 | - | **-** | 12 | - | POS +$4.6M | 69.1 | 70 | 70 | -$91k | - | out (clean 31, ADX 39, RVol 1.1) |
| 22 | **DELL** | 350.95 | - | **-** | 10 | - | NEG -$6.3M | - | 350 | 340 | -$484k | - | out (clean 32, ADX 41, RVol 0.2) |
| 23 | **ARM** | 187.40 | - | **-** | 10 | - | NEG -$4.6M | - | 185 | 190 | +$290k | - | out (clean 27, ADX 38, RVol 0.5) |
| 24 | **CRM** | 215.97 | - | **-** | 10 | - | NEG -$11.2M | - | 230 | 220 | -$44k | - | out (clean 34, ADX 28, RVol 0.6) |
| 25 | **MSTR** | 125.50 | - | **-** | 8 | - | POS +$761k | 124.07 | 135 | 120 | -$2.1M | - | out (clean 30, ADX 19, RVol 0.2) |
| 26 | **BABA** | 105.55 | - | **-** | 7 | - | POS +$2.5M | 104.14 | 110 | 110 | +$97k | - | out (clean 31, ADX 31, RVol 0.2) |
| 27 | **NFLX** | 63.98 | - | **-** | 4 | - | NEG -$18.0M | 67.68 | 65 | 65 | +$15k | - | out (clean 31, ADX 17, RVol 0.5) |

## Big prints this scan (36)
- **SPY** PUT 730 2026-11-13 (4DTE): 55,626 @ 1.16 = **+$6.5M** BUY | vol 67,326 / OI 25,107
- **SPY** PUT 715 2026-11-13 (4DTE): 36,834 @ 0.44 = **+$1.6M** BUY | vol 58,936 / OI 10,487
- **QQQ** CALL 665 2026-11-09 (0DTE): 1,000 @ 12.91 = **+$1.3M** BUY | vol 23,957 / OI 3,005
- **QQQ** CALL 665 2026-11-09 (0DTE): 1,000 @ 12.90 = **+$1.3M** BUY | vol 23,957 / OI 3,005
- **SPY** PUT 715 2026-11-13 (4DTE): 18,792 @ 0.43 = **+$808k** BUY | vol 58,936 / OI 10,487
- **SPY** CALL 738 2026-11-09 (0DTE): 250 @ 14.35 = **+$359k** MID | vol 3,775 / OI 906
- **QQQ** PUT 680 2026-11-09 (0DTE): 1,000 @ 2.80 = **+$280k** SELL | vol 17,134 / OI 3,024
- **QQQ** PUT 680 2026-11-09 (0DTE): 1,000 @ 2.79 = **+$279k** SELL | vol 17,134 / OI 3,024
- **NVDA** PUT 170 2026-11-13 (4DTE): 1,000 @ 2.55 = **+$255k** BUY | vol 22,443 / OI 10,619
- **SPY** CALL 750 2026-11-10 (1DTE): 500 @ 4.82 = **+$241k** BUY | vol 31,495 / OI 8,230
- **SPY** CALL 738 2026-11-13 (4DTE): 129 @ 16.90 = **+$218k** MID | vol 551 / OI 595
- **AMD** CALL 490 2026-11-13 (4DTE): 50 @ 27.00 = **+$135k** BUY | vol 2,942 / OI 1,648
- **AMD** CALL 490 2026-11-13 (4DTE): 48 @ 26.95 = **+$129k** BUY | vol 2,942 / OI 1,648
- **NVDA** CALL 177.5 2026-11-13 (4DTE): 200 @ 5.70 = **+$114k** BUY | vol 12,339 / OI 121
- **AMD** CALL 490 2026-11-13 (4DTE): 36 @ 27.00 = **+$97k** BUY | vol 2,942 / OI 1,648

## New unusual volume (traded more than open interest, 500+)
- **IWM** PUT 280 2026-11-10 (1DTE): 3,126 traded vs OI 3,064
- **IWM** CALL 287 2026-11-11 (2DTE): 851 traded vs OI 291
- **AMD** CALL 502.5 2026-11-13 (4DTE): 506 traded vs OI 197
- **META** CALL 665 2026-11-11 (2DTE): 508 traded vs OI 70
- **MSFT** CALL 547.5 2026-11-13 (4DTE): 502 traded vs OI 206

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
