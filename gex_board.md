# GEX + FLOW SCAN - Mon Nov 02, 11:30 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 11:30:08 ET, last candle SPY 11:29, QQQ 11:29 | no errors

## Flow surges NOT fired - price disagreed (5 today, last 5)
- 10:35 SPY PUTS: price +0.32 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:25 SPY PUTS: price +2.69 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:10 BABA PUTS: over EMA 20 - flow says one way, price says the other
- 10:05 BABA PUTS: over EMA 20 - flow says one way, price says the other
- 09:50 BABA PUTS: price +0.75 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **MSTR** | 134.89 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 45 | none: 27 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$3.4M | - | 135 | 125 | +$2.6M | +$46k bull / +$0 bear | out (clean 27, ADX 36, RVol 1.2) |
| 2 | **TSLA** | 410.87 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 43 | none: 132 puts 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (57 contracts' greeks worked out here) | POS +$311.7M | - | 410 | 400 | -$79.0M | +$6.4M bull / +$0 bear | out (clean 30, ADX 40, RVol 0.9) |
| 3 | **MU** | 864.25 | - | **-** | 28 | - | NEG -$210.8M | - | 910 | 850 | +$68.8M | +$4.5M bull / +$0 bear | out (clean 30, ADX 22, RVol 2.5) |
| 4 | **AMZN** | 251.52 | - | **-** | 27 | - | POS +$109.4M | 241.98 | 250 | 250 | -$23.9M | +$416k bull / +$0 bear | out (clean 33, ADX 63, RVol 0.8) |
| 5 | **SMCI** | 32.26 | TREND (flow not with it) | **PUTS** | 27 | none: 12 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$86k | - | 35 | 30 | +$144k | - | SHORT (clean 33, ADX 32, RVol 1.0) |
| 6 | **AMD** | 489.46 | - | **-** | 26 | - | NEG -$82.8M | - | 500 | 500 | +$24.9M | +$1.1M bull / +$0 bear | out (clean 30, ADX 34, RVol 1.2) |
| 7 | **SMH** | 522.99 | - | **-** | 25 | - | NEG -$338.4M | - | 532.5 | 500 | +$2.9M | +$2.0M bull / +$0 bear | out (clean 31, ADX 30, RVol 0.7) |
| 8 | **BABA** | 103.28 | - | **-** | 24 | - | POS +$2.9M | 100.94 | 105 | 100 | -$1.2M | - | out (clean 33, ADX 56, RVol 1.4) |
| 9 | **SHOP** | 158.25 | - | **-** | 21 | - | NEG -$445k | - | 170 | 160 | -$425k | - | out (clean 28, ADX 23, RVol 1.6) |
| 10 | **META** | 611.93 | - | **-** | 20 | - | NEG -$125.7M | 624.99 | 650 | 610 | +$8.4M | +$918k bull / -$83k bear | out (clean 29, ADX 28, RVol 0.7) |
| 11 | **AAPL** | 341.24 | - | **-** | 19 | - | POS +$75.8M | 336.32 | 350 | 330 | +$7.3M | +$888k bull / -$245k bear | out (clean 31, ADX 16, RVol 0.9) |
| 12 | **GOOGL** | 283.22 | - | **-** | 19 | - | NEG -$88.5M | - | 285 | 290 | +$1.7M | +$57k bull / +$0 bear | out (clean 34, ADX 30, RVol 0.7) |
| 13 | **SPY** | 760.02 | - | **-** | 18 | - | NEG -$9.3B | 774.35 | 770 | 750 | -$29.5M | +$1.8M bull / +$0 bear | out (clean 29, ADX 32, RVol 0.5) |
| 14 | **IWM** | 282.12 | - | **-** | 18 | - | NEG -$824.9M | 286.33 | 285 | 270 | +$598k | +$1.1M bull / +$0 bear | out (clean 31, ADX 37, RVol 0.4) |
| 15 | **NVDA** | 206.88 | - | **-** | 18 | - | NEG -$202.8M | 214.62 | 210 | 200 | +$5.4M | +$829k bull / -$66k bear | out (clean 29, ADX 23, RVol 1.2) |
| 16 | **ORCL** | 123.26 | - | **-** | 18 | - | NEG -$39.6M | - | 130 | 120 | -$460k | +$89k bull / -$207k bear | out (clean 32, ADX 34, RVol 0.7) |
| 17 | **QQQ** | 693.68 | - | **-** | 17 | - | NEG -$5.4B | 731.37 | 720 | 680 | +$14.8M | +$961k bull / +$0 bear | out (clean 30, ADX 27, RVol 0.6) |
| 18 | **AVGO** | 330.25 | - | **-** | 15 | - | NEG -$102.7M | - | 340 | 330 | -$5.6M | - | out (clean 31, ADX 47, RVol 0.5) |
| 19 | **PLTR** | 184.67 | - | **-** | 15 | - | NEG -$11.6M | - | 200 | 180 | -$552k | +$270k bull / +$0 bear | out (clean 25, ADX 11, RVol 0.8) |
| 20 | **UBER** | 67.24 | - | **-** | 15 | - | NEG -$8.3M | - | 70 | 65 | -$225k | - | out (clean 28, ADX 45, RVol 0.7) |
| 21 | **CRM** | 231.22 | - | **-** | 12 | - | NEG -$5.3M | 241.68 | 240 | 220 | +$108k | - | out (clean 28, ADX 15, RVol 0.8) |
| 22 | **MSFT** | 523.16 | - | **-** | 10 | - | POS +$325.8M | 500.81 | 540 | 500 | -$3.2M | - | out (clean 26, ADX 22, RVol 1.2) |
| 23 | **HOOD** | 86.06 | - | **-** | 10 | - | NEG -$9.3M | - | 93 | 90 | -$417k | - | out (clean 32, ADX 40, RVol 0.4) |
| 24 | **ARM** | 205.10 | - | **-** | 10 | - | NEG -$7.1M | - | 220 | 200 | +$187k | - | out (clean 26, ADX 20, RVol 0.6) |
| 25 | **NFLX** | 62.10 | - | **-** | 9 | - | NEG -$23.4M | - | 63 | 60 | +$319k | - | out (clean 29, ADX 16, RVol 1.0) |
| 26 | **COIN** | 138.90 | - | **-** | 7 | - | NEG -$7.9M | - | 150 | 130 | -$64k | - | out (clean 25, ADX 21, RVol 1.1) |
| 27 | **DELL** | 414.99 | - | **-** | 5 | - | NEG -$23.9M | - | 440 | 400 | +$73k | - | out (clean 34, ADX 15, RVol 1.0) |

## Big prints this scan (84)
- **SMH** PUT 500 2026-11-06 (4DTE): 5,400 @ 3.62 = **+$2.0M** SELL | vol 6,427 / OI 35,661
- **QQQ** PUT 695 2026-11-04 (2DTE): 899 @ 6.95 = **+$625k** SELL | vol 3,991 / OI 2,938
- **AMZN** PUT 250 2026-11-06 (4DTE): 428 @ 2.99 = **+$128k** SELL | vol 6,036 / OI 3,922
- **MU** PUT 870 2026-11-02 (0DTE): 200 @ 5.95 = **+$119k** SELL | vol 16,906 / OI 677
- **TSLA** PUT 400 2026-11-06 (4DTE): 250 @ 4.65 = **+$116k** SELL | vol 4,042 / OI 4,312
- **SPY** PUT 760 2026-11-03 (1DTE): 450 @ 2.55 = **+$115k** SELL | vol 29,817 / OI 1,594
- **QQQ** CALL 695 2026-11-03 (1DTE): 250 @ 4.51 = **+$113k** BUY | vol 9,117 / OI 32
- **MU** PUT 895 2026-11-06 (4DTE): 20 @ 42.05 = **+$84k** SELL | vol 191 / OI 327
- **MU** PUT 880 2026-11-02 (0DTE): 65 @ 11.80 = **+$77k** SELL | vol 8,854 / OI 325
- **MU** PUT 850 2026-11-04 (2DTE): 50 @ 12.61 = **+$63k** SELL | vol 1,955 / OI 232
- **MU** PUT 850 2026-11-04 (2DTE): 50 @ 12.60 = **+$63k** SELL | vol 1,955 / OI 232
- **TSLA** CALL 415 2026-11-04 (2DTE): 93 @ 6.65 = **+$62k** BUY | vol 9,517 / OI 907
- **TSLA** CALL 415 2026-11-04 (2DTE): 100 @ 6.15 = **+$62k** BUY | vol 9,517 / OI 907
- **AMD** CALL 485 2026-11-04 (2DTE): 25 @ 24.46 = **+$61k** BUY | vol 127 / OI 26
- **AMD** CALL 485 2026-11-04 (2DTE): 25 @ 24.39 = **+$61k** BUY | vol 127 / OI 26

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 726 2026-11-04 (2DTE): 729 traded vs OI 270
- **SPY** PUT 757 2026-11-04 (2DTE): 836 traded vs OI 833
- **SPY** PUT 765 2026-11-03 (1DTE): 1,246 traded vs OI 1,237
- **SPY** CALL 798 2026-11-03 (1DTE): 1,051 traded vs OI 249
- **SPY** CALL 797 2026-11-03 (1DTE): 807 traded vs OI 439
- **SPY** CALL 765 2026-11-27 (25DTE): 500 traded vs OI 451
- **QQQ** PUT 655 2026-11-03 (1DTE): 852 traded vs OI 789
- **QQQ** CALL 730 2026-11-11 (9DTE): 533 traded vs OI 148
- **QQQ** CALL 688 2026-11-20 (18DTE): 2,047 traded vs OI 113
- **QQQ** CALL 696 2026-11-20 (18DTE): 2,261 traded vs OI 194
- **SMH** PUT 480 2026-11-06 (4DTE): 5,506 traded vs OI 1,741
- **SMH** PUT 500 2026-11-13 (11DTE): 1,992 traded vs OI 1,425
- **NVDA** PUT 207.5 2026-11-13 (11DTE): 603 traded vs OI 589
- **NVDA** PUT 195 2026-11-09 (7DTE): 500 traded vs OI 390
- **TSLA** PUT 410 2026-11-13 (11DTE): 518 traded vs OI 78

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
