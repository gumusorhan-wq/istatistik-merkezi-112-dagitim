"""Sürüm 12.43 (Aşama 2, 2. adım): 4 ve daha çok aylık dönem (istasyon süzgeçsiz, kurum arşivi) aylık özetlerden birleştirilir
(donem_ozet.js). İstasyon süzgeçli dönemde her ay inerken seçilen istasyonlara süzülür (bellekte tüm ayların satırları tutulmaz).
Özet dönemde istasyon seçici listesi sonuçtan gelir. Modül 2 "önceki ay" cihazda yoksa sunucudaki ay özetinden alınır. ozet_yamasi.py'den SONRA uygulanır."""
import base64, re, sys, os
p = sys.argv[1]; html = open(p, encoding="utf-8").read()
m = re.search(r'var b="([A-Za-z0-9+/=]+)";var bin=atob\(b\)', html)
js = base64.b64decode(m.group(1)).decode("utf-8")
assert "__ozetBirlestir" in js and "__ozDonem" not in js
def bir(a, b, n=1):
    global js
    assert js.count(a) == n, (js.count(a), a[:90]); js = js.replace(a, b)
FN = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'donem_ozet.js'), encoding='utf-8').read()
bir('async function __donemHesapla(L,ist,ilerleme){', FN + '\nasync function __donemHesapla(L,ist,ilerleme){')
bir('if(__DN_ONB.has(k))return __DN_ONB.get(k);',
    'if(__DN_ONB.has(k))return __DN_ONB.get(k);'
    'if(L.length>=__OZ_ESIK&&!ist.length&&K&&K.aktif()&&!window.__OZ_KAPALI){const Z=await __ozDonem(L,ilerleme),de=__dnEtiket(L),__bos=[],'
    '__il=(((Z.results.istasyonDegerlendirme||{}).toplam||{}).rows||[]).map(x=>[x.istasyon,x.toplamVaka]).sort((a,b)=>a[0].localeCompare(b[0],"tr",{numeric:!0})),'
    'D={aylar:L,ist,rows:__bos,kaynak:null,istListe:__il,cols:Z.cols,allHeaders:Z.allHeaders,donemEtiket:de,istEtiket:"",etiket:de,ozet:!0},'
    'P={D,results:Z.results,cm:L[L.length-1],file:{name:"Seçili dönem: "+de+" (aylık özetlerden)",size:0},cols:Z.cols,rows:__bos,kaynak:null,allHeaders:Z.allHeaders,aylar:L,ist,ham:Z.results,dosyaHam:null,ozet:!0,ozetSatir:Z.satir};'
    '__DN_ONB.set(k,P);while(__DN_ONB.size>4)__DN_ONB.delete(__DN_ONB.keys().next().value);return P}let __onSuz=!1;')
bir('recs.push(await __dnAyAl(L[i],yerel,il,ilerleme))}',
    '{const r=await __dnAyAl(L[i],yerel,il,ilerleme);if(ist.length&&L.length>1){const c=__cT(r.cols,r.allHeaders),ic=c&&c.istasyon,IS=new Set(ist);ic&&(r.rows=r.rows.filter(x=>IS.has(String(x[ic]==null?"":x[ic]).trim())),__onSuz=!0)}recs.push(r)}}')
bir('__DN_ONB.set(k,P);const __enCok=', '__onSuz&&(P.kaynak=null,P.D&&(P.D.kaynak=null,P.D.istListe=null));__DN_ONB.set(k,P);const __enCok=')
bir('const istler=R.useMemo(()=>{const rows=D?D.kaynak:pr,c=(D?D.cols:cols)||{},k=c.istasyon;if(!rows||!k)return[];',
    'const istler=R.useMemo(()=>{if(D&&!D.kaynak&&D.istListe)return D.istListe;const rows=D?D.kaynak:pr,c=(D?D.cols:cols)||{},k=c.istasyon;if(!rows||!k)return[];')
bir('const p=(async()=>{try{const L=(await(0,ze.yZ)()).map(e=>e.ym).filter(y=>y<K).sort(),pr=L[L.length-1];if(!pr)return null;',
    'const p=(async()=>{try{const L=(await(0,ze.yZ)()).map(e=>e.ym).filter(y=>y<K).sort(),pr=L[L.length-1];'
    'try{const uz=await __ozOncUzak(K);if(uz&&(!pr||uz.ym>pr)){const T=await __ozOncOzet(uz.il,uz.ym,Y);if(T)return{ym:uz.ym,T}}}catch(e){}if(!pr)return null;')
bir('rawRowCount:P.rows.length,parsedRows:P.rows,', 'rawRowCount:P.ozetSatir||P.rows.length,parsedRows:P.rows,')
html = html[:m.start(1)] + base64.b64encode(js.encode("utf-8")).decode() + html[m.end(1):]
open(p, "w", encoding="utf-8").write(html); print("DONEM_OZET_OK")
