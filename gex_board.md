# GEX + FLOW SCAN - Mon Nov 02, 12:50 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (2)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 12:03 | **QQQ** | **PUTS** | 1m FAILED POP (R3) | 11/02 691P | 0.65 | 1.81 | +291% (43m) | **+178%** | +11% | 692.76 hit |
| 11:37 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/02 691P | 0.71 | 1.27 | +111% (58m) | **+79%** (done) | +12% | 693.07 hit |

## 1m RULES on SPY / QQQ - loose (4 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 12:50:08 ET, last candle SPY 12:49, QQQ 12:49 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 12:02 | QQQ | 1m FAILED POP | R3 | PUTS | TURNING away | **FIRE** QQQ261102P00691000 |
| 11:54 | SPY | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | no contract: 90 puts 0-1DTE > 5 priced 0.40-0.80 > 3 delta 0.15+ > 3 spread ok > 3 liquid  |
| 11:36 | QQQ | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | **FIRE** QQQ261102P00691000 |
| 11:36 | SPY | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | no contract: 90 puts 0-1DTE > 5 priced 0.40-0.80 > 3 delta 0.15+ > 3 spread ok > 3 liquid  |

## Flow surges NOT fired - price disagreed (5 today, last 5)
- 10:35 SPY PUTS: price +0.32 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:25 SPY PUTS: price +2.69 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:10 BABA PUTS: over EMA 20 - flow says one way, price says the other
- 10:05 BABA PUTS: over EMA 20 - flow says one way, price says the other
- 09:50 BABA PUTS: price +0.75 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **MU** | 848.24 | FLOW SURGE | **CALLS** | 44 | none: 138 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (57 contracts' greeks worked out here) | NEG -$212.9M | - | 910 | 850 | +$131.0M | +$5.2M bull / +$0 bear | out (clean 31, ADX 38, RVol 1.1) |
| 2 | **BABA** | 102.78 | TREND + FLOW | **PUTS** | 42 | none: 21 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$2.7M | 100.73 | 105 | 100 | -$1000k | - | SHORT (clean 33, ADX 29, RVol 1.6) |
| 3 | **AMZN** | 250.49 | PINNED between the walls (positive gamma) - chop | **-** | 35 | - | POS +$99.1M | 241.83 | 250 | 250 | -$21.5M | +$80k bull / -$94k bear | out (clean 33, ADX 31, RVol 0.6) |
| 4 | **MSFT** | 520.57 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 35 | none: 168 calls 0-7DTE > 10 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (80 contracts' greeks worked out here) | POS +$243.3M | 501.24 | 540 | 520 | -$1.3M | +$0 bull / -$243k bear | out (clean 27, ADX 29, RVol 0.5) |
| 5 | **SMCI** | 31.51 | TREND (flow not with it) | **PUTS** | 32 | none: 13 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$337k | - | 34 | 30 | +$430k | - | SHORT (clean 33, ADX 37, RVol 1.1) |
| 6 | **SHOP** | 159.90 | - | **-** | 29 | - | NEG -$241k | - | 175 | 175 | -$752k | +$58k bull / +$0 bear | out (clean 28, ADX 22, RVol 0.9) |
| 7 | **AMD** | 482.17 | - | **-** | 26 | - | NEG -$80.8M | - | 500 | 480 | +$34.1M | +$2.6M bull / +$0 bear | out (clean 31, ADX 35, RVol 1.1) |
| 8 | **SMH** | 518.57 | - | **-** | 24 | - | NEG -$342.6M | - | 532.5 | 500 | +$3.7M | +$189k bull / +$0 bear | out (clean 31, ADX 22, RVol 1.1) |
| 9 | **AAPL** | 338.20 | - | **-** | 24 | - | POS +$22.7M | 336.76 | 350 | 330 | +$16.1M | +$492k bull / -$1.5M bear | out (clean 31, ADX 33, RVol 1.0) |
| 10 | **MSTR** | 132.96 | - | **-** | 21 | - | POS +$2.3M | - | 135 | 125 | +$3.6M | +$508k bull / -$27k bear | out (clean 26, ADX 24, RVol 0.8) |
| 11 | **META** | 611.13 | - | **-** | 20 | - | NEG -$125.7M | 622.71 | 650 | 610 | +$10.8M | +$0 bull / -$385k bear | out (clean 29, ADX 28, RVol 0.6) |
| 12 | **TSLA** | 407.80 | - | **-** | 19 | - | POS +$299.6M | - | 410 | 400 | -$63.3M | +$1.2M bull / +$0 bear | out (clean 30, ADX 26, RVol 0.5) |
| 13 | **AVGO** | 328.68 | - | **-** | 19 | - | NEG -$100.2M | - | 340 | 330 | -$4.8M | +$392k bull / +$0 bear | out (clean 30, ADX 23, RVol 0.3) |
| 14 | **QQQ** | 690.81 | - | **-** | 18 | - | NEG -$5.6B | - | 720 | 680 | +$73.3M | +$7.9M bull / +$0 bear | out (clean 30, ADX 23, RVol 0.4) |
| 15 | **SPY** | 757.71 | - | **-** | 17 | - | NEG -$10.0B | 774.42 | 800 | 750 | +$46.2M | +$845k bull / +$0 bear | out (clean 29, ADX 24, RVol 0.7) |
| 16 | **NVDA** | 206.12 | - | **-** | 17 | - | NEG -$195.6M | 213.68 | 210 | 205 | +$9.9M | +$284k bull / +$0 bear | out (clean 29, ADX 17, RVol 0.8) |
| 17 | **NFLX** | 62.60 | - | **-** | 17 | - | NEG -$19.7M | - | 63 | 60 | -$220k | +$0 bull / -$26k bear | out (clean 28, ADX 25, RVol 0.5) |
| 18 | **PLTR** | 184.19 | - | **-** | 17 | - | NEG -$11.0M | - | 200 | 180 | +$2.6M | +$84k bull / +$0 bear | out (clean 25, ADX 13, RVol 0.5) |
| 19 | **ORCL** | 121.98 | - | **-** | 17 | - | NEG -$37.8M | - | 130 | 120 | -$176k | +$84k bull / +$0 bear | out (clean 31, ADX 33, RVol 0.6) |
| 20 | **GOOGL** | 282.60 | - | **-** | 16 | - | NEG -$70.4M | - | 285 | 290 | +$2.4M | +$28k bull / -$104k bear | out (clean 34, ADX 18, RVol 0.4) |
| 21 | **DELL** | 406.11 | - | **-** | 16 | - | NEG -$21.2M | - | 440 | 400 | +$547k | +$372k bull / +$0 bear | out (clean 33, ADX 21, RVol 0.7) |
| 22 | **HOOD** | 85.08 | - | **-** | 16 | - | NEG -$10.4M | - | 93 | 90 | -$120k | +$26k bull / +$0 bear | out (clean 31, ADX 27, RVol 0.4) |
| 23 | **UBER** | 67.16 | - | **-** | 14 | - | NEG -$8.0M | - | 70 | 65 | -$474k | - | out (clean 28, ADX 30, RVol 0.4) |
| 24 | **ARM** | 201.88 | - | **-** | 13 | - | NEG -$6.6M | - | 220 | 200 | +$307k | - | out (clean 25, ADX 17, RVol 1.0) |
| 25 | **IWM** | 280.82 | - | **-** | 8 | - | NEG -$1.1B | 286.57 | 285 | 270 | +$2.3M | - | out (clean 31, ADX 25, RVol 1.4) |
| 26 | **COIN** | 139.41 | - | **-** | 8 | - | NEG -$7.7M | - | 150 | 130 | -$300k | - | out (clean 24, ADX 14, RVol 1.1) |
| 27 | **CRM** | 232.40 | - | **-** | 7 | - | NEG -$4.4M | 240.97 | 240 | 220 | +$71k | - | out (clean 27, ADX 10, RVol 0.4) |

## Big prints this scan (111)
- **QQQ** PUT 691 2026-11-06 (4DTE): 3,500 @ 9.33 = **+$3.3M** SELL | vol 4,122 / OI 15,392
- **QQQ** CALL 693 2026-11-06 (4DTE): 3,500 @ 9.17 = **+$3.2M** BUY | vol 3,924 / OI 73
- **QQQ** PUT 700 2026-11-03 (1DTE): 249 @ 9.72 = **+$242k** SELL | vol 4,909 / OI 1,423
- **DELL** PUT 390 2026-11-06 (4DTE): 257 @ 8.00 = **+$206k** SELL | vol 898 / OI 427
- **QQQ** PUT 700 2026-11-03 (1DTE): 200 @ 9.79 = **+$196k** SELL | vol 4,909 / OI 1,423
- **QQQ** PUT 700 2026-11-03 (1DTE): 189 @ 9.38 = **+$177k** SELL | vol 4,909 / OI 1,423
- **AMD** PUT 480 2026-11-06 (4DTE): 79 @ 20.64 = **+$163k** SELL | vol 1,907 / OI 1,980
- **QQQ** CALL 713 2026-11-06 (4DTE): 798 @ 2.04 = **+$163k** BUY | vol 2,236 / OI 689
- **QQQ** CALL 692 2026-11-04 (2DTE): 200 @ 7.28 = **+$146k** BUY | vol 682 / OI 0
- **AAPL** PUT 345 2026-11-06 (4DTE): 110 @ 12.10 = **+$133k** BUY | vol 989 / OI 4,204
- **MU** PUT 880 2026-11-02 (0DTE): 50 @ 26.00 = **+$130k** SELL | vol 9,501 / OI 325
- **AVGO** CALL 332.5 2026-11-02 (0DTE): 2,915 @ 0.41 = **+$120k** BUY | vol 17,003 / OI 157
- **AMD** PUT 480 2026-11-06 (4DTE): 55 @ 20.62 = **+$113k** SELL | vol 1,907 / OI 1,980
- **AMD** PUT 480 2026-11-06 (4DTE): 55 @ 20.62 = **+$113k** SELL | vol 1,907 / OI 1,980
- **AMD** PUT 480 2026-11-06 (4DTE): 55 @ 20.62 = **+$113k** SELL | vol 1,907 / OI 1,980

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 755 2026-11-06 (4DTE): 6,120 traded vs OI 6,105
- **SPY** CALL 780 2026-11-12 (10DTE): 503 traded vs OI 263
- **SPY** CALL 770 2026-11-13 (11DTE): 2,629 traded vs OI 2,592
- **QQQ** CALL 692 2026-11-04 (2DTE): 682 traded vs OI 0
- **QQQ** CALL 701 2026-11-04 (2DTE): 583 traded vs OI 20
- **QQQ** CALL 693 2026-11-06 (4DTE): 3,924 traded vs OI 73
- **QQQ** PUT 689 2026-11-04 (2DTE): 541 traded vs OI 0
- **QQQ** PUT 650 2026-11-04 (2DTE): 595 traded vs OI 568
- **QQQ** PUT 670 2026-11-16 (14DTE): 514 traded vs OI 0
- **QQQ** PUT 665 2026-11-16 (14DTE): 522 traded vs OI 0
- **QQQ** PUT 690 2026-11-16 (14DTE): 540 traded vs OI 0
- **QQQ** PUT 681 2026-11-13 (11DTE): 506 traded vs OI 89
- **QQQ** CALL 709 2026-11-20 (18DTE): 772 traded vs OI 380
- **IWM** CALL 282 2026-11-06 (4DTE): 1,359 traded vs OI 1,326
- **NVDA** PUT 220 2026-11-09 (7DTE): 502 traded vs OI 42

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
