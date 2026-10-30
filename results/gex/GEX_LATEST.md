# GEX latest

2026-10-30 15:00:07 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: no 0DTE gamma flip (cumulative GEX did not cross zero); the call wall and the put wall are the same distance, 2.08 pts (0.28%) away.
QQQ: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the call wall at 685.00, 0.35 pts (0.05%) away.

SPY top |GEX| strikes: 750.00 ($3.50B), 755.00 ($1.58B), 745.00 ($612.31M).
QQQ top |GEX| strikes: 690.00 ($1.64B), 685.00 ($930.86M), 680.00 ($557.22M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 752.08 | 685.35 |
| 0DTE flip |  |  |
| All-expiry flip |  |  |
| 0DTE call wall | 750.00 | 685.00 |
| 0DTE put wall | 750.00 | 690.00 |
| Net GEX 0DTE | -$9.05B | -$5.20B |
| Net GEX all | -$10.47B | -$5.86B |
| Vol-adj net 0DTE | -$111.36B | -$34.91B |
| Vol-adj net all | -$117.54B | -$35.84B |
| Missing greeks | 421/890 | 316/826 |
| OI used | 1619470 | 1119960 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
