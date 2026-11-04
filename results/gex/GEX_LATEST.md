# GEX latest

2026-11-04 13:13:25 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: spot above the 0DTE flip by 2.63 pts (0.34%); nearest wall is the call wall at 770.00, 1.37 pts (0.18%) away.
QQQ: spot below the 0DTE flip by 0.74 pts (0.11%); nearest wall is the call wall at 694.00, 1.62 pts (0.23%) away.

SPY top |GEX| strikes: 770.00 ($672.64M), 767.00 ($652.66M), 780.00 ($325.54M).
QQQ top |GEX| strikes: 680.00 ($299.73M), 675.00 ($268.63M), 713.00 ($266.69M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 768.63 | 695.62 |
| 0DTE flip | 766.00 | 696.36 |
| All-expiry flip | 773.94 |  |
| 0DTE call wall | 770.00 | 694.00 |
| 0DTE put wall | 767.00 | 700.00 |
| Net GEX 0DTE | $404.14M | $110.98M |
| Net GEX all | $1.01B | -$1.66B |
| Vol-adj net 0DTE | $79.82B | $17.11B |
| Vol-adj net all | $84.07B | $16.74B |
| Missing greeks | 364/902 | 300/848 |
| OI used | 1099520 | 1023098 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
