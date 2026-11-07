"""Sürüm 12.52: Brifing (Slayt 3 Ambulans Durumu) araç bilgileri Teknik modülünden:
model yılı otomatik dolar (yaş tablosu), bu ay vakası olmayan envanter araçları da listeye eklenir (pert / hizmet dışı hariç).
112 içinde gömülüyken /api/teknik/<il>/brifing-araclar okunur; alınamazsa eski davranış. turgos_secici_yamasi.py'den SONRA."""
import base64, re, sys
p = sys.argv[1]; html = open(p, encoding="utf-8").read()
m = re.search(r'var b="([A-Za-z0-9+/=]+)";var bin=atob\(b\)', html)
js = base64.b64decode(m.group(1)).decode("utf-8")
assert "brifing-araclar" not in js
def bir(a, b):
    global js
    assert js.count(a) == 1, (js.count(a), a[:90]); js = js.replace(a, b)

bir('const T=o=>Object.values(o||{}).reduce((s,v)=>s+(v||0),0),pc=',
    'let TEK=null;try{const K_=window.__IM112_KURUM;if(K_&&K_.aktif()){const il_=await K_.hedefIl(),r_=await fetch(`/api/teknik/${encodeURIComponent(il_)}/brifing-araclar`,{credentials:"same-origin"});r_.ok&&(TEK=(await r_.json()).araclar||null)}}catch(e){console.warn("[brifing] Teknik envanteri alınamadı",e)}\n'
    '  if(TEK&&TEK.length&&ARAC){const M_=new Map(TEK.map(a=>[a.kisa,a])),G_=new Set;for(const x of ARAC){const a=M_.get(String(x.plaka).replace(/\\s+/g,"").toLocaleUpperCase("tr-TR"));a&&(x.my=a.model_yili||"",G_.add(a.kisa))}'
    'for(const a of TEK)G_.has(a.kisa)||"Pert"===a.durum||"Hizmet dışı"===a.durum||ARAC.push({plaka:a.plaka,ist:a.gorev_yeri,km:a.son_km||null,n:0,uy:0,my:a.model_yili||"",ek:"Teknik envanteri — bu ay vakası yok"})}\n'
    '  const T=o=>Object.values(o||{}).reduce((s,v)=>s+(v||0),0),pc=')
bir('''["3","Ambulans model yılı (yaş tablosu için)","","'SLAYT 3 Ambulans Durumu' sayfasındaki araç listesine MODEL YILI yazılınca yaş tablosu kendiliğinden dolar"],''',
    '''...(TEK&&TEK.length?[]:[["3","Ambulans model yılı (yaş tablosu için)","","'SLAYT 3 Ambulans Durumu' sayfasındaki araç listesine MODEL YILI yazılınca yaş tablosu kendiliğinden dolar"]]),''')
bir('nt.push("Kişisel veri içermez; yalnızca sayılar.");',
    'TEK&&TEK.length&&nt.push("Ambulans model yılları ve bu ay vakası olmayan araçlar Teknik modülünün araç listesinden alındı ("+TEK.length+" araç); listede olmayan aracın model yılını elle yazın.");nt.push("Kişisel veri içermez; yalnızca sayılar.");')
bir('satir(ws,r,[x.plaka,x.ist,x.n,x.km==null?"":x.km,"",F(', 'satir(ws,r,[x.plaka,x.ist,x.n,x.km==null?"":x.km,x.my||"",F(')
bir('x.uy?"⚠ "+x.uy+" uyarı":""]', 'x.uy?"⚠ "+x.uy+" uyarı":(x.ek||"")]')
html = html[:m.start(1)] + base64.b64encode(js.encode("utf-8")).decode() + html[m.end(1):]
open(p, "w", encoding="utf-8").write(html); print("TEKNIK_BRIFING_OK")
