// Replays saved days (results/bars_<day>.json) through the vfrev engine (Public Vix Fix reversal) in DRY RUN,
// minute by minute, with the bot's real rules (whole contracts, shutoffs, $0.80 floor) from a $1,000 start.
//   node spy0dte/replay_vfrev.js            -> trades + ending balance
//   node spy0dte/replay_vfrev.js why        -> also every pane arrow and why it was taken or skipped
//   node spy0dte/replay_vfrev.js 2026-10    -> a month from the history files instead (results/spy_1m.csv.gz + results/opt_1m/<day>.json.gz)
//   (VF_CFG='{"cutMin":0}' etc. overrides engine settings for a what-if)
const fs = require("fs");
const path = require("path");
const { computeMarks, paneStrikes, osi, coreT } = require("./marks");
const { VfEngine } = require("./vfrev");
const { newDay } = require("./ledger");

const ROOT = path.join(__dirname, "..");
const SHOW_WHY = process.argv.includes("why");
const MONTH = process.argv.slice(2).find((a) => /^\d{4}-\d\d$/.test(a));
const zlib = require("zlib");
const days = MONTH
  ? fs.readdirSync(path.join(ROOT, "results", "opt_1m")).filter((f) => f.startsWith(MONTH)).sort().map((f) => f.slice(0, 10))
  : fs.readdirSync(path.join(ROOT, "results")).filter((f) => /^bars_\d{4}-\d\d-\d\d\.json$/.test(f)).sort();

// a history day in the same shape as results/bars_<day>.json (SPY regular hours + that day's 0DTE contracts)
let SPY_HIST = null;
function fromHistory(day) {
  if (!SPY_HIST) {
    SPY_HIST = {};
    for (const line of zlib.gunzipSync(fs.readFileSync(path.join(ROOT, "results", "spy_1m.csv.gz"))).toString().split("\n").slice(1)) {
      if (!line) continue;
      const [t, o, h, l, c, v] = line.split(",");
      const hm = t.slice(11, 16);
      if (hm < "09:30" || hm > "15:59") continue;
      (SPY_HIST[t.slice(0, 10)] = SPY_HIST[t.slice(0, 10)] || []).push([t.slice(0, 10) + "T" + t.slice(11, 19) + t.slice(-6), +o, +h, +l, +c, +v]);
    }
  }
  const O = JSON.parse(zlib.gunzipSync(fs.readFileSync(path.join(ROOT, "results", "opt_1m", day + ".json.gz"))).toString());
  const yy = day.slice(2, 4) + day.slice(5, 7) + day.slice(8, 10), opt = {};
  for (const [k, rows] of Object.entries(O.opt)) if (k.slice(3, 9) === yy) opt[k] = rows.map((r) => r.slice(0, 5));
  if (!SPY_HIST[day]) throw new Error("no SPY bars in spy_1m.csv.gz for " + day);
  return { day, spy: SPY_HIST[day], opt };
}

function load(f) {
  const B = MONTH ? fromHistory(f) : JSON.parse(fs.readFileSync(path.join(ROOT, "results", f), "utf8"));
  const off = B.spy[0][0].slice(-6);
  const base = new Date(B.day + "T09:30:00" + off).getTime();
  const iso = (ms) => new Date(ms + Number(off.slice(0, 3)) * 3600000).toISOString().slice(0, 19) + off;
  const spy = B.spy.map(([t, o, h, l, c, v]) => ({ timestamp: t.slice(0, 19) + t.slice(-6), open: o, high: h, low: l, close: c, volume: v }));
  const opt = {};
  for (const [sym, rows] of Object.entries(B.opt)) opt[sym] = rows.map(([i, o, h, l, c]) => ({ timestamp: iso(base + i * 60000), open: o, high: h, low: l, close: c, volume: 1 }));
  return { day: B.day, spy, opt };
}

const state = { balance: 1000, trades: [], last10: [], day: null };
const lines = [];
(async () => {
  for (const f of days) {
    const D = load(f);
    newDay(state, D.day);
    let nowC = 0;
    const oc = {};
    for (const [sym, bars] of Object.entries(D.opt)) oc[sym] = bars.map((b) => ({ t: coreT(b), o: +b.open, h: +b.high, l: +b.low, c: +b.close }));
    const market = {
      nowC: () => nowC,
      optBars: (sym) => (oc[sym] || []).filter((b) => b.t + 60 <= nowC),
      // the backtest's "price at the mark" = the option's open on the next minute
      quote: async (sym, m) => {
        const bars = oc[sym] || [];
        const b = m ? bars.find((x) => x.t > m.ts) : [...bars].reverse().find((x) => x.t + 60 <= nowC);
        if (!b) return null;
        const ref = m ? b.o : b.c;
        return { bid: ref, ask: ref, ref, spreadPct: 0, stale: false };
      },
    };
    const log = (e, d) => {
      if (["trade", "shutoff"].includes(e)) lines.push(`${D.day} ${e} ${JSON.stringify(d)}`);
      if (e === "shadow_late") lines.push(`${D.day} ${d.mark.t} P:${d.mark.src} ${d.mark.s} shadow (1:00-1:45, logged only)`);
      if (SHOW_WHY && (e === "mark_skip" || e === "order_buy_DRY") && d.mark && d.mark.k === "P" && d.mark.tod >= 31 && d.mark.tod < 210)
        lines.push(`${D.day} ${d.mark.t} P:${d.mark.src} ${d.mark.s} ${e === "order_buy_DRY" ? "TAKEN " + d.sym + " @" + d.limit : "skip: " + d.why}`);
    };
    const eng = new VfEngine({ state, market, log, cfg: process.env.VF_CFG ? JSON.parse(process.env.VF_CFG) : {} });
    for (let i = 10; i < D.spy.length; i++) {
      nowC = coreT(D.spy[i]) + 60;
      await eng.tick();
      const spy = D.spy.slice(0, i + 1);
      const last = spy[spy.length - 1];
      const ks = paneStrikes(+last.close);
      const opt = {};
      for (const [cp, K] of [["C", ks.call], ["P", ks.put]]) { const s = osi(D.day, cp, K); if (D.opt[s]) opt[s] = D.opt[s].filter((b) => coreT(b) <= coreT(last)); }
      const { marks, kills } = computeMarks(D.day, spy, opt);
      eng.setSpy(spy);
      await eng.onMarks(marks.filter((m) => m.ts === coreT(last)), kills);
    }
    await eng.flatten("end of day");
  }
  console.log(lines.map((l) => {
    const m = l.match(/^(\S+) trade (.*)$/);
    if (!m) return l;
    const t = JSON.parse(m[2]);
    return `${t.day} ${t.mark.t} P:${t.mark.src} ${t.mark.s} ${t.sym.slice(9)} x${t.qty} entry ${t.entry} ret ${t.ret}% pnl ${t.pnl} bal ${t.balance} | ${t.exits}`;
  }).join("\n"));
  const w = state.trades.filter((t) => t.pnl > 0).length;
  console.log(`END ${MONTH || "results/bars_*"} balance $${state.balance.toFixed(0)} from $1,000 · trades ${state.trades.length} · winners ${w} · losers ${state.trades.length - w}`);
})().catch((e) => { console.error(e); process.exit(1); });
