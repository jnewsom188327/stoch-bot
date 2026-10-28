# GEX + FLOW SCAN - Wed Oct 28, 11:50 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (4)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:40 | **HOOD** | **CALLS** | FLOW SURGE | 10/30 96C | 0.77 | 0.64 | -1% (3m) | **-17%** | +49% | 93.02 |
| 11:05 | **HOOD** | **CALLS** | FLOW SURGE | 10/30 97C | 0.63 | 0.52 | +19% (1m) | **-17%** | +53% | 93.44 |
| 10:50 | **IWM** | **CALLS** | FLOW SURGE | 10/30 284C | 0.57 | 0.54 | +7% (2m) | **-5%** | +22% | 280.64 |
| 10:20 | **IWM** | **CALLS** | FLOW SURGE | 10/29 284C | 0.47 | 0.34 | +11% (0m) | **-28%** (done) | +27% | 281.41 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **HOOD** | 91.06 | FLOW SURGE | **CALLS** | 43 | 10/30 96C @ 0.66 (delta 0.21) = est +49% at 92.58 | NEG -$16.9M | - | 100 | 90 | +$4.2M | +$102k bull / +$0 bear | out (clean 30, ADX 27, RVol 1.2) |
| 2 | **AAPL** | 345.08 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 33 | none: 81 calls 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (48 contracts' greeks worked out here) | POS +$330.8M | 341.24 | 350 | 345 | +$629k | +$160k bull / -$103k bear | out (clean 29, ADX 19, RVol 0.5) |
| 3 | **ORCL** | 130.11 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 33 | none: 26 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$8.9M | 126.86 | 135 | 130 | -$60k | +$0 bull / -$145k bear | out (clean 28, ADX 14, RVol 0.6) |
| 4 | **SMH** | 565.20 | - | **-** | 25 | - | POS +$55.1M | 560 | 570 | 555 | -$1.7M | +$76k bull / +$0 bear | out (clean 28, ADX 26, RVol 0.6) |
| 5 | **IWM** | 279.99 | - | **-** | 23 | - | NEG -$399.2M | 281.31 | 280 | 270 | +$9.6M | +$0 bull / -$343k bear | out (clean 24, ADX 19, RVol 0.8) |
| 6 | **PLTR** | 194.22 | - | **-** | 23 | - | POS +$43.4M | 188.99 | 200 | 190 | -$739k | +$0 bull / -$48k bear | out (clean 27, ADX 52, RVol 1.0) |
| 7 | **META** | 613.30 | - | **-** | 22 | - | NEG -$254.0M | 635.01 | 650 | 610 | +$9.7M | +$0 bull / -$447k bear | out (clean 29, ADX 27, RVol 0.8) |
| 8 | **MSFT** | 527.10 | - | **-** | 21 | - | POS +$423.2M | - | 550 | 500 | +$2.4M | +$223k bull / -$35k bear | out (clean 30, ADX 23, RVol 0.9) |
| 9 | **MU** | 970.48 | - | **-** | 20 | - | POS +$629.2M | - | 950 | 950 | +$20.4M | +$1.9M bull / -$57k bear | out (clean 28, ADX 35, RVol 0.3) |
| 10 | **TSLA** | 401.18 | - | **-** | 18 | - | POS +$598.1M | - | 400 | 395 | -$21.9M | +$576k bull / -$372k bear | out (clean 29, ADX 18, RVol 0.4) |
| 11 | **AMD** | 566.76 | - | **-** | 18 | - | POS +$180.0M | - | 600 | 550 | +$2.7M | +$28k bull / -$220k bear | out (clean 29, ADX 27, RVol 0.6) |
| 12 | **SHOP** | 165.41 | - | **-** | 18 | - | NEG -$5.7M | 172.05 | 175 | 165 | +$22k | - | out (clean 27, ADX 29, RVol 1.1) |
| 13 | **AVGO** | 345.91 | - | **-** | 16 | - | POS +$53.0M | 336.9 | 350 | 340 | +$610k | +$121k bull / -$73k bear | out (clean 29, ADX 14, RVol 0.8) |
| 14 | **NVDA** | 217.44 | - | **-** | 15 | - | POS +$544.6M | 210.11 | 220 | 215 | +$4.7M | +$143k bull / +$0 bear | out (clean 26, ADX 8, RVol 0.4) |
| 15 | **SPY** | 771.18 | - | **-** | 14 | - | NEG -$2.3B | 773.49 | 780 | 750 | -$11.7M | +$0 bull / -$1.9M bear | out (clean 29, ADX 12, RVol 0.4) |
| 16 | **GOOGL** | 323.75 | - | **-** | 14 | - | POS +$14.3M | 320.94 | 355 | 300 | -$263k | +$0 bull / -$2.8M bear | out (clean 33, ADX 14, RVol 0.6) |
| 17 | **AMZN** | 252.21 | - | **-** | 9 | - | POS +$168.5M | 243.64 | 250 | 250 | +$2.3M | - | out (clean 32, ADX 23, RVol 0.8) |
| 18 | **SMCI** | 34.77 | - | **-** | 9 | - | POS +$19.1M | - | 35 | 35 | +$129k | - | out (clean 28, ADX 18, RVol 0.2) |
| 19 | **UBER** | 65.47 | - | **-** | 9 | - | NEG -$30.2M | - | 70 | 65 | +$27k | - | out (clean 28, ADX 30, RVol 0.8) |
| 20 | **BABA** | 100.16 | - | **-** | 9 | - | NEG -$14.1M | 103.51 | 102 | 100 | +$39k | - | out (clean 28, ADX 13, RVol 0.5) |
| 21 | **NFLX** | 61.77 | - | **-** | 8 | - | NEG -$54.6M | - | 65 | 60 | -$6k | - | out (clean 32, ADX 41, RVol 0.4) |
| 22 | **ARM** | 232.63 | - | **-** | 8 | - | POS +$1.9M | 223.53 | 227.5 | 250 | +$112k | - | out (clean 27, ADX 28, RVol 0.4) |
| 23 | **DELL** | 497.49 | - | **-** | 6 | - | POS +$32.4M | - | 500 | 500 | -$62k | - | out (clean 30, ADX 19, RVol 0.9) |
| 24 | **COIN** | 158.34 | - | **-** | 5 | - | POS +$1.2M | 155.43 | 170 | 150 | -$20k | - | out (clean 29, ADX 12, RVol 0.5) |
| 25 | **CRM** | 240.82 | - | **-** | 5 | - | POS +$5.0M | 235 | 260 | 240 | +$10k | - | out (clean 28, ADX 20, RVol 0.3) |
| 26 | **QQQ** | 722.21 | - | **-** | 3 | - | NEG -$1.7B | 727.77 | 720 | 720 | -$9.5M | - | out (clean 30, ADX 9, RVol 0.3) |
| 27 | **MSTR** | 139.59 | - | **-** | 3 | - | POS +$16.7M | - | 152.5 | 140 | -$77k | - | out (clean 27, ADX 8, RVol 0.3) |

## Big prints this scan (32)
- **META** CALL 630 2026-10-30 (2DTE): 700 @ 3.05 = **+$214k** SELL | vol 7,469 / OI 476
- **SPY** CALL 772 2026-11-02 (5DTE): 252 @ 4.38 = **+$110k** SELL | vol 1,523 / OI 408
- **MU** CALL 970 2026-10-30 (2DTE): 50 @ 20.85 = **+$104k** BUY | vol 4,749 / OI 1,990
- **MU** PUT 935 2026-10-30 (2DTE): 100 @ 6.80 = **+$68k** SELL | vol 1,107 / OI 936
- **MU** CALL 950 2026-10-28 (0DTE): 30 @ 22.00 = **+$66k** BUY | vol 3,314 / OI 1,527
- **MU** PUT 965 2026-10-28 (0DTE): 183 @ 3.50 = **+$64k** SELL | vol 14,707 / OI 17
- **META** PUT 640 2026-10-30 (2DTE): 20 @ 30.09 = **+$60k** BUY | vol 192 / OI 1,094
- **MU** PUT 975 2026-10-30 (2DTE): 25 @ 21.88 = **+$55k** SELL | vol 1,607 / OI 305
- **AMD** CALL 570 2026-10-30 (2DTE): 50 @ 10.85 = **+$54k** SELL | vol 2,283 / OI 1,640
- **MU** CALL 1,000 2026-10-30 (2DTE): 50 @ 9.20 = **+$46k** BUY | vol 11,359 / OI 8,792
- **TSLA** PUT 392.5 2026-10-30 (2DTE): 225 @ 1.98 = **+$45k** SELL | vol 3,910 / OI 1,194
- **TSLA** PUT 397.5 2026-10-30 (2DTE): 130 @ 3.35 = **+$44k** SELL | vol 7,302 / OI 334
- **TSLA** CALL 410 2026-10-30 (2DTE): 161 @ 2.54 = **+$41k** BUY | vol 14,086 / OI 7,751
- **TSLA** CALL 410 2026-10-30 (2DTE): 139 @ 2.54 = **+$35k** BUY | vol 14,086 / OI 7,751
- **TSLA** PUT 392.5 2026-10-30 (2DTE): 174 @ 2.00 = **+$35k** SELL | vol 3,910 / OI 1,194

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 773 2026-11-02 (5DTE): 501 traded vs OI 271
- **NVDA** CALL 217.5 2026-11-06 (9DTE): 2,231 traded vs OI 1,505
- **AMD** CALL 572.5 2026-10-30 (2DTE): 569 traded vs OI 540
- **META** PUT 600 2026-10-30 (2DTE): 3,601 traded vs OI 3,579
- **META** PUT 600 2026-11-27 (30DTE): 718 traded vs OI 712
- **NFLX** CALL 65 2026-10-30 (2DTE): 8,821 traded vs OI 8,817
- **MU** PUT 875 2026-10-28 (0DTE): 605 traded vs OI 475
- **HOOD** PUT 84 2026-11-06 (9DTE): 519 traded vs OI 410
- **UBER** CALL 72 2026-11-20 (23DTE): 746 traded vs OI 0
- **BABA** CALL 103 2026-10-30 (2DTE): 1,297 traded vs OI 1,296

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
