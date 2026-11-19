// temp (branch only): today's bars so far from Public, saved in the replay format
const fs = require("fs");
const { PublicAPI } = require("./public");
const { osi } = require("./marks");
(async () => {
  const day = process.env.DAY;
  const api = new PublicAPI(process.env.PUBLIC_API_SECRET);
  await api.auth();
  let spy = (await api.bars("SPY")).filter((b) => b.timestamp.slice(0, 10) === day && /:00-0[45]:00$/.test(b.timestamp));
  spy = spy.slice(0, -1); // drop the bar still forming
  const off = spy[0].timestamp.slice(-6);
  const base = new Date(day + "T09:30:00" + off).getTime();
  const lo = Math.floor(Math.min(...spy.map((b) => +b.low))) - 2, hi = Math.ceil(Math.max(...spy.map((b) => +b.high))) + 2;
  const opt = {};
  for (let K = lo; K <= hi; K++) for (const cp of ["C", "P"]) {
    const s = osi(day, cp, K);
    try {
      const b = await api.bars(s, "OPTION");
      const rows = b.filter((x) => +x.volume > 0 && /:00-0[45]:00$/.test(x.timestamp) && x.timestamp <= spy[spy.length - 1].timestamp)
        .map((x) => [Math.round((Date.parse(x.timestamp) - base) / 60000), +x.open, +x.high, +x.low, +x.close]);
      if (rows.length) opt[s] = rows;
    } catch (e) { console.log(s, String(e.message).slice(0, 100)); }
  }
  fs.mkdirSync("results", { recursive: true });
  fs.writeFileSync(`results/bars_${day}.json`, JSON.stringify({ day, feed: "public-partial", spy: spy.map((b) => [b.timestamp, +b.open, +b.high, +b.low, +b.close, +b.volume]), opt }));
  console.log(`SPY ${spy.length} bars to ${spy[spy.length - 1].timestamp}, ${Object.keys(opt).length} contracts ${lo}-${hi}`);
})().catch((e) => { console.error(e); process.exit(1); });
