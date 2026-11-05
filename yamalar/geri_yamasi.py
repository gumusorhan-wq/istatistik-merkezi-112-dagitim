"""Sürüm 1.0.29: 'Yeni Dosya' artık açık ayı silmez; Excel yükleme ekranında, açık bir ay varsa '← Geri dön' düğmesi
(dosya yüklemeden kaldığı yere döner)."""
import base64, re, sys
p = sys.argv[1]; html = open(p, encoding="utf-8").read()
m = re.search(r'var b="([A-Za-z0-9+/=]+)";var bin=atob\(b\)', html)
js = base64.b64decode(m.group(1)).decode("utf-8")
assert "__UGeri" not in js
def bir(a, b):
    global js
    assert js.count(a) == 1, (js.count(a), a[:90]); js = js.replace(a, b)
KOD = r'''
function __UGeri(){const r=Ge(e=>e.results),pr=Ge(e=>e.processing),cm=Ge(e=>e.currentMonth),sv=Ge(e=>e.setActiveView);if(!r||pr)return null;
  return(0,a().jsx)("button",{type:"button",className:"btn btn-ghost","data-testid":"upload-geri",title:"Dosya yüklemeden açık olan sayfaya dön",style:{marginLeft:"auto",alignSelf:"center"},onClick:()=>sv("dashboard"),children:"← Geri dön"+(cm?" ("+(window.__donemAktif&&window.__donemAktif()?window.__DONEM.etiket:Du(cm))+")":"")})}
window.__UGeri=__UGeri;
'''
bir('function __MahView(P){', KOD + 'function __MahView(P){')
bir('onClick:()=>{G(),Z("upload")},"data-testid":"btn-new-upload"', 'onClick:()=>{Z("upload")},"data-testid":"btn-new-upload"')
A0='(0,a().jsx)("div",{className:"dash-header",children:(0,a().jsxs)("div",{className:"dash-title",children:[(0,a().jsx)("h1",{children:"Excel Analizi"}),'
i0=js.index(A0); k=js.index('"})]})}),',i0)+len('"})]})}),')
assert k-i0<400
seg=js[i0:k]; js=js[:i0]+'(0,a().jsxs)("div",{className:"dash-header",children:['+seg[len('(0,a().jsx)("div",{className:"dash-header",children:'):-len('})}),')]+'}),(0,a().jsx)(window.__UGeri,{})]}),'+js[k:]
html = html[:m.start(1)] + base64.b64encode(js.encode("utf-8")).decode() + html[m.end(1):]
open(p, "w", encoding="utf-8").write(html); print("GERI_OK")
