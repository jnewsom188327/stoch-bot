# GEX + FLOW SCAN - Mon Nov 02, 12:30 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (2)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 12:03 | **QQQ** | **PUTS** | 1m FAILED POP (R3) | 11/02 691P | 0.65 | 1.07 | +71% (25m) | **+65%** | +11% | 692.76 hit |
| 11:37 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/02 691P | 0.71 | 1.07 | +56% (51m) | **+51%** | +12% | 693.07 hit |

## 1m RULES on SPY / QQQ - loose (4 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 12:30:08 ET, last candle SPY 12:29, QQQ 12:29 | no errors
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
| 1 | **SHOP** | 159.98 | FLOW SURGE | **PUTS** | 44 | none: 17 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$338k | - | 175 | 175 | -$781k | +$0 bull / -$185k bear | out (clean 28, ADX 20, RVol 1.0) |
| 2 | **MU** | 855.61 | FLOW SURGE | **CALLS** | 42 | none: 140 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (55 contracts' greeks worked out here) | NEG -$225.9M | - | 910 | 850 | +$112.4M | +$6.4M bull / -$88k bear | out (clean 30, ADX 32, RVol 1.1) |
| 3 | **TSLA** | 409.37 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 37 | none: 132 puts 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (54 contracts' greeks worked out here) | POS +$320.6M | - | 410 | 400 | -$77.6M | +$725k bull / -$445k bear | out (clean 30, ADX 30, RVol 0.4) |
| 4 | **SMCI** | 31.95 | TREND (flow not with it) | **PUTS** | 29 | none: 13 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$89k | - | 35 | 30 | +$325k | +$26k bull / +$0 bear | SHORT (clean 33, ADX 32, RVol 1.0) |
| 5 | **AAPL** | 337.26 | - | **-** | 25 | - | NEG -$4.8M | 336.95 | 350 | 330 | +$19.3M | +$1.8M bull / +$0 bear | out (clean 31, ADX 29, RVol 1.1) |
| 6 | **AMD** | 487.62 | - | **-** | 24 | - | NEG -$86.5M | - | 500 | 500 | +$27.9M | +$597k bull / -$326k bear | out (clean 31, ADX 31, RVol 0.6) |
| 7 | **AMZN** | 250.88 | - | **-** | 24 | - | POS +$98.2M | 242.67 | 250 | 250 | -$22.7M | +$75k bull / -$51k bear | out (clean 33, ADX 36, RVol 0.4) |
| 8 | **MSTR** | 133.46 | - | **-** | 21 | - | POS +$2.4M | - | 135 | 125 | +$3.3M | +$260k bull / +$0 bear | out (clean 26, ADX 26, RVol 0.8) |
| 9 | **META** | 610.31 | - | **-** | 20 | - | NEG -$141.4M | 626.22 | 650 | 610 | +$11.8M | +$240k bull / -$47k bear | out (clean 29, ADX 29, RVol 0.3) |
| 10 | **MSFT** | 520.17 | - | **-** | 19 | - | POS +$230.5M | 501.8 | 540 | 500 | -$1.6M | +$382k bull / +$0 bear | out (clean 26, ADX 25, RVol 1.4) |
| 11 | **BABA** | 103.24 | - | **-** | 19 | - | POS +$2.5M | 101.13 | 105 | 100 | -$1.1M | - | out (clean 33, ADX 34, RVol 1.2) |
| 12 | **ORCL** | 122.50 | - | **-** | 18 | - | NEG -$38.0M | - | 130 | 120 | -$327k | +$61k bull / -$31k bear | out (clean 32, ADX 30, RVol 0.8) |
| 13 | **PLTR** | 184.20 | - | **-** | 17 | - | NEG -$11.4M | - | 200 | 180 | +$2.6M | +$84k bull / +$0 bear | out (clean 25, ADX 11, RVol 0.8) |
| 14 | **NVDA** | 206.64 | - | **-** | 16 | - | NEG -$208.7M | 215.35 | 210 | 200 | +$8.3M | +$781k bull / +$0 bear | out (clean 29, ADX 15, RVol 0.6) |
| 15 | **GOOGL** | 282.50 | - | **-** | 16 | - | NEG -$92.3M | - | 285 | 290 | +$2.5M | +$137k bull / +$0 bear | out (clean 34, ADX 17, RVol 0.4) |
| 16 | **UBER** | 67.44 | - | **-** | 16 | - | NEG -$8.0M | - | 70 | 65 | -$503k | - | out (clean 28, ADX 34, RVol 0.7) |
| 17 | **QQQ** | 692.36 | - | **-** | 15 | - | NEG -$5.7B | 733.27 | 720 | 680 | +$30.3M | +$1.2M bull / -$492k bear | out (clean 30, ADX 17, RVol 0.3) |
| 18 | **IWM** | 281.73 | - | **-** | 15 | - | NEG -$964.3M | 286.58 | 285 | 270 | -$413k | +$0 bull / -$300k bear | out (clean 31, ADX 22, RVol 0.4) |
| 19 | **NFLX** | 62.48 | - | **-** | 15 | - | NEG -$21.3M | - | 63 | 60 | +$18k | +$0 bull / -$73k bear | out (clean 28, ADX 20, RVol 0.5) |
| 20 | **SPY** | 759.03 | - | **-** | 14 | - | NEG -$10.0B | 775.19 | 800 | 750 | -$3.7M | +$2.1M bull / +$0 bear | out (clean 29, ADX 18, RVol 0.5) |
| 21 | **SMH** | 521.77 | - | **-** | 12 | - | NEG -$347.4M | - | 532.5 | 500 | +$3.0M | - | out (clean 31, ADX 19, RVol 0.5) |
| 22 | **AVGO** | 330.45 | - | **-** | 10 | - | NEG -$101.2M | - | 340 | 330 | -$5.8M | - | out (clean 30, ADX 23, RVol 0.3) |
| 23 | **ARM** | 203.94 | - | **-** | 9 | - | NEG -$7.2M | - | 220 | 200 | +$185k | - | out (clean 25, ADX 12, RVol 0.5) |
| 24 | **CRM** | 232.46 | - | **-** | 8 | - | NEG -$5.2M | 242.04 | 240 | 220 | +$76k | - | out (clean 27, ADX 12, RVol 0.5) |
| 25 | **COIN** | 139.36 | - | **-** | 7 | - | NEG -$7.9M | - | 150 | 130 | -$315k | - | out (clean 24, ADX 12, RVol 0.7) |
| 26 | **HOOD** | 85.78 | - | **-** | 6 | - | NEG -$9.2M | - | 93 | 90 | -$287k | - | out (clean 31, ADX 24, RVol 0.3) |
| 27 | **DELL** | 412.11 | - | **-** | 5 | - | NEG -$23.2M | - | 440 | 400 | +$779k | - | out (clean 33, ADX 14, RVol 0.6) |

## Big prints this scan (85)
- **SPY** PUT 767 2026-11-04 (2DTE): 500 @ 8.50 = **+$425k** SELL | vol 2,449 / OI 36,998
- **MU** CALL 850 2026-11-06 (4DTE): 129 @ 31.80 = **+$410k** BUY | vol 1,038 / OI 203
- **SPY** PUT 765 2026-11-05 (3DTE): 500 @ 8.00 = **+$400k** SELL | vol 5,471 / OI 2,269
- **QQQ** PUT 720 2026-11-06 (4DTE): 141 @ 27.75 = **+$391k** SELL | vol 331 / OI 10,591
- **MU** CALL 850 2026-11-06 (4DTE): 100 @ 31.80 = **+$318k** BUY | vol 1,038 / OI 203
- **MSFT** CALL 545 2026-11-06 (4DTE): 3,000 @ 0.97 = **+$291k** BUY | vol 4,685 / OI 2,578
- **MU** PUT 850 2026-11-06 (4DTE): 100 @ 24.00 = **+$240k** SELL | vol 1,921 / OI 1,436
- **NVDA** CALL 207.5 2026-11-06 (4DTE): 468 @ 3.85 = **+$180k** BUY | vol 6,512 / OI 327
- **SPY** PUT 770 2026-11-03 (1DTE): 155 @ 10.37 = **+$161k** SELL | vol 1,047 / OI 1,238
- **SPY** CALL 760 2026-11-02 (0DTE): 1,400 @ 1.12 = **+$157k** BUY | vol 189,968 / OI 467
- **QQQ** CALL 694 2026-11-04 (2DTE): 200 @ 6.82 = **+$136k** BUY | vol 4,614 / OI 0
- **MU** CALL 860 2026-11-06 (4DTE): 52 @ 26.15 = **+$136k** BUY | vol 620 / OI 130
- **QQQ** CALL 694 2026-11-04 (2DTE): 200 @ 6.68 = **+$134k** BUY | vol 4,614 / OI 0
- **MSTR** PUT 136 2026-11-06 (4DTE): 191 @ 6.20 = **+$118k** SELL | vol 1,829 / OI 424
- **MU** CALL 850 2026-11-02 (0DTE): 100 @ 10.25 = **+$102k** BUY | vol 874 / OI 56

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 758 2026-11-04 (2DTE): 3,748 traded vs OI 3,730
- **QQQ** CALL 705 2026-11-09 (7DTE): 658 traded vs OI 116
- **QQQ** PUT 680 2026-11-10 (8DTE): 521 traded vs OI 281
- **SMH** PUT 470 2026-11-06 (4DTE): 2,281 traded vs OI 0
- **SMH** PUT 470 2026-11-20 (18DTE): 2,971 traded vs OI 0
- **NVDA** PUT 187.5 2026-11-04 (2DTE): 548 traded vs OI 268
- **NVDA** PUT 192.5 2026-11-09 (7DTE): 548 traded vs OI 0
- **AAPL** CALL 352.5 2026-11-06 (4DTE): 1,064 traded vs OI 944
- **AAPL** PUT 312.5 2026-11-06 (4DTE): 932 traded vs OI 916
- **META** CALL 610 2026-11-04 (2DTE): 503 traded vs OI 42
- **MSFT** CALL 545 2026-11-06 (4DTE): 4,685 traded vs OI 2,578
- **MSFT** CALL 490 2026-11-06 (4DTE): 1,545 traded vs OI 149
- **NFLX** CALL 64 2026-11-06 (4DTE): 7,804 traded vs OI 7,671
- **AVGO** CALL 335 2026-11-06 (4DTE): 501 traded vs OI 318
- **SMCI** CALL 32 2026-11-06 (4DTE): 767 traded vs OI 649

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
