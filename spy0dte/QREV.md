# QQQ 0DTE Public reversal bot ("qrev")

The Public account's strategy from Nov 23, 2026. It replaces the SPY Vix Fix plan for Public, so the two accounts never trade the same ticker: Robinhood trades SPY (bot.js), Public trades QQQ (qbot.js).

## Entry (all must be true)
- A fear/greed pane arrow on the QQQ chart, the QQQ call chart or the QQQ put chart, **against** the trend line.
- QQQ moved **$3.00 or more** the other way over the last 15 minutes.
- Stalled: no new day low (calls) / high (puts) in the last 5 bars.
- Candles shrinking: the last 3 bodies average under 0.8× the 10 before them.
- 10:01 AM to 2:00 PM (1:00 PM cutoff for entries on half days is earlier, as in the other bots).

## Contract and exits (live version)
- 0DTE, first-out strike (call = first strike above QQQ, put = first strike below).
- Limit bid 3% under the mid, rounded down, cancelled after 5 minutes.
- **All out at +50%.** −75% stop at the broker. 2-hour max. Flat by 3:08 PM.
- Full port of Public's options buying power (never more than the bot's own money).

## Shadow version (paper only)
1 strike in the money, a third sold at +30%, stop to breakeven, the rest out at minute 15. It runs beside the live version with its own $1,000 paper ledger in `spy0dte/qrev/shadow/`, never sends an order, and its result is in every daily summary. To switch the live bot to it later, set `steps: 2, tp: 0.30, sellFrac: 1/3` in `QR_CFG` in qrev.js.

## Safety
- Safety brake: after a loss of 25% or more, paper only until 5 paper trades win in a row; after a −75% stop, half port until the account is back to its pre-stop balance.
- Day lock (+25% then give back a third), down 30% on the day = stop, a −75% stop = done for the day.
- `clear_review = yes` clears the brake and any review hold.

## Turning it on
- DRY RUN unless the repo variable `QQQ0DTE_PUBLIC_LIVE` is exactly `yes`.
- Workflow: `.github/workflows/qqq0dte_public.yml` (9:20 AM ET start, its own concurrency group).
- Uses the same `PUBLIC_API_SECRET` secret and `PUBLIC_ACCOUNT_ID` variable as the other Public bots.

## Backtest it was picked from (Oct 1 – Nov 13, 2026, $1,000)
- Live version: 8 trades, 8 won, $20,191, no drop. Average dip before paying −18%, average 27 minutes.
- Shadow version: 8 trades, 8 won, $6,409.
- `node spy0dte/replay_qrev.js <folder of QQQ bars files> [from] [to] [shadow]` replays saved QQQ days through this engine.
