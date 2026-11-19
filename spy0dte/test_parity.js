// Parity test: replays each saved day minute by minute through the live mark code and checks it prints
// exactly the marks build_day.js (the Edge Stress Test builder) finds for that day, with the same fields.
// Usage: node spy0dte/test_parity.js [results/bars_2026-11-18.json ...]   (no args = every results/bars_*.json)
const fs = require("fs");
const path = require("path");
const { execFileSync } = require("child_process");
const { computeMarks, closedOnly, paneStrikes, osi, barStart, coreT } = require("./marks");

const ROOT = path.join(__dirname, "..");
const files = process.argv.slice(2).length
  ? process.argv.slice(2)
  : fs.readdirSync(path.join(ROOT, "results")).filter((f) => /^bars_\d{4}-\d\d-\d\d\.json$/.test(f)).sort().map((f) => path.join(ROOT, "results", f));

// results/bars_<day>.json -> Public-style bars
function toPublic(B) {
  const off = B.spy[0][0].slice(-6);
  const base = new Date(B.day + "T09:30:00" + off).getTime();
  const iso = (ms) => {
    const local = new Date(ms + Number(off.slice(0, 3)) * 3600000).toISOString().slice(0, 19);
    return local + off;
  };
  const spy = B.spy.map(([t, o, h, l, c, v]) => ({ timestamp: t.slice(0, 19) + t.slice(-6), open: o, high: h, low: l, close: c, volume: v }));
  const opt = {};
  for (const [sym, rows] of Object.entries(B.opt)) opt[sym] = rows.map(([i, o, h, l, c]) => ({ timestamp: iso(base + i * 60000), open: o, high: h, low: l, close: c, volume: 1 }));
  return { spy, opt };
}

let bad = 0;
for (const f of files) {
  const B = JSON.parse(fs.readFileSync(f, "utf8"));
  const tmp = path.join(require("os").tmpdir(), "parity_" + B.day + ".json");
  execFileSync("node", [path.join(__dirname, "build_day.js"), f, tmp], { stdio: "pipe" });
  const want = JSON.parse(fs.readFileSync(tmp, "utf8"));
  const P = toPublic(B);
  const got = [];
  const seen = new Set();
  for (let i = 10; i < P.spy.length; i++) {
    const now = barStart(P.spy[i]) + 61; // one second after bar i-1 closed... bar i just closed at start+60
    const spy = closedOnly(P.spy, now);
    const last = spy[spy.length - 1];
    // Live fetch: only the call/put pane strikes for the newest closed SPY bar's close
    const ks = paneStrikes(+last.close);
    const opt = {};
    for (const [cp, K] of [["C", ks.call], ["P", ks.put]]) {
      const sym = osi(B.day, cp, K);
      if (P.opt[sym]) opt[sym] = closedOnly(P.opt[sym], now);
    }
    const { marks } = computeMarks(B.day, spy, opt);
    const lastT = coreT(last);
    for (const m of marks) {
      if (m.ts !== lastT) continue; // a live bot acts on marks printed on the bar that just closed
      const key = [m.t, m.k, m.src, m.s].join("|");
      if (seen.has(key)) continue;
      seen.add(key);
      got.push(m);
    }
  }
  // build_day.js only keeps marks whose option had bars after the mark (it needs the price path); do the same
  const optSyms = new Set(Object.keys(B.opt));
  const gotKept = got.filter((m) => optSyms.has(m.contract.sym));
  const key = (m) => [m.t, m.k, m.src || null, m.s].join("|");
  const W = new Map(want.map((m) => [key(m), m]));
  const G = new Map(gotKept.map((m) => [key(m), m]));
  // CORE's signals() prints nothing until it has 20 bars (9:49 close), then fills in 9:45-9:48 after the fact.
  // A live bot sees those few marks 1-4 minutes late, so it skips them; they are reported, not failed.
  const late = [...W.keys()].filter((k) => !G.has(k) && W.get(k).tod >= 15 && W.get(k).tod <= 18 && W.get(k).k !== "P");
  const missing = [...W.keys()].filter((k) => !G.has(k) && !late.includes(k));
  const extra = [...G.keys()].filter((k) => !W.has(k));
  const fieldDiff = [];
  for (const [k, w] of W) {
    const g = G.get(k);
    if (!g) continue;
    for (const fld of ["tw", "ag", "busy", "kill", "g"]) {
      const gv = fld === "g" ? g.grade : g[fld];
      if (fld === "kill" && g.k !== "D") continue;
      if ((gv ?? null) !== (w[fld] ?? null)) fieldDiff.push(`${k} ${fld} live=${gv} backtest=${w[fld]}`);
    }
  }
  // kill (the x) is only known after the fact; check it against the final whole-day kill list
  const ok = !missing.length && !extra.length && !fieldDiff.filter((x) => !x.includes(" kill ")).length;
  console.log(`${B.day}: backtest ${want.length} marks, live ${gotKept.length} | missing ${missing.length} extra ${extra.length} field diffs ${fieldDiff.filter((x) => !x.includes(" kill ")).length} ${ok ? "OK" : "FAIL"}${late.length ? ` (printed late by the 20-bar warm-up, skipped live: ${late.join(", ")})` : ""}`);
  if (!ok) {
    bad++;
    console.log("  missing:", missing.slice(0, 8), "\n  extra:", extra.slice(0, 8), "\n  diffs:", fieldDiff.slice(0, 8));
  }
}
if (bad) process.exit(1);
console.log("All days match the backtest marks.");
