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
| limit bid 15% under the dot price (5 min max) | 42% | 1.9m | -15.0% | 80% | -8% | +26% | -1.47% | 75% | -1.68% / -1.26% | +0.97% | +2.34% (n=4332) |
| limit bid 20% under the dot price (5 min max) | 28% | 2.2m | -20.0% | 80% | -9% | +29% | -2.34% | 72% | -3.06% / -1.59% | +0.87% | +0.83% (n=5331) |
| limit bid 25% under the dot price (5 min max) | 18% | 2.4m | -25.0% | 81% | -9% | +33% | -2.74% | 71% | -3.06% / -2.39% | +1.41% | -0.99% (n=6106) |

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
| limit bid 15% under the dot price (5 min max) | 16% | 2.4m | -15.0% | 74% | -8% | +18% | +0.39% | 74% | +0.03% / +0.79% | +0.45% | +1.04% (n=6219) |
| limit bid 20% under the dot price (5 min max) | 8% | 2.7m | -20.0% | 75% | -8% | +19% | +0.42% | 74% | +0.47% / +0.36% | -0.36% | -0.09% (n=6843) |
| limit bid 25% under the dot price (5 min max) | 4% | 2.9m | -25.0% | 81% | -7% | +22% | +2.56% | 81% | +2.39% / +2.76% | +1.89% | -0.75% (n=7144) |

## Pegged fear/greed: how deep to bid (1 OTM)

Green = traded at least +2% above your fill within 60 min. Plan A as above.

| Dots | Bid | Filled | Green within 60m | +10% first | Median heat | Run: median best in 60m / reached +40% | Plan A avg | 1st half / 2nd half | Before 1:00 |
|---|---|---|---|---|---|---|---|---|---|
| every dot (n=7455) | at the dot | 100% | 96% | 68% | -12% | +40% / 50% | -4.76% | -4.57% / -4.96% | -2.82% |
| every dot (n=7455) | 5% under | 75% | 99% | 71% | -11% | +39% / 49% | -3.94% | -3.91% / -3.97% | -1.94% |
| every dot (n=7455) | 10% under | 59% | 99% | 83% | -8% | +42% / 52% | -0.25% | -0.24% / -0.26% | +1.68% |
| every dot (n=7455) | 15% under | 42% | 99% | 80% | -8% | +45% / 54% | -1.47% | -1.68% / -1.26% | +0.97% |
| every dot (n=7455) | 20% under | 28% | 99% | 80% | -9% | +47% / 56% | -2.34% | -3.06% / -1.59% | +0.87% |
| every dot (n=7455) | 25% under | 18% | 99% | 81% | -9% | +48% / 57% | -2.74% | -3.06% / -2.39% | +1.41% |
| stretch pegged 95-100 AND other side bottomed (10 or less) (n=2226) | at the dot | 100% | 96% | 69% | -11% | +42% / 51% | -4.36% | -4.61% / -4.11% | -2.12% |
| stretch pegged 95-100 AND other side bottomed (10 or less) (n=2226) | 5% under | 76% | 99% | 72% | -11% | +39% / 49% | -3.55% | -4.39% / -2.74% | -0.99% |
| stretch pegged 95-100 AND other side bottomed (10 or less) (n=2226) | 10% under | 61% | 100% | 83% | -8% | +43% / 52% | -0.13% | -0.81% / +0.56% | +2.46% |
| stretch pegged 95-100 AND other side bottomed (10 or less) (n=2226) | 15% under | 43% | 100% | 80% | -8% | +45% / 54% | -1.82% | -2.37% / -1.28% | +1.15% |
| stretch pegged 95-100 AND other side bottomed (10 or less) (n=2226) | 20% under | 30% | 99% | 78% | -9% | +50% / 58% | -3.04% | -4.59% / -1.43% | +1.54% |
| stretch pegged 95-100 AND other side bottomed (10 or less) (n=2226) | 25% under | 20% | 99% | 78% | -11% | +50% / 57% | -3.86% | -3.40% / -4.36% | +0.76% |
|   ...same, day NOT stretched (range 11.5 ATR or less) (n=508) | at the dot | 100% | 96% | 71% | -10% | +37% / 47% | -1.86% | -1.23% / -2.49% | -1.67% |
|   ...same, day NOT stretched (range 11.5 ATR or less) (n=508) | 5% under | 79% | 100% | 74% | -9% | +35% / 46% | -0.83% | +0.23% / -1.82% | -0.82% |
|   ...same, day NOT stretched (range 11.5 ATR or less) (n=508) | 10% under | 59% | 100% | 85% | -6% | +36% / 48% | +2.69% | +1.24% / +4.12% | +2.77% |
|   ...same, day NOT stretched (range 11.5 ATR or less) (n=508) | 15% under | 43% | 100% | 84% | -6% | +38% / 48% | +2.37% | +3.55% / +1.18% | +2.23% |
|   ...same, day NOT stretched (range 11.5 ATR or less) (n=508) | 20% under | 27% | 100% | 87% | -5% | +44% / 53% | +3.20% | +2.19% / +4.20% | +2.81% |
|   ...same, day NOT stretched (range 11.5 ATR or less) (n=508) | 25% under | 17% | 100% | 81% | -7% | +43% / 52% | +1.04% | +3.80% / -1.72% | +0.67% |
|   ...same, day stretched (trend / lock-out / big selloff) (n=1718) | at the dot | 100% | 96% | 69% | -11% | +43% / 53% | -5.10% | -5.62% / -4.59% | -2.46% |
|   ...same, day stretched (trend / lock-out / big selloff) (n=1718) | 5% under | 76% | 99% | 71% | -12% | +40% / 50% | -4.38% | -5.77% / -3.03% | -1.13% |
|   ...same, day stretched (trend / lock-out / big selloff) (n=1718) | 10% under | 61% | 100% | 82% | -8% | +44% / 53% | -0.93% | -1.37% / -0.47% | +2.24% |
|   ...same, day stretched (trend / lock-out / big selloff) (n=1718) | 15% under | 43% | 100% | 78% | -9% | +48% / 56% | -3.05% | -4.12% / -1.99% | +0.22% |
|   ...same, day stretched (trend / lock-out / big selloff) (n=1718) | 20% under | 31% | 99% | 76% | -10% | +51% / 59% | -4.64% | -6.29% / -2.91% | +0.48% |
|   ...same, day stretched (trend / lock-out / big selloff) (n=1718) | 25% under | 21% | 99% | 77% | -11% | +52% / 59% | -5.07% | -5.11% / -5.04% | +0.85% |
|   ...pegged + TTM ticking fast your way (n=262) | at the dot | 100% | 96% | 68% | -9% | +45% / 54% | -4.69% | -3.61% / -5.96% | -3.66% |
|   ...pegged + TTM ticking fast your way (n=262) | 5% under | 76% | 100% | 70% | -11% | +43% / 52% | -3.95% | -2.69% / -5.51% | -3.53% |
|   ...pegged + TTM ticking fast your way (n=262) | 10% under | 63% | 100% | 84% | -8% | +46% / 58% | +0.56% | -0.09% / +1.30% | +2.38% |
|   ...pegged + TTM ticking fast your way (n=262) | 15% under | 45% | 100% | 82% | -7% | +51% / 56% | -0.47% | -0.74% / -0.14% | +2.45% |
|   ...pegged + TTM ticking fast your way (n=262) | 20% under | 35% | 99% | 78% | -10% | +55% / 56% | -2.21% | -3.21% / -1.04% | +1.39% |
|   ...pegged + TTM ticking fast your way (n=262) | 25% under | 25% | 98% | 80% | -9% | +47% / 56% | -1.93% | -3.42% / -0.02% | +7.60% |
|   ...pegged + TTM slow or still against (n=1964) | at the dot | 100% | 96% | 70% | -11% | +41% / 51% | -4.32% | -4.76% / -3.89% | -1.93% |
|   ...pegged + TTM slow or still against (n=1964) | 5% under | 76% | 99% | 72% | -11% | +39% / 49% | -3.49% | -4.65% / -2.43% | -0.68% |
|   ...pegged + TTM slow or still against (n=1964) | 10% under | 60% | 100% | 83% | -8% | +42% / 51% | -0.22% | -0.91% / +0.46% | +2.47% |
|   ...pegged + TTM slow or still against (n=1964) | 15% under | 43% | 100% | 79% | -8% | +45% / 54% | -2.01% | -2.62% / -1.42% | +0.97% |
|   ...pegged + TTM slow or still against (n=1964) | 20% under | 29% | 99% | 78% | -9% | +50% / 58% | -3.17% | -4.82% / -1.49% | +1.57% |
|   ...pegged + TTM slow or still against (n=1964) | 25% under | 19% | 99% | 78% | -11% | +52% / 58% | -4.20% | -3.39% / -5.03% | -0.45% |
|   ...pegged + TTM fast + day NOT stretched (n=49) | at the dot | 100% | 98% | 69% | -8% | +43% / 55% | -2.26% | -2.43% / -2.02% | -1.39% |
|   ...pegged + TTM fast + day NOT stretched (n=49) | 5% under | 78% | 100% | 74% | -8% | +47% / 55% | -0.88% | +0.67% / -3.26% | -0.37% |
|   ...pegged + TTM fast + day NOT stretched (n=49) | 10% under | 61% | 100% | 90% | -4% | +55% / 63% | +4.58% | +2.24% / +8.08% | +5.63% |
|   ...pegged + TTM fast + day NOT stretched (n=49) | 15% under | 49% | 100% | 88% | -9% | +61% / 58% | +3.54% | +5.51% / +0.27% | +4.83% |
|   ...pegged + TTM fast + day NOT stretched (n=49) | 20% under | 37% | 100% | 94% | -7% | +71% / 56% | +5.80% | +4.76% / +7.89% | +5.71% |
|   ...pegged + TTM fast + day NOT stretched (n=49) | 25% under | 29% | 100% | 93% | -8% | +92% / 71% | +5.34% | +7.74% / +1.02% | +8.07% |
|   ...pegged + TTM still against you (neg for calls / pos for puts) (n=2220) | at the dot | 100% | 96% | 69% | -11% | +42% / 51% | -4.36% | -4.63% / -4.10% | -2.12% |
|   ...pegged + TTM still against you (neg for calls / pos for puts) (n=2220) | 5% under | 76% | 99% | 72% | -11% | +39% / 49% | -3.54% | -4.40% / -2.72% | -0.97% |
|   ...pegged + TTM still against you (neg for calls / pos for puts) (n=2220) | 10% under | 61% | 100% | 83% | -8% | +43% / 52% | -0.14% | -0.82% / +0.55% | +2.45% |
|   ...pegged + TTM still against you (neg for calls / pos for puts) (n=2220) | 15% under | 43% | 100% | 79% | -8% | +45% / 54% | -1.84% | -2.39% / -1.30% | +1.14% |
|   ...pegged + TTM still against you (neg for calls / pos for puts) (n=2220) | 20% under | 30% | 99% | 78% | -9% | +50% / 58% | -3.04% | -4.59% / -1.43% | +1.54% |
|   ...pegged + TTM still against you (neg for calls / pos for puts) (n=2220) | 25% under | 20% | 99% | 78% | -11% | +50% / 57% | -3.86% | -3.40% / -4.36% | +0.76% |
|   ...pegged + TTM deep against (-2 or past) and curling your way (n=478) | at the dot | 100% | 96% | 69% | -11% | +42% / 51% | -4.34% | -4.43% / -4.25% | -2.42% |
|   ...pegged + TTM deep against (-2 or past) and curling your way (n=478) | 5% under | 77% | 99% | 72% | -10% | +40% / 50% | -3.47% | -3.58% / -3.37% | -0.86% |
|   ...pegged + TTM deep against (-2 or past) and curling your way (n=478) | 10% under | 63% | 100% | 82% | -7% | +44% / 53% | -0.33% | -0.89% / +0.21% | +3.13% |
|   ...pegged + TTM deep against (-2 or past) and curling your way (n=478) | 15% under | 44% | 100% | 77% | -8% | +46% / 55% | -2.62% | -3.01% / -2.25% | +1.33% |
|   ...pegged + TTM deep against (-2 or past) and curling your way (n=478) | 20% under | 31% | 99% | 78% | -9% | +49% / 57% | -3.09% | -5.28% / -1.10% | +2.67% |
|   ...pegged + TTM deep against (-2 or past) and curling your way (n=478) | 25% under | 22% | 97% | 77% | -11% | +49% / 55% | -4.36% | -6.13% / -2.80% | +3.16% |
|   ...pegged + TTM deep against + curling + day NOT stretched (n=91) | at the dot | 100% | 100% | 78% | -9% | +42% / 53% | +0.94% | +1.84% / +0.13% | +1.34% |
|   ...pegged + TTM deep against + curling + day NOT stretched (n=91) | 5% under | 77% | 100% | 81% | -9% | +45% / 51% | +1.81% | +4.77% / -0.42% | +1.52% |
|   ...pegged + TTM deep against + curling + day NOT stretched (n=91) | 10% under | 55% | 100% | 98% | -4% | +47% / 52% | +7.42% | +6.70% / +8.08% | +7.38% |
|   ...pegged + TTM deep against + curling + day NOT stretched (n=91) | 15% under | 38% | 100% | 91% | -7% | +38% / 49% | +5.04% | +5.95% / +4.19% | +4.89% |
|   ...pegged + TTM deep against + curling + day NOT stretched (n=91) | 20% under | 25% | 100% | 96% | -5% | +44% / 61% | +6.36% | +4.22% / +8.01% | +6.25% |
|   ...pegged + TTM deep against + curling + day NOT stretched (n=91) | 25% under | 15% | 100% | 86% | -9% | +46% / 50% | +2.97% | +2.02% / +3.68% | +2.24% |
| every dot + TTM deep against and curling your way (n=837) | at the dot | 100% | 96% | 70% | -11% | +41% / 51% | -4.09% | -3.77% / -4.39% | -2.08% |
| every dot + TTM deep against and curling your way (n=837) | 5% under | 78% | 100% | 74% | -10% | +42% / 52% | -2.71% | -2.80% / -2.63% | -0.29% |
| every dot + TTM deep against and curling your way (n=837) | 10% under | 63% | 100% | 82% | -7% | +46% / 54% | -0.14% | -0.02% / -0.26% | +2.36% |
| every dot + TTM deep against and curling your way (n=837) | 15% under | 45% | 100% | 80% | -8% | +49% / 57% | -1.25% | -1.40% / -1.11% | +2.20% |
| every dot + TTM deep against and curling your way (n=837) | 20% under | 30% | 100% | 81% | -9% | +50% / 57% | -1.87% | -3.55% / -0.31% | +2.48% |
| every dot + TTM deep against and curling your way (n=837) | 25% under | 20% | 98% | 78% | -10% | +43% / 52% | -3.70% | -4.57% / -2.84% | +2.29% |
| every dot + TTM ticking fast your way (n=635) | at the dot | 100% | 97% | 71% | -10% | +44% / 53% | -4.24% | -3.64% / -4.86% | -2.38% |
| every dot + TTM ticking fast your way (n=635) | 5% under | 77% | 100% | 73% | -11% | +42% / 51% | -3.28% | -2.61% / -3.95% | -2.32% |
| every dot + TTM ticking fast your way (n=635) | 10% under | 62% | 100% | 85% | -8% | +46% / 55% | +0.26% | +0.10% / +0.41% | +1.23% |
| every dot + TTM ticking fast your way (n=635) | 15% under | 45% | 100% | 82% | -8% | +51% / 58% | -1.09% | -0.89% / -1.30% | +1.42% |
| every dot + TTM ticking fast your way (n=635) | 20% under | 34% | 100% | 81% | -10% | +52% / 58% | -2.29% | -2.26% / -2.32% | +0.60% |
| every dot + TTM ticking fast your way (n=635) | 25% under | 23% | 99% | 83% | -10% | +47% / 55% | -2.08% | -2.22% / -1.92% | +5.71% |

## Pegged fear/greed: how deep to bid (2 ITM)

Green = traded at least +2% above your fill within 60 min. Plan A as above.

| Dots | Bid | Filled | Green within 60m | +10% first | Median heat | Run: median best in 60m / reached +40% | Plan A avg | 1st half / 2nd half | Before 1:00 |
|---|---|---|---|---|---|---|---|---|---|
| every dot (n=7445) | at the dot | 100% | 93% | 66% | -11% | +22% / 27% | -1.67% | -1.43% / -1.91% | -1.65% |
| every dot (n=7445) | 5% under | 57% | 97% | 66% | -12% | +24% / 29% | -2.13% | -1.80% / -2.47% | -2.30% |
| every dot (n=7445) | 10% under | 32% | 98% | 73% | -8% | +26% / 34% | +0.24% | +0.15% / +0.33% | +0.18% |
| every dot (n=7445) | 15% under | 16% | 98% | 74% | -8% | +28% / 36% | +0.39% | +0.03% / +0.79% | +0.45% |
| every dot (n=7445) | 20% under | 8% | 99% | 75% | -8% | +30% / 40% | +0.42% | +0.47% / +0.36% | -0.36% |
| every dot (n=7445) | 25% under | 4% | 99% | 81% | -7% | +37% / 45% | +2.56% | +2.39% / +2.76% | +1.89% |
| stretch pegged 95-100 AND other side bottomed (10 or less) (n=2225) | at the dot | 100% | 93% | 66% | -11% | +22% / 28% | -1.72% | -1.78% / -1.66% | -1.83% |
| stretch pegged 95-100 AND other side bottomed (10 or less) (n=2225) | 5% under | 59% | 97% | 67% | -13% | +24% / 30% | -2.15% | -2.20% / -2.10% | -2.41% |
| stretch pegged 95-100 AND other side bottomed (10 or less) (n=2225) | 10% under | 33% | 98% | 74% | -8% | +28% / 36% | +0.45% | -0.43% / +1.35% | +0.52% |
| stretch pegged 95-100 AND other side bottomed (10 or less) (n=2225) | 15% under | 18% | 97% | 73% | -9% | +31% / 37% | -0.11% | -0.59% / +0.43% | +1.32% |
| stretch pegged 95-100 AND other side bottomed (10 or less) (n=2225) | 20% under | 9% | 100% | 74% | -8% | +30% / 41% | -0.05% | +0.20% / -0.32% | -0.21% |
| stretch pegged 95-100 AND other side bottomed (10 or less) (n=2225) | 25% under | 5% | 99% | 83% | -6% | +39% / 49% | +3.04% | +1.44% / +5.18% | +2.63% |
|   ...same, day NOT stretched (range 11.5 ATR or less) (n=507) | at the dot | 100% | 93% | 66% | -11% | +24% / 32% | -2.18% | -1.22% / -3.13% | -2.17% |
|   ...same, day NOT stretched (range 11.5 ATR or less) (n=507) | 5% under | 67% | 98% | 65% | -13% | +27% / 33% | -2.74% | -2.03% / -3.44% | -2.59% |
|   ...same, day NOT stretched (range 11.5 ATR or less) (n=507) | 10% under | 44% | 99% | 75% | -7% | +30% / 41% | +0.77% | +0.10% / +1.43% | +0.79% |
|   ...same, day NOT stretched (range 11.5 ATR or less) (n=507) | 15% under | 25% | 97% | 75% | -9% | +31% / 41% | +0.37% | -1.12% / +1.90% | +1.11% |
|   ...same, day NOT stretched (range 11.5 ATR or less) (n=507) | 20% under | 14% | 100% | 68% | -11% | +30% / 42% | -1.93% | -3.16% / -0.94% | -0.94% |
|   ...same, day NOT stretched (range 11.5 ATR or less) (n=507) | 25% under | 7% | 100% | 80% | -6% | +49% / 51% | +2.16% | -1.13% / +5.27% | +0.72% |
|   ...same, day stretched (trend / lock-out / big selloff) (n=1718) | at the dot | 100% | 94% | 66% | -11% | +21% / 27% | -1.58% | -1.95% / -1.23% | -1.58% |
|   ...same, day stretched (trend / lock-out / big selloff) (n=1718) | 5% under | 56% | 96% | 67% | -13% | +23% / 29% | -1.94% | -2.26% / -1.62% | -2.26% |
|   ...same, day stretched (trend / lock-out / big selloff) (n=1718) | 10% under | 30% | 98% | 73% | -9% | +27% / 33% | +0.31% | -0.65% / +1.31% | +0.24% |
|   ...same, day stretched (trend / lock-out / big selloff) (n=1718) | 15% under | 16% | 97% | 73% | -9% | +30% / 35% | -0.32% | -0.36% / -0.28% | +1.58% |
|   ...same, day stretched (trend / lock-out / big selloff) (n=1718) | 20% under | 8% | 99% | 77% | -8% | +28% / 40% | +0.90% | +1.59% / +0.06% | +0.78% |
|   ...same, day stretched (trend / lock-out / big selloff) (n=1718) | 25% under | 4% | 99% | 84% | -6% | +35% / 47% | +3.48% | +2.46% / +5.12% | +4.85% |
|   ...pegged + TTM ticking fast your way (n=262) | at the dot | 100% | 92% | 69% | -9% | +23% / 29% | -1.21% | -1.42% / -0.97% | -1.70% |
|   ...pegged + TTM ticking fast your way (n=262) | 5% under | 59% | 95% | 65% | -14% | +26% / 33% | -2.74% | -1.96% / -3.69% | -3.44% |
|   ...pegged + TTM ticking fast your way (n=262) | 10% under | 37% | 97% | 73% | -8% | +32% / 40% | +0.44% | -0.57% / +1.51% | +1.35% |
|   ...pegged + TTM ticking fast your way (n=262) | 15% under | 21% | 98% | 72% | -13% | +33% / 44% | -0.54% | -1.32% / +0.44% | +2.77% |
|   ...pegged + TTM ticking fast your way (n=262) | 20% under | 12% | 97% | 81% | -7% | +33% / 42% | +2.37% | -0.16% / +4.74% | +3.37% |
|   ...pegged + TTM ticking fast your way (n=262) | 25% under | 7% | 100% | 83% | -3% | +36% / 44% | +3.26% | -2.59% / +9.10% | +6.20% |
|   ...pegged + TTM slow or still against (n=1963) | at the dot | 100% | 94% | 66% | -11% | +22% / 28% | -1.79% | -1.83% / -1.74% | -1.85% |
|   ...pegged + TTM slow or still against (n=1963) | 5% under | 59% | 97% | 67% | -13% | +24% / 29% | -2.07% | -2.23% / -1.91% | -2.27% |
|   ...pegged + TTM slow or still against (n=1963) | 10% under | 33% | 98% | 74% | -8% | +27% / 35% | +0.45% | -0.41% / +1.32% | +0.39% |
|   ...pegged + TTM slow or still against (n=1963) | 15% under | 18% | 97% | 74% | -8% | +30% / 36% | -0.04% | -0.47% / +0.43% | +1.11% |
|   ...pegged + TTM slow or still against (n=1963) | 20% under | 9% | 100% | 73% | -9% | +29% / 41% | -0.48% | +0.26% / -1.28% | -0.92% |
|   ...pegged + TTM slow or still against (n=1963) | 25% under | 4% | 99% | 83% | -6% | +39% / 49% | +3.00% | +2.15% / +4.20% | +1.61% |
|   ...pegged + TTM fast + day NOT stretched (n=49) | at the dot | 100% | 92% | 69% | -7% | +32% / 33% | -1.33% | +0.93% / -4.61% | -1.26% |
|   ...pegged + TTM fast + day NOT stretched (n=49) | 5% under | 73% | 97% | 69% | -11% | +35% / 42% | -1.35% | +1.39% / -5.65% | -0.94% |
|   ...pegged + TTM fast + day NOT stretched (n=49) | 10% under | 53% | 100% | 81% | -4% | +45% / 54% | +2.57% | +2.31% / +2.92% | +3.69% |
|   ...pegged + TTM fast + day NOT stretched (n=49) | 15% under | 31% | 100% | 93% | -9% | +55% / 60% | +6.92% | +9.27% / +3.39% | +9.24% |
|   ...pegged + TTM fast + day NOT stretched (n=49) | 20% under | 22% | 100% | 82% | -5% | +70% / 55% | +2.86% | +3.40% / +2.20% | +5.70% |
|   ...pegged + TTM still against you (neg for calls / pos for puts) (n=2219) | at the dot | 100% | 93% | 66% | -11% | +22% / 28% | -1.72% | -1.79% / -1.66% | -1.83% |
|   ...pegged + TTM still against you (neg for calls / pos for puts) (n=2219) | 5% under | 59% | 97% | 67% | -13% | +24% / 30% | -2.14% | -2.22% / -2.07% | -2.38% |
|   ...pegged + TTM still against you (neg for calls / pos for puts) (n=2219) | 10% under | 33% | 98% | 74% | -8% | +28% / 36% | +0.43% | -0.46% / +1.32% | +0.50% |
|   ...pegged + TTM still against you (neg for calls / pos for puts) (n=2219) | 15% under | 18% | 97% | 73% | -9% | +31% / 37% | -0.11% | -0.59% / +0.43% | +1.32% |
|   ...pegged + TTM still against you (neg for calls / pos for puts) (n=2219) | 20% under | 9% | 100% | 74% | -8% | +30% / 41% | -0.05% | +0.20% / -0.32% | -0.21% |
|   ...pegged + TTM still against you (neg for calls / pos for puts) (n=2219) | 25% under | 5% | 99% | 83% | -6% | +39% / 49% | +3.04% | +1.44% / +5.18% | +2.63% |
|   ...pegged + TTM deep against (-2 or past) and curling your way (n=478) | at the dot | 100% | 93% | 67% | -11% | +23% / 29% | -1.70% | -3.48% / -0.05% | -1.30% |
|   ...pegged + TTM deep against (-2 or past) and curling your way (n=478) | 5% under | 62% | 96% | 67% | -13% | +25% / 31% | -2.01% | -3.27% / -0.80% | -1.41% |
|   ...pegged + TTM deep against (-2 or past) and curling your way (n=478) | 10% under | 34% | 96% | 74% | -8% | +29% / 35% | +0.80% | -2.21% / +3.45% | +1.07% |
|   ...pegged + TTM deep against (-2 or past) and curling your way (n=478) | 15% under | 19% | 98% | 74% | -8% | +32% / 37% | +0.04% | -1.07% / +1.03% | +3.62% |
|   ...pegged + TTM deep against (-2 or past) and curling your way (n=478) | 20% under | 10% | 100% | 74% | -10% | +34% / 41% | +0.00% | +1.81% / -1.97% | +5.87% |
|   ...pegged + TTM deep against (-2 or past) and curling your way (n=478) | 25% under | 5% | 100% | 91% | -6% | +51% / 55% | +5.85% | +6.28% / +5.23% | +9.11% |
|   ...pegged + TTM deep against + curling + day NOT stretched (n=91) | at the dot | 100% | 98% | 76% | -8% | +28% / 38% | +1.40% | +1.91% / +0.94% | +1.75% |
|   ...pegged + TTM deep against + curling + day NOT stretched (n=91) | 5% under | 66% | 98% | 80% | -8% | +31% / 42% | +1.76% | +2.86% / +0.86% | +2.59% |
|   ...pegged + TTM deep against + curling + day NOT stretched (n=91) | 10% under | 40% | 97% | 92% | -5% | +36% / 47% | +6.37% | +2.73% / +9.29% | +6.21% |
|   ...pegged + TTM deep against + curling + day NOT stretched (n=91) | 15% under | 22% | 100% | 85% | -12% | +36% / 45% | +4.04% | -2.35% / +9.27% | +7.35% |
|   ...pegged + TTM deep against + curling + day NOT stretched (n=91) | 20% under | 13% | 100% | 75% | -10% | +32% / 42% | +0.52% | -4.75% / +4.28% | +5.77% |
| every dot + TTM deep against and curling your way (n=835) | at the dot | 100% | 93% | 67% | -11% | +23% / 28% | -1.62% | -2.20% / -1.06% | -1.05% |
| every dot + TTM deep against and curling your way (n=835) | 5% under | 60% | 96% | 67% | -12% | +26% / 32% | -1.70% | -2.24% / -1.15% | -1.41% |
| every dot + TTM deep against and curling your way (n=835) | 10% under | 36% | 97% | 75% | -7% | +30% / 37% | +0.80% | -0.40% / +1.87% | -0.13% |
| every dot + TTM deep against and curling your way (n=835) | 15% under | 19% | 99% | 74% | -8% | +31% / 36% | +0.15% | -1.09% / +1.34% | +2.89% |
| every dot + TTM deep against and curling your way (n=835) | 20% under | 9% | 99% | 70% | -11% | +26% / 38% | -1.13% | -1.03% / -1.23% | +1.82% |
| every dot + TTM deep against and curling your way (n=835) | 25% under | 5% | 100% | 90% | -7% | +30% / 40% | +5.55% | +5.65% / +5.45% | +7.30% |
| every dot + TTM ticking fast your way (n=635) | at the dot | 100% | 93% | 69% | -9% | +23% / 28% | -1.05% | -0.48% / -1.63% | -0.90% |
| every dot + TTM ticking fast your way (n=635) | 5% under | 58% | 96% | 65% | -12% | +25% / 31% | -2.42% | -1.61% / -3.23% | -3.22% |
| every dot + TTM ticking fast your way (n=635) | 10% under | 36% | 98% | 74% | -8% | +30% / 37% | +0.80% | +0.97% / +0.65% | +0.37% |
| every dot + TTM ticking fast your way (n=635) | 15% under | 19% | 98% | 75% | -10% | +32% / 40% | +0.41% | +0.00% / +0.89% | +0.81% |
| every dot + TTM ticking fast your way (n=635) | 20% under | 10% | 98% | 75% | -7% | +33% / 43% | +0.42% | -1.78% / +2.56% | +1.30% |
| every dot + TTM ticking fast your way (n=635) | 25% under | 5% | 100% | 88% | -4% | +31% / 39% | +4.80% | +1.51% / +7.22% | +7.05% |

## 5-minute candle + 2m / 3m charts (1 OTM)

| Dots | Count | Per day | Bid | Filled | +10% first | Median heat | Run: median best 60m / +40% | Plan A avg | 1st half / 2nd half | Before 1:00 |
|---|---|---|---|---|---|---|---|---|---|---|
| 1m dots: every dot | 7455 | 29.2 | at the dot | 100% | 68% | -12% | +40% / 50% | -4.76% | -4.57% / -4.96% | -2.82% |
| 1m dots: every dot | 7455 | 29.2 | 10% under | 59% | 83% | -8% | +42% / 52% | -0.25% | -0.24% / -0.26% | +1.68% |
| 1m: dot on the LAST minute of a 5m candle | 1559 | 6.1 | at the dot | 100% | 69% | -11% | +41% / 50% | -4.72% | -4.75% / -4.68% | -2.78% |
| 1m: dot on the LAST minute of a 5m candle | 1559 | 6.1 | 10% under | 59% | 83% | -7% | +44% / 53% | -0.26% | -0.70% / +0.17% | +1.87% |
| 1m: dot on minutes 1-4 of a 5m candle | 5896 | 23.1 | at the dot | 100% | 68% | -12% | +40% / 50% | -4.78% | -4.52% / -5.03% | -2.83% |
| 1m: dot on minutes 1-4 of a 5m candle | 5896 | 23.1 | 10% under | 59% | 83% | -8% | +42% / 51% | -0.25% | -0.12% / -0.37% | +1.62% |
| 1m: last minute of the previous 5m candle moved your way | 2743 | 10.8 | at the dot | 100% | 69% | -11% | +42% / 52% | -4.57% | -4.53% / -4.61% | -2.86% |
| 1m: last minute of the previous 5m candle moved your way | 2743 | 10.8 | 10% under | 58% | 83% | -8% | +44% / 53% | -0.23% | -0.14% / -0.31% | +1.70% |
| 1m: last minute of the previous 5m candle moved against | 4712 | 18.5 | at the dot | 100% | 68% | -12% | +40% / 49% | -4.87% | -4.59% / -5.16% | -2.79% |
| 1m: last minute of the previous 5m candle moved against | 4712 | 18.5 | 10% under | 59% | 83% | -8% | +41% / 51% | -0.26% | -0.30% / -0.23% | +1.66% |
| 1m: previous 5m candle closed your way | 1044 | 4.1 | at the dot | 100% | 68% | -12% | +43% / 53% | -5.13% | -5.43% / -4.85% | -3.44% |
| 1m: previous 5m candle closed your way | 1044 | 4.1 | 10% under | 60% | 85% | -8% | +41% / 50% | +0.17% | -0.00% / +0.35% | +2.57% |
| 1m: current 5m candle already your way at the dot | 3278 | 12.9 | at the dot | 100% | 68% | -12% | +42% / 51% | -4.91% | -4.94% / -4.87% | -2.82% |
| 1m: current 5m candle already your way at the dot | 3278 | 12.9 | 10% under | 61% | 82% | -8% | +44% / 53% | -0.41% | -0.31% / -0.50% | +1.92% |
| 1m: 2m fear/greed pegged + other bottomed | 978 | 3.8 | at the dot | 100% | 69% | -11% | +42% / 51% | -4.34% | -4.37% / -4.32% | -3.40% |
| 1m: 2m fear/greed pegged + other bottomed | 978 | 3.8 | 10% under | 60% | 82% | -7% | +46% / 55% | -0.56% | +0.08% / -1.17% | +1.18% |
| 1m: 3m fear/greed pegged + other bottomed | 654 | 2.6 | at the dot | 100% | 71% | -11% | +40% / 50% | -3.80% | -2.97% / -4.55% | -1.86% |
| 1m: 3m fear/greed pegged + other bottomed | 654 | 2.6 | 10% under | 56% | 80% | -8% | +44% / 52% | -1.18% | -0.61% / -1.67% | +1.74% |
| 1m: 3m TTM deep against + curling | 217 | 0.9 | at the dot | 100% | 67% | -11% | +33% / 43% | -5.13% | -4.89% / -5.33% | -4.23% |
| 1m: 3m TTM deep against + curling | 217 | 0.9 | 10% under | 56% | 80% | -8% | +40% / 49% | -0.82% | -0.11% / -1.38% | -0.93% |
| 1m: 3m TTM ticking fast your way | 59 | 0.2 | at the dot | 100% | 69% | -9% | +38% / 46% | -4.53% | -5.21% / -4.02% | -1.78% |
| 1m: 3m TTM ticking fast your way | 59 | 0.2 | 10% under | 53% | 77% | -9% | +31% / 35% | -1.32% | +3.40% / -4.72% | +3.55% |
| 1m A+ (pegged, TTM deep+curl, day calm) | 91 | 0.4 | at the dot | 100% | 78% | -9% | +42% / 53% | +0.94% | +1.84% / +0.13% | +1.34% |
| 1m A+ (pegged, TTM deep+curl, day calm) | 91 | 0.4 | 10% under | 55% | 98% | -4% | +47% / 52% | +7.42% | +6.70% / +8.08% | +7.38% |
| 1m A+ AND last 5m minute your way | 42 | 0.2 | at the dot | 100% | 79% | -6% | +45% / 62% | +0.94% | +1.02% / +0.84% | +2.06% |
| 1m A+ AND last 5m minute your way | 42 | 0.2 | 10% under | 52% | 95% | -4% | +48% / 55% | +6.73% | +5.56% / +8.42% | +6.62% |
| 1m pegged + calm day AND 3m pegged | 47 | 0.2 | at the dot | 100% | 70% | -7% | +29% / 38% | -2.04% | +0.40% / -3.42% | -2.04% |
| 1m pegged + calm day AND 3m pegged | 47 | 0.2 | 10% under | 53% | 80% | -8% | +30% / 36% | +1.29% | -4.53% / +4.02% | +1.29% |
| 2m chart dots: every dot | 3468 | 13.6 | at the dot | 100% | 67% | -11% | +40% / 50% | -5.04% | -4.72% / -5.37% | -3.61% |
| 2m chart dots: every dot | 3468 | 13.6 | 10% under | 58% | 83% | -8% | +39% / 49% | -0.20% | -0.61% / +0.20% | +0.99% |
| 2m chart dots: pegged + other bottomed | 705 | 2.8 | at the dot | 100% | 69% | -11% | +42% / 51% | -4.35% | -4.70% / -4.03% | -2.33% |
| 2m chart dots: pegged + other bottomed | 705 | 2.8 | 10% under | 59% | 84% | -7% | +42% / 51% | +0.52% | +0.10% / +0.92% | +1.63% |
| 2m chart dots: pegged + calm day | 122 | 0.5 | at the dot | 100% | 73% | -10% | +45% / 57% | -1.31% | -1.42% / -1.22% | -0.99% |
| 2m chart dots: pegged + calm day | 122 | 0.5 | 10% under | 57% | 91% | -5% | +56% / 58% | +4.71% | +4.26% / +5.06% | +4.40% |
| 2m chart dots: A+ (pegged, TTM deep+curl, calm) | 17 | 0.1 | at the dot | 100% | 94% | -13% | +42% / 53% | +5.66% | +7.19% / +4.30% | +5.66% |
| 2m chart dots: before 1:00 | 1780 | 7.0 | at the dot | 100% | 67% | -11% | +35% / 47% | -3.61% | -2.97% / -4.28% | -3.61% |
| 2m chart dots: before 1:00 | 1780 | 7.0 | 10% under | 54% | 82% | -7% | +34% / 45% | +0.99% | +0.61% / +1.38% | +0.99% |
| 3m chart dots: every dot | 2183 | 8.6 | at the dot | 100% | 68% | -12% | +40% / 50% | -4.99% | -4.25% / -5.76% | -3.86% |
| 3m chart dots: every dot | 2183 | 8.6 | 10% under | 56% | 83% | -8% | +39% / 49% | -0.20% | +0.22% / -0.67% | +1.21% |
| 3m chart dots: pegged + other bottomed | 432 | 1.7 | at the dot | 100% | 68% | -12% | +41% / 51% | -4.74% | -3.32% / -5.97% | -4.59% |
| 3m chart dots: pegged + other bottomed | 432 | 1.7 | 10% under | 58% | 81% | -9% | +43% / 51% | -0.37% | +1.79% / -2.33% | +0.29% |
| 3m chart dots: pegged + calm day | 49 | 0.2 | at the dot | 100% | 67% | -11% | +35% / 47% | -3.32% | -2.78% / -3.65% | -3.57% |
| 3m chart dots: pegged + calm day | 49 | 0.2 | 10% under | 55% | 78% | -7% | +33% / 37% | -0.05% | -4.69% / +3.15% | -0.05% |
| 3m chart dots: before 1:00 | 1073 | 4.2 | at the dot | 100% | 67% | -11% | +32% / 44% | -3.86% | -3.44% / -4.27% | -3.86% |
| 3m chart dots: before 1:00 | 1073 | 4.2 | 10% under | 53% | 83% | -7% | +31% / 41% | +1.21% | +1.74% / +0.66% | +1.21% |

## 5-minute candle + 2m / 3m charts (2 ITM)

| Dots | Count | Per day | Bid | Filled | +10% first | Median heat | Run: median best 60m / +40% | Plan A avg | 1st half / 2nd half | Before 1:00 |
|---|---|---|---|---|---|---|---|---|---|---|
| 1m dots: every dot | 7445 | 29.2 | at the dot | 100% | 66% | -11% | +22% / 27% | -1.67% | -1.43% / -1.91% | -1.65% |
| 1m dots: every dot | 7445 | 29.2 | 10% under | 32% | 73% | -8% | +26% / 34% | +0.24% | +0.15% / +0.33% | +0.18% |
| 1m: dot on the LAST minute of a 5m candle | 1557 | 6.1 | at the dot | 100% | 65% | -11% | +22% / 29% | -2.08% | -2.24% / -1.92% | -1.91% |
| 1m: dot on the LAST minute of a 5m candle | 1557 | 6.1 | 10% under | 31% | 73% | -8% | +26% / 35% | +0.42% | +0.03% / +0.82% | -0.17% |
| 1m: dot on minutes 1-4 of a 5m candle | 5888 | 23.1 | at the dot | 100% | 67% | -10% | +22% / 27% | -1.56% | -1.21% / -1.91% | -1.58% |
| 1m: dot on minutes 1-4 of a 5m candle | 5888 | 23.1 | 10% under | 32% | 73% | -8% | +26% / 34% | +0.19% | +0.18% / +0.20% | +0.27% |
| 1m: last minute of the previous 5m candle moved your way | 2740 | 10.7 | at the dot | 100% | 67% | -10% | +23% / 28% | -1.42% | -1.13% / -1.71% | -1.19% |
| 1m: last minute of the previous 5m candle moved your way | 2740 | 10.7 | 10% under | 32% | 73% | -8% | +29% / 37% | +0.29% | +0.48% / +0.10% | +0.51% |
| 1m: last minute of the previous 5m candle moved against | 4705 | 18.5 | at the dot | 100% | 66% | -11% | +21% / 27% | -1.82% | -1.60% / -2.03% | -1.92% |
| 1m: last minute of the previous 5m candle moved against | 4705 | 18.5 | 10% under | 32% | 73% | -8% | +25% / 32% | +0.21% | -0.04% / +0.46% | -0.02% |
| 1m: previous 5m candle closed your way | 1041 | 4.1 | at the dot | 100% | 65% | -11% | +23% / 28% | -1.83% | -2.05% / -1.61% | -1.46% |
| 1m: previous 5m candle closed your way | 1041 | 4.1 | 10% under | 31% | 77% | -7% | +26% / 34% | +1.18% | +0.59% / +1.82% | +1.40% |
| 1m: current 5m candle already your way at the dot | 3272 | 12.8 | at the dot | 100% | 67% | -11% | +22% / 27% | -1.52% | -1.42% / -1.61% | -1.59% |
| 1m: current 5m candle already your way at the dot | 3272 | 12.8 | 10% under | 33% | 75% | -8% | +27% / 33% | +0.81% | +0.18% / +1.43% | +0.58% |
| 1m: 2m fear/greed pegged + other bottomed | 978 | 3.8 | at the dot | 100% | 67% | -11% | +21% / 28% | -1.46% | -1.29% / -1.62% | -2.43% |
| 1m: 2m fear/greed pegged + other bottomed | 978 | 3.8 | 10% under | 34% | 76% | -8% | +27% / 35% | +0.96% | -0.74% / +2.48% | -0.40% |
| 1m: 3m fear/greed pegged + other bottomed | 653 | 2.6 | at the dot | 100% | 69% | -9% | +22% / 26% | -0.82% | +0.05% / -1.58% | -0.73% |
| 1m: 3m fear/greed pegged + other bottomed | 653 | 2.6 | 10% under | 31% | 77% | -9% | +25% / 30% | +1.26% | +0.22% / +2.11% | +1.60% |
| 1m: 3m TTM deep against + curling | 217 | 0.9 | at the dot | 100% | 64% | -11% | +20% / 22% | -1.92% | -2.78% / -1.19% | -1.15% |
| 1m: 3m TTM deep against + curling | 217 | 0.9 | 10% under | 29% | 70% | -10% | +24% / 35% | -0.44% | -0.45% / -0.42% | -0.55% |
| 1m: 3m TTM ticking fast your way | 59 | 0.2 | at the dot | 100% | 59% | -12% | +22% / 24% | -2.97% | -0.64% / -4.68% | -1.96% |
| 1m: 3m TTM ticking fast your way | 59 | 0.2 | 10% under | 32% | 74% | -5% | +24% / 16% | +0.09% | -2.48% / +2.40% | +1.01% |
| 1m A+ (pegged, TTM deep+curl, day calm) | 91 | 0.4 | at the dot | 100% | 76% | -8% | +28% / 38% | +1.40% | +1.91% / +0.94% | +1.75% |
| 1m A+ (pegged, TTM deep+curl, day calm) | 91 | 0.4 | 10% under | 40% | 92% | -5% | +36% / 47% | +6.37% | +2.73% / +9.29% | +6.21% |
| 1m A+ AND last 5m minute your way | 42 | 0.2 | at the dot | 100% | 81% | -5% | +36% / 43% | +2.20% | +3.29% / +0.76% | +3.30% |
| 1m A+ AND last 5m minute your way | 42 | 0.2 | 10% under | 40% | 94% | -4% | +38% / 47% | +7.27% | +5.42% / +9.35% | +7.01% |
| 1m pegged + calm day AND 3m pegged | 47 | 0.2 | at the dot | 100% | 62% | -8% | +23% / 30% | -2.46% | -0.67% / -3.48% | -2.46% |
| 1m pegged + calm day AND 3m pegged | 47 | 0.2 | 10% under | 38% | 78% | -16% | +22% / 28% | +1.52% | +0.61% / +1.78% | +1.52% |
| 2m chart dots: every dot | 3460 | 13.6 | at the dot | 100% | 66% | -11% | +22% / 28% | -1.52% | -1.02% / -2.01% | -1.64% |
| 2m chart dots: every dot | 3460 | 13.6 | 10% under | 32% | 71% | -9% | +24% / 33% | -0.61% | -0.64% / -0.58% | -0.66% |
| 2m chart dots: pegged + other bottomed | 705 | 2.8 | at the dot | 100% | 69% | -11% | +23% / 31% | -1.15% | -0.22% / -2.02% | -0.89% |
| 2m chart dots: pegged + other bottomed | 705 | 2.8 | 10% under | 32% | 75% | -10% | +27% / 36% | +0.44% | -0.17% / +1.01% | -0.89% |
| 2m chart dots: pegged + calm day | 122 | 0.5 | at the dot | 100% | 74% | -9% | +30% / 38% | +0.48% | +0.26% / +0.67% | +0.55% |
| 2m chart dots: pegged + calm day | 122 | 0.5 | 10% under | 32% | 82% | -8% | +32% / 38% | +3.17% | +2.70% / +3.49% | +2.07% |
| 2m chart dots: A+ (pegged, TTM deep+curl, calm) | 17 | 0.1 | at the dot | 100% | 82% | -7% | +29% / 29% | +4.88% | +2.53% / +6.97% | +4.88% |
| 2m chart dots: before 1:00 | 1778 | 7.0 | at the dot | 100% | 67% | -11% | +22% / 28% | -1.64% | -1.06% / -2.26% | -1.64% |
| 2m chart dots: before 1:00 | 1778 | 7.0 | 10% under | 33% | 72% | -9% | +23% / 33% | -0.66% | -0.01% / -1.38% | -0.66% |
| 3m chart dots: every dot | 2178 | 8.5 | at the dot | 100% | 66% | -10% | +22% / 28% | -1.69% | -1.08% / -2.33% | -1.66% |
| 3m chart dots: every dot | 2178 | 8.5 | 10% under | 29% | 73% | -9% | +24% / 31% | -0.32% | +0.75% / -1.55% | -0.62% |
| 3m chart dots: pegged + other bottomed | 432 | 1.7 | at the dot | 100% | 67% | -10% | +24% / 31% | -1.26% | +0.19% / -2.52% | -1.47% |
| 3m chart dots: pegged + other bottomed | 432 | 1.7 | 10% under | 31% | 75% | -10% | +28% / 33% | +0.44% | -0.59% / +1.40% | +1.34% |
| 3m chart dots: pegged + calm day | 49 | 0.2 | at the dot | 100% | 71% | -8% | +25% / 29% | -0.30% | -1.69% / +0.59% | -0.50% |
| 3m chart dots: pegged + calm day | 49 | 0.2 | 10% under | 39% | 84% | -12% | +28% / 32% | +3.72% | -2.37% / +9.21% | +3.72% |
| 3m chart dots: before 1:00 | 1071 | 4.2 | at the dot | 100% | 67% | -10% | +21% / 27% | -1.66% | -1.22% / -2.09% | -1.66% |
| 3m chart dots: before 1:00 | 1071 | 4.2 | 10% under | 32% | 72% | -10% | +21% / 29% | -0.62% | +1.26% / -2.82% | -0.62% |

## Hard jump on a 1-minute candle: does it keep going? (1 OTM, bought in the jump's direction)

Jump = 1-minute candle body at least 1.5x or 2.5x the 1-minute ATR. SPY kept going = closed further that way 5 / 15 min later (avg move in ATR).

| Jump | Filter | Count | Per day | Bid | SPY kept going 5m / 15m | Avg move 5m / 15m (ATR) | Filled | +10% first | Median heat | Plan A avg | 1st half / 2nd half | Before 1:00 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| jump 1.5x ATR on the last minute of the 5m candle | all | 263 | 1.0 | at the jump | 46% / 45% | -0.16 / -0.18 | 100% | 68% | -12% | -4.47% | -7.23% / -2.54% | -3.93% |
| jump 1.5x ATR on the last minute of the 5m candle | all | 263 | 1.0 | 10% under | 46% / 45% | -0.16 / -0.18 | 65% | 82% | -9% | +0.09% | -1.15% / +1.26% | +0.96% |
| jump 1.5x ATR on the last minute of the 5m candle | dot same side in the last 5 min | 54 | 0.2 | at the jump | 48% / 46% | +0.03 / -0.09 | 100% | 67% | -7% | -4.94% | -9.21% / -1.52% | -3.32% |
| jump 1.5x ATR on the last minute of the 5m candle | dot same side in the last 5 min | 54 | 0.2 | 10% under | 48% / 46% | +0.03 / -0.09 | 59% | 72% | -13% | -3.49% | -4.51% / -2.00% | -3.88% |
| jump 1.5x ATR on the last minute of the 5m candle | dot on the OTHER side in the last 5 min | 40 | 0.2 | at the jump | 52% / 48% | -0.07 / -0.03 | 100% | 80% | -8% | -0.70% | -2.06% / -0.19% | -5.83% |
| jump 1.5x ATR on the last minute of the 5m candle | dot on the OTHER side in the last 5 min | 40 | 0.2 | 10% under | 52% / 48% | -0.07 / -0.03 | 65% | 92% | -8% | +3.35% | +3.12% / +3.45% | +2.49% |
| jump 1.5x ATR on the last minute of the 5m candle | calm day (11.5 ATR or less) | 48 | 0.2 | at the jump | 40% / 42% | -0.17 / -0.18 | 100% | 60% | -11% | -5.46% | -9.78% / -2.10% | -6.76% |
| jump 1.5x ATR on the last minute of the 5m candle | calm day (11.5 ATR or less) | 48 | 0.2 | 10% under | 40% / 42% | -0.17 / -0.18 | 65% | 81% | -9% | +1.46% | +0.09% / +3.13% | +1.92% |
| jump 1.5x ATR on the last minute of the 5m candle | before 1:00 | 130 | 0.5 | at the jump | 45% / 45% | -0.04 / +0.07 | 100% | 68% | -11% | -3.93% | -5.09% / -3.16% | -3.93% |
| jump 1.5x ATR on the last minute of the 5m candle | before 1:00 | 130 | 0.5 | 10% under | 45% / 45% | -0.04 / +0.07 | 59% | 82% | -8% | +0.96% | +3.18% / -1.00% | +0.96% |
| jump 1.5x ATR on the minutes 1-4 of the 5m candle | all | 1522 | 6.0 | at the jump | 48% / 48% | -0.07 / -0.04 | 100% | 68% | -12% | -4.97% | -6.14% / -3.78% | -3.27% |
| jump 1.5x ATR on the minutes 1-4 of the 5m candle | all | 1522 | 6.0 | 10% under | 48% / 48% | -0.07 / -0.04 | 65% | 86% | -9% | +1.22% | +1.30% / +1.13% | +3.12% |
| jump 1.5x ATR on the minutes 1-4 of the 5m candle | dot same side in the last 5 min | 330 | 1.3 | at the jump | 53% / 50% | -0.01 / -0.04 | 100% | 71% | -10% | -4.22% | -6.10% / -2.62% | -2.33% |
| jump 1.5x ATR on the minutes 1-4 of the 5m candle | dot same side in the last 5 min | 330 | 1.3 | 10% under | 53% / 50% | -0.01 / -0.04 | 59% | 86% | -8% | +0.67% | -0.08% / +1.41% | +3.71% |
| jump 1.5x ATR on the minutes 1-4 of the 5m candle | dot on the OTHER side in the last 5 min | 302 | 1.2 | at the jump | 51% / 49% | +0.06 / +0.03 | 100% | 70% | -11% | -4.24% | -4.14% / -4.35% | -2.48% |
| jump 1.5x ATR on the minutes 1-4 of the 5m candle | dot on the OTHER side in the last 5 min | 302 | 1.2 | 10% under | 51% / 49% | +0.06 / +0.03 | 65% | 85% | -10% | +0.66% | +2.14% / -1.04% | +3.16% |
| jump 1.5x ATR on the minutes 1-4 of the 5m candle | calm day (11.5 ATR or less) | 320 | 1.3 | at the jump | 49% / 48% | -0.00 / -0.12 | 100% | 66% | -13% | -3.77% | -4.58% / -2.73% | -3.82% |
| jump 1.5x ATR on the minutes 1-4 of the 5m candle | calm day (11.5 ATR or less) | 320 | 1.3 | 10% under | 49% / 48% | -0.00 / -0.12 | 66% | 86% | -8% | +2.85% | +2.22% / +3.77% | +2.79% |
| jump 1.5x ATR on the minutes 1-4 of the 5m candle | before 1:00 | 708 | 2.8 | at the jump | 47% / 48% | -0.09 / -0.15 | 100% | 69% | -11% | -3.27% | -4.48% / -1.89% | -3.27% |
| jump 1.5x ATR on the minutes 1-4 of the 5m candle | before 1:00 | 708 | 2.8 | 10% under | 47% / 48% | -0.09 / -0.15 | 62% | 88% | -8% | +3.12% | +3.27% / +2.92% | +3.12% |
| jump 2.5x ATR on the last minute of the 5m candle | all | 28 | 0.1 | at the jump | 29% / 39% | -0.58 / -0.15 | 100% | 29% | -28% | -17.27% | -22.35% / -11.41% | -16.30% |
| jump 2.5x ATR on the last minute of the 5m candle | all | 28 | 0.1 | 10% under | 29% / 39% | -0.58 / -0.15 | 89% | 60% | -20% | -6.63% | -9.99% / -2.36% | +0.62% |
| jump 2.5x ATR on the last minute of the 5m candle | before 1:00 | 13 | 0.1 | at the jump | 23% / 38% | -0.28 / -0.26 | 100% | 31% | -27% | -16.30% | -17.80% / -15.64% | -16.30% |
| jump 2.5x ATR on the last minute of the 5m candle | before 1:00 | 13 | 0.1 | 10% under | 23% / 38% | -0.28 / -0.26 | 77% | 80% | -15% | +0.62% | +7.78% / -2.45% | +0.62% |
| jump 2.5x ATR on the minutes 1-4 of the 5m candle | all | 120 | 0.5 | at the jump | 38% / 38% | -0.25 / -0.24 | 100% | 59% | -20% | -6.87% | -8.81% / -5.23% | -4.52% |
| jump 2.5x ATR on the minutes 1-4 of the 5m candle | all | 120 | 0.5 | 10% under | 38% / 38% | -0.25 / -0.24 | 83% | 77% | -14% | -0.99% | -1.95% / -0.21% | -0.91% |
| jump 2.5x ATR on the minutes 1-4 of the 5m candle | dot same side in the last 5 min | 17 | 0.1 | at the jump | 29% / 47% | -0.67 / -0.78 | 100% | 59% | -19% | -6.86% | -9.61% / -6.01% | +0.93% |
| jump 2.5x ATR on the minutes 1-4 of the 5m candle | dot same side in the last 5 min | 17 | 0.1 | 10% under | 29% / 47% | -0.67 / -0.78 | 88% | 93% | -17% | +4.47% | +7.52% / +3.36% | +3.00% |
| jump 2.5x ATR on the minutes 1-4 of the 5m candle | dot on the OTHER side in the last 5 min | 20 | 0.1 | at the jump | 45% / 30% | -0.03 / -0.29 | 100% | 50% | -23% | -10.27% | -5.18% / -16.49% | -10.62% |
| jump 2.5x ATR on the minutes 1-4 of the 5m candle | dot on the OTHER side in the last 5 min | 20 | 0.1 | 10% under | 45% / 30% | -0.03 / -0.29 | 80% | 88% | -13% | +2.36% | +7.16% / -2.45% | -6.17% |
| jump 2.5x ATR on the minutes 1-4 of the 5m candle | calm day (11.5 ATR or less) | 38 | 0.1 | at the jump | 39% / 37% | -0.32 / -0.32 | 100% | 55% | -19% | -7.55% | -11.25% / -4.22% | -8.06% |
| jump 2.5x ATR on the minutes 1-4 of the 5m candle | calm day (11.5 ATR or less) | 38 | 0.1 | 10% under | 39% / 37% | -0.32 / -0.32 | 89% | 82% | -14% | +1.56% | +1.30% / +1.79% | -1.03% |
| jump 2.5x ATR on the minutes 1-4 of the 5m candle | before 1:00 | 52 | 0.2 | at the jump | 31% / 35% | -0.66 / -0.69 | 100% | 63% | -17% | -4.52% | -7.67% / -1.81% | -4.52% |
| jump 2.5x ATR on the minutes 1-4 of the 5m candle | before 1:00 | 52 | 0.2 | 10% under | 31% / 35% | -0.66 / -0.69 | 90% | 74% | -10% | -0.91% | -1.93% / -0.08% | -0.91% |

## Hard jump on a 1-minute candle: does it keep going? (2 ITM, bought in the jump's direction)

Jump = 1-minute candle body at least 1.5x or 2.5x the 1-minute ATR. SPY kept going = closed further that way 5 / 15 min later (avg move in ATR).

| Jump | Filter | Count | Per day | Bid | SPY kept going 5m / 15m | Avg move 5m / 15m (ATR) | Filled | +10% first | Median heat | Plan A avg | 1st half / 2nd half | Before 1:00 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| jump 1.5x ATR on the last minute of the 5m candle | all | 263 | 1.0 | at the jump | 46% / 45% | -0.16 / -0.18 | 100% | 70% | -11% | -1.11% | -1.17% / -1.08% | -0.72% |
| jump 1.5x ATR on the last minute of the 5m candle | all | 263 | 1.0 | 10% under | 46% / 45% | -0.16 / -0.18 | 44% | 77% | -8% | +1.21% | +1.34% / +1.07% | +1.29% |
| jump 1.5x ATR on the last minute of the 5m candle | dot same side in the last 5 min | 54 | 0.2 | at the jump | 48% / 46% | +0.03 / -0.09 | 100% | 76% | -7% | +1.12% | -4.18% / +5.35% | +0.45% |
| jump 1.5x ATR on the last minute of the 5m candle | dot same side in the last 5 min | 54 | 0.2 | 10% under | 48% / 46% | +0.03 / -0.09 | 41% | 73% | -9% | -0.05% | +1.68% / -3.09% | -4.05% |
| jump 1.5x ATR on the last minute of the 5m candle | dot on the OTHER side in the last 5 min | 40 | 0.2 | at the jump | 52% / 48% | -0.07 / -0.03 | 100% | 72% | -8% | +0.18% | +2.79% / -0.82% | -4.79% |
| jump 1.5x ATR on the last minute of the 5m candle | dot on the OTHER side in the last 5 min | 40 | 0.2 | 10% under | 52% / 48% | -0.07 / -0.03 | 40% | 75% | -5% | +0.46% | -0.77% / +1.41% | -2.43% |
| jump 1.5x ATR on the last minute of the 5m candle | calm day (11.5 ATR or less) | 48 | 0.2 | at the jump | 40% / 42% | -0.17 / -0.18 | 100% | 62% | -15% | -3.35% | -6.45% / -0.94% | -3.72% |
| jump 1.5x ATR on the last minute of the 5m candle | calm day (11.5 ATR or less) | 48 | 0.2 | 10% under | 40% / 42% | -0.17 / -0.18 | 52% | 72% | -10% | -0.50% | -4.16% / +3.45% | -0.26% |
| jump 1.5x ATR on the last minute of the 5m candle | before 1:00 | 130 | 0.5 | at the jump | 45% / 45% | -0.04 / +0.07 | 100% | 71% | -11% | -0.72% | +0.53% / -1.55% | -0.72% |
| jump 1.5x ATR on the last minute of the 5m candle | before 1:00 | 130 | 0.5 | 10% under | 45% / 45% | -0.04 / +0.07 | 40% | 77% | -8% | +1.29% | +2.23% / +0.41% | +1.29% |
| jump 1.5x ATR on the minutes 1-4 of the 5m candle | all | 1522 | 6.0 | at the jump | 48% / 48% | -0.07 / -0.04 | 100% | 67% | -11% | -1.44% | -2.26% / -0.61% | -1.43% |
| jump 1.5x ATR on the minutes 1-4 of the 5m candle | all | 1522 | 6.0 | 10% under | 48% / 48% | -0.07 / -0.04 | 40% | 79% | -7% | +1.86% | +1.60% / +2.18% | +2.67% |
| jump 1.5x ATR on the minutes 1-4 of the 5m candle | dot same side in the last 5 min | 330 | 1.3 | at the jump | 53% / 50% | -0.01 / -0.04 | 100% | 68% | -10% | -1.43% | -2.34% / -0.66% | -1.08% |
| jump 1.5x ATR on the minutes 1-4 of the 5m candle | dot same side in the last 5 min | 330 | 1.3 | 10% under | 53% / 50% | -0.01 / -0.04 | 33% | 78% | -8% | +1.89% | +0.98% / +2.91% | +2.09% |
| jump 1.5x ATR on the minutes 1-4 of the 5m candle | dot on the OTHER side in the last 5 min | 302 | 1.2 | at the jump | 51% / 49% | +0.06 / +0.03 | 100% | 72% | -8% | -0.67% | -1.23% / -0.08% | +0.05% |
| jump 1.5x ATR on the minutes 1-4 of the 5m candle | dot on the OTHER side in the last 5 min | 302 | 1.2 | 10% under | 51% / 49% | +0.06 / +0.03 | 37% | 79% | -5% | +1.54% | +1.63% / +1.43% | +4.43% |
| jump 1.5x ATR on the minutes 1-4 of the 5m candle | calm day (11.5 ATR or less) | 320 | 1.3 | at the jump | 49% / 48% | -0.00 / -0.12 | 100% | 68% | -12% | -2.08% | -3.84% / +0.15% | -2.50% |
| jump 1.5x ATR on the minutes 1-4 of the 5m candle | calm day (11.5 ATR or less) | 320 | 1.3 | 10% under | 49% / 48% | -0.00 / -0.12 | 53% | 81% | -6% | +2.76% | +1.20% / +5.13% | +2.23% |
| jump 1.5x ATR on the minutes 1-4 of the 5m candle | before 1:00 | 708 | 2.8 | at the jump | 47% / 48% | -0.09 / -0.15 | 100% | 68% | -11% | -1.43% | -2.65% / -0.03% | -1.43% |
| jump 1.5x ATR on the minutes 1-4 of the 5m candle | before 1:00 | 708 | 2.8 | 10% under | 47% / 48% | -0.09 / -0.15 | 43% | 81% | -6% | +2.67% | +2.19% / +3.43% | +2.67% |
| jump 2.5x ATR on the last minute of the 5m candle | all | 28 | 0.1 | at the jump | 29% / 39% | -0.58 / -0.15 | 100% | 54% | -21% | -7.56% | -4.68% / -10.88% | -9.83% |
| jump 2.5x ATR on the last minute of the 5m candle | all | 28 | 0.1 | 10% under | 29% / 39% | -0.58 / -0.15 | 86% | 96% | -6% | +7.73% | +9.18% / +5.69% | +5.70% |
| jump 2.5x ATR on the last minute of the 5m candle | before 1:00 | 13 | 0.1 | at the jump | 23% / 38% | -0.28 / -0.26 | 100% | 46% | -25% | -9.83% | -8.11% / -10.60% | -9.83% |
| jump 2.5x ATR on the last minute of the 5m candle | before 1:00 | 13 | 0.1 | 10% under | 23% / 38% | -0.28 / -0.26 | 77% | 90% | -5% | +5.70% | +9.22% / +4.19% | +5.70% |
| jump 2.5x ATR on the minutes 1-4 of the 5m candle | all | 120 | 0.5 | at the jump | 38% / 38% | -0.25 / -0.24 | 100% | 66% | -13% | -1.45% | -3.72% / +0.47% | -2.25% |
| jump 2.5x ATR on the minutes 1-4 of the 5m candle | all | 120 | 0.5 | 10% under | 38% / 38% | -0.25 / -0.24 | 64% | 86% | -7% | +4.13% | +4.51% / +3.78% | +1.30% |
| jump 2.5x ATR on the minutes 1-4 of the 5m candle | dot same side in the last 5 min | 17 | 0.1 | at the jump | 29% / 47% | -0.67 / -0.78 | 100% | 65% | -14% | -1.83% | -8.16% / +0.12% | -1.16% |
| jump 2.5x ATR on the minutes 1-4 of the 5m candle | dot same side in the last 5 min | 17 | 0.1 | 10% under | 29% / 47% | -0.67 / -0.78 | 65% | 82% | -11% | +2.83% | +0.49% / +4.16% | +2.23% |
| jump 2.5x ATR on the minutes 1-4 of the 5m candle | dot on the OTHER side in the last 5 min | 20 | 0.1 | at the jump | 45% / 30% | -0.03 / -0.29 | 100% | 60% | -13% | -3.69% | -0.26% / -7.89% | -9.05% |
| jump 2.5x ATR on the minutes 1-4 of the 5m candle | dot on the OTHER side in the last 5 min | 20 | 0.1 | 10% under | 45% / 30% | -0.03 / -0.29 | 55% | 100% | -5% | +9.19% | +9.18% / +9.20% | +9.20% |
| jump 2.5x ATR on the minutes 1-4 of the 5m candle | calm day (11.5 ATR or less) | 38 | 0.1 | at the jump | 39% / 37% | -0.32 / -0.32 | 100% | 66% | -16% | -2.10% | -5.04% / +0.54% | -5.48% |
| jump 2.5x ATR on the minutes 1-4 of the 5m candle | calm day (11.5 ATR or less) | 38 | 0.1 | 10% under | 39% / 37% | -0.32 / -0.32 | 79% | 83% | -8% | +3.43% | +2.71% / +4.27% | +0.08% |
| jump 2.5x ATR on the minutes 1-4 of the 5m candle | before 1:00 | 52 | 0.2 | at the jump | 31% / 35% | -0.66 / -0.69 | 100% | 65% | -13% | -2.25% | -7.48% / +2.24% | -2.25% |
| jump 2.5x ATR on the minutes 1-4 of the 5m candle | before 1:00 | 52 | 0.2 | 10% under | 31% / 35% | -0.66 / -0.69 | 69% | 78% | -11% | +1.30% | +1.53% / +1.07% | +1.30% |

How to read it: a plan helps if its Plan A avg beats 'at the dot' in BOTH halves. A filter plan (green candle, fear/greed under
its average, quits driving, limit bids) also helps if the dots it skipped did worse at the dot than the ones it took.
