"""Sürüm 12.41: haritada rota yönü ambulansın gidiş yönü. Vaka ile istasyon arasında rota istenince başlangıç hangisi
seçilmiş olursa olsun istasyon → vaka çizilir (tek yönlü yollar doğru yönde); kutuda "⇄ Yönü çevir" ile tersi görülebilir.
Google Haritalar bağlantısı da aynı yönle açılır."""
import base64, re, sys
p = sys.argv[1]; html = open(p, encoding="utf-8").read()
m = re.search(r'var b="([A-Za-z0-9+/=]+)";var bin=atob\(b\)', html)
js = base64.b64decode(m.group(1)).decode("utf-8")
assert "__rotaTers" not in js
def bir(a, b):
    global js
    assert js.count(a) == 1, (js.count(a), a[:90]); js = js.replace(a, b)
bir('window.__rotaCiz=async function(el){const M=window.__rotaMap,A=window.__rotaA;if(!M||!A)return!1;const B={lat:+el.getAttribute("data-lat"),lon:+el.getAttribute("data-lon"),ad:decodeURIComponent(el.getAttribute("data-ad")||"")};',
    'window.__rotaCiz=async function(el){const M=window.__rotaMap;let A=window.__rotaA;if(!M||!A||!el)return!1;let B={lat:+el.getAttribute("data-lat"),lon:+el.getAttribute("data-lon"),ad:decodeURIComponent(el.getAttribute("data-ad")||"")};'
    'el!==window.__rotaSon&&(window.__rotaTers=!1);window.__rotaSon=el;'
    'const __ist=s=>/ASH[İI]|[İI]STASYON/i.test(String(s||"")),__vk=s=>/^Vaka/.test(String(s||"")),__oto=__vk(A.ad)&&__ist(B.ad)&&!__vk(B.ad);(__oto!==!!window.__rotaTers)&&([A,B]=[B,A]);')
bir('<a href="#" data-testid="m5-rota-temizle" onclick="return window.__rotaIptal()" style="color:#b91c1c;font-weight:600;text-decoration:none">✖ Temizle</a></div>`;',
    '<a href="#" data-testid="m5-rota-ters" onclick="window.__rotaTers=!window.__rotaTers;window.__rotaCiz(window.__rotaSon);return false" title="Rotayı ters yönde çiz" style="color:#2563eb;font-weight:600;text-decoration:none">⇄ Yönü çevir</a> · <a href="#" data-testid="m5-rota-temizle" onclick="return window.__rotaIptal()" style="color:#b91c1c;font-weight:600;text-decoration:none">✖ Temizle</a></div>`;')
bir('<div style="color:#6b7280;font-size:11px">Normal araç hızıyla tahmin (ambulans değil) · Kuş uçuşu ${kus.replace(".",",")} km</div>',
    '<div style="color:#6b7280;font-size:11px">Normal araç hızıyla tahmin (ambulans değil) · Kuş uçuşu ${kus.replace(".",",")} km${__ist(A.ad)&&__vk(B.ad)?" · Yön: istasyondan vakaya (tek yönlü yollara uyar)":""}</div>')
html = html[:m.start(1)] + base64.b64encode(js.encode("utf-8")).decode() + html[m.end(1):]
open(p, "w", encoding="utf-8").write(html); print("ROTAYON_OK")
