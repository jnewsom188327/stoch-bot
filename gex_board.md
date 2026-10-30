# GEX + FLOW SCAN - Fri Oct 30, 11:00 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (2)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:25 | **SMCI** | **PUTS** | FLIP CROSS down into negative gamma | 10/30 32.5P | 0.43 | 0.24 | -12% (1m) | **-44%** | +32% | 32 |
| 10:15 | **AAPL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 10/30 347.5C | 0.50 | 1.71 | +356% (38m) | **+242%** | +104% | 347.56 hit |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 11:00:08 ET, last candle SPY 10:59, QQQ 10:59 | no errors

## Flow surges NOT fired - price disagreed (36 today, last 5)
- 10:55 AAPL PUTS: price +1.23 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:50 AAPL PUTS: price +2.30 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:45 SMCI CALLS: under EMA 20 - flow says one way, price says the other
- 10:45 AAPL PUTS: price +2.47 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:40 SMCI CALLS: under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **MSTR** | 130.83 | FLOW SURGE | **PUTS** | 53 | none: 52 puts 0-7DTE > 2 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only -9% at the target (needs +20%) (46 contracts' greeks worked out here) | NEG -$25.3M | - | 135 | 130 | -$4.6M | +$0 bull / -$3.0M bear | out (clean 27, ADX 39, RVol 2.5) |
| 2 | **META** | 625.12 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 46 | none: 200 calls 0-7DTE > 11 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (78 contracts' greeks worked out here) | POS +$60.6M | 622.59 | 630 | 625 | -$8.8M | +$28k bull / -$1.2M bear | out (clean 28, ADX 21, RVol 1.0) |
| 3 | **AAPL** | 348.50 | FLOW SURGE | **PUTS** | 45 | none: 83 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (39 contracts' greeks worked out here) | POS +$741.4M | 342.42 | 350 | 345 | -$10.8M | +$0 bull / -$780k bear | out (clean 31, ADX 38, RVol 1.8) |
| 4 | **COIN** | 140.64 | - | **-** | 33 | - | NEG -$15.1M | - | 150 | 140 | -$2.9M | +$0 bull / -$2.9M bear | out (clean 27, ADX 56, RVol 2.4) |
| 5 | **AMD** | 514.72 | - | **-** | 27 | - | NEG -$88.3M | 525.23 | 527.5 | 500 | +$7.7M | +$727k bull / -$1.1M bear | out (clean 28, ADX 40, RVol 2.0) |
| 6 | **ARM** | 205.34 | - | **-** | 27 | - | NEG -$19.5M | - | 220 | 205 | +$417k | - | out (clean 26, ADX 47, RVol 3.6) |
| 7 | **SMH** | 528.86 | - | **-** | 26 | - | NEG -$552.0M | - | 530 | 530 | +$3.8M | +$3.5M bull / -$1.4M bear | out (clean 28, ADX 46, RVol 1.3) |
| 8 | **NVDA** | 206.91 | - | **-** | 26 | - | NEG -$411.5M | 211.8 | 210 | 210 | +$5.2M | +$1.0M bull / -$1.1M bear | out (clean 25, ADX 41, RVol 1.7) |
| 9 | **QQQ** | 696.67 | - | **-** | 25 | - | NEG -$9.7B | 727.84 | 720 | 700 | -$26.9M | +$2.3M bull / -$6.7M bear | out (clean 27, ADX 45, RVol 3.8) |
| 10 | **IWM** | 280.44 | - | **-** | 25 | - | NEG -$432.1M | 281.23 | 280 | 270 | +$5.1M | +$51k bull / -$133k bear | out (clean 28, ADX 40, RVol 0.7) |
| 11 | **TSLA** | 401.63 | - | **-** | 25 | - | POS +$509.8M | - | 400 | 400 | -$27.8M | +$578k bull / -$8.6M bear | out (clean 29, ADX 26, RVol 2.0) |
| 12 | **AMZN** | 239.69 | - | **-** | 25 | - | NEG -$170.3M | 247.84 | 250 | 240 | -$5.8M | +$201k bull / -$2.2M bear | out (clean 32, ADX 23, RVol 3.9) |
| 13 | **NFLX** | 62.73 | - | **-** | 25 | - | NEG -$10.2M | 63.04 | 63 | 63 | +$600k | +$95k bull / +$0 bear | out (clean 32, ADX 34, RVol 0.9) |
| 14 | **MU** | 895.09 | - | **-** | 25 | - | NEG -$222.2M | 929.23 | 900 | 900 | +$21.6M | +$4.3M bull / -$903k bear | out (clean 29, ADX 34, RVol 1.5) |
| 15 | **HOOD** | 84.38 | - | **-** | 24 | - | NEG -$38.5M | - | 85 | 85 | +$447k | +$0 bull / -$59k bear | out (clean 31, ADX 53, RVol 1.3) |
| 16 | **AVGO** | 327.76 | - | **-** | 23 | - | NEG -$129.6M | 345.1 | 330 | 330 | +$455k | +$988k bull / -$1.5M bear | out (clean 29, ADX 50, RVol 1.4) |
| 17 | **DELL** | 433.34 | - | **-** | 23 | - | NEG -$56.6M | - | 440 | 425 | -$33k | +$295k bull / -$32k bear | out (clean 32, ADX 48, RVol 3.2) |
| 18 | **GOOGL** | 281.35 | - | **-** | 22 | - | NEG -$258.1M | - | 280 | 280 | -$1.2M | +$0 bull / -$187k bear | out (clean 31, ADX 30, RVol 1.0) |
| 19 | **SMCI** | 32.66 | - | **-** | 22 | - | POS +$918k | 32.55 | 35 | 32 | +$491k | - | out (clean 28, ADX 43, RVol 1.4) |
| 20 | **SPY** | 759.79 | - | **-** | 21 | - | NEG -$13.1B | 771.86 | 760 | 760 | +$10.7M | +$956k bull / -$4.2M bear | out (clean 27, ADX 42, RVol 1.5) |
| 21 | **PLTR** | 188.11 | - | **-** | 21 | - | NEG -$61.2M | 192.75 | 200 | 190 | -$729k | +$158k bull / -$163k bear | out (clean 25, ADX 36, RVol 1.3) |
| 22 | **MSFT** | 522.00 | - | **-** | 19 | - | POS +$503.2M | 514.78 | 525 | 525 | +$806k | +$543k bull / -$26k bear | out (clean 27, ADX 24, RVol 1.4) |
| 23 | **ORCL** | 132.95 | - | **-** | 17 | - | POS +$68.0M | 129.91 | 135 | 130 | +$905k | - | out (clean 33, ADX 38, RVol 0.9) |
| 24 | **SHOP** | 157.71 | - | **-** | 15 | - | NEG -$16.9M | 163.65 | 150 | 157.5 | +$75k | - | out (clean 25, ADX 45, RVol 1.7) |
| 25 | **BABA** | 99.08 | - | **-** | 10 | - | NEG -$32.4M | 100.45 | 100 | 99 | -$69k | - | out (clean 29, ADX 18, RVol 0.6) |
| 26 | **CRM** | 232.39 | - | **-** | 9 | - | NEG -$20.7M | 240.34 | 240 | 230 | -$69k | - | out (clean 27, ADX 15, RVol 0.7) |
| 27 | **UBER** | 65.37 | - | **-** | 5 | - | NEG -$30.1M | 66.32 | 66 | 65 | -$16k | - | out (clean 28, ADX 12, RVol 0.5) |

## Big prints this scan (235)
- **MSTR** CALL 136 2026-11-06 (7DTE): 3,750 @ 3.80 = **+$1.4M** SELL | vol 5,340 / OI 69
- **COIN** CALL 142 2026-11-06 (7DTE): 2,471 @ 5.09 = **+$1.3M** SELL | vol 5,152 / OI 1
- **COIN** CALL 142 2026-11-06 (7DTE): 1,250 @ 5.09 = **+$636k** SELL | vol 5,152 / OI 1
- **COIN** CALL 142 2026-11-06 (7DTE): 1,250 @ 5.09 = **+$636k** SELL | vol 5,152 / OI 1
- **MU** CALL 910 2026-11-02 (3DTE): 440 @ 11.40 = **+$502k** BUY | vol 1,685 / OI 199
- **MSTR** CALL 136 2026-11-06 (7DTE): 1,250 @ 3.80 = **+$475k** SELL | vol 5,340 / OI 69
- **SPY** CALL 758 2026-11-02 (3DTE): 888 @ 4.50 = **+$400k** BUY | vol 15,302 / OI 147
- **TSLA** PUT 405 2026-10-30 (0DTE): 500 @ 4.80 = **+$240k** BUY | vol 6,473 / OI 3,049
- **TSLA** PUT 405 2026-10-30 (0DTE): 500 @ 4.80 = **+$240k** BUY | vol 6,473 / OI 3,049
- **SPY** PUT 770 2026-11-06 (7DTE): 180 @ 12.50 = **+$225k** BUY | vol 1,218 / OI 4,714
- **TSLA** CALL 407.5 2026-11-06 (7DTE): 338 @ 6.65 = **+$225k** SELL | vol 2,498 / OI 628
- **QQQ** CALL 690 2026-11-03 (4DTE): 191 @ 11.63 = **+$222k** BUY | vol 1,195 / OI 105
- **QQQ** CALL 690 2026-11-03 (4DTE): 188 @ 11.63 = **+$219k** BUY | vol 1,195 / OI 105
- **TSLA** CALL 390 2026-11-02 (3DTE): 168 @ 12.70 = **+$213k** SELL | vol 2,284 / OI 626
- **QQQ** CALL 700 2026-11-06 (7DTE): 237 @ 8.93 = **+$212k** BUY | vol 22,866 / OI 1,011

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 759 2026-11-04 (5DTE): 609 traded vs OI 229
- **SPY** PUT 752 2026-11-04 (5DTE): 573 traded vs OI 535
- **SPY** PUT 725 2026-11-03 (4DTE): 850 traded vs OI 203
- **SPY** PUT 741 2026-11-02 (3DTE): 912 traded vs OI 857
- **SPY** PUT 764 2026-11-02 (3DTE): 691 traded vs OI 663
- **SPY** CALL 756 2026-11-02 (3DTE): 528 traded vs OI 45
- **SPY** PUT 735 2026-11-09 (10DTE): 500 traded vs OI 195
- **SPY** PUT 730 2026-11-10 (11DTE): 501 traded vs OI 154
- **SPY** CALL 762 2026-11-06 (7DTE): 2,382 traded vs OI 2,319
- **SPY** PUT 756 2026-11-06 (7DTE): 906 traded vs OI 826
- **QQQ** CALL 696 2026-11-04 (5DTE): 528 traded vs OI 0
- **QQQ** CALL 694 2026-11-06 (7DTE): 525 traded vs OI 56
- **QQQ** CALL 698 2026-11-06 (7DTE): 512 traded vs OI 88
- **QQQ** CALL 715 2026-11-04 (5DTE): 507 traded vs OI 280
- **QQQ** PUT 697 2026-11-03 (4DTE): 609 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
