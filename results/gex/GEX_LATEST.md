# GEX latest

2026-10-30 12:16:34 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: spot above the 0DTE flip by 50.54 pts (6.68%); nearest wall is the put wall at 755.00, 1.98 pts (0.26%) away.
QQQ: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the put wall at 690.00, 1.85 pts (0.27%) away.

SPY top |GEX| strikes: 755.00 ($2.09B), 760.00 ($1.37B), 750.00 ($1.09B).
QQQ top |GEX| strikes: 690.00 ($2.51B), 695.00 ($683.09M), 700.00 ($556.33M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 756.98 | 691.85 |
| 0DTE flip | 706.44 |  |
| All-expiry flip | 704.16 |  |
| 0DTE call wall | 760.00 | 695.00 |
| 0DTE put wall | 755.00 | 690.00 |
| Net GEX 0DTE | -$6.51B | -$5.60B |
| Net GEX all | -$8.11B | -$6.30B |
| Vol-adj net 0DTE | -$50.06B | -$17.88B |
| Vol-adj net all | -$52.56B | -$18.09B |
| Missing greeks | 386/890 | 351/872 |
| OI used | 1661876 | 1129299 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
