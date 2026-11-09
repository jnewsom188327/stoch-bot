# GEX + FLOW SCAN - Mon Nov 09, 10:35 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (3)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:35 | **AMZN** | **CALLS** | TREND + FLOW | 11/09 272.5C | 0.49 | 0.43 | -12% (0m) | **-12%** | +225% | 273.49 |
| 10:00 | **MSFT** | **CALLS** | TREND + FLOW | 11/09 545C | 0.77 | 0.58 | +51% (23m) | **-25%** | +545% | 550 |
| 10:00 | **AMZN** | **CALLS** | TREND + FLOW | 11/09 275C | 0.48 | 0.12 | +13% (6m) | **-75%** | +258% | 275.95 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:35:08 ET, last candle SPY 10:34, QQQ 10:34 | no errors

## Flow surges NOT fired - price disagreed (14 today, last 5)
- 10:35 AVGO PUTS: price +1.05 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:30 QQQ PUTS: price +0.53 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:25 SMCI PUTS: price +0.08 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:20 SMCI PUTS: price +0.50 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:15 SPY PUTS: price +0.94 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **AMZN** | 270.12 | TREND + FLOW | **CALLS** | 51 | 11/09 272.5C @ 0.49 (delta 0.24) = est +225% at 273.49 | POS +$401.5M | - | 270 | 265 | +$15.4M | +$377k bull / +$0 bear | LONG (clean 35, ADX 37, RVol 1.1) |
| 2 | **AVGO** | 316.93 | FLOW SURGE | **PUTS** | 48 | 11/09 312.5P @ 0.72 (delta 0.21) = est +156% at 312.5 | NEG -$66.3M | - | 340 | 320 | -$6.3M | +$152k bull / -$251k bear | out (clean 30, ADX 58, RVol 1.6) |
| 3 | **QQQ** | 675.08 | FLOW SURGE | **PUTS** | 47 | none: 775 puts 0-7DTE > 60 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (244 contracts' greeks worked out here) | NEG -$2.2B | 700.4 | 680 | 680 | -$228.2M | +$0 bull / -$2.7M bear | out (clean 32, ADX 44, RVol 1.2) |
| 4 | **META** | 638.66 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 47 | none: 208 calls 0-7DTE > 10 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (85 contracts' greeks worked out here) | POS +$149.0M | 614.76 | 650 | 640 | -$4.5M | +$510k bull / -$230k bear | out (clean 33, ADX 44, RVol 1.6) |
| 5 | **SMH** | 482.52 | FLOW SURGE | **PUTS** | 46 | none: 156 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (68 contracts' greeks worked out here) | NEG -$235.3M | - | 500 | 475 | -$3.5M | +$0 bull / -$288k bear | out (clean 31, ADX 44, RVol 1.0) |
| 6 | **IWM** | 279.88 | FLOW SURGE | **PUTS** | 43 | 11/09 280P @ 0.77 (delta 0.52) = est +54% at 279 | NEG -$1.3B | 285.18 | 285 | 270 | -$12.8M | +$0 bull / -$104k bear | out (clean 33, ADX 46, RVol 0.8) |
| 7 | **SPY** | 749.46 | FLOW SURGE | **PUTS** | 42 | 11/09 746P @ 0.62 (delta 0.23) = est +103% at 746.66 | NEG -$7.1B | 761.88 | 750 | 740 | -$206.7M | +$0 bull / -$5.6M bear | out (clean 32, ADX 43, RVol 0.7) |
| 8 | **TSLA** | 378.10 | FLOW SURGE | **PUTS** | 41 | none: 120 puts 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (52 contracts' greeks worked out here) | POS +$115.6M | - | 380 | 380 | -$90.1M | +$44k bull / -$2.1M bear | LONG (clean 35, ADX 44, RVol 0.7) |
| 9 | **SHOP** | 150.34 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 40 | none: 21 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$1.5M | - | 150 | 140 | -$68k | - | out (clean 34, ADX 17, RVol 0.7) |
| 10 | **AAPL** | 350.40 | PINNED between the walls (positive gamma) - chop | **-** | 38 | - | POS +$456.1M | 337.88 | 350 | 350 | -$9.3M | +$0 bull / -$5.0M bear | out (clean 27, ADX 36, RVol 0.8) |
| 11 | **MSFT** | 541.51 | TREND + FLOW | **CALLS** | 35 | 11/09 545C @ 0.67 (delta 0.24) = est +645% at 550 | POS +$575.7M | - | 550 | 540 | +$3.1M | +$0 bull / -$115k bear | LONG (clean 34, ADX 32, RVol 0.9) |
| 12 | **NVDA** | 179.62 | - | **-** | 31 | - | NEG -$178.2M | - | 190 | 190 | -$69.3M | +$954k bull / -$2.6M bear | out (clean 32, ADX 39, RVol 3.6) |
| 13 | **AMD** | 491.54 | - | **-** | 30 | - | POS +$2.7M | 489.23 | 500 | 500 | -$36.8M | +$86k bull / -$3.1M bear | out (clean 33, ADX 52, RVol 1.6) |
| 14 | **HOOD** | 85.09 | - | **-** | 30 | - | NEG -$1.2M | - | 85 | 85 | -$2.8M | +$25k bull / -$329k bear | out (clean 30, ADX 63, RVol 0.9) |
| 15 | **DELL** | 349.67 | - | **-** | 29 | - | NEG -$6.3M | - | 350 | 340 | -$843k | +$0 bull / -$28k bear | out (clean 32, ADX 45, RVol 1.2) |
| 16 | **MSTR** | 128.94 | - | **-** | 27 | - | POS +$4.6M | - | 135 | 135 | -$2.3M | +$0 bull / -$503k bear | out (clean 29, ADX 26, RVol 1.5) |
| 17 | **PLTR** | 168.35 | - | **-** | 25 | - | POS +$10.7M | - | 165 | 170 | -$2.4M | +$0 bull / -$29k bear | out (clean 29, ADX 44, RVol 0.6) |
| 18 | **COIN** | 137.62 | - | **-** | 23 | - | NEG -$6.4M | - | 140 | 135 | -$1.4M | - | out (clean 31, ADX 20, RVol 0.5) |
| 19 | **SMCI** | 29.53 | - | **-** | 21 | - | NEG -$62k | - | 30 | 30 | -$993k | - | out (clean 31, ADX 24, RVol 0.8) |
| 20 | **GOOGL** | 294.05 | - | **-** | 20 | - | POS +$22.3M | 290.5 | 300 | 290 | +$1.3M | +$154k bull / +$0 bear | out (clean 32, ADX 35, RVol 1.0) |
| 21 | **MU** | 732.03 | - | **-** | 20 | - | NEG -$11.9M | - | 750 | 750 | -$8.1M | +$3.5M bull / -$4.7M bear | out (clean 32, ADX 41, RVol 0.7) |
| 22 | **BABA** | 106.20 | - | **-** | 20 | - | POS +$4.6M | 103.53 | 110 | 110 | -$82k | +$0 bull / -$28k bear | out (clean 31, ADX 33, RVol 1.4) |
| 23 | **ORCL** | 119.14 | - | **-** | 19 | - | NEG -$26.3M | - | 125 | 125 | -$230k | +$0 bull / -$266k bear | out (clean 30, ADX 36, RVol 0.5) |
| 24 | **ARM** | 187.10 | - | **-** | 11 | - | NEG -$4.4M | - | 185 | 190 | +$33k | - | out (clean 26, ADX 47, RVol 1.2) |
| 25 | **NFLX** | 63.58 | - | **-** | 10 | - | NEG -$19.9M | - | 65 | 65 | +$163k | - | out (clean 32, ADX 22, RVol 0.8) |
| 26 | **CRM** | 214.92 | - | **-** | 7 | - | NEG -$11.0M | - | 195 | 220 | -$11k | - | out (clean 34, ADX 23, RVol 0.4) |
| 27 | **UBER** | 69.08 | - | **-** | 5 | - | NEG -$1.1M | 69.37 | 70 | 65 | -$5k | - | out (clean 30, ADX 22, RVol 0.5) |

## Big prints this scan (169)
- **MU** CALL 720 2026-11-13 (4DTE): 200 @ 36.13 = **+$723k** BUY | vol 1,195 / OI 408
- **AMD** CALL 510 2026-11-13 (4DTE): 499 @ 11.00 = **+$549k** SELL | vol 1,661 / OI 452
- **AAPL** CALL 345 2026-11-09 (0DTE): 1,000 @ 4.89 = **+$489k** SELL | vol 9,098 / OI 1,909
- **AAPL** CALL 345 2026-11-09 (0DTE): 1,000 @ 4.88 = **+$488k** SELL | vol 9,098 / OI 1,909
- **SPY** PUT 744 2026-11-12 (3DTE): 1,000 @ 4.06 = **+$406k** BUY | vol 7,206 / OI 211
- **AAPL** CALL 345 2026-11-09 (0DTE): 733 @ 4.89 = **+$358k** SELL | vol 9,098 / OI 1,909
- **MU** CALL 760 2026-11-13 (4DTE): 200 @ 17.18 = **+$344k** BUY | vol 487 / OI 923
- **AAPL** CALL 345 2026-11-09 (0DTE): 700 @ 4.89 = **+$342k** SELL | vol 9,098 / OI 1,909
- **AMD** PUT 485 2026-11-13 (4DTE): 187 @ 16.75 = **+$313k** BUY | vol 1,417 / OI 518
- **AAPL** CALL 347.5 2026-11-09 (0DTE): 1,000 @ 2.80 = **+$280k** SELL | vol 14,575 / OI 909
- **AAPL** CALL 347.5 2026-11-09 (0DTE): 1,000 @ 2.78 = **+$278k** SELL | vol 14,575 / OI 909
- **NVDA** CALL 177.5 2026-11-13 (4DTE): 352 @ 6.35 = **+$224k** SELL | vol 6,528 / OI 121
- **SPY** PUT 756 2026-11-09 (0DTE): 300 @ 7.41 = **+$222k** BUY | vol 6,345 / OI 382
- **SPY** PUT 756 2026-11-09 (0DTE): 300 @ 7.18 = **+$215k** BUY | vol 6,345 / OI 382
- **SPY** PUT 756 2026-11-09 (0DTE): 300 @ 7.13 = **+$214k** BUY | vol 6,345 / OI 382

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 742 2026-11-12 (3DTE): 510 traded vs OI 167
- **SPY** CALL 750 2026-11-16 (7DTE): 935 traded vs OI 843
- **SPY** CALL 748 2026-11-16 (7DTE): 559 traded vs OI 264
- **SPY** CALL 760 2026-11-18 (9DTE): 771 traded vs OI 146
- **SPY** PUT 750 2026-12-04 (25DTE): 1,615 traded vs OI 882
- **QQQ** PUT 671 2026-11-11 (2DTE): 515 traded vs OI 168
- **QQQ** PUT 634 2026-11-09 (0DTE): 525 traded vs OI 0
- **QQQ** PUT 671 2026-11-10 (1DTE): 1,408 traded vs OI 1,264
- **QQQ** CALL 705 2026-11-12 (3DTE): 920 traded vs OI 710
- **QQQ** PUT 673 2026-11-11 (2DTE): 522 traded vs OI 96
- **QQQ** CALL 683 2026-11-11 (2DTE): 501 traded vs OI 105
- **QQQ** PUT 679 2026-11-09 (0DTE): 590 traded vs OI 139
- **QQQ** CALL 681 2026-11-11 (2DTE): 529 traded vs OI 260
- **QQQ** PUT 643 2026-11-10 (1DTE): 522 traded vs OI 155
- **QQQ** PUT 675 2026-11-10 (1DTE): 768 traded vs OI 738

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
