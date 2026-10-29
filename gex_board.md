# GEX + FLOW SCAN - Thu Oct 29, 12:10 PM ET
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
Last 1m check 12:10:08 ET, last candle SPY 12:09, QQQ 12:09 | no errors

## Flow surges NOT fired - price disagreed (2 today, last 5)
- 10:05 HOOD PUTS: price +0.99 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:00 HOOD PUTS: price +0.89 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **ARM** | 230.50 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 48 | none: 19 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (7 contracts' greeks worked out here) | POS +$3.2M | 223.33 | 227.5 | 230 | +$1.5M | +$0 bull / -$32k bear | out (clean 26, ADX 20, RVol 1.2) |
| 2 | **MSFT** | 524.07 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 42 | none: 126 puts 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (3 contracts' greeks worked out here) | POS +$507.2M | 502.13 | 525 | 530 | +$27.8M | +$114k bull / -$280k bear | out (clean 28, ADX 12, RVol 0.9) |
| 3 | **IWM** | 284.42 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 39 | none: 307 puts 0-7DTE > 16 priced 0.40-0.80 > 4 delta 0.2+ > 4 spread ok > 4 liquid > best one only +14% at the target (needs +20%) (132 contracts' greeks worked out here) | POS +$883.4M | 281.58 | 284 | 270 | -$3.8M | +$3.0M bull / -$363k bear | out (clean 25, ADX 47, RVol 0.7) |
| 4 | **GOOGL** | 286.23 | - | **-** | 26 | - | NEG -$209.2M | - | 300 | 290 | -$11.2M | +$2.2M bull / -$277k bear | out (clean 32, ADX 42, RVol 2.1) |
| 5 | **META** | 629.78 | - | **-** | 24 | - | NEG -$11.6M | 630.4 | 650 | 625 | -$19.8M | +$425k bull / -$208k bear | out (clean 28, ADX 46, RVol 0.8) |
| 6 | **CRM** | 231.23 | - | **-** | 24 | - | NEG -$20.1M | - | 240 | 230 | -$233k | +$0 bull / -$27k bear | out (clean 26, ADX 33, RVol 1.1) |
| 7 | **ORCL** | 139.79 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 23 | 10/30 144C @ 0.70 (delta 0.22) = est +52% at 141.52 | POS +$126.5M | - | 135 | 140 | -$11k | - | out (clean 31, ADX 20, RVol 0.6) |
| 8 | **AMZN** | 246.61 | - | **-** | 20 | - | POS +$12.6M | 242.62 | 265 | 250 | -$10.1M | +$1.4M bull / +$0 bear | out (clean 31, ADX 21, RVol 0.7) |
| 9 | **SPY** | 769.59 | - | **-** | 19 | - | NEG -$4.0B | 772.72 | 770 | 765 | -$135.9M | +$2.2M bull / -$1.9M bear | out (clean 25, ADX 11, RVol 0.7) |
| 10 | **MU** | 946.55 | - | **-** | 19 | - | POS +$360.2M | - | 950 | 950 | +$21.4M | +$762k bull / -$557k bear | out (clean 27, ADX 27, RVol 0.7) |
| 11 | **TSLA** | 405.67 | - | **-** | 18 | - | POS +$528.7M | - | 400 | 400 | -$20.7M | +$577k bull / +$0 bear | out (clean 29, ADX 20, RVol 0.5) |
| 12 | **QQQ** | 716.15 | - | **-** | 17 | - | NEG -$4.6B | 726.39 | 720 | 720 | -$86.1M | +$376k bull / -$200k bear | out (clean 27, ADX 12, RVol 0.5) |
| 13 | **AAPL** | 349.09 | - | **-** | 17 | - | POS +$610.8M | 340.5 | 350 | 345 | +$3.3M | +$83k bull / -$507k bear | out (clean 28, ADX 24, RVol 0.7) |
| 14 | **AVGO** | 344.82 | - | **-** | 17 | - | POS +$31.1M | 340.41 | 350 | 340 | +$1.5M | +$0 bull / -$28k bear | out (clean 27, ADX 18, RVol 0.8) |
| 15 | **HOOD** | 92.18 | - | **-** | 17 | - | NEG -$20.3M | - | 95 | 90 | -$769k | +$45k bull / +$0 bear | out (clean 28, ADX 18, RVol 0.5) |
| 16 | **NVDA** | 213.84 | - | **-** | 15 | - | POS +$235.3M | 211.03 | 215 | 210 | -$5.4M | +$0 bull / -$139k bear | out (clean 24, ADX 11, RVol 0.7) |
| 17 | **AMD** | 572.04 | - | **-** | 15 | - | POS +$149.1M | - | 600 | 550 | -$5.6M | +$165k bull / -$137k bear | out (clean 27, ADX 15, RVol 0.4) |
| 18 | **NFLX** | 62.09 | - | **-** | 15 | - | NEG -$46.4M | 64.62 | 63 | 60 | -$556k | - | out (clean 31, ADX 37, RVol 0.7) |
| 19 | **UBER** | 65.44 | - | **-** | 15 | - | NEG -$30.1M | 68.21 | 67 | 65 | -$174k | - | out (clean 28, ADX 15, RVol 0.3) |
| 20 | **COIN** | 162.18 | - | **-** | 9 | - | POS +$7.3M | - | 170 | 155 | -$330k | - | out (clean 26, ADX 13, RVol 1.3) |
| 21 | **MSTR** | 144.38 | - | **-** | 9 | - | POS +$36.3M | - | 152.5 | 140 | -$797k | - | out (clean 26, ADX 24, RVol 1.4) |
| 22 | **SHOP** | 166.84 | - | **-** | 8 | - | NEG -$6.1M | 173.12 | 175 | 165 | -$44k | - | out (clean 26, ADX 10, RVol 0.3) |
| 23 | **BABA** | 99.73 | - | **-** | 8 | - | NEG -$15.5M | 101.44 | 102 | 100 | -$66k | - | out (clean 28, ADX 13, RVol 0.4) |
| 24 | **DELL** | 486.51 | - | **-** | 7 | - | POS +$9.3M | 477.81 | 500 | 500 | +$275k | - | out (clean 29, ADX 28, RVol 0.5) |
| 25 | **SMCI** | 35.39 | - | **-** | 7 | - | POS +$26.2M | - | 35 | 35 | +$134k | - | out (clean 26, ADX 13, RVol 0.4) |
| 26 | **SMH** | 563.69 | - | **-** | 4 | - | POS +$11.6M | 562.68 | 570 | 555 | -$103k | - | out (clean 26, ADX 15, RVol 0.5) |
| 27 | **PLTR** | 195.07 | - | **-** | 4 | - | POS +$32.3M | 191.77 | 200 | 190 | -$910k | - | out (clean 25, ADX 8, RVol 0.4) |

## Big prints this scan (36)
- **GOOGL** PUT 287.5 2026-11-02 (4DTE): 500 @ 5.00 = **+$250k** BUY | vol 1,182 / OI 70
- **QQQ** CALL 707 2026-10-29 (0DTE): 185 @ 9.43 = **+$174k** BUY | vol 3,596 / OI 185
- **IWM** PUT 285 2026-10-30 (1DTE): 1,205 @ 1.43 = **+$172k** MID | vol 25,042 / OI 761
- **IWM** PUT 284 2026-10-30 (1DTE): 1,439 @ 0.98 = **+$141k** BUY | vol 56,250 / OI 301
- **SPY** CALL 770 2026-10-29 (0DTE): 1,000 @ 1.14 = **+$114k** SELL | vol 327,664 / OI 1,967
- **IWM** CALL 276 2026-10-30 (1DTE): 122 @ 8.54 = **+$104k** BUY | vol 681 / OI 2,871
- **MU** CALL 930 2026-10-30 (1DTE): 41 @ 24.99 = **+$102k** BUY | vol 1,752 / OI 1,361
- **IWM** PUT 284 2026-10-30 (1DTE): 1,086 @ 0.93 = **+$101k** SELL | vol 56,250 / OI 301
- **IWM** PUT 284 2026-10-30 (1DTE): 1,054 @ 0.95 = **+$100k** MID | vol 56,250 / OI 301
- **MU** CALL 930 2026-10-30 (1DTE): 40 @ 24.99 = **+$100k** BUY | vol 1,752 / OI 1,361
- **IWM** PUT 285 2026-10-29 (0DTE): 1,169 @ 0.80 = **+$94k** SELL | vol 37,539 / OI 57
- **IWM** CALL 276 2026-10-30 (1DTE): 95 @ 8.60 = **+$82k** BUY | vol 681 / OI 2,871
- **IWM** CALL 276 2026-10-30 (1DTE): 89 @ 8.56 = **+$76k** BUY | vol 681 / OI 2,871
- **MU** PUT 945 2026-10-30 (1DTE): 61 @ 11.75 = **+$72k** SELL | vol 5,230 / OI 239
- **IWM** CALL 276 2026-10-30 (1DTE): 83 @ 8.61 = **+$71k** BUY | vol 681 / OI 2,871

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 749 2026-10-29 (0DTE): 565 traded vs OI 529
- **QQQ** CALL 732 2026-11-02 (4DTE): 507 traded vs OI 274
- **IWM** CALL 283 2026-11-02 (4DTE): 509 traded vs OI 421
- **IWM** PUT 270 2026-11-27 (29DTE): 1,755 traded vs OI 707
- **META** CALL 680 2026-11-06 (8DTE): 768 traded vs OI 763
- **GOOGL** CALL 290 2026-11-27 (29DTE): 1,065 traded vs OI 14
- **GOOGL** PUT 280 2026-11-13 (15DTE): 817 traded vs OI 548
- **NFLX** CALL 59 2026-11-20 (22DTE): 515 traded vs OI 18
- **AVGO** CALL 345 2026-11-02 (4DTE): 528 traded vs OI 248
- **AVGO** CALL 342.5 2026-11-02 (4DTE): 565 traded vs OI 281
- **MU** PUT 875 2026-10-30 (1DTE): 961 traded vs OI 943
- **MU** CALL 950 2026-10-30 (1DTE): 12,736 traded vs OI 12,588

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
