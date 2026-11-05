"""Sürüm 12.40: Hastaneler arası nakil sayımı tüm ekranlarda aynı kurala bağlanır (karar: her nakil ayrı sayılır).
Özel Değerlendirme aynı protokol+ekip+istasyon tekrarını tek vaka sayar; hastaneler arası nakil tekrarları (hasta ikinci
bir hastaneye taşındıysa) yalnız sevk sütunlarında sayılıyordu. Artık Sonuç sütununda da sayılır; böylece
"Sonuç = Nakil - Hastaneler Arası" sayısı İstasyon Değerlendirme'deki "Hst-arası Nakil" ile aynı çıkar."""
import base64, re, sys
p = sys.argv[1]; html = open(p, encoding="utf-8").read()
m = re.search(r'var b="([A-Za-z0-9+/=]+)";var bin=atob\(b\)', html)
js = base64.b64decode(m.group(1)).decode("utf-8")
assert "__NAKIL_HER" not in js
def bir(a, b):
    global js
    assert js.count(a) == 1, (js.count(a), a[:90]); js = js.replace(a, b)
bir('__sc=new Set([t.sevkIl,t.sevkEdilenHastane,t.sevkEdenHastane,"__AH","__AHK"].filter(Boolean))',
    '__sc=new Set([t.sevkIl,t.sevkEdilenHastane,t.sevkEdenHastane,t.sonuc,"__AH","__AHK"].filter(Boolean)),__NAKIL_HER=1')
html = html[:m.start(1)] + base64.b64encode(js.encode("utf-8")).decode() + html[m.end(1):]
open(p, "w", encoding="utf-8").write(html); print("NAKIL_OK")
