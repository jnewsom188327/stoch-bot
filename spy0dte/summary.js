// After-the-close summary: spy0dte/summaries/<day>.md (the workflow posts it as a GitHub issue so it reaches your phone)
const fs = require("fs");
const path = require("path");
// the twin (SPY0DTE_TAG) keeps its own summaries and trades.csv in spy0dte/twin_<tag>/
const dataDir = () => { const t = (process.env.SPY0DTE_TAG || "").replace(/[^a-z0-9_-]/gi, ""); return t ? path.join(__dirname, "twin_" + t) : __dirname; };

const usd = (x) => (x < 0 ? "-$" : "$") + Math.abs(Math.round(x)).toLocaleString("en-US");

function writeSummary({ day, live, st, events, stats, error, sawToday }) {
  const dir = path.join(dataDir(), "summaries");
  fs.mkdirSync(dir, { recursive: true });
  const trades = st.trades.filter((t) => t.day === day);
  const pnl = trades.reduce((a, t) => a + t.pnl, 0);
  const shut = events.filter((e) => ["shutoff", "done_for_day", "flatten", "market_closed"].includes(e.event));
  const L = [];
  L.push(`## SPY 0DTE bot · ${day} · ${live ? "LIVE" : "DRY RUN (no orders sent)"}`);
  L.push("");
  if (!sawToday) L.push("No SPY bars today (market closed?). Nothing traded.");
  L.push(`**Day:** ${usd(st.dayStart)} → ${usd(st.balance)} (${pnl >= 0 ? "+" : ""}${usd(pnl)}, ${st.dayStart ? (st.balance / st.dayStart * 100 - 100).toFixed(1) : 0}%) · ${trades.length} trade${trades.length === 1 ? "" : "s"}`);
  if (st.halt) L.push(`**Stopped today:** ${st.halt}`);
  if (st.reviewHold) L.push(`**⚠ On hold until you review:** ${st.reviewHold}. Run the workflow with clear_review = yes to restart.`);
  if (error) L.push(`**⚠ Error:** \`${error.split("\n")[0].slice(0, 300)}\``);
  const br = st.brake || {};
  if (br.need > 0) L.push(`**Safety brake on:** paper only until ${br.need} more paper win${br.need === 1 ? "" : "s"} in a row (no orders sent meanwhile).`);
  if (br.half) L.push(`**Safety brake:** half port until the account is back to ${usd(br.target || 0)}.`);
  const paper = (st.paper || []).filter((p) => p.day === day);
  if (paper.length) L.push("Paper trades today (brake): " + paper.map((p) => `${p.t} ${p.s === "C" ? "call" : "put"} ${p.ret > 0 ? "+" : ""}${p.ret}%`).join(" · "));
  L.push("");
  if (trades.length) {
    L.push("| Mark | Contract | Qty | Entry | Exits | Return | P&L |");
    L.push("|---|---|---|---|---|---|---|");
    for (const t of trades) L.push(`| ${t.mark.t} ${t.mark.k}${t.mark.src ? ":" + t.mark.src : ""} ${t.mark.s} | ${t.sym} | ${t.qty} | ${t.entry.toFixed(2)} | ${t.exits} | ${t.ret}% | ${usd(t.pnl)} |`);
    L.push("");
  }
  L.push(`Marks printed: ${stats.marks} · entries placed: ${events.filter((e) => /^order_buy/.test(e.event)).length} · unfilled/cancelled: ${events.filter((e) => e.event === "entry_cancel").length}`);
  const sk = Object.entries(stats.skipped).sort((a, b) => b[1] - a[1]);
  if (sk.length) L.push("Skipped: " + sk.map(([k, n]) => `${k} ×${n}`).join(" · "));
  if (shut.length) L.push("Events: " + shut.map((e) => `${e.at} ${e.event}${e.why ? " (" + e.why + ")" : ""}`).join(" · "));
  L.push("");
  L.push(`Full log: ${path.relative(path.join(__dirname, ".."), path.join(dataDir(), "logs", day + ".jsonl"))}`);
  const md = L.join("\n");
  const file = path.join(dir, `${day}.md`);
  const title = `${live ? "LIVE" : "DRY RUN"} · ${pnl >= 0 ? "+" : ""}${usd(pnl)} · ${trades.length} trade${trades.length === 1 ? "" : "s"} · balance ${usd(st.balance)}${st.halt ? " · stopped" : ""}${st.reviewHold ? " · REVIEW NEEDED" : ""}${st.brake && st.brake.need > 0 ? " · BRAKE (paper)" : ""}${error ? " · ERROR" : ""}`;
  fs.writeFileSync(path.join(dir, `${day}.title`), title + "\n");
  fs.writeFileSync(file, md + "\n");
  if (process.env.GITHUB_STEP_SUMMARY) fs.appendFileSync(process.env.GITHUB_STEP_SUMMARY, md + "\n");
  // trade log CSV
  const csv = path.join(dataDir(), "trades.csv");
  if (!fs.existsSync(csv)) fs.writeFileSync(csv, "day,mark_time,mark,side,contract,qty,entry,return_pct,pnl,balance,exits,dry_run\n");
  for (const t of trades) fs.appendFileSync(csv, [t.day, t.mark.t, t.mark.k + (t.mark.src ? ":" + t.mark.src : ""), t.mark.s, t.sym, t.qty, t.entry, t.ret, t.pnl, t.balance, `"${t.exits}"`, t.dry ? "yes" : "no"].join(",") + "\n");
  console.log("\n" + md);
  return file;
}

module.exports = { writeSummary };
