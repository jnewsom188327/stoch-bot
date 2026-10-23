# EDGE FINDER - SCORECARD x DIAMONDS x REAL OPTION PRICES - SPY, QQQ - 2024-02-15 to now - 2026-10-23 11:26 ET
Runtime 40 min. 449,666 entries on 675 trading days. Option prices = Alpaca OPRA 1-minute bars: 85,749 of 86,062 contract-days found. DATA ONLY.
**Each trade** buys the option at the close of the signal minute (+ cost) and sells at the exit minute's close (- cost). **Cost** = $0.01 or 0.5% of the price per side, whichever is bigger. Entries 9:35-14:45, out by 15:55, max 90 min. **Return** = % on the premium paid. **Fires/day** = trades per trading day, SPY + QQQ together.
**Prices = STRICT:** buy at the first REAL option trade after the signal (within 3 minutes - otherwise no trade), sell at the first real trade after the exit. Nothing carried forward. (The first run used the last price carried forward up to 5 minutes = LOOSE.)
**Halves** = the older and newer half of the days. **BLIND** = picked or learned on one half, judged on the half it never saw.

## 0. PRICE CHECK - LOOSE (last price carried forward) vs STRICT (real trades only)
Entries that got a real option trade within 3 minutes: **94%** (6,320,603 of 6,721,543 entry x contract tries).
Median average return per trade over every exit and chart (SPY+QQQ per chart). If STRICT falls apart where LOOSE looked great, the first run's edge was stale prices.
| Option | Signals LOOSE | Signals STRICT | Random LOOSE | Random STRICT | Signal setups passing (STRICT) |
|---|---|---|---|---|---|
| 3 ITM 0DTE | -0.5% | **-1.2%** | -0.9% | **-1.1%** | 1% |
| 3 ITM 1DTE | -0.2% | **-1.1%** | -0.7% | **-1.1%** | 1% |
| 3 ITM 2DTE | +0.2% | **-1.1%** | -0.4% | **-1.0%** | 1% |
| 2 ITM 0DTE | -0.8% | **-1.2%** | -1.1% | **-1.2%** | 1% |
| 2 ITM 1DTE | -0.6% | **-1.1%** | -0.9% | **-1.1%** | 1% |
| 2 ITM 2DTE | -0.0% | **-1.1%** | -0.6% | **-1.0%** | 1% |
| 1 ITM 0DTE | -1.3% | **-1.4%** | -1.5% | **-1.5%** | 0% |
| 1 ITM 1DTE | -0.9% | **-1.1%** | -1.1% | **-1.1%** | 1% |
| 1 ITM 2DTE | -0.4% | **-1.2%** | -0.9% | **-1.1%** | 1% |
| ATM 0DTE | -2.1% | **-2.2%** | -2.5% | **-2.4%** | 0% |
| ATM 1DTE | -1.1% | **-1.2%** | -1.2% | **-1.2%** | 0% |
| ATM 2DTE | -0.7% | **-1.2%** | -1.0% | **-1.1%** | 1% |
| 1 OTM 0DTE | -3.8% | **-3.9%** | -4.6% | **-4.6%** | 0% |
| 1 OTM 1DTE | -1.2% | **-1.4%** | -1.4% | **-1.4%** | 0% |
| 1 OTM 2DTE | -0.5% | **-1.2%** | -0.9% | **-1.2%** | 1% |

**By exit, 3 ITM 2DTE (the first run's winner):**
| Exit | Signals LOOSE | Signals STRICT | Random LOOSE | Random STRICT |
|---|---|---|---|---|
| LINE BREAK | +1.8% | **-1.1%** | +0.5% | **-1.0%** |
| LINE OR STRUCTURE | +1.9% | **-1.0%** | +0.6% | **-1.0%** |
| TRAIL STRUCTURE | +1.8% | **-1.2%** | +0.7% | **-1.1%** |
| LINE COLOR | +0.3% | **-0.6%** | -0.5% | **-0.5%** |
| ANGLE BACK -20 | -2.6% | **-1.2%** | -2.5% | **-0.9%** |
| 5 MINUTES | +0.2% | **-1.1%** | -0.7% | **-1.1%** |
| 15 MINUTES | +0.1% | **-1.1%** | -0.8% | **-1.0%** |
| 30 MINUTES | -0.2% | **-1.2%** | -1.1% | **-1.0%** |
| OPTION +5% / -10% | +0.4% | **-1.1%** | -0.6% | **-1.1%** |
| OPTION +10% / -10% | +0.4% | **-1.3%** | -0.7% | **-1.1%** |
| OPTION +20% / -10% | +0.1% | **-1.2%** | -0.9% | **-1.0%** |
| OPTION +10% / -20% | +0.6% | **-1.3%** | -0.3% | **-1.1%** |
| OPTION TRAIL 15% | -1.7% | **-1.1%** | -2.5% | **-1.0%** |
| PLAN Q (3 LOTS) | -0.4% | **-1.1%** | -1.4% | **-1.1%** |
| LINE BREAK OR +20% | +2.1% | **-1.1%** | +1.1% | **-0.9%** |

**Signals:**
- **DIAMOND (YOURS)** - AGREE DOTS diamond, your settings (TTM 20/14/5/1, Vix 22/50/10/50, within 2)
- **DIAMOND (TUNED)** - AGREE DOTS diamond, 1m-tuned settings (TTM 30/14/3/1, Vix 30/50/5/70, same candle)
- **TREND LINE CROSS** - a candle closes through the trend line (EMA 13) to the other side - every one
- **LINE TURNS YOUR COLOR** - the trend line turns green / blue (long) or red / pink (short)
- **ANGLE UP THROUGH 23** - trend-line angle crosses up through 23 deg (long) / down through -23 (short) - scorecard 37
- **ANGLE FLATTENS THROUGH 23** - a steep line flattens back through 23 deg (long) / -23 (short) - scorecard 50
- **FEAR / GREED MAXED** - Vix Fix fear hits 95+ (long) / greed hits 95+ (short) - scorecard 52
- **GAP & GO** - 0.3+ daily-ATR gap, first candle from 9:35 that holds the gap side of yesterday's close and VWAP - scorecard 56
- **PAUSE THEN GO** - a steep line (20+ deg) stalls under 5 deg, then the angle turns back up through 10 (long) / mirror - scorecard 47
- **RANDOM** - random candles, random side - the bar to beat

**Exits:**
- **LINE BREAK** - ride until a candle closes back through the trend line
- **LINE OR STRUCTURE** - line break, or $0.05 past the last 10 candles' low / high (1-minute check), whichever first
- **TRAIL STRUCTURE** - structure stop that trails to the last 3 candles' low / high after every closed candle
- **LINE COLOR** - ride until the line turns the other color
- **ANGLE BACK -20** - ride until the trend-line angle crosses -20 deg against you (the angle study's best exit)
- **5 MINUTES** - out after 5 minutes
- **15 MINUTES** - out after 15 minutes
- **30 MINUTES** - out after 30 minutes
- **OPTION +5% / -10%** - the option: out at +5% or -10%
- **OPTION +10% / -10%** - the option: out at +10% or -10%
- **OPTION +20% / -10%** - the option: out at +20% or -10%
- **OPTION +10% / -20%** - the option: out at +10% or -20%
- **OPTION TRAIL 15%** - the option: out 15% off its best, or -10%
- **PLAN Q (3 LOTS)** - your Diamond-bot plan Q: 1 lot at +5%, 1 at +10%, runner trails 15% (30 min max), -10% stop on all
- **LINE BREAK OR +20%** - line break, or the option +20%, whichever first

## 1. HOW OFTEN EACH SIGNAL FIRES (per trading day, SPY + QQQ together, entries with option prices)
| Signal | Entry | 1m | 2m | 3m | 5m | all charts |
|---|---|---|---|---|---|---|
| DIAMOND (YOURS) | AT THE SIGNAL | 15.4 | 7.3 | 4.7 | 3.0 | 30.4 |
| DIAMOND (YOURS) | WAIT FOR THE LINE CROSS | 13.6 | 6.4 | 4.0 | 2.6 | 26.6 |
| DIAMOND (TUNED) | AT THE SIGNAL | 4.6 | 2.2 | 1.4 | 0.9 | 9.2 |
| DIAMOND (TUNED) | WAIT FOR THE LINE CROSS | 4.1 | 2.0 | 1.2 | 0.8 | 8.1 |
| TREND LINE CROSS | AT THE SIGNAL | 104.4 | 51.6 | 33.7 | 20.6 | 210.3 |
| LINE TURNS YOUR COLOR | AT THE SIGNAL | 20.5 | 12.6 | 9.9 | 7.5 | 50.4 |
| ANGLE UP THROUGH 23 | AT THE SIGNAL | 1.3 | 0.7 | 0.5 | 0.4 | 2.9 |
| ANGLE FLATTENS THROUGH 23 | AT THE SIGNAL | 1.4 | 0.7 | 0.5 | 0.4 | 3.0 |
| FEAR / GREED MAXED | AT THE SIGNAL | 36.8 | 18.3 | 12.1 | 8.6 | 75.9 |
| FEAR / GREED MAXED | WAIT FOR THE LINE CROSS | 24.8 | 11.9 | 7.7 | 5.4 | 49.9 |
| GAP & GO | AT THE SIGNAL | 0.5 | 0.5 | 0.5 | 0.5 | 2.1 |
| PAUSE THEN GO | AT THE SIGNAL | 0.6 | 0.3 | 0.2 | 0.2 | 1.2 |
| RANDOM | AT THE SIGNAL | 52.5 | 26.0 | 17.1 | 10.2 | 105.9 |
| RANDOM | WAIT FOR THE LINE CROSS | 45.3 | 22.3 | 14.4 | 8.5 | 90.4 |

## 2. EVERY SIGNAL'S BEST OPTION TRADE (whole sample, t 2.5+, positive in both halves) - 111 of 35,100 pass (RANDOM: 0 of 5,850)
Best per signal and chart, sorted by average return. Edge vs random = this signal minus random entries on the exact same trade.
| Signal | Entry | Chart | Exit | Option | Fires/day | Win % | Avg | Avg win / loss | t | 1st / 2nd half | Random same trade | Edge vs random |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ANGLE FLATTENS THROUGH 23 | AT THE SIGNAL | SPY+QQQ 3m | ANGLE BACK -20 | 2 ITM 0DTE | 0.50 | 51% | **+15.6%** | +67% / -38% | 2.6 | +15.6% / +15.6% | -1.2% | +16.8% |
| PAUSE THEN GO | AT THE SIGNAL | SPY+QQQ 5m | OPTION +20% / -10% | 2 ITM 1DTE | 0.15 | 54% | **+4.8%** | +20% / -13% | 2.6 | +5.5% / +4.3% | -1.4% | +6.2% |

### Most fires with quality (whole sample): best average at each fire rate, t 2.5+, both halves positive, beats random
| Signal | Entry | Chart | Exit | Option | Fires/day | Win % | Avg | Avg win / loss | t | 1st / 2nd half | Random same trade | Edge vs random |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **0.25-0.5 fires/day** | | | | | | | | | | | | |
| ANGLE FLATTENS THROUGH 23 | AT THE SIGNAL | SPY+QQQ 3m | LINE COLOR | 3 ITM 2DTE | 0.43 | 55% | **+9.6%** | +33% / -18% | 3.0 | +9.2% / +10.0% | -0.5% | +10.0% |
| **0.5-1 fires/day** | | | | | | | | | | | | |
| ANGLE FLATTENS THROUGH 23 | AT THE SIGNAL | SPY+QQQ 3m | ANGLE BACK -20 | 2 ITM 0DTE | 0.50 | 51% | **+15.6%** | +67% / -38% | 2.6 | +15.6% / +15.6% | -1.2% | +16.8% |

## 3. WHICH OPTION? (every signal x chart x exit, SPY + QQQ per chart)
Median average return, and the share of setups that pass (t 2.5+, both halves positive).
| Option | 0DTE | 1DTE | 2DTE |
|---|---|---|---|
| 3 ITM | -1.2% (1% pass) | -1.1% (1% pass) | -1.1% (1% pass) |
| 2 ITM | -1.2% (1% pass) | -1.1% (1% pass) | -1.1% (1% pass) |
| 1 ITM | -1.4% (0% pass) | -1.1% (1% pass) | -1.2% (1% pass) |
| ATM | -2.2% (0% pass) | -1.2% (0% pass) | -1.2% (1% pass) |
| 1 OTM | -3.9% (0% pass) | -1.4% (0% pass) | -1.2% (1% pass) |

## 4. WHICH EXIT? (every signal x chart x option)
| Exit | Median avg | Pass % | Best signal with it (avg, fires/day) |
|---|---|---|---|
| LINE BREAK | -1.1% | 0% | - |
| LINE OR STRUCTURE | -1.1% | 0% | - |
| TRAIL STRUCTURE | -1.3% | 0% | - |
| LINE COLOR | -0.7% | 1% | ANGLE FLATTENS THROUGH 23 SPY+QQQ 3m 2 ITM 0DTE (+15.4%, 0.5/day) |
| ANGLE BACK -20 | -1.3% | 2% | ANGLE FLATTENS THROUGH 23 SPY+QQQ 3m 2 ITM 0DTE (+15.6%, 0.5/day) |
| 5 MINUTES | -1.2% | 0% | - |
| 15 MINUTES | -1.2% | 2% | ANGLE FLATTENS THROUGH 23 SPY+QQQ 3m ATM 0DTE (+8.2%, 0.5/day) |
| 30 MINUTES | -1.3% | 2% | ANGLE FLATTENS THROUGH 23 SPY+QQQ 3m 2 ITM 0DTE (+8.8%, 0.5/day) |
| OPTION +5% / -10% | -1.2% | 0% | - |
| OPTION +10% / -10% | -1.3% | 0% | - |
| OPTION +20% / -10% | -1.4% | 0% | PAUSE THEN GO SPY+QQQ 5m 2 ITM 1DTE (+4.8%, 0.1/day) |
| OPTION +10% / -20% | -1.3% | 0% | - |
| OPTION TRAIL 15% | -1.3% | 0% | - |
| PLAN Q (3 LOTS) | -1.3% | 0% | - |
| LINE BREAK OR +20% | -1.2% | 0% | - |

## 5. BLIND CONFLUENCE - the trade AND the readings that help learned on one half, judged on the half it never saw
For every signal and chart: the best trade is picked on one half (by t). On that same half, every reading that lifts the average (t 2+) counts +1 and every one that drags it counts -1. **Score k+** = trades with k or more helping readings (net). Everything below is the OTHER half. ✅ in the frontier = avg +3%+ and t 2.5+ on unseen days.

### The frontier: most fires per day that still held up on unseen days
Unseen half only, t 2+, positive, and better than random entries with the same trade and filter. Best 4 per fire rate.
| Learned on | Signal | Entry | Chart | Trade (picked blind) | Filter | Fires/day | Win % | Avg | Avg win / loss | t | Kelly | Random + same filter |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **0.25-0.5 fires/day** | | | | | | | | | | | | |
| **0.5-1 fires/day** | | | | | | | | | | | | |
| **1-2 fires/day** | | | | | | | | | | | | |
| 1st half | FEAR / GREED MAXED | AT THE SIGNAL | SPY+QQQ 3m | LINE COLOR / 2 ITM 0DTE | none | 1.92 | 43% | **+7.7%**  | +61% / -33% | 2.1 | 24% | +0.5% (1792) |
| **2-4 fires/day** | | | | | | | | | | | | |
| **4-8 fires/day** | | | | | | | | | | | | |
| **8-15 fires/day** | | | | | | | | | | | | |
| **15+ fires/day** | | | | | | | | | | | | |

### Held up BOTH ways (learned on either half, positive with t 2+ on the other) - 0 setups
| Signal | Entry | Chart | Filter | Fires/day (avg of both) | Worst half avg | Worst t |
|---|---|---|---|---|---|---|

### What the filters learned (the readings that helped / hurt, for the setups above)

### Every signal, no filter vs best filter (unseen half)
| Learned on | Signal | Entry | Chart | Trade (picked blind) | Filter | Fires/day | Win % | Avg | Avg win / loss | t | Kelly | Random + same filter |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1st half | DIAMOND (YOURS) | AT THE SIGNAL | SPY+QQQ 1m | LINE COLOR / 2 ITM 0DTE | none | 15.07 | 37% | **-1.4%**  | +19% / -13% | -2.4 | 0% | -1.0% (11213) |
| 2nd half | DIAMOND (YOURS) | AT THE SIGNAL | SPY+QQQ 1m | ANGLE BACK -20 / 2 ITM 0DTE | none | 15.30 | 42% | **-2.5%**  | +44% / -36% | -3.0 | 0% | -2.2% (17439) |
| 2nd half | DIAMOND (YOURS) | AT THE SIGNAL | SPY+QQQ 1m | ANGLE BACK -20 / 2 ITM 0DTE | score 2+ | 0.09 | 47% | **+0.9%**  | +39% / -32% | 0.1 | 5% | -3.5% (2439) |
| 1st half | DIAMOND (YOURS) | AT THE SIGNAL | SPY+QQQ 2m | LINE COLOR / 2 ITM 0DTE | none | 1.14 | 35% | **-0.9%**  | +49% / -28% | -0.3 | 0% | +0.2% (2003) |
| 2nd half | DIAMOND (YOURS) | AT THE SIGNAL | SPY+QQQ 2m | OPTION TRAIL 15% / 2 ITM 0DTE | none | 2.90 | 28% | **-2.0%**  | +24% / -12% | -2.4 | 0% | -1.0% (2763) |
| 1st half | DIAMOND (YOURS) | AT THE SIGNAL | SPY+QQQ 3m | LINE COLOR / 2 ITM 0DTE | none | 3.73 | 36% | **-2.4%**  | +20% / -16% | -2.6 | 0% | -0.2% (4902) |
| 2nd half | DIAMOND (YOURS) | AT THE SIGNAL | SPY+QQQ 3m | 15 MINUTES / 1 ITM 0DTE | none | 4.71 | 41% | **-3.5%**  | +20% / -20% | -4.1 | 0% | -2.1% (4821) |
| 2nd half | DIAMOND (YOURS) | AT THE SIGNAL | SPY+QQQ 3m | 15 MINUTES / 1 ITM 0DTE | score 2+ | 0.29 | 47% | **-1.9%**  | +22% / -23% | -0.6 | 0% | -0.6% (307) |
| 1st half | DIAMOND (YOURS) | AT THE SIGNAL | SPY+QQQ 5m | TRAIL STRUCTURE / 1 ITM 0DTE | none | 1.14 | 31% | **-1.3%**  | +50% / -24% | -0.5 | 0% | -1.5% (1264) |
| 2nd half | DIAMOND (YOURS) | AT THE SIGNAL | SPY+QQQ 5m | LINE COLOR / 2 ITM 0DTE | none | 1.01 | 40% | **+0.9%**  | +25% / -15% | 0.5 | 11% | +0.2% (492) |
| 1st half | DIAMOND (YOURS) | WAIT FOR THE LINE CROSS | SPY+QQQ 1m | LINE COLOR / 1 ITM 0DTE | none | 12.67 | 36% | **-2.0%**  | +25% / -17% | -2.5 | 0% | -1.7% (11552) |
| 2nd half | DIAMOND (YOURS) | WAIT FOR THE LINE CROSS | SPY+QQQ 1m | ANGLE BACK -20 / 3 ITM 0DTE | none | 9.49 | 43% | **-3.0%**  | +36% / -32% | -3.4 | 0% | -1.5% (7482) |
| 2nd half | DIAMOND (YOURS) | WAIT FOR THE LINE CROSS | SPY+QQQ 1m | ANGLE BACK -20 / 3 ITM 0DTE | score 1+ | 2.01 | 43% | **-3.6%**  | +35% / -33% | -1.6 | 0% | -1.1% (2200) |
| 1st half | DIAMOND (YOURS) | WAIT FOR THE LINE CROSS | SPY+QQQ 2m | ANGLE BACK -20 / 3 ITM 0DTE | none | 6.16 | 44% | **-2.2%**  | +38% / -34% | -1.6 | 0% | -1.5% (7470) |
| 2nd half | DIAMOND (YOURS) | WAIT FOR THE LINE CROSS | SPY+QQQ 2m | 30 MINUTES / 1 ITM 0DTE | none | 5.43 | 44% | **-2.3%**  | +31% / -28% | -2.2 | 0% | -1.6% (6544) |
| 1st half | DIAMOND (YOURS) | WAIT FOR THE LINE CROSS | SPY+QQQ 2m | ANGLE BACK -20 / 3 ITM 0DTE | score 1+ | 2.35 | 45% | **-2.1%**  | +36% / -33% | -1.1 | 0% | -0.4% (4016) |
| 1st half | DIAMOND (YOURS) | WAIT FOR THE LINE CROSS | SPY+QQQ 3m | LINE OR STRUCTURE / 1 ITM 0DTE | none | 1.53 | 24% | **-4.0%**  | +31% / -15% | -2.7 | 0% | -2.1% (2120) |
| 2nd half | DIAMOND (YOURS) | WAIT FOR THE LINE CROSS | SPY+QQQ 3m | 15 MINUTES / 2 ITM 0DTE | none | 1.98 | 45% | **-1.5%**  | +16% / -16% | -1.5 | 0% | -1.9% (2322) |
| 2nd half | DIAMOND (YOURS) | WAIT FOR THE LINE CROSS | SPY+QQQ 3m | 15 MINUTES / 2 ITM 0DTE | score 1+ | 0.53 | 46% | **-1.9%**  | +15% / -17% | -1.1 | 0% | -1.0% (697) |
| 1st half | DIAMOND (YOURS) | WAIT FOR THE LINE CROSS | SPY+QQQ 5m | OPTION +10% / -20% / 2 ITM 0DTE | none | 1.42 | 58% | **-1.7%**  | +14% / -23% | -1.7 | 0% | -1.4% (1626) |
| 2nd half | DIAMOND (YOURS) | WAIT FOR THE LINE CROSS | SPY+QQQ 5m | LINE COLOR / 3 ITM 0DTE | none | 0.81 | 41% | **+0.4%**  | +26% / -17% | 0.2 | 5% | +2.9% (643) |
| 1st half | DIAMOND (YOURS) | WAIT FOR THE LINE CROSS | SPY+QQQ 5m | OPTION +10% / -20% / 2 ITM 0DTE | score 1+ | 0.08 | 81% | **+7.2%**  | +15% / -24% | 2.0 | 100% | -2.8% (109) |
| 1st half | DIAMOND (TUNED) | AT THE SIGNAL | SPY+QQQ 1m | LINE COLOR / 2 ITM 0DTE | none | 1.98 | 32% | **-1.8%**  | +40% / -21% | -0.9 | 0% | -0.7% (10069) |
| 2nd half | DIAMOND (TUNED) | AT THE SIGNAL | SPY+QQQ 1m | OPTION TRAIL 15% / 2 ITM 0DTE | none | 1.63 | 28% | **-1.8%**  | +28% / -13% | -1.2 | 0% | -1.8% (3736) |
| 1st half | DIAMOND (TUNED) | AT THE SIGNAL | SPY+QQQ 2m | 30 MINUTES / 1 ITM 0DTE | none | 1.31 | 38% | **-6.4%**  | +31% / -30% | -2.9 | 0% | -0.7% (2336) |
| 2nd half | DIAMOND (TUNED) | AT THE SIGNAL | SPY+QQQ 2m | ANGLE BACK -20 / 1 ITM 0DTE | none | 1.43 | 37% | **-7.3%**  | +50% / -41% | -2.4 | 0% | -2.3% (5893) |
| 1st half | DIAMOND (TUNED) | AT THE SIGNAL | SPY+QQQ 2m | 30 MINUTES / 1 ITM 0DTE | score 1+ | 0.44 | 36% | **-11.4%**  | +29% / -34% | -3.5 | 0% | -1.3% (791) |
| 1st half | DIAMOND (TUNED) | AT THE SIGNAL | SPY+QQQ 3m | OPTION TRAIL 15% / 2 ITM 2DTE | none | 0.70 | 34% | **-0.5%**  | +19% / -10% | -0.4 | 0% | -0.8% (2786) |
| 2nd half | DIAMOND (TUNED) | AT THE SIGNAL | SPY+QQQ 3m | OPTION +20% / -10% / 3 ITM 2DTE | none | 0.75 | 37% | **-1.4%**  | +17% / -12% | -1.2 | 0% | -1.1% (3429) |
| 1st half | DIAMOND (TUNED) | AT THE SIGNAL | SPY+QQQ 5m | 30 MINUTES / 3 ITM 2DTE | none | 0.46 | 37% | **-3.7%**  | +11% / -12% | -2.5 | 0% | -1.0% (1979) |
| 2nd half | DIAMOND (TUNED) | AT THE SIGNAL | SPY+QQQ 5m | ANGLE BACK -20 / 3 ITM 0DTE | none | 0.73 | 47% | **-0.4%**  | +40% / -36% | -0.1 | 0% | +1.0% (2828) |
| 2nd half | DIAMOND (TUNED) | AT THE SIGNAL | SPY+QQQ 5m | ANGLE BACK -20 / 3 ITM 0DTE | score 1+ | 0.23 | 53% | **+9.4%**  | +51% / -37% | 1.3 | 34% | -2.0% (649) |
| 1st half | DIAMOND (TUNED) | WAIT FOR THE LINE CROSS | SPY+QQQ 1m | LINE COLOR / ATM 1DTE | none | 0.70 | 35% | **-1.0%**  | +28% / -17% | -0.5 | 0% | -0.9% (2042) |
| 2nd half | DIAMOND (TUNED) | WAIT FOR THE LINE CROSS | SPY+QQQ 1m | OPTION TRAIL 15% / 2 ITM 0DTE | none | 0.82 | 23% | **-4.9%**  | +22% / -13% | -3.8 | 0% | -1.2% (1742) |
| 1st half | DIAMOND (TUNED) | WAIT FOR THE LINE CROSS | SPY+QQQ 2m | OPTION +10% / -10% / 1 ITM 0DTE | none | 1.74 | 44% | **-2.1%**  | +15% / -15% | -2.5 | 0% | -1.3% (6544) |
| 2nd half | DIAMOND (TUNED) | WAIT FOR THE LINE CROSS | SPY+QQQ 2m | ANGLE BACK -20 / 1 ITM 0DTE | none | 1.38 | 35% | **-9.2%**  | +52% / -43% | -3.0 | 0% | -1.8% (5018) |
| 1st half | DIAMOND (TUNED) | WAIT FOR THE LINE CROSS | SPY+QQQ 2m | OPTION +10% / -10% / 1 ITM 0DTE | score 1+ | 0.65 | 43% | **-2.2%**  | +15% / -16% | -1.6 | 0% | -1.5% (1712) |
| 1st half | DIAMOND (TUNED) | WAIT FOR THE LINE CROSS | SPY+QQQ 3m | LINE BREAK / 2 ITM 0DTE | none | 0.58 | 21% | **-3.3%**  | +34% / -13% | -1.4 | 0% | -0.7% (2122) |
| 2nd half | DIAMOND (TUNED) | WAIT FOR THE LINE CROSS | SPY+QQQ 3m | 15 MINUTES / 2 ITM 2DTE | none | 0.42 | 44% | **-1.3%**  | +10% / -10% | -1.0 | 0% | -1.3% (1225) |
| 1st half | DIAMOND (TUNED) | WAIT FOR THE LINE CROSS | SPY+QQQ 5m | 30 MINUTES / 3 ITM 2DTE | none | 0.49 | 38% | **-3.1%**  | +13% / -13% | -2.3 | 0% | -1.3% (2062) |
| 2nd half | DIAMOND (TUNED) | WAIT FOR THE LINE CROSS | SPY+QQQ 5m | ANGLE BACK -20 / 3 ITM 0DTE | none | 0.80 | 45% | **-5.7%**  | +33% / -37% | -1.8 | 0% | +1.1% (2709) |
| 1st half | DIAMOND (TUNED) | WAIT FOR THE LINE CROSS | SPY+QQQ 5m | 30 MINUTES / 3 ITM 2DTE | score 1+ | 0.11 | 31% | **-3.1%**  | +15% / -11% | -1.1 | 0% | -0.5% (595) |
| 1st half | TREND LINE CROSS | AT THE SIGNAL | SPY+QQQ 1m | LINE COLOR / 3 ITM 0DTE | none | 58.49 | 37% | **-1.2%**  | +34% / -22% | -1.4 | 0% | -0.5% (10452) |
| 2nd half | TREND LINE CROSS | AT THE SIGNAL | SPY+QQQ 1m | LINE COLOR / 2 ITM 0DTE | none | 101.76 | 34% | **-1.0%**  | +28% / -16% | -1.6 | 0% | -0.5% (17439) |
| 1st half | TREND LINE CROSS | AT THE SIGNAL | SPY+QQQ 2m | LINE COLOR / 2 ITM 0DTE | none | 28.92 | 36% | **-1.5%**  | +38% / -24% | -1.6 | 0% | -0.4% (4086) |
| 2nd half | TREND LINE CROSS | AT THE SIGNAL | SPY+QQQ 2m | LINE COLOR / 2 ITM 0DTE | none | 39.20 | 36% | **-0.9%**  | +29% / -18% | -1.3 | 0% | -0.1% (7238) |
| 2nd half | TREND LINE CROSS | AT THE SIGNAL | SPY+QQQ 2m | LINE COLOR / 2 ITM 0DTE | score 1+ | 0.96 | 36% | **-1.3%**  | +44% / -27% | -0.4 | 0% | -1.3% (1198) |
| 1st half | TREND LINE CROSS | AT THE SIGNAL | SPY+QQQ 3m | LINE COLOR / 2 ITM 0DTE | none | 19.79 | 36% | **-2.2%**  | +46% / -29% | -1.9 | 0% | +0.2% (3279) |
| 2nd half | TREND LINE CROSS | AT THE SIGNAL | SPY+QQQ 3m | ANGLE BACK -20 / 1 OTM 1DTE | none | 5.71 | 40% | **-2.3%**  | +37% / -28% | -1.8 | 0% | -1.4% (1123) |
| 1st half | TREND LINE CROSS | AT THE SIGNAL | SPY+QQQ 5m | LINE BREAK / 1 ITM 0DTE | none | 10.46 | 26% | **-1.6%**  | +53% / -21% | -1.4 | 0% | -2.8% (1796) |
| 2nd half | TREND LINE CROSS | AT THE SIGNAL | SPY+QQQ 5m | ANGLE BACK -20 / 1 OTM 1DTE | none | 7.94 | 41% | **-0.7%**  | +38% / -28% | -0.6 | 0% | +0.4% (1272) |
| 1st half | LINE TURNS YOUR COLOR | AT THE SIGNAL | SPY+QQQ 1m | LINE COLOR / 1 ITM 0DTE | none | 2.75 | 28% | **-1.1%**  | +71% / -29% | -0.4 | 0% | -0.9% (2231) |
| 2nd half | LINE TURNS YOUR COLOR | AT THE SIGNAL | SPY+QQQ 1m | ANGLE BACK -20 / 1 OTM 1DTE | none | 10.12 | 40% | **+0.0%**  | +39% / -26% | 0.0 | 1% | -2.0% (10765) |
| 2nd half | LINE TURNS YOUR COLOR | AT THE SIGNAL | SPY+QQQ 1m | ANGLE BACK -20 / 1 OTM 1DTE | score 1+ | 0.19 | 32% | **-7.7%**  | +29% / -25% | -1.7 | 0% | -4.0% (1173) |
| 1st half | LINE TURNS YOUR COLOR | AT THE SIGNAL | SPY+QQQ 2m | LINE COLOR / 1 ITM 0DTE | none | 6.27 | 32% | **+0.6%**  | +75% / -35% | 0.3 | 1% | -0.7% (2048) |
| 2nd half | LINE TURNS YOUR COLOR | AT THE SIGNAL | SPY+QQQ 2m | ANGLE BACK -20 / 1 ITM 0DTE | none | 12.68 | 41% | **-1.6%**  | +59% / -43% | -1.0 | 0% | -1.4% (8756) |
| 2nd half | LINE TURNS YOUR COLOR | AT THE SIGNAL | SPY+QQQ 2m | ANGLE BACK -20 / 1 ITM 0DTE | score 1+ | 2.20 | 42% | **-0.1%**  | +61% / -44% | -0.0 | 0% | -1.4% (3278) |
| 1st half | LINE TURNS YOUR COLOR | AT THE SIGNAL | SPY+QQQ 3m | LINE OR STRUCTURE / 1 ITM 0DTE | none | 4.16 | 31% | **-0.7%**  | +47% / -22% | -0.4 | 0% | -2.4% (2072) |
| 2nd half | LINE TURNS YOUR COLOR | AT THE SIGNAL | SPY+QQQ 3m | LINE COLOR / 1 ITM 0DTE | none | 5.18 | 34% | **-0.5%**  | +63% / -34% | -0.3 | 0% | -0.6% (2510) |
| 1st half | LINE TURNS YOUR COLOR | AT THE SIGNAL | SPY+QQQ 3m | LINE OR STRUCTURE / 1 ITM 0DTE | score 1+ | 1.42 | 31% | **+0.1%**  | +52% / -24% | 0.0 | 1% | -1.9% (401) |
| 1st half | LINE TURNS YOUR COLOR | AT THE SIGNAL | SPY+QQQ 5m | LINE COLOR / 1 ITM 0DTE | none | 4.79 | 37% | **-1.2%**  | +64% / -39% | -0.5 | 0% | -0.5% (2622) |
| 2nd half | LINE TURNS YOUR COLOR | AT THE SIGNAL | SPY+QQQ 5m | ANGLE BACK -20 / 2 ITM 0DTE | none | 7.56 | 45% | **+1.6%**  | +49% / -37% | 0.9 | 5% | +0.5% (3350) |
| 1st half | ANGLE UP THROUGH 23 | AT THE SIGNAL | SPY+QQQ 1m | OPTION TRAIL 15% / 3 ITM 2DTE | none | 0.49 | 36% | **+0.3%**  | +21% / -11% | 0.1 | 6% | -1.2% (5386) |
| 2nd half | ANGLE UP THROUGH 23 | AT THE SIGNAL | SPY+QQQ 1m | ANGLE BACK -20 / ATM 2DTE | none | 0.97 | 46% | **+6.4%**  | +40% / -22% | 1.6 | 38% | -1.4% (9528) |
| 1st half | ANGLE UP THROUGH 23 | AT THE SIGNAL | SPY+QQQ 2m | LINE COLOR / 1 OTM 2DTE | none | 0.43 | 48% | **+6.6%**  | +40% / -24% | 1.4 | 41% | -0.8% (2380) |
| 2nd half | ANGLE UP THROUGH 23 | AT THE SIGNAL | SPY+QQQ 2m | ANGLE BACK -20 / 3 ITM 1DTE | none | 0.33 | 45% | **+7.4%**  | +42% / -21% | 1.4 | 49% | -0.5% (6133) |
| 1st half | ANGLE UP THROUGH 23 | AT THE SIGNAL | SPY+QQQ 3m | LINE COLOR / 2 ITM 0DTE | none | 0.38 | 43% | **+8.4%**  | +78% / -44% | 0.8 | 15% | +0.1% (2159) |
| 2nd half | ANGLE UP THROUGH 23 | AT THE SIGNAL | SPY+QQQ 3m | OPTION +10% / -20% / 3 ITM 2DTE | none | 0.52 | 60% | **-0.4%**  | +12% / -19% | -0.3 | 0% | -1.3% (3429) |
| 1st half | ANGLE UP THROUGH 23 | AT THE SIGNAL | SPY+QQQ 5m | ANGLE BACK -20 / 2 ITM 2DTE | none | 0.33 | 47% | **+4.2%**  | +32% / -20% | 1.0 | 38% | -1.2% (2886) |
| 2nd half | ANGLE UP THROUGH 23 | AT THE SIGNAL | SPY+QQQ 5m | 5 MINUTES / 1 ITM 1DTE | none | 0.14 | 50% | **-0.7%**  | +13% / -14% | -0.2 | 0% | -1.3% (2010) |
| 1st half | ANGLE FLATTENS THROUGH 23 | AT THE SIGNAL | SPY+QQQ 1m | OPTION +10% / -10% / 1 OTM 1DTE | none | 1.29 | 51% | **+0.1%**  | +13% / -14% | 0.1 | 3% | -1.6% (17676) |
| 2nd half | ANGLE FLATTENS THROUGH 23 | AT THE SIGNAL | SPY+QQQ 1m | ANGLE BACK -20 / 3 ITM 1DTE | none | 1.24 | 45% | **+3.9%**  | +37% / -23% | 1.2 | 26% | -1.2% (8722) |
| 1st half | ANGLE FLATTENS THROUGH 23 | AT THE SIGNAL | SPY+QQQ 2m | LINE COLOR / 1 ITM 2DTE | none | 0.44 | 47% | **+5.7%**  | +35% / -21% | 1.1 | 43% | -0.9% (4978) |
| 2nd half | ANGLE FLATTENS THROUGH 23 | AT THE SIGNAL | SPY+QQQ 2m | ANGLE BACK -20 / 3 ITM 1DTE | none | 0.79 | 46% | **+5.2%**  | +38% / -22% | 1.5 | 36% | -0.5% (7426) |
| 1st half | ANGLE FLATTENS THROUGH 23 | AT THE SIGNAL | SPY+QQQ 3m | 15 MINUTES / 1 ITM 2DTE | none | 0.46 | 49% | **+2.5%**  | +17% / -11% | 1.4 | 79% | -0.9% (5284) |
| 2nd half | ANGLE FLATTENS THROUGH 23 | AT THE SIGNAL | SPY+QQQ 3m | ANGLE BACK -20 / 3 ITM 2DTE | none | 0.10 | 38% | **+0.0%**  | +41% / -26% | 0.0 | 1% | -1.1% (1358) |
| 1st half | ANGLE FLATTENS THROUGH 23 | AT THE SIGNAL | SPY+QQQ 5m | 30 MINUTES / 2 ITM 0DTE | none | 0.20 | 50% | **+6.7%**  | +40% / -27% | 1.1 | 36% | -0.9% (1276) |
| 2nd half | ANGLE FLATTENS THROUGH 23 | AT THE SIGNAL | SPY+QQQ 5m | 5 MINUTES / 2 ITM 0DTE | none | 0.21 | 52% | **+3.8%**  | +18% / -11% | 1.5 | 100% | -1.4% (3076) |
| 1st half | ANGLE FLATTENS THROUGH 23 | AT THE SIGNAL | SPY+QQQ 5m | 30 MINUTES / 2 ITM 0DTE | score 1+ | 0.13 | 48% | **+3.7%**  | +40% / -29% | 0.4 | 19% | -1.2% (483) |
| 1st half | FEAR / GREED MAXED | AT THE SIGNAL | SPY+QQQ 1m | LINE COLOR / 2 ITM 0DTE | none | 3.04 | 43% | **+3.4%**  | +58% / -37% | 1.0 | 10% | +0.3% (1813) |
| 2nd half | FEAR / GREED MAXED | AT THE SIGNAL | SPY+QQQ 1m | ANGLE BACK -20 / 3 ITM 0DTE | none | 31.36 | 42% | **-0.4%**  | +39% / -29% | -0.5 | 0% | -1.6% (15825) |
| 1st half | FEAR / GREED MAXED | AT THE SIGNAL | SPY+QQQ 2m | LINE COLOR / 2 ITM 0DTE | none | 3.53 | 38% | **-0.3%**  | +47% / -29% | -0.1 | 0% | -1.2% (3466) |
| 2nd half | FEAR / GREED MAXED | AT THE SIGNAL | SPY+QQQ 2m | LINE COLOR / 2 ITM 0DTE | none | 6.80 | 37% | **+2.2%**  | +48% / -25% | 1.1 | 10% | +1.5% (2727) |
| 1st half | FEAR / GREED MAXED | AT THE SIGNAL | SPY+QQQ 2m | LINE COLOR / 2 ITM 0DTE | score 1+ | 0.63 | 44% | **+5.7%**  | +46% / -25% | 1.4 | 33% | -2.3% (994) |
| 1st half | FEAR / GREED MAXED | AT THE SIGNAL | SPY+QQQ 3m | LINE COLOR / 2 ITM 0DTE | none | 1.92 | 43% | **+7.7%**  | +61% / -33% | 2.1 | 24% | +0.5% (1792) |
| 2nd half | FEAR / GREED MAXED | AT THE SIGNAL | SPY+QQQ 3m | LINE COLOR / 1 ITM 0DTE | none | 2.27 | 39% | **+4.6%**  | +61% / -31% | 1.2 | 13% | -3.0% (1546) |
| 2nd half | FEAR / GREED MAXED | AT THE SIGNAL | SPY+QQQ 3m | LINE COLOR / 1 ITM 0DTE | score 1+ | 0.38 | 46% | **+8.7%**  | +63% / -36% | 1.2 | 25% | -6.1% (267) |
| 1st half | FEAR / GREED MAXED | AT THE SIGNAL | SPY+QQQ 5m | ANGLE BACK -20 / 3 ITM 0DTE | none | 6.87 | 42% | **-2.1%**  | +42% / -34% | -1.6 | 0% | -1.6% (2818) |
| 2nd half | FEAR / GREED MAXED | AT THE SIGNAL | SPY+QQQ 5m | LINE COLOR / 2 ITM 0DTE | none | 1.54 | 37% | **-1.1%**  | +51% / -32% | -0.3 | 0% | +3.0% (1405) |
| 2nd half | FEAR / GREED MAXED | AT THE SIGNAL | SPY+QQQ 5m | LINE COLOR / 2 ITM 0DTE | score 1+ | 0.23 | 42% | **-3.8%**  | +44% / -38% | -0.4 | 0% | +1.8% (449) |
| 1st half | FEAR / GREED MAXED | WAIT FOR THE LINE CROSS | SPY+QQQ 1m | LINE COLOR / 1 ITM 0DTE | none | 1.56 | 40% | **+1.3%**  | +70% / -44% | 0.2 | 3% | -0.6% (1074) |
| 2nd half | FEAR / GREED MAXED | WAIT FOR THE LINE CROSS | SPY+QQQ 1m | ANGLE BACK -20 / 3 ITM 0DTE | none | 21.61 | 43% | **+0.1%**  | +41% / -31% | 0.1 | 1% | -1.4% (13891) |
| 2nd half | FEAR / GREED MAXED | WAIT FOR THE LINE CROSS | SPY+QQQ 1m | ANGLE BACK -20 / 3 ITM 0DTE | score 1+ | 1.18 | 43% | **+4.4%**  | +53% / -32% | 0.9 | 15% | -0.5% (308) |
| 1st half | FEAR / GREED MAXED | WAIT FOR THE LINE CROSS | SPY+QQQ 2m | LINE COLOR / 2 ITM 0DTE | none | 2.90 | 42% | **+2.5%**  | +50% / -32% | 0.9 | 10% | -0.4% (3513) |
| 2nd half | FEAR / GREED MAXED | WAIT FOR THE LINE CROSS | SPY+QQQ 2m | LINE COLOR / 2 ITM 0DTE | none | 11.85 | 36% | **+0.2%**  | +32% / -18% | 0.1 | 1% | +0.4% (5991) |
| 2nd half | FEAR / GREED MAXED | WAIT FOR THE LINE CROSS | SPY+QQQ 2m | LINE COLOR / 2 ITM 0DTE | score 1+ | 0.55 | 38% | **-3.3%**  | +35% / -27% | -0.9 | 0% | -0.1% (114) |
| 1st half | FEAR / GREED MAXED | WAIT FOR THE LINE CROSS | SPY+QQQ 3m | LINE COLOR / 3 ITM 2DTE | none | 0.91 | 50% | **+5.4%**  | +30% / -19% | 2.0 | 61% | +0.6% (1028) |
| 2nd half | FEAR / GREED MAXED | WAIT FOR THE LINE CROSS | SPY+QQQ 3m | ANGLE BACK -20 / 1 OTM 1DTE | none | 4.29 | 39% | **-1.8%**  | +37% / -27% | -1.2 | 0% | -1.5% (2419) |
| 1st half | FEAR / GREED MAXED | WAIT FOR THE LINE CROSS | SPY+QQQ 5m | LINE COLOR / 3 ITM 2DTE | none | 1.64 | 40% | **-0.7%**  | +18% / -13% | -0.5 | 0% | -0.2% (800) |
| 2nd half | FEAR / GREED MAXED | WAIT FOR THE LINE CROSS | SPY+QQQ 5m | LINE COLOR / ATM 0DTE | none | 4.67 | 32% | **-3.5%**  | +48% / -27% | -1.6 | 0% | +0.8% (2045) |
| 2nd half | FEAR / GREED MAXED | WAIT FOR THE LINE CROSS | SPY+QQQ 5m | LINE COLOR / ATM 0DTE | score 1+ | 0.21 | 35% | **-8.7%**  | +57% / -44% | -0.8 | 0% | +3.0% (470) |
| 1st half | GAP & GO | AT THE SIGNAL | SPY+QQQ 1m | OPTION +20% / -10% / 1 OTM 1DTE | none | 0.39 | 42% | **+0.6%**  | +22% / -15% | 0.3 | 16% | -1.7% (11215) |
| 2nd half | GAP & GO | AT THE SIGNAL | SPY+QQQ 1m | OPTION +10% / -20% / 3 ITM 0DTE | none | 0.51 | 63% | **+0.6%**  | +14% / -22% | 0.3 | 15% | -1.6% (16613) |
| 1st half | GAP & GO | AT THE SIGNAL | SPY+QQQ 2m | OPTION +5% / -10% / 3 ITM 1DTE | none | 0.53 | 57% | **-0.3%**  | +8% / -12% | -0.3 | 0% | -1.0% (8150) |
| 2nd half | GAP & GO | AT THE SIGNAL | SPY+QQQ 2m | OPTION +10% / -20% / 2 ITM 0DTE | none | 0.50 | 67% | **+1.8%**  | +14% / -23% | 1.0 | 45% | -1.0% (8690) |
| 1st half | GAP & GO | AT THE SIGNAL | SPY+QQQ 3m | OPTION +10% / -20% / 1 OTM 0DTE | none | 0.51 | 54% | **-0.3%**  | +19% / -23% | -0.1 | 0% | -4.5% (5707) |
| 2nd half | GAP & GO | AT THE SIGNAL | SPY+QQQ 3m | OPTION +20% / -10% / 2 ITM 1DTE | none | 0.50 | 42% | **+0.9%**  | +21% / -13% | 0.6 | 29% | -1.4% (5465) |
| 1st half | GAP & GO | AT THE SIGNAL | SPY+QQQ 5m | 5 MINUTES / 2 ITM 0DTE | none | 0.51 | 55% | **+3.3%**  | +18% / -14% | 1.6 | 80% | -1.0% (3512) |
| 2nd half | GAP & GO | AT THE SIGNAL | SPY+QQQ 5m | 5 MINUTES / 1 ITM 0DTE | none | 0.50 | 55% | **+2.1%**  | +14% / -12% | 1.4 | 85% | -1.7% (3369) |
| 1st half | PAUSE THEN GO | AT THE SIGNAL | SPY+QQQ 1m | OPTION +10% / -20% / 2 ITM 1DTE | none | 0.50 | 56% | **-2.8%**  | +12% / -21% | -1.7 | 0% | -1.3% (17384) |
| 2nd half | PAUSE THEN GO | AT THE SIGNAL | SPY+QQQ 1m | ANGLE BACK -20 / 3 ITM 0DTE | none | 0.43 | 51% | **+12.3%**  | +56% / -34% | 1.2 | 32% | -1.8% (13486) |
| 1st half | PAUSE THEN GO | AT THE SIGNAL | SPY+QQQ 2m | TRAIL STRUCTURE / 1 ITM 0DTE | none | 0.25 | 38% | **-1.8%**  | +21% / -16% | -0.6 | 0% | -1.3% (8716) |
| 2nd half | PAUSE THEN GO | AT THE SIGNAL | SPY+QQQ 2m | OPTION +20% / -10% / 1 ITM 2DTE | none | 0.30 | 42% | **+0.8%**  | +21% / -14% | 0.4 | 25% | -1.0% (7849) |
| 1st half | RANDOM | AT THE SIGNAL | SPY+QQQ 1m | LINE COLOR / 2 ITM 0DTE | none | 36.13 | 36% | **-0.9%**  | +40% / -24% | -1.0 | 0% | -0.9% (12211) |
| 2nd half | RANDOM | AT THE SIGNAL | SPY+QQQ 1m | LINE COLOR / 3 ITM 0DTE | none | 16.30 | 38% | **+0.4%**  | +36% / -22% | 0.3 | 2% | +0.4% (5494) |
| 1st half | RANDOM | AT THE SIGNAL | SPY+QQQ 2m | LINE COLOR / 2 ITM 0DTE | none | 6.17 | 42% | **+0.2%**  | +48% / -34% | 0.1 | 1% | +0.2% (2086) |
| 2nd half | RANDOM | AT THE SIGNAL | SPY+QQQ 2m | LINE COLOR / 2 ITM 0DTE | none | 25.79 | 39% | **-0.0%**  | +29% / -18% | -0.0 | 0% | -0.0% (8690) |
| 2nd half | RANDOM | AT THE SIGNAL | SPY+QQQ 2m | LINE COLOR / 2 ITM 0DTE | score 2+ | 1.06 | 42% | **-0.7%**  | +7% / -6% | -1.3 | 0% | -0.7% (357) |
| 1st half | RANDOM | AT THE SIGNAL | SPY+QQQ 3m | LINE COLOR / 3 ITM 0DTE | none | 9.41 | 39% | **-0.2%**  | +35% / -23% | -0.2 | 0% | -0.2% (3180) |
| 2nd half | RANDOM | AT THE SIGNAL | SPY+QQQ 3m | ANGLE BACK -20 / 3 ITM 0DTE | none | 9.45 | 43% | **-2.4%**  | +36% / -32% | -2.5 | 0% | -2.4% (3183) |
| 1st half | RANDOM | AT THE SIGNAL | SPY+QQQ 5m | ANGLE BACK -20 / 3 ITM 0DTE | none | 2.06 | 47% | **+0.7%**  | +43% / -36% | 0.3 | 2% | +0.7% (696) |
| 2nd half | RANDOM | AT THE SIGNAL | SPY+QQQ 5m | LINE COLOR / 2 ITM 0DTE | none | 2.01 | 43% | **+2.0%**  | +49% / -34% | 0.7 | 7% | +2.0% (678) |
| 2nd half | RANDOM | AT THE SIGNAL | SPY+QQQ 5m | LINE COLOR / 2 ITM 0DTE | score 1+ | 0.38 | 44% | **+2.7%**  | +49% / -34% | 0.5 | 10% | +2.7% (127) |
| 1st half | RANDOM | WAIT FOR THE LINE CROSS | SPY+QQQ 1m | LINE COLOR / 2 ITM 0DTE | none | 32.01 | 36% | **-0.8%**  | +40% / -24% | -0.8 | 0% | -0.8% (10818) |
| 2nd half | RANDOM | WAIT FOR THE LINE CROSS | SPY+QQQ 1m | LINE COLOR / 2 ITM 0DTE | none | 31.43 | 35% | **-0.3%**  | +32% / -18% | -0.4 | 0% | -0.3% (10592) |
| 1st half | RANDOM | WAIT FOR THE LINE CROSS | SPY+QQQ 2m | LINE COLOR / 2 ITM 0DTE | none | 10.50 | 39% | **-0.1%**  | +46% / -29% | -0.1 | 0% | -0.1% (3549) |
| 2nd half | RANDOM | WAIT FOR THE LINE CROSS | SPY+QQQ 2m | LINE COLOR / 2 ITM 0DTE | none | 21.94 | 38% | **+0.3%**  | +34% / -20% | 0.4 | 2% | +0.3% (7393) |
| 1st half | RANDOM | WAIT FOR THE LINE CROSS | SPY+QQQ 3m | LINE BREAK / 1 ITM 0DTE | none | 7.28 | 26% | **-3.5%**  | +36% / -17% | -3.1 | 0% | -3.5% (2461) |
| 2nd half | RANDOM | WAIT FOR THE LINE CROSS | SPY+QQQ 3m | ANGLE BACK -20 / 3 ITM 0DTE | none | 7.39 | 44% | **-2.0%**  | +37% / -32% | -1.7 | 0% | -2.0% (2492) |
| 1st half | RANDOM | WAIT FOR THE LINE CROSS | SPY+QQQ 5m | LINE COLOR / 3 ITM 0DTE | none | 3.38 | 48% | **+2.0%**  | +38% / -31% | 0.9 | 9% | +2.0% (1143) |
| 2nd half | RANDOM | WAIT FOR THE LINE CROSS | SPY+QQQ 5m | LINE COLOR / 2 ITM 0DTE | none | 3.66 | 42% | **+0.8%**  | +36% / -24% | 0.5 | 4% | +0.8% (1232) |
| 2nd half | RANDOM | WAIT FOR THE LINE CROSS | SPY+QQQ 5m | LINE COLOR / 2 ITM 0DTE | score 1+ | 0.40 | 44% | **+2.4%**  | +50% / -35% | 0.5 | 9% | +2.4% (134) |
| 2nd half | PAUSE THEN GO | AT THE SIGNAL | SPY+QQQ 3m | OPTION +10% / -20% / 3 ITM 2DTE | none | 0.18 | 48% | **-6.1%**  | +10% / -21% | -2.5 | 0% | -1.3% (3429) |
| 2nd half | PAUSE THEN GO | AT THE SIGNAL | SPY+QQQ 5m | OPTION +5% / -10% / 3 ITM 0DTE | none | 0.12 | 73% | **+2.5%**  | +8% / -12% | 1.6 | 100% | -1.1% (3187) |

## 6. BEST SINGLE READING OR PAIR - picked on one half (by t), judged on the other
| Picked on | Signal | Entry | Chart | Trade | Readings | t when picked | Fires/day | Win % | Avg | t | Random + same readings |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1st half | TREND LINE CROSS | AT THE SIGNAL | SPY+QQQ 3m | LINE COLOR / 2 ITM 0DTE | REAL VIX today (VIXY vs yesterday): up 3%+ + REAL VIX vs its 20-day average: LOW (5%+ under) | 3.6 | 0.07 | 62% | **+85.0%** ✅ | 3.1 | - |
| 1st half | TREND LINE CROSS | AT THE SIGNAL | SPY+QQQ ALL CHARTS | LINE COLOR / 2 ITM 0DTE | REAL VIX today (VIXY vs yesterday): up 3%+ + REAL VIX vs its 20-day average: LOW (5%+ under) | 7.9 | 0.42 | 50% | **+43.6%**  | 1.1 | +13.8% (81) |
| 1st half | ANGLE UP THROUGH 23 | AT THE SIGNAL | SPY+QQQ ALL CHARTS | LINE COLOR / 2 ITM 0DTE | Today's gap (daily ATR, + = your way): 0.3+ AGAINST you + A diamond AGAINST you in the last 10 candles: no | 5.1 | 0.66 | 45% | **+21.0%**  | 1.1 | -1.6% (7570) |
| 1st half | TREND LINE CROSS | AT THE SIGNAL | SPY+QQQ 1m | LINE COLOR / 3 ITM 0DTE | REAL VIX today (VIXY vs yesterday): up 3%+ + REAL VIX vs its 20-day average: LOW (5%+ under) | 6.2 | 0.19 | 41% | **+17.4%**  | 0.6 | -10.0% (26) |
| 2nd half | LINE TURNS YOUR COLOR | AT THE SIGNAL | SPY+QQQ 5m | ANGLE BACK -20 / 2 ITM 0DTE | Vix Fix AGAINST you now (fear for longs / greed for shorts): 85+ + Your side MAXED (95+) in the last 30 candles: no | 3.2 | 0.06 | 48% | **+16.1%**  | 1.6 | -1.7% (176) |
| 2nd half | DIAMOND (TUNED) | AT THE SIGNAL | SPY+QQQ 5m | ANGLE BACK -20 / 3 ITM 0DTE | Price vs VWAP (ATR, + = your side): 1-3 wrong side + Distance from the 20-candle extreme behind you ($): $1+ | 2.3 | 0.14 | 60% | **+15.6%**  | 1.7 | +4.5% (180) |
| 1st half | ANGLE UP THROUGH 23 | AT THE SIGNAL | SPY+QQQ 3m | LINE COLOR / 2 ITM 0DTE | Your side: change in the last 2 candles: flat / falling + Price vs VWAP (ATR, + = your side): 3+ your side | 3.3 | 0.33 | 46% | **+14.6%**  | 1.2 | -0.7% (695) |
| 2nd half | FEAR / GREED MAXED | WAIT FOR THE LINE CROSS | SPY+QQQ 3m | ANGLE BACK -20 / 1 OTM 1DTE | REAL VIX vs its 20-day average: HIGH (5%+ over) + A diamond AGAINST you in the last 10 candles: YES | 3.2 | 0.32 | 52% | **+12.0%**  | 1.7 | -1.8% (131) |
| 1st half | ANGLE UP THROUGH 23 | AT THE SIGNAL | SPY+QQQ 2m | LINE COLOR / 1 OTM 2DTE | Against side MAXED (95+) in the last 10 candles: no + Today's gap (daily ATR, + = your way): 0.3+ AGAINST you | 3.0 | 0.15 | 46% | **+11.2%**  | 1.0 | -1.9% (1561) |
| 2nd half | FEAR / GREED MAXED | WAIT FOR THE LINE CROSS | SPY+QQQ 1m | ANGLE BACK -20 / 3 ITM 0DTE | Price vs VWAP (ATR, + = your side): 3+ your side + REAL VIX vs its 20-day average: HIGH (5%+ over) | 4.5 | 1.31 | 44% | **+10.8%**  | 1.3 | +2.9% (975) |
| 2nd half | DIAMOND (TUNED) | AT THE SIGNAL | SPY+QQQ ALL CHARTS | ANGLE BACK -20 / 2 ITM 0DTE | Price vs VWAP (ATR, + = your side): 1-3 wrong side + REAL VIX vs its 20-day average: HIGH (5%+ over) | 3.0 | 0.49 | 49% | **+10.7%**  | 1.8 | -0.2% (1116) |
| 1st half | ANGLE FLATTENS THROUGH 23 | AT THE SIGNAL | SPY+QQQ 2m | LINE COLOR / 1 ITM 2DTE | Vix Fix YOUR side now (greed for longs / fear for shorts): 85+ + Today's gap (daily ATR, + = your way): 0.3+ AGAINST you | 3.8 | 0.09 | 47% | **+9.6%**  | 0.8 | +0.1% (254) |
| 2nd half | RANDOM | AT THE SIGNAL | SPY+QQQ 5m | LINE COLOR / 2 ITM 0DTE | Your side: change in the last 2 candles: flat / falling + Price vs trend line (ATR): 1+ your side | 3.2 | 0.89 | 50% | **+9.1%**  | 2.1 | +9.1% (301) |
| 2nd half | RANDOM | WAIT FOR THE LINE CROSS | SPY+QQQ 5m | LINE COLOR / 2 ITM 0DTE | Your side: change in the last 2 candles: flat / falling + Price vs trend line (ATR): 1+ your side | 3.2 | 0.89 | 50% | **+9.1%**  | 2.1 | +9.1% (301) |
| 2nd half | ANGLE UP THROUGH 23 | AT THE SIGNAL | SPY+QQQ 1m | ANGLE BACK -20 / ATM 2DTE | REAL VIX today (VIXY vs yesterday): down + Chart ATR vs its recent average: wild (1.6x+) | 3.7 | 0.26 | 53% | **+8.5%**  | 1.1 | -1.5% (2176) |
| 2nd half | FEAR / GREED MAXED | AT THE SIGNAL | SPY+QQQ ALL CHARTS | LINE COLOR / 2 ITM 0DTE | Price vs VWAP (ATR, + = your side): 3+ your side + REAL VIX vs its 20-day average: HIGH (5%+ over) | 6.6 | 2.50 | 42% | **+8.3%**  | 0.9 | +5.7% (1693) |
| 2nd half | ANGLE FLATTENS THROUGH 23 | AT THE SIGNAL | SPY+QQQ 1m | ANGLE BACK -20 / 3 ITM 1DTE | REAL VIX today (VIXY vs yesterday): down + Chart ATR vs its recent average: wild (1.6x+) | 3.6 | 0.32 | 53% | **+7.6%**  | 1.7 | -1.0% (2005) |
| 2nd half | RANDOM | WAIT FOR THE LINE CROSS | SPY+QQQ 2m | LINE COLOR / 2 ITM 0DTE | Price vs VWAP (ATR, + = your side): 3+ your side + Options today: 9:45 straddle vs the last 20 days' move: unknown | 3.1 | 0.29 | 53% | **+7.5%**  | 0.9 | +7.5% (97) |
| 2nd half | FEAR / GREED MAXED | AT THE SIGNAL | SPY+QQQ 1m | ANGLE BACK -20 / 3 ITM 0DTE | Price vs VWAP (ATR, + = your side): 3+ your side + REAL VIX vs its 20-day average: HIGH (5%+ over) | 6.5 | 1.71 | 43% | **+7.4%**  | 0.9 | +1.4% (1052) |
| 2nd half | ANGLE FLATTENS THROUGH 23 | AT THE SIGNAL | SPY+QQQ ALL CHARTS | 30 MINUTES / 1 ITM 1DTE | REAL VIX vs its 20-day average: LOW (5%+ under) + Day's range so far vs the 20-day average day: already a full day+ | 5.3 | 0.13 | 52% | **+7.3%**  | 1.0 | -1.5% (655) |
| 2nd half | RANDOM | WAIT FOR THE LINE CROSS | SPY+QQQ ALL CHARTS | LINE COLOR / 2 ITM 0DTE | Price vs VWAP (ATR, + = your side): 3+ your side + REAL VIX vs its 20-day average: HIGH (5%+ over) | 5.2 | 4.72 | 44% | **+6.3%**  | 1.1 | +6.3% (1589) |
| 1st half | ANGLE FLATTENS THROUGH 23 | AT THE SIGNAL | SPY+QQQ ALL CHARTS | LINE COLOR / 1 ITM 2DTE | Price vs VWAP (ATR, + = your side): 3+ your side + Day's range so far vs the 20-day average day: already a full day+ | 5.4 | 0.72 | 50% | **+6.0%**  | 0.9 | -0.5% (2485) |
| 2nd half | RANDOM | AT THE SIGNAL | SPY+QQQ ALL CHARTS | LINE COLOR / 2 ITM 0DTE | Price vs VWAP (ATR, + = your side): 3+ your side + REAL VIX vs its 20-day average: HIGH (5%+ over) | 5.2 | 5.02 | 43% | **+5.7%**  | 1.0 | +5.7% (1693) |
| 2nd half | FEAR / GREED MAXED | WAIT FOR THE LINE CROSS | SPY+QQQ ALL CHARTS | LINE COLOR / 2 ITM 0DTE | Distance from the 20-candle extreme behind you ($): $1+ + REAL VIX today (VIXY vs yesterday): down | 4.9 | 3.32 | 35% | **+5.6%**  | 0.9 | +0.9% (5839) |
| 2nd half | RANDOM | AT THE SIGNAL | SPY+QQQ 2m | LINE COLOR / 2 ITM 0DTE | Price vs VWAP (ATR, + = your side): 3+ your side + Options today: 9:45 straddle vs the last 20 days' move: unknown | 2.9 | 0.31 | 51% | **+5.6%**  | 0.7 | +5.6% (105) |
| 1st half | GAP & GO | AT THE SIGNAL | SPY+QQQ 5m | 5 MINUTES / 2 ITM 0DTE | TTM average size before now (ATR): 3+ + REAL VIX today (VIXY vs yesterday): down | 2.8 | 0.07 | 59% | **+4.6%**  | 1.1 | -1.8% (143) |
| 1st half | DIAMOND (YOURS) | AT THE SIGNAL | SPY+QQQ 2m | LINE COLOR / 2 ITM 0DTE | Your side Vix LINE COLOR: BUILDING (light blue / salmon) + Trade vs the day's move so far: WITH the day | 3.4 | 0.46 | 36% | **+4.2%**  | 0.8 | -0.3% (609) |
| 2nd half | ANGLE FLATTENS THROUGH 23 | AT THE SIGNAL | SPY+QQQ 5m | 5 MINUTES / 2 ITM 0DTE | Lines GLOW (Vix flow + TTM agree): no glow + Candles closed on your side of the trend line in a row: 6-15 | 3.0 | 0.13 | 56% | **+4.2%**  | 1.4 | -0.3% (198) |
| 2nd half | RANDOM | AT THE SIGNAL | SPY+QQQ 1m | LINE COLOR / 3 ITM 0DTE | REAL VIX vs its 20-day average: HIGH (5%+ over) + Chart ATR vs its recent average: normal | 4.4 | 3.31 | 40% | **+4.0%**  | 1.3 | +4.0% (1114) |
| 1st half | TREND LINE CROSS | AT THE SIGNAL | SPY+QQQ 2m | LINE COLOR / 2 ITM 0DTE | Against side Vix LINE COLOR: MAXED (bright blue / hot pink) + Today's gap (daily ATR, + = your way): 0.3+ YOUR way | 4.1 | 0.26 | 41% | **+4.0%**  | 0.7 | +3.0% (186) |
| 2nd half | GAP & GO | AT THE SIGNAL | SPY+QQQ ALL CHARTS | OPTION +10% / -20% / 2 ITM 0DTE | Vix flow (greed + fear averages): YOUR way + Day's range so far vs the 20-day average day: 40-70% | 7.1 | 0.06 | 71% | **+3.9%**  | 1.0 | -1.3% (4560) |
| 1st half | ANGLE FLATTENS THROUGH 23 | AT THE SIGNAL | SPY+QQQ 3m | 15 MINUTES / 1 ITM 2DTE | Your side Vix LINE COLOR: MAXED (bright blue / hot pink) + Trend paused: angle was 20+ your way, dipped under 5 (last 15 candles): no | 4.1 | 0.15 | 52% | **+3.6%**  | 1.2 | +1.4% (442) |
| 1st half | FEAR / GREED MAXED | WAIT FOR THE LINE CROSS | SPY+QQQ 3m | LINE COLOR / 3 ITM 2DTE | Options today: 9:45 straddle vs the last 20 days' move: fair + Higher chart (5m, or 15m for 5m) vs its trend line: WITH you | 3.6 | 0.54 | 46% | **+3.0%**  | 0.9 | -0.1% (854) |
| 1st half | RANDOM | WAIT FOR THE LINE CROSS | SPY+QQQ 3m | LINE BREAK / 1 ITM 0DTE | Lines GLOW (Vix flow + TTM agree): glow YOUR way + REAL VIX vs its 20-day average: HIGH (5%+ over) | 3.5 | 0.53 | 29% | **+2.8%**  | 0.5 | +2.8% (178) |
| 1st half | RANDOM | WAIT FOR THE LINE CROSS | SPY+QQQ 5m | LINE COLOR / 3 ITM 0DTE | Your side: change in the last 2 candles: flat / falling + Trade vs the day's move so far: WITH the day | 4.3 | 3.10 | 48% | **+2.6%**  | 1.1 | +2.6% (1047) |
| 1st half | ANGLE FLATTENS THROUGH 23 | AT THE SIGNAL | SPY+QQQ 5m | 30 MINUTES / 2 ITM 0DTE | Day's range so far vs the 20-day average day: already a full day+ + A diamond YOUR way in the last 10 candles (either setting): no | 4.2 | 0.14 | 47% | **+2.3%**  | 0.3 | -0.2% (676) |
| 2nd half | PAUSE THEN GO | AT THE SIGNAL | SPY+QQQ 5m | OPTION +5% / -10% / 3 ITM 0DTE | Your side MAXED (95+) in the last 30 candles: YES + Price vs VWAP (ATR, + = your side): 1-3 your side | 1.9 | 0.06 | 75% | **+2.3%**  | 1.1 | -0.3% (644) |
| 1st half | ANGLE FLATTENS THROUGH 23 | AT THE SIGNAL | SPY+QQQ 1m | OPTION +10% / -10% / 1 OTM 1DTE | Vix Fix YOUR side now (greed for longs / fear for shorts): 60-85 + Range of the last 20 candles ($): $1.50-3 | 3.7 | 0.14 | 60% | **+2.1%**  | 1.0 | -1.1% (1137) |
| 1st half | FEAR / GREED MAXED | AT THE SIGNAL | SPY+QQQ 1m | LINE COLOR / 2 ITM 0DTE | Distance from the 20-candle extreme behind you ($): $1+ + Volume vs this time of day (20-day avg): 2.5x+ | 5.1 | 0.92 | 42% | **+2.1%**  | 0.3 | +1.4% (340) |
| 2nd half | GAP & GO | AT THE SIGNAL | SPY+QQQ 5m | 5 MINUTES / 1 ITM 0DTE | Your side MAXED (95+) in the last 30 candles: no + Price vs VWAP (ATR, + = your side): 1-3 your side | 3.8 | 0.11 | 54% | **+2.0%**  | 0.7 | +0.4% (177) |
| 2nd half | FEAR / GREED MAXED | AT THE SIGNAL | SPY+QQQ 2m | LINE COLOR / 2 ITM 0DTE | Trend line angle (+ = your way): flat -5 to +5 + Range of the last 20 candles ($): under $0.75 | 3.9 | 0.25 | 37% | **+2.0%**  | 0.3 | -0.4% (424) |
| 2nd half | DIAMOND (YOURS) | AT THE SIGNAL | SPY+QQQ 5m | LINE COLOR / 2 ITM 0DTE | Your side MAXED (95+) in the last 30 candles: YES + Chart ATR vs its recent average: busy (1.2-1.6x) | 2.4 | 0.51 | 41% | **+1.9%**  | 0.7 | -2.0% (609) |
| 2nd half | ANGLE FLATTENS THROUGH 23 | AT THE SIGNAL | SPY+QQQ 2m | ANGLE BACK -20 / 3 ITM 1DTE | TTM average size before now (ATR): 2-3 + Trend line color: YOUR WAY strong | 3.1 | 0.23 | 47% | **+1.5%**  | 0.3 | +0.2% (553) |
| 2nd half | PAUSE THEN GO | AT THE SIGNAL | SPY+QQQ ALL CHARTS | OPTION +20% / -10% / 2 ITM 1DTE | REAL VIX vs its 20-day average: normal + Today's gap (daily ATR, + = your way): 0.3+ YOUR way | 4.5 | 0.13 | 45% | **+1.4%**  | 0.5 | -1.6% (3722) |
| 1st half | ANGLE UP THROUGH 23 | AT THE SIGNAL | SPY+QQQ 5m | ANGLE BACK -20 / 2 ITM 2DTE | Lines GLOW (Vix flow + TTM agree): glow YOUR way + A diamond YOUR way in the last 10 candles (either setting): no | 3.0 | 0.20 | 42% | **+1.4%**  | 0.3 | -0.0% (650) |
| 1st half | DIAMOND (YOURS) | WAIT FOR THE LINE CROSS | SPY+QQQ 2m | ANGLE BACK -20 / 3 ITM 0DTE | Against side: points dropped in the last 2 candles: 15-30 + Trade vs the day's move so far: WITH the day | 3.0 | 0.87 | 49% | **+1.4%**  | 0.4 | -3.1% (535) |
| 2nd half | PAUSE THEN GO | AT THE SIGNAL | SPY+QQQ 2m | OPTION +20% / -10% / 1 ITM 2DTE | Lines GLOW (Vix flow + TTM agree): no glow + Day so far: net move / range: trending (60%+) | 3.1 | 0.15 | 42% | **+1.3%**  | 0.5 | -0.9% (1221) |
| 1st half | FEAR / GREED MAXED | WAIT FOR THE LINE CROSS | SPY+QQQ 5m | LINE COLOR / 3 ITM 2DTE | Trade vs the day's move so far: WITH the day + Today's gap (daily ATR, + = your way): no real gap | 2.6 | 0.91 | 45% | **+1.0%**  | 0.4 | +0.0% (627) |
| 2nd half | LINE TURNS YOUR COLOR | AT THE SIGNAL | SPY+QQQ ALL CHARTS | ANGLE BACK -20 / 1 ITM 0DTE | Price vs VWAP (ATR, + = your side): -1 to +1 + REAL VIX vs its 20-day average: normal | 5.9 | 14.57 | 41% | **+0.9%**  | 0.3 | -2.4% (3281) |
| 1st half | DIAMOND (TUNED) | AT THE SIGNAL | SPY+QQQ 3m | OPTION TRAIL 15% / 2 ITM 2DTE | TTM average size before now (ATR): 2-3 + Today's gap (daily ATR, + = your way): no real gap | 2.7 | 0.12 | 33% | **+0.9%**  | 0.3 | -1.2% (375) |
| 1st half | RANDOM | AT THE SIGNAL | SPY+QQQ 3m | LINE COLOR / 3 ITM 0DTE | Day's range so far vs the 20-day average day: 70-100% + Today's gap (daily ATR, + = your way): 0.3+ YOUR way | 3.4 | 1.08 | 48% | **+0.7%**  | 0.2 | +0.7% (364) |
| 1st half | ANGLE UP THROUGH 23 | AT THE SIGNAL | SPY+QQQ 1m | OPTION TRAIL 15% / 3 ITM 2DTE | Today's gap (daily ATR, + = your way): 0.3+ AGAINST you + A diamond AGAINST you in the last 10 candles: no | 3.2 | 0.27 | 40% | **+0.6%**  | 0.2 | -1.7% (2376) |
| 2nd half | TREND LINE CROSS | AT THE SIGNAL | SPY+QQQ 2m | LINE COLOR / 2 ITM 0DTE | Trade vs the day's move so far: WITH the day + Trend paused: angle was 20+ your way, dipped under 5 (last 15 candles): YES | 4.5 | 0.97 | 40% | **+0.5%**  | 0.1 | +1.8% (144) |
| 2nd half | DIAMOND (TUNED) | WAIT FOR THE LINE CROSS | SPY+QQQ ALL CHARTS | ANGLE BACK -20 / 2 ITM 0DTE | REAL VIX today (VIXY vs yesterday): down + REAL VIX vs its 20-day average: HIGH (5%+ over) | 2.7 | 0.76 | 45% | **+0.5%**  | 0.1 | +2.8% (2622) |
| 1st half | GAP & GO | AT THE SIGNAL | SPY+QQQ 3m | OPTION +10% / -20% / 1 OTM 0DTE | Against side MAXED (95+) in the last 10 candles: no + A diamond AGAINST you in the last 10 candles: no | 3.6 | 0.33 | 57% | **+0.5%**  | 0.2 | -5.2% (3629) |
| 1st half | FEAR / GREED MAXED | WAIT FOR THE LINE CROSS | SPY+QQQ ALL CHARTS | LINE COLOR / 2 ITM 0DTE | Trend line color: YOUR WAY strong + Volume vs this time of day (20-day avg): 2.5x+ | 6.2 | 1.43 | 44% | **+0.4%**  | 0.0 | +0.8% (547) |
| 2nd half | FEAR / GREED MAXED | AT THE SIGNAL | SPY+QQQ 3m | LINE COLOR / 1 ITM 0DTE | Trade vs the day's move so far: WITH the day + REAL VIX today (VIXY vs yesterday): down | 3.7 | 2.66 | 37% | **+0.3%**  | 0.1 | -3.7% (1711) |
| 2nd half | LINE TURNS YOUR COLOR | AT THE SIGNAL | SPY+QQQ 1m | ANGLE BACK -20 / 1 OTM 1DTE | Price vs VWAP (ATR, + = your side): -1 to +1 + REAL VIX vs its 20-day average: normal | 4.8 | 5.40 | 39% | **+0.2%**  | 0.1 | -2.3% (1183) |
| 2nd half | GAP & GO | AT THE SIGNAL | SPY+QQQ 3m | OPTION +20% / -10% / 2 ITM 1DTE | Your side: change in the last 2 candles: flat / falling + TTM color: your way, rising | 4.1 | 0.09 | 39% | **+0.2%**  | 0.1 | -1.2% (894) |
| 2nd half | RANDOM | WAIT FOR THE LINE CROSS | SPY+QQQ 3m | ANGLE BACK -20 / 3 ITM 0DTE | Lines GLOW (Vix flow + TTM agree): glow AGAINST you + Trend line angle (+ = your way): +5 to +15 | 4.0 | 0.50 | 49% | **+0.1%**  | 0.0 | +0.1% (168) |
| 1st half | FEAR / GREED MAXED | AT THE SIGNAL | SPY+QQQ 3m | LINE COLOR / 2 ITM 0DTE | Options today: 9:45 straddle vs the last 20 days' move: fair + Chart ATR vs its recent average: wild (1.6x+) | 4.4 | 2.38 | 41% | **+0.1%**  | 0.0 | -1.4% (764) |
| 2nd half | GAP & GO | AT THE SIGNAL | SPY+QQQ 1m | OPTION +10% / -20% / 3 ITM 0DTE | TTM average size before now (ATR): under 1.5 + Volume vs this time of day (20-day avg): below normal | 2.8 | 0.15 | 65% | **+0.1%**  | 0.0 | -1.9% (6956) |
| 1st half | GAP & GO | AT THE SIGNAL | SPY+QQQ 2m | OPTION +5% / -10% / 3 ITM 1DTE | Vix Fix YOUR side now (greed for longs / fear for shorts): 85+ + Your side MAXED (95+) in the last 30 candles: YES | 3.3 | 0.22 | 57% | **-0.0%**  | -0.0 | -0.7% (1113) |
| 1st half | LINE TURNS YOUR COLOR | AT THE SIGNAL | SPY+QQQ 3m | LINE OR STRUCTURE / 1 ITM 0DTE | Price vs VWAP (ATR, + = your side): 1-3 your side + A diamond AGAINST you in the last 10 candles: no | 3.5 | 2.80 | 31% | **-0.1%**  | -0.0 | -2.8% (974) |
| 1st half | GAP & GO | AT THE SIGNAL | SPY+QQQ ALL CHARTS | OPTION +10% / -20% / ATM 0DTE | Vix flow (greed + fear averages): YOUR way + Chart ATR vs its recent average: normal | 6.6 | 0.27 | 57% | **-0.2%**  | -0.1 | -2.2% (3614) |
| 2nd half | DIAMOND (YOURS) | WAIT FOR THE LINE CROSS | SPY+QQQ 3m | 15 MINUTES / 2 ITM 0DTE | Trend line color: GRAY + Price vs trend line (ATR): 1+ your side | 3.0 | 0.20 | 49% | **-0.3%**  | -0.1 | -4.3% (131) |
| 2nd half | RANDOM | WAIT FOR THE LINE CROSS | SPY+QQQ 1m | LINE COLOR / 2 ITM 0DTE | Range of the last 20 candles ($): $0.75-1.50 + REAL VIX vs its 20-day average: HIGH (5%+ over) | 4.4 | 2.74 | 34% | **-0.3%**  | -0.1 | -0.3% (925) |
| 2nd half | ANGLE UP THROUGH 23 | AT THE SIGNAL | SPY+QQQ 5m | 5 MINUTES / 1 ITM 1DTE | Your side: change in the last 2 candles: flat / falling + Today's gap (daily ATR, + = your way): no real gap | 2.9 | 0.21 | 49% | **-0.3%**  | -0.1 | -1.3% (1199) |
| 2nd half | ANGLE FLATTENS THROUGH 23 | AT THE SIGNAL | SPY+QQQ 3m | ANGLE BACK -20 / 3 ITM 2DTE | Vix flow (greed + fear averages): AGAINST you + Trade vs the day's move so far: WITH the day | 3.5 | 0.16 | 43% | **-0.3%**  | -0.1 | -0.3% (593) |
| 2nd half | DIAMOND (YOURS) | AT THE SIGNAL | SPY+QQQ 3m | 15 MINUTES / 1 ITM 0DTE | Price vs trend line (ATR): 1+ your side + Trend line angle (+ = your way): flat -5 to +5 | 3.0 | 0.26 | 44% | **-0.6%**  | -0.2 | -4.7% (124) |
| 1st half | DIAMOND (YOURS) | AT THE SIGNAL | SPY+QQQ 1m | LINE COLOR / 2 ITM 0DTE | Trend line color: YOUR WAY strong + Options today: 9:45 straddle vs the last 20 days' move: CHEAP (under 0.8x) | 2.8 | 0.17 | 45% | **-0.6%**  | -0.1 | -1.3% (908) |
| 2nd half | RANDOM | AT THE SIGNAL | SPY+QQQ 3m | ANGLE BACK -20 / 3 ITM 0DTE | Lines GLOW (Vix flow + TTM agree): glow AGAINST you + Trend line angle (+ = your way): +5 to +15 | 4.1 | 0.53 | 49% | **-0.6%**  | -0.2 | -0.6% (177) |
| 2nd half | DIAMOND (TUNED) | WAIT FOR THE LINE CROSS | SPY+QQQ 1m | OPTION TRAIL 15% / 2 ITM 0DTE | Range of the last 20 candles ($): $0.75-1.50 + Day so far: net move / range: trending (60%+) | 1.9 | 0.54 | 29% | **-0.9%**  | -0.4 | -1.5% (2255) |
| 1st half | RANDOM | AT THE SIGNAL | SPY+QQQ 5m | ANGLE BACK -20 / 3 ITM 0DTE | Options today: 9:45 straddle vs the last 20 days' move: RICH (over 1.2x) + Higher chart (5m, or 15m for 5m) vs its trend line: WITH you | 3.6 | 1.80 | 47% | **-0.9%**  | -0.3 | -0.9% (608) |
| 1st half | LINE TURNS YOUR COLOR | AT THE SIGNAL | SPY+QQQ 2m | LINE COLOR / 1 ITM 0DTE | Your side: change in the last 2 candles: up 15-30 + Distance from the 20-candle extreme behind you ($): $1+ | 3.2 | 1.80 | 33% | **-0.9%**  | -0.3 | -0.5% (490) |
| 2nd half | DIAMOND (TUNED) | AT THE SIGNAL | SPY+QQQ 1m | OPTION TRAIL 15% / 2 ITM 0DTE | Against side Vix LINE COLOR: SURGING (blue greed / red fear) | 2.1 | 0.10 | 32% | **-0.9%**  | -0.2 | -1.1% (1698) |
| 1st half | FEAR / GREED MAXED | AT THE SIGNAL | SPY+QQQ ALL CHARTS | LINE COLOR / 2 ITM 0DTE | REAL VIX today (VIXY vs yesterday): up 0-3% + Chart ATR vs its recent average: wild (1.6x+) | 6.3 | 14.05 | 39% | **-1.0%**  | -0.7 | -0.9% (5308) |
| 1st half | DIAMOND (TUNED) | WAIT FOR THE LINE CROSS | SPY+QQQ ALL CHARTS | LINE COLOR / 1 ITM 0DTE | REAL VIX today (VIXY vs yesterday): up 3%+ + Day's range so far vs the 20-day average day: 40-70% | 2.5 | 0.17 | 29% | **-1.1%**  | -0.2 | +3.2% (586) |
| 1st half | DIAMOND (YOURS) | AT THE SIGNAL | SPY+QQQ 5m | TRAIL STRUCTURE / 1 ITM 0DTE | Distance from the 20-candle extreme behind you ($): $1+ + Volume vs this time of day (20-day avg): below normal | 3.3 | 0.80 | 28% | **-1.1%**  | -0.4 | -2.1% (1227) |
| 1st half | FEAR / GREED MAXED | WAIT FOR THE LINE CROSS | SPY+QQQ 1m | LINE COLOR / 1 ITM 0DTE | REAL VIX today (VIXY vs yesterday): up 0-3% + Today's gap (daily ATR, + = your way): 0.3+ YOUR way | 5.3 | 1.98 | 38% | **-1.1%**  | -0.5 | -3.6% (1267) |
| 1st half | PAUSE THEN GO | AT THE SIGNAL | SPY+QQQ 2m | TRAIL STRUCTURE / 1 ITM 0DTE | Vix flow (greed + fear averages): none + Price vs trend line (ATR): 1+ your side | 2.2 | 0.09 | 34% | **-1.2%**  | -0.3 | -1.2% (389) |
| 1st half | PAUSE THEN GO | AT THE SIGNAL | SPY+QQQ 1m | OPTION +10% / -20% / 2 ITM 1DTE | REAL VIX today (VIXY vs yesterday): up 0-3% + Chart ATR vs its recent average: wild (1.6x+) | 4.2 | 0.13 | 58% | **-1.2%**  | -0.4 | -1.1% (2563) |
| 1st half | DIAMOND (YOURS) | WAIT FOR THE LINE CROSS | SPY+QQQ 1m | LINE COLOR / 1 ITM 0DTE | Trend line color: YOUR WAY strong + Options today: 9:45 straddle vs the last 20 days' move: CHEAP (under 0.8x) | 2.8 | 0.16 | 46% | **-1.2%**  | -0.2 | -1.9% (890) |
| 1st half | RANDOM | WAIT FOR THE LINE CROSS | SPY+QQQ ALL CHARTS | LINE COLOR / 2 ITM 0DTE | Range of the last 20 candles ($): $3+ + Options today: 9:45 straddle vs the last 20 days' move: RICH (over 1.2x) | 5.5 | 9.64 | 39% | **-1.2%**  | -0.6 | -1.2% (3258) |
| 1st half | FEAR / GREED MAXED | AT THE SIGNAL | SPY+QQQ 5m | ANGLE BACK -20 / 3 ITM 0DTE | TTM average size before now (ATR): 3+ + REAL VIX today (VIXY vs yesterday): up 0-3% | 2.8 | 0.23 | 41% | **-1.3%**  | -0.3 | +2.5% (70) |
| 1st half | RANDOM | WAIT FOR THE LINE CROSS | SPY+QQQ 1m | LINE COLOR / 2 ITM 0DTE | Range of the last 20 candles ($): $3+ + Options today: 9:45 straddle vs the last 20 days' move: RICH (over 1.2x) | 3.9 | 2.34 | 38% | **-1.4%**  | -0.5 | -1.4% (790) |
| 2nd half | TREND LINE CROSS | AT THE SIGNAL | SPY+QQQ 5m | ANGLE BACK -20 / 1 OTM 1DTE | REAL VIX vs its 20-day average: normal + Higher chart (5m, or 15m for 5m) vs its trend line: AGAINST you | 3.3 | 5.99 | 39% | **-1.5%**  | -1.0 | -3.0% (788) |
| 1st half | RANDOM | AT THE SIGNAL | SPY+QQQ ALL CHARTS | LINE COLOR / 2 ITM 0DTE | REAL VIX today (VIXY vs yesterday): up 0-3% + Options today: 9:45 straddle vs the last 20 days' move: RICH (over 1.2x) | 5.2 | 13.05 | 37% | **-1.6%**  | -1.0 | -1.6% (4411) |
| 1st half | RANDOM | AT THE SIGNAL | SPY+QQQ 2m | LINE COLOR / 2 ITM 0DTE | Price vs VWAP (ATR, + = your side): 1-3 your side + REAL VIX today (VIXY vs yesterday): up 0-3% | 3.3 | 1.64 | 37% | **-1.7%**  | -0.6 | -1.7% (554) |
| 1st half | GAP & GO | AT THE SIGNAL | SPY+QQQ 1m | OPTION +20% / -10% / 1 OTM 1DTE | TTM color: your way, fading + Day's range so far vs the 20-day average day: under 40% | 3.7 | 0.11 | 33% | **-1.7%**  | -0.6 | -1.5% (568) |
| 1st half | DIAMOND (YOURS) | WAIT FOR THE LINE CROSS | SPY+QQQ ALL CHARTS | LINE COLOR / 2 ITM 0DTE | Trend line color: YOUR WAY strong + Chart ATR vs its recent average: wild (1.6x+) | 2.9 | 0.95 | 38% | **-1.8%**  | -0.5 | -0.7% (4464) |
| 2nd half | DIAMOND (YOURS) | WAIT FOR THE LINE CROSS | SPY+QQQ 1m | ANGLE BACK -20 / 3 ITM 0DTE | Price vs VWAP (ATR, + = your side): -1 to +1 + Today's gap (daily ATR, + = your way): 0.3+ YOUR way | 3.8 | 0.42 | 43% | **-1.9%**  | -0.4 | -4.9% (426) |
| 1st half | DIAMOND (TUNED) | AT THE SIGNAL | SPY+QQQ 5m | 30 MINUTES / 3 ITM 2DTE | Vix Fix AGAINST you now (fear for longs / greed for shorts): 60-85 + Trend line color: AGAINST you strong | 3.1 | 0.18 | 38% | **-2.0%**  | -0.8 | -2.3% (204) |
| 2nd half | DIAMOND (YOURS) | AT THE SIGNAL | SPY+QQQ 2m | OPTION TRAIL 15% / 2 ITM 0DTE | Distance from the 20-candle extreme behind you ($): $0.20-0.50 + Options today: 9:45 straddle vs the last 20 days' move: fair | 2.2 | 1.18 | 29% | **-2.1%**  | -2.0 | -0.6% (880) |
| 1st half | FEAR / GREED MAXED | AT THE SIGNAL | SPY+QQQ 2m | LINE COLOR / 2 ITM 0DTE | REAL VIX today (VIXY vs yesterday): up 0-3% + Chart ATR vs its recent average: wild (1.6x+) | 4.1 | 3.53 | 37% | **-2.1%**  | -1.2 | -2.5% (1394) |
| 1st half | RANDOM | WAIT FOR THE LINE CROSS | SPY+QQQ 2m | LINE COLOR / 2 ITM 0DTE | Vix flow (greed + fear averages): AGAINST you + REAL VIX today (VIXY vs yesterday): up 0-3% | 3.4 | 2.36 | 36% | **-2.3%**  | -1.3 | -2.3% (798) |
| 2nd half | FEAR / GREED MAXED | WAIT FOR THE LINE CROSS | SPY+QQQ 5m | LINE COLOR / ATM 0DTE | Trade vs the day's move so far: WITH the day + Day's range so far vs the 20-day average day: 40-70% | 2.8 | 0.68 | 35% | **-2.8%**  | -0.5 | -2.5% (593) |
| 1st half | DIAMOND (TUNED) | AT THE SIGNAL | SPY+QQQ 1m | LINE COLOR / 2 ITM 0DTE | Against side: points dropped in the last 2 candles: 30+ + Trend line angle (+ = your way): flat -5 to +5 | 2.4 | 0.24 | 37% | **-2.9%**  | -0.7 | +0.8% (412) |
| 1st half | DIAMOND (TUNED) | WAIT FOR THE LINE CROSS | SPY+QQQ 1m | LINE COLOR / ATM 1DTE | REAL VIX vs its 20-day average: normal + Today's gap (daily ATR, + = your way): 0.3+ AGAINST you | 2.5 | 0.58 | 33% | **-2.9%**  | -3.2 | -1.6% (1852) |
| 2nd half | DIAMOND (TUNED) | AT THE SIGNAL | SPY+QQQ 2m | ANGLE BACK -20 / 1 ITM 0DTE | Vix Fix YOUR side now (greed for longs / fear for shorts): 10-35 + Candles closed on your side of the trend line in a row: 0 (wrong side) | 2.6 | 0.66 | 43% | **-3.0%**  | -0.6 | -2.1% (2399) |
| 2nd half | LINE TURNS YOUR COLOR | AT THE SIGNAL | SPY+QQQ 3m | LINE COLOR / 1 ITM 0DTE | Your side Vix LINE COLOR: FADING (purple greed / orange fear) + Vix flow (greed + fear averages): AGAINST you | 3.5 | 0.23 | 31% | **-3.0%**  | -0.5 | -5.3% (246) |
| 2nd half | DIAMOND (TUNED) | WAIT FOR THE LINE CROSS | SPY+QQQ 5m | ANGLE BACK -20 / 3 ITM 0DTE | Against side: points dropped in the last 2 candles: 5-15 + Trend line color: AGAINST you strong | 2.4 | 0.20 | 44% | **-3.1%**  | -0.4 | -1.6% (160) |
| 1st half | DIAMOND (TUNED) | WAIT FOR THE LINE CROSS | SPY+QQQ 5m | 30 MINUTES / 3 ITM 2DTE | Chart ATR vs its recent average: normal | 1.9 | 0.11 | 31% | **-3.1%**  | -1.1 | -0.5% (595) |
| 1st half | LINE TURNS YOUR COLOR | AT THE SIGNAL | SPY+QQQ 5m | LINE COLOR / 1 ITM 0DTE | Vix Fix YOUR side now (greed for longs / fear for shorts): 10-35 + REAL VIX today (VIXY vs yesterday): down | 3.9 | 0.80 | 31% | **-3.1%**  | -0.7 | -2.1% (702) |
| 1st half | DIAMOND (YOURS) | AT THE SIGNAL | SPY+QQQ 3m | LINE COLOR / 2 ITM 0DTE | Vix Fix YOUR side now (greed for longs / fear for shorts): 10-35 + Against side Vix LINE COLOR: DROPPING FAST (yellow) | 3.1 | 0.36 | 35% | **-3.3%**  | -1.0 | -8.1% (65) |
| 1st half | TREND LINE CROSS | AT THE SIGNAL | SPY+QQQ 5m | LINE BREAK / 1 ITM 0DTE | Trend line color: YOUR WAY strong + Chart ATR vs its recent average: wild (1.6x+) | 2.5 | 2.79 | 26% | **-3.5%**  | -1.7 | +2.3% (429) |
| 2nd half | DIAMOND (YOURS) | WAIT FOR THE LINE CROSS | SPY+QQQ 5m | LINE COLOR / 3 ITM 0DTE | Your side: change in the last 2 candles: up 5-15 + Chart ATR vs its recent average: normal | 2.3 | 0.16 | 42% | **-3.6%**  | -1.3 | -3.4% (134) |
| 2nd half | DIAMOND (TUNED) | AT THE SIGNAL | SPY+QQQ 3m | OPTION +20% / -10% / 3 ITM 2DTE | Vix flow (greed + fear averages): YOUR way + Day's range so far vs the 20-day average day: 70-100% | 1.8 | 0.10 | 32% | **-3.6%**  | -1.4 | -0.8% (271) |
| 2nd half | GAP & GO | AT THE SIGNAL | SPY+QQQ 2m | OPTION +10% / -20% / 2 ITM 0DTE | TTM color: your way, rising + REAL VIX today (VIXY vs yesterday): down | 3.9 | 0.14 | 54% | **-3.7%**  | -1.2 | -0.2% (1322) |
| 1st half | DIAMOND (TUNED) | AT THE SIGNAL | SPY+QQQ ALL CHARTS | LINE COLOR / 2 ITM 0DTE | Your side MAXED (95+) in the last 30 candles: no + Distance from the 20-candle extreme behind you ($): $1+ | 2.5 | 1.27 | 36% | **-3.7%**  | -1.9 | -2.1% (4206) |
| 2nd half | ANGLE UP THROUGH 23 | AT THE SIGNAL | SPY+QQQ 3m | OPTION +10% / -20% / 3 ITM 2DTE | Vix flow (greed + fear averages): YOUR way + Today's gap (daily ATR, + = your way): no real gap | 4.2 | 0.20 | 46% | **-3.8%**  | -1.5 | -1.4% (677) |
| 2nd half | DIAMOND (TUNED) | WAIT FOR THE LINE CROSS | SPY+QQQ 3m | 15 MINUTES / 2 ITM 2DTE | Your side: change in the last 2 candles: up 30+ + REAL VIX today (VIXY vs yesterday): down | 2.5 | 0.12 | 41% | **-3.8%**  | -1.3 | -2.8% (103) |
| 2nd half | DIAMOND (YOURS) | WAIT FOR THE LINE CROSS | SPY+QQQ ALL CHARTS | ANGLE BACK -20 / 2 ITM 0DTE | TTM average size before now (ATR): under 1.5 + Today's gap (daily ATR, + = your way): 0.3+ YOUR way | 3.3 | 1.25 | 44% | **-3.9%**  | -1.2 | -0.6% (4225) |
| 1st half | DIAMOND (YOURS) | AT THE SIGNAL | SPY+QQQ ALL CHARTS | LINE COLOR / 2 ITM 0DTE | Price vs VWAP (ATR, + = your side): 3+ your side + Chart ATR vs its recent average: wild (1.6x+) | 2.8 | 0.73 | 42% | **-4.0%**  | -0.7 | -1.5% (2251) |
| 1st half | LINE TURNS YOUR COLOR | AT THE SIGNAL | SPY+QQQ ALL CHARTS | LINE COLOR / 1 ITM 0DTE | REAL VIX vs its 20-day average: normal + Today's gap (daily ATR, + = your way): 0.3+ AGAINST you | 6.1 | 5.44 | 26% | **-4.2%**  | -0.9 | -3.4% (4374) |
| 1st half | DIAMOND (YOURS) | WAIT FOR THE LINE CROSS | SPY+QQQ 5m | OPTION +10% / -20% / 2 ITM 0DTE | REAL VIX vs its 20-day average: HIGH (5%+ over) + Day's range so far vs the 20-day average day: 70-100% | 4.6 | 0.07 | 54% | **-4.2%**  | -1.3 | +4.2% (80) |
| 1st half | LINE TURNS YOUR COLOR | AT THE SIGNAL | SPY+QQQ 1m | LINE COLOR / 1 ITM 0DTE | Options today: 9:45 straddle vs the last 20 days' move: RICH (over 1.2x) + Today's gap (daily ATR, + = your way): 0.3+ AGAINST you | 3.3 | 2.10 | 25% | **-4.9%**  | -1.2 | -2.0% (1807) |
| 2nd half | DIAMOND (YOURS) | AT THE SIGNAL | SPY+QQQ 1m | ANGLE BACK -20 / 2 ITM 0DTE | TTM color: against you, still pushing + Distance from the 20-candle extreme behind you ($): under $0.20 | 4.1 | 0.12 | 39% | **-5.3%**  | -0.8 | -3.6% (2737) |
| 2nd half | DIAMOND (TUNED) | WAIT FOR THE LINE CROSS | SPY+QQQ 2m | ANGLE BACK -20 / 1 ITM 0DTE | Vix Fix YOUR side now (greed for longs / fear for shorts): 10-35 + Trend line color: AGAINST you strong | 2.7 | 0.60 | 34% | **-5.5%**  | -1.0 | +1.4% (1151) |
| 2nd half | DIAMOND (YOURS) | WAIT FOR THE LINE CROSS | SPY+QQQ 2m | 30 MINUTES / 1 ITM 0DTE | REAL VIX today (VIXY vs yesterday): up 0-3% + Day's range so far vs the 20-day average day: already a full day+ | 3.2 | 0.30 | 39% | **-5.5%**  | -1.1 | +0.8% (363) |
| 1st half | DIAMOND (YOURS) | WAIT FOR THE LINE CROSS | SPY+QQQ 3m | LINE OR STRUCTURE / 1 ITM 0DTE | Range of the last 20 candles ($): $1.50-3 + Day's range so far vs the 20-day average day: already a full day+ | 2.4 | 0.18 | 26% | **-5.6%**  | -1.9 | -3.7% (342) |
| 1st half | PAUSE THEN GO | AT THE SIGNAL | SPY+QQQ ALL CHARTS | OPTION +20% / -10% / 1 ITM 0DTE | Day's range so far vs the 20-day average day: 70-100% + Volume vs this time of day (20-day avg): 1-2.5x | 2.7 | 0.14 | 34% | **-6.1%**  | -2.1 | -1.2% (3145) |
| 1st half | DIAMOND (TUNED) | WAIT FOR THE LINE CROSS | SPY+QQQ 2m | OPTION +10% / -10% / 1 ITM 0DTE | Vix Fix AGAINST you now (fear for longs / greed for shorts): 60-85 + REAL VIX vs its 20-day average: HIGH (5%+ over) | 3.9 | 0.12 | 32% | **-6.3%**  | -2.1 | -1.9% (134) |
| 2nd half | ANGLE UP THROUGH 23 | AT THE SIGNAL | SPY+QQQ ALL CHARTS | ANGLE BACK -20 / 3 ITM 1DTE | REAL VIX today (VIXY vs yesterday): down + Options today: 9:45 straddle vs the last 20 days' move: unknown | 5.4 | 0.34 | 37% | **-6.3%**  | -1.4 | -1.6% (1590) |
| 2nd half | ANGLE UP THROUGH 23 | AT THE SIGNAL | SPY+QQQ 2m | ANGLE BACK -20 / 3 ITM 1DTE | REAL VIX today (VIXY vs yesterday): down + Options today: 9:45 straddle vs the last 20 days' move: unknown | 3.0 | 0.11 | 35% | **-6.3%**  | -1.1 | +1.2% (385) |
| 2nd half | FEAR / GREED MAXED | AT THE SIGNAL | SPY+QQQ 5m | LINE COLOR / 2 ITM 0DTE | Trend line angle (+ = your way): +5 to +15 + Day so far: net move / range: 30-60% | 3.4 | 0.19 | 35% | **-7.2%**  | -0.9 | -2.6% (282) |
| 1st half | FEAR / GREED MAXED | WAIT FOR THE LINE CROSS | SPY+QQQ 2m | LINE COLOR / 2 ITM 0DTE | Your side MAXED (95+) in the last 30 candles: no + Trend line color: YOUR WAY strong | 4.1 | 0.26 | 32% | **-7.3%**  | -1.1 | -2.0% (1092) |
| 2nd half | PAUSE THEN GO | AT THE SIGNAL | SPY+QQQ 3m | OPTION +10% / -20% / 3 ITM 2DTE | Price vs trend line (ATR): 1+ your side + Trend line angle (+ = your way): +5 to +15 | 2.0 | 0.17 | 43% | **-7.8%**  | -3.2 | -0.7% (492) |
| 2nd half | PAUSE THEN GO | AT THE SIGNAL | SPY+QQQ 1m | ANGLE BACK -20 / 3 ITM 0DTE | Volume vs this time of day (20-day avg): below normal + Candles closed on your side of the trend line in a row: 6-15 | 3.0 | 0.15 | 44% | **-7.9%**  | -1.2 | -2.7% (1702) |
| 1st half | DIAMOND (TUNED) | AT THE SIGNAL | SPY+QQQ 2m | 30 MINUTES / 1 ITM 0DTE | REAL VIX today (VIXY vs yesterday): up 3%+ + REAL VIX vs its 20-day average: HIGH (5%+ over) | 3.0 | 0.10 | 40% | **-8.1%**  | -1.2 | -3.1% (386) |
| 1st half | DIAMOND (TUNED) | WAIT FOR THE LINE CROSS | SPY+QQQ 3m | LINE BREAK / 2 ITM 0DTE | Day so far: net move / range: trending (60%+) + REAL VIX vs its 20-day average: normal | 1.9 | 0.18 | 18% | **-8.6%**  | -4.0 | -0.5% (822) |
| 2nd half | LINE TURNS YOUR COLOR | AT THE SIGNAL | SPY+QQQ 2m | ANGLE BACK -20 / 1 ITM 0DTE | REAL VIX vs its 20-day average: normal + Today's gap (daily ATR, + = your way): 0.3+ YOUR way | 3.6 | 1.27 | 39% | **-9.2%**  | -1.8 | -3.8% (989) |
| 2nd half | DIAMOND (YOURS) | AT THE SIGNAL | SPY+QQQ ALL CHARTS | ANGLE BACK -20 / 2 ITM 0DTE | Vix Fix YOUR side now (greed for longs / fear for shorts): 10-35 + TTM color: against you, still pushing | 4.4 | 0.25 | 36% | **-9.5%**  | -2.0 | -1.9% (5926) |
| 2nd half | TREND LINE CROSS | AT THE SIGNAL | SPY+QQQ 1m | LINE COLOR / 2 ITM 0DTE | Options today: 9:45 straddle vs the last 20 days' move: unknown + Day's range so far vs the 20-day average day: already a full day+ | 4.6 | 1.07 | 31% | **-9.7%**  | -2.5 | -8.5% (232) |
| 1st half | RANDOM | AT THE SIGNAL | SPY+QQQ 1m | LINE COLOR / 2 ITM 0DTE | REAL VIX today (VIXY vs yesterday): up 3%+ + REAL VIX vs its 20-day average: LOW (5%+ under) | 3.8 | 0.08 | 35% | **-10.7%**  | -0.7 | -10.7% (26) |
| 2nd half | TREND LINE CROSS | AT THE SIGNAL | SPY+QQQ ALL CHARTS | LINE COLOR / 2 ITM 0DTE | Options today: 9:45 straddle vs the last 20 days' move: unknown + Day's range so far vs the 20-day average day: already a full day+ | 6.9 | 2.20 | 30% | **-12.0%**  | -3.2 | -9.3% (445) |
| 1st half | PAUSE THEN GO | AT THE SIGNAL | SPY+QQQ 3m | LINE COLOR / 1 OTM 0DTE | Your side MAXED (95+) in the last 30 candles: YES + Lines GLOW (Vix flow + TTM agree): no glow | 0.0 | 0.10 | 29% | **-12.6%**  | -1.0 | -0.6% (1094) |
| 2nd half | FEAR / GREED MAXED | WAIT FOR THE LINE CROSS | SPY+QQQ 2m | LINE COLOR / 2 ITM 0DTE | Trend line color: GRAY + Trend paused: angle was 20+ your way, dipped under 5 (last 15 candles): YES | 4.5 | 0.18 | 23% | **-12.9%**  | -3.3 | +3.2% (27) |
| 2nd half | TREND LINE CROSS | AT THE SIGNAL | SPY+QQQ 3m | ANGLE BACK -20 / 1 OTM 1DTE | Today's gap (daily ATR, + = your way): 0.3+ YOUR way + Trend paused: angle was 20+ your way, dipped under 5 (last 15 candles): YES | 3.8 | 0.16 | 35% | **-14.1%**  | -2.0 | -14.1% (26) |

## 7. THE STACK - one scalp book from every setup that cleared the bar on one half, traded on the half it never saw
Each setup keeps its own trade and filter (picked on the build half: the fewest helping readings that gave +2% (or +3%) with t 2.5). One trade at a time per ticker: a signal is skipped while that ticker's last trade is still open.
| Built on | Book | Setups | Trades | Trades/day | Win % | Avg | Avg win / loss | t | Kelly | Growth / trade | Biggest parts |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1st half | STACK +2% | 9 | 1961 | 5.80 | 35% | **-0.0%** | +39% / -21% | -0.0 | 0% | +0.00% | LINE TURNS YOUR COLOR / AT THE SIGNAL / SPY+QQQ 3m (1283); FEAR / GREED MAXED / AT THE SIGNAL / SPY+QQQ 2m (160); GAP & GO / AT THE SIGNAL / SPY+QQQ 1m (120); DIAMOND (TUNED) / WAIT FOR THE LINE CROSS / SPY+QQQ 2m (99); ANGLE UP THROUGH 23 / AT THE SIGNAL / SPY+QQQ 1m (98); DIAMOND (TUNED) / AT THE SIGNAL / SPY+QQQ 2m (92); ANGLE FLATTENS THROUGH 23 / AT THE SIGNAL / SPY+QQQ 2m (59); ANGLE FLATTENS THROUGH 23 / AT THE SIGNAL / SPY+QQQ 3m (35); ANGLE FLATTENS THROUGH 23 / AT THE SIGNAL / SPY+QQQ 5m (15) |
| 1st half | STACK +3% | 9 | 1961 | 5.80 | 35% | **-0.0%** | +39% / -21% | -0.0 | 0% | +0.00% | LINE TURNS YOUR COLOR / AT THE SIGNAL / SPY+QQQ 3m (1283); FEAR / GREED MAXED / AT THE SIGNAL / SPY+QQQ 2m (160); GAP & GO / AT THE SIGNAL / SPY+QQQ 1m (120); DIAMOND (TUNED) / WAIT FOR THE LINE CROSS / SPY+QQQ 2m (99); ANGLE UP THROUGH 23 / AT THE SIGNAL / SPY+QQQ 1m (98); DIAMOND (TUNED) / AT THE SIGNAL / SPY+QQQ 2m (92); ANGLE FLATTENS THROUGH 23 / AT THE SIGNAL / SPY+QQQ 2m (59); ANGLE FLATTENS THROUGH 23 / AT THE SIGNAL / SPY+QQQ 3m (35); ANGLE FLATTENS THROUGH 23 / AT THE SIGNAL / SPY+QQQ 5m (15) |
| 2nd half | STACK +2% | 6 | 744 | 2.21 | 40% | **+1.7%** | +47% / -29% | 0.7 | 5% | +0.04% | FEAR / GREED MAXED / AT THE SIGNAL / SPY+QQQ 3m (457); DIAMOND (YOURS) / WAIT FOR THE LINE CROSS / SPY+QQQ 3m (130); DIAMOND (TUNED) / AT THE SIGNAL / SPY+QQQ 5m (58); FEAR / GREED MAXED / AT THE SIGNAL / SPY+QQQ 5m (39); ANGLE UP THROUGH 23 / AT THE SIGNAL / SPY+QQQ 5m (34); DIAMOND (YOURS) / AT THE SIGNAL / SPY+QQQ 1m (26) |
| 2nd half | STACK +3% | 6 | 744 | 2.21 | 40% | **+1.7%** | +47% / -29% | 0.7 | 5% | +0.04% | FEAR / GREED MAXED / AT THE SIGNAL / SPY+QQQ 3m (457); DIAMOND (YOURS) / WAIT FOR THE LINE CROSS / SPY+QQQ 3m (130); DIAMOND (TUNED) / AT THE SIGNAL / SPY+QQQ 5m (58); FEAR / GREED MAXED / AT THE SIGNAL / SPY+QQQ 5m (39); ANGLE UP THROUGH 23 / AT THE SIGNAL / SPY+QQQ 5m (34); DIAMOND (YOURS) / AT THE SIGNAL / SPY+QQQ 1m (26) |

**Luck check:** tens of thousands of trades and filters are scored. Sections 2-4 are the whole sample (some will look good by chance). Sections 5-7 are BLIND: picked on one half, judged on the other - those are the ones that count. Kelly near 100% comes from small average losses and is not a size to use.

