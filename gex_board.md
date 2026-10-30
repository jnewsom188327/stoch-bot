# GEX + FLOW SCAN - Fri Oct 30, 10:25 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (2)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:25 | **SMCI** | **PUTS** | FLIP CROSS down into negative gamma | 10/30 32.5P | 0.43 | 0.35 | -19% (0m) | **-19%** | +32% | 32 |
| 10:15 | **AAPL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 10/30 347.5C | 0.50 | 0.53 | +38% (8m) | **+6%** | +104% | 347.56 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:25:08 ET, last candle SPY 10:24, QQQ 10:24 | no errors

## Flow surges NOT fired - price disagreed (15 today, last 5)
- 10:25 HOOD CALLS: price -0.19 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:25 COIN CALLS: price -2.96 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:25 PLTR CALLS: price -1.78 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:25 GOOGL CALLS: price -0.26 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:25 AMZN CALLS: price -1.57 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **SMH** | 526.90 | FLOW SURGE | **CALLS** | 65 | none: 168 calls 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (78 contracts' greeks worked out here) | NEG -$536.8M | - | 532.5 | 530 | +$825k | +$240k bull / +$0 bear | out (clean 28, ADX 46, RVol 3.0) |
| 2 | **ARM** | 204.34 | FLOW SURGE | **CALLS** | 65 | none: 32 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (30 contracts' greeks worked out here) | NEG -$18.1M | - | 220 | 205 | +$214k | +$368k bull / +$0 bear | out (clean 25, ADX 43, RVol 3.8) |
| 3 | **QQQ** | 692.90 | FLOW SURGE | **CALLS** | 63 | none: 560 calls 0-7DTE > 26 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (258 contracts' greeks worked out here) | NEG -$9.6B | 729.48 | 720 | 690 | +$40.5M | +$3.6M bull / +$0 bear | out (clean 28, ADX 47, RVol 3.6) |
| 4 | **AMZN** | 236.02 | FLOW SURGE | **CALLS** | 61 | 10/30 240C @ 0.54 (delta 0.20) = est +194% at 240 | NEG -$196.7M | 246.52 | 250 | 240 | +$4.3M | +$561k bull / +$0 bear | out (clean 32, ADX 30, RVol 3.7) |
| 5 | **PLTR** | 186.76 | FLOW SURGE | **CALLS** | 61 | 10/30 190C @ 0.55 (delta 0.22) = est +149% at 190 | NEG -$56.6M | 191.32 | 200 | 190 | +$923k | +$311k bull / +$0 bear | out (clean 26, ADX 36, RVol 4.2) |
| 6 | **HOOD** | 83.61 | FLOW SURGE | **CALLS** | 61 | 10/30 85C @ 0.41 (delta 0.28) = est +93% at 85 | NEG -$34.7M | - | 85 | 85 | +$785k | +$537k bull / +$0 bear | out (clean 31, ADX 51, RVol 2.9) |
| 7 | **NVDA** | 206.03 | FLOW SURGE | **CALLS** | 60 | 10/30 207.5C @ 0.52 (delta 0.30) = est +388% at 210 | NEG -$401.0M | 212 | 210 | 205 | +$4.2M | +$420k bull / +$0 bear | out (clean 25, ADX 42, RVol 2.2) |
| 8 | **AAPL** | 345.75 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 60 | 10/30 347.5C @ 0.68 (delta 0.31) = est +88% at 347.76 | POS +$424.5M | 341.56 | 350 | 345 | -$1.5M | +$189k bull / -$2.5M bear | out (clean 30, ADX 50, RVol 1.9) |
| 9 | **COIN** | 138.44 | FLOW SURGE | **CALLS** | 60 | 10/30 142C @ 0.68 (delta 0.24) = est +21% at 140 | NEG -$13.4M | - | 150 | 140 | +$331k | +$83k bull / +$0 bear | out (clean 27, ADX 51, RVol 2.9) |
| 10 | **MSFT** | 520.02 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 58 | none: 164 calls 0-7DTE > 8 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (73 contracts' greeks worked out here) | POS +$346.9M | 513.98 | 525 | 520 | +$1.5M | +$847k bull / -$136k bear | out (clean 27, ADX 27, RVol 1.5) |
| 11 | **SPY** | 757.54 | FLOW SURGE | **CALLS** | 56 | 10/30 761C @ 0.67 (delta 0.23) = est +72% at 760 | NEG -$13.7B | 772.09 | 770 | 750 | +$39.3M | +$2.5M bull / +$0 bear | out (clean 27, ADX 43, RVol 2.2) |
| 12 | **GOOGL** | 280.06 | FLOW SURGE | **CALLS** | 53 | 10/30 282.5C @ 0.54 (delta 0.25) = est +111% at 282.37 | NEG -$258.8M | - | 280 | 280 | +$1.4M | +$810k bull / +$0 bear | out (clean 31, ADX 34, RVol 1.5) |
| 13 | **AVGO** | 327.12 | FLOW SURGE | **CALLS** | 52 | none: 104 calls 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (46 contracts' greeks worked out here) | NEG -$123.3M | 341.31 | 330 | 330 | +$592k | +$72k bull / -$61k bear | out (clean 29, ADX 44, RVol 1.2) |
| 14 | **MU** | 886.25 | FLOW SURGE | **CALLS** | 51 | none: 157 calls 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (62 contracts' greeks worked out here) | NEG -$219.8M | 915.21 | 900 | 900 | +$12.4M | +$5.7M bull / +$0 bear | out (clean 29, ADX 40, RVol 1.6) |
| 15 | **CRM** | 230.58 | FLOW SURGE | **CALLS** | 50 | none: 36 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (28 contracts' greeks worked out here) | NEG -$20.1M | 235.23 | 240 | 230 | +$89k | +$36k bull / +$0 bear | out (clean 28, ADX 21, RVol 1.2) |
| 16 | **SMCI** | 32.46 | FLIP CROSS down into negative gamma | **PUTS** | 49 | 10/30 32.5P @ 0.43 (delta 0.51) = est +32% at 32 | NEG -$6k | 32.46 | 35 | 32 | +$154k | - | out (clean 28, ADX 48, RVol 2.1) |
| 17 | **IWM** | 280.10 | FLOW SURGE | **CALLS** | 48 | 10/30 281C @ 0.44 (delta 0.33) = est +124% at 281.56 | NEG -$709.5M | 281.56 | 280 | 270 | +$4.1M | +$89k bull / +$0 bear | out (clean 27, ADX 39, RVol 1.2) |
| 18 | **META** | 616.93 | FLOW SURGE | **CALLS** | 47 | none: 192 calls 0-7DTE > 8 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (77 contracts' greeks worked out here) | NEG -$93.2M | 620.84 | 625 | 625 | +$3.0M | +$1.3M bull / +$0 bear | out (clean 28, ADX 29, RVol 0.9) |
| 19 | **ORCL** | 132.99 | FLOW SURGE | **CALLS** | 39 | 10/30 135C @ 0.50 (delta 0.26) = est +113% at 135 | POS +$65.2M | 129.61 | 135 | 130 | +$504k | +$325k bull / +$0 bear | out (clean 32, ADX 33, RVol 0.9) |
| 20 | **AMD** | 510.82 | - | **-** | 32 | - | NEG -$112.2M | 525.13 | 527.5 | 500 | +$2.3M | +$1.6M bull / -$185k bear | out (clean 28, ADX 42, RVol 4.7) |
| 21 | **SHOP** | 158.45 | - | **-** | 30 | - | NEG -$14.1M | 164.22 | 160 | 157.5 | +$137k | - | out (clean 25, ADX 41, RVol 1.1) |
| 22 | **DELL** | 431.78 | - | **-** | 25 | - | NEG -$53.6M | - | 440 | 425 | +$77k | +$153k bull / +$0 bear | out (clean 32, ADX 48, RVol 3.9) |
| 23 | **BABA** | 98.31 | - | **-** | 25 | - | NEG -$38.8M | 100.02 | 100 | 98 | +$63k | - | out (clean 29, ADX 20, RVol 1.1) |
| 24 | **MSTR** | 128.43 | - | **-** | 24 | - | NEG -$24.6M | 135.3 | 135 | 125 | -$86k | +$279k bull / +$0 bear | out (clean 26, ADX 42, RVol 4.0) |
| 25 | **NFLX** | 62.57 | - | **-** | 22 | - | NEG -$18.7M | 63.37 | 63 | 63 | +$101k | +$0 bull / -$54k bear | out (clean 31, ADX 31, RVol 0.9) |
| 26 | **TSLA** | 397.23 | - | **-** | 21 | - | POS +$385.6M | 383.21 | 400 | 400 | -$2.4M | +$2.3M bull / -$5.4M bear | out (clean 28, ADX 33, RVol 1.6) |
| 27 | **UBER** | 65.08 | - | **-** | 10 | - | NEG -$32.0M | 66.65 | 67 | 65 | +$15k | - | out (clean 28, ADX 16, RVol 0.7) |

## Big prints this scan (98)
- **TSLA** CALL 402.5 2026-11-06 (7DTE): 2,000 @ 6.78 = **+$1.4M** SELL | vol 4,481 / OI 693
- **TSLA** CALL 415 2026-11-06 (7DTE): 2,000 @ 2.88 = **+$576k** SELL | vol 4,893 / OI 2,192
- **SPY** CALL 740 2026-11-05 (6DTE): 200 @ 21.60 = **+$432k** BUY | vol 304 / OI 6
- **QQQ** PUT 720 2026-10-30 (0DTE): 175 @ 22.69 = **+$397k** SELL | vol 1,098 / OI 22,475
- **QQQ** PUT 720 2026-10-30 (0DTE): 175 @ 22.69 = **+$397k** SELL | vol 1,098 / OI 22,475
- **SPY** PUT 765 2026-11-02 (3DTE): 462 @ 5.94 = **+$274k** SELL | vol 1,404 / OI 3,902
- **AMD** CALL 510 2026-11-02 (3DTE): 200 @ 13.63 = **+$273k** BUY | vol 677 / OI 144
- **HOOD** CALL 86 2026-11-06 (7DTE): 1,002 @ 2.45 = **+$245k** BUY | vol 5,860 / OI 1,507
- **HOOD** CALL 86 2026-11-06 (7DTE): 995 @ 2.44 = **+$243k** BUY | vol 5,860 / OI 1,507
- **SPY** PUT 765 2026-10-30 (0DTE): 462 @ 5.04 = **+$233k** SELL | vol 9,096 / OI 59,152
- **SPY** PUT 767 2026-11-04 (5DTE): 250 @ 8.95 = **+$224k** SELL | vol 5,819 / OI 29,783
- **GOOGL** CALL 282.5 2026-11-06 (7DTE): 450 @ 4.50 = **+$202k** BUY | vol 2,278 / OI 0
- **META** CALL 632.5 2026-11-06 (7DTE): 200 @ 9.10 = **+$182k** BUY | vol 274 / OI 92
- **MU** PUT 925 2026-10-30 (0DTE): 63 @ 28.15 = **+$177k** SELL | vol 385 / OI 1,189
- **MU** CALL 875 2026-11-06 (7DTE): 40 @ 43.66 = **+$175k** BUY | vol 303 / OI 53

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 755 2026-10-30 (0DTE): 1,412 traded vs OI 1,294
- **SPY** PUT 757 2026-11-03 (4DTE): 506 traded vs OI 349
- **SPY** PUT 740 2026-11-05 (6DTE): 660 traded vs OI 345
- **SPY** PUT 760 2026-11-03 (4DTE): 1,771 traded vs OI 1,516
- **SPY** CALL 774 2026-11-03 (4DTE): 510 traded vs OI 498
- **SPY** CALL 764 2026-11-03 (4DTE): 525 traded vs OI 123
- **SPY** CALL 800 2026-11-09 (10DTE): 578 traded vs OI 161
- **QQQ** CALL 690 2026-11-02 (3DTE): 569 traded vs OI 34
- **QQQ** CALL 705 2026-11-03 (4DTE): 620 traded vs OI 53
- **QQQ** CALL 696 2026-11-06 (7DTE): 500 traded vs OI 100
- **QQQ** CALL 713 2026-11-02 (3DTE): 695 traded vs OI 214
- **QQQ** PUT 675 2026-11-05 (6DTE): 743 traded vs OI 447
- **IWM** CALL 286 2026-11-06 (7DTE): 937 traded vs OI 929
- **IWM** CALL 281 2026-10-30 (0DTE): 6,800 traded vs OI 6,690
- **NVDA** CALL 207.5 2026-11-04 (5DTE): 559 traded vs OI 114

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
