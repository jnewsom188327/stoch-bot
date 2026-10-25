# Edge hunt (2026-10-25 15:26 ET)

**Verdict:** 339 candidate rules. Best real out-of-sample net is +15.7% on pair vix_prior|high + wvf_roll_1m|event|follow (atm, target 20% / stop 10% / 10m). Luck benchmark (best out-of-sample net across 200 shuffles of the daily labels): +15.7%. Median of those per-shuffle bests: +15.4%. Rules expected to look at least this good by luck: 0.52.

A candidate must do all three: out-of-sample mean net above 0 after costs, mean net above its matched random book, and a positive fold mean in at least 3 of 5 folds. The top 30 below are ranked by out-of-sample net even when they are not candidates.

**Data span:** SPY, QQQ, 170 completed sessions with option prints, 2026-02-23 through 2026-10-23. Warmup bars before 2026-02-23 seed indicators, relative volume, and prior-day stats, and are not scored. VIX: Yahoo ^VIX + Cboe VIX. VIX data span 1990-01-02 through 2026-10-23 (9301 closes). Last date 2026-10-23.. Premium $0.45 to $0.80. Quick mode: no.

Family size: 97128 (2698 setups x 2 strikes x 18 exits). Benjamini-Hochberg uses that full family as N. Primary selection exit: target 15%, stop 20%, 10-minute time stop. The same chosen thresholds are then scored at 10% and 20% targets, stops 10%, 20%, and none, and time stops of 10 and 30 minutes.

## Candidates

| Rule | Strike | Exit | OOS net | Trades | Hit | t | Folds + | 95% CI | Random | Candidate |
|---|---|---|---:|---:|---:|---:|---:|---|---:|---|
| pair vix_chg_5d|high + ret_15|low|put | atm | target 20% / no stop / 10m | +14.4% | 9 | 100% | 47.22 | 4/5 | +13.8% to +15.0% | -6.1% | yes |
| pair vix_chg_5d|high + ret_15|low|put | atm | target 20% / no stop / 30m | +14.4% | 9 | 100% | 47.22 | 4/5 | +13.8% to +15.0% | -4.5% | yes |
| pair vix_chg_5d|high + div_5m|event|fade | atm | target 20% / no stop / 30m | +11.4% | 16 | 88% | 4.02 | 3/5 | +3.8% to +14.6% | -8.3% | yes |
| pair dow|4|gate + tod|9|put | 1otm | target 20% / no stop / 30m | +10.9% | 45 | 96% | 5.02 | 4/5 | +6.3% to +14.2% | -0.4% | yes |
| pair vix_chg_5d|low + tod|4|call | 1otm | target 20% / no stop / 30m | +10.4% | 17 | 88% | 3.45 | 3/5 | +2.9% to +14.8% | -3.2% | yes |
| pair vix_chg_5d|high + ret_15|low|put | atm | target 20% / stop 20% / 10m | +10.1% | 9 | 89% | 2.57 | 3/5 | +1.8% to +15.0% | -4.6% | yes |
| pair vix_chg_5d|high + ret_15|low|put | atm | target 20% / stop 20% / 30m | +10.1% | 9 | 89% | 2.57 | 3/5 | +2.6% to +15.0% | -4.4% | yes |
| pair vix_chg_5d|high + ret_15|low|put | atm | target 15% / no stop / 10m | +9.5% | 9 | 100% | 31.56 | 4/5 | +8.9% to +10.1% | -7.7% | yes |
| pair vix_chg_5d|high + ret_15|low|put | atm | target 15% / no stop / 30m | +9.5% | 9 | 100% | 31.56 | 4/5 | +8.8% to +10.1% | -6.8% | yes |
| pair or_size|high + vix_chg_5d|mag|fade | atm | target 20% / no stop / 30m | +9.0% | 12 | 92% | 2.38 | 3/5 | +3.0% to +15.5% | +6.9% | yes |
| pair vix_chg_5d|low + tod|2|call | 1otm | target 15% / no stop / 30m | +8.8% | 11 | 91% | 10.82 | 3/5 | +6.9% to +10.0% | +4.2% | yes |
| pair gap_vs_range|low + div_5m|event|fade | atm | target 20% / no stop / 30m | +8.2% | 19 | 89% | 1.59 | 3/5 | -3.9% to +14.7% | -5.3% | yes |
| pair gap_pct|low + div_1m|event|fade | atm | target 15% / no stop / 30m | +8.0% | 23 | 96% | 5.50 | 4/5 | +4.0% to +9.8% | -5.6% | yes |
| pair prior_range_pct|high + swing_3m|event|fade | atm | target 20% / no stop / 30m | +7.9% | 39 | 87% | 2.87 | 4/5 | +2.2% to +13.2% | -10.1% | yes |
| pair gap_pct|low + div_5m|event|fade | atm | target 20% / no stop / 30m | +7.9% | 18 | 89% | 1.45 | 3/5 | -6.4% to +14.8% | -9.0% | yes |
| pair prior_range_pct|high + tod|8|call | atm | target 20% / no stop / 30m | +7.8% | 27 | 85% | 2.60 | 4/5 | +1.1% to +12.8% | -1.5% | yes |
| pair dow|4|gate + ret_15|high|put | 1otm | target 20% / no stop / 30m | +7.6% | 97 | 85% | 3.90 | 5/5 | +3.7% to +11.7% | -3.1% | yes |
| pair vix_chg_5d|low + tod|2|call | 1otm | target 20% / no stop / 30m | +7.6% | 11 | 73% | 1.95 | 3/5 | -3.4% to +14.6% | -0.5% | yes |
| pair gap_pct|low + div_1m|event|fade | atm | target 20% / no stop / 30m | +7.4% | 23 | 87% | 1.89 | 4/5 | -2.4% to +14.2% | -5.8% | yes |
| pair vix_chg_5d|high + div_5m|event|fade | atm | target 15% / no stop / 30m | +7.0% | 16 | 94% | 2.77 | 3/5 | +0.4% to +9.8% | -7.6% | yes |
| pair vix_chg_5d|low + tod|4|call | 1otm | target 15% / no stop / 30m | +6.9% | 17 | 94% | 2.61 | 3/5 | +0.1% to +10.0% | -2.7% | yes |
| pair gap_vs_range|low + tod|10|put | 1otm | target 20% / no stop / 30m | +6.9% | 83 | 92% | 2.57 | 4/5 | +0.9% to +11.5% | -5.3% | yes |
| pair or_size|high + vwap_rvol|event|fade | atm | target 20% / no stop / 30m | +6.6% | 62 | 84% | 2.78 | 5/5 | +2.3% to +11.7% | -0.9% | yes |
| pair gap_vs_range|low + wvi_roll_3m|event|fade | atm | target 20% / no stop / 30m | +6.4% | 44 | 84% | 2.33 | 4/5 | -0.3% to +11.9% | -5.9% | yes |
| pair dow|4|gate + tod|9|put | 1otm | target 15% / no stop / 30m | +6.2% | 45 | 96% | 3.04 | 4/5 | +1.6% to +9.3% | -2.8% | yes |
| pair gap_vs_range|high + ret_5|low|call | atm | target 20% / no stop / 30m | +6.1% | 47 | 85% | 1.96 | 4/5 | -0.0% to +12.3% | -5.0% | yes |
| pair vix_chg_5d|low + tod|4|call | 1otm | target 20% / stop 20% / 10m | +6.1% | 17 | 65% | 2.54 | 3/5 | +0.3% to +11.9% | +0.7% | yes |
| pair prior_close_pos|low + ret_15|low|put | atm | target 20% / no stop / 10m | +5.9% | 26 | 88% | 1.40 | 3/5 | -2.2% to +14.4% | -5.6% | yes |
| pair prior_close_pos|high + macd_zero_3m|event|fade | atm | target 20% / no stop / 10m | +5.9% | 14 | 71% | 1.64 | 3/5 | -1.5% to +14.4% | -3.9% | yes |
| pair vix_chg_5d|high + ret_15|low|put | atm | target 15% / stop 20% / 10m | +5.7% | 9 | 89% | 1.64 | 3/5 | -2.3% to +10.1% | -4.8% | yes |
| pair vix_chg_5d|high + ret_15|low|put | atm | target 15% / stop 20% / 30m | +5.7% | 9 | 89% | 1.64 | 3/5 | -2.4% to +10.1% | -4.7% | yes |
| pair prior_close_pos|high + tod|2|put | 1otm | target 20% / stop 10% / 10m | +5.5% | 19 | 68% | 1.84 | 3/5 | -0.7% to +12.3% | -4.7% | yes |
| pair prior_close_pos|high + tod|2|put | 1otm | target 20% / stop 10% / 30m | +5.5% | 19 | 68% | 1.84 | 3/5 | -0.1% to +12.5% | -4.8% | yes |
| pair vix_chg_5d|low + tod|4|call | 1otm | target 20% / stop 20% / 30m | +5.4% | 17 | 76% | 1.82 | 3/5 | -1.3% to +12.0% | +0.6% | yes |
| pair gap_pct|low + vwap_atr|low|put | 1otm | target 20% / no stop / 30m | +5.3% | 78 | 85% | 1.78 | 3/5 | -1.6% to +11.1% | -0.6% | yes |
| pair vix_chg_5d|low + tod|4|call | 1otm | target 20% / no stop / 10m | +5.0% | 17 | 65% | 1.66 | 3/5 | -1.5% to +11.9% | -0.5% | yes |
| pair dow|4|gate + ret_15|high|put | 1otm | target 15% / no stop / 30m | +5.0% | 97 | 89% | 3.81 | 4/5 | +2.4% to +7.4% | -4.0% | yes |
| pair dow|2|gate + tod|10|put | 1otm | target 20% / no stop / 30m | +4.9% | 42 | 81% | 1.55 | 4/5 | -2.5% to +10.1% | -3.2% | yes |
| pair vix_prior|high + wvf_roll_3m|event|fade | 1otm | target 20% / no stop / 10m | +4.9% | 18 | 78% | 2.31 | 3/5 | +1.1% to +15.3% | -7.2% | yes |
| pair dow|0|gate + vix_chg_5d|mag|fade | atm | target 20% / no stop / 30m | +4.8% | 155 | 81% | 1.62 | 3/5 | -1.8% to +10.3% | +1.7% | yes |

299 more candidates are in the CSV.

## Top 30 by out-of-sample net

These are the highest out-of-sample means. A 'no' in the candidate column failed the bar above. They are not a trade list.

| Rule | Strike | Exit | OOS net | Trades | Hit | t | Folds + | 95% CI | Random | Candidate |
|---|---|---|---:|---:|---:|---:|---:|---|---:|---|
| pair vix_prior|high + wvf_roll_1m|event|follow | atm | target 20% / stop 10% / 10m | +15.7% | 1 | 100% |  | 1/5 | +15.7% to +15.7% | -5.6% | no |
| pair vix_prior|high + wvf_roll_1m|event|follow | atm | target 20% / stop 10% / 30m | +15.7% | 1 | 100% |  | 1/5 | +15.7% to +15.7% | -5.6% | no |
| pair vix_prior|high + wvf_roll_1m|event|follow | atm | target 20% / stop 20% / 10m | +15.7% | 1 | 100% |  | 1/5 | +15.7% to +15.7% | -7.1% | no |
| pair vix_prior|high + wvf_roll_1m|event|follow | atm | target 20% / stop 20% / 30m | +15.7% | 1 | 100% |  | 1/5 | +15.7% to +15.7% | -7.4% | no |
| pair vix_prior|high + wvf_roll_1m|event|follow | atm | target 20% / no stop / 10m | +15.7% | 1 | 100% |  | 1/5 | +15.7% to +15.7% | -4.7% | no |
| pair vix_prior|high + wvf_roll_1m|event|follow | atm | target 20% / no stop / 30m | +15.7% | 1 | 100% |  | 1/5 | +15.7% to +15.7% | -7.9% | no |
| pair dow|2|gate + tod|7|call | atm | target 20% / no stop / 30m | +15.7% | 2 | 100% |  | 1/5 | +15.7% to +15.7% | -3.6% | no |
| pair vix_prior|high + tod|2|put | 1otm | target 20% / stop 10% / 10m | +15.6% | 1 | 100% |  | 1/5 | +15.6% to +15.6% | -6.6% | no |
| pair vix_prior|high + tod|2|put | 1otm | target 20% / stop 10% / 30m | +15.6% | 1 | 100% |  | 1/5 | +15.6% to +15.6% | -6.6% | no |
| pair vix_prior|high + tod|2|put | 1otm | target 20% / stop 20% / 10m | +15.6% | 1 | 100% |  | 1/5 | +15.6% to +15.6% | -8.1% | no |
| pair vix_prior|high + tod|2|put | 1otm | target 20% / stop 20% / 30m | +15.6% | 1 | 100% |  | 1/5 | +15.6% to +15.6% | -8.9% | no |
| pair vix_prior|high + tod|2|put | 1otm | target 20% / no stop / 10m | +15.6% | 1 | 100% |  | 1/5 | +15.6% to +15.6% | -6.6% | no |
| pair vix_prior|high + tod|2|put | 1otm | target 20% / no stop / 30m | +15.6% | 1 | 100% |  | 1/5 | +15.6% to +15.6% | +4.8% | no |
| pair vix_prior|high + ret_30|high|put | 1otm | target 20% / stop 10% / 10m | +15.5% | 1 | 100% |  | 1/5 | +15.5% to +15.5% | +5.5% | no |
| pair vix_prior|high + ret_30|high|put | 1otm | target 20% / stop 10% / 30m | +15.5% | 1 | 100% |  | 1/5 | +15.5% to +15.5% | +5.5% | no |
| pair vix_prior|high + ret_30|high|put | 1otm | target 20% / stop 20% / 10m | +15.5% | 1 | 100% |  | 1/5 | +15.5% to +15.5% | +2.5% | no |
| pair vix_prior|high + ret_30|high|put | 1otm | target 20% / stop 20% / 30m | +15.5% | 1 | 100% |  | 1/5 | +15.5% to +15.5% | +2.5% | no |
| pair vix_prior|high + ret_30|high|put | 1otm | target 20% / no stop / 10m | +15.5% | 1 | 100% |  | 1/5 | +15.5% to +15.5% | +3.9% | no |
| pair vix_prior|high + ret_30|high|put | 1otm | target 20% / no stop / 30m | +15.5% | 1 | 100% |  | 1/5 | +15.5% to +15.5% | +11.3% | no |
| pair vix_prior|high + tod|12|put | 1otm | target 20% / stop 20% / 30m | +15.5% | 2 | 100% |  | 1/5 | +15.5% to +15.5% | +6.8% | no |
| pair vix_prior|high + tod|12|put | 1otm | target 20% / no stop / 30m | +15.5% | 2 | 100% |  | 1/5 | +15.5% to +15.5% | +4.3% | no |
| pair vix_prior|high + wvf_1m|high|put | atm | target 20% / stop 20% / 10m | +15.4% | 4 | 100% |  | 1/5 | +15.4% to +15.4% | +0.4% | no |
| pair vix_prior|high + wvf_1m|high|put | atm | target 20% / stop 20% / 30m | +15.4% | 4 | 100% |  | 1/5 | +15.4% to +15.4% | +0.4% | no |
| pair vix_prior|high + wvf_1m|high|put | atm | target 20% / no stop / 10m | +15.4% | 4 | 100% |  | 1/5 | +15.4% to +15.4% | -4.2% | no |
| pair vix_prior|high + wvf_1m|high|put | atm | target 20% / no stop / 30m | +15.4% | 4 | 100% |  | 1/5 | +15.4% to +15.4% | -3.1% | no |
| pair dow|2|gate + vix_chg_5d|mag|follow | atm | target 20% / stop 10% / 10m | +15.3% | 1 | 100% |  | 1/5 | +15.3% to +15.3% | +9.2% | no |
| pair dow|2|gate + vix_chg_5d|mag|follow | atm | target 20% / stop 10% / 30m | +15.3% | 1 | 100% |  | 1/5 | +15.3% to +15.3% | +9.2% | no |
| pair dow|2|gate + vix_chg_5d|mag|follow | atm | target 20% / stop 20% / 10m | +15.3% | 1 | 100% |  | 1/5 | +15.3% to +15.3% | +7.2% | no |
| pair dow|2|gate + vix_chg_5d|mag|follow | atm | target 20% / stop 20% / 30m | +15.3% | 1 | 100% |  | 1/5 | +15.3% to +15.3% | +7.2% | no |
| pair dow|2|gate + vix_chg_5d|mag|follow | atm | target 20% / no stop / 10m | +15.3% | 1 | 100% |  | 1/5 | +15.3% to +15.3% | +6.0% | no |

## What was searched

Singles cover each daily and intraday feature as a high bucket and a low bucket, both call and put; each signed feature as follow and as fade; day of week; each 30-minute clock bucket; squeeze on and off; and every reversal event as follow and fade. Pairs are every daily-context gate with every setup that uses a different feature, plus each reversal event with a predeclared intraday gate (relative volume, Williams VIX Fix level, squeeze length or on, VWAP stretch, EMA slope, 5-minute return) when that gate is not the same measurement as the event. This is not the cross of every feature with every other feature.

Reversal events, all causal: MACD(12,26,9) histogram zero-cross, shrink, and color flip on 1-minute and 3-minute bars; regular bullish/bearish divergence of price vs MACD histogram on 1-minute, 3-minute, and 5-minute bars; 5-bar-left/5-bar-right swing pivots on 1-minute and 3-minute bars, flagged at the confirmation bar; VWAP stretch in ATR units with relative volume at least 1.5x the same-minute 20-day median; Williams VIX Fix (and the greed mirror) spike then rollover on 1-minute and 3-minute bars; TTM squeeze release with a momentum color flip on 1-minute and 3-minute bars. Follow trades the event's direction. Fade trades against it. A pivot or a divergence is not tradable until the right-side bars have closed.

Costs match scalp_real: half-spread per side is max(1 cents, 0.5% of premium), commission $0.65 per contract per side, one contract. Entry is the next real option open after the signal bar (that minute, or the next minute if it has no print), plus the half-spread. Exit is the bid-side proxy from scalp_real.simulate_trade. Premium band $0.45 to $0.80. Strikes: 1otm, atm. Cooldown 10 minutes per rule per day. Calls win if call and put both fire on the same minute. Walk-forward: sessions split into 6 chronological blocks; the first block is train only; each of the 5 later blocks is an out-of-sample fold trained on every earlier block. Quantile cuts and fixed grids (1.0, 1.5, 2.0 ATR, VIX-fix levels 60, 75, 90) are chosen only on that training prefix, by mean net on the 15%/20%/10-minute exit, with at least the minimum train trade count. Matched random uses the same days, the same strike and premium band, the same exit, and the rule's own entry-clock distribution (a one-minute spike falls back to its 30-minute bucket). Day-clustered t and a day-resampled 95% bootstrap describe the pooled out-of-sample trades. The luck benchmark permutes daily-feature labels across sessions (200 times unless quick or overridden), refits every daily-context rule, and leaves intraday rules as they were.

## Limits

Long premium only, one contract, no spreads. A 30-minute time stop can still be open when the next entry fires 10 minutes later, so trades can overlap; the number above is per trade, not a one-position account path. The half-spread is a proxy, not the quote. Thresholds are fit on one primary exit per strike, then reused for the other exits, and those other exits still count in the family. Pairs are daily context with a setup, and reversal events with a short gate list, not every pair of indicators. A rule that trades almost every eligible minute on a 'good' day will look like its matched random, because the random book is drawn on those same days at the same clock. Its expectancy is still in the top 30 and the CSV. The candidate flag is the stricter test: better minutes than that random book. Shuffling daily labels does not break an intraday event, so the luck benchmark is a floor under the best intraday result and a null for the daily-context rules. VIX is the prior daily close (FRED VIXCLS, then the Yahoo chart, then Cboe, then data/vix_daily.csv), not an intraday VIX. Relative volume needs 20 prior sessions; early days stay blank. This is a search of a predeclared family. It is not a promise that a candidate will keep working.

Data only. Research tool, not trading advice. No order is sent.
