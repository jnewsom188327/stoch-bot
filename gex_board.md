# GEX + FLOW SCAN - Mon Nov 09, 10:00 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (2)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:00 | **MSFT** | **CALLS** | TREND + FLOW | 11/09 545C | 0.77 | 0.70 | -9% (0m) | **-9%** | +545% | 550 |
| 10:00 | **AMZN** | **CALLS** | TREND + FLOW | 11/09 275C | 0.48 | 0.45 | -6% (0m) | **-6%** | +258% | 275.95 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:00:08 ET, last candle SPY 09:59, QQQ 09:59 | no errors

## Flow surges NOT fired - price disagreed (4 today, last 5)
- 10:00 SMCI PUTS: price +1.22 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:00 IWM PUTS: price +0.83 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:55 IWM PUTS: price +1.09 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 SPY PUTS: price +3.67 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **MSFT** | 540.37 | TREND + FLOW | **CALLS** | 65 | 11/09 545C @ 0.77 (delta 0.22) = est +545% at 550 | POS +$543.7M | - | 550 | 540 | +$3.6M | +$1.4M bull / +$0 bear | LONG (clean 34, ADX 30, RVol 2.1) |
| 2 | **AMZN** | 272.12 | TREND + FLOW | **CALLS** | 64 | 11/09 275C @ 0.48 (delta 0.22) = est +258% at 275.95 | POS +$414.8M | - | 270 | 265 | +$7.5M | +$2.2M bull / -$1.1M bear | LONG (clean 35, ADX 39, RVol 3.2) |
| 3 | **TSLA** | 377.58 | FLOW SURGE | **PUTS** | 61 | none: 124 puts 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (54 contracts' greeks worked out here) | POS +$99.4M | - | 400 | 380 | -$85.2M | +$101k bull / -$5.6M bear | LONG (clean 34, ADX 37, RVol 2.5) |
| 4 | **AMD** | 489.03 | FLOW SURGE | **PUTS** | 61 | none: 156 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (64 contracts' greeks worked out here) | NEG -$63k | 488.69 | 500 | 500 | -$30.7M | +$0 bull / -$4.6M bear | out (clean 32, ADX 42, RVol 4.2) |
| 5 | **AVGO** | 315.15 | FLOW SURGE | **PUTS** | 58 | none: 100 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (41 contracts' greeks worked out here) | NEG -$70.7M | - | 340 | 320 | -$3.9M | +$300k bull / -$624k bear | out (clean 30, ADX 39, RVol 3.2) |
| 6 | **PLTR** | 167.69 | FLOW SURGE | **PUTS** | 55 | none: 13 puts 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$10.8M | - | 165 | 170 | -$3.5M | +$0 bull / -$1.3M bear | out (clean 28, ADX 36, RVol 2.7) |
| 7 | **SMH** | 480.21 | FLOW SURGE | **PUTS** | 53 | none: 156 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (69 contracts' greeks worked out here) | NEG -$257.6M | - | 500 | 475 | -$1.8M | +$0 bull / -$933k bear | out (clean 31, ADX 32, RVol 2.4) |
| 8 | **SMCI** | 29.22 | FLOW SURGE | **PUTS** | 53 | 11/13 27P @ 0.51 (delta 0.23) = est +33% at 28.44 | NEG -$32k | - | 30 | 30 | -$752k | +$0 bull / -$222k bear | out (clean 32, ADX 30, RVol 1.4) |
| 9 | **IWM** | 278.97 | FLOW SURGE | **PUTS** | 51 | 11/09 278P @ 0.51 (delta 0.33) = est +51% at 278 | NEG -$1.5B | 285.25 | 285 | 270 | -$6.0M | +$0 bull / -$316k bear | out (clean 32, ADX 34, RVol 2.0) |
| 10 | **SPY** | 747.76 | FLOW SURGE | **PUTS** | 47 | none: 676 puts 0-7DTE > 40 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (240 contracts' greeks worked out here) | NEG -$7.6B | 762.04 | 750 | 740 | -$107.2M | +$0 bull / -$5.0M bear | out (clean 32, ADX 29, RVol 1.7) |
| 11 | **QQQ** | 673.30 | FLOW SURGE | **PUTS** | 47 | none: 785 puts 0-7DTE > 61 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (247 contracts' greeks worked out here) | NEG -$2.3B | 700.54 | 680 | 680 | -$118.5M | +$0 bull / -$6.8M bear | out (clean 32, ADX 32, RVol 1.5) |
| 12 | **META** | 639.82 | TREND (flow not with it) | **CALLS** | 46 | none: 204 calls 0-7DTE > 8 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (84 contracts' greeks worked out here) | POS +$158.6M | 615.42 | 650 | 600 | -$3.8M | +$942k bull / -$2.9M bear | LONG (clean 33, ADX 41, RVol 3.2) |
| 13 | **HOOD** | 83.88 | FLOW SURGE | **PUTS** | 46 | none: 17 puts 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$1.6M | - | 85 | 85 | -$1.4M | +$0 bull / -$754k bear | out (clean 30, ADX 49, RVol 1.3) |
| 14 | **COIN** | 136.21 | FLOW SURGE | **PUTS** | 45 | none: 27 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$6.5M | - | 140 | 135 | -$865k | +$0 bull / -$417k bear | out (clean 31, ADX 20, RVol 0.8) |
| 15 | **NVDA** | 178.75 | - | **-** | 31 | - | NEG -$170.1M | - | 190 | 190 | -$37.4M | +$857k bull / -$21.2M bear | out (clean 32, ADX 35, RVol 11.9) |
| 16 | **GOOGL** | 293.88 | - | **-** | 30 | - | POS +$22.7M | 289.87 | 300 | 290 | +$3.2M | +$918k bull / -$60k bear | out (clean 32, ADX 30, RVol 2.7) |
| 17 | **MSTR** | 125.82 | - | **-** | 29 | - | POS +$1.0M | 123.1 | 135 | 120 | -$1.2M | +$0 bull / -$992k bear | out (clean 30, ADX 36, RVol 1.9) |
| 18 | **DELL** | 345.82 | - | **-** | 28 | - | NEG -$6.3M | - | 350 | 340 | -$326k | +$0 bull / -$523k bear | out (clean 31, ADX 32, RVol 1.6) |
| 19 | **AAPL** | 348.21 | - | **-** | 26 | - | POS +$356.0M | 338.66 | 350 | 350 | +$4.6M | +$1.8M bull / -$406k bear | out (clean 27, ADX 28, RVol 1.5) |
| 20 | **MU** | 727.65 | - | **-** | 24 | - | NEG -$16.4M | - | 750 | 750 | -$17.8M | +$0 bull / -$16.3M bear | out (clean 31, ADX 27, RVol 2.1) |
| 21 | **ARM** | 183.47 | - | **-** | 23 | - | NEG -$4.6M | - | 185 | 190 | -$274k | - | out (clean 25, ADX 34, RVol 1.1) |
| 22 | **ORCL** | 118.61 | - | **-** | 22 | - | NEG -$26.3M | - | 125 | 125 | -$300k | +$0 bull / -$294k bear | out (clean 29, ADX 29, RVol 0.8) |
| 23 | **BABA** | 106.19 | - | **-** | 20 | - | POS +$3.3M | 103.88 | 110 | 110 | +$11k | +$88k bull / -$106k bear | out (clean 32, ADX 28, RVol 2.1) |
| 24 | **CRM** | 214.44 | - | **-** | 12 | - | NEG -$10.6M | - | 195 | 220 | +$7k | - | out (clean 34, ADX 23, RVol 1.4) |
| 25 | **NFLX** | 63.65 | - | **-** | 11 | - | NEG -$19.2M | - | 65 | 65 | +$14k | - | out (clean 32, ADX 33, RVol 2.0) |
| 26 | **SHOP** | 149.31 | - | **-** | 11 | - | POS +$1.1M | 142.12 | 150 | 140 | -$4k | - | out (clean 34, ADX 17, RVol 0.6) |
| 27 | **UBER** | 69.09 | - | **-** | 8 | - | NEG -$104k | 69.3 | 70 | 65 | +$4k | - | out (clean 31, ADX 24, RVol 1.0) |

## Big prints this scan (287)
- **NVDA** CALL 172.5 2026-11-09 (0DTE): 731 @ 5.00 = **+$366k** SELL | vol 8,976 / OI 0
- **MU** PUT 697.5 2026-11-16 (7DTE): 112 @ 32.44 = **+$363k** BUY | vol 150 / OI 115
- **MU** PUT 697.5 2026-11-13 (4DTE): 112 @ 29.21 = **+$327k** BUY | vol 145 / OI 192
- **QQQ** PUT 667 2026-11-09 (0DTE): 1,000 @ 2.70 = **+$270k** BUY | vol 19,632 / OI 212
- **QQQ** PUT 667 2026-11-09 (0DTE): 1,000 @ 2.70 = **+$270k** BUY | vol 19,632 / OI 212
- **QQQ** PUT 667 2026-11-09 (0DTE): 877 @ 3.00 = **+$263k** BUY | vol 19,632 / OI 212
- **MU** CALL 727.5 2026-11-16 (7DTE): 99 @ 24.07 = **+$238k** SELL | vol 110 / OI 122
- **SPY** CALL 744 2026-11-10 (1DTE): 444 @ 5.29 = **+$235k** SELL | vol 4,493 / OI 586
- **SMH** PUT 470 2026-11-13 (4DTE): 200 @ 11.60 = **+$232k** BUY | vol 204 / OI 408
- **MU** CALL 727.5 2026-11-13 (4DTE): 99 @ 20.84 = **+$206k** SELL | vol 162 / OI 163
- **QQQ** PUT 667 2026-11-09 (0DTE): 760 @ 2.70 = **+$205k** BUY | vol 19,632 / OI 212
- **SPY** PUT 770 2026-11-09 (0DTE): 80 @ 25.43 = **+$203k** BUY | vol 82 / OI 17
- **NVDA** PUT 185 2026-11-09 (0DTE): 200 @ 9.79 = **+$196k** BUY | vol 4,116 / OI 2,768
- **AMZN** CALL 270 2026-11-13 (4DTE): 250 @ 7.60 = **+$190k** BUY | vol 1,325 / OI 7,386
- **QQQ** CALL 675 2026-11-10 (1DTE): 583 @ 3.17 = **+$185k** SELL | vol 1,463 / OI 300

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 738 2026-11-10 (1DTE): 610 traded vs OI 337
- **SPY** PUT 727 2026-11-09 (0DTE): 1,462 traded vs OI 1,357
- **SPY** CALL 760 2026-11-09 (0DTE): 5,052 traded vs OI 4,499
- **SPY** PUT 747 2026-11-09 (0DTE): 2,449 traded vs OI 1,091
- **SPY** PUT 743 2026-11-10 (1DTE): 691 traded vs OI 483
- **SPY** PUT 746 2026-11-10 (1DTE): 852 traded vs OI 213
- **SPY** CALL 759 2026-11-10 (1DTE): 1,268 traded vs OI 652
- **SPY** PUT 749 2026-11-09 (0DTE): 719 traded vs OI 351
- **SPY** CALL 763 2026-11-09 (0DTE): 2,731 traded vs OI 970
- **SPY** CALL 751 2026-11-10 (1DTE): 2,093 traded vs OI 1,787
- **SPY** CALL 737 2026-11-09 (0DTE): 828 traded vs OI 640
- **SPY** PUT 739 2026-11-10 (1DTE): 679 traded vs OI 380
- **SPY** PUT 728 2026-11-10 (1DTE): 929 traded vs OI 473
- **SPY** CALL 764 2026-11-10 (1DTE): 820 traded vs OI 415
- **SPY** PUT 745 2026-11-09 (0DTE): 10,839 traded vs OI 4,541

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
