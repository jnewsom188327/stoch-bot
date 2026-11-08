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

How to read it: a plan helps if its Plan A avg beats 'at the dot' in BOTH halves. A filter plan (green candle, fear/greed under
its average, quits driving, limit bids) also helps if the dots it skipped did worse at the dot than the ones it took.
