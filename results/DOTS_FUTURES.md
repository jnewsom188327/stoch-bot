# Dots on futures (MES)

Feed sip. 2025-11-05 to 2026-11-10, 255 days. SPY 1-minute bars stand in for MES: $1 of SPY = $50 per MES contract.
Every white dot, 1 MES contract, one trade per dot (overlaps allowed). Costs: 1 tick slippage in and out, stops fill 1 tick worse, $1.24 fees round trip.
R = result divided by the money at risk to the stop. Max hold 60 min. Worst drawdown = biggest dip in the running total over the year, 1 contract.

## Every stop x exit, every dot (at the dot (next open))

| Stop | Exit | Trades/day | Win rate | Avg $/trade | Avg R | Profit factor | 1st half / 2nd half ($/trade) | $/day | Worst drawdown | Avg hold |
|---|---|---|---|---|---|---|---|---|---|---|
| swing (past the last 5 bars' extreme) | +1 ATR target | 29.4 | 47% | $-3.25 | -0.30R | 0.65 | $-3.19 / $-3.31 | $-95.5 | $-24,502 | 3m |
| swing (past the last 5 bars' extreme) | +2 ATR target | 29.4 | 32% | $-3.67 | -0.32R | 0.70 | $-3.59 / $-3.75 | $-107.7 | $-27,767 | 6m |
| swing (past the last 5 bars' extreme) | +3 ATR target | 29.4 | 23% | $-4.21 | -0.36R | 0.70 | $-4.41 / $-4.01 | $-123.5 | $-32,349 | 8m |
| swing (past the last 5 bars' extreme) | trend line break | 29.4 | 26% | $-4.28 | -0.37R | 0.56 | $-4.45 / $-4.11 | $-125.6 | $-32,353 | 5m |
| swing (past the last 5 bars' extreme) | fear/greed curl | 29.4 | 28% | $-4.40 | -0.37R | 0.63 | $-4.49 / $-4.31 | $-129.0 | $-33,472 | 6m |
| swing (past the last 5 bars' extreme) | out at 15 min | 29.4 | 25% | $-4.25 | -0.37R | 0.66 | $-4.54 / $-3.97 | $-124.7 | $-32,672 | 7m |
| swing (past the last 5 bars' extreme) | out at 30 min | 29.4 | 20% | $-4.41 | -0.38R | 0.68 | $-4.46 / $-4.35 | $-129.3 | $-34,240 | 11m |
| 1 ATR | +1 ATR target | 29.4 | 50% | $-3.16 | -0.23R | 0.67 | $-3.03 / $-3.28 | $-92.7 | $-24,000 | 2m |
| 1 ATR | +2 ATR target | 29.4 | 33% | $-3.35 | -0.25R | 0.74 | $-3.16 / $-3.53 | $-98.3 | $-25,619 | 5m |
| 1 ATR | +3 ATR target | 29.4 | 24% | $-3.93 | -0.28R | 0.73 | $-4.10 / $-3.76 | $-115.3 | $-30,429 | 8m |
| 1 ATR | trend line break | 29.4 | 30% | $-4.18 | -0.31R | 0.61 | $-4.03 / $-4.33 | $-122.8 | $-31,930 | 5m |
| 1 ATR | fear/greed curl | 29.4 | 30% | $-4.05 | -0.31R | 0.68 | $-4.00 / $-4.10 | $-118.9 | $-31,325 | 6m |
| 1 ATR | out at 15 min | 29.4 | 27% | $-3.91 | -0.30R | 0.71 | $-3.95 / $-3.87 | $-114.9 | $-30,577 | 7m |
| 1 ATR | out at 30 min | 29.4 | 21% | $-4.22 | -0.30R | 0.71 | $-4.34 / $-4.10 | $-123.8 | $-32,978 | 11m |
| 2 ATR | +1 ATR target | 29.4 | 66% | $-3.28 | -0.12R | 0.72 | $-2.87 / $-3.69 | $-96.4 | $-25,019 | 5m |
| 2 ATR | +2 ATR target | 29.4 | 49% | $-3.51 | -0.13R | 0.80 | $-2.76 / $-4.23 | $-102.9 | $-26,801 | 11m |
| 2 ATR | +3 ATR target | 29.4 | 39% | $-4.18 | -0.15R | 0.80 | $-3.92 / $-4.44 | $-122.8 | $-32,616 | 16m |
| 2 ATR | trend line break | 29.4 | 36% | $-4.62 | -0.17R | 0.63 | $-4.60 / $-4.64 | $-135.6 | $-35,115 | 8m |
| 2 ATR | fear/greed curl | 29.4 | 44% | $-4.45 | -0.17R | 0.73 | $-4.04 / $-4.85 | $-130.6 | $-34,555 | 11m |
| 2 ATR | out at 15 min | 29.4 | 39% | $-4.44 | -0.17R | 0.73 | $-4.32 / $-4.57 | $-130.4 | $-34,732 | 11m |
| 2 ATR | out at 30 min | 29.4 | 35% | $-4.50 | -0.16R | 0.78 | $-4.22 / $-4.77 | $-132.0 | $-34,832 | 19m |

## Every stop x exit, every dot (limit 0.25 ATR better (5 min))

| Stop | Exit | Trades/day | Win rate | Avg $/trade | Avg R | Profit factor | 1st half / 2nd half ($/trade) | $/day | Worst drawdown | Avg hold |
|---|---|---|---|---|---|---|---|---|---|---|
| swing (past the last 5 bars' extreme) | +1 ATR target | 25.0 | 43% | $-2.89 | -0.36R | 0.65 | $-2.90 / $-2.87 | $-72.2 | $-18,693 | 2m |
| swing (past the last 5 bars' extreme) | +2 ATR target | 25.0 | 26% | $-4.04 | -0.44R | 0.64 | $-3.84 / $-4.24 | $-101.2 | $-26,064 | 5m |
| swing (past the last 5 bars' extreme) | +3 ATR target | 25.0 | 20% | $-4.38 | -0.46R | 0.65 | $-4.62 / $-4.14 | $-109.5 | $-28,409 | 7m |
| swing (past the last 5 bars' extreme) | trend line break | 25.0 | 23% | $-4.65 | -0.50R | 0.49 | $-4.71 / $-4.60 | $-116.5 | $-29,850 | 4m |
| swing (past the last 5 bars' extreme) | fear/greed curl | 25.0 | 23% | $-4.57 | -0.49R | 0.58 | $-4.60 / $-4.54 | $-114.3 | $-29,384 | 5m |
| swing (past the last 5 bars' extreme) | out at 15 min | 25.0 | 21% | $-4.45 | -0.50R | 0.60 | $-4.49 / $-4.42 | $-111.4 | $-28,869 | 6m |
| swing (past the last 5 bars' extreme) | out at 30 min | 25.0 | 17% | $-4.48 | -0.50R | 0.64 | $-4.29 / $-4.67 | $-112.2 | $-29,184 | 9m |
| 1 ATR | +1 ATR target | 25.0 | 52% | $-2.52 | -0.20R | 0.73 | $-2.49 / $-2.56 | $-63.1 | $-16,495 | 3m |
| 1 ATR | +2 ATR target | 25.0 | 33% | $-3.40 | -0.26R | 0.74 | $-2.94 / $-3.85 | $-85.1 | $-22,242 | 6m |
| 1 ATR | +3 ATR target | 25.0 | 25% | $-3.82 | -0.27R | 0.74 | $-3.69 / $-3.95 | $-95.6 | $-25,203 | 8m |
| 1 ATR | trend line break | 25.0 | 30% | $-4.38 | -0.32R | 0.59 | $-4.25 / $-4.51 | $-109.7 | $-28,445 | 5m |
| 1 ATR | fear/greed curl | 25.0 | 30% | $-4.08 | -0.31R | 0.68 | $-3.93 / $-4.22 | $-102.1 | $-26,630 | 7m |
| 1 ATR | out at 15 min | 25.0 | 27% | $-4.03 | -0.31R | 0.70 | $-3.89 / $-4.16 | $-100.8 | $-26,557 | 8m |
| 1 ATR | out at 30 min | 25.0 | 22% | $-3.98 | -0.29R | 0.73 | $-3.64 / $-4.31 | $-99.6 | $-26,311 | 12m |
| 2 ATR | +1 ATR target | 25.0 | 67% | $-2.60 | -0.11R | 0.77 | $-1.95 / $-3.24 | $-65.1 | $-17,087 | 5m |
| 2 ATR | +2 ATR target | 25.0 | 49% | $-3.93 | -0.14R | 0.78 | $-2.98 / $-4.85 | $-98.4 | $-25,502 | 11m |
| 2 ATR | +3 ATR target | 25.0 | 39% | $-4.45 | -0.15R | 0.79 | $-4.00 / $-4.88 | $-111.3 | $-28,952 | 16m |
| 2 ATR | trend line break | 25.0 | 36% | $-5.12 | -0.19R | 0.60 | $-4.82 / $-5.42 | $-128.2 | $-33,129 | 8m |
| 2 ATR | fear/greed curl | 25.0 | 44% | $-4.83 | -0.18R | 0.71 | $-4.27 / $-5.38 | $-120.9 | $-31,608 | 11m |
| 2 ATR | out at 15 min | 25.0 | 39% | $-4.84 | -0.18R | 0.71 | $-4.29 / $-5.38 | $-121.2 | $-31,842 | 11m |
| 2 ATR | out at 30 min | 25.0 | 35% | $-4.76 | -0.17R | 0.76 | $-3.87 / $-5.61 | $-119.0 | $-31,011 | 19m |

## Filters on: limit 0.25 ATR better (5 min) · stop 1 ATR · exit +1 ATR target

| Filter | Trades/day | Win rate | Avg $/trade | Avg R | Profit factor | 1st half / 2nd half ($/trade) | $/day | Worst drawdown | Avg hold |
|---|---|---|---|---|---|---|---|---|---|
| every dot | 25.0 | 52% | $-2.52 | -0.20R | 0.73 | $-2.49 / $-2.56 | $-63.1 | $-16,495 | 3m |
| before 1:00 | 13.0 | 53% | $-2.19 | -0.14R | 0.79 | $-1.83 / $-2.55 | $-28.6 | $-7,603 | 3m |
| busy day | 8.6 | 53% | $-1.83 | -0.08R | 0.86 | $-1.54 / $-2.31 | $-15.7 | $-4,537 | 3m |
| day not stretched | 5.7 | 51% | $-2.52 | -0.13R | 0.81 | $-2.34 / $-2.70 | $-14.3 | $-3,947 | 3m |
| trend line your way | 4.0 | 51% | $-2.53 | -0.20R | 0.73 | $-2.44 / $-2.62 | $-10.1 | $-2,737 | 3m |
| busy + trend line your way | 1.4 | 54% | $-1.68 | -0.05R | 0.88 | $-0.35 / $-3.74 | $-2.3 | $-904 | 3m |
| pegged + other side bottomed | 7.4 | 50% | $-3.07 | -0.22R | 0.69 | $-3.98 / $-2.24 | $-22.8 | $-6,120 | 2m |
| pegged + calm day | 1.7 | 51% | $-3.08 | -0.13R | 0.77 | $-4.66 / $-1.65 | $-5.2 | $-1,599 | 3m |
| your rules: 10:00+, stressed, solid fear, averages turned | 3.2 | 51% | $-2.84 | -0.20R | 0.71 | $-3.43 / $-2.31 | $-9.2 | $-2,605 | 3m |
| calls only | 12.0 | 52% | $-2.34 | -0.19R | 0.75 | $-2.50 / $-2.18 | $-28.0 | $-7,392 | 2m |
| puts only | 13.0 | 51% | $-2.69 | -0.21R | 0.71 | $-2.47 / $-2.91 | $-35.1 | $-9,290 | 3m |

## Filters on: limit 0.25 ATR better (5 min) · stop 2 ATR · exit +1 ATR target

| Filter | Trades/day | Win rate | Avg $/trade | Avg R | Profit factor | 1st half / 2nd half ($/trade) | $/day | Worst drawdown | Avg hold |
|---|---|---|---|---|---|---|---|---|---|
| every dot | 25.0 | 67% | $-2.60 | -0.11R | 0.77 | $-1.95 / $-3.24 | $-65.1 | $-17,087 | 5m |
| before 1:00 | 13.0 | 67% | $-2.67 | -0.09R | 0.80 | $-1.16 / $-4.14 | $-34.8 | $-9,203 | 6m |
| busy day | 8.6 | 68% | $-2.25 | -0.05R | 0.87 | $-0.74 / $-4.72 | $-19.3 | $-5,563 | 6m |
| day not stretched | 5.7 | 66% | $-2.97 | -0.08R | 0.82 | $-1.69 / $-4.32 | $-16.9 | $-4,586 | 6m |
| trend line your way | 4.0 | 69% | $-1.51 | -0.08R | 0.86 | $-0.57 / $-2.41 | $-6.1 | $-2,046 | 5m |
| busy + trend line your way | 1.4 | 70% | $+0.28 | -0.00R | 1.02 | $+2.02 / $-2.43 | $+0.4 | $-703 | 6m |
| pegged + other side bottomed | 7.4 | 67% | $-3.36 | -0.11R | 0.72 | $-3.80 / $-2.96 | $-24.9 | $-6,636 | 5m |
| pegged + calm day | 1.7 | 65% | $-4.60 | -0.09R | 0.75 | $-4.21 / $-4.94 | $-7.8 | $-2,214 | 6m |
| your rules: 10:00+, stressed, solid fear, averages turned | 3.2 | 67% | $-2.55 | -0.10R | 0.79 | $-2.06 / $-3.00 | $-8.2 | $-2,418 | 5m |
| calls only | 12.0 | 67% | $-2.66 | -0.11R | 0.77 | $-2.55 / $-2.76 | $-31.8 | $-8,574 | 5m |
| puts only | 13.0 | 67% | $-2.55 | -0.11R | 0.77 | $-1.41 / $-3.69 | $-33.3 | $-9,099 | 6m |

## Filters on: limit 0.25 ATR better (5 min) · stop swing (past the last 5 bars' extreme) · exit +1 ATR target

| Filter | Trades/day | Win rate | Avg $/trade | Avg R | Profit factor | 1st half / 2nd half ($/trade) | $/day | Worst drawdown | Avg hold |
|---|---|---|---|---|---|---|---|---|---|
| every dot | 25.0 | 43% | $-2.89 | -0.36R | 0.65 | $-2.90 / $-2.87 | $-72.2 | $-18,693 | 2m |
| before 1:00 | 13.0 | 41% | $-2.68 | -0.32R | 0.70 | $-2.59 / $-2.77 | $-35.0 | $-9,055 | 2m |
| busy day | 8.6 | 40% | $-2.63 | -0.26R | 0.77 | $-2.35 / $-3.07 | $-22.5 | $-5,964 | 2m |
| day not stretched | 5.7 | 39% | $-2.83 | -0.31R | 0.74 | $-2.92 / $-2.74 | $-16.1 | $-4,336 | 2m |
| trend line your way | 4.0 | 48% | $-2.54 | -0.30R | 0.71 | $-2.35 / $-2.72 | $-10.2 | $-2,849 | 3m |
| busy + trend line your way | 1.4 | 48% | $-1.81 | -0.21R | 0.86 | $-1.34 / $-2.55 | $-2.5 | $-999 | 3m |
| pegged + other side bottomed | 7.4 | 41% | $-3.53 | -0.39R | 0.60 | $-4.14 / $-2.96 | $-26.1 | $-6,862 | 2m |
| pegged + calm day | 1.7 | 39% | $-3.06 | -0.29R | 0.73 | $-4.23 / $-2.01 | $-5.2 | $-1,571 | 2m |
| your rules: 10:00+, stressed, solid fear, averages turned | 3.2 | 50% | $-3.08 | -0.25R | 0.69 | $-3.21 / $-2.96 | $-10.0 | $-2,930 | 3m |
| calls only | 12.0 | 44% | $-2.58 | -0.34R | 0.68 | $-2.58 / $-2.57 | $-30.9 | $-7,969 | 2m |
| puts only | 13.0 | 42% | $-3.17 | -0.38R | 0.62 | $-3.19 / $-3.15 | $-41.3 | $-10,765 | 2m |

How to read it: a setup has an edge on futures only if Avg $/trade is positive in BOTH halves after costs.
$/day is per MES contract with every qualifying dot taken; you'd take fewer, one at a time.
