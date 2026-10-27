# GEX latest

2026-10-27 09:40:20 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the put wall at 767.00, 1.13 pts (0.15%) away.
QQQ: spot above the 0DTE flip by 5.92 pts (0.82%); nearest wall is the call wall at 719.00, 1.08 pts (0.15%) away.

SPY top |GEX| strikes: 755.00 ($1.59B), 767.00 ($1.40B), 745.00 ($749.80M).
QQQ top |GEX| strikes: 700.00 ($485.42M), 690.00 ($372.58M), 719.00 ($148.33M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 768.13 | 717.92 |
| 0DTE flip |  | 712.00 |
| All-expiry flip |  |  |
| 0DTE call wall | 770.00 | 719.00 |
| 0DTE put wall | 767.00 | 722.00 |
| Net GEX 0DTE | -$917.19M | $405.90M |
| Net GEX all | -$4.17B | -$1.39B |
| Vol-adj net 0DTE | $6.94B | $4.13B |
| Vol-adj net all | $3.57B | $1.75B |
| Missing greeks | 300/882 | 302/918 |
| OI used | 1954163 | 1224111 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
