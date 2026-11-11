# GEX + FLOW SCAN - Wed Nov 11, 02:30 PM ET
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
Last 1m check 14:30:08 ET, last candle SPY 14:29, QQQ 14:29 | no errors
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
| 1 | **META** | 635.21 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 40 | none: 204 calls 0-7DTE > 10 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid (84 contracts' greeks worked out here) | POS +$181.5M | 627.02 | 650 | 635 | +$5.2M | +$695k bull / +$0 bear | out (clean 30, ADX 39, RVol 0.8) |
| 2 | **MSFT** | 520.71 | PIN AT PUT WALL (positive gamma) - bounce | **CALLS** | 36 | none: 166 calls 0-7DTE > 8 priced 0.40-0.80 > 1 delta 0.2+ > 1 spread ok > 1 liquid > best one only +5% at the target (needs +20%) (69 contracts' greeks worked out here) | POS +$27.9M | 517.81 | 535 | 520 | +$13.5M | +$148k bull / -$52k bear | out (clean 32, ADX 16, RVol 0.4) |
| 3 | **IWM** | 283.07 | PIN AT CALL WALL (positive gamma) - fade | **PUTS** | 27 | none: 340 puts 0-7DTE > 14 priced 0.40-0.80 > 5 delta 0.2+ > 5 spread ok > 5 liquid > best one only +4% at the target (needs +20%) (163 contracts' greeks worked out here) | POS +$131.3M | 282.85 | 283 | 270 | -$5.5M | - | out (clean 35, ADX 29, RVol 0.4) |
| 4 | **AMD** | 561.42 | - | **-** | 27 | - | POS +$140.6M | - | 550 | 550 | -$104.3M | +$2.4M bull / -$445k bear | out (clean 34, ADX 48, RVol 0.7) |
| 5 | **MU** | 818.23 | - | **-** | 25 | - | POS +$158.6M | - | 800 | 800 | -$201.1M | +$4.7M bull / -$782k bear | out (clean 34, ADX 36, RVol 0.7) |
| 6 | **SPY** | 760.35 | - | **-** | 21 | - | NEG -$1.2B | 761.66 | 760 | 750 | -$108.7M | +$15.6M bull / -$136k bear | out (clean 33, ADX 40, RVol 0.5) |
| 7 | **QQQ** | 692.39 | - | **-** | 21 | - | POS +$538.9M | 689.88 | 700 | 680 | -$137.8M | +$4.1M bull / -$100k bear | out (clean 32, ADX 36, RVol 0.6) |
| 8 | **AVGO** | 349.06 | - | **-** | 21 | - | POS +$101.4M | - | 350 | 350 | +$8.0M | +$750k bull / +$0 bear | out (clean 36, ADX 29, RVol 0.6) |
| 9 | **SMH** | 510.99 | - | **-** | 20 | - | NEG -$35.9M | - | 500 | 500 | -$2.9M | +$610k bull / +$0 bear | out (clean 31, ADX 36, RVol 0.4) |
| 10 | **GOOGL** | 293.94 | - | **-** | 19 | - | POS +$93.1M | 290.6 | 300 | 290 | -$601k | +$61k bull / -$56k bear | out (clean 30, ADX 40, RVol 0.4) |
| 11 | **NVDA** | 175.37 | - | **-** | 18 | - | NEG -$179.1M | - | 180 | 175 | -$20.6M | +$3.8M bull / +$0 bear | out (clean 34, ADX 29, RVol 0.7) |
| 12 | **SHOP** | 149.39 | - | **-** | 18 | - | POS +$4.1M | 145.01 | 150 | 140 | -$476k | - | out (clean 33, ADX 19, RVol 0.3) |
| 13 | **AAPL** | 354.82 | PINNED between the walls (positive gamma) - chop | **-** | 17 | - | POS +$2.3B | 341.12 | 355 | 355 | -$423k | - | out (clean 28, ADX 30, RVol 0.3) |
| 14 | **MSTR** | 122.15 | - | **-** | 17 | - | NEG -$5.7M | 123.56 | 133 | 120 | +$1.3M | +$0 bull / -$55k bear | out (clean 28, ADX 20, RVol 0.4) |
| 15 | **ORCL** | 129.34 | - | **-** | 17 | - | POS +$4.3M | 124.35 | 130 | 125 | +$129k | +$0 bull / -$203k bear | out (clean 30, ADX 33, RVol 0.3) |
| 16 | **AMZN** | 266.55 | - | **-** | 16 | - | POS +$407.7M | - | 270 | 265 | +$3.4M | +$0 bull / -$480k bear | out (clean 31, ADX 15, RVol 0.5) |
| 17 | **ARM** | 205.06 | - | **-** | 16 | - | POS +$5.3M | - | 200 | 200 | -$1.7M | - | out (clean 31, ADX 34, RVol 0.5) |
| 18 | **TSLA** | 392.69 | - | **-** | 15 | - | POS +$410.1M | - | 400 | 380 | -$5.0M | +$2.8M bull / -$93k bear | out (clean 32, ADX 20, RVol 0.3) |
| 19 | **DELL** | 378.72 | - | **-** | 13 | - | POS +$2.4M | - | 380 | 380 | -$2.6M | - | out (clean 37, ADX 42, RVol 0.6) |
| 20 | **SMCI** | 30.72 | - | **-** | 13 | - | POS +$13.2M | - | 30 | 30 | -$596k | - | out (clean 33, ADX 32, RVol 0.6) |
| 21 | **BABA** | 101.67 | - | **-** | 13 | - | NEG -$16.7M | 106.44 | 110 | 101 | +$371k | - | out (clean 29, ADX 16, RVol 0.3) |
| 22 | **PLTR** | 173.17 | - | **-** | 10 | - | POS +$78.8M | - | 170 | 180 | +$1.6M | - | out (clean 29, ADX 28, RVol 0.3) |
| 23 | **HOOD** | 85.39 | - | **-** | 10 | - | POS +$15.9M | - | 85 | 85 | -$638k | - | out (clean 34, ADX 29, RVol 0.5) |
| 24 | **UBER** | 70.98 | - | **-** | 10 | - | POS +$21.2M | 68.22 | 70 | 70 | -$17k | - | out (clean 32, ADX 44, RVol 0.6) |
| 25 | **NFLX** | 64.06 | - | **-** | 9 | - | NEG -$4.8M | 64.46 | 65 | 65 | -$256k | - | out (clean 28, ADX 18, RVol 0.9) |
| 26 | **CRM** | 217.37 | - | **-** | 7 | - | NEG -$11.3M | - | 230 | 220 | -$57k | - | out (clean 30, ADX 14, RVol 0.3) |
| 27 | **COIN** | 137.37 | - | **-** | 5 | - | POS +$25.4M | - | 141 | 135 | +$88k | - | out (clean 29, ADX 22, RVol 0.4) |

## Big prints this scan (121)
- **SPY** PUT 763 2026-11-16 (5DTE): 2,400 @ 5.08 = **+$1.2M** SELL | vol 20,202 / OI 216
- **SPY** PUT 763 2026-11-13 (2DTE): 2,400 @ 4.23 = **+$1.0M** SELL | vol 40,589 / OI 954
- **SPY** PUT 763 2026-11-16 (5DTE): 1,600 @ 5.13 = **+$821k** SELL | vol 20,202 / OI 216
- **SPY** PUT 763 2026-11-16 (5DTE): 1,434 @ 5.13 = **+$736k** SELL | vol 20,202 / OI 216
- **SPY** PUT 763 2026-11-16 (5DTE): 1,340 @ 5.13 = **+$687k** SELL | vol 20,202 / OI 216
- **SPY** PUT 763 2026-11-13 (2DTE): 1,600 @ 4.28 = **+$685k** SELL | vol 40,589 / OI 954
- **SPY** PUT 763 2026-11-13 (2DTE): 1,434 @ 4.28 = **+$614k** SELL | vol 40,589 / OI 954
- **SPY** PUT 763 2026-11-13 (2DTE): 1,340 @ 4.28 = **+$574k** SELL | vol 40,589 / OI 954
- **SPY** PUT 763 2026-11-16 (5DTE): 960 @ 5.13 = **+$492k** SELL | vol 20,202 / OI 216
- **SPY** PUT 763 2026-11-13 (2DTE): 960 @ 4.28 = **+$411k** SELL | vol 40,589 / OI 954
- **QQQ** PUT 692 2026-11-12 (1DTE): 995 @ 3.27 = **+$325k** SELL | vol 15,600 / OI 73
- **AMD** PUT 550 2026-11-13 (2DTE): 317 @ 8.98 = **+$285k** BUY | vol 3,188 / OI 154
- **QQQ** PUT 698 2026-11-11 (0DTE): 500 @ 5.43 = **+$272k** SELL | vol 5,209 / OI 115
- **NVDA** CALL 182.5 2026-11-13 (2DTE): 2,250 @ 1.11 = **+$250k** BUY | vol 33,336 / OI 4,853
- **MU** PUT 825 2026-11-11 (0DTE): 300 @ 8.30 = **+$249k** BUY | vol 19,100 / OI 75

## New unusual volume (traded more than open interest, 500+)
- **SPY** CALL 763 2026-11-20 (9DTE): 1,721 traded vs OI 1,698
- **SPY** PUT 735 2026-11-27 (16DTE): 1,914 traded vs OI 1,880
- **QQQ** CALL 713 2026-11-13 (2DTE): 694 traded vs OI 688
- **QQQ** PUT 693 2026-11-16 (5DTE): 594 traded vs OI 36
- **QQQ** CALL 715 2026-11-13 (2DTE): 2,080 traded vs OI 1,834
- **QQQ** PUT 692 2026-11-16 (5DTE): 573 traded vs OI 109
- **IWM** CALL 282 2026-11-13 (2DTE): 1,169 traded vs OI 1,150
- **IWM** PUT 279 2026-11-20 (9DTE): 10,956 traded vs OI 6,802
- **SMH** PUT 502.5 2026-11-11 (0DTE): 510 traded vs OI 174
- **SMH** CALL 522.5 2026-11-11 (0DTE): 503 traded vs OI 40
- **NVDA** CALL 180 2026-11-27 (16DTE): 3,025 traded vs OI 2,969
- **NVDA** CALL 185 2026-11-18 (7DTE): 3,467 traded vs OI 3,457
- **TSLA** PUT 387.5 2026-11-18 (7DTE): 724 traded vs OI 15
- **TSLA** CALL 397.5 2026-11-16 (5DTE): 510 traded vs OI 167
- **TSLA** PUT 392.5 2026-11-18 (7DTE): 2,529 traded vs OI 8

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
