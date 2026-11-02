# GEX + FLOW SCAN - Mon Nov 02, 02:20 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (2)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 12:03 | **QQQ** | **PUTS** | 1m FAILED POP (R3) | 11/02 691P | 0.65 | 1.48 | +291% (43m) | **+128%** (done) | +11% | 692.76 hit |
| 11:37 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/02 691P | 0.71 | 1.27 | +111% (58m) | **+79%** (done) | +12% | 693.07 hit |

## 1m RULES on SPY / QQQ - loose (5 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 14:20:08 ET, last candle SPY 14:19, QQQ 14:19 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
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
| 1 | **MU** | 842.33 | FLOW SURGE | **CALLS** | 41 | none: 135 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (61 contracts' greeks worked out here) | NEG -$219.9M | - | 910 | 850 | +$160.4M | +$1.9M bull / -$1.0M bear | out (clean 31, ADX 47, RVol 0.7) |
| 2 | **TSLA** | 405.70 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 39 | none: 128 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (52 contracts' greeks worked out here) | POS +$261.9M | - | 405 | 400 | -$59.9M | +$2.0M bull / +$0 bear | out (clean 31, ADX 24, RVol 1.0) |
| 3 | **SMCI** | 30.84 | TREND (flow not with it) | **PUTS** | 39 | none: 12 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$573k | - | 33 | 30 | +$895k | - | SHORT (clean 35, ADX 51, RVol 1.3) |
| 4 | **SMH** | 513.79 | - | **-** | 27 | - | NEG -$339.8M | - | 532.5 | 500 | +$5.4M | +$505k bull / +$0 bear | out (clean 32, ADX 40, RVol 0.7) |
| 5 | **AMD** | 474.88 | - | **-** | 27 | - | NEG -$68.5M | - | 500 | 480 | +$46.5M | +$1.1M bull / +$0 bear | out (clean 32, ADX 53, RVol 1.0) |
| 6 | **DELL** | 401.16 | TREND (flow not with it) | **PUTS** | 26 | none: 31 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$20.1M | - | 440 | 400 | +$2.1M | +$985k bull / +$0 bear | SHORT (clean 34, ADX 37, RVol 0.7) |
| 7 | **AAPL** | 336.90 | - | **-** | 23 | - | NEG -$6.2M | 337.16 | 350 | 330 | +$23.7M | +$554k bull / +$0 bear | out (clean 31, ADX 32, RVol 0.9) |
| 8 | **QQQ** | 686.79 | - | **-** | 21 | - | NEG -$5.4B | - | 720 | 680 | +$121.0M | +$2.3M bull / +$0 bear | out (clean 31, ADX 39, RVol 0.7) |
| 9 | **AMZN** | 248.60 | - | **-** | 21 | - | POS +$65.4M | 242.81 | 250 | 250 | -$19.0M | +$60k bull / +$0 bear | out (clean 34, ADX 32, RVol 0.5) |
| 10 | **SPY** | 755.68 | - | **-** | 20 | - | NEG -$10.4B | 775.24 | 770 | 750 | +$92.6M | +$2.3M bull / +$0 bear | out (clean 30, ADX 36, RVol 0.6) |
| 11 | **MSTR** | 132.53 | - | **-** | 20 | - | POS +$1.5M | - | 135 | 125 | +$4.3M | +$27k bull / +$0 bear | out (clean 26, ADX 18, RVol 1.0) |
| 12 | **ORCL** | 120.01 | - | **-** | 20 | - | NEG -$36.1M | - | 130 | 120 | +$486k | +$80k bull / +$0 bear | out (clean 32, ADX 40, RVol 0.9) |
| 13 | **NVDA** | 204.72 | - | **-** | 19 | - | NEG -$232.0M | 215.66 | 210 | 205 | +$12.9M | +$1.0M bull / +$0 bear | out (clean 29, ADX 28, RVol 0.9) |
| 14 | **PLTR** | 182.72 | - | **-** | 19 | - | NEG -$11.1M | - | 200 | 180 | +$3.8M | +$350k bull / +$0 bear | out (clean 26, ADX 23, RVol 0.8) |
| 15 | **HOOD** | 84.30 | - | **-** | 19 | - | NEG -$11.3M | - | 85 | 90 | +$329k | +$191k bull / +$0 bear | out (clean 32, ADX 38, RVol 0.7) |
| 16 | **SHOP** | 158.98 | - | **-** | 17 | - | NEG -$308k | - | 170 | 165 | -$622k | - | out (clean 29, ADX 19, RVol 2.0) |
| 17 | **META** | 610.60 | - | **-** | 16 | - | NEG -$145.1M | 626.03 | 650 | 610 | +$9.6M | +$69k bull / +$0 bear | out (clean 29, ADX 17, RVol 0.3) |
| 18 | **BABA** | 102.44 | - | **-** | 15 | - | POS +$1.4M | 101.35 | 105 | 100 | -$982k | - | out (clean 33, ADX 24, RVol 1.1) |
| 19 | **ARM** | 199.28 | - | **-** | 13 | - | NEG -$5.8M | - | 200 | 200 | +$285k | - | out (clean 25, ADX 30, RVol 0.9) |
| 20 | **UBER** | 66.83 | - | **-** | 13 | - | NEG -$8.5M | - | 70 | 65 | -$409k | - | out (clean 28, ADX 30, RVol 1.0) |
| 21 | **NFLX** | 62.77 | - | **-** | 10 | - | NEG -$19.8M | - | 63 | 60 | -$706k | - | out (clean 29, ADX 30, RVol 0.6) |
| 22 | **CRM** | 228.69 | - | **-** | 10 | - | NEG -$7.1M | - | 240 | 220 | +$72k | - | out (clean 27, ADX 26, RVol 1.0) |
| 23 | **MSFT** | 516.62 | - | **-** | 9 | - | POS +$165.4M | 501.96 | 540 | 500 | +$186k | - | out (clean 27, ADX 43, RVol 0.5) |
| 24 | **COIN** | 137.72 | - | **-** | 9 | - | NEG -$7.5M | - | 150 | 130 | -$224k | - | out (clean 24, ADX 26, RVol 0.8) |
| 25 | **IWM** | 280.18 | - | **-** | 8 | - | NEG -$1.2B | 286.83 | 285 | 270 | +$2.6M | - | out (clean 32, ADX 32, RVol 0.6) |
| 26 | **AVGO** | 324.95 | - | **-** | 8 | - | NEG -$115.0M | - | 340 | 320 | -$2.7M | - | out (clean 31, ADX 30, RVol 0.5) |
| 27 | **GOOGL** | 283.02 | - | **-** | 5 | - | NEG -$87.3M | - | 285 | 290 | -$3.2M | - | out (clean 34, ADX 14, RVol 0.4) |

## Big prints this scan (74)
- **DELL** CALL 400 2026-11-06 (4DTE): 500 @ 18.67 = **+$934k** BUY | vol 713 / OI 25
- **MU** CALL 845 2026-11-06 (4DTE): 188 @ 27.30 = **+$513k** SELL | vol 603 / OI 22
- **SPY** PUT 767 2026-11-04 (2DTE): 250 @ 11.21 = **+$280k** SELL | vol 4,211 / OI 36,998
- **SPY** PUT 767 2026-11-04 (2DTE): 250 @ 11.00 = **+$275k** SELL | vol 4,211 / OI 36,998
- **QQQ** PUT 697 2026-11-03 (1DTE): 200 @ 10.58 = **+$212k** SELL | vol 8,517 / OI 0
- **QQQ** PUT 697 2026-11-03 (1DTE): 200 @ 10.40 = **+$208k** SELL | vol 8,517 / OI 0
- **MU** PUT 845 2026-11-09 (7DTE): 50 @ 33.00 = **+$165k** MID | vol 78 / OI 41
- **SPY** PUT 755 2026-11-02 (0DTE): 2,243 @ 0.72 = **+$161k** SELL | vol 264,226 / OI 3,901
- **SPY** PUT 757 2026-11-03 (1DTE): 480 @ 3.33 = **+$160k** SELL | vol 27,876 / OI 386
- **AMD** PUT 475 2026-11-06 (4DTE): 68 @ 23.05 = **+$157k** SELL | vol 524 / OI 899
- **NVDA** PUT 207.5 2026-11-06 (4DTE): 268 @ 5.40 = **+$145k** SELL | vol 5,976 / OI 2,759
- **QQQ** CALL 690 2026-11-04 (2DTE): 200 @ 6.92 = **+$138k** BUY | vol 2,540 / OI 35
- **QQQ** PUT 691 2026-11-02 (0DTE): 425 @ 3.25 = **+$138k** SELL | vol 153,447 / OI 0
- **SPY** PUT 755 2026-11-02 (0DTE): 1,885 @ 0.72 = **+$136k** SELL | vol 264,226 / OI 3,901
- **QQQ** PUT 687 2026-11-04 (2DTE): 180 @ 7.37 = **+$133k** SELL | vol 1,313 / OI 0

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 690 2026-11-04 (2DTE): 617 traded vs OI 107
- **SPY** PUT 738 2026-11-04 (2DTE): 525 traded vs OI 270
- **SPY** PUT 757 2026-11-13 (11DTE): 1,493 traded vs OI 859
- **QQQ** PUT 689 2026-11-06 (4DTE): 1,036 traded vs OI 1,006
- **QQQ** PUT 687 2026-11-06 (4DTE): 513 traded vs OI 337
- **QQQ** PUT 650 2026-11-03 (1DTE): 3,605 traded vs OI 3,479
- **QQQ** CALL 722 2026-11-03 (1DTE): 520 traded vs OI 518
- **QQQ** PUT 681 2026-11-04 (2DTE): 503 traded vs OI 0
- **QQQ** PUT 655 2026-11-09 (7DTE): 511 traded vs OI 453
- **QQQ** CALL 705 2026-11-16 (14DTE): 504 traded vs OI 0
- **IWM** CALL 286 2026-11-13 (11DTE): 506 traded vs OI 313
- **SMH** PUT 510 2026-11-20 (18DTE): 4,396 traded vs OI 4,085
- **SMH** CALL 530 2026-11-20 (18DTE): 1,330 traded vs OI 618
- **SMH** PUT 505 2026-11-04 (2DTE): 587 traded vs OI 10
- **NVDA** CALL 197.5 2026-11-04 (2DTE): 520 traded vs OI 74

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
