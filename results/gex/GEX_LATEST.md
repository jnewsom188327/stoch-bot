# GEX latest

2026-11-10 10:29:40 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: spot above the 0DTE flip by 9.61 pts (1.28%); nearest wall is the call wall at 750.00, 0.80 pts (0.11%) away.
QQQ: spot above the 0DTE flip by 4.67 pts (0.69%); nearest wall is the call wall at 678.00, 2.08 pts (0.31%) away.

SPY top |GEX| strikes: 730.00 ($482.78M), 750.00 ($418.30M), 745.00 ($365.07M).
QQQ top |GEX| strikes: 650.00 ($203.31M), 685.00 ($197.50M), 678.00 ($89.93M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 749.20 | 675.92 |
| 0DTE flip | 739.59 | 671.25 |
| All-expiry flip | 799.08 |  |
| 0DTE call wall | 750.00 | 678.00 |
| 0DTE put wall | 755.00 | 671.00 |
| Net GEX 0DTE | $1.05B | $276.78M |
| Net GEX all | $14.77M | -$60.63M |
| Vol-adj net 0DTE | $4.15B | $3.54B |
| Vol-adj net all | $2.83B | $3.05B |
| Missing greeks | 362/896 | 357/1028 |
| OI used | 1115025 | 615761 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
