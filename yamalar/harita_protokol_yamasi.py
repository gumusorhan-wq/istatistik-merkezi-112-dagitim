"""Sürüm 13.57: Modül 5 › Harita arama kutusu KKM protokol numarasını da arar.
Rakam yazılınca öneri listesinde eşleşen protokoller ("KKM 123456 — mahalle · ilçe") önce gelir; seçilen protokol
süzgece eklenir (çoklu seçimle birlikte çalışır) ve harita o vakaya yakınlaşır. Enter da protokolü kapsar."""
import base64, re, sys
p = sys.argv[1]; html = open(p, encoding="utf-8").read()
m = re.search(r'var b="([A-Za-z0-9+/=]+)";var bin=atob\(b\)', html)
js = base64.b64decode(m.group(1)).decode("utf-8")
assert "__protO" not in js
def bir(a, b):
    global js
    assert js.count(a) == 1, (js.count(a), a[:90]); js = js.replace(a, b)

bir('const R=(0,s().useMemo)(()=>{const e=M(k);return e?C.filter(t=>M(t.mahalle).includes(e)||M(t.ilce).includes(e)).sort((e,t)=>t.sayi-e.sayi).slice(0,8):[]},[k,C]);',
    'const R=(0,s().useMemo)(()=>{const e=M(k);if(!e)return[];const __mh=C.filter(t=>M(t.mahalle).includes(e)||M(t.ilce).includes(e)).sort((e,t)=>t.sayi-e.sayi).slice(0,8);'
    'const __q=e.replace(/\\s+/g,"");if(!/\\d{3,}/.test(__q))return __mh;const __protO=[],__g=new Set;for(const r of __t0||[]){const pr=String(r.prot||"");if(!pr||__g.has(pr)||!pr.replace(/\\s+/g,"").includes(__q))continue;__g.add(pr);'
    '__protO.push({__prot:pr,mahalle:"KKM "+pr,ilce:r.mahalle+" \\xb7 "+r.ilce,sayi:1,lat:r.lat,lon:r.lon});if(__protO.length>=8)break}return[...__protO,...__mh].slice(0,10)},[k,C,__t0]);')
bir('onClick:()=>(e=>{const t=i.current;__smf({f:r=>r.ilce===e.ilce&&r.mahalle===e.mahalle,ad:`${e.mahalle} (${e.ilce})`});',
    'onClick:()=>(e=>{const t=i.current;__smf(e.__prot?{f:r=>String(r.prot||"")===e.__prot,ad:"KKM "+e.__prot}:{f:r=>r.ilce===e.ilce&&r.mahalle===e.mahalle,ad:`${e.mahalle} (${e.ilce})`});')
bir('const __p=e=>M(e.mahalle).includes(n)||M(e.ilce).includes(n),',
    'const __p=e=>M(e.mahalle).includes(n)||M(e.ilce).includes(n)||(/\\d{3,}/.test(n)&&String(e.prot||"").replace(/\\s+/g,"").includes(n.replace(/\\s+/g,""))),')
bir('placeholder:"Mahalle veya il\\xe7e ara...","data-testid":"m5-harita-arama-input",style:{padding:"7px 10px",borderRadius:8,border:"1px solid rgba(255,255,255,0.2)",background:"rgba(15,42,68,0.9)",color:"#fff",fontSize:12,width:190}',
    'placeholder:"Mahalle, il\\xe7e ya da KKM protokol ara...",title:"Mahalle / il\\xe7e ad\\u0131 ya da KKM protokol numaras\\u0131 (en az 3 rakam)","data-testid":"m5-harita-arama-input",style:{padding:"7px 10px",borderRadius:8,border:"1px solid rgba(255,255,255,0.2)",background:"rgba(15,42,68,0.9)",color:"#fff",fontSize:12,width:240}')
html = html.replace(m.group(1), base64.b64encode(js.encode("utf-8")).decode("ascii"), 1)
open(p, "w", encoding="utf-8").write(html)
print("harita protokol yaması uygulandı")
