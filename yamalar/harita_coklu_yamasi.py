"""Sürüm 13.57: Modül 5 › Harita — birden fazla mahalle / ilçe seçimi.
Öneriden (ya da Enter ile) seçilen her mahalle / ilçe süzgece EKLENİR; haritada seçilenlerin hepsinin vakaları kalır ve
harita hepsini sığdıracak şekilde yakınlaşır. Sol alttaki kutuda her seçimin yanında ✖ (tek tek kaldır) ve "Tümünü göster" var.
Arama kutusu seçimden sonra boşalır (sıradaki mahalle yazılabilsin); kutuyu boşaltmak süzgeci artık silmez."""
import base64, re, sys
p = sys.argv[1]; html = open(p, encoding="utf-8").read()
m = re.search(r'var b="([A-Za-z0-9+/=]+)";var bin=atob\(b\)', html)
js = base64.b64decode(m.group(1)).decode("utf-8")
assert "__mfl" not in js
def bir(a, b):
    global js
    assert js.count(a) == 1, (js.count(a), a[:90]); js = js.replace(a, b)

# durum: tek süzgeç → liste; __mf / __smf adları korunur (__smf(v) ekler, __smf(null) hepsini kaldırır)
bir('const[__mf,__smf]=(0,s().useState)(null),t=(0,s().useMemo)(()=>__mf&&__t0?__t0.filter(__mf.f):__t0,[__t0,__mf]);',
    'const[__mfl,__smfl]=(0,s().useState)([]),__mf=(0,s().useMemo)(()=>__mfl.length?{f:r=>__mfl.some(x=>x.f(r)),ad:__mfl.map(x=>x.ad).join(", ")}:null,[__mfl]),'
    '__smf=v=>v?__smfl(l=>l.some(x=>x.ad===v.ad)?l:[...l,v]):__smfl([]),'
    't=(0,s().useMemo)(()=>__mf&&__t0?__t0.filter(__mf.f):__t0,[__t0,__mf]);'
    '(0,s().useEffect)(()=>{const m=i&&i.current;if(!m||__mfl.length<2||!t||!t.length)return;'
    'try{m.fitBounds(Xd().latLngBounds(t.map(e=>[e.lat,e.lon])),{padding:[40,40],maxZoom:16})}catch(e){}},[__mfl]);')
# arama kutusu boşalınca süzgeç silinmez
bir(',e.target.value.trim()||__smf(null)}', '}')
# öneriden seçince kutu boşalır
bir('t&&(t.setView([e.lat,e.lon],16),w(`${e.mahalle} (${e.ilce})`),T(!1),x(!1))',
    't&&(t.setView([e.lat,e.lon],16),w(""),T(!1),x(!1))')
# Enter ile seçince de
bir('if(__smf({f:__p,ad:k.trim()}),x(!1),T(!1),', 'if(__smf({f:__p,ad:k.trim()}),w(""),x(!1),T(!1),')
# sol alt kutu: her seçim ayrı, ✖ ile tek tek kaldırılır
bir('children:[(0,a().jsxs)("span",{children:["Yaln\\u0131z: ",(0,a().jsx)("b",{children:__mf.ad})," \\u2014 ",(t||[]).length.toLocaleString("tr-TR")," vaka"]}),',
    'children:[(0,a().jsxs)("span",{style:{display:"flex",flexWrap:"wrap",alignItems:"center",gap:4,maxWidth:520},children:["Yaln\\u0131z:",'
    '__mfl.map(x=>(0,a().jsxs)("span",{style:{display:"inline-flex",alignItems:"center",gap:4,background:"rgba(255,255,255,0.14)",borderRadius:6,padding:"1px 6px"},children:[(0,a().jsx)("b",{children:x.ad}),'
    '(0,a().jsx)("button",{type:"button",title:"Bu se\\xe7imi kald\\u0131r",onClick:()=>__smfl(l=>l.filter(y=>y.ad!==x.ad)),style:{background:"none",border:"none",color:"#fff",cursor:"pointer",padding:0,fontSize:11},children:"\\u2716"})]},x.ad)),'
    '"\\u2014 ",(t||[]).length.toLocaleString("tr-TR")," vaka",(0,a().jsx)("span",{style:{opacity:.7,fontSize:11},children:"(eklemek i\\xe7in yeni mahalle aray\\u0131n)"})]}),')

html = html.replace(m.group(1), base64.b64encode(js.encode("utf-8")).decode("ascii"), 1)
open(p, "w", encoding="utf-8").write(html)
print("harita çoklu seçim yaması uygulandı")
