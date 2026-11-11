# GEX latest

2026-11-11 15:12:56 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: spot above the 0DTE flip by 2.81 pts (0.37%); the call wall and the put wall are the same distance, 0.27 pts (0.04%) away.
QQQ: spot above the 0DTE flip by 12.09 pts (1.75%); the call wall and the put wall are the same distance, 1.27 pts (0.18%) away.

SPY top |GEX| strikes: 760.00 ($816.69M), 770.00 ($244.41M), 765.00 ($243.13M).
QQQ top |GEX| strikes: 696.00 ($183.97M), 700.00 ($174.45M), 690.00 ($172.29M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 760.27 | 691.27 |
| 0DTE flip | 757.46 | 679.18 |
| All-expiry flip | 760.00 | 691.03 |
| 0DTE call wall | 760.00 | 690.00 |
| 0DTE put wall | 760.00 | 690.00 |
| Net GEX 0DTE | $934.20M | $635.99M |
| Net GEX all | $1.78B | $1.15B |
| Vol-adj net 0DTE | $159.05B | $8.88B |
| Vol-adj net all | $162.96B | $9.78B |
| Missing greeks | 366/912 | 312/968 |
| OI used | 1092944 | 714018 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
