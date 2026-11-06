# GEX + FLOW SCAN - Fri Nov 06, 11:00 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (3)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:30 | **NVDA** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/06 192.5C | 0.73 | 0.55 | +12% (20m) | **-25%** | +199% | 193.9 |
| 10:00 | **NVDA** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/06 197.5C | 0.67 | 0.04 | -6% (1m) | **-94%** | +24% | 195 |
| 09:50 | **NFLX** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/06 64C | 0.40 | 0.36 | +32% (4m) | **-10%** (done) | +164% | 65 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 11:00:08 ET, last candle SPY 10:59, QQQ 10:59 | no errors

## Flow surges NOT fired - price disagreed (6 today, last 5)
- 09:55 SMCI PUTS: price +0.09 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 HOOD PUTS: price +3.27 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 MSTR PUTS: price +3.75 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 SMCI PUTS: price +0.89 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 PLTR PUTS: price +5.57 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **NVDA** | 189.50 | RUN: clean trend + negative gamma + flow agrees | **CALLS** | 48 | 11/06 192.5C @ 0.49 (delta 0.22) = est +203% at 192.92 | NEG -$395.3M | - | 200 | 190 | +$14.3M | +$112k bull / -$6.7M bear | LONG (clean 34, ADX 24, RVol 1.4) |
| 2 | **AAPL** | 344.90 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 40 | 11/06 347.5C @ 0.46 (delta 0.23) = est +455% at 350 | POS +$168.7M | 343.03 | 350 | 345 | -$16.5M | +$0 bull / -$2.5M bear | out (clean 29, ADX 14, RVol 0.7) |
| 3 | **META** | 622.58 | FLIP CROSS down into negative gamma | **PUTS** | 38 | none: 196 puts 0-7DTE > 8 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (84 contracts' greeks worked out here) | NEG -$15.2M | 623.21 | 650 | 625 | -$10.7M | +$0 bull / -$2.9M bear | out (clean 33, ADX 44, RVol 0.8) |
| 4 | **TSLA** | 359.31 | TREND (flow not with it) | **CALLS** | 30 | none: 116 calls 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (50 contracts' greeks worked out here) | NEG -$280.9M | - | 370 | 360 | -$62.2M | +$300k bull / -$3.7M bear | LONG (clean 35, ADX 43, RVol 0.7) |
| 5 | **MSTR** | 127.92 | - | **-** | 24 | - | POS +$3.0M | 127.65 | 135 | 125 | -$7.8M | +$0 bull / -$1.9M bear | out (clean 31, ADX 17, RVol 1.1) |
| 6 | **SMH** | 464.03 | - | **-** | 22 | - | NEG -$527.2M | - | 505 | 465 | +$4.0M | +$0 bull / -$1.5M bear | out (clean 34, ADX 16, RVol 2.9) |
| 7 | **DELL** | 334.54 | - | **-** | 22 | - | NEG -$25.7M | - | 340 | 335 | +$3.6M | +$35k bull / -$774k bear | out (clean 33, ADX 17, RVol 0.6) |
| 8 | **COIN** | 134.78 | - | **-** | 21 | - | NEG -$13.6M | 136.55 | 141 | 135 | -$2.2M | +$58k bull / +$0 bear | out (clean 31, ADX 16, RVol 0.5) |
| 9 | **MU** | 689.30 | - | **-** | 20 | - | NEG -$180.6M | - | 700 | 700 | +$71.0M | +$117k bull / -$10.7M bear | out (clean 32, ADX 16, RVol 1.2) |
| 10 | **AMZN** | 263.57 | - | **-** | 19 | - | POS +$373.0M | - | 265 | 265 | -$3.6M | +$150k bull / -$1.1M bear | out (clean 34, ADX 28, RVol 0.5) |
| 11 | **PLTR** | 161.72 | - | **-** | 19 | - | NEG -$69.4M | - | 165 | 160 | +$1.3M | +$0 bull / -$365k bear | out (clean 28, ADX 33, RVol 0.7) |
| 12 | **HOOD** | 80.02 | - | **-** | 19 | - | NEG -$21.0M | 84.51 | 85 | 80 | +$2.0M | +$0 bull / -$177k bear | out (clean 29, ADX 24, RVol 0.7) |
| 13 | **SPY** | 740.00 | - | **-** | 18 | - | NEG -$14.3B | 769.65 | 770 | 740 | -$113.4M | +$0 bull / -$3.2M bear | out (clean 35, ADX 17, RVol 0.9) |
| 14 | **GOOGL** | 287.76 | - | **-** | 18 | - | POS +$58.4M | 285 | 290 | 290 | +$1.9M | +$0 bull / -$65k bear | out (clean 34, ADX 21, RVol 0.7) |
| 15 | **IWM** | 272.58 | - | **-** | 17 | - | NEG -$3.4B | 285.66 | 285 | 270 | -$4.3M | +$0 bull / -$239k bear | out (clean 34, ADX 15, RVol 0.7) |
| 16 | **BABA** | 108.85 | - | **-** | 17 | - | POS +$31.9M | - | 110 | 110 | -$265k | +$0 bull / -$32k bear | out (clean 34, ADX 18, RVol 0.5) |
| 17 | **AMD** | 442.98 | - | **-** | 16 | - | NEG -$174.5M | - | 430 | 450 | +$836k | +$0 bull / -$6.9M bear | out (clean 33, ADX 22, RVol 1.1) |
| 18 | **MSFT** | 535.51 | - | **-** | 16 | - | POS +$672.8M | 509.73 | 540 | 540 | -$374k | +$2.7M bull / -$536k bear | out (clean 32, ADX 21, RVol 1.0) |
| 19 | **AVGO** | 297.26 | - | **-** | 16 | - | NEG -$143.1M | - | 325 | 300 | -$232k | +$61k bull / -$467k bear | out (clean 31, ADX 18, RVol 1.1) |
| 20 | **QQQ** | 660.06 | - | **-** | 15 | - | NEG -$6.0B | - | 700 | 680 | -$207k | +$108k bull / -$6.5M bear | out (clean 35, ADX 19, RVol 0.8) |
| 21 | **CRM** | 214.23 | - | **-** | 14 | - | NEG -$20.7M | - | 230 | 215 | +$218k | - | out (clean 34, ADX 42, RVol 0.8) |
| 22 | **ARM** | 173.13 | - | **-** | 10 | - | NEG -$23.9M | - | 190 | 170 | -$560k | - | out (clean 25, ADX 12, RVol 1.1) |
| 23 | **SMCI** | 28.84 | - | **-** | 9 | - | NEG -$4.7M | - | 30 | 30 | +$211k | - | out (clean 35, ADX 30, RVol 0.4) |
| 24 | **NFLX** | 64.27 | - | **-** | 8 | - | POS +$11.7M | 63.52 | 65 | 65 | -$225k | - | out (clean 32, ADX 21, RVol 0.8) |
| 25 | **SHOP** | 148.48 | - | **-** | 7 | - | NEG -$3.5M | 151.47 | 150 | 150 | -$30k | - | out (clean 37, ADX 25, RVol 0.6) |
| 26 | **UBER** | 69.69 | - | **-** | 6 | - | POS +$11.1M | 68.7 | 70 | 70 | +$90k | - | out (clean 30, ADX 10, RVol 0.5) |
| 27 | **ORCL** | 117.45 | - | **-** | 3 | - | NEG -$73.6M | - | 125 | 115 | -$24k | - | out (clean 30, ADX 13, RVol 0.5) |

## Big prints this scan (142)
- **QQQ** CALL 653 2026-11-06 (0DTE): 1,000 @ 6.39 = **+$639k** SELL | vol 5,204 / OI 0
- **SPY** PUT 741 2026-11-06 (0DTE): 853 @ 4.59 = **+$392k** BUY | vol 28,708 / OI 4,188
- **QQQ** PUT 658 2026-11-06 (0DTE): 800 @ 4.40 = **+$352k** BUY | vol 42,625 / OI 466
- **SPY** PUT 740 2026-11-06 (0DTE): 853 @ 3.98 = **+$339k** BUY | vol 71,002 / OI 21,704
- **QQQ** PUT 685 2026-11-13 (7DTE): 104 @ 29.28 = **+$305k** BUY | vol 265 / OI 30,486
- **QQQ** PUT 663 2026-11-06 (0DTE): 400 @ 6.80 = **+$272k** BUY | vol 14,941 / OI 190
- **QQQ** PUT 632 2026-11-13 (7DTE): 391 @ 5.23 = **+$204k** BUY | vol 1,741 / OI 0
- **QQQ** CALL 653 2026-11-06 (0DTE): 236 @ 6.90 = **+$163k** SELL | vol 5,204 / OI 0
- **QQQ** PUT 632 2026-11-13 (7DTE): 304 @ 5.23 = **+$159k** BUY | vol 1,741 / OI 0
- **QQQ** PUT 658 2026-11-06 (0DTE): 400 @ 3.80 = **+$152k** BUY | vol 42,625 / OI 466
- **AMD** PUT 435 2026-11-06 (0DTE): 272 @ 5.50 = **+$150k** BUY | vol 6,622 / OI 973
- **MU** PUT 690 2026-11-06 (0DTE): 100 @ 14.50 = **+$145k** BUY | vol 9,768 / OI 1,246
- **QQQ** CALL 663 2026-11-06 (0DTE): 1,000 @ 1.44 = **+$144k** SELL | vol 51,209 / OI 0
- **MU** PUT 680 2026-11-13 (7DTE): 40 @ 36.00 = **+$144k** BUY | vol 382 / OI 359
- **TSLA** PUT 350 2026-11-06 (0DTE): 1,348 @ 1.05 = **+$142k** BUY | vol 39,549 / OI 5,385

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 741 2026-11-11 (5DTE): 530 traded vs OI 0
- **SPY** CALL 734 2026-11-10 (4DTE): 500 traded vs OI 15
- **SPY** PUT 730 2026-11-10 (4DTE): 1,173 traded vs OI 1,158
- **SPY** CALL 742 2026-11-11 (5DTE): 514 traded vs OI 0
- **SPY** CALL 731 2026-11-09 (3DTE): 507 traded vs OI 2
- **SPY** CALL 765 2026-11-19 (13DTE): 503 traded vs OI 0
- **SPY** CALL 743 2026-11-20 (14DTE): 1,440 traded vs OI 71
- **SPY** CALL 738 2026-11-20 (14DTE): 1,372 traded vs OI 77
- **QQQ** PUT 659 2026-11-10 (4DTE): 555 traded vs OI 68
- **QQQ** CALL 680 2026-11-10 (4DTE): 518 traded vs OI 196
- **QQQ** PUT 636 2026-11-09 (3DTE): 542 traded vs OI 0
- **QQQ** PUT 649 2026-11-09 (3DTE): 549 traded vs OI 0
- **QQQ** PUT 632 2026-11-13 (7DTE): 1,741 traded vs OI 0
- **QQQ** CALL 675 2026-11-27 (21DTE): 508 traded vs OI 88
- **SMH** PUT 445 2026-11-06 (0DTE): 528 traded vs OI 416

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
