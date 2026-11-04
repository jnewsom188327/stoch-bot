# GEX + FLOW SCAN - Wed Nov 04, 11:20 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (6)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:20 | **SMCI** | **CALLS** | FLOW SURGE | 11/06 33C | 0.65 | 0.17 | -3% (1m) | **-74%** | +39% | 32.81 |
| 10:20 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/04 284C | 0.49 | 0.21 | +2% (22m) | **-57%** | +131% | 284.74 |
| 10:00 | **AMZN** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/04 267.5P | 0.68 | 1.54 | +169% (60m) | **+126%** (done) | +258% | 265.7 |
| 09:50 | **UBER** | **CALLS** | FLIP CROSS up into positive gamma | 11/06 71C | 0.60 | 1.56 | +168% (52m) | **+160%** (done) | +50% | 70 hit |
| 09:50 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/04 286C | 0.53 | 0.06 | +2% (1m) | **-89%** (done) | +150% | 287 |
| 09:45 | **UBER** | **PUTS** | FLIP CROSS down into negative gamma | 11/06 67P | 0.63 | 0.10 | -3% (1m) | **-84%** (done) | +27% | 68.03 |

## 1m RULES on SPY / QQQ - loose (0 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 11:20:08 ET, last candle SPY 11:19, QQQ 11:19 | no errors

## Flow surges NOT fired - price disagreed (30 today, last 5)
- 11:20 SMCI CALLS: under EMA 20 - flow says one way, price says the other
- 11:15 SMCI CALLS: price -0.11 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:50 SMCI CALLS: price -1.23 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:50 AAPL PUTS: over EMA 20 - flow says one way, price says the other
- 10:45 AAPL PUTS: price +0.02 over the last 15 min / over EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **SMCI** | 30.19 | FLOW SURGE | **CALLS** | 64 | 11/06 31.5C @ 0.46 (delta 0.30) = est +66% at 31.13 | NEG -$739k | - | 33 | 30 | +$1.7M | +$64k bull / +$0 bear | SHORT (clean 33, ADX 44, RVol 3.6) |
| 2 | **AMZN** | 266.76 | TREND (flow not with it) | **CALLS** | 48 | none: 84 calls 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (37 contracts' greeks worked out here) | POS +$533.0M | - | 270 | 250 | -$18.5M | +$917k bull / +$0 bear | LONG (clean 35, ADX 49, RVol 1.5) |
| 3 | **SHOP** | 151.86 | FLOW SURGE | **PUTS** | 37 | none: 20 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$5.5M | - | 160 | 150 | -$380k | +$0 bull / -$29k bear | out (clean 35, ADX 31, RVol 0.4) |
| 4 | **AAPL** | 352.10 | - | **-** | 34 | - | POS +$892.7M | 342.71 | 350 | 350 | -$79.2M | +$1.0M bull / -$107k bear | out (clean 32, ADX 59, RVol 1.8) |
| 5 | **SMH** | 505.62 | - | **-** | 32 | - | NEG -$531.8M | - | 532.5 | 500 | +$5.0M | +$248k bull / -$33k bear | out (clean 32, ADX 38, RVol 3.2) |
| 6 | **GOOGL** | 291.70 | - | **-** | 30 | - | POS +$95.6M | 283.04 | 290 | 290 | -$26.7M | +$183k bull / -$34k bear | out (clean 35, ADX 48, RVol 0.7) |
| 7 | **MU** | 807.54 | - | **-** | 30 | - | NEG -$361.6M | - | 850 | 800 | +$110.9M | +$6.4M bull / -$6.4M bear | out (clean 31, ADX 36, RVol 2.0) |
| 8 | **DELL** | 370.50 | - | **-** | 27 | - | NEG -$28.0M | - | 400 | 400 | +$2.0M | +$255k bull / +$0 bear | out (clean 33, ADX 40, RVol 4.3) |
| 9 | **UBER** | 72.23 | - | **-** | 27 | - | POS +$15.7M | - | 75 | 70 | -$1.5M | - | out (clean 31, ADX 67, RVol 2.6) |
| 10 | **MSFT** | 553.38 | - | **-** | 26 | - | POS +$989.8M | - | 550 | 535 | -$14.9M | +$514k bull / -$895k bear | out (clean 29, ADX 66, RVol 1.5) |
| 11 | **AVGO** | 326.42 | - | **-** | 25 | - | NEG -$98.2M | - | 340 | 320 | +$3.7M | +$514k bull / -$284k bear | out (clean 30, ADX 36, RVol 1.7) |
| 12 | **TSLA** | 384.66 | - | **-** | 24 | - | NEG -$138.7M | 395.83 | 400 | 380 | -$65.6M | +$3.1M bull / +$0 bear | out (clean 30, ADX 22, RVol 1.7) |
| 13 | **IWM** | 282.61 | - | **-** | 23 | - | NEG -$639.3M | 284.55 | 285 | 270 | +$14.1M | +$0 bull / -$159k bear | out (clean 34, ADX 18, RVol 1.3) |
| 14 | **ARM** | 195.31 | - | **-** | 23 | - | NEG -$6.9M | - | 212.5 | 200 | +$810k | - | out (clean 26, ADX 37, RVol 0.8) |
| 15 | **SPY** | 766.01 | - | **-** | 22 | - | NEG -$4.1B | 770.13 | 770 | 750 | -$76.8M | +$2.9M bull / -$1.8M bear | out (clean 32, ADX 35, RVol 1.3) |
| 16 | **NVDA** | 203.05 | - | **-** | 22 | - | NEG -$55.6M | 203.99 | 210 | 200 | +$2.1M | +$293k bull / -$487k bear | out (clean 30, ADX 38, RVol 2.1) |
| 17 | **AMD** | 486.76 | - | **-** | 22 | - | NEG -$89.1M | - | 500 | 500 | +$38.2M | +$1.0M bull / -$2.2M bear | out (clean 32, ADX 21, RVol 1.4) |
| 18 | **COIN** | 151.91 | - | **-** | 22 | - | POS +$28.4M | - | 148 | 150 | -$1.2M | +$0 bull / -$28k bear | out (clean 30, ADX 15, RVol 0.6) |
| 19 | **META** | 630.35 | - | **-** | 21 | - | POS +$149.2M | 619.63 | 650 | 625 | +$7.9M | +$720k bull / +$0 bear | out (clean 30, ADX 35, RVol 0.9) |
| 20 | **MSTR** | 144.52 | - | **-** | 21 | - | POS +$120.2M | - | 135 | 150 | +$314k | +$38k bull / -$366k bear | out (clean 31, ADX 45, RVol 1.1) |
| 21 | **BABA** | 106.91 | - | **-** | 21 | - | POS +$16.2M | - | 110 | 110 | -$849k | - | out (clean 36, ADX 63, RVol 2.7) |
| 22 | **NFLX** | 66.15 | - | **-** | 19 | - | POS +$19.8M | 62.24 | 65 | 65 | -$2.2M | - | out (clean 31, ADX 69, RVol 1.1) |
| 23 | **QQQ** | 693.33 | - | **-** | 18 | - | NEG -$5.0B | 721.43 | 700 | 680 | -$66.1M | +$3.7M bull / -$6.0M bear | out (clean 31, ADX 24, RVol 1.0) |
| 24 | **ORCL** | 125.43 | - | **-** | 18 | - | NEG -$33.6M | - | 130 | 125 | +$283k | +$88k bull / -$26k bear | out (clean 35, ADX 15, RVol 2.5) |
| 25 | **HOOD** | 87.14 | - | **-** | 17 | - | POS +$2.4M | 84.78 | 90 | 90 | -$1.1M | +$0 bull / -$125k bear | out (clean 28, ADX 15, RVol 0.8) |
| 26 | **PLTR** | 173.57 | - | **-** | 16 | - | NEG -$45.5M | - | 180 | 170 | -$1.3M | +$279k bull / -$595k bear | out (clean 26, ADX 15, RVol 1.0) |
| 27 | **CRM** | 228.48 | - | **-** | 16 | - | NEG -$9.0M | 238.23 | 240 | 220 | -$223k | - | out (clean 31, ADX 46, RVol 0.8) |

## Big prints this scan (118)
- **QQQ** PUT 698 2026-11-04 (0DTE): 1,667 @ 4.85 = **+$808k** SELL | vol 50,806 / OI 420
- **SPY** PUT 770 2026-11-05 (1DTE): 891 @ 4.82 = **+$429k** SELL | vol 4,975 / OI 1,690
- **TSLA** PUT 385 2026-11-09 (5DTE): 488 @ 7.50 = **+$366k** SELL | vol 3,503 / OI 308
- **MU** PUT 830 2026-11-04 (0DTE): 106 @ 27.50 = **+$292k** BUY | vol 7,944 / OI 840
- **MU** PUT 830 2026-11-04 (0DTE): 106 @ 27.50 = **+$292k** BUY | vol 7,944 / OI 840
- **QQQ** PUT 696 2026-11-05 (1DTE): 487 @ 5.65 = **+$275k** SELL | vol 6,696 / OI 0
- **SPY** CALL 767 2026-11-09 (5DTE): 558 @ 4.76 = **+$266k** BUY | vol 3,719 / OI 0
- **QQQ** CALL 694 2026-11-04 (0DTE): 1,303 @ 1.80 = **+$235k** SELL | vol 49,541 / OI 2,952
- **SPY** PUT 768 2026-11-05 (1DTE): 500 @ 4.25 = **+$212k** BUY | vol 23,136 / OI 0
- **MU** PUT 820 2026-11-04 (0DTE): 100 @ 20.08 = **+$201k** BUY | vol 14,132 / OI 1,070
- **SPY** PUT 768 2026-11-05 (1DTE): 470 @ 4.25 = **+$200k** BUY | vol 23,136 / OI 0
- **PLTR** CALL 167.5 2026-11-06 (2DTE): 199 @ 8.10 = **+$161k** BUY | vol 1,124 / OI 103
- **QQQ** PUT 695 2026-11-05 (1DTE): 255 @ 6.14 = **+$157k** BUY | vol 9,949 / OI 1,805
- **SPY** CALL 767 2026-11-04 (0DTE): 997 @ 1.51 = **+$151k** BUY | vol 181,523 / OI 2,706
- **MU** PUT 785 2026-11-04 (0DTE): 600 @ 2.50 = **+$150k** BUY | vol 8,887 / OI 365

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 732 2026-11-04 (0DTE): 1,813 traded vs OI 1,524
- **SPY** PUT 765 2026-11-06 (2DTE): 6,935 traded vs OI 6,567
- **SPY** CALL 765 2026-11-06 (2DTE): 6,136 traded vs OI 6,014
- **SPY** PUT 765 2026-11-10 (6DTE): 829 traded vs OI 804
- **SPY** PUT 766 2026-11-11 (7DTE): 569 traded vs OI 0
- **SPY** CALL 810 2026-11-10 (6DTE): 642 traded vs OI 249
- **SPY** PUT 767 2026-11-11 (7DTE): 612 traded vs OI 0
- **SPY** PUT 755 2026-11-11 (7DTE): 808 traded vs OI 801
- **SPY** CALL 768 2026-11-13 (9DTE): 1,397 traded vs OI 1,379
- **QQQ** CALL 707 2026-11-06 (2DTE): 845 traded vs OI 841
- **QQQ** CALL 700 2026-11-10 (6DTE): 880 traded vs OI 861
- **QQQ** PUT 685 2026-11-11 (7DTE): 558 traded vs OI 353
- **QQQ** PUT 660 2026-11-27 (23DTE): 1,108 traded vs OI 1,095
- **QQQ** CALL 700 2026-12-04 (30DTE): 597 traded vs OI 585
- **IWM** PUT 281 2026-11-11 (7DTE): 501 traded vs OI 374

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
