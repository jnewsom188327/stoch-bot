# GEX latest

2026-11-13 10:31:07 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the call wall at 750.00, 0.15 pts (0.02%) away.
QQQ: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the call wall at 675.00, 0.39 pts (0.06%) away.

SPY top |GEX| strikes: 745.00 ($763.17M), 755.00 ($538.13M), 740.00 ($309.27M).
QQQ top |GEX| strikes: 660.00 ($133.95M), 670.00 ($128.24M), 678.00 ($117.95M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 749.85 | 674.61 |
| 0DTE flip |  |  |
| All-expiry flip |  |  |
| 0DTE call wall | 750.00 | 675.00 |
| 0DTE put wall | 745.00 | 680.00 |
| Net GEX 0DTE | -$2.83B | -$885.27M |
| Net GEX all | -$3.21B | -$1.01B |
| Vol-adj net 0DTE | -$30.61B | -$9.41B |
| Vol-adj net all | -$32.10B | -$10.07B |
| Missing greeks | 313/872 | 355/1012 |
| OI used | 1147371 | 753498 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
