# GEX latest

2026-10-28 13:03:59 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: spot above the 0DTE flip by 1.35 pts (0.17%); nearest wall is the call wall at 772.00, 0.30 pts (0.04%) away.
QQQ: spot above the 0DTE flip by 6.52 pts (0.90%); the call wall and the put wall are the same distance, 3.09 pts (0.43%) away.

SPY top |GEX| strikes: 765.00 ($819.22M), 755.00 ($721.41M), 780.00 ($527.65M).
QQQ top |GEX| strikes: 730.00 ($257.09M), 740.00 ($239.02M), 729.00 ($224.87M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 771.70 | 723.09 |
| 0DTE flip | 770.35 | 716.57 |
| All-expiry flip | 792.01 | 754.82 |
| 0DTE call wall | 772.00 | 720.00 |
| 0DTE put wall | 765.00 | 720.00 |
| Net GEX 0DTE | $734.84M | $350.82M |
| Net GEX all | $242.85M | $54.66M |
| Vol-adj net 0DTE | $6.25B | $2.78B |
| Vol-adj net all | $5.89B | $2.38B |
| Missing greeks | 308/884 | 316/888 |
| OI used | 1884905 | 1153756 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
