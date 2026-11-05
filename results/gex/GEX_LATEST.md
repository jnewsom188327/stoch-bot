# GEX latest

2026-11-05 15:13:04 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the put wall at 735.00, 0.21 pts (0.03%) away.
QQQ: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the put wall at 650.00, 0.92 pts (0.14%) away.

SPY top |GEX| strikes: 735.00 ($1.11B), 740.00 ($503.60M), 730.00 ($426.84M).
QQQ top |GEX| strikes: 675.00 ($212.32M), 650.00 ($206.57M), 660.00 ($145.19M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 735.21 | 650.92 |
| 0DTE flip |  |  |
| All-expiry flip |  |  |
| 0DTE call wall | 745.00 | 700.00 |
| 0DTE put wall | 735.00 | 650.00 |
| Net GEX 0DTE | -$1.25B | -$302.58M |
| Net GEX all | -$4.39B | -$1.75B |
| Vol-adj net 0DTE | -$77.90B | -$20.91B |
| Vol-adj net all | -$86.26B | -$23.72B |
| Missing greeks | 333/856 | 182/644 |
| OI used | 905512 | 787032 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
