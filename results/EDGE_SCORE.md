# SPY 0DTE Edge score backtest - 2025-11-06 to 2026-11-11

255 trading days, SPY 1-minute bars (sip), every minute 9:45-2:30 scored with the dashboard's chart factors (61 of its 100 points; contract charts, gamma and contract math are not in this test). Entry = next minute's open. DATA ONLY.

## 1. Every minute: what SPY did next, by score

| Score | Minutes | Share | SPY +5m | Up % | SPY +10m | Up % | SPY +20m | Up % |
|---|---|---|---|---|---|---|---|---|
| A calls 62+ | 10,760 | 15% | -0.009 | 50% | +0.007 | 51% | +0.004 | 52% |
| B calls 55-62 | 14,144 | 19% | +0.008 | 50% | +0.004 | 51% | -0.011 | 51% |
| C neutral 45-55 | 23,175 | 32% | +0.007 | 50% | +0.007 | 51% | +0.010 | 51% |
| D puts 55-62 | 13,637 | 19% | -0.007 | 50% | -0.006 | 50% | +0.006 | 51% |
| E puts 62+ | 11,204 | 15% | -0.003 | 50% | -0.011 | 50% | -0.001 | 51% |
| ALL MINUTES (baseline) | 72,920 | 100% | +0.001 | 50% | +0.001 | 51% | +0.002 | 51% |

The score works if SPY +$ falls steadily from the top row to the bottom row, and the top and bottom rows beat the baseline.

## 2. Fresh readings only (first minute in a bucket), SPY move in the score's direction

| Score | Fires | Per day | +5m | Right % | +10m | Right % | +20m | Right % | +10m 1st half | +10m 2nd half |
|---|---|---|---|---|---|---|---|---|---|---|
| A calls 62+ | 1,464 | 5.7 | -0.001 | 50% | -0.002 | 52% | +0.039 | 53% | +0.023 | -0.027 |
| B calls 55-62 | 1,981 | 7.8 | +0.022 | 50% | +0.036 | 52% | +0.062 | 52% | +0.057 | +0.015 |
| D puts 55-62 | 2,003 | 7.9 | +0.006 | 49% | +0.030 | 50% | +0.009 | 48% | +0.010 | +0.051 |
| E puts 62+ | 1,530 | 6.0 | -0.009 | 47% | +0.005 | 49% | +0.005 | 49% | -0.009 | +0.019 |

An edge is only real if both halves are positive.

## 3. Real 1-OTM 0DTE option prices, last 120 trading days

Alpaca 1-minute option bars: 10,690 of 10,692 entries had a price. Buy at the next minute's open, sell at the close 5 / 10 / 20 minutes later. 'After slip' takes 2 cents off the exit. 'Favored' = the call when the score says calls, the put when it says puts.

| Score | Fires | Favored +5m | Win % | Favored +10m | Win % | After slip | Favored +20m | Win % | Other side +10m |
|---|---|---|---|---|---|---|---|---|---|
| A calls 62+ | 686 | -0.6% | 45% | -2.2% | 39% | -5.0% | -2.4% | 39% | +2.5% |
| B calls 55-62 | 924 | -0.9% | 42% | -0.9% | 41% | -3.7% | -0.7% | 41% | +0.2% |
| D puts 55-62 | 930 | +0.4% | 43% | +1.4% | 45% | -1.3% | +0.3% | 40% | -1.9% |
| E puts 62+ | 713 | +0.1% | 44% | -0.0% | 43% | -2.6% | +0.0% | 37% | -0.3% |
| Baseline: any call, every 15 min | 2,400 | -0.8% | 42% | -1.7% | 41% | -4.6% | -1.7% | 40% | - |
| Baseline: any put, every 15 min | 2,400 | +1.0% | 46% | +1.1% | 44% | -1.6% | +1.0% | 41% | - |

The score earns its place only if the favored side beats both baselines after slip. Averages on cheap options are pulled up by a few big winners, so read Win % too.

