# GEX + FLOW SCAN - Mon Nov 02, 12:00 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (1)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:37 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/02 691P | 0.71 | 0.63 | +18% (4m) | **-11%** | +12% | 693.07 |

## 1m RULES on SPY / QQQ - loose (3 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 12:00:08 ET, last candle SPY 11:59, QQQ 11:59 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
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
| 1 | **MU** | 859.93 | FLOW SURGE | **CALLS** | 51 | none: 144 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (58 contracts' greeks worked out here) | NEG -$222.1M | - | 910 | 850 | +$92.9M | +$4.0M bull / -$149k bear | out (clean 30, ADX 27, RVol 2.6) |
| 2 | **MSTR** | 134.72 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 45 | none: 27 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$3.5M | - | 135 | 125 | +$1.8M | +$145k bull / +$0 bear | out (clean 26, ADX 36, RVol 1.5) |
| 3 | **SMCI** | 32.19 | FLIP CROSS up into positive gamma | **CALLS** | 37 | none: 13 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$9k | 32.06 | 35 | 33 | +$192k | +$42k bull / +$0 bear | SHORT (clean 34, ADX 29, RVol 1.0) |
| 4 | **SHOP** | 158.46 | - | **-** | 28 | - | NEG -$395k | - | 170 | 160 | -$411k | +$78k bull / -$45k bear | out (clean 28, ADX 18, RVol 1.0) |
| 5 | **AMZN** | 251.25 | - | **-** | 26 | - | POS +$107.9M | 242.31 | 250 | 250 | -$24.0M | +$94k bull / -$317k bear | out (clean 33, ADX 49, RVol 0.4) |
| 6 | **AMD** | 489.58 | - | **-** | 25 | - | NEG -$82.8M | - | 500 | 500 | +$27.6M | +$563k bull / -$654k bear | out (clean 30, ADX 34, RVol 0.8) |
| 7 | **SMH** | 523.18 | - | **-** | 23 | - | NEG -$334.1M | - | 532.5 | 500 | +$3.0M | +$0 bull / -$31k bear | out (clean 31, ADX 25, RVol 0.5) |
| 8 | **AAPL** | 339.19 | - | **-** | 23 | - | POS +$30.0M | 336.9 | 350 | 330 | +$14.6M | +$1.8M bull / +$0 bear | out (clean 31, ADX 19, RVol 1.3) |
| 9 | **AVGO** | 330.85 | - | **-** | 23 | - | NEG -$97.6M | - | 340 | 330 | -$6.0M | +$26k bull / +$0 bear | out (clean 30, ADX 33, RVol 0.3) |
| 10 | **BABA** | 103.37 | - | **-** | 22 | - | POS +$3.2M | 100.83 | 105 | 100 | -$1.2M | - | out (clean 33, ADX 46, RVol 1.0) |
| 11 | **TSLA** | 411.50 | - | **-** | 21 | - | POS +$318.3M | - | 410 | 400 | -$75.5M | +$584k bull / -$796k bear | out (clean 30, ADX 34, RVol 0.5) |
| 12 | **META** | 610.64 | - | **-** | 20 | - | NEG -$130.6M | 623.56 | 650 | 610 | +$10.6M | +$698k bull / +$0 bear | out (clean 29, ADX 26, RVol 0.5) |
| 13 | **HOOD** | 86.44 | - | **-** | 20 | - | NEG -$8.8M | - | 93 | 90 | -$690k | +$0 bull / -$31k bear | out (clean 32, ADX 32, RVol 0.4) |
| 14 | **IWM** | 282.28 | - | **-** | 18 | - | NEG -$819.6M | 286.42 | 285 | 270 | -$1.3M | +$729k bull / -$1.6M bear | out (clean 31, ADX 32, RVol 0.6) |
| 15 | **MSFT** | 523.46 | - | **-** | 18 | - | POS +$349.1M | 500.56 | 540 | 500 | -$3.1M | +$375k bull / +$0 bear | out (clean 26, ADX 18, RVol 0.6) |
| 16 | **GOOGL** | 283.06 | - | **-** | 17 | - | NEG -$89.1M | - | 285 | 290 | +$2.1M | +$72k bull / +$0 bear | out (clean 35, ADX 21, RVol 0.6) |
| 17 | **ORCL** | 122.87 | - | **-** | 17 | - | NEG -$39.8M | - | 130 | 120 | -$449k | +$30k bull / +$0 bear | out (clean 32, ADX 28, RVol 0.4) |
| 18 | **UBER** | 67.39 | - | **-** | 17 | - | NEG -$8.2M | - | 70 | 65 | -$488k | - | out (clean 28, ADX 40, RVol 0.8) |
| 19 | **SPY** | 760.00 | - | **-** | 16 | - | NEG -$9.6B | 774.28 | 770 | 750 | -$22.5M | +$128k bull / -$234k bear | out (clean 30, ADX 21, RVol 0.7) |
| 20 | **NVDA** | 207.02 | - | **-** | 16 | - | NEG -$177.7M | 213.03 | 210 | 200 | +$5.7M | +$151k bull / -$224k bear | out (clean 29, ADX 18, RVol 0.8) |
| 21 | **QQQ** | 693.70 | - | **-** | 15 | - | NEG -$5.5B | 731.55 | 720 | 680 | +$13.2M | +$577k bull / -$102k bear | out (clean 30, ADX 20, RVol 0.5) |
| 22 | **PLTR** | 184.20 | - | **-** | 15 | - | NEG -$11.1M | - | 200 | 180 | +$984k | +$32k bull / -$95k bear | out (clean 25, ADX 10, RVol 0.7) |
| 23 | **DELL** | 412.99 | - | **-** | 15 | - | NEG -$23.2M | - | 440 | 400 | +$486k | +$157k bull / +$0 bear | out (clean 34, ADX 14, RVol 0.9) |
| 24 | **COIN** | 140.25 | - | **-** | 9 | - | NEG -$7.8M | - | 150 | 130 | -$406k | - | out (clean 24, ADX 15, RVol 0.8) |
| 25 | **ARM** | 204.54 | - | **-** | 9 | - | NEG -$6.8M | - | 220 | 200 | +$186k | - | out (clean 26, ADX 14, RVol 0.5) |
| 26 | **CRM** | 231.63 | - | **-** | 9 | - | NEG -$5.8M | 242.41 | 240 | 220 | +$94k | - | out (clean 28, ADX 12, RVol 0.5) |
| 27 | **NFLX** | 62.33 | - | **-** | 6 | - | NEG -$22.4M | - | 63 | 60 | +$142k | - | out (clean 29, ADX 16, RVol 1.0) |

## Big prints this scan (82)
- **IWM** CALL 285 2026-11-09 (7DTE): 2,500 @ 2.15 = **+$538k** BUY | vol 3,690 / OI 0
- **MSFT** CALL 525 2026-11-06 (4DTE): 400 @ 7.82 = **+$313k** BUY | vol 904 / OI 918
- **AAPL** CALL 350 2026-11-06 (4DTE): 700 @ 3.55 = **+$248k** BUY | vol 16,891 / OI 6,983
- **QQQ** PUT 715 2026-11-06 (4DTE): 100 @ 22.47 = **+$225k** MID | vol 238 / OI 12,617
- **META** PUT 640 2026-11-06 (4DTE): 44 @ 30.25 = **+$133k** SELL | vol 504 / OI 1,804
- **QQQ** PUT 701 2026-11-06 (4DTE): 100 @ 12.90 = **+$129k** MID | vol 669 / OI 595
- **AMD** PUT 490 2026-11-06 (4DTE): 50 @ 24.35 = **+$122k** BUY | vol 791 / OI 644
- **MU** CALL 890 2026-11-06 (4DTE): 80 @ 14.94 = **+$120k** SELL | vol 768 / OI 224
- **QQQ** PUT 696 2026-11-02 (0DTE): 313 @ 3.25 = **+$102k** BUY | vol 72,574 / OI 0
- **AMD** PUT 487.5 2026-11-04 (2DTE): 50 @ 20.30 = **+$102k** BUY | vol 168 / OI 27
- **MU** PUT 850 2026-11-09 (7DTE): 40 @ 25.20 = **+$101k** MID | vol 100 / OI 86
- **DELL** PUT 400 2026-11-06 (4DTE): 100 @ 9.70 = **+$97k** SELL | vol 1,318 / OI 922
- **META** CALL 610 2026-11-02 (0DTE): 268 @ 3.50 = **+$94k** BUY | vol 2,468 / OI 108
- **META** CALL 620 2026-11-06 (4DTE): 100 @ 9.00 = **+$90k** BUY | vol 1,347 / OI 1,057
- **AMZN** CALL 257.5 2026-11-09 (7DTE): 364 @ 2.32 = **+$84k** MID | vol 1,199 / OI 0

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 753 2026-11-06 (4DTE): 502 traded vs OI 67
- **QQQ** PUT 675 2026-11-09 (7DTE): 516 traded vs OI 427
- **QQQ** PUT 701 2026-11-06 (4DTE): 669 traded vs OI 595
- **QQQ** CALL 709 2026-11-04 (2DTE): 502 traded vs OI 29
- **NVDA** PUT 197.5 2026-11-06 (4DTE): 3,661 traded vs OI 3,622
- **NVDA** PUT 190 2026-11-06 (4DTE): 5,565 traded vs OI 5,203
- **TSLA** PUT 400 2026-11-09 (7DTE): 504 traded vs OI 425
- **AAPL** PUT 322.5 2026-11-06 (4DTE): 714 traded vs OI 711
- **AMD** CALL 510 2026-11-04 (2DTE): 520 traded vs OI 44
- **AMD** CALL 487.5 2026-11-02 (0DTE): 546 traded vs OI 21
- **META** PUT 550 2026-11-06 (4DTE): 689 traded vs OI 0
- **DELL** PUT 400 2026-11-06 (4DTE): 1,318 traded vs OI 922
- **MU** PUT 780 2026-11-13 (11DTE): 510 traded vs OI 0
- **MU** PUT 810 2026-11-06 (4DTE): 545 traded vs OI 493
- **MU** PUT 860 2026-11-06 (4DTE): 644 traded vs OI 638

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
