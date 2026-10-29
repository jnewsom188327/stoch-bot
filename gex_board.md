# GEX + FLOW SCAN - Thu Oct 29, 02:00 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (4)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:30 | **IWM** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 10/29 284P | 0.65 | 0.22 | +3% (25m) | **-66%** (done) | +232% | 281.86 |
| 10:00 | **ORCL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 10/30 145C | 0.79 | 0.84 | +18% (37m) | **+6%** (done) | +139% | 143.92 |
| 09:55 | **AAPL** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 10/30 345P | 0.77 | 0.68 | +17% (2m) | **-12%** (done) | +198% | 345 |
| 09:50 | **IWM** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 10/29 283P | 0.50 | 0.18 | +20% (21m) | **-64%** (done) | +159% | 282 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 14:00:08 ET, last candle SPY 13:59, QQQ 13:59 | no errors

## Flow surges NOT fired - price disagreed (2 today, last 5)
- 10:05 HOOD PUTS: price +0.99 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:00 HOOD PUTS: price +0.89 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **MSFT** | 526.26 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 42 | none: 126 puts 0-7DTE > 11 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (22 contracts' greeks worked out here) | POS +$566.8M | 502.2 | 525 | 530 | +$25.3M | +$34k bull / -$130k bear | out (clean 27, ADX 14, RVol 1.1) |
| 2 | **IWM** | 283.44 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 36 | 10/29 284P @ 0.76 (delta 0.71) = est +62% at 282.76 | POS +$795.2M | 281.44 | 284 | 270 | -$389k | +$132k bull / +$0 bear | out (clean 25, ADX 23, RVol 0.9) |
| 3 | **AAPL** | 349.68 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 33 | none: 55 puts 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (8 contracts' greeks worked out here) | POS +$646.9M | 340.89 | 350 | 345 | +$3.9M | +$70k bull / +$0 bear | out (clean 29, ADX 17, RVol 0.6) |
| 4 | **DELL** | 476.92 | - | **-** | 23 | - | NEG -$4.0M | 480.22 | 500 | 460 | +$1.9M | +$565k bull / +$0 bear | out (clean 30, ADX 45, RVol 0.9) |
| 5 | **GOOGL** | 282.61 | - | **-** | 22 | - | NEG -$183.8M | - | 300 | 290 | -$7.1M | +$62k bull / +$0 bear | out (clean 32, ADX 38, RVol 1.3) |
| 6 | **MU** | 935.12 | - | **-** | 20 | - | POS +$266.3M | 883.89 | 950 | 900 | +$30.7M | +$7.1M bull / +$0 bear | out (clean 27, ADX 39, RVol 0.3) |
| 7 | **META** | 626.83 | - | **-** | 19 | - | NEG -$40.3M | 629.75 | 650 | 625 | -$10.2M | +$365k bull / +$0 bear | out (clean 28, ADX 32, RVol 0.5) |
| 8 | **QQQ** | 712.97 | - | **-** | 17 | - | NEG -$5.6B | 725.61 | 720 | 700 | -$48.9M | +$818k bull / +$0 bear | out (clean 26, ADX 23, RVol 0.5) |
| 9 | **SMH** | 559.15 | - | **-** | 17 | - | NEG -$77.3M | 563.26 | 560 | 555 | +$652k | +$52k bull / +$0 bear | out (clean 26, ADX 16, RVol 0.4) |
| 10 | **TSLA** | 404.42 | - | **-** | 16 | - | POS +$495.0M | - | 400 | 400 | -$19.0M | +$144k bull / +$0 bear | out (clean 28, ADX 18, RVol 0.3) |
| 11 | **AMZN** | 244.69 | - | **-** | 16 | - | POS +$7.2M | 242.41 | 265 | 250 | -$2.4M | +$364k bull / +$0 bear | out (clean 31, ADX 21, RVol 0.9) |
| 12 | **NVDA** | 212.91 | - | **-** | 15 | - | POS +$155.2M | 211 | 215 | 210 | -$4.0M | +$147k bull / +$0 bear | out (clean 24, ADX 18, RVol 0.6) |
| 13 | **AMD** | 565.25 | - | **-** | 15 | - | POS +$141.7M | - | 600 | 550 | -$3.0M | +$397k bull / +$0 bear | out (clean 28, ADX 19, RVol 0.3) |
| 14 | **ARM** | 229.18 | - | **-** | 14 | - | POS +$3.4M | 221.32 | 227.5 | 220 | +$1.6M | - | out (clean 24, ADX 10, RVol 1.1) |
| 15 | **UBER** | 65.11 | - | **-** | 14 | - | NEG -$34.4M | 68.5 | 67 | 65 | -$162k | - | out (clean 27, ADX 15, RVol 0.4) |
| 16 | **SMCI** | 34.75 | - | **-** | 12 | - | POS +$22.3M | - | 35 | 35 | +$268k | - | out (clean 26, ADX 27, RVol 0.5) |
| 17 | **NFLX** | 61.66 | - | **-** | 11 | - | NEG -$54.5M | 64.62 | 63 | 61 | -$424k | - | out (clean 31, ADX 28, RVol 0.7) |
| 18 | **ORCL** | 137.18 | - | **-** | 11 | - | POS +$113.0M | - | 135 | 140 | +$1.2M | - | out (clean 32, ADX 43, RVol 0.7) |
| 19 | **CRM** | 231.72 | - | **-** | 8 | - | NEG -$20.0M | - | 240 | 230 | -$244k | - | out (clean 27, ADX 12, RVol 0.4) |
| 20 | **SPY** | 767.29 | - | **-** | 7 | - | NEG -$6.5B | 772.45 | 770 | 765 | -$91.0M | - | out (clean 25, ADX 22, RVol 0.3) |
| 21 | **BABA** | 99.27 | - | **-** | 7 | - | NEG -$20.8M | 101.47 | 100 | 100 | -$25k | - | out (clean 29, ADX 24, RVol 0.8) |
| 22 | **COIN** | 160.06 | - | **-** | 5 | - | POS +$4.6M | 153.7 | 170 | 155 | -$118k | - | out (clean 25, ADX 12, RVol 0.7) |
| 23 | **MSTR** | 141.74 | - | **-** | 5 | - | POS +$26.4M | - | 152.5 | 140 | +$171k | - | out (clean 25, ADX 15, RVol 0.8) |
| 24 | **HOOD** | 90.80 | - | **-** | 5 | - | NEG -$24.9M | 96.18 | 95 | 90 | -$371k | - | out (clean 28, ADX 18, RVol 0.3) |
| 25 | **SHOP** | 166.52 | - | **-** | 5 | - | NEG -$5.3M | 170.18 | 175 | 165 | -$29k | - | out (clean 25, ADX 12, RVol 0.3) |
| 26 | **AVGO** | 344.99 | - | **-** | 4 | - | POS +$31.4M | 340.75 | 350 | 340 | +$563k | - | out (clean 27, ADX 17, RVol 0.4) |
| 27 | **PLTR** | 193.64 | - | **-** | 4 | - | POS +$15.4M | 192.11 | 200 | 190 | -$230k | - | out (clean 25, ADX 18, RVol 0.3) |

## Big prints this scan (29)
- **QQQ** PUT 713 2026-11-02 (4DTE): 500 @ 4.93 = **+$246k** SELL | vol 2,286 / OI 742
- **QQQ** PUT 737 2026-10-30 (1DTE): 50 @ 23.22 = **+$116k** SELL | vol 100 / OI 2,539
- **QQQ** PUT 735 2026-10-30 (1DTE): 53 @ 20.95 = **+$111k** SELL | vol 360 / OI 9,129
- **QQQ** PUT 712 2026-10-29 (0DTE): 872 @ 1.15 = **+$100k** SELL | vol 161,563 / OI 1,739
- **MU** PUT 950 2026-11-02 (4DTE): 33 @ 25.65 = **+$85k** SELL | vol 1,493 / OI 521
- **MU** PUT 950 2026-11-02 (4DTE): 33 @ 25.65 = **+$85k** SELL | vol 1,493 / OI 521
- **MU** CALL 935 2026-10-30 (1DTE): 51 @ 16.10 = **+$82k** BUY | vol 2,898 / OI 1,088
- **DELL** CALL 480 2026-10-30 (1DTE): 109 @ 7.35 = **+$80k** BUY | vol 923 / OI 1,229
- **IWM** CALL 276 2026-10-30 (1DTE): 100 @ 7.88 = **+$79k** BUY | vol 800 / OI 2,871
- **MU** CALL 955 2026-10-30 (1DTE): 100 @ 7.25 = **+$72k** BUY | vol 14,083 / OI 878
- **META** CALL 602.5 2026-11-04 (6DTE): 19 @ 28.90 = **+$55k** BUY | vol 23 / OI 0
- **META** PUT 625 2026-10-30 (1DTE): 100 @ 5.32 = **+$53k** SELL | vol 9,707 / OI 3,179
- **IWM** CALL 281 2026-10-30 (1DTE): 169 @ 3.13 = **+$53k** BUY | vol 7,228 / OI 6,518
- **MU** CALL 930 2026-10-30 (1DTE): 25 @ 18.60 = **+$46k** BUY | vol 2,351 / OI 1,361
- **DELL** CALL 480 2026-10-30 (1DTE): 58 @ 7.35 = **+$43k** BUY | vol 923 / OI 1,229

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 745 2026-11-03 (5DTE): 504 traded vs OI 429
- **SPY** PUT 774 2026-10-30 (1DTE): 2,198 traded vs OI 2,182
- **SPY** PUT 740 2026-11-03 (5DTE): 739 traded vs OI 738
- **SPY** CALL 770 2026-11-12 (14DTE): 579 traded vs OI 0
- **IWM** PUT 268 2026-11-03 (5DTE): 2,002 traded vs OI 596
- **SMH** PUT 520 2026-11-02 (4DTE): 1,256 traded vs OI 1,122
- **NVDA** CALL 220 2026-10-30 (1DTE): 52,463 traded vs OI 52,363
- **NVDA** PUT 227.5 2026-11-06 (8DTE): 502 traded vs OI 136
- **TSLA** CALL 422.5 2026-11-06 (8DTE): 2,223 traded vs OI 174
- **META** CALL 645 2026-11-06 (8DTE): 3,216 traded vs OI 3,162
- **MSFT** CALL 527.5 2026-11-06 (8DTE): 503 traded vs OI 38
- **MSFT** PUT 525 2026-11-02 (4DTE): 589 traded vs OI 140
- **GOOGL** PUT 297.5 2026-10-30 (1DTE): 794 traded vs OI 778

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
