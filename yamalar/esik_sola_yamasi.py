"""Sürüm 13.60: Eşik aşımı listelerinde (tüm modüller, Md bileşeni) İSTASYON ve EKİP sütunları sola yaslı."""
import base64, re, sys
p = sys.argv[1]; html = open(p, encoding="utf-8").read()
m = re.search(r'var b="([A-Za-z0-9+/=]+)";var bin=atob\(b\)', html)
js = base64.b64decode(m.group(1)).decode("utf-8")
assert "__esikSol" not in js
def bir(a, b, say=1):
    global js
    assert js.count(a) == say, (js.count(a), a[:90]); js = js.replace(a, b)
# başlıklar
bir('(0,a().jsx)("th",{style:{width:22}}),(0,a().jsx)("th",{children:"\\u0130STASYON"})',
    '(0,a().jsx)("th",{style:{width:22}}),(0,a().jsx)("th",{style:{textAlign:"left"},"data-x":"__esikSol",children:"\\u0130STASYON"})')
bir('(0,a().jsx)("th",{children:"PROTOKOL"}),(0,a().jsx)("th",{children:"EK\\u0130P"}),__iv',
    '(0,a().jsx)("th",{children:"PROTOKOL"}),(0,a().jsx)("th",{style:{textAlign:"left"},children:"EK\\u0130P"}),__iv')
# satırlar
bir('"\\u25b8":""}),(0,a().jsx)("td",{children:e.kisaStasyon||e.istasyon})',
    '"\\u25b8":""}),(0,a().jsx)("td",{style:{textAlign:"left"},children:e.kisaStasyon||e.istasyon})')
bir('"\\u26a0"})]}),(0,a().jsx)("td",{children:e.ekip}),__iv',
    '"\\u26a0"})]}),(0,a().jsx)("td",{style:{textAlign:"left"},children:e.ekip}),__iv')
html = html.replace(m.group(1), base64.b64encode(js.encode("utf-8")).decode("ascii"), 1)
open(p, "w", encoding="utf-8").write(html)
print("eşik sola yaslama yaması uygulandı")
