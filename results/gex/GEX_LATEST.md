# GEX latest

2026-11-03 15:26:57 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the put wall at 755.00, 0.40 pts (0.05%) away.
QQQ: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the call wall at 686.00, 0.33 pts (0.05%) away.

SPY top |GEX| strikes: 740.00 ($706.41M), 755.00 ($538.41M), 750.00 ($502.65M).
QQQ top |GEX| strikes: 680.00 ($415.71M), 685.00 ($348.60M), 675.00 ($314.73M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 754.60 | 685.67 |
| 0DTE flip |  |  |
| All-expiry flip |  |  |
| 0DTE call wall | 756.00 | 686.00 |
| 0DTE put wall | 755.00 | 685.00 |
| Net GEX 0DTE | -$311.30M | -$407.92M |
| Net GEX all | -$3.34B | -$2.24B |
| Vol-adj net 0DTE | -$43.02B | -$20.01B |
| Vol-adj net all | -$45.83B | -$22.40B |
| Missing greeks | 379/888 | 262/840 |
| OI used | 1070754 | 899569 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
