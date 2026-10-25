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

Leave `cci` on (default true) so the run includes the CCI washout family. Set `only_cci` to true to score only that family and skip the older setups. Leave both at the defaults for the full family. The other inputs stay as they are: `days` (default 170), `symbols` (SPY,QQQ), `strikes` (1otm,atm), premium 0.45 to 0.80, `quick` false, half-spread 1 cent or 0.5%, commission 0.65, results branch `edge-hunt-results`.

Results land on the branch `edge-hunt-results` (never main): `results/EDGE_HUNT.md`, `results/edge_hunt_rules.csv`, `results/edge_hunt_trades.csv`. The report has a **CCI washout** section.

The `quick` input (30 sessions) is only a smoke test. The real run uses the `days` input (default 170). Data only. No orders. The option download is the long part. `only_cci` shortens the search. It does not shrink the download.

## Clean Scan replay (research, no orders)

On your phone: open the repo on GitHub, tap **Actions**, tap **Clean Scan replay (real option prices)**, tap **Run workflow**. That starts a fresh run. Do not tap Re-run. Leave the inputs at their defaults unless you mean to change the cost model. This does not start the Clean Scan bot and it does not change `cleanbot.py`.

Results land on the branch `cleanbot-replay-results` (never main): `results/CLEANBOT_REPLAY.md`, `results/cleanbot_replay_trades.csv`.

Inputs: `trades` (default `clean_trades.csv`), `half_spread_cents` (default 1), `half_spread_pct` (default 0.5), `commission` (default 0.65), `results_branch` (default `cleanbot-replay-results`). Data only. No orders.
