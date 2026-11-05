# GEX latest

2026-11-05 12:43:41 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the put wall at 735.00, 2.96 pts (0.40%) away.
QQQ: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the put wall at 650.00, 3.20 pts (0.49%) away.

SPY top |GEX| strikes: 735.00 ($824.41M), 740.00 ($511.88M), 750.00 ($504.89M).
QQQ top |GEX| strikes: 675.00 ($231.20M), 660.00 ($158.10M), 650.00 ($153.15M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 737.96 | 653.20 |
| 0DTE flip |  |  |
| All-expiry flip |  |  |
| 0DTE call wall | 745.00 | 685.00 |
| 0DTE put wall | 735.00 | 650.00 |
| Net GEX 0DTE | -$951.05M | -$295.16M |
| Net GEX all | -$4.20B | -$1.69B |
| Vol-adj net 0DTE | -$45.55B | -$9.25B |
| Vol-adj net all | -$54.09B | -$11.94B |
| Missing greeks | 288/868 | 188/660 |
| OI used | 914134 | 806609 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
