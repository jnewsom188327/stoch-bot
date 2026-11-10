# GEX latest

2026-11-10 15:17:54 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: spot above the 0DTE flip by 19.55 pts (2.61%); the call wall and the put wall are the same distance, 1.16 pts (0.16%) away.
QQQ: spot above the 0DTE flip by 1.95 pts (0.29%); nearest wall is the call wall at 672.00, 1.01 pts (0.15%) away.

SPY top |GEX| strikes: 750.00 ($748.51M), 730.00 ($423.91M), 748.00 ($405.78M).
QQQ top |GEX| strikes: 672.00 ($271.28M), 650.00 ($224.71M), 685.00 ($188.22M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 748.84 | 673.01 |
| 0DTE flip | 729.28 | 671.06 |
| All-expiry flip | 750.50 | 674.94 |
| 0DTE call wall | 750.00 | 672.00 |
| 0DTE put wall | 750.00 | 671.00 |
| Net GEX 0DTE | $1.72B | $409.61M |
| Net GEX all | $535.44M | -$25.85M |
| Vol-adj net 0DTE | $29.72B | $1.45B |
| Vol-adj net all | $28.84B | $239.34M |
| Missing greeks | 388/896 | 420/1046 |
| OI used | 1115025 | 615793 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
