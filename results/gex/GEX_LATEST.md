# GEX latest

2026-10-29 11:28:51 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: no 0DTE gamma flip (cumulative GEX did not cross zero); the call wall and the put wall are the same distance, 0.08 pts (0.01%) away.
QQQ: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the put wall at 718.00, 1.45 pts (0.20%) away.

SPY top |GEX| strikes: 765.00 ($1.16B), 775.00 ($389.43M), 760.00 ($356.99M).
QQQ top |GEX| strikes: 700.00 ($315.52M), 710.00 ($289.78M), 715.00 ($266.12M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 770.08 | 716.55 |
| 0DTE flip |  |  |
| All-expiry flip |  |  |
| 0DTE call wall | 770.00 | 725.00 |
| 0DTE put wall | 770.00 | 718.00 |
| Net GEX 0DTE | -$4.37M | -$358.57M |
| Net GEX all | -$878.60M | -$1.92B |
| Vol-adj net 0DTE | $17.06B | $6.26B |
| Vol-adj net all | $16.53B | $4.74B |
| Missing greeks | 358/882 | 316/848 |
| OI used | 1708296 | 1181692 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
