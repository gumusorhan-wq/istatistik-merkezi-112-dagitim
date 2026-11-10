"""Sürüm 13.57: Modül 5 › Harita — "Yalnız: …" süzgeç kutusu sol alttaki katman düğmeleriyle (112 İstasyonları, Dış Kurum
Ambulans, hastaneler) üst üste geliyordu; kutu sağ alta, katman düğmelerinin üstüne alındı ve genişliği sınırlandı."""
import base64, re, sys
p = sys.argv[1]; html = open(p, encoding="utf-8").read()
m = re.search(r'var b="([A-Za-z0-9+/=]+)";var bin=atob\(b\)', html)
js = base64.b64decode(m.group(1)).decode("utf-8")
def bir(a, b):
    global js
    assert js.count(a) == 1, (js.count(a), a[:90]); js = js.replace(a, b)
bir('"data-testid":"m5-harita-suzgec",style:{position:"absolute",bottom:24,left:10,zIndex:1e3,',
    '"data-testid":"m5-harita-suzgec",style:{position:"absolute",bottom:48,right:10,maxWidth:"min(520px, calc(100% - 20px))",zIndex:1e3,')
html = html.replace(m.group(1), base64.b64encode(js.encode("utf-8")).decode("ascii"), 1)
open(p, "w", encoding="utf-8").write(html)
print("harita kutu yaması uygulandı")
