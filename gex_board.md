# GEX + FLOW SCAN - Thu Nov 12, 11:30 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (5)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 10:35 | **SPY** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/12 754P | 0.59 | 0.09 | +10% (1m) | **-85%** | +70% | 755 |
| 09:50 | **HOOD** | **PUTS** | TREND + FLOW | 11/13 79P | 0.55 | 0.36 | +5% (19m) | **-35%** (done) | +92% | 80 |
| 09:45 | **ORCL** | **CALLS** | PIN AT PUT WALL (positive gamma) - bounce | 11/13 130C | 0.75 | 0.72 | +4% (60m) | **-4%** (done) | +59% | 126.9 |
| 09:45 | **SMCI** | **PUTS** | TREND + FLOW | 11/13 27P | 0.42 | 0.23 | -5% (6m) | **-45%** (done) | +57% | 27 |
| 09:45 | **SPY** | **PUTS** | RUN: clean trend + negative gamma + flow agrees | 11/12 753P | 0.79 | 0.31 | +23% (18m) | **-61%** (done) | +51% | 754.88 |

## 1m RULES on SPY / QQQ - loose (1 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 11:30:08 ET, last candle SPY 11:29, QQQ 11:29 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 10:03 | SPY | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |

## Flow surges NOT fired - price disagreed (3 today, last 5)
- 10:30 IWM CALLS: price -0.04 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:25 IWM CALLS: price -0.79 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:20 IWM CALLS: price -0.12 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **AMD** | 589.39 | TREND (flow not with it) | **CALLS** | 40 | none: 138 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (5 contracts' greeks worked out here) | POS +$194.4M | - | 600 | 550 | -$45.8M | +$234k bull / -$11.0M bear | LONG (clean 34, ADX 38, RVol 2.0) |
| 2 | **SHOP** | 150.12 | PINNED between the walls (positive gamma) - chop | **-** | 35 | - | POS +$6.2M | 143.22 | 150 | 150 | -$21k | - | out (clean 30, ADX 22, RVol 1.1) |
| 3 | **AMZN** | 269.78 | PINNED between the walls (positive gamma) - chop | **-** | 34 | - | POS +$511.6M | - | 270 | 270 | -$7.5M | +$84k bull / +$0 bear | out (clean 31, ADX 22, RVol 0.8) |
| 4 | **HOOD** | 84.28 | TREND (flow not with it) | **CALLS** | 26 | none: 17 calls 0-7DTE > 2 priced 0.40-0.80 > 2 delta 0.2+ > 2 spread ok > 2 liquid > best one only +14% at the target (needs +20%) (3 contracts' greeks worked out here) | POS +$16.2M | 79.26 | 85 | 80 | -$298k | - | LONG (clean 34, ADX 27, RVol 0.8) |
| 5 | **MSTR** | 118.63 | - | **-** | 24 | - | NEG -$28.7M | - | 125 | 120 | -$2.5M | +$118k bull / +$0 bear | out (clean 28, ADX 31, RVol 1.7) |
| 6 | **SPY** | 762.00 | - | **-** | 23 | - | POS +$212.6M | 761.44 | 760 | 760 | -$157.7M | +$1.2M bull / -$1.4M bear | out (clean 31, ADX 28, RVol 1.1) |
| 7 | **QQQ** | 692.68 | - | **-** | 23 | - | POS +$281.7M | 691.2 | 700 | 680 | -$134.3M | +$1.3M bull / -$1.4M bear | out (clean 31, ADX 30, RVol 1.0) |
| 8 | **NVDA** | 165.51 | - | **-** | 23 | - | NEG -$185.7M | - | 170 | 160 | -$104.7M | +$4.1M bull / -$3.0M bear | out (clean 33, ADX 26, RVol 1.4) |
| 9 | **MSFT** | 528.66 | - | **-** | 23 | - | POS +$210.2M | 520.05 | 535 | 520 | -$4.3M | +$0 bull / -$89k bear | out (clean 31, ADX 36, RVol 0.7) |
| 10 | **GOOGL** | 298.69 | - | **-** | 23 | - | POS +$127.4M | 288.87 | 300 | 290 | -$3.0M | +$55k bull / -$227k bear | out (clean 29, ADX 31, RVol 2.0) |
| 11 | **UBER** | 69.86 | PINNED between the walls (positive gamma) - chop | **-** | 23 | - | POS +$16.5M | 68.29 | 70 | 70 | -$72k | - | out (clean 31, ADX 24, RVol 0.4) |
| 12 | **AVGO** | 368.31 | - | **-** | 22 | - | POS +$137.1M | - | 380 | 350 | +$3.2M | +$0 bull / -$410k bear | out (clean 35, ADX 34, RVol 2.0) |
| 13 | **ORCL** | 128.34 | - | **-** | 21 | - | POS +$15.0M | - | 130 | 125 | -$660k | +$122k bull / +$0 bear | out (clean 29, ADX 27, RVol 0.7) |
| 14 | **META** | 625.85 | - | **-** | 20 | - | POS +$7.8M | 624.15 | 650 | 600 | +$1.8M | +$228k bull / -$129k bear | out (clean 28, ADX 38, RVol 0.7) |
| 15 | **AAPL** | 358.14 | - | **-** | 19 | - | POS +$1.2B | 339.32 | 360 | 360 | -$560k | +$135k bull / -$267k bear | out (clean 28, ADX 40, RVol 0.8) |
| 16 | **IWM** | 281.32 | - | **-** | 18 | - | NEG -$721.6M | 282.75 | 285 | 275 | -$1.5M | +$0 bull / -$182k bear | out (clean 34, ADX 34, RVol 0.7) |
| 17 | **MU** | 792.52 | - | **-** | 17 | - | POS +$102.2M | - | 800 | 800 | +$10.8M | +$3.0M bull / -$1.4M bear | out (clean 31, ADX 27, RVol 0.6) |
| 18 | **BABA** | 95.16 | - | **-** | 17 | - | NEG -$19.5M | - | 100 | 100 | +$148k | - | out (clean 29, ADX 52, RVol 2.6) |
| 19 | **TSLA** | 392.71 | - | **-** | 16 | - | POS +$382.7M | - | 400 | 380 | +$4.8M | +$0 bull / -$468k bear | out (clean 29, ADX 21, RVol 0.5) |
| 20 | **SMCI** | 27.45 | - | **-** | 15 | - | POS +$1.2M | 26.54 | 30 | 25 | -$129k | - | out (clean 33, ADX 36, RVol 4.7) |
| 21 | **SMH** | 507.45 | - | **-** | 12 | - | NEG -$73.2M | - | 500 | 500 | -$2.1M | - | out (clean 31, ADX 29, RVol 0.8) |
| 22 | **NFLX** | 63.68 | - | **-** | 11 | - | NEG -$7.4M | 64.01 | 65 | 65 | -$227k | - | out (clean 27, ADX 25, RVol 0.5) |
| 23 | **ARM** | 202.77 | - | **-** | 11 | - | POS +$9.9M | - | 200 | 200 | -$347k | - | out (clean 31, ADX 20, RVol 0.4) |
| 24 | **COIN** | 134.51 | - | **-** | 10 | - | POS +$11.9M | 129.91 | 137 | 135 | -$66k | - | out (clean 29, ADX 34, RVol 1.5) |
| 25 | **PLTR** | 172.16 | - | **-** | 9 | - | POS +$92.4M | - | 170 | 170 | -$354k | - | out (clean 27, ADX 32, RVol 0.4) |
| 26 | **DELL** | 372.08 | - | **-** | 7 | - | POS +$5.6M | - | 360 | 340 | +$216k | - | out (clean 36, ADX 23, RVol 1.0) |
| 27 | **CRM** | 216.84 | - | **-** | 6 | - | NEG -$8.3M | - | 220 | 220 | -$18k | - | out (clean 28, ADX 20, RVol 0.4) |

## Big prints this scan (185)
- **AMD** PUT 617.5 2026-11-16 (4DTE): 100 @ 36.42 = **+$364k** BUY | vol 100 / OI 0
- **AMD** PUT 615 2026-11-16 (4DTE): 100 @ 34.47 = **+$345k** BUY | vol 107 / OI 1
- **AMD** PUT 617.5 2026-11-18 (6DTE): 80 @ 40.09 = **+$321k** BUY | vol 201 / OI 0
- **QQQ** CALL 692 2026-11-12 (0DTE): 986 @ 3.21 = **+$317k** BUY | vol 94,636 / OI 513
- **AMD** PUT 615 2026-11-18 (6DTE): 80 @ 38.32 = **+$307k** BUY | vol 200 / OI 0
- **MU** CALL 770 2026-11-13 (1DTE): 100 @ 30.00 = **+$300k** BUY | vol 8,039 / OI 1,263
- **QQQ** CALL 692 2026-11-12 (0DTE): 906 @ 3.20 = **+$290k** BUY | vol 94,636 / OI 513
- **SPY** CALL 760 2026-11-16 (4DTE): 440 @ 5.65 = **+$249k** BUY | vol 5,512 / OI 1,658
- **AMD** PUT 617.5 2026-11-18 (6DTE): 60 @ 40.09 = **+$241k** BUY | vol 201 / OI 0
- **AMD** PUT 617.5 2026-11-18 (6DTE): 60 @ 40.09 = **+$241k** BUY | vol 201 / OI 0
- **AMD** PUT 615 2026-11-18 (6DTE): 60 @ 38.32 = **+$230k** BUY | vol 200 / OI 0
- **AMD** PUT 615 2026-11-18 (6DTE): 60 @ 38.32 = **+$230k** BUY | vol 200 / OI 0
- **QQQ** CALL 690 2026-11-12 (0DTE): 500 @ 4.20 = **+$210k** BUY | vol 171,203 / OI 1,788
- **SPY** CALL 758 2026-11-13 (1DTE): 267 @ 6.12 = **+$163k** BUY | vol 18,655 / OI 3,119
- **SPY** PUT 760 2026-11-17 (5DTE): 450 @ 3.63 = **+$163k** SELL | vol 1,903 / OI 187

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 746 2026-11-16 (4DTE): 543 traded vs OI 533
- **SPY** CALL 794 2026-11-17 (5DTE): 2,402 traded vs OI 227
- **SPY** CALL 759 2026-11-17 (5DTE): 540 traded vs OI 390
- **SPY** CALL 795 2026-11-17 (5DTE): 1,705 traded vs OI 176
- **SPY** CALL 777 2026-11-12 (0DTE): 769 traded vs OI 766
- **SPY** CALL 772 2026-11-16 (4DTE): 1,676 traded vs OI 1,527
- **SPY** PUT 762 2026-11-13 (1DTE): 2,074 traded vs OI 2,068
- **SPY** PUT 767 2026-11-12 (0DTE): 587 traded vs OI 3
- **SPY** CALL 780 2026-11-17 (5DTE): 609 traded vs OI 599
- **SPY** CALL 774 2026-11-16 (4DTE): 757 traded vs OI 523
- **SPY** PUT 766 2026-11-12 (0DTE): 636 traded vs OI 74
- **SPY** PUT 747 2026-11-13 (1DTE): 4,452 traded vs OI 3,309
- **SPY** PUT 753 2026-11-23 (11DTE): 531 traded vs OI 149
- **SPY** PUT 755 2026-11-19 (7DTE): 507 traded vs OI 275
- **SPY** PUT 738 2026-11-23 (11DTE): 508 traded vs OI 125

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
