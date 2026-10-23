# DIAMOND OPTIONS LAB - EVERY DIAMOND ON REAL OPTION PRICES - SPY, QQQ - 2024-02-15 to now - 2026-10-23 08:48 ET
Runtime 16 min. Diamond entries: 77,283 (both books, 1m, 2m, 3m, 5m, both entry types). Option prices = Alpaca OPRA 1-minute bars: 49,113 of 49,197 contract-days found. DATA ONLY.
**Each trade** buys the option at the close of the signal minute (+ cost) and sells at the exit minute's close (- cost). **Cost** = $0.01 or 0.5% of the price per side, whichever is bigger. Entries 9:45-14:30, everything out by 15:55, max 120 minutes. **Return** = % on the premium paid.
**Kelly** = the share of the ACCOUNT to put into premium per trade that grows it fastest (exact, from the trades' returns). **Growth/trade** = the typical account growth per trade at full Kelly (half Kelly keeps ~75% of it with half the swings). 0 = no edge: any size loses.
**Strikes:** ATM = nearest strike; 1-2 ITM / OTM = $1 strikes in / out of the money. **0DTE** = expires today, **1DTE** = the next trading day's expiration (still closed the same day).

**Exits:**
- **LINE BREAK** - ride until a candle closes back through the trend line (armed once a candle closed on your side)
- **LINE COLOR** - ride until the trend line turns the other color (red / pink for longs, green / blue for shorts)
- **STRUCTURE** - stop $0.05 past the last 10 candles' low (longs) / high (shorts), checked every minute
- **LINE OR STRUCTURE** - whichever comes first: line break or the structure stop
- **TRAIL STRUCTURE** - structure stop that trails: each closed candle moves it to the last 3 candles' low / high
- **OPPOSITE DIAMOND** - ride until the opposite diamond on the same chart
- **OPTION +10% / -10%** - the option itself: out at +10% or -10% (1-minute closes)
- **OPTION TRAIL 15%** - the option itself: out when it falls 15% from its best, or -10% from entry
- **Entries:** AT THE DIAMOND = right after the diamond candle closes. TREND LINE CROSS = wait (up to 10 candles) for the first candle that closes on your side of the trend line.

## 1. ARE 0DTE / 1DTE OPTIONS CHEAP OR RICH? (9:45 at-the-money straddle, held to 15:55)
Straddle P&L = what the call + put are worth at 15:55 vs what they cost at 9:45 (no costs). Negative = buyers overpay.
| Group | Expiration | Days | Straddle cost | Real move 9:45-15:55 | Straddle P&L (avg) | Days it made money |
|---|---|---|---|---|---|---|
| all days | 0DTE | 1318 | $3.57 | $3.29 | **-3.4%** | 37% |
| VIX LOW (5%+ under) | 0DTE | 518 | $3.04 | $2.57 | **-10.2%** | 34% |
| VIX normal | 0DTE | 593 | $3.53 | $3.31 | **+0.3%** | 37% |
| VIX HIGH (5%+ over) | 0DTE | 207 | $5.04 | $5.01 | **+3.4%** | 43% |
| VIX today down | 0DTE | 728 | $3.39 | $3.20 | **-4.6%** | 36% |
| VIX today up 0-3% | 0DTE | 472 | $3.53 | $3.16 | **-1.6%** | 38% |
| VIX today up 3%+ | 0DTE | 118 | $4.87 | $4.37 | **-2.4%** | 41% |
| all days | 1DTE | 1312 | $5.99 | $3.22 | **-2.1%** | 31% |
| VIX LOW (5%+ under) | 1DTE | 521 | $5.16 | $2.60 | **-4.6%** | 27% |
| VIX normal | 1DTE | 584 | $5.93 | $3.24 | **-0.6%** | 32% |
| VIX HIGH (5%+ over) | 1DTE | 207 | $8.22 | $4.74 | **+0.1%** | 35% |
| VIX today down | 1DTE | 726 | $5.65 | $3.09 | **-2.6%** | 29% |
| VIX today up 0-3% | 1DTE | 466 | $5.96 | $3.07 | **-2.1%** | 30% |
| VIX today up 3%+ | 1DTE | 120 | $8.13 | $4.61 | **+1.3%** | 41% |

## 2. 0DTE vs 1DTE, EVERY STRIKE - average return per trade (all charts together, entry at the diamond)
Each cell: avg return on premium (Kelly %). Kelly 0 = no edge.

### YOUR SETTINGS - AT THE DIAMOND
| Exit | 2 ITM 0DTE | 1 ITM 0DTE | ATM 0DTE | 1 OTM 0DTE | 2 OTM 0DTE | 2 ITM 1DTE | 1 ITM 1DTE | ATM 1DTE | 1 OTM 1DTE | 2 OTM 1DTE |
|---|---|---|---|---|---|---|---|---|---|---|
| LINE BREAK | -0.9% (0%) | -1.8% (0%) | -3.1% (0%) | -5.4% (0%) | -8.9% (0%) | -0.1% (0%) | -0.8% (0%) | -1.3% (0%) | -1.5% (0%) | -1.7% (0%) |
| LINE COLOR | -1.0% (0%) | -1.4% (0%) | -2.6% (0%) | -4.9% (0%) | -8.4% (0%) | -0.7% (0%) | -1.0% (0%) | -1.0% (0%) | -1.2% (0%) | -1.4% (0%) |
| STRUCTURE | -2.7% (0%) | -2.8% (0%) | -4.0% (0%) | -6.9% (0%) | -10.6% (0%) | -1.9% (0%) | -2.0% (0%) | -1.9% (0%) | -2.0% (0%) | -2.3% (0%) |
| LINE OR STRUCTURE | -0.9% (0%) | -1.7% (0%) | -2.8% (0%) | -4.9% (0%) | -8.3% (0%) | -0.1% (0%) | -0.8% (0%) | -1.2% (0%) | -1.4% (0%) | -1.6% (0%) |
| TRAIL STRUCTURE | -1.4% (0%) | -2.0% (0%) | -3.0% (0%) | -5.1% (0%) | -8.5% (0%) | -0.4% (0%) | -1.2% (0%) | -1.5% (0%) | -1.7% (0%) | -2.0% (0%) |
| OPPOSITE DIAMOND | -2.7% (0%) | -3.7% (0%) | -5.8% (0%) | -9.0% (0%) | -13.3% (0%) | -1.7% (0%) | -2.1% (0%) | -2.4% (0%) | -2.7% (0%) | -3.2% (0%) |
| OPTION +10% / -10% | -1.4% (0%) | -1.7% (0%) | -2.4% (0%) | -4.3% (0%) | -7.5% (0%) | -1.2% (0%) | -1.4% (0%) | -1.6% (0%) | -1.8% (0%) | -2.1% (0%) |
| OPTION TRAIL 15% | -1.9% (0%) | -2.3% (0%) | -3.1% (0%) | -5.1% (0%) | -8.7% (0%) | -1.9% (0%) | -1.9% (0%) | -2.0% (0%) | -2.1% (0%) | -2.5% (0%) |

### YOUR SETTINGS - TREND LINE CROSS
| Exit | 2 ITM 0DTE | 1 ITM 0DTE | ATM 0DTE | 1 OTM 0DTE | 2 OTM 0DTE | 2 ITM 1DTE | 1 ITM 1DTE | ATM 1DTE | 1 OTM 1DTE | 2 OTM 1DTE |
|---|---|---|---|---|---|---|---|---|---|---|
| LINE BREAK | -0.1% (0%) | -1.1% (0%) | -2.1% (0%) | -4.1% (0%) | -7.2% (0%) | +0.5% (32%) | -0.4% (0%) | -0.9% (0%) | -1.0% (0%) | -1.1% (0%) |
| LINE COLOR | -0.8% (0%) | -1.5% (0%) | -2.7% (0%) | -5.1% (0%) | -8.6% (0%) | -0.4% (0%) | -0.9% (0%) | -1.0% (0%) | -1.2% (0%) | -1.4% (0%) |
| STRUCTURE | -2.2% (0%) | -2.4% (0%) | -3.7% (0%) | -6.5% (0%) | -10.1% (0%) | -1.5% (0%) | -1.7% (0%) | -1.7% (0%) | -1.9% (0%) | -2.1% (0%) |
| LINE OR STRUCTURE | -0.1% (0%) | -1.1% (0%) | -2.1% (0%) | -4.1% (0%) | -7.2% (0%) | +0.5% (32%) | -0.4% (0%) | -0.9% (0%) | -1.0% (0%) | -1.1% (0%) |
| TRAIL STRUCTURE | -0.8% (0%) | -1.7% (0%) | -2.6% (0%) | -4.6% (0%) | -7.9% (0%) | +0.1% (6%) | -0.9% (0%) | -1.3% (0%) | -1.5% (0%) | -1.7% (0%) |
| OPPOSITE DIAMOND | -2.0% (0%) | -3.1% (0%) | -4.9% (0%) | -7.8% (0%) | -11.6% (0%) | -1.1% (0%) | -1.7% (0%) | -2.0% (0%) | -2.3% (0%) | -2.7% (0%) |
| OPTION +10% / -10% | -1.0% (0%) | -1.6% (0%) | -2.4% (0%) | -4.3% (0%) | -7.3% (0%) | -0.8% (0%) | -1.3% (0%) | -1.5% (0%) | -1.6% (0%) | -1.8% (0%) |
| OPTION TRAIL 15% | -1.6% (0%) | -2.1% (0%) | -2.8% (0%) | -4.7% (0%) | -8.4% (0%) | -1.4% (0%) | -1.6% (0%) | -1.7% (0%) | -1.9% (0%) | -2.1% (0%) |

### 1m TUNED - AT THE DIAMOND
| Exit | 2 ITM 0DTE | 1 ITM 0DTE | ATM 0DTE | 1 OTM 0DTE | 2 OTM 0DTE | 2 ITM 1DTE | 1 ITM 1DTE | ATM 1DTE | 1 OTM 1DTE | 2 OTM 1DTE |
|---|---|---|---|---|---|---|---|---|---|---|
| LINE BREAK | -0.3% (0%) | -1.3% (0%) | -2.4% (0%) | -4.5% (0%) | -7.5% (0%) | +0.5% (20%) | -0.5% (0%) | -1.0% (0%) | -1.1% (0%) | -1.3% (0%) |
| LINE COLOR | -1.0% (0%) | -1.6% (0%) | -2.5% (0%) | -4.3% (0%) | -7.5% (0%) | -0.6% (0%) | -0.9% (0%) | -1.2% (0%) | -1.2% (0%) | -1.4% (0%) |
| STRUCTURE | -2.5% (0%) | -2.7% (0%) | -3.6% (0%) | -6.6% (0%) | -10.5% (0%) | -1.5% (0%) | -1.7% (0%) | -1.8% (0%) | -1.8% (0%) | -2.1% (0%) |
| LINE OR STRUCTURE | -0.5% (0%) | -1.3% (0%) | -2.3% (0%) | -4.2% (0%) | -7.2% (0%) | +0.3% (18%) | -0.6% (0%) | -1.0% (0%) | -1.2% (0%) | -1.4% (0%) |
| TRAIL STRUCTURE | -0.9% (0%) | -1.6% (0%) | -2.5% (0%) | -4.7% (0%) | -7.7% (0%) | +0.1% (8%) | -0.9% (0%) | -1.2% (0%) | -1.4% (0%) | -1.6% (0%) |
| OPPOSITE DIAMOND | -3.4% (0%) | -4.5% (0%) | -6.9% (0%) | -11.4% (0%) | -16.5% (0%) | -2.1% (0%) | -2.6% (0%) | -2.7% (0%) | -3.0% (0%) | -3.5% (0%) |
| OPTION +10% / -10% | -1.1% (0%) | -1.4% (0%) | -2.2% (0%) | -3.8% (0%) | -6.9% (0%) | -0.8% (0%) | -1.1% (0%) | -1.5% (0%) | -1.6% (0%) | -1.9% (0%) |
| OPTION TRAIL 15% | -1.7% (0%) | -2.2% (0%) | -2.5% (0%) | -4.3% (0%) | -7.6% (0%) | -1.4% (0%) | -1.6% (0%) | -2.0% (0%) | -2.1% (0%) | -2.5% (0%) |

### 1m TUNED - TREND LINE CROSS
| Exit | 2 ITM 0DTE | 1 ITM 0DTE | ATM 0DTE | 1 OTM 0DTE | 2 OTM 0DTE | 2 ITM 1DTE | 1 ITM 1DTE | ATM 1DTE | 1 OTM 1DTE | 2 OTM 1DTE |
|---|---|---|---|---|---|---|---|---|---|---|
| LINE BREAK | -0.1% (0%) | -1.1% (0%) | -2.0% (0%) | -3.8% (0%) | -6.6% (0%) | +0.8% (46%) | -0.3% (0%) | -0.9% (0%) | -1.0% (0%) | -1.1% (0%) |
| LINE COLOR | -1.0% (0%) | -1.8% (0%) | -2.6% (0%) | -4.7% (0%) | -8.0% (0%) | -0.4% (0%) | -0.9% (0%) | -1.2% (0%) | -1.3% (0%) | -1.4% (0%) |
| STRUCTURE | -2.2% (0%) | -2.3% (0%) | -3.4% (0%) | -6.5% (0%) | -10.1% (0%) | -1.3% (0%) | -1.4% (0%) | -1.7% (0%) | -1.6% (0%) | -1.9% (0%) |
| LINE OR STRUCTURE | -0.1% (0%) | -1.1% (0%) | -1.9% (0%) | -3.8% (0%) | -6.6% (0%) | +0.8% (46%) | -0.3% (0%) | -0.8% (0%) | -1.0% (0%) | -1.1% (0%) |
| TRAIL STRUCTURE | -0.7% (0%) | -1.6% (0%) | -2.4% (0%) | -4.6% (0%) | -7.8% (0%) | +0.4% (20%) | -0.8% (0%) | -1.2% (0%) | -1.3% (0%) | -1.5% (0%) |
| OPPOSITE DIAMOND | -3.2% (0%) | -4.2% (0%) | -6.6% (0%) | -11.0% (0%) | -15.6% (0%) | -1.9% (0%) | -2.3% (0%) | -2.6% (0%) | -2.8% (0%) | -3.3% (0%) |
| OPTION +10% / -10% | -1.0% (0%) | -1.6% (0%) | -2.2% (0%) | -4.0% (0%) | -6.9% (0%) | -0.5% (0%) | -1.0% (0%) | -1.4% (0%) | -1.6% (0%) | -1.7% (0%) |
| OPTION TRAIL 15% | -1.5% (0%) | -2.0% (0%) | -2.5% (0%) | -4.4% (0%) | -7.5% (0%) | -0.9% (0%) | -1.3% (0%) | -1.7% (0%) | -2.0% (0%) | -2.2% (0%) |

### RANDOM - AT THE DIAMOND (the bar to beat: random candles, random side, same exits)
| Exit | 2 ITM 0DTE | 1 ITM 0DTE | ATM 0DTE | 1 OTM 0DTE | 2 OTM 0DTE | 2 ITM 1DTE | 1 ITM 1DTE | ATM 1DTE | 1 OTM 1DTE | 2 OTM 1DTE |
|---|---|---|---|---|---|---|---|---|---|---|
| LINE BREAK | -1.1% (0%) | -2.0% (0%) | -3.2% (0%) | -5.6% (0%) | -9.1% (0%) | -0.6% (0%) | -1.0% (0%) | -1.3% (0%) | -1.5% (0%) | -1.7% (0%) |
| LINE COLOR | -0.9% (0%) | -1.3% (0%) | -2.4% (0%) | -4.9% (0%) | -8.8% (0%) | -0.9% (0%) | -0.9% (0%) | -0.8% (0%) | -0.9% (0%) | -1.1% (0%) |
| STRUCTURE | -1.9% (0%) | -2.0% (0%) | -3.0% (0%) | -5.6% (0%) | -9.2% (0%) | -1.3% (0%) | -1.4% (0%) | -1.2% (0%) | -1.3% (0%) | -1.6% (0%) |
| LINE OR STRUCTURE | -1.1% (0%) | -1.8% (0%) | -2.9% (0%) | -5.0% (0%) | -8.4% (0%) | -0.6% (0%) | -1.0% (0%) | -1.3% (0%) | -1.5% (0%) | -1.7% (0%) |
| TRAIL STRUCTURE | -1.3% (0%) | -1.8% (0%) | -2.8% (0%) | -4.9% (0%) | -8.3% (0%) | -0.7% (0%) | -1.2% (0%) | -1.4% (0%) | -1.5% (0%) | -1.9% (0%) |
| OPPOSITE DIAMOND | -3.0% (0%) | -3.7% (0%) | -5.5% (0%) | -8.9% (0%) | -13.3% (0%) | -2.3% (0%) | -2.1% (0%) | -2.0% (0%) | -2.3% (0%) | -2.7% (0%) |
| OPTION +10% / -10% | -1.2% (0%) | -1.5% (0%) | -2.3% (0%) | -4.3% (0%) | -7.4% (0%) | -1.4% (0%) | -1.4% (0%) | -1.4% (0%) | -1.6% (0%) | -2.0% (0%) |
| OPTION TRAIL 15% | -2.0% (0%) | -2.3% (0%) | -3.1% (0%) | -5.2% (0%) | -8.8% (0%) | -2.1% (0%) | -1.9% (0%) | -2.0% (0%) | -2.2% (0%) | -2.6% (0%) |

### RANDOM - TREND LINE CROSS (the bar to beat: random candles, random side, same exits)
| Exit | 2 ITM 0DTE | 1 ITM 0DTE | ATM 0DTE | 1 OTM 0DTE | 2 OTM 0DTE | 2 ITM 1DTE | 1 ITM 1DTE | ATM 1DTE | 1 OTM 1DTE | 2 OTM 1DTE |
|---|---|---|---|---|---|---|---|---|---|---|
| LINE BREAK | -0.8% (0%) | -1.7% (0%) | -2.9% (0%) | -5.1% (0%) | -8.2% (0%) | -0.0% (0%) | -0.7% (0%) | -1.1% (0%) | -1.3% (0%) | -1.4% (0%) |
| LINE COLOR | -0.8% (0%) | -1.4% (0%) | -2.7% (0%) | -5.4% (0%) | -9.3% (0%) | -0.4% (0%) | -0.7% (0%) | -0.7% (0%) | -0.9% (0%) | -1.0% (0%) |
| STRUCTURE | -1.9% (0%) | -2.3% (0%) | -3.5% (0%) | -6.4% (0%) | -10.2% (0%) | -1.2% (0%) | -1.3% (0%) | -1.2% (0%) | -1.3% (0%) | -1.6% (0%) |
| LINE OR STRUCTURE | -0.8% (0%) | -1.7% (0%) | -2.9% (0%) | -5.1% (0%) | -8.3% (0%) | -0.0% (0%) | -0.7% (0%) | -1.2% (0%) | -1.3% (0%) | -1.4% (0%) |
| TRAIL STRUCTURE | -1.2% (0%) | -1.9% (0%) | -3.1% (0%) | -5.3% (0%) | -8.7% (0%) | -0.3% (0%) | -1.1% (0%) | -1.4% (0%) | -1.6% (0%) | -1.8% (0%) |
| OPPOSITE DIAMOND | -2.3% (0%) | -3.2% (0%) | -5.0% (0%) | -8.3% (0%) | -12.6% (0%) | -1.5% (0%) | -1.6% (0%) | -1.7% (0%) | -1.9% (0%) | -2.2% (0%) |
| OPTION +10% / -10% | -1.0% (0%) | -1.6% (0%) | -2.5% (0%) | -4.4% (0%) | -7.6% (0%) | -0.9% (0%) | -1.2% (0%) | -1.4% (0%) | -1.6% (0%) | -1.9% (0%) |
| OPTION TRAIL 15% | -1.9% (0%) | -2.5% (0%) | -3.2% (0%) | -5.2% (0%) | -8.9% (0%) | -1.6% (0%) | -1.7% (0%) | -1.9% (0%) | -2.2% (0%) | -2.6% (0%) |

## 3. THE BEST COMBINATIONS (t 2.5+, positive in both halves, Kelly > 0) - 28 of 4,160 (RANDOM entries: 4 of 2,080 - if random entries pass too, it is the option prices / exits, not the diamond)
| Book | Chart | Entry | Exit | Strike | Exp | Trades | Win % | Avg return | Avg win / loss | t | Kelly | Growth / trade | 1st / 2nd half |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1m TUNED | QQQ 1m | TREND LINE CROSS | LINE OR STRUCTURE | 2 ITM | 1DTE | 1198 | 41% | **+2.2%** | +10% / -3% | 4.8 | 100% | +1.56% | +2.9% / +1.6% |
| 1m TUNED | QQQ 1m | TREND LINE CROSS | LINE BREAK | 2 ITM | 1DTE | 1198 | 41% | **+2.2%** | +10% / -3% | 4.8 | 100% | +1.56% | +2.9% / +1.6% |
| 1m TUNED | SPY+QQQ 1m | TREND LINE CROSS | LINE OR STRUCTURE | 2 ITM | 1DTE | 2457 | 39% | **+1.6%** | +10% / -4% | 4.8 | 100% | +1.04% | +2.1% / +1.2% |
| 1m TUNED | SPY+QQQ 1m | TREND LINE CROSS | LINE BREAK | 2 ITM | 1DTE | 2457 | 39% | **+1.6%** | +10% / -4% | 4.8 | 100% | +1.04% | +2.1% / +1.2% |
| YOUR SETTINGS | QQQ 1m | TREND LINE CROSS | LINE OR STRUCTURE | 2 ITM | 1DTE | 4064 | 39% | **+1.5%** | +10% / -4% | 7.8 | 100% | +0.97% | +2.1% / +0.8% |
| YOUR SETTINGS | QQQ 1m | TREND LINE CROSS | LINE BREAK | 2 ITM | 1DTE | 4064 | 39% | **+1.5%** | +10% / -4% | 7.8 | 100% | +0.96% | +2.1% / +0.8% |
| 1m TUNED | QQQ 1m | AT THE DIAMOND | LINE OR STRUCTURE | 2 ITM | 1DTE | 1357 | 42% | **+1.4%** | +9% / -4% | 4.6 | 100% | +0.87% | +1.5% / +1.4% |
| 1m TUNED | QQQ 1m | TREND LINE CROSS | TRAIL STRUCTURE | 2 ITM | 1DTE | 1202 | 43% | **+1.5%** | +10% / -5% | 3.8 | 100% | +0.85% | +1.9% / +1.1% |
| 1m TUNED | QQQ 1m | AT THE DIAMOND | LINE BREAK | 2 ITM | 1DTE | 1355 | 47% | **+1.4%** | +9% / -5% | 4.1 | 100% | +0.70% | +1.4% / +1.4% |
| YOUR SETTINGS | SPY+QQQ 1m | TREND LINE CROSS | LINE OR STRUCTURE | 2 ITM | 1DTE | 8261 | 37% | **+1.1%** | +9% / -4% | 7.4 | 100% | +0.69% | +1.7% / +0.6% |
| YOUR SETTINGS | SPY+QQQ 1m | TREND LINE CROSS | LINE BREAK | 2 ITM | 1DTE | 8261 | 37% | **+1.1%** | +9% / -4% | 7.4 | 100% | +0.68% | +1.7% / +0.6% |
| 1m TUNED | QQQ 1m | AT THE DIAMOND | TRAIL STRUCTURE | 2 ITM | 1DTE | 1367 | 40% | **+1.1%** | +10% / -5% | 3.5 | 100% | +0.56% | +1.3% / +1.0% |
| 1m TUNED | SPY 1m | TREND LINE CROSS | LINE OR STRUCTURE | 2 ITM | 1DTE | 1259 | 37% | **+1.0%** | +9% / -4% | 3.2 | 100% | +0.55% | +1.4% / +0.7% |
| 1m TUNED | SPY 1m | TREND LINE CROSS | LINE BREAK | 2 ITM | 1DTE | 1259 | 37% | **+1.0%** | +9% / -4% | 3.2 | 100% | +0.55% | +1.4% / +0.7% |
| 1m TUNED | SPY+QQQ 1m | TREND LINE CROSS | TRAIL STRUCTURE | 2 ITM | 1DTE | 2462 | 41% | **+1.0%** | +10% / -5% | 3.7 | 99% | +0.47% | +1.3% / +0.8% |
| 1m TUNED | SPY+QQQ 1m | AT THE DIAMOND | LINE OR STRUCTURE | 2 ITM | 1DTE | 2786 | 41% | **+1.0%** | +9% / -4% | 3.8 | 100% | +0.43% | +1.2% / +0.7% |
| YOUR SETTINGS | SPY 1m | TREND LINE CROSS | LINE OR STRUCTURE | 2 ITM | 1DTE | 4197 | 36% | **+0.8%** | +9% / -4% | 4.9 | 100% | +0.41% | +1.2% / +0.4% |
| YOUR SETTINGS | SPY 1m | TREND LINE CROSS | LINE BREAK | 2 ITM | 1DTE | 4197 | 36% | **+0.8%** | +9% / -4% | 4.9 | 100% | +0.41% | +1.2% / +0.4% |
| 1m TUNED | SPY+QQQ 1m | AT THE DIAMOND | LINE BREAK | 2 ITM | 1DTE | 2784 | 45% | **+1.0%** | +9% / -5% | 3.4 | 70% | +0.32% | +1.1% / +0.8% |
| YOUR SETTINGS | QQQ 1m | AT THE DIAMOND | LINE OR STRUCTURE | 2 ITM | 1DTE | 4594 | 40% | **+0.7%** | +9% / -5% | 4.6 | 76% | +0.25% | +1.2% / +0.2% |
| YOUR SETTINGS | QQQ 1m | TREND LINE CROSS | TRAIL STRUCTURE | 2 ITM | 1DTE | 4058 | 41% | **+0.7%** | +9% / -5% | 4.1 | 75% | +0.25% | +1.3% / +0.1% |
| 1m TUNED | SPY+QQQ 1m | AT THE DIAMOND | TRAIL STRUCTURE | 2 ITM | 1DTE | 2796 | 39% | **+0.7%** | +10% / -5% | 3.0 | 71% | +0.24% | +1.0% / +0.5% |
| YOUR SETTINGS | QQQ 1m | AT THE DIAMOND | LINE BREAK | 2 ITM | 1DTE | 4592 | 44% | **+0.7%** | +9% / -5% | 4.2 | 58% | +0.21% | +1.1% / +0.4% |
| 1m TUNED | SPY+QQQ ALL timeframes | TREND LINE CROSS | LINE OR STRUCTURE | 2 ITM | 1DTE | 4912 | 35% | **+0.8%** | +12% / -5% | 2.7 | 46% | +0.17% | +1.3% / +0.2% |
| 1m TUNED | SPY+QQQ ALL timeframes | TREND LINE CROSS | LINE BREAK | 2 ITM | 1DTE | 4912 | 35% | **+0.8%** | +12% / -5% | 2.7 | 46% | +0.16% | +1.3% / +0.2% |
| YOUR SETTINGS | SPY+QQQ 1m | AT THE DIAMOND | LINE BREAK | 2 ITM | 1DTE | 9368 | 42% | **+0.5%** | +9% / -5% | 3.3 | 39% | +0.10% | +0.9% / +0.1% |
| YOUR SETTINGS | SPY+QQQ ALL timeframes | TREND LINE CROSS | LINE OR STRUCTURE | 2 ITM | 1DTE | 16199 | 33% | **+0.5%** | +12% / -5% | 3.2 | 32% | +0.08% | +0.9% / +0.2% |
| YOUR SETTINGS | SPY+QQQ ALL timeframes | TREND LINE CROSS | LINE BREAK | 2 ITM | 1DTE | 16199 | 33% | **+0.5%** | +12% / -5% | 3.2 | 32% | +0.08% | +0.9% / +0.2% |

### 1m charts - best 8
| Book | Chart | Entry | Exit | Strike | Exp | Trades | Win % | Avg return | Avg win / loss | t | Kelly | Growth / trade | 1st / 2nd half |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1m TUNED | QQQ 1m | TREND LINE CROSS | LINE OR STRUCTURE | 2 ITM | 1DTE | 1198 | 41% | **+2.2%** | +10% / -3% | 4.8 | 100% | +1.56% | +2.9% / +1.6% |
| 1m TUNED | QQQ 1m | TREND LINE CROSS | LINE BREAK | 2 ITM | 1DTE | 1198 | 41% | **+2.2%** | +10% / -3% | 4.8 | 100% | +1.56% | +2.9% / +1.6% |
| 1m TUNED | SPY+QQQ 1m | TREND LINE CROSS | LINE OR STRUCTURE | 2 ITM | 1DTE | 2457 | 39% | **+1.6%** | +10% / -4% | 4.8 | 100% | +1.04% | +2.1% / +1.2% |
| 1m TUNED | SPY+QQQ 1m | TREND LINE CROSS | LINE BREAK | 2 ITM | 1DTE | 2457 | 39% | **+1.6%** | +10% / -4% | 4.8 | 100% | +1.04% | +2.1% / +1.2% |
| YOUR SETTINGS | QQQ 1m | TREND LINE CROSS | LINE OR STRUCTURE | 2 ITM | 1DTE | 4064 | 39% | **+1.5%** | +10% / -4% | 7.8 | 100% | +0.97% | +2.1% / +0.8% |
| YOUR SETTINGS | QQQ 1m | TREND LINE CROSS | LINE BREAK | 2 ITM | 1DTE | 4064 | 39% | **+1.5%** | +10% / -4% | 7.8 | 100% | +0.96% | +2.1% / +0.8% |
| 1m TUNED | QQQ 1m | AT THE DIAMOND | LINE OR STRUCTURE | 2 ITM | 1DTE | 1357 | 42% | **+1.4%** | +9% / -4% | 4.6 | 100% | +0.87% | +1.5% / +1.4% |
| 1m TUNED | QQQ 1m | TREND LINE CROSS | TRAIL STRUCTURE | 2 ITM | 1DTE | 1202 | 43% | **+1.5%** | +10% / -5% | 3.8 | 100% | +0.85% | +1.9% / +1.1% |

### 2m charts - best 8
| Book | Chart | Entry | Exit | Strike | Exp | Trades | Win % | Avg return | Avg win / loss | t | Kelly | Growth / trade | 1st / 2nd half |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

### 3m charts - best 8
| Book | Chart | Entry | Exit | Strike | Exp | Trades | Win % | Avg return | Avg win / loss | t | Kelly | Growth / trade | 1st / 2nd half |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

### 5m charts - best 8
| Book | Chart | Entry | Exit | Strike | Exp | Trades | Win % | Avg return | Avg win / loss | t | Kelly | Growth / trade | 1st / 2nd half |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

## 4. BLIND TESTS - the best combination picked on ONE half (by t), judged on the OTHER half (✅ = avg +3%+ and t 2.5+)
- **YOUR SETTINGS SPY+QQQ ALL timeframes**, picked on the 1st half: TREND LINE CROSS / LINE OR STRUCTURE / 2 ITM 1DTE (t 3.9) -> other half: **8041 trades, 31% win, +0.2%/trade, Kelly 8%** (t 0.7) 
- **YOUR SETTINGS SPY+QQQ ALL timeframes**, picked on the 2nd half: TREND LINE CROSS / LINE OR STRUCTURE / 2 ITM 1DTE (t 0.7) -> other half: **8158 trades, 35% win, +0.9%/trade, Kelly 61%** (t 3.9) 
- **YOUR SETTINGS SPY+QQQ 1m**, picked on the 1st half: TREND LINE CROSS / LINE OR STRUCTURE / 2 ITM 1DTE (t 6.9) -> other half: **4165 trades, 34% win, +0.6%/trade, Kelly 71%** (t 3.3) 
- **YOUR SETTINGS SPY+QQQ 1m**, picked on the 2nd half: TREND LINE CROSS / LINE OR STRUCTURE / 2 ITM 1DTE (t 3.3) -> other half: **4096 trades, 40% win, +1.7%/trade, Kelly 100%** (t 6.9) 
- **YOUR SETTINGS SPY+QQQ 2m**, picked on the 1st half: TREND LINE CROSS / LINE OR STRUCTURE / 2 ITM 1DTE (t 0.6) -> other half: **1914 trades, 30% win, +0.4%/trade, Kelly 16%** (t 0.9) 
- **YOUR SETTINGS SPY+QQQ 2m**, picked on the 2nd half: TREND LINE CROSS / LINE OR STRUCTURE / 2 ITM 1DTE (t 0.9) -> other half: **1986 trades, 33% win, +0.2%/trade, Kelly 13%** (t 0.6) 
- **YOUR SETTINGS SPY+QQQ 3m**, picked on the 1st half: TREND LINE CROSS / LINE OR STRUCTURE / 2 ITM 1DTE (t 0.6) -> other half: **1193 trades, 25% win, -1.3%/trade, Kelly 0%** (t -2.4) 
- **YOUR SETTINGS SPY+QQQ 3m**, picked on the 2nd half: TREND LINE CROSS / LINE COLOR / 2 ITM 0DTE (t -1.7) -> other half: **1294 trades, 35% win, -0.7%/trade, Kelly 0%** (t -0.6) 
- **YOUR SETTINGS SPY+QQQ 5m**, picked on the 1st half: TREND LINE CROSS / TRAIL STRUCTURE / 2 ITM 0DTE (t 0.7) -> other half: **781 trades, 31% win, -2.5%/trade, Kelly 0%** (t -1.7) 
- **YOUR SETTINGS SPY+QQQ 5m**, picked on the 2nd half: TREND LINE CROSS / STRUCTURE / 2 OTM 0DTE (t -0.2) -> other half: **818 trades, 22% win, -4.0%/trade, Kelly 0%** (t -0.4) 
- **1m TUNED SPY+QQQ ALL timeframes**, picked on the 1st half: TREND LINE CROSS / LINE BREAK / 2 ITM 1DTE (t 2.8) -> other half: **2509 trades, 34% win, +0.2%/trade, Kelly 14%** (t 0.7) 
- **1m TUNED SPY+QQQ ALL timeframes**, picked on the 2nd half: TREND LINE CROSS / LINE OR STRUCTURE / 2 ITM 1DTE (t 0.8) -> other half: **2403 trades, 36% win, +1.3%/trade, Kelly 81%** (t 2.8) 
- **1m TUNED SPY+QQQ 1m**, picked on the 1st half: TREND LINE CROSS / LINE OR STRUCTURE / 2 ITM 1DTE (t 3.5) -> other half: **1286 trades, 39% win, +1.2%/trade, Kelly 100%** (t 3.4) 
- **1m TUNED SPY+QQQ 1m**, picked on the 2nd half: TREND LINE CROSS / LINE OR STRUCTURE / 2 ITM 1DTE (t 3.4) -> other half: **1171 trades, 39% win, +2.1%/trade, Kelly 100%** (t 3.5) 
- **1m TUNED SPY+QQQ 2m**, picked on the 1st half: AT THE DIAMOND / LINE BREAK / 2 ITM 1DTE (t 2.0) -> other half: **687 trades, 43% win, +0.5%/trade, Kelly 28%** (t 0.9) 
- **1m TUNED SPY+QQQ 2m**, picked on the 2nd half: AT THE DIAMOND / LINE BREAK / 2 ITM 1DTE (t 0.9) -> other half: **683 trades, 42% win, +1.4%/trade, Kelly 67%** (t 2.0) 
- **1m TUNED SPY+QQQ 3m**, picked on the 1st half: TREND LINE CROSS / LINE BREAK / 2 ITM 0DTE (t 0.8) -> other half: **378 trades, 23% win, -3.7%/trade, Kelly 0%** (t -2.3) 
- **1m TUNED SPY+QQQ 3m**, picked on the 2nd half: AT THE DIAMOND / OPTION TRAIL 15% / ATM 0DTE (t -0.8) -> other half: **443 trades, 23% win, -2.7%/trade, Kelly 0%** (t -1.8) 
- **1m TUNED SPY+QQQ 5m**, picked on the 1st half: AT THE DIAMOND / TRAIL STRUCTURE / 2 ITM 1DTE (t 0.4) -> other half: **274 trades, 24% win, -3.7%/trade, Kelly 0%** (t -3.2) 
- **1m TUNED SPY+QQQ 5m**, picked on the 2nd half: TREND LINE CROSS / OPPOSITE DIAMOND / 2 OTM 1DTE (t -0.4) -> other half: **248 trades, 35% win, -3.7%/trade, Kelly 0%** (t -1.1) 
- **RANDOM SPY+QQQ ALL timeframes**, picked on the 1st half: TREND LINE CROSS / LINE OR STRUCTURE / 2 ITM 1DTE (t 0.9) -> other half: **7249 trades, 31% win, -0.2%/trade, Kelly 0%** (t -0.8) 
- **RANDOM SPY+QQQ ALL timeframes**, picked on the 2nd half: TREND LINE CROSS / LINE BREAK / 2 ITM 1DTE (t -0.7) -> other half: **6808 trades, 35% win, +0.2%/trade, Kelly 10%** (t 0.8) 
- **RANDOM SPY+QQQ 1m**, picked on the 1st half: TREND LINE CROSS / LINE OR STRUCTURE / 2 ITM 1DTE (t 5.6) -> other half: **3755 trades, 33% win, +0.1%/trade, Kelly 11%** (t 0.6) 
- **RANDOM SPY+QQQ 1m**, picked on the 2nd half: TREND LINE CROSS / LINE BREAK / 2 ITM 1DTE (t 0.7) -> other half: **3473 trades, 39% win, +1.1%/trade, Kelly 100%** (t 5.6) 
- **RANDOM SPY+QQQ 2m**, picked on the 1st half: TREND LINE CROSS / LINE COLOR / 2 ITM 0DTE (t -0.9) -> other half: **1781 trades, 34% win, -3.5%/trade, Kelly 0%** (t -2.9) 
- **RANDOM SPY+QQQ 2m**, picked on the 2nd half: AT THE DIAMOND / LINE BREAK / 2 ITM 1DTE (t -0.9) -> other half: **1978 trades, 38% win, -1.4%/trade, Kelly 0%** (t -4.7) 
- **RANDOM SPY+QQQ 3m**, picked on the 1st half: TREND LINE CROSS / STRUCTURE / ATM 1DTE (t 0.7) -> other half: **1092 trades, 32% win, -1.6%/trade, Kelly 0%** (t -1.1) 
- **RANDOM SPY+QQQ 3m**, picked on the 2nd half: TREND LINE CROSS / LINE COLOR / 1 ITM 0DTE (t 0.1) -> other half: **1098 trades, 35% win, -0.0%/trade, Kelly 0%** (t -0.0) 
- **RANDOM SPY+QQQ 5m**, picked on the 1st half: TREND LINE CROSS / OPPOSITE DIAMOND / 1 ITM 1DTE (t -0.6) -> other half: **629 trades, 46% win, +0.5%/trade, Kelly 3%** (t 0.3) 
- **RANDOM SPY+QQQ 5m**, picked on the 2nd half: TREND LINE CROSS / STRUCTURE / 1 OTM 1DTE (t 0.9) -> other half: **594 trades, 31% win, -3.6%/trade, Kelly 0%** (t -1.9) 

## 5. EVERY READING AS A FILTER (Vix Fix, colors, TTM, trend line, VWAP, the day, real VIX, option prices)
For the 3 best all-chart combinations + YOUR / TUNED at the diamond, line-or-structure exit, ATM 0DTE. ✅ = t 2.5+, positive in both halves.

### 1m TUNED / SPY+QQQ ALL timeframes / TREND LINE CROSS / LINE OR STRUCTURE / 2 ITM 1DTE
| Reading | Trades | Win % | Avg return | t | Kelly | Growth / trade | 1st / 2nd half | |
|---|---|---|---|---|---|---|---|---|
| (no filter) | 4912 | 35% | +0.8% | 2.7 | 46% | +0.17% | | |
| Stretched side now (fear for longs / greed for shorts): 0-35 | 291 | 41% | +3.5% | 2.7 | 100% | +2.11% | +4.6% / +2.5% | ✅ |
| Stretched side now (fear for longs / greed for shorts): 35-60 | 1709 | 34% | +0.4% | 1.2 | 28% | +0.05% | +0.7% / +0.1% |  |
| Stretched side now (fear for longs / greed for shorts): 60-85 | 2259 | 35% | +0.6% | 1.9 | 38% | +0.12% | +1.3% / +0.0% |  |
| Stretched side now (fear for longs / greed for shorts): 85+ | 653 | 34% | +1.1% | 1.1 | 47% | +0.23% | +1.8% / +0.4% |  |
| Other side now: 0-10 | 187 | 36% | +0.6% | 0.7 | 47% | +0.14% | +3.1% / -1.5% |  |
| Other side now: 10-20 | 725 | 36% | +1.1% | 2.2 | 100% | +0.54% | +1.7% / +0.6% |  |
| Other side now: 20-35 | 1513 | 36% | +1.4% | 2.8 | 79% | +0.47% | +2.6% / +0.3% | ✅ |
| Other side now: 35+ | 2487 | 34% | +0.3% | 0.9 | 19% | +0.03% | +0.4% / +0.2% |  |
| Stretched side's peak, last 10 candles: under 70 | 232 | 34% | +0.9% | 1.0 | 62% | +0.25% | +2.8% / -0.7% |  |
| Stretched side's peak, last 10 candles: 70-85 | 794 | 38% | +1.2% | 2.3 | 87% | +0.47% | +2.9% / -0.4% |  |
| Stretched side's peak, last 10 candles: 85-95 | 966 | 35% | +1.0% | 1.9 | 63% | +0.28% | +0.9% / +1.0% |  |
| Stretched side's peak, last 10 candles: 95-99 | 512 | 40% | +0.8% | 1.4 | 63% | +0.24% | +1.8% / -0.1% |  |
| Stretched side's peak, last 10 candles: MAXED 100 | 2408 | 33% | +0.6% | 1.3 | 28% | +0.07% | +0.8% / +0.3% |  |
| Stretched side MAXED (95+) in the last 10 candles: no | 1992 | 36% | +1.1% | 2.7 | 72% | +0.35% | +1.9% / +0.3% | ✅ |
| Stretched side MAXED (95+) in the last 10 candles: YES | 2920 | 34% | +0.6% | 1.6 | 32% | +0.09% | +1.0% / +0.2% |  |
| Other side MAXED (95+) in the last 30 candles: no | 3432 | 36% | +1.0% | 2.7 | 64% | +0.27% | +1.9% / +0.0% | ✅ |
| Other side MAXED (95+) in the last 30 candles: YES | 1480 | 33% | +0.4% | 0.9 | 19% | +0.04% | +0.0% / +0.8% |  |
| Stretched LINE COLOR: calm (gray) | 756 | 36% | +1.3% | 2.2 | 84% | +0.49% | +1.9% / +0.9% |  |
| Stretched LINE COLOR: DROPPING FAST (yellow) | 751 | 36% | +0.8% | 1.3 | 45% | +0.17% | +0.7% / +0.8% |  |
| Stretched LINE COLOR: FADING (purple greed / orange fear) | 3029 | 34% | +0.6% | 1.9 | 36% | +0.10% | +1.1% / +0.1% |  |
| Stretched LINE COLOR: BUILDING (light blue / salmon) | 152 | 32% | +0.5% | 0.5 | 42% | +0.09% | +1.5% / -0.7% |  |
| Stretched LINE COLOR: SURGING (blue greed / red fear) | 106 | 42% | +2.1% | 1.4 | 100% | +1.19% | +4.2% / +0.0% |  |
| Stretched LINE COLOR: MAXED (bright blue / hot pink) | 117 | 30% | +1.6% | 0.5 | 44% | +0.30% | +4.3% / -1.7% |  |
| Other LINE COLOR: calm (gray) | 841 | 34% | +0.7% | 1.4 | 46% | +0.15% | +1.3% / +0.2% |  |
| Other LINE COLOR: BUILDING (light blue / salmon) | 1409 | 34% | +0.6% | 1.4 | 34% | +0.09% | +0.3% / +0.9% |  |
| Other LINE COLOR: SURGING (blue greed / red fear) | 920 | 33% | +0.3% | 0.5 | 14% | +0.02% | +0.7% / -0.1% |  |
| Other LINE COLOR: MAXED (bright blue / hot pink) | 254 | 33% | +0.5% | 0.5 | 24% | +0.06% | +2.0% / -1.0% |  |
| Other LINE COLOR: BOTTOMED (brown) | 187 | 36% | +0.6% | 0.7 | 47% | +0.14% | +3.1% / -1.5% |  |
| Other LINE COLOR: WAKING UP (lime) | 1279 | 38% | +1.4% | 3.0 | 100% | +0.66% | +2.8% / +0.2% | ✅ |
| Stretched side: points dropped in the last 2 candles: rising / under 5 | 1451 | 35% | +0.7% | 1.7 | 49% | +0.17% | +1.2% / +0.3% |  |
| Stretched side: points dropped in the last 2 candles: 5-15 | 1663 | 35% | +1.0% | 2.3 | 56% | +0.25% | +1.9% / +0.1% |  |
| Stretched side: points dropped in the last 2 candles: 15-30 | 1309 | 34% | +0.5% | 1.1 | 29% | +0.07% | +0.9% / +0.2% |  |
| Stretched side: points dropped in the last 2 candles: 30+ | 489 | 36% | +1.0% | 1.3 | 57% | +0.25% | +1.0% / +0.9% |  |
| Other side: change in the last 2 candles: flat / falling | 1125 | 35% | +0.8% | 1.6 | 50% | +0.18% | +2.0% / -0.3% |  |
| Other side: change in the last 2 candles: up 5-15 | 1355 | 36% | +0.7% | 2.0 | 51% | +0.18% | +0.9% / +0.6% |  |
| Other side: change in the last 2 candles: up 15-30 | 1348 | 36% | +1.4% | 2.9 | 81% | +0.51% | +2.2% / +0.7% | ✅ |
| Other side: change in the last 2 candles: up 30+ | 1084 | 32% | +0.0% | 0.1 | 2% | +0.00% | +0.2% / -0.2% |  |
| Vix flow (greed + fear averages): YOUR way | 3505 | 35% | +0.9% | 3.0 | 52% | +0.21% | +1.2% / +0.6% | ✅ |
| Vix flow (greed + fear averages): none | 1209 | 36% | +0.4% | 0.9 | 26% | +0.05% | +1.5% / -0.6% |  |
| Vix flow (greed + fear averages): the RUN way | 198 | 32% | +1.3% | 0.7 | 55% | +0.31% | +3.7% / -1.0% |  |
| Lines GLOW (Vix flow + TTM agree): glow YOUR way | 2760 | 34% | +0.8% | 2.5 | 44% | +0.15% | +0.9% / +0.6% |  |
| Lines GLOW (Vix flow + TTM agree): no glow | 2009 | 36% | +0.7% | 1.9 | 45% | +0.15% | +1.6% / -0.2% |  |
| Lines GLOW (Vix flow + TTM agree): glow the RUN way | 143 | 32% | +2.3% | 1.0 | 100% | +0.95% | +5.4% / -0.4% |  |
| TTM COLOR: RUN STILL PUSHING (cyan shorts / red longs) | 431 | 36% | +0.6% | 0.9 | 45% | +0.12% | +1.5% / -0.3% |  |
| TTM COLOR: RUN FADING (blue shorts / yellow longs) | 4343 | 34% | +0.7% | 2.4 | 43% | +0.15% | +1.2% / +0.3% |  |
| TTM COLOR: FLIPPED YOUR WAY (red shorts / cyan longs) | 123 | 46% | +3.4% | 2.0 | 100% | +2.17% | +7.7% / -0.3% |  |
| TTM average peak before the turn (ATR): under 1.5 | 1989 | 37% | +0.9% | 2.3 | 59% | +0.25% | +1.9% / +0.1% |  |
| TTM average peak before the turn (ATR): 1.5-2 | 1064 | 33% | +0.4% | 1.0 | 26% | +0.05% | +0.8% / +0.1% |  |
| TTM average peak before the turn (ATR): 2-3 | 1380 | 35% | +1.4% | 2.3 | 78% | +0.47% | +1.9% / +0.8% |  |
| TTM average peak before the turn (ATR): 3+ | 479 | 31% | -0.7% | -1.2 | 0% | +0.00% | -1.3% / -0.1% |  |
| TREND LINE COLOR: RUN SIDE STRONG (green shorts / red longs) | 3376 | 34% | +0.9% | 2.6 | 50% | +0.20% | +1.4% / +0.4% | ✅ |
| TREND LINE COLOR: RUN SIDE FADING (blue shorts / pink longs) | 149 | 40% | +0.8% | 0.6 | 41% | +0.15% | +2.5% / -1.0% |  |
| TREND LINE COLOR: GRAY | 1215 | 37% | +0.3% | 0.8 | 24% | +0.03% | +0.4% / +0.2% |  |
| TREND LINE COLOR: YOUR SIDE STRONG (red shorts / green longs) | 166 | 42% | +2.3% | 1.4 | 96% | +0.93% | +6.7% / -1.8% |  |
| Price vs trend line (ATR): through it to YOUR side | 1763 | 37% | +1.2% | 2.7 | 60% | +0.33% | +1.5% / +0.9% | ✅ |
| Price vs trend line (ATR): at the line | 1614 | 33% | +0.5% | 1.3 | 36% | +0.09% | +1.0% / +0.1% |  |
| Price vs trend line (ATR): 0.25-1 ATR on the run side | 1274 | 35% | +0.8% | 1.4 | 50% | +0.18% | +1.6% / -0.0% |  |
| Price vs trend line (ATR): 1+ ATR on the run side | 261 | 30% | -0.3% | -0.4 | 0% | +0.00% | +0.9% / -1.7% |  |
| Trend line angle (+ = the run's way): flat (-5 to +5) | 1790 | 36% | +1.0% | 2.5 | 56% | +0.25% | +1.1% / +0.9% |  |
| Trend line angle (+ = the run's way): run way 5-15 | 2836 | 34% | +0.6% | 1.7 | 38% | +0.11% | +1.4% / -0.1% |  |
| Trend line angle (+ = the run's way): run way 15+ | 280 | 32% | +0.8% | 0.9 | 54% | +0.21% | +1.6% / -0.2% |  |
| TTM squeeze: ON | 1037 | 38% | +0.9% | 2.0 | 64% | +0.27% | +1.7% / +0.3% |  |
| TTM squeeze: just fired | 168 | 41% | +3.2% | 2.4 | 100% | +2.08% | +5.2% / +1.0% |  |
| TTM squeeze: off | 3707 | 34% | +0.6% | 1.9 | 36% | +0.11% | +1.1% / +0.2% |  |
| Price vs VWAP (ATR, + = run side): your side | 913 | 38% | +0.9% | 2.0 | 79% | +0.34% | +1.8% / +0.2% |  |
| Price vs VWAP (ATR, + = run side): -1 to +1 | 1208 | 34% | +0.2% | 0.4 | 10% | +0.01% | +0.5% / -0.1% |  |
| Price vs VWAP (ATR, + = run side): +1 to +3 | 1164 | 34% | +1.7% | 2.6 | 75% | +0.56% | +2.8% / +0.7% | ✅ |
| Price vs VWAP (ATR, + = run side): +3 or more | 1627 | 34% | +0.4% | 1.4 | 44% | +0.09% | +0.7% / +0.2% |  |
| The move into the diamond (last 20 candles, $): under $0.75 | 585 | 41% | +1.0% | 3.0 | 100% | +0.76% | +0.9% / +1.1% | ✅ |
| The move into the diamond (last 20 candles, $): $0.75-1.50 | 1508 | 38% | +1.4% | 3.1 | 100% | +0.75% | +2.3% / +0.4% | ✅ |
| The move into the diamond (last 20 candles, $): $1.50-3 | 1790 | 33% | +0.3% | 0.7 | 16% | +0.02% | +0.8% / -0.1% |  |
| The move into the diamond (last 20 candles, $): $3+ | 1029 | 30% | +0.6% | 0.7 | 18% | +0.05% | +0.9% / +0.4% |  |
| Price already came back from the extreme ($): under $0.20 | 389 | 36% | +0.8% | 1.5 | 100% | +0.40% | +1.9% / -0.4% |  |
| Price already came back from the extreme ($): $0.20-0.50 | 1560 | 36% | +0.6% | 2.0 | 73% | +0.20% | +1.1% / +0.1% |  |
| Price already came back from the extreme ($): $0.50-1 | 1703 | 39% | +1.2% | 3.0 | 83% | +0.45% | +1.1% / +1.3% | ✅ |
| Price already came back from the extreme ($): $1+ | 1260 | 28% | +0.4% | 0.6 | 13% | +0.03% | +1.9% / -0.7% |  |
| Day so far: net move / range: round trips (under 30%) | 1462 | 35% | +0.4% | 1.1 | 29% | +0.06% | +0.7% / +0.2% |  |
| Day so far: net move / range: 30-60% | 1821 | 35% | +1.0% | 2.3 | 50% | +0.22% | +1.4% / +0.5% |  |
| Day so far: net move / range: trending (60%+) | 1629 | 35% | +0.9% | 2.2 | 58% | +0.24% | +1.9% / -0.0% |  |
| Diamond vs the day's move so far: WITH the day | 1586 | 39% | +1.0% | 2.5 | 73% | +0.32% | +1.7% / +0.3% |  |
| Diamond vs the day's move so far: AGAINST the day | 3326 | 33% | +0.7% | 1.9 | 37% | +0.12% | +1.2% / +0.2% |  |
| REAL VIX today (VIXY vs yesterday): down | 2712 | 35% | +0.8% | 2.4 | 53% | +0.20% | +1.0% / +0.6% |  |
| REAL VIX today (VIXY vs yesterday): up 0-3% | 1605 | 36% | +0.3% | 0.8 | 19% | +0.03% | +1.1% / -0.3% |  |
| REAL VIX today (VIXY vs yesterday): up 3%+ | 595 | 32% | +2.0% | 1.5 | 86% | +0.72% | +3.1% / +0.2% |  |
| REAL VIX vs its 20-day average: LOW (5%+ under) | 1919 | 36% | +0.6% | 1.6 | 43% | +0.12% | +0.3% / +0.8% |  |
| REAL VIX vs its 20-day average: normal | 2172 | 34% | +0.5% | 1.2 | 28% | +0.06% | +1.2% / -0.2% |  |
| REAL VIX vs its 20-day average: HIGH (5%+ over) | 821 | 36% | +2.1% | 1.9 | 85% | +0.78% | +3.2% / +0.0% |  |
| Options today: 9:45 ATM straddle vs the last 20 days' real move: CHEAP (under 0.8x) | 803 | 36% | +0.6% | 1.0 | 40% | +0.11% | -0.2% / +1.3% |  |
| Options today: 9:45 ATM straddle vs the last 20 days' real move: fair (0.8-1.2x) | 2174 | 34% | +0.7% | 1.9 | 46% | +0.16% | +1.6% / -0.1% |  |
| Options today: 9:45 ATM straddle vs the last 20 days' real move: RICH (over 1.2x) | 1786 | 35% | +0.6% | 1.4 | 35% | +0.10% | +1.0% / +0.2% |  |
| Options today: 9:45 ATM straddle vs the last 20 days' real move: unknown (before 9:45) | 149 | 38% | +4.6% | 1.0 | 100% | +2.55% | +6.7% / -1.3% |  |

**Best pairs for this combination (12 shown):**
| Readings | Trades | Win % | Avg return | t | Kelly | Growth / trade | 1st / 2nd half |
|---|---|---|---|---|---|---|---|
| Stretched side now (fear for longs / greed for shorts): 0-35 + REAL VIX vs its 20-day average: normal | 116 | 44% | +5.4% | 2.5 | 100% | +3.76% | +8.0% / +3.2% |
| Stretched side now (fear for longs / greed for shorts): 0-35 + Price vs trend line (ATR): through it to YOUR side | 175 | 44% | +5.3% | 2.7 | 100% | +3.30% | +6.3% / +4.3% |
| Stretched side now (fear for longs / greed for shorts): 0-35 + Lines GLOW (Vix flow + TTM agree): glow YOUR way | 240 | 42% | +4.3% | 2.8 | 100% | +2.63% | +5.5% / +3.1% |
| Stretched side now (fear for longs / greed for shorts): 0-35 + Vix flow (greed + fear averages): YOUR way | 252 | 43% | +4.2% | 2.9 | 100% | +2.59% | +5.4% / +3.0% |
| Stretched side now (fear for longs / greed for shorts): 0-35 + Trend line angle (+ = the run's way): flat (-5 to +5) | 236 | 41% | +3.9% | 2.6 | 100% | +2.32% | +4.6% / +3.1% |
| TTM COLOR: RUN STILL PUSHING (cyan shorts / red longs) + The move into the diamond (last 20 candles, $): $0.75-1.50 | 147 | 46% | +3.1% | 2.6 | 100% | +2.28% | +5.4% / +0.8% |
| Stretched side's peak, last 10 candles: 70-85 + The move into the diamond (last 20 candles, $): $0.75-1.50 | 285 | 47% | +3.2% | 2.9 | 100% | +2.14% | +5.4% / +0.9% |
| The move into the diamond (last 20 candles, $): $0.75-1.50 + Day so far: net move / range: trending (60%+) | 471 | 40% | +3.0% | 3.6 | 100% | +2.05% | +3.9% / +2.0% |
| Other side now: 20-35 + Stretched side's peak, last 10 candles: 70-85 | 263 | 46% | +2.9% | 2.9 | 100% | +1.96% | +5.8% / +0.3% |
| Other side: change in the last 2 candles: up 15-30 + Price already came back from the extreme ($): $0.50-1 | 503 | 42% | +3.0% | 3.5 | 100% | +1.92% | +3.2% / +2.9% |
| Other side: change in the last 2 candles: up 15-30 + Price vs VWAP (ATR, + = run side): +1 to +3 | 308 | 35% | +3.5% | 2.6 | 100% | +1.75% | +4.3% / +2.9% |
| Price vs VWAP (ATR, + = run side): -1 to +1 + The move into the diamond (last 20 candles, $): under $0.75 | 97 | 53% | +2.0% | 2.6 | 100% | +1.69% | +1.5% / +3.3% |
- BLIND, picked on the 1st half: Other side now: 20-35 + Stretched side MAXED (95+) in the last 10 candles: no (t 3.6) -> other half: **350 trades, 36% win, +0.5%/trade, Kelly 32%** (t 0.6) 
- BLIND, picked on the 2nd half: The move into the diamond (last 20 candles, $): under $0.75 + REAL VIX today (VIXY vs yesterday): up 0-3% (t 3.3) -> other half: **96 trades, 36% win, +0.3%/trade, Kelly 82%** (t 0.4) 

### 1m TUNED / SPY+QQQ ALL timeframes / TREND LINE CROSS / LINE BREAK / 2 ITM 1DTE
| Reading | Trades | Win % | Avg return | t | Kelly | Growth / trade | 1st / 2nd half | |
|---|---|---|---|---|---|---|---|---|
| (no filter) | 4912 | 35% | +0.8% | 2.7 | 46% | +0.16% | | |
| Stretched side now (fear for longs / greed for shorts): 0-35 | 291 | 41% | +3.5% | 2.7 | 100% | +2.04% | +4.6% / +2.4% | ✅ |
| Stretched side now (fear for longs / greed for shorts): 35-60 | 1709 | 34% | +0.4% | 1.2 | 28% | +0.05% | +0.7% / +0.1% |  |
| Stretched side now (fear for longs / greed for shorts): 60-85 | 2259 | 35% | +0.6% | 1.8 | 38% | +0.11% | +1.3% / +0.0% |  |
| Stretched side now (fear for longs / greed for shorts): 85+ | 653 | 34% | +1.1% | 1.0 | 47% | +0.22% | +1.8% / +0.4% |  |
| Other side now: 0-10 | 187 | 36% | +0.7% | 0.7 | 49% | +0.15% | +3.1% / -1.5% |  |
| Other side now: 10-20 | 725 | 36% | +1.1% | 2.2 | 100% | +0.52% | +1.7% / +0.5% |  |
| Other side now: 20-35 | 1513 | 36% | +1.3% | 2.8 | 78% | +0.46% | +2.6% / +0.3% | ✅ |
| Other side now: 35+ | 2487 | 34% | +0.3% | 0.9 | 18% | +0.03% | +0.4% / +0.2% |  |
| Stretched side's peak, last 10 candles: under 70 | 232 | 34% | +0.9% | 1.0 | 62% | +0.25% | +2.8% / -0.7% |  |
| Stretched side's peak, last 10 candles: 70-85 | 794 | 38% | +1.2% | 2.2 | 84% | +0.44% | +2.9% / -0.5% |  |
| Stretched side's peak, last 10 candles: 85-95 | 966 | 35% | +1.0% | 1.9 | 62% | +0.28% | +0.9% / +1.0% |  |
| Stretched side's peak, last 10 candles: 95-99 | 512 | 40% | +0.8% | 1.4 | 63% | +0.23% | +1.8% / -0.1% |  |
| Stretched side's peak, last 10 candles: MAXED 100 | 2408 | 33% | +0.5% | 1.3 | 28% | +0.07% | +0.8% / +0.3% |  |
| Stretched side MAXED (95+) in the last 10 candles: no | 1992 | 36% | +1.0% | 2.7 | 70% | +0.33% | +1.9% / +0.2% | ✅ |
| Stretched side MAXED (95+) in the last 10 candles: YES | 2920 | 34% | +0.6% | 1.6 | 32% | +0.09% | +1.0% / +0.2% |  |
| Other side MAXED (95+) in the last 30 candles: no | 3432 | 36% | +0.9% | 2.7 | 63% | +0.27% | +1.9% / +0.0% | ✅ |
| Other side MAXED (95+) in the last 30 candles: YES | 1480 | 33% | +0.4% | 0.9 | 18% | +0.03% | +0.0% / +0.8% |  |
| Stretched LINE COLOR: calm (gray) | 756 | 36% | +1.3% | 2.2 | 81% | +0.46% | +1.9% / +0.8% |  |
| Stretched LINE COLOR: DROPPING FAST (yellow) | 751 | 36% | +0.8% | 1.3 | 44% | +0.16% | +0.7% / +0.8% |  |
| Stretched LINE COLOR: FADING (purple greed / orange fear) | 3029 | 34% | +0.6% | 1.9 | 35% | +0.10% | +1.1% / +0.0% |  |
| Stretched LINE COLOR: BUILDING (light blue / salmon) | 152 | 32% | +0.5% | 0.5 | 45% | +0.10% | +1.5% / -0.6% |  |
| Stretched LINE COLOR: SURGING (blue greed / red fear) | 106 | 42% | +2.1% | 1.4 | 100% | +1.19% | +4.2% / +0.0% |  |
| Stretched LINE COLOR: MAXED (bright blue / hot pink) | 117 | 30% | +1.6% | 0.5 | 44% | +0.30% | +4.3% / -1.7% |  |
| Other LINE COLOR: calm (gray) | 841 | 34% | +0.7% | 1.4 | 44% | +0.14% | +1.3% / +0.2% |  |
| Other LINE COLOR: BUILDING (light blue / salmon) | 1409 | 34% | +0.6% | 1.3 | 34% | +0.09% | +0.3% / +0.9% |  |
| Other LINE COLOR: SURGING (blue greed / red fear) | 920 | 33% | +0.3% | 0.5 | 13% | +0.02% | +0.7% / -0.1% |  |
| Other LINE COLOR: MAXED (bright blue / hot pink) | 254 | 33% | +0.5% | 0.5 | 25% | +0.06% | +2.0% / -1.0% |  |
| Other LINE COLOR: BOTTOMED (brown) | 187 | 36% | +0.7% | 0.7 | 49% | +0.15% | +3.1% / -1.5% |  |
| Other LINE COLOR: WAKING UP (lime) | 1279 | 38% | +1.4% | 3.0 | 100% | +0.64% | +2.8% / +0.2% | ✅ |
| Stretched side: points dropped in the last 2 candles: rising / under 5 | 1451 | 35% | +0.8% | 1.7 | 50% | +0.17% | +1.3% / +0.3% |  |
| Stretched side: points dropped in the last 2 candles: 5-15 | 1663 | 35% | +0.9% | 2.3 | 54% | +0.24% | +1.9% / +0.0% |  |
| Stretched side: points dropped in the last 2 candles: 15-30 | 1309 | 34% | +0.5% | 1.1 | 29% | +0.07% | +0.9% / +0.1% |  |
| Stretched side: points dropped in the last 2 candles: 30+ | 489 | 36% | +0.9% | 1.3 | 55% | +0.24% | +1.0% / +0.9% |  |
| Other side: change in the last 2 candles: flat / falling | 1125 | 35% | +0.8% | 1.5 | 49% | +0.17% | +2.0% / -0.3% |  |
| Other side: change in the last 2 candles: up 5-15 | 1355 | 36% | +0.7% | 2.0 | 51% | +0.18% | +0.9% / +0.6% |  |
| Other side: change in the last 2 candles: up 15-30 | 1348 | 36% | +1.4% | 2.9 | 77% | +0.48% | +2.2% / +0.6% | ✅ |
| Other side: change in the last 2 candles: up 30+ | 1084 | 32% | +0.1% | 0.1 | 3% | +0.00% | +0.3% / -0.2% |  |
| Vix flow (greed + fear averages): YOUR way | 3505 | 35% | +0.9% | 3.0 | 52% | +0.21% | +1.2% / +0.6% | ✅ |
| Vix flow (greed + fear averages): none | 1209 | 36% | +0.4% | 0.8 | 25% | +0.05% | +1.5% / -0.7% |  |
| Vix flow (greed + fear averages): the RUN way | 198 | 32% | +1.3% | 0.7 | 55% | +0.31% | +3.7% / -1.0% |  |
| Lines GLOW (Vix flow + TTM agree): glow YOUR way | 2760 | 34% | +0.7% | 2.4 | 43% | +0.15% | +0.9% / +0.6% |  |
| Lines GLOW (Vix flow + TTM agree): no glow | 2009 | 36% | +0.7% | 1.9 | 44% | +0.15% | +1.6% / -0.2% |  |
| Lines GLOW (Vix flow + TTM agree): glow the RUN way | 143 | 32% | +2.3% | 1.0 | 100% | +0.95% | +5.4% / -0.4% |  |
| TTM COLOR: RUN STILL PUSHING (cyan shorts / red longs) | 431 | 36% | +0.6% | 0.9 | 46% | +0.12% | +1.6% / -0.3% |  |
| TTM COLOR: RUN FADING (blue shorts / yellow longs) | 4343 | 34% | +0.7% | 2.3 | 42% | +0.14% | +1.2% / +0.3% |  |
| TTM COLOR: FLIPPED YOUR WAY (red shorts / cyan longs) | 123 | 46% | +3.4% | 2.0 | 100% | +2.17% | +7.7% / -0.3% |  |
| TTM average peak before the turn (ATR): under 1.5 | 1989 | 37% | +0.9% | 2.4 | 59% | +0.25% | +1.9% / +0.1% |  |
| TTM average peak before the turn (ATR): 1.5-2 | 1064 | 33% | +0.4% | 0.9 | 24% | +0.05% | +0.8% / +0.0% |  |
| TTM average peak before the turn (ATR): 2-3 | 1380 | 35% | +1.4% | 2.3 | 77% | +0.46% | +1.9% / +0.8% |  |
| TTM average peak before the turn (ATR): 3+ | 479 | 31% | -0.7% | -1.2 | 0% | +0.00% | -1.3% / -0.1% |  |
| TREND LINE COLOR: RUN SIDE STRONG (green shorts / red longs) | 3376 | 34% | +0.9% | 2.6 | 50% | +0.20% | +1.4% / +0.4% | ✅ |
| TREND LINE COLOR: RUN SIDE FADING (blue shorts / pink longs) | 149 | 40% | +0.8% | 0.6 | 40% | +0.14% | +2.5% / -1.0% |  |
| TREND LINE COLOR: GRAY | 1215 | 37% | +0.3% | 0.7 | 21% | +0.03% | +0.4% / +0.2% |  |
| TREND LINE COLOR: YOUR SIDE STRONG (red shorts / green longs) | 166 | 42% | +2.2% | 1.3 | 91% | +0.87% | +6.7% / -1.9% |  |
| Price vs trend line (ATR): through it to YOUR side | 1763 | 37% | +1.2% | 2.7 | 58% | +0.31% | +1.5% / +0.8% | ✅ |
| Price vs trend line (ATR): at the line | 1614 | 33% | +0.5% | 1.3 | 36% | +0.09% | +1.0% / +0.1% |  |
| Price vs trend line (ATR): 0.25-1 ATR on the run side | 1274 | 35% | +0.8% | 1.4 | 50% | +0.18% | +1.6% / -0.1% |  |
| Price vs trend line (ATR): 1+ ATR on the run side | 261 | 30% | -0.3% | -0.4 | 0% | +0.00% | +1.0% / -1.7% |  |
| Trend line angle (+ = the run's way): flat (-5 to +5) | 1790 | 36% | +0.9% | 2.4 | 54% | +0.24% | +1.1% / +0.8% |  |
| Trend line angle (+ = the run's way): run way 5-15 | 2836 | 34% | +0.6% | 1.7 | 38% | +0.11% | +1.4% / -0.1% |  |
| Trend line angle (+ = the run's way): run way 15+ | 280 | 32% | +0.8% | 0.9 | 54% | +0.21% | +1.6% / -0.2% |  |
| TTM squeeze: ON | 1037 | 38% | +0.9% | 2.0 | 63% | +0.26% | +1.7% / +0.3% |  |
| TTM squeeze: just fired | 168 | 41% | +3.2% | 2.4 | 100% | +2.08% | +5.2% / +1.0% |  |
| TTM squeeze: off | 3707 | 34% | +0.6% | 1.8 | 35% | +0.10% | +1.1% / +0.2% |  |
| Price vs VWAP (ATR, + = run side): your side | 913 | 38% | +0.9% | 1.9 | 75% | +0.32% | +1.8% / +0.2% |  |
| Price vs VWAP (ATR, + = run side): -1 to +1 | 1208 | 34% | +0.2% | 0.4 | 9% | +0.01% | +0.5% / -0.1% |  |
| Price vs VWAP (ATR, + = run side): +1 to +3 | 1164 | 34% | +1.7% | 2.6 | 75% | +0.56% | +2.8% / +0.7% | ✅ |
| Price vs VWAP (ATR, + = run side): +3 or more | 1627 | 34% | +0.4% | 1.4 | 44% | +0.09% | +0.7% / +0.2% |  |
| The move into the diamond (last 20 candles, $): under $0.75 | 585 | 41% | +1.0% | 3.1 | 100% | +0.77% | +0.9% / +1.1% | ✅ |
| The move into the diamond (last 20 candles, $): $0.75-1.50 | 1508 | 38% | +1.4% | 3.1 | 100% | +0.76% | +2.3% / +0.4% | ✅ |
| The move into the diamond (last 20 candles, $): $1.50-3 | 1790 | 33% | +0.3% | 0.7 | 15% | +0.02% | +0.8% / -0.2% |  |
| The move into the diamond (last 20 candles, $): $3+ | 1029 | 30% | +0.6% | 0.7 | 17% | +0.05% | +0.9% / +0.3% |  |
| Price already came back from the extreme ($): under $0.20 | 389 | 36% | +0.8% | 1.5 | 100% | +0.40% | +1.9% / -0.4% |  |
| Price already came back from the extreme ($): $0.20-0.50 | 1560 | 36% | +0.6% | 2.0 | 75% | +0.21% | +1.1% / +0.1% |  |
| Price already came back from the extreme ($): $0.50-1 | 1703 | 39% | +1.2% | 3.0 | 82% | +0.44% | +1.1% / +1.3% | ✅ |
| Price already came back from the extreme ($): $1+ | 1260 | 28% | +0.4% | 0.5 | 12% | +0.02% | +1.9% / -0.7% |  |
| Day so far: net move / range: round trips (under 30%) | 1462 | 35% | +0.4% | 1.1 | 28% | +0.06% | +0.7% / +0.2% |  |
| Day so far: net move / range: 30-60% | 1821 | 35% | +0.9% | 2.2 | 49% | +0.21% | +1.4% / +0.5% |  |
| Day so far: net move / range: trending (60%+) | 1629 | 35% | +0.9% | 2.1 | 57% | +0.23% | +1.9% / -0.0% |  |
| Diamond vs the day's move so far: WITH the day | 1586 | 39% | +0.9% | 2.5 | 73% | +0.32% | +1.7% / +0.2% |  |
| Diamond vs the day's move so far: AGAINST the day | 3326 | 33% | +0.7% | 1.8 | 36% | +0.12% | +1.2% / +0.2% |  |
| REAL VIX today (VIXY vs yesterday): down | 2712 | 35% | +0.8% | 2.4 | 51% | +0.19% | +1.0% / +0.6% |  |
| REAL VIX today (VIXY vs yesterday): up 0-3% | 1605 | 36% | +0.3% | 0.8 | 19% | +0.03% | +1.1% / -0.3% |  |
| REAL VIX today (VIXY vs yesterday): up 3%+ | 595 | 32% | +1.9% | 1.5 | 85% | +0.71% | +3.1% / +0.2% |  |
| REAL VIX vs its 20-day average: LOW (5%+ under) | 1919 | 36% | +0.6% | 1.6 | 43% | +0.11% | +0.3% / +0.7% |  |
| REAL VIX vs its 20-day average: normal | 2172 | 34% | +0.5% | 1.2 | 27% | +0.06% | +1.2% / -0.3% |  |
| REAL VIX vs its 20-day average: HIGH (5%+ over) | 821 | 36% | +2.1% | 1.9 | 85% | +0.77% | +3.2% / +0.0% |  |
| Options today: 9:45 ATM straddle vs the last 20 days' real move: CHEAP (under 0.8x) | 803 | 36% | +0.6% | 1.0 | 41% | +0.11% | -0.2% / +1.3% |  |
| Options today: 9:45 ATM straddle vs the last 20 days' real move: fair (0.8-1.2x) | 2174 | 34% | +0.7% | 1.9 | 46% | +0.16% | +1.6% / -0.1% |  |
| Options today: 9:45 ATM straddle vs the last 20 days' real move: RICH (over 1.2x) | 1786 | 35% | +0.6% | 1.4 | 34% | +0.09% | +1.0% / +0.2% |  |
| Options today: 9:45 ATM straddle vs the last 20 days' real move: unknown (before 9:45) | 149 | 38% | +4.6% | 1.0 | 100% | +2.55% | +6.7% / -1.3% |  |

**Best pairs for this combination (12 shown):**
| Readings | Trades | Win % | Avg return | t | Kelly | Growth / trade | 1st / 2nd half |
|---|---|---|---|---|---|---|---|
| Stretched side now (fear for longs / greed for shorts): 0-35 + Price vs trend line (ATR): through it to YOUR side | 175 | 44% | +5.3% | 2.7 | 100% | +3.30% | +6.3% / +4.3% |
| Stretched side now (fear for longs / greed for shorts): 0-35 + Lines GLOW (Vix flow + TTM agree): glow YOUR way | 240 | 42% | +4.3% | 2.8 | 100% | +2.63% | +5.5% / +3.1% |
| Stretched side now (fear for longs / greed for shorts): 0-35 + Vix flow (greed + fear averages): YOUR way | 252 | 43% | +4.2% | 2.9 | 100% | +2.59% | +5.4% / +3.0% |
| TTM COLOR: RUN STILL PUSHING (cyan shorts / red longs) + The move into the diamond (last 20 candles, $): $0.75-1.50 | 147 | 46% | +3.1% | 2.6 | 100% | +2.28% | +5.4% / +0.8% |
| Stretched side now (fear for longs / greed for shorts): 0-35 + Trend line angle (+ = the run's way): flat (-5 to +5) | 236 | 41% | +3.8% | 2.6 | 100% | +2.23% | +4.6% / +3.0% |
| Stretched side's peak, last 10 candles: 70-85 + The move into the diamond (last 20 candles, $): $0.75-1.50 | 285 | 47% | +3.2% | 2.9 | 100% | +2.14% | +5.4% / +0.9% |
| The move into the diamond (last 20 candles, $): $0.75-1.50 + Day so far: net move / range: trending (60%+) | 471 | 40% | +3.0% | 3.6 | 100% | +2.05% | +3.9% / +2.0% |
| Other side now: 20-35 + Stretched side's peak, last 10 candles: 70-85 | 263 | 46% | +2.9% | 2.9 | 100% | +1.96% | +5.8% / +0.3% |
| Other side: change in the last 2 candles: up 15-30 + Price already came back from the extreme ($): $0.50-1 | 503 | 42% | +3.0% | 3.5 | 100% | +1.91% | +3.1% / +2.9% |
| Price vs VWAP (ATR, + = run side): -1 to +1 + The move into the diamond (last 20 candles, $): under $0.75 | 97 | 53% | +2.1% | 2.8 | 100% | +1.79% | +1.6% / +3.3% |
| Other side: change in the last 2 candles: up 15-30 + Price vs VWAP (ATR, + = run side): +1 to +3 | 308 | 35% | +3.5% | 2.6 | 100% | +1.73% | +4.3% / +2.9% |
| Other LINE COLOR: WAKING UP (lime) + The move into the diamond (last 20 candles, $): $0.75-1.50 | 458 | 41% | +2.5% | 2.8 | 100% | +1.67% | +4.1% / +0.9% |
- BLIND, picked on the 1st half: Other side now: 20-35 + Stretched side MAXED (95+) in the last 10 candles: no (t 3.6) -> other half: **350 trades, 36% win, +0.4%/trade, Kelly 29%** (t 0.6) 
- BLIND, picked on the 2nd half: The move into the diamond (last 20 candles, $): under $0.75 + REAL VIX today (VIXY vs yesterday): up 0-3% (t 3.3) -> other half: **96 trades, 36% win, +0.3%/trade, Kelly 82%** (t 0.4) 

### YOUR SETTINGS / SPY+QQQ ALL timeframes / TREND LINE CROSS / LINE OR STRUCTURE / 2 ITM 1DTE
| Reading | Trades | Win % | Avg return | t | Kelly | Growth / trade | 1st / 2nd half | |
|---|---|---|---|---|---|---|---|---|
| (no filter) | 16199 | 33% | +0.5% | 3.2 | 32% | +0.08% | | |
| Stretched side now (fear for longs / greed for shorts): 0-35 | 376 | 34% | +0.8% | 1.0 | 41% | +0.16% | +1.3% / +0.3% |  |
| Stretched side now (fear for longs / greed for shorts): 35-60 | 4645 | 33% | +0.5% | 2.1 | 31% | +0.08% | +1.1% / -0.1% |  |
| Stretched side now (fear for longs / greed for shorts): 60-85 | 8887 | 33% | +0.5% | 2.3 | 29% | +0.07% | +0.8% / +0.2% |  |
| Stretched side now (fear for longs / greed for shorts): 85+ | 2291 | 32% | +0.8% | 2.0 | 42% | +0.16% | +1.0% / +0.6% |  |
| Other side now: 0-10 | 553 | 30% | +0.1% | 0.1 | 6% | +0.00% | +0.1% / +0.1% |  |
| Other side now: 10-20 | 2440 | 31% | +0.5% | 1.6 | 35% | +0.08% | +1.1% / -0.1% |  |
| Other side now: 20-35 | 4925 | 34% | +0.9% | 3.8 | 61% | +0.25% | +1.5% / +0.3% | ✅ |
| Other side now: 35+ | 8281 | 33% | +0.4% | 1.7 | 20% | +0.04% | +0.6% / +0.1% |  |
| Stretched side's peak, last 10 candles: under 70 | 1207 | 33% | -0.0% | -0.0 | 0% | +0.00% | +0.3% / -0.3% |  |
| Stretched side's peak, last 10 candles: 70-85 | 2352 | 34% | +1.1% | 3.1 | 71% | +0.33% | +1.7% / +0.5% | ✅ |
| Stretched side's peak, last 10 candles: 85-95 | 1926 | 35% | +0.6% | 2.0 | 48% | +0.14% | +1.4% / -0.1% |  |
| Stretched side's peak, last 10 candles: 95-99 | 1007 | 33% | -0.1% | -0.2 | 0% | +0.00% | +0.5% / -0.6% |  |
| Stretched side's peak, last 10 candles: MAXED 100 | 9707 | 33% | +0.5% | 2.4 | 29% | +0.07% | +0.8% / +0.3% |  |
| Stretched side MAXED (95+) in the last 10 candles: no | 5485 | 34% | +0.7% | 3.0 | 48% | +0.15% | +1.2% / +0.1% | ✅ |
| Stretched side MAXED (95+) in the last 10 candles: YES | 10714 | 33% | +0.5% | 2.3 | 26% | +0.06% | +0.8% / +0.2% |  |
| Other side MAXED (95+) in the last 30 candles: no | 9452 | 34% | +0.8% | 4.1 | 58% | +0.21% | +1.3% / +0.2% | ✅ |
| Other side MAXED (95+) in the last 30 candles: YES | 6747 | 32% | +0.2% | 0.8 | 10% | +0.01% | +0.4% / +0.0% |  |
| Stretched LINE COLOR: calm (gray) | 1095 | 32% | +0.0% | 0.1 | 2% | +0.00% | +0.2% / -0.1% |  |
| Stretched LINE COLOR: DROPPING FAST (yellow) | 4152 | 33% | +0.7% | 2.2 | 35% | +0.11% | +1.1% / +0.3% |  |
| Stretched LINE COLOR: FADING (purple greed / orange fear) | 9753 | 33% | +0.5% | 2.8 | 32% | +0.08% | +0.9% / +0.2% | ✅ |
| Stretched LINE COLOR: BUILDING (light blue / salmon) | 306 | 33% | +1.0% | 1.3 | 71% | +0.33% | +3.0% / -1.0% |  |
| Stretched LINE COLOR: SURGING (blue greed / red fear) | 652 | 32% | +0.9% | 1.6 | 57% | +0.24% | +1.0% / +0.8% |  |
| Stretched LINE COLOR: MAXED (bright blue / hot pink) | 241 | 30% | -0.1% | -0.1 | 0% | +0.00% | +0.7% / -0.9% |  |
| Other LINE COLOR: calm (gray) | 3398 | 34% | +0.8% | 3.0 | 57% | +0.20% | +1.1% / +0.5% | ✅ |
| Other LINE COLOR: FADING (purple greed / orange fear) | 349 | 36% | +0.6% | 0.7 | 35% | +0.09% | +0.8% / +0.2% |  |
| Other LINE COLOR: BUILDING (light blue / salmon) | 4470 | 33% | +0.3% | 1.4 | 20% | +0.03% | +0.6% / +0.1% |  |
| Other LINE COLOR: SURGING (blue greed / red fear) | 2273 | 34% | +0.7% | 1.9 | 40% | +0.14% | +1.1% / +0.3% |  |
| Other LINE COLOR: MAXED (bright blue / hot pink) | 1024 | 32% | -0.0% | -0.0 | 0% | +0.00% | +0.2% / -0.3% |  |
| Other LINE COLOR: BOTTOMED (brown) | 552 | 30% | +0.1% | 0.1 | 6% | +0.00% | +0.1% / +0.1% |  |
| Other LINE COLOR: WAKING UP (lime) | 4107 | 32% | +0.7% | 2.8 | 48% | +0.16% | +1.4% / +0.0% | ✅ |
| Stretched side: points dropped in the last 2 candles: rising / under 5 | 1887 | 34% | +1.0% | 2.8 | 64% | +0.28% | +1.6% / +0.3% | ✅ |
| Stretched side: points dropped in the last 2 candles: 5-15 | 5258 | 33% | +0.6% | 2.4 | 35% | +0.09% | +0.8% / +0.4% |  |
| Stretched side: points dropped in the last 2 candles: 15-30 | 6430 | 33% | +0.3% | 1.4 | 19% | +0.03% | +0.7% / -0.1% |  |
| Stretched side: points dropped in the last 2 candles: 30+ | 2624 | 33% | +0.8% | 1.9 | 35% | +0.13% | +1.3% / +0.2% |  |
| Other side: change in the last 2 candles: flat / falling | 3142 | 32% | +0.5% | 1.6 | 31% | +0.07% | +0.6% / +0.3% |  |
| Other side: change in the last 2 candles: up 5-15 | 4374 | 34% | +1.0% | 3.9 | 69% | +0.31% | +1.4% / +0.6% | ✅ |
| Other side: change in the last 2 candles: up 15-30 | 4700 | 33% | +0.2% | 0.8 | 12% | +0.01% | +0.7% / -0.3% |  |
| Other side: change in the last 2 candles: up 30+ | 3983 | 33% | +0.5% | 1.6 | 23% | +0.06% | +0.9% / +0.1% |  |
| Vix flow (greed + fear averages): YOUR way | 13654 | 33% | +0.5% | 2.9 | 31% | +0.08% | +0.9% / +0.2% | ✅ |
| Vix flow (greed + fear averages): none | 2345 | 32% | +0.5% | 2.0 | 40% | +0.10% | +0.9% / +0.2% |  |
| Vix flow (greed + fear averages): the RUN way | 200 | 33% | +0.5% | 0.5 | 42% | +0.10% | +1.9% / -0.8% |  |
| Lines GLOW (Vix flow + TTM agree): glow YOUR way | 11849 | 33% | +0.5% | 2.8 | 29% | +0.07% | +0.9% / +0.1% | ✅ |
| Lines GLOW (Vix flow + TTM agree): no glow | 4321 | 33% | +0.6% | 2.4 | 42% | +0.12% | +1.0% / +0.3% |  |
| TTM COLOR: RUN STILL PUSHING (cyan shorts / red longs) | 189 | 34% | +0.5% | 0.7 | 55% | +0.14% | +0.8% / +0.3% |  |
| TTM COLOR: RUN FADING (blue shorts / yellow longs) | 16001 | 33% | +0.6% | 3.2 | 32% | +0.08% | +0.9% / +0.2% | ✅ |
| TTM average peak before the turn (ATR): under 1.5 | 3560 | 34% | +0.3% | 1.0 | 17% | +0.02% | +0.9% / -0.3% |  |
| TTM average peak before the turn (ATR): 1.5-2 | 3854 | 33% | +0.8% | 2.6 | 43% | +0.15% | +1.1% / +0.4% | ✅ |
| TTM average peak before the turn (ATR): 2-3 | 5841 | 34% | +0.9% | 3.2 | 53% | +0.20% | +1.2% / +0.4% | ✅ |
| TTM average peak before the turn (ATR): 3+ | 2944 | 31% | -0.0% | -0.0 | 0% | +0.00% | +0.1% / -0.2% |  |
| TREND LINE COLOR: RUN SIDE STRONG (green shorts / red longs) | 8966 | 32% | +0.3% | 1.4 | 17% | +0.02% | +0.6% / -0.1% |  |
| TREND LINE COLOR: RUN SIDE FADING (blue shorts / pink longs) | 1406 | 33% | +1.4% | 2.6 | 81% | +0.48% | +1.7% / +1.1% | ✅ |
| TREND LINE COLOR: GRAY | 4210 | 36% | +0.7% | 2.7 | 46% | +0.16% | +0.8% / +0.7% | ✅ |
| TREND LINE COLOR: YOUR SIDE FADING (pink shorts / blue longs) | 121 | 31% | -1.4% | -2.5 | 0% | +0.00% | -1.8% / -1.2% |  |
| TREND LINE COLOR: YOUR SIDE STRONG (red shorts / green longs) | 1496 | 32% | +1.0% | 1.6 | 41% | +0.18% | +2.7% / -0.6% |  |
| Price vs trend line (ATR): through it to YOUR side | 6234 | 34% | +0.9% | 3.3 | 43% | +0.18% | +1.3% / +0.5% | ✅ |
| Price vs trend line (ATR): at the line | 4891 | 33% | +0.4% | 1.7 | 27% | +0.05% | +0.9% / -0.1% |  |
| Price vs trend line (ATR): 0.25-1 ATR on the run side | 4153 | 32% | +0.3% | 1.3 | 21% | +0.03% | +0.6% / +0.0% |  |
| Price vs trend line (ATR): 1+ ATR on the run side | 921 | 34% | +0.1% | 0.3 | 9% | +0.01% | +0.3% / -0.1% |  |
| Trend line angle (+ = the run's way): your way 5+ | 43 | 37% | +1.5% | 0.4 | 34% | +0.25% | +8.7% / -6.0% |  |
| Trend line angle (+ = the run's way): flat (-5 to +5) | 6409 | 33% | +0.6% | 2.7 | 35% | +0.11% | +1.0% / +0.3% | ✅ |
| Trend line angle (+ = the run's way): run way 5-15 | 8849 | 33% | +0.5% | 2.3 | 30% | +0.07% | +1.0% / -0.1% |  |
| Trend line angle (+ = the run's way): run way 15+ | 898 | 31% | +0.6% | 0.8 | 29% | +0.09% | -0.0% / +1.4% |  |
| TTM squeeze: ON | 1129 | 31% | +0.2% | 0.3 | 8% | +0.01% | +1.6% / -1.3% |  |
| TTM squeeze: just fired | 112 | 38% | +3.1% | 1.6 | 100% | +1.79% | +4.6% / +1.7% |  |
| TTM squeeze: off | 14958 | 33% | +0.6% | 3.2 | 33% | +0.09% | +0.9% / +0.3% | ✅ |
| Price vs VWAP (ATR, + = run side): your side | 3938 | 35% | +0.6% | 2.3 | 48% | +0.15% | +1.3% / +0.0% |  |
| Price vs VWAP (ATR, + = run side): -1 to +1 | 3952 | 33% | +0.8% | 2.1 | 30% | +0.12% | +0.8% / +0.8% |  |
| Price vs VWAP (ATR, + = run side): +1 to +3 | 3638 | 31% | +0.5% | 1.4 | 24% | +0.05% | +0.9% / +0.1% |  |
| Price vs VWAP (ATR, + = run side): +3 or more | 4671 | 33% | +0.3% | 1.4 | 30% | +0.04% | +0.8% / -0.2% |  |
| The move into the diamond (last 20 candles, $): under $0.75 | 1270 | 36% | +0.8% | 3.9 | 100% | +0.63% | +0.9% / +0.8% | ✅ |
| The move into the diamond (last 20 candles, $): $0.75-1.50 | 4742 | 36% | +0.8% | 3.9 | 100% | +0.38% | +1.0% / +0.5% | ✅ |
| The move into the diamond (last 20 candles, $): $1.50-3 | 6144 | 33% | +0.5% | 2.3 | 32% | +0.08% | +1.1% / +0.0% |  |
| The move into the diamond (last 20 candles, $): $3+ | 4043 | 29% | +0.2% | 0.4 | 5% | +0.00% | +0.5% / -0.1% |  |
| Price already came back from the extreme ($): under $0.20 | 1259 | 33% | +0.5% | 1.9 | 89% | +0.20% | +0.7% / +0.2% |  |
| Price already came back from the extreme ($): $0.20-0.50 | 4759 | 34% | +0.7% | 3.9 | 92% | +0.30% | +0.9% / +0.5% | ✅ |
| Price already came back from the extreme ($): $0.50-1 | 5685 | 34% | +0.7% | 3.2 | 48% | +0.15% | +1.1% / +0.2% | ✅ |
| Price already came back from the extreme ($): $1+ | 4496 | 30% | +0.3% | 0.6 | 7% | +0.01% | +0.9% / -0.2% |  |
| Day so far: net move / range: round trips (under 30%) | 5052 | 33% | +0.4% | 1.7 | 24% | +0.05% | +0.5% / +0.4% |  |
| Day so far: net move / range: 30-60% | 5959 | 33% | +0.7% | 2.8 | 40% | +0.13% | +1.3% / +0.1% | ✅ |
| Day so far: net move / range: trending (60%+) | 5188 | 33% | +0.4% | 1.7 | 32% | +0.07% | +0.9% / -0.0% |  |
| Diamond vs the day's move so far: WITH the day | 6145 | 35% | +0.6% | 2.5 | 40% | +0.11% | +1.1% / +0.1% | ✅ |
| Diamond vs the day's move so far: AGAINST the day | 10054 | 32% | +0.5% | 2.2 | 28% | +0.07% | +0.8% / +0.2% |  |
| REAL VIX today (VIXY vs yesterday): down | 9083 | 33% | +0.7% | 3.1 | 42% | +0.14% | +0.8% / +0.6% | ✅ |
| REAL VIX today (VIXY vs yesterday): up 0-3% | 5234 | 33% | +0.1% | 0.3 | 4% | +0.00% | +0.7% / -0.5% |  |
| REAL VIX today (VIXY vs yesterday): up 3%+ | 1882 | 33% | +1.1% | 1.8 | 59% | +0.30% | +1.9% / -0.1% |  |
| REAL VIX vs its 20-day average: LOW (5%+ under) | 6299 | 32% | +0.4% | 1.7 | 28% | +0.06% | +0.3% / +0.5% |  |
| REAL VIX vs its 20-day average: normal | 7312 | 34% | +0.4% | 1.6 | 21% | +0.04% | +0.9% / -0.2% |  |
| REAL VIX vs its 20-day average: HIGH (5%+ over) | 2588 | 34% | +1.3% | 2.5 | 65% | +0.40% | +2.0% / -0.0% |  |
| Options today: 9:45 ATM straddle vs the last 20 days' real move: CHEAP (under 0.8x) | 2430 | 32% | +0.4% | 1.1 | 28% | +0.05% | +0.5% / +0.2% |  |
| Options today: 9:45 ATM straddle vs the last 20 days' real move: fair (0.8-1.2x) | 7267 | 33% | +0.4% | 1.8 | 28% | +0.06% | +0.5% / +0.3% |  |
| Options today: 9:45 ATM straddle vs the last 20 days' real move: RICH (over 1.2x) | 6007 | 34% | +0.7% | 2.6 | 36% | +0.12% | +1.5% / -0.1% |  |
| Options today: 9:45 ATM straddle vs the last 20 days' real move: unknown (before 9:45) | 495 | 35% | +1.2% | 0.6 | 55% | +0.28% | +1.6% / -0.0% |  |

**Best pairs for this combination (12 shown):**
| Readings | Trades | Win % | Avg return | t | Kelly | Growth / trade | 1st / 2nd half |
|---|---|---|---|---|---|---|---|
| Stretched side: points dropped in the last 2 candles: rising / under 5 + Other side: change in the last 2 candles: up 30+ | 148 | 43% | +3.9% | 2.5 | 100% | +2.66% | +5.1% / +2.6% |
| Price vs VWAP (ATR, + = run side): -1 to +1 + Price already came back from the extreme ($): under $0.20 | 133 | 47% | +2.7% | 3.2 | 100% | +2.27% | +2.1% / +3.4% |
| Stretched side: points dropped in the last 2 candles: rising / under 5 + Price vs trend line (ATR): through it to YOUR side | 340 | 41% | +3.0% | 2.7 | 100% | +1.81% | +4.4% / +1.7% |
| Other LINE COLOR: WAKING UP (lime) + REAL VIX vs its 20-day average: HIGH (5%+ over) | 610 | 37% | +2.9% | 3.2 | 100% | +1.70% | +3.2% / +2.5% |
| Stretched side: points dropped in the last 2 candles: 30+ + REAL VIX vs its 20-day average: HIGH (5%+ over) | 391 | 37% | +3.3% | 2.6 | 100% | +1.59% | +4.2% / +1.6% |
| TTM squeeze: ON + The move into the diamond (last 20 candles, $): under $0.75 | 243 | 39% | +1.8% | 2.9 | 100% | +1.39% | +2.3% / +0.9% |
| Other LINE COLOR: SURGING (blue greed / red fear) + Stretched side: points dropped in the last 2 candles: 30+ | 565 | 38% | +2.7% | 2.8 | 100% | +1.36% | +3.2% / +2.1% |
| Other side: change in the last 2 candles: up 5-15 + REAL VIX vs its 20-day average: HIGH (5%+ over) | 661 | 37% | +2.5% | 3.1 | 100% | +1.36% | +3.1% / +1.4% |
| Other side now: 20-35 + REAL VIX vs its 20-day average: HIGH (5%+ over) | 767 | 34% | +2.6% | 3.1 | 100% | +1.36% | +3.5% / +0.9% |
| Price already came back from the extreme ($): $0.50-1 + REAL VIX vs its 20-day average: HIGH (5%+ over) | 840 | 38% | +2.1% | 3.6 | 100% | +1.31% | +2.7% / +1.0% |
| Stretched side: points dropped in the last 2 candles: rising / under 5 + Trend line angle (+ = the run's way): flat (-5 to +5) | 757 | 38% | +2.2% | 3.5 | 100% | +1.29% | +3.5% / +1.0% |
| Stretched side's peak, last 10 candles: 70-85 + The move into the diamond (last 20 candles, $): under $0.75 | 285 | 39% | +1.5% | 3.2 | 100% | +1.22% | +1.4% / +1.7% |
- BLIND, picked on the 1st half: Other side MAXED (95+) in the last 30 candles: no + Day so far: net move / range: 30-60% (t 4.5) -> other half: **1734 trades, 31% win, +0.1%/trade, Kelly 5%** (t 0.2) 
- BLIND, picked on the 2nd half: Other side: change in the last 2 candles: up 5-15 + REAL VIX vs its 20-day average: LOW (5%+ under) (t 2.7) -> other half: **693 trades, 34% win, +0.5%/trade, Kelly 36%** (t 0.7) 

### TUNED / SPY+QQQ ALL timeframes / AT THE DIAMOND / LINE OR STRUCTURE / ATM 0DTE
| Reading | Trades | Win % | Avg return | t | Kelly | Growth / trade | 1st / 2nd half | |
|---|---|---|---|---|---|---|---|---|

### YOURS / SPY+QQQ ALL timeframes / AT THE DIAMOND / LINE OR STRUCTURE / ATM 0DTE
| Reading | Trades | Win % | Avg return | t | Kelly | Growth / trade | 1st / 2nd half | |
|---|---|---|---|---|---|---|---|---|

**Luck check:** thousands of combinations and filters are scored, so some look great by chance. The BLIND TESTS (picked on one half, judged on the other) are what count.

