# GEX + FLOW SCAN - Wed Nov 11, 10:05 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (6)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:05 | **NVDA** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/11 175C | 0.76 | 0.75 | -1% (0m) | **-1%** | +58% | 175 |
| 09:50 | **GOOGL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/11 292.5C | 0.51 | 0.51 | +14% (6m) | **+0%** | +82% | 291.86 |
| 09:45 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/11 282C | 0.68 | 0.61 | +85% (6m) | **-10%** | +68% | 282.96 |
| 09:45 | **QQQ** | **CALLS** | FLOW SURGE | 11/11 690C | 0.63 | 0.70 | +13% (1m) | **+11%** | +171% | 689.78 |
| 09:39 | **QQQ** | **CALLS** | 1m WHIPSAW (R1 R5) | 11/11 693C | 0.52 | 0.23 | -10% (0m) | **-56%** | +92% | 690.43 |
| 09:39 | **SPY** | **CALLS** | 1m WHIPSAW (R1 R5) | 11/11 760C | 0.53 | 0.28 | -2% (0m) | **-47%** | +79% | 758.82 |

## 1m RULES on SPY / QQQ - loose (3 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:05:08 ET, last candle SPY 10:04, QQQ 10:04 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 10:02 | QQQ | 1m AGREE FLIP | FULL | CALLS | up | logged (agree flip) |
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
| 1 | **DELL** | 367.65 | TREND (flow not with it) | **CALLS** | 58 | none: 29 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$945k | - | 380 | 340 | -$933k | +$68k bull / +$0 bear | LONG (clean 35, ADX 47, RVol 2.2) |
| 2 | **NVDA** | 173.41 | RUN: clean trend + negative gamma + flow agrees | **CALLS** | 56 | 11/11 175C @ 0.76 (delta 0.33) = est +58% at 175 | NEG -$187.2M | - | 180 | 175 | +$2.6M | +$3.8M bull / -$3.1M bear | LONG (clean 34, ADX 26, RVol 1.2) |
| 3 | **AVGO** | 353.41 | TREND + FLOW | **CALLS** | 56 | none: 110 calls 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (44 contracts' greeks worked out here) | POS +$89.7M | - | 350 | 350 | +$122k | +$1.8M bull / -$819k bear | LONG (clean 35, ADX 49, RVol 2.6) |
| 4 | **MU** | 794.83 | FLOW SURGE | **PUTS** | 49 | none: 157 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (70 contracts' greeks worked out here) | POS +$160.2M | - | 800 | 800 | -$77.3M | +$0 bull / -$7.3M bear | out (clean 32, ADX 47, RVol 1.7) |
| 5 | **BABA** | 101.44 | FLOW SURGE | **CALLS** | 48 | none: 20 calls 0-7DTE > 2 priced 0.40-0.80 > 2 delta 0.2+ > 2 spread ok > 2 liquid > best one only +17% at the target (needs +20%) | NEG -$15.5M | 106.6 | 110 | 101 | +$304k | +$112k bull / +$0 bear | out (clean 29, ADX 30, RVol 1.0) |
| 6 | **MSFT** | 527.38 | FLOW SURGE | **CALLS** | 47 | none: 172 calls 0-7DTE > 9 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (84 contracts' greeks worked out here) | POS +$231.2M | 513.65 | 535 | 520 | +$4.4M | +$380k bull / +$0 bear | out (clean 31, ADX 26, RVol 1.8) |
| 7 | **AMD** | 539.06 | FLOW SURGE | **PUTS** | 45 | none: 172 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (81 contracts' greeks worked out here) | POS +$130.6M | - | 550 | 500 | -$28.4M | +$626k bull / -$6.0M bear | out (clean 33, ADX 30, RVol 1.6) |
| 8 | **AMZN** | 269.13 | FLOW SURGE | **CALLS** | 44 | 11/11 270C @ 0.80 (delta 0.38) = est +20% at 270 | POS +$500.1M | - | 270 | 265 | +$4.8M | +$89k bull / +$0 bear | out (clean 33, ADX 30, RVol 1.1) |
| 9 | **GOOGL** | 290.61 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 43 | 11/11 292.5C @ 0.52 (delta 0.27) = est +109% at 292.6 | POS +$31.1M | 289.1 | 300 | 290 | +$368k | +$82k bull / -$28k bear | out (clean 28, ADX 39, RVol 1.2) |
| 10 | **PLTR** | 171.13 | FLOW SURGE | **CALLS** | 42 | none: 14 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (2 contracts' greeks worked out here) | POS +$73.2M | - | 170 | 170 | +$1.8M | +$86k bull / +$0 bear | out (clean 30, ADX 42, RVol 0.8) |
| 11 | **IWM** | 281.95 | TREND (flow not with it) | **CALLS** | 31 | 11/11 282C @ 0.67 (delta 0.49) = est +62% at 282.85 | NEG -$371.5M | 282.85 | 285 | 270 | -$1.0M | +$0 bull / -$91k bear | LONG (clean 35, ADX 37, RVol 1.2) |
| 12 | **ORCL** | 125.64 | - | **-** | 28 | - | NEG -$2.9M | 129.15 | 130 | 125 | +$849k | +$281k bull / -$50k bear | out (clean 28, ADX 39, RVol 2.0) |
| 13 | **AAPL** | 353.53 | - | **-** | 24 | - | POS +$1.3B | 340.59 | 355 | 350 | -$3.2M | +$394k bull / -$546k bear | out (clean 27, ADX 39, RVol 1.7) |
| 14 | **SMH** | 502.40 | - | **-** | 23 | - | NEG -$81.5M | - | 500 | 475 | +$394k | +$0 bull / -$29k bear | out (clean 30, ADX 33, RVol 2.3) |
| 15 | **ARM** | 192.60 | - | **-** | 23 | - | POS +$1.2M | 189.73 | 200 | 200 | -$260k | - | out (clean 28, ADX 49, RVol 0.5) |
| 16 | **QQQ** | 686.36 | - | **-** | 21 | - | NEG -$701.9M | 689.73 | 700 | 680 | +$10.9M | +$3.0M bull / -$6.5M bear | out (clean 32, ADX 44, RVol 0.8) |
| 17 | **TSLA** | 389.64 | - | **-** | 21 | - | POS +$385.3M | - | 400 | 380 | +$5.1M | +$1.6M bull / -$1.3M bear | out (clean 32, ADX 38, RVol 0.9) |
| 18 | **META** | 639.12 | - | **-** | 21 | - | POS +$255.7M | 623.56 | 650 | 625 | +$1.4M | +$2.9M bull / -$43k bear | out (clean 31, ADX 27, RVol 1.4) |
| 19 | **SMCI** | 29.71 | - | **-** | 21 | - | POS +$10.4M | - | 30 | 30 | -$191k | - | out (clean 31, ADX 39, RVol 1.1) |
| 20 | **SPY** | 756.38 | - | **-** | 20 | - | NEG -$4.1B | 761.02 | 760 | 750 | +$8.2M | +$140k bull / -$498k bear | out (clean 32, ADX 46, RVol 0.5) |
| 21 | **COIN** | 133.64 | - | **-** | 16 | - | POS +$15.6M | 126.94 | 137 | 135 | +$150k | - | out (clean 29, ADX 31, RVol 0.6) |
| 22 | **MSTR** | 121.00 | - | **-** | 16 | - | NEG -$7.0M | 123.47 | 133 | 120 | -$167k | +$133k bull / +$0 bear | out (clean 29, ADX 16, RVol 0.9) |
| 23 | **CRM** | 214.81 | - | **-** | 15 | - | NEG -$11.5M | - | 195 | 220 | -$20k | - | out (clean 31, ADX 30, RVol 1.2) |
| 24 | **NFLX** | 63.17 | - | **-** | 14 | - | NEG -$14.5M | 64.4 | 65 | 65 | +$153k | - | out (clean 28, ADX 20, RVol 1.1) |
| 25 | **SHOP** | 148.29 | - | **-** | 14 | - | POS +$3.0M | 144.33 | 150 | 140 | -$3k | - | out (clean 33, ADX 43, RVol 0.4) |
| 26 | **HOOD** | 82.88 | - | **-** | 13 | - | POS +$9.2M | 78.95 | 85 | 80 | -$108k | - | out (clean 32, ADX 28, RVol 1.1) |
| 27 | **UBER** | 69.47 | - | **-** | 7 | - | POS +$9.6M | 68.17 | 70 | 70 | +$2k | - | out (clean 33, ADX 23, RVol 0.7) |

## Big prints this scan (164)
- **QQQ** CALL 685 2026-11-13 (2DTE): 3,000 @ 6.32 = **+$1.9M** SELL | vol 7,107 / OI 8,669
- **QQQ** CALL 685 2026-11-13 (2DTE): 600 @ 6.32 = **+$379k** SELL | vol 7,107 / OI 8,669
- **QQQ** CALL 685 2026-11-13 (2DTE): 600 @ 6.32 = **+$379k** SELL | vol 7,107 / OI 8,669
- **QQQ** CALL 685 2026-11-13 (2DTE): 600 @ 6.32 = **+$379k** SELL | vol 7,107 / OI 8,669
- **QQQ** CALL 685 2026-11-13 (2DTE): 600 @ 6.32 = **+$379k** SELL | vol 7,107 / OI 8,669
- **QQQ** CALL 685 2026-11-13 (2DTE): 600 @ 6.32 = **+$379k** SELL | vol 7,107 / OI 8,669
- **QQQ** CALL 683 2026-11-12 (1DTE): 500 @ 5.60 = **+$280k** SELL | vol 925 / OI 730
- **AMD** PUT 530 2026-11-13 (2DTE): 154 @ 18.00 = **+$277k** BUY | vol 1,118 / OI 425
- **QQQ** PUT 685 2026-11-12 (1DTE): 546 @ 5.03 = **+$275k** BUY | vol 5,900 / OI 479
- **AMD** CALL 535 2026-11-11 (0DTE): 850 @ 3.00 = **+$255k** SELL | vol 5,595 / OI 268
- **QQQ** PUT 685 2026-11-12 (1DTE): 489 @ 5.06 = **+$247k** BUY | vol 5,900 / OI 479
- **QQQ** PUT 685 2026-11-12 (1DTE): 417 @ 5.04 = **+$210k** BUY | vol 5,900 / OI 479
- **NVDA** CALL 172.5 2026-11-11 (0DTE): 1,520 @ 1.33 = **+$202k** SELL | vol 23,925 / OI 1,302
- **QQQ** PUT 685 2026-11-12 (1DTE): 365 @ 5.04 = **+$184k** BUY | vol 5,900 / OI 479
- **NVDA** CALL 172.5 2026-11-11 (0DTE): 1,241 @ 1.33 = **+$165k** SELL | vol 23,925 / OI 1,302

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 755 2026-11-12 (1DTE): 1,725 traded vs OI 1,511
- **SPY** CALL 788 2026-11-17 (6DTE): 600 traded vs OI 361
- **SPY** PUT 740 2026-11-11 (0DTE): 7,192 traded vs OI 5,417
- **SPY** PUT 748 2026-11-12 (1DTE): 874 traded vs OI 658
- **SPY** CALL 772 2026-11-11 (0DTE): 1,776 traded vs OI 1,620
- **SPY** PUT 726 2026-11-11 (0DTE): 1,203 traded vs OI 964
- **SPY** CALL 758 2026-11-16 (5DTE): 521 traded vs OI 317
- **SPY** CALL 767 2026-11-12 (1DTE): 1,083 traded vs OI 1,062
- **SPY** CALL 764 2026-11-12 (1DTE): 1,148 traded vs OI 966
- **SPY** PUT 746 2026-11-12 (1DTE): 744 traded vs OI 533
- **SPY** CALL 757 2026-11-16 (5DTE): 616 traded vs OI 326
- **SPY** PUT 740 2026-11-17 (6DTE): 1,005 traded vs OI 1,003
- **SPY** PUT 757 2026-11-18 (7DTE): 565 traded vs OI 172
- **SPY** CALL 815 2026-11-18 (7DTE): 3,820 traded vs OI 39
- **SPY** PUT 756 2026-12-11 (30DTE): 732 traded vs OI 285

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
