# GEX latest

2026-11-02 11:40:35 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the put wall at 760.00, 0.00 pts (0.00%) away.
QQQ: no 0DTE gamma flip (cumulative GEX did not cross zero); the call wall and the put wall are the same distance, 1.27 pts (0.18%) away.

SPY top |GEX| strikes: 767.00 ($662.30M), 760.00 ($538.12M), 755.00 ($288.81M).
QQQ top |GEX| strikes: 695.00 ($416.99M), 680.00 ($164.42M), 700.00 ($153.81M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 760.00 | 693.73 |
| 0DTE flip |  |  |
| All-expiry flip |  |  |
| 0DTE call wall | 763.00 | 695.00 |
| 0DTE put wall | 760.00 | 695.00 |
| Net GEX 0DTE | -$1.39B | -$704.73M |
| Net GEX all | -$2.88B | -$1.18B |
| Vol-adj net 0DTE | -$5.20B | -$1.45B |
| Vol-adj net all | -$6.46B | -$1.65B |
| Missing greeks | 287/650 | 355/748 |
| OI used | 430259 | 320202 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
