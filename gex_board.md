# GEX + FLOW SCAN - Thu Oct 29, 03:15 PM ET
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
Last 1m check 15:15:08 ET, last candle SPY 15:14, QQQ 15:14 | no errors
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
| 1 | **AAPL** | 350.19 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 34 | none: 55 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (9 contracts' greeks worked out here) | POS +$703.5M | 340.76 | 350 | 345 | +$3.0M | +$475k bull / -$32k bear | out (clean 29, ADX 16, RVol 0.7) |
| 2 | **SMH** | 557.51 | - | **-** | 24 | - | NEG -$106.2M | 562.86 | 560 | 555 | +$2.6M | +$43k bull / -$37k bear | out (clean 27, ADX 30, RVol 0.5) |
| 3 | **MU** | 928.14 | - | **-** | 22 | - | POS +$180.7M | 900.03 | 950 | 900 | +$48.7M | +$1.9M bull / -$301k bear | out (clean 29, ADX 57, RVol 0.3) |
| 4 | **MSFT** | 527.94 | - | **-** | 21 | - | POS +$638.1M | 502.22 | 525 | 530 | +$24.0M | +$0 bull / -$152k bear | out (clean 28, ADX 22, RVol 0.8) |
| 5 | **GOOGL** | 282.30 | - | **-** | 21 | - | NEG -$181.1M | - | 300 | 290 | -$6.1M | +$74k bull / -$40k bear | out (clean 31, ADX 28, RVol 2.1) |
| 6 | **QQQ** | 712.62 | - | **-** | 19 | - | NEG -$5.8B | 725.35 | 720 | 700 | -$109.6M | +$1.5M bull / -$38.4M bear | out (clean 26, ADX 26, RVol 0.6) |
| 7 | **SPY** | 767.33 | - | **-** | 18 | - | NEG -$6.3B | 772.22 | 770 | 765 | -$98.2M | +$309k bull / -$560k bear | out (clean 25, ADX 24, RVol 0.6) |
| 8 | **ORCL** | 138.11 | - | **-** | 18 | - | POS +$115.7M | - | 135 | 140 | +$627k | +$43k bull / +$0 bear | out (clean 33, ADX 20, RVol 1.8) |
| 9 | **NVDA** | 212.61 | - | **-** | 17 | - | POS +$130.0M | 211.23 | 215 | 210 | -$976k | +$96k bull / +$0 bear | out (clean 24, ADX 30, RVol 0.5) |
| 10 | **META** | 627.51 | - | **-** | 17 | - | NEG -$38.1M | 630.33 | 650 | 625 | -$11.9M | +$0 bull / -$282k bear | out (clean 27, ADX 23, RVol 0.7) |
| 11 | **AMZN** | 245.19 | - | **-** | 17 | - | POS +$10.2M | 242.21 | 265 | 250 | -$3.1M | +$528k bull / -$1.9M bear | out (clean 31, ADX 19, RVol 1.3) |
| 12 | **AMD** | 562.04 | - | **-** | 16 | - | POS +$114.7M | - | 550 | 550 | +$1.3M | +$188k bull / -$81k bear | out (clean 28, ADX 25, RVol 0.6) |
| 13 | **SMCI** | 34.29 | - | **-** | 16 | - | POS +$19.0M | - | 35 | 35 | +$352k | - | out (clean 27, ADX 47, RVol 0.5) |
| 14 | **TSLA** | 404.96 | - | **-** | 15 | - | POS +$515.7M | - | 400 | 400 | -$19.6M | +$314k bull / -$241k bear | out (clean 28, ADX 11, RVol 0.4) |
| 15 | **AVGO** | 343.12 | - | **-** | 15 | - | POS +$8.9M | 342.2 | 350 | 340 | +$1.5M | +$638k bull / +$0 bear | out (clean 28, ADX 14, RVol 0.5) |
| 16 | **DELL** | 473.13 | - | **-** | 15 | - | NEG -$12.0M | 483.08 | 500 | 460 | +$2.5M | - | out (clean 32, ADX 52, RVol 1.2) |
| 17 | **UBER** | 65.47 | - | **-** | 15 | - | NEG -$29.3M | 67.74 | 67 | 65 | -$166k | - | out (clean 28, ADX 21, RVol 1.1) |
| 18 | **PLTR** | 193.30 | - | **-** | 14 | - | POS +$14.0M | 192.04 | 200 | 190 | -$193k | +$38k bull / +$0 bear | out (clean 25, ADX 15, RVol 0.4) |
| 19 | **ARM** | 226.43 | - | **-** | 14 | - | POS +$3.4M | 220.95 | 220 | 220 | +$1.5M | - | out (clean 24, ADX 18, RVol 0.7) |
| 20 | **CRM** | 229.22 | - | **-** | 10 | - | NEG -$18.1M | - | 240 | 230 | -$207k | - | out (clean 28, ADX 19, RVol 0.9) |
| 21 | **BABA** | 98.91 | - | **-** | 10 | - | NEG -$22.4M | 101.68 | 100 | 100 | -$10k | - | out (clean 29, ADX 36, RVol 1.7) |
| 22 | **NFLX** | 62.05 | - | **-** | 9 | - | NEG -$49.9M | - | 63 | 60 | -$500k | - | out (clean 32, ADX 20, RVol 0.5) |
| 23 | **HOOD** | 90.40 | - | **-** | 9 | - | NEG -$27.0M | - | 95 | 90 | -$666k | - | out (clean 29, ADX 35, RVol 0.7) |
| 24 | **SHOP** | 166.34 | - | **-** | 9 | - | NEG -$5.2M | 169.6 | 175 | 165 | -$71k | - | out (clean 25, ADX 19, RVol 0.5) |
| 25 | **COIN** | 158.72 | - | **-** | 8 | - | POS +$2.3M | 155.26 | 170 | 155 | -$129k | - | out (clean 26, ADX 28, RVol 1.0) |
| 26 | **IWM** | 283.17 | - | **-** | 7 | - | POS +$720.6M | 280.9 | 284 | 270 | -$1.3M | - | out (clean 26, ADX 29, RVol 0.7) |
| 27 | **MSTR** | 140.90 | - | **-** | 7 | - | POS +$24.3M | - | 152.5 | 140 | +$219k | - | out (clean 26, ADX 20, RVol 1.3) |

## Big prints this scan (59)
- **QQQ** PUT 710 2026-11-03 (5DTE): 1,500 @ 5.19 = **+$778k** SELL | vol 2,926 / OI 898
- **AMZN** CALL 245 2026-10-30 (1DTE): 462 @ 9.95 = **+$460k** BUY | vol 9,078 / OI 2,504
- **AAPL** PUT 355 2026-10-30 (1DTE): 800 @ 4.81 = **+$385k** SELL | vol 2,591 / OI 1,471
- **QQQ** PUT 712 2026-10-30 (1DTE): 875 @ 3.44 = **+$301k** SELL | vol 20,015 / OI 7,961
- **SPY** CALL 766 2026-10-29 (0DTE): 900 @ 2.18 = **+$196k** BUY | vol 41,586 / OI 865
- **AMZN** PUT 240 2026-10-30 (1DTE): 251 @ 7.25 = **+$182k** BUY | vol 10,057 / OI 8,499
- **QQQ** PUT 717 2026-10-30 (1DTE): 252 @ 6.00 = **+$151k** SELL | vol 15,020 / OI 3,101
- **AVGO** CALL 340 2026-11-04 (6DTE): 142 @ 9.80 = **+$139k** BUY | vol 1,175 / OI 163
- **QQQ** PUT 703 2026-10-30 (1DTE): 1,350 @ 0.97 = **+$131k** SELL | vol 6,567 / OI 2,778
- **QQQ** PUT 713 2026-10-30 (1DTE): 300 @ 3.80 = **+$114k** SELL | vol 20,800 / OI 2,501
- **SPY** CALL 766 2026-10-29 (0DTE): 490 @ 2.31 = **+$113k** BUY | vol 41,586 / OI 865
- **SMH** PUT 560 2026-10-30 (1DTE): 150 @ 6.18 = **+$93k** MID | vol 926 / OI 1,768
- **AMZN** PUT 240 2026-10-30 (1DTE): 117 @ 7.35 = **+$86k** BUY | vol 10,057 / OI 8,499
- **AVGO** CALL 340 2026-11-04 (6DTE): 78 @ 9.80 = **+$76k** BUY | vol 1,175 / OI 163
- **MU** CALL 950 2026-10-30 (1DTE): 120 @ 6.05 = **+$73k** BUY | vol 22,666 / OI 12,588

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 728 2026-11-02 (4DTE): 5,442 traded vs OI 189
- **SPY** CALL 786 2026-11-03 (5DTE): 582 traded vs OI 128
- **SPY** CALL 795 2026-11-05 (7DTE): 1,446 traded vs OI 347
- **QQQ** CALL 713 2026-11-03 (5DTE): 522 traded vs OI 170
- **QQQ** CALL 710 2026-11-13 (15DTE): 502 traded vs OI 495
- **QQQ** PUT 676 2026-11-13 (15DTE): 653 traded vs OI 0
- **IWM** PUT 278 2026-11-02 (4DTE): 770 traded vs OI 166
- **IWM** PUT 274 2026-11-20 (22DTE): 2,201 traded vs OI 2,167
- **AMZN** CALL 240 2026-11-06 (8DTE): 522 traded vs OI 361
- **AMZN** CALL 260 2026-11-09 (11DTE): 503 traded vs OI 38
- **AMZN** PUT 240 2026-10-30 (1DTE): 10,057 traded vs OI 8,499
- **MSFT** PUT 485 2026-10-30 (1DTE): 1,676 traded vs OI 1,603
- **GOOGL** PUT 300 2026-11-06 (8DTE): 3,306 traded vs OI 3,278
- **AVGO** CALL 345 2026-11-04 (6DTE): 510 traded vs OI 59
- **MU** PUT 860 2026-11-06 (8DTE): 513 traded vs OI 370

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
