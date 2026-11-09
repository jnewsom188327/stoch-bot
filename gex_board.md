# GEX + FLOW SCAN - Mon Nov 09, 10:20 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (2)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:00 | **MSFT** | **CALLS** | TREND + FLOW | 11/09 545C | 0.77 | 1.01 | +31% (20m) | **+31%** | +545% | 550 |
| 10:00 | **AMZN** | **CALLS** | TREND + FLOW | 11/09 275C | 0.48 | 0.20 | +13% (6m) | **-58%** | +258% | 275.95 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:20:08 ET, last candle SPY 10:19, QQQ 10:19 | no errors

## Flow surges NOT fired - price disagreed (11 today, last 5)
- 10:20 SMCI PUTS: price +0.50 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:15 SPY PUTS: price +0.94 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:10 SMCI PUTS: price +0.22 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:10 IWM PUTS: price +0.10 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:10 SPY PUTS: price +0.55 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **META** | 640.91 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 64 | none: 208 calls 0-7DTE > 10 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (89 contracts' greeks worked out here) | POS +$174.1M | 611.89 | 650 | 640 | -$5.1M | +$882k bull / -$476k bear | LONG (clean 33, ADX 44, RVol 1.9) |
| 2 | **AVGO** | 315.88 | FLOW SURGE | **PUTS** | 56 | none: 100 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (47 contracts' greeks worked out here) | NEG -$68.8M | - | 340 | 320 | -$6.1M | +$0 bull / -$328k bear | out (clean 30, ADX 51, RVol 2.5) |
| 3 | **NVDA** | 178.76 | FLOW SURGE | **PUTS** | 55 | none: 56 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (23 contracts' greeks worked out here) | NEG -$168.6M | - | 190 | 190 | -$66.7M | +$426k bull / -$5.6M bear | out (clean 32, ADX 38, RVol 5.5) |
| 4 | **AMZN** | 270.46 | TREND + FLOW | **CALLS** | 53 | 11/09 272.5C @ 0.73 (delta 0.30) = est +184% at 273.95 | POS +$415.2M | - | 270 | 265 | +$12.4M | +$1.2M bull / +$0 bear | LONG (clean 35, ADX 40, RVol 1.4) |
| 5 | **AMD** | 491.70 | FLIP CROSS up into positive gamma | **CALLS** | 52 | none: 156 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (73 contracts' greeks worked out here) | POS +$505k | 491.57 | 500 | 500 | -$29.8M | +$2.3M bull / -$3.7M bear | out (clean 32, ADX 48, RVol 2.1) |
| 6 | **SMH** | 481.67 | FLOW SURGE | **PUTS** | 50 | none: 152 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (61 contracts' greeks worked out here) | NEG -$241.4M | - | 500 | 475 | -$3.5M | +$0 bull / -$482k bear | out (clean 31, ADX 40, RVol 1.4) |
| 7 | **MSFT** | 541.79 | TREND + FLOW | **CALLS** | 50 | none: 172 calls 0-7DTE > 9 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (95 contracts' greeks worked out here) | POS +$583.5M | - | 550 | 540 | +$3.8M | +$30k bull / +$0 bear | LONG (clean 34, ADX 31, RVol 1.0) |
| 8 | **QQQ** | 674.68 | FLOW SURGE | **PUTS** | 49 | none: 775 puts 0-7DTE > 60 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (255 contracts' greeks worked out here) | NEG -$2.2B | 699.3 | 680 | 680 | -$191.1M | +$0 bull / -$3.5M bear | out (clean 32, ADX 39, RVol 1.6) |
| 9 | **SMCI** | 29.59 | FLOW SURGE | **PUTS** | 48 | 11/13 27.5P @ 0.56 (delta 0.24) = est +31% at 28.79 | NEG -$35k | - | 30 | 30 | -$1.1M | +$0 bull / -$48k bear | out (clean 31, ADX 27, RVol 0.8) |
| 10 | **IWM** | 279.35 | FLOW SURGE | **PUTS** | 47 | none: 314 puts 0-7DTE > 22 priced 0.40-0.80 > 3 delta 0.2+ > 3 spread ok > 3 liquid > best one only +8% at the target (needs +20%) (133 contracts' greeks worked out here) | NEG -$1.3B | 284.93 | 285 | 270 | -$12.0M | +$51k bull / -$309k bear | out (clean 32, ADX 42, RVol 1.2) |
| 11 | **SPY** | 749.02 | FLOW SURGE | **PUTS** | 44 | 11/09 745P @ 0.62 (delta 0.21) = est +110% at 745.92 | NEG -$7.2B | 761.86 | 750 | 740 | -$187.2M | +$0 bull / -$8.8M bear | out (clean 32, ADX 38, RVol 1.0) |
| 12 | **TSLA** | 377.73 | FLOW SURGE | **PUTS** | 44 | none: 124 puts 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (62 contracts' greeks worked out here) | POS +$101.9M | - | 400 | 380 | -$81.0M | +$1.2M bull / -$2.6M bear | LONG (clean 35, ADX 42, RVol 1.0) |
| 13 | **COIN** | 137.08 | FLOW SURGE | **PUTS** | 43 | none: 27 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$6.2M | - | 140 | 135 | -$1.2M | +$0 bull / -$79k bear | out (clean 31, ADX 18, RVol 0.6) |
| 14 | **AAPL** | 349.81 | PINNED between the walls (positive gamma) - chop | **-** | 32 | - | POS +$412.5M | 338.97 | 350 | 350 | +$82k | +$126k bull / -$506k bear | out (clean 27, ADX 32, RVol 0.9) |
| 15 | **HOOD** | 85.11 | - | **-** | 30 | - | NEG -$1.4M | - | 85 | 85 | -$2.1M | +$0 bull / -$699k bear | out (clean 30, ADX 58, RVol 1.3) |
| 16 | **MSTR** | 128.08 | - | **-** | 27 | - | POS +$4.3M | - | 135 | 135 | -$1.9M | +$0 bull / -$66k bear | out (clean 30, ADX 29, RVol 1.4) |
| 17 | **PLTR** | 167.70 | - | **-** | 26 | - | POS +$10.8M | - | 165 | 170 | -$2.5M | +$773k bull / -$128k bear | out (clean 29, ADX 40, RVol 1.0) |
| 18 | **ORCL** | 118.94 | - | **-** | 24 | - | NEG -$26.0M | - | 125 | 125 | -$574k | +$0 bull / -$221k bear | out (clean 29, ADX 34, RVol 0.7) |
| 19 | **DELL** | 347.52 | - | **-** | 22 | - | NEG -$6.0M | - | 350 | 340 | -$814k | - | out (clean 31, ADX 40, RVol 1.5) |
| 20 | **MU** | 728.79 | - | **-** | 21 | - | NEG -$10.9M | - | 750 | 750 | -$12.4M | +$130k bull / -$6.6M bear | out (clean 32, ADX 36, RVol 1.2) |
| 21 | **ARM** | 187.09 | - | **-** | 20 | - | NEG -$4.5M | - | 185 | 190 | +$13k | +$0 bull / -$45k bear | out (clean 26, ADX 43, RVol 1.2) |
| 22 | **GOOGL** | 294.15 | - | **-** | 19 | - | POS +$28.7M | 289.96 | 300 | 290 | -$108k | +$68k bull / -$1.1M bear | out (clean 32, ADX 34, RVol 1.3) |
| 23 | **BABA** | 105.87 | - | **-** | 17 | - | POS +$3.4M | 103.87 | 110 | 110 | +$348k | - | out (clean 32, ADX 32, RVol 2.0) |
| 24 | **CRM** | 214.41 | - | **-** | 16 | - | NEG -$10.8M | - | 195 | 220 | +$27k | - | out (clean 34, ADX 22, RVol 0.5) |
| 25 | **SHOP** | 150.47 | - | **-** | 16 | - | POS +$1.9M | - | 150 | 140 | -$14k | - | out (clean 34, ADX 16, RVol 0.5) |
| 26 | **NFLX** | 63.70 | - | **-** | 13 | - | NEG -$21.1M | - | 65 | 65 | +$138k | - | out (clean 32, ADX 25, RVol 1.9) |
| 27 | **UBER** | 69.02 | - | **-** | 6 | - | NEG -$1.3M | 69.38 | 70 | 65 | +$5k | - | out (clean 31, ADX 24, RVol 0.6) |

## Big prints this scan (147)
- **TSLA** PUT 380 2026-11-13 (4DTE): 500 @ 11.10 = **+$555k** BUY | vol 916 / OI 1,736
- **SPY** CALL 725 2026-11-10 (1DTE): 225 @ 23.10 = **+$520k** SELL | vol 232 / OI 266
- **SPY** CALL 727 2026-11-10 (1DTE): 225 @ 21.17 = **+$476k** SELL | vol 236 / OI 256
- **AMD** CALL 505 2026-11-13 (4DTE): 366 @ 12.11 = **+$443k** SELL | vol 1,166 / OI 548
- **TSLA** CALL 380 2026-11-13 (4DTE): 500 @ 8.35 = **+$418k** SELL | vol 2,401 / OI 2,522
- **SPY** PUT 756 2026-11-09 (0DTE): 490 @ 7.82 = **+$383k** BUY | vol 1,931 / OI 382
- **AMD** PUT 485 2026-11-13 (4DTE): 200 @ 18.00 = **+$360k** BUY | vol 772 / OI 518
- **SPY** PUT 740 2026-11-10 (1DTE): 1,500 @ 1.67 = **+$250k** BUY | vol 4,739 / OI 1,202
- **SPY** CALL 725 2026-11-13 (4DTE): 100 @ 25.00 = **+$250k** SELL | vol 103 / OI 287
- **QQQ** CALL 649 2026-11-09 (0DTE): 100 @ 23.91 = **+$239k** SELL | vol 115 / OI 0
- **SPY** PUT 756 2026-11-09 (0DTE): 300 @ 7.89 = **+$237k** BUY | vol 1,931 / OI 382
- **NVDA** PUT 187.5 2026-11-16 (7DTE): 195 @ 11.85 = **+$231k** BUY | vol 697 / OI 145
- **QQQ** CALL 650 2026-11-09 (0DTE): 100 @ 23.01 = **+$230k** SELL | vol 224 / OI 1,963
- **NVDA** PUT 187.5 2026-11-16 (7DTE): 195 @ 11.75 = **+$229k** BUY | vol 697 / OI 145
- **QQQ** PUT 672 2026-11-13 (4DTE): 200 @ 9.30 = **+$186k** BUY | vol 1,057 / OI 622

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 716 2026-11-11 (2DTE): 505 traded vs OI 303
- **SPY** PUT 742 2026-11-11 (2DTE): 507 traded vs OI 310
- **SPY** PUT 732 2026-11-10 (1DTE): 1,363 traded vs OI 1,032
- **SPY** CALL 759 2026-11-11 (2DTE): 511 traded vs OI 394
- **SPY** PUT 745 2026-11-11 (2DTE): 866 traded vs OI 798
- **SPY** PUT 752 2026-11-09 (0DTE): 963 traded vs OI 743
- **SPY** CALL 768 2026-11-09 (0DTE): 1,675 traded vs OI 1,628
- **SPY** CALL 787 2026-11-10 (1DTE): 500 traded vs OI 273
- **SPY** PUT 730 2026-11-12 (3DTE): 4,124 traded vs OI 1,056
- **SPY** PUT 748 2026-11-11 (2DTE): 563 traded vs OI 432
- **SPY** PUT 706 2026-11-09 (0DTE): 807 traded vs OI 470
- **SPY** PUT 721 2026-11-10 (1DTE): 551 traded vs OI 385
- **SPY** PUT 747 2026-11-11 (2DTE): 594 traded vs OI 316
- **SPY** PUT 716 2026-11-09 (0DTE): 1,119 traded vs OI 892
- **SPY** PUT 744 2026-11-12 (3DTE): 4,177 traded vs OI 211

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
