# GEX + FLOW SCAN - Mon Nov 02, 12:40 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (2)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 12:03 | **QQQ** | **PUTS** | 1m FAILED POP (R3) | 11/02 691P | 0.65 | 1.57 | +143% (37m) | **+142%** | +11% | 692.76 hit |
| 11:37 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/02 691P | 0.71 | 1.27 | +111% (58m) | **+79%** (done) | +12% | 693.07 hit |

## 1m RULES on SPY / QQQ - loose (4 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 12:40:08 ET, last candle SPY 12:39, QQQ 12:39 | no errors
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
| 1 | **SHOP** | 159.68 | FLOW SURGE | **PUTS** | 45 | none: 17 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$419k | - | 175 | 175 | -$804k | +$0 bull / -$185k bear | out (clean 28, ADX 21, RVol 1.1) |
| 2 | **AAPL** | 336.96 | FLIP CROSS up into positive gamma | **CALLS** | 42 | none: 81 calls 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$7.2M | 336.75 | 350 | 330 | +$20.3M | +$1.1M bull / +$0 bear | out (clean 31, ADX 33, RVol 1.2) |
| 3 | **MU** | 851.87 | FLOW SURGE | **CALLS** | 41 | none: 139 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (57 contracts' greeks worked out here) | NEG -$221.7M | - | 910 | 850 | +$124.7M | +$6.2M bull / +$0 bear | out (clean 31, ADX 35, RVol 0.8) |
| 4 | **MSFT** | 519.92 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 40 | 11/02 522.5C @ 0.61 (delta 0.25) = est +318% at 525 | POS +$238.2M | 501.87 | 540 | 520 | -$1.2M | +$291k bull / +$0 bear | out (clean 26, ADX 28, RVol 1.2) |
| 5 | **AMZN** | 250.14 | PINNED between the walls (positive gamma) - chop | **-** | 36 | - | POS +$92.3M | 242.04 | 250 | 250 | -$21.6M | +$114k bull / +$0 bear | out (clean 33, ADX 33, RVol 0.6) |
| 6 | **SMCI** | 31.76 | TREND (flow not with it) | **PUTS** | 28 | none: 12 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$440k | - | 34 | 30 | +$390k | +$26k bull / +$0 bear | SHORT (clean 33, ADX 34, RVol 0.8) |
| 7 | **AMD** | 486.25 | - | **-** | 24 | - | NEG -$84.4M | - | 500 | 480 | +$30.6M | +$859k bull / -$48k bear | out (clean 31, ADX 32, RVol 0.5) |
| 8 | **SMH** | 520.19 | - | **-** | 22 | - | NEG -$349.4M | - | 532.5 | 500 | +$3.4M | +$143k bull / +$0 bear | out (clean 31, ADX 20, RVol 0.5) |
| 9 | **MSTR** | 133.16 | - | **-** | 21 | - | POS +$2.2M | - | 135 | 125 | +$3.7M | +$644k bull / +$0 bear | out (clean 26, ADX 25, RVol 0.8) |
| 10 | **META** | 611.78 | - | **-** | 20 | - | NEG -$133.8M | 625.91 | 650 | 610 | +$11.5M | +$357k bull / -$98k bear | out (clean 29, ADX 29, RVol 0.4) |
| 11 | **TSLA** | 408.60 | - | **-** | 19 | - | POS +$299.6M | - | 410 | 400 | -$70.0M | +$724k bull / +$0 bear | out (clean 30, ADX 27, RVol 0.4) |
| 12 | **AVGO** | 329.09 | - | **-** | 19 | - | NEG -$104.2M | - | 340 | 330 | -$4.9M | +$272k bull / +$0 bear | out (clean 30, ADX 22, RVol 0.3) |
| 13 | **PLTR** | 184.26 | - | **-** | 17 | - | NEG -$11.3M | - | 200 | 180 | +$2.7M | +$168k bull / +$0 bear | out (clean 25, ADX 11, RVol 0.7) |
| 14 | **ORCL** | 122.08 | - | **-** | 17 | - | NEG -$38.1M | - | 130 | 120 | -$198k | +$92k bull / -$31k bear | out (clean 32, ADX 31, RVol 0.7) |
| 15 | **BABA** | 103.00 | - | **-** | 17 | - | POS +$2.1M | 101.22 | 105 | 100 | -$1.1M | - | out (clean 33, ADX 30, RVol 0.9) |
| 16 | **QQQ** | 691.55 | - | **-** | 16 | - | NEG -$5.6B | - | 720 | 680 | +$47.4M | +$1.4M bull / +$0 bear | out (clean 30, ADX 19, RVol 0.3) |
| 17 | **NVDA** | 206.29 | - | **-** | 16 | - | NEG -$217.9M | 215.34 | 210 | 200 | +$9.6M | +$523k bull / +$0 bear | out (clean 29, ADX 15, RVol 0.7) |
| 18 | **GOOGL** | 282.51 | - | **-** | 16 | - | NEG -$93.6M | - | 285 | 290 | +$2.8M | +$165k bull / +$0 bear | out (clean 34, ADX 18, RVol 0.3) |
| 19 | **SPY** | 758.23 | - | **-** | 15 | - | NEG -$10.1B | 775.79 | 770 | 750 | +$13.1M | +$2.5M bull / +$0 bear | out (clean 29, ADX 20, RVol 0.5) |
| 20 | **NFLX** | 62.59 | - | **-** | 15 | - | NEG -$20.5M | - | 63 | 60 | -$32k | +$0 bull / -$30k bear | out (clean 28, ADX 23, RVol 0.5) |
| 21 | **UBER** | 67.36 | - | **-** | 15 | - | NEG -$8.3M | - | 70 | 65 | -$492k | - | out (clean 28, ADX 33, RVol 0.6) |
| 22 | **ARM** | 203.24 | - | **-** | 10 | - | NEG -$7.2M | - | 220 | 200 | +$212k | - | out (clean 25, ADX 14, RVol 1.0) |
| 23 | **COIN** | 139.10 | - | **-** | 7 | - | NEG -$7.8M | - | 150 | 130 | -$290k | - | out (clean 24, ADX 13, RVol 0.8) |
| 24 | **CRM** | 231.87 | - | **-** | 7 | - | NEG -$5.6M | 242.36 | 240 | 220 | +$70k | - | out (clean 27, ADX 11, RVol 0.5) |
| 25 | **DELL** | 410.51 | - | **-** | 6 | - | NEG -$22.9M | - | 440 | 400 | +$973k | - | out (clean 33, ADX 16, RVol 0.7) |
| 26 | **HOOD** | 85.44 | - | **-** | 6 | - | NEG -$10.5M | - | 93 | 90 | -$185k | - | out (clean 31, ADX 25, RVol 0.4) |
| 27 | **IWM** | 281.27 | - | **-** | 5 | - | NEG -$1.0B | 286.61 | 285 | 270 | +$628k | - | out (clean 31, ADX 23, RVol 0.4) |

## Big prints this scan (71)
- **MSTR** PUT 136 2026-11-06 (4DTE): 580 @ 6.45 = **+$374k** SELL | vol 2,457 / OI 424
- **MU** PUT 865 2026-11-04 (2DTE): 126 @ 24.20 = **+$305k** SELL | vol 2,358 / OI 190
- **MU** PUT 870 2026-11-04 (2DTE): 109 @ 27.00 = **+$294k** SELL | vol 2,200 / OI 274
- **AMD** PUT 485 2026-11-04 (2DTE): 150 @ 19.45 = **+$292k** SELL | vol 627 / OI 21
- **AVGO** CALL 332.5 2026-11-02 (0DTE): 2,350 @ 0.64 = **+$150k** BUY | vol 13,745 / OI 157
- **SPY** CALL 764 2026-11-06 (4DTE): 344 @ 4.03 = **+$139k** BUY | vol 3,416 / OI 1,314
- **SPY** CALL 760 2026-11-03 (1DTE): 500 @ 2.70 = **+$135k** BUY | vol 21,896 / OI 437
- **QQQ** PUT 693 2026-11-04 (2DTE): 192 @ 7.03 = **+$135k** SELL | vol 1,580 / OI 0
- **SPY** PUT 756 2026-11-04 (2DTE): 421 @ 3.15 = **+$133k** SELL | vol 12,438 / OI 149
- **MU** PUT 865 2026-11-04 (2DTE): 46 @ 24.20 = **+$111k** SELL | vol 2,358 / OI 190
- **MSTR** PUT 134 2026-11-06 (4DTE): 184 @ 5.45 = **+$100k** SELL | vol 1,321 / OI 116
- **AAPL** PUT 330 2026-11-04 (2DTE): 200 @ 4.20 = **+$84k** SELL | vol 13,368 / OI 3,455
- **TSLA** PUT 415 2026-11-02 (0DTE): 190 @ 4.30 = **+$82k** SELL | vol 10,668 / OI 137
- **MU** PUT 870 2026-11-04 (2DTE): 27 @ 27.00 = **+$73k** SELL | vol 2,200 / OI 274
- **AMD** PUT 490 2026-11-04 (2DTE): 30 @ 22.00 = **+$66k** SELL | vol 594 / OI 104

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 742 2026-11-06 (4DTE): 1,519 traded vs OI 1,517
- **SPY** CALL 771 2026-11-06 (4DTE): 1,193 traded vs OI 1,187
- **SPY** PUT 735 2026-11-05 (3DTE): 1,083 traded vs OI 858
- **QQQ** PUT 672 2026-11-02 (0DTE): 504 traded vs OI 0
- **IWM** PUT 278 2026-11-04 (2DTE): 519 traded vs OI 492
- **SMH** PUT 510 2026-11-06 (4DTE): 501 traded vs OI 372
- **TSLA** CALL 425 2026-11-13 (11DTE): 1,197 traded vs OI 1,052
- **AAPL** CALL 345 2026-11-06 (4DTE): 1,837 traded vs OI 1,802
- **AAPL** CALL 340 2026-11-06 (4DTE): 2,772 traded vs OI 2,704
- **AMD** PUT 485 2026-11-04 (2DTE): 627 traded vs OI 21
- **MSFT** CALL 532.5 2026-11-06 (4DTE): 513 traded vs OI 391
- **MSFT** CALL 555 2026-11-06 (4DTE): 1,070 traded vs OI 1,067
- **AVGO** CALL 332.5 2026-11-06 (4DTE): 541 traded vs OI 359
- **MU** CALL 915 2026-11-06 (4DTE): 542 traded vs OI 251
- **MU** CALL 925 2026-11-06 (4DTE): 523 traded vs OI 238

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
