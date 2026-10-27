# GEX latest

2026-10-27 15:27:55 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: spot below the 0DTE flip by 0.70 pts (0.09%); nearest wall is the call wall at 770.00, 0.22 pts (0.03%) away.
QQQ: spot above the 0DTE flip by 0.13 pts (0.02%); the call wall and the put wall are the same distance, 0.42 pts (0.06%) away.

SPY top |GEX| strikes: 755.00 ($1.35B), 765.00 ($681.78M), 767.00 ($657.84M).
QQQ top |GEX| strikes: 700.00 ($402.23M), 690.00 ($289.65M), 729.00 ($160.05M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 770.22 | 721.58 |
| 0DTE flip | 770.91 | 721.45 |
| All-expiry flip | 699.48 |  |
| 0DTE call wall | 770.00 | 722.00 |
| 0DTE put wall | 767.00 | 722.00 |
| Net GEX 0DTE | $333.58M | $170.35M |
| Net GEX all | -$1.79B | -$1.17B |
| Vol-adj net 0DTE | $157.62B | $50.59B |
| Vol-adj net all | $156.68B | $50.18B |
| Missing greeks | 335/886 | 320/920 |
| OI used | 1951606 | 1227712 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
