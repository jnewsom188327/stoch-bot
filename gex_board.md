# GEX + FLOW SCAN - Mon Nov 02, 11:20 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 11:20:08 ET, last candle SPY 11:19, QQQ 11:19 | no errors

## Flow surges NOT fired - price disagreed (5 today, last 5)
- 10:35 SPY PUTS: price +0.32 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:25 SPY PUTS: price +2.69 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:10 BABA PUTS: over EMA 20 - flow says one way, price says the other
- 10:05 BABA PUTS: over EMA 20 - flow says one way, price says the other
- 09:50 BABA PUTS: price +0.75 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **SMCI** | 32.35 | FLIP CROSS up into positive gamma | **CALLS** | 37 | none: 13 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$11k | 32.15 | 35 | 33 | +$113k | +$26k bull / +$0 bear | out (clean 33, ADX 33, RVol 1.2) |
| 2 | **AMZN** | 251.61 | - | **-** | 28 | - | POS +$118.1M | 241.5 | 250 | 250 | -$25.8M | +$1.1M bull / -$1.2M bear | out (clean 33, ADX 67, RVol 0.8) |
| 3 | **MU** | 869.88 | - | **-** | 27 | - | NEG -$222.5M | - | 910 | 850 | +$60.5M | +$5.0M bull / +$0 bear | out (clean 30, ADX 21, RVol 1.8) |
| 4 | **SMH** | 525.92 | - | **-** | 26 | - | NEG -$332.8M | - | 532.5 | 500 | +$2.7M | +$118k bull / +$0 bear | out (clean 31, ADX 34, RVol 0.8) |
| 5 | **AMD** | 492.82 | - | **-** | 26 | - | NEG -$91.0M | - | 540 | 500 | +$21.0M | +$2.7M bull / -$30k bear | out (clean 30, ADX 31, RVol 1.4) |
| 6 | **TSLA** | 412.50 | - | **-** | 25 | - | POS +$303.8M | - | 410 | 400 | -$84.5M | +$6.5M bull / -$59k bear | out (clean 30, ADX 41, RVol 1.2) |
| 7 | **MSTR** | 134.66 | - | **-** | 25 | - | POS +$3.6M | - | 135 | 125 | +$2.9M | +$46k bull / +$0 bear | out (clean 27, ADX 38, RVol 1.0) |
| 8 | **BABA** | 103.33 | - | **-** | 24 | - | POS +$2.6M | 101.27 | 105 | 100 | -$1.2M | - | out (clean 33, ADX 59, RVol 1.5) |
| 9 | **SHOP** | 158.65 | - | **-** | 22 | - | NEG -$445k | - | 170 | 160 | -$427k | - | out (clean 28, ADX 26, RVol 2.0) |
| 10 | **AAPL** | 340.76 | - | **-** | 21 | - | POS +$57.6M | 336.68 | 350 | 330 | +$8.8M | +$3.1M bull / +$0 bear | out (clean 31, ADX 18, RVol 1.0) |
| 11 | **SPY** | 760.55 | - | **-** | 20 | - | NEG -$9.5B | 775.17 | 770 | 750 | -$46.7M | +$4.4M bull / +$0 bear | out (clean 29, ADX 37, RVol 0.5) |
| 12 | **META** | 610.27 | - | **-** | 20 | - | NEG -$139.0M | 625.47 | 650 | 600 | +$7.8M | +$1.4M bull / +$0 bear | out (clean 29, ADX 28, RVol 0.7) |
| 13 | **MSFT** | 524.29 | - | **-** | 20 | - | POS +$333.7M | 500.78 | 540 | 530 | -$3.4M | +$591k bull / +$0 bear | out (clean 26, ADX 23, RVol 1.2) |
| 14 | **GOOGL** | 283.00 | - | **-** | 19 | - | NEG -$88.4M | - | 285 | 290 | +$1.6M | +$86k bull / +$0 bear | out (clean 34, ADX 35, RVol 0.7) |
| 15 | **IWM** | 282.24 | - | **-** | 18 | - | NEG -$843.8M | 286.43 | 285 | 270 | +$576k | +$320k bull / -$128k bear | out (clean 31, ADX 41, RVol 0.4) |
| 16 | **NVDA** | 207.73 | - | **-** | 18 | - | NEG -$197.5M | 215.01 | 210 | 210 | +$4.6M | +$579k bull / -$999k bear | out (clean 29, ADX 26, RVol 1.0) |
| 17 | **ORCL** | 123.15 | - | **-** | 18 | - | NEG -$39.7M | - | 130 | 120 | -$421k | +$140k bull / -$207k bear | out (clean 32, ADX 35, RVol 0.5) |
| 18 | **COIN** | 139.34 | - | **-** | 17 | - | NEG -$8.0M | - | 150 | 130 | -$79k | +$27k bull / +$0 bear | out (clean 25, ADX 22, RVol 0.8) |
| 19 | **QQQ** | 694.82 | - | **-** | 16 | - | NEG -$5.7B | 731.58 | 720 | 680 | +$173k | +$2.2M bull / +$0 bear | out (clean 30, ADX 30, RVol 0.5) |
| 20 | **AVGO** | 332.70 | - | **-** | 16 | - | NEG -$96.7M | - | 340 | 330 | -$6.0M | - | out (clean 31, ADX 52, RVol 0.6) |
| 21 | **PLTR** | 184.93 | - | **-** | 15 | - | NEG -$11.5M | - | 200 | 180 | -$683k | +$378k bull / -$44k bear | out (clean 25, ADX 12, RVol 0.7) |
| 22 | **UBER** | 67.17 | - | **-** | 15 | - | NEG -$8.7M | - | 70 | 65 | -$242k | - | out (clean 28, ADX 48, RVol 0.7) |
| 23 | **CRM** | 231.20 | - | **-** | 13 | - | NEG -$5.7M | 242.04 | 240 | 220 | +$105k | - | out (clean 28, ADX 16, RVol 1.0) |
| 24 | **HOOD** | 85.89 | - | **-** | 12 | - | NEG -$9.4M | - | 93 | 90 | -$533k | - | out (clean 32, ADX 45, RVol 0.5) |
| 25 | **ARM** | 205.44 | - | **-** | 11 | - | NEG -$7.1M | - | 220 | 200 | +$197k | - | out (clean 26, ADX 21, RVol 0.7) |
| 26 | **NFLX** | 61.92 | - | **-** | 9 | - | NEG -$24.8M | - | 63 | 60 | +$349k | - | out (clean 30, ADX 16, RVol 1.0) |
| 27 | **DELL** | 416.11 | - | **-** | 5 | - | NEG -$23.8M | - | 440 | 400 | +$59k | - | out (clean 34, ADX 16, RVol 0.8) |

## Big prints this scan (111)
- **TSLA** CALL 392.5 2026-11-09 (7DTE): 200 @ 24.63 = **+$493k** BUY | vol 202 / OI 0
- **TSLA** CALL 397.5 2026-11-06 (4DTE): 200 @ 19.98 = **+$400k** BUY | vol 785 / OI 1,118
- **SPY** PUT 765 2026-11-05 (3DTE): 500 @ 7.00 = **+$350k** SELL | vol 4,401 / OI 2,269
- **SPY** PUT 763 2026-11-03 (1DTE): 600 @ 3.69 = **+$221k** SELL | vol 11,428 / OI 649
- **AAPL** PUT 337.5 2026-11-06 (4DTE): 338 @ 6.25 = **+$211k** SELL | vol 4,822 / OI 600
- **AAPL** PUT 337.5 2026-11-06 (4DTE): 294 @ 6.25 = **+$184k** SELL | vol 4,822 / OI 600
- **SPY** PUT 770 2026-11-04 (2DTE): 180 @ 9.62 = **+$173k** SELL | vol 270 / OI 1,423
- **SPY** PUT 764 2026-11-02 (0DTE): 500 @ 3.26 = **+$163k** SELL | vol 33,822 / OI 1,448
- **SPY** PUT 763 2026-11-02 (0DTE): 600 @ 2.61 = **+$157k** SELL | vol 61,040 / OI 1,678
- **IWM** PUT 290 2026-11-06 (4DTE): 197 @ 7.65 = **+$151k** SELL | vol 414 / OI 47
- **AMZN** PUT 250 2026-11-06 (4DTE): 428 @ 3.10 = **+$133k** SELL | vol 4,443 / OI 3,922
- **SPY** PUT 763 2026-11-02 (0DTE): 500 @ 2.61 = **+$130k** SELL | vol 61,040 / OI 1,678
- **MU** CALL 885 2026-11-09 (7DTE): 50 @ 25.20 = **+$126k** BUY | vol 510 / OI 4
- **ORCL** PUT 125 2026-11-06 (4DTE): 271 @ 4.58 = **+$124k** BUY | vol 2,571 / OI 4,197
- **MU** CALL 900 2026-11-06 (4DTE): 77 @ 15.85 = **+$122k** BUY | vol 1,646 / OI 373

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 777 2026-11-03 (1DTE): 588 traded vs OI 525
- **QQQ** PUT 678 2026-11-03 (1DTE): 503 traded vs OI 0
- **QQQ** CALL 716 2026-11-03 (1DTE): 504 traded vs OI 308
- **IWM** CALL 284 2026-11-04 (2DTE): 528 traded vs OI 122
- **SMH** PUT 480 2026-11-13 (11DTE): 873 traded vs OI 164
- **TSLA** CALL 405 2026-11-09 (7DTE): 655 traded vs OI 238
- **TSLA** PUT 412.5 2026-11-06 (4DTE): 503 traded vs OI 66
- **AAPL** PUT 327.5 2026-11-04 (2DTE): 543 traded vs OI 233
- **AAPL** CALL 370 2026-11-04 (2DTE): 2,715 traded vs OI 2,567
- **AAPL** CALL 357.5 2026-11-06 (4DTE): 733 traded vs OI 717
- **AMD** PUT 450 2026-11-27 (25DTE): 548 traded vs OI 0
- **AMD** PUT 480 2026-11-04 (2DTE): 512 traded vs OI 273
- **META** CALL 635 2026-11-04 (2DTE): 506 traded vs OI 217
- **META** CALL 615 2026-11-04 (2DTE): 540 traded vs OI 89
- **META** PUT 590 2026-11-04 (2DTE): 600 traded vs OI 103

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
