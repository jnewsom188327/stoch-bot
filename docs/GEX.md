# Intraday GEX logger

This logger records an estimate of dealer gamma exposure (GEX) for SPY and QQQ during the regular session. It is a forward-looking sample for a later confluence check against 0DTE diamond / Vix Fix signals. It does not place orders, it does not read or write the bot trade logs, and the workflow pushes data only to the `gex-data` branch.

SPX options are not on Alpaca. SPY is the S&P proxy. A SPY level is not an SPX level: the prices differ by roughly an order of magnitude, and SPY has dividends. QQQ is recorded directly.

## What a run does

During regular hours the script, for each of SPY and QQQ:

1. Reads the underlying price from Alpaca stock data (`/v2/stocks/{symbol}/trades/latest`, IEX feed, the same feed the other bots use). If that trade is missing it falls back to the stock snapshot.
2. Reads option contracts from the trading API `GET /v2/options/contracts` (open interest, size, strike, type, expiration). Pages are followed until `next_page_token` is empty, with a cap (`GEX_MAX_PAGES`, default 8).
3. Reads option snapshots from `GET /v1beta1/options/snapshots/{underlying}` (greeks, implied volatility, quote, trade, daily bar volume). Same paging and the same cap.
4. Appends one summary row and the per-contract rows, then rewrites the short markdown and the Pine snippet.

Expiries kept: 0DTE (expiration date equals the New York session date) when that expiry exists, the next expiry after today, and `GEX_EXTRA_EXPIRIES` further expiries (default 2, so four expiries on a normal day). Strikes outside `spot * (1 ± GEX_STRIKE_WINDOW_PCT)` are not requested. The default window is 10% either side, so a wall sitting further out is invisible. That default is part of the sample. Do not widen it after looking at results and then mix the two windows in one test.

Hosts, matching the alpaca-py clients already used in this repo (`TradingClient(..., paper=True)` and the data clients):

| Use | Base URL |
|---|---|
| Clock, calendar, contracts (paper trading API) | `https://paper-api.alpaca.markets` |
| Stock and option market data | `https://data.alpaca.markets` |

Secrets are `ALPACA_KEY` and `ALPACA_SECRET`, the same names as the other workflows. They are request headers only. The logger has no order call and no `/v2/orders` path.

A 429 or a 5xx is retried with `Retry-After` or a short backoff. Anything else fails the run and writes nothing, so a half-finished chain is not appended.

## Market hours

GitHub's cron is UTC and does not move when the US switches between EST and EDT. The workflow fires every five minutes from 13:00 through 21:55 UTC on weekdays. That covers 09:30–16:00 New York time in both EST (14:30–21:00 UTC) and EDT (13:30–20:00 UTC).

The script itself decides whether to record anything, using Alpaca:

- `GET /v2/calendar` for today's session. An empty calendar (holiday, or weekend) exits. The row's `open` and `close` are the session bounds, so an early close stops the log at that close rather than at 16:00.
- `GET /v2/clock`. `is_open` must be true. Alpaca sets that flag only during the regular session.

Outside the session the process exits without writing a file and without a commit. A concurrency group keeps two runs from publishing at once. If a push is rejected, the publisher checks out the latest `gex-data` tip and appends this snapshot again. Rows are deduped on `(ticker, timestamp_et)`, so a retry does not double-count. The push ref is `gex-data` only.

Scheduled workflows run from the default branch after the workflow file is merged. Until then the cron does not fire.

## Formula and sign

For each contract:

```
sign = +1 call, -1 put
GEX  = sign * gamma * open_interest * size * spot^2 * 0.01
```

This is dollar hedge notional for a 1% move in the underlying. `size` is the contract multiplier (100 when the contract omits it). Gamma from Alpaca is used when it is a positive finite number (`gamma_source=alpaca`).

**Sign convention, stated as an assumption:** dealers are treated as long calls and short puts (`sign_convention=dealer_long_calls_short_puts`), which is the usual retail GEX dashboard convention. Call GEX is positive (stabilizing). Put GEX is negative (destabilizing). Net GEX above zero means this assumption says dealers are net long gamma. This is not something Alpaca tells us. Customers and dealers both take both sides. If the sign is backwards, the study below is designed to fail rather than to be quietly reversed.

When Alpaca does not send a usable gamma, gamma is computed with European Black-Scholes from the snapshot IV and, if IV is also missing, from the quote mid (bid/ask mid, else the last trade). The fallback uses r = 0, q = 0, and a 365-day year. Time is measured to 16:00 New York on the expiration date, with a one-minute floor so gamma does not explode in the last minute. SPY and QQQ options are American; the fallback ignores early exercise. Those rows are counted in `n_missing_greeks` and `n_gamma_bs_fallback`, and `gamma_source` is `bs_iv` or `bs_mid`. Contracts with no gamma and no usable price contribute to open interest and to the missing count, and they contribute nothing to GEX.

Columns:

- `net_gex_0dte` / `net_gex_all` sum the signed dollar GEX. `all` means every expiry this run fetched, not every listed expiry in the market. Blank (not zero) when no contract in that scope had a gamma.
- Volume-adjusted columns repeat the same formula with `open_interest + today's daily-bar volume` in place of open interest. Volume counts opens and closes, buys and sells, so this is an activity weight, not a true position update. It is stored beside the open-interest figure and is not part of the confirmatory test.
- Gamma flip (`gamma_flip_0dte`, `gamma_flip_all`) is the zero-cross of cumulative signed GEX, summed from the lowest strike upward, linearly interpolated between the strikes on either side of the cross. If the cumulative sum crosses zero more than once, the cross closest to spot is kept. `flip_method` is `cumulative_from_low_strike`.
- `gamma_flip_*_shifted` recomputes Black-Scholes gamma as if spot sat on each strike (same IV, same time, r = 0, q = 0) and finds the zero of that net-GEX curve closest to the real spot. It is left blank unless IV covers at least half the open interest. Method name: `spot_shifted_bs_r0_q0`. The cumulative flip is the one the markdown and the Pine snippet use.
- Call wall: the strike with the largest call GEX (the most positive call contribution).
- Put wall: the strike with the largest put exposure, which under this sign convention is the most negative put GEX. The CSV stores that signed (negative) number in `put_wall_*_gex`.
- Top 3 strikes are the three strikes with the largest absolute net GEX across every fetched expiry (`top_strikes_scope=all`). Ties break toward the strike closer to spot, then the lower strike.
- Distances are `level - spot` in points and in percent of spot (`0.30` means 0.30 percent). Positive means the level is above spot.
- `total_oi` is the open interest on the contracts that were fetched, including ones with missing greeks. `n_contracts` is that count.

The one-line reading and the Pine defaults use the 0DTE flip, call wall, and put wall when the snapshot contains any 0DTE contracts. Otherwise they fall back to the all-expiry figures and the reading says so.

Pine v6 cannot draw `hline` from an `input.float`, so the snippet plots a constant input, which is a horizontal line. Paste `results/gex/GEX_PINE_SNIPPET.txt` on a SPY or QQQ chart. Regenerate from a CSV with `python3 gex_logger.py --pine --out results/gex`.

## Files

On `gex-data` (created by the workflow, not by a push to `main`):

| Path | What |
|---|---|
| `results/gex/gex_levels.csv` | One row per ticker per snapshot. |
| `results/gex/gex_strikes_YYYY-MM-DD.csv.gz` | One row per contract per snapshot for that New York date: ticker, time, expiry, strike, type, oi, volume, gamma, iv, gex, and the fields needed to recompute. |
| `results/gex/GEX_LATEST.md` | Rewritten each run. Short table plus one sentence per ticker. |
| `results/gex/GEX_PINE_SNIPPET.txt` | Rewritten each run. Pine v6 snippet. |

Timestamps are `YYYY-MM-DD HH:MM:SS` in America/New_York and UTC with a `Z` suffix. The runner clock is converted with `America/New_York`; it is not Alpaca's clock timestamp.

## Caveats (do not skip these)

- Open interest on Alpaca updates overnight. Intraday GEX moves only because spot, IV, gamma, and the volume add-on move. It is an estimate of a positioning snapshot, not a live dealer book.
- The dealer sign is an assumption. See above.
- Alpaca does not provide historical open interest, so there is no backtest on past weeks. The plan is to collect forward and only then look.
- The strike window and the expiry cap throw away far strikes and far expiries. A wall outside the window cannot appear.
- Alpaca gamma (when present) and the Black-Scholes fallback are different models. The `gamma_source` column says which one was used. Indicative quotes (the default `GEX_OPTION_FEED=indicative`) are the free feed; greeks are often missing and the fallback fills some of them. An account with OPRA can set `GEX_OPTION_FEED=opra`. The stock feed stays IEX unless `GEX_STOCK_FEED` is changed, consistent with the other bots, so the spot can differ slightly from a consolidated print.
- GitHub cron can fire late. The timestamp is when the script ran. A duplicate `(ticker, timestamp_et)` is not appended.
- Nothing here is a trade signal. The Pine lines are a visual aid.

## Pre-declared analysis

Written before any GEX sample existed. These rules are the confirmatory study. Do not edit them after looking at the collected returns. If something has to change (a formula bug, a broken column), add a dated note at the bottom, discard the sample, and start the 15 + 5 session count over. Do not mix two formulas in one sample. Do not flip the sign convention because the first look went the wrong way; that would be a new study.

### Question

Do YOURS-book diamond signals (the AGREE DOTS diamond, which already requires the Vix Fix turn) do better when they print near a recorded wall, or on a pre-declared side of the 0DTE gamma flip, than the other diamonds and than same-clock random entries?

"Better" means a higher average trade-aligned underlying return. Not win rate, not option P&L. This logger does not store a clean option mark series. An option-P&L study would be a new pre-registration.

### Sample

- Source of levels: `gex_levels.csv` on `gex-data`, columns as written by the logger that collected them. Confirmatory columns are the 0DTE ones: `gamma_flip_0dte`, `call_wall_0dte`, `put_wall_0dte`, `net_gex_0dte`, `spot`, `timestamp_et`, `ticker`.
- Source of signals: `diamond_signals.csv` in this repo. Columns used: `date`, `closed`, `book`, `ticker`, `tf`, `diamond`, `first`. Signal time is `date` plus `closed` (candle close, `HH:MM`) in America/New_York. Direction is +1 for `GREEN` and -1 for `RED`, matching the bot (green = long / calls, red = short / puts).
- Confirmatory book is `YOURS` only. `TUNED` may be repeated later with the same rules as an exploratory copy. A TUNED result cannot be swapped in if YOURS is flat.
- Collapse: among YOURS rows for the same `(date, ticker, 5-minute bucket)`, keep the smallest `tf` (1, then 2, then 3, then 5). The bucket is the clock time floored to 5 minutes. This stops four charts from counting one idea four times.
- Eligible session: a New York date in the GEX file where both SPY and QQQ have at least 30 snapshots, the first snapshot is at or before 10:00 ET, and the last is at or after 15:30 ET. Anything else (early close, holiday, broken log) is dropped. Dropped days are not back-filled.
- Window, in calendar order of eligible sessions from the first date in the file: sessions 1–15 are the analysis window, sessions 16–20 are the holdout. No peeking at holdout returns while writing code that touches the analysis window. If 20 eligible sessions are not yet in the file, wait. Do not analyze a shorter window and then add days.
- Join: the GEX row for that ticker whose `timestamp_et` is closest to the signal time, maximum gap 7 minutes. If none, the signal is excluded and counted. If more than 30% of collapsed signals fail the join, the study is inconclusive.
- 60-minute outcome: spot from the matched GEX row, and spot from the GEX row closest to 60 minutes later, same ticker and same date, maximum gap 10 minutes. If the later row is missing, that signal is dropped from this outcome only.
- Trade-aligned return in percent: `(spot_later - spot_now) / spot_now * direction * 100`.

### Same-time random entries

For each ticker and each 5-minute clock bucket, the baseline pool is every GEX row in the analysis window in that bucket. Each row gets a direction of +1 or -1 from SHA-256 of `20261025|{ticker}|{timestamp_et}`, first 4 bytes as a big-endian integer, even = short, odd = long. The baseline is the mean trade-aligned 60-minute return of that pool (same 60-minute rule). The seed stays 20261025. This is the "same clock, random direction" entry, not a reshuffle of the diamond days.

### Hypotheses (favored side is fixed now)

- **H1 flip.** Favored: spot below `gamma_flip_0dte` (the short-gamma side under this convention). Unfavored: spot above the flip. Signals with no flip, or spot equal to the flip, are excluded from H1 only.
- **H2 walls.** Near: the closer of the 0DTE call wall and put wall is within 0.15% of spot (`min(|spot-call|, |spot-put|) / spot <= 0.0015`). Far: that distance is at least 0.50% (`>= 0.0050`). Favored side is **far**. Signals between 0.15% and 0.50% are excluded from H2 only. The thresholds are frozen.
- **H3 net GEX sign.** Favored: `net_gex_0dte` < 0. Unfavored: `net_gex_0dte` > 0. Exact zeros are excluded from H3 only.

Rationale, recorded in advance and not required to be true: under this sign convention, negative gamma means dealer hedging amplifies the move the diamond already picked, and a nearby wall means pin risk and less follow-through. The test is allowed to reject that.

### What gets reported, and what counts as confirmed

Report every one of the 6 ticker × hypothesis pairs (SPY, QQQ) × (H1, H2, H3), analysis window and holdout, whether or not it "works":

- n signals favored, n unfavored, n excluded by the join, n excluded by the bucket rule
- mean 60-minute trade-aligned return (percent) for favored, unfavored, and the difference
- the same-clock random baseline mean
- the to-close return difference (secondary, see below)

A pair is **confirmed** only when all of the following are true:

1. Analysis-window favored mean exceeds the unfavored mean by at least 0.02 percentage points of the underlying.
2. Analysis-window favored mean exceeds the same-clock random baseline.
3. The holdout difference (favored minus unfavored) has the same sign as the analysis difference.
4. Both sides have at least 8 signals in the analysis window and at least 8 in the holdout. Otherwise the pair is **inconclusive**, not confirmed and not a rejection.

To the close (last GEX spot of that ticker that day at or before 16:00 ET) is reported next to the 60-minute numbers. It can be called supportive only when its holdout sign matches the 60-minute analysis sign. It cannot confirm a hypothesis by itself.

No p-value is a pass/fail gate. With a few dozen diamonds the test is under-powered. A null result means "not confirmed on this sample", not "walls do not exist".

### What is not confirmatory

These may be tabulated later if labeled exploratory, and they cannot be promoted after seeing the sign:

- `TUNED` book, or any split on the `first` column (including rows whose `first` contains `VIX FIX`)
- all-expiry flip, shifted flip, volume-adjusted GEX, top-3 proximity
- any threshold other than 0.15% and 0.50%, any horizon other than 60 minutes as the primary
- morning versus afternoon, Monday versus other days, or dropping a day because the return looked odd
- option P&L, win rate, or a sign flip of GEX

The Vix Fix is already inside the YOURS diamond (AGREE DOTS). A bare Vix Fix fire is not a separate confirmatory signal. The `first` column is the place to see whether the diamond was a Vix Fix lead, and that split stays exploratory.
