# GEX latest

2026-11-04 11:30:48 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the call wall at 765.00, 0.23 pts (0.03%) away.
QQQ: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the call wall at 690.00, 1.77 pts (0.26%) away.

SPY top |GEX| strikes: 767.00 ($502.43M), 750.00 ($420.61M), 770.00 ($411.89M).
QQQ top |GEX| strikes: 680.00 ($365.91M), 675.00 ($350.52M), 685.00 ($228.03M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 764.77 | 691.77 |
| 0DTE flip |  |  |
| All-expiry flip |  |  |
| 0DTE call wall | 765.00 | 690.00 |
| 0DTE put wall | 767.00 | 685.00 |
| Net GEX 0DTE | -$216.49M | -$195.72M |
| Net GEX all | -$617.53M | -$2.11B |
| Vol-adj net 0DTE | -$6.01B | -$6.30B |
| Vol-adj net all | -$6.50B | -$7.98B |
| Missing greeks | 381/900 | 270/832 |
| OI used | 1104623 | 1021041 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
