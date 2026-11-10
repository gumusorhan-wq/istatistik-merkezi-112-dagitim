"""Sürüm 13.59: KKM eşik aşımı listelerinde İHBAR VEREN sütunu (kullanıcı kararı 10.11.2026: ihbar veren adı artık
silinmez; yalnız Başhekimlik modülü yetkilileri görür). Modül 4'te de KKM Reaksiyon eşik aşanlar listesi (Modül 2'deki gibi)."""
import base64, re, sys
p = sys.argv[1]; html = open(p, encoding="utf-8").read()
m = re.search(r'var b="([A-Za-z0-9+/=]+)";var bin=atob\(b\)', html)
js = base64.b64decode(m.group(1)).decode("utf-8")
assert "ihbarVeren" not in js
def bir(a, b, say=1):
    global js
    assert js.count(a) == say, (js.count(a), a[:90]); js = js.replace(a, b)
# 1) sütun eşlemesi
bir('{key:"kkmAciklama",m:e=>e.startsWith("kkm aciklama")},', '{key:"kkmAciklama",m:e=>e.startsWith("kkm aciklama")},{key:"ihbarVeren",m:e=>e.includes("ihbar veren")},')
# 2) paket hazırlanırken ihbar veren artık yıldızlanmaz
bir('diger=[...veren,...hb(H,"akilli bileklik no")]', 'diger=[...hb(H,"akilli bileklik no")]')
# 3) eşik aşan vaka kayıtları (KKM reaksiyon) ihbar veren adını taşır
bir('kkmReak:me(Hu(k,t.kkmReak)),istReak:me(Hu(k,t.istReak)),', 'kkmReak:me(Hu(k,t.kkmReak)),istReak:me(Hu(k,t.istReak)),...(i===t.kkmReak&&t.ihbarVeren?{ihbarVeren:String(Hu(k,t.ihbarVeren)||"").trim()}:{}),')
bir('tip:"__KKM"===s?String(Hu(g,t.bolgeTipi)||"").trim():s,', 'tip:"__KKM"===s?String(Hu(g,t.bolgeTipi)||"").trim():s,...((n===t.kkmReak||"__KKM"===s)&&t.ihbarVeren?{ihbarVeren:String(Hu(g,t.ihbarVeren)||"").trim()}:{}),')
# 4) ekrandaki eşik aşımı tablosu (Md): İHBAR VEREN sütunu ve aramada
i = js.index('function Md(e){var t,r;let{title:n,threshold:i,gkg:o,')
j = js.index('function ', i + 30)
md = js[i:j]
def mb(a, b):
    global md
    assert md.count(a) == 1, (md.count(a), a[:80]); md = md.replace(a, b)
mb('__ch=(o.exceed||[]).some(e=>void 0!==e.coklu);', '__ch=(o.exceed||[]).some(e=>void 0!==e.coklu),__iv=(o.exceed||[]).some(e=>void 0!==e.ihbarVeren);')
mb('${e.ekip||""} ${e.gecUlasimNedeni||""}', '${e.ekip||""} ${e.ihbarVeren||""} ${e.gecUlasimNedeni||""}')
mb('(0,a().jsx)("th",{children:"EK\\u0130P"}),(0,a().jsx)("th",{children:"B\\xd6LGE"})', '(0,a().jsx)("th",{children:"EK\\u0130P"}),__iv&&(0,a().jsx)("th",{style:{textAlign:"left"},children:"\\u0130HBAR VEREN"}),(0,a().jsx)("th",{children:"B\\xd6LGE"})')
mb('(0,a().jsx)("td",{children:e.ekip}),(0,a().jsx)("td",{children:e.bolge||e.bolgeTipi||e.tip})', '(0,a().jsx)("td",{children:e.ekip}),__iv&&(0,a().jsx)("td",{style:{textAlign:"left"},children:e.ihbarVeren&&!/^\\*+$/.test(e.ihbarVeren)?e.ihbarVeren:"-"}),(0,a().jsx)("td",{children:e.bolge||e.bolgeTipi||e.tip})')
js = js[:i] + md + js[j:]
# 5) Excel: eşik aşımı sayfasında İHBAR VEREN
bir('__nk&&[s.indexOf("SAATTE KM (km/h)"),s.indexOf("KM")]', 'n.exceed.some(e=>void 0!==e.ihbarVeren)&&(s.splice(4,0,"\\u0130HBAR VEREN"),o.forEach((t,x)=>t.splice(4,0,n.exceed[x].ihbarVeren||"")),l&&l.widths&&l.widths.splice(4,0,26)),__nk&&[s.indexOf("SAATTE KM (km/h)"),s.indexOf("KM")]')
# 6) Modül 4: KKM Reaksiyon eşik aşanlar (ekran + Excel)
bir('"gkg15"===n&&(0,a().jsx)(Md,{title:"KKM Reaksiyon",threshold:120,gkg:t.gkg15})', '"gkg15"===n&&(0,a().jsx)(Md,{title:"KKM Reaksiyon",threshold:120,gkg:t.gkg15,showExceed:!0,hideKmAciklama:!0})')
bir('rf(n,"M4 - KKM","M4 Nakil KKM Reaksiyon",e.m4.gkg15)', 'rf(n,"M4 - KKM","M4 Nakil KKM Reaksiyon",e.m4.gkg15,{showExceed:!0,noKm:!0})')
html = html.replace(m.group(1), base64.b64encode(js.encode("utf-8")).decode("ascii"), 1)
open(p, "w", encoding="utf-8").write(html)
print("ihbar veren yaması uygulandı")
