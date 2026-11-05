"""Sürüm 12.42: vaka noktası en yakın araç yoluna uzaksa uyarı.
Rota motoru noktayı en yakın yola bağlar; köy/orman içinde bu yol çıkmaz bir yol olabilir ve rota kısa görünür.
- Haritadaki rota kutusu: başlangıç/varış noktası yola 250 m'den uzaksa uyarı + noktaya kesikli çizgi.
- Tahmini varış: vaka noktası yola 500 m'den uzaksa tahmin yazılmaz; "hesaplanamayan" listesine nedeniyle girer."""
import base64, re, sys
p = sys.argv[1]; html = open(p, encoding="utf-8").read()
m = re.search(r'var b="([A-Za-z0-9+/=]+)";var bin=atob\(b\)', html)
js = base64.b64decode(m.group(1)).decode("utf-8")
assert "m5-rota-uzak" not in js
def bir(a, b, n=1):
    global js
    assert js.count(a) == n, (js.count(a), a[:90]); js = js.replace(a, b)
bir('const j=await r.json(),rt=j&&j.routes&&j.routes[0];if(rt&&window.__rotaLay===lay){const ll=rt.geometry.coordinates.map(c=>[c[1],c[0]]);L.polyline(ll,{pane:"__rotaPane",color:"#2563eb",weight:5,opacity:.85}).addTo(lay);',
    'const j=await r.json(),rt=j&&j.routes&&j.routes[0];if(rt&&window.__rotaLay===lay){const ll=rt.geometry.coordinates.map(c=>[c[1],c[0]]);L.polyline(ll,{pane:"__rotaPane",color:"#2563eb",weight:5,opacity:.85}).addTo(lay);'
    'const __wp=(j.waypoints||[]).map(x=>Math.round(x&&x.distance||0)),__uz=Math.max(0,...__wp);if(__uz>250&&ll.length){__wp[0]>250&&L.polyline([[A.lat,A.lon],ll[0]],{pane:"__rotaPane",color:"#b45309",weight:3,dashArray:"5 6"}).addTo(lay);__wp[__wp.length-1]>250&&L.polyline([ll[ll.length-1],[B.lat,B.lon]],{pane:"__rotaPane",color:"#b45309",weight:3,dashArray:"5 6"}).addTo(lay)}')
bir('· Yön: istasyondan vakaya (tek yönlü yollara uyar)":""}</div>`+son);ok=!0}',
    '· Yön: istasyondan vakaya (tek yönlü yollara uyar)":""}</div>`+(__uz>250?`<div data-testid="m5-rota-uzak" style="color:#b45309;font-size:11.5px;margin-top:4px;font-weight:600">⚠ ${__wp[0]>=__wp[__wp.length-1]?"Başlangıç (A)":"Varış (B)"} noktası en yakın araç yoluna ${__uz.toLocaleString("tr-TR")} m uzak. Rota o yolun ucuna kadar çizildi (kesikli çizgi: yolsuz kalan kısım); gerçek yol daha uzun olabilir — Google Haritalar ile karşılaştırın.</div>`:"")+son);ok=!0}')
bir('const j=await r.json(),du=j.durations&&j.durations[0]||[],di=j.distances&&j.distances[0]||[];',
    'const j=await r.json(),du=j.durations&&j.durations[0]||[],di=j.distances&&j.distances[0]||[],dz=(j.destinations||[]).map(x=>x&&x.distance||0);')
bir('c=null==sn?null:{yol:Math.round(sn),km:null==km?null:Math.round(km/100)/10}',
    'c=null==sn?null:{yol:Math.round(sn),km:null==km?null:Math.round(km/100)/10,uz:Math.round(dz[x+1]||0)}')
bir('c?(sonuc.set(e,{...c,sn:AMB(e,c.yol),...ek}),ozet.hesap++):eksik.push({e,neden:"rota bulunamadı (yol ağına uzak nokta)"})',
    'c&&!(c.uz>500)?(sonuc.set(e,{...c,sn:AMB(e,c.yol),...ek}),ozet.hesap++):eksik.push({e,neden:c?"vaka noktası en yakın araç yoluna 500 m\'den uzak (tahmin güvenilmez)":"rota bulunamadı (yol ağına uzak nokta)"})', 2)
html = html[:m.start(1)] + base64.b64encode(js.encode("utf-8")).decode() + html[m.end(1):]
open(p, "w", encoding="utf-8").write(html); print("YOLUZAK_OK")
