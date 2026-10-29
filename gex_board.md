# GEX + FLOW SCAN - Thu Oct 29, 03:25 PM ET
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
Last 1m check 15:25:08 ET, last candle SPY 15:24, QQQ 15:24 | no errors
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
| 1 | **AAPL** | 350.19 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 34 | none: 55 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (7 contracts' greeks worked out here) | POS +$693.0M | 340.58 | 350 | 345 | +$3.0M | +$475k bull / -$87k bear | out (clean 29, ADX 18, RVol 0.8) |
| 2 | **IWM** | 283.40 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 25 | 10/30 282P @ 0.45 (delta 0.28) = est +26% at 282.88 | POS +$951.6M | 281.05 | 284 | 270 | -$1.5M | - | out (clean 26, ADX 29, RVol 0.7) |
| 3 | **SMH** | 558.72 | - | **-** | 24 | - | NEG -$84.9M | 563.41 | 560 | 555 | +$2.5M | +$43k bull / +$0 bear | out (clean 27, ADX 28, RVol 0.6) |
| 4 | **MU** | 929.72 | - | **-** | 23 | - | POS +$195.5M | 900.39 | 950 | 900 | +$48.1M | +$1.1M bull / -$1.4M bear | out (clean 29, ADX 57, RVol 0.6) |
| 5 | **MSFT** | 528.56 | - | **-** | 21 | - | POS +$642.6M | 501.64 | 525 | 530 | +$24.3M | +$219k bull / -$96k bear | out (clean 27, ADX 21, RVol 0.9) |
| 6 | **GOOGL** | 282.95 | - | **-** | 21 | - | NEG -$187.0M | - | 300 | 290 | -$5.9M | +$74k bull / +$0 bear | out (clean 31, ADX 27, RVol 2.1) |
| 7 | **QQQ** | 713.37 | - | **-** | 19 | - | NEG -$5.5B | 725.1 | 720 | 710 | -$112.7M | +$1.5M bull / -$1.2M bear | out (clean 26, ADX 25, RVol 0.8) |
| 8 | **NFLX** | 62.01 | - | **-** | 19 | - | NEG -$46.9M | - | 63 | 60 | -$479k | +$25k bull / +$0 bear | out (clean 31, ADX 20, RVol 0.7) |
| 9 | **SPY** | 767.90 | - | **-** | 18 | - | NEG -$5.8B | 772.36 | 770 | 765 | -$107.4M | +$309k bull / -$645k bear | out (clean 25, ADX 22, RVol 0.6) |
| 10 | **META** | 628.31 | - | **-** | 17 | - | NEG -$36.2M | 631.31 | 650 | 625 | -$12.0M | +$27k bull / -$162k bear | out (clean 27, ADX 21, RVol 0.7) |
| 11 | **ORCL** | 138.46 | - | **-** | 17 | - | POS +$105.9M | - | 135 | 140 | +$432k | +$43k bull / +$0 bear | out (clean 33, ADX 18, RVol 1.6) |
| 12 | **NVDA** | 212.91 | - | **-** | 16 | - | POS +$171.7M | 211.31 | 215 | 210 | -$1.1M | +$96k bull / -$88k bear | out (clean 24, ADX 29, RVol 0.5) |
| 13 | **AMD** | 563.02 | - | **-** | 16 | - | POS +$113.0M | - | 550 | 550 | +$682k | +$160k bull / -$211k bear | out (clean 28, ADX 25, RVol 0.8) |
| 14 | **AMZN** | 244.85 | - | **-** | 16 | - | POS +$8.3M | 242.5 | 265 | 250 | -$1.4M | +$1.2M bull / -$968k bear | out (clean 31, ADX 18, RVol 1.3) |
| 15 | **SMCI** | 34.35 | - | **-** | 16 | - | POS +$20.2M | - | 35 | 35 | +$350k | - | out (clean 27, ADX 49, RVol 0.5) |
| 16 | **TSLA** | 404.65 | - | **-** | 15 | - | POS +$504.4M | - | 400 | 400 | -$19.0M | +$403k bull / -$26k bear | out (clean 28, ADX 11, RVol 0.4) |
| 17 | **AVGO** | 343.89 | - | **-** | 15 | - | POS +$10.7M | 342.8 | 350 | 340 | +$1.5M | +$638k bull / +$0 bear | out (clean 28, ADX 15, RVol 0.7) |
| 18 | **PLTR** | 193.43 | - | **-** | 15 | - | POS +$16.0M | 192.29 | 200 | 190 | -$259k | +$38k bull / +$0 bear | out (clean 25, ADX 18, RVol 0.7) |
| 19 | **UBER** | 65.50 | - | **-** | 15 | - | NEG -$29.5M | 67.81 | 67 | 65 | -$168k | - | out (clean 28, ADX 20, RVol 1.1) |
| 20 | **DELL** | 473.95 | - | **-** | 14 | - | NEG -$9.8M | 482.47 | 500 | 460 | +$2.3M | - | out (clean 32, ADX 50, RVol 0.8) |
| 21 | **ARM** | 226.93 | - | **-** | 14 | - | POS +$3.4M | 221.22 | 227.5 | 220 | +$1.5M | - | out (clean 24, ADX 19, RVol 0.8) |
| 22 | **CRM** | 229.62 | - | **-** | 10 | - | NEG -$16.2M | 239.88 | 240 | 230 | -$198k | - | out (clean 28, ADX 22, RVol 1.1) |
| 23 | **SHOP** | 166.32 | - | **-** | 10 | - | NEG -$5.5M | 170.72 | 175 | 165 | -$73k | - | out (clean 25, ADX 20, RVol 0.8) |
| 24 | **HOOD** | 90.79 | - | **-** | 9 | - | NEG -$25.9M | 96.1 | 95 | 90 | -$738k | - | out (clean 29, ADX 32, RVol 0.8) |
| 25 | **BABA** | 99.11 | - | **-** | 9 | - | NEG -$21.4M | 101.56 | 100 | 100 | -$16k | - | out (clean 29, ADX 33, RVol 1.0) |
| 26 | **COIN** | 159.20 | - | **-** | 8 | - | POS +$2.9M | 154.81 | 170 | 155 | -$170k | - | out (clean 26, ADX 27, RVol 0.9) |
| 27 | **MSTR** | 141.16 | - | **-** | 6 | - | POS +$25.7M | - | 152.5 | 140 | +$109k | - | out (clean 26, ADX 20, RVol 1.3) |

## Big prints this scan (38)
- **QQQ** PUT 715 2026-11-02 (4DTE): 780 @ 6.20 = **+$484k** BUY | vol 8,123 / OI 832
- **AMZN** CALL 247.5 2026-10-30 (1DTE): 479 @ 8.88 = **+$425k** BUY | vol 5,077 / OI 2,330
- **SPY** PUT 775 2026-11-02 (4DTE): 484 @ 7.70 = **+$373k** BUY | vol 27,018 / OI 149
- **SPY** PUT 775 2026-11-02 (4DTE): 186 @ 7.70 = **+$143k** BUY | vol 27,018 / OI 149
- **SPY** PUT 775 2026-11-02 (4DTE): 168 @ 7.70 = **+$129k** BUY | vol 27,018 / OI 149
- **MU** PUT 927.5 2026-10-30 (1DTE): 80 @ 13.20 = **+$106k** BUY | vol 2,952 / OI 120
- **MU** PUT 920 2026-11-02 (4DTE): 60 @ 14.90 = **+$89k** BUY | vol 1,006 / OI 123
- **MSFT** PUT 525 2026-10-30 (1DTE): 292 @ 2.50 = **+$73k** SELL | vol 14,245 / OI 1,940
- **MSFT** CALL 535 2026-10-30 (1DTE): 266 @ 2.20 = **+$59k** BUY | vol 25,366 / OI 2,646
- **MU** CALL 950 2026-10-30 (1DTE): 77 @ 6.05 = **+$47k** SELL | vol 23,296 / OI 12,588
- **MSFT** CALL 527.5 2026-11-04 (6DTE): 50 @ 8.75 = **+$44k** BUY | vol 1,248 / OI 43
- **AMZN** CALL 245 2026-11-02 (4DTE): 40 @ 10.85 = **+$43k** BUY | vol 1,199 / OI 316
- **AMD** CALL 562.5 2026-10-30 (1DTE): 48 @ 8.90 = **+$43k** SELL | vol 1,313 / OI 597
- **AMD** CALL 560 2026-11-02 (4DTE): 32 @ 13.00 = **+$42k** SELL | vol 269 / OI 188
- **AMZN** CALL 245 2026-10-30 (1DTE): 40 @ 10.09 = **+$40k** BUY | vol 9,404 / OI 2,504

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 726 2026-11-02 (4DTE): 2,003 traded vs OI 132
- **SPY** PUT 715 2026-11-05 (7DTE): 650 traded vs OI 186
- **QQQ** CALL 706 2026-10-29 (0DTE): 515 traded vs OI 222
- **QQQ** CALL 730 2026-11-05 (7DTE): 557 traded vs OI 384
- **NVDA** PUT 192.5 2026-11-06 (8DTE): 1,008 traded vs OI 1,007
- **AMD** CALL 572.5 2026-11-02 (4DTE): 501 traded vs OI 68
- **AMZN** PUT 230 2026-11-06 (8DTE): 1,987 traded vs OI 1,967
- **NFLX** CALL 63 2026-11-13 (15DTE): 516 traded vs OI 425
- **COIN** CALL 175 2026-10-30 (1DTE): 1,892 traded vs OI 0
- **COIN** CALL 175 2026-11-06 (8DTE): 746 traded vs OI 0
- **MU** PUT 865 2026-11-02 (4DTE): 538 traded vs OI 111

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
