# GEX + FLOW SCAN - Thu Nov 05, 10:30 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (3)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 09:52 | **SPY** | **PUTS** | 1m WHIPSAW (R1) | 11/05 749P | 0.78 | 4.04 | +617% (36m) | **+418%** | +47% | 753.11 hit |
| 09:50 | **BABA** | **CALLS** | TREND + FLOW | 11/06 111C | 0.48 | 0.22 | -12% (0m) | **-54%** | +136% | 110 |
| 09:40 | **QQQ** | **CALLS** | 1m WHIPSAW (R1) | 11/05 683C | 0.78 | 0.14 | -4% (0m) | **-82%** | +66% | 678.43 |

## 1m RULES on SPY / QQQ - loose (2 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 10:30:08 ET, last candle SPY 10:29, QQQ 10:29 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 09:51 | SPY | 1m WHIPSAW | R1 | PUTS | TURNING away | **FIRE** SPY261105P00749000 |
| 09:39 | QQQ | 1m WHIPSAW | R1 | CALLS | AGAINST you | **FIRE** QQQ261105C00683000 |

## Flow surges NOT fired - price disagreed (14 today, last 5)
- 10:30 HOOD CALLS: price -0.77 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:25 BABA CALLS: under EMA 20 - flow says one way, price says the other
- 10:25 HOOD CALLS: price -1.21 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:20 BABA CALLS: price -0.42 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 10:20 HOOD CALLS: price -0.79 over the last 15 min / under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **MSFT** | 541.29 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 68 | none: 132 puts 0-7DTE > 12 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (4 contracts' greeks worked out here) | POS +$871.1M | - | 540 | 500 | +$18.0M | +$3.2M bull / +$0 bear | out (clean 31, ADX 48, RVol 2.8) |
| 2 | **SMH** | 461.98 | FLOW SURGE | **CALLS** | 67 | none: 92 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (4 contracts' greeks worked out here) | NEG -$322.7M | - | 505 | 500 | +$16.9M | +$5.6M bull / +$0 bear | SHORT (clean 34, ADX 54, RVol 2.8) |
| 3 | **QQQ** | 659.50 | FLOW SURGE | **CALLS** | 66 | none: 528 calls 0-7DTE > 39 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (181 contracts' greeks worked out here) | NEG -$5.3B | - | 700 | 680 | +$606.5M | +$30.8M bull / +$0 bear | SHORT (clean 34, ADX 58, RVol 3.6) |
| 4 | **DELL** | 327.02 | FLOW SURGE | **CALLS** | 66 | none: 19 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (10 contracts' greeks worked out here) | NEG -$12.9M | - | 350 | 340 | +$6.7M | +$373k bull / +$0 bear | SHORT (clean 34, ADX 49, RVol 2.2) |
| 5 | **SMCI** | 26.65 | FLOW SURGE | **CALLS** | 65 | none: 11 calls 0-7DTE > 2 priced 0.40-0.80 > 2 delta 0.2+ > 2 spread ok > 2 liquid > best one only +14% at the target (needs +20%) (3 contracts' greeks worked out here) | NEG -$2.8M | - | 28 | 27 | +$557k | +$91k bull / +$0 bear | SHORT (clean 36, ADX 54, RVol 2.2) |
| 6 | **AVGO** | 302.40 | FLOW SURGE | **CALLS** | 64 | none: 65 calls 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (3 contracts' greeks worked out here) | NEG -$123.2M | - | 330 | 300 | +$6.5M | +$202k bull / +$0 bear | out (clean 31, ADX 55, RVol 3.7) |
| 7 | **PLTR** | 156.00 | FLOW SURGE | **CALLS** | 64 | none: 15 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (2 contracts' greeks worked out here) | NEG -$45.4M | - | 165 | 150 | +$13.0M | +$1.4M bull / +$0 bear | out (clean 28, ADX 48, RVol 2.9) |
| 8 | **SHOP** | 139.05 | TREND (flow not with it) | **PUTS** | 64 | none: 26 puts 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (7 contracts' greeks worked out here) | NEG -$6.6M | - | 144 | 135 | +$194k | - | SHORT (clean 36, ADX 57, RVol 3.5) |
| 9 | **SPY** | 747.43 | FLOW SURGE | **CALLS** | 62 | none: 667 calls 0-7DTE > 25 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (318 contracts' greeks worked out here) | NEG -$11.5B | 770.21 | 760 | 750 | +$639.4M | +$16.6M bull / +$0 bear | SHORT (clean 34, ADX 58, RVol 2.2) |
| 10 | **TSLA** | 347.94 | FLOW SURGE | **CALLS** | 62 | none: 76 calls 0-7DTE > 4 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (5 contracts' greeks worked out here) | NEG -$157.2M | - | 370 | 350 | +$95.2M | +$1.7M bull / -$974k bear | SHORT (clean 34, ADX 55, RVol 5.9) |
| 11 | **NVDA** | 186.37 | FLOW SURGE | **CALLS** | 61 | none: 39 calls 0-7DTE > 5 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (1 contracts' greeks worked out here) | NEG -$295.4M | - | 200 | 190 | +$58.1M | +$6.7M bull / -$111k bear | out (clean 32, ADX 65, RVol 4.8) |
| 12 | **AMD** | 418.72 | FLOW SURGE | **CALLS** | 61 | none: 102 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (12 contracts' greeks worked out here) | NEG -$103.7M | - | 430 | 440 | +$40.8M | +$2.1M bull / +$0 bear | out (clean 32, ADX 47, RVol 2.9) |
| 13 | **MU** | 695.45 | FLOW SURGE | **CALLS** | 61 | none: 94 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (6 contracts' greeks worked out here) | NEG -$102.2M | - | 700 | 750 | +$166.1M | +$12.8M bull / -$1.5M bear | out (clean 32, ADX 64, RVol 4.6) |
| 14 | **META** | 595.91 | FLOW SURGE | **CALLS** | 60 | none: 138 calls 0-7DTE > 7 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (11 contracts' greeks worked out here) | NEG -$175.6M | 629.85 | 650 | 600 | +$30.9M | +$4.1M bull / -$26k bear | SHORT (clean 33, ADX 41, RVol 2.4) |
| 15 | **MSTR** | 129.89 | FLOW SURGE | **CALLS** | 60 | none: 26 calls 0-7DTE > 3 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (7 contracts' greeks worked out here) | POS +$61.9M | - | 135 | 125 | +$4.3M | +$195k bull / +$0 bear | SHORT (clean 34, ADX 64, RVol 2.9) |
| 16 | **ARM** | 168.55 | FLOW SURGE | **CALLS** | 58 | none: 12 calls 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (4 contracts' greeks worked out here) | NEG -$7.0M | - | 180 | 180 | +$1.3M | +$27k bull / +$0 bear | out (clean 27, ADX 56, RVol 2.8) |
| 17 | **AMZN** | 256.15 | FLOW SURGE | **CALLS** | 57 | none: 60 calls 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (2 contracts' greeks worked out here) | POS +$345.8M | - | 260 | 250 | +$31.4M | +$596k bull / +$0 bear | SHORT (clean 34, ADX 27, RVol 2.4) |
| 18 | **HOOD** | 78.13 | FLOW SURGE | **CALLS** | 57 | 11/06 82C @ 0.73 (delta 0.24) = est +66% at 80 | NEG -$9.5M | - | 85 | 80 | +$2.0M | +$79k bull / +$0 bear | out (clean 31, ADX 58, RVol 2.7) |
| 19 | **IWM** | 278.03 | TREND (flow not with it) | **PUTS** | 51 | 11/05 276P @ 0.61 (delta 0.27) = est +62% at 276.28 | NEG -$1.9B | 285.96 | 285 | 270 | +$25.3M | - | SHORT (clean 34, ADX 39, RVol 2.5) |
| 20 | **ORCL** | 116.72 | FLOW SURGE | **CALLS** | 50 | none: 23 calls 0-7DTE > 2 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (4 contracts' greeks worked out here) | NEG -$57.8M | - | 125 | 120 | +$2.2M | +$99k bull / +$0 bear | out (clean 33, ADX 48, RVol 1.0) |
| 21 | **AAPL** | 349.79 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 47 | none: 84 puts 0-7DTE > 9 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (8 contracts' greeks worked out here) | POS +$679.3M | 334.04 | 350 | 340 | +$6.8M | +$850k bull / -$1.4M bear | out (clean 30, ADX 18, RVol 2.1) |
| 22 | **GOOGL** | 283.88 | FLOW SURGE | **CALLS** | 45 | none: 66 calls 0-7DTE > 6 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (10 contracts' greeks worked out here) | POS +$31.5M | 281.18 | 285 | 290 | +$8.6M | +$1.4M bull / +$0 bear | out (clean 35, ADX 25, RVol 1.9) |
| 23 | **COIN** | 138.02 | - | **-** | 30 | - | POS +$21.0M | - | 142 | 135 | +$1.8M | - | out (clean 32, ADX 53, RVol 1.1) |
| 24 | **BABA** | 106.20 | - | **-** | 28 | - | POS +$22.0M | - | 110 | 100 | +$1.1M | - | out (clean 37, ADX 28, RVol 3.2) |
| 25 | **CRM** | 225.63 | - | **-** | 20 | - | NEG -$12.6M | - | 240 | 220 | +$258k | - | out (clean 34, ADX 18, RVol 2.5) |
| 26 | **UBER** | 68.89 | - | **-** | 15 | - | POS +$6.1M | 68.05 | 70 | 65 | +$116k | - | out (clean 33, ADX 20, RVol 1.5) |
| 27 | **NFLX** | 65.70 | - | **-** | 14 | - | POS +$32.4M | 62.08 | 65 | 65 | +$292k | - | out (clean 33, ADX 20, RVol 1.2) |

## Big prints this scan (315)
- **QQQ** PUT 686 2026-11-06 (1DTE): 500 @ 24.60 = **+$1.2M** SELL | vol 1,426 / OI 4,253
- **QQQ** PUT 685 2026-11-06 (1DTE): 500 @ 23.68 = **+$1.2M** SELL | vol 5,883 / OI 9,276
- **SMH** PUT 465 2026-11-06 (1DTE): 800 @ 8.63 = **+$690k** SELL | vol 1,428 / OI 10,681
- **QQQ** CALL 665 2026-11-05 (0DTE): 2,000 @ 2.78 = **+$556k** BUY | vol 21,645 / OI 21
- **QQQ** CALL 665 2026-11-05 (0DTE): 1,907 @ 2.86 = **+$545k** BUY | vol 21,645 / OI 21
- **TSLA** CALL 350 2026-11-06 (1DTE): 639 @ 7.60 = **+$486k** BUY | vol 10,704 / OI 1,359
- **SMH** PUT 470 2026-11-06 (1DTE): 400 @ 11.21 = **+$448k** SELL | vol 1,548 / OI 11,200
- **QQQ** PUT 686 2026-11-06 (1DTE): 174 @ 24.42 = **+$425k** SELL | vol 1,426 / OI 4,253
- **QQQ** PUT 686 2026-11-06 (1DTE): 174 @ 24.37 = **+$424k** SELL | vol 1,426 / OI 4,253
- **SMH** PUT 455 2026-11-06 (1DTE): 800 @ 4.90 = **+$392k** SELL | vol 1,124 / OI 619
- **QQQ** PUT 675 2026-11-10 (5DTE): 200 @ 17.50 = **+$350k** SELL | vol 362 / OI 478
- **META** CALL 602.5 2026-11-06 (1DTE): 451 @ 7.27 = **+$328k** MID | vol 1,206 / OI 77
- **QQQ** CALL 666 2026-11-05 (0DTE): 1,000 @ 2.57 = **+$257k** BUY | vol 19,933 / OI 0
- **QQQ** CALL 665 2026-11-09 (4DTE): 308 @ 7.99 = **+$246k** BUY | vol 2,689 / OI 100
- **QQQ** CALL 665 2026-11-09 (4DTE): 308 @ 7.99 = **+$246k** BUY | vol 2,689 / OI 100

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 741 2026-11-09 (4DTE): 536 traded vs OI 174
- **SPY** PUT 721 2026-11-09 (4DTE): 1,165 traded vs OI 54
- **SPY** PUT 716 2026-11-05 (0DTE): 1,095 traded vs OI 214
- **SPY** PUT 751 2026-11-10 (5DTE): 611 traded vs OI 28
- **SPY** PUT 727 2026-11-05 (0DTE): 633 traded vs OI 72
- **SPY** CALL 754 2026-11-09 (4DTE): 553 traded vs OI 412
- **SPY** CALL 740 2026-11-05 (0DTE): 507 traded vs OI 428
- **SPY** PUT 732 2026-11-09 (4DTE): 509 traded vs OI 37
- **SPY** CALL 749 2026-11-06 (1DTE): 547 traded vs OI 477
- **SPY** PUT 726 2026-11-06 (1DTE): 1,891 traded vs OI 1,626
- **SPY** PUT 742 2026-11-09 (4DTE): 535 traded vs OI 105
- **SPY** PUT 728 2026-11-05 (0DTE): 510 traded vs OI 16
- **SPY** PUT 736 2026-11-06 (1DTE): 4,263 traded vs OI 3,602
- **SPY** CALL 762 2026-11-06 (1DTE): 4,808 traded vs OI 4,453
- **SPY** CALL 750 2026-11-05 (0DTE): 7,734 traded vs OI 4,270

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
