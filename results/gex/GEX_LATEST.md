# GEX latest

2026-10-28 15:58:18 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: spot above the 0DTE flip by 3.01 pts (0.39%); nearest wall is the call wall at 772.00, 0.15 pts (0.02%) away.
QQQ: spot above the 0DTE flip by 5.33 pts (0.74%); nearest wall is the call wall at 725.00, 0.24 pts (0.03%) away.

SPY top |GEX| strikes: 765.00 ($863.25M), 755.00 ($620.52M), 780.00 ($521.12M).
QQQ top |GEX| strikes: 730.00 ($295.60M), 729.00 ($266.15M), 740.00 ($265.03M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 771.85 | 724.76 |
| 0DTE flip | 768.84 | 719.43 |
| All-expiry flip | 781.47 | 734.83 |
| 0DTE call wall | 772.00 | 725.00 |
| 0DTE put wall | 770.00 | 720.00 |
| Net GEX 0DTE | $1.05B | $465.13M |
| Net GEX all | $931.93M | $538.41M |
| Vol-adj net 0DTE | $21.87B | $18.75B |
| Vol-adj net all | $23.53B | $19.41B |
| Missing greeks | 363/884 | 334/884 |
| OI used | 1884905 | 1151891 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
