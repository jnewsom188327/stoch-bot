# GEX + FLOW SCAN - Mon Nov 02, 12:20 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (2)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 12:03 | **QQQ** | **PUTS** | 1m FAILED POP (R3) | 11/02 691P | 0.65 | 0.61 | +34% (8m) | **-6%** | +11% | 692.76 |
| 11:37 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/02 691P | 0.71 | 0.61 | +23% (34m) | **-14%** | +12% | 693.07 hit |

## 1m RULES on SPY / QQQ - loose (4 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 12:20:08 ET, last candle SPY 12:19, QQQ 12:19 | no errors
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
| 1 | **MU** | 859.12 | FLOW SURGE | **CALLS** | 44 | none: 144 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (54 contracts' greeks worked out here) | NEG -$230.5M | - | 910 | 850 | +$108.1M | +$3.9M bull / -$88k bear | out (clean 30, ADX 31, RVol 1.4) |
| 2 | **SMCI** | 32.05 | TREND (flow not with it) | **PUTS** | 30 | none: 13 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$44k | 33.02 | 35 | 33 | +$298k | - | SHORT (clean 33, ADX 31, RVol 1.1) |
| 3 | **AMZN** | 251.44 | - | **-** | 25 | - | POS +$104.8M | 242.61 | 250 | 250 | -$23.6M | +$161k bull / -$82k bear | out (clean 33, ADX 42, RVol 0.4) |
| 4 | **AAPL** | 337.99 | - | **-** | 24 | - | POS +$12.1M | 337 | 350 | 330 | +$17.1M | +$1.7M bull / +$0 bear | out (clean 31, ADX 25, RVol 1.3) |
| 5 | **AMD** | 489.75 | - | **-** | 23 | - | NEG -$86.5M | - | 500 | 500 | +$27.4M | +$345k bull / -$343k bear | out (clean 31, ADX 31, RVol 0.5) |
| 6 | **TSLA** | 411.62 | - | **-** | 21 | - | POS +$319.4M | - | 410 | 400 | -$81.0M | +$454k bull / -$860k bear | out (clean 30, ADX 34, RVol 0.5) |
| 7 | **MSTR** | 134.01 | - | **-** | 21 | - | POS +$3.3M | - | 135 | 125 | +$2.6M | +$116k bull / +$0 bear | out (clean 26, ADX 28, RVol 0.7) |
| 8 | **META** | 611.45 | - | **-** | 19 | - | NEG -$140.5M | 626.53 | 650 | 610 | +$10.7M | +$170k bull / -$47k bear | out (clean 29, ADX 28, RVol 0.3) |
| 9 | **MSFT** | 521.41 | - | **-** | 19 | - | POS +$257.9M | 501.67 | 540 | 500 | -$2.1M | +$151k bull / +$0 bear | out (clean 26, ADX 22, RVol 1.3) |
| 10 | **SHOP** | 160.06 | - | **-** | 19 | - | NEG -$301k | - | 175 | 175 | -$540k | - | out (clean 28, ADX 18, RVol 0.8) |
| 11 | **BABA** | 103.12 | - | **-** | 19 | - | POS +$2.3M | 101.23 | 105 | 100 | -$1.1M | - | out (clean 33, ADX 37, RVol 1.1) |
| 12 | **PLTR** | 184.62 | - | **-** | 17 | - | NEG -$11.3M | - | 200 | 180 | +$2.6M | +$266k bull / +$0 bear | out (clean 25, ADX 10, RVol 0.9) |
| 13 | **NVDA** | 206.92 | - | **-** | 16 | - | NEG -$197.4M | 214.56 | 210 | 200 | +$8.1M | +$448k bull / +$0 bear | out (clean 29, ADX 15, RVol 0.6) |
| 14 | **GOOGL** | 283.46 | - | **-** | 16 | - | NEG -$94.4M | - | 285 | 290 | +$2.2M | +$26k bull / +$0 bear | out (clean 34, ADX 17, RVol 0.4) |
| 15 | **DELL** | 413.98 | - | **-** | 16 | - | NEG -$23.7M | - | 440 | 400 | +$659k | +$36k bull / +$0 bear | out (clean 33, ADX 13, RVol 1.0) |
| 16 | **UBER** | 67.39 | - | **-** | 16 | - | NEG -$8.1M | - | 70 | 65 | -$493k | - | out (clean 28, ADX 35, RVol 0.8) |
| 17 | **QQQ** | 693.78 | - | **-** | 15 | - | NEG -$5.7B | 732.57 | 720 | 680 | +$31.4M | +$273k bull / -$492k bear | out (clean 30, ADX 16, RVol 0.4) |
| 18 | **IWM** | 282.15 | - | **-** | 15 | - | NEG -$856.7M | 286.41 | 285 | 270 | -$618k | +$0 bull / -$300k bear | out (clean 31, ADX 25, RVol 0.4) |
| 19 | **NFLX** | 62.37 | - | **-** | 15 | - | NEG -$22.2M | - | 63 | 60 | +$50k | +$0 bull / -$43k bear | out (clean 28, ADX 18, RVol 0.6) |
| 20 | **SMH** | 523.72 | - | **-** | 12 | - | NEG -$336.8M | - | 532.5 | 500 | +$3.0M | - | out (clean 31, ADX 20, RVol 0.5) |
| 21 | **AVGO** | 330.98 | - | **-** | 11 | - | NEG -$101.9M | - | 340 | 330 | -$5.6M | - | out (clean 31, ADX 26, RVol 0.3) |
| 22 | **CRM** | 232.55 | - | **-** | 9 | - | NEG -$4.6M | 241.09 | 240 | 220 | +$91k | - | out (clean 27, ADX 11, RVol 0.5) |
| 23 | **COIN** | 139.68 | - | **-** | 8 | - | NEG -$7.9M | - | 150 | 130 | -$344k | - | out (clean 24, ADX 12, RVol 0.6) |
| 24 | **ORCL** | 123.11 | - | **-** | 8 | - | NEG -$39.7M | - | 130 | 120 | -$436k | - | out (clean 32, ADX 30, RVol 0.8) |
| 25 | **ARM** | 205.01 | - | **-** | 8 | - | NEG -$7.0M | - | 220 | 200 | +$184k | - | out (clean 25, ADX 12, RVol 0.3) |
| 26 | **HOOD** | 86.18 | - | **-** | 7 | - | NEG -$8.9M | - | 93 | 90 | -$389k | - | out (clean 31, ADX 26, RVol 0.4) |
| 27 | **SPY** | 759.94 | - | **-** | 5 | - | NEG -$9.7B | 774.7 | 770 | 750 | -$4.2M | - | out (clean 29, ADX 18, RVol 0.7) |

## Big prints this scan (76)
- **IWM** PUT 285 2026-11-02 (0DTE): 1,000 @ 3.00 = **+$300k** BUY | vol 2,357 / OI 498
- **AAPL** CALL 350 2026-11-06 (4DTE): 700 @ 3.21 = **+$225k** BUY | vol 22,278 / OI 6,983
- **AAPL** PUT 340 2026-11-04 (2DTE): 242 @ 7.60 = **+$184k** SELL | vol 8,007 / OI 2,460
- **AAPL** CALL 340 2026-11-04 (2DTE): 242 @ 6.81 = **+$165k** BUY | vol 3,282 / OI 204
- **MU** CALL 865 2026-11-02 (0DTE): 400 @ 3.20 = **+$128k** BUY | vol 8,347 / OI 463
- **NVDA** CALL 207.5 2026-11-06 (4DTE): 240 @ 4.05 = **+$97k** BUY | vol 5,938 / OI 327
- **NVDA** CALL 210 2026-11-06 (4DTE): 340 @ 2.80 = **+$95k** BUY | vol 15,677 / OI 997
- **AMD** CALL 490 2026-11-06 (4DTE): 38 @ 23.90 = **+$91k** SELL | vol 536 / OI 214
- **AMD** CALL 487.5 2026-11-02 (0DTE): 198 @ 4.55 = **+$90k** BUY | vol 1,044 / OI 21
- **MSTR** PUT 134 2026-11-06 (4DTE): 175 @ 4.80 = **+$84k** SELL | vol 1,063 / OI 116
- **NVDA** CALL 210 2026-11-04 (2DTE): 436 @ 1.78 = **+$78k** BUY | vol 22,129 / OI 492
- **MU** CALL 885 2026-11-09 (7DTE): 39 @ 19.70 = **+$77k** BUY | vol 1,048 / OI 4
- **NVDA** CALL 207.5 2026-11-06 (4DTE): 181 @ 4.05 = **+$73k** BUY | vol 5,938 / OI 327
- **AMD** CALL 490 2026-11-06 (4DTE): 30 @ 23.90 = **+$72k** SELL | vol 536 / OI 214
- **AAPL** CALL 337.5 2026-11-06 (4DTE): 80 @ 8.80 = **+$70k** BUY | vol 179 / OI 397

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 725 2026-11-10 (8DTE): 1,330 traded vs OI 126
- **SPY** CALL 815 2026-11-09 (7DTE): 602 traded vs OI 115
- **SPY** CALL 810 2026-11-09 (7DTE): 828 traded vs OI 55
- **SPY** CALL 810 2026-11-10 (8DTE): 945 traded vs OI 110
- **QQQ** CALL 712 2026-11-06 (4DTE): 514 traded vs OI 397
- **QQQ** CALL 693 2026-11-04 (2DTE): 510 traded vs OI 0
- **QQQ** PUT 680 2026-11-13 (11DTE): 3,503 traded vs OI 3,437
- **IWM** CALL 281 2026-11-04 (2DTE): 500 traded vs OI 161
- **NVDA** PUT 202.5 2026-11-13 (11DTE): 627 traded vs OI 603
- **TSLA** CALL 437.5 2026-11-02 (0DTE): 506 traded vs OI 168
- **AMD** CALL 490 2026-11-13 (11DTE): 535 traded vs OI 38
- **AMD** CALL 490 2026-11-06 (4DTE): 536 traded vs OI 214
- **MSFT** CALL 547.5 2026-11-06 (4DTE): 768 traded vs OI 764
- **MSFT** CALL 525 2026-11-06 (4DTE): 942 traded vs OI 918
- **MU** PUT 810 2026-11-04 (2DTE): 537 traded vs OI 123

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
