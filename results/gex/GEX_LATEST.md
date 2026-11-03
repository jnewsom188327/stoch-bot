# GEX latest

2026-11-03 11:25:02 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the call wall at 756.00, 0.48 pts (0.06%) away.
QQQ: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the call wall at 690.00, 3.65 pts (0.53%) away.

SPY top |GEX| strikes: 740.00 ($673.73M), 750.00 ($405.13M), 755.00 ($332.75M).
QQQ top |GEX| strikes: 680.00 ($464.78M), 675.00 ($317.13M), 685.00 ($222.18M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 755.52 | 686.35 |
| 0DTE flip |  |  |
| All-expiry flip |  |  |
| 0DTE call wall | 756.00 | 690.00 |
| 0DTE put wall | 755.00 | 680.00 |
| Net GEX 0DTE | -$19.92M | -$301.75M |
| Net GEX all | -$2.80B | -$2.12B |
| Vol-adj net 0DTE | $30.88B | $7.62B |
| Vol-adj net all | $29.52B | $5.92B |
| Missing greeks | 349/888 | 271/840 |
| OI used | 1070754 | 899569 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
