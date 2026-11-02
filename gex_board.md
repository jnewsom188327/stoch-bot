# GEX + FLOW SCAN - Mon Nov 02, 11:40 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (1)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:37 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/02 691P | 0.71 | 0.79 | +13% (1m) | **+11%** | +12% | 693.07 |

## 1m RULES on SPY / QQQ - loose (2 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 11:40:08 ET, last candle SPY 11:39, QQQ 11:39 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
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
| 1 | **MU** | 863.22 | FLOW SURGE | **CALLS** | 50 | none: 141 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (63 contracts' greeks worked out here) | NEG -$220.0M | - | 910 | 850 | +$77.5M | +$4.3M bull / +$0 bear | out (clean 30, ADX 23, RVol 2.6) |
| 2 | **TSLA** | 410.65 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 41 | none: 132 puts 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (58 contracts' greeks worked out here) | POS +$319.0M | - | 410 | 400 | -$70.4M | +$2.1M bull / +$0 bear | out (clean 30, ADX 38, RVol 0.7) |
| 3 | **SMCI** | 32.22 | FLIP CROSS down into negative gamma | **PUTS** | 38 | none: 13 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$52k | 33.4 | 35 | 30 | +$175k | +$30k bull / +$0 bear | SHORT (clean 33, ADX 30, RVol 1.0) |
| 4 | **AMZN** | 251.49 | - | **-** | 27 | - | POS +$108.6M | 242.07 | 250 | 250 | -$24.4M | +$517k bull / -$104k bear | out (clean 33, ADX 59, RVol 0.7) |
| 5 | **AMD** | 488.76 | - | **-** | 26 | - | NEG -$83.1M | - | 500 | 500 | +$27.3M | +$1.5M bull / +$0 bear | out (clean 30, ADX 34, RVol 1.2) |
| 6 | **SMH** | 522.54 | - | **-** | 25 | - | NEG -$342.8M | - | 532.5 | 500 | +$3.1M | +$2.1M bull / +$0 bear | out (clean 31, ADX 28, RVol 0.8) |
| 7 | **MSTR** | 135.81 | - | **-** | 24 | - | POS +$3.7M | - | 135 | 125 | +$2.3M | +$0 bull / -$84k bear | out (clean 26, ADX 37, RVol 1.6) |
| 8 | **BABA** | 103.25 | - | **-** | 23 | - | POS +$2.9M | 100.96 | 105 | 100 | -$1.2M | - | out (clean 33, ADX 52, RVol 1.3) |
| 9 | **AAPL** | 340.43 | - | **-** | 20 | - | POS +$51.5M | 336.9 | 350 | 330 | +$9.9M | +$554k bull / -$245k bear | out (clean 31, ADX 15, RVol 0.9) |
| 10 | **COIN** | 139.81 | - | **-** | 20 | - | NEG -$7.9M | - | 150 | 130 | -$334k | +$0 bull / -$64k bear | out (clean 25, ADX 19, RVol 1.1) |
| 11 | **META** | 613.41 | - | **-** | 19 | - | NEG -$130.4M | 626.61 | 650 | 610 | +$8.1M | +$0 bull / -$338k bear | out (clean 29, ADX 27, RVol 0.6) |
| 12 | **MSFT** | 523.82 | - | **-** | 19 | - | POS +$321.4M | 501.66 | 540 | 530 | -$2.8M | +$43k bull / +$0 bear | out (clean 26, ADX 22, RVol 1.0) |
| 13 | **SHOP** | 158.28 | - | **-** | 19 | - | NEG -$429k | - | 170 | 160 | -$421k | - | out (clean 28, ADX 21, RVol 1.2) |
| 14 | **NVDA** | 206.65 | - | **-** | 18 | - | NEG -$207.5M | 215.45 | 210 | 200 | +$6.6M | +$537k bull / +$0 bear | out (clean 30, ADX 21, RVol 1.1) |
| 15 | **GOOGL** | 283.31 | - | **-** | 18 | - | NEG -$88.8M | - | 285 | 290 | +$1.7M | +$57k bull / +$0 bear | out (clean 35, ADX 26, RVol 0.8) |
| 16 | **NFLX** | 62.12 | - | **-** | 18 | - | NEG -$24.0M | - | 63 | 60 | +$298k | +$0 bull / -$41k bear | out (clean 29, ADX 15, RVol 1.2) |
| 17 | **ORCL** | 123.71 | - | **-** | 18 | - | NEG -$40.0M | - | 130 | 120 | -$516k | +$30k bull / -$27k bear | out (clean 32, ADX 31, RVol 0.7) |
| 18 | **SPY** | 759.98 | - | **-** | 17 | - | NEG -$9.6B | 774.69 | 770 | 750 | -$24.9M | +$902k bull / -$797k bear | out (clean 29, ADX 28, RVol 0.6) |
| 19 | **QQQ** | 693.76 | - | **-** | 16 | - | NEG -$5.7B | 731.38 | 720 | 680 | +$17.4M | +$956k bull / +$0 bear | out (clean 29, ADX 24, RVol 0.7) |
| 20 | **PLTR** | 184.64 | - | **-** | 15 | - | NEG -$11.1M | - | 200 | 180 | -$830k | +$0 bull / -$76k bear | out (clean 25, ADX 11, RVol 0.7) |
| 21 | **DELL** | 415.43 | - | **-** | 15 | - | NEG -$24.1M | - | 440 | 400 | -$166k | +$0 bull / -$72k bear | out (clean 34, ADX 13, RVol 0.9) |
| 22 | **AVGO** | 330.99 | - | **-** | 14 | - | NEG -$100.6M | - | 340 | 330 | -$5.4M | - | out (clean 31, ADX 42, RVol 0.4) |
| 23 | **UBER** | 67.25 | - | **-** | 14 | - | NEG -$8.5M | - | 70 | 65 | -$232k | - | out (clean 28, ADX 42, RVol 0.7) |
| 24 | **CRM** | 232.05 | - | **-** | 11 | - | NEG -$5.6M | 242.36 | 240 | 220 | +$99k | - | out (clean 28, ADX 14, RVol 0.8) |
| 25 | **ARM** | 204.75 | - | **-** | 10 | - | NEG -$7.1M | - | 220 | 200 | +$186k | - | out (clean 26, ADX 19, RVol 0.6) |
| 26 | **HOOD** | 86.17 | - | **-** | 9 | - | NEG -$9.1M | - | 93 | 90 | -$469k | - | out (clean 32, ADX 37, RVol 0.4) |
| 27 | **IWM** | 282.55 | - | **-** | 7 | - | NEG -$802.6M | 286.46 | 285 | 270 | +$161k | - | out (clean 31, ADX 35, RVol 0.4) |

## Big prints this scan (100)
- **SPY** PUT 765 2026-11-05 (3DTE): 500 @ 7.50 = **+$375k** MID | vol 4,917 / OI 2,269
- **SPY** CALL 761 2026-11-06 (4DTE): 507 @ 5.87 = **+$298k** BUY | vol 4,205 / OI 499
- **TSLA** PUT 407.5 2026-11-06 (4DTE): 243 @ 7.50 = **+$182k** SELL | vol 2,802 / OI 1,311
- **MU** PUT 870 2026-11-02 (0DTE): 284 @ 5.85 = **+$166k** SELL | vol 19,281 / OI 677
- **MU** PUT 870 2026-11-02 (0DTE): 276 @ 5.85 = **+$161k** SELL | vol 19,281 / OI 677
- **SPY** PUT 790 2026-11-06 (4DTE): 50 @ 30.00 = **+$150k** MID | vol 100 / OI 30
- **AMD** CALL 490 2026-11-02 (0DTE): 339 @ 4.25 = **+$144k** BUY | vol 1,386 / OI 10
- **AAPL** PUT 325 2026-11-06 (4DTE): 500 @ 2.73 = **+$136k** SELL | vol 3,255 / OI 10,672
- **SPY** PUT 759 2026-11-03 (1DTE): 567 @ 2.31 = **+$131k** SELL | vol 13,445 / OI 2,770
- **SPY** PUT 761 2026-11-03 (1DTE): 400 @ 3.12 = **+$125k** SELL | vol 13,094 / OI 628
- **QQQ** CALL 694 2026-11-04 (2DTE): 150 @ 7.32 = **+$110k** BUY | vol 2,996 / OI 0
- **QQQ** CALL 694 2026-11-04 (2DTE): 150 @ 7.27 = **+$109k** BUY | vol 2,996 / OI 0
- **SMH** PUT 525 2026-11-06 (4DTE): 89 @ 12.25 = **+$109k** SELL | vol 340 / OI 1,477
- **AMD** CALL 492.5 2026-11-02 (0DTE): 339 @ 2.94 = **+$100k** BUY | vol 2,213 / OI 2
- **MU** CALL 860 2026-11-02 (0DTE): 100 @ 9.70 = **+$97k** BUY | vol 1,267 / OI 55

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 815 2026-11-10 (8DTE): 980 traded vs OI 9
- **SPY** PUT 764 2026-11-04 (2DTE): 666 traded vs OI 470
- **SPY** CALL 830 2026-11-11 (9DTE): 700 traded vs OI 2
- **SPY** PUT 755 2026-11-16 (14DTE): 500 traded vs OI 0
- **SPY** CALL 825 2026-11-11 (9DTE): 599 traded vs OI 8
- **SPY** CALL 820 2026-11-11 (9DTE): 796 traded vs OI 3
- **QQQ** CALL 725 2026-11-03 (1DTE): 1,375 traded vs OI 987
- **QQQ** CALL 717 2026-11-06 (4DTE): 825 traded vs OI 751
- **IWM** CALL 292 2026-11-13 (11DTE): 555 traded vs OI 477
- **IWM** CALL 285 2026-11-13 (11DTE): 1,384 traded vs OI 1,336
- **IWM** CALL 290 2026-11-13 (11DTE): 1,047 traded vs OI 1,021
- **SMH** PUT 522.5 2026-11-02 (0DTE): 522 traded vs OI 281
- **NVDA** PUT 192.5 2026-11-04 (2DTE): 1,422 traded vs OI 1,413
- **TSLA** PUT 400 2026-11-06 (4DTE): 4,465 traded vs OI 4,312
- **TSLA** PUT 372.5 2026-11-04 (2DTE): 507 traded vs OI 127

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
