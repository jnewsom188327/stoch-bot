// SPY 0DTE SMALL-WIN Vix Fix bot ("swrev") — DRY RUN ONLY. It never sends an order: there is no live switch.
// Rules: swrev.js (setup A "maxed" + setup B "swing", boosters, vetoes, +8% / ratchet exits, 2-loss and day-target stops).
// Public is used for prices only (key: GitHub secret PUBLIC_API_SECRET). Fills are judged on Public's real 1-minute
// option bars, the same way as the other dry runs. Its own files in spy0dte/smallwin/ (state.json, logs/, summaries/, trades.csv).
// Separate from the Robinhood dot bot and the Public bots: it reads none of their state and changes none of their files.
const fs = require("fs");
const path = require("path");
const { PublicAPI, sleep } = require("./public");
const { computeMarks, closedOnly, paneStrikes, osi, coreT } = require("./marks");
const { loadCore } = require("./core");
const { SwEngine, swMarks, weakOpen, SW, SW_CFG } = require("./swrev");
const { freshState, newDay } = require("./ledger");

const DIR = path.join(__dirname, "smallwin");
fs.mkdirSync(DIR, { recursive: true });
const STATE = path.join(DIR, "state.json");
const MODE = process.env.MODE || "run"; // run | check
const HALF_DAYS = { "2026-11-27": true, "2026-12-24": true, "2027-11-26": true, "2027-12-24": true };
const L = loadCore();
const toRes = (bars) => JSON.stringify({ regularMarket: { bars } });
const str = (b, vol) => ({ timestamp: b.timestamp, open: String(b.open), high: String(b.high), low: String(b.low), close: String(b.close), volume: vol != null ? vol : String(b.volume) });
const rowsOf = (bars) => { const p = L.parseBars(toRes(bars)); return p ? L.compute(L.cleanPrints(p.filter((x) => !x.live && !x.fill))) : []; };

function et(d = new Date()) {
  const p = Object.fromEntries(new Intl.DateTimeFormat("en-US", { timeZone: "America/New_York", year: "numeric", month: "2-digit", day: "2-digit", hour: "2-digit", minute: "2-digit", second: "2-digit", hourCycle: "h23" }).formatToParts(d).map((x) => [x.type, x.value]));
  const day = `${p.year}-${p.month}-${p.day}`;
  const asUTC = Date.UTC(+p.year, +p.month - 1, +p.day, +p.hour, +p.minute, +p.second);
  return { day, min: +p.hour * 60 + +p.minute, sec: +p.second, hms: `${p.hour}:${p.minute}:${p.second}`, offSec: Math.round((asUTC - d.getTime()) / 1000) };
}
function loadState() { try { return JSON.parse(fs.readFileSync(STATE, "utf8")); } catch { return freshState(); } }
function saveState(st) { fs.writeFileSync(STATE, JSON.stringify(st, null, 1)); }
const usd = (x) => (x < 0 ? "-$" : "$") + Math.abs(Math.round(x)).toLocaleString("en-US");

// yesterday's close for the weak-open booster: this bot's own record, else the newest results/bars_<day>.json before today
function prevClose(st, day) {
  if (st.lastClose && st.lastCloseDay && st.lastCloseDay < day) return st.lastClose;
  const res = path.join(__dirname, "..", "results");
  try {
    const f = fs.readdirSync(res).filter((x) => /^bars_\d{4}-\d\d-\d\d\.json$/.test(x) && x.slice(5, 15) < day).sort().pop();
    if (f) { const B = JSON.parse(fs.readFileSync(path.join(res, f), "utf8")); return B.spy[B.spy.length - 1][4]; }
  } catch {}
  return null;
}

async function main() {
  const T0 = et(), day = T0.day;
  const logDir = path.join(DIR, "logs");
  fs.mkdirSync(logDir, { recursive: true });
  const logFile = path.join(logDir, `${day}.jsonl`);
  const events = [];
  const log = (event, data = {}) => {
    const row = { at: et().hms, event, ...data };
    events.push(row);
    fs.appendFileSync(logFile, JSON.stringify(row) + "\n");
    console.log(`${row.at} ${event} ${JSON.stringify(data)}`);
  };

  const st = loadState();
  if (process.env.RESET === "yes") { log("reset_by_you", { from: st.balance }); Object.assign(st, freshState(), { trades: st.trades }); saveState(st); }
  if (MODE === "run" && st.lastRunDay === day && process.env.RESTART !== "yes") { console.log(`Already ran today (${day}); exiting.`); return; }
  if (MODE === "run" && !process.env.FORCE && (T0.min < 9 * 60 || T0.min > 11 * 60)) { console.log(`Not the 9:20 ET start (it is ${T0.hms} ET); exiting.`); return; }

  const api = new PublicAPI(process.env.PUBLIC_API_SECRET, { accountId: process.env.PUBLIC_ACCOUNT_ID || "" });
  await api.auth();
  log("start", { strategy: "swrev (small-win Vix Fix)", mode: "DRY RUN (no orders, ever)", prices: "public", balance: st.balance });

  if (MODE === "check") {
    const spy = await api.bars("SPY", "EQUITY");
    log("check_spy_bars", { count: spy.length, last: spy.length ? spy[spy.length - 1] : null });
    const v = await api.bars("VIX1D", "INDEX").catch((e) => ({ err: String(e.message).slice(0, 160) }));
    log("check_vix1d", Array.isArray(v) ? { count: v.length } : v);
    return;
  }

  if (process.env.RESTART === "yes") { st.halt = null; st.day = null; log("restart_by_you", {}); }
  newDay(st, day);
  st.lastRunDay = day;
  saveState(st);
  const half = !!HALF_DAYS[day] || process.env.SW_HALF === "yes"; // SW_HALF: the mock test can rehearse a half day
  const pc = prevClose(st, day);
  log("prev_close", { prevClose: pc });

  const optCache = {};
  const market = {
    nowC: () => Math.floor(Date.now() / 1000) + et().offSec,
    async quote(sym) {
      const q = (await api.quotes([sym], "OPTION"))[sym];
      if (!q || q.outcome !== "SUCCESS") return null;
      const bid = +q.bid || 0, ask = +q.ask || 0, mid = bid > 0 && ask > 0 ? (bid + ask) / 2 : +q.last || 0;
      const ts = [q.bidTimestamp, q.askTimestamp].filter(Boolean).map(Date.parse);
      const ageSec = ts.length ? Math.round((Date.now() - Math.max(...ts)) / 1000) : null;
      return { bid, ask, ref: mid, last: +q.last || 0, spreadPct: mid > 0 ? (ask - bid) / mid : 9, ageSec, stale: ageSec == null || ageSec > 30 };
    },
    optBars: (sym) => optCache[sym] || [],
  };
  const refreshOpt = async (sym) => {
    optCache[sym] = closedOnly(await api.bars(sym, "OPTION"), Math.floor(Date.now() / 1000)).map((b) => ({ t: coreT(b), o: +b.open, h: +b.high, l: +b.low, c: +b.close }));
  };

  // Half day (closes 1:00): entries until 12:30, flat by 12:50 (0DTE expires at 1:00). Normal days (practice): entries until 3:30.
  const cfg = half ? { lastEntryTod: 180, flattenAtTod: 200 } : {};
  const eng = new SwEngine({ state: st, market, broker: null, log, cfg }); // broker null = DRY RUN, always
  const endMin = half ? 12 * 60 + 55 : 15 * 60 + 56;
  const stats = { setups: 0, skipped: {} };
  let lastBarT = 0, sawToday = false, error = null, wo, vixOk = null;
  const optRows = {}, armed = {};

  while (et().min < 9 * 60 + 25) await sleep(5000);
  log("watching", { until: half ? "12:55 PM (half day, entries until 12:30)" : "3:56 PM (practice: entries until 3:30)" });

  while (et().min < endMin) {
    try {
      const nowReal = Math.floor(Date.now() / 1000), t = et();
      if (t.min >= 9 * 60 + 31 && t.sec >= 3) {
        const spy = closedOnly(await api.bars("SPY", "EQUITY"), nowReal).filter((b) => b.timestamp.slice(0, 10) === day);
        if (!spy.length && t.min >= 9 * 60 + 45) { log("market_closed", { note: "no SPY bars for today" }); break; }
        const last = spy[spy.length - 1];
        if (last && Math.floor(Date.parse(last.timestamp) / 1000) > lastBarT) {
          sawToday = true;
          lastBarT = Math.floor(Date.parse(last.timestamp) / 1000);
          const need = new Set();
          if (eng.pending) need.add(eng.pending.sym);
          if (eng.pos) need.add(eng.pos.sym);
          for (const s of need) await refreshOpt(s);
          // the call and put pane charts (first-out strikes), as the pages draw them
          const ks = paneStrikes(+last.close), opt = {};
          for (const [cp, K] of [["C", ks.call], ["P", ks.put]]) {
            const s = osi(day, cp, K);
            opt[s] = closedOnly(await api.bars(s, "OPTION"), nowReal);
            optRows[s] = rowsOf(opt[s].filter((b) => +b.volume > 0).map((b) => str(b, "1")));
          }
          const { marks, kills, rows } = computeMarks(day, spy, opt);
          const pane = marks.filter((m) => m.k === "P").map((m) => ({ ts: m.ts, side: m.side, src: m.src }));
          // VIX1D (booster only; skipped quietly if Public doesn't serve it)
          let vix = null;
          if (vixOk !== false) {
            try {
              const vb = closedOnly(await api.bars("VIX1D", "INDEX"), nowReal);
              vix = new Map(vb.map((b) => [coreT(b), +b.close]));
              if (vixOk == null) log("vix1d", { ok: true, bars: vb.length });
              vixOk = true;
            } catch (e) { if (vixOk == null) log("vix1d", { ok: false, note: "no VIX1D from Public; the vix1d_div booster is off today", err: String(e.message).slice(0, 160) }); vixOk = false; }
          }
          if (wo === undefined && rows.length >= 15) { wo = weakOpen(rows, pc); log("weak_open", { weakOpen: wo, prevClose: pc }); }
          eng.setCtx(rows, pane);
          await eng.tick();
          const ms = swMarks(day, rows, SW, L.hmLabel, { optRows, weakOpen: !!wo, vix, armed });
          stats.setups += ms.length;
          if (ms.length) log("setups", { bar: last.timestamp.slice(11, 16), setups: ms.map((m) => `${m.setup} ${m.s} [${m.boosters.join("+") || "no booster"}]`) });
          await eng.onMarks(ms, kills);
          saveState(st);
        }
      }
    } catch (e) {
      error = String((e && e.stack) || e);
      log("ERROR", { err: error.slice(0, 600) });
      try { await eng.flatten("error: closing the paper position and stopping for the day", true); } catch {}
      st.halt = st.halt || "error";
      break;
    }
    if (st.halt && !eng.pos && !eng.pending) { log("done_for_day", { why: st.halt }); break; }
    await sleep(5000);
  }
  if (eng.pos || eng.pending) await eng.flatten("end of the run").catch(() => {});
  try { const spy = await api.bars("SPY", "EQUITY"); const lb = spy.filter((b) => b.timestamp.slice(0, 10) === day).pop(); if (lb) { st.lastClose = +lb.close; st.lastCloseDay = day; } } catch {}
  for (const e of events) {
    if (e.event !== "mark_skip") continue;
    const k = String(e.why).split(" (")[0].replace(/\$[\d.]+/g, "$").replace(/[\d.]+%/g, "N%").trim();
    stats.skipped[k] = (stats.skipped[k] || 0) + 1;
  }
  saveState(st);
  summary({ day, st, events, stats, error, sawToday, half });
}

const CSV_HEAD = "day,mark_time,setup,side,boosters,port,contract,qty,entry,return_pct,pnl,balance,confirm,exits,peak,opp_at_peak,side_now,opp_now,ran15,swing,stall_bars,trend_line,shading,ttm,ttm_turning,opt_fear,opt_greed,panes\n";
function csvRow(t) {
  const r = t.read || {}, o = t.optRead || {};
  const q = (x) => (x == null ? "" : `"${String(x).replace(/"/g, "'")}"`);
  return [t.day, t.mark.t, t.setup, t.mark.s, t.boosters, t.boosters === "none" ? "half" : "full", t.sym, t.qty, t.entry, t.ret, t.pnl, t.balance, q(t.confirm), q(t.exits),
    r.peak, r.oppAtPeak, r.sideNow, r.oppNow, r.ran15, r.swing, r.stall, r.trendLine, r.shading, r.ttm, r.ttmTurning, o.optFear, o.optGreed, q(r.panes)].join(",") + "\n";
}

function summary({ day, st, events, stats, error, sawToday, half }) {
  const dir = path.join(DIR, "summaries");
  fs.mkdirSync(dir, { recursive: true });
  const trades = st.trades.filter((t) => t.day === day);
  const pnl = trades.reduce((a, t) => a + t.pnl, 0);
  const L2 = [`## SPY 0DTE small-win Vix Fix (swrev) · ${day} · DRY RUN (no orders sent)${half ? " · half day" : ""}`, ""];
  if (!sawToday) L2.push("No SPY bars today (market closed?). Nothing traded.");
  L2.push(`**Day:** ${usd(st.dayStart)} → ${usd(st.balance)} (${pnl >= 0 ? "+" : ""}${usd(pnl)}) · ${trades.length} trade${trades.length === 1 ? "" : "s"}`);
  if (st.halt) L2.push(`**Stopped today:** ${st.halt}`);
  if (error) L2.push(`**⚠ Error:** \`${error.split("\n")[0].slice(0, 300)}\``);
  L2.push("");
  if (trades.length) {
    L2.push("| Time | Setup | Side | Boosters | Port | Contract | Entry | Exits | Return | P&L |", "|---|---|---|---|---|---|---|---|---|---|");
    for (const t of trades) L2.push(`| ${t.mark.t} | ${t.setup} | ${t.mark.s} | ${t.boosters} | ${t.boosters === "none" ? "half" : "full"} | ${t.sym} | ${t.entry.toFixed(2)} | ${t.exits} | ${t.ret}% | ${usd(t.pnl)} |`);
    L2.push("", "Readings at entry (compare with your own picks):");
    for (const t of trades) { const r = t.read || {}, o = t.optRead || {}; L2.push(`- ${t.mark.t} ${t.setup} ${t.mark.s}: peak ${r.peak} (other side ${r.oppAtPeak ?? r.oppNow}), now ${r.sideNow}/${r.oppNow}, ${r.swing != null ? "swing $" + r.swing : "ran $" + r.ran15}, stalled ${r.stall} bars, trend line ${r.trendLine}, shading ${r.shading}, TTM ${r.ttm}${r.ttmTurning ? " turning" : ""}${o.optGreed != null ? `, option fear/greed ${o.optFear}/${o.optGreed}` : ""}${r.panes ? `, panes: ${r.panes}` : ""} · confirm: ${t.confirm}`); }
    L2.push("");
  }
  L2.push(`Setups seen: ${stats.setups} · entries placed: ${events.filter((e) => /^order_buy/.test(e.event)).length} · unfilled: ${events.filter((e) => e.event === "entry_cancel").length}`);
  const sk = Object.entries(stats.skipped).sort((a, b) => b[1] - a[1]);
  if (sk.length) L2.push("Skipped: " + sk.map(([k, n]) => `${k} ×${n}`).join(" · "));
  L2.push("", `Full log: spy0dte/smallwin/logs/${day}.jsonl · all trades: spy0dte/smallwin/trades.csv`);
  const md = L2.join("\n");
  const title = `DRY RUN · ${pnl >= 0 ? "+" : ""}${usd(pnl)} · ${trades.length} trade${trades.length === 1 ? "" : "s"} · balance ${usd(st.balance)}${st.halt ? " · " + st.halt : ""}${error ? " · ERROR" : ""}`;
  fs.writeFileSync(path.join(dir, `${day}.title`), title + "\n");
  fs.writeFileSync(path.join(dir, `${day}.md`), md + "\n");
  if (process.env.GITHUB_STEP_SUMMARY) fs.appendFileSync(process.env.GITHUB_STEP_SUMMARY, md + "\n");
  const csv = path.join(DIR, "trades.csv");
  if (!fs.existsSync(csv)) fs.writeFileSync(csv, CSV_HEAD);
  for (const t of trades) fs.appendFileSync(csv, csvRow(t));
  console.log("\n" + md);
}

module.exports = { csvRow, CSV_HEAD, main };
if (require.main === module) main().catch((e) => { console.error(e); process.exit(1); });
