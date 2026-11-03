# GEX latest

2026-11-03 13:06:14 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: spot below the 0DTE flip by 1.77 pts (0.23%); nearest wall is the call wall at 756.00, 0.02 pts (0.00%) away.
QQQ: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the call wall at 690.00, 2.45 pts (0.36%) away.

SPY top |GEX| strikes: 740.00 ($644.50M), 750.00 ($423.54M), 755.00 ($420.48M).
QQQ top |GEX| strikes: 680.00 ($401.68M), 675.00 ($300.24M), 685.00 ($241.85M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 756.02 | 687.55 |
| 0DTE flip | 757.79 |  |
| All-expiry flip |  |  |
| 0DTE call wall | 756.00 | 690.00 |
| 0DTE put wall | 755.00 | 685.00 |
| Net GEX 0DTE | $54.71M | -$278.73M |
| Net GEX all | -$2.68B | -$2.08B |
| Vol-adj net 0DTE | $40.03B | $13.73B |
| Vol-adj net all | $38.42B | $11.86B |
| Missing greeks | 340/882 | 275/854 |
| OI used | 1067904 | 903860 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
