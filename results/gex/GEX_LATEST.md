# GEX latest

2026-11-12 14:23:45 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: spot above the 0DTE flip by 5.56 pts (0.73%); the call wall and the put wall are the same distance, 0.91 pts (0.12%) away.
QQQ: spot above the 0DTE flip by 6.11 pts (0.89%); the call wall and the put wall are the same distance, 0.72 pts (0.10%) away.

SPY top |GEX| strikes: 759.00 ($428.86M), 761.00 ($299.75M), 762.00 ($294.71M).
QQQ top |GEX| strikes: 696.00 ($162.88M), 700.00 ($162.69M), 685.00 ($146.34M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 759.09 | 689.28 |
| 0DTE flip | 753.52 | 683.17 |
| All-expiry flip | 760.80 | 694.27 |
| 0DTE call wall | 760.00 | 690.00 |
| 0DTE put wall | 760.00 | 690.00 |
| Net GEX 0DTE | $1.05B | $374.56M |
| Net GEX all | $1.71B | $688.03M |
| Vol-adj net 0DTE | -$590.38M | $11.27B |
| Vol-adj net all | $220.55M | $11.90B |
| Missing greeks | 363/896 | 309/958 |
| OI used | 1123000 | 674815 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
