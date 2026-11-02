# GEX + FLOW SCAN - Mon Nov 02, 01:30 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (2)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 12:03 | **QQQ** | **PUTS** | 1m FAILED POP (R3) | 11/02 691P | 0.65 | 1.48 | +291% (43m) | **+128%** (done) | +11% | 692.76 hit |
| 11:37 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/02 691P | 0.71 | 1.27 | +111% (58m) | **+79%** (done) | +12% | 693.07 hit |

## 1m RULES on SPY / QQQ - loose (4 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 13:30:08 ET, last candle SPY 13:29, QQQ 13:28 | no errors
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
| 1 | **SMCI** | 31.48 | TREND (flow not with it) | **PUTS** | 35 | none: 13 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$445k | - | 34 | 30 | +$652k | +$140k bull / +$0 bear | SHORT (clean 34, ADX 41, RVol 1.1) |
| 2 | **MU** | 852.22 | - | **-** | 28 | - | NEG -$224.1M | - | 910 | 850 | +$135.0M | +$2.9M bull / -$191k bear | out (clean 31, ADX 37, RVol 0.9) |
| 3 | **DELL** | 405.50 | TREND (flow not with it) | **PUTS** | 26 | none: 33 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$21.2M | - | 440 | 400 | +$552k | +$27k bull / +$0 bear | SHORT (clean 34, ADX 28, RVol 1.2) |
| 4 | **AMD** | 480.99 | - | **-** | 25 | - | NEG -$76.2M | - | 500 | 480 | +$34.6M | +$476k bull / -$159k bear | out (clean 31, ADX 42, RVol 0.7) |
| 5 | **MSFT** | 519.40 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 25 | none: 167 calls 0-7DTE > 10 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (62 contracts' greeks worked out here) | POS +$223.9M | 501.63 | 540 | 520 | -$911k | - | out (clean 27, ADX 31, RVol 0.6) |
| 6 | **AAPL** | 337.14 | - | **-** | 24 | - | NEG -$1.4M | 336.87 | 350 | 330 | +$20.6M | +$2.3M bull / +$0 bear | out (clean 31, ADX 33, RVol 1.0) |
| 7 | **AMZN** | 249.83 | PINNED between the walls (positive gamma) - chop | **-** | 22 | - | POS +$81.6M | 243.65 | 250 | 250 | -$21.1M | - | out (clean 33, ADX 23, RVol 0.4) |
| 8 | **ARM** | 202.49 | - | **-** | 20 | - | NEG -$6.9M | - | 220 | 200 | +$253k | +$0 bull / -$38k bear | out (clean 25, ADX 19, RVol 0.3) |
| 9 | **TSLA** | 408.08 | - | **-** | 18 | - | POS +$305.0M | - | 410 | 400 | -$71.4M | +$206k bull / -$545k bear | out (clean 30, ADX 18, RVol 0.5) |
| 10 | **MSTR** | 133.24 | - | **-** | 18 | - | POS +$2.4M | - | 135 | 125 | +$3.6M | +$0 bull / -$244k bear | out (clean 25, ADX 16, RVol 0.6) |
| 11 | **SHOP** | 160.00 | - | **-** | 18 | - | NEG -$424k | - | 175 | 175 | -$727k | - | out (clean 28, ADX 24, RVol 0.8) |
| 12 | **META** | 612.30 | - | **-** | 17 | - | NEG -$119.4M | 623.37 | 650 | 610 | +$9.7M | +$0 bull / -$239k bear | out (clean 29, ADX 19, RVol 0.3) |
| 13 | **ORCL** | 121.77 | - | **-** | 17 | - | NEG -$37.2M | - | 130 | 120 | -$344k | +$221k bull / +$0 bear | out (clean 31, ADX 32, RVol 0.4) |
| 14 | **SPY** | 758.47 | - | **-** | 16 | - | NEG -$10.0B | 774.45 | 800 | 750 | +$28.7M | +$4.3M bull / +$0 bear | out (clean 30, ADX 22, RVol 0.6) |
| 15 | **QQQ** | 691.08 | - | **-** | 16 | - | NEG -$5.5B | 732.54 | 720 | 680 | +$48.2M | +$338k bull / +$0 bear | out (clean 30, ADX 23, RVol 0.4) |
| 16 | **NVDA** | 206.58 | - | **-** | 16 | - | NEG -$212.7M | 215.31 | 210 | 200 | +$6.6M | +$784k bull / -$475k bear | out (clean 28, ADX 14, RVol 1.1) |
| 17 | **PLTR** | 184.25 | - | **-** | 16 | - | NEG -$11.1M | - | 200 | 180 | +$2.6M | +$203k bull / -$144k bear | out (clean 25, ADX 14, RVol 0.6) |
| 18 | **HOOD** | 85.12 | - | **-** | 16 | - | NEG -$10.3M | - | 93 | 90 | -$219k | +$67k bull / +$0 bear | out (clean 32, ADX 26, RVol 0.5) |
| 19 | **IWM** | 281.00 | - | **-** | 15 | - | NEG -$1.0B | 286.71 | 285 | 270 | +$379k | +$53k bull / -$261k bear | out (clean 32, ADX 22, RVol 0.7) |
| 20 | **GOOGL** | 283.88 | - | **-** | 15 | - | NEG -$90.4M | - | 285 | 285 | -$2.4M | +$0 bull / -$2.7M bear | out (clean 34, ADX 15, RVol 0.3) |
| 21 | **BABA** | 102.97 | - | **-** | 14 | - | POS +$2.6M | 101.02 | 105 | 100 | -$1.0M | - | out (clean 33, ADX 20, RVol 0.9) |
| 22 | **UBER** | 67.25 | - | **-** | 13 | - | NEG -$8.4M | - | 70 | 65 | -$502k | - | out (clean 28, ADX 22, RVol 0.6) |
| 23 | **SMH** | 519.19 | - | **-** | 12 | - | NEG -$348.8M | - | 532.5 | 500 | +$3.5M | - | out (clean 31, ADX 23, RVol 0.5) |
| 24 | **NFLX** | 62.58 | - | **-** | 8 | - | NEG -$21.2M | - | 63 | 60 | -$280k | - | out (clean 28, ADX 28, RVol 0.5) |
| 25 | **AVGO** | 329.22 | - | **-** | 8 | - | NEG -$101.8M | - | 340 | 330 | -$5.0M | - | out (clean 31, ADX 17, RVol 0.3) |
| 26 | **COIN** | 139.10 | - | **-** | 7 | - | NEG -$7.8M | - | 150 | 130 | -$352k | - | out (clean 23, ADX 11, RVol 0.5) |
| 27 | **CRM** | 231.74 | - | **-** | 5 | - | NEG -$5.5M | 242.32 | 240 | 220 | +$46k | - | out (clean 26, ADX 10, RVol 0.6) |

## Big prints this scan (76)
- **AAPL** PUT 335 2026-11-06 (4DTE): 1,464 @ 6.80 = **+$996k** SELL | vol 5,543 / OI 7,284
- **AAPL** PUT 330 2026-11-06 (4DTE): 488 @ 5.06 = **+$247k** SELL | vol 11,757 / OI 10,211
- **GOOGL** CALL 287.5 2026-11-09 (7DTE): 600 @ 3.35 = **+$201k** SELL | vol 1,500 / OI 0
- **GOOGL** CALL 285 2026-11-06 (4DTE): 476 @ 3.90 = **+$186k** SELL | vol 9,053 / OI 2,236
- **SPY** PUT 759 2026-11-06 (4DTE): 313 @ 5.93 = **+$186k** SELL | vol 7,616 / OI 1,010
- **AAPL** PUT 325 2026-11-06 (4DTE): 488 @ 3.70 = **+$181k** SELL | vol 5,728 / OI 10,672
- **GOOGL** CALL 282.5 2026-11-06 (4DTE): 346 @ 5.20 = **+$180k** SELL | vol 2,831 / OI 445
- **GOOGL** CALL 287.5 2026-11-06 (4DTE): 600 @ 2.88 = **+$173k** SELL | vol 5,697 / OI 375
- **SPY** PUT 762 2026-11-06 (4DTE): 231 @ 7.34 = **+$170k** SELL | vol 9,035 / OI 7,408
- **SPY** PUT 762 2026-11-06 (4DTE): 230 @ 7.34 = **+$169k** SELL | vol 9,035 / OI 7,408
- **MU** PUT 855 2026-11-04 (2DTE): 80 @ 20.81 = **+$166k** SELL | vol 1,711 / OI 268
- **MU** PUT 875 2026-11-02 (0DTE): 80 @ 20.05 = **+$160k** SELL | vol 14,809 / OI 366
- **AAPL** PUT 330 2026-11-06 (4DTE): 300 @ 4.92 = **+$148k** SELL | vol 11,757 / OI 10,211
- **GOOGL** CALL 287.5 2026-11-06 (4DTE): 512 @ 2.87 = **+$147k** SELL | vol 5,697 / OI 375
- **AAPL** PUT 330 2026-11-04 (2DTE): 300 @ 4.37 = **+$131k** SELL | vol 16,939 / OI 3,455

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 740 2026-11-02 (0DTE): 4,032 traded vs OI 3,574
- **SPY** CALL 785 2026-11-16 (14DTE): 602 traded vs OI 0
- **SPY** CALL 780 2026-11-16 (14DTE): 595 traded vs OI 0
- **QQQ** CALL 730 2026-11-05 (3DTE): 1,338 traded vs OI 1,280
- **IWM** CALL 289 2026-11-06 (4DTE): 6,960 traded vs OI 4,719
- **IWM** PUT 281 2026-11-11 (9DTE): 541 traded vs OI 111
- **IWM** PUT 281 2026-11-09 (7DTE): 501 traded vs OI 82
- **IWM** CALL 282 2026-11-09 (7DTE): 570 traded vs OI 203
- **IWM** CALL 282.5 2026-11-06 (4DTE): 1,022 traded vs OI 935
- **NVDA** PUT 200 2026-11-11 (9DTE): 761 traded vs OI 537
- **NVDA** CALL 197.5 2026-11-09 (7DTE): 542 traded vs OI 0
- **META** CALL 607.5 2026-11-02 (0DTE): 534 traded vs OI 64
- **AMZN** CALL 242.5 2026-11-04 (2DTE): 510 traded vs OI 51
- **AMZN** CALL 257.5 2026-11-20 (18DTE): 1,222 traded vs OI 1,218
- **GOOGL** CALL 285 2026-11-13 (11DTE): 547 traded vs OI 538

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
