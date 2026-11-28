// In-the-money prices + trend strength for the Edge Stress Test marks of one day (option 2: strike + size by trend).
// Usage: node itm.js bars_YYYY-MM-DD.json out.json   (build_day.js must sit next to this file)
// For every mark build_day.js makes, writes { key: { mv30, eg, s0:{e,h,l,c,tl}, s2:{...}, s4:{...} } }
//   key = "M/D|time|kind|src|side" (same fields as marks.json), s0 = the mark's own strike (a check: equals marks.json),
//   s2 = 2 strikes in from it (1 in the money), s4 = 4 strikes in (3 in the money), built exactly like build_day.js builds its path.
//   mv30 = SPY's move your way over the last 30 min ($), eg = EMA13 - EMA34 your way ($), both on 9:30-on closes; null before 10:01.
const fs=require("fs"),path=require("path");
const src=fs.readFileSync(path.join(__dirname,"build_day.js"),"utf8");
const CORE=JSON.parse(src.match(/^const CORE=(".*");$/m)[1]);
const mod={exports:{}};new Function("module","require",CORE)(mod,require);const L=mod.exports;const S=L.S;
const B=JSON.parse(fs.readFileSync(process.argv[2],"utf8"));const day=B.day;const mmdd=day.slice(5,7)+day.slice(8,10);
const off=B.spy[0][0].slice(-6);const base=new Date(day+"T09:30:00"+off).getTime();
const toRes=bars=>JSON.stringify({regularMarket:{bars}});
const spyBars=B.spy.map(([t,o,h,l,c,v])=>({timestamp:t.slice(0,19)+t.slice(-6),open:String(o),high:String(h),low:String(l),close:String(c),volume:String(v)}));
const optBars=rows=>rows.map(([i,o,h,l,c])=>({timestamp:new Date(base+i*60000+(Number(off.slice(0,3))*3600000)).toISOString().slice(0,19)+off,open:String(o),high:String(h),low:String(l),close:String(c),volume:"1"}));
const R=L.compute(L.cleanPrints(L.parseBars(toRes(spyBars)).filter(x=>!x.live&&!x.fill)));S.spy=R;S.sigs=L.signals(R.slice(0,-1));const byT=new Map(R.map(r=>[r.t,r]));
const OB={};for(const [sym,rows] of Object.entries(B.opt))OB[sym]=L.parseBars(toRes(optBars(rows))).filter(x=>!x.live&&!x.fill).sort((x,y)=>x.t-y.t);
// trend strength on the raw 9:30-on SPY closes (same numbers the dot bot uses)
const C=B.spy.map(r=>+r[4]);const e13=[],e34=[];{let a=C[0],b=C[0];for(const x of C){a+=(x-a)*(2/14);b+=(x-b)*(2/35);e13.push(a);e34.push(b)}}
const MAXH=150;const marks=[];
// Fear/greed (Vix Fix) on any minute series, as the chart pane: fear = wvf/max50(wvf)x100, wvf = (22-bar highest close - low)/that high x100; greed mirrored.
const fgArr=(H,L,Cc)=>{const n=Cc.length,wf=[],ws=[],F=[],G=[];for(let k=0;k<n;k++){const a=Cc.slice(Math.max(0,k-21),k+1),hc=Math.max(...a),lc=Math.min(...a);wf.push(hc>0?(hc-L[k])/hc*100:0);ws.push(lc>0?(H[k]-lc)/lc*100:0)}
  for(let k=0;k<n;k++){const mf=Math.max(...wf.slice(Math.max(0,k-49),k+1))||1e-9,mg=Math.max(...ws.slice(Math.max(0,k-49),k+1))||1e-9;F.push(wf[k]/mf*100);G.push(ws[k]/mg*100)}return[F,G]};
const SPYH=B.spy.map(r=>+r[2]),SPYL=B.spy.map(r=>+r[3]);const [SF,SG]=fgArr(SPYH,SPYL,C);
const optFG={};const fgOf=sym=>{if(sym in optFG)return optFG[sym];const rows=B.opt[sym];if(!rows){optFG[sym]=null;return null}const by=new Map(rows.map(r=>[r[0],r]));const H=[],L=[],Cc=[];let last=null;
  for(let i=0;i<C.length;i++){const r=by.get(i);if(r){last=+r[4];H.push(+r[2]);L.push(+r[3]);Cc.push(+r[4])}else{H.push(last);L.push(last);Cc.push(last)}}
  const f=Cc.findIndex(v=>v!=null);if(f<0){optFG[sym]=null;return null}for(let i=0;i<f;i++){H[i]=L[i]=Cc[i]=Cc[f]}optFG[sym]=fgArr(H,L,Cc);return optFG[sym]};
for(const s of S.sigs){if(s.kind==="add")marks.push(["A",s,null]);if(s.kind==="stall"){const d=L.dotTrade(s);if(d)marks.push(["D",d,null])}}
const a=L.vixArrows(R.slice(0,-1));for(const t of a.g)marks.push(["P",{t,side:"long"},"SPY"]);for(const t of a.f)marks.push(["P",{t,side:"short"},"SPY"]);
for(const sym of Object.keys(OB)){const cp=sym[9],K=+sym.slice(10)/1000;const rows=L.compute(L.cleanPrints(OB[sym]));
  for(const t of L.vixArrows(rows.slice(0,-1)).g){const r=byT.get(t);if(!r)continue;if((cp==="C"?Math.floor(r.c)+1:Math.ceil(r.c)-1)!==K)continue;marks.push(["P",{t,side:cp==="C"?"long":"short"},cp==="C"?"call":"put"])}}
const out={};let n=0,miss=0;
for(const [k,m0,srcK] of marks){const s=m0.px?m0:L.dotTrade(m0);if(!s)continue;const tod=L.etMin(s.t)-570;if(tod>330||tod<10)continue;const Lg=s.side==="long";
  const K0=Lg?Math.floor(s.px)+1:(Number.isInteger(s.px)?s.px-1:Math.floor(s.px));
  const pathFor=(steps,L=Lg)=>{const K0x=L?Math.floor(s.px)+1:(Number.isInteger(s.px)?s.px-1:Math.floor(s.px));const K=L?K0x-steps:K0x+steps;const sym="SPY"+day.slice(2,4)+mmdd+(L?"C":"P")+String(K*1000).padStart(8,"0");const Bo=OB[sym];if(!Bo)return null;
    const i0=Bo.findIndex(b=>b.t>s.t);if(i0<0)return null;const e=Bo[i0].o;if(!(e>0))return null;const seg=Bo.slice(i0).filter(b=>b.t<=Bo[i0].t+MAXH*60);if(seg.length<5)return null;
    const q=x=>Math.round((x/e-1)*1000);const h=[],l=[],c=[],tl=[];
    for(const b of seg){h.push(q(b.h));l.push(q(b.l));c.push(q(b.c));const r=byT.get(b.t);tl.push(r&&(L?r.c<r.ef:r.c>r.ef)?1:0)}
    return{e:+e.toFixed(2),h,l,c,tl:tl.join(""),sym}};
  const s0=pathFor(0);if(!s0)continue;n++;
  const d=Lg?1:-1;let mv30=null,eg=null;if(tod>=31&&tod<C.length){mv30=+(d*(C[tod]-C[tod-30])).toFixed(3);eg=+(d*(e13[tod]-e34[tod])).toFixed(3)}
  const key=[(+mmdd.slice(0,2))+"/"+(+mmdd.slice(2)),L.hmLabel(s.t),k,srcK,Lg?"C":"P"].join("|");
  const s2=pathFor(2),s4=pathFor(4);if(!s2||!s4)miss++;
  // "ran hard, then stalled" reversal readings (null before 10:01): mv15 = SPY's move your way over the last 15 min ($),
  // ne5 = 1 if SPY made a new day low (calls) / high (puts) in the last 5 min, st = avg candle body of the last 3 bars / the 10 before
  let rv=null;if(tod>=31&&tod<C.length){const O=B.spy.map(r=>+r[1]),H=B.spy.map(r=>+r[2]),Lo=B.spy.map(r=>+r[3]),i=tod;
    const ne5=d===1?Math.min(...Lo.slice(i-4,i+1))<=Math.min(...Lo.slice(0,i-4)):Math.max(...H.slice(i-4,i+1))>=Math.max(...H.slice(0,i-4));
    const bod=(a,z)=>{let t=0;for(let j=a;j<z;j++)t+=Math.abs(C[j]-O[j]);return t/(z-a)};
    rv={mv15:+(d*(C[i]-C[i-15])).toFixed(3),ne5:ne5?1:0,st:+(bod(i-2,i+1)/Math.max(.001,bod(i-12,i-2))).toFixed(3)}}
  // Vix Fix stretch on your side (fear for calls, greed for puts), same math as the chart pane: vk = highest reading over the last 10 bars
  if(rv){const i=tod,Hh=B.spy.map(r=>+r[2]),Ll=B.spy.map(r=>+r[3]);const sideAt=j=>{
      if(d===1){const w=k=>{const hc=Math.max(...C.slice(Math.max(0,k-21),k+1));return (hc-Ll[k])/hc*100};let mx=0;for(let k=Math.max(0,j-49);k<=j;k++)mx=Math.max(mx,w(k));return w(j)/(mx||1e-9)*100}
      const w=k=>{const lc=Math.min(...C.slice(Math.max(0,k-21),k+1));return (Hh[k]-lc)/lc*100};let mx=0;for(let k=Math.max(0,j-49);k<=j;k++)mx=Math.max(mx,w(k));return w(j)/(mx||1e-9)*100};
    let pk=0;for(let j=i-9;j<=i;j++)pk=Math.max(pk,sideAt(j));rv.vk=+pk.toFixed(1)}
  // Public Fade readings: dm = SPY's move since the open your way (%); bar15 = average 1-min candle (high-low, $) over the last 15 bars;
  // so = SPY's OTHER side of the fear/greed pane now (greed for calls, fear for puts); cF/cG = the bought contract's own fear peak (last 10 bars) and greed now
  if(rv){const i=tod,O0=+B.spy[0][1];rv.dm=+(d*(C[i]-O0)/O0*100).toFixed(3);let b15=0;for(let j=i-14;j<=i;j++)b15+=SPYH[j]-SPYL[j];rv.bar15=+(b15/15).toFixed(3);
    rv.so=+(d===1?SG[i]:SF[i]).toFixed(1);const cf=s2&&fgOf(s2.sym);if(cf){let p=0;for(let j=i-9;j<=i;j++)p=Math.max(p,cf[0][j]);rv.cF=+p.toFixed(1);rv.cG=+cf[1][i].toFixed(1)}}
  const strip=p=>p&&{e:p.e,h:p.h,l:p.l,c:p.c,tl:p.tl};const o2=strip(pathFor(2,!Lg));
  out[key]={mv30,eg,rv,s0:process.env.CHECK?s0:{e:s0.e},s2:strip(s2),s4:strip(s4),o2}}
fs.writeFileSync(process.argv[3],JSON.stringify(out));console.log(day,"marks",n,"keys",Object.keys(out).length,"missing an ITM strike",miss);
