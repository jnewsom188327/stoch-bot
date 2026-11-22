// Replays saved QQQ days through the real QQQ reversal engine (qrev.js) in DRY RUN, minute by minute, from a $1,000 start.
// Usage: node spy0dte/replay_qrev.js <folder of QQQ bars_YYYY-MM-DD.json> [first day] [last day] [shadow]
//   bars files have the same shape as results/bars_<day>.json, with QQQ in "spy" and QQQ option symbols in "opt".
//   "shadow" replays the shadow version (1 ITM, a third at +30%) instead of the live one.
const fs = require("fs");
const path = require("path");
const { computeMarks, paneStrikes, osi, coreT } = require("./marks");
const { QEngine, QR_SHADOW } = require("./qrev");
const { newDay } = require("./ledger");

const dir = process.argv[2], from = process.argv[3] || "0000", to = process.argv[4] || "9999", shadow = process.argv[5] === "shadow";
const days = fs.readdirSync(dir).filter((f) => /^bars_\d{4}-\d\d-\d\d\.json$/.test(f)).sort().filter((f) => f.slice(5, 15) >= from && f.slice(5, 15) <= to);
function load(f) {
  const B = JSON.parse(fs.readFileSync(path.join(dir, f), "utf8"));
  const off = B.spy[0][0].slice(-6);
  const base = new Date(B.day + "T09:30:00" + off).getTime();
  const iso = (ms) => new Date(ms + Number(off.slice(0, 3)) * 3600000).toISOString().slice(0, 19) + off;
  const spy = B.spy.map(([t, o, h, l, c, v]) => ({ timestamp: t.slice(0, 19) + t.slice(-6), open: o, high: h, low: l, close: c, volume: v }));
  const opt = {};
  for (const [sym, rows] of Object.entries(B.opt)) opt[sym] = rows.map(([i, o, h, l, c]) => ({ timestamp: iso(base + i * 60000), open: o, high: h, low: l, close: c, volume: 1 }));
  return { day: B.day, spy, opt };
}
const cfg = { minPrice: 0, maxSpread: 99, simUnroundedFill: true, ...(shadow ? QR_SHADOW : {}), ...(process.env.CFG ? JSON.parse(process.env.CFG) : {}) };
const state = { balance: 1000, trades: [], last10: [], day: null };
const lines = [];
(async () => {
  for (const f of days) {
    const D = load(f);
    if (D.spy.length < 380) continue;
    newDay(state, D.day);
    let nowC = 0;
    const oc = {};
    for (const [sym, bars] of Object.entries(D.opt)) oc[sym] = bars.map((b) => ({ t: coreT(b), o: +b.open, h: +b.high, l: +b.low, c: +b.close }));
    const market = {
      nowC: () => nowC,
      optBars: (sym) => (oc[sym] || []).filter((b) => b.t + 60 <= nowC),
      quote: async (sym, m) => {
        const bars = oc[sym] || [];
        const b = m ? bars.find((x) => x.t > m.ts) : [...bars].reverse().find((x) => x.t + 60 <= nowC);
        if (!b) return null;
        const ref = m ? b.o : b.c;
        return { bid: ref, ask: ref, ref, spreadPct: 0, stale: false };
      },
    };
    const log = (e, d) => { if (["trade", "shutoff", "brake_on", "brake_off", "brake_half", "paper_trade"].includes(e)) lines.push(`${D.day} ${e} ${JSON.stringify(d)}`); };
    const eng = new QEngine({ state, market, log, cfg });
    for (let i = 10; i < D.spy.length; i++) {
      nowC = coreT(D.spy[i]) + 60;
      await eng.tick();
      const spy = D.spy.slice(0, i + 1);
      const last = spy[spy.length - 1];
      const ks = paneStrikes(+last.close);
      const opt = {};
      for (const [cp, K] of [["C", ks.call], ["P", ks.put]]) { const s = osi(D.day, cp, K, undefined, "QQQ"); if (D.opt[s]) opt[s] = D.opt[s].filter((b) => coreT(b) <= coreT(last)); }
      const { marks, kills } = computeMarks(D.day, spy, opt, "QQQ");
      eng.setSpy(spy);
      await eng.onMarks(marks.filter((m) => m.ts === coreT(last)), kills);
    }
    await eng.flatten("end of day");
  }
  for (const l of lines) {
    const m = l.match(/^(\S+) trade (.*)$/);
    if (!m) { console.log(l); continue; }
    const t = JSON.parse(m[2]);
    console.log(`${t.day} ${t.mark.t} P:${t.mark.src} ${t.mark.s} ${t.sym} entry ${t.entry} ret ${t.ret}% bal ${t.balance} | ${t.exits}`);
  }
  console.log(`END balance $${state.balance.toFixed(0)} trades ${state.trades.length} losers ${state.trades.filter((t) => t.pnl <= 0).length}`);
})().catch((e) => { console.error(e); process.exit(1); });
