"""Sürüm 13.62: Modül 4 (İstasyon İstatistik) üstündeki 10 kartlık özet, modülün kendi 'Genel' sekmesindeki
metriklerin tekrarıydı — Modül 2'deki gibi tek satırlık özet cümlesi gösterilir. Kart ızgarası yalnız Modül 1'de kalır."""
import base64, re, sys
p = sys.argv[1]; html = open(p, encoding="utf-8").read()
m = re.search(r'var b="([A-Za-z0-9+/=]+)";var bin=atob\(b\)', html)
js = base64.b64decode(m.group(1)).decode("utf-8")
def bir(a, b, say=1):
    global js
    assert js.count(a) == say, (js.count(a), a[:90]); js = js.replace(a, b)
bir('__hm&&("m2"===te||"m3"===te||"m5"===te)?("m2"===te?(0,a().jsx)(__HarmanM2Cumle,{})',
    '__hm&&("m2"===te||"m3"===te||"m4"===te||"m5"===te)?("m2"===te||"m4"===te?(0,a().jsx)(__HarmanM2Cumle,{})')
html = html.replace(m.group(1), base64.b64encode(js.encode("utf-8")).decode("ascii"), 1)
open(p, "w", encoding="utf-8").write(html)
print("m4 cümle yaması uygulandı")
