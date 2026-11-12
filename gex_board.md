# GEX + FLOW SCAN - Thu Nov 12, 09:50 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (4)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 09:50 | **HOOD** | **PUTS** | TREND + FLOW | 11/13 79P | 0.55 | 0.49 | -11% (0m) | **-11%** | +92% | 80 |
| 09:45 | **ORCL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/13 130C | 0.75 | 0.61 | -4% (2m) | **-19%** | +59% | 126.9 |
| 09:45 | **SMCI** | **PUTS** | TREND + FLOW | 11/13 27P | 0.42 | 0.37 | -12% (0m) | **-12%** | +57% | 27 |
| 09:45 | **SPY** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/12 753P | 0.79 | 0.72 | +6% (1m) | **-9%** | +51% | 754.88 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 09:50:08 ET, last candle SPY 09:49, QQQ 09:49 | no errors

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **NVDA** | 159.57 | RUN: clean trend + negative gamma + flow agrees | **PUTS** | 91 | none: 51 puts 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (8 contracts' greeks worked out here) | NEG -$192.3M | - | 170 | 160 | -$73.0M | +$0 bull / -$18.7M bear | SHORT (clean 34, ADX 43, RVol 5.5) |
| 2 | **QQQ** | 686.30 | RUN: clean trend + negative gamma + flow agrees | **PUTS** | 81 | none: 696 puts 0-7DTE > 62 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (265 contracts' greeks worked out here) | NEG -$875.4M | 690.41 | 700 | 680 | -$25.9M | +$0 bull / -$3.4M bear | SHORT (clean 33, ADX 40, RVol 3.3) |
| 3 | **SPY** | 757.32 | RUN: clean trend + negative gamma + flow agrees | **PUTS** | 79 | 11/12 753P @ 0.74 (delta 0.22) = est +60% at 754.85 | NEG -$2.8B | 760.95 | 760 | 760 | -$25.5M | +$0 bull / -$2.2M bear | SHORT (clean 33, ADX 32, RVol 2.5) |
| 4 | **DELL** | 359.75 | TREND + FLOW | **PUTS** | 77 | none: 29 puts 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (5 contracts' greeks worked out here) | POS +$2.6M | 346.47 | 360 | 340 | -$1.5M | +$0 bull / -$615k bear | SHORT (clean 38, ADX 41, RVol 4.0) |
| 5 | **ORCL** | 125.01 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 64 | 11/13 130C @ 0.74 (delta 0.22) = est +55% at 127.11 | POS +$8.1M | 120.2 | 130 | 125 | -$599k | +$0 bull / -$558k bear | out (clean 30, ADX 25, RVol 2.5) |
| 6 | **AVGO** | 358.08 | TREND + FLOW | **CALLS** | 63 | none: 83 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (5 contracts' greeks worked out here) | POS +$125.0M | - | 350 | 350 | +$1.4M | +$564k bull / -$97k bear | LONG (clean 37, ADX 48, RVol 6.0) |
| 7 | **SMCI** | 27.77 | TREND + FLOW | **PUTS** | 63 | 11/13 27P @ 0.44 (delta 0.32) = est +83% at 26.69 | POS +$2.0M | 26.69 | 30 | 25 | -$38k | - | SHORT (clean 34, ADX 47, RVol 3.1) |
| 8 | **HOOD** | 82.18 | TREND + FLOW | **PUTS** | 58 | 11/13 79P @ 0.55 (delta 0.21) = est +92% at 80 | POS +$8.3M | 79.8 | 85 | 80 | -$123k | - | SHORT (clean 35, ADX 26, RVol 3.3) |
| 9 | **AMD** | 564.44 | FLOW SURGE | **PUTS** | 55 | none: 135 puts 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (9 contracts' greeks worked out here) | POS +$183.8M | - | 600 | 550 | -$7.7M | +$246k bull / -$1.6M bear | LONG (clean 36, ADX 33, RVol 3.8) |
| 10 | **AMZN** | 271.71 | FLOW SURGE | **PUTS** | 55 | none: 66 puts 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (4 contracts' greeks worked out here) | POS +$523.1M | - | 270 | 270 | -$4.0M | +$0 bull / -$441k bear | out (clean 31, ADX 27, RVol 2.4) |
| 11 | **ARM** | 199.63 | PINNED between the walls (positive gamma) - chop | **-** | 52 | - | POS +$8.6M | - | 200 | 200 | -$113k | - | out (clean 32, ADX 25, RVol 3.0) |
| 12 | **MU** | 783.47 | TREND (flow not with it) | **PUTS** | 48 | none: 125 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (6 contracts' greeks worked out here) | POS +$86.8M | - | 800 | 800 | +$5.2M | +$774k bull / -$6.7M bear | SHORT (clean 33, ADX 33, RVol 2.0) |
| 13 | **COIN** | 130.81 | FLIP CROSS up into positive gamma | **CALLS** | 45 | none: 26 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (6 contracts' greeks worked out here) | NEG -$623k | 130.47 | 137 | 135 | +$64k | - | out (clean 31, ADX 43, RVol 1.8) |
| 14 | **IWM** | 281.02 | TREND (flow not with it) | **PUTS** | 44 | 11/12 280P @ 0.62 (delta 0.34) = est +128% at 279 | NEG -$850.2M | 283 | 285 | 275 | +$911k | +$50k bull / +$0 bear | SHORT (clean 35, ADX 33, RVol 2.6) |
| 15 | **META** | 623.89 | - | **-** | 33 | - | NEG -$3.8M | 622.73 | 650 | 600 | +$1.1M | +$464k bull / -$65k bear | out (clean 30, ADX 52, RVol 2.8) |
| 16 | **BABA** | 94.08 | - | **-** | 31 | - | NEG -$16.4M | - | 100 | 100 | +$194k | - | out (clean 28, ADX 36, RVol 6.2) |
| 17 | **GOOGL** | 295.53 | - | **-** | 29 | - | POS +$98.6M | 288.69 | 300 | 290 | +$884k | +$75k bull / -$106k bear | out (clean 30, ADX 26, RVol 3.8) |
| 18 | **NFLX** | 63.50 | - | **-** | 29 | - | NEG -$12.5M | 64.23 | 65 | 65 | +$66k | - | out (clean 27, ADX 35, RVol 2.2) |
| 19 | **SHOP** | 148.60 | - | **-** | 29 | - | POS +$5.4M | 142.3 | 150 | 140 | -$2k | - | out (clean 32, ADX 24, RVol 2.8) |
| 20 | **AAPL** | 357.32 | - | **-** | 28 | - | POS +$1.1B | 337.76 | 360 | 360 | -$1.1M | +$97k bull / -$251k bear | out (clean 28, ADX 40, RVol 2.3) |
| 21 | **PLTR** | 170.49 | - | **-** | 28 | - | POS +$87.0M | - | 170 | 170 | -$215k | +$0 bull / -$55k bear | out (clean 29, ADX 28, RVol 2.2) |
| 22 | **SMH** | 495.10 | - | **-** | 26 | - | NEG -$154.6M | - | 500 | 475 | -$387k | +$0 bull / -$1.3M bear | out (clean 32, ADX 44, RVol 1.5) |
| 23 | **TSLA** | 393.13 | - | **-** | 22 | - | POS +$380.8M | - | 400 | 380 | +$2.2M | +$272k bull / -$1.2M bear | out (clean 31, ADX 30, RVol 2.0) |
| 24 | **MSFT** | 524.93 | - | **-** | 22 | - | POS +$110.1M | 519.62 | 535 | 520 | -$132k | +$0 bull / -$513k bear | out (clean 32, ADX 30, RVol 2.5) |
| 25 | **MSTR** | 113.31 | - | **-** | 22 | - | NEG -$30.0M | - | 120 | 110 | +$48k | +$77k bull / -$65k bear | out (clean 28, ADX 33, RVol 4.5) |
| 26 | **UBER** | 70.35 | - | **-** | 17 | - | POS +$18.9M | 68.35 | 70 | 70 | -$1k | - | out (clean 31, ADX 28, RVol 2.9) |
| 27 | **CRM** | 216.35 | - | **-** | 13 | - | NEG -$9.3M | - | 220 | 220 | -$20k | - | out (clean 28, ADX 23, RVol 2.3) |

## Big prints this scan (595)
- **AMD** PUT 575 2026-11-13 (1DTE): 998 @ 18.00 = **+$1.8M** MID | vol 1,066 / OI 31
- **NVDA** CALL 162.5 2026-11-18 (6DTE): 2,196 @ 3.70 = **+$813k** SELL | vol 2,438 / OI 61
- **NVDA** PUT 160 2026-11-13 (1DTE): 659 @ 9.41 = **+$620k** BUY | vol 10,252 / OI 24,121
- **SPY** PUT 763 2026-11-16 (4DTE): 600 @ 9.50 = **+$570k** BUY | vol 2,002 / OI 216
- **SPY** PUT 763 2026-11-16 (4DTE): 547 @ 9.50 = **+$520k** BUY | vol 2,002 / OI 216
- **NVDA** PUT 155 2026-11-13 (1DTE): 659 @ 6.27 = **+$413k** BUY | vol 21,787 / OI 9,956
- **DELL** PUT 352.5 2026-11-13 (1DTE): 299 @ 12.45 = **+$372k** BUY | vol 308 / OI 104
- **SPY** PUT 763 2026-11-16 (4DTE): 368 @ 9.50 = **+$350k** BUY | vol 2,002 / OI 216
- **NVDA** PUT 155 2026-11-18 (6DTE): 400 @ 8.25 = **+$330k** BUY | vol 965 / OI 1,510
- **SPY** PUT 760 2026-11-13 (1DTE): 500 @ 6.40 = **+$320k** BUY | vol 1,835 / OI 27,552
- **SMH** PUT 515 2026-11-13 (1DTE): 100 @ 30.00 = **+$300k** BUY | vol 102 / OI 198
- **NVDA** PUT 160 2026-11-13 (1DTE): 315 @ 9.41 = **+$296k** BUY | vol 10,252 / OI 24,121
- **QQQ** PUT 695 2026-11-13 (1DTE): 212 @ 13.80 = **+$293k** BUY | vol 1,176 / OI 4,281
- **QQQ** PUT 680 2026-11-13 (1DTE): 500 @ 5.77 = **+$288k** BUY | vol 5,063 / OI 5,045
- **NVDA** CALL 160 2026-11-13 (1DTE): 1,434 @ 2.00 = **+$287k** SELL | vol 36,017 / OI 2,015

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 754 2026-11-12 (0DTE): 4,750 traded vs OI 3,346
- **SPY** CALL 789 2026-11-18 (6DTE): 1,000 traded vs OI 42
- **SPY** CALL 759 2026-11-12 (0DTE): 7,000 traded vs OI 3,545
- **SPY** CALL 766 2026-11-12 (0DTE): 2,501 traded vs OI 748
- **SPY** CALL 771 2026-11-12 (0DTE): 1,179 traded vs OI 438
- **SPY** CALL 768 2026-11-12 (0DTE): 2,547 traded vs OI 1,007
- **SPY** PUT 759 2026-11-13 (1DTE): 973 traded vs OI 972
- **SPY** CALL 762 2026-11-12 (0DTE): 4,707 traded vs OI 2,051
- **SPY** PUT 711 2026-11-12 (0DTE): 2,295 traded vs OI 1,312
- **SPY** CALL 753 2026-11-12 (0DTE): 2,381 traded vs OI 1,361
- **SPY** CALL 764 2026-11-12 (0DTE): 6,352 traded vs OI 1,554
- **SPY** CALL 783 2026-11-17 (5DTE): 599 traded vs OI 361
- **SPY** CALL 754 2026-11-16 (4DTE): 501 traded vs OI 379
- **SPY** CALL 757 2026-11-16 (4DTE): 564 traded vs OI 424
- **SPY** PUT 719 2026-11-12 (0DTE): 2,483 traded vs OI 314

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
