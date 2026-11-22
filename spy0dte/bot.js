// SPY 0DTE bot: runs one market day (9:25 - 3:10 ET), checks for marks every minute, trades them by the rules in engine.js.
// DRY RUN by default: real Public prices, every decision made and logged, no orders sent.
// LIVE only when the repo variable SPY0DTE_LIVE is exactly "yes".
const fs = require("fs");
const path = require("path");
const { PublicAPI, sleep } = require("./public");
const { computeMarks, closedOnly, paneStrikes, osi, coreT } = require("./marks");
const { Engine } = require("./engine");
const { withBrake } = require("./brake");
const BrakeEngine = withBrake(Engine);
const { freshState, newDay } = require("./ledger");
const { writeSummary } = require("./summary");

// SPY0DTE_TAG = a second copy of the bot (the "twin") with its own state, logs and summaries in spy0dte/twin_<tag>/.
// A twin is ALWAYS a dry run: it never sends an order, whatever the live setting says.
const TAG = (process.env.SPY0DTE_TAG || "").replace(/[^a-z0-9_-]/gi, "");
const DIR = TAG ? path.join(__dirname, "twin_" + TAG) : __dirname;
fs.mkdirSync(DIR, { recursive: true });
const STATE = path.join(DIR, "state.json");
const LIVE = !TAG && process.env.SPY0DTE_LIVE === "yes";
const BROKER = (process.env.SPY0DTE_BROKER || "public").toLowerCase(); // where orders go: public | robinhood (prices always from Public)
const MODE = process.env.MODE || "run"; // run | check
const HALF_DAYS = { "2026-11-27": true, "2026-12-24": true, "2027-11-26": true, "2027-12-24": true }; // 1:00 PM closes

// ---------- ET clock ----------
function et(d = new Date()) {
  const p = Object.fromEntries(new Intl.DateTimeFormat("en-US", { timeZone: "America/New_York", year: "numeric", month: "2-digit", day: "2-digit", hour: "2-digit", minute: "2-digit", second: "2-digit", hourCycle: "h23" }).formatToParts(d).map((x) => [x.type, x.value]));
  const day = `${p.year}-${p.month}-${p.day}`;
  const asUTC = Date.UTC(+p.year, +p.month - 1, +p.day, +p.hour, +p.minute, +p.second);
  return { day, min: +p.hour * 60 + +p.minute, sec: +p.second, hms: `${p.hour}:${p.minute}:${p.second}`, offSec: Math.round((asUTC - d.getTime()) / 1000) };
}

function loadState() {
  try { return JSON.parse(fs.readFileSync(STATE, "utf8")); } catch { return freshState(); }
}
function saveState(st) { fs.writeFileSync(STATE, JSON.stringify(st, null, 1)); }

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
  if (process.env.RESET === "yes" || process.env.CLEAR_REVIEW === "yes") saveState(st);
  const RESTART = MODE === "run" && process.env.RESTART === "yes"; // you started it again by hand after a stop
  if (MODE === "run" && st.lastRunDay === day && !RESTART) { console.log(`Already ran today (${day}); exiting.`); return; }
  // two cron times cover summer/winter clocks; only the one that lands near 9:20 ET runs (late GitHub starts allowed until 11:00)
  if (MODE === "run" && !process.env.FORCE && !RESTART && (T0.min < 9 * 60 || T0.min > 11 * 60)) { console.log(`Not the 9:20 ET start (it is ${T0.hms} ET); exiting.`); return; }

  const api = new PublicAPI(process.env.PUBLIC_API_SECRET, { accountId: process.env.PUBLIC_ACCOUNT_ID || "" });
  await api.auth();
  let broker = api;
  if (BROKER === "robinhood") {
    const { RobinhoodBroker } = require("./rh");
    broker = new RobinhoodBroker({ accountNumber: process.env.RH_ACCOUNT || "", log });
    const info = await broker.setup();
    log("robinhood", { account: "…" + info.account.slice(-4), type: info.type, optionLevel: info.optionLevel });
  }
  log("start", { mode: LIVE ? "LIVE" : "DRY RUN", orders: BROKER, prices: "Public …" + String(api.accountId).slice(-4), balance: st.balance });

  if (MODE === "check") return check(api, day, log, broker);

  if (RESTART) {
    // never start blind: refuse if the broker shows any open option position or order
    if (LIVE && broker.openOptionPositions) {
      const pos = await broker.openOptionPositions(), ord = await broker.openOptionOrders();
      if (pos.length || ord.length) { log("restart_refused", { openPositions: pos.length, openOrders: ord.length, note: "close these first" }); saveState(st); return; }
    }
    log("restart_by_you", { clearedStop: st.halt || null, balance: st.balance });
    st.halt = null;
    st.day = null; // the day shutoffs start fresh from the buying power right now
  }
  newDay(st, day);
  if (LIVE) { // live: the day starts from what's really in the account
    st.balance = Math.round((await broker.optionsBuyingPower()) * 100) / 100;
    st.dayStart = st.balance;
    log("buying_power", { optionsBuyingPower: st.balance });
  }
  st.lastRunDay = day;
  saveState(st);
  const half = !!HALF_DAYS[day];

  // ---------- market adapter ----------
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
  if (process.env.SPY0DTE_TRENDSIZING === "off") cfg.trendSizing = false; // original rules: first-out strike, full port
  if (TAG) cfg.firstEntryTod = 15; // the twin starts at 9:45 like the Robinhood bot, so the two see the same marks
  if (BROKER === "robinhood") cfg.firstEntryTod = 15; // Robinhood refuses option stop orders before 9:45
  if (TAG) { cfg.tpPut = null; cfg.brake = false; } // the twin keeps the original rules: +10% on both sides, no brake
  const eng = new BrakeEngine({ state: st, market, broker: LIVE ? broker : null, log, cfg });
  const endMin = half ? 13 * 60 : 15 * 60 + 10;
  const stats = { marks: 0, taken: 0, skipped: {} };
  let lastBarT = 0, sawToday = false, error = null;

  // wait for 9:25
  while (et().min < 9 * 60 + 25) await sleep(5000);
  log("watching", { until: half ? "1:00 PM (half day)" : "3:10 PM" });

  while (et().min < endMin) {
    try {
      const nowReal = Math.floor(Date.now() / 1000);
      const t = et();
      // new closed minute? (bars land a few seconds after the minute)
      if (t.min >= 9 * 60 + 31 && t.sec >= 3 && Math.floor(nowReal / 60) * 60 - 60 > lastBarT - 0) {
        const spy = closedOnly(await api.bars("SPY", "EQUITY"), nowReal).filter((b) => b.timestamp.slice(0, 10) === day);
        if (!spy.length && t.min >= 9 * 60 + 45) { log("market_closed", { note: "no SPY bars for today" }); break; }
        const last = spy[spy.length - 1];
        if (last && Math.floor(Date.parse(last.timestamp) / 1000) > lastBarT) {
          sawToday = true;
          lastBarT = Math.floor(Date.parse(last.timestamp) / 1000);
          // option bars the engine needs (dry-run fills and exits are judged on them)
          const need = new Set();
          if (eng.pending) need.add(eng.pending.sym);
          if (eng.pos) need.add(eng.pos.sym);
          for (const s of need) await refreshOpt(s);
          await eng.tick();
          // marks on the bar that just closed
          const ks = paneStrikes(+last.close);
          const opt = {};
          for (const [cp, K] of [["C", ks.call], ["P", ks.put]]) {
            const s = osi(day, cp, K);
            opt[s] = closedOnly(await api.bars(s, "OPTION"), nowReal);
          }
          const { marks, kills } = computeMarks(day, spy, opt);
          const fresh = marks.filter((m) => m.ts === coreT(last));
          stats.marks += fresh.length;
          if (fresh.length) log("marks", { bar: last.timestamp.slice(11, 16), marks: fresh.map((m) => `${m.k}${m.src ? ":" + m.src : ""} ${m.s} tw${m.tw} ag${m.ag}`) });
          await eng.onMarks(fresh, kills);
          if (eng.pending && eng.pending.markT === coreT(last)) stats.taken++;
          saveState(st);
        }
      } else if (LIVE && (eng.pos || eng.pending)) {
        await eng.tick(); // live: watch the position between minutes
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
    await sleep(LIVE && eng.pos ? 1500 : LIVE && eng.pending ? 3000 : 5000); // in a trade: watch the quote every 1.5 s
  }
  if (eng.pos || eng.pending) {
    try { await eng.flatten("end of the run"); } catch (e) { log("FLATTEN_FAILED", { err: String(e.message || e), note: "CHECK YOUR PUBLIC ACCOUNT" }); }
  }
  for (const e of events) {
    if (e.event !== "mark_skip") continue;
    const k = String(e.why).split(" (")[0].replace(/\$[\d.]+/g, "$").replace(/[\d.]+%/g, "N%").trim();
    stats.skipped[k] = (stats.skipped[k] || 0) + 1;
  }
  saveState(st);
  writeSummary({ day, live: LIVE, st, events, stats, error, sawToday });
}

// MODE=check: proves the key works and shows what the bot sees, sends nothing
async function check(api, day, log, broker) {
  if (broker && broker !== api) {
    log("check_robinhood_buying_power", { buyingPower: await broker.optionsBuyingPower() });
    const spy0 = await api.bars("SPY", "EQUITY");
    const lastC = spy0.length ? +spy0[spy0.length - 1].close : 0;
    if (lastC) {
      const ex = (await broker.mcp.call("get_option_chains", { underlying_symbol: "SPY" })).chains.find((c) => c.symbol === "SPY").expiration_dates[0];
      const sym = osi(ex, "C", Math.floor(lastC) + 1);
      log("check_robinhood_contract", { sym, option_id: await broker.optionId(sym), positionQty: await broker.positionQty(sym) });
    }
  }
  const spy = await api.bars("SPY", "EQUITY");
  log("check_spy_bars", { count: spy.length, last: spy.length ? spy[spy.length - 1] : null });
  const last = spy[spy.length - 1];
  if (last) {
    const ks = paneStrikes(+last.close);
    const sym = osi(last.timestamp.slice(0, 10), "C", ks.call);
    const q = (await api.quotes([sym], "OPTION"))[sym];
    log("check_quote", { sym, q });
    const ob = await api.bars(sym, "OPTION");
    log("check_option_bars", { sym, count: ob.length });
    const { marks } = computeMarks(last.timestamp.slice(0, 10), closedOnly(spy, Math.floor(Date.now() / 1000)), {});
    log("check_marks_so_far", { count: marks.length, last: marks.slice(-3).map((m) => `${m.t} ${m.k} ${m.s} tw${m.tw} ag${m.ag}`) });
  }
  log("check_buying_power", { optionsBuyingPower: await api.optionsBuyingPower() });
}

main().catch((e) => { console.error(e); process.exit(1); });
