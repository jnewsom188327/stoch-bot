# GEX latest

2026-10-28 13:44:46 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: spot above the 0DTE flip by 0.67 pts (0.09%); nearest wall is the call wall at 772.00, 1.01 pts (0.13%) away.
QQQ: spot above the 0DTE flip by 2.82 pts (0.39%); the call wall and the put wall are the same distance, 2.18 pts (0.30%) away.

SPY top |GEX| strikes: 765.00 ($877.31M), 755.00 ($753.75M), 780.00 ($472.57M).
QQQ top |GEX| strikes: 730.00 ($245.26M), 700.00 ($244.88M), 740.00 ($218.59M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 770.99 | 722.18 |
| 0DTE flip | 770.32 | 719.36 |
| All-expiry flip | 699.65 |  |
| 0DTE call wall | 772.00 | 720.00 |
| 0DTE put wall | 765.00 | 720.00 |
| Net GEX 0DTE | $698.30M | $319.52M |
| Net GEX all | -$135.36M | -$158.95M |
| Vol-adj net 0DTE | $4.33B | $2.56B |
| Vol-adj net all | $3.44B | $1.85B |
| Missing greeks | 310/886 | 327/888 |
| OI used | 1886450 | 1176188 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
