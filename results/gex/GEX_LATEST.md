# GEX latest

2026-10-30 14:16:05 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: spot above the 0DTE flip by 46.86 pts (6.22%); the call wall and the put wall are the same distance, 2.88 pts (0.38%) away.
QQQ: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the put wall at 690.00, 3.62 pts (0.53%) away.

SPY top |GEX| strikes: 750.00 ($3.05B), 755.00 ($1.98B), 745.00 ($638.00M).
QQQ top |GEX| strikes: 690.00 ($2.03B), 685.00 ($870.21M), 680.00 ($482.84M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 752.88 | 686.38 |
| 0DTE flip | 706.02 |  |
| All-expiry flip |  |  |
| 0DTE call wall | 750.00 | 695.00 |
| 0DTE put wall | 750.00 | 690.00 |
| Net GEX 0DTE | -$8.84B | -$4.86B |
| Net GEX all | -$10.28B | -$5.54B |
| Vol-adj net 0DTE | -$93.30B | -$29.85B |
| Vol-adj net all | -$97.05B | -$30.55B |
| Missing greeks | 432/890 | 331/840 |
| OI used | 1620566 | 1128686 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
