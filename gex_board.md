# GEX + FLOW SCAN - Mon Nov 02, 10:50 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:50:08 ET, last candle SPY 10:49, QQQ 10:49 | no errors

## Flow surges NOT fired - price disagreed (5 today, last 5)
- 10:35 SPY PUTS: price +0.32 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:25 SPY PUTS: price +2.69 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:10 BABA PUTS: over EMA 20 - flow says one way, price says the other
- 10:05 BABA PUTS: over EMA 20 - flow says one way, price says the other
- 09:50 BABA PUTS: price +0.75 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **AMZN** | 253.24 | FLOW SURGE | **PUTS** | 40 | none: 80 puts 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (38 contracts' greeks worked out here) | POS +$127.6M | 242 | 265 | 250 | -$29.0M | +$0 bull / -$725k bear | out (clean 33, ADX 67, RVol 1.1) |
| 2 | **MSFT** | 529.51 | PINNED between the walls (positive gamma) - chop | **-** | 40 | - | POS +$445.5M | 499.38 | 530 | 530 | -$5.5M | +$31k bull / -$743k bear | out (clean 26, ADX 28, RVol 1.0) |
| 3 | **BABA** | 103.62 | - | **-** | 35 | - | POS +$3.1M | 101.03 | 105 | 100 | -$1.2M | +$34k bull / +$0 bear | out (clean 33, ADX 61, RVol 1.7) |
| 4 | **SPY** | 762.42 | - | **-** | 28 | - | NEG -$8.5B | 775.44 | 800 | 750 | -$111.4M | +$3.7M bull / -$2.0M bear | out (clean 30, ADX 48, RVol 1.1) |
| 5 | **TSLA** | 413.85 | - | **-** | 28 | - | POS +$312.1M | - | 410 | 400 | -$108.1M | +$0 bull / -$9.3M bear | out (clean 29, ADX 36, RVol 1.6) |
| 6 | **AVGO** | 331.38 | - | **-** | 27 | - | NEG -$97.7M | - | 340 | 330 | -$5.7M | +$126k bull / -$176k bear | out (clean 32, ADX 56, RVol 0.7) |
| 7 | **SMH** | 527.28 | - | **-** | 26 | - | NEG -$309.2M | - | 532.5 | 500 | +$1.9M | +$0 bull / -$34k bear | out (clean 32, ADX 44, RVol 0.7) |
| 8 | **MSTR** | 135.60 | - | **-** | 26 | - | POS +$3.5M | - | 135 | 125 | +$2.0M | +$0 bull / -$206k bear | out (clean 27, ADX 43, RVol 1.4) |
| 9 | **MU** | 877.52 | - | **-** | 25 | - | NEG -$202.2M | - | 910 | 850 | +$34.8M | +$5.5M bull / -$571k bear | out (clean 30, ADX 27, RVol 1.6) |
| 10 | **AMD** | 497.95 | - | **-** | 23 | - | NEG -$92.7M | - | 540 | 500 | +$6.6M | +$616k bull / +$0 bear | out (clean 30, ADX 31, RVol 1.8) |
| 11 | **UBER** | 67.26 | - | **-** | 23 | - | NEG -$8.3M | - | 70 | 65 | -$393k | - | out (clean 28, ADX 55, RVol 0.9) |
| 12 | **QQQ** | 696.70 | - | **-** | 22 | - | NEG -$5.6B | 730.96 | 720 | 700 | -$39.2M | +$1.4M bull / -$1.2M bear | out (clean 30, ADX 42, RVol 1.0) |
| 13 | **COIN** | 141.54 | - | **-** | 22 | - | NEG -$9.0M | - | 150 | 130 | -$192k | +$0 bull / -$30k bear | out (clean 26, ADX 31, RVol 1.3) |
| 14 | **ORCL** | 123.55 | - | **-** | 22 | - | NEG -$39.2M | - | 130 | 120 | -$1.3M | +$249k bull / +$0 bear | out (clean 33, ADX 36, RVol 1.0) |
| 15 | **NVDA** | 207.49 | - | **-** | 21 | - | NEG -$196.1M | 215.37 | 210 | 200 | +$3.6M | +$2.2M bull / -$385k bear | out (clean 30, ADX 36, RVol 1.5) |
| 16 | **GOOGL** | 285.11 | - | **-** | 20 | - | NEG -$78.0M | - | 285 | 290 | +$2k | +$93k bull / +$0 bear | out (clean 34, ADX 50, RVol 0.8) |
| 17 | **PLTR** | 185.41 | - | **-** | 20 | - | NEG -$11.2M | - | 200 | 180 | -$1.9M | +$0 bull / -$115k bear | out (clean 26, ADX 15, RVol 1.3) |
| 18 | **AAPL** | 341.94 | - | **-** | 19 | - | POS +$90.8M | 336.12 | 350 | 330 | +$3.2M | +$1.8M bull / -$922k bear | out (clean 32, ADX 24, RVol 1.1) |
| 19 | **META** | 617.32 | - | **-** | 18 | - | NEG -$99.2M | 627.02 | 650 | 610 | -$1.9M | +$1.4M bull / -$409k bear | out (clean 29, ADX 31, RVol 0.5) |
| 20 | **DELL** | 415.13 | - | **-** | 16 | - | NEG -$23.7M | - | 440 | 400 | -$302k | +$37k bull / -$90k bear | out (clean 34, ADX 17, RVol 0.8) |
| 21 | **CRM** | 231.52 | - | **-** | 16 | - | NEG -$5.3M | 241.75 | 240 | 220 | +$128k | - | out (clean 28, ADX 17, RVol 0.8) |
| 22 | **HOOD** | 86.62 | - | **-** | 15 | - | NEG -$9.2M | - | 93 | 90 | -$982k | - | out (clean 32, ADX 58, RVol 0.4) |
| 23 | **SHOP** | 159.07 | - | **-** | 15 | - | NEG -$164k | - | 170 | 160 | -$62k | - | out (clean 28, ADX 32, RVol 2.1) |
| 24 | **ARM** | 203.18 | - | **-** | 13 | - | NEG -$6.9M | - | 220 | 200 | +$233k | - | out (clean 26, ADX 22, RVol 0.8) |
| 25 | **IWM** | 282.83 | - | **-** | 12 | - | NEG -$710.9M | 286.33 | 285 | 270 | -$2.7M | - | out (clean 31, ADX 49, RVol 0.8) |
| 26 | **SMCI** | 32.62 | - | **-** | 11 | - | POS +$51k | 31.75 | 35 | 33 | -$27k | - | out (clean 33, ADX 43, RVol 1.3) |
| 27 | **NFLX** | 61.90 | - | **-** | 10 | - | NEG -$24.4M | - | 63 | 60 | +$281k | - | out (clean 30, ADX 21, RVol 1.0) |

## Big prints this scan (124)
- **TSLA** CALL 405 2026-11-02 (0DTE): 412 @ 6.15 = **+$253k** SELL | vol 67,254 / OI 1,899
- **TSLA** CALL 420 2026-11-06 (4DTE): 418 @ 5.40 = **+$226k** SELL | vol 10,955 / OI 5,521
- **MU** CALL 890 2026-11-06 (4DTE): 100 @ 21.73 = **+$217k** BUY | vol 580 / OI 224
- **TSLA** CALL 400 2026-11-04 (2DTE): 160 @ 13.55 = **+$217k** SELL | vol 4,647 / OI 612
- **NVDA** CALL 210 2026-11-06 (4DTE): 600 @ 3.60 = **+$216k** BUY | vol 9,381 / OI 997
- **SPY** PUT 762 2026-11-06 (4DTE): 380 @ 5.04 = **+$192k** SELL | vol 4,928 / OI 7,408
- **TSLA** CALL 405 2026-11-02 (0DTE): 315 @ 5.60 = **+$176k** SELL | vol 67,254 / OI 1,899
- **SPY** PUT 760 2026-11-03 (1DTE): 931 @ 1.77 = **+$165k** SELL | vol 19,951 / OI 1,594
- **SPY** PUT 760 2026-11-05 (3DTE): 431 @ 3.70 = **+$159k** SELL | vol 3,854 / OI 2,641
- **TSLA** CALL 400 2026-11-04 (2DTE): 117 @ 13.55 = **+$159k** SELL | vol 4,647 / OI 612
- **TSLA** CALL 400 2026-11-04 (2DTE): 117 @ 13.55 = **+$159k** SELL | vol 4,647 / OI 612
- **MU** PUT 880 2026-11-02 (0DTE): 300 @ 5.20 = **+$156k** SELL | vol 6,436 / OI 325
- **SPY** PUT 763 2026-11-03 (1DTE): 503 @ 2.82 = **+$142k** SELL | vol 5,595 / OI 649
- **SPY** PUT 763 2026-11-03 (1DTE): 500 @ 2.79 = **+$140k** SELL | vol 5,595 / OI 649
- **MU** CALL 885 2026-11-09 (7DTE): 50 @ 27.60 = **+$138k** BUY | vol 400 / OI 4

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 763 2026-11-04 (2DTE): 599 traded vs OI 298
- **SPY** CALL 792 2026-11-06 (4DTE): 2,086 traded vs OI 480
- **SPY** PUT 715 2026-11-09 (7DTE): 530 traded vs OI 303
- **SPY** PUT 729 2026-11-04 (2DTE): 507 traded vs OI 246
- **SPY** PUT 764 2026-11-03 (1DTE): 1,420 traded vs OI 1,342
- **SPY** PUT 732 2026-11-02 (0DTE): 1,069 traded vs OI 1,064
- **SPY** PUT 727 2026-11-04 (2DTE): 685 traded vs OI 78
- **SPY** CALL 768 2026-11-06 (4DTE): 1,261 traded vs OI 1,258
- **QQQ** PUT 673 2026-11-04 (2DTE): 658 traded vs OI 0
- **QQQ** CALL 726 2026-11-06 (4DTE): 731 traded vs OI 726
- **QQQ** PUT 690 2026-11-09 (7DTE): 742 traded vs OI 741
- **QQQ** PUT 685 2026-11-04 (2DTE): 942 traded vs OI 935
- **QQQ** PUT 665 2026-11-02 (0DTE): 4,873 traded vs OI 4,013
- **QQQ** CALL 710 2026-11-09 (7DTE): 504 traded vs OI 390
- **QQQ** PUT 674 2026-11-02 (0DTE): 682 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
