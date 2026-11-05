"""Sürüm 12.43 (Aşama 2, 1. adım): hesap sonucuna birleştirme için ham alanlar (__sn, __ist, __ay, __gun, __mesg, __km, konumIstat.__ham)
ve aylık sonuçları birleştiren window.__ozetBirlestir. Ekranlar bu alanları kullanmaz; davranış değişmez."""
import base64, re, sys, os
p = sys.argv[1]; html = open(p, encoding="utf-8").read()
m = re.search(r'var b="([A-Za-z0-9+/=]+)";var bin=atob\(b\)', html)
js = base64.b64decode(m.group(1)).decode("utf-8")
assert "__ozetBirlestir" not in js
def bir(a, b, n=1):
    global js
    assert js.count(a) == n, (js.count(a), a[:90]); js = js.replace(a, b)
bir('ortSn:t.toplam>0?Math.round(t.toplamSn/t.toplam):0}', 'ortSn:t.toplam>0?Math.round(t.toplamSn/t.toplam):0,__sn:t.toplamSn}', 2)
bir('toplam:o.toplam,alti:o.alti,oran:o.toplam?Math.round(o.alti/o.toplam*1e3)/10:0}))', 'toplam:o.toplam,alti:o.alti,oran:o.toplam?Math.round(o.alti/o.toplam*1e3)/10:0,__ist:o.ist}))')
bir('istasyon:Object.entries(o.ist).sort((x,z)=>z[1]-x[1])[0][0],toplam:o.t,alti:o.a}))', 'istasyon:Object.entries(o.ist).sort((x,z)=>z[1]-x[1])[0][0],toplam:o.t,alti:o.a,__ist:o.ist}))')
bir('k:{r1:o.r1,r2:o.r2,h1:o.h1,h2:o.h2,i1:o.i1,i2:o.i2,kapali:o.kapali,toplam:o.toplam}})', 'k:{r1:o.r1,r2:o.r2,h1:o.h1,h2:o.h2,i1:o.i1,i2:o.i2,kapali:o.kapali,toplam:o.toplam},__ay:[...AY]})')
bir('vakaBasinaKm:Math.round(10*c)/10,aktifGunSayisi:o.aktifGunler.size})', 'vakaBasinaKm:Math.round(10*c)/10,aktifGunSayisi:o.aktifGunler.size,__gun:[...o.aktifGunler],__mesg:o.mesgTop,__km:o.kmTop})')
bir('return __kiFin(__KI)})()}}', 'return Object.assign(__kiFin(__KI),{__ham:__KI})})()}}')
FN = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'birlestir.js'), encoding='utf-8').read()
bir('function Qu(e,t,r){try{window.__IL', FN + '\nfunction Qu(e,t,r){try{window.__IL')
bir('return{__il:window.__IL?window.__IL.bitir():null,', 'return{__oz:1,__il:window.__IL?window.__IL.bitir():null,')
html = html[:m.start(1)] + base64.b64encode(js.encode("utf-8")).decode() + html[m.end(1):]
open(p, "w", encoding="utf-8").write(html); print("OZET_OK")
