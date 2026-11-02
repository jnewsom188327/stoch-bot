# GEX latest

2026-11-02 14:21:15 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the put wall at 755.00, 0.00 pts (0.00%) away.
QQQ: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the put wall at 685.00, 0.95 pts (0.14%) away.

SPY top |GEX| strikes: 755.00 ($440.56M), 767.00 ($414.42M), 760.00 ($239.94M).
QQQ top |GEX| strikes: 680.00 ($289.09M), 685.00 ($242.62M), 695.00 ($150.07M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 755.00 | 685.95 |
| 0DTE flip |  |  |
| All-expiry flip |  |  |
| 0DTE call wall | 770.00 | 725.00 |
| 0DTE put wall | 755.00 | 685.00 |
| Net GEX 0DTE | -$1.28B | -$498.97M |
| Net GEX all | -$2.66B | -$1.03B |
| Vol-adj net 0DTE | -$79.08B | -$30.50B |
| Vol-adj net all | -$83.67B | -$31.97B |
| Missing greeks | 351/648 | 340/698 |
| OI used | 430406 | 317664 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
