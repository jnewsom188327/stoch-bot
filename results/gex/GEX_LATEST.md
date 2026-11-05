# GEX latest

2026-11-05 14:24:01 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the put wall at 735.00, 0.98 pts (0.13%) away.
QQQ: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the put wall at 650.00, 2.22 pts (0.34%) away.

SPY top |GEX| strikes: 735.00 ($956.78M), 740.00 ($499.77M), 750.00 ($424.17M).
QQQ top |GEX| strikes: 675.00 ($232.23M), 650.00 ($179.40M), 660.00 ($157.64M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 735.98 | 652.22 |
| 0DTE flip |  |  |
| All-expiry flip |  |  |
| 0DTE call wall | 745.00 | 700.00 |
| 0DTE put wall | 735.00 | 650.00 |
| Net GEX 0DTE | -$1.13B | -$304.47M |
| Net GEX all | -$4.21B | -$1.71B |
| Vol-adj net 0DTE | -$64.35B | -$12.55B |
| Vol-adj net all | -$72.81B | -$15.22B |
| Missing greeks | 344/858 | 218/652 |
| OI used | 907555 | 800641 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
