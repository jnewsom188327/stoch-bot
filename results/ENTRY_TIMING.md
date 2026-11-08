# Entry timing: buy at the dot, or wait?

Feed sip. 2025-11-03 to 2026-11-06, 255 days, 14900 dot-contracts.
Same dots and same contract each time; only the buy moment changes. Real 0DTE option bars, 1c spread a side.
Plan A = sell all at +10%, stop at -25%, else out at 30 min. +10% first = hit +10% before -25%.
Skipped = the plan never triggered within 5 minutes (so you'd have sat out). 'Skipped dots at the dot' shows what those would have done.

## 1 OTM

| Entry plan | Taken | Avg wait | Price vs dot | +10% first | Median heat | Best in 15m | Plan A avg | Plan A win | 1st half / 2nd half | Before 1:00 | Skipped dots at the dot |
|---|---|---|---|---|---|---|---|---|---|---|---|
| at the dot (next minute) | 100% | 0.0m | +0.0% | 68% | -12% | +22% | -4.76% | 64% | -4.57% / -4.96% | -2.82% | - |
| wait 1 min | 100% | 1.0m | -0.2% | 68% | -11% | +22% | -4.98% | 64% | -4.90% / -5.05% | -3.32% | - |
| wait 2 min | 100% | 2.0m | -0.4% | 68% | -12% | +22% | -5.00% | 64% | -5.09% / -4.90% | -3.08% | - |
| wait 3 min | 100% | 3.0m | -0.6% | 67% | -12% | +22% | -5.37% | 63% | -5.39% / -5.35% | -3.34% | - |
| first green candle your way (5 min max) | 97% | 1.9m | +0.7% | 68% | -11% | +22% | -4.97% | 64% | -4.83% / -5.11% | -3.36% | -24.30% (n=254) |
| fear/greed under its average (5 min max) | 80% | 1.3m | +3.6% | 68% | -12% | +22% | -4.75% | 64% | -4.79% / -4.71% | -3.08% | -14.44% (n=1507) |
| price quits driving: no new extreme for 2 min | 43% | 2.0m | +7.3% | 68% | -12% | +22% | -4.81% | 64% | -5.08% / -4.54% | -2.69% | -9.19% (n=4278) |
| limit bid 5% under the dot price (5 min max) | 75% | 0.8m | -5.0% | 71% | -11% | +21% | -3.94% | 67% | -3.91% / -3.97% | -1.94% | +4.82% (n=1831) |
| limit bid 10% under the dot price (5 min max) | 59% | 1.4m | -10.0% | 83% | -8% | +23% | -0.25% | 78% | -0.24% / -0.26% | +1.68% | +4.00% (n=3075) |

## 2 ITM

| Entry plan | Taken | Avg wait | Price vs dot | +10% first | Median heat | Best in 15m | Plan A avg | Plan A win | 1st half / 2nd half | Before 1:00 | Skipped dots at the dot |
|---|---|---|---|---|---|---|---|---|---|---|---|
| at the dot (next minute) | 100% | 0.0m | +0.0% | 66% | -11% | +11% | -1.67% | 65% | -1.43% / -1.91% | -1.65% | - |
| wait 1 min | 100% | 1.0m | -0.0% | 66% | -11% | +11% | -1.63% | 65% | -1.47% / -1.79% | -1.69% | +0.52% (n=8) |
| wait 2 min | 100% | 2.0m | -0.2% | 66% | -10% | +12% | -1.57% | 65% | -1.43% / -1.72% | -1.61% | -18.31% (n=3) |
| wait 3 min | 100% | 3.0m | -0.2% | 66% | -11% | +12% | -1.69% | 65% | -1.42% / -1.96% | -1.80% | -2.27% (n=6) |
| first green candle your way (5 min max) | 96% | 1.9m | +0.6% | 66% | -11% | +11% | -1.61% | 65% | -1.44% / -1.77% | -1.57% | -17.86% (n=261) |
| fear/greed under its average (5 min max) | 80% | 1.3m | +2.0% | 67% | -11% | +11% | -1.47% | 65% | -1.13% / -1.81% | -1.32% | -9.29% (n=1507) |
| price quits driving: no new extreme for 2 min | 43% | 2.0m | +3.4% | 67% | -10% | +11% | -1.30% | 66% | -1.04% / -1.57% | -1.28% | -4.40% (n=4272) |
| limit bid 5% under the dot price (5 min max) | 57% | 1.4m | -5.0% | 66% | -12% | +12% | -2.13% | 64% | -1.80% / -2.47% | -2.30% | +4.77% (n=3222) |
| limit bid 10% under the dot price (5 min max) | 32% | 2.0m | -10.0% | 73% | -8% | +15% | +0.24% | 73% | +0.15% / +0.33% | +0.18% | +2.55% (n=5078) |

How to read it: a plan helps if its Plan A avg beats 'at the dot' in BOTH halves. A filter plan (green candle, fear/greed under
its average, quits driving, limit bids) also helps if the dots it skipped did worse at the dot than the ones it took.
