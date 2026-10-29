# GEX + FLOW SCAN - Thu Oct 29, 09:55 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (2)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 09:55 | **AAPL** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 10/30 345P | 0.77 | 0.75 | -3% (0m) | **-3%** | +198% | 345 |
| 09:50 | **IWM** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 10/29 283P | 0.50 | 0.39 | +2% (4m) | **-22%** | +159% | 282 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 09:55:08 ET, last candle SPY 09:54, QQQ 09:54 | no errors

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **AAPL** | 349.99 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 64 | 10/30 345P @ 0.77 (delta 0.21) = est +198% at 345 | POS +$612.5M | 339.44 | 350 | 345 | +$12.0M | +$5.6M bull / -$606k bear | out (clean 28, ADX 26, RVol 3.4) |
| 2 | **AVGO** | 339.35 | FLOW SURGE | **CALLS** | 63 | none: 81 calls 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (7 contracts' greeks worked out here) | NEG -$23.1M | 342.49 | 350 | 340 | +$2.8M | +$142k bull / +$0 bear | out (clean 29, ADX 41, RVol 3.0) |
| 3 | **MSTR** | 140.34 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 63 | none: 25 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (6 contracts' greeks worked out here) | POS +$22.6M | - | 152.5 | 140 | -$787k | +$165k bull / +$0 bear | out (clean 26, ADX 25, RVol 4.1) |
| 4 | **IWM** | 284.06 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 59 | 10/29 283P @ 0.46 (delta 0.31) = est +178% at 282 | POS +$730.2M | 281.61 | 284 | 270 | -$1.8M | +$0 bull / -$441k bear | out (clean 25, ADX 41, RVol 3.2) |
| 5 | **MU** | 945.21 | FLOW SURGE | **CALLS** | 57 | none: 117 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (8 contracts' greeks worked out here) | POS +$301.7M | - | 950 | 900 | +$29.6M | +$8.7M bull / +$0 bear | out (clean 29, ADX 34, RVol 2.7) |
| 6 | **CRM** | 231.49 | FLOW SURGE | **PUTS** | 57 | none: 18 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (6 contracts' greeks worked out here) | NEG -$17.3M | - | 240 | 230 | -$113k | +$0 bull / -$54k bear | out (clean 27, ADX 27, RVol 5.0) |
| 7 | **SMH** | 556.70 | FLOW SURGE | **CALLS** | 55 | none: 132 calls 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (25 contracts' greeks worked out here) | NEG -$131.8M | 563.73 | 560 | 555 | +$457k | +$87k bull / +$0 bear | out (clean 28, ADX 25, RVol 2.9) |
| 8 | **MSFT** | 528.12 | FLOW SURGE | **CALLS** | 55 | none: 126 calls 0-7DTE > 13 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (6 contracts' greeks worked out here) | POS +$572.2M | - | 525 | 530 | +$14.8M | +$3.5M bull / -$904k bear | out (clean 29, ADX 39, RVol 7.5) |
| 9 | **HOOD** | 90.37 | FLOW SURGE | **PUTS** | 55 | none: 18 puts 0-7DTE > 2 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only +3% at the target (needs +20%) | NEG -$25.2M | - | 95 | 90 | -$929k | +$0 bull / -$58k bear | out (clean 29, ADX 16, RVol 2.8) |
| 10 | **AMZN** | 245.04 | FLOW SURGE | **PUTS** | 53 | none: 57 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (8 contracts' greeks worked out here) | POS +$7.3M | 242.43 | 265 | 250 | -$3.9M | +$547k bull / -$1.8M bear | out (clean 31, ADX 47, RVol 7.8) |
| 11 | **SHOP** | 166.94 | FLOW SURGE | **PUTS** | 51 | none: 13 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (1 contracts' greeks worked out here) | NEG -$5.7M | 172.51 | 175 | 165 | -$45k | +$0 bull / -$29k bear | out (clean 27, ADX 21, RVol 1.7) |
| 12 | **META** | 620.66 | FLOW SURGE | **PUTS** | 50 | none: 144 puts 0-7DTE > 8 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (5 contracts' greeks worked out here) | NEG -$101.5M | 629.33 | 650 | 625 | -$8.8M | +$520k bull / -$1.1M bear | out (clean 28, ADX 31, RVol 2.0) |
| 13 | **PLTR** | 196.69 | FLOW SURGE | **PUTS** | 49 | none: 16 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (2 contracts' greeks worked out here) | POS +$57.2M | 190.69 | 200 | 200 | -$1.8M | +$0 bull / -$168k bear | out (clean 26, ADX 20, RVol 3.6) |
| 14 | **NFLX** | 62.08 | - | **-** | 33 | - | NEG -$50.4M | - | 63 | 60 | -$282k | +$30k bull / +$0 bear | out (clean 31, ADX 30, RVol 2.3) |
| 15 | **AMD** | 562.05 | - | **-** | 32 | - | POS +$121.6M | - | 550 | 550 | +$5.8M | +$907k bull / -$935k bear | out (clean 30, ADX 41, RVol 3.4) |
| 16 | **GOOGL** | 282.79 | - | **-** | 31 | - | NEG -$181.5M | - | 300 | 290 | -$5.3M | +$762k bull / -$6.5M bear | out (clean 33, ADX 40, RVol 14.4) |
| 17 | **TSLA** | 402.55 | - | **-** | 30 | - | POS +$451.3M | - | 400 | 400 | -$12.7M | +$2.0M bull / -$975k bear | out (clean 29, ADX 28, RVol 1.8) |
| 18 | **SPY** | 768.06 | - | **-** | 29 | - | NEG -$5.4B | 772.97 | 770 | 765 | -$31.2M | +$1.5M bull / -$597k bear | out (clean 28, ADX 23, RVol 4.0) |
| 19 | **ARM** | 225.13 | - | **-** | 28 | - | POS +$1.9M | 222.33 | 220 | 220 | +$74k | - | out (clean 26, ADX 28, RVol 3.8) |
| 20 | **COIN** | 161.42 | - | **-** | 27 | - | POS +$7.2M | - | 170 | 155 | -$99k | - | out (clean 27, ADX 19, RVol 3.9) |
| 21 | **UBER** | 65.04 | - | **-** | 27 | - | NEG -$34.0M | - | 70 | 65 | -$110k | - | out (clean 29, ADX 28, RVol 2.8) |
| 22 | **QQQ** | 713.08 | - | **-** | 26 | - | NEG -$5.3B | 726.96 | 720 | 700 | -$24.2M | +$2.3M bull / -$3.2M bear | out (clean 29, ADX 32, RVol 3.1) |
| 23 | **ORCL** | 139.59 | - | **-** | 25 | - | POS +$115.5M | - | 135 | 140 | +$152k | +$102k bull / +$0 bear | out (clean 31, ADX 43, RVol 4.0) |
| 24 | **SMCI** | 35.09 | - | **-** | 23 | - | POS +$23.1M | - | 35 | 35 | +$69k | - | out (clean 28, ADX 27, RVol 2.1) |
| 25 | **BABA** | 99.54 | - | **-** | 22 | - | NEG -$17.6M | 102.11 | 102 | 100 | -$39k | - | out (clean 28, ADX 30, RVol 3.3) |
| 26 | **NVDA** | 212.50 | - | **-** | 21 | - | POS +$110.0M | 210.27 | 215 | 210 | +$54k | +$1.1M bull / -$272k bear | out (clean 26, ADX 32, RVol 3.0) |
| 27 | **DELL** | 489.12 | - | **-** | 19 | - | POS +$11.3M | 474.79 | 500 | 500 | -$129k | +$31k bull / -$264k bear | out (clean 31, ADX 29, RVol 1.5) |

## Big prints this scan (241)
- **GOOGL** PUT 295 2026-10-30 (1DTE): 2,077 @ 14.03 = **+$2.9M** BUY | vol 4,371 / OI 5,774
- **GOOGL** PUT 295 2026-10-30 (1DTE): 1,683 @ 14.03 = **+$2.4M** BUY | vol 4,371 / OI 5,774
- **AMZN** CALL 247.5 2026-10-30 (1DTE): 463 @ 7.95 = **+$368k** SELL | vol 711 / OI 2,330
- **AMZN** CALL 245 2026-10-30 (1DTE): 385 @ 9.20 = **+$354k** SELL | vol 1,846 / OI 2,504
- **QQQ** CALL 720 2026-11-02 (4DTE): 1,200 @ 2.85 = **+$342k** SELL | vol 1,463 / OI 2,018
- **QQQ** PUT 717 2026-10-29 (0DTE): 494 @ 5.72 = **+$283k** BUY | vol 4,765 / OI 1,065
- **MSFT** CALL 540 2026-11-02 (4DTE): 599 @ 4.60 = **+$276k** BUY | vol 935 / OI 225
- **SPY** PUT 772 2026-10-29 (0DTE): 500 @ 4.70 = **+$235k** BUY | vol 3,090 / OI 415
- **QQQ** PUT 717 2026-10-29 (0DTE): 405 @ 5.56 = **+$225k** BUY | vol 4,765 / OI 1,065
- **IWM** CALL 282 2026-11-02 (4DTE): 700 @ 2.75 = **+$192k** SELL | vol 1,776 / OI 782
- **AMZN** CALL 245 2026-10-30 (1DTE): 224 @ 8.50 = **+$190k** SELL | vol 1,846 / OI 2,504
- **QQQ** CALL 701 2026-10-29 (0DTE): 160 @ 11.50 = **+$184k** SELL | vol 201 / OI 29
- **AMZN** CALL 245 2026-10-30 (1DTE): 216 @ 8.50 = **+$184k** SELL | vol 1,846 / OI 2,504
- **QQQ** PUT 725 2026-10-30 (1DTE): 125 @ 13.83 = **+$173k** BUY | vol 1,970 / OI 25,057
- **NVDA** PUT 212.5 2026-10-30 (1DTE): 837 @ 2.03 = **+$170k** SELL | vol 10,664 / OI 5,164

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 775 2026-11-03 (5DTE): 595 traded vs OI 515
- **SPY** CALL 765 2026-10-29 (0DTE): 1,396 traded vs OI 1,115
- **SPY** PUT 775 2026-10-29 (0DTE): 691 traded vs OI 214
- **SPY** CALL 781 2026-10-29 (0DTE): 1,054 traded vs OI 982
- **SPY** CALL 763 2026-10-29 (0DTE): 1,710 traded vs OI 1,290
- **SPY** PUT 768 2026-10-30 (1DTE): 4,306 traded vs OI 3,046
- **SPY** PUT 755 2026-10-29 (0DTE): 1,712 traded vs OI 1,541
- **SPY** CALL 840 2026-11-03 (5DTE): 908 traded vs OI 1
- **SPY** CALL 758 2026-10-29 (0DTE): 1,760 traded vs OI 32
- **SPY** PUT 757 2026-11-20 (22DTE): 15,007 traded vs OI 1,945
- **QQQ** CALL 725 2026-10-29 (0DTE): 4,858 traded vs OI 4,143
- **QQQ** CALL 738 2026-10-29 (0DTE): 1,672 traded vs OI 1,203
- **QQQ** PUT 719 2026-10-29 (0DTE): 875 traded vs OI 790
- **QQQ** CALL 726 2026-11-02 (4DTE): 3,330 traded vs OI 142
- **QQQ** CALL 716 2026-10-30 (1DTE): 1,575 traded vs OI 1,305

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
