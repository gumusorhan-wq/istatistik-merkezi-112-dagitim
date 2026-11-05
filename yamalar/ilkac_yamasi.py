"""Sürüm 12.40: kurum arşivinden ay indiğinde cihazda açık ay yoksa en yeni ay açılır ve Kontrol Paneli'ne geçilir
(girişte aylar inse de ekran Excel Yükle / Arşiv sayfasında bekliyordu). Açık bir ay varken davranış değişmez.
Ortak (Drive) arşiv yolunda da Arşiv sayfasındayken geçiş yapılır."""
import base64, re, sys
p = sys.argv[1]; html = open(p, encoding="utf-8").read()
m = re.search(r'var b="([A-Za-z0-9+/=]+)";var bin=atob\(b\)', html)
js = base64.b64decode(m.group(1)).decode("utf-8")
assert "__kIlkAc" not in js
def bir(a, b):
    global js
    assert js.count(a) == 1, (js.count(a), a[:90]); js = js.replace(a, b)
bir('processError:null}),st.setActiveView&&"archive"!==Ge.getState().activeView&&st.setActiveView("dashboard")}catch(e){console.warn("[ortak] ilk ay açılamadı",e)}}',
    'processError:null}),st.setActiveView&&st.setActiveView("dashboard")}catch(e){console.warn("[ortak] ilk ay açılamadı",e)}}')
bir('function __KurumSync(e) {',
    'async function __kIlkAc(alinan){try{if(Ge.getState().results)return;let L=(alinan||[]).slice().sort().reverse();if(!L.length)L=((await(0,ze.yZ)())||[]).map(r=>r.ym).filter(Boolean).sort().reverse();'
    'for(const ym of L){const r=await(0,ze.tj)(ym);if(Ge.getState().results)return;if(!r||!r.results)continue;const st=Ge.getState();'
    'st.setResults({results:r.results,currentMonth:ym,currentFile:{name:r.fileName||"kurum arşivi",size:r.fileSize||0},cols:r.cols,rawRowCount:r.rawRowCount||0,parsedRows:r.rows||null,allHeaders:r.allHeaders||null,fromArchive:!0,processing:!1,processError:null});'
    'st.setActiveView&&st.setActiveView("dashboard");return}}catch(e){console.warn("[kurum] ilk ay açılamadı",e)}}\n'
    'function __KurumSync(e) {')
bir('(o.alinan.length || o.silinen.length) && (await (t && t()));',
    '(o.alinan.length || o.silinen.length) && (await (t && t())); await __kIlkAc(o.alinan);')
bir('const o = await __HOST.esitle(il, x => setIs(x), secim); await (t && t());',
    'const o = await __HOST.esitle(il, x => setIs(x), secim); await (t && t()); await __kIlkAc(o.alinan);')
html = html[:m.start(1)] + base64.b64encode(js.encode("utf-8")).decode() + html[m.end(1):]
open(p, "w", encoding="utf-8").write(html); print("ILKAC_OK")
