# GEX latest

2026-11-09 14:28:23 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: spot above the 0DTE flip by 2.32 pts (0.31%); nearest wall is the call wall at 750.00, 2.06 pts (0.27%) away.
QQQ: spot above the 0DTE flip by 6.12 pts (0.90%); the call wall and the put wall are the same distance, 2.97 pts (0.44%) away.

SPY top |GEX| strikes: 755.00 ($261.00M), 750.00 ($242.69M), 751.00 ($69.06M).
QQQ top |GEX| strikes: 680.00 ($104.75M), 674.00 ($64.14M), 672.00 ($63.46M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 752.06 | 677.03 |
| 0DTE flip | 749.74 | 670.92 |
| All-expiry flip | 749.64 | 671.96 |
| 0DTE call wall | 750.00 | 680.00 |
| 0DTE put wall | 755.00 | 680.00 |
| Net GEX 0DTE | $9.11M | $259.27M |
| Net GEX all | $413.01M | $354.75M |
| Vol-adj net 0DTE | $76.38B | $15.31B |
| Vol-adj net all | $79.28B | $15.18B |
| Missing greeks | 376/896 | 373/1006 |
| OI used | 658564 | 345001 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
