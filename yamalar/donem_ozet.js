/* ===== Sürüm 12.43 (Aşama 2): çok aylı dönem aylık özetlerden. Her ay için: geçerli özet (yerel → sunucu ?ozet=1);
   yoksa o ayın satırları tek başına hesaplanır (bellekte aynı anda tek ay) ve yetkiliyse özet sunucuya yazılır.
   Sonra __ozetBirlestir. Vaka listeleri bu dönemde boştur (tek ay seçilince gelir). ===== */
const __OZ_ESIK=4;
function __ozGecerli(R,fp,matFp){return!!(R&&1===R.__oz&&R.ashi&&R.ashi.m4&&R.ashi.m5&&fp&&fp===matFp)}
function __ozBosListe(R){const g=["gkg15","gkg16","gkg17","gkg20","hastaneTeslim"];
  const doldur=s=>{if(!s)return;for(const k of["gkg15","gkg16","gkg17","gkg20"])s.m2&&s.m2[k]&&(s.m2[k].exceed=[]);
    for(const m of["m4","m5"]){const x=s[m];if(!x)continue;for(const k of g)x[k]&&(x[k].exceed=[]);x.kapatmaSureDetay=[];x.kapatilmayanVakalar=[];x.vakaKoordinatlari=[];x.icd10&&(x.icd10.girilmeyenVakalar=[]);x.akilliBileklik&&(x.akilliBileklik.takilmayanVakalar=[])}};
  for(const sc of["ashi","diskurum","toplam"])doldur(R[sc]);for(const k of["m1","m2","m3","m4","m5","master"])R.ashi&&(R[k]=R.ashi[k]);return R}
async function __ozDonem(L,ilerleme){
  const st=Ge.getState(),K=window.__IM112_KURUM,H=window.__IM112_HOST,matFp=(0,ze.a8)(st.matrix),S={...st.settings,matrix:st.matrix};
  const il=await K.hedefIl(),k0=await K.oturum(),yaz=!!(K.yetkili&&K.yetkili(k0,il)&&!k0.istasyon);
  const uzak=new Map(((await K.liste(il))||[]).map(f=>[f.ym,f])),parca=[];let cols=null,ah=null,yazilan=0,hesaplanan=0;
  for(let i=0;i<L.length;i++){const ym=L[i],f=uzak.get(ym);let R=null;ilerleme(`${Du(ym)} özeti hazırlanıyor (${i+1}/${L.length})…`);
    try{const r=await(0,ze.tj)(ym);if(r&&__ozGecerli(r.results,r.matrixFingerprint,matFp)&&(!f||r.kurumMod===(f.guncelleme||null)||r.kaynak!=="kurum")){R=r.results;cols=cols||r.cols;ah=ah||r.allHeaders}}catch(e){}
    if(!R&&f)try{const p=await __ORT.paketAc(new Uint8Array(await H.arsiv.indir(il,ym,{ozet:!0})));if(p&&p.ym===ym&&51===p.schema&&__ozGecerli(p.results,p.fp,matFp)){R=p.results;cols=cols||p.cols;ah=ah||p.allHeaders}}catch(e){console.warn("[özet] sunucu özeti alınamadı",ym,e)}
    if(!R){ilerleme(`${Du(ym)} hesaplanıyor (${i+1}/${L.length})…`);let r=await(0,ze.tj)(ym);
      if(!r||!Array.isArray(r.rows)||!r.rows.length){if(!f)throw new Error(Du(ym)+" bu cihazda yok");await K.tamYukle(il,ym);r=await(0,ze.tj)(ym)}
      if(!r||!Array.isArray(r.rows)||!r.rows.length)throw new Error(Du(ym)+": ham veri okunamadı");
      const c=__cT(r.cols,r.allHeaders);await new Promise(x=>setTimeout(x,20));R=Qu(r.rows,c,S);cols=cols||c;ah=ah||r.allHeaders;r=null;hesaplanan++;
      R=__ozKopya(R);if(yaz&&f&&f.paket)try{await H.arsiv.ozetYaz(il,ym,{results:R,fp:matFp,paket:f.paket});yazilan++}catch(e){console.warn("[özet] sunucuya yazılamadı",ym,e)}}
    else R=__ozKopya(R);
    parca.push(R);await new Promise(x=>setTimeout(x,0))}
  ilerleme(`${L.length} ayın özeti birleştiriliyor…`);await new Promise(x=>setTimeout(x,20));
  const M=__ozBosListe(__ozetBirlestir(parca));M.__ozetDonem={aylar:L.slice(),hesaplanan,yazilan};return{results:M,cols,allHeaders:ah}}
window.__ozDonem=__ozDonem;
