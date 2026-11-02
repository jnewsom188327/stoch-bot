# GEX latest

2026-11-02 15:46:46 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the put wall at 755.00, 1.31 pts (0.17%) away.
QQQ: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the put wall at 685.00, 2.11 pts (0.31%) away.

SPY top |GEX| strikes: 755.00 ($497.41M), 767.00 ($393.34M), 750.00 ($302.06M).
QQQ top |GEX| strikes: 680.00 ($354.90M), 685.00 ($241.65M), 690.00 ($76.27M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 753.69 | 682.89 |
| 0DTE flip |  |  |
| All-expiry flip |  |  |
| 0DTE call wall | 760.00 | 725.00 |
| 0DTE put wall | 755.00 | 685.00 |
| Net GEX 0DTE | -$1.20B | -$449.82M |
| Net GEX all | -$2.62B | -$995.69M |
| Vol-adj net 0DTE | -$113.82B | -$35.02B |
| Vol-adj net all | -$120.23B | -$37.07B |
| Missing greeks | 320/640 | 302/688 |
| OI used | 428172 | 316982 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
