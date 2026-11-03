# GEX + FLOW SCAN - Tue Nov 03, 10:40 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:40:08 ET, last candle SPY 10:39, QQQ 10:39 | no errors

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **ORCL** | 125.40 | FLOW SURGE | **PUTS** | 51 | none: 25 puts 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$40.6M | - | 135 | 125 | -$6.5M | +$0 bull / -$267k bear | out (clean 33, ADX 47, RVol 1.5) |
| 2 | **COIN** | 147.06 | FLOW SURGE | **PUTS** | 47 | none: 22 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$20.8M | - | 148 | 150 | -$1.6M | +$0 bull / -$87k bear | out (clean 27, ADX 55, RVol 1.0) |
| 3 | **MSTR** | 135.29 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 46 | none: 27 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$79.5M | - | 135 | 125 | -$2.7M | +$0 bull / -$27k bear | out (clean 28, ADX 36, RVol 0.6) |
| 4 | **BABA** | 100.58 | TREND (flow not with it) | **PUTS** | 43 | none: 20 puts 0-7DTE > 2 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only +10% at the target (needs +20%) (1 contracts' greeks worked out here) | POS +$2.5M | 99.82 | 102 | 100 | +$198k | - | SHORT (clean 35, ADX 58, RVol 1.1) |
| 5 | **MSFT** | 514.42 | FLOW SURGE | **PUTS** | 41 | none: 122 puts 0-7DTE > 11 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (21 contracts' greeks worked out here) | POS +$165.7M | 501.06 | 540 | 500 | -$5.8M | +$0 bull / -$173k bear | out (clean 29, ADX 34, RVol 1.1) |
| 6 | **META** | 617.24 | FLOW SURGE | **PUTS** | 39 | none: 146 puts 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (18 contracts' greeks worked out here) | NEG -$51.4M | 625.94 | 650 | 610 | -$13.0M | +$0 bull / -$987k bear | out (clean 27, ADX 33, RVol 0.4) |
| 7 | **GOOGL** | 277.26 | TREND (flow not with it) | **PUTS** | 31 | none: 66 puts 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (3 contracts' greeks worked out here) | NEG -$49.5M | 285.4 | 285 | 290 | +$3.6M | +$343k bull / +$0 bear | SHORT (clean 34, ADX 36, RVol 0.5) |
| 8 | **SHOP** | 144.00 | - | **-** | 31 | - | NEG -$3.8M | - | 145 | 140 | -$4.1M | - | out (clean 32, ADX 53, RVol 2.7) |
| 9 | **DELL** | 409.02 | - | **-** | 28 | - | NEG -$25.9M | - | 440 | 400 | +$1.9M | +$128k bull / -$145k bear | out (clean 35, ADX 33, RVol 0.8) |
| 10 | **AVGO** | 333.07 | - | **-** | 25 | - | NEG -$59.2M | - | 340 | 340 | +$2.6M | +$0 bull / -$190k bear | out (clean 32, ADX 35, RVol 0.7) |
| 11 | **PLTR** | 169.76 | - | **-** | 25 | - | NEG -$28.3M | - | 165 | 180 | +$1.4M | +$158k bull / -$243k bear | out (clean 28, ADX 57, RVol 2.4) |
| 12 | **SMH** | 519.45 | - | **-** | 22 | - | NEG -$276.6M | - | 532.5 | 500 | +$1.1M | +$785k bull / +$0 bear | out (clean 33, ADX 31, RVol 0.8) |
| 13 | **IWM** | 281.51 | - | **-** | 21 | - | NEG -$925.1M | 287.11 | 285 | 270 | -$4.1M | +$0 bull / -$54k bear | out (clean 33, ADX 21, RVol 1.0) |
| 14 | **AMD** | 488.13 | - | **-** | 21 | - | NEG -$87.0M | - | 520 | 440 | +$3.8M | +$1.2M bull / -$305k bear | out (clean 33, ADX 40, RVol 1.0) |
| 15 | **SMCI** | 31.58 | - | **-** | 21 | - | POS +$2.1M | - | 34.5 | 30 | -$253k | +$25k bull / +$0 bear | out (clean 35, ADX 29, RVol 1.3) |
| 16 | **HOOD** | 84.95 | - | **-** | 21 | - | NEG -$2.7M | - | 90 | 90 | -$487k | +$0 bull / -$64k bear | out (clean 31, ADX 22, RVol 0.8) |
| 17 | **NVDA** | 207.20 | - | **-** | 20 | - | POS +$98.8M | 203.66 | 210 | 200 | +$5.7M | +$337k bull / +$0 bear | out (clean 31, ADX 36, RVol 0.6) |
| 18 | **AAPL** | 329.57 | - | **-** | 20 | - | NEG -$412.3M | 342.74 | 350 | 330 | -$6.3M | +$1.6M bull / +$0 bear | out (clean 32, ADX 33, RVol 1.3) |
| 19 | **SPY** | 754.20 | - | **-** | 19 | - | NEG -$8.9B | 770.15 | 770 | 750 | -$42.0M | +$1.2M bull / -$2.1M bear | out (clean 31, ADX 21, RVol 0.8) |
| 20 | **TSLA** | 401.50 | - | **-** | 19 | - | POS +$242.3M | - | 400 | 400 | +$12.0M | +$898k bull / -$747k bear | out (clean 31, ADX 20, RVol 0.7) |
| 21 | **MU** | 857.47 | - | **-** | 17 | - | NEG -$192.1M | - | 900 | 850 | -$3.9M | +$1.2M bull / -$3.7M bear | out (clean 32, ADX 31, RVol 0.6) |
| 22 | **QQQ** | 685.22 | - | **-** | 16 | - | NEG -$5.1B | - | 700 | 680 | -$2.0M | +$821k bull / -$409k bear | out (clean 32, ADX 24, RVol 0.7) |
| 23 | **CRM** | 220.88 | - | **-** | 16 | - | NEG -$14.7M | - | 240 | 220 | -$289k | - | out (clean 28, ADX 45, RVol 0.3) |
| 24 | **NFLX** | 62.45 | - | **-** | 11 | - | NEG -$12.7M | 64.42 | 63 | 60 | -$189k | - | out (clean 28, ADX 28, RVol 0.7) |
| 25 | **UBER** | 66.58 | - | **-** | 11 | - | NEG -$13.2M | - | 70 | 65 | -$37k | - | out (clean 29, ADX 22, RVol 0.8) |
| 26 | **ARM** | 203.66 | - | **-** | 10 | - | NEG -$6.5M | - | 220 | 200 | -$100k | - | out (clean 25, ADX 29, RVol 0.4) |
| 27 | **AMZN** | 246.10 | - | **-** | 9 | - | POS +$121.5M | 236.27 | 250 | 250 | +$1.3M | - | out (clean 34, ADX 25, RVol 0.6) |

## Big prints this scan (119)
- **SPY** CALL 745 2026-11-05 (2DTE): 500 @ 11.51 = **+$576k** SELL | vol 4,161 / OI 186
- **SPY** CALL 745 2026-11-05 (2DTE): 500 @ 11.51 = **+$576k** SELL | vol 4,161 / OI 186
- **TSLA** PUT 402.5 2026-11-04 (1DTE): 223 @ 6.85 = **+$153k** BUY | vol 7,318 / OI 654
- **SPY** CALL 740 2026-11-03 (0DTE): 100 @ 14.75 = **+$148k** SELL | vol 288 / OI 235
- **TSLA** PUT 402.5 2026-11-04 (1DTE): 190 @ 6.85 = **+$130k** BUY | vol 7,318 / OI 654
- **SPY** CALL 755 2026-11-03 (0DTE): 764 @ 1.64 = **+$125k** SELL | vol 128,668 / OI 1,485
- **QQQ** PUT 684 2026-11-04 (1DTE): 200 @ 6.09 = **+$122k** BUY | vol 3,780 / OI 263
- **QQQ** PUT 684 2026-11-03 (0DTE): 500 @ 2.10 = **+$105k** BUY | vol 46,629 / OI 507
- **DELL** CALL 407.5 2026-11-06 (3DTE): 62 @ 16.50 = **+$102k** MID | vol 502 / OI 0
- **TSLA** PUT 402.5 2026-11-04 (1DTE): 145 @ 6.85 = **+$99k** BUY | vol 7,318 / OI 654
- **PLTR** PUT 170 2026-11-06 (3DTE): 160 @ 4.80 = **+$77k** BUY | vol 7,114 / OI 2,434
- **META** CALL 617.5 2026-11-04 (1DTE): 100 @ 7.64 = **+$76k** SELL | vol 3,088 / OI 106
- **META** CALL 617.5 2026-11-04 (1DTE): 100 @ 7.59 = **+$76k** SELL | vol 3,088 / OI 106
- **META** CALL 620 2026-11-04 (1DTE): 100 @ 6.33 = **+$63k** SELL | vol 4,179 / OI 383
- **DELL** CALL 407.5 2026-11-06 (3DTE): 38 @ 16.50 = **+$63k** MID | vol 502 / OI 0

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 774 2026-11-04 (1DTE): 1,280 traded vs OI 1,135
- **SPY** PUT 761 2026-11-03 (0DTE): 1,022 traded vs OI 995
- **SPY** CALL 760 2026-11-05 (2DTE): 2,111 traded vs OI 2,040
- **SPY** CALL 744 2026-11-03 (0DTE): 502 traded vs OI 67
- **SPY** PUT 749 2026-11-04 (1DTE): 996 traded vs OI 985
- **SPY** CALL 771 2026-11-04 (1DTE): 3,007 traded vs OI 2,935
- **SPY** PUT 755 2026-11-04 (1DTE): 5,457 traded vs OI 5,209
- **SPY** PUT 726 2026-11-04 (1DTE): 630 traded vs OI 504
- **QQQ** PUT 687 2026-11-09 (6DTE): 520 traded vs OI 0
- **QQQ** PUT 650 2026-11-03 (0DTE): 5,685 traded vs OI 4,606
- **QQQ** PUT 683 2026-11-06 (3DTE): 1,426 traded vs OI 1,342
- **QQQ** CALL 697 2026-11-04 (1DTE): 568 traded vs OI 470
- **QQQ** PUT 652 2026-11-05 (2DTE): 917 traded vs OI 0
- **QQQ** PUT 686 2026-11-06 (3DTE): 1,390 traded vs OI 1,249
- **QQQ** PUT 662 2026-11-03 (0DTE): 638 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
