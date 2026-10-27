# GEX latest

2026-10-27 12:41:20 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the call wall at 770.00, 0.34 pts (0.04%) away.
QQQ: spot above the 0DTE flip by 6.47 pts (0.90%); nearest wall is the put wall at 722.00, 0.88 pts (0.12%) away.

SPY top |GEX| strikes: 755.00 ($1.42B), 767.00 ($1.13B), 765.00 ($694.48M).
QQQ top |GEX| strikes: 700.00 ($415.39M), 690.00 ($305.03M), 719.00 ($200.02M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 769.66 | 721.12 |
| 0DTE flip |  | 714.64 |
| All-expiry flip | 699.59 |  |
| 0DTE call wall | 770.00 | 719.00 |
| 0DTE put wall | 767.00 | 722.00 |
| Net GEX 0DTE | -$348.06M | $486.44M |
| Net GEX all | -$2.75B | -$902.64M |
| Vol-adj net 0DTE | $90.42B | $34.74B |
| Vol-adj net all | $88.92B | $34.35B |
| Missing greeks | 300/888 | 301/920 |
| OI used | 1957126 | 1227712 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
