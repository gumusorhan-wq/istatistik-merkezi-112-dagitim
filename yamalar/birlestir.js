/* ===== Sürüm 12.43 (Aşama 2): aylık sonuçları (Qu çıktısı + __ ham alanlar) birleştirir. Vaka listeleri birleşime girmez. ===== */
const __OZ_LISTE=new Set(["exceed","kapatmaSureDetay","kapatilmayanVakalar","girilmeyenVakalar","takilmayanVakalar","vakaKoordinatlari"]);
const __OZ_SABIT=new Set(["threshold","maxScore","scope","detected","noKm","hastaBazli","hasMesguliyetKolonu"]);
const __ozTr=(a,b)=>String(a||"").localeCompare(String(b||""),"tr",{numeric:!0});
const __ozAnahtar={rows:o=>o.ekip!=null&&o.stasyon!=null?"e|"+o.ekip:"i|"+o.istasyon,stationRows:o=>o.istasyon,sefRows:o=>o.sef,perStationList:o=>o.istasyon,kapatmaSureEkip:o=>o.istasyon,istasyonPerformans:o=>o.istasyon,mahalleDagilimi:o=>o.ilce+"||"+o.mahalle,ekipDagilimi:o=>o.ekip+"||"+o.istasyon,mahalleEkipDetay:o=>o.ilce+"||"+o.mahalle+"||"+o.ekip};
function __ozSay(x){return"number"==typeof x&&isFinite(x)}
function __ozTopla(a,b,ad){
  if(a===void 0)return __ozKopya(b);if(b===void 0)return a;
  if(__OZ_SABIT.has(ad))return a;
  if(__ozSay(a)&&__ozSay(b))return a+b;
  if(Array.isArray(a)&&Array.isArray(b)){
    if(ad==="__gun")return[...new Set([...a,...b])];
    if(ad==="__ay"){const m=new Map(a);for(const[k,v]of b)m.set(k,(m.get(k)||0)+v);return[...m]}
    const f=__ozAnahtar[ad];if(f){const m=new Map;for(const o of a)m.set(f(o),o);for(const o of b){const k=f(o);m.set(k,m.has(k)?__ozTopla(m.get(k),o,null):__ozKopya(o))}return[...m.values()]}
    return a}
  if(a&&b&&"object"==typeof a&&"object"==typeof b){for(const k of Object.keys(b)){if(__OZ_LISTE.has(k)){delete a[k];continue}a[k]=__ozTopla(a[k],b[k],k)}return a}
  return a===""||a==null?b:a}
function __ozKopya(x){if(x==null||"object"!=typeof x)return x;const y=JSON.parse(JSON.stringify(x));(function sil(o){if(o&&"object"==typeof o)for(const k of Object.keys(o))__OZ_LISTE.has(k)?delete o[k]:sil(o[k])})(y);return y}
const __ozOran=(p,q)=>q>0?Math.round(p/q*1e3)/10:0;
function __ozGkg(g){if(!g||"object"!=typeof g||!("alti"in g))return;const s=g.maxScore;
  "oran"in g&&(g.oran=__ozOran(g.alti,g.toplam));"puan"in g&&__ozSay(s)&&(g.puan=g.toplam>0?Math.round(g.alti/g.toplam*s*10)/10:0);"ortSn"in g&&(g.ortSn=g.toplam>0?Math.round(g.toplamSn/g.toplam):0);
  for(const r of g.stationRows||[])r.oran=__ozOran(r.alti,r.toplam),r.puan=r.toplam>0?Math.round(r.alti/r.toplam*s*10)/10:0,r.ortSn=r.toplam>0?Math.round(r.__sn/r.toplam):0;
  for(const r of g.sefRows||[])r.oran=__ozOran(r.alti,r.toplam),r.__ist&&(r.istasyon=Se(Object.entries(r.__ist).sort((x,z)=>z[1]-x[1])[0][0],r.__kapsam));
  g.stationRows&&g.stationRows.sort((e,t)=>__ozTr(e.kisaStasyon,t.kisaStasyon))}
function __ozModul(m,kapsam,AY){if(!m)return;
  for(const k of["gkg15","gkg16","gkg17","gkg20","hastaneTeslim"])if(m[k]){for(const r of m[k].sefRows||[])r.__kapsam=kapsam;__ozGkg(m[k]);for(const r of m[k].sefRows||[])delete r.__kapsam}
  const vk=m.vakaKapatma;if(vk){vk.oran=__ozOran(vk.kapali,vk.toplam);for(const r of vk.perStationList||[])r.oran=__ozOran(r.kapali,r.toplam);vk.perStationList&&vk.perStationList.sort((e,t)=>__ozTr(e.istasyon,t.istasyon))}
  for(const r of m.kapatmaSureEkip||[])r.oran24=__ozOran(r.s24,r.toplam),r.oran72=__ozOran(r.s72,r.toplam),r.oranDiger=__ozOran(r.diger,r.toplam);m.kapatmaSureEkip&&m.kapatmaSureEkip.sort((e,t)=>__ozTr(e.istasyon,t.istasyon));
  for(const k of["icd10","akilliBileklik"]){const x=m[k];if(!x)continue;x.oran=__ozOran(x.verilmis,x.toplam);"puan"in x&&(x.puan=x.toplam>0?Math.round(x.verilmis/x.toplam*300*10)/10:0);for(const r of x.perStationList||[])r.oran=__ozOran(r.verilmis,r.toplam);x.perStationList&&x.perStationList.sort((e,t)=>__ozTr(e.istasyon,t.istasyon));
    for(const r of x.sefRows||[])r.__ist&&(r.istasyon=Object.entries(r.__ist).sort((a,b)=>b[1]-a[1])[0][0])}
  if(m.istasyonPerformans){const P=m.istasyonPerformans;AY=AY||new Map((P[0]&&P[0].__ay)||[]);let gs=30,en=null,n=0;for(const[k,x]of AY)x>n&&(en=k,n=x);if(en){const[y,a]=en.split("-").map(Number);gs=new Date(y,a+1,0).getDate()}
    for(const r of P){const o=r.k,go=o.toplam/gs,gp=go>=10?600:go>=6?450:300,i=o.r2?Math.round(o.r1/o.r2*400):0,s=o.h2?Math.round(o.h1/o.h2*300):0,cc=o.i2?Math.round(o.i1/o.i2*300):0,kp=o.toplam>0&&o.kapali===o.toplam?400:0;
      Object.assign(r,{toplamVaka:o.toplam,aktifGunSayisi:gs,gunlukOrt:Math.round(10*go)/10,istReakPuan:i,htPuan:s,gunlukPuan:gp,icdPuan:cc,kapatmaPuan:kp,toplamPuan:i+s+gp+cc+kp,__ay:[...AY]})}
    P.sort((e,t)=>__ozTr(e.kisaStasyon,t.kisaStasyon))}
  m.mahalleDagilimi&&m.mahalleDagilimi.sort((e,t)=>t.sayi-e.sayi||__ozTr(e.ilce,t.ilce)||__ozTr(e.mahalle,t.mahalle));
  m.ekipDagilimi&&m.ekipDagilimi.sort((e,t)=>__ozTr(e.istasyon,t.istasyon)||__ozTr(e.ekip,t.ekip));
  m.mahalleEkipDetay&&m.mahalleEkipDetay.sort((e,t)=>t.sayi-e.sayi||__ozTr(e.ilce,t.ilce)||__ozTr(e.mahalle,t.mahalle)||__ozTr(e.ekip,t.ekip));
  m.konumIstat&&m.konumIstat.__ham&&(m.konumIstat=Object.assign(__kiFin(m.konumIstat.__ham),{__ham:m.konumIstat.__ham}))}
function __ozM1(m1){if(!m1)return;for(const r of m1.rows||[])r.reaksiyonOrani=__ozOran(r.reaksiyon,r.reaksiyonToplam);(m1.rows||[]).sort((e,t)=>__ozTr(e.kisaStasyon,t.kisaStasyon));
  const T={toplam:0,il_ici:0,il_disi:0,km:0,kentsel:0,kirsal:0,reaksiyon:0};for(const r of m1.rows||[])for(const k in T)T[k]+=r[k]||0;T.km=Math.round(10*T.km)/10;m1.totals=T}
function __ozMaster(s){const g=(o,k)=>o&&o[k]||{},a=(o,...k)=>Object.fromEntries(k.map(x=>[x,(o&&o[x])||0])),m4=s.m4||{},m3=s.m3||{};
  return{genelToplam:g(m3,"genel").toplam||0,toplamVaka:g(s.m1,"totals").toplam||0,hizmetVerilen:g(m3,"gkg09").toplam||0,kkm:a(m4.gkg15,"toplam","ustu","alti","oran"),istasyon:a(m4.gkg16,"toplam","ustu","alti","oran"),kentsel:a(m4.gkg17,"toplam","ustu","alti","oran"),kirsal:a(m4.gkg20,"toplam","ustu","alti","oran"),
    hastaneTeslim:a(m4.hastaneTeslim,"toplam","alti","ustu","oran","ortSn"),vakaKapatma:a(m4.vakaKapatma,"toplam","kapali","acik","oran"),icd10:a(m4.icd10,"toplam","verilmis","eksik","oran"),akilliBileklik:a(m4.akilliBileklik,"toplam","verilmis","eksik","oran")}}
function __ozIstDeg(D){if(!D)return;for(const o of D.rows||[]){const e=(o.__gun||[]).length||1,a=Math.round(10*o.__km)/10;Object.assign(o,{gunlukOrtVaka:Math.round(10*o.toplamVaka/e)/10,gunlukOrtNakil:Math.round(10*o.hstArasi/e)/10,gunlukOrtMesg:Math.round(o.__mesg/e),vakaBasinaMesg:o.toplamVaka>0?Math.round(o.__mesg/o.toplamVaka):0,toplamKm:a,gunlukOrtKm:Math.round(10*a/e)/10,vakaBasinaKm:o.toplamVaka>0?Math.round(10*a/o.toplamVaka)/10:0,aktifGunSayisi:(o.__gun||[]).length})}
  (D.rows||[]).sort((e,t)=>__ozTr(e.kisaStasyon,t.kisaStasyon))}
function __ozAy(L,sc,k){const m=new Map;for(const x of L){const P=x&&x[sc]&&x[sc][k]&&x[sc][k].istasyonPerformans;for(const[a,v]of(P&&P[0]&&P[0].__ay)||[])m.set(a,(m.get(a)||0)+v)}return m}
function __ozetBirlestir(L){if(!L||!L.length)return null;let R=__ozKopya(L[0]);for(let i=1;i<L.length;i++)R=__ozTopla(R,L[i],null);
  for(const sc of["ashi","diskurum","toplam"]){const s=R[sc];if(!s)continue;__ozM1(s.m1);for(const k of["m2","m3","m4","m5"])s[k]&&(k==="m2"?["gkg15","gkg16","gkg17","gkg20"].forEach(x=>__ozGkg(s.m2[x])):__ozModul(s[k],sc,__ozAy(L,sc,k)));s.master=__ozMaster(s);s.sks&&(s.sks.v=L[0][sc]&&L[0][sc].sks?L[0][sc].sks.v:1);__ozIstDeg(R.istasyonDegerlendirme&&R.istasyonDegerlendirme[sc])}
  for(const k of["m1","m2","m3","m4","m5","master"])R.ashi&&(R[k]=R.ashi[k]);R.__il=null;return R}
window.__ozetBirlestir=__ozetBirlestir;
