# GEX latest

2026-11-04 15:45:41 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: spot above the 0DTE flip by 0.88 pts (0.11%); the call wall and the put wall are the same distance, 0.04 pts (0.01%) away.
QQQ: no 0DTE gamma flip (cumulative GEX did not cross zero); the call wall and the put wall are the same distance, 1.54 pts (0.22%) away.

SPY top |GEX| strikes: 767.00 ($1.87B), 765.00 ($464.21M), 770.00 ($460.13M).
QQQ top |GEX| strikes: 680.00 ($366.28M), 675.00 ($337.83M), 691.00 ($257.93M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 767.04 | 691.54 |
| 0DTE flip | 766.17 |  |
| All-expiry flip |  |  |
| 0DTE call wall | 767.00 | 690.00 |
| 0DTE put wall | 767.00 | 690.00 |
| Net GEX 0DTE | -$1.24B | -$48.14M |
| Net GEX all | -$867.23M | -$2.06B |
| Vol-adj net 0DTE | -$36.11B | -$63.23B |
| Vol-adj net all | -$35.52B | -$65.96B |
| Missing greeks | 382/894 | 306/832 |
| OI used | 1099225 | 1021041 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
