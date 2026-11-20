# SPY 0DTE bot (Public.com)

Trades the Edge Stress Test white dots and pane arrows (SPY + call/put; arrows are not traded) on SPY 0DTE options through Public.
**Starts in DRY RUN:** real Public prices, every decision made and logged, no orders sent.

## Where orders go
Prices always come from Public (so marks match the backtest). Orders go to:
- **Public** (default), or
- **Robinhood agent (MCP) account**: set repo variable `SPY0DTE_BROKER` = `robinhood`, then run the **Robinhood login** workflow once (it opens an issue with the sign-in link; paste the `http://localhost:1455/callback?...` address you land on as a comment). The login is saved encrypted in `spy0dte/rh_tokens.enc` and refreshes itself; if it ever expires, the summary says so: run the login again. On Robinhood the first entry is 9:45 (Robinhood refuses option stop orders before then) and trade approvals must be off for the agent account.

## Turn it on / off
| What | Where |
|---|---|
| API key | Secret `PUBLIC_API_SECRET` (already set) |
| Go LIVE | Settings → Secrets and variables → Actions → **Variables** → `SPY0DTE_LIVE` = `yes` |
| Back to dry run | Delete `SPY0DTE_LIVE` (or set it to anything but `yes`) |
| Pick an account (only if you have more than one) | Variable `PUBLIC_ACCOUNT_ID` |
| Test the key + marks | Actions → SPY 0DTE bot → Run workflow → mode `check` |
| Clear the 2-of-10 hold | Run workflow, mode `run`, clear_review `yes` |

Runs by itself every weekday: starts 9:20 ET, works 9:25–3:10, posts a summary as a GitHub issue (you get the GitHub notification).

## Rules (engine.js)
- **Marks:** white dots and pane arrows (SPY pane, 1-out call chart, 1-out put chart). No arrows. Read with the CORE code from the Edge Stress Test's `build/build_day.js` (byte-for-byte copy here, sha256-checked every run).
- **Take a mark only if:** SPY trend line your way, SPY shading not against you, before 1:00 PM (after 9:40, as in the backtest). One trade at a time; marks while a trade is open are ignored, not queued; a new qualifying mark replaces an unfilled limit. The 9:45–9:48 dots that print late are skipped.
- **Contract + size by trend strength (option 2, Nov 20 2026):** 0DTE. **Strong trend** = SPY moved $0.30+ your way over the last 30 minutes AND EMA13 is $0.10+ past EMA34 your way (SPY 1-minute closes from 9:30): **1 strike in the money** (2 strikes in from the old first-out strike), **full port**. **Weak trend** (anything else, including marks before 10:01 with no 30-minute reading): **3 strikes in the money** (4 in), **half the port**. Skip if under $0.80, spread over 10%, or the quote is over 30 s old. Off switch: `trendSizing: false` in engine.js goes back to the first-out strike at full port.
- **Entry:** limit 5% under the option's mid at the mark (rounded down to the cent), sent the same minute; cancelled after 5 minutes. Never a market order.
- **Size:** full port on strong-trend marks, half on weak-trend marks (see above). Live = the options buying power Public reports at that moment (margin account, so unsettled proceeds count), capped at the bot's own money (that morning's buying power + the day's closed P&L) so it never borrows. Dry run = the bot's paper balance, starting $1,000. No ladder, no pullouts, no 1DTE.
- **Exits:** −75% stop at Public the moment it fills; it must show as working at Public within 30 s, or the bot sells and stops for the day. At +10% sell half and move the stop to breakeven (1 contract: sell it all). Rest out at minute 15. White-dot trade with an x: everything out at minute 10. Out by 120 minutes, flat by 3:08. Sells are limits at the bid.
- **Shutoffs (after each closed trade):** a −75% stop = done for the day; day down 30%; day up 25% then gives back a third of the best; 2 of the last 10 trades at −75% = hold until you clear it; any error, rejected stop, or position mismatch = close everything and stop for the day.

## Safety close (separate workflow, 3:30 PM ET)
`SPY 0DTE safety close` checks the Public account every weekday at 3:30 PM ET and closes **any** open option position (not just the bot's), cancelling that contract's open orders first, then a limit at the bid. It runs whether or not the bot is running, and acts on the real account even in dry run. It opens a GitHub issue only if it had to close something or something failed. Off switch: repo variable `SPY0DTE_SAFETY` = `off`.

## Files
`bot.js` the minute loop · `engine.js` rules · `marks.js` live marks · `core.js` loads CORE from `build_day.js` · `public.js` API · `ledger.js` money · `summary.js` daily report · `rh.js` Robinhood broker + login store · `rh_login.js` one-time sign-in · `safety.js` 3:30 safety close
State: `state.json` · logs: `logs/<day>.jsonl` · `trades.csv` · `summaries/<day>.md`

## Tests (no key needed)
- `node spy0dte/test_parity.js`: replays every `results/bars_*.json` minute by minute; the live marks must equal `build_day.js` marks.
- `node spy0dte/replay.js compare`: the engine on saved days with backtest settings, to line up with the Edge Stress Test trade by trade.
- `node spy0dte/test_bot_mock.js 2026-11-17 dry|live`: the full bot against a fake Public on a fast clock.
