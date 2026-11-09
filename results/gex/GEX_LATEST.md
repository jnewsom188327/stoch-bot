# GEX latest

2026-11-09 11:49:28 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: spot above the 0DTE flip by 1.26 pts (0.17%); the call wall and the put wall are the same distance, 0.98 pts (0.13%) away.
QQQ: spot above the 0DTE flip by 17.21 pts (2.54%); the call wall and the put wall are the same distance, 3.46 pts (0.51%) away.

SPY top |GEX| strikes: 750.00 ($234.19M), 755.00 ($115.49M), 725.00 ($68.27M).
QQQ top |GEX| strikes: 680.00 ($95.67M), 672.00 ($63.55M), 674.00 ($57.23M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 750.98 | 676.54 |
| 0DTE flip | 749.71 | 659.33 |
| All-expiry flip | 749.92 | 667.02 |
| 0DTE call wall | 750.00 | 680.00 |
| 0DTE put wall | 750.00 | 680.00 |
| Net GEX 0DTE | $133.30M | $352.09M |
| Net GEX all | $433.60M | $434.70M |
| Vol-adj net 0DTE | $41.19B | $12.75B |
| Vol-adj net all | $43.95B | $12.98B |
| Missing greeks | 356/896 | 351/1014 |
| OI used | 658564 | 345001 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
