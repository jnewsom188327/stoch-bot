# GEX latest

2026-10-28 12:16:00 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: spot above the 0DTE flip by 0.71 pts (0.09%); nearest wall is the call wall at 772.00, 0.75 pts (0.10%) away.
QQQ: spot above the 0DTE flip by 2.87 pts (0.40%); the call wall and the put wall are the same distance, 2.09 pts (0.29%) away.

SPY top |GEX| strikes: 765.00 ($847.34M), 755.00 ($746.75M), 780.00 ($511.17M).
QQQ top |GEX| strikes: 700.00 ($243.44M), 730.00 ($243.05M), 740.00 ($220.78M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 771.25 | 722.09 |
| 0DTE flip | 770.54 | 719.22 |
| All-expiry flip | 703.37 |  |
| 0DTE call wall | 772.00 | 720.00 |
| 0DTE put wall | 765.00 | 720.00 |
| Net GEX 0DTE | $695.53M | $314.62M |
| Net GEX all | -$61.44M | -$134.94M |
| Vol-adj net 0DTE | $4.80B | $1.91B |
| Vol-adj net all | $4.14B | $1.30B |
| Missing greeks | 305/884 | 300/888 |
| OI used | 1884905 | 1176188 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
