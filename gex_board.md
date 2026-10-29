# GEX + FLOW SCAN - Thu Oct 29, 11:20 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (4)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:30 | **IWM** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 10/29 284P | 0.65 | 0.25 | +3% (25m) | **-62%** | +232% | 281.86 |
| 10:00 | **ORCL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 10/30 145C | 0.79 | 0.84 | +18% (37m) | **+6%** (done) | +139% | 143.92 |
| 09:55 | **AAPL** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 10/30 345P | 0.77 | 0.68 | +17% (2m) | **-12%** (done) | +198% | 345 |
| 09:50 | **IWM** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 10/29 283P | 0.50 | 0.18 | +20% (21m) | **-64%** (done) | +159% | 282 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 11:20:08 ET, last candle SPY 11:19, QQQ 11:19 | no errors

## Flow surges NOT fired - price disagreed (2 today, last 5)
- 10:05 HOOD PUTS: price +0.99 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:00 HOOD PUTS: price +0.89 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **ARM** | 228.02 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 46 | none: 18 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (1 contracts' greeks worked out here) | POS +$2.7M | 223.33 | 227.5 | 220 | +$1.7M | - | out (clean 26, ADX 18, RVol 1.9) |
| 2 | **AMZN** | 247.40 | FLOW SURGE | **PUTS** | 37 | none: 57 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (8 contracts' greeks worked out here) | POS +$20.3M | 240.88 | 265 | 250 | -$14.1M | +$0 bull / -$776k bear | out (clean 31, ADX 33, RVol 1.0) |
| 3 | **GOOGL** | 286.07 | - | **-** | 28 | - | NEG -$208.6M | - | 300 | 290 | -$10.8M | +$0 bull / -$763k bear | out (clean 32, ADX 53, RVol 2.9) |
| 4 | **MSFT** | 523.27 | - | **-** | 27 | - | POS +$484.7M | 500.71 | 525 | 530 | +$27.4M | +$302k bull / -$999k bear | out (clean 28, ADX 21, RVol 1.9) |
| 5 | **META** | 629.04 | - | **-** | 26 | - | NEG -$16.3M | 630.16 | 650 | 625 | -$16.8M | +$0 bull / -$2.1M bear | out (clean 28, ADX 48, RVol 1.2) |
| 6 | **IWM** | 284.80 | - | **-** | 22 | - | POS +$880.6M | 281.95 | 284 | 270 | -$4.2M | +$0 bull / -$380k bear | out (clean 25, ADX 51, RVol 1.0) |
| 7 | **SPY** | 769.67 | - | **-** | 20 | - | NEG -$3.9B | 772.9 | 770 | 765 | -$116.1M | +$0 bull / -$2.8M bear | out (clean 25, ADX 12, RVol 0.6) |
| 8 | **TSLA** | 405.77 | - | **-** | 20 | - | POS +$500.9M | - | 400 | 400 | -$24.4M | +$362k bull / -$271k bear | out (clean 29, ADX 26, RVol 0.5) |
| 9 | **AAPL** | 348.43 | - | **-** | 20 | - | POS +$573.2M | 340.1 | 350 | 345 | +$6.2M | +$477k bull / -$123k bear | out (clean 29, ADX 33, RVol 0.7) |
| 10 | **QQQ** | 716.22 | - | **-** | 19 | - | NEG -$4.6B | 726.68 | 720 | 720 | -$84.3M | +$0 bull / -$1.0M bear | out (clean 26, ADX 18, RVol 0.5) |
| 11 | **MU** | 952.91 | - | **-** | 19 | - | POS +$389.8M | - | 950 | 950 | +$13.5M | +$1.6M bull / -$5.8M bear | out (clean 28, ADX 31, RVol 0.4) |
| 12 | **AMD** | 572.38 | - | **-** | 18 | - | POS +$146.5M | - | 600 | 550 | -$5.6M | +$0 bull / -$246k bear | out (clean 27, ADX 27, RVol 0.5) |
| 13 | **ORCL** | 141.03 | - | **-** | 18 | - | POS +$126.5M | - | 135 | 140 | -$505k | +$0 bull / -$25k bear | out (clean 31, ADX 25, RVol 0.8) |
| 14 | **UBER** | 65.48 | - | **-** | 18 | - | NEG -$30.2M | 68.27 | 67 | 65 | -$173k | - | out (clean 29, ADX 19, RVol 0.4) |
| 15 | **SMH** | 563.23 | FLIP CROSS down into negative gamma | **PUTS** | 17 | none: 135 puts 0-7DTE > 10 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (18 contracts' greeks worked out here) | NEG -$11.7M | 563.34 | 570 | 555 | +$4k | - | out (clean 26, ADX 12, RVol 0.7) |
| 16 | **NVDA** | 213.86 | - | **-** | 17 | - | POS +$232.2M | 210.94 | 215 | 210 | -$3.3M | +$101k bull / -$551k bear | out (clean 24, ADX 19, RVol 0.8) |
| 17 | **DELL** | 487.93 | - | **-** | 16 | - | POS +$13.4M | 476.99 | 500 | 500 | -$32k | +$0 bull / -$66k bear | out (clean 30, ADX 29, RVol 0.2) |
| 18 | **NFLX** | 62.05 | - | **-** | 15 | - | NEG -$49.2M | - | 63 | 60 | -$564k | - | out (clean 31, ADX 32, RVol 0.6) |
| 19 | **CRM** | 229.52 | - | **-** | 14 | - | NEG -$19.6M | - | 240 | 230 | -$188k | - | out (clean 27, ADX 35, RVol 0.9) |
| 20 | **BABA** | 100.00 | - | **-** | 13 | - | NEG -$14.2M | 101.84 | 102 | 100 | -$102k | - | out (clean 28, ADX 14, RVol 0.4) |
| 21 | **SHOP** | 167.06 | - | **-** | 12 | - | NEG -$6.2M | 172.25 | 175 | 165 | -$69k | - | out (clean 26, ADX 9, RVol 0.3) |
| 22 | **AVGO** | 343.98 | - | **-** | 10 | - | POS +$16.8M | 342.09 | 350 | 340 | +$2.2M | - | out (clean 28, ADX 22, RVol 0.5) |
| 23 | **COIN** | 160.41 | - | **-** | 9 | - | POS +$5.1M | 152.61 | 170 | 155 | -$111k | - | out (clean 26, ADX 18, RVol 1.7) |
| 24 | **SMCI** | 35.41 | - | **-** | 9 | - | POS +$25.9M | - | 35 | 35 | +$125k | - | out (clean 26, ADX 15, RVol 0.9) |
| 25 | **MSTR** | 143.27 | - | **-** | 8 | - | POS +$33.1M | - | 152.5 | 140 | -$677k | - | out (clean 26, ADX 16, RVol 1.1) |
| 26 | **HOOD** | 91.79 | - | **-** | 8 | - | NEG -$21.5M | - | 95 | 90 | -$954k | - | out (clean 28, ADX 14, RVol 0.7) |
| 27 | **PLTR** | 194.52 | - | **-** | 6 | - | POS +$28.1M | 191.61 | 200 | 190 | -$344k | - | out (clean 25, ADX 12, RVol 1.8) |

## Big prints this scan (66)
- **SPY** PUT 775 2026-11-02 (4DTE): 1,000 @ 6.60 = **+$660k** BUY | vol 12,960 / OI 149
- **META** PUT 660 2026-10-30 (1DTE): 100 @ 32.80 = **+$328k** BUY | vol 520 / OI 957
- **MU** CALL 955 2026-10-30 (1DTE): 215 @ 13.85 = **+$298k** BUY | vol 7,415 / OI 878
- **AAPL** CALL 335 2026-10-30 (1DTE): 130 @ 14.30 = **+$186k** BUY | vol 446 / OI 3,239
- **QQQ** CALL 710 2026-10-30 (1DTE): 200 @ 7.50 = **+$150k** SELL | vol 3,326 / OI 9,068
- **QQQ** CALL 710 2026-10-30 (1DTE): 200 @ 7.50 = **+$150k** SELL | vol 3,326 / OI 9,068
- **MU** CALL 955 2026-10-30 (1DTE): 100 @ 13.50 = **+$135k** BUY | vol 7,415 / OI 878
- **AMZN** CALL 250 2026-10-30 (1DTE): 125 @ 8.50 = **+$106k** SELL | vol 4,612 / OI 7,932
- **AMZN** CALL 240 2026-10-30 (1DTE): 65 @ 13.70 = **+$89k** SELL | vol 1,533 / OI 742
- **MSFT** CALL 527.5 2026-10-30 (1DTE): 240 @ 3.67 = **+$88k** BUY | vol 6,307 / OI 644
- **AMD** CALL 565 2026-10-30 (1DTE): 70 @ 12.50 = **+$88k** SELL | vol 1,848 / OI 956
- **AMZN** CALL 252.5 2026-10-30 (1DTE): 100 @ 7.43 = **+$74k** SELL | vol 975 / OI 6,011
- **META** CALL 650 2026-11-04 (6DTE): 150 @ 4.79 = **+$72k** SELL | vol 457 / OI 542
- **AMZN** CALL 252.5 2026-10-30 (1DTE): 91 @ 7.43 = **+$68k** SELL | vol 975 / OI 6,011
- **AMZN** CALL 255 2026-10-30 (1DTE): 100 @ 6.47 = **+$65k** SELL | vol 3,332 / OI 12,075

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 768 2026-11-03 (5DTE): 919 traded vs OI 906
- **SPY** CALL 788 2026-11-02 (4DTE): 626 traded vs OI 199
- **SPY** CALL 787 2026-11-02 (4DTE): 598 traded vs OI 329
- **QQQ** CALL 715 2026-11-04 (6DTE): 519 traded vs OI 310
- **QQQ** CALL 717 2026-11-06 (8DTE): 510 traded vs OI 251
- **QQQ** CALL 750 2026-11-11 (13DTE): 526 traded vs OI 0
- **NVDA** PUT 205 2026-11-04 (6DTE): 1,096 traded vs OI 1,032
- **AAPL** PUT 360 2026-11-06 (8DTE): 1,093 traded vs OI 168
- **AMD** PUT 545 2026-10-30 (1DTE): 1,411 traded vs OI 1,405
- **META** CALL 665 2026-11-02 (4DTE): 662 traded vs OI 196
- **META** CALL 667.5 2026-11-02 (4DTE): 898 traded vs OI 243
- **MSFT** CALL 530 2026-11-02 (4DTE): 2,781 traded vs OI 2,635
- **GOOGL** CALL 290 2026-11-04 (6DTE): 539 traded vs OI 3

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
