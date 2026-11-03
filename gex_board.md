# GEX + FLOW SCAN - Tue Nov 03, 11:00 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 11:00:08 ET, last candle SPY 10:59, QQQ 10:59 | no errors

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **COIN** | 149.89 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 59 | none: 21 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$20.3M | - | 148 | 150 | -$3.3M | +$0 bull / -$346k bear | out (clean 28, ADX 62, RVol 1.2) |
| 2 | **ORCL** | 126.31 | FLOW SURGE | **PUTS** | 46 | none: 25 puts 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$39.4M | - | 135 | 125 | -$7.5M | +$0 bull / -$175k bear | out (clean 33, ADX 52, RVol 0.8) |
| 3 | **MSTR** | 137.81 | FLOW SURGE | **PUTS** | 42 | none: 26 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$84.9M | - | 135 | 125 | -$4.5M | +$0 bull / -$1.6M bear | out (clean 28, ADX 44, RVol 1.2) |
| 4 | **META** | 621.55 | FLOW SURGE | **PUTS** | 41 | none: 150 puts 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (1 contracts' greeks worked out here) | NEG -$37.8M | 627.27 | 650 | 610 | -$16.5M | +$0 bull / -$309k bear | out (clean 28, ADX 40, RVol 0.5) |
| 5 | **MSFT** | 516.78 | FLOW SURGE | **PUTS** | 37 | none: 122 puts 0-7DTE > 12 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (14 contracts' greeks worked out here) | POS +$182.8M | 501.18 | 540 | 500 | -$7.4M | +$0 bull / -$1.1M bear | out (clean 29, ADX 32, RVol 0.7) |
| 6 | **SHOP** | 144.10 | - | **-** | 29 | - | NEG -$4.0M | - | 145 | 150 | -$4.0M | - | out (clean 32, ADX 46, RVol 3.3) |
| 7 | **DELL** | 410.77 | - | **-** | 26 | - | NEG -$25.9M | - | 440 | 400 | +$1.9M | +$0 bull / -$54k bear | out (clean 34, ADX 30, RVol 0.3) |
| 8 | **PLTR** | 176.04 | - | **-** | 25 | - | NEG -$24.2M | - | 165 | 180 | -$3.5M | +$0 bull / -$105k bear | out (clean 28, ADX 46, RVol 1.7) |
| 9 | **AVGO** | 334.21 | - | **-** | 24 | - | NEG -$42.2M | 351.42 | 340 | 340 | +$2.4M | +$0 bull / -$76k bear | out (clean 31, ADX 36, RVol 0.5) |
| 10 | **ARM** | 205.00 | - | **-** | 24 | - | NEG -$6.5M | - | 220 | 200 | -$281k | +$0 bull / -$75k bear | out (clean 25, ADX 30, RVol 0.3) |
| 11 | **HOOD** | 85.52 | - | **-** | 22 | - | NEG -$2.5M | - | 90 | 90 | -$583k | +$32k bull / -$27k bear | out (clean 31, ADX 26, RVol 1.2) |
| 12 | **GOOGL** | 279.35 | - | **-** | 21 | - | NEG -$38.9M | 285.21 | 285 | 290 | +$2.4M | +$0 bull / -$69k bear | out (clean 33, ADX 32, RVol 0.5) |
| 13 | **SPY** | 756.24 | - | **-** | 20 | - | NEG -$8.3B | 770.47 | 770 | 750 | -$78.9M | +$0 bull / -$3.1M bear | out (clean 31, ADX 21, RVol 0.7) |
| 14 | **AAPL** | 329.12 | - | **-** | 20 | - | NEG -$429.1M | 343.26 | 350 | 330 | +$2.0M | +$1.7M bull / -$140k bear | out (clean 32, ADX 37, RVol 1.5) |
| 15 | **IWM** | 281.76 | - | **-** | 19 | - | NEG -$912.7M | 287.05 | 285 | 270 | -$2.6M | +$170k bull / -$155k bear | out (clean 33, ADX 26, RVol 0.8) |
| 16 | **SMH** | 522.64 | - | **-** | 19 | - | NEG -$263.5M | - | 532.5 | 500 | +$501k | +$0 bull / -$415k bear | out (clean 33, ADX 31, RVol 0.9) |
| 17 | **NVDA** | 207.83 | - | **-** | 19 | - | POS +$110.8M | 203.67 | 210 | 200 | +$4.7M | +$56k bull / -$681k bear | out (clean 31, ADX 34, RVol 0.7) |
| 18 | **AMD** | 492.56 | - | **-** | 19 | - | NEG -$67.5M | - | 520 | 500 | +$2.7M | +$93k bull / -$928k bear | out (clean 33, ADX 39, RVol 0.6) |
| 19 | **BABA** | 100.58 | - | **-** | 19 | - | POS +$1.6M | 100.06 | 102 | 100 | +$169k | - | out (clean 35, ADX 56, RVol 0.7) |
| 20 | **TSLA** | 401.62 | - | **-** | 18 | - | POS +$239.9M | - | 400 | 400 | +$11.0M | +$566k bull / -$747k bear | out (clean 30, ADX 19, RVol 0.6) |
| 21 | **QQQ** | 688.10 | - | **-** | 17 | - | NEG -$4.9B | - | 700 | 680 | -$25.7M | +$0 bull / -$860k bear | out (clean 32, ADX 25, RVol 0.6) |
| 22 | **AMZN** | 247.41 | - | **-** | 17 | - | POS +$133.9M | 236.3 | 250 | 250 | +$520k | +$165k bull / +$0 bear | out (clean 33, ADX 22, RVol 0.7) |
| 23 | **MU** | 860.93 | - | **-** | 16 | - | NEG -$189.0M | - | 900 | 850 | -$3.5M | +$1.9M bull / -$755k bear | out (clean 32, ADX 28, RVol 0.5) |
| 24 | **CRM** | 221.98 | - | **-** | 16 | - | NEG -$14.4M | - | 240 | 220 | -$332k | - | out (clean 29, ADX 36, RVol 0.6) |
| 25 | **UBER** | 66.84 | - | **-** | 12 | - | NEG -$8.8M | - | 70 | 65 | -$65k | - | out (clean 29, ADX 20, RVol 0.7) |
| 26 | **NFLX** | 62.49 | - | **-** | 11 | - | NEG -$12.1M | 64.26 | 63 | 60 | -$237k | - | out (clean 28, ADX 29, RVol 0.8) |
| 27 | **SMCI** | 31.75 | - | **-** | 11 | - | POS +$2.2M | - | 34.5 | 30 | -$319k | - | out (clean 35, ADX 28, RVol 1.0) |

## Big prints this scan (91)
- **SPY** CALL 745 2026-11-05 (2DTE): 955 @ 12.50 = **+$1.2M** MID | vol 7,169 / OI 186
- **SPY** CALL 745 2026-11-05 (2DTE): 749 @ 12.00 = **+$899k** SELL | vol 7,169 / OI 186
- **MU** CALL 860 2026-11-06 (3DTE): 169 @ 26.95 = **+$455k** BUY | vol 1,574 / OI 194
- **QQQ** CALL 680 2026-11-03 (0DTE): 400 @ 7.80 = **+$312k** SELL | vol 3,665 / OI 340
- **SMH** PUT 530 2026-11-04 (1DTE): 200 @ 13.25 = **+$265k** MID | vol 204 / OI 1,319
- **SPY** CALL 745 2026-11-05 (2DTE): 176 @ 12.00 = **+$211k** SELL | vol 7,169 / OI 186
- **QQQ** CALL 680 2026-11-03 (0DTE): 200 @ 7.80 = **+$156k** SELL | vol 3,665 / OI 340
- **AAPL** PUT 337.5 2026-11-06 (3DTE): 164 @ 9.41 = **+$154k** SELL | vol 1,323 / OI 1,206
- **SPY** CALL 756 2026-11-09 (6DTE): 219 @ 7.00 = **+$153k** SELL | vol 888 / OI 0
- **QQQ** CALL 686 2026-11-03 (0DTE): 500 @ 2.81 = **+$140k** SELL | vol 87,120 / OI 1,049
- **SMH** CALL 530 2026-11-06 (3DTE): 156 @ 8.35 = **+$130k** SELL | vol 259 / OI 766
- **IWM** CALL 284 2026-11-04 (1DTE): 1,000 @ 1.15 = **+$115k** BUY | vol 3,551 / OI 552
- **QQQ** PUT 685 2026-11-04 (1DTE): 198 @ 5.75 = **+$114k** BUY | vol 12,017 / OI 3,872
- **AAPL** PUT 335 2026-11-04 (1DTE): 164 @ 6.80 = **+$112k** BUY | vol 6,680 / OI 2,490
- **AAPL** PUT 325 2026-11-06 (3DTE): 400 @ 2.54 = **+$102k** SELL | vol 11,783 / OI 14,287

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 755 2026-11-06 (3DTE): 2,601 traded vs OI 2,449
- **SPY** CALL 756 2026-11-09 (6DTE): 888 traded vs OI 0
- **SPY** CALL 774 2026-11-03 (0DTE): 1,656 traded vs OI 1,604
- **SPY** CALL 764 2026-11-05 (2DTE): 527 traded vs OI 0
- **SPY** CALL 753 2026-11-06 (3DTE): 799 traded vs OI 786
- **SPY** PUT 724 2026-11-03 (0DTE): 786 traded vs OI 0
- **SPY** PUT 754 2026-11-09 (6DTE): 565 traded vs OI 0
- **SPY** CALL 756 2026-11-30 (27DTE): 600 traded vs OI 570
- **QQQ** PUT 674 2026-11-04 (1DTE): 560 traded vs OI 390
- **QQQ** CALL 749 2026-11-04 (1DTE): 500 traded vs OI 186
- **QQQ** PUT 690 2026-11-03 (0DTE): 3,509 traded vs OI 3,245
- **QQQ** CALL 725 2026-11-30 (27DTE): 985 traded vs OI 940
- **QQQ** CALL 745 2026-11-30 (27DTE): 1,807 traded vs OI 1,534
- **TSLA** PUT 400 2026-11-27 (24DTE): 534 traded vs OI 459
- **AAPL** PUT 317.5 2026-11-13 (10DTE): 676 traded vs OI 217

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
