# GEX + FLOW SCAN - Thu Oct 29, 12:40 PM ET
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
Last 1m check 12:40:08 ET, last candle SPY 12:39, QQQ 12:39 | no errors

## Flow surges NOT fired - price disagreed (2 today, last 5)
- 10:05 HOOD PUTS: price +0.99 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 10:00 HOOD PUTS: price +0.89 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **MSFT** | 524.57 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 42 | none: 126 puts 0-7DTE > 8 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (6 contracts' greeks worked out here) | POS +$520.5M | 501.62 | 525 | 530 | +$27.0M | +$366k bull / -$221k bear | out (clean 28, ADX 12, RVol 1.0) |
| 2 | **IWM** | 284.30 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 36 | none: 307 puts 0-7DTE > 16 priced 0.40-0.80 > 6 delta 0.2+ > 6 spread ok > 6 liquid > best one only +8% at the target (needs +20%) (123 contracts' greeks worked out here) | POS +$776.5M | 282.61 | 284 | 270 | -$2.5M | +$93k bull / -$228k bear | out (clean 25, ADX 35, RVol 0.5) |
| 3 | **AAPL** | 349.26 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 35 | none: 55 puts 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (9 contracts' greeks worked out here) | POS +$612.7M | 340.56 | 350 | 345 | +$3.1M | +$26k bull / +$0 bear | out (clean 28, ADX 21, RVol 0.7) |
| 4 | **META** | 634.39 | - | **-** | 24 | - | POS +$44.3M | 630.54 | 650 | 625 | -$17.7M | +$0 bull / -$389k bear | out (clean 28, ADX 45, RVol 0.9) |
| 5 | **GOOGL** | 285.38 | - | **-** | 24 | - | NEG -$191.3M | - | 300 | 290 | -$12.1M | +$395k bull / -$651k bear | out (clean 32, ADX 40, RVol 1.3) |
| 6 | **MU** | 941.68 | - | **-** | 21 | - | POS +$317.9M | - | 950 | 950 | +$32.9M | +$6.7M bull / +$0 bear | out (clean 27, ADX 31, RVol 0.7) |
| 7 | **AMZN** | 246.53 | - | **-** | 19 | - | POS +$15.2M | 241.89 | 265 | 250 | -$8.8M | +$270k bull / -$251k bear | out (clean 32, ADX 21, RVol 0.8) |
| 8 | **AVGO** | 343.92 | - | **-** | 18 | - | POS +$15.7M | 341.98 | 350 | 340 | +$2.2M | +$26k bull / +$0 bear | out (clean 27, ADX 12, RVol 0.9) |
| 9 | **SPY** | 769.03 | - | **-** | 17 | - | NEG -$4.5B | 772.57 | 770 | 765 | -$110.3M | +$775k bull / -$826k bear | out (clean 25, ADX 9, RVol 0.6) |
| 10 | **TSLA** | 405.55 | - | **-** | 17 | - | POS +$490.0M | - | 400 | 400 | -$20.9M | +$361k bull / -$180k bear | out (clean 28, ADX 15, RVol 0.4) |
| 11 | **MSTR** | 143.33 | - | **-** | 17 | - | POS +$32.9M | - | 152.5 | 140 | -$406k | +$37k bull / +$0 bear | out (clean 26, ADX 21, RVol 0.9) |
| 12 | **QQQ** | 715.16 | - | **-** | 16 | - | NEG -$5.0B | 725.62 | 720 | 720 | -$66.4M | +$778k bull / +$0 bear | out (clean 27, ADX 12, RVol 0.4) |
| 13 | **NVDA** | 213.51 | - | **-** | 15 | - | POS +$210.6M | 211.06 | 215 | 210 | -$3.8M | +$361k bull / -$119k bear | out (clean 24, ADX 13, RVol 0.7) |
| 14 | **AMD** | 568.93 | - | **-** | 15 | - | POS +$152.7M | - | 600 | 550 | -$2.3M | +$769k bull / -$38k bear | out (clean 27, ADX 16, RVol 0.6) |
| 15 | **ARM** | 230.41 | - | **-** | 15 | - | POS +$3.9M | 220.95 | 227.5 | 240 | +$1.6M | - | out (clean 25, ADX 16, RVol 0.6) |
| 16 | **SMH** | 561.79 | - | **-** | 14 | - | NEG -$31.6M | 563.36 | 560 | 555 | +$282k | +$31k bull / +$0 bear | out (clean 26, ADX 12, RVol 0.4) |
| 17 | **UBER** | 65.43 | - | **-** | 14 | - | NEG -$30.5M | 68.23 | 67 | 65 | -$166k | - | out (clean 28, ADX 13, RVol 0.4) |
| 18 | **NFLX** | 62.12 | - | **-** | 13 | - | NEG -$48.6M | - | 63 | 60 | -$546k | - | out (clean 30, ADX 32, RVol 0.4) |
| 19 | **CRM** | 230.92 | - | **-** | 11 | - | NEG -$20.7M | - | 240 | 230 | -$242k | - | out (clean 27, ADX 22, RVol 0.8) |
| 20 | **DELL** | 484.02 | - | **-** | 8 | - | POS +$8.0M | 477.32 | 500 | 480 | +$642k | - | out (clean 29, ADX 30, RVol 0.3) |
| 21 | **SMCI** | 35.18 | - | **-** | 8 | - | POS +$25.3M | - | 35 | 35 | +$176k | - | out (clean 26, ADX 12, RVol 0.4) |
| 22 | **SHOP** | 167.11 | - | **-** | 8 | - | NEG -$5.7M | 171.7 | 175 | 165 | -$48k | - | out (clean 26, ADX 12, RVol 0.4) |
| 23 | **COIN** | 161.51 | - | **-** | 7 | - | POS +$7.0M | - | 170 | 155 | -$215k | - | out (clean 26, ADX 10, RVol 1.3) |
| 24 | **ORCL** | 138.50 | - | **-** | 6 | - | POS +$113.6M | - | 135 | 140 | +$371k | - | out (clean 32, ADX 24, RVol 0.5) |
| 25 | **BABA** | 99.46 | - | **-** | 6 | - | NEG -$18.1M | 101.59 | 100 | 100 | -$19k | - | out (clean 29, ADX 22, RVol 0.7) |
| 26 | **HOOD** | 91.68 | - | **-** | 5 | - | NEG -$21.1M | - | 95 | 90 | -$596k | - | out (clean 28, ADX 15, RVol 0.4) |
| 27 | **PLTR** | 194.03 | - | **-** | 3 | - | POS +$21.7M | 191.93 | 200 | 190 | -$386k | - | out (clean 25, ADX 12, RVol 0.3) |

## Big prints this scan (60)
- **MU** CALL 900 2026-11-02 (4DTE): 500 @ 49.28 = **+$2.5M** MID | vol 1,077 / OI 169
- **MU** CALL 900 2026-10-30 (1DTE): 500 @ 46.08 = **+$2.3M** BUY | vol 1,208 / OI 2,922
- **GOOGL** PUT 285 2026-11-02 (4DTE): 500 @ 4.50 = **+$225k** BUY | vol 5,930 / OI 80
- **MU** PUT 955 2026-11-02 (4DTE): 84 @ 25.07 = **+$211k** SELL | vol 489 / OI 29
- **MU** PUT 950 2026-11-02 (4DTE): 84 @ 22.27 = **+$187k** SELL | vol 1,025 / OI 521
- **GOOGL** CALL 290 2026-10-30 (1DTE): 1,000 @ 1.50 = **+$150k** SELL | vol 43,564 / OI 113
- **AMZN** CALL 240 2026-10-30 (1DTE): 100 @ 13.35 = **+$134k** SELL | vol 2,779 / OI 742
- **SPY** CALL 770 2026-10-29 (0DTE): 1,000 @ 1.07 = **+$107k** BUY | vol 379,555 / OI 1,967
- **IWM** PUT 287 2026-10-29 (0DTE): 380 @ 2.45 = **+$93k** SELL | vol 5,126 / OI 0
- **META** CALL 620 2026-10-30 (1DTE): 69 @ 12.75 = **+$88k** SELL | vol 7,797 / OI 771
- **TSLA** CALL 405 2026-10-30 (1DTE): 200 @ 4.20 = **+$84k** BUY | vol 46,304 / OI 4,208
- **MU** CALL 925 2026-10-30 (1DTE): 30 @ 26.65 = **+$80k** BUY | vol 110 / OI 851
- **GOOGL** PUT 280 2026-11-02 (4DTE): 332 @ 2.30 = **+$76k** BUY | vol 6,044 / OI 63
- **MU** CALL 955 2026-10-30 (1DTE): 80 @ 9.10 = **+$73k** BUY | vol 10,973 / OI 878
- **GOOGL** PUT 280 2026-11-02 (4DTE): 287 @ 2.40 = **+$69k** BUY | vol 6,044 / OI 63

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 795 2026-11-02 (4DTE): 538 traded vs OI 446
- **SPY** CALL 790 2026-11-10 (12DTE): 740 traded vs OI 706
- **IWM** PUT 280 2026-11-05 (7DTE): 534 traded vs OI 5
- **IWM** PUT 282 2026-11-05 (7DTE): 518 traded vs OI 0
- **IWM** CALL 285 2026-10-30 (1DTE): 15,287 traded vs OI 15,275
- **NVDA** PUT 220 2026-11-04 (6DTE): 553 traded vs OI 263
- **AMD** CALL 582.5 2026-10-30 (1DTE): 501 traded vs OI 464
- **META** CALL 630 2026-11-04 (6DTE): 503 traded vs OI 300
- **GOOGL** PUT 275 2026-11-04 (6DTE): 501 traded vs OI 15
- **COIN** CALL 165 2026-10-30 (1DTE): 501 traded vs OI 426
- **MU** PUT 880 2026-10-30 (1DTE): 2,484 traded vs OI 2,474
- **MU** PUT 940 2026-11-02 (4DTE): 538 traded vs OI 108
- **MU** PUT 870 2026-11-02 (4DTE): 578 traded vs OI 201

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
