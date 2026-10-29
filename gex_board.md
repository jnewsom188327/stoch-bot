# GEX + FLOW SCAN - Thu Oct 29, 03:35 PM ET
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
Last 1m check 15:32:08 ET, last candle SPY 15:31, QQQ 15:31 | no errors
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
| 1 | **ARM** | 227.09 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 37 | none: 18 puts 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (2 contracts' greeks worked out here) | POS +$2.9M | 221.87 | 227.5 | 220 | +$1.6M | - | out (clean 24, ADX 17, RVol 1.4) |
| 2 | **AAPL** | 350.40 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 35 | none: 55 puts 0-7DTE > 4 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only -1% at the target (needs +20%) (8 contracts' greeks worked out here) | POS +$698.5M | 340.61 | 350 | 345 | +$2.5M | +$0 bull / -$55k bear | out (clean 29, ADX 20, RVol 0.8) |
| 3 | **IWM** | 283.77 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 24 | 10/29 284P @ 0.42 (delta 0.63) = est +75% at 283.24 | POS +$880.5M | 282.64 | 284 | 270 | -$1.8M | - | out (clean 26, ADX 26, RVol 0.6) |
| 4 | **MU** | 932.51 | - | **-** | 23 | - | POS +$205.6M | 899.49 | 950 | 900 | +$46.6M | +$274k bull / -$2.6M bear | out (clean 29, ADX 53, RVol 0.8) |
| 5 | **MSFT** | 528.01 | - | **-** | 21 | - | POS +$622.7M | 502.9 | 525 | 530 | +$25.6M | +$246k bull / +$0 bear | out (clean 27, ADX 19, RVol 1.1) |
| 6 | **GOOGL** | 282.90 | - | **-** | 21 | - | NEG -$193.8M | - | 300 | 290 | -$6.1M | +$0 bull / -$360k bear | out (clean 31, ADX 25, RVol 2.4) |
| 7 | **CRM** | 229.50 | - | **-** | 21 | - | NEG -$17.0M | 240.57 | 240 | 230 | -$226k | +$0 bull / -$28k bear | out (clean 28, ADX 25, RVol 1.3) |
| 8 | **QQQ** | 714.36 | - | **-** | 20 | - | NEG -$5.4B | 725.86 | 720 | 710 | -$147.3M | +$0 bull / -$1.1M bear | out (clean 26, ADX 22, RVol 0.9) |
| 9 | **SPY** | 768.63 | - | **-** | 19 | - | NEG -$5.3B | 772.48 | 770 | 765 | -$118.6M | +$0 bull / -$1.9M bear | out (clean 26, ADX 21, RVol 1.0) |
| 10 | **NFLX** | 62.02 | - | **-** | 19 | - | NEG -$46.1M | 64.02 | 63 | 60 | -$466k | +$25k bull / +$0 bear | out (clean 31, ADX 21, RVol 0.8) |
| 11 | **ORCL** | 137.54 | - | **-** | 17 | - | POS +$117.2M | - | 135 | 140 | +$537k | +$60k bull / +$0 bear | out (clean 33, ADX 17, RVol 1.3) |
| 12 | **NVDA** | 213.27 | - | **-** | 16 | - | POS +$159.5M | 211.48 | 215 | 210 | -$1.3M | +$0 bull / -$88k bear | out (clean 24, ADX 26, RVol 0.7) |
| 13 | **AMD** | 565.52 | - | **-** | 16 | - | POS +$121.0M | - | 550 | 550 | +$9k | +$0 bull / -$950k bear | out (clean 28, ADX 23, RVol 0.9) |
| 14 | **META** | 628.80 | - | **-** | 16 | - | NEG -$34.5M | 630.98 | 650 | 625 | -$13.7M | +$27k bull / -$855k bear | out (clean 27, ADX 18, RVol 0.6) |
| 15 | **AMZN** | 245.34 | - | **-** | 16 | - | POS +$10.5M | 242.12 | 265 | 250 | -$147k | +$1.3M bull / -$1.0M bear | out (clean 31, ADX 18, RVol 1.4) |
| 16 | **SMCI** | 34.40 | - | **-** | 16 | - | POS +$18.6M | - | 35 | 35 | +$340k | - | out (clean 27, ADX 46, RVol 0.5) |
| 17 | **UBER** | 65.64 | - | **-** | 16 | - | NEG -$24.7M | 67.56 | 67 | 65 | -$169k | - | out (clean 28, ADX 21, RVol 1.4) |
| 18 | **TSLA** | 404.29 | - | **-** | 15 | - | POS +$503.9M | - | 400 | 400 | -$18.7M | +$182k bull / +$0 bear | out (clean 28, ADX 12, RVol 0.5) |
| 19 | **SMH** | 560.45 | - | **-** | 13 | - | NEG -$70.5M | 563.31 | 560 | 555 | +$2.5M | - | out (clean 27, ADX 26, RVol 0.7) |
| 20 | **DELL** | 475.41 | - | **-** | 13 | - | NEG -$8.6M | 482.39 | 500 | 460 | +$2.3M | - | out (clean 32, ADX 44, RVol 0.7) |
| 21 | **SHOP** | 166.91 | - | **-** | 10 | - | NEG -$6.0M | 171.03 | 175 | 165 | -$77k | - | out (clean 25, ADX 18, RVol 0.8) |
| 22 | **HOOD** | 91.00 | - | **-** | 9 | - | NEG -$25.9M | - | 95 | 90 | -$796k | - | out (clean 29, ADX 29, RVol 0.9) |
| 23 | **COIN** | 159.54 | - | **-** | 8 | - | POS +$2.9M | 155.16 | 170 | 155 | -$215k | - | out (clean 26, ADX 24, RVol 1.1) |
| 24 | **BABA** | 99.22 | - | **-** | 8 | - | NEG -$21.7M | 101.76 | 100 | 100 | -$27k | - | out (clean 29, ADX 29, RVol 0.9) |
| 25 | **PLTR** | 193.94 | - | **-** | 6 | - | POS +$18.1M | 192.28 | 200 | 190 | -$368k | - | out (clean 25, ADX 17, RVol 1.1) |
| 26 | **MSTR** | 141.78 | - | **-** | 6 | - | POS +$27.1M | - | 152.5 | 140 | -$42k | - | out (clean 26, ADX 18, RVol 1.2) |
| 27 | **AVGO** | 344.14 | - | **-** | 5 | - | POS +$12.7M | 342.36 | 350 | 340 | +$1.4M | - | out (clean 28, ADX 14, RVol 0.8) |

## Big prints this scan (54)
- **AMZN** CALL 255 2026-10-30 (1DTE): 647 @ 5.60 = **+$362k** SELL | vol 11,032 / OI 12,075
- **SPY** CALL 760 2026-10-30 (1DTE): 400 @ 8.19 = **+$328k** SELL | vol 2,095 / OI 6,380
- **SPY** PUT 775 2026-11-02 (4DTE): 256 @ 8.00 = **+$205k** BUY | vol 28,098 / OI 149
- **GOOGL** CALL 285 2026-10-30 (1DTE): 757 @ 2.16 = **+$164k** SELL | vol 48,536 / OI 198
- **SPY** CALL 760 2026-10-30 (1DTE): 200 @ 8.08 = **+$162k** SELL | vol 2,095 / OI 6,380
- **SPY** PUT 775 2026-11-02 (4DTE): 200 @ 8.00 = **+$160k** BUY | vol 28,098 / OI 149
- **SPY** PUT 775 2026-11-02 (4DTE): 200 @ 8.00 = **+$160k** BUY | vol 28,098 / OI 149
- **SPY** PUT 775 2026-11-02 (4DTE): 166 @ 8.00 = **+$133k** BUY | vol 28,098 / OI 149
- **QQQ** PUT 710 2026-10-30 (1DTE): 500 @ 2.58 = **+$129k** BUY | vol 50,033 / OI 25,987
- **QQQ** PUT 710 2026-10-30 (1DTE): 490 @ 2.58 = **+$126k** BUY | vol 50,033 / OI 25,987
- **SPY** PUT 775 2026-11-02 (4DTE): 132 @ 8.00 = **+$106k** BUY | vol 28,098 / OI 149
- **MU** PUT 930 2026-10-30 (1DTE): 56 @ 14.98 = **+$84k** BUY | vol 10,911 / OI 2,191
- **MU** PUT 920 2026-10-30 (1DTE): 69 @ 10.30 = **+$71k** BUY | vol 6,283 / OI 962
- **GOOGL** CALL 285 2026-10-30 (1DTE): 315 @ 2.16 = **+$68k** SELL | vol 48,536 / OI 198
- **META** CALL 625 2026-10-30 (1DTE): 87 @ 7.30 = **+$64k** SELL | vol 21,824 / OI 1,463

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 730 2026-11-02 (4DTE): 1,405 traded vs OI 465
- **SPY** PUT 754 2026-11-04 (6DTE): 519 traded vs OI 150
- **SPY** PUT 740 2026-11-27 (29DTE): 1,314 traded vs OI 1,312
- **QQQ** PUT 739 2026-10-30 (1DTE): 1,066 traded vs OI 414
- **QQQ** PUT 742 2026-10-30 (1DTE): 1,069 traded vs OI 411
- **QQQ** PUT 736 2026-10-30 (1DTE): 1,228 traded vs OI 804
- **QQQ** CALL 733 2026-11-02 (4DTE): 502 traded vs OI 293
- **QQQ** PUT 744 2026-10-30 (1DTE): 1,353 traded vs OI 586
- **QQQ** PUT 741 2026-10-30 (1DTE): 936 traded vs OI 370
- **QQQ** PUT 755 2026-11-06 (8DTE): 818 traded vs OI 538
- **QQQ** PUT 767 2026-11-13 (15DTE): 803 traded vs OI 302
- **QQQ** PUT 775 2026-11-20 (22DTE): 617 traded vs OI 245
- **QQQ** PUT 761 2026-11-06 (8DTE): 500 traded vs OI 201
- **IWM** CALL 287.5 2026-10-30 (1DTE): 2,225 traded vs OI 2,206
- **NVDA** PUT 200 2026-11-02 (4DTE): 3,705 traded vs OI 2,822

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
