# DIP IN A TREND - every candle, 10:00-3:00, 2026, real 0DTE options $0.45-1.00

SPY + QQQ | charts 1m, 2m, 3m | Jan 1 2026 to 2026-10-31 (209 trading days). A setup fires on the first candle its agreement turns true (then 10 min cool-down per chart and side). Buys the same-day call (long) / put (short) closest to $0.70 inside $0.45-1.00 at the 1-minute close when the candle closes (+ max(1c, 0.5%)); 1-minute closes after that (- the same), up to 60 min. '+10% before -20%' = the option closed 10% up before it ever closed 20% down. Half 1 = Jan-Jun, half 2 = Jul-now. DATA ONLY.

Setups:
- **A** = 15m trend your way + price on the OTHER side of VWAP + your Vix Fix side under 85
- **B** = 15m trend your way + price on the OTHER side of VWAP
- **C** = 60m trend your way + price on the OTHER side of VWAP + your Vix Fix side under 85
- **D** = 15m AND 60m trend your way + price on the OTHER side of VWAP + your Vix Fix side under 85
- **E** = ANGLE FLATTENS 23 + neither Vix Fix side 85+
- **T** = BASELINE: random candle, side = the 15m trend
- **R** = BASELINE: random candle, random side

## A) How often each setup gets +10% BEFORE -20% (the number you trade)

| Setup | Fires/day | +10% before -20% | Half 1 / Half 2 | +10% before -30% | +15% before -20% | +20% before -30% | Hit +10% at all | Median min to +10% |
|---|---|---|---|---|---|---|---|---|
| **A** | 22.3 | **52%** | 53% / 50% | 60% | 46% | 50% | 74% | 4 |
| **B** | 19.6 | **51%** | 53% / 49% | 60% | 46% | 49% | 73% | 4 |
| **C** | 25.3 | **53%** | 52% / 54% | 61% | 47% | 50% | 73% | 4 |
| **D** | 14.9 | **53%** | 53% / 53% | 61% | 47% | 51% | 74% | 4 |
| **E** | 0.4 | **53%** | 55% / 51% | 64% | 47% | 55% | 85% | 3 |
| **T** | - | **51%** | 51% / 51% | 60% | 45% | 49% | 73% | 4 |
| **R** | - | **51%** | 50% / 52% | 58% | 45% | 47% | 70% | 4 |

## B) What each plan pays per trade (avg % on the premium)

| Setup | Trades | Sell +10% / stop -20% | Sell +15% / stop -20% | Sell +20% / stop -30% | Lock +10% then trail 10 (stop -20%) | Hold 30 min | Avg best | Avg worst |
|---|---|---|---|---|---|---|---|---|
| **A** | 4652 | **-2.8%** | -2.7% | -2.6% | -3.3% | +0.3% | +68% | -47% |
| **B** | 4097 | **-2.9%** | -2.7% | -2.5% | -3.5% | -0.1% | +68% | -47% |
| **C** | 5293 | **-2.5%** | -2.4% | -2.7% | -3.1% | -1.9% | +63% | -48% |
| **D** | 3122 | **-2.4%** | -2.3% | -2.3% | -3.4% | -0.3% | +63% | -47% |
| **E** | 74 | **-1.6%** | -0.7% | +3.5% | +3.4% | +38.6% | +150% | -44% |
| **T** | 4645 | **-2.9%** | -2.9% | -3.0% | -3.5% | -2.3% | +62% | -47% |
| **R** | 4653 | **-3.2%** | -3.4% | -4.5% | -4.1% | -4.8% | +58% | -49% |

## C) Sell +10% / stop -20% by half (must be positive in BOTH to count)

| Setup | Half 1 avg | Half 2 avg | Half 1 win | Half 2 win |
|---|---|---|---|---|
| **A** | -2.2% | -3.5% | 53% | 50% |
| **B** | -2.1% | -3.9% | 53% | 49% |
| **C** | -2.8% | -2.3% | 52% | 54% |
| **D** | -2.1% | -2.7% | 53% | 53% |
| **E** | -0.4% | -2.6% | 55% | 51% |
| **T** | -2.7% | -3.3% | 52% | 51% |
| **R** | -3.3% | -3.0% | 50% | 52% |

## DA) Setup A split up (+10% before -20% and the +10%/-20% plan)

| Group | Trades | +10% before -20% | Plan avg |
|---|---|---|---|
| QQQ 1m | 927 | 52% | -2.6% |
| QQQ 2m | 723 | 51% | -3.0% |
| QQQ 3m | 604 | 50% | -3.3% |
| SPY 1m | 999 | 53% | -2.7% |
| SPY 2m | 756 | 53% | -2.6% |
| SPY 3m | 643 | 53% | -2.7% |
| PUTS | 2422 | 55% | -1.2% |
| CALLS | 2230 | 49% | -4.5% |
| 10:00 | 1739 | 51% | -2.7% |
| 11:00 | 815 | 54% | -1.4% |
| 12:00 | 750 | 50% | -4.5% |
| 13:00 | 648 | 55% | -1.4% |
| 14:00 | 694 | 50% | -4.0% |
| 15:00 | 6 | 33% | -15.9% |

## DD) Setup D split up (+10% before -20% and the +10%/-20% plan)

| Group | Trades | +10% before -20% | Plan avg |
|---|---|---|---|
| QQQ 1m | 638 | 54% | -1.7% |
| QQQ 2m | 489 | 52% | -2.4% |
| QQQ 3m | 404 | 52% | -2.7% |
| SPY 1m | 666 | 54% | -2.5% |
| SPY 2m | 495 | 53% | -2.6% |
| SPY 3m | 430 | 53% | -2.8% |
| PUTS | 1571 | 55% | -1.1% |
| CALLS | 1551 | 51% | -3.8% |
| 10:00 | 1155 | 51% | -3.2% |
| 11:00 | 518 | 53% | -1.7% |
| 12:00 | 492 | 55% | -2.4% |
| 13:00 | 449 | 60% | +0.2% |
| 14:00 | 503 | 51% | -3.6% |
| 15:00 | 5 | 40% | -13.0% |

## DE) Setup E split up (+10% before -20% and the +10%/-20% plan)

| Group | Trades | +10% before -20% | Plan avg |
|---|---|---|---|
| QQQ 1m | 21 | 52% | -2.1% |
| QQQ 2m | 11 | 55% | -1.6% |
| QQQ 3m | 8 | 62% | +8.5% |
| SPY 1m | 17 | 47% | -6.4% |
| SPY 2m | 14 | 57% | +0.6% |
| SPY 3m | 3 | 33% | -8.6% |
| PUTS | 36 | 58% | +3.1% |
| CALLS | 38 | 47% | -6.1% |
| 10:00 | 25 | 60% | +1.2% |
| 11:00 | 14 | 50% | -1.2% |
| 12:00 | 16 | 38% | -8.9% |
| 13:00 | 7 | 57% | -2.5% |
| 14:00 | 12 | 58% | +2.3% |

Runtime 3.8 min. This is math/data, not financial advice.