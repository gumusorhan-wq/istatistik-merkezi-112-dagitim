"""Sürüm 13.68 (2): İstasyon / Dönem pencereleri dokunmatik cihazlarda (telefon, tablet; yatay dahil) ve alçak ekranda
her zaman alt sayfa olarak açılır. Yatay telefonda pencere düğmenin altında birkaç piksellik yüksekliğe sıkışıyordu."""
import base64, re, sys
p = sys.argv[1]; html = open(p, encoding="utf-8").read()
m = re.search(r'var b="([A-Za-z0-9+/=]+)";var bin=atob\(b\)', html)
js = base64.b64decode(m.group(1)).decode("utf-8")
a = 'const __vw=window.innerWidth,__panelDar=__vw<640;'
b = ('const __vw=window.innerWidth,__panelDar=__vw<640||window.innerHeight<560||!!(window.matchMedia&&'
     'window.matchMedia("(pointer: coarse)").matches);')
assert js.count(a) == 1; js = js.replace(a, b)
html = html[:m.start(1)] + base64.b64encode(js.encode("utf-8")).decode() + html[m.end(1):]
open(p, "w", encoding="utf-8").write(html); print("MOBIL_PANEL2_OK")
