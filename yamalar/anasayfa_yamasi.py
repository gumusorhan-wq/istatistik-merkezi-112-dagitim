"""Sürüm 13.23: yan menüde 'Kontrol Paneli' → 'Ana Sayfa' (bütün modüllerde ilk öğe Ana Sayfa). ortak_dil_yamasi.py'den SONRA."""
import base64, re, sys
p = sys.argv[1]; html = open(p, encoding="utf-8").read()
m = re.search(r'var b="([A-Za-z0-9+/=]+)";var bin=atob\(b\)', html)
js = base64.b64decode(m.group(1)).decode("utf-8")
a = '{id:"dashboard",label:"Kontrol Paneli",icon:re,testId:"nav-dashboard"'
assert js.count(a) == 1
js = js.replace(a, '{id:"dashboard",label:"Ana Sayfa",icon:re,testId:"nav-dashboard"')
html = html[:m.start(1)] + base64.b64encode(js.encode("utf-8")).decode("ascii") + html[m.end(1):]
open(p, "w", encoding="utf-8").write(html)
print("anasayfa_yamasi: Kontrol Paneli → Ana Sayfa")
