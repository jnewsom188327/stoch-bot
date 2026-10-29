# GEX latest

2026-10-29 10:38:03 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: no 0DTE gamma flip (cumulative GEX did not cross zero); the call wall and the put wall are the same distance, 0.07 pts (0.01%) away.
QQQ: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the put wall at 718.00, 1.52 pts (0.21%) away.

SPY top |GEX| strikes: 765.00 ($1.12B), 775.00 ($390.93M), 760.00 ($366.22M).
QQQ top |GEX| strikes: 700.00 ($322.71M), 710.00 ($287.76M), 715.00 ($262.60M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 770.07 | 716.48 |
| 0DTE flip |  |  |
| All-expiry flip | 704.15 |  |
| 0DTE call wall | 770.00 | 725.00 |
| 0DTE put wall | 770.00 | 718.00 |
| Net GEX 0DTE | -$12.41M | -$326.78M |
| Net GEX all | -$942.77M | -$1.90B |
| Vol-adj net 0DTE | $7.03B | $2.75B |
| Vol-adj net all | $6.41B | $1.11B |
| Missing greeks | 360/882 | 305/848 |
| OI used | 1708296 | 1181692 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
