// Loads the CORE mark logic straight out of build_day.js (the Edge Stress Test builder), unchanged.
// build_day.js is a byte-for-byte copy of the artifact's build/build_day.js; tests/check its sha256.
const fs = require("fs");
const path = require("path");

const SRC = path.join(__dirname, "build_day.js");
const BUILD_DAY_SHA256 = "3b4f90b3a3a46030982434feef3ea98f85f9b57fc72876b0721194dc44187554";

function sha256(buf) {
  return require("crypto").createHash("sha256").update(buf).digest("hex");
}

function loadCore() {
  const raw = fs.readFileSync(SRC);
  const sha = sha256(raw);
  if (sha !== BUILD_DAY_SHA256) throw new Error(`build_day.js changed (sha ${sha}); marks would no longer match the backtest`);
  const m = raw.toString("utf8").match(/^const CORE=(".*");$/m);
  if (!m) throw new Error("CORE string not found in build_day.js");
  const CORE = JSON.parse(m[1]);
  // Same way build_day.js runs it: new Function("module","require",CORE)
  const mod = { exports: {} };
  new Function("module", "require", CORE)(mod, require);
  return mod.exports;
}

module.exports = { loadCore, BUILD_DAY_SHA256 };
