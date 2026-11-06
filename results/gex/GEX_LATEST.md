# GEX latest

2026-11-06 10:30:28 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the put wall at 740.00, 1.25 pts (0.17%) away.
QQQ: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the call wall at 655.00, 2.48 pts (0.38%) away.

SPY top |GEX| strikes: 740.00 ($677.64M), 735.00 ($609.72M), 750.00 ($577.13M).
QQQ top |GEX| strikes: 660.00 ($222.14M), 675.00 ($200.37M), 680.00 ($153.98M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 738.75 | 657.48 |
| 0DTE flip |  |  |
| All-expiry flip |  |  |
| 0DTE call wall | 745.00 | 655.00 |
| 0DTE put wall | 740.00 | 660.00 |
| Net GEX 0DTE | -$3.69B | -$1.48B |
| Net GEX all | -$4.77B | -$1.84B |
| Vol-adj net 0DTE | $7.75B | -$804.47M |
| Vol-adj net all | $7.39B | -$983.11M |
| Missing greeks | 343/892 | 313/1010 |
| OI used | 988308 | 888606 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
