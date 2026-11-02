# GEX + FLOW SCAN - Mon Nov 02, 02:10 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (2)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 12:03 | **QQQ** | **PUTS** | 1m FAILED POP (R3) | 11/02 691P | 0.65 | 1.48 | +291% (43m) | **+128%** (done) | +11% | 692.76 hit |
| 11:37 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/02 691P | 0.71 | 1.27 | +111% (58m) | **+79%** (done) | +12% | 693.07 hit |

## 1m RULES on SPY / QQQ - loose (4 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 14:10:08 ET, last candle SPY 14:09, QQQ 14:09 | no errors
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
| 1 | **MU** | 843.95 | FLOW SURGE | **CALLS** | 41 | none: 136 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (60 contracts' greeks worked out here) | NEG -$225.9M | - | 910 | 850 | +$160.5M | +$3.7M bull / -$33k bear | out (clean 31, ADX 46, RVol 0.7) |
| 2 | **SMCI** | 31.07 | TREND (flow not with it) | **PUTS** | 38 | none: 13 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$440k | - | 34 | 30 | +$861k | - | SHORT (clean 35, ADX 49, RVol 1.2) |
| 3 | **SMH** | 515.28 | - | **-** | 27 | - | NEG -$345.9M | - | 532.5 | 500 | +$4.8M | +$470k bull / +$0 bear | out (clean 31, ADX 36, RVol 1.0) |
| 4 | **AMD** | 476.13 | - | **-** | 27 | - | NEG -$72.5M | - | 500 | 480 | +$44.8M | +$1.3M bull / -$144k bear | out (clean 32, ADX 50, RVol 0.9) |
| 5 | **AAPL** | 337.04 | - | **-** | 24 | - | NEG -$794k | 337.02 | 350 | 330 | +$23.3M | +$106k bull / -$727k bear | out (clean 31, ADX 33, RVol 0.9) |
| 6 | **DELL** | 402.75 | TREND (flow not with it) | **PUTS** | 24 | none: 32 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$20.4M | - | 440 | 400 | +$1.1M | +$26k bull / +$0 bear | SHORT (clean 34, ADX 35, RVol 0.7) |
| 7 | **AMZN** | 248.81 | - | **-** | 21 | - | POS +$68.7M | 242.85 | 250 | 250 | -$19.7M | +$262k bull / +$0 bear | out (clean 34, ADX 30, RVol 0.5) |
| 8 | **QQQ** | 687.69 | - | **-** | 20 | - | NEG -$5.4B | - | 720 | 680 | +$106.2M | +$8.5M bull / +$0 bear | out (clean 30, ADX 35, RVol 0.6) |
| 9 | **MSTR** | 132.22 | - | **-** | 20 | - | POS +$1.3M | - | 135 | 125 | +$4.2M | +$27k bull / -$86k bear | out (clean 26, ADX 17, RVol 0.8) |
| 10 | **TSLA** | 406.15 | - | **-** | 19 | - | POS +$284.2M | - | 410 | 400 | -$63.7M | +$1.0M bull / -$32k bear | out (clean 31, ADX 22, RVol 0.9) |
| 11 | **MSFT** | 517.21 | - | **-** | 19 | - | POS +$175.6M | 502.46 | 540 | 500 | -$214k | +$144k bull / +$0 bear | out (clean 27, ADX 40, RVol 0.7) |
| 12 | **PLTR** | 182.81 | - | **-** | 19 | - | NEG -$11.3M | - | 200 | 180 | +$3.7M | +$272k bull / +$0 bear | out (clean 25, ADX 21, RVol 0.9) |
| 13 | **ORCL** | 120.48 | - | **-** | 19 | - | NEG -$36.6M | - | 130 | 120 | +$394k | +$255k bull / -$64k bear | out (clean 32, ADX 37, RVol 0.9) |
| 14 | **SPY** | 756.41 | - | **-** | 18 | - | NEG -$10.4B | 775.35 | 800 | 750 | +$65.8M | +$3.7M bull / +$0 bear | out (clean 30, ADX 32, RVol 0.6) |
| 15 | **IWM** | 280.43 | - | **-** | 18 | - | NEG -$1.2B | 286.82 | 285 | 270 | +$2.2M | +$290k bull / +$0 bear | out (clean 32, ADX 31, RVol 0.8) |
| 16 | **NVDA** | 205.16 | - | **-** | 18 | - | NEG -$224.5M | 215.41 | 210 | 205 | +$11.5M | +$816k bull / +$0 bear | out (clean 28, ADX 25, RVol 0.9) |
| 17 | **HOOD** | 84.47 | - | **-** | 18 | - | NEG -$11.4M | - | 85 | 90 | +$252k | +$191k bull / +$0 bear | out (clean 32, ADX 35, RVol 0.5) |
| 18 | **SHOP** | 158.71 | - | **-** | 17 | - | NEG -$287k | - | 170 | 160 | -$629k | - | out (clean 29, ADX 20, RVol 1.7) |
| 19 | **META** | 611.21 | - | **-** | 16 | - | NEG -$123.0M | 622.99 | 650 | 610 | +$9.1M | +$565k bull / +$0 bear | out (clean 29, ADX 17, RVol 0.3) |
| 20 | **GOOGL** | 283.53 | - | **-** | 16 | - | NEG -$81.9M | - | 285 | 285 | -$3.3M | +$239k bull / +$0 bear | out (clean 34, ADX 16, RVol 0.4) |
| 21 | **BABA** | 102.56 | - | **-** | 14 | - | POS +$1.9M | 101.16 | 105 | 100 | -$994k | - | out (clean 33, ADX 22, RVol 1.0) |
| 22 | **ARM** | 199.97 | - | **-** | 13 | - | NEG -$5.8M | - | 200 | 200 | +$281k | - | out (clean 25, ADX 26, RVol 0.9) |
| 23 | **UBER** | 66.89 | - | **-** | 12 | - | NEG -$8.5M | - | 70 | 65 | -$418k | - | out (clean 28, ADX 27, RVol 0.7) |
| 24 | **NFLX** | 62.77 | - | **-** | 11 | - | NEG -$19.7M | - | 63 | 60 | -$654k | - | out (clean 29, ADX 32, RVol 0.7) |
| 25 | **CRM** | 229.66 | - | **-** | 10 | - | NEG -$6.4M | 243.09 | 240 | 220 | +$70k | - | out (clean 27, ADX 21, RVol 1.3) |
| 26 | **COIN** | 137.94 | - | **-** | 9 | - | NEG -$7.6M | - | 150 | 130 | -$274k | - | out (clean 24, ADX 22, RVol 0.9) |
| 27 | **AVGO** | 325.95 | - | **-** | 8 | - | NEG -$111.2M | - | 340 | 330 | -$3.0M | - | out (clean 30, ADX 26, RVol 0.4) |

## Big prints this scan (70)
- **SPY** CALL 760 2026-11-06 (4DTE): 500 @ 5.33 = **+$266k** BUY | vol 13,900 / OI 1,345
- **QQQ** PUT 692 2026-11-02 (0DTE): 731 @ 3.50 = **+$256k** SELL | vol 163,336 / OI 0
- **SPY** PUT 758 2026-11-02 (0DTE): 1,199 @ 1.74 = **+$209k** SELL | vol 382,293 / OI 1,174
- **QQQ** PUT 692 2026-11-02 (0DTE): 500 @ 3.30 = **+$165k** SELL | vol 163,336 / OI 0
- **SPY** CALL 762 2026-11-03 (1DTE): 1,185 @ 1.31 = **+$155k** BUY | vol 32,781 / OI 183
- **SPY** CALL 760 2026-11-06 (4DTE): 273 @ 5.33 = **+$146k** BUY | vol 13,900 / OI 1,345
- **SPY** PUT 757 2026-11-03 (1DTE): 490 @ 2.90 = **+$142k** SELL | vol 24,651 / OI 386
- **SMH** PUT 507.5 2026-11-04 (2DTE): 248 @ 5.58 = **+$138k** SELL | vol 408 / OI 19
- **SMH** PUT 505 2026-11-04 (2DTE): 248 @ 4.90 = **+$122k** SELL | vol 431 / OI 10
- **QQQ** PUT 690 2026-11-02 (0DTE): 543 @ 2.05 = **+$111k** SELL | vol 234,182 / OI 2,736
- **QQQ** PUT 691 2026-11-02 (0DTE): 399 @ 2.70 = **+$108k** SELL | vol 150,915 / OI 0
- **MU** CALL 825 2026-11-09 (7DTE): 24 @ 43.50 = **+$104k** BUY | vol 59 / OI 1
- **QQQ** PUT 689 2026-11-06 (4DTE): 100 @ 10.03 = **+$100k** SELL | vol 917 / OI 1,006
- **SPY** CALL 757 2026-11-02 (0DTE): 700 @ 1.43 = **+$100k** BUY | vol 45,403 / OI 68
- **MU** CALL 885 2026-11-09 (7DTE): 65 @ 14.85 = **+$97k** BUY | vol 1,422 / OI 4

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 727 2026-11-06 (4DTE): 853 traded vs OI 787
- **SPY** PUT 746 2026-11-06 (4DTE): 1,075 traded vs OI 1,074
- **SPY** CALL 754 2026-11-03 (1DTE): 506 traded vs OI 25
- **SPY** CALL 785 2026-11-12 (10DTE): 544 traded vs OI 477
- **SMH** CALL 525 2026-11-06 (4DTE): 549 traded vs OI 228
- **AMD** CALL 490 2026-11-20 (18DTE): 812 traded vs OI 641
- **AMD** PUT 487.5 2026-11-04 (2DTE): 504 traded vs OI 27
- **AMZN** PUT 235 2026-11-09 (7DTE): 503 traded vs OI 128
- **MSFT** CALL 535 2026-11-06 (4DTE): 1,341 traded vs OI 1,325
- **GOOGL** CALL 302.5 2026-11-04 (2DTE): 773 traded vs OI 337
- **AVGO** CALL 347.5 2026-11-06 (4DTE): 598 traded vs OI 596
- **PLTR** CALL 200 2026-11-06 (4DTE): 4,186 traded vs OI 4,152
- **MU** PUT 790 2026-11-02 (0DTE): 699 traded vs OI 0
- **MSTR** PUT 119 2026-11-06 (4DTE): 523 traded vs OI 0
- **ORCL** PUT 109 2026-11-06 (4DTE): 2,028 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
