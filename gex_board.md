# GEX + FLOW SCAN - Tue Nov 10, 10:40 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (3)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:15 | **IWM** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/10 280P | 0.63 | 1.24 | +97% (25m) | **+97%** | +22% | 280 hit |
| 09:50 | **SPY** | **PUTS** | FLOW SURGE | 11/10 743P | 0.77 | 0.37 | +5% (1m) | **-52%** | +54% | 745.65 |
| 09:45 | **IWM** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/10 279P | 0.52 | 0.71 | +50% (8m) | **+37%** | +87% | 278.66 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:40:08 ET, last candle SPY 10:39, QQQ 10:39 | no errors

## Flow surges NOT fired - price disagreed (6 today, last 5)
- 10:15 BABA PUTS: price +0.24 over the last 15 min - flow says one way, price says the other
- 10:10 BABA PUTS: price +0.73 over the last 15 min - flow says one way, price says the other
- 10:00 NFLX CALLS: price -0.14 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:00 AAPL CALLS: price -2.97 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 09:55 BABA CALLS: price -0.98 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **GOOGL** | 289.50 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 38 | none: 69 calls 0-7DTE > 6 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only +2% at the target (needs +20%) (1 contracts' greeks worked out here) | POS +$3.7M | 289.12 | 300 | 290 | +$1.2M | +$61k bull / +$0 bear | out (clean 30, ADX 14, RVol 0.8) |
| 2 | **MSTR** | 121.26 | FLIP CROSS down into negative gamma | **PUTS** | 32 | none: 24 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$6.8M | 123.96 | 133 | 110 | +$662k | +$54k bull / +$0 bear | out (clean 30, ADX 26, RVol 0.6) |
| 3 | **AMD** | 527.03 | - | **-** | 30 | - | POS +$46.7M | - | 500 | 500 | -$77.9M | +$5.4M bull / -$80k bear | out (clean 31, ADX 35, RVol 2.1) |
| 4 | **AAPL** | 348.23 | - | **-** | 29 | - | POS +$431.4M | 336.3 | 350 | 340 | +$16.5M | +$0 bull / -$179k bear | out (clean 28, ADX 21, RVol 0.9) |
| 5 | **AVGO** | 330.29 | - | **-** | 24 | - | NEG -$12.9M | 345.6 | 340 | 340 | -$9.1M | +$671k bull / +$0 bear | out (clean 31, ADX 33, RVol 1.3) |
| 6 | **IWM** | 279.33 | - | **-** | 23 | - | NEG -$1.3B | 283.86 | 280 | 270 | +$3.4M | +$138k bull / +$0 bear | out (clean 36, ADX 43, RVol 0.9) |
| 7 | **COIN** | 131.30 | - | **-** | 22 | - | POS +$3.3M | 128.7 | 137 | 135 | +$229k | +$27k bull / +$0 bear | out (clean 31, ADX 27, RVol 0.5) |
| 8 | **NVDA** | 171.05 | - | **-** | 21 | - | NEG -$182.2M | - | 185 | 170 | +$17.5M | +$1.5M bull / +$0 bear | out (clean 32, ADX 30, RVol 1.4) |
| 9 | **AMZN** | 271.59 | - | **-** | 20 | - | POS +$484.0M | - | 270 | 265 | +$3.9M | +$25k bull / -$147k bear | out (clean 33, ADX 33, RVol 0.6) |
| 10 | **UBER** | 70.16 | PINNED between the walls (positive gamma) - chop | **-** | 20 | - | POS +$8.7M | 68.48 | 70 | 70 | -$11k | - | out (clean 33, ADX 38, RVol 0.3) |
| 11 | **TSLA** | 376.49 | - | **-** | 19 | - | POS +$194.1M | - | 400 | 380 | -$5.5M | +$343k bull / -$636k bear | out (clean 34, ADX 36, RVol 0.4) |
| 12 | **DELL** | 335.12 | - | **-** | 18 | - | NEG -$8.8M | - | 350 | 340 | +$416k | +$74k bull / +$0 bear | out (clean 32, ADX 26, RVol 0.7) |
| 13 | **MU** | 720.42 | - | **-** | 18 | - | NEG -$27.6M | - | 750 | 750 | -$17.0M | +$5.8M bull / +$0 bear | out (clean 30, ADX 21, RVol 0.7) |
| 14 | **SPY** | 749.15 | - | **-** | 17 | - | NEG -$6.9B | 760.92 | 750 | 730 | -$11.6M | +$4.9M bull / +$0 bear | out (clean 32, ADX 29, RVol 0.4) |
| 15 | **QQQ** | 675.64 | - | **-** | 17 | - | NEG -$1.8B | 692.93 | 680 | 680 | -$32.1M | +$2.4M bull / +$0 bear | out (clean 31, ADX 22, RVol 0.5) |
| 16 | **BABA** | 103.96 | - | **-** | 17 | - | NEG -$6.3M | 106.09 | 110 | 100 | -$451k | - | out (clean 29, ADX 31, RVol 0.8) |
| 17 | **SMH** | 484.87 | - | **-** | 16 | - | NEG -$210.9M | - | 500 | 475 | -$470k | +$142k bull / +$0 bear | out (clean 29, ADX 19, RVol 0.6) |
| 18 | **META** | 643.56 | - | **-** | 16 | - | POS +$259.6M | 605.08 | 650 | 650 | -$372k | +$336k bull / +$0 bear | out (clean 33, ADX 22, RVol 0.6) |
| 19 | **ORCL** | 118.83 | - | **-** | 16 | - | NEG -$23.2M | - | 130 | 120 | +$29k | +$192k bull / +$0 bear | out (clean 28, ADX 27, RVol 0.4) |
| 20 | **HOOD** | 81.26 | - | **-** | 16 | - | POS +$3.1M | 79.08 | 85 | 80 | +$597k | - | out (clean 30, ADX 32, RVol 0.5) |
| 21 | **CRM** | 213.49 | - | **-** | 16 | - | NEG -$10.8M | - | 195 | 220 | -$90k | - | out (clean 31, ADX 34, RVol 0.3) |
| 22 | **ARM** | 180.89 | - | **-** | 15 | - | NEG -$5.0M | - | 185 | 190 | -$138k | - | out (clean 27, ADX 25, RVol 0.7) |
| 23 | **PLTR** | 166.89 | - | **-** | 12 | - | POS +$52.6M | - | 165 | 170 | -$426k | - | out (clean 28, ADX 43, RVol 0.8) |
| 24 | **NFLX** | 63.06 | - | **-** | 10 | - | NEG -$20.0M | 65.26 | 65 | 60 | -$209k | - | out (clean 30, ADX 30, RVol 0.9) |
| 25 | **SHOP** | 149.18 | - | **-** | 9 | - | POS +$1.9M | 144.95 | 155 | 140 | +$3k | - | out (clean 31, ADX 36, RVol 0.3) |
| 26 | **MSFT** | 542.84 | - | **-** | 8 | - | POS +$672.3M | - | 550 | 535 | -$111k | - | out (clean 33, ADX 38, RVol 0.4) |
| 27 | **SMCI** | 28.29 | - | **-** | 8 | - | POS +$3.6M | - | 30 | 30 | -$60k | - | out (clean 28, ADX 21, RVol 0.4) |

## Big prints this scan (133)
- **AMD** CALL 530 2026-11-13 (3DTE): 151 @ 21.50 = **+$325k** BUY | vol 2,535 / OI 1,599
- **SPY** PUT 738 2026-11-13 (3DTE): 1,600 @ 1.68 = **+$269k** SELL | vol 3,998 / OI 5,354
- **SPY** PUT 738 2026-11-13 (3DTE): 1,500 @ 1.69 = **+$254k** SELL | vol 3,998 / OI 5,354
- **AMD** CALL 530 2026-11-13 (3DTE): 100 @ 21.30 = **+$213k** BUY | vol 2,535 / OI 1,599
- **QQQ** CALL 679 2026-11-11 (1DTE): 433 @ 4.50 = **+$195k** BUY | vol 5,095 / OI 135
- **QQQ** PUT 680 2026-11-10 (0DTE): 499 @ 3.50 = **+$175k** SELL | vol 24,860 / OI 670
- **QQQ** PUT 680 2026-11-10 (0DTE): 499 @ 3.30 = **+$165k** SELL | vol 24,860 / OI 670
- **TSLA** CALL 372.5 2026-11-11 (1DTE): 200 @ 7.50 = **+$150k** BUY | vol 5,734 / OI 914
- **MU** PUT 700 2026-11-11 (1DTE): 260 @ 5.40 = **+$140k** SELL | vol 6,147 / OI 160
- **MU** CALL 700 2026-11-13 (3DTE): 34 @ 40.05 = **+$136k** BUY | vol 342 / OI 841
- **MU** CALL 740 2026-11-11 (1DTE): 100 @ 12.45 = **+$124k** BUY | vol 4,084 / OI 238
- **QQQ** PUT 675 2026-11-13 (3DTE): 200 @ 6.10 = **+$122k** SELL | vol 3,150 / OI 5,033
- **QQQ** PUT 675 2026-11-10 (0DTE): 875 @ 1.36 = **+$119k** SELL | vol 61,331 / OI 718
- **QQQ** PUT 680 2026-11-12 (2DTE): 160 @ 7.20 = **+$115k** SELL | vol 2,585 / OI 236
- **MU** PUT 700 2026-11-11 (1DTE): 182 @ 6.15 = **+$112k** SELL | vol 6,147 / OI 160

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 762 2026-11-12 (2DTE): 582 traded vs OI 557
- **SPY** PUT 754 2026-11-11 (1DTE): 542 traded vs OI 234
- **SPY** PUT 733 2026-11-12 (2DTE): 501 traded vs OI 266
- **SPY** CALL 763 2026-11-12 (2DTE): 570 traded vs OI 214
- **SPY** CALL 772 2026-11-16 (6DTE): 863 traded vs OI 668
- **SPY** PUT 690 2026-11-19 (9DTE): 729 traded vs OI 379
- **SPY** CALL 758 2026-11-18 (8DTE): 617 traded vs OI 282
- **SPY** PUT 690 2026-11-30 (20DTE): 3,789 traded vs OI 2,049
- **SPY** CALL 760 2026-11-24 (14DTE): 551 traded vs OI 0
- **SPY** CALL 770 2026-11-24 (14DTE): 519 traded vs OI 0
- **QQQ** CALL 696 2026-11-13 (3DTE): 533 traded vs OI 521
- **QQQ** CALL 679 2026-11-13 (3DTE): 721 traded vs OI 394
- **QQQ** PUT 630 2026-11-10 (0DTE): 1,270 traded vs OI 1,236
- **QQQ** PUT 646 2026-11-13 (3DTE): 516 traded vs OI 174
- **IWM** CALL 283 2026-11-16 (6DTE): 524 traded vs OI 106

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
