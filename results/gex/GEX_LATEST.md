# GEX latest

2026-11-03 10:29:53 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: spot above the 0DTE flip by 4.34 pts (0.58%); nearest wall is the put wall at 755.00, 0.33 pts (0.04%) away.
QQQ: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the call wall at 690.00, 3.85 pts (0.56%) away.

SPY top |GEX| strikes: 740.00 ($716.66M), 750.00 ($380.95M), 755.00 ($323.05M).
QQQ top |GEX| strikes: 680.00 ($471.27M), 675.00 ($326.28M), 713.00 ($212.31M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 754.67 | 686.15 |
| 0DTE flip | 750.33 |  |
| All-expiry flip |  |  |
| 0DTE call wall | 750.00 | 690.00 |
| 0DTE put wall | 755.00 | 680.00 |
| Net GEX 0DTE | $7.14M | -$284.92M |
| Net GEX all | -$3.00B | -$2.13B |
| Vol-adj net 0DTE | $10.43B | $3.56B |
| Vol-adj net all | $8.02B | $1.80B |
| Missing greeks | 370/888 | 250/840 |
| OI used | 1070754 | 899569 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
