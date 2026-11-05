# GEX latest

2026-11-05 13:25:50 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the put wall at 735.00, 1.00 pts (0.14%) away.
QQQ: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the put wall at 650.00, 1.53 pts (0.23%) away.

SPY top |GEX| strikes: 735.00 ($881.02M), 740.00 ($485.60M), 750.00 ($413.73M).
QQQ top |GEX| strikes: 675.00 ($216.67M), 650.00 ($163.69M), 660.00 ($152.93M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 736.00 | 651.53 |
| 0DTE flip |  |  |
| All-expiry flip |  |  |
| 0DTE call wall | 745.00 | 700.00 |
| 0DTE put wall | 735.00 | 650.00 |
| Net GEX 0DTE | -$1.02B | -$290.60M |
| Net GEX all | -$4.33B | -$1.68B |
| Vol-adj net 0DTE | -$52.99B | -$12.01B |
| Vol-adj net all | -$62.12B | -$14.81B |
| Missing greeks | 272/858 | 182/644 |
| OI used | 907555 | 787032 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
