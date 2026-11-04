# GEX + FLOW SCAN - Wed Nov 04, 11:40 AM ET
Log only, no orders. Options feed: indicative. Flow = real time (volume change x price). Big prints run 16 min behind (free plan limit on option trades). FIRE = score 45+ with a bias: the bot picks the 0.40-0.80 contract with the most juice for the move and follows its real bid for 60 minutes. Score and fires are being graded, not proven.

## FIRES today (8)
| Time | Ticker | Side | Setup | Contract | Paid (ask) | Bid now | Best | Now | Est | Target |
|---|---|---|---|---|---|---|---|---|---|---|
| 11:38 | **QQQ** | **PUTS** | 1m FAILED POP (R3) | 11/04 686P | 0.80 | 0.67 | -1% (0m) | **-16%** | +26% | 689.6 |
| 11:21 | **QQQ** | **PUTS** | 1m FAILED POP (R3 R4) | 11/04 685P | 0.67 | 0.54 | +66% (7m) | **-19%** | +25% | 690.3 hit |
| 10:20 | **SMCI** | **CALLS** | FLOW SURGE | 11/06 33C | 0.65 | 0.13 | -3% (1m) | **-80%** (done) | +39% | 32.81 |
| 10:20 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/04 284C | 0.49 | 0.17 | +2% (22m) | **-65%** (done) | +131% | 284.74 |
| 10:00 | **AMZN** | **PUTS** | PIN AT CALL WALL (positive gamma) - fade | 11/04 267.5P | 0.68 | 1.54 | +169% (60m) | **+126%** (done) | +258% | 265.7 |
| 09:50 | **UBER** | **CALLS** | FLIP CROSS up into positive gamma | 11/06 71C | 0.60 | 1.56 | +168% (52m) | **+160%** (done) | +50% | 70 hit |
| 09:50 | **IWM** | **CALLS** | RUN: clean trend + negative gamma + flow agrees | 11/04 286C | 0.53 | 0.06 | +2% (1m) | **-89%** (done) | +150% | 287 |
| 09:45 | **UBER** | **PUTS** | FLIP CROSS down into negative gamma | 11/06 67P | 0.63 | 0.10 | -3% (1m) | **-84%** (done) | +27% | 68.03 |

## 1m RULES on SPY / QQQ - loose (2 signals today, last 10)
Whipsaw (R1, +R2 TTM with/turning, +R5 near VWAP, +R6 both) and failed pop (R3, +R4 TTM not turning away). Every signal fires if a 0-1 DTE contract qualifies. Full list: gex_rules.csv.
Last 1m check 11:40:08 ET, last candle SPY 11:39, QQQ 11:39 | no errors
| Candle | Ticker | Rule | Tags | Side | TTM | Result |
|---|---|---|---|---|---|---|
| 11:37 | QQQ | 1m FAILED POP | R3 | PUTS | TURNING away | **FIRE** QQQ261104P00686000 |
| 11:20 | QQQ | 1m FAILED POP | R3 R4 | PUTS | AGAINST you | **FIRE** QQQ261104P00685000 |

## Flow surges NOT fired - price disagreed (34 today, last 5)
- 11:40 SMCI CALLS: under EMA 20 - flow says one way, price says the other
- 11:35 SMCI CALLS: price -0.19 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 11:30 SMCI CALLS: price -0.20 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 11:25 SMCI CALLS: price -0.14 over the last 15 min / under EMA 20 - flow says one way, price says the other
- 11:20 SMCI CALLS: under EMA 20 - flow says one way, price says the other

| # | Ticker | Price | Setup | Bias | Score | Best contract for the move | Gamma | Flip | Call wall | Put wall | Flow today | Big prints 15m | Trend |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **SMCI** | 29.87 | FLOW SURGE | **CALLS** | 59 | 11/06 31.5C @ 0.41 (delta 0.27) = est +57% at 30.74 | NEG -$986k | - | 32 | 30 | +$2.0M | +$53k bull / +$0 bear | SHORT (clean 34, ADX 49, RVol 2.1) |
| 2 | **DELL** | 368.50 | TREND (flow not with it) | **PUTS** | 47 | none: 23 puts 0-7DTE > 0 priced 0.40-0.80 > 0 delta 0.2+ > 0 spread ok > 0 liquid | NEG -$27.3M | - | 400 | 400 | +$2.1M | +$34k bull / +$0 bear | SHORT (clean 33, ADX 42, RVol 3.8) |
| 3 | **GOOGL** | 290.58 | PINNED between the walls (positive gamma) - chop | **-** | 41 | - | POS +$92.2M | 282.92 | 290 | 290 | -$26.0M | +$671k bull / +$0 bear | out (clean 36, ADX 37, RVol 0.7) |
| 4 | **AAPL** | 352.16 | - | **-** | 32 | - | POS +$919.5M | 341.59 | 350 | 350 | -$77.7M | +$291k bull / -$280k bear | out (clean 32, ADX 53, RVol 1.1) |
| 5 | **MU** | 802.24 | - | **-** | 27 | - | NEG -$349.4M | - | 850 | 800 | +$106.9M | +$2.7M bull / -$3.2M bear | out (clean 31, ADX 36, RVol 1.2) |
| 6 | **MSFT** | 555.79 | - | **-** | 25 | - | POS +$969.2M | - | 550 | 535 | -$15.6M | +$159k bull / -$350k bear | out (clean 28, ADX 64, RVol 1.1) |
| 7 | **TSLA** | 383.70 | - | **-** | 24 | - | NEG -$112.1M | 391.78 | 400 | 380 | -$63.1M | +$214k bull / -$1.3M bear | out (clean 30, ADX 24, RVol 1.7) |
| 8 | **AMZN** | 266.20 | - | **-** | 24 | - | POS +$516.8M | - | 270 | 250 | -$17.5M | +$182k bull / -$26k bear | out (clean 35, ADX 40, RVol 1.2) |
| 9 | **ORCL** | 124.51 | - | **-** | 24 | - | NEG -$35.3M | - | 130 | 125 | +$2.6M | +$29k bull / +$0 bear | out (clean 35, ADX 16, RVol 3.3) |
| 10 | **UBER** | 71.65 | - | **-** | 24 | - | POS +$12.0M | 68.25 | 70 | 70 | -$1.4M | - | out (clean 31, ADX 57, RVol 1.6) |
| 11 | **ARM** | 193.93 | - | **-** | 23 | - | NEG -$6.7M | - | 200 | 200 | +$836k | - | out (clean 26, ADX 38, RVol 1.0) |
| 12 | **IWM** | 282.88 | - | **-** | 21 | - | NEG -$576.8M | 284.62 | 285 | 270 | +$13.8M | +$55k bull / +$0 bear | out (clean 34, ADX 15, RVol 1.1) |
| 13 | **NVDA** | 202.12 | - | **-** | 21 | - | NEG -$89.6M | 203.77 | 210 | 200 | +$2.1M | +$773k bull / -$212k bear | out (clean 30, ADX 39, RVol 1.6) |
| 14 | **AMD** | 482.71 | - | **-** | 21 | - | NEG -$96.4M | - | 500 | 440 | +$40.5M | +$539k bull / -$263k bear | out (clean 32, ADX 19, RVol 0.8) |
| 15 | **MSTR** | 143.70 | - | **-** | 20 | - | POS +$123.4M | - | 135 | 150 | +$548k | +$306k bull / -$39k bear | out (clean 31, ADX 41, RVol 0.8) |
| 16 | **BABA** | 106.58 | - | **-** | 20 | - | POS +$16.2M | - | 110 | 110 | -$838k | - | out (clean 36, ADX 54, RVol 2.2) |
| 17 | **SPY** | 765.82 | - | **-** | 19 | - | NEG -$4.1B | 770.02 | 770 | 750 | -$60.5M | +$1.5M bull / -$1.1M bear | out (clean 32, ADX 28, RVol 1.1) |
| 18 | **META** | 630.76 | - | **-** | 19 | - | POS +$142.2M | 619.64 | 650 | 625 | +$7.3M | +$0 bull / -$82k bear | out (clean 30, ADX 29, RVol 0.8) |
| 19 | **PLTR** | 170.18 | - | **-** | 18 | - | NEG -$49.9M | - | 165 | 170 | -$646k | +$511k bull / +$0 bear | out (clean 26, ADX 21, RVol 1.8) |
| 20 | **QQQ** | 692.21 | - | **-** | 17 | - | NEG -$4.9B | 720.89 | 700 | 680 | -$65.6M | +$2.4M bull / -$964k bear | out (clean 31, ADX 22, RVol 0.9) |
| 21 | **NFLX** | 66.25 | - | **-** | 17 | - | POS +$18.9M | - | 65 | 65 | -$2.2M | - | out (clean 31, ADX 63, RVol 0.7) |
| 22 | **HOOD** | 87.14 | - | **-** | 16 | - | POS +$1.7M | 85.47 | 90 | 90 | -$879k | +$28k bull / +$0 bear | out (clean 28, ADX 13, RVol 0.7) |
| 23 | **SMH** | 503.36 | - | **-** | 15 | - | NEG -$527.1M | - | 532.5 | 500 | +$3.8M | - | out (clean 32, ADX 38, RVol 1.0) |
| 24 | **CRM** | 227.51 | - | **-** | 14 | - | NEG -$9.8M | 238.95 | 240 | 220 | -$193k | - | out (clean 32, ADX 39, RVol 0.6) |
| 25 | **SHOP** | 151.93 | - | **-** | 14 | - | NEG -$5.1M | - | 160 | 150 | -$309k | - | out (clean 34, ADX 30, RVol 0.4) |
| 26 | **AVGO** | 325.59 | - | **-** | 12 | - | NEG -$98.3M | - | 340 | 320 | +$2.9M | - | out (clean 30, ADX 34, RVol 1.1) |
| 27 | **COIN** | 151.63 | - | **-** | 12 | - | POS +$28.2M | - | 148 | 150 | -$1.3M | - | out (clean 30, ADX 16, RVol 0.5) |

## Big prints this scan (97)
- **QQQ** PUT 705 2026-11-06 (2DTE): 458 @ 15.20 = **+$696k** BUY | vol 1,492 / OI 5,241
- **SPY** PUT 770 2026-11-05 (1DTE): 862 @ 6.00 = **+$517k** BUY | vol 11,061 / OI 1,690
- **SPY** PUT 770 2026-11-05 (1DTE): 500 @ 5.80 = **+$290k** BUY | vol 11,061 / OI 1,690
- **SPY** PUT 770 2026-11-05 (1DTE): 500 @ 5.80 = **+$290k** BUY | vol 11,061 / OI 1,690
- **QQQ** PUT 693 2026-11-09 (5DTE): 202 @ 7.95 = **+$161k** SELL | vol 1,055 / OI 0
- **QQQ** PUT 695 2026-11-05 (1DTE): 230 @ 6.65 = **+$153k** BUY | vol 11,028 / OI 1,805
- **GOOGL** PUT 290 2026-11-06 (2DTE): 434 @ 3.47 = **+$151k** MID | vol 4,172 / OI 3,541
- **NVDA** PUT 200 2026-11-09 (5DTE): 466 @ 3.20 = **+$149k** BUY | vol 4,372 / OI 910
- **MU** PUT 785 2026-11-04 (0DTE): 567 @ 2.16 = **+$122k** MID | vol 15,302 / OI 365
- **QQQ** CALL 692 2026-11-04 (0DTE): 441 @ 2.72 = **+$120k** BUY | vol 41,726 / OI 681
- **MSFT** CALL 532.5 2026-11-11 (7DTE): 51 @ 23.25 = **+$119k** SELL | vol 85 / OI 7
- **MSFT** CALL 530 2026-11-04 (0DTE): 51 @ 22.99 = **+$117k** SELL | vol 1,139 / OI 1,850
- **QQQ** CALL 690 2026-11-05 (1DTE): 200 @ 5.75 = **+$115k** SELL | vol 4,301 / OI 925
- **MU** PUT 785 2026-11-04 (0DTE): 535 @ 2.00 = **+$107k** SELL | vol 15,302 / OI 365
- **TSLA** PUT 387.5 2026-11-04 (0DTE): 200 @ 5.27 = **+$105k** BUY | vol 26,766 / OI 703

## New unusual volume (traded more than open interest, 500+)
- **SPY** PUT 735 2026-11-04 (0DTE): 6,076 traded vs OI 3,952
- **SPY** CALL 787 2026-11-06 (2DTE): 1,734 traded vs OI 1,722
- **SPY** PUT 759 2026-11-09 (5DTE): 504 traded vs OI 0
- **SPY** PUT 735 2026-11-13 (9DTE): 2,617 traded vs OI 2,522
- **SPY** PUT 760 2026-11-10 (6DTE): 751 traded vs OI 739
- **SPY** CALL 780 2026-11-13 (9DTE): 8,632 traded vs OI 8,074
- **SPY** PUT 750 2026-11-13 (9DTE): 6,363 traded vs OI 4,728
- **SPY** PUT 750 2026-11-11 (7DTE): 3,630 traded vs OI 3,330
- **QQQ** CALL 694 2026-11-10 (6DTE): 500 traded vs OI 0
- **QQQ** CALL 717 2026-11-05 (1DTE): 506 traded vs OI 0
- **QQQ** PUT 696 2026-11-06 (2DTE): 1,727 traded vs OI 1,704
- **QQQ** CALL 691 2026-11-09 (5DTE): 504 traded vs OI 0
- **QQQ** CALL 710 2026-11-06 (2DTE): 12,583 traded vs OI 12,515
- **QQQ** PUT 676 2026-11-11 (7DTE): 798 traded vs OI 0
- **QQQ** PUT 691 2026-11-13 (9DTE): 2,336 traded vs OI 967

**How to read it:** POS gamma = dealers pin price (fade the walls). NEG gamma = dealers chase (moves run). Flip = where gamma turns from one to the other. Call wall / put wall = the strikes with the most call / put gamma (magnets and lids). Flow today = bullish $ (calls bought + puts sold) minus bearish $ (puts bought + calls sold), near the money, 0-7 DTE. BUY / SELL is a guess from where the print hit the current quote.
