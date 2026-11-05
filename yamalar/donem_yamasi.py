"""Sürüm 1.0.29 (stok takip 12.33): bütün modüllerde çoklu ay / yıl seçimi.
Modül sekmelerinin sağındaki "Dönem" düğmesi: yıl ya da tek tek aylar seçilir. Tek ay seçilirse o ay açılır;
birden çok ay seçilirse seçilen ayların ham satırları birleştirilip bütün modüller (Kontrol Paneli, Modül 1–5,
Araç, Tahmini Varış …) bu birleşik veriyle yeniden hesaplanır. Cihazda olmayan kurum ayları sunucudan indirilir.
Sütun düzeni farklı aylar başlık adına göre eşlenir. Özet / Sunum / Mahalle gibi kendi ay seçimi olan ekranlar
birleşik sonucu "son ay" sanmasın diye ayKapsam ve Mahalle yaması dönemde arşivdeki aya bakar."""
import base64, re, sys
p = sys.argv[1]; html = open(p, encoding="utf-8").read()
m = re.search(r'var b="([A-Za-z0-9+/=]+)";var bin=atob\(b\)', html)
js = base64.b64decode(m.group(1)).decode("utf-8")
assert "__DonemSec" not in js
def bir(a, b):
    global js
    assert js.count(a) == 1, (js.count(a), a[:90]); js = js.replace(a, b)

KOD = r'''
window.__DONEM=null;
window.__donemAktif=function(){const D=window.__DONEM;return D&&D.rows&&Ge.getState().parsedRows===D.rows?D:null};
function __dnAyK(ym){const A=["Oca","Şub","Mar","Nis","May","Haz","Tem","Ağu","Eyl","Eki","Kas","Ara"],p=String(ym||"").split("-");return p.length<2?String(ym||""):A[+p[1]-1]+" "+p[0]}
function __dnEtiket(L){if(!L||!L.length)return"";if(L.length===1)return Du(L[0]);const s=[...L].sort(),y=[...new Set(s.map(x=>x.slice(0,4)))];
  if(y.length===1&&s.length===12)return y[0]+" yılı (12 ay)";
  let ard=!0;for(let i=1;i<s.length;i++){const[a,b]=s[i-1].split("-").map(Number),[c,d]=s[i].split("-").map(Number);if(c*12+d!==a*12+b+1){ard=!1;break}}
  return ard?`${__dnAyK(s[0])} – ${__dnAyK(s[s.length-1])} (${s.length} ay)`:`${s.length} ay: ${s.map(__dnAyK).join(", ")}`}
function __dnBirlestir(recs){
  const b=recs[0],bc=__cT(b.cols,b.allHeaders)||{},bh=b.allHeaders||[],imza=r=>JSON.stringify(__cT(r.cols,r.allHeaders)||{})+"|"+JSON.stringify((r.allHeaders||[]).map(h=>h.letter+"="+h.baslik));
  const bi=imza(b),harf=new Set([...bh.map(h=>h.letter),...Object.values(bc).filter(Boolean)]),byT=new Map(bh.map(h=>[String(h.baslik).trim(),h.letter])),out=[];
  for(const r of recs){if(r===b||imza(r)===bi){for(const x of r.rows)out.push(x);continue}
    const c=__cT(r.cols,r.allHeaders)||{},M=[],kul=new Set();
    for(const k of Object.keys(bc))bc[k]&&c[k]&&!kul.has(bc[k])&&(M.push([c[k],bc[k]]),kul.add(bc[k]));
    for(const h of r.allHeaders||[]){const t=byT.get(String(h.baslik).trim());t&&!kul.has(t)&&(M.push([h.letter,t]),kul.add(t))}
    const bos=[...harf].filter(x=>!kul.has(x));
    for(const x of r.rows){const o={};for(const[f,t]of M)o[t]=x[f];for(const t of bos)o[t]="";out.push(o)}}
  return{rows:out,cols:bc,allHeaders:bh}}
async function __dnAyAl(ym,yerel,il,ilerleme){
  const K=window.__IM112_KURUM;
  if(!yerel.has(ym)){if(!K||!K.aktif()||!il)throw new Error(Du(ym)+" bu cihazda yok");ilerleme(Du(ym)+" sunucudan indiriliyor…");await K.tamYukle(il,ym)}
  const r=await(0,ze.tj)(ym);if(!r||!Array.isArray(r.rows)||!r.rows.length)throw new Error(Du(ym)+": ham veri okunamadı");return r}
const __DN_ONB=new Map;window.__DN_MOD={};window.__DN_TABAN=null;window.__DN_AKTIF_K=null;window.__DN_YAZIYOR=!1;
function __ozMod(){try{if(__HMS.te!=="m5")return!1;const o="function"==typeof __otdOku?__otdOku():{};return"ozet"===o.m5_sekme}catch(e){return!1}}
const __M5_KENDI=["istasyonbazli","ozeldegerlendirme","bransdeg","bransic","arackm","ozet"];
function __m5Kendi(){try{if(__HMS.te!=="m5")return!1;const o="function"==typeof __otdOku?__otdOku():{};return __M5_KENDI.includes(o.m5_sekme||"performans")}catch(e){return!1}}
function __useOtd(){const R=s(),[,f]=R.useState(0);R.useEffect(()=>{const g=()=>f(x=>x+1);window.addEventListener("im112-otd",g);return()=>window.removeEventListener("im112-otd",g)},[])}
function __dnK(L,ist){return L.join(",")+"|"+(ist||[]).join("¦")}
function __dnTabanAl(){const st=Ge.getState();if(window.__DN_TABAN)return window.__DN_TABAN;if(window.__DONEM||!st.results||!st.currentMonth)return null;
  const T={D:null,results:st.results,cm:st.currentMonth,file:st.currentFile,cols:st.cols,rows:st.parsedRows||[],kaynak:st.parsedRows||[],allHeaders:st.allHeaders,aylar:[st.currentMonth],ist:[],ham:st.results};
  window.__DN_TABAN=T;window.__DN_AKTIF_K=__dnK(T.aylar,[]);return T}
/* başka yoldan (arşivden ay açma, yeni dosya, açılış) ay değişince: o ay taban olur, modüllerin kendi seçimleri sıfırlanır */
try{Ge.subscribe((s,o)=>{if(window.__DN_YAZIYOR||!o||s.parsedRows===o.parsedRows&&s.results===o.results)return;window.__DONEM=null;window.__DN_TABAN=null;window.__DN_MOD={};__DN_ONB.clear();__dnTabanAl()})}catch(e){console.warn("[dönem] store izlenemedi",e)}
function __dnYaz(P){window.__DN_YAZIYOR=!0;try{window.__DONEM=P.D;window.__DN_AKTIF_K=__dnK(P.aylar,P.ist);Ge.getState().setResults({results:P.results,currentMonth:P.cm,currentFile:P.file,cols:P.cols,rawRowCount:P.rows.length,parsedRows:P.rows,allHeaders:P.allHeaders,fromArchive:!0,processing:!1,processError:null})}finally{window.__DN_YAZIYOR=!1}}
async function __donemHesapla(L,ist,ilerleme){
  const st=Ge.getState(),T=__dnTabanAl(),K=window.__IM112_KURUM,S={...st.settings,matrix:st.matrix},k=__dnK(L,ist);
  if(T&&k===__dnK(T.aylar,[]))return T;
  if(__DN_ONB.has(k))return __DN_ONB.get(k);
  let B=null,R1=null,dosya=null;const ayK=L.join(",");
  const es=[T,...__DN_ONB.values()].find(P=>P&&P.aylar.join(",")===ayK&&P.kaynak);
  if(es)B={rows:es.kaynak,cols:es.cols,allHeaders:es.allHeaders},R1=es.ham||null,dosya=es.dosyaHam||es.file||null;
  else{const il=K&&K.aktif()?await K.hedefIl():null,yerel=new Set((st.archivedMonths||[]).map(x=>x&&x.ym).filter(Boolean)),recs=[];
    for(let i=0;i<L.length;i++){ilerleme(`${Du(L[i])} hazırlanıyor (${i+1}/${L.length})…`);recs.push(await __dnAyAl(L[i],yerel,il,ilerleme))}
    try{window.__DN_YAZIYOR=!0;st.setArchivedMonths(await(0,ze.yZ)())}catch(e){}finally{window.__DN_YAZIYOR=!1}
    if(L.length===1){const r=recs[0],c=__cT(r.cols,r.allHeaders);B={rows:r.rows,cols:c,allHeaders:r.allHeaders||null};R1=r.results&&51===r.schemaVersion&&r.matrixFingerprint===(0,ze.a8)(st.matrix)?r.results:null;dosya={name:r.fileName||"arşiv",size:r.fileSize||0}}
    else{ilerleme(`${L.length} ay birleştiriliyor…`);await new Promise(r=>setTimeout(r,30));B=__dnBirlestir(recs)}}
  const ic=B.cols&&B.cols.istasyon,IS=new Set(ist),rows=ist.length&&ic?B.rows.filter(x=>IS.has(String(x[ic]==null?"":x[ic]).trim())):B.rows;
  if(ist.length&&!rows.length)throw new Error("Seçilen istasyonlarda bu dönemde vaka yok");
  let R;if(!ist.length&&R1)R=R1;else{ilerleme(`${rows.length.toLocaleString("tr-TR")} vaka hesaplanıyor…`);await new Promise(r=>setTimeout(r,30));R=Qu(rows,B.cols,S)}
  const ham=ist.length?R1:R;
  let P;
  if(L.length===1&&!ist.length)P={D:null,results:R,cm:L[0],file:dosya||{name:"arşiv",size:0},cols:B.cols,rows,kaynak:B.rows,allHeaders:B.allHeaders,aylar:L,ist,ham,dosyaHam:dosya};
  else{const de=__dnEtiket(L),ie=ist.length?(ist.length===1?ist[0]:ist.length+" istasyon"):"",et=de+(ie?" · "+ie:"");
    const D={aylar:L,ist,rows,kaynak:B.rows,cols:B.cols,allHeaders:B.allHeaders,donemEtiket:de,istEtiket:ie,etiket:et};
    P={D,results:R,cm:L[L.length-1],file:{name:(L.length>1?"Seçili dönem: ":"")+et,size:0},cols:B.cols,rows,kaynak:B.rows,allHeaders:B.allHeaders,aylar:L,ist,ham,dosyaHam:dosya}}
  __DN_ONB.set(k,P);while(__DN_ONB.size>4)__DN_ONB.delete(__DN_ONB.keys().next().value);
  return P}
async function __donemUygula(L,ist,ilerleme,mod){
  L=[...new Set(L)].sort();ist=[...new Set(ist||[])].sort();if(!L.length)return;
  mod=mod||__HMS.te;
  const P=await __donemHesapla(L,ist,ilerleme),T=__dnTabanAl();
  if(__HMS.te!==mod){window.__DN_MOD[mod]=T&&P===T?null:{aylar:L,ist};return}
  __dnYaz(P);window.__DN_MOD[mod]=T&&P===T?null:{aylar:L,ist}}
function __DonemSec(){
  __useOtd();__useHMS();
  const R=s(),J=a(),E=(t,p,...c)=>{const ch=c.flat(9).filter(x=>x!==null&&x!==false&&x!==void 0&&x!=="");return ch.length>1?(0,J.jsxs)(t,{...(p||{}),children:ch}):(0,J.jsx)(t,{...(p||{}),children:ch[0]})};
  const cm=Ge(e=>e.currentMonth),pr=Ge(e=>e.parsedRows),cols=Ge(e=>e.cols),arsiv=Ge(e=>e.archivedMonths)||[],sc=Ge(e=>e.activeScope)||"ashi",kapsamda=v=>{try{return xe(v,sc)}catch(e){return!0}};
  const[ac,setAc]=R.useState(null),[sec,setSec]=R.useState([]),[isec,setIsec]=R.useState([]),[iq,setIq]=R.useState(""),[uzak,setUzak]=R.useState([]),[dur,setDur]=R.useState(""),[hata,setHata]=R.useState(null),[,setTik]=R.useState(0);const ref=R.useRef(null),kRef=R.useRef(()=>{});
  const D=window.__donemAktif(),aylarSimdi=D?D.aylar:cm?[cm]:[],istSimdi=__ozMod()?(window.__OZ_IST||[]):D?D.ist:[],ozM=__ozMod(),ozUygula=I=>{window.__OZ_IST=[...I].sort();try{window.dispatchEvent(new Event("im112-oz-ist"))}catch(e){}setAc(null)};
  R.useEffect(()=>{if(!ac)return;const f=e=>{ref.current&&!ref.current.contains(e.target)&&!dur&&kRef.current()},k=e=>{e.key==="Escape"&&!dur&&kRef.current()},y=()=>setTik(t=>t+1);document.addEventListener("mousedown",f);document.addEventListener("keydown",k);window.addEventListener("resize",y);window.addEventListener("scroll",y,!0);return()=>{document.removeEventListener("mousedown",f);document.removeEventListener("keydown",k);window.removeEventListener("resize",y);window.removeEventListener("scroll",y,!0)}},[ac,dur]);
  R.useEffect(()=>{if(!ac)return;setSec([...aylarSimdi]);setIsec([...istSimdi]);setIq("");setHata(null);if(ac!=="ay")return;const K=window.__IM112_KURUM;if(!K||!K.aktif())return;let c=!0;(async()=>{try{const il=await K.hedefIl(),L=await K.liste(il);c&&setUzak(L.map(f=>f.ym))}catch(e){}})();return()=>{c=!1}},[ac]);
  const istler=R.useMemo(()=>{const rows=D?D.kaynak:pr,c=(D?D.cols:cols)||{},k=c.istasyon;if(!rows||!k)return[];const m=new Map;for(const x of rows){const v=String(x[k]==null?"":x[k]).trim();v&&m.set(v,(m.get(v)||0)+1)}return[...m.entries()].sort((a,b)=>a[0].localeCompare(b[0],"tr",{numeric:!0}))},[pr,cols]);
  const yerel=new Set(arsiv.map(x=>x&&x.ym).filter(Boolean)),tum=[...new Set([...yerel,...uzak,cm].filter(x=>x&&/^\d{4}-\d{2}$/.test(x)))].sort(),yillar=[...new Set(tum.map(y=>y.slice(0,4)))].sort().reverse(),S=new Set(sec),IS=new Set(isec);
  const AYK=["Oca","Şub","Mar","Nis","May","Haz","Tem","Ağu","Eyl","Eki","Kas","Ara"];
  const uygula=async(L,I)=>{if(!L.length)return;setHata(null);try{await __donemUygula(L,I,setDur,__HMS.te);setDur("");setAc(null)}catch(e){setDur("");setHata(String(e&&e.message||e))}};
  const ayTik=ym=>{setSec(S.has(ym)?sec.filter(x=>x!==ym):[...sec,ym].sort())};
  const yilTik=y=>{const Y=tum.filter(x=>x.slice(0,4)===y);const hep=Y.every(x=>S.has(x));setSec(hep?sec.filter(x=>x.slice(0,4)!==y):[...new Set([...sec,...Y])].sort())};
  const indir=sec.filter(x=>!yerel.has(x)).length,ayDeg=sec.length>0&&[...sec].sort().join()!==aylarSimdi.join(),istDeg=[...isec].sort().join("¦")!==[...istSimdi].sort().join("¦");const kapat=()=>{if(dur)return;ac==="ay"&&ayDeg?uygula(sec,istSimdi):ac==="ist"&&istDeg?(ozM?ozUygula(isec):uygula(aylarSimdi,isec)):setAc(null)};kRef.current=kapat;const ust=(baslik,tid,yazi,aktif,on,tem)=>E("div",{style:{position:"sticky",top:-12,zIndex:2,margin:"-12px -12px 10px",padding:"10px 12px",display:"flex",gap:8,alignItems:"center",background:"var(--bg-elevated, #fff)",borderBottom:"1px solid var(--border-subtle, rgba(148,163,184,.3))"}},E("b",{style:{fontSize:12.5,flex:1,color:"var(--text-primary)"}},baslik),E("button",{type:"button",className:"btn btn-ghost",disabled:!!dur,onClick:tem,style:{fontSize:12,padding:"5px 9px"}},"Temizle"),E("button",{type:"button",className:"btn btn-primary","data-testid":tid,disabled:!aktif||!!dur,onClick:on,style:{fontSize:12.5,padding:"6px 14px"}},yazi));
  const chip=(on,dis)=>({fontSize:12,padding:"4px 0",width:44,borderRadius:6,cursor:dis?"default":"pointer",border:"1px solid "+(on?"var(--turquoise, #17a2a8)":"var(--border-subtle, rgba(148,163,184,.35))"),background:on?"var(--turquoise, #17a2a8)":"transparent",color:on?"#fff":dis?"var(--text-muted)":"var(--text-primary)",opacity:dis?.35:1,fontWeight:on?700:500});
  const rc=ref.current?ref.current.getBoundingClientRect():null,panel=(id,w,...c)=>E("div",{"data-testid":id,style:{position:"fixed",top:rc?Math.round(rc.bottom+6):80,right:rc?Math.max(8,Math.round(window.innerWidth-rc.right)):16,maxHeight:"calc(100vh - "+(rc?Math.round(rc.bottom+20):100)+"px)",overflowY:"auto",zIndex:2000,width:w,padding:12,borderRadius:12,background:"var(--bg-elevated, #0f2a44)",border:"1px solid var(--border-subtle)",boxShadow:"0 12px 30px rgba(0,0,0,.25)"}},...c);
  const durum=dur?E("div",{"data-testid":"donem-durum",style:{fontSize:12,marginTop:8,color:"var(--turquoise-glow, #17a2a8)"}},"⏳ ",dur):null,hataK=hata?E("div",{style:{fontSize:12,marginTop:8,color:"#dc2626"}},hata):null;
  const ayEt=D?D.donemEtiket:cm?Du(cm):"Ay seçilmedi",isEt=ozM?(istSimdi.length?(istSimdi.length===1?istSimdi[0]:istSimdi.length+" istasyon"):({ashi:"Tüm ASHİ istasyonları",diskurum:"Tüm dış kurum ekipleri"}[sc]||"Tüm istasyonlar")):D&&D.istEtiket?D.istEtiket:({ashi:"Tüm ASHİ istasyonları",diskurum:"Tüm dış kurum ekipleri"}[sc]||"Tüm istasyonlar");
  const iK=istler.filter(([v])=>kapsamda(v)||IS.has(v)),iL=iK.filter(([v])=>!iq||v.toLocaleLowerCase("tr").includes(iq.toLocaleLowerCase("tr"))),tumEt={ashi:"Tüm ASHİ istasyonları",diskurum:"Tüm dış kurum ekipleri"}[sc]||"Tüm istasyonlar";const ilceAd=v=>{try{return fh(v)||"Diğer"}catch(e){return"Diğer"}},IG=(()=>{const m=new Map;for(const[v]of iK){const k=ilceAd(v);m.has(k)||m.set(k,[]);m.get(k).push(v)}return[...m.entries()].sort((a,b)=>a[0]==="Diğer"?1:b[0]==="Diğer"?-1:a[0].localeCompare(b[0],"tr"))})(),IGg=IG.filter(([k,L])=>!iq||k.toLocaleLowerCase("tr").includes(iq.toLocaleLowerCase("tr"))||L.some(v=>v.toLocaleLowerCase("tr").includes(iq.toLocaleLowerCase("tr")))),ilceTik=L=>{const hep=L.every(v=>IS.has(v));setIsec(hep?isec.filter(x=>!L.includes(x)):[...new Set([...isec,...L])])};
  if(__m5Kendi()&&!ozM)return null;
  return E("div",{ref:ref,style:{position:"relative",display:"inline-flex",gap:6,marginLeft:"auto",flexShrink:0}},
    istler.filter(([v])=>kapsamda(v)).length>1||istSimdi.length?E("button",{type:"button",className:"tab "+(istSimdi.length||ac==="ist"?"active":""),onClick:()=>!dur&&(ac==="ist"?kapat():ac?(kapat(),setAc("ist")):setAc("ist")),"data-testid":"istasyon-sec",title:"Bütün modülleri seçilen istasyonlarla hesapla",style:{whiteSpace:"nowrap",maxWidth:260,overflow:"hidden",textOverflow:"ellipsis"}},"🚑 ",isEt,ac==="ist"?" ▴":" ▾"):null,
    ozM?null:E("button",{type:"button",className:"tab "+(D&&D.aylar.length>1||ac==="ay"?"active":""),onClick:()=>!dur&&(ac==="ay"?kapat():ac?(kapat(),setAc("ay")):setAc("ay")),"data-testid":"donem-sec",title:"Ay ya da yıl seçin",style:{whiteSpace:"nowrap"}},"📅 ",ayEt,ac==="ay"?" ▴":" ▾"),
    ac==="ay"&&panel("donem-panel",360,
      ust(sec.length?`${sec.length} ay seçili`:"Ay seçin","donem-uygula","Hesapla",ayDeg,()=>uygula(sec,istSimdi),()=>setSec([])),E("div",{style:{fontSize:11.5,color:"var(--text-muted)",lineHeight:1.5,marginBottom:10}},"Koyu olan aylar seçilidir. Aya tıklayarak ekleyip çıkarın; yıla tıklayınca o yılın bütün ayları. Paneli kapatınca da hesaplanır.",indir>0?` ${indir} ay sunucudan inecek.`:""),yillar.length?yillar.map(y=>E("div",{key:y,style:{marginBottom:10}},
        E("button",{type:"button","data-testid":"donem-yil-"+y,onClick:()=>yilTik(y),disabled:!!dur,title:"Yılın bütün aylarını seç / çıkar",style:{fontSize:12.5,fontWeight:800,background:"none",border:"none",padding:"0 0 4px",cursor:"pointer",color:"var(--text-primary)",textDecoration:"underline dotted"}},y," ",E("span",{style:{fontWeight:500,color:"var(--text-muted)"}},`(${tum.filter(x=>x.slice(0,4)===y).length} ay)`)),
        E("div",{style:{display:"grid",gridTemplateColumns:"repeat(6, 44px)",gap:5}},AYK.map((k,i)=>{const ym=y+"-"+String(i+1).padStart(2,"0"),var_=tum.includes(ym),on=S.has(ym);return E("button",{key:ym,type:"button","data-testid":"donem-ay-"+ym,disabled:!var_||!!dur,onClick:()=>ayTik(ym),title:var_?(yerel.has(ym)?Du(ym):Du(ym)+" — sunucudan indirilecek"):Du(ym)+" — veri yok",style:chip(on,!var_)},k,var_&&!yerel.has(ym)?"↓":"")}))
      )):E("div",{style:{fontSize:12,color:"var(--text-muted)"}},"Arşivde ay yok."),
      durum,hataK),
    ac==="ist"&&panel("istasyon-panel",340,
      ust(isec.length?`${isec.length} istasyon seçili`:tumEt,"istasyon-uygula","Hesapla",istDeg,()=>ozM?ozUygula(isec):uygula(aylarSimdi,isec),()=>setIsec([])),
      E("input",{type:"text",className:"input","data-testid":"istasyon-ara",placeholder:"İlçe ya da istasyon ara…",value:iq,onChange:e=>setIq(e.target.value),style:{width:"100%",boxSizing:"border-box",fontSize:12.5,padding:"6px 8px",marginBottom:8}}),
      IG.length>1&&E("div",{"data-testid":"ilce-secim",style:{display:"flex",flexWrap:"wrap",gap:5,marginBottom:8,maxHeight:150,overflowY:"auto"}},IGg.map(([k,L])=>{const on=L.every(v=>IS.has(v)),kis=!on&&L.some(v=>IS.has(v));return E("button",{key:k,type:"button","data-testid":"ilce-"+k,onClick:()=>ilceTik(L),title:on?k+" istasyonlarını çıkar":k+" istasyonlarının hepsini seç",style:{fontSize:12,padding:"4px 9px",borderRadius:6,cursor:"pointer",fontWeight:600,border:"1px solid "+(on||kis?"var(--turquoise, #17a2a8)":"var(--border-subtle, rgba(148,163,184,.35))"),background:on?"var(--turquoise, #17a2a8)":kis?"rgba(23,162,168,.12)":"transparent",color:on?"#fff":"var(--text-primary)"}},`${k} (${L.length})`)})),E("div",{style:{display:"flex",gap:8,marginBottom:6}},E("button",{type:"button",className:"btn btn-ghost",style:{fontSize:11.5,padding:"3px 8px"},onClick:()=>setIsec([...new Set([...isec,...iL.map(x=>x[0])])])},"Görünenleri seç"),E("span",{style:{marginLeft:"auto",fontSize:11.5,color:"var(--text-muted)",alignSelf:"center"}},isec.length?isec.length+" seçili":"hepsi")),
      E("div",{style:{maxHeight:300,overflowY:"auto",border:"1px solid var(--border-subtle, rgba(148,163,184,.3))",borderRadius:8,padding:4}},iL.length?iL.map(([v,n])=>E("label",{key:v,"data-testid":"istasyon-secenek",style:{display:"flex",alignItems:"center",gap:8,padding:"4px 6px",fontSize:12.5,cursor:"pointer",borderRadius:6,background:IS.has(v)?"rgba(23,162,168,.10)":"transparent",color:"var(--text-primary)"}},E("input",{type:"checkbox",checked:IS.has(v),onChange:()=>setIsec(IS.has(v)?isec.filter(x=>x!==v):[...isec,v]),style:{accentColor:"#17a2a8"}}),E("span",{style:{flex:1,opacity:kapsamda(v)?1:.5}},v,kapsamda(v)?"":" (bu kapsamda değil)"),E("span",{style:{fontSize:11,color:"var(--text-muted)"}},n))):E("div",{style:{fontSize:12,color:"var(--text-muted)",padding:6}},"Eşleşen istasyon yok.")),
      E("div",{style:{fontSize:11.5,color:"var(--text-muted)",marginTop:8}},ozM?"Özet, kendi dönem seçimiyle (Son Ay / Son 3 Ay / Ay Seç) bu istasyonlar için hesaplanır. Paneli kapatınca da uygulanır.":["Seçili dönem: ",ayEt," · Paneli kapatınca da hesaplanır."]),
      durum,hataK))}
function __DonemBant(){
  Ge(e=>e.parsedRows);__useOtd();const mod=__useHMS().te,kendi=__m5Kendi(),R=s(),[dur,setDur]=R.useState("");
  R.useEffect(()=>{const T=__dnTabanAl();if(!T)return;const h=kendi?null:window.__DN_MOD[mod],L=h?h.aylar:T.aylar,I=h?h.ist:[];if(window.__DN_AKTIF_K===__dnK(L,I))return;let c=!0;
    (async()=>{try{setDur("Bu modülün seçimi hazırlanıyor…");const P=await __donemHesapla(L,I,m=>c&&setDur(m));if(c&&__HMS.te===mod)__dnYaz(P)}catch(e){console.warn("[dönem]",e);delete window.__DN_MOD[mod];c&&__dnYaz(T)}finally{c&&setDur("")}})();return()=>{c=!1}},[mod,kendi]);
  const D=window.__donemAktif();let ad="bu modül";try{const m=Ph.find(e=>e.id===mod);m&&(ad=m.label)}catch(e){}
  if(dur)return(0,a().jsx)("div",{"data-testid":"donem-bant-yukleniyor",style:{margin:"0 0 12px",padding:"8px 12px",borderRadius:10,fontSize:12.5,background:"rgba(23,162,168,0.08)",border:"1px solid rgba(23,162,168,0.35)",color:"var(--text-secondary)"},children:"⏳ "+dur});
  if(!D||kendi)return null;
  return(0,a().jsxs)("div",{"data-testid":"donem-bant",style:{margin:"0 0 12px",padding:"8px 12px",borderRadius:10,fontSize:12.5,lineHeight:1.6,background:"rgba(23,162,168,0.08)",border:"1px solid rgba(23,162,168,0.35)",color:"var(--text-secondary)"},children:[(0,a().jsx)("b",{children:(D.aylar.length>1?"Seçili dönem: ":"")+D.etiket}),` · ${D.rows.length.toLocaleString("tr-TR")} satır · bu seçim yalnız ${ad} için geçerli; diğer modüller kendi seçimleriyle açılır.`+(D.aylar.length>1?` Bazı tablo başlıklarında ve dosya adlarında dönemin son ayı (${Du(D.aylar[D.aylar.length-1])}) yazabilir.`:"")]})}
window.__DonemSec=__DonemSec;window.__DonemBant=__DonemBant;
'''
bir('function __MahView(P){', KOD + 'function __MahView(P){')

# modül sekmeleri: Dönem seçici (sağda) + bilgi bandı
bir('(0,a().jsxs)("div",{className:"tabs","data-testid":"module-tabs",style:{alignItems:"center"},children:[',
    '(0,a().jsx)(window.__DonemBant,{}),(0,a().jsxs)("div",{className:"tabs","data-testid":"module-tabs",style:{alignItems:"center"},children:[')
bir('(0,a().jsx)("button",{type:"button",className:"btn btn-ghost","data-testid":"sayfa-excel",title:"Yalnızca şu an ekranda açık olan sayfadaki tabloları Excel’e aktarır",style:{marginLeft:"auto",',
    '(0,a().jsx)(window.__DonemSec,{}),(0,a().jsx)("button",{type:"button",className:"btn btn-ghost","data-testid":"sayfa-excel",title:"Yalnızca şu an ekranda açık olan sayfadaki tabloları Excel’e aktarır",style:{marginLeft:8,')

# kendi ay seçimi olan ekranlar dönemde birleşik sonucu "son ay" saymasın
bir('("h1",{children:Du(K)})', '("h1",{children:window.__donemAktif()?window.__DONEM.etiket:Du(K)})')
bir('async function ayKapsam(ym,scope,cur,kok){\n  let R;\n  if(cur&&cur.ym===ym&&cur.results)R=cur.results;',
    'const __OZK=new Map;\nasync function ayKapsam(ym,scope,cur,kok){\n  let R;const __I=cur&&Array.isArray(cur.ist)&&cur.ist.length?cur.ist:null;\n  if(__I){const ck=ym+"|"+__I.join("¦");if(!__OZK.has(ck)){const rec=await(0,ze.tj)(ym);if(!rec||!Array.isArray(rec.rows)||!rec.rows.length)throw new Error(Du(ym)+" arşiv kaydı okunamadı");const st=Ge.getState(),c=__cT(rec.cols,rec.allHeaders),ic=c&&c.istasyon,IS=new Set(__I),rows=ic?rec.rows.filter(x=>IS.has(String(x[ic]==null?"":x[ic]).trim())):rec.rows;__OZK.size>24&&__OZK.delete(__OZK.keys().next().value);__OZK.set(ck,Qu(rows,c,{...st.settings,matrix:st.matrix}))}R=__OZK.get(ck)}\n  else if(cur&&cur.ym===ym&&cur.results&&!window.__donemAktif())R=cur.results;')
# Özet görünümü: istasyon süzgeci
bir('const sira=R.useRef(0);\n  const yuk=()=>{', 'const[ozIst,setOzIst]=R.useState(()=>window.__OZ_IST||[]);R.useEffect(()=>{const f=()=>setOzIst(window.__OZ_IST||[]);window.addEventListener("im112-oz-ist",f);return()=>window.removeEventListener("im112-oz-ist",f)},[]);\n  const sira=R.useRef(0);\n  const yuk=()=>{')
bir('__SUNUM.ozetHesap({ym:cm,scope:sc,results},', '__SUNUM.ozetHesap({ym:cm,scope:sc,results,ist:ozIst},')
bir('R.useEffect(()=>{yuk()},[cm,sc,results,arsiv.length,mod,secim.join("|"),mod==="ozel"?ozelAy.join("|"):""]);', 'R.useEffect(()=>{yuk()},[cm,sc,results,arsiv.length,mod,secim.join("|"),mod==="ozel"?ozelAy.join("|"):"",ozIst.join("|")]);')
bir('let T;if(ym===cm)T=(results&&', 'let T;if(ym===cm&&!window.__donemAktif())T=(results&&')
bir('if(cur&&cur.ym===ym&&st.parsedRows&&st.allHeaders){rows=st.parsedRows;H=st.allHeaders}',
    'if(cur&&cur.ym===ym&&st.parsedRows&&st.allHeaders&&!window.__donemAktif()){rows=st.parsedRows;H=st.allHeaders}')


# Mahalle & Ekip: kendi ay seçicisi kaldırıldı, üstteki dönem/istasyon seçimiyle çalışır
bir('const sec=aylar.filter(x=>tumAy.includes(x)),coklu=sec.length>0;', 'const sec=[],coklu=!1;')
bir('tab("harita","Harita"),picker),', 'tab("harita","Harita")),')
bir(':(cm?Du(cm):"");\n  const toplam=veri.mahalleDagilimi', ':(window.__donemAktif()?window.__DONEM.etiket:cm?Du(cm):"");\n  const toplam=veri.mahalleDagilimi')
html = html[:m.start(1)] + base64.b64encode(js.encode("utf-8")).decode() + html[m.end(1):]
open(p, "w", encoding="utf-8").write(html); print("DONEM_OK")
