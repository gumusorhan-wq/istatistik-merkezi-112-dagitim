"""Sürüm 13.45 (kullanıcı kararı 08.11.2026): bütün ambulans simgelerinde artı yerine HİLAL. 🚑 emojisi (artılı) yerine
112'deki ortak hilalli ambulans çizimi (components/AmbulansIkon.js ile aynı). anasayfa_yamasi.py'den SONRA."""
import base64, re, sys
p = sys.argv[1]; html = open(p, encoding="utf-8").read()
m = re.search(r'var b="([A-Za-z0-9+/=]+)";var bin=atob\(b\)', html)
js = base64.b64decode(m.group(1)).decode("utf-8")
assert "__ambAy" not in js

YOL = ["M14 18V6a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2v11a1 1 0 0 0 1 1h2",
       "M19 18h2a1 1 0 0 0 1-1v-3.28a1 1 0 0 0-.684-.948l-1.923-.641a1 1 0 0 1-.578-.502l-1.539-3.076A1 1 0 0 0 16.382 8H14",
       "M9 18h6"]
HILAL = "M9.573 8.057A2.5 2.5 0 1 0 9.573 11.943A2 2 0 1 1 9.573 8.057Z"
def svg(b=16):
    return (f"<svg __ambAy xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' width='{b}' height='{b}' fill='none' stroke='currentColor' stroke-width='2' "
            "stroke-linecap='round' stroke-linejoin='round' aria-hidden='true' style='vertical-align:-0.18em'>"
            + "".join(f"<path d='{d}'/>" for d in YOL) + f"<path d='{HILAL}' fill='currentColor' stroke='none'/><circle cx='17' cy='18' r='2'/><circle cx='7' cy='18' r='2'/></svg>")


def bir(a, b, n=1):
    global js
    assert js.count(a) == n, (js.count(a), a[:80]); js = js.replace(a, b)

S = svg()
# 1) rota yazıları (innerHTML / şablon): emoji yerine çizim
bir('<b>🚑 Rota</b>', f'<b>{S} Rota</b>')
bir('white-space:normal">🚑 Rota: ', f'white-space:normal">{S} Rota: ')
# 2) düz metin: emoji kaldırılır (metin kutusu / kılavuz yazısı çizim gösteremez)
bir('value:"🚑 "+(__istS.size?', 'value:""+(__istS.size?')
bir('“🚑 Rota”', '“Rota”')
# 3) İstasyon seçimi düğmesi: çizim
bir('"🚑 ",isEt,ac==="ist"?" ▴":" ▾"', 'E("span",{style:{display:"inline-flex",marginRight:4},dangerouslySetInnerHTML:{__html:"' + S.replace('"', '\\"') + '"}}),isEt,ac==="ist"?" ▴":" ▾"')
# 4) harita: 112 istasyon işareti ve açıklaması
bir('emoji:"\\ud83d\\ude91"', 'emoji:"' + svg(15) + '"', 2)
bir('(0,a().jsx)("span",{children:e.emoji})', '(0,a().jsx)("span",String(e.emoji).indexOf("<svg")===0?{style:{display:"inline-flex"},dangerouslySetInnerHTML:{__html:e.emoji}}:{children:e.emoji})')
js = js.replace("<svg __ambAy ", "<svg data-amb-ay='1' ")
assert "🚑" not in js and "\\ud83d\\ude91" not in js
html = html[:m.start(1)] + base64.b64encode(js.encode("utf-8")).decode("ascii") + html[m.end(1):]
open(p, "w", encoding="utf-8").write(html)
print("ambulans_ay_yamasi: hilalli ambulans")
