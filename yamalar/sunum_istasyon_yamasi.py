"""Sürüm 13.57: Excel İndir › "Sunum ve Özet" (Sunum .pptx, Özet, Brifing Verileri) istasyon sorumlularına gösterilmez.
Host (im112-host.js) oturumdaki kullanıcı istasyona bağlıysa window.__IM112_IST = true yapar."""
import base64, re, sys
p = sys.argv[1]; html = open(p, encoding="utf-8").read()
m = re.search(r'var b="([A-Za-z0-9+/=]+)";var bin=atob\(b\)', html)
js = base64.b64decode(m.group(1)).decode("utf-8")
def bir(a, b):
    global js
    assert js.count(a) == 1, (js.count(a), a[:90]); js = js.replace(a, b)
bir('(0,a().jsx)(ip,{icon:(0,a().jsx)(Qf,{size:22}),title:"Sunum ve \\xd6zet"',
    '!window.__IM112_IST&&(0,a().jsx)(ip,{icon:(0,a().jsx)(Qf,{size:22}),title:"Sunum ve \\xd6zet"')
html = html.replace(m.group(1), base64.b64encode(js.encode("utf-8")).decode("ascii"), 1)
open(p, "w", encoding="utf-8").write(html)
print("sunum istasyon yaması uygulandı")
