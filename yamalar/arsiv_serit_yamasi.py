"""Sürüm 13.61: 'N ay kurum arşivinde güncel değil' kutusu tablonun sağ alt köşesini kapatıyordu —
alt bilginin hemen üstünde, ortalanmış tek satırlık ince şerit olur (Sonra / Yükle aynı satırda)."""
import base64, re, sys
p = sys.argv[1]; html = open(p, encoding="utf-8").read()
m = re.search(r'var b="([A-Za-z0-9+/=]+)";var bin=atob\(b\)', html)
js = base64.b64decode(m.group(1)).decode("utf-8")
assert "__arsivSerit" not in js
def bir(a, b, say=1):
    global js
    assert js.count(a) == say, (js.count(a), a[:90]); js = js.replace(a, b)
bir('''__h("div", { "data-testid": "kurum-bekleyen", style: { position: "fixed", right: 18, bottom: 18, zIndex: 4e3, background: "#fff", border: "1px solid rgba(23,162,168,0.6)", color: "#0f172a", padding: "12px 14px", borderRadius: 12, fontSize: 13, boxShadow: "0 10px 30px rgba(0,0,0,0.25)", maxWidth: 460 } },
      __h("div", { style: { fontWeight: 600, marginBottom: 8 } }, `🏛 ${bekleyen.length} ay kurum arşivinde güncel değil: ${bekleyen.map(Du).join(", ")}`),
      __h("div", { style: { display: "flex", gap: 8, justifyContent: "flex-end" } },''',
'''__h("div", { "data-testid": "kurum-bekleyen", "data-x": "__arsivSerit", style: { position: "fixed", left: "50%", transform: "translateX(-50%)", bottom: 40, zIndex: 4e3, background: "#fffbeb", border: "1px solid #f59e0b", color: "#78350f", padding: "5px 6px 5px 12px", borderRadius: 8, fontSize: 12.5, boxShadow: "0 4px 14px rgba(0,0,0,0.15)", maxWidth: "calc(100vw - 32px)", display: "flex", alignItems: "center", gap: 10, flexWrap: "wrap" } },
      __h("span", { style: { fontWeight: 600 } }, `🏛 ${bekleyen.length} ay kurum arşivinde güncel değil: ${bekleyen.map(Du).join(", ")}`),
      __h("span", { style: { display: "flex", gap: 6 } },''')
html = html.replace(m.group(1), base64.b64encode(js.encode("utf-8")).decode("ascii"), 1)
open(p, "w", encoding="utf-8").write(html)
print("arşiv şeridi yaması uygulandı")
