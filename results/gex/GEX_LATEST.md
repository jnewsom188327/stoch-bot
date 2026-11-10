# GEX latest

2026-11-10 12:14:16 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: spot above the 0DTE flip by 8.04 pts (1.08%); nearest wall is the put wall at 745.00, 2.30 pts (0.31%) away.
QQQ: spot above the 0DTE flip by 6.44 pts (0.96%); nearest wall is the put wall at 671.00, 0.22 pts (0.03%) away.

SPY top |GEX| strikes: 730.00 ($505.26M), 745.00 ($406.71M), 750.00 ($405.22M).
QQQ top |GEX| strikes: 650.00 ($252.01M), 685.00 ($168.44M), 672.00 ($134.14M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 747.30 | 670.78 |
| 0DTE flip | 739.26 | 664.34 |
| All-expiry flip |  |  |
| 0DTE call wall | 750.00 | 672.00 |
| 0DTE put wall | 745.00 | 671.00 |
| Net GEX 0DTE | $1.10B | $260.78M |
| Net GEX all | -$276.60M | -$240.12M |
| Vol-adj net 0DTE | -$41.15B | -$22.97B |
| Vol-adj net all | -$44.94B | -$24.53B |
| Missing greeks | 384/896 | 399/1048 |
| OI used | 1115025 | 613398 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
