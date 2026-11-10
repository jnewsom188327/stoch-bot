# GEX + FLOW SCAN - Tue Nov 10, 10:20 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (3)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:15 | **IWM** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/10 280P | 0.63 | 0.57 | +13% (1m) | **-10%** | +22% | 280 |
| 09:50 | **SPY** | **PUTS** | FLOW SURGE | 11/10 743P | 0.77 | 0.30 | +5% (1m) | **-61%** | +54% | 745.65 |
| 09:45 | **IWM** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/10 279P | 0.52 | 0.28 | +50% (8m) | **-46%** | +87% | 278.66 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:20:08 ET, last candle SPY 10:19, QQQ 10:19 | no errors

## Flow surges NOT fired - price disagreed (6 today, last 5)
- 10:15 BABA PUTS: price +0.24 over the last 15 min - flow says one way, price says the other
- 10:10 BABA PUTS: price +0.73 over the last 15 min - flow says one way, price says the other
- 10:00 NFLX CALLS: price -0.14 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:00 AAPL CALLS: price -2.97 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 09:55 BABA CALLS: price -0.98 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **AMD** | 532.21 | FLOW SURGE | **PUTS** | 55 | none: 129 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (6 contracts' greeks worked out here) | POS +$40.7M | - | 550 | 500 | -$99.0M | +$3.3M bull / -$3.5M bear | out (clean 31, ADX 37, RVol 2.8) |
| 2 | **BABA** | 104.29 | FLOW SURGE | **PUTS** | 49 | none: 21 puts 0-7DTE > 3 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only +20% at the target (needs +20%) | NEG -$4.3M | 105.86 | 110 | 105 | -$579k | +$0 bull / -$134k bear | out (clean 29, ADX 30, RVol 1.5) |
| 3 | **AAPL** | 346.90 | FLOW SURGE | **CALLS** | 47 | none: 84 calls 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (14 contracts' greeks worked out here) | POS +$389.6M | 335.56 | 350 | 340 | +$16.7M | +$737k bull / +$0 bear | out (clean 28, ADX 22, RVol 1.4) |
| 4 | **TSLA** | 376.93 | TREND + FLOW | **PUTS** | 40 | none: 90 puts 0-7DTE > 8 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (7 contracts' greeks worked out here) | POS +$195.0M | - | 400 | 380 | -$7.9M | +$850k bull / -$2.2M bear | SHORT (clean 34, ADX 40, RVol 0.6) |
| 5 | **IWM** | 280.65 | TREND (flow not with it) | **PUTS** | 33 | none: 316 puts 0-7DTE > 21 priced 0.40-0.80 > 2 delta 0.2+ > 2 spread ok > 2 liquid > best one only +17% at the target (needs +20%) (122 contracts' greeks worked out here) | NEG -$850.8M | 284.1 | 285 | 270 | +$993k | +$529k bull / +$0 bear | SHORT (clean 36, ADX 43, RVol 1.4) |
| 6 | **AVGO** | 332.21 | - | **-** | 28 | - | NEG -$11.6M | 346.43 | 340 | 340 | -$8.9M | +$122k bull / -$1.3M bear | out (clean 31, ADX 34, RVol 2.8) |
| 7 | **ARM** | 183.35 | - | **-** | 27 | - | NEG -$4.3M | - | 185 | 190 | -$141k | +$27k bull / +$0 bear | out (clean 27, ADX 24, RVol 0.6) |
| 8 | **SMH** | 488.27 | - | **-** | 23 | - | NEG -$192.9M | - | 500 | 475 | -$1.5M | +$400k bull / -$876k bear | out (clean 29, ADX 24, RVol 1.0) |
| 9 | **PLTR** | 168.01 | - | **-** | 23 | - | POS +$53.9M | - | 165 | 170 | -$604k | +$68k bull / +$0 bear | out (clean 28, ADX 38, RVol 0.5) |
| 10 | **MU** | 730.82 | - | **-** | 23 | - | NEG -$10.9M | - | 750 | 750 | -$34.1M | +$4.3M bull / -$4.0M bear | out (clean 30, ADX 23, RVol 1.2) |
| 11 | **SPY** | 750.63 | - | **-** | 22 | - | NEG -$6.1B | 761.22 | 750 | 730 | -$56.1M | +$1.3M bull / -$5.3M bear | out (clean 32, ADX 30, RVol 0.8) |
| 12 | **QQQ** | 678.20 | - | **-** | 22 | - | NEG -$1.6B | 692.91 | 680 | 680 | -$82.5M | +$916k bull / -$1.3M bear | out (clean 31, ADX 25, RVol 0.8) |
| 13 | **AMZN** | 272.35 | - | **-** | 22 | - | POS +$485.3M | - | 270 | 265 | +$4.5M | +$0 bull / -$235k bear | out (clean 32, ADX 31, RVol 0.9) |
| 14 | **GOOGL** | 290.76 | - | **-** | 21 | - | POS +$20.8M | 288.9 | 300 | 290 | +$1.1M | +$27k bull / -$102k bear | out (clean 30, ADX 17, RVol 2.0) |
| 15 | **ORCL** | 119.69 | - | **-** | 21 | - | NEG -$22.6M | - | 130 | 120 | -$215k | +$26k bull / -$76k bear | out (clean 28, ADX 30, RVol 0.9) |
| 16 | **NVDA** | 172.65 | - | **-** | 20 | - | NEG -$176.2M | - | 185 | 180 | +$1.6M | +$3.1M bull / -$4.4M bear | out (clean 32, ADX 28, RVol 2.5) |
| 17 | **MSFT** | 542.20 | - | **-** | 20 | - | POS +$666.7M | - | 550 | 535 | +$133k | +$108k bull / -$47k bear | out (clean 33, ADX 41, RVol 1.0) |
| 18 | **META** | 643.57 | - | **-** | 18 | - | POS +$266.8M | - | 650 | 650 | -$1.3M | +$200k bull / -$1.0M bear | out (clean 33, ADX 29, RVol 0.7) |
| 19 | **MSTR** | 123.98 | - | **-** | 18 | - | POS +$7.9M | 120.52 | 133 | 120 | +$349k | +$111k bull / +$0 bear | out (clean 30, ADX 24, RVol 0.7) |
| 20 | **CRM** | 213.34 | - | **-** | 17 | - | NEG -$10.8M | - | 195 | 220 | -$93k | - | out (clean 31, ADX 31, RVol 0.7) |
| 21 | **DELL** | 338.66 | - | **-** | 16 | - | NEG -$8.4M | - | 350 | 340 | +$109 | +$182k bull / -$54k bear | out (clean 32, ADX 26, RVol 0.6) |
| 22 | **HOOD** | 82.36 | - | **-** | 15 | - | POS +$4.6M | 78.82 | 85 | 80 | +$376k | - | out (clean 30, ADX 30, RVol 1.2) |
| 23 | **SHOP** | 149.60 | - | **-** | 12 | - | POS +$3.3M | 143.24 | 155 | 140 | -$6k | - | out (clean 31, ADX 36, RVol 0.4) |
| 24 | **NFLX** | 63.04 | - | **-** | 11 | - | NEG -$22.4M | 65.39 | 65 | 60 | -$182k | - | out (clean 30, ADX 32, RVol 1.1) |
| 25 | **SMCI** | 28.50 | - | **-** | 11 | - | POS +$3.8M | - | 30 | 30 | -$90k | - | out (clean 28, ADX 23, RVol 0.5) |
| 26 | **UBER** | 70.19 | - | **-** | 11 | - | POS +$10.0M | 68.34 | 70 | 70 | -$27k | - | out (clean 33, ADX 39, RVol 0.5) |
| 27 | **COIN** | 133.45 | - | **-** | 6 | - | POS +$9.0M | 125.52 | 141 | 135 | -$4k | - | out (clean 31, ADX 24, RVol 0.6) |

## Big prints this scan (242)
- **NVDA** CALL 170 2026-11-13 (3DTE): 1,498 @ 6.21 = **+$930k** BUY | vol 6,000 / OI 389
- **SPY** PUT 748 2026-11-13 (3DTE): 1,791 @ 3.68 = **+$659k** SELL | vol 7,986 / OI 2,268
- **SMH** CALL 480 2026-11-13 (3DTE): 197 @ 18.00 = **+$355k** BUY | vol 309 / OI 194
- **AMD** CALL 510 2026-11-16 (6DTE): 90 @ 38.00 = **+$342k** BUY | vol 332 / OI 49
- **AMD** CALL 510 2026-11-16 (6DTE): 90 @ 37.95 = **+$342k** BUY | vol 332 / OI 49
- **AMD** PUT 530 2026-11-11 (1DTE): 223 @ 10.00 = **+$223k** SELL | vol 850 / OI 45
- **SPY** PUT 752 2026-11-11 (1DTE): 500 @ 3.70 = **+$185k** SELL | vol 1,897 / OI 281
- **QQQ** CALL 662 2026-11-13 (3DTE): 90 @ 20.50 = **+$184k** BUY | vol 207 / OI 426
- **SPY** PUT 748 2026-11-13 (3DTE): 500 @ 3.68 = **+$184k** SELL | vol 7,986 / OI 2,268
- **NVDA** CALL 172.5 2026-11-16 (6DTE): 314 @ 5.60 = **+$176k** BUY | vol 3,426 / OI 10
- **AMD** PUT 530 2026-11-13 (3DTE): 100 @ 14.80 = **+$148k** SELL | vol 441 / OI 380
- **IWM** PUT 283 2026-11-11 (1DTE): 499 @ 2.90 = **+$145k** SELL | vol 1,137 / OI 359
- **MU** CALL 750 2026-11-11 (1DTE): 100 @ 13.95 = **+$140k** BUY | vol 4,308 / OI 728
- **MU** CALL 750 2026-11-11 (1DTE): 99 @ 14.00 = **+$139k** BUY | vol 4,308 / OI 728
- **SPY** CALL 748 2026-11-10 (0DTE): 297 @ 4.44 = **+$132k** BUY | vol 28,129 / OI 4,785

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 753 2026-11-12 (2DTE): 823 traded vs OI 646
- **SPY** PUT 734 2026-11-10 (0DTE): 10,042 traded vs OI 9,952
- **SPY** CALL 752 2026-11-12 (2DTE): 692 traded vs OI 685
- **SPY** PUT 731 2026-11-11 (1DTE): 1,089 traded vs OI 943
- **SPY** PUT 745 2026-11-16 (6DTE): 600 traded vs OI 441
- **QQQ** CALL 693 2026-11-11 (1DTE): 584 traded vs OI 567
- **QQQ** PUT 629 2026-11-10 (0DTE): 811 traded vs OI 42
- **QQQ** CALL 697 2026-11-10 (0DTE): 513 traded vs OI 123
- **QQQ** PUT 679 2026-11-11 (1DTE): 911 traded vs OI 320
- **QQQ** PUT 683 2026-11-10 (0DTE): 765 traded vs OI 97
- **QQQ** PUT 684 2026-11-10 (0DTE): 526 traded vs OI 123
- **IWM** PUT 283 2026-11-11 (1DTE): 1,137 traded vs OI 359
- **IWM** CALL 286 2026-11-10 (0DTE): 2,097 traded vs OI 2,066
- **IWM** CALL 287 2026-11-10 (0DTE): 1,629 traded vs OI 1,616
- **IWM** CALL 285 2026-11-11 (1DTE): 961 traded vs OI 744

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
