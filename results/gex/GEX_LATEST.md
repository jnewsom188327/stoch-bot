# GEX latest

2026-10-27 13:26:28 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the call wall at 770.00, 0.40 pts (0.05%) away.
QQQ: spot above the 0DTE flip by 2.83 pts (0.39%); nearest wall is the put wall at 722.00, 1.21 pts (0.17%) away.

SPY top |GEX| strikes: 755.00 ($1.44B), 767.00 ($1.11B), 765.00 ($755.49M).
QQQ top |GEX| strikes: 700.00 ($422.73M), 690.00 ($309.27M), 719.00 ($248.48M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 769.60 | 720.79 |
| 0DTE flip |  | 717.96 |
| All-expiry flip | 697.09 |  |
| 0DTE call wall | 770.00 | 719.00 |
| 0DTE put wall | 767.00 | 722.00 |
| Net GEX 0DTE | -$435.69M | $474.70M |
| Net GEX all | -$3.00B | -$977.06M |
| Vol-adj net 0DTE | $77.02B | $28.61B |
| Vol-adj net all | $75.03B | $28.02B |
| Missing greeks | 323/888 | 301/922 |
| OI used | 1957126 | 1229922 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
