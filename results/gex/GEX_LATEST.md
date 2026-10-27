# GEX latest

2026-10-27 14:44:40 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the call wall at 770.00, 0.77 pts (0.10%) away.
QQQ: spot above the 0DTE flip by 10.58 pts (1.47%); nearest wall is the put wall at 722.00, 1.46 pts (0.20%) away.

SPY top |GEX| strikes: 755.00 ($1.46B), 767.00 ($1.30B), 765.00 ($689.55M).
QQQ top |GEX| strikes: 700.00 ($425.48M), 690.00 ($303.78M), 719.00 ($284.31M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 769.23 | 720.54 |
| 0DTE flip |  | 709.96 |
| All-expiry flip | 699.35 |  |
| 0DTE call wall | 770.00 | 719.00 |
| 0DTE put wall | 767.00 | 722.00 |
| Net GEX 0DTE | -$425.13M | $543.16M |
| Net GEX all | -$3.09B | -$950.65M |
| Vol-adj net 0DTE | $62.16B | $22.89B |
| Vol-adj net all | $59.64B | $22.16B |
| Missing greeks | 321/888 | 309/922 |
| OI used | 1957126 | 1229922 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
