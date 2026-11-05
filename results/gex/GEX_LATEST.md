# GEX latest

2026-11-05 09:57:56 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: no 0DTE gamma flip (cumulative GEX did not cross zero); the call wall and the put wall are the same distance, 3.08 pts (0.41%) away.
QQQ: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the put wall at 670.00, 4.68 pts (0.70%) away.

SPY top |GEX| strikes: 750.00 ($872.33M), 740.00 ($301.08M), 745.00 ($291.06M).
QQQ top |GEX| strikes: 675.00 ($466.71M), 680.00 ($294.22M), 670.00 ($283.57M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 753.08 | 665.32 |
| 0DTE flip |  |  |
| All-expiry flip |  |  |
| 0DTE call wall | 750.00 | 690.00 |
| 0DTE put wall | 750.00 | 670.00 |
| Net GEX 0DTE | -$101.27M | -$392.63M |
| Net GEX all | -$2.59B | -$2.44B |
| Vol-adj net 0DTE | -$8.54B | -$3.02B |
| Vol-adj net all | -$12.11B | -$5.61B |
| Missing greeks | 346/888 | 243/738 |
| OI used | 905321 | 919691 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
