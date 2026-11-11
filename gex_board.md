# GEX + FLOW SCAN - Wed Nov 11, 03:05 PM ET
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
Last 1m check 15:05:08 ET, last candle SPY 15:04, QQQ 15:04 | no errors
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
| 1 | **MSFT** | 519.85 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 36 | none: 162 calls 0-7DTE > 8 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (61 contracts' greeks worked out here) | POS +$45.2M | 515.98 | 535 | 520 | +$14.5M | +$320k bull / +$0 bear | out (clean 32, ADX 16, RVol 0.5) |
| 2 | **META** | 635.94 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 28 | 11/11 637.5C @ 0.69 (delta 0.32) = est +22% at 638.37 | POS +$171.3M | 630.07 | 650 | 635 | +$5.5M | - | out (clean 30, ADX 43, RVol 0.5) |
| 3 | **AAPL** | 354.61 | PINNED between the walls (positive gamma) - chop | **-** | 26 | - | POS +$2.4B | 341.28 | 355 | 355 | +$696k | +$55k bull / +$0 bear | out (clean 28, ADX 23, RVol 0.2) |
| 4 | **IWM** | 283.04 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 25 | none: 340 puts 0-7DTE > 14 priced 0.40-0.80 > 6 delta 0.2+ > 6 spread ok > 6 liquid > best one only +14% at the target (needs +20%) (151 contracts' greeks worked out here) | POS +$214.5M | 282.69 | 283 | 270 | -$5.0M | - | out (clean 35, ADX 24, RVol 0.3) |
| 5 | **AMD** | 557.37 | - | **-** | 23 | - | POS +$141.7M | - | 550 | 550 | -$93.5M | +$5.2M bull / +$0 bear | out (clean 35, ADX 32, RVol 0.3) |
| 6 | **AVGO** | 348.42 | - | **-** | 22 | - | POS +$105.6M | - | 350 | 340 | +$8.9M | +$42k bull / -$202k bear | out (clean 37, ADX 35, RVol 0.4) |
| 7 | **MU** | 816.79 | - | **-** | 21 | - | POS +$170.8M | - | 800 | 800 | -$201.0M | +$1.9M bull / -$1.2M bear | out (clean 34, ADX 24, RVol 0.3) |
| 8 | **SPY** | 760.41 | - | **-** | 19 | - | NEG -$924.6M | 761.63 | 760 | 750 | -$122.6M | +$176k bull / -$139k bear | out (clean 34, ADX 28, RVol 0.2) |
| 9 | **QQQ** | 692.00 | - | **-** | 19 | - | POS +$410.0M | 689.99 | 700 | 680 | -$137.2M | +$229k bull / +$0 bear | out (clean 33, ADX 29, RVol 0.2) |
| 10 | **MSTR** | 121.60 | - | **-** | 18 | - | NEG -$7.9M | 123.6 | 133 | 120 | +$1.8M | +$25k bull / +$0 bear | out (clean 28, ADX 21, RVol 0.4) |
| 11 | **NVDA** | 175.42 | - | **-** | 17 | - | NEG -$179.0M | 181.42 | 175 | 175 | -$21.8M | +$421k bull / -$765k bear | out (clean 35, ADX 28, RVol 0.4) |
| 12 | **SHOP** | 149.40 | - | **-** | 17 | - | POS +$3.6M | 145.42 | 150 | 140 | -$478k | - | out (clean 33, ADX 15, RVol 0.3) |
| 13 | **AMZN** | 266.55 | - | **-** | 16 | - | POS +$389.8M | - | 270 | 265 | +$4.1M | +$62k bull / +$0 bear | out (clean 31, ADX 15, RVol 0.5) |
| 14 | **TSLA** | 391.35 | - | **-** | 15 | - | POS +$461.2M | - | 400 | 380 | -$1.8M | +$670k bull / +$0 bear | out (clean 32, ADX 23, RVol 0.3) |
| 15 | **ARM** | 204.33 | - | **-** | 14 | - | POS +$5.5M | - | 200 | 200 | -$1.7M | - | out (clean 32, ADX 22, RVol 0.4) |
| 16 | **DELL** | 378.25 | - | **-** | 12 | - | POS +$2.3M | - | 380 | 380 | -$2.3M | - | out (clean 38, ADX 39, RVol 0.4) |
| 17 | **SMCI** | 30.55 | - | **-** | 12 | - | POS +$13.2M | - | 30 | 30 | -$586k | - | out (clean 33, ADX 31, RVol 0.3) |
| 18 | **BABA** | 101.75 | - | **-** | 12 | - | NEG -$17.2M | 106.44 | 110 | 101 | +$358k | - | out (clean 28, ADX 18, RVol 0.1) |
| 19 | **NFLX** | 64.14 | - | **-** | 10 | - | NEG -$5.6M | 64.53 | 65 | 65 | -$254k | - | out (clean 27, ADX 28, RVol 1.0) |
| 20 | **SMH** | 510.06 | - | **-** | 9 | - | NEG -$31.6M | 513.11 | 500 | 500 | -$2.3M | - | out (clean 32, ADX 33, RVol 0.3) |
| 21 | **PLTR** | 173.05 | - | **-** | 8 | - | POS +$79.4M | - | 170 | 180 | +$1.5M | - | out (clean 29, ADX 20, RVol 0.3) |
| 22 | **HOOD** | 85.29 | - | **-** | 8 | - | POS +$15.6M | - | 85 | 85 | -$620k | - | out (clean 35, ADX 20, RVol 0.3) |
| 23 | **GOOGL** | 294.31 | - | **-** | 7 | - | POS +$98.4M | 289.82 | 300 | 290 | -$813k | - | out (clean 30, ADX 28, RVol 0.4) |
| 24 | **UBER** | 70.89 | - | **-** | 7 | - | POS +$21.6M | 68.29 | 70 | 70 | -$14k | - | out (clean 32, ADX 33, RVol 0.4) |
| 25 | **CRM** | 217.65 | - | **-** | 7 | - | NEG -$10.7M | - | 230 | 220 | -$55k | - | out (clean 29, ADX 10, RVol 0.4) |
| 26 | **COIN** | 137.31 | - | **-** | 5 | - | POS +$24.6M | - | 141 | 135 | +$38k | - | out (clean 29, ADX 25, RVol 0.4) |
| 27 | **ORCL** | 128.88 | - | **-** | 5 | - | POS +$4.5M | 124.21 | 130 | 125 | +$287k | - | out (clean 30, ADX 22, RVol 0.3) |

## Big prints this scan (50)
- **AMD** CALL 550 2026-11-11 (0DTE): 1,000 @ 10.17 = **+$1.0M** BUY | vol 43,781 / OI 918
- **AMD** CALL 555 2026-11-11 (0DTE): 1,000 @ 5.72 = **+$572k** BUY | vol 34,163 / OI 266
- **AMD** CALL 550 2026-11-11 (0DTE): 500 @ 10.35 = **+$518k** BUY | vol 43,781 / OI 918
- **AMD** CALL 550 2026-11-11 (0DTE): 500 @ 10.31 = **+$516k** BUY | vol 43,781 / OI 918
- **AMD** CALL 550 2026-11-11 (0DTE): 500 @ 10.26 = **+$513k** BUY | vol 43,781 / OI 918
- **AMD** CALL 555 2026-11-11 (0DTE): 500 @ 5.85 = **+$292k** BUY | vol 34,163 / OI 266
- **AMD** CALL 555 2026-11-11 (0DTE): 500 @ 5.81 = **+$290k** BUY | vol 34,163 / OI 266
- **AMD** CALL 555 2026-11-11 (0DTE): 500 @ 5.81 = **+$290k** BUY | vol 34,163 / OI 266
- **MU** CALL 810 2026-11-11 (0DTE): 200 @ 8.40 = **+$168k** BUY | vol 35,645 / OI 513
- **QQQ** PUT 694 2026-11-11 (0DTE): 796 @ 1.61 = **+$128k** SELL | vol 215,797 / OI 92
- **MU** PUT 825 2026-11-11 (0DTE): 131 @ 7.85 = **+$103k** SELL | vol 20,963 / OI 75
- **AMD** CALL 560 2026-11-13 (2DTE): 74 @ 13.45 = **+$100k** BUY | vol 6,378 / OI 1,480
- **AMD** PUT 560 2026-11-13 (2DTE): 70 @ 13.70 = **+$96k** SELL | vol 2,206 / OI 104
- **TSLA** CALL 392.5 2026-11-13 (2DTE): 175 @ 5.30 = **+$93k** BUY | vol 11,825 / OI 1,321
- **NVDA** CALL 175 2026-11-11 (0DTE): 1,000 @ 0.85 = **+$85k** BUY | vol 323,503 / OI 3,333

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 750 2026-11-27 (16DTE): 2,258 traded vs OI 2,238
- **SPY** PUT 760 2026-12-11 (30DTE): 514 traded vs OI 250
- **QQQ** PUT 664 2026-11-13 (2DTE): 509 traded vs OI 259
- **QQQ** PUT 690 2026-11-17 (6DTE): 514 traded vs OI 136
- **QQQ** CALL 735 2026-11-30 (19DTE): 1,574 traded vs OI 1,289
- **NVDA** PUT 160 2026-11-13 (2DTE): 17,680 traded vs OI 16,619
- **AMD** PUT 502.5 2026-11-13 (2DTE): 740 traded vs OI 248
- **AMD** PUT 512.5 2026-11-13 (2DTE): 502 traded vs OI 374
- **AMD** CALL 590 2026-11-18 (7DTE): 566 traded vs OI 0
- **META** PUT 580 2026-11-20 (9DTE): 1,010 traded vs OI 0
- **AMZN** PUT 267.5 2026-11-20 (9DTE): 842 traded vs OI 562
- **NFLX** CALL 70 2026-11-13 (2DTE): 528 traded vs OI 0

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
