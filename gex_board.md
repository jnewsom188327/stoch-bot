# GEX + FLOW SCAN - Mon Nov 02, 02:30 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (2)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 12:03 | **QQQ** | **PUTS** | 1m FAILED POP (R3) | 11/02 691P | 0.65 | 1.48 | +291% (43m) | **+128%** (done) | +11% | 692.76 hit |
| 11:37 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/02 691P | 0.71 | 1.27 | +111% (58m) | **+79%** (done) | +12% | 693.07 hit |

## 1m RULES on SPY / QQQ - loose (7 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 14:30:08 ET, last candle SPY 14:29, QQQ 14:29 | no errors
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
| 1 | **MU** | 842.85 | FLOW SURGE | **CALLS** | 42 | none: 135 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (55 contracts' greeks worked out here) | NEG -$233.0M | - | 910 | 850 | +$165.5M | +$2.3M bull / -$1.0M bear | out (clean 31, ADX 48, RVol 0.8) |
| 2 | **SMH** | 513.25 | FLOW SURGE | **CALLS** | 41 | none: 162 calls 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (75 contracts' greeks worked out here) | NEG -$337.9M | - | 532.5 | 500 | +$7.1M | +$103k bull / +$0 bear | out (clean 32, ADX 45, RVol 0.8) |
| 3 | **TSLA** | 405.36 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 40 | none: 132 puts 0-7DTE > 5 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only +13% at the target (needs +20%) (50 contracts' greeks worked out here) | POS +$246.5M | - | 405 | 400 | -$51.2M | +$2.7M bull / +$0 bear | out (clean 31, ADX 28, RVol 1.1) |
| 4 | **SMCI** | 30.84 | TREND (flow not with it) | **PUTS** | 38 | none: 12 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$515k | - | 33 | 30 | +$878k | - | SHORT (clean 36, ADX 54, RVol 1.2) |
| 5 | **BABA** | 102.46 | TREND + FLOW | **PUTS** | 33 | none: 20 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (1 contracts' greeks worked out here) | POS +$1.9M | 100.96 | 105 | 100 | -$975k | - | SHORT (clean 33, ADX 28, RVol 0.7) |
| 6 | **DELL** | 399.77 | TREND (flow not with it) | **PUTS** | 29 | none: 31 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$19.8M | - | 430 | 400 | +$2.1M | +$985k bull / +$0 bear | SHORT (clean 34, ADX 40, RVol 0.9) |
| 7 | **AMD** | 474.00 | - | **-** | 28 | - | NEG -$68.4M | - | 500 | 480 | +$48.8M | +$1.4M bull / +$0 bear | out (clean 32, ADX 56, RVol 1.3) |
| 8 | **AAPL** | 336.87 | - | **-** | 25 | - | NEG -$9.6M | 337.25 | 350 | 330 | +$25.6M | +$651k bull / +$0 bear | out (clean 31, ADX 32, RVol 1.4) |
| 9 | **SHOP** | 157.97 | - | **-** | 24 | - | NEG -$420k | - | 170 | 165 | -$529k | +$40k bull / +$0 bear | out (clean 29, ADX 20, RVol 1.5) |
| 10 | **QQQ** | 686.17 | - | **-** | 23 | - | NEG -$5.3B | - | 720 | 680 | +$148.2M | +$4.5M bull / +$0 bear | out (clean 31, ADX 44, RVol 1.0) |
| 11 | **SPY** | 755.39 | - | **-** | 22 | - | NEG -$10.5B | 775.64 | 770 | 750 | +$118.0M | +$3.0M bull / +$0 bear | out (clean 31, ADX 41, RVol 0.9) |
| 12 | **AMZN** | 248.77 | - | **-** | 22 | - | POS +$61.7M | 243.73 | 250 | 250 | -$18.4M | +$146k bull / +$0 bear | out (clean 34, ADX 37, RVol 0.6) |
| 13 | **NVDA** | 204.43 | - | **-** | 21 | - | NEG -$241.6M | - | 210 | 205 | +$15.9M | +$1.5M bull / +$0 bear | out (clean 29, ADX 33, RVol 1.0) |
| 14 | **MSFT** | 516.60 | - | **-** | 20 | - | POS +$155.8M | 502.12 | 540 | 500 | +$697k | +$74k bull / +$0 bear | out (clean 27, ADX 47, RVol 0.6) |
| 15 | **PLTR** | 182.26 | - | **-** | 20 | - | NEG -$11.5M | - | 200 | 180 | +$4.2M | +$660k bull / +$0 bear | out (clean 26, ADX 27, RVol 0.9) |
| 16 | **ORCL** | 120.30 | - | **-** | 20 | - | NEG -$36.3M | - | 130 | 120 | +$710k | +$62k bull / +$0 bear | out (clean 32, ADX 42, RVol 0.9) |
| 17 | **HOOD** | 84.22 | - | **-** | 20 | - | NEG -$11.3M | - | 85 | 90 | +$559k | +$149k bull / +$0 bear | out (clean 32, ADX 40, RVol 0.8) |
| 18 | **IWM** | 279.89 | - | **-** | 19 | - | NEG -$1.3B | 286.87 | 285 | 270 | +$3.5M | +$51k bull / +$0 bear | out (clean 33, ADX 35, RVol 0.8) |
| 19 | **AVGO** | 325.42 | - | **-** | 19 | - | NEG -$113.5M | - | 340 | 320 | -$2.2M | +$116k bull / +$0 bear | out (clean 31, ADX 34, RVol 0.7) |
| 20 | **META** | 611.43 | - | **-** | 17 | - | NEG -$128.7M | 624.61 | 650 | 610 | +$9.9M | +$69k bull / +$0 bear | out (clean 28, ADX 17, RVol 0.5) |
| 21 | **ARM** | 198.76 | - | **-** | 15 | - | NEG -$5.6M | - | 200 | 200 | +$308k | - | out (clean 25, ADX 35, RVol 1.0) |
| 22 | **UBER** | 66.79 | - | **-** | 15 | - | NEG -$8.4M | - | 70 | 65 | -$405k | - | out (clean 28, ADX 34, RVol 1.2) |
| 23 | **MSTR** | 132.25 | - | **-** | 11 | - | POS +$1.1M | - | 135 | 125 | +$4.3M | - | out (clean 26, ADX 20, RVol 1.0) |
| 24 | **CRM** | 228.92 | - | **-** | 11 | - | NEG -$6.9M | - | 240 | 220 | +$89k | - | out (clean 28, ADX 30, RVol 0.9) |
| 25 | **NFLX** | 62.65 | - | **-** | 10 | - | NEG -$20.2M | - | 63 | 60 | -$659k | - | out (clean 29, ADX 28, RVol 0.7) |
| 26 | **COIN** | 137.73 | - | **-** | 9 | - | NEG -$7.6M | - | 150 | 130 | -$200k | - | out (clean 24, ADX 30, RVol 0.9) |
| 27 | **GOOGL** | 282.78 | - | **-** | 5 | - | NEG -$90.2M | - | 285 | 290 | -$2.9M | - | out (clean 33, ADX 16, RVol 0.4) |

## Big prints this scan (63)
- **QQQ** PUT 690 2026-11-06 (4DTE): 313 @ 11.26 = **+$352k** SELL | vol 14,907 / OI 13,512
- **QQQ** PUT 690 2026-11-06 (4DTE): 300 @ 11.26 = **+$338k** SELL | vol 14,907 / OI 13,512
- **QQQ** PUT 690 2026-11-06 (4DTE): 278 @ 11.25 = **+$313k** SELL | vol 14,907 / OI 13,512
- **SPY** PUT 756 2026-11-04 (2DTE): 426 @ 4.48 = **+$191k** SELL | vol 16,914 / OI 149
- **QQQ** PUT 690 2026-11-06 (4DTE): 161 @ 11.26 = **+$181k** SELL | vol 14,907 / OI 13,512
- **QQQ** CALL 700 2026-11-06 (4DTE): 335 @ 5.11 = **+$171k** BUY | vol 15,835 / OI 1,051
- **AAPL** PUT 325 2026-11-06 (4DTE): 400 @ 3.89 = **+$156k** SELL | vol 12,124 / OI 10,672
- **QQQ** PUT 690 2026-11-06 (4DTE): 134 @ 11.26 = **+$151k** SELL | vol 14,907 / OI 13,512
- **QQQ** CALL 685 2026-11-06 (4DTE): 111 @ 12.24 = **+$136k** BUY | vol 831 / OI 166
- **SPY** CALL 752 2026-11-02 (0DTE): 257 @ 4.43 = **+$114k** BUY | vol 4,192 / OI 84
- **QQQ** PUT 690 2026-11-06 (4DTE): 100 @ 11.26 = **+$113k** SELL | vol 14,907 / OI 13,512
- **SPY** PUT 759 2026-11-06 (4DTE): 149 @ 7.47 = **+$111k** SELL | vol 18,121 / OI 1,010
- **SPY** PUT 759 2026-11-06 (4DTE): 144 @ 7.44 = **+$107k** SELL | vol 18,121 / OI 1,010
- **SPY** CALL 755 2026-11-02 (0DTE): 514 @ 2.05 = **+$105k** BUY | vol 17,334 / OI 59
- **QQQ** PUT 688 2026-11-06 (4DTE): 100 @ 10.37 = **+$104k** SELL | vol 846 / OI 1,514

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 740 2026-11-06 (4DTE): 9,948 traded vs OI 7,769
- **SPY** CALL 757 2026-11-13 (11DTE): 520 traded vs OI 162
- **QQQ** CALL 723 2026-11-03 (1DTE): 1,156 traded vs OI 223
- **QQQ** CALL 724 2026-11-03 (1DTE): 1,719 traded vs OI 179
- **QQQ** PUT 669 2026-11-04 (2DTE): 518 traded vs OI 0
- **QQQ** CALL 702 2026-11-06 (4DTE): 670 traded vs OI 669
- **QQQ** CALL 740 2026-11-09 (7DTE): 1,066 traded vs OI 856
- **QQQ** PUT 690 2026-11-06 (4DTE): 14,907 traded vs OI 13,512
- **QQQ** CALL 710 2026-11-16 (14DTE): 502 traded vs OI 0
- **IWM** CALL 287.5 2026-11-04 (2DTE): 500 traded vs OI 320
- **IWM** PUT 275 2026-11-03 (1DTE): 1,339 traded vs OI 1,308
- **TSLA** PUT 405 2026-11-09 (7DTE): 525 traded vs OI 287
- **AAPL** PUT 320 2026-11-09 (7DTE): 520 traded vs OI 119
- **AMD** PUT 477.5 2026-11-04 (2DTE): 500 traded vs OI 267
- **GOOGL** CALL 295 2026-11-06 (4DTE): 2,978 traded vs OI 2,972

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
