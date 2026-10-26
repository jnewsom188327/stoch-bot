# Fear-greed fade PERFECT

The rule chosen on the first 75% of sessions is tf1_turn_mom_g95_f20__tod_1200__be_a15_d0. Its held-out mean net is 7.6% per trade across 68 fills and 26 of 30 held-out sessions.

Yes. tf1_turn_mom_g95_f20__tod_1200__be_a15_d0 has a positive held-out net, beats a random entry with the same exit, and fires on most held-out sessions.

This is the one rule the train sample picked. It is still one study, not a reason to change the live bot.

Family scored this run: 111888 configs (111 entries × 1008 exits). The predeclared family is 111888 configs.

Sessions 2026-05-05 through 2026-10-23 (120 sessions). Held out: the last 30 sessions. Train gate: at least 100 fills and 60 distinct days.

Benjamini-Hochberg q uses the day-clustered p of (signal net − random net) under the same exit, over all 111888 configs. q is a screen on the full sample. The fold table is the out-of-sample result.

Train-qualified rules: 81648. Of those, 2488 have a positive held-out point estimate.

## Top 15

These are train-qualified rules sorted by held-out net per trade. Sorting uses the holdout, so the top row is not a fresh discovery. The train-only choice is named in the verdict. Sessions covered sit next to the net.

| rule | hold net | hold fills | hold sessions | hold win | random net | paired edge | per $1000 | q |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tf1_turn_mom_g95_f20__tod_1000__stall_n3_d0 | 119.2% | 59 | 27/30 | 49.2% | 55.0% | 64.2% | 1192.0 | 0.629 |
| tf1_turn_mom_g95_f20__tod_1000__stall_n3_d1 | 119.2% | 59 | 27/30 | 49.2% | 55.1% | 64.1% | 1191.9 | 0.630 |
| tf1_turn_mom_g95_f20__tod_1000__stall_n5_d0 | 117.9% | 59 | 27/30 | 49.2% | 55.3% | 62.6% | 1178.7 | 0.650 |
| tf1_turn_mom_g95_f20__tod_1000__stall_n5_d1 | 117.8% | 59 | 27/30 | 49.2% | 55.3% | 62.5% | 1178.3 | 0.649 |
| tf1_turn_mom_g95_f20__tod_1000__stall_n10_d1 | 116.5% | 59 | 27/30 | 49.2% | 51.6% | 64.9% | 1164.7 | 0.628 |
| tf1_turn_mom_g95_f20__tod_1000__stall_n10_d0 | 116.5% | 59 | 27/30 | 49.2% | 51.6% | 64.9% | 1164.6 | 0.629 |
| tf1_turn_mom_g95_f20__tod_1000__scale_s25_y10_d1 | 60.8% | 59 | 27/30 | 54.2% | 25.7% | 35.1% | 607.9 | 0.653 |
| tf1_turn_mom_g95_f20__tod_1000__scale_s25_y15_d1 | 60.8% | 59 | 27/30 | 54.2% | 25.7% | 35.1% | 607.9 | 0.653 |
| tf1_turn_mom_g95_f20__tod_1000__scale_s25_y20_d1 | 60.8% | 59 | 27/30 | 54.2% | 25.7% | 35.1% | 607.9 | 0.653 |
| tf1_turn_mom_g95_f20__tod_1000__scale_s15_y10_d1 | 58.6% | 59 | 27/30 | 52.5% | 27.5% | 31.1% | 586.1 | 0.689 |
| tf1_turn_mom_g95_f20__tod_1000__scale_s15_y15_d1 | 58.6% | 59 | 27/30 | 52.5% | 27.5% | 31.1% | 586.1 | 0.689 |
| tf1_turn_mom_g95_f20__tod_1000__scale_s15_y20_d1 | 58.6% | 59 | 27/30 | 52.5% | 27.5% | 31.1% | 586.1 | 0.689 |
| tf1_turn_mom_g95_f20__tod_1000__scale_s20_y10_d1 | 58.4% | 59 | 27/30 | 52.5% | 25.3% | 33.1% | 583.9 | 0.645 |
| tf1_turn_mom_g95_f20__tod_1000__scale_s20_y15_d1 | 58.4% | 59 | 27/30 | 52.5% | 25.3% | 33.1% | 583.9 | 0.645 |
| tf1_turn_mom_g95_f20__tod_1000__scale_s20_y20_d1 | 58.4% | 59 | 27/30 | 52.5% | 25.3% | 33.1% | 583.9 | 0.645 |

## Marginal effect of each filter

Each row changes one thing from `tf1_turn_mom_g95_f20` and uses the reference exit `fix_tp15_sl15_t30_d0` (target +15%, stop -15%, 30 minutes). Mean net, win rate, and sessions are the full sample. This section describes the sample. It is not the held-out rank.

### base

| config | fills | sessions | mean net | win rate | vs base |
| --- | --- | --- | --- | --- | --- |
| tf1_turn_mom_g95_f20 | 1625 | 120/120 | -6.8% | 45.9% | -0.0% |
### tf

| config | fills | sessions | mean net | win rate | vs base |
| --- | --- | --- | --- | --- | --- |
| tf2_turn_mom_g95_f20 | 870 | 120/120 | -7.9% | 41.5% | -1.1% |
| tf3_turn_mom_g95_f20 | 598 | 119/120 | -7.7% | 42.1% | -0.9% |
| tf5_turn_mom_g95_f20 | 458 | 112/120 | -7.2% | 42.1% | -0.4% |
### G

| config | fills | sessions | mean net | win rate | vs base |
| --- | --- | --- | --- | --- | --- |
| tf1_turn_mom_g75_f20 | 2300 | 120/120 | -7.5% | 43.5% | -0.7% |
| tf1_turn_mom_g80_f20 | 2150 | 120/120 | -7.4% | 44.0% | -0.6% |
| tf1_turn_mom_g85_f20 | 1981 | 120/120 | -7.4% | 44.1% | -0.6% |
| tf1_turn_mom_g90_f20 | 1814 | 120/120 | -7.3% | 44.2% | -0.5% |
| tf1_turn_mom_g100_f20 | 1404 | 120/120 | -7.2% | 44.4% | -0.4% |
### F

| config | fills | sessions | mean net | win rate | vs base |
| --- | --- | --- | --- | --- | --- |
| tf1_turn_mom_g95_f0 | 1 | 1/120 | -37.5% | 0.0% | -30.7% |
| tf1_turn_mom_g95_f5 | 403 | 116/120 | -7.7% | 42.9% | -0.9% |
| tf1_turn_mom_g95_f10 | 1000 | 120/120 | -7.1% | 44.6% | -0.3% |
| tf1_turn_mom_g95_f15 | 1384 | 120/120 | -7.1% | 45.1% | -0.3% |
| tf1_turn_mom_g95_f25 | 1771 | 120/120 | -7.0% | 45.0% | -0.2% |
| tf1_turn_mom_g95_f30 | 1830 | 120/120 | -7.1% | 44.6% | -0.3% |
| tf1_turn_mom_g95_f35 | 1882 | 120/120 | -7.0% | 44.8% | -0.2% |
### pinned

| config | fills | sessions | mean net | win rate | vs base |
| --- | --- | --- | --- | --- | --- |
| tf1_turn_mom_g95_f20_k2 | 1077 | 120/120 | -7.1% | 44.4% | -0.3% |
| tf1_turn_mom_g95_f20_k3 | 712 | 120/120 | -6.9% | 44.8% | -0.1% |
| tf1_turn_mom_g95_f20_k4 | 449 | 116/120 | -6.5% | 46.8% | 0.3% |
| tf1_turn_mom_g95_f20_k5 | 276 | 100/120 | -6.4% | 45.7% | 0.4% |
### turn

| config | fills | sessions | mean net | win rate | vs base |
| --- | --- | --- | --- | --- | --- |
| tf1_drop1_mom_g95_f20 | 1548 | 120/120 | -6.8% | 46.1% | 0.0% |
| tf1_drop2_mom_g95_f20 | 1471 | 120/120 | -7.0% | 45.6% | -0.2% |
| tf1_drop3_mom_g95_f20 | 1409 | 120/120 | -6.9% | 45.6% | -0.1% |
| tf1_cross_mom_g95_f20 | 994 | 120/120 | -7.2% | 43.6% | -0.4% |
| tf1_within1_mom_g95_f20 | 1722 | 120/120 | -7.0% | 45.5% | -0.2% |
| tf1_within2_mom_g95_f20 | 1733 | 120/120 | -7.0% | 45.3% | -0.2% |
| tf1_within3_mom_g95_f20 | 1730 | 120/120 | -7.0% | 45.5% | -0.2% |
### mom

| config | fills | sessions | mean net | win rate | vs base |
| --- | --- | --- | --- | --- | --- |
| tf1_turn_sq_g95_f20 | 983 | 120/120 | -7.3% | 43.3% | -0.5% |
| tf1_turn_macd_g95_f20 | 1587 | 120/120 | -6.8% | 45.7% | -0.1% |
### squeeze

| config | fills | sessions | mean net | win rate | vs base |
| --- | --- | --- | --- | --- | --- |
| tf1_turn_mom_g95_f20_sqon | 121 | 74/120 | -8.9% | 40.5% | -2.1% |
| tf1_turn_mom_g95_f20_sqoff | 1415 | 120/120 | -6.8% | 46.1% | 0.0% |
| tf1_turn_mom_g95_f20_sqrel | 308 | 111/120 | -7.4% | 44.2% | -0.6% |
### vwap

| config | fills | sessions | mean net | win rate | vs base |
| --- | --- | --- | --- | --- | --- |
| tf1_turn_mom_g95_f20_vwap05 | 934 | 120/120 | -7.1% | 44.2% | -0.3% |
| tf1_turn_mom_g95_f20_vwap10 | 854 | 120/120 | -7.0% | 44.8% | -0.2% |
| tf1_turn_mom_g95_f20_vwap15 | 787 | 120/120 | -6.6% | 46.3% | 0.2% |
| tf1_turn_mom_g95_f20_vwap20 | 705 | 120/120 | -7.1% | 45.1% | -0.3% |
### band

| config | fills | sessions | mean net | win rate | vs base |
| --- | --- | --- | --- | --- | --- |
| tf1_turn_mom_g95_f20_band | 857 | 120/120 | -7.0% | 44.8% | -0.2% |
### rsi

| config | fills | sessions | mean net | win rate | vs base |
| --- | --- | --- | --- | --- | --- |
| tf1_turn_mom_g95_f20_rsi | 281 | 105/120 | -6.3% | 44.5% | 0.5% |
### stoch

| config | fills | sessions | mean net | win rate | vs base |
| --- | --- | --- | --- | --- | --- |
| tf1_turn_mom_g95_f20_stoch | 911 | 120/120 | -6.5% | 47.3% | 0.3% |
### cci

| config | fills | sessions | mean net | win rate | vs base |
| --- | --- | --- | --- | --- | --- |
| tf1_turn_mom_g95_f20_cci | 1138 | 120/120 | -7.2% | 45.3% | -0.4% |
### candle

| config | fills | sessions | mean net | win rate | vs base |
| --- | --- | --- | --- | --- | --- |
| tf1_turn_mom_g95_f20_wick | 288 | 111/120 | -6.4% | 47.2% | 0.4% |
| tf1_turn_mom_g95_f20_engulf | 422 | 117/120 | -7.2% | 44.8% | -0.4% |
### htf

| config | fills | sessions | mean net | win rate | vs base |
| --- | --- | --- | --- | --- | --- |
| tf1_turn_mom_g95_f20_htf | 119 | 70/120 | -5.0% | 47.1% | 1.8% |
### rvol

| config | fills | sessions | mean net | win rate | vs base |
| --- | --- | --- | --- | --- | --- |
| tf1_turn_mom_g95_f20__rvol_low | 1272 | 120/120 | -7.1% | 45.9% | -0.3% |
| tf1_turn_mom_g95_f20__rvol_mid | 190 | 82/120 | -6.1% | 43.2% | 0.7% |
| tf1_turn_mom_g95_f20__rvol_high | 163 | 70/120 | -5.2% | 49.1% | 1.6% |
### prior_day

| config | fills | sessions | mean net | win rate | vs base |
| --- | --- | --- | --- | --- | --- |
| tf1_turn_mom_g95_f20__above_pdh | 492 | 61/120 | -8.6% | 41.9% | -1.8% |
| tf1_turn_mom_g95_f20__below_pdl | 447 | 56/120 | -5.8% | 47.9% | 1.0% |
| tf1_turn_mom_g95_f20__above_pdc | 817 | 93/120 | -7.8% | 43.8% | -1.0% |
| tf1_turn_mom_g95_f20__below_pdc | 806 | 85/120 | -5.8% | 47.9% | 1.0% |
### orb

| config | fills | sessions | mean net | win rate | vs base |
| --- | --- | --- | --- | --- | --- |
| tf1_turn_mom_g95_f20__orb_break | 524 | 115/120 | -7.0% | 45.6% | -0.2% |
| tf1_turn_mom_g95_f20__orb_hold | 47 | 37/120 | -9.3% | 36.2% | -2.5% |
### day_extreme

| config | fills | sessions | mean net | win rate | vs base |
| --- | --- | --- | --- | --- | --- |
| tf1_turn_mom_g95_f20__near_high | 21 | 17/120 | -3.6% | 47.6% | 3.2% |
| tf1_turn_mom_g95_f20__near_low | 7 | 7/120 | 0.3% | 57.1% | 7.1% |
### gap

| config | fills | sessions | mean net | win rate | vs base |
| --- | --- | --- | --- | --- | --- |
| tf1_turn_mom_g95_f20__gap_up | 806 | 66/120 | -7.1% | 45.0% | -0.3% |
| tf1_turn_mom_g95_f20__gap_down | 601 | 52/120 | -6.0% | 47.3% | 0.8% |
| tf1_turn_mom_g95_f20__gap_flat | 218 | 27/120 | -7.8% | 45.4% | -1.0% |
### trend

| config | fills | sessions | mean net | win rate | vs base |
| --- | --- | --- | --- | --- | --- |
| tf1_turn_mom_g95_f20__trend_up | 826 | 111/120 | -7.1% | 46.0% | -0.3% |
| tf1_turn_mom_g95_f20__trend_down | 682 | 103/120 | -6.6% | 45.7% | 0.2% |
| tf1_turn_mom_g95_f20__trend_flat | 117 | 65/120 | -5.3% | 46.2% | 1.5% |
### agree

| config | fills | sessions | mean net | win rate | vs base |
| --- | --- | --- | --- | --- | --- |
| tf1_turn_mom_g95_f20__spyqqq | 878 | 117/120 | -6.7% | 46.0% | 0.1% |
### vix

| config | fills | sessions | mean net | win rate | vs base |
| --- | --- | --- | --- | --- | --- |
| tf1_turn_mom_g95_f20__vix_lt14 | 0 | 0/120 | n/a | n/a | n/a |
| tf1_turn_mom_g95_f20__vix_14_16 | 656 | 49/120 | -9.0% | 42.5% | -2.2% |
| tf1_turn_mom_g95_f20__vix_16_18 | 637 | 47/120 | -5.8% | 48.4% | 1.0% |
| tf1_turn_mom_g95_f20__vix_18_22 | 317 | 23/120 | -4.7% | 47.3% | 2.1% |
| tf1_turn_mom_g95_f20__vix_22p | 15 | 1/120 | 1.1% | 60.0% | 7.9% |
### vix_change

| config | fills | sessions | mean net | win rate | vs base |
| --- | --- | --- | --- | --- | --- |
| tf1_turn_mom_g95_f20__vix_up | 543 | 41/120 | -7.4% | 45.7% | -0.6% |
| tf1_turn_mom_g95_f20__vix_down | 703 | 51/120 | -5.8% | 47.5% | 1.0% |
| tf1_turn_mom_g95_f20__vix_flat | 379 | 28/120 | -7.7% | 43.3% | -0.9% |
### dow

| config | fills | sessions | mean net | win rate | vs base |
| --- | --- | --- | --- | --- | --- |
| tf1_turn_mom_g95_f20__dow_mon | 280 | 22/120 | -7.9% | 43.9% | -1.1% |
| tf1_turn_mom_g95_f20__dow_tue | 322 | 25/120 | -7.9% | 46.0% | -1.1% |
| tf1_turn_mom_g95_f20__dow_wed | 355 | 25/120 | -4.5% | 49.9% | 2.3% |
| tf1_turn_mom_g95_f20__dow_thu | 338 | 25/120 | -6.4% | 46.2% | 0.4% |
| tf1_turn_mom_g95_f20__dow_fri | 330 | 23/120 | -7.7% | 43.0% | -0.9% |
### tod

| config | fills | sessions | mean net | win rate | vs base |
| --- | --- | --- | --- | --- | --- |
| tf1_turn_mom_g95_f20__tod_0935 | 141 | 87/120 | -3.2% | 47.5% | 3.6% |
| tf1_turn_mom_g95_f20__tod_1000 | 232 | 109/120 | -4.4% | 45.3% | 2.4% |
| tf1_turn_mom_g95_f20__tod_1100 | 252 | 107/120 | -2.1% | 56.3% | 4.7% |
| tf1_turn_mom_g95_f20__tod_1200 | 269 | 111/120 | -4.1% | 52.4% | 2.7% |
| tf1_turn_mom_g95_f20__tod_1300 | 267 | 111/120 | -7.7% | 46.1% | -0.9% |
| tf1_turn_mom_g95_f20__tod_1400 | 246 | 110/120 | -8.5% | 44.3% | -1.7% |
| tf1_turn_mom_g95_f20__tod_1500 | 218 | 104/120 | -17.5% | 27.1% | -10.7% |
### since

| config | fills | sessions | mean net | win rate | vs base |
| --- | --- | --- | --- | --- | --- |
| tf1_turn_mom_g95_f20__since_lt20 | 182 | 89/120 | -8.2% | 40.1% | -1.4% |
| tf1_turn_mom_g95_f20__since_20_40 | 520 | 118/120 | -8.0% | 44.6% | -1.2% |
| tf1_turn_mom_g95_f20__since_40_60 | 319 | 109/120 | -6.6% | 47.0% | 0.2% |
| tf1_turn_mom_g95_f20__since_60p | 604 | 120/120 | -5.5% | 48.2% | 1.3% |
### nth

| config | fills | sessions | mean net | win rate | vs base |
| --- | --- | --- | --- | --- | --- |
| tf1_turn_mom_g95_f20__nth_1 | 238 | 120/120 | -3.2% | 49.2% | 3.6% |
| tf1_turn_mom_g95_f20__nth_2 | 103 | 75/120 | -3.5% | 52.4% | 3.3% |
| tf1_turn_mom_g95_f20__nth_3p | 1284 | 120/120 | -7.7% | 44.8% | -0.9% |
### side

| config | fills | sessions | mean net | win rate | vs base |
| --- | --- | --- | --- | --- | --- |
| tf1_turn_mom_g95_f20__side_call | 813 | 120/120 | -7.5% | 44.2% | -0.7% |
| tf1_turn_mom_g95_f20__side_put | 812 | 120/120 | -6.1% | 47.7% | 0.7% |
### prev

| config | fills | sessions | mean net | win rate | vs base |
| --- | --- | --- | --- | --- | --- |
| tf1_turn_mom_g95_f20__prev_win | 744 | 120/120 | -6.9% | 45.4% | -0.1% |
| tf1_turn_mom_g95_f20__prev_loss | 877 | 120/120 | -6.8% | 46.2% | 0.0% |
### regime

| config | fills | sessions | mean net | win rate | vs base |
| --- | --- | --- | --- | --- | --- |
| tf1_turn_mom_g95_f20__regime_trend | 469 | 48/120 | -7.1% | 43.9% | -0.3% |
| tf1_turn_mom_g95_f20__regime_range | 1156 | 98/120 | -6.7% | 46.7% | 0.1% |
### event

| config | fills | sessions | mean net | win rate | vs base |
| --- | --- | --- | --- | --- | --- |
| tf1_turn_mom_g95_f20__event_yes | 133 | 9/120 | -6.5% | 43.6% | 0.3% |
| tf1_turn_mom_g95_f20__event_no | 1492 | 111/120 | -6.8% | 46.1% | -0.0% |
### strike

| config | fills | sessions | mean net | win rate | vs base |
| --- | --- | --- | --- | --- | --- |
| tf1_turn_mom_g95_f20__atm | 1633 | 120/120 | -3.1% | 50.3% | 3.7% |
| tf1_turn_mom_g95_f20__2otm | 1564 | 120/120 | -11.5% | 37.7% | -4.7% |
### dte

| config | fills | sessions | mean net | win rate | vs base |
| --- | --- | --- | --- | --- | --- |
| tf1_turn_mom_g95_f20__dte1 | 1612 | 119/120 | -1.9% | 45.1% | 4.9% |
### premium

| config | fills | sessions | mean net | win rate | vs base |
| --- | --- | --- | --- | --- | --- |
| tf1_turn_mom_g95_f20__prem_020_040 | 303 | 97/120 | -10.8% | 43.9% | -4.0% |
| tf1_turn_mom_g95_f20__prem_030_060 | 395 | 109/120 | -7.6% | 50.4% | -0.8% |
| tf1_turn_mom_g95_f20__prem_040_080 | 479 | 114/120 | -4.4% | 54.3% | 2.4% |
| tf1_turn_mom_g95_f20__prem_060_100 | 454 | 114/120 | -2.3% | 56.4% | 4.5% |
| tf1_turn_mom_g95_f20__prem_100_200 | 422 | 110/120 | -2.9% | 48.3% | 3.9% |
| tf1_turn_mom_g95_f20__prem_200p | 124 | 46/120 | -3.6% | 43.5% | 3.2% |
### cost

| config | fills | sessions | mean net | win rate | vs base |
| --- | --- | --- | --- | --- | --- |
| tf1_turn_mom_g95_f20__mid1c | 1625 | 120/120 | -6.8% | 45.9% | 0.0% |
### spread

| config | fills | sessions | mean net | win rate | vs base |
| --- | --- | --- | --- | --- | --- |
| tf1_turn_mom_g95_f20__spread1 | 545 | 110/120 | -3.0% | 47.2% | 3.8% |
| tf1_turn_mom_g95_f20__spread2 | 1095 | 119/120 | -3.1% | 50.9% | 3.7% |
| tf1_turn_mom_g95_f20__spread5 | 1500 | 120/120 | -4.9% | 49.7% | 1.9% |
### entry_delay

| config | fills | sessions | mean net | win rate | vs base |
| --- | --- | --- | --- | --- | --- |
| tf1_turn_mom_g95_f20__edelay1 | 1618 | 120/120 | -7.4% | 43.9% | -0.6% |
| tf1_turn_mom_g95_f20__edelay2 | 1611 | 120/120 | -7.9% | 42.2% | -1.1% |

## Exit families on the base entry

In-sample, on the base signal only. The best cell in a family is the highest full-sample mean, which is a description, not a selection.

| family | rules | best mean | best id | median mean |
| --- | --- | --- | --- | --- |
| fixed | 896 | -6.2% | fix_tp15_sl25_t20_d1 | -7.3% |
| trail | 40 | -8.0% | trail_a10_y5_d1 | -9.4% |
| breakeven | 4 | -7.1% | be_a10_d1 | -7.9% |
| scale | 18 | -7.7% | scale_s15_y10_d1 | -8.9% |
| signal | 8 | -6.5% | sig_band_d1 | -8.6% |
| stall | 6 | -7.9% | stall_n10_d1 | -8.0% |
| underlying | 36 | -6.2% | und_k20_m50_t60_d0 | -6.4% |

## Stability

Train-chosen exit `be_a15_d0` on `tf1_turn_mom_g95_f20__tod_1200`. Mean net on the train sample:

| arm \ delay | 0 | 1 |
| --- | --- | --- |
| 10% | 6.2% | 6.2% |
| 15% | 7.2% | 6.6% |

The same grid on the held-out sessions:

| arm \ delay | 0 | 1 |
| --- | --- | --- |
| 10% | 10.6% | 11.6% |
| 15% | 7.6% | 7.6% |

Neighbours are the next step on each axis of the exit, same entry, same other settings. Every neighbour has a positive train mean.

## Walk-forward

Five expanding folds. Block 0 is train only. A fold chooses on its train days and is scored only on the following test days. Early folds cannot reach 60 distinct train days. Those folds say the candidate minimum was not met. When that note is on the row, the named rule is only the highest train mean. It was not selected.

| fold | chosen | note | train n | train days | train net | test n | test net | test random | test paired |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | tf1_turn_mom_g95_f20__near_low__stall_n3_d0 | candidate minimum was not met | 2 | 2 | 139.0% | 1 | -100.1% | -100.5% | 0.4% |
| 2 | tf1_turn_mom_g95_f20__vix_22p__stall_n10_d1 | candidate minimum was not met | 15 | 1 | 133.6% | 0 | n/a | n/a | n/a |
| 3 | tf1_turn_mom_g95_f20__nth_1__stall_n10_d1 | chosen on train | 120 | 60 | 14.4% | 38 | -55.2% | -41.7% | -12.5% |
| 4 | tf1_turn_mom_g95_f20__tod_1200__be_a15_d0 | chosen on train | 178 | 76 | 11.1% | 48 | -5.5% | 4.0% | -9.5% |
| 5 | tf1_turn_mom_g95_f20__tod_1000__stall_n10_d1 | chosen on train | 189 | 90 | 14.7% | 43 | 86.7% | 37.5% | 49.2% |

## Luck

20 block shuffles of 5 sessions. The train-chosen held-out net is 7.6%. 6 of 20 shuffles reached a test net at least that high. The best shuffled test net was 61.5%.

## Trades from 2026-10-19 through 2026-10-23

Up to 25 fills of `tf1_turn_mom_g95_f20__tod_1200__be_a15_d0` on those dates. Net is that rule's net percent.

| day | symbol | time | side | greed | fear | squeeze | mom | net |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-10-19 | SPY | 09:56 | call | 5.1 | 99.7 | off | -1.03 | -2.6% |
| 2026-10-19 | SPY | 10:36 | call | 8.8 | 87.5 | off | -0.78 | -4.4% |
| 2026-10-19 | SPY | 12:05 | call | 22.9 | 78.9 | off | -0.81 | -93.4% |
| 2026-10-19 | SPY | 13:20 | put | 73.5 | 30.3 | on | 0.13 | -7.9% |
| 2026-10-19 | SPY | 14:16 | put | 92.8 | 13.0 | off | 0.29 | -10.3% |
| 2026-10-19 | SPY | 14:37 | call | 39.2 | 86.6 | off | -0.57 | -9.7% |
| 2026-10-19 | QQQ | 10:03 | call | 4.6 | 95.8 | off | -2.21 | -1.8% |
| 2026-10-19 | QQQ | 11:30 | put | 93.9 | 23.0 | off | 1.18 | -2.7% |
| 2026-10-19 | QQQ | 12:05 | call | 21.0 | 83.1 | off | -1.03 | -98.5% |
| 2026-10-19 | QQQ | 13:20 | put | 72.0 | 21.1 | on | 0.15 | -4.1% |
| 2026-10-19 | QQQ | 13:50 | call | 30.0 | 91.8 | off | -0.54 | -6.7% |
| 2026-10-19 | QQQ | 14:37 | call | 50.6 | 79.1 | off | -0.63 | 113.4% |
| 2026-10-20 | SPY | 10:01 | put | 98.8 | 13.4 | off | 2.15 | -92.5% |
| 2026-10-20 | SPY | 11:08 | call | 4.4 | 97.9 | off | -0.36 | -101.5% |
| 2026-10-20 | SPY | 12:39 | put | 97.9 | 9.6 | off | 0.76 | -4.6% |
| 2026-10-20 | SPY | 13:33 | put | 82.0 | 4.4 | off | 0.60 | -6.5% |
| 2026-10-20 | SPY | 14:07 | call | 12.5 | 97.2 | off | -0.29 | -9.2% |
| 2026-10-20 | SPY | 14:28 | call | 14.9 | 71.9 | off | -0.21 | -81.0% |
| 2026-10-20 | SPY | 14:57 | put | 88.5 | 9.6 | off | 0.37 | -14.3% |
| 2026-10-20 | QQQ | 10:03 | put | 99.5 | 4.3 | off | 4.07 | -86.3% |
| 2026-10-20 | QQQ | 11:16 | call | 29.0 | 82.2 | off | -1.67 | -2.2% |
| 2026-10-20 | QQQ | 12:56 | call | 36.6 | 83.2 | off | -1.08 | -3.5% |
| 2026-10-20 | QQQ | 14:07 | call | 13.4 | 85.2 | off | -0.20 | -5.1% |
| 2026-10-20 | QQQ | 14:40 | call | 20.3 | 89.3 | off | -0.71 | -5.1% |
| 2026-10-21 | SPY | 10:14 | call | 11.8 | 84.6 | off | -1.41 | -3.1% |

## How to read the tests

Costs are fixed: half-spread max(1 cent, 0.5% of the print), commission $0.65 a side. At the base book's median print, a +15%/−15% target needs about a 72.0% target-exit rate to break even. The reference exit's full-sample target-exit rate on the base signal is 50.1%. A peak bid of +15% is a different test from a resting +15% target. This study scores the resting order.
The same bar checks the stop before the target. A trail checks the low against the peak from earlier bars, then lets the high raise the peak.
Delay 1 sells the next minute's open. That is the phone-delay copy of each rule. If there is no next bar, the sale is the current close.
There is no quoted spread in the minute bars. Ask versus mid+1 cent, and the spread filter, are cost-model assumptions. The spread filter is a premium floor in disguise (1% keeps prints at or above $1, 2% at or above $0.50, 5% at or above $0.20).
Random entries use the same exit, the same strike, the same DTE, and the same delay. Premium-band and spread filters also require the random fill to pass, so a cheap random is not compared with an expensive signal. Other filters are not forced onto the random entry. That is what separates the entry from the exit.
Per $1,000 notional is 10 times the net percent, because the position is sized as $1,000 of debit. Per contract is the dollar result of one option.
VIX9D and a VIX term proxy were not in the repo and were not scored.
GEX levels were not in this checkout for these sessions, so GEX was not scored.
VIX buckets use the prior session's close. VIX change is that prior close minus the one before it. Today's VIX change is not known at the entry.
The first signal of a day counts as 60+ minutes since the last signal. Minutes-since is measured on the raw stream, before the 20-minute cooldown, so a kept signal can still sit in the under-20 bucket when a skipped signal stands between it and the previous kept signal.
Full-sample paired comparison: the base reference exit mean is -6.8% versus random -6.2% (q 0.759).
Runtime 10.9 minutes. Symbols SPY, QQQ.

Data only. Research tool, not trading advice. No orders. A short sample is not a reason to change the live bot.
