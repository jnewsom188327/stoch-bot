# GEX latest

2026-10-28 14:23:54 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: spot below the 0DTE flip by 0.26 pts (0.03%); nearest wall is the call wall at 771.00, 0.81 pts (0.11%) away.
QQQ: spot above the 0DTE flip by 4.70 pts (0.65%); the call wall and the put wall are the same distance, 1.42 pts (0.20%) away.

SPY top |GEX| strikes: 765.00 ($926.24M), 755.00 ($820.43M), 760.00 ($448.80M).
QQQ top |GEX| strikes: 700.00 ($247.03M), 730.00 ($237.04M), 690.00 ($214.35M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 770.19 | 721.42 |
| 0DTE flip | 770.45 | 716.72 |
| All-expiry flip | 700.78 |  |
| 0DTE call wall | 771.00 | 720.00 |
| 0DTE put wall | 765.00 | 720.00 |
| Net GEX 0DTE | $590.94M | $317.03M |
| Net GEX all | -$585.88M | -$214.81M |
| Vol-adj net 0DTE | -$2.98B | $423.70M |
| Vol-adj net all | -$4.59B | -$436.42M |
| Missing greeks | 337/886 | 325/888 |
| OI used | 1886450 | 1176188 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
