# GEX + FLOW SCAN - Fri Oct 30, 11:10 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (2)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:25 | **SMCI** | **PUTS** | FLIP CROSS down into negative gamma | 10/30 32.5P | 0.43 | 0.22 | -12% (1m) | **-49%** | +32% | 32 |
| 10:15 | **AAPL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 10/30 347.5C | 0.50 | 1.34 | +356% (38m) | **+168%** | +104% | 347.56 hit |

## 1m RULES on SPY / QQQ - loose (1 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 11:10:08 ET, last candle SPY 11:09, QQQ 11:09 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 11:05 | SPY | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |

## Flow surges NOT fired - price disagreed (37 today, last 5)
- 11:10 MSTR PUTS: price +1.77 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:55 AAPL PUTS: price +1.23 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:50 AAPL PUTS: price +2.30 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:45 SMCI CALLS: under EMA 20 - flow says one way, price says the other
- 10:45 AAPL PUTS: price +2.47 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **ARM** | 205.16 | FLOW SURGE | **CALLS** | 60 | none: 34 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (32 contracts' greeks worked out here) | NEG -$20.0M | - | 220 | 205 | +$456k | +$35k bull / +$0 bear | out (clean 26, ADX 48, RVol 3.4) |
| 2 | **MSTR** | 132.54 | FLOW SURGE | **PUTS** | 49 | 10/30 129P @ 0.57 (delta 0.21) = est +80% at 130 | NEG -$21.7M | - | 135 | 130 | -$5.0M | +$0 bull / -$2.8M bear | out (clean 27, ADX 36, RVol 2.0) |
| 3 | **META** | 624.99 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 47 | none: 199 calls 0-7DTE > 10 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (91 contracts' greeks worked out here) | POS +$50.1M | 622.88 | 630 | 625 | -$11.8M | +$28k bull / -$3.2M bear | out (clean 28, ADX 20, RVol 1.0) |
| 4 | **SMCI** | 32.61 | FLIP CROSS up into positive gamma | **CALLS** | 38 | 10/30 32C @ 0.72 (delta 0.81) = est +64% at 33.21 | POS +$463k | 32.55 | 35 | 32 | +$522k | - | out (clean 28, ADX 42, RVol 1.4) |
| 5 | **COIN** | 140.80 | - | **-** | 32 | - | NEG -$15.4M | - | 150 | 140 | -$3.1M | +$0 bull / -$3.0M bear | out (clean 27, ADX 55, RVol 2.1) |
| 6 | **NVDA** | 206.64 | - | **-** | 28 | - | NEG -$434.0M | 212.04 | 210 | 205 | +$9.6M | +$3.5M bull / -$542k bear | out (clean 26, ADX 40, RVol 1.5) |
| 7 | **ORCL** | 132.39 | - | **-** | 28 | - | POS +$55.3M | 129.03 | 135 | 130 | +$1.1M | +$75k bull / +$0 bear | out (clean 33, ADX 40, RVol 0.9) |
| 8 | **SHOP** | 156.78 | - | **-** | 28 | - | NEG -$15.0M | 163.31 | 150 | 157.5 | +$176k | +$45k bull / +$0 bear | out (clean 26, ADX 47, RVol 1.6) |
| 9 | **SMH** | 527.67 | - | **-** | 27 | - | NEG -$574.4M | - | 530 | 530 | +$4.0M | +$3.5M bull / -$954k bear | out (clean 28, ADX 47, RVol 1.5) |
| 10 | **AMD** | 513.43 | - | **-** | 27 | - | NEG -$94.3M | 524.22 | 527.5 | 500 | +$9.1M | +$1.2M bull / -$437k bear | out (clean 28, ADX 39, RVol 1.7) |
| 11 | **AAPL** | 348.03 | - | **-** | 26 | - | POS +$724.6M | 343.12 | 350 | 345 | -$6.9M | +$221k bull / -$523k bear | out (clean 31, ADX 34, RVol 1.6) |
| 12 | **AMZN** | 240.61 | - | **-** | 26 | - | NEG -$145.4M | 246.36 | 250 | 240 | -$7.6M | +$373k bull / -$402k bear | out (clean 32, ADX 21, RVol 3.5) |
| 13 | **GOOGL** | 282.49 | - | **-** | 26 | - | NEG -$256.5M | - | 280 | 280 | -$3.3M | +$0 bull / -$918k bear | out (clean 31, ADX 27, RVol 1.1) |
| 14 | **NFLX** | 62.63 | - | **-** | 25 | - | NEG -$13.3M | 63.08 | 63 | 63 | +$715k | +$169k bull / +$0 bear | out (clean 31, ADX 31, RVol 0.9) |
| 15 | **DELL** | 431.21 | - | **-** | 25 | - | NEG -$57.2M | - | 440 | 425 | +$379k | +$295k bull / -$32k bear | out (clean 32, ADX 47, RVol 3.3) |
| 16 | **MU** | 893.40 | - | **-** | 25 | - | NEG -$202.1M | 926.27 | 900 | 900 | +$25.3M | +$5.4M bull / -$429k bear | out (clean 29, ADX 33, RVol 1.3) |
| 17 | **IWM** | 280.14 | - | **-** | 24 | - | NEG -$577.6M | 281.29 | 280 | 270 | +$4.9M | +$51k bull / -$200k bear | out (clean 28, ADX 38, RVol 0.6) |
| 18 | **AVGO** | 327.19 | - | **-** | 24 | - | NEG -$138.2M | 344.55 | 330 | 330 | +$915k | +$1.2M bull / -$38k bear | out (clean 30, ADX 51, RVol 1.3) |
| 19 | **PLTR** | 187.47 | - | **-** | 24 | - | NEG -$57.2M | 191.37 | 200 | 190 | -$2.8M | +$778k bull / -$72k bear | out (clean 25, ADX 36, RVol 1.1) |
| 20 | **QQQ** | 696.19 | - | **-** | 23 | - | NEG -$9.8B | 726.95 | 720 | 700 | -$17.4M | +$4.3M bull / -$6.3M bear | out (clean 27, ADX 45, RVol 2.0) |
| 21 | **TSLA** | 403.09 | - | **-** | 23 | - | POS +$464.0M | 389.73 | 400 | 400 | -$27.0M | +$3.0M bull / -$7.1M bear | out (clean 29, ADX 25, RVol 2.0) |
| 22 | **HOOD** | 84.24 | - | **-** | 23 | - | NEG -$36.4M | - | 85 | 85 | +$318k | +$0 bull / -$27k bear | out (clean 31, ADX 53, RVol 1.3) |
| 23 | **SPY** | 759.30 | - | **-** | 22 | - | NEG -$13.3B | 771.37 | 760 | 760 | +$32.4M | +$2.2M bull / -$3.9M bear | out (clean 27, ADX 41, RVol 1.3) |
| 24 | **MSFT** | 522.15 | - | **-** | 20 | - | POS +$498.1M | 514.71 | 525 | 525 | +$1.2M | +$163k bull / +$0 bear | out (clean 26, ADX 24, RVol 1.1) |
| 25 | **CRM** | 232.17 | - | **-** | 8 | - | NEG -$20.7M | 240.65 | 240 | 230 | -$66k | - | out (clean 27, ADX 14, RVol 0.7) |
| 26 | **BABA** | 98.84 | - | **-** | 5 | - | NEG -$31.6M | 100.3 | 100 | 99 | -$20k | - | out (clean 29, ADX 17, RVol 0.5) |
| 27 | **UBER** | 65.25 | - | **-** | 4 | - | NEG -$32.7M | 66.26 | 70 | 65 | -$10k | - | out (clean 28, ADX 11, RVol 0.4) |

## Big prints this scan (85)
- **QQQ** CALL 700 2026-11-06 (7DTE): 327 @ 8.63 = **+$282k** SELL | vol 25,595 / OI 1,011
- **SPY** PUT 765 2026-10-30 (0DTE): 500 @ 5.53 = **+$276k** SELL | vol 13,779 / OI 59,152
- **SPY** PUT 765 2026-10-30 (0DTE): 500 @ 5.42 = **+$271k** SELL | vol 13,779 / OI 59,152
- **QQQ** CALL 700 2026-11-06 (7DTE): 299 @ 8.65 = **+$259k** SELL | vol 25,595 / OI 1,011
- **TSLA** CALL 395 2026-11-04 (5DTE): 200 @ 12.50 = **+$250k** SELL | vol 1,159 / OI 167
- **AMD** CALL 520 2026-11-06 (7DTE): 100 @ 22.78 = **+$228k** BUY | vol 374 / OI 581
- **MU** PUT 880 2026-10-30 (0DTE): 741 @ 2.40 = **+$178k** BUY | vol 19,214 / OI 2,467
- **QQQ** CALL 695 2026-11-02 (3DTE): 267 @ 6.38 = **+$170k** BUY | vol 8,761 / OI 107
- **MU** PUT 880 2026-10-30 (0DTE): 683 @ 2.30 = **+$157k** BUY | vol 19,214 / OI 2,467
- **SPY** PUT 762 2026-10-30 (0DTE): 500 @ 3.07 = **+$154k** SELL | vol 23,435 / OI 6,095
- **SPY** PUT 762 2026-10-30 (0DTE): 500 @ 2.99 = **+$150k** SELL | vol 23,435 / OI 6,095
- **SPY** PUT 765 2026-10-30 (0DTE): 250 @ 5.48 = **+$137k** SELL | vol 13,779 / OI 59,152
- **SPY** PUT 759 2026-11-04 (5DTE): 251 @ 5.14 = **+$129k** BUY | vol 1,731 / OI 979
- **QQQ** CALL 700 2026-11-06 (7DTE): 145 @ 8.65 = **+$125k** SELL | vol 25,595 / OI 1,011
- **META** PUT 620 2026-11-06 (7DTE): 100 @ 12.00 = **+$120k** BUY | vol 678 / OI 765

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 736 2026-11-04 (5DTE): 898 traded vs OI 90
- **SPY** PUT 756 2026-11-03 (4DTE): 544 traded vs OI 460
- **SPY** PUT 734 2026-11-04 (5DTE): 1,267 traded vs OI 42
- **SPY** PUT 715 2026-11-05 (6DTE): 501 traded vs OI 162
- **SPY** PUT 705 2026-11-10 (11DTE): 530 traded vs OI 4
- **SPY** PUT 709 2026-11-20 (21DTE): 2,301 traded vs OI 1,503
- **SPY** PUT 740 2026-11-13 (14DTE): 6,718 traded vs OI 5,698
- **QQQ** CALL 712 2026-11-06 (7DTE): 1,670 traded vs OI 221
- **QQQ** PUT 685 2026-11-09 (10DTE): 503 traded vs OI 409
- **IWM** PUT 275 2026-11-02 (3DTE): 1,980 traded vs OI 1,526
- **SMH** CALL 575 2026-11-20 (21DTE): 2,210 traded vs OI 2,200
- **NVDA** CALL 212.5 2026-11-13 (14DTE): 500 traded vs OI 60
- **NVDA** PUT 197.5 2026-11-02 (3DTE): 1,157 traded vs OI 948
- **TSLA** CALL 417.5 2026-10-30 (0DTE): 2,645 traded vs OI 2,529
- **TSLA** CALL 415 2026-11-04 (5DTE): 794 traded vs OI 774

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
