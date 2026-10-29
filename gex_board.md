# GEX + FLOW SCAN - Thu Oct 29, 02:30 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (4)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:30 | **IWM** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 10/29 284P | 0.65 | 0.22 | +3% (25m) | **-66%** (done) | +232% | 281.86 |
| 10:00 | **ORCL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 10/30 145C | 0.79 | 0.84 | +18% (37m) | **+6%** (done) | +139% | 143.92 |
| 09:55 | **AAPL** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 10/30 345P | 0.77 | 0.68 | +17% (2m) | **-12%** (done) | +198% | 345 |
| 09:50 | **IWM** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 10/29 283P | 0.50 | 0.18 | +20% (21m) | **-64%** (done) | +159% | 282 |

## 1m RULES on SPY / QQQ - loose (3 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 14:30:08 ET, last candle SPY 14:29, QQQ 14:29 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 14:23 | QQQ | 1m FAILED POP | R3 R4 | PUTS | TURNING your way | no contract: 86 puts 0-1DTE > 5 priced 0.40-0.80 > 1 delta 0.15+ > 1 spread ok > 1 liquid  |
| 14:17 | QQQ | 1m FAILED POP | R3 R4 | PUTS | TURNING your way | no contract: 86 puts 0-1DTE > 6 priced 0.40-0.80 > 2 delta 0.15+ > 2 spread ok > 2 liquid  |
| 14:12 | QQQ | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | no contract: 86 puts 0-1DTE > 8 priced 0.40-0.80 > 3 delta 0.15+ > 3 spread ok > 3 liquid  |

## Flow surges NOT fired - price disagreed (2 today, last 5)
- 10:05 HOOD PUTS: price +0.99 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:00 HOOD PUTS: price +0.89 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **AAPL** | 349.90 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 33 | none: 55 puts 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (10 contracts' greeks worked out here) | POS +$651.9M | 340.86 | 350 | 345 | +$3.9M | +$29k bull / +$0 bear | out (clean 29, ADX 14, RVol 0.6) |
| 2 | **ARM** | 227.59 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 30 | none: 19 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (4 contracts' greeks worked out here) | POS +$2.0M | 224.12 | 227.5 | 220 | +$1.5M | - | out (clean 24, ADX 13, RVol 0.5) |
| 3 | **DELL** | 475.07 | - | **-** | 24 | - | NEG -$5.4M | 479.92 | 500 | 460 | +$2.2M | +$33k bull / +$0 bear | out (clean 31, ADX 50, RVol 0.9) |
| 4 | **MSFT** | 528.07 | - | **-** | 23 | - | POS +$610.2M | 501.53 | 525 | 530 | +$23.7M | +$342k bull / -$823k bear | out (clean 28, ADX 25, RVol 1.3) |
| 5 | **GOOGL** | 281.89 | - | **-** | 23 | - | NEG -$183.3M | - | 300 | 290 | -$5.0M | +$227k bull / +$0 bear | out (clean 32, ADX 42, RVol 2.1) |
| 6 | **MU** | 931.53 | - | **-** | 22 | - | POS +$237.2M | 883.8 | 950 | 900 | +$43.4M | +$3.7M bull / -$114k bear | out (clean 28, ADX 47, RVol 0.5) |
| 7 | **SPY** | 767.33 | - | **-** | 18 | - | NEG -$6.4B | 772.44 | 770 | 765 | -$90.2M | +$224k bull / -$1.2M bear | out (clean 25, ADX 26, RVol 0.6) |
| 8 | **META** | 626.44 | - | **-** | 18 | - | NEG -$53.5M | 630.13 | 650 | 625 | -$9.5M | +$108k bull / -$452k bear | out (clean 28, ADX 29, RVol 0.8) |
| 9 | **NFLX** | 61.76 | - | **-** | 18 | - | NEG -$50.8M | 65.29 | 63 | 61 | -$368k | +$40k bull / +$0 bear | out (clean 31, ADX 22, RVol 0.5) |
| 10 | **QQQ** | 713.09 | - | **-** | 17 | - | NEG -$5.6B | 725.84 | 720 | 700 | -$60.4M | +$139k bull / -$491k bear | out (clean 26, ADX 26, RVol 0.5) |
| 11 | **AMZN** | 244.75 | - | **-** | 17 | - | POS +$7.6M | 242.4 | 265 | 250 | -$1.1M | +$183k bull / -$307k bear | out (clean 32, ADX 26, RVol 1.0) |
| 12 | **NVDA** | 212.68 | - | **-** | 16 | - | POS +$129.2M | 211.09 | 215 | 210 | -$1.4M | +$102k bull / -$185k bear | out (clean 24, ADX 26, RVol 0.5) |
| 13 | **TSLA** | 405.12 | - | **-** | 16 | - | POS +$517.7M | - | 400 | 400 | -$19.9M | +$92k bull / -$400k bear | out (clean 28, ADX 16, RVol 0.4) |
| 14 | **AMD** | 564.48 | - | **-** | 15 | - | POS +$139.7M | - | 550 | 550 | -$573k | +$99k bull / -$154k bear | out (clean 28, ADX 22, RVol 0.3) |
| 15 | **COIN** | 158.37 | - | **-** | 15 | - | POS +$1.8M | 155.31 | 170 | 155 | -$77k | +$0 bull / -$374k bear | out (clean 25, ADX 16, RVol 0.7) |
| 16 | **SMCI** | 34.60 | - | **-** | 14 | - | POS +$21.3M | - | 35 | 35 | +$297k | - | out (clean 26, ADX 36, RVol 0.6) |
| 17 | **UBER** | 65.01 | - | **-** | 14 | - | NEG -$32.3M | 67.22 | 70 | 65 | -$157k | - | out (clean 28, ADX 21, RVol 0.6) |
| 18 | **SMH** | 558.25 | - | **-** | 11 | - | NEG -$79.2M | 562.29 | 560 | 555 | +$1.4M | - | out (clean 27, ADX 24, RVol 0.7) |
| 19 | **ORCL** | 138.09 | - | **-** | 9 | - | POS +$119.0M | - | 135 | 140 | +$607k | - | out (clean 32, ADX 33, RVol 1.0) |
| 20 | **CRM** | 231.71 | - | **-** | 9 | - | NEG -$19.5M | - | 240 | 230 | -$240k | - | out (clean 27, ADX 11, RVol 0.8) |
| 21 | **SHOP** | 166.71 | - | **-** | 9 | - | NEG -$6.0M | 171.97 | 175 | 165 | -$74k | - | out (clean 25, ADX 16, RVol 0.4) |
| 22 | **HOOD** | 90.32 | - | **-** | 7 | - | NEG -$26.6M | - | 95 | 90 | -$338k | - | out (clean 28, ADX 28, RVol 0.7) |
| 23 | **BABA** | 99.08 | - | **-** | 7 | - | NEG -$21.3M | 101.71 | 100 | 100 | -$17k | - | out (clean 29, ADX 27, RVol 0.9) |
| 24 | **IWM** | 283.12 | - | **-** | 6 | - | POS +$604.8M | 281.29 | 284 | 270 | +$121k | - | out (clean 26, ADX 28, RVol 0.7) |
| 25 | **MSTR** | 141.04 | - | **-** | 6 | - | POS +$24.3M | - | 152.5 | 140 | +$260k | - | out (clean 26, ADX 20, RVol 1.0) |
| 26 | **AVGO** | 344.39 | - | **-** | 5 | - | POS +$18.1M | 341.87 | 350 | 340 | +$1.6M | - | out (clean 28, ADX 13, RVol 0.5) |
| 27 | **PLTR** | 194.18 | - | **-** | 4 | - | POS +$19.1M | 192.52 | 200 | 190 | -$306k | - | out (clean 26, ADX 15, RVol 0.4) |

## Big prints this scan (39)
- **MU** PUT 930 2026-10-30 (1DTE): 300 @ 13.05 = **+$392k** SELL | vol 7,203 / OI 2,191
- **MSFT** CALL 532.5 2026-10-30 (1DTE): 879 @ 2.85 = **+$251k** BUY | vol 8,027 / OI 1,809
- **QQQ** PUT 722 2026-11-04 (6DTE): 112 @ 12.39 = **+$139k** SELL | vol 345 / OI 40
- **SPY** PUT 767 2026-10-29 (0DTE): 1,094 @ 1.05 = **+$115k** SELL | vol 359,192 / OI 2,012
- **META** CALL 615 2026-10-30 (1DTE): 50 @ 14.60 = **+$73k** BUY | vol 2,082 / OI 639
- **MU** CALL 935 2026-10-30 (1DTE): 50 @ 12.90 = **+$64k** BUY | vol 4,361 / OI 1,088
- **MU** CALL 970 2026-10-30 (1DTE): 225 @ 2.71 = **+$61k** BUY | vol 14,240 / OI 2,312
- **MSFT** CALL 542.5 2026-10-30 (1DTE): 879 @ 0.67 = **+$59k** BUY | vol 7,430 / OI 1,400
- **TSLA** CALL 405 2026-11-02 (4DTE): 100 @ 5.60 = **+$56k** BUY | vol 4,438 / OI 874
- **MU** CALL 950 2026-10-30 (1DTE): 80 @ 7.00 = **+$56k** BUY | vol 20,989 / OI 12,588
- **AMZN** CALL 245 2026-10-30 (1DTE): 50 @ 9.70 = **+$48k** BUY | vol 7,052 / OI 2,504
- **AMZN** CALL 245 2026-10-30 (1DTE): 50 @ 9.69 = **+$48k** BUY | vol 7,052 / OI 2,504
- **GOOGL** CALL 290 2026-10-30 (1DTE): 500 @ 0.89 = **+$44k** MID | vol 55,151 / OI 113
- **MU** CALL 890 2026-10-30 (1DTE): 10 @ 44.40 = **+$44k** BUY | vol 90 / OI 803
- **AMD** CALL 565 2026-10-30 (1DTE): 48 @ 9.00 = **+$43k** SELL | vol 3,850 / OI 956

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 724 2026-10-30 (1DTE): 1,533 traded vs OI 1,326
- **SPY** PUT 735 2026-11-12 (14DTE): 1,216 traded vs OI 0
- **SPY** CALL 768 2026-11-13 (15DTE): 1,099 traded vs OI 1,089
- **SPY** PUT 700 2026-11-12 (14DTE): 1,027 traded vs OI 0
- **SPY** PUT 764 2026-11-06 (8DTE): 2,976 traded vs OI 2,906
- **QQQ** PUT 713 2026-11-03 (5DTE): 603 traded vs OI 253
- **IWM** PUT 272 2026-11-09 (11DTE): 633 traded vs OI 7
- **IWM** PUT 273 2026-11-09 (11DTE): 517 traded vs OI 36
- **IWM** PUT 277 2026-11-13 (15DTE): 1,065 traded vs OI 675
- **IWM** PUT 280 2026-11-13 (15DTE): 1,966 traded vs OI 1,148
- **SMH** PUT 502.5 2026-10-30 (1DTE): 673 traded vs OI 0
- **TSLA** PUT 392.5 2026-11-04 (6DTE): 514 traded vs OI 107
- **AMZN** PUT 237.5 2026-10-30 (1DTE): 1,187 traded vs OI 1,183
- **GOOGL** CALL 297.5 2026-11-02 (4DTE): 501 traded vs OI 16
- **AVGO** PUT 337.5 2026-11-02 (4DTE): 500 traded vs OI 65

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
