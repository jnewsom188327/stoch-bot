# GEX latest

2026-11-10 14:30:19 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: spot above the 0DTE flip by 12.31 pts (1.64%); the call wall and the put wall are the same distance, 1.51 pts (0.20%) away.
QQQ: spot above the 0DTE flip by 10.04 pts (1.49%); nearest wall is the call wall at 672.00, 0.05 pts (0.01%) away.

SPY top |GEX| strikes: 750.00 ($610.02M), 730.00 ($442.05M), 745.00 ($406.03M).
QQQ top |GEX| strikes: 650.00 ($237.68M), 672.00 ($227.28M), 685.00 ($182.01M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 748.49 | 671.95 |
| 0DTE flip | 736.18 | 661.91 |
| All-expiry flip | 757.80 |  |
| 0DTE call wall | 750.00 | 672.00 |
| 0DTE put wall | 750.00 | 671.00 |
| Net GEX 0DTE | $1.61B | $373.93M |
| Net GEX all | $404.68M | -$114.19M |
| Vol-adj net 0DTE | -$11.89B | -$16.72B |
| Vol-adj net all | -$14.03B | -$18.34B |
| Missing greeks | 407/896 | 396/1046 |
| OI used | 1115025 | 613774 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
