"""Branş önerisi (İl Dışı / İl İçi Sevk): KKM ya da istasyon açıklamasında branşın adı açıkça geçiyorsa (ör. "beyin cerrahi dr…",
"ortopedi kabul etti") bu, belirti kelimelerinden (kırık, hematom…) 5 kat ağır sayılır. Beyin Cerrahi'ye "beyin cer" kısaltması ve
omurga kırığı ifadeleri eklendi (boyun kırığı, odontoid, vertebra, omurga, spinal, medulla, servikal, kompresyon kırığı, parapleji…).
Kayıtlı kurallarda Beyin Cerrahi eski varsayılan haldeyse yenisine güncellenir; elle değiştirilmiş kurallara dokunulmaz."""
import base64, re, sys
p = sys.argv[1]; html = open(p, encoding="utf-8").read()
m = re.search(r'var b="([A-Za-z0-9+/=]+)";var bin=atob\(b\)', html)
js = base64.b64decode(m.group(1)).decode("utf-8")
assert "__BR_ACIK" not in js
def bir(a, b):
    global js
    assert js.count(a) == 1, (js.count(a), a[:90]); js = js.replace(a, b)
ESKI = "beyin cerrahi, beyincerrahi, beyin sinir, subaraknoid, sak, hematom, anevriz, hidrosefali, sant tak, intrakranial, subdural, epidural, kafa travma"
YENI = "beyin cerrahi, beyincerrahi, beyin cer, beyin sinir, norosirurji, subaraknoid, sak, hematom, anevriz, hidrosefali, sant tak, intrakranial, subdural, epidural, kafa travma, boyun kirigi, odontoid, dens kirigi, vertebra, omurga, spinal, medulla, servikal, kompresyon kirigi, parapleji, kuadripleji, tetrapleji"
bir('["Beyin Cerrahi","' + ESKI + '","hepsi",10,0]', '["Beyin Cerrahi","' + YENI + '","hepsi",10,0]')
bir('const OLDY={', 'const __BR_ACIK=5,OLD2={"Beyin Cerrahi":["' + ESKI + '"]};const OLDY={')
bir('null!=OLD1[e.ad]&&String(e.anahtar||"")===OLD1[e.ad]&&(n={...n,anahtar:d.anahtar});',
    'null!=OLD1[e.ad]&&String(e.anahtar||"")===OLD1[e.ad]&&(n={...n,anahtar:d.anahtar});OLD2[e.ad]&&OLD2[e.ad].includes(String(n.anahtar||""))&&(n={...n,anahtar:d.anahtar});')
bir('let n=0;const yer=[];for(const[e,t]of SR){const m=t.match(re);m&&(n+=m.length,yer.push(KAY[e]))}n&&(hit+=n,hw.push(src?k:k+" ("+yer.join("+")+")"))',
    'let n=0;const yer=[],__ac=!src&&!any&&!r.kesin&&k.length>=3&&fold(r.ad).startsWith(k);for(const[e,t]of SR){const m=t.match(re);m&&(n+=m.length*(__ac&&("kkm"===e||"istac"===e)?__BR_ACIK:1),yer.push(KAY[e]))}n&&(hit+=n,hw.push(src?k:k+" ("+yer.join("+")+(__ac&&yer.some(x=>"KKM"===x||"İst. açıklama"===x)?", branş adı":"")+")"))')
# "takipli" anahtar kelimesiyle (alan değil) tutan Takipli Hasta kuralı, açıklamada adı geçen branşı ezmesin
bir('let best=null,why=[];const R=K.slice()', 'let best=null,why=[],__kes=null;const R=K.slice()')
bir('let hit=0,hw=[];if(!src&&r.alan&&h.ham)', 'let hit=0,hw=[],__acv=!1;if(!src&&r.alan&&h.ham)')
bir('(n+=m.length*(__ac&&("kkm"===e||"istac"===e)?__BR_ACIK:1),yer.push(KAY[e]))}', '(n+=m.length*(__ac&&("kkm"===e||"istac"===e)?(__acv=!0,__BR_ACIK):1),yer.push(KAY[e]))}')
bir('if(r.kesin)return{ad:hedef,neden:hw};const sc=10*hit-(r.oncelik||0);(!best||sc>best.sc)&&(best={sc,ad:hedef,neden:hw})}',
    'if(r.kesin){if(!src&&/takipli/i.test(fold(r.ad))&&!hw.some(x=>/ = /.test(String(x)))){__kes||(__kes={ad:hedef,neden:hw});continue}return{ad:hedef,neden:hw}}const sc=10*hit-(r.oncelik||0);(!best||sc>best.sc)&&(best={sc,ad:hedef,neden:hw,ac:__acv})}'
    'if(__kes){if(best&&best.ac)return{ad:best.ad,neden:best.neden.concat(["takipli olduğu bölüm açıklamada adı geçen branş"])};return __kes}')

# --- 12.35: Dahiliye ve Travma branşları; il dışı sevkte takipli + aynı hastane → Takipli Hasta ---
bir('["DSA iht.","dsa","hepsi",3,1]', '["Dahiliye","dahiliye, ic hastaliklari, hiperglisemi, hipoglisemi, diyabet, diabet, diyabetik, ketoasidoz, hipertansiyon, kan basinci, kan basincinin yuksek, hiperkalemi, hipokalemi, hiponatremi, elektrolit","eriskin",13,0],["DSA iht.","dsa","hepsi",3,1]')
bir('["I20-I25,I30-I52,I10-I15,R00-R01,R07,R55","Kardiyoloji"]', '["I10-I15,R03,E00-E90,R73","Dahiliye"],["I20-I25,I30-I52,R00-R01,R07,R55","Kardiyoloji"]')
bir('const ICDB2=[["W00-W19,V01-V99","Ortopedi"]', 'const ICDB2=[["W50-W52,Y04,Z04.1,Z04.3","Travma"],["W50-W52,Y04,Z04.1,Z04.3","Beyin Cerrahi"],["W00-W19,V01-V99","Ortopedi"]')
# yeni varsayılan branşlar kayıtlı listeye bir kez eklenir (kullanıcı silerse geri gelmez)
bir('return r.list.map(e=>{const d=DEF.find(t=>t.ad===e.ad);if(!d)return e;', 'const __yeni=(r.ekV||0)<1?DEF.filter(d=>["Dahiliye","Travma"].includes(d.ad)&&!r.list.some(e=>e.ad===d.ad)).map(e=>({...e})):[];return r.list.concat(__yeni).map(e=>{const d=DEF.find(t=>t.ad===e.ad);if(!d)return e;')
bir('await kput({id:"branslar",list,tarih:(new Date).toISOString()})', 'await kput({id:"branslar",list,ekV:1,tarih:(new Date).toISOString()})')
# il içi / il dışı bilgisi
bir('out.push({key:b+"|"+n,protokol:p,', 'out.push({key:b+"|"+n,mod:"ic"===mod?"ic":"dis",protokol:p,')
# takipli + takip edildiği hastaneye sevk (il dışı) → Takipli Hasta
bir('if(__kes){if(best&&best.ac)', 'if(__kes&&"ic"!==h.mod&&__ayniHst(h))return{ad:__kes.ad,neden:__kes.neden.concat(["takipli olduğu hastaneye sevk"])};if(__kes){if(best&&best.ac)')
bir('function oner(h,K,src){', 'const __HGEN=new Set("t c tc saglik bakanligi egitim ve arastirma hastanesi hastane hast devlet universitesi universite univ sehir ozel tip fakultesi il ilce merkezi merkez acil dr prof izmir manisa ankara istanbul aydin denizli usak balikesir bursa kutahya afyon afyonkarahisar mugla antalya eskisehir konya".split(" "));\nfunction __ayniHst(h){const T0=" "+fold([h.kkm,h.istac].join(" "))+" ",T=(T0.match(/.{0,70}takipli.{0,10}/g)||[]).join(" | "),tk=fold(h.edilen||"").split(/[^a-z0-9]+/).filter(t=>t.length>=3&&!__HGEN.has(t));return tk.some(t=>new RegExp("(?<![a-z0-9])"+esc(t)+"(?![a-z0-9])").test(T))}\nfunction oner(h,K,src){')
# --- 12.35b: açıklamada bağlam — branş adı sevk/ihtiyaç/kabul bağlamında ×5, gönderen taraf/ret/'X:' görüşü sayılmaz; eş anlamlılar; travma + baş → Beyin Cerrahi
bir('function oner(h,K,src){', r"""const __SYN={"Erişkin Yoğun Bakım":["yb","ybu","yogun bakim","yogunbakim"],"Çocuk Yoğun Bakım":["cocuk yb","cocuk yogun"],"Hematoloji":["hematoloji","hemotoloji"],"Göğüs Hastalıkları":["gogus hastaliklari","gogus hast","gogus uzm","gogus hekim","gogus servis"],"Beyin Cerrahi":["beyin cer","beyin cerrahi","norosirurji"],"Dahiliye":["dahiliye","ic hastaliklari"],"Kardiyoloji":["kardiyoloji"],"Nöroloji":["noroloji"],"Ortopedi":["ortopedi"],"Genel Cerrahi":["genel cerrahi"],"Üroloji":["uroloji"],"Gastroenteroloji":["gastroenteroloji"],"Nefroloji":["nefroloji"]};
const __EK={"Göğüs Hastalıkları":["akciger odem","pulmoner odem","pnomoni","pnemoni","plevral efuzyon","astim atak"],"Hematoloji":["hematolojik","kan temin"]};
function __edenYakin(b,h){const tk=fold(h.eden||"").split(/[^a-z0-9]+/).filter(t=>t.length>=4&&!__HGEN.has(t));return tk.some(t=>new RegExp("(?<![a-z0-9])"+esc(t)+"(?![a-z0-9])[^a-z0-9]*([a-z]+[^a-z0-9]*){0,1}$").test(b))}
function __baglam(t,i,L,h){const a=t.slice(i+L,i+L+45),b=t.slice(Math.max(0,i-24),i);
  if(/^[a-z]{0,4}\s*:/.test(a)||/(bizlik|bizim degil|kabul etme|kabul etmi|kabul etmiyor|(^|[^a-z])ret([^a-z]|$)|reddet|istemedi|yok dedi|ulasilamadi|uygun degil|gerek yok|(^|[^a-z])dolu)/.test(a.slice(0,30))||/^[a-z]{0,6}\s*servis[a-z]*\s*([^\s]+\s*){0,2}(yat|alin)/.test(a)||/(kendi|hastanemiz[a-z]*|bizde)\s*$/.test(b)||__edenYakin(b,h))return-1;
  if(/(sevk|uygun|ihtiyac|(^|[^a-z])iht|kabul etti|kabul edildi|kabul ediyor|teyit|gidecek|yatis|bekleniyor)/.test(a)||/(olan (bir )?yerde|olan hastaneye|uzm(an)? hekim[a-z]*|ihtiyaci olan)\s*$/.test(b))return 1;return 0}
function __travmaBas(h){const T=" "+fold([h.kkm,h.istac,h.tani].join(" "))+" ";return/(trafik kaza|kaza sonra|darp|dusme|yuksekten|travma|motosiklet)/.test(T)&&/(bas agri|bas travma|kafa|bilinc|tomografi|beyin bt|kranial)/.test(T)}
function oner(h,K,src){""")
bir('const ks=String(r.anahtar||"").split(",").map(e=>fold(e).trim()).filter(Boolean);', 'const ks=[...new Set(String(r.anahtar||"").split(",").concat(src?[]:(__SYN[r.ad]||[]),src?[]:(__EK[r.ad]||[])).map(e=>fold(e).trim()).filter(Boolean))];')
bir('let hit=0,hw=[],__acv=!1;', 'let hit=0,hw=[],__acv=!1;!src&&"Beyin Cerrahi"===r.ad&&__travmaBas(h)&&(hit+=3,hw.push("travma + baş ağrısı/tomografi"));')
bir('let n=0;const yer=[],__ac=!src&&!any&&!r.kesin&&k.length>=3&&fold(r.ad).startsWith(k);for(const[e,t]of SR){const m=t.match(re);m&&(n+=m.length*(__ac&&("kkm"===e||"istac"===e)?(__acv=!0,__BR_ACIK):1),yer.push(KAY[e]))}',
    'let n=0;const yer=[],__ac=!src&&!any&&!r.kesin&&(k.length>=3&&fold(r.ad).startsWith(k)||(__SYN[r.ad]||[]).map(fold).includes(k));for(const[e,t]of SR){let w=0,c=0;if(!src&&("kkm"===e||"istac"===e)){re.lastIndex=0;let mm;while(mm=re.exec(t)){c++;const g=__baglam(t,mm.index,mm[0].length,h);g<0||(g>0&&__ac?(w+=/yogun bakim/.test(fold(r.ad))?3*__BR_ACIK:__BR_ACIK,__acv=!0):w+=1)}}else{const m=t.match(re);m&&(c=m.length,w=m.length)}c&&w&&(n+=w,yer.push(KAY[e]))}')
bir('return best?{ad:best.ad,neden:best.neden}:{ad:"",neden:[]}}', 'return best?{ad:best.ad,neden:best.neden,ac:best.ac}:{ad:"",neden:[]}}')
bir('return{ad:best.ad,neden:best.neden.concat(["takipli olduğu bölüm açıklamada adı geçen branş"])}', 'return{ad:best.ad,ac:!0,neden:best.neden.concat(["takipli olduğu bölüm açıklamada adı geçen branş"])}')
bir('const ky=kaynak(h,K);if(base.ad&&!ky.uyumsuz)return base;', 'if(base.ad&&base.ac)return base;const ky=kaynak(h,K);if(base.ad&&!ky.uyumsuz)return base;')

# --- 12.35c: Dahiliye ve Travma yalnız il içi sevkte; il dışında listede de görünmez
bir('["Ücretli Hasta","ucretli","hepsi",1,1]', '["Travma","darp, muayene ve gozlem","hepsi",14,0],["Ücretli Hasta","ucretli","hepsi",1,1]')
bir('function oner(h,K,src){', 'const __SADECE_IC=["Dahiliye","Travma"];\nfunction oner(h,K,src){')
bir('for(const r of R){if("cocuk"===r.yas&&!ck)continue;', 'for(const r of R){if(__SADECE_IC.includes(r.ad)&&"ic"!==h.mod)continue;if("cocuk"===r.yas&&!ck)continue;')
bir('let e=K.find(t=>t.ad===ad);if(!e)continue;', 'let e=K.find(t=>t.ad===ad);if(!e)continue;if(__SADECE_IC.includes(ad)&&"ic"!==h.mod)continue;')
bir('__BR.kurallar().then(t=>{e&&o(t)})', '__BR.kurallar().then(t=>{e&&o("ic"===__md?t:t.filter(x=>!["Dahiliye","Travma"].includes(x.ad)))})')
bir('const ad=K.map(k=>k.ad);for(const b of Object.keys(BRA))', 'const ad=K.filter(k=>!["Dahiliye","Travma"].includes(k.ad)).map(k=>k.ad);for(const b of Object.keys(BRA))')
html = html[:m.start(1)] + base64.b64encode(js.encode("utf-8")).decode() + html[m.end(1):]
open(p, "w", encoding="utf-8").write(html); print("BRANS_OK")
