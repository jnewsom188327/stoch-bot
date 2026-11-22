// QQQ 0DTE PUBLIC reversal bot ("qrev"): the Public account's strategy from Nov 23, 2026, separate from the Robinhood SPY dot bot.
// Same minute loop as bot.js / vfbot.js, on QQQ: pane arrows only, the QQQ reversal filter (qrev.js), first-out strike,
// all out at +50%, orders ONLY to Public, and its own files in spy0dte/qrev/ (state.json, logs/, summaries/, trades.csv).
// A SHADOW copy (1 strike in the money, a third at +30%, rest at minute 15) runs beside it on paper only, in spy0dte/qrev/shadow/,
// so the two versions can be compared day by day. It never sends an order.
// DRY RUN unless the repo variable QQQ0DTE_PUBLIC_LIVE is exactly "yes".
const fs = require("fs");
const path = require("path");
const { PublicAPI, sleep } = require("./public");
const { computeMarks, closedOnly, paneStrikes, osi, coreT } = require("./marks");
const { QEngine, QR_SHADOW } = require("./qrev");
const { freshState, newDay } = require("./ledger");

const DIR = path.join(__dirname, "qrev");
const SDIR = path.join(DIR, "shadow");
fs.mkdirSync(SDIR, { recursive: true });
fs.mkdirSync(DIR, { recursive: true });
const STATE = path.join(DIR, "state.json");
const LIVE = process.env.QQQ0DTE_PUBLIC_LIVE === "yes";
const ROOT_SYM = "QQQ";
const MODE = process.env.MODE || "run"; // run | check
const HALF_DAYS = { "2026-11-27": true, "2026-12-24": true, "2027-11-26": true, "2027-12-24": true };

function et(d = new Date()) {
  const p = Object.fromEntries(new Intl.DateTimeFormat("en-US", { timeZone: "America/New_York", year: "numeric", month: "2-digit", day: "2-digit", hour: "2-digit", minute: "2-digit", second: "2-digit", hourCycle: "h23" }).formatToParts(d).map((x) => [x.type, x.value]));
  const day = `${p.year}-${p.month}-${p.day}`;
  const asUTC = Date.UTC(+p.year, +p.month - 1, +p.day, +p.hour, +p.minute, +p.second);
  return { day, min: +p.hour * 60 + +p.minute, sec: +p.second, hms: `${p.hour}:${p.minute}:${p.second}`, offSec: Math.round((asUTC - d.getTime()) / 1000) };
}
const SSTATE = path.join(SDIR, "state.json");
function loadState(f = STATE) { try { return JSON.parse(fs.readFileSync(f, "utf8")); } catch { return freshState(); } }
function saveState(st, f = STATE) { fs.writeFileSync(f, JSON.stringify(st, null, 1)); }
const usd = (x) => (x < 0 ? "-$" : "$") + Math.abs(Math.round(x)).toLocaleString("en-US");

async function main() {
  const T0 = et();
  const day = T0.day;
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
  if (process.env.CLEAR_REVIEW === "yes" && st.reviewHold) { log("review_cleared", { was: st.reviewHold }); st.reviewHold = null; st.last10 = []; }
  if (process.env.CLEAR_REVIEW === "yes" && st.brake && (st.brake.need || st.brake.half)) { log("brake_cleared", { was: st.brake }); st.brake = { need: 0, half: false, target: null }; }
  if (process.env.RESET === "yes") { log("reset_by_you", { from: st.balance }); Object.assign(st, freshState(), { trades: st.trades }); }
  if (process.env.RESET === "yes") { const s0 = loadState(SSTATE); Object.assign(s0, freshState(), { trades: s0.trades }); saveState(s0, SSTATE); }
  if (process.env.RESET === "yes" || process.env.CLEAR_REVIEW === "yes") saveState(st);
  const RESTART = MODE === "run" && process.env.RESTART === "yes";
  if (MODE === "run" && st.lastRunDay === day && !RESTART) { console.log(`Already ran today (${day}); exiting.`); return; }
  if (MODE === "run" && !process.env.FORCE && !RESTART && (T0.min < 9 * 60 || T0.min > 11 * 60)) { console.log(`Not the 9:20 ET start (it is ${T0.hms} ET); exiting.`); return; }

  const api = new PublicAPI(process.env.PUBLIC_API_SECRET, { accountId: process.env.PUBLIC_ACCOUNT_ID || "" });
  await api.auth();
  log("start", { strategy: "qrev (QQQ reversal)", mode: LIVE ? "LIVE" : "DRY RUN", orders: "public", account: "…" + String(api.accountId).slice(-4), balance: st.balance });

  if (MODE === "check") {
    log("check_buying_power", { optionsBuyingPower: await api.optionsBuyingPower() });
    const qqq = await api.bars(ROOT_SYM, "EQUITY");
    log("check_qqq_bars", { count: qqq.length, last: qqq.length ? qqq[qqq.length - 1] : null });
    return;
  }

  if (RESTART) {
    if (LIVE) {
      const p = await api.portfolio();
      const open = ((p && p.positions) || []).filter((x) => x.instrument && x.instrument.type === "OPTION" && +x.quantity);
      if (open.length) { log("restart_refused", { openPositions: open.length, note: "close these first" }); saveState(st); return; }
    }
    log("restart_by_you", { clearedStop: st.halt || null, balance: st.balance });
    st.halt = null;
    st.day = null;
  }
  newDay(st, day);
  if (LIVE) {
    st.balance = Math.round((await api.optionsBuyingPower()) * 100) / 100;
    st.dayStart = st.balance;
    log("buying_power", { optionsBuyingPower: st.balance });
  }
  st.lastRunDay = day;
  saveState(st);
  const half = !!HALF_DAYS[day];

  const optCache = {};
  const market = {
    nowC: () => { const t = et(); return Math.floor(Date.now() / 1000) + t.offSec; },
    async quote(sym) {
      const q = (await api.quotes([sym], "OPTION"))[sym];
      if (!q || q.outcome !== "SUCCESS") return null;
      const bid = +q.bid || 0, ask = +q.ask || 0, mid = bid > 0 && ask > 0 ? (bid + ask) / 2 : +q.last || 0;
      const ts = [q.bidTimestamp, q.askTimestamp].filter(Boolean).map(Date.parse);
      const ageSec = ts.length ? Math.round((Date.now() - Math.max(...ts)) / 1000) : null;
      return { bid, ask, ref: mid, last: +q.last || 0, spreadPct: mid > 0 ? (ask - bid) / mid : 9, ageSec, stale: ageSec == null || ageSec > 30 };
    },
    optBars: (sym) => optCache[sym] || [],
    async preflight(order) {
      try { const r = await api.preflight(order); log("preflight_ok", { sym: order.symbol, est: r && (r.estimatedCost || r.orderValue || r.estimatedProceeds) }); }
      catch (e) { log("preflight_warn", { sym: order.symbol, err: String(e.message).slice(0, 200) }); }
    },
  };
  const refreshOpt = async (sym) => {
    const nowReal = Math.floor(Date.now() / 1000);
    optCache[sym] = closedOnly(await api.bars(sym, "OPTION"), nowReal).map((b) => ({ t: coreT(b), o: +b.open, h: +b.high, l: +b.low, c: +b.close }));
  };

  const cfg = half ? { lastEntryTod: 90, flattenAtTod: 200 } : {};
  const eng = new QEngine({ state: st, market, broker: LIVE ? api : null, log, cfg });
  // the shadow version: paper only (broker null), its own ledger, logged with a "shadow_" prefix
  const sst = loadState(SSTATE);
  newDay(sst, day);
  const slog = (event, data = {}) => log("shadow_" + event, data);
  const shadow = new QEngine({ state: sst, market, broker: null, log: slog, cfg: { ...cfg, ...QR_SHADOW } });
  const endMin = half ? 13 * 60 : 15 * 60 + 10;
  const stats = { marks: 0, skipped: {} };
  let lastBarT = 0, sawToday = false, error = null;

  while (et().min < 9 * 60 + 25) await sleep(5000);
  log("watching", { until: half ? "1:00 PM (half day)" : "3:10 PM" });

  while (et().min < endMin) {
    try {
      const nowReal = Math.floor(Date.now() / 1000);
      const t = et();
      if (t.min >= 9 * 60 + 31 && t.sec >= 3 && Math.floor(nowReal / 60) * 60 - 60 > lastBarT - 0) {
        const spy = closedOnly(await api.bars(ROOT_SYM, "EQUITY"), nowReal).filter((b) => b.timestamp.slice(0, 10) === day);
        if (!spy.length && t.min >= 9 * 60 + 45) { log("market_closed", { note: "no QQQ bars for today" }); break; }
        const last = spy[spy.length - 1];
        if (last && Math.floor(Date.parse(last.timestamp) / 1000) > lastBarT) {
          sawToday = true;
          lastBarT = Math.floor(Date.parse(last.timestamp) / 1000);
          const need = new Set();
          if (eng.pending) need.add(eng.pending.sym);
          if (eng.pos) need.add(eng.pos.sym);
          if (shadow.pending) need.add(shadow.pending.sym);
          if (shadow.pos) need.add(shadow.pos.sym);
          for (const s of need) await refreshOpt(s);
          await eng.tick();
          await shadow.tick().catch((e) => slog("ERROR", { err: String(e.message || e).slice(0, 300) }));
          const ks = paneStrikes(+last.close);
          const opt = {};
          for (const [cp, K] of [["C", ks.call], ["P", ks.put]]) {
            const s = osi(day, cp, K, undefined, ROOT_SYM);
            opt[s] = closedOnly(await api.bars(s, "OPTION"), nowReal);
          }
          const { marks, kills } = computeMarks(day, spy, opt, ROOT_SYM);
          const fresh = marks.filter((m) => m.ts === coreT(last) && m.k === "P");
          stats.marks += fresh.length;
          if (fresh.length) log("marks", { bar: last.timestamp.slice(11, 16), marks: fresh.map((m) => `${m.k}:${m.src} ${m.s} tw${m.tw}`) });
          eng.setSpy(spy);
          await eng.onMarks(fresh, kills);
          shadow.setSpy(spy);
          await shadow.onMarks(fresh, kills).catch((e) => slog("ERROR", { err: String(e.message || e).slice(0, 300) }));
          saveState(st);
          saveState(sst, SSTATE);
        }
      } else if (LIVE && (eng.pos || eng.pending)) {
        await eng.tick();
      }
    } catch (e) {
      error = String((e && e.stack) || e);
      log("ERROR", { err: error.slice(0, 600) });
      try { await eng.flatten("error: closing everything and stopping for the day", true); }
      catch (e2) { log("FLATTEN_FAILED", { err: String(e2.message || e2).slice(0, 400), note: "CHECK YOUR PUBLIC ACCOUNT" }); }
      st.halt = st.halt || "error";
      break;
    }
    if (st.halt || st.reviewHold) {
      if (!eng.pos && !eng.pending) { log("done_for_day", { why: st.halt || st.reviewHold }); break; }
    }
    await sleep(LIVE && eng.pos ? 1500 : LIVE && eng.pending ? 3000 : 5000);
  }
  if (shadow.pos || shadow.pending) await shadow.flatten("end of the run").catch(() => {});
  saveState(sst, SSTATE);
  if (eng.pos || eng.pending) {
    try { await eng.flatten("end of the run"); } catch (e) { log("FLATTEN_FAILED", { err: String(e.message || e), note: "CHECK YOUR PUBLIC ACCOUNT" }); }
  }
  for (const e of events) {
    if (e.event !== "mark_skip") continue;
    const k = String(e.why).split(" (")[0].replace(/\$[\d.]+/g, "$").replace(/[\d.]+%/g, "N%").replace(/stretch [\d.]+/, "stretch").trim();
    stats.skipped[k] = (stats.skipped[k] || 0) + 1;
  }
  saveState(st);
  summary({ day, st, sst, events, stats, error, sawToday });
}

function summary({ day, st, sst, events, stats, error, sawToday }) {
  const dir = path.join(DIR, "summaries");
  fs.mkdirSync(dir, { recursive: true });
  const trades = st.trades.filter((t) => t.day === day);
  const pnl = trades.reduce((a, t) => a + t.pnl, 0);
  const L = [`## QQQ 0DTE Public reversal (qrev) · ${day} · ${LIVE ? "LIVE" : "DRY RUN (no orders sent)"}`, ""];
  if (!sawToday) L.push("No QQQ bars today (market closed?). Nothing traded.");
  L.push(`**Day:** ${usd(st.dayStart)} → ${usd(st.balance)} (${pnl >= 0 ? "+" : ""}${usd(pnl)}) · ${trades.length} trade${trades.length === 1 ? "" : "s"}`);
  if (st.halt) L.push(`**Stopped today:** ${st.halt}`);
  if (st.reviewHold) L.push(`**⚠ On hold until you review:** ${st.reviewHold}. Run the workflow with clear_review = yes to restart.`);
  if (error) L.push(`**⚠ Error:** \`${error.split("\n")[0].slice(0, 300)}\``);
  L.push("");
  if (trades.length) {
    L.push("| Mark | Contract | Qty | Entry | Exits | Return | P&L |", "|---|---|---|---|---|---|---|");
    for (const t of trades) L.push(`| ${t.mark.t} P:${t.mark.src} ${t.mark.s} | ${t.sym} | ${t.qty} | ${t.entry.toFixed(2)} | ${t.exits} | ${t.ret}% | ${usd(t.pnl)} |`);
    L.push("");
  }
  L.push(`Pane arrows: ${stats.marks} · entries placed: ${events.filter((e) => /^order_buy/.test(e.event)).length} · unfilled: ${events.filter((e) => e.event === "entry_cancel").length}`);
  const strades = (sst.trades || []).filter((t) => t.day === day);
  L.push(`**Shadow (paper: 1 ITM, a third at +30%):** ${strades.length ? strades.map((t) => `${t.mark.t} ${t.mark.s} ${t.ret}%`).join(", ") : "no trade"} · its paper $1,000 is now ${usd(sst.balance)}`);
  const b = st.brake || {};
  const pt = events.filter((e) => e.event === "paper_trade");
  if (b.need > 0 || pt.length) L.push(`**Safety brake:** ${b.need > 0 ? `PAPER ONLY until ${b.need} more paper win${b.need === 1 ? "" : "s"} in a row` : "off (real trades)"}${pt.length ? " · paper trades today: " + pt.map((e) => `${e.mark.t} ${e.mark.s} ${e.ret}%`).join(", ") : ""}`);
  if (b.half) L.push(`**Safety brake:** half port until the bot's money is back to ${usd(b.target || 0)}`);
  const sk = Object.entries(stats.skipped).sort((a, b) => b[1] - a[1]);
  if (sk.length) L.push("Skipped: " + sk.map(([k, n]) => `${k} ×${n}`).join(" · "));
  L.push("", `Full log: spy0dte/qrev/logs/${day}.jsonl`);
  const md = L.join("\n");
  const title = `${LIVE ? "LIVE" : "DRY RUN"} · ${pnl >= 0 ? "+" : ""}${usd(pnl)} · ${trades.length} trade${trades.length === 1 ? "" : "s"} · balance ${usd(st.balance)}${st.halt ? " · stopped" : ""}${st.reviewHold ? " · REVIEW NEEDED" : ""}${st.brake && st.brake.need > 0 ? " · BRAKE: paper only" : ""}${error ? " · ERROR" : ""}`;
  fs.writeFileSync(path.join(dir, `${day}.title`), title + "\n");
  fs.writeFileSync(path.join(dir, `${day}.md`), md + "\n");
  if (process.env.GITHUB_STEP_SUMMARY) fs.appendFileSync(process.env.GITHUB_STEP_SUMMARY, md + "\n");
  const csv = path.join(DIR, "trades.csv");
  if (!fs.existsSync(csv)) fs.writeFileSync(csv, "day,mark_time,mark,side,contract,qty,entry,return_pct,pnl,balance,exits,dry_run\n");
  for (const t of trades) fs.appendFileSync(csv, [t.day, t.mark.t, "P:" + t.mark.src, t.mark.s, t.sym, t.qty, t.entry, t.ret, t.pnl, t.balance, `"${t.exits}"`, t.dry ? "yes" : "no"].join(",") + "\n");
  const scsv = path.join(SDIR, "trades.csv");
  if (!fs.existsSync(scsv)) fs.writeFileSync(scsv, "day,mark_time,mark,side,contract,qty,entry,return_pct,pnl,balance,exits\n");
  for (const t of strades) fs.appendFileSync(scsv, [t.day, t.mark.t, "P:" + t.mark.src, t.mark.s, t.sym, t.qty, t.entry, t.ret, t.pnl, t.balance, `"${t.exits}"`].join(",") + "\n");
  console.log("\n" + md);
}

main().catch((e) => { console.error(e); process.exit(1); });
