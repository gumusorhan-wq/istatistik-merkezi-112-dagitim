"""Sürüm 12.37: yükleme ekranındaki açıklama kartları sisteme uygun (kurum arşivi sunucuda, cihazdaki kopya çıkışta silinir)."""
import base64, re, sys
p = sys.argv[1]; html = open(p, encoding="utf-8").read()
m = re.search(r'var b="([A-Za-z0-9+/=]+)";var bin=atob\(b\)', html)
js = base64.b64decode(m.group(1)).decode("utf-8")
def kac(t): return ''.join(c if ord(c) < 128 else '\\u%04x' % ord(c) for c in t)
def bir(a, b):
    global js
    a = kac(a)
    assert js.count(a) == 1, (js.count(a), a[:90]); js = js.replace(a, b)
bir(r'title:"Yerel Arşiv",text:"Yıl filtresi · Aylar arası karşılaştırma"',
    'title:"Kurum Arşivi",text:"Aylar sunucuda · Yetkili yükler, herkes yetkisi kadarını görür"')
bir(r'title:"Yedek ve Gizlilik",text:"Otomatik yedek · Veri cihazda kalır"',
    'title:"Yedek ve Gizlilik",text:"Sunucuda yedeklenir · Cihazdaki kopya çıkışta silinir"')
bir(r'title:"5 Modül Paralel",text:"Tek yüklemede 5 modül analizi"',
    'title:"5 Modül Birlikte",text:"Tek yüklemede 5 modülün analizi"')
# Modül başlığında 📅/🚑 seçici gizliyken (Modül 5) "⬇ Sayfa Excel" sola kaymasın: araya esneyen boşluk
bir('(0,a().jsx)(window.__DonemSec,{}),(0,a().jsx)("button",{type:"button",className:"btn btn-ghost","data-testid":"sayfa-excel"',
    '(0,a().jsx)("span",{style:{flex:"1 1 auto"}}),(0,a().jsx)(window.__DonemSec,{}),(0,a().jsx)("button",{type:"button",className:"btn btn-ghost","data-testid":"sayfa-excel"')
html = html[:m.start(1)] + base64.b64encode(js.encode("utf-8")).decode() + html[m.end(1):]
open(p, "w", encoding="utf-8").write(html); print("KART_OK")
