"""Sürüm 13.68: telefonda modül başlığındaki İstasyon ve Dönem pencereleri ekran dışında açılıyordu (pencere düğmenin
sağ kenarına hizalanıyor, düğme yatay kayan sekme satırında ekranın dışında kalabiliyordu). Dar ekranda (< 640 px)
pencereler artık ekranın altında tam genişlikte açılır (alt sayfa); geniş ekranda pencere ekranın içinde kalacak
şekilde sınırlanır."""
import base64, re, sys
p = sys.argv[1]; html = open(p, encoding="utf-8").read()
m = re.search(r'var b="([A-Za-z0-9+/=]+)";var bin=atob\(b\)', html)
js = base64.b64decode(m.group(1)).decode("utf-8")
assert "__panelDar" not in js
def bir(a, b):
    global js
    assert js.count(a) == 1, (js.count(a), a[:90]); js = js.replace(a, b)
bir('panel=(id,w,...c)=>E("div",{"data-testid":id,style:{position:"fixed",top:rc?Math.round(rc.bottom+6):80,right:rc?Math.max(8,Math.round(window.innerWidth-rc.right)):16,maxHeight:"calc(100vh - "+(rc?Math.round(rc.bottom+20):100)+"px)",overflowY:"auto",zIndex:2000,width:w,',
    'panel=(id,w,...c)=>{const __vw=window.innerWidth,__panelDar=__vw<640;return E("div",{"data-testid":id,"data-dar":__panelDar?"1":"0",style:{position:"fixed",'
    '...(__panelDar?{left:8,right:8,bottom:"calc(8px + env(safe-area-inset-bottom, 0px))",maxHeight:"75vh",width:"auto",boxSizing:"border-box"}'
    ':{top:rc?Math.round(rc.bottom+6):80,right:rc?Math.min(Math.max(8,Math.round(__vw-rc.right)),Math.max(8,__vw-w-8)):16,maxHeight:"calc(100vh - "+(rc?Math.round(rc.bottom+20):100)+"px)",width:w}),'
    'overflowY:"auto",zIndex:2000,')
# kapanış parantezini düzelt: eski ifade "...c);" ile bitiyordu, artık blok gövdesi
bir('boxShadow:"0 12px 30px rgba(0,0,0,.25)"}},...c);\n', 'boxShadow:"0 12px 30px rgba(0,0,0,.25)"}},...c)};\n')
html = html[:m.start(1)] + base64.b64encode(js.encode("utf-8")).decode() + html[m.end(1):]
open(p, "w", encoding="utf-8").write(html); print("MOBIL_PANEL_OK")
