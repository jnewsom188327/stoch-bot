// Dress rehearsal for the small-win DRY RUN bot: runs the real swbot.js against a fake Public API that replays a saved day
// (results/bars_<day>.json) on a fast clock. Fails if the bot ever tries to send an order or leaves a paper position open.
//   node spy0dte/test_swrev_mock.js 2026-11-25 [half]      (half = rehearse a 1:00 PM close like Friday Nov 27)
const fs = require("fs");
const os = require("os");
const path = require("path");

const day = process.argv[2] || "2026-11-25";
const SRC = __dirname;
const TMP = fs.mkdtempSync(path.join(os.tmpdir(), "swrev-"));
for (const f of fs.readdirSync(SRC)) if (f.endsWith(".js")) fs.copyFileSync(path.join(SRC, f), path.join(TMP, f));
fs.cpSync(path.join(SRC, "shadow_src"), path.join(TMP, "shadow_src"), { recursive: true }); // the shadow log's copied tracker code

const B = JSON.parse(fs.readFileSync(path.join(SRC, "..", "results", `bars_${day}.json`), "utf8"));
const off = B.spy[0][0].slice(-6);
const base = Date.parse(day + "T09:30:00" + off);
const iso = (ms) => new Date(ms + Number(off.slice(0, 3)) * 3600000).toISOString().slice(0, 19) + off;
const spy = B.spy.map(([t, o, h, l, c, v]) => ({ ms: Date.parse(t), timestamp: t.slice(0, 19) + t.slice(-6), open: String(o), high: String(h), low: String(l), close: String(c), volume: String(v) }));
const opt = {};
for (const [sym, rows] of Object.entries(B.opt)) opt[sym] = rows.map(([i, o, h, l, c]) => ({ ms: base + i * 60000, timestamp: iso(base + i * 60000), open: String(o), high: String(h), low: String(l), close: String(c), volume: "5" }));

let NOW = base - 10 * 60000; // 9:20 ET
const RealDate = Date;
class FakeDate extends RealDate { constructor(...a) { if (a.length) super(...a); else super(NOW); } static now() { return NOW; } }
global.Date = FakeDate;
const realSetTimeout = setTimeout;
global.setTimeout = (fn, ms) => { NOW += ms || 0; return realSetTimeout(fn, 0); };
const visible = (bars) => bars.filter((b) => b.ms <= NOW).map(({ ms, ...b }) => b);
const barAt = (bars) => [...bars].reverse().find((b) => b.ms + 60000 <= NOW);

let orderAttempts = 0, calls = 0;
global.fetch = async (url, opts = {}) => {
  const u = new URL(url), p = u.pathname, m = opts.method || "GET", body = opts.body ? JSON.parse(opts.body) : null;
  calls++;
  const ok = (j) => ({ ok: true, status: 200, text: async () => JSON.stringify(j) });
  if (p.endsWith("/access-tokens")) return ok({ accessToken: "fake" });
  if (p.endsWith("/trading/account")) return ok({ accounts: [{ accountId: "TEST1234", accountType: "BROKERAGE" }] });
  let mm;
  if ((mm = p.match(/historicdata\/(\w+)\/([^/]+)\/DAY\/ONE_MINUTE$/))) {
    if (mm[1] === "INDEX") return { ok: false, status: 400, text: async () => "unsupported" }; // no VIX1D: booster must switch off quietly
    return ok({ regularMarket: { bars: visible(mm[1] === "EQUITY" ? spy : opt[decodeURIComponent(mm[2])] || []) } });
  }
  if (p.endsWith("/quotes")) {
    const quotes = body.instruments.map(({ symbol }) => {
      const b = barAt(opt[symbol] || []);
      if (!b) return { instrument: { symbol, type: "OPTION" }, outcome: "FAILED" };
      const c = +b.close, ts = new RealDate(NOW - 2000).toISOString();
      return { instrument: { symbol, type: "OPTION" }, outcome: "SUCCESS", last: b.close, bid: (c - 0.01).toFixed(2), ask: (c + 0.01).toFixed(2), bidTimestamp: ts, askTimestamp: ts };
    });
    return ok({ quotes });
  }
  if (/\/order/.test(p) || /preflight/.test(p)) { orderAttempts++; return { ok: false, status: 400, text: async () => "orders are not allowed in the dry run test" }; }
  return { ok: false, status: 400, text: async () => "unknown " + p };
};

process.env.PUBLIC_API_SECRET = "fake";
process.env.MODE = "run";
if (process.argv[3] === "half") process.env.SW_HALF = "yes";
process.on("exit", () => {
  const st = JSON.parse(fs.readFileSync(path.join(TMP, "smallwin", "state.json"), "utf8"));
  const csv = fs.readFileSync(path.join(TMP, "smallwin", "trades.csv"), "utf8").trim().split("\n");
  console.error(`[mock] files: ${TMP}`);
  console.error(`\n[mock] ${calls} API calls · order attempts ${orderAttempts} · trades ${csv.length - 1} · balance ${st.balance}`);
  if (orderAttempts) { console.error("[mock] FAIL: the dry run tried to send an order"); process.exitCode = 1; }
});
require(path.join(TMP, "swbot.js")).main().catch((e) => { console.error(e); process.exit(1); });
