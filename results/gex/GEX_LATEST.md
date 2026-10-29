# GEX latest

2026-10-29 12:22:16 ET. Log only. This run places no orders.

Sign convention: dealers long calls (call GEX positive) and short puts (put GEX negative). Dollar GEX is the hedge notional for a 1% move in the underlying. Open interest is the overnight print, so this is an estimate.

SPY: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the put wall at 770.00, 0.85 pts (0.11%) away.
QQQ: no 0DTE gamma flip (cumulative GEX did not cross zero); nearest wall is the put wall at 718.00, 2.49 pts (0.35%) away.

SPY top |GEX| strikes: 765.00 ($1.29B), 760.00 ($409.44M), 775.00 ($342.51M).
QQQ top |GEX| strikes: 700.00 ($354.01M), 710.00 ($323.40M), 715.00 ($280.86M).

|  | SPY | QQQ |
|---|---:|---:|
| Spot | 769.15 | 715.51 |
| 0DTE flip |  |  |
| All-expiry flip | 706.37 |  |
| 0DTE call wall | 768.00 | 725.00 |
| 0DTE put wall | 770.00 | 718.00 |
| Net GEX 0DTE | -$111.13M | -$418.91M |
| Net GEX all | -$1.55B | -$2.31B |
| Vol-adj net 0DTE | $5.87B | $3.08B |
| Vol-adj net all | $3.64B | $728.59M |
| Missing greeks | 334/884 | 313/850 |
| OI used | 1714109 | 1182529 |

The one-line reading uses the 0DTE flip and walls when that expiry is in the snapshot. CSV distances are level minus spot: positive means the level is above spot.

Pine defaults: `results/gex/GEX_PINE_SNIPPET.txt`.
