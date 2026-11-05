"""Sürüm 1.0.29: Modül 5 seçimleri oturum boyunca kalır.
Özel Değerlendirme (sütun/değer filtresi, eşik filtresi, metrikler, istasyonlar, eklenen aylar, gruplama, ortak vaka),
Modül 5 alt sekmesi, Mahalle & Ekip alt sekmesi ve Özet (sekme, dönem türü, filtre, iç sekmeler) sessionStorage'da
"im112_oturum_v1" altında tutulur: başka modüle / sayfaya geçip dönünce yerinde durur. Yeni girişte stok takip
(AuthContext → modulVerisiniSil) bu anahtarı siler; ilk açılış hep temiz. Özel Değerlendirme'ye 'Değerlendirmeyi temizle'."""
import base64, re, sys
p = sys.argv[1]; html = open(p, encoding="utf-8").read()
m = re.search(r'var b="([A-Za-z0-9+/=]+)";var bin=atob\(b\)', html)
js = base64.b64decode(m.group(1)).decode("utf-8")
assert "__oS" not in js
def bir(a, b, kapsam=None):
    global js
    if kapsam:
        i = js.index(kapsam[0]); j = i + kapsam[1]; seg = js[i:j]
        assert seg.count(a) == 1, (seg.count(a), a[:90]); js = js[:i] + seg.replace(a, b) + js[j:]; return
    assert js.count(a) == 1, (js.count(a), a[:90]); js = js.replace(a, b)

KOD = r'''
window.__OTD=null;
function __otdOku(){if(window.__OTD)return window.__OTD;let o={};try{o=JSON.parse(sessionStorage.getItem("im112_oturum_v1")||"{}")||{}}catch(e){}window.__OTD=o;return o}
function __otdYaz(k,v){const o=__otdOku();o[k]=v instanceof Set?{__set:[...v]}:v;try{sessionStorage.setItem("im112_oturum_v1",JSON.stringify(o))}catch(e){}try{window.dispatchEvent(new CustomEvent("im112-otd",{detail:k}))}catch(e){}}
window.__oS=function(k,ilk){const R=s();const[v,setV]=R.useState(()=>{const o=__otdOku();if(Object.prototype.hasOwnProperty.call(o,k)){const x=o[k];return x&&"object"==typeof x&&Array.isArray(x.__set)?new Set(x.__set):x}return"function"==typeof ilk?ilk():ilk});
  const set=R.useCallback(x=>setV(o=>{const n="function"==typeof x?x(o):x;__otdYaz(k,n);return n}),[]);return[v,set]};
'''
bir('function __MahView(P){', KOD + 'function __MahView(P){')

NH = ('function Nh(){', 59108)
for a, k, b in [('[d,h]=(0,s().useState)(null)', 'oz_d', 'null'), ('[f,p]=(0,s().useState)("")', 'oz_f', '""'),
                ('[__oc,__soc]=(0,s().useState)(!1)', 'oz_oc', '!1'), ('[ee,te]=(0,s().useState)([])', 'oz_ee', '[]'),
                ('[x,S]=(0,s().useState)(null)', 'oz_x', 'null'), ('[M,R]=(0,s().useState)(()=>new Set)', 'oz_M', '()=>new Set'),
                ('[H,K]=(0,s().useState)(()=>new Set)', 'oz_H', '()=>new Set'), ('[Q,J]=(0,s().useState)(()=>new Set)', 'oz_Q', '()=>new Set'),
                ('[re,ne]=(0,s().useState)("istasyon")', 'oz_re', '"istasyon"')]:
    bir(a, a.split('=(0,s()')[0] + f'=window.__oS("{k}",{b})', NH)
# eklenen aylar geri gelince ham verileri yeniden okunur
bir('[V,$]=(0,s().useState)({}),',
    '[V,$]=(0,s().useState)({}),__vyk=(0,s().useEffect)(()=>{for(const t of H){if(t===e||V[t])continue;$(x=>({...x,[t]:"loading"}));(0,ze.tj)(t).then(r=>{if(!r||!r.rows||!r.rows.length)throw new Error("ham veri yok");$(x=>({...x,[t]:{rows:r.rows,cols:r.cols,allHeaders:r.allHeaders||[]}}))}).catch(()=>$(x=>({...x,[t]:"error"})))}},[]),', NH)
bir('return(0,a().jsxs)("div",{"data-testid":"m5-ozel-degerlendirme",style:{display:"flex",gap:16,alignItems:"flex-start",flexWrap:"wrap"},children:[',
    'return(0,a().jsxs)("div",{"data-testid":"m5-ozel-degerlendirme",style:{display:"flex",gap:16,alignItems:"flex-start",flexWrap:"wrap"},children:['
    '(0,a().jsxs)("div",{style:{flexBasis:"100%",display:"flex",justifyContent:"flex-end",alignItems:"center",gap:10,fontSize:11.5,color:"var(--text-muted)"},children:["Seçimleriniz bu oturum boyunca saklanır.",'
    '(0,a().jsx)("button",{type:"button",className:"btn btn-ghost","data-testid":"ozel-hepsini-temizle",style:{fontSize:12,padding:"4px 10px"},'
    'onClick:()=>{window.confirm("Seçili istasyonlar, metrikler, filtreler ve eklenen aylar temizlensin mi?")&&(h(null),p(""),__soc(!1),te([]),S(null),R(new Set),K(new Set),J(new Set),ne("istasyon"))},children:"Değerlendirmeyi temizle"})]}),', NH)

# Modül 5 alt sekmeleri
bir('function Lh(e){var t,r;let{data:n}=e;const[i,o]=(0,s().useState)("performans"),[l,c]=(0,s().useState)("ashi"),[u,d]=(0,s().useState)("mahalle")',
    'function Lh(e){var t,r;let{data:n}=e;const[i,o]=window.__oS("m5_sekme","performans"),[l,c]=(0,s().useState)("ashi"),[u,d]=window.__oS("m5_me","mahalle")')
# Özet
OZ = ('function __OzetView(){', 4000)
bir('[sek,setSek]=R.useState("dikkat")', '[sek,setSek]=window.__oS("ozt_sek","dikkat")', OZ)
bir('[fd,setFd]=R.useState("hepsi")', '[fd,setFd]=window.__oS("ozt_fd","hepsi")', OZ)
bir('[mod,setMod]=R.useState("ay")', '[mod,setMod]=window.__oS("ozt_mod","ay")', OZ)
bir('const[ic,setIc]=R.useState({d:"il",s:"top"})', 'const[ic,setIc]=window.__oS("ozt_ic",{d:"il",s:"top"})', OZ)

html = html[:m.start(1)] + base64.b64encode(js.encode("utf-8")).decode() + html[m.end(1):]
open(p, "w", encoding="utf-8").write(html); print("OTURUM_OK")
