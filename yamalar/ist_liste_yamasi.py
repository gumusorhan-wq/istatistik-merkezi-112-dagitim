"""Sürüm 12.45: istasyon süzgeçli çok aylı dönemde (satırlar her ay inerken seçilen istasyonlara süzülür) istasyon seçici
listesi boş kalıyordu ("Eşleşen istasyon yok"). Süzmeden önce tüm istasyonlar sayılır ve D.istListe'ye yazılır. yil_tum_yamasi.py'den SONRA."""
import base64, re, sys
p = sys.argv[1]; html = open(p, encoding="utf-8").read()
m = re.search(r'var b="([A-Za-z0-9+/=]+)";var bin=atob\(b\)', html)
js = base64.b64decode(m.group(1)).decode("utf-8")
assert "__onSuz" in js and "__isSay" not in js
def bir(a, b, n=1):
    global js
    assert js.count(a) == n, (js.count(a), a[:90]); js = js.replace(a, b)
bir('ic&&(r.rows=r.rows.filter(x=>IS.has(String(x[ic]==null?"":x[ic]).trim())),__onSuz=!0)',
    'ic&&(r.rows.forEach(x=>{const v=String(x[ic]==null?"":x[ic]).trim();v&&__isSay.set(v,(__isSay.get(v)||0)+1)}),r.rows=r.rows.filter(x=>IS.has(String(x[ic]==null?"":x[ic]).trim())),__onSuz=!0)')
bir('let __onSuz=!1;', 'let __onSuz=!1;const __isSay=new Map;')
bir('__onSuz&&(P.kaynak=null,P.D&&(P.D.kaynak=null,P.D.istListe=null));',
    '__onSuz&&(P.kaynak=null,P.D&&(P.D.kaynak=null,P.D.istListe=[...__isSay.entries()].sort((a,b)=>a[0].localeCompare(b[0],"tr",{numeric:!0}))));')
html = html[:m.start(1)] + base64.b64encode(js.encode("utf-8")).decode() + html[m.end(1):]
open(p, "w", encoding="utf-8").write(html); print("IST_LISTE_OK")
