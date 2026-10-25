# stoch-bot

## 0DTE scalp on real option prices

Phone steps and the example inputs (vix_min 16, late-day 1otm): [docs/README.md](docs/README.md).

## Intraday GEX logger (log only)

`gex_logger.py` records dealer gamma exposure for SPY and QQQ about every five minutes during the regular session. It does not place orders and it does not change the trading bots.

The scheduled workflow commits the CSVs to the `gex-data` branch, never to `main`. Assumptions, the dollar-GEX formula, and the pre-declared analysis plan are in [docs/GEX.md](docs/GEX.md).

```bash
python3 gex_logger.py --dry-run --out /tmp/gex-dry
python3 -m unittest tests.test_gex
```

## Edge hunt (research, no orders)

On your phone: open the repo on GitHub, tap **Actions**, tap **Edge hunt (walk-forward, real option prices)**, tap **Run workflow**. That starts a fresh run. Do not tap Re-run.

Results land on the branch `edge-hunt-results` (never main): `results/EDGE_HUNT.md`, `results/edge_hunt_rules.csv`, `results/edge_hunt_trades.csv`.

The `quick` input (30 sessions) is only a smoke test. The real run uses the `days` input (default 170). Data only. No orders.
