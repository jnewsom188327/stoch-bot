# GEX + FLOW SCAN - Wed Nov 04, 09:50 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (3)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 09:50 | **UBER** | **CALLS** | FLIP CROSS up into positive gamma | 11/06 71C | 0.60 | 0.53 | -12% (0m) | **-12%** | +50% | 70 |
| 09:50 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/04 286C | 0.53 | 0.48 | -9% (0m) | **-9%** | +150% | 287 |
| 09:45 | **UBER** | **PUTS** | FLIP CROSS down into negative gamma | 11/06 67P | 0.63 | 0.47 | -3% (1m) | **-25%** | +27% | 68.03 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 09:50:08 ET, last candle SPY 09:49, QQQ 09:49 | no errors

## Flow surges NOT fired - price disagreed (2 today, last 5)
- 09:50 AMZN PUTS: price +2.12 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 NVDA PUTS: price +4.27 over the last 15 min - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **IWM** | 285.06 | RUN: clean trend + negative gamma + flow agrees | **CALLS** | 81 | 11/04 286C @ 0.53 (delta 0.34) = est +150% at 287 | NEG -$32.1M | 285.11 | 285 | 270 | +$2.7M | +$212k bull / -$102k bear | LONG (clean 34, ADX 38, RVol 4.9) |
| 2 | **GOOGL** | 289.77 | PINNED between the walls (positive gamma) - chop | **-** | 69 | - | POS +$70.9M | 284.42 | 290 | 290 | -$7.0M | +$0 bull / -$1.0M bear | LONG (clean 34, ADX 40, RVol 2.5) |
| 3 | **AAPL** | 350.09 | PINNED between the walls (positive gamma) - chop | **-** | 65 | - | POS +$739.0M | 341.5 | 350 | 350 | -$34.8M | +$0 bull / -$2.2M bear | out (clean 31, ADX 32, RVol 4.4) |
| 4 | **AMZN** | 268.66 | FLOW SURGE | **PUTS** | 63 | 11/04 265P @ 0.64 (delta 0.22) = est +232% at 263.91 | POS +$532.9M | - | 270 | 250 | -$13.8M | +$1.5M bull / -$5.5M bear | LONG (clean 34, ADX 46, RVol 5.5) |
| 5 | **MSFT** | 550.49 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 63 | none: 167 puts 0-7DTE > 14 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (80 contracts' greeks worked out here) | POS +$952.5M | - | 550 | 535 | -$6.3M | +$0 bull / -$3.8M bear | out (clean 28, ADX 48, RVol 4.9) |
| 6 | **BABA** | 106.03 | TREND (flow not with it) | **CALLS** | 62 | 11/06 109C @ 0.79 (delta 0.27) = est +35% at 107.15 | POS +$15.9M | - | 110 | 100 | -$267k | - | LONG (clean 35, ADX 36, RVol 5.0) |
| 7 | **NFLX** | 65.32 | FLOW SURGE | **PUTS** | 60 | none: 13 puts 0-7DTE > 1 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only +12% at the target (needs +20%) (1 contracts' greeks worked out here) | POS +$17.6M | 62.8 | 65 | 65 | -$678k | +$0 bull / -$54k bear | out (clean 29, ADX 42, RVol 3.5) |
| 8 | **AMD** | 510.02 | FLOW SURGE | **PUTS** | 57 | none: 164 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (68 contracts' greeks worked out here) | NEG -$25.8M | - | 510 | 500 | -$11.5M | +$0 bull / -$1.5M bear | out (clean 32, ADX 31, RVol 10.1) |
| 9 | **DELL** | 385.88 | FLOW SURGE | **CALLS** | 57 | none: 27 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$29.3M | - | 400 | 400 | +$458k | +$56k bull / +$0 bear | out (clean 32, ADX 26, RVol 3.8) |
| 10 | **NVDA** | 205.31 | FLOW SURGE | **PUTS** | 56 | 11/04 202.5P @ 0.61 (delta 0.24) = est +24% at 204.1 | POS +$60.4M | 204.1 | 210 | 200 | -$8.7M | +$0 bull / -$673k bear | out (clean 29, ADX 31, RVol 4.9) |
| 11 | **UBER** | 68.91 | FLIP CROSS up into positive gamma | **CALLS** | 56 | 11/06 71C @ 0.60 (delta 0.30) = est +50% at 70 | POS +$2.1M | 68.79 | 70 | 65 | -$222k | - | out (clean 30, ADX 31, RVol 4.5) |
| 12 | **COIN** | 148.96 | FLOW SURGE | **PUTS** | 55 | none: 21 puts 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (1 contracts' greeks worked out here) | POS +$29.5M | - | 148 | 150 | -$736k | +$0 bull / -$141k bear | out (clean 30, ADX 20, RVol 2.5) |
| 13 | **TSLA** | 382.42 | FLOW SURGE | **PUTS** | 54 | none: 124 puts 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (60 contracts' greeks worked out here) | NEG -$140.5M | 395.47 | 400 | 380 | -$13.9M | +$302k bull / -$7.3M bear | out (clean 31, ADX 28, RVol 4.6) |
| 14 | **QQQ** | 697.91 | FLOW SURGE | **PUTS** | 53 | none: 612 puts 0-7DTE > 35 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (260 contracts' greeks worked out here) | NEG -$4.2B | 723.06 | 700 | 680 | -$37.8M | +$0 bull / -$3.6M bear | out (clean 29, ADX 28, RVol 4.6) |
| 15 | **ORCL** | 127.48 | TREND (flow not with it) | **CALLS** | 46 | none: 26 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (2 contracts' greeks worked out here) | NEG -$30.4M | - | 130 | 125 | -$410k | +$61k bull / -$76k bear | LONG (clean 35, ADX 27, RVol 4.1) |
| 16 | **HOOD** | 86.20 | FLOW SURGE | **PUTS** | 46 | none: 17 puts 0-7DTE > 2 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only +2% at the target (needs +20%) | POS +$973k | 85.79 | 90 | 90 | -$482k | +$0 bull / -$78k bear | out (clean 29, ADX 17, RVol 2.0) |
| 17 | **SMH** | 518.93 | - | **-** | 32 | - | NEG -$385.1M | - | 532.5 | 500 | +$1.1M | +$0 bull / -$1.2M bear | out (clean 32, ADX 21, RVol 4.7) |
| 18 | **META** | 631.22 | - | **-** | 31 | - | POS +$154.3M | 619.55 | 650 | 625 | +$4.3M | +$2.8M bull / -$30k bear | out (clean 30, ADX 39, RVol 2.6) |
| 19 | **AVGO** | 332.72 | - | **-** | 31 | - | NEG -$66.8M | 350.82 | 340 | 330 | +$887k | +$0 bull / -$26k bear | out (clean 30, ADX 20, RVol 3.6) |
| 20 | **SPY** | 767.06 | - | **-** | 29 | - | NEG -$3.0B | 770.23 | 770 | 750 | -$33.0M | +$0 bull / -$4.7M bear | out (clean 30, ADX 32, RVol 3.4) |
| 21 | **PLTR** | 172.61 | - | **-** | 29 | - | NEG -$45.0M | - | 165 | 170 | -$1.3M | +$0 bull / -$1.1M bear | out (clean 27, ADX 22, RVol 4.2) |
| 22 | **SMCI** | 32.38 | - | **-** | 27 | - | POS +$7.4M | - | 34.5 | 30 | +$231k | +$0 bull / -$37k bear | out (clean 33, ADX 14, RVol 4.8) |
| 23 | **SHOP** | 147.19 | - | **-** | 27 | - | NEG -$10.5M | - | 160 | 135 | -$39k | - | out (clean 34, ADX 38, RVol 4.8) |
| 24 | **MU** | 845.33 | - | **-** | 26 | - | NEG -$253.4M | - | 840 | 850 | +$6.8M | +$0 bull / -$4.6M bear | out (clean 31, ADX 19, RVol 3.0) |
| 25 | **MSTR** | 141.00 | - | **-** | 25 | - | POS +$125.2M | - | 135 | 150 | -$747k | - | out (clean 30, ADX 29, RVol 2.2) |
| 26 | **CRM** | 230.00 | - | **-** | 25 | - | NEG -$8.9M | 239.32 | 240 | 220 | +$98k | - | out (clean 30, ADX 35, RVol 3.7) |
| 27 | **ARM** | 207.29 | - | **-** | 16 | - | NEG -$5.3M | - | 212.5 | 200 | -$13k | - | out (clean 26, ADX 27, RVol 2.2) |

## Big prints this scan (626)
- **QQQ** PUT 720 2026-11-09 (5DTE): 422 @ 29.00 = **+$1.2M** BUY | vol 710 / OI 2,092
- **QQQ** PUT 720 2026-11-09 (5DTE): 288 @ 29.00 = **+$835k** BUY | vol 710 / OI 2,092
- **AMZN** CALL 262.5 2026-11-04 (0DTE): 952 @ 5.90 = **+$562k** SELL | vol 2,439 / OI 817
- **TSLA** PUT 377.5 2026-11-11 (7DTE): 500 @ 9.60 = **+$480k** BUY | vol 1,072 / OI 60
- **SPY** CALL 740 2026-11-05 (1DTE): 167 @ 23.88 = **+$399k** SELL | vol 236 / OI 392
- **AMZN** CALL 260 2026-11-04 (0DTE): 498 @ 7.71 = **+$384k** SELL | vol 4,009 / OI 3,272
- **SPY** CALL 756 2026-11-06 (2DTE): 320 @ 10.31 = **+$330k** SELL | vol 732 / OI 1,403
- **TSLA** PUT 397.5 2026-11-09 (5DTE): 168 @ 19.20 = **+$323k** BUY | vol 378 / OI 200
- **TSLA** PUT 397.5 2026-11-09 (5DTE): 168 @ 19.05 = **+$320k** BUY | vol 378 / OI 200
- **SPY** CALL 765 2026-11-06 (2DTE): 800 @ 3.83 = **+$306k** SELL | vol 2,178 / OI 6,014
- **TSLA** PUT 380 2026-11-06 (2DTE): 375 @ 8.00 = **+$300k** BUY | vol 3,213 / OI 10,447
- **AMZN** CALL 260 2026-11-04 (0DTE): 400 @ 7.10 = **+$284k** SELL | vol 4,009 / OI 3,272
- **AMZN** CALL 260 2026-11-04 (0DTE): 352 @ 7.40 = **+$260k** SELL | vol 4,009 / OI 3,272
- **MU** CALL 820 2026-11-09 (5DTE): 100 @ 24.90 = **+$249k** SELL | vol 107 / OI 18
- **SMH** CALL 505 2026-11-11 (7DTE): 148 @ 16.05 = **+$238k** SELL | vol 550 / OI 1

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 724 2026-11-04 (0DTE): 766 traded vs OI 0
- **SPY** CALL 766 2026-11-05 (1DTE): 1,120 traded vs OI 0
- **SPY** CALL 810 2026-11-09 (5DTE): 600 traded vs OI 102
- **SPY** CALL 777 2026-11-05 (1DTE): 2,320 traded vs OI 0
- **SPY** CALL 778 2026-11-05 (1DTE): 913 traded vs OI 0
- **SPY** PUT 753 2026-11-05 (1DTE): 771 traded vs OI 0
- **SPY** CALL 765 2026-11-04 (0DTE): 13,257 traded vs OI 6,721
- **SPY** CALL 770 2026-11-05 (1DTE): 6,108 traded vs OI 4,614
- **SPY** PUT 752 2026-11-04 (0DTE): 3,630 traded vs OI 1,770
- **SPY** PUT 757 2026-11-05 (1DTE): 538 traded vs OI 0
- **SPY** CALL 772 2026-11-04 (0DTE): 6,662 traded vs OI 5,170
- **SPY** PUT 756 2026-11-05 (1DTE): 777 traded vs OI 0
- **SPY** PUT 762 2026-11-05 (1DTE): 878 traded vs OI 0
- **SPY** PUT 763 2026-11-05 (1DTE): 1,313 traded vs OI 0
- **SPY** PUT 737 2026-11-05 (1DTE): 636 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
