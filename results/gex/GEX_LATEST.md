# GEX latest

2026-10-28 15:15:52 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: spot above the 0DTE flip by 1.00 pts (0.13%); nearest wall is the call wall at 771.00, 0.54 pts (0.07%) away.
QQQ: spot above the 0DTE flip by 6.35 pts (0.88%); the call wall and the put wall are the same distance, 2.86 pts (0.40%) away.

SPY top |GEX| strikes: 765.00 ($934.94M), 755.00 ($745.93M), 780.00 ($435.98M).
QQQ top |GEX| strikes: 730.00 ($256.99M), 729.00 ($234.12M), 740.00 ($230.33M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 770.46 | 722.86 |
| 0DTE flip | 769.46 | 716.51 |
| All-expiry flip | 704.19 | 743.86 |
| 0DTE call wall | 771.00 | 720.00 |
| 0DTE put wall | 765.00 | 720.00 |
| Net GEX 0DTE | $794.52M | $396.24M |
| Net GEX all | -$193.79M | $140.96M |
| Vol-adj net 0DTE | -$6.61B | $5.76B |
| Vol-adj net all | -$7.77B | $5.38B |
| Missing greeks | 368/886 | 340/888 |
| OI used | 1886450 | 1153756 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
