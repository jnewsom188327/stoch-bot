# GEX + FLOW SCAN - Thu Oct 29, 12:00 PM ET
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
Last 1m check 12:00:08 ET, last candle SPY 11:59, QQQ 11:59 | no errors

## Flow surges NOT fired - price disagreed (2 today, last 5)
- 10:05 HOOD PUTS: price +0.99 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:00 HOOD PUTS: price +0.89 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **MSFT** | 523.77 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 42 | none: 126 puts 0-7DTE > 9 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (6 contracts' greeks worked out here) | POS +$502.6M | 501.3 | 525 | 530 | +$28.4M | +$118k bull / -$158k bear | out (clean 28, ADX 13, RVol 0.9) |
| 2 | **AAPL** | 349.25 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 36 | 10/30 345P @ 0.65 (delta 0.21) = est +46% at 347.76 | POS +$610.0M | 340.32 | 350 | 345 | +$3.9M | +$40k bull / -$222k bear | out (clean 28, ADX 25, RVol 0.7) |
| 3 | **MU** | 951.04 | PINNED between the walls (positive gamma) - chop | **-** | 34 | - | POS +$368.9M | - | 950 | 950 | +$20.0M | +$597k bull / -$532k bear | out (clean 27, ADX 28, RVol 0.8) |
| 4 | **ORCL** | 140.27 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 33 | 10/30 145C @ 0.63 (delta 0.20) = est +62% at 142.13 | POS +$120.6M | - | 135 | 140 | -$128k | +$52k bull / +$0 bear | out (clean 31, ADX 21, RVol 0.6) |
| 5 | **ARM** | 231.62 | - | **-** | 28 | - | POS +$4.2M | 219.93 | 227.5 | 250 | +$1.4M | +$0 bull / -$32k bear | out (clean 26, ADX 19, RVol 2.0) |
| 6 | **GOOGL** | 286.81 | - | **-** | 27 | - | NEG -$208.2M | - | 300 | 290 | -$10.5M | +$2.3M bull / +$0 bear | out (clean 32, ADX 45, RVol 2.3) |
| 7 | **META** | 630.43 | - | **-** | 24 | - | NEG -$1.4M | 630.98 | 650 | 625 | -$19.2M | +$809k bull / -$147k bear | out (clean 28, ADX 46, RVol 0.8) |
| 8 | **AMZN** | 247.41 | - | **-** | 22 | - | POS +$18.5M | 241.43 | 265 | 250 | -$11.7M | +$1.3M bull / +$0 bear | out (clean 32, ADX 22, RVol 0.8) |
| 9 | **IWM** | 284.75 | - | **-** | 21 | - | POS +$927.6M | 281.78 | 284 | 270 | -$4.5M | +$407k bull / +$0 bear | out (clean 25, ADX 50, RVol 0.7) |
| 10 | **SPY** | 770.15 | - | **-** | 19 | - | NEG -$3.5B | 772.98 | 770 | 765 | -$130.1M | +$2.9M bull / +$0 bear | out (clean 26, ADX 11, RVol 0.7) |
| 11 | **TSLA** | 405.97 | - | **-** | 19 | - | POS +$515.3M | - | 400 | 400 | -$21.7M | +$665k bull / -$76k bear | out (clean 29, ADX 22, RVol 0.6) |
| 12 | **QQQ** | 717.47 | - | **-** | 18 | - | NEG -$4.1B | 726.75 | 720 | 720 | -$97.2M | +$636k bull / -$200k bear | out (clean 27, ADX 13, RVol 0.7) |
| 13 | **AVGO** | 345.97 | - | **-** | 17 | - | POS +$32.2M | 341.57 | 350 | 340 | +$1.2M | +$211k bull / +$0 bear | out (clean 27, ADX 18, RVol 1.0) |
| 14 | **HOOD** | 92.02 | - | **-** | 17 | - | NEG -$20.2M | 97.48 | 95 | 90 | -$648k | +$74k bull / +$0 bear | out (clean 28, ADX 17, RVol 0.9) |
| 15 | **NVDA** | 214.36 | - | **-** | 16 | - | POS +$273.4M | 211.09 | 215 | 210 | -$6.0M | +$30k bull / -$139k bear | out (clean 24, ADX 12, RVol 0.8) |
| 16 | **AMD** | 574.72 | - | **-** | 16 | - | POS +$143.6M | - | 600 | 550 | -$7.1M | +$447k bull / -$137k bear | out (clean 27, ADX 17, RVol 0.4) |
| 17 | **UBER** | 65.36 | - | **-** | 16 | - | NEG -$31.4M | 67.94 | 67 | 65 | -$174k | - | out (clean 29, ADX 16, RVol 0.3) |
| 18 | **SMH** | 565.70 | - | **-** | 15 | - | POS +$32.9M | 563.83 | 570 | 555 | -$131k | +$73k bull / +$0 bear | out (clean 26, ADX 14, RVol 0.6) |
| 19 | **NFLX** | 62.16 | - | **-** | 15 | - | NEG -$44.3M | - | 63 | 60 | -$565k | - | out (clean 31, ADX 38, RVol 0.6) |
| 20 | **CRM** | 230.21 | - | **-** | 14 | - | NEG -$20.4M | - | 240 | 230 | -$174k | - | out (clean 27, ADX 37, RVol 1.3) |
| 21 | **BABA** | 99.88 | - | **-** | 9 | - | NEG -$14.6M | 101.51 | 102 | 100 | -$75k | - | out (clean 28, ADX 12, RVol 0.4) |
| 22 | **SHOP** | 167.12 | - | **-** | 8 | - | NEG -$5.5M | 172.54 | 175 | 165 | -$44k | - | out (clean 26, ADX 10, RVol 0.4) |
| 23 | **DELL** | 488.24 | - | **-** | 7 | - | POS +$11.9M | 478.26 | 500 | 500 | +$262k | - | out (clean 29, ADX 28, RVol 0.5) |
| 24 | **SMCI** | 35.57 | - | **-** | 7 | - | POS +$27.3M | - | 35 | 35 | +$130k | - | out (clean 26, ADX 14, RVol 0.5) |
| 25 | **MSTR** | 143.91 | - | **-** | 7 | - | POS +$34.7M | - | 152.5 | 140 | -$627k | - | out (clean 26, ADX 22, RVol 0.8) |
| 26 | **COIN** | 161.83 | - | **-** | 6 | - | POS +$7.1M | - | 170 | 155 | -$151k | - | out (clean 26, ADX 13, RVol 0.8) |
| 27 | **PLTR** | 195.45 | - | **-** | 4 | - | POS +$34.9M | 191.89 | 200 | 190 | -$984k | - | out (clean 25, ADX 8, RVol 0.5) |

## Big prints this scan (42)
- **GOOGL** PUT 285 2026-11-02 (4DTE): 1,000 @ 3.00 = **+$300k** SELL | vol 4,755 / OI 80
- **GOOGL** PUT 287.5 2026-11-02 (4DTE): 500 @ 4.30 = **+$215k** SELL | vol 681 / OI 70
- **QQQ** PUT 724 2026-11-03 (5DTE): 200 @ 10.00 = **+$200k** BUY | vol 227 / OI 24
- **AMZN** CALL 257.5 2026-10-30 (1DTE): 250 @ 6.18 = **+$154k** BUY | vol 1,755 / OI 2,517
- **AMZN** CALL 257.5 2026-10-30 (1DTE): 250 @ 6.18 = **+$154k** BUY | vol 1,755 / OI 2,517
- **AMZN** CALL 240 2026-10-30 (1DTE): 95 @ 14.56 = **+$138k** BUY | vol 2,338 / OI 742
- **SPY** CALL 771 2026-10-29 (0DTE): 1,083 @ 1.12 = **+$121k** BUY | vol 187,011 / OI 1,080
- **MSFT** CALL 532.5 2026-11-04 (6DTE): 275 @ 4.25 = **+$117k** SELL | vol 911 / OI 84
- **NVDA** PUT 215 2026-10-30 (1DTE): 444 @ 2.30 = **+$102k** BUY | vol 17,279 / OI 12,332
- **GOOGL** PUT 300 2026-10-30 (1DTE): 50 @ 12.50 = **+$62k** SELL | vol 10,495 / OI 8,616
- **META** PUT 625 2026-10-30 (1DTE): 130 @ 4.60 = **+$60k** BUY | vol 5,820 / OI 3,179
- **MU** CALL 930 2026-11-02 (4DTE): 18 @ 30.42 = **+$55k** SELL | vol 151 / OI 269
- **IWM** CALL 285 2026-11-02 (4DTE): 300 @ 1.80 = **+$54k** BUY | vol 3,175 / OI 446
- **MU** CALL 950 2026-10-30 (1DTE): 40 @ 13.00 = **+$52k** SELL | vol 12,301 / OI 12,588
- **GOOGL** CALL 290 2026-10-30 (1DTE): 184 @ 2.58 = **+$47k** BUY | vol 37,410 / OI 113

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 766 2026-10-30 (1DTE): 13,025 traded vs OI 12,971
- **SPY** PUT 765 2026-11-02 (4DTE): 3,833 traded vs OI 3,697
- **SPY** PUT 768 2026-11-04 (6DTE): 1,308 traded vs OI 1,296
- **SPY** PUT 770 2026-11-05 (7DTE): 1,072 traded vs OI 1,043
- **SPY** PUT 755 2026-11-05 (7DTE): 623 traded vs OI 290
- **QQQ** PUT 717 2026-11-03 (5DTE): 513 traded vs OI 118
- **QQQ** PUT 706 2026-11-02 (4DTE): 535 traded vs OI 283
- **QQQ** PUT 716 2026-11-03 (5DTE): 505 traded vs OI 276
- **QQQ** CALL 725 2026-11-03 (5DTE): 587 traded vs OI 537
- **QQQ** PUT 688 2026-10-30 (1DTE): 1,233 traded vs OI 1,064
- **QQQ** CALL 712 2026-11-06 (8DTE): 506 traded vs OI 234
- **QQQ** PUT 710 2026-11-05 (7DTE): 535 traded vs OI 336
- **IWM** CALL 284 2026-11-02 (4DTE): 846 traded vs OI 844
- **TSLA** CALL 417.5 2026-11-02 (4DTE): 500 traded vs OI 399
- **AAPL** CALL 347.5 2026-10-30 (1DTE): 8,171 traded vs OI 7,887

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
