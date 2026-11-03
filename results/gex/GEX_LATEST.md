# GEX latest

2026-11-03 12:20:54 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: spot above the 0DTE flip by 4.28 pts (0.57%); nearest wall is the put wall at 755.00, 0.09 pts (0.01%) away.
QQQ: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the call wall at 690.00, 2.81 pts (0.41%) away.

SPY top |GEX| strikes: 740.00 ($701.63M), 750.00 ($382.37M), 755.00 ($379.14M).
QQQ top |GEX| strikes: 680.00 ($432.70M), 675.00 ($306.46M), 685.00 ($228.02M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 755.09 | 687.19 |
| 0DTE flip | 750.80 |  |
| All-expiry flip |  |  |
| 0DTE call wall | 756.00 | 690.00 |
| 0DTE put wall | 755.00 | 680.00 |
| Net GEX 0DTE | -$13.46M | -$291.72M |
| Net GEX all | -$2.89B | -$2.08B |
| Vol-adj net 0DTE | $19.82B | $11.57B |
| Vol-adj net all | $17.94B | $9.72B |
| Missing greeks | 365/888 | 277/848 |
| OI used | 1070754 | 902998 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
