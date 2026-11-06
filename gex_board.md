# GEX + FLOW SCAN - Fri Nov 06, 12:00 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (3)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:30 | **NVDA** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/06 192.5C | 0.73 | 0.28 | +12% (20m) | **-62%** (done) | +199% | 193.9 |
| 10:00 | **NVDA** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/06 197.5C | 0.67 | 0.03 | -6% (1m) | **-96%** (done) | +24% | 195 |
| 09:50 | **NFLX** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/06 64C | 0.40 | 0.36 | +32% (4m) | **-10%** (done) | +164% | 65 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 12:00:08 ET, last candle SPY 11:59, QQQ 11:59 | no errors

## Flow surges NOT fired - price disagreed (6 today, last 5)
- 09:55 SMCI PUTS: price +0.09 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 HOOD PUTS: price +3.27 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 MSTR PUTS: price +3.75 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 SMCI PUTS: price +0.89 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 PLTR PUTS: price +5.57 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **AAPL** | 344.24 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 36 | none: 112 calls 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (55 contracts' greeks worked out here) | POS +$328k | 344.15 | 350 | 345 | -$17.0M | +$197k bull / +$0 bear | out (clean 29, ADX 10, RVol 0.4) |
| 2 | **TSLA** | 361.53 | - | **-** | 24 | - | NEG -$296.0M | - | 370 | 360 | -$73.2M | +$381k bull / -$174k bear | out (clean 35, ADX 38, RVol 0.7) |
| 3 | **MSTR** | 128.48 | - | **-** | 21 | - | POS +$9.8M | 127.75 | 135 | 125 | -$8.0M | +$0 bull / -$730k bear | out (clean 30, ADX 12, RVol 0.5) |
| 4 | **DELL** | 335.04 | - | **-** | 20 | - | NEG -$28.7M | - | 340 | 335 | +$4.4M | +$46k bull / +$0 bear | out (clean 32, ADX 10, RVol 0.5) |
| 5 | **META** | 621.47 | - | **-** | 19 | - | NEG -$66.0M | 623.97 | 650 | 625 | -$8.2M | +$338k bull / -$85k bear | out (clean 33, ADX 30, RVol 0.5) |
| 6 | **CRM** | 216.12 | - | **-** | 19 | - | NEG -$24.3M | - | 230 | 220 | -$434k | +$0 bull / -$29k bear | out (clean 35, ADX 22, RVol 0.3) |
| 7 | **IWM** | 274.10 | - | **-** | 18 | - | NEG -$3.3B | 285.67 | 275 | 270 | -$6.1M | +$0 bull / -$89k bear | out (clean 34, ADX 23, RVol 0.5) |
| 8 | **SMH** | 465.18 | - | **-** | 18 | - | NEG -$587.9M | - | 505 | 470 | +$6.7M | +$186k bull / -$47k bear | out (clean 34, ADX 13, RVol 0.5) |
| 9 | **PLTR** | 161.62 | - | **-** | 18 | - | NEG -$73.3M | - | 165 | 160 | +$3.0M | +$214k bull / +$0 bear | out (clean 28, ADX 24, RVol 0.4) |
| 10 | **SPY** | 740.47 | - | **-** | 16 | - | NEG -$15.1B | 769.43 | 760 | 740 | -$63.0M | +$997k bull / -$739k bear | out (clean 34, ADX 14, RVol 0.8) |
| 11 | **NVDA** | 188.53 | - | **-** | 16 | - | NEG -$402.0M | - | 200 | 190 | +$22.8M | +$1.7M bull / +$0 bear | out (clean 34, ADX 12, RVol 0.7) |
| 12 | **AMD** | 445.14 | - | **-** | 16 | - | NEG -$175.8M | - | 430 | 450 | +$9.2M | +$655k bull / -$370k bear | out (clean 33, ADX 18, RVol 0.7) |
| 13 | **AMZN** | 263.36 | - | **-** | 16 | - | POS +$380.6M | - | 265 | 265 | -$2.2M | +$112k bull / +$0 bear | out (clean 34, ADX 22, RVol 0.4) |
| 14 | **MSFT** | 535.99 | - | **-** | 16 | - | POS +$714.1M | 512.05 | 540 | 540 | +$2.4M | +$871k bull / -$46k bear | out (clean 33, ADX 15, RVol 0.6) |
| 15 | **MU** | 697.52 | - | **-** | 16 | - | NEG -$204.3M | - | 700 | 700 | +$58.4M | +$2.7M bull / -$2.4M bear | out (clean 32, ADX 11, RVol 0.6) |
| 16 | **HOOD** | 80.18 | - | **-** | 16 | - | NEG -$23.4M | 84 | 85 | 80 | +$1.8M | +$0 bull / -$28k bear | out (clean 30, ADX 18, RVol 0.3) |
| 17 | **QQQ** | 660.81 | - | **-** | 15 | - | NEG -$6.0B | - | 700 | 680 | +$26.3M | +$2.0M bull / -$225k bear | out (clean 35, ADX 17, RVol 0.5) |
| 18 | **GOOGL** | 287.17 | - | **-** | 15 | - | POS +$84.1M | 283.08 | 290 | 290 | +$1.1M | +$42k bull / +$0 bear | out (clean 34, ADX 14, RVol 0.6) |
| 19 | **AVGO** | 296.74 | - | **-** | 15 | - | NEG -$147.9M | - | 325 | 300 | +$1.8M | +$192k bull / +$0 bear | out (clean 31, ADX 10, RVol 0.8) |
| 20 | **ORCL** | 116.77 | - | **-** | 14 | - | NEG -$80.2M | - | 125 | 115 | +$477k | +$158k bull / +$0 bear | out (clean 30, ADX 8, RVol 0.4) |
| 21 | **COIN** | 134.06 | - | **-** | 12 | - | NEG -$21.2M | 137.02 | 141 | 135 | -$3.6M | - | out (clean 31, ADX 19, RVol 0.3) |
| 22 | **SHOP** | 150.94 | - | **-** | 11 | - | NEG -$1.8M | 151.97 | 150 | 150 | -$87k | - | out (clean 36, ADX 36, RVol 0.7) |
| 23 | **BABA** | 109.36 | - | **-** | 9 | - | POS +$26.8M | 106.45 | 110 | 110 | -$532k | - | out (clean 34, ADX 22, RVol 0.6) |
| 24 | **SMCI** | 28.55 | - | **-** | 7 | - | NEG -$3.6M | 29.65 | 30 | 29 | +$313k | - | out (clean 34, ADX 18, RVol 0.3) |
| 25 | **ARM** | 173.35 | - | **-** | 7 | - | NEG -$26.0M | - | 190 | 170 | -$452k | - | out (clean 25, ADX 13, RVol 0.5) |
| 26 | **NFLX** | 64.22 | - | **-** | 6 | - | POS +$17.9M | 63.8 | 64 | 64 | -$304k | - | out (clean 32, ADX 11, RVol 0.6) |
| 27 | **UBER** | 69.73 | - | **-** | 5 | - | POS +$16.8M | 68.83 | 70 | 70 | +$92k | - | out (clean 30, ADX 7, RVol 0.5) |

## Big prints this scan (80)
- **SPY** PUT 735 2026-11-13 (7DTE): 604 @ 6.62 = **+$400k** SELL | vol 10,858 / OI 3,260
- **MU** CALL 670 2026-11-06 (0DTE): 100 @ 27.30 = **+$273k** SELL | vol 884 / OI 0
- **QQQ** PUT 661 2026-11-06 (0DTE): 800 @ 2.90 = **+$232k** SELL | vol 53,951 / OI 371
- **MU** PUT 695 2026-11-06 (0DTE): 300 @ 7.55 = **+$226k** BUY | vol 15,006 / OI 0
- **QQQ** PUT 660 2026-11-10 (4DTE): 250 @ 8.31 = **+$208k** SELL | vol 3,551 / OI 511
- **MU** PUT 705 2026-11-06 (0DTE): 142 @ 14.00 = **+$199k** BUY | vol 6,220 / OI 0
- **MU** PUT 705 2026-11-06 (0DTE): 132 @ 13.80 = **+$182k** BUY | vol 6,220 / OI 0
- **QQQ** CALL 665 2026-11-10 (4DTE): 250 @ 7.14 = **+$178k** BUY | vol 1,816 / OI 37
- **SPY** PUT 765 2026-11-06 (0DTE): 70 @ 25.20 = **+$176k** MID | vol 550 / OI 12,575
- **QQQ** PUT 680 2026-11-13 (7DTE): 70 @ 23.45 = **+$164k** MID | vol 555 / OI 10,074
- **QQQ** PUT 663 2026-11-06 (0DTE): 440 @ 3.63 = **+$160k** SELL | vol 21,004 / OI 190
- **QQQ** PUT 671 2026-11-06 (0DTE): 150 @ 10.31 = **+$155k** SELL | vol 817 / OI 299
- **MSTR** PUT 123 2026-11-13 (7DTE): 375 @ 4.08 = **+$153k** BUY | vol 1,985 / OI 329
- **META** CALL 592.5 2026-11-06 (0DTE): 50 @ 29.23 = **+$146k** BUY | vol 120 / OI 23
- **MU** PUT 672.5 2026-11-13 (7DTE): 58 @ 24.80 = **+$144k** SELL | vol 106 / OI 0

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 791 2026-11-12 (6DTE): 931 traded vs OI 72
- **SPY** CALL 786 2026-11-11 (5DTE): 593 traded vs OI 90
- **SPY** CALL 769 2026-11-06 (0DTE): 7,924 traded vs OI 7,905
- **QQQ** CALL 725 2026-11-13 (7DTE): 530 traded vs OI 0
- **IWM** PUT 268 2026-11-27 (21DTE): 756 traded vs OI 564
- **NVDA** PUT 205 2026-11-09 (3DTE): 799 traded vs OI 752
- **TSLA** CALL 397.5 2026-11-13 (7DTE): 514 traded vs OI 0
- **TSLA** CALL 395 2026-11-27 (21DTE): 530 traded vs OI 0
- **TSLA** PUT 357.5 2026-11-13 (7DTE): 739 traded vs OI 737
- **TSLA** CALL 397.5 2026-11-06 (0DTE): 806 traded vs OI 0
- **TSLA** CALL 397.5 2026-11-09 (3DTE): 538 traded vs OI 0
- **AMZN** PUT 257.5 2026-11-13 (7DTE): 553 traded vs OI 543
- **AMZN** PUT 240 2026-11-09 (3DTE): 814 traded vs OI 742
- **MSFT** PUT 530 2026-11-09 (3DTE): 509 traded vs OI 405
- **MSTR** PUT 125 2026-11-13 (7DTE): 2,261 traded vs OI 2,229

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
