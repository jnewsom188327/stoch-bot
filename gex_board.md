# GEX + FLOW SCAN - Mon Nov 02, 10:40 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:40:08 ET, last candle SPY 10:39, QQQ 10:39 | no errors

## Flow surges NOT fired - price disagreed (5 today, last 5)
- 10:35 SPY PUTS: price +0.32 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:25 SPY PUTS: price +2.69 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:10 BABA PUTS: over EMA 20 - flow says one way, price says the other
- 10:05 BABA PUTS: over EMA 20 - flow says one way, price says the other
- 09:50 BABA PUTS: price +0.75 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **BABA** | 103.52 | TREND (flow not with it) | **CALLS** | 54 | 11/06 108C @ 0.77 (delta 0.23) = est +40% at 105 | POS +$2.7M | 101.17 | 105 | 100 | -$1.3M | - | LONG (clean 33, ADX 60, RVol 2.3) |
| 2 | **TSLA** | 409.85 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 47 | none: 132 puts 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (64 contracts' greeks worked out here) | POS +$294.1M | - | 410 | 400 | -$77.8M | +$0 bull / -$7.3M bear | out (clean 29, ADX 33, RVol 1.3) |
| 3 | **AMZN** | 252.86 | FLOW SURGE | **PUTS** | 41 | none: 80 puts 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (39 contracts' greeks worked out here) | POS +$125.5M | 241.61 | 265 | 250 | -$26.6M | +$0 bull / -$855k bear | out (clean 32, ADX 64, RVol 1.2) |
| 4 | **SPY** | 762.55 | - | **-** | 29 | - | NEG -$8.3B | 774.26 | 800 | 750 | -$113.8M | +$2.0M bull / -$4.0M bear | out (clean 30, ADX 48, RVol 1.1) |
| 5 | **AVGO** | 332.44 | - | **-** | 29 | - | NEG -$94.6M | - | 340 | 330 | -$6.7M | +$0 bull / -$272k bear | out (clean 32, ADX 54, RVol 0.7) |
| 6 | **MSTR** | 135.51 | - | **-** | 28 | - | POS +$3.8M | - | 135 | 125 | +$2.5M | +$230k bull / -$452k bear | out (clean 27, ADX 42, RVol 1.7) |
| 7 | **QQQ** | 697.54 | - | **-** | 25 | - | NEG -$5.6B | 731.1 | 720 | 700 | -$56.0M | +$229k bull / -$1.6M bear | out (clean 30, ADX 42, RVol 1.4) |
| 8 | **SMH** | 529.50 | - | **-** | 25 | - | NEG -$297.3M | - | 532.5 | 500 | +$1.5M | +$0 bull / -$88k bear | out (clean 32, ADX 45, RVol 0.8) |
| 9 | **MSFT** | 527.41 | - | **-** | 25 | - | POS +$408.8M | 501.38 | 530 | 530 | -$5.2M | +$31k bull / -$544k bear | out (clean 26, ADX 27, RVol 1.0) |
| 10 | **MU** | 880.37 | - | **-** | 25 | - | NEG -$210.7M | - | 910 | 900 | +$28.4M | +$2.1M bull / -$2.3M bear | out (clean 30, ADX 29, RVol 1.6) |
| 11 | **NFLX** | 62.01 | - | **-** | 24 | - | NEG -$23.9M | - | 63 | 60 | +$445k | +$36k bull / +$0 bear | out (clean 30, ADX 23, RVol 1.3) |
| 12 | **HOOD** | 86.86 | - | **-** | 24 | - | NEG -$8.8M | - | 93 | 90 | -$839k | +$29k bull / +$0 bear | out (clean 32, ADX 58, RVol 0.5) |
| 13 | **UBER** | 67.39 | - | **-** | 24 | - | NEG -$8.1M | - | 70 | 65 | -$401k | - | out (clean 28, ADX 53, RVol 1.0) |
| 14 | **PLTR** | 185.92 | - | **-** | 23 | - | NEG -$11.2M | - | 200 | 180 | -$2.1M | +$0 bull / -$213k bear | out (clean 26, ADX 16, RVol 2.1) |
| 15 | **ORCL** | 123.56 | - | **-** | 23 | - | NEG -$39.1M | - | 130 | 120 | -$1.7M | +$59k bull / -$189k bear | out (clean 33, ADX 37, RVol 1.0) |
| 16 | **AMD** | 503.38 | - | **-** | 22 | - | NEG -$95.2M | - | 550 | 500 | +$4.4M | +$304k bull / -$738k bear | out (clean 30, ADX 34, RVol 1.6) |
| 17 | **NVDA** | 208.64 | - | **-** | 21 | - | NEG -$174.2M | 215.2 | 210 | 210 | -$2.3M | +$1.0M bull / -$1.1M bear | out (clean 30, ADX 38, RVol 1.4) |
| 18 | **AAPL** | 340.93 | - | **-** | 21 | - | POS +$78.7M | 336.08 | 350 | 330 | +$4.6M | +$2.2M bull / -$612k bear | out (clean 32, ADX 27, RVol 1.1) |
| 19 | **COIN** | 141.84 | - | **-** | 21 | - | NEG -$8.8M | - | 150 | 150 | -$64k | +$0 bull / -$30k bear | out (clean 26, ADX 31, RVol 2.1) |
| 20 | **GOOGL** | 285.65 | - | **-** | 20 | - | NEG -$73.4M | - | 285 | 290 | -$323k | +$124k bull / +$0 bear | out (clean 34, ADX 51, RVol 0.8) |
| 21 | **META** | 618.17 | - | **-** | 18 | - | NEG -$95.7M | 627.57 | 650 | 610 | -$2.1M | +$1.4M bull / -$77k bear | out (clean 29, ADX 32, RVol 0.5) |
| 22 | **CRM** | 231.34 | - | **-** | 17 | - | NEG -$6.1M | 242.8 | 240 | 220 | +$126k | - | out (clean 28, ADX 19, RVol 1.2) |
| 23 | **DELL** | 418.33 | - | **-** | 16 | - | NEG -$24.1M | - | 440 | 400 | -$309k | +$0 bull / -$126k bear | out (clean 34, ADX 18, RVol 0.9) |
| 24 | **SHOP** | 158.80 | - | **-** | 14 | - | NEG -$203k | - | 170 | 160 | -$61k | - | out (clean 28, ADX 34, RVol 1.5) |
| 25 | **SMCI** | 33.12 | - | **-** | 13 | - | POS +$519k | - | 35 | 33 | -$70k | - | out (clean 32, ADX 48, RVol 1.3) |
| 26 | **ARM** | 204.71 | - | **-** | 12 | - | NEG -$7.1M | - | 220 | 200 | +$189k | - | out (clean 26, ADX 23, RVol 0.7) |
| 27 | **IWM** | 282.73 | - | **-** | 11 | - | NEG -$727.7M | 286.35 | 285 | 270 | -$1.3M | - | out (clean 31, ADX 48, RVol 0.9) |

## Big prints this scan (143)
- **SPY** PUT 755 2026-11-09 (7DTE): 1,261 @ 3.35 = **+$422k** SELL | vol 2,775 / OI 964
- **QQQ** PUT 707 2026-11-06 (4DTE): 280 @ 14.00 = **+$392k** BUY | vol 296 / OI 393
- **TSLA** CALL 420 2026-11-06 (4DTE): 726 @ 5.05 = **+$367k** SELL | vol 9,488 / OI 5,521
- **SPY** CALL 767 2026-11-04 (2DTE): 952 @ 2.49 = **+$237k** BUY | vol 2,298 / OI 402
- **SPY** CALL 764 2026-11-03 (1DTE): 952 @ 2.47 = **+$235k** BUY | vol 14,839 / OI 144
- **TSLA** CALL 420 2026-11-04 (2DTE): 680 @ 3.20 = **+$218k** SELL | vol 5,089 / OI 1,302
- **MU** CALL 885 2026-11-09 (7DTE): 73 @ 28.85 = **+$211k** BUY | vol 273 / OI 4
- **NVDA** CALL 207.5 2026-11-02 (0DTE): 1,000 @ 2.05 = **+$205k** BUY | vol 46,267 / OI 510
- **SPY** CALL 753 2026-11-02 (0DTE): 200 @ 10.23 = **+$205k** BUY | vol 1,607 / OI 31
- **AAPL** CALL 342.5 2026-11-04 (2DTE): 312 @ 6.30 = **+$197k** SELL | vol 2,417 / OI 130
- **SPY** CALL 754 2026-11-02 (0DTE): 200 @ 9.26 = **+$185k** BUY | vol 2,725 / OI 20
- **SPY** CALL 760 2026-11-06 (4DTE): 200 @ 8.05 = **+$161k** BUY | vol 6,514 / OI 1,345
- **AAPL** CALL 342.5 2026-11-04 (2DTE): 237 @ 6.60 = **+$156k** BUY | vol 2,417 / OI 130
- **QQQ** PUT 697 2026-11-02 (0DTE): 700 @ 2.09 = **+$146k** BUY | vol 11,510 / OI 0
- **AAPL** CALL 342.5 2026-11-04 (2DTE): 213 @ 6.60 = **+$141k** BUY | vol 2,417 / OI 130

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 775 2026-11-05 (3DTE): 2,123 traded vs OI 1,948
- **SPY** CALL 770 2026-11-06 (4DTE): 4,234 traded vs OI 4,063
- **SPY** CALL 768 2026-11-04 (2DTE): 519 traded vs OI 396
- **SPY** CALL 763 2026-11-06 (4DTE): 1,179 traded vs OI 907
- **SPY** PUT 763 2026-11-03 (1DTE): 967 traded vs OI 649
- **SPY** CALL 764 2026-11-04 (2DTE): 857 traded vs OI 132
- **SPY** PUT 759 2026-11-06 (4DTE): 1,036 traded vs OI 1,010
- **SPY** CALL 772 2026-11-03 (1DTE): 1,367 traded vs OI 1,021
- **SPY** CALL 774 2026-11-04 (2DTE): 728 traded vs OI 404
- **SPY** PUT 767 2026-11-02 (0DTE): 1,257 traded vs OI 994
- **SPY** PUT 758 2026-11-06 (4DTE): 1,626 traded vs OI 1,449
- **SPY** CALL 757 2026-11-06 (4DTE): 516 traded vs OI 96
- **SPY** CALL 776 2026-11-02 (0DTE): 1,900 traded vs OI 1,447
- **SPY** CALL 783 2026-11-04 (2DTE): 802 traded vs OI 403
- **SPY** PUT 755 2026-11-03 (1DTE): 3,439 traded vs OI 3,155

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
