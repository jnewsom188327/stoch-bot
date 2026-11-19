// Replays saved days (results/bars_<day>.json) through the real bot engine in DRY RUN, minute by minute.
//   node spy0dte/replay.js compare   -> backtest settings only (no shutoffs, fractional, no $0.80/spread filters),
//                                       to line up trade by trade with the Edge Stress Test
//   node spy0dte/replay.js           -> the bot's real rules (whole contracts, shutoffs, $0.80 floor) from a $1,000 start
const fs = require("fs");
const path = require("path");
const { computeMarks, paneStrikes, osi, coreT } = require("./marks");
const { Engine } = require("./engine");
const { newDay } = require("./ledger");

const ROOT = path.join(__dirname, "..");
const mode = process.argv[2] || "full";
const days = fs.readdirSync(path.join(ROOT, "results")).filter((f) => /^bars_\d{4}-\d\d-\d\d\.json$/.test(f)).sort();

function load(f) {
  const B = JSON.parse(fs.readFileSync(path.join(ROOT, "results", f), "utf8"));
  const off = B.spy[0][0].slice(-6);
  const base = new Date(B.day + "T09:30:00" + off).getTime();
  const iso = (ms) => new Date(ms + Number(off.slice(0, 3)) * 3600000).toISOString().slice(0, 19) + off;
  const spy = B.spy.map(([t, o, h, l, c, v]) => ({ timestamp: t.slice(0, 19) + t.slice(-6), open: o, high: h, low: l, close: c, volume: v }));
  const opt = {};
  for (const [sym, rows] of Object.entries(B.opt)) opt[sym] = rows.map(([i, o, h, l, c]) => ({ timestamp: iso(base + i * 60000), open: o, high: h, low: l, close: c, volume: 1 }));
  return { day: B.day, spy, opt };
}

const cfg = mode === "compare"
  ? { fractional: true, simUnroundedFill: true, minPrice: 0, maxSpread: 99, dayMaxLoss: 99, dayLockAt: 99, reviewStops: 99 }
  : process.env.LIMIT_NEAREST ? { limitDown: false } : {};
const state = { balance: 1000, trades: [], last10: [], day: null };
const lines = [];
(async () => {
  for (const f of days) {
    const D = load(f);
    newDay(state, D.day);
    if (mode === "compare") state.halt = null;
    let nowC = 0;
    const oc = {}; // core bars per option symbol
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
    const log = (e, d) => { if (["trade", "shutoff", "entry_cancel", "flatten", "x_printed"].includes(e)) lines.push(`${D.day} ${e} ${JSON.stringify(d)}`); };
    const eng = new Engine({ state, market, log, cfg });
    for (let i = 10; i < D.spy.length; i++) {
      nowC = coreT(D.spy[i]) + 60;
      await eng.tick();
      const spy = D.spy.slice(0, i + 1); // bars closed so far
      const last = spy[spy.length - 1];
      const ks = paneStrikes(+last.close);
      const opt = {};
      for (const [cp, K] of [["C", ks.call], ["P", ks.put]]) { const s = osi(D.day, cp, K); if (D.opt[s]) opt[s] = D.opt[s].filter((b) => coreT(b) <= coreT(last)); }
      const { marks, kills } = computeMarks(D.day, spy, opt);
      await eng.onMarks(marks.filter((m) => m.ts === coreT(last)), kills);
    }
    await eng.flatten("end of day");
  }
  console.log(lines.filter((l) => / (trade|shutoff) /.test(l)).map((l) => {
    const m = l.match(/^(\S+) trade (.*)$/);
    if (!m) return l;
    const t = JSON.parse(m[2]);
    return `${t.day} ${t.mark.t} ${t.mark.k}${t.mark.src ? ":" + t.mark.src : ""} ${t.mark.s} entry ${t.entry} ret ${t.ret}% pnl ${t.pnl} bal ${t.balance} | ${t.exits}`;
  }).join("\n"));
  console.log(`END balance $${state.balance.toFixed(0)} trades ${state.trades.length} losers ${state.trades.filter((t) => t.pnl <= 0).length}`);
})().catch((e) => { console.error(e); process.exit(1); });
