# GEX latest

2026-11-05 10:50:26 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the call wall at 745.00, 4.46 pts (0.60%) away.
QQQ: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the put wall at 650.00, 2.21 pts (0.34%) away.

SPY top |GEX| strikes: 735.00 ($608.83M), 750.00 ($560.59M), 740.00 ($423.23M).
QQQ top |GEX| strikes: 675.00 ($233.27M), 660.00 ($137.77M), 680.00 ($136.27M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 740.54 | 652.21 |
| 0DTE flip |  |  |
| All-expiry flip |  |  |
| 0DTE call wall | 745.00 | 690.00 |
| 0DTE put wall | 735.00 | 650.00 |
| Net GEX 0DTE | -$708.35M | -$226.40M |
| Net GEX all | -$3.59B | -$1.71B |
| Vol-adj net 0DTE | -$20.49B | -$4.63B |
| Vol-adj net all | -$26.33B | -$7.18B |
| Missing greeks | 341/868 | 182/652 |
| OI used | 914510 | 800641 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
