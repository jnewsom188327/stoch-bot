# GEX + FLOW SCAN - Thu Oct 29, 03:45 PM ET
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
| 1 | **AAPL** | 349.40 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 38 | none: 55 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (10 contracts' greeks worked out here) | POS +$663.5M | 340.95 | 350 | 345 | +$3.0M | +$52k bull / +$0 bear | out (clean 29, ADX 19, RVol 1.2) |
| 2 | **IWM** | 283.37 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 25 | 10/29 284P @ 0.64 (delta 0.96) = est +138% at 282.51 | POS +$589.6M | 282.51 | 284 | 270 | -$1.5M | - | out (clean 27, ADX 24, RVol 0.7) |
| 3 | **MU** | 929.90 | - | **-** | 24 | - | POS +$194.7M | 899.05 | 950 | 900 | +$52.5M | +$1.3M bull / -$1.4M bear | out (clean 29, ADX 48, RVol 1.0) |
| 4 | **DELL** | 473.99 | - | **-** | 23 | - | NEG -$11.8M | 482.96 | 500 | 460 | +$2.4M | +$60k bull / -$54k bear | out (clean 32, ADX 40, RVol 0.9) |
| 5 | **MSFT** | 527.87 | - | **-** | 21 | - | POS +$619.0M | 502.76 | 525 | 530 | +$26.4M | +$392k bull / +$0 bear | out (clean 27, ADX 17, RVol 0.9) |
| 6 | **GOOGL** | 282.58 | - | **-** | 21 | - | NEG -$188.2M | - | 300 | 290 | -$5.6M | +$48k bull / -$360k bear | out (clean 31, ADX 25, RVol 2.6) |
| 7 | **QQQ** | 713.23 | - | **-** | 19 | - | NEG -$5.7B | 725.5 | 720 | 710 | -$146.3M | +$8.7M bull / -$31.2M bear | out (clean 26, ADX 20, RVol 1.0) |
| 8 | **SPY** | 768.08 | - | **-** | 18 | - | NEG -$5.8B | 772.25 | 770 | 765 | -$106.1M | +$532k bull / -$2.8M bear | out (clean 26, ADX 20, RVol 1.1) |
| 9 | **AMZN** | 245.43 | - | **-** | 17 | - | POS +$10.7M | 242.13 | 265 | 250 | -$1.2M | +$413k bull / -$1.5M bear | out (clean 31, ADX 17, RVol 2.1) |
| 10 | **NVDA** | 212.97 | - | **-** | 16 | - | POS +$161.8M | 211.37 | 215 | 210 | -$1.6M | +$39k bull / -$140k bear | out (clean 24, ADX 23, RVol 0.8) |
| 11 | **TSLA** | 403.76 | - | **-** | 16 | - | POS +$484.1M | - | 400 | 400 | -$15.9M | +$1.3M bull / +$0 bear | out (clean 28, ADX 15, RVol 0.5) |
| 12 | **META** | 627.93 | - | **-** | 16 | - | NEG -$31.8M | 630.31 | 650 | 625 | -$13.4M | +$0 bull / -$120k bear | out (clean 27, ADX 16, RVol 0.7) |
| 13 | **PLTR** | 193.35 | - | **-** | 16 | - | POS +$11.9M | 192.4 | 200 | 190 | -$346k | +$43k bull / -$41k bear | out (clean 25, ADX 16, RVol 1.4) |
| 14 | **SMCI** | 34.18 | - | **-** | 16 | - | POS +$17.9M | - | 35 | 35 | +$357k | - | out (clean 28, ADX 44, RVol 0.6) |
| 15 | **ORCL** | 138.32 | - | **-** | 16 | - | POS +$108.2M | - | 135 | 140 | +$699k | +$34k bull / +$0 bear | out (clean 33, ADX 16, RVol 1.2) |
| 16 | **ARM** | 225.97 | - | **-** | 16 | - | POS +$2.8M | 221.39 | 220 | 220 | +$1.6M | - | out (clean 24, ADX 17, RVol 1.9) |
| 17 | **UBER** | 65.50 | - | **-** | 16 | - | NEG -$28.4M | 67.61 | 67 | 65 | -$166k | - | out (clean 28, ADX 22, RVol 1.7) |
| 18 | **AMD** | 563.37 | - | **-** | 15 | - | POS +$120.0M | - | 550 | 550 | +$225k | +$27k bull / -$251k bear | out (clean 28, ADX 21, RVol 0.7) |
| 19 | **SMH** | 559.04 | - | **-** | 13 | - | NEG -$88.4M | 562.92 | 560 | 555 | +$2.5M | - | out (clean 27, ADX 26, RVol 0.6) |
| 20 | **CRM** | 229.18 | - | **-** | 12 | - | NEG -$16.4M | 239.76 | 240 | 230 | -$219k | - | out (clean 28, ADX 28, RVol 1.6) |
| 21 | **COIN** | 159.26 | - | **-** | 10 | - | POS +$2.8M | 155.14 | 170 | 155 | -$186k | - | out (clean 26, ADX 22, RVol 2.0) |
| 22 | **NFLX** | 61.94 | - | **-** | 9 | - | NEG -$51.5M | - | 63 | 61 | -$455k | - | out (clean 31, ADX 18, RVol 1.0) |
| 23 | **HOOD** | 90.96 | - | **-** | 9 | - | NEG -$26.6M | 96.4 | 95 | 90 | -$689k | - | out (clean 30, ADX 28, RVol 0.9) |
| 24 | **SHOP** | 166.65 | - | **-** | 9 | - | NEG -$6.3M | 170.99 | 175 | 165 | -$77k | - | out (clean 24, ADX 16, RVol 0.8) |
| 25 | **BABA** | 99.38 | - | **-** | 9 | - | NEG -$22.9M | 101.92 | 100 | 100 | -$35k | - | out (clean 29, ADX 29, RVol 1.3) |
| 26 | **MSTR** | 141.60 | - | **-** | 6 | - | POS +$25.2M | - | 152.5 | 140 | -$95k | - | out (clean 26, ADX 17, RVol 1.2) |
| 27 | **AVGO** | 343.70 | - | **-** | 5 | - | POS +$13.9M | 341.86 | 350 | 340 | +$1.4M | - | out (clean 28, ADX 12, RVol 0.8) |

## Big prints this scan (64)
- **MU** CALL 935 2026-10-30 (1DTE): 191 @ 11.60 = **+$222k** BUY | vol 6,002 / OI 1,088
- **MSFT** CALL 505 2026-10-30 (1DTE): 75 @ 24.00 = **+$180k** BUY | vol 165 / OI 372
- **QQQ** PUT 739 2026-11-02 (4DTE): 68 @ 25.54 = **+$174k** SELL | vol 85 / OI 2
- **SPY** PUT 775 2026-11-02 (4DTE): 224 @ 7.40 = **+$166k** SELL | vol 29,569 / OI 149
- **SPY** CALL 760 2026-10-30 (1DTE): 184 @ 8.45 = **+$155k** SELL | vol 2,551 / OI 6,380
- **MU** CALL 910 2026-10-30 (1DTE): 50 @ 26.10 = **+$130k** MID | vol 279 / OI 1,167
- **QQQ** PUT 712 2026-10-29 (0DTE): 1,400 @ 0.88 = **+$123k** SELL | vol 239,794 / OI 1,739
- **SPY** PUT 775 2026-11-02 (4DTE): 165 @ 7.40 = **+$122k** SELL | vol 29,569 / OI 149
- **SPY** PUT 775 2026-11-02 (4DTE): 165 @ 7.40 = **+$122k** SELL | vol 29,569 / OI 149
- **SPY** PUT 775 2026-11-02 (4DTE): 165 @ 7.40 = **+$122k** SELL | vol 29,569 / OI 149
- **MU** CALL 910 2026-10-30 (1DTE): 40 @ 26.43 = **+$106k** BUY | vol 279 / OI 1,167
- **AMZN** PUT 235 2026-10-30 (1DTE): 192 @ 5.50 = **+$106k** BUY | vol 11,083 / OI 5,203
- **MU** CALL 920 2026-10-30 (1DTE): 50 @ 19.35 = **+$97k** BUY | vol 1,713 / OI 1,840
- **MU** CALL 915 2026-10-30 (1DTE): 40 @ 23.03 = **+$92k** BUY | vol 190 / OI 1,171
- **MU** CALL 932.5 2026-10-30 (1DTE): 70 @ 12.80 = **+$90k** MID | vol 1,841 / OI 285

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 762 2026-11-04 (6DTE): 530 traded vs OI 111
- **SPY** CALL 784 2026-11-02 (4DTE): 530 traded vs OI 275
- **SPY** CALL 781 2026-11-03 (5DTE): 513 traded vs OI 271
- **SPY** CALL 794 2026-11-04 (6DTE): 599 traded vs OI 36
- **SPY** PUT 729 2026-10-30 (1DTE): 2,588 traded vs OI 2,404
- **SPY** PUT 729 2026-11-03 (5DTE): 603 traded vs OI 135
- **SPY** CALL 778 2026-11-03 (5DTE): 502 traded vs OI 270
- **QQQ** CALL 712 2026-11-03 (5DTE): 506 traded vs OI 88
- **QQQ** PUT 730 2026-10-29 (0DTE): 577 traded vs OI 270
- **QQQ** PUT 705 2026-11-09 (11DTE): 529 traded vs OI 262
- **QQQ** CALL 735 2026-11-12 (14DTE): 688 traded vs OI 0
- **SMH** PUT 590 2026-10-30 (1DTE): 811 traded vs OI 542
- **SMH** PUT 587.5 2026-10-30 (1DTE): 884 traded vs OI 586
- **NVDA** CALL 195 2026-11-06 (8DTE): 625 traded vs OI 86
- **NVDA** PUT 217.5 2026-11-02 (4DTE): 897 traded vs OI 895

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
