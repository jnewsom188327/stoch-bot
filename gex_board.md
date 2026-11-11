# GEX + FLOW SCAN - Wed Nov 11, 03:45 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (12)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:40 | **MSFT** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/11 522.5C | 0.73 | 1.07 | +73% (34m) | **+47%** (done) | +146% | 523.2 |
| 11:05 | **MSFT** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/11 525C | 0.64 | 0.36 | +2% (1m) | **-44%** (done) | +363% | 527.5 |
| 10:45 | **AVGO** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/11 345P | 0.78 | 0.10 | +6% (1m) | **-87%** (done) | +149% | 345 |
| 10:35 | **MSFT** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/11 525C | 0.76 | 0.25 | +96% (9m) | **-67%** (done) | +343% | 527.5 |
| 10:20 | **AVGO** | **CALLS** | TREND + FLOW | 11/11 355C | 0.71 | 0.76 | +127% (38m) | **+7%** (done) | +280% | 356.78 |
| 10:15 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/11 282C | 0.65 | 1.05 | +72% (56m) | **+62%** (done) | +66% | 282.84 hit |
| 10:05 | **NVDA** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/11 175C | 0.76 | 1.54 | +142% (51m) | **+103%** (done) | +58% | 175 hit |
| 09:50 | **GOOGL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/11 292.5C | 0.51 | 0.62 | +39% (28m) | **+22%** (done) | +82% | 291.86 |
| 09:45 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/11 282C | 0.68 | 0.64 | +85% (6m) | **-6%** (done) | +68% | 282.96 |
| 09:45 | **QQQ** | **CALLS** | FLOW SURGE | 11/11 690C | 0.63 | 1.23 | +103% (59m) | **+95%** (done) | +171% | 689.78 |
| 09:39 | **QQQ** | **CALLS** | 1m WHIPSAW (R1 R5) | 11/11 693C | 0.52 | 0.29 | -10% (0m) | **-44%** (done) | +92% | 690.43 |
| 09:39 | **SPY** | **CALLS** | 1m WHIPSAW (R1 R5) | 11/11 760C | 0.53 | 0.17 | -2% (0m) | **-68%** (done) | +79% | 758.82 |

## 1m RULES on SPY / QQQ - loose (3 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 15:32:08 ET, last candle SPY 15:31, QQQ 15:31 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 10:02 | QQQ | 1m AGREE FLIP | FULL | CALLS | up | logged (agree flip) |
| 09:38 | QQQ | 1m WHIPSAW | R1 R5 | CALLS | TURNING away | **FIRE** QQQ261111C00693000 |
| 09:38 | SPY | 1m WHIPSAW | R1 R5 | CALLS | TURNING away | **FIRE** SPY261111C00760000 |

## Flow surges NOT fired - price disagreed (7 today, last 5)
- 10:15 BABA CALLS: under EMA 20 - flow says one way, price says the other
- 10:00 MSFT CALLS: price -4.55 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:00 AMZN CALLS: price -0.73 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 09:55 AAPL PUTS: price +1.32 over the last 15 min / over EMA 20 - flow says one way, price says the other
- 09:50 MSFT CALLS: price -2.01 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **META** | 633.50 | PINNED between the walls (positive gamma) - chop | **-** | 34 | - | POS +$128.1M | 630.58 | 635 | 635 | +$7.6M | +$1.2M bull / +$0 bear | out (clean 30, ADX 44, RVol 0.4) |
| 2 | **MSFT** | 519.56 | FLIP CROSS up into positive gamma | **CALLS** | 34 | none: 162 calls 0-7DTE > 9 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only -94% at the target (needs +20%) (63 contracts' greeks worked out here) | NEG -$25.5M | 519.06 | 535 | 520 | +$14.8M | +$0 bull / -$33k bear | out (clean 32, ADX 21, RVol 0.7) |
| 3 | **HOOD** | 85.16 | PINNED between the walls (positive gamma) - chop | **-** | 30 | - | POS +$17.8M | - | 85 | 85 | -$604k | +$0 bull / -$59k bear | out (clean 35, ADX 15, RVol 0.6) |
| 4 | **TSLA** | 390.44 | PINNED between the walls (positive gamma) - chop | **-** | 29 | - | POS +$452.0M | - | 390 | 390 | +$314k | +$545k bull / +$0 bear | out (clean 32, ADX 28, RVol 0.5) |
| 5 | **AAPL** | 355.30 | PINNED between the walls (positive gamma) - chop | **-** | 29 | - | POS +$3.9B | 341.85 | 355 | 355 | -$1.8M | +$0 bull / -$73k bear | out (clean 28, ADX 24, RVol 0.6) |
| 6 | **IWM** | 282.99 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 26 | none: 340 puts 0-7DTE > 16 priced 0.40-0.80 > 5 delta 0.2+ > 5 spread ok > 5 liquid > best one only +11% at the target (needs +20%) (172 contracts' greeks worked out here) | POS +$243.5M | 282.64 | 283 | 270 | -$5.0M | - | out (clean 35, ADX 21, RVol 0.5) |
| 7 | **AVGO** | 346.93 | - | **-** | 24 | - | POS +$101.8M | - | 350 | 340 | +$10.1M | +$218k bull / +$0 bear | out (clean 37, ADX 43, RVol 0.8) |
| 8 | **AMD** | 555.85 | - | **-** | 22 | - | POS +$198.8M | - | 550 | 550 | -$91.4M | +$112k bull / -$244k bear | out (clean 36, ADX 28, RVol 0.5) |
| 9 | **MU** | 812.78 | - | **-** | 21 | - | POS +$168.2M | - | 800 | 850 | -$188.3M | +$2.5M bull / -$1.4M bear | out (clean 33, ADX 22, RVol 0.7) |
| 10 | **QQQ** | 690.91 | - | **-** | 20 | - | POS +$534.7M | 689.27 | 700 | 680 | -$121.8M | +$1.3M bull / +$0 bear | out (clean 33, ADX 33, RVol 0.5) |
| 11 | **NVDA** | 174.73 | - | **-** | 19 | - | NEG -$100.8M | 179.77 | 175 | 190 | -$20.4M | +$855k bull / -$836k bear | out (clean 34, ADX 34, RVol 0.5) |
| 12 | **SPY** | 760.01 | - | **-** | 18 | - | NEG -$917.4M | 761.02 | 760 | 760 | -$123.1M | +$130k bull / -$1.7M bear | out (clean 34, ADX 25, RVol 0.5) |
| 13 | **SMH** | 507.92 | - | **-** | 18 | - | NEG -$32.1M | 512.49 | 500 | 500 | -$1.0M | +$147k bull / +$0 bear | out (clean 32, ADX 36, RVol 0.5) |
| 14 | **SHOP** | 149.46 | - | **-** | 18 | - | POS +$4.2M | 145.32 | 150 | 140 | -$479k | - | out (clean 32, ADX 13, RVol 0.6) |
| 15 | **PLTR** | 172.96 | - | **-** | 17 | - | POS +$75.9M | - | 170 | 180 | +$1.4M | +$0 bull / -$35k bear | out (clean 29, ADX 15, RVol 0.3) |
| 16 | **AMZN** | 266.23 | - | **-** | 16 | - | POS +$434.4M | - | 270 | 265 | +$4.6M | +$0 bull / -$37k bear | out (clean 31, ADX 13, RVol 0.5) |
| 17 | **SMCI** | 30.35 | - | **-** | 13 | - | POS +$15.9M | - | 30 | 30 | -$548k | - | out (clean 34, ADX 38, RVol 0.5) |
| 18 | **ARM** | 203.81 | - | **-** | 13 | - | POS +$7.0M | - | 200 | 200 | -$1.7M | - | out (clean 32, ADX 20, RVol 0.7) |
| 19 | **BABA** | 101.62 | - | **-** | 13 | - | NEG -$17.0M | 106.5 | 110 | 101 | +$360k | - | out (clean 28, ADX 16, RVol 0.4) |
| 20 | **DELL** | 375.81 | - | **-** | 11 | - | NEG -$1.1M | - | 400 | 400 | -$2.2M | - | out (clean 38, ADX 32, RVol 0.6) |
| 21 | **NFLX** | 64.31 | - | **-** | 10 | - | NEG -$431k | 64.32 | 65 | 65 | -$270k | - | out (clean 26, ADX 29, RVol 0.8) |
| 22 | **MSTR** | 120.84 | - | **-** | 10 | - | NEG -$22.4M | - | 132 | 120 | +$2.1M | - | out (clean 28, ADX 25, RVol 1.0) |
| 23 | **UBER** | 70.93 | - | **-** | 8 | - | POS +$21.4M | 68.31 | 70 | 70 | -$22k | - | out (clean 31, ADX 23, RVol 1.5) |
| 24 | **CRM** | 217.56 | - | **-** | 8 | - | NEG -$11.5M | - | 230 | 220 | -$58k | - | out (clean 29, ADX 13, RVol 0.8) |
| 25 | **COIN** | 136.45 | - | **-** | 7 | - | POS +$23.7M | 128.5 | 141 | 135 | +$82k | - | out (clean 30, ADX 30, RVol 0.7) |
| 26 | **GOOGL** | 293.98 | - | **-** | 5 | - | POS +$112.0M | 289.57 | 300 | 290 | -$794k | - | out (clean 29, ADX 18, RVol 0.5) |
| 27 | **ORCL** | 128.81 | - | **-** | 5 | - | POS +$12.9M | - | 130 | 125 | +$486k | - | out (clean 30, ADX 15, RVol 0.7) |

## Big prints this scan (55)
- **SPY** CALL 760 2026-11-13 (2DTE): 846 @ 3.31 = **+$280k** SELL | vol 27,300 / OI 13,281
- **QQQ** CALL 691 2026-11-12 (1DTE): 699 @ 3.91 = **+$273k** BUY | vol 15,453 / OI 310
- **SPY** PUT 760 2026-11-13 (2DTE): 846 @ 2.94 = **+$249k** BUY | vol 38,872 / OI 6,054
- **SPY** PUT 763 2026-11-11 (0DTE): 716 @ 2.88 = **+$206k** BUY | vol 83,899 / OI 2,103
- **SPY** CALL 758 2026-11-11 (0DTE): 900 @ 2.24 = **+$202k** SELL | vol 338,559 / OI 1,040
- **SPY** CALL 758 2026-11-11 (0DTE): 900 @ 2.22 = **+$200k** SELL | vol 338,559 / OI 1,040
- **SPY** CALL 758 2026-11-11 (0DTE): 873 @ 2.20 = **+$192k** SELL | vol 338,559 / OI 1,040
- **MU** PUT 820 2026-11-13 (2DTE): 77 @ 22.00 = **+$169k** SELL | vol 9,795 / OI 597
- **SMH** CALL 500 2026-11-13 (2DTE): 113 @ 13.20 = **+$149k** MID | vol 3,033 / OI 4,456
- **SPY** CALL 758 2026-11-11 (0DTE): 589 @ 2.14 = **+$126k** SELL | vol 338,559 / OI 1,040
- **QQQ** PUT 693 2026-11-13 (2DTE): 200 @ 5.74 = **+$115k** SELL | vol 4,331 / OI 719
- **SPY** CALL 758 2026-11-11 (0DTE): 500 @ 2.21 = **+$110k** SELL | vol 338,559 / OI 1,040
- **SPY** CALL 758 2026-11-11 (0DTE): 496 @ 2.17 = **+$108k** SELL | vol 338,559 / OI 1,040
- **MU** PUT 815 2026-11-13 (2DTE): 50 @ 20.80 = **+$104k** BUY | vol 5,662 / OI 225
- **MU** PUT 820 2026-11-13 (2DTE): 42 @ 23.25 = **+$98k** BUY | vol 9,795 / OI 597

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 752 2026-12-11 (30DTE): 535 traded vs OI 530
- **QQQ** CALL 710 2026-11-18 (7DTE): 710 traded vs OI 110
- **QQQ** PUT 655 2026-11-27 (16DTE): 1,666 traded vs OI 1,088
- **IWM** PUT 273 2026-11-20 (9DTE): 10,306 traded vs OI 6,339
- **NVDA** CALL 165 2026-11-20 (9DTE): 1,872 traded vs OI 1,826
- **NVDA** CALL 177.5 2026-11-18 (7DTE): 1,574 traded vs OI 1,568
- **AAPL** PUT 355 2026-11-27 (16DTE): 570 traded vs OI 534
- **GOOGL** CALL 292.5 2026-11-13 (2DTE): 5,571 traded vs OI 5,570
- **SMCI** PUT 28 2026-11-13 (2DTE): 1,676 traded vs OI 1,655
- **MU** PUT 807.5 2026-11-13 (2DTE): 511 traded vs OI 1
- **MU** PUT 810 2026-11-16 (5DTE): 529 traded vs OI 18
- **UBER** PUT 67 2026-12-04 (23DTE): 515 traded vs OI 97

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
