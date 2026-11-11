# GEX latest

2026-11-11 09:51:57 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: spot below the 0DTE flip by 1.99 pts (0.26%); nearest wall is the put wall at 753.00, 2.89 pts (0.38%) away.
QQQ: spot above the 0DTE flip by 0.20 pts (0.03%); nearest wall is the call wall at 690.00, 5.16 pts (0.75%) away.

SPY top |GEX| strikes: 745.00 ($332.82M), 760.00 ($297.81M), 744.00 ($228.60M).
QQQ top |GEX| strikes: 685.00 ($138.61M), 696.00 ($119.42M), 700.00 ($109.99M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 755.89 | 684.84 |
| 0DTE flip | 757.88 | 684.64 |
| All-expiry flip |  | 702.16 |
| 0DTE call wall | 760.00 | 690.00 |
| 0DTE put wall | 753.00 | 675.00 |
| Net GEX 0DTE | $236.97M | $207.98M |
| Net GEX all | -$171.17M | $226.07M |
| Vol-adj net 0DTE | $3.66B | $372.68M |
| Vol-adj net all | $3.84B | $525.65M |
| Missing greeks | 336/904 | 332/990 |
| OI used | 1090376 | 707074 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
