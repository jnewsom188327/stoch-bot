# GEX latest

2026-11-10 13:34:33 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: spot above the 0DTE flip by 1.69 pts (0.23%); nearest wall is the call wall at 748.00, 0.97 pts (0.13%) away.
QQQ: spot above the 0DTE flip by 1.23 pts (0.18%); nearest wall is the put wall at 671.00, 0.67 pts (0.10%) away.

SPY top |GEX| strikes: 730.00 ($538.06M), 745.00 ($421.31M), 750.00 ($384.68M).
QQQ top |GEX| strikes: 650.00 ($260.29M), 672.00 ($171.11M), 685.00 ($165.38M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 747.03 | 670.33 |
| 0DTE flip | 745.34 | 669.09 |
| All-expiry flip |  |  |
| 0DTE call wall | 748.00 | 672.00 |
| 0DTE put wall | 745.00 | 671.00 |
| Net GEX 0DTE | $917.96M | $253.95M |
| Net GEX all | -$566.23M | -$253.32M |
| Vol-adj net 0DTE | -$59.60B | -$28.72B |
| Vol-adj net all | -$64.17B | -$30.77B |
| Missing greeks | 374/896 | 416/1048 |
| OI used | 1115025 | 613398 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
