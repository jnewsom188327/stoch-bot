# GEX + FLOW SCAN - Mon Nov 02, 12:10 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (2)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 12:03 | **QQQ** | **PUTS** | 1m FAILED POP (R3) | 11/02 691P | 0.65 | 0.82 | +26% (7m) | **+26%** | +11% | 692.76 |
| 11:37 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/02 691P | 0.71 | 0.82 | +18% (4m) | **+15%** | +12% | 693.07 |

## 1m RULES on SPY / QQQ - loose (4 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 12:10:08 ET, last candle SPY 12:09, QQQ 12:09 | no errors
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
| 1 | **MU** | 857.73 | FLOW SURGE | **CALLS** | 49 | none: 140 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (59 contracts' greeks worked out here) | NEG -$223.9M | - | 910 | 850 | +$102.3M | +$4.4M bull / -$149k bear | out (clean 30, ADX 29, RVol 2.1) |
| 2 | **SMCI** | 31.93 | TREND (flow not with it) | **PUTS** | 30 | none: 13 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$84k | 33.73 | 35 | 30 | +$276k | - | SHORT (clean 34, ADX 29, RVol 1.2) |
| 3 | **SHOP** | 158.76 | - | **-** | 27 | - | NEG -$369k | - | 170 | 160 | -$408k | +$78k bull / -$45k bear | out (clean 27, ADX 16, RVol 0.9) |
| 4 | **AMZN** | 251.48 | - | **-** | 26 | - | POS +$105.3M | 242.51 | 250 | 250 | -$23.5M | +$203k bull / -$135k bear | out (clean 33, ADX 45, RVol 0.4) |
| 5 | **AMD** | 489.37 | - | **-** | 24 | - | NEG -$86.5M | - | 500 | 500 | +$26.8M | +$65k bull / -$1.1M bear | out (clean 31, ADX 33, RVol 0.6) |
| 6 | **AAPL** | 338.75 | - | **-** | 23 | - | POS +$14.5M | 337.13 | 350 | 330 | +$14.9M | +$1.6M bull / -$28k bear | out (clean 31, ADX 21, RVol 1.3) |
| 7 | **SMH** | 522.80 | - | **-** | 22 | - | NEG -$342.3M | - | 532.5 | 500 | +$2.9M | +$0 bull / -$153k bear | out (clean 31, ADX 22, RVol 0.4) |
| 8 | **TSLA** | 412.52 | - | **-** | 22 | - | POS +$307.8M | - | 410 | 400 | -$80.7M | +$0 bull / -$1.7M bear | out (clean 30, ADX 34, RVol 0.5) |
| 9 | **AVGO** | 330.22 | - | **-** | 21 | - | NEG -$102.9M | - | 340 | 330 | -$5.7M | +$52k bull / +$0 bear | out (clean 31, ADX 29, RVol 0.3) |
| 10 | **META** | 611.41 | - | **-** | 20 | - | NEG -$141.7M | 626.03 | 650 | 610 | +$11.0M | +$489k bull / +$0 bear | out (clean 29, ADX 27, RVol 0.4) |
| 11 | **BABA** | 103.15 | - | **-** | 20 | - | POS +$2.1M | 101.38 | 105 | 100 | -$1.1M | - | out (clean 33, ADX 42, RVol 1.0) |
| 12 | **IWM** | 282.19 | - | **-** | 17 | - | NEG -$871.8M | 286.54 | 285 | 270 | -$1.0M | +$538k bull / +$0 bear | out (clean 31, ADX 28, RVol 0.5) |
| 13 | **MSFT** | 520.85 | - | **-** | 17 | - | POS +$245.7M | 502.44 | 540 | 500 | -$2.7M | +$435k bull / +$0 bear | out (clean 26, ADX 20, RVol 0.6) |
| 14 | **PLTR** | 184.06 | - | **-** | 17 | - | NEG -$11.5M | - | 200 | 180 | +$2.6M | +$266k bull / +$0 bear | out (clean 25, ADX 10, RVol 0.9) |
| 15 | **NVDA** | 206.77 | - | **-** | 16 | - | NEG -$207.5M | 215.65 | 210 | 200 | +$6.2M | +$0 bull / -$106k bear | out (clean 29, ADX 16, RVol 0.7) |
| 16 | **GOOGL** | 283.29 | - | **-** | 16 | - | NEG -$94.1M | - | 285 | 290 | +$1.9M | +$26k bull / +$0 bear | out (clean 34, ADX 19, RVol 0.5) |
| 17 | **DELL** | 413.06 | - | **-** | 16 | - | NEG -$23.3M | - | 440 | 400 | +$706k | +$504k bull / +$0 bear | out (clean 33, ADX 14, RVol 0.8) |
| 18 | **UBER** | 67.25 | - | **-** | 16 | - | NEG -$8.4M | - | 70 | 65 | -$483k | - | out (clean 27, ADX 37, RVol 0.7) |
| 19 | **SPY** | 759.66 | - | **-** | 15 | - | NEG -$9.9B | 775.33 | 800 | 750 | -$10.1M | +$114k bull / +$0 bear | out (clean 30, ADX 19, RVol 0.6) |
| 20 | **QQQ** | 693.38 | - | **-** | 15 | - | NEG -$5.7B | 732.19 | 720 | 680 | +$21.4M | +$0 bull / -$233k bear | out (clean 30, ADX 17, RVol 0.5) |
| 21 | **MSTR** | 134.38 | - | **-** | 12 | - | POS +$3.2M | - | 135 | 125 | +$2.2M | - | out (clean 26, ADX 32, RVol 1.0) |
| 22 | **CRM** | 231.49 | - | **-** | 9 | - | NEG -$5.4M | 242.07 | 240 | 220 | +$95k | - | out (clean 27, ADX 11, RVol 0.4) |
| 23 | **COIN** | 139.84 | - | **-** | 8 | - | NEG -$8.0M | - | 150 | 130 | -$355k | - | out (clean 24, ADX 14, RVol 0.7) |
| 24 | **HOOD** | 86.32 | - | **-** | 8 | - | NEG -$9.1M | - | 93 | 90 | -$556k | - | out (clean 32, ADX 29, RVol 0.4) |
| 25 | **ARM** | 203.94 | - | **-** | 8 | - | NEG -$7.1M | - | 220 | 200 | +$182k | - | out (clean 26, ADX 13, RVol 0.3) |
| 26 | **ORCL** | 122.20 | - | **-** | 7 | - | NEG -$38.1M | - | 130 | 120 | -$332k | - | out (clean 32, ADX 29, RVol 0.6) |
| 27 | **NFLX** | 62.23 | - | **-** | 6 | - | NEG -$23.3M | - | 63 | 60 | +$116k | - | out (clean 28, ADX 17, RVol 0.7) |

## Big prints this scan (53)
- **MU** PUT 900 2026-11-02 (0DTE): 98 @ 39.00 = **+$382k** SELL | vol 673 / OI 740
- **AAPL** CALL 350 2026-11-06 (4DTE): 700 @ 3.20 = **+$224k** BUY | vol 21,059 / OI 6,983
- **AAPL** CALL 350 2026-11-06 (4DTE): 641 @ 3.25 = **+$208k** BUY | vol 21,059 / OI 6,983
- **PLTR** PUT 185 2026-11-06 (4DTE): 100 @ 11.63 = **+$116k** SELL | vol 1,445 / OI 1,451
- **PLTR** CALL 185 2026-11-06 (4DTE): 100 @ 11.27 = **+$113k** BUY | vol 2,283 / OI 423
- **MU** CALL 900 2026-11-06 (4DTE): 69 @ 11.85 = **+$82k** BUY | vol 2,361 / OI 373
- **MU** CALL 875 2026-11-04 (2DTE): 56 @ 14.47 = **+$81k** BUY | vol 1,742 / OI 93
- **AMZN** CALL 252.5 2026-11-02 (0DTE): 1,120 @ 0.60 = **+$67k** BUY | vol 58,779 / OI 366
- **AMD** PUT 495 2026-11-06 (4DTE): 24 @ 27.04 = **+$65k** SELL | vol 316 / OI 761
- **TSLA** PUT 405 2026-11-06 (4DTE): 91 @ 7.05 = **+$64k** BUY | vol 3,234 / OI 1,523
- **AMZN** CALL 252.5 2026-11-02 (0DTE): 1,000 @ 0.60 = **+$60k** BUY | vol 58,779 / OI 366
- **MU** PUT 875 2026-11-04 (2DTE): 20 @ 28.40 = **+$57k** SELL | vol 1,532 / OI 237
- **TSLA** CALL 415 2026-11-04 (2DTE): 100 @ 5.20 = **+$52k** SELL | vol 11,014 / OI 907
- **MU** PUT 870 2026-11-04 (2DTE): 20 @ 25.45 = **+$51k** SELL | vol 1,803 / OI 274
- **MU** PUT 885 2026-11-02 (0DTE): 20 @ 24.68 = **+$49k** SELL | vol 2,855 / OI 261

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 755 2026-11-06 (4DTE): 912 traded vs OI 911
- **SPY** CALL 763 2026-11-13 (11DTE): 638 traded vs OI 610
- **SPY** PUT 764 2026-11-13 (11DTE): 739 traded vs OI 734
- **QQQ** PUT 707 2026-11-06 (4DTE): 608 traded vs OI 393
- **QQQ** PUT 688 2026-11-04 (2DTE): 609 traded vs OI 0
- **IWM** PUT 283 2026-11-04 (2DTE): 501 traded vs OI 161
- **IWM** PUT 279 2026-11-03 (1DTE): 1,389 traded vs OI 1,298
- **SMH** CALL 525 2026-11-02 (0DTE): 522 traded vs OI 3
- **SMH** CALL 562.5 2026-11-06 (4DTE): 663 traded vs OI 238
- **AAPL** PUT 305 2026-11-06 (4DTE): 747 traded vs OI 0
- **AAPL** PUT 305 2026-11-04 (2DTE): 3,010 traded vs OI 0
- **AAPL** CALL 372.5 2026-11-04 (2DTE): 1,429 traded vs OI 1,383
- **AMD** CALL 507.5 2026-11-06 (4DTE): 504 traded vs OI 62
- **AMD** CALL 505 2026-11-04 (2DTE): 502 traded vs OI 34
- **AMZN** CALL 260 2026-11-27 (25DTE): 716 traded vs OI 704

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
