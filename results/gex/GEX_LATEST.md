# GEX latest

2026-10-27 14:04:24 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the call wall at 770.00, 0.52 pts (0.07%) away.
QQQ: spot above the 0DTE flip by 6.29 pts (0.87%); nearest wall is the put wall at 722.00, 1.33 pts (0.18%) away.

SPY top |GEX| strikes: 755.00 ($1.44B), 767.00 ($1.15B), 765.00 ($762.53M).
QQQ top |GEX| strikes: 700.00 ($421.58M), 690.00 ($309.45M), 719.00 ($247.90M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 769.48 | 720.67 |
| 0DTE flip |  | 714.39 |
| All-expiry flip | 699.19 |  |
| 0DTE call wall | 770.00 | 719.00 |
| 0DTE put wall | 767.00 | 722.00 |
| Net GEX 0DTE | -$301.08M | $486.95M |
| Net GEX all | -$2.90B | -$970.39M |
| Vol-adj net 0DTE | $98.74B | $26.04B |
| Vol-adj net all | $96.78B | $25.34B |
| Missing greeks | 306/888 | 309/922 |
| OI used | 1957126 | 1229922 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
