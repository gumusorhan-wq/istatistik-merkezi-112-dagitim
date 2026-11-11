"""Sürüm 13.66: haritada alternatif güzergâhlar. Rota istenince motordan en çok 3 alternatif de istenir
(OSRM alternatives=3). Seçili güzergâh mavi, diğerleri gri kesikli çizilir; üzerine gelince mesafe ve ambulans
tahmini görünür, tıklayınca o güzergâh seçilir. Rota kutusunda bütün güzergâhlar listelenir (en hızlıya göre fark).
Alternatif bulunamazsa kutuda yazılır."""
import base64, re, sys
p = sys.argv[1]; html = open(p, encoding="utf-8").read()
m = re.search(r'var b="([A-Za-z0-9+/=]+)";var bin=atob\(b\)', html)
js = base64.b64decode(m.group(1)).decode("utf-8")
assert "__rotaAltSec" not in js
def bir(a, b):
    global js
    assert js.count(a) == 1, (js.count(a), a[:90]); js = js.replace(a, b)
bir('el!==window.__rotaSon&&(window.__rotaTers=!1);', 'el!==window.__rotaSon&&(window.__rotaTers=!1,window.__rotaAltSec=0);')
bir('onclick="window.__rotaTers=!window.__rotaTers;window.__rotaCiz(window.__rotaSon);return false"',
    'onclick="window.__rotaTers=!window.__rotaTers;window.__rotaAltSec=0;window.__rotaCiz(window.__rotaSon);return false"')
bir('/route/v1/driving/${A.lon},${A.lat};${B.lon},${B.lat}?overview=full&geometries=geojson`',
    '/route/v1/driving/${A.lon},${A.lat};${B.lon},${B.lat}?overview=full&geometries=geojson&alternatives=3`')
bir('const j=await r.json(),rt=j&&j.routes&&j.routes[0];if(rt&&window.__rotaLay===lay){const ll=rt.geometry.coordinates.map(c=>[c[1],c[0]]);L.polyline(ll,{pane:"__rotaPane",color:"#2563eb",weight:5,opacity:.85}).addTo(lay);',
    'const j=await r.json(),__R=(j&&j.routes)||[],__si=(window.__rotaAltSec|0)<__R.length?(window.__rotaAltSec|0):0,rt=__R[__si];if(rt&&window.__rotaLay===lay){'
    'const __dk=x=>Math.max(1,Math.round((window.__tvsAmb?window.__tvsAmb(x.duration,__rbt):x.duration)/60)),__km=x=>(x.distance/1e3).toFixed(1).replace(".",","),__ad=i=>i===0?"En hızlı":"Alternatif "+i;'
    '__R.forEach((x,i)=>{if(i===__si)return;L.polyline(x.geometry.coordinates.map(c=>[c[1],c[0]]),{pane:"__rotaPane",color:"#64748b",weight:5,opacity:.6,dashArray:"9 7"})'
    '.bindTooltip(`${__ad(i)}: ${__km(x)} km · ambulans ~${__dk(x)} dk (seçmek için tıklayın)`,{sticky:!0}).on("click",()=>{window.__rotaAltSec=i;window.__rotaCiz(window.__rotaSon)}).addTo(lay)});'
    'const ll=rt.geometry.coordinates.map(c=>[c[1],c[0]]);L.polyline(ll,{pane:"__rotaPane",color:"#2563eb",weight:5,opacity:.85}).addTo(lay);'
    'const __alt=__R.length>1?`<div data-testid="m5-rota-alternatif" style="margin:4px 0 2px;font-size:12px;border-top:1px solid #e5e7eb;padding-top:3px">'
    '${__R.map((x,i)=>{const f=__dk(x)-__dk(__R[0]),t=`${__ad(i)}: ${__km(x)} km · ambulans ~${__dk(x)} dk${i>0?` (${f>=0?"+":"−"}${Math.abs(f)} dk)`:""}`;'
    'return i===__si?`<div style="font-weight:700;color:#1d4ed8">● ${t}</div>`:`<div><a href="#" data-testid="m5-rota-alt-${i}" onclick="window.__rotaAltSec=${i};window.__rotaCiz(window.__rotaSon);return false" style="color:#475569;text-decoration:none">○ ${t}</a></div>`}).join("")}'
    '<div style="color:#6b7280;font-size:11px">Gri kesikli çizgiler alternatif yollar; tıklayarak seçebilirsiniz.</div></div>`'
    ':`<div data-testid="m5-rota-alternatif" style="color:#6b7280;font-size:11px;margin-top:2px">Bu iki nokta arasında belirgin bir alternatif yol bulunamadı.</div>`;')
bir('dk</b></div><div style="color:#6b7280;font-size:11px">Ambulans tahmini = ',
    'dk</b></div>${__alt}<div style="color:#6b7280;font-size:11px">Ambulans tahmini = ')
html = html[:m.start(1)] + base64.b64encode(js.encode("utf-8")).decode() + html[m.end(1):]
open(p, "w", encoding="utf-8").write(html); print("ROTA_ALT_OK")
