# GEX latest

2026-10-28 10:34:24 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: spot above the 0DTE flip by 0.30 pts (0.04%); nearest wall is the call wall at 772.00, 0.91 pts (0.12%) away.
QQQ: spot above the 0DTE flip by 2.93 pts (0.41%); the call wall and the put wall are the same distance, 2.17 pts (0.30%) away.

SPY top |GEX| strikes: 765.00 ($844.91M), 755.00 ($769.57M), 780.00 ($491.46M).
QQQ top |GEX| strikes: 700.00 ($243.43M), 730.00 ($242.14M), 740.00 ($220.85M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 771.09 | 722.17 |
| 0DTE flip | 770.79 | 719.24 |
| All-expiry flip | 699.07 |  |
| 0DTE call wall | 772.00 | 720.00 |
| 0DTE put wall | 765.00 | 720.00 |
| Net GEX 0DTE | $625.89M | $320.83M |
| Net GEX all | -$278.56M | -$152.03M |
| Vol-adj net 0DTE | $1.24B | $830.67M |
| Vol-adj net all | $195.27M | $234.67M |
| Missing greeks | 319/886 | 299/888 |
| OI used | 1886450 | 1176188 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
