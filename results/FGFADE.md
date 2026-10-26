# Fear-greed fade

Data only. Research tool, not trading advice. No orders. Symbols SPY, QQQ. Sessions 2026-05-05 through 2026-10-23 (120). Timeframes 1m, 3m, 5m. Regular hours, entry from 9:35 through 15:45 ET. Costs match the edge hunt: buy the ask (option open plus the half-spread), sell the bid (fill minus the half-spread), half-spread the larger of 1 cent and 0.5% of premium, $0.65 a side.

## Verdict

The setup on the most sessions is `tf1_turn_mom_g95_f20` (120 of 120 sessions, 838 filled trades).

Matched pairs 604. On those pairs the signal +15% within 30 min is 67.4% and the random entry is 60.4%.

The +15% peak hit-rate within 30 minutes is higher than the matched random entry on this sample (67.4% signal, 60.4% random). Full-sample q is 0.098.

At a $0.62 premium, the fixed exit TP +15% / stop −15% needs a 67.7% win rate to break even after the half-spread and both commissions. That win rate is the share of trades that exit at the target, not the share whose peak bid tags +15%. This book's target-exit rate is 53.7%.

Mean peak net 73.3%, median peak net 40.7%, median minutes to the peak 15.0, median drawdown to that peak -20.0%. 95% bootstrap for the +15% within 30 min hit rate: 64.4% to 70.8%. 95% bootstrap for the mean TP +15% / stop −15% net: -5.8% to -3.8%.

The all-three cluster on the most sessions is `tf1_all3_n3_any_g95_f20` (120 of 120 sessions, 672 fills).

Matched pairs 491. On those pairs the signal +15% within 30 min is 62.9% and the random entry is 55.8%.

The +15% peak hit-rate within 30 minutes is higher than the matched random entry on this sample (62.9% signal, 55.8% random). Full-sample q is 0.121.

At a $0.61 premium, the fixed exit TP +15% / stop −15% needs a 68.0% win rate to break even after the half-spread and both commissions. That win rate is the share of trades that exit at the target, not the share whose peak bid tags +15%. This book's target-exit rate is 48.2%.

## Coverage

Greed/fear alone (`first`, the threshold that fires on the most days) is on 120 of 120 sessions. The all-three cluster (squeeze filter off, the window that fires on the most days) is on 120 sessions, which is 100% as many.

Same threshold as that `first` cell (tf 1m, G95, F30), all three with the squeeze filter off:

| setup | days | % sess | fills |
| --- | --- | --- | --- |
| first | 120 | 100.0% | 1041 |
| all3 N=0 | 91 | 75.8% | 94 |
| all3 N=1 | 120 | 100.0% | 556 |
| all3 N=2 | 120 | 100.0% | 682 |
| all3 N=3 | 120 | 100.0% | 759 |

Squeeze state at `tf1_all3_n3_any_g95_f20` (same timeframe, thresholds, and N). `any` is the cluster with no squeeze-state filter.

| squeeze | days | vs filter off | fills | +15% 30m |
| --- | --- | --- | --- | --- |
| any | 120 | 100.0% | 672 | 63.5% |
| released5 | 75 | 62.5% | 69 | 63.8% |
| on | 58 | 48.3% | 44 | 70.5% |
| off | 120 | 100.0% | 592 | 63.5% |

## Headline: all three turn

A put fires when greed is the pinned side and fear is the quiet side. A call is the mirror. The signal line is a 9-bar average of that pane. The pane does not publish its own signal line. Squeeze is Bollinger 20 / 2.0 inside Keltner 20 / 1.5, momentum a 20-bar linear regression of close minus the mid. That is the definition in backtest.py. All three means, within N bars on that timeframe: the pinned side turns down off its peak or under its signal line, the quiet side lifts off its low or through its signal line, and the squeeze momentum ticks against the move. The extreme (pinned at or above G, quiet at or below F) has to sit in that same window. The row fires once, on the first bar the set is complete. Squeeze `released5` means the squeeze fired within the last 5 bars. `on` means it is on now. `off` means it is not on and it did not fire in those 5 bars. `any` leaves that filter off.

Peak-bid hit rates for `tf1_all3_n3_any_g95_f20` (first OTM, premium 0.30–1.00):

| window | +10% | +15% | +20% | +30% |
| --- | --- | --- | --- | --- |
| 5 min | 46.0% | 34.2% | 26.2% | 15.5% |
| 15 min | 62.6% | 51.9% | 44.5% | 32.9% |
| 30 min | 72.2% | 63.5% | 56.8% | 44.6% |
| 60 min | 76.0% | 69.6% | 63.7% | 54.6% |

Fixed exits on that book: TP +15% / stop −15% mean -6.4% (target exits 48.2%), TP +15% / stop −25% mean -7.3%, TP +15% / no stop / 30 min mean -6.7%.

All-three rows with the most sessions (first OTM, premium 0.30–1.00):

| setup | days | % sess | fills | +15% 30m | random | mean MFE | mean 15/15 | q |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| all3 1m G95 F20 N=3 any | 120 | 100.0% | 672 | 63.5% | 55.8% | 70.0 | -6.4 | 0.121 |
| all3 1m G95 F20 N=3 off | 120 | 100.0% | 592 | 63.5% | 53.3% | 70.6 | -6.4 | 0.047 |
| all3 3m G85 F20 N=2 any | 120 | 100.0% | 284 | 63.4% | 48.0% | 74.5 | -7.8 | 0.051 |
| all3 1m G80 F20 N=3 off | 120 | 100.0% | 870 | 63.3% | 54.0% | 68.0 | -6.5 | 0.016 |
| all3 1m G95 F20 N=1 any | 120 | 100.0% | 482 | 63.1% | 54.9% | 68.3 | -6.3 | 0.176 |
| all3 1m G95 F30 N=3 off | 120 | 100.0% | 674 | 63.1% | 52.8% | 71.8 | -6.7 | 0.095 |
| all3 1m G95 F30 N=2 off | 120 | 100.0% | 605 | 63.0% | 52.7% | 71.6 | -6.8 | 0.125 |
| all3 1m G80 F30 N=3 off | 120 | 100.0% | 972 | 63.0% | 53.9% | 68.7 | -6.5 | 0.046 |
| all3 1m G80 F30 N=3 any | 120 | 100.0% | 1111 | 62.9% | 56.4% | 69.0 | -6.6 | 0.121 |
| all3 3m G85 F20 N=3 any | 120 | 100.0% | 302 | 62.9% | 49.6% | 75.3 | -8.2 | 0.113 |
| all3 1m G80 F30 N=2 off | 120 | 100.0% | 950 | 62.8% | 53.1% | 69.1 | -6.4 | 0.024 |
| all3 1m G80 F20 N=2 off | 120 | 100.0% | 827 | 62.8% | 54.4% | 69.7 | -6.2 | 0.026 |

## Walk-forward

Five expanding folds. Block 0 is train only. Each fold picks one cell on its train days (first OTM, premium 0.30–1.00, most sessions, then the higher +15% peak within 30 minutes) and scores that cell only on the later test days. A cell needs 15 train fills to be eligible when any cell has that many.

Fold 1: train 2026-05-05 to 2026-06-02 (20 sessions, 33 fills, minimum met), chose `tf1_all3_n3_off_g85_f5`. Test 2026-06-03 to 2026-07-01: 16 sessions, 11 fills, +15% within 30 min 72.7% (matched 85.7% versus random 71.4%), mean net at TP +15% / stop −15% -3.5%, target exits 54.5%. Bootstrap for the test hit rate: 50.0% to 100.0%.

Fold 2: train 2026-05-05 to 2026-07-01 (40 sessions, 64 fills, minimum met), chose `tf3_all3_n1_off_g90_f30`. Test 2026-07-02 to 2026-07-30: 20 sessions, 32 fills, +15% within 30 min 59.4% (matched 57.7% versus random 42.3%), mean net at TP +15% / stop −15% -10.8%, target exits 34.4%. Bootstrap for the test hit rate: 39.0% to 78.6%.

Fold 3: train 2026-05-05 to 2026-07-30 (60 sessions, 206 fills, minimum met), chose `tf3_first_g90_f20`. Test 2026-07-31 to 2026-08-27: 20 sessions, 70 fills, +15% within 30 min 54.3% (matched 50.0% versus random 51.7%), mean net at TP +15% / stop −15% -9.2%, target exits 40.0%. Bootstrap for the test hit rate: 40.8% to 67.9%.

Fold 4: train 2026-05-05 to 2026-08-27 (80 sessions, 514 fills, minimum met), chose `tf1_turn_mom_g95_f20`. Test 2026-08-28 to 2026-09-25: 20 sessions, 177 fills, +15% within 30 min 66.1% (matched 66.9% versus random 63.2%), mean net at TP +15% / stop −15% -7.2%, target exits 46.3%. Bootstrap for the test hit rate: 58.9% to 73.8%.

Fold 5: train 2026-05-05 to 2026-09-25 (100 sessions, 691 fills, minimum met), chose `tf1_turn_mom_g95_f20`. Test 2026-09-28 to 2026-10-23: 20 sessions, 147 fills, +15% within 30 min 70.1% (matched 70.4% versus random 46.9%), mean net at TP +15% / stop −15% -3.6%, target exits 57.1%. Bootstrap for the test hit rate: 61.4% to 77.8%.

## Held-out last 25%

The last 25% of sessions were not used to pick the cell. The pick uses the first 75% and the same rule as the folds.

Fold heldout: train 2026-05-05 to 2026-09-11 (90 sessions, 616 fills, minimum met), chose `tf1_turn_mom_g95_f20`. Test 2026-09-14 to 2026-10-23: 30 sessions, 222 fills, +15% within 30 min 68.9% (matched 69.1% versus random 51.3%), mean net at TP +15% / stop −15% -4.5%, target exits 54.5%. Bootstrap for the test hit rate: 62.4% to 75.1%.

## Other variants

Sorted by sessions covered, then the +15% peak within 30 minutes, then fills. `first` is the first bar of the extreme. `turn` is the pinned side leaving that extreme. `turn_band` also wants price outside the fade-side VWAP band (VWAP plus or minus ATR 14) or the Bollinger band. `turn_mom` also wants squeeze momentum or the MACD histogram ticking against the move. The cooldown is one event per ticker per 20 minutes inside each cell, so the variants can be compared. The full grid, both strikes, and both premium books are in `fgfade_summary.csv`. Hit columns there are percents. q is Benjamini-Hochberg over every row in that file. It is a screen. The fold section is the out-of-sample result.

| setup | days | % sess | fills | +15% 30m | random | mean MFE | mean 15/15 | q |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| turn_mom 1m G95 F20 | 120 | 100.0% | 838 | 67.5% | 60.4% | 73.3 | -4.8 | 0.098 |
| turn 1m G95 F20 | 120 | 100.0% | 902 | 67.0% | 59.6% | 71.9 | -5.3 | 0.036 |
| first 1m G95 F30 | 120 | 100.0% | 1041 | 66.2% | 62.9% | 75.0 | -5.3 | 0.447 |
| first 1m G95 F20 | 120 | 100.0% | 956 | 66.1% | 63.1% | 72.4 | -5.6 | 0.557 |
| turn 1m G95 F30 | 120 | 100.0% | 1020 | 65.8% | 58.5% | 72.8 | -5.8 | 0.035 |
| turn 1m G95 F10 | 120 | 100.0% | 603 | 65.5% | 63.3% | 73.6 | -5.8 | 0.557 |
| turn_mom 1m G90 F20 | 120 | 100.0% | 932 | 65.2% | 59.8% | 69.6 | -5.3 | 0.198 |
| turn_mom 1m G95 F30 | 120 | 100.0% | 948 | 65.0% | 60.8% | 73.9 | -5.8 | 0.347 |
| first 1m G90 F20 | 120 | 100.0% | 1037 | 64.7% | 62.7% | 70.9 | -6.0 | 0.743 |
| turn 1m G90 F20 | 120 | 100.0% | 986 | 64.7% | 60.3% | 69.7 | -5.7 | 0.196 |
| turn_mom 1m G95 F10 | 120 | 100.0% | 541 | 64.7% | 63.5% | 73.5 | -5.6 | 0.907 |
| first 1m G95 F10 | 120 | 100.0% | 715 | 64.6% | 60.0% | 69.8 | -6.0 | 0.387 |
| first 1m G85 F30 | 120 | 100.0% | 1211 | 64.6% | 60.8% | 72.2 | -6.0 | 0.387 |
| first 1m G80 F30 | 120 | 100.0% | 1308 | 64.5% | 61.0% | 70.6 | -6.0 | 0.507 |
| first 1m G80 F20 | 120 | 100.0% | 1242 | 64.5% | 60.1% | 68.9 | -6.0 | 0.243 |

## 2026-10-19 through 2026-10-23

| date | time | ticker | side | variant | entry ask | peak bid | min to peak | 15/15 net |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-10-19 | 09:57 | SPY | call | all3 | 0.92 | 1.97 | 21 | -18.4 |
| 2026-10-19 | 10:36 | SPY | call | turn | 0.75 | 1.88 | 52 | -19.2 |
| 2026-10-19 | 10:36 | SPY | call | turn_mom | 0.75 | 1.88 | 52 | -19.2 |
| 2026-10-19 | 11:28 | SPY | put | first | 0.67 | 1.81 | 39 | 9.9 |
| 2026-10-19 | 11:49 | SPY | call | first | 0.47 | 0.56 | 4 | 7.7 |
| 2026-10-19 | 12:05 | SPY | call | turn | 0.86 | 0.95 | 6 | -18.7 |
| 2026-10-19 | 12:05 | SPY | call | turn_mom | 0.86 | 0.95 | 6 | -18.7 |
| 2026-10-19 | 13:15 | QQQ | put | first | 0.81 | 1.43 | 34 | -18.9 |
| 2026-10-19 | 13:15 | SPY | put | first | 0.40 | 0.51 | 34 | -22.9 |
| 2026-10-19 | 13:20 | QQQ | put | turn | 0.81 | 1.43 | 29 | 10.7 |
| 2026-10-19 | 13:20 | QQQ | put | turn_mom | 0.81 | 1.43 | 29 | 10.7 |
| 2026-10-19 | 13:20 | SPY | put | all3 | 0.42 | 0.51 | 29 | 6.8 |
| 2026-10-19 | 13:20 | SPY | put | turn | 0.42 | 0.51 | 29 | 6.8 |
| 2026-10-19 | 13:20 | SPY | put | turn_mom | 0.42 | 0.51 | 29 | 6.8 |
| 2026-10-19 | 13:21 | QQQ | put | all3 | 0.66 | 0.94 | 28 | -19.8 |
| 2026-10-19 | 13:49 | QQQ | call | first | 0.81 | 1.43 | 11 | 10.7 |
| 2026-10-19 | 13:50 | QQQ | call | turn | 0.49 | 0.85 | 10 | 8.0 |
| 2026-10-19 | 13:50 | QQQ | call | turn_mom | 0.49 | 0.85 | 10 | 8.0 |
| 2026-10-19 | 13:59 | SPY | put | first | 0.51 | 0.83 | 36 | -21.2 |
| 2026-10-19 | 14:02 | SPY | put | turn | 0.48 | 0.83 | 33 | 7.8 |
| 2026-10-19 | 14:16 | SPY | put | all3 | 0.32 | 0.83 | 19 | 4.2 |
| 2026-10-19 | 14:16 | SPY | put | turn_mom | 0.32 | 0.83 | 19 | 4.2 |
| 2026-10-19 | 14:27 | SPY | call | first | 0.33 | 0.79 | 58 | -24.5 |
| 2026-10-19 | 14:29 | QQQ | call | first | 0.52 | 2.27 | 56 | 8.4 |
| 2026-10-19 | 14:37 | QQQ | call | all3 | 0.35 | 1.42 | 47 | 5.1 |
| 2026-10-19 | 14:37 | QQQ | call | turn | 0.35 | 1.42 | 47 | 5.1 |
| 2026-10-19 | 14:37 | QQQ | call | turn_mom | 0.35 | 1.42 | 47 | 5.1 |
| 2026-10-19 | 14:37 | SPY | call | all3 | 0.34 | 0.79 | 48 | 4.9 |
| 2026-10-19 | 14:37 | SPY | call | turn | 0.34 | 0.79 | 48 | 4.9 |
| 2026-10-19 | 14:37 | SPY | call | turn_mom | 0.34 | 0.79 | 48 | 4.9 |
| 2026-10-20 | 11:04 | SPY | call | first | 0.90 | 0.91 | 0 | -18.5 |
| 2026-10-20 | 11:08 | SPY | call | turn | 0.86 | 0.91 | 0 | -18.7 |
| 2026-10-20 | 11:08 | SPY | call | turn_mom | 0.86 | 0.91 | 0 | -18.7 |
| 2026-10-20 | 11:17 | SPY | call | all3 | 0.78 | 0.91 | 0 | 10.6 |
| 2026-10-20 | 12:38 | SPY | put | first | 0.68 | 1.41 | 16 | 9.9 |
| 2026-10-20 | 12:39 | SPY | put | turn | 0.72 | 1.41 | 15 | 10.2 |
| 2026-10-20 | 12:39 | SPY | put | turn_mom | 0.72 | 1.41 | 15 | 10.2 |
| 2026-10-20 | 12:40 | SPY | put | all3 | 0.48 | 0.92 | 14 | -21.6 |
| 2026-10-20 | 12:55 | QQQ | call | first | 0.90 | 1.58 | 59 | 11.2 |
| 2026-10-20 | 12:56 | QQQ | call | turn | 0.94 | 1.58 | 58 | 11.3 |
| 2026-10-20 | 12:56 | QQQ | call | turn_mom | 0.94 | 1.58 | 58 | 11.3 |
| 2026-10-20 | 12:58 | QQQ | call | all3 | 0.94 | 1.58 | 56 | 11.3 |
| 2026-10-20 | 13:23 | SPY | put | first | 0.34 | 0.33 | 0 | -24.3 |
| 2026-10-20 | 13:24 | SPY | put | turn | 0.59 | 0.64 | 10 | -20.3 |
| 2026-10-20 | 13:33 | SPY | put | turn_mom | 0.51 | 0.73 | 60 | 8.2 |
| 2026-10-20 | 14:03 | QQQ | call | first | 0.67 | 0.78 | 6 | 9.9 |
| 2026-10-20 | 14:03 | SPY | call | first | 0.41 | 0.51 | 11 | 6.6 |
| 2026-10-20 | 14:07 | QQQ | call | turn | 0.65 | 0.78 | 2 | 9.7 |
| 2026-10-20 | 14:07 | QQQ | call | turn_mom | 0.65 | 0.78 | 2 | 9.7 |
| 2026-10-20 | 14:07 | SPY | call | turn | 0.36 | 0.51 | 7 | 5.4 |
| 2026-10-20 | 14:07 | SPY | call | turn_mom | 0.36 | 0.51 | 7 | 5.4 |
| 2026-10-20 | 14:09 | QQQ | call | all3 | 0.42 | 0.43 | 0 | -22.5 |
| 2026-10-20 | 14:26 | QQQ | call | first | 0.46 | 0.51 | 3 | 7.5 |
| 2026-10-20 | 14:27 | SPY | call | first | 0.31 | 0.30 | 2 | -25.2 |
| 2026-10-20 | 14:37 | QQQ | call | turn | 0.57 | 0.84 | 18 | 8.9 |
| 2026-10-20 | 14:39 | QQQ | call | all3 | 0.60 | 0.84 | 16 | 9.2 |
| 2026-10-20 | 14:40 | QQQ | call | turn_mom | 0.65 | 0.84 | 15 | -19.8 |
| 2026-10-20 | 14:55 | QQQ | put | first | 0.41 | 1.03 | 28 | -22.7 |
| 2026-10-20 | 14:57 | QQQ | put | turn | 0.69 | 1.61 | 26 | 10.0 |
| 2026-10-21 | 10:45 | SPY | put | first | 0.89 | 0.87 | 0 | -18.5 |
| 2026-10-21 | 10:46 | SPY | put | all3 | 0.85 | 0.86 | 0 | -18.7 |
| 2026-10-21 | 10:46 | SPY | put | turn | 0.85 | 0.86 | 0 | -18.7 |
| 2026-10-21 | 10:46 | SPY | put | turn_mom | 0.85 | 0.86 | 0 | -18.7 |
| 2026-10-21 | 11:21 | SPY | call | first | 0.77 | 1.57 | 29 | 10.5 |
| 2026-10-21 | 11:22 | SPY | call | turn | 0.85 | 1.57 | 28 | 10.9 |
| 2026-10-21 | 11:22 | SPY | call | turn_mom | 0.85 | 1.57 | 28 | 10.9 |
| 2026-10-21 | 12:10 | SPY | call | first | 0.72 | 1.59 | 30 | 10.2 |
| 2026-10-21 | 12:11 | SPY | call | all3 | 0.72 | 1.59 | 29 | 10.2 |
| 2026-10-21 | 12:11 | SPY | call | turn | 0.72 | 1.59 | 29 | 10.2 |
| 2026-10-21 | 12:11 | SPY | call | turn_mom | 0.72 | 1.59 | 29 | 10.2 |
| 2026-10-21 | 12:12 | QQQ | call | first | 0.97 | 2.02 | 28 | -18.2 |
| 2026-10-21 | 12:13 | QQQ | call | all3 | 0.93 | 2.02 | 27 | -18.4 |
| 2026-10-21 | 12:13 | QQQ | call | turn | 0.93 | 2.02 | 27 | -18.4 |
| 2026-10-21 | 12:13 | QQQ | call | turn_mom | 0.93 | 2.02 | 27 | -18.4 |
| 2026-10-21 | 13:33 | QQQ | call | first | 0.94 | 1.18 | 57 | 11.3 |
| 2026-10-21 | 13:36 | QQQ | call | turn | 0.93 | 1.18 | 54 | 11.3 |
| 2026-10-21 | 13:36 | QQQ | call | turn_mom | 0.93 | 1.18 | 54 | 11.3 |
| 2026-10-21 | 14:17 | SPY | put | first | 0.34 | 2.77 | 46 | -24.3 |
| 2026-10-21 | 14:18 | QQQ | put | turn | 1.00 | 3.93 | 45 | 11.5 |
| 2026-10-21 | 14:18 | SPY | put | turn | 0.33 | 2.77 | 45 | 4.5 |
| 2026-10-21 | 14:20 | QQQ | put | turn_mom | 1.01 | 3.93 | 43 | 11.6 |
| 2026-10-21 | 14:59 | SPY | call | turn | 0.64 | 1.22 | 52 | -19.9 |
| 2026-10-21 | 15:18 | SPY | put | first | 0.51 | 0.62 | 0 | 8.2 |
| 2026-10-21 | 15:19 | QQQ | put | turn | 1.01 | 1.00 | 0 | -18.1 |
| 2026-10-21 | 15:19 | QQQ | put | turn_mom | 1.01 | 1.00 | 0 | -18.1 |
| 2026-10-21 | 15:19 | SPY | put | turn | 0.60 | 0.59 | 0 | -20.3 |
| 2026-10-21 | 15:19 | SPY | put | turn_mom | 0.60 | 0.59 | 0 | -20.3 |
| 2026-10-21 | 15:24 | SPY | put | all3 | 0.47 | 0.54 | 0 | -21.7 |
| 2026-10-22 | 11:27 | SPY | put | turn | 1.01 | 1.87 | 13 | 11.6 |
| 2026-10-22 | 11:27 | SPY | put | turn_mom | 1.01 | 1.87 | 13 | 11.6 |
| 2026-10-22 | 12:01 | SPY | put | first | 0.98 | 2.55 | 49 | 11.5 |
| 2026-10-22 | 12:50 | SPY | call | all3 | 0.88 | 1.29 | 9 | 11.1 |
| 2026-10-22 | 13:02 | SPY | put | turn | 0.84 | 1.36 | 60 | 10.9 |
| 2026-10-22 | 13:02 | SPY | put | turn_mom | 0.84 | 1.36 | 60 | 10.9 |
| 2026-10-22 | 13:59 | QQQ | call | first | 0.94 | 1.46 | 21 | -18.4 |
| 2026-10-22 | 14:00 | QQQ | call | turn | 0.96 | 1.46 | 20 | -18.3 |
| 2026-10-22 | 14:00 | QQQ | call | turn_mom | 0.96 | 1.46 | 20 | -18.3 |
| 2026-10-22 | 14:02 | SPY | call | first | 0.74 | 1.48 | 19 | -19.3 |
| 2026-10-22 | 14:06 | SPY | call | all3 | 0.67 | 1.48 | 15 | 9.9 |
| 2026-10-22 | 14:06 | SPY | call | turn | 0.67 | 1.48 | 15 | 9.9 |
| 2026-10-22 | 14:06 | SPY | call | turn_mom | 0.67 | 1.48 | 15 | 9.9 |
| 2026-10-22 | 14:22 | QQQ | put | turn | 0.98 | 3.00 | 40 | 11.5 |
| 2026-10-22 | 14:22 | QQQ | put | turn_mom | 0.98 | 3.00 | 40 | 11.5 |
| 2026-10-22 | 14:42 | SPY | call | first | 0.53 | 0.88 | 47 | 8.5 |
| 2026-10-22 | 14:43 | SPY | call | all3 | 0.51 | 0.88 | 46 | 8.2 |
| 2026-10-22 | 14:43 | SPY | call | turn | 0.51 | 0.88 | 46 | 8.2 |
| 2026-10-22 | 14:43 | SPY | call | turn_mom | 0.51 | 0.88 | 46 | 8.2 |
| 2026-10-22 | 15:21 | QQQ | put | first | 0.67 | 1.49 | 26 | -19.7 |
| 2026-10-22 | 15:21 | SPY | put | first | 0.53 | 0.92 | 26 | -20.9 |
| 2026-10-22 | 15:23 | QQQ | put | all3 | 0.77 | 1.49 | 24 | -19.1 |
| 2026-10-22 | 15:23 | QQQ | put | turn | 0.77 | 1.49 | 24 | -19.1 |
| 2026-10-22 | 15:23 | QQQ | put | turn_mom | 0.77 | 1.49 | 24 | -19.1 |
| 2026-10-22 | 15:23 | SPY | put | all3 | 0.34 | 0.44 | 24 | -24.3 |
| 2026-10-22 | 15:23 | SPY | put | turn | 0.34 | 0.44 | 24 | -24.3 |
| 2026-10-22 | 15:23 | SPY | put | turn_mom | 0.34 | 0.44 | 24 | -24.3 |
| 2026-10-22 | 15:43 | SPY | call | turn | 0.33 | 1.21 | 8 | -24.5 |
| 2026-10-22 | 15:43 | SPY | call | turn_mom | 0.33 | 1.21 | 8 | -24.5 |
| 2026-10-22 | 15:44 | QQQ | call | first | 0.55 | 1.99 | 11 | 8.7 |
| 2026-10-23 | 12:25 | SPY | call | first | 0.84 | 1.14 | 21 | 10.9 |
| 2026-10-23 | 12:26 | SPY | call | turn | 0.80 | 1.14 | 20 | 10.7 |
| 2026-10-23 | 12:28 | SPY | call | turn_mom | 0.80 | 1.14 | 18 | 10.7 |
| 2026-10-23 | 12:29 | SPY | call | all3 | 0.81 | 1.14 | 17 | 10.7 |
| 2026-10-23 | 12:45 | SPY | put | first | 0.71 | 1.79 | 31 | 10.1 |
| 2026-10-23 | 12:49 | SPY | put | all3 | 0.75 | 1.79 | 27 | 10.4 |
| 2026-10-23 | 12:49 | SPY | put | turn | 0.75 | 1.79 | 27 | 10.4 |
| 2026-10-23 | 12:49 | SPY | put | turn_mom | 0.75 | 1.79 | 27 | 10.4 |
| 2026-10-23 | 13:06 | SPY | call | first | 0.86 | 0.87 | 0 | -18.7 |
| 2026-10-23 | 13:59 | QQQ | put | first | 0.93 | 1.75 | 49 | 11.3 |
| 2026-10-23 | 13:59 | SPY | put | first | 0.51 | 0.81 | 49 | 8.2 |
| 2026-10-23 | 14:40 | SPY | call | first | 0.51 | 0.62 | 12 | 8.2 |
| 2026-10-23 | 14:41 | SPY | call | turn | 0.51 | 0.62 | 11 | 8.2 |
| 2026-10-23 | 14:43 | QQQ | call | first | 0.60 | 0.65 | 1 | -20.3 |
| 2026-10-23 | 14:43 | SPY | call | turn_mom | 0.55 | 0.62 | 9 | -20.7 |
| 2026-10-23 | 14:44 | QQQ | call | turn | 0.66 | 0.65 | 0 | -19.8 |
| 2026-10-23 | 14:44 | QQQ | call | turn_mom | 0.66 | 0.65 | 0 | -19.8 |
| 2026-10-23 | 15:04 | SPY | put | first | 0.45 | 0.68 | 48 | 7.3 |
| 2026-10-23 | 15:05 | SPY | put | all3 | 0.47 | 0.68 | 47 | 7.7 |
| 2026-10-23 | 15:05 | SPY | put | turn | 0.47 | 0.68 | 47 | 7.7 |

## Notes

The +15% peak test uses the best bid in the window. Net is that bid against the entry ask, minus both commissions. The fixed +15% target is different: the option high has to touch the raw premium times 1.15, and the sale is on the bid. On a bar that touches both the stop and the target, the stop is taken first.

The book flats at 15:55. An entry at 15:45 has ten minutes of path, so the 30-minute and 60-minute windows are that shorter path. A chart event whose entry would fall before 9:35 is not taken, and a run that started then is not re-armed at 9:35.

This file scores 960 setups and 3840 rows after strike and premium band. Bootstrap draws: 1000. Runtime 2.4 minutes. A short sample is not a reason to change the live bot.
