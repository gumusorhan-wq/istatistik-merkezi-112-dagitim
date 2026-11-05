"""Sürüm 12.44: dönem seçicide her yılın satırında "Tümünü seç" düğmesi (yılın bütün mevcut ayları; hepsi seçiliyse "Yılı çıkar")."""
import base64, re, sys
p = sys.argv[1]; html = open(p, encoding="utf-8").read()
m = re.search(r'var b="([A-Za-z0-9+/=]+)";var bin=atob\(b\)', html)
js = base64.b64decode(m.group(1)).decode("utf-8")
assert "donem-yil-tum-" not in js
a = '`(${tum.filter(x=>x.slice(0,4)===y).length} ay)`)),'
assert js.count(a) == 1
js = js.replace(a, a + 'E("button",{type:"button","data-testid":"donem-yil-tum-"+y,onClick:()=>yilTik(y),disabled:!!dur,'
    'style:{marginLeft:"auto",marginBottom:4,fontSize:11.5,fontWeight:700,padding:"3px 10px",borderRadius:6,cursor:"pointer",'
    'border:"1px solid var(--turquoise, #17a2a8)",background:"transparent",color:"var(--turquoise, #17a2a8)"}},'
    'tum.filter(x=>x.slice(0,4)===y).every(x=>S.has(x))?"\\u2715 Y\\u0131l\\u0131 \\xe7\\u0131kar":"\\u2713 T\\xfcm\\xfcn\\xfc se\\xe7"),')
html = html[:m.start(1)] + base64.b64encode(js.encode("utf-8")).decode() + html[m.end(1):]
open(p, "w", encoding="utf-8").write(html); print("YILTUM_OK")
