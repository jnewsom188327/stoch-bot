# GEX + FLOW SCAN - Thu Oct 29, 01:30 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (4)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:30 | **IWM** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 10/29 284P | 0.65 | 0.22 | +3% (25m) | **-66%** (done) | +232% | 281.86 |
| 10:00 | **ORCL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 10/30 145C | 0.79 | 0.84 | +18% (37m) | **+6%** (done) | +139% | 143.92 |
| 09:55 | **AAPL** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 10/30 345P | 0.77 | 0.68 | +17% (2m) | **-12%** (done) | +198% | 345 |
| 09:50 | **IWM** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 10/29 283P | 0.50 | 0.18 | +20% (21m) | **-64%** (done) | +159% | 282 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 13:30:08 ET, last candle SPY 13:29, QQQ 13:29 | no errors

## Flow surges NOT fired - price disagreed (2 today, last 5)
- 10:05 HOOD PUTS: price +0.99 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:00 HOOD PUTS: price +0.89 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **MSFT** | 525.50 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 38 | none: 126 puts 0-7DTE > 9 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (11 contracts' greeks worked out here) | POS +$552.5M | 503.21 | 525 | 530 | +$27.1M | +$322k bull / -$59k bear | out (clean 28, ADX 9, RVol 0.5) |
| 2 | **DELL** | 480.54 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 38 | none: 39 calls 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (3 contracts' greeks worked out here) | POS +$1.6M | 479.05 | 500 | 480 | +$1.1M | +$151k bull / +$0 bear | out (clean 29, ADX 39, RVol 0.5) |
| 3 | **ARM** | 230.02 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 36 | none: 19 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (2 contracts' greeks worked out here) | POS +$3.2M | 221.88 | 227.5 | 230 | +$1.5M | - | out (clean 24, ADX 12, RVol 1.2) |
| 4 | **IWM** | 284.07 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 34 | 10/29 284P @ 0.40 (delta 0.47) = est +224% at 282.7 | POS +$846.4M | 282.7 | 284 | 270 | -$1.4M | +$58k bull / +$0 bear | out (clean 25, ADX 21, RVol 0.6) |
| 5 | **META** | 629.33 | FLIP CROSS down into negative gamma | **PUTS** | 34 | none: 147 puts 0-7DTE > 9 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (8 contracts' greeks worked out here) | NEG -$10.1M | 629.8 | 650 | 625 | -$13.8M | +$579k bull / +$0 bear | out (clean 27, ADX 36, RVol 0.7) |
| 6 | **AAPL** | 349.77 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 33 | none: 55 puts 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (9 contracts' greeks worked out here) | POS +$657.1M | 340.61 | 350 | 345 | +$3.2M | +$0 bull / -$31k bear | out (clean 29, ADX 22, RVol 0.4) |
| 7 | **SMCI** | 35.02 | PINNED between the walls (positive gamma) - chop | **-** | 23 | - | POS +$24.2M | - | 35 | 35 | +$229k | - | out (clean 26, ADX 21, RVol 0.5) |
| 8 | **GOOGL** | 283.36 | - | **-** | 22 | - | NEG -$193.1M | - | 300 | 290 | -$9.0M | +$227k bull / +$0 bear | out (clean 32, ADX 37, RVol 1.2) |
| 9 | **MU** | 938.74 | - | **-** | 20 | - | POS +$293.3M | 882.81 | 950 | 900 | +$27.7M | +$4.7M bull / -$445k bear | out (clean 27, ADX 36, RVol 0.3) |
| 10 | **SPY** | 768.55 | - | **-** | 17 | - | NEG -$5.2B | 772.48 | 770 | 765 | -$112.9M | +$1.8M bull / +$0 bear | out (clean 25, ADX 12, RVol 0.5) |
| 11 | **TSLA** | 404.81 | - | **-** | 17 | - | POS +$503.1M | - | 400 | 400 | -$19.8M | +$252k bull / -$662k bear | out (clean 28, ADX 18, RVol 0.3) |
| 12 | **AMZN** | 246.11 | - | **-** | 17 | - | POS +$12.9M | 242.13 | 265 | 250 | -$6.3M | +$4.3M bull / -$907k bear | out (clean 32, ADX 21, RVol 0.7) |
| 13 | **QQQ** | 714.66 | - | **-** | 16 | - | NEG -$5.4B | 726.4 | 720 | 700 | -$65.9M | +$452k bull / -$364k bear | out (clean 26, ADX 16, RVol 0.5) |
| 14 | **SMH** | 561.29 | - | **-** | 16 | - | NEG -$56.7M | 563.21 | 560 | 555 | +$604k | +$166k bull / +$0 bear | out (clean 26, ADX 14, RVol 0.3) |
| 15 | **NVDA** | 213.53 | - | **-** | 15 | - | POS +$201.6M | 211.13 | 215 | 210 | -$6.8M | +$51k bull / -$33k bear | out (clean 24, ADX 16, RVol 0.4) |
| 16 | **AMD** | 567.59 | - | **-** | 15 | - | POS +$144.5M | - | 600 | 550 | -$3.6M | +$555k bull / +$0 bear | out (clean 28, ADX 17, RVol 0.4) |
| 17 | **UBER** | 65.38 | - | **-** | 13 | - | NEG -$30.3M | 67.77 | 67 | 65 | -$168k | - | out (clean 27, ADX 10, RVol 0.4) |
| 18 | **NFLX** | 61.86 | - | **-** | 11 | - | NEG -$53.0M | - | 63 | 60 | -$477k | - | out (clean 31, ADX 23, RVol 1.0) |
| 19 | **ORCL** | 137.87 | - | **-** | 9 | - | POS +$122.0M | - | 135 | 140 | +$770k | - | out (clean 32, ADX 37, RVol 0.4) |
| 20 | **CRM** | 231.13 | - | **-** | 9 | - | NEG -$20.1M | - | 240 | 230 | -$228k | - | out (clean 27, ADX 13, RVol 0.6) |
| 21 | **COIN** | 161.49 | - | **-** | 7 | - | POS +$6.8M | - | 170 | 155 | -$236k | - | out (clean 26, ADX 10, RVol 1.2) |
| 22 | **BABA** | 99.47 | - | **-** | 7 | - | NEG -$18.4M | 101.7 | 100 | 100 | -$25k | - | out (clean 29, ADX 26, RVol 0.4) |
| 23 | **AVGO** | 345.46 | - | **-** | 6 | - | POS +$32.0M | 340.96 | 350 | 340 | +$1.7M | - | out (clean 27, ADX 13, RVol 0.4) |
| 24 | **SHOP** | 167.18 | - | **-** | 6 | - | NEG -$5.8M | 172.51 | 175 | 165 | -$32k | - | out (clean 25, ADX 10, RVol 0.5) |
| 25 | **HOOD** | 91.39 | - | **-** | 5 | - | NEG -$23.7M | 96.76 | 95 | 90 | -$553k | - | out (clean 27, ADX 11, RVol 0.5) |
| 26 | **PLTR** | 194.02 | - | **-** | 4 | - | POS +$20.2M | 192.07 | 200 | 190 | -$287k | - | out (clean 25, ADX 16, RVol 0.4) |
| 27 | **MSTR** | 142.67 | - | **-** | 4 | - | POS +$31.3M | - | 152.5 | 140 | -$407k | - | out (clean 25, ADX 13, RVol 0.7) |

## Big prints this scan (58)
- **SPY** PUT 775 2026-11-02 (4DTE): 999 @ 6.93 = **+$692k** SELL | vol 25,997 / OI 149
- **MU** CALL 900 2026-10-30 (1DTE): 100 @ 42.45 = **+$424k** BUY | vol 2,047 / OI 2,922
- **MU** PUT 935 2026-10-30 (1DTE): 300 @ 11.90 = **+$357k** SELL | vol 5,496 / OI 1,035
- **MU** PUT 935 2026-10-30 (1DTE): 248 @ 11.80 = **+$293k** SELL | vol 5,496 / OI 1,035
- **META** PUT 632.5 2026-10-30 (1DTE): 400 @ 7.00 = **+$280k** SELL | vol 2,485 / OI 567
- **TSLA** PUT 407.5 2026-10-30 (1DTE): 450 @ 5.50 = **+$248k** BUY | vol 8,246 / OI 835
- **SPY** PUT 775 2026-11-02 (4DTE): 328 @ 7.22 = **+$237k** MID | vol 25,997 / OI 149
- **SPY** PUT 775 2026-11-02 (4DTE): 328 @ 7.22 = **+$237k** MID | vol 25,997 / OI 149
- **AMZN** PUT 245 2026-10-30 (1DTE): 250 @ 9.40 = **+$235k** BUY | vol 7,203 / OI 3,801
- **AMZN** CALL 240 2026-10-30 (1DTE): 158 @ 12.94 = **+$204k** SELL | vol 3,222 / OI 742
- **QQQ** CALL 711 2026-11-04 (6DTE): 200 @ 9.71 = **+$194k** SELL | vol 421 / OI 19
- **QQQ** PUT 712 2026-10-29 (0DTE): 1,419 @ 1.20 = **+$170k** BUY | vol 149,092 / OI 1,739
- **TSLA** PUT 405 2026-10-30 (1DTE): 441 @ 3.80 = **+$168k** BUY | vol 34,137 / OI 2,059
- **AMD** CALL 540 2026-10-30 (1DTE): 49 @ 29.20 = **+$143k** BUY | vol 216 / OI 4,559
- **SPY** PUT 775 2026-11-02 (4DTE): 190 @ 7.22 = **+$137k** MID | vol 25,997 / OI 149

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 772 2026-11-06 (8DTE): 1,019 traded vs OI 894
- **QQQ** CALL 718 2026-11-04 (6DTE): 531 traded vs OI 73
- **QQQ** PUT 726 2026-10-29 (0DTE): 513 traded vs OI 278
- **QQQ** CALL 730 2026-11-02 (4DTE): 2,306 traded vs OI 2,289
- **QQQ** CALL 710 2026-11-10 (12DTE): 529 traded vs OI 159
- **SMH** PUT 557.5 2026-11-20 (22DTE): 1,024 traded vs OI 577
- **AMD** CALL 587.5 2026-10-30 (1DTE): 760 traded vs OI 744
- **META** CALL 632.5 2026-11-02 (4DTE): 506 traded vs OI 50
- **MSFT** CALL 562.5 2026-10-30 (1DTE): 1,835 traded vs OI 1,101
- **AVGO** CALL 355 2026-11-02 (4DTE): 710 traded vs OI 707
- **MSTR** CALL 140 2026-10-30 (1DTE): 1,727 traded vs OI 1,673
- **ORCL** PUT 136 2026-11-06 (8DTE): 500 traded vs OI 229

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
