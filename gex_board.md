# GEX + FLOW SCAN - Thu Nov 12, 11:10 AM ET
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
Last 1m check 11:10:08 ET, last candle SPY 11:09, QQQ 11:09 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 10:03 | SPY | 1m AGREE FLIP | FULL | PUTS | down | logged (agree flip) |

## Flow surges NOT fired - price disagreed (3 today, last 5)
- 10:30 IWM CALLS: price -0.04 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:25 IWM CALLS: price -0.79 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:20 IWM CALLS: price -0.12 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **SHOP** | 149.96 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 39 | none: 21 calls 0-7DTE > 1 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (6 contracts' greeks worked out here) | POS +$7.0M | 142.86 | 155 | 150 | -$6k | - | out (clean 30, ADX 22, RVol 1.8) |
| 2 | **SPY** | 762.02 | FLIP CROSS up into positive gamma | **CALLS** | 36 | 11/12 765C @ 0.49 (delta 0.22) = est +144% at 764.85 | POS +$316.5M | 761.68 | 760 | 760 | -$100.5M | +$0 bull / -$1.7M bear | out (clean 31, ADX 24, RVol 1.0) |
| 3 | **QQQ** | 693.30 | FLIP CROSS up into positive gamma | **CALLS** | 35 | none: 678 calls 0-7DTE > 23 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (227 contracts' greeks worked out here) | POS +$464.4M | 691 | 700 | 680 | -$89.4M | +$0 bull / -$1.9M bear | out (clean 30, ADX 29, RVol 0.8) |
| 4 | **HOOD** | 84.39 | TREND (flow not with it) | **CALLS** | 35 | none: 17 calls 0-7DTE > 2 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only +10% at the target (needs +20%) (2 contracts' greeks worked out here) | POS +$17.0M | - | 85 | 85 | -$255k | +$0 bull / -$33k bear | LONG (clean 33, ADX 27, RVol 1.8) |
| 5 | **AMZN** | 270.53 | PINNED between the walls (positive gamma) - chop | **-** | 32 | - | POS +$505.2M | - | 270 | 270 | -$6.2M | +$0 bull / -$44k bear | out (clean 31, ADX 22, RVol 0.5) |
| 6 | **AMD** | 588.79 | TREND (flow not with it) | **CALLS** | 30 | none: 141 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (5 contracts' greeks worked out here) | POS +$189.9M | - | 600 | 550 | -$231k | +$0 bull / -$4.6M bear | LONG (clean 34, ADX 31, RVol 1.7) |
| 7 | **NVDA** | 166.92 | - | **-** | 25 | - | NEG -$154.9M | - | 170 | 160 | -$106.7M | +$323k bull / -$3.8M bear | out (clean 32, ADX 32, RVol 1.7) |
| 8 | **ORCL** | 128.66 | - | **-** | 25 | - | POS +$13.0M | - | 130 | 130 | -$1.0M | +$0 bull / -$140k bear | out (clean 29, ADX 24, RVol 0.7) |
| 9 | **UBER** | 69.86 | PINNED between the walls (positive gamma) - chop | **-** | 24 | - | POS +$16.8M | 68.3 | 70 | 70 | -$34k | - | out (clean 31, ADX 30, RVol 0.7) |
| 10 | **MSFT** | 528.28 | - | **-** | 22 | - | POS +$212.0M | 520.67 | 535 | 520 | -$3.6M | +$0 bull / -$285k bear | out (clean 31, ADX 33, RVol 0.7) |
| 11 | **ARM** | 204.64 | - | **-** | 22 | - | POS +$9.7M | - | 200 | 200 | -$316k | +$0 bull / -$37k bear | out (clean 30, ADX 26, RVol 0.4) |
| 12 | **AVGO** | 364.70 | - | **-** | 21 | - | POS +$128.8M | - | 350 | 350 | +$5.4M | +$0 bull / -$228k bear | out (clean 35, ADX 33, RVol 1.2) |
| 13 | **META** | 626.32 | - | **-** | 20 | - | POS +$10.5M | 624.62 | 650 | 600 | +$299k | +$0 bull / -$119k bear | out (clean 28, ADX 47, RVol 1.1) |
| 14 | **IWM** | 281.52 | - | **-** | 19 | - | NEG -$532.3M | 282.86 | 285 | 275 | +$327k | +$0 bull / -$155k bear | out (clean 34, ADX 42, RVol 0.7) |
| 15 | **AAPL** | 358.05 | - | **-** | 19 | - | POS +$1.2B | 338.96 | 360 | 360 | -$461k | +$0 bull / -$291k bear | out (clean 28, ADX 42, RVol 0.7) |
| 16 | **MU** | 793.23 | - | **-** | 19 | - | POS +$99.7M | - | 800 | 800 | +$9.6M | +$0 bull / -$3.7M bear | out (clean 31, ADX 33, RVol 0.8) |
| 17 | **MSTR** | 118.92 | - | **-** | 18 | - | NEG -$26.7M | - | 125 | 120 | -$3.2M | - | out (clean 27, ADX 30, RVol 1.9) |
| 18 | **TSLA** | 392.00 | - | **-** | 17 | - | POS +$359.1M | - | 400 | 380 | +$6.8M | +$0 bull / -$700k bear | out (clean 29, ADX 26, RVol 0.3) |
| 19 | **SMCI** | 28.84 | - | **-** | 17 | - | POS +$4.9M | - | 30 | 30 | -$186k | - | out (clean 33, ADX 41, RVol 1.8) |
| 20 | **BABA** | 94.84 | - | **-** | 16 | - | NEG -$19.4M | - | 100 | 100 | +$197k | - | out (clean 29, ADX 57, RVol 1.3) |
| 21 | **SMH** | 508.71 | - | **-** | 12 | - | NEG -$70.9M | - | 500 | 500 | -$2.1M | - | out (clean 30, ADX 32, RVol 0.5) |
| 22 | **NFLX** | 63.59 | - | **-** | 12 | - | NEG -$8.7M | 64.04 | 65 | 65 | -$196k | - | out (clean 27, ADX 31, RVol 0.7) |
| 23 | **PLTR** | 172.07 | - | **-** | 10 | - | POS +$84.7M | - | 170 | 170 | -$229k | - | out (clean 27, ADX 38, RVol 0.4) |
| 24 | **COIN** | 134.43 | - | **-** | 10 | - | POS +$15.1M | 129.9 | 137 | 135 | +$41k | - | out (clean 29, ADX 36, RVol 1.4) |
| 25 | **GOOGL** | 299.08 | - | **-** | 8 | - | POS +$125.4M | 288.63 | 300 | 290 | +$91k | - | out (clean 28, ADX 24, RVol 1.6) |
| 26 | **CRM** | 216.62 | - | **-** | 7 | - | NEG -$9.4M | - | 220 | 220 | -$9k | - | out (clean 28, ADX 25, RVol 0.6) |
| 27 | **DELL** | 367.23 | - | **-** | 6 | - | POS +$5.5M | - | 360 | 340 | +$11k | - | out (clean 36, ADX 28, RVol 0.7) |

## Big prints this scan (120)
- **AMD** CALL 575 2026-11-13 (1DTE): 457 @ 13.19 = **+$603k** SELL | vol 8,740 / OI 1,800
- **AMD** CALL 575 2026-11-13 (1DTE): 293 @ 13.20 = **+$387k** SELL | vol 8,740 / OI 1,800
- **MU** CALL 775 2026-11-18 (6DTE): 100 @ 34.00 = **+$340k** SELL | vol 598 / OI 814
- **AMD** CALL 590 2026-11-13 (1DTE): 457 @ 6.89 = **+$315k** SELL | vol 5,135 / OI 1,196
- **MU** CALL 785 2026-11-13 (1DTE): 176 @ 12.50 = **+$220k** SELL | vol 4,388 / OI 317
- **AMD** CALL 590 2026-11-13 (1DTE): 293 @ 6.90 = **+$202k** SELL | vol 5,135 / OI 1,196
- **AMD** CALL 575 2026-11-18 (6DTE): 100 @ 20.00 = **+$200k** SELL | vol 385 / OI 54
- **QQQ** CALL 685 2026-11-19 (7DTE): 150 @ 12.15 = **+$182k** SELL | vol 344 / OI 414
- **AMD** CALL 565 2026-11-13 (1DTE): 98 @ 18.30 = **+$179k** SELL | vol 6,066 / OI 618
- **QQQ** CALL 659 2026-11-12 (0DTE): 55 @ 30.02 = **+$165k** SELL | vol 68 / OI 438
- **NVDA** CALL 170 2026-11-13 (1DTE): 1,000 @ 1.62 = **+$162k** SELL | vol 126,125 / OI 11,191
- **NVDA** CALL 160 2026-11-13 (1DTE): 225 @ 6.90 = **+$155k** SELL | vol 118,940 / OI 2,015
- **NVDA** CALL 160 2026-11-16 (4DTE): 200 @ 7.53 = **+$151k** SELL | vol 15,077 / OI 766
- **MU** CALL 800 2026-11-13 (1DTE): 164 @ 8.70 = **+$143k** SELL | vol 13,851 / OI 5,964
- **QQQ** CALL 686 2026-11-12 (0DTE): 344 @ 3.98 = **+$137k** SELL | vol 67,347 / OI 503

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 767 2026-11-16 (4DTE): 964 traded vs OI 928
- **SPY** PUT 764 2026-11-12 (0DTE): 697 traded vs OI 674
- **SPY** CALL 755 2026-11-13 (1DTE): 7,475 traded vs OI 7,349
- **SPY** PUT 759 2026-11-16 (4DTE): 567 traded vs OI 142
- **SPY** CALL 765 2026-11-16 (4DTE): 1,756 traded vs OI 1,546
- **SPY** CALL 756 2026-11-20 (8DTE): 2,833 traded vs OI 2,827
- **QQQ** CALL 693 2026-11-16 (4DTE): 507 traded vs OI 244
- **QQQ** CALL 683 2026-11-13 (1DTE): 1,262 traded vs OI 1,252
- **QQQ** CALL 692 2026-11-18 (6DTE): 513 traded vs OI 145
- **NVDA** CALL 182.5 2026-11-18 (6DTE): 2,450 traded vs OI 0
- **NVDA** CALL 182.5 2026-11-16 (4DTE): 6,270 traded vs OI 0
- **NVDA** PUT 170 2026-11-13 (1DTE): 15,939 traded vs OI 14,967
- **NVDA** CALL 182.5 2026-11-20 (8DTE): 7,379 traded vs OI 0
- **NVDA** CALL 182.5 2026-11-13 (1DTE): 19,913 traded vs OI 0
- **TSLA** PUT 390 2026-11-18 (6DTE): 510 traded vs OI 131

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
