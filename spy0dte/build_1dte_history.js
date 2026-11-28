// 1DTE history for the shadow logs (Nov 28, 2026). Merges the next-day (1DTE) 1-minute option bars that pull_opts.py saved
// from Alpaca (results/opt_1m/<day>.json.gz, through Nov 13) into each saved day (results/bars_<day>.json, Public's 0DTE bars),
// and sets exp = the 1DTE expiry, so replay_swrev.js runs the bot and the shadow avenues on 1DTE the way the live bot does.
// Usage: node spy0dte/build_1dte_history.js <out dir>   then
//        BARS_DIR=<out dir> SHADOW=1 SHADOW_TAG=baseline_1dte node spy0dte/replay_swrev.js
const fs = require("fs"), path = require("path"), zlib = require("zlib");
const RES = path.join(__dirname, "..", "results"), OUT = path.resolve(process.argv[2] || "/tmp/bars_1dte");
fs.mkdirSync(OUT, { recursive: true });
for (const f of ["spy_1m.csv.gz", "vixy_1m.csv.gz"]) { const p = path.join(RES, f), q = path.join(OUT, f); if (fs.existsSync(p) && !fs.existsSync(q)) fs.symlinkSync(p, q); }
let n = 0;
for (const f of fs.readdirSync(RES).filter((x) => /^bars_\d{4}-\d\d-\d\d\.json$/.test(x)).sort()) {
  const day = f.slice(5, 15), a = path.join(RES, "opt_1m", `${day}.json.gz`);
  if (!fs.existsSync(a)) continue;
  const B = JSON.parse(fs.readFileSync(path.join(RES, f), "utf8")), A = JSON.parse(zlib.gunzipSync(fs.readFileSync(a)));
  const tag = A.exp1.slice(2, 4) + A.exp1.slice(5, 7) + A.exp1.slice(8, 10);
  let k = 0;
  for (const [sym, rows] of Object.entries(A.opt)) if (sym.slice(3, 9) === tag && !B.opt[sym]) { B.opt[sym] = rows.map((r) => r.slice(0, 5)); k++; } // minute from 9:30, o, h, l, c
  B.exp = A.exp1;
  fs.writeFileSync(path.join(OUT, f), JSON.stringify(B));
  console.log(`${day}: 1DTE ${A.exp1}, ${k} contracts added`); n++;
}
console.log(`${n} days written to ${OUT}`);
