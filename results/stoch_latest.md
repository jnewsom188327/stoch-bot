# STOCH SCALP PRO - LAST 2 YEARS - 2026-10-20 11:49 ET
Data 2024-10-19 to 2026-10-19, SPY, QQQ, 1m, 2m, 3m, 5m. Same rules as your Stoch Pro v1.2 box (Stoch 14-3-3 hook, LIVE = trend + price switches, entry next open, 3-bar cooldown, 0.02 ATR slippage a side, flat 15:55, one trade at a time). DATA ONLY - no orders. Runtime 1 min.
**ATR** = average result per trade in ATR. **Year 1 / Year 2** = 2024-10-19 to 2025-10-19 | 2025-10-19 to 2026-10-19 (an edge must hold in BOTH). **$ per contract**: **0DTE ATM** and **0DTE 1 out** (1 strike out of the money) and **1DTE ATM** = Black-Scholes estimate at today's prices incl. time decay and $2 costs; **Box $** = your box's own math (delta 0.50 x move - $8/hr theta). **Worst DD** = biggest drop of the running total, 1 contract, every trade taken. Rough: real fills and IV moves differ.

## The answer in 30 seconds
- **YOUR Oct 14 box: stop 3, no target, 40 bars**: 9351 trades | win 45% | **+0.07 ATR** | both years + on 6/8 charts | 0DTE ATM -$18 | 0DTE 1 out -$18 | 1DTE -$7 | box $ -$6 per trade
- **YOUR Oct 15 box: stop 3, TP 5, 40 bars**: 9565 trades | win 46% | **+0.04 ATR** | both years + on 2/8 charts | 0DTE ATM -$19 | 0DTE 1 out -$19 | 1DTE -$8 | box $ -$6 per trade
- **v1.2 default: stop 2, no target, 40 bars**: 10210 trades | win 37% | **+0.04 ATR** | both years + on 4/8 charts | 0DTE ATM -$15 | 0DTE 1 out -$16 | 1DTE -$7 | box $ -$5 per trade
- **COIN FLIP: same entries, random direction (stop 3, 40 bars)**: 9310 trades | win 43% | **-0.08 ATR** | both years + on 0/8 charts | 0DTE ATM -$22 | 0DTE 1 out -$21 | 1DTE -$11 | box $ -$9 per trade
- **Best stop / target for 0DTE (all charts)**: stop 1 ATR / TP 0.5 ATR -> -$4/trade ATM, -0.06 ATR, positive on 0/8 charts
- **Best max hold for 0DTE (stop 3, no target)**: 5 candles -> -$5/trade, -0.05 ATR
- **Per chart (best 0DTE stop/target that held up in both years)**: SPY 1m: nothing made money on 0DTE in both years | SPY 2m: nothing made money on 0DTE in both years | SPY 3m: nothing made money on 0DTE in both years | SPY 5m: nothing made money on 0DTE in both years | QQQ 1m: nothing made money on 0DTE in both years | QQQ 2m: nothing made money on 0DTE in both years | QQQ 3m: nothing made money on 0DTE in both years | QQQ 5m: nothing made money on 0DTE in both years

## Setup levels (stop 3, no target, 40 bars) - all 8 charts
| Setup | Trades | Win % | Avg ATR | Charts + both years | 0DTE ATM $ | 1DTE $ | Edge vs coin flip (+1 ATR first) |
|---|---|---|---|---|---|---|---|
| 1 hook | 20954 | 42% | **-0.05** | 0/8 | -$19 | -$9 | +0.3 |
| 2 +trend | 11581 | 45% | **+0.06** | 4/8 | -$18 | -$7 | +0.3 |
| 3 +VWAP | 8539 | 45% | **+0.02** | 3/8 | -$19 | -$7 | +0.2 |
| 4 +5m | 7807 | 46% | **+0.05** | 4/8 | -$19 | -$7 | +0.3 |
| 5 +price | 6483 | 46% | **+0.07** | 3/8 | -$19 | -$7 | +0.2 |
| Fast 5-3-3 (trend + price) | 11804 | 45% | **+0.02** | 3/8 | -$18 | -$7 | -0.8 |
| Slow 21-5-5 (trend + price) | 4183 | 46% | **+0.09** | 3/8 | -$20 | -$8 | +1.0 |
| LIVE: trend + price (your switches) | 9351 | 45% | **+0.07** | 6/8 | -$18 | -$7 | +0.2 |

## Stop x target on your LIVE fires (40-bar max) - all 8 charts: avg ATR | 0DTE ATM $/trade | win %
| Stop \ Target | 0.5 ATR | 1 ATR | 2 ATR | 3 ATR | 5 ATR | none |
|---|---|---|---|---|---|---|
| 1 ATR | -0.06 / -$4 / 65% ★ | -0.05 / -$5 / 50% | -0.03 / -$6 / 34% | -0.03 / -$9 / 26% | -0.01 / -$10 / 23% | +0.01 / -$10 / 22% |
| 1.5 ATR | -0.06 / -$5 / 74% | -0.05 / -$6 / 59% | -0.04 / -$9 / 43% | -0.04 / -$12 / 35% | -0.01 / -$14 / 31% | +0.01 / -$14 / 30% |
| 2 ATR | -0.07 / -$5 / 79% | -0.04 / -$7 / 66% | -0.03 / -$10 / 50% | -0.02 / -$14 / 42% | +0.00 / -$16 / 38% | +0.04 / -$15 / 37% |
| 3 ATR | -0.06 / -$6 / 85% | -0.04 / -$8 / 74% | +0.00 / -$12 / 59% | +0.00 / -$17 / 51% | +0.04 / -$19 / 46% | +0.07 / -$18 / 45% |

## How long to hold (stop 3, no target) - all 8 charts
| Max hold (candles) | Trades | Win % | Avg ATR | 0DTE ATM $ | 0DTE 1 out $ | 1DTE $ | Charts + both years |
|---|---|---|---|---|---|---|---|
| 5 | 12690 | 48% | **-0.05** | -$5 | -$5 | -$4 | 0/8 |
| 10 | 11881 | 49% | **-0.02** | -$8 | -$8 | -$4 | 1/8 |
| 15 | 11377 | 49% | **-0.02** | -$11 | -$11 | -$6 | 2/8 |
| 20 | 10837 | 49% | **-0.01** | -$13 | -$13 | -$6 | 2/8 |
| 30 | 10031 | 47% | **+0.05** | -$15 | -$15 | -$6 | 4/8 |
| 40 | 9351 | 45% | **+0.07** | -$18 | -$18 | -$7 | 6/8 |
| 48 | 8910 | 44% | **+0.07** | -$20 | -$20 | -$8 | 4/8 |
| 60 | 8392 | 43% | **+0.08** | -$23 | -$23 | -$9 | 3/8 |

## Hold curve - every LIVE fire, no stop: average move after N candles (close / best / worst, ATR, win %)
| Chart | 3 | 6 | 12 | 24 | 48 |
|---|---|---|---|---|---|
| SPY 1m | +0.01 / +0.90 / -0.88 / 49% | +0.01 / +1.27 / -1.26 / 49% | +0.03 / +1.80 / -1.79 / 51% | +0.05 / +2.52 / -2.56 / 51% | +0.19 / +3.68 / -3.58 / 52% |
| SPY 2m | -0.03 / +0.87 / -0.94 / 47% | -0.02 / +1.23 / -1.30 / 49% | -0.01 / +1.73 / -1.83 / 49% | +0.11 / +2.52 / -2.56 / 51% | +0.07 / +3.55 / -3.66 / 51% |
| SPY 3m | -0.04 / +0.86 / -0.95 / 48% | -0.02 / +1.22 / -1.32 / 48% | +0.06 / +1.78 / -1.82 / 52% | +0.01 / +2.50 / -2.57 / 50% | -0.04 / +3.44 / -3.65 / 49% |
| SPY 5m | -0.04 / +0.88 / -0.91 / 47% | -0.04 / +1.22 / -1.27 / 50% | +0.04 / +1.74 / -1.80 / 50% | -0.19 / +2.35 / -2.68 / 50% | -0.28 / +2.99 / -3.54 / 49% |
| QQQ 1m | -0.00 / +0.88 / -0.88 / 49% | -0.00 / +1.25 / -1.26 / 50% | +0.03 / +1.77 / -1.75 / 50% | +0.06 / +2.47 / -2.45 / 51% | +0.08 / +3.56 / -3.51 / 51% |
| QQQ 2m | -0.01 / +0.86 / -0.86 / 49% | -0.01 / +1.21 / -1.22 / 49% | -0.01 / +1.67 / -1.72 / 50% | +0.03 / +2.40 / -2.45 / 52% | +0.10 / +3.37 / -3.39 / 52% |
| QQQ 3m | -0.00 / +0.83 / -0.84 / 50% | +0.00 / +1.17 / -1.20 / 49% | +0.06 / +1.67 / -1.68 / 51% | +0.07 / +2.37 / -2.38 / 51% | +0.03 / +3.19 / -3.22 / 50% |
| QQQ 5m | +0.03 / +0.85 / -0.82 / 51% | +0.10 / +1.20 / -1.11 / 53% | +0.09 / +1.73 / -1.61 / 51% | +0.05 / +2.31 / -2.18 / 51% | +0.15 / +3.01 / -2.75 / 52% |

## Monte Carlo - 10,000 shuffled years, best 0DTE stop/target on each chart (1 contract, ATM)
| Setup | Option | Days sampled from | Trades / yr | Typical year | Bad year (1 in 20) | Good year (1 in 20) | Chance of a losing year | Chance of a losing 3 months | Typical worst drop | Bad-case worst drop | Chance the edge is real |
|---|---|---|---|---|---|---|---|---|---|---|---|
| SPY 1m stop 1.5 / TP 0.5 | 0DTE ATM | 500 days | 1673 | **-$5,060** | -$6,328 | -$3,823 | **100%** | 100% | -$5,116 | -$6,369 | 0% |
| SPY 2m stop 1 / TP 0.5 | 0DTE ATM | 500 days | 843 | **-$3,689** | -$4,788 | -$2,584 | **100%** | 99% | -$3,759 | -$4,828 | 0% |
| SPY 3m stop 1 / TP 0.5 | 0DTE ATM | 500 days | 526 | **-$2,270** | -$3,279 | -$1,198 | **100%** | 96% | -$2,387 | -$3,361 | 0% |
| SPY 5m stop 1 / TP 0.5 | 0DTE ATM | 500 days | 304 | **-$1,789** | -$2,754 | -$870 | **100%** | 95% | -$1,915 | -$2,831 | 0% |
| QQQ 1m stop 1 / TP 1 | 0DTE ATM | 500 days | 1737 | **-$5,810** | -$7,688 | -$3,892 | **100%** | 99% | -$5,962 | -$7,793 | 0% |
| QQQ 2m stop 1 / TP 0.5 | 0DTE ATM | 500 days | 845 | **-$3,644** | -$5,178 | -$2,072 | **100%** | 97% | -$3,780 | -$5,268 | 0% |
| QQQ 3m stop 1 / TP 0.5 | 0DTE ATM | 500 days | 547 | **-$3,388** | -$4,830 | -$1,995 | **100%** | 98% | -$3,516 | -$4,922 | 0% |
| QQQ 5m stop 1 / TP 0.5 | 0DTE ATM | 500 days | 333 | **-$2,644** | -$4,110 | -$1,221 | **100%** | 94% | -$2,819 | -$4,236 | 0% |

## Every chart - your two box setups
| Chart | Setup | Trades/yr | Win % | ATR | PF | Year 1 | Year 2 | 0DTE ATM $ | 0DTE 1 out $ | 1DTE $ | Box $ | 0DTE $/yr | Worst DD 0DTE | Worst DD 1DTE | Losing run | Avg hold |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SPY 1m | YOUR Oct 14 box | 1167 | 45% | **+0.08** | 1.05 | +0.01 | +0.15 | -$8 | -$8 | -$3 | -$3 | -$9,254 | -$19,185 | -$9,996 | 12 | 30 min |
| SPY 1m | YOUR Oct 15 box | 1198 | 46% | **+0.05** | 1.04 | +0.02 | +0.09 | -$7 | -$7 | -$3 | -$3 | -$8,941 | -$18,951 | -$10,193 | 11 | 27 min |
| SPY 1m | COIN FLIP | 1167 | 43% | **-0.08** | 0.94 | -0.04 | -0.12 | -$11 | -$10 | -$6 | -$5 | -$12,378 | -$25,659 | -$14,810 | 12 | 30 min |
| SPY 2m | YOUR Oct 14 box | 579 | 45% | **+0.10** | 1.07 | +0.10 | +0.09 | -$15 | -$15 | -$5 | -$6 | -$8,599 | -$18,027 | -$8,226 | 11 | 58 min |
| SPY 2m | YOUR Oct 15 box | 589 | 45% | **+0.00** | 1.00 | -0.01 | +0.01 | -$17 | -$17 | -$8 | -$7 | -$10,038 | -$20,644 | -$10,090 | 10 | 53 min |
| SPY 2m | COIN FLIP | 577 | 43% | **-0.06** | 0.96 | -0.04 | -0.09 | -$18 | -$18 | -$9 | -$9 | -$10,671 | -$21,629 | -$10,484 | 11 | 58 min |
| SPY 3m | YOUR Oct 14 box | 374 | 44% | **+0.14** | 1.10 | +0.10 | +0.18 | -$23 | -$23 | -$9 | -$8 | -$8,644 | -$19,028 | -$9,890 | 11 | 86 min |
| SPY 3m | YOUR Oct 15 box | 384 | 46% | **+0.04** | 1.03 | -0.01 | +0.10 | -$23 | -$23 | -$9 | -$10 | -$8,728 | -$17,779 | -$8,502 | 11 | 78 min |
| SPY 3m | COIN FLIP | 378 | 42% | **-0.17** | 0.88 | -0.14 | -0.20 | -$30 | -$29 | -$17 | -$15 | -$11,351 | -$23,001 | -$12,999 | 11 | 83 min |
| SPY 5m | YOUR Oct 14 box | 222 | 48% | **+0.07** | 1.06 | +0.11 | +0.03 | -$30 | -$30 | -$7 | -$14 | -$6,622 | -$17,775 | -$8,805 | 7 | 123 min |
| SPY 5m | YOUR Oct 15 box | 225 | 48% | **-0.00** | 1.00 | +0.03 | -0.03 | -$41 | -$41 | -$17 | -$15 | -$9,143 | -$18,224 | -$8,978 | 7 | 114 min |
| SPY 5m | COIN FLIP | 222 | 42% | **-0.35** | 0.74 | -0.11 | -0.56 | -$41 | -$40 | -$18 | -$26 | -$9,072 | -$21,722 | -$13,058 | 14 | 120 min |
| QQQ 1m | YOUR Oct 14 box | 1180 | 45% | **+0.06** | 1.04 | +0.05 | +0.08 | -$10 | -$10 | -$4 | -$3 | -$12,139 | -$24,353 | -$10,762 | 18 | 30 min |
| QQQ 1m | YOUR Oct 15 box | 1217 | 46% | **+0.07** | 1.05 | +0.04 | +0.10 | -$9 | -$9 | -$4 | -$2 | -$11,419 | -$23,133 | -$10,081 | 18 | 27 min |
| QQQ 1m | COIN FLIP | 1166 | 44% | **-0.02** | 0.98 | +0.02 | -0.06 | -$12 | -$12 | -$6 | -$4 | -$14,210 | -$28,758 | -$14,722 | 13 | 30 min |
| QQQ 2m | YOUR Oct 14 box | 577 | 45% | **+0.00** | 1.00 | +0.05 | -0.05 | -$27 | -$27 | -$13 | -$8 | -$15,447 | -$32,502 | -$16,972 | 11 | 59 min |
| QQQ 2m | YOUR Oct 15 box | 586 | 45% | **-0.01** | 0.99 | +0.10 | -0.13 | -$25 | -$25 | -$12 | -$8 | -$14,769 | -$30,836 | -$16,425 | 11 | 55 min |
| QQQ 2m | COIN FLIP | 570 | 45% | **+0.01** | 1.00 | -0.03 | +0.04 | -$26 | -$26 | -$12 | -$8 | -$15,067 | -$31,203 | -$15,179 | 10 | 60 min |
| QQQ 3m | YOUR Oct 14 box | 377 | 46% | **+0.00** | 1.00 | -0.07 | +0.07 | -$38 | -$38 | -$18 | -$12 | -$14,229 | -$29,690 | -$14,897 | 13 | 87 min |
| QQQ 3m | YOUR Oct 15 box | 383 | 47% | **+0.01** | 1.01 | +0.04 | -0.02 | -$35 | -$35 | -$16 | -$10 | -$13,300 | -$27,388 | -$13,650 | 13 | 81 min |
| QQQ 3m | COIN FLIP | 377 | 44% | **-0.13** | 0.90 | +0.02 | -0.28 | -$42 | -$43 | -$22 | -$16 | -$15,975 | -$31,889 | -$16,717 | 10 | 86 min |
| QQQ 5m | YOUR Oct 14 box | 237 | 50% | **+0.21** | 1.20 | +0.38 | +0.06 | -$40 | -$43 | -$7 | -$8 | -$9,561 | -$23,144 | -$9,958 | 9 | 131 min |
| QQQ 5m | YOUR Oct 15 box | 240 | 50% | **+0.10** | 1.09 | +0.25 | -0.04 | -$57 | -$59 | -$22 | -$12 | -$13,666 | -$28,547 | -$12,331 | 9 | 123 min |
| QQQ 5m | COIN FLIP | 235 | 45% | **-0.03** | 0.97 | -0.20 | +0.12 | -$54 | -$54 | -$21 | -$19 | -$12,736 | -$26,423 | -$13,371 | 8 | 129 min |

