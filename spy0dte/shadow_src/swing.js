// Swing Break signals for one day (added Nov 24 at the user's request; tracking only).
// Usage: node swing.js bars_YYYY-MM-DD.json out.json   (build_day.js must sit next to this file)
// One flush = one setup: SPY's fear (calls) or greed (puts) hits 95+ while the other side is at 25 or under.
// The signal is the first minute after that where the pinned side falls AND the collapsed side rises in the same bar
// ("breaks together"); then it waits for a fresh flush. Each signal is written as a stress-test mark (k "S", src "swing")
// priced on the first out-of-the-money contract (like the other marks), with x.s2 = 1 strike in the money and
// x.rv.run15 = SPY's move against the trade over the 15 minutes before ($).
const fs=require("fs"),path=require("path");
const src=fs.readFileSync(path.join(__dirname,"build_day.js"),"utf8");
const CORE=JSON.parse(src.match(/^const CORE=(".*");$/m)[1]);
const mod={exports:{}};new Function("module","require",CORE)(mod,require);const L=mod.exports;
const B=JSON.parse(fs.readFileSync(process.argv[2],"utf8"));const day=B.day;const mmdd=day.slice(5,7)+day.slice(8,10);
const off=B.spy[0][0].slice(-6);const base=new Date(day+"T09:30:00"+off).getTime();
const toRes=bars=>JSON.stringify({regularMarket:{bars}});
const spyBars=B.spy.map(([t,o,h,l,c,v])=>({timestamp:t.slice(0,19)+t.slice(-6),open:String(o),high:String(h),low:String(l),close:String(c),volume:String(v)}));
const optBars=rows=>rows.map(([i,o,h,l,c])=>({timestamp:new Date(base+i*60000+(Number(off.slice(0,3))*3600000)).toISOString().slice(0,19)+off,open:String(o),high:String(h),low:String(l),close:String(c),volume:"1"}));
const R=L.compute(L.cleanPrints(L.parseBars(toRes(spyBars)).filter(x=>!x.live&&!x.fill)));const byT=new Map(R.map(r=>[r.t,r]));
const OB={};for(const [sym,rows] of Object.entries(B.opt))OB[sym]=L.parseBars(toRes(optBars(rows))).filter(x=>!x.live&&!x.fill).sort((x,y)=>x.t-y.t);
const t0=R[0].t;const MAXH=150;const out=[];
for(const side of ["C","P"]){const Lg=side==="C";let armed=false;
  for(let i=31;i<R.length-1&&i<330;i++){const hi=Lg?R[i].F:R[i].G,lo=Lg?R[i].G:R[i].F,hp=Lg?R[i-1].F:R[i-1].G,lp=Lg?R[i-1].G:R[i-1].F;
    if(hi>=95&&lo<=25)armed=true;
    if(!armed||!(hi<hp&&lo>lp))continue;armed=false;
    const tod=Math.round((R[i].t-t0)/60);const px=R[i].c;
    const pathFor=steps=>{const K0=Lg?Math.floor(px)+1:(Number.isInteger(px)?px-1:Math.floor(px));const K=Lg?K0-steps:K0+steps;
      const sym="SPY"+day.slice(2,4)+mmdd+side+String(K*1000).padStart(8,"0");const Bo=OB[sym];if(!Bo)return null;
      const i0=Bo.findIndex(b=>b.t>R[i].t);if(i0<0)return null;const e=Bo[i0].o;if(!(e>0))return null;const seg=Bo.slice(i0).filter(b=>b.t<=Bo[i0].t+MAXH*60);if(seg.length<5)return null;
      const q=x=>Math.round((x/e-1)*1000);const h=[],l=[],c=[],tl=[];
      for(const b of seg){h.push(q(b.h));l.push(q(b.l));c.push(q(b.c));const r=byT.get(b.t);tl.push(r&&(Lg?r.c<r.ef:r.c>r.ef)?1:0)}
      return{e:+e.toFixed(2),h,l,c,tl:tl.join("")}};
    const p0=pathFor(0),p2=pathFor(2);if(!p0||!p2)continue;
    const back=R[Math.max(0,i-15)].c;
    out.push({d:(+mmdd.slice(0,2))+"/"+(+mmdd.slice(2)),t:L.hmLabel(R[i].t),k:"S",s:side,src:"swing",g:"S",kill:0,tod,e:p0.e,h:p0.h,l:p0.l,c:p0.c,tl:p0.tl,busy:0,tw:0,ag:0,
      x:{mv30:null,eg:null,rv:{run15:+((Lg?1:-1)*(back-px)).toFixed(3),spyMy:+hi.toFixed(1),spyOther:+lo.toFixed(1)},s2:p2}})}}
out.sort((a,b)=>a.tod-b.tod);
fs.writeFileSync(process.argv[3],JSON.stringify(out));console.log(day,"swing breaks",out.length,"(calls",out.filter(m=>m.s==="C").length+", puts",out.filter(m=>m.s==="P").length+")");
