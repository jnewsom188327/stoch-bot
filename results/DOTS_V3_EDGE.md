# White dots v3 - edge miner, 130 days, 3979 dots, real option prices

Feed sip. TRAIN = 2026-05-05 to 2026-09-04 (2699 dots). TEST (never seen while searching) = 2026-09-08 to 2026-11-06 (1280 dots).
Score per dot = 1 OTM 0DTE, +10% target / -25% stop / out at 30 min, after the spread (R, % of premium). Win = +10% before -25%.

| Group | Dots | Win | Avg R |
|---|---|---|---|
| All dots | 3979 | 66.6% | -6.01% |
| Random entries (same days, same count) | 3998 | 67.9% | -4.58% |
| All dots at 2 ITM | 3979 | 60.4% | -2.75% |

## Every reading on its own (fifths set on TRAIN; avg R in each fifth, train | test)

| Reading | lowest fifth | 2nd | 3rd | 4th | highest fifth | spread train | spread test |
|---|---|---|---|---|---|---|---|
| minute_of_day | -3.3 \| -4.4 | -4.6 \| -3.6 | -5.9 \| -5.8 | -4.9 \| -6.4 | -10.8 \| -11.2 | 7.5 | 7.5 |
| dots_today_same_side | -3.5 \| -4.0 | -3.8 \| -3.9 | -6.9 \| -6.1 | -7.1 \| -8.3 | -9.5 \| -11.7 | 6.1 | 7.8 |
| atr_pct | -9.0 \| -11.7 | -6.5 \| -6.4 | -5.4 \| -5.0 | -5.0 \| -4.4 | -3.5 \| -2.1 | 5.5 | 9.6 |
| day_range_atr | -2.9 \| -4.6 | -5.6 \| -3.9 | -8.1 \| -5.5 | -5.8 \| -9.2 | -7.0 \| -8.9 | 5.2 | 5.2 |
| dist_overnight_level_atr | -5.0 \| -5.0 | -4.6 \| -5.7 | -5.9 \| -5.4 | -6.1 \| -5.5 | -7.9 \| -8.9 | 3.3 | 3.9 |
| rejection_wick_atr | -4.0 \| -4.8 | -6.2 \| -9.0 | -7.1 \| -5.3 | -5.2 \| -5.1 | -7.0 \| -7.0 | 3.1 | 4.2 |
| dist_prev_day_level_atr | -4.5 \| -6.6 | -4.5 \| -5.3 | -6.3 \| -5.1 | -6.8 \| -6.0 | -7.5 \| -7.6 | 3.0 | 2.5 |
| rel_volume5 | -4.4 \| -6.0 | -5.4 \| -6.4 | -6.3 \| -3.8 | -6.2 \| -3.3 | -7.3 \| -9.6 | 3.0 | 6.3 |
| vix_15m_helping_pct | -4.5 \| -3.5 | -6.3 \| -6.8 | -5.7 \| -7.1 | -5.7 \| -7.8 | -7.3 \| -6.9 | 2.8 | 4.3 |
| ttm_slope3 | -6.8 \| -6.1 | -4.6 \| -6.7 | -7.2 \| -6.8 | -5.0 \| -5.6 | -5.8 \| -5.9 | 2.6 | 1.2 |
| fg_stretch | -6.0 \| -7.2 | -7.1 \| -6.4 | -6.4 \| -6.8 | -5.2 \| -5.6 | -4.8 \| -5.2 | 2.3 | 2.0 |
| fg_bars_90plus_20 | -6.3 \| -7.4 | -7.4 \| -7.8 | -5.6 \| -5.4 | -5.7 \| -6.9 | -5.1 \| -3.3 | 2.3 | 4.6 |
| fg_gap | -6.7 \| -6.8 | -6.3 \| -6.6 | -6.2 \| -7.2 | -5.7 \| -5.4 | -4.5 \| -5.1 | 2.2 | 2.1 |
| dist_extreme_atr | -5.4 \| -7.4 | -5.5 \| -7.2 | -5.8 \| -4.5 | -5.4 \| -5.1 | -7.5 \| -7.6 | 2.1 | 3.1 |
| fg_other | -5.6 \| -6.2 | -4.9 \| -5.7 | -5.3 \| -5.0 | -7.0 \| -7.7 | -6.7 \| -6.4 | 2.1 | 2.7 |
| dist_day_extreme_atr | -5.4 \| -5.1 | -5.0 \| -5.7 | -5.1 \| -5.1 | -6.8 \| -7.0 | -7.1 \| -8.1 | 2.1 | 3.0 |
| fg_mins_since_95 | -4.9 \| -4.5 | -5.8 \| -5.9 | -5.6 \| -7.1 | -6.9 \| -7.2 | -6.5 \| -7.0 | 2.0 | 2.6 |
| day_chg_pct | -5.1 \| -4.5 | -6.4 \| -5.0 | -5.7 \| -7.0 | -5.4 \| -9.1 | -6.9 \| -4.5 | 1.9 | 4.6 |
| tl_slope_atr | -6.5 \| -5.6 | -5.4 \| -7.2 | -5.8 \| -5.8 | -5.1 \| -6.4 | -6.7 \| -6.3 | 1.6 | 1.6 |
| ttm_mom | -5.0 \| -4.7 | -6.3 \| -7.6 | -6.5 \| -5.9 | -5.4 \| -6.0 | -6.3 \| -7.1 | 1.6 | 2.9 |
| fg_other_slope3 | -5.7 \| -7.6 | -5.2 \| -4.5 | -6.3 \| -7.2 | -6.8 \| -5.2 | -5.6 \| -6.5 | 1.5 | 3.1 |
| fg_letting_off | -5.5 \| -5.8 | -5.3 \| -6.5 | -6.0 \| -5.4 | -6.0 \| -6.2 | -6.7 \| -7.4 | 1.5 | 2.0 |
| stall_body_atr | -6.4 \| -6.7 | -5.4 \| -5.9 | -5.6 \| -6.1 | -5.3 \| -5.3 | -6.8 \| -7.1 | 1.4 | 1.8 |
| trend_color | -5.6 \| -6.5 | +nan \| +nan | -6.7 \| -6.1 | +nan \| +nan | -5.6 \| -5.5 | 1.1 | 0.9 |
| dist_round5_dollars | -6.1 \| -8.8 | -6.2 \| -4.7 | -5.9 \| -6.3 | -5.3 \| -4.9 | -6.0 \| -6.2 | 1.0 | 4.1 |
| gap_pct | -5.4 \| -5.9 | -5.5 \| -5.0 | -6.1 \| -10.0 | -6.1 \| -5.7 | -6.3 \| -6.3 | 1.0 | 4.9 |
| stall_vs_drive_volume | -5.7 \| -5.9 | -5.4 \| -5.0 | -6.3 \| -6.4 | -6.0 \| -5.1 | -6.1 \| -8.2 | 0.9 | 3.2 |
| ttm_turned2 | -6.0 \| -6.5 | +nan \| +nan | +nan \| +nan | +nan \| +nan | -5.6 \| -5.3 | 0.4 | 1.2 |
| bars_since_extreme | -5.9 \| -6.0 | +nan \| +nan | +nan \| +nan | +nan \| +nan | -6.1 \| -7.6 | 0.2 | 1.7 |
| fg_stretch_peak5 | -5.5 \| -6.0 | -7.1 \| -7.4 | -5.7 \| -7.6 | -5.5 \| -5.1 | +nan \| +nan | 1.6 | 2.5 |
| fg_stretch_peak20 | -5.3 \| -6.6 | -7.7 \| -8.4 | -5.5 \| -5.3 | +nan \| +nan | +nan \| +nan | 2.5 | 3.1 |
| fg_stretch_slope3 | -6.1 \| -6.6 | -5.3 \| -5.9 | -5.6 \| -5.8 | -7.5 \| -6.2 | -5.0 \| -6.6 | 2.5 | 0.8 |
| fg_both_turning | -5.4 \| -6.9 | +nan \| +nan | -6.4 \| -5.7 | +nan \| +nan | +nan \| +nan | 1.0 | 1.2 |
| fg_stretch_under_avg | -6.0 \| -6.5 | +nan \| +nan | +nan \| +nan | -5.8 \| -5.8 | +nan \| +nan | 0.2 | 0.7 |
| fg_other_over_avg | -5.7 \| -6.0 | +nan \| +nan | +nan \| +nan | -6.4 \| -6.6 | +nan \| +nan | 0.7 | 0.6 |
| ttm_slope1 | -6.5 \| -6.4 | -5.5 \| -6.5 | -6.3 \| -6.7 | -5.3 \| -4.7 | -5.8 \| -7.1 | 1.2 | 2.4 |
| ttm_squeeze | -5.9 \| -6.0 | +nan \| +nan | +nan \| +nan | -5.8 \| -6.7 | +nan \| +nan | 0.1 | 0.7 |
| tl_dist_atr | -6.1 \| -6.8 | -5.8 \| -5.6 | -5.6 \| -5.7 | -4.7 \| -6.3 | -7.2 \| -6.7 | 2.5 | 1.2 |
| tl_13_vs_34_atr | -5.6 \| -5.9 | -6.6 \| -7.2 | -5.6 \| -6.7 | -6.0 \| -6.0 | -5.7 \| -5.4 | 1.0 | 1.8 |
| ema9_dist_atr | -6.8 \| -7.3 | -5.0 \| -6.4 | -5.3 \| -4.9 | -5.4 \| -5.5 | -6.9 \| -7.2 | 1.9 | 2.4 |
| vwap_dist_atr | -5.6 \| -7.7 | -6.6 \| -4.1 | -4.8 \| -7.1 | -5.3 \| -6.4 | -7.1 \| -5.8 | 2.3 | 3.6 |
| drive_atr | -5.3 \| -7.0 | -5.4 \| -6.4 | -6.8 \| -5.5 | -6.1 \| -6.1 | -5.8 \| -6.1 | 1.5 | 1.5 |
| pos_in_day_range | -6.7 \| -5.4 | -5.1 \| -6.7 | -4.6 \| -5.6 | -6.6 \| -7.2 | -6.6 \| -6.1 | 2.1 | 1.8 |
| mins_since_opposite_dot | -7.0 \| -6.6 | -5.3 \| -4.9 | -6.3 \| -6.2 | -6.6 \| -5.6 | -4.0 \| -7.7 | 3.0 | 2.8 |
| weak_gray | -5.6 \| -5.8 | +nan \| +nan | +nan \| +nan | -7.2 \| -8.0 | +nan \| +nan | 1.6 | 2.2 |
| vix_day_helping_pct | -6.6 \| -5.4 | -4.9 \| -4.8 | -6.2 \| -7.9 | -5.5 \| -8.1 | -6.2 \| -5.7 | 1.7 | 3.4 |
| weekday | -6.1 \| -8.9 | -5.4 \| -4.2 | +nan \| +nan | -5.2 \| -6.3 | -6.9 \| -3.3 | 1.7 | 5.6 |

## Luck check
With the outcomes shuffled at random, the best train score the search still finds is: single -4.08%, pair +0.35%, triple +3.59% per trade. A real rule has to beat these on TRAIN and also stay positive on TEST.

## Rules that beat luck on TRAIN and stayed positive on TEST (0 found, best 40)

| Rule | Size | Train dots | Train win | Train R | Test dots | Test win | Test R |
|---|---|---|---|---|---|---|---|

## Best 20 on TRAIN alone, and what happened on TEST (shows how much is curve-fit)

| Rule | Train dots | Train R | Test dots | Test R |
|---|---|---|---|---|
| fg_stretch_slope3 >= 8.87 AND fg_gap >= 73.6 AND minute_of_day <= 173 | 56 | +2.77% | 28 | -7.83% |
| fg_other <= 16 AND atr_pct >= 0.0538 AND gap_pct <= -0.424 | 65 | +2.47% | 9 | -0.94% |
| fg_stretch_peak20 >= 92.5 AND fg_stretch_slope3 >= 8.87 AND day_range_atr <= 11.3 | 52 | +2.46% | 24 | -7.44% |
| fg_stretch_slope3 >= 8.87 AND fg_gap >= 73.6 AND dots_today_same_side <= 6 | 68 | +2.33% | 34 | -6.66% |
| fg_stretch >= 91.1 AND fg_stretch_slope3 >= 8.87 AND dots_today_same_side <= 6 | 61 | +2.33% | 34 | -4.57% |
| ttm_slope3 >= -0.279 AND day_range_atr <= 11.3 AND rel_volume5 <= 0.713 | 64 | +2.31% | 31 | -5.56% |
| fg_stretch >= 78.4 AND fg_stretch_slope3 >= 8.87 AND day_range_atr <= 11.3 | 55 | +2.07% | 27 | -3.16% |
| fg_stretch >= 78.4 AND rejection_wick_atr <= 0.293 AND vix_15m_helping_pct <= -0.403 | 73 | +2.00% | 36 | -1.63% |
| fg_other <= 16 AND atr_pct >= 0.0538 AND gap_pct <= -0.149 | 92 | +1.95% | 24 | -4.64% |
| fg_gap >= 57.7 AND rejection_wick_atr <= 0.293 AND dots_today_same_side <= 3 | 73 | +1.92% | 24 | -1.35% |
| ttm_mom <= -2.39 AND atr_pct >= 0.0384 AND gap_pct <= -0.424 | 53 | +1.89% | 21 | -0.68% |
| fg_gap >= 57.7 AND rejection_wick_atr <= 0.293 AND vix_15m_helping_pct <= -0.403 | 65 | +1.89% | 31 | +0.24% |
| fg_gap >= 73.6 AND gap_pct <= -0.424 AND dots_today_same_side <= 6 | 51 | +1.83% | 26 | -9.04% |
| dist_extreme_atr <= 0.438 AND rel_volume5 <= 0.713 AND minute_of_day <= 93.6 | 53 | +1.83% | 18 | -6.62% |
| gap_pct <= -0.149 AND mins_since_opposite_dot >= 58 AND rel_volume5 <= 0.713 | 52 | +1.81% | 38 | -3.06% |
| rejection_wick_atr <= 0.293 AND atr_pct >= 0.0538 AND day_range_atr <= 11.3 | 68 | +1.71% | 17 | +2.98% |
| fg_bars_90plus_20 >= 4 AND rejection_wick_atr <= 0.293 AND vix_15m_helping_pct <= -0.403 | 68 | +1.71% | 38 | -1.99% |
| rejection_wick_atr <= 0.293 AND atr_pct >= 0.0538 AND minute_of_day <= 93.6 | 68 | +1.69% | 15 | +2.52% |
| drive_atr <= 3.95 AND day_range_atr <= 17.6 AND vix_15m_helping_pct <= -0.403 | 56 | +1.67% | 34 | -5.41% |
| ttm_slope3 >= -0.279 AND day_range_atr <= 11.3 AND gap_pct <= -0.149 | 68 | +1.66% | 40 | -5.21% |

## Trading the top 5 surviving rules from $2,000 (cash account, 25% size, -25% stop)

| Rule | Exit | TRAIN period | TEST period | Test trades | Test win |
|---|---|---|---|---|---|

## GEX (only the 9 days in gex_log.csv, 273 dots - too few to trust, a first look)

| Reading | Dots | Win | Avg R |
|---|---|---|---|
| negative gamma | 273 | 66% | -4.53% |
| within 1 ATR of the wall you're trading into | 10 | 80% | +0.56% |
| more than 3 ATR from that wall | 239 | 64% | -5.13% |
| on the helpful side of the flip | 124 | 69% | -3.44% |
| on the wrong side of the flip | 149 | 64% | -5.44% |
