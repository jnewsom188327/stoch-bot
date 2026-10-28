# GEX + FLOW SCAN - Wed Oct 28, 11:30 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (3)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:05 | **HOOD** | **CALLS** | FLOW SURGE | 10/30 97C | 0.63 | 0.69 | +19% (1m) | **+10%** | +53% | 93.44 |
| 10:50 | **IWM** | **CALLS** | FLOW SURGE | 10/30 284C | 0.57 | 0.52 | +7% (2m) | **-9%** | +22% | 280.64 |
| 10:20 | **IWM** | **CALLS** | FLOW SURGE | 10/29 284C | 0.47 | 0.34 | +11% (0m) | **-28%** (done) | +27% | 281.41 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **HOOD** | 92.07 | FLOW SURGE | **CALLS** | 49 | 10/30 97C @ 0.69 (delta 0.21) = est +41% at 93.66 | NEG -$16.5M | - | 100 | 90 | +$3.0M | +$388k bull / +$0 bear | out (clean 30, ADX 28, RVol 2.2) |
| 2 | **GOOGL** | 323.25 | FLOW SURGE | **CALLS** | 35 | none: 78 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$11.8M | 320.93 | 355 | 300 | +$3.2M | +$70k bull / -$46k bear | out (clean 33, ADX 17, RVol 0.9) |
| 3 | **AAPL** | 345.56 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 34 | none: 84 calls 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (50 contracts' greeks worked out here) | POS +$363.6M | 341.24 | 350 | 345 | +$560k | +$543k bull / -$95k bear | out (clean 30, ADX 22, RVol 0.5) |
| 4 | **META** | 612.51 | - | **-** | 26 | - | NEG -$263.7M | 635.64 | 650 | 600 | +$12.0M | +$312k bull / -$348k bear | out (clean 29, ADX 32, RVol 1.0) |
| 5 | **MSFT** | 528.22 | - | **-** | 23 | - | POS +$465.7M | - | 550 | 500 | +$2.3M | +$40k bull / -$270k bear | out (clean 30, ADX 21, RVol 1.1) |
| 6 | **PLTR** | 194.39 | - | **-** | 21 | - | POS +$44.0M | 189.04 | 200 | 190 | -$232k | +$123k bull / +$0 bear | out (clean 28, ADX 54, RVol 1.2) |
| 7 | **MSTR** | 140.33 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 21 | none: 25 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$17.8M | - | 152.5 | 140 | -$243k | - | out (clean 28, ADX 9, RVol 0.3) |
| 8 | **SHOP** | 165.54 | - | **-** | 21 | - | NEG -$5.7M | 172.37 | 175 | 165 | +$26k | - | out (clean 27, ADX 26, RVol 0.9) |
| 9 | **TSLA** | 402.38 | - | **-** | 20 | - | POS +$599.9M | - | 400 | 395 | -$22.3M | +$0 bull / -$2.3M bear | out (clean 29, ADX 22, RVol 0.5) |
| 10 | **AMZN** | 252.23 | - | **-** | 20 | - | POS +$176.2M | 242.87 | 250 | 250 | +$2.3M | +$251k bull / -$1.0M bear | out (clean 32, ADX 24, RVol 1.2) |
| 11 | **MU** | 972.34 | - | **-** | 20 | - | POS +$618.6M | - | 950 | 950 | +$14.6M | +$1.5M bull / -$2.3M bear | out (clean 28, ADX 36, RVol 0.7) |
| 12 | **AMD** | 566.05 | - | **-** | 19 | - | POS +$178.7M | - | 550 | 550 | +$3.0M | +$454k bull / -$975k bear | out (clean 29, ADX 26, RVol 1.0) |
| 13 | **SMH** | 564.35 | - | **-** | 16 | - | POS +$54.9M | 559.54 | 570 | 555 | -$1.6M | - | out (clean 28, ADX 26, RVol 1.0) |
| 14 | **DELL** | 496.85 | - | **-** | 16 | - | POS +$31.5M | - | 500 | 500 | -$46k | +$0 bull / -$44k bear | out (clean 30, ADX 22, RVol 0.7) |
| 15 | **NVDA** | 217.65 | - | **-** | 15 | - | POS +$570.1M | 210.04 | 220 | 215 | +$3.4M | +$186k bull / -$30k bear | out (clean 26, ADX 8, RVol 0.5) |
| 16 | **CRM** | 240.90 | - | **-** | 15 | - | POS +$4.9M | 234.87 | 260 | 240 | +$7k | +$0 bull / -$27k bear | out (clean 28, ADX 22, RVol 0.2) |
| 17 | **SPY** | 770.99 | - | **-** | 14 | - | NEG -$2.5B | 773.49 | 780 | 750 | -$1.8M | +$0 bull / -$346k bear | out (clean 30, ADX 13, RVol 0.6) |
| 18 | **IWM** | 279.92 | - | **-** | 14 | - | NEG -$398.8M | 281.33 | 280 | 270 | +$10.0M | - | out (clean 24, ADX 19, RVol 0.6) |
| 19 | **QQQ** | 722.00 | - | **-** | 13 | - | NEG -$1.8B | 727.81 | 720 | 720 | -$3.3M | +$183k bull / -$101k bear | out (clean 30, ADX 10, RVol 0.3) |
| 20 | **AVGO** | 345.80 | - | **-** | 10 | - | POS +$55.0M | 336.56 | 350 | 340 | +$1.3M | - | out (clean 30, ADX 14, RVol 1.4) |
| 21 | **UBER** | 64.95 | - | **-** | 10 | - | NEG -$33.3M | - | 70 | 65 | +$35k | - | out (clean 28, ADX 35, RVol 0.4) |
| 22 | **NFLX** | 61.70 | - | **-** | 9 | - | NEG -$52.9M | - | 65 | 60 | +$8k | - | out (clean 32, ADX 46, RVol 0.6) |
| 23 | **SMCI** | 34.74 | - | **-** | 9 | - | POS +$18.5M | - | 35 | 35 | +$121k | - | out (clean 28, ADX 18, RVol 0.4) |
| 24 | **ORCL** | 129.66 | - | **-** | 9 | - | POS +$7.5M | 126.84 | 135 | 130 | +$249k | - | out (clean 28, ADX 18, RVol 0.7) |
| 25 | **BABA** | 100.11 | - | **-** | 9 | - | NEG -$14.1M | 103.11 | 102 | 100 | +$35k | - | out (clean 28, ADX 16, RVol 0.2) |
| 26 | **COIN** | 159.29 | - | **-** | 8 | - | POS +$1.8M | 154.96 | 170 | 150 | -$55k | - | out (clean 29, ADX 15, RVol 0.5) |
| 27 | **ARM** | 232.74 | - | **-** | 8 | - | POS +$2.0M | 222.21 | 227.5 | 250 | +$99k | - | out (clean 26, ADX 29, RVol 0.4) |

## Big prints this scan (76)
- **MU** CALL 975 2026-10-28 (0DTE): 798 @ 6.10 = **+$487k** BUY | vol 27,278 / OI 683
- **HOOD** CALL 94 2026-10-30 (2DTE): 2,431 @ 1.44 = **+$350k** BUY | vol 5,340 / OI 1,135
- **SMH** CALL 550 2026-10-30 (2DTE): 149 @ 18.00 = **+$268k** MID | vol 691 / OI 3,703
- **TSLA** CALL 397.5 2026-10-28 (0DTE): 524 @ 4.80 = **+$252k** SELL | vol 14,776 / OI 2,326
- **TSLA** CALL 397.5 2026-10-28 (0DTE): 467 @ 4.80 = **+$224k** SELL | vol 14,776 / OI 2,326
- **SMH** CALL 560 2026-10-30 (2DTE): 197 @ 11.00 = **+$217k** MID | vol 1,011 / OI 4,896
- **SMH** CALL 550 2026-10-30 (2DTE): 75 @ 18.00 = **+$135k** MID | vol 691 / OI 3,703
- **SMH** CALL 550 2026-10-30 (2DTE): 75 @ 18.00 = **+$135k** MID | vol 691 / OI 3,703
- **SMH** CALL 550 2026-10-30 (2DTE): 75 @ 18.00 = **+$135k** MID | vol 691 / OI 3,703
- **SMH** CALL 550 2026-10-30 (2DTE): 75 @ 18.00 = **+$135k** MID | vol 691 / OI 3,703
- **SMH** CALL 550 2026-10-30 (2DTE): 75 @ 18.00 = **+$135k** MID | vol 691 / OI 3,703
- **SMH** CALL 550 2026-10-30 (2DTE): 75 @ 18.00 = **+$135k** MID | vol 691 / OI 3,703
- **AMD** PUT 565 2026-10-28 (0DTE): 352 @ 3.30 = **+$116k** SELL | vol 3,183 / OI 19
- **TSLA** CALL 397.5 2026-10-28 (0DTE): 228 @ 4.80 = **+$109k** SELL | vol 14,776 / OI 2,326
- **TSLA** CALL 397.5 2026-10-28 (0DTE): 220 @ 4.80 = **+$106k** SELL | vol 14,776 / OI 2,326

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 767 2026-10-29 (1DTE): 915 traded vs OI 693
- **QQQ** CALL 748 2026-10-30 (2DTE): 1,191 traded vs OI 1,136
- **IWM** PUT 266 2026-11-04 (7DTE): 732 traded vs OI 168
- **IWM** PUT 275 2026-10-28 (0DTE): 6,350 traded vs OI 6,313
- **NVDA** CALL 207.5 2026-11-04 (7DTE): 506 traded vs OI 47
- **TSLA** PUT 415 2026-10-28 (0DTE): 502 traded vs OI 20
- **META** CALL 612.5 2026-10-30 (2DTE): 506 traded vs OI 17
- **META** PUT 590 2026-10-30 (2DTE): 971 traded vs OI 961
- **GOOGL** CALL 325 2026-11-06 (9DTE): 500 traded vs OI 389
- **MU** PUT 945 2026-10-30 (2DTE): 504 traded vs OI 251
- **MU** CALL 940 2026-10-28 (0DTE): 1,216 traded vs OI 1,185
- **HOOD** PUT 92 2026-11-06 (9DTE): 520 traded vs OI 224
- **HOOD** PUT 92 2026-10-30 (2DTE): 3,035 traded vs OI 2,938

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
