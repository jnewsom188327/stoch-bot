# GEX + FLOW SCAN - Thu Oct 29, 03:05 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (4)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:30 | **IWM** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 10/29 284P | 0.65 | 0.22 | +3% (25m) | **-66%** (done) | +232% | 281.86 |
| 10:00 | **ORCL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 10/30 145C | 0.79 | 0.84 | +18% (37m) | **+6%** (done) | +139% | 143.92 |
| 09:55 | **AAPL** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 10/30 345P | 0.77 | 0.68 | +17% (2m) | **-12%** (done) | +198% | 345 |
| 09:50 | **IWM** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 10/29 283P | 0.50 | 0.18 | +20% (21m) | **-64%** (done) | +159% | 282 |

## 1m RULES on SPY / QQQ - loose (4 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 15:05:08 ET, last candle SPY 15:04, QQQ 15:04 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 14:31 | SPY | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |
| 14:23 | QQQ | 1m FAILED POP | R3 R4 | PUTS | TURNING your way | no contract: 86 puts 0-1DTE > 5 priced 0.40-0.80 > 1 delta 0.15+ > 1 spread ok > 1 liquid  |
| 14:17 | QQQ | 1m FAILED POP | R3 R4 | PUTS | TURNING your way | no contract: 86 puts 0-1DTE > 6 priced 0.40-0.80 > 2 delta 0.15+ > 2 spread ok > 2 liquid  |
| 14:12 | QQQ | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | no contract: 86 puts 0-1DTE > 8 priced 0.40-0.80 > 3 delta 0.15+ > 3 spread ok > 3 liquid  |

## Flow surges NOT fired - price disagreed (2 today, last 5)
- 10:05 HOOD PUTS: price +0.99 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:00 HOOD PUTS: price +0.89 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **MSFT** | 528.91 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 40 | none: 126 calls 0-7DTE > 8 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (8 contracts' greeks worked out here) | POS +$640.6M | 502.43 | 525 | 530 | +$24.5M | +$80k bull / -$335k bear | out (clean 28, ADX 23, RVol 0.7) |
| 2 | **IWM** | 283.30 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 35 | 10/30 282P @ 0.56 (delta 0.31) = est +42% at 282.52 | POS +$477.4M | 282.52 | 284 | 270 | -$1.1M | +$0 bull / -$69k bear | out (clean 26, ADX 31, RVol 0.6) |
| 3 | **AAPL** | 350.18 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 33 | none: 55 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (8 contracts' greeks worked out here) | POS +$697.6M | 341.3 | 350 | 345 | +$3.2M | +$38k bull / -$271k bear | out (clean 29, ADX 14, RVol 0.6) |
| 4 | **ARM** | 227.82 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 33 | none: 18 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (2 contracts' greeks worked out here) | POS +$2.4M | 222.43 | 227.5 | 220 | +$1.5M | - | out (clean 24, ADX 18, RVol 0.8) |
| 5 | **DELL** | 473.00 | - | **-** | 25 | - | NEG -$11.3M | 482.6 | 500 | 460 | +$2.5M | +$93k bull / +$0 bear | out (clean 31, ADX 53, RVol 1.3) |
| 6 | **SMH** | 558.50 | - | **-** | 24 | - | NEG -$101.9M | 563.45 | 560 | 555 | +$2.5M | +$0 bull / -$37k bear | out (clean 27, ADX 30, RVol 0.4) |
| 7 | **MU** | 929.29 | - | **-** | 22 | - | POS +$182.6M | 900.23 | 950 | 900 | +$45.8M | +$4.4M bull / -$690k bear | out (clean 29, ADX 55, RVol 0.2) |
| 8 | **GOOGL** | 283.33 | - | **-** | 21 | - | NEG -$192.9M | - | 300 | 290 | -$6.5M | +$0 bull / -$1.6M bear | out (clean 31, ADX 31, RVol 2.0) |
| 9 | **QQQ** | 713.37 | - | **-** | 19 | - | NEG -$5.6B | 725.57 | 720 | 700 | -$115.8M | +$0 bull / -$38.9M bear | out (clean 26, ADX 26, RVol 0.6) |
| 10 | **SPY** | 767.71 | - | **-** | 18 | - | NEG -$6.1B | 772.37 | 770 | 765 | -$101.2M | +$0 bull / -$560k bear | out (clean 25, ADX 25, RVol 0.6) |
| 11 | **META** | 628.21 | - | **-** | 18 | - | NEG -$33.2M | 630.64 | 650 | 625 | -$12.3M | +$0 bull / -$933k bear | out (clean 27, ADX 26, RVol 0.7) |
| 12 | **NFLX** | 62.09 | - | **-** | 18 | - | NEG -$50.8M | - | 63 | 60 | -$470k | +$0 bull / -$29k bear | out (clean 31, ADX 20, RVol 0.4) |
| 13 | **NVDA** | 212.86 | - | **-** | 17 | - | POS +$159.7M | 211.19 | 215 | 210 | -$1.5M | +$35k bull / -$39k bear | out (clean 24, ADX 30, RVol 0.5) |
| 14 | **AMZN** | 245.56 | - | **-** | 17 | - | POS +$13.2M | 241.82 | 265 | 250 | -$3.9M | +$58k bull / -$3.8M bear | out (clean 31, ADX 22, RVol 1.2) |
| 15 | **ORCL** | 138.16 | - | **-** | 17 | - | POS +$119.9M | - | 135 | 140 | +$561k | +$43k bull / +$0 bear | out (clean 33, ADX 21, RVol 1.3) |
| 16 | **SMCI** | 34.42 | - | **-** | 16 | - | POS +$19.6M | - | 35 | 35 | +$334k | - | out (clean 27, ADX 45, RVol 0.5) |
| 17 | **TSLA** | 405.19 | - | **-** | 15 | - | POS +$507.1M | - | 400 | 400 | -$20.4M | +$29k bull / -$547k bear | out (clean 28, ADX 12, RVol 0.3) |
| 18 | **AMD** | 562.62 | - | **-** | 15 | - | POS +$117.6M | - | 550 | 550 | +$940k | +$230k bull / -$124k bear | out (clean 29, ADX 24, RVol 0.4) |
| 19 | **UBER** | 65.53 | - | **-** | 15 | - | NEG -$29.1M | 67.79 | 67 | 65 | -$166k | - | out (clean 28, ADX 21, RVol 1.0) |
| 20 | **BABA** | 98.92 | - | **-** | 11 | - | NEG -$22.1M | 101.63 | 100 | 100 | -$13k | - | out (clean 29, ADX 35, RVol 1.8) |
| 21 | **COIN** | 158.64 | - | **-** | 9 | - | POS +$2.3M | 155.09 | 170 | 155 | -$131k | - | out (clean 26, ADX 27, RVol 1.3) |
| 22 | **HOOD** | 90.37 | - | **-** | 9 | - | NEG -$28.0M | - | 95 | 90 | -$572k | - | out (clean 29, ADX 36, RVol 0.6) |
| 23 | **CRM** | 229.84 | - | **-** | 9 | - | NEG -$16.3M | 239.89 | 240 | 230 | -$210k | - | out (clean 28, ADX 15, RVol 0.8) |
| 24 | **SHOP** | 166.78 | - | **-** | 9 | - | NEG -$5.1M | 170.64 | 175 | 165 | -$72k | - | out (clean 25, ADX 19, RVol 0.4) |
| 25 | **MSTR** | 141.33 | - | **-** | 6 | - | POS +$25.2M | - | 152.5 | 140 | +$6k | - | out (clean 26, ADX 22, RVol 1.2) |
| 26 | **AVGO** | 344.68 | - | **-** | 4 | - | POS +$25.7M | 340.71 | 350 | 340 | +$1.3M | - | out (clean 28, ADX 12, RVol 0.3) |
| 27 | **PLTR** | 193.93 | - | **-** | 4 | - | POS +$19.7M | 192.15 | 200 | 190 | -$202k | - | out (clean 25, ADX 14, RVol 0.4) |

## Big prints this scan (86)
- **QQQ** PUT 740 2026-10-30 (1DTE): 6,800 @ 27.08 = **+$18.4M** BUY | vol 7,192 / OI 6,764
- **QQQ** PUT 737 2026-10-30 (1DTE): 2,550 @ 25.06 = **+$6.4M** BUY | vol 2,651 / OI 2,539
- **QQQ** PUT 745 2026-10-30 (1DTE): 1,350 @ 32.85 = **+$4.4M** BUY | vol 4,367 / OI 1,306
- **QQQ** PUT 744 2026-10-30 (1DTE): 550 @ 31.86 = **+$1.8M** BUY | vol 557 / OI 586
- **QQQ** PUT 743 2026-10-30 (1DTE): 500 @ 30.85 = **+$1.5M** BUY | vol 507 / OI 475
- **QQQ** PUT 742 2026-10-30 (1DTE): 450 @ 29.93 = **+$1.3M** BUY | vol 454 / OI 411
- **QQQ** PUT 738 2026-10-30 (1DTE): 500 @ 26.00 = **+$1.3M** BUY | vol 534 / OI 499
- **QQQ** PUT 739 2026-10-30 (1DTE): 450 @ 26.85 = **+$1.2M** BUY | vol 451 / OI 414
- **QQQ** PUT 741 2026-10-30 (1DTE): 400 @ 28.97 = **+$1.2M** BUY | vol 411 / OI 370
- **SPY** PUT 783 2026-10-30 (1DTE): 350 @ 16.00 = **+$560k** BUY | vol 384 / OI 340
- **QQQ** CALL 700 2026-10-30 (1DTE): 100 @ 13.39 = **+$134k** SELL | vol 580 / OI 2,340
- **AMZN** PUT 245 2026-10-30 (1DTE): 108 @ 9.70 = **+$105k** BUY | vol 10,941 / OI 3,801
- **AMZN** PUT 245 2026-10-30 (1DTE): 106 @ 9.70 = **+$103k** BUY | vol 10,941 / OI 3,801
- **AMZN** PUT 245 2026-10-30 (1DTE): 100 @ 9.70 = **+$97k** BUY | vol 10,941 / OI 3,801
- **AMZN** PUT 245 2026-10-30 (1DTE): 100 @ 9.70 = **+$97k** BUY | vol 10,941 / OI 3,801

## New unusual volume (traded more than open interest, 500+)
- **QQQ** PUT 740 2026-10-30 (1DTE): 7,192 traded vs OI 6,764
- **QQQ** PUT 738 2026-10-30 (1DTE): 534 traded vs OI 499
- **QQQ** PUT 737 2026-10-30 (1DTE): 2,651 traded vs OI 2,539
- **QQQ** PUT 743 2026-10-30 (1DTE): 507 traded vs OI 475
- **NVDA** PUT 222.5 2026-10-30 (1DTE): 1,872 traded vs OI 1,870
- **TSLA** CALL 442.5 2026-10-30 (1DTE): 1,404 traded vs OI 636
- **META** CALL 660 2026-10-30 (1DTE): 4,777 traded vs OI 4,770
- **AMZN** CALL 257.5 2026-10-30 (1DTE): 2,522 traded vs OI 2,517
- **AMZN** CALL 270 2026-11-04 (6DTE): 651 traded vs OI 0
- **MSFT** CALL 522.5 2026-11-02 (4DTE): 501 traded vs OI 3
- **COIN** CALL 165 2026-11-06 (8DTE): 692 traded vs OI 230
- **MSTR** CALL 146 2026-11-06 (8DTE): 1,255 traded vs OI 406
- **MSTR** CALL 152.5 2026-11-06 (8DTE): 1,145 traded vs OI 1,008

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
