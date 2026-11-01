# DIV PRO lock-green study - 2026, real 0DTE options $0.45-1.00

QQQ, SPY | charts 1m, 3m, 5m | Jan 1 2026 to 2026-10-31. Each DIV PRO fire (9:45-2:30 ET, options trade 9:30-4) buys the same-day call (long) or put (short) priced closest to $0.70 inside $0.45-1.00, at the last 1-minute close before the fire candle opens + 1c. Sold at 1-minute closes - 1c. Watched 30 minutes. Random row = 2 random times per fire, same day and side, same contract rule. Real Alpaca option prices. DATA ONLY.

## A) How far the option runs in 30 minutes

| Group | Trades | Avg entry $ | Avg best % | Median best % | Avg worst % | Median worst % | Median minutes to best | Avg % if just held 30 min |
|---|---|---|---|---|---|---|---|---|
| **DIV fires** | 1532 | 0.70 | **39%** | 19% | -36% | -36% | 10 | -4% |
| Random entries | 3051 | 0.70 | **35%** | 17% | -38% | -38% | 10 | -9% |
| QQQ 1m | 116 | 0.69 | **37%** | 18% | -38% | -38% | 10 | -9% |
| QQQ 3m | 361 | 0.70 | **44%** | 21% | -37% | -37% | 10 | -1% |
| QQQ 5m | 261 | 0.70 | **38%** | 18% | -39% | -40% | 9 | -8% |
| SPY 1m | 156 | 0.69 | **41%** | 19% | -33% | -31% | 10 | +0% |
| SPY 3m | 379 | 0.70 | **38%** | 18% | -34% | -35% | 10 | -3% |
| SPY 5m | 259 | 0.70 | **36%** | 18% | -35% | -37% | 10 | -5% |
| PUTS (short fires) | 830 | 0.70 | **40%** | 18% | -36% | -37% | 9 | -5% |
| CALLS (long fires) | 702 | 0.70 | **39%** | 20% | -36% | -35% | 10 | -2% |

## B) How often each lock-green level gets hit (within 30 min)

Hit = the option's 1-minute close reached that gain at least once. 'Before -30%' = it got there before ever closing 30% down.

| Lock level | DIV hit % | Hit before -20% | Hit before -30% | Median minutes to hit | Random hit % |
|---|---|---|---|---|---|
| +10% | **63%** | 48% | 57% | 4 | 61% |
| +15% | **55%** | 41% | 49% | 6 | 53% |
| +20% | **48%** | 35% | 42% | 8 | 46% |
| +25% | **41%** | 30% | 36% | 9 | 40% |
| +30% | **37%** | 28% | 33% | 9 | 36% |
| +40% | **31%** | 23% | 27% | 11 | 29% |
| +50% | **26%** | 19% | 23% | 12 | 22% |
| +75% | **17%** | 13% | 15% | 15 | 14% |
| +100% | **11%** | 8% | 9% | 17 | 9% |

## C) What each plan pays per trade (avg % on the premium, after the 1c fills)

Sell ALL at the lock level, stop at the % shown, otherwise sell at the 30-minute close. Best cell = the lock to use.

| Lock (sell all at) | stop -20% | stop -30% | stop -50% | no stop | Random, stop -30% |
|---|---|---|---|---|---|
| +10% | -5.4% | -6.6% | -8.1% | -8.9% | -7.1% |
| +15% | -5.1% | -6.6% | -8.3% | -9.2% | -7.1% |
| +20% | -5.3% | -7.2% | -9.1% | -10.1% | -7.3% |
| +25% | -5.3% | -7.4% | -9.4% | -10.4% | -7.5% |
| +30% | -4.8% | -7.1% | -9.2% | -10.2% | -7.5% |
| +40% | -4.2% | -6.5% | -8.7% | -9.7% | -7.3% |
| +50% | -3.8% | -6.0% | -8.0% | -9.0% | -7.4% |
| +75% | -2.5% | -4.7% | -6.5% | -7.4% | -6.8% |
| +100% | -2.5% | -4.6% | -6.2% | -7.2% | -6.6% |

**Best plan: sell at +100%, stop -20% -> -2.5% per trade on average.**

## D) Best plan by chart and by hour (sell at the best lock above)

| Group | Trades | Hit the lock % | Stopped % | Avg % per trade |
|---|---|---|---|---|
| QQQ 1m | 116 | 7% | 77% | **-4.6%** |
| QQQ 3m | 361 | 10% | 75% | **-0.8%** |
| QQQ 5m | 261 | 7% | 76% | **-5.5%** |
| SPY 1m | 156 | 7% | 69% | **-0.8%** |
| SPY 3m | 379 | 8% | 72% | **-0.8%** |
| SPY 5m | 259 | 6% | 75% | **-4.3%** |
| PUTS | 830 | 9% | 74% | **-1.9%** |
| CALLS | 702 | 6% | 74% | **-3.1%** |
| 9:00 | 211 | 9% | 77% | **-2.4%** |
| 10:00 | 392 | 8% | 76% | **-2.3%** |
| 11:00 | 302 | 7% | 76% | **-3.7%** |
| 12:00 | 287 | 8% | 69% | **-0.4%** |
| 13:00 | 227 | 6% | 71% | **-4.1%** |
| 14:00 | 113 | 11% | 73% | **-1.6%** |
| G2 | 766 | 8% | 73% | **-2.0%** |
| G3 | 618 | 8% | 73% | **-2.2%** |
| G4 | 148 | 6% | 82% | **-5.8%** |

Runtime 3.7 min. This is math/data, not financial advice.