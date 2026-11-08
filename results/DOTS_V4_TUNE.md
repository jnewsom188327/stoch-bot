# White dot rules - every setting, 130 days, real option prices (backtest only, page unchanged)

Feed sip. TRAIN 2026-05-05 to 2026-09-04 (86 days), TEST 2026-09-08 to 2026-11-06 (44 days).
Win / Avg R: 1 OTM 0DTE, +10% target, -25% stop, out at 30 min, after the spread. Turn = SPY moves 1 ATR your way before 0.5 ATR against (30 min). Jump = 2 ATR your way first.

## Baseline: every minute 9:45-3:00, both directions (what random entries get)
| Setting | Dots/day | Win (train \| test) | Avg R % | Turn 1 ATR first | Jump 2 ATR first |
|---|---|---|---|---|---|
| every minute | - | 68% \| 67% | -4.49 \| -4.73 | 33% \| 34% | 20% \| 21% |

## Your current dot rules
| Setting | Dots/day | Win (train \| test) | Avg R % | Turn 1 ATR first | Jump 2 ATR first |
|---|---|---|---|---|---|
| lb=16 drive=2.0 stall=2 tol=0.2 away=1.5 body=0.6 | 31.6 | 67% \| 66% | -5.88 \| -6.23 | 32% \| 32% | 20% \| 20% |

## Best 30 settings for the option trade (ranked by the worse of train and test R)
| Setting | Dots/day | Win (train \| test) | Avg R % | Turn 1 ATR first | Jump 2 ATR first |
|---|---|---|---|---|---|
| lb=8 drive=3.0 stall=4 tol=0.3 away=0.75 body=0.6 | 2.5 | 71% \| 71% | -4.78 \| -4.05 | 36% \| 32% | 20% \| 17% |
| lb=8 drive=3.0 stall=4 tol=0.3 away=0.75 body=0.8 | 2.5 | 71% \| 72% | -4.78 \| -3.97 | 36% \| 33% | 20% \| 18% |
| lb=8 drive=3.0 stall=4 tol=0.3 away=0.75 body=1.0 | 2.5 | 71% \| 72% | -4.78 \| -3.97 | 36% \| 33% | 20% \| 18% |
| lb=20 drive=1.0 stall=5 tol=0.3 away=0.75 body=0.3 | 1.8 | 72% \| 71% | -4.80 \| -4.28 | 33% \| 32% | 19% \| 17% |
| lb=20 drive=1.5 stall=5 tol=0.3 away=0.75 body=0.3 | 1.8 | 72% \| 71% | -4.80 \| -4.28 | 33% \| 32% | 19% \| 17% |
| lb=20 drive=2.0 stall=5 tol=0.3 away=0.75 body=0.3 | 1.8 | 72% \| 71% | -4.80 \| -4.28 | 33% \| 32% | 19% \| 17% |
| lb=8 drive=3.0 stall=4 tol=0.5 away=0.75 body=0.4 | 3.4 | 70% \| 68% | -4.86 \| -4.69 | 35% \| 27% | 20% \| 16% |
| lb=8 drive=3.0 stall=4 tol=0.3 away=0.75 body=0.5 | 2.4 | 71% \| 71% | -4.89 \| -4.05 | 37% \| 32% | 20% \| 17% |
| lb=20 drive=2.5 stall=5 tol=0.3 away=0.75 body=0.3 | 1.8 | 72% \| 71% | -4.91 \| -4.28 | 33% \| 32% | 19% \| 17% |
| lb=8 drive=2.0 stall=4 tol=0.3 away=0.75 body=0.8 | 5.3 | 71% \| 69% | -4.40 \| -4.93 | 34% \| 32% | 19% \| 18% |
| lb=8 drive=2.0 stall=4 tol=0.3 away=0.75 body=1.0 | 5.3 | 71% \| 69% | -4.40 \| -4.93 | 34% \| 32% | 19% \| 18% |
| lb=8 drive=2.0 stall=4 tol=0.3 away=0.75 body=0.3 | 4.4 | 70% \| 68% | -4.93 \| -4.91 | 34% \| 31% | 19% \| 17% |
| lb=10 drive=2.0 stall=1 tol=0.2 away=0.75 body=0.4 | 32.4 | 69% \| 69% | -4.90 \| -4.94 | 35% \| 36% | 20% \| 21% |
| lb=8 drive=2.0 stall=4 tol=0.5 away=0.75 body=0.5 | 8.0 | 69% \| 69% | -4.99 \| -4.73 | 34% \| 31% | 20% \| 19% |
| lb=8 drive=2.0 stall=4 tol=0.5 away=0.75 body=0.6 | 8.1 | 69% \| 68% | -5.00 \| -4.79 | 34% \| 31% | 20% \| 20% |
| lb=8 drive=2.0 stall=4 tol=0.5 away=0.75 body=0.8 | 8.1 | 69% \| 69% | -5.00 \| -4.72 | 34% \| 31% | 20% \| 20% |
| lb=8 drive=2.0 stall=4 tol=0.5 away=0.75 body=1.0 | 8.1 | 69% \| 69% | -5.00 \| -4.72 | 34% \| 31% | 20% \| 20% |
| lb=10 drive=2.0 stall=1 tol=0.2 away=0.75 body=0.3 | 27.3 | 69% \| 69% | -5.00 \| -4.86 | 35% \| 37% | 20% \| 21% |
| lb=10 drive=2.0 stall=1 tol=0.2 away=0.75 body=0.5 | 34.9 | 69% \| 69% | -5.00 \| -4.93 | 35% \| 36% | 20% \| 21% |
| lb=8 drive=3.0 stall=4 tol=0.3 away=0.75 body=0.4 | 2.4 | 70% \| 71% | -5.01 \| -4.18 | 37% \| 33% | 20% \| 18% |
| lb=10 drive=2.0 stall=4 tol=0.5 away=0.75 body=0.8 | 7.7 | 69% \| 68% | -5.02 \| -4.83 | 35% \| 31% | 20% \| 20% |
| lb=10 drive=2.0 stall=4 tol=0.5 away=0.75 body=1.0 | 7.7 | 69% \| 68% | -5.02 \| -4.83 | 35% \| 31% | 20% \| 20% |
| lb=10 drive=2.0 stall=4 tol=0.5 away=0.75 body=0.6 | 7.7 | 69% \| 68% | -5.02 \| -4.90 | 35% \| 31% | 20% \| 20% |
| lb=10 drive=2.0 stall=4 tol=0.3 away=0.75 body=0.8 | 5.0 | 70% \| 69% | -4.70 \| -5.02 | 35% \| 32% | 19% \| 20% |
| lb=10 drive=2.0 stall=4 tol=0.3 away=0.75 body=1.0 | 5.0 | 70% \| 69% | -4.70 \| -5.02 | 35% \| 32% | 19% \| 20% |
| lb=13 drive=2.0 stall=1 tol=0.2 away=0.75 body=0.4 | 28.8 | 68% \| 69% | -5.03 \| -4.88 | 35% \| 36% | 20% \| 22% |
| lb=10 drive=2.0 stall=1 tol=0.2 away=0.75 body=0.6 | 36.8 | 69% \| 70% | -5.03 \| -4.68 | 35% \| 37% | 21% \| 22% |
| lb=8 drive=2.0 stall=4 tol=0.3 away=0.75 body=0.6 | 5.3 | 71% \| 68% | -4.40 \| -5.04 | 34% \| 32% | 19% \| 18% |
| lb=13 drive=1.0 stall=1 tol=0.2 away=0.75 body=0.4 | 29.1 | 68% \| 69% | -5.06 \| -4.89 | 35% \| 37% | 20% \| 22% |
| lb=13 drive=1.5 stall=1 tol=0.2 away=0.75 body=0.4 | 29.1 | 68% \| 69% | -5.06 \| -4.89 | 35% \| 37% | 20% \| 22% |

## Best 30 settings for catching a real turn (ranked by the worse of train and test turn rate)
| Setting | Dots/day | Win (train \| test) | Avg R % | Turn 1 ATR first | Jump 2 ATR first |
|---|---|---|---|---|---|
| lb=10 drive=4.0 stall=5 tol=0.5 away=1.0 body=0.5 | 2.3 | 65% \| 71% | -7.07 \| -3.85 | 37% \| 38% | 22% \| 29% |
| lb=8 drive=3.5 stall=5 tol=0.5 away=1.0 body=0.5 | 2.8 | 68% \| 69% | -5.81 \| -4.66 | 40% \| 37% | 23% \| 24% |
| lb=10 drive=4.0 stall=5 tol=0.5 away=1.0 body=0.8 | 2.4 | 64% \| 71% | -7.09 \| -3.81 | 37% \| 38% | 22% \| 27% |
| lb=10 drive=4.0 stall=5 tol=0.5 away=1.0 body=1.0 | 2.4 | 64% \| 71% | -7.09 \| -3.81 | 37% \| 38% | 22% \| 27% |
| lb=8 drive=3.5 stall=5 tol=0.5 away=1.0 body=0.8 | 2.9 | 67% \| 70% | -5.89 \| -4.37 | 39% \| 37% | 22% \| 24% |
| lb=8 drive=3.5 stall=5 tol=0.5 away=1.0 body=1.0 | 2.9 | 67% \| 70% | -5.89 \| -4.37 | 39% \| 37% | 22% \| 24% |
| lb=10 drive=4.0 stall=5 tol=0.5 away=1.0 body=0.4 | 1.8 | 65% \| 71% | -7.19 \| -4.03 | 37% \| 38% | 20% \| 28% |
| lb=10 drive=4.0 stall=5 tol=0.5 away=1.0 body=0.6 | 2.3 | 64% \| 71% | -7.11 \| -3.90 | 36% \| 38% | 22% \| 27% |
| lb=8 drive=3.5 stall=5 tol=0.5 away=1.5 body=0.5 | 7.2 | 67% \| 67% | -5.82 \| -5.90 | 37% \| 36% | 22% \| 19% |
| lb=8 drive=3.5 stall=5 tol=0.5 away=1.0 body=0.6 | 2.9 | 67% \| 70% | -5.79 \| -4.44 | 39% \| 36% | 22% \| 24% |
| lb=10 drive=3.5 stall=5 tol=0.5 away=1.0 body=0.8 | 3.9 | 68% \| 67% | -5.45 \| -5.37 | 37% \| 36% | 21% \| 23% |
| lb=10 drive=3.5 stall=5 tol=0.5 away=1.0 body=1.0 | 3.9 | 68% \| 67% | -5.45 \| -5.37 | 37% \| 36% | 21% \| 23% |
| lb=8 drive=3.5 stall=3 tol=0.5 away=1.5 body=0.4 | 9.8 | 67% \| 68% | -5.67 \| -5.38 | 36% \| 36% | 22% \| 20% |
| lb=8 drive=3.5 stall=5 tol=0.5 away=1.5 body=0.4 | 5.4 | 66% \| 66% | -6.13 \| -6.38 | 36% \| 36% | 22% \| 20% |
| lb=10 drive=3.5 stall=5 tol=0.5 away=1.0 body=0.5 | 3.8 | 69% \| 66% | -5.38 \| -5.64 | 38% \| 36% | 22% \| 23% |
| lb=30 drive=4.0 stall=1 tol=0.3 away=0.75 body=1.0 | 19.3 | 67% \| 69% | -5.61 \| -5.20 | 36% \| 36% | 22% \| 21% |
| lb=10 drive=3.5 stall=5 tol=0.5 away=1.0 body=0.6 | 3.9 | 69% \| 67% | -5.38 \| -5.43 | 37% \| 36% | 21% \| 23% |
| lb=30 drive=4.0 stall=1 tol=0.3 away=0.75 body=0.8 | 19.2 | 67% \| 69% | -5.58 \| -5.20 | 36% \| 36% | 22% \| 21% |
| lb=8 drive=3.5 stall=4 tol=0.5 away=1.5 body=0.4 | 7.4 | 66% \| 68% | -6.11 \| -5.51 | 36% \| 37% | 22% \| 21% |
| lb=30 drive=4.0 stall=1 tol=0.05 away=0.75 body=1.0 | 16.5 | 67% \| 70% | -5.72 \| -4.76 | 36% \| 38% | 22% \| 23% |
| lb=30 drive=4.0 stall=1 tol=0.05 away=0.75 body=0.8 | 16.3 | 67% \| 70% | -5.67 \| -4.78 | 36% \| 37% | 22% \| 23% |
| lb=8 drive=3.5 stall=3 tol=0.3 away=1.5 body=0.4 | 8.9 | 67% \| 68% | -5.59 \| -5.22 | 36% \| 36% | 21% \| 21% |
| lb=30 drive=4.0 stall=1 tol=0.3 away=0.75 body=0.5 | 17.7 | 67% \| 68% | -5.51 \| -5.42 | 36% \| 36% | 22% \| 22% |
| lb=30 drive=4.0 stall=1 tol=0.2 away=0.75 body=1.0 | 18.6 | 67% \| 70% | -5.57 \| -4.81 | 36% \| 37% | 22% \| 22% |
| lb=10 drive=4.0 stall=4 tol=0.5 away=1.5 body=0.4 | 5.6 | 64% \| 68% | -6.84 \| -5.47 | 36% \| 36% | 22% \| 21% |
| lb=25 drive=4.0 stall=1 tol=0.05 away=0.75 body=1.0 | 16.9 | 67% \| 69% | -5.79 \| -5.16 | 36% \| 36% | 21% \| 23% |
| lb=30 drive=4.0 stall=1 tol=0.05 away=0.75 body=0.5 | 15.0 | 67% \| 70% | -5.65 \| -4.79 | 36% \| 38% | 21% \| 24% |
| lb=10 drive=4.0 stall=4 tol=0.5 away=1.5 body=0.5 | 7.0 | 64% \| 69% | -6.58 \| -4.98 | 36% \| 36% | 22% \| 21% |
| lb=30 drive=1.0 stall=1 tol=0.05 away=0.75 body=1.0 | 18.1 | 67% \| 70% | -5.64 \| -5.01 | 36% \| 37% | 21% \| 23% |
| lb=30 drive=1.5 stall=1 tol=0.05 away=0.75 body=1.0 | 18.1 | 67% \| 70% | -5.64 \| -5.01 | 36% \| 37% | 21% \| 23% |

## Best 20 for catching a jump (2 ATR first)
| Setting | Dots/day | Win (train \| test) | Avg R % | Turn 1 ATR first | Jump 2 ATR first |
|---|---|---|---|---|---|
| lb=8 drive=3.5 stall=5 tol=0.5 away=1.0 body=0.5 | 2.8 | 68% \| 69% | -5.81 \| -4.66 | 40% \| 37% | 23% \| 24% |
| lb=10 drive=4.0 stall=5 tol=0.5 away=1.0 body=0.8 | 2.4 | 64% \| 71% | -7.09 \| -3.81 | 37% \| 38% | 22% \| 27% |
| lb=10 drive=4.0 stall=5 tol=0.5 away=1.0 body=1.0 | 2.4 | 64% \| 71% | -7.09 \| -3.81 | 37% \| 38% | 22% \| 27% |
| lb=8 drive=3.5 stall=5 tol=0.5 away=1.0 body=0.8 | 2.9 | 67% \| 70% | -5.89 \| -4.37 | 39% \| 37% | 22% \| 24% |
| lb=8 drive=3.5 stall=5 tol=0.5 away=1.0 body=1.0 | 2.9 | 67% \| 70% | -5.89 \| -4.37 | 39% \| 37% | 22% \| 24% |
| lb=8 drive=3.5 stall=5 tol=0.3 away=1.0 body=0.5 | 1.9 | 67% \| 72% | -6.20 \| -4.33 | 37% \| 34% | 22% \| 22% |
| lb=10 drive=4.0 stall=5 tol=0.5 away=1.0 body=0.5 | 2.3 | 65% \| 71% | -7.07 \| -3.85 | 37% \| 38% | 22% \| 29% |
| lb=8 drive=3.5 stall=5 tol=0.3 away=1.0 body=0.6 | 1.9 | 67% \| 71% | -6.10 \| -4.60 | 37% \| 33% | 22% \| 22% |
| lb=10 drive=3.5 stall=5 tol=0.5 away=1.0 body=0.5 | 3.8 | 69% \| 66% | -5.38 \| -5.64 | 38% \| 36% | 22% \| 23% |
| lb=8 drive=3.5 stall=5 tol=0.3 away=1.0 body=0.8 | 1.9 | 67% \| 71% | -6.24 \| -4.49 | 36% \| 34% | 22% \| 22% |
| lb=8 drive=3.5 stall=5 tol=0.3 away=1.0 body=1.0 | 1.9 | 67% \| 71% | -6.24 \| -4.49 | 36% \| 34% | 22% \| 22% |
| lb=8 drive=3.5 stall=5 tol=0.5 away=1.0 body=0.6 | 2.9 | 67% \| 70% | -5.79 \| -4.44 | 39% \| 36% | 22% \| 24% |
| lb=8 drive=4.0 stall=4 tol=0.5 away=1.5 body=0.5 | 5.0 | 66% \| 71% | -6.25 \| -4.35 | 35% \| 37% | 22% \| 22% |
| lb=30 drive=4.0 stall=1 tol=0.2 away=0.75 body=1.0 | 18.6 | 67% \| 70% | -5.57 \| -4.81 | 36% \| 37% | 22% \| 22% |
| lb=10 drive=3.5 stall=5 tol=0.5 away=1.0 body=0.4 | 3.3 | 71% \| 65% | -4.74 \| -6.18 | 39% \| 34% | 22% \| 23% |
| lb=30 drive=4.0 stall=1 tol=0.2 away=0.75 body=0.8 | 18.4 | 67% \| 70% | -5.54 \| -4.84 | 36% \| 37% | 22% \| 22% |
| lb=30 drive=4.0 stall=1 tol=0.05 away=0.75 body=0.8 | 16.3 | 67% \| 70% | -5.67 \| -4.78 | 36% \| 37% | 22% \| 23% |
| lb=30 drive=4.0 stall=1 tol=0.3 away=0.75 body=0.5 | 17.7 | 67% \| 68% | -5.51 \| -5.42 | 36% \| 36% | 22% \| 22% |
| lb=16 drive=3.5 stall=5 tol=0.5 away=0.75 body=0.6 | 2.4 | 67% \| 67% | -5.90 \| -4.68 | 35% \| 37% | 22% \| 24% |
| lb=16 drive=3.5 stall=5 tol=0.5 away=0.75 body=0.8 | 2.4 | 67% \| 67% | -5.90 \| -4.68 | 35% \| 37% | 22% \| 24% |

## Each rule number on its own (average over every other setting; train | test)

| Rule | Value | Dots/day | Avg R % | Turn | Jump |
|---|---|---|---|---|---|
| drive lookback (bars) | 8 | 20.6 | -6.33 \| -6.00 | 33% \| 33% | 19% \| 20% |
| drive lookback (bars) | 10 | 20.3 | -6.20 \| -6.09 | 33% \| 33% | 19% \| 19% |
| drive lookback (bars) | 13 | 19.4 | -6.27 \| -6.21 | 33% \| 32% | 18% \| 19% |
| drive lookback (bars) | 16 (yours) | 18.3 | -6.29 \| -6.15 | 33% \| 33% | 18% \| 19% |
| drive lookback (bars) | 20 | 16.8 | -6.34 \| -6.27 | 32% \| 32% | 18% \| 19% |
| drive lookback (bars) | 25 | 15.1 | -6.41 \| -6.34 | 33% \| 32% | 18% \| 20% |
| drive lookback (bars) | 30 | 13.6 | -6.26 \| -6.15 | 33% \| 33% | 19% \| 20% |
| drive size (ATR) | 1.0 | 21.4 | -6.17 \| -6.26 | 33% \| 32% | 19% \| 20% |
| drive size (ATR) | 1.5 | 21.4 | -6.17 \| -6.27 | 33% \| 32% | 19% \| 20% |
| drive size (ATR) | 2.0 (yours) | 20.9 | -6.12 \| -6.28 | 33% \| 32% | 19% \| 20% |
| drive size (ATR) | 2.5 | 19.4 | -6.26 \| -6.36 | 33% \| 32% | 19% \| 20% |
| drive size (ATR) | 3.0 | 17.0 | -6.28 \| -6.17 | 33% \| 33% | 18% \| 20% |
| drive size (ATR) | 3.5 | 13.6 | -6.43 \| -6.02 | 32% \| 33% | 18% \| 19% |
| drive size (ATR) | 4.0 | 10.4 | -6.67 \| -5.84 | 32% \| 33% | 18% \| 20% |
| stall bars | 1 | 32.6 | -5.89 \| -5.38 | 34% \| 36% | 20% \| 21% |
| stall bars | 2 (yours) | 21.2 | -6.18 \| -6.27 | 32% \| 33% | 19% \| 20% |
| stall bars | 3 | 14.7 | -6.14 \| -6.27 | 34% \| 31% | 18% \| 18% |
| stall bars | 4 | 11.2 | -6.57 \| -6.42 | 32% \| 31% | 18% \| 19% |
| stall bars | 5 | 8.9 | -6.72 \| -6.52 | 31% \| 32% | 17% \| 20% |
| new-extreme tolerance (ATR) | 0.05 | 15.9 | -6.58 \| -6.36 | 32% \| 32% | 18% \| 20% |
| new-extreme tolerance (ATR) | 0.1 | 16.7 | -6.44 \| -6.41 | 32% \| 32% | 18% \| 19% |
| new-extreme tolerance (ATR) | 0.2 (yours) | 17.7 | -6.17 \| -6.19 | 32% \| 33% | 18% \| 20% |
| new-extreme tolerance (ATR) | 0.3 | 18.7 | -6.19 \| -5.97 | 33% \| 33% | 19% \| 19% |
| new-extreme tolerance (ATR) | 0.5 | 19.7 | -6.12 \| -5.93 | 33% \| 33% | 19% \| 20% |
| max bounce before reset (ATR) | 0.75 | 8.6 | -6.17 \| -5.51 | 33% \| 32% | 18% \| 19% |
| max bounce before reset (ATR) | 1.0 | 12.7 | -6.37 \| -5.92 | 33% \| 33% | 19% \| 20% |
| max bounce before reset (ATR) | 1.5 (yours) | 19.6 | -6.25 \| -6.56 | 33% \| 33% | 19% \| 20% |
| max bounce before reset (ATR) | 2.0 | 23.1 | -6.38 \| -6.45 | 32% \| 32% | 18% \| 19% |
| max bounce before reset (ATR) | 2.5 | 24.5 | -6.34 \| -6.42 | 32% \| 33% | 18% \| 20% |
| stall candle size (ATR) | 0.3 | 11.5 | -6.66 \| -6.39 | 32% \| 32% | 18% \| 19% |
| stall candle size (ATR) | 0.4 | 15.6 | -6.35 \| -6.26 | 33% \| 33% | 18% \| 20% |
| stall candle size (ATR) | 0.5 | 18.3 | -6.15 \| -6.12 | 33% \| 33% | 18% \| 20% |
| stall candle size (ATR) | 0.6 (yours) | 19.6 | -6.22 \| -6.05 | 33% \| 33% | 19% \| 20% |
| stall candle size (ATR) | 0.8 | 20.5 | -6.21 \| -6.12 | 33% \| 33% | 19% \| 20% |
| stall candle size (ATR) | 1.0 | 20.8 | -6.22 \| -6.10 | 33% \| 33% | 19% \| 20% |

## Does the best setting change with the day? (picked on TRAIN days of that kind, judged on TEST days of that kind)

| Kind of day | Best setting on train | Train R | Test R | Test turn | Your rules: test R | Your rules: test turn | Test dots |
|---|---|---|---|---|---|---|---|
| low VIX (<=15.9) | lb=10 drive=4.0 stall=3 tol=0.5 away=0.75 body=0.3 | -2.37 | -7.55 | 31% | -7.39 | 32% | 39 |
| mid VIX (15.9-17.3) | lb=20 drive=4.0 stall=5 tol=0.5 away=0.75 body=0.6 | -2.77 | -4.65 | 29% | -4.31 | 32% | 41 |
| high VIX (>17.3) | lb=8 drive=4.0 stall=5 tol=0.5 away=1.0 body=0.5 | -1.82 | -0.29 | 76% | -6.67 | 32% | 17 |
| small gap (<=0.185) | lb=8 drive=4.0 stall=5 tol=0.5 away=1.0 body=0.4 | -2.79 | -5.41 | 39% | -8.12 | 33% | 18 |
| mid gap (0.185-0.462) | lb=8 drive=3.0 stall=5 tol=0.3 away=0.75 body=0.4 | +0.37 | -2.22 | 27% | -5.28 | 30% | 22 |
| big gap (>0.462) | lb=13 drive=3.5 stall=3 tol=0.05 away=1.0 body=0.4 | -2.08 | -4.02 | 39% | -6.05 | 35% | 51 |
| tight first 30 min (<=4.59) | lb=16 drive=2.0 stall=3 tol=0.5 away=0.75 body=0.4 | -4.70 | -6.83 | 32% | -5.78 | 32% | 131 |
| normal first 30 min (4.59-5.64) | lb=10 drive=3.5 stall=4 tol=0.3 away=0.75 body=0.4 | -1.69 | -6.90 | 32% | -7.62 | 32% | 22 |
| wide first 30 min (>5.64) | lb=8 drive=3.5 stall=4 tol=0.5 away=0.75 body=0.4 | -1.58 | -5.12 | 19% | -5.84 | 32% | 27 |
| quiet day before (<=0.674) | lb=8 drive=3.0 stall=3 tol=0.2 away=0.75 body=0.5 | -2.02 | -6.20 | 31% | -6.14 | 33% | 86 |
| normal day before (0.674-0.95) | lb=20 drive=4.0 stall=5 tol=0.5 away=0.75 body=0.6 | -0.49 | -7.77 | 32% | -6.97 | 30% | 28 |
| wide day before (>0.95) | lb=10 drive=3.5 stall=1 tol=0.2 away=0.75 body=0.4 | -2.05 | -3.83 | 37% | -5.18 | 35% | 112 |
| Mon | lb=8 drive=4.0 stall=4 tol=0.2 away=2.5 body=0.3 | -1.99 | -13.74 | 20% | -9.04 | 27% | 20 |
| Tue | lb=8 drive=3.0 stall=3 tol=0.1 away=0.75 body=0.5 | -2.39 | -9.99 | 41% | -8.75 | 32% | 27 |
| Wed | lb=8 drive=3.0 stall=5 tol=0.5 away=1.0 body=0.3 | +1.13 | -2.90 | 29% | -4.24 | 31% | 38 |
| Thu | lb=16 drive=1.0 stall=5 tol=0.5 away=0.75 body=0.3 | -0.89 | +0.52 | 39% | -6.30 | 33% | 18 |
| Fri | lb=16 drive=4.0 stall=5 tol=0.2 away=1.0 body=0.5 | -1.69 | -7.16 | 33% | -3.32 | 37% | 18 |
| 9:30-11 | lb=20 drive=3.5 stall=4 tol=0.1 away=1.0 body=0.5 | +0.34 | -0.59 | 7% | -4.50 | 31% | 15 |
| 11-1 | lb=30 drive=3.5 stall=5 tol=0.5 away=0.75 body=0.4 | +0.55 | -6.76 | 16% | -4.05 | 33% | 25 |
| 1-3 | lb=8 drive=2.5 stall=3 tol=0.05 away=0.75 body=0.3 | +0.25 | -7.31 | 38% | -6.30 | 33% | 34 |
| after 3 | lb=8 drive=3.0 stall=5 tol=0.5 away=1.0 body=0.3 | -5.33 | -6.42 | 45% | -11.19 | 31% | 38 |
| calls | lb=10 drive=4.0 stall=3 tol=0.5 away=0.75 body=0.3 | -3.24 | -4.12 | 35% | -6.58 | 30% | 34 |
| puts | lb=8 drive=3.0 stall=5 tol=0.3 away=0.75 body=0.3 | -1.35 | -3.53 | 30% | -5.89 | 34% | 27 |

## Arrows (the confirm layer): best 25 full settings, all 13 numbers (train | test)

| Setting | Arrows/day | Win | Avg R % | Turn | Jump |
|---|---|---|---|---|---|
| lb=20 drive=4.0 stall=1 tol=0.5 away=0.75 body=0.5 late=1.5 window=15 stretch=80 ext=90 maxbx=3 snap=1 mindr=1.5 | 1.4 | 70% \| 66% | -3.35 \| -5.58 | 40% \| 49% | 22% \| 34% |
| lb=8 drive=3.5 stall=3 tol=0.2 away=0.75 body=0.4 late=4.0 window=15 stretch=60 ext=90 maxbx=20 snap=2 mindr=1.5 | 1.0 | 62% \| 67% | -5.69 \| -4.44 | 40% \| 41% | 22% \| 31% |
| lb=20 drive=4.0 stall=1 tol=0.5 away=0.75 body=1.0 late=1.5 window=20 stretch=70 ext=90 maxbx=3 snap=4 mindr=3.0 | 1.7 | 65% \| 68% | -4.70 \| -4.79 | 37% \| 46% | 20% \| 32% |
| lb=20 drive=3.0 stall=3 tol=0.05 away=1.0 body=0.6 late=4.0 window=20 stretch=80 ext=90 maxbx=12 snap=2 mindr=1.5 | 2.6 | 68% \| 74% | -4.30 \| -1.72 | 37% \| 40% | 22% \| 27% |
| lb=30 drive=1.5 stall=3 tol=0.3 away=1.0 body=0.3 late=2.5 window=15 stretch=80 ext=90 maxbx=12 snap=3 mindr=3.0 | 2.5 | 66% \| 72% | -5.03 \| -2.68 | 36% \| 45% | 23% \| 29% |
| lb=30 drive=1.5 stall=1 tol=0.3 away=0.75 body=1.0 late=4.0 window=20 stretch=80 ext=90 maxbx=3 snap=6 mindr=3.0 | 1.7 | 63% \| 71% | -5.96 \| -2.99 | 36% \| 45% | 22% \| 36% |
| lb=16 drive=3.0 stall=3 tol=0.3 away=2.5 body=0.3 late=2.5 window=20 stretch=90 ext=90 maxbx=3 snap=2 mindr=1.5 | 1.9 | 68% \| 78% | -4.07 \| -0.62 | 36% \| 50% | 21% \| 29% |
| lb=10 drive=3.5 stall=4 tol=0.2 away=1.0 body=0.4 late=1.5 window=20 stretch=80 ext=90 maxbx=8 snap=6 mindr=1.5 | 2.1 | 67% \| 71% | -4.54 \| -3.02 | 36% \| 42% | 21% \| 28% |
| lb=8 drive=3.5 stall=5 tol=0.3 away=1.5 body=0.8 late=1.5 window=5 stretch=90 ext=90 maxbx=3 snap=2 mindr=2.5 | 1.3 | 70% \| 82% | -3.53 \| +0.97 | 36% \| 50% | 19% \| 29% |
| lb=10 drive=4.0 stall=4 tol=0.2 away=2.0 body=1.0 late=2.5 window=5 stretch=90 ext=60 maxbx=3 snap=2 mindr=2.0 | 1.9 | 65% \| 74% | -5.18 \| -2.46 | 36% \| 42% | 23% \| 24% |
| lb=8 drive=3.5 stall=1 tol=0.1 away=0.75 body=0.6 late=3.0 window=5 stretch=80 ext=60 maxbx=5 snap=2 mindr=2.5 | 1.7 | 65% \| 70% | -5.33 \| -2.83 | 36% \| 40% | 22% \| 25% |
| lb=8 drive=1.5 stall=2 tol=0.5 away=1.0 body=0.8 late=3.0 window=15 stretch=70 ext=90 maxbx=3 snap=4 mindr=1.0 | 2.0 | 67% \| 76% | -4.39 \| -1.45 | 36% \| 51% | 22% \| 34% |
| lb=25 drive=4.0 stall=2 tol=0.1 away=0.75 body=0.6 late=2.5 window=20 stretch=80 ext=90 maxbx=12 snap=2 mindr=1.5 | 2.0 | 69% \| 74% | -3.80 \| -1.96 | 36% \| 45% | 21% \| 34% |
| lb=10 drive=4.0 stall=4 tol=0.1 away=1.0 body=0.8 late=1.5 window=10 stretch=60 ext=60 maxbx=20 snap=4 mindr=3.0 | 2.2 | 65% \| 75% | -4.99 \| -2.05 | 36% \| 40% | 24% \| 24% |
| lb=10 drive=4.0 stall=4 tol=0.05 away=0.75 body=0.6 late=1.5 window=10 stretch=40 ext=90 maxbx=5 snap=1 mindr=1.0 | 0.8 | 63% \| 75% | -5.26 \| -0.91 | 36% \| 50% | 16% \| 36% |
| lb=8 drive=3.5 stall=5 tol=0.1 away=1.0 body=0.4 late=3.0 window=5 stretch=70 ext=60 maxbx=8 snap=6 mindr=1.5 | 2.3 | 66% \| 75% | -4.96 \| -2.03 | 36% \| 38% | 24% \| 23% |
| lb=8 drive=3.5 stall=1 tol=0.05 away=0.75 body=0.4 late=3.0 window=5 stretch=50 ext=60 maxbx=12 snap=6 mindr=1.0 | 2.0 | 66% \| 76% | -4.64 \| -1.31 | 36% \| 45% | 23% \| 30% |
| lb=8 drive=3.5 stall=2 tol=0.2 away=2.5 body=0.3 late=2.5 window=5 stretch=80 ext=60 maxbx=3 snap=2 mindr=3.0 | 2.9 | 68% \| 74% | -4.31 \| -2.36 | 36% \| 44% | 22% \| 24% |
| lb=25 drive=4.0 stall=5 tol=0.2 away=1.0 body=0.4 late=4.0 window=3 stretch=80 ext=90 maxbx=20 snap=3 mindr=1.5 | 2.4 | 67% \| 74% | -4.50 \| -1.91 | 35% \| 44% | 23% \| 31% |
| lb=8 drive=3.5 stall=2 tol=0.1 away=0.75 body=1.0 late=2.5 window=15 stretch=40 ext=45 maxbx=3 snap=6 mindr=2.5 | 1.6 | 64% \| 78% | -5.32 \| -0.98 | 35% \| 46% | 25% \| 32% |
| lb=25 drive=3.5 stall=5 tol=0.3 away=1.0 body=0.3 late=2.0 window=15 stretch=80 ext=60 maxbx=20 snap=2 mindr=1.5 | 2.0 | 69% \| 78% | -4.29 \| -1.08 | 35% \| 42% | 25% \| 27% |
| lb=10 drive=4.0 stall=5 tol=0.05 away=0.75 body=0.3 late=3.0 window=20 stretch=90 ext=90 maxbx=8 snap=4 mindr=2.0 | 1.0 | 66% \| 77% | -4.35 \| -0.47 | 35% \| 51% | 21% \| 40% |
| lb=13 drive=4.0 stall=3 tol=0.05 away=2.5 body=0.8 late=1.5 window=20 stretch=90 ext=60 maxbx=3 snap=2 mindr=2.0 | 2.8 | 68% \| 72% | -4.32 \| -3.21 | 35% \| 43% | 21% \| 27% |
| lb=8 drive=3.5 stall=3 tol=0.1 away=0.75 body=0.3 late=3.0 window=15 stretch=60 ext=45 maxbx=12 snap=3 mindr=3.0 | 1.6 | 64% \| 76% | -5.43 \| -1.38 | 35% \| 44% | 24% \| 29% |
| lb=30 drive=1.0 stall=3 tol=0.2 away=0.75 body=0.4 late=1.5 window=5 stretch=80 ext=90 maxbx=20 snap=6 mindr=2.5 | 1.9 | 66% \| 73% | -5.10 \| -2.30 | 35% \| 42% | 20% \| 33% |

Your current arrows: 9.3/day, R -5.34 | -4.06, turn 29% | 35%.
