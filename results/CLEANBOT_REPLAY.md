# Clean Scan replay

Data only. No order is sent. The live Clean Scan bot and its schedule are unchanged.

Log: 34 sales, 26 entries, 2026-10-21, 2026-10-22, 2026-10-23.
30 of 34 sales traded green at some point (best_pct > 0). 18 of those 30 closed at a loss. Stops and scan exits (leg got choppy, trend flipped) gave back more than the take-profits kept.

34 sales over 3 days is far too small to conclude anything. The intervals are a 95% bootstrap of the entry dollars (2,000 resamples, seed 20261025). They describe this sample. They are not a reason to change the bot.

Costs, same model as scalp_real: the entry is the logged fill plus a half-spread, the exit is the replay fill minus a half-spread, half-spread = max(1 cent, 0.5% of premium) per side, commission $0.65 per contract per side. Logged dollars are paper fills with no commission, so the replay dollars will not equal the log even when the rule matches.
Stops and targets are measured from the logged fill. If one 1-minute bar touches the active stop and a target, the stop is filled. A trail that arms on this bar's high and is then broken by this bar's low stops out. The live bot checks a quote mid every 5 seconds. This replay only has 1-minute highs and lows, so some exits cannot match. Those rows are flagged.

## Does the replay reproduce the log?

The scan clock is cleanbot.scan on IEX 5-minute bars (the feed the bot trades on). Option bars are Alpaca OPRA 1-minute bars from the entry minute through 15:59 ET.

Flags: cost drag 1, mismatch 6, price gap 19. Logged total $-1,264. Replay raw (no spread, no commission) $-854. Replay net $-1,100.
match = same exit class, within 1 minute, and the raw dollars are close. price gap = the rule matched but the bar price is not the paper fill. cost drag = the raw dollars match and the spread plus commission is the gap. mismatch = a different exit or a different minute. no bars = nothing to replay.

| day | v | sym | in | best | log | log $ | replay | replay $ | flag |
|---|---|---|---|---:|---|---:|---|---:|---|
| 10-21 | A | TSLA | 12:45 | 0% | choppy | -140 | choppy | -146 | price gap |
| 10-21 | B | TSLA | 12:45 | 2% | choppy | -125 | choppy | -125 | price gap |
| 10-21 | B | QQQ | 15:00 | 21% | tp1 + tp2 | +29 | tp2 | +35 | mismatch |
| 10-21 | A | QQQ | 15:00 | 78% | tp1 + stop | +18 | tp1 + stop | -7 | price gap |
| 10-22 | B | SPY | 10:00 | 4% | stop | -24 | stop | -32 | price gap |
| 10-22 | A | SPY | 10:00 | 214% | tp1 + choppy | +175 | tp1 + choppy | +170 | cost drag |
| 10-22 | B | PLTR | 10:30 | 16% | tp1 + stop | -5 | tp1 + stop | -7 | price gap |
| 10-22 | A | PLTR | 10:30 | 16% | stop | -114 | choppy | +33 | mismatch |
| 10-22 | B | AMZN | 11:15 | 0% | stop | -22 | stop | -22 | price gap |
| 10-22 | A | AMZN | 11:15 | 0% | choppy | -70 | choppy | -71 | price gap |
| 10-22 | B | META | 11:55 | 3% | stop | -200 | stop | -161 | price gap |
| 10-22 | A | META | 11:55 | 1% | flip | -230 | flip | -221 | price gap |
| 10-22 | B | META | 12:45 | 13% | tp1 + stop | -15 | tp1 + stop | -16 | mismatch |
| 10-22 | B | COIN | 12:55 | 0% | stop | -50 | stop | -49 | price gap |
| 10-22 | B | QQQ | 13:05 | 9% | stop | -32 | stop | -31 | price gap |
| 10-22 | B | SPY | 13:10 | 5% | stop | -22 | stop | -27 | price gap |
| 10-22 | A | SPY | 13:10 | 4% | stop | -64 | stop | -69 | price gap |
| 10-22 | A | QQQ | 13:05 | 12% | stop | -94 | stop | -87 | mismatch |
| 10-22 | A | META | 12:45 | 15% | choppy | -150 | choppy | -102 | price gap |
| 10-22 | A | COIN | 12:55 | 25% | tp1 + choppy | +54 | choppy | +8 | mismatch |
| 10-22 | B | GOOGL | 14:50 | 14% | tp1 + stop | -12 | tp1 + stop | -7 | price gap |
| 10-22 | B | AMZN | 15:15 | 17% | tp1 + stop | -1 | tp1 + stop | -8 | mismatch |
| 10-22 | A | AMZN | 15:15 | 13% | stop | -90 | stop | -91 | price gap |
| 10-22 | A | GOOGL | 14:50 | 14% | 15:45 | +26 | 15:45 | +25 | price gap |
| 10-23 | B | COIN | 10:30 | 0% | stop | -18 | stop | -19 | price gap |
| 10-23 | A | COIN | 10:30 | 1% | stop | -88 | stop | -75 | price gap |

## Exit variants

Each variant starts from the same logged entries and contract counts. A and B keep their own stops except where the variant says otherwise.
- **current**: Current bot rules (stop, scale-out, scan exit, 15:45)
- **fixed**: Fixed stop and target only (A sells all at +25/-25; B is +10 then +20 / -10)
- **no_scan**: Current scale-out with scan exits turned off (15:45 still flats)
- **breakeven**: After +10%, stop moves to the entry price (costs still apply)
- **trail50**: After +10%, exit on a 50% giveback of the peak gain
- **trail30**: After +15%, exit on a 30% giveback of the peak gain
- **partial10**: Sell half at +10%, trail the rest at a 50% giveback
- **time5**: Exit 5 minutes after entry
- **time10**: Exit 10 minutes after entry
- **time15**: Exit 15 minutes after entry
- **time30**: Exit 30 minutes after entry

A fixed target sells both contracts at +25%. The current A rule sells one at +25% and leaves the other on until a scan exit or 15:45. no_scan is that current rule with the scan turned off. Breakeven moves the stop to the entry price, and the spread and commission still come out, so that exit is a small loss.

## Totals

### current

| slice | n | wins | net $ | avg % | max DD | 95% CI |
|---|---:|---:|---:|---:|---:|---|
| all | 26 | 5 | $-1,100 | -7.5% | $-1,021 | $-1,812 to $-330 |
| version A | 13 | 4 | $-632 | -7.4% | $-682 | $-1,267 to $+81 |
| version B | 13 | 1 | $-468 | -7.7% | $-377 | $-827 to $-151 |
| 2026-10-21 | 4 | 1 | $-244 | +0.1% | $-125 | $-543 to $+56 |
| 2026-10-22 | 20 | 4 | $-763 | -7.6% | $-952 | $-1,415 to $-79 |
| 2026-10-23 | 2 | 0 | $-94 | -22.5% | $-75 | $-150 to $-37 |
| 2026-10-21 A | 2 | 0 | $-153 | -4.7% | $-6.60 | $-293 to $-13 |
| 2026-10-21 B | 2 | 1 | $-91 | +4.9% | $+0.00 | $-250 to $+69 |
| 2026-10-22 A | 10 | 4 | $-404 | -5.9% | $-632 | $-1,003 to $+228 |
| 2026-10-22 B | 10 | 0 | $-359 | -9.2% | $-327 | $-661 to $-159 |
| 2026-10-23 A | 1 | 0 | $-75 | -27.2% | $+0.00 | $-75 to $-75 |
| 2026-10-23 B | 1 | 0 | $-19 | -17.9% | $+0.00 | $-19 to $-19 |

| day | v | sym | out | why | net $ |
|---|---|---|---|---|---:|
| 10-21 | A | TSLA | 12:50 | choppy | -146 |
| 10-21 | B | TSLA | 12:50 | choppy | -125 |
| 10-21 | B | QQQ | 15:00 | tp2 | +35 |
| 10-21 | A | QQQ | 15:23 | tp1 + stop | -7 |
| 10-22 | B | SPY | 10:00 | stop | -32 |
| 10-22 | A | SPY | 11:25 | tp1 + choppy | +170 |
| 10-22 | B | PLTR | 10:32 | tp1 + stop | -7 |
| 10-22 | A | PLTR | 11:30 | choppy | +33 |
| 10-22 | B | AMZN | 11:16 | stop | -22 |
| 10-22 | A | AMZN | 11:25 | choppy | -71 |
| 10-22 | B | META | 11:57 | stop | -161 |
| 10-22 | A | META | 12:00 | flip | -221 |
| 10-22 | B | META | 13:01 | tp1 + stop | -16 |
| 10-22 | B | COIN | 13:00 | stop | -49 |
| 10-22 | B | QQQ | 13:10 | stop | -31 |
| 10-22 | B | SPY | 13:10 | stop | -27 |
| 10-22 | A | SPY | 13:15 | stop | -69 |
| 10-22 | A | QQQ | 13:15 | stop | -87 |
| 10-22 | A | META | 13:36 | choppy | -102 |
| 10-22 | A | COIN | 14:40 | choppy | +8 |
| 10-22 | B | GOOGL | 15:29 | tp1 + stop | -7 |
| 10-22 | B | AMZN | 15:25 | tp1 + stop | -8 |
| 10-22 | A | AMZN | 15:30 | stop | -91 |
| 10-22 | A | GOOGL | 15:45 | 15:45 | +25 |
| 10-23 | B | COIN | 10:30 | stop | -19 |
| 10-23 | A | COIN | 10:31 | stop | -75 |

### fixed

| slice | n | wins | net $ | avg % | max DD | 95% CI |
|---|---:|---:|---:|---:|---:|---|
| all | 26 | 5 | $-1,386 | -9.9% | $-1,170 | $-2,711 to $-47 |
| version A | 13 | 4 | $-838 | -11.9% | $-797 | $-2,059 to $+498 |
| version B | 13 | 1 | $-548 | -8.0% | $-377 | $-1,019 to $-151 |
| 2026-10-21 | 4 | 2 | $-367 | +3.8% | $-205 | $-933 to $+199 |
| 2026-10-22 | 20 | 3 | $-925 | -11.4% | $-1,110 | $-2,103 to $+341 |
| 2026-10-23 | 2 | 0 | $-94 | -22.5% | $-75 | $-150 to $-37 |
| 2026-10-21 A | 2 | 1 | $-197 | +4.9% | $+0.00 | $-524 to $+130 |
| 2026-10-21 B | 2 | 1 | $-170 | +2.7% | $+0.00 | $-410 to $+69 |
| 2026-10-22 A | 10 | 3 | $-566 | -13.7% | $-797 | $-1,724 to $+601 |
| 2026-10-22 B | 10 | 0 | $-359 | -9.2% | $-327 | $-661 to $-159 |
| 2026-10-23 A | 1 | 0 | $-75 | -27.2% | $+0.00 | $-75 to $-75 |
| 2026-10-23 B | 1 | 0 | $-19 | -17.9% | $+0.00 | $-19 to $-19 |

| day | v | sym | out | why | net $ |
|---|---|---|---|---|---:|
| 10-21 | A | TSLA | 15:45 | 15:45 | -262 |
| 10-21 | B | TSLA | 13:43 | stop | -205 |
| 10-21 | B | QQQ | 15:00 | tp2 | +35 |
| 10-21 | A | QQQ | 15:01 | tp1 | +65 |
| 10-22 | B | SPY | 10:00 | stop | -32 |
| 10-22 | A | SPY | 10:07 | tp1 | +77 |
| 10-22 | B | PLTR | 10:32 | tp1 + stop | -7 |
| 10-22 | A | PLTR | 12:27 | stop | -118 |
| 10-22 | B | AMZN | 11:16 | stop | -22 |
| 10-22 | A | AMZN | 11:56 | stop | -81 |
| 10-22 | B | META | 11:57 | stop | -161 |
| 10-22 | A | META | 12:02 | stop | -442 |
| 10-22 | B | META | 13:01 | tp1 + stop | -16 |
| 10-22 | B | COIN | 13:00 | stop | -49 |
| 10-22 | B | QQQ | 13:10 | stop | -31 |
| 10-22 | B | SPY | 13:10 | stop | -27 |
| 10-22 | A | SPY | 13:15 | stop | -69 |
| 10-22 | A | QQQ | 13:15 | stop | -87 |
| 10-22 | A | META | 14:30 | tp1 | +365 |
| 10-22 | A | COIN | 15:30 | stop | -145 |
| 10-22 | B | GOOGL | 15:29 | tp1 + stop | -7 |
| 10-22 | B | AMZN | 15:25 | tp1 + stop | -8 |
| 10-22 | A | AMZN | 15:30 | stop | -91 |
| 10-22 | A | GOOGL | 15:45 | 15:45 | +25 |
| 10-23 | B | COIN | 10:30 | stop | -19 |
| 10-23 | A | COIN | 10:31 | stop | -75 |

### no_scan

| slice | n | wins | net $ | avg % | max DD | 95% CI |
|---|---:|---:|---:|---:|---:|---|
| all | 26 | 4 | $-1,314 | -8.0% | $-1,211 | $-2,697 to $+193 |
| version A | 13 | 3 | $-767 | -7.9% | $-865 | $-2,063 to $+691 |
| version B | 13 | 1 | $-548 | -8.0% | $-377 | $-1,019 to $-151 |
| 2026-10-21 | 4 | 1 | $-439 | -2.4% | $-205 | $-933 to $+56 |
| 2026-10-22 | 20 | 3 | $-782 | -7.6% | $-1,142 | $-2,058 to $+581 |
| 2026-10-23 | 2 | 0 | $-94 | -22.5% | $-75 | $-150 to $-37 |
| 2026-10-21 A | 2 | 0 | $-268 | -7.5% | $-6.60 | $-524 to $-13 |
| 2026-10-21 B | 2 | 1 | $-170 | +2.7% | $+0.00 | $-410 to $+69 |
| 2026-10-22 A | 10 | 3 | $-423 | -6.1% | $-815 | $-1,632 to $+844 |
| 2026-10-22 B | 10 | 0 | $-359 | -9.2% | $-327 | $-661 to $-159 |
| 2026-10-23 A | 1 | 0 | $-75 | -27.2% | $+0.00 | $-75 to $-75 |
| 2026-10-23 B | 1 | 0 | $-19 | -17.9% | $+0.00 | $-19 to $-19 |

| day | v | sym | out | why | net $ |
|---|---|---|---|---|---:|
| 10-21 | A | TSLA | 15:45 | 15:45 | -262 |
| 10-21 | B | TSLA | 13:43 | stop | -205 |
| 10-21 | B | QQQ | 15:00 | tp2 | +35 |
| 10-21 | A | QQQ | 15:23 | tp1 + stop | -7 |
| 10-22 | B | SPY | 10:00 | stop | -32 |
| 10-22 | A | SPY | 15:45 | tp1 + 15:45 | +367 |
| 10-22 | B | PLTR | 10:32 | tp1 + stop | -7 |
| 10-22 | A | PLTR | 12:27 | stop | -118 |
| 10-22 | B | AMZN | 11:16 | stop | -22 |
| 10-22 | A | AMZN | 11:56 | stop | -81 |
| 10-22 | B | META | 11:57 | stop | -161 |
| 10-22 | A | META | 12:02 | stop | -442 |
| 10-22 | B | META | 13:01 | tp1 + stop | -16 |
| 10-22 | B | COIN | 13:00 | stop | -49 |
| 10-22 | B | QQQ | 13:10 | stop | -31 |
| 10-22 | B | SPY | 13:10 | stop | -27 |
| 10-22 | A | SPY | 13:15 | stop | -69 |
| 10-22 | A | QQQ | 13:15 | stop | -87 |
| 10-22 | A | META | 15:45 | tp1 + 15:45 | +218 |
| 10-22 | A | COIN | 15:30 | stop | -145 |
| 10-22 | B | GOOGL | 15:29 | tp1 + stop | -7 |
| 10-22 | B | AMZN | 15:25 | tp1 + stop | -8 |
| 10-22 | A | AMZN | 15:30 | stop | -91 |
| 10-22 | A | GOOGL | 15:45 | 15:45 | +25 |
| 10-23 | B | COIN | 10:30 | stop | -19 |
| 10-23 | A | COIN | 10:31 | stop | -75 |

### breakeven

| slice | n | wins | net $ | avg % | max DD | 95% CI |
|---|---:|---:|---:|---:|---:|---|
| all | 26 | 7 | $-1,125 | -4.7% | $-1,064 | $-2,426 to $+227 |
| version A | 13 | 2 | $-680 | -3.0% | $-815 | $-1,920 to $+550 |
| version B | 13 | 5 | $-444 | -6.4% | $-274 | $-958 to $-8.01 |
| 2026-10-21 | 4 | 2 | $-403 | +0.7% | $-205 | $-933 to $+127 |
| 2026-10-22 | 20 | 5 | $-628 | -4.0% | $-970 | $-1,828 to $+560 |
| 2026-10-23 | 2 | 0 | $-94 | -22.5% | $-75 | $-150 to $-37 |
| 2026-10-21 A | 2 | 1 | $-233 | -1.3% | $+0.00 | $-524 to $+58 |
| 2026-10-21 B | 2 | 1 | $-170 | +2.7% | $+0.00 | $-410 to $+69 |
| 2026-10-22 A | 10 | 1 | $-373 | -0.9% | $-739 | $-1,600 to $+791 |
| 2026-10-22 B | 10 | 4 | $-256 | -7.1% | $-240 | $-597 to $+37 |
| 2026-10-23 A | 1 | 0 | $-75 | -27.2% | $+0.00 | $-75 to $-75 |
| 2026-10-23 B | 1 | 0 | $-19 | -17.9% | $+0.00 | $-19 to $-19 |

| day | v | sym | out | why | net $ |
|---|---|---|---|---|---:|
| 10-21 | A | TSLA | 15:45 | 15:45 | -262 |
| 10-21 | B | TSLA | 13:43 | stop | -205 |
| 10-21 | B | QQQ | 15:00 | tp2 | +35 |
| 10-21 | A | QQQ | 15:15 | tp1 + breakeven | +29 |
| 10-22 | B | SPY | 10:00 | stop | -32 |
| 10-22 | A | SPY | 15:45 | tp1 + 15:45 | +367 |
| 10-22 | B | PLTR | 10:31 | tp1 + breakeven | +7 |
| 10-22 | A | PLTR | 10:31 | breakeven | -7 |
| 10-22 | B | AMZN | 11:16 | stop | -22 |
| 10-22 | A | AMZN | 11:56 | stop | -81 |
| 10-22 | B | META | 11:57 | stop | -161 |
| 10-22 | A | META | 12:02 | stop | -442 |
| 10-22 | B | META | 12:57 | tp1 + breakeven | +51 |
| 10-22 | B | COIN | 13:00 | stop | -49 |
| 10-22 | B | QQQ | 13:10 | stop | -31 |
| 10-22 | B | SPY | 13:10 | stop | -27 |
| 10-22 | A | SPY | 13:15 | stop | -69 |
| 10-22 | A | QQQ | 13:15 | stop | -87 |
| 10-22 | A | META | 13:00 | breakeven | -18 |
| 10-22 | A | COIN | 13:18 | breakeven | -16 |
| 10-22 | B | GOOGL | 15:12 | tp1 + breakeven | +7 |
| 10-22 | B | AMZN | 15:18 | tp1 + breakeven | +2 |
| 10-22 | A | AMZN | 15:20 | breakeven | -7 |
| 10-22 | A | GOOGL | 15:13 | breakeven | -13 |
| 10-23 | B | COIN | 10:30 | stop | -19 |
| 10-23 | A | COIN | 10:31 | stop | -75 |

### trail50

| slice | n | wins | net $ | avg % | max DD | 95% CI |
|---|---:|---:|---:|---:|---:|---|
| all | 26 | 12 | $-1,155 | -6.0% | $-950 | $-2,372 to $-127 |
| version A | 13 | 7 | $-813 | -8.4% | $-679 | $-1,888 to $+57 |
| version B | 13 | 5 | $-342 | -3.6% | $-231 | $-916 to $+181 |
| 2026-10-21 | 4 | 2 | $-354 | +6.9% | $-205 | $-933 to $+226 |
| 2026-10-22 | 20 | 10 | $-707 | -7.0% | $-891 | $-1,747 to $+108 |
| 2026-10-23 | 2 | 0 | $-94 | -22.5% | $-75 | $-150 to $-37 |
| 2026-10-21 A | 2 | 1 | $-241 | -2.8% | $+0.00 | $-524 to $+41 |
| 2026-10-21 B | 2 | 1 | $-112 | +16.6% | $+0.00 | $-410 to $+185 |
| 2026-10-22 A | 10 | 6 | $-496 | -7.7% | $-679 | $-1,507 to $+192 |
| 2026-10-22 B | 10 | 4 | $-211 | -6.2% | $-212 | $-580 to $+124 |
| 2026-10-23 A | 1 | 0 | $-75 | -27.2% | $+0.00 | $-75 to $-75 |
| 2026-10-23 B | 1 | 0 | $-19 | -17.9% | $+0.00 | $-19 to $-19 |

| day | v | sym | out | why | net $ |
|---|---|---|---|---|---:|
| 10-21 | A | TSLA | 15:45 | 15:45 | -262 |
| 10-21 | B | TSLA | 13:43 | stop | -205 |
| 10-21 | B | QQQ | 15:04 | trail50 | +92 |
| 10-21 | A | QQQ | 15:01 | trail50 | +20 |
| 10-22 | B | SPY | 10:00 | stop | -32 |
| 10-22 | A | SPY | 10:07 | trail50 | +31 |
| 10-22 | B | PLTR | 10:31 | trail50 | +12 |
| 10-22 | A | PLTR | 10:31 | trail50 | +21 |
| 10-22 | B | AMZN | 11:16 | stop | -22 |
| 10-22 | A | AMZN | 11:56 | stop | -81 |
| 10-22 | B | META | 11:57 | stop | -161 |
| 10-22 | A | META | 12:02 | stop | -442 |
| 10-22 | B | META | 12:56 | trail50 | +79 |
| 10-22 | B | COIN | 13:00 | stop | -49 |
| 10-22 | B | QQQ | 13:10 | stop | -31 |
| 10-22 | B | SPY | 13:10 | stop | -27 |
| 10-22 | A | SPY | 13:15 | stop | -69 |
| 10-22 | A | QQQ | 13:15 | stop | -87 |
| 10-22 | A | META | 12:56 | trail50 | +88 |
| 10-22 | A | COIN | 13:17 | trail50 | +4 |
| 10-22 | B | GOOGL | 15:10 | trail50 | +12 |
| 10-22 | B | AMZN | 15:17 | trail50 | +7 |
| 10-22 | A | AMZN | 15:17 | trail50 | +17 |
| 10-22 | A | GOOGL | 15:10 | trail50 | +21 |
| 10-23 | B | COIN | 10:30 | stop | -19 |
| 10-23 | A | COIN | 10:31 | stop | -75 |

### trail30

| slice | n | wins | net $ | avg % | max DD | 95% CI |
|---|---:|---:|---:|---:|---:|---|
| all | 26 | 8 | $-1,436 | -8.8% | $-1,217 | $-2,656 to $-348 |
| version A | 13 | 6 | $-731 | -8.4% | $-679 | $-1,834 to $+257 |
| version B | 13 | 2 | $-705 | -9.3% | $-524 | $-1,199 to $-269 |
| 2026-10-21 | 4 | 2 | $-411 | -0.4% | $-205 | $-933 to $+111 |
| 2026-10-22 | 20 | 6 | $-931 | -9.1% | $-1,119 | $-1,984 to $-7.26 |
| 2026-10-23 | 2 | 0 | $-94 | -22.5% | $-75 | $-150 to $-37 |
| 2026-10-21 A | 2 | 1 | $-231 | -1.0% | $+0.00 | $-524 to $+62 |
| 2026-10-21 B | 2 | 1 | $-181 | +0.2% | $+0.00 | $-410 to $+48 |
| 2026-10-22 A | 10 | 5 | $-426 | -7.9% | $-679 | $-1,469 to $+390 |
| 2026-10-22 B | 10 | 1 | $-506 | -10.3% | $-487 | $-874 to $-209 |
| 2026-10-23 A | 1 | 0 | $-75 | -27.2% | $+0.00 | $-75 to $-75 |
| 2026-10-23 B | 1 | 0 | $-19 | -17.9% | $+0.00 | $-19 to $-19 |

| day | v | sym | out | why | net $ |
|---|---|---|---|---|---:|
| 10-21 | A | TSLA | 15:45 | 15:45 | -262 |
| 10-21 | B | TSLA | 13:43 | stop | -205 |
| 10-21 | B | QQQ | 15:01 | trail30 | +24 |
| 10-21 | A | QQQ | 15:01 | trail30 | +31 |
| 10-22 | B | SPY | 10:00 | stop | -32 |
| 10-22 | A | SPY | 10:07 | trail30 | +47 |
| 10-22 | B | PLTR | 10:32 | trail30 | -15 |
| 10-22 | A | PLTR | 11:31 | trail30 | +51 |
| 10-22 | B | AMZN | 11:16 | stop | -22 |
| 10-22 | A | AMZN | 11:56 | stop | -81 |
| 10-22 | B | META | 11:57 | stop | -161 |
| 10-22 | A | META | 12:02 | stop | -442 |
| 10-22 | B | META | 13:01 | stop | -149 |
| 10-22 | B | COIN | 13:00 | stop | -49 |
| 10-22 | B | QQQ | 13:10 | stop | -31 |
| 10-22 | B | SPY | 13:10 | stop | -27 |
| 10-22 | A | SPY | 13:15 | stop | -69 |
| 10-22 | A | QQQ | 13:15 | stop | -87 |
| 10-22 | A | META | 14:09 | trail30 | +152 |
| 10-22 | A | COIN | 14:18 | trail30 | +70 |
| 10-22 | B | GOOGL | 15:29 | stop | -33 |
| 10-22 | B | AMZN | 15:17 | trail30 | +13 |
| 10-22 | A | AMZN | 15:30 | stop | -91 |
| 10-22 | A | GOOGL | 15:45 | 15:45 | +25 |
| 10-23 | B | COIN | 10:30 | stop | -19 |
| 10-23 | A | COIN | 10:31 | stop | -75 |

### partial10

| slice | n | wins | net $ | avg % | max DD | 95% CI |
|---|---:|---:|---:|---:|---:|---|
| all | 26 | 12 | $-1,103 | -6.2% | $-959 | $-2,351 to $-55 |
| version A | 13 | 7 | $-750 | -7.7% | $-679 | $-1,860 to $+139 |
| version B | 13 | 5 | $-352 | -4.6% | $-208 | $-915 to $+148 |
| 2026-10-21 | 4 | 2 | $-392 | +2.2% | $-205 | $-933 to $+149 |
| 2026-10-22 | 20 | 10 | $-617 | -6.2% | $-872 | $-1,700 to $+229 |
| 2026-10-23 | 2 | 0 | $-94 | -22.5% | $-75 | $-150 to $-37 |
| 2026-10-21 A | 2 | 1 | $-241 | -2.7% | $+0.00 | $-524 to $+42 |
| 2026-10-21 B | 2 | 1 | $-152 | +7.2% | $+0.00 | $-410 to $+106 |
| 2026-10-22 A | 10 | 6 | $-435 | -6.7% | $-679 | $-1,464 to $+301 |
| 2026-10-22 B | 10 | 4 | $-182 | -5.7% | $-192 | $-567 to $+184 |
| 2026-10-23 A | 1 | 0 | $-75 | -27.2% | $+0.00 | $-75 to $-75 |
| 2026-10-23 B | 1 | 0 | $-19 | -17.9% | $+0.00 | $-19 to $-19 |

| day | v | sym | out | why | net $ |
|---|---|---|---|---|---:|
| 10-21 | A | TSLA | 15:45 | 15:45 | -262 |
| 10-21 | B | TSLA | 13:43 | stop | -205 |
| 10-21 | B | QQQ | 15:04 | half + trail50 | +53 |
| 10-21 | A | QQQ | 15:01 | half + trail50 | +21 |
| 10-22 | B | SPY | 10:00 | stop | -32 |
| 10-22 | A | SPY | 10:07 | half + trail50 | +29 |
| 10-22 | B | PLTR | 10:31 | half + trail50 | +16 |
| 10-22 | A | PLTR | 10:31 | half + trail50 | +29 |
| 10-22 | B | AMZN | 11:16 | stop | -22 |
| 10-22 | A | AMZN | 11:56 | stop | -81 |
| 10-22 | B | META | 11:57 | stop | -161 |
| 10-22 | A | META | 12:02 | stop | -442 |
| 10-22 | B | META | 12:56 | half + trail50 | +98 |
| 10-22 | B | COIN | 13:00 | stop | -49 |
| 10-22 | B | QQQ | 13:10 | stop | -31 |
| 10-22 | B | SPY | 13:10 | stop | -27 |
| 10-22 | A | SPY | 13:15 | stop | -69 |
| 10-22 | A | QQQ | 13:15 | stop | -87 |
| 10-22 | A | META | 12:56 | half + trail50 | +112 |
| 10-22 | A | COIN | 13:17 | half + trail50 | +23 |
| 10-22 | B | GOOGL | 15:10 | half + trail50 | +16 |
| 10-22 | B | AMZN | 15:17 | half + trail50 | +9 |
| 10-22 | A | AMZN | 15:17 | half + trail50 | +22 |
| 10-22 | A | GOOGL | 15:10 | half + trail50 | +29 |
| 10-23 | B | COIN | 10:30 | stop | -19 |
| 10-23 | A | COIN | 10:31 | stop | -75 |

### time5

| slice | n | wins | net $ | avg % | max DD | 95% CI |
|---|---:|---:|---:|---:|---:|---|
| all | 26 | 5 | $-1,104 | -8.0% | $-1,019 | $-1,773 to $-460 |
| version A | 13 | 2 | $-626 | -7.2% | $-582 | $-1,158 to $-119 |
| version B | 13 | 3 | $-478 | -8.8% | $-438 | $-896 to $-66 |
| 2026-10-21 | 4 | 2 | $-85 | +15.6% | $-125 | $-543 to $+374 |
| 2026-10-22 | 20 | 3 | $-916 | -10.7% | $-872 | $-1,446 to $-483 |
| 2026-10-23 | 2 | 0 | $-103 | -28.5% | $-71 | $-141 to $-65 |
| 2026-10-21 A | 2 | 1 | $-45 | +14.0% | $+0.00 | $-293 to $+203 |
| 2026-10-21 B | 2 | 1 | $-40 | +17.1% | $+0.00 | $-250 to $+171 |
| 2026-10-22 A | 10 | 1 | $-511 | -9.6% | $-462 | $-935 to $-211 |
| 2026-10-22 B | 10 | 2 | $-405 | -11.7% | $-364 | $-739 to $-170 |
| 2026-10-23 A | 1 | 0 | $-71 | -25.6% | $+0.00 | $-71 to $-71 |
| 2026-10-23 B | 1 | 0 | $-33 | -31.3% | $+0.00 | $-33 to $-33 |

| day | v | sym | out | why | net $ |
|---|---|---|---|---|---:|
| 10-21 | A | TSLA | 12:50 | +5m | -146 |
| 10-21 | B | TSLA | 12:50 | +5m | -125 |
| 10-21 | B | QQQ | 15:05 | +5m | +85 |
| 10-21 | A | QQQ | 15:05 | +5m | +101 |
| 10-22 | B | SPY | 10:05 | +5m | -45 |
| 10-22 | A | SPY | 10:05 | +5m | -49 |
| 10-22 | B | PLTR | 10:35 | +5m | -21 |
| 10-22 | A | PLTR | 10:35 | +5m | -21 |
| 10-22 | B | AMZN | 11:20 | +5m | -41 |
| 10-22 | A | AMZN | 11:20 | +5m | -59 |
| 10-22 | B | META | 12:00 | +5m | -176 |
| 10-22 | A | META | 12:00 | +5m | -221 |
| 10-22 | B | META | 12:50 | +5m | +4 |
| 10-22 | B | COIN | 13:00 | +5m | -49 |
| 10-22 | B | QQQ | 13:10 | +5m | -19 |
| 10-22 | B | SPY | 13:15 | +5m | -47 |
| 10-22 | A | SPY | 13:15 | +5m | -61 |
| 10-22 | A | QQQ | 13:10 | +5m | -15 |
| 10-22 | A | META | 12:50 | +5m | -10 |
| 10-22 | A | COIN | 13:00 | +5m | -55 |
| 10-22 | B | GOOGL | 14:55 | +5m | -17 |
| 10-22 | B | AMZN | 15:20 | +5m | +3 |
| 10-22 | A | AMZN | 15:20 | +5m | +3 |
| 10-22 | A | GOOGL | 14:55 | +5m | -25 |
| 10-23 | B | COIN | 10:35 | +5m | -33 |
| 10-23 | A | COIN | 10:35 | +5m | -71 |

### time10

| slice | n | wins | net $ | avg % | max DD | 95% CI |
|---|---:|---:|---:|---:|---:|---|
| all | 26 | 10 | $-1,277 | -9.3% | $-1,371 | $-2,938 to $+112 |
| version A | 13 | 5 | $-705 | -8.3% | $-798 | $-2,015 to $+315 |
| version B | 13 | 5 | $-573 | -10.4% | $-604 | $-1,670 to $+278 |
| 2026-10-21 | 4 | 2 | $-53 | +11.5% | $-93 | $-380 to $+274 |
| 2026-10-22 | 20 | 8 | $-1,043 | -9.4% | $-1,320 | $-2,712 to $+310 |
| 2026-10-23 | 2 | 0 | $-181 | -50.4% | $-123 | $-245 to $-117 |
| 2026-10-21 A | 2 | 1 | $-21 | +10.7% | $+0.00 | $-193 to $+151 |
| 2026-10-21 B | 2 | 1 | $-32 | +12.2% | $+0.00 | $-187 to $+123 |
| 2026-10-22 A | 10 | 4 | $-561 | -8.4% | $-798 | $-1,807 to $+341 |
| 2026-10-22 B | 10 | 4 | $-482 | -10.3% | $-550 | $-1,534 to $+280 |
| 2026-10-23 A | 1 | 0 | $-123 | -44.4% | $+0.00 | $-123 to $-123 |
| 2026-10-23 B | 1 | 0 | $-59 | -56.3% | $+0.00 | $-59 to $-59 |

| day | v | sym | out | why | net $ |
|---|---|---|---|---|---:|
| 10-21 | A | TSLA | 12:55 | +10m | -97 |
| 10-21 | B | TSLA | 12:55 | +10m | -93 |
| 10-21 | B | QQQ | 15:10 | +10m | +61 |
| 10-21 | A | QQQ | 15:10 | +10m | +75 |
| 10-22 | B | SPY | 10:10 | +10m | +63 |
| 10-22 | A | SPY | 10:10 | +10m | +83 |
| 10-22 | B | PLTR | 10:40 | +10m | -15 |
| 10-22 | A | PLTR | 10:40 | +10m | -25 |
| 10-22 | B | AMZN | 11:25 | +10m | -49 |
| 10-22 | A | AMZN | 11:25 | +10m | -71 |
| 10-22 | B | META | 12:05 | +10m | -487 |
| 10-22 | A | META | 12:05 | +10m | -557 |
| 10-22 | B | META | 12:55 | +10m | +135 |
| 10-22 | B | COIN | 13:05 | +10m | +13 |
| 10-22 | B | QQQ | 13:15 | +10m | -59 |
| 10-22 | B | SPY | 13:20 | +10m | -63 |
| 10-22 | A | SPY | 13:20 | +10m | -83 |
| 10-22 | A | QQQ | 13:15 | +10m | -63 |
| 10-22 | A | META | 12:55 | +10m | +161 |
| 10-22 | A | COIN | 13:05 | +10m | +26 |
| 10-22 | B | GOOGL | 15:00 | +10m | +3 |
| 10-22 | B | AMZN | 15:25 | +10m | -27 |
| 10-22 | A | AMZN | 15:25 | +10m | -45 |
| 10-22 | A | GOOGL | 15:00 | +10m | +11 |
| 10-23 | B | COIN | 10:40 | +10m | -59 |
| 10-23 | A | COIN | 10:40 | +10m | -123 |

### time15

| slice | n | wins | net $ | avg % | max DD | 95% CI |
|---|---:|---:|---:|---:|---:|---|
| all | 26 | 7 | $-1,860 | -13.4% | $-1,993 | $-3,694 to $-387 |
| version A | 13 | 4 | $-1,002 | -12.0% | $-1,087 | $-2,393 to $+35 |
| version B | 13 | 3 | $-858 | -14.8% | $-905 | $-1,981 to $-59 |
| 2026-10-21 | 4 | 2 | $-117 | +2.6% | $-81 | $-328 to $+94 |
| 2026-10-22 | 20 | 5 | $-1,509 | -11.5% | $-1,759 | $-3,360 to $-82 |
| 2026-10-23 | 2 | 0 | $-233 | -64.0% | $-161 | $-321 to $-145 |
| 2026-10-21 A | 2 | 1 | $-55 | +2.7% | $+0.00 | $-165 to $+55 |
| 2026-10-21 B | 2 | 1 | $-62 | +2.4% | $+0.00 | $-163 to $+39 |
| 2026-10-22 A | 10 | 3 | $-786 | -10.3% | $-927 | $-2,165 to $+171 |
| 2026-10-22 B | 10 | 2 | $-723 | -12.7% | $-833 | $-1,850 to $+84 |
| 2026-10-23 A | 1 | 0 | $-161 | -58.2% | $+0.00 | $-161 to $-161 |
| 2026-10-23 B | 1 | 0 | $-73 | -69.8% | $+0.00 | $-73 to $-73 |

| day | v | sym | out | why | net $ |
|---|---|---|---|---|---:|
| 10-21 | A | TSLA | 13:00 | +15m | -83 |
| 10-21 | B | TSLA | 13:00 | +15m | -81 |
| 10-21 | B | QQQ | 15:15 | +15m | +19 |
| 10-21 | A | QQQ | 15:15 | +15m | +27 |
| 10-22 | B | SPY | 10:15 | +15m | +109 |
| 10-22 | A | SPY | 10:15 | +15m | +141 |
| 10-22 | B | PLTR | 10:45 | +15m | -47 |
| 10-22 | A | PLTR | 10:45 | +15m | -51 |
| 10-22 | B | AMZN | 11:30 | +15m | -17 |
| 10-22 | A | AMZN | 11:30 | +15m | -31 |
| 10-22 | B | META | 12:10 | +15m | -544 |
| 10-22 | A | META | 12:10 | +15m | -627 |
| 10-22 | B | META | 13:00 | +15m | -22 |
| 10-22 | B | COIN | 13:11 | +15m | +9 |
| 10-22 | B | QQQ | 13:20 | +15m | -81 |
| 10-22 | B | SPY | 13:25 | +15m | -77 |
| 10-22 | A | SPY | 13:25 | +15m | -103 |
| 10-22 | A | QQQ | 13:20 | +15m | -89 |
| 10-22 | A | META | 13:00 | +15m | +32 |
| 10-22 | A | COIN | 13:12 | +15m | +30 |
| 10-22 | B | GOOGL | 15:05 | +15m | -3 |
| 10-22 | B | AMZN | 15:30 | +15m | -53 |
| 10-22 | A | AMZN | 15:30 | +15m | -87 |
| 10-22 | A | GOOGL | 15:05 | +15m | -3 |
| 10-23 | B | COIN | 10:45 | +15m | -73 |
| 10-23 | A | COIN | 10:45 | +15m | -161 |

### time30

| slice | n | wins | net $ | avg % | max DD | 95% CI |
|---|---:|---:|---:|---:|---:|---|
| all | 26 | 3 | $-2,639 | -16.5% | $-2,995 | $-5,058 to $-156 |
| version A | 13 | 2 | $-1,435 | -15.4% | $-1,626 | $-3,238 to $+392 |
| version B | 13 | 1 | $-1,203 | -17.7% | $-1,370 | $-2,758 to $+343 |
| 2026-10-21 | 4 | 0 | $-551 | -31.5% | $-410 | $-593 to $-508 |
| 2026-10-22 | 20 | 3 | $-1,793 | -7.3% | $-2,700 | $-4,314 to $+584 |
| 2026-10-23 | 2 | 0 | $-295 | -79.4% | $-209 | $-417 to $-173 |
| 2026-10-21 A | 2 | 0 | $-293 | -29.9% | $-153 | $-305 to $-281 |
| 2026-10-21 B | 2 | 0 | $-258 | -33.2% | $-123 | $-270 to $-245 |
| 2026-10-22 A | 10 | 2 | $-934 | -6.4% | $-1,417 | $-2,906 to $+831 |
| 2026-10-22 B | 10 | 1 | $-859 | -8.1% | $-1,283 | $-2,466 to $+649 |
| 2026-10-23 A | 1 | 0 | $-209 | -75.6% | $+0.00 | $-209 to $-209 |
| 2026-10-23 B | 1 | 0 | $-87 | -83.3% | $+0.00 | $-87 to $-87 |

| day | v | sym | out | why | net $ |
|---|---|---|---|---|---:|
| 10-21 | A | TSLA | 13:15 | +30m | -140 |
| 10-21 | B | TSLA | 13:15 | +30m | -135 |
| 10-21 | B | QQQ | 15:30 | +30m | -123 |
| 10-21 | A | QQQ | 15:30 | +30m | -153 |
| 10-22 | B | SPY | 10:30 | +30m | +424 |
| 10-22 | A | SPY | 10:30 | +30m | +483 |
| 10-22 | B | PLTR | 11:00 | +30m | -81 |
| 10-22 | A | PLTR | 11:00 | +30m | -111 |
| 10-22 | B | AMZN | 11:45 | +30m | -13 |
| 10-22 | A | AMZN | 11:45 | +30m | -7 |
| 10-22 | B | META | 12:25 | +30m | -654 |
| 10-22 | A | META | 12:25 | +30m | -776 |
| 10-22 | B | META | 13:18 | +30m | -229 |
| 10-22 | B | COIN | 13:26 | +30m | -9 |
| 10-22 | B | QQQ | 13:35 | +30m | -141 |
| 10-22 | B | SPY | 13:40 | +30m | -107 |
| 10-22 | A | SPY | 13:40 | +30m | -139 |
| 10-22 | A | QQQ | 13:35 | +30m | -165 |
| 10-22 | A | META | 13:15 | +30m | -157 |
| 10-22 | A | COIN | 13:30 | +30m | +2 |
| 10-22 | B | GOOGL | 15:20 | +30m | -7 |
| 10-22 | B | AMZN | 15:45 | +30m | -45 |
| 10-22 | A | AMZN | 15:45 | +30m | -65 |
| 10-22 | A | GOOGL | 15:21 | +30m | -1 |
| 10-23 | B | COIN | 11:00 | +30m | -87 |
| 10-23 | A | COIN | 11:00 | +30m | -209 |

n=34 sales over 3 days is far too small to conclude anything.
