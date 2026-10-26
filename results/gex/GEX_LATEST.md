# GEX latest

2026-10-26 13:26:54 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the put wall at 766.00, 0.14 pts (0.02%) away.
QQQ: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the call wall at 715.00, 0.89 pts (0.12%) away.

SPY top |GEX| strikes: 766.00 ($2.18B), 767.00 ($1.26B), 762.00 ($479.76M).
QQQ top |GEX| strikes: 722.00 ($147.80M), 715.00 ($87.80M), 710.00 ($74.23M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 766.14 | 714.11 |
| 0DTE flip |  |  |
| All-expiry flip |  |  |
| 0DTE call wall | 765.00 | 715.00 |
| 0DTE put wall | 766.00 | 722.00 |
| Net GEX 0DTE | -$2.70B | -$176.76M |
| Net GEX all | -$4.30B | -$265.14M |
| Vol-adj net 0DTE | $70.51B | $34.91B |
| Vol-adj net all | $71.87B | $35.44B |
| Missing greeks | 335/796 | 328/764 |
| OI used | 729363 | 380969 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
