# GEX + FLOW SCAN - Fri Oct 30, 10:20 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (1)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:15 | **AAPL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 10/30 347.5C | 0.50 | 0.55 | +36% (3m) | **+10%** | +104% | 347.56 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:20:08 ET, last candle SPY 10:19, QQQ 10:19 | no errors

## Flow surges NOT fired - price disagreed (7 today, last 5)
- 10:20 HOOD CALLS: price -0.34 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:20 MSTR CALLS: price -1.00 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:20 COIN CALLS: price -3.73 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:20 PLTR CALLS: price -2.25 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:20 GOOGL CALLS: price -1.33 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **COIN** | 139.15 | FLOW SURGE | **CALLS** | 65 | 10/30 142C @ 0.75 (delta 0.26) = est +212% at 143.67 | NEG -$14.6M | - | 150 | 140 | +$120k | +$83k bull / +$0 bear | out (clean 27, ADX 50, RVol 2.9) |
| 2 | **ARM** | 206.44 | FLOW SURGE | **CALLS** | 65 | none: 32 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (28 contracts' greeks worked out here) | NEG -$17.5M | - | 220 | 205 | +$115k | +$368k bull / +$0 bear | out (clean 25, ADX 41, RVol 4.6) |
| 3 | **AAPL** | 345.58 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 63 | 10/30 347.5C @ 0.54 (delta 0.28) = est +109% at 347.6 | POS +$390.8M | 342.22 | 350 | 345 | -$1.1M | +$189k bull / -$2.5M bear | out (clean 30, ADX 50, RVol 2.1) |
| 4 | **AMZN** | 236.14 | FLOW SURGE | **CALLS** | 63 | none: 72 calls 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (34 contracts' greeks worked out here) | NEG -$210.4M | - | 250 | 240 | +$2.9M | +$506k bull / +$0 bear | out (clean 32, ADX 30, RVol 4.0) |
| 5 | **PLTR** | 187.65 | FLOW SURGE | **CALLS** | 63 | 10/30 190C @ 0.64 (delta 0.27) = est +88% at 190 | NEG -$60.6M | 192.79 | 200 | 190 | +$544k | +$253k bull / +$0 bear | out (clean 26, ADX 34, RVol 3.8) |
| 6 | **SMH** | 529.63 | FLOW SURGE | **CALLS** | 61 | none: 172 calls 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (70 contracts' greeks worked out here) | NEG -$546.1M | - | 532.5 | 530 | +$155k | +$36k bull / +$0 bear | out (clean 28, ADX 44, RVol 3.2) |
| 7 | **AVGO** | 328.22 | FLOW SURGE | **CALLS** | 61 | none: 104 calls 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (52 contracts' greeks worked out here) | NEG -$120.0M | 342.81 | 330 | 330 | +$412k | +$72k bull / -$61k bear | out (clean 29, ADX 42, RVol 2.3) |
| 8 | **QQQ** | 694.43 | FLOW SURGE | **CALLS** | 60 | none: 564 calls 0-7DTE > 28 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (241 contracts' greeks worked out here) | NEG -$9.6B | 726.02 | 720 | 690 | +$21.0M | +$2.8M bull / +$0 bear | out (clean 28, ADX 45, RVol 2.5) |
| 9 | **HOOD** | 83.91 | FLOW SURGE | **CALLS** | 58 | 10/30 84C @ 0.80 (delta 0.49) = est +60% at 85 | NEG -$37.6M | - | 85 | 85 | +$158k | +$49k bull / +$0 bear | out (clean 31, ADX 50, RVol 4.4) |
| 10 | **NVDA** | 206.87 | FLOW SURGE | **CALLS** | 57 | 10/30 207.5C @ 0.76 (delta 0.41) = est +240% at 210 | NEG -$392.2M | 212.08 | 210 | 210 | +$2.4M | +$372k bull / +$0 bear | out (clean 25, ADX 41, RVol 2.0) |
| 11 | **MSTR** | 127.91 | FLOW SURGE | **CALLS** | 56 | 10/30 131C @ 0.76 (delta 0.26) = est +56% at 130 | NEG -$28.0M | - | 135 | 125 | +$357k | +$231k bull / +$0 bear | out (clean 26, ADX 42, RVol 4.9) |
| 12 | **MU** | 892.10 | FLOW SURGE | **CALLS** | 54 | none: 162 calls 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (72 contracts' greeks worked out here) | NEG -$218.2M | 929.28 | 900 | 900 | +$7.7M | +$4.0M bull / +$0 bear | out (clean 29, ADX 40, RVol 1.8) |
| 13 | **SPY** | 758.25 | FLOW SURGE | **CALLS** | 53 | 10/30 761C @ 0.76 (delta 0.27) = est +44% at 760 | NEG -$13.1B | 770.35 | 760 | 760 | +$11.3M | +$962k bull / +$0 bear | out (clean 27, ADX 41, RVol 2.3) |
| 14 | **GOOGL** | 279.80 | FLOW SURGE | **CALLS** | 51 | 10/30 282.5C @ 0.61 (delta 0.25) = est +92% at 282.2 | NEG -$207.7M | - | 280 | 280 | +$534k | +$576k bull / +$0 bear | out (clean 31, ADX 33, RVol 1.4) |
| 15 | **CRM** | 230.88 | FLOW SURGE | **CALLS** | 50 | none: 36 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (27 contracts' greeks worked out here) | NEG -$20.6M | 238.04 | 240 | 230 | +$61k | +$36k bull / +$0 bear | out (clean 28, ADX 21, RVol 1.2) |
| 16 | **META** | 618.34 | FLOW SURGE | **CALLS** | 47 | none: 196 calls 0-7DTE > 10 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (76 contracts' greeks worked out here) | NEG -$64.0M | 620.73 | 625 | 625 | +$2.0M | +$792k bull / +$0 bear | out (clean 28, ADX 29, RVol 0.9) |
| 17 | **MSFT** | 521.68 | FLOW SURGE | **CALLS** | 46 | none: 168 calls 0-7DTE > 11 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (68 contracts' greeks worked out here) | POS +$455.5M | 514.04 | 525 | 525 | +$469k | +$702k bull / -$136k bear | out (clean 27, ADX 26, RVol 1.8) |
| 18 | **ORCL** | 133.34 | FLOW SURGE | **CALLS** | 37 | 10/30 136C @ 0.40 (delta 0.21) = est +62% at 135 | POS +$70.7M | 129.95 | 135 | 130 | +$254k | +$194k bull / +$0 bear | out (clean 32, ADX 32, RVol 0.9) |
| 19 | **DELL** | 432.86 | - | **-** | 30 | - | NEG -$51.8M | - | 440 | 425 | +$141k | +$86k bull / +$0 bear | out (clean 32, ADX 48, RVol 3.2) |
| 20 | **SHOP** | 159.22 | - | **-** | 29 | - | NEG -$14.2M | - | 160 | 157.5 | +$15k | - | out (clean 25, ADX 40, RVol 1.2) |
| 21 | **IWM** | 280.13 | - | **-** | 28 | - | NEG -$602.6M | 281.26 | 280 | 270 | +$1.1M | +$89k bull / +$0 bear | out (clean 27, ADX 38, RVol 1.3) |
| 22 | **AMD** | 513.48 | - | **-** | 28 | - | NEG -$87.2M | 523.6 | 527.5 | 500 | +$856k | +$1.1M bull / -$185k bear | out (clean 28, ADX 40, RVol 4.5) |
| 23 | **BABA** | 98.21 | - | **-** | 26 | - | NEG -$36.2M | 99.63 | 100 | 98 | +$36k | - | out (clean 29, ADX 20, RVol 1.3) |
| 24 | **UBER** | 65.11 | - | **-** | 24 | - | NEG -$32.5M | 66.42 | 70 | 65 | +$35k | - | out (clean 28, ADX 16, RVol 0.8) |
| 25 | **SMCI** | 32.60 | - | **-** | 22 | - | POS +$958k | 32.47 | 35 | 32 | +$26k | - | out (clean 28, ADX 48, RVol 2.2) |
| 26 | **TSLA** | 396.95 | - | **-** | 20 | - | POS +$400.3M | 377.61 | 400 | 400 | +$619k | +$1.5M bull / -$3.4M bear | out (clean 28, ADX 34, RVol 1.6) |
| 27 | **NFLX** | 62.52 | - | **-** | 17 | - | NEG -$14.3M | 62.85 | 63 | 63 | +$6k | +$0 bull / -$26k bear | out (clean 31, ADX 30, RVol 0.8) |

## Big prints this scan (195)
- **TSLA** PUT 402.5 2026-11-04 (5DTE): 999 @ 10.90 = **+$1.1M** MID | vol 1,082 / OI 225
- **SPY** CALL 759 2026-11-02 (3DTE): 997 @ 4.22 = **+$421k** BUY | vol 3,508 / OI 169
- **TSLA** PUT 387.5 2026-11-06 (7DTE): 496 @ 5.00 = **+$248k** SELL | vol 2,872 / OI 510
- **SPY** PUT 767 2026-11-04 (5DTE): 250 @ 8.79 = **+$220k** SELL | vol 5,312 / OI 29,783
- **SPY** PUT 767 2026-11-04 (5DTE): 250 @ 8.78 = **+$220k** SELL | vol 5,312 / OI 29,783
- **TSLA** PUT 400 2026-10-30 (0DTE): 449 @ 4.60 = **+$207k** BUY | vol 6,124 / OI 4,157
- **TSLA** PUT 400 2026-10-30 (0DTE): 439 @ 4.50 = **+$198k** BUY | vol 6,124 / OI 4,157
- **TSLA** CALL 402.5 2026-11-06 (7DTE): 241 @ 6.85 = **+$165k** SELL | vol 4,463 / OI 693
- **TSLA** CALL 402.5 2026-11-06 (7DTE): 200 @ 6.86 = **+$137k** SELL | vol 4,463 / OI 693
- **QQQ** CALL 670 2026-10-30 (0DTE): 50 @ 27.33 = **+$137k** BUY | vol 128 / OI 140
- **TSLA** PUT 405 2026-11-06 (7DTE): 100 @ 13.50 = **+$135k** SELL | vol 307 / OI 816
- **TSLA** CALL 402.5 2026-11-06 (7DTE): 183 @ 6.85 = **+$125k** SELL | vol 4,463 / OI 693
- **MU** CALL 900 2026-11-02 (3DTE): 69 @ 18.00 = **+$124k** BUY | vol 2,692 / OI 165
- **MU** PUT 880 2026-10-30 (0DTE): 556 @ 2.10 = **+$117k** SELL | vol 8,214 / OI 2,467
- **TSLA** CALL 387.5 2026-10-30 (0DTE): 100 @ 10.55 = **+$106k** BUY | vol 3,676 / OI 3,278

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 734 2026-11-02 (3DTE): 537 traded vs OI 385
- **SPY** CALL 779 2026-10-30 (0DTE): 3,751 traded vs OI 3,022
- **SPY** PUT 705 2026-11-04 (5DTE): 598 traded vs OI 482
- **SPY** CALL 792 2026-11-04 (5DTE): 1,041 traded vs OI 151
- **SPY** CALL 773 2026-11-02 (3DTE): 538 traded vs OI 486
- **SPY** PUT 731 2026-11-02 (3DTE): 519 traded vs OI 101
- **QQQ** PUT 665 2026-11-03 (4DTE): 829 traded vs OI 731
- **QQQ** PUT 682 2026-11-02 (3DTE): 615 traded vs OI 0
- **QQQ** CALL 715 2026-11-03 (4DTE): 653 traded vs OI 186
- **QQQ** CALL 717 2026-11-06 (7DTE): 511 traded vs OI 246
- **QQQ** PUT 684 2026-11-02 (3DTE): 554 traded vs OI 0
- **QQQ** CALL 708 2026-11-02 (3DTE): 523 traded vs OI 325
- **QQQ** CALL 720 2026-11-02 (3DTE): 2,049 traded vs OI 1,925
- **QQQ** CALL 695 2026-11-13 (14DTE): 544 traded vs OI 342
- **QQQ** CALL 713 2026-11-27 (28DTE): 601 traded vs OI 97

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
