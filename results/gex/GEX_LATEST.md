# GEX latest

2026-11-11 12:26:55 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: spot above the 0DTE flip by 3.74 pts (0.49%); nearest wall is the call wall at 760.00, 0.79 pts (0.10%) away.
QQQ: spot above the 0DTE flip by 5.08 pts (0.73%); the call wall and the put wall are the same distance, 0.90 pts (0.13%) away.

SPY top |GEX| strikes: 760.00 ($526.19M), 770.00 ($299.53M), 765.00 ($286.87M).
QQQ top |GEX| strikes: 700.00 ($225.43M), 696.00 ($205.57M), 685.00 ($140.41M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 760.79 | 694.10 |
| 0DTE flip | 757.05 | 689.02 |
| All-expiry flip | 761.86 | 694.61 |
| 0DTE call wall | 760.00 | 695.00 |
| 0DTE put wall | 763.00 | 695.00 |
| Net GEX 0DTE | $736.78M | $478.66M |
| Net GEX all | $1.72B | $1.14B |
| Vol-adj net 0DTE | $110.52B | $38.14B |
| Vol-adj net all | $115.55B | $40.42B |
| Missing greeks | 363/912 | 328/958 |
| OI used | 1092944 | 720175 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
