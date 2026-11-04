# GEX + FLOW SCAN - Wed Nov 04, 02:40 PM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (10)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 13:05 | **AAPL** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/04 352.5P | 0.58 | 0.89 | +76% (29m) | **+53%** (done) | +57% | 352.38 hit |
| 12:50 | **AMZN** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/04 267.5P | 0.40 | 0.76 | +100% (55m) | **+90%** (done) | +109% | 267.48 |
| 11:38 | **QQQ** | **PUTS** | 1m FAILED POP (R3) | 11/04 686P | 0.80 | 0.15 | -1% (0m) | **-81%** (done) | +26% | 689.6 |
| 11:21 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/04 685P | 0.67 | 0.12 | +66% (7m) | **-82%** (done) | +25% | 690.3 hit |
| 10:20 | **SMCI** | **CALLS** | FLOW SURGE | 11/06 33C | 0.65 | 0.13 | -3% (1m) | **-80%** (done) | +39% | 32.81 |
| 10:20 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/04 284C | 0.49 | 0.17 | +2% (22m) | **-65%** (done) | +131% | 284.74 |
| 10:00 | **AMZN** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/04 267.5P | 0.68 | 1.54 | +169% (60m) | **+126%** (done) | +258% | 265.7 |
| 09:50 | **UBER** | **CALLS** | FLIP CROSS up into positive gamma | 11/06 71C | 0.60 | 1.56 | +168% (52m) | **+160%** (done) | +50% | 70 hit |
| 09:50 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/04 286C | 0.53 | 0.06 | +2% (1m) | **-89%** (done) | +150% | 287 |
| 09:45 | **UBER** | **PUTS** | FLIP CROSS down into negative gamma | 11/06 67P | 0.63 | 0.10 | -3% (1m) | **-84%** (done) | +27% | 68.03 |

## 1m RULES on SPY / QQQ - loose (3 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 14:40:08 ET, last candle SPY 14:39, QQQ 14:39 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 14:01 | QQQ | 1m WHIPSAW | R1 | PUTS | TURNING away | no contract: 82 puts 0-1DTE > 8 priced 0.40-0.80 > 2 delta 0.15+ > 2 spread ok > 2 liquid  |
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
| 1 | **SMH** | 503.91 | FLOW SURGE | **CALLS** | 35 | 11/04 507.5C @ 0.63 (delta 0.22) = est +24% at 507.5 | NEG -$588.7M | - | 532.5 | 500 | +$22.5M | +$94k bull / +$0 bear | out (clean 33, ADX 16, RVol 0.4) |
| 2 | **SMCI** | 29.77 | TREND (flow not with it) | **PUTS** | 31 | none: 12 puts 0-7DTE > 2 priced 0.40-0.80 > 2 delta 0.2+ > 1 spread ok > 1 liquid > best one only +9% at the target (needs +20%) | NEG -$971k | - | 32 | 30 | +$2.0M | - | SHORT (clean 34, ADX 23, RVol 0.7) |
| 3 | **ORCL** | 125.40 | - | **-** | 24 | - | NEG -$33.1M | - | 130 | 125 | +$3.6M | +$131k bull / +$0 bear | out (clean 34, ADX 23, RVol 2.0) |
| 4 | **AAPL** | 352.62 | - | **-** | 23 | - | POS +$1.0B | 342.17 | 355 | 350 | -$77.1M | +$1.1M bull / -$799k bear | out (clean 32, ADX 16, RVol 0.6) |
| 5 | **ARM** | 191.73 | - | **-** | 22 | - | NEG -$7.3M | - | 200 | 200 | +$1.1M | +$353k bull / +$0 bear | out (clean 26, ADX 29, RVol 0.7) |
| 6 | **MU** | 802.96 | - | **-** | 20 | - | NEG -$398.7M | - | 850 | 800 | +$113.0M | +$3.1M bull / -$341k bear | out (clean 31, ADX 18, RVol 0.6) |
| 7 | **MSTR** | 143.97 | - | **-** | 20 | - | POS +$129.8M | - | 135 | 150 | -$9.5M | +$25k bull / +$0 bear | out (clean 31, ADX 21, RVol 0.3) |
| 8 | **TSLA** | 389.15 | - | **-** | 19 | - | NEG -$58.9M | 391.51 | 400 | 390 | -$79.9M | +$1.1M bull / -$118k bear | out (clean 31, ADX 17, RVol 0.5) |
| 9 | **AMD** | 480.49 | - | **-** | 19 | - | NEG -$98.7M | - | 500 | 480 | +$51.0M | +$416k bull / +$0 bear | out (clean 32, ADX 16, RVol 0.4) |
| 10 | **META** | 628.64 | - | **-** | 19 | - | POS +$150.8M | 619.7 | 650 | 625 | +$11.9M | +$481k bull / -$114k bear | out (clean 32, ADX 31, RVol 0.8) |
| 11 | **MSFT** | 556.07 | - | **-** | 19 | - | POS +$1.0B | - | 550 | 535 | -$16.9M | +$51k bull / +$0 bear | out (clean 29, ADX 18, RVol 0.9) |
| 12 | **AMZN** | 268.16 | - | **-** | 18 | - | POS +$562.9M | - | 270 | 250 | -$17.4M | +$66k bull / +$0 bear | out (clean 36, ADX 19, RVol 0.5) |
| 13 | **AVGO** | 326.86 | - | **-** | 17 | - | NEG -$104.7M | - | 340 | 330 | +$5.6M | +$201k bull / +$0 bear | out (clean 30, ADX 16, RVol 0.4) |
| 14 | **SPY** | 767.98 | - | **-** | 16 | - | NEG -$2.8B | 769.62 | 770 | 767 | -$91.3M | +$1.9M bull / +$0 bear | out (clean 32, ADX 15, RVol 0.6) |
| 15 | **BABA** | 106.42 | - | **-** | 16 | - | POS +$16.8M | - | 110 | 110 | -$299k | +$73k bull / +$0 bear | out (clean 36, ADX 18, RVol 0.5) |
| 16 | **QQQ** | 693.30 | - | **-** | 15 | - | NEG -$5.0B | 718.17 | 700 | 680 | -$97.8M | +$3.0M bull / +$0 bear | out (clean 32, ADX 12, RVol 0.4) |
| 17 | **IWM** | 283.80 | - | **-** | 15 | - | NEG -$189.0M | 284.27 | 285 | 270 | +$9.0M | +$282k bull / +$0 bear | out (clean 34, ADX 9, RVol 0.5) |
| 18 | **NVDA** | 203.71 | - | **-** | 14 | - | NEG -$44.3M | 204.19 | 210 | 200 | +$3.8M | +$725k bull / -$73k bear | out (clean 30, ADX 11, RVol 0.7) |
| 19 | **PLTR** | 170.87 | - | **-** | 14 | - | NEG -$51.8M | - | 165 | 170 | -$978k | +$269k bull / +$0 bear | out (clean 26, ADX 11, RVol 0.5) |
| 20 | **GOOGL** | 291.58 | - | **-** | 12 | - | POS +$107.2M | 283.05 | 290 | 290 | -$26.6M | - | out (clean 36, ADX 13, RVol 0.4) |
| 21 | **NFLX** | 66.18 | - | **-** | 11 | - | POS +$20.4M | 62.41 | 65 | 65 | -$2.0M | - | out (clean 31, ADX 18, RVol 0.7) |
| 22 | **UBER** | 70.96 | - | **-** | 10 | - | POS +$10.5M | 68.63 | 70 | 65 | -$1.0M | - | out (clean 31, ADX 13, RVol 0.8) |
| 23 | **SHOP** | 151.58 | - | **-** | 10 | - | NEG -$5.9M | - | 160 | 150 | -$359k | - | out (clean 32, ADX 10, RVol 0.5) |
| 24 | **COIN** | 151.61 | - | **-** | 9 | - | POS +$30.6M | - | 148 | 150 | -$1.2M | - | out (clean 31, ADX 12, RVol 0.2) |
| 25 | **DELL** | 369.62 | - | **-** | 7 | - | NEG -$28.3M | - | 400 | 400 | +$1.2M | - | out (clean 33, ADX 18, RVol 0.8) |
| 26 | **CRM** | 226.11 | - | **-** | 6 | - | NEG -$13.0M | - | 240 | 220 | -$132k | - | out (clean 34, ADX 13, RVol 0.6) |
| 27 | **HOOD** | 87.81 | - | **-** | 4 | - | POS +$2.8M | 84.57 | 90 | 90 | -$831k | - | out (clean 29, ADX 12, RVol 0.5) |

## Big prints this scan (36)
- **AAPL** CALL 362.5 2026-11-09 (5DTE): 9,997 @ 0.91 = **+$910k** BUY | vol 12,370 / OI 74
- **SPY** PUT 770 2026-11-05 (1DTE): 1,524 @ 3.27 = **+$498k** SELL | vol 29,759 / OI 1,690
- **QQQ** CALL 690 2026-11-04 (0DTE): 395 @ 4.50 = **+$178k** BUY | vol 43,339 / OI 3,346
- **TSLA** PUT 392.5 2026-11-06 (2DTE): 228 @ 7.50 = **+$171k** SELL | vol 2,064 / OI 3,501
- **PLTR** CALL 172.5 2026-11-06 (2DTE): 427 @ 3.10 = **+$132k** BUY | vol 9,414 / OI 460
- **QQQ** CALL 685 2026-11-04 (0DTE): 136 @ 9.11 = **+$124k** BUY | vol 5,274 / OI 3,466
- **MU** PUT 805 2026-11-09 (5DTE): 50 @ 24.12 = **+$121k** BUY | vol 1,041 / OI 219
- **NVDA** CALL 202.5 2026-11-06 (2DTE): 250 @ 3.90 = **+$98k** BUY | vol 8,614 / OI 1,974
- **PLTR** CALL 172.5 2026-11-06 (2DTE): 197 @ 3.10 = **+$61k** BUY | vol 9,414 / OI 460
- **TSLA** CALL 405 2026-11-09 (5DTE): 200 @ 2.90 = **+$58k** BUY | vol 1,439 / OI 732
- **PLTR** CALL 175 2026-11-06 (2DTE): 244 @ 2.08 = **+$51k** BUY | vol 12,113 / OI 862
- **META** PUT 630 2026-11-06 (2DTE): 50 @ 10.10 = **+$50k** BUY | vol 3,101 / OI 686
- **MU** PUT 805 2026-11-09 (5DTE): 20 @ 23.02 = **+$46k** SELL | vol 1,041 / OI 219
- **NVDA** CALL 202.5 2026-11-04 (0DTE): 300 @ 1.50 = **+$45k** BUY | vol 65,296 / OI 1,808
- **MU** PUT 800 2026-11-09 (5DTE): 20 @ 21.82 = **+$44k** BUY | vol 1,176 / OI 321

## New unusual volume (traded more than open interest, 500+)
- **QQQ** PUT 694 2026-11-13 (9DTE): 527 traded vs OI 226
- **QQQ** CALL 700 2026-11-12 (8DTE): 571 traded vs OI 496
- **QQQ** CALL 725 2026-11-11 (7DTE): 665 traded vs OI 647
- **QQQ** CALL 725 2026-11-12 (8DTE): 503 traded vs OI 437
- **SMH** CALL 510 2026-11-06 (2DTE): 509 traded vs OI 146
- **NVDA** PUT 205 2026-11-06 (2DTE): 10,242 traded vs OI 10,223
- **TSLA** CALL 380 2026-11-13 (9DTE): 1,604 traded vs OI 1,600
- **AAPL** CALL 325 2026-11-04 (0DTE): 523 traded vs OI 128
- **META** CALL 647.5 2026-11-06 (2DTE): 690 traded vs OI 612
- **MU** CALL 840 2026-11-13 (9DTE): 502 traded vs OI 274
- **ARM** CALL 197.5 2026-11-06 (2DTE): 500 traded vs OI 103
- **UBER** CALL 72 2026-11-20 (16DTE): 1,401 traded vs OI 1,389
- **BABA** PUT 107 2026-11-06 (2DTE): 501 traded vs OI 144

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
