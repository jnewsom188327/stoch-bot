# GEX latest

2026-11-12 13:24:34 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: spot above the 0DTE flip by 4.85 pts (0.64%); the call wall and the put wall are the same distance, 0.30 pts (0.04%) away.
QQQ: spot above the 0DTE flip by 3.39 pts (0.49%); the call wall and the put wall are the same distance, 0.62 pts (0.09%) away.

SPY top |GEX| strikes: 762.00 ($362.68M), 759.00 ($350.02M), 761.00 ($329.35M).
QQQ top |GEX| strikes: 700.00 ($194.02M), 685.00 ($190.95M), 696.00 ($185.80M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 760.30 | 690.62 |
| 0DTE flip | 755.45 | 687.23 |
| All-expiry flip | 760.84 | 695.05 |
| 0DTE call wall | 760.00 | 690.00 |
| 0DTE put wall | 760.00 | 690.00 |
| Net GEX 0DTE | $1.06B | $362.34M |
| Net GEX all | $2.13B | $773.08M |
| Vol-adj net 0DTE | $62.86B | $24.92B |
| Vol-adj net all | $66.51B | $26.09B |
| Missing greeks | 325/904 | 322/952 |
| OI used | 1124489 | 674456 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
