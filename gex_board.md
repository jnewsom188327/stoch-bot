# GEX + FLOW SCAN - Fri Nov 06, 11:20 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (3)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:30 | **NVDA** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/06 192.5C | 0.73 | 0.24 | +12% (20m) | **-67%** | +199% | 193.9 |
| 10:00 | **NVDA** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/06 197.5C | 0.67 | 0.03 | -6% (1m) | **-96%** (done) | +24% | 195 |
| 09:50 | **NFLX** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/06 64C | 0.40 | 0.36 | +32% (4m) | **-10%** (done) | +164% | 65 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 11:20:08 ET, last candle SPY 11:19, QQQ 11:19 | no errors

## Flow surges NOT fired - price disagreed (6 today, last 5)
- 09:55 SMCI PUTS: price +0.09 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 HOOD PUTS: price +3.27 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 MSTR PUTS: price +3.75 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 SMCI PUTS: price +0.89 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 PLTR PUTS: price +5.57 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **AAPL** | 344.68 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 40 | 11/06 347.5C @ 0.43 (delta 0.21) = est +477% at 350 | POS +$134.3M | 343.23 | 350 | 345 | -$19.2M | +$946k bull / -$65k bear | out (clean 29, ADX 14, RVol 0.7) |
| 2 | **MSFT** | 535.30 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 34 | 11/06 540C @ 0.66 (delta 0.20) = est +169% at 540 | POS +$669.6M | 512.94 | 540 | 535 | +$1.9M | +$309k bull / -$27k bear | out (clean 33, ADX 16, RVol 0.6) |
| 3 | **NFLX** | 64.15 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 24 | none: 26 puts 0-7DTE > 1 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only -11% at the target (needs +20%) (20 contracts' greeks worked out here) | POS +$10.1M | 63.83 | 64 | 65 | -$269k | - | out (clean 32, ADX 17, RVol 0.6) |
| 4 | **TSLA** | 358.60 | - | **-** | 23 | - | NEG -$294.5M | - | 370 | 360 | -$58.2M | +$1.9M bull / -$75k bear | out (clean 35, ADX 38, RVol 0.6) |
| 5 | **MSTR** | 126.66 | - | **-** | 22 | - | NEG -$7.0M | 127.31 | 135 | 125 | -$7.2M | +$47k bull / +$0 bear | out (clean 31, ADX 15, RVol 0.7) |
| 6 | **DELL** | 330.68 | - | **-** | 21 | - | NEG -$23.8M | - | 340 | 335 | +$4.1M | +$73k bull / +$0 bear | out (clean 33, ADX 16, RVol 0.5) |
| 7 | **HOOD** | 79.06 | - | **-** | 21 | - | NEG -$21.3M | - | 85 | 80 | +$3.8M | +$285k bull / +$0 bear | out (clean 30, ADX 20, RVol 0.7) |
| 8 | **SMH** | 460.74 | - | **-** | 20 | - | NEG -$475.8M | - | 505 | 465 | +$7.6M | +$1.4M bull / +$0 bear | out (clean 34, ADX 13, RVol 0.8) |
| 9 | **META** | 618.39 | - | **-** | 20 | - | NEG -$91.1M | 622.35 | 650 | 610 | -$4.4M | +$1.2M bull / +$0 bear | out (clean 33, ADX 41, RVol 0.7) |
| 10 | **PLTR** | 159.94 | - | **-** | 20 | - | NEG -$73.5M | - | 165 | 160 | +$3.0M | +$131k bull / +$0 bear | out (clean 28, ADX 27, RVol 0.8) |
| 11 | **MU** | 687.66 | - | **-** | 19 | - | NEG -$171.9M | - | 700 | 700 | +$80.1M | +$6.0M bull / -$985k bear | out (clean 32, ADX 14, RVol 0.7) |
| 12 | **CRM** | 215.33 | - | **-** | 19 | - | NEG -$25.9M | - | 230 | 220 | +$118k | +$58k bull / +$0 bear | out (clean 34, ADX 34, RVol 0.5) |
| 13 | **NVDA** | 187.51 | - | **-** | 18 | - | NEG -$380.5M | - | 200 | 190 | +$27.3M | +$3.8M bull / +$0 bear | out (clean 34, ADX 19, RVol 0.9) |
| 14 | **AMZN** | 262.83 | - | **-** | 17 | - | POS +$365.4M | - | 265 | 260 | -$2.1M | +$119k bull / +$0 bear | out (clean 34, ADX 26, RVol 0.5) |
| 15 | **GOOGL** | 287.01 | - | **-** | 17 | - | POS +$73.0M | 282.61 | 285 | 290 | +$2.3M | +$628k bull / -$42k bear | out (clean 34, ADX 17, RVol 0.5) |
| 16 | **SPY** | 738.32 | - | **-** | 16 | - | NEG -$14.4B | 768.34 | 770 | 740 | -$72.8M | +$1.7M bull / +$0 bear | out (clean 35, ADX 14, RVol 0.7) |
| 17 | **QQQ** | 657.50 | - | **-** | 16 | - | NEG -$5.5B | - | 700 | 680 | +$66.0M | +$2.4M bull / +$0 bear | out (clean 35, ADX 15, RVol 0.6) |
| 18 | **AMD** | 439.81 | - | **-** | 16 | - | NEG -$172.4M | - | 430 | 450 | +$7.5M | +$987k bull / -$135k bear | out (clean 33, ADX 19, RVol 0.9) |
| 19 | **AVGO** | 295.00 | - | **-** | 16 | - | NEG -$134.1M | - | 320 | 300 | +$1.5M | +$27k bull / +$0 bear | out (clean 31, ADX 16, RVol 0.9) |
| 20 | **ORCL** | 115.81 | - | **-** | 15 | - | NEG -$72.3M | - | 125 | 115 | +$544k | +$82k bull / +$0 bear | out (clean 30, ADX 12, RVol 0.5) |
| 21 | **COIN** | 132.09 | - | **-** | 11 | - | NEG -$20.5M | 136.36 | 142 | 130 | -$1.9M | - | out (clean 31, ADX 18, RVol 0.7) |
| 22 | **SMCI** | 28.45 | - | **-** | 9 | - | NEG -$4.3M | - | 30 | 30 | +$361k | - | out (clean 35, ADX 25, RVol 0.3) |
| 23 | **ARM** | 171.28 | - | **-** | 7 | - | NEG -$23.4M | - | 180 | 170 | -$367k | - | out (clean 25, ADX 10, RVol 0.8) |
| 24 | **BABA** | 109.04 | - | **-** | 7 | - | POS +$30.1M | - | 110 | 110 | -$308k | - | out (clean 34, ADX 20, RVol 0.3) |
| 25 | **IWM** | 272.41 | - | **-** | 6 | - | NEG -$3.5B | 286.15 | 285 | 270 | -$3.5M | - | out (clean 34, ADX 15, RVol 0.5) |
| 26 | **SHOP** | 148.16 | - | **-** | 6 | - | NEG -$2.9M | 150.47 | 150 | 145 | -$12k | - | out (clean 37, ADX 26, RVol 0.7) |
| 27 | **UBER** | 69.75 | - | **-** | 5 | - | POS +$15.2M | 68.77 | 70 | 70 | +$59k | - | out (clean 30, ADX 9, RVol 0.4) |

## Big prints this scan (109)
- **NVDA** CALL 195 2026-11-13 (7DTE): 3,999 @ 3.83 = **+$1.5M** BUY | vol 17,441 / OI 582
- **NVDA** CALL 195 2026-11-13 (7DTE): 1,000 @ 3.83 = **+$383k** BUY | vol 17,441 / OI 582
- **QQQ** PUT 660 2026-11-06 (0DTE): 500 @ 3.90 = **+$195k** SELL | vol 85,928 / OI 12,054
- **MU** PUT 700 2026-11-06 (0DTE): 110 @ 17.35 = **+$191k** SELL | vol 20,166 / OI 2,759
- **MU** PUT 680 2026-11-09 (3DTE): 87 @ 18.68 = **+$163k** SELL | vol 1,467 / OI 24
- **SMH** PUT 460 2026-11-11 (5DTE): 120 @ 12.40 = **+$149k** SELL | vol 409 / OI 1
- **SMH** PUT 460 2026-11-11 (5DTE): 120 @ 12.40 = **+$149k** SELL | vol 409 / OI 1
- **SMH** PUT 460 2026-11-11 (5DTE): 120 @ 12.40 = **+$149k** SELL | vol 409 / OI 1
- **MU** CALL 680 2026-11-06 (0DTE): 95 @ 15.35 = **+$146k** BUY | vol 3,226 / OI 21
- **MU** PUT 670 2026-11-06 (0DTE): 300 @ 4.50 = **+$135k** BUY | vol 16,174 / OI 734
- **MU** PUT 670 2026-11-06 (0DTE): 250 @ 5.15 = **+$129k** BUY | vol 16,174 / OI 734
- **NVDA** CALL 195 2026-11-13 (7DTE): 330 @ 3.70 = **+$122k** BUY | vol 17,441 / OI 582
- **GOOGL** PUT 290 2026-11-09 (3DTE): 250 @ 4.80 = **+$120k** SELL | vol 392 / OI 346
- **QQQ** PUT 660 2026-11-06 (0DTE): 309 @ 3.65 = **+$113k** SELL | vol 85,928 / OI 12,054
- **SPY** PUT 760 2026-11-13 (7DTE): 50 @ 21.42 = **+$107k** SELL | vol 210 / OI 6,735

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 736 2026-11-11 (5DTE): 573 traded vs OI 230
- **SPY** PUT 729 2026-11-10 (4DTE): 733 traded vs OI 732
- **SPY** PUT 706 2026-11-10 (4DTE): 537 traded vs OI 5
- **SPY** PUT 700 2026-11-10 (4DTE): 1,403 traded vs OI 1,349
- **SPY** PUT 737 2026-11-13 (7DTE): 558 traded vs OI 551
- **SPY** PUT 738 2026-11-12 (6DTE): 530 traded vs OI 159
- **SPY** CALL 765 2026-11-13 (7DTE): 2,147 traded vs OI 2,132
- **SPY** CALL 742 2026-11-20 (14DTE): 555 traded vs OI 142
- **QQQ** PUT 627 2026-11-09 (3DTE): 521 traded vs OI 0
- **QQQ** CALL 685 2026-11-10 (4DTE): 504 traded vs OI 496
- **QQQ** CALL 661 2026-11-10 (4DTE): 500 traded vs OI 0
- **QQQ** PUT 628 2026-11-09 (3DTE): 518 traded vs OI 0
- **QQQ** PUT 658 2026-11-10 (4DTE): 504 traded vs OI 57
- **QQQ** CALL 714 2026-11-09 (3DTE): 521 traded vs OI 269
- **QQQ** PUT 655 2026-11-12 (6DTE): 506 traded vs OI 451

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
