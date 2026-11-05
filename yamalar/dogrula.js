const {JSDOM,VirtualConsole}=require('jsdom');const fs=require('fs');const vc=new VirtualConsole();
const dom=new JSDOM('<!doctype html><html><head></head><body><div id="root"></div></body></html>',{runScripts:'outside-only',pretendToBeVisual:true,url:'https://test.local/',virtualConsole:vc});
try{dom.window.matchMedia=()=>({matches:false,addListener(){},removeListener(){},addEventListener(){},removeEventListener(){}});dom.window.eval(fs.readFileSync(process.argv[2]||'t_oz.js','utf8'))}catch(e){}
setTimeout(()=>{const w=dom.window,Q=w.__QU;const ay=process.argv.slice(3).map(f=>JSON.parse(fs.readFileSync(f,'utf8')));const S=ay[0].S,c=ay[0].cols;
 const J=x=>JSON.parse(JSON.stringify(x));const parca=ay.map(a=>J(Q(a.rows,c,S)));const tum=J(Q(ay.flatMap(a=>a.rows),c,S));
 const t0=Date.now();const M=J(w.__ozetBirlestir(parca));const ms=Date.now()-t0;
 const LISTE=new Set(["exceed","kapatmaSureDetay","kapatilmayanVakalar","girilmeyenVakalar","takilmayanVakalar","vakaKoordinatlari"]);
 const fark=[];let n=0;
 const kars=(m,t,p)=>{if(t===null||typeof t!=='object'){n++;if(JSON.stringify(m)!==JSON.stringify(t))fark.push(p+' : '+JSON.stringify(m)+' ≠ '+JSON.stringify(t));return}
  if(Array.isArray(t)){if(!Array.isArray(m)){fark.push(p+' dizi yok');return}if(m.length!==t.length)fark.push(p+' uzunluk '+m.length+'≠'+t.length);for(let i=0;i<Math.min(m.length,t.length);i++)kars(m[i],t[i],p+'['+i+']');return}
  for(const k of Object.keys(t)){if(LISTE.has(k)||k.startsWith('__'))continue;kars(m?m[k]:undefined,t[k],p+'.'+k)}};
 kars(M,tum,'R');
 const boy=JSON.stringify(parca[0]).length,boyOz=JSON.stringify(parca[0],(k,v)=>LISTE.has(k)?undefined:v).length;
 console.log('alan',n,'fark',fark.length,'birleştirme ms',ms,'ay sonucu MB',(boy/1e6).toFixed(2),'özet (listesiz) MB',(boyOz/1e6).toFixed(2));
 const g={};for(const f of fark){const k=f.replace(/\[\d+\]/g,'[]').split(' : ')[0].split(' ')[0];g[k]=(g[k]||0)+1}
 Object.entries(g).sort((a,b)=>b[1]-a[1]).slice(0,30).forEach(([k,v])=>console.log(v,k));
 fark.slice(0,8).forEach(f=>console.log('  ',f.slice(0,220)));process.exit(0)},3000);
