"""Sürüm 13.67: Kırsal (ve diğer ulaşım) eşik aşımı yanındaki "Tahmini Varış" sekmesi yalnız Genel Admin ve İl Admini'ne
görünür (/api/im112/durum "yonetici"; tahmini varış denemesi düğmesiyle aynı kural). Diğer kullanıcılarda sekme hiç
hesaplanmaz. Yetki bilgisi açılıştan kısa süre sonra geldiği için "tvs-yon" olayıyla sekme sonradan da açılabilir."""
import base64, re, sys
p = sys.argv[1]; html = open(p, encoding="utf-8").read()
m = re.search(r'var b="([A-Za-z0-9+/=]+)";var bin=atob\(b\)', html)
js = base64.b64decode(m.group(1)).decode("utf-8")
assert "tvs-yon" not in js
def bir(a, b):
    global js
    assert js.count(a) == 1, (js.count(a), a[:90]); js = js.replace(a, b)
bir('K.oturum().then(k=>{window.__tvsYon=!!k&&(k.yonetici===!0||k.rol==="super_admin")})',
    'K.oturum().then(k=>{window.__tvsYon=!!k&&(k.yonetici===!0||k.rol==="super_admin");try{window.dispatchEvent(new Event("tvs-yon"))}catch(e){}})')
bir('const[__tv,__setTv]=(0,s().useState)(null),[__tvH,__setTvH]=(0,s().useState)(!1);(0,s().useEffect)(()=>{if(!__ko||!o||!(o.exceed||[]).length){__setTv(null);return}',
    'const[__tv,__setTv]=(0,s().useState)(null),[__tvH,__setTvH]=(0,s().useState)(!1),[__ty,__setTy]=(0,s().useState)(window.__tvsYon===!0);'
    '(0,s().useEffect)(()=>{const f=()=>__setTy(window.__tvsYon===!0);window.addEventListener("tvs-yon",f);f();return()=>window.removeEventListener("tvs-yon",f)},[]);'
    '(0,s().useEffect)(()=>{if(!__ty||!__ko||!o||!(o.exceed||[]).length){__setTv(null);return}')
bir('window.__tvsHesapla(o.exceed,__ko).then(r=>{__c||__setTv(r)});return()=>{__c=!0}},[o,__ko]);',
    'window.__tvsHesapla(o.exceed,__ko).then(r=>{__c||__setTv(r)});return()=>{__c=!0}},[o,__ko,__ty]);')
html = html[:m.start(1)] + base64.b64encode(js.encode("utf-8")).decode() + html[m.end(1):]
open(p, "w", encoding="utf-8").write(html); print("TVS_YONETICI_OK")
