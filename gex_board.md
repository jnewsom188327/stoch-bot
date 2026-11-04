# GEX + FLOW SCAN - Wed Nov 04, 12:00 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (8)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:38 | **QQQ** | **PUTS** | 1m FAILED POP (R3) | 11/04 686P | 0.80 | 0.18 | -1% (0m) | **-78%** | +26% | 689.6 |
| 11:21 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/04 685P | 0.67 | 0.18 | +66% (7m) | **-73%** | +25% | 690.3 hit |
| 10:20 | **SMCI** | **CALLS** | FLOW SURGE | 11/06 33C | 0.65 | 0.13 | -3% (1m) | **-80%** (done) | +39% | 32.81 |
| 10:20 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/04 284C | 0.49 | 0.17 | +2% (22m) | **-65%** (done) | +131% | 284.74 |
| 10:00 | **AMZN** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/04 267.5P | 0.68 | 1.54 | +169% (60m) | **+126%** (done) | +258% | 265.7 |
| 09:50 | **UBER** | **CALLS** | FLIP CROSS up into positive gamma | 11/06 71C | 0.60 | 1.56 | +168% (52m) | **+160%** (done) | +50% | 70 hit |
| 09:50 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/04 286C | 0.53 | 0.06 | +2% (1m) | **-89%** (done) | +150% | 287 |
| 09:45 | **UBER** | **PUTS** | FLIP CROSS down into negative gamma | 11/06 67P | 0.63 | 0.10 | -3% (1m) | **-84%** (done) | +27% | 68.03 |

## 1m RULES on SPY / QQQ - loose (2 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 12:00:08 ET, last candle SPY 11:59, QQQ 11:59 | no errors
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
| 1 | **AAPL** | 353.69 | FLOW SURGE | **PUTS** | 39 | none: 108 puts 0-7DTE > 10 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (61 contracts' greeks worked out here) | POS +$1.1B | 341.84 | 355 | 350 | -$81.7M | +$0 bull / -$474k bear | out (clean 32, ADX 51, RVol 0.8) |
| 2 | **NVDA** | 204.12 | FLIP CROSS down into negative gamma | **PUTS** | 34 | 11/04 202.5P @ 0.47 (delta 0.27) = est +431% at 200 | NEG -$11.3M | 204.15 | 210 | 200 | -$340k | +$0 bull / -$708k bear | out (clean 30, ADX 33, RVol 1.2) |
| 3 | **GOOGL** | 292.29 | FLOW SURGE | **PUTS** | 34 | 11/04 290P @ 0.54 (delta 0.25) = est +100% at 290 | POS +$97.1M | 283.79 | 290 | 290 | -$27.6M | +$0 bull / -$114k bear | out (clean 36, ADX 32, RVol 0.5) |
| 4 | **SMH** | 508.77 | - | **-** | 30 | - | NEG -$524.9M | - | 532.5 | 500 | +$12.9M | +$0 bull / -$12.1M bear | out (clean 32, ADX 30, RVol 1.6) |
| 5 | **MSFT** | 557.53 | - | **-** | 27 | - | POS +$986.3M | - | 550 | 535 | -$21.5M | +$0 bull / -$1.6M bear | out (clean 28, ADX 64, RVol 1.5) |
| 6 | **MU** | 809.97 | - | **-** | 25 | - | NEG -$359.9M | - | 850 | 800 | +$94.5M | +$1.1M bull / -$2.3M bear | out (clean 31, ADX 32, RVol 1.2) |
| 7 | **AMZN** | 268.18 | - | **-** | 24 | - | POS +$541.9M | - | 270 | 250 | -$19.4M | +$0 bull / -$178k bear | out (clean 35, ADX 39, RVol 0.8) |
| 8 | **TSLA** | 385.04 | - | **-** | 23 | - | NEG -$126.4M | 395.42 | 400 | 380 | -$67.2M | +$0 bull / -$1.0M bear | out (clean 30, ADX 21, RVol 1.4) |
| 9 | **DELL** | 374.93 | - | **-** | 23 | - | NEG -$30.1M | - | 400 | 400 | +$1.5M | +$0 bull / -$28k bear | out (clean 33, ADX 36, RVol 1.8) |
| 10 | **SMCI** | 30.39 | - | **-** | 23 | - | NEG -$644k | - | 33 | 30 | +$1.9M | - | out (clean 34, ADX 46, RVol 1.0) |
| 11 | **UBER** | 71.81 | - | **-** | 22 | - | POS +$13.4M | 68.26 | 70 | 70 | -$1.4M | - | out (clean 30, ADX 51, RVol 0.9) |
| 12 | **SPY** | 768.60 | - | **-** | 21 | - | NEG -$1.9B | 770.22 | 770 | 750 | -$124.2M | +$0 bull / -$2.4M bear | out (clean 32, ADX 28, RVol 1.2) |
| 13 | **AMD** | 490.33 | - | **-** | 20 | - | NEG -$64.5M | - | 500 | 500 | +$37.8M | +$180k bull / -$799k bear | out (clean 32, ADX 15, RVol 1.1) |
| 14 | **IWM** | 284.10 | - | **-** | 19 | - | NEG -$204.5M | 284.65 | 285 | 270 | +$10.0M | +$0 bull / -$348k bear | out (clean 34, ADX 18, RVol 1.1) |
| 15 | **AVGO** | 328.60 | - | **-** | 19 | - | NEG -$88.9M | - | 340 | 330 | +$1.3M | +$0 bull / -$203k bear | out (clean 31, ADX 27, RVol 1.2) |
| 16 | **MSTR** | 144.94 | - | **-** | 19 | - | POS +$122.4M | - | 135 | 150 | -$252k | +$0 bull / -$224k bear | out (clean 31, ADX 40, RVol 0.7) |
| 17 | **BABA** | 107.23 | - | **-** | 19 | - | POS +$15.6M | - | 110 | 110 | -$868k | - | out (clean 36, ADX 50, RVol 1.5) |
| 18 | **QQQ** | 696.41 | - | **-** | 18 | - | NEG -$4.5B | 721.19 | 700 | 680 | -$141.8M | +$0 bull / -$8.8M bear | out (clean 31, ADX 18, RVol 0.7) |
| 19 | **ARM** | 196.28 | - | **-** | 18 | - | NEG -$7.4M | - | 212.5 | 200 | +$55k | +$0 bull / -$90k bear | out (clean 26, ADX 33, RVol 1.0) |
| 20 | **NFLX** | 66.17 | - | **-** | 17 | - | POS +$19.1M | 62.43 | 65 | 65 | -$2.1M | - | out (clean 31, ADX 58, RVol 0.7) |
| 21 | **HOOD** | 87.77 | - | **-** | 17 | - | POS +$2.0M | 85.63 | 90 | 90 | -$1.3M | +$0 bull / -$33k bear | out (clean 28, ADX 16, RVol 0.8) |
| 22 | **META** | 636.28 | - | **-** | 16 | - | POS +$198.2M | 623.64 | 650 | 625 | +$2.8M | +$0 bull / -$412k bear | out (clean 29, ADX 24, RVol 0.6) |
| 23 | **SHOP** | 152.93 | - | **-** | 15 | - | NEG -$5.2M | - | 160 | 150 | -$381k | - | out (clean 34, ADX 32, RVol 0.4) |
| 24 | **COIN** | 152.05 | - | **-** | 13 | - | POS +$29.1M | - | 148 | 150 | -$1.3M | - | out (clean 31, ADX 20, RVol 0.7) |
| 25 | **ORCL** | 127.53 | - | **-** | 12 | - | NEG -$30.7M | - | 130 | 125 | +$2.2M | - | out (clean 35, ADX 15, RVol 2.8) |
| 26 | **CRM** | 226.05 | - | **-** | 11 | - | NEG -$12.5M | - | 240 | 220 | -$132k | - | out (clean 32, ADX 35, RVol 0.6) |
| 27 | **PLTR** | 172.30 | - | **-** | 7 | - | NEG -$46.1M | - | 180 | 170 | -$2.2M | - | out (clean 26, ADX 22, RVol 0.8) |

## Big prints this scan (104)
- **SMH** PUT 500 2026-11-06 (2DTE): 19,686 @ 5.90 = **+$11.6M** BUY | vol 22,628 / OI 37,205
- **SPY** PUT 770 2026-11-05 (1DTE): 901 @ 5.01 = **+$451k** BUY | vol 16,225 / OI 1,690
- **SPY** PUT 770 2026-11-05 (1DTE): 500 @ 5.18 = **+$259k** BUY | vol 16,225 / OI 1,690
- **SPY** PUT 770 2026-11-05 (1DTE): 500 @ 5.18 = **+$259k** BUY | vol 16,225 / OI 1,690
- **QQQ** CALL 683 2026-11-06 (2DTE): 166 @ 13.34 = **+$221k** SELL | vol 1,391 / OI 3,485
- **QQQ** CALL 683 2026-11-06 (2DTE): 148 @ 13.33 = **+$197k** SELL | vol 1,391 / OI 3,485
- **QQQ** CALL 683 2026-11-06 (2DTE): 146 @ 13.28 = **+$194k** SELL | vol 1,391 / OI 3,485
- **QQQ** CALL 683 2026-11-06 (2DTE): 131 @ 13.30 = **+$174k** SELL | vol 1,391 / OI 3,485
- **MSFT** CALL 537.5 2026-11-06 (2DTE): 82 @ 19.53 = **+$160k** SELL | vol 432 / OI 1,073
- **QQQ** CALL 683 2026-11-06 (2DTE): 117 @ 13.25 = **+$155k** SELL | vol 1,391 / OI 3,485
- **MSFT** CALL 537.5 2026-11-04 (0DTE): 82 @ 18.28 = **+$150k** SELL | vol 497 / OI 442
- **QQQ** CALL 683 2026-11-06 (2DTE): 104 @ 13.31 = **+$138k** SELL | vol 1,391 / OI 3,485
- **MSFT** CALL 537.5 2026-11-06 (2DTE): 67 @ 19.58 = **+$131k** SELL | vol 432 / OI 1,073
- **QQQ** CALL 683 2026-11-06 (2DTE): 95 @ 13.29 = **+$126k** SELL | vol 1,391 / OI 3,485
- **QQQ** CALL 683 2026-11-06 (2DTE): 93 @ 13.31 = **+$124k** SELL | vol 1,391 / OI 3,485

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 771 2026-11-10 (6DTE): 578 traded vs OI 0
- **SPY** CALL 769 2026-11-09 (5DTE): 513 traded vs OI 0
- **SPY** PUT 760 2026-11-06 (2DTE): 12,646 traded vs OI 12,306
- **SPY** CALL 777 2026-11-10 (6DTE): 626 traded vs OI 0
- **SPY** PUT 700 2026-11-16 (12DTE): 503 traded vs OI 53
- **SPY** CALL 791 2026-11-13 (9DTE): 1,858 traded vs OI 1,844
- **SPY** PUT 768 2026-11-10 (6DTE): 524 traded vs OI 0
- **SPY** PUT 756 2026-11-13 (9DTE): 1,640 traded vs OI 1,447
- **SPY** CALL 763 2026-11-11 (7DTE): 515 traded vs OI 0
- **SPY** CALL 766 2026-11-11 (7DTE): 575 traded vs OI 0
- **SPY** CALL 785 2026-11-27 (23DTE): 1,104 traded vs OI 1,094
- **SPY** CALL 780 2026-12-04 (30DTE): 1,899 traded vs OI 1,878
- **QQQ** CALL 699 2026-11-09 (5DTE): 506 traded vs OI 0
- **QQQ** CALL 716 2026-11-06 (2DTE): 1,406 traded vs OI 1,398
- **QQQ** PUT 688 2026-11-20 (16DTE): 2,522 traded vs OI 2,011

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
