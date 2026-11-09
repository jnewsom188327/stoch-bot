# GEX + FLOW SCAN - Mon Nov 09, 11:00 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (3)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:35 | **AMZN** | **CALLS** | TREND + FLOW | 11/09 272.5C | 0.49 | 0.19 | +2% (2m) | **-61%** | +225% | 273.49 |
| 10:00 | **MSFT** | **CALLS** | TREND + FLOW | 11/09 545C | 0.77 | 0.83 | +51% (23m) | **+8%** | +545% | 550 |
| 10:00 | **AMZN** | **CALLS** | TREND + FLOW | 11/09 275C | 0.48 | 0.03 | +13% (6m) | **-94%** | +258% | 275.95 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 11:00:08 ET, last candle SPY 10:59, QQQ 10:59 | no errors

## Flow surges NOT fired - price disagreed (17 today, last 5)
- 10:55 AVGO PUTS: price +2.40 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:40 AVGO PUTS: price +1.16 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:40 QQQ PUTS: price +0.45 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:35 AVGO PUTS: price +1.05 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:30 QQQ PUTS: price +0.53 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **SMH** | 487.46 | FLOW SURGE | **PUTS** | 50 | none: 156 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (71 contracts' greeks worked out here) | NEG -$220.2M | - | 500 | 475 | -$4.1M | +$0 bull / -$139k bear | out (clean 32, ADX 47, RVol 1.5) |
| 2 | **AMD** | 500.49 | PINNED between the walls (positive gamma) - chop | **-** | 46 | - | POS +$15.4M | 486.09 | 500 | 500 | -$38.6M | +$191k bull / -$826k bear | out (clean 33, ADX 54, RVol 1.4) |
| 3 | **AMZN** | 269.36 | TREND + FLOW | **CALLS** | 46 | none: 88 calls 0-7DTE > 7 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only +6% at the target (needs +20%) (44 contracts' greeks worked out here) | POS +$394.4M | - | 270 | 265 | +$18.2M | +$441k bull / -$30k bear | LONG (clean 35, ADX 31, RVol 0.8) |
| 4 | **AVGO** | 320.25 | FLOW SURGE | **PUTS** | 46 | none: 100 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (41 contracts' greeks worked out here) | NEG -$66.8M | - | 340 | 320 | -$7.9M | +$0 bull / -$67k bear | out (clean 31, ADX 66, RVol 1.1) |
| 5 | **COIN** | 138.97 | FLOW SURGE | **PUTS** | 46 | none: 26 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$4.9M | - | 140 | 140 | -$2.3M | +$0 bull / -$300k bear | out (clean 32, ADX 26, RVol 0.8) |
| 6 | **TSLA** | 379.95 | PINNED between the walls (positive gamma) - chop | **-** | 45 | - | POS +$118.4M | - | 380 | 380 | -$96.4M | +$310k bull / -$1.5M bear | LONG (clean 35, ADX 47, RVol 0.5) |
| 7 | **QQQ** | 678.38 | FLOW SURGE | **PUTS** | 43 | none: 766 puts 0-7DTE > 65 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (253 contracts' greeks worked out here) | NEG -$2.2B | 699.88 | 680 | 680 | -$257.9M | +$119k bull / -$3.3M bear | out (clean 33, ADX 49, RVol 0.8) |
| 8 | **IWM** | 280.76 | FLOW SURGE | **PUTS** | 43 | 11/09 281P @ 0.80 (delta 0.56) = est +40% at 280 | NEG -$1.1B | 285.16 | 285 | 270 | -$16.6M | +$0 bull / -$309k bear | out (clean 33, ADX 53, RVol 0.6) |
| 9 | **SPY** | 751.73 | FLOW SURGE | **PUTS** | 42 | 11/09 749P @ 0.70 (delta 0.26) = est +42% at 750 | NEG -$6.5B | 761.89 | 750 | 740 | -$250.8M | +$138k bull / -$4.4M bear | out (clean 33, ADX 51, RVol 0.7) |
| 10 | **MU** | 739.60 | FLIP CROSS up into positive gamma | **CALLS** | 35 | none: 188 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (78 contracts' greeks worked out here) | POS +$1.7M | 737.03 | 750 | 750 | -$19.8M | +$687k bull / -$4.0M bear | out (clean 33, ADX 46, RVol 0.6) |
| 11 | **MSTR** | 128.91 | FLOW SURGE | **PUTS** | 35 | none: 25 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$4.9M | - | 135 | 135 | -$3.3M | +$0 bull / -$293k bear | out (clean 30, ADX 25, RVol 0.9) |
| 12 | **NVDA** | 179.69 | - | **-** | 30 | - | NEG -$182.5M | - | 190 | 190 | -$68.2M | +$2.2M bull / -$3.4M bear | out (clean 32, ADX 38, RVol 2.9) |
| 13 | **HOOD** | 85.03 | - | **-** | 28 | - | NEG -$1.3M | - | 85 | 85 | -$3.0M | +$367k bull / -$75k bear | out (clean 30, ADX 65, RVol 0.6) |
| 14 | **PLTR** | 169.68 | - | **-** | 27 | - | POS +$11.1M | - | 165 | 180 | -$3.1M | +$0 bull / -$374k bear | out (clean 30, ADX 48, RVol 0.9) |
| 15 | **AAPL** | 351.04 | - | **-** | 24 | - | POS +$471.7M | 338.44 | 350 | 350 | -$9.4M | +$841k bull / -$560k bear | out (clean 28, ADX 42, RVol 0.5) |
| 16 | **META** | 641.97 | - | **-** | 23 | - | POS +$164.1M | 615.95 | 650 | 640 | -$7.9M | +$136k bull / -$382k bear | out (clean 33, ADX 42, RVol 0.7) |
| 17 | **GOOGL** | 293.45 | - | **-** | 22 | - | POS +$23.6M | 289 | 300 | 290 | +$2.4M | +$28k bull / +$0 bear | out (clean 31, ADX 33, RVol 1.2) |
| 18 | **MSFT** | 542.70 | - | **-** | 21 | - | POS +$585.1M | - | 550 | 540 | +$2.3M | +$0 bull / -$91k bear | out (clean 34, ADX 34, RVol 0.6) |
| 19 | **ORCL** | 119.76 | - | **-** | 21 | - | NEG -$26.2M | - | 125 | 125 | -$732k | +$46k bull / +$0 bear | out (clean 30, ADX 34, RVol 0.5) |
| 20 | **SMCI** | 29.66 | - | **-** | 18 | - | NEG -$23k | - | 30 | 30 | -$1.0M | - | out (clean 31, ADX 18, RVol 0.6) |
| 21 | **DELL** | 352.99 | - | **-** | 17 | - | NEG -$5.8M | - | 350 | 340 | -$971k | - | out (clean 32, ADX 49, RVol 0.7) |
| 22 | **ARM** | 189.77 | - | **-** | 11 | - | NEG -$4.1M | - | 185 | 190 | -$23k | - | out (clean 27, ADX 53, RVol 1.6) |
| 23 | **UBER** | 69.42 | - | **-** | 8 | - | POS +$896k | 69.31 | 70 | 65 | -$35k | - | out (clean 30, ADX 25, RVol 0.7) |
| 24 | **CRM** | 215.09 | - | **-** | 8 | - | NEG -$11.4M | - | 195 | 220 | +$15k | - | out (clean 34, ADX 21, RVol 0.8) |
| 25 | **BABA** | 105.80 | - | **-** | 8 | - | POS +$3.1M | 104.09 | 110 | 110 | +$34k | - | out (clean 31, ADX 34, RVol 0.7) |
| 26 | **NFLX** | 63.74 | - | **-** | 7 | - | NEG -$19.0M | - | 65 | 65 | +$97k | - | out (clean 31, ADX 19, RVol 0.8) |
| 27 | **SHOP** | 150.46 | - | **-** | 7 | - | POS +$1.8M | - | 150 | 140 | -$25k | - | out (clean 34, ADX 14, RVol 0.3) |

## Big prints this scan (90)
- **AAPL** CALL 350 2026-11-13 (4DTE): 1,000 @ 5.00 = **+$500k** BUY | vol 5,406 / OI 4,089
- **SPY** PUT 744 2026-11-12 (3DTE): 1,000 @ 3.64 = **+$364k** BUY | vol 9,341 / OI 211
- **NVDA** PUT 177.5 2026-11-16 (7DTE): 500 @ 5.60 = **+$280k** BUY | vol 1,850 / OI 123
- **SPY** PUT 756 2026-11-09 (0DTE): 399 @ 6.08 = **+$243k** BUY | vol 9,662 / OI 382
- **MU** CALL 730 2026-11-09 (0DTE): 299 @ 7.45 = **+$223k** SELL | vol 16,497 / OI 259
- **SPY** PUT 756 2026-11-09 (0DTE): 300 @ 6.57 = **+$197k** BUY | vol 9,662 / OI 382
- **SPY** PUT 756 2026-11-09 (0DTE): 300 @ 6.43 = **+$193k** BUY | vol 9,662 / OI 382
- **MU** PUT 722.5 2026-11-13 (4DTE): 75 @ 25.30 = **+$190k** BUY | vol 147 / OI 515
- **QQQ** PUT 675 2026-11-09 (0DTE): 800 @ 2.04 = **+$163k** BUY | vol 31,361 / OI 1,826
- **SPY** PUT 756 2026-11-09 (0DTE): 231 @ 6.28 = **+$145k** BUY | vol 9,662 / OI 382
- **QQQ** CALL 674 2026-11-09 (0DTE): 496 @ 2.80 = **+$139k** SELL | vol 79,961 / OI 2,191
- **QQQ** CALL 674 2026-11-09 (0DTE): 493 @ 2.65 = **+$131k** SELL | vol 79,961 / OI 2,191
- **AAPL** CALL 350 2026-11-11 (2DTE): 300 @ 3.95 = **+$118k** BUY | vol 8,762 / OI 705
- **SPY** PUT 730 2026-11-12 (3DTE): 1,000 @ 1.18 = **+$118k** BUY | vol 9,316 / OI 1,056
- **QQQ** CALL 674 2026-11-09 (0DTE): 403 @ 2.85 = **+$115k** SELL | vol 79,961 / OI 2,191

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 769 2026-11-11 (2DTE): 714 traded vs OI 709
- **SPY** PUT 721 2026-11-11 (2DTE): 522 traded vs OI 229
- **SPY** PUT 747 2026-11-12 (3DTE): 538 traded vs OI 183
- **SPY** CALL 762 2026-11-12 (3DTE): 567 traded vs OI 560
- **SPY** CALL 751 2026-11-16 (7DTE): 602 traded vs OI 306
- **QQQ** PUT 681 2026-11-09 (0DTE): 631 traded vs OI 407
- **QQQ** PUT 644 2026-11-10 (1DTE): 504 traded vs OI 234
- **QQQ** CALL 696 2026-11-13 (4DTE): 9,929 traded vs OI 285
- **QQQ** CALL 745 2026-11-16 (7DTE): 1,746 traded vs OI 0
- **QQQ** CALL 674 2026-11-13 (4DTE): 505 traded vs OI 163
- **QQQ** CALL 703 2026-11-13 (4DTE): 10,061 traded vs OI 1,047
- **QQQ** CALL 691 2026-11-20 (11DTE): 564 traded vs OI 557
- **NVDA** CALL 197.5 2026-11-20 (11DTE): 500 traded vs OI 0
- **NVDA** CALL 182.5 2026-11-20 (11DTE): 524 traded vs OI 0
- **TSLA** PUT 352.5 2026-11-11 (2DTE): 564 traded vs OI 170

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
