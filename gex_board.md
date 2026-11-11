# GEX + FLOW SCAN - Wed Nov 11, 10:00 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (5)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 09:50 | **GOOGL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/11 292.5C | 0.51 | 0.43 | +14% (6m) | **-16%** | +82% | 291.86 |
| 09:45 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/11 282C | 0.68 | 0.96 | +85% (6m) | **+41%** | +68% | 282.96 |
| 09:45 | **QQQ** | **CALLS** | FLOW SURGE | 11/11 690C | 0.63 | 0.51 | +13% (1m) | **-19%** | +171% | 689.78 |
| 09:39 | **QQQ** | **CALLS** | 1m WHIPSAW (R1 R5) | 11/11 693C | 0.52 | 0.15 | -10% (0m) | **-71%** | +92% | 690.43 |
| 09:39 | **SPY** | **CALLS** | 1m WHIPSAW (R1 R5) | 11/11 760C | 0.53 | 0.28 | -2% (0m) | **-47%** | +79% | 758.82 |

## 1m RULES on SPY / QQQ - loose (2 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:00:08 ET, last candle SPY 09:59, QQQ 09:59 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 09:38 | QQQ | 1m WHIPSAW | R1 R5 | CALLS | TURNING away | **FIRE** QQQ261111C00693000 |
| 09:38 | SPY | 1m WHIPSAW | R1 R5 | CALLS | TURNING away | **FIRE** SPY261111C00760000 |

## Flow surges NOT fired - price disagreed (6 today, last 5)
- 10:00 MSFT CALLS: price -4.55 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:00 AMZN CALLS: price -0.73 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 09:55 AAPL PUTS: price +1.32 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 MSFT CALLS: price -2.01 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 09:50 NVDA CALLS: price -1.77 over the last 15 min - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **AVGO** | 351.60 | TREND + FLOW | **CALLS** | 59 | none: 112 calls 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (53 contracts' greeks worked out here) | POS +$99.8M | - | 350 | 350 | +$860k | +$2.9M bull / -$871k bear | LONG (clean 34, ADX 47, RVol 3.1) |
| 2 | **DELL** | 365.39 | TREND (flow not with it) | **CALLS** | 57 | none: 29 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$2.4M | - | 350 | 340 | -$483k | +$162k bull / +$0 bear | LONG (clean 35, ADX 44, RVol 2.5) |
| 3 | **MU** | 787.36 | FLOW SURGE | **PUTS** | 54 | none: 165 puts 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (70 contracts' greeks worked out here) | POS +$152.2M | - | 800 | 800 | -$64.0M | +$964k bull / -$11.7M bear | out (clean 32, ADX 45, RVol 2.2) |
| 4 | **MSFT** | 528.19 | FLOW SURGE | **CALLS** | 49 | 11/11 532.5C @ 0.76 (delta 0.23) = est +26% at 530 | POS +$241.2M | 514.23 | 535 | 520 | +$3.5M | +$753k bull / +$0 bear | out (clean 31, ADX 24, RVol 2.0) |
| 5 | **AMZN** | 268.57 | FLOW SURGE | **CALLS** | 47 | 11/11 270C @ 0.60 (delta 0.31) = est +64% at 270 | POS +$483.8M | - | 270 | 265 | +$4.2M | +$179k bull / +$0 bear | out (clean 33, ADX 30, RVol 1.6) |
| 6 | **GOOGL** | 290.39 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 47 | 11/11 292.5C @ 0.47 (delta 0.25) = est +109% at 292.36 | POS +$27.7M | 288.94 | 300 | 290 | +$827k | +$529k bull / +$0 bear | out (clean 28, ADX 37, RVol 1.4) |
| 7 | **PLTR** | 171.58 | FLOW SURGE | **CALLS** | 47 | none: 14 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (1 contracts' greeks worked out here) | POS +$73.6M | - | 170 | 170 | +$1.9M | +$359k bull / +$0 bear | out (clean 30, ADX 42, RVol 1.1) |
| 8 | **IWM** | 282.58 | TREND (flow not with it) | **CALLS** | 35 | none: 337 calls 0-7DTE > 13 priced 0.40-0.80 > 6 delta 0.2+ > 6 spread ok > 6 liquid > best one only +10% at the target (needs +20%) (126 contracts' greeks worked out here) | NEG -$191.4M | 282.96 | 285 | 270 | -$1.7M | - | LONG (clean 34, ADX 36, RVol 1.3) |
| 9 | **AMD** | 534.00 | - | **-** | 33 | - | POS +$136.7M | - | 550 | 500 | -$22.8M | +$5.4M bull / -$4.7M bear | out (clean 33, ADX 28, RVol 2.2) |
| 10 | **SMCI** | 29.67 | - | **-** | 32 | - | POS +$9.9M | - | 30 | 30 | -$189k | +$33k bull / +$0 bear | out (clean 31, ADX 37, RVol 1.3) |
| 11 | **SMH** | 500.90 | - | **-** | 30 | - | NEG -$79.3M | - | 500 | 475 | +$961k | +$615k bull / +$0 bear | out (clean 30, ADX 32, RVol 2.9) |
| 12 | **ORCL** | 124.88 | - | **-** | 30 | - | NEG -$2.7M | 127.79 | 130 | 125 | +$1.1M | +$281k bull / -$183k bear | out (clean 28, ADX 37, RVol 2.2) |
| 13 | **QQQ** | 685.35 | - | **-** | 26 | - | NEG -$827.2M | 689.47 | 700 | 680 | +$37.3M | +$6.1M bull / -$192k bear | out (clean 32, ADX 44, RVol 0.9) |
| 14 | **META** | 639.40 | - | **-** | 25 | - | POS +$259.5M | 623.11 | 650 | 625 | +$2.0M | +$3.1M bull / +$0 bear | out (clean 31, ADX 28, RVol 1.9) |
| 15 | **SPY** | 756.30 | - | **-** | 24 | - | NEG -$4.1B | 761.04 | 760 | 750 | +$21.4M | +$4.2M bull / -$498k bear | out (clean 32, ADX 45, RVol 0.6) |
| 16 | **TSLA** | 389.52 | - | **-** | 24 | - | POS +$386.0M | - | 400 | 380 | +$9.9M | +$6.8M bull / -$1.7M bear | out (clean 32, ADX 35, RVol 1.0) |
| 17 | **AAPL** | 353.56 | - | **-** | 24 | - | POS +$1.3B | 339.14 | 355 | 350 | -$2.4M | +$25k bull / -$824k bear | out (clean 27, ADX 37, RVol 2.1) |
| 18 | **ARM** | 191.28 | - | **-** | 23 | - | POS +$796k | 189.55 | 200 | 200 | -$209k | - | out (clean 28, ADX 47, RVol 0.7) |
| 19 | **CRM** | 215.24 | - | **-** | 23 | - | NEG -$11.1M | - | 230 | 220 | -$34k | - | out (clean 31, ADX 29, RVol 0.7) |
| 20 | **BABA** | 101.59 | - | **-** | 21 | - | NEG -$15.6M | 106.51 | 110 | 101 | +$51k | - | out (clean 30, ADX 28, RVol 1.0) |
| 21 | **NVDA** | 173.00 | - | **-** | 20 | - | NEG -$189.6M | - | 180 | 170 | +$4.6M | +$7.8M bull / -$1.6M bear | out (clean 34, ADX 25, RVol 1.4) |
| 22 | **MSTR** | 121.28 | - | **-** | 18 | - | NEG -$8.0M | 123.32 | 133 | 120 | -$221k | +$56k bull / -$192k bear | out (clean 29, ADX 17, RVol 1.0) |
| 23 | **COIN** | 134.20 | - | **-** | 16 | - | POS +$14.6M | 126.72 | 137 | 135 | +$139k | - | out (clean 28, ADX 32, RVol 0.7) |
| 24 | **NFLX** | 63.30 | - | **-** | 14 | - | NEG -$13.0M | 64.43 | 65 | 65 | +$135k | - | out (clean 28, ADX 21, RVol 1.2) |
| 25 | **SHOP** | 148.66 | - | **-** | 14 | - | POS +$2.8M | 144.42 | 150 | 140 | -$2k | - | out (clean 33, ADX 43, RVol 0.5) |
| 26 | **HOOD** | 83.00 | - | **-** | 11 | - | POS +$9.4M | 78.8 | 85 | 80 | -$44k | - | out (clean 32, ADX 28, RVol 1.4) |
| 27 | **UBER** | 69.50 | - | **-** | 7 | - | POS +$10.4M | 68.09 | 70 | 70 | +$1k | - | out (clean 33, ADX 24, RVol 0.7) |

## Big prints this scan (181)
- **AVGO** CALL 362.5 2026-11-13 (2DTE): 1,980 @ 3.25 = **+$644k** BUY | vol 3,204 / OI 215
- **AVGO** CALL 367.5 2026-11-13 (2DTE): 1,980 @ 2.19 = **+$434k** BUY | vol 2,242 / OI 180
- **NVDA** PUT 172.5 2026-11-11 (0DTE): 2,533 @ 1.60 = **+$405k** BUY | vol 27,686 / OI 2,988
- **AAPL** CALL 352.5 2026-11-18 (7DTE): 823 @ 4.65 = **+$383k** SELL | vol 1,970 / OI 94
- **SPY** PUT 757 2026-11-12 (1DTE): 875 @ 3.17 = **+$277k** BUY | vol 6,326 / OI 375
- **META** CALL 645 2026-11-13 (2DTE): 300 @ 8.47 = **+$254k** BUY | vol 820 / OI 888
- **QQQ** PUT 685 2026-11-13 (2DTE): 493 @ 4.96 = **+$245k** SELL | vol 2,375 / OI 23,913
- **META** CALL 647.5 2026-11-13 (2DTE): 300 @ 7.40 = **+$222k** BUY | vol 793 / OI 1,813
- **NVDA** CALL 170 2026-11-13 (2DTE): 418 @ 4.84 = **+$202k** SELL | vol 4,198 / OI 1,540
- **QQQ** PUT 688 2026-11-11 (0DTE): 463 @ 4.14 = **+$192k** BUY | vol 13,236 / OI 162
- **NVDA** CALL 172.5 2026-11-13 (2DTE): 380 @ 4.97 = **+$189k** BUY | vol 6,461 / OI 1,001
- **TSLA** CALL 380 2026-11-13 (2DTE): 181 @ 10.42 = **+$189k** SELL | vol 1,865 / OI 8,112
- **AMD** CALL 540 2026-11-13 (2DTE): 198 @ 9.00 = **+$178k** SELL | vol 918 / OI 1,314
- **META** CALL 640 2026-11-11 (0DTE): 300 @ 5.45 = **+$164k** BUY | vol 976 / OI 1,118
- **TSLA** CALL 390 2026-11-11 (0DTE): 481 @ 3.10 = **+$149k** BUY | vol 35,408 / OI 2,864

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 771 2026-11-11 (0DTE): 2,523 traded vs OI 1,027
- **SPY** CALL 777 2026-11-17 (6DTE): 529 traded vs OI 273
- **SPY** PUT 733 2026-11-11 (0DTE): 1,758 traded vs OI 811
- **SPY** PUT 737 2026-11-11 (0DTE): 934 traded vs OI 813
- **SPY** CALL 799 2026-11-16 (5DTE): 600 traded vs OI 148
- **SPY** PUT 761 2026-11-11 (0DTE): 755 traded vs OI 151
- **SPY** PUT 741 2026-11-12 (1DTE): 522 traded vs OI 511
- **SPY** PUT 756 2026-11-13 (2DTE): 2,497 traded vs OI 2,459
- **SPY** PUT 742 2026-11-12 (1DTE): 571 traded vs OI 542
- **SPY** PUT 757 2026-11-16 (5DTE): 619 traded vs OI 95
- **SPY** PUT 755 2026-11-12 (1DTE): 2,280 traded vs OI 1,732
- **SPY** PUT 750 2026-11-12 (1DTE): 2,794 traded vs OI 1,830
- **QQQ** PUT 661 2026-11-11 (0DTE): 566 traded vs OI 323
- **QQQ** PUT 638 2026-11-11 (0DTE): 509 traded vs OI 482
- **QQQ** PUT 683 2026-11-12 (1DTE): 776 traded vs OI 144

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
