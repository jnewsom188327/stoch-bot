# NO STOP - time and HEAT to +10% / +15% / +20% - every setup, 10:00-3:00, 2026, real 0DTE options $0.45-1.00

SPY + QQQ | charts 1m, 2m, 3m, 5m | Jan 1 2026 to 2026-10-31 (209 trading days). Same fires as the dip test. NO STOP: each option is watched up to 60 minutes (or 3:55) on 1-minute closes after the fill (+/- max(1c, 0.5%)). HEAT = how far the option was DOWN (worst close) before it first reached the target. Heat 0% = it never went red first. Half 1 = Jan-Jun, half 2 = Jul-now. DATA ONLY.

Setups:
- **A** = 15m trend your way + price on the OTHER side of VWAP + your Vix Fix side under 85
- **B** = 15m trend your way + price on the OTHER side of VWAP
- **C** = 60m trend your way + price on the OTHER side of VWAP + your Vix Fix side under 85
- **D** = 15m AND 60m trend your way + price on the OTHER side of VWAP + your Vix Fix side under 85
- **E** = ANGLE FLATTENS 23 + neither Vix Fix side 85+
- **T** = BASELINE: random candle, side = the 15m trend
- **R** = BASELINE: random candle, random side

## A) Reaching +10% with NO stop

| Setup | Trades | Fires/day | Reached +10% | Half 1 / Half 2 | Within 2 min | 5 min | 10 min | 30 min | Median min | Never got there: avg end |
|---|---|---|---|---|---|---|---|---|---|---|
| **A** | 5769 | 27.6 | **73%** | 75% / 72% | 21% | 38% | 51% | 66% | 5 | -59% |
| **B** | 5212 | 24.9 | **73%** | 74% / 72% | 21% | 38% | 50% | 66% | 5 | -58% |
| **C** | 6428 | 30.8 | **72%** | 72% / 73% | 22% | 39% | 51% | 66% | 5 | -59% |
| **D** | 3868 | 18.5 | **74%** | 74% / 74% | 22% | 39% | 52% | 67% | 5 | -59% |
| **E** | 84 | 0.4 | **85%** | 88% / 82% | 21% | 51% | 61% | 81% | 4 | -64% |
| **T** | 5755 | - | **74%** | 74% / 73% | 21% | 38% | 50% | 66% | 5 | -58% |
| **R** | 5763 | - | **71%** | 71% / 70% | 19% | 36% | 48% | 64% | 5 | -57% |

## B) HEAT before +10% (only the trades that got there) - how far down it went first

| Setup | Got +10% | Never red first | Heat under 10% | under 20% | under 30% | under 50% | Median heat | 75% of trades | 90% of trades |
|---|---|---|---|---|---|---|---|---|---|
| **A** | 4238 | 31% | 53% | **71%** | 82% | 95% | -9% | -23% | -39% |
| **B** | 3810 | 31% | 53% | **71%** | 83% | 95% | -9% | -23% | -39% |
| **C** | 4650 | 33% | 56% | **73%** | 83% | 96% | -8% | -22% | -38% |
| **D** | 2868 | 33% | 55% | **71%** | 83% | 95% | -8% | -23% | -38% |
| **E** | 71 | 30% | 52% | **66%** | 77% | 93% | -9% | -28% | -41% |
| **T** | 4231 | 31% | 53% | **71%** | 82% | 95% | -8% | -23% | -40% |
| **R** | 4071 | 31% | 53% | **72%** | 83% | 95% | -9% | -22% | -39% |

## C) Same for +15% and +20%

| Setup | Reached +15% | Median min | Median heat | 75% heat | Reached +20% | Median min | Median heat | 75% heat |
|---|---|---|---|---|---|---|---|---|
| **A** | 68% | 7 | -10% | -25% | 63% | 9 | -11% | -26% |
| **B** | 68% | 7 | -10% | -25% | 62% | 9 | -11% | -26% |
| **C** | 67% | 7 | -9% | -24% | 62% | 9 | -10% | -26% |
| **D** | 69% | 7 | -10% | -25% | 64% | 9 | -11% | -26% |
| **E** | 79% | 6 | -9% | -29% | 77% | 6 | -13% | -29% |
| **T** | 68% | 7 | -11% | -25% | 63% | 10 | -12% | -27% |
| **R** | 65% | 7 | -11% | -25% | 59% | 10 | -12% | -26% |

## D) What the heat says: if you hold through X% down with NO stop, how many still reach +10%?

Each column = trades that went at least that far red BEFORE reaching +10%, and the share of those that still came back to +10%.

| Setup | Went -10% | came back | Went -20% | came back | Went -30% | came back | Went -50% | came back |
|---|---|---|---|---|---|---|---|---|
| **A** | 3535 | **57%** | 2756 | **45%** | 2261 | **33%** | 1561 | **14%** |
| **B** | 3196 | **56%** | 2504 | **44%** | 2044 | **32%** | 1413 | **13%** |
| **C** | 3833 | **54%** | 3043 | **42%** | 2536 | **31%** | 1780 | **12%** |
| **D** | 2287 | **56%** | 1818 | **45%** | 1494 | **33%** | 1021 | **14%** |
| **E** | 47 | **72%** | 37 | **65%** | 29 | **55%** | 18 | **28%** |
| **T** | 3515 | **57%** | 2756 | **45%** | 2239 | **33%** | 1529 | **14%** |
| **R** | 3597 | **53%** | 2839 | **41%** | 2338 | **29%** | 1635 | **12%** |

## EA) Setup A split up (no stop)

| Group | Trades | Reached +10% | Median min | Median heat (got there) | 75% heat |
|---|---|---|---|---|---|
| QQQ 1m | 927 | 74% | 5 | -9% | -24% |
| QQQ 2m | 723 | 73% | 6 | -11% | -25% |
| QQQ 3m | 604 | 74% | 5 | -10% | -25% |
| QQQ 5m | 547 | 74% | 5 | -8% | -22% |
| SPY 1m | 999 | 73% | 5 | -7% | -22% |
| SPY 2m | 756 | 73% | 5 | -9% | -22% |
| SPY 3m | 643 | 73% | 5 | -8% | -22% |
| SPY 5m | 570 | 73% | 5 | -9% | -21% |
| PUTS | 2999 | 75% | 5 | -9% | -22% |
| CALLS | 2770 | 72% | 5 | -9% | -25% |
| 10:00 | 2204 | 74% | 5 | -9% | -24% |
| 11:00 | 1000 | 72% | 5 | -8% | -20% |
| 12:00 | 924 | 73% | 7 | -10% | -23% |
| 13:00 | 796 | 76% | 6 | -9% | -22% |
| 14:00 | 839 | 71% | 5 | -8% | -25% |
| 15:00 | 6 | 67% | 11 | -13% | -28% |

## ED) Setup D split up (no stop)

| Group | Trades | Reached +10% | Median min | Median heat (got there) | 75% heat |
|---|---|---|---|---|---|
| QQQ 1m | 638 | 76% | 5 | -6% | -23% |
| QQQ 2m | 489 | 74% | 5 | -9% | -24% |
| QQQ 3m | 404 | 75% | 5 | -8% | -27% |
| QQQ 5m | 368 | 73% | 5 | -8% | -23% |
| SPY 1m | 666 | 74% | 5 | -6% | -22% |
| SPY 2m | 495 | 73% | 5 | -8% | -21% |
| SPY 3m | 430 | 74% | 5 | -8% | -22% |
| SPY 5m | 378 | 74% | 6 | -9% | -23% |
| PUTS | 1941 | 76% | 5 | -8% | -22% |
| CALLS | 1927 | 72% | 5 | -8% | -24% |
| 10:00 | 1459 | 73% | 4 | -8% | -25% |
| 11:00 | 632 | 71% | 4 | -5% | -21% |
| 12:00 | 604 | 77% | 6 | -8% | -22% |
| 13:00 | 558 | 77% | 6 | -8% | -19% |
| 14:00 | 610 | 73% | 5 | -7% | -27% |
| 15:00 | 5 | 80% | 11 | -13% | -28% |

## EE) Setup E split up (no stop)

| Group | Trades | Reached +10% | Median min | Median heat (got there) | 75% heat |
|---|---|---|---|---|---|
| QQQ 1m | 21 | 86% | 5 | -14% | -30% |
| QQQ 2m | 11 | 100% | 3 | -6% | -35% |
| QQQ 3m | 8 | 75% | 4 | -12% | -18% |
| QQQ 5m | 5 | 60% | 5 | -0% | -1% |
| SPY 1m | 17 | 71% | 5 | -9% | -30% |
| SPY 2m | 14 | 93% | 4 | -6% | -32% |
| SPY 3m | 3 | 100% | 16 | -21% | -22% |
| SPY 5m | 5 | 100% | 5 | -15% | -16% |
| PUTS | 39 | 92% | 4 | -9% | -29% |
| CALLS | 45 | 78% | 5 | -9% | -24% |
| 10:00 | 31 | 77% | 4 | -4% | -17% |
| 11:00 | 17 | 94% | 5 | -11% | -30% |
| 12:00 | 16 | 100% | 7 | -28% | -37% |
| 13:00 | 8 | 75% | 4 | -16% | -18% |
| 14:00 | 12 | 75% | 2 | -7% | -9% |

Runtime 3.7 min. This is math/data, not financial advice.