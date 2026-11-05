"""Sürüm 12.40: dönem seçicide yıllar açılır/kapanır (yıl arttıkça panel kalabalıklaşmasın).
Açılışta seçili ayların yılları (seçim yoksa en yeni yıl) açık gelir; ▸/▾ ile açılır, kapalı yılda seçili ay sayısı yazar.
Yıl adına tıklamak eskisi gibi o yılın bütün aylarını seçer/çıkarır."""
import base64, re, sys
p = sys.argv[1]; html = open(p, encoding="utf-8").read()
m = re.search(r'var b="([A-Za-z0-9+/=]+)";var bin=atob\(b\)', html)
js = base64.b64decode(m.group(1)).decode("utf-8")
assert "donem-yil-ac-" not in js
def bir(a, b):
    global js
    assert js.count(a) == 1, (js.count(a), a[:90]); js = js.replace(a, b)
bir('[hata,setHata]=R.useState(null),[,setTik]=R.useState(0);', '[hata,setHata]=R.useState(null),[,setTik]=R.useState(0),[yAc,setYAc]=R.useState(null);')
bir('yillar.length?yillar.map(y=>E("div",{key:y,style:{marginBottom:10}},\n        E("button",{type:"button","data-testid":"donem-yil-"+y,',
    'yillar.length?yillar.map(y=>{const __yD=yAc||new Set(sec.length?sec.map(x=>x.slice(0,4)):yillar.slice(0,1)),__acik=__yD.has(y),__ss=sec.filter(x=>x.slice(0,4)===y).length;'
    'return E("div",{key:y,style:{marginBottom:__acik?10:6}},E("div",{style:{display:"flex",alignItems:"center",gap:6}},'
    'E("button",{type:"button","data-testid":"donem-yil-ac-"+y,onClick:()=>{const b=new Set(__yD);b.has(y)?b.delete(y):b.add(y);setYAc(b)},title:__acik?"Yılı kapat":"Yılın aylarını göster",'
    'style:{fontSize:12,width:22,height:22,lineHeight:"20px",padding:0,borderRadius:6,cursor:"pointer",border:"1px solid var(--border-subtle, rgba(148,163,184,.35))",background:"transparent",color:"var(--text-primary)",marginBottom:4}},__acik?"▾":"▸"),\n'
    '        E("button",{type:"button","data-testid":"donem-yil-"+y,')
bir('`(${tum.filter(x=>x.slice(0,4)===y).length} ay)`)),\n        E("div",{style:{display:"grid",',
    '`(${tum.filter(x=>x.slice(0,4)===y).length} ay)`)),__ss&&!__acik?E("span",{style:{fontSize:11.5,fontWeight:700,color:"var(--turquoise, #17a2a8)",paddingBottom:4}},"· "+__ss+" seçili"):null),\n        __acik&&E("div",{style:{display:"grid",')
bir('"↓":"")}))\n      )):E("div",{style:{fontSize:12,color:"var(--text-muted)"}},"Arşivde ay yok.")',
    '"↓":"")}))\n      )}):E("div",{style:{fontSize:12,color:"var(--text-muted)"}},"Arşivde ay yok.")')
html = html[:m.start(1)] + base64.b64encode(js.encode("utf-8")).decode() + html[m.end(1):]
open(p, "w", encoding="utf-8").write(html); print("YILAC_OK")
