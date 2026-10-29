# GEX + FLOW SCAN - Thu Oct 29, 10:30 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (4)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:30 | **IWM** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 10/29 284P | 0.65 | 0.63 | -3% (0m) | **-3%** | +232% | 281.86 |
| 10:00 | **ORCL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 10/30 145C | 0.79 | 0.69 | +9% (2m) | **-13%** | +139% | 143.92 |
| 09:55 | **AAPL** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 10/30 345P | 0.77 | 0.60 | +17% (2m) | **-22%** | +198% | 345 |
| 09:50 | **IWM** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 10/29 283P | 0.50 | 0.23 | +20% (21m) | **-54%** | +159% | 282 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:30:08 ET, last candle SPY 10:29, QQQ 10:29 | no errors

## Flow surges NOT fired - price disagreed (2 today, last 5)
- 10:05 HOOD PUTS: price +0.99 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:00 HOOD PUTS: price +0.89 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **MSFT** | 526.09 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 63 | none: 126 puts 0-7DTE > 11 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (3 contracts' greeks worked out here) | POS +$534.1M | 498.9 | 525 | 530 | +$29.3M | +$670k bull / -$355k bear | out (clean 28, ADX 32, RVol 2.8) |
| 2 | **ARM** | 227.75 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 52 | none: 19 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (3 contracts' greeks worked out here) | POS +$2.3M | 224 | 227.5 | 220 | +$1.8M | - | out (clean 27, ADX 24, RVol 2.2) |
| 3 | **IWM** | 284.18 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 46 | 10/29 284P @ 0.65 (delta 0.46) = est +232% at 281.86 | POS +$758.1M | 281.86 | 284 | 270 | -$4.0M | +$494k bull / -$3.0M bear | out (clean 26, ADX 51, RVol 1.4) |
| 4 | **AMZN** | 246.98 | FLOW SURGE | **PUTS** | 46 | none: 60 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (9 contracts' greeks worked out here) | POS +$16.4M | 241.95 | 265 | 250 | -$10.1M | +$0 bull / -$3.1M bear | out (clean 31, ADX 45, RVol 1.8) |
| 5 | **AAPL** | 349.85 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 44 | none: 55 puts 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (9 contracts' greeks worked out here) | POS +$639.9M | 339.88 | 350 | 345 | +$6.0M | +$739k bull / -$392k bear | out (clean 29, ADX 40, RVol 1.2) |
| 6 | **MSTR** | 140.35 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 41 | none: 25 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (6 contracts' greeks worked out here) | POS +$23.0M | - | 152.5 | 140 | -$624k | +$163k bull / +$0 bear | out (clean 26, ADX 17, RVol 1.2) |
| 7 | **ORCL** | 140.24 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 39 | 10/30 145C @ 0.78 (delta 0.22) = est +111% at 143.55 | POS +$112.2M | - | 135 | 140 | +$128k | +$0 bull / -$55k bear | out (clean 32, ADX 36, RVol 1.1) |
| 8 | **MU** | 951.40 | PINNED between the walls (positive gamma) - chop | **-** | 38 | - | POS +$371.4M | - | 950 | 950 | +$16.0M | +$260k bull / -$3.1M bear | out (clean 29, ADX 35, RVol 1.1) |
| 9 | **GOOGL** | 285.69 | - | **-** | 29 | - | NEG -$199.2M | - | 300 | 290 | -$10.2M | +$469k bull / -$2.2M bear | out (clean 33, ADX 51, RVol 5.5) |
| 10 | **META** | 624.41 | - | **-** | 26 | - | NEG -$58.0M | 629.05 | 650 | 625 | -$11.1M | +$490k bull / -$751k bear | out (clean 28, ADX 45, RVol 1.2) |
| 11 | **QQQ** | 715.60 | - | **-** | 23 | - | NEG -$4.6B | 726.69 | 720 | 720 | -$78.4M | +$569k bull / -$2.1M bear | out (clean 28, ADX 25, RVol 1.2) |
| 12 | **UBER** | 65.18 | - | **-** | 23 | - | NEG -$33.0M | 69.02 | 67 | 65 | -$164k | - | out (clean 28, ADX 28, RVol 0.5) |
| 13 | **TSLA** | 405.57 | - | **-** | 22 | - | POS +$498.1M | - | 400 | 400 | -$15.4M | +$0 bull / -$1.3M bear | out (clean 29, ADX 28, RVol 1.1) |
| 14 | **SPY** | 769.38 | - | **-** | 21 | - | NEG -$4.2B | 773.05 | 770 | 765 | -$68.0M | +$330k bull / -$1.3M bear | out (clean 27, ADX 16, RVol 1.0) |
| 15 | **AMD** | 567.26 | - | **-** | 20 | - | POS +$137.2M | - | 600 | 550 | -$2.1M | +$0 bull / -$604k bear | out (clean 29, ADX 37, RVol 0.9) |
| 16 | **NFLX** | 62.04 | - | **-** | 20 | - | NEG -$51.3M | - | 63 | 60 | -$534k | - | out (clean 30, ADX 40, RVol 1.2) |
| 17 | **NVDA** | 213.63 | - | **-** | 19 | - | POS +$212.4M | 210.77 | 215 | 210 | +$1.6M | +$0 bull / -$641k bear | out (clean 25, ADX 30, RVol 1.2) |
| 18 | **DELL** | 488.27 | - | **-** | 19 | - | POS +$14.3M | 476.45 | 500 | 500 | +$598k | +$0 bull / -$84k bear | out (clean 31, ADX 28, RVol 0.8) |
| 19 | **PLTR** | 195.27 | - | **-** | 17 | - | POS +$34.4M | 191.11 | 200 | 190 | -$230k | +$165k bull / +$0 bear | out (clean 26, ADX 14, RVol 2.0) |
| 20 | **SHOP** | 166.90 | - | **-** | 17 | - | NEG -$5.9M | 173.44 | 175 | 165 | -$72k | - | out (clean 26, ADX 15, RVol 0.7) |
| 21 | **BABA** | 99.92 | - | **-** | 17 | - | NEG -$16.4M | 102.25 | 102 | 100 | -$64k | - | out (clean 28, ADX 24, RVol 1.2) |
| 22 | **AVGO** | 341.92 | - | **-** | 16 | - | NEG -$1.7M | 342.09 | 350 | 340 | +$2.6M | - | out (clean 29, ADX 34, RVol 0.6) |
| 23 | **CRM** | 231.60 | - | **-** | 16 | - | NEG -$19.7M | - | 240 | 230 | -$244k | - | out (clean 27, ADX 29, RVol 0.9) |
| 24 | **COIN** | 161.75 | - | **-** | 12 | - | POS +$7.2M | - | 170 | 155 | -$117k | - | out (clean 26, ADX 18, RVol 1.2) |
| 25 | **HOOD** | 91.12 | - | **-** | 11 | - | NEG -$23.7M | - | 95 | 90 | -$1.1M | - | out (clean 28, ADX 13, RVol 1.0) |
| 26 | **SMH** | 560.43 | - | **-** | 9 | - | NEG -$51.3M | 563.69 | 560 | 555 | +$348k | - | out (clean 27, ADX 18, RVol 1.1) |
| 27 | **SMCI** | 35.66 | - | **-** | 8 | - | POS +$27.3M | - | 35 | 35 | +$38k | - | out (clean 27, ADX 25, RVol 0.8) |

## Big prints this scan (139)
- **AMZN** PUT 247.5 2026-11-02 (4DTE): 500 @ 11.55 = **+$578k** BUY | vol 582 / OI 188
- **IWM** CALL 281 2026-10-30 (1DTE): 1,759 @ 3.23 = **+$568k** SELL | vol 5,878 / OI 6,518
- **QQQ** PUT 740 2026-10-30 (1DTE): 100 @ 25.73 = **+$257k** BUY | vol 207 / OI 6,764
- **QQQ** CALL 705 2026-10-30 (1DTE): 162 @ 11.04 = **+$179k** SELL | vol 648 / OI 6,223
- **IWM** PUT 283 2026-10-30 (1DTE): 1,494 @ 1.08 = **+$161k** BUY | vol 11,235 / OI 472
- **IWM** PUT 285 2026-10-30 (1DTE): 756 @ 2.13 = **+$161k** BUY | vol 8,456 / OI 761
- **QQQ** CALL 714 2026-11-04 (6DTE): 159 @ 8.90 = **+$142k** SELL | vol 520 / OI 31
- **IWM** PUT 284 2026-10-30 (1DTE): 862 @ 1.60 = **+$138k** BUY | vol 12,371 / OI 301
- **IWM** PUT 284 2026-10-30 (1DTE): 804 @ 1.54 = **+$124k** BUY | vol 12,371 / OI 301
- **AMZN** PUT 240 2026-10-30 (1DTE): 164 @ 7.36 = **+$121k** BUY | vol 3,472 / OI 8,499
- **AMZN** PUT 240 2026-10-30 (1DTE): 164 @ 7.36 = **+$121k** BUY | vol 3,472 / OI 8,499
- **MSFT** PUT 537.5 2026-10-30 (1DTE): 80 @ 15.00 = **+$120k** BUY | vol 541 / OI 442
- **GOOGL** PUT 285 2026-11-02 (4DTE): 250 @ 4.80 = **+$120k** BUY | vol 1,420 / OI 80
- **IWM** PUT 284 2026-10-30 (1DTE): 786 @ 1.49 = **+$117k** BUY | vol 12,371 / OI 301
- **IWM** PUT 285 2026-10-30 (1DTE): 527 @ 2.14 = **+$113k** BUY | vol 8,456 / OI 761

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 759 2026-10-29 (0DTE): 572 traded vs OI 168
- **SPY** CALL 777 2026-11-03 (5DTE): 514 traded vs OI 169
- **SPY** CALL 774 2026-11-04 (6DTE): 520 traded vs OI 322
- **SPY** PUT 764 2026-10-30 (1DTE): 4,018 traded vs OI 3,855
- **SPY** PUT 766 2026-11-04 (6DTE): 500 traded vs OI 100
- **SPY** PUT 768 2026-11-13 (15DTE): 1,113 traded vs OI 1,102
- **QQQ** PUT 671 2026-10-29 (0DTE): 983 traded vs OI 41
- **QQQ** CALL 717 2026-11-02 (4DTE): 519 traded vs OI 179
- **QQQ** PUT 715 2026-11-04 (6DTE): 3,577 traded vs OI 3,574
- **QQQ** CALL 720 2026-11-05 (7DTE): 513 traded vs OI 324
- **IWM** CALL 290 2026-11-09 (11DTE): 506 traded vs OI 34
- **IWM** PUT 280 2026-10-30 (1DTE): 5,678 traded vs OI 5,244
- **IWM** CALL 287 2026-10-30 (1DTE): 6,062 traded vs OI 5,900
- **IWM** PUT 287 2026-10-29 (0DTE): 512 traded vs OI 0
- **IWM** PUT 281 2026-11-06 (8DTE): 641 traded vs OI 272

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
