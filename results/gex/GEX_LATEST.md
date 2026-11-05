# GEX latest

2026-11-05 15:57:52 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the put wall at 735.00, 1.49 pts (0.20%) away.
QQQ: no 0DTE gamma flip (cumulative GEX did not cross zero); the call wall and the put wall are the same distance, 2.17 pts (0.33%) away.

SPY top |GEX| strikes: 735.00 ($1.73B), 730.00 ($456.67M), 740.00 ($413.88M).
QQQ top |GEX| strikes: 650.00 ($255.45M), 645.00 ($125.55M), 660.00 ($110.85M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 733.51 | 647.83 |
| 0DTE flip |  |  |
| All-expiry flip |  |  |
| 0DTE call wall | 745.00 | 650.00 |
| 0DTE put wall | 735.00 | 650.00 |
| Net GEX 0DTE | -$1.95B | -$223.88M |
| Net GEX all | -$4.70B | -$1.24B |
| Vol-adj net 0DTE | -$128.56B | -$33.32B |
| Vol-adj net all | -$136.85B | -$35.77B |
| Missing greeks | 353/852 | 214/620 |
| OI used | 902544 | 681494 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
