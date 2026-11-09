# GEX latest

2026-11-09 10:48:39 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: spot below the 0DTE flip by 2.57 pts (0.34%); the call wall and the put wall are the same distance, 0.01 pts (0.00%) away.
QQQ: spot above the 0DTE flip by 15.10 pts (2.24%); the call wall and the put wall are the same distance, 4.32 pts (0.64%) away.

SPY top |GEX| strikes: 750.00 ($214.93M), 755.00 ($146.73M), 745.00 ($82.00M).
QQQ top |GEX| strikes: 680.00 ($82.39M), 672.00 ($64.81M), 670.00 ($60.71M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 750.01 | 675.68 |
| 0DTE flip | 752.58 | 660.58 |
| All-expiry flip | 750.63 | 669.44 |
| 0DTE call wall | 750.00 | 680.00 |
| 0DTE put wall | 750.00 | 680.00 |
| Net GEX 0DTE | $14.35M | $285.48M |
| Net GEX all | $314.02M | $357.91M |
| Vol-adj net 0DTE | $31.74B | $11.58B |
| Vol-adj net all | $34.08B | $11.95B |
| Missing greeks | 354/896 | 349/1014 |
| OI used | 658564 | 345001 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
