# GEX + FLOW SCAN - Wed Nov 04, 01:40 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (10)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 13:05 | **AAPL** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/04 352.5P | 0.58 | 0.79 | +76% (29m) | **+36%** | +57% | 352.38 hit |
| 12:50 | **AMZN** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/04 267.5P | 0.40 | 0.46 | +17% (7m) | **+15%** | +109% | 267.48 |
| 11:38 | **QQQ** | **PUTS** | 1m FAILED POP (R3) | 11/04 686P | 0.80 | 0.15 | -1% (0m) | **-81%** (done) | +26% | 689.6 |
| 11:21 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/04 685P | 0.67 | 0.12 | +66% (7m) | **-82%** (done) | +25% | 690.3 hit |
| 10:20 | **SMCI** | **CALLS** | FLOW SURGE | 11/06 33C | 0.65 | 0.13 | -3% (1m) | **-80%** (done) | +39% | 32.81 |
| 10:20 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/04 284C | 0.49 | 0.17 | +2% (22m) | **-65%** (done) | +131% | 284.74 |
| 10:00 | **AMZN** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/04 267.5P | 0.68 | 1.54 | +169% (60m) | **+126%** (done) | +258% | 265.7 |
| 09:50 | **UBER** | **CALLS** | FLIP CROSS up into positive gamma | 11/06 71C | 0.60 | 1.56 | +168% (52m) | **+160%** (done) | +50% | 70 hit |
| 09:50 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/04 286C | 0.53 | 0.06 | +2% (1m) | **-89%** (done) | +150% | 287 |
| 09:45 | **UBER** | **PUTS** | FLIP CROSS down into negative gamma | 11/06 67P | 0.63 | 0.10 | -3% (1m) | **-84%** (done) | +27% | 68.03 |

## 1m RULES on SPY / QQQ - loose (2 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 13:40:08 ET, last candle SPY 13:39, QQQ 13:39 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 11:37 | QQQ | 1m FAILED POP | R3 | PUTS | TURNING away | **FIRE** QQQ261104P00686000 |
| 11:20 | QQQ | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | **FIRE** QQQ261104P00685000 |

## Flow surges NOT fired - price disagreed (36 today, last 5)
- 11:50 SMCI CALLS: under EMA 20 - flow says one way, price says the other
- 11:45 SMCI CALLS: under EMA 20 - flow says one way, price says the other
- 11:40 SMCI CALLS: under EMA 20 - flow says one way, price says the other
- 11:35 SMCI CALLS: price -0.19 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 11:30 SMCI CALLS: price -0.20 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **SMH** | 505.17 | FLOW SURGE | **CALLS** | 33 | none: 160 calls 0-7DTE > 8 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (67 contracts' greeks worked out here) | NEG -$547.6M | - | 532.5 | 500 | +$21.6M | +$25k bull / +$0 bear | out (clean 32, ADX 14, RVol 0.2) |
| 2 | **AAPL** | 352.76 | - | **-** | 27 | - | POS +$1.0B | 343.05 | 355 | 350 | -$77.5M | +$214k bull / +$0 bear | out (clean 32, ADX 31, RVol 0.8) |
| 3 | **MSTR** | 145.40 | - | **-** | 23 | - | POS +$122.3M | - | 135 | 150 | -$10.4M | +$3.8M bull / -$418k bear | out (clean 31, ADX 34, RVol 0.2) |
| 4 | **AMZN** | 268.56 | - | **-** | 22 | - | POS +$567.3M | - | 270 | 250 | -$19.9M | +$720k bull / +$0 bear | out (clean 36, ADX 34, RVol 0.8) |
| 5 | **MSFT** | 555.86 | - | **-** | 21 | - | POS +$1.0B | - | 550 | 535 | -$16.8M | +$26k bull / -$117k bear | out (clean 29, ADX 30, RVol 0.9) |
| 6 | **ARM** | 192.63 | - | **-** | 21 | - | NEG -$7.1M | - | 200 | 200 | +$839k | +$0 bull / -$26k bear | out (clean 26, ADX 25, RVol 0.7) |
| 7 | **MU** | 807.46 | - | **-** | 20 | - | NEG -$375.4M | - | 850 | 800 | +$100.7M | +$441k bull / -$1.9M bear | out (clean 31, ADX 17, RVol 0.4) |
| 8 | **ORCL** | 125.50 | - | **-** | 20 | - | NEG -$32.5M | - | 130 | 125 | +$3.0M | +$142k bull / +$0 bear | out (clean 34, ADX 13, RVol 1.3) |
| 9 | **TSLA** | 389.07 | - | **-** | 19 | - | NEG -$104.6M | 395.96 | 400 | 390 | -$81.5M | +$987k bull / -$463k bear | out (clean 31, ADX 17, RVol 0.4) |
| 10 | **AMD** | 483.14 | - | **-** | 19 | - | NEG -$93.8M | - | 500 | 440 | +$47.6M | +$445k bull / -$186k bear | out (clean 32, ADX 12, RVol 0.5) |
| 11 | **META** | 632.86 | - | **-** | 18 | - | POS +$164.3M | 621.79 | 650 | 625 | +$5.6M | +$486k bull / +$0 bear | out (clean 31, ADX 22, RVol 1.2) |
| 12 | **SMCI** | 29.91 | - | **-** | 18 | - | NEG -$939k | - | 32 | 30 | +$2.0M | - | out (clean 34, ADX 24, RVol 0.8) |
| 13 | **SPY** | 767.83 | - | **-** | 17 | - | NEG -$2.9B | 769.8 | 770 | 767 | -$99.3M | +$3.8M bull / +$0 bear | out (clean 32, ADX 22, RVol 0.4) |
| 14 | **QQQ** | 694.26 | - | **-** | 15 | - | NEG -$4.8B | 718.96 | 700 | 680 | -$121.7M | +$758k bull / +$0 bear | out (clean 32, ADX 10, RVol 0.5) |
| 15 | **PLTR** | 170.98 | - | **-** | 15 | - | NEG -$51.5M | - | 165 | 170 | -$1.4M | +$60k bull / +$0 bear | out (clean 26, ADX 16, RVol 0.7) |
| 16 | **NVDA** | 203.75 | - | **-** | 14 | - | NEG -$17.4M | 204.02 | 210 | 200 | +$1.2M | +$320k bull / -$130k bear | out (clean 30, ADX 14, RVol 0.8) |
| 17 | **GOOGL** | 291.11 | - | **-** | 13 | - | POS +$102.6M | 282.96 | 290 | 290 | -$26.7M | - | out (clean 36, ADX 17, RVol 0.3) |
| 18 | **UBER** | 71.55 | - | **-** | 13 | - | POS +$13.1M | 68.22 | 70 | 70 | -$1.2M | - | out (clean 30, ADX 22, RVol 0.7) |
| 19 | **NFLX** | 65.89 | - | **-** | 12 | - | POS +$20.7M | 62.38 | 65 | 65 | -$1.9M | - | out (clean 31, ADX 23, RVol 0.7) |
| 20 | **BABA** | 106.97 | - | **-** | 12 | - | POS +$16.5M | - | 110 | 110 | -$814k | - | out (clean 36, ADX 25, RVol 0.5) |
| 21 | **COIN** | 152.29 | - | **-** | 11 | - | POS +$28.9M | - | 148 | 150 | -$1.2M | - | out (clean 31, ADX 20, RVol 0.2) |
| 22 | **SHOP** | 151.40 | - | **-** | 10 | - | NEG -$5.8M | - | 160 | 150 | -$348k | - | out (clean 33, ADX 15, RVol 0.3) |
| 23 | **CRM** | 225.27 | - | **-** | 7 | - | NEG -$13.3M | - | 240 | 220 | -$114k | - | out (clean 34, ADX 24, RVol 0.4) |
| 24 | **IWM** | 283.83 | - | **-** | 6 | - | NEG -$216.8M | 284.34 | 285 | 270 | +$9.9M | - | out (clean 35, ADX 12, RVol 0.5) |
| 25 | **AVGO** | 327.19 | - | **-** | 6 | - | NEG -$95.2M | - | 340 | 330 | +$2.9M | - | out (clean 30, ADX 13, RVol 0.5) |
| 26 | **DELL** | 373.17 | - | **-** | 6 | - | NEG -$30.5M | - | 400 | 400 | +$1.5M | - | out (clean 32, ADX 13, RVol 0.5) |
| 27 | **HOOD** | 88.08 | - | **-** | 6 | - | POS +$3.1M | 84.62 | 90 | 90 | -$860k | - | out (clean 28, ADX 22, RVol 0.5) |

## Big prints this scan (42)
- **AMD** CALL 475 2026-11-06 (2DTE): 200 @ 18.50 = **+$370k** MID | vol 1,382 / OI 264
- **AMZN** PUT 270 2026-11-04 (0DTE): 2,239 @ 1.15 = **+$257k** SELL | vol 22,704 / OI 0
- **TSLA** PUT 400 2026-11-04 (0DTE): 120 @ 11.50 = **+$138k** BUY | vol 1,691 / OI 3,748
- **MU** PUT 830 2026-11-04 (0DTE): 50 @ 23.20 = **+$116k** MID | vol 8,145 / OI 840
- **QQQ** PUT 706 2026-11-05 (1DTE): 100 @ 11.49 = **+$115k** SELL | vol 395 / OI 0
- **TSLA** PUT 400 2026-11-04 (0DTE): 102 @ 11.00 = **+$112k** SELL | vol 1,691 / OI 3,748
- **QQQ** PUT 697 2026-11-04 (0DTE): 364 @ 2.85 = **+$104k** SELL | vol 94,591 / OI 457
- **TSLA** PUT 390 2026-11-06 (2DTE): 132 @ 7.20 = **+$95k** BUY | vol 8,430 / OI 4,169
- **AMZN** CALL 265 2026-11-09 (5DTE): 132 @ 6.76 = **+$89k** BUY | vol 618 / OI 473
- **AMD** CALL 475 2026-11-06 (2DTE): 48 @ 18.50 = **+$89k** MID | vol 1,382 / OI 264
- **MU** PUT 820 2026-11-04 (0DTE): 50 @ 13.90 = **+$70k** BUY | vol 15,022 / OI 1,070
- **AMD** PUT 475 2026-11-06 (2DTE): 50 @ 10.40 = **+$52k** BUY | vol 3,864 / OI 892
- **TSLA** PUT 387.5 2026-11-04 (0DTE): 400 @ 1.20 = **+$48k** BUY | vol 57,473 / OI 703
- **MU** PUT 800 2026-11-06 (2DTE): 28 @ 16.41 = **+$46k** MID | vol 9,455 / OI 3,802
- **MU** PUT 800 2026-11-06 (2DTE): 28 @ 16.41 = **+$46k** MID | vol 9,455 / OI 3,802

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 774 2026-11-09 (5DTE): 502 traded vs OI 0
- **SPY** CALL 781 2026-11-16 (12DTE): 672 traded vs OI 0
- **SPY** PUT 755 2026-11-16 (12DTE): 902 traded vs OI 718
- **QQQ** PUT 690 2026-11-11 (7DTE): 512 traded vs OI 338
- **QQQ** CALL 720 2026-11-11 (7DTE): 621 traded vs OI 617
- **QQQ** PUT 665 2026-11-18 (14DTE): 2,130 traded vs OI 0
- **QQQ** PUT 691 2026-11-20 (16DTE): 3,529 traded vs OI 1,019
- **NVDA** CALL 217.5 2026-11-11 (7DTE): 500 traded vs OI 275
- **TSLA** PUT 370 2026-11-11 (7DTE): 500 traded vs OI 98
- **TSLA** CALL 375 2026-11-06 (2DTE): 1,795 traded vs OI 1,792
- **AAPL** PUT 345 2026-11-13 (9DTE): 2,821 traded vs OI 2,386
- **AAPL** PUT 345 2026-12-04 (30DTE): 514 traded vs OI 273
- **AMD** CALL 485 2026-11-09 (5DTE): 509 traded vs OI 24
- **META** CALL 635 2026-11-06 (2DTE): 2,376 traded vs OI 2,274
- **META** PUT 627.5 2026-11-06 (2DTE): 512 traded vs OI 332

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
