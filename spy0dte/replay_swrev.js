// Replays the tracked days (results/bars_YYYY-MM-DD.json) through the small-win engine (swrev.js) in DRY RUN, minute by minute.
// Usage: node spy0dte/replay_swrev.js [first day] [last day]        -> every trade with its setup, boosters and readings
//        CFG='{"tp":0.1}' SWP='{"setMin":85}' SWG='{"min":0.8}' node spy0dte/replay_swrev.js   (override settings)
// VIX1D: there is no VIX1D minute history in the repo, so the replay uses VIXY 1-minute bars (results/vixy_1m.csv.gz,
// through Nov 17) as a stand-in for the vix1d_div booster. Live, the bot reads VIX1D from Public when it can.
const fs = require("fs");
const path = require("path");
const zlib = require("zlib");
const { loadCore } = require("./core");
const { computeMarks, coreT } = require("./marks");
const { SwEngine, swMarks, weakOpen, SW, SWING, BOOST, SW_CFG } = require("./swrev");
const { newDay } = require("./ledger");

const RES = process.env.BARS_DIR ? path.resolve(process.env.BARS_DIR) : path.join(__dirname, "..", "results");
const L = loadCore();
const toRes = (bars) => JSON.stringify({ regularMarket: { bars } });
const isoCore = (iso) => { const m = iso.match(/([+-])(\d\d):(\d\d)$/); const off = (m[1] === "-" ? -1 : 1) * (+m[2] * 3600 + +m[3] * 60); return Math.floor(Date.parse(iso) / 60000) * 60 + off; };

function loadVix() {
  const f = path.join(RES, "vixy_1m.csv.gz");
  const m = new Map();
  if (!fs.existsSync(f)) return m;
  for (const line of zlib.gunzipSync(fs.readFileSync(f)).toString().split("\n").slice(1)) {
    const a = line.split(","); if (a.length < 5) continue;
    m.set(isoCore(a[0].replace(" ", "T")), +a[4]);
  }
  return m;
}
function prevCloses() { // day -> previous session's last close
  const out = {};
  const f = path.join(RES, "spy_1m.csv.gz");
  const last = {};
  if (fs.existsSync(f)) for (const line of zlib.gunzipSync(fs.readFileSync(f)).toString().split("\n").slice(1)) { const a = line.split(","); if (a.length > 4) last[a[0].slice(0, 10)] = +a[4]; }
  return last;
}

function loadDay(f) {
  const B = JSON.parse(fs.readFileSync(path.join(RES, f), "utf8"));
  const off = B.spy[0][0].slice(-6);
  const base = new Date(B.day + "T09:30:00" + off).getTime();
  const iso = (ms) => new Date(ms + Number(off.slice(0, 3)) * 3600000).toISOString().slice(0, 19) + off;
  const spy = B.spy.map(([t, o, h, l, c, v]) => ({ timestamp: t.slice(0, 19) + t.slice(-6), open: o, high: h, low: l, close: c, volume: v }));
  const opt = {};
  for (const [sym, rows] of Object.entries(B.opt)) opt[sym] = rows.map(([i, o, h, l, c]) => ({ timestamp: iso(base + i * 60000), open: o, high: h, low: l, close: c, volume: 1 }));
  const rows = L.compute(L.cleanPrints(L.parseBars(toRes(spy.map((b) => ({ ...b, open: String(b.open), high: String(b.high), low: String(b.low), close: String(b.close), volume: String(b.volume) })))).filter((x) => !x.live && !x.fill)));
  const optRows = {}, oc = {};
  for (const [sym, bars] of Object.entries(opt)) {
    const p = L.parseBars(toRes(bars.map((b) => ({ timestamp: b.timestamp, open: String(b.open), high: String(b.high), low: String(b.low), close: String(b.close), volume: "1" }))));
    optRows[sym] = L.compute(L.cleanPrints((p || []).filter((x) => !x.live && !x.fill)));
    oc[sym] = bars.map((b) => ({ t: coreT(b), o: +b.open, h: +b.high, l: +b.low, c: +b.close }));
  }
  const { marks, kills } = computeMarks(B.day, spy, opt);
  let vixRows = null;
  if (B.vix) { const p = L.parseBars(toRes(B.vix.map(([t, o, h, l, c]) => ({ timestamp: t, open: String(o), high: String(h), low: String(l), close: String(c), volume: "1" })))); if (p) vixRows = new Map(L.compute(L.cleanPrints(p.filter((x) => !x.live && !x.fill))).map((x) => [x.t, x])); }
  const pane = marks.filter((m) => m.k === "P").map((m) => ({ ts: m.ts, side: m.side, src: m.src }));
  return { file: f, day: B.day, exp: B.exp || B.day, vixRows, spy, rows, optRows, oc, pane, kills, n: B.spy.length };
}

let CACHE = null;
function days(from = "0000", to = "9999") {
  if (!CACHE) {
    const pc = prevCloses();
    const files = fs.readdirSync(RES).filter((f) => (/^bars_\d{4}-\d\d-\d\d\.json$/.test(f) || /^\d{4}-\d\d-\d\d\.json$/.test(f))).sort();
    CACHE = [];
    let prev = null;
    for (const f of files) {
      const D = loadDay(f);
      const pd = Object.keys(pc).filter((d) => d < D.day).sort().pop();
      D.prevClose = prev != null ? prev : pd ? pc[pd] : null;
      prev = D.rows.length ? D.rows[D.rows.length - 1].c : prev;
      CACHE.push(D);
    }
  }
  return CACHE.filter((D) => D.day >= from && D.day <= to && D.n >= 200); // full days and half days (1:00 close)
}

let VIXROWS = null;
function vixRowsFor(D) {
  if (D.vixRows) return D.vixRows;
  if (!VIXROWS) {
    VIXROWS = new Map();
    const f = path.join(__dirname, "..", "results", "vixy_1m.csv.gz");
    if (fs.existsSync(f)) {
      const byDay = {};
      for (const line of zlib.gunzipSync(fs.readFileSync(f)).toString().split("\n").slice(1)) { const a = line.split(","); if (a.length < 5) continue; const d = a[0].slice(0, 10); (byDay[d] = byDay[d] || []).push({ timestamp: a[0].replace(" ", "T"), open: a[1], high: a[2], low: a[3], close: a[4], volume: "1" }); }
      for (const [d, bars] of Object.entries(byDay)) { const p = L.parseBars(toRes(bars)); if (p) VIXROWS.set(d, new Map(L.compute(L.cleanPrints(p.filter((x) => !x.live && !x.fill))).map((x) => [x.t, x]))); }
    }
  }
  return VIXROWS.get(D.day) || null;
}

async function run({ cfg = {}, swp = {}, swg = {}, from, to, vix = null, quiet = true, hook = null } = {}) {
  Object.assign(SWING, swg);
  const P = { ...SW, ...swp };
  const state = { balance: 1000, trades: [], last10: [], day: null };
  const lines = [];
  let maxDD = 0, peakBal = 1000;
  for (const D of days(from, to)) {
    newDay(state, D.day);
    let nowC = 0;
    const market = {
      nowC: () => nowC,
      optBars: (sym) => (D.oc[sym] || []).filter((b) => b.t + 60 <= nowC),
      quote: async (sym, m) => {
        const bars = D.oc[sym] || [];
        const b = m ? bars.find((x) => x.t > m.ts) : [...bars].reverse().find((x) => x.t + 60 <= nowC);
        if (!b) return null;
        const ref = m ? b.o : b.c;
        return { bid: ref, ask: ref, ref, spreadPct: 0, stale: false };
      },
    };
    const log = (e, d) => { if (!quiet && ["shutoff", "confirm"].includes(e)) lines.push(`${D.day} ${e} ${JSON.stringify(d)}`); };
    const halfCfg = D.n < 300 ? { lastEntryTod: 180, flattenAtTod: 200 } : {}; // half day: entries until 12:30, flat by 12:50
    const eng = new SwEngine({ state, market, log, cfg: { minPrice: 0, maxSpread: 99, ...halfCfg, ...cfg } });
    let wo = null;
    const armed = {};
    for (let i = 10; i < D.rows.length; i++) {
      const R = D.rows.slice(0, i + 1), t = R[i].t;
      nowC = t + 60;
      if (i === 14) wo = weakOpen(R, D.prevClose);
      eng.setCtx(R, D.pane.filter((a) => a.ts <= t));
      await eng.tick();
      const ms = swMarks(D.exp, R, P, L.hmLabel, { optRows: D.optRows, weakOpen: !!wo, vix: vix || null, vixRows: cfg.noVixPane ? null : vixRowsFor(D), swing: swp.swing !== false, armed, bothBoost: !!swp.bothBoost });
      await eng.onMarks(ms, D.kills.filter((k) => k.ts <= t));
      if (hook) hook.minute(D, t, eng); // shadow baseline: reads the position side only
    }
    await eng.flatten("end of day");
    if (hook) await hook.day(D, state);
    peakBal = Math.max(peakBal, state.balance); maxDD = Math.min(maxDD, state.balance / peakBal - 1);
  }
  const T = state.trades;
  return { end: state.balance, n: T.length, wins: T.filter((t) => t.pnl > 0).length, worst: T.length ? Math.min(...T.map((t) => t.ret)) : 0, maxDD, trades: T, lines };
}

module.exports = { run, days, loadVix };

// SHADOW=1: also replay the shadow avenues on every saved day (the baseline): writes spy0dte/smallwin/shadow_baseline.csv,
// shadow_baseline_real.csv and SHADOW_BASELINE.md. The engine's trades are the same either way.
async function shadowBaseline(r0opts) {
  const S = require("./shadow");
  const busy = new Map();
  const out = path.join(__dirname, "smallwin");
  fs.mkdirSync(out, { recursive: true });
  const csv = path.join(out, "shadow_baseline.csv"), rcsv = path.join(out, "shadow_baseline_real.csv");
  for (const f of [csv, rcsv]) if (fs.existsSync(f)) fs.unlinkSync(f);
  const hook = {
    minute(D, t, eng) { const p = eng.pos || eng.pending; if (!busy.has(D.day)) busy.set(D.day, new Map()); if (p && p.m) busy.get(D.day).set(Math.round((((t % 86400) + 86400) % 86400) / 60 - 570), p.m.s); },
  };
  const tmp = path.join(out, ".shadow_tmp");
  fs.mkdirSync(tmp, { recursive: true });
  // finish() writes shadow.csv / shadow_real.csv; the baseline keeps them under their own names
  hook.day = async (D, state) => { const B = JSON.parse(fs.readFileSync(path.join(RES, D.file), "utf8")); S.finish(D.day, B, busy.get(D.day) || new Map(), state.trades, tmp, null); };
  const r = await run({ ...r0opts, hook });
  fs.renameSync(path.join(tmp, "shadow.csv"), csv); fs.renameSync(path.join(tmp, "shadow_real.csv"), rcsv); fs.rmSync(tmp, { recursive: true, force: true });
  const rows = S.parseCsv(csv), real = S.parseCsv(rcsv), days = [...new Set(rows.map((x) => x.date))];
  const L = [`# Shadow baseline · ${days.length} saved days (${days[0]} to ${days[days.length - 1]}) · 0DTE bars (1DTE bars are saved from Nov 30 on)`, "",
    "Every signal scored on its own (one row per signal, overlapping signals all counted). 5% bid, skipped if it doesn't fill.", "",
    "| Avenue | Signals | Filled | Own exits: won · avg · total · worst | Small-win exits: won · avg · total · worst |", "|---|---|---|---|---|"];
  for (const a of S.AVENUES) { const T = rows.filter((x) => x.avenue === a.id), A = S.record(T, "result_a"), Bb = S.record(T, "result_b");
    L.push(`| ${a.name} | ${T.length} | ${A.filled} | ${A.filled ? `${A.won}/${A.filled} (${A.pct}%) · ${A.avg}% · ${A.sum}% · ${A.worst}%` : "—"} | ${Bb.filled ? `${Bb.won}/${Bb.filled} (${Bb.pct}%) · ${Bb.avg}% · ${Bb.sum}% · ${Bb.worst}%` : "—"} |`); }
  const tw = rows.filter((x) => x.avenue === "trend" && x.both_charts);
  const y = S.record(tw.filter((x) => x.both_charts === "yes"), "result_a"), n = S.record(tw.filter((x) => x.both_charts === "no"), "result_a");
  L.push("", `Trend safety check (both charts breaking your way): yes ${y.won}/${y.filled} (${y.pct}%) avg ${y.avg}% · no ${n.won}/${n.filled} (${n.pct}%) avg ${n.avg}%`);
  const usd = (x) => "$" + Math.round(x).toLocaleString("en-US");
  const safe = rows.filter((x) => x.avenue !== "trend" || x.both_charts === "yes");
  const alone = S.combine([], real, "result_a", [], true);
  L.push("", "One $1,000 account, first come, one trade at a time (full port; weak-trend signals half):", "",
    "| Account | Own exits | Small-win exits |", "|---|---|---|");
  const acct = (lab, R, ids, withReal) => { const a = S.combine(R, real, "result_a", ids, withReal), b = S.combine(R, real, "result_b", ids, withReal); L.push(`| ${lab} | ${usd(a.eq)} · ${a.n} trades · ${a.won} won · worst drop ${Math.round(a.mdd * 100)}% | ${usd(b.eq)} · ${b.n} trades · ${b.won} won · worst drop ${Math.round(b.mdd * 100)}% |`); };
  L.push(`| Small-win reversal bot alone | ${usd(alone.eq)} · ${alone.n} trades · ${alone.won} won · worst drop ${Math.round(alone.mdd * 100)}% | (same) |`);
  acct("Trend (safety check) + reversal dots (lined up)", safe, ["trend", "lined"], false);
  acct("All three (+ Swing Break)", safe, ["trend", "lined", "swing"], false);
  for (const a of S.AVENUES) acct(`Small-win bot + ${a.name}`, a.id === "trend" ? safe : rows, [a.id], true);
  L.push("", "Rules are copied from the Edge Stress Test (build/track.js, swing.js, itm.js) and the 1 ITM Confluence trackers (lu_track.js, bs_build.js). Replay fills at the next bar's open with the 1¢ slip the trackers use; live fills will cost a little more.");
  fs.writeFileSync(path.join(out, "SHADOW_BASELINE.md"), L.join("\n") + "\n");
  console.log(L.join("\n"));
  return r;
}

module.exports.shadowBaseline = shadowBaseline;

if (require.main === module && process.env.SHADOW === "1") {
  shadowBaseline({ from: process.argv[2], to: process.argv[3], vix: loadVix(), quiet: true }).catch((e) => { console.error(e); process.exit(1); });
} else if (require.main === module) {
  (async () => {
    const cfg = process.env.CFG ? JSON.parse(process.env.CFG) : {}, swp = process.env.SWP ? JSON.parse(process.env.SWP) : {}, swg = process.env.SWG ? JSON.parse(process.env.SWG) : {};
    const r = await run({ cfg, swp, swg, from: process.argv[2], to: process.argv[3], vix: loadVix(), quiet: false });
    for (const t of r.trades) console.log(`${t.day} ${t.mark.t} ${t.setup.padEnd(5)} ${t.mark.s} [${t.boosters}] ${t.sym} x${t.qty} @${t.entry} ${t.ret >= 0 ? "+" : ""}${t.ret}% $${Math.round(t.pnl)} bal $${Math.round(t.balance)} | ${t.confirm} | ${t.exits}`);
    for (const l of r.lines.filter((l) => / shutoff /.test(l))) console.log(l);
    console.log(`END $${r.end.toFixed(0)} · ${r.n} trades · ${r.wins} wins · worst trade ${r.worst}% · max drawdown ${(r.maxDD * 100).toFixed(1)}%`);
  })().catch((e) => { console.error(e); process.exit(1); });
}
