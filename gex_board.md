# GEX + FLOW SCAN - Wed Oct 28, 02:00 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (6)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 12:56 | **QQQ** | **CALLS** | 1m WHIPSAW (R1 R2) | 10/28 730C | 0.63 | 0.67 | +24% (10m) | **+6%** (done) | -35% | 723.9 |
| 12:56 | **SPY** | **CALLS** | 1m WHIPSAW (R1 R2) | 10/29 779C | 0.63 | 0.51 | +3% (9m) | **-19%** (done) | +10% | 772.67 |
| 11:40 | **HOOD** | **CALLS** | FLOW SURGE | 10/30 96C | 0.77 | 0.55 | -1% (3m) | **-29%** (done) | +49% | 93.02 |
| 11:05 | **HOOD** | **CALLS** | FLOW SURGE | 10/30 97C | 0.63 | 0.45 | +19% (1m) | **-29%** (done) | +53% | 93.44 |
| 10:50 | **IWM** | **CALLS** | FLOW SURGE | 10/30 284C | 0.57 | 0.54 | +7% (2m) | **-5%** (done) | +22% | 280.64 |
| 10:20 | **IWM** | **CALLS** | FLOW SURGE | 10/29 284C | 0.47 | 0.34 | +11% (0m) | **-28%** (done) | +27% | 281.41 |

## 1m RULES on SPY / QQQ - loose (2 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 12:55 | QQQ | 1m WHIPSAW | R1 R2 | CALLS | WITH you | **FIRE** QQQ261028C00730000 |
| 12:55 | SPY | 1m WHIPSAW | R1 R2 | CALLS | WITH you | **FIRE** SPY261029C00779000 |

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **AAPL** | 345.25 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 34 | none: 81 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (46 contracts' greeks worked out here) | POS +$371.1M | 341.71 | 350 | 345 | +$789k | +$60k bull / -$44k bear | out (clean 28, ADX 14, RVol 0.9) |
| 2 | **MU** | 970.76 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 34 | none: 162 puts 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (63 contracts' greeks worked out here) | POS +$612.8M | - | 970 | 900 | +$18.5M | +$0 bull / -$2.7M bear | out (clean 28, ADX 20, RVol 0.5) |
| 3 | **ORCL** | 130.13 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 24 | none: 26 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$8.5M | 127.17 | 135 | 130 | -$900k | - | out (clean 29, ADX 11, RVol 0.4) |
| 4 | **MSTR** | 139.94 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 23 | none: 26 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | POS +$17.4M | - | 152.5 | 140 | +$583k | - | out (clean 27, ADX 13, RVol 0.4) |
| 5 | **IWM** | 280.38 | - | **-** | 22 | - | NEG -$324.8M | 281.15 | 280 | 270 | +$10.0M | +$173k bull / +$0 bear | out (clean 24, ADX 30, RVol 0.3) |
| 6 | **HOOD** | 90.88 | - | **-** | 22 | - | NEG -$17.4M | - | 95 | 90 | +$3.9M | +$0 bull / -$36k bear | out (clean 30, ADX 16, RVol 0.5) |
| 7 | **AMD** | 569.73 | - | **-** | 18 | - | POS +$190.3M | - | 600 | 550 | +$5.3M | +$1.3M bull / -$90k bear | out (clean 29, ADX 27, RVol 0.6) |
| 8 | **META** | 611.93 | - | **-** | 18 | - | NEG -$260.5M | 633.28 | 650 | 610 | +$8.2M | +$169k bull / +$0 bear | out (clean 28, ADX 17, RVol 0.7) |
| 9 | **PLTR** | 193.99 | - | **-** | 18 | - | POS +$40.6M | 189.53 | 200 | 190 | +$298k | +$52k bull / +$0 bear | out (clean 27, ADX 38, RVol 0.4) |
| 10 | **NVDA** | 217.02 | - | **-** | 17 | - | POS +$535.1M | 210.06 | 220 | 215 | +$8.4M | +$36k bull / -$59k bear | out (clean 26, ADX 18, RVol 0.7) |
| 11 | **GOOGL** | 324.50 | - | **-** | 17 | - | POS +$17.8M | 321.04 | 355 | 330 | -$1.2M | +$393k bull / -$130k bear | out (clean 32, ADX 26, RVol 0.8) |
| 12 | **AMZN** | 252.76 | - | **-** | 16 | - | POS +$184.9M | 243.86 | 255 | 250 | +$2.7M | +$96k bull / -$25k bear | out (clean 31, ADX 15, RVol 0.7) |
| 13 | **MSFT** | 526.84 | - | **-** | 16 | - | POS +$430.8M | - | 550 | 500 | -$1.1M | +$2.1M bull / -$5.6M bear | out (clean 29, ADX 14, RVol 1.2) |
| 14 | **AVGO** | 348.25 | - | **-** | 16 | - | POS +$61.4M | 337.02 | 350 | 340 | -$277k | +$31k bull / -$32k bear | out (clean 29, ADX 28, RVol 0.4) |
| 15 | **TSLA** | 402.53 | - | **-** | 15 | - | POS +$619.9M | - | 400 | 400 | -$17.6M | +$90k bull / -$322k bear | out (clean 29, ADX 14, RVol 0.2) |
| 16 | **SPY** | 771.34 | - | **-** | 13 | - | NEG -$2.2B | 773.36 | 780 | 750 | -$8.1M | +$3.6M bull / -$4.6M bear | out (clean 28, ADX 12, RVol 0.3) |
| 17 | **QQQ** | 722.62 | - | **-** | 13 | - | NEG -$1.5B | 727.51 | 720 | 720 | +$10.2M | +$0 bull / -$268k bear | out (clean 29, ADX 11, RVol 0.3) |
| 18 | **SMH** | 565.66 | - | **-** | 13 | - | POS +$65.5M | 559.52 | 570 | 555 | -$3.8M | - | out (clean 28, ADX 18, RVol 0.5) |
| 19 | **DELL** | 494.56 | - | **-** | 13 | - | POS +$28.1M | - | 500 | 500 | +$117k | +$46k bull / +$0 bear | out (clean 31, ADX 11, RVol 0.2) |
| 20 | **SHOP** | 168.43 | - | **-** | 11 | - | NEG -$3.6M | 171.95 | 175 | 165 | -$34k | - | out (clean 29, ADX 28, RVol 0.3) |
| 21 | **BABA** | 100.08 | - | **-** | 8 | - | NEG -$15.3M | 102.81 | 102 | 100 | +$68k | - | out (clean 28, ADX 14, RVol 0.5) |
| 22 | **SMCI** | 34.85 | - | **-** | 6 | - | POS +$18.5M | - | 35 | 35 | +$91k | - | out (clean 28, ADX 15, RVol 0.2) |
| 23 | **UBER** | 65.54 | - | **-** | 6 | - | NEG -$31.5M | 69.46 | 70 | 65 | +$17k | - | out (clean 30, ADX 25, RVol 0.4) |
| 24 | **NFLX** | 61.73 | - | **-** | 5 | - | NEG -$55.5M | - | 65 | 60 | -$88k | - | out (clean 31, ADX 12, RVol 0.6) |
| 25 | **COIN** | 159.50 | - | **-** | 5 | - | POS +$1.4M | 155.67 | 170 | 150 | +$28k | - | out (clean 29, ADX 11, RVol 1.0) |
| 26 | **ARM** | 232.46 | - | **-** | 4 | - | POS +$1.8M | 221.93 | 220 | 240 | +$93k | - | out (clean 26, ADX 13, RVol 0.3) |
| 27 | **CRM** | 241.11 | - | **-** | 4 | - | POS +$5.2M | 235.49 | 260 | 240 | +$9k | - | out (clean 27, ADX 14, RVol 0.5) |

## Big prints this scan (39)
- **MSFT** CALL 540 2026-10-30 (2DTE): 1,000 @ 7.70 = **+$770k** BUY | vol 3,677 / OI 7,800
- **MSFT** CALL 540 2026-10-30 (2DTE): 1,000 @ 7.69 = **+$769k** BUY | vol 3,677 / OI 7,800
- **MSFT** CALL 530 2026-10-30 (2DTE): 218 @ 11.97 = **+$261k** BUY | vol 3,564 / OI 7,642
- **MU** CALL 970 2026-10-28 (0DTE): 499 @ 4.90 = **+$245k** SELL | vol 34,127 / OI 3,109
- **MSFT** CALL 520 2026-10-30 (2DTE): 111 @ 17.03 = **+$189k** MID | vol 675 / OI 2,841
- **IWM** PUT 281 2026-10-29 (1DTE): 900 @ 1.92 = **+$173k** SELL | vol 3,600 / OI 22
- **MSFT** CALL 520 2026-10-30 (2DTE): 97 @ 17.03 = **+$165k** MID | vol 675 / OI 2,841
- **MSFT** CALL 510 2026-10-30 (2DTE): 50 @ 23.70 = **+$118k** BUY | vol 113 / OI 431
- **TSLA** PUT 402.5 2026-10-28 (0DTE): 479 @ 2.18 = **+$104k** BUY | vol 56,725 / OI 123
- **MSFT** CALL 520 2026-10-30 (2DTE): 59 @ 17.02 = **+$100k** MID | vol 675 / OI 2,841
- **MSFT** CALL 530 2026-10-30 (2DTE): 80 @ 11.97 = **+$96k** BUY | vol 3,564 / OI 7,642
- **MU** CALL 965 2026-10-28 (0DTE): 100 @ 7.45 = **+$74k** SELL | vol 10,944 / OI 281
- **SMH** CALL 567.5 2026-10-30 (2DTE): 100 @ 6.80 = **+$68k** MID | vol 549 / OI 410
- **MU** PUT 970 2026-10-30 (2DTE): 30 @ 21.00 = **+$63k** BUY | vol 6,791 / OI 562
- **AAPL** CALL 345 2026-10-28 (0DTE): 500 @ 1.20 = **+$60k** BUY | vol 41,138 / OI 1,839

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 715 2026-11-02 (5DTE): 746 traded vs OI 434
- **SMH** CALL 567.5 2026-10-30 (2DTE): 549 traded vs OI 410
- **NVDA** CALL 212.5 2026-11-04 (7DTE): 547 traded vs OI 134
- **AMD** CALL 592.5 2026-10-28 (0DTE): 583 traded vs OI 172
- **META** PUT 587.5 2026-10-28 (0DTE): 500 traded vs OI 164
- **MSFT** PUT 520 2026-11-20 (23DTE): 3,136 traded vs OI 2,480
- **MSFT** CALL 547.5 2026-11-06 (9DTE): 575 traded vs OI 81

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
