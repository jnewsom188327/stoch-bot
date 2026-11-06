# GEX latest

2026-11-06 09:49:24 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the put wall at 750.00, 9.03 pts (1.22%) away.
QQQ: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the call wall at 655.00, 8.18 pts (1.23%) away.

SPY top |GEX| strikes: 750.00 ($701.75M), 740.00 ($648.44M), 735.00 ($520.82M).
QQQ top |GEX| strikes: 675.00 ($459.00M), 680.00 ($208.38M), 660.00 ($190.91M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 740.97 | 663.18 |
| 0DTE flip |  |  |
| All-expiry flip |  |  |
| 0DTE call wall | 760.00 | 655.00 |
| 0DTE put wall | 750.00 | 675.00 |
| Net GEX 0DTE | -$3.63B | -$2.12B |
| Net GEX all | -$4.77B | -$2.46B |
| Vol-adj net 0DTE | -$2.32B | -$1.72B |
| Vol-adj net all | -$3.52B | -$2.04B |
| Missing greeks | 282/896 | 293/1046 |
| OI used | 989845 | 931305 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
