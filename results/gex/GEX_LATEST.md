# GEX latest

2026-10-27 10:28:53 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the put wall at 767.00, 0.67 pts (0.09%) away.
QQQ: spot above the 0DTE flip by 6.24 pts (0.87%); nearest wall is the call wall at 719.00, 3.09 pts (0.43%) away.

SPY top |GEX| strikes: 755.00 ($1.79B), 767.00 ($1.70B), 745.00 ($867.96M).
QQQ top |GEX| strikes: 700.00 ($529.07M), 690.00 ($413.68M), 720.00 ($156.71M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 766.33 | 715.91 |
| 0DTE flip |  | 709.67 |
| All-expiry flip |  |  |
| 0DTE call wall | 765.00 | 719.00 |
| 0DTE put wall | 767.00 | 722.00 |
| Net GEX 0DTE | -$1.42B | $397.86M |
| Net GEX all | -$5.65B | -$1.71B |
| Vol-adj net 0DTE | -$3.23B | $7.07B |
| Vol-adj net all | -$7.73B | $4.96B |
| Missing greeks | 345/892 | 317/928 |
| OI used | 1965560 | 1231709 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
