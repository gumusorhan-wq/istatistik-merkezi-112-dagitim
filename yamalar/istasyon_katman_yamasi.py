"""Sürüm 13.57: Modül 5 › Harita — "112 İstasyonları" katmanındaki istasyon işaretleri paket içindeki sabit listeden
geliyordu; Yönetim › İstasyonlar'da girilen konum (window.__ikBul) varsa işaret o noktaya çizilir. Aynı kural rota
hesabındaki istasyon listesine (__tvsIstasyonlar) de uygulanır."""
import base64, re, sys
p = sys.argv[1]; html = open(p, encoding="utf-8").read()
m = re.search(r'var b="([A-Za-z0-9+/=]+)";var bin=atob\(b\)', html)
js = base64.b64decode(m.group(1)).decode("utf-8")
assert "__ikKatman" in js or "__ikBul" in js
assert "__ikKatman" not in js
def bir(a, b):
    global js
    assert js.count(a) == 1, (js.count(a), a[:90]); js = js.replace(a, b)
YARDIMCI = r'''window.__ikKatman=function(L){try{if(!window.__ikBul)return L;return L.map(s=>{if("İASB İstasyon"!==s.tur)return s;const o=window.__ikBul(s.aciklama)||window.__ikBul(s.ad);return o?Object.assign({},s,{lat:o.lat,lon:o.lon}):s})}catch(e){return L}};
'''
js = YARDIMCI + js
bir('const t=(window.__IL&&!window.__IL.manisaMi()?[]:rh).filter(',
    'const t=(window.__IL&&!window.__IL.manisaMi()?[]:window.__ikKatman(rh)).filter(')
bir('for(const s of rh)if("İASB İstasyon"===s.tur){M.set(__tvsAnah(s.ad),s)}',
    'for(const s of window.__ikKatman(rh))if("İASB İstasyon"===s.tur){M.set(__tvsAnah(s.ad),s)}')
html = html.replace(m.group(1), base64.b64encode(js.encode("utf-8")).decode("ascii"), 1)
open(p, "w", encoding="utf-8").write(html)
print("istasyon katman yaması uygulandı")
