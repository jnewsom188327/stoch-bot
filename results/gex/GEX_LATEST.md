# GEX latest

2026-10-29 13:58:14 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the call wall at 768.00, 0.79 pts (0.10%) away.
QQQ: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the put wall at 714.00, 1.15 pts (0.16%) away.

SPY top |GEX| strikes: 765.00 ($1.53B), 760.00 ($565.98M), 755.00 ($365.66M).
QQQ top |GEX| strikes: 700.00 ($442.42M), 710.00 ($372.44M), 715.00 ($286.49M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 767.21 | 712.85 |
| 0DTE flip |  |  |
| All-expiry flip | 704.27 |  |
| 0DTE call wall | 768.00 | 715.00 |
| 0DTE put wall | 765.00 | 714.00 |
| Net GEX 0DTE | -$303.97M | -$495.84M |
| Net GEX all | -$3.01B | -$2.82B |
| Vol-adj net 0DTE | -$34.56B | -$12.84B |
| Vol-adj net all | -$40.69B | -$16.47B |
| Missing greeks | 330/880 | 328/846 |
| OI used | 1712665 | 1179706 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
