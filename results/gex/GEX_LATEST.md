# GEX latest

2026-10-27 11:58:33 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the call wall at 770.00, 0.38 pts (0.05%) away.
QQQ: spot above the 0DTE flip by 11.65 pts (1.62%); nearest wall is the put wall at 722.00, 0.41 pts (0.06%) away.

SPY top |GEX| strikes: 755.00 ($1.34B), 767.00 ($849.34M), 765.00 ($676.67M).
QQQ top |GEX| strikes: 700.00 ($400.58M), 690.00 ($295.55M), 729.00 ($168.69M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 770.38 | 721.59 |
| 0DTE flip |  | 709.94 |
| All-expiry flip |  |  |
| 0DTE call wall | 770.00 | 719.00 |
| 0DTE put wall | 767.00 | 722.00 |
| Net GEX 0DTE | -$67.57M | $521.86M |
| Net GEX all | -$2.15B | -$806.33M |
| Vol-adj net 0DTE | $87.97B | $32.22B |
| Vol-adj net all | $87.33B | $31.72B |
| Missing greeks | 319/886 | 312/920 |
| OI used | 1951606 | 1227712 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
