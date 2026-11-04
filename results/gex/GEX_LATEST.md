# GEX latest

2026-11-04 12:24:12 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: spot above the 0DTE flip by 2.25 pts (0.29%); nearest wall is the put wall at 767.00, 1.32 pts (0.17%) away.
QQQ: spot below the 0DTE flip by 1.18 pts (0.17%); the call wall and the put wall are the same distance, 3.93 pts (0.57%) away.

SPY top |GEX| strikes: 767.00 ($594.65M), 770.00 ($582.10M), 780.00 ($325.02M).
QQQ top |GEX| strikes: 713.00 ($320.91M), 680.00 ($287.48M), 675.00 ($266.63M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 768.32 | 696.07 |
| 0DTE flip | 766.07 | 697.24 |
| All-expiry flip | 774.41 |  |
| 0DTE call wall | 770.00 | 700.00 |
| 0DTE put wall | 767.00 | 700.00 |
| Net GEX 0DTE | $423.94M | $112.36M |
| Net GEX all | $916.12M | -$1.66B |
| Vol-adj net 0DTE | $55.17B | $13.37B |
| Vol-adj net all | $59.00B | $12.92B |
| Missing greeks | 376/902 | 298/848 |
| OI used | 1099520 | 1023098 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
