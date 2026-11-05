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
  const M=__ozListeBagla(__ozBosListe(__ozetBirlestir(parca)),il,L);M.__ozetDonem={aylar:L.slice(),hesaplanan,yazilan};return{results:M,cols,allHeaders:ah}}
window.__ozDonem=__ozDonem;
/* Modül 2 "önceki ay": önceki ay bu cihazda yoksa (ya da cihazdaki daha eskiyse) sunucudaki ay özetinden alınır (Sürüm 12.43) */
const __OZ_ONC=new Map;
async function __ozOncUzak(K){const KK=window.__IM112_KURUM;if(!KK||!KK.aktif())return null;const k=await KK.oturum();if(!k||k.istasyon)return null;
  const il=await KK.hedefIl(),L=((await KK.liste(il))||[]).map(f=>f.ym).filter(y=>y<K).sort();return L.length?{il,ym:L[L.length-1]}:null}
async function __ozOncOzet(il,ym,Y){const key=il+"|"+ym;let p=__OZ_ONC.get(key);
  if(!p){p=(async()=>{const u8=new Uint8Array(await window.__IM112_HOST.arsiv.indir(il,ym,{ozet:!0})),q=await __ORT.paketAc(u8);return q&&q.ym===ym&&q.results?{fp:q.fp,results:q.results}:null})().catch(e=>{console.warn("[özet] önceki ay alınamadı",ym,e);return null});__OZ_ONC.set(key,p)}
  const o=await p;if(!o||o.fp!==(0,ze.a8)(Ge.getState().matrix))return null;const T=o.results[Y]||o.results;return T&&T.master&&T.m2?T:null}
/* Özet dönemde vaka listeleri istek üzerine: liste alanı okununca (ekran açılınca) seçili ayların o listesi sunucudan iner,
   birleşik sonuca yazılır ve ekran yenilenir. Okunmayan liste hiç inmez. */
let __OZL_BEKLE=0;
function __ozlBildir(){try{let b=document.getElementById("__ozlBant");if(__OZL_BEKLE>0){if(!b){b=document.createElement("div");b.id="__ozlBant";b.setAttribute("data-testid","ozet-liste-yukleniyor");b.style.cssText="position:fixed;right:16px;bottom:16px;z-index:4000;background:#0f2a44;color:#fff;padding:8px 14px;border-radius:8px;font:600 12.5px system-ui,sans-serif;box-shadow:0 6px 20px rgba(0,0,0,.3)";document.body.appendChild(b)}b.textContent="⏳ Vaka listesi seçili aylar için sunucudan alınıyor…"}else b&&b.remove()}catch(e){}}
function __ozlSirala(ad,L,yol){if(ad==="exceed"&&!/\.m2\./.test(yol)&&L.length&&L[0]&&"kisaStasyon"in L[0])return L.slice().sort((e,t)=>String(e.kisaStasyon||"").localeCompare(String(t.kisaStasyon||""),"tr",{numeric:!0}));
  if(ad==="girilmeyenVakalar"||ad==="takilmayanVakalar")return L.slice().sort((e,t)=>(t.vakaTarihi||"").localeCompare(e.vakaTarihi||""));
  if(ad==="kapatilmayanVakalar"){const n=Date.now();return L.map(x=>{const b=x.baslangic?Date.parse(x.baslangic):NaN;return isNaN(b)?x:{...x,acikSaat:Math.round(10*(n-b)/36e5)/10}}).sort((e,t)=>t.acikSaat-e.acikSaat)}return L}
function __ozListeBagla(R,il,L){const ICI=new Map;let CUR=R;
  const tanim=(o,ad,yol)=>{if(!o||"object"!=typeof o)return;let deger=[];
    Object.defineProperty(o,ad,{configurable:!0,enumerable:!1,get(){if(!ICI.has(yol)&&window.__OZ_LISTE!==!1&&window.__IM112_HOST){ICI.set(yol,1);__OZL_BEKLE++;__ozlBildir();
        (async()=>{const T=[];for(const ym of L){try{const x=await window.__IM112_HOST.arsiv.liste(il,ym,yol);Array.isArray(x)&&T.push(...x)}catch(e){console.warn("[özet] liste alınamadı",ym,yol,e)}}
          deger=__ozlSirala(ad,T,yol);Object.defineProperty(o,ad,{configurable:!0,enumerable:!0,writable:!0,value:deger});
          try{const st=Ge.getState();if(st.results===CUR){CUR={...CUR};Ge.setState({results:CUR})}}catch(e){}})().finally(()=>{__OZL_BEKLE--;__ozlBildir()})}
      return deger},set(v){Object.defineProperty(o,ad,{configurable:!0,enumerable:!0,writable:!0,value:v})}})};
  for(const sc of["ashi","diskurum","toplam"]){const s=R[sc];if(!s)continue;
    for(const k of["gkg15","gkg16","gkg17","gkg20"])s.m2&&tanim(s.m2[k],"exceed",`${sc}.m2.${k}.exceed`);
    for(const m of["m4","m5"]){const x=s[m];if(!x)continue;for(const k of["gkg15","gkg16","gkg17","gkg20","hastaneTeslim"])tanim(x[k],"exceed",`${sc}.${m}.${k}.exceed`);
      for(const k of["kapatmaSureDetay","kapatilmayanVakalar","vakaKoordinatlari"])tanim(x,k,`${sc}.${m}.${k}`);
      tanim(x.icd10,"girilmeyenVakalar",`${sc}.${m}.icd10.girilmeyenVakalar`);tanim(x.akilliBileklik,"takilmayanVakalar",`${sc}.${m}.akilliBileklik.takilmayanVakalar`)}}
  return R}
window.__ozSonuc=()=>Ge.getState().results;
