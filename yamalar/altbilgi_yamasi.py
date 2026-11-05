"""Sürüm 12.41: sol alt bilgi — HUSER içinde (kurum sunucusu) "Offline · IndexedDB Arşiv" yerine "Çevrimiçi · Kurum sunucusu"."""
import base64, re, sys
p = sys.argv[1]; html = open(p, encoding="utf-8").read()
m = re.search(r'var b="([A-Za-z0-9+/=]+)";var bin=atob\(b\)', html)
js = base64.b64decode(m.group(1)).decode("utf-8")
a = '"v","1.0.28"," \\xb7 Offline \\xb7 IndexedDB Ar\\u015fiv"]'
assert js.count(a) == 1, js.count(a)
js = js.replace(a, '"v","1.0.28",window.__IM112_HOST?" \\xb7 \\xc7evrimi\\xe7i \\xb7 Kurum sunucusu":" \\xb7 Offline \\xb7 IndexedDB Ar\\u015fiv"]')
html = html[:m.start(1)] + base64.b64encode(js.encode("utf-8")).decode() + html[m.end(1):]
open(p, "w", encoding="utf-8").write(html); print("ALTBILGI_OK")
