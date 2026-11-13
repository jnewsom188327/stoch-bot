# GEX latest

2026-11-13 11:25:38 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the call wall at 750.00, 0.36 pts (0.05%) away.
QQQ: no 0DTE gamma flip (cumulative GEX did not cross zero); the call wall and the put wall are the same distance, 1.36 pts (0.20%) away.

SPY top |GEX| strikes: 745.00 ($848.22M), 755.00 ($454.53M), 740.00 ($290.33M).
QQQ top |GEX| strikes: 670.00 ($159.91M), 678.00 ($124.81M), 660.00 ($112.49M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 749.64 | 673.64 |
| 0DTE flip |  |  |
| All-expiry flip |  |  |
| 0DTE call wall | 750.00 | 675.00 |
| 0DTE put wall | 745.00 | 675.00 |
| Net GEX 0DTE | -$2.34B | -$868.83M |
| Net GEX all | -$2.93B | -$1.01B |
| Vol-adj net 0DTE | -$38.66B | -$12.52B |
| Vol-adj net all | -$40.18B | -$13.26B |
| Missing greeks | 332/872 | 350/1018 |
| OI used | 1147371 | 753599 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
