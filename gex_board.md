# GEX + FLOW SCAN - Mon Nov 02, 03:35 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (2)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 12:03 | **QQQ** | **PUTS** | 1m FAILED POP (R3) | 11/02 691P | 0.65 | 1.48 | +291% (43m) | **+128%** (done) | +11% | 692.76 hit |
| 11:37 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/02 691P | 0.71 | 1.27 | +111% (58m) | **+79%** (done) | +12% | 693.07 hit |

## 1m RULES on SPY / QQQ - loose (7 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 15:32:08 ET, last candle SPY 15:31, QQQ 15:31 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 14:28 | QQQ | 1m WHIPSAW | R1 R2 | CALLS | TURNING your way | no contract: 75 calls 0-1DTE > 6 priced 0.40-0.80 > 2 delta 0.15+ > 2 spread ok > 2 liquid |
| 14:26 | QQQ | 1m WHIPSAW | R1 R2 | PUTS | WITH you | no contract: 75 puts 0-1DTE > 4 priced 0.40-0.80 > 2 delta 0.15+ > 2 spread ok > 2 liquid  |
| 14:16 | SPY | 1m WHIPSAW | R1 | PUTS | TURNING away | no contract: 92 puts 0-1DTE > 6 priced 0.40-0.80 > 3 delta 0.15+ > 3 spread ok > 3 liquid  |
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
| 1 | **MSFT** | 509.82 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 45 | none: 162 calls 0-7DTE > 8 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (68 contracts' greeks worked out here) | POS +$59.7M | 503.02 | 535 | 510 | +$6.9M | +$826k bull / +$0 bear | out (clean 28, ADX 60, RVol 1.2) |
| 2 | **SMH** | 508.17 | FLOW SURGE | **CALLS** | 40 | none: 160 calls 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (71 contracts' greeks worked out here) | NEG -$343.7M | - | 532.5 | 500 | +$9.9M | +$804k bull / -$33k bear | out (clean 33, ADX 50, RVol 0.6) |
| 3 | **MU** | 832.65 | - | **-** | 30 | - | NEG -$241.4M | - | 910 | 850 | +$188.6M | +$5.6M bull / -$900k bear | out (clean 32, ADX 47, RVol 1.4) |
| 4 | **AMD** | 468.24 | - | **-** | 28 | - | NEG -$109.2M | - | 430 | 440 | +$54.4M | +$1.6M bull / +$0 bear | out (clean 33, ADX 58, RVol 1.5) |
| 5 | **QQQ** | 682.09 | - | **-** | 24 | - | NEG -$5.3B | - | 720 | 680 | +$223.5M | +$6.7M bull / -$167k bear | out (clean 32, ADX 50, RVol 0.8) |
| 6 | **SPY** | 753.18 | - | **-** | 23 | - | NEG -$10.7B | 775.52 | 770 | 750 | +$192.2M | +$3.9M bull / +$0 bear | out (clean 31, ADX 43, RVol 1.1) |
| 7 | **NVDA** | 202.46 | - | **-** | 23 | - | NEG -$254.3M | - | 210 | 200 | +$23.7M | +$575k bull / +$0 bear | out (clean 30, ADX 40, RVol 1.1) |
| 8 | **AMZN** | 246.50 | - | **-** | 23 | - | POS +$45.1M | 243 | 250 | 250 | -$16.1M | +$164k bull / +$0 bear | out (clean 34, ADX 43, RVol 0.9) |
| 9 | **PLTR** | 180.28 | - | **-** | 23 | - | NEG -$13.3M | - | 165 | 180 | +$5.5M | +$451k bull / -$212k bear | out (clean 27, ADX 42, RVol 0.9) |
| 10 | **DELL** | 393.28 | - | **-** | 23 | - | NEG -$20.3M | - | 430 | 400 | +$3.0M | +$194k bull / +$0 bear | out (clean 34, ADX 46, RVol 0.8) |
| 11 | **AAPL** | 338.84 | - | **-** | 22 | - | POS +$26.3M | 336.86 | 350 | 330 | +$21.6M | +$1.4M bull / -$1.4M bear | out (clean 32, ADX 26, RVol 1.3) |
| 12 | **MSTR** | 130.29 | - | **-** | 22 | - | NEG -$2.2M | 137.59 | 135 | 125 | +$4.5M | +$62k bull / +$0 bear | out (clean 26, ADX 32, RVol 1.0) |
| 13 | **ORCL** | 119.48 | - | **-** | 21 | - | NEG -$43.6M | - | 130 | 120 | +$756k | +$0 bull / -$26k bear | out (clean 33, ADX 35, RVol 1.8) |
| 14 | **SHOP** | 155.49 | - | **-** | 21 | - | NEG -$459k | - | 170 | 160 | -$101k | +$29k bull / +$0 bear | out (clean 30, ADX 35, RVol 1.7) |
| 15 | **IWM** | 279.63 | - | **-** | 20 | - | NEG -$1.3B | 287.06 | 285 | 270 | +$6.7M | +$129k bull / -$108k bear | out (clean 33, ADX 30, RVol 1.2) |
| 16 | **TSLA** | 402.07 | - | **-** | 19 | - | POS +$189.6M | - | 400 | 400 | -$22.8M | +$3.5M bull / +$0 bear | out (clean 32, ADX 40, RVol 0.6) |
| 17 | **NFLX** | 62.35 | - | **-** | 19 | - | NEG -$21.8M | - | 63 | 60 | -$613k | +$28k bull / +$0 bear | out (clean 29, ADX 26, RVol 0.8) |
| 18 | **HOOD** | 83.85 | - | **-** | 19 | - | NEG -$11.2M | - | 85 | 90 | +$695k | +$0 bull / -$78k bear | out (clean 32, ADX 30, RVol 0.8) |
| 19 | **AVGO** | 322.91 | - | **-** | 18 | - | NEG -$116.9M | - | 340 | 320 | -$1.5M | +$171k bull / +$0 bear | out (clean 32, ADX 34, RVol 0.6) |
| 20 | **SMCI** | 30.59 | - | **-** | 18 | - | NEG -$992k | - | 33 | 30 | +$903k | - | out (clean 36, ADX 42, RVol 1.5) |
| 21 | **META** | 609.89 | - | **-** | 16 | - | NEG -$147.4M | 625.28 | 650 | 610 | +$11.7M | +$968k bull / +$0 bear | out (clean 28, ADX 12, RVol 0.4) |
| 22 | **GOOGL** | 281.80 | - | **-** | 16 | - | NEG -$108.6M | - | 285 | 280 | -$1.9M | +$30k bull / +$0 bear | out (clean 33, ADX 19, RVol 0.8) |
| 23 | **ARM** | 197.85 | - | **-** | 16 | - | NEG -$6.5M | - | 200 | 200 | +$273k | - | out (clean 26, ADX 34, RVol 2.5) |
| 24 | **BABA** | 101.88 | - | **-** | 16 | - | POS +$581k | 101.43 | 105 | 100 | -$936k | - | out (clean 33, ADX 41, RVol 0.8) |
| 25 | **UBER** | 66.72 | - | **-** | 15 | - | NEG -$8.0M | - | 70 | 65 | -$399k | - | out (clean 29, ADX 35, RVol 1.5) |
| 26 | **CRM** | 226.57 | - | **-** | 14 | - | NEG -$10.5M | - | 240 | 220 | +$106k | - | out (clean 28, ADX 38, RVol 1.4) |
| 27 | **COIN** | 136.58 | - | **-** | 10 | - | NEG -$8.3M | - | 150 | 130 | -$215k | - | out (clean 25, ADX 40, RVol 0.7) |

## Big prints this scan (103)
- **SPY** CALL 750 2026-11-05 (3DTE): 572 @ 9.04 = **+$517k** BUY | vol 1,187 / OI 13
- **SPY** CALL 750 2026-11-05 (3DTE): 428 @ 9.04 = **+$387k** BUY | vol 1,187 / OI 13
- **SPY** PUT 767 2026-11-04 (2DTE): 227 @ 13.27 = **+$301k** SELL | vol 6,730 / OI 36,998
- **QQQ** PUT 675 2026-11-04 (2DTE): 685 @ 4.33 = **+$297k** SELL | vol 11,460 / OI 442
- **QQQ** PUT 680 2026-11-04 (2DTE): 480 @ 5.99 = **+$288k** SELL | vol 9,366 / OI 670
- **SPY** PUT 745 2026-11-06 (4DTE): 436 @ 3.45 = **+$150k** SELL | vol 12,851 / OI 12,695
- **SPY** PUT 745 2026-11-06 (4DTE): 419 @ 3.48 = **+$146k** SELL | vol 12,851 / OI 12,695
- **MU** CALL 855 2026-11-06 (4DTE): 65 @ 20.92 = **+$136k** BUY | vol 983 / OI 50
- **SPY** PUT 755 2026-11-03 (1DTE): 400 @ 3.34 = **+$134k** SELL | vol 45,121 / OI 3,155
- **SPY** PUT 735 2026-11-05 (3DTE): 1,023 @ 1.29 = **+$132k** SELL | vol 22,850 / OI 858
- **MU** CALL 860 2026-11-04 (2DTE): 100 @ 12.70 = **+$127k** BUY | vol 2,726 / OI 37
- **SPY** PUT 745 2026-11-06 (4DTE): 345 @ 3.46 = **+$119k** SELL | vol 12,851 / OI 12,695
- **SPY** PUT 761 2026-11-02 (0DTE): 181 @ 6.24 = **+$113k** SELL | vol 189,492 / OI 875
- **NVDA** PUT 197.5 2026-11-06 (4DTE): 500 @ 2.03 = **+$102k** SELL | vol 14,751 / OI 3,622
- **AMD** CALL 475 2026-11-04 (2DTE): 49 @ 20.25 = **+$99k** BUY | vol 478 / OI 0

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 745 2026-11-06 (4DTE): 12,851 traded vs OI 12,695
- **SPY** CALL 755 2026-11-13 (11DTE): 682 traded vs OI 410
- **SPY** PUT 757 2026-11-30 (28DTE): 601 traded vs OI 515
- **QQQ** PUT 615 2026-11-20 (18DTE): 4,432 traded vs OI 0
- **QQQ** CALL 707 2026-11-20 (18DTE): 504 traded vs OI 327
- **IWM** CALL 282.5 2026-11-13 (11DTE): 835 traded vs OI 497
- **NVDA** CALL 182.5 2026-11-06 (4DTE): 556 traded vs OI 0
- **NVDA** PUT 182.5 2026-11-06 (4DTE): 674 traded vs OI 0
- **AAPL** CALL 360 2026-11-27 (25DTE): 1,741 traded vs OI 1,507
- **AMD** PUT 472.5 2026-11-04 (2DTE): 506 traded vs OI 17
- **MSFT** PUT 505 2026-11-04 (2DTE): 640 traded vs OI 207
- **ORCL** CALL 119 2026-11-06 (4DTE): 513 traded vs OI 36
- **ORCL** PUT 108 2026-11-06 (4DTE): 571 traded vs OI 356
- **SHOP** PUT 140 2026-11-06 (4DTE): 630 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
