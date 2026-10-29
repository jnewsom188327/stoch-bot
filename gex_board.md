# GEX + FLOW SCAN - Thu Oct 29, 03:55 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (4)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:30 | **IWM** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 10/29 284P | 0.65 | 0.22 | +3% (25m) | **-66%** (done) | +232% | 281.86 |
| 10:00 | **ORCL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 10/30 145C | 0.79 | 0.84 | +18% (37m) | **+6%** (done) | +139% | 143.92 |
| 09:55 | **AAPL** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 10/30 345P | 0.77 | 0.68 | +17% (2m) | **-12%** (done) | +198% | 345 |
| 09:50 | **IWM** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 10/29 283P | 0.50 | 0.18 | +20% (21m) | **-64%** (done) | +159% | 282 |

## 1m RULES on SPY / QQQ - loose (4 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 15:32:08 ET, last candle SPY 15:31, QQQ 15:31 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 14:31 | SPY | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |
| 14:23 | QQQ | 1m FAILED POP | R3 R4 | PUTS | TURNING your way | no contract: 86 puts 0-1DTE > 5 priced 0.40-0.80 > 1 delta 0.15+ > 1 spread ok > 1 liquid  |
| 14:17 | QQQ | 1m FAILED POP | R3 R4 | PUTS | TURNING your way | no contract: 86 puts 0-1DTE > 6 priced 0.40-0.80 > 2 delta 0.15+ > 2 spread ok > 2 liquid  |
| 14:12 | QQQ | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | no contract: 86 puts 0-1DTE > 8 priced 0.40-0.80 > 3 delta 0.15+ > 3 spread ok > 3 liquid  |

## Flow surges NOT fired - price disagreed (2 today, last 5)
- 10:05 HOOD PUTS: price +0.99 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:00 HOOD PUTS: price +0.89 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **MSFT** | 529.41 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 42 | none: 126 calls 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (11 contracts' greeks worked out here) | POS +$655.2M | 502.18 | 525 | 530 | +$25.4M | +$241k bull / -$207k bear | out (clean 27, ADX 17, RVol 1.2) |
| 2 | **IWM** | 283.69 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 30 | 10/30 282.5P @ 0.51 (delta 0.31) = est +30% at 283.13 | POS +$1.1B | 281.51 | 284 | 270 | -$1.8M | - | out (clean 26, ADX 22, RVol 1.5) |
| 3 | **MU** | 937.30 | - | **-** | 24 | - | POS +$231.1M | 900.52 | 950 | 900 | +$50.8M | +$1.3M bull / -$3.2M bear | out (clean 29, ADX 44, RVol 1.5) |
| 4 | **DELL** | 475.68 | - | **-** | 23 | - | NEG -$7.7M | 482.72 | 500 | 460 | +$2.2M | +$60k bull / -$65k bear | out (clean 32, ADX 37, RVol 1.3) |
| 5 | **COIN** | 160.78 | - | **-** | 22 | - | POS +$3.9M | 155.48 | 170 | 155 | -$368k | +$0 bull / -$33k bear | out (clean 26, ADX 22, RVol 2.9) |
| 6 | **SPY** | 769.12 | - | **-** | 20 | - | NEG -$4.7B | 772.39 | 770 | 765 | -$118.8M | +$532k bull / -$1.2M bear | out (clean 26, ADX 18, RVol 1.8) |
| 7 | **QQQ** | 714.76 | - | **-** | 20 | - | NEG -$5.3B | 725.22 | 720 | 720 | -$152.2M | +$1.1M bull / -$1.1M bear | out (clean 26, ADX 19, RVol 1.4) |
| 8 | **AAPL** | 348.93 | - | **-** | 19 | - | POS +$590.2M | 341.88 | 350 | 345 | +$4.1M | +$184k bull / +$0 bear | out (clean 29, ADX 21, RVol 1.8) |
| 9 | **AMZN** | 245.59 | - | **-** | 18 | - | POS +$8.4M | 242.61 | 265 | 250 | -$265k | +$419k bull / -$506k bear | out (clean 31, ADX 16, RVol 3.2) |
| 10 | **PLTR** | 195.91 | - | **-** | 18 | - | POS +$50.8M | 192.49 | 200 | 200 | -$656k | +$43k bull / -$39k bear | out (clean 25, ADX 17, RVol 2.1) |
| 11 | **UBER** | 65.53 | - | **-** | 18 | - | NEG -$29.2M | 67.67 | 67 | 65 | -$179k | - | out (clean 28, ADX 20, RVol 2.4) |
| 12 | **NVDA** | 213.05 | - | **-** | 17 | - | POS +$193.4M | 211.33 | 215 | 210 | -$2.2M | +$405k bull / -$145k bear | out (clean 24, ADX 20, RVol 1.3) |
| 13 | **META** | 627.03 | - | **-** | 17 | - | NEG -$79.7M | 630.56 | 650 | 625 | -$13.6M | +$26k bull / +$0 bear | out (clean 27, ADX 15, RVol 1.2) |
| 14 | **ORCL** | 139.28 | - | **-** | 17 | - | POS +$122.3M | - | 135 | 140 | +$556k | +$34k bull / +$0 bear | out (clean 33, ADX 17, RVol 1.5) |
| 15 | **ARM** | 228.09 | - | **-** | 17 | - | POS +$3.3M | 221.15 | 227.5 | 220 | +$1.5M | - | out (clean 24, ADX 17, RVol 2.8) |
| 16 | **TSLA** | 403.40 | - | **-** | 16 | - | POS +$472.3M | - | 400 | 400 | -$15.4M | +$1.1M bull / +$0 bear | out (clean 28, ADX 16, RVol 0.6) |
| 17 | **AMD** | 565.27 | - | **-** | 16 | - | POS +$114.7M | - | 600 | 550 | -$613k | +$137k bull / -$337k bear | out (clean 28, ADX 19, RVol 1.3) |
| 18 | **SMCI** | 34.38 | - | **-** | 16 | - | POS +$19.6M | - | 35 | 35 | +$358k | - | out (clean 28, ADX 43, RVol 0.9) |
| 19 | **CRM** | 230.74 | - | **-** | 14 | - | NEG -$17.5M | 243.52 | 240 | 230 | -$229k | - | out (clean 28, ADX 28, RVol 2.1) |
| 20 | **SMH** | 560.85 | - | **-** | 13 | - | NEG -$45.7M | 563.1 | 560 | 555 | +$2.4M | - | out (clean 27, ADX 23, RVol 0.9) |
| 21 | **GOOGL** | 283.54 | - | **-** | 11 | - | NEG -$198.8M | - | 300 | 290 | -$5.7M | - | out (clean 31, ADX 24, RVol 4.2) |
| 22 | **SHOP** | 166.53 | - | **-** | 11 | - | NEG -$5.3M | 170.76 | 175 | 165 | -$77k | - | out (clean 24, ADX 15, RVol 2.0) |
| 23 | **BABA** | 99.37 | - | **-** | 11 | - | NEG -$22.5M | 101.79 | 100 | 100 | -$38k | - | out (clean 30, ADX 28, RVol 2.0) |
| 24 | **NFLX** | 61.94 | - | **-** | 10 | - | NEG -$51.5M | - | 63 | 65 | -$456k | - | out (clean 31, ADX 17, RVol 1.7) |
| 25 | **HOOD** | 91.28 | - | **-** | 9 | - | NEG -$23.6M | 96.71 | 95 | 90 | -$771k | - | out (clean 30, ADX 27, RVol 1.0) |
| 26 | **MSTR** | 141.67 | - | **-** | 6 | - | POS +$27.2M | - | 152.5 | 140 | -$89k | - | out (clean 26, ADX 16, RVol 1.6) |
| 27 | **AVGO** | 344.90 | - | **-** | 5 | - | POS +$28.4M | 341.77 | 350 | 340 | +$1.1M | - | out (clean 28, ADX 12, RVol 1.1) |

## Big prints this scan (61)
- **QQQ** CALL 723 2026-10-30 (1DTE): 4,000 @ 0.92 = **+$368k** BUY | vol 34,859 / OI 1,302
- **NVDA** CALL 217.5 2026-10-30 (1DTE): 7,500 @ 0.30 = **+$225k** BUY | vol 77,161 / OI 44,295
- **QQQ** CALL 727 2026-10-30 (1DTE): 4,000 @ 0.35 = **+$140k** BUY | vol 32,281 / OI 2,697
- **MU** CALL 950 2026-10-30 (1DTE): 199 @ 6.60 = **+$131k** SELL | vol 25,262 / OI 12,588
- **MU** PUT 945 2026-10-30 (1DTE): 59 @ 21.50 = **+$127k** BUY | vol 8,537 / OI 239
- **SPY** CALL 766 2026-10-29 (0DTE): 448 @ 2.60 = **+$116k** SELL | vol 48,493 / OI 865
- **AMD** PUT 550 2026-10-30 (1DTE): 300 @ 3.50 = **+$105k** BUY | vol 4,237 / OI 1,905
- **NVDA** PUT 212.5 2026-10-30 (1DTE): 667 @ 1.34 = **+$89k** BUY | vol 89,275 / OI 5,164
- **NVDA** CALL 212.5 2026-11-04 (6DTE): 154 @ 4.05 = **+$62k** BUY | vol 1,599 / OI 138
- **TSLA** CALL 405 2026-10-30 (1DTE): 189 @ 2.93 = **+$55k** BUY | vol 63,316 / OI 4,208
- **AMD** CALL 550 2026-10-30 (1DTE): 30 @ 18.15 = **+$54k** SELL | vol 1,683 / OI 3,519
- **AMZN** CALL 242.5 2026-10-30 (1DTE): 45 @ 11.10 = **+$50k** BUY | vol 2,181 / OI 512
- **AMZN** PUT 250 2026-10-30 (1DTE): 40 @ 12.47 = **+$50k** BUY | vol 3,489 / OI 7,140
- **MU** CALL 940 2026-10-30 (1DTE): 49 @ 10.08 = **+$49k** SELL | vol 11,654 / OI 2,522
- **MU** CALL 940 2026-10-30 (1DTE): 49 @ 10.04 = **+$49k** SELL | vol 11,654 / OI 2,522

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 790 2026-11-04 (6DTE): 502 traded vs OI 221
- **SPY** PUT 765 2026-11-13 (15DTE): 1,872 traded vs OI 1,861
- **QQQ** CALL 729 2026-11-04 (6DTE): 658 traded vs OI 50
- **QQQ** PUT 692 2026-10-30 (1DTE): 2,374 traded vs OI 2,346
- **IWM** PUT 262 2026-11-13 (15DTE): 14,436 traded vs OI 13,781
- **IWM** PUT 273 2026-11-13 (15DTE): 14,913 traded vs OI 14,378
- **NVDA** PUT 222.5 2026-11-02 (4DTE): 505 traded vs OI 225
- **TSLA** CALL 420 2026-11-09 (11DTE): 508 traded vs OI 0
- **AAPL** CALL 345 2026-10-30 (1DTE): 8,503 traded vs OI 8,414
- **AMD** CALL 575 2026-11-06 (8DTE): 1,568 traded vs OI 1,265
- **AMD** CALL 592.5 2026-11-06 (8DTE): 1,099 traded vs OI 72
- **AMZN** CALL 270 2026-11-13 (15DTE): 678 traded vs OI 0
- **AMZN** PUT 225 2026-11-06 (8DTE): 2,178 traded vs OI 1,907
- **AMZN** CALL 265 2026-11-06 (8DTE): 4,582 traded vs OI 4,578
- **MSFT** CALL 565 2026-11-02 (4DTE): 500 traded vs OI 159

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
